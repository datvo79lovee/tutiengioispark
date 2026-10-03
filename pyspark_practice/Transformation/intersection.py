from pyspark import SparkContext, SparkConf
config = SparkConf().setAppName('dat').setMaster('local[3]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)
rdd = sc.parallelize(['adudu mEo trang caM Sung ngan, nOi saU cOCAcola, GAU truc Tap xe, bUn dau nuoc tuong'])\
        .flatMap(lambda x: x.split(' '))\
        .map(lambda x: x.strip(',.;').lower())

rdd1 = sc.parallelize(['GAU truc TAP xe'])\
            .flatMap(lambda x: x.split())\
            .map(lambda x: x.strip(',;.').lower())

dup = rdd.intersection(rdd1)
print(dup.glom().collect())
print(dup.collect())
print(rdd.subtract(dup).collect())