from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, to_date

RAW_PATH = "s3://aphiwat-tourism-data-lake-dev/raw/tourism_domestic/year=2019-2023/"
PROCESSED_PATH = "s3://aphiwat-tourism-data-lake-dev/processed/tourism_domestic/"

spark = (
    SparkSession.builder
    .appName("tourism-raw-to-processed")
    .getOrCreate()
)

# Read raw CSV
df = (
    spark.read
    .option("header", "true")
    .csv(RAW_PATH)
)

# Parse date and extract year / month
df_clean = (
    df
    .withColumn("date_parsed", to_date(col("date")))
    .withColumn("year", year(col("date_parsed")))
    .withColumn("month", month(col("date_parsed")))
    .drop("date_parsed")
)

# Write partitioned Parquet
(
    df_clean
    .write
    .mode("overwrite")
    .partitionBy("year", "month")
    .parquet(PROCESSED_PATH)
)

spark.stop()