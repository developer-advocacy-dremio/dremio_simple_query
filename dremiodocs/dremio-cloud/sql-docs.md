# Dremio Docs in One PDF

This repo is for having a markdown file of all Dremio docs that can be easily used with AI tools to better generate SQL queries.

## Reserved Words

Dremio reserves ANSI keywords and additional keywords to perform SQL queries on datalake sources and relational databases. These reserved keywords are part of the grammar of the SQL language that is used by Dremio to parse and understand SQL statements.

However, you can use these reserved keywords as an object name by enclosing a keyword in double quotes (for example, "boolean").

ABS, ACCESS, ACOS, AES_DECRYPT, AGGREGATE, ALL, ALLOCATE, ALLOW, ALTER, ANALYZE, AND, ANY, APPROX_COUNT_DISTINCT, APPROX_PERCENTILE, ARE, ARRAY_AVG, ARRAY_CAT, ARRAY_COMPACT, ARRAY_CONTAINS, ARRAY_GENERATE_RANGE, ARRAY_MAX_CARDINALITY, ARRAY_MAX, ARRAY_MIN, ARRAY_POSITION, ARRAY_REMOVE_AT, ARRAY_REMOVE, ARRAY_SIZE, ARRAY_SUM, ARRAY_TO_STRING, ARRAY, ARROW, AS, ASCII, ASENSITIVE, ASIN, ASSIGN, ASYMMETRIC, AT, ATAN, ATAN2, ATOMIC, AUTHORIZATION, AUTO, AVG, AVOID, BASE64, BATCH, BEGIN_FRAME, BEGIN_PARTITION, BEGIN, BETWEEN, BIGINT, BIN_PACK, BIN, BINARY_STRING, BINARY, BIT_AND, BIT_LENGTH, BIT_OR, BIT, BITWISE_AND, BITWISE_NOT, BITWISE_OR, BITWISE_XOR, BLOB, BOOL_AND, BOOL_OR, BOOLEAN, BOTH, BRANCH, BROUND, BTRIM, BY, CACHE, CALL, CALLED, CARDINALITY, CASCADED, CASE, CAST, CATALOG, CBRT, CEIL, CEILING, CHANGE, CHAR_LENGTH, CHAR, CHARACTER_LENGTH, CHARACTER, CHECK, CHR, CLASSIFIER, CLOB, CLOSE, CLOUD, COALESCE, COL_LIKE, COLLATE, COLLECT, COLUMN, COLUMNS, COMMIT, COMMITS_OLDER_THAN, COMPUTE, CONCAT_WS, CONCAT, CONDITION, CONNECT, CONSTRAINT, CONTAINS, CONVERT_FROM, CONVERT_REPLACEUTF8, CONVERT_TIMEZONE, CONVERT_TO, CONVERT, COPY, CORR, CORRESPONDING, COS, COSH, COT, COUNT, COVAR_POP, COVAR_SAMP, CRC32, CREATE, CROSS, CUBE, CUME_DIST, CURRENT_CATALOG, CURRENT_DATE_UTC, CURRENT_DATE, CURRENT_DEFAULT_TRANSFORM_GROUP, CURRENT_PATH, CURRENT_ROLE, CURRENT_ROW, CURRENT_SCHEMA, CURRENT_TIME, CURRENT_TIMESTAMP, CURRENT_TRANSFORM_GROUP_FOR_TYPE, CURRENT_USER, CURRENT, CURSOR, CYCLE, DATA, DATABASES, DATASETS, DATE_ADD, DATE_DIFF, DATE_FORMAT, DATE_PART, DATE_SUB, DATE_TRUNC, DATE, DATEDIFF, DATETYPE, DAY, DAYOFMONTH, DAYOFWEEK, DAYOFYEAR, DEALLOCATE, DEC, DECIMAL, DECLARE, DEDUPE_LOOKBACK_PERIOD, DEFAULT, DEFINE, DEGREES, DELETE, DENSE_RANK, DEREF, DESCRIBE, DETERMINISTIC, DIMENSIONS, DISALLOW, DISCONNECT, DISPLAY, DISTINCT, DOUBLE, DROP, DYNAMIC, E, EACH, ELEMENT, ELSE, EMPTY_AS_NULL, EMPTY, ENCODE, END_FRAME, END_PARTITION, END-EXEC, END, ENDS_WITH, ENGINE, EQUALS, ESCAPE_CHAR, ESCAPE, EVERY, EXCEPT, EXEC, EXECUTE, EXISTS, EXP, EXP, EXPIRE, EXPLAIN, EXTEND, EXTERNAL, EXTRACT, FACTORIAL, FALSE, FETCH, FIELD_DELIMITER, FIELD, FILE_FORMAT, FILES, FILTER, FIRST_VALUE, FLATTEN, FLOAT, FLOOR, FOLDER, FOR, FOREIGN, FRAME_ROW, FREE, FROM_HEX, FROM, FULL, FUNCTION, FUSION, GEO_BEYOND, GEO_DISTANCE, GEO_NEARBY, GET, GLOBAL, GRANT, GRANTS, GREATEST, GROUP, GROUPING, GROUPS, HASH, HASH64, HAVING, HEX, HISTORY, HOLD, HOUR, IDENTITY, IF, ILIKE, IMINDIR, IMPORT, IN, INCLUDE, INDICATOR, INITCAP, INITIAL, INNER, INOUT, INSENSITIVE, INSERT, INSTR, INT, INTEGER, INTERSECT, INTERSECTION, INTERVAL, INTO, IS [NOT] DISTINCT FROM, IS [NOT] FALSE, IS [NOT] NULL, IS [NOT] TRUE, IS_BIGINT, IS_INT, IS_MEMBER, IS_SUBSTR, IS_UTF8, IS_VARCHAR, IS, ISDATE, ISNUMERIC, JOB, JOIN, JSON_ARRAY, JSON_ARRAYAGG, JSON_EXISTS, JSON_OBJECT, JSON_OBJECTAGG, JSON_QUERY, JSON_VALUE, LAG, LANGUAGE, LARGE, LAST_DAY, LAST_QUERY_ID, LAST_VALUE, LATERAL, LAZY, LCASE, LEAD, LEADING, LEAST, LEFT, LENGTH, LEVENSHTEIN, LIKE_REGEX, LIKE, LIMIT, LISTAGG, LN, LOCAL, LOCALSORT, LOCALTIME, LOCALTIMESTAMP, LOCATE, LOG, LOG10, LOGS, LOWER, LPAD, LSHIFT, LTRIM, MANIFESTS, MAP_KEYS, MAP_VALUES, MASK_FIRST_N, MASK_HASH, MASK_LAST_N, MASK_SHOW_FIRST_N, MASK_SHOW_LAST_N, MASK, MASKING, MATCH_NUMBER, MATCH_RECOGNIZE, MATCH, MATCHES, MAX_FILE_SIZE_MB, MAX, MAXDIR, MD5, MEASURES, MEDIAN, MEMBER, MERGE, METADATA, METHOD, MIN_FILE_SIZE_MB, MIN_INPUT_FILES, MIN, MINDIR, MINUS, MINUTE, MISSING, MOD, MODIFIES, MODULE, MONITOR, MONTH, MONTH, MONTHS_BETWEEN, MORE, MULTISET, NATIONAL, NATURAL, NCHAR, NCLOB, NDV, NEW, NEXT_DAY, NEXT, NO, NONE, NORMALIZE_STRING, NORMALIZE, NOT, NOTIFICATION_PROVIDER, NOTIFICATION_QUEUE_REFERENCE, NOW, NTH_VALUE, NTILE, NULL_IF, NULL, NULLIF, NUMERIC, NVL, OCCURRENCES_REGEX, OCTET_LENGTH, OF, OFFSET, OLD, OLDER_THAN, OMIT, ON, ONE, ONLY, OPEN, OPERATE, OPTIMIZE, OR, ORDER, ORPHAN, OUT, OUTER, OVER, OVERLAPS, OVERLAY, OWNERSHIP, PARAMETER, PARSE_URL, PARTITION, PARTITIONS, PATTERN, PER, PERCENT_RANK, PERCENT, PERCENTILE_CONT, PERCENTILE_DISC, PERIOD, PERMUTE, PI, PIPE, PIPES, PIVOT, PMOD, POLICY, PORTION, POSITION_REGEX, POSITION, POW, POWER, PRECEDES, PRECISION, PREPARE, PREV, PRIMARY, PROCEDURE, PROJECT, PROMOTION, QUALIFY, QUARTER, QUERY_USER, QUERY, QUOTE_CHAR, QUOTE, RADIANS, RANDOM, RANGE, RANK, RAW, READS, REAL, RECORD_DELIMITER, RECURSIVE, REF, REFERENCE, REFERENCES, REFERENCING, REFLECTION, REFLECTIONS, REFRESH, REGEX, REGEXP_COL_LIKE, REGEXP_EXTRACT, REGEXP_LIKE, REGEXP_MATCHES, REGEXP_REPLACE, REGEXP_SPLIT, REGR_AVGX, REGR_AVGY, REGR_COUNT, REGR_INTERCEPT, REGR_R2, REGR_SLOPE, REGR_SXY, REGR_SYY, RELEASE, REMOVE, RENAME, REPEAT, REPEATSTR, REPLACE, RESET, RESULT, RETAIN_LAST, RETAIN_LAST_COMMITS, RETAIN_LAST_SNAPSHOTS, RETURN, RETURNS, REVERSE, REVOKE, REWRITE, RIGHT, ROLE, ROLLBACK, ROLLUP, ROUND, ROUTE, ROW_NUMBER, ROW, ROWS, RPAD, RSHIFT, RTRIM, RUNNING, SAVEPOINT, SCHEMAS, SCOPE, SCROLL, SEARCH, SECOND, SEEK, SELECT, SENSITIVE, SESSION_USER, SET, SHA, SHA1, SHA256, SHA512, SHOW, SIGN, SIMILAR_TO, SIMILAR, SIN, SINH, SIZE, SKIP, SMALLINT, SNAPSHOT, SNAPSHOTS_OLDER_THAN, SNAPSHOTS, SOME, SOUNDEX, SPECIFIC, SPECIFICTYPE, SPLIT_PART, SQL, SQLEXCEPTION, SQLSTATE, SQLWARNING, SQRT, SQRT, ST_FROMGEOHASH, ST_GEOHASH, START, STARTS_WITH, STATIC, STATISTICS, STDDEV_POP, STDDEV_SAMP, STDDEV, STREAM, STRING_BINARY, STRPOS, SUBMULTISET, SUBSET, SUBSTR, SUBSTRING_INDEX, SUBSTRING_REGEX, SUBSTRING, SUCCEEDS, SUM, SYMMETRIC, SYSTEM_TIME, SYSTEM_USER, SYSTEM, TABLE, TABLES, TABLESAMPLE, TAG, TAN, TANH, TARGET_FILE_SIZE_MB, TBLPROPERTIES, THEN, TIME_FORMAT, TIME, TIMESTAMP_FORMAT, TIMESTAMP, TIMESTAMPADD, TIMESTAMPDIFF, TIMESTAMPTYPE, TIMEZONE_HOUR, TIMEZONE_MINUTE, TINYINT, TO_CHAR, TO_DATE, TO_HEX, TO_NUMBER, TO_TIME, TO_TIMESTAMP, TO, TOASCII, TRAILING, TRANSACTION_TIMESTAMP, TRANSLATE_REGEX, TRANSLATE, TRANSLATION, TREAT, TRIGGER, TRIM_ARRAY, TRIM_SPACE, TRIM, TRUE, TRUNCATE, TYPEOF, UCASE, UESCAPE, UNBASE64, UNHEX, UNION, UNIQUE, UNIX_TIMESTAMP, UNKNOWN, UNNEST, UNPIVOT, UNSET, UPDATE, UPPER, UPSERT, USAGE, USE, USER, USING, VACUUM, VALUE_OF, VALUE, VALUES, VAR_POP, VAR_SAMP, VARBINARY, VARCHAR, VARYING, VERSIONING, VIEW, VIEWS, WEEK, WEEKOFYEAR, WHEN, WHENEVER, WHERE, WIDTH_BUCKET, WINDOW, WITH, WITHIN, WITHOUT, WRITE, XOR, YEAR

## Data Types

`Data Types`  
A data type classifies data and determines the operations allowed on it. Dremio supports numeric, string and binary, boolean, date and time, and semi-structured types.

The following topics are covered:  
`Coercions Support`: how types are coerced when source and table differ.  
`Summary of Supported Data Types in Dremio`.

`Numeric Data Types`

#### DECIMAL
    A DECIMAL type has precision (p) and scale (s): `DECIMAL(p,s)`. Precision is total digits. Scale is digits to the right of the decimal. Arithmetic between DECIMAL values adjusts precision and scale automatically.  
    Decimal limits:  
    - Decimal literals cannot exceed BIGINT max: `9223372036854775807`.  
    - Arithmetic with column + literal may fail. Example: `SELECT CAST(12345 as DOUBLE) * CAST(A as DOUBLE)` fails. Use a string literal instead.  
    - Casting numeric literals to DECIMAL requires explicit precision. Precision cannot be lowered.  
    - Decimal overflows return overflow values.  
    Example: `987.65` is a `DECIMAL(5,2)`.

#### INT  
    A 4-byte signed integer: -2147483648 to 2147483647.  
    Example: `5135`

#### BIGINT  
    An 8-byte signed integer: -9223372036854775808 to 9223372036854775807.  
    Example: `-749826542587`

#### FLOAT  
    4-byte single-precision float with six decimal digits.  
    Example: `123.123456`

#### DOUBLE  
    8-byte double-precision float with fifteen decimal digits.  
    Example: `123.123456789012345`

`String & Binary Data Types`

#### VARCHAR  
    Variable-length UTF-8 string.  
    Example: `18852367854`

#### VARBINARY  
    Variable-length binary string (up to 32,000 bytes).  
    Example:  
        - `SELECT CAST('help' AS VARBINARY)`
        - `-- aGVscA==`

`Boolean Data Type`

#### BOOLEAN  
    Supported values: `TRUE`, `FALSE`, `NULL`.

`Date & Time Data Types`

`note:` Dremio retrieves TIME and TIMESTAMP values as UTC without conversion.

#### DATE  
    Stores calendar dates.  
    `note:` String literal format must be `yyyy-mm-dd`.  
    Example: `DATE '2000-01-01'`

#### TIME  
    Stores time of day.  
    `note:` Supported formats: `HH24:MI:SS.sss` and `HH24:MI:SS`.  
    Examples:  
        - `TIME '17:30:50.235'`  
        - `TIME '17:30:50'`

#### TIMESTAMP  
    Represents an absolute moment with millisecond precision (no time zone).  
    Examples:  
        - `TIMESTAMP '2000-01-01 01:30:50'`  
        - `TIMESTAMP '2000-01-01 17:30:50.9'`  
        - `TIMESTAMP '2000-01-01 17:30:50.123'`

#### INTERVAL  
    Represents spans of time (year-month or day-time).  
    Supported forms include:  
    - `INTERVAL '3' DAY`  
    - `INTERVAL '3' MONTH`  
    - `INTERVAL '1' YEAR`  
    - `INTERVAL '5' MINUTE`  
    - `INTERVAL '4 01:01' DAY TO MINUTE`  
    Examples:  
        - `INTERVAL '1 2:34:56.789' DAY TO SECOND`  
        - `INTERVAL '1-5' YEAR TO MONTH`

`Semi-structured Data Types`

#### STRUCT  
    Represents key-value pairs. Keys are case-insensitive strings; values may be any type.  
    `note:` Use `CONVERT_FROM` with JSON strings to create STRUCT-like literals.  
    Example:  
        - `SELECT CONVERT_FROM('{"name":"Gnarly","age":7}', 'json')`  
        - `SELECT address['city'] FROM customerTable`

#### LIST  
    A list indexed by non-negative integers, values share one type.  
    `note:` LIST literals use `ARRAY`.  
    Example:  
        - `SELECT ARRAY[1,2,3]`  
        - `SELECT customerOrders[100] FROM OrderHistoryTable`
#### MAP  
    Key-value pairs where keys are case-insensitive strings and values share one type.  
    Syntax:  
        SELECT column_name['key'] FROM table_name  
    `note:`  
    - Run `ALTER TABLE ... FORGET METADATA` if MAP columns were previously read as STRUCT.  
    - MAP does not support null values.  
    Example:  
        - `SELECT address['city'] FROM customerTable`


## SQL Commands

### `SELECT`

Dremio supports querying using standard `SELECT` statements. You can query tables and views in connected sources and catalogs.

When working with Apache Iceberg tables, you can:

- Query table metadata  
- Run queries by snapshot ID  

**note**  
Dremio supports reading positional and equality deletes for Iceberg v2 tables. Dremio writes using copy-on-write by default and supports merge-on-read when enabled in table properties.

#### Syntax

```sql
[ WITH ... ]
SELECT [ ALL | DISTINCT ]
{ *
| <column_name1>, <column_name2>, ... }
FROM { <table_name> | <view_name>
| TABLE ( <iceberg_metadata> ( <table_name> ) )
| UNNEST ( <list_expression> ) [ WITH ORDINALITY ] }
[ { PIVOT | UNPIVOT } ( <expression> ) ]
[ WHERE <condition> ]
[ GROUP BY <expression> ]
[ QUALIFY <expression> ]
[ ORDER BY <column_name1>, <column_name2>, ... [ DESC ] ]
[ LIMIT <count> ]
[ AT { { REF[ERENCE] | BRANCH | TAG | COMMIT } <reference_name>
[ AS OF <timestamp> ]
| { SNAPSHOT <snapshot_id> | <timestamp> } } ]
| <function_name>
[ AT { REF[ERENCE] | BRANCH | TAG | COMMIT } <reference_name> ]
[ AS OF <timestamp> ]
| TABLE(<source_name>.EXTERNAL_QUERY ('<select_statement>'))
```

#### Parameters

- **`WITH`**  
  Defines a common table expression (CTE).

- **`ALL` / `DISTINCT`**  
  `ALL` returns all rows. `DISTINCT` removes duplicates.

- **`*`**  
  Selects all columns.

- **`<column_name>`**  
  One or more columns to query.

- **`FROM <table_name> | <view_name>`**  
  Source of the data.

- **`FROM TABLE(<iceberg_metadata>(<table_name>))`**  
  Queries Iceberg system metadata. Metadata includes:
  - Data files  
  - History  
  - Manifest files  
  - Partition statistics  
  - Snapshots  

#### Supported Iceberg Metadata Tables

##### `table_files(<table_name>)`
Returns metadata for each data file including:
- file_path  
- file_format  
- partition  
- record_count  
- file_size_in_bytes  
- column_sizes  
- value_counts  
- null_value_counts  
- nan_value_counts  
- lower_bounds  
- upper_bounds  
- key_metadata  
- split_offsets  

##### `table_history(<table_name>)`
Returns:
- made_current_at  
- snapshot_id  
- parent_id  
- is_current_ancestor  

##### `table_manifests(<table_name>)`
Returns:
- path  
- length  
- partition_spec_id  
- added_snapshot_id  
- added_data_files_count  
- existing_data_files_count  
- deleted_data_files_count  
- partition_summaries  

##### `table_partitions('<table_name>')`
Includes:
- partition  
- record_count  
- file_count  
- spec_id  

##### `table_snapshot(<table_name>)`
Includes:
- committed_at  
- snapshot_id  
- parent_id  
- operation  
- manifest_list  
- summary  

##### `clustering_information('<table_name>')`
Includes:
- table_name  
- clustering_keys  
- clustering_depth  
- last_clustering_timestamp  

#### `UNNEST(<list_expression>) [WITH ORDINALITY]`

- Expands a LIST into rows.  
- `WITH ORDINALITY` adds index values.

#### `PIVOT` / `UNPIVOT`

- `PIVOT`: rows → columns  
- `UNPIVOT`: columns → rows  

**note:** Aliases between table/subquery and pivot clauses are not supported.

#### `WHERE <condition>`

Filters records using comparison or logical operators (`=`, `>=`, `<`, `AND`, `OR`, `IN`, etc.).

#### `GROUP BY <expression>`

Groups rows to compute aggregations like `COUNT()`, `SUM()`, `AVG()`.

#### `QUALIFY <expression>`

Filters results *after* window functions are evaluated.

#### `ORDER BY <column_name> [DESC]`

Sorts results.

#### `LIMIT <count>`

Restricts number of returned rows.

#### `AT REF | BRANCH | TAG | COMMIT <reference_name>`

Time-travel and versioned queries.

- `REF` for any reference  
- `BRANCH`, `TAG`, `COMMIT`  
- Commit hashes must be in double quotes

#### `AS OF <timestamp>`

Reads the reference as of a timestamp.

#### `AT SNAPSHOT <snapshot_id>`

Reads a specific Iceberg or Delta snapshot.

#### `<function_name>`

Execute a UDF.

#### `TABLE(<source>.EXTERNAL_QUERY('...'))`

Runs a native query directly on external systems.

Limitations:

- Only SELECT statements allowed  
- No batched/multi-statement returns  
- Views created from EXTERNAL_QUERY cannot move before first refresh  

#### Examples

##### Query an existing table
```sql
SELECT *
FROM Samples."samples.dremio.com"."zips.json";
```

##### Query a specific column
```sql
SELECT city
FROM Samples."samples.dremio.com"."zips.json";
```

##### DISTINCT example
```sql
SELECT DISTINCT city
FROM Samples."samples.dremio.com"."zips.json";
```

##### WHERE clause
```sql
SELECT *
FROM Samples."samples.dremio.com"."zips.json"
WHERE state = 'MA' AND city = 'AGAWAM';
```

##### QUALIFY example (in SELECT)
```sql
SELECT passenger_count, trip_distance_mi, fare_amount,
RANK() OVER (PARTITION BY passenger_count ORDER BY trip_distance_mi) AS pc_rank
FROM "NYC-taxi-trips"
QUALIFY pc_rank = 1;
```

##### QUALIFY example (in QUALIFY)
```sql
SELECT passenger_count, trip_distance_mi, fare_amount
FROM "NYC-taxi-trips"
QUALIFY RANK() OVER (PARTITION BY passenger_count ORDER BY trip_distance_mi) = 1;
```

##### GROUP BY and ORDER BY
```sql
SELECT COUNT(city), city, state
FROM Samples."samples.dremio.com"."zips.json"
GROUP BY state, CITY
ORDER BY COUNT(city) DESC;
```

##### CTE example
```sql
WITH cte_quantity (Total) AS (
SELECT SUM(passenger_count) AS Total
FROM Samples."samples.dremio.com"."NYC-taxi-trips"
WHERE passenger_count > 2
GROUP BY pickup_datetime
)
SELECT AVG(Total) AS average_pass
FROM cte_quantity;
```

##### PIVOT / UNPIVOT example
```sql
ALTER DATASET Samples."samples.dremio.com"."SF weather 2018-2019.csv"
REFRESH METADATA auto promotion FORCE UPDATE;

SELECT * FROM (
SELECT EXTRACT(YEAR FROM CAST(F AS DATE)) AS "YEAR",
EXTRACT(MONTH FROM CAST(F AS DATE)) AS "MONTH",
K AS MAX_TEMP
FROM Samples."samples.dremio.com"."SF weather 2018-2019.csv"
WHERE F <> 'DATE'
)
PIVOT (
max(MAX_TEMP) FOR "MONTH" IN (1 AS JAN, 2 AS FEB, 3 AS MAR, 4 AS APR, 5 AS MAY, 6 AS JUN,
7 AS JUL, 8 AS AUG, 9 AS SEP, 10 AS OCT, 11 AS NOV, 12 AS "DEC")
)
UNPIVOT (
GLOBAL_MAX_TEMP FOR "MONTH" IN (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, "DEC")
)
ORDER BY "YEAR","MONTH";
```

##### UNNEST example
```sql
SELECT index, UPPER(array_item)
FROM UNNEST (ARRAY['a','b','c']) WITH ORDINALITY AS my_table (array_item, index)
ORDER BY index;
```

##### Query using a branch reference
```sql
SELECT *
FROM myCatalog.demo_table AT REF main_branch;
```

##### Query using a commit
```sql
SELECT *
FROM myCatalog.demo_view AT COMMIT "7f643f2b9cf250ce1f5d6ff4397237b705d866fbf34d714";
```

##### Time-travel by timestamp
```sql
SELECT *
FROM myTable AT TIMESTAMP '2022-01-01 17:30:50.000';
```

##### Time-travel by snapshot
```sql
SELECT *
FROM myTable AT SNAPSHOT '5393090506354317772';
```

##### Query Iceberg history
```sql
SELECT *
FROM TABLE(table_history('myTable'))
WHERE snapshot_id = 4593468819579153853;
```

##### Count snapshots
```sql
SELECT COUNT(*)
FROM TABLE(table_snapshot('myTable'))
```

#### Time-travel by timestamp
```sql
SELECT *
FROM myTable AT TIMESTAMP '2022-01-01 17:30:50.000';
```

#### Time-travel by snapshot
```sql
SELECT *
FROM myTable AT SNAPSHOT '5393090506354317772';
```

#### Query Iceberg history
```sql
SELECT *
FROM TABLE(table_history('myTable'))
WHERE snapshot_id = 4593468819579153853;
```

#### Count snapshots
```sql
SELECT COUNT(*)
FROM TABLE(table_snapshot('myTable'))
GROUP BY snapshot_id;
```

#### External query
```sql
SELECT *
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT * FROM Actor'));
```

#### External query with string literal
```sql
SELECT *
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT string_col FROM tbl WHERE string_col = ''test'' '));
```

#### JOIN external query
```sql
SELECT B.customer_id, A.product_id, A.price
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT product_id, price FROM products')) AS A,
source_b.sales AS B
WHERE B.product_id = A.product_id;
```

#### Time-travel by snapshot
```sql
SELECT *
FROM myTable AT SNAPSHOT '5393090506354317772';
```

#### Query Iceberg history
```sql
SELECT *
FROM TABLE(table_history('myTable'))
WHERE snapshot_id = 4593468819579153853;
```

#### Count snapshots
```sql
SELECT COUNT(*)
FROM TABLE(table_snapshot('myTable'))
GROUP BY snapshot_id;
```

#### Escaping quotes
```sql
SELECT *
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT string_col FROM tbl WHERE string_col = ''john '''' s car '''));
```

#### External query
```sql
SELECT *
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT * FROM Actor'));
```

#### External query with string literal
```sql
SELECT *
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT string_col FROM tbl WHERE string_col = ''test'' '));
```

#### Escaping quotes
```sql
SELECT *
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT string_col FROM tbl WHERE string_col = ''john '''' s car '''));
```

#### JOIN external query
```sql
SELECT B.customer_id, A.product_id, A.price
FROM TABLE(<source_name>.EXTERNAL_QUERY('SELECT product_id, price FROM products')) AS A,
source_b.sales AS B
WHERE B.product_id = A.product_id;
```

#### Column Aliasing

If you specify an alias, you can reference it elsewhere in the query.

#### Example 1
```sql
SELECT c_custkey AS c, lower(c)
FROM "customer.parquet";
```

#### Example 2
```sql
SELECT c_custkey AS c, lower(c)
FROM (
SELECT c_custkey, c_mktsegment AS c
FROM "customer.parquet"
);
```

#### Example 3
```sql
SELECT c_name AS n, n
FROM (
SELECT c_mktsegment AS n, c_name
FROM "customer.parquet"
) AS MY_TABLE
WHERE n = 'BUILDING';
```

#### Example 4
```sql
SELECT c_custkey
FROM (
SELECT c_custkey, c_name AS c
FROM "customer.parquet"
)
WHERE c = 'aa';
```

#### Example 5
```sql
SELECT *
FROM (
SELECT c_custkey AS c, c_name
FROM "customer.parquet"
)
JOIN "orders.parquet" ON c = o_orderkey;
```

#### Example 6
```sql
SELECT c_custkey AS c
FROM "customer.parquet"
JOIN "orders.parquet" ON c = o_orderkey;
```

#### Distributing Data Evenly Across Engines (BROADCAST Hint)

Use a BROADCAST hint if a join is skewed.

**note:** Not supported on views; ignored for nested-loop joins.

Syntax (inline): `/*+ BROADCAST */`

#### Example 1
```sql
SELECT *
FROM T1 /*+ BROADCAST */
INNER JOIN t2 ON t1.key = t2.key
INNER JOIN t3 ON t2.key = t3.key;
```

#### Example 2
```sql
SELECT *
FROM T1
INNER JOIN (
SELECT key, max(cost) cost
FROM t2 /*+ BROADCAST */
) T2 ON t1.key = t2.key
INNER JOIN t3 ON t2.key = t3.key;
```

#### `copy_errors()` — Inspect Rejected COPY INTO Records

#### Syntax
```sql
SELECT *
FROM TABLE(copy_errors('<table_name>', ['<query_id>']));
```

#### Fields Returned

- `job_id`: ID of the COPY job  
- `file_name`: file path  
- `line_number`: physical line number  
- `row_number`: record position  
- `column_name`: column with error  
- `error`: error description  

### `ALTER PIPE` Preview

Changes an existing autoingest pipe.

#### Syntax

```sql
ALTER PIPE <pipe_name>
{ SET PIPE_EXECUTION_RUNNING = { TRUE | FALSE }
| [ DEDUPE_LOOKBACK_PERIOD <number_of_days> ]
AS COPY INTO <table_name>
FROM '@<storage_location_name>[ /<folder_name> ]'
[ FILE_FORMAT 'csv' | 'json' | 'parquet']
[ ( [csv_format_options] | [json_format_options] | [parquet_format_options]) ]
}
```

#### CSV Format Options
```sql
[ DATE_FORMAT '<string>' ]
[ EMPTY_AS_NULL [ '<boolean>' ] [, ...] ]
[ ESCAPE_CHAR '<escape_character>' ]
[ EXTRACT_HEADER '<boolean>' ]
[ FIELD_DELIMITER '<character>' ]
[ NULL_IF ('<string>' [, ...]) ]
[ ON_ERROR 'skip_file' ]
[ QUOTE_CHAR '<character>' ]
[ RECORD_DELIMITER '<character>' ]
[ SKIP_LINES <n> ]
[ TIME_FORMAT '<string>' ]
[ TIMESTAMP_FORMAT '<string>' ]
[ TRIM_SPACE [ '<boolean>' ] ]
```

#### JSON Format Options
```sql
[ DATE_FORMAT '<string>' ]
[ EMPTY_AS_NULL [ '<boolean>' ] [, ...] ]
[ NULL_IF ('<string>' [, ...]) [, ...] ]
[ ON_ERROR 'skip_file' ]
[ TIME_FORMAT '<string>' ]
[ TIMESTAMP_FORMAT '<string>' ]
[ TRIM_SPACE [ '<boolean>' ] ]
```

#### Parquet Format Options
```sql
[ ON_ERROR 'skip_file' ]
```

#### Parameters

- **`<pipe_name>`**  
  Unique name of the autoingest pipe. Cannot be modified.

- **`SET PIPE_EXECUTION_RUNNING = { TRUE | FALSE }`**  
  Controls whether the pipe triggers a `COPY INTO` on notifications.  
  - `TRUE`: pipe active  
  - `FALSE`: pipe paused (default is TRUE)

- **`DED UPE_LOOKBACK_PERIOD <days>`**  
  - Days to look back for deduplication (0–90).  
  - Default: 14 days.

- **`AS COPY INTO <table_name>`**  
  Target Iceberg table. Use full qualifier if not in current context.

- **`@<storage_location_name>`**  
  Source location for files. Must exist as a configured Dremio source.

  **note:** Autoingest pipes ingest only from Amazon S3.

- **`/<folder_name>`**  
  Optional subfolder under the storage location.

- **`FILE_FORMAT 'csv' | 'json' | 'parquet'`**  
  Required. All files must match format.  
  - CSV/JSON may be compressed (`.gz`, `.bz2`)  
  - Parquet supports only `ON_ERROR 'skip_file'`

#### CSV Format Option Details

- **`DATE_FORMAT '<string>'`**  
  Defaults to `YYYY-MM-DD`.

- **`EMPTY_AS_NULL '<boolean>'`**  
  Default: `TRUE`.

- **`ESCAPE_CHAR '<escape_character>'`**  
  Default: `"`.

- **`EXTRACT_HEADER '<boolean>'`**  
  Default: `TRUE`.

- **`FIELD_DELIMITER '<character>'`**  
  Default: `,`.

- **`NULL_IF ('<string>' ...)`**  
  Strings to convert to NULL.

- **`ON_ERROR 'skip_file'`**  
  Stops at first error and logs error to `sys.project.copy_errors_history`.

- **`QUOTE_CHAR '<character>'`**  
  Default: `"`. 

- **`RECORD_DELIMITER '<character>'`**  
  Default: `\r\n`.

- **`SKIP_LINES <n>`**  
  Skips initial lines.

- **`TIME_FORMAT '<string>'`**  
  Default: `HH24:MI:SS.FFF`.

- **`TIMESTAMP_FORMAT '<string>'`**  
  Default: `YYYY-MM-DD HH24:MI:SS.FFF`.

- **`TRIM_SPACE '<boolean>'`**  
  Default: `FALSE`.

#### JSON Format Option Details

- **`DATE_FORMAT '<string>'`** – default: `YYYY-MM-DD`  
- **`EMPTY_AS_NULL '<boolean>'`** – default: `TRUE`  
- **`NULL_IF ('<string>'...)`** – replace values with NULL  
- **`ON_ERROR 'skip_file'`** – default, only supported mode  
- **`TIME_FORMAT '<string>'`** – default: `HH24:MI:SS.FFF`  
- **`TIMESTAMP_FORMAT '<string>'`** – default: `YYYY-MM-DD HH24:MI:SS.FFF`  
- **`TRIM_SPACE '<boolean>'`** – default: `FALSE`

#### Parquet Format Option Details

- **`ON_ERROR 'skip_file'`** only  
  - Logs first error to history  
  - Requires extra file processing  
  - Skips entire file on any error  

#### Examples

#### Pause an autoingest pipe
```sql
ALTER PIPE test_pipe
SET PIPE_EXECUTION_RUNNING = FALSE
```

#### Change the pipe storage location
```sql
ALTER PIPE test_pipe
AS COPY INTO Table_one
FROM '@s3_source/folder'
FILE_FORMAT 'json'
```

### `ALTER SOURCE`

Change the configuration or status of an existing source.

#### Syntax
```sql
ALTER SOURCE <source_name>
{ CLEAR PERMISSION CACHE | REFRESH STATUS }
```

To run `ALTER SOURCE`, you need the **MODIFY** privilege on the source.

#### Parameters

- **`<source_name>`**  
  Name of the source to alter.

- **`CLEAR PERMISSION CACHE`**  
  - Clears the AWS Lake Formation permission cache.  
  - Applies only to AWS Glue Data Catalog sources.  
  - Dremio caches Lake Formation permissions for one hour.  
  - Use this command after changing permissions in AWS Lake Formation to invalidate the cache immediately.

  **note:**  
  Any change to AWS Glue Data Catalog settings also clears the permission cache.

- **`REFRESH STATUS`**  
  Refreshes the status of the source.

#### Examples

#### Clear the Lake Formation permission cache
```sql
ALTER SOURCE glue1
CLEAR PERMISSION CACHE
```

#### Refresh status for an Amazon S3 source
```sql
ALTER SOURCE S3
REFRESH STATUS
```



### `ALTER TABLE`

Update a table’s definition or schema.

#### Syntax

```sql
ALTER TABLE <table_name>
{ ADD PRIMARY KEY ( <column_name> [ , ... ] )
| DROP PRIMARY KEY
| ADD COLUMNS ( <column_name> <data_type> [ NULL ] [ , ... ] )
| DROP COLUMN <column_name>
| { ALTER | MODIFY | CHANGE } COLUMN <old_name> <new_name> <data_type> [ { NULL | NOT NULL | DROP NOT NULL } ]
| MODIFY COLUMN <column_name> { SET MASKING POLICY <function_name> ( <column_name> [, ... ] ) | UNSET MASKING POLICY <function_name> }
| { ADD | DROP } ROW ACCESS POLICY <function_name> ( <column_name> [, ... ] )
| CLUSTER BY ( <column_name> [ , ... ] )
| DROP CLUSTERING KEY
| LOCALSORT BY ( <column_name> [ , ... ] )
| REFRESH METADATA [ IN <catalog_name> ] [ FOR PARTITIONS ( <partition_name> = '<value>') ] [ { AVOID | AUTO } PROMOTION ] [ { FORCE | LAZY } UPDATE ] [ { MAINTAIN | DELETE } WHEN MISSING ]
| FORGET METADATA
| SET TBLPROPERTIES ( '<property_name>' = '<property_value>' [ , ... ] )
| UNSET TBLPROPERTIES ( '<property_name>' [ , ... ] )
| CREATE AGGREGATE REFLECTION <reflection_name> USING { DIMENSIONS ( <column_name> [ , ... ] ) | MEASURES ( <column_name> ( <aggregation_type> ) [ , ... ] ) ) | DIMENSIONS ( <column_name> [ , ... ] ) MEASURES ( <column_name> ( <aggregation_type> ) [ , ... ] ) } [ PARTITION BY ( { <column_name> | <partition_transform> } [ , ... ] ) ] [ LOCALSORT BY ( <column_name> [ , ... ] ) ]
| CREATE EXTERNAL REFLECTION <reflection_name> USING <table_name>
| CREATE RAW REFLECTION <reflection_name> USING DISPLAY ( <column_name> [ , ... ] ) [ PARTITION BY ( { <column_name> | <partition_transform> } [ , ... ] ) ] [ LOCALSORT BY ( <column_name> [ , ... ] ) ]
| DROP REFLECTION <reflection_name>
| REFRESH REFLECTIONS
| ROUTE REFLECTIONS TO { DEFAULT ENGINE | ENGINE { <engine_name> | <engine_uuid> } }
| { ADD | DROP } PARTITION FIELD { <column_name> | <partition_transform> }
}
```

#### Parameters

- **`<table_name>`**  
  The name of the table that you want to alter.

- **`ADD PRIMARY KEY ( <column_name> [ , ... ] )`**  
  Specifies to use one or more existing columns as the primary key of a table. Primary keys provide hints to the query planning during join planning. They can be added to Apache Iceberg tables only. Uniqueness of the values in a primary key is not enforced.

- **`DROP PRIMARY KEY`**  
  Removes a table's primary key. The columns that make up the primary key remain in the table.

- **`ADD COLUMNS ( <column_name> <data_type> [ NULL ] [ , ... ] )`**  
  Creates one or more columns that have the specified names, data types, character limits, and nullability properties.
  
  Supported primitive types: `BOOLEAN`, `VARBINARY`, `DATE`, `FLOAT`, `DECIMAL`, `DOUBLE`, `INTERVAL`, `INT`, `BIGINT`, `TIME`, `TIMESTAMP`, `VARCHAR`.
  
  Complex types syntax:
  - `ROW( name primitive_or_complex_type, .. )`
  - `ARRAY(primitive_or_complex_type)`
  - `STRUCT <name : primitive_or_complex_type, ... >`
  - `{ LIST | ARRAY } < primitive_or_complex_type >`

  Use `NULL` to allow NULL values (default). You cannot add a `NOT NULL` column to an existing table.

- **`DROP COLUMN <column_name>`**  
  Drops the specified column. This action cannot be undone.

- **`{ ALTER | MODIFY | CHANGE } COLUMN <old_column_name> <new_column_name> <data_type>`**  
  Changes the data type for a column, and gives you the option to rename the column. Renaming is supported except for Parquet, JSON, or BSON.
  
  Allowed primitive type changes:
  - `INT` to `BIGINT`
  - `FLOAT` to `DOUBLE`
  - `DECIMAL(p, s)` to `DECIMAL(p', s)` (widening precision)

- **`[ { NULL | NOT NULL | DROP NOT NULL } ]`**  
  - `NULL`: Allow NULL values.
  - `NOT NULL`: Prevent NULL values.
  - `DROP NOT NULL`: Change from preventing NULLs to allowing them.

- **`MODIFY COLUMN <column_name> { SET | UNSET } MASKING POLICY`**  
  Sets or unsets a masking policy on a column. (Enterprise only)

- **`{ ADD | DROP } ROW ACCESS POLICY`**  
  Adds or removes a row-access policy. (Enterprise only)

- **`CLUSTER BY ( <column_name> [ , ... ] )`**  
  Columns to cluster the table by. Future `OPTIMIZE TABLE` commands will follow this scheme. (Enterprise only)

- **`DROP CLUSTERING KEY`**  
  Removes clustering keys.

- **`LOCALSORT BY ( <column_name> [ , ... ] )`**  
  Columns to sort new data by.

- **`REFRESH METADATA`**  
  Refreshes table metadata.
  - `FOR PARTITIONS ( <partition_name> = '<value>' )`: Partial refresh.
  - `{ AVOID | AUTO } PROMOTION`: Handle file promotion.
  - `{ FORCE | LAZY } UPDATE`: Force full update or lazy update.
  - `{ MAINTAIN | DELETE } WHEN MISSING`: Handle missing metadata.

- **`FORGET METADATA`**  
  Deletes metadata until next refresh.

- **`SET TBLPROPERTIES`**  
  Sets table properties (e.g., for Iceberg).

- **`UNSET TBLPROPERTIES`**  
  Removes table properties.

- **`CREATE AGGREGATE REFLECTION`**  
  Creates an aggregation reflection.
  - `DIMENSIONS`: Columns for dimensions.
  - `MEASURES`: Columns for measures and aggregation types (`COUNT`, `MIN`, `MAX`, `SUM`, `APPROXIMATE COUNT DISTINCT`).
  - `PARTITION BY`: Horizontal partitioning.
  - `LOCALSORT BY`: Sort order.

- **`CREATE EXTERNAL REFLECTION`**  
  Creates an external reflection using a derived table.

- **`CREATE RAW REFLECTION`**  
  Creates a raw reflection.
  - `USING DISPLAY`: Columns to include.

- **`DROP REFLECTION`**  
  Drops a reflection.

- **`REFRESH REFLECTIONS`**  
  Triggers reflection refresh.

- **`ROUTE REFLECTIONS TO`**  
  Specifies engine for reflection jobs.

- **`{ ADD | DROP } PARTITION FIELD`**  
  Adds or drops partition fields (Iceberg only).
  Transforms: `identity`, `year`, `month`, `day`, `hour`, `bucket`, `truncate`.

#### Examples

##### Add a primary key
```sql
ALTER TABLE services ADD PRIMARY KEY (Country_ID);
```

##### Add columns
```sql
ALTER TABLE services ADD COLUMNS (county varchar);
```

##### Modify column type
```sql
ALTER TABLE services MODIFY COLUMN tip_amount tip_amount DECIMAL;
```

##### Modify struct column
```sql
ALTER TABLE struct_type MODIFY COLUMN a a struct<x: varchar, y: bigint>;
```

##### Rename and modify column
```sql
ALTER TABLE services MODIFY COLUMN tip_amount gratuity_amount DECIMAL;
```

##### Change column nullability
```sql
ALTER TABLE age_table CHANGE age age INT DROP NOT NULL;
```

##### Add multiple columns
```sql
ALTER TABLE my_table ADD COLUMNS ( email VARCHAR NULL, date_of_birth DATE );
```

##### Refresh metadata
```sql
ALTER TABLE services REFRESH METADATA;
```

##### Refresh metadata with options
```sql
ALTER TABLE services REFRESH METADATA AUTO PROMOTION LAZY UPDATE MAINTAIN WHEN MISSING;
```

##### Partial metadata refresh
```sql
ALTER TABLE Samples."samples.dremio.com"."zips.json" REFRESH METADATA FOR PARTITIONS (state = 'TX');
```

##### Forget metadata
```sql
ALTER TABLE Samples."samples.dremio.com"."zips.json" FORGET METADATA;
```

##### Create raw reflection
```sql
ALTER TABLE Sales."customers" CREATE RAW REFLECTION customers_by_country USING DISPLAY (id,lastName,firstName,address,country) PARTITION BY (country) LOCALSORT BY (lastName);
```

##### Create aggregate reflection
```sql
ALTER TABLE Samples."samples.dremio.com"."zips.json" CREATE AGGREGATE REFLECTION per_state USING DIMENSIONS (state) MEASURES (city (COUNT)) LOCALSORT BY (state);
```

##### Route reflections
```sql
ALTER TABLE "Table 1" ROUTE REFLECTIONS TO ENGINE "Engine 1";
```

##### Cluster by
```sql
ALTER TABLE clustered_table CLUSTER BY (Col_one, Col_two, Col_three);
```

##### Drop clustering key
```sql
ALTER TABLE clustered_table DROP CLUSTERING KEY;
```


### `ALTER VIEW`

Change an existing view.

#### Syntax

```sql
ALTER VIEW <view_name>
{ REFRESH METADATA [ FOR PARTITIONS ( <partition_name> = '<value>') ] [ { AVOID | AUTO } PROMOTION ] [ { FORCE | LAZY } UPDATE ] [ { MAINTAIN | DELETE } WHEN MISSING ]
| CREATE EXTERNAL REFLECTION <reflection_name> USING <view_name>
| CREATE AGGREGATE REFLECTION <reflection_name> USING { DIMENSIONS ( <column_name1>, <column_name2>, ... ) | MEASURES ( <column_name1> ( <aggregation_type>, <column_name2> <aggregation_type> , ... ) ) | DIMENSIONS ( <column_name1>, <column_name2>, ... ) MEASURES ( <column_name1> ( <aggregation_type>, <column_name2> <aggregation_type> , ... ) ) } [ PARTITION BY ( <column_name1>, <column_name2>, ... ) ] [ LOCALSORT BY ( <column_name1>, <column_name2>, ... ) ]
| CREATE RAW REFLECTION <reflection_name> USING DISPLAY ( <column_name1>, <column_name2>, ...) [ PARTITION BY ( <column_name1>, <column_name2>, ... ) ] [ LOCALSORT BY ( <column_name1>, <column_name2>, ... ) ]
| DROP REFLECTION <reflection_name>
| REFRESH REFLECTIONS
| ROUTE REFLECTIONS TO { DEFAULT ENGINE | ENGINE { <engine_name> | <engine_uuid> } }
}
```

#### Parameters

- **`<view_name>`**  
  The name of the view that you want to alter.

- **`REFRESH METADATA`**  
  Refreshes metadata (Iceberg REST Catalog sources only).
  - `FOR PARTITIONS ( <partition_name> = '<value>' )`: Partial refresh.
  - `{ AVOID | AUTO } PROMOTION`: Handle file promotion.
  - `{ FORCE | LAZY } UPDATE`: Force full update or lazy update.
  - `{ MAINTAIN | DELETE } WHEN MISSING`: Handle missing metadata.

- **`CREATE EXTERNAL REFLECTION`**  
  Creates an external reflection.

- **`CREATE AGGREGATE REFLECTION`**  
  Creates an aggregate reflection.

- **`CREATE RAW REFLECTION`**  
  Creates a raw reflection.

- **`DROP REFLECTION`**  
  Drops a reflection.

- **`REFRESH REFLECTIONS`**  
  Triggers reflection refresh.

- **`ROUTE REFLECTIONS TO`**  
  Specifies engine for reflection jobs.

#### Examples

##### Create raw reflection on view
```sql
ALTER VIEW Sales."customers" CREATE RAW REFLECTION customers_by_country USING DISPLAY (id,lastName,firstName,address,country) PARTITION BY (country) LOCALSORT BY (lastName);
```

##### Create aggregate reflection on view
```sql
ALTER VIEW Samples."samples.dremio.com"."zips.json" CREATE AGGREGATE REFLECTION per_state USING DIMENSIONS (state) MEASURES (city (COUNT)) LOCALSORT BY (state);
```

##### Route reflections
```sql
ALTER VIEW "View 1" ROUTE REFLECTIONS TO ENGINE "Engine 1";
```

### `ANALYZE TABLE`

Compute and delete statistics for tables, including estimated number of distinct values, number of rows, and number of null values.

#### Syntax

```sql
ANALYZE TABLE <table_name> FOR { ALL COLUMNS | COLUMNS ( <column_name1>, <column_name2>, ... ) } { COMPUTE | DELETE } STATISTICS
```

#### Parameters

- **`<table_name>`**  
  The path to the table.

- **`FOR { ALL COLUMNS | COLUMNS (...) }`**  
  Specify columns to analyze.

- **`{ COMPUTE | DELETE } STATISTICS`**  
  Compute or delete statistics.

#### Examples

##### Compute statistics for all columns
```sql
ANALYZE TABLE Samples."samples.dremio.com"."NYC-taxi-trips" FOR ALL COLUMNS COMPUTE STATISTICS
```

##### Compute statistics for specific columns
```sql
ANALYZE TABLE Samples."samples.dremio.com"."NYC-taxi-trips" FOR COLUMNS (fare_amount, tip_amount) COMPUTE STATISTICS
```


### `COPY INTO`

Load data from CSV, JSON, or Parquet files into an existing Apache Iceberg table.

#### Syntax

```sql
COPY INTO <table_name>
FROM '@<storage_location_name>[/<path>[/<file_name>] ]'
[ FILES ( '<file_name>' [ , ... ] ) | REGEX '<regex_pattern>' ]
[ FILE_FORMAT 'csv' | 'json' | 'parquet' ]
[ ( [csv_format_options] | [json_format_options] | [parquet_format_options] ) ]
```

#### Parameters

- **`<table_name>`**  
  The target table.

- **`FROM '@<storage_location_name>...'`**  
  Source location. Can be a directory or specific file.

- **`FILES ( '<file_name>' ... )`**  
  List of specific files to load.

- **`REGEX '<regex_pattern>'`**  
  Regex pattern to match files.

- **`FILE_FORMAT`**  
  `csv`, `json`, or `parquet`.

#### Format Options

**CSV Options:**
- `DATE_FORMAT`: Date format string.
- `EMPTY_AS_NULL`: Treat empty strings as NULL (default TRUE).
- `ESCAPE_CHAR`: Escape character (default `"`).
- `EXTRACT_HEADER`: First line is header (default TRUE).
- `FIELD_DELIMITER`: Field separator (default `,`).
- `NULL_IF`: Strings to replace with NULL.
- `ON_ERROR`: `abort` (default), `continue`, or `skip_file`.
- `QUOTE_CHAR`: Quote character (default `"`).
- `RECORD_DELIMITER`: Record separator (default `\r\n`).
- `SKIP_LINES`: Number of lines to skip.
- `TIME_FORMAT`: Time format string.
- `TIMESTAMP_FORMAT`: Timestamp format string.
- `TRIM_SPACE`: Trim whitespace (default FALSE).

**JSON Options:**
- `DATE_FORMAT`
- `EMPTY_AS_NULL`
- `NULL_IF`
- `ON_ERROR`
- `TIME_FORMAT`
- `TIMESTAMP_FORMAT`
- `TRIM_SPACE`

**Parquet Options:**
- `ON_ERROR`: `abort` or `skip_file`.

#### Examples

##### Copy from specific file
```sql
COPY INTO context.myTable FROM '@SOURCE/bucket/path/folder' FILES ('fileName.csv') (ON_ERROR 'continue')
```

##### Copy JSON files
```sql
COPY INTO context.MyTable FROM '@SOURCE/bucket/path/folder/' FILE_FORMAT 'json'
```

##### Copy using Regex
```sql
COPY INTO context.myTable FROM '@SOURCE/bucket/path/folder' REGEX '.*.csv'
```

##### Copy with CSV options
```sql
COPY INTO context.myTable FROM '@SOURCE/bucket/path/folder' FILE_FORMAT 'csv' (RECORD_DELIMITER '\n', FIELD_DELIMITER '\t')
```

### `CREATE FOLDER`

Create a new folder in your catalog.

#### Syntax

```sql
CREATE FOLDER [ IF NOT EXISTS ] <folder_name>
```

#### Parameters

- **`IF NOT EXISTS`**  
  Prevent error if folder exists.

- **`<folder_name>`**  
  Name of the folder. Cannot include `/`, `:`, `[`, `]`.

#### Examples

##### Create folder
```sql
CREATE FOLDER myFolder
```

##### Create if not exists
```sql
CREATE FOLDER IF NOT EXISTS myFolder
```


### `CREATE FUNCTION`

Creates user-defined functions (UDFs) in the catalog.

#### Syntax

```sql
CREATE [ OR REPLACE ] FUNCTION [ IF NOT EXISTS ] <function_name> ( [ <function_parameter> [, ...] ] )
RETURNS { <data_type> | TABLE ( <column_name> [, ...] ) }
RETURN { <expression> | <query> }
```

#### Parameters

- **`OR REPLACE`**  
  Replaces existing UDF. Cannot use with `IF NOT EXISTS`.

- **`IF NOT EXISTS`**  
  Creates only if it doesn't exist. Cannot use with `OR REPLACE`.

- **`<function_name>`**  
  Name of the UDF.

- **`<function_parameter>`**  
  `parameter_name` and `data_type`.

- **`RETURNS <data_type>`**  
  Return type for scalar function.

- **`RETURNS TABLE ( <column_name> [, ...] )`**  
  Return signature for tabular function.

- **`RETURN { <expression> | <query> }`**  
  Body of the UDF. Expression for scalar, query for tabular.

#### Examples

##### Scalar function
```sql
CREATE FUNCTION area (x DOUBLE, y DOUBLE) RETURNS DOUBLE RETURN x * y;
```

##### Tabular function
```sql
CREATE FUNCTION all_fruits() RETURNS TABLE (name VARCHAR, hue VARCHAR) RETURN SELECT * FROM <catalog-name>.t2;
```

### `CREATE PIPE`

Create a pipe object that automatically ingests files from a cloud storage location.

#### Syntax

```sql
CREATE PIPE [ IF NOT EXISTS ] <pipe_name>
[ DEDUPE_LOOKBACK_PERIOD <number_of_days> ]
AS COPY INTO <table_name>
FROM '@<storage_location_name>[ /<folder_name> ]'
[ FILE_FORMAT 'csv' | 'json' | 'parquet']
[ ( [csv_format_options] | [json_format_options] | [parquet_format_options] ) ]
```

#### Parameters

- **`IF NOT EXISTS`**  
  Prevent error if pipe exists.

- **`<pipe_name>`**  
  Unique name of the pipe.

- **`DEDUPE_LOOKBACK_PERIOD <days>`**  
  Days to check for duplicates (0-90, default 14).

- **`AS COPY INTO <table_name>`**  
  Target Iceberg table.

- **`FROM '@<storage_location_name>...'`**  
  Source location (Amazon S3 only).

- **`FILE_FORMAT`**  
  `csv`, `json`, or `parquet`.

#### Examples

##### Create pipe
```sql
CREATE PIPE Example_pipe AS COPY INTO Pipe_sink FROM '@<storage_location_name>/folder' FILE_FORMAT 'csv'
```

##### Create pipe with dedupe lookback
```sql
CREATE PIPE Example_pipe DEDUPE_LOOKBACK_PERIOD 5 AS COPY INTO Table_one FROM '@<storage_location_name>/files' FILE_FORMAT 'csv'
```

### `CREATE ROLE`

Create a new role.

#### Syntax

```sql
CREATE ROLE <role_name>
```

#### Parameters

- **`<role_name>`**  
  Name of the new role.

#### Example

```sql
CREATE ROLE role1
```


### `CREATE TABLE`

Create a new table.

#### Syntax

```sql
CREATE TABLE [ IF NOT EXISTS ] <table_name>
( <column_name> <data_type> [ { NULL | NOT NULL } ] [ , ... ] )
[ MASKING POLICY <function_name> ( <column_name> [ , ... ] ) ]
[ ROW ACCESS POLICY <function_name> ( <column_name> [ , ... ] ) ]
[ PARTITION BY ( { <column_name> | <partition_transform> } [ , ... ] ) ]
[ CLUSTER BY ( <column_name> [ , ... ] ) ]
[ LOCALSORT BY ( <column_name> [ , ... ] ) ]
[ TBLPROPERTIES ( '<property_name>' = '<property_value>' [ , ... ] ) ]
```

#### Parameters

- **`IF NOT EXISTS`**  
  Prevent error if table exists.

- **`<table_name>`**  
  Name of the table.

- **`( <column_name> <data_type> ... )`**  
  Column definitions.
  - Primitive types: `BOOLEAN`, `VARBINARY`, `DATE`, `FLOAT`, `DECIMAL`, `DOUBLE`, `INTERVAL`, `INT`, `BIGINT`, `TIME`, `TIMESTAMP`, `VARCHAR`.
  - Complex types: `ROW`, `ARRAY`, `STRUCT`, `LIST`.
  - Nullability: `NULL` (default) or `NOT NULL`.

- **`MASKING POLICY`**  
  Set masking policy (Enterprise).

- **`ROW ACCESS POLICY`**  
  Set row access policy (Enterprise).

- **`PARTITION BY`**  
  Partition columns or transforms (`identity`, `year`, `month`, `day`, `hour`, `bucket`, `truncate`).

- **`CLUSTER BY`**  
  Cluster columns (Enterprise).

- **`LOCALSORT BY`**  
  Sort columns within files.

- **`TBLPROPERTIES`**  
  Table properties (Iceberg).

#### Examples

##### Create table with columns
```sql
CREATE TABLE employees (PersonID int, LastName varchar, FirstName varchar, Address varchar, City varchar)
```

##### Create table with partitions
```sql
CREATE TABLE myTable (col1 int, col2 date) PARTITION BY (month(col2))
```

##### Create table with complex types
```sql
CREATE TABLE my_table (name VARCHAR NOT NULL, age INT NULL, address STRUCT<street VARCHAR, zip INT NOT NULL, city VARCHAR NOT NULL>);
```

### `CREATE TABLE AS`

Create a new table as a select statement from another table.

#### Syntax

```sql
CREATE TABLE [ IF NOT EXISTS ] <table_name>
[ ( <column_name> <data_type> [ { NULL | NOT NULL } ] [ , ... ] ) ]
[ PARTITION BY ( { <column_name> | <partition_transform> } [ , ... ] )
[ CLUSTER BY ( <column_name> [ , ... ] ) ]
[ LOCALSORT BY ( <column_name> [ , ... ] ) ]
[ TBLPROPERTIES ( '<property_name>' = '<property_value>' [ , ... ] ) ]
AS <select_statement>
```

#### Parameters

- **`IF NOT EXISTS`**  
  Prevent error if table exists.

- **`<table_name>`**  
  Name of the table.

- **`( <column_name> <data_type> ... )`**  
  Optional column definitions to override source.

- **`PARTITION BY`**  
  Partition columns or transforms.

- **`CLUSTER BY`**  
  Cluster columns (Enterprise).

- **`LOCALSORT BY`**  
  Sort columns.

- **`TBLPROPERTIES`**  
  Table properties.

- **`AS <select_statement>`**  
  Query to populate the table.

#### Examples

##### Create table from select
```sql
CREATE TABLE demo_table AS SELECT * FROM Samples."samples.dremio.com"."zips.json"
```

##### Create table with partition and sort
```sql
CREATE TABLE demo_table2 PARTITION BY (state) LOCALSORT BY (city) AS SELECT * FROM Samples."samples.dremio.com"."zips.json"
```

##### Create table from time travel query
```sql
CREATE TABLE demo.example_table AS SELECT * FROM "oracle_tpch".DREMIO.JOBS AT TAG Jan2020
```

### `CREATE USER`

Create a new user.

#### Syntax

```sql
CREATE USER <username>
```

#### Parameters

- **`<username>`**  
  Email of the user (in double quotes).

#### Example

```sql
CREATE USER "user@dremio.com"
```


### `CREATE VIEW`

Create or replace a view.

#### Syntax

```sql
CREATE [ OR REPLACE ] VIEW <view_name> AS <select_statement>
```

#### Parameters

- **`OR REPLACE`**  
  Replaces existing view.

- **`<view_name>`**  
  Name of the view.

- **`AS <select_statement>`**  
  Query to populate the view.

#### Examples

##### Create view
```sql
CREATE VIEW demo.example_view AS SELECT * FROM "oracle_tpch".DREMIO.JOBS
```

##### Replace view
```sql
CREATE OR REPLACE VIEW demo.example_view AS SELECT * FROM "oracle_tpch".DREMIO.INVENTORY
```

### `DESCRIBE FUNCTION`

Returns the metadata about an existing user-defined function (UDF).

#### Syntax

```sql
{ DESC | DESCRIBE } FUNCTION <function_name>
```

#### Parameters

- **`<function_name>`**  
  Name of the UDF.

#### Examples

```sql
DESCRIBE FUNCTION hello
```

### `DESCRIBE PIPE`

Get high-level information about the settings and configuration of a specific autoingest pipe.

#### Syntax

```sql
DESCRIBE PIPE <pipe_name>
```

#### Parameters

- **`<pipe_name>`**  
  Name of the pipe.

#### Examples

```sql
DESCRIBE PIPE Example_pipe
```


### `DESCRIBE TABLE`

Provide high-level information regarding the overall column properties of an existing dataset.

#### Syntax

```sql
DESCRIBE TABLE <table_name>
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

#### Example

```sql
DESCRIBE TABLE taxistats
```

### `DROP FOLDER`

Remove a folder from a catalog.

#### Syntax

```sql
DROP FOLDER [ IF EXISTS ] <folder_name> [ .<child_folder_name> ]
```

#### Parameters

- **`IF EXISTS`**  
  Prevent error if folder doesn't exist.

- **`<folder_name>`**  
  Name of the folder.

#### Examples

##### Drop folder
```sql
DROP FOLDER myFolder
```

##### Drop child folder
```sql
DROP FOLDER myFolder.resources
```

### `DROP FUNCTION`

Drops a user-defined function (UDF) in the catalog.

#### Syntax

```sql
DROP FUNCTION [ IF EXISTS ] <function_name> [ AS OF <timestamp> ]
```

#### Parameters

- **`IF EXISTS`**  
  Prevent error if function doesn't exist.

- **`<function_name>`**  
  Name of the UDF.

#### Examples

##### Drop function
```sql
DROP FUNCTION hello
```

##### Drop if exists
```sql
DROP FUNCTION IF EXISTS hello
```


### `DROP PIPE`

Removes the specified pipe from a source.

#### Syntax

```sql
DROP PIPE <pipe_name>
```

#### Parameters

- **`<pipe_name>`**  
  Name of the pipe.

#### Examples

```sql
DROP PIPE Example_pipe
```

### `DROP ROLE`

Removes a role.

#### Syntax

```sql
DROP ROLE <role_name>
```

#### Parameters

- **`<role_name>`**  
  Name of the role.

#### Examples

```sql
DROP ROLE role1
```

### `DROP TABLE`

Removes a table from your data source.

#### Syntax

```sql
DROP TABLE [ IF EXISTS ] <table_name>
```

#### Parameters

- **`IF EXISTS`**  
  Prevent error if table doesn't exist.

- **`<table_name>`**  
  Name of the table.

#### Example

```sql
DROP TABLE demo.example_table
```


### `DROP USER`

Removes a user.

#### Syntax

```sql
DROP USER <username>
```

#### Parameters

- **`<username>`**  
  Email of the user (in double quotes).

#### Example

```sql
DROP USER "user@dremio.com"
```

### `DROP VIEW`

Removes a view.

#### Syntax

```sql
DROP VIEW [ IF EXISTS ] <view_name>
```

#### Parameters

- **`IF EXISTS`**  
  Prevent error if view doesn't exist.

- **`<view_name>`**  
  Name of the view.

#### Examples

```sql
DROP VIEW demo.example_view
```

### `GRANT ROLE`

Grant a role to a user or a role.

#### Syntax

```sql
GRANT ROLE <role_name> TO { ROLE | USER } <role_or_user_name>
```

#### Parameters

- **`<role_name>`**  
  Name of the role to grant.

- **`TO { ROLE | USER } <role_or_user_name>`**  
  Recipient role or user.

#### Examples

##### Grant role to user
```sql
GRANT ROLE role1 TO USER "user@dremio.com"
```

##### Grant role to role
```sql
GRANT ROLE subrole TO ROLE role1
```


### `GRANT TO ROLE`

Grant privileges to a role.

#### Syntax

```sql
GRANT { <objectPrivilege> | ALL } ON { <object_type> <object_name> } TO ROLE <role_name>
```

#### Parameters

- **`<objectPrivilege>`**  
  Privilege to grant (e.g., `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `ALTER`, `DROP`, `OWNERSHIP`).

- **`<object_type>`**  
  Type of object (e.g., `PROJECT`, `SOURCE`, `TABLE`, `VIEW`, `FOLDER`).

- **`<object_name>`**  
  Name of the object.

- **`<role_name>`**  
  Name of the role.

#### Examples

##### Grant create project
```sql
GRANT CREATE PROJECT, CREATE CLOUD ON ORG TO ROLE "DATA_ENGINEER"
```

##### Grant select on table
```sql
GRANT SELECT ON TABLE myTable TO ROLE "DATA_ENGINEER"
```

### `GRANT TO USER`

Grant privileges to a user.

#### Syntax

```sql
GRANT { <objectPrivilege> | ALL } ON { <object_type> <object_name> } TO USER <username>
```

#### Parameters

- **`<objectPrivilege>`**  
  Privilege to grant.

- **`<object_type>`**  
  Type of object.

- **`<object_name>`**  
  Name of the object.

- **`<username>`**  
  Email of the user.

#### Examples

##### Grant select on project
```sql
GRANT SELECT ON PROJECT TO USER "user@dremio.com"
```

##### Grant ownership on catalog
```sql
GRANT OWNERSHIP ON CATALOG prodCatalog TO USER "user@dremio.com"
```

### `RESET ENGINE`

Clears any session-specific execution engine set using the SET ENGINE command.

#### Syntax

```sql
RESET ENGINE
```

#### Examples

```sql
RESET ENGINE;
```


### `REVOKE FROM ROLE`

Revoke privileges from a role.

#### Syntax

```sql
REVOKE { <objectPrivilege> | ALL } ON { <object_type> <object_name> } FROM ROLE <role_name>
```

#### Parameters

- **`<objectPrivilege>`**  
  Privilege to revoke.

- **`<object_type>`**  
  Type of object.

- **`<object_name>`**  
  Name of the object.

- **`<role_name>`**  
  Name of the role.

#### Examples

##### Revoke modify from role
```sql
REVOKE MODIFY, MONITOR ON CLOUD "Default Cloud" FROM ROLE "DATA_ENGINEER"
```

##### Revoke ownership from role
```sql
REVOKE OWNERSHIP ON CATALOG prodCatalog FROM ROLE data_engineer
```

### `REVOKE FROM USER`

Revoke privileges from a user.

#### Syntax

```sql
REVOKE { <objectPrivilege> | ALL } ON { <object_type> <object_name> } FROM USER <username>
```

#### Parameters

- **`<objectPrivilege>`**  
  Privilege to revoke.

- **`<object_type>`**  
  Type of object.

- **`<object_name>`**  
  Name of the object.

- **`<username>`**  
  Email of the user.

#### Examples

##### Revoke select from user
```sql
REVOKE SELECT ON PROJECT FROM USER "user@dremio.com"
```

##### Revoke ownership from user
```sql
REVOKE OWNERSHIP ON CATALOG prodCatalog FROM USER "user@dremio.com"
```

### `REVOKE ROLE`

Revoke a role from the role or user.

#### Syntax

```sql
REVOKE ROLE <role_name> FROM { ROLE | USER } <role_or_user_name>
```

#### Parameters

- **`<role_name>`**  
  Name of the role to revoke.

- **`FROM { ROLE | USER } <role_or_user_name>`**  
  Role or user to revoke from.

#### Example

```sql
REVOKE ROLE role1 FROM USER "user@dremio.com"
```


### `SET ENGINE`

Specify the engine that will be used to execute subsequent queries in the current session.

#### Syntax

```sql
SET ENGINE <engine_name>
```

#### Parameters

- **`<engine_name>`**  
  Name of the engine.

#### Examples

```sql
SET ENGINE first_engine;
```

### `SET TAG`

Specify the routing tag that will be used to route subsequent queries in the current session.

#### Syntax

```sql
SET TAG <tag_name>
```

#### Parameters

- **`<tag_name>`**  
  Name of the routing tag.

#### Examples

```sql
SET TAG Dashboard;
```

### `SHOW CREATE TABLE`

Show the definition that creates the specified table.

#### Syntax

```sql
SHOW CREATE TABLE <table_name>
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

#### Examples

```sql
SHOW CREATE TABLE "company_data".employees
```


### `SHOW CREATE VIEW`

Show the definition for a view.

#### Syntax

```sql
SHOW CREATE VIEW <view_name>
```

#### Parameters

- **`<view_name>`**  
  Name of the view.

#### Examples

```sql
SHOW CREATE VIEW "company_data".Locations."offices_by_region"
```

### `SHOW FUNCTIONS`

Returns the list of user-defined functions (UDFs).

#### Syntax

```sql
SHOW FUNCTIONS [ AS OF <timestamp> ] [ LIKE { <pattern> } ]
```

#### Parameters

- **`AS OF <timestamp>`**  
  Optional timestamp.

- **`LIKE { <pattern> }`**  
  Optional pattern to filter results.

#### Examples

##### Show all functions
```sql
SHOW FUNCTIONS;
```

##### Show functions matching pattern
```sql
SHOW FUNCTIONS LIKE 'hello';
```

### `SHOW TABLES`

Show all the tables that are available in a catalog.

#### Syntax

```sql
SHOW TABLES [ IN <catalog_name> ]
```

#### Parameters

- **`IN <catalog_name>`**  
  Optional catalog name.

#### Examples

##### Show tables
```sql
SHOW TABLES
```

##### Show tables in catalog
```sql
SHOW TABLES IN myCatalog
```


### `SHOW VIEWS`

Show all the views that are available in a catalog.

#### Syntax

```sql
SHOW VIEWS [ IN <catalog_name> ]
```

#### Parameters

- **`IN <catalog_name>`**  
  Optional catalog name.

#### Examples

##### Show views
```sql
SHOW VIEWS
```

##### Show views in catalog
```sql
SHOW VIEWS IN myCatalog
```

### `RESET TAG`

Clears any session-specific routing tag set using the SET TAG command.

#### Syntax

```sql
RESET TAG
```

#### Examples

```sql
RESET TAG;
```

### `VACUUM TABLE`

Remove older table snapshots and orphan files from Iceberg tables.

#### Syntax

```sql
VACUUM TABLE <table_name>
{ EXPIRE SNAPSHOTS [ older_than = <timestamp> ] [ retain_last = <count> ]
| REMOVE ORPHAN FILES [ older_than = <timestamp> ] [ location = <path> ] }
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

- **`EXPIRE SNAPSHOTS`**  
  Remove old snapshots.
  - `older_than`: Timestamp limit (default: 5 days ago).
  - `retain_last`: Minimum snapshots to keep.

- **`REMOVE ORPHAN FILES`**  
  Remove files not in metadata.
  - `older_than`: Creation timestamp limit (default: 3 days ago).
  - `location`: Directory to search.

#### Examples

##### Expire snapshots
```sql
VACUUM TABLE my_table EXPIRE SNAPSHOTS older_than = '2023-01-01 00:00:00.000' retain_last = 5
```

##### Remove orphan files
```sql
VACUUM TABLE my_table REMOVE ORPHAN FILES older_than = '2023-01-01 00:00:00.000'
```


### `WITH`

Defines a common table expression (CTE), which is a temporary named result set.

#### Syntax

```sql
WITH <cte_name> [ ( <cte_column1>, <cte_column2>, ... ) ] AS ( <query> )
SELECT ...
```

#### Parameters

- **`<cte_name>`**  
  Name of the CTE.

- **`<cte_column>`**  
  Optional column names.

- **`AS ( <query> )`**  
  Query defining the CTE.

#### Examples

```sql
WITH cte_quantity (Total) AS ( SELECT SUM(passenger_count) as Total FROM Samples."samples.dremio.com"."NYC-taxi-trips" where passenger_count > 2 GROUP BY pickup_datetime )
SELECT AVG(Total) average_pass FROM cte_quantity
```

### `DELETE`

Delete rows from a table.

#### Syntax

```sql
DELETE FROM <table_name> [ AS <alias> ] [ USING <additional_table_or_query> ] [ WHERE <where_conditions> ]
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

- **`USING <additional_table>`**  
  Additional tables for join conditions.

- **`WHERE <where_conditions>`**  
  Filter for rows to delete.

#### Examples

##### Delete with join
```sql
DELETE FROM orders USING returns WHERE orders.order_id = returns.order_id;
```

##### Delete with subquery
```sql
DELETE FROM orders WHERE EXISTS (select 1 from returns where order_id = orders.order_id)
```

### `INSERT`

Insert records into a table.

#### Syntax

```sql
INSERT INTO <table_name> [ ( <column_name> [ , ... ] ) ]
{ <select_statement> | VALUES ( <value> [ , ... ] ) [ , ... ] }
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

- **`( <column_name> ... )`**  
  Optional column list.

- **`VALUES`**  
  List of values to insert.

#### Examples

##### Insert values
```sql
INSERT INTO myTable VALUES (21, 'Ruth Asawa'), (38, 'Magdalena Abakanowicz')
```

##### Insert from select
```sql
INSERT INTO struct_type VALUES (convert_from('{ x: "hi" }', 'json'))
```


### `MERGE`

Run insert or update operations on a target table from the results of a join with a source table.

#### Syntax

```sql
MERGE INTO <target_table> [ AS <target_alias> ]
USING <source_table> [ AS <source_alias> ]
ON ( <condition> )
[ WHEN MATCHED THEN UPDATE SET <column> = <value> [ , ... ] ]
[ WHEN NOT MATCHED THEN INSERT ( <column> [ , ... ] ) VALUES ( <value> [ , ... ] ) ]
```

#### Parameters

- **`<target_table>`**  
  Table to merge into.

- **`USING <source_table>`**  
  Source table for data.

- **`ON ( <condition> )`**  
  Join condition.

- **`WHEN MATCHED THEN UPDATE`**  
  Update existing rows.

- **`WHEN NOT MATCHED THEN INSERT`**  
  Insert new rows.

#### Examples

```sql
MERGE INTO target_table AS t USING source_table AS s ON (t.id = s.id)
WHEN MATCHED THEN UPDATE SET description = s.description_2
WHEN NOT MATCHED THEN INSERT (id, description) VALUES (s.id, s.description_1);
```

### `OPTIMIZE TABLE`

Rewrite data and manifest files to provide peak performance.

#### Syntax

```sql
OPTIMIZE TABLE <table_name>
[ REWRITE DATA [ USING BIN_PACK ]
  [ ( { TARGET_FILE_SIZE_MB | MIN_FILE_SIZE_MB | MAX_FILE_SIZE_MB | MIN_INPUT_FILES } = <value> [, ... ] ) ]
  [ FOR PARTITIONS <predicate> ] ]
[ REWRITE MANIFESTS ]
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

- **`REWRITE DATA`**  
  Rewrite data files.
  - `TARGET_FILE_SIZE_MB`: Target size.
  - `MIN_INPUT_FILES`: Min files to trigger optimization.

- **`FOR PARTITIONS`**  
  Filter partitions to optimize.

- **`REWRITE MANIFESTS`**  
  Optimize manifest files.

#### Examples

##### Optimize data
```sql
OPTIMIZE TABLE demo.example_table REWRITE DATA USING BIN_PACK (TARGET_FILE_SIZE_MB=512, MIN_INPUT_FILES=10)
```

##### Optimize manifests
```sql
OPTIMIZE TABLE demo.example_table REWRITE MANIFESTS
```

### `ROLLBACK TABLE`

Roll back an Iceberg table to a previous snapshot.

#### Syntax

```sql
ROLLBACK TABLE <table_name> TO { SNAPSHOT '<snapshot_id>' | TIMESTAMP '<timestamp>' }
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

- **`TO SNAPSHOT '<snapshot_id>'`**  
  Rollback to snapshot ID.

- **`TO TIMESTAMP '<timestamp>'`**  
  Rollback to timestamp.

#### Examples

##### Rollback to snapshot
```sql
ROLLBACK TABLE demo.example_table TO SNAPSHOT '2489484212521283189'
```

##### Rollback to timestamp
```sql
ROLLBACK TABLE demo.example_table TO TIMESTAMP '2022-06-22 17:06:00'
```


### `TRUNCATE`

Delete all rows from a table with minimal computation.

#### Syntax

```sql
TRUNCATE [ TABLE ] [ IF EXISTS ] <table_name>
```

#### Parameters

- **`TABLE`**  
  Optional keyword.

- **`IF EXISTS`**  
  Prevent error if table missing.

- **`<table_name>`**  
  Name of the table.

#### Examples

```sql
TRUNCATE TABLE IF EXISTS myTable
```

### `UPDATE`

Update rows in a table.

#### Syntax

```sql
UPDATE <table_name> [ AS <alias> ]
SET <column> = <value> [ , ... ]
[ WHERE <condition> ]
```

#### Parameters

- **`<table_name>`**  
  Name of the table.

- **`SET <column> = <value>`**  
  Columns to update.

- **`WHERE <condition>`**  
  Filter for rows to update.

#### Examples

```sql
UPDATE MYSOURCE.MYTABLE SET EXPR$0 = s.EXPR$1 FROM MYSOURCE.MYTABLE2 AS s
```

## SQL Functions



















### ABS

Returns the absolute value of the argument.

#### Syntax

```sql
ABS(numeric_expression NUMERIC) → NUMERIC
```

#### Parameters

- `numeric_expression`: BINARY, DECIMAL, DOUBLE, FLOAT, INTEGER

#### Examples

```sql
SELECT ABS(0.0) -- 0.0
SELECT ABS(-2) -- 2
SELECT ABS(NULL) -- null
```

### ACOS

Returns the arc cosine of the argument.

#### Syntax

```sql
ACOS(numeric_expression NUMERIC) → FLOAT
```

#### Parameters

- `numeric_expression`: The number in radians. This must be DOUBLE, INTEGER, BIGINT, DECIMAL, or FLOAT.

#### Examples

```sql
SELECT ACOS(0) -- 1.5707963267948966
SELECT ACOS(1.0) -- 0.0
SELECT ACOS(-1) -- 3.141592653589793
```

### AES_DECRYPT

Decrypts a string using AES encryption.

#### Syntax

```sql
AES_DECRYPT(ciphertext varchar, key varchar) → varchar
```

#### Parameters

- `ciphertext`: The string to be decrypted.
- `key`: The key to use to decrypt the ciphertext. Must be 16, 24, or 32 characters.

#### Examples

```sql
SELECT AES_DECRYPT(UNBASE64('UvicDn/xiUDmfSE+KYjjyw=='), 'mypassword123456') -- Dremio
```

### AES_ENCRYPT

Encrypts a string using AES encryption.

#### Syntax

```sql
AES_ENCRYPT(plaintext varchar, key varchar) → varchar
```

#### Parameters

- `plaintext`: The string to be encrypted.
- `key`: The key to use to encrypt the plaintext. Must be 16, 24, or 32 characters.

#### Examples

```sql
SELECT BASE64(AES_ENCRYPT('Dremio', 'mypassword123456')) -- UvicDn/xiUDmfSE+KYjjyw==
```

### AI_CLASSIFY

Classifies text using a Large Language Model (LLM).

#### Syntax

```sql
AI_CLASSIFY( [model_name VARCHAR,] prompt VARCHAR | (prompt VARCHAR, file_reference), categories ARRAY<VARCHAR|INT|FLOAT|BOOLEAN> ) → VARCHAR|INT|FLOAT|BOOLEAN
```

#### Parameters

- `model_name` (optional): Optional model specification in format 'modelProvider.modelName' (e.g., 'gpt.4o').
- `prompt`: Classification instructions for the LLM. Use (prompt, file_reference) to process files from LIST_FILES.
- `categories`: Array of possible classifications. The LLM will choose one of these values as the result.

#### Examples

```sql
SELECT recipe_name, AI_CLASSIFY( 'Determine the difficulty level based on these ingredients and steps', ingredients || ' - Steps: ' || cooking_instructions, ARRAY['Beginner', 'Easy', 'Intermediate', 'Advanced', 'Expert'] ) AS difficulty_level, prep_time, number_of_ingredients FROM recipe_database;
```

### AI_COMPLETE

Generates text completion using a Large Language Model (LLM).

#### Syntax

```sql
AI_COMPLETE( [model_name VARCHAR,] prompt VARCHAR ) → VARCHAR
```

#### Parameters

- `model_name` (optional): Optional model specification in format 'modelProvider.modelName'.
- `prompt`: Completion instruction for the LLM. Natural language text describing what you want the model to generate.

#### Examples

```sql
SELECT dish_name, AI_COMPLETE( 'Write an appetizing menu description for this dish: ' || dish_name || '. Main ingredients: ' || main_ingredients || '. Cooking style: ' || cuisine_type ) AS menu_description FROM restaurant_dishes;
```

### AI_GENERATE

Generates structured data or text using a Large Language Model (LLM).

#### Syntax

```sql
AI_GENERATE( [model_name VARCHAR,] prompt VARCHAR | (prompt VARCHAR, file_reference) [WITH SCHEMA data_type] ) → ANY|ROW
```

#### Parameters

- `model_name` (optional): Optional model specification in format 'modelProvider.modelName'.
- `prompt`: Natural language instruction for the LLM. Use (prompt, file_reference) to process files from LIST_FILES.
- `WITH SCHEMA data_type`: Output structure specification (optional).

#### Examples

```sql
WITH recipe_analysis AS ( SELECT file['path'] AS recipe_file, AI_GENERATE( 'gpt.4o', ('Extract recipe details', file) WITH SCHEMA ROW( recipe_name VARCHAR, cuisine_type VARCHAR) ) AS recipe_info FROM TABLE(LIST_FILES('@Cookbooks/cookbook_recipes')) WHERE file['path'] LIKE '%.pdf' ) SELECT recipe_file, recipe_info['recipe_name'] AS recipe, recipe_info['cuisine_type'] AS cuisine FROM recipe_analysis ORDER BY recipe ASC;
```

### APPROX_COUNT_DISTINCT

Returns the approximate number of distinct values in a column.

#### Syntax

```sql
APPROX_COUNT_DISTINCT(column_name any primitive) → BIGINT
```

#### Parameters

- `column_name`: You can specify a column of any primitive data type.

#### Examples

```sql
SELECT APPROX_COUNT_DISTINCT(IncidntNum) FROM Samples."samples.dremio.com"."SF_incidents2016.json" -- 116696
```

### APPROX_PERCENTILE

Returns the approximate percentile of a column.

#### Syntax

```sql
APPROX_PERCENTILE(column_name numeric, percentile double) → DOUBLE
```

#### Parameters

- `column_name`: The column for which to compute the approximate percentile.
- `percentile`: The percentile to use in the approximation. Must be a number between 0 and 1.

#### Examples

```sql
SELECT APPROX_PERCENTILE(pop, 0.5) FROM Samples."samples.dremio.com"."zips.json" -- 2780.17855684608
```

### ARRAYS_OVERLAP

Checks if two arrays have any elements in common.

#### Syntax

```sql
ARRAYS_OVERLAP(arr1 LIST, arr2 LIST) → BOOLEAN
```

#### Parameters

- `arr1`: The first array.
- `arr2`: The second array.

#### Examples

```sql
SELECT ARRAYS_OVERLAP(ARRAY['foo', 'bar'], ARRAY['bar', 'baz']) -- true
SELECT ARRAYS_OVERLAP(ARRAY['foo', 'bar'], ARRAY['baz', 'qux']) -- false
```

### ARRAY_AGG

Aggregates values into an array.

#### Syntax

```sql
ARRAY_AGG ( [ DISTINCT ] expression ) → array
```

#### Parameters

- `expression`: An expression of any primitive type to aggregate into an array.

#### Examples

```sql
SELECT ARRAY_AGG(name) FROM <catalog-name>.people; -- ['Bob', 'Charlie', 'Alice']
```

### ARRAY_APPEND

Appends an element to an array.

#### Syntax

```sql
ARRAY_APPEND(array LIST, element ANY) → LIST
```

#### Parameters

- `array`: The array to append to.
- `element`: The element to append to the array.

#### Examples

```sql
SELECT ARRAY_APPEND(ARRAY[1, 2], 3); -- [1, 2, 3]
```

### ARRAY_AVG

Returns the average of the elements in an array.

#### Syntax

```sql
ARRAY_AVG(list_column LIST) → numeric
```

#### Parameters

- `list_column`: Column that contains a LIST expression. Every element of the list must be a number.

#### Examples

```sql
SELECT ARRAY_AVG(array_col) -- 2
```

### ARRAY_CAT

Concatenates two arrays.

#### Syntax

```sql
ARRAY_CAT(arr1 LIST, arr2 LIST) → list
```

#### Parameters

- `arr1`: The source array.
- `arr2`: The array to be appended to the source array.

#### Examples

```sql
SELECT ARRAY_CAT(ARRAY[1, 2, 3], ARRAY[4, 5, 6]) -- [1, 2, 3, 4, 5, 6]
```


### ARRAY_COMPACT

Removes null values from an array.

#### Syntax

```sql
ARRAY_COMPACT(arr LIST) → list
```

#### Parameters

- `arr`: The array from which to remove null values.

#### Examples

```sql
SELECT ARRAY_COMPACT(array_col) -- [1, 2]
```

### ARRAY_CONTAINS

Checks if an array contains a specific value.

#### Syntax

```sql
ARRAY_CONTAINS(list LIST, value any) → boolean
```

#### Parameters

- `list`: The list to search.
- `value`: An expression of a type that is comparable with the LIST.

#### Examples

```sql
SELECT ARRAY_CONTAINS(CONVERT_FROM('["apple", "pear", "banana"]', 'json'), NULL) -- null
SELECT ARRAY_CONTAINS(CONVERT_FROM('["apple", "pear", "banana"]', 'json'), 'pear') -- true
SELECT ARRAY_CONTAINS(CONVERT_FROM('["apple", "pear", "banana"]', 'json'), 'grape') -- false
```

### ARRAY_DISTINCT

Returns an array with distinct elements from the input array.

#### Syntax

```sql
ARRAY_DISTINCT(input LIST) → LIST
```

#### Parameters

- `input`: The input array from which to return only distinct elements.

#### Examples

```sql
SELECT ARRAY_DISTINCT(ARRAY[1, 2, 3, 1, 2, 3]) -- [2, 3, 1]
```

### ARRAY_FREQUENCY

Returns a map where keys are the elements of the array and values are their frequencies.

#### Syntax

```sql
ARRAY_FREQUENCY(array LIST) → MAP
```

#### Parameters

- `array`: The array of values for which to calculate frequency. Accepts primitive types.

#### Examples

```sql
SELECT ARRAY_FREQUENCY(ARRAY[2,1,2,1,1,5]); -- {"1":3, "2":2, "5":1}
SELECT ARRAY_FREQUENCY(ARRAY['a','b','ab','b','a']); -- {"a":2, "ab":1, "b":2}
SELECT ARRAY_FREQUENCY(ARRAY['foo', 'bar', 'FOO', 'foo']); -- {"FOO":1, "bar":1, "foo":2}
SELECT ARRAY_FREQUENCY(array_col); -- {"1":1, "2":2}
```

### ARRAY_GENERATE_RANGE

Generates an array of integers in a specified range.

#### Syntax

```sql
ARRAY_GENERATE_RANGE(start int32, stop int32, step int32) → list
```

#### Parameters

- `start`: The first number in the range of numbers to return.
- `stop`: The last number in the range. Note that this number is not included in the range of numbers returned.
- `step`: The amount to increment or decrement each subsequent number in the array. May be a positive or negative number. Cannot be 0. Default value is 1.

#### Examples

```sql
SELECT ARRAY_GENERATE_RANGE(1, 5) -- [1, 2, 3, 4]
SELECT ARRAY_GENERATE_RANGE(0, 16, 5) -- [0, 5, 10, 15]
SELECT ARRAY_GENERATE_RANGE(0, -16, -5) -- [0, -5, -10, -15]
SELECT ARRAY_GENERATE_RANGE(2, 2, 4) -- []
SELECT ARRAY_GENERATE_RANGE(8, 2, 2) -- []
SELECT ARRAY_GENERATE_RANGE(2, 8, -2) -- []
SELECT ARRAY_GENERATE_RANGE(2, 2) -- []
```

### ARRAY_INSERT

Inserts an element into an array at a specified position.

#### Syntax

```sql
ARRAY_INSERT(arr LIST, position INT, new_element ANY) → LIST
```

#### Parameters

- `arr`: The array to search.
- `position`: The zero-based position in the input array where the new element should be inserted.
- `new_element`: The new element to insert in the specified position.

#### Examples

```sql
SELECT ARRAY_INSERT(ARRAY[1, 2, 3, 4, 5], 2, 55); -- [1, 2, 55, 3, 4, 5]
SELECT ARRAY_INSERT(ARRAY[1, 2, 3], 6, 55); -- [1, 2, 3, NULL, NULL, NULL, 55]
SELECT ARRAY_INSERT(ARRAY[1, 2, 3], -1, 55); -- [1, 2, 55, 3]
```

### ARRAY_MAX

Returns the maximum value in an array.

#### Syntax

```sql
ARRAY_MAX(list_column LIST) → numeric
```

#### Parameters

- `list_column`: Column that contains a LIST expression. Every element of the list must be a number such as INT, BIGINT, FLOAT4, FLOAT8, or DECIMAL. Cannot be an array literal.

#### Examples

```sql
SELECT ARRAY_MAX(array_col) -- 3
SELECT ARRAY_MAX(array_col) -- NULL
```

### ARRAY_MIN

Returns the minimum value in an array.

#### Syntax

```sql
ARRAY_MIN(list_column LIST) → numeric
```

#### Parameters

- `list_column`: Column that contains a LIST expression. Every element of the list must be a number such as INT, BIGINT, FLOAT4, FLOAT8, or DECIMAL. Cannot be an array literal.

#### Examples

```sql
SELECT ARRAY_MIN(array_col) -- 1
SELECT ARRAY_MIN(array_col) -- NULL
```

### ARRAY_POSITION

Returns the position of the first occurrence of an element in an array.

#### Syntax

```sql
ARRAY_POSITION(element ANY, arr LIST) → numeric
```

#### Parameters

- `element`: Element to find in the array.
- `arr`: The array to search.

#### Examples

```sql
SELECT ARRAY_POSITION(CAST(3 AS BIGINT), ARRAY[1, 2, 3]) -- 2
SELECT ARRAY_POSITION(4, ARRAY[1, 2, 3]) -- NULL
SELECT ARRAY_POSITION(NULL, array_col) -- 1
SELECT ARRAY_POSITION(ARRAY[2,3], ARRAY[ARRAY[1,2], ARRAY[2,3]]) -- 1
```

### ARRAY_PREPEND

Prepends an element to the beginning of an array.

#### Syntax

```sql
ARRAY_PREPEND(element ANY, array LIST) → LIST
```

#### Parameters

- `element`: The element to prepend to the array.
- `array`: The array to prepend to.

#### Examples

```sql
SELECT ARRAY_PREPEND(1, ARRAY[2, 3]); -- [1, 2, 3]
```

### ARRAY_REMOVE

Removes all occurrences of a value from an array.

#### Syntax

```sql
ARRAY_REMOVE(list_column LIST, value any) → list
```

#### Parameters

- `list_column`: Column that contains a LIST expression. Cannot be an array literal.
- `value`: An expression of any data type.

#### Examples

```sql
SELECT ARRAY_REMOVE(array_col, 1) -- [2, 3]
SELECT ARRAY_REMOVE(array_col, 2) -- [1,null]
SELECT ARRAY_REMOVE(array_col, null) -- NULL
SELECT ARRAY_REMOVE(array_col, 2) -- NULL
SELECT ARRAY_REMOVE(null, 2) -- NULL
```

### ARRAY_REMOVE_AT

Removes the element at a specified position from an array.

#### Syntax

```sql
ARRAY_REMOVE_AT(arr LIST, position int32) → list
```

#### Parameters

- `arr`: Array from which to remove the element at the specified position.
- `position`: The zero-based position of the element to be removed. The function removes the element at the specified position. A negative position is interpreted as an index from the back of the array. For example, the value -1 removes the last element in the array.

#### Examples

```sql
SELECT ARRAY_REMOVE_AT(ARRAY[1, 2, 3], 1) -- [1, 3]
SELECT ARRAY_REMOVE_AT(ARRAY[1, 2, 3], -1) -- [1, 2]
SELECT ARRAY_REMOVE_AT(ARRAY[1, 2, 3], 10) -- [1, 2, 3]
```

### ARRAY_SIZE

Returns the number of elements in an array.

#### Syntax

```sql
ARRAY_SIZE(arr LIST) → numeric
```

#### Parameters

- `arr`: The source array.

#### Examples

```sql
SELECT ARRAY_SIZE(ARRAY[1, 4, 5]) -- 3
```

### ARRAY_SLICE

Returns a subset of an array.

#### Syntax

```sql
ARRAY_SLICE(arr LIST, from int, to int) → LIST
```

#### Parameters

- `arr`: The input array.
- `from`: The zero-based position in the input array of the first element to include in the output array. Elements in positions that are less than the from position are not included in the output array. A negative position is interpreted as an index from the back of the array. For example, the value -1 begins the output array with the last element in the input array.
- `to`: The zero-based position in the input array of the last element to include in the output array. Elements in positions that are equal to or greater than the to position are not included in the resulting array. A negative position is interpreted as an index from the back of the array. For example, the value -1 ends the output array with the second-to-last element in the input array.

#### Examples

```sql
SELECT ARRAY_SLICE(array_col) -- [0,1,2]
SELECT ARRAY_SLICE(array_col) -- [0,1,2,3,4]
SELECT ARRAY_SLICE(array_col) -- [2,3]
SELECT ARRAY_SLICE(array_col) -- []
```

### ARRAY_SUM

Returns the sum of the elements in an array.

#### Syntax

```sql
ARRAY_SUM(list_column LIST) → numeric
```

#### Parameters

- `list_column`: Column that contains a LIST expression. Every element of the list must be a number such as INT, BIGINT, FLOAT4, FLOAT8, or DECIMAL. Cannot be an array literal.

#### Examples

```sql
SELECT ARRAY_SUM(array_col) -- 6
SELECT ARRAY_SUM(array_col) -- 3
SELECT ARRAY_SUM(array_col) -- 0
SELECT ARRAY_SUM(array_col) -- NULL
```

### ARRAY_TO_STRING

Converts an array to a string, with elements separated by a delimiter.

#### Syntax

```sql
ARRAY_TO_STRING(arr LIST, delimiter VARCHAR) → VARCHAR
```

#### Parameters

- `arr`: The source array.
- `delimiter`: The string to place between each element in the array.

#### Examples

```sql
SELECT ARRAY_TO_STRING(ARRAY[1, 2, 3], ',') -- 1,2,3
SELECT ARRAY_TO_STRING(array_col, ',') -- 1,,3
```

### ASCII

Returns the ASCII code value of the leftmost character of the string.

#### Syntax

```sql
ASCII(expression varchar) → int32
```

#### Parameters

- `expression`: The string for which the ASCII code for the first character in the string is returned.

#### Examples

```sql
SELECT ASCII ('DREMIO') -- 68
SELECT ASCII ('D') -- 68
SELECT ASCII ('') -- 0
```

### ASIN

Returns the arc sine of the argument.

#### Syntax

```sql
ASIN(numeric_expression NUMERIC) → FLOAT
```

#### Parameters

- `numeric_expression`: The number in radians. This must be DOUBLE, INTEGER, or FLOAT.

#### Examples

```sql
SELECT ASIN(0) -- 0.0
SELECT ASIN(1) -- 1.5707963267948966
SELECT ASIN(-1) -- -1.5707963267948966
```

### ATAN

Returns the arc tangent of the argument.

#### Syntax

```sql
ATAN(inputValue FLOAT) → FLOAT
```

#### Parameters

- `inputValue`: Floating-point input value, in the range (negative-infinity:positive-infinity)

#### Examples

```sql
SELECT ATAN(0) -- 0.0
SELECT ATAN(1) -- 0.7853981633974483
SELECT ATAN(-1) -- -0.7853981633974483
SELECT ATAN(19564.7) -- 1.5707452143321894
```

### ATAN2

Returns the arc tangent of the two arguments.

#### Syntax

```sql
ATAN2(y NUMERIC, x NUMERIC) → DOUBLE
```

#### Parameters

- `y`: Floating-point input value for the y-coordinate, in the range (negative-infinity:positive-infinity).
- `x`: Floating-point input value for the x-coordinate, in the range (negative-infinity:positive-infinity).

#### Examples

```sql
SELECT ATAN2(1.0,0.0) -- 1.5707963267948966
SELECT ATAN2(0.0,1.0) -- 0.0
SELECT ATAN2(0.0,-1.0) -- 3.141592653589793
SELECT ATAN2(-0.00000000001,-1.0) -- -3.141592653579793
SELECT ATAN2(0.0,0.0) -- 0.0
```

### AVG

Returns the average of the values in a group.

#### Syntax

```sql
AVG(numeric_expression NUMERIC) → DOUBLE
```

#### Parameters

- `numeric_expression`: The values for which to compute the average. Values can be type DOUBLE, NUMERIC, INTEGER, INTERVAL_DATE, or INTERVAL_YEAR.

#### Examples

```sql
SELECT AVG(3) -- 3.0
SELECT AVG("val_col"); -- -0.333333
```

### BASE64

Encodes a string using Base64.

#### Syntax

```sql
BASE64(expression varbinary) → varchar
```

#### Parameters

- `expression`: The string to encode.

#### Examples

```sql
SELECT BASE64('Dremio') -- RHJlbWlv
```

### BIN

Returns a string representation of the binary value of an integer.

#### Syntax

```sql
BIN(expression integer) → varchar
```

#### Parameters

- `expression`: An integer expression to encode.

#### Examples

```sql
SELECT BIN(100) -- 1100100
SELECT BIN(-100) -- 11111111111111111111111110011100
SELECT BIN(null) -- null
```

### BINARY_STRING

Converts a string to a binary string.

#### Syntax

```sql
BINARY_STRING(expression VARCHAR) → BINARY
```

#### Parameters

- `expression`: Varchar expression to convert to binary

#### Examples

```sql
SELECT BINARY_STRING('DREMIO') -- RFJFTUlP
SELECT BINARY_STRING('000') -- MDAw
```

### BITWISE_AND

Returns the bitwise AND of two numbers.

#### Syntax

```sql
BITWISE_AND(op1 NUMERIC, op2 NUMERIC) → NUMERIC
```

#### Parameters

- `op1`: First operand
- `op2`: Second operand

#### Examples

```sql
SELECT BITWISE_AND(7, 4) -- 4
SELECT BITWISE_AND(1, 2) -- 0
```

### BITWISE_NOT

Returns the bitwise NOT of a number.

#### Syntax

```sql
BITWISE_NOT(op1 NUMERIC) → NUMERIC
```

#### Parameters

- `op1`: Value to invert.

#### Examples

```sql
SELECT BITWISE_NOT(0) -- -1
SELECT BITWISE_NOT(9223372036854775807) -- -9223372036854775808
```

### BITWISE_OR

Returns the bitwise OR of two numbers.

#### Syntax

```sql
BITWISE_OR(op1 NUMERIC, op2 NUMERIC) → NUMERIC
```

#### Parameters

- `op1`: First operand.
- `op2`: Second operand.

#### Examples

```sql
SELECT BITWISE_OR(7, 4) -- 7
SELECT BITWISE_OR(1, 2) -- 3
```

### BITWISE_XOR

Returns the bitwise XOR of two numbers.

#### Syntax

```sql
BITWISE_XOR(op1 NUMERIC, op2 NUMERIC) → NUMERIC
```

#### Parameters

- `op1`: First operand.
- `op2`: Second operand.

#### Examples

```sql
SELECT BITWISE_XOR(7, 4) -- 3
SELECT BITWISE_XOR(1, 2) -- 3
```

### BIT_AND

Returns the bitwise AND of all non-null input values, or null if none.

#### Syntax

```sql
BIT_AND(expression int) → int
```

#### Parameters

- `expression`: An expression that evaluates to a data type that can be cast as an integer.

#### Examples

```sql
SELECT BIT_AND(passenger_count) FROM Samples."samples.dremio.com"."NYC-taxi-trips" -- 0
```

### BIT_LENGTH

Returns the length of the string in bits.

#### Syntax

```sql
BIT_LENGTH(expression binary, varchar) → integer
```

#### Parameters

- `expression`: A binary or varchar expression.

#### Examples

```sql
SELECT BIT_LENGTH(1010) -- 32
SELECT BIT_LENGTH('DREMIO') -- 48
SELECT BIT_LENGTH('abc') -- 24
SELECT BIT_LENGTH(NULL) -- null
```

### BIT_OR

Returns the bitwise OR of all non-null input values, or null if none.

#### Syntax

```sql
BIT_OR(expression int) → int
```

#### Parameters

- `expression`: An expression that evaluates to a data type that can be cast as an integer.

#### Examples

```sql
SELECT BIT_OR(passenger_count) FROM Samples."samples.dremio.com"."NYC-taxi-trips" -- 255
```

### BOOL_AND

Computes the boolean AND of two boolean expressions.

#### Syntax

```sql
BOOL_AND(bool_expression1 boolean, bool_expression2 boolean) → boolean
```

#### Parameters

- `bool_expression1`: Boolean input expression.
- `bool_expression2`: Boolean input expression.

#### Examples

```sql
SELECT BOOL_AND(TRUE, FALSE) -- False
```

### BOOL_OR

Computes the boolean OR of two boolean expressions.

#### Syntax

```sql
BOOL_OR(bool_expression1 boolean, bool_expression2 boolean) → boolean
```

#### Parameters

- `bool_expression1`: Boolean input expression.
- `bool_expression2`: Boolean input expression.

#### Examples

```sql
SELECT BOOL_OR(TRUE, FALSE) -- True
```

### CBRT

Returns the cube root of a number.

#### Syntax

```sql
CBRT(numeric_expression NUMERIC) → FLOAT
```

#### Parameters

- `numeric_expression`: The number (DOUBLE, FLOAT, INTEGER) for which you want to compute the cube root.

#### Examples

```sql
SELECT CBRT(8) -- 2.0
SELECT CBRT(120) -- 4.932424148660941
SELECT CBRT(99.5) -- 4.633839922986558
```

### CEIL

Alias for CEILING.

### CEILING

Returns the smallest integer not less than the argument.

#### Syntax

```sql
CEILING(numeric_expression NUMERIC) → INTEGER
```

#### Parameters

- `numeric_expression`: The number (DOUBLE, FLOAT, INTEGER) for which you want to compute the ceiling.

#### Examples

```sql
SELECT CEILING(3.1459) -- 4
SELECT CEIL(37.775420706711) -- 38
SELECT CEIL(-37.775420706711) -- -37
SELECT CEIL(0) -- 0
```

### CHAR

Alias for CHR.

### CHAR_LENGTH

Returns the number of characters in a string.

#### Syntax

```sql
CHAR_LENGTH(expression STRING) → INTEGER
```

#### Parameters

- `expression`: The expression (VARCHAR) to determine character length for.

#### Examples

```sql
SELECT CHAR_LENGTH('get the char length') -- 19
SELECT CHAR_LENGTH('DREMIO') -- 6
```

### CHARACTER_LENGTH

Returns the number of characters in a string.

#### Syntax

```sql
CHARACTER_LENGTH(expression varchar) → int32
```

#### Parameters

- `expression`: String expression to determine the length of.

#### Examples

```sql
SELECT CHARACTER_LENGTH('DREMIO') -- 6
```

### CHR

Returns the character with the given ASCII code.

#### Syntax

```sql
CHR(integer_expression int32) → varchar
```

#### Parameters

- `integer_expression`: Unicode code point to convert to character.

#### Examples

```sql
SELECT CHR(72) -- H
SELECT CHR(33) -- null
```

### COALESCE

Returns the first non-null expression in the list.

#### Syntax

```sql
COALESCE(expression1, expression2, [ ..., expressionN ]) → same as input type
```

#### Parameters

- `expression`: A combination of symbols and operators that the database evaluates to obtain a single data value. Expressions can be a single constant, variable, column, or scalar function.

#### Examples

```sql
SELECT COALESCE(address1, address2, city, state, zipCode) FROM customers -- 123 Main Street
```

### COL_LIKE

Returns true if the expression matches the pattern.

#### Syntax

```sql
COL_LIKE(expression_col varchar, pattern_col varchar) → boolean
```

#### Parameters

- `expression_col`: A column containing an expression to compare.
- `pattern_col`: A column containing the pattern to compare to the expression.

#### Examples

```sql
-- Assuming table 'names' with columns 'name' and 'pat'
-- values ('john', '%oh%'), ('jacob', '%aco%'), ('bill', '%ob%')
SELECT name FROM names WHERE COL_LIKE(name, pat);
-- john
-- jacob
```

### CONCAT

Concatenates two or more strings.

#### Syntax

```sql
CONCAT(expression1 string [, expression2 string] [, expressionN string]) → string
```

#### Parameters

- `expression1`: First string expression.
- `expression2` (optional): Second string expression.
- `expressionN` (optional): Nth string expression.

#### Examples

```sql
SELECT CONCAT('CON', 'CAT') -- CONCAT
SELECT CONCAT('con', 'cat', NULL) -- concat
```

### CONCAT_WS

Concatenates strings with a separator.

#### Syntax

```sql
CONCAT_WS(separator, expression1, expression2, [ ... expressionN ]) → string
```

#### Parameters

- `separator`: An expression of any character type.
- `expression`: An expression can be any data type. All arguments must be the same data type.

#### Examples

```sql
SELECT CONCAT_WS('-', 'cat', 'dog', 'bird') -- cat-dog-bird
```

### CONVERT_FROM

Converts a binary string to a Dremio data type.

#### Syntax

```sql
CONVERT_FROM(binary_value value_to_convert, data_type name_of_type) → varies
```

#### Parameters

- `binary_value`: The binary string to convert to a Dremio data type.
- `data_type`: The data type of the specified binary string.

#### Examples

```sql
SELECT CONVERT_FROM('["apple", "strawberry", "banana"]', 'json') -- ['apple', 'strawberry', 'banana']
SELECT CONVERT_FROM('{"name":"Gnarly", "age":7, "car":null}', 'json') -- {"name:"Gnarly","age":7}
```

### CONVERT_TO

Converts a value to a binary string.

#### Syntax

```sql
CONVERT_TO(expression value_to_convert, data_type name_of_type) → VARBINARY
```

#### Parameters

- `expression`: The value to convert to a binary string.
- `data_type`: The data type to use for the conversion to a binary string.

#### Examples

```sql
SELECT CONVERT_TO('this value' ,'UTF8') -- dGhpcyB2YWx1ZQ==
```

### CONVERT_TIMEZONE

Converts a timestamp to a different time zone.

#### Syntax

```sql
CONVERT_TIMEZONE([sourceTimezone string], destinationTimezone string, timestamp date, timestamp, or string in ISO 8601 format) → timestamp
```

#### Parameters

- `sourceTimezone` (optional): The time zone of the timestamp. If you omit this parameter, Dremio assumes that the source time zone is UTC.
- `destinationTimezone`: The time zone to convert the timestamp to.
- `timestamp`: The timestamp to convert

#### Examples

```sql
select convert_timezone('America/Los_Angeles', 'America/New_York', '2021-04-01 15:27:32') -- 2021-04-01 18:27:32
select convert_timezone('America/Los_Angeles', 'America/New_York', timestamp '2021-04-01 15:27:32'); -- 2021-04-01 18:27:32
select convert_timezone('PST', 'EST', '2021-04-01 15:27:32') -- 2021-04-01 18:27:32
select convert_timezone('America/Los_Angeles', 'America/New_York', '2021-04-01') -- 2021-04-01 03:00:00
select convert_timezone('America/Los_Angeles', 'America/New_York', date '2021-04-01') -- 2021-04-01 03:00:00
select convert_timezone('EDT', '2021-04-01 15:27:32') -- 2021-04-01 11:27:32
select convert_timezone('PST', '+02:00', '2021-04-01 15:27:32') -- 2021-04-02 01:27:32
```

### CORR

Returns the coefficient of correlation of a set of number pairs.

#### Syntax

```sql
CORR(expression1 numeric, expression2 numeric) → double
```

#### Parameters

- `expression1`: An expression that evaluates to a numeric type. This parameter is the dependent value.
- `expression2`: An expression that evaluates to a numeric type. This parameter is the independent value.

#### Examples

```sql
SELECT "CORR"(100, 4) -- NaN
```

### COS

Returns the cosine of an angle.

#### Syntax

```sql
COS(numeric_expression NUMERIC) → FLOAT
```

#### Parameters

- `numeric_expression`: The number in radians. This must be DOUBLE, INTEGER, or FLOAT.

#### Examples

```sql
SELECT COS(0) -- 1.0
SELECT COS(1.0) -- 0.5403023058681398
SELECT COS(-1) -- 0.5403023058681398
```

### COT

Returns the cotangent of an angle.

#### Syntax

```sql
COT(numeric_expression NUMERIC) → FLOAT
```

#### Parameters

- `numeric_expression`: The number in radians. This must be DOUBLE, INTEGER, or FLOAT.

#### Examples

```sql
SELECT COT(0) -- 1.0
SELECT COT(1.0) -- 0.5403023058681398
SELECT COT(-1) -- 0.5403023058681398
```

### COUNT

Returns the number of rows in the query.

#### Syntax

```sql
COUNT(expression ANY) → BIGINT
```

#### Parameters

- `expression`: The expression to evaluate. Can be an asterisk (*) or the column name of any primitive data type. Use an asterisk to include rows that contain NULL. Use a column name to ignore rows that contain NULL.

#### Examples

```sql
SELECT COUNT(passenger_count) FROM "Samples"."samples.dremio.com"."NYC-taxi-trips"; -- 338293677
```

### COVAR_POP

Returns the population covariance of a set of number pairs.

#### Syntax

```sql
COVAR_POP(expression1 NUMERIC, expression2 NUMERIC) → DOUBLE
```

#### Parameters

- `expression1`: An expression that evaluates to a numeric type. This parameter is the dependent value.
- `expression2`: An expression that evaluates to a numeric type. This parameter is the independent value.

#### Examples

```sql
SELECT COVAR_POP(trip_distance_mi, fare_amount) FROM Samples."samples.dremio.com"."NYC-taxi-trips"; -- 31.705367711861427
SELECT COVAR_POP(DISTINCT trip_distance_mi, fare_amount FROM Samples."samples.dremio.com"."NYC-taxi-trips"; -- 302.592806814534
```

### COVAR_SAMP

Returns the sample covariance of a set of number pairs.

#### Syntax

```sql
COVAR_SAMP(expression1 NUMERIC, expression2 NUMERIC) → DOUBLE
```

#### Parameters

- `expression1`: An expression that evaluates to a numeric type. This parameter is the dependent value.
- `expression2`: An expression that evaluates to a numeric type. This parameter is the independent value.

#### Examples

```sql
SELECT COVAR_SAMP(trip_distance_mi, fare_amount) FROM Samples."samples.dremio.com"."NYC-taxi-trips"; -- 31.705367805565245
SELECT COVAR_SAMP(DISTINCT trip_distance_mi, fare_amount) FROM Samples."samples.dremio.com"."NYC-taxi-trips"; -- 302.5936880585907
```

### CUME_DIST

Calculates the cumulative distribution of a value in a group of values.

#### Syntax

```sql
CUME_DIST() OVER ( [PARTITION BY partition_expression] [ORDER BY order_expression]) → double
```

#### Parameters

- `partition_expression` (optional): An expression that groups rows into partitions.
- `order_expression`: An expression that specifies the order of the rows within each partition.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", CUME_DIST() OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
-- Category, Descript, DayOfWeek, EXPR$3
-- ARSON, ARSON, Friday, 0.13636363636363635
-- EMBEZZLEMENT, EMBEZZLED VEHICLE, Friday, 0.18452380952380953
```

### CURRENT_DATE

Returns the current date.

#### Syntax

```sql
CURRENT_DATE() → date
```

#### Examples

```sql
SELECT CURRENT_DATE() -- 2021-07-02
SELECT CURRENT_DATE -- 2021-07-02
```

### CURRENT_TIME

Returns the current time.

#### Syntax

```sql
CURRENT_TIME() → TIME
```

#### Examples

```sql
SELECT CURRENT_TIME() -- 06:04:31
SELECT CURRENT_TIME -- 06:04:31
```

### CURRENT_TIMESTAMP

Returns the current timestamp.

#### Syntax

```sql
CURRENT_TIMESTAMP() → TIMESTAMP
```

#### Examples

```sql
SELECT CURRENT_TIMESTAMP() -- 2021-06-24 06:11:51.567000
```

### DATE_ADD

Adds a specified number of days or a time interval to a date or timestamp.

#### Syntax

```sql
DATE_ADD(date_expression string, days integer) → date
DATE_ADD(date_expression date, days integer) → date
DATE_ADD(date_expression string, time_interval interval) → timestamp
DATE_ADD(date_expression date, time_interval interval) → timestamp
DATE_ADD(timestamp_expression string, time_interval interval) → timestamp
```

#### Parameters

- `date_expression`: A string-formatted date ('YYYY-MM-DD') or a DATE column/literal.
- `days`: The number of days to add.
- `time_interval`: A CAST of a number to an interval (e.g., DAY, MONTH, YEAR).
- `timestamp_expression`: A string-formatted timestamp ('YYYY-MM-DD HH24:MI:SS').

#### Examples

```sql
SELECT DATE_ADD('2022-01-01', 2) -- 2022-01-03
SELECT DATE_ADD(DATE '2022-01-01', 30) -- 2022-01-31
SELECT DATE_ADD('2022-01-01', CAST(2 AS INTERVAL DAY)) -- 2022-01-03 00:00:00.000
SELECT DATE_ADD('2022-01-01 12:00:00', CAST(30 AS INTERVAL DAY)) -- 2022-01-31 00:00:00.000
```

### DATE_DIFF

Returns the difference between two dates or timestamps.

#### Syntax

```sql
DATE_DIFF(date_expression DATE, days INTEGER) → DATE
DATE_DIFF(date_expression DATE, date_expression DATE) → INTERVAL DAY
DATE_DIFF(timestamp_expression TIMESTAMP, timestamp_expression TIMESTAMP) → INTERVAL DAY
DATE_DIFF(time_expression TIME, time_interval INTERVAL) → TIME
```

#### Parameters

- `date_expression`: The date to subtract from or subtract days from.
- `days`: Number of days to subtract.
- `timestamp_expression`: The timestamp to subtract from.
- `time_expression`: The time to subtract from.
- `time_interval`: Interval to subtract.

#### Examples

```sql
SELECT DATE_DIFF(DATE '2022-01-01', 5) -- 2021-12-27
SELECT DATE_DIFF(DATE '2022-04-01', DATE '2022-01-01') -- +090 00:00:00.000
SELECT DATE_DIFF(TIMESTAMP '2022-04-01 12:35:23', TIMESTAMP '2022-01-01 01:00:00') -- +090 11:35:23.000
SELECT DATE_DIFF(TIME '12:00:00', CAST(30 AS INTERVAL SECOND)) -- 11:59:30
```

### DATE_PART

Extracts a subfield from a date or timestamp.

#### Syntax

```sql
DATE_PART(field string, source date or timestamp) → integer
```

#### Parameters

- `field`: Must be one of: YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE, SECOND.
- `source`: The value from which to extract the subfield

#### Examples

```sql
select date_part('year', timestamp '2021-04-01 15:27:32') -- 2021
select date_part('month', date '2021-04-01') -- 4
```

### DATE_SUB

Subtracts a specified number of days or a time interval from a date or timestamp.

#### Syntax

```sql
DATE_SUB(date_expression STRING, days INTEGER) → DATE
DATE_SUB(date_expression DATE, days INTEGER) → DATE
DATE_SUB(date_expression STRING, time_interval INTERVAL) → TIMESTAMP
DATE_SUB(date_expression DATE, time_interval INTERVAL) → TIMESTAMP
DATE_SUB(timestamp_expression STRING, time_interval INTERVAL) → TIMESTAMP
```

#### Parameters

- `date_expression`: A string-formatted date ('YYYY-MM-DD') or a DATE column/literal.
- `days`: The number of days to subtract.
- `time_interval`: A CAST of a number to an interval.
- `timestamp_expression`: A string-formatted timestamp.

#### Examples

```sql
SELECT DATE_SUB('2022-01-01', 2) -- 2021-12-30
SELECT DATE_SUB(DATE '2022-01-01', 30) -- 2021-12-02
SELECT DATE_SUB('2022-01-01', CAST(2 AS INTERVAL DAY)) -- 2021-12-30 00:00:00.000
SELECT DATE_SUB('2022-01-01 12:00:00', CAST(30 AS INTERVAL DAY)) -- 2021-12-02 00:00:00.000
```

### DATE_TRUNC

Truncates a date or timestamp to the specified time unit.

#### Syntax

```sql
DATE_TRUNC(time_unit LITERAL, date_timestamp_expression DATE OR TIMESTAMP) → DATE
```

#### Parameters

- `time_unit`: 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', or 'SECOND'.
- `date_timestamp_expression`: The date or timestamp to truncate.

#### Examples

```sql
SELECT DATE_TRUNC('MONTH', '2021-12-24') -- 2021-12-01
SELECT DATE_TRUNC('MINUTE', CAST('2021-12-24 12:28:33' as TIMESTAMP)) -- 2021-12-24 12:28:00
SELECT DATE_TRUNC('HOUR', '2021-12-24 12:28:33') -- 2021-12-24
```

### DAY

Returns the day of the month from a date or timestamp.

#### Syntax

```sql
DAY(date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT "DAY"('2003-02-01 11:43:22') -- 1
```

### DAYOFMONTH

Returns the day of the month from a date or timestamp.

#### Syntax

```sql
DAYOFMONTH(date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT DAYOFMONTH(DATE '2021-02-28') -- 28
SELECT DAYOFMONTH(TIMESTAMP '2021-02-28 11:43:22') -- 28
```

### DAYOFWEEK

Returns the day of the week from a date or timestamp.

#### Syntax

```sql
DAYOFWEEK(date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT DAYOFWEEK(DATE '2021-02-28') -- 1
SELECT DAYOFWEEK(TIMESTAMP '2021-02-27 11:43:22') -- 7
```

### DAYOFYEAR

Returns the day of the year from a date or timestamp.

#### Syntax

```sql
DAYOFYEAR(date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT DAYOFYEAR(DATE '2021-02-28') -- 59
SELECT DAYOFYEAR(TIMESTAMP '2021-03-15 11:43:22') -- 74
```

### DEGREES

Converts radians to degrees.

#### Syntax

```sql
DEGREES(numeric_expression NUMERIC) → FLOAT
```

#### Parameters

- `numeric_expression`: The number of radians. This must be an DOUBLE, INTEGER, or FLOAT.

#### Examples

```sql
SELECT DEGREES(PI()) -- 180.0
SELECT DEGREES(0) -- 0.0
SELECT DEGREES(1) -- 57.29577951308232
```

### DENSE_RANK

Returns the rank of a value in a group of values.

#### Syntax

```sql
DENSE_RANK() OVER ( [PARTITION BY partition_expression] [ORDER BY order_expression]) → bigint
```

#### Parameters

- `partition_expression` (optional): An expression that groups rows into partitions.
- `order_expression`: An expression that specifies the order of the rows within each partition.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", DENSE_RANK() OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
-- Category, Descript, DayOfWeek, EXPR$3
-- ARSON, ARSON, Friday, 1
-- ARSON, ARSON, Monday, 2
```

### E

Returns the base of the natural logarithm (e).

#### Syntax

```sql
E() → float
```

#### Examples

```sql
SELECT E() -- 2.718281828459045
```

### EXP

Returns e raised to the power of a specified number.

#### Syntax

```sql
EXP(numeric_expression NUMERIC) → FLOAT
```

#### Parameters

- `numeric_expression`: The exponent value to raise e to. This must be an DOUBLE, INTEGER, or FLOAT.

#### Examples

```sql
SELECT EXP(1) -- 2.718281828459045
SELECT EXP(10.0) -- 22026.465794806718
```

### EXTRACT

Extracts a part of a date, time, or timestamp.

#### Syntax

```sql
EXTRACT(time_unit KEYWORD, date_time_expression DATE, TIME, TIMESTAMP) → INTEGER
```

#### Parameters

- `time_unit`: The time unit to extract (EPOCH, YEAR, MONTH, DAY, HOUR, MINUTE, SECOND).
- `date_time_expression`: The date, time, or timestamp.

#### Examples

```sql
SELECT EXTRACT(HOUR FROM CAST('05:33:44' AS TIME)) -- 5
SELECT EXTRACT(MONTH FROM CAST('2021-03-22 05:33:44.2' AS TIMESTAMP)) -- 3
SELECT EXTRACT(SECOND FROM CAST('2021-03-22 05:33:44.2' AS TIMESTAMP)) -- 44
SELECT EXTRACT(YEAR FROM CAST('2021-03-22' AS DATE)) -- 2021
SELECT EXTRACT(EPOCH FROM CAST('2021-03-22 05:33:44.2' AS TIMESTAMP)) -- 1616391224
SELECT EXTRACT(EPOCH FROM CAST('2021-03-22' AS DATE)) -- 1616371200
```

### FIRST_VALUE

Returns the first value in an ordered set of values.

#### Syntax

```sql
FIRST_VALUE(expression VARCHAR, order_subclause VARCHAR) → VARCHAR
```

#### Parameters

- `expression`: The expression that determines the return value.
- `order_subclause`: A subclause that specifies the order of the rows within each partition of the result set.

#### Examples

```sql
SELECT city, state, pop, FIRST_VALUE(pop) OVER (PARTITION BY state ORDER BY city) FROM Samples."samples.dremio.com"."zips.json";
```

### FLATTEN

Explodes a compound value into multiple rows.

#### Syntax

```sql
FLATTEN(expression list) → list
```

#### Parameters

- `expression`: The expression that will be unpacked into rows. The expression must be of data type LIST.

#### Examples

```sql
SELECT FLATTEN(CONVERT_FROM ('["Ford", "BMW", "Fiat"]', 'json'))
-- Ford
-- BMW
-- Fiat
```

### FLOOR

Returns the largest integer not greater than the argument.

#### Syntax

```sql
FLOOR(numeric_expression NUMERIC) → INTEGER
```

#### Parameters

- `numeric_expression`: The number (DOUBLE, FLOAT, INTEGER) for which you want to compute the floor.

#### Examples

```sql
SELECT FLOOR(0) -- 0
SELECT FLOOR(45.76) -- 45
SELECT FLOOR(-1.3) -- -2
```

### FROM_HEX

Converts a hexadecimal string to a binary value.

#### Syntax

```sql
FROM_HEX(in string) → binary
```

#### Parameters

- `in`: A hexadecimal string

#### Examples

```sql
select from_hex('3fd98a3c') -- P9mKPA==
```

### GREATEST

Returns the largest value from a list of expressions.

#### Syntax

```sql
GREATEST(expression) → same as input type
```

#### Parameters

- `expression`: The arguments must include at least one expression. All the expressions should be of the same type or compatible types.

#### Examples

```sql
SELECT GREATEST(1, 5, 3, 8) -- 8
```

### HASH

Computes a hash value for an expression.

#### Syntax

```sql
HASH(expression any) → numeric
```

#### Parameters

- `expression`: Can be a general expression of any Dremio-supported data type.

#### Examples

```sql
SELECT HASH(host_id) FROM "Samples"."samples.dremio.com"."Dremio University"."airbnb_listings.csv" LIMIT 5
```

### HASH64

Computes a 64-bit hash value for an expression.

#### Syntax

```sql
HASH64(value ANY [, seed BIGINT]) → BIGINT
```

#### Parameters

- `value`: Input value for hash calculation.
- `seed` (optional): Optional seed for hash calculation.

#### Examples

```sql
SELECT HASH64('abc') -- -5434086359492102041
SELECT HASH64(5.127) -- -1149762993205326574
SELECT HASH64(null) -- 0
SELECT HASH64('abc',123) -- 1489494923063836066
```

### HEX

Returns the hexadecimal representation of a value.

#### Syntax

```sql
HEX(expression any primitive) → varchar
```

#### Parameters

- `expression`: The expression to encode.

#### Examples

```sql
SELECT HEX('Dremio') -- 4472656D696F
SELECT HEX(2023) -- 7E7
```

### HOUR

Extracts the hour from a time, timestamp, or date.

#### Syntax

```sql
EXTRACT(HOUR FROM date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A TIME, TIMESTAMP, or DATE expression.

#### Examples

```sql
SELECT EXTRACT(HOUR FROM TIMESTAMP '2019-08-12 01:10:30.123456') -- 1
SELECT EXTRACT(HOUR FROM TIME '01:10:30.123456') -- 1
SELECT EXTRACT(HOUR FROM CAST('2019-08-12 01:10:30' AS TIMESTAMP)) -- 1
```

### IFNULL

Alias for COALESCE or NVL.

### ILIKE

Compares two strings for equality, ignoring case.

#### Syntax

```sql
ILIKE(expression varchar, pattern varchar) → boolean
ILIKE(expression varchar, pattern varchar, escape_character varchar) → boolean
```

#### Parameters

- `expression`: The expression to compare.
- `pattern`: The pattern that is compared to the expression.
- `escape_character`: Putting escape_character before a wildcard in pattern makes ILIKE treat the wildcard as a regular character when it appears in expression.

#### Examples

```sql
SELECT ILIKE ('pancake', '%Cake') -- True
SELECT ILIKE ('50%_Off', '%50!%%','!') -- True
```

### INITCAP

Returns the string with the first letter of each word in uppercase and all other letters in lowercase.

#### Syntax

```sql
INITCAP(expression varchar) → varchar
```

#### Parameters

- `expression`: Input string.

#### Examples

```sql
SELECT INITCAP('a guide to data lakehouses') -- A Guide To Data Lakehouses
SELECT INITCAP('a guide to data lakeHouses') -- A Guide To Data Lakehouses
```

### IS_MEMBER

Checks if the current user is a member of a specific role.

#### Syntax

```sql
IS_MEMBER(expression varchar) → boolean
```

#### Parameters

- `expression`: String expression identfying a role in Dremio.

#### Examples

```sql
SELECT IS_MEMBER ('public') -- True
SELECT IS_MEMBER ('non-role') -- False
```

### IS_UTF8

Checks if a binary string is a valid UTF-8 string.

#### Syntax

```sql
IS_UTF8(in any) → boolean
```

#### Parameters

- `in`: an expression

#### Examples

```sql
select is_utf8('hello') -- True
```

### IS_VARCHAR

Checks if an expression is a VARCHAR.

#### Syntax

```sql
IS_VARCHAR(expression any) → boolean
```

#### Parameters

- `expression`: Input expression.

#### Examples

```sql
SELECT IS_VARCHAR(column_name) -- True
```

### LAG

Returns the value of a column at a specified offset before the current row.

#### Syntax

```sql
LAG(expression, [offset]) OVER ([PARTITION BY partition_expression] [ORDER BY order_expression]) → same as input type
```

#### Parameters

- `expression` (optional): An expression that is returned.
- `offset` (optional): The number of rows before the current row from which to obtain a value.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", LAG(DayOfWeek, 3) OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
-- Category, Descript, DayOfWeek, EXPR$3
-- ARSON, ARSON, Friday, null
-- ARSON, ARSON, Friday, null
-- ARSON, ARSON OF AN INHABITED DWELLING, Friday, null
-- ARSON, ARSON, Friday, Friday
```

### LAST_DAY

Returns the last day of the month for a given date or timestamp.

#### Syntax

```sql
LAST_DAY(date_timestamp_expression string) → date
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT LAST_DAY('2009-01-12 12:58:59') -- 2009-01-31
```

### LAST_VALUE

Returns the last value in an ordered set of values.

#### Syntax

```sql
LAST_VALUE(expression VARCHAR, order_subclause VARCHAR) → VARCHAR
```

#### Parameters

- `expression`: The expression that determines the return value.
- `order_subclause`: A subclause that specifies the order of the rows within each partition of the result set.

#### Examples

```sql
SELECT city, state, pop, LAST_VALUE(pop) OVER (PARTITION BY state ORDER BY city) FROM Samples."samples.dremio.com"."zips.json"
```

### LCASE

Returns the string in lowercase.

#### Syntax

```sql
LCASE(expression varchar) → varchar
```

#### Parameters

- `expression`: String to convert to lowercase.

#### Examples

```sql
SELECT LCASE('A GUIDE to data Lakehouses') -- a guide to data lakehouses
```

### LEAD

Returns the value of a column at a specified offset after the current row.

#### Syntax

```sql
LEAD(expression, [offset]) OVER ([PARTITION BY partition_expression] [ORDER BY order_expression]) → same as input type
```

#### Parameters

- `expression` (optional): An expression that is returned.
- `offset` (optional): The number of rows after the current row from which to obtain a value.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", LEAD(DayOfWeek, 3) OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
```

### LEFT

Returns the specified number of characters from the left of a string.

#### Syntax

```sql
LEFT(expression varchar, length int64) → varchar
```

#### Parameters

- `expression`: String input parameter
- `length`: Number of characters on the left to return.

#### Examples

```sql
SELECT "LEFT"('Dremio - SQL Engine', -12) -- Dremio
SELECT "LEFT"('Dremio - SQL Engine', 6) -- Dremio
```

### LENGTH

Returns the length of a string.

#### Syntax

```sql
LENGTH([expression varchar]) → int32
```

#### Parameters

- `expression` (optional): String expression to determine the length of.

#### Examples

```sql
SELECT LENGTH('DREMIO') -- 6
```

### LISTAGG

Concatenates the values of a column for each group.

#### Syntax

```sql
LISTAGG ( [ALL | DISTINCT] measure_expr [, 'delimiter'] ) [WITHIN GROUP ( ORDER BY measure_expr [ASC | DESC] )]
```

#### Parameters

- `ALL` (optional): Keeps duplicate values in the return list. This is the default behavior.
- `DISTINCT` (optional): Removes duplicate values from the return list.
- `measure_expr`: A string column or value.
- `delimiter` (optional): Designates a string literal to separate the measure column values. If a delimiter is not specified, will default to NULL.
- `WITHIN GROUP` (optional): Determines the order in which the concatenated values are returned.

#### Examples

```sql
SELECT LISTAGG(city, '; ') FROM "Samples"."samples.dremio.com"."zips.json"
```

### LN

Returns the natural logarithm of a number.

#### Syntax

```sql
LN(numeric_expression double) → float8
```

#### Parameters

- `numeric_expression`: A number greater than 0.

#### Examples

```sql
SELECT LN(0), LN(.1525), LN(1), LN(5.35), LN(5269853105789632584), LN(-1)
-- null, -1.8805906829346708, 0.0, 1.6770965609079151, 43.10853416239341, null
```

### LOCALTIME

Returns the current time in the local time zone.

#### Syntax

```sql
LOCALTIME() → time
```

#### Examples

```sql
SELECT LOCALTIME() -- 05:07:01
```

### LOCALTIMESTAMP

Returns the current timestamp in the local time zone.

#### Syntax

```sql
LOCALTIMESTAMP() → timestamp
```

#### Examples

```sql
SELECT LOCALTIMESTAMP() -- 2021-06-29 05:17:44.703000
```

### LOCATE

Returns the position of the first occurrence of a substring in a string.

#### Syntax

```sql
LOCATE(substring varchar, expression varchar [, start int32]) → int32
```

#### Parameters

- `substring`: Substring to search for in the expression.
- `expression`: The input expression to search.
- `start` (optional): Position to start the search from.

#### Examples

```sql
SELECT LOCATE('no','banana') -- 0
SELECT LOCATE('an','banana') -- 2
SELECT LOCATE('an','banana', 3) -- 4
```

### LOG

Returns the logarithm of a number.

#### Syntax

```sql
LOG([base_expression float], expression float) → double
LOG([base_expression double], expression double) → double
LOG(expression int64) → double
LOG([base_expression int64], expression int64) → double
LOG(expression int32) → double
LOG([base_expression int32], expression int32) → double
LOG(expression float) → double
LOG(expression double) → double
```

#### Parameters

- `base_expression` (optional): The base to use.
- `expression`: The value for which you want to calculate the log.

#### Examples

```sql
SELECT LOG(20.5, 1.5) -- 0.1342410830900514
SELECT LOG(10) -- 2.302585092994046
SELECT LOG(10, 2) -- 0.30102999566398114
SELECT LOG(12.5) -- 2.5257286443082556
```

### LOG10

Returns the base-10 logarithm of a number.

#### Syntax

```sql
LOG10(expression double) → double
LOG10(expression int64) → double
LOG10(expression int32) → double
LOG10(expression float) → double
```

#### Parameters

- `expression`: The value for which you want to calculate the log.

#### Examples

```sql
SELECT LOG10(20.5) -- 1.3117538610557542
SELECT LOG10(100) -- 2.0
```

### LOWER

Returns the string in lowercase.

#### Syntax

```sql
LOWER(expression varchar) → varchar
```

#### Parameters

- `expression`: String to convert to lowercase.

#### Examples

```sql
SELECT LOWER('A GUIDE to data Lakehouses') -- a guide to data lakehouses
```

### LPAD

Pads a string on the left with a specified character.

#### Syntax

```sql
LPAD(base_expression varchar, length int64) → varchar
LPAD(base_expression varchar, length int64 [, pad_expression varchar]) → varchar
```

#### Parameters

- `base_expression`: The expression to pad.
- `length`: The number of characters to return.
- `pad_expression` (optional): Characters to pad the base_expression with.

#### Examples

```sql
SELECT LPAD('parameter', 11) -- parameter
SELECT LPAD('engineering', 6) -- engine
select LPAD('parameter', 11, '-') -- --parameter
```

### LTRIM

Removes leading characters from a string.

#### Syntax

```sql
LTRIM(expression varchar, trim_expression varchar) → varchar
```

#### Parameters

- `expression`: The expression to be trimmed.
- `trim_expression`: Leading characters to trim. If this parameter is not specified, then spaces will be trimmed from the input expression.

#### Examples

```sql
SELECT LTRIM('pancake', 'pan') -- cake
SELECT LTRIM('pancake', 'abnp') -- cake
SELECT LTRIM(' dremio') -- dremio
```

### MASK_FIRST_N

Masks the first N characters of a string.

#### Syntax

```sql
MASK_FIRST_N(expression varchar [, num_chars int] [, uc_mask varchar] [, lc_mask varchar] [, num_mask varchar]) → varchar
```

#### Parameters

- `expression`: The string to mask.
- `num_chars` (optional): The number of characters to mask.
- `uc_mask` (optional): Controls the mask character for upper case letters.
- `lc_mask` (optional): Controls the mask character for lower case letters.
- `num_mask` (optional): Controls the mask character for numbers.

#### Examples

```sql
SELECT MASK_FIRST_N('abcd-ABCD-1234') -- xxxx-ABCD-1234
SELECT MASK_FIRST_N('abcd-ABCD-1234', 2) -- xxcd-ABCD-1234
SELECT MASK_FIRST_N('Aa12-ABCD-1234', 4, 'U', 'u', '#') -- Uu##-ABCD-1234
SELECT MASK_FIRST_N('abcd-ABCD-1234', 7, '', 'u', '') -- uuuu-XXCD-1234
```

### MASK_LAST_N

Masks the last N characters of a string.

#### Syntax

```sql
MASK_LAST_N(expression varchar [, num_chars int] [, uc_mask varchar] [, lc_mask varchar] [, num_mask varchar]) → varchar
```

#### Parameters

- `expression`: The string to mask.
- `num_chars` (optional): The number of characters to mask.
- `uc_mask` (optional): Controls the mask character for upper case letters.
- `lc_mask` (optional): Controls the mask character for lower case letters.
- `num_mask` (optional): Controls the mask character for numbers.

#### Examples

```sql
SELECT MASK_LAST_N('abcd-ABCD-1234') -- abcd-ABCD-nnnn
SELECT MASK_LAST_N('abcd-ABCD-1234', 2) -- abcd-ABCD-12nn
SELECT MASK_LAST_N('abcd-ABCD-Aa12', 4, 'U', 'u', '#') -- abcd-ABCD-Uu##
SELECT MASK_LAST_N('abcd-ABCD-1234', 7, '', 'u', '') -- abcd-ABXX-nnnn
```

### MASK_SHOW_FIRST_N

Masks all but the first N characters of a string.

#### Syntax

```sql
MASK_SHOW_FIRST_N(expression varchar [, num_chars int] [, uc_mask varchar] [, lc_mask varchar] [, num_mask varchar]) → varchar
```

#### Parameters

- `expression`: The string to mask.
- `num_chars` (optional): The number of characters to unmask.
- `uc_mask` (optional): Controls the mask character for upper case letters.
- `lc_mask` (optional): Controls the mask character for lower case letters.
- `num_mask` (optional): Controls the mask character for numbers.

#### Examples

```sql
SELECT MASK_SHOW_FIRST_N('abcd-ABab-1234') -- abcd-XXxx-nnnn
SELECT MASK_SHOW_FIRST_N('abcd-ABab-1234', 2) -- abxx-XXxx-nnnn
SELECT MASK_SHOW_FIRST_N('Aa12-ABab-1234', 4, 'U', 'u', '#') -- Aa12-UUuu-####
SELECT MASK_SHOW_FIRST_N('abcd-ABCD-1234', 2, '', 'u', '') -- abuu-XXXX-nnnn
```

### MASK_SHOW_LAST_N

Masks all but the last N characters of a string.

#### Syntax

```sql
MASK_SHOW_LAST_N(expression varchar [, num_chars int] [, uc_mask varchar] [, lc_mask varchar] [, num_mask varchar]) → varchar
```

#### Parameters

- `expression`: The string to mask.
- `num_chars` (optional): The number of characters to unmask.
- `uc_mask` (optional): Controls the mask character for upper case letters.
- `lc_mask` (optional): Controls the mask character for lower case letters.
- `num_mask` (optional): Controls the mask character for numbers.

#### Examples

```sql
SELECT MASK_SHOW_LAST_N('ab12-ABab-1234') -- xxnn-XXxx-1324
SELECT MASK_SHOW_LAST_N('ab12-ABab-1234', 2) -- xxnn-XXxx-nn34
SELECT MASK_SHOW_LAST_N('Aa12-ABab-1234', 4, 'U', 'u', '#') -- Uu##-UUuu-1234
SELECT MASK_SHOW_LAST_N('abcd-ABCD-1234', 2, '', 'u', '') -- uuuu-XXXX-nn34
```

### MAX

Returns the maximum value of an expression across all rows.

#### Syntax

```sql
MAX(expression NUMERIC) → NUMERIC
```

#### Parameters

- `expression`: The expression from which to take the maximum value, across all rows.

#### Examples

```sql
SELECT MAX("total_amount") FROM "Samples"."samples.dremio.com"."NYC-taxi-trips"; -- 685908.1
```

### MD5

Computes the MD5 hash of a string.

#### Syntax

```sql
MD5(expression varchar) → varchar
```

#### Parameters

- `expression`: The string to hash.

#### Examples

```sql
SELECT MD5('Dremio') -- 288e0e9ab8b8ac8737afefecf16f61fd
```

### MEDIAN

Computes the median value of a numeric column.

#### Syntax

```sql
MEDIAN(num_col numeric) → double precision
```

#### Parameters

- `num_col`: A numeric column whose median value you want to compute.

#### Examples

```sql
SELECT MEDIAN(pop) FROM Samples."samples.dremio.com"."zips.json" -- 2783.0
```

### MIN

Returns the minimum value of an expression across all rows.

#### Syntax

```sql
MIN(expression NUMERIC) → NUMERIC
```

#### Parameters

- `expression`: The expression from which to take the minimum value, across all rows.

#### Examples

```sql
SELECT MIN("total_amount") FROM "Samples"."samples.dremio.com"."NYC-taxi-trips"; -- -1430.0
```

### MOD

Returns the remainder of a division.

#### Syntax

```sql
MOD(numeric_expression int64, numeric_expression int64) → int64
MOD(numeric_expression int64, numeric_expression int32) → int32
MOD(numeric_expression decimal(0,0), numeric_expression decimal(0,0)) → decimal(0,0)
```

#### Parameters

- `numeric_expression`: The dividend.
- `numeric_expression`: The divisor.

#### Examples

```sql
SELECT MOD(50, 7) -- 1
SELECT MOD(35, 5) -- 0
SELECT MOD(47.6, 5.2) -- 0.8
```

### MONTH

Extracts the month from a time, timestamp, or date.

#### Syntax

```sql
EXTRACT(MONTH FROM date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT EXTRACT(MONTH FROM TIMESTAMP '2019-08-12 01:00:00.123456') -- 8
SELECT EXTRACT(MONTH FROM DATE '2019-08-12') -- 8
SELECT EXTRACT(MONTH FROM CAST('2019-08-12 01:00:00' AS TIMESTAMP)) -- 8
```

### MULTIPLY

Use the `*` operator for multiplication.

### NEAR

Not a supported function.

### NEXT_DAY

Returns the date of the first specified day of the week that occurs after the input date.

#### Syntax

```sql
NEXT_DAY(date_timestamp_expression string, day_of_week string) → date
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.
- `day_of_week`: A string expression identifying a day of the week (e.g., 'SU', 'SUN', 'SUNDAY').

#### Examples

```sql
SELECT NEXT_DAY('2015-01-14 12:05:55', 'TU') -- 2015-01-20
```

### NOW

Returns the current timestamp.

#### Syntax

```sql
NOW() → timestamp
```

#### Examples

```sql
SELECT NOW() -- 2021-07-02 04:55:55.267000
```

### NTILE

Divides an ordered data set into a number of buckets indicated by `buckets` and assigns the appropriate bucket number to each row.

#### Syntax

```sql
NTILE(buckets) OVER (PARTITION BY partition_expression ORDER BY order_expression) → int
```

#### Parameters

- `buckets`: A positive integer literal.
- `partition_expression` (optional): An expression that groups rows into partitions.
- `order_expression`: An expression that specifies the order of the rows within each partition.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", NTILE(1) OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
```

### NULLIF

Returns NULL if the two expressions are equal, otherwise returns the first expression.

#### Syntax

```sql
NULLIF(expression1, expression2) → same as input type
```

#### Parameters

- `expression1`: The first expression.
- `expression2`: The second expression.

#### Examples

```sql
SELECT NULLIF(user_id, customer_id)
```

### NVL

Returns the first non-null expression. Alias for COALESCE.

#### Syntax

```sql
NVL(expression1, expression2) → same as input type
```

#### Parameters

- `expression1`: The first expression.
- `expression2`: The second expression.

#### Examples

```sql
SELECT NVL(NULL, 2) -- 2
SELECT NVL(5, 2) -- 5
```

### NVL2

Not supported. Use `CASE` or `NVL`/`COALESCE`.

### OCTET_LENGTH

Returns the length of a string in bytes (octets).

#### Syntax

```sql
OCTET_LENGTH(input varchar) → int32
```

#### Parameters

- `input`: The string for which the length is returned.

#### Examples

```sql
SELECT OCTET_LENGTH('abc') -- 3
```

### OVERLAY

Not supported. Use `SUBSTR` or `SUBSTRING`.

### PERCENT_RANK

Calculates the percent rank of a value in a group of values.

#### Syntax

```sql
PERCENT_RANK() OVER ( [PARTITION BY partition_expression] [ORDER BY order_expression]) → double
```

#### Parameters

- `partition_expression` (optional): An expression that groups rows into partitions.
- `order_expression`: An expression that specifies the order of the rows within each partition.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", PERCENT_RANK() OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
```

### PI

Returns the value of PI.

#### Syntax

```sql
PI() → double
```

#### Examples

```sql
SELECT PI() -- 3.141592653589793
```

### POSITION

Returns the position of a substring within a string.

#### Syntax

```sql
POSITION(substr string IN expression string) → integer
```

#### Parameters

- `substr`: The substring to search for in the expression.
- `expression`: The input expression to search.

#### Examples

```sql
select position('an' in 'banana') -- 2
select position('no' in 'banana') -- 0
```

### POW

Alias for POWER.

### POWER

Returns the value of a number raised to a power.

#### Syntax

```sql
POWER(numeric_expression, power) → double
```

#### Parameters

- `numeric_expression`: The base number.
- `power`: The exponent.

#### Examples

```sql
SELECT POWER(5, 2) -- 25.0
SELECT POWER(10, -2) -- 0.01
```

### QUARTER

Extracts the quarter from a time, timestamp, or date.

#### Syntax

```sql
EXTRACT(QUARTER FROM date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT EXTRACT(QUARTER FROM TIMESTAMP '2019-08-12 01:00:00.123456') -- 3
SELECT EXTRACT(QUARTER FROM DATE '2019-08-12') -- 3
SELECT EXTRACT(QUARTER FROM CAST('2019-08-12 01:00:00' AS TIMESTAMP)) -- 3
```

### RADIANS

Converts degrees to radians.

#### Syntax

```sql
RADIANS(x number) → float
```

#### Parameters

- `x`: The number in degrees.

#### Examples

```sql
select radians(45) -- 0.7853981633974483
```

### RAND

Alias for RANDOM.

### RANK

Returns the rank of a value in a group of values.

#### Syntax

```sql
RANK() OVER ( [PARTITION BY partition_expression] [ORDER BY order_expression]) → bigint
```

#### Parameters

- `partition_expression` (optional): An expression that groups rows into partitions.
- `order_expression`: An expression that specifies the order of the rows within each partition.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", RANK() OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
```

### REGEXP_COL_LIKE

Matches a string against a regular expression contained in a column.

#### Syntax

```sql
REGEXP_COL_LIKE(input string, regex string) → boolean
```

#### Parameters

- `input`: The string to test.
- `regex`: The column containing the Perl-compatible regular expression (PCRE) to use for the test.

#### Examples

```sql
SELECT Category, REGEXP_COL_LIKE('WARRANTS', Category) FROM Samples."samples.dremio.com"."SF_incidents2016.json" LIMIT 3
```

### REGEXP_LIKE

Matches a string against a regular expression.

#### Syntax

```sql
REGEXP_LIKE(input string, regex string) → boolean
```

#### Parameters

- `input`: The string to test.
- `regex`: The Perl-compatible regular expression (PCRE) to use for the test. Must be a literal.

#### Examples

```sql
SELECT REGEXP_LIKE('the data lakehouse', '.*?\\Qlake\\E.*?') -- True
```

### REGEXP_MATCH

Alias for REGEXP_MATCHES or REGEXP_LIKE.

### REGEXP_REPLACE

Replaces substrings matching a regular expression.

#### Syntax

```sql
REGEXP_REPLACE(input string, regex string, replacement_string string) → string
```

#### Parameters

- `input`: The expression to search for a matching string.
- `regex`: The Perl-compatible regular expression (PCRE) to match against.
- `replacement_string`: The string with which to replace the matching string.

#### Examples

```sql
SELECT REGEXP_REPLACE('8AM-4PM', '\\Q-\\E', ' to ') -- 8AM to 4PM
```

### REGEXP_SPLIT

Splits a string using a regular expression.

#### Syntax

```sql
REGEXP_SPLIT(input string, regex string, keyword string, integer integer) → array
```

#### Parameters

- `input`: The string that you want to split by means of the regular expression.
- `regex`: The regular expression to use to split the string.
- `keyword`: The keyword that determines where or how many times to use the regular expression to split the string. Can be FIRST, LAST, INDEX, or ALL.
- `integer`: The value specified for the keyword.

#### Examples

```sql
SELECT REGEXP_SPLIT('REGULAR AIR', 'R', 'FIRST', -1) AS R_LESS_SHIPMENT_TYPE -- ['', 'EGULAR AIR']
```

### REPEAT

Repeats a string a specified number of times.

#### Syntax

```sql
REPEAT(expression varchar, nTimes int32) → varchar
```

#### Parameters

- `expression`: The input string from which the output string is built.
- `nTimes`: The number of times the input expression should be repeated.

#### Examples

```sql
SELECT REPEAT('abc', 3) -- abcabcabc
```

### REPLACE

Replaces all occurrences of a specified string.

#### Syntax

```sql
REPLACE(string_expression varchar, pattern varchar, replacement varchar) → varchar
```

#### Parameters

- `string_expression`: String expression in which to do the replacements.
- `pattern`: The substring you want replaced in the string_expression.
- `replacement`: The string to replace the occurrences of the pattern substring with.

#### Examples

```sql
SELECT REPLACE('THE CATATONIC CAT', 'CAT', 'DOG')
```

### REVERSE

Reverses a string.

#### Syntax

```sql
REVERSE(expression varchar) → varchar
```

#### Parameters

- `expression`: The string to reverse.

#### Examples

```sql
SELECT REVERSE('Hello, world!'); -- !dlrow ,olleH
```

### RIGHT

Returns the specified number of characters from the right of a string.

#### Syntax

```sql
RIGHT(string varchar, length int64) → varchar
```

#### Parameters

- `string`: String input parameter.
- `length`: Number of characters on the right to return.

#### Examples

```sql
SELECT "RIGHT"('Dremio - SQL Engine', 6) -- Engine
```

### ROUND

Rounds a number to a specified number of decimal places.

#### Syntax

```sql
ROUND(numeric_expression decimal(0,0), scale int32) → decimal(0,0)
ROUND(numeric_expression int32, scale int32) → int32
ROUND(numeric_expression int32) → int32
ROUND(numeric_expression double) → double
```

#### Parameters

- `numeric_expression`: Numeric value to round.
- `scale`: The decimal place to round.

#### Examples

```sql
SELECT ROUND(-24.35, -1) -- -24.4
SELECT ROUND(24.35, 1) -- 24.4
SELECT ROUND(24, 0) -- 0
```

### ROW_NUMBER

Returns the row number for the current row in a partition.

#### Syntax

```sql
ROW_NUMBER() OVER ( [PARTITION BY partition_expression] [ORDER BY order_expression]) → bigint
```

#### Parameters

- `partition_expression` (optional): An expression that groups rows into partitions.
- `order_expression` (optional): An expression that specifies the order of the rows within each partition.

#### Examples

```sql
SELECT "Category", "Descript", "DayOfWeek", ROW_NUMBER() OVER ( PARTITION BY "Category" ORDER BY "DayOfWeek") FROM Samples."samples.dremio.com"."SF_incidents2016.json"
```

### RPAD

Right-pads a string with another string to a specified length.

#### Syntax

```sql
RPAD(base_expression varchar, length int64 [, pad_expression varchar]) → varchar
```

#### Parameters

- `base_expression`: The expression to pad.
- `length`: The number of characters to return.
- `pad_expression` (optional): Characters to pad the base_expression with.

#### Examples

```sql
select RPAD('dremio', 9, '!') -- dremio!!!
select RPAD('base_', 9, 'expression') -- base_expr
select RPAD('dremio', 9) -- dremio
```

### RTRIM

Removes trailing characters from a string.

#### Syntax

```sql
RTRIM(expression varchar [, trim_expression varchar]) → varchar
```

#### Parameters

- `expression`: The expression to be trimmed.
- `trim_expression` (optional): Trailing characters to trim. If this parameter is not specified, then spaces will be trimmed from the input expression.

#### Examples

```sql
SELECT RTRIM('pancake', 'cake') -- pan
SELECT RTRIM('pancake pan', 'abnp') -- pancake
SELECT RTRIM('dremio ') -- dremio
```

### SEARCH

Not a direct function. Use LOCATE or POSITION.

### SEC

Alias for SECOND.

### SECOND

Extracts the second from a time, timestamp, or date.

#### Syntax

```sql
EXTRACT(SECOND FROM date_timestamp_expression string) → bigint
```

#### Parameters

- `timestamp_expression`: A TIME, TIMESTAMP, or DATE expression.

#### Examples

```sql
SELECT EXTRACT(SECOND FROM TIMESTAMP '2019-08-12 01:10:30.123456') -- 1
SELECT EXTRACT(SECOND FROM TIME '01:10:30.123456') -- 1
SELECT EXTRACT(SECOND FROM CAST('2019-08-12 01:10:30' AS TIMESTAMP)) -- 1
```

### SHA1

Computes the SHA-1 hash of a string.

#### Syntax

```sql
SHA1(expression varchar) → varchar
```

#### Parameters

- `expression`: The string to hash.

#### Examples

```sql
SELECT SHA1('Dremio') -- dda3f1ef53d1e82a4845ef5b2893b9d9c04bd3b1
```

### SHA256

Computes the SHA-256 hash of a string.

#### Syntax

```sql
SHA256(expression varchar) → varchar
```

#### Parameters

- `expression`: The string to hash.

#### Examples

```sql
SELECT SHA256('Dremio') -- ffae26c65c486a4d9143cbb1a6829166f17dab711910fdfc5787b1a249bd9921
```

### SIGN

Returns the sign of a number.

#### Syntax

```sql
SIGN(numeric_expression double) → int
SIGN(numeric_expression int32) → int32
SIGN(numeric_expression int64) → int64
SIGN(numeric_expression float) → int
```

#### Parameters

- `numeric_expression`: Input expression.

#### Examples

```sql
SELECT SIGN(10.3) -- 1
SELECT SIGN(-5) -- -1
SELECT SIGN(24) -- 1
SELECT SIGN(0.0) -- 0
```

### SIN

Returns the sine of a number (in radians).

#### Syntax

```sql
SIN(numeric_expression int32) → double
SIN(numeric_expression float) → double
SIN(numeric_expression int64) → double
SIN(numeric_expression double) → double
```

#### Parameters

- `numeric_expression`: The number in radians.

#### Examples

```sql
SELECT SIN(360) -- 0.9589157234143065
SELECT SIN(510.89) -- 0.9282211721815067
```

### SINH

Returns the hyperbolic sine of a number.

#### Syntax

```sql
SINH(numeric_expression int32) → double
SINH(numeric_expression float) → double
SINH(numeric_expression double) → double
SINH(numeric_expression int64) → double
```

#### Parameters

- `numeric_expression`: Input expression.

#### Examples

```sql
SELECT SINH(1) -- 1.1752011936438014
SELECT SINH(1.5) -- 2.1292794550948173
```

### SIZE

Returns the number of entries in a map.

#### Syntax

```sql
SIZE(input map) → int
```

#### Parameters

- `input`: A map expression for which to return the number of entries.

#### Examples

```sql
SELECT SIZE(properties)
```

### SPLIT_PART

Splits a string by a delimiter and returns the specified part.

#### Syntax

```sql
SPLIT_PART(expression varchar, delimiter varchar, part_number int32) → varchar
```

#### Parameters

- `expression`: Input expression.
- `delimiter`: String representing the delimiter to split the input expression by.
- `part_number`: Requested part of the split. Must be an integer greater than zero.

#### Examples

```sql
SELECT SPLIT_PART('127.0.0.1', '.', 1) -- 127
```

### SQRT

Returns the square root of a number.

#### Syntax

```sql
SQRT(numeric_expression double) → double
SQRT(numeric_expression int64) → int64
SQRT(numeric_expression int32) → int32
SQRT(numeric_expression float) → float
```

#### Parameters

- `numeric_expression`: Numeric expression to calculate the square root for.

#### Examples

```sql
SELECT SQRT(25.25) -- 5.024937810560445
SELECT SQRT(-25.25) -- NaN
SELECT SQRT(25) -- 5
```

### STDDEV

Returns the sample standard deviation of a numeric column.

#### Syntax

```sql
STDDEV(col_name NUMERIC) → DOUBLE
```

#### Parameters

- `col_name`: The name of the column for which to return the standard deviation. The values in the column must be numbers, such as INT, DOUBLE, or FLOAT.

#### Examples

```sql
SELECT STDDEV(tip_amount) FROM Samples."samples.dremio.com"."NYC-taxi-trips"; -- 2.2596650338662974
```

### STDDEV_POP

Returns the population standard deviation of a numeric column.

#### Syntax

```sql
STDDEV_POP(col_name NUMERIC) → DOUBLE
```

#### Parameters

- `col_name`: The name of the column for which to return the population standard deviation. The values in the column must be numbers, such as INT, DOUBLE, or FLOAT.

#### Examples

```sql
SELECT STDDEV_POP(tip_amount) FROM Samples."samples.dremio.com"."NYC-taxi-trips" -- 2.259665030506379
```

### STDDEV_SAMP

Returns the sample standard deviation of a numeric column.

#### Syntax

```sql
STDDEV_SAMP(col_name NUMERIC) → DOUBLE
```

#### Parameters

- `col_name`: The name of the column for which to return the sample standard deviation. The values in the column must be numbers, such as INT, DOUBLE, or FLOAT.

#### Examples

```sql
SELECT STDDEV_SAMP(tip_amount) FROM Samples."samples.dremio.com"."NYC-taxi-trips" -- 2.259665033866297
```

### STRING_BINARY

Converts a binary value to a string.

#### Syntax

```sql
STRING_BINARY(bytes BYTES) → STRING
```

#### Parameters

- `bytes`: Bytes to convert to a string.

#### Examples

```sql
SELECT STRING_BINARY(BINARY_STRING('Dremio')) -- Dremio
SELECT STRING_BINARY(FROM_HEX('54455354111213')) -- TEST\x11\x12\x13
```

### SUBSTR

Extracts a substring from a string.

#### Syntax

```sql
SUBSTR(string_expression varchar, offset int64) → varchar
SUBSTR(string_expression varchar, offset int64, length int64) → varchar
SUBSTR(string_expression varchar, pattern varchar) → varchar
```

#### Parameters

- `string_expression`: Base expression to extract substring from.
- `offset`: The offset from which the substring starts.
- `length` (optional): The length limit of the substring.
- `pattern`: Regex pattern to match.

#### Examples

```sql
SELECT SUBSTR('dremio user 1 2 3', 12) -- 1 2 3
SELECT SUBSTR('base expression', 6, 4) -- expr
SELECT SUBSTR('dremio user 123', '[0-9]+') -- 123
```

### SUBSTRING

Extracts a substring from a string.

#### Syntax

```sql
SUBSTRING(string_expression varchar, offset int64) → varchar
SUBSTRING(string_expression varchar FROM offset int64) → varchar
SUBSTRING(string_expression varchar, offset int64, length int64) → varchar
```

#### Parameters

- `string_expression`: Base expression to extract substring from.
- `offset`: The offset from which the substring starts.
- `length` (optional): The length limit of the substring.

#### Examples

```sql
SELECT SUBSTRING('dremio user 1 2 3', 12) -- 1 2 3
SELECT SUBSTRING('dremio user 1 2 3' FROM 12) -- 1 2 3
SELECT SUBSTRING('base expression', 6, 4) -- expr
```

### SUM

Returns the sum of values in a column.

#### Syntax

```sql
SUM(col_name NUMERIC) → same as input except for INT, which returns BIGINT
```

#### Parameters

- `col_name`: The name of the column for which to return the sum. The values in the column must be numbers, such as INT, DOUBLE, or FLOAT.

#### Examples

```sql
SELECT SUM(trip_distance_mi) FROM Samples."samples.dremio.com"."NYC-taxi-trips"; -- 9.858134477692287E8
```

### TAN

Returns the tangent of a number (in radians).

#### Syntax

```sql
TAN(numeric_expression double) → double
TAN(numeric_expression int64) → double
TAN(numeric_expression int32) → double
TAN(numeric_expression float) → double
```

#### Parameters

- `numeric_expression`: The number in radians.

#### Examples

```sql
SELECT TAN(180.8) -- -6.259341891872157
SELECT TAN(1200) -- -0.08862461268886584
```

### TANH

Returns the hyperbolic tangent of a number.

#### Syntax

```sql
TANH(numeric_expression double) → double
TANH(numeric_expression int64) → double
TANH(numeric_expression float) → double
TANH(numeric_expression int32) → double
```

#### Parameters

- `numeric_expression`: Input expression to calculate tanh for.

#### Examples

```sql
SELECT TANH(1.5); -- 0.9051482536448664
SELECT TANH(1); -- 0.7615941559557649
```

### TIMESTAMPADD

Adds a specified number of units to a timestamp.

#### Syntax

```sql
TIMESTAMPADD(unit symbol, count integer, givenTime date or timestamp) → date or timestamp
```

#### Parameters

- `unit`: The unit of the interval. Must be one of the following: YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE, SECOND.
- `count`: Number of units to be added (or subtracted) from givenTime. To subtract units, pass a negative number.
- `givenTime`: Value to which to add units (either a database column in DATE or TIMESTAMP format, or literal value explicitly converted to DATE or TIMESTAMP).

#### Examples

```sql
SELECT TIMESTAMPADD(DAY, 1, DATE '2021-04-01') -- 2021-04-02
SELECT TIMESTAMPADD(HOUR, -2, TIMESTAMP '2021-04-01 17:14:32') -- 2021-04-01 15:14:32
```

### TIMESTAMPDIFF

Returns the difference between two timestamps in the specified unit.

#### Syntax

```sql
TIMESTAMPDIFF(unit symbol, giventime1 date or timestamp, givenTime2 date or timestamp) → integer
```

#### Parameters

- `unit`: The unit of the interval. Must be one of the following: YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE, SECOND.
- `giventime1`: The first DATE or TIMESTAMP (subtrahend).
- `givenTime2`: The second DATE or TIMESTAMP (minuend).

#### Examples

```sql
SELECT TIMESTAMPDIFF(MONTH, DATE '2021-02-01', DATE '2021-05-01'); -- 3
SELECT TIMESTAMPDIFF(DAY, TIMESTAMP '2003-02-01 11:43:22', TIMESTAMP '2005-04-09 12:05:55'); -- 798
```

### TO_BINARY

Not a direct function. Use `CONVERT_TO` or `BINARY_STRING`.

### TO_CHAR

Converts an expression to a string using a specified format.

#### Syntax

```sql
TO_CHAR(expression time, format varchar) → varchar
TO_CHAR(expression date, format varchar) → varchar
TO_CHAR(expression int32, format varchar) → varchar
TO_CHAR(expression float, format varchar) → varchar
TO_CHAR(expression int64, format varchar) → varchar
TO_CHAR(expression double, format varchar) → varchar
TO_CHAR(expression timestamp, format varchar) → varchar
```

#### Parameters

- `expression`: Expression to convert to a string.
- `format`: Format to use for the conversion.

#### Examples

```sql
SELECT TO_CHAR(CAST('01:02:03' AS TIME) , 'HH:MI'); -- 01:02
SELECT TO_CHAR(CAST('2021-02-11' AS DATE) , 'yyyy.mm.dd'); -- 2021.02.11
SELECT TO_CHAR(10, '#') -- 10
SELECT TO_CHAR(7.5, '#.#') -- 7.5
```

### TO_DATE

Converts an expression to a date.

#### Syntax

```sql
TO_DATE(in timestamp) → date
TO_DATE(numeric_expression int32) → date
TO_DATE(numeric_expression float) → date
TO_DATE(numeric_expression int64) → date
TO_DATE(string_expression varchar, format varchar, replaceErrorWithNull int32) → date
TO_DATE(string_expression varchar, format varchar) → date
TO_DATE(numeric_expression double) → date
```

#### Parameters

- `in`: The date is extracted from the timestamp.
- `numeric_expression`: A Unix epoch timestamp.
- `string_expression`: The string from which to extract the date.
- `format`: String to specify format of the date.
- `replaceErrorWithNull`: If 0, the function will fail when given malformed input. If 1, the function will return NULL when given the malformed input.

#### Examples

```sql
SELECT TO_DATE(TIMESTAMP '2022-05-17 19:15:00.000') -- 2022-05-17
SELECT TO_DATE(1640131200) -- 2021-12-22
SELECT TO_DATE('05/24/22', 'MM/DD/YY') -- 2022-05-24
```

### TO_HEX

Converts a binary value to a hexadecimal string.

#### Syntax

```sql
TO_HEX(in binary) → string
```

#### Parameters

- `in`: A binary value

#### Examples

```sql
select to_hex(binary_string('hello')) -- 68656C6C6F
```

### TO_NUMBER

Converts a string to a number.

#### Syntax

```sql
TO_NUMBER(expression varchar, format varchar) → double
```

#### Parameters

- `expression`: String to convert to a number.
- `format`: Format for number conversion.

#### Examples

```sql
SELECT TO_NUMBER('12374.0023', '#####.###') -- 12374.002
SELECT TO_NUMBER('12374', '#####') -- 12374.0
```

### TO_TIME

Converts an expression to a time.

#### Syntax

```sql
TO_TIME(numeric_expression int32) → time
TO_TIME(numeric_expression int64) → time
TO_TIME(string_expression varchar, format varchar, replaceErrorWithNull int32) → time
TO_TIME(string_expression varchar, format varchar) → time
TO_TIME(numeric_expression double) → time
TO_TIME(numeric_expression float) → time
```

#### Parameters

- `numeric_expression`: A Unix epoch timestamp.
- `string_expression`: The string from which to extract the time.
- `format`: String to specify format of the time.
- `replaceErrorWithNull`: If 0, the function will fail when given malformed input. If 1, the function will return NULL when given malformed input.

#### Examples

```sql
SELECT TO_TIME(1665131223) -- 08:27:03
SELECT TO_TIME('09:15:00', 'HH:MI:SS') -- 09:15:00
```

### TO_TIMESTAMP

Converts an expression to a timestamp.

#### Syntax

```sql
TO_TIMESTAMP(numeric_expression double) → timestamp
TO_TIMESTAMP(string_expression varchar, format varchar [, replaceErrorWithNull int32]) → timestamp
TO_TIMESTAMP(numeric_expression int64) → timestamp
TO_TIMESTAMP(numeric_expression int32) → timestamp
TO_TIMESTAMP(numeric_expression float) → timestamp
```

#### Parameters

- `numeric_expression`: A Unix epoch timestamp.
- `string_expression`: The string from which to extract the timestamp.
- `format`: String to specify format of the timestamp.
- `replaceErrorWithNull` (optional): If 0, the function will fail when given malformed input. If 1, the function will return NULL when given malformed input.

#### Examples

```sql
SELECT TO_TIMESTAMP(52 * 365.25 * 86400) -- 2022-01-01 00:00:00
SELECT TO_TIMESTAMP(1640131200) -- 2021-12-22 00:00:00
```

### TRANSACTION_TIMESTAMP

Returns the timestamp of the start of the current transaction.

#### Syntax

```sql
TRANSACTION_TIMESTAMP() → timestamp
```

#### Examples

```sql
SELECT TRANSACTION_TIMESTAMP() -- 2021-07-13 06:52:10.694000
```

### TRANSLATE

Replaces a sequence of characters in a string with another set of characters.

#### Syntax

```sql
TRANSLATE(base_expression varchar, source_characters varchar, target_characters varchar) → varchar
```

#### Parameters

- `base_expression`: The string to translate.
- `source_characters`: A string with all the characters in the base expression that need translating.
- `target_characters`: A string containing all the characters to replace the original characters with.

#### Examples

```sql
SELECT TRANSLATE('*a*bX*dYZ*','XYZ*','cef'); -- abcdef
```

### TRIM

Removes leading, trailing, or both spaces or specified characters from a string.

#### Syntax

```sql
TRIM(LEADING or TRAILING or BOTH trim_expression varchar FROM expression varchar) → varchar
```

#### Parameters

- `trim_expression` (optional): The characters to trim.
- `expression`: The expression to be trimmed.

#### Examples

```sql
SELECT TRIM(' pancake ') -- pancake
SELECT TRIM(leading 'pan' from 'pancake') -- cake
SELECT TRIM(trailing 'cake' from 'pancake') -- pan
SELECT TRIM(both 'pan' from 'pancake pan') -- cake
```

### TRUNC

Alias for TRUNCATE (numeric) or DATE_TRUNC (date).

### TRUNCATE

Truncates a number to a specified scale.

#### Syntax

```sql
TRUNCATE(numeric_expression float) → int
TRUNCATE(numeric_expression double) → int
TRUNCATE(numeric_expression int32) → int32
TRUNCATE(numeric_expression int64) → int64
TRUNCATE(numeric_expression decimal(0,0) [, scale_expression int32]) → decimal(0,0)
TRUNCATE(numeric_expression float [, scale_expression int32]) → float
TRUNCATE(numeric_expression double [, scale_expression int32]) → double
```

#### Parameters

- `numeric_expression`: The numeric expression to truncate.
- `scale_expression` (optional): The decimal place to round to.

#### Examples

```sql
SELECT TRUNCATE(987.65) -- 987
SELECT TRUNCATE(89.2283211, 2) -- 89.22
SELECT TRUNCATE(2021, -1) -- 2020
```

### UPPER

Converts a string to uppercase.

#### Syntax

```sql
UPPER(expression varchar) → varchar
```

#### Parameters

- `expression`: String to convert to uppercase.

#### Examples

```sql
SELECT UPPER('a guide to data lakehouses') -- A GUIDE TO DATA LAKEHOUSES
```

### VAR_POP

Returns the population variance of a numeric column.

#### Syntax

```sql
VAR_POP(col_name NUMERIC) → NUMERIC
```

#### Parameters

- `col_name`: The name of the column for which to return the population variance. The values in the column must be numbers, such as INT, DOUBLE, or FLOAT.

#### Examples

```sql
SELECT VAR_POP(pop) FROM Samples."samples.dremio.com"."zips.json"; -- 1.5167869917122573E8
```

### VAR_SAMP

Returns the sample variance of a numeric column.

#### Syntax

```sql
VAR_SAMP(col_name NUMERIC) → NUMERIC
```

#### Parameters

- `col_name`: The name of the column for which to return the sample variance. The values in the column must be numbers, such as INT, DOUBLE, or FLOAT.

#### Examples

```sql
SELECT VAR_SAMP(passenger_count) FROM Samples."samples.dremio.com"."NYC-taxi-trips"; -- 1.868747683518558
```

### VARIANCE

Alias for VAR_SAMP.

### WEEK

Extracts the week from a date or timestamp.

#### Syntax

```sql
EXTRACT(WEEK FROM date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT EXTRACT(WEEK FROM TIMESTAMP '2019-08-12 01:00:00.123456') -- 33
SELECT EXTRACT(WEEK FROM DATE '2019-08-12') -- 33
```

### YEAR

Extracts the year from a date or timestamp.

#### Syntax

```sql
EXTRACT(YEAR FROM date_timestamp_expression string) → bigint
```

#### Parameters

- `date_timestamp_expression`: A DATE or TIMESTAMP expression.

#### Examples

```sql
SELECT EXTRACT(YEAR FROM TIMESTAMP '2019-08-12 01:00:00.123456') -- 2019
SELECT EXTRACT(YEAR FROM DATE '2019-08-12') -- 2019
```

## System Tables

System tables make up Dremio's system-created catalog to store metadata for the objects in your Dremio organization.

### sys.organization.model_usage

Contains metadata for LLM model usage through Dremio.

| Field | Data Type | Description |
| --- | --- | --- |
| organization_id | nvarchar | The UUID of the organization. |
| project_id | nvarchar | The UUID of the project. |
| user_id | nvarchar | The UUID of the user. |
| model_name | nvarchar | The name of the model. |
| operation | nvarchar | The operation performed. Enum: `CHAT`, `SQL` |
| input_tokens | integer | The number of input tokens. |
| output_tokens | integer | The number of output tokens. |
| timestamp | timestamp | The timestamp of the usage. |

### sys.organization.privileges

Contains metadata for privileges at the organization-level.

| Field | Data Type | Description |
| --- | --- | --- |
| grantee_id | nvarchar | The UUID of the user or role that has been granted the privilege. |
| grantee_type | nvarchar | The type of grantee. Enum: `user`, `role` |
| privilege | nvarchar | The privilege that has been granted. |
| object_id | nvarchar | The UUID of the object on which the privilege has been granted. |
| object_type | nvarchar | The type of the object on which the privilege has been granted. |

### sys.organization.projects

Contains metadata for projects in an organization.

| Field | Data Type | Description |
| --- | --- | --- |
| project_id | nvarchar | The UUID to identify the project. |
| project_name | nvarchar | The name of the project. |
| project_state | nvarchar | The state of the project. Enum: `COMMISSIONING`, `ACTIVE`, `FAILED`, `MARK_DELETE` |
| description | nvarchar | The description of the project. |
| created | timestamp | The timestamp for when the project was created. |
| organization_id | nvarchar | The UUID of the organization. |
| identity_type | nvarchar | The type of identity. Enum: `ACCESS_KEY`, `IAM_ROLE` |
| owner_id | nvarchar | The UUID of the owner. |
| owner_type | nvarchar | The type of owner. Enum: `USER`, `ROLE` |

### sys.organization.roles

Contains metadata for roles in an organization.

| Field | Data Type | Description |
| --- | --- | --- |
| role_id | nvarchar | The UUID to identify the role. |
| role_name | nvarchar | The name of the role. |
| role_type | nvarchar | The type of role. Enum: `SYSTEM`, `INTERNAL`, `USER` |
| owner_id | nvarchar | The UUID of the owner (user or role) of the role. |
| owner_type | nvarchar | The type of owner of the role. Enum: `USER`, `ROLE` |
| created | timestamp | The timestamp for when the role was created. |
| created_by | nvarchar | The method of creation. Enum: `LOCAL`, `SCIM` |

### sys.organization.usage

Contains data about an organization's usage.

| Field | Data Type | Description |
| --- | --- | --- |
| organization_id | nvarchar | The UUID of the organization. |
| project_id | nvarchar | The UUID of the project. |
| edition | nvarchar | The edition of Dremio. |
| job_id | nvarchar | The UUID of the job. |
| user_id | nvarchar | The UUID of the user. |
| start_time | timestamp | The start time of the job. |
| end_time | timestamp | The end time of the job. |
| engine_id | nvarchar | The UUID of the engine. |
| engine_name | nvarchar | The name of the engine. |
| engine_size | nvarchar | The size of the engine (e.g., m5d.4xlarge). |
| dcu | double | The number of Dremio Capacity Units (DCUs) consumed. |
| job_type | nvarchar | The type of job. |
| status | nvarchar | The status of the job. |
| considered_reflection_count | integer | The number of reflections considered. |
| matched_reflection_count | integer | The number of reflections matched. |
| chosen_reflection_count | integer | The number of reflections chosen. |

### sys.organization.users

Contains metadata for users in an organization.

| Field | Data Type | Description |
| --- | --- | --- |
| user_id | nvarchar | The UUID to identify the user. |
| user_name | nvarchar | The email of the user is used as the username. |
| first_name | nvarchar | The first name of the user. |
| last_name | nvarchar | The last name of the user. |
| status | nvarchar | The state of the user depending on if they have accepted the invite to the organization and have logged in to the application. Enum: `active`, `invited` |
| user_type | nvarchar | The type of user based on how it was created. Enum: `EXTERNAL`, `LOCAL` |
| created | timestamp | The timestamp for when the user was created. |
| owner_id | nvarchar | The UUID for the owner (user or role) of the user. This UUID corresponds to the `user_id` or `role_id` in the `users` or `roles` table. |
| owner_type | nvarchar | The type of owner of the user. Enum: `user`, `role` |
| created_by | nvarchar | The method of creation. Enum: `LOCAL`, `SCIM` |

### sys.project.engines

Contains metadata for engines in a project.

| Field | Data Type | Description |
| --- | --- | --- |
| engine_id | nvarchar | The UUID to identify the engine. |
| engine_name | nvarchar | The name of the engine. |
| engine_size | nvarchar | The size of the engine. Enum: `XX_SMALL_V1`, `X_SMALL_V1`, `SMALL_V1`, `MEDIUM_V1`, `LARGE_V1`, `X_LARGE_V1`, `XX_LARGE_V1`, `XXX_LARGE_V1` |
| engine_state | nvarchar | The state of the engine. Enum: `DELETING`, `DISABLED`, `DISABLING`, `ENABLED` |
| min_replicas | integer | The minimum number of replicas for the engine. |
| max_replicas | integer | The maximum number of replicas for the engine. |
| current_replicas | integer | The current number of replicas for the engine. |
| instance_family | nvarchar | The instance family of the engine. |
| tag | nvarchar | The tag of the engine. |

### sys.project.jobs

Contains the metadata for the jobs in a project.

| Field | Data Type | Description |
| --- | --- | --- |
| job_id | nvarchar | The UUID to identify the job. |
| job_type | nvarchar | The type of job. Enum: `ACCELERATOR_CREATE`, `ACCELERATOR_DROP`, `ACCELERATOR_EXPLAIN`, `FLIGHT`, `INTERNAL_ICEBERG_METADATA_DROP`, `JDBC`, `UI_EXPORT`, `UI_INTERNAL_PREVIEW`, `UI_INTERNAL_RUN`, `UI_PREVIEW`, `UI_RUN`, `METADATA_REFRESH`, `ODBC`, `PREPARE_INTERNAL`, `REST`, `UNKNOWN` |
| status | nvarchar | The status of the job. Enum: `SETUP`, `QUEUED`, `ENGINE START`, `RUNNING` |
| user_name | nvarchar | The username of the user who submitted the job. |
| submitted_ts | timestamp | The timestamp for when the job was submitted. |
| submitted_epoch | bigint | The epoch timestamp for when the job was submitted. |
| is_accelerated | boolean | Whether the job was accelerated. |
| accelerated_by_substitution | boolean | Whether the job was accelerated by substitution. |
| queried_datasets | array | The datasets that were queried. |
| scanned_datasets | array | The datasets that were scanned. |
| attempt_count | integer | The number of attempts for the job. |
| error_msg | nvarchar | The error message if the job failed. |
| query_type | nvarchar | The type of query. |

### sys.project.pipes

Contains the metadata for autoingest pipes in a project.

| Column Name | Data Type | Description |
| --- | --- | --- |
| pipe_name | nvarchar | The name of the pipe. |
| pipe_id | nvarchar | The unique identifier of the pipe. |
| pipe_state | nvarchar | The current state of the pipe. Enum: `Running`, `Paused`, `Stopped_Missing_Table_or_Branch`, `Stopped_Storage_Location_Altered`, `Stopped_Access_Denied`, `Stopped_Missing_Dremio_Source`, `Unhealthy`, `Stopped_Internal_Error` |
| dedupe_lookback_period | integer | The number of days to look back for deduplication. |
| notification_provider | nvarchar | The notification provider for the pipe. |
| notification_queue_reference | nvarchar | The reference to the notification queue. |
| source_root_path | nvarchar | The root path of the source data. |
| target_table | nvarchar | The target table for the pipe. |
| file_format | nvarchar | The file format of the source data. |
| pipe_owner | nvarchar | The owner of the pipe. |
| created_at | timestamp | The timestamp for when the pipe was created. |
| last_updated_at | timestamp | The timestamp for when the pipe was last updated. |
| cloud_settings | nvarchar | The cloud settings for the pipe. |

### sys.project.privileges

Contains metadata for privileges at the project-level.

| Field | Data Type | Description |
| --- | --- | --- |
| grantee_id | nvarchar | The UUID of the user or role that has been granted the privilege. |
| grantee_type | nvarchar | The type of grantee. Enum: `user`, `role` |
| privilege | nvarchar | The privilege that has been granted. |
| object_id | nvarchar | The UUID of the object on which the privilege has been granted. |
| object_type | nvarchar | The type of the object on which the privilege has been granted. (e.g., VDS for view) |

### sys.project.reflection_dependencies

Contains metadata for Reflection dependencies in the current project.

| Field | Data Type | Description |
| --- | --- | --- |
| reflection_id | nvarchar | The UUID of the Reflection. |
| dependency_id | nvarchar | The UUID of the dependency. |
| dependency_type | nvarchar | The type of dependency. Enum: `DATASET`, `REFLECTION` |
| dependency_path | array | The path of the dependency. |

### sys.project.reflections

Contains metadata for Reflections in a project.

| Field | Data Type | Description |
| --- | --- | --- |
| reflection_id | nvarchar | The UUID to identify the Reflection. |
| reflection_name | nvarchar | The name of the Reflection. |
| type | nvarchar | The type of Reflection. Enum: `AGGREGATION`, `RAW` |
| status | nvarchar | The status of the Reflection. Enum: `CAN_ACCELERATE`, `CAN_ACCELERATE_WITH_FAILURES`, `REFRESHING`, `FAILED`, `EXPIRED`, `DISABLED`, `INVALID`, `CANNOT_ACCELERATE_SCHEDULED`, `CANNOT_ACCELERATE_MANUAL` |
| dataset_id | nvarchar | The UUID of the dataset that the Reflection is defined on. |
| dataset_name | nvarchar | The name of the dataset. |
| dataset_type | nvarchar | The type of dataset. Enum: `PHYSICAL_DATASET_HOME_FILE`, `PHYSICAL_DATASET_SOURCE_FILE`, `PHYSICAL_DATASET_SOURCE_FOLDER`, `VIRTUAL_DATASET` |
| sort_columns | array | The columns that the Reflection is sorted by. |
| partition_columns | array | The columns that the Reflection is partitioned by. |
| distribution_columns | array | The columns that the Reflection is distributed by. |
| dimensions | array | The dimensions of the Reflection. |
| measures | array | The measures of the Reflection. |
| external_reflection | nvarchar | The name of the external reflection. |
| arrow_caching_enabled | boolean | Whether Arrow caching is enabled. |
| partition_distribution_strategy | nvarchar | The partition distribution strategy. |
| measure_fields | array | The measure fields. |
| dimension_fields | array | The dimension fields. |
| display_columns | array | The display columns. |
| num_failures | integer | The number of failures. |
| created | timestamp | The timestamp for when the Reflection was created. |
| modified | timestamp | The timestamp for when the Reflection was last modified. |
| refresh_method | nvarchar | The refresh method. Enum: `Manual`, `Autonomous` |
| refresh_status | nvarchar | The refresh status. Enum: `NONE` |

### sys.project."tables"

Contains metadata for tables in a project.

| Field | Data Type | Description |
| --- | --- | --- |
| table_id | nvarchar | The UUID to identify the table. |
| table_name | nvarchar | The name of the table. |
| schema_id | nvarchar | The UUID for the schema/folder in which the table is contained. |
| path | nvarchar | The string array representation of the path of the table. |
| tag | nvarchar | The UUID that is generated to identify the instance of the table. Dremio changes this tag whenever a change is made to the table. |
| type | nvarchar | The type of table. Enum: `PHYSICAL_DATASET`, `SYSTEM_TABLE`, `NESSIE_TABLE` |
| format | nvarchar | The format of the table. Enum: `DELTA`, `EXCEL`, `ICEBERG`, `JSON`, `PARQUET`, `TEXT`, `UNKNOWN`, `XLS` |
| created | timestamp | The date and time that the table was created. |
| owner_id | nvarchar | The UUID for the owner (user or role) of the table. |
| owner_type | nvarchar | The type of owner of the table. Enum: `USER_OWNER`, `ROLE_OWNER` |
| record_count | bigint | The number of records in the table. |
| column_count | integer | The number of columns in the table. |
| is_approximate_stats | boolean | Whether the statistics are approximate. |

### sys.project.views

Contains metadata for views in a project.

| Field | Data Type | Description |
| --- | --- | --- |
| view_id | nvarchar | The UUID to identify the view. |
| space_id | nvarchar | The UUID to identify the parent space that the view is saved under. |
| view_name | nvarchar | The user- or system-defined name of the view. |
| schema_id | nvarchar | The UUID for the schema/folder in which the view is contained. |
| path | nvarchar | The string array representation of the path of the view. |
| tag | nvarchar | The UUID that is generated to identify the instance of the view. Dremio changes this tag whenever a change is made to the view. |
| type | nvarchar | The type of view. Enum: `VIRTUAL_DATASET`, `NESSIE_VIEW` |
| created | timestamp | The date and time that the view was created. |
| sql_definition | nvarchar | The DDL statement that was used to create the view. |
| sql_context | nvarchar | The context for the SQL definition. |
| owner_id | nvarchar | The UUID for the owner (user or role) of the view. |
| owner_type | nvarchar | The type of owner of the view. Enum: `USER_OWNER`, `ROLE_OWNER` |

### sys.project.copy_errors_history

Contains metadata for copy errors history.

| Column Name | Data Type | Description |
| --- | --- | --- |
| executed_at | timestamp | The timestamp when the copy command was executed. |
| job_id | nvarchar | The UUID of the job that executed the copy command. |
| table_name | nvarchar | The name of the table. |
| user_name | nvarchar | The name of the user who executed the command. |
| file_path | nvarchar | The path of the file that caused the error. |
| line_number | bigint | The line number in the file where the error occurred. |
| error_message | nvarchar | The error message. |

### sys.project.copy_file_history

Contains metadata for copy file history.

| Column Name | Data Type | Description |
| --- | --- | --- |
| executed_at | timestamp | The timestamp when the copy command was executed. |
| job_id | nvarchar | The UUID of the job that executed the copy command. |
| table_name | nvarchar | The name of the table. |
| user_name | nvarchar | The name of the user who executed the command. |
| file_path | nvarchar | The path of the file that was copied. |
| file_state | nvarchar | The state of the file copy. Enum: `LOADED`, `PARTIALLY_LOADED`, `SKIPPED` |
| records_loaded_count | bigint | The number of records loaded. |
| records_rejected_count | bigint | The number of records rejected. |

### sys.project.history.autonomous_reflections

Contains metadata for autonomous reflections history.

| Column Name | Data Type | Description |
| --- | --- | --- |
| reflection_id | nvarchar | The UUID of the Reflection. |
| reflection_name | nvarchar | The name of the Reflection. |
| dataset_id | nvarchar | The UUID of the dataset. |
| dataset_name | nvarchar | The name of the dataset. |
| status | nvarchar | The status of the Reflection. |
| event_type | nvarchar | The type of event. |
| event_timestamp | timestamp | The timestamp of the event. |
| details | nvarchar | The details of the event. |

### sys.project.history.events

Contains metadata for historical events.

| Field | Data Type | Description |
| --- | --- | --- |
| event_id | nvarchar | The UUID of the event. |
| event_type | nvarchar | The type of event. |
| event_timestamp | timestamp | The timestamp of the event. |
| user_id | nvarchar | The UUID of the user who triggered the event. |
| entity_id | nvarchar | The UUID of the entity related to the event. |
| entity_type | nvarchar | The type of entity. |
| details | nvarchar | The details of the event. |

### sys.project.history.jobs

Contains metadata for historical jobs.

| Field | Data Type | Description |
| --- | --- | --- |
| job_id | nvarchar | The UUID to identify the job. |
| job_type | nvarchar | The type of job. |
| status | nvarchar | The status of the job. |
| user_name | nvarchar | The username of the user who submitted the job. |
| submitted_ts | timestamp | The timestamp for when the job was submitted. |
| submitted_epoch | bigint | The epoch timestamp for when the job was submitted. |
| is_accelerated | boolean | Whether the job was accelerated. |
| accelerated_by_substitution | boolean | Whether the job was accelerated by substitution. |
| queried_datasets | array | The datasets that were queried. |
| scanned_datasets | array | The datasets that were scanned. |
| attempt_count | integer | The number of attempts for the job. |
| error_msg | nvarchar | The error message if the job failed. |
| query_type | nvarchar | The type of query. |

### sys.project.materializations

Contains metadata for materializations.

| Field | Data Type | Description |
| --- | --- | --- |
| materialization_id | nvarchar | The UUID of the materialization. |
| reflection_id | nvarchar | The UUID of the Reflection. |
| job_id | nvarchar | The UUID of the job that created the materialization. |
| created | timestamp | The timestamp for when the materialization was created. |
| expires | timestamp | The timestamp for when the materialization expires. |
| state | nvarchar | The state of the materialization. |
| footprint | bigint | The size of the materialization. |
| original_cost | double | The original cost of the query. |
| reflection_type | nvarchar | The type of Reflection. |
| series_id | nvarchar | The series ID. |
| series_ordinal | integer | The series ordinal. |
| join_analysis | nvarchar | The join analysis. |

### sys.project.pipe_summary

Contains metadata for pipe summary.

| Column Name | Data Type | Description |
| --- | --- | --- |
| pipe_name | nvarchar | The name of the pipe. |
| pipe_id | nvarchar | The unique identifier of the pipe. |
| jobs_count | integer | The number of jobs completed for autoingestion related to this pipe. |
| files_loaded_count | integer | The number of files loaded by the pipe. |
| files_skipped_count | integer | The number of files skipped by the pipe. |
| files_partially_loaded_count | integer | The number of files partially loaded by the pipe. |
| pipe_status | nvarchar | The current status of the pipe. |
| error_message | nvarchar | The error message if the pipe is in an error state. |
| last_updated_at | timestamp | The timestamp of the last update to the pipe summary. |
| total_records_count | integer | The total number of records processed by the pipe. |


## Table Functions

Table functions in Dremio return a table as a result and can be used in the `FROM` clause of a query.

### sys.recommend_reflections

Returns a list of recommendations for Reflections that can be created to accelerate queries.

**Syntax:**
```sql
SELECT * FROM TABLE(sys.recommend_reflections())
```

**Columns:**

| Column | Data Type | Description |
| --- | --- | --- |
| query_id | VARCHAR | The job ID of the query that would benefit from the reflection. |
| dataset_id | VARCHAR | The ID of the dataset. |
| dataset_name | VARCHAR | The name of the dataset. |
| reflection_type | VARCHAR | The type of reflection (RAW or AGGREGATION). |
| display_columns | LIST | The list of display columns. |
| dimension_columns | LIST | The list of dimension columns. |
| measure_columns | LIST | The list of measure columns. |
| sort_columns | LIST | The list of sort columns. |
| partition_columns | LIST | The list of partition columns. |
| distribution_columns | LIST | The list of distribution columns. |
| acceleration_count | BIGINT | The number of times the reflection would have accelerated queries. |
| ratio | DOUBLE | The ratio of acceleration. |
| error_message | VARCHAR | Any error message associated with the recommendation. |

### sys.reflection_lineage

Return a list of the Reflections that will also be refreshed if a refresh is triggered for a particular Reflection.

**Syntax:**
```sql
SELECT * FROM TABLE(sys.reflection_lineage('<reflection_id>'))
```

**Parameters:**
*   `<reflection_id>` (String): The ID of the Reflection.

**Columns:**

| Column | Data Type | Description |
| --- | --- | --- |
| reflection_id | nvarchar | The ID of the Reflection. |
| reflection_name | nvarchar | The name of the Reflection. |
| dataset_name | nvarchar | The name of the dataset. |
| dataset_id | nvarchar | The ID of the dataset. |
| reflection_type | nvarchar | The type of Reflection. Enum: `RAW`, `AGG` |
| status | nvarchar | The status of the Reflection. Enum: `INVALID`, `REFRESHING`, `METADATA_REFRESH`, `COMPACTING`, `FAILED`, `DEPRECATED`, `CANNOT_ACCELERATE`, `MANUAL_REFRESH`, `DONE` |
| num_failures | integer | The number of consecutive failures for the Reflection. |
| is_active | boolean | Indicates whether the Reflection is active (true) or inactive (false). |
| can_view | boolean | Indicates whether the current user has permission to view the Reflection. |

### sys.reflection_refresh_settings

Returns the refresh settings for a Reflection, including settings inherited from the datasets that the Reflection depends on.

**Syntax:**
```sql
SELECT * FROM TABLE(sys.reflection_refresh_settings('<reflection_id>'))
```

**Columns:**

| Column | Data Type | Description |
| --- | --- | --- |
| table_type | nvarchar | Defines the type of table. Enum: `DATASET` or `EXTERNAL_QUERY` |
| table_path | nvarchar | Identifies the path to the dataset or external query source that the Reflection depends on. |
| table_version_context | nvarchar | Specifies the versioning context for datasets, stored in JSON format. |
| overrides_source | boolean | Indicates whether settings are inherited from the source (true) or set on the table (false). |
| refresh_method | nvarchar | Shows the method used for the most recent refresh of the Reflection. Enum: `FULL`, `INCREMENTAL`, `AUTO` |
| refresh_policy | nvarchar | Identifies the type of refresh policy. Enum: `PERIOD`, `SCHEDULE`, `LIVE_REFRESH`, `NEVER_REFRESH` |
| refresh_period_seconds | double | Specifies the time in seconds (truncated from milliseconds) between refreshes. |
| refresh_schedule | nvarchar | Provides the cron expression (UTC) that defines the refresh schedule for the Reflection. |
| never_expire | boolean | Indicates whether the Reflection never expires (true) or uses the expiration setting (false). |
| expiration_seconds | double | Defines the expiration time in seconds (truncated from milliseconds), after which the system removes the Reflection. |

## Information Schema

Dremio stores metadata for the objects in your project in the Information Schema, which is a set of system-generated read-only views.

### INFORMATION_SCHEMA.CATALOGS

Returns metadata for the catalogs.

**Fields:**

| Field | Data Type | Description |
| --- | --- | --- |
| CATALOG_NAME | nvarchar | The name of the catalog, which is always DREMIO. |
| CATALOG_DESCRIPTION | nvarchar | The description for the catalog that contains metadata. |
| CATALOG_CONNECT | nvarchar | The connection permissions to the catalog that contains metadata information. This is an inherited field and is always empty. |

### INFORMATION_SCHEMA.COLUMNS

Returns metadata for columns in tables and views.

**Fields:**

| Field | Data Type | Description |
| --- | --- | --- |
| TABLE_CATALOG | nvarchar | The name of the catalog, which is always DREMIO. |
| TABLE_SCHEMA | nvarchar | The path (source, space, folders) to the table or view. |
| TABLE_NAME | nvarchar | The name of the table or view that the column belongs to. |
| COLUMN_NAME | nvarchar | The name of the column in the table or view. |
| ORDINAL_POSITION | integer | This represents the position at which the column appears in the table or view. |
| COLUMN_DEFAULT | nvarchar | The default value of the column. |
| IS_NULLABLE | nvarchar | The value is YES if null values can be stored in the column and the value is NO if null values cannot be stored in the column. |
| DATA_TYPE | nvarchar | The system-defined data type of the column in the table or view. |
| COLUMN_SIZE | integer | The size of the table or view column in bytes. |
| CHARACTER_MAXIMUM_LENGTH | integer | The maximum length in characters for binary data, character data, or text and image data. |
| CHARACTER_OCTET_LENGTH | integer | The maximum length in bytes for binary data, character data, or text and image data. |
| NUMERIC_PRECISION | integer | The precision of approximate numeric data, exact numeric data, integer data, or monetary data. |
| NUMERIC_PRECISION_RADIX | integer | The precision radix of approximate numeric data, exact numeric data, integer data, or monetary data. |
| NUMERIC_SCALE | integer | The scale of approximate numeric data, exact numeric data, integer data, or monetary data. |
| DATETIME_PRECISION | integer | The supported precision for datetime and interval data types. |
| INTERVAL_TYPE | integer | If the data type is interval, then specified fields (year) are returned. |
| INTERVAL_PRECISION | integer | If the data type is interval, then the declared precision is displayed. |

### INFORMATION_SCHEMA.SCHEMATA

Returns metadata for schemas (folders/spaces).

**Fields:**

| Field | Data Type | Description |
| --- | --- | --- |
| CATALOG_NAME | nvarchar | Name of the catalog, which is always DREMIO. |
| SCHEMA_NAME | nvarchar | Path (source, space, folders) that contains datasets. |
| SCHEMA_OWNER | nvarchar | Owner of the schema. This is an inherited field and <owner> is always returned. |
| TYPE | nvarchar | Type of the schema, which is always SIMPLE. |
| IS_MUTABLE | nvarchar | The value in this column is YES if the schema can be modified. NO if it's immutable. |

### INFORMATION_SCHEMA."TABLES"

Returns metadata for tables and views.

**Fields:**

| Field | Data Type | Description |
| --- | --- | --- |
| TABLE_CATALOG | nvarchar | Name of the catalog, which is always DREMIO. |
| TABLE_SCHEMA | nvarchar | The path (source, space, folders) to the table or view. |
| TABLE_NAME | nvarchar | The name of the table or view. |
| TABLE_TYPE | nvarchar | The type of the object. Enum: `SYSTEM_TABLE`, `TABLE`, `VIEW` |

### INFORMATION_SCHEMA.VIEWS

Returns metadata for views.

**Fields:**

| Field | Data Type | Description |
| --- | --- | --- |
| TABLE_CATALOG | nvarchar | The name of the catalog, which is always DREMIO. |
| TABLE_SCHEMA | nvarchar | The path (source, space, folders) to the view. |
| TABLE_NAME | nvarchar | The name of the view. |
| VIEW_DEFINITION | nvarchar | The original SQL query (underlying DDL statement) used to define the view. |
