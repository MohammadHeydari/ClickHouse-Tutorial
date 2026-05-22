# ClickHouse MergeTree & Index Usage Example

This guide demonstrates how to:

* Create a table using MergeTree
* Insert large-scale random data
* Analyze query performance using EXPLAIN
* Understand how primary index works

1. Create Table

```
CREATE TABLE default.research
(
    research_id UInt32,
    name String,
    created_date Date
)
ENGINE = MergeTree
ORDER BY (research_id, created_date);
```

2. Insert Sample Data (20000000 rows)

```
INSERT INTO research
SELECT *
FROM generateRandom('research_id UInt32, name String, created_date Date', 7, 77, 1)
LIMIT 20000000;
```

3. Analyze Query with EXPLAIN

```
EXPLAIN indexes = 1
SELECT *
FROM research
WHERE created_date = today();
```

## Sample Output Explanation

```

┌─explain───────────────────────────────────────────┐
│ Expression ((Projection + Before ORDER BY))       │
│   ReadFromMergeTree (default.research)            │
│   Indexes:                                        │
│     PrimaryKey                                    │
│       Keys:                                       │
│         created_date                              │
│       Condition: (created_date in [20595, 20595]) │
│       Parts: 5/5                                  │
│       Granules: 2442/2442                         │
└───────────────────────────────────────────────────┘

```

Key Insights

**Primary Key Usage**

* ClickHouse uses the ORDER BY as the primary index
* Even though the order is (research_id, created_date), it can still filter on created_date

**Granules**
* Data is divided into chunks called granules
* Each granule: 8192 rows
* Granules: 2442/2442 means:
* *  No skipping happened
* * Full scan was required

**Why No Index Pruning?**

Because:

```
ORDER BY (research_id, created_date)
```

But query is:

```
WHERE created_date = today()
```

* The first key (research_id) is missing in filter
* So index is less effective

**Optimization Tip**

For better performance on this query pattern:

```

ORDER BY (created_date, research_id)

```

This allows ClickHouse to skip unnecessary data efficiently.

**Summary**

* MergeTree organizes data using ORDER BY
* Index works best when filtering starts from the first key
* EXPLAIN indexes=1 helps understand performance
* Granules show how much data was scanned

# ClickHouse Index Optimization (ORDER BY Comparison)
## Performance Comparison with Better ORDER BY
### Scenario 2: Optimized ORDER BY

In this section, we recreate the same table but optimize the sorting key to improve query performance.

We compare two scenarios:

- Nonoptimized sorting key
- Optimized sorting key

Table Definition

```
CREATE TABLE research 
( 
    research_id UInt32, 
    name String, created_date Date
) 
ENGINE = MergeTree ORDER BY 
(
    created_date, 
    research_id
);

```

Data Insertion

```
INSERT INTO research SELECT * FROM generateRandom('research_id UInt32, name String, created_date Date', 7, 77, 1) LIMIT 20000000;

```

Query

```
EXPLAIN indexes = 1 SELECT * FROM research WHERE created_date = today();
```

Result

```
Granules: 5/2442
```

### Why This Works

- ClickHouse uses ORDER BY as a primary index.

- It works best when ```WHERE``` clause starts with the first column in ORDER BY

## Key Takeaways
- Always design ORDER BY based on query patterns
- Put most frequently filtered column first
- Use EXPLAIN indexes=1 to verify performance
- Lower granules scanned = faster queries

## Conclusion

By simply changing:

```
(research_id, created_date)
 
```
to

```
(created_date, research_id)
```

We reduced scanned data from:

```2442``` to ```5``` granules

This is a massive performance improvement in real workloads.