## dremio_simple_query

The purpose of this library is to easily query a Dremio source using Arrow Flight for analytics.

[LEARN MORE ABOUT DREMIO](https://www.dremio.com)

Use Dremio to Help:
- Govern your data
- Join your data across sources (Iceberg, Delta, S3, JSON, CSV, RDBMS, and more)
- Accelerate your queries across data sources
- Reduce your Data Warehouse Workloads

With this library your analysts can more easily get their data from Dremio and easily get to work running local analytics with Arrow, Pandas, Polars and DuckDB. This library can grab large datasets performantly thanks to using Apache Arrow Flight.

## Getting Your URI and Token

| | Protocol | Endpoint | Result|
|-|----------|----------|-------|
|Dremio Cloud (NA)| grpc+tls:// | data.dremio.cloud:443| grpc+tls://data.dremio.cloud:443|
|Dremio Cloud (EU)| grpc+tls:// | data.eu.dremio.cloud:443| grpc+tls://data.eu.dremio.cloud:443|
|Dremio Software (SSL)| grpc+tls:// | `<ip-address>`:32010| grpc+tls://`<ip-address>`:32010|
|Dremio Software (NoSSL)| grpc:// | `<ip-address>`:32010| grpc://`<ip-address>`:32010|

Getting your token

- For Dremio Cloud can get token from interface or REST API
- For Dremio Software can get token from Rest API

The get_token function is included to help get the token from the Dremio Rest API.

```py
from dremio_simple_query.connect import get_token, DremioConnection

## URL to Login Endpoint
login_endpoint = "http://localhost:9047/apiv2/login"

## Payload for Login
payload = {
    "userName": username,
    "password": password
}

## Get token from API
token = get_token(uri = login_endpoint, payload=payload)

## URL Dremio Software Flight Endpoint
arrow_endpoint="grpc://localhost:32010"

## Establish Client
dremio = DremioConnection(token, arrow_endpoint)
```

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

#### toPandas (Get Pandas Dataframe Back)

```py
df = dremio.toPandas("SELECT * FROM arctic.table1;")
```

#### toPolars (Get Polars Dataframe Back)

```py
df = dremio.toPolars("SELECT * FROM arctic.table1;")
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

