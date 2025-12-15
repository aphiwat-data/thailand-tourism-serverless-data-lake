# Tourism Data Lake Analytics (AWS)

## Overview
This project demonstrates an end-to-end analytics data lake built on AWS
using real tourism data. The pipeline ingests raw CSV data, transforms it
using AWS Glue (PySpark), and enables analytical queries via Amazon Athena.

## Architecture
Raw Zone (S3)
→ Processed Zone (Parquet, partitioned by year/month)
→ Fact Table (Athena)
→ Analytics Views (Aggregated KPIs)

## Tech Stack
- AWS S3 (Data Lake Storage)
- AWS Glue (PySpark ETL)
- Amazon Athena (SQL Analytics)
- Parquet + Partitioning
- SQL Views for BI consumption

## Key Features
- Partitioned Parquet tables (year/month)
- Fact table design for analytics
- Aggregated analytics view (monthly KPIs)
- Metadata embedded for governance

## Example Analytics
- Monthly tourist count
- Revenue by type
- Ratio-based metrics
- Ready for BI / dashboard integration

## Sample Query
```sql
SELECT *
FROM vw_tourism_monthly_analytics
WHERE year = 2022
ORDER BY month;