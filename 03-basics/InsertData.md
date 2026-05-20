# ClickHouse Data Insertion Examples

This section demonstrates how to insert sample data into the previously created tables: `profiles` and `logTimes`.

---

## Insert Data into `profiles`

The `profiles` table stores simple user information.

### SQL Query

```sql id="p1w7qk"
INSERT INTO profiles VALUES
(1, 'One'),
(2, 'Two'),
(3, 'Three');
```

### Results
```sql
Ok.

3 rows in set. Elapsed: 0.016 sec.
```

## Insert Data into logTimes

The logTimes table stores timestamps associated with user IDs. It demonstrates usage of:

- now() function
- Date arithmetic
- Static datetime values

### SQL Query

```sql
INSERT INTO logTimes VALUES
(now(), 1),
(now() - 216000, 1),
(now() + 216000, 2),
('2020-01-01 10:00:00', 3),
('2000-01-01 10:00:00', 3);
```

### Results 

```sql
Ok.

5 rows in set. Elapsed: 0.016 sec.
```