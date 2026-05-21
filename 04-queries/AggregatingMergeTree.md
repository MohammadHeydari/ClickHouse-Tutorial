# ClickHouse AggregatingMergeTree with Materialized View

This guide demonstrates how to use AggregatingMergeTree together with a Materialized View to precompute aggregations in ClickHouse.

## Create Source Table

```
DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory
(
    id Int32,
    status String,
    price Int32,
    num_items UInt64
)
ENGINE = MergeTree
ORDER BY (id, status);

```

## Create Aggregation Table

This table stores aggregation states, not final values.

```

DROP TABLE IF EXISTS agg_inventory;

CREATE TABLE agg_inventory
(
    id Int32,
    max_price AggregateFunction(max, Int32),
    sum_items AggregateFunction(sum, UInt64)
)
ENGINE = AggregatingMergeTree()
ORDER BY id;

```

## Create Materialized View

```
CREATE MATERIALIZED VIEW agg_inventory_mv
TO agg_inventory
AS
SELECT
    id,
    maxState(price) AS max_price,
    sumState(num_items) AS sum_items
FROM inventory
GROUP BY id;
```

## Important Fix

If you previously created another Materialized View (e.g., using anyLast(comment)), it may still be active and cause errors like:

```
Missing columns: 'comment'
```

Fix:

```

DROP VIEW IF EXISTS inventory_mv;

90e209aed2ad :) DROP VIEW IF EXISTS inventory_mv;

DROP VIEW IF EXISTS inventory_mv

Query id: c633e59b-99aa-4535-80eb-289972ee5416

Ok.

0 rows in set. Elapsed: 0.004 sec.
```

## Insert Data

```

INSERT INTO inventory VALUES
(3, 'ok', 100, 2),
(3, 'ok', 500, 4);

```

## Query Final Aggregated Result

```
SELECT
    id,
    maxMerge(max_price) AS max_price,
    sumMerge(sum_items) AS sum_items
FROM agg_inventory
GROUP BY id;
```

### Result

```
Query id: 46750c32-6877-4b8b-8fd2-ead6e14e177f

┌─id─┬─max_price─┬─sum_items─┐
│  3 │       500 │         6 │
└────┴───────────┴───────────┘

1 row in set. Elapsed: 0.007 sec.

```

### How It Works
- inventory : raw data (append-only)
- agg_inventory_mv : computes aggregation on insert
- agg_inventory : stores aggregation states

### Notes
- AggregatingMergeTree does not store final values, only intermediate states
- You must use Merge functions when querying
- Materialized Views only process new inserts

### Use Cases
- Real-time analytics
- Pre-aggregated dashboards
- High-performance OLAP queries