from pyspark import SparkConf, SparkContext
config = SparkConf().setAppName('datvo').setMaster('local[3]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)

rdd = sc.parallelize([('79Lovee', 79), ('ahshibas', 68), ('kkkk', 9),('79Lovee', 34), ('79Lovee', 81)])
rdd1 = rdd.groupByKey()
result = rdd1.collect()
for key, val in result:
    print(key, list(val))

bill = rdd.reduceByKey(lambda val1, val2: val1 + val2).collect()
print(bill)
sc.stop()