# Performance Tips

- Always define ORDER BY properly
- Use PARTITION BY carefully (not too granular)
- Avoid SELECT *
- Batch inserts instead of single-row inserts
- Prefer pre-aggregation when possible
- Avoid heavy JOINs on large datasets