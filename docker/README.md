# To run Clickhouse container in docker: 

use: 

```
docker compose up -d
```
and then

```
curl http://localhost:8123
```

or

```
docker exec -it clickhouse-server clickhouse-client
```