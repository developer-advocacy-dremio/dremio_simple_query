# Get Started with Dremio Cloud | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/get-started/

On this page

To get started, sign up for an account at [dremio.com/get-started](https://www.dremio.com/get-started) and follow the guided setup to create your first project.

This guide shows you how to analyze transportation data and find usage patterns using natural language queries with Dremio's AI Agent. You'll work with the `dremio_samples.nyc_citibikes.citibikes` table that contains over 115 million bike-sharing records from New York City—real patterns from one of the world's busiest transportation networks.

## Step 1: Discover and Explore Your Data

Understanding your dataset structure is crucial before diving into analysis. Start by getting an overview of the bike-sharing data to understand what insights are possible.

On the homepage, enter the following prompt into Dremio's AI Agent chat box: `Give me an overview of the nyc_citibikes.citibikes dataset`.

The AI Agent uses capabilities like semantic search to find relevant datasets. Review the response to understand the schema, field definitions, and what types of analysis are possible with bike-sharing data.

## Step 2: Compare User Behavior

Ask a question in natural language to compare how different user types interact with the bike-sharing service. This analysis reveals usage patterns that inform operational decisions.

Ask the AI Agent to compare how subscribers and casual riders use the service: `Give me the total number of rides and the average trip duration grouped by user type across the dataset.`

The AI Agent generates and runs SQL using Dremio's query engine to answer this question. The results show that subscribers typically show higher ride frequency but shorter durations, indicating commuter behavior. Casual riders often have longer trips but lower frequency, suggesting leisure or tourist usage patterns. This analysis reveals how different user types require different operational strategies for bike availability, pricing models, and infrastructure investment.

## Step 3: Analyze Peak Demand Patterns

Dive deeper to understand when different user groups are most active. This temporal analysis provides insights for operational planning and resource allocation.

Ask the AI Agent to reveal hourly demand patterns: `Analyze hourly ride patterns to find when demand peaks. Show a line chart of total rides per hour of the day, separated by user type, and include a short report highlighting the busiest hours for each group and recommendations for bike availability`.

The AI Agent will create a clear chart showing distinct patterns. Subscribers peak during rush hours (8-9 AM, 5-6 PM) indicating commuter usage, while casual riders peak during midday and weekends showing leisure patterns. This temporal analysis reveals opportunities for dynamic pricing during peak hours, optimal timing for maintenance during low-demand periods, and capacity planning insights for fleet optimization.

## Step 4: Run Comparative Analysis

Use the AI Agent to identify the most influential factors affecting rider behavior. This analysis compares multiple variables to determine primary drivers of ridership patterns.

Ask the AI Agent to run a comprehensive comparative analysis: `Run comparative analysis on seasonal, daily, hourly, and bike type patterns to identify which factor has the most significant impact on ride behavior. Then create a detailed visualization of the most influential factor.`

The AI Agent will compare multiple variables and automatically identify which factor has the biggest impact on rider behavior, complete with actionable recommendations. This analysis reveals primary drivers of ridership, correlation insights between variables, and predictive indicators for forecasting usage patterns.

## Step 5: Try Your Own Analysis

Now that you understand how to analyze transportation data with the AI Agent, try exploring other bike-sharing questions.

You can also analyze your own data using Dremio's AI Agent.

## Summary

You have completed a transportation data analysis using natural language. You explored the dataset structure, compared user behavior patterns, analyzed peak demand times, and identified influential factors affecting ridership. Discovery, exploration, and analysis that could previously take hours can now be done in minutes with Dremio's AI Agent.

## Troubleshoot

* If a prompt doesn't work as expected, try simplifying the request or verifying that you're referencing the correct dataset (`nyc_citibikes.citibikes`).
* Contact your administrator if sample data isn't available in your environment.

## Related Topics

* [Bring Your Data](/dremio-cloud/bring-data/) – Load, connect, and prepare your data.
* [Quick Tour of the Dremio Console](/dremio-cloud/get-started/quick-tour) – Learn how to navigate Dremio.
* [Add a User](/dremio-cloud/admin/users#add-a-user) – Invite team members to your organization.

Was this page helpful?

* Step 1: Discover and Explore Your Data
* Step 2: Compare User Behavior
* Step 3: Analyze Peak Demand Patterns
* Step 4: Run Comparative Analysis
* Step 5: Try Your Own Analysis
* Summary
* Troubleshoot
* Related Topics

<div style="page-break-after: always;"></div>

# Build Your First Agentic Lakehouse Use Case | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/get-started/use-case

On this page

This guide will help you turn a business question into a working, governed data product using your own data, all within your 30-day Dremio Cloud trial.

In the [Getting Started guide](/dremio-cloud/get-started/), you saw how Dremio's AI Agent can take you from question to insight within minutes using sample data. With this guide, you'll connect your data, prepare and transform it, build reusable views with semantics, and deliver insights using Dremio's AI Agent or your preferred tool of choice. The end goal is flexible: you might produce an aggregated view that analysts and AI agents query regularly, or a dashboard. Either way, you’ll experience the full value of Dremio Cloud as an agentic lakehouse — open, governed, and self-optimizing.

## Prerequisites

Before you begin, ensure that you have the following:

* A Dremio Cloud account: You'll need an active Dremio Cloud trial account. If you haven't already, sign up at [dremio.com/get-started](https://dremio.com/get-started) for a 30-day trial with $400 in free credits.
* Access to data: Identify at least one data source you can connect to, such as object storage or databases. If you don't have these, then you will need a set of local files that you can upload to Dremio Cloud.
* (Optional) Access to your BI tool: If your use case requires a dashboard, you will need access to your BI tool. This is optional, as you can use Dremio's AI Agent to generate basic charts to visualize trends directly within the Dremio console.

## Step 1: Identify a Business Use Case

Begin by identifying a business use case that you will be implementing using this guide. The use case you choose should have clear value and measurable results, not a massive data project but a business question that matters.

### How to Do It

Pick a concrete business question, such as:

* *How are customer support metrics trending this quarter?*
* *Which product lines are driving margin growth?*
* *What are our top churn risks by region?*

We recommend that you select a business question that can be answered using a few datasets, going across a maximum of two sources.

## Step 2: Add Your Data

To implement the data model that answers the business question you identified in the Identify a Business Use Case section, you will first add your data to the project in your Dremio Cloud account.

### How to Do It

You can add data to your project in one of three ways:

**Load Data into the Open Catalog**: Dremio provides a default Open Catalog, powered by Apache Polaris. You can load data directly into this catalog as an Iceberg table in your silver layer using your tool of choice, such as Fivetran, dbt, and Airbyte. From there, Dremio manages all Iceberg table metadata and governance while keeping your data in an open format. For instructions on how to load data into your Open Catalog, see [Load Data into Tables](/dremio-cloud/bring-data/load/).

**Connect an Existing Source**: Connect your object store, catalogs, databases so Dremio can query data in place. This is your bronze layer of data. For a list of supported sources and step-by-step connection instructions, see [Connect to Your Data](/dremio-cloud/bring-data/connect/).

**Upload Local Files**: Upload local files (CSV, JSON, or Parquet) for quick exploration if you don't have direct access to your data sources. Dremio will write the uploaded data into an Iceberg table in your project's Open Catalog. For step-by-step instructions on how to upload files, see [Upload Local Files](/dremio-cloud/bring-data/load/#upload-local-files).

Whichever method you choose, Dremio provides live, federated access to all of your data. This flexibility allows you to move from data connection to analysis in minutes.

## Step 3: Clean and Transform Data

Dremio lets you prepare data from across different sources without having to move it. You're able to use natural language to generate the SQL using Dremio's AI Agent or write SQL yourself. Your data preparation steps can be represented as views; no additional pipelines are required.

### How to Do It

**Use SQL and AI Functions**: Prepare and transform data using [SQL Functions](/dremio-cloud/sql/sql-functions/). You can also turn unstructured data, such as images or PDFs, into a structured, governed Iceberg table using [AI Functions](/dremio-cloud/sql/sql-functions/AI).

**Use Dremio's AI Agent**: Ask the built-in AI Agent to identify issues with the data and generate SQL to prepare and transform it. For example, you can ask the AI Agent to:

* *Generate SQL to remove null values in the revenue column.*
* *Generate SQL to join orders and customers on customerID.*
* *Add a column for gross margin = revenue - cost.*

Each transformation can be saved as a view in your silver layer, giving you reusable building blocks. This way, your transformations are continuously updated as more data comes in with no additional changes required from you. This approach replaces complex ETL pipelines with a simple workflow that keeps your data fresh, governed, and easy to iterate on. For instructions on how to create views, see [Create a View](/dremio-cloud/bring-data/prepare/#create-a-view).

## Step 4: Build Views for Aggregations and Metrics

Once you've created your silver layer by cleansing and transforming your data, you can create your gold layer of views. These views will capture aggregations and metrics and will be ready for exploration, ad-hoc analysis, or dashboards.

### How to Do It

**Use SQL Functions**: Aggregate and build out metrics using [SQL Functions](/dremio-cloud/sql/sql-functions/).

**Use Dremio's AI Agent**: Ask the built-in AI Agent to generate the SQL for your view. For example, you can ask the agent to *Give me the SQL for views that summarize the average response time by call center employees and the customer sentiment by region.*

Aggregations and metrics are saved as governed views in your Open Catalog. For instructions on how to create views, see [Create a View](/dremio-cloud/bring-data/prepare/#create-a-view).

## Step 5: Add Semantics to Views

Data only becomes valuable when everyone can interpret it in the same way. The AI Semantic Layer gives your datasets shared meaning, so when an analyst or AI Agent is looking at "fiscal Q2" or "positive sentiment", they're applying the same business logic every time.

### How to Do It

**Enrich Your Data with Semantics**: Generate wikis and labels on your views to reduce the amount of time being spent on manual tasks. For more information on generating semantics, see [Generate Wikis and Labels](/dremio-cloud/manage-govern/wikis-labels/#generate-labels-and-wikis-preview).

You can add additional context, such as usage notes, definitions specific to your industry, and common queries.
These definitions and classifications are stored with the data, guiding both natural language queries, SQL generation, and manual exploration.

## Step 6: Deliver Insights

Now that you have connected, curated, aggregated, and enriched your data, you can deliver on the outcome for the business question you defined in [Step 1](/dremio-cloud/get-started/use-case/#step-1-identify-a-business-use-case). The outcome may be the aggregated view you created in the previous step that teams and agents will use directly, or it may be a dashboard that tracks metrics over time. With Dremio Cloud, you're able to deliver on either one.

### How to Do It

**Use Dremio's AI Agent for Actionable Insights**: Dremio's AI Agent can analyze patterns and trends directly from views. You and your users can ask the business question you identified in [Step 1](/dremio-cloud/get-started/use-case/#step-1-identify-a-business-use-case), along with other questions. The AI Agent will use the semantics and samples of the data to generate the appropriate SQL queries that provide you with insights and visualizations of the data. For example, on sales data, you can ask the AI Agent to *Create a chart to show the trends in sales across regions over the last year and provide an analysis on the changes.*

**Create a Dashboard Using Your Tool of Choice**: If you already have a dashboard or report that you would like to update or you want to create a new one to represent the insights on your data, you can connect to Dremio from tools like Tableau, Microsoft Power BI, and others using Flight SQL JDBC/ODBC connections. For a list of supported tools and step-by-step instructions on connecting, see [Connect Client Applications](/dremio-cloud/explore-analyze/client-apps/).

## Step 7: Operationalize the Use Case

Each use case is operationalized when it's governed, monitored, and shareable.

### How to Do It

**Access Control Policies**: Create and implement access control policies from role-based access to more granular row and column-level policies. For more information, see [Privileges](/dremio-cloud/security/privileges/) and [Row-Access and Column-Masking Policies](/dremio-cloud/manage-govern/row-column-policies/).

**Monitor Query Volumes and Performance**: Track performance and usage of the data. Dremio's [Autonomous Management capability](/dremio-cloud/admin/performance/) automatically handles data management and ensures reliable and fast query performance. In Dremio, you're able to [monitor queries and their performance](/dremio-cloud/admin/monitor/).

**Cost Management**: Review consumption and spend of this use case within the Dremio console. These dashboards show how much compute and storage each workload consumes, helping you plan budgets, optimize workloads, and estimate spend before moving to production. For more information, see [Usage](/dremio-cloud/admin/subscription/usage/).

Operationalizing your first use case ensures it remains reliable, governed, and cost-effective. You gain insight into both performance and consumption trends, enabling you to scale confidently while maintaining control of your budget.

## Wrap Up and Next Steps

You've now implemented your first use case on Dremio Cloud by:

* Defining a valuable business use case
* Adding your own data to your Open Catalog or by connecting existing data sources
* Cleaning and transforming the data
* Creating reusable views with semantics
* Delivering insights via AI or dashboards
* Operationalizing the data through governance and monitoring

Next, extend your use case with additional business questions or another business domain.

## Related Topics

* [Dremio MCP Server](/dremio-cloud/developer/mcp-server/) - Use Dremio's hosted MCP server to customize your agentic workflow.
* [Visual Studio Code](/dremio-cloud/developer/vs-code/) - Use the Visual Studio (VS) Code extension for Dremio for development and analysis.
* [Optimize Performance](/dremio-cloud/admin/performance/) - Learn about how Dremio autonomously optimizes performance.

Was this page helpful?

* Prerequisites
* Step 1: Identify a Business Use Case
  + How to Do It
* Step 2: Add Your Data
  + How to Do It
* Step 3: Clean and Transform Data
  + How to Do It
* Step 4: Build Views for Aggregations and Metrics
  + How to Do It
* Step 5: Add Semantics to Views
  + How to Do It
* Step 6: Deliver Insights
  + How to Do It
* Step 7: Operationalize the Use Case
  + How to Do It
* Wrap Up and Next Steps
* Related Topics

<div style="page-break-after: always;"></div>

# Quick Tour of the Dremio Console | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/get-started/quick-tour

On this page

This quick tour introduces you to the main areas of the Dremio console, including the homepage, Datasets, SQL Runner, and Jobs pages. You'll learn how to navigate the interface and access key features of your agentic lakehouse.

## Console Navigation

The side navigation bar provides links to key areas of the Dremio console.

![Dremio console navigation.](/images/homepage-navigation.png "Dremio console navigation.")

| Location | Description |
| --- | --- |
| 1 | **Homepage**: Central landing page when you log in. |
| 2 | **Datasets**: Interface for exploring tables and views across the default Open Catalog, other catalogs, object storage, and database sources. |
| 3 | **SQL Runner**: Editor for constructing and querying data. |
| 4 | **Jobs**: History of executed SQL and job details. |
| 5 | **Project and Organization Settings**: Configuration for your catalog, engines, and routing rules in your project and management of authentication, users, billing, and projects in your organization. |
| 6 | **Documentation and Support**: Access point for documentation, the Community Forum, or the Support Portal. |
| 7 | **Account Settings**: Section for managing general information, personal access tokens, appearance preferences, and logout options. |

## Datasets Page

The Datasets page provides navigation and management for data in your Open Catalog, other catalogs, object stores, and databases.

![Datasets page navigation and management interface.](/images/datasets-nav.png "Datasets page navigation and management interface.")

| Location | Description |
| --- | --- |
| 1 | **Project Name**: Name of the current project being explored. |
| 2 | **Namespaces**: Logical containers that organize data objects within Dremio's Open Catalog, providing hierarchical organization and access control for tables, views, and folders. |
| 3 | **Sources**: Self-hosted catalogs, object stores, or databases. |
| 4 | **Path**: Dot-separated identifier indicating the location of the object, starting with the source or catalog name, followed by any folders, and ending with the name of table or view. |

## SQL Runner

The SQL Runner provides a query editor for running SQL. Access via ![](/images/icons/sql-runner.png) in the side navigation bar.

![SQL Runner interface](/images/sql-runner-nav.png "SQL Runner interface")

| Location | Description |
| --- | --- |
| 1 | **Data Panel**: Area for exploring data across your Open Catalog, other catalogs, object stores, and databases, with drag-and-drop support for adding objects into the SQL editor. |
| 2 | **Scripts Panel**: Panel for saved SQL scripts that can be reused and shared with other users in your organization. Each script includes creation/modification timestamps and editor context and requires VIEW privileges. |
| 3 | **SQL Editor**: Workspace for creating and editing SQL with autocomplete, syntax highlighting, and function lookup. See [SQL Reference](/dremio-cloud/sql/) for supported SQL. You may also highlight SQL, right-click, and select **Explain SQL** to start a chat with the AI Agent, which features a summary of the query’s overview, datasets, and architecture. For more details, see [Explain SQL](/dremio-cloud/admin/monitor/jobs/#explain-sql). |
| 4 | **Run**: Execution of the SQL, which returns the complete result set. |
| 5 | **Preview**: Option for previewing the result set, which returns a subset of rows in less time than running the SQL. |
| 6 | **Engine**: Dropdown menu for selecting an engine for SQL execution. By default, Automatic is selected, which routes the query to the appropriate engine based on engine routing rules. For more details, see [Manage Engines](/dremio-cloud/admin/engines/). |
| 7 | **Results Panel**: Table displaying the results of your query with options to download, copy, or edit values. |
| 8 | **Job Summary**: Tab showing the job status, query type, start time, duration, and job ID. |
| 9 | **Transformations**: Tools for applying transformations such as Add Column, Group By, Join, Filter, Convert Data Type, and Add Calculated Field that automatically update SQL. |
| 10 | **Execution State**: Indicator displaying the job status, record count, and execution time, with a link to view full job details. Includes options to download results as JSON, CSV, or Parquet files, or copy data to the clipboard. |
| 11 | **Details Panel**: Right-side panel for viewing and managing dataset metadata, including columns, ownership, searchable labels, and wiki content. |

### Limitations and Considerations

**Row Limit**: `COUNT(*)` and `SELECT` query results are limited to one million rows and may be truncated based on thread distribution. When truncated, a warning appears. To obtain complete results, use [JDBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc/) or [ODBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/) drivers.

**CSV Download**: CSV download is unavailable for result sets with complex data types (union, map, array). The download and copy results options can be enabled or disabled for a specific project by navigating to **Project Settings** > **Preferences**.

Was this page helpful?

* Console Navigation
* Datasets Page
* SQL Runner
  + Limitations and Considerations

<div style="page-break-after: always;"></div>

