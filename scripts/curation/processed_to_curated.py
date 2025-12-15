from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
from pyspark.sql.types import DoubleType

spark = SparkSession.builder \
    .appName("build_fact_tourism_metrics") \
    .getOrCreate()

# อ่าน processed data
df = spark.read.parquet(
    "s3://aphiwat-tourism-data-lake-dev/processed/tourism_domestic/"
)

# 🔥 CLEAN + CAST VALUE
fact_df = (
    df
    # ลบ comma เช่น 1,234,567 → 1234567
    .withColumn(
        "value_clean",
        regexp_replace(col("value"), ",", "")
    )
    # cast เป็น double
    .withColumn(
        "value",
        col("value_clean").cast(DoubleType())
    )
    # เอาเฉพาะแถวที่ cast ได้จริง
    .filter(col("value").isNotNull())
    .select(
        "year",
        "month",
        "province_eng",
        "variable",
        "value"
    )
)

# เขียน curated fact table
fact_df.write \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet(
        "s3://aphiwat-tourism-data-lake-dev/curated/fact_tourism_metrics/"
    )

spark.stop()