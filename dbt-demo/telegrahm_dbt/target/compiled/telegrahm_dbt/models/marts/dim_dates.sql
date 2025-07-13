

WITH date_range AS (
    SELECT generate_series('2025-07-01'::DATE, '2025-07-31'::DATE, INTERVAL '1 day') AS date
)
SELECT
    date,
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(DAY FROM date) AS day,
    EXTRACT(DOW FROM date) AS day_of_week,
    TO_CHAR(date, 'Day') AS day_name
FROM date_range