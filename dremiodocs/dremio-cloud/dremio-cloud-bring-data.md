# Bring Your Data | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/

On this page

Dremio enables you to connect to, load, and prepare data from a wide variety of sources to enable unified data access. Whether your data resides in catalogs, object storage, or databases, Dremio provides the tools you need to bring your data into the lakehouse and prepare it for analytics.

## Load Data into Tables

[Load data](/dremio-cloud/bring-data/load/) from CSV, JSON, or Parquet files into Apache Iceberg tables for faster, more efficient queries. Dremio supports several methods for loading data:

* **Copy Data Into Tables** – Run the `COPY INTO` command to execute a one-time data load from files into existing Iceberg tables.
* **Autoingest Data** – Set up pipe that keep your tables up to date by automatically loading new files into Iceberg tables as they arrive in Amazon S3.
* **Upload Local Files** – Upload local files to create Iceberg tables in an Open Catalog for experimentation.

## Connect to Your Data

Connect Dremio to your existing [data sources](/dremio-cloud/bring-data/connect/) to query data in place without moving it. Dremio supports a wide range of data sources including catalogs, object storage, and databases.

## Prepare Your Data

Transform and enhance your data to make it ready for analytics. Dremio provides tools for [data preparation](/dremio-cloud/bring-data/prepare/) including:

* **Views** – Create virtual tables based on SQL queries to transform, join, and aggregate data without moving or duplicating it.
* **Data Transformations** – Apply column aliasing, type casting, data cleansing, and create derived columns.
* **AI Functions** – Use AI-powered functions to enhance and analyze your data.

Was this page helpful?

* Load Data into Tables
* Connect to Your Data
* Prepare Your Data

<div style="page-break-after: always;"></div>

# Load Data into Tables | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/load

On this page

Dremio supports three main methods for loading data into Apache Iceberg tables. You can copy data from CSV, JSON, or Parquet files directly into an existing table, set up autoingest pipes to continuously ingest new data as it arrives, or upload local files as Iceberg tables in a catalog.

## Copy Data into Tables

Querying large datasets stored in CSV or JSON files can be inefficient. For faster performance and scalability, load your data into Apache Iceberg tables, which use the columnar Parquet format for optimized storage and retrieval. Even queries on Parquet files perform faster when the data is stored in Iceberg tables, enabling you to take full advantage of Dremio’s Iceberg capabilities.

### Prerequisites

* At least one column in the target table must match a column in every data file.
* Files cannot contain duplicate column names.
* CSV data files must have a header line at the start of the file.
* Supported storage locations: Azure Storage or Amazon S3.

### Copy Operation

Use the [`COPY INTO`](/dremio-cloud/sql/commands/copy-into-table/) SQL command to load data from CSV, JSON, and Parquet files into existing Iceberg tables. The operation matches columns in the files to columns in the target table and loads data accordingly.

The copy operation supports Iceberg tables in the Open Catalog, AWS Glue Data Catalog, and catalogs that implement the Iceberg REST Catalog specification.

The copy operation verifies that at least one column in the target table matches a column represented in the data files. It then follows these rules:

* If a match is found, the values in the data files are loaded into the column or columns.
* If additional non-matching columns are present in the data files, the values in these columns are not loaded.
* If additional non-matching columns are present in the target table, the operation inserts NULL values into these columns.
* If no column in the target table matches any column represented in the data files, the operation fails.

The copy operation ignores case when comparing column names.

### Type Coercion

For a list of the type coercions used by the copy operation when copying data from CSV and JSON files, see [Type Coercion When Copying Data from CSV or JSON Files Into Apache Iceberg Tables](/dremio-cloud/sql/data-types/coercions#type-coercion-when-copying-data-from-csv-or-json-files-into-apache-iceberg-tables).

For the type coercions used by the copy operation when copying data from Parquet files, refer to this table:
![Supported and Unsupported Coercions for File-formatted Sources](/assets/images/table-supported-coercions-b78a45f7e4abe4fb3348514afe2845f8.png)

### Column Nullability Constraints

A column's nullability constraint defines whether the column can contain `NULL` values, because you can specify that each column is either:

* `NULL` — Allows `NULL` values, which is useful for optional or unknown data.
* `NOT NULL` — Requires a value for every row; `NULL` values are not allowed.

When running `COPY INTO` with `ON_ERROR` set to 'continue' or 'skip\_file', the command will not fail on nullability conflicts. Instead, it skips the problematic file or record.

However, if `ON_ERROR` is set to 'abort' (or left unspecified), the command will fail if any row violates the table’s `NOT NULL` constraints.

## Autoingest Data Preview

You can use autoingest pipes to automatically ingest data into Apache Iceberg tables.

Autoingest pipes are objects in Dremio that represent event-driven [ingestion pipelines](https://www.dremio.com/wiki/ingestion-pipelines/), which collect and load data into a centralized data repository for further analysis and utilization. Event-driven ingestion, or autoingestion, occurs when a new file is added to a specified cloud storage location, which sets off an event in Dremio to copy the new file into an Iceberg table. Dremio automatically ingests the file with [micro-batch processing](https://www.dremio.com/wiki/micro-batch-processing/), loading files in small, predefined batches at regular intervals.

Autoingest pipes remove the complexity and operational overhead of setting up, running, and monitoring data pipelines by providing:

* **Single-Command Setup**: Dremio provides a streamlined process for setting up and running autoingest pipes. Create an autoingest pipe using the [`CREATE PIPE`](/dremio-cloud/sql/commands/create-pipe/) SQL command to specify the parameters, and run a cloud-specific CLI command to set up the required infrastructure and connect your cloud storage to Dremio for autoingestion.
* **File Deduplication**: [File deduplication](https://www.dremio.com/wiki/deduplication/) eliminates copies of files and enhances storage utilization. Dremio's autoingest pipes provide file deduplication by ensuring that your pipe loads semantics only once and preventing files with the same name from loading in a given time period (the `DEDUPE_LOOKBACK_PERIOD`).
* **Event-Based Execution of `COPY INTO`**: After a new file is added in the source location, an event is sent to Dremio to run a [`COPY INTO`](/dremio-cloud/sql/commands/copy-into-table) statement. Ingested files are processed in [micro-batches](https://www.dremio.com/wiki/micro-batch-processing/) to optimize user resources and ensure that the data is efficiently loaded into Dremio.
* **Execution Monitoring and Error Handling**: For common issues that can occur with data pipelines, such as single rows that do not conform to the target table schema or read permissions being revoked on the source, Dremio takes the appropriate action to alert the user and suggest potential solutions.
* **Efficient Batching for Optimal Engine Utilization**: When implementing an event-based loading system, users often execute a load command for every file immediately after the file is added to cloud storage. This frequent loading increases the likelihood that Iceberg file sizes will be smaller than the optimal size and the engine will be overutilized. Both of these issues result in higher total cost of ownership because they require running [`OPTIMIZE TABLE`](/dremio-cloud/sql/commands/optimize-table) jobs more frequently to compact Iceberg tables, which uses engine resources inefficiently. Dremio’s autoingest pipes efficiently organize requests into micro-batches that minimize the cost of loading data and maintain acceptable [latency](https://www.dremio.com/wiki/latency/) in a data lifecycle.

note

Autoingest pipes can only ingest data from Amazon S3 sources in Dremio.

## Upload Local Files

You can upload an individual local file to Dremio if the file is 500 MB or smaller and in CSV, JSON, or Parquet format. During the upload process, Dremio formats the file into an Iceberg table.

To upload a file:

1. In the Dremio console, click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon.") in the side navigation bar to go to the Datasets page.
2. Click **Add Data** in the bottom left corner of the Datasets page.
3. Upload the file either by:

   a. Dragging the file from your local machine and dropping it in the Add Data dialog.

   b. Clicking **Choose file to upload** and navigating to the file on your local machine.

   If the file is large, it may take a few moments to upload, depending on your connection speed.
4. (Optional) During the upload process, configure the file settings. For example, configure how the file is delimited.
5. Click **Save**.

### Limits

* Uploaded files are copies of your local file. Updates to your local file are not automatically reflected in Dremio.
* Bulk upload of multiple files is not supported.

## Case Sensitivity

Dremio does not support case-sensitive data file names, table names, or column names.

For example, if you have three file names that have the same name, but with different cases (such as, `MARKET`, `Market`, and `market`), Dremio is unable to discern the case differences, resulting in unanticipated data results.

For column names, if two columns have the same name using different cases (such as `Trip_Pickup_DateTime` and `trip_pickup_datetime`) exist in the table, one of the columns may disappear when the header is extracted.

Was this page helpful?

* Copy Data into Tables
  + Prerequisites
  + Copy Operation
  + Type Coercion
  + Column Nullability Constraints
* Autoingest Data Preview
* Upload Local Files
  + Limits
* Case Sensitivity

<div style="page-break-after: always;"></div>

# Prepare Your Data | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/prepare

On this page

You can bring curated data into Dremio by:

* Landing it in Dremio's Open Catalog as Iceberg tables using your tool of choice, such as dbt, Fivetran, Confluent, or others.
* Connecting your existing data sources to Dremio

Once this data is in Dremio, you can further cleanse, combine, transform, and aggregate your data using SQL functions in Dremio and create virtual representations of your data in the form of views.

## Unified Data Access

You can query and combine data across multiple sources and formats in Dremio. Dremio's Query Engine can federate queries across sources in real time without requiring ETL. This allows you to pull together Iceberg tables from Dremio's Open Catalog with existing data in other catalogs, object stores, and databases. For more information on supported data sources, see [Connect to Your Data](/dremio-cloud/bring-data/connect). You can then create views from the SQL that queries across your sources into your Open Catalog.

## Process Unstructured Data

Dremio allows you to process and combine structured, semi-structured, and unstructured data. Examples of unstructured data include PDFs, images, and videos that are stored in object storage.

Dremio natively offers [AI functions](/dremio-cloud/sql/sql-functions/AI/) to enable you to extract and process unstructured data:

* [`AI_GENERATE`](/dremio-cloud/sql/sql-functions/functions/AI_GENERATE/) – Process unstructured data, primarily for complex data extraction requiring multiple fields from source files.
* [`AI_CLASSIFY`](/dremio-cloud/sql/sql-functions/functions/AI_CLASSIFY/) – Categorize documents or analyze sentiment as `VARCHAR` values, using a provided classification list.
* [`AI_COMPLETE`](/dremio-cloud/sql/sql-functions/functions/AI_COMPLETE/) – Generate text or create summaries as `VARCHAR` values.

These functions are processed using Dremio's Query Engine and the AI model provider of your choice. For more information on how to configure your model provider, see [Configure Model Providers](/dremio-cloud/admin/model-providers).

## Create a View

To create a virtual representation of your transformed and aggregated data, you can create a view by following these steps in the Dremio console:

1. Click ![The SQL Runner icon](/images/icons/sql-runner.png "SQL Runner icon") in the side navigation bar to open the SQL Runner.
2. Write a SQL query that transforms your data and click **Run** to validate the query.
3. After the query has finished running, click the arrow next to **Save as View** in the top right of the SQL editor, and select **Save as View...** from the dropdown menu.
4. In the Save View As dialog, name the new view and select from a list of folders where it will be stored.

You can also run the [`CREATE VIEW`](/dremio-cloud/sql/commands/create-view/) from the SQL Runner or your tool of choice to achieve the same results.

## Related Topics

* [Explore and Analyze](/dremio-cloud/explore-analyze/) – Run queries on prepared data.
* [Manage and Govern Data](/dremio-cloud/manage-govern/) – Organize and secure your data in the AI Semantic Layer.
* [Data Privacy](/data-privacy/) – Learn more about Dremio's data privacy practices.

Was this page helpful?

* Unified Data Access
* Process Unstructured Data
* Create a View
* Related Topics

<div style="page-break-after: always;"></div>

# Connect to Your Data | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/

On this page

You can connect to and access data from a variety of sources, including lakehouse catalogs, object storage, and databases. These sources are supported across Dremio projects, providing a unified foundation for data exploration and analytics.

## Catalogs

Every Dremio project includes a native Open Catalog, powered by Apache Polaris. You can connect additional Open Catalogs from other projects and the following external catalogs:

* [AWS Glue Data Catalog](/dremio-cloud/bring-data/connect/catalogs/aws-glue-data-catalog)
* [Snowflake Open Catalog](/dremio-cloud/bring-data/connect/catalogs/snowflake-open-catalog)
* [Unity Catalog](/dremio-cloud/bring-data/connect/catalogs/databricks-unity-catalog)

## Object Storage

Dremio supports [Amazon S3](/dremio-cloud/bring-data/connect/object-storage/amazon-s3) and [Azure Storage](/dremio-cloud/bring-data/connect/object-storage/azure-storage) as object storage services.

## Databases

You can run queries directly on the data in [databases](/dremio-cloud/bring-data/connect/databases/), which are referred to as external sources. In addition, you can run external queries:

* That use the native syntax of the relational database.
* To process SQL statements that are not supported by Dremio or are too complex to convert.

## Network Connectivity

When connecting Dremio to data sources, the connection must use public networking. Ensure that the data source endpoint is publicly accessible and that network egress rules, firewall settings, and IAM permissions are properly configured to allow outbound connectivity from Dremio to the source.

Was this page helpful?

* Catalogs
* Object Storage
* Databases
* Network Connectivity

<div style="page-break-after: always;"></div>

# Dremio | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/dremio

On this page

Connect your project to one or more Dremio Software clusters to create a federated data architecture that combines the best of both environments.

![](/assets/images/dremio-to-dremio-6b84a1b6425cdd8e85ab79448a05db00.png)

This configuration enables:

* **Reduced query latency** – Queries or portions of queries that utilize tables on the Software cluster are pushed down to maximize performance and reduce latency compared to transporting large raw tables.
* **Cross-cluster data federation** – Join data across multiple Dremio Software clusters and expose unified views through Dremio.
* **Enhanced security and data isolation** – Expose only a single Dremio port to the cloud instead of opening multiple source connections from your data center. Administrators of the Software cluster control what data is visible to the managing Dremio environment, allowing isolation of highly sensitive data on the Software cluster while exposing only aggregations or derived datasets to the managing project.
* **Simplified data access** – Access all data sources connected to Software clusters as schemas within Dremio without managing individual source connections.
* **Centralized semantic layer** – Build views and virtual datasets on top of federated clusters for consistent business logic across your organization.

When you connect a Dremio Software cluster as a data source, all sources on the Software cluster can be available from your project. You can create Reflections, build views, and query across the federated environment just as you would with any connected source.

## Example Configuration

When you add a Dremio Software cluster as a source to your Dremio project:

* The Software cluster appears under Sources > Databases in your project.
* Data sources connected to the Software cluster appear as folders/schemas.
* You can promote tables from both directly connected sources and federated sources.
* Create views and Reflections on any promoted tables, regardless of source type.
* Query and join data across all sources—direct and federated.

## Deployment Considerations

If your Dremio project and the source Dremio Software cluster are in different cloud regions or cloud vendors, your deployment design may be influenced by network latency and egress costs.

### Network Latency

Cross-region or cross-cloud queries can experience increased latency. To minimize impact:

* **Use Reflections** – Create Reflections in your Dremio project of frequently queried data from the Software cluster. Queries use the Reflections instead of fetching data across regions.
* **Push down filters and aggregations** – Write queries that leverage Dremio's query pushdown to perform filtering and aggregation on the Software cluster before returning results.
* **Colocate when possible** – If latency is critical, deploy the Software cluster in the same region as your Dremio organization.

### Cloud Egress Costs

Data transfer between cloud regions or cloud vendors can incur significant egress charges. To control costs:

* **Create Reflections for frequently used data** – Reflection data is stored in your Dremio region, eliminating repeated egress charges for frequently accessed datasets.
* **Use aggregated views** – Expose only aggregated or summarized data from the Software cluster rather than raw tables, reducing data transfer volume.
* **Limit full table scans** – Ensure queries include appropriate filters to minimize the amount of data transferred across regions.
* **Monitor query patterns** – Use Dremio's query history to identify expensive cross-region queries and optimize them with Reflections.

### Security

Configure full TLS wire encryption on Software clusters to protect data in transit across regions and cloud boundaries.

## User Impersonation

When you connect your project to a Dremio Software cluster, you provide the username and password of an account on the cluster. By default, queries that run from the project against the Dremio Software cluster run under the username of that account.

Alternatively, you can utilize user impersonation, which allows users running queries from your project to run them under their own usernames on the Dremio Software cluster. Users in your project must have accounts on the Dremio Software cluster, and the usernames must match. User impersonation (also known as *Inbound Impersonation*) must be set up on the Dremio Software cluster. The policy for user impersonation would look like this:

Example policy

```
ALTER SYSTEM SET "exec.impersonation.inbound_policies"='[  
   {  
      "proxy_principals":{  
         "users":[  
            "User_1"  
         ]  
      },  
      "target_principals":{  
         "users":[  
            "User_1"  
         ]  
      }  
   }  
]'
```

## Prerequisites

You must have a username and password for the account on the Dremio Software cluster to use for connections from your project.

## Configure a Dremio Software Cluster as a Source

1. In the bottom-left corner of the Datasets page, click **Add Data**.
2. Under **Databases** in the Add Data Source dialog, select **Dremio**.

### General Options

1. In the **Name** field, specify the name by which you want the data-source cluster to appear in the **Databases** section. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, specify how you want to connect to the data-source cluster:
   * **Direct**: Connect directly to a coordinator node of the cluster.
   * **ZooKeeper**: Connect to an external ZooKeeper instance that is coordinating the nodes of the cluster.
3. In the **Host** and **Port** fields, specify the hostname or IP address and the port number of the coordinator node or ZooKeeper instance.
4. If the data-source cluster is configured to use TLS for connections to it, select the **Use SSL** option.
5. Under **Authentication**, specify the username and password for the project to use when connecting to the data-source cluster.

### Advanced Options

On the Advanced Options page, you can set values for these optional parameters:

* **Maximum Idle Connections** – The total number of connections allowed to be idle at a given time. The default is 8.
* **Connection Idle Time** – The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default is 60 seconds.
* **Query Timeout** – The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **User Impersonation** – Allows users to run queries on the data-source cluster under their own user IDs, not the user ID for the account used to authenticate with the data-source cluster. Inbound impersonation must be configured on the data-source cluster.

### Reflection Refresh Options

On the Reflection Refresh page, set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed.

* **Never refresh** – Select to prevent automatic Reflection refresh. The default is to automatically refresh.
* **Refresh every** – How often to refresh Reflections, specified in hours, days, or weeks. This option is ignored if **Never refresh** is selected.
* **Never expire** – Select to prevent Reflections from expiring. The default is to automatically expire after the time limit below.
* **Expire after** – The time limit after which Reflections expire and are removed from Dremio, specified in hours, days, or weeks. This option is ignored if **Never expire** is selected.

### Metadata Options

On the Metadata page, you can configure settings to refresh metadata and handle datasets.

#### Dataset Handling

* **Remove dataset definitions if underlying data is unavailable** – By default, Dremio removes dataset definitions if underlying data is unavailable. This is useful when files are temporarily deleted and added back in the same location with new sets of files.

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.
  + **Fetch every** (Optional) – You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default is 1 hour.
* **Dataset Details**: The metadata that Dremio needs for query planning, such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information:
  + **Fetch mode** – You can choose to fetch only from queried datasets, which is set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated.
  + **Fetch every** – You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default is 1 hour.
  + **Expire after** – You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default is 3 hours.

### Privileges

On the Privileges page, you can grant privileges to specific users or roles. See [Access Control](/cloud/security/access-control/) for additional information about user privileges.

1. (Optional) For **Privileges**, enter the username or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **Users** table.
2. (Optional) For the users or roles in the **Users** table, toggle the green checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update a Dremio Source

To edit a Dremio source:

1. On the Datasets page, under **Databases**, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions.
3. In the Source Settings dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configure a Dremio Software Cluster as a Source.
4. Click **Save**.

## Remove a Dremio Source

To remove a Dremio source, perform these steps:

1. On the Datasets page, under **Databases**, find the name of the source you want to remove.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

## Predicate Pushdowns

Projects offload these operations to data-source clusters. Data-source clusters either process these operations or offload them to their connected data sources.

`&&`, `||`, `!`, `AND`, `OR`  
`+`, `-`, `/`, `*`, `%`  
`<=`, `<`, `>`, `>=`, `=`, `<>`, `!=`  
`ABS`  
`ADD_MONTHS`  
`AVG`  
`BETWEEN`  
`CASE`  
`CAST`  
`CEIL`  
`CEILING`  
`CHARACTER_LENGTH`  
`CHAR_LENGTH`  
`COALESCE`  
`CONCAT`  
`CONTAINS`  
`COUNT`  
`COUNT_DISTINCT`  
`COUNT_DISTINCT_MULTI`  
`COUNT_FUNCTIONS`  
`COUNT_MULTI`  
`COUNT_STAR`  
`CURRENT_DATE`  
`CURRENT_TIMESTAMP`  
`DATE_ADD`  
`DATE_DIFF`  
`DATE_SUB`  
`DATE_TRUNC`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_QUARTER`  
`DATE_TRUNC_WEEK`  
`DATE_TRUNC_YEAR`  
`DAYOFMONTH`  
`DAYOFWEEK`  
`DAYOFYEAR`  
`EXTRACT`  
`FLATTEN`  
`FLOOR`  
`ILIKE`  
`IN`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LCASE`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LOCATE`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MEDIAN`  
`MIN`  
`MOD`  
`NEXT_DAY`  
`NOT`  
`NVL`  
`PERCENTILE_CONT`  
`PERCENTILE_DISC`  
`PERCENT_RANK`  
`POSITION`  
`REGEXP_LIKE`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SQRT`  
`STDDEV`  
`STDDEV_POP`  
`STDDEV_SAMP`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TO_CHAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UCASE`  
`UPPER`  
`VAR_POP`  
`VAR_SAMP`

## Limitations

You cannot query columns that use complex data types, such as `LIST`, `STRUCT`, and `MAP`. Columns of complex data types do not appear in result sets.

Was this page helpful?

* Example Configuration
* Deployment Considerations
  + Network Latency
  + Cloud Egress Costs
  + Security
* User Impersonation
* Prerequisites
* Configure a Dremio Software Cluster as a Source
  + General Options
  + Advanced Options
  + Reflection Refresh Options
  + Metadata Options
  + Privileges
* Update a Dremio Source
* Remove a Dremio Source
* Predicate Pushdowns
* Limitations

<div style="page-break-after: always;"></div>

# Catalogs | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/catalogs/

On this page

A catalog is a metadata repository that maintains information about datasets and their structure. Catalogs enable consistent discovery, organization, and query execution by storing metadata independently of the underlying data.

A catalog typically includes:

* **Tables and views** – definitions, schemas, columns, and data types
* **Data locations** – where files are stored in object storage
* **Metadata** – partitioning, file formats, and statistics

Dremio can connect to external catalogs to provide a unified metadata layer across platforms. This allows users to query existing datasets in place, without data movement, while preserving a single source of truth for metadata management.

## Catalog Comparison

| Catalog | Provider | Read | Write | Vended Credentials | Best For |
| --- | --- | --- | --- | --- | --- |
| [Dremio's Open Catalog](/dremio-cloud/bring-data/connect/catalogs/open-catalog) | Dremio | ✔ | ✔ | ✔ | Open lakehouses |
| [Iceberg REST Catalog](/dremio-cloud/bring-data/connect/catalogs/iceberg-rest-catalog) | Various | ✔ | ✔ | Varies | Third-party Iceberg catalogs |
| [Snowflake Open Catalog](/dremio-cloud/bring-data/connect/catalogs/snowflake-open-catalog) | Snowflake | ✔ | ✔\* | ✔ | Snowflake-managed Iceberg tables |
| [Unity Catalog](/dremio-cloud/bring-data/connect/catalogs/databricks-unity-catalog) | Databricks | ✔ |  | ✔ | Databricks Delta Lake with UniForm |
| [AWS Glue Data Catalog](/dremio-cloud/bring-data/connect/catalogs/aws-glue-data-catalog) | AWS | ✔ | ✔ | ✔ | AWS-native Iceberg environments |

\*Write supported for external catalogs only

## Dremio's Open Catalog

Every Dremio project includes a built-in [Open Catalog](/dremio-cloud/bring-data/connect/catalogs/open-catalog) for managing your Iceberg tables. You can also connect to catalogs from other projects in your organization for cross-project collaboration.

**Key features:**

* Open and standards-based catalog for Apache Iceberg
* Automatic table maintenance with compaction and vacuuming
* Built-in access controls enforced at the catalog level
* Multi-engine compatibility via Iceberg REST API

**Best for:** Teams working with Apache Iceberg who want automated maintenance and multi-engine access without vendor lock-in.

## AWS Glue Data Catalog

Connect to [AWS Glue's managed metadata catalog](/dremio-cloud/bring-data/connect/catalogs/aws-glue-data-catalog/) for accessing Iceberg tables stored in Amazon S3.

**Key features:**

* Native integration with AWS ecosystem
* Managed metadata storage and schema management
* Support for both read and write operations
* Integration with AWS Lake Formation for fine-grained access control

**Best for:** AWS-native environments that use Glue for metadata management and want to query Iceberg tables with Dremio.

## Iceberg REST Catalog

Connect to any [Iceberg Catalog](/dremio-cloud/bring-data/connect/catalogs/iceberg-rest-catalog/) implementing the REST API specification, including Apache Polaris, AWS Glue Data Catalog, Snowflake Open Catalog, Amazon S3 tables, and Confluent Tableflow.

**Key features:**

* Universal compatibility with REST-compliant Iceberg catalogs
* Support for multiple authentication mechanisms
* Flexible storage credential management
* Connect to on-premises Dremio clusters for hybrid cloud analytics

**Best for:** Connecting to Iceberg catalogs from other vendors or on-premises systems.

## Snowflake Open Catalog

Connect to [Snowflake's managed service](/dremio-cloud/bring-data/connect/catalogs/snowflake-open-catalog/) for Apache Polaris to read and write Iceberg tables across Snowflake and other compatible engines.

**Key features:**

* Read from internal and external Snowflake Open Catalogs
* Write to external Snowflake Open Catalogs
* Credential vending for secure storage access
* Support for AWS, Azure, and GCS storage

**Best for:** Organizations using Snowflake that want to query Iceberg tables with Dremio while leveraging Snowflake's catalog management.

## Unity Catalog

Connect to Databricks [Unity Catalog](/dremio-cloud/bring-data/connect/catalogs/databricks-unity-catalog/) to query Delta Lake tables through the UniForm Iceberg compatibility layer.

**Key features:**

* Read Delta Lake tables via UniForm Iceberg metadata layer
* Integration with Databricks governance and security
* Support for AWS, Azure, and GCS storage
* Credential vending for secure access

**Best for:** Databricks users who want to query Delta Lake tables with Dremio using the UniForm compatibility layer.

Was this page helpful?

* Catalog Comparison
* Dremio's Open Catalog
* AWS Glue Data Catalog
* Iceberg REST Catalog
* Snowflake Open Catalog
* Unity Catalog

<div style="page-break-after: always;"></div>

# Databases | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/

On this page

Databases are external sources that you can connect to and query data from. This includes relational databases, data warehouses, and NoSQL databases, with some sources also supporting external queries for advanced use cases.

note

For the Dremio trial, database sources are not supported.

## Relational Databases

These relational databases store data in tables with predefined schemas and use SQL for queries:

* [IBM Db2](/dremio-cloud/bring-data/connect/databases/ibm-db2)
* [Microsoft SQL Server](/dremio-cloud/bring-data/connect/databases/microsoft-sql-server)
* [MySQL](/dremio-cloud/bring-data/connect/databases/mysql)
* [Oracle](/dremio-cloud/bring-data/connect/databases/oracle)
* [PostgreSQL](/dremio-cloud/bring-data/connect/databases/postgres)
* [SAP HANA](/dremio-cloud/bring-data/connect/databases/sap-hana)

## Data Warehouses

These data warehouses are optimized for large-scale analytical queries rather than transactional workloads:

* [Amazon Redshift](/dremio-cloud/bring-data/connect/databases/amazon-redshift)
* [Google BigQuery](/dremio-cloud/bring-data/connect/databases/google-bigquery)
* [Microsoft Azure Synapse Analytics](/dremio-cloud/bring-data/connect/databases/microsoft-azure-synapse-analytics)
* [Snowflake](/dremio-cloud/bring-data/connect/databases/snowflake)
* [Vertica](/dremio-cloud/bring-data/connect/databases/vertica/)

## NoSQL Databases

These NoSQL databases use flexible schemas and are designed for unstructured or semi-structured data:

* [Apache Druid](/dremio-cloud/bring-data/connect/databases/apache-druid)
* [MongoDB](/dremio-cloud/bring-data/connect/databases/mongodb)

## External Queries

External queries use native syntax for a source and can be used for SQL statements that are not supported directly in Dremio or are too complex to convert. To run external queries, use the [`SELECT`](/dremio-cloud/sql/commands/SELECT) SQL command with the `EXTERNAL_QUERY` parameter.

You can run external queries against the following databases: [Amazon Redshift](/dremio-cloud/bring-data/connect/databases/amazon-redshift), [Microsoft SQL Server](/dremio-cloud/bring-data/connect/databases/microsoft-sql-server), [MySQL](/dremio-cloud/bring-data/connect/databases/mysql), and [PostgreSQL](/dremio-cloud/bring-data/connect/databases/postgres). To run these queries, you need the [EXTERNAL QUERY](/dremio-cloud/security/privileges/) privilege. Keep in mind, however, when you update the metadata for the data source, Dremio clears permissions, formats, and data Reflections for all datasets created from external queries.

When external querying is not enabled, all queries must use standard SQL syntax. Likewise, all user or role read and write access to tables or views within a source are governed by [privileges](/dremio-cloud/security/privileges/).

Was this page helpful?

* Relational Databases
* Data Warehouses
* NoSQL Databases
* External Queries

<div style="page-break-after: always;"></div>

# Data Type Mapping

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/mysql

On this page

[MySQL](https://www.mysql.com/) is a managed database service for deploying cloud-native applications.

## Prerequisites

Ensure that you have the following details before configuring MySQL as a source:

* Hostname or IP address
* Port
* Outbound port (3306 is the default port) open in your AWS or Azure security group

## Configure MySQL as a Source

Perform these steps to configure MySQL as a source:

1. On the Datasets page, you can see a truncated list of **Sources** at the bottom-left of the page. Click **Add Source**.

   Alternatively, select **Databases** in the Data panel. The page displays all database sources. Click the **Add database** button at the top-right corner of that page.
2. In the **Add Data Source** dialog, click **MySQL**.

   The following section describes the source configuration settings in the New MySQL Source dialog.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### General

Under **General** in the sidebar, complete the following steps:

1. For **Name**, enter a name. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. For **Host**, enter the MySQL host name.
3. For **Port**, enter the MySQL port number. The default port is 3306.
4. (Optional) For **Database**, enter the MySQL database name.
5. For **Authentication**, choose one of the following options:

   a. Select **No Authentication** to not provide credentials.

   b. Select **Master Credentials** to provide the username and password of a master database user with permissions to read required objects:

   * For **Username**, enter your MySQL database username.
   * For **Password**, enter your MySQL database password.

### Advanced Options

(Optional) Select **Advanced Options** in the sidebar and change any of the following settings:

| Advanced Option | Description |
| --- | --- |
| **Net write timeout (in seconds)** | Seconds to wait for data from the server before aborting the connection. The default timeout is 60 seconds. |
| **Record fetch size** | Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default record fetch size is 200. |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection idle time (s)** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query timeout (s)** | The amount of time (in seconds) for the query to be executed before it is canceled. |
| **Properties** | Custom key value pairs for the connection relevant to the source. To add a connection property, click **Add property** and add the property name and value. |

### Reflection Refresh

Select **Reflection Refresh** in the sidebar and set time intervals for Reflections to refresh or expire.

![](/assets/images/mysql-reflection-refresh-9a82eaa074c09dfa6a581c5df40a7ce1.png)

### Metadata

(Optional) Select **Metadata** in the sidebar and complete the following steps:

1. Select **Remove dataset definitions if underlying data is unavailable**. By default, Dremio removes dataset definitions if underlying data is unavailable. This can be useful when files are temporarily deleted and added back in the same location with new sets of files.
2. Set the following **Metadata Refresh** parameters:

| Parameter | Description | Field | Setting |
| --- | --- | --- | --- |
| Dataset Discovery | The refresh interval for fetching top-level source object names such as databases and tables. | **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
| Dataset Details | The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information. | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
| **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
| **Expire after** | You can choose to set the expire time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

(Optional) Select **Privileges** in the sidebar and grant privileges to specific users or roles by completing the following steps:

![](/assets/images/mysql-privileges-c9d5c3ecfb5fccc56ca0b88f3fe34a46.png)

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **Users** table.
2. For the users or roles in the **Users** table, toggle the green checkmark for each privilege you want to grant to the MySQL source that is being created.
3. Click **Save**.

## Edit a MySQL Source

To edit a MySQL source:

1. On the Database page, click **Databases**. A list of databases is displayed.
2. Hover over the database and click the Settings ![This is the icon that represents the Database settings.](/images/icons/settings.png "Icon represents the Database settings.") icon that appears next to the source.
3. In the Source Settings dialog, you cannot edit the name. Editing other parameters is optional.
4. Click **Save**.

## Remove a MySQL Source

To remove a MySQL source, perform these steps:

1. On the Datasets page, click **Databases**. A list of sources is displayed.
2. Hover over the source and click the More (...) icon that appears next to the source.
3. From the list of actions, click **Remove Source**. Confirm that you want to remove the source.

   caution

   Removing a source causes all downstream views dependent on objects in this source to break.

   note

   Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Predicate Pushdowns

Dremio offloads these operations to MySQL.

`*`, `+`, `-`, `/`, `%`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
`AND`, `NOT`, `NOT` `LIKE`, `OR`, `||`  
`ABS`  
`ACOS`  
`ADD_MONTHS`  
`ASIN`  
`ATAN`  
`ATAN2`  
`AVG`  
`CAST`  
`CEIL`  
`CEILING`  
`CHAR_LENGTH`  
`CHARACTER_LENGTH`  
`CONCAT`  
`COS`  
`COT`  
`CURRENT_DATE`  
`CURRENT_TIME`  
`CURRENT_TIMESTAMP`  
`DATE_ADD`  
`DATE_SUB`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_DECADE`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_SECOND`  
`DATE_TRUNC_WEEK`  
`DATE_TRUNC_YEAR`  
`DEGREES`  
`E`  
`EXP`  
`EXTRACT_DAY`  
`EXTRACT_DOW`  
`EXTRACT_DOY`  
`EXTRACT_HOUR`  
`EXTRACT_MINUTE`  
`EXTRACT_MONTH`  
`EXTRACT_QUARTER`  
`EXTRACT_SECOND`  
`EXTRACT_WEEK`  
`EXTRACT_YEAR`  
`FLOOR`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LCASE`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LN`  
`LOCATE`  
`LOG`  
`LOG10`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MIN`  
`MOD`  
`PI`  
`POSITION`  
`POW`  
`POWER`  
`RADIANS`  
`RAND`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SIN`  
`SQRT`  
`STDDEV`  
`STDDEV_POP`  
`STDDEV_SAMP`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TAN`  
`TIMESTAMPADD_DAY`  
`TIMESTAMPADD_HOUR`  
`TIMESTAMPADD_MINUTE`  
`TIMESTAMPADD_MONTH`  
`TIMESTAMPADD_QUARTER`  
`TIMESTAMPADD_SECOND`  
`TIMESTAMPADD_YEAR`  
`TIMESTAMPDIFF_DAY`  
`TIMESTAMPDIFF_HOUR`  
`TIMESTAMPDIFF_MINUTE`  
`TIMESTAMPDIFF_MONTH`  
`TIMESTAMPDIFF_QUARTER`  
`TIMESTAMPDIFF_SECOND`  
`TIMESTAMPDIFF_WEEK`  
`TIMESTAMPDIFF_YEAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UCASE`  
`UPPER`  
`VAR_POP`  
`VAR_SAMP`

# Data Type Mapping

Dremio supports MySQL data types, as shown in the following table which provides the mappings from MySQL to Dremio data types. If there are additional MySQL types not listed in the table, then those types are not supported in Dremio.

| MySQL Data Type | Dremio Type |
| --- | --- |
| BIT | BOOLEAN |
| BIGINT | BIGINT |
| BIGINT UNSIGNED | BIGINT |
| BINARY | VARBINARY |
| BLOB | VARBINARY |
| CHAR | VARCHAR |
| DATE | DATE |
| DATETIME | TIMESTAMP |
| DECIMAL UNSIGNED | DECIMAL |
| DOUBLE | DOUBLE |
| DOUBLE PRECISION | DOUBLE |
| ENUM | VARCHAR |
| FLOAT | FLOAT |
| INT | INTEGER |
| INT UNSIGNED | BIGINT |
| INTEGER | INTEGER |
| INTEGER UNSIGNED | BIGINT |
| LONG VARBINARY | VARBINARY |
| LONG VARCHAR | VARCHAR |
| LONGBLOB | VARBINARY |
| LONGTEXT | VARCHAR |
| MEDIUMBLOB | VARBINARY |
| MEDIUMINT | INTEGER |
| MEDIUMINT UNSIGNED | INTEGER |
| MEDIUMTEXT | VARCHAR |
| NUMERIC | NUMERIC |
| REAL | DOUBLE |
| SET | VARCHAR |
| SMALLINT | INTEGER |
| SMALLINT UNSIGNED | INTEGER |
| TEXT | VARCHAR |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| TINYBLOB | VARBINARY |
| TINYINT | INTEGER |
| TINYINT UNSIGNED | INTEGER |
| TINYTEXT | VARCHAR |
| VARBINARY | VARBINARY |
| VARCHAR | VARCHAR |
| YEAR | INTEGER |

Was this page helpful?

* Prerequisites
* Configure MySQL as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Edit a MySQL Source
* Remove a MySQL Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Object Storage | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/object-storage/

On this page

Object storage provides scalable, cost-effective storage for data lakes. Dremio connects directly to your Amazon S3 bucket or Azure Storage to query data in place without moving or copying it.

## Amazon S3

Dremio supports [Amazon S3](/dremio-cloud/bring-data/connect/object-storage/amazon-s3/), which stores data in Amazon S3 buckets on AWS. Use data source credentials or project data credentials to enable Dremio to access Amazon S3 using the IAM role that is associated with your Dremio project.

## Azure Storage

Dremio supports [Azure Storage](/dremio-cloud/bring-data/connect/object-storage/azure-storage/), which stores data in Azure Blob Storage and Azure Data Lake Storage Gen2.

## Table Formatting

Dremio can query data in object storage across multiple formats:

* **Apache Iceberg** – Open table format designed for petabyte-scale analytics
* **Delta Lake** – Open-source storage framework that brings reliability and performance to data lakes
* **Delimited files** (CSV, TSV, etc.) - Text files with configurable delimiters
* **JSON** - Structured and semi-structured JSON data
* **Parquet** - Columnar format optimized for analytics
* **Excel** (XLSX, XLS) - Spreadsheet files

For information about formatting files and folders as tables, see [Table Formatting](/dremio-cloud/bring-data/connect/object-storage/format/).

Was this page helpful?

* Amazon S3
* Azure Storage
* Table Formatting

<div style="page-break-after: always;"></div>

# Data Type Mapping

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/oracle

On this page

[Oracle](https://www.oracle.com/database/technologies/) is an object-relational database management system that is widely used in enterprise applications.

## Prerequisites

Ensure that you have the following details before configuring Oracle as a source:

* Hostname or IP address
* Port
* Service Name
* Outbound port (1521 is the default port) open in your AWS or Azure security group

## User Impersonation

The Oracle database username provided in the source configuration is the default username that is used for running queries. When queries are run against Oracle in Dremio, users use the privileges associated with the Oracle database username and run queries under that username.

You can change this default in Dremio by enabling user impersonation in the Advanced Options, which allows users to run queries under their own usernames and restricts their access. For example, `user_1` can run queries as `user_1` rather than `oracle_svc`. Before enabling user impersonation, some setup is required in Oracle to allow one user to impersonate another user, because the username of the user in Dremio must be the same as their username in Oracle and the user must be able to connect through the Oracle database username.

To set up user impersonation, follow these steps:

1. Ensure the user's username in Oracle matches their username in Dremio. If the usernames do not match, modify one of the usernames or create a new user account with a matching username.
2. Run a ALTER USER command in Oracle to allow the user to connect through the Oracle database username:

Example of altering the user in Oracle

```
ALTER USER testuser1 GRANT CONNECT THROUGH proxyuser;
```

In this example, the user can log in as `testuser1` in Dremio and in Oracle, and they can connect through the `proxyuser`. The `proxyuser` is the Oracle database username provided in the source configuration.

3. Log in as an admin to Dremio.
4. Follow the steps for Configure Oracle as a Source using the Oracle database username and enable **User Impersonation** in the **Advanced Options**.
5. Grant [source privileges](/dremio-cloud/security/privileges/#source-privileges) to the user.

Now that you have enabled user impersonation, a user logging in to Dremio with their username can access the Oracle source and its datasets according to their privileges. The user also runs queries against Oracle under their username.

## Configure Oracle as a Source

Perform these steps to configure Oracle:

1. On the Datasets page, you can see a truncated list of **Sources** at the bottom-left of the page. Click **Add Source**.

   Alternatively, click **Databases**. The page displays all database sources. Click the **Add database** button at the top-right of that page.
2. In the **Add Data Source** dialog, click **Oracle**.

   The following section describes the source configuration tabs.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### General

The **General** tab contains the required fields to create an Oracle source.

![](/assets/images/oracle-general-bd85ad26b9e3d4ef229c657b08e5ac04.png)

Perform these steps in the **General** tab:

1. In the **General** tab, for **Name**, enter a name. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. For **Host**, enter the Oracle host name.
3. For **Port**, enter the Oracle port number. The default port is 1521.
4. For **Service Name**, enter the service name of your Oracle database.
5. (Optional) For **Enable TLS encryption**, enable encrypted connections to Oracle using TLS.

note

You can only enable TLS encryption or Oracle native encryption for a given source.

6. (Optional) For **Oracle Native Encryption**, the default encryption is **Accepted**. The other values are **Required**, **Rejected**, and **Requested**.

   To enable Oracle native encryption, you should also modify the **SQLNET.Ora** file by adding the following lines.

   ```
   SQLNET.ENCRYPTION_SERVER = required. //Set the value to required or request  
   SQLNET.ENCRYPTION_TYPES_SERVER = (AES256) //Set the value to the appropriate encryption and the value can be different.  
   SQLNET.CRYPTO_CHECKSUM_SERVER = required
   ```

   The Oracle native encryption values are described in the following table.

   | Oracle Native Encryption Values | Description |
   | --- | --- |
   | Accepted | The client or server allows both encrypted and non-encrypted connections. This is the default if the parameter is not set. |
   | Rejected | The client or server refuses encrypted traffic. |
   | Requested | The client or server requests encrypted traffic if it is possible, but accepts non-encrypted traffic if encryption is not possible. |
   | Required | The client or server only accepts encrypted traffic. |
7. For **Authentication**, you must choose one of the following authentication options:

   * **Master Authentication**, this is the default option. Provide the username and password of a master database user with permissions to read required objects:
     + For **Username**, enter your Oracle database username.
     + For **Password**, enter your Oracle database password.
   * **Secret Resource Url**:
     + For **Username**, enter your Oracle database username.
     + For **Secret Resource Url**, enter the Secret Resource URL that allows Dremio to fetch the password from [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). The Secret Resource URL is the Amazon Resource Name (ARN) for the secret (for example, `arn:aws:secretsmanager:us-west-2:123456789012:secret:my-rds-secret-VNenFy`).
   * For **Kerebros**, choose this option when the source database has Kerebros configured.

### Advanced Options

Click **Advanced Options** in the sidebar.

![](/assets/images/oracle-adv-options-1aca4006ff6820eef977e67a183784ce.png)

note

All advanced options are optional.

| Advanced Option | Description |
| --- | --- |
| **Use timezone as connection region** | If selected, uses timezone to set connection region. |
| **Include synonyms** | If selected, includes synonyms as datasets. |
| **Map Oracle DATE columns to TIMESTAMP** | If checked, Oracle `DATE` columns are exposed as `TIMESTAMP`. |
| **Record fetch size** | Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default record fetch size is 200. |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Use LDAP Naming Services** | To use LDAP in the authentication of the external sources that can be used rather than locally configured users within Oracle. If checked, enter a domain name in the **Set DN for LDAP Naming Services** text box. |
| **User Impersonation** | Allows users to run queries using their credentials rather than the username provided in the source credentials. Some setup is required in Oracle to allow one user to impersonate another user. See User Impersonation. |
| **Encryption** | Provide the **SSL/TLS server certificate distinguished name**, otherwise, leave it blank to disable the DN match. |
| **Connection Properties** | Custom key value pairs for the connection relevant to the source. To add a connection property, click **Add property** and add the property name and value. |

### Reflection Refresh

The **Reflection Refresh** tab in the sidebar allows you to set time intervals for Reflections to refresh or expire.

![](/assets/images/oracle-reflection-refresh-c3bf964a68466d3d73cfb58ecacfef56.png)

### Metadata

You can configure settings to refresh metadata and handle datasets. Click **Metadata** in the sidebar.

![](/assets/images/oracle-metadata-569297204461a37db9fda2e145263868.png)

You can configure Dataset Handling and Metadata Refresh parameters.

##### Dataset Handling

These are the **Dataset Handling** parameters.

note

All **Dataset Handling** parameters are optional.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

##### Metadata Refresh

These are the **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  note

  All **Dataset Details** parameters are optional.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

You can grant privileges to specific users or roles.

![](/assets/images/oracle-privileges-1168c81c161709c47ab60a0234c3646a.png)

1. (Optional) For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **Users** table.
2. (Optional) For the users or roles in the **Users** table, toggle the green checkmark for each privilege you want to grant to the Oracle source that is being created.

Click **Save** after setting the configuration.

## Edit an Oracle Source

To edit an Oracle source:

1. On the Datasets page, click **Databases**. A list of databases is displayed.
2. Hover over the database and click the Settings ![This is the Settings icon.](/images/icons/settings.png "This is the Settings icon.")
3. In the Source Settings dialog, you cannot edit the name. Editing other parameters is optional.
4. Click **Save**.

## Remove an Oracle Source

To remove an Oracle source, perform these steps:

1. On the Datasets page, click **Databases**. A list of sources is displayed.
2. Hover over the source and click the More (...) icon that appears next to the source.
3. From the list of actions, click **Remove Source**. Confirm that you want to remove the source.

caution

Removing a source causes all downstream views dependent on objects in this source to break.

note

Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Predicate Pushdowns

Dremio offloads these operations to Oracle.

`*`, `+`, `-`, `/`, `%`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
`AND`, `NOT`, `OR`, `||`  
`ABS`  
`ACOS`  
`ADD_MONTHS`  
`ASIN`  
`ATAN`  
`ATAN2`  
`AVG`  
`CAST`  
`CEIL`  
`CEILING`  
`CHAR_LENGTH`  
`CHARACTER_LENGTH`  
`CONCAT`  
`COS`  
`COSH`  
`COT`  
`COVAR_POP`  
`COVAR_SAMP`  
`DATE_ADD`  
`DATE_SUB`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_QUARTER`  
`DATE_TRUNC_WEEK`  
`DATE_TRUNC_YEAR`  
`DEGREES`  
`E`  
`EXP`  
`EXTRACT_CENTURY`  
`EXTRACT_DAY`  
`EXTRACT_DOW`  
`EXTRACT_DOY`  
`EXTRACT_HOUR`  
`EXTRACT_MINUTE`  
`EXTRACT_MONTH`  
`EXTRACT_QUARTER`  
`EXTRACT_SECOND`  
`EXTRACT_WEEK`  
`EXTRACT_YEAR`  
`FLOOR`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LCASE`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LN`  
`LOCATE`  
`LOG`  
`LOG10`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MEDIAN`  
`MIN`  
`MOD`  
`PERCENT_CONT`  
`PERCENT_DISC`  
`PI`  
`POSITION`  
`POW`  
`POWER`  
`RADIANS`  
`REGEXP_LIKE`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SIN`  
`SINH`  
`SQRT`  
`STDDEV`  
`STDDEV_POP`  
`STDDEV_SAMP`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TAN`  
`TANH`  
`TO_CHAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UCASE`  
`UPPER`  
`VAR_POP`  
`VAR_SAMP`

# Data Type Mapping

Dremio supports Oracle data types, as shown in the following table which provides the mappings from Oracle to Dremio data types. If there are additional Oracle types not listed in the table, then those types are not supported in Dremio.

| Oracle Data Type | Dremio Type |
| --- | --- |
| BINARY\_DOUBLE | DOUBLE |
| BINARY\_FLOAT | FLOAT |
| BLOB | VARBINARY |
| CHAR | VARCHAR |
| DATE | DATE |
| FLOAT | DOUBLE |
| INTERVALDS | INTERVAL (day to seconds) |
| INTERVALYM | INTERVAL (years to months) |
| LONG RAW | VARBINARY |
| LONG | VARCHAR |
| NCHAR | VARCHAR |
| NUMBER | DECIMAL |
| NVARCHAR2 | VARCHAR |
| RAW | VARBINARY |
| TIMESTAMP | TIMESTAMP |
| VARCHAR2 | VARCHAR |

Was this page helpful?

* Prerequisites
* User Impersonation
* Configure Oracle as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Edit an Oracle Source
* Remove an Oracle Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# IBM Db2 | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/ibm-db2

On this page

You can add Db2 databases as sources to Dremio.

## Limitations

Only IBM Db2 for Linux, UNIX, and Windows is supported.

## Configure IBM Db2 as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **IBM Db2**.

### General Options

1. In the **Name** field, specify the name by which you want the Db2 source to appear in the **Databases** section. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, follow these steps:

   1. In the **Host** field, specify the hostname or IP address of the database to connect to.
   2. In the **Port** field, specify the port to use when connecting. The default is 50000.
   3. In the **Database** field, specify the name of the database.
3. Under **Authentication**, follow these steps:

   * For **Username**, enter your database username.
   * For **Password**, enter your database password.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### Advanced Options

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Record fetch size** | Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. By default, this is set to **200**. |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default number of maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |
| **Enable external authorization plugin** | When enabled, authorizes an external plugin. |
| **Connection Properties** | Connection properties and values for the data source. |

### Reflection Refresh Options

On the Reflection Refresh page, set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed.

| Option | Description |
| --- | --- |
| **Never refresh** | Select to prevent automatic Reflection refresh, default is to automatically refresh. |
| **Refresh every** | How often to refresh Reflections, specified in hours, days or weeks. This option is ignored if **Never refresh** is selected. |
| **Never expire** | Select to prevent Reflections from expiring, default is to automatically expire after the time limit below. |
| **Expire after** | The time limit after which Reflections expire and are removed from Dremio, specified in hours, days or weeks. This option is ignored if **Never expire** is selected. |

### Metadata Options

On the Metadata page, you can configure settings to refresh metadata and handle datasets.

#### Dataset Handling

These are the optional **Dataset Handling** parameters.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Privileges](/dremio-cloud/security/privileges/) for additional information about privileges.

note

All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update an IBM Db2 Source

To update an IBM Db2 source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configure IBM Db2 as a Source.
4. Click **Save**.

## Delete an IBM Db2 Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an IBM Db2 source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

   caution

   Deleting a source causes all downstream views that depend on objects in the source to break.

   note

   Sources containing a large number of files or tables may take longer to be deleted. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being deleted. Once complete, the source disappears.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

`||`, `AND`, `OR`  
`=`, `+`, `-`, `/`, `*`  
`<=`, `<`, `>`, `>=`, `=`, `<>`, `!=`  
ABS  
ADD\_MONTHS  
AVG  
BETWEEN  
CASE  
CAST  
CEIL  
CEILING  
CHAR\_LENGTH  
CHARACTER\_LENGTH  
COALESCE  
CONCAT  
DATE\_ADD  
DATE\_DIFF  
DATE\_TRUNC  
DATE\_TRUNC\_CENTURY  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_DECADE  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MICROSECOND  
DATE\_TRUNC\_MILLENIUM  
DATE\_TRUNC\_MILLISECOND  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_QUARTER  
DATE\_TRUNC\_SECOND  
DATE\_TRUNC\_WEEK  
DATE\_TRUNC\_YEAR  
DAYOFMONTH  
DAYOFWEEK  
DAYOFYEAR  
EXTRACT  
FLOOR  
ILIKE  
IN  
IS DISTINCT FROM  
IS NOT DISTINCT FROM  
IS NOT NULL  
IS NULL  
LAST\_DAY  
LEFT  
LENGTH  
LIKE  
LOCATE  
LOWER  
LPAD  
LTRIM  
MAX  
MIN  
MOD  
NOT  
OR  
PERCENT\_RANK  
POSITION  
REPLACE  
RIGHT  
ROUND  
RPAD  
RTRIM  
SIGN  
SQRT  
STDDEV  
STDDEV\_POP  
STDDEV\_SAMP  
SUBSTR  
SUBSTRING  
SUM  
TO\_CHAR  
TO\_DATE  
TRIM  
TRUNC  
TRUNCATE  
UPPER

## Data Type Mapping

The following table shows the mappings from Db2 to Dremio data types.

note

If a type is not present in the table, it is not currently supported.

| Db2 Database Type | Dremio Type |
| --- | --- |
| BIGINT | BIGINT |
| BLOB | VARCHAR |
| BOOLEAN | BOOLEAN |
| CHAR | VARCHAR |
| CHAR () FOR BIT DATA | VARCHAR |
| CLOB | VARCHAR |
| DATE | DATE |
| DBCLOB | VARCHAR |
| DECFLOAT | DECIMAL |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| GRAPHIC | VARCHAR |
| INTEGER | INTEGER |
| LONG VARCHAR | VARCHAR |
| LONG VARCHAR FOR BIT DATA | VARCHAR |
| LONG VARGRAPHIC | VARCHAR |
| REAL | DOUBLE |
| SMALLINT | INTEGER |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| VARCHAR () FOR BIT DATA | VARCHAR |
| VARGRAPHIC | VARCHAR |

Was this page helpful?

* Limitations
* Configure IBM Db2 as a Source
  + General Options
  + Advanced Options
  + Reflection Refresh Options
  + Metadata Options
  + Privileges
* Update an IBM Db2 Source
* Delete an IBM Db2 Source
* Predicate Pushdowns
* Data Type Mapping

<div style="page-break-after: always;"></div>

# Data Type Mapping

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/mongodb

On this page

## Supported Versions

Dremio supports MongoDB 3.6 through 8.0.

## Prerequisites

Ensure that that you have the outbound port (27017 is the default port) open in your AWS or Azure security group.

## Configure MongoDB as a Source

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

| Name | Description |
| --- | --- |
| Hosts | A list of Mongo hosts. If MongoDB is sharded, enter the mongos hosts. Otherwise, enter the mongod host. |
| Port | A list of Mongo port numbers. Defaults to 27017. |

* **Connection Scheme** -- Select how to connect to the source.
* **Encrypt connection** -- Forces an encrypted connection over SSL.
* **Read from secondaries only** -- Disables reading from primaries. Might degrade performance.

#### Authentication

* No authentication method
* Master Authentication method (default)
  + Username -- MongoDB user name
  + Password -- MongoDB password
* Authentication database -- Database to authenticate against.

### Advanced Options

![](/assets/images/mongodb-adv-options-79dc1d63a1a229984f1da353ea129c52.png) !

* **Subpartition Size** -- Number of records to be read by query fragments. This option can be used to increase query parallelism.
* **Sample Size** -- Number of records to be read when sampling to determine the schema for a collection. If zero the sample size is unlimited.
* **Sample Method** -- The method (First or Last) by which records should be read when sampling a collection to determine the schema.
* **Auth Timeout (millis)** -- Authentication timeout in milliseconds.
* **Field names are case insensitive** -- When enabled, Dremio reads all known variations of a field name when determining the schema, ignoring any value set for Sample Size. All field name variations are then used when pushing an operation down to Mongo.
* **Connection Properties** -- A list of additional MongoDB connection parameters.

### Reflection Refresh

![](/assets/images/hdfs-refresh-policy-9ae71114907887b859a9d01425390739.png) !

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

!

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).  
  If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

#### Metadata Refresh

* **Dataset Discovery** -- Refresh interval for top-level source object names such as names of DBs and tables.
  + Fetch every -- Specify fetch time based on minutes, hours, days, or weeks. Default: 1 hour
* **Dataset Details** -- The metadata that Dremio needs for query planning such as information needed for
  fields, types, shards, statistics, and locality.
  + Fetch mode -- Specify either Only Queried Datasets, All Datasets, or As Needed. Default: Only Queried Datasets
    - Only Queried Datasets -- Dremio updates details for previously queried objects in a source.  
      This mode increases query performance because less work is needed at query time for these datasets.
    - All Datasets -- Dremio updates details for all datasets in a source.
      This mode increases query performance because less work is needed at query time.
    - As Needed -- Dremio updates details for a dataset at query time.
      This mode minimized metadata queries on a source when not used,
      but might lead to longer planning times.
  + Fetch every -- Specify fetch time based on minutes, hours, days, or weeks. Default: 1 hour
  + Expire after -- Specify expiration time based on minutes, hours, days, or weeks. Default: 3 hours

### Share

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ0AAACkCAYAAACNdnuaAAABfGlDQ1BJQ0MgUHJvZmlsZQAAKJFjYGAqSSwoyGFhYGDIzSspCnJ3UoiIjFJgv8PAzcDDIMRgxSCemFxc4BgQ4MOAE3y7xsAIoi/rgsxK8/x506a1fP4WNq+ZclYlOrj1gQF3SmpxMgMDIweQnZxSnJwLZOcA2TrJBUUlQPYMIFu3vKQAxD4BZIsUAR0IZN8BsdMh7A8gdhKYzcQCVhMS5AxkSwDZAkkQtgaInQ5hW4DYyRmJKUC2B8guiBvAgNPDRcHcwFLXkYC7SQa5OaUwO0ChxZOaFxoMcgcQyzB4MLgwKDCYMxgwWDLoMjiWpFaUgBQ65xdUFmWmZ5QoOAJDNlXBOT+3oLQktUhHwTMvWU9HwcjA0ACkDhRnEKM/B4FNZxQ7jxDLX8jAYKnMwMDcgxBLmsbAsH0PA4PEKYSYyjwGBn5rBoZt5woSixLhDmf8xkKIX5xmbARh8zgxMLDe+///sxoDA/skBoa/E////73o//+/i4H2A+PsQA4AJHdp4IxrEg8AAAGdaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjQuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjI2OTwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4xNjQ8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KLcvSuAAAHaZJREFUeAHtXQd4VEW0PgGSEBJ6771IR5oiHQELKqIoNlQUpahPVBBQBKSr+Ck8sD0E+yciKEVAQEQpAgKCIkU60kuAAAEC7Jt/YNa7m91sIHeXm93/fN/u3ntn7pR/Mv8958zNnKikFJdLlCRkwzeFCBABIpA2AlnSTmYqESACRMATAZKGJx48IwJEIAACJI0AADGZCBABTwRIGp548IwIEIEACJA0AgDEZCJABDwRIGl44sEzIkAEAiBA0ggAEJOJABHwRICk4YkHz4gAEQiAAEkjAEBMJgJEwBMBkoYnHjwjAkQgAAIkjQAAMZkIEAFPBEgannjwjAgQgQAIkDQCAMRkIkAEPBEgaXjiwTMiQAQCIEDSCAAQk4kAEfBEgKThiQfPiAARCIAASSMAQEwmAkTAEwGShicePCMCRCAAAiSNAAAxmQgQAU8ESBqeePCMCBCBAAiQNAIAxGQiQAQ8EQgKaZw+fVqOHj0qJ0+e9KxNnZ0/f16GDBki27ZtS5Vm54ULFy7IiRMn7CySZREBIqAQsJU0Vq5cKe3atZMbbrhBmjdvLo0aNZKOHTvK+vXr3WCfPXtWZs+eLYmJie5rwTj44YcfpFmzZkGvJxhtZ5lEwMkI2EYav/zyizzxxBOSP39++eijj2TmzJn69+LFi/LAAw/ImjVrNA5Zs2bVv1FRUUHFpWjRopq4YmJigloPCycCkYZAlB3Bklwq3tJjjz0mOXPmlDFjxkiWLP9xEUijR48esmfPHvn+++/l3Llz0rJlSxk3bpzUqVMn0vBmf4lApkfgv9mdga7A5Ni5c6eULl3agzBQJAgEhLJ//36Br8MIiGbGjBnahKlZs6Y8+uijsm7dOpOsf48dOyZvv/221K9fX0yeWbNmCe41snjxYhk+fLgsWrRIm0bIh3J27dol3bp1kzNnzuisyDdixAh9/cUXX9TlgbTGjx8v8H9Y5dChQ/Laa6/pPChv5MiRsmLFCk1+p06dsmblMRGIPASgaeCTEVHahKt3796uhg0bujZt2uSzKOUA1deTk5NdStNw1ahRw1WvXj3X9OnTXfPmzXMp/4M+P3jwoM6nfB7ua1OnTnUp88Y1bNgwfd/kyZPddSANZeEzYMAA15QpU1xqYru2bNmiy1MOWZ3Xmu+VV15xLVmyxDV69Gh939ixY93lHT9+3F2vaVuHDh10PrTXlOe+gQdEIMIQsCWCK/wTvXr10k/je++9V9q2bSvt27eXatWqSZ48eTQTG1+GoeWEhASBs9Kk165dW5st//77rxQsWFDmzp0ragLLnDlzpHDhwvo25IHm8umnn8o999zjodVAI7n55ptN8e5fb9+JIhbtnEUGOGrh81CkpbUIlK2IQqBNfPfdd1K8eHFdTqtWreTVV1+VH3/8UbzLc1fEAyIQIQjYYp4AKzgeMdGhyu/du1e6d+8uTZs2lS5dunisniAvzAGlNbgJA9fy5csnZcuWlQ0bNuBUbrvtNl2eIQx9UX1VqlTJgyxwHfe2aNHCZPH7C4K6++67PdKV9iAHDhzQppN6YMjy5cvlrrvuchMGMoMo0A8KESACIrZoGgbI2NhYPdkx4bGkiiVY+BuwejJq1Ci59dZbdVY4Q42GYe7FxARpQLuAwKmKdzomTJggyuTQjlSTFxPdCCZ67ty5A2oAyJc3b95UhAOtBiSWkpKif7dv304HrQGXv0TABwK2kQZU+hw5crgnLyZomzZtpHXr1lq1Hzx4sDRp0kSyZbtUJSaxt2DympWXHTt2yJ133ikgov79+0vFihUlLi5OvvzyS7c24n1/Rs5BWoY8QCAUIkAEfCNgi3minJ/SuHFjSUpKSlULJuODDz6oJyQ0h/QICGXSpElStWpVWbZsmTYpqlevLuXLl5e6detqn0N6yrnSPPBvwPzBapC3GLLzvs5zIhBpCNhCGjAP8JRWqxo+8Vu1apXP62ldPHLkiJQsWVKsDlSQDhyV8fHxad161WkguFq1amltBsu9VoGzlEIEiIBNPo0iRYrISy+9JG+99ZY2He6//37BNfzvCYhELXfq1Qn4Mcx7E/7Ax8tgmLxwbA4aNEi/+wGzBr4OmDh4hwKrGvCLZM+e3V8x7uu+zCB3ouXA5IMTFC+ode3aVbDSglUerKRA84H5RSECkY6AbT6Nzp07S4UKFbTD88knn3TjCp8EJj+WYCEgBPgm/Kn7uXLl0vmwyoHl1w8//FB/cLFTp06i3gWRvn37inrfQ5MGTAp/mge0lOjoaF1eevPBMQqiw2rJww8/rO8FSfXp00feffddjxfLdCK/iECEIWDLa+TemMEnAI0CkxZP6owINApDECCgUAq0G5AciGzhwoXSr18/mT9/fob7FMo+sC4iYDcCtvg0vBuFyQ0/R0YJA+VCQ0BZoSIM/I9M8+bN9b/2o14QBhy8Q4cOlQYNGvjVarwx4DkRCFcEbDNPwgUgmDrQkEAceL8E5g3eQAVp4X9WoHlQiEAkIxAU8ySzAwrzasGCBaL+P0Uv72JFBT4ZvHtCIQKRjgBJI9L/Ath/InCFCATFp3GFbWB2IkAEMhECJI1MNFhsKhFwAgIkDSeMAttABDIRAiSNTDRYbCoRcAICJA0njALbQAQyEQIkjUw0WGwqEXACAiQNJ4wC20AEMhECJI1MNFhsKhFwAgIkDSeMAttABDIRArb87wk2EqYQASIQGQjwNfLIGGf2kgjYhgDNE9ugZEFEIDIQIGlExjizl0TANgRIGrZByYKIQGQgQNKIjHFmL4mAbQiQNGyDkgURgchAgKQRGePMXhIB2xAgadgGJQsiApGBAEkjMsaZvSQCtiFA0rANShZEBCIDAZJGZIwze0kEbEOApGEblCyICEQGAiSNyBhn9pII2IYAScM2KFkQEYgMBEgakTHO7CURsA0BkoZtULIgIhAZCJA0ImOc2UsiYBsCJA3boGRBRCAyECBpRMY4s5dEwDYESBq2QcmCiEBkIEDSiIxxZi+JgG0IkDRsg5IFEYHIQICkERnjzF4SAdsQsCXuibU1B5LPytRte2XZgaOy62SyTiqVECc3Fs4nHcoVk8JxsdbsPCYCRCCTIWCrpjFj5365f95KcSkQ+l9fWea1u0l/cIxrSEOejEhSUpL8/vvv4nK5xHqckTLD8d79+/fLH3/8oXEKx/6xT9cOAdtIA2Tw+ebd8n7T2tKjWlmpkidBorNE6Q+Oce0DlYY86SEOkMKzzz4rw4YN80Bnz5498tJLL+nJYD32yMQTWbBggTz//PMap9dff1369OmjUTl9+rRs27aNZMK/katGwBbzBCbJ6LVbNClUVgSx6dhJmbhpl6w8mKgbVr9QXnm8cilB2uD610m3X/6QBupaWqbKgQMHZNGiRRIbGys9e/aUPHny6LKio6Mla9asqY6vGoEwvTF37tyCD+TRRx+V8+fP6+N9+/bJE088IT/99JNERUXpa/wiAleCgC2aBnwY95UvrkkBhNHj17WyeN8ROXvhov7gGNeQBq0DeXFPWjJ//nypU6eOlCpVSpYuXZpWVo80aCgjRoyQb7/9Vl/H+aBBg2TdunX6fOvWrXLXXXdJzZo15ZlnnpFDhw65802cOFFfr1+/vqB+CJ7YrVq1knbt2smDDz4oFy5cEJMP7Zs6darPp/b69ev1PagHT/njx4/r8mA2dO/eXdfTsWNHQXtMPZjcvXr10mldunRx36MzXP5Cf0z91nbi+pdffqnvRXuHDx8u8fHx+q6NGzfKypUrZdasWXL33XfL0aNHpXHjxnLs2DFr0TwmAulCwBbSgNOzZfGCukJoGCALb8E1pEGQF/f4EzwVP/vsM3nuueekW7du8sEHH8jFi6nL9Hc/AlIfPHjQnbxr1y5JSUnRT9sePXrIzTffLDNmzJDDhw/Lk08+qcuePHmyjB8/Xj7++GPp37+/vPDCC7J9+3Y5ceKEJpZbb71VX//55591PkzQUaNGaUL6888/3XXhAJPxgQcekLZt28q0adME9cOkOnfunDz00EOSL18++fHHH6VBgwb6qQ8iQj1r1qyR2rVr677DhAAheYu/dq5evVpGjhwpQ4cO1e2y3of2AI+bbrpJE2pCQoJMmDBB8EshAleKgC3mCVZJyue69FQzJomvhpg05DUrK77ybdq0STs5a9SooSc7JjEmXpkyZXxl93ktS5bUfIjJefbsWcmZM6cUK1ZMEwSIASQFsoAPAJO2SpUqMmnSJPnnn3+0FlG2bFmtHaBMXIOJlCtXLqlevbpgEhcpUsSjDSARmFPQKLJlyyZvv/22Lh9m1SeffCJxcXHaNICmgPtBGNAUUM8jjzwiqKdr165y5MgRj3JBfL7auXnzZq2N3XnnnYIPBCSFuqyCNqFvqL9y5cq6Hms6j4lAehBIPbPSc1eQ80ALwAT57rvvZPr06Xqi4wl/tWIIBP6Rd955Rz788EOpW7euntR58+bVdYFMoDlcf/310qhRI61lgFC85Y477pD27du7TY+1a9dqArHmg6ZTokQJ96QEQb366qv6/Ndff5UWLVpokweaFMSXbwHE5C3QVHy1c8eOHdrkKF++vPctPCcCtiNgC2ngPYytJ07pxsHp6U9MGvLiHl+Cpy6IAhMLExK+iObNm+snLIgkvRITE5MqKyYdNIQlS5ZoX0W5cuXk6aefdk/aN998U9cHVR+mwlNPPZWqDDhocR3pH330kV7dwbFVChQoICAOI1ixQD/g14C/BdoF7pkzZ47JkuoXmoe3GAewdzuhlUB7gLllxOQ159bfHDlyWE95TASuCAFbSAMvbv2055JDEasksVlTF4trSIMgL+7xJXgHA4KlVnwwyfBJTk4Wb9+Br/txDRMIT3RMUjgAV6xYoYkB59ASZs+eLdAwYF5gQkMDueWWW2Tw4MHaDML7HzAT4ED0FvhaYAKgLJAO/BMwe6xSrVo1/eQHKZw5c0b7QKBVGL8MNBj4GMaMGWO9LeCxv3bCnIOjFn4WvJuBsr/66iu3I9RaMEwxmD1wyIKY4PCF/4RCBNKLgC0+DbzpiRe34ODE6sj4JrX8LrliBWXy1j3ydev6qdqIP2JoGZ07d9Z+A5MBT0Z4/eEYfPzxx8X6pLQeIz9UfaxAwBHZpEkT9/IsrhcsWFD7F+Dk7Nu3ryYLaAt4KmNSY1UBkw8CJ2bp0qVly5YtHg5D5MP7IdB+IGgX/CBWgY8DZhB8JJCiRYvqCQ2CGThwoLz88sv6OvwKkJMnT+r+Wh2TvkwWXPPXTvgqsLoD7IzA0QqxlgVTCaR6++23a8IYO3as3HfffZoAzX38JQJpIRCVlHJJD07IIH2Yl7teV+9h4H0MX7JREcbAlRvk4Uol5Y7Sns5DX/kzeg1aBCaIddKgTDzxobmAcLzTYMLABwIHZlqCsmECpZUP9cCkgoZgFX/XrXkCHftrp7/r3uXBN+LdLu88PCcCvhCwjTRQOIgDL3nhPQxoHWZFBT4MmCTQMF6sVSEkhOGrs7xGBIhAxhGwlTTQHP7DWsYHhSUQAScjYDtpOLmzbBsRIAIZRyD1MkfGy2QJRIAIhDECJI0wHlx2jQgEAwGSRjBQZZlEIIwRIGmE8eCya0QgGAiQNIKBKsskAmGMAEkjjAeXXSMCwUCApBEMVFkmEQhjBEgaYTy47BoRCAYCJI1goMoyiUAYI0DSCOPBZdeIQDAQIGkEA1WWSQTCGAGSRhgPLrtGBIKBQNqbRlxFjdinAntWYlu8U6cubQGIrfQLFy4sZdTGwNjfgkIEiEDmRcDW/3LFjuHYkg+7amOHKOzHCcG+n9gzE9vcYYdxxDJJj2CjGOyqldZGN+kpJ715sNX/8uXL9fZ92LIPO3dRiAAR8ETANtIAYWB7f+zybaKheVZ1KR7IqlWrpGLFimkSB/b1RHwSkAYEG/ni3Owq7l3u1Z4jXCG22nvjjTc0sWHvT2hHlSpVkuLFi+vdyb139rraungfEQgXBGwxT8ymvwjG448wABjSQCrYDRz7dfoyVaCRIGxgv379BAGKdu/eLYg2ho2AEWjITrGGK0SkNWyVt2zZspBpNnb2hWURgVAhYIsjFD4MmCRpEYbpEPIgL+7xJdgJHHtXYuNb5IU5g8hh2P0b92CX8CFDhujwg9j814Q1RFmI/YoARAiF+N5777l3/4bZAU0F1xEKEcGFICZcIcrABsHQOpo2bar9MdbdyP2FWNSFqC9oRIiHYnYvx3mnTp3cYQ+t7ULgJLN7OfpjQkQi2DX6iM2VsUs52om+ILocMMFGyGg/+owdxylE4FohYAtpwOkJH0Z6BXlxjy9BGhynmDS//fabDgGA2KSY9JhsiIUCMwWxWuFzwO7k2LwXExsTb8CAAToeCSKRIVQBNvFFHuw0/v333+tASNixGwRhwhVit3CESTDhCkFa0HCweTDy+AqxiHKNYKIjLADyQ3AOjcn8ol0o//PPP9ehBRCsCWYQdg/HjumIgwI8ELIB9+zcuVPvgg5tCyQxevRoHXIA7QeZIs4JiIRCBK4FAraYJ5gAxumZnk4gr1lZ8c6PkIkgBEQ7M8GKsG0/TBQIJjTOkQ9Bjlu2bKkdrN988400a9ZMWrdurcMBYKLD1MA2/tAk5s6dq0MJYAIjLojxl6BM7EpuDVcIMwUfiL8QizoxHV8w3SCoA1oTosehbjhcISA0kFXPnj014YEYUTf63qFDB00iIC7kgYmG9iN8AncS1/Dx6xogYAtp2N3u/Pnza+ckor0jHCNUcxAN/CEQo96DOBBLJDExUT95YQY0bNjQ3RwEQ4IGgAlm/CdYicFTP70CjcFXiMX03o+ASoh1gkDWEJgtiIeCKG7QdhBJzgjaaTQI4/SFIxYhHaFpwXRCHsQq8RVBzpTDXyIQTARsIQ2YE1hWTY9PA51BXtzjS/AkRkT1d999Vz+db7vtNk0KX3zxhdSpU0ffYpZg8cSGxgLzAk9nrH7A34FjkweRxBBVDGo/BL/wCVx33XX6PNCXrxCLCKAEQjIT25CYqdMaEhF+ihtvvFGHZcSSM8gDGgMCKgGvefPm6dgr5h5TpmkX2gtyQf9hhs2aNUtrG8AI5VCIQKgRsMWngRe38EROryAv7vElJUuW1A7NadOm6ckC38Knn36qnYKYUCAKhFzEL3wDCJSMlRio8ojOZtT+cePGyddff60JpVChQoJzmAoLFiwQrJoY/4OvNhgSQJq/EIvW+0AW0GRgDqEOmEr4hZaAGK7wQ8BJCn8NyAZtB5HA7IAphvoWLlyoNRCrrwR1gDQQbxbaEcoD2YEEIdCiEHUO90DL+vvvv3WZ5prOxC8iYDcCiLCGT0ZETUDXzJkzXcpMCFgM8iAv7vEnyiRx1atXz6V8APqjnJsu9bR1qSe8+xrSVDhEl4rTqotRE8c1ceJEd7qKzepSDkWdtmPHDpfyd+g03LN06VJ9XZGKS2k0+hhlq5CMLjWBXSr+qkv5SlzKhNBpimjc5bZp08alwjLq69YvlGnai3vRfvQV7Xr//ffdacrB61JOT32rWnp2X0e7cI78vXv3dilHrrt4tM20H3VMmTJF51Mak64HWCrnqGvChAmuDRs26GvKzHHfzwMiYCcCjny5yxAjnsjWN0Lh0IRPAE9l2PTQPIxJYO7BU9dXKESkQ7uARnA1L2ylVW566obJpAbOpwMT/UR/ArUL7YdPw5gypl7+EoFQImCLTwMNNq+G48Utu14jxwSxCsgAEwy/1mDJ1jwgEu/7TLp3sGhzPT2/aZVr7k8rT1qOS3/tNeWa34y035TBXyKQUQRs0zRMQ2DLK3MgKP+wBqcnlkCxjIoJSiECRCD0CNhOGqHvAmskAkQglAjwcR1KtFkXEQgDBEgaYTCI7AIRCCUCJI1Qos26iEAYIEDSCINBZBeIQCgRIGmEEm3WRQTCAAGSRhgMIrtABEKJAEkjlGizLiIQBgiQNMJgENkFIhBKBEgaoUSbdRGBMECApBEGg8guEIFQIkDSCCXarIsIhAECJI0wGER2gQiEEgGSRijRZl1EIAwQIGmEwSCyC0QglAjYtglPKBvNukQOnzknW45fCrANPIrkiJUyOXMQGiIQdARIGkGH+OorSLnoksX7jsiRs5disJiSKuSKl9PnL0jf5etFZdFyfYE8MqZxDZOFv0QgaAg42jxJPJsizacvlmnb9wUNACcX/MzitbL5+EmfTWxUJJ88Xvm/qPYX5TJ7+MzNi0TAPgQcr2ngSXpWbfEfabL52EkpEpddnq5axmfXYZpM2bZX8sRGy4lzKT7z8CIRCAYCjicNf50GmfT+7S9ZfiBRskSJ3FuuuDxXo5x+3g7+faP8tOeQVt3rF8orb9xQTanz5+WhBavUjuAix9Uke6Z6WZXnsBxTx0fPpMgZRUxV8+aUcU1qSTQKvCxL9x+V11ZukALZY+XfU8kSkzWLdK5UUubsOqjP47NllWENq0q9gnl0faZNKKF5sQIyqH4VOZmSuu5WJQpJz1/Xyt5TZ3SZA+pWlhYqvxGYHzlU2b4EhPE/S/6UGNXOsU1qyvqjSfKrMmMoRCAUCDjaPEkLgIG/b5CVBxOle7Wy0lpNwMlb98gvauL875/bZP6/h9QTuqy8WKuCrDqUKJM27VLaykU9eZMVOXQsX0xAJjB/9qlJe68671ShhPydmCQzd+73qBZkckbdmzMmmwyqV0VP5P/bsFOfv3J9JZ13+OrNckGxUf/lf8sKRWJoU+fKpWTh3sMyQqWlqrtgXun68xqlIZyXfnUqaQfmwJUbNZl5VO7jxJswSsTHSduShWRog/RFjPNRJC8RgStCIFNqGngKL1EawE1F8kuHskXVZDsvi/YekdWHjmkCACEUi88uxxUpxKvoZ+uOHFeayKWo9lD37y9fXGsk51WMlNoFcks3dQ0eARAGSMJboHgMrFdZMEFR91trt8iYm2pInNIEVh8+LguVVpOonJXLDx6VO8oUkYcqltBFbDyWJD+rdoHAIKZukB1WP0BqzYrll4JxMfLC0r9kkzJJGqi2+xNvwgAZ4ROrtB8KEQgVApmSNKDuX1RPdqjkrWcudWO1Pem0nEq5IP1X/C3n1GSKVmEOUhQxZFXhDCEwaRCwyCpZLqfhWjaLWWLNg+Pzl5cpEqKzarMg2+UQCmiHSJSavC6lbYhUzJ3gvrWN0oBAZBBr3Umq/ZDRinzwMbLtxKk0SWOrSgdBYJUEBPbKig3SpUopKa9WUyhEIFQIZArSiPGKcQIygNyjtIdeNctf1g6i9IR6UT2x88REy9et62vfRIe5K7TpYCegMEW8BW0E50CDMLJCaRSXCCt1fuQZoXwhNxTOq8kGWk9CdNrDATMEfg/4VShE4Foh4Pi/PkxE+Brw+V09tfGJVpOmXM54vRQLR+Ue5ZdoP2e5/LDzgMYRJsRfR08IfA8Hk8/aor77IgrroGEVA1rGZ5t3Kz/KMa0FzVO+lVrK/DFaicl/Y+F8lzQG5X/ZfTJZmVpH5I7Zv8m+02dMFimVM052KM0J72pYxRAGNCnkL5ojuzWZx0Qg6Aik/WgLevWBK4BhMWf3Qf0xuZ9VqySjbqymVx/6/LZeX8bkaaCe2hVyx0t3tSrx7OJ1ymgQ9fSPkkPJ57QWAAKKzfrfigTIJy2TxNSHX2PieB9DwzBlvKXa1HXRH3plA/nwhuawBlWV6XJB12/qhi9kpNIy0PbOP61GVsF7F4Xi/gtDmS82RloWLyiPL1ztNo10xstfMFPuU74Zfyss1rw8JgJ2IpDpI6zBP4Al0uwWMgBAWFbNpcwUEEeoBW2CBZNLrbgEErQzTrXdaBCB8jOdCFxrBDI9aVxrAFk/EYg0BBzv04i0AWF/iYDTESBpOH2E2D4i4DAESBoOGxA2hwg4HQGShtNHiO0jAg5DgKThsAFhc4iA0xEgaTh9hNg+IuAwBEgaDhsQNocIOB0BkobTR4jtIwIOQ4Ck4bABYXOIgNMRIGk4fYTYPiLgMARIGg4bEDaHCDgdAZKG00eI7SMCDkOApOGwAWFziIDTESBpOH2E2D4i4DAESBoOGxA2hwg4HQGShtNHiO0jAg5DgKThsAFhc4iA0xEgaTh9hNg+IuAwBEgaDhsQNocIOB0BkobTR4jtIwIOQ4Ck4bABYXOIgNMR+H9Aywkjmi5+mwAAAABJRU5ErkJggg==) !

You can specify which users can edit. Options include:

* All users can edit.
* Specific users can edit.

## Predicate Pushdowns

Dremio offloads these operations to MongoDB:

ABS  
ADD  
AND  
CASE  
CEIL  
CONCAT  
DAY\_OF\_MONTH  
DIVIDE  
EQUAL  
EXP  
FLOOR  
GREATER  
GREATER\_OR\_EQUAL  
HOUR  
LESS  
LESS\_OR\_EQUAL  
LN  
LOG  
LOG10  
MAX  
MIN  
MINUTE  
MOD  
MONTH  
MULTIPLY  
NOT  
NOT\_EQUAL  
OR  
POW  
REGEX  
SECOND  
SQRT  
SUBSTR  
SUBTRACT  
TO\_LOWER  
TO\_UPPER  
TRUNC  
YEAR

## For More Information

For information about Dremio data types, see [Data Types](/dremio-cloud/sql/data-types/).

## Limitations

Queries that un-nest nested fields are not allowed as they would cause incorrect schemas. This may be easily circumvented by pushing filters into the subquery or by simply not referencing the alias.

# Data Type Mapping

Dremio supports selecting the following MongoDB Database types.
The following table shows the mappings from MongoDB to Dremio data types. If there are additional MongoDB types not listed in the table, then those types are not supported in Dremio.

| MongoDB Database Type | Dremio Type |
| --- | --- |
| ARRAY | LIST |
| BINDATA | VARBINARY |
| BOOL | BOOLEAN |
| DATE | TIMESTAMP |
| DBPOINTER | { "namespace": VARCHAR, "id": VARBINARY } |
| DOUBLE | DOUBLE |
| INT | INTEGER (or DOUBLE if store.mongo.read\_numbers\_as\_double set) |
| JAVASCRIPT | VARCHAR |
| JAVASCRIPTWITHSCOPE | { "code": VARCHAR, "scope": { ... } } |
| LONG | BIGINT (or DOUBLE if store.mongo.read\_numbers\_as\_double set) |
| OBJECT | STRUCT |
| OBJECTID | VARBINARY |
| REGEX | { "pattern": VARCHAR, "options": VARCHAR } |
| STRING | VARCHAR |
| SYMBOL | VARCHAR |
| TIMESTAMP | TIMESTAMP |

Was this page helpful?

* Supported Versions
* Prerequisites
* Configure MongoDB as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Share
* Predicate Pushdowns
* For More Information
* Limitations

<div style="page-break-after: always;"></div>

# Vertica | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/vertica

On this page

[Vertica](https://www.vertica.com/) is an analytical database.

## Prerequisites

Ensure that you have the following details before configuring Vertica as a source:

* Database name
* Hostname or IP address
* Port
* Outbound port (5433 is the default port) open in your AWS or Azure security group

## Configure Vertica as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Vertica**.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### General

For **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

| Name | Description |
| --- | --- |
| Host | Vertica host name. |
| Port | Vertica port number. Defaults to 5433. |
| Database | Service name of your database. |

#### Authentication

* For **Username**, enter your Vertica username.
* For **Password**, enter your Vertica password.

### Advanced Options

Specify advanced options with the following settings.

* **Record fetch size**: Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. By default, this is set to **10**.
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to **8**.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to **60**.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Enable external authorization plugin**: When enabled, authorizes an external plugin.
* **Connection Properties**: Connection properties and values for the data source.

### Reflection Refresh

You can set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed.

| Option | Description |
| --- | --- |
| **Never refresh** | Select to prevent automatic Reflection refresh, default is to automatically refresh. |
| **Refresh every** | How often to refresh Reflections, specified in hours, days or weeks. This option is ignored if **Never refresh** is selected. |
| **Set refresh schedule** | Specify the daily or weekly schedule. |
| **Never expire** | Select to prevent Reflections from expiring, default is to automatically expire after the time limit below. |
| **Expire after** | The time limit after which Reflections expire and are removed from Dremio, specified in hours, days or weeks. This option is ignored if **Never expire** is selected. |

### Metadata

Specifying metadata options is handled with the following settings.

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information needed for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Control](/dremio-cloud/security/privileges/) for additional information about privileges.

note

All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update a Vertica Source

To update a Vertica source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configure Vertica as a Source.
4. Click **Save**.

## Delete a Vertica Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Vertica source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

   caution

   Deleting a source causes all downstream views that depend on objects in the source to break.

   note

   Sources containing a large number of files or tables may take longer to be deleted. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being deleted. Once complete, the source disappears.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

`*`, `+`, `-`, `/`, `%`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
AND, NOT, OR, `||`  
ABS  
ACOS  
ADD\_MONTHS  
ASIN  
ATAN  
ATAN2  
AVG  
BTRIM  
CAST  
CBRT  
CEIL  
CEILING  
CHAR\_LENGTH  
CHARACTER\_LENGTH  
CONCAT  
COS  
COT  
DATE\_ADD  
DATE\_PART  
DATE\_SUB  
DATE\_TRUNC\_CENTURY  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_DECADE  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MICROSECOND  
DATE\_TRUNC\_MILLISECOND  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_QUARTER  
DATE\_TRUNC\_SECOND  
DATE\_TRUNC\_WEEK  
DATE\_TRUNC\_YEAR  
DEGREES  
E  
EXP  
EXTRACT\_CENTURY  
EXTRACT\_DAY  
EXTRACT\_DECADE  
EXTRACT\_DOW  
EXTRACT\_DOY  
EXTRACT\_EPOCH  
EXTRACT\_HOUR  
EXTRACT\_MILLENNIUM  
EXTRACT\_MINUTE  
EXTRACT\_MONTH  
EXTRACT\_QUARTER  
EXTRACT\_SECOND  
EXTRACT\_WEEK  
EXTRACT\_YEAR  
FLOOR  
ILIKE  
IS DISTINCT FROM  
IS NOT DISTINCT FROM  
IS NOT NULL  
IS NULL  
ISNULL  
LAST\_DAY  
LCASE  
LEFT  
LENGTH  
LIKE  
LN  
LOCALTIME  
LOCALTIMESTAMP  
LOCATE  
LOG  
LOG10  
LOWER  
LPAD  
LTRIM  
MAX  
MIN  
MOD  
NOW  
NULLIF  
PI  
POSITION  
POW  
POWER  
RADIANS  
RANDOM  
REGEXP\_REPLACE  
REPLACE  
RIGHT  
ROUND  
RPAD  
RTRIM  
SIGN  
SIN  
SQRT  
STDDEV  
STDDEV\_POP  
STDDEV\_SAMP  
STRPOS  
SUBSTR  
SUBSTRING  
SUM  
TAN  
TIMESTAMPADD  
TIMESTAMPDIFF  
TO\_CHAR  
TO\_DATE  
TO\_NUMBER  
TO\_TIMESTAMP  
TRIM  
TRUNC  
TRUNCATE  
UCASE  
UPPER  
VAR\_POP  
VAR\_SAMP  
VARIANCE

Was this page helpful?

* Prerequisites
* Configure Vertica as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update a Vertica Source
* Delete a Vertica Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Data Type Mapping

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/postgres

On this page

[PostgreSQL](https://www.postgresql.org/) is an open source object-relational database management system that is known for its reliability and performance.

## Prerequisites

Ensure that you have the following details before configuring PostgreSQL as a source:

* Database name
* Hostname or IP address
* Port
* Outbound port (5432 is the default port) open in your AWS or Azure security group

## Configure PostgreSQL as a Source

Perform these steps to configure PostgreSQL:

1. On the Datasets page, you can see a truncated list of **Sources** at the bottom-left of the page. Click **Add Source**.

   Alternatively, click **Databases**. The page displays all database sources. Click the **Add database** button at the top-right of that page.
2. In the **Add Data Source** dialog, click **PostgreSQL**.

   The following section describes the source configuration tabs.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### General

The **General** tab contains the required fields to create a PostgreSQL source.

![](/assets/images/postgres-general-8196de68127b20feb46abe5bdf68a384.png)

Perform these steps in the **General** tab:

1. In the **General** tab, for **Name**, enter a name. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. For **Host**, enter the PostgreSQL host name.
3. For **Port**, enter the PostgreSQL port number. The default port is 5432.
4. For **Database**, enter the PostgreSQL database name.
5. (Optional) For **Encrypt connection**, enable encrypted connections to PostgreSQL using SSL. You can modify the encryption validation mode under **Advanced Options**.
6. For **Authentication**, you must choose one of the following authentication options:

   * **Master Authentication**, this is the default option. Provide the username and password of a master database user with permissions to read required objects:
     + For **Username**, enter your PostgreSQL database username.
     + For **Password**, enter your PostgreSQL database password.
   * **Secret Resource Url**:
     + For **Username**, enter your PostgreSQL database username.
     + For **Secret Resource Url**, enter the Secret Resource URL that allows Dremio to fetch the password from [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). The Secret Resource URL is the Amazon Resource Name (ARN) for the secret (for example, `arn:aws:secretsmanager:us-west-2:123456789012:secret:my-rds-secret-VNenFy`).

### Advanced Options

Click **Advanced Options** in the sidebar.

![](/assets/images/postgres-adv-options-b34cd338bfbb986277bbcc9d9ea834bb.png)

note

All advanced options are optional.

| Advanced Option | Description |
| --- | --- |
| **Record fetch size** | Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default record fetch size is 200. |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Encryption**   **Validation Mode** | When encryption is enabled, set the validation mode as one of the following:  * **Validate certificate and hostname** (default mode) * **Validate certificate only** * **Do not validate certificate or hostname** |
| **Connection Properties** | Custom key value pairs for the connection relevant to the source. To add a connection property, click **Add property** and add the property name and value. |

### Reflection Refresh

The **Reflection Refresh** tab in the sidebar allows you to set time intervals for Reflections to refresh or expire.

![](/assets/images/postgres-reflection-refresh-8bc86e0010238700aa08d8aba8a4a0fd.png)

### Metadata

You can configure settings to refresh metadata and handle datasets. Click **Metadata** in the sidebar.

![](/assets/images/postgres-metadata-e66c9225307d756198205b4c2f0d31f8.png)

You can configure Dataset Handling and Metadata Refresh parameters.

##### Dataset Handling

These are the **Dataset Handling** parameters.

note

All **Dataset Handling** parameters are optional.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

##### Metadata Refresh

These are the **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  note

  All **Dataset Details** parameters are optional.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

You can grant privileges to specific users or roles.

![](/assets/images/postgres-privileges-9322dec7fd163edd9acbb00cc83ed50d.png)

1. (Optional) For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **Users** table.
2. (Optional) For the users or roles in the **Users** table, toggle the green checkmark for each privilege you want to grant to the PostgreSQL source that is being created.

Click **Save** after setting the configuration.

## Edit a PostgreSQL Source

To edit a PostgreSQL source:

1. On the Datasets page, click **Databases**. A list of databases is displayed.
2. Hover over the database and click the Settings ![This is the icon that represents the Database settings.](/images/icons/settings.png "Icon represents the Database settings.") icon that appears next to the source.
3. In the Source Settings dialog, you cannot edit the name. Editing other parameters is optional.
4. Click **Save**.

## Remove a PostgreSQL Source

To remove a PostgreSQL source, perform these steps:

1. On the Datasets page, click **Databases**. A list of sources is displayed.
2. Hover over the source and click the More (...) icon that appears next to the source.
3. From the list of actions, click **Remove Source**. Confirm that you want to remove the source.

caution

Removing a source causes all downstream views dependent on objects in this source to break.

note

Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Predicate Pushdowns

Dremio offloads these operations to Postgres.

`*`, `+`, `-`, `/`, `%`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
`AND`, `NOT`, `OR`, `||`  
`ABS`  
`ACOS`  
`ADD_MONTHS`  
`ASIN`  
`ATAN`  
`ATAN2`  
`AVG`  
`CAST`  
`CBRT`  
`CEIL`  
`CEILING`  
`CHAR_LENGTH`  
`CHARACTER_LENGTH`  
`CONCAT`  
`COS`  
`COT`  
`COVAR_POP`  
`COVAR_SAMP`  
`DATE_ADD`  
`DATE_SUB`  
`DATE_TRUNC_CENTURY`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_DECADE`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_QUARTER`  
`DATE_TRUNC_SECOND`  
`DATE_TRUNC_WEEK`  
`DATE_TRUNC_YEAR`  
`DEGREES`  
`E`  
`EXP`  
`EXTRACT_CENTURY`  
`EXTRACT_DAY`  
`EXTRACT_DECADE`  
`EXTRACT_DOW`  
`EXTRACT_DOY`  
`EXTRACT_EPOCH`  
`EXTRACT_HOUR`  
`EXTRACT_MILLENNIUM`  
`EXTRACT_MINUTE`  
`EXTRACT_MONTH`  
`EXTRACT_QUARTER`  
`EXTRACT_SECOND`  
`EXTRACT_WEEK`  
`EXTRACT_YEAR`  
`FLOOR`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LCASE`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LN`  
`LOCATE`  
`LOG`  
`LOG10`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MEDIAN`  
`MIN`  
`MOD`  
`PERCENT_CONT`  
`PERCENT_DISC`  
`PI`  
`POSITION`  
`POW`  
`POWER`  
`RADIANS`  
`REGEXP_LIKE`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SIN`  
`SQRT`  
`STDDEV`  
`STDDEV_POP`  
`STDDEV_SAMP`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TAN`  
`TO_CHAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UCASE`  
`UPPER`  
`VAR_POP`  
`VAR_SAMP`

# Data Type Mapping

Dremio supports PostgreSQL data types, as shown in the following table which provides the mappings from PostgreSQL to Dremio data types. If there are additional PostgreSQL types not listed in the table, then those types are not supported in Dremio.

| PostgreSQL Data Type | Dremio Type |
| --- | --- |
| BIGSERIAL | BIGINT |
| BIT | BOOLEAN |
| BOOL | BOOLEAN |
| BPCHAR | VARCHAR |
| BYTEA | VARBINARY |
| CHAR | VARCHAR |
| DATE | DATE |
| DOUBLE PRECISION | DOUBLE |
| FLOAT4 | FLOAT |
| FLOAT8 | DOUBLE |
| INT2 | INTEGER |
| INT4 | INTEGER |
| INT8 | BIGINT |
| INTERVAL\_DS | INTERVAL (day to seconds) |
| INTERVAL\_YM | INTERVAL (years to months) |
| MONEY | DOUBLE |
| NAME | VARCHAR |
| NUMERIC | DECIMAL |
| OID | BIGINT |
| SERIAL | INTEGER |
| TEXT | VARCHAR |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| TIMESTAMPTZ | TIMESTAMP |
| TIMETZ | TIME |
| VARCHAR | VARCHAR |

Was this page helpful?

* Prerequisites
* Configure PostgreSQL as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Edit a PostgreSQL Source
* Remove a PostgreSQL Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# SAP HANA | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/sap-hana

On this page

Dremio supports direct connections to SAP HANA using only a username and password.

## Supported Versions

The SAP HANA source supports SAP HANA 2.0. The connector was tested against [HANA Express](https://hub.docker.com/r/saplabs/hanaexpress).

## Configure SAP HANA as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **SAP HANA**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

* Under **Host**, enter the URL or IP address for the SAP HANA instance. Example: `sap://myServer:`
* Under **Port**, enter the port required to access the data source. Port 39017 is the default for SAP HANA.
* Under **Schema (optional)**, enter the schema within the SAP HANA instance that you would like to connect to.

#### Authentication

Choose an authentication method:

* **User Credentials** - Dremio must provide a specified username and password in order to access the SAP HANA.
  + **Username** - The username with sufficient privileges to perform read/write actions on the SAP HANA instance
  + **Password** - The password associated with the username.

### Advanced Options

The following settings control more advanced functionalities in Dremio.

* **Advanced Options**
  + \*\*Record fetch size \*\* - Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default value is `200`.
  + \*\*Maximum idle connections \*\* - The maximum number of idle connections to keep. The default value is `8`.
  + \*\*Connection idle time (s) \*\* - Idle time, in seconds, before a connection is considered for closure. The default value is `60`.
  + \*\*Query timeout (s) \*\* - The timeout, in seconds, for query execution before it is canceled. Set to `0` for no timeout. The default value is `0`.
* **Connection Properties**
  + \*\*Name \*\* - The unique name for any custom properties.
  + \*\*Value \*\* - The value associated with the custom property.

### Reflection Refresh

This tab controls the frequency of Reflection refreshes or the timespan for expiration for any queries performed using this data source.

* \*\*Never refresh \*\* - Prevents any query Reflections associated with this source from refreshing.
* \*\*Refresh every \*\* - Sets the time interval by which Reflections for this source are refreshed. This may be set to hours, days, and weeks.
* \*\*Set refresh schedule \*\* - Specify the daily or weekly schedule.
* \*\*Never expire \*\* - Prevents any query Reflections associated with this source from expiring.
* \*\*Expire after \*\* - Sets the time after a Reflection is created that it then expires and can no longer be used for queries. This may be set to hours, days, and weeks.

### Metadata

This tab offers settings that control how dataset details are fetched and refreshed.

* **Dataset Handling**
  + \*\*Remove dataset definitions if underlying data is unavailable \*\* - If this box is not checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.
* **Metadata Refresh**
  + **Dataset Discovery**
    - \*\*Fetch every \*\* - Specifies the time interval by which Dremio fetches object names. This can be set by minutes, hours, days, and weeks.
  + **Dataset Details**
    - \*\*Fetch mode \*\* - Restricts when metadata is retrieved.
    - \*\*Fetch every \*\* - Specifies the time interval by which metadata is fetched. This can be set by minutes, hours, days, and weeks.
    - \*\*Expire after \*\* - Specifies the timespan for when dataset details expire after a dataset is queried. This can be set by minutes, hours, days, and weeks.

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Control](/dremio-cloud/security/privileges/) for additional information about privileges.

note

All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The **USERS/ROLES** table will display the added user or role.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update an SAP HANA source

To update an SAP HANA source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name.
4. Click **Save**.

## Delete an SAP HANA Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an SAP HANA source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

   caution

   Deleting a source causes all downstream views that depend on objects in the source to break.

   note

   Sources containing a large number of files or tables may take longer to be deleted. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being deleted. Once complete, the source disappears.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of the following expressions and functions:

`%`, `*`, `+`, `-`, `/`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
AND, NOT, OR, `||`  
ABS  
ACOS  
ADD\_MONTHS  
ASIN  
ATAN  
ATAN2  
AVG  
CAST  
CBRT  
CEIL  
CEILING  
CHAR\_LENGTH  
CHARACTER\_LENGTH  
CONCAT  
COS  
COT  
DATE\_ADD  
DATE\_DIFF  
DATE\_SUB  
DATE\_TRUNC\_CENTURY  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_DECADE  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MILLENIUM  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_SECOND  
DATE\_TRUNC\_YEAR  
DEGREES  
E  
EXP  
EXTRACT\_DAY  
EXTRACT\_DOW  
EXTRACT\_DOY  
EXTRACT\_HOUR  
EXTRACT\_MINUTE  
EXTRACT\_MONTH  
EXTRACT\_QUARTER  
EXTRACT\_SECOND  
EXTRACT\_WEEK  
EXTRACT\_YEAR  
FLOOR  
IS DISTINCT FROM  
IS NOT DISTINCT FROM  
IS NOT NULL  
IS NULL  
LCASE  
LEFT  
LN  
LOCATE  
LOG  
LOG10  
LPAD  
LTRIM  
MAX  
MIN  
MOD  
MONTH  
PI  
POSITION  
POW  
POWER  
RADIANS  
RAND  
REPLACE  
REVERSE  
RIGHT  
ROUND  
RPAD  
RTRIM  
SIGN  
SIN  
SQRT  
SUBSTR  
SUBSTRING  
SUM  
TAN  
TO\_CHAR  
TO\_DATE  
TRIM  
TRUNC  
TRUNCATE  
UCASE  
UPPER  
YEAR

Was this page helpful?

* Supported Versions
* Configure SAP HANA as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update an SAP HANA source
* Delete an SAP HANA Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Snowflake | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/snowflake

On this page

[Snowflake](http://www.snowflake.com) is a cloud data warehouse.

## User Impersonation

Dremio supports OAuth with impersonation for Snowflake. This allows Dremio users to authenticate via external OAuth and map to Snowflake roles securely. For reference, see [Snowflake's Create Security Integration (External OAuth) documentation](https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-oauth-external).

Before configuring a Snowflake source with user impersonation, perform the following steps:

1. Run the following curl commands to obtain the Dremio OAuth parameters (issuer and public key):

   To get the issuer:

   ```
   curl --location 'https://<dremio_url>/api/v3/external-oauth/discovery/jwt-issuer' \  
   --header 'Authorization: Bearer <Token>' \  
   --header 'Content-Type: application/json' \  
   --data ''
   ```

   To get the public key:

   ```
   curl --location 'https://<dremio_url>/api/v3/external-oauth/discovery/jwks' \  
   --header 'Authorization: Bearer <Token>' \  
   --header 'Content-Type: application/json' \  
   --data ''
   ```

   The above JWKS response needs to be converted to PEM format, which Snowflake accepts. We recommend using this open-source tool: [rsa-jwks-to-pem](https://github.com/bcmeireles/rsa-jwks-to-pem).

   Example conversion:

   ```
   python rsa-jwks-to-pem.py key_jwks.json
   ```
2. Create a [Snowflake external OAuth security integration](https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-oauth-external) in Snowflake.
   Set `EXTERNAL_OAUTH_ISSUER` to the issuer obtained from Dremio, `EXTERNAL_OAUTH_RSA_PUBLIC_KEY` to the PEM-formatted key from the script, and `EXTERNAL_OAUTH_AUDIENCE_LIST` to any additional audience values for token validation beyond your Snowflake account URL.

   Create Security Integration 

   ```
   CREATE OR REPLACE SECURITY INTEGRATION snowflake_imp  
   TYPE = EXTERNAL_OAUTH  
   ENABLED = TRUE  
   EXTERNAL_OAUTH_TYPE = CUSTOM  
   EXTERNAL_OAUTH_ISSUER = '<issuer-from-dremio>'  
   EXTERNAL_OAUTH_AUDIENCE_LIST = ('<audience-values>')  
   EXTERNAL_OAUTH_ALLOWED_ROLES_LIST = ('REGRESSION', 'ACCOUNTADMIN', 'PUBLIC')  
   EXTERNAL_OAUTH_RSA_PUBLIC_KEY = '<PEM-formatted-key>'  
   EXTERNAL_OAUTH_TOKEN_USER_MAPPING_CLAIM = 'sub'  
   EXTERNAL_OAUTH_SNOWFLAKE_USER_MAPPING_ATTRIBUTE = 'login_name';
   ```

   To configure Snowflake source in any mode (which allows users to assume any role they have access to in Snowflake), enable `EXTERNAL_OAUTH_ANY_ROLE_MODE` for Snowflake security integration:
   Alter Security Integration

   ```
   ALTER SECURITY INTEGRATION snowflake_imp SET EXTERNAL_OAUTH_ANY_ROLE_MODE = 'ENABLE';
   ```

## Configure Snowflake as a Source

1. In the bottom-left corner of the Datasets page, click **Add Source**.
2. Under **Databases** in the Add Data Source dialog, select **Snowflake**.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### General

Perform these steps in the **General** tab:

1. For **Name**, specify the name by which you want the Snowflake source to appear in the **Databases** section. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. For **Host**, specify the hostname of the Snowflake source in the format `LOCATOR_ID.snowflakecomputing.com`.
3. For **Port**, enter the port number. The default port is 443.

note

The optional connection parameters are case-sensitive. For example, if the name of a warehouse uses upper case only (e.g., WAREHOUSE1), specify it the same way in the **Warehouse** field.

4. (Optional) For **Database**, specify the default database to use.
5. (Optional) For **Role**, specify the default access-control role to use.
6. (Optional) For **Schema**, specify the default schema to use.
7. (Optional) For **Warehouse**, specify the warehouse that will provide resources for executing DML statements and queries.
8. Under **Authentication**, you must choose one of the following authentication methods:
   * **Login-password authentication**:
     + For **Username**, enter your Snowflake username.
     + For **Password**, enter your Snowflake password.
   * **Key-pair authentication** (see [Snowflake's key-pair documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth)):
     + For **Username**, enter your Snowflake username.
     + For **Private Key**, enter your generated Snowflake private key in Privacy Enhanced Mail (PEM) format.
     + (Optional) For **Private key passphrase**, enter the passphrase if you are using an encrypted private key.
   * **OAuth with impersonation**: This allows Dremio users to authenticate via external OAuth and map to Snowflake roles securely. If you have not already, complete the steps in User Impersonation.
     + Set the JWT `audience` parameter to match Snowflake’s `EXTERNAL_OAUTH_AUDIENCE_LIST`. This ensures proper token validation and role mapping between Dremio and Snowflake.

### Advanced

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |

### Reflection Refresh

On the Reflection Refresh page, set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed.

| Option | Description |
| --- | --- |
| **Never refresh** | Select to prevent automatic Reflection refresh, default is to automatically refresh. |
| **Refresh every** | How often to refresh Reflections, specified in hours, days or weeks. This option is ignored if **Never refresh** is selected. |
| **Never expire** | Select to prevent Reflections from expiring, default is to automatically expire after the time limit below. |
| **Expire after** | The time limit after which Reflections expire and are removed from Dremio, specified in hours, days or weeks. This option is ignored if **Never expire** is selected. |

### Metadata Options

On the Metadata page, you can configure settings to refresh metadata and handle datasets.

#### Dataset Handling

These are the optional **Dataset Handling** parameters.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

On the Privileges page, you can grant privileges to specific users or roles. See [Access Control](/dremio-cloud/security/privileges/) for additional information about user privileges.

1. (Optional) For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **Users** table.
2. (Optional) For the users or roles in the **Users** table, toggle the green checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Edit a Snowflake Source

To edit a Snowflake source:

1. On the Datasets page, click **External Sources** at the bottom-left of the page. A list of sources is displayed.
2. Hover over the external source and click the Settings ![This is the icon that represents the Source settings.](/images/icons/settings.png "Icon represents the Source settings.") icon that appears next to the source.
3. In the Source Settings dialog, you cannot edit the name. Editing other parameters is optional. For parameters and advanced options, see Configure Snowflake as a Source.
4. Click **Save**.

## Remove a Snowflake Source

To remove a Snowflake source, perform these steps:

1. On the Datasets page, click **External Sources** at the bottom-left of the page. A list of sources is displayed.
2. Hover over the source and click the More (...) icon that appears next to the source.
3. From the list of actions, click **Remove Source**. Confirm that you want to remove the source.

   caution

   Removing a source causes all downstream views dependent on objects in this source to break.

   note

   Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Predicate Pushdowns

These operations and functions are performed by Snowflake warehouses:

`||`, `AND`, `OR`  
`+`, `-`, `/`, `*`  
`<=`, `<`, `>`, `>=`, `=`, `<>`, `!=`  
`ABS`  
`ADD_MONTHS`  
`AVG`  
`BETWEEN`  
`CASE`  
`CAST`  
`CEIL`  
`CEILING`  
`CHARACTER_LENGTH`  
`CHAR_LENGTH`  
`COALESCE`  
`CONCAT`  
`COUNT`  
`COUNT_DISTINCT`  
`COUNT_DISTINCT_MULTI`  
`COUNT_FUNCTIONS`  
`COUNT_MULTI`  
`COUNT_STAR`  
`DATE_ADD`  
`DATE_SUB`  
`DATE_TRUNC`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_QUARTER`  
`DATE_TRUNC_WEEK`  
`DATE_TRUNC_YEAR`  
`DAYOFMONTH`  
`DAYOFWEEK`  
`DAYOFYEAR`  
`EXTRACT`  
`FLOOR`  
`ILIKE`  
`IN`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LOCATE`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MEDIAN`  
`MIN`  
`MOD`  
`NOT`  
`PERCENT_CONT`  
`PERCENT_DISC`  
`PERCENT_RANK`  
`POSITION`  
`REGEXP_LIKE`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SQRT`  
`STDDEV`  
`STDDEV_POP`  
`STDDEV_SAMP`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TO_CHAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UPPER`

Was this page helpful?

* User Impersonation
* Configure Snowflake as a Source
  + General
  + Advanced
  + Reflection Refresh
  + Metadata Options
  + Privileges
* Edit a Snowflake Source
* Remove a Snowflake Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Open Catalog | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/catalogs/open-catalog

On this page

Dremio's Open Catalog is a built-in lakehouse catalog powered by [Apache Polaris](https://polaris.apache.org/). It provides centralized, secure access to your Iceberg tables while automating data maintenance to keep performance optimized.

## Key Capabilities

* **Comprehensive Access Controls** – Protect your data with Role-Based Access Control (RBAC) alongside fine-grained security policies. RBAC privileges are enforced within the catalog itself, providing complete privilege enforcement as the catalog is shared with other projects or engines. Apply row filters to limit data visibility by criteria such as region, or use column masks to obfuscate sensitive information such as Social Security numbers.
* **Automatic Table Maintenance** – Open Catalog handles Iceberg table compaction and vacuum operations automatically, so you get optimal query performance and lower storage costs without manual intervention. These table maintenance jobs run on a dedicated engine that requires no routing rules, engine configuration, or scheduling.
* **Analyst-Friendly Data Discovery** – Built-in data product capabilities make it easy for analysts to find and understand data. Use semantic search to discover datasets with natural language, leverage descriptions and labels to understand business context, and explore lineage graphs to trace data transformations and assess downstream impact.
* **Multi-Engine Compatibility** – Access your catalog from any query engine or framework that supports the Iceberg REST API. Ingest data using Spark or Flink, then leverage Dremio to curate and deliver refined data products—all working from the same catalog.

Every project in your Dremio organization includes an Open Catalog by default. This catalog is automatically provisioned when you create a project and provides immediate access to your Iceberg tables with full control over security, maintenance, and data organization. Your Open Catalog is ready to use out of the box.

## Create a Namespace

Namespaces help you organize tables logically within your Open Catalog. You might create namespaces by team (Engineering, Revenue), by domain (Finance, Marketing), or by use case.

**To create a namespace:**

1. In the Data panel, click ![Add icon](/images/icons/plus.png "Add icon") next to **Namespaces**.
2. Enter a namespace name.
3. Click **Create**.

Your namespace is now ready for tables. You can create tables within the namespace using SQL or by uploading data through the Dremio console.

**Naming tips:**

* Use lowercase letters, numbers, and underscores for maximum compatibility across engines.
* Choose descriptive names that clearly indicate the namespace's purpose (e.g., `customer_analytics`, `finance_reporting`).
* Avoid spaces or special characters that may require escaping in SQL queries.

## Observe Table Maintenance

Open Catalog automatically performs maintenance operations such as compaction and vacuum to optimize query performance. You can monitor these jobs to understand maintenance activity.

To view maintenance jobs:

1. In the Dremio console, click ![Jobs icon](/images/icons/jobs.png "Jobs icon") in the side navigation bar to open the Jobs page.
2. Select **Internal** job type.
3. Review jobs with engine type **MAINTENANCE**.

## Add Catalogs from Other Projects

In addition to your Open Catalog, you can connect to Open Catalogs from other projects in your organization. When you add a catalog from another project, it appears as a source in your project, enabling you to access shared data assets while maintaining consistent security and governance. All Role-Based Access Control (RBAC) privileges and fine-grained access controls are enforced at the catalog level, ensuring secure data access across projects.

Catalogs from other projects enable:

* **Cross-Project Collaboration** – Access tables from other teams without duplicating data or managing separate copies.
* **Centralized Governance** – Data owners maintain control over access policies while enabling broad data sharing.
* **Consistent Security** – RBAC and fine-grained controls travel with the catalog, so permissions are enforced regardless of which project accesses the data.
* **Simplified Data Discovery** – Users can browse and query shared data assets directly from their own project workspace.

**To add a catalog from another project:**

1. In the Datasets panel, click ![Add Source icon](/images/icons/plus.png "Add Source icon") next to **Sources**.
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Open Catalog**.
3. In the **Name** field, choose the project hosting the desired catalog from the dropdown menu.
4. Click **Save**.

The catalog now appears under **Lakehouse Catalogs** in your Sources panel. You can browse its namespaces and query tables just as you would with your catalog, with all access controls enforced automatically.

You will only see projects in the dropdown where you have been granted access to their Open Catalog. If you do not see a project you expect, contact the project owner to request access.

## Catalog Settings

The default catalog configurations work well for most use cases. If you need to adjust them:

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and choose **Project Settings**.
2. Select **Catalog** to view the catalog settings page.

**For catalogs from other projects:**

1. Select the catalog from the **Lakehouse Catalogs** section of **Sources** on the Datasets panel.
2. Select **Settings** from the dropdown menu.
3. Select from the available tabs for additional configurations.

### Reflection Refresh

Control how often Reflections are automatically refreshed and when they expire. These settings are specific to each project using the catalog.

#### Refresh Settings

* **Never refresh**: Prevent automatic Reflection refresh. By default, Reflections refresh automatically.
* **Refresh every**: Set the refresh interval in hours, days, or weeks. Ignored if **Never refresh** is selected.
* **Set refresh schedule**: Specify a daily or weekly refresh schedule.

#### Expire Settings

* **Never expire**: Prevent Reflections from expiring. By default, Reflections expire after the configured time limit.
* **Expire after**: The time limit after which Reflections are removed from Dremio, specified in hours, days, or weeks. Ignored if **Never expire** is selected.

### Metadata

Configure how Dremio handles dataset definitions and metadata refresh. These settings are specific to each project using the catalog.

In Open Catalog, metadata refresh serves two purposes:

* **Cache Refresh**: Dremio maintains a project-level cache of table metadata to accelerate query planning and execution. Writes from Dremio query engines automatically update this cache. However, writes from other query engines only update snapshot metadata in object storage. Metadata refresh syncs these external changes into Dremio's cache to improve subsequent query performance.
* **Lineage Computation**: Metadata refresh recomputes lineage information to reflect the latest changes in lineage graphs.

#### Dataset Handling

* **Remove dataset definitions if the underlying data is unavailable** (Default) – When selected, Dremio removes dataset definitions if the underlying files are deleted or the folder/source becomes inaccessible. When deselected, Dremio retains dataset definitions even when data is unavailable. This is useful when files are temporarily deleted and replaced with new files.

#### Dataset Discovery

* **Fetch every**: How often to refresh top-level source object names (databases and tables). Set the interval in minutes, hours, days, or weeks. Default: 1 hour.

#### Dataset Details

Metadata Dremio needs for query planning, including field information, types, shards, statistics, and locality.

* **Fetch mode**: Choose to fetch metadata only from queried datasets. Dremio updates details for previously queried objects in the source. Default: **Only Queried Datasets**.
* **Fetch every**: How often to fetch dataset details, specified in minutes, hours, days, or weeks. Default: 1 hour.
* **Expire after**: When dataset details expire, specified in minutes, hours, days, or weeks. Default: 3 hours.

### Privileges

Grant access to specific users or roles. See [Privileges](/dremio-cloud/security/privileges) for additional information about privileges.

**To grant access:**

1. Under **Privileges**, enter the user name or role name you want to grant access to and click **Add to Privileges**. The user or role appears in the **USERS/ROLES** table.
2. In the **USERS/ROLES** table, toggle the checkbox for each privilege you want to grant.
3. Click **Save** after configuring all settings.

## Delete an Open Catalog Connection

To delete a catalog connection from another project:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the Data panel.
2. In the list of data sources, hover over the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm removal.

You cannot delete your default Open Catalog as it is a core component of your project.

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

Was this page helpful?

* Key Capabilities
* Create a Namespace
* Observe Table Maintenance
* Add Catalogs from Other Projects
* Catalog Settings
  + Reflection Refresh
  + Metadata
  + Privileges
* Delete an Open Catalog Connection

<div style="page-break-after: always;"></div>

# Table Formatting | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/object-storage/format

On this page

This topic describes how to query the data from your data lake sources by creating tables.

## Overview

Dremio allows you to query the data from your data lake sources without ingesting or copying it. After configuring your data source, you can format the data in your source as a table so that it can be queried in Dremio using SQL. You can format individual files or a folder of files, which will create one table with the data from the folder. You can query the file or folder without creating a table, but performance may be impacted.

This functionality is currently only supported on object storage sources.

### Supported Table and File Formats

| Format | File Limit |
| --- | --- |
| **Apache Iceberg** | Unlimited |
| **Delta Lake** | Unlimited |
| **Excel** | 10,000 |
| **JSON** | 300,000 |
| **Parquet** | Unlimited |
| **Text (delimited)** | 300,000 |
| **XLS** | 10,000 |

note

Formatting folders that contain a mix of file formats is not supported. All files in a folder must be the same format.

The names of files and folders cannot include the following special characters: `/`, `:`, `[`, or `]`.

## Format a File or Folder as a Table

To format a file or folder as a table:

1. On the Datasets page, navigate to the file or folder that you want to format.
2. To format a file or folder:

   **File**: Hover over the file to format and click on the ![This is the icon that represents the format file action.](/images/cloud/format-data.png "Format file.") button on the far right.

   **Folder**: Hover over the folder to format and click on the ![This is the icon that represents the format folder action.](/images/cloud/format-data.png "Format folder.") button on the far right.
3. In the Dataset Settings dialog, for **Format**, verify that the correct format has been detected.
4. (Optional) For the Parquet format, click the checkbox to enable the **Ignore other file formats** if desired. If you select this option, Dremio ignores all non-Parquet files in the related folder structure, and the promoted table works as if only Parquet files are in the folder structure.
5. (Optional) For Excel, XLS, and Text (delimited) formats, you can configure the following parameters.

   **Excel and XLS format:**

   | Parameter | Description |
   | --- | --- |
   | **Extract Field Names** | Check this box to extract the column names from the first line of the file. |
   | **Expand Merged Cells** | Check this box to expand out cells that have been merged in the Excel sheet. |
   | **Sheet Name** | Specify the sheet name if there are multiple sheets within the file. |

   **Text (delimited) format:**

   | Parameter | Description |
   | --- | --- |
   | **Field Delimiter** | Select the delimiter in your text file - Comma, Tab, Pipe, or Custom. For Custom, enter the characters used for a delimiter in the text box. |
   | **Quote** | Select the character that is used for quotes in your file - Single Quote, Double Quote, Custom. For Custom, enter the characters used for quotes in the text box. |
   | **Comment** | Select the character that is used for comments in your file - Number Sign, Double Slash, Custom. For Custom, enter the characters used for comments in the text box. |
   | **Line Delimiter** | Select the character that is used for a line delimiter in your file - CRLF, LF, Custom. For Custom, enter the characters used for a line delimiter in the text box. |
   | **Escape** | Select the character that is used for to escape in your file - Double Quote, Back Quote, Backslack, Custom. For Custom, enter the characters used to escape in the text box. |
   | **Extract Field Names** | Select this option to extract the column names from the first line of the file. |
   | **Skip First Line** | Select this option to skip the first line of the file. |
   | **Trim Column Names** | Select this option to trim whitespace from the left and right sides of the names of the columns. This option is checked by default. |
6. Click **Save**. The parameter values will be auto-detected but can be altered. When you click **Save**, your table will appear in the Datasets page.

## Partitioned Data

The data in a source dataset might be partitioned into one or more levels of subfolders, one level for each partition column. In such cases, when you format the source dataset as a table, Dremio appends to the table one column per partition. The data type of the appended columns is varchar.

### Examples

![](/images/cloud/partitioned-data.png)

#### Example 1

The source dataset `orders` is partitioned on the column `state`. Each subfolder is named `state=<abbreviation>`, where `<abbreviation>` is the two-letter abbreviation of the name of a US state.

When you format `orders` as a table, all of the columns from the Parquet files, except `state`, are included, and Dremio appends the column `dir0`, which has the data type varchar. The values in that column are `state=AK` for the rows from the file `0.parquet`, `state=AL` for the rows from the file `1.parquet`, `state=AR` for the rows from the file `2.parquet`, and so on.

#### Example 2

The source dataset `orders` is partitioned on the columns `state` and `zipCode`. Each first-level subfolder is named `state=<abbreviation>`, where `<abbreviation>` is the two-letter abbreviation of the name of a US state. Each second-level subfolder is named `zipCode=<zip code>`.

When you format `orders` as a table, all of the columns from the Parquet files, except `state` and `zipCode`, are included, and Dremio appends the columns `dir0` and `dir1`, which both have the data type varchar.

The values in `dir0` are `state=AK` for all rows in which the value in `dir1` is `zipCode=<zip code in AK>`, `state=AL` for all rows in which the value in `dir1` is `zipCode=<zip code in Al>`, and so on.

The values in `dir1` are `zipCode=99502` for the rows from `0.parquet`, `zipCode=99503` for the rows from `1.parquet`, and so on.

## Partition Column Inference

By default, when a source dataset uses Parquet files and the data is partitioned on one or more columns, Dremio behaves as described in Partitioned Data. However, if you select the option **Enable partition column inference** in the advanced options for a data source, you change how Dremio handles partition columns.

In addition to appending a column named `dir<n>` for each partition level and using subfolder names for values in those columns, Dremio detects the name of the partition column, appends a column that uses that name, detects values in the names of subfolders, and uses those values in the appended column.

Appended columns still use the varchar data type.

### Examples

![](/images/cloud/partitioned-data-2.png)

#### Example 1

The source dataset `orders` is partitioned on the column `state`. Each subfolder is named `state=<abbreviation>`, where `<abbreviation>` is the two-letter abbreviation of the name of a US state.

When you format `orders` as a table, all of the columns from the Parquet files are included, and Dremio appends the columns `dir0` and `state`, both of which use the varchar data type.

The values in `dir0` are `state=AK` for the rows from the file `0.parquet`, `state=AL` for the rows from the file `1.parquet`, `state=AR` for the rows from the file `2.parquet`, and so on.

The values in `state` are `AK` for the rows from the file `0.parquet`, `AL` for the rows from the file `1.parquet`, `AR` for the rows from the file `2.parquet`, and so on.

#### Example 2

The source dataset `orders` is partitioned on the columns `state` and `zipCode`. Each first-level subfolder is named `state=<abbreviation>`, where `<abbreviation>` is the two-letter abbreviation of the name of a US state. Each second-level subfolder is named `zipCode=<zip code>`.

When you format `orders` as a table, all of the columns from the Parquet files are included, and Dremio appends the columns `dir0`, `dir1`, `state`, and `zipCode`, all of which use the varchar data type.

The values in `dir0` are `state=AK` for all rows in which the value in `dir1` is `zipCode=<zip code in AK>`, `state=AL` for all rows in which the value in `dir1` is `zipCode=<zip code in Al>`, and so on.

The values in `dir1` are `zipCode=99502` for the rows from `0.parquet`, `zipCode=99503` for the rows from `1.parquet`, and so on.

The values in `state` are `AK` for all rows in which the value in `zipCode` is `<zip code in AK>`, `AL` for all rows in which the value in `zipCode` is `<zip code in Al>`, and so on.

The values in `zipCode` are `99502` for the rows from `0.parquet`, `99503` for the rows from `1.parquet`, and so on.

### Requirements

For the **Enable partition column inference** option to work correctly, ensure that the names of your subfolders meet these requirements:

* Names must be in the format `column_name=<column_value>`. `colum_name=` is a valid input.
* Names must meet Dremio's naming conventions for columns.
* Names must be unique within and across directory levels.
* Names must not be present in data files.
* All Parquet files in the source dataset must be in leaf subfolders.

### How Dremio Handles Existing Tables

If you enable the **Enable partition column inference** option, and already have one or more tables that are based on sources that use Parquet files and that are partitioned, those existing tables remain as they are until you run the `ALTER TABLE` command twice on each. The first time, you run the command to cause Dremio to forget the metadata for the table. The second time, you run the command to cause Dremio to refresh the metadata. The commands are listed in ALTER Commands to Cause Dremio to Forget and to Refresh Metadata on each of those tables.

For example, before you enable the **Enable partition column inference** option, your `orders` table might have these columns:

| orderID | *multiple columns* | dir0 |
| --- | --- | --- |
| 000001 | ... | state=CA |
| 000002 | ... | state=WA |

Suppose that you enable the **Enable partition column inference** option. The columns in the table remain the same. If you want to take advantage of partition column inference, you run these two SQL commands:

SQL commands for partition column inference

```
ALTER TABLE path.to.orders FORGET METADATA  
ALTER TABLE path.to.orders REFRESH METADATA
```

As a result of the second `ALTER TABLE` command, Dremio adds the column `state`:

| orderID | *multiple columns* | dir0 | state |
| --- | --- | --- | --- |
| 000001 | ... | state=CA | CA |
| 000002 | ... | state=WA | WA |

Because Dremio appends the new column, any views that are defined on the table and that use the `dir0` column are still valid. When you define new views, you can use the appended column.

### Enable Partition Column Inference

After you follow the steps in either of these procedures, Dremio uses partition column inference for all source datasets that you format to tables.

To enable partition column inference for a new source:

1. On the Datasets page, click **Add Source** below the list of sources.
2. Select **Advanced Options**.
3. Select **Enable partition column inference**.
4. Specify any other settings that you want for your new data source.
5. Click **Save**.

To enable partition column inference for an existing source:

1. On the Datasets page, click the name of the data source.
2. In the top-right corner of the page, click the gear icon.
3. In the Edit Source dialog, select **Advanced Options**.
4. Select **Enable partition column inference**.
5. Click **Save**.
6. If there are existing tables that are based on datasets in the current data source, run the two ALTER commands described in `ALTER` Commands to Cause Dremio to Forget and to Refresh Metadata on each of those tables.

note

If you change the partitioning schema of a source dataset after enabling partition column inference, metadata refreshes of all tables defined on the source dataset fail. To resolve this problem, run the two `ALTER` commands described here on each of the affected tables.

### `ALTER` Commands to Cause Dremio to Forget and to Refresh Metadata

When you enable partition column inference on a source, you might have one or more existing tables in Dremio that are based on datasets in that source. Also, you might you enable partition column inference on a source and then change the partition schema of a source dataset that is the basis of one or more tables in Dremio.

In both cases, you must run these two `ALTER` commands on each affected table:

SQL ALTER commands to forget and refresh metadata

```
ALTER TABLE <dataset_path> FORGET METADATA  
ALTER TABLE <dataset_path> REFRESH METADATA
```

## Enable Automatic Formatting of Data

You can configure a source to automatically format the data located in the source to tables when a user triggers a query on the data for the first time.

To configure data to be automatically formatted:

1. Click on the **Object Storage** header in the left panel on the **Datasets** page.
2. On the Object storage page, hover over the source for which you want to enable this property. Click the ![This is the icon that represents additional settings.](/images/cloud/more.png "Additional settings.") button on the far right and select **Settings**.
3. In the **Source Settings** dialog, navigate to the **Metadata** tab.
4. In the **Metadata** tab, click the checkbox to **Automatically format files into tables when users issue queries**.
5. Click **Save**.

## Remove Formatting on Data

Removing the formatting on a table will revert the table to the folder or file format that it was originally in. Removing the formatting is not supported for tables in an Open Catalog.

To remove the formatting on data:

1. On the **Datasets** page, locate the table for which you want to remove formatting.
2. Hover over the table for which you want to remove formatting. Click the ![This is the icon that represents additional settings.](/images/cloud/more.png "Additional settings.") button and select **Remove Format**.
3. In the **Remove Format** dialog, confirm that you want to remove formatting for the selected dataset. Any views that have been created from this table will be disconnected from the parent.

## Time Zone Support

Dremio does *not* apply any conversions to the `TIME` or `TIMESTAMP` entry that is in the datasource table. Dremio retrieves the time or timestamp value with the assumption that the time zone is in Coordinated Universal Time (UTC).

### Time Zone Limitation

For JSON files where the time zone for the time or timestamp values are not in UTC time, Dremio assumes and processes the values as in UTC time. For such files, we recommend that you convert these values to the UTC time zone before using in Dremio.

## Related Topics

* [Apache Iceberg](/dremio-cloud/developer/data-formats/iceberg/) – Open table format designed for petabyte-scale analytics.

* [Delta Lake](/dremio-cloud/developer/data-formats/delta-lake/) – Open-source storage framework that brings reliability and performance to data lakes.
* [Parquet](/dremio-cloud/developer/data-formats/parquet/) – Columnar storage format optimized for analytical workloads.

Was this page helpful?

* Overview
  + Supported Table and File Formats
* Format a File or Folder as a Table
* Partitioned Data
  + Examples
* Partition Column Inference
  + Examples
  + Requirements
  + How Dremio Handles Existing Tables
  + Enable Partition Column Inference
  + `ALTER` Commands to Cause Dremio to Forget and to Refresh Metadata
* Enable Automatic Formatting of Data
* Remove Formatting on Data
* Time Zone Support
  + Time Zone Limitation
* Related Topics

<div style="page-break-after: always;"></div>

# Apache Druid | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/apache-druid

On this page

[Apache Druid](https://druid.apache.org/) is a high performance, real-time analytics database that delivers sub-second queries on streaming and batch data at scale and under load.

## Prerequisites

Ensure that that you have the outbound port (27017 is the default port) open in your AWS or Azure security group.

## Configure Apache Druid as a Source

1. In the bottom-left corner of the Datasets page, click **Add Source**.
2. Under **Databases** in the Add Data Source dialog, select **Apache Druid**.

### General

1. In the **Name** field, specify the name by which you want the Druid source to appear in the list of data sources. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, follow these steps:

   1. In the **Host** field, specify the hostname or IP address of the Druid source.
   2. In the **Port** field, specify the port to use. The default port is 8888.
   3. (Optional) Select **Use SSL** to use SSL to secure connections.
3. Under **Authentication**, specify the username and password for Dremio to use when connecting to the Druid source.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### Advanced Options

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |

### Reflection Refresh

On the Reflection Refresh page, set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed.

| Option | Description |
| --- | --- |
| **Never refresh** | Select to prevent automatic Reflection refresh, default is to automatically refresh. |
| **Refresh every** | How often to refresh Reflections, specified in hours, days or weeks. This option is ignored if **Never refresh** is selected. |
| **Never expire** | Select to prevent Reflections from expiring, default is to automatically expire after the time limit below. |
| **Expire after** | The time limit after which Reflections expire and are removed from Dremio, specified in hours, days or weeks. This option is ignored if **Never expire** is selected. |

### Metadata

On the Metadata page, you can configure settings to refresh metadata and handle datasets.

#### Dataset Handling

These are the optional **Dataset Handling** parameters.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

On the Privileges page, you can grant privileges to specific users or roles. See [Privileges](/dremio-cloud/security/privileges/) for additional information about user privileges.

1. (Optional) For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **Users** table.
2. (Optional) For the users or roles in the **Users** table, toggle the green checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Edit a Druid Source

To edit a Druid source:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left. The list of data sources appears to the right.
2. Hover over the name of the Druid source.
3. Click ![The Settings icon](/images/settings-icon.png "The Settings icon") to the right.
4. In the **Source Settings** dialog, you cannot edit the name. Editing other parameters is optional. For parameters and advanced options, see Configuring Apache Druid as a Source.
5. Click **Save**.

## Remove a Druid Source

To remove a Druid source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left. The list of data sources appears to the right.
2. Hover over the name of the Druid source.
3. Click ![The Ellipsis icon](/images/ellipsis-icon.png "The Ellipsis icon") to the right.
4. From the list of actions, click **Remove Source**. Confirm that you want to remove the source.

   warning

   Removing a source causes all downstream views dependent on objects in this source to break.

   note

   Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Predicate Pushdowns

These operations are performed by Druid:

`!=`  
`*`  
`+`  
`-`  
`/`  
`<`  
`<=`  
`<>`  
`=`  
`>`  
`>=`  
abs  
acos  
and  
asin  
atan  
atan2  
avg  
cast  
ceil  
concat  
convert\_timezone  
cos  
cot  
degrees  
floor  
is not null  
is null  
length  
like  
ln  
log  
lower  
lpad  
ltrim  
max  
min  
mod  
not  
or  
power  
radians  
regexp\_like  
replace  
reverse  
round  
rpad  
rtrim  
sign  
sin  
substr  
substring  
sum  
tan  
tanh  
trim  
upper  
`||`

Was this page helpful?

* Prerequisites
* Configure Apache Druid as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Edit a Druid Source
* Remove a Druid Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Amazon S3 | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/object-storage/amazon-s3

On this page

[Amazon S3](https://aws.amazon.com/s3/) is an object storage service from AWS.

## Supported Formats

Dremio can query data stored in S3 in file formats (including delimited, Excel (XLSX), JSON, and Parquet) and table formats (including [Apache Iceberg](/dremio-cloud/developer/data-formats/iceberg/) and [Delta Lake](/dremio-cloud/developer/data-formats/delta-lake/)).

## Add an Amazon S3 Source

To add an S3 source:

1. From the Datasets page, next to Sources, click ![Add Source icon.](/images/icons/plus.png "Add Source icon.").
2. In the Add Data Source dialog, under **Object Storage**, click **Amazon S3**.

### General

To configure an S3 source:

* **Name** – In the Name field, enter a name for the Amazon S3 source. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
* **Authentication** – Provide the role that Dremio will assume to gain access to the source:
  + Create an AWS IAM role in your AWS account that trusts Dremio.
  + Add an S3 Access Policy to your custom role that provides access to your S3 source.
  + Add the **Role ARN** to the source configuration.
* **Public Buckets** – (Optional) Click **Add bucket** and enter the public S3 bucket URL. You can add multiple public S3 buckets. AWS credentials are not necessary if you are accessing only public S3 buckets.
* **Encrypt Connection** – (Optional) To secure the connections between the S3 buckets and Dremio, select the **Encrypt connection** checkbox.

### Advanced Options

Click **Advanced Options** in the left menu sidebar.

* **Apply requester-pays to S3 requests** – The requester (instead of the bucket owner) pays the cost of the S3 request and the data downloaded from the S3 bucket.
* **Enable file status check** – Enabled by default; uncheck the box to disable. Enables Dremio to check if a file exists in the S3 bucket before proceeding to handle errors gracefully. Disable this option when there are no files missing from the S3 bucket or when the file's access permissions have not changed. Disabling this option reduces the amount of communication to the S3 bucket.
* **Root Path** – The root path for the Amazon S3 bucket. The default root path is /.
  + VPC-restricted S3 buckets are not supported.
* **Server-side encryption key ARN** – Add the ARN key created in [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS) if you want to store passwords in AWS KMS. Ensure that the AWS credentials you share with Dremio have access to this ARN key.
* **Default CTAS Format** – Choose the default format for tables you create in Dremio: either Parquet or Iceberg (default).
* **Connection Properties** – Provide custom key-value pairs for the connection relevant to the source. Click **Add Property**. For Name, enter a connection property. For Value, enter the corresponding connection property value.
* **Allowlisted buckets** – Add an approved S3 bucket in the text field. You can add multiple S3 buckets. When using this option to add specific S3 buckets, you will only be able to see those buckets and not all the buckets that may be available in the source. Buckets entered must be valid. Misspelled or nonexistent buckets will not appear in the resulting source.

Under Cache Options:

* **Enable local caching when possible** – Selected by default, along with asynchronous access for cloud caching. Uncheck the checkbox to disable this option.
* **Max percent of total available cache space to use when possible** – Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage.

### Reflection Refresh

Click **Reflection Refresh** in the left menu sidebar. This section allows you to manage how often reflections are refreshed and how long data can be served before expiration. To learn more about reflections, refer to [Manual Reflections](/dremio-cloud/admin/performance/manual-reflections). All settings are optional.

You can set the following refresh policies for reflections:

* **Refresh period** – Manage the refresh period by either enabling the option to never refresh or setting a refresh frequency in hours, days, or weeks. The default frequency to refresh reflections is every hour.
* **Expiration period** – Set the expiration period for the length of time that data can be served by either enabling the option to never expire or setting an expiration time in hours, days, or weeks. The default expiration time is three hours.

### Metadata

Click **Metadata** in the left menu sidebar. This section allows you to configure settings to refresh metadata and enable other dataset options.

You can configure Dataset Handling and Metadata Refresh parameters.

#### Dataset Handling

Select from the following options. All settings are optional.

* **Remove dataset definitions if underlying data is unavailable** – By default, Dremio removes dataset definitions if underlying data is unavailable. This option is for scenarios when files are temporarily deleted and added back in the same location with new sets of files.
* **Automatically format files into tables when users issue queries** – Enable this option to allow Dremio to automatically format files into tables when you run queries. This option is for scenarios when the data contains CSV files with non-default options.

#### Metadata Refresh

The **Metadata Refresh** parameters include **Dataset Discovery** and **Dataset Details**.

* **Dataset Discovery** – The refresh interval for fetching top-level source object names such as databases and tables. Use this parameter to set the time interval. You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is one hour.
* **Dataset Details** – The metadata that Dremio needs for query planning, such as information required for fields, types, shards, statistics, and locality. The following describes the parameters that fetch the dataset information.
  + **Fetch mode** – You can choose to fetch only from queried datasets, which is set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated.
  + **Fetch every** – You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is one hour.
  + **Expire after** – You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is three hours.

### Privileges

Click **Privileges** in the left menu sidebar. This section allows you to grant privileges to specific users or roles. To learn more about how Dremio allows for the implementation of granular-level privileges, see [Privileges](/dremio-cloud/security/privileges/). All settings are optional.

To add a privilege for a user or role:

1. In the Add User/Role field, enter the user or role name to which you want to apply privileges.
2. Click **Add to Privileges**. The user or role is added to the Users table.

To set privileges for a user or role:

1. In the Users table, identify the user for which you want to set privileges and click under the appropriate column (Select, Alter, Create Table, etc.) to either enable or disable that privilege. A green checkmark indicates that the privilege is enabled.
2. Click **Save**.

## Edit an Amazon S3 Source

To edit an S3 source:

1. From the Datasets page, right-click on the source to edit and select **Settings**.
2. In the Edit Source dialog box, make changes as needed. For information about the settings in each category, see Add an Amazon S3 Source.
3. Click **Save**.

## Remove an Amazon S3 Source

To remove an S3 source:

1. From the Datasets page, right-click on the source to be removed and select **Delete**.
2. Confirm that you want to remove the source.

## Create an AWS IAM Role

To create an AWS IAM role that provides Dremio with access to your source:

1. Sign in to the [AWS Identity and Access Management (IAM) console](https://console.aws.amazon.com/iamv2/home).
2. From the left menu pane, under Access management, select **Roles**.
3. On the Roles page, click **Create role**.
4. On the Select trusted entity page:

   * Under **Trusted entity type**, select the radio button for **Custom Trust Policy**.
   * Delete the current JSON policy and paste in the custom trust policy template:

     Custom Trust Policy Template

     ```
     {  
       "Version": "2012-10-17",  
       "Statement": [  
         {  
           "Sid": "AllowAssumeRoleWithExternalId",  
           "Effect": "Allow",  
           "Principal": {  
             "AWS": "arn:aws:iam::<dremio_trust_account>:root"  
           },  
           "Action": "sts:AssumeRole",  
           "Condition": {  
             "StringEquals": {  
               "sts:ExternalId": "<project_id>"  
             }  
           }  
         },  
         {  
           "Sid": "AllowTagSessionFromCallerRole",  
           "Effect": "Allow",  
           "Principal": {  
             "AWS": "arn:aws:iam::<dremio_trust_account>:root"  
           },  
           "Action": "sts:TagSession"  
         }  
       ]  
     }
     ```
   * Replace `<dremio_trust_account>` with your [Dremio Trust Account ID](/dremio-cloud/admin/projects/your-own-project-storage#define-the-trust-relationship).
   * Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Project settings** to copy your Project ID. Replace `<project_id>` with your Project ID.
5. Click **Next** to go to the Add permissions page. No edits are needed on this page.
6. Click **Next** to go to the Name, review, and create page.
7. In the **Role details** section, in the Role name field, enter a name for this role.
8. Click **Create role**.

## Add an S3 Access Policy to a Custom Role

To add the required S3 access policy to your custom role:

1. On the Roles page, click the role name. Use the **Search** field to locate the role if needed.
2. From the Roles page, in the Permissions section, click **Add permissions** > **Create inline policy**.
3. On the Create policy page, click the **JSON** tab.
4. Delete the current JSON policy and copy the [IAM Policy Template for S3](/dremio-cloud/admin/projects/your-own-project-storage#create-your-iam-role). Replace `<bucket-name>` with the name of your S3 bucket.
5. Click **Next**.
6. On the Review policy page, in the Name field, enter a name for the policy.
7. Click **Create policy**. The policy is created and you are returned to the Roles page.

Was this page helpful?

* Supported Formats
* Add an Amazon S3 Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Edit an Amazon S3 Source
* Remove an Amazon S3 Source
* Create an AWS IAM Role
* Add an S3 Access Policy to a Custom Role

<div style="page-break-after: always;"></div>

# Data Type Mapping

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/amazon-redshift

On this page

[Amazon Redshift](https://aws.amazon.com/redshift/) is a cloud data-warehouse service.

There are two different types of connection that you can make to a Redshift cluster that you add as a source:

* A secure connection to a publicly accessible Redshift cluster
* A secure connection to a private Redshift cluster

## Create a Secure Connection to a Publicly Accessible Amazon Redshift Cluster

When Dremio runs queries against the Redshift cluster, the compute engines in your VPC and the cluster communicate through a connection that consists of a NAT gateway and internet gateway in the VPC used with Dremio, the internet, and the internet gateway in the VPC used for Redshift.

![](/assets/images/aws-redshift-1-510645224a9161e8fb65f55ca09eff7a.png)

### Prerequisites for the VPC that You Are Using for Your Dremio project

* Ensure that the compute engines are deployed in a private subnet.
* Ensure that a NAT gateway configured in a public subnet.
* Ensure that an internet gateway is attached to the VPC.

### Prerequisites for the VPC that You Are Using for Amazon Redshift

* Ensure that the Redshift cluster is in a public subnet.
* Ensure that you know the IP address of the NAT gateway that is in the VPC that you are using for Dremio.

### Steps to Follow in Amazon Redshift

1. In the **Clusters** table, click the name of the Redshift cluster that you plan to use. The UI console for the cluster opens.
2. Make the cluster publicly accessible:
   1. Click **Actions** in the upper-right corner of the console.
   2. Select **Modify publicly accessible setting**.
   3. In the **Edit publicly accessible** dialog, select the check box **Turn on Publicly accessible**, and select the Elastic IP address to use for connections to the cluster.
3. Create an inbound rule for the IP address of the NAT gateway that is in the VPC being used with Dremio:
   1. In the UI console for the cluster, scroll down to the **Network and security settings** section.
   2. Click the name of the VPC security group. The UI console for the security group opens.
   3. In the **Inbound rules** section, click **Edit Inbound Rules**.
   4. On the Edit inbound rules page, click **Add rule**.
   5. In the **Type** field, select **Redshift**.
   6. Specify the IP address for the NAT gateway in the field to the right of the **Source** field.
   7. Click **Save rules**.

## Create a Secure Connection to a Private Amazon Redshift Cluster

When Dremio runs queries against the Redshift cluster, the compute engines in your VPC and the cluster communicate through a VPC peering connection.

![](/assets/images/aws-redshift-2-e37b3707455bf52bf327a6a3ffd0ce91.png)

### Prerequisite for the VPC that You Are Using for Your Dremio project

Ensure that the compute engines are deployed in a private subnet.

### Prerequisite for the VPC that You Are Using for Amazon Redshift

Ensure that the Redshift cluster is in a private subnet.

### Steps in AWS

1. Create a [VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html) between the two VPCs.
2. Add the Redshift cluster VPC's CIDR block as a destination in the route tables of the VPC that you are using for Dremio:
   1. In the left navigation bar of the VPC console, click **Your VPCs**.
   2. Select the VPC that you are using for Dremio.
   3. In the **Details** section, copy the VPC ID and copy the IPv4 CIDR.
   4. In the left navigation bar, click **Route tables**.
   5. In the search field at the top of the Route tables page, paste the VPC ID.
   6. Select the route table.
   7. In the **Routes** section, click **Edit routes**.
   8. On the Edit routes page, click **Add route**.
   9. In the **Destination** field, paste the IPv4 CIDR that you copied in step 3.
   10. In the **Target** field, specify your VPC peering connection.
   11. Click **Save changes**.
3. Add the Dremio VPC's CIDR block as a destination in the route tables of the Redshift cluster's VPC:
   1. In the left navigation bar of the VPC console, click **Your VPCs**.
   2. Select the VPC that you are using for Redshift.
   3. In the **Details** section, copy the VPC ID and copy the IPv4 CIDR.
   4. In the left navigation bar, click **Route tables**.
   5. In the search field at the top of the Route tables page, paste the VPC ID.
   6. Select the route table.
   7. In the **Routes** section, click **Edit routes**.
   8. On the Edit routes page, click **Add route**.
   9. In the **Destination** field, paste the IPv4 CIDR.
   10. In the **Target** field, specify your VPC peering connection.
   11. Click **Save changes**.
4. In the security group for the Redshift cluster, create an inbound rule for the CIDR block of the VPC that you are using for Dremio:
   1. In the left navigation bar of the VPC console, click **Your VPCs**.
   2. Select the VPC that you are using for Dremio.
   3. In the **Details** section, copy the IPv4 CIDR.
   4. Open the Redshift console.
   5. Select your Redshift cluster. The UI console for the cluster opens.
   6. Under **Properties**, scroll down to the **Network and security settings** section.
   7. Click the name of the VPC security group. The UI console for the security group opens.
   8. In the **Inbound rules** section, click **Edit Inbound Rules**.
   9. On the Edit inbound rules console, click **Add rule**.
   10. In the **Type** field, select **Redshift**.
   11. In the **Port range** field, specify `5439`.
   12. Paste the IPv4 CIDR for the Dremio VPC into the field to the right of the **Source** field.
   13. Click **Save rules**.
5. In the security group for the Dremio VPC cluster, create an inbound rule for the CIDR block of the VPC that you are using for the Redshift cluster:
   1. In the left navigation bar of the VPC console, click **Your VPCs**.
   2. Select the VPC that you are using for the Redshift cluster.
   3. In the **Details** section, copy the IPv4 CIDR.
   4. In the left navigation bar of the VPC console, click **Security groups**.
   5. For each security group that you are using for Dremio:
   6. Click the name of the VPC security group. The UI console for the security group opens.
   7. In the **Inbound rules** section, click **Edit Inbound Rules**.
   8. On the Edit inbound rules console, click **Add rule**.
   9. In the **Type** field, select **Redshift**.
   10. In the **Port range** field, specify `5439`.
   11. Paste the IPv4 CIDR for the Redshift cluster VPC into the field to the right of the **Source** field.
   12. Click **Save rules**.

## Add an Amazon Redshift Cluster as a Data Source

After you create a connection between the VPC that you are using with Dremio and the VPC that hosts your Redshift cluster, you can add the cluster as a data source.

### Prerequisites

Ensure that you have the JDBC connection string of the Redshift database to add it as a source. You can find the JDBC connection URL in the AWS console.

### Steps

Perform these steps to configure Redshift:

1. On the Datasets page, you can see a truncated list of **Sources** at the bottom-left of the page. Click **Add Source**.

   Alternatively, click **Databases**. The page displays all database sources. Click the **Add database** button at the top-right of that page.
2. In the **Add Data Source** dialog, click **Amazon Redshift**.

   The following section describes the source configuration tabs.

#### General

The **General** tab contains the required fields to create a Redshift source.

![](/assets/images/redshift-general-6319e201383d638e537949351fc4dd82.png)

Perform these steps in the **General** tab:

1. In the **General** tab, for **Name**, enter a name. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. For **JDBC Connection String**, enter the JDBC connection string of the Redshift database.
3. For **Authentication**, you must choose one of the following authentication options:

   * **Master Authentication**, this is the default option. Provide the username and password of a master database user with permissions to read required objects:

     + For **Username**, enter your Redshift database username.
     + For **Password**, enter your Redshift database password.
   * **Secret Resource Url**:

     + For **Username**, enter your Redshift database username.
     + For **Secret Resource Url**, enter the Secret Resource URL that allows Dremio to fetch the password from [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). The Secret Resource URL is the Amazon Resource Name (ARN) for the secret (for example, `arn:aws:secretsmanager:us-west-2:123456789012:secret:my-rds-secret-VNenFy`).

#### Advanced Options

Click **Advanced Options** in the sidebar.

![](/assets/images/redshift-adv-options-ef5f219cf59fafbc5d2ab6ae42b999a8.png)

note

All advanced options are optional.

| Advanced Option | Description |
| --- | --- |
| **Record fetch size** | Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default record fetch size is 200. |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Connection Properties** | Custom key value pairs for the connection relevant to the source. To add a connection property, click **Add property** and add the property name and value. |

#### Reflection Refresh

The **Reflection Refresh** tab in the sidebar allows you to set time intervals for Reflections to refresh or expire.

![](/assets/images/redshift-reflection-refresh-a6c4875383f12d719c33f8e223326970.png)

#### Metadata

You can configure settings to refresh metadata and handle datasets. Click **Metadata** in the sidebar.

![](/assets/images/redshift-metadata-ee5821704a1a98b7c062dd1fde70a1dc.png)

You can configure Dataset Handling and Metadata Refresh parameters.

###### Dataset Handling

These are the **Dataset Handling** parameters.

note

All **Dataset Handling** parameters are optional.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

###### Metadata Refresh

These are the **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  note

  All **Dataset Details** parameters are optional.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

#### Privileges

You can grant privileges to specific users or roles.

![](/assets/images/redshift-privileges-6d1d17028cc37f471ed2a0438d561ccc.png)

1. (Optional) For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **Users** table.
2. (Optional) For the users or roles in the **Users** table, toggle the green checkmark for each privilege you want to grant to the Redshift source that is being created.

Click **Save** after setting the configuration.

note

Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### Edit Information About an Amazon Redshift Cluster Used as a Data Source

To edit a Redshift source:

1. On the Datasets page, click **Databases**. A list of databases is displayed.
2. Hover over the database and click the Settings ![This is the icon that represents the Database settings.](/images/icons/settings.png "Icon represents the Database settings.") icon that appears next to the database.
3. In the Source Settings dialog, you cannot edit the name. Editing other parameters is optional.
4. Click **Save**.

## Remove an Amazon Redshift Cluster Used as a Data Source

To remove a Redshift source, perform these steps:

1. On the Datasets page, click **Databases**. A list of sources is displayed.
2. Hover over the database and click the More (...) icon that appears next to the database.
3. From the list of actions, click **Remove Source**. Confirm that you want to remove the source.

   caution

   Removing a source causes all downstream views dependent on objects in this source to break.

   note

   Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Predicate Pushdowns

Dremio offloads these operations to Redshift.

`-*`, `+`, `-`, `/`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
`AND`, `NOT`, `OR`, `||`  
`ABS`  
`ACOS`  
`ADD_MONTHS`  
`ASIN`  
`ATAN`  
`ATAN2`  
`AVG`  
`CAST`  
`CBRT`  
`CEIL`  
`CEILING`  
`CHAR_LENGTH`  
`CHARACTER_LENGTH`  
`CONCAT`  
`COS`  
`COT`  
`DATE_ADD`  
`DATE_SUB`  
`DATE_TRUNC_CENTURY`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_DECADE`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_QUARTER`  
`DATE_TRUNC_SECOND`  
`DATE_TRUNC_WEEK`  
`DATE_TRUNC_YEAR`  
`DEGREES`  
`E`  
`EXP`  
`EXTRACT_CENTURY`  
`EXTRACT_DAY`  
`EXTRACT_DECADE`  
`EXTRACT_DOW`  
`EXTRACT_DOY`  
`EXTRACT_EPOCH`  
`EXTRACT_HOUR`  
`EXTRACT_MILLENNIUM`  
`EXTRACT_MINUTE`  
`EXTRACT_MONTH`  
`EXTRACT_QUARTER`  
`EXTRACT_SECOND`  
`EXTRACT_WEEK`  
`EXTRACT_YEAR`  
`FLOOR`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LCASE`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LN`  
`LOCATE`  
`LOG`  
`LOG10`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MEDIAN`  
`MIN`  
`MOD`  
`PERCENT_CONT`  
`PERCENT_DISC`  
`PI`  
`POSITION`  
`POW`  
`POWER`  
`RADIANS`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SIN`  
`SQRT`  
`STDDEV`  
`STDDEV_POP`  
`STDDEV_SAMP`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TAN`  
`TIMESTAMPADD_DAY`  
`TIMESTAMPADD_HOUR`  
`TIMESTAMPADD_MINUTE`  
`TIMESTAMPADD_MONTH`  
`TIMESTAMPADD_QUARTER`  
`TIMESTAMPADD_SECOND`  
`TIMESTAMPADD_WEEK`  
`TIMESTAMPADD_YEAR`  
`TIMESTAMPDIFF_DAY`  
`TIMESTAMPDIFF_HOUR`  
`TIMESTAMPDIFF_MINUTE`  
`TIMESTAMPDIFF_MONTH`  
`TIMESTAMPDIFF_QUARTER`  
`TIMESTAMPDIFF_SECOND`  
`TIMESTAMPDIFF_WEEK`  
`TIMESTAMPDIFF_YEAR`  
`TO_CHAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UCASE`  
`UPPER`  
`VAR_POP`  
`VAR_SAMP`

# Data Type Mapping

Dremio supports Amazon Redshift data types, as shown in the following table which provides the mappings from Amazon Redshift to Dremio data types. If there are additional Redshift types not listed in the table, then those types are not supported in Dremio.

| Amazon Redshift Data Type | Dremio Type |
| --- | --- |
| BIT | BOOLEAN |
| BOOL | BOOLEAN |
| BOOLEAN | BOOLEAN |
| BPCHAR | VARCHAR |
| BYTEA | VARBINARY |
| CHAR | VARCHAR |
| CHARACTER VARYING | VARCHAR |
| DATE | DATE |
| FLOAT4 | FLOAT |
| FLOAT8 | DOUBLE |
| INT | INTEGER |
| INT2 | INTEGER |
| INT4 | INTEGER |
| INT8 | BIGINT |
| INTEGER | INTEGER |
| NCHAR | VARCHAR |
| NUMERIC | DECIMAL |
| NVARCHAR | VARCHAR |
| TEXT | VARCHAR |
| TIMESTAMP WITH TIMEZONE | TIMESTAMP |
| TIMESTAMP WITHOUT TIMEZONE | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| TIMESTAMPTZ | TIMESTAMP |
| TINYINT | INTEGER |
| VARBINARY | VARBINARY |
| VARCHAR | VARCHAR |

Was this page helpful?

* Create a Secure Connection to a Publicly Accessible Amazon Redshift Cluster
  + Prerequisites for the VPC that You Are Using for Your Dremio project
  + Prerequisites for the VPC that You Are Using for Amazon Redshift
  + Steps to Follow in Amazon Redshift
* Create a Secure Connection to a Private Amazon Redshift Cluster
  + Prerequisite for the VPC that You Are Using for Your Dremio project
  + Prerequisite for the VPC that You Are Using for Amazon Redshift
  + Steps in AWS
* Add an Amazon Redshift Cluster as a Data Source
  + Prerequisites
  + Steps
  + Edit Information About an Amazon Redshift Cluster Used as a Data Source
* Remove an Amazon Redshift Cluster Used as a Data Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Google BigQuery | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/google-bigquery

On this page

Dremio supports connecting to Google BigQuery as an external source. The connector uses Google Service Account Keys as the authentication method. To know more about creating service account keys, see [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete).

## Configure Google BigQuery as a Source

1. In the bottom-left corner of the Datasets page, click **Add Source**.
2. Under **Databases** in the Add Data Source dialog, select **Google BigQuery**.

### General

1. In the **Name** field, specify the name by which you want the Google BigQuery source to appear in the list of data sources. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, follow these steps:

   1. In the **Host** field, specify the URL for the Google BigQuery source.
   2. In the **Port** field, specify the port to use. The default port is `443`.
   3. In the **Project Id** field, specifiy the Google Cloud Project ID.
3. Under **Authentication**, specify the service account **Client Email** and the **Service Account Key** (JSON).

   note

   This connector assumes that the **Service Account Key** is a JSON Web Key. For more information on Google Cloud service account credentials, please see [Service account credentials](https://cloud.google.com/iam/docs/service-account-creds).

### Advanced Options

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Record fetch size** | Number of records to fetch at once. Set to `0` (zero) to have Dremio automatically decide. By default, this is set to `200`. |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default number of maximum idle connections is `8`. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is `6` seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. Set the Query timneout to 0 for no timeout. The default Query timeout is `0`. |

### Reflection Refresh

On the Reflection Refresh page, set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed.

| Option | Description |
| --- | --- |
| **Never refresh** | Select to prevent automatic Reflection refresh, otherwise, the default is to refresh automatically. |
| **Refresh every** | How often to refresh Reflections, specified in hours, days or weeks. This option is ignored if **Never refresh** is selected. |
| **Set refresh schedule** | Specify the daily or weekly schedule. |
| **Never expire** | Select to prevent Reflections from expiring, otherwise, the default is to expire automatically after the time limit specified in **Expire after**. |
| **Expire after** | The time limit after which Reflections expire and are removed from Dremio, specified in hours, days or weeks. This option is ignored if **Never expire** is selected. |

### Metadata

On the Metadata page, you can configure settings to refresh metadata and handle datasets.

#### Dataset Handling

These are the optional **Dataset Handling** parameters.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is `1` hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is `3` hours. |

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Control](/dremio-cloud/security/privileges/) for additional information about privileges.

note

All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update a Google BigQuery Source

To update a Google BigQuery source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configure Google BigQuery as a Source.
4. Click **Save**.

## Delete a Google BigQuery Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Google BigQuery source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and click ![The Settings icon](/images/settings-icon.png "The Settings icon") to the right.
3. From the dropdown, select **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

   caution

   Deleting a source causes all downstream views that depend on objects in the source to break.

   note

   Sources containing a large number of files or tables may take longer to be deleted. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being deleted. Once complete, the source disappears.

## Predicate Pushdowns

Dremio pushes the following operations to Google BigQuery.

`*`, `+`, `-`, `/`, `%`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
`AND`, `NOT`, `OR`, `||`  
`ABS`  
`ACOS`  
`ADD_MONTHS`  
`ASIN`  
`ATAN`  
`ATAN2`  
`AVG`  
`CAST`  
`CEIL`  
`CEILING`  
`CHAR_LENGTH`  
`CHARACTER_LENGTH`  
`CONCAT`  
`COS`  
`COT`  
`DATE_ADD`  
`DATE_SUB`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_YEAR`  
`DEGREES`  
`E`  
`EXP`  
`EXTRACT_DAY`  
`EXTRACT_DOW`  
`EXTRACT_DOY`  
`EXTRACT_HOUR`  
`EXTRACT_MINUTE`  
`EXTRACT_MONTH`  
`EXTRACT_QUARTER`  
`EXTRACT_SECOND`  
`EXTRACT_WEEK`  
`EXTRACT_YEAR`  
`FLOOR`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LCASE`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LN`  
`LOCATE`  
`LOG`  
`LOG10`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MEDIAN`  
`MIN`  
`MOD`  
`MONTH`  
`PERCENT_CONT`  
`PERCENT_DISC`  
`PI`  
`POSITION`  
`POW`  
`POWER`  
`RADIANS`  
`RAND`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SIN`  
`SQRT`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TAN`  
`TIMESTAMPADD_DAY`  
`TIMESTAMPADD_HOUR`  
`TIMESTAMPADD_MINUTE`  
`TIMESTAMPADD_MONTH`  
`TIMESTAMPADD_QUARTER`  
`TIMESTAMPADD_SECOND`  
`TIMESTAMPADD_YEAR`  
`TIMESTAMPDIFF_DAY`  
`TIMESTAMPDIFF_HOUR`  
`TIMESTAMPDIFF_MINUTE`  
`TIMESTAMPDIFF_MONTH`  
`TIMESTAMPDIFF_QUARTER`  
`TIMESTAMPDIFF_SECOND`  
`TIMESTAMPDIFF_WEEK`  
`TIMESTAMPDIFF_YEAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UCASE`  
`UPPER`  
`YEAR`

Was this page helpful?

* Configure Google BigQuery as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update a Google BigQuery Source
* Delete a Google BigQuery Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Azure Storage | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/object-storage/azure-storage

On this page

The Dremio source connector for Azure Storage includes support for the following Azure Storage services:

* **Azure Blob Storage** is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data, such as text or binary data.
* **Azure Data Lake Storage Gen2** is a set of capabilities dedicated to big data analytics, built on top of Azure Blob storage. Features, such as file system semantics, directory, and file-level security and scale are combined with the low-cost, tiered storage, and high availability/disaster recovery capabilities of Azure Blob storage.

note

Soft delete for blobs is not supported for Azure Storage accounts. Soft delete should be disabled to establish a successful connection.

Zero-byte files created with Iceberg tables in Azure Storage can be safely ignored—they don't impact Dremio's functionality. To prevent these files from being created, enable **Hierarchical Namespace** on your storage container. See [Azure Data Lake Storage Gen2 hierarchical namespace](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-namespace) for instructions.

## Grant Permissions

In order to use Azure Storage as a data source, the OAuth 2.0 application that you created in Azure must have appropriate permissions within the specified Azure Storage account.

To grant these permissions, you can use the built-in **Storage Blob Data Contributor** role by [assigning roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) for your storage account:

1. In [Step 3: Select the appropriate role](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal#step-3-select-the-appropriate-role), assign the **Storage Blob Data Contributor** role.
2. In [Step 4: Select who needs access](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal#step-4-select-who-needs-access), for **Assign access to**, select **User, group or service principal**. For **Select Members**, select the name of the application/service principal that you previously registered.

## Add an Azure Storage Source

To add an Azure Storage source to your project:

1. From the Datasets page, click **Object Storage** at the bottom of the Sources pane.
2. From the top-right of the page, click **Add object storage**.
3. In the Add Data Source dialog, under Object Storage, click **Azure Storage**.

   The New Azure Storage Source dialog box appears, which contains the following sections: General, Advanced Options, Reflection Refresh, Metadata, Privileges.

Refer to the following for guidance on how to complete each section.

### General

| Section | Field/Option | Description |
| --- | --- | --- |
| Name | Name | Provide a name to use for this Azure Storage source. The name cannot include the following special characters: `/`, `:`, `[`, or `]`. |
| Connection | Account Name | The name of the Azure Storage account from the Azure portal app. |
| Encrypt connection | Enabled by default, this option encrypts network traffic with TLS. Dremio recommends encrypted connections. |
| Storage Connection Protocol (Driver) | Select the Azure Storage driver connection protocol you would like to use. The options are `WASBS (Legacy)` and `ABFSS (Recommended)`. ABFSS is the default based on Azure best practices. |
| Authentication | Shared access key | Select this option to authenticate using the Shared Access Key from the Azure portal App. |
| Microsoft Entra ID | Select this option to use Microsoft Entra ID credentials for authentication. |

#### Microsoft Entra ID Authentication

To configure the Azure Storage source to use Microsoft Entra ID for authentication, provide the following values from the OAuth 2.0 application that you created in the Azure portal for this source:

* Application ID - The application (client) ID in Azure.
* OAuth 2.0 Token Endpoint - The OAuth 2.0 token endpoint (v1.0), which includes the tenant ID and is used by the application in order to get an access token or a refresh token.
* Application Secret - The secret key generated for the application.

### Advanced Options

Advanced Options include:

* **Enable partition column inference** – If a source dataset uses Parquet files and the data is partitioned on one or more columns, enabling this option will append a column named `dir<n>` for each partition level and use subfolder names for values in those columns. Dremio detects the name of the partition column, appends a column that uses that name, detects values in the names of subfolders, and uses those values in the appended column.
* **Root Path** – The root path for the Azure Storage location. The default root path is /.
* **Default CTAS Format** – Choose the default format for tables you create in Dremio, either Iceberg or Parquet.
* **Advanced Properties** – Provide the custom key value pairs for the connection relevant to the source.
  + Click **Add Property**.
  + For Name, enter a connection property.
  + For Value, enter the corresponding connection property value.
* **Blob Containers & Filesystem Allowlist** – Add an approved Azure Storage account in the text field. You can add multiple accounts this way. When using this option to add specific accounts, you will only be able to see those accounts and not all accounts that may be available in the source.

Under Cache Options, review the following table and edit the options to meet your needs.

* **Enable local caching when possible** – Selected by default, along with asynchronous access for cloud caching. Uncheck the checkbox to disable this option. For more information about local caching, see the note below this table.
* **Max percent of total available cache space to use when possible** – Specifies the disk quota, as a percentage, that a source can use on any single node only when local caching is enabled. The default is 100 percent of the total disk space available. You can either manually enter in a percentage in the value field or use the arrows to the far right to adjust the percentage.

Columnar Cloud Cache (C3) enables Dremio to achieve NVMe-level I/O performance on S3/ADLS by leveraging the NVMe/SSD built into cloud compute instances. C3 caches only the data required to satisfy your workloads and can even cache individual microblocks within datasets. If your table has 1,000 columns and you only query a subset of those columns and filter for data within a certain timeframe, C3 will cache only that portion of your table. By selectively caching data, C3 eliminates over 90% of S3/ADLS I/O costs, which can make up 10-15% of the costs for each query you run.

### Reflection Refresh

These settings define how often Reflections are refreshed and how long data can be served before expiration. To learn more about Reflections, refer to [Optimize Performance](/dremio-cloud/admin/performance/manual-reflections). All Reflection parameters are optional.

You can set the following refresh policies for Reflections:

* **Refresh period** – Manage the refresh period by either enabling the option to never refresh or setting a refresh frequency in hours, days, or weeks. The default frequency to refresh Reflections is every hour.
* **Expiration period** – Set the expiration period for the length of time that data can be served by either enabling the option to never expire or setting an expiration time in hours, days, or weeks. The default expiration time is set to three hours.

### Metadata

Metadata settings include Dataset Handling options and Metadata Refresh options.

#### Dataset Handling

You can review each option provided in the following table to set up the dataset handling options to meet your needs.

* **Remove dataset definitions if underlying data is unavailable** (Default) – When selected, datasets are automatically removed if their underlying files/folders are removed from Azure Storage or if the folder or source are not accessible. If this option is *not* selected, Dremio will not remove dataset definitions if underlying files/folder are removed from Azure Storage. This may be useful if files are temporarily deleted and replaced with a new set of files.
* **Automatically format files into physical datasets when you issue queries** – When selected, Dremio will automatically promote a folder to a table using default options. If you have CSV files, especially with non-default formatting, it might be useful to *not* select this option.

#### Metadata Refresh

The **Metadata Refresh** parameters include **Dataset Details**, which is the metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. All metadata parameters are optional. The following table describes the parameters that fetch the dataset information.

* **Fetch mode** – You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated.
* **Fetch every** – You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is one day.
* **Expire after** – You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is three days.

### Privileges

This section lets you grant privileges on the source to specific users or roles. All privilege parameters are optional. To learn more about how Dremio allows for the implementation of granular-level privileges, see [Privileges](/dremio-cloud/security/privileges).

To add a privilege for a user or to a role:

1. In the **Add User/Role** field, enter the user or role to which you want to apply privileges.
2. Click **Add to Privileges**. The user or role is added to the Users table.

To set privileges for a user or role:

1. In the Users table, identify the user to set privileges for and click under the appropriate column (Select, Alter, Create Table, etc.) to either enable or disable that privilege. A green checkmark indicates that the privilege is enabled.
2. Click **Save**.

Was this page helpful?

* Grant Permissions
* Add an Azure Storage Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges

<div style="page-break-after: always;"></div>

# Iceberg REST Catalog | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/catalogs/iceberg-rest-catalog

On this page

Dremio connects to any catalog supporting the Iceberg REST Catalog specification. See Supported Configurations below for ready-to-use configurations for many popular catalogs, including:

* [Apache Polaris](https://polaris.apache.org/)
* [Project Nessie](https://projectnessie.org/)
* [AWS Glue](https://aws.amazon.com/glue/)
* [S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html)
* [Confluent Tableflow](https://docs.confluent.io/cloud/current/topics/tableflow/overview.html)
* [Microsoft OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview)

In addition, Dremio provides specific connectors for:

* [Snowflake Open Catalog](/dremio-cloud/bring-data/connect/catalogs/snowflake-open-catalog)
* [Databricks Unity Catalog](/dremio-cloud/bring-data/connect/catalogs/databricks-unity-catalog)

## Configure an Iceberg REST Catalog Source

To add an Iceberg REST Catalog source:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "Add Source icon").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Iceberg REST Catalog Source**.

### General

To configure the source connection:

1. For **Name**, enter a name for the source. The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore (\_), or hyphen (-).
2. For **Endpoint URI**, specify the catalog service URI.
3. By default, **Use vended credentials** is turned on. This allows Dremio to connect to the catalog and receive temporary credentials for the underlying storage location. When this setting is enabled, you do not need to add storage authentication in **Advanced Options**. If you experience errors using vended credentials, turn the setting off and provide credentials via **Advanced Options** to establish a connection.
4. (Optional) For **Allowed Namespaces**, add each namespace and check the option if you want to include their entire subtrees. Tables are organized into namespaces, which can be at the top level or nested within one another. Namespace names cannot contain periods or spaces.

### Advanced Options

**Storage Authentication**

If you disabled vended credentials in the General tab, you must manually provide storage authentication.

Dremio supports Amazon S3 and Azure Storage as object storage services. For acceptable storage authentication configurations, see the following catalog properties and credentials for each service option.

* S3 Access Key
* S3 Assumed Role
* Azure Shared Key

* `fs.s3a.aws.credentials.provider` (property)

  + Value: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
  + Description: Required field for an Iceberg REST Catalog source
* `fs.s3a.access.key` (credential)

  + Value: `<your_access_key>`
  + Description: AWS access key ID used by the S3A file system. Omit for IAM role-based or provider-based authentication.
* `fs.s3a.secret.key` (credential)

  + Value: `<your_secret_key>`
  + Description: AWS secret access key used by the S3A file system. Omit for IAM role-based or provider-based authentication.

* `fs.s3a.assumed.role.arn` (property)

  + Value: `arn:aws:iam::*******:role/OrganizationAccountAccessRole`
  + Description: AWS ARN for the role to be assumed
* `fs.s3a.aws.credentials.provider` (property)

  + Value: `com.dremio.plugins.s3.store.STSCredentialProviderV1`
  + Description: Required field for an Iceberg REST Catalog source
* `fs.s3a.assumed.role.credentials.provider` (property)

  + Value: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
  + Description: Use only if the credential provider is `AssumedRoleCredentialProvider`; lists credential providers to authenticate with the STS endpoint and retrieve short-lived role credentials

* `fs.azure.account.key` (credential)
  + Value: `<your_account_key>`
  + Description: Storage account key

**Cache Options**

* **Enable local caching when possible**: Selected by default. Along with asynchronous access for cloud caching, local caching can improve query performance.
* **Max percent of total available cache space to use when possible**: Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage.

### Reflection Refresh

You can set the policy that controls how often reflections are scheduled to be refreshed automatically, as well as the time limit after which reflections expire and are removed.

**Refresh Settings**

* **Never refresh**: Prevent automatic Reflection refresh. By default, Reflections refresh automatically.
* **Refresh every**: Set the refresh interval in hours, days, or weeks. Ignored if **Never refresh** is selected.
* **Set refresh schedule**: Specify a daily or weekly refresh schedule.

**Expire Settings**

* **Never expire**: Prevent reflections from expiring. By default, reflections expire after the configured time limit.
* **Expire after**: The time limit after which reflections are removed from Dremio, specified in hours, days, or weeks. Ignored if **Never expire** is selected.

### Metadata

Specifying metadata options is handled with the following settings.

**Dataset Handling**

* Remove dataset definitions if underlying data is unavailable (default).

**Dataset Discovery**

The refresh interval for fetching top-level source object names such as databases and tables.

* **Fetch every**: You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour.

**Dataset Details**

The metadata that Dremio needs for query planning, such as information needed for fields, types, shards, statistics, and locality.

* **Fetch mode**: You can choose to fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**.
* **Fetch every**: You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour.
* **Expire after**: You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours.

### Privileges

You can grant [privileges](/dremio-cloud/security/privileges) to specific users or roles. To grant access to a user or role:

1. For **Privileges**, enter the user name or role name to which you want to grant access and click **Add to Privileges**. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source being created.
3. Click **Save** after setting the configuration.

## Update an Iceberg REST Catalog Source

To update an Iceberg REST Catalog:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the Source Settings dialog, edit the settings you wish to update. Dremio does not support updating the source name.
4. Click **Save**.

## Delete an Iceberg REST Catalog Source

To delete an Iceberg REST Catalog source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

## Supported Configurations

Select your catalog type below.

* Apache Polaris OSS
* Nessie Catalog
* Glue Iceberg REST
* S3 Tables
* Tableflow Catalog
* Microsoft OneLake

**General Settings**

* **Endpoint URI**: `http://localhost:8181/api/catalog`
* **Use vended credentials**: Unchecked

**Advanced Options – Catalog Properties**

* `warehouse`: `polaris_oss_catalog`
* `scope`: `PRINCIPAL_ROLE:ALL`
* `fs.s3a.aws.credentials.provider`: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`

**Advanced Options – Catalog Credentials**

* `fs.s3a.access.key`: `<s3AccessKey>`
* `fs.s3a.secret.key`: `<s3SecretKey>`
* `credential`: `<client_id:client_secret>`

**General Settings**

* **Endpoint URI**: `http://127.0.0.1:19120/iceberg/`
* **Use vended credentials**: Unchecked

**Advanced Options – Catalog Properties**

* `warehouse`: `s3://mybucket/restcatalog/`
* `fs.s3a.aws.credentials.provider`: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`

**Advanced Options – Catalog Credentials**

* `fs.s3a.access.key`: `<s3AccessKey>`
* `fs.s3a.secret.key`: `<s3SecretKey>`

Replace `region` with your AWS region (e.g., `us-west-2`). You will need your AWS account number and Table Bucket name.

**General Settings**

* **Endpoint URI**: `https://glue.region.amazonaws.com/iceberg`
* **Use vended credentials**: Unchecked

**Advanced Options – Catalog Properties**

* `warehouse`: `accountnumber:s3tablescatalog/tablebucketname`
* `rest.sigv4-enabled`: `true`
* `rest.signing-name`: `glue`
* `rest.signing-region`: `<region>`
* `fs.s3a.aws.credentials.provider`: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
* `dremio.bucket.discovery.enabled`: `false`
* `dremio.s3.region`: `<region>`
* `fs.s3a.audit.enabled`: `false`
* `fs.s3a.create.file-status-check`: `false`

**Advanced Options – Catalog Credentials**

* `rest.access-key-id`: `<s3AccessKey>`
* `rest.secret-access-key`: `<s3SecretKey>`
* `fs.s3a.access.key`: `<s3AccessKey>`
* `fs.s3a.secret.key`: `<s3SecretKey>`

Replace `region` with your AWS region (e.g., `us-west-2`). You will need your AWS account number and Table Bucket name.

**General Settings**

* **Endpoint URI**: `https://s3tables.region.amazonaws.com/iceberg`
* **Use vended credentials**: Unchecked

**Advanced Options – Catalog Properties**

* `warehouse`: `arn:aws:s3tables:region:accountnumber:bucket/tablebucketname`
* `rest.sigv4-enabled`: `true`
* `rest.signing-name`: `s3tables`
* `rest.signing-region`: `<region>`
* `fs.s3a.aws.credentials.provider`: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
* `dremio.bucket.discovery.enabled`: `false`
* `dremio.s3.region`: `<region>`
* `fs.s3a.audit.enabled`: `false`
* `fs.s3a.create.file-status-check`: `false`

**Advanced Options – Catalog Credentials**

* `rest.access-key-id`: `<s3AccessKey>`
* `rest.secret-access-key`: `<s3SecretKey>`
* `fs.s3a.access.key`: `<s3AccessKey>`
* `fs.s3a.secret.key`: `<s3SecretKey>`

Note: Namespaces for the Tableflow Catalog are the Kafka clusters within your environment.

**General Settings**

* **Endpoint URI**: `https://tableflow.us-west-2.aws.confluent.cloud/iceberg/catalog/organizations/f140b886-a3e9-4e1d-ba9d-5b96b8bf4ea8/environments/env-7kn93o`
* **Allowed Namespaces**: `<kafkaClusterID>`
* **Allowed Namespaces include their whole subtrees**: Unchecked
* **Use vended credentials**: Checked

**Advanced Options – Catalog Credentials**

* `credential`: `<api_key:secret_key>`

Replace the placeholders inside `<...>` with your respective values. For example, a warehouse value could be `icy/icelake.Lakehouse`. The `fs.*` values are used to establish connections to the storage underlying your catalog in OneLake.

**General Settings**

* **Endpoint URI**: `https://onelake.table.fabric.microsoft.com/iceberg`
* **Use vended credentials**: Unchecked

**Advanced Options – Catalog Properties**

* `rest.auth.type`: `oauth2`
* `oauth2-server-uri`: `https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/token`
* `scope`: `https://storage.azure.com/.default`
* `warehouse`: `<catalog>`
* `fs.azure.endpoint`: `dfs.fabric.microsoft.com`
* `fs.azure.account.auth.type`: `OAuth`
* `fs.azure.account.oauth2.client.endpoint`: `https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/token`
* `fs.azure.account.oauth2.client.id`: `<oauth_client_id>`

**Advanced Options – Catalog Credentials**

* `fs.azure.account.oauth2.client.secret`: `<oauth_client_secret>`
* `credential`: `<oauth_client_id:oauth_client_secret>`

Was this page helpful?

* Configure an Iceberg REST Catalog Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update an Iceberg REST Catalog Source
* Delete an Iceberg REST Catalog Source
* Supported Configurations

<div style="page-break-after: always;"></div>

# AWS Glue Data Catalog | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/catalogs/aws-glue-data-catalog

On this page

The [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html) is a metadata store that lets you store and share metadata in the AWS Cloud.

## Supported Formats

Dremio can query data stored in S3 in file formats (including delimited, Excel (XLSX), and Parquet) and [Apache Iceberg](/dremio-cloud/developer/data-formats/iceberg/) or [Delta Lake](/dremio-cloud/developer/data-formats/delta-lake/) table formats.

## Add an AWS Glue Data Catalog

To add an AWS Glue Data Catalog to your project:

1. From the Datasets page, to the right of **Sources** in the left panel, click ![Add icon](/images/icons/plus.png "Add icon").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **AWS Glue Data Catalog**.

### General

To configure an AWS Glue Data Catalog source:

* **Name** – Specify a name for the data source. You cannot change the name after the source is created. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
* **AWS Region Selection** – Specify the region hosting the AWS Glue catalog.
* **Authentication** – Provide the role that Dremio will assume to gain access to the source:

  + [Create an AWS IAM role](/dremio-cloud/bring-data/connect/object-storage/amazon-s3/#create-an-aws-iam-role) in your AWS account that trusts Dremio.
  + Add an AWS Glue Access Policy to your custom role that provides access to your AWS Glue Data Catalog source.
  + Add the **Role ARN** to the source configuration.
* **Allowed Databases** – (Optional) The allowed databases configuration is a post-connection filter on the databases visible from AWS Glue. When selective access to the databases within AWS Glue is required, the allowed databases filter limits access within Dremio to only the needed databases per source connection, improving data security and source metadata refresh performance.

  When the allowed databases filter is empty, all databases from the AWS Glue source are visible in Dremio. When a database is added to or removed from the filter, Dremio performs an asynchronous update to expose new databases and remove databases not included in the filter. Each entry in the allowed databases filter must be a valid database name; misspelled or nonexistent databases are ignored.
* **Encrypted Connection** – (Optional) To secure the connections between AWS Glue and Dremio, select the **Encrypt connection** checkbox.

### Advanced Options

Click **Advanced Options** in the left menu sidebar.

* **Connection Properties** – You can add key-value pairs to provide custom connection properties relevant to the source.
  1. Click **Add Property**.
  2. For Name, enter a connection property.
  3. For Value, enter the corresponding connection property value.
* **Lake Formation** – Lake Formation provides access controls and allows administrators to define security policies. Enabling this functionality and additional details on the configuration options below are described in AWS Lake Formation.
  + **Enforce AWS Lake Formation access permissions on datasets** – Dremio checks any datasets included in the AWS Glue source for the required permissions to perform queries.
  + **Prefix to map Dremio users to AWS ARNs** – Leave blank to default to the end user's username, or enter a regular expression.
  + **Prefix to map Dremio groups to AWS ARNs** – Leave blank to default to the end user's group, or enter a regular expression.

Under Cache Options:

* **Enable local caching when possible** – Selected by default, along with asynchronous access for cloud caching. Uncheck the checkbox to disable this option.
* **Max percent of total available cache space to use when possible** – Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage.

### Reflection Refresh

Click **Reflection Refresh** in the source settings sidebar. This section lets you manage how often Reflections are refreshed and how long data can be served before expiration. To learn more about Reflections, see [Manual Reflections](/dremio-cloud/admin/performance/manual-reflections/). All Reflection parameters are optional.

You can set the following refresh policies for Reflections:

* **Refresh period** – Manage the refresh period by either enabling the option to never refresh or setting a refresh frequency in hours, days, or weeks. The default frequency to refresh Reflections is every hour.
* **Expiration period** – Set the expiration period for the length of time that data can be served by either enabling the option to never expire or setting an expiration time in hours, days, or weeks. The default expiration time is three hours.

### Metadata

Click **Metadata** in the left menu sidebar. This section lets you configure settings to refresh metadata and enable other dataset options. All metadata parameters are optional.

You can configure Dataset Handling and Metadata Refresh parameters.

#### Dataset Handling

* **Remove dataset definitions if underlying data is unavailable** – By default, Dremio removes dataset definitions if underlying data is unavailable. This option is for scenarios when files are temporarily deleted and added back in the same location with new sets of files.

#### Metadata Refresh

* **Dataset Discovery** – The refresh interval for retrieving top-level source object names such as databases and tables. Use this parameter to set the time interval. You can choose to set the frequency to collect object names in minutes, hours, days, or weeks. The default frequency to fetch object names is one hour.
* **Dataset Details** – The metadata that Dremio needs for query planning, such as information required for fields, types, shards, statistics, and locality.

  + **Fetch mode** – You can choose to fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**.
  + **Fetch every** – You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is one hour.
  + **Expire after** – You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is three hours.

### Privileges

Click **Privileges** in the left menu sidebar. This section lets you grant privileges to specific users or roles. To learn more about how Dremio allows for the implementation of granular-level privileges, see [Privileges](/dremio-cloud/security/privileges).

To add a privilege for a user or role:

1. In the Add User/Role field, enter the user or role name to which you want to apply privileges.
2. Click **Add to Privileges**. The user or role is added to the Users table.

To set privileges for a user or role:

1. In the Users table, identify the user to set privileges for and click under the appropriate column (Select, Alter, Create Table, etc.) to either enable or disable that privilege. A green checkmark indicates that the privilege is enabled.
2. Click **Save**.

After you have connected Dremio to the AWS Glue Data Catalog, you will be able to edit the Data Catalog and remove it when it is no longer needed.

## Update an AWS Glue Data Catalog Source

To update an AWS Glue Data Catalog source:

1. From the Datasets page, in the **Lakehouse Catalogs** section, right-click on the source and select **Settings**.
2. For information about these settings and guidance on the changes you can make, see Add an AWS Glue Data Catalog.
3. Click **Save**.

## Delete an AWS Glue Data Catalog Source

To remove a Data Catalog source:

1. From the Datasets page, in the **Lakehouse Catalogs** section, right-click on the source and select **Delete**.
2. Click **Delete** again to confirm.

## Add an AWS Glue Access Policy to a Custom Role

To add the required AWS Glue access policy to your custom role:

1. On the Roles page, click the role name. Use the **Search** field to locate the role if needed.
2. From the Roles page, in the Permissions section, click **Add permissions** > **Create inline policy**.
3. On the Create policy page, click the **JSON** tab.
4. Delete the current JSON policy and copy the [IAM Policy Template for AWS Glue Catalog](/dremio-cloud/admin/projects/your-own-project-storage#create-your-iam-role).

   IAM Policy Template for AWS Glue Catalog

   ```
   {  
       "Version": "2012-10-17",  
       "Statement": [  
           {  
               "Sid": "AccessGlueCatalog",  
               "Effect": "Allow",  
               "Action": [  
                   "glue:GetDatabase",  
                   "glue:GetDatabases",  
                   "glue:GetPartition",  
                   "glue:GetPartitions",  
                   "glue:GetTable",  
                   "glue:GetTableVersions",  
                   "glue:GetTables",  
                   "glue:GetConnection",  
                   "glue:GetConnections",  
                   "glue:GetDevEndpoint",  
                   "glue:GetDevEndpoints",  
                   "glue:GetUserDefinedFunction",  
                   "glue:GetUserDefinedFunctions",  
                   "glue:BatchGetPartition"  
               ],  
               "Resource": [  
                   "*"  
               ]  
           },  
           {  
               "Sid": "ReadWriteGlueS3Buckets",  
               "Effect": "Allow",  
               "Action": [  
                   "s3:GetObject",  
                   "s3:PutObject"  
               ],  
               "Resource": [  
                   "arn:aws:s3:::aws-glue-*/*",  
                   "arn:aws:s3:::*/*aws-glue-*/*"  
               ]  
           },  
           {  
               "Sid": "ReadPublicGlueBuckets",  
               "Effect": "Allow",  
               "Action": [  
                   "s3:GetObject"  
               ],  
               "Resource": [  
                   "arn:aws:s3:::crawler-public*",  
                   "arn:aws:s3:::aws-glue-*"  
               ]  
           },  
           {  
               "Sid": "ManageGlueServiceTags",  
               "Effect": "Allow",  
               "Action": [  
                   "ec2:CreateTags",  
                   "ec2:DeleteTags"  
               ],  
               "Condition": {  
                   "ForAllValues:StringEquals": {  
                       "aws:TagKeys": [  
                           "aws-glue-service-resource"  
                       ]  
                   }  
               },  
               "Resource": [  
                   "arn:aws:ec2:*:*:network-interface/*",  
                   "arn:aws:ec2:*:*:security-group/*",  
                   "arn:aws:ec2:*:*:instance/*"  
               ]  
           }  
       ]  
   }
   ```
5. Click **Next**.
6. On the Review policy page, in the **Name** field, enter a name for the policy.
7. Click **Create policy**. The policy is created and you are returned to the Roles page.

## AWS Lake Formation

AWS Lake Formation provides access controls for datasets in the AWS Glue Data Catalog and is used to define security policies from a centralized location that may be shared across multiple tools. Dremio may be configured to refer to this service to verify user access to contained datasets.

### Requirements

* [Identity provider service](/dremio-cloud/security/authentication/idp) set up
  + (Recommended) [SAML connection](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html) with AWS
* [Permissions set up in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html)
* AWS Glue Data Catalog connected to Dremio
* User and Group ARN prefixes specified and enabled

### Lake Formation Workflow

When Lake Formation is properly configured, Dremio adheres to the following workflow each time an end user attempts to access, edit, or query datasets with managed privileges:

1. Dremio enforces [access control](/dremio-cloud/security/#access-control). See Configure Sources for Lake Formation for access control recommendations.
2. Dremio checks each table to determine if those stored in the AWS Glue source are configured to use Lake Formation for security.

   * If one or more datasets leverage Lake Formation, Dremio determines the user ARNs to use when checking against Lake Formation.
3. Dremio queries Lake Formation to determine a user's access level to the datasets using the user/group ARNs.

   * If the user has access to the datasets specified within the query's scope, the query proceeds.
   * If the user lacks access, the query fails with a permission error.

### Configure Sources for Lake Formation

Lake Formation integration is dependent on the mapping of user/group names in Dremio to the IAM user/group ARNs used by AWS.

To configure an existing or new AWS Glue Data Catalog source, you must set the following options:

1. From your existing source or upon creating an **AWS Glue Data Catalog** source, navigate to the Advanced Options tab.
2. Enable **Enforce AWS Lake Formation access permissions on datasets**.
3. Fill in the user and group prefix settings as instructed in the [Lake Formation Permissions Reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html). For example, if you are using a SAML provider in AWS:

   * User prefix with SAML: `arn:aws:iam::<AWS_ACCOUNT_ID>:saml-provider/<PROVIDER_NAME_IN_AWS>:user/`
   * Group prefix with SAML: `arn:aws:iam::<AWS_ACCOUNT_ID>:saml-provider/<PROVIDER_NAME_IN_AWS>:group/`

   note

   **Best Practice:** On the Privileges tab, we recommend enabling the **Select** privilege for **All Users** to allow non-admin users to access the AWS Glue source from Dremio.

### Lake Formation Cell-Level Security

Dremio supports AWS Lake Formation [cell-level security](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) with row-level access permissions based on AWS Lake Formation [PartiQL expressions](https://docs.aws.amazon.com/lake-formation/latest/dg/partiql-support.html). If the user does not have read permissions on a column or cell, Dremio masks the data in that column or cell with a `NULL` value.

To speed up query planning, Dremio uses the AWS Lake Formation permissions cache for each table. By default, the cache is enabled and reuses previously loaded permissions for up to 3600 seconds (1 hour).

## Limitations

* VPC-restricted S3 buckets are not supported.

Was this page helpful?

* Supported Formats
* Add an AWS Glue Data Catalog
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update an AWS Glue Data Catalog Source
* Delete an AWS Glue Data Catalog Source
* Add an AWS Glue Access Policy to a Custom Role
* AWS Lake Formation
  + Requirements
  + Lake Formation Workflow
  + Configure Sources for Lake Formation
  + Lake Formation Cell-Level Security
* Limitations

<div style="page-break-after: always;"></div>

# Data Type Mapping

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/microsoft-sql-server

On this page

[Microsoft SQL Server](https://www.microsoft.com/en-in/sql-server/sql-server-2019) is a database server for storing and retrieving data.

## Prerequisites

Ensure that you have the following details before configuring Microsoft SQL Server as a source:

* Hostname or IP address of the database
* Port
* Outbound port (1433 is the default port) open in your AWS or Azure security group
* Ensure that the database version is Microsoft SQL Server version 2012 or later

## User Impersonation

The Microsoft SQL Server username provided in the source configuration is the default username that is used for running queries. When queries are run against Microsoft SQL Server in Dremio, users use the privileges associated with the Microsoft SQL Server username and run queries under that username.

You can change this default in Dremio by enabling user impersonation in the Advanced Options, which allows users to run queries under their own usernames and restricts their access. For example, `user_1` can run queries as `user_1` rather than `sqlsvr_svc`. Before enabling user impersonation, some setup is required in Microsoft SQL Server to allow one user to impersonate another user because the username of the user in Dremio must be the same as their username in Microsoft SQL Server and the user must be able to connect through the Microsoft SQL Server username.

To set up user impersonation, follow these steps:

1. Ensure the user's username in Microsoft SQL Server matches their username in Dremio. If the usernames do not match, modify one of the usernames or create a new user account with a matching username.
2. Run a GRANT IMPERSONATE command in Microsoft SQL Server to allow the user to connect through their Microsoft SQL Server username:

Example of granting impersonate privilege in Microsoft SQL Server

```
GRANT IMPERSONATE ON USER::testuser1 TO proxyuser;
```

In this example, the user can log in as `testuser1` in Dremio and in Microsoft SQL Server, and they can connect through the `proxyuser`. The `proxyuser` is the Microsoft SQL Server username provided in the source configuration.

3. Log in to Dremio as a member of the ADMIN role.
4. Follow the steps for Configure Microsoft SQL Server as a Source using the Microsoft SQL Server username `proxyuser` and enable **User Impersonation** in the **Advanced Options**.
5. Grant [source privileges](/dremio-cloud/security/privileges/#source-privileges) to the user.

Now that you have enabled user impersonation, a user who logs in to Dremio with their username can access the Microsoft SQL Server source and its datasets according to their privileges. The user can also run queries against Microsoft SQL Server under their username.

## Configure Microsoft SQL Server as a Source

Perform these steps to configure Microsoft SQL Server as a source:

1. On the Datasets page, you can see a truncated list of **Sources** at the bottom-left of the page. Click **Add Source**.

   Alternatively, click **Databases**. The page displays all database sources. Click the **Add database** button at the top-right of that page.
2. In the **Add Data Source** dialog, click **Microsoft SQL Server**.

   The following section describes the source configuration tabs.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### General

The **General** tab contains the required fields to create a Microsoft SQL Server source.

![](/assets/images/microsoft-general-8c49cb3c2449ba897888cae20a775881.png)

Perform these steps in the **General** tab:

1. In the **General** tab, for **Name**, enter a name. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. For **Host**, enter the Microsoft SQL Server host name.
3. For **Port**, enter the Microsoft SQL Server port number. The default port is 1433.
4. (Optional) For **Database**, enter the Microsoft SQL Server database name.
5. (Optional) For **Encrypt connection**, enable encrypted connections to Microsoft SQL Server using SSL.
6. For **Authentication**, **Master Authentication** is the default and the only option. Provide the username and password of a master database user with permissions to read required objects:

* For **Username**, enter your Microsoft SQL Server database username.
* For **Password**, enter your Microsoft SQL Server database password.

### Advanced Options

Click **Advanced Options** in the sidebar.

note

All advanced options are optional.

| Advanced Option | Description |
| --- | --- |
| **Show only the initial database used for connecting** | If selected, hides the other databases that the credential has access to. |
| **Record fetch size** | Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default record fetch size is 200. |
| **Maximum idle connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection idle time (s)** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query timeout (s)** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |
| **Enable user impersonation** | Select the checkbox to allow users to run queries using their credentials rather than those of the user specified in the Authentication configuration. Some setup is required in Microsoft SQL Server to allow one user to impersonate another user. Read User Impersonation for more information. |
| **Encryption** | **Verify Server Certificate** is enabled. Add an SSL/TLS server certificate distinguished name in the text box. |
| **Connection Properties** | Custom key value pairs for the connection relevant to the source. To add a connection property, click **Add property** and add the property name and value. |

### Reflection Refresh

The **Reflection Refresh** tab in the sidebar allows you to set time intervals for Reflections to refresh or expire.

![](/assets/images/microsoft-reflection-refresh-723c9eaee40b5e5605cdf11dc4b86d66.png)

### Metadata

You can configure settings to refresh metadata and handle datasets. Click **Metadata** in the sidebar.

![](/assets/images/microsoft-metadata-cb2b389165756ea21b84be3e0b96466c.png)

You can configure Dataset Handling and Metadata Refresh parameters.

##### Dataset Handling

These are the **Dataset Handling** parameters.

note

All **Dataset Handling** parameters are optional.

| Parameter | Description |
| --- | --- |
| **Remove dataset definitions if underlying data is unavailable** | By default, Dremio removes dataset definitions if underlying data is unavailable. Useful when files are temporarily deleted and added back in the same location with new sets of files. |

##### Metadata Refresh

These are the **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | (Optional) **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning such as information required for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  note

  All **Dataset Details** parameters are optional.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets that are set by default. Dremio updates details for previously queried objects in a source. Fetching from all datasets is deprecated. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

Grant privileges on the source to specific users and roles. Read [Privileges](/dremio-cloud/security/privileges) for more information about privileges.

To add source-specific privileges:

1. Enter a user or role name under **Add User/Role**, click to select the user or role, and click the **Add to Privileges** button. The added user or role is displayed in the **Users/Roles** table.
2. For each user or role listed in the **Users/Roles** table, select the checkboxes for each privilege you want to grant on the source.
3. Click **Save**.

## Edit a Microsoft SQL Server Source

To edit a Microsoft SQL Server source:

1. On the Datasets page, click **Databases**. A list of databases is displayed.
2. Hover over the database and click Settings ![](/images/icons/project-settings.png) that appears next to the database.
3. In the Source Settings dialog, you cannot edit the name. Editing other parameters is optional.
4. Click **Save**.

## Remove a Microsoft SQL Server Source

To remove a Microsoft SQL Server source, perform these steps:

1. On the Datasets page, click **Databases**. A list of sources is displayed.
2. Hover over the source and click the More (...) icon that appears next to the source.
3. From the list of actions, click **Remove Source**. Confirm that you want to remove the source.

   caution

   Removing a source causes all downstream views dependent on objects in this source to break.

   note

   Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Predicate Pushdowns

Dremio offloads these operations to Microsoft SQL Server.

`*`, `+`, `-`, `/`, `%`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
`AND`, `NOT`, `OR`, `||`  
`ABS`  
`ACOS`  
`ADD_MONTHS`  
`ASIN`  
`ATAN`  
`ATAN2`  
`AVG`  
`CAST`  
`CEIL`  
`CEILING`  
`CHAR_LENGTH`  
`CHARACTER_LENGTH`  
`CONCAT`  
`COS`  
`COT`  
`DATE_ADD`  
`DATE_SUB`  
`DATE_TRUNC_DAY`  
`DATE_TRUNC_HOUR`  
`DATE_TRUNC_MINUTE`  
`DATE_TRUNC_MONTH`  
`DATE_TRUNC_YEAR`  
`DEGREES`  
`E`  
`EXP`  
`EXTRACT_DAY`  
`EXTRACT_DOW`  
`EXTRACT_DOY`  
`EXTRACT_HOUR`  
`EXTRACT_MINUTE`  
`EXTRACT_MONTH`  
`EXTRACT_QUARTER`  
`EXTRACT_SECOND`  
`EXTRACT_WEEK`  
`EXTRACT_YEAR`  
`FLOOR`  
`IS DISTINCT FROM`  
`IS NOT DISTINCT FROM`  
`IS NOT NULL`  
`IS NULL`  
`LAST_DAY`  
`LCASE`  
`LEFT`  
`LENGTH`  
`LIKE`  
`LN`  
`LOCATE`  
`LOG`  
`LOG10`  
`LOWER`  
`LPAD`  
`LTRIM`  
`MAX`  
`MEDIAN`  
`MIN`  
`MOD`  
`MONTH`  
`PERCENT_CONT`  
`PERCENT_DISC`  
`PI`  
`POSITION`  
`POW`  
`POWER`  
`RADIANS`  
`RAND`  
`REPLACE`  
`REVERSE`  
`RIGHT`  
`ROUND`  
`RPAD`  
`RTRIM`  
`SIGN`  
`SIN`  
`SQRT`  
`SUBSTR`  
`SUBSTRING`  
`SUM`  
`TAN`  
`TIMESTAMPADD_DAY`  
`TIMESTAMPADD_HOUR`  
`TIMESTAMPADD_MINUTE`  
`TIMESTAMPADD_MONTH`  
`TIMESTAMPADD_QUARTER`  
`TIMESTAMPADD_SECOND`  
`TIMESTAMPADD_YEAR`  
`TIMESTAMPDIFF_DAY`  
`TIMESTAMPDIFF_HOUR`  
`TIMESTAMPDIFF_MINUTE`  
`TIMESTAMPDIFF_MONTH`  
`TIMESTAMPDIFF_QUARTER`  
`TIMESTAMPDIFF_SECOND`  
`TIMESTAMPDIFF_WEEK`  
`TIMESTAMPDIFF_YEAR`  
`TO_DATE`  
`TRIM`  
`TRUNC`  
`TRUNCATE`  
`UCASE`  
`UPPER`  
`YEAR`

note

Since Microsoft SQL Server has no Boolean type, project operations that contain SQL expressions which evaluate to true or false (e.g. `SELECT username, friends > 0`), and filter operations that include Boolean literals in a filter (e.g. `WHERE currentAccount = true`) cannot be executed as pushdowns.

# Data Type Mapping

Dremio supports SQL Server data types, as shown in the following table which provides the mappings from SQL Server to Dremio data types. If there are additional SQL Server types not listed in the table, then those types are not supported in Dremio.

| SQL Server Data Type | Dremio Type |
| --- | --- |
| BIGINT IDENTITY | BIGINT |
| BIGINT | BIGINT |
| BINARY | VARBINARY |
| BIT | BOOLEAN |
| CHAR | VARCHAR |
| DATE | DATE |
| DATETIME | TIMESTAMP |
| DATETIME2 | TIMESTAMP |
| DECIMAL | DECIMAL |
| DECIMAL() IDENTITY | DECIMAL |
| FLOAT | DOUBLE |
| IMAGE | VARBINARY |
| INT IDENTITY | INTEGER |
| INT | INTEGER |
| MONEY | DOUBLE |
| NCHAR | VARCHAR |
| NTEXT | VARCHAR |
| NUMERIC | DECIMAL |
| NUMERIC() IDENTITY | DECIMAL |
| NVARCHAR | VARCHAR |
| REAL | FLOAT |
| SMALLDATETIME | TIMESTAMP |
| SMALLINT IDENTITY | INTEGER |
| SMALLINT | INTEGER |
| SMALLMONEY | DOUBLE |
| SYSNAME | VARCHAR |
| TEXT | VARCHAR |
| TIME | TIME |
| TINYINT IDENTITY | INTEGER |
| TINYINT | INTEGER |
| UNIQUEIDENTIFIER | VARBINARY |
| VARBINARY | VARBINARY |
| VARCHAR | VARCHAR |

Was this page helpful?

* Prerequisites
* User Impersonation
* Configure Microsoft SQL Server as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Edit a Microsoft SQL Server Source
* Remove a Microsoft SQL Server Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

# Snowflake Open Catalog | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/catalogs/snowflake-open-catalog

On this page

Dremio supports Snowflake Open Catalog as an Iceberg catalog source. With this source connector, you can connect to and read from internal and external Snowflake Open Catalogs and write to external Snowflake Open Catalogs.

## Prerequisites

You will need the catalog **Service URI**, **Client ID**, and **Client Secret** from the Snowflake setup. For a walkthrough of the Snowflake setup, refer to [Query a table in Snowflake Open Catalog using a third-party engine](https://other-docs.snowflake.com/opencatalog/query-table-using-third-party-engine).

## Configure Snowflake Open Catalog as a Source

To add a Snowflake Open Catalog source:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![Add Source icon](/images/icons/plus.png "Add Source icon").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Snowflake Open Catalog**.

### General

To configure the source connection:

1. For **Name**, enter a name for the source. The name you enter must be unique in the organization. Consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore (\_), or hyphen (-).
2. Enter the name of the Snowflake Open Catalog.
3. For **Endpoint URI**, specify the catalog service URI.
4. In the Authentication section, use the **Client ID** and **Client Secret** created during the [configuration of a service connection](https://other-docs.snowflake.com/opencatalog/configure-service-connection) for the Snowflake Open Catalog.
5. By default, **Use vended credentials** is enabled. This allows Dremio to connect to the catalog and receive temporary credentials to the underlying storage location. If this is enabled, you do not need to add storage authentication in Advanced Options.
6. (Optional) For **Allowed Namespaces**, add each namespace and select the option if you want to include their entire subtrees. Tables are organized into namespaces, which can be at the top level or nested within one another. Namespace names cannot contain periods or spaces.

### Advanced Options

**Storage Authentication**

If you disabled vended credentials in the General tab, you must manually provide the storage authentication.

Dremio supports Amazon S3, Azure Storage, and Google Cloud Storage (GCS) as object storage services. For acceptable storage authentication configurations, see the following catalog properties and credentials for each service option.

* S3 Access Key
* S3 Assumed Role
* Azure with Entra ID
* Azure Shared Key
* GCS Default Credentials
* GCS KeyFile

* `fs.s3a.aws.credentials.provider` (property)

  + Value: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
  + Description: Required value for a Snowflake Open Catalog source
* `fs.s3a.access.key` (credential)

  + Value: `<your_access_key>`
  + Description: AWS access key ID used by S3A file system
* `fs.s3a.secret.key` (credential)

  + Value: `<your_secret_key>`
  + Description: AWS secret key used by S3A file system

* `fs.s3a.assumed.role.arn` (property)

  + Value: `arn:aws:iam::*******:role/OrganizationAccountAccessRole`
  + Description: AWS ARN for the role to be assumed
* `fs.s3a.aws.credentials.provider` (property)

  + Value: `com.dremio.plugins.s3.store.STSCredentialProviderV1`
  + Description: Required value for a Snowflake Open Catalog source
* `fs.s3a.assumed.role.credentials.provider` (property)

  + Value: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
  + Description: Use only if the credential provider is `AssumedRoleCredentialProvider`; lists credential providers to authenticate with the STS endpoint and retrieve short-lived role credentials
* `fs.s3a.access.key` (credential)

  + Value: `<your_access_key>`
  + Description: AWS access key ID used by S3A file system
* `fs.s3a.secret.key` (credential)

  + Value: `<your_secret_key>`
  + Description: AWS secret key used by S3A file system

* `fs.azure.account.auth.type` (property)

  + Value: `OAuth`
  + Description: Authentication type
* `fs.azure.account.oauth2.client.id` (property)

  + Value: `<your_client_ID>`
  + Description: Client ID from App Registration within Azure Portal
* `fs.azure.account.oauth2.client.endpoint` (property)

  + Value: `https://login.microsoftonline.com/<ENTRA_ID>/oauth2/token`
  + Description: Microsoft Entra ID from Azure Portal
* `fs.azure.account.oauth2.client.secret` (credential)

  + Value: `<your_client_secret>`
  + Description: Client secret from App Registration within Azure Portal

* `fs.azure.account.key` (credential)
  + Value: `<your_account_key>`
  + Description: Storage account key

* `dremio.gcs.use_keyfile` (property)
  + Value: `false`
  + Description: Required value for a Snowflake Open Catalog source

* `dremio.gcs.clientId` (property)

  + Value: `<your_client_ID>`
  + Description: Client ID from GCS
* `dremio.gcs.projectId` (property)

  + Value: `<your_project_ID>`
  + Description: Project ID from GCS
* `dremio.gcs.clientEmail` (property)

  + Value: `<your_client_email>`
  + Description: Client email from GCS
* `dremio.gcs.privateKeyId` (property)

  + Value: `<your_private_key_ID>`
  + Description: Private key ID from GCS
* `dremio.gcs.use_keyfile` (property)

  + Value: `true`
  + Description: Required value for a Snowflake Open Catalog source
* `dremio.gcs.privateKey` (credential)

  + Value: `<your_private_key>`
  + Description: Private key from GCS

**Cache Options**

* **Enable local caching when possible**: Selected by default. Along with asynchronous access for cloud caching, local caching can improve query performance.
* **Max percent of total available cache space to use when possible**: Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage.

### Reflection Refresh

You can set the policy that controls how often reflections are scheduled to be refreshed automatically, as well as the time limit after which reflections expire and are removed.

**Refresh Settings**

* **Never refresh**: Prevent automatic Reflection refresh. By default, Reflections refresh automatically.
* **Refresh every**: Set the refresh interval in hours, days, or weeks. Ignored if **Never refresh** is selected.
* **Set refresh schedule**: Specify a daily or weekly refresh schedule.

**Expire Settings**

* **Never expire**: Prevent Reflections from expiring. By default, Reflections expire after the configured time limit.
* **Expire after**: The time limit after which Reflections are removed from Dremio, specified in hours, days, or weeks. Ignored if **Never expire** is selected.

### Metadata

Specify metadata options with the following settings.

#### Dataset Handling

Remove dataset definitions if underlying data is unavailable (default).

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

**Dataset Discovery**

The refresh interval for fetching top-level source object names such as databases and tables.

* **Fetch every**: You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour.

**Dataset Details**

The metadata that Dremio needs for query planning, such as information needed for fields, types, shards, statistics, and locality.

* **Fetch mode**: You can choose to fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**.
* **Fetch every**: You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour.
* **Expire after**: You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours.

### Privileges

You can grant privileges to specific users or roles. See [Privileges](/dremio-cloud/security/privileges) for more information.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name to which you want to grant access and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update a Snowflake Open Catalog Source

To update a Snowflake Open Catalog source:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![Settings icon](/images/settings-icon.png "Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you want to update. Dremio does not support updating the source name. For information about the settings options, see Configure Snowflake Open Catalog as a Source.
4. Click **Save**.

## Delete a Snowflake Open Catalog Source

To delete a Snowflake Open Catalog source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

Was this page helpful?

* Prerequisites
* Configure Snowflake Open Catalog as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update a Snowflake Open Catalog Source
* Delete a Snowflake Open Catalog Source

<div style="page-break-after: always;"></div>

# Databricks Unity Catalog | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/catalogs/databricks-unity-catalog

On this page

Connect to Delta Lake tables in Databricks Unity Catalog through Dremio. Unity Catalog acts as a centralized metastore for managing tables across your Databricks environment, and Dremio can query these tables when they use Delta Lake's Universal Format (UniForm).

## UniForm Iceberg Required

To query Delta tables through Dremio, you must enable UniForm on your tables in Databricks. UniForm provides an Iceberg metadata layer that allows Iceberg-compatible clients like Dremio to read Delta tables.

**Requirements:**

* UniForm must be enabled on your Delta tables. See [Enable UniForm Iceberg](https://docs.databricks.com/en/delta/uniform.html#enable-uniform-iceberg) in the Databricks documentation.
* Your tables must use Delta protocol minReaderVersion 2 or higher. See [Features by protocol version](https://docs.databricks.com/en/delta/feature-compatibility.html#features-by-protocol-version).

UniForm tables have certain limitations. Review [Limitations](https://docs.databricks.com/en/delta/uniform.html#limitations) in the Databricks documentation before proceeding.

## Configure Databricks Unity Catalog as a Source

To add a Unity Catalog source:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "Add Source icon").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Unity Catalog**.

### General

To configure the source connection:

1. For **Name**, enter a name for the source. The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore (\_), or hyphen (-).
2. For **Unity Catalog**, enter the catalog name.
3. For **Endpoint URI**, specify the catalog service URI. For more information on how to find your Unity Catalog URI, see [Read using the Unity Catalog Iceberg catalog endpoint](https://docs.databricks.com/en/delta/uniform.html#read-using-the-unity-catalog-iceberg-catalog-endpoint).
4. Under **Authentication Type**, select one of the following:

   * **Databricks Personal Access Token**: Provide a Databricks Personal Access Token (PAT). Depending on your deployment, see the following:
     + AWS-based Unity deployment: See [Databricks personal access tokens for service principals](https://docs.databricks.com/en/dev-tools/auth/pat.html#databricks-personal-access-tokens-for-service-principals) to create a PAT.
     + Azure Databricks-based Unity deployment: See [Azure Databricks personal access tokens for service principals](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth/pat#azure-databricks-personal-access-tokens-for-service-principals) to create a PAT.
   * **Microsoft Entra ID**: Provide the following information from your application registered in Microsoft Entra ID:
     + **Application ID**: The Application ID of the application registered in Microsoft Entra ID.
     + **OAuth 2.0 Token Endpoint**: The OAuth 2.0 token endpoint URL (for example, `https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/token`).
     + **Application Secret**: The Application Secret of the application registered in Microsoft Entra ID.
5. By default, **Use vended credentials** is turned on. This allows Dremio to connect to the catalog and receive temporary credentials for the underlying storage location. When this option is enabled, you don't need to add the storage authentication in **Advanced Options**.
6. (Optional) For **Allowed Namespaces**, add each namespace and check the option if you want to include their entire subtrees. Tables are organized into namespaces, which can be at the top level or nested within one another. Namespace names cannot contain periods or spaces.

### Advanced Options

**Storage Authentication**

If you disabled vended credentials in the General tab, you must manually provide the storage authentication.

Dremio supports Amazon S3, Azure Storage, and Google Cloud Storage (GCS) as object storage services. For acceptable storage authentication configurations, see the following catalog properties and credentials for each service option.

* S3 Access Key
* S3 Assumed Role
* Azure Shared Key
* GCS KeyFile

* `fs.s3a.aws.credentials.provider` (property)

  + Value: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
  + Description: Required field for a Unity Catalog source
* `fs.s3a.access.key` (credential)

  + Value: `<your_access_key>`
  + Description: AWS access key ID used by S3A file system. Omit for IAM role-based or provider-based authentication.
* `fs.s3a.secret.key` (credential)

  + Value: `<your_secret_key>`
  + Description: AWS secret key used by S3A file system. Omit for IAM role-based or provider-based authentication.

* `fs.s3a.assumed.role.arn` (property)

  + Value: `arn:aws:iam::*******:role/OrganizationAccountAccessRole`
  + Description: AWS ARN for the role to be assumed
* `fs.s3a.aws.credentials.provider` (property)

  + Value: `com.dremio.plugins.s3.store.STSCredentialProviderV1`
  + Description: Required field for a Unity Catalog source
* `fs.s3a.assumed.role.credentials.provider` (property)

  + Value: `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider`
  + Description: Use only if the credential provider is `AssumedRoleCredentialProvider`; lists credential providers to authenticate with the STS endpoint and retrieve short-lived role credentials.

* `fs.azure.account.key` (credential)
  + Value: `<your_account_key>`
  + Description: Storage account key

* `fs.AbstractFileSystem.gs.impl` (property)

  + Value: `com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS`
  + Description: Required field for a Unity Catalog source
* `fs.gs.auth.service.account.enable` (property)

  + Value: `true`
  + Description: Required field for a Unity Catalog source
* `fs.gs.impl` (property)

  + Value: `com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem`
  + Description: Required field for a Unity Catalog source
* `fs.gs.bucket` (property)

  + Value: `<your_bucket>`
  + Description: Bucket where your data is stored for Unity Catalog in GCS
* `fs.gs.project.id` (property)

  + Value: `<your_project_ID>`
  + Description: Project ID from GCS
* `fs.gs.auth.service.account.email` (property)

  + Value: `<your_client_email>`
  + Description: Client email from GCS
* `fs.gs.auth.service.account.private.key.id` (property)

  + Value: `<your_private_key_id>`
  + Description: Private key ID from GCS
* `dremio.gcs.use_keyfile` (property)

  + Value: `true`
  + Description: Required field for a Unity Catalog source
* `fs.gs.auth.service.account.private.key` (credential)

  + Value: `<your_private_key>`
  + Description: Private key from GCS

**Cache Options**

* **Enable local caching when possible**: Selected by default. Along with asynchronous access for cloud caching, local caching can improve query performance.
* **Max percent of total available cache space to use when possible**: Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage.

### Reflection Refresh

You can set the policy that controls how often reflections are scheduled to be refreshed automatically, as well as the time limit after which reflections expire and are removed.

**Refresh Settings**

* **Never refresh**: Prevent automatic Reflection refresh. By default, Reflections refresh automatically.
* **Refresh every**: Set the refresh interval in hours, days, or weeks. Ignored if **Never refresh** is selected.
* **Set refresh schedule**: Specify a daily or weekly refresh schedule.

**Expire Settings**

* **Never expire**: Prevent reflections from expiring. By default, reflections expire after the configured time limit.
* **Expire after**: The time limit after which reflections are removed from Dremio, specified in hours, days, or weeks. Ignored if **Never expire** is selected.

### Metadata

Specifying metadata options is handled with the following settings.

#### Dataset Handling

Remove dataset definitions if underlying data is unavailable (default).

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

**Dataset Discovery**

The refresh interval for fetching top-level source object names such as databases and tables.

* **Fetch every**: You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour.

**Dataset Details**

The metadata that Dremio needs for query planning, such as information needed for fields, types, shards, statistics, and locality.

* **Fetch mode**: You can choose to fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**.
* **Fetch every**: You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour.
* **Expire after**: You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours.

### Privileges

You can grant privileges to specific users or roles. See [Privileges](/dremio-cloud/security/privileges) for additional information.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update a Databricks Unity Catalog Source

To update a Unity Catalog source:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name, and then click the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top-right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configure Databricks Unity Catalog as a Source.
4. Click **Save**.

## Delete a Databricks Unity Catalog Source

To delete a Unity Catalog source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

Was this page helpful?

* UniForm Iceberg Required
* Configure Databricks Unity Catalog as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update a Databricks Unity Catalog Source
* Delete a Databricks Unity Catalog Source

<div style="page-break-after: always;"></div>

# Microsoft Azure Synapse Analytics | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/bring-data/connect/databases/microsoft-azure-synapse-analytics

On this page

Dremio supports integrations with organizations using Azure Synapse Analytics dedicated SQL pools via the external source.

## Configure Microsoft Azure Synapse Analytics as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Microsoft Azure Synapse Analytics**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

* Under **Host**, enter the URL for your dedicated SQL pool, which typically ends in `.sql.azuresynapse.net`.
* Under **Port (optional)**, enter the port required to access the data source. Port 1433 is the default for Azure Synapse dedicated pools.
* Under **Database**, enter the database's name. Only this database is accessed by Dremio.

#### Authentication

Choose an authentication method:

* **No Authentication**: Dremio does not attempt to provide any authentication when connecting with the SQL pool.
* **Master Credentials**: Dremio must provide a specified username and password in order to access the SQL pool.
  + Username: Enter the Microsoft Azure Synapse Analytics username.
  + Password:
    - Dremio: Provide the Microsoft Azure Synapse Analytics password in plain text. Dremio stores the password.

Select the **Encrypt connection** option to encrypt the connection to Microsoft Azure Synapse Analytics. Clear the checkbox to disable encryption.

### Advanced Options

The following settings control more advanced functionalities in Dremio.

* **Advanced Options**
  + **Record fetch size -** Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default value is `200`.
  + **Maximum idle connections -** The maximum number of idle connections to keep. The default value is `8`.
  + **Connection idle time (s) -** Idle time, in seconds, before a connection is considered for closure. The default value is `60`.
  + **Query timeout (s) -** The timeout, in seconds, for query execution before it is canceled. Set to `0` for no timeout. The default value is `0`.
* **Encryption**
  + **Verify server certificate -** Forces Dremio to verify the server's certificate using the distinguished name.
  + **SSL/TLS server certificate distinguished name -** Specifies the location for the certificate server, which must be set to `*.sql.azuresynapse.net`.
* **Connection Properties**
  + **Name -** The unique name for any custom properties.
  + **Value -** The value associated with the custom property.

### Reflection Refresh

This tab controls the frequency of Reflection refreshes or the timespan for expiration for any queries performed using this data source.

* **Never refresh -** Prevents any query Reflections associated with this source from refreshing.
* **Refresh every -** Sets the time interval by which Reflections for this source are refreshed. This may be set to hours, days, and weeks.
* **Set refresh schedule -** Specify the daily or weekly schedule.
* **Never expire -** Prevents any query Reflections associated with this source from expiring.
* **Expire after -** Sets the time after a Reflection is created that it then expires and can no longer be used for queries. This may be set to hours, days, and weeks.

### Metadata

This tab offers settings that control how dataset details are fetched and refreshed.

* **Dataset Handling**
  + **Remove dataset definitions if underlying data is unavailable -** If this box is not checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.
* **Metadata Refresh**
  + **Dataset Discovery**
    - **Fetch every -** Specifies the time interval by which Dremio fetches object names. This can be set by minutes, hours, days, and weeks.
  + **Dataset Details**
    - **Fetch mode -** Restricts when metadata is retrieved.
    - **Fetch every -** Specifies the time interval by which metadata is fetched. This can be set by minutes, hours, days, and weeks.
    - **Expire after -** Specifies the timespan for when dataset details expire after a dataset is queried. This can be set by minutes, hours, days, and weeks.

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/dremio-cloud/security/privileges/) for additional information about privileges.

note

All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update a Microsoft Azure Synapse Analytics Source

To update a Microsoft Azure Synapse Analytics source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configure Microsoft Azure Synapse Analytics as a Source.
4. Click **Save**.

## Delete a Microsoft Azure Synapse Analytics Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Microsoft Azure Synapse Analytics source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

`%`, `*`, `+`, `-`, `/`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
AND, NOT, OR, `||`  
ABS  
ACOS  
ADD\_MONTHS  
ASIN  
ATAN  
ATAN2  
AVG  
CAST  
CEIL  
CEILING  
CHAR\_LENGTH  
CHARACTER\_LENGTH  
CONCAT  
COS  
COT  
DATE\_ADD  
DATE\_SUB  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_YEAR  
DEGREES  
E  
EXP  
EXTRACT\_DAY  
EXTRACT\_DOW  
EXTRACT\_DOY  
EXTRACT\_HOUR  
EXTRACT\_MINUTE  
EXTRACT\_MONTH  
EXTRACT\_QUARTER  
EXTRACT\_SECOND  
EXTRACT\_WEEK  
EXTRACT\_YEAR  
FLOOR  
IS DISTINCT FROM  
IS NOT DISTINCT FROM  
IS NOT NULL  
IS NULL  
LAST\_DAY  
LCASE  
LEFT  
LENGTH  
LIKE  
LN  
LOCATE  
LOG  
LOG10  
LOWER  
LPAD  
LTRIM  
MAX  
MIN  
MOD  
MONTH  
PI  
POSITION  
POW  
POWER  
RADIANS  
RAND  
REPLACE  
REVERSE  
RIGHT  
ROUND  
RPAD  
RTRIM  
SIGN  
SIN  
SQRT  
SUBSTR  
SUBSTRING  
SUM  
TAN  
TIMESTAMPADD\_DAY  
TIMESTAMPADD\_HOUR  
TIMESTAMPADD\_MINUTE  
TIMESTAMPADD\_MONTH  
TIMESTAMPADD\_QUARTER  
TIMESTAMPADD\_SECOND  
TIMESTAMPADD\_YEAR  
TIMESTAMPDIFF\_DAY  
TIMESTAMPDIFF\_HOUR  
TIMESTAMPDIFF\_MINUTE  
TIMESTAMPDIFF\_MONTH  
TIMESTAMPDIFF\_QUARTER  
TIMESTAMPDIFF\_SECOND  
TIMESTAMPDIFF\_WEEK  
TIMESTAMPDIFF\_YEAR  
TO\_DATE  
TRIM  
TRUNC  
TRUNCATE  
UCASE  
UPPER  
YEAR

Was this page helpful?

* Configure Microsoft Azure Synapse Analytics as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update a Microsoft Azure Synapse Analytics Source
* Delete a Microsoft Azure Synapse Analytics Source
* Predicate Pushdowns

<div style="page-break-after: always;"></div>

