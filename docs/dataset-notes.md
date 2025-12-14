# Dataset Notes

## Overview
This dataset contains monthly domestic tourism statistics for all provinces in Thailand
from 2019 to 2023.

The data is provided at province level and is intended for statistical reporting.

## Structure
The dataset is in long format.
Each row represents one metric (`variable`) for one province in one month.

Main columns:
- date
- province_thai
- province_eng
- region_thai
- region_eng
- variable
- value

## Observations
- Data is mostly clean and consistent.
- Multiple metrics are stored in the `variable` column.
- The same province and date appear multiple times with different metrics.

## Data Engineering Notes
Although the dataset is usable, it is not analytics-ready.
For efficient querying and analytics, the data needs to be remodeled into
fact and dimension tables (star schema).

This project focuses on transforming the dataset into a structure
that can be efficiently queried in a data lake environment.