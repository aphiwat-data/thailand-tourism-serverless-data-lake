from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_date,
    year,
    month
)

RAW_PATH = "s3://aphiwat-tourism-data-lake-dev/raw/tourism_domestic/"
PROCESSED_PATH = "s3://aphiwat-tourism-data-lake-dev/processed/tourism_domestic/"

spark = (
    SparkSession.builder
    .appName("tourism-raw-to-processed")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")


df_raw = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(RAW_PATH)
)


df_clean = (
    df_raw
    # parse date column
    .withColumn("date_parsed", to_date(col("date")))
    # extract partitions
    .withColumn("year", year(col("date_parsed")).cast("string"))
    .withColumn("month", month(col("date_parsed")).cast("string"))
    # drop helper column
    .drop("date_parsed")
)


(
    df_clean
    .write
    .mode("overwrite")              # overwrite entire processed layer
    .partitionBy("year", "month")   # partition strategy
    .parquet(PROCESSED_PATH)
)


spark.stop()