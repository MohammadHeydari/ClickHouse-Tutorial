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