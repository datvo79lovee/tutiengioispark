from pyspark import SparkContext, SparkConf

config = SparkConf().setAppName("DatVo").setMaster("local[2]").set("spark.executor.memory", "2g")

sc = SparkContext(conf = config)

datafile = sc.textFile("D:\de_rm\pyspark_practice\DATA\data.txt")

flat_map = datafile.flatMap(lambda x: x.split(" "))

print(flat_map.collect())