from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.compat import jobconf_from_env

class proj1(MRJob):
    def mapper(self,_,lines):
        country,region,city,month, day,year, fahrenheit =lines.strip().split('\t')
        celsius = (float(fahrenheit) - 32) *5/9
        yield f'{city},total,cel',celsius
        yield f'{city},total,count',1
        yield f'{city},{year},cel',celsius
        yield f'{city},{year},count',1
    
    def combiner(self,key,values):
        yield key,sum(values)
    
    def reducer_init(self):
        self.overallsum =0
        self.dailysum =0
        self.avg =0
        self.tau =float(jobconf_from_env('myjob.settings.tau'))

    def reducer(self,keys,values):
        name,year,flag =keys.split(',')
        addedvalues =sum(list(values))
        if year=='total':
            if flag =='cel':
                self.overallsum =addedvalues
            else:
                self.avg=self.overallsum / addedvalues
        else:
            if flag =='cel':
                self.dailysum =addedvalues
            else:
                difference = (self.dailysum/addedvalues)-self.avg
                if difference >self.tau:
                    yield name,f'{year},{difference}'

    SORT_VALUES=True

    def steps(self):
        JOBCONF = { 
            'stream.num.map.output.key.fields':3,
            'mapreduce.map.output.key.field.separator':',',
            'mapreduce.job.output.key.comparator.class':'org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator',
            'mapreduce.partition.keycomparator.options':'-k1,1 -k2,2r -k3,3',
            'mapreduce.partition.keypartitioner.options':'-k1,1'
        }

        return [
            MRStep(jobconf=JOBCONF,mapper=self.mapper,combiner=self.combiner, reducer_init=self.reducer_init, reducer=self.reducer
            )
        ]

if __name__ == '__main__':
    proj1.run()
