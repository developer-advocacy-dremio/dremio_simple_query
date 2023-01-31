## dremio_simple_query

The purpose of this library is to easily query a Dremio source using Arrow Flight for analytics.

[LEARN MORE ABOUT DREMIO](https://www.dremio.com)

Use Dremio to Help:
- Govern your data
- Join your data across sources (Iceberg, Delta, S3, JSON, CSV, RDBMS, and more)
- Accelerate your queries across data sources
- Reduce your Data Warehouse Workloads

With this library your analysts can more easily get their data from Dremio and easily get to work running local analytics with Arrow and DuckDB. This library can grab large datasets performantly thanks to using Apache Arrow Flight.

#### Setting up your connection

```py
from dremio_simple_query.connect import DremioConnection
from os import getenv
from dotenv import load_dotenv

load_dotenv()

## Dremio Person Token
token = getenv("TOKEN")

## Arrow Endpoint (See Dremio Documentation)
uri = getenv("ARROW_ENDPOINT")

## Create Dremio Arrow Connection
dremio = DremioConnection(token, uri)
```

#### Query (Get Arrow Back)

If you want to get Arrow Data back you can run a query like so.

```py

stream = dremio.toArrow("SELECT * FROM arctic.table1;")
```

The `.toArrow` method returns a `FlightStreamReader` object which can be converted into typical Arrow objects.

**Arrow Table**
```py
arrow_table = stream.read_all()
```

**Arrow RecordBatchReader**
```py
batch_reader = stream.to_reader()
```

**Pandas Dataframe**
```py
df = stream.read_pandas()
```

## Querying with DuckDB

#### Using the DuckDB Relation API

Using the `.toDuckDB` method the query results will be returned as a DuckDB relation.

```py
duck_rel = dremio.toDuckDB("SELECT * FROM arctic.table1")

result = duck_rel.query("table1", "SELECT * from table1").fetchall()

result2 = duck_rel.filter

print(result)
```

#### Querying Arrow Objects with DuckDB

```py
from dremio_simple_query.connect import DremioConnection
from os import getenv
from dotenv import load_dotenv
import duckdb

## DuckDB Connection
con = duckdb.connection()

load_dotenv()

## Dremio Person Token
token = getenv("TOKEN")

## Arrow Endpoint (See Dremio Documentation)
uri = getenv("ARROW_ENDPOINT")

## Create Dremio Arrow Connection
dremio = DremioConnection(token, uri)

## Get Data from Dremio
stream = dremio.toArrow("SELECT * FROM arctic.table1;")

## Turn into Arrow Table
my_table = stream.read_all()

## Query with Duckdb
results = con.execute("SELECT * FROM my_table;").fetchall()

print(results)
```