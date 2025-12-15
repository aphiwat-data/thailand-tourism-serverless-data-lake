CREATE OR REPLACE VIEW vw_tourism_monthly_analytics AS
SELECT
    year,
    month,
    variable,
    CASE
        WHEN variable LIKE 'no_tourist%' THEN 'tourist'
        WHEN variable LIKE 'revenue%' THEN 'revenue'
        WHEN variable LIKE 'ratio%' THEN 'ratio'
        ELSE 'other'
    END AS metric_group,
    SUM(value) AS total_value
FROM fact_tourism_metrics
GROUP BY year, month, variable;