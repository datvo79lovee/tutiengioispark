from pyspark import SparkContext, SparkConf
config = SparkConf().setAppName('dat').setMaster('local[2]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)

rdd = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize([5,4,3,2,1])
rdd3 = rdd.union(rdd2).collect()
print(rdd3)