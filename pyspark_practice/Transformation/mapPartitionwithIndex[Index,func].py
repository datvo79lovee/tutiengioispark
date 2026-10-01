from pyspark import SparkConf, SparkContext

config = SparkConf().setAppName('dat').setMaster('local[4]').set('spark.executor.memory','2g')

sc = SparkContext(conf=config)

numbersRdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10], 4)
# (1,0),(2,0),(3,0),(4,0),(5,0),(6,1),(7,1),(8,1),(9,1),(10,1)
"""
index: id of partition (ex: 0, 1, 2, ...)
iterator: đối tượng chứa dữ liệu lặp qua tất cả các phần tử trong phân vùng

lambda:
- idx: chi so cua partition (ở bài này là 0,1)
- itr: vong lap qua tat ca cac phan tu trong phan vung
- n: tung phan tu trong partition thi no se tao ra (n, idx) ghep noi lai voi nhau
"""
result = numbersRdd.mapPartitionsWithIndex(lambda idx, itr: [[idx, val] for val in itr])
print(result.collect())
print(numbersRdd.glom().collect())

