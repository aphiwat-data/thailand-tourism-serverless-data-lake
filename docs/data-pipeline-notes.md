# Data Pipeline Notes

## Dataset
Thailand domestic tourism statistics (2019–2023), monthly provincial data.
Key metrics include tourist numbers, occupancy ratio, and tourism revenue.

## Why this dataset
- Public, structured, time-series data
- Clear grain (province + month)
- Suitable for analytics-oriented data modeling

## Data Flow Overview
Raw data is stored in S3, transformed into analytics-ready tables, and queried via Athena.

Raw → Processed → Curated

## Ingestion
- Source: CSV / Parquet
- Ingested manually for learning purposes
- Stored in S3 raw layer partitioned by year and month

## Processing
- Data cleaned and standardized
- Converted to Parquet
- Partitioned for query efficiency

## Data Model (High-level)
- Fact table: tourism_metrics
- Dimensions: date, province, region

## Output
- Curated tables ready for analytical queries
- Queryable using Amazon Athena