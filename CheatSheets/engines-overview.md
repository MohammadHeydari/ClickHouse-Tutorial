# ClickHouse Table Engines

## MergeTree (Most important)
- Default engine for large-scale data
- Supports indexing and partitioning

## ReplacingMergeTree
- Keeps latest version of rows

## SummingMergeTree
- Automatically aggregates numeric columns

## AggregatingMergeTree
- Stores pre-aggregated states