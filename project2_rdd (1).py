from pyspark import SparkContext, SparkConf
import sys
import re
from itertools import combinations

class Project2:
    
    def run(self, inputPath, outputPath, stopwordsPath, k):
        conf = SparkConf().setAppName("project2_rdd").setMaster("local")
        sc = SparkContext(conf=conf)
        inputFile = sc.textFile(inputPath)
        # collects stopwords from the file and adds them into a set.
        stopwords=set(sc.textFile(stopwordsPath).collect())
        

        # i have put the lines of code and functions 
        # in the order in which they are run for ease of reading

        def process(line):
            #this next line split the line after the first comma. So that we can separate the category and headline
            lines =line.split(',',1)
            category,headline = lines[0],lines[1]
            #this regex ignores all the words in headline that are not alphabetical. it also lowers cases all the words in headline
            words = re.split(r'[^a-zA-Z]+',headline.lower())
            #word should not be a stopword and not be an alphabetical word
            alphabetic_words=[word for word in words if word.isalpha()]
            valid_terms=[word for word in alphabetic_words if word not in stopwords]

            return (category, valid_terms)
        process_words = inputFile.map(process)
        #for all valid words (headlines with 3 or more valid words)
        valid_headlines=process_words.filter(lambda x:len(x[1])>=3)
        #find all invalid headslines
        invalid_headlines =process_words.filter(lambda x: len(x[1]) < 3)
        #after finding invalid headlies, maps it to the category and then reducebykey to find the total invalid headlines per category
        invalid_headline_counts = invalid_headlines.map(lambda x:(x[0], 1)).reduceByKey(lambda a,b: a+b)
        
        #converts all headlines into triads

        def make_triads(category_words):
            category, words = category_words
            #makes combinations of alphabetically sorted triads 
            triadss= [tuple(sorted(triad)) for triad in combinations(words,3)]
            return [(category, triad) for triad in triadss]

        triads = valid_headlines.flatMap(make_triads)

        #to calculate the number of triads in each category similar to before with the help of reducebykey and mapping
        triad_count = triads.map(lambda x:((x[0], x[1]),1)).reduceByKey(lambda a,b: a+b)
        #using valid_headslines from earlier for total valid headlines in each category
        valid_headline_count=valid_headlines.map(lambda x:(x[0], 1)).reduceByKey(lambda a, b:a + b)
        # Joinning the triad counts with the total headline counts
        joined = triad_count.map(lambda x:(x[0][0],(x[0][1],x[1]))).join(valid_headline_count)
        #so the output woyuld be ((category, (triad,number of triads in this category)) and valid headline counts)

        # relative freq. x[0] is category, x[1][0][0] is term1,term2,term3 and x[1][0][1], x[1][1] are triad count and total headline in each category count
        relative_frequencies =joined.map(lambda x:(x[0],(x[1][0][0],x[1][0][1] /x[1][1])))
        
        def format_result(rfs):
            category,(triad, rf) =rfs
            triad_str=','.join(triad)
            return f"{category}\t{triad_str}:{rf}"

        results=relative_frequencies.map(format_result)
        # split the result for (category,formatted_result)
        category_result =results.map(lambda x:(x.split('\t')[0],x))
        grouped_by_category = category_result.groupByKey()

        # sort the results for category and take the top k
        def top_k(triads, k):
            sorted_ =sorted(triads,key=lambda y:(-float(y.split(':')[1]),y.split('\t')[1]))
            return sorted_[:k]

        top_k_triads=grouped_by_category.flatMap(lambda x:top_k(list(x[1]),k))
        # format result for invalid text
        invalid_headline_ = invalid_headline_counts.map(lambda x:(x[0],f"{x[0]}\tinvalid line:{x[1]}")).collectAsMap()

        top_k_triads_output =top_k_triads.collect()
        final_output=[]
        #for only unique topk and invalid categories
        categories_from_invalid =set(invalid_headline_.keys())
        categories_top_k =set(x.split('\t')[0] for x in top_k_triads_output)
        #combine topk and invalid text
        all_categories = sorted(categories_from_invalid.union(categories_top_k))

        #print number of invalid lines then triads for each category. invalid first for each category
        for category in all_categories:
            if category in invalid_headline_:
                final_output.append(invalid_headline_[category])
            final_output.extend([line for line in top_k_triads_output if line.startswith(f"{category}\t")])


        sc.parallelize(final_output).coalesce(1).saveAsTextFile(outputPath)
        
        sc.stop()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong arguments")
        sys.exit(-1)
    Project2().run(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))

