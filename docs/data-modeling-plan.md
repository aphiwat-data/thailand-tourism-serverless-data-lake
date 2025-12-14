# Data Modeling Plan (Star Schema)

## Objective
Design an analytics-friendly data model
that supports efficient querying and reporting.

The processed tourism data will be remodeled
into a star schema consisting of fact and dimension tables.

## Fact Table

### fact_tourism
Grain: one metric for one province in one month

Columns:
- date_id
- province_id
- variable_id
- value

The fact table stores only numeric measures
and foreign keys to dimension tables.

## Dimension Tables

### dim_date
- date_id
- year
- month
- quarter
- date

### dim_province
- province_id
- province_thai
- province_eng
- region_thai
- region_eng

### dim_variable
- variable_id
- variable_name
- description

## Modeling Notes
- Star schema is chosen for simplicity and query performance.
- Dimensions are kept denormalized.
- The model is optimized for analytical queries, not transactions.