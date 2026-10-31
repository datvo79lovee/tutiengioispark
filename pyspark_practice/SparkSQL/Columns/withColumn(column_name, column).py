from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pathlib import Path
from pyspark.sql.functions import udf, split
path = str(Path(__file__).parent.parent.parent/'DATA'/'2015-03-01-17.json')
spark = (SparkSession.builder.appName
         ('datvo')\
    .master('local[4]')\
    .config('spark.executor.memory', '2g')\
    .getOrCreate())

schemaFile = StructType([
    StructField('id', StringType(), True),
    StructField('type', StringType(), True),
    StructField('actor', StructType([
        StructField('id', LongType(), True),
        StructField('login', StringType(), True),
        StructField('gravatar_id', StringType(), True),
        StructField('url', StringType(), True),
        StructField('avatar_url', StringType(), True)
    ]), True),
    StructField('repo', StructType([
        StructField('id', LongType(), True),
        StructField('name', StringType(), True),
        StructField('url', StringType(), True)
    ]), True),
    StructField('payload', StructType([
        StructField('action', StringType(), True),
        StructField('issue', StructType([
            StructField('url', StringType(), True),
            StructField('labels_url', StringType(), True),
            StructField('comments_url', StringType(), True),
            StructField('events_url', StringType(), True),
            StructField('html_url', StringType(), True),
            StructField('id', LongType(), True),
            StructField('number', IntegerType(), True),
            StructField('title', StringType(), True),
            StructField('user', StructType([
                StructField('login', StringType(), True),
                StructField('id', LongType(), True),
                StructField('avatar_url', StringType(), True),
                StructField('gravatar_id', StringType(), True),
                StructField('url', StringType(), True),
                StructField('html_url', StringType(), True),
                StructField('followers_url', StringType(), True),
                StructField('following_url', StringType(), True),
                StructField('gists_url', StringType(), True),
                StructField('starred_url', StringType(), True),
                StructField('subscriptions_url', StringType(), True),
                StructField('organizations_url', StringType(), True),
                StructField('repos_url', StringType(), True),
                StructField('events_url', StringType(), True),
                StructField('received_events_url', StringType(), True),
                StructField('type', StringType(), True),
                StructField('site_admin', BooleanType(), True)
            ]), True),
            StructField('labels', ArrayType(StructType([
                StructField('url', StringType(), True),
                StructField('name', StringType(), True),
                StructField('color', StringType(), True)
            ])), True),
            StructField('state', StringType(), True),
            StructField('locked', BooleanType(), True),
            StructField('assignee', StructType(), True),
            StructField('milestone', StructType(), True),
            StructField('comments', IntegerType(), True),
            StructField('created_at', TimestampType(), True),
            StructField('updated_at', TimestampType(), True),
            StructField('closed_at', TimestampType(), True),
            StructField('body', StringType(), True)
        ]))
    ]), True),
    StructField('public', BooleanType(), True),
    StructField('created_at', TimestampType(), True)
])
from pyspark.sql.functions import col, upper, lit, struct
dataFile = spark.read.schema(schemaFile).json(path)
# dataFile.printSchema()
"""
    withColumn
colName: ten cua cot
column: gia tri cua cot
    - Them 1 cot moi neu colName khong ton tai
    - ghi de len cot hien tai neu colName ton tai
    col(), lit(), struct(): de xac dinh gia tri cua cot
    
"""
# # dataFile.withColumn('actor.id2', lit('dat')).select(col('id'), col('actor.id2')).show()
# dataFileStruct = dataFile.withColumn('actor1',
#     struct(
#         col('actor.id').alias('id'),
#         col('actor.login').alias('login'),
#         col('actor.gravatar_id').alias('gravatar_id'),
#         col('actor.url').alias('url'),
#         col('actor.avatar_url').alias('avatar_url'),
#         lit('dat').alias('id2')
#     )
# ).select(col('id'), col('actor1.id2'))
# dataFileStruct.show()
from pyspark.sql.functions import udf, col, split
import re
data = [['11//02/2025'],
        ['27/11-2021'],
        ['     28.12-2005'],
        ['-31:03{]1995'],
        ['13~04*2002']]
df = spark.createDataFrame(data, ['date'])

def clean_date(data):
    if data is None: return  None
    date = re.sub(r'[^\d]+', ' ', data).strip()
    day, month, year = re.split(' ', date)
    return {'clean_date': date,'day': day, 'month': month, 'year': year}

udf_clean = udf(clean_date, StructType([
    StructField('clean_date', StringType(), True),
    StructField('day', StringType(), True),
    StructField('month', StringType(), True),
    StructField('year', StringType(), True)
]))
df_clean = df.withColumn('clean_date', udf_clean("date"))\
    .select(col('clean_date'),col('clean_date.day'), col('clean_date.month'), col('clean_date.year'))
df_clean.show(truncate=False)


