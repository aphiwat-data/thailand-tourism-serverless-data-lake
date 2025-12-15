Data Pipeline Notes

Dataset

Thailand domestic tourism data (2019–2023), monthly data by province.
Metrics include tourist counts, revenue, and ratio-based indicators.

⸻

Goal

Build a simple serverless data pipeline on AWS that can take raw CSV data
and turn it into analytics-ready tables.

Focus is on data flow and structure, not dashboards.

⸻

Pipeline Flow

Raw CSV (S3)
→ Glue (Spark)
→ Processed Parquet (year/month partition)
→ Fact table (Athena)
→ Analytics view

Raw Layer
	•	Stored in S3 as CSV
	•	No transformation
	•	Used as the source of truth

Path: s3://aphiwat-tourism-data-lake-dev/raw/tourism_domestic/

Processed Layer
	•	Clean and parse date
	•	Extract year and month
	•	Convert to Parquet
	•	Partition by year/month for faster Athena queries

    Path: s3://aphiwat-tourism-data-lake-dev/processed/tourism_domestic/

    Curated Layer (Fact)
	•	Aggregated monthly metrics
	•	Only numeric values kept
	•	Partitioned by year/month
	•	Used directly for analytics

Table: fact_tourism_metrics

Analytics View

A single view is created to standardize metrics:
	•	Groups metrics (tourist / revenue / ratio)
	•	Provides monthly totals
	•	Ready for BI or further analysis

View: vw_tourism_monthly_analytics

Data Checks
	•	Partition coverage checked for all years
	•	Schema mismatch issues fixed during development
	•	Verified aggregation results in Athena

⸻

Tools
	•	S3
	•	AWS Glue (Spark)
	•	Athena
	•	Parquet + partitioning

⸻

Notes

This project focuses on core data engineering concepts:
ETL design, partitioning, schema handling, and analytics enablement.

No automation or dashboard was added to keep the scope realistic.
