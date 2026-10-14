from pyspark.sql import SparkSession
import random

spark = SparkSession.builder.appName('datvo').master('local[2]').config('spark.executor.memory','2g').getOrCreate()

rdd = spark.sparkContext.parallelize(range(0,10)).map(lambda x: (x, random.randint(1,100) * x))
spark.createDataFrame(rdd, ['col1', 'col2']).show()
# print(rdd.collect())
spark.stop()