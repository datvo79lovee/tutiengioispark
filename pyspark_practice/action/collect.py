from pyspark import SparkContext, SparkConf
config = SparkConf().setAppName('dat').setMaster('local[2]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)
print((sc.parallelize([1,2,3,4,5,6,7]).filter(lambda m: m > 5)).collect())