from clickhouse_driver import Client

# your linux vm ip address
HOST = "192.168.224.128"

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