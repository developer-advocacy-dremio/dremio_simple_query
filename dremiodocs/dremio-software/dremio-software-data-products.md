# Dremio Software - Data Products



---

# Source: https://docs.dremio.com/current/data-products/

Version: current [26.x]

On this page

# Build Data Products

A data product is a self-contained data asset that has been prepared, can be trusted, and has an SLA. It is meant to optimize for reuse, consistency, and sharing of data. Organizations have data products that are domain-specific and data products that are common at the organization level.

In Dremio, there are two levels of data products:

1. Data products that are created by curating and transforming one or more source tables into a view.
2. Data products that are created at the business or application layer and are used in reports, dashboards, and other applications.

Here are two examples of data products:

* Sam is a data analyst in the sales team, and he is asked to create a data product that provides a unified data asset that segments customers into different groups based on behavior, spending, and demographics. He creates a data product with a curated and transformed view of customer data from multiple source tables (e.g., customer demographics, purchase history, and engagement activity). The data in the data product is cleansed, transformed, enriched, certified, and structured for easy consumption by marketing and sales teams.
* Alice is an analyst in the finance team, and she needs to create an executive financial dashboard at the business or application layer for her company’s E-staff team. She creates a data product that powers a visualization report for financial performance metrics for her company, including revenue, expenses, and profitability over time. The data product integrates multiple data sources from various domains, including transactional and financial data, and presents the information in a format that is easily consumable by executives for decision-making.

## Data Product Lifecyle

Data products are created and managed through a lifecycle similar to the software development lifecycle. The data product lifecycle encompasses the end-to-end process of developing, deploying, and maintaining data products, ensuring they provide ongoing value to users. The image below depicts the phases of the lifecycle, which teams iterate through.

![This image illustrates the data products lifecycle.](/images/data-products-lifecycle.png "Data products lifecycle")

### Discover

To make data products reusable, they must be easily discoverable and explorable. Cross-functional or organization level data products must be accessible across various team to drive consistency. Users need to be able to quickly understand how to interpret the data in a data product and determine if it is relevant to the business problem at hand. For this to happen, data products must be published with adequate metadata such as domain, descriptions and definitions, tags, and usage information. To learn more about data discovery, see [Discover Data](/current/data-products/discover).

### Develop

Data products can be developed using SQL in Dremio's SQL Runner. You can just as easily use your IDE of choice for development. To learn more about developing data products, see [Develop Data Products](/current/data-products/develop).

### Deploy

To learn more about deploying your semantic layer with dbt, see [Deploy with dbt](/current/data-products/deploy-with-dbt).

### Govern

Effective data governance ensures secure, compliant, and transparent management of data by ensuring documentation and traceability, enforcing fine-grained access policies, and tracking dataset lineage to enhance data quality, minimize risks, and optimize value. To learn more about governance, see [Govern Data](/current/data-products/govern).

### Serve

Data products can be served in multiple forms. For example, data products are served in the Dremio console for adhoc analysis or they can be incorporated into a dashboard or report. This phase of the lifecycle is focused on delivering insights and data output to users ensuring accessibility and usability. For more information on the client applications that support connectivity to Dremio, see [Connecting Client Applications to Dremio](/current/client-applications).

### Observe

To fully empower users to manage their data products, they must be able to monitor them continuously to assess usage and performance over time. Observability enables data product owners to make iterative improvements based on their users' needs.

## Additional Resources

Find out more about data products by enrolling in the [Data Product Fundamentals course in Dremio University](https://university.dremio.com/course/data-product-fundamentals).

Was this page helpful?

[Previous

Clustering](/current/load-data/clustering)[Next

Discover Data](/current/data-products/discover/)

* Data Product Lifecyle
  + Discover
  + Develop
  + Deploy
  + Govern
  + Serve
  + Observe
* Additional Resources

---

# Source: https://docs.dremio.com/current/data-products/discover/

Version: current [26.x]

On this page

# Discover Data

Dremio simplifies the discovery of data objects and other Dremio entities.

Data discovery capabilities in Dremio include the following:

* Catalog exploration in the Dremio console
* AI-enabled semantic search for objects and entities
* Star objects

Data discovery capabilities are optimized for data that is governed by Dremio. Files and folders that have not been formatted as a table in Dremio may not be easily discoverable.

## Catalog exploration in the Dremio console

The Datasets page allows you to navigate through and explore objects that you have access to in Dremio. To learn more about the Datasets page, see [Quick Tour of the Datasets Page](/current/get-started/quick_tour#datasets-page). Once you have located the table of view that you are interested in, you can use the Details panel to learn more about it.

## AI-enabled semantic search for objects Enterprise

You can use the search bar in Dremio to find objects that are accessible through Dremio. This capability performs keyword and semantic search to find tables, views, and other objects that are related to your search criteria. Search only returns results that you have privileges to see. See [Searching for Dremio Objects](/current/data-products/discover/semantic-search).

## Object Metadata

Metadata such as the owner of the table or view, when it was created, and columns is easily accessible through metadata cards. Metadata cards can help you learn more about the object of interest and provide quick links to actions that you may want to take on the table or view. See [Metadata Cards](/current/data-products/discover/metadata) for more information.

## Star objects

You can star objects that you use frequently to provide easier discoverability and access. Starring objects such as sources, spaces, folders, tables, and views will surface them in the **Starred** tab of the SQL Runner. See [Star Objects](/current/data-products/discover/bookmarks) to learn more.

Was this page helpful?

[Previous

Build Data Products](/current/data-products/)[Next

Searching for Dremio Objects](/current/data-products/discover/semantic-search)

* Catalog exploration in the Dremio console
* AI-enabled semantic search for objects Enterprise
* Object Metadata
* Star objects

---

# Source: https://docs.dremio.com/current/data-products/develop

Version: current [26.x]

On this page

# Develop Data Products

You can curate and transform your data to create a data product by

* Writing SQL in the SQL Runner
* Using the low-code tranformation flows in the SQL Runner to help generate SQL

## Write SQL in the SQL Runner

You can use the SQL Runner to transform your data and create data products in Dremio.

* For a quick tour of the SQL Runner and the supported capabilities, see [Quick Tour of the SQL Runner](/current/get-started/quick_tour#sql-runner).
* See the [SQL Reference](/current/reference/sql) for functions and commands that you can use to transform and work with your data.
* You can also create data products using an IDE of your choice. Use [Arrow Flight JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver) to establish a connection to Dremio from and IDE to do your development.

### Create a View

You can create a view from an existing table or view by transforming the data as required and performing the following steps:

1. Compose the query in the SQL Runner and click **Run** to validate the query. After running the query, click the arrow next to **Save Script As** in the top right of the SQL editor, and select **Save View as...** from the drop-down menu.
2. Name the new view and select where the view will be located. If the location is not updated, the view will get saved to your home space. Once the view is saved, you will be navigated to the Dataset page.

### Retrieve a View Definition

If you have the `SELECT` privilege for a view, you can see the underlying definition in the SQL editor but cannot edit the view directly. To see a view definition, on the Datasets page, hover over the line containing the view and click ![](/images/icons/go-to-table.png) on the right.

tip

If you have the required privileges, you can run `SHOW CREATE VIEW <view_name>` in the SQL editor to see the view definition. See [SHOW CREATE VIEW](/current/reference/sql/commands/show-create-view).

### Edit a View

If you have the privileges required to edit a view, you can see and edit the definition of the view.

To edit a view, perform the following steps:

1. On the Datasets page, hover over the line containing the view and click ![](/images/icons/edit.png) on the right. The view definition will open.
2. Edit the view definition as needed and click **Run** to validate the query.
3. Click **Save View** in the top right corner of the SQL editor. This will overwrite the current definition of the view with the new definition.

### Delete a View

Perform the following steps to delete a view:

1. On the Datasets page, go to the folder or space where your view is located.
2. Hover over the line containing the view that you want to delete, click the ellipses (...) icon. From the list of actions, click **Delete**. Confirm that you want to delete the view.

caution

If you are deleting a table or view with children, you get a warning. Removing a table or view with children leaves you with disconnected views that you can no longer query.

## Use Low-Code to Transform Data in the SQL Runner

To begin a data transformation, via one of the following methods:

* Highlighting a portion or all of a field's value
* Using the dropdown menu for the transformation.
  The dropdown is to the right of the field's name.

### Use Highlighting

The highlighting method is often the most intuitive method.  
It provides enough context for Dremio to make some best guesses
about how to execute the transformation that you have in mind.

For instance, you could highlight a portion of a field that contains customer names to quickly perform an extract
that creates a new field with only last names.

**Suggestion Cards**  
For transformations that are initiated by highlighting part or all of a field value,
Dremio uses a heuristic to determine a set of "suggestion cards" that represent its
best guesses as to your intended result.

You can click on one of these suggestion cards to inspect a preview of the new dataset and
confirm that it matches your expectations.
If no suggestion card is a perfect match, you can "flip" the card (by clicking the
pencil icon in the upper right corner) to tweak the
card's parameters before applying the transformation.

note

The highlight method is great for beginning an extract. However, in cases where other capabilities are required, the dropdown menu may be more useful.

### Use Dropdown Menus

The dropdown menu provides a more complete list of transformations that are applicable to the data type.

### Fix Inconsistent Data with a Join

In situations where the entries in a field are inconsistent
(for example, different spellings or abbreviations for the same name),
the following technique can be used to increase the quality of the dataset:

1. Identify the field with the problematic data. It may be useful to run this command in the SQL Editor:

   Identify a field

   ```
   SELECT DISTINCT myProblemFieldName FROM myDatasource.myTable
   ```
2. Download the results as CSV using the Download button.
3. Open the file in a text editor or Excel and create lookup values for the distinct values
   from your table in a second column.
   For example, standardizing variations in color names to a single canonical name.
4. Upload this file to your Home space on Dremio
5. Open this new dataset and hit the Join button located on the left above the field names
6. Select Custom Join and then the name of the inconsistent dataset you would like to fix, followed by Next
7. Drag over the name of the left column from your uploaded dataset, and match it with the name of the field you
   would like to correct in the inconsistent dataset
8. Apply the Join then drop the old field, renaming the new one to take its place
9. Save the corrected dataset

### Clean Text

For text data, excess whitespace and changing capitalization schemes are two common data cleanliness issues.
Dremio provides two transformations for dealing with these possible inconsistencies:
**Trim Whitespace** and **Convert Case**.

### Handle Invalid, Empty and NULL Values

Empty or NULL text values are best eliminated by using Exclude.
You can initiate this transformation by:

1. Highlight a value from the field
   that contains empty or NULL values, and
2. Select Exclude from the dropdown that appears.
   This renders a list of the values in this field, and the frequency at which they occur.
3. Check the boxes next to the empty and/or NULL values you which to exclude from the dataset and click Apply.

### Work with Date Types

You can convert a text type field that contains date information into a proper date type field. This allows you to do more sophisticated analyses in external tools such as spotting by trends by month, year, or quarter.

You can begin this conversion by selecting 'Date & Time' from the type menu located to the left of the text field's name. In the subsequent dialog, select whether the output should be a time, date, date and time. It also gives a few default options for the format as well as a 'Custom' field for indicating a custom format. See [Data & Time Data Types](/current/reference/sql/data-types/#date--time-data-types) for more information on the conversions you can do.

Was this page helpful?

[Previous

Star Objects](/current/data-products/discover/bookmarks)[Next

Deploy with dbt](/current/data-products/deploy-with-dbt)

* Write SQL in the SQL Runner
  + Create a View
  + Retrieve a View Definition
  + Edit a View
  + Delete a View
* Use Low-Code to Transform Data in the SQL Runner
  + Use Highlighting
  + Use Dropdown Menus
  + Fix Inconsistent Data with a Join
  + Clean Text
  + Handle Invalid, Empty and NULL Values
  + Work with Date Types

---

# Source: https://docs.dremio.com/current/data-products/deploy-with-dbt

Version: current [26.x]

On this page

# Deploy with dbt

dbt enables analytics engineers to develop and manage semantic layers within dbt projects and deploy them to Dremio.

You can use Dremio's dbt connector `dbt-dremio` to transform data that is in data sources that are connected to a Dremio project.

## Prerequisites

* Download the `dbt-dremio` package from <https://github.com/dremio/dbt-dremio>.
* Ensure that Python 3.9.x or later is installed.
* Ensure that you are using Dremio Software version 22.0 or later.
* If you want to use TLS to secure the connection between dbt and Dremio Software, configure full wire encryption in your Dremio cluster. For more information, see the configuration of TLS for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#full-wire-encryption-enterprise).

## Installing

Install this package from PyPi by running this command:

Install dbt-dremio package

```
pip install dbt-dremio
```

note

`dbt-dremio` works with dbt-core versions 1.8 and 1.9. Earlier versions of dbt-core are out of support from dbt.

## Initializing a dbt Project

1. Run the command `dbt init <project_name>`.
2. Select `dremio` as the database to use.
3. Select one of these options to generate a profile for your project:
   * `software_with_username_password` for working with a Dremio Software cluster and authenticating to the cluster with a username and a password
   * `software_with_pat` for working with a Dremio Software cluster and authenticating to the cluster with a personal access token

Next, configure the profile for your dbt project.

## Profiles

When you initialize a dbt project, you create one of these three profiles. You must configure it before trying to connect to Dremio Cloud or Dremio Software.

* Profile for Dremio Software with Username/Password Authentication
* Profile for Dremio Software with Authentication Through a Personal Access Token

For descriptions of the configurations in these profiles, see Configurations.

### Dremio Software Profile with Username & Password

Example Profile

```
[project name]:  
  outputs:  
    dev:  
      password: b9JtkIgI3uup9gGxxK  
      port: 9047  
      software_host: 192.0.2.0  
      object_storage_source: Samples  
      object_storage_path: "samples.dremio.com"."Dremio University"  
      dremio_space: Space1  
      dremio_space_folder: Folder1.Folder2  
      threads: 1  
      type: dremio  
      use_ssl: true  
      user: userName  
  target: dev
```

### Dremio Software Profile with Personal Access Token

Example Profile

```
[project name]:  
  outputs:  
    dev:  
      pat: A1BCDrE2FwgH3IJkLM4NoPqrsT5uV6WXyza7I8bcDEFgJ9hIj0Kl1MNOPq2Rstu  
      port: 9047  
      software_host: 192.0.2.0  
      object_storage_source: Samples  
      object_storage_path: "samples.dremio.com"."Dremio University"  
      dremio_space: Space1  
      dremio_space_folder: Folder1.Folder2  
      threads: 1  
      type: dremio  
      use_ssl: true  
      user: userName  
  target: dev
```

## Configurations

| Configuration | Required? | Default Value | Description |
| --- | --- | --- | --- |
| `password` | Yes, if you are not using the pat configuration. | None | The password of the account to use when logging into the Dremio cluster. |
| `pat` | Yes, if you are not using the user and password configurations. | None | The personal access token to use for authenticating to Dremio. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for instructions about obtaining a token. The use of a personal access token takes precedence if values for the three configurations user, password and pat are specified. |
| `port` | Yes | `9047` | Port for Dremio Software cluster API endpoints. |
| `software_host` | Yes | None | The hostname or IP address of the coordinator node of the Dremio cluster. |
| `enterprise_catalog_namespace` | No | None | The name of the catalog in which to create tables, materialized views, tests, and other objects, and views. The dbt aliases are `datalake` (for objects) and `database` (for views). This name corresponds to the name of a catalog in the **Open Catalogs** section of the Datasets page in Dremio. |
| `enterprise_catalog_folder` | No | None | The path in the catalog in which to create objects / views. The dbt aliases are `root_path` (for objects) and `schema` (for views). Nested folders in the path are separated with periods. This value corresponds to the path in this location in the Datasets page in Dremio. |
| `object_storage_source` | No | $scratch | The name of the filesystem in which to create tables, materialized views, tests, and other objects. The dbt alias is `datalake`. This name corresponds to the name of a source in the **Object Storage** section of the Datasets page in Dremio: |
| `object_storage_path` | No | `no_schema` | The path in the filesystem in which to create objects. The default is the root level of the filesystem. The dbt alias is `root_path`. Nested folders in the path are separated with periods. This value corresponds to the path in this location in the Datasets page in Dremio: 'samples.dremio.com'.'Dremio University' |
| `dremio_space` | No | `@<username>` | The value of the Dremio space in which to create views. The dbt alias is `database`. This value corresponds to the name in this location in the **Spaces** section of the Datasets page in Dremio: Spaces1 |
| `dremio_space_folder` | No | `no_schema` | The folder in the Dremio space in which to create views. The default is the top level in the space. The dbt alias is `schema`. Nested folders are separated with periods. This value corresponds to the path in this location in the Datasets page in Dremio: |
| `threads` | Yes | 1 | The number of threads the dbt project runs on. |
| `type` | Yes | dremio | Auto-populated when creating a Dremio project. Do not change this value. |
| `use_ssl` | Yes | `true` | Acceptable values are `true` and `false`. If the value is set to true, ensure that full wire encryption is configured in your Dremio cluster. See [Prerequisites](/current/data-products/deploy-with-dbt#prerequisites). |
| `verify_ssl` | No | `true` | Acceptable values are `true` and `false`. Set to `false` if using a self-signed certificate or if the root certificate authority (CA) is not included in Python’s CA certificates. |
| `user` | Yes | None | The username of the account to use when logging into the Dremio cluster. |

## Known Issues

[Model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts) are not supported.

## Additional Resources

Learn more about DataOps by enrolling in the [DataOps with Apache Iceberg course in Dremio University](https://university.dremio.com/course/dataops-with-apache-iceberg).

Was this page helpful?

[Previous

Develop Data Products](/current/data-products/develop)[Next

Govern Data](/current/data-products/govern/)

* Prerequisites
* Installing
* Initializing a dbt Project
* Profiles
  + Dremio Software Profile with Username & Password
  + Dremio Software Profile with Personal Access Token
* Configurations
* Known Issues
* Additional Resources

---

# Source: https://docs.dremio.com/current/data-products/govern/

Version: current [26.x]

On this page

# Govern Data

Effective data governance is essential for managing secure, compliant, transparent, and traceable data products. In addition to securing your data using role-based access control (RBAC), data governance for data products allows you to apply fine-grained access controls (row access & column-masking policies) on your data, as well as trace the lineage of any dataset in the lakehouse. Together, these governance tools help organizations optimize the value they derive from their data to enhance data quality and transparency, while minimizing the risks associated with data misuse and non-compliance.
Dremio also provides tools for describing, identifying, and displaying datasets using wikis and tags.

## Row-Access and Column-Masking Policies

[Row access & column-masking (or fine-grained access control) policies](/current/data-products/govern/row-column-policies-udf) provide mechanisms to enforce data privacy and security rules directly on your data.

## Lineage

[Data lineage](/current/data-products/govern/lineage) allows you to track and visualize data as it moves through the various stages of a data pipeline. It provides clarity on where the data comes from, how it is transformed, and where it is used.

## Wikis and Tags

[Wikis](/current/data-products/govern/wikis-tags) for datasets allow users to document and describe datasets in the Open Catalog using a rich text editor with [Github-flavored markdown](https://github.github.com/gfm/).

[Tags](/current/data-products/govern/wikis-tags) for datasets help organize and retrieve data efficiently by allowing users to search, filter, and locate datasets through specific tag associations.

Was this page helpful?

[Previous

Deploy with dbt](/current/data-products/deploy-with-dbt)[Next

Row-Access and Column-Masking Policies](/current/data-products/govern/row-column-policies-udf)

* Row-Access and Column-Masking Policies
* Lineage
* Wikis and Tags

---

# Source: https://docs.dremio.com/current/data-products/discover

Version: current [26.x]

On this page

# Discover Data

Dremio simplifies the discovery of data objects and other Dremio entities.

Data discovery capabilities in Dremio include the following:

* Catalog exploration in the Dremio console
* AI-enabled semantic search for objects and entities
* Star objects

Data discovery capabilities are optimized for data that is governed by Dremio. Files and folders that have not been formatted as a table in Dremio may not be easily discoverable.

## Catalog exploration in the Dremio console

The Datasets page allows you to navigate through and explore objects that you have access to in Dremio. To learn more about the Datasets page, see [Quick Tour of the Datasets Page](/current/get-started/quick_tour#datasets-page). Once you have located the table of view that you are interested in, you can use the Details panel to learn more about it.

## AI-enabled semantic search for objects Enterprise

You can use the search bar in Dremio to find objects that are accessible through Dremio. This capability performs keyword and semantic search to find tables, views, and other objects that are related to your search criteria. Search only returns results that you have privileges to see. See [Searching for Dremio Objects](/current/data-products/discover/semantic-search).

## Object Metadata

Metadata such as the owner of the table or view, when it was created, and columns is easily accessible through metadata cards. Metadata cards can help you learn more about the object of interest and provide quick links to actions that you may want to take on the table or view. See [Metadata Cards](/current/data-products/discover/metadata) for more information.

## Star objects

You can star objects that you use frequently to provide easier discoverability and access. Starring objects such as sources, spaces, folders, tables, and views will surface them in the **Starred** tab of the SQL Runner. See [Star Objects](/current/data-products/discover/bookmarks) to learn more.

Was this page helpful?

[Previous

Build Data Products](/current/data-products/)[Next

Searching for Dremio Objects](/current/data-products/discover/semantic-search)

* Catalog exploration in the Dremio console
* AI-enabled semantic search for objects Enterprise
* Object Metadata
* Star objects

---

# Source: https://docs.dremio.com/current/data-products/govern

Version: current [26.x]

On this page

# Govern Data

Effective data governance is essential for managing secure, compliant, transparent, and traceable data products. In addition to securing your data using role-based access control (RBAC), data governance for data products allows you to apply fine-grained access controls (row access & column-masking policies) on your data, as well as trace the lineage of any dataset in the lakehouse. Together, these governance tools help organizations optimize the value they derive from their data to enhance data quality and transparency, while minimizing the risks associated with data misuse and non-compliance.
Dremio also provides tools for describing, identifying, and displaying datasets using wikis and tags.

## Row-Access and Column-Masking Policies

[Row access & column-masking (or fine-grained access control) policies](/current/data-products/govern/row-column-policies-udf) provide mechanisms to enforce data privacy and security rules directly on your data.

## Lineage

[Data lineage](/current/data-products/govern/lineage) allows you to track and visualize data as it moves through the various stages of a data pipeline. It provides clarity on where the data comes from, how it is transformed, and where it is used.

## Wikis and Tags

[Wikis](/current/data-products/govern/wikis-tags) for datasets allow users to document and describe datasets in the Open Catalog using a rich text editor with [Github-flavored markdown](https://github.github.com/gfm/).

[Tags](/current/data-products/govern/wikis-tags) for datasets help organize and retrieve data efficiently by allowing users to search, filter, and locate datasets through specific tag associations.

Was this page helpful?

[Previous

Deploy with dbt](/current/data-products/deploy-with-dbt)[Next

Row-Access and Column-Masking Policies](/current/data-products/govern/row-column-policies-udf)

* Row-Access and Column-Masking Policies
* Lineage
* Wikis and Tags