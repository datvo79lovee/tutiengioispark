from pyspark.sql import SparkSession
from pathlib import Path
path = Path(__file__).parent.parent/'DATA'/'data.txt'

spark = SparkSession.builder.appName('datvo').master('local[2]')\
    .config('spark.executor.memory','2g')\
    .getOrCreate()

textFile = spark.read.text(str(path))
textFile.show(truncate=False)
