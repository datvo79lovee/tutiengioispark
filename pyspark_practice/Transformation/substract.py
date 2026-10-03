from pyspark import SparkConf, SparkContext
config = SparkConf().setAppName('datvo').setMaster('local[2]').set('spark.executor.memory','2g')
sc = SparkContext(conf=config)
text = sc.parallelize(['adudu mEo trang caM Sung ngan, nOi saU cOCAcola, GAU truc Tap xe, bUn dau nuoc tuong']) \
            .flatMap(lambda c: c.split(' '))\
            .map(lambda x: x.upper().strip(','))
# text = sc.parallelize(['adudu mEo trang caM Sung ngan, nOi saU cOCAcola, GAU truc Tap xe, bUn dau nuoc tuong']) \
#             .map(lambda c: c.strip(',').upper().split(' ')).flatMap(lambda x: x)
            
sim = sc.parallelize(['GAU truc TAP xe']).flatMap(lambda x: x.split(' ')).map(lambda x: x.upper().strip(','))
# sim = sc.parallelize(['GAU truc TAP xe']) .map(lambda c: c.strip(',').upper().split(' ')).flatMap(lambda x: x)

print((text.subtract(sim)).collect())

