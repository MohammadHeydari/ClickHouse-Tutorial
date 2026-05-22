# ClickHouse Tutorial Project

This repository contains a simple hands-on tutorial for learning ClickHouse using Docker and basic SQL queries.

It includes:
- Table creation examples
- Data insertion
- Basic SELECT queries
- Aggregation and JOIN examples

---

## Setup

### 1. Run ClickHouse with Docker

```bash
docker run -d --name clickhouse-server \
  -p 8123:8123 \
  -p 9000:9000 \
  -v clickhouse_data:/var/lib/clickhouse \
  clickhouse/clickhouse-server:24.1
```

## Connect to ClickHouse client

```
docker exec -it clickhouse-server clickhouse-client
```

## Connect to ClickHouse (From Windows to Linux Server)
This section explains how to connect from a Windows machine (Python) to a ClickHouse server running in Docker on a Linux VM.

```
docker run -d \
  --name clickhouse-server \
  -p 8123:8123 \
  -p 9000:9000 \
  -v clickhouse_data:/var/lib/clickhouse \
  clickhouse/clickhouse-server:24.1
```

### Verify ClickHouse is Running

```
docker ps
```

You should see:

```
clickhouse-server   Up ...
```

### Check Port 9000 (Native Protocol)

```
ss -ltnp | grep 9000
```

Expected:

```
0.0.0.0:9000
```

### Get Linux VM IP Address

```
ip a
```

## Python Test Script (Windows)

Install driver:

```
pip install clickhouse-driver
```

### Create test_clickhouse.py

```
from clickhouse_driver import Client

# your linux vm ip address
HOST = "YOUR-LINUX-IP-HERE"

client = Client(
    host=HOST,        # http port
    port=9000,        # Native port
    user='default',
    password=''
)

print("Connected to ClickHouse!")


result = client.execute("SELECT version()")
print("Version:", result)

client.execute("""
CREATE TABLE IF NOT EXISTS test_table
(
    id Int32,
    name String
)
ENGINE = MergeTree()
ORDER BY id
""")

client.execute("INSERT INTO test_table VALUES", [
    (1, 'Ali'),
    (2, 'Reza'),
    (3, 'Mohammad Ehsan')
])

rows = client.execute("SELECT * FROM test_table")
print("Data:", rows)
```

### Run Test

```
python test_clickhouse.py
```
### Expected Output:

```

Connected to ClickHouse!
Version: [('24.1.8.22',)]
Data: [(1, 'Ali'), (2, 'Reza')]

```

## Purpose

This project is for learning and practicing:

- ClickHouse basics
- SQL analytics
- Time-series style queries
- Simple user activity tracking

## Notes
- Data is persisted using Docker volume
- ClickHouse runs on ports:
- 8123 (HTTP)
- 9000 (native client)

## Useful papers about ClickHouse on the Internet 
- [ClickHouse Basic Tutorial: An Introduction](https://dev.to/hoptical/clickhouse-basic-tutorial-an-introduction-52il)
- [How Clickhouse primary key works and how to choose it](https://medium.com/datadenys/how-clickhouse-primary-key-works-and-how-to-choose-it-4aaf3bf4a8b9)

## Benchmarks

- [ClickBench — a Benchmark For Analytical DBMS](https://benchmark.clickhouse.com/)
- [RTABench a Benchmark For Real Time Analytics](https://rtabench.com/)
- [ClickHouse® for Time Series Scalability Benchmarks](https://altinitydb.medium.com/clickhouse-for-time-series-scalability-benchmarks-e181132a895b)

## Next Steps

You can extend this project with:

- More complex analytics queries
- Real-world datasets
- Dashboard integration (Grafana / Superset)
- FastAPI or backend integration