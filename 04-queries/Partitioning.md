# ClickHouse MergeTree & Partitioning Tutorial

This document demonstrates practical usage of ClickHouse MergeTree engines, indexing behavior, and partitioning using real examples.

---

# 1. Basic MergeTree Table

### Create Table
```sql
CREATE TABLE default.research
(
    research_id UInt32,
    name String,
    created_date Date
)
ENGINE = MergeTree
ORDER BY (created_date, research_id);
```

Insert Sample Data

```
INSERT INTO research VALUES
(1, 'Ali', '2020-01-10'),
(2, 'Reza', '2020-01-20'),
(3, 'Sara', '2020-02-05'),
(4, 'Mina', '2020-02-15'),
(5, 'John', '2020-03-01');
```

Check Data Distribution (Parts)

```
SELECT
    name,
    partition
FROM system.parts
WHERE table = 'research'
ORDER BY partition;
```

2. Partitioned MergeTree Table

Create Partitioned Table

```
CREATE TABLE default.researches_partitioned
(
    research_id UInt32,
    name String,
    created_date Date
)
ENGINE = MergeTree
PARTITION BY toYYYYMM(created_date)
ORDER BY (created_date, research_id, name);
```

Insert Data

```
INSERT INTO default.researches_partitioned VALUES
(1, 'Ali', '2020-01-10'),
(2, 'Reza', '2020-01-20'),
(3, 'Sara', '2020-02-05'),
(4, 'Mina', '2020-02-15'),
(5, 'John', '2020-03-01');
```

View Physical Partitions

```
SELECT
    name,
    partition
FROM system.parts
WHERE table = 'researches_partitioned'
ORDER BY partition;
```

Result

```
┌─name─────────┬─partition─┐
│ 202001_1_1_0 │ 202001    │
│ 202002_2_2_0 │ 202002    │
│ 202003_3_3_0 │ 202003    │
└──────────────┴───────────┘
```

Query Optimization & Index Usage
Query with Filtering

```

EXPLAIN indexes = 1
SELECT *
FROM researches_partitioned
WHERE created_date = '2020-02-05';
```

What ClickHouse does:
- Uses MinMax index on created_date
- Uses Partition pruning (only relevant month scanned)
- Uses Primary key index

Key Result Insight

```
EXPLAIN indexes = 1
SELECT *
FROM researches_partitioned
WHERE created_date = '2020-02-05'
```
Results

```
┌─explain───────────────────────────────────────────────────────┐
│ Expression ((Projection + Before ORDER BY))                   │
│   ReadFromMergeTree (default.researches_partitioned)          │
│   Indexes:                                                    │
│     MinMax                                                    │
│       Keys:                                                   │
│         created_date                                          │
│       Condition: (created_date in [18297, 18297])             │
│       Parts: 1/3                                              │
│       Granules: 1/3                                           │
│     Partition                                                 │
│       Keys:                                                   │
│         toYYYYMM(created_date)                                │
│       Condition: (toYYYYMM(created_date) in [202002, 202002]) │
│       Parts: 1/1                                              │
│       Granules: 1/1                                           │
│     PrimaryKey                                                │
│       Keys:                                                   │
│         created_date                                          │
│       Condition: (created_date in [18297, 18297])             │
│       Parts: 1/1                                              │
│       Granules: 1/1                                           │
└───────────────────────────────────────────────────────────────┘
```
### Note: Only a fraction of data is scanned instead of full table.

## Key Observations

**Without Partitioning**
- All parts may be scanned
- Less efficient for time-based queries

**With Partitioning (toYYYYMM)**
- Data is split into monthly partitions
- Queries become faster via partition pruning
- Reduced IO and scan cost

Summary

ClickHouse performance heavily depends on:

- ORDER BY (primary key structure)
- PARTITION BY (data skipping at disk level)
- Index granules (data skipping at block level)

Proper schema design dramatically reduces query cost.


