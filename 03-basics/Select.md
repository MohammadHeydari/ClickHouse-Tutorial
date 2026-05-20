# ClickHouse SELECT Queries Examples

This section demonstrates how to query data from the `logTimes` table, including basic selection and ordering.

---

## Select All Data

To retrieve all rows from the `logTimes` table:

```sql 
SELECT * FROM logTimes;

```

### Result

┌────────────────time─┬─ID─┐
│ 2026-05-20 22:41:28 │  1 │
│ 2026-05-18 10:41:28 │  1 │
│ 2026-05-23 10:41:28 │  2 │
│ 2020-01-01 10:00:00 │  3 │
│ 2000-01-01 10:00:00 │  3 │
└─────────────────────┴────┘

5 rows in set.

## Order Data by Time (Descending)
To sort results by the time column in descending order:

```sql 
SELECT *
FROM logTimes
ORDER BY time DESC;

```

### Result

┌────────────────time─┬─ID─┐
│ 2026-05-23 10:41:28 │  2 │
│ 2026-05-20 22:41:28 │  1 │
│ 2026-05-18 10:41:28 │  1 │
│ 2020-01-01 10:00:00 │  3 │
│ 2000-01-01 10:00:00 │  3 │
└─────────────────────┴────┘

5 rows in set.

## Notes 
- SELECT * returns all columns from the table.
- ORDER BY time DESC sorts records from newest to oldest.
- ClickHouse performs sorting efficiently using its columnar engine.

## Use Cases
- Viewing event logs chronologically
- Debugging inserted data
- Time-based analysis of user activity
- Preparing data for analytics dashboards

## Ideas you can do 
- WHERE filters (e.g., by ID or time range)
- GROUP BY aggregations
- COUNT() analytics
- JOIN queries between profiles and logTimes