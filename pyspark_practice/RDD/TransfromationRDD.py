from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("DatVo").setMaster("local[*]").set("spark.executor.memory", "2g")

sc = SparkContext(conf=conf)

l = [1,2,3,4,5,6,7,8,9,10]
rdd = sc.parallelize(l)
print(rdd.collect())

#using transformation 
# squareRDD = rdd.map(lambda i : i * i)
# filterRDD = rdd.filter(lambda x: x > 4)
# print(squareRDD.collect())
# print(filterRDD.collect())
print(rdd.getNumPartitions())
