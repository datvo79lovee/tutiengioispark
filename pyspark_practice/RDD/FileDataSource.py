from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("DatVo").setMaster("local[*]").set("spark.executỏ.memory", "2g")
sc = SparkContext(conf=conf)

#doc file
fileRdd = sc.textFile("D:\de_rm\pyspark_practice\DATA\data.txt")
print(fileRdd.collect())
print(f"num of data: {fileRdd.count()}")
print(f"first: {fileRdd.first()}")