from pyspark import SparkConf, SparkContext
config = SparkConf().setAppName('datvo').setMaster('local[3]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)

rdd = sc.parallelize(['adudu mEo trang caM Sung ngan, nOi saU cOCAcola, GAU truc Tap xe, bUn dau nuoc tuong, con .meo ;di gap gau truc'])

# rdd1 = rdd.flatMap(lambda x: x.split(' '))\
#             .map(lambda x: x.strip(',.;').lower())
# #chia ra từng phần tử nhỏ
# # print(rdd1.collect())

# rdd2 = rdd1.map(lambda x: (x, len(x)))
# #đưa về dạng (meo, 3)
# # print(rdd2.collect())

# rdd3 = rdd2.reduceByKey(lambda v1, v2: v1 + v2)
# #đưa về (meo, 6)
# # print(rdd3.collect())
# rdd4 = rdd3.map(lambda x: (x[1], x[0])) #(6, meo)
# # print(rdd4.collect())
# rdd5 = rdd4.sortByKey()
# print(rdd5.collect())
rdd_split = rdd.flatMap(lambda x: x.split())
rdd_strip  = rdd_split.map(lambda x: x.strip(',.;').lower())
rdd_char = rdd_strip.map(lambda x: (x, 1))
rdd_reduce = rdd_char.reduceByKey(lambda v1, v2: v1 + v2)
result = rdd_reduce.collect()
for i in result:
    print(i)
sc.stop()