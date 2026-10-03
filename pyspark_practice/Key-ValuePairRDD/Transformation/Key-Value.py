from pyspark import SparkConf, SparkContext
config = SparkConf().setAppName('datvo').setMaster('local[3]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)

rdd = sc.parallelize(['adudu mEo trang caM Sung ngan, nOi saU cOCAcola, GAU truc Tap xe, bUn dau nuoc tuong'])

rdd1 = rdd.flatMap(lambda x: x.split(' '))
print(rdd1.collect())
pairRDD = rdd1.map(lambda x: (len(x), x))
# print(pairRDD.collect())
for pair in pairRDD.collect():
    print(*pair)