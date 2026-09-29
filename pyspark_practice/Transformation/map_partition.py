from pyspark import SparkContext, SparkConf

import time
from random import Random
config = SparkConf().setAppName("Datvo").setMaster("local[2]").set("spark.executor.memory","2g")

rc = SparkContext(conf= config)

data = ["dat","tri","vo","dep","trai"]

rdd = rc.parallelize(data)

# def numsPartition(iter):
#     rand = Random(int(time.time()*1000) + Random().randint(0, 1000))
#     return [f"{item}: {rand.randint(1,10000)}" for item in iter]

# result = rdd.mapPartitions(numsPartition)
result = rdd.mapPartitions(lambda item: map(lambda l: f"{l} : {(Random(int(time.time()*1000) + Random().randint(0, 1000))).randint(1,1000)}", item))
print(result.collect())