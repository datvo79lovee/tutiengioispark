from os import truncate

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pathlib import Path
from pyspark.sql.functions import col, upper
path = str(Path(__file__).parent.parent/'DATA'/'2015-03-01-17.json')
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

jsonFile = spark.read.schema(schemaFile).json(path)
# jsonFile.select('id').show()
# jsonFile.select(col('id')).show()
# jsonFile.select(col('id'), col>...).show()

#   SELECT WITH ALIAS = SQL (as)

# jsonFile.select(col('id').alias('user_id'), col('type').alias('users_type'), col('actor.id')).show()

# SELECT WITH EXPRESSION
# jsonFile.select(col('id')*2, upper(col('type')).alias("upper_type")).show()

#select all
# jsonFile.select('*').show()
jsonFile.select(jsonFile.columns).show()