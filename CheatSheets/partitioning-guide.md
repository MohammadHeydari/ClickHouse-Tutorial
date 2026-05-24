# Partitioning Guide

## What is partitioning?
Splitting data into smaller chunks for performance.

## Example:
PARTITION BY toYYYYMM(created_at)

## Best practices:
- Use time-based partitioning
- Avoid too many small partitions
- Don't over-partition (bad performance)