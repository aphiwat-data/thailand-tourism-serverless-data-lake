from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
from pyspark.sql.types import DoubleType

spark = SparkSession.builder \
    .appName("build_fact_tourism_metrics") \
    .getOrCreate()

df = spark.read.parquet(
    "s3://aphiwat-tourism-data-lake-dev/processed/tourism_domestic/"
)

fact_df = (
    df
    .withColumn(
        "value_clean",
        regexp_replace(col("value"), ",", "")
    )
    .withColumn(
        "value",
        col("value_clean").cast(DoubleType())
    )
    .filter(col("value").isNotNull())
    .select(
        "year",
        "month",
        "province_eng",
        "variable",
        "value"
    )
)

fact_df.write \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet(
        "s3://aphiwat-tourism-data-lake-dev/curated/fact_tourism_metrics/"
    )

spark.stop()