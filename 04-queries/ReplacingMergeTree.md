# ReplacingMergeTree Tutorial (ClickHouse)

This section demonstrates how `ReplacingMergeTree` works in ClickHouse using real behavior:  
👉 multiple inserts for the same key + automatic deduplication.

---

## 1. Create Table

```sql
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

## Insert Multiple Versions of the Same Row

```
INSERT INTO inventory VALUES
(233, 'successful', 33000, 'Verified'),
(233, 'successful', 44000, 'Updated'),
(233, 'successful', 50000, 'Latest');
```

## Query Without FINAL (Important Behavior)

```
SELECT * FROM inventory WHERE id = 233;
```

## Result (MergeTree behavior)

```
233 | successful | 50000 | Latest
```

In this case, ClickHouse already returned the latest version from background merges.

## Query With FINAL (Guaranteed Deduplication)

```
SELECT * FROM inventory FINAL WHERE id = 233;
```

## Result

```
233 | successful | 50000 | Latest
```

### Key Insight

ReplacingMergeTree does NOT update rows.

Instead:

- Inserts are stored as separate rows
- Background merge process keeps only the **latest** row per ORDER BY key
- “Latest” is determined by insertion order (unless version column is used)

### Why We See Only One Row

In this example:

- All rows have same id = 233
- ClickHouse collapses duplicates during merge
- Final retained row is the latest inserted version

### Important Notes
- ReplacingMergeTree is not immediate deduplication
- Results depend on background merge process
- FINAL forces merge at query time (can be expensive)
- Best practice: use a version column for deterministic results

### Takeaway

ReplacingMergeTree behaves like a "**event log with automatic cleanup**", not a traditional UPDATE system.

It is ideal for:

- Latest-state tracking
- Log deduplication
- Slowly changing data



