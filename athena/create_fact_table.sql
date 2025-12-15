CREATE EXTERNAL TABLE IF NOT EXISTS fact_tourism_metrics (
  province_eng string,
  variable string,
  value double
)
PARTITIONED BY (
  year int,
  month int
)
STORED AS PARQUET
LOCATION 's3://aphiwat-tourism-data-lake-dev/curated/fact_tourism_metrics/';