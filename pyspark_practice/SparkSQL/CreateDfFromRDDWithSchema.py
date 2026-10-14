from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *
from decimal import *
import datetime

from reportlab.lib.utils import TimeStamp
from sympy import true

spark = SparkSession.builder.appName('gatvo')\
    .master('local[2]')\
    .config('spark.executor.memory','2g')\
    .getOrCreate()

# data = [
#     {'id': 1, "name": 'dat'},
#     {'id': 2, "name": 'phuc'},
#     {'id': 3, "name": 'hung'},
#     {'id': 4, "name": 'vi'},
# ]
# data = spark.sparkContext.parallelize([
#     Row(1, 'dat', 21),
#     Row(2, 'phuc', 22),
#     Row(3, 'hung', 23),
#     Row(4, 'vi', 24)
# ])
#
# schema = StructType([
#     StructField('id', IntegerType(), True),
#     StructField('name', StringType(), True),
#     StructField('age', IntegerType(), True)
# ])
#
# df = spark.createDataFrame(data,schema)
# df.show()

"""
    PYSPARK SQL TYPE
        StringType: chuoi ky tu,
        LongType: so nguyen 64 bit,
        IntegerType: so nguyen 32 bit,
        FloatType: so thap phan 32 bit,
        DoubleType: so thap phan 64 bit,
        BooleanType: true/false,
        TimestampType: ngay va gio,
        DateType: nam/thang/ngay,
        DecimalType(precision, scale): do chinh xac cua so thap phan
            - precision: tong chu so
            - scale: so chu so sau dau phay
        ByteType: so nguyen 8 bit
        ShortType: so nguyen 16 bit 
        ========ADVANCE========
        StructType: bieu dien 1 cau truc
        StructField(name, datatype, nullable): bieu dien 1 truong trong StructType
            - name: ten cua truong
            - datatype: kieu du lieu cua truong
            - nullable: co cho phep null khong
        ArrayType(elementType): bieu dien ca mang duoc chi dinh
            - elementType: kieu du lieu cua cac phan tu trong mang
        MapType(keyType, valueType): bieu dien cap khoa key-val
            - keyType: kieu du lieu cua "key"
            - valueType: kieu du lieu  cua gia tri "value"
"""

# data = ([
#     Row(
#         name = 'votridat',
#         age = 21,
#         id = 1,
#         salary = 10000.0,
#         bonus = 5000.79,
#         scores = [1,7,9],
#         attributes = {'dept':'engineering', 'role':'data engineering'},
#         hire_date = datetime.datetime.strptime('2025-12-24', '%Y-%m-%d').date(),
#         last_login = datetime.datetime.strptime('2017-10-15 14:22:22', '%Y-%m-%d %H:%M:%S'),
#         tax_rate = Decimal('12.3456'),
#         is_active = True
#     ),
#     Row(
#         name='anh dep trai',
#         age=28,
#         id=2,
#         salary=100000.0,
#         bonus=50000.79,
#         scores=[6, 9, 7, 9],
#         attributes={'dept': 'engineering', 'role': 'lead data engineering'},
#         hire_date=datetime.datetime.strptime('2025-12-29', '%Y-%m-%d').date(),
#         last_login=datetime.datetime.strptime('2028-15-10 15:10:02', '%Y-%d-%m %H:%M:%S'),
#         tax_rate= Decimal('79.7997'),
#         is_active = False
#     )
# ])
# schema = StructType([
#     StructField('name', StringType(), True),
#     StructField('age', IntegerType(), True),
#     StructField('id', IntegerType(), False),
#     StructField('salary',FloatType(), True),
#     StructField('bonus', FloatType(), True),
#     StructField('scores', ArrayType(IntegerType()), True),
#     StructField('attributes', MapType(StringType(), StringType()), True),
#     StructField('hire_date', DateType(), True),
#     StructField('last_login',TimestampType(), True),
#     StructField('tax_rate', DecimalType(12, 4), True),
#     StructField('is_active', BooleanType(), True)
# ])
# df = spark.createDataFrame(data, schema=schema)
# df.show(vertical=False, truncate=False)
# print(df.collect()[1])
# df.printSchema()
# spark.stop()

spark.range(1, 10).toDF('num').show()