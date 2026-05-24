# ClickHouse Query Cheatsheet

## Basic SELECT
SELECT * FROM table_name;

## Filtering
SELECT * FROM table_name
WHERE user_id = 123;

## Aggregation
SELECT
    user_id,
    count() AS total
FROM events
GROUP BY user_id;

## Sorting
ORDER BY created_at DESC;

## Limit
LIMIT 10;

## DISTINCT
SELECT DISTINCT user_id FROM events;