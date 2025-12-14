# Processing Plan (Raw → Processed)

## Objective
Prepare raw tourism data into a clean and consistent format
that can be used for data modeling and analytics.

## Processing Scope
The following steps are applied in the processed layer:

- Standardize column names and data types
- Validate required fields (date, province, variable, value)
- Handle missing or invalid numeric values
- Remove obvious duplicates if any
- Keep data at the same grain (province, month, metric)

No aggregations are performed at this stage.

## Output
Processed data is stored in Parquet format.

Folder structure:
processed/tourism_domestic/
  └── year=YYYY/
      └── month=MM/

## Notes
- Raw data remains unchanged.
- All transformations are reproducible.
- Business logic is applied only in later stages.