from pyspark.sql import SparkSession
from pyspark.sql.types import *
import json
from pathlib import Path
path = str(Path(__file__).parent.parent/'DATA'/'2015-03-01-17.json')
spark = SparkSession.builder.appName('datvo')\
    .master('local[4]')\
    .config('spark.executor.memory', '2g')\
    .getOrCreate()
df = spark.read.json(path)
df.printSchema()