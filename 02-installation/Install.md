# Quick Start

## Installation

This tutorial uses Docker to run ClickHouse.  
For other installation methods, please refer to the official ClickHouse documentation.

---

## Docker Setup

Create a `docker-compose.yml` file:

```yaml

services:
  clickhouse:
    container_name: myclickhouse
    image: clickhouse/clickhouse-server:latest
    ports:
      - "8123:8123"
      - "9000:9000"
    volumes:
      - ./clickhouse-data:/var/lib/clickhouse/
    restart: unless-stopped

```

## Run ClickHouse

```
docker compose up -d
```

### Exposed Ports

The container exposes two important ports:

- 8123 (HTTP API), Used for HTTP requests and tools like:
- - JDBC / ODBC
- - Web interfaces
- - DBeaver
- 9000 (Native Protocol), Used by:
- - clickhouse-client
- - ClickHouse applications
- - Python drivers (e.g. clickhouse-driver)
- - Internal distributed queries

Your client will choose which port to use depending on the driver.

## Connect to ClickHouse

To access the ClickHouse client inside the container:

```

docker exec -it myclickhouse clickhouse-client

```

## Notes
- Data is persisted locally in ./clickhouse-data
- The container will restart automatically unless stopped
- You can connect using GUI tools like DBeaver or programmatically via Python