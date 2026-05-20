# ClickHouse Aggregation & JOIN Examples

This section demonstrates advanced ClickHouse queries including:
- Aggregations (`COUNT`, `MAX`)
- Filtering with `WHERE`
- Grouping with `GROUP BY`
- Joining multiple tables
- Derived fields for user activity status

---

## Aggregation Query (Per User Activity)

This query calculates:
- Number of logins per user
- Last login time
- Filters logs after a specific date
- Sorts users by most recent activity

### SQL Query

```sql id="a1k9pz"
SELECT
    ID,
    COUNT(*) AS times_logged_in,
    MAX(time) AS last_logged
FROM logTimes
WHERE time >= '2010-01-01 00:00:00'
GROUP BY ID
ORDER BY last_logged DESC;
```

### Result
```
┌─ID─┬─times_logged_in─┬─────────last_logged─┐
│  2 │               1 │ 2026-05-23 10:41:28 │
│  1 │               2 │ 2026-05-20 22:41:28 │
│  3 │               1 │ 2020-01-01 10:00:00 │
└────┴─────────────────┴─────────────────────┘
```

### JOIN + User Activity Classification
This query joins logTimes with profiles and categorizes users as active or inactive based on last login time.

```
SELECT
    ID,
    name,
    COUNT(*) AS times_logged_in,
    MAX(time) AS last_logged,
    multiIf(
        MAX(time) >= '2023-09-08 18:34:52',
        'active',
        'inactive'
    ) AS activity
FROM logTimes
INNER JOIN profiles ON profiles.ID = logTimes.ID
WHERE time >= '2010-01-01 00:00:00'
GROUP BY
    ID,
    name
ORDER BY last_logged DESC;
```

### Result

```

┌─ID─┬─name──┬─times_logged_in─┬─────────last_logged─┬─activity─┐
│  2 │ Two   │               1 │ 2026-05-23 10:41:28 │ active   │
│  1 │ One   │               2 │ 2026-05-20 22:41:28 │ active   │
│  3 │ Three │               1 │ 2020-01-01 10:00:00 │ inactive │
└────┴───────┴─────────────────┴─────────────────────┴──────────┘

```

## Notes
- COUNT(*) counts number of log entries per user.
- MAX(time) is used to find the latest activity.
- multiIf() is ClickHouse’s conditional function (similar to CASE WHEN).
- INNER JOIN links user metadata with log data.
- GROUP BY is required when using aggregate functions.

## Use Cases
- User activity tracking
- Active vs inactive user segmentation
- Login frequency analytics
- Time-based behavioral analysis
- Joining event data with user profiles

## Ideas 
- Daily/weekly active users (DAU/WAU)
- Retention queries
- Window functions (if needed)
- Materialized views for performance
- Dashboard integration (Grafana / Superset)