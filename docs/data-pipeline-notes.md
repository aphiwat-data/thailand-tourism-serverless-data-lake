# Data Pipeline Notes

## Dataset
Thailand domestic tourism statistics (2019–2023), monthly data at province level.

Key fields include:
- date (month-level)
- province / region
- metric type (tourists, revenue, occupancy)
- value

The dataset is public and structured, suitable for analytics-oriented processing.

---

## Purpose
This project demonstrates an end-to-end data engineering workflow
using a simple serverless-style data lake on AWS.

The focus is on data flow, structure, and readiness for analytics
rather than visualization or advanced modeling.

---

## Data Flow Overview
Raw data is ingested into Amazon S3, transformed into analytics-ready formats,
and queried using Amazon Athena.

Flow:
Raw (CSV) → Processed (Parquet) → Analytics-ready tables

---

## Raw Layer
- Stored in Amazon S3
- Original CSV files are kept unchanged
- Simple folder structure for easy discovery

Example path: