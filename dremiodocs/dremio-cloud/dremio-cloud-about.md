# What is Dremio Cloud? | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/about/

On this page

Dremio Cloud is the agentic lakehouse—a fully managed platform built for AI agents and managed by AI agents. It unifies data across lakes, warehouses, and databases while automating platform and data operations through autonomous workflows.

Unlike traditional systems that require constant tuning and manual operations, Dremio Cloud continuously learns, adapts, and optimizes without human intervention. This creates a self-managing environment where AI agents, applications, and users can seamlessly access consistent, governed data.

## Core Capabilities

**AI Agent**: Dremio Cloud includes a native AI agent integrated with the catalog and governance controls. The agent can discover datasets, generate queries, and help both technical and non-technical users move from questions to repeatable assets quickly. It reduces complexity by automating routine analytics tasks while operating within enterprise security and governance.

**AI Semantic Layer**: The [semantic layer](/dremio-cloud/manage-govern/) acts as a living dictionary for business entities, metrics, and relationships so agents and analysts share the same context. This reduces ambiguity, prevents hallucinations, and improves accuracy in both AI-generated and human-authored queries. Because definitions travel with the data, consistency is enforced across tools and users.

**Unified Data Access**: Dremio Cloud provides live access to data across lakes, warehouses, and databases without ETL pipelines or copies. Structured, semi-structured, and unstructured data can be queried together in real time, and built-in [AI functions](/dremio-cloud/sql/sql-functions/AI) let you process formats such as PDFs and images directly in SQL workflows. At the foundation is Dremio's [Open Catalog](/dremio-cloud/bring-data/connect/catalogs/open-catalog), built on Apache Polaris and co-created by Dremio. This ensures interoperability with engines like Spark and Trino, integration with catalogs such as AWS Glue and Unity Catalog, and fine-grained role-based access controls.

**Autonomous Management**: The platform delivers consistent sub-second performance without manual tuning. Features such as [Autonomous Reflections](/dremio-cloud/admin/performance/autonomous-reflections) act as an intelligent cache that adapts to workload patterns, while Iceberg clustering and automatic table optimization continuously organize data to address skew and small files. These optimizations happen transparently—no changes to applications or hand-tuning required.

## Why It Matters

Dremio Cloud gives AI agents and humans a unified, governed foundation for analytics and decision-making. The AI Semantic Layer ensures a consistent business context, while Autonomous Management capabilities deliver fast, reliable performance across all data. Built on open standards—Apache Iceberg, Apache Polaris, and Apache Arrow—Dremio avoids lock-in while supporting the scale, speed, and trust required for agentic workloads.

Was this page helpful?

* Core Capabilities
* Why It Matters

<div style="page-break-after: always;"></div>

# Supported Regions | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/about/regions

On this page

When you create a Dremio project, you select the region in which your resources will be created and run. This determines where your metadata is stored and where your compute resources are provisioned.

When selecting a region for your Dremio project, consider the following factors:

* **Network Connectivity**: Select regions with close geographic proximity to your data sources and end users to minimize latency and align with your existing cloud infrastructure
* **Data Residency**: Your region choice determines where your data is stored and processed, so select regions that align with regulatory obligations

The table below lists the supported regions and availability zones:

| Region | Code | Availability Zones |
| --- | --- | --- |
| US East (N. Virginia) | us-east-1 | us-east-1a, us-east-1b, us-east-1c, us-east-1d, us-east-1e, and us-east-1f |
| US West (Oregon) | us-west-2 | us-west-2a, us-west-2b, us-west-2c, us-west-2d |

## Connection Endpoints

Use these URLs to connect to Dremio:

| Interface | Endpoint |
| --- | --- |
| Arrow Flight (includes JDBC and ODBC) | data.dremio.cloud |
| Dremio console | app.dremio.cloud |
| Dremio JDBC (Legacy) | sql.dremio.cloud |
| MCP | mcp.dremio.cloud |
| OAuth | login.dremio.cloud |
| Open Catalog | catalog.dremio.cloud |
| REST API | api.dremio.cloud |
| SCIM | scim.dremio.cloud |

Was this page helpful?

* Connection Endpoints

<div style="page-break-after: always;"></div>

# Key Concepts | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/about/concepts

On this page

This page defines core Dremio concepts.

## Platform

The platform provides the foundational organizational structure for Dremio. It establishes the account hierarchy through organizations and projects, and enables administrators to control user access and allocate resources.

### Organizations and Projects

An [organization](/dremio-cloud/admin/subscription/#organizations) is the top-level account within Dremio where authentication, roles, AI configuration for Model Providers, and billing are managed. An organization can contain multiple projects.

A [project](/dremio-cloud/admin/projects/) isolates compute, data, and resources for team-based data analysis. Projects provide the primary boundary for resource allocation and access control.

When creating a project, you can choose between Dremio-managed storage or provide [your own object storage](/dremio-cloud/admin/projects/your-own-project-storage) as the project store. This is where Dremio stores materializations, metadata, and Iceberg tables created in your Open Catalog.

### Roles and Permissions

[Roles](/dremio-cloud/security/roles) define what actions users can perform within Dremio. Permissions control access to specific resources like projects, catalogs, tables, and views. Administrators assign roles to users to manage who can view, create, modify, or delete data objects and configurations.

## Catalog

Enables unified data access across heterogeneous sources without requiring data movement or ETL processes.

### Open Catalog

[Dremio's Open Catalog](/dremio-cloud/bring-data/connect/catalogs/open-catalog) is a metadata and data management layer built on Apache Polaris. It provides a unified namespace for organizing and accessing data across your Dremio environment with Apache Iceberg support.

#### Namespaces and Folders

A **namespace** is the top-level container within the Open Catalog that organizes data objects. The catalog name corresponds to your project name, and namespaces are the primary organizational boundary for tables, views, and folders within that catalog.

**Folders** are directories that contain tables, views, and other folders. Use folders to organize your data into common themes, such as data quality (raw, enrichment, and presentation layers), business units, or geographic regions. Folders can be organized hierarchically for better data governance.

#### Tables and Views

**Tables** contain data from your sources, formatted as rows and columns. Tables in the Open Catalog use the Iceberg table format, and Dremio automates maintenance processes including compaction and garbage collection.

**Views** are virtual tables based on SQL queries. Views do not contain data but provide logical abstractions over tables, other views, or combinations of both. Views leverage the Iceberg view specification for portability across different query engines.

### Data Sources

Dremio connects to external systems through data sources without data movement. Supported sources include:

* **Iceberg Catalogs**: AWS Glue Data Catalog, Snowflake Open Catalog, Unity Catalog, and Iceberg REST Catalogs
* **Object Storage**: Amazon S3 and Azure Storage for data lake workloads
* **Relational Databases**: PostgreSQL, MySQL, SQL Server, and other RDBMS systems

### Paths

Paths are dot-separated identifiers that specify the location of an object, starting with the source or catalog name, followed by any folders, and ending with the name of the dataset, table, or view. Paths are used to qualify objects when referencing them in queries.

For example, in the path `my_catalog.usage.onprem_deployment.daily_usage`:

* `my_catalog` is the catalog name
* `usage` and `onprem_deployment` are folders within the catalog
* `daily_usage` is the table or view name

## AI Semantic Layer

Dremio provides multiple ways to discover and understand your data across all connected sources.

### Wikis and Labels

[Wikis](/dremio-cloud/manage-govern/wikis-labels#wikis) provide detailed descriptions and context for your datasets, like a README for your data. Wikis support [Markdown](https://daringfireball.net/projects/markdown/) formatting and can include dataset descriptions, source information, and example queries.

[Labels](/dremio-cloud/manage-govern/wikis-labels#labels) enable easy categorization of datasets. For example, add a `PII` label to indicate personally identifiable information, or `Finance` to group financial datasets.

### Semantic Search

[Semantic search](/dremio-cloud/explore-analyze/discover#search-for-dremio-objects-and-entities) enables you to find objects and entities across your data catalog using natural language queries. It searches object names, metadata, wikis, and labels to return relevant results including sources, folders, tables, views, user-defined functions, Reflections, scripts, and jobs.

## Dremio's AI Agent

[Dremio's AI Agent](/dremio-cloud/explore-analyze/ai-agent) enables natural language data exploration and analysis. You can ask questions about your data in natural language, and the AI Agent generates SQL queries and provides insights based on your datasets. The AI Agent works with data from all connected sources and can help create views and analyze patterns across your data catalog.

## Query Engine

A Dremio-managed compute engine that automatically starts, scales, and stops based on query demand. Each query engine consists of one or more replicas made up of executor instances that process queries. Every project includes a default preview query engine, which remains available for essential operations and automatically scales down when idle.

### Engines

An engine processes jobs that run queries issued by users (either through a client application or through the user interface) or by Dremio (as, for example, when Dremio creates a Reflection that a user has defined). Compute resources for an engine are allocated in the cloud associated with the project. All engines in a project are associated with the same cloud.

Engines are automatically started and stopped by the Dremio control plane and can be configured to have multiple replicas for scaling. For more information, see [Manage Engines](/dremio-cloud/admin/engines/).

### Workload Management

[Workload Management](/dremio-cloud/admin/engines/workload-management/) enables you to control how compute resources are allocated and prioritized across different types of queries and users to optimize performance for your specific workloads.

### Reflections

Reflections accelerate query performance by providing precomputed and optimized copies of source data or query results. They can be [Autonomous](/dremio-cloud/admin/performance/autonomous-reflections) or [manually managed](/dremio-cloud/admin/performance/manual-reflections/). For more details, see [Optimize Performance](/dremio-cloud/admin/performance/).

Was this page helpful?

* Platform
  + Organizations and Projects
  + Roles and Permissions
* Catalog
  + Open Catalog
  + Data Sources
  + Paths
* AI Semantic Layer
  + Wikis and Labels
  + Semantic Search
* Dremio's AI Agent
* Query Engine
  + Engines
  + Workload Management
  + Reflections

<div style="page-break-after: always;"></div>

# Architecture | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/about/architecture

On this page

At a high level, Dremio's architecture is divided into three planes: data, execution, and control. Dremio is fully hosted with the control and execution planes running on Dremio's tenant.

## Data

Dremio's primary data plane is Amazon S3. You can use Dremio-managed storage or bring your own bucket. Dremio can also federate across relational sources, so you can pull data from wherever it resides.

## Execution

The execution plane follows a massively parallel processing (MPP) model, where workloads are divided into fragments and spread across a cluster of executors. To minimize repeated reads from S3, Dremio uses caching layers to make queries as fast as possible.

## Control

The control plane is where metadata is managed, queries are planned, and security is defined.

![](/images/cloud/simple_architecture_diagram.png)

## How Queries Flow Through Dremio

With an understanding of the layers, we can follow a query through Dremio. A SQL query will start in your organization's slice of our control plane, whether submitted via the web console or via a client connection. The metadata of the datasets being queried informs Dremio how it should plan to access and transform your data. This plan is iterated over, with each iteration applying optimization. This plan, separated into fragments, is passed to a query engine. The query engine will read and transform the data amongst its constituent executors, delivering the results back up to the point of origin.

Was this page helpful?

* Data
* Execution
* Control
* How Queries Flow Through Dremio

<div style="page-break-after: always;"></div>

