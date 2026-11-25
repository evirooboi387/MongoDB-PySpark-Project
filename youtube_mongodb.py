import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

mongo_uri = os.environ["MONGODB_URI"]

spark = SparkSession.builder \
    .appName("YouTubeMongoDB") \
    .getOrCreate()

df = spark.read \
    .format("mongodb") \
    .option("connection.uri", mongo_uri) \
    .option("database", "youtube_project") \
    .option("collection", "youtube") \
    .load()

print("YouTube Data:")
df.show(truncate=False)

df_exploded = df.withColumn(
    "item", explode(col("items"))
)

result = df_exploded.filter(
    col("item.id.channelId") == "UCJowOS1R0FnhipXVqEnYU1A"
).select("regionCode")

print("Filtered Region Code:")
result.show()

spark.stop()
