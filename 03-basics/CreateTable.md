# ClickHouse Simple Example (Tables & Schema)

This project demonstrates a basic setup of ClickHouse tables using the `MergeTree` engine. It includes two simple tables and basic SQL operations.

---

## Prerequisites

- ClickHouse server running (Docker or native installation)
- ClickHouse client (`clickhouse-client`) available

---

## Create Database Tables

### 1. Create `profiles` table

This table stores user profile information.

```sql
CREATE TABLE profiles
(
    ID UInt8,
    name String
)
ENGINE = MergeTree
PRIMARY KEY ID;
```

### Create logTimes table

This table stores log timestamps associated with user IDs.

```sql
CREATE TABLE logTimes
(
    time DateTime,
    ID UInt8
)
ENGINE = MergeTree
PRIMARY KEY ID;
```

### List Tables
To verify that tables were created successfully:

```sql
SHOW TABLES;
```

### Expected Output:

```sql

┌─name─────┐
│ logTimes │
│ profiles │
└──────────┘

```

### Notes

- Both tables use the MergeTree engine, which is the most commonly used engine in ClickHouse.
- PRIMARY KEY in ClickHouse is used for data skipping, not strict uniqueness.
- UInt8 is a small integer type (0–255 range), suitable for simple IDs in this example.

### Example Use Cases
- Store user profiles in profiles
- Track events or timestamps in logTimes
