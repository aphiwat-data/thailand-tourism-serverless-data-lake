# Thailand Tourism Serverless Data Lake (AWS)

## Overview
This project demonstrates an **end-to-end serverless data lake and analytics pipeline**
built on AWS using Thailand domestic tourism data.

The main objective is to showcase **data engineering fundamentals**:
data ingestion, transformation, data modeling, and analytics-ready outputs —
without focusing on dashboards or visualization.

---

## Architecture
Raw Zone (S3, CSV)
→ Processed Zone (S3, Parquet, partitioned by year/month)
→ Curated Zone (Fact table)
→ Analytics Views (Athena)

The pipeline follows a production-style data lake design with clear separation
between raw, processed, and curated layers.

---

## Tech Stack
- **Amazon S3** – Data lake storage
- **AWS Glue** – Serverless ETL using PySpark
- **Amazon Athena** – SQL-based analytics
- **Parquet** – Columnar storage format
- **Partitioning** – Year / Month
- **SQL Views** – Analytics abstraction layer

---

## Data Layers

### Raw Zone
- Original CSV files stored in Amazon S3
- No transformations applied
- Raw data is not committed to GitHub

### Processed Zone
- Cleaned and standardized data
- Converted to Parquet format
- Partitioned by `year` and `month`
- Optimized for analytical queries

### Curated Zone
- Analytics-focused fact table
- Clean numeric metrics
- Designed for aggregation and reporting

---

## Analytics Design
- Fact table contains tourism metrics by:
  - Year
  - Month
  - Province
  - Metric type (tourist count, revenue, ratios)
- SQL views provide:
  - Monthly aggregations
  - KPI-ready structure
  - Easy BI tool integration

---

## Example Query
```sql
SELECT *
FROM vw_tourism_monthly_analytics
WHERE year = 2022
ORDER BY month;

Raw Data Source
	•	Provider: Ministry of Tourism and Sports, Thailand
	•	Dataset: Domestic tourism statistics
	•	Granularity: Monthly, province-level
	•	Time Range: 2019–2023
	•	Original Format: CSV

Data Handling
	•	Full raw data is stored in Amazon S3
	•	GitHub contains only code, documentation, and small sample files
	•	ETL logic is implemented using AWS Glue (PySpark)

⸻

Project Scope

This project intentionally stops at the analytics-ready layer.
	•	No dashboard or visualization is included
	•	Focus is placed on:
	•	Data lake architecture
	•	ETL pipeline design
	•	Data modeling and partitioning
	•	Query-ready datasets

The curated data can be consumed by BI tools or notebooks if needed.

⸻

What This Project Demonstrates
	•	End-to-end serverless data pipeline on AWS
	•	Production-style data lake architecture
	•	Clean ETL logic using PySpark
	•	Analytics-oriented data modeling
	•	AWS-native data engineering workflow

    