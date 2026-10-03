from pyspark import SparkContext, SparkConf
config = SparkConf().setAppName('dat').setMaster('local[1]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)
rdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10],4)
# def add(lst):
#     tong = 0
#     for i in lst:
#         tong += i
#     return tong
# print(add(rdd.collect()))

print(rdd.glom().collect())

def add(n1: int, n2: int) -> int:
    print(f'n1: {n1}, n2: {n2} => ({n1 + n2})')
    return n1 + n2

print((rdd.reduce(add)))