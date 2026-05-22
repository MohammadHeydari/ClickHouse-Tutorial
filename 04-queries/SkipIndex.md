# Skip Index in ClickHouse

Skip Index is one of the powerful optimization mechanisms in ClickHouse designed to reduce the amount of data that needs to be scanned during query execution.

## Intuition

Imagine a book:

The ORDER BY / primary key is like the table of contents.
But what if you want to find information based on a word that is not in the index?

Instead of scanning the entire book, you use sticky notes on pages to quickly skip irrelevant sections.

That is exactly what Skip Index does in ClickHouse.

It helps the database skip entire granules that do not contain the required values, reducing I/O and improving performance.


## When Skip Index is Needed

In ClickHouse, if you filter on a column that is not part of the primary key (ORDER BY), the engine may need to scan a large amount of data.

Example:

```
EXPLAIN indexes = 1
SELECT *
FROM researches_partitioned
WHERE name = 'ali';
```

Result (before Skip Index)

```
┌─explain──────────────────────────────────────────────┐
│ Expression ((Projection + Before ORDER BY))          │
│   ReadFromMergeTree (default.researches_partitioned) │
│   Indexes:                                           │
│     MinMax                                           │
│       Condition: true                                │
│       Parts: 3/3                                     │
│       Granules: 3/3                                  │
│     Partition                                        │
│       Condition: true                                │
│       Parts: 3/3                                     │
│       Granules: 3/3                                  │
│     PrimaryKey                                       │
│       Condition: true                                │
│       Parts: 3/3                                     │
│       Granules: 3/3                                  │
└──────────────────────────────────────────────────────┘
Skip Index: not present or ineffective

```

Meaning:

- All parts and granules are scanned
- No optimization happens for the name column

## Creating a Skip Index

To optimize filtering on a non-key column like name, we can define a Skip Index.

```
ALTER TABLE researches_partitioned
ADD INDEX name_index name TYPE bloom_filter GRANULARITY 1;
```

## Why Bloom Filter?

We use bloom_filter because:

- It works well with high-cardinality string columns
- It quickly determines whether a value might exist in a block3

# Applying the Index on Existing Data

By default, Skip Index is only applied to new data.

To apply it on existing data:

```
ALTER TABLE researches_partitioned
MATERIALIZE INDEX name_index;
```

This ensures that old parts are also indexed.

## Query Behavior After Skip Index

After creating and materializing the index:

```
EXPLAIN indexes = 1
SELECT *
FROM researches_partitioned
WHERE name = 'ali';
```

Result:
```
┌─explain──────────────────────────────────────────────┐
│ Expression ((Projection + Before ORDER BY))          │
│   ReadFromMergeTree (default.researches_partitioned) │
│   Indexes:                                           │
│     MinMax                                           │
│       Condition: true                                │
│       Parts: 3/3                                     │
│       Granules: 3/3                                  │
│     Partition                                        │
│       Condition: true                                │
│       Parts: 3/3                                     │
│       Granules: 3/3                                  │
│     PrimaryKey                                       │
│       Condition: true                                │
│       Parts: 3/3                                     │
│       Granules: 3/3                                  │
│     Skip                                             │
│       Name: name_index                               │
│       Description: bloom_filter GRANULARITY 1        │
│       Parts: 0/3                                     │
│       Granules: 0/3                                  │
└──────────────────────────────────────────────────────┘
```

## Interpretation

Even though the Skip Index is evaluated, ClickHouse decides:

- No granules can be safely eliminated
- All parts must still be scanned

This demonstrates an important concept:

- Skip Index does not guarantee skipping 
- it only enables the possibility of skipping.

### Why Skip Index May Not Work

Skip Index effectiveness depends on:

- Data distribution
- Column selectivity
- Correlation with sorting keys
- Index granularity
- Index type (e.g. bloom_filter, minmax, set)

### Key Takeaways
- Skip Index reduces unnecessary data scans
- It works at granule-level, not row-level
- It is most effective for selective filters
- It may show no effect if data is not discriminative enough

## Summary

- Skip Index in ClickHouse acts as a granule-level filtering mechanism that helps avoid reading irrelevant data parts. 
- However, its effectiveness is highly dependent on data distribution and query patterns.