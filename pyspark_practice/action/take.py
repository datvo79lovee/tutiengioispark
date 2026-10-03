from pyspark import SparkContext, SparkConf
config = SparkConf().setAppName('dat').setMaster('local[2]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)
num = sc.parallelize([1,2,9,4,3,5,6,7,8,9],2)
print(num.take(3))