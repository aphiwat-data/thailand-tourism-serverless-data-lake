# Curated Layer Plan

## Objective
Provide analytics-ready datasets
that can be directly queried using Athena.

The curated layer contains modeled fact
and dimension tables based on the star schema design.

## Output Tables

### fact_tourism
- Stored in Parquet format
- Partitioned by year and month
- One row per province, month, and metric

Columns:
- date_id
- province_id
- variable_id
- value

### dim_date
- Small reference table
- No partitioning

### dim_province
- Small reference table
- No partitioning

### dim_variable
- Small reference table
- No partitioning

## Folder Structure
curated/tourism_analytics/
  ├── fact_tourism/
  │   └── year=YYYY/month=MM/
  └── dimensions/
      ├── dim_date/
      ├── dim_province/
      └── dim_variable/

## Notes
- Curated data is optimized for read performance.
- Parquet format is used to reduce scan cost in Athena.
- Partitioning is applied only where it provides clear benefit.