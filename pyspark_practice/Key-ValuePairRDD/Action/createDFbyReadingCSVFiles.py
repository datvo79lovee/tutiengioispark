from pyspark.sql import SparkSession
import pandas as pd
from pathlib import Path

path = Path(__file__).parent.parent.parent/'DATA'/'airports.csv'
spark = SparkSession.builder.appName('datvo')\
    .master('local[2]')\
    .config('spark.executor.memory','2g')\
    .getOrCreate()
spark.read.option('header', True).csv(str(path)).show()
