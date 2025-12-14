# Ingestion Plan

## Data Source
Thailand domestic tourism statistics (2019–2023),
provided as CSV/Parquet files.

The dataset is treated as a batch data source
with monthly updates.

## Ingestion Strategy
- Data is ingested in batch mode.
- Raw files are stored without modification.
- No transformations are applied at this stage.

## Raw Zone Layout
Raw data is stored in Amazon S3 using the following structure:

raw/tourism_domestic/
  └── source=ministry_tourism/
      └── ingestion_date=YYYY-MM-DD/

This layout keeps raw data immutable and traceable.

## Notes
- Raw data is never overwritten.
- Any data quality issues are handled in later processing stages.