from pyspark import SparkContext, SparkConf
config = SparkConf().setAppName('dat').setMaster('local[2]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)
data = [1,2,3,4,5,6]
rdd = sc.parallelize(data)
#Yêu cầu: Sử dụng mapPartitions() và hai hàm lambda để nhân mỗi phần tử với 10.

result = rdd.mapPartitions(lambda x: map(lambda i: i * 10, x) )
# print(result.glom().collect())


rdd1 = sc.parallelize([
    ("A", 10),
    ("B", 20),
    ("A", 30),
    ("B", 40)
], 2)

result1 = (
    rdd1
    .map(lambda x: (x[0], x[1] * 2))
    .filter(lambda x: x[1] > 20)
    .reduceByKey(lambda a, b: a + b)
)
print(result1.glom().collect())
