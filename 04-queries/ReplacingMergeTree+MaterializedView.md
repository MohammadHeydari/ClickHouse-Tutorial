# ClickHouse ReplacingMergeTree + Materialized View

This guide demonstrates how to use ReplacingMergeTree together with a Materialized View to keep the latest version of records.

## Create Source Table

```
DROP TABLE IF EXISTS inventory;
```
and then 

```
CREATE TABLE inventory
(
    id Int32,
    status String,
    price Int32,
    comment String
)
ENGINE = ReplacingMergeTree()
ORDER BY id;
```

## Create Target Table (Latest State)

```
DROP TABLE IF EXISTS inventory_latest;
```

and then

```
CREATE TABLE inventory_latest
(
    id Int32,
    status String,
    price Int32,
    comment String
)
ENGINE = ReplacingMergeTree()
ORDER BY id;
```

## Create Materialized View

This view aggregates data and keeps only the latest values per id.

```
CREATE MATERIALIZED VIEW inventory_mv
TO inventory_latest
AS
SELECT
    id,
    anyLast(status) AS status,
    anyLast(price) AS price,
    anyLast(comment) AS comment
FROM inventory
GROUP BY id;
```

## Insert Data

```
INSERT INTO inventory VALUES
(233, 'successful', 33000, 'Verified'),
(233, 'successful', 44000, 'Updated'),
(233, 'successful', 50000, 'Latest');
```
## Query Final Result

```
SELECT * FROM inventory_latest;
```

### Result

```
233 | successful | 50000 | Latest
```

### Explanation
- inventory : Raw append-only table (multiple versions per id)
- inventory_mv : Processes data on insert
- inventory_latest : Stores only the latest state

### Important Notes
- ReplacingMergeTree does not guarantee immediate deduplication
- anyLast() returns the latest inserted value (not strictly deterministic)
- Materialized Views only process new inserts

### When to Use This Pattern
- Event sourcing / append-only logs
- Keeping latest state per entity
- Pre-aggregated fast reads