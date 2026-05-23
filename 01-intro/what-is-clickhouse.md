### Intro 

ClickHouse, an open-source Online Analytical Processing (OLAP) database, stands out for its remarkable speed and exceptional performance in various warehousing and analytics scenarios such as analytical and time-series data.
Its rapid growth in popularity is a testament to its high-performance capabilities, earning it a place in the tech stacks of renowned companies such as eBay, Microsoft, Lyft, and IBM etc.
Various benchmarks can be found demonstrating the speed advantage ClickHouse has. For example, ClickHouse has several entries in the benchmarks querying 1.1 billion taxi ride records here:

![ClickHouse](../images/img.png)

At the time of writing, most of the faster performers are databases that can take advantage of GPUs and co-processors with a very large number of cores such as Intel Xeon Phi or NVidia Tesla. These database systems include the likes of BrytlyteDB. An interesting point to note here is that ClickHouse running on a laptop with Intel Core i5 4670K processor, 16GB RAM, and SanDisk SSD has performed faster on this dataset than a 6 node Redshift cluster on one of the four test queries (which is on a smaller dataset). So a single-node ClickHouse running locally on a laptop is quite powerful tool for quick data exploration and analytics.

### Useful Links 

[ClickHouse documentation explaining the design choices behind its performance](https://clickhouse.com/docs/en/concepts/why-clickhouse-is-so-fast?source=post_page-----55315107399a---------------------------------------)

[This benchmark compares ClickHouse with Druid and Rocketship, both in terms of performance and cost](https://altinity.com/blog/clickhouse-nails-cost-efficiency-challenge-against-druid-rockset?source=post_page-----55315107399a---------------------------------------)

[Article on CloudFlare using ClickHouse to replace the old system to handle scale](https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse/?source=post_page-----55315107399a---------------------------------------)

### Feature Highlights
Here are some prominent features of ClickHouse, which are beneficial for a wide range of use-cases:

- ClickHouse is available both as an open-source product and as a managed cloud-based offering on AWS, Azure, and GCP
- ClickHouse is a multi-node database system, which allows for horizontal scaling. It can execute parts of queries on multiple nodes for improved performance.
- The use of columnar storage in ClickHouse, together with Vectorized query engine enhance the efficiency of analytical queries
- ClickHouse is a very fast OLAP database system, optimized for reporting queries that perform aggregations on a large amount of data.

### Is not built for
- ClickHouse is not built for performing a large number of mutations. Update and Delete operations are asynchronous, and there is no support for transactions.
- ClickHouse is not built for handling a large number of parallel connections, therefore, beyond a certain scale, it should be used as a warehouse in warehouse-mart architecture with application and user-facing queries going to the data marts

### Update and Delete 

- ClickHouse Update and Delete operations are asynchronous, and there is no support for transactions

### Column-Oriented
- Data in ClickHouse is stored in columns instead of rows, bringing at least two benefits:

- Every column can be sorted in a separate file; hence, stronger compression happens on each column and the whole table.
In range queries common in analytical processing, the system can access and process data easier since data is sorted in some columns (i.e., columns defined as sort keys). Additionally, it can parallelize processes on multi-cores while loading massive columns.

<p align="center">
  <img src="../images/co.gif" width="600"/>
</p>

<p align="center">
  <img src="../images/cd.webp" width="600"/>
</p>

### Note
Note: It should not get mistaken with Wide-Column databases like Cassandra as they store data in rows but enable you to denormalize intensive data in a table with many columns leading to a No-SQL structure.

###Data Compression
Thanks to compression algorithms (zstd and LZ4), data occupies much less storage, even more than 20x smaller! You can study some of the benchmarks on ClickHouse and other databases storage here.

<p align="center">
  <img src="../images/dca.webp" width="600"/>
</p>

### Scalability
ClickHouse scales well both vertically and horizontally. It can be scaled by adding extra replicas and extra shards to process queries in a distributed way. ClickHouse supports multi-master asynchronous replication and can be deployed across multiple data centers. All nodes are equal, which allows for avoiding having single points of failure.

### Weaknesses
To mention some:

- Lack of full-fledged UPDATE/DELETE implementation: ClickHouse is unsuited for modification and mutations. So you'll come across poor performance regarding those kinds of queries.
- OLTP queries like pointy ones would not make you happy since ClickHouse is easily outperformed by traditional RDBMSs like MySQL with those queries.

### Rivals and Alternatives
To name a few:

- Apache Druid
- ElasticSearch
- SingleStore
- Snowflake
- TimescaleDB

