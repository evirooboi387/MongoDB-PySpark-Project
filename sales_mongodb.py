
import os
from pyspark.sql import SparkSession
# Create Spark session
spark = SparkSession.builder \
    .appName("SalesMongoDB") \
    .getOrCreate()
# Get MongoDB Atlas connection string
mongo_uri = os.environ["MONGODB_URI"]

# Read sales.csv into Spark DataFrame
sales_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("file:///home/takeo/pycharmprojects/PythonProject/MongoDBPyspark/sales.csv")

print("Sales DataFrame:")
sales_df.show()

print("Schema:")
sales_df.printSchema()

# Write DataFrame into MongoDB
sales_df.write \
    .format("mongodb") \
    .mode("append") \
    .option("connection.uri", mongo_uri) \
    .option("database", "youtube_project") \
    .option("collection", "sales") \
    .save()
print("Sales data successfully written to MongoDB Atlas!")
spark.stop()
