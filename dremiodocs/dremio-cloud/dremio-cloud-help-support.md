# Help and Support | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/

The section contains additional details including:

* [Limits](/dremio-cloud/help-support/limits/)
* [Well-Architected Framework](/dremio-cloud/help-support/well-architected-framework/)
* [Keyboard Shortcuts](/dremio-cloud/help-support/keyboard-shortcuts/)

Was this page helpful?

<div style="page-break-after: always;"></div>

# Limits | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/limits

On this page

For each organization, Dremio imposes limits on the use of its resources. The following limits are grouped according to Dremio components.

Please contact Dremio to discuss if extra capacity is required.

## Organization

| Item | Enterprise Trial | Enterprise Paid |
| --- | --- | --- |
| Number of projects | 1 | 200 |
| Enterprise identity providers | 1 | 1 |
| Number of users | 5 | 15,000 |
| User invitations at once | 5 | 10 |
| Pending user invitations | 5 | 100 |
| Daily user invitations | 5 | 100 |
| Number of custom roles | 10 | 5,000 |
| Layers of nested roles | 10 | 10 |
| Direct custom role members | 5 | 1,000 |

## Projects

| Item | Enterprise Trial | Enterprise Paid |
| --- | --- | --- |
| Number of engines | 1 | 50 |
| Number of sources | 100 | 100 |
| Folder nesting depth | 8 | 8 |
| Number of tables | Unlimited | Unlimited |
| Number of views | Unlimited | Unlimited |
| Number of scripts per user | 1,000 | 1,000 |
| ACLs update rate per minute | 600 | 600 |

## Engines

| Item | Enterprise Trial | Enterprise Paid |
| --- | --- | --- |
| Replica sizes | XS | 2XS, XS, S, M, L, XL, 2XL, 3XL |
| Number of replicas | 3 | 100 |
| Query concurrency | The query concurrency limits are determined by the replica sizes as described in [Engines](/dremio-cloud/admin/engines/). | The query concurrency limits are determined by the replica sizes as described in [Engines](/dremio-cloud/admin/engines). |
| Query runtime max limit | Min 30 seconds | Min 30 seconds |

## Datasets

| Item | Enterprise Trial | Enterprise Paid |
| --- | --- | --- |
| Metadata refresh time - data lake | 15 minutes | 15 minutes |
| Metadata refresh time - RDBMS | 1 hour | 1 hour |
| Reflection refresh frequency | 1 hour | 1 hour |
| Wiki character limit | 100k characters | 100k characters |
| Number of JSON files | 300,000 | 300,000 |
| Row width | 16 MB | 16 MB |

## Reflections

| Item | Enterprise Trial | Enterprise Paid |
| --- | --- | --- |
| Maximum number of Reflections (including enabled and disabled Reflections) | 500 | 500 |
| Autonomous Reflections | 100 | 100 |

## Arrow Flight SQL (ADBC, ODBC, and JDBC)

| Item | Enterprise Trial | Enterprise Paid |
| --- | --- | --- |
| Max returned data volume | 10GB | 10GB |
| Flight Service Data Pipeline Drain Timeout | 50 seconds | 50 seconds |

## Rate Limits

Rate limits are enforced on a single IP address and apply across all organizations and projects.

| Item | Enterprise Trial | Enterprise Paid |
| --- | --- | --- |
| Login rate per user per second | 100 | 100 |
| SCIM reads per minute - user | 180 | 180 |
| SCIM writes per minute - user | 300 | 300 |
| API calls per minute | 1,200 | 1,200 |
| API: `/job/{id}/results` calls per minute | 1,000 | 1,000 |
| API: `/job/{id}/cancel` calls per minute | 100 | 100 |
| API: `/job/{id}` calls per minute | 100 | 100 |
| API: `/login/userpass` calls per second | 45 | 45 |
| Access control list update rate per minute | 60 | 60 |

Was this page helpful?

* Organization
* Projects
* Engines
* Datasets
* Reflections
* Arrow Flight SQL (ADBC, ODBC, and JDBC)
* Rate Limits

<div style="page-break-after: always;"></div>

# Keyboard Shortcuts | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/keyboard-shortcuts

On this page

Keyboard shortcuts for functions supported by Dremio are available for macOS, Windows, and Linux.

## SQL Editor

While using the SQL editor on the SQL Runner page or Datasets page, you can use shortcuts for commonly used actions, as shown in the following table:

| Function | macOS Shortcut | Windows/Linux Shortcut |
| --- | --- | --- |
| Preview | Cmd + Enter | Ctrl + Enter |
| Run | Cmd + Shift + Enter | Ctrl + Shift + Enter |
| Search | Cmd + K | Ctrl + K |
| Comment Out/In | Cmd + / | Ctrl + / |
| Find | Cmd + f | Ctrl + f |
| Trigger Autocomplete | Ctrl + Space | Ctrl + Space |
| Format Query | Cmd + Shift + f | Ctrl + Shift + f |
| Delete Line | Cmd + Shift + k | Ctrl + Shift + k |
| Toggle AI Agent | Cmd + Shift + g | Ctrl + Shift + g |

Was this page helpful?

* SQL Editor

<div style="page-break-after: always;"></div>

# Well-Architected Framework | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/well-architected-framework/

On this page

Dremio’s well-architected framework is a resource for anyone who is designing or operating solutions with Dremio. It provides insight from lessons learned through helping hundreds of customers be successful. The framework is composed of pillars that describe design principles as well as best practices based on those principles.

The Well-Architected Framework is considered complementary to the [Dremio Shared Responsibility Model](/assets/files/Dremio-Cloud-Shared-Responsibility-Model-15f76b24f0b48153532ca15b25d831c4.pdf). The Shared Responsibility Model lays out Dremio's responsibilities and your responsibilities for maintaining and operating an optimal Dremio environment, while the Well-Architected Framework provides details for carrying out your responsibilities.

## Key Pillars of Dremio’s Well-Architected Framework

Dremio’s well-architected framework follows five common pillars from cloud providers AWS, Microsoft, and Google and a sixth Dremio-specific pillar:

1. [Security](/dremio-cloud/help-support/well-architected-framework/security)
2. [Performance Efficiency](/dremio-cloud/help-support/well-architected-framework/performance-efficiency)
3. [Cost Optimization](/dremio-cloud/help-support/well-architected-framework/cost-optimization)
4. [Reliability](/dremio-cloud/help-support/well-architected-framework/reliability)
5. [Operational Excellence](/dremio-cloud/help-support/well-architected-framework/operational-excellence)
6. [Self-Serve Semantic Layer](/dremio-cloud/help-support/well-architected-framework/self-serve-semantic-layer)

Each pillar includes principles, best practices, and how-to articles on the pillar's theme.

Dremio's well-architected framework covers best practices related to configuration and operation of Dremio. Read [Architecture](/dremio-cloud/about/architecture) for more information about the Dremio architecture.

Was this page helpful?

* Key Pillars of Dremio’s Well-Architected Framework

<div style="page-break-after: always;"></div>

# Security | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/well-architected-framework/security

On this page

The security pillar is essential to ensuring that your data is secured properly when using Dremio to query your data lakehouse. The security components are especially important to architect and design your data platform. After your workloads are in production, you must continue to review your security components to ensure compliance and eliminate threats.

## Principles

### Leverage Industry-Standard Identity Providers and Authorization Systems

Dremio integrates with leading social and enterprise identity providers and data authorization systems. For robust enterprise integration with corporate policies, it is essential to leverage those third-party systems. We recommend systems that use multi-factor authentication methods and are connected to single sign-on (SSO) platforms.

### Design for Least-Privilege Access to Objects

When providing self-service access to your data lakehouse via Dremio’s [AI semantic layer](/dremio-cloud/help-support/well-architected-framework/self-serve-semantic-layer), access should only be granted to the data that is required for the role accessing the data.

## Best Practices

### Protect Access Credentials

Where possible, leverage identity providers such as [Microsoft Entra ID](/dremio-cloud/security/authentication/idp/microsoft-entra-id) and [Okta](/dremio-cloud/security/authentication/idp/okta) in conjunction with [System for Cross-domain Identity Management (SCIM)](/dremio-cloud/security/authentication/idp/#scim) where applicable to ensure that you never need to share passwords with Dremio. SSO with Microsoft Entra ID or Okta is also recommended where possible.

### Leverage Role Based Access Controls

Access to each catalog, folder, view, and table can be managed and regulated by [roles](/dremio-cloud/security/roles). Roles are used to organize privileges at scale rather than managing privileges for each individual user. You can create roles to manage privileges for users with different job functions in your organization, such as “Analyst” and “Security\_Admin” roles. Users who are members of a role gain all of the privileges granted to the role. Roles can also be nested. For example, the users in the "UK" role can automatically be members of the "EMEA” role.

Access control protects the integrity of your data and simplifies the data architecture available to users based on their roles and responsibilities within your organization. Effective controls allow users to access data that is central to their work without regard for the complexities of where and how the data is physically stored and organized.

Was this page helpful?

* Principles
  + Leverage Industry-Standard Identity Providers and Authorization Systems
  + Design for Least-Privilege Access to Objects
* Best Practices
  + Protect Access Credentials
  + Leverage Role Based Access Controls

<div style="page-break-after: always;"></div>

# Reliability | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/well-architected-framework/reliability

On this page

The reliability pillar focuses on ensuring your system is up and running and can be quickly and efficiently restored in case of unexpected downtime.

## Principles

### Set Engine Routing Rules and Engine Settings

Dremio’s engine routing rules and engine settings are powerful and protect the system from being overloaded by queries that exceed currently available resources.

### Monitor and Measure Platform Activity

To ensure the reliability of your Dremio project, you must regularly monitor and measure its activity.

## Best Practices

### Initialize Engine Routing and Engine Settings

It is important to set up engine routing rules and engines with sensible concurrency, replica, and time limits. It's better to spin replicas at sensible concurrency limits rather than risk a large number of rogue queries bringing down the engine.

### Use the Monitor Page in the Dremio Console

As an administrator using the Dremio console, you can effectively monitor catalog usage and jobs within your projects. The [Monitor page](/dremio-cloud/admin/monitor/) provides detailed visualizations and metrics that allow you to track usage patterns, resource consumption, and user impact.

In the Catalog Usage tab, you can view the 10 most-queried datasets and source folders, along with relevant statistics such as linked jobs and acceleration usage. The Catalog Usage tab excludes system tables and INFORMATION\_SCHEMA datasets and focuses solely on user queries.

In the Jobs tab, you can access comprehensive metrics on job performance, including daily job counts, failure rates, and user activity. Visualizations include graphs of completed and failed jobs, job states, and the 10 longest-running jobs, providing an overview of job execution and performance trends.

We recommend that administrators frequently review the Monitor page, including daily consumption patterns and the weekly and monthly aggregate. Monitoring insights like the most queried datasets over time can help administrators optimize performance, adapt a Reflection strategy, and leverage the jobs-per-engine distribution to improve workload management and resource allocation.

### Perform Impact Analysis if Security Rules Change

Dremio’s control plane interacts with your own virtual private clouds for query execution. If you make changes to your security rules after they are initially set and working correctly with Dremio, perform impact analysis to make sure that your connectivity with Dremio remains unaffected.

Was this page helpful?

* Principles
  + Set Engine Routing Rules and Engine Settings
  + Monitor and Measure Platform Activity
* Best Practices
  + Initialize Engine Routing and Engine Settings
  + Use the Monitor Page in the Dremio Console
  + Perform Impact Analysis if Security Rules Change

<div style="page-break-after: always;"></div>

# Cost Optimization | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/well-architected-framework/cost-optimization

On this page

Although it's important to get the best performance possible with Dremio, it's also important to optimize costs associated with managing the Dremio platform.

## Principles

### Minimize Running Executor Nodes

Dremio can scale to many hundreds of nodes, but any given engine should have only as many nodes as are required to satisfy the current load and meet service-level agreements.

### Dynamically Scale Executor Nodes Up and Down

When running Dremio engines, designers can leverage concurrency per replica and minimum and maximum number of replicas to dynamically expand and contract capacity based on load.

### Eliminate Unnecessary Data Processing

As described in the [best practices for Pillar 2: Performance Efficiency](/dremio-cloud/help-support/well-architected-framework/performance-efficiency#leverage-reflections-to-improve-performance), creating too many Reflections, especially those that perform similar work to other Reflections or provide little added benefit in terms of query performance, can incur unnecessary costs because Reflections need system resources to rebuild. For this reason, consider removing any unnecessary Reflections.

To avoid the need to process data that is not required for a query to succeed, use filters that can be pushed down to the source wherever possible. Enabling partitioning on source data that are in line with the filters also helps speed up data retrieval.

Also, optimize source data files by merging smaller files or splitting larger files whenever possible.

## Best Practices

### Size Engines to the Minimum Replicas Required

To avoid accruing unnecessary cost, reduce the number of active replicas in your engines to the minimum (typically 1, but 0 when the engine is not in use on weekends or non-business hours). A minimum replica count of 0 delays the first query of the day due to engine startup, which you can mitigate with an external script that executes a dummy SQL statement prior to normal daily use.

### Remove Unused Reflections

Analyze the results in Dremio `sys.project.jobs_recent` system table along with the results for the system tables [`sys.project.reflections`](/dremio-cloud/sql/system-tables/reflections) and [`sys.project.materializations`](/dremio-cloud/sql/system-tables/materializations) to get information about the frequency at which each Reflection present in Dremio is leveraged. You can further analyze Reflections that are not being leveraged to determine if any are still being refreshed, and if they are, how many times they have been refreshed in the reporting period and how many hours of cluster execution time they have been consuming.

Checking for and removing unused Reflections is good practice because it can reduce clutter in the Reflection configuration and often free up many hours of cluster execution cycles that can be used for more critical workloads.

### Optimize Metadata Refresh Frequency

Ensure metadata-refresh frequencies are set appropriately based on what you know about the frequency that metadata is changing in the data source.

The default metadata refresh frequency set against data sources is once per hour, which is too frequent for many data sources. For example, if data in the sources are only updated once every 6 hours, it is not necessary to refresh the data sets every hour. Instead, change the refresh schedule to every 6 hours in the data source settings.

Furthermore, because metadata refreshes can be scheduled at the data source level, overridden at each individual table level, and performed programmatically, it makes sense to review each new data source to determine the most appropriate setting for it. For example, for data lake sources, you might set a long metadata refresh schedule such as 3000 weeks so that the scheduled refresh is very unlikely to fire, and then perform the refresh programmatically as part of the extract, transform, and load (ETL) process, where you know when the data generation has completed. You might set relational data sources to refresh every few days, but then override the source-level setting for tables that change more frequently.

When datasets are updated as part of overnight ETL runs, it doesn’t make sense to refresh the dataset metadata until you know the ETL process is finished. In this case, you can create a script that triggers the manual refresh of each dataset in the ETL process after you know the dataset ETL is complete.

For data sources that contain a large number of datasets but few datasets that change their structure or have new files added, it makes little sense to refresh at the source level on a fixed schedule. Instead, set the metadata to a long source-level refresh timeframe like 52 weeks and use scripts to trigger a manual refresh against a specific dataset.

If you set the metadata refresh schedule for a long timeframe and you do not have any scripting mechanism to refresh your metadata, when a query runs and the planner notices that the metadata is stale or invalid, Dremio performs an inline metadata refresh during the query planning phase. This can have a negative impact on the duration of query execution because it also incorporates that metadata refresh duration.

Was this page helpful?

* Principles
  + Minimize Running Executor Nodes
  + Dynamically Scale Executor Nodes Up and Down
  + Eliminate Unnecessary Data Processing
* Best Practices
  + Size Engines to the Minimum Replicas Required
  + Remove Unused Reflections
  + Optimize Metadata Refresh Frequency

<div style="page-break-after: always;"></div>

# Operational Excellence | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/well-architected-framework/operational-excellence

On this page

Following a regular schedule of maintenance tasks is key to keeping your Dremio project operating at peak performance and efficiency. The operational excellence pillar describes the tasks required to maintain an operationally healthy Dremio project.

## Principles

### Regularly Evaluate Engine Resources

As workloads expand and grow on your Dremio project, it is important to evaluate engine usage to ensure that you have correctly sized engines and the right number of replicas.

### Regularly Evaluate Query Performance

Regular query performance reviews help you identify challenges and mitigate them before they become a problem. For example, if you find an unacceptably large number of queries waiting on engine or replica starts, you can adjust the minimum, maximum, and last replica auto-stop settings. If you see an unacceptable number of query execution failures, you can adjust concurrency limits per replica more appropriately or revisit the semantic layer and introduce Reflections to improve performance.

### Clean Up Tables with Vacuum

Open Catalog automates Iceberg maintenance operations like compaction and vacuum, which maximizes query performance, minimizes storage costs, and eliminates the need to run manual data maintenance.

### Optimize Tables

When operating on Iceberg tables and using Open Catalog, you can schedule [optimization](/dremio-cloud/developer/data-formats/iceberg#optimization) jobs to help you manage the accumulation of data files that occurs through data manipulation language (DML) operations. Regular maintenance ensures optimal query performance on these tables.

### Regularly Monitor Live Metrics for Dremio

To ensure smooth operations in Dremio, collect metrics and take action when appropriate. Read [Monitor](/dremio-cloud/admin/monitor/) for more details.

## Best Practices

### Optimize Workload Management Rules

Because workloads and volumes of queries change over time, you should periodically reevaluate workload management engine routing rules and engines and adjust for optimal size, concurrency, and replica limits.

### Configure Engines

When possible, leverage engines to segregate workloads. Configuring engine and usage offers the following benefits:

* Platform stability: if one engine goes down, it won’t affect other engines.
* Flexibility to start and stop engines on demand at certain times of day.
* Engines can be sized differently based on workload patterns.
* It's possible to separate queries from different tenants into their own engine to enable a chargeback model.

We recommend separate engines for the following types of workloads:

* Reflection refreshes.
* Metadata refreshes.
* API queries.
* Queries from BI tools.
* Extract, transform, and load (ETL)-type workloads like CREATE TABLE AS (CTAS) and Iceberg DML.
* Ad hoc data science queries with long execution times.

In multi-tenant environments like multiple departments or geographic locations where chargeback models can be implemented for resource usage, we recommend having a separate set of engines per tenant.

### Optimize Query Performance

When developing the semantic layer, it is best to create the views in each of the three layers according to best practices without using Reflections, then test queries of the application layer views to gauge baseline performance.

For queries that appear to be running sub-optimally, we recommend analyzing the query profile to determine whether any bottlenecks can be removed to improve performance. If performance issues persist, place Reflections where they will have the most benefit. A well-architected semantic layer allows you to place Reflections at strategic locations in the semantic layer such that large volumes of queries benefit from the fewest number of Reflections, such as in the business layer where a view is constructed by joining several other views.

### Design Reflections for Expensive Query Patterns

1. Review query history (jobs) to determine the most expensive and most-frequent queries being submitted.
2. Look in the job profiles for these queries. Tables and views referenced by multiple queries that perform expensive scans, joins, and aggregations are good candidates for Reflections.
3. Examine the SQL for the selected queries that reference the same table or view to find patterns that can help you define a Reflection on that table or view that satisfies as many of those queries as possible.

### Avoid the “More Is Always Better” Approach

Creating more Reflections than are necessary to support your data consumers can lead to the use of more resources than might be optimal for your environment, both in terms of system resources and the time and attention devoted to working with them.

### Establish Criteria for When to create Reflections

Create them only when data consumers are experiencing slow query responses, or when reports are not meeting established SLAs.

### Create Reflections Without Duplicating the Work of Other Reflections

Dremio recommends that, when you create tables and views, you create them in layers:

* The bottom or first layer consists of your tables.
* In the second layer are views, one for each table, that do lightweight preparation of data for views in the next layers. Here, administrators might create views that do limited casting, type conversion, and field renaming, and redacting sensitive information, among other prepping operations. Administrators can also add security by subsetting both rows and fields that users in other layers are not allowed to access. The data has been lightly scrubbed and restricted to the group of people who have the business knowledge that lets them use these views to build higher-order views that data consumers can use. Then, admins grant access to these views to users who create views in the next layer, without being able to see the raw data in the tables.
* In the third layer, users create views that perform joins and other expensive operations. This layer is where the intensive work on data is performed. These users then create Reflections (raw, aggregation, or both) from their views.
* In the fourth layer, users can create lightweight views for dashboards, reports, and visualization tools. They can also create aggregation Reflections, as needed.

### Establish a Routine for Checking How often Reflections Are Used

At regular intervals, check for Reflections that are no longer being used by the query planner and evaluate whether they should be removed. Query patterns can change over time, and frequently-used Reflections can gradually become less relevant.

### Use Supporting Anchors

Anchors for Reflections are views that data consumers have access to from their business-intelligence tools. As you develop a better understanding of query patterns, you might want to support those patterns by creating Reflections from views that perform expensive joins, transformations, filters, calculations, or a combination of those operations. You would probably not want data consumers to be able to access those views directly in situations where the query optimizer did not use any of the Reflections created from those views. Repeated and concurrent queries on such views could put severe strain on system resources.

You can prevent queries run by data consumers from accessing those views directly. Anchors that perform expensive operations and to which access is restricted are called supporting anchors.

For example, suppose that you find these three, very large tables are used in many queries:

* Customer
* Order
* Lineitem

You determine that there are a few common patterns in the user queries on these tables:

* The queries frequently join the three tables together.
* Queries always filter by `commit_date < ship_date`
* There is a calculated field in most of the queries: `extended_price * (1-discount) AS revenue`

You can create a view that applies these common patterns, and then create a raw Reflection to accelerate queries that follow these patterns.

First, you create a folder in the Dremio space that your data consumers have access to. Then, you configure this folder to be invisible and inaccessible to the data consumers.

Next, you write the query to create the view, you follow these guidelines:

* Use `SELECT *` to include all fields, making it possible for the query optimizer to accelerate the broadest set of queries. Alternatively, if you know exactly which subset of fields are used in the three tables, you can include just that subset in the view.
* Add any calculated fields, which in this case is the revenue field.
* Apply the appropriate join on the three tables.
* Apply any filters that are used by all queries, which in this case is only `commit_date < ship_date`.
* Always use the most generic predicate possible to maximize the number of queries that will match.

Next, you run the following query to create a new view:

Create a new view

```
SELECT *, extendedprice * (1 - discount) AS revenue FROM customer AS c, orders AS o, lineitem AS l WHERE c.c_custkey = o.o_custkey AND l.l_orderkey = o.o_orderkey AND o.commit_date < o.ship_date
```

Then, you save the view in the folder that you created earlier.

Finally, you create one or more raw Reflections on this new supporting anchor. If most of the queries against the view were aggregation queries, you could create an aggregation Reflection. In both cases, you can select fields, as needed, to sort on or partition on.

The result is that, even though the data consumers do not have access to the supporting anchor, Dremio can accelerate their queries by using the new Reflections as long as they have access to the tables that the Reflections are ultimately derived from: Customer, Order, and Lineitem.

If the query optimizer should determine that a query cannot be satisfied by any of the Reflections, it is possible, if no other views can satisfy it, for the query to run directly against the tables, as is always the case with any query.

### Horizontally Partition Reflections that Have Many Rows

If you select a field for partitioning in a data Reflection, Dremio physically groups records together into a common directory on the file system. For example, if you partition by the field Country, in which the values are two-letter abbreviations for the names of countries, such as US, UK, DE, and CA, Dremio stores the data for each country in a separate directory named US, UK, DE, CA, and so on. This optimization allows Dremio to scan a subset of the directories based on the query, which is an optimization called partition pruning.

If a user queries on records for which the value of Country is US or UK, then Dremio can apply partition pruning to scan only the US and UK directories, significantly reducing the amount of data that is scanned for the query.

When you are selecting a partitioning field for a data Reflection, ask yourself these questions:

1. Is the field used in many queries?
2. Are there relatively few unique values in the field (low cardinality)?

To partition the data, Dremio must first sort all records, which consumes resources. Accordingly, partition data only on fields that can be used to optimize queries. In addition, the number of unique values for a field should be relatively small, so that Dremio creates only a relatively small number of partitions. If all values in a field are unique, the cost to partition outweighs the benefit.

In general, Dremio recommends the total number of partitions for a Reflection to be less than 10,000.

Because Reflections are created as Apache Iceberg tables, you can use partition transforms to specify transformations to apply to partition columns to produce partition values. For example, if you choose to partition on a column of timestamps, you can set partition transforms that produce partition values that are the years, months, days, or hours in those timestamps. The following table lists the partition transforms that you can choose from.

note

* If a column is listed as a partition column, it cannot also be listed as a sort column for the same Reflection.
* In aggregation Reflections, each column specified as a partition column or used in transform must also be listed as a dimension column.
* In raw Reflections, each column specified as a partition column or used in transform must also be listed as a display column.

Value | Type of Partition Transform | Description || IDENTITY | identity(<column\_name>) | Creates one partition per value. This is the default transform. If no transform is specified for a column named by the `name` property, an IDENTITY transform is performed. The column can use any supported data type. |
| YEAR | year(<column\_name>) | Partitions by year. The column must use the DATE or TIMESTAMP data type. |
| MONTH | month(<column\_name>) | Partitions by month. The column must use the DATE or TIMESTAMP data type. |
| DAY | day(<column\_name>) | Partitions on the equivalent of dateint. The column must use the DATE or TIMESTAMP data type. |
| HOUR | hour(<column\_name>) | Partitions on the equivalent of dateint and hour. The column must use the TIMESTAMP data type. |
| BUCKET | bucket(<integer>, <column\_name>) | Partitions data into the number of partitions specified by an integer. For example, if the integer value N is specified, the data is partitioned into N, or (0 to (N-1)), partitions. The partition in which an individual row is stored is determined by hashing the column value and then calculating `<hash_value> mod N`. If the result is 0, the row is placed in partition 0; if the result is 1, the row is placed in partition 1; and so on.  The column can use the DECIMAL, INT, BIGINT, VARCHAR, VARBINARY, DATE, or TIMESTAMP data type. |
| TRUNCATE | truncate(<integer>, <column\_name>) | If the specified column uses the string data type, truncates strings to a maximum of the number of characters specified by an integer. For example, suppose the specified transform is truncate(1, stateUS). A value of `CA` is truncated to `C`, and the row is placed in partition C. A value of `CO` is also truncated to `C`, and the row is also placed in partition C.   If the specified column uses the integer or long data type, truncates column values in the following way: For any `truncate(L, col)`, truncates the column value to the biggest multiple of L that is smaller than the column value. For example, suppose the specified transform is `truncate(10, intColumn)`. A value of 1 is truncated to 0 and the row is placed in the partition 0. A value of 247 is truncated to 240 and the row is placed in partition 240. If the transform is `truncate(3, intColumn)`, a value of 13 is truncated to 12 and the row is placed in partition 12. A value of 255 is not truncated, because it is divisble by 3, and the row is placed in partition 255.  The column can use the DECIMAL, INT, BIGINT, VARCHAR, or VARBINARY data type.  **Note:** The truncate transform does not change column values. It uses column values to calculate the correct partitions in which to place rows. |

### Partition Reflections to Allow for Partition-Based Incremental Refreshes

Incremental refreshes of data in Reflections are much faster than full refreshes. Partition-based incremental refreshes are based on Iceberg metadata that is used to identify modified partitions and to restrict the scope of the refresh to only those partitions. For more information about partition-based incremental refreshes, see Types of Refresh for Reflections on Apache Iceberg Tables, Filesystem Sources, Glue Sources, and Hive Sources in [Refresh Reflections](/dremio-cloud/admin/performance/manual-reflections/reflection-refresh).

For partition-based incremental refreshes, both the base table and its Reflections must be partitioned, and the partition transforms that they use must be compatible. The following table lists which partition transforms on the base table and which partition transforms on Reflections are compatible:

| Partition Transform on the Base Table | Compatible Partition Transforms on Reflections |
| --- | --- |
| Identity | Identity, Hour, Day, Month, Year, Truncate |
| Hour | Hour, Day, Month, Year |
| Day | Day, Month, Year |
| Month | Month, Year |
| Year | Year |
| Truncate | Truncate |

note

* If both a base table and a Reflection use the Truncate partition transform, follow these rules concerning truncation lengths:
  + If the partition column uses the String data type, the truncation length used for the Reflection must be less than or equal to the truncation length used for the base table.
  + If the partition column uses the Integer data type, the remainder from the truncation length on the Reflection (A) divided by the truncation length on the base table (B) must be equal to 0: `A MOD B = 0`
  + If the partition column uses any other data type, the truncation lengths must be identical.
* If a base table uses the Bucket partition transform, partition-based incremental refreshes are not possible.

#### Partition Aggregation Reflections on Timestamp Data in Very Large Base Tables

Suppose you want to define an aggregation Reflection on a base table that has billions of rows. The base table includes a column that either uses the TIMESTAMP data type or includes a timestamp as a string, and the base table is partitioned on that column.

In your aggregation Reflection, you plan to aggregate on timestamp data that is in the base table. However, to get the benefits of partition-based incremental refresh, you need to partition the Reflection in a way that is compatible with the partitioning on the base table. You can make the partitioning compatible in either of two ways:

* By defining a view on the base table, and then defining the aggregation Reflection on that view
* By using the advanced Reflection editor to define the aggregation Reflection on the base table

##### Define an Aggregation Reflection on a View

If the timestamp column in the base table uses the TIMESTAMP data type, use one of the functions in this table to define the corresponding column in the view. You can partition the aggregation Reflection on the view column and use the partition transform that corresponds to the function.

| Function in View Definition | Corresponding Partition Transform |
| --- | --- |
| DATE\_TRUNC('HOUR', <base\_table\_column>) | HOUR(<view\_col>) |
| DATE\_TRUNC('DAY', <base\_table\_column>) | DAY(<view\_col>) |
| DATE\_TRUNC('MONTH', <base\_table\_column>) | MONTH(<view\_col>) |
| DATE\_TRUNC('YEAR', <base\_table\_column>) | YEAR(<view\_col>) |
| CAST <base\_table\_column> as DATE | DAY(<view\_col>) |
| TO\_DATE(<base\_table\_column>) | DAY(<view\_col>) |

If the timestamp column in the base table uses the STRING data type, use one of the functions in this table to define the corresponding column in the view. You can partition the aggregation Reflection on the view column and use the partition transform that corresponds to the function.

| Function in View Definition | Corresponding Partition Transform |
| --- | --- |
| LEFT(<base\_table\_column>, X) | TRUNCATE(<view\_col>, X) |
| SUBSTR(<base\_table\_column>, 0, X) | TRUNCATE(<view\_col>, X) |
| SUBSTRING(<base\_table\_column>, 0, X) | TRUNCATE(<view\_col>, X) |

##### Define an Aggregation Reflection on a Base Table

When creating or editing the aggregation Reflection in the Advanced View, as described in [Manual Reflections](/dremio-cloud/admin/performance/manual-reflections/), follow these steps:

1. Set the base table's timestamp column as a dimension.

![Setting the column as a dimension.](/images/date-granularity-1.png "Setting the column as a dimension.")

2. Click the down-arrow next to the green circle.
3. Select **Date** for the date granularity.

![Selecting the granularity.](/images/date-granularity-2.png "Selecting the granularity.")

### Use Dimmensions with Low Cardinality

Use dimensions that have relatively low cardinality in a table or view. The higher the cardinality of a dimension, the less benefit an aggregation Reflection has on query performance. Lower cardinality aggregation Reflections require less time to scan.

### Create One Aggregation Reflection for Each Important Subset of Dimensions

* For a single table or view, create one aggregation Reflection for each important subset of dimensions in your queries, rather than one aggregation Reflection that includes all dimensions. Multiple small aggregation Reflections (versus one large one) are good for isolated pockets of query patterns on the same table or view that do not overlap. If your query patterns overlap, use fewer larger aggregation Reflections.

  There are two cautions that accompany this advice, however:

  + Be careful of creating aggregation Reflections that have too few dimensions for your queries.

    If a query uses more dimensions than are included in an aggregation Reflection, the Reflection cannot satisfy the query and the query optimizer does not run the query against it.
  + Be careful of creating more aggregation Reflections than are necessary to satisfy queries against a table or view.

    The more Reflections you create, the more time the query optimizer requires to plan the execution of queries. Therefore, creating more aggregation Reflections than you need can slow down query performance, even if your aggregation Reflections are low-cardinality.

### Sort Reflections on High-Cardinality Fields

The sort option is useful for optimizing queries that use filters or range predicates, especially on fields with high cardinality. If sorting is enabled, during query execution, Dremio skips over large blocks of records based on filters on sorted fields.

Dremio sorts data during the execution of a query if a Reflection spans multiple nodes and is composed of multiple partitions.

Sorting on more than one field in a single data Reflection typically does not improve read performance significantly and increases the costs of maintenance tasks.

For workloads that need sorting on more than one field, consider creating multiple Reflections, each being sorted on a single field.

### Create Reflections from Joins that are Based on Joins from Multiple Queries

Joins between tables, views, or both tend to be expensive. You can reduce the costs of joins by performing them only when building and refreshing Reflections.

As an administrator, you can identify a group of queries that use similar joins. Then, you can create a general query that uses a join that is based on the similar joins, but does not include any additional predicates from the queries in the group. This generic query can serve as the basis of a raw Reflection, an aggregation Reflection, or both.

For example, consider the following three queries which use similar joins on views A, B and C:

Three queries with joins on views A, B, and C

```
SELECT a.col1, b.col1, c.col1 FROM a join b on (a.col4 = b.col4) join c on (c.col5=a.col5)  
  WHERE a.size = 'M' AND a.col3 > '2001-01-01' AND b.col3 IN ('red','blue','green')  
SELECT a.col1, a.col2, c.col1, COUNT(b.col1) FROM a join b on (a.col4 = b.col4) join c on (c.col5=a.col5)  
  WHERE a.size = 'M' AND b.col2 < 10 AND c.col2 > 2 GROUP BY a.col1, a.col2, c.col1  
SELECT a.col1, b.col2 FROM a join b on (a.col4 = b.col4) join c on (c.col5=a.col5)  
  WHERE c.col1 = 123
```

You can write and run this generic query to create a raw Reflection to accelerate all three original queries:

Create a Reflection to accelerate three queries

```
SELECT a.col1 , a.col2, a.col3, b.col1, b.col2, b.col3, c.col1, c.col2 FROM a join b on (a.col4 = b.col4) join c on (c.col5=a.col5)
```

### Time Reflection Refreshes to Occur After Metadata Refreshes of Tables

Time your refresh Reflections to occur only after the metadata for their underlying tables is refreshed. Otherwise, Reflection refreshes do not include data from any files that were added to a table since the last metadata refresh, if any files were added.

For example, suppose a data source that is promoted to a table consists of 10,000 files, and that the metadata refresh for the table is set to happen every three hours. Subsequently, Reflections are created from views on that table, and the refresh of Reflections on the table is set to occur every hour.

Now, one thousand files are added to the table. Before the next metadata refresh, the Reflections are refreshed twice, yet the refreshes do not add data from those one thousand files. Only on the third refresh of the Reflections does data from those files get added to the Reflections.

### Rotation Personal Access Tokens

When Dremio [personal access tokens (PATs)](/dremio-cloud/security/authentication/personal-access-token/) are used in custom applications, consider scripting an automated periodic refresh to avoid job failures when the PATs expire.

### Monitor Dremio Projects

It's important to set up a good monitoring solution to maximize your investment in Dremio and identify and resolve issues related to Dremio projects before they have a broader impact on workload. Your monitoring solution should ensure overall cluster health and performance.

Was this page helpful?

* Principles
  + Regularly Evaluate Engine Resources
  + Regularly Evaluate Query Performance
  + Clean Up Tables with Vacuum
  + Optimize Tables
  + Regularly Monitor Live Metrics for Dremio
* Best Practices
  + Optimize Workload Management Rules
  + Configure Engines
  + Optimize Query Performance
  + Design Reflections for Expensive Query Patterns
  + Avoid the “More Is Always Better” Approach
  + Establish Criteria for When to create Reflections
  + Create Reflections Without Duplicating the Work of Other Reflections
  + Establish a Routine for Checking How often Reflections Are Used
  + Use Supporting Anchors
  + Horizontally Partition Reflections that Have Many Rows
  + Partition Reflections to Allow for Partition-Based Incremental Refreshes
  + Use Dimmensions with Low Cardinality
  + Create One Aggregation Reflection for Each Important Subset of Dimensions
  + Sort Reflections on High-Cardinality Fields
  + Create Reflections from Joins that are Based on Joins from Multiple Queries
  + Time Reflection Refreshes to Occur After Metadata Refreshes of Tables
  + Rotation Personal Access Tokens
  + Monitor Dremio Projects

<div style="page-break-after: always;"></div>

# Performance Efficiency | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/well-architected-framework/performance-efficiency

On this page

Dremio is a powerful massively parallel processing (MPP) platform that can process terabyte-scale datasets. To get the best performance from your Dremio environment, follow these design principles and best practices for implementation.

## Dimensions of Performance Optimization

When optimizing Dremio, several factors can affect workload and project performance. Queries submitted to Dremio must be planned on the control plane before being routed for execution. The resource requirements and degree of optimization of individual queries can vary widely. Those queries can be rewritten and optimized on their own without regard to a larger engine.

Beyond individual queries, executor nodes have individual constraints of memory and CPU. Executors in Dremio are also part of an engine that groups executors together to process queries in parallel across multiple machines. The size of the engine that a query runs on can affect its performance. To enhance the ability to handle additional queries beyond certain concurrency thresholds, configure replicas for the engine.

These dimensions of performance optimization can be simplified in the following decision tree, which addresses the most common scenarios. In the decision tree, `engine_start_epoch_millis > 0` implies that the engine is down.

![Decision tree diagram that shows common performance optimization scenarios for Dremio.](/images/cloud/optimization-decision-tree.png "Dremio performance optimization scenarios")

## Principles

### Perform Regular Maintenance

Conduct regular maintenance to ensure that your project is set up for optimal performance and can handle more data, queries, and workloads. Regular maintenance will establish a solid baseline from which you can design and optimize. Dremio can be set up to automatically optimize and vacuum tables in your Open catalog.

### Optimize Queries for Efficiency

Before worrying about scaling out your engines, it is important to optimize your semantic layer and queries to be as efficient as possible. For example, if there are partition columns, you should use them. Create sorted or partitioned Reflections. Follow standard SQL writing best practices such as applying functions to values rather than columns in where clauses.

### Optimize Engines

Dremio provides several facilities to allow workload isolation and ensure your queries do not overload the engines. Multiple engines are used to keep some queries from affecting others and concurrency rules are used to buffer queries to prevent overloading any one particular engine.

## Best Practices

### Design Semantic Layer for Workload Performance

Dremio’s enterprise-scale semantic layer clearly defines the boundary between your physically stored tables and your logical, governed, and self-service views. The semantic layer seamlessly allows data engineers and semantic data modelers to create views based on tables without having to make copies of the physical data.

Since interactive performance for business users is a key capability of the semantic layer, when appropriate, Dremio can leverage physically optimized representations of source data known as [Reflections](/dremio-cloud/admin/performance/autonomous-reflections). When queries are made against views that have Reflections enabled, the query optimizer can accelerate a query by using one or more Reflections to partially or entirely satisfy that query rather than processing the raw data in the underlying data source. Queries do not have to be rewritten to take advantage of Reflections. Instead, Dremio's optimizer automatically considers Reflection suitability while planning the query.

With Dremio, you can create layers of views that allow you to present data to business consumers in a format they need while satisfying the security requirements of the organization. Business consumers do not need to worry about which physical locations the data comes from or how the data is physically organized. A layered approach allows you to create sets of views that can be reused many times across multiple projects.

Leveraging Dremio’s layering best practices promotes a more-performant, low-maintenance solution that can provide agility to development teams and business users as well as better control over data.

### Improve the Performance of Poor-Performing Queries

Run `SELECT * FROM sys.project.jobs_recent` to analyze the query history and determine which queries are performing sub-optimally. This allows you to consider a number of factors, including the overall execution time of a query. Identify the 10 longest-running queries to understand why they are taking so long. For example, is it the time taken to read data from the source, lacking CPU cycles, query spilling to disk, query queued at the start, or another issue? Did the query take a long time to plan?

note

Read [Query Performance Analysis and Improvement](https://www.dremio.com/wp-content/uploads/2024/01/Query-Performance-Analysis-and-Improvement.pdf) for details about query performance analysis techniques. This white paper was developed based on Dremio Software, but the content applies equally to Dremio.

The query history also allows you to focus on planning times. You should also investigate queries to pinpoint high planning time, which could be due to the complexity of the query (which you can address by rewriting the query) or due to many Reflections being considered (which indiciates that too many Reflections are defined in the environment). Read [Remove Unused Reflections](/dremio-cloud/help-support/well-architected-framework/cost-optimization#remove-unused-reflections) for more information about identifying redundant Reflections in your Dremio project.

The query history also allows you to focus on metadata refresh times, which could be due to inline metadata refresh. Read [Optimize Metadata Refresh Frequency](/dremio-cloud/help-support/well-architected-framework/cost-optimization#optimize-metadata-refresh-frequency) for more information about checking metadata refresh schedules.

Sometimes, query performance is inconsistent. A query may complete execution in less than 10 seconds in one instance but require 1 minute of execution time in another instance. This is a sign of resource contention in the engine, which can happen in high-volume environments or when too many jobs (including user queries, metadata, and reflections) are running at the same time. We recommend having separate, dedicated engines for metadata refreshes, Reflection refreshes, and user queries to reduce the contention for resources when user queries need run concurrently with refreshes.

For Reflection jobs that require excessive memory, we recommend two Reflection refresh engines of different sizes, routing the Reflections that require excessive memory to the larger engine. This is typically needed for Reflections on views that depend on the largest datasets and can be done with the [ALTER TABLE ROUTE REFLECTIONS](/dremio-cloud/sql/commands/alter-table/) command.

### Read Dremio Profiles to Pinpoint Bottlenecks

Dremio job profiles contain a lot of fine-grained information about how a query was planned, how the phases of execution were constructed, how the query was actually executed, and the decisions made about whether to use Reflections to accelerate the query.

For each phase of the query that is documented in the job profile, check the start and end times of the phase for an initial indication of the phase in which any bottlenecks are located. After you identify the phase, check the operators of that phase to identify which operator or thread within the operator may have been the specific bottleneck. This information usually helps determine why a query performs sub-optimally so that you can plan improvements. Reasons for bottlenecks and potential improvement options include:

* High metadata retrieval times from inline metadata refresh indicate that you should revisit metadata refresh settings.
* High planning time can be caused by too many Reflections or may mean that a query is too complex and should be rewritten.
* High engine start times indicate that the engine is down. The enqueued time may include replica start time. You may be able to mitigate these issues with minimum replica and last replica auto-stop settings.
* High setup times in table functions indicate overhead due to opening and closing too many small files. High wait times indicate that there is a network or i/o delay in reading the data. High sleep times in certain phases could indicate CPU contention.

note

Read [Reading Dremio Job Profiles](https://www.dremio.com/wp-content/uploads/2024/01/Reading-Dremio-Job-Profiles.pdf) for details about job profile analysis techniques. This white paper was developed based on Dremio Software, but the content applies equally to Dremio.

### Engine Routing and Workload Management

Since the workloads and volumes of queries change over time, reevaluate engine routing settings, engine sizes, engine replicas, and concurrency per replica and adjust as needed to rebalance the proportion of queries that execute concurrently on a replica of an engine.

### Right-Size Engines and Executors

Analyze the query history to determine whether a change in the number of executors in your engines is necessary.

When the volume of queries being simultaneously executed by the current set of executor nodes in an engine starts to reach a saturation point, Dremio exhibits several symptoms. Saturation point is typically manifested as increased sleep time during query execution. Sleep time is incurred when a running query needs to wait for available CPU cycles due to all available CPUs being in operation. Another symptom is an increased number of queries spilling to disk or out-of-memory exceptions.

You can identify these symptoms by analyzing the system table by running `SELECT * FROM sys.project.jobs_recent`. The resulting table lists query execution times, planning time, engine start times, enqueued times, and job failure.

Failure to address these symptoms can result in increasing query failures, increasing query times, and queries spilling to disk, which in turn lead to a bad end-user experience and poor satisfaction. Spilling to disk ensures that a query succeeds because some of its high-memory-consuming operations are processed via local disks. This reduces the memory footprint of the query significantly, but the trade-off is that the query inevitably runs more slowly.

You can alleviate these issues by adding replicas to the engine and reducing concurrency per replica and adding a larger engine, then altering the engine routing rules to route some of the workload to the new engine. Remember that a query executes on the nodes of a single replica or an engine, not across multiple replicas or multiple engines.

A good reason to create a new engine is when a new workload is introduced to your Dremio project, perhaps by a new department within an organization, and the queries cause the existing engine setup to degrade in performance. Creating a new engine to isolate the new workload, most likely by creating rules to route queries from users in that organization to the new engine, is a useful way of segregating workloads.

### Leverage Reflections to Improve Performance

When developing use cases in Dremio’s semantic layer, it’s often best to build out the use case iteratively without any Reflections to begin with. Then, as you complete iterations, run the queries and analyze the data in the query history to deduce which queries take the longest to execute and whether any common factors among a set of slow queries are contributing to the slowness.

For example, if a set of five slow queries are each derived from a view that contains a join between two relatively large tables, you might find that adding a raw Reflection on the view that is performing the join helps to speed up all five queries because doing so creates an Apache Iceberg materialization of the join results, which is automatically used to accelerate views derived from the join. This provides the query planning and performance benefits of Apache Iceberg and allows you to partition the Reflection to accelerate queries for which the underlying data weren't initially optimized. This is an important pattern because it means you can leverage a small number of Reflections to speed up many workloads.

Raw Reflections can be useful when you have large volumes of JSON or CSV data. Querying such data requires processing the entire data set, which can be inefficient. Adding a raw Reflection over the JSON or CSV data again allows for an Apache Iceberg representation of that data to be created and opens up all of the planning and performance benefits that come along with it.

Another use of raw Reflections is to offload heavy queries from an operational data store. Often, database administrators do not want their operational data stores (for example, online transaction processing databases) overloaded with analytical queries while they are busy processing billions of transactions. In this situation, you can leverage Dremio raw Reflections again to create an Apache Iceberg representation of the operational table. When a query comes in that needs the data, Dremio reads the Reflection data instead of going back to the operational source.

Another very important use case that often requires raw Reflections is when you join on-premises data to cloud data. In this situation, retrieving the on-premises data often becomes a bottleneck for queries due to the latency in retrieving data from the source system. Leveraging a default raw Reflection on the view where the data is joined together often yields significant performance gains.

If you have connected Dremio to client tools that issue different sets of GROUP BY queries against a view, and the GROUP BY statements take too long to process compared to the desired service level agreement, consider adding an aggregation Reflection to the view to satisfy the combinations of dimensions and measures that are submitted from the client tool.

Read [Best Practices for Creating Raw and Aggregation Reflections](/dremio-cloud/admin/performance/manual-reflections) when you are considering how and where to apply Reflections.

Failing to make use of Dremio Reflections means you could be missing out on significant performance enhancements for some of your poorest-performing queries. However, creating too many Reflections can also have a negative impact on the system as a whole. The misconception is often that more Reflections must be better, but when you consider the overhead in maintaining and refreshing Reflections at intervals, Reflection refreshes can end up stealing valuable resources from your everyday workloads, especially if you have not created a dedicated Reflection refresh engine.

Where possible, organize your queries by pattern. The idea is to create as few Reflections as possible to service as many queries as possible, so finding points in the semantic tree through which many queries go can help you accelerate a larger number of queries. The more Reflections you have that may be able to accelerate the same query patterns, the longer the planner takes to evaluate which Reflection is best suited for accelerating the query being planned.

### Optimize Metadata Refresh Performance

Add a dedicated metadata refresh engine to your Dremio project. This ensures that all metadata refresh activities for Parquet, Optimized Row Columnar (ORC), and Avro datasets that are serviced by executors are completed in isolation from any other workloads and prevents problems with metadata refresh workloads taking CPU cycles and memory away from business-critical workloads. This gives the refreshes have the best chance of finishing in a timely manner.

Was this page helpful?

* Dimensions of Performance Optimization
* Principles
  + Perform Regular Maintenance
  + Optimize Queries for Efficiency
  + Optimize Engines
* Best Practices
  + Design Semantic Layer for Workload Performance
  + Improve the Performance of Poor-Performing Queries
  + Read Dremio Profiles to Pinpoint Bottlenecks
  + Engine Routing and Workload Management
  + Right-Size Engines and Executors
  + Leverage Reflections to Improve Performance
  + Optimize Metadata Refresh Performance

<div style="page-break-after: always;"></div>

# AI Semantic Layer | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/help-support/well-architected-framework/self-serve-semantic-layer

On this page

Dremio has a unique capability in its AI Semantic Layer, which is where the magic happens in mapping the physical structure of the underlying data storage to how the data is consumed via SQL queries. When you optimally design and maintain the semantic layer, data is more discoverable, writing queries is more straightforward, and performance is optimized.

## Principles

### Layer Views

Layering your views allows you to balance security, performance, and usability. Layered views help you expose the data in your physical tables to external consumption tools in the format the tools require, with proper security and performance. A well-architected semantic layer consists of three layers to organize your views: preparation, business, and application. Each layer serves a purpose in transforming data for consumption by external tools.

### Annotate Datasets to Enhance Discovery and Understanding

You can label and document datasets within Dremio to make data more discoverable and verifiable and allow you to apply governance.

## Best Practices

### Use the Preparation Layer to Map 1-1 to Tables

The preparation layer is closest to the data source. This layer is used to organize and expose only the required datasets from the source rather than all datasets the source contains. In the preparation layer, each view is mapped to the table that it is derived from in the data source, and there are no joins to other views.

Typically, a data engineer is responsible for preparing the data in the preparation layer. The data engineer should apply column aliasing so that all downstream views can use the normalized column names. Casting column data types should also be done in the preparation layer so that all higher-level views can leverage the correct type and conversion is done only once. Data should be cleansed in the preparation layer for central management and to ensure that all downstream views use clean data. Derived columns based on existing columns should be configured in the preparation layer so that all future layers can use the new columns.

### Use the Business Layer to Logically Join Datasets

The business layer provides a holistic view of all data across your catalog or folder. It is the first layer where joins among and between sources should occur. All views in the business layer must be built by either querying resources in the preparation layer or querying other resources in the same business layer.

* Querying resources in the preparation layer: views in the business layer should start with selecting all columns from the preparation layer of that view. This is typically a 1-1 mapping between the preparation and business layer view.
* Querying other resources in the same business layer: when joining two views together, they should be joined from the business layer representation of the view, not the preparation layer. This allows all changes made in the business layer to propagate to all joins.

Use your list of common terms to describe the key business entities in your organization, such as customer, product, and order. Typically, a data modeler works with business experts and data providers to define the views that represent the business entities.

You can create many sub-layers inside the business layer, each consisting of views for different subject areas or verticals. These views are reusable components that can and should be shared across business lines. Typically, views do not filter rows or columns in the business layer; this is deferred to the application layer.

Use the business layer to improve productivity for analytics initiatives and minimize the risk of duplicative efforts in your organization by reducing the cost of service delivery to lines of business, providing a self-service model for data engineers to quickly provision datasets, and enabling data consumers to quickly use and share datasets.

### Use the Application Layer to Arrange Datasets for Consumption

Application layer views are arranged for the needs of data consumers and organizational departments. Typically, data consumers like analysts and data scientists use the views from the business layer and work directly in the application layer to create and modify views in their own dashboards.

If the application layer provides self-service access to Dremio’s AI Semantic Layer, you should expose all business layer views in the application layer at minimum. Even if the view is created by running `SELECT * from BUSINESS_VIEW`, it provides logical separation for security and performance improvements.

If the application layer is not for self-service but for particular applications, the views in the application layer should be built on top of those self-service views in the application layer, adding any application-specific logic. Application logic should be row filters as needed by the application. Columns can be left as-is, and the list of columns the application selects are reduced in the SQL query.

### Leverage Labels to Enhance Searchability

Use Dremio’s [label](/dremio-cloud/manage-govern/wikis-labels) functionality to create and assign labels to tables and views to group related objects and enhance the discoverability of data across your organization. You can search for sets of tables and views based on a label or click on a label in the Dremio console to start a search based on it. Objects can have multiple labels so that they can belong to different logical groups.

### Create Wiki Content to Describe Datasets

Use Dremio’s [wiki](/dremio-cloud/manage-govern/wikis-labels) functionality to add descriptions for catalogs, sources, folders, tables, and views. Wikis enhance understanding of data inside your organization. Wikis allow you to provide context for datasets, such as descriptions for each column, and content that helps users get started with the data, such as usage examples, notes, and points of contact for questions or issues.

Dremio wikis use [GitHub-Flavored Markdown](https://github.github.com/gfm/) and are supported by a rich text editor.

To help eliminate the need for labor-intensive manual classification and cataloging, you can use [generative AI](/dremio-cloud/manage-govern/wikis-labels) to generate labels and wikis for your datasets. Enabling the generative AI feature in Dremio allows you to generate a detailed description of each dataset’s purpose and schema. Dremio's generative AI bases its understanding on your schema and data to produce descriptions of datasets because it can determine how the columns within the dataset relate to each other and to the dataset as a whole.

Was this page helpful?

* Principles
  + Layer Views
  + Annotate Datasets to Enhance Discovery and Understanding
* Best Practices
  + Use the Preparation Layer to Map 1-1 to Tables
  + Use the Business Layer to Logically Join Datasets
  + Use the Application Layer to Arrange Datasets for Consumption
  + Leverage Labels to Enhance Searchability
  + Create Wiki Content to Describe Datasets

<div style="page-break-after: always;"></div>

