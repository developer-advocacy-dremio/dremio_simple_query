# Manage and Govern Your Data | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/manage-govern/

On this page

Data management focuses on the operational efficiency, performance, and reliability of your data at scale. With Dremio’s autonomous management capabilities, many of these processes are intelligently automated; reducing manual effort and ensuring consistent optimization. Dremio automates table optimization by merging small files into optimally sized ones (typically around 512 MB), reducing metadata overhead, and reclaiming storage by physically removing deleted rows. It also reorganizes data to align with clustering specifications, ensuring consistent, high-performance queries across large datasets. Together, these autonomous management features help keep your lakehouse fast, efficient, and cost-effective.

Data governance is the foundation of a secure, reliable, and compliant lakehouse. It ensures that data across your environment is accurate, consistent, and properly controlled throughout its lifecycle. With Dremio, you can implement robust governance practices by maintaining complete data lineage for transparency and auditability, defining role-based and fine-grained (row-access and column-masking) access controls on data, and using documentation and tags to improve data discoverability. Together, these capabilities enable trustworthy, well-governed data that fuels analytics and AI with confidence.

## Autonomous Management

### Optimization

Managing [Apache Iceberg tables](/dremio-cloud/manage-govern/optimization/) is critical to maintaining fast and predictable query performance, especially for agentic AI workloads that demand low latency. As new data is ingested and tables are updated, metadata and small data files accumulate, leading to performance degradation over time. Dremio automates table optimization by merging small files into optimally sized ones (typically ~512 MB), reducing metadata overhead, organizing data to align with clustering specification and reclaiming storage by physically removing deleted rows.

### Clustering

Dremio also reorganizes data to align with [clustering](/dremio-cloud/manage-govern/optimization/) specifications, ensuring consistent, high-performance queries at scale.

### Materialize and Query Rewrite

Dremio can autonomously materialize datasets using Reflections, a precomputed and optimized copy of source data or a query result, designed to speed up query performance. Dremio's query optimizer can accelerate a query against tables or views by using one or more Reflections to partially or entirely satisfy that query, rather than processing the raw data in the underlying data source. Queries do not need to reference Reflections directly. Instead, Dremio rewrites queries on the fly to use the Reflections that satisfy them. For more information, see [Reflections](/dremio-cloud/admin/performance/autonomous-reflections/).

## Governance

### Lineage

Track and visualize how data flows through your lakehouse, from source to consumption. [Lineage](/dremio-cloud/manage-govern/lineage/) helps you understand data origins, track transformations, identify dependencies, and perform impact analysis.

### Wikis

Enrich data understanding by documenting datasets with wikis. Use Generative AI to automatically generate [wikis](/dremio-cloud/manage-govern/wikis-labels/), reducing manual documentation effort. Wikis are used by Dremio's AI Agent to understand the semantics of your environment and adhere to these definitions in response to user prompts.

### Labels

Enhance data discoverability and searchability by categorizing datasets with labels. Use Generative AI to automatically generate [labels](/dremio-cloud/manage-govern/wikis-labels/), reducing manual cataloging effort.

### Role-Based Access Control Policies

Manage access to datasets through [roles](/dremio-cloud/security/roles) rather than individual user grants for easier administration. Assign [privileges](/dremio-cloud/security/privileges) to roles, simplifying management and ensuring users only have access to what they need to perform their job.

### Row-Access and Column-Masking Policies

Apply fine-grained access controls to protect sensitive data using row-access and column-masking policies. Control access to specific rows and columns based on rules and conditions to maintain compliance and adhere to regulatory requirements. For more information, see [Row-Access & Column-Masking Policies](/dremio-cloud/manage-govern/row-column-policies/).

## Related Topics

* [Roles](/dremio-cloud/security/roles) – Manage role-based access control.
* [Explore and Analyze Your Data](/dremio-cloud/explore-analyze/) - Explore and analyze your governed data.
* [Catalog API - Lineage](/dremio-cloud/api/catalog/lineage/) - Retrieve lineage information about datasets.

Was this page helpful?

* Autonomous Management
  + Optimization
  + Clustering
  + Materialize and Query Rewrite
* Governance
  + Lineage
  + Wikis
  + Labels
  + Role-Based Access Control Policies
  + Row-Access and Column-Masking Policies
* Related Topics

<div style="page-break-after: always;"></div>

# Lineage | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/manage-govern/lineage

On this page

Lineage provides a graph of a dataset's relationships (its source, parent datasets, and child datasets) to illustrate how datasets are connected, where the data originates, while tracking its movement and transformations.

By default, the lineage graph focuses on the initially selected dataset and its relationships with other datasets, represented as nodes that display the dataset name and path. To view additional metadata, use the **Show/hide layers** options.

If you wish to track lineage for a different dataset node, the lineage graph needs to be refocused. To refocus the lineage graph on a different dataset, you can either click ![This is the Focus icon.](/images/icons/focus.png "Focus icon") or ![](/images/icons/more.png) on the right of the dataset name, and then select **Focus on this dataset**.

![This is a screenshot showing the option to refocus the lineage graph on a different dataset.](/images/lineage-focus.png "Lineage focus on dataset")

## Privileges Required for Lineage

* If you have the `SELECT` privilege on the parent datasets and the child datasets, you can see the parent datasets and data sources on the left. The child datasets appear on the right.
* If you have only the `READ METADATA` privilege on the parent and child datasets, then you can only see limited metadata for these datasets.
* If you do not have the `SELECT` or the `READ METADATA` privilege on the parent and child datasets, they are not visible.

## Lineage Refresh with Dataset Schema Changes

For datasets in Iceberg REST catalogs, the lineage graphs are stored in Dremio's metadata cache, which is automatically refreshed at fixed time intervals. For more information, see [Metadata Refresh](/dremio-cloud/bring-data/connect/catalogs/iceberg-rest-catalog/#metadata). It is possible that the lineage graph might show an outdated schema for the dataset if the dataset schema has been recently updated and Dremio's metadata cache has not yet been refreshed.

Was this page helpful?

* Privileges Required for Lineage
* Lineage Refresh with Dataset Schema Changes

<div style="page-break-after: always;"></div>

# Automatic Optimization | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/manage-govern/optimization

On this page

As [Apache Iceberg](/dremio-cloud/developer/data-formats/iceberg) tables are written to and updated, data and metadata files accumulate, which can affect query performance. For example, small files produced by data ingestion jobs slow queries because the query engine must read more files.

To optimize performance, Dremio automates table maintenance in the Open Catalog. This process compacts small files into larger ones, partitions data based on the values of a table's columns, rewrites manifest files, removes position delete files, and clusters tables—improving query speed while reducing storage costs.

Automatic optimization runs on a dedicated engine configured by Dremio, ensuring peak performance without impacting project query workloads.

When Dremio optimizes a table, it evaluates file sizes, partition layout, and metadata organization to reduce I/O and metadata overhead. Optimization consists of five main operations: clustering, data file compaction, partition evolution, manifest file rewriting, and position delete files.

## Clustering

Iceberg clustering sorts individual records in data files based on the clustered columns provided in the [`CREATE TABLE`](/dremio-cloud/sql/commands/create-table/) or [`ALTER TABLE`](/dremio-cloud/sql/commands/alter-table/) statement.

To cluster a table, you must first define the clustering keys. Then, automatic optimization uses the clustering keys to optimize tables. For details, see [Clustering](/dremio-cloud/developer/data-formats/iceberg/#clustering).

## Data File Compaction

Iceberg tables that are constantly being updated can have data files of various sizes. As a result, query performance can be negatively affected by sub-optimal file sizes. The optimal file size in Dremio is 256 MB.

Dremio logically combines smaller files and splits larger ones to 256 MB (see the following graphic), helping to reduce metadata overhead and costs related to opening and reading files.

![Optimizing file sizes in Dremio.](/images/file-sizes3.png "Optimizing file sizes in Dremio.")

## Partition Evolution

To improve read or write performance, data is partitioned based on the values of a table's columns. If the columns used in a partition evolve over time, query performance can be impacted when the queries are not aligned with the current segregations of the partition. Dremio detects and rewrites these files to align with the current partition specification. This operation is used:

* When select partitions are queried more often or are of more importance (than others), and it's not necessary to optimize the entire table.
* When select partitions are more active and are constantly being updated. Optimization should only occur when activity is low or paused.

## Manifest File Rewriting

Iceberg uses metadata files (or manifests) to track point-in-time snapshots by maintaining all deltas as a table. This metadata layer functions as an index over a table’s data and the manifest files contained in this layer speed up query planning and prune unnecessary data files. For Iceberg tables that are constantly being updated (such as the ingestion of streaming data or users performing frequent DML operations), the number of manifest files that are suboptimal in size can grow over time. Additionally, the clustering of metadata entries in these files may not be optimal. As a result, suboptimal manifests can impact the time it takes to plan and execute a query.

Dremio rewrites these manifest files quickly based on size criteria. The target size for a manifest file is based on the Iceberg table's property. If a default size is not set, Dremio defaults to 8 MB. For the target size, Dremio considers the range from 0.75x to 1.8x, inclusive, to be optimal. Manifest files exceeding the 1.8x size will be split while files smaller than the 0.75x size will be compacted.

This operation results in the optimization of the metadata, helping to reduce query planning time.

## Position Delete Files

Iceberg v2 added the ability for delete files to be encoded to rows that have been deleted in existing data files. This enables you to delete or replace individual rows in immutable data files without the need to rewrite those files. [Position delete files](https://iceberg.apache.org/spec/#position-delete-files) identify deleted rows by file and position in one or more data files, as shown in the following example.

| `file_path` | `pos` |
| --- | --- |
| `file:/Users/test.user/Downloads/gen_tables/orders_with_deletes/data/2021/2021-00.parquet` | `6` |
| `file:/Users/test.user/Downloads/gen_tables/orders_with_deletes/data/2021/2021-00.parquet` | `16` |

Dremio can optimize Iceberg tables containing position delete files. This is beneficial to do because when data files are read, the associated delete files are stored in memory. Also, one data file can be linked to several delete files, which can impact read time.

When tables are optimized in Dremio, the position delete files are removed and the data files that are linked to them are rewritten. Data files are rewritten if any of the following conditions are met:

* The file size is not within the optimum range.
* The partition's specification is not current.
* The data file has an attached delete file.

## Related Topics

* [Apache Iceberg](/dremio-cloud/developer/data-formats/iceberg) – Learn more about the Apache Iceberg table format.
* [Load Data Into Tables](/dremio-cloud/bring-data/load/) – Load data from CSV, JSON, or Parquet files into existing Iceberg tables.

Was this page helpful?

* Clustering
* Data File Compaction
* Partition Evolution
* Manifest File Rewriting
* Position Delete Files
* Related Topics

<div style="page-break-after: always;"></div>

# Wikis and Labels | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/manage-govern/wikis-labels

On this page

Wikis and labels help users document, organize, and discover datasets within the Open Catalog. This page explains how to manage wikis and labels, as well as how Dremio’s Generative AI features can assist in generating wikis and labels for you.

## Wikis

Wikis for datasets provide an efficient way to document and describe datasets within the Open Catalog. These wikis enable users to add comprehensive information, context, and relevant details about the datasets they manage.
With a user-friendly, rich text editor, the wikis support [Github-flavored markdown](https://github.github.com/gfm/), allowing users to format content easily and enhance readability.
Wikis ensure that dataset documentation is both accessible and structured, making it simpler for teams to understand the datasets and how to work with them effectively.

![This image shows an example of the Wiki editor in Dremio.](/images/data-wiki-new.png "Creating a Wiki Entry in Dremio")

### Manage Wikis

note

Ensure you have sufficient [Role-Based Access Control (RBAC) privileges](/dremio-cloud/security/privileges/) to view or edit wikis.

To view or edit the wiki for a dataset in the Dremio console:

1. On the Datasets page, navigate to the folder where your dataset is stored.
2. Hover over your dataset, and on the right-hand side, click the ![This is the icon that represents more actions.](/images/icons/more.png "Icon represents more actions.") icon.
3. Click **Open Details Panel**.
   * You can edit the dataset wiki by clicking **Edit Wiki**, writing your wiki content, and clicking **Save**.

## Labels

Labels for datasets offer a powerful way to organize and retrieve datasets within a data catalog. By creating and assigning labels to datasets, users can easily search and filter through large collections related datasets.
Labels also enhance the search experience, allowing users to quickly locate datasets associated with a specific label. By clicking on a label, users can initiate a search that brings up all datasets linked to that label, streamlining the process of finding relevant data and improving overall data management.

The following image shows a dataset in the catalog with several label and a brief wiki. In this example, the label "pii-data" was used in the search field to narrow down on a customer dataset that contains Personally Identifiable Information (PII).

![This image shows an example of creating labels.](/images/tags-new.png "Creating Labels")

### Manage Labels

note

Ensure you have sufficient [Role-Based Access Control (RBAC) privileges](/dremio-cloud/security/privileges/) to view or edit labels.

To view or edit the labels for a dataset in the Dremio console:

1. On the Datasets page, navigate to the folder where your dataset is stored.
2. Hover over your dataset, and on the right-hand side, click the ![This is the icon that represents more actions.](/images/icons/more.png "Icon represents more actions.") icon.
3. Click **Open Details Panel**.
   * You can add a label by clicking on the ![](/images/icons/edit.png) icon, typing a label name (e.g. `PII`), and clicking **Enter**.

## Generate Labels and Wikis Preview

To help eliminate the need for manual profiling and cataloging, you can use Generative AI to generate labels and wikis for your datasets.

note

If you haven't opted into the Generative AI features, see [Dremio Preferences](/dremio-cloud/admin/projects/preferences) for the steps on how to enable.

#### Generate Labels

In order to generate a label, Generative AI bases its understanding on your schema by considering other labels that have been previously generated and labels that have been created by other users.

To generate labels:

1. Navigate to either the Details page or Details Panel of a dataset.
2. In the Dataset Overview on the right, click ![This is the icon that represents Generative AI.](/images/cloud/gen-ai-icon.png "Icon represents Generative AI.") to generate labels.
3. In the Generating labels dialog, review the labels generated for the dataset and decide which to save. If multiple labels have been generated, you can save some, all, or none of them. To remove, simply click the **x** on the label.

![This screenshot is showing how to generate a label.](/images/cloud/label-autolabel-new.png "Generating a label.")

4. Complete one of the following actions:

   * If these are the only labels for your dataset, click **Save**.
   * If you already have labels for the dataset and want to add these generated labels, click **Append**.
   * If you already have labels for the dataset and want to replace them with these generated labels, click **Overwrite**.

   The labels for the dataset will appear in the Dataset Overview.

#### Generate Wikis

In order to generate a wiki, Generative AI bases its understanding on your schema and data to produce descriptions of datasets, because it can determine how the columns within the dataset relate to each other and to the dataset as a whole.

You can generate wikis only if you are the dataset owner or have `ALTER` privileges on the dataset.

To generate a wiki:

1. Navigate to either the Details page or Details Panel of a dataset.
2. In the Wiki section, click **Generate wiki**. A dialog will open and a preview of the wiki content will generate on the right of the dialog. If you would like to regenerate, click ![](/images/icons/regenerate.png).

![This screenshot is showing how to generate wikis.](/images/cloud/wiki-autosummarize-new.png "Generating a Wiki.")

3. Click ![](/images/cloud/copy-button.png) to copy the generated wiki content on the right of the dialog.
4. Click within the text box on the left and paste the wiki content.
5. (Optional) Use the toolbar to make edits to the wiki content. If you would like to regenerate, click ![This is the icon that represents Generative AI.](/images/cloud/gen-ai-icon.png "Icon represents Generative AI.") in the toolbar to regenerate wiki content in the preview.
6. Click **Save**.

The wiki for the dataset will appear in the Wiki section.

## Related Topics

* [Search for Dremio Objects and Entities](/dremio-cloud/explore-analyze/discover#search-for-dremio-objects-and-entities) - Explore Dremio's semantic search capabilities.
* [Data Privacy](/data-privacy/) - Learn more about Dremio's data privacy practices.

Was this page helpful?

* Wikis
  + Manage Wikis
* Labels
  + Manage Labels
* Generate Labels and Wikis Preview
* Related Topics

<div style="page-break-after: always;"></div>

# Row-Access and Column-Masking Policies | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/manage-govern/row-column-policies

On this page

Row-access and column-masking policies may be applied to tables, views, and columns via [user-defined functions (UDFs)](/dremio-cloud/sql/commands/create-function/). Using these policies, you can control access to sensitive data based upon the rules and conditions you need to maintain compliance or adhere to regulatory requirements, while also removing the need to produce a secondary set of data with protected information manually removed.

The following restrictions apply to policies and UDFs:

* Only users with the ADMIN role can create UDFs.
* UDFs can only have one owner, which is the user that created the UDF, by default.
* You can transfer ownership of a UDF using the `GRANT OWNERSHIP` command (see [Privileges](/dremio-cloud/security/privileges)).
* Users or roles must have the EXECUTE privilege in order to apply filtering and masking policies.

## Column-Masking Policies

Column-masking is a way to mask—or scramble—private data at the column-level dynamically prior to query execution. For example, the owner of a table or view may apply a policy to a column to only display the year of a date or the last four digits of a credit card.

Column-masking policies may be any UDF with a scalar return type that is identical to the data type of the column on which it is applied. However, only one column-masking policy may be applied to each column.

In the following example of a user-defined function, only users within in the Accounting department in the state of California (CA) may see an entry's social security number (ssn) if the record lists an income above $10,000, otherwise the SSN value is masked with XXX-XX-.

Column-masking policy example

```
CREATE FUNCTION protect_ssn (ssn VARCHAR(11))  
    RETURNS VARCHAR(11)  
        RETURN SELECT CASE WHEN query_user()='jdoe@dremio.com' OR is_member('Accounting') THEN ssn  
            ELSE CONCAT('XXX-XXX-', SUBSTR(ssn,9,3))  
        END;
```

## Row-Access Policies

Row-access policies are a way to control which records in a table or view are returned for specific users and roles. For example, the owner of a table or view may apply a policy that filters out customers from a specific country unless the user running the query has a specific role.

Row-access policy example

```
CREATE FUNCTION country_filter (country VARCHAR)  
    RETURNS BOOLEAN  
        RETURN SELECT query_user()='jdoe@dremio.com' OR (is_member('Accounting') AND country='CA');
```

Row-access policies may be any boolean UDF applied to the table or view. The return value of the UDF is treated logically in a query as an `AND` operator included in a `WHERE` clause. The return type of the UDF must be `BOOLEAN`, otherwise Dremio will give an error at execution time.

## User-Defined Functions

A user-defined function, or [UDF,](/dremio-cloud/sql/commands/create-function) is a callable routine that accepts input parameters, executes the function body, and returns a single value or a set of rows.

The UDFs which serve as the basis for filtering and masking policies must be defined independently of your sources. Not only does this allow organizations to use a single policy for multiple tables and views, but this also restricts user access to policies and prevents unauthorized tampering. Modifying a single UDF automatically updates the policy in the context of any tables or views using that access or mask policy.

The following process describes how policies are enforced with Dremio:

1. A user with the ADMIN role creates a UDF to serve as a security policy.
2. The administrator then sets the security policy to one or more tables, views, and/or columns.
3. Dremio enforces the policy at runtime when an end-user performs a query.

Creating UDFs and attaching security policies is done through SQL commands. Policies are applied prior to execution during the query planning phase. At this point, Dremio checks first the table/view for a row-access policy and then each column accessed for a column-masking policy. If any policies are found, they are automatically applied to the policy's scope using the associated UDF in the query plan.

### Query Substitutions

Row-access and column-masking function act as an "implicit view," replacing a table/view reference in an SQL statement prior to processing the query. This implicit view is created through an examination of each policy applied to a table, view, or column.

For example, [jdoe@dremio.com](mailto:jdoe@dremio.com) has SELECT access to table\_1. However, the column-masking policy protect\_ssn is set for the column\_1 column with a UDF to replace all but the last four digits of a social security number with X for anyone that is not a member of the Accounting department, or this user. When they run a query in Dremio that includes this column-masking policy, the following occurs:

1. During the SQL Planning phase, Dremio identifies which tables, views, and columns are being accessed (table\_1) and whether security policies must be enforced.
2. The engine searches for any security policies set to the associated objects, such as protect\_ssn (see Examples of UDFs below).
3. When the protect\_ssn policy is found for the object affected by the query, the query planner immediately modifies the execution path to incorporate the masking function.
4. Query execution proceeds as normal with the associated UDF included within the execution path.

## List Existing UDFs

To view all existing UDFs created in Dremio, use the [`SHOW FUNCTIONS`](/dremio-cloud/sql/commands/show-functions/) SQL command.

## List Existing Policies

To view row-access and column-masking policies, use a [`SELECT` statement](/dremio-cloud/sql/commands/SELECT) with the target table/view, system table, and policies specified.

List existing column-masking and row-access policies

```
SELECT view_name, masking_policies, row_access_policies FROM sys.project.views;  
SELECT table_name, masking_policies, row_access_policies FROM sys.project."tables";
```

To view all column-masking policies set for a given table, use the [`DESCRIBE TABLE`](/dremio-cloud/sql/commands/describe-table/) command.

## Set a Policy

To create a row-access or column-masking policy, you must perform the following steps using the associated SQL commands:

1. Create a new UDF or replace an existing one using the `CREATE \[OR REPLACE\]` [function](/dremio-cloud/sql/commands/create-function/) command.

   Create or replace UDF

   ```
   CREATE FUNCTION country_filter (country VARCHAR)  
   RETURNS BOOLEAN  
   RETURN SELECT query_user()='jdoe@dremio.com' OR (is_member('Accounting') AND country='CA');  
     
   CREATE FUNCTION id_filter (id INT)  
   RETURNS BOOLEAN  
   RETURN SELECT id = 1;
   ```
2. Grant the [EXECUTE privilege](/dremio-cloud/security/privileges) to the role/users to apply the policy.

   Grant EXECUTE privilege

   ```
   GRANT EXECUTE ON FUNCTION country_filter TO role Policy_Role;
   ```
3. Create a policy to apply the function use `ADD ROW ACCESS POLICY` for row-level access or `SET MASKING POLICY` for column-masking. These may be used with the `CREATE TABLE`, `CREATE VIEW`, `ALTER TABLE`, and `ALTER VIEW` commands.

   Create policy to apply function

   ```
   -- Add row-access policy  
   ALTER TABLE e.employee  
   ADD ROW ACCESS POLICY country_filter(country);  
     
   -- Add column-masking policy  
   ALTER VIEW e.employee_view  
   SET MASKING POLICY protect_ssn (ssn_col, region);  
     
   -- Create table with row policy  
   CREATE TABLE e.employee(  
   id INTEGER,  
   ssn VARCHAR(11),  
   country VARCHAR,  
   ROW ACCESS POLICY country_filter(country)  
   );  
     
   -- Create table with masking policy  
   CREATE VIEW e.employee_view(  
   ssn_col VARCHAR MASKING POLICY protect_ssn (ssn_col, region),  
   region VARCHAR,  
   state_col VARCHAR)  
   );
   ```

note

Both row-access and column-masking UDFs may be applied in a single security policy, or set individually.

## Drop a Policy

To remove a security policy from a table, view, or row, use `UNSET MASKING POLICY` or `DROP ROW ACCESS POLICY` with `ALTER TABLE` or `ALTER VIEW`.

Remove security policy

```
ALTER TABLE w.employee DROP ROW ACCESS POLICY country_filter(country);  
ALTER VIEW e.employees_view MODIFY COLUMN ssn_col UNSET MASKING POLICY protect_ssn;
```

## Examples of UDFs

The following are examples of user-defined functions that you may create with Dremio.

### Column-Masking Policies

Redact SSN

```
CREATE FUNCTION  
    protect_ssn (val VARCHAR)  
    RETURNS VARCHAR  
    RETURN  
        SELECT  
            CASE  
                WHEN query_user() IN ('jdoe@dremio.com','janders@dremio.com')  
                    OR is_member('Accounting') THEN val  
                ELSE CONCAT('XXX-XX-',SUBSTR(value,8,4))  
            END;
```

Use column-masking and row-access policies

```
CREATE FUNCTION lower_country(country VARCHAR)  
    RETURNS VARCHAR  
    RETURN SELECT lower(country);  
  
CREATE FUNCTION country_filter (country VARCHAR)  
    RETURNS BOOLEAN  
    RETURN SELECT query_user()='dremio'  
                      OR (is_member('Accounting')  
                              AND country='CA');  
  
CREATE FUNCTION protect_ssn (ssn VARCHAR(11))  
    RETURNS VARCHAR(11)  
    RETURN SELECT CASE WHEN query_user()='dremio' OR is_member('Accounting') THEN ssn  
            ELSE CONCAT('XXX-XXX-', SUBSTR(ssn,9,3))  
        END;  
  
CREATE FUNCTION salary_range (salary FLOAT, id INTEGER)  
    RETURNS BOOLEAN  
        RETURN SELECT CASE WHEN id > 1 AND salary > 10000 THEN true  
            ELSE false  
        END;
```

Use STRUCT

```
--  
CREATE TABLE struct_demo (emp_info struct <name : VARCHAR>);  
INSERT INTO nas.struct_demo VALUES(SELECT convert_from('{"name":"a"}', 'json'));  
CREATE FUNCTION hello(nameCol struct<name:VARCHAR>) RETURNS struct<name:VARCHAR> RETURN SELECT nameCol;  
ALTER TABLE nas.struct_demo MODIFY COLUMN emp_info SET MASKING POLICY hello(emp_info);
```

Use LIST

```
CREATE FUNCTION hello_country(countryList LIST<VARCHAR>) RETURNS VARCHAR RETURN SELECT 'Hello World';  
ALTER TABLE "test.json" MODIFY COLUMN country SET MASKING POLICY hello_country(country);
```

### Row-Access Policies

Use simple filter expressions

```
CREATE FUNCTION country_filter (country VARCHAR)  
    RETURNS BOOLEAN  
        RETURN SELECT state='CA';
```

Match users

```
CREATE FUNCTION query_1(my_value varchar)  
    RETURNS BOOLEAN  
        RETURN SELECT CASE  
            WHEN current_user = 'jdoe@dremio.com' THEN true  
            ELSE false  
        END;
```

### Table-Driven Policy with a Subquery

Use a subquery as a table-driven policy

```
DROP TABLE <catalog-name>.salesmanagerregions;  
CREATE TABLE <catalog-name>.salesmanagerregions (  
    sales_manager varchar,  
    sales_region varchar  
);  
  
INSERT INTO <catalog-name>.salesmanagerregions  
VALUES ('john.smith@example.com', 'WW'),  
('jane.doe@example.com', 'NA'),  
('viktor.jones@example.com', 'EU');  
  
CREATE TABLE  <catalog-name>.revenue (  
    company varchar,  
    region varchar,  
    revenue decimal(18,2)  
);  
  
INSERT INTO <catalog-name>.revenue  
VALUES ('Acme', 'EU', 2.5),  
('Acme', 'NA', 1.5);  
  
CREATE OR REPLACE FUNCTION security.sales_policy (sales_region_in varchar) RETURNS BOOLEAN  
  RETURN SELECT is_member('sales_executive_role')  
    OR EXISTS (  
        SELECT 1 FROM <catalog-name>.salesmanagerregions  
            WHERE user() = sales_manager  
            AND sales_region = sales_region_in  
        );  
  
ALTER TABLE <catalog-name>.revenue  
ADD ROW ACCESS POLICY security.sales_policy(region);  
  
SELECT * FROM <catalog-name>.revenue;  
-- company, region, revenue  
-- Acme, NA, 1.50
```

## Use Reflections on Datasets with Policies

Dremio supports Reflection creation on views and tables with row-access and column-masking policies defined on any of the underlying anchor datasets. See the following examples.

Example of a view with a row-access policy and a raw Reflection

```
-- Create nested views  
CREATE OR REPLACE VIEW myView AS  
  SELECT city, state, pop FROM Samples."samples.dremio.com"."zips.json"  
  WHERE pop > 10000;  
CREATE OR REPLACE VIEW myView2 AS  
  SELECT city, state FROM myView  
  WHERE STARTS_WITH(city, 'A');  
  
-- Create a raw Reflection on the inner view  
ALTER TABLE myView  
  CREATE RAW REFLECTION myReflection  
  USING DISPLAY(city, state);  
  
-- Query the view after the Reflection is created  
SELECT * FROM myView2;  
  
-- Create a UDF  
CREATE OR REPLACE FUNCTION isMA(state VARCHAR)  
  RETURNS BOOLEAN  
  RETURN SELECT CASE WHEN IS_MEMBER('hr') THEN state='MA'  
      ELSE NULL  
    END;  
  
-- Add a row-access policy and query the view  
ALTER TABLE myView  
  ADD ROW ACCESS POLICY isMA("state");  
SELECT * FROM myView2;
```

After running the last query, the Reflection is used to accelerate the query as shown in the results below:

![](/assets/images/rcac_reflection_accelerated-31f0960f65be2a237384c0bd0956681f.png)

The `Query1` results show that the row-access policy has been applied successfully:

![](/assets/images/rcac_reflection_policy-e386c1d9134a00081efd62fe472e3edb.png)

The `Query2` results do not appear to those who are not members of HR:

![](/assets/images/rcac_reflection_accelerated_nonmember-28eade94013c96a7ec2ba42c29b2b67d.png)

The `Query2` results appear to those who are members of HR:

![](/assets/images/rcac_reflection_accelerated_member-9c4fd2be39fe181162620c678e99766c.png)

Example of a table with a row-access policy and an aggregation Reflection

```
ALTER TABLE NAS.rcac.employee  
  ADD ROW ACCESS POLICY is_recent_employee(hire_date);  
ALTER TABLE NAS.rcac.employee  
  CREATE AGGREGATE REFLECTION ar_tvrf_1 USING DIMENSIONS(hire_date);  
SELECT MIN(SALARY) FROM NAS.rcac.employee  
  GROUP BY hire_date;
```

### Limitations

See the following limitations where datasets with row-access and/or column-masking policies cannot support Reflections:

* Policies with Multiple Arguments
* Aggregates on Masked Columns
* SET Operations
* NULL Generating JOINs
* Trimming Projects

#### Policies with Multiple Arguments

If a policy on an anchor dataset contains multiple columns, the Reflection created on the view containing the policy fails. See the following example:

Example of the limitation

```
-- Create tables  
CREATE TABLE employees (  
 id INT,  
 hire_date DATE,  
 ssn VARCHAR(11),  
 name VARCHAR,  
 country VARCHAR,  
 salary FLOAT,  
 job_id INT);  
CREATE TABLE jobs (  
 id INT,  
 title VARCHAR,  
 is_good BOOLEAN);  
  
-- Create a view  
CREATE VIEW job_salary_in_the_usa AS  
 SELECT job_id, salary  
 FROM employees  
 WHERE country = 'USA';  
  
-- Create a UDF  
CREATE OR REPLACE FUNCTION hide_salary_on_bad_job(salary FLOAT, job_id_in INT)  
  RETURNS BOOLEAN  
  RETURN SELECT CASE WHEN IS_MEMBER('public') AND (  
     SELECT is_good FROM jobs j WHERE job_id_in = j.id)  
      THEN NULL  
    ELSE salary  
    END;  
  
-- Add a column-masking policy  
ALTER TABLE employees  
 MODIFY COLUMN salary  
 SET MASKING POLICY hide_salary_on_bad_job(salary, job_id);  
  
-- Create a raw Reflection on the view  
ALTER DATASET job_salary_in_the_usa  
 CREATE RAW REFLECTION job_salary_drr USING DISPLAY(job_id, salary);
```

In the above example, the `job_salary_drr` Reflection fails to materialize due to the multi-argument policy on `test.tables.employees::salary`.

#### Aggregates on Masked Columns

You cannot create a raw Reflection on the view if there is a policy defined on the masked column.

Example of the limitation

```
CREATE OR REPLACE VIEW myView AS  
  SELECT MIN(salary)  
  FROM employees
```

In the above example, there is a policy defined on `salary`, so you cannot create a Reflection on this view.

#### NULL Generating JOINs

You can only apply the policy if it's on the “join side” of the join, such as:

* Left side of LEFT JOIN
* Right side of RIGHT JOIN
* Either side of INNER JOIN
* Neither side of FULL OUTER JOIN

If the policy is not on the "join side", the join generates NULL values for all the entries that didn’t match the join condition.

Example of the limitation

```
CREATE OR REPLACE VIEW myView AS  
  SELECT emp.department_id, dept.department_name, emp.name  
  FROM employees as emp  
   RIGHT JOIN department as dept  
   ON emp.department_id = dept.department_id
```

In the above example, there is a policy defined on the `employees` table, which is on the left side of the RIGHT JOIN, so you cannot create a Reflection on this view.

#### SET Operations

The policy must be defined on all UNION datasets and on the same field.

Example of the limitation

```
CREATE OR REPLACE VIEW myView AS  
  SELECT * FROM a  
  UNION SELECT * FROM employees  
  UNION SELECT * FROM c
```

In the above example, there is a policy defined on the `employees` table, so you cannot create a Reflection on this view.

#### Trim Projects

In order to create a Reflection on a view, the view should reference all the fields that are part of the row-access and column-masking policies.

Example of the limitation

```
-- Create a UDF  
CREATE OR REPLACE FUNCTION isMA(state VARCHAR)  
  RETURNS BOOLEAN  
  RETURN SELECT CASE WHEN IS_MEMBER('public') THEN state='MA'  
      ELSE NULL  
    END;  
  
-- Create views  
CREATE OR REPLACE VIEW myView1 AS  
  SELECT city, state, pop FROM Samples."samples.dremio.com"."zips.json"  
  WHERE pop > 10000;  
  
-- Add a row-access policy  
ALTER TABLE myView1  
  ADD ROW ACCESS POLICY isMA("state");  
  
-- Create views  
CREATE OR REPLACE VIEW myView2 AS  
  SELECT * FROM myView1;  
CREATE OR REPLACE VIEW myView3 AS  
  SELECT city, pop FROM myView1;
```

#### Trimming Projects

In the above example, you can create a Reflection on `myView2` but not on `myView3` since it trims the `state` column from the view which has a policy defined on it.

Was this page helpful?

* Column-Masking Policies
* Row-Access Policies
* User-Defined Functions
  + Query Substitutions
* List Existing UDFs
* List Existing Policies
* Set a Policy
* Drop a Policy
* Examples of UDFs
  + Column-Masking Policies
  + Row-Access Policies
  + Table-Driven Policy with a Subquery
* Use Reflections on Datasets with Policies
  + Limitations

<div style="page-break-after: always;"></div>

