from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.sql.types import *
import sys
from itertools import combinations

class Project2:
    def run(self, inputPath, outputPath, stopwordsPath, k):
        spark = SparkSession.builder.master("local").appName("project2_df").getOrCreate()
        stopwords_set =set(spark.read.text(stopwordsPath).rdd.map(lambda r: r[0]).collect())
        df =spark.read.option("header", False).csv(inputPath)
        df=df.withColumnRenamed("_c0", "category").withColumnRenamed("_c1", "headline")
        cleaned =df.withColumn("words", split(lower(regexp_replace(col("headline"), r"[^a-zA-Z]+", " ")), r"\s+"))
        # filter out stopwords and non-alphabetic words
        stopwords_broadcast =spark.sparkContext.broadcast(stopwords_set)
        def filter_words(words):
            if words is None:
                return []
            return [word for word in words if word.isalpha() and word not in stopwords_broadcast.value]
        filter_words_udf =udf(filter_words,ArrayType(StringType()))
        cleaned =cleaned.withColumn("filtered_words",filter_words_udf(col("words")))
        # get valid and invalid headlines
        valid_headlines = cleaned.filter(size(col("filtered_words"))>= 3)
        invalid_headlines = cleaned.filter(size(col("filtered_words"))< 3)
        #get the number of invalid headlines
        invalid_count =invalid_headlines.groupBy("category").agg(count(lit(1)).alias("invalid_count"))
        def generate_triad_combinations(words):
            return list(map(lambda x:list(x),combinations(sorted(words),3)))
        generate_triads_udf=udf(generate_triad_combinations,ArrayType(ArrayType(StringType())))
        triads_df=valid_headlines.withColumn("triads",explode(generate_triads_udf(col("filtered_words"))))
        triad_counts =triads_df.groupBy("category","triads").agg(count(lit(1)).alias("triad_count"))
        valid_counts=valid_headlines.groupBy("category").agg(count(lit(1)).alias("valid_count"))
        #find the relative freq.
        relative_freqs =triad_counts.join(valid_counts, "category").withColumn("relative_freq", col("triad_count") / col("valid_count")).select("category", "triads", "relative_freq")
        relative_freqs = relative_freqs.withColumn("triad_str", concat_ws(",", array_sort(col("triads")))).withColumn("result", concat_ws(":", col("triad_str"), col("relative_freq")))
        window_spec = Window.partitionBy("category").orderBy(col("relative_freq").desc(), col("triad_str"))
        #find the top k triads
        top_k_triads = relative_freqs.withColumn("rank", row_number().over(window_spec)).filter(col("rank") <= k).select("category", "result")
        invalid_output = invalid_count.withColumn("sort_order", lit(0)).withColumn("result", concat_ws("\t", col("category"), lit("invalid line:"), col("invalid_count"))).select("category", "result", "sort_order")
        top_k_output = top_k_triads.withColumn("sort_order", lit(1)).select("category", "result", "sort_order")
        combined_output = invalid_output.union(top_k_output).orderBy("category", "sort_order", col("result").desc())
        final_output = combined_output.rdd.map(lambda row: f"{row['category']}\t{row['result']}").collect()
        spark.sparkContext.parallelize(final_output).coalesce(1).saveAsTextFile(outputPath)
        spark.stop()

if __name__ == "__main__":
  if len(sys.argv) != 5:
     print("Wrong arguments")
     sys.exit(-1)
  Project2().run(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))

