from pyspark import SparkContext

#create sparkcontext
sc = SparkContext("local", "datvo")

#create object
data = [
    {"id": 1, "name": "dat"},
    {"id": 2, "name": "tri"},
    {"id": 3, "name": "vo"}
]

#create rdd from data
rdd = sc.parallelize(data)
print(rdd.collect()) #in dưới dạng list
print(f"number of list: {rdd.count()}")
print(f"first value of data: {rdd.first()} " )
