from pyspark.sql import SparkSession
from helper import *

#new data to score
path = '/localuser'
filename = path + "/score_data.csv"

spark = SparkSession.builder.getOrCreate()
score_data = spark.read.csv(filename, header=True, inferSchema=True, sep=';')

final_scores_df = score_new_df(score_data)
#final_scores_df.show()
final_scores_df.repartition(1).write.format('csv').mode('overwrite') \
	.options(sep='|', header='true').save(path + "predictions.csv")
