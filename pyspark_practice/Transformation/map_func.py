from pyspark import SparkContext, SparkConf

config = SparkConf().setAppName("Datvo").setMaster("local[2]").set("spark.executor.memory", "2g")


rc = SparkContext(conf = config)

datafile = rc.textFile("D:\de_rm\pyspark_practice\DATA\data.txt")

upper_char = datafile.map(lambda line: line.lower())

for line in upper_char.collect():
    print(line)
# print(({[(SparkContext(conf = config).textFile("D:\de_rm\pyspark_practice\DATA\data.txt"))].map(lambda line: line.upper())}.collect()))