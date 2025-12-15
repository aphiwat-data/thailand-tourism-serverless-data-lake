Thailand Tourism Serverless Data Lake (AWS)

Overview

This project demonstrates an end-to-end serverless analytics data lake on AWS using real Thailand tourism data.

The focus is on data engineering fundamentals:
	•	Data lake design
	•	ETL pipelines
	•	Analytics-ready datasets

The pipeline ingests raw CSV data, processes it with AWS Glue (PySpark), stores optimized Parquet datasets on S3, and enables analytical queries via Amazon Athena.

Architecture
Raw Zone (S3, CSV)
→ Processed Zone (S3, Parquet, partitioned)
→ Curated Zone / Fact Table
→ Analytics Views (Athena)

Each layer is clearly separated to reflect a production-style data lake architecture.

Tech Stack
	•	AWS S3 – Data lake storage (raw / processed / curated)
	•	AWS Glue – Serverless ETL using PySpark
	•	Amazon Athena – SQL-based analytics
	•	Parquet – Columnar storage format
	•	Partitioning – Year / Month
	•	SQL Views – Analytics abstraction layer

⸻

Data Layers

Raw Zone
	•	Original CSV files stored in S3
	•	No transformations applied
	•	Raw data is not committed to GitHub

Processed Zone
	•	Cleaned and standardized data
	•	Converted to Parquet
	•	Partitioned by year and month
	•	Optimized for query performance

Curated Zone
	•	Analytics-focused fact table
	•	Clean schema with numeric metrics
	•	Designed for aggregation and reporting

⸻

Analytics Design
	•	Fact table contains tourism metrics by:
	•	Year
	•	Month
	•	Province
	•	Metric type (tourists, revenue, ratios)
	•	SQL views provide:
	•	Monthly aggregations
	•	KPI-friendly structure
	•	Easy BI tool integration

⸻

Example Analytics Use Cases
	•	Monthly tourist counts
	•	Revenue by tourist type
	•	Ratio-based tourism indicators
	•	Time-series analysis (2019–2023)

    Sample Query
SELECT *
FROM vw_tourism_monthly_analytics
WHERE year = 2022
ORDER BY month;

Raw Data Source

Dataset Information
	•	Provider: Ministry of Tourism and Sports, Thailand
	•	Dataset: Domestic tourism statistics
	•	Granularity: Monthly, province-level
	•	Time Range: 2019–2023
	•	Original Format: CSV

Raw Data Handling
	•	Raw files are stored in Amazon S3 only
	•	GitHub contains:
	•	Sample data (for structure reference)
	•	Data source documentation
	•	ETL logic is implemented in AWS Glue (PySpark)

⸻

Project Scope

This project intentionally stops at the analytics-ready layer.
	•	No dashboard or visualization included
	•	Emphasis on:
	•	Data modeling
	•	ETL reliability
	•	Query performance
	•	Clean data architecture

The curated datasets are ready for downstream consumption by BI tools or notebooks if required.

⸻

What This Project Demonstrates
	•	End-to-end serverless data pipeline
	•	Production-style data lake architecture
	•	Clean ETL logic with PySpark
	•	Analytics-oriented data modeling
	•	AWS-native data engineering workflow