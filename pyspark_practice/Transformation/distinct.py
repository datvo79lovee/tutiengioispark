from pyspark import SparkConf, SparkContext
config = SparkConf().setAppName('datvo').setMaster('local[2]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)

data = ([1,'mot','1',1,2,'hai','ba','79lovee'])
rdd = sc.parallelize(data).distinct().collect()
print(sc.parallelize(data).distinct().collect())