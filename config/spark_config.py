from typing import Optional, List, Dict
import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv
from config.mysql_config import get_mysql_config
from pathlib import Path

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_NAME = os.getenv('MYSQL_DATABASE')
JARS_DIR = PROJECT_ROOT / "jars"

def create_spark_session(
         app_name: str, #ten ung dung spark
         master_url: str = 'local[*]', #xac dinh chay spark o dau
         executor_memory: Optional[str] = '4g', # ram cap cho MOI executor
         executor_cores: Optional[int] = 2, # so cpu core cap cho MOI executor
         driver_memory: Optional[str]= '2g', #ram cap cho driver
         num_executors: Optional[int]= 3, #so executor muon su dung
         jars: Optional[List[str]] = None, #ds file jar
         spark_conf: Optional[Dict[str, str]] = None, #
         log_level: str = 'OFF'
)-> SparkSession:

    builder = SparkSession.builder\
        .appName(app_name)\
        .master(master_url)

    if executor_memory:
        builder.config('spark.executor.memory', executor_memory)

    if executor_cores:
        builder.config('spark.executor.cores', executor_cores)

    if driver_memory:
        builder.config('spark.driver.memory', driver_memory)

    if num_executors:
        builder.config('spark.executor.instances', num_executors)

    ''''
        [
            "mysql-connector-j-26.10.0/mysql-connector-j-26.10.0/mysql-connector-j-26.10.0.jar",
            "mysql-connector-j-26.10.0/mongodb-connector-j-26.10.0/mongodb-connector-j-26.10.0.jar",
            "mysql-connector-j-26.10.0/redis-connector-j-26.10.0/redis-connector-j-26.10.0.jar"

        ]
    '''
    if jars:
        jars_path = ",".join(
            str(JARS_DIR / jar) for jar in jars
        )
        builder.config("spark.jars", jars_path)

    # {'spark.sql.shuffle.partitions': '10'}
    if spark_conf:
        for key, val in spark_conf.items():
            builder.config(key, val)

    spark = builder.getOrCreate()

    spark.sparkContext.setLogLevel(log_level)

    return spark


def connect_to_mysql(spark: SparkSession, table_name: str):
    df = (
        spark.read
        .format("jdbc")
        .option("url", os.getenv("MYSQL_URL"))
        .option("dbtable", table_name)
        .option("user", os.getenv("MYSQL_USER"))
        .option("password", os.getenv("MYSQL_PASSWORD"))
        .option("driver", os.getenv("MY_JDBC"))
        .load()
    )

    return df

if __name__ == '__main__':

    spark = create_spark_session(
        app_name = '79lovee',  # ten ung dung spark
        master_url =  'local[*]',  # xac dinh chay spark o dau
        executor_memory = '4g',  # ram cap cho MOI executor
        executor_cores = 2,  # so cpu core cap cho MOI executor
        driver_memory = '2g',  # ram cap cho driver
        num_executors = 3,  # so executor muon su dung
        jars=["mysql-connector-j-26.10.0.jar"],
        spark_conf = None,  #
        log_level = 'OFF'
    )

    df = connect_to_mysql(
        spark,
        table_name="github_users"
    )
    # data = [['dat', 18], ['79lovee', 21]]
    # df = spark.createDataFrame(data, ['ten', 'tuoi'])
    df.printSchema()
    df.show(5, truncate=False)

    spark.stop()
