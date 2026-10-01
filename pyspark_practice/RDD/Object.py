from pyspark import SparkConf, SparkContext

config = SparkConf().setAppName("datvo").setMaster("local[2]").set("spark.executor.memory","2g")

obj = [
    {"1" : "dat"},
    {"2": "vo"},
    {"tri": 1}
]

cnn = SparkContext(conf= config)
rdd = cnn.parallelize(obj)
print(rdd.collect())


