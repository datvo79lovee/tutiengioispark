from pyspark import SparkConf, SparkContext
config = SparkConf().setAppName('datvo').setMaster('local[3]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)

rdd = sc.parallelize(['adudu mEo trang caM Sung ngan, nOi saU cOCAcola, GAU truc Tap xe, bUn dau nuoc tuong'])

rdd1 = rdd.flatMap(lambda x: x.split(' '))

pairRDD = rdd1.map(lambda x: (len(x.strip(',')), x.strip(',')))
print(pairRDD.collect())
grouByKeyRDD = pairRDD.groupByKey()
# print(grouByKeyRDD.collect())

result = grouByKeyRDD.collect()
for keys in result:
    print(keys)

for key, val in result:
    print(key, list(val))