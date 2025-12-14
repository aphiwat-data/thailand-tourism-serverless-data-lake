import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring

RAW_PATH = "s3://aphiwat-tourism-data-lake-dev/raw/tourism_domestic/year=2019-2023/"
PROCESSED_PATH = "s3://aphiwat-tourism-data-lake-dev/processed/tourism_domestic/"

spark = (
    SparkSession.builder
    .appName("raw-to-processed-tourism")
    .getOrCreate()
)

df = (
    spark.read
    .option("header", "true")
    .csv(RAW_PATH)
)

df_clean = (
    df
    .withColumn("year", substring(col("date"), 1, 4))
    .withColumn("month", substring(col("date"), 6, 2))
)

(
    df_clean
    .write
    .mode("overwrite")
    .partitionBy("year", "month")
    .parquet(PROCESSED_PATH)
)

spark.stop()