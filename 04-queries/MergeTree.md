# ClickHouse MergeTree Tutorial

This guide demonstrates correct usage of different ClickHouse MergeTree engines with clean examples.

---

# 1. Basic MergeTree Table

## Create Table

```sql
CREATE TABLE inventory
(
    id Int32,
    status String,
    price String,
    comment String
)
ENGINE = MergeTree
PRIMARY KEY (id, price)
ORDER BY (id, price, status);
```

## Insert Data

```
INSERT INTO inventory VALUES
(233, 'successful', '33000', 'Verified'),
(233, 'successful', '44000', 'Failed');
```

## Query Data

```
SELECT * FROM inventory WHERE id = 233;
```

## Result

```
233 | successful | 33000 | Verified
233 | successful | 44000 | Failed
```

### Note: MergeTree does NOT deduplicate rows.







