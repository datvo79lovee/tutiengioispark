from pyspark.sql import SparkSession
import re
from pyspark.sql.functions import udf, col
from pyspark.sql.types import *

spark = SparkSession.builder.appName('datvo').master('local[4]').config('spark.executor.memory', '4g').getOrCreate()

data = [['11//02/2025'],
        ['27/11-2021'],
        ['     28.12-2005'],
        ['-31:03{]1995'],
        ['13~04*2002'],
        ['']]
df = spark.createDataFrame(data, ['raw'])
# df.show()

def clean(date):

    if date is None:
        return None

    results = re.sub(r'[^\d]+', ' ', date).strip()

    day_month_year = results.split()

    if len(day_month_year) != 3:

        return {
            'date': day_month_year,
            'day': None,
            'month':  None,
            'year': None
        }

    day, month, year = day_month_year
    return {
        'date': day_month_year,
        'day': day,
        'month': month,
        'year': year
    }

udf_date = udf(clean, StructType([
    StructField('date', ArrayType(StringType()), True),
    StructField('day', StringType(), True),
    StructField('month', StringType(), True),
    StructField('year', StringType(), True)
]))

df_clean = df.withColumn('date_clean', udf_date(col('raw')))\
                .select(
                        col('raw').alias('raw_date'),
                        col('date_clean'),
                        col('date_clean.date').alias('date'),
                        col('date_clean.day').alias('day'),
                        col('date_clean.month').alias('month'),
                        col('date_clean.year').alias('year')
                        )
df_clean.show(truncate=False)
df_clean.printSchema()

