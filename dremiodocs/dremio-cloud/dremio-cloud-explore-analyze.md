# Explore and Analyze Your Data | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/

Dremio enables data engineers and data analysts to explore and analyze data regardless of the location of the data or the data format. You can explore and analyze using Dremio's console or use your tool of choice.

* **Discover Data**: Dremio offers several ways of discovering your data. Semantic search, metadata, and lineage help you find the right data quickly. Enrich the semantics of your data with wikis and labels so that AI agents and users can quickly identify relevant data. See [Discover Data](/dremio-cloud/explore-analyze/discover).
* **Explore Using AI Agent**: Use natural language to discover datasets, analyze data, and generate visualizations without writing SQL. The AI Agent uses the AI Semantic Layer to provide relevant responses and ensures governed access to data. See [Explore Using AI Agent](/dremio-cloud/explore-analyze/ai-agent).
* **Connect Client Applications**: Connect your preferred BI and data tools directly to Dremio to analyze data live without extracts or replication. See [Connect Client Applications](/dremio-cloud/explore-analyze/client-apps/).

Was this page helpful?

<div style="page-break-after: always;"></div>

# Explore Using AI Agent | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/ai-agent

On this page

Understanding your data quickly using Dremio's AI Agent, an interface built into the Dremio console that allows users to converse with their data using natural language.

The AI Agent accesses data and entities that the logged in user has privileges on to address the prompt.

The AI Agent is currently optimized for the following tasks:

* **Discover and Explore**: Learn about the data that is available to you to answer your business question.
* **Analyze**: Ask questions using business terms using natural language and get insights instantly. The AI Agent goes beyond basic analysis to detect patterns in the data and return actionable insights.
* **Visualize**: Quickly visualize the patterns and trends in your data within the Dremio console.
* **Explain and Optimize SQL**: Ask the agent to review SQL queries, identify bottlenecks, and suggest optimizations. For more information on this, see [**Explain SQL**](/dremio-cloud/admin/monitor/jobs/#explain-sql).
* **Analyze and Improve Job Performance**: Ask the agent to review past jobs, identify performance issues, and suggest ways to improve them. For more information on this, see [**Explain Job**](/dremio-cloud/admin/monitor/jobs/#explain-job).

As Dremio's AI Agent reasons through your questions and requirements, you're able to see the actions it is taking directly in the interface so you can review, audit, and understand how the response is generated.

Generative AI can make mistakes; therefore, you should verify all output.

## Use Dremio's AI Agent

To use Dremio's AI Agent, you can access it by:

1. Typing a question into the chat on the homepage in the Dremio console.
2. Use the shortcut keys ⌘+Shift+G on a Mac or Ctrl+Shift+G on Windows to open the agent.

To use the AI Agent, you need to be granted CALL MODEL on the default model provider.

## Discover and Explore

Dremio's AI Agent will help you discover available data and provide a detailed breakdown of schema, as well as offer guidance on what tables and views you may want to use. The AI Agent will use wikis and labels as well as perform sampling or other simple analysis on the datasets to determine relevance and interesting patterns. The more detailed the question, the better the insight that the AI Agent can provide.

| Okay Prompt | Great Prompt |
| --- | --- |
| What tables can I use? | Which tables or views have customer location data? |
| How can I analyze time series data? | Which tables or views can I use to do a time series analysis on customer activity? |
| What is the `customer_activity` table? | How is the `customer_activity` table structured, and what other tables does it relate to? |

## Analyze

Dremio's AI Agent will write and execute SQL on your behalf based on your natural language input and the information available from the semantic layer. From within the chat, you can further audit the SQL by expanding the tool calls in the chat window.

| Okay Prompt | Great Prompt |
| --- | --- |
| I want to see analysis of customer activity | I want to see an analysis of customer purchase activity by region, by customer type for each month of the year. |
| Which customers are the most valuable? | Which customers have spent the most with us over the lifetime of the relationship? |

## Visualize

Dremio's AI Agent will visualize insights on your behalf based on your natural language input. The details you provide, including the chart type, axis requirements, grouping, or trendlines, will be considered by the LLM. The visualization will be accompanied by insights that serve as a narrative for the chart that the AI Agent generated. Once a visualization has been created, you can toggle between the visualization and a grid representation of the data that is used to back the visualization.

The AI Agent can return the following types of visualizations: Bar, Line, Area, Scatter, Pie, Heatmap

| Okay Prompt | Great Prompt |
| --- | --- |
| Visualize the data | Visualize the data as a bar chart with month on the x asis and sum of purchase value as the y axis |
| Create a visual trendline showing me the activity | Create a visualization with a trendline showing customer activity by month? |

## Related Topics

* [Jobs](/dremio-cloud/admin/monitor/jobs) – See the **Explain SQL** and **Explain Job** options on the Jobs page.
* [Data Privacy](/data-privacy/) – Learn more about Dremio's data privacy practices.

Was this page helpful?

* Use Dremio's AI Agent
* Discover and Explore
* Analyze
* Visualize
* Related Topics

<div style="page-break-after: always;"></div>

# Discover Data | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/discover

On this page

Dremio provides multiple ways to discover and explore your data. Whether you prefer browsing catalogs, using semantic search, or leveraging the AI Agent, you can find the data you need quickly and efficiently.

Data discovery capabilities in Dremio include the following:

* Dremio's AI Agent for natural language data discovery and exploration
* AI-enabled semantic search for objects and entities
* Catalog exploration in the Dremio console
* Metadata cards for dataset details

## Discover using Dremio's AI Agent

Dremio's AI Agent makes it easy to find relevant data using natural language and your business terms. To learn more about using the AI Agent, see [Explore Using AI Agent](/dremio-cloud/explore-analyze/ai-agent).

## Search for Dremio Objects and Entities

You can quickly and easily find objects and entities with the AI-enabled search experience. Semantic search returns results of sources, folders, tables in Dremio's Open Catalog and external sources registered in Dremio, views in external sources registered in Dremio catalogs, user-defined functions (UDFs), Reflections, scripts, and jobs.

Semantic search takes object names and metadata such as wikis and labels into account to return results that are relevant to your search criteria.

To search for objects and entities:

1. Click the search bar on the top right of the page and type in your search criteria. You can activate the search bar by using the shortcut keys `Command + K` (Mac) or `Ctrl + K` (Windows/Linux).
2. Press the return or enter key to execute the search. Under **Recents**, you will see your recent searches.
3. Select a search result to view details. For a table or view, you can click the ![](/images/cloud/dataset-sql-runner-icon.png) icon to query the table or view in the SQL Runner.

### Limitations and Considerations

* Semantic search has been optimized for English terms.
* After creating new objects, they can take a few hours to appear in search results.
* After deleting objects or entities, they can take a few hours to disappear from search results.
* Data discovery capabilities are optimized for data that is governed by Dremio. Files and folders in object storage that have not been formatted as a table in Dremio may not be easily discoverable.

## Navigate Your Catalog

The Datasets page allows you to navigate through and explore objects that you have access to in Dremio. To learn more about the Datasets page, see [Quick Tour of the Dremio Console](/dremio-cloud/get-started/quick-tour/#datasets-page). Once you have located the table or view that you are interested in, click it to open the Details panel and view comprehensive information about the dataset.

## View Metadata of a Dataset

Wherever a dataset is referenced in Dremio, you can view a metadata card with details about the dataset.

To view the metadata, hover over a dataset to see a metadata card appear with details about the dataset. Key information displayed on dataset cards includes:

* **Dataset type and name**: Icon and title showing the dataset format and name
* **Quick actions**: Query, edit, or view the dataset
* **Path and labels**: Location and any applied labels
* **Usage metrics**: Jobs run and views created from the dataset
* **Ownership and dates**: Creator, creation date, and last modified

## Related Topics

* [Wikis and Labels](/dremio-cloud/manage-govern/wikis-labels) – Learn more about using wikis and labels to enrich your data.
* [Data Privacy](/data-privacy/) – Learn more about Dremio's data privacy practices.

Was this page helpful?

* Discover using Dremio's AI Agent
* Search for Dremio Objects and Entities
  + Limitations and Considerations
* Navigate Your Catalog
* View Metadata of a Dataset
* Related Topics

<div style="page-break-after: always;"></div>

# Connect Client Applications | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/

You can connect to Dremio from several popular applications to query and visualize the data in Dremio:

* [Alteryx Designer](/dremio-cloud/explore-analyze/client-apps/alteryx-designer)
* [Apache Superset](/dremio-cloud/explore-analyze/client-apps/apache-superset)
* [Astrato](/dremio-cloud/explore-analyze/client-apps/astrato)
* [DBeaver](/dremio-cloud/explore-analyze/client-apps/dbeaver)
* [DbVisualizer](/dremio-cloud/explore-analyze/client-apps/dbvisualizer)
* [Deepnote](/dremio-cloud/explore-analyze/client-apps/deepnote)
* [Domo](/dremio-cloud/explore-analyze/client-apps/domo)
* [Hex](/dremio-cloud/explore-analyze/client-apps/hex)
* [IBM Cognos Analytics](/dremio-cloud/explore-analyze/client-apps/ibm-cognos-analytics)
* [Looker](/dremio-cloud/explore-analyze/client-apps/looker)
* [Microsoft Excel PowerPivot](/dremio-cloud/explore-analyze/client-apps/microsoft-excel-powerpivot/)
* [Microsoft Power BI](/dremio-cloud/explore-analyze/client-apps/microsoft-power-bi/)
* [Preset](/dremio-cloud/explore-analyze/client-apps/preset/)
* [SAP Business Objects](/dremio-cloud/explore-analyze/client-apps/sap-business-objects)
* [Tableau](/dremio-cloud/explore-analyze/client-apps/tableau)
* [ThoughtSpot](/dremio-cloud/explore-analyze/client-apps/thoughtspot)

Dremio provides Arrow Flight SQL ODBC and JDBC drivers:

* [Arrow Flight SQL JDBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc/)
* [Arrow Flight SQL ODBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/)

Dremio also supports the [Dremio JDBC (Legacy)](/dremio-cloud/explore-analyze/client-apps/drivers/jdbc-legacy).

Was this page helpful?

<div style="page-break-after: always;"></div>

# Hex | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/hex

On this page

[Hex](https://hex.tech/) is a data workspace where you can analyze and share data from Dremio.

## Supported Authentication Methods

Use a personal access token (PAT) obtained from Dremio. To create a PAT, follow the steps in the section [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

## Prerequisites

If you want to connect to a specific project in Dremio, copy the ID of the project. See [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project) for the steps. After you obtain it, save it somewhere that you can retrieve it from during the procedure.

## Create a Connection

1. Log into your Hex project.
2. Go to the **Data sources** tab on the side navigation bar.
3. Click **+ Add** > **Create project connection**.
4. Select **Dremio** from the project connections.
5. In the **Name** field, enter a name for the data connection.
6. (Optional) In the **Description** field, enter a brief description of the data connection.
7. In the **JDBC Connection** field, paste your JDBC connection string:

   JDBC connection string

   ```
   jdbc:dremio:direct=sql.dremio.cloud:443;ssl=true;
   ```

   a. (Optional) Add ;PROJECT\_ID={project-id} to the JDBC connection string and in the **Project ID** field, paste the ID of the project that you want to connect to. If the project ID isn't specified, then the [default project](/dremio-cloud/admin/projects/#set-the-default-project) will be used.

   b. (Optional) Add ;engine={engine-name} to the JDBC connection string and in the **Engine Name** field, specify the engine that you want the query routed to.
8. For the **Access Token**, paste your personal access token.
9. Click **Create Connection**.

Was this page helpful?

* Supported Authentication Methods
* Prerequisites
* Create a Connection

<div style="page-break-after: always;"></div>

# Domo | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/domo

On this page

[Domo](https://www.domo.com/) is a cloud-based platform designed to provide direct, simplified, real-time access to business data for decision makers across the company with minimal IT involvement.

## Supported Authentication Method

Authenticate to Dremio by using a personal access token (PAT). To create one, see [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

## Prerequisite

Obtain the ID of the project in Dremio that you want to connect to. For the steps, see [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).

## Create a Cloud Integration with Dremio

1. Click the **Data** tab to open the Datasets page.
2. Click the **Federated** tab to open the **Amplify existing cloud warehouses** dialog.
3. Next to **Native integration**, click **Dremio**.
4. In the **Cloud integrations** dialog, click **Add new integration**.
5. In step 1 of the **Connect a Dremio cloud integration** wizard, follow these sub-steps:
   1. In the **Integration name** field, specify a unique name for the integration.
   2. (Optional) In the **Integration description** field, briefly describe the integration.
   3. Select **Dremio Cloud** as the connection type.
6. Click **Next**.
7. In step 2 of the wizard, follow these sub-steps:
   1. In the **Dremio connection URL** field, specify the following connection URL, where `PROJECT_ID` is the ID of the project that you want to connect to:
      Connection URL

      ```
      jdbc:dremio:direct=sql.dremio.cloud:443;ssl=true;token_type=personal_access_token;PROJECT_ID=<project-ID>
      ```
   2. Paste your PAT into the **Personal Access Token** field.
8. Click **Next**.
9. Select the tables that you want to use with Domo through this integration.
10. Click **Create Datasets**.

Datasets are created from the tables, though no data is moved or copied. Datasets in Domo are connections to data in data sources.

Was this page helpful?

* Supported Authentication Method
* Prerequisite
* Create a Cloud Integration with Dremio

<div style="page-break-after: always;"></div>

# Looker | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/looker

On this page

You can use [Looker](https://looker.com/) to query and visualize data by means of Dremio.

## Supported Authentication Method

Use a personal access token (PAT) obtained from Dremio. To create a PAT, follow the steps in [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

## Prerequisite

Copy the ID of the Dremio project that you want to connect to. See [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project) for the steps. After you obtain it, save it somewhere that you can retrieve it from during the procedure.

## Create a Connection

1. Log into Looker.
2. In the menu bar at the top of the page, select **Admin**, and then select **Connections** under **Database**.
3. Click the **Add Connection** button in the top-right corner of the page to open the Connection Settings page for creating a connection.
4. Specify a name for the connection.
5. In the **Dialect** field, select **Dremio 11+**.
6. In the **Remote Host:Port** fields, specify `sql.dremio.cloud` and `443`.
7. In the **Database** field, specify any value. Though Looker requires a value in this field, Dremio does not use the value.
8. In the **Username** and **Password** fields, specify your authentication credentials:

   * In the **Username** field, type `$token`.
   * In the **Password** field, paste your personal access token.
9. Ensure that the **SSL** check box is selected.
10. If there is more that one project in your Dremio organization and you are not connecting to the default project, specify this additional JDBC parameter in the **Additional Settings** section: `PROJECT_ID=<project id>`. To obtain the ID, see [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).
11. Click **Test These Settings** at the bottom of the page to check that the information that you specified is all valid.
12. Click **Add Connection** if the test of the connection is successful.

The new connection is listed on the Connections page.

Was this page helpful?

* Supported Authentication Method
* Prerequisite
* Create a Connection

<div style="page-break-after: always;"></div>

# Preset | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/preset

On this page

You can use [Preset](https://preset.io/), a cloud service for Superset, to query and visualize data.

## Supported Authentication Method

Use a personal access token (PAT) obtained from a project.
To obtain one, follow the steps in [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).
After you obtain a PAT, it is recommended that you URL-encode it. To encode it locally on your system, you can follow these steps:

1. In a browser window, right-click an empty area of the page and select **Inspect** or **Inspect Element**, depending on your browser.
2. In the top bar of the inspection pane, click **Console**.
3. Type `encodeURIComponent("<PAT>")`, where `<PAT>` is the personal access token that you obtained from Dremio. The URL-encoded PAT appears in red on the next line. You can highlight it and copy it to your clipboard.

## Prerequisite

Obtain the ID of the project that you want to connect to in Dremio. To obtain the ID, follow these steps inside the project:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **General Information** in the project settings sidebar.
3. Copy the project ID to your system clipboard.

## Create a Connection

1. Click **Settings** in the top-right corner, and select **Database Connections** under **Data**.
2. Click the **+Database** button in the top-right corner.
3. Select **Other** from the **Supported Databases** field of the Connect a Database dialog.
4. In the **Display Name** field, specify any name you prefer.
5. In the **Connect a Database** dialog, follow these steps:

   1. Select **Other** from the **Supported Databases** field.
   2. In the **Display Name** field, name the new connection.
   3. In the **SQLALCHEMY URI** field, specify a URI that is in this format. Use an ampersand in front of each additional property that you add:SQLAlchemy URI format

   ```
   dremio://$token:<PAT>@sql.dremio.cloud:443/<project-ID>;ssl=1[;<option>=<value>[;...]]
   ```

   * `<PAT>`: The URL-encoded personal access token that you obtained from Dremio. See Supported Authentication Method.
   * `<project-ID>`: The ID of the project that you want to connect to. See Prerequisite for the steps to obtain the ID.
   * `[;<option>=<value>[;...]]`: One or more optional [encryption properties](/dremio-cloud/explore-analyze/client-apps/drivers/jdbc-legacy#encryption-parameters). Separate each property with a semicolon (`;`).Example SQLAlchemy URI

   ```
   dremio://$token:hoYL2mqORpOv1Lq5WNOT-A-REAL-PATq5yeHEYon%2BOT0VHM0JYS%2BCMH7kpL%2BPQ%3D%3D@sql.dremio.cloud:443/1df71752-NOT-A-PROJECT-ID-990e6b194aa4;ssl=1
   ```

   1. Test the connection. If the test fails, check the syntax and values in the connection URI.
   2. Click **Connect**.

Was this page helpful?

* Supported Authentication Method
* Prerequisite
* Create a Connection

<div style="page-break-after: always;"></div>

# Astrato | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/astrato

On this page

[Astrato](https://astrato.io/) is a no-code framework to build powerful data visualizations and custom data applications that actively drive better business decisions.

## Supported Authentication Method

Authenticate to Dremio from Astrato by using a personal access token (PAT). To create one, see [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

## Create a Connection to Dremio

1. In Astrato, click **Data** in the left-hand navigation bar.
2. On the Data page, follow either of these sets of steps:
   * Create a connection from the **Data Views** section.
     1. Click **Data Views**.
     2. In the top-right corner, click **New Data View**.
   * Create a connection from the **Data Connections** section.
     1. Click **Data Connection**.
     2. In the top-right corner of the page, click **New connection**.
3. In the Create connection page, click the **Dremio** tile.
4. In the **Host** field, follow either of these steps:
   * If your Dremio organization is in the [European control plane](/dremio-cloud/about/regions), leave the default value of `eu.dremio.cloud`.
   * If your Dremio organization is in the [US control plane](/dremio-cloud/about/regions), specify `dremio.cloud`.
5. In the **Personal Access Token** field, paste your PAT.
6. Click **Test connection**.
7. In the Connect to Dremio page, follow these steps:
   1. Select the project that you want to connect to in your organization.
   2. Select the folder that you want to connect to in your project.
   3. Click **Connect**.

You can now define a data view from data that resides in the folder that you connected to.

Was this page helpful?

* Supported Authentication Method
* Create a Connection to Dremio

<div style="page-break-after: always;"></div>

# DBeaver | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/dbeaver

On this page

You can run SQL from [DBeaver](https://dbeaver.io/) to explore your data in your data lakes and relational databases through Dremio.

## Supported Versions

You can use any version of DBeaver for Linux, MacOS, or Windows, except for version 23.0.2.202304091457.

## Supported Authentication Method

Authenticate to Dremio by using a personal access token. To create one, see [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

## Prerequisites

* Download the [Arrow Flight SQL JDBC driver](https://www.dremio.com/drivers/jdbc/).
* For MacOS, ensure you have the latest version of Java Runtime Environment (JRE).

## Connect to Dremio

### Step 1: Add the JDBC Driver

You only need to add the Arrow Flight SQL JDBC driver once. You can skip this step if DBeaver already lists this driver in its Driver Manager dialog. To add the JDBC driver, follow these steps:

1. In the menubar, select **Database** > **Driver Manager**.
2. In the Driver Manager dialog, click **New**.
3. In the Settings section, follow these steps:

   1. In the **Name** field, specify a name for the driver, such as "Arrow Flight SQL JDBC Driver".
   2. In the **Driver Type** field, ensure that **Generic** is the selected driver type.
   3. In the **Class Name** field, specify `org.apache.arrow.driver.jdbc.ArrowFlightJdbcDriver`.
   4. In the **URL Template** field, specify `jdbc:arrow-flight-sql://data.dremio.cloud:443/` .
   5. In the **Default Port** field, specify `443`.
4. In the Libraries section, click **Add File** and select the `.jar` file for the Arrow Flight SQL JDBC driver.
5. Click **OK**.

### Step 2: Create a Connection

Once you've added the Arrow Flight SQL JDBC driver, follow these steps to create a connection to Dremio:

1. Select **Database** > **New Connection from JDBC URL**.
2. In the dialog that follows, enter `jdbc:arrow-flight-sql://data.dremio.cloud:443/`. At this point, DBeaver lists the driver in the **Drivers** field. If the driver is not immediately suggested, type and then delete a character in the input field to refresh suggestions.
3. Select the JDBC driver and click **Next**.
4. In the Connect to a Database dialog, follow these steps:

   1. Select **URL** as the value for **Connect By**.
   2. In the JDBC URL field, append `?token=<encoded_pat>` to the URL and replace `<encoded_pat>` with your URL-encoded personal access token.

      note

      If connecting to a non-default project, you must also append `&catalog=<project_id>` to the URL and replace `<project_id>` with your project ID.
   3. (Optional) Click **Test Connection**. If the connection works, the **Connection Test** dialog opens and indicates that DBeaver is able to connect to Dremio. The connection is not held open. Click **OK**.
5. Click **Finish**.

Was this page helpful?

* Supported Versions
* Supported Authentication Method
* Prerequisites
* Connect to Dremio
  + Step 1: Add the JDBC Driver
  + Step 2: Create a Connection

<div style="page-break-after: always;"></div>

# Tableau | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/tableau

On this page

Connect [Tableau](https://www.tableau.com/) to Dremio to derive powerful insights from your data and create real-time dashboards.

note

When using Tableau with Dremio, avoid using periods in space or dataset names. Due to differences in hierarchy support, periods in paths are treated as separators, resulting in errors when navigating or selecting spaces or datasets with periods in their names.

You can connect from your Tableau application to Dremio in either of two ways:

* Configure a reusable connection in Tableau Desktop, Tableau Server, or Tableau Cloud.
* Connect to a specific dataset by downloading the `.tds` file from Dremio and opening it in Tableau Desktop.

## Supported Versions

| Product | Supported Versions |
| --- | --- |
| Tableau Desktop | 2022.1 and later |
| Tableau Server | 2022.1 and later |
| Tableau Cloud | Latest version deployed by Tableau |

## Supported Authentication Methods

From Tableau, you can authenticate to Dremio with a username and password, or with a [personal access token (PAT)](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat) that can be obtained from the Dremio console.

You can also configure single sign-on (SSO) through OAuth 2.0. For steps on how to configure SSO, see Enable SSO to Dremio from Tableau.

## Tableau Desktop

Tableau Desktop includes a native connector that you can use to connect to Dremio.

### Prerequisites for Using the Dremio JDBC Driver (Legacy)

To connect to Dremio, you'll also need to install the Dremio JDBC driver. Download the Dremio JDBC driver and copy it to the Tableau Desktop's `Drivers` folder.

Download driver for macOS by running this command in a Terminal window

```
curl -L https://download.dremio.com/jdbc-driver/dremio-jdbc-driver-LATEST.jar -o ~/Library/Tableau/Drivers/dremio-jdbc-driver-LATEST.jar
```

Download driver for Windows by running this command in a PowerShell window

```
Invoke-WebRequest -Uri "https://download.dremio.com/jdbc-driver/dremio-jdbc-driver-LATEST.jar" -OutFile "C:\Program Files\Tableau\Drivers\dremio-jdbc-driver-LATEST.jar"
```

### Prerequisites for Using the Arrow Flight SQL JDBC Driver

The Tableau Desktop 2025.1+ connector for Dremio supports Arrow Flight SQL JDBC in place of the Dremio JDBC driver (Legacy). To change the driver, download the Arrow Flight SQL JDBC driver, copy it to Tableau Desktop's `Drivers` folder, and select the **Use Arrow Flight SQL Driver (preview)** option in the **Advanced** tab of the connection dialog.

Download driver for macOS by running this command in a Terminal window

```
curl -L https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/18.3.0/flight-sql-jdbc-driver-18.3.0.jar -o ~/Library/Tableau/Drivers/flight-sql-jdbc-driver-18.3.0.jar
```

Download driver for Windows by running this command in a PowerShell window

```
Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/18.3.0/flight-sql-jdbc-driver-18.3.0.jar" -OutFile "C:\Program Files\Tableau\Drivers\flight-sql-jdbc-driver-18.3.0.jar"
```

### Steps for Connecting

To create a Dremio source in Tableau Desktop:

1. Open Tableau Desktop. If you already had Tableau Desktop open, restart the application. Under the **To a Server** section in the **Connect** panel, click **More**.
2. Select **Dremio**. The **Dremio** connection dialog opens.
3. In the **Product** field, select **Dremio Cloud**.
4. In the **Region** field, select the Dremio control plane in which your Dremio organization is located: `US` or `Europe`. For Tableau 2024.3 or before, in the **Server** field, select `sql.dremio.cloud (US)` or `sql.eu.dremio.cloud (EU)`.
5. In the **Authentication** field, select **Personal Access Token** or **OAuth 2.0**.
   * If you selected **Personal Access Token**, in the **Password** field, specify your [PAT](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
   * If you selected **OAuth 2.0**, specify one of these URLs in the **Dremio Authentication Server** field:
     + If your Dremio organization is on the US control plane: `https://login.dremio.cloud`
     + If your Dremio organization is on the EU control plane: `https://login.eu.dremio.cloud`
6. (Optional) In the **Project** field, if your datasets are in a non-default project of your Dremio organization or you do not have access to the default project, paste the ID of the project that you want to connect to. To obtain the project ID, see [Obtain the ID of a project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).
7. (Optional for Tableau 2025.1+) If you are using the Arrow Flight SQL JDBC driver, in the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option. Ensure that you have the Arrow Flight SQL JDBC driver [downloaded](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc).
8. (Optional) In the **Advanced** tab, specify an **Engine** to run queries on.
9. Click **Sign In**.

### Create a Live Connection to a Dataset from Dremio

You can generate a Tableau Datasource (`.tds`) file that represents a live connection to a dataset that is in Dremio. No actual data is stored in this file, and you can think of it as a shortcut to a Tableau session with a preconfigured view of your data.

note

* The `.tds` file download option must be enabled for users to have access to this feature. To enable this feature, see Enable the .tds File Download in the Dremio Console.
* OAuth is the only supported authentication mechanism for `.tds` files.

To download a `.tds` file:

1. On the Datasets page of your Dremio project, find the dataset you want to work with and open the Details panel for the dataset.
2. Click the button that displays the Tableau logo. Dremio downloads a `.tds` file to your system.
3. Open the `.tds` file.
4. Authenticate to Dremio in the browser window that Tableau opens. The dataset will open in Tableau Desktop.

## Tableau Server

Tableau Server includes a native connector that you can use to connect to Dremio.

### Prerequisites for Using the Dremio JDBC (Legacy) Driver

To connect to Dremio, you'll need to install the Dremio JDBC driver. Download the Dremio JDBC driver and copy it to the `Drivers` folder.

Download driver for Windows by running this command in a PowerShell window

```
Invoke-WebRequest -Uri "https://download.dremio.com/jdbc-driver/dremio-jdbc-driver-LATEST.jar" -OutFile "C:\Program Files\Tableau\Drivers\dremio-jdbc-driver-LATEST.jar"
```

Download driver for Linux by running this command in a command-line window

```
curl -L https://download.dremio.com/jdbc-driver/dremio-jdbc-driver-LATEST.jar -o /opt/tableau/tableau_driver/jdbc/dremio-jdbc-driver-LATEST.jar
```

### Prerequisites for Using the Arrow Flight SQL JDBC Driver

The Tableau Server 2025.1+ connector for Dremio supports Arrow Flight SQL JDBC in place of the Dremio JDBC driver (Legacy). To change the driver, download the Arrow Flight SQL JDBC driver, copy it to the `Drivers` folder, and select the **Use Arrow Flight SQL Driver (preview)** option in the **Advanced** tab of the connection dialog.

Download driver for Windows by running this command in a PowerShell window

```
Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/18.3.0/flight-sql-jdbc-driver-18.3.0.jar" -OutFile "C:\Program Files\Tableau\Drivers\flight-sql-jdbc-driver-18.3.0.jar"
```

Download driver for Linux by running this command in a command-line window

```
curl -L https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/18.3.0/flight-sql-jdbc-driver-18.3.0.jar -o /opt/tableau/tableau_driver/jdbc/flight-sql-jdbc-driver-18.3.0.jar
```

### Steps for Connecting

To create a Dremio source in Tableau Server:

1. In a web browser, navigate to your Tableau Server site.
2. In your workbook, click **Add a Data Source**. Alternatively, you can [publish an existing data source](https://help.tableau.com/current/pro/desktop/en-us/publish_datasources.htm) to Tableau Server.
3. In the **Connect to Data** dialog, select **Dremio** under the **Connectors** tab.
4. In the **Dremio** connection dialog, for the **Product** field, select **Dremio Cloud**.
5. In the **Region** field, select the Dremio control plane in which your Dremio organization is located: `US` or `Europe`. For Tableau 2024.3 or before, in the **Server** field, select `sql.dremio.cloud (US)` or `sql.eu.dremio.cloud (EU)`.
6. In the **Authentication** field, select **Personal Access Token** or **OAuth 2.0**.
   * If you selected **Personal Access Token**, in the **Password** field, specify your [PAT](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
   * If you selected **OAuth 2.0**, specify one of these URLs in the **Dremio Authentication Server** field:
     + If your Dremio organization is on the US control plane: `https://login.dremio.cloud`
     + If your Dremio organization is on the EU control plane: `https://login.eu.dremio.cloud`
7. (Optional) In the **Project** field, if your datasets are in a non-default project of your Dremio organization or you do not have access to the default project, paste the ID of the project that you want to connect to. To obtain the project ID, see [Obtain the ID of a project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).
8. (Optional for Tableau 2025.1+) If you are using the Arrow Flight SQL JDBC driver, in the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option. Ensure that you have the Arrow Flight SQL JDBC driver [downloaded](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc).
9. (Optional) In the **Advanced** tab, specify an **Engine** to run queries on.
10. Click **Sign In**.

## Tableau Cloud

Tableau Cloud includes a native connector that you can use to connect to Dremio.

note

The Tableau Cloud 2025.1 connector for Dremio has an option to use the [Arrow Flight SQL JDBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc) driver in place of the Dremio JDBC driver to power the connection to Dremio. In the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option.

To create a Dremio source in Tableau Cloud:

1. In a web browser, navigate to your Tableau Cloud site.
2. Click **New** > **Published Data Source** to create a reusable data source or **Data** > **Add a Data Source** from within a workbook. Alternatively, you can [publish an existing data source](https://help.tableau.com/current/pro/desktop/en-us/publish_datasources.htm) to Tableau Cloud.
3. In the **Connect to Data** dialog, select Dremio under the Connectors tab.
4. In the **Dremio** connection dialog, for the **Product** field, select **Dremio Cloud**.
5. In the **Region** field, select the Dremio control plane in which your Dremio organization is located: `US` or `Europe`.
6. In the **Authentication** field, select **Personal Access Token** or **OAuth 2.0**.
   * If you selected **Personal Access Token**, in the **Password** field, specify your [PAT](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
   * If you selected **OAuth 2.0**, specify one of these URLs in the **Dremio Authentication Server** field:
     + If your Dremio organization is on the US control plane: `https://login.dremio.cloud`
     + If your Dremio organization is on the EU control plane: `https://login.eu.dremio.cloud`
7. (Optional) In the **Project** field, if your datasets are in a non-default project of your Dremio organization or you do not have access to the default project, paste the ID of the project that you want to connect to. To obtain the project ID, see [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).
8. (Optional for Tableau 2025.1+) If you are using the Arrow Flight SQL JDBC driver, in the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option.
9. (Optional) In the **Advanced** tab, specify an **Engine** to run queries on.
10. Click **Sign In**.

## Advanced Configuration

### Enable the `.tds` File Download in the Dremio console

`ADMIN` privileges are required to make updates to this setting.

To enable users to download `.tds` files for datasets in Dremio, follow these steps:

1. In the Dremio console, click ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **BI Applications** in the project settings sidebar.
3. Select the **Tableau** tab.
4. Toggle the **Enable Tableau Desktop** setting on.

After the organization administrator completes these steps, refresh your browser window.

### Enable SSO to Dremio from Tableau

SSO using OAuth 2.0 is supported by Tableau Desktop 2022.3 or later, Tableau Server, and Tableau Cloud.

Users of Tableau Desktop will use SSO authentication whether connecting directly to Dremio or connecting through a `.tds` file downloaded from Dremio. If you want to use SSO to authenticate when connecting to Dremio through a `.tds` file, ensure that SSO is enabled and configured for your Dremio cluster before the file is downloaded.

To enable SSO to Dremio from Tableau, ensure that your Dremio cluster has SSO configured with your [identity provider](/dremio-cloud/security/authentication/idp/) and follow these steps:

1. For Tableau Server only, follow the configuration steps.
2. Follow the steps to enable SSO to Dremio from Tableau.

#### Configure SSO for Tableau Server

note

**Use OAuth 2.0 with Tableau Server**
If you are using Tableau Server and you want to use OAuth 2.0 to authenticate to Dremio, you must have TLS enabled for Tableau Server for OAuth 2.0 to work. See [Example: SSL Certificate - Generate a Key and CSR](https://help.tableau.com/current/server-linux/en-us/ssl_cert_create.htm) in the Tableau's documentation for additional information.

To configure SSO using [OAuth for Tableau Server](https://tableau.github.io/connector-plugin-sdk/docs/oauth), follow these steps:

1. Run the following command in the Tableau Services Manager (TSM) command line. The only variable that you need to set the value for is `<tableau-server-domain-name-or-ip>`, which is the domain name or IP of your Tableau Server deployment:

   Configure OAuth for Tableau Server

   ```
   tsm configuration set -k oauth.config.clients -v "[{\"oauth.config.id\":\"dremio\", \"oauth.config.client_id\":\"https\:\/\/connectors.dremio.app\/tableau\", \"oauth.config.client_secret\":\"test-client-secret\", \"oauth.config.redirect_uri\":\"https://<tableau-server-domain-name-or-ip>/auth/add_oauth_token\"}]" --force-keys
   ```
2. To apply the changes to Tableau Server, run the command `tsm pending-changes apply`.

#### Configure Dremio

To enable SSO authentication to Dremio from Tableau:

1. In the Dremio console, click ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **BI Applications** in the project settings sidebar.
3. On the BI Applications page, click **Tableau**.
4. Ensure that **Enable single sign-on for Tableau** is toggled on.
5. **For Tableau Server only:** In the **Redirect URIs** field, paste in the redirect URI for your Tableau Server. If you have set up more than one Tableau Server, you can add multiple URIs, separating them with commas. Each URI uses this format, where `<tableau-server>` is the hostname or IP address of Tableau Server:

   Redirect URI for Tableau Server

   ```
   https://<tableau-server>/auth/add_oauth_token
   ```

### Customize the Connection String

If you want to add JDBC parameters to the JDBC URL that Tableau generates for connections to Dremio, parameters other than those Tableau sets through the Dremio connection dialog, see [Use a Properties file to customize a JDBC connection](https://help.tableau.com/current/pro/desktop/en-us/connect_customize.htm#use-a-properties-file-to-customize-a-jdbc-connection) in the Tableau documentation.

### Manually Install the Dremio Connector

If you are previewing a feature that hasn't been released or you have been provided a `.taco` file with a fix that hasn't been released, you can manually install this version of the Dremio connector for temporary use.

To manually install the connector:

1. Download the [`dremio.taco` file](https://download.dremio.com/tableau-connector/).
2. Move the `dremio.taco` file:

   Copy dremio.taco file on macOS

   ```
   cp <download-location>/dremio.taco ~/Library/Tableau/Connectors/
   ```

   Copy dremio.taco file on Windows

   ```
   copy C:\<download-location>\dremio.taco "C:\Program Files\Tableau\Connectors"
   ```

   Move dremio.taco file for Linux (Tableau Server only)

   ```
   mv <download-location>/dremio.taco /opt/tableau/connectors/dremio.taco
   ```
3. (Optional) If a new version of the Dremio JDBC driver is required, download it and copy it to Tableau Desktop's `Drivers` folder by running the following command:

   Download driver for macOS

   ```
   curl https://download.dremio.com/jdbc-driver/dremio-jdbc-driver-LATEST.jar -o -l ~/Library/Tableau/Drivers/dremio-jdbc-driver-LATEST.jar
   ```

   Download driver for Windows

   ```
   Invoke-WebRequest -Uri "https://download.dremio.com/jdbc-driver/dremio-jdbc-driver-LATEST.jar" -OutFile "C:\Program Files\Tableau\Drivers\dremio-jdbc-driver-LATEST.jar"
   ```

   For Linux, download the driver from the [download site](https://download.dremio.com/jdbc-driver/?_ga=2.148321079.1016122501.1667783452-235854462.1630284576&_gac=1.263316990.1664550761.CjwKCAjwp9qZBhBkEiwAsYFsb0x4InlcRP7Rv4XsjamZQHhJILHJWOtBOu30xZC1QwvEXF8cPFs1HhoCB-kQAvD_BwE) and move it by using this command:
   Download driver for Linux (Tableau Server only)

   ```
   mv <download-location>/dremio-jdbc-driver-LATEST.jar /opt/tableau/tableau_driver/jdbc/dremio-jdbc-driver-LATEST.jar
   ```
4. Now you can connect to Dremio from Tableau Desktop. or Tableau Server.

Was this page helpful?

* Supported Versions
* Supported Authentication Methods
* Tableau Desktop
  + Prerequisites for Using the Dremio JDBC Driver (Legacy)
  + Prerequisites for Using the Arrow Flight SQL JDBC Driver
  + Steps for Connecting
  + Create a Live Connection to a Dataset from Dremio
* Tableau Server
  + Prerequisites for Using the Dremio JDBC (Legacy) Driver
  + Prerequisites for Using the Arrow Flight SQL JDBC Driver
  + Steps for Connecting
* Tableau Cloud
* Advanced Configuration
  + Enable the `.tds` File Download in the Dremio console
  + Enable SSO to Dremio from Tableau
  + Customize the Connection String
  + Manually Install the Dremio Connector

<div style="page-break-after: always;"></div>

# Deepnote | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/deepnote

On this page

You can use [Deepnote](https://deepnote.com/) to explore data in Dremio with Python and SQL.

## Supported Authentication Method

Use a personal access token (PAT) obtained from Dremio. To create a PAT, follow the steps in the section [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

## Create an Integration with Dremio

1. After logging into Deepnote, click **Integrations** on the left.
2. Scroll down to **Create new integration**.
3. Under **Data warehouses & lakes**, click **Dremio**.
4. Specify a name for the integration.
5. In the **Host name** field, specify either `data.dremio.cloud` (Dremio's US control plane) or `data.eu.dremio.cloud` (Dremio's European control plane).
6. In the **Port** field, specify the number 443.
7. (Optional) In the **Schema** field, specify the database schema to use by default when a schema is not given in a query.
8. In the **Token** field, paste the PAT that you obtained from Dremio Cloud.
9. Click **Create integration**.

note

Do not toggle on the **Use SSH** switch. Dremio integrations do not support SSH tunnels.

Deepnote gives you the option of associating the integration with a project immediately. If you click **Skip**, the integration is listed under **Workspace integrations** on the **Integrations** page.

Was this page helpful?

* Supported Authentication Method
* Create an Integration with Dremio

<div style="page-break-after: always;"></div>

# Drivers | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/

Dremio provides Arrow Flight SQL ODBC and JDBC drivers:

* [Arrow Flight SQL JDBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc/)
* [Arrow Flight SQL ODBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/)

Dremio also supports the [Dremio JDBC (Legacy)](/dremio-cloud/explore-analyze/client-apps/drivers/jdbc-legacy).

note

To connect from supported client applications, follow the connection steps for that specific application rather than installing drivers separately. For example, to connect from Tableau, follow the steps in [Tableau](/dremio-cloud/explore-analyze/client-apps/tableau/), which include driver installation instructions.

Was this page helpful?

<div style="page-break-after: always;"></div>

# ThoughtSpot | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/thoughtspot

On this page

You can use [ThoughtSpot](https://www.thoughtspot.com/) to search directly against your data in Dremio for live analytics and actionable insights.

## Supported Versions

Dremio supports ThoughtSpot cloud 8.3 and ThoughtSpot software 7.2.1.

## Supported Authentication Methods

Use a personal access token (PAT) obtained from Dremio. To create a PAT, follow the steps in the section [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

If you want to use an OAuth application for authentication, you will first need to [add the OAuth application](/dremio-cloud/security/authentication/app-authentication/oauth-apps) and then copy the client ID.

## Prerequisites

If you want to connect to a specific project in Dremio, copy the ID of the project. See [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project) for the steps. After you obtain it, save it somewhere that you can retrieve it from during the procedure.

## Create a Connection

note

While you're using the connection, the data fields that you create, modify, and delete in Dremio are reflected as table columns in ThoughtSpot. To account for new or outdated fields, you will need to go back into the data connection to check or uncheck the columns that you want added or removed on the Select Tables page.

1. Log into ThoughtSpot.
2. Navigate to **Data** > **Connections** > **Add Connection**.
3. On the Choose Your Data Warehouse page, specify your data connection details:

   * In the **Name your connection** field, enter a name.
   * (Optional) In the **Describe your connection** field, enter a brief description.
   * For the **Choose your data warehouse** field, select **Dremio**.
4. Click **Continue**.
5. On the Dremio Connection Details page, to provide your authentication credentials, follow either of these steps:

   a. To use a personal access token that you obtained from Dremio, select **Use Service Account**.

   b. To use an OAuth application that you added in Dremio, select **Use OAuth**.
6. In the **Host** field, enter sql.dremio.cloud.
7. In the **Port** field, enter 443.
8. Follow either of these steps based on the authentication type that you chose:

   a. For using a personal access token:

   * In the **User** field, type `$token`.
   * In the **Password** field, paste your personal access token.
   * (Optional) In the **Project ID** field, paste the project ID.

   b. For using an OAuth application:

   * In the **Project ID** field, paste the project ID.
   * In the **OAuth Client ID** field, paste the client ID.
   * In the **OAuth Client Secret** field, enter your password.
   * In the **Auth URL** field, enter the authorization URL of the application.
   * In the **Access Token URL** field, enter the URL of the access token.
9. (Optional) In the **Schema** field, enter the project schema.
10. Click **Continue**.
11. On the Select Tables page, you can see all the data tables and views from Dremio. To select tables and columns from that list, select a table and check the boxes next to the columns for that table.
12. Click **Create Connection**.
13. In the **Create Connection** dialog, click **Confirm**.

Was this page helpful?

* Supported Versions
* Supported Authentication Methods
* Prerequisites
* Create a Connection

<div style="page-break-after: always;"></div>

# DbVisualizer | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/dbvisualizer

On this page

You can use [DbVisualizer](https://www.dbvis.com/) to query and visualize data by means of Dremio.

## Supported Versions

You can use any version of DbVisualizer, as long as you use Dremio JDBC Driver 14.0.0 or later.

## Supported Authentication Methods

There are two methods of authenticating that you can choose from when you connect from DbVisualizer to Dremio:

* Use Microsoft Entra ID as an enterprise identity provider

  To configure Microsoft Entra ID, see [Microsoft Entra ID](/dremio-cloud/security/authentication/idp/microsoft-entra-id/).

  note

  You can use Microsoft authentication only if the admin for your Dremio organization has enabled it.
* Use a personal access token (PAT) obtained from Dremio

  To create a PAT, follow the steps in [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat).

## Prerequisites

* [Download the Dremio JDBC driver](https://www.dremio.com/drivers/jdbc).
* If you do not want to connect to the default project in your Dremio organization, copy the ID of the Dremio Cloud project that you want to connect to. See [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project) for the steps. After you obtain it, save it somewhere that you can retrieve it from during the procedure.

## Add Dremio's JDBC Driver to DbVisualizer's Driver Manager

1. Launch DbVisualizer.
2. Select **Tools** > **Driver Manager**.
3. In the **Driver Name** list of the **Driver Manager** dialog, select **Dremio**.
4. Click the folder icon to find and select the downloaded Dremio JDBC driver.
5. Close the **Driver Manager** dialog.

## Create a Connection

1. Launch DbVisualizer.
2. Select **Database** > **Create Database Connection**.
3. In the **Use Connection Wizard?** dialog, click **No Wizard**.
4. Name the connection.
5. Ensure that these default values are set:

   | Field | Value |
   | --- | --- |
   | **Settings Format** | Server Info |
   | **Database Type** | Auto Detect (Dremio) |
   | **Driver** | Dremio |
   | **Connection Type** | Direct |
6. In the **Database Server** field, specify `sql.dremio.cloud`.
7. In the **Database Port** field, specify `443`.
8. In the **Database Userid** and **Database Password** fields, specify your authentication credentials:

   * If you want to authenticate by using a Microsoft account and password, and Microsoft Entra ID is configured as an enterprise identity provider for Dremio Cloud, specify the username and password for the account.
   * If you want to authenticate by using a personal access token, specify these values:

     + In the **Username** field, type `$token`.
     + In the **Password** field, paste your personal access token.
9. Click **Properties**.
10. Click the plus sign to add a new parameter.
11. Name the parameter `ssl`.
12. Specify `true` for the value of this parameter.
13. If you do not want to connect to the default project in your organization, follow these steps:

    a. Click the plus sign to add a new parameter.

    b. Name the parameter `PROJECT_ID`.

    c. In the `Value` field, paste the ID of the project that you want to connect to.
14. Click **Apply**.
15. Click **Connect**.

If the connection works, DbVisualizer displays a message as shown below (the reported version numbers might differ):

`Dremio Server 20.0.0-202112201840340507-df2e9b7c`

`Dremio JDBC Driver 19.1.0-202111160130570172-0ee00450`

You can now expand your Dremio connection to see a list of the data sources that are in the project.

Was this page helpful?

* Supported Versions
* Supported Authentication Methods
* Prerequisites
* Add Dremio's JDBC Driver to DbVisualizer's Driver Manager
* Create a Connection

<div style="page-break-after: always;"></div>

# Apache Superset | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/apache-superset

On this page

You can use [Superset](https://superset.apache.org/) to query and visualize data.

## Supported Versions

* Superset 1.5.3 and later
* Dremio SQLAlchemy connector 3.0.2 and later

## Supported Authentication Method

Use a personal access token (PAT) created in a project. To create one, follow the steps [Create a PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat). After you obtain a PAT, it is recommended that you URL-encode it. To encode it locally on your system, you can follow these steps:

1. In a browser window, right-click an empty area of the page and select **Inspect** or **Inspect Element**, depending on your browser.
2. In the top bar of the inspection pane, click **Console**.
3. Type `encodeURIComponent("<PAT>")`, where `<PAT>` is the personal access token that you obtained from Dremio. The URL-encoded PAT appears in red on the next line. You can highlight it and copy it to your clipboard.

## Prerequisites

If you installed Superset according to [the instructions for installing from scratch](https://superset.apache.org/docs/installation/installing-superset-from-scratch), install the Dremio SQLAlchemy Connector on the system or in the VM where Apache Superset is running. Instructions are in the [sqlalchemy\_dremio repository](https://github.com/narendrans/sqlalchemy_dremio) in GitHub.

## Create a Connection

1. If you are using a version of Superset earlier than 2.1.0, follow these steps:

   1. Select **Data** > **Databases** in the menu bar at the top of the screen.
   2. Click the **Database** button in the top-right corner of the screen.
2. If you are using version 2.1.0 or later of Superset, follow these steps:

   1. Click **Datasets** in the menu bar at the top of the screen.
   2. Click the plus (+) icon in the top-right corner.
   3. Select **Data** > **Connect database**.
3. In the **Connect a Database** dialog, follow these steps:

   1. Select **Other** from the **Supported Databases** field.
   2. In the **Display Name** field, name the new connection.
   3. In the **SQLALCHEMY URI** field, specify a URI that is in this format. Use an ampersand in front of each additional property that you add:SQLAlchemy URI format

   ```
   dremio+flight://data.dremio.cloud:443/[<schema>]?token=<PAT>&UseEncryption=true[&<option>=<value>[&...]]
   ```

   * `<schema>`: The name of the database schema to use by default when a schema is not given in a query. Providing a schema is optional. Specifying a schema does not prevent queries from being issued for other schemas; such queries must explicitly include the schema.
   * `<PAT>`: The URL-encoded personal access token that you obtained from Dremio. See Supported Authentication Method.
   * `[&<option>=<value>[&...]]` is one or more optional properties from the SSL connection properties and Advanced properties tables below. Separate each property with an ampersand (`&`).Example SQLAlchemy URI

   ```
   dremio+flight://data.dremio.cloud:443/?token=dOOfxnJlTnebGu7Beta9NOT-A-REAL-PATyfOoNbJwEMep7UjkQu0JTsFXpYGm==&UseEncryption=true
   ```

    
   4. Test the connection. If the test fails, check the syntax and values in the connection URI.
   5. Click **Connect**.

## SSL Connection Properties

Use the following properties to configure SSL encryption and verification methods:

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| UseEncryption | integer | Forces the client to use an SSL-encrypted connection to communicate with Dremio. Accepted value: `true`, the client communicates with Dremio only using SSL encryption. This is the only possible value. | true |
| disableCertificateVerification | integer | Specifies whether to verify the host certificate against the trust store. Accepted values: `false`, verifies the certificate against the trust store; `true`, does not verify the certificate against the trust store. | false |
| trustedCerts | string | The full path of the .pem file containing certificates trusted by a CA, for the purpose of verifying the server. If this option is not set, defaults to using the trusted CA certificates .pem file. The TLS connection fails if you do not specify a value when UseEncryption is true and disableCertificateVerification is false. | N/A |

## Advanced Properties

| Name | Type | Description | Default Value | Required? |
| --- | --- | --- | --- | --- |
| routing\_engine | string | The engine to route queries to while a connection remains open. | N/A | No |
| routing\_tag | string | The tag to be associated with all queries executed within a connection session. | N/A | No |

Was this page helpful?

* Supported Versions
* Supported Authentication Method
* Prerequisites
* Create a Connection
* SSL Connection Properties
* Advanced Properties

<div style="page-break-after: always;"></div>

# Alteryx Designer | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/alteryx-designer

On this page

You can use Alteryx Designer to quickly prepare, blend, conform, and analyze data from datasets in Dremio.

## Supported Versions

Alteryx Designer 10.6+

## Prerequisite

Download, install, and configure the [ODBC driver for Arrow Flight SQL](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/).

note

* The driver supports 64-bit Windows 10 or later.
* The personal access token (PAT) that you add to the DSN that you configure for the driver determines the Dremio project that the driver connects you to. Ensure that you create your PAT in the correct project.

## Select Dremio as a Data Source

1. In Alteryx Designer, select **File** > **New Workflow**.
2. Drag the **Input Data** tool from the tool palette on to the workflow canvas.
3. In the configuration properties for Input Data, click the arrow on the right side of the **Connect a File or Database** field.
4. In the Data connections dialog, follow these steps:

   a. Select **Recent** and click **Clear List** in the top-right corner if there are any entries on the page.

   b. Select **Data Sources**.

   c. Scroll down to the option **Generic connection**.

   d. Click either **ODBC** or **OleDB**.
5. If you clicked **ODBC**, follow these steps in the ODBC Connection dialog:

   a. In the **Data Source Name** field, select the data source name for the Arrow Flight SQL ODBC driver.

   b. Leave the **User name** and **Password** field blank. The authentication credentials for connecting to Dremio are already present in the user DSN.

   c. Click **OK**.
6. If you clicked **OleDB**, follow these steps in the Data Link Properties dialog:

   a. On the **Provider** tab, select **Microsoft OLE DB Provider for ODBC Drivers**.

   b. Click **Next>>**.

   c. For step 1 on the **Connection** tab, select **Use data source name**, and then select the data source name for the Arrow Flight SQL ODBC driver.

   d. For step 2 on the **Connection** tab, leave the **User name** and **Password** fields blank. The authentication credentials for connecting to Dremio are already present in the user DSN.

   e. (Optional) Click **Test Connection** to find out whether the info you specified on this tab is correct.

   f. Click **OK**.

You can now browse and query datasets that are in Dremio.

Was this page helpful?

* Supported Versions
* Prerequisite
* Select Dremio as a Data Source

<div style="page-break-after: always;"></div>

# Microsoft Power BI | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/microsoft-power-bi

On this page

Connect [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) to visualize your data and create reports.

You can connect Power BI to Dremio in one of the following ways:

* Configure a reusable connection to use in Power BI Desktop, Power BI Gateway, or Power BI Service. Power BI Service can connect to Dremio through DirectQuery or through Power BI Gateway.
* Connect to a specific dataset by downloading the `.pbids` file from Dremio and opening it in Power BI Desktop.

## Supported Authentication Methods

From Power BI, you can authenticate to Dremio with one of the following methods:

* **Personal access token (PAT)**: For details, see [Create a PAT](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
* **Single sign-on (SSO) through OAuth 2.0**: For steps on how to configure SSO, see Enable SSO to Dremio from Power BI.

## Connect to Dremio from Power BI

The Power BI connector for Dremio now supports connectivity through the open-source [Arrow Database Connectivity (ADBC) driver](https://arrow.apache.org/docs/format/ADBC.html), which Dremio highly recommends using to connect to Dremio. To enable reports to use ADBC, see Enable Connectivity with ADBC.

Existing connections will continue to work, but we recommend using the embedded ADBC driver for all new reports and migrating existing reports to ADBC to benefit from improved performance and supportability.

To connect to Dremio from Power BI Desktop:

1. Click **Get data**, search for `Dremio`, select **Dremio Cloud**, and click **Connect**.
2. In the Dremio Cloud dialog, follow these steps:

   a. Use the Flight SQL ADBC driver and in the **Server** field specify which of Dremio's control planes to connect to:

   * If your Dremio organization is on the US control plane: `adbc://data.dremio.cloud`
   * If your Dremio organization is on the EU control plane: `adbc://data.eu.dremio.cloud`

   b. (Optional) In the **Project** field, if your datasets are in a non-default project of your Dremio organization or you do not have access to the default project, paste the ID of the project that you want to connect to. To obtain the project ID, see [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).

   c. (Optional) In the **Engine** field, specify the name of the query-execution engine for your project. For information about query-execution engines, see [Manage Engines](/dremio-cloud/admin/engines/).

   d. (Optional) In the **Native Query** field, specify a SQL query as the data input source.

   e. Under **Data Connectivity mode**, select either **Import** or **DirectQuery**. Click **OK**.

   f. For **Authentication Method**, select **Key** or **Microsoft Account**.

   * **Key**: Paste in the personal access token you obtained from Dremio. For details, see [Create a PAT](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
   * **Microsoft Account**: Click **Sign in**, and then specify your credentials.

note

Creating Dataflows through Power BI Service is also supported. To create a dataflow, click **New** > **Dataflow**. For the data source connection, follow the steps above.

### Create a Live Connection to a Dataset from Dremio

You can generate a Microsoft Power BI Data Source (`.pbids`) file that represents a live connection to a dataset that is in Dremio. No actual data is stored in this file, and you can think of it as a shortcut to a Power BI Desktop session with a preconfigured view of your data.

note

The `.pbids` file download option must be enabled for users to have access to this feature. To enable this feature, see Enable the .pbids file download.

To download a `.pbids` file:

1. On the Datasets page in Dremio, find the dataset you want to work with and open the Details panel for the dataset.
2. Click the button that displays the Power BI logo. Dremio downloads a `.pbids` file to your system.
3. Open the `.pbids` file.
4. Authenticate using a personal access token or your organizational account and click **Load**.

### Connect to Dremio via PrivateLink

Use these instructions to connect to Dremio if your organization uses PrivateLink for secure private connectivity.

#### Prerequisites

* A [PrivateLink](/dremio-cloud/security/privatelink) connection configured in your AWS VPC.
* The November 2025 version of Power BI Desktop.

#### Connect with an Organizational Account

1. In Power BI Desktop, click Get data.
2. In the Get Data dialog, choose Blank Query and click **Connect**.
3. Select Advanced Editor and add the following:

   ```
   let  
    Source = DremioCloud.DatabasesByServerV370("adbc://<orgAlias>.data.privatelink.dremio.cloud", null, null, null, null, "Enabled-PEM", [AuthorizationServerPort=443, AuthorizationServerDomain="<orgAlias>.login.privatelink.dremio.cloud"])  
   in  
    Source
   ```

   where `<orgAlias>` is the organization alias implemented in your [PrivateLink configuration](/dremio-cloud/security/privatelink).
4. Click **Done**.
5. Select **Edit Credentials**.
6. Choose Organizational Account and click **Sign in**.

#### Connect with a Personal Access Token

1. In Power BI Desktop, click Get data, choose Dremio Cloud, and click **Connect**.
2. In the Dremio Cloud connection box, enter the PrivateLink DNS name created in your [PrivateLink configuration](/dremio-cloud/security/privatelink), in the form

   ```
   adbc://<orgAlias>.data.privatelink.dremio.cloud
   ```

   where `<orgAlias>` is your PrivateLink organization alias. Click **OK**.

## Power BI Gateway

To enable Power BI users to connect to Dremio via Power BI Gateway:

1. In Power BI Service, click **...** next to your profile picture at the top-right corner of the browser and navigate to **Settings > Manage gateways**.
2. Under **GATEWAY CLUSTERS**, select the gateway you created previously.
3. Select the checkbox **Allow user's cloud data sources to refresh through this gateway cluster**.
4. At the top of the page, click **Add data sources to use the gateway**. This launches the *Data Source Settings* page.
5. Enter a **Data Source Name**.
6. Select the **Data Source Type** drop-down menu and select **Dremio Cloud**.
7. In the **Server** field, specify which of Dremio's control planes to connect to:

   * If your Dremio organization is on the US control plane: `sql.dremio.cloud`.
   * If your Dremio organization is on the EU control plane: `sql.eu.dremio.cloud`.
8. (Optional) In the **Project** field, if your datasets are in a non-default project of your Dremio organization or you do not have access to the default project, paste the ID of the project that you want to connect to. To obtain the project ID, see [Obtain the ID of a project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).
9. For **Authentication Method**, select **Key** or **Microsoft Account**.

   * **Key**: Paste in the personal access token you obtained from Dremio. For details, see [Create a PAT](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
   * **Microsoft Account**: Click **Sign in**, and then specify your credentials.
10. Ignore the **Engine** field. It is not used.
11. Under **Advanced Settings**, set the **Connection Encryption setting for this data source** to **Encrypted**.
12. Click **Add**. A **Connection Successful** message is shown on top of the Data Source Settings page.

## Advanced Configuration

### Enable Connectivity with ADBC

Dremio supports connectivity through Arrow Database Connectivity (ADBC). To enable this for Power BI Service, see the following options.

#### Enable the ADBC Option for a New Connection

1. In Power BI Desktop, click **Get data**.
2. In the Get Data dialog, locate and select **Dremio Cloud**, and click **Connect**.
3. In the Dremio Cloud dialog, in the **Server** field, enter `adbc://data.dremio.cloud` or `adbc://data.eu.dremio.cloud`, depending on which control plane your Dremio account is on.
4. (Optional) Complete the other fields in the dialog as you normally would.
5. Click **OK**.
6. Authenticate using your preferred method, and click **Connect**.

#### Enable the ADBC Option for an Existing Connection

1. In Power BI Desktop, go to **Data source settings**, select your source, and click **Change source**.
2. In the Dremio Cloud dialog, update the **Server** field to `adbc://data.dremio.cloud` or `adbc://data.eu.dremio.cloud`, depending on which control plane your Dremio account is on. If you're unable to edit the source this way, click **Transform data**, then click **Advanced Editor** in the **Home** tab. In the dialog that appears, update the hostname/server with the `adbc://` prefix, and click **Done**.
3. Click **OK**.
4. Reauthenticate using your preferred method, and click **Connect**.

### Enable the `.pbids` File Download in the Dremio Console

`ADMIN` privileges are required to make updates to this setting.

To enable users to download `.pbids` files for datasets in the Dremio console, follow these steps:

1. Click ![](/images/icons/settings.png) in the side navigation bar and select **Project Settings**.
2. Select **BI Applications** in the projects settings sidebar.
3. Toggle the **Microsoft Power BI Desktop** setting on.

After the organization administrator completes these steps, refresh your browser window.

### Enable SSO to Dremio from Power BI

When Single Sign-On (SSO) is enabled, viewers of reports in Power BI Service run them under their own Power BI username instead of as the user who published the reports, or under the username of the user who set up Power BI Gateway. SSO is supported for DirectQuery mode.

To enable SSO to Dremio from Power BI, ensure that your Dremio organization is configured with [Microsoft Entra ID](/cloud/security/authentication/idp/microsoft-entra-id/) and follow these steps:

1. In the Dremio console, click ![](/images/icons/settings.png) in the side navigation bar and select **Organization Settings**.
2. Select **BI Applications** from the organization settings sidebar.
3. On the BI Applications page, click **Power BI**.
4. Ensure that **Enable single sign-on for Power BI** is toggled on.
5. For **Microsoft Entra Tenant ID**, enter the tenant ID of your Microsoft Entra ID account. The tenant ID of each Microsoft Entra ID account can only be assigned to a single Dremio organization.
6. For **User Claim Mapping**, specify the key of the user claim that Dremio must look up in access tokens to find the username of the user attempting to log in. See [User Claim Mapping](/cloud/security/authentication/app-authentication/external-token#user-claim-mapping) for more information about this field.
7. Click **Save**.
8. In the Power BI Admin portal, select **Tenant settings** and toggle on the **Enabled** switch under **Dremio SSO**.

#### Enable SSO for a DirectQuery Report

To enable SSO for a report that uses DirectQuery:

1. In Power BI Service, open the workspace to which you published the report.
2. Find the dataset that is associated with the report, click the three dots next to its name, and select **Settings**.
3. Expand the **Data source credentials** section and click **Edit credentials**.
4. In the configure dialog, follow these steps:

   1. In the **Authentication method** field, select one of these options:

      * **Key**: Paste your personal access token into the **Account Key** field.
      * **OAuth2**: Authenticate by using your Microsoft ID and password.
   2. In the **Privacy level setting for this data source** field, ensure that **Private** is selected.
   3. Select the check box **Report viewers can only access this data source with their own Power BI identities using DirectQuery**.
   4. Click **Sign in**.

#### Enable SSO for Reports with Power BI Gateway

To enable SSO when you are using Power BI Gateway:

1. In Power BI Service, open the workspace to which you published the report.
2. Find the dataset that is associated with the report, click the three dots next to its name, and select **Settings**.
3. In the settings for the dataset, expand **Gateway connection**.
4. Recreate your data source by following these steps:

   1. Select the **Maps to** field.
   2. Select **Manually add to gateway**.
   3. In the New data source dialog, create a data source that matches the one that you previously used for your dataset. However, give the new data source a different name.
   4. In the **Authentication method** field, select one of these options:

      * **Key**: Paste your personal access token into the **Account Key** field.
      * **OAuth2**: Click **Edit credentials** and select the option **Use SSO via Microsoft Entra ID for DirectQuery queries**.
   5. Click **Create**.
5. Under **Gateway connection**, verify that the new data source is selected in the **Maps to** field.

## Arrow Database Connectivity (ADBC) Limitations

* ADBC is not enabled by default. It must be enabled by the owner of the report.
* NativeQuery is not supported.
* Metadata calls are not cached.
* SSO is not supported in environments that use different domain names for the UI and Flight services.
* Power BI Desktop occasionally caches errors that might affect future connection attempts until the cache is cleared.
* Complex data types such as `MAP` and `INTERVAL` are not supported.
* When using DirectQuery, chaining functions is supported, but some complex scenarios may not work as expected. Complex optional parameters for functions are not supported.

## Troubleshoot Power BI

### Cached Data Issues

If you have previously installed older versions of Power BI Desktop, cached data may interfere with the newer versions of the Flight SQL drivers resulting in connection errors.

#### Problem

For example, when using Flight SQL ADBC, cached connection data in Power BI could cause the following errors:

* `ADBC: IOError [] [FlightSQL] [FlightSQL] unresolved address (Unavailable; GetObjects(GetDBSchemas))`
* `ADBC: IOError [] [FlightSQL] [FlightSQL] connection error: desc = "transport: authentication handshake failed: credentials: cannot check peer: missing selected ALPN property. If you upgraded from a grpc-go version earlier than 1.67, your TLS connections may have stopped working due to ALPN enforcement. For more details, see: https://github.com/grpc/grpc-go/issues/434" (Unavailable; GetObjects(GetDBSchemas))`

#### Solution

Clear the Power BI Desktop cache and any cached data source permissions involving Dremio connections by following these steps:

1. [Clear Power BI Desktop Caches](https://community.fabric.microsoft.com/t5/Desktop/How-to-clear-cache-in-Power-BI-Desktop/m-p/853389#M409501).
2. In Power BI Desktop, go to **File** > **Options and Settings** > **Data Source Settings**.
3. Select **Global Permissions**.
4. Clear all cached connections by clicking **Clear All Permissions**, or select specific Dremio data sources and click **Clear Permissions**.

After completing these steps, try reconnecting to Dremio using the instructions above.

### Large Result Sets

#### Problem

When fetching data from Dremio with ADBC you may see the following error:

* `Unexpected error: [FlightSQL] grpc: received message larger than max (43747370 vs. 16777216) (ResourceExhausted; DoGet: endpoint 0: [])`

#### Solution

By default, the ADBC driver accepts only messages up to 16 MiB in size. This can be fixed by updating the Power BI M expression to customize the connection as follows:

```
let  
    Source = DremioCloud.DatabasesByServerV370("adbc://data.dremio.cloud", null, null, null, null, "Enabled-PEM", [AdbcMaxMessageSize=33554432]) // 32 MiB  
in  
    Source
```

Was this page helpful?

* Supported Authentication Methods
* Connect to Dremio from Power BI
  + Create a Live Connection to a Dataset from Dremio
  + Connect to Dremio via PrivateLink
* Power BI Gateway
* Advanced Configuration
  + Enable Connectivity with ADBC
  + Enable the `.pbids` File Download in the Dremio Console
  + Enable SSO to Dremio from Power BI
* Arrow Database Connectivity (ADBC) Limitations
* Troubleshoot Power BI
  + Cached Data Issues
  + Large Result Sets

<div style="page-break-after: always;"></div>

# Dremio JDBC (Legacy) | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/jdbc-legacy

On this page

You can use the Dremio JDBC driver (Legacy) version 25+ to connect to Dremio from JDBC client applications. This driver is licensed under [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Prerequisites

Java 11 is required as of Dremio JDBC (Legacy) version 25.

note

The [Arrow Flight SQL JDBC driver](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc) is the recommended driver for connectivity to Java-based applications. The Dremio JDBC driver (Legacy) will not be updated or fixed moving forward.

## Supported Authentication Methods

* Use personal access tokens. To generate one, see [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
* Use JSON Web Tokens (JWT) from an external token provider. To use a JWT, you must have OAuth enabled in Dremio. For more information about using JWTs, see [External Token Providers](/dremio-cloud/security/authentication/app-authentication/external-token).

## Download and Install

You can download the JDBC driver from [here](https://www.dremio.com/drivers/jdbc/). The driver does not require installation.

## Connect to Dremio

note

If you are using the JDBC driver to connect to Dremio from a supported client application, refer to the documentation for [creating connections from that application](/dremio-cloud/explore-analyze/client-apps/).

If you want to start with the base JDBC connection string for your Dremio project:

1. Click Project Settings ![](/images/icons/project-settings.png) in the side navigation bar.
2. Select **General Information** in the project settings sidebar.
3. Copy the connection string that is in the **JDBC Connection** field.

To construct a connection string:

1. Set the subprotocol to `jdbc:dremio:`.
2. Set the property `direct` equal to `sql.dremio.cloud:443`.
3. Add one of these types of authentication credentials for connecting from your JDBC client application to Dremio:

   * Use a [personal access token (PAT)](/dremio-cloud/security/authentication/personal-access-token/) in either of the following ways:

     + Set `user` to `$token` and use the PAT as the password when the client application does not support OAuth:

       Use PAT as password when client app does not support OAuth

       ```
       jdbc:dremio:direct=sql.dremio.cloud:443;user=$token;password=<personal-access-token>;
       ```
     + Set `token_type` to `personal_access_token`, use the PAT as the password, and set `username` to null when the client application supports OAuth:

       Use PAT as password

       ```
       jdbc:dremio:direct=sql.dremio.cloud:443;token_type=personal_access_token;password=<personal-access-token>;username=;
       ```
   * Use a [JSON Web Token (JWT)](/dremio-cloud/security/authentication/app-authentication/external-token). You can use a JWT when the tool used with the JDBC driver supports OAuth:

     Use a JWT

     ```
     jdbc:dremio:direct=sql.dremio.cloud:443;token_type=jwt;password=<jwt>;username=;
     ```
4. Set the property `ssl` equal to `true`: `ssl=true;`
5. Add the ID of the project that you are connecting to: `project_id=<project-id>;`
6. (Optional) Route queries to a particular [engine](/dremio-cloud/admin/engines/) in your project, set the property `engine` to the name of an engine: `engine=<engine-name>;`

## Connection Parameters

### Encryption Parameters

To encrypt communication between your JDBC client applications and Dremio,
use the SSL JDBC connection parameters and a fully qualified host name to
configure the JDBC connection string and connect to Dremio.

| SSL JDBC Connection Parameter | Type | Description | Default Value | Required |
| --- | --- | --- | --- | --- |
| disableCertificateVerification | boolean | Controls whether the driver verifies the host certificate against the trust store.  * The driver **will** verify the certificate against the trust store when it is set to `false`. * The driver **will not** verify the certificate against the trust store when the value is set to `true`  . | `false` | No |
| disableHostVerification | boolean | Forces the driver to verify that the host in the certificate is the host being connected to.  * The driver **will** verify the certificate against the host being connected to when it is set to `false`. * The driver **will not** verify the certificate against the host whe it is set to `true`. | `false` | No |
| ssl | boolean | Forces the client to use an SSL encrypted connection to communicate with the Dremio server.  * SSL encryption is disabled with the client when it is set to `false`. * The client communicates with the Dremio server only using SSL encryption when it is set to `true`.   **Note:**  To connect to Dremio, SSL must be enabled. | `false` | Yes |
| trustStoreType | string | The trustStore type. Accepted value is: JKS PKCS12    The following property only applies to **Windows**.  * If the `useSystemTrustStore` parameter is set to true, the accepted values are: `Windows-MY` and `Windows-ROOT`. * Import the certificate into the **Trusted Root Certificate Authorities** and set `trustStoreType=Windows-ROOT`. * Import the certificate into **Trusted Root Certificate Authorities** or **Personal** and set `trustStoreType=Windows-MY`. | `None` | No |
| trustStore | string | Path to the truststore.  If this parameter is not specified, it defaults to Java truststore (`$JAVA_HOME/lib/security/cacerts`) and the trustStorePassword parameter is ignored. | `$JAVA_HOME/lib/security/cacerts` | No |
| useSystemTrustStore | boolean | Bypasses trustStoreType and automatically picks the correct truststore based on the operating system:  * Keychain on MacOS * [Local Machine and Current User Certificate Stores](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores) on Windows * Default truststore on other systems | `true` | No |
| trustStorePassword | string | Password to the truststore. | `None` | No |

### SOCKS Proxy Connection Parameters

If you want to connect to Dremio through a SOCKS proxy, use these connection parameters:

| Parameter | Type | Description | Default Value | Required? |
| --- | --- | --- | --- | --- |
| socksProxyHost | string | The IP address or hostname of the SOCKS proxy. | N/A | Yes |
| socksProxyPort | integer | The port to use on the SOCKS proxy. | 1080 | No |
| socksProxyUsername | string | The username to use for connections. | N/A | No |
| socksProxyPassword | string | The password to use for connections. | N/A | Only if a username is specified. |

### Advanced Parameters

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| quoting | string | Specifies which type of character to use to delimit values in queries. The value can be `BACK_TICK`, `BRACKET`, or `DOUBLE_QUOTE`. | `DOUBLE_QUOTE` |
| routing\_tag | string | When this parameter is set, the specified tag is associated with all queries executed within a session. Rules can check for the presence of a tag with the function "tag()". For more information, see [Workload Management](/dremio-cloud/admin/engines/workload-management). | N/A |
| stringColumnLength | string | The maximum length of data in columns of the STRING datatype and of complex datatypes. The range is 1 to 2147483647. | 1024. |

## Parameterized Queries with Prepared Statements

Dremio supports using parameters in prepared statements for SELECT queries.

The parameter marker is `?` in prepared statements. To execute a prepared statement, you must set the parameter marker with one of the supported data types and set methods.

The example below uses the Date type parameter and the `setDate` set method. For set methods, the first argument is the index of the parameter marker in the SQL query, starting from 1. This example includes only one parameter marker, and the second argument is the value for the parameter marker. After you set the parameter, you can execute the prepared statement by calling the `executeQuery()` method on the prepared statement.

Example prepared statement with parameters

```
public class HelloWorld {  
  public static void main(String[] args) {  
    try (PreparedStatement stmt = getConnection().prepareStatement("SELECT * FROM (values (DATE '2024-02-20'), (null)) AS a(id) WHERE id=?")) {  
      Date date = Date.valueOf(LocalDate.of(2024, 02, 20));  
      stmt.setDate(1, date);  
      try (ResultSet rs = stmt.executeQuery()) {  
        assertThat(rs.getMetaData().getColumnCount()).isEqualTo(1);  
        assertThat(rs.next()).isTrue();  
        assertThat(rs.getDate(1)).isEqualTo(date);  
        assertThat(rs.next()).isFalse();  
      }  
    }  
  }  
}
```

The example below demonstrates how to reuse the same prepared statement by defining a different set method and parameter value.

Example prepared statement with different set method and parameters

```
public class HelloWorld {  
  public static void main(String[] args) {  
    try (PreparedStatement stmt = getConnection().prepareStatement("SELECT * FROM (values (DATE '2024-02-20'), (null)) AS a(id) WHERE id=?")) {  
      Date date = Date.valueOf(LocalDate.of(2024, 02, 20));  
      stmt.setDate(1, date);  
      try (ResultSet rs = stmt.executeQuery()) {  
        assertThat(rs.getMetaData().getColumnCount()).isEqualTo(1);  
        assertThat(rs.next()).isTrue();  
        assertThat(rs.getDate(1)).isEqualTo(date);  
        assertThat(rs.next()).isFalse();  
      }  
      stmt.setDate(1, Date.valueOf(LocalDate.of(2025, 02, 20)));  
      try (ResultSet rs = stmt.executeQuery()) {  
        assertThat(rs.next()).isFalse();  
      }  
    }  
  }  
}
```

The following example shows how to use more than one parameter in a prepared statement.

Example prepared statement with two parameters

```
public class HelloWorld {  
  public static void main(String[] args) {  
    try (PreparedStatement stmt = getConnection().prepareStatement("SELECT * FROM (values (1), (2), (null)) AS a(id) WHERE id = ? OR id < ?")) {  
      stmt.setInt(1, 1);  
      stmt.setInt(2, 3);  
      try (ResultSet rs = stmt.executeQuery()) {  
        assertThat(rs.getMetaData().getColumnCount()).isEqualTo(1);  
        assertThat(rs.next()).isTrue();  
        assertThat(rs.getInt(1)).isEqualTo(1);  
        assertThat(rs.next()).isFalse();  
      }  
    }  
  }  
}
```

### Supported Data Types and Set Methods

To execute a prepared statement, you must set the parameter marker with one of the supported set methods listed in the table below.

| Column Data Type | Supported Set Methods |
| --- | --- |
| Integer | setInt(), setShort(), setNull() |
| Numeric | setInt(), setShort(), setLong(), setBigDecimal(), setNull() |
| Decimal | setShort(), setInt(), setLong(), setBigDecimal(), setNull() |
| BigInt | setShort(), setInt(), setLong(), setBigDecimal(), setNull() |
| Double | setDouble(), setFloat(), setNull() |
| Float | setFloat(), setNull() |
| Char | setString(), setNull() |
| Varchar | setString(), setNull() |
| Boolean | setBoolean(), setNull() |
| Time | setTime(), setNull() |
| TimeStamp | setTimestamp(), setNull() |
| Date | setDate(), setNull() |
| VarBinary | setNull(), setBytes() |

Was this page helpful?

* Prerequisites
* Supported Authentication Methods
* Download and Install
* Connect to Dremio
* Connection Parameters
  + Encryption Parameters
  + SOCKS Proxy Connection Parameters
  + Advanced Parameters
* Parameterized Queries with Prepared Statements
  + Supported Data Types and Set Methods

<div style="page-break-after: always;"></div>

# IBM Cognos Analytics | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/ibm-cognos-analytics

On this page

You can run SQL from [Cognos Analytics](https://www.ibm.com/products/cognos-analytics) to explore your data through Dremio. Cognos Analytics Dynamic Query supports connections to Dremio through the [legacy JDBC driver](/dremio-cloud/explore-analyze/client-apps/drivers/jdbc-legacy/).

## Supported Versions

To learn which versions of Dremio are supported with IBM Cognos 11.2.x, see [DQM testing of vendor-supported client driver versions for each Cognos Analytics 11.2.x release](https://www.ibm.com/support/pages/node/6441017#11.2.4fp2r).

To learn which versions of Dremio are supported with IBM Cognos 12.0.x, see [DQM testing of vendor-supported client driver versions for each Cognos Analytics 12.0.x release](https://www.ibm.com/support/pages/node/6989513#12.0.2r).

## Supported Authentication Methods

Use a Dremio [personal access token (PAT)](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat) for authentication.

## Create a Connection

1. Launch Cognos Analytics.
2. Navigate to **Manage** > **Data Server Connections**.
3. Click **Add Data Server** and select **Dremio** as the type of connection.
4. In the **JDBC URL** field, enter the connection string in the JDBC Connection field in the project settings' General Information sidebar in Dremio. The EU and US have different control planes, so the connection strings differ slightly depending on the control plane you're using.

   JDBC connection string example for US control plane

   ```
   jdbc:dremio:direct=sql.eu.dremio.cloud:443[;ssl=true;PROJECT_ID=<YOUR_PROJECT_ID>;ENGINE=<OPTIONAL_ENGINE_NAME>]
   ```

   JDBC connection string example for EU control plane

   ```
   jdbc:dremio:direct=sql.eu.dremio.cloud:443[;ssl=true;PROJECT_ID=<YOUR_PROJECT_ID>;ENGINE=<OPTIONAL_ENGINE_NAME>]
   ```
5. In the **Username** field, enter `$token`, and in the **Password** field, enter your Dremio PAT to authenticate to Dremio.
6. Click **Save**.
7. Click **Test** to confirm the connection.

Was this page helpful?

* Supported Versions
* Supported Authentication Methods
* Create a Connection

<div style="page-break-after: always;"></div>

# SAP Business Objects | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/sap-business-objects

On this page

You can use [SAP Business Objects](https://www.sap.com/products/technology-platform/bi-platform.html) to query and visualize data by means of Dremio.

## Supported Versions

SAP Business Objects 4.0+

## Prerequisite

Download, install, and configure the [Arrow Flight SQL ODBC driver](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/).

## Connect to Dremio

1. Open Information Design Tool.
2. Select **File** > **New** > **Project**.
3. Set the name of the project and click **Finish**.
4. Right-click the project and select **New** > **Relational Connection**.
5. Specify a name for the relational connection and click **Next**.
6. Select the Generic ODBC3 datasource driver and click **Next**.
7. Follow either of these steps:

   * Select **Use existing data source** and select the Arrow Flight SQL ODBC DSN.
   * Select Use connection string, select the Arrow Flight SQL ODBC driver, and specify this base connection string:

     Base connection string

     ```
     HOST=data.dremio.cloud;PORT=443;token=<personal-access-token>;  
     UseEncryption=true;DisableCertificateVerification=false;
     ```

   See [Connection Parameters](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/#connection-parameters) for additional connection parameters that are available.
8. (Optional) Test the connection.
9. Click **Finish**.

Dremio schemas and tables are now available.

Was this page helpful?

* Supported Versions
* Prerequisite
* Connect to Dremio

<div style="page-break-after: always;"></div>

# Driver Release Notes | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/release-notes/

On this page

This section contains the changes for the drivers that are supported for use with Dremio.

## Arrow Flight SQL Drivers

* [Arrow Flight SQL JDBC](/dremio-cloud/explore-analyze/client-apps/drivers/release-notes/arrow-flight-sql-jdbc/)
* [Arrow Flight SQL ODBC](/dremio-cloud/explore-analyze/client-apps/drivers/release-notes/arrow-flight-sql-odbc/)

## Other Drivers

* [Dremio JDBC Driver (Legacy)](/dremio-cloud/explore-analyze/client-apps/drivers/release-notes/jdbc-legacy)

note

The [Arrow Flight SQL JDBC driver](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc) is the recommended driver for connectivity to Java-based applications. The Dremio JDBC driver (Legacy) will not be updated or fixed moving forward.

Was this page helpful?

* Arrow Flight SQL Drivers
* Other Drivers

<div style="page-break-after: always;"></div>

# Microsoft Excel PowerPivot | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/microsoft-excel-powerpivot

On this page

## Prerequisites

* Ensure that your operating system is 64-bit Windows 10 or later.
* Download, install, and configure the [Arrow Flight SQL ODBC driver](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/).

## Update the DSN Configuration

1. Launch ODBC Data Sources on your Windows system.
2. Select the **User DSN** tab.
3. Select the DSN entry that you created when you configured the Arrow Flight SQL ODBC driver.
4. Click **Configure**.
5. In the **Advanced Properties** section, add the following key/value pair:  
   * **Key:** quoting
   * **Value:** BRACKET

## Connect to Dremio

1. Open Excel.
2. Click the **Power Pivot** tab and then click **Manage**.
3. Select **From Other Sources**.
4. In the Table Import Wizard, select **Others (OLEDB/ODBC)**.
5. Click **Next**.
6. Click **Build**.
7. In the Data Link Properties dialog, follow these steps:

   a. On the **Provider** tab, select **Microsoft OLE DB Provider for ODBC Drivers**.

   b. Click **Next>>**.

   c. For step 1 on the **Connection** tab, select **Use data source name**, and then select the data source name for the Arrow Flight SQL ODBC driver.

   d. For step 2 on the **Connection** tab, leave the **User name** and **Password** fields blank. The authentication credentials for connecting to Dremio Cloud are already present in the user DSN.

   e. (Optional) Click **Test Connection** to find out whether the info you specified on this tab is correct.

   f. Click **OK**.
8. Click **Next**.
9. Ensure that the option **Select from a list of tables and views to choose the data to import**.
10. Click **Next**.
11. Select the tables and views that you want to import data from.
12. Click **Finish**.

Was this page helpful?

* Prerequisites
* Update the DSN Configuration
* Connect to Dremio

<div style="page-break-after: always;"></div>

# Arrow Flight SQL JDBC | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc

On this page

The Arrow Flight SQL JDBC driver is an open-source driver that is based on the specifications for the Java Database Connectivity (JDBC) API. The Flight SQL JDBC driver uses Apache Arrow, so it is able to move large amounts of data faster, in part because it does not need to serialize and then deserialize data.

This driver is licensed under [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Prerequisites

You can use the Arrow Flight SQL JDBC 18.3.0 driver on systems that:

* Support Java versions: Java 11+
* Run the following 64-bit operating systems:
  + Linux: RedHat/CentOS
  + Windows 10 and later
  + macOS

## Supported Authentication Method

You can use personal access tokens for authenticating to Dremio. To generate one, see [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).

## Download and Install

1. Download the Driver: You can download the driver at [Arrow Flight SQL JDBC Driver](https://www.dremio.com/drivers/jdbc/).
2. Integrate the Driver: To integrate the driver into your development environment, you need to add the location of the driver to your classpath to inform the Java Virtual Machine (JVM) and the Java compiler where to locate the driver class files and resources during compilation and runtime.
3. For name the of the driver class, specify `org.apache.arrow.driver.jdbc.ArrowFlightJdbcDriver`.

## Connect to Dremio

Use this template to create a direct connection to Dremio Cloud:

Template for the JDBC URL

```
jdbc:arrow-flight-sql://data.dremio.cloud:443/?token=<encoded_pat>[&catalog=<project_id>][&schema=<schema>][&<properties>]
```

* `token`: The personal access token to use to authenticate to Dremio. See [Personal Access Tokens](/cloud/security/authentication/personal-access-token/) for information about enabling and creating PATs. You must URL-encode PATs that you include in JDBC URLs. See URL-encode Values for suggested steps.
* `catalog`: Specifies the project ID of a project in Dremio Cloud. You can use this to connect to non-default Dremio Cloud projects.
* `schema`: The name of the schema (data source or folder, including child paths, such as `mySource.folder1` and `folder1.folder2`) to use by default when a schema is not specified in a query.
* `<properties>`: A list of JDBC properties for encrypting connections and routing queries to particular engines. Values must be URL-encoded. See URL-encode Values for suggested steps.

To authenticate to Dremio Cloud, pass in a personal access token (PAT) with the `token` property. Use the PAT as the value. See [Personal Access Tokens](/cloud/security/authentication/personal-access-token/) for information about enabling the use of PATs in Dremio and about creating PATs. You must URL-encode PATs that you include in JDBC URLs. To encode a PAT locally on your system, you can follow the steps in URL-encode Values.

## Connection Parameters

### Encryption Parameters

If you are setting up encrypted communication between your JDBC client applications and the Dremio server, use the SSL JDBC connection parameters and fully qualified hostname to
configure the JDBC connection string and connect to Dremio.

note

This driver does not yet support these features:

* Disabling host verification
* Impersonation

| Properties | Value | Required | Description |
| --- | --- | --- | --- |
| `disableCertificateVerification` | `true` or `false` | [Optional] | If `true`, Dremio does not verify the host certificate against the truststore. The default value is `false`. |
| `trustStoreType` | string | [Optional] | Default: JKS The trustStore type. Allowed values are : `JKS`, `PKCS12`   If the useSystemTrustStore option is set to true (on Windows only), the allowed values are: `Windows-MY`, `Windows-ROOT`  Import the certificate into the **Trusted Root Certificate Authorities** and set `trustStoreType=Windows-ROOT`.  Also import the certificate into **Trusted Root Certificate Authorities** or **Personal** and set `trustStoreType=Windows-MY`. |
| `trustStore` | string | [Optional] | Path to the truststore.  If not provided, the default Java truststore is used (usually `$JAVA_HOME/lib/security/cacerts`) and the trustStorePassword parameter is ignored. |
| `useSystemTrustStore` | `true` or `false` | [Optional] | By default, the value is `true`. Bypasses trustStoreType and automatically picks the correct truststore based on the operating system: Keychain on MacOS, [Local Machine and Current User Certificate Stores](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores) on Windows, and default truststore on other operating systems. If you are using an operating system other than MacOS or Windows, you must use the `trustStorePassword` property to pass the password of the truststore. Here is an example of a connection string for Linux:  `jdbc:arrow-flight-sql://data.dremio.cloud:443/?useEncryption=true&token=1234&trustStorePassword=901234` |
| `trustStorePassword` | string | [Optional] | Password to the truststore. |

### Advanced Parameters

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| quoting | string | Specifies which type of character to use to delimit values in queries. The value can be `BACK_TICK`, `BRACKET`, or `DOUBLE_QUOTE`. | `DOUBLE_QUOTE` |
| routing\_tag | string | When this parameter is set, the specified tag is associated with all queries executed within a session. Rules can check for the presence of a tag with the function "tag()". For more information, see [Workload Management](/dremio-cloud/admin/engines/workload-management). | N/A |
| stringColumnLength | string | The maximum length of data in columns of the STRING datatype and of complex datatypes. The range is 1 to 2147483647. | 1024 |

### URL-encode Values

To encode a personal access token (PAT) or property value locally on your system, you can follow these steps:

1. In a browser window, right-click an empty area of the page and select **Inspect**.
2. Click **Console**.
3. Type `encodeURIComponent("<PAT-or-value>")`, where `<PAT-or-value>` is the personal access token that you obtained from Dremio or the value of a supported JDBC property. The URL-encoded PAT or value appears on the next line. You can highlight it and copy it to your clipboard.

## Parameterized Queries with Prepared Statements

Prepared statements allow you to dynamically pass parameters to SQL queries using placeholders, ensuring safer query execution by separating the query structure from the values in parameters.

With a prepared statement, parameters (`?`) can be set at runtime using set methods to reuse queries with different values.

note

This feature requires Apache Arrow 18.3.0 or later. It supports `SELECT` and `DML` statements.

To use parameterized queries with prepared statements, follow these steps:

1. Use the `prepareStatement()` method to define a query with parameters, which act as placeholders for dynamic values.
2. Set the values by replacing each parameter with a value using the appropriate set methods.
3. Ensure all parameters are set before running the query, with indexing starting at 1. If parameters are not set before running the query, JBDC throws an exception.
4. Call `executeQuery()` to run the `SELECT` query and retrieve results, or `executeUpdate()` to run the `DML` query and retrieve the count of modified records.

Java examples for SELECT and DML queries

```
PreparedStatement preparedStatement = connection.prepareStatement(  
  "SELECT * FROM employees WHERE department = ? AND salary > ?");  
preparedStatement.setString(1, "Engineering");  
preparedStatement.setDouble(2, 75000);  
ResultSet resultSet = preparedStatement.executeQuery();  
  
PreparedStatement preparedStatement = connection.prepareStatement(  
  "DELETE FROM employees WHERE department = ? AND salary > ?");  
preparedStatement.setString(1, "Engineering");  
preparedStatement.setDouble(2, 75000);  
int rowsUpdated = preparedStatement.executeUpdate();
```

### Supported Data Types and Set Methods

| **Column Data Type** | **Supported Set Methods** |
| --- | --- |
| Integer | `setInt()`, `setShort()`, `setNull()` |
| Numeric | `setInt()`, `setShort()`, `setLong()`, `setBigDecimal()`, `setNull()` |
| Decimal | `setShort()`, `setInt()`, `setLong()`, `setBigDecimal()`, `setNull()` |
| BigInt | `setShort()`, `setInt()`, `setLong()`, `setBigDecimal()`, `setNull()` |
| Double | `setDouble()`, `setFloat()`, `setNull()` |
| Float | `setFloat()`, `setNull()` |
| Char | `setString()`, `setNull()` |
| Varchar | `setString()`, `setNull()` |
| Boolean | `setBoolean()`, `setNull()` |
| Time | `setTime()`, `setNull()` |
| Timestamp | `setTimestamp()`, `setNull()` |
| Date | `setNull()` |
| VarBinary | `setBytes()`, `setNull()` |

### Limitations

The JDBC client does not support the `setDate()` method due to mismatched date encoding formats between the Arrow Flight JDBC client and Dremio.

## Differences between the Arrow Flight SQL JDBC and the Dremio JDBC (Legacy) Driver

The Arrow Flight SQL JDBC driver differs from the Dremio JDBC (Legacy) driver in the following:

* Requires Java 11+.
* Supports `ResultSet.getBoolean()` on `varchar` columns in which boolean values are represented as these strings: "0", "1", "true", "false".
* Supports `null` Calendar in calls to `ResultSet.getDate()`, `ResultSet.getTime()`, and `ResultSet.getTimestamp()`  
  When a call to one of these methods has no `Calendar` parameter, or the `Calendar` parameter is `null`, the Flight JDBC driver uses the default timezone when it constructs the returned object.
* Supports `ResultSet.getDate()`, `ResultSet.getTime()`, and `ResultSet.getTimestamp()` on `varchar` columns in which dates, times, or timestamps are represented as strings.
* Supports varchar values that represent numeric values in calls to `ResultSet.getInteger()`, `ResultSet.getFloat()`, `ResultSet.getDouble()`, `ResultSet.getShort()`, `ResultSet.getLong()`, and `ResultSet.getBigDecimal()`
* Supports integer values in calls to `getFloat()`  
  Integers returned gain one decimal place.
* Supports the native SQL complex types `List`, `Map`, and `Struct`  
  Dremio's legacy JDBC driver uses String representations of these types.
* Supports using the Interval data type in SQL functions.
* Removes support for calling `ResultSet.getBinaryStream()` on non-binary data types. Though such support exists in traditional JDBC drivers, it is not in the specification for the JDBC API.

note

Calling `DatabaseMetadata.getCatalog()` when connected to Dremio returns empty. Other `DatabaseMetadata` methods return null values in the `TABLE_CAT` column. This is expected behavior because Dremio does not have a catalog.

## Supported Conversions from Dremio Datatypes to JDBC Datatypes

| **DREMIO TYPE** | **JDBCARROW TYPE** |
| --- | --- |
| BIGINT | Int |
| BIT | Bool |
| DATE | Date |
| DECIMAL | Decimal |
| DOUBLE | FloatingPoint(DOUBLE) |
| FIXEDSIZEBINARY | FixedSizeBinary |
| FLOAT | FloatingPoint(SINGLE) |
| INT | Int |
| INTERVAL\_DAY\_SECONDS | Interval(DAY\_TIME) |
| INTERVAL\_YEAR\_MONTHS | Interval(YEAR\_MONTH) |
| LIST | List |
| MAP | Map |
| NULL | Null |
| OBJECT | Not Supported |
| STRUCT | Struct |
| TIME | Time(MILLISECOND) |
| TIMESTAMP | Timestamp(MILLISECOND) |
| VARBINARY | Binary |
| VARCHAR | Utf8 |

## Add the Root CA Certificate to Your System Truststore

1. At a command-line prompt, run this command:

   ```
   openssl s_client -showcerts -connect data.dremio.cloud:443 </dev/null
   ```
2. Copy the last certificate, including the lines `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`, to your clipboard.
3. Create a text file and paste the certificate into it.
4. Save the text file as `cert.pem`.
5. If you are using MacOS, follow these steps:

   a. In Finder, double-click the `cert.pem` file.

   b. In the dialog that opens, select the option to add the root certificate to the system truststore.
6. If you are using Windows, follow these steps:

   a. At a command-line prompt, enter one of these commands:

   * `certlm` if you want to add the certificate for all user accounts on your Windows system.
   * `certmgr` if you want to add the certificate only for the current user account.

   b. Right-click the folder **Trusted Root Certification Authorities**.

   c. Select **Import**.

   d. Browse for the `cert.pem` file and import it.
7. If you are using a version of Linux, follow the instructions for your version.
8. If you are developing your own client application to use the driver to connect to Dremio, add the certificate to the Java truststore. You must know the path to the `cacerts` file from `$JAVA_HOME`.

   * If you are using Java 11, run this command:

     ```
     keytool -import -trustcacerts -file cert.pem -alias gtsrootr1ca -keystore $JAVA_HOME/lib/security/cacerts
     ```

## Limitations

* Impersonation is not supported.
* Disabling host verification is not supported.

Was this page helpful?

* Prerequisites
* Supported Authentication Method
* Download and Install
* Connect to Dremio
* Connection Parameters
  + Encryption Parameters
  + Advanced Parameters
  + URL-encode Values
* Parameterized Queries with Prepared Statements
  + Supported Data Types and Set Methods
  + Limitations
* Differences between the Arrow Flight SQL JDBC and the Dremio JDBC (Legacy) Driver
* Supported Conversions from Dremio Datatypes to JDBC Datatypes
* Add the Root CA Certificate to Your System Truststore
* Limitations

<div style="page-break-after: always;"></div>

# Arrow Flight SQL ODBC | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc

On this page

You can use the Arrow Flight SQL ODBC 0.9.7 driver to connect to Dremio from ODBC client applications.

This driver is licensed under [GNU Library General Public License, Version 2](https://github.com/dremio/warpdrive/blob/master/license.txt).

## Prerequisites

You can use the Arrow Flight SQL ODBC 0.9.7 driver on systems that:

* Run the following 64-bit operating systems:
  + Linux: RedHat/CentOS
  + Windows 10 and later
  + macOS

## Supported Authentication Method

You can use personal access tokens for authenticating to Dremio. To generate one, see [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).

## Windows

### Download and Install

To download and install the Arrow Flight SQL ODBC driver:

1. Download the Windows 64-bit version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Run the installer.
3. (Optional) In the **User Account Control** page, click **Yes**. This page appears only if there is user account control configured on your Windows machine.
4. In the **Welcome to Dremio** page, click **Next**.
5. Click **Install**.
6. In the **Installation Complete** page, click **Next**.
7. In the **Completing Arrow Flight SQL ODBC Driver Setup Wizard** page, click **Finish**.

### Connect to Dremio

caution

Do not follow these steps if you are using Microsoft Power BI Desktop to connect to Dremio. For the steps for configuring Power BI, see [Connecting from Microsoft Power BI](/dremio-cloud/explore-analyze/client-apps/microsoft-power-bi/).

note

Before following these steps, generate a personal access token in Dremio. See [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).

To configure a user DSN:

1. Go to **Start Menu** > **Window Administrative Tools**. Click **ODBC Data Sources (64-bit)**.
2. In the **ODBC Data Source Administrator (64-bit)** dialog, click **System DSN**.
3. Select **Arrow Flight SQL ODBC DSN** and click **Configure**.
4. (Optional) Change the data source name.
5. In the **Host name** field, `data.dremio.cloud` for the US control plane, or `data.eu.dremio.cloud` for the European control plane.
6. In the **Port** field, specify `443`.
7. In the **Authentication Type** field, select **Token Authentication**.
8. In the **Authentication Token** field, paste a personal access token.
9. Click the **Advanced** tab.
10. Ensure that the **Use Encryption** option is selected.

For additional parameters, see [Connection Parameters](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/#connection-parameters).

If you ever need to enable tracing for troubleshooting problems with the driver, click the **Tracing** tab in the **ODBC Data Source Administrator (64-bit)** dialog, set the log-file path, and then click **Start Tracing Now**.

## Linux

### Download and Install

To download and install the Arrow Flight SQL ODBC driver:

1. Download the Linux version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Run the following command to install the driver and automatically create the data source name (DSN) `Arrow Flight SQL ODBC DSN`:

Install Dremio ODBC driver

```
sudo yum localinstall <dremio-odbc-rpm-path>
```

### Connect to Dremio

note

* Before configuring, ensure that unixODBC is installed.
* In Dremio, generate a personal access token. See [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).
* If you want to base your configuration on examples, copy the content of the `odbc.ini` and `odbcinst.ini` files in the `/opt/arrow-flight-sql/odbc-driver/conf` directory and paste the content into your system `/etc/odbc.ini` and `/etc/odbcinst.ini` files.

To configure the properties in the odbc.ini file:

1. For `HOST`, specify `data.dremio.cloud` for the US control plane, or `data.eu.dremio.cloud` for the European control plane.
2. For `PORT`, specify `443`.
3. For `TOKEN`, specify a personal access token.
4. Ensure that the value of `SSL` is `1`.

For additional parameters, see [Connection Parameters](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/#connection-parameters).

note

To find out unixODBC has created your `odbc.ini` and `odbcinst.ini` files, run this command: `odbcinst -j`

If you ever need to enable tracing for troubleshooting problems with the driver, see the help for unixODBC.

## macOS

### Download and Install

To download and install the Arrow Flight SQL ODBC driver:

Intel Macs Only

This driver only supports Intel-based Macs. It is not compatible with Apple Silicon M1, M2, and M3 processors.

1. Download the macOS driver version from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Go to the download location and double-click the downloaded `.dmg` file.
3. Double-click the `.pkg` file.
4. In the **Welcome to the Arrow Flight SQL ODBC Driver Installer** page, click **Continue**.
5. In the **Standard Install on "Macintosh HD"** page, Click **Install**. Optionally, if you want to change the install location, click **Change Install Location** and navigate to the new location.
6. In the **Installer is trying to install new software** dialog, specify your macOS password. Then, click **Install Software**.
7. After the installation is complete, click **Close**.

### Connect to Dremio

note

Before configuring, follow these steps:

* Ensure that [ODBC Manager](http://www.odbcmanager.net/) is installed.
* In Dremio, generate a personal access token. See [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).

To configure a system DSN:

1. Launch ODBC Manager.
2. On the User DSN page, select **Arrow Flight SQL ODBC DSN** and click **Configure**.
3. (Optional) Change the DSN.
4. In the **Host** field, specify `data.dremio.cloud` for the US control plane, or `data.eu.dremio.cloud` for the European control plane.
5. In the **Port** field, specify `443`.
6. Select the **UID** field and click **Remove**.
7. Select the **PWD** field and click **Remove**.
8. In the **UseEncryption** field, specify `true`.
9. Click **Add** to add a line for a new parameter. Change `keyword` to `TOKEN`, Paste a personal access token as the value.

For additional parameters, see [Connection Parameters](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/#connection-parameters).

If you ever need to enable tracing for troubleshooting problems with the driver, see the help for your driver manager.

## Connection Parameters

### Primary Connection Parameters

Use these parameters to configure basic connection details such as what data source to connect with.

note

The Arrow Flight SQL ODBC driver does not support password-protected `.pem`/`.crt` files or multiple `.crt` certificates in a single `.pem`/`.crt` file.

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Host | string | `data.dremio.cloud` for the US control plane, `data.eu.dremio.cloud` for the European control plane. | None |
| Port | integer | Sets the TCP port number that Dremio uses to listen to connections from ODBC clients. | 443 |
| Schema | string | Provides the name of the database schema to use by default when a schema is not specified in a query. However, this does not prevent queries from being issued for other schemas. Such queries must explicitly include the schema. | None |
| Token | string | Sets the personal access token to use when authenticating to Dremio. See [Creating a Token](/cloud/security/authentication/personal-access-token/#creating-a-token) for the steps to generate a personal access token. | None |

### Encryption Parameters

Use the following parameters to configure SSL encryption and verification methods for regular connections.

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| useEncryption | integer | Forces the client to use an SSL-encrypted connection to communicate with Dremio. Accepted values include:   `true`: The client communicates with Dremio only using SSL encryption. This is the only possible value.   `false`: The value cannot be false. | true |
| disableCertificateVerification | integer | Specifies whether the driver should verify the host certificate against the trust store. Accepted values are:   `false`: The driver verifies the certificate against the trust store.   `true`: The driver does not verify the certificate against the trust store. | false |
| useSystemTrustStore | integer | Controls whether to use a CA certificate from the system's trust store, or from a specified .pem file.   `true`: The driver verifies the connection using a certificate in the system trust store.   `false`: The driver verifies the connection using the .pem file specified by the trustedCerts parameter. | true on Windows and macOS, false on Linux (which does not have a system truststore) |
| trustedCerts | string | The full path of the .pem file containing certificates trusted by a CA, for the purpose of verifying the server. If this option is not set, then the driver defaults to using the trusted CA certificates .pem file installed by the driver.   The exact file path varies according to the operating system on which the driver is installed. The path for the Windows driver is different from the path set for the macOS driver.   The TLS connection fails if you do not specify a value when useEncryption is true and disableCertificateVerification is false. | N/A |

### Advanced Parameters

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| quoting | string | Specifies which type of character to use to delimit values in queries. The value can be `BACK_TICK`, `BRACKET`, or `DOUBLE_QUOTE`. | `DOUBLE_QUOTE` |
| routing\_tag | string | When this parameter is set, the specified tag is associated with all queries executed within a session. Rules can check for the presence of a tag with the function "tag()". For more information, see [Workload Management](/dremio-cloud/admin/engines/workload-management). | N/A |
| stringColumnLength | string | The maximum length of data in columns of the STRING datatype and of complex datatypes. The range is 1 to 2147483647. | 1024 |

### Example of a Basic Connection String

Some BI client applications, such as Microsoft Excel, let you specify a connection string, rather than select a DSN, for connecting to Dremio. If you want to connect by using a connection string, you can use this example, basic connection string as a basis for your own:

Example connection string

```
host=data.dremio.cloud;port=443;useEncryption=1;disableCertificateVerification=1;token=<personal-access-token>
```

## Supported Conversions from Dremio Datatypes to ODBC Datatypes

| Dremio Data Types | SQL\_C\_BINARY | SQL\_C\_BIT | SQL\_C\_CHAR | SQL\_C\_WCHAR | SQL\_C\_STINYINT | SQL\_C\_UTINYINT | SQL\_C\_SSHORT | SQL\_C\_USHORT | SQL\_C\_SLONG | SQL\_C\_ULONG | SQL\_C\_SBIGINT | SQL\_C\_UBIGINT | SQL\_C\_FLOAT | SQL\_C\_DOUBLE | SQL\_C\_NUMERIC | SQL\_C\_DATE | SQL\_C\_TIME | SQL\_C\_TIMESTAMP | SQL\_C\_GUID | SQL\_C\_INTERVAL\_\* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BOOLEAN | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Invalid | Invalid | Invalid | Invalid | N |
| VARBINARY | Y | Invalid | N | N | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid |
| DATE | N | Invalid | Y | Y | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Y | Invalid | Y | Invalid | Invalid |
| FLOAT | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Invalid | Invalid | Invalid | Invalid | N |
| DECIMAL | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Invalid | Invalid | Invalid | Invalid | N |
| DOUBLE | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Invalid | Invalid | Invalid | Invalid | N |
| INTERVAL (day to seconds) | N | N | N | N | N | N | N | N | N | N | N | N | N | N | N | N | Invalid | Invalid | Invalid | N |
| INTERVAL (years to months) | N | N | N | N | N | N | N | N | N | N | N | N | N | N | N | N | Invalid | Invalid | Invalid | N |
| INT | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Invalid | Invalid | Invalid | Invalid | N |
| BIGINT | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Invalid | Invalid | Invalid | Invalid | N |
| TIME | N | N | Y | Y | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Y | Y | Invalid | Invalid |
| TIMESTAMP | N | N | Y | Y | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Y | Y | Invalid | Invalid |
| VARCHAR | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Invalid |
| STRUCT | N | N | Y | Y | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid |
| LIST | N | Invalid | Y | Y | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid | Invalid |

Was this page helpful?

* Prerequisites
* Supported Authentication Method
* Windows
  + Download and Install
  + Connect to Dremio
* Linux
  + Download and Install
  + Connect to Dremio
* macOS
  + Download and Install
  + Connect to Dremio
* Connection Parameters
  + Primary Connection Parameters
  + Encryption Parameters
  + Advanced Parameters
  + Example of a Basic Connection String
* Supported Conversions from Dremio Datatypes to ODBC Datatypes

<div style="page-break-after: always;"></div>

# Dremio JDBC (Legacy) Release Notes | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/release-notes/jdbc-legacy

On this page

This article contains the release notes for the Dremio JDBC driver (Legacy). See [Dremio JDBC Driver (Legacy)](/dremio-cloud/explore-analyze/client-apps/drivers/jdbc-legacy) for documentation.

note

The [Arrow Flight SQL JDBC driver](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc) is the recommended driver for connectivity to Java-based applications. The Dremio JDBC driver (Legacy) will not be updated or fixed moving forward.

## Legacy JDBC Driver 17.0.0 (June 2021)

***Connection.getCatalog() would always return `null`.***  
Connection.getCatalog() now returns the current catalog for the connection.

## Legacy JDBC Driver 15.2.0 (March 2021)

* Dremio uses the local timezone rather than UTC for datetime values.

## Legacy JDBC Driver 15.0.0 (March 2021)

* Provides a `useSystemTrustStore` property that bypasses `trustStoreType` and automatically selects the correct Truststore based on the operating system. See [JDBC Parameters for Dremio Wire Encryption](/dremio-cloud/explore-analyze/client-apps/drivers/jdbc-legacy/#encryption-parameters) for more information.

* Dremio no longer maps empty usernames to anonymous. Rather, Dremio treats empty usernames as empty.

## Legacy JDBC Driver 14.0.0 (February 2021)

* Provides a new class loader from a previously-loaded class when no class loader is available for a thread.

## Legacy JDBC Driver 11.0.0 (November 2020)

* Support for TLS SNI when connecting to a TLS-enabled Dremio deployment. Dremio implicitly sets the TLS SNI property to the hostname used in the connection string.

Was this page helpful?

* Legacy JDBC Driver 17.0.0 (June 2021)
* Legacy JDBC Driver 15.2.0 (March 2021)
* Legacy JDBC Driver 15.0.0 (March 2021)
* Legacy JDBC Driver 14.0.0 (February 2021)
* Legacy JDBC Driver 11.0.0 (November 2020)

<div style="page-break-after: always;"></div>

# Arrow Flight SQL JDBC Release Notes | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/release-notes/arrow-flight-sql-jdbc

On this page

You can connect to Dremio through the Arrow Flight SQL JDBC driver. The driver is open-source and you are free to use it with Dremio's data lakehouse platform or any other data platform that has an Arrow Flight SQL endpoint.
These release notes summarize Dremio-specific updates, compatibility notes, and limitations.

For more information about this driver, see [Arrow Flight SQL JDBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc).

## Version 10.0.0 (November 2022)

### Security

Transport Layer Security (TLS) communication is enabled by default for Arrow Flight client applications.

### Limitations

* Time offsets are not being reported in query results.
* User impersonation is not yet supported.

### Recommendation

It is recommended to use the Arrow Flight SQL JDBC driver instead of the Dremio JDBC (Legacy) driver. The Dremio JDBC (Legacy) driver will not be updated or fixed moving forward.

Was this page helpful?

* Version 10.0.0 (November 2022)
  + Security
  + Limitations
  + Recommendation

<div style="page-break-after: always;"></div>

# Arrow Flight SQL ODBC Release Notes | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/explore-analyze/client-apps/drivers/release-notes/arrow-flight-sql-odbc

On this page

This article contains the release notes for the Arrow Flight SQL ODBC driver.

See [Arrow Flight SQL ODBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc/) for documentation.

## 0.9.7 (August 2025)

Issues Fixed

General Updates

Fixed an issue on macOS where the error was sometimes not displayed in Microsoft Excel.

DX-90575

General Updates

Fixed an issue with an inconsistent searchable attribute returned by the `SQLColAttribute` function.

DX-102851

General Updates

Fixed an issue where Microsoft Excel was not showing small decimals correctly.

DX-104574

## 0.9.6 (June 2025)

Issues Fixed

General Updates

Resolved an issue where the Arrow Flight SQL ODBC driver failed to connect to TLS-secured Flight endpoints.

General Updates

Fixed an issue where calling metadata functions like `SQLPrimaryKeysW` or `SQLForeignKeysW` caused an error.
The driver now handles these calls more gracefully.

## 0.9.5 (May 2025)

What's New

General Updates

A new driver configuration flag is available for macOS (Intel and Apple Silicon): `hideSQLTablesListing`.

DX-101630

## 0.9.4 (April 2025)

What's New

General Updates

The Arrow Flight SQL ODBC driver now supports Apple Silicon. [Download the driver](https://download.dremio.com/arrow-flight-sql-odbc-driver/arrow-flight-sql-odbc-LATEST-armv8.dmg).

General Updates

Upgraded to Arrow Flight [v9](https://arrow.apache.org/docs/9.0/format/FlightSql.html) for enhanced compatibility and performance.

Issues Fixed

General Updates

Fixed date handling for pre-1970 dates in Microsoft tools.

General Updates

Fixed segmentation fault in Arrow Flight SQL ODBC Driver.

Was this page helpful?

* 0.9.7 (August 2025)
* 0.9.6 (June 2025)
* 0.9.5 (May 2025)
* 0.9.4 (April 2025)

<div style="page-break-after: always;"></div>

