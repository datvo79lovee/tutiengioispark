from pyspark import SparkConf, SparkContext
config = SparkConf().setAppName('datvo').setMaster('local[3]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)

table = sc.parallelize([(100, 111), (101, 112), (102, 113), (103, 114), (104, 115)])
table1 = sc.parallelize([(100, 'abc'), (131, 'vcl'), (100, 113), (103, 440), (104, 9999)])

table_new = table.join(table1)
# print(table_new.collect())

print(table_new.lookup(100) )
