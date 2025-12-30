# Dremio Software - Get Started



---

# Source: https://docs.dremio.com/current/get-started/

Version: current [26.x]

On this page

# Get Started with Dremio

Welcome to Dremio, a data lakehouse platform that facilitates high-performance, self-service analytics on large datasets.

To get started with Dremio, you have two options for a hands-on experience:

* [Enterprise Edition Free Trial](/current/get-started/kubernetes-trial) (Recommended) - Deploy and explore Dremio on Kubernetes using the Enterprise Edition free trial with all features unlocked.
* [Community Edition on Docker](/current/get-started/docker) - Deploy and explore Dremio on Docker using the Community Edition with a limited set of features. This option provides a local deployment with a single node, which is suggested for testing and evaluation purposes.

Choose the option that best fits your needs.
To learn about the differences between the two editions, see [Dremio Editions](/editions).

## Related Topics

If you want to learn more about Dremio, see the following:

* [Quick Tour of the Console](/current/get-started/quick_tour/) - A walkthrough of the Dremio console and how to best use its various capabilities.
* [What is Dremio?](/current/what-is-dremio/) - An overview of Dremio, its key concepts, and architecture.

Was this page helpful?

[Previous

Overview](/current/)[Next

Enterprise Edition Free Trial](/current/get-started/kubernetes-trial)

* Related Topics

---

# Source: https://docs.dremio.com/current/get-started/kubernetes-trial

Version: current [26.x]

On this page

# Get Started with the Enterprise Edition Free Trial

This Get Started guide walks you through deploying Dremio on Kubernetes using a free trial of the Enterprise Edition, exploring the multiple features available in this edition. For more information, see [How Does the Enterprise Edition Free Trial Work](/current/admin/licensing/free-trial#how-does-the-enterprise-edition-free-trial-work).

## Prerequisites

Before deploying Dremio on Kubernetes, ensure you have the following:

* A hosted Kubernetes environment to deploy and manage the Dremio cluster.  
  Each Dremio release is tested against [Amazon Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/what-is-aks), and [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine?hl=en#how-it-works) to ensure compatibility. If you have a containerization platform built on top of Kubernetes that is not listed here, please contact your provider and the Dremio Account Team regarding compatibility.
* Helm 3 installed on your local machine to run Helm commands. For installation instructions, refer to [Installing Helm](https://helm.sh/docs/intro/install/) in the Helm documentation.
* A local kubectl configured to access your Kubernetes cluster. For installation instructions, refer to [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) in the Kubernetes documentation.
* Object Storage: Amazon S3 (including S3-compatible, e.g., MinIO), Azure Storage, or Google Cloud Storage (GCS).

## Step 1: Deploy Dremio

Let's start by deploying the Enterprise Edition on your hosted Kubernetes environment:

1. If you haven't already, [sign up for the Enterprise Edition Free Trial](https://www.dremio.com/get-started/?utm_source=dremio-docs&utm_medium=referral).
2. In the email you receive from Dremio, click a link to download the `values-overrides.yaml` file containing the deployment information and save the file locally.
3. Open the `values-overrides.yaml` file in an editor to make the following configurations:

   1. For distributed storage, follow the instructions in [Configuring the Distributed Storage](/current/deploy-dremio/configuring-kubernetes/#configuring-the-distributed-storage), and then return here.
   2. For object storage, follow the instructions in [Configuring Storage for Dremio Catalog](/current/deploy-dremio/configuring-kubernetes/#configuring-storage-for-dremio-catalog), and then return here.
   3. (Optional) For the coordinator, you can adjust its default values by following the instructions in [Recommended Resources Configuration](/current/deploy-dremio/configuring-kubernetes/#recommended-resources-configuration), and then return here.
   4. Save the `values-overrides.yaml` file.
4. Open a terminal window, and start the deployment by installing Dremio's Helm chart with the following command:

   Run helm install

   ```
   helm install <your-dremio-install-release> \  
     oci://quay.io/dremio/dremio-helm \  
     -f <your-local-path>/values-overrides.yaml
   ```

   Where:

   * `<your-dremio-install-release>` - The name that identifies your Dremio installation. For example, `dremio-1-0`.
   * `<your-local-path>` - The path to reach the `values-overrides.yaml` file.
5. Monitor the deployment using the following command:

   Run kubectl to monitor pods

   ```
   kubectl get pods
   ```

The deployment is complete when all pods are in the `Ready` state.

Now, access the Dremio console to interact with the platform in a user-friendly and visual way. It is a key component of the Dremio experience and is accessible through a web browser:

1. Run the following command in Kubernetes to find the host for the Dremio console:

   Run kubectl to find the Dremio console

   ```
   kubectl get services dremio-client
   ```
2. Depending on the value in the `TYPE` column of the output, open the Dremio console in your browser with one of the following URLs:

   * https://EXTERNAL\_IP:9047 - If the value in the `TYPE` column is `LoadBalancer`, use the value from the `EXTERNAL_IP` column of the output in the URL. For example, `https://8.8.8.8:9047`.
   * <http://localhost:32390> - If the value in the `TYPE` column is `NodePort`.
3. Follow the instructions, and enter your details.

You should have the Dremio console ready in your browser.

![Dremio console landing page.](/images/get-started/free-trial-dremio-console-land.png "Dremio console landing page.")

To learn how to navigate the Dremio console, see [Quick Tour of the Dremio Console](/current/get-started/quick_tour).

## Step 2: Create an Engine

Engines are responsible for query execution. Each engine comprises one or more executors that perform queries and Data Manipulation Language (DML) operations by running the query execution plan and transiting data between themselves to serve queries.

To create an engine, do the following:

1. Click ![This is the icon that represents the Organization settings.](/images/icons/settings.png "Icon represents the Organization settings.") in the side navigation bar to go to the Settings page.
2. Select **Engines** from the settings sidebar, and then click **Add Engine** on the far right.
3. In the New Engine dialog, enter a name for your engine. For example, `my-engine`.
4. Click **Add**.

You will see a new line with your engine with the **Status** as `Starting`.  
Wait until the **Status** changes to `Running` for the engine to be available to serve your queries.

note

The engine you created is configured to automatically stop/start. This means that Dremio automatically stops the engine after 15 minutes of idle time to save resources. When a new query is issued, Dremio automatically starts the engine, but your query may take a bit longer to execute while the engine starts.

If you want to have the engine always running, edit the engine and uncheck the **Automatically start/stop** option.

## Step 3: Add the Sample Data

Let's add the sample datasets that will be used in this Get Started guide, namely:

* **NYC taxi trip data** – In Iceberg format, with more than 338 million records.
* **NYC weather data** – In CSV format, with more than 4 thousand records.

### Add the Datasets

Add the datasets from a sample data source, as follows:

1. In the Dremio console, click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon.") in the side navigation bar to go to the Datasets page.
2. Click ![This is the Add Source icon.](/images/icons/plus.png "The Add Source icon.") right next to **Sources**.
3. In the Add Source dialog, select `Sample Source` in the **Object Storage** section.

### Format the Datasets

Now that the data source has been added, let's format the needed datasets as tables so that we can query them:

1. Under **Object Storage**, click the newly added `Samples` source, and then `samples.dremio.com` to see its details.
2. Hover over the `NYC-taxi-trips-iceberg` folder, and click ![This is the icon that represents the format folder action.](/images/cloud/format-data.png "Format folder.") on the far right.
3. In the Folder Settings dialog, check the **Format**, verify that `Iceberg` is detected, and click **Save**.
4. Click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon.") in the side navigation bar, click the `Samples` source, and then `samples.dremio.com` to see its details.
5. Hover over the `NYC-weather.csv` file, and click ![This is the icon that represents the format file action.](/images/icons/format-file.png "Format file") on the far right.
6. In the Table Settings dialog, do the following:
   1. For **Line Delimiter**, select `LF - Unix/Linux`.
   2. Under **Options**, check **Extract Column Names**.
   3. Click **Save**.

The sample data is now added, formatted, and ready to be queried.  
You can validate it by clicking ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon.") in the side navigation bar, then the `Samples` source, and then `samples.dremio.com` to see its details:

* The icon for `NYC-taxi-trips-iceberg` is ![This is the icon that represents a formatted folder on the Datasets page.](/images/tableIcon-folder.png "The formatted folder icon."), which means the folder is formatted as a table.
* The icon for `NYC-weather.csv` is ![This is the icon that represents the a formatted file on the Datasets page.](/images/tableicon-file.png "The formatted file icon."), which means the file is formatted as a table.

## Step 4: Create a Data Product

In this step, you will start creating a data product to explore the relationship between weather conditions and tipping behavior in taxi rides to answer the business question: "Do people tip more during taxi rides when it's raining?".

### Run the Query for the Data Product

To answer the business question, you will need the average tip amount per precipitation level. For that, combine the data in the `NYC-taxi-trips-iceberg` and `NYC-weather.csv` datasets on a common field: the date.

To do this, run the SQL query that joins the two datasets, and calculates the average tip amount per precipitation level:

1. Click ![This is the icon that represents the SQL runner.](/images/cloud/sql-runner-icon.png "Icon represents the SQL runner.") in the side navigation bar to go to the [SQL Runner](/current/get-started/quick_tour/#sql-runner).
2. Copy the SQL below, paste it in the SQL Runner, and click **Run**.

   SQL to join datasets

   ```
   SELECT AVG(tip_amount) as avg_tip_amount, prcp  
   FROM   Samples."samples.dremio.com"."NYC-weather.csv"  
   JOIN   Samples."samples.dremio.com"."NYC-taxi-trips-iceberg"  
   ON     (TO_CHAR(CAST(pickup_datetime AS DATE), 'YYYY-MM-DD')) = SUBSTRING(CAST("date" AS CHAR) FROM 0 FOR 10)  
   GROUP BY prcp;
   ```

You will get the query results, as shown in the image below.

![The result of the query to join the datasets with the average tip amount per precipitation level.](/images/get-started/free-trial-run-query.png "The result of the query with the average the tip amount per precipitation level.")

### Create the View for the Data Product

In Dremio, views are virtual tables based on the result set of a query. You can create views from data that resides in any data source, folder, table, or view that you have access to. You can also share views you've created with stakeholders in your organization.

Let's create a view for the data product from the query that you ran above:

1. Click **Save as View** on the far right to create a view of your query that others can access.
2. In the Save View As dialog, enter a name for your view. For example, `avg_tips_precipitation`.
3. Click **Save**.

You can see the [lineage](/current/data-products/govern/lineage) of your datasets in a graph showing all the relationships with end-to-end visibility into how data is sourced and transformed, which helps you understand the data flow and dependencies between datasets.  
For your newly created view, see the lineage by selecting the **Lineage** tab at the top of the page:

![The lineage graph for the view showing how datasets are connected.](/images/get-started/free-trial-lineage.png "The lineage graph for the view.")

## Step 5: Accelerate the Query with Reflections

In this step, you will use [Reflections](/current/acceleration) to accelerate queries, particularly when working with large datasets.

### Enable the Reflection

Let's enable a [Raw Reflection](/current/acceleration/#types) to accelerate the query of your view:

1. Select the **Reflections** tab at the top of the page, toggle the **Raw Reflections** switch to on, and click **Save**.
2. On the far right, you will see an animated spinner icon close to **Footprint**. Wait until it turns into a green checkmark, which means that your query has been accelerated.

### Run the Accelerated Query

Let's now query the view and see the acceleration in action:

1. Click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon."), click `avg_tips_precipitation`, and click **Run** to execute the query.
2. Check the execution time. It's **a sub-second query**!

   ![The query with a highlight in the execution time after the acceleration.](/images/get-started/free-trial-reflections-after.png "The query execution time after the acceleration.")
3. Now, go to the Jobs tab, and confirm that the query was accelerated with a Reflection.

   ![The details of a query showing it was accelerated with a Reflection.](/images/get-started/free-trial-reflections-details.png "The details of a query showing the acceleration with a Reflection.")

You’ve just created a Raw Reflection and accelerated your query!

While creating a Reflection manually is a great way to understand how Dremio boosts performance, you don’t need to manage this complexity yourself in real-world environments if you use [Autonomous Reflections](/current/acceleration/autonomous-reflections) — available exclusively in the Enterprise Edition. Dremio will automatically create, select, and maintain the most efficient Reflections for you, saving time while ensuring consistently fast performance of your queries.

And that's it! You finished the Get Started guide for the Enterprise Edition free trial.

Explore the documentation to learn more about Dremio, start using your data, build your data products, connect your client applications, and much more.

Was this page helpful?

[Previous

Get Started with Dremio](/current/get-started/)[Next

Community Edition on Docker](/current/get-started/docker)

* Prerequisites
* Step 1: Deploy Dremio
* Step 2: Create an Engine
* Step 3: Add the Sample Data
  + Add the Datasets
  + Format the Datasets
* Step 4: Create a Data Product
  + Run the Query for the Data Product
  + Create the View for the Data Product
* Step 5: Accelerate the Query with Reflections
  + Enable the Reflection
  + Run the Accelerated Query

---

# Source: https://docs.dremio.com/current/get-started/docker

Version: current [26.x]

On this page

# Get Started with the Community Edition on Docker

This Docker-based Get Started guide offers a simple and fast way to spin up Dremio locally with the Community Edition and explore the capabilities available in this edition.

This Docker deployment is indicated for testing and evaluation purposes and is not recommended for production usage. To try out a complete version of Dremio with enterprise-grade features, go to [Get Started with the Enterprise Edition Free Trial](/current/get-started/kubernetes-trial).

## Prerequisites

Before you start, download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

## Step 1: Deploy Dremio

Let's deploy the Dremio Community Edition on Docker:

1. Open your Docker Desktop.
2. Click **>\_Terminal** on the bottom-right of the screen, and run the following command:

   Run Docker command

   ```
   docker run \  
       -p 9047:9047 -p 31010:31010 -p 45678:45678 -p 32010:32010 \  
       -e DREMIO_JAVA_SERVER_EXTRA_OPTS=-Dpaths.dist=file:///opt/dremio/data/dist \  
       dremio/dremio-oss
   ```

After a couple of minutes, the containers should be up and running, and Dremio is deployed.

Now, access the Dremio console, where you interact with the platform in a user-friendly and visual way. It is a key component of the Dremio experience and is accessible through a web browser:

1. In your browser, navigate to <http://localhost:9047>.
2. You will be asked to enter your details and click **Next**.

You should have the Dremio console ready in your browser.

![Dremio console landing page.](/images/get-started/docker-dremio-console-land.png "Dremio console landing page.")

To learn how to navigate the Dremio console, see [Quick Tour of the Dremio Console](/current/get-started/quick_tour).

## Step 2: Add the Sample Data

Let's add the sample datasets that will be used in this Get Started guide, namely:

* **NYC taxi trip data** – In Iceberg format, with more than 338 million records.
* **NYC weather data** – In CSV format, with more than 4 thousand records.

### Add the Datasets

Add the datasets from a sample data source, as follows:

1. In the Dremio console, click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon.") in the side navigation bar to go to the Datasets page.
2. Click ![This is the Add Source icon.](/images/icons/plus.png "The Add Source icon.") right next to **Sources**.
3. In the Add Source dialog, select `Sample Source` in the **Object Storage** section.

### Format the Datasets

Now that the data source has been added, let's format the needed datasets as tables so that we can query them:

1. Under **Object Storage**, click the newly added `Samples` source, and then `samples.dremio.com` to see its details.
2. Hover over the `NYC-taxi-trips-iceberg` folder, and click ![This is the icon that represents the format folder action.](/images/cloud/format-data.png "Format folder.") on the far right.
3. In the Folder Settings dialog, check the **Format**, verify that `Iceberg` is detected, and click **Save**.
4. Click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon.") in the side navigation bar, click the `Samples` source, and then `samples.dremio.com` to see its details.
5. Hover over the `NYC-weather.csv` file, and click ![This is the icon that represents the format file action.](/images/icons/format-file.png "Format file") on the far right.
6. In the Table Settings dialog, do the following:
   1. For **Line Delimiter**, select `LF - Unix/Linux`.
   2. Under **Options**, check **Extract Column Names**.
   3. Click **Save**.

The sample data is now added, formatted, and ready to be queried.  
You can validate it by clicking ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon.") in the side navigation bar, then the `Samples` source, and then `samples.dremio.com` to see its details:

* The icon for `NYC-taxi-trips-iceberg` is ![This is the icon that represents a formatted folder on the Datasets page.](/images/tableIcon-folder.png "The formatted folder icon."), which means the folder is formatted as a table.
* The icon for `NYC-weather.csv` is ![This is the icon that represents the a formatted file on the Datasets page.](/images/tableicon-file.png "The formatted file icon."), which means the file is formatted as a table.

## Step 3: Create a Data Product

In this step, you will start creating a data product to explore the relationship between weather conditions and tipping behavior in taxi rides to answer the business question: "Do people tip more during taxi rides when it's raining?".

### Run the Query for the Data Product

To answer the business question, you will need the average tip amount per precipitation level. For that, combine the data in the `NYC-taxi-trips-iceberg` and `NYC-weather.csv` datasets on a common field: the date.

To do this, run the SQL query that joins the two datasets, and calculates the average tip amount per precipitation level:

1. Click ![This is the icon that represents the SQL runner.](/images/cloud/sql-runner-icon.png "Icon represents the SQL runner.") in the side navigation bar to go to the [SQL Runner](/current/get-started/quick_tour/#sql-runner).
2. Copy the SQL below, paste it in the SQL Runner, and click **Run**.

   SQL to join datasets

   ```
   SELECT AVG(tip_amount) as avg_tip_amount, prcp  
   FROM   Samples."samples.dremio.com"."NYC-weather.csv"  
   JOIN   Samples."samples.dremio.com"."NYC-taxi-trips-iceberg"  
   ON     (TO_CHAR(CAST(pickup_datetime AS DATE), 'YYYY-MM-DD')) = SUBSTRING(CAST("date" AS CHAR) FROM 0 FOR 10)  
   GROUP BY prcp;
   ```

You will get the query results, as shown in the image below.

![The result of the query to join the datasets with the average tip amount per precipitation level.](/images/get-started/docker-run-query.png "The result of the query with the average the tip amount per precipitation level.")

### Create the View for the Data Product

In Dremio, views are virtual tables based on the result set of a query. You can create views from data that resides in any data source, folder, table, or view that you have access to. You can also share views you've created with stakeholders in your organization.

Let's create a view for the data product from the query that you ran above:

1. Click **Save as View** on the far right to create a view of your query that others can access.
2. On the Save View As dialog, enter a name for your view. For example, `avg_tips_precipitation`.
3. Click **Save**.

Your view is created and ready to be used.

## Step 4: Accelerate the Query with Reflections

In this step, you will use [Reflections](/current/acceleration) to accelerate queries, particularly when working with large datasets.

### Enable the Reflection

Let's enable a [Raw Reflection](/current/acceleration/#types) to accelerate the query of your view:

1. Select the **Reflections** tab at the top of the page, toggle the **Raw Reflections** switch to on, and click **Save**.
2. On the far right, you will see an animated spinner icon close to **Footprint**. Wait until it turns into a green checkmark, which means that your query has been accelerated.

### Run the Accelerated Query

Let's now query the view and see the acceleration in action:

1. Click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "The Datasets page icon."), click `avg_tips_precipitation`, and click **Run** to execute the query.
2. Check the execution time. It's **a sub-second query**!

   ![The query with a highlight in the execution time after the acceleration.](/images/get-started/docker-reflections-after.png "The query execution time after the acceleration.")
3. Now, go to the Jobs tab, and confirm that the query was accelerated with a Reflection.

   ![The details of a query showing it was accelerated with a Reflection.](/images/get-started/docker-reflections-details.png "The details of a query showing the acceleration with a Reflection.")

You’ve just created a Raw Reflection and accelerated your query!

While creating a Reflection manually is a great way to understand how Dremio boosts performance, you don’t need to manage this complexity yourself in real-world environments if you use [Autonomous Reflections](/current/acceleration/autonomous-reflections) — available exclusively in the Enterprise Edition. Dremio will automatically create, select, and maintain the most efficient Reflections for you, saving time while ensuring consistently fast performance of your queries.

And that's it! You finished the Get Started guide for the Community Edition on Docker.

For a more complete and full-featured experience with Dremio, [sign up for the Enterprise Edition free trial](https://www.dremio.com/get-started/?utm_source=dremio-docs&utm_medium=referral) on the Dremio website, and follow the steps in [Get Started with the Enterprise Edition Free Trial](/current/get-started/kubernetes-trial).

Was this page helpful?

[Previous

Enterprise Edition Free Trial](/current/get-started/kubernetes-trial)[Next

Quick Tour of the Console](/current/get-started/quick_tour)

* Prerequisites
* Step 1: Deploy Dremio
* Step 2: Add the Sample Data
  + Add the Datasets
  + Format the Datasets
* Step 3: Create a Data Product
  + Run the Query for the Data Product
  + Create the View for the Data Product
* Step 4: Accelerate the Query with Reflections
  + Enable the Reflection
  + Run the Accelerated Query

---

# Source: https://docs.dremio.com/current/get-started/quick_tour

Version: current [26.x]

On this page

# Quick Tour of the Console

This section walks you through the Dremio console and how to best use the different capabilities to get to insights quickly and how to manage your data products.

The Dremio console has two main pages:

* **Datasets page**: Provides a view of your data products and underlying source tables. You can discover and explore your data on this page. For a quick tour of the Datasets page, see [Datasets Page Quick Tour](/current/get-started/quick_tour#datasets-page).
* **SQL Runner**: An easy to use editor to query data and create data products. For a quick tour of the SQL Runner, see [SQL Runner Quick Tour](/current/get-started/quick_tour#sql-runner).

## Datasets Page

When you work on the Datasets page, there are different components that you can use to manage your data. The largest component is the **Data** panel, which is used to explore the spaces and sources in your data catalog, as shown in this image:

![This screenshot is displaying the Data panel.](/images/sw24-1-software-data-panel-Nessie-sm-labeled.png "This screenshot is displaying the Data panel.")

| Location | Description |
| --- | --- |
| 1 | By default, you have a home space that you can further organize by creating a hierarchy of folders, and you can create additional spaces. |
| 2 | A [space](/current/what-is-dremio/key-concepts#spaces-and-folders) is a directory in which views are saved. Spaces provide a way to group datasets by common themes such as a project, purpose, department, or geographic region. |
| 3 | A [source](/current/data-sources/) is a data lake or external source (such as a relational database) that you can connect to Dremio. |
| 4 | The title indicates that the Samples data lake is open and lists the contents of the sample source. A source also consists of layers, so if you expand a data source, you will find datasets and data types within the datasets. |
| 5 | A [dataset](/current/what-is-dremio/key-concepts/#tables-and-views) is a collection of data. The datasets stored in files can be in many different formats, and to run SQL queries against data in different formats, you can create tables and views. By default, when you click on a dataset, the SQL editor is opened on the SQL Runner page with a `SELECT * FROM <dataset_name>` statement. To get a preview of the query, click **Run** or **Preview**. If you would rather click directly on a dataset to see or edit the definition, see [Preferences](/current/help-support/advanced-topics/dremio-preferences) for modifying this setting. |

### Opening Datasets

If you have privileges to modify the table or view, you will have the option of viewing and editing the table or view definition. When viewing or editing a table or view, you are directed to the **Data** tab by default, which shows the definitions of the table or view. For more options, check out the other tabs:

![This is a screenshot showing the Datasets page.](/images/software-dataset-components.png "This is a screenshot showing the Datasets page.")

| Location | Description |
| --- | --- |
| 1 | [Details](/current/data-products/govern/wikis-tags) shows the columns in a dataset and lets you add information about a specific dataset in its wiki. You can add searchable labels, which enhances team collaboration because other users can search the labels to trace a specific dataset. |
| 2 | [Lineage](/current/data-products/govern/lineage) is a graph of the dataset, showing its data source, parent datasets, and children datasets. |
| 3 | [Reflections](/current/acceleration/) are physically optimized representations of source data. |

Tabs are made visible based on the privileges that you have.

## SQL Runner

The SQL Runner is where you run queries on your datasets and get results. To navigate to the SQL Runner, click ![](/images/cloud/sql-runner-icon.png) in the side navigation bar. The main components of the SQL Runner are highlighted below:

![The main components of the SQL Runner are highlighted.](/images/software-sql-runner.png "SQL Runner")

caution

Dremio's query engine intentionally ignores any file or folder if the filename or folder name starts with a period (“.”) or an underscore (“\_”).

### 1. Data

The **Data** panel is used to explore your data catalog, which includes [sources](/current/data-sources/), [tables, and views](/current/what-is-dremio/key-concepts#tables--views). For catalog objects that you use frequently, you can star the objects to make them easier to access from the panel.

To add a dataset into the SQL editor, go to the data source. Use the left caret > to expand the source view. Locate the dataset that you would like to use within the query. Click the + button or drag and drop the data into the SQL editor.

### 2. Scripts

You can save your SQL as a script if you have drafts or SQL statements that you run frequently. Each saved script has a name, when the script was created or modified, and the context that was set for the editor.

In the **Scripts** panel, you can:

* Open a script in the SQL editor
* Rename a script
* Delete a script
* Share a script by [granting privileges](/current/security/rbac/privileges/#granting-privileges)
* Search your set of scripts by name
* Sort scripts by name or date

### 3. Run Mode

Running the query routes it to the engine and returns the complete result set. Dremio's query engine intentionally ignores any file or folder if the filename or folder name starts with a period (“.”) or an underscore (“\_”).

caution

If the engine scaled down, the startup time will take about two minutes.

note

Sometimes `COUNT(*)` and `SELECT` query results do not match because the result of queries run in the Dremio app has a threshold of one million. Depending on the number of threads (minor fragments) and how data is distributed among those threads, Dremio could truncate results before reaching the threshold. Each individual thread stops processing after returning a number of records equal to `threshold/# of threads`. For example, a query runs with 10 threads and should return 800,000 records, but one of the threads is responsible for 400,000 records. The per-thread threshold is 100,000, so that thread will only return 100,000 records and you will only see 500,000 records in the output. When results are truncated, the Dremio app will display a warning that the results are not complete and users can execute the query using JDBC/ODBC to get complete results.

note

Known issue: Running a `USE` statement will not update the context that is set in the SQL Runner.

### 4. Preview Mode

Executing a preview returns a subset of rows in the result set. Like the run mode, running the preview job will route the query to the selected engine, although the preview mode runs a subset of your results in less time.

### 5. SQL Editor

The SQL editor is where you create and edit queries to get insight from your data. In the top-right corner of the SQL editor, you'll find:

![](/assets/images/sql-editor-1df8d782abd0150557177c5e72d144f0.png)

a. Create a new tab by clicking **+** next to the other tabs. Because a tab is defined by a session, a new tab is automatically saved as a script and named as the date and time that the session was created, such as `Nov 3, 2023, 10:19:57 AM`.

b. Grant [script privileges](/current/security/rbac/privileges/#granting-privileges) to share a saved script with others in your organization.

c. Save your SQL as a script or as a view. You can save a script even if there are syntax errors. Saving a new view requires valid syntax, and there can be only one SQL statement in the editor. When you save the script as a view, the tab will remain open in the SQL Runner and the Edit dataset page for the view will open in a new browser tab.

d. Set a **Context** for a session to run queries without having to qualify the referenced objects.

e. Use **fx** to see a list of functions supported by Dremio along with a short description and syntax of each function. Click on the + button or drag and drop the function template into the SQL editor. For more information on supported SQL, see the [SQL Reference](/current/reference/sql/).

f. Toggle the **dark/light mode** to change the theme of the SQL editor.

g. Enable autocomplete to receive suggestions for SQL keywords, catalog objects, and functions while you are constructing SQL statements. Suggestions depend on the context set in the SQL Runner. To enable or disable the autocomplete feature, see [Dremio Preferences](/current/help-support/advanced-topics/dremio-preferences).

h. Click the keyboard button to see the shortcuts for the SQL Runner. For a list of shortcuts, see [Keyboard Shortcuts](/current/help-support/keyboard-shortcuts).

#### Syntax Error Highlighting

Before you run a query, make sure to fix any syntax errors that have been detected in your query.

The SQL editor automatically checks for syntax errors, and every detected error is marked with a red wavy underline. If you hover over the error, you’ll see a message stating whether the error is the result of a token that is missing, unexpected, unrecognized, or extraneous in the query.

#### Running Multiple Queries

You can run multiple queries in the SQL editor by using a semicolon to separate each statement. To run all of the queries in the SQL editor, simply click **Run**. The results of each query will be shown in the same order that the queries are constructed:

![](/assets/images/multiple-queries-e0d47509f2d191a19517e666732b66e3.png)

When you have multiple queries, you can also select a subset to run. If you select one or more queries and then click **Run**, only the selected queries will run accordingly, as shown below:

![](/assets/images/select-multiple-queries-db16bfe6d0aff008ac78896692644232.png)

### 6. Result Set Actions

Above the top-right corner of the result set, you will find these actions:

![](/assets/images/result-set-actions-0d0110a7f9dccebf985083f82d95eba9.png)

a. Download the result set as a JSON, CSV, or Parquet file. By default, downloading writes out the results from the last run of the query into the download file. To trigger a rerun of queries for downloads, see the [Rerun on download preference](/current/help-support/advanced-topics/dremio-preferences).

b. Copy result set to a clipboard. If the result set is too large, then download the table content to get the complete results.

note

* The option to download as a CSV file is not available if the result set includes one or more columns that have complex datatypes (ie., a union, map, or array). Column headers for the results table indicate complex types with this icon: ![](data:image/png;base64,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)
* The download process runs a CREATE TABLE AS SELECT (CTAS) command, which is why compute resources are required.

The download and copy results features can be enabled or disabled for a project in [Dremio Preferences](/current/help-support/advanced-topics/dremio-preferences). Disabling this in a project will prevent all users from downloading and copying results from the project.

### 7. Execution State

The execution state will show you the type of job that was run, the number of records, and the amount of time that it took to run the query. When you click on the linked job, a Job Overview page opens in a new tab, providing a summary, total execution time, Reflections data, job results, and more details. If a job took too long or failed, [viewing the job overview](/current/admin/monitoring/jobs/) can help you troubleshoot what actually happened.

![](/assets/images/execution-state-21cf846753f9770af207bac5cf203d62.png)

### 8. Transformations

Transformations can be applied to data. Using the following no-code UI flows automatically updates the SQL in the SQL editor:

* **Add Field**
* **Group By**
* **Join**
* **Filter Columns**

If you are using the preview mode, transformations use a subset of the results and may not provide a complete profile of the result set. It may show null or incomplete values in the dataset as a result of joining, grouping, or calculating fields. You may encounter an error showing "no rows returned due to the LIMIT logic" or "more rows returned due to an outer join".

### 9. Results Table

The results of the query are shown in a table format. You can edit a table column by clicking directly on the column title to open a dropdown of edit options, which include sorting results, converting data types, renaming columns, and calculating fields.

![](/assets/images/results-table-8a8d426aecc409f3d4bd92442db917e6.png)

You can edit a result value directly if you click and drag your cursor over the result value, which opens a dropdown of available edit options such as to replace, keep only, exclude, or copy the result value.

tip

Downloading large result sets could produce delays and errors. If you encounter these issues, create smaller views that summarize the results. You can then run queries on these smaller views and download the results.

## Additional Resources

Find out more about Dremio by enrolling in the [Dremio Fundamentals course in Dremio University](https://university.dremio.com/course/dremio-fundamentals-software).

Was this page helpful?

[Previous

Community Edition on Docker](/current/get-started/docker)[Next

What is Dremio?](/current/what-is-dremio/)

* Datasets Page
  + Opening Datasets
* SQL Runner
  + 1. Data
  + 2. Scripts
  + 3. Run Mode
  + 4. Preview Mode
  + 5. SQL Editor
  + 6. Result Set Actions
  + 7. Execution State
  + 8. Transformations
  + 9. Results Table
* Additional Resources

---

# Source: https://docs.dremio.com/current/get-started/quick_tour/

Version: current [26.x]

On this page

# Quick Tour of the Console

This section walks you through the Dremio console and how to best use the different capabilities to get to insights quickly and how to manage your data products.

The Dremio console has two main pages:

* **Datasets page**: Provides a view of your data products and underlying source tables. You can discover and explore your data on this page. For a quick tour of the Datasets page, see [Datasets Page Quick Tour](/current/get-started/quick_tour#datasets-page).
* **SQL Runner**: An easy to use editor to query data and create data products. For a quick tour of the SQL Runner, see [SQL Runner Quick Tour](/current/get-started/quick_tour#sql-runner).

## Datasets Page

When you work on the Datasets page, there are different components that you can use to manage your data. The largest component is the **Data** panel, which is used to explore the spaces and sources in your data catalog, as shown in this image:

![This screenshot is displaying the Data panel.](/images/sw24-1-software-data-panel-Nessie-sm-labeled.png "This screenshot is displaying the Data panel.")

| Location | Description |
| --- | --- |
| 1 | By default, you have a home space that you can further organize by creating a hierarchy of folders, and you can create additional spaces. |
| 2 | A [space](/current/what-is-dremio/key-concepts#spaces-and-folders) is a directory in which views are saved. Spaces provide a way to group datasets by common themes such as a project, purpose, department, or geographic region. |
| 3 | A [source](/current/data-sources/) is a data lake or external source (such as a relational database) that you can connect to Dremio. |
| 4 | The title indicates that the Samples data lake is open and lists the contents of the sample source. A source also consists of layers, so if you expand a data source, you will find datasets and data types within the datasets. |
| 5 | A [dataset](/current/what-is-dremio/key-concepts/#tables-and-views) is a collection of data. The datasets stored in files can be in many different formats, and to run SQL queries against data in different formats, you can create tables and views. By default, when you click on a dataset, the SQL editor is opened on the SQL Runner page with a `SELECT * FROM <dataset_name>` statement. To get a preview of the query, click **Run** or **Preview**. If you would rather click directly on a dataset to see or edit the definition, see [Preferences](/current/help-support/advanced-topics/dremio-preferences) for modifying this setting. |

### Opening Datasets

If you have privileges to modify the table or view, you will have the option of viewing and editing the table or view definition. When viewing or editing a table or view, you are directed to the **Data** tab by default, which shows the definitions of the table or view. For more options, check out the other tabs:

![This is a screenshot showing the Datasets page.](/images/software-dataset-components.png "This is a screenshot showing the Datasets page.")

| Location | Description |
| --- | --- |
| 1 | [Details](/current/data-products/govern/wikis-tags) shows the columns in a dataset and lets you add information about a specific dataset in its wiki. You can add searchable labels, which enhances team collaboration because other users can search the labels to trace a specific dataset. |
| 2 | [Lineage](/current/data-products/govern/lineage) is a graph of the dataset, showing its data source, parent datasets, and children datasets. |
| 3 | [Reflections](/current/acceleration/) are physically optimized representations of source data. |

Tabs are made visible based on the privileges that you have.

## SQL Runner

The SQL Runner is where you run queries on your datasets and get results. To navigate to the SQL Runner, click ![](/images/cloud/sql-runner-icon.png) in the side navigation bar. The main components of the SQL Runner are highlighted below:

![The main components of the SQL Runner are highlighted.](/images/software-sql-runner.png "SQL Runner")

caution

Dremio's query engine intentionally ignores any file or folder if the filename or folder name starts with a period (“.”) or an underscore (“\_”).

### 1. Data

The **Data** panel is used to explore your data catalog, which includes [sources](/current/data-sources/), [tables, and views](/current/what-is-dremio/key-concepts#tables--views). For catalog objects that you use frequently, you can star the objects to make them easier to access from the panel.

To add a dataset into the SQL editor, go to the data source. Use the left caret > to expand the source view. Locate the dataset that you would like to use within the query. Click the + button or drag and drop the data into the SQL editor.

### 2. Scripts

You can save your SQL as a script if you have drafts or SQL statements that you run frequently. Each saved script has a name, when the script was created or modified, and the context that was set for the editor.

In the **Scripts** panel, you can:

* Open a script in the SQL editor
* Rename a script
* Delete a script
* Share a script by [granting privileges](/current/security/rbac/privileges/#granting-privileges)
* Search your set of scripts by name
* Sort scripts by name or date

### 3. Run Mode

Running the query routes it to the engine and returns the complete result set. Dremio's query engine intentionally ignores any file or folder if the filename or folder name starts with a period (“.”) or an underscore (“\_”).

caution

If the engine scaled down, the startup time will take about two minutes.

note

Sometimes `COUNT(*)` and `SELECT` query results do not match because the result of queries run in the Dremio app has a threshold of one million. Depending on the number of threads (minor fragments) and how data is distributed among those threads, Dremio could truncate results before reaching the threshold. Each individual thread stops processing after returning a number of records equal to `threshold/# of threads`. For example, a query runs with 10 threads and should return 800,000 records, but one of the threads is responsible for 400,000 records. The per-thread threshold is 100,000, so that thread will only return 100,000 records and you will only see 500,000 records in the output. When results are truncated, the Dremio app will display a warning that the results are not complete and users can execute the query using JDBC/ODBC to get complete results.

note

Known issue: Running a `USE` statement will not update the context that is set in the SQL Runner.

### 4. Preview Mode

Executing a preview returns a subset of rows in the result set. Like the run mode, running the preview job will route the query to the selected engine, although the preview mode runs a subset of your results in less time.

### 5. SQL Editor

The SQL editor is where you create and edit queries to get insight from your data. In the top-right corner of the SQL editor, you'll find:

![](/assets/images/sql-editor-1df8d782abd0150557177c5e72d144f0.png)

a. Create a new tab by clicking **+** next to the other tabs. Because a tab is defined by a session, a new tab is automatically saved as a script and named as the date and time that the session was created, such as `Nov 3, 2023, 10:19:57 AM`.

b. Grant [script privileges](/current/security/rbac/privileges/#granting-privileges) to share a saved script with others in your organization.

c. Save your SQL as a script or as a view. You can save a script even if there are syntax errors. Saving a new view requires valid syntax, and there can be only one SQL statement in the editor. When you save the script as a view, the tab will remain open in the SQL Runner and the Edit dataset page for the view will open in a new browser tab.

d. Set a **Context** for a session to run queries without having to qualify the referenced objects.

e. Use **fx** to see a list of functions supported by Dremio along with a short description and syntax of each function. Click on the + button or drag and drop the function template into the SQL editor. For more information on supported SQL, see the [SQL Reference](/current/reference/sql/).

f. Toggle the **dark/light mode** to change the theme of the SQL editor.

g. Enable autocomplete to receive suggestions for SQL keywords, catalog objects, and functions while you are constructing SQL statements. Suggestions depend on the context set in the SQL Runner. To enable or disable the autocomplete feature, see [Dremio Preferences](/current/help-support/advanced-topics/dremio-preferences).

h. Click the keyboard button to see the shortcuts for the SQL Runner. For a list of shortcuts, see [Keyboard Shortcuts](/current/help-support/keyboard-shortcuts).

#### Syntax Error Highlighting

Before you run a query, make sure to fix any syntax errors that have been detected in your query.

The SQL editor automatically checks for syntax errors, and every detected error is marked with a red wavy underline. If you hover over the error, you’ll see a message stating whether the error is the result of a token that is missing, unexpected, unrecognized, or extraneous in the query.

#### Running Multiple Queries

You can run multiple queries in the SQL editor by using a semicolon to separate each statement. To run all of the queries in the SQL editor, simply click **Run**. The results of each query will be shown in the same order that the queries are constructed:

![](/assets/images/multiple-queries-e0d47509f2d191a19517e666732b66e3.png)

When you have multiple queries, you can also select a subset to run. If you select one or more queries and then click **Run**, only the selected queries will run accordingly, as shown below:

![](/assets/images/select-multiple-queries-db16bfe6d0aff008ac78896692644232.png)

### 6. Result Set Actions

Above the top-right corner of the result set, you will find these actions:

![](/assets/images/result-set-actions-0d0110a7f9dccebf985083f82d95eba9.png)

a. Download the result set as a JSON, CSV, or Parquet file. By default, downloading writes out the results from the last run of the query into the download file. To trigger a rerun of queries for downloads, see the [Rerun on download preference](/current/help-support/advanced-topics/dremio-preferences).

b. Copy result set to a clipboard. If the result set is too large, then download the table content to get the complete results.

note

* The option to download as a CSV file is not available if the result set includes one or more columns that have complex datatypes (ie., a union, map, or array). Column headers for the results table indicate complex types with this icon: ![](data:image/png;base64,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)
* The download process runs a CREATE TABLE AS SELECT (CTAS) command, which is why compute resources are required.

The download and copy results features can be enabled or disabled for a project in [Dremio Preferences](/current/help-support/advanced-topics/dremio-preferences). Disabling this in a project will prevent all users from downloading and copying results from the project.

### 7. Execution State

The execution state will show you the type of job that was run, the number of records, and the amount of time that it took to run the query. When you click on the linked job, a Job Overview page opens in a new tab, providing a summary, total execution time, Reflections data, job results, and more details. If a job took too long or failed, [viewing the job overview](/current/admin/monitoring/jobs/) can help you troubleshoot what actually happened.

![](/assets/images/execution-state-21cf846753f9770af207bac5cf203d62.png)

### 8. Transformations

Transformations can be applied to data. Using the following no-code UI flows automatically updates the SQL in the SQL editor:

* **Add Field**
* **Group By**
* **Join**
* **Filter Columns**

If you are using the preview mode, transformations use a subset of the results and may not provide a complete profile of the result set. It may show null or incomplete values in the dataset as a result of joining, grouping, or calculating fields. You may encounter an error showing "no rows returned due to the LIMIT logic" or "more rows returned due to an outer join".

### 9. Results Table

The results of the query are shown in a table format. You can edit a table column by clicking directly on the column title to open a dropdown of edit options, which include sorting results, converting data types, renaming columns, and calculating fields.

![](/assets/images/results-table-8a8d426aecc409f3d4bd92442db917e6.png)

You can edit a result value directly if you click and drag your cursor over the result value, which opens a dropdown of available edit options such as to replace, keep only, exclude, or copy the result value.

tip

Downloading large result sets could produce delays and errors. If you encounter these issues, create smaller views that summarize the results. You can then run queries on these smaller views and download the results.

## Additional Resources

Find out more about Dremio by enrolling in the [Dremio Fundamentals course in Dremio University](https://university.dremio.com/course/dremio-fundamentals-software).

Was this page helpful?

[Previous

Community Edition on Docker](/current/get-started/docker)[Next

What is Dremio?](/current/what-is-dremio/)

* Datasets Page
  + Opening Datasets
* SQL Runner
  + 1. Data
  + 2. Scripts
  + 3. Run Mode
  + 4. Preview Mode
  + 5. SQL Editor
  + 6. Result Set Actions
  + 7. Execution State
  + 8. Transformations
  + 9. Results Table
* Additional Resources