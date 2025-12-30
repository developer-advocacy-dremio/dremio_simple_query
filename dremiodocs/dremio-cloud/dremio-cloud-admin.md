# Administration | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/

On this page

Dremio administration covers organization-wide and project-level management. Use these tools to configure your environment, manage users and resources, and monitor system performance.

## Organization Management

* [Manage Your Subscription](/dremio-cloud/admin/subscription/) – Upgrade from a free trial to a paid subscription, manage billing and payment methods, and track your organization's usage and costs.
* [Manage Users](/dremio-cloud/admin/users) – Add users to your organization, configure authentication methods (local or SSO), manage user roles and privileges, and control access to Dremio resources.
* [Configure Model Providers](/dremio-cloud/admin/model-providers) – Configure AI model providers for Dremio's AI Agent, enabling natural language queries and data exploration across your organization.

## Project Management

* [Manage Projects](/dremio-cloud/admin/projects/) – Create new projects to isolate compute and data resources for different teams. Configure storage options (Dremio-managed or your own S3 bucket) and manage project-level settings.
* [Manage Engines](/dremio-cloud/admin/engines/) – Set up and configure query engines that provide the compute resources for running queries. Choose engine sizes, configure auto-scaling, and manage multiple engine replicas for your projects.
* [Configure External Engines](/dremio-cloud/admin/external-engines) – Connect industry-standard engines like Apache Spark, Trino, and Apache Flink directly to Dremio without vendor lock-in or proprietary protocols.
* [Monitor Jobs and Audit Logs](/dremio-cloud/admin/monitor/) – Monitor system health, query performance, and resource utilization. View metrics, logs, and alerts to ensure your Dremio environment is running optimally.
* [Optimize Performance](/dremio-cloud/admin/performance/) – Improve query performance and resource efficiency through Reflection management and the results cache.

## Shared Responsibility Model

Dremio operates on a shared responsibility model. For detailed information about responsibilities in each area, download the [Dremio Shared Responsibility Model](https://docs-3063.dremio-documentation.pages.dev/assets/files/Dremio-Cloud-Shared-Responsibility-Model-15f76b24f0b48153532ca15b25d831c4.pdf).

Was this page helpful?

* Organization Management
* Project Management
* Shared Responsibility Model

<div style="page-break-after: always;"></div>

# Manage Users | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/users

On this page

Manage user access to your Dremio organization through internal authentication or external identity providers. This page covers user types, account management, and administrative tasks.

All users in Dremio are identified by their email address, which serves as their username. Invitations are sent to users' email addresses to set up their accounts.

## User Types

Dremio supports two user types with different authentication and management workflows:

| Feature | Local Users | SSO Users |
| --- | --- | --- |
| **Authentication** | Password set in Dremio | Identity Provider (IdP) credentials |
| **Credential Management** | Within Dremio | Through your IdP |
| **Provisioning** | Manual invitation | Manual invitation or SCIM automated |
| **Password Reset** | Self-service or admin-initiated | Through IdP only |

### Local Users

Local users authenticate with passwords managed directly in Dremio. These users must be invited manually. Use local users when you need standalone accounts for contractors, external partners, or testing and development environments.

### SSO Users

SSO users authenticate through your organization's identity provider (IdP) like Microsoft Entra ID or Okta, or through social identity providers like Google or GitHub. These users can be invited manually or provisioned automatically via System for Cross-domain Identity Management (SCIM).

#### What is SCIM?

SCIM is an open standard protocol that automates user provisioning between your identity provider and Dremio. Instead of manually creating and managing users in multiple systems, SCIM keeps everything synchronized automatically. When you add, update, or remove a user in your IdP, those changes propagate to Dremio without manual intervention.

#### SCIM Provisioning Benefits

When SCIM is configured, Dremio stays synchronized with your IdP. Deleting a user in your IdP automatically reflects in Dremio. Additional benefits of SCIM integration include:

* Automatic user creation and deactivation
* Synchronized user attributes
* Centralized access management

To learn more:

* [Configure SCIM with Microsoft Entra ID](/dremio-cloud/security/authentication/idp/microsoft-entra-id)
* [Configure SCIM with Okta](/dremio-cloud/security/authentication/idp/okta)
* [Configure SCIM with a generic OIDC provider](/dremio-cloud/security/authentication/idp/generic-oidc-provider)

## Manage Your Account

### Update Your Password

**Local users** can reset passwords using either method:

**If locked out:**

1. On the login screen, enter your email.
2. Click **Forgot Password?**.
3. Check your email for the reset link.

**If logged in:**

1. Hover over the user icon at the bottom of the navigation sidebar.
2. Select **Account Settings**.
3. Click **Reset Password**.
4. Check your email for the reset link.

Changing your password ends all existing Dremio web sessions.

**SSO users** must reset passwords through their organization's identity provider. Contact your authentication administrator for assistance.

### Update Your Name

You can change your display name at any time:

1. Click the user icon on the side navigation bar.
2. Select **Account Settings**.
3. On the **General Information** page, edit **First Name** and **Last Name**.
4. Click **Save**.

## Administrative Tasks

The following tasks require administrator privileges or the [CREATE USER](/dremio-cloud/security/privileges#organization-privileges) privilege.

### View All Users

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and choose **Organization settings**.
2. Select **Users** in the organization settings sidebar.

The table displays all local and SSO users with access to your Dremio instance.

### Add a User

**SSO users** are added automatically when you configure [SCIM provisioning](/dremio-cloud/security/authentication/idp#scim).

**To add a local user:**

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and choose **Organization settings**.
2. Select **Users**.
3. Click **Add Users**.
4. In the **Email address(es)** field, enter one or more email addresses separated by commas, spaces, or line breaks.
5. For **Dremio Role**, select the [roles](/dremio-cloud/security/roles) where the user will be a member. All users are members of the PUBLIC role by default.
6. Click **Add**.

Each user receives an invitation email to set up their account. You can configure additional roles after users accept their invitations.

A user's email address serves as their unique identifier and cannot be changed after account creation. If a user's email changes, you must create a new account with the new email address.

If invited users don't receive the email, check spam folders and verify the email addresses are correct.

### Edit a User

You can modify a user's name and role assignments. Email addresses cannot be edited—if a user's email changes, you must create a new account.

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and choose **Organization settings**.
2. Select **Users**.
3. Hover over the user's row and click ![Edit icon](/images/icons/edit.png) to edit the user.
4. **Details tab:** Edit **First Name** and **Last Name**, then click **Save**.
5. **Roles tab:** Manage role assignments:
   * **Add roles:** Search for and select roles, then click **Add Roles**.
   * **Remove roles:** Hover over a role and click **Remove**.
6. Click **Save**.

### Reset a User's Password

This option is only available for local users. SSO users must reset passwords through their identity provider. To send a password reset email to a local user:

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and choose **Organization settings**.
2. Select **Users**.
3. Click the user's name.
4. Click **Send Password Reset**.

The user receives an immediate email with reset instructions.

### Remove a User

**To remove an SSO user:**

1. First, remove the user from your external identity provider.
2. Then follow the steps below to remove them from Dremio.

**To remove a local user:**

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and choose **Organization settings**.
2. Select **Users**.
3. Click the user's name.
4. Click ![Remove icon](/images/icons/trash.png) to remove.
5. Confirm the deletion.

## Related Topics

* [Roles](/dremio-cloud/security/roles)
* [Privileges](/dremio-cloud/security/privileges)
* [Configure Identity Providers](/dremio-cloud/security/authentication/idp/)

Was this page helpful?

* User Types
  + Local Users
  + SSO Users
* Manage Your Account
  + Update Your Password
  + Update Your Name
* Administrative Tasks
  + View All Users
  + Add a User
  + Edit a User
  + Reset a User's Password
  + Remove a User
* Related Topics

<div style="page-break-after: always;"></div>

# Manage Engines | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/engines/

On this page

An engine is a Dremio entity that manages compute resources. Each engine has one or more replicas that are created for executing queries. An engine replica consists of a group of executor instances defined by the engine capacity.

When you signed up for Dremio, an organization and a project were automatically created. Each new project has a preview engine. The preview engine, by default, will scale down after 1 hour without a query. As the name suggests, it provides previews of queries and datasets. Unlike other engines, the preview engine cannot be disabled.

If an engine is created with a minimum replica of 0, it remains idle until the first query runs. No executor instances run initially. When you run a query, Dremio allocates executors to your project and starts the engine. Engines automatically start and stop based on query load.

## Sizes

Dremio provides a standard executor, which is used in all of our query engine sizes. Query engine sizes are differentiated by the number of executors in a replica. For each size, Dremio provides a default query concurrency, as shown in the table below.

| Replica Size | Executors per Replica | DCUs | Default Concurrency | Max Concurrency |
| --- | --- | --- | --- | --- |
| 2XSmall | 1 | 14 | 2 | 20 |
| XSmall | 1 | 30 | 4 | 40 |
| Small | 2 | 60 | 6 | 60 |
| Medium | 4 | 120 | 8 | 80 |
| Large | 8 | 240 | 10 | 100 |
| XLarge | 16 | 480 | 12 | 120 |
| 2XLarge | 32 | 960 | 16 | 160 |
| 3XLarge | 64 | 1920 | 20 | 200 |

## States

An engine can be in one of the following states.

| State | Icon | Description |
| --- | --- | --- |
| Running |  | Represents an enabled engine (replicas are provisioned automatically or running as per the minimum number of replicas configured). You can use this engine for running queries. |
| Adding Replica |  | Represents an engine that is scaling up (adding a replica). |
| Removing Replica |  | Represents an engine that is scaling down (removing a replica). |
| Disabling |  | Represents an engine that is being disabled. |
| Disabled |  | Represents a disabled engine (no engine replicas have been provisioned dynamically or there are no active replicas). You cannot use this engine for running queries. |
| Starting Engine |  | Represents an engine that is starting (transitioning from the disabled state to the enabled state). |
| Stopping Engine |  | Represents an engine that is stopping (transitioning from the enabled state to the disabled state). |
| Stopped |  | Represents an enabled engine that has been stopped (zero replicas running). |
| Deleting |  | Represents an engine that is being deleted. |

## Autoscaling

The autoscaling capability dynamically manages query workload for you based on parameters that you set for the engine. Engine replicas are started and stopped as required to provide a seamless query execution by monitoring the engine replica health.

The following table describes the engine parameters along with their role in autoscaling.

| Parameter | Description |
| --- | --- |
| **Size** | The number of executors that make up an engine replica. |
| **Max Concurrency** | Maximum number of jobs that can be run concurrently on an engine replica. |
| **Last Replica Auto-Stop** | Time to wait before deleting the last replica if the engine is not in use. Not valid when the minimum engine replicas is 1 or higher. The default value is 2 hours. |
| **Enqueued Time Limit** | If there are no available resources, the query waits for a period of time that is set by this parameter. When this time limit exceeds, the query gets canceled. You are notified with the timeout during slot reservation error if the query gets canceled due to the query time limit being exceeded. The default value is 5 minutes. |
| **Query Runtime Limit** | Time a query can run before it is canceled. The default value is 5 minutes. |
| **Drain Time Limit** | Time until an engine replica continues to run after the engine is resized, disabled, or deleted before it is terminated and the running queries fail. The default value is 30 minutes. If there are no queries running on a replica, the engine is terminated without waiting for the drain time limit. |

For a query that is submitted to execute on an engine, the control plane assigns an engine replica to that query. Replicas are dynamically created and assigned to queries based on the query workload. The control plane observes the query workload and current active engine replicas to determine whether to scale up or scale down replicas. Replica is assigned to the query until the query execution is done. For a given engine, Dremio Cloud does not scale up replicas beyond the configured maximum replicas and it does not scale them down below the configured minimum replicas.

### Monitor Engine Health

The Dremio Cloud control plane monitors the engines health and manages unhealthy replicas to provide a seamless query execution experience. The replica nodes send periodic heartbeats to the control plane, which determines their liveness. If a periodic heartbeat is not returned from a replica node, the control plane marks that node as unhealthy and replaces it with a healthy one.

## View All Engines

To view engines:

1. In the Dremio Cloud application, click the Project Settings ![This is the icon that represents the Project Settings.](/images/icons/project-settings.png "Icon represents the Project Settings.") icon in the side navigation bar.
2. Select **Engines** in the project settings sidebar to see the list of engines in the project. On the **Engines** page, you can also see engines as per the status. Click the **Status** dropdown list to see the different statuses.

## Add an Engine

To add a new engine:

1. On the **Project Settings** page, select **Engines** in the project settings sidebar. The **Engines** page lists the engines created for the project. Every engine created in a project is created in the cloud account associated with that project.
2. Click the **Add Engine** button on the top-right of the **Engines** page to create a new engine.
3. In the **Add Engine** dialog, for **Engine**, enter a name.
4. (Optional) For **Description**, enter a description.
5. (Optional) For **Size**, select the size of the engine. The size designates the number of executors.
6. (Optional) For **Max Concurrency per Replica**, enter the maximum number of jobs that can be run concurrently on this engine.

The following parameters are for **Engine Replicas**:

7. For **Min Replicas**, enter the minimum number of engine replicas that Dremio Cloud has running at any given time. For auto-stop, set it to 0. To guarantee low-latency query execution, set it to 1 or higher. The default number of minimum replicas is 0.
8. For **Max Replicas**, enter the maximum number of engine replicas that Dremio Cloud scales up to. The default number of maximum replicas is 1.

tip

You can use these settings to control costs and ensure that excessive replicas are not spun up.

10. Under **Advanced Configuration**. For **Last Replica Auto-Stop**, enter the time to wait before deleting the last replica if engine is not in use. The default value is 2 hours, and the minimum value is 1 minute.

note

The last replica auto stop is not valid when the minimum number of engine replicas is 1 or higher.

The following parameters are for **Time Limit**:

11. For **Enable Enqueued Time Limit**, check the box.
12. For **Enqueued Time Limit**, enter the time a query waits before being cancelled. The default value is 5 minutes.

caution

You should not set the enqueued time limit to less than one minutes, which is the typical time to start a new replica. Changing this setting does not affect queries that are currently running or queued.

13. (Optional) For **Enable Query Time Limit**, check the box to enable the query time limit for making a query run before it is canceled.
14. (Optional) For **Query Runtime Limit**, enter the time a query can run before it is canceled. The default query runtime limit is 5 minutes.
15. For **Drain Time Limit**, enter the time (in minutes) that an engine replica continues to run after the engine is resized, disabled, or deleted before it is terminated and the running queries fail. The default value is 30 minutes. If there are no queries running on a replica, the engine is terminated without waiting for the drain time limit.
16. Click **Save and Launch**. This action saves the configuration, enables this engine, and allocates the executors.

## Edit an Engine

To edit an engine:

1. On the **Project Settings** page, select **Engines** in the project settings sidebar.
2. On the **Engines** page, hover over the row of the engine that you want to edit and click on the Edit Engine ![This is the icon that represents the Edit Engine settings.](/images/icons/edit.png "Icon represents the Edit Engines settings.") icon that appears next to the engine. The **Edit Engine** dialog is opened.

Alternatively, you can click the engine to go to the engine's page. Click the **Edit Engine** button on the top-right of the page.

note

You cannot edit the **Engine name** parameter.

3. For **Description**, enter a description.
4. For **Size**, select the size of the engine. The size designates the number of executors.
5. For **Max Concurrency per Replica**, enter the maximum number of jobs that can be run concurrently on this engine.

The following parameters are for **Engine Replicas**:

6. For **Min Replicas**, enter the number of engine replicas that Dremio has running at any given time. Set this value to 0 to enable auto-stop, or to 1 or higher to ensure low-latency query execution.
7. For **Max Replicas**, enter the maximum number of engine replicas that Dremio scales up to.
8. Under **Advanced Configuration**. **Last Replica Auto-Stop**, enter the time to wait before deleting the last replica if the engine is not in use. The default value is 2 hours.

note

The last replica auto-stop is not valid when the minimum number of engine replicas is 1 or higher.

The following parameters are for **Time Limit**:

10. For **Enable Enqueued Time Limit**, check the box.
11. For **Enqueued Time Limit**, enter the time a query waits before being canceled. The default value is 5 minutes.

caution

You should not set the enqueued time limit to less than one minutes, which is the typical time to start a new replica. Changing this setting does not affect queries that are currently running or queued.

12. (Optional) For **Enable Query Time Limit**, check the box to enable the query time limit for making a query run before it is canceled.
13. (Optional) For **Query Runtime Limit**, enter the time a query can run before it is canceled. The default query runtime limit is 5 minutes.
14. For **Drain Time Limit**, enter the time (in minutes) that an engine replica continues to run after the engine is resized, disabled, or deleted before it is terminated and any running queries fail. The default value is 30 minutes. If no queries are running on a replica, the engine is terminated without waiting for the drain time limit.
15. Click **Save**.

## Disable an Engine

You can disable an engine that is not being used:

To disable the engine:

1. On the **Project Settings** page, select **Engines** in the project settings sidebar. The list of engines in this project are displayed.
2. Disable the engine by using the toggle in the **Enabled** column.
3. Confirm that you want to disable the engine.

## Enable an Engine

To enable a disabled engine:

1. On the **Project Settings** page, select **Engines** in the project settings sidebar. The list of engines in this project are displayed.
2. Enable the engine by using the toggle in the **Enabled** column.
3. Confirm that you want to enable the engine.

## Delete an Engine

You can permanently delete an engine if it is not in use (this action is irreversible). If queries are running on the engine, then Dremio waits for the drain-time-limit for the running queries to complete before deleting the engine.

caution

An engine that has a routing rule associated with it cannot be deleted. Delete the rules before deleting the engine.

To delete an engine:

1. On the **Project Settings** page, select **Engines** in the project settings sidebar. The list of engines in this project are displayed.
2. On the **Engines** page, hover over the row of the engine that you want to delete and click the Delete ![This is the icon that represents the Delete settings.](/images/icons/trash.png "Icon represents the Delete settings.") icon that appears next to the engine.
3. Confirm that you want to delete the engine.

## Troubleshoot

If your engines are not scaling up or down as expected, you can reference the engine events to see the error that is causing the issue.

To view engine events:

1. On the **Project Settings** page, select **Engines** in the project settings sidebar. The list of engines in this project are displayed.
2. On the **Engines** page, click on the engine that you want to investigate.
3. In the engine details page, click on the **Events** tab to view the scaling events and status of each event.
4. If any scaling problems persist, contact [Dremio Support](https://support.dremio.com/).

Was this page helpful?

* Sizes
* States
* Autoscaling
  + Monitor Engine Health
* View All Engines
* Add an Engine
* Edit an Engine
* Disable an Engine
* Enable an Engine
* Delete an Engine
* Troubleshoot

<div style="page-break-after: always;"></div>

# Monitor | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/monitor/

On this page

As an administrator, you can monitor catalog usage and jobs in the Dremio console. You can also use the Dremio APIs and SQL to retrieve information about jobs and events for the projects in your organization.

### Monitor the Dremio Console

The Monitor page in the Dremio console allows you to monitor usage across your project, making it easier to observe patterns, analyze the resources being consumed by your data platform, and understand the impact on your users. You must be a member of the `ADMIN` role to access the Monitor page.

#### Catalog Usage

The data visualizations on the Monitor page point you to the most queried data and folders in a catalog.

Go to **Settings** > **Monitor** to view your catalog usage. When you open the Monitor page, you are directed to the Catalog Usage tab by default where you can see the following metrics:

* A table of the top 10 most queried datasets within the specified time range, including for each the number of linked jobs, the percentage of linked jobs in which the dataset was accelerated, and the total number of Reflections defined on the dataset
* A table of the top 10 most queried source folders within the specified time range, including for each the number of linked jobs and the top users of that folder

note

A source can be listed in the top 10 most queried source folders if the source contains a child dataset that was used in the query (for example, `postgres.accounts`). Queries of datasets in sub-folders (for example, `s3.mybucket.iceberg_table`) are classified by the sub-folder and not the source.

All datasets are assessed in the metrics on the Monitor page except for datasets in the [system tables](/dremio-cloud/sql/system-tables/) and the [information schema](/dremio-cloud/sql/information-schema/).

The metrics on the Monitor page analyze only user queries. Refreshes of data Reflections and metadata refreshes are excluded.

#### Jobs

The data visualizations on the Monitor page show the metrics for queries executed in your project, including statistics about performance and utilization.

Go to **Settings** > **Monitor** > **Jobs** to open the Jobs tab and see an aggregate view of the following metrics for the jobs that are running in your project:

* A report of today's job count and failed/canceled rate in comparison to yesterday's metrics
* A list of the top 10 most active users within the specified time range, including the number of linked jobs for each user
* Total jobs accelerated, total job time saved, and average job speedup from Autonomous Reflections over the past month
* Total number of jobs accelerated by autonomous and manual Reflections over time
* A graph showing the total number of completed and failed jobs over time (aggregated hourly or daily)
* A graph of all completed and failed jobs according to their engine (aggregated hourly or daily)
* A graph of all job states showing the percentage of time consumed for each [state](/dremio-cloud/admin/monitor/jobs#job-states-and-statuses) (aggregated hourly or daily)
* A table of the top 10 longest running jobs within the specified time range, including the linked ID, duration, user, query type, and start time of each job

To examine all jobs and the details of specific jobs, see [Viewing Jobs](/dremio-cloud/admin/monitor/jobs).

You can create reports of jobs in other BI tools by leveraging the [`sys.project.history.jobs` table](/dremio-cloud/sql/system-tables/jobs-historical).

### Monitor with Dremio APIs and SQL

Administrators can use the Dremio APIs and SQL to retrieve information about the jobs and events in every project in the organization. This information is useful for further monitoring and analysis.

Before you begin, make sure that you are assigned to the ADMIN role for the organization whose information you want to retrieve. You also need a [personal access token (PAT)](/dremio-cloud/security/authentication/personal-access-token#create-a-pat) to make the necessary API requests.

The code examples in this section are written in Python.

The procedure below provides individual code examples for retrieving project IDs, retrieving information for jobs and events, saving query results to Parquet files, and uploading the Parquet files to an AWS S3 bucket. See the combined example for a single code example that combines all of the steps.

1. Get the IDs for all projects in the organization. In the code example for this step, the `get_projects` method uses the [Projects](/dremio-cloud/api/projects) API to get the project IDs.

note

In the following code example, replace `<personal_access_token>` with your PAT.

To use the API control plane for the EU rather than the US, replace `https://api.dremio.cloud/` with `https://api.eu.dremio.cloud/`.

Get the IDs for all projects

```
import requests  
import json  
  
dremio_server = "https://api.dremio.cloud/"  
personal_access_token = "<personal_access_token>"  
  
headers = {  
   'Authorization': "Bearer " + personal_access_token,  
   'Content-Type': "application/json"  
}  
  
def api_get(endpoint: str) -> Response:  
   return requests.get(f'{dremio_server}/{endpoint}', headers=headers)  
  
def get_projects() -> dict:  
   """  
   Get all projects in the Dremio Cloud organization  
   :return: Dictionary of project IDs and project names  
   """  
   projects = dict()  
   projects_response = api_get('v0/projects')  
   for project in projects_response.json():  
       projects[project['id']] = project['name']  
   return projects
```

2. Run a SQL query to get the jobs or events for the project. The code examples for this step show how to use the [SQL](/dremio-cloud/api/sql) API to submit a SQL query, get all jobs during a specific period with the `get_jobs` method, and get all events in the [`sys.project.history.events`](/dremio-cloud/sql/system-tables/events-historical) system table during a specific period with the `get_events` method.

Submit SQL query using the API

```
def api_post(endpoint: str, body=None) -> Response:  
   return requests.post(f'{dremio_server}/{endpoint}',  
                        headers=headers, data=json.dumps(body))  
  
def run_sql(project_id: str, query: str) -> str:  
   """  
   Run a SQL query  
   :param project_id: project ID  
   :param query: SQL query  
   :return: query job ID  
   """  
   query_response = api_post(f'v0/projects/{project_id}/sql', body={'sql': query})  
   job_id = query_response.json()['id']  
   return job_id
```

Get all jobs in the project during a specific period

```
def api_post(endpoint: str, body=None) -> Response:  
   return requests.post(f'{dremio_server}/{endpoint}',  
                        headers=headers, data=json.dumps(body))  
  
def get_jobs(project_id: str, start_time: str, end_time: str) -> str:  
   """  
   Run SQL query to get all jobs in a project during the specified time period  
   :param project_id: project ID  
   :param start_time: start timestamp (inclusive)  
   :param end_time: end timestamp (exclusive)  
   :return: query job ID  
   """  
   query_response = api_post(f'v0/projects/{project_id}/sql', body={'sql': query})  
   job_id = run_sql(project_id, f'SELECT * FROM sys.project.history.jobs '  
                                f'WHERE "submitted_ts" >= \'{start_time}\' '  
                                f'AND "submitted_ts" < \'{end_time}\'')  
   return job_id
```

Get all events during a specific period

```
def get_events(project_id: str, start_time: str, end_time: str) -> str:  
   """  
   Run SQL query to get all events in sys.project.history.events during the specified time period  
   :param project_id: project ID  
   :param start_time: start timestamp (inclusive)  
   :param end_time: end timestamp (exclusive)  
   :return: query job ID  
   """  
   job_id = run_sql(project_id, f'SELECT * FROM sys.project.history.events '  
                                f'WHERE "timestamp" >= \'{start_time}\' '  
                                f'AND "timestamp" < \'{end_time}\'')  
   return job_id
```

3. Check the status of the query to get jobs or events. In the code example for this step, the `wait_for_job_complete` method periodically checks and returns the query job state and prints out the final job status when the query is complete.

Check status of the query to get jobs or events

```
def wait_for_job_complete(project_id: str, job_id: str) -> str:  
   """  
   Wait for a query job to complete  
   :param project_id: project ID  
   :param job_id: job ID  
   :return: if the job completed successfully, True; otherwise, False  
   """  
   while True:  
       time.sleep(1)  
       job = api_get(f'v0/projects/{project_id}/job/{job_id}')  
       job_state = job.json()["jobState"]  
       if job_state == 'COMPLETED':  
           print("Job complete.")  
           break  
       elif job_state == 'FAILED':  
           print("Job failed.", job.json()['errorMessage'])  
           break  
       elif job_state == 'CANCELED':  
           print("Job canceled.")  
           break  
  
   return job_state
```

4. Download the result for the query to get jobs or events and save it to a Parquet file. In the code example for this step, the `save_job_results_to_parquet` method downloads the query result and, if the result contains at least one row, saves the result to a single Parquet file.

Download query result and save to a Parquet file

```
def save_job_results_to_parquet(project_id: str, job_id: str,  
                               parquet_file_name: str) -> bool:  
   """  
   Download the query result and save it to a Parquet file  
   :param project_id: project ID  
   :param job_id: query job ID  
   :param parquet_file_name: file name to save the job result  
   :return: if the query returns more than 0 rows and parquet file is saved, True; otherwise False  
   """  
   offset = 0  
   rows_downloaded = 0  
   rows = []  
   while True:  
       job_result = api_get(f'v0/projects/{project_id}/job/{job_id}/'  
                            f'results/?offset={offset}&limit=500')  
       job_result_json = job_result.json()  
       row_count = job_result_json['rowCount']  
       rows_downloaded += len(job_result_json['rows'])  
       rows += job_result_json['rows']  
       if rows_downloaded >= row_count:  
           break  
       offset += 500  
  
   print(rows_downloaded, "rows")  
   if rows_downloaded > 0:  
       py_rows = pyarrow.array(job_result_json['rows'])  
       table = pyarrow.Table.from_struct_array(py_rows)  
       pyarrow.parquet.write_table(table, parquet_file_name)  
       return True  
  
   return False
```

5. If desired, you can use the [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) library to upload the Parquet file to an AWS S3 bucket.

Upload Parquet file to AWS S3 with Boto3 library

```
def upload_file(file_name: str, bucket: str, folder: str):  
   """Upload Parquet file to an S3 bucket with Boto3  
   :param file_name: File to upload  
   :param bucket: Bucket to upload to  
   :param folder: Folder to upload to  
   :return: True if file was uploaded, else False  
   """  
  
   # Upload the file  
   s3_client = boto3.client('s3')  
   try:  
       response = s3_client.upload_file(file_name, bucket, f'{folder}/{file_name}')  
   except ClientError as e:  
       print(e)  
       return False  
   return True
```

#### Combined Example

The following code example combines the steps above to get all jobs and events from all projects during a specific period, save the query results to Parquet files, and upload the Parquet files to an AWS S3 bucket. The parameter `start` is the start timestamp (inclusive) and the parameter `end` is the end timestamp (exclusive).

All jobs in each project during the specified time period are saved in an individual Parquet file with file name `jobs_<project_id><start>.parquet`. All events in each project during the specified time period are saved in one Parquet file with file name `events_<project_id><start>.parquet`.

Combine all steps in a single code example

```
def main(start: str, end: str):  
   """  
   Get all jobs and events from all projects during the specified time period, save the results in Parquet files, and upload the files to an AWS S3 bucket.  
   :param start: start timestamp (inclusive, in format "YYYY-MM-DD" or "YYYY-MM-DD hh:mm:ss"  
   :param end: end timestamp (exclusive, in format "YYYY-MM-DD" or "YYYY-MM-DD hh:mm:ss"  
   """  
   projects = get_projects()  
   print("Projects in organization:")  
   print(projects)  
  
   # Get jobs for each project  
   for project_id in projects:  
       print("Get jobs for project", projects[project_id])  
       # run query  
       job_id = get_jobs(project_id, start, end)  
       # check job status  
       job_state = wait_for_job_complete(project_id, job_id)  
       if job_state == "COMPLETED":  
           file_name = f'jobs_{project_id}{start}.parquet'  
           if save_job_results_to_parquet(project_id, job_id, file_name):  
               upload_file(file_name, 'S3_BUCKET_NAME', 'dremio/jobs')  
  
   for project_id in projects:  
       print("Get events for project", projects[project_id])  
       # run query  
       job_id = get_events(project_id, start, end)  
       # check job status  
       job_state = wait_for_job_complete(project_id, job_id)  
       if job_state == "COMPLETED":  
           file_name = f'events_{project_id}{start}.parquet'  
           if save_job_results_to_parquet(project_id, job_id, file_name):  
               upload_file(file_name, 'S3_BUCKET_NAME', 'dremio/events')  
  
if __name__ == "__main__":  
   parser = argparse.ArgumentParser(  
       description='Demo of collecting jobs and events from Dremio Cloud Projects')  
   parser.add_argument('start',  
                       help='start timestamp (inclusive, in format "YYYY-MM-DD" or "YYYY-MM-DD hh:mm:ss")')  
   parser.add_argument('end',  
                       help='end timestamp (exclusive, in format "YYYY-MM-DD" or "YYYY-MM-DD hh:mm:ss")')  
   args = parser.parse_args()  
  
   main(args.start, args.end)
```

Was this page helpful?

* Monitor the Dremio Console
* Monitor with Dremio APIs and SQL

<div style="page-break-after: always;"></div>

# Manage Projects | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/projects/

On this page

A project isolates the compute, data, and other resources a team needs for data analysis. An organization may contain multiple projects. Your first project is created during the sign-up process.

Each project in Dremio has its own storage. This is used to store metadata and Reflections and serves as the default storage location for the project's Open Catalog. You can choose between two storage options:

* Dremio-managed storage – No setup or configuration required. Usage is priced per TB, billed monthly.
* Your own storage – Use your own Amazon S3 storage. However, this requires you to manage this infrastructure.

For details on pricing, see [How Storage Usage Is Calculated](/dremio-cloud/admin/subscription/usage#how-storage-usage-is-calculated).

Each project in your organization contains a preview engine. Each new project has a preview engine. The preview engine, by default, will scale down after 1 hour without a query. As the name suggests, it provides previews of queries and datasets. Unlike other engines, the preview engine cannot be disabled, ensuring that many core Dremio functions that require an engine can always run.

## View All Projects

To view all projects:

1. In the Dremio console, hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Organization settings**.
2. Select **Projects** in the organization settings sidebar.

The Projects page displays the status of all projects in your organization. Possible statuses include:

* Creating
* Active
* Inactive
* Deactivating
* Activating
* Archiving
* Archived
* Restoring

## Grant Access to a Project

New projects are private by default. In the projects page, users can see only the projects for which they have USAGE or OWNERSHIP [privileges](/dremio-cloud/security/privileges). The projects page is empty for users without USAGE or OWNERSHIP privileges on any projects. The projects dropdown list shares this behavior.

Similarly, the [Projects API](/dremio-cloud/api/projects) returns an HTTP 403 Forbidden error for requests from users who do not have USAGE or OWNERSHIP privileges on the project. Also, users must have USAGE or OWNERSHIP privileges on a project before they can make API requests or run SQL queries on any objects in the project, even if they have object-level privileges on sources, folders, or other objects in the project.

To allow users to access a project, use the [`GRANT TO ROLE`](/dremio-cloud/sql/commands/grant-to-role) or [`GRANT TO USER`](/dremio-cloud/sql/commands/grant-to-user) SQL command or the [Grants API](/dremio-cloud/api/catalog/grants) to grant them the USAGE privilege on the project. For users who do not own the project, USAGE is the minimum privilege required to perform any operation on the project and the objects the project contains. For example, if you are using `GRANT TO USER`, you can run `GRANT USAGE ON PROJECT TO USER <username>`.

## Obtain the ID of a Project

A BI client application might require the ID of a project as part of the information for creating a connection to Dremio. You can obtain the ID from the General Information page of a project's settings.

To obtain a project ID:

1. In the Dremio console, hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Project settings**.
2. Select **General Information** in the project settings sidebar.
3. Copy the value in the **Project ID** field.

## Set the Default Project

When your data consumers connect to Dremio from BI tools, they must connect to the projects where their datasets reside. They can either connect to the default project or select a different project.

If an organization administrator does not set this value, Dremio automatically sets the default project to the oldest project in your organization.

You can change the default project at any time.

note

Data consumers who do not have access to the default project must select an alternative project ID when connecting to Dremio from their BI tools.

To specify the default project for your organization:

1. Hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Organization settings**.
2. Select **General Information** in the organization settings sidebar.
3. In the **Default Project** field, select the project that you want data consumers to connect to by default through their BI tools.
4. Click **Save**.

## Create a Project

If you're planning on using your own bucket, you will need create a role for Dremio granting access, this must be done prior to creating a project, see [Bring Your Own Project Store](/dremio-cloud/admin/projects/your-own-project-storage) for instructions. To avoid having to do this simply use Dremio-managed storage.

To add a project:

1. In the Dremio console, hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Organization settings**.
2. Select **Projects** option in the organization settings sidebar.
3. In the top-right corner of the Projects page, click **Create**.
4. For **Project name**, specify a name that is unique within the organization.
5. For **Region**, select the AWS Region where you wish the project to reside.
6. Select one of the two **Storage** options:

   * For **Dremio managed storage**, Dremio will create and manage object storage for your use.
   * For **your own storage**, you will need to provide Dremio the bucket URI and Role ARN previously created.

## Activate a Project

Dremio automatically deactivates any project that has not been accessed in the last 15 days. Dremio sends a courtesy email to project owners three days prior to deactivation. Inactive projects are displayed in the project selector in the side navigation bar and on the Projects page. An inactive project will be activated automatically when any user tries to access it via the Dremio console, an ODBC or JDBC connection, or an API call.

note

Inactive projects do not consume any compute resources.

You can activate an inactive project on the Projects page, or by clicking the project in the project selector. It takes a few minutes to activate a project.

To activate a project from the Projects page:

1. Hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Organization settings**.
2. Select **Projects** in the organization settings sidebar.
3. Click the ellipsis menu to the far right of the inactive project, and then click **Activate Project**.

The project status will change to *Activating* while the project is activated. You can access the project after the status changes to *Active*.

## Archive a Project

Users with OWNERSHIP privileges or users assigned to the ADMIN role can archive a project. Archived projects are displayed only on the Projects page.

note

Archived projects do not consume any compute resources.

To archive a project:

1. In the Dremio console, hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Organization settings**.
2. Select **Projects** in the organization settings sidebar.
3. Click the ellipsis menu to the far right of an active or inactive project, and then click **Archive Project**.

The project status will change to *Archiving* while the project is archived. When archiving is complete, the status changes to *Archived*.

## Restore an Archived Project

An archived project will not be restored automatically if a user tries to access it and can only be restored manually by a user with OWNERSHIP privileges on the project or users assigned to the ADMIN role. It takes a few minutes to restore an archived project.

To restore an archived project:

1. In the Dremio console, hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Organization settings**.
2. Select **Projects** in the organization settings sidebar.
3. Click the ellipsis menu to the far right of an archived project and select **Restore Project**.

The project status will change to *Restoring* while the project is restored. You can access the project after the status changes to *Active*.

## Delete a Project

Default projects cannot be deleted. If you want to delete the default project, you must first set another project as the default. See Set the Default Project.

To delete a project:

1. In the Dremio console, hover over ![This is the Dremio Settings icon.](/images/icons/settings.png "This is the Dremio Settings icon.") in the side navigation bar and select **Organization Settings**.
2. Select **Projects** in the organization settings sidebar.
3. Click the ellipsis menu to the far right and select **Delete Project**.
4. Confirm that you want to delete the project.

Was this page helpful?

* View All Projects
* Grant Access to a Project
* Obtain the ID of a Project
* Set the Default Project
* Create a Project
* Activate a Project
* Archive a Project
* Restore an Archived Project
* Delete a Project

<div style="page-break-after: always;"></div>

# Audit Logs | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/monitor/logs

On this page

The creation and modification of Dremio resources are tracked and traceable via the [`sys.project.history.events`](/dremio-cloud/sql/system-tables/events-historical) table. Audit logging is enabled by default and available to users with administrative permissions on the project.

An event can take up to three hours to propagate to the system table. There is currently no maximum retention policy for audit events.

note

This is a subset of the events that Dremio supports.

## Organization Events

Dremio supports audit logging for the following organization event types and actions. The [`sys.project.history.events`](/dremio-cloud/sql/system-tables/events-historical) table contains these events in the default project.

| Event Type | Actions | Description |
| --- | --- | --- |
| BILLING\_ACCOUNT | BILLING\_ACCOUNT\_ADD\_PROJECT | Dremio added a new project to the billing account during project creation. |
| BILLING\_ACCOUNT | BILLING\_ACCOUNT\_CREATE | A user created a billing account. |
| BILLING\_ACCOUNT | BILLING\_ACCOUNT\_REMOVE\_PROJECT | Dremio removed a project from the billing account during project deletion. |
| BILLING\_ACCOUNT | BILLING\_ACCOUNT\_UPDATE | A user modified the billing account, such as the notification email address. |
| BILLING\_TRANSACTION | TRANSACTION\_CHARGE | Dremio recorded Dremio Consumption Unit (DCU) usage charges for the period. |
| BILLING\_TRANSACTION | TRANSACTION\_CREDIT\_LOAD | Dremio loaded DCU credits into the billing account. |
| CATALOG | CREATE | A user created a new Open Catalog. Catalog creation is included with project creation. |
| CATALOG | DELETE | A user deleted an Open Catalog. Project deletion also deletes its primary Open Catalog. |
| CATALOG | UPDATE | A user updated an Open Catalog configuration. |
| CLOUD | CREATE\_STARTED CREATE\_COMPLETED | A user created a cloud. Clouds provide resources for running engines and storing metadata in a project. |
| CLOUD | DELETE\_STARTED DELETE\_COMPLETED | A user deleted a cloud. |
| CLOUD | UPDATE | A user updated a cloud. |
| CONNECTION | FORCE\_LOGOUT | A user changed their password or deactivated another user, ending all of that user's sessions. |
| CONNECTION | LOGIN | A user logged in. |
| CONNECTION | LOGOUT | A user logged out. |
| EDITION | DOWNGRADE | A user downgraded the billing edition in the Dremio organization. |
| EDITION | UPGRADE | A user upgraded the billing edition in the Dremio organization. |
| IDENTITY\_PROVIDER | CREATE | A user configured a new OpenID Connect (OIDC) identity provider integration. |
| IDENTITY\_PROVIDER | DELETE | A user deleted an OIDC identity provider. |
| IDENTITY\_PROVIDER | UPDATE | A user updated an OIDC identity provider configuration. |
| MODEL\_PROVIDER\_CONFIG | CREATE | A user created a new model provider in the Dremio organization. |
| MODEL\_PROVIDER\_CONFIG | UPDATE | A user updated a model provider in the Dremio organization. |
| MODEL\_PROVIDER\_CONFIG | DELETE | A user deleted a model provider in the Dremio organization. |
| MODEL\_PROVIDER\_CONFIG | SET\_DEFAULT | A user set a new default model provider in the Dremio organization. |
| ORGANIZATION | CREATE\_STARTED CREATE\_COMPLETED | A user created the Dremio organization. |
| ORGANIZATION | DELETE\_STARTED DELETE\_COMPLETED | A user closed and deleted the Dremio organization. |
| ORGANIZATION | UPDATE | A user updated the Dremio Cloud organization. |
| PERSONAL\_ACCESS\_TOKEN | CREATE | A user created a new personal access token in their account. |
| PERSONAL\_ACCESS\_TOKEN | DELETE | A user deleted a personal access token. |
| PROJECT | CREATE\_STARTED CREATE\_COMPLETED | A user created a project in the Dremio organization. |
| PROJECT | DELETE\_STARTED DELETE\_COMPLETED | A user deleted a project. |
| PROJECT | HIBERNATE\_STARTED HIBERNATE\_COMPLETED | A user archived a project. |
| PROJECT | UNHIBERNATE\_STARTED UNHIBERNATE\_COMPLETED | A user activated an archived project. |
| PROJECT | UPDATE | A user updated the configuration of a project. |
| ROLE | CREATE | A user created a custom role. |
| ROLE | DELETE | A user deleted a role. |
| ROLE | MEMBERS\_ADDED | A user added users or roles as members of a role. |
| ROLE | MEMBERS\_REMOVED | A user removed users or roles as members of a role. |
| ROLE | UPDATE | A user updated the metadata of a custom role, such as the description. |
| USER\_ACCOUNT | CREATE | A user added a user account. |
| USER\_ACCOUNT | DELETE | A user deleted a user account. |
| USER\_ACCOUNT | PASSWORD\_CHANGE | A user updated their account password. |
| USER\_ACCOUNT | UPDATE | A user updated user account metadata. |

## Project Events

| Event Type | Actions | Description |
| --- | --- | --- |
| AI\_AGENT | REQUEST   RESPONSE | A user sent a request to the AI Agent and received a response. |
| ENGINE | CREATE\_STARTED CREATE\_COMPLETED | A user created an engine. |
| ENGINE | DELETE\_STARTED DELETE\_COMPLETED | A user deleted an engine. |
| ENGINE | DISABLE\_STARTED DISABLE\_COMPLETED | A user disabled an engine. |
| ENGINE | ENABLE\_STARTED ENABLE\_COMPLETED | A user enabled an engine. |
| ENGINE | UPDATE\_STARTED UPDATE\_COMPLETED | A user updated an engine configuration. |
| ENGINE\_SCALING | SCALE\_DOWN\_STARTED SCALE\_DOWN\_COMPLETED | Dremio scaled down an engine by stopping one or more running replicas. |
| ENGINE\_SCALING | SCALE\_UP\_STARTED SCALE\_UP\_COMPLETED | Dremio scaled up an engine by starting one or more additional replicas. |
| LABEL | UPDATE | A user created a label on a dataset, source, or other object. |
| PIPE | CREATE | A user created an autoingest pipe for Apache Iceberg. |
| PIPE | DELETE | A user dropped an autoingest pipe. |
| PIPE | UPDATE | A user updated the configuration of an existing autoingest pipe. |
| PRIVILEGE | DELETE | A user deleted a privilege from a user or role. |
| PRIVILEGE | UPDATE | A user granted a privilege to a user or role. |
| REFLECTION | CREATE | A user created a new raw or aggregate Reflection. |
| REFLECTION | DELETE | A user deleted a Reflection. |
| REFLECTION | UPDATE | A user updated the content or configuration of a Reflection. |
| REPLICA | CREATE\_STARTED CREATE\_COMPLETED | Dremio started a replica during an ENGINE\_SCALING scale-up event. |
| REPLICA | DELETE\_STARTED DELETE\_COMPLETED | Dremio stopped a replica during an ENGINE\_SCALING scale-down event. |
| ROUTING\_RULESET | UPDATE | A user modified an engine routing rule. |
| SUPPORT\_SETTING | RESET | A user reset an advanced configuration or diagnostic setting. |
| SUPPORT\_SETTING | SET | A user set an advanced configuration or diagnostic setting. |
| UDF | CREATE | A user created a user-defined function. |
| UDF | DELETE | A user deleted a user-defined function. |
| UDF | UPDATE | A user modified the SQL definition of a user-defined function. |
| WIKI | EDIT | A user created or updated a wiki. |

## Open Catalog Events

These events appear in the [`sys.project.history.events`](/dremio-cloud/sql/system-tables/events-historical) table of the project where the catalog is designated as the primary catalog.

| Event Type | Actions | Description |
| --- | --- | --- |
| FOLDER | CREATE | A user created a folder in the catalog. |
| FOLDER | DELETE | A user deleted a folder in the catalog. |
| TABLE | CREATE | A user created a table in the catalog. |
| TABLE | DELETE | A user deleted a table in the catalog. |
| TABLE | READ | A user read table information or data from the catalog. |
| TABLE | REGISTER | A user registered a new table in the catalog. |
| TABLE | UPDATE | A user updated a table definition in the catalog. |
| VIEW | CREATE | A user created a view in the catalog. |
| VIEW | DELETE | A user deleted a view in the catalog. |
| VIEW | READ | A user read a view in the catalog. |
| VIEW | UPDATE | A user updated a view definition in the catalog. |

## Source Events

These events appear in the [`sys.project.history.events`](/dremio-cloud/sql/system-tables/events-historical) table for any source in the project.

| Event Type | Actions | Description |
| --- | --- | --- |
| SOURCE | CREATE | A user created a data source. |
| SOURCE | DELETE | A user deleted a source connection. Any tables from the source were removed. |
| SOURCE | UPDATE | A user updated a source configuration. |
| FOLDER | CREATE | A user created a folder. |
| FOLDER | DELETE | A user deleted a folder. |
| TABLE | CREATE | A user created a non-catalog table. |
| TABLE | DELETE | A user deleted a non-catalog table. |
| TABLE | UPDATE | A user updated a table, or Dremio performed a metadata refresh on a non-Parquet table. |

Was this page helpful?

* Organization Events
* Project Events
* Open Catalog Events
* Source Events

<div style="page-break-after: always;"></div>

# Optimize Performance | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/performance/

Dremio uses a variety of tools to help you autonomously optimize your lakehouse. These tools apply at four stages: (1) source files, (2) intermediate transformations, (3) final or production transformations, and (4) client queries. Dremio also offers tools that allow you to manually fine-tune performance. Both approaches can coexist, enabling Dremio to manage most optimizations automatically while still giving you the flexibility to take direct action when desired.

For details on how Dremio autonomously manages your tables, see [Automatic Optimization](/dremio-cloud/manage-govern/optimization), which focuses on Iceberg table management.

This section focuses instead on accelerating views and SQL queries, including those from clients such as AI agents and BI dashboards. The principal method for this acceration is Dremio's patterned materialization and query-rewriting, known as Reflections.

* [Autonomous Reflections](/dremio-cloud/admin/performance/autonomous-reflections) – Learn how Dremio automatically learns your query patterns and manages Reflections to optimize performance accordingly. This capability is available for Iceberg tables, UniForm tables, Parquet datasets, and any views built on these datasets.
* [Manual Reflections](/dremio-cloud/admin/performance/manual-reflections) – Use this option primarily for data formats not supported by Autonomous Reflections. Learn how to define your own Reflections and the best practices for using and managing them.
* [Results Cache](/dremio-cloud/admin/performance/results-cache) – Understand how Dremio caches the results of queries from AI agents and BI dashboards.

Was this page helpful?

<div style="page-break-after: always;"></div>

# Jobs | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/monitor/jobs/

On this page

All jobs run in Dremio are listed on a separate page, showing the job ID, type, status, and other attributes.

To navigate to the Jobs page, click ![This is the icon that represents the Jobs page.](/images/cloud/jobs-page-icon.png "Icon represents the Jobs page.") in the side navigation bar.

## Search Filters and Columns

By default, the Jobs page lists the jobs run within the last 30 days and the jobs are filtered by **UI, External Tools** job types. To change these defaults for your account, you can filter on values and manage columns directly on the Jobs page, as shown in this image:

![This is a screenshot showing the main components of the Jobs page.](/images/cloud/jobs-map.png "This is a screenshot showing the main components of the Jobs page.")

a. **Search Jobs** by typing the username or job ID.

b. **Start Time** allows you to pick the date and time at which the job began.

c. **Status** represents one or more job states. For descriptions, see [Job States and Statuses](.#job-states-and-statuses).

d. **Type** includes Accelerator, Downloads, External Tools, Internal, and UI. For descriptions, see Job Properties.

e. **User** can be searched by typing the username or checking the box next to the username in the dropdown.

f. **Manage Columns** by checking the boxes next to additional columns that you want to see in the Jobs list. The grayed out checkboxes show the columns that are required by default. You can also rearrange the column order by clicking directly on a column to drag and drop.

## Job Properties

Each job has the following properties, which can appear as columns in the list of jobs on the Jobs page or as details on the Job Overview page:

| Property | Description |
| --- | --- |
| Accelerated | A purple lightning bolt in a row indicates that the job ran a query that was accelerated by one or more Reflections. |
| Attribute | Represents at least one of the following query types:  * **UI** - queries issued from the SQL Runner in the Dremio console. * **External Tools** - queries from client applications, such as Microsoft Power BI, Superset, Tableau, other third-party client applications, and custom applications. * **Accelerator** - queries related to creating, maintaining, and removing Reflections. * **Internal** - queries that Dremio submits for internal operations. * **Downloads** - queries used to download datasets. * **AI** – queries issued from the Dremio AI Agent. |
| CPU Used | Provides statistics about the actual cost of the query operations in terms of CPU processing. |
| Dataset | The queried dataset, if one was queried. Hover over the dataset to see a metadata card appear with details about the dataset. For more information, see [Discover Data](/dremio-cloud/explore-analyze/discover). |
| Duration | The length of time (in seconds) that a job required from start to completion. |
| Engine | The engine used to run the query. |
| Input | The number of bytes and the number of rows considered for the job. |
| Job ID | A universally unique identifier. |
| Output | The number of bytes and the number of rows resulted as output from the job. |
| Planner Cost Estimate | A cost estimate calculated by Dremio based on an evaluation of the resources that to be used in the execution of a query. The number is not in units, and is intended to give a an idea of the cost of executing a query relative to the costs of executing other queries. Values are derived by adding weighted estimates of required I/O, memory, and CPU load. In reported values, K = thousand, M = million, B = billion, and T = trillion. For example, a value of 12,543,765,321 is reported as 12.5B. |
| Planning Time | The length of time (in seconds) in which the query optimizer planned the execution of the query. |
| Rows Returned | Number of output records. |
| Rows Scanned | Number of input records. |
| SQL | The SQL query that was submitted for the job. |
| Start Time | The date and time which the job began. |
| Status | Represents one or more job states. For descriptions, see Job States and Statuses. |
| Total Memory | Provides statistics about the actual cost of the query operations in terms of memory. |
| User | Username of the user who ran the query and initiated the job. |
| Wait on Client | The length of time (in seconds) that is waiting on the client. |

## Job States and Statuses

Each job passes through a sequence of states until it is complete, though the sequence can be interrupted if a query is canceled or if there is an error during a state. In this diagram, the states that a job passes through are in white, and the possible end states are in dark gray.

![](/assets/images/job-states-d8a1b49d0b4cef93a610cd185648e268.png)

This table lists the statuses that the UI lets you filter on and shows how they map to the states:

| Icon | Status | State | Description |
| --- | --- | --- | --- |
|  | Setup | Pending | Represents a state where the query is waiting to be scheduled on the query pool. |
| Metadata Retrieval | Represents a state where metadata schema is retrieved and the SQL command is parsed. |
| Planning | Represents a state where the following are done:  * Physical and logical planning * Reflection matching * Partition metadata retrieval * Mapping the query to an engine-based workload management rule * Pick the engine associated with the query to run the query. |
|  | Engine Start | Engine Start | Represents a state where the engine starts if it has stopped. If the engine is stopped, it takes time to restart for the executors to be active. If the engine is already started, then this state does not have a duration. |
|  | Queued | Queued | Represents a state where a job is queued. Each engine has a limit of concurrent queries. If the queries in progress exceed the concurrency limit, the query should wait until the jobs in progress complete. |
|  | Running | Execution Planning | Represents a state where executor nodes are selected from the chosen engine to run the query, and work is distributed to each executor. |
| Running | Represents a state where executor nodes execute and complete the fragments assigned to them. Typically, most queries spend more time in this state. |
| Starting | Represents a state where the query is starting up. |
|  | Canceled | Canceled | Represents a terminal state that indicates that the query is canceled by the user or an intervention in the system. |
|  | Completed | Completed | Represents a terminal state that indicates that the query is successfully completed. |
|  | Failed | Failed | Represents a terminal state that indicates that the query has failed due to an error. |

## View Job Details

You can view the details of a specific job by viewing the Job Overview, SQL, Visual Profile, and Raw Profile pages.

To navigate to the job details:

1. Click ![This is the icon that represents the Jobs page.](/images/cloud/jobs-page-icon.png "Icon represents the Jobs page.") in the side navigation bar.
2. On the Jobs page, click a job that you would like to see the job overview for.
3. The Job Overview page then replaces the list of jobs.

### Explain SQL

Use the **Explain SQL** option in the SQL Runner to analyze and optimize your SQL queries with assistance from the AI Agent. In the SQL Runner, highlight the SQL you want to review, right-click, and select **Explain SQL**. This prompts the AI Agent to examine the query, datasets, and underlying architecture to identify potential optimizations. The AI Agent uses Dremio’s SQL Parser—the same logic used during query execution—to identify referenced tables, schemas, and relationships. Based on this analysis, the Agent provides insights and recommendations to improve query performance and structure. You can continue interacting with the AI Agent to refine the analysis and iterate on the SQL. The AI Agent applies SQL best practices when suggesting improvements and may execute revised queries to validate quality before presenting recommendations.

### Explain Job

Use the **Explain Job** option on the Job Details page to analyze job performance and identify opportunities for optimization. From the Job Details page, click **Explain Job** to prompt the AI Agent to review the job’s query profile, planning, and execution details to compare with the AI Agents’s internal understanding of optimal performance characteristics. The AI Agent generates a detailed analysis that highlights key performance metrics such as data skew, memory usage, threading efficiency, and network utilization. Based on this assessment, it recommends potential optimizations to improve performance and resource utilization. You can continue the conversation with the AI Agent to explore the job in greater depth or reference additional job IDs to extend the investigation and compare results.

### Job Overview

You can view the details of a specific job on the Job Overview page.

To navigate to a job overview:

1. Click ![This is the icon that represents the Jobs page.](/images/cloud/jobs-page-icon.png "Icon represents the Jobs page.") in the side navigation bar.
2. On the Jobs page, click a job that you would like to see the job overview for. The Job Overview page then replaces the list of jobs.

The main components of the Job Overview page are numbered below:

![This is a screenshot showing the main components of the Job Overview page.](/images/cloud/job-overview-page-cloud.png "This is a screenshot showing the main components of the Job Overview page.")

#### 1. Summary

Each job is summarized.

#### 2. Total Execution Time

The total execution time is the length of time for the total execution and the job state durations in the order they occur. Only the duration of the Engine Start state is in minutes and seconds. If the engine is stopped, it takes time to restart for the executors to be active. If the engine is already started, then Engine Start duration does not have a value. For descriptions, see Job States and Statuses.

#### 3. Download Profile

To download the query profile, click the **Download Profile** button in the bottom-left corner of the Job Overview page. The profile will help you see more granular details about the job.

The profile downloads as a **ZIP** file. When you extract the **ZIP** file, you will see the following JSON files:

* profile\_attempt\_0.json: This file helps with troubleshooting out of memory and wrong results issues. Note that the start and end time of the query is provided in EPOCH format. See the [Epoch Converter](https://www.epochconverter.com) utility for converting query time.
* header.json: This file provides the full list of Dremio coordinators and executors, data sets, and sources.
  This information is useful when you are using REST calls.

#### 4. Submitted SQL

The SQL query for the selected job.

#### 5. Queried Datasets

The datasets queried for the selected job. These can be views or tables.

#### 6. Scans

Scan details include the source type, scan thread count, IO wait time (in milliseconds), and the number of rows scanned.

#### 7. Acceleration

Only if the job was accelerated, the Acceleration section appears and Reflections data is provided. See [Optimize Performance](/dremio-cloud/admin/performance/) for more information.

#### 8. Results

To see the job results, click the **Open Results** link in the top-right corner of the Job Overview page. As long as the engine that ran the job is up, the **Open Results** link is visible in the UI. It disappears when the engine that ran the job shuts down and is only visible for the jobs that are run through the UI.

### Job SQL

Next to the Job Overview page is a tab for the SQL page, which shows the Submitted SQL and Dataset Graph.

You can view the SQL statement that was used for the selected job. Although the SQL statement is in read-only mode on the SQL Details page, the statement can be copied from the page and pasted into the SQL editor.

A dataset graph only appears if there is a queried dataset for the selected job. The dataset graph is a visual representation of the datasets used in the SQL statement.

## Related Topics

* [Profiles](/dremio-cloud/admin/monitor/jobs/profiles) – See the visual profiles and raw profiles of jobs.

Was this page helpful?

* Search Filters and Columns
* Job Properties
* Job States and Statuses
* View Job Details
  + Explain SQL
  + Explain Job
  + Job Overview
  + Job SQL
* Related Topics

<div style="page-break-after: always;"></div>

# Manage Your Subscription | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/subscription/

On this page

Dremio offers multiple payment options for users to upgrade their organization after conclusion of the free trial:

* Pay-as-you-go (PAYG): Provide credit card details via the upgrade steps in the Dremio console.
* Commit-based offerings: Prepaid contracts for your organization's usage. Dremio invoices you directly, and a variety of payment options are available. Please contact [Dremio Sales](https://www.dremio.com/contact/) for more details.
* AWS Marketplace: A commit-based contract paid with AWS credits. Check out the [Dremio Cloud AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-pnlijtzyoyjok) listing on the AWS Marketplace. Once ready to proceed, contact [Dremio Sales](https://www.dremio.com/contact/) for more details.

Note that your organization can be moved to a commit-based contract after upgrading to PAYG.

## Upgrade

At any point during your free trial of Dremio, an organization can be upgraded by entering your credit card details. If the free trial concludes, your organization will become partially inaccessible for 30 days. During this time, you can still log in to upgrade your account, but if you do not upgrade your account before then, your organization and all of its contents may be deleted.

## Pay-as-you-go Billing Cycles

Your billing cycle starts from the day of your organization's upgrade and ends one month later. At the conclusion of the billing period, we will immediately attempt to charge your card for the outstanding balance.

If for any reason payment fails (or is only partially successful), we will attempt the charge again. If these subsequent attempts fail, your organization will become partially inaccessible. You can still log in but only to update your payment method. If a new payment method is not provided before the end of this billing period, your organization and all of its contents may be deleted.

## Organizations

A Dremio organization can have one or more projects. Usage across projects is aggregated for billing purposes, meaning that when the PAYG bill is paid for an organization, the balance is paid for all projects. Only users who are members of the ADMIN role within the organization can manage billing details within the Dremio console.

## Find Your Organization ID

The ID of your organization can be helpful during communication with Dremio Sales or Support. To find your organization's ID:

1. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and select **Organization settings** to open the Organization settings page.
2. On the General Information tab, copy your organization's ID.

## Delete Your Organization

Please contact Dremio's Support team if you would like to have your organization deleted.

Was this page helpful?

* Upgrade
* Pay-as-you-go Billing Cycles
* Organizations
* Find Your Organization ID
* Delete Your Organization

<div style="page-break-after: always;"></div>

# Configure Model Providers | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/model-providers

On this page

You configure model providers for your organization for AI features when deploying Dremio. After you configure at least one model provider, you must set a default model provider and optionally set an allowlist of available models. Dremio uses this default provider for all Dremio's AI Agent interactions, whereas the allowlist models can be used by anyone writing AI functions. By default CALL MODEL is granted to all users for all new model providers so if the default changes users can continue to use the AI Agent without interruption.

## Dremio-Provided LLM

Dremio provides all organizations with an out-of-the-box model provider so that all users can begin engaging with the AI Agent and AI functions without any other configuration required. Once you have added your own model provider and set it as the new default, the Dremio-Provided LLM will no longer be used. If you delete all other model providers, then the Dremio-Provided LLM will revert to the organization's default model provider. This model provider cannot be deleted.

## Supported Model Providers

Dremio supports configuration of the following model providers and models. Dremio recommends using enterprise-grade reasoning models for the best performance and experience.

| Category | Models | Connection Method(s) |
| --- | --- | --- |
| **OpenAI** | * gpt-5-2025-08-07 * gpt-5-mini-2025-08-07 * gpt-5-nano-2025-08-07 * gpt-4.1-2025-04-14 * gpt-4o-2024-11-20 * gpt-4-turbo-2024-04-09 * gpt-4.1-mini-2025-04-14 * o3-mini-2025-01-31 * o4-mini-2025-04-16 * o3-2025-04-16 | * Access Key |
| **Anthropic** | * claude-sonnet-4-5-20250929 * claude-opus-4-1-20250805 * claude-opus-4-20250514 * claude-sonnet-4-20250514 | * Access Key |
| **Google Gemini** | * gemini-2.5-pro | * Access Key |
| **AWS Bedrock** | * specify Model ID(s) * [AWS Bedrock Supported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) | * Access Key * IAM Role |
| **Azure OpenAI** | * specify Deployment Name(s) * [Azure Supported Models](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cstandard-chat-completions%2Cglobal-standard&pivots=azure-openai#azure-openai-in-azure-ai-foundry-models) | Combination of  1. Resource Name 2. Directory ID 3. Application ID 4. Client Secret Value |

## Rate Limiting and Quotas

### AWS Bedrock Rate Limits

When using AWS Bedrock model providers, you may encounter rate limiting errors such as "429 Too Many Tokens (Rate Limit Exceeded)". This is particularly common with new AWS accounts that start with lower or fixed quotas.

If you experience rate limiting issues, you can contact AWS Support and request a quota increase by providing:

* Quota name
* Model ID
* AWS region
* Use case description
* Projected token and request usage

For more information about AWS Bedrock quotas and limits, see the [AWS Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html).

## Default Model Provider

To delete the model provider, you must assign a new default unless you are deleting the last available model provider that you have configured. To update the default model provider to a new one, you must have MODIFY privilege on both the current default and the new proposed default model provider.

## Add Model Provider

To add a model provider in the Dremio console:

1. Click ![This is the Settings icon.](/images/green-settings-icon.png "The Settings icon.") in the side navigation bar to go to the Settings page.
2. Select **Organization Settings**.
3. Select the **AI Configuration** setting.
4. Click **Add model provider**.

Was this page helpful?

* Dremio-Provided LLM
* Supported Model Providers
* Rate Limiting and Quotas
  + AWS Bedrock Rate Limits
* Default Model Provider
* Add Model Provider

<div style="page-break-after: always;"></div>

# External Engines | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/external-engines

On this page

Dremio's Open Catalog is built on Apache Polaris, providing a standards-based, open approach to data catalog management. At its core is the Iceberg REST interface, which enables seamless integration with any query engine that supports the Apache Iceberg REST catalog specification. This open architecture means you can connect industry-standard engines such as Apache Spark, Trino, and Apache Flink directly to Dremio.

| Engine | Best For | Key Features |
| --- | --- | --- |
| [Apache Spark](https://spark.apache.org/) | Data engineering, ETL | Token exchange, nested folders, views |
| [Trino](https://trino.io/) | Interactive analytics | Fast queries, BI workloads |
| [Apache Flink](https://flink.apache.org/) | Real-time streaming | Event-driven, continuous pipelines |

By leveraging the Iceberg REST standard, the Open Catalog acts as a universal catalog layer that query engines can communicate with using a common language. This allows organizations to build flexible data architectures where multiple engines can work together, each accessing and managing the same Iceberg tables through Dremio's centralized catalog.

## Apache Spark

Apache Spark is a unified analytics engine for large-scale data processing, widely used for ETL, batch processing, and data engineering workflows.

### Prerequisites

This example uses Spark 3.5.3 with Iceberg 1.9.1. For other versions, ensure compatibility between Spark, Scala, and Iceberg runtime versions. Additional prerequisites include:

* The following JAR files downloaded to your local directory:
  + `authmgr-oauth2-runtime-0.0.5.jar` from [Dremio Auth Manager releases](https://github.com/dremio/iceberg-auth-manager/releases). This open-source library handles token exchange, automatically converting your personal access token (PAT) into an OAuth token for seamless authentication. For more details about Dremio Auth Manager's capabilities and configuration options, see [Introducing Dremio Auth Manager for Apache Iceberg](https://www.dremio.com/blog/introducing-dremio-auth-manager-for-apache-iceberg/).
  + `iceberg-spark-runtime-3.5_2.12-1.9.1.jar` (from [Apache Iceberg releases](https://iceberg.apache.org/releases/))
  + `iceberg-aws-bundle-1.9.1.jar` (from [Apache Iceberg releases](https://iceberg.apache.org/releases/))
* Docker installed and running.
* Your Dremio catalog name – The default catalog in each project has the same name as the project.
* If authenticating with a PAT, you must generate a token. See [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token/) for step-by-step instructions.
* If authenticating with an identity provider (IDP), your IDP or other external token provider must be configured as a trusted OAuth [external token provider](/dremio-cloud/security/authentication/app-authentication/external-token) in Dremio.
* You must have an OAuth2 client registered in your IDP configured to issue tokens that Dremio accepts (matching audience and scopes) and with a client ID and client secret provided by your IDP.

### Authenticate with a PAT

You can authenticate your Apache Spark session with a Dremio personal access token using the following script. Replace `<personal_access_token>` with your Dremio personal access token and replace `<catalog_name>` with your catalog name.

In addition, you can adjust the volume mount paths to match where you've downloaded the JAR files and where you want your workspace directory. The example uses `$HOME/downloads` and `$HOME/workspace`.

Spark with PAT Authentication

```
#!/bin/bash  
export CATALOG_NAME="<catalog_name>"  
export DREMIO_PAT="<personal_access_token>"  
  
docker run -it \  
  -v $HOME/downloads:/opt/jars \  
  -v $HOME/workspace:/workspace \  
  apache/spark:3.5.3 \  
  /opt/spark/bin/spark-shell \  
  --jars /opt/jars/authmgr-oauth2-runtime-0.0.5.jar,/opt/jars/iceberg-spark-runtime-3.5_2.12-1.9.1.jar,/opt/jars/iceberg-aws-bundle-1.9.1.jar \  
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \  
  --conf spark.sql.catalog.polaris=org.apache.iceberg.spark.SparkCatalog \  
  --conf spark.sql.catalog.polaris.type=rest \  
  --conf spark.sql.catalog.polaris.cache-enabled=false \  
  --conf spark.sql.catalog.polaris.warehouse=$CATALOG_NAME \  
  --conf spark.sql.catalog.polaris.uri=https://catalog.dremio.cloud/api/iceberg \  
  --conf spark.sql.catalog.polaris.io-impl=org.apache.iceberg.aws.s3.S3FileIO \  
  --conf spark.sql.catalog.polaris.header.X-Iceberg-Access-Delegation=vended-credentials \  
  --conf spark.sql.catalog.polaris.rest.auth.type=com.dremio.iceberg.authmgr.oauth2.OAuth2Manager \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.token-endpoint=https://login.dremio.cloud/oauth/token \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.grant-type=token_exchange \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.client-id=dremio-catalog-cli \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.scope=dremio.all \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.token-exchange.subject-token="$DREMIO_PAT" \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.token-exchange.subject-token-type=urn:ietf:params:oauth:token-type:dremio:personal-access-token
```

note

In this configuration, `polaris` is the catalog identifier used within Spark. This identifier is mapped to your actual Dremio catalog via the `spark.sql.catalog.polaris.warehouse` property.

### Authenticate with an IDP

You can authenticate your Apache Spark session using an [external token provider](/dremio-cloud/security/authentication/app-authentication/external-token) that has been integrated with Dremio.

**Using this configuration:**

* Spark obtains a user-specific JWT from the external token provider.
* Spark connects to Dremio and [exchanges the JWT](/dremio-cloud/api/oauth-token) for an access token.
* Spark connects to the Open Catalog using the access token.

Using the following script, replace `<catalog_name>` with your catalog name, `<idp_url>` with the location of your external token provider, `<client_id>` and `<client_secret>` with the credentials issued by the external token provider.

In addition, you can adjust the volume mount paths to match where you've downloaded the JAR files and where you want your workspace directory. The example uses `$HOME/downloads` and `$HOME/workspace`.

Spark with IDP Authentication

```
#!/bin/bash  
export CATALOG_NAME="<catalog_name>"  
export IDP_URL="<idp_url>"  
export CLIENT_ID="<idp_client_id>"   
export CLIENT_SECRET="<idp_client_secret>"   
  
docker run -it \  
  -v $HOME/downloads:/opt/jars \  
  -v $HOME/workspace:/workspace \  
  apache/spark:3.5.3 \  
  /opt/spark/bin/spark-shell \  
  --jars /opt/jars/authmgr-oauth2-runtime-0.0.5.jar,/opt/jars/iceberg-spark-runtime-3.5_2.12-1.9.1.jar,/opt/jars/iceberg-aws-bundle-1.9.1.jar \  
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \  
  --conf spark.sql.catalog.polaris=org.apache.iceberg.spark.SparkCatalog \  
  --conf spark.sql.catalog.polaris.type=rest \  
  --conf spark.sql.catalog.polaris.cache-enabled=false \  
  --conf spark.sql.catalog.polaris.warehouse=$CATALOG_NAME \  
  --conf spark.sql.catalog.polaris.uri=https://catalog.dremio.cloud/api/iceberg \  
  --conf spark.sql.catalog.polaris.io-impl=org.apache.iceberg.aws.s3.S3FileIO \  
  --conf spark.sql.catalog.polaris.header.X-Iceberg-Access-Delegation=vended-credentials \  
  --conf spark.sql.catalog.polaris.rest.auth.type=com.dremio.iceberg.authmgr.oauth2.OAuth2Manager \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.issuer-url=$IDP_URL \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.grant-type=device_code \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.client-id=$CLIENT_ID \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.client-secret=$CLIENT_SECRET \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.scope=dremio.all \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.impersonation.enabled=true \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.impersonation.token-endpoint=https://login.dremio.cloud/oauth/token \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.impersonation.scope=dremio.all \  
  --conf spark.sql.catalog.polaris.rest.auth.oauth2.token-exchange.subject-token-type=urn:ietf:params:oauth:token-type:jwt
```

### Usage Examples

With these configurations, `polaris` is the catalog identifier used within Spark. This identifier is mapped to your actual Dremio catalog via the `spark.sql.catalog.polaris.warehouse` property. Once Spark is running and connected to your Dremio catalog:

List namespaces

```
spark.sql("SHOW NAMESPACES IN polaris").show()
```

Query a table

```
spark.sql("SELECT * FROM polaris.your_namespace.your_table LIMIT 10").show()
```

Create a table

```
spark.sql("""  
  CREATE TABLE polaris.your_namespace.new_table (  
    id INT,  
    name STRING  
  ) USING iceberg  
""")
```

## Trino

Trino is a distributed SQL query engine designed for fast analytic queries against data sources of all sizes. It excels at interactive SQL analysis, ad hoc queries, and joining data across multiple sources.

### Prerequisites

* Docker installed and running.
* A valid Dremio personal access token – See [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token/) for instructions to generate a personal access token.
* Your Dremio catalog name – The default catalog in each project has the same name as the project.

### Configuration

To connect Trino to Dremio using Docker, follow these steps:

1. Create a directory for Trino configuration and add a catalog configuration:

   ```
   mkdir -p ~/trino-config/catalog
   ```

   In `trino-config/catalog`, create a catalog configuration file named `polaris.properties` with the following values:

   Trino polaris.properties

   ```
   connector.name=iceberg  
   iceberg.catalog.type=rest  
   iceberg.rest-catalog.uri=https://catalog.dremio.cloud/api/iceberg  
   iceberg.rest-catalog.oauth2.token=<personal_access_token>  
     
   iceberg.rest-catalog.warehouse=<catalog_name>  
   iceberg.rest-catalog.security=OAUTH2  
     
   iceberg.rest-catalog.vended-credentials-enabled=true  
   fs.native-s3.enabled=true  
   s3.region=<region>
   ```

   Replace the following:

   * `<personal_access_token>` with your Dremio personal access token.
   * `<catalog_name>` with your catalog name.
   * `<region>` with the AWS region where your data is stored, such as `us-west-2`.

   note

   * In this configuration, `polaris` (from the filename `polaris.properties`) is the catalog identifier used in Trino queries. The `iceberg.rest-catalog.warehouse` property maps this identifier to your actual Dremio catalog.
   * In `oauth2.token`, you provide your Dremio personal access token directly. Dremio's catalog API accepts PATs as bearer tokens without requiring token exchange.
2. Pull and start the Trino container:

   ```
   docker run --name trino -d -p 8080:8080 trinodb/trino:latest
   ```
3. Verify that Trino is running:

   ```
   docker ps
   ```

   You can access the web UI at `http://localhost:8080` and log in as `admin`.
4. Restart Trino with the configuration:

   ```
   docker stop trino  
   docker rm trino  
     
   # Start with mounted configuration  
   docker run --name trino -d -p 8080:8080 -v ~/trino-config/catalog:/etc/trino/catalog trinodb/trino:latest  
     
   # Verify Trino is running  
   docker ps  
     
   # Check logs  
   docker logs trino -f
   ```
5. In another window, connect to the Trino CLI:

   ```
   docker exec -it trino trino --user admin
   ```

   You should see the Trino prompt:

   ```
   trino>
   ```
6. Verify the catalog connection:

   ```
   trino> show catalogs;
   ```

### Usage Examples

Once Trino is running and connected to your Dremio catalog:

List namespaces

```
trino> show schemas from polaris;
```

Query a table

```
trino> select * from polaris.your_namespace.your_table;
```

Create a table

```
trino> CREATE TABLE polaris.demo_namespace.test_table (  
  id INT,  
  name VARCHAR,  
  created_date DATE,  
  value DOUBLE  
);
```

### Limitations

* **Case sensitivity:** Namespace and table names must be in lowercase. Trino will not list or access tables in namespaces that begin with an uppercase character.
* **View compatibility:** Trino cannot read views created in Dremio due to SQL dialect incompatibility. Returns error: "Cannot read unsupported dialect 'DremioSQL'."

## Apache Flink

Apache Flink is a distributed stream processing framework designed for stateful computations over bounded and unbounded data streams, enabling real-time data pipelines and event-driven applications.

To connect Apache Flink to Dremio using Docker Compose, follow these steps:

### Prerequisites

You'll need to download the required JAR files and organize them in a project directory structure.

1. Create the project directory structure:

   ```
   mkdir -p flink-dremio/jars  
   cd flink-dremio
   ```
2. Download the required JARs into the `jars/` directory:

   * Iceberg Flink Runtime 1.20:

     ```
     wget -P jars/ https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-flink-runtime-1.20/1.9.1/iceberg-flink-runtime-1.20-1.9.1.jar
     ```
   * Iceberg AWS Bundle for vended credentials:

     ```
     wget -P jars/ https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/1.9.1/iceberg-aws-bundle-1.9.1.jar
     ```
   * Hadoop dependencies required by Flink:

     ```
     wget -P jars/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-shaded-hadoop-2-uber/2.8.3-10.0/flink-shaded-hadoop-2-uber-2.8.3-10.0.jar
     ```
3. Create the Dockerfile.

   Create a file named `Dockerfile` in the `flink-dremio` directory:

   Flink Dockerfile

   ```
   FROM flink:1.20-scala_2.12   
     
   # Copy all required JARs  
   COPY jars/*.jar /opt/flink/lib/
   ```
4. Create the `docker-compose.yml` file in the `flink-dremio` directory:

   Flink docker-compose.yml

   ```
   services:  
     flink-jobmanager:  
       build: .   
       ports:  
         - "8081:8081"  
       command: jobmanager  
       environment:  
         - |  
           FLINK_PROPERTIES=  
           jobmanager.rpc.address: flink-jobmanager  
           parallelism.default: 2          
         - AWS_REGION=us-west-2  
     
     flink-taskmanager:  
       build: .          
       depends_on:  
         - flink-jobmanager  
       command: taskmanager  
       scale: 1  
       environment:  
         - |  
           FLINK_PROPERTIES=  
           jobmanager.rpc.address: flink-jobmanager  
           taskmanager.numberOfTaskSlots: 4  
           parallelism.default: 2  
         - AWS_REGION=us-west-2
   ```
5. Build and start the Flink cluster:

   ```
   # Build and start the cluster  
   docker-compose build --no-cache  
   docker-compose up -d  
     
   # Verify the cluster is running  
   docker-compose ps  
     
   # Verify required JARs are present  
   docker-compose exec flink-jobmanager ls -la /opt/flink/lib/ | grep -E "(iceberg|hadoop)"
   ```

   You should see the JARs you downloaded in the previous step.
6. Connect to the Flink SQL client:

   ```
   docker-compose exec flink-jobmanager ./bin/sql-client.sh
   ```

   You can also access the Flink web UI at `http://localhost:8081` to monitor jobs.
7. Create the Dremio catalog connection in Flink:

   ```
   CREATE CATALOG polaris WITH (  
     'type' = 'iceberg',  
     'catalog-impl' = 'org.apache.iceberg.rest.RESTCatalog',  
     'uri' = 'https://catalog.dremio.cloud/api/iceberg',  
     'token' = '<personal_access_token>',   
     'warehouse' = '<catalog_name>',  
     'header.X-Iceberg-Access-Delegation' = 'vended-credentials',  
     'io-impl' = 'org.apache.iceberg.aws.s3.S3FileIO'  
   );
   ```

   Replace the following:

   * `<personal_access_token>` with your Dremio personal access token.
   * `<catalog_name>` with your catalog name.

   note

   * In this configuration, `polaris` is the catalog identifier used in Flink queries. The `CREATE CATALOG` command maps this identifier to your actual Dremio catalog.
   * In `token`, you provide your Dremio personal access token directly. Dremio's catalog API accepts PATs as bearer tokens without requiring token exchange.
8. Verify the catalog connection:

   ```
   Flink SQL> show catalogs;
   ```

### Usage Examples

Once Apache Flink is running and connected to your Dremio catalog:

List namespaces

```
Flink SQL> show databases in polaris;
```

Query a table

```
Flink SQL> select * from polaris.your_namespace.your_table;
```

Create a table

```
Flink SQL> CREATE TABLE polaris.demo_namespace.test_table (  
  id INT,  
  name STRING,  
  created_date DATE,  
  `value` DOUBLE  
);
```

### Limitations

* **Reserved keywords:** Column names that are reserved keywords, such as `value`, `timestamp`, and `date`, must be enclosed in backticks when creating or querying tables.

Was this page helpful?

* Apache Spark
  + Prerequisites
  + Authenticate with a PAT
  + Authenticate with an IDP
  + Usage Examples
* Trino
  + Prerequisites
  + Configuration
  + Usage Examples
  + Limitations
* Apache Flink
  + Prerequisites
  + Usage Examples
  + Limitations

<div style="page-break-after: always;"></div>

# Usage | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/subscription/usage

On this page

There are multiple forms of billable Dremio usage within an [organization](/dremio-cloud/admin/subscription/#organizations):

* Dremio Consumption Units (DCUs) represent the usage of Dremio engines. DCUs are only consumed when your engines are running.
* Large-language model (LLM) tokens are billed when you use Dremio's AI features via the Dremio-Provided LLM.
* Storage usage is billed in terabyte-months and only applies to projects that use Dremio-hosted storage. If your projects use an object storage bucket in your account with a cloud provider as the catalog store, storage fees do not apply.

## How DCUs are Calculated

The number of DCUs consumed by an engine depends on two factors:

* The size of the engine
* How long the engine and its replicas have been running for

DCU consumption for an engine is calculated as `(Total uptime for the engine and its replicas) * (DCU consumption rate for that engine size)`.

Uptime is measured in seconds and has a 60-second minimum.

The DCU consumption rate for each engine size supported in Dremio is listed in [Manage Engines](/dremio-cloud/admin/engines/).

### DCU Examples

#### Example 1

An organization has two Dremio Cloud engines defined: Engine A and Engine B, where Engine A is a 2XSmall engine, and Engine B is a Medium engine.

Suppose that between 8 a.m. and 9 a.m. one day:

* Engine A had 2 replicas running for 40 minutes each, so it accumulates a total of 80 minutes of engine uptime.
* Engine B had 5 replicas running for 50 minutes each, so it accumulates a total of 250 minutes of engine uptime.

The total usage for Engine A for this hour is `(80/60) * (16 DCUs/hour) = 21.33 DCUs`.

The total usage for Engine B for this hour is `(250/60) * (128 DCUs/hour) = 533.33 DCUs`.

#### Example 2

An organization has one Dremio Cloud engine defined: Engine A, where Engine A is a Medium engine.

Suppose that between 8 a.m. and 9 a.m. one day:

* Engine A had 1 replica running for the entire hour (60 minutes).
* Engine A needed to spin up an additional replica for 30 minutes to tackle a workload spike.

Engine A accumulated a total of 90 minutes of engine uptime, so the total usage for Engine A for this hour is `(90/60) * (128 DCUs/hour) = 192 DCUs`.

## How AI Usage Is Calculated

If you use the Dremio-Provided LLM, you pay directly for the cost of both the input and output tokens used. If you connect to another LLM via your own model provider, you are not currently charged for this usage.

### AI Examples

#### Example 1

Say that you use an external model provider as well as the Dremio-Provided LLM to use Dremio's AI features, resulting in a usage footprint like the below:

* External model provider 500K input tokens used.
* External model provider: 30K output tokens used.
* Dremio-Provided: 200K input tokens used.
* Dremio-Provided: 20K output tokens used.

You are not charged for using Dremio's AI features via an external model. Instead, you are only charged for the tokens consumed by the Dremio-Provided LLM:

* (200K input tokens)\*($1.25/1 million tokens) = $0.25
* (20K output tokens)\*($10.00/1 million tokens) = $0.20

In this scenario, you would be billed for $0.45 of AI feature usage.

In order to simplify the billing experience for AI features Dremio may explore the addition of an AI specific credit, similar to DCUs, in the future.

## How Storage Usage Is Calculated

Storage is calculated through the collection of periodic snapshots of the Dremio-hosted bucket. These snapshots throughout a billing period are averaged through the billing period to calculate a number of billable terabyte-months.

### Storage Usage Examples

#### Example 1

Suppose an organization has one Dremio project in a region where the price of a terabyte-month is $23.00, and that in a given month this project:

* Stores 1 terabyte of data for the entire 30 days of the billing period

Then the total amount charged for the storage would be (1) \* ($23.00) = $23.00

#### Example 2

Suppose your organization has a project in a region where the price of a terabyte-month is $23.00, and that in a given period this project:

* Stores 1 terabyte of data for the first 15 days of the month
* Stores 2 terabyte of data for the last 15 days of the month

On average throughout the month, the project was storing 1.5Tb of data. So the bill would be (1.5) \* ($23.00) = $34.5.

Was this page helpful?

* How DCUs are Calculated
  + DCU Examples
* How AI Usage Is Calculated
  + AI Examples
* How Storage Usage Is Calculated
  + Storage Usage Examples

<div style="page-break-after: always;"></div>

# Project Preferences | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/projects/preferences

Preferences let you customize the behavior of specific features in the Dremio console.

To view the available preferences:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **Preferences** in the project settings sidebar.

   This opens the Preferences page, showing the Dremio console settings that can be modified.
3. Use the toggle next to the setting to enable or disable for all users.

   If any preferences are modified, users must refresh their browsers to see the change.

These preferences and their descriptions are listed in the table below.

| Setting | Default | Enabled | Disabled | Details |
| --- | --- | --- | --- | --- |
| SQL Autocomplete | Enabled | Autocomplete provides suggestions for SQL keywords, catalog objects, and functions while you are constructing SQL statements.  is visible in the SQL editor, although users can switch the button off within their own accounts. | The button is hidden from the SQL editor and suggestions are not provided. | See how this works in the [SQL editor](/dremio-cloud/get-started/quick-tour). |
| Copy or Download Results | Enabled | and  are visible above the results table, because users are allowed to copy or download the results in the SQL editor. | The buttons are hidden and users cannot copy or download results in the SQL editor. | See how this works in [result set actions](/dremio-cloud/get-started/quick-tour). |
| Query Dataset on Click | Enabled | Clicking on a dataset opens the SQL Runner with a `SELECT` statement on the dataset. | If you would rather click directly on a dataset to see or edit the definition, disable this preference. Clicking on a dataset opens the Datasets page, showing a `SELECT` statement on the dataset or the dataset's definition that you can view or edit depending on your dataset privileges. |  |
| Autonomous Reflections | Enabled | Dremio automatically creates and drops Reflections based on query patterns from the last 7 days to seamlessly accelerate performance. | Dremio will provide recommendations to create and drop Reflections based on query patterns from the last 7 days to accelerate query performance. | See how this works in the [Autonomous Reflections](/dremio-cloud/admin/performance/autonomous-reflections). |
| AI Features | Enabled | When enabled, users can interact with the Dremio's AI Agent and AI functions. The AI Agent enables agentic workflows, allowing analysts to work with the agent to generate SQL queries, find insights, and create visualizations. The AI functions allow engineers to query unstructured data and use LLMs during SQL execution. | The AI Agent and AI functions will not work. | See how this works in [Explore with AI Agent](/dremio-cloud/explore-analyze/ai-agent) and [AI Functions](/dremio-cloud/sql/sql-functions/AI). |
| Generate wikis and labels | Enabled | In the Details panel, both **Generate wiki** and **Generate labels** links will be visible for generating wikis and labels. | The links for **Generate wiki** and **Generate labels** will be hidden, making these features unavailable. | See how this works in [Wikis and Labels](/dremio-cloud/manage-govern/wikis-labels). |

Was this page helpful?

<div style="page-break-after: always;"></div>

# Profiles | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/monitor/jobs/profiles

On this page

Visual profiles and raw profiles are available for jobs that have run queries.

## Visual Profiles

You can view the operations in visual profiles to diagnose performance or cost issues and to see the results of changes that you make, either to queries themselves or their environment, to improve performance or reduce costs.

A query profile details the plan that Dremio devised for running a query and shows statistics from the query's execution. A visual representation of a query profile is located on the Visual Profile tab. This visual profile consists of operators that are arranged as a tree, where each operator has one or two upstream operators that represent a specific action, such as a table scan, join, or sort. At the top of the tree, a single root operator represents the query results, and at the bottom, the leaf operators represent scan or read operations from datasets.

Data processing begins with the reading of datasets at the bottom of the tree structure, and data is sequentially processed up the tree. A query plan can have many branches, and each branch is processed separately until a join or other operation connects it to the rest of the tree.

### Phases

A query plan is composed of query phases (also called major fragments), and each phase defines a series of operations that are running in parallel. A query phase is depicted by the same colored boxes that are grouped together in a visual profile.

Within the query phases are multiple, single-threaded instances (also called minor fragments) running in parallel. Each thread is processing a different set of data through the same series of operations, and this data is exchanged from one phase to another. The number of threads for each operator can be found in the Details section (right panel) of a visual profile.

### Use Visual Profiles

To navigate to the visual profile for a job:

1. Click ![This is the icon that represents the Jobs page.](/images/cloud/jobs-page-icon.png "Icon represents the Jobs page.") in the side navigation bar.
2. On the Jobs page, click a job that you would like to see the visual profile for.
3. At the top of the next page, click the Visual Profile tab to open.

The main components of a visual profile are shown below:

![](/images/query-profile-visualizer.png)

| Location | Description |
| --- | --- |
| 1 | The Visual Profile tab shows a visual representation of a query profile. |
| 2 | The left panel is where you can view the phases of the query execution or single operators, sorting them by runtime, total memory used, or records produced. Operators of the same color are within the same phase. Clicking the Collapse This button hides a panel from view. hides the left panel from view. |
| 3 | The tree graph allows you to select an operator and find out where it is in relation to the rest of the query plan. |
| 4 | The zoom controls the size of the tree graph so it's easier for you to view. |
| 5 | The right panel shows the details and statistics about the selected operator. Clicking the Collapse This button hides a panel from view. hides the right panel from view. |

### Use Cases

#### Improve the Performance of Queries

You may notice that a query is taking more time than expected and want to know if something can be done to reduce the execution time. By viewing its visual profile, you can, for example, quickly find the operators with the highest processing times.

You might decide to try making simple adjustments to cause Dremio to choose a different plan. Some of the possible adjustments include:

* Adding a filter on a partition column to reduce the amount of data scanned
* Changing join logic to avoid expanding joins (which return more rows than either of the inputs) or nested-loop joins
* Creating a Reflection to avoid some of processing-intensive work done by the query

#### Reduce Query-Execution Costs

If you are an administrator, you may be interested in tuning the system as a whole to support higher concurrency and lower resource usage across the system, because you want to identify the most expensive queries in the system and then see what can be done to lower the cost of these queries. Such an investigation is often important even if individual users are happy with the performance of their own queries.

On the Jobs page, you can use the columns to find the queries with the highest cost, greatest number of rows scanned, and more. You can then study the visual profiles for these queries, identifying system or data problems, and mismatches between how data is stored and how these queries retrieve it. You can try repartitioning data, modifying data types, sorting, creating views, creating Reflections, and other changes.

## Raw Profiles

Click **Raw Profile** to open a raw profile of the job in a separate dialog, which includes a job summary, state durations, threads, resource allocation, operators, visualized plan, acceleration, and other details.

A raw profile is a UI-generated profile that is a subset of the data that you can download and provides a summary of metrics collected for each executed query that can be used to monitor and analyze query performance.

To navigate to a raw profile:

1. Click ![This is the icon that represents the Jobs page.](/images/cloud/jobs-page-icon.png "Icon represents the Jobs page.") in the side navigation bar to open the Jobs page.
2. On the Jobs page, click a job that you would like to see the raw profile for.
3. At the top of the next page, click the Raw Profile tab to open a raw profile of the job in a separate dialog. The associated raw profile dialog shows a variety of information for review.

### Views

Within the Raw Profile dialog, you can analyze the Job Metrics based on the following views:

| View | Description |
| --- | --- |
| Query | Shows the selected query statement and job metrics. See if your SQL query is what you were expecting and the query is run against the source data. |
| Visualized Plan | Shows a visualized diagram and job metrics. This view is useful in understanding the flow of the query and for analyzing out of memory issues and incorrect results. The detailed visualized pan diagram is always read from the bottom up. |
| Planning | Shows planning metrics, query output schema, non default options, and job metrics. This view shows how query planning is executed, because it provides statistics about the actual cost of the query operations in terms of memory, input/output, and CPU processing. You can use this view to identify which operations consumed the majority of the resources during a query and to address the cost-intensive operations. In particular, the following information is useful:  * Non Default Options – See if non-default parameters are being used. * Metadata Cache Hits and Misses with times * Final Physical Transformation – Look for pushdown queries for RDBMS, MongoDB, or Elasticsearch, filter pushdowns or partition pruning for parquet, and view usage of stripes for ORC. * Compare the estimated row count versus the actual scan, join, or aggregate result. * Row Count – See if row count (versus rows) is used. Row count can cause an expensive broadcast. * Build – See if build (versus probe) is used. Build loads data into memory. |
| Acceleration | Shows Reflection outcome, canonicalized user query alternatives, Reflection details, and job metrics.  * Multiple substitutions – See if the substitutions are excessive. * System activity – See if `sys.project.reflections`, `sys.project.materializations`, and `sys.project.refreshes` are excessive. * Comparisons – Compare cumulative cost (found in Best Cost Replacement Plan) against Logical Planning, which is in the Planning view.  This view is useful for determining whether exceptions or matches are occurring. The following considerations determines the acceleration process:  * Considered, Matched, Chosen – The query is accelerated. * Considered, Matched, Not Chosen – The query is not accelerated because either a costing issue or an exception during substitution occurred. * Considered, Not Matched, Not Chosen – The query is not accelerated because the Reflection does not have the data to accelerate. |
| Error | (If applicable) Shows information about an error. The Failure Node is always the coordinator node and the server name inside the error message is the actual affected node. |

### Job Metrics

Each view displays the following metrics:

* **Job Summary**
* **Time in UTC**
* **State Durations**
* **Context**
* **Threads**
* **Resource Allocation**
* **Nodes**
* **Operators**

#### Job Summary

The job summary information includes:

* State
* Coordinator
* Threads
* Command Pool Wait
* Total Query Time
* # Joins in user query
* # Joins in final plan
* Considered Reflections
* Matched Reflections
* Chosen Reflections

#### Time in UTC

The Time in UTC section lists the job's start and end time, in UTC format.

#### State Durations

The State Durations section lists the length of time (in milliseconds) for each of the job states:

* Pending
* Metadata Retrieval
* Planning
* Engine Start
* Queued
* Execution Planning
* Starting
* Running

For descriptions of the job states, see [Job States and Statuses](/dremio-cloud/admin/monitor/jobs/#job-states-and-statuses).

#### Context

If you are querying an Iceberg catalog object, the Context section lists the Iceberg catalog and branch that is referenced in the query. Otherwise, the Context section is not populated. Read [Iceberg Catalogs in Dremio](/dremio-cloud/developer/data-formats/iceberg#iceberg-catalogs-in-dremio) for more information.

#### Threads

The Threads section provides an overview table and a major fragment block for each major fragment. Each row in the Overview table provides the number of minor fragments that Dremio parallelized from each major fragment, as well as aggregate time and memory metrics for the minor fragments.

Major fragment blocks correspond to a row in the Overview table. You can expand the blocks to see metrics for all of the minor fragments that were parallelized from each major fragment, including the host on which each minor fragment ran. Each row in the major fragment table presents the fragment state, time metrics, memory metrics, and aggregate input metrics of each minor fragment.

In particular, the following metrics are useful:

* Setup – Time opening and closing of files.
* Waiting – Time waiting on the CPU.
* Blocked on Downstream – Represents completed work whereas the next phase is not ready to accept work.
* Blocked on Upstream – Represents the phase before it is ready to give work though the cloud phase is not ready.
* Phase Metrics – Displays memory used per node (Phases can run in parallel).

#### Resource Allocation

The Resource Allocation section shows the following details for managed resources and workloads:

* Engine Name
* Queue Name
* Queue Id
* Query Cost
* Query Type

#### Nodes

The Nodes section includes host name, resource waiting time, and peak memory.

#### Operators

The Operators section shows aggregate metrics for each operator within a major fragment that performed relational operations during query execution.

**Operator Overview Table**

The following table lists descriptions for each column in the Operators Overview table:

| Column Name | Description |
| --- | --- |
| SqlOperatorImpl ID | The coordinates of an operator that performed an operation during a particular phase of the query. For example, 02-xx-03 where 02 is the major fragment ID, xx corresponds to a minor fragment ID, and 03 is the Operator ID. |
| Type | The operator type. Operators can be of type project, filter, hash join, single sender, or unordered receiver. |
| Min Setup Time, Avg Setup Time, Max Setup Time | In general, the time spent opening and closing files. Specifically, the minimum, average, and maximum amount of time spent by the operator to set up before performing the operation. |
| Min Process Time, Avg Process Time, Max Process Time | The shortest amount of time the operator spent processing a record, the average time the operator spent in processing each record, and the maximum time that the operator spent in processing a record. |
| Wait (min, avg, max) | In general, the time spent waiting on Disk I/O. These fields represent the minimum, average, and maximum times spent by operators waiting on disk I/O. |
| Avg Peak Memory | Represents the average of the peak direct memory allocated across minor fragments. Relates to the memory needed by operators to perform their operations, such as hash join or sort. |
| Max Peak Memory | Represents the maximum of the peak direct memory allocated across minor fragments. Relates to the memory needed by operators to perform their operations, such as hash join or sort. |

**Operator Block**

The Operator Block shows time and memory metrics for each operator type within a major fragment. Examples of operator types include:

* SCREEN
* PROJECT
* WRITER\_COMMITTER
* ARROW\_WRITER

The following table describes each column in the Operator Block:

| Column Name | Description |
| --- | --- |
| Thread | The coordinate ID of the minor fragment on which the operator ran. For example, 04-03-01 where 04 is the major fragment ID, 03 is the minor fragment ID, and 01 is the Operator ID. |
| Setup Time | The amount of time spent by the operator to set up before performing its operation. This includes run-time code generation and opening a file. |
| Process Time | The amount of time spent by the operator to perform its operation. |
| Wait Time | The cumulative amount of time spent by an operator waiting for external resources. such as waiting to send records, waiting to receive records, waiting to write to disk, and waiting to read from disk. |
| Max Batches | The maximum number of record batches consumed from a single input stream. |
| Max Records | The maximum number of records consumed from a single input stream. |
| Peak Memory | Represents the peak direct memory allocated. Relates to the memory needed by the operators to perform their operations, such as hash join and sort. |
| Host Name | The hostname of the Executor the minor fragment is running on. |
| Record Processing Rate | The rate at which records in the minor fragment are being processed. Combined with the Host Name, the Record Processing Rate can help find hot spots in the cluster, either from skewed data or a noisy query running on the same cluster. |
| Operator State | The status of the minor fragment. |
| Last Schedule Time | The last time at which work related to the minor fragment was scheduled to be executed. |

Operator blocks also contain three drop-down menus: Operator Metrics, Operator Details, and Host Metrics. Operator Metrics and Operator Details are unique to the type of operator and provide more detail about the operation of the minor fragments. Operator Metrics and Operator Details are intended to be consumed by Dremio engineers. Depending on the operator, both can be blank. Host Metrics provides high-level information about the host used when executing the operator.

Was this page helpful?

* Visual Profiles
  + Phases
  + Use Visual Profiles
  + Use Cases
* Raw Profiles
  + Views
  + Job Metrics

<div style="page-break-after: always;"></div>

# Results Cache | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/performance/results-cache

On this page

Results cache improves query performance by reusing results from previous executions of the same deterministic query, provided that the underlying dataset remains unchanged and the previous execution was by the same user. The results cache feature works out of the box, requires no configuration, and automatically caches and reuses results. Regardless of whether a query uses results cache, it always returns the same results.

Results cache is client-agnostic, meaning a query executed in the Dremio console will result in a cache hit even if it is later re-run through other clients like JDBC, ODBC, REST, or Arrow Flight. For a query to use the cache, its query plan must remain identical to the original cached version. Any changes to the schema or dataset generate a new query plan, invalidating the cache.

Results cache also supports seamless coordinator scale-out, allowing newly added coordinators to benefit immediately from previously cached results.

## Cases Supported By Results Cache

Query result are cached in the following cases:

* The SQL statement is a `SELECT` statement.
* The query reads from an Iceberg, Parquet dataset, or from a raw Reflection defined on other Dremio supported data sources and formats, such as relational databases, `CSV`, `JSON`, or `TEXT`.
* The query does not contain dynamic functions such as `QUERY_USER`, `IS_MEMBER`, `RAND`, `CURRENT_DATE`, or `NOW`.
* The query does not reference `SYS` or `INFORMATION_SCHEMA` tables, or use external query.
* The result set size, when stored in Arrow format, is less than or equal to 20 MB.
* The query is not executed in Dremio console as a preview.

## View Whether Queries Used Results Cache

You can view the list of jobs on the Jobs page to determine if queries from data consumers were accelerated by the results cache.

To find whether a query was accelerated by a results cache:

1. Find the job that ran the query and look for ![This is the icon that indicates a Reflection was used.](/images/icons/reflections.png "Reflections icon") next to it, which indicates that the query was accelerated using either Reflections or the results cache.
2. Click on the row representing the job that ran the query to view the job summary. The summary, displayed in the pane to the right, provides details on whether the query was accelerated using results cache or Reflections.

![Results cache on the Job Overview page](/images/cloud/jobs-details-results-cache.png "Results cache")

## Storage

Cached results are stored in the project store alongside all project-specific data, such as metadata and Reflections. Executors write cache entries as Arrow data files and read them when processing `SELECT` queries that result in a cache hit. Coordinators are responsible for managing the deletion of expired cache files.

## Deletion

A background task running on one of the Dremio coordinators handles cache expiration. This task runs every hour to mark cache entries that have not been accessed in the past 24 hours as expired and subsequently deletes them along with their associated cache files.

## Considerations and Limitations

SQL queries executed through the Dremio console or a REST client that access the cache will rewrite the cached query results to the job results store to enable pagination.

Was this page helpful?

* Cases Supported By Results Cache
* View Whether Queries Used Results Cache
* Storage
* Deletion
* Considerations and Limitations

<div style="page-break-after: always;"></div>

# Workload Management | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/engines/workload-management

On this page

This topic covers how to manage resources and workloads by routing queries to particular engines through rules.

## Overview

You can manage Dremio workloads via routing rules, which are evaluated at runtime (before query planning) to decide which [query engine](/dremio-cloud/admin/engines/) to use for a given query. In projects with only one engine, all queries share the same execution resources and route to the same single engine. However, when multiple engines are provisioned, rules determine the engine to be used.

You must arrange the rules in the order that you want them to be evaluated. In the case that multiple rules evaluate to true for a given query, the first rule that returns true will be used to select the engine.
The following diagram shows a series of rules that are evaluated when a job gets submitted.

* Rule1 routes jobs to Engine1
* Rule2 routes jobs to Engine2
* Rule3 routes jobs to the default engine that was created on project start up
* Rule4 rejects the jobs that evaluate to true

![](/images/cloud/rules-diagram.png)

## Rules

You can use Dremio SQL syntax to specify rules to target particular jobs.

The following are the types of rules that can be created along with examples.

### User

Create a rule that identifies the user that triggers the job.

Create rule that identifies user

```
USER in ('JRyan','PDirk','CPhillips')
```

### Group Membership

Create a rule that identifies if the user that triggers the job is part of a particular group.

Create rule that identifies whether user belongs to a specified group

```
is_member('MarketingOps') OR  
is_member('Engineering')
```

### Job Type

Create a rule depending on the type of job. The types of jobs can be identified by the following categories:

* Flight
* JDBC
* Internal Preview
* Internal Run
* Metadata Refresh
* ODBC
* Reflections
* REST
* UI Download
* UI Preview
* UI Run

Create rule based on type of job

```
query_type() IN ('JDBC', 'ODBC', 'UI Run', 'Flight')
```

### Query Label

Labels enable rules that route queries running named commands to specific engines. Dremio supports the following query labels:

| Query Label | Description |
| --- | --- |
| COPY | Assigned to all queries running a [COPY INTO](/dremio-cloud/sql/commands/copy-into-table) SQL command |
| CTAS | Assigned to all queries running a [CREATE TABLE AS](/dremio-cloud/sql/commands/create-table-as) SQL command |
| DML | Assigned to all queries running an [INSERT](/dremio-cloud/sql/commands/insert), [UPDATE](/dremio-cloud/sql/commands/update), [DELETE](/dremio-cloud/sql/commands/delete), [MERGE](/dremio-cloud/sql/commands/merge), or [TRUNCATE](/dremio-cloud/sql/commands/truncate) SQL command |
| OPTIMIZATION | Assigned to all queries running an [OPTIMIZE](/dremio-cloud/sql/commands/optimize-table) SQL command |

Here are two example routing rules:

Create a routing rule for queries running a COPY INTO command

```
query_label() IN ('COPY')
```

Create a routing rule for queries running the DML commands INSERT, UPDATE, DELETE, MERGE, or TRUNCATE

```
query_label() IN ('DML')
```

### Query Attributes

Query attributes enable routing rules that direct queries to specific engines based on their characteristics.

Dremio supports the following query attributes:

| Query Attribute | Description |
| --- | --- |
| `DREMIO_MCP` | Set when the job is submitted via the Dremio MCP Server. |
| `AI_AGENT` | Set when the job is submitted via the Dremio AI Agent. |
| `AI_FUNCTIONS` | Set when the job contains AI functions. |

You can use the following functions to define routing rules based on query attributes:

| Function | Applicable Attribute | Description |
| --- | --- | --- |
| `query_has_attribute(<attr>)` | `DREMIO_MCP`, `AI_AGENT`, `AI_FUNCTIONS` | Returns true if the specified attribute is present. |
| `query_attribute(<attr>)` | `DREMIO_MCP`, `AI_AGENT`, `AI_FUNCTIONS` | Returns the value of the attribute (if present), otherwise NULL. |
| `query_calls_ai_functions()` | NA | Returns true if the job has an AI function in the query. |

Examples:

Create a routing rule for queries that use AI functions and are executed by a user

```
query_calls_ai_functions() AND USER = 'JRyan'
```

Create a routing rule for queries with `DREMIO_MCP` and `AI_FUNCTION` 

```
query_has_attribute('DREMIO_MCP') AND query_has_attribute('AI_FUNCTIONS')
```

### Tag

Create a rule that routes jobs based on a routing tag.

Create rule that routes jobs based on routing tag

```
tag() = 'ProductionDashboardQueue'
```

### Date and Time

Create a rule that routes a job based on the time it was triggered. Use Dremio SQL Functions.

Create rule that routes jobs based on time triggered

```
EXTRACT(HOUR FROM CURRENT_TIME)  
BETWEEN 9 AND 18
```

### Combined Conditions

Create rules based on multiple conditions.

The following example routes a job depending on user, group membership, query type, query cost, tag, and the time of day that it was triggered.

Create rule based on user, group, job type, query cost, tag, and time triggered

```
(  
USER IN ('JRyan', 'PDirk', 'CPhillips')  
OR  is_member('superadmins')  
)  
AND query_type IN ('ODBC')  
AND EXTRACT(HOUR FROM CURRENT_TIME)  
BETWEEN 9 AND 18
```

### Default Rules

Each Dremio [project](/dremio-cloud/admin/projects/) has its own set of rules. When a project is created, Dremio automatically creates rules for the default and preview engines. You can edit these rules as needed.

| Order | Rule Name | Rule | Engine |
| --- | --- | --- | --- |
| 1 | UI Previews | query\_type() = 'UI Preview' | preview |
| 2 | Reflections | query\_type() = 'Reflections' | default |
| 3 | All Other Queries | All other queries | default |

## View All Rules

To view all rules:

1. Click the Project Settings ![This is the icon that represents the Project Settings.](/images/icons/project-settings.png "Icon represents the Project Settings.") icon in the side navigation bar.
2. Select **Engine Routing** in the project settings sidebar to see the list of engine routing rules.

## Add a Rule

To add a rule:

1. On the Engine Routing page, click the **Add Rule** button at the top-right corner of the screen.
2. In the **New Rule** dialog, for **Rule Name**, enter a name.
3. For **Conditions**, enter the routing condition. See Rules for supported conditions.
4. For **Action**, complete one of the following options:

   a. If you want to route the jobs that meet the conditions to a particular engine, select the **Route to engine** option. Then use the engine selector to choose the engine.

   b. If you want to reject the jobs that meet the conditions, select the **Reject** option.
5. Click **Add**.

## Edit a Rule

To edit a rule:

1. On the Engine Routing page, hover over the rule and click the Edit Rule ![This is the icon that represents the Edit Rule settings.](/images/icons/edit.png "Icon represents the Edit Rule settings.") icon that appears next to the rule.
2. In the **Edit Rule** dialog, for **Rule Name**, enter a name.
3. For **Conditions**, enter the routing condition. See Rules for supported conditions.
4. For **Action**, complete one of the following options:

   a. If you want to route the jobs that meet the conditions to a particular engine, select the **Route to engine** option. Then use the engine selector to choose the engine.

   b. If you want to reject the jobs that meet the conditions, select the **Reject** option.
5. Click **Save**.

## Delete a Rule

To delete a rule:

1. On the Engine Routing page, hover over the rule and click the Delete Rule ![This is the icon that represents the Delete Rule settings.](/images/icons/trash.png "Icon represents the Delete Rule settings.") icon that appears next to the rule.

caution

You must have at least one rule per project to route queries to a particular engine.

2. In the **Delete Rule** dialog, click **Delete** to confirm.

## Set and Reset Engines

The [`SET ENGINE`](/dremio-cloud/sql/commands/set-engine) SQL command is used to specify the exact execution engine to run subsequent queries in the current session. When using `SET ENGINE`, WLM rules and direct routing connection properties are bypassed, and queries are routed directly to the specified queue. The [`RESET ENGINE`](/dremio-cloud/sql/commands/reset-engine) command clears the session-level engine override, reverting query routing to follow the Workload Management (WLM) rules or any direct routing connection property if set.

## SET TAG

The [`SET TAG`](/dremio-cloud/sql/commands/set-tag) SQL command is used to specify routing tag for subsequent queries in the current session. If a `ROUTING_TAG` connection property is already set for the session, `SET TAG` will override it. When using `SET TAG`, you must have a previously defined Workload Management (WLM) routing rule that routes queries based on that routing tag. The [`RESET TAG`](/dremio-cloud/sql/commands/reset-tag) command clears the session-level routing tag override, reverting query routing to follow the Workload Management (WLM) rules or any direct routing connection property if set.

## Connection Tagging and Direct Routing Configuration

Routing tags are configured by setting the `ROUTING_TAG = <Tag Name>` parameter for a given session to the desired tag name.

### JDBC Session Configuration

To configure JDBC sessions add the `ROUTING_TAG` parameter to the JDBC connection URL. For example: `jdbc:dremio:direct=localhost;ROUTING_TAG='TagA'`.

### ODBC Session Configuration

Configure ODBC sessions as follows:

*Windows Sessions*

Add the `ROUTING_TAG` parameter to the `AdvancedProperties` parameter in the ODBC DSN field.

*Mac OS Sessions*

1. Add the `ROUTING_TAG` parameter to the `AdvancedProperties` parameter in the system `odbc.ini` file located at `/Library/ODBC/odbc.ini`. After adding the parameter, an example Advanced Properties configuration might be: `AdvancedProperties=CastAnyToVarchar=true;HandshakeTimeout=5;QueryTimeout=180;TimestampTZDisplayTimezone=utc;NumberOfPrefetchBuffers=5;ROUTING_TAG='TagA';`
2. Add the `ROUTING_TAG` parameter to the `AdvancedProperties` parameter in the user's DSN located at `~/Library/ODBC/odbc.ini`

## Best Practices for Workload Management

Because every query workload is different, engine sizing often depends on several factors, such as the complexity of queries, number of concurrent users, data sources, dataset size, file and table formats, and specific business requirements for latency and cost. Workload management (WLM) ensures reliable query performance by choosing adequately sized engines for each workload type, configuring engines, and implementing query routing rules to segregate and route query workload types to appropriate engines.

This section describes best practices for adding and using Dremio engines, as well as configuring WLM to achieve reliable query performance in Dremio. This section also includes tips for migrating from self-managed Dremio Software to fully managed Dremio and information about using the system table `sys.project.history.jobs`, which stores metadata for historical jobs executed in a project, to assess the efficacy of WLM settings and make adjustments.

### Set Up Engines

As a fully managed offering, Dremio is the best deployment model for Dremio in production because it allows you to achieve high levels of reliability and durability for your queries and maximize resource efficiency with engine autoscaling and does not require you to manually create and manage engines.

Segregating workload types into separate engines is vital for mitigating noisy neighbor issues, which can jeopardize performance reliability. You can segregate workloads by type, such as ad hoc, dashboard, and lakehouse (COPY INTO, DML, and optimization), as well as by business unit to facilitate cost distribution.

Metadata and Reflection refresh workloads should have their own engines for executing metadata and Reflection refresh queries. These internal queries can use a substantial amount of engine bandwidth, so assigning separate engines ensures that they do not interfere with user-initiated queries. Initial engine sizes should be XSmall and Small, but these sizes may change depending on the number and complexity of Reflection refresh and metadata jobs.

Dremio recommends the following engine setup configurations:

* Dremio offers a range of [engine sizes](/dremio-cloud/admin/engines/#sizes). Experiment with typical queries, concurrency, and engine sizes to establish the best engine size for each workload type based on your organization's budget constraints and latency requirements.
* Maximum concurrency is the maximum number of jobs that Dremio can execute concurrently on an engine replica. Dremio provides an out-of-the-box value for maximum concurrency based on engine size, but we recommend testing with typical queries directed to specific engines to determine the best maximum concurrency values for your query workloads.
* Dremio offers autoscaling to meet the demands of dynamic workloads with engine replicas. It is vital to assess and configure each engine's autoscaling parameters based on your organization's budget constraints and latency requirements for each workload type. You can choose the minimum and maximum number of replicas for each engine and specify any advanced configuration as needed. For example, dashboard workloads must meet stringent low-latency requirements and are prioritized for performance rather than cost. Engines added and assigned to execute the dashboard workloads may therefore be configured to autoscale using replicas. On the other hand, an engine for ad hoc workloads may have budget constraints and therefore be configured to autoscale with a maximum of one replica.

### Route Workloads

Queries are routed to engines according to routing rules. You may use Dremio's out-of-the-box routing rules that route queries to the preview engines that are established by default, but Dremio recommends creating custom routing rules based on your workloads and business requirements. Custom rules can include factors such as user, group membership, job type, date and time, query label, and tag. Read Rules for examples.

The following table lists example routing rules based on query\_type, query\_label, and tags:

| Order | Rule Name | Rule | Engine |
| --- | --- | --- | --- |
| 1 | Reflections | `query_type() = 'Reflections'` | Reflection |
| 2 | Metadata | `query_type() = 'Metadata Refresh'` | Metadata |
| 3 | Dashboards | `tag() = 'dashboard'` | Dashboard |
| 4 | Ad hoc Queries | `query_type() IN ( 'UI Run' , 'REST') OR tag() = 'ad hoc'` | Ad hoc |
| 5 | Lakehouse Queries | `query_label() IN ('COPY','DML','CTAS', 'OPTIMIZATION')` | Lakehouse |
| 6 | All Other Queries | All other queries | Preview |

### Use the `sys.project.history.jobs` System Table

The [`sys.project.history.jobs`](/dremio-cloud/sql/system-tables/jobs-historical) system table contains metadata for recent jobs executed in a project, including time statistics, cost, and other relevant information. You can use the data in the `sys.project.history.jobs` system table to evaluate the effectiveness of WLM settings and make adjustments based on job metadata.

### Use Job Analyzer

Job Analyzer is a package of useful query and view definitions that you may create over the `sys.projects.history.jobs` system table and use to analyze job metadata. Job Analyzer is available in a [public GitHub repository](https://github.com/dremio/professional-services/tree/main/tools/dremio-cloud-job-analyzer).

Was this page helpful?

* Overview
* Rules
  + User
  + Group Membership
  + Job Type
  + Query Label
  + Query Attributes
  + Tag
  + Date and Time
  + Combined Conditions
  + Default Rules
* View All Rules
* Add a Rule
* Edit a Rule
* Delete a Rule
* Set and Reset Engines
* SET TAG
* Connection Tagging and Direct Routing Configuration
  + JDBC Session Configuration
  + ODBC Session Configuration
* Best Practices for Workload Management
  + Set Up Engines
  + Route Workloads
  + Use the `sys.project.history.jobs` System Table
  + Use Job Analyzer

<div style="page-break-after: always;"></div>

# Manual Reflections | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/performance/manual-reflections/

On this page

With [Autonomous Reflections](/dremio-cloud/admin/performance/autonomous-reflections) reducing the need for manual work, you no longer need to create or manage Reflections. However, when Autonomous Reflections are not enabled or for situations that require manual control, this page provides guidance on getting Reflection recommendations and how to manage raw Reflections, aggregation Reflections, and external Reflections in Dremio.

note

For non-duplicating joins, Dremio can accelerate queries that reference only some of the joins in a Reflection, eliminating the need to create separate Reflections for every table combination.

## Reflection Recommendations

When [Autonomous Reflections](/dremio-cloud/admin/performance/autonomous-reflections) are not enabled, Dremio automatically provides recommendations to add and remove Reflections based on query patterns to optimize performance for queries on Iceberg tables, UniForm table, Parquet datasets, and any views built on these datasets.

Recommendations to add Reflections are sorted by overall effectiveness, with the most effective recommendations shown on top. Effectiveness relates to metrics such as the estimated number of accelerated jobs, potential increase in query execution speedup, and potential time saved during querying. These are rough estimates based on past data that can give you insight into the potential benefits of each recommendation.
Reflections created using these recommendations refresh automatically when source data changes on:

* Iceberg tables – When the table is modified through Dremio or other engines. Dremio polls tables every 10 seconds.
* Parquet datasets   – When metadata is updated in Dremio.

To view and apply the Reflection recommendations:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project Settings**.
2. Select **Reflections** from the project settings sidebar.
3. Click **Reflections Recommendations** to access the list of suggested Reflections.
4. To apply a recommendation, click ![](/images/icons/add-recommendation.png) at the end of the corresponding row.

Reflections created using usage-based recommendations are only used when fully synchronized with their source data to ensure up-to-date query results.

To generate recommendations for default raw and aggregation Reflections, you can obtain the job IDs by looking them up on the [Jobs page](/dremio-cloud/admin/monitor/jobs). Then, use either the [`SYS.RECOMMEND_REFLECTIONS`](/dremio-cloud/sql/table-functions/recommend-reflections) table function or the [Recommendations API](/dremio-cloud/api/reflection/recommendations) to submit job IDs to accelerate specific SQL queries.

## Raw Reflections

Retain the same number of records as its anchor while allowing a subset of columns. It enhances query performance by materializing complex views, transforming data from non-performant sources into the Iceberg table format optimized for large-scale analytics, and utilizing partitioning and sorting for faster access. By precomputing and storing data in an optimized format, raw Reflections significantly reduce query latency and improve overall efficiency.

You can use the Reflections editor to create two types of raw Reflection:

* A default raw Reflection that includes all of the columns of the anchor, but does not sort or horizontally partition on any columns
* A raw Reflection that includes all or a subset of the columns of the anchor, and that does one or both of the following things:

  + Sorts on one or more columns
  + Horizontally partitions the data according to the values in one or more columns

note

For creating Reflections on views and tables with row-access and column-masking policies, see [Use Reflections on Datasets with Policies](/dremio-cloud/manage-govern/row-column-policies#use-reflections-on-datasets-with-policies).

### Prerequisites

* If you want to accelerate queries on unoptimized data or data in slow storage, create a view that is itself created from a table in a non-columnar format or on slow-scan storage. You can then create your raw Reflection from that view.
* If you want to accelerate "needle-in-a-haystack" queries, create a view that includes a predicate to include only the rows that you want to scan. You can then create your raw Reflection from that view.
* If you want to accelerate queries that perform expensive transformations, create a view that performs those transformations. You can then create your raw Reflection from that view.
* If you want to accelerate queries that perform joins, create a view that performs the joins. You can then create your raw Reflection from that view.

### Create Default Raw Reflections

In the **Basic** view of the Reflections editor, you can create a raw Reflection that includes all of the fields that are in a table or view. Creating a basic raw Reflection ensures that Dremio never runs user queries against the underlying table or view when the raw Reflection is enabled.

To create a raw Reflection in the **Basic** view of the Reflections editor:

1. In the Dremio console, click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "Datasets page.") in the side navigation bar to go to the Datasets page.
2. In the catalog or folder in which the anchor is located, hover over the anchor name and click ![](/images/icons/settings.png).
3. Select **Reflections** in the table or view settings sidebar.
4. Click the toggle switch on the left side of the **Raw Reflections** bar.

   ![](/images/enabling-raw-reflections.png)
5. Click **Save**.

#### Restrictions of the **Basic** View

* You cannot select fields to sort or create horizontal partitions on.
* The name of the Reflection that you create is restricted to "Raw Reflection".
* You can create only one raw Reflection. If you want to create multiple raw Reflections at a time, use the **Advanced** view.

### Create Customized Raw Reflections

In the **Advanced** view of the Reflections editor, you can create one or more raw Reflections that include all or a selection of the fields that are in the anchor or supported anchor. You can also choose sort fields and fields for partitioning horizontally.

Dremio recommends that you follow the best practices listed in [Operational Excellence](/dremio-cloud/help-support/well-architected-framework/operational-excellence/) when you create customized raw Reflections.

If you make any of the following changes to a raw Reflection when you are using the **Advanced** view, you cannot switch to the **Basic** view:

* Deselect one or more fields in the **Display** column. By default, all of the fields are selected.
* Select one or more fields in the **Sort**, **Partition**, or **Distribute** column.

To create a raw Reflection in the **Advanced** view of the Reflections editor:

1. In the Dremio console, click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "Datasets page.") in the side navigation bar to go to the Datasets page.
2. In the catalog or folder in which the anchor is located, hover over the anchor name and click ![](/images/icons/settings.png).
3. If the **Advanced** view is not already displayed, click the **Advanced View** button in the top-right corner of the editor.
4. Click the toggle switch in the table labeled **Raw Reflection** to enable the raw Reflection.

   Queries do not start using the Reflection, however, until after you have finished editing the Reflection and click **Save** in a later step.

   ![](/images/raw-reflections.png)
5. (Optional) Click in the label to rename the Reflection.

   The purpose of the name is to help you understand, when you read job reports, which Reflections the query optimizer considered and chose when planning queries.
6. In the columns of the table, follow these steps, which you don't have to do in any particular order:

   note

   Ignore the **Distribution** column. Selecting fields in it has no effect on the Reflection.

   * Click in the **Display** column to include fields in or exclude them from your Reflection.
   * Click in the **Sort** column to select fields on which to sort the data in the Reflection. For guidance in selecting a field on which to sort, see [Sort Reflections on High-Cardinality Fields](/dremio-cloud/help-support/well-architected-framework/operational-excellence#sort-reflections-on-high-cardinality-fields).
   * Click in the **Partition** column to select fields on which to horizontally partition the rows in the Reflection. For guidance in selecting fields on which to partition, and which partition transforms to apply to those fields, see [Horizontally Partition Reflections that Have Many Rows](/dremio-cloud/help-support/well-architected-framework/operational-excellence#horizontally-partition-reflections-that-have-many-rows).

     note

     If the Reflection is based on an Iceberg table, a filesystem source, an AWS Glue source, or a Hive source, and that table is partitioned, recommended partition columns and transforms are selected for you. If you change the selection of columns, then this icon appears at the top of the table: ![This is the Recommendations icon.](/images/icons/partition-column-recommendation-icon.png "The Recommendations icon"). You can click it to revert to the recommended selection of partition columns.
7. (Optional) Optimize the number of files used to store the Reflection. You can optimize for fast refreshes or for fast read performance by queries. Follow these steps:

   a. Click the ![](/images/icons/settings.png) in the table in which you are defining the Reflection.

   b. In the field **Reflection execution strategy**, select either of these options:

   * Select **Minimize Time Needed To Refresh** if you need the Reflection to be created as fast as possible. This option can result in the data for the Reflection being stored in many small files. This is the default option.
   * Select **Minimize Number Of Files** when you want to improve the read performance of queries against the Reflection. With this option, there tend to be fewer seeks performed for a given query.
8. Click **Save** when you are finished.

### Edit Raw Reflections

You can edit an existing raw Reflection. You might want to do so if you are iteratively designing and testing a raw Reflection, if the definition of the view that the Reflection was created from was changed, or if the schema of the underlying table was changed.

If you created a raw Reflection in the **Basic** view of the Reflections editor, you must use the **Advanced** view to edit it.

Dremio runs the job or jobs to recreate the Reflection after you click **Save**.

To edit a raw Reflection in the **Advanced** view of the Reflections editor:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **Reflections** in the project settings sidebar.
3. Click the name of the Reflection. This opens the Acceleration dialog with the Reflections editor.
4. Click the **Advanced View** button in the top-right corner of the editor.
5. In the **Raw Reflections** section of the **Advanced** view, locate the table that shows the definition of your Reflection.
6. (Optional) Click in the label to rename the Reflection.

   The purpose of the name is to help you understand, when you read job reports, which Reflections the query optimizer considered and chose when planning queries.
7. In the columns of the table, follow these steps, which you don't have to do in any particular order:

   * Click in the **Display** column to include fields in or exclude them from your Reflection.
   * Click in the **Sort** column to select fields on which to sort the data in the Reflection. For guidance in selecting a field on which to sort, see [Sort Reflections on High-Cardinality Fields](/dremio-cloud/help-support/well-architected-framework/operational-excellence#sort-reflections-on-high-cardinality-fields).
   * Click in the **Partition** column to select fields on which to horizontally partition the rows in the Reflection. For guidance in selecting fields on which to partition, and which partition transforms to apply to those fields, see [Horizontally Partition Reflections that Have Many Rows](/dremio-cloud/help-support/well-architected-framework/operational-excellence#horizontally-partition-reflections-that-have-many-rows).

     If the Reflection is based on an Iceberg table, a filesystem source, an AWS Glue source, or a Hive source, and that table is partitioned, partition columns and transforms are recommended for you. Hover over ![This is the Recommendations icon.](/images/icons/partition-column-recommendation-icon.png "The Recommendations icon") at the top of the table to see the recommendation. Click the icon to accept the recommendation.

   note

   Ignore the **Distribution** column. Selecting fields in it has no effect on the Reflection.
8. (Optional) Optimize the number of files used to store the Reflection. You can optimize for fast refreshes or for fast read performance by queries. Follow these steps:

   a. Click the ![](/images/icons/settings.png) in the table in which you are defining the Reflection.

   b. In the field **Reflection execution strategy**, select either of these options:

   * Select **Minimize Time Needed To Refresh** if you need the Reflection to be created as fast as possible. This option can result in the data for the Reflection being stored in many small files. This is the default option.
   * Select **Minimize Number Of Files** when you want to improve read performance of queries against the Reflection. With this option, there tend to be fewer seeks performed for a given query.
9. Click **Save** when you are finished.

## Aggregation Reflections

Accelerate BI-style queries that involve aggregations (`GROUP BY` queries) by precomputing results (like `SUM`, `COUNT`, `AVG`, `GROUP BY`) across selected dimensions and measures. By precomputing expensive computations, they significantly improve query performance at runtime. These Reflections are ideal for analytical workloads with frequent aggregations on large datasets.

### Create Default Aggregation Reflections

You can use the **Basic** view of the Reflections editor to create one aggregation Reflection that includes fields, from the anchor or supported anchor, that are recommended for use as dimensions or measures. You can add or remove dimensions and measures, too.

To create an aggregation Reflection in the **Basic** view of the Reflections editor:

1. In the Dremio console, click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "Datasets page.") in the side navigation bar to go to the Datasets page.
2. In the catalog or folder in which the anchor is located, hover over the anchor name and click ![](/images/icons/settings.png).
3. In the **Aggregations Reflections** section of the editor, click **Generate** to get recommended fields to use as dimensions and measures. This will override any previously selected dimensions and measures. If you wish to proceed, click **Continue** in the confirmation dialog that follows.
4. In the **Aggregation Reflection** section of the editor, modify or accept the recommended fields for dimensions and measures.
5. To make the Reflection available to the query optimizer after you create it, click the toggle switch on the left side of the **Aggregation Reflections** bar.

   ![](/images/enabling-aggregation-reflections.png)
6. Click **Save**.

#### Restrictions

* You can create only one aggregation Reflection in the **Basic** view. If you want to create multiple aggregations Reflections at a time, use the **Advanced** view.
* You cannot select fields for sorting or horizontally partitioning.
* The name of the Reflection is restricted to "Aggregation Reflection".

### Create Customized Aggregation Reflections

You can use the **Advanced** view of the Reflections editor to create one or more aggregation Reflections that select which fields in the anchor or supporting anchor to use as dimensions and measures. For each field that you use as a measure, you can use one or more of these SQL functions: `APPROX_DISTINCT_COUNT`, `COUNT`, `MAX`, and `MIN`. You can also choose sort fields and fields for partitioning horizontally.

Before you create customized aggregation Reflections, Dremio recommends that you follow the best practices listed in [Operational Excellence](/dremio-cloud/help-support/well-architected-framework/operational-excellence/) when you create customized aggregation Reflections.

To create an aggregation Reflection in the **Advanced** view of the Reflections editor:

1. In the Dremio console, click ![This is the icon that represents the Datasets page.](/images/icons/datasets-page.png "Datasets page.") in the side navigation bar to go to the Datasets page.
2. In the catalog or folder in which the anchor is located, hover over the anchor name and click ![](/images/icons/settings.png).
3. Click the **Advanced View** button in the top-right corner of the editor.
4. Click **Aggregation Reflections**.

   The Aggregation Reflections section is displayed, and one table for refining the aggregation Reflection that appeared in the **Basic** view is ready.

   ![](/images/aggregation-reflections.png)
5. (Optional) Click in the name to rename the Reflection.

   The purpose of the name is to help you understand, when you read job reports, which Reflections the query optimizer considered and chose when planning queries.
6. In the columns of the table, follow these steps, which you don't have to do in any particular order:

   * Click in the **Dimension** column to include or exclude fields to use as dimensions.
   * Click in the **Measure** column to include or exclude fields to use as measures. You can use one or more of these SQL functions for each measure: `APPROX_DISTINCT_COUNT`, `COUNT`, `MAX`, and `MIN`.

     If you want to include a computed measure, first create a view with the computed column to use as a measure, and then create the aggregation Reflection on the view.

   The full list of SQL aggregation functions that Dremio supports is not supported in the Reflections editor. If you want to create a Reflection that aggregates data by using the `AVG`, `CORR`, `HLL`, `SUM`, `VAR_POP`, or `VAR_SAMP` SQL functions, you must create a view that uses the function, and then create a raw Reflection from that view.

   * Click in the **Sort** column to select fields on which to sort the data in the Reflection. For guidance in selecting a field on which to sort, see [Sort Reflections on High-Cardinality Fields](/dremio-cloud/help-support/well-architected-framework/operational-excellence#sort-reflections-on-high-cardinality-fields).
   * Click in the **Partition** column to select fields on which to horizontally partition the rows in the Reflection. For guidance in selecting fields on which to partition, and which partition transforms to apply to those fields, see [Horizontally Partition Reflections that Have Many Rows](/dremio-cloud/help-support/well-architected-framework/operational-excellence#horizontally-partition-reflections-that-have-many-rows).

     If the Reflection is based on an Iceberg table, a filesystem source, an AWS Glue source, or a Hive source, and that table is partitioned, recommended partition columns and transforms are selected for you. If you change the selection of columns, then this icon appears at the top of the table: ![This is the Recommendations icon.](/images/icons/partition-column-recommendation-icon.png "The Recommendations icon"). You can click it to revert back to the recommended selection of partition columns.

   note

   Ignore the **Distribution** column. Selecting fields in it has no effect on the Reflection.
7. (Optional) Optimize the number of files used to store the Reflection. You can optimize for fast refreshes or for fast read performance by queries. Follow these steps:

   a. Click the ![](/images/icons/settings.png) in the table in which you are defining the Reflection.

   b. In the field **Reflection execution strategy**, select either of these options:

   * Select **Minimize Time Needed To Refresh** if you need the Reflection to be created as fast as possible. This option can result in the data for the Reflection being stored in many small files. This is the default option.
   * Select **Minimize Number Of Files** when you want to improve the read performance of queries against the Reflection. With this option, there tend to be fewer seeks performed for a given query.
8. Click **Save** when you are finished.

### Edit Aggregation Reflections

You might want to edit an aggregation Reflection if you are iteratively designing and testing an aggregation Reflection, if the definition of the view that the Reflection was created from was changed, if the schema of the underlying table was changed, or if you want to revise one or more aggregations defined in the Reflection.

If you created an aggregation Reflection in the **Basic** view of the Reflections editor, you can edit that Reflection either in the **Basic** view or in the **Advanced** view.

Dremio runs the job or jobs to recreate the Reflection after you click **Save**.

#### Use the Basic View

To edit an aggregation Reflection in the **Basic** view of the Reflections editor:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **Reflections** in the project settings sidebar.
3. Click the name of the Reflection. This opens the Acceleration dialog with the Reflections editor.
4. In the Aggregation Reflection section of the editor, modify or accept the recommendation for **Dimension** and **Measure** columns.
5. Click **Save**.

#### Use the Advanced View

To edit an aggregation Reflection in the **Advanced** view of the Reflections editor:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **Reflections** in the project settings sidebar.
3. Click the name of the Reflection. This opens the Acceleration dialog with the Reflections editor.
4. Click the **Advanced View** button in the top-right corner of the editor.
5. Click **Aggregation Reflections**.
6. (Optional) Click in the name to rename the Reflection.

   The purpose of the name is to help you understand, when you read job reports, which Reflections the query optimizer considered and chose when planning queries.
7. In the columns of the table, follow these steps, which you don't have to do in any particular order:

   * Click in the **Dimension** column to include or exclude fields to use as dimensions.
   * Click in the **Measure** column to include or exclude fields to use as measures. You can use one or more of these SQL functions for each measure: `APPROX_DISTINCT_COUNT`, `COUNT`, `MAX`, and `MIN`.

   The full list of SQL aggregation functions that Dremio supports is not supported in the Reflections editor. If you want to create a Reflection that aggregates data by using the `AVG`, `CORR`, `HLL`, `SUM`, `VAR_POP`, or `VAR_SAMP` SQL functions, you must create a view that uses the function, and then create a raw Reflection from that view.

   * Click in the **Sort** column to select fields on which to sort the data in the Reflection. For guidance in selecting a field on which to sort, see [Sort Reflections on High-Cardinality Fields](/dremio-cloud/help-support/well-architected-framework/operational-excellence#sort-reflections-on-high-cardinality-fields).
   * Click in the **Partition** column to select fields on which to horizontally partition the rows in the Reflection. For guidance in selecting fields on which to partition, and which partition transforms to apply to those fields, see [Horizontally Partition Reflections that Have Many Rows](/dremio-cloud/help-support/well-architected-framework/operational-excellence#horizontally-partition-reflections-that-have-many-rows).

     If the Reflection is based on an Iceberg table, a filesystem source, an AWS Glue source, or a Hive source, and that table is partitioned, partition columns and transforms are recommended for you. Hover over ![This is the Recommendations icon.](/images/icons/partition-column-recommendation-icon.png "The Recommendations icon") at the top of the table to see the recommendation. Click the icon to accept the recommendation.

   note

   Ignore the **Distribution** column. Selecting fields in it has no effect on the Reflection.
8. (Optional) Optimize the number of files used to store the Reflection. You can optimize for fast refreshes or for fast read performance by queries. Follow these steps:

   a. Click the ![](/images/icons/settings.png) in the table in which you are defining the Reflection.

   b. In the field **Reflection execution strategy**, select either of these options:

   * Select **Minimize Time Needed To Refresh** if you need the Reflection to be created as fast as possible. This option can result in the data for the Reflection being stored in many small files. This is the default option.
   * Select **Minimize Number Of Files** when you want to improve the read performance of queries against the Reflection. With this option, there tend to be fewer seeks performed for a given query.
9. Click **Save** when you are finished.

## External Reflections

Reference precomputed tables in external data sources instead of materializing Reflections within Dremio, eliminating refresh overhead and storage costs. You can use an external Reflection by defining a view in Dremio that matches the precomputed table and mapping the view to the external data source. The data in the precomputed table is not refreshed by Dremio. When querying the view, Dremio’s query planner leverages the external Reflection to generate optimal execution plans, improving query performance without additional storage consumption in Dremio.

### Create External Reflections

To create an external Reflection:

1. Follow these steps in the data source:

   a. Select your source table.

   b. Create a table that is derived from the source table, such as an aggregation table, if you do not already have one.
2. Follow these steps in Dremio:

   a. [Define a view on the derived table in the data source.](/dremio-cloud/sql/commands/create-view) The definition must match that of the derived table.

   b. [Define a new external Reflection that maps the view to the derived table.](/dremio-cloud/sql/commands/alter-table)

note

The data types and column names in the external Reflection must match those in the view that the external Reflection is mapped to.

Suppose you have a data source named `mySource` that is connected to Dremio. In that data source, there are (among all of your other tables) these two tables:

* `sales`, which is a very large table of sales data.
* `sales_by_region`, which aggregates by region the data that is in `sales`.
  You want to make the data in `sales_by_region` available to data analysts who use Dremio. However, because you already have the `sales_by_region` table created, you do not see the need to create a Dremio table from `sales`, then create a Dremio view that duplicates `sales_by_region`, and finally create a Reflection on the view. You would like instead to make `sales_by_region` available to queries run from BI tools through Dremio.

To do that, you follow these steps:

1. Create a view in Dremio that has the same definition as `sales_by_region`. Notice that the `FROM` clause points to the `sales` table that is in your data source, not to a Dremio table.

   Example View 

   ```
   CREATE VIEW "myWorkspace"."sales_by_region" AS  
   SELECT  
       AVG(sales_amount) average_sales,  
       SUM(sales_amount) total_sales,  
       COUNT(*) sales_count,  
       region  
   FROM mySource.sales  
   GROUP BY region
   ```
2. Create an external Reflection that maps the view above to `sales_by_region` in `mySource`.

   Example External Reflection 

   ```
   ALTER DATASET "myWorkspace"."sales_by_region"  
   CREATE EXTERNAL Reflection "external_sales_by_region"  
   USING "mySource"."sales_by_region"
   ```

The external Reflection lets Dremio's query planner know that there is a table in `mySource` that matches the Dremio view `myWorkplace.sales_by_region` and that can be used to satisfy queries against the view. When Dremio users query `myWorkspace.sales_by_region`, Dremio routes the query to the data source `mySource`, which runs the query against `mySource.sales_by_region`.

### Edit External Reflections

If you have modified the DDL of a derived table in your data source, follow these steps in Dremio to update the corresponding external Reflection:

1. [Replace the view with one that has a definition that matches the definition of the derived table](/dremio-cloud/sql/commands/create-view). When you do so, the external Reflection is dropped.
2. [Define a new external Reflection that maps the view to the derived table.](/dremio-cloud/sql/commands/alter-table)

## Test Reflections

You can test whether the Reflections that you created are used to satisfy a query without actually running the query. This practice can be helpful when the tables are very large and you want to avoid processing large queries unnecessarily.

To test whether one or more Reflections are used by a query:

1. In the Dremio console, click ![The SQL Runner icon](/images/sql-runner-icon.png "The SQL Runner icon") in the side navigation bar to open the SQL Runner.
2. In the SQL editor, type `EXPLAIN PLAN FOR` and then type or paste in your query.
3. Click **Run**.
4. When the query has finished, click the **Run** link found directly above the query results to view the job details. Any Reflections used will be shown on the page.

## View Whether Queries Used Reflections

You can view the list of jobs on the Jobs page to find out whether queries were accelerated by Reflections. The Jobs page lists the jobs that ran queries, both queries from your data consumers and queries run within the Dremio user interface.

To find whether a query used a Reflection:

1. Find the job that ran the query by looking below the details in each row.
2. Look for ![This is the icon that indicates a Reflection was used.](/images/icons/reflections.png "Reflections icon") next to the job to indicate that one or more Reflections were used.
3. View the job summary by clicking the row that represents the job that ran the query. The job summary appears in the pane to the right of the list of jobs.

### Relationship between Reflections and Jobs

The relationship between a job and a Reflection can be one of the following types:

* CONSIDERED – The Reflection is defined on a dataset that is used in the query but was determined not to cover the query (for example, the Reflection did not have a field that is used by the query).
* MATCHED – A Reflection could have been used to accelerate the query, but Dremio determined that it would not provide any benefits or another Reflection was determined to be a better choice.
* CHOSEN – A Reflection is used to accelerate the query. Note that multiple Reflections can be used to accelerate queries.

## Disable Reflections

Disabled Reflections become unavailable for use by queries and will not be refreshed manually or according to their schedule.

note

Dremio does not disable external Reflections.

To disable a Reflection:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project Settings**.
2. Select **Reflections** in the project settings sidebar.

   This opens the Reflections editor for the Reflection's anchor or supporting anchor.
3. Follow one of these steps:

   * If there is only one raw Reflection for the table or view, in the **Basic** view, click the toggle switch in the **Raw Reflections** bar.
   * If there are two or more raw Reflections for the table or view, in the **Advanced** view, click the toggle switch for the individual raw Reflection that you want to disable.
   * If there is only one aggregation Reflection for the table or view, in the **Basic** view, click the toggle switch in the **Raw Reflections** bar.
   * If there are two or more aggregation Reflections for the table or view, in the **Advanced** view, click the toggle switch for the individual aggregation Reflection that you want to disable.
4. Click **Save**. The changes take effect immediately.

## Delete Reflections

You can delete Reflections individually, or all of the Reflections on a table or view. When you delete a Reflection, its definition, data, and metadata are entirely deleted.

To delete a single raw or aggregation Reflection:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project settings**.
2. Select **Reflections** in the project settings sidebar.

   This opens the Reflections editor for the Reflection's anchor or supporting anchor.
3. Open the **Advanced** view, if it is not already open.
4. If the Reflection is an aggregation Reflection, click **Aggregation Reflections**.
5. Click ![](/images/icons/trash.png) for the Reflection that you want to delete.
6. Click **Save**. The deletion takes effect immediately.

To delete all raw and aggregation Reflections on a table or view:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project Settings**.
2. Select **Reflections** in the project settings sidebar.

   This opens the Reflections editor for the Reflection's anchor or supporting anchor.
3. Click the  in the top right corner of the Reflections page.
4. Click **Delete all reflections**.
5. Click **Save**.

To delete an external Reflection, or to delete a raw or aggregation Reflection without using the Reflections editor, run this SQL command:

Delete a Reflection

```
ALTER DATASET <DATASET_PATH> DROP Reflection <REFLECTION_NAME>
```

* `DATASET_PATH`: The path of the view on which the external Reflection is based.
* `REFLECTION_NAME`: The name of the external Reflection.

## Related Topics

* [Data Reflections Deep Dive](https://university.dremio.com/course/data-reflections-deep-dive) – Enroll in this Dremio University course to learn more about Reflections.
* [Operational Excellence](/dremio-cloud/help-support/well-architected-framework/operational-excellence/) - Follow best practices in Dremio's Well-Architected Framework for creating and managing Reflections.

Was this page helpful?

* Reflection Recommendations
* Raw Reflections
  + Prerequisites
  + Create Default Raw Reflections
  + Create Customized Raw Reflections
  + Edit Raw Reflections
* Aggregation Reflections
  + Create Default Aggregation Reflections
  + Create Customized Aggregation Reflections
  + Edit Aggregation Reflections
* External Reflections
  + Create External Reflections
  + Edit External Reflections
* Test Reflections
* View Whether Queries Used Reflections
  + Relationship between Reflections and Jobs
* Disable Reflections
* Delete Reflections
* Related Topics

<div style="page-break-after: always;"></div>

# Bring Your Own Project Store | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/projects/your-own-project-storage

On this page

To enable secure access between Dremio and your AWS environment, you must create an AWS Identity and Access Management (IAM) role with specific permissions and a trust relationship that allows Dremio’s AWS account to assume that role. The IAM policy and trust configuration are detailed bellow.

## Create Your IAM Role

You will create an IAM Role in your AWS account that grants Dremio the permissions it needs to access your S3 bucket.

Attach the following policy to the role and replace `<bucket-name>` with the name of your own S3 bucket.

IAM Policy

```
{  
   "Version": "2012-10-17",  
   "Statement": [  
       {  
           "Effect": "Allow",  
           "Action": [  
               "s3:GetBucketLocation",  
               "s3:ListAllMyBuckets"  
           ],  
           "Resource": "*"  
       },  
       {  
           "Effect": "Allow",  
           "Action": [  
               "s3:PutObject",  
               "s3:GetObject",  
               "s3:ListBucket",  
               "s3:DeleteObject"  
           ],  
           "Resource": [  
               "arn:aws:s3:::<bucket-name>",  
               "arn:aws:s3:::<bucket-name>/*"  
           ]  
       }  
   ]  
}
```

The first statement allows Dremio to find buckets in your account.

* **ListAllMyBuckets** – Allow Dremio to discover your buckets when validating connectivity.
* **GetBucketLocation** - Allow Dremio to discover your bucket's location.

The second statement allows Dremio to work with the data in your bucket.

* **PutObject / GetObject / DeleteObject** – Allow Dremio to read, write, and delete data within the bucket.
* **ListBucket** – Allow Dremio to enumerate objects in the bucket.

## Define the Trust Relationship

The trust relationship determines which AWS account (in this case, Dremio’s) is permitted to assume your IAM role.

Attach the following policy to the role.

Dremio's US trust account ID is `894535543691`.

Trust Relationship

```
{  
  "Version": "2012-10-17",  
  "Statement": [  
    {  
      "Effect": "Allow",  
      "Principal": {  
        "AWS": "arn:aws:iam::894535543691:root"  
      },  
      "Action": [  
        "sts:AssumeRole",  
        "sts:TagSession"  
      ]  
    }  
  ]  
}
```

* **AssumeRole** - Allows Dremio to assume the provided role.
* **TagSession** - Allows Dremio to pass identifying tags during role assumption, enabling improved tracking and auditing across accounts.

## Validate Role Configuration

1. In the AWS Console, navigate to **IAM → Roles → [Your Role Name]**.
2. Confirm that:

   * The permissions policy matches the example above.
   * The trust relationship allows the Dremio AWS account as the trusted principal.
   * Both `sts:AssumeRole` and `sts:TagSession` actions are present.
3. If Dremio provided an AWS account ID or specific region endpoint, ensure these match your configuration.

## Provide Role ARN to Dremio

Once your role is created and validated:

* Copy the Role ARN (e.g. `arn:aws:iam::<your-account-id>:role/<role-name>`).
* Provide this ARN to Dremio via the [Create Project](/dremio-cloud/admin/projects/#create-a-project) flow.

This allows Dremio to assume the role securely and begin reading/writing data to your S3 bucket.

## (Optional) Enable PrivateLink Connectivity

To enhance security and keep data traffic within AWS’s private network, Dremio supports integration via [AWS PrivateLink](/dremio-cloud/security/privatelink) with DNS-based endpoint resolution.

**To enable:**

* Ensure your AWS environment has PrivateLink endpoints configured for the required services.
* Verify that DNS resolution is enabled so that Dremio can route traffic to your private endpoints.
* Confirm connectivity by testing the endpoint using your VPC configuration.

Was this page helpful?

* Create Your IAM Role
* Define the Trust Relationship
* Validate Role Configuration
* Provide Role ARN to Dremio
* (Optional) Enable PrivateLink Connectivity

<div style="page-break-after: always;"></div>

# Autonomous Reflections | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/performance/autonomous-reflections/

On this page

Dremio automatically creates and manages Reflections based on query patterns to optimize performance for queries on Iceberg tables, UniForm tables, Parquet datasets, and any views built on these datasets. With Autonomous Reflections, management and maintenance are fully automated, reducing manual effort and ensuring queries run efficiently. This eliminates the need for manual performance tuning while maintaining query correctness.

note

For data sources and formats not supported by Autonomous Reflections, you can create [manual Reflections](/dremio-cloud/admin/performance/manual-reflections) to optimize query performance.

## What Is a Reflection?

A Reflection is a precomputed and optimized copy of a query result, designed to speed up query performance. It is derived from an existing table or view, known as its anchor.

Dremio's query optimizer uses Reflections to accelerate queries by avoiding the need to scan the original data. Instead of querying the raw source, Dremio automatically rewrites queries to use Reflections when they provide the necessary results, without requiring you to reference them directly.

When Dremio receives a query, it first determines whether any Reflections have at least one table in common with the tables and views referenced by the query. If any Reflections do, Dremio evaluates them to determine whether they satisfy the query. Then, if any Reflections do satisfy the query, Dremio generates a query plan that uses them.

Dremio then compares the cost of the plan to the cost of executing the query directly against the tables, and selects the plan with the lower cost. Finally, Dremio executes the selected query plan. Typically, plans that use one or more Reflections are less expensive than plans that run against raw data.

## How Workloads Are Autonomously Accelerated

Dremio autonomously creates Reflections to accelerate queries on existing views, queries with joins written directly on base tables (not referencing any views), and queries that summarize data, typically submitted by AI Agents and BI dashboards.

Reflections are automatically generated based on query patterns without user intervention. Dremio continuously collects metadata from user queries, and the Autonomous Algorithm runs daily at midnight UTC to analyze recent query patterns from the last 7 days and create Autonomous Reflections that accelerate frequent and expensive queries.

### Query Qualification

Only queries meeting the following criteria are considered:

1. Based on Iceberg tables, Uniform table, Parquet datasets, or views built on them. Queries referencing non-Iceberg or non-Parquet datasets, either directly or via a view, are excluded.
2. Execution time longer than one second.

Dremio may create system-managed views to anchor raw or aggregation Reflections that cannot be modified or referenced by users. Admins can drop these views, which also deletes the associated Reflection.

### Reflection Limits

Dremio can create up to 100 Reflections total, with a maximum of 10 new Reflections created per day. The actual number depends on query patterns.

## How Autonomous Reflections Are Maintained

Autonomous Reflections refresh automatically when source data changes:

* **Iceberg tables**: Refreshed when the table is modified via Dremio (triggered immediately) or other engines (Dremio polls tables every 10 seconds to detect changes).
* **Uniform tables**: Refreshed when the table is modified via Dremio (triggered immediately) or other engines (Dremio polls tables every 10 seconds to detect changes).
* **Parquet datasets**: Refreshed when metadata updates occur in Dremio.

**Refresh Engine:** When a project is created, Dremio automatically provisions a Small internal refresh engine dedicated to executing Autonomous Reflection refresh jobs. This ensures Reflections are always accurate and up-to-date without manual refresh. The engine automatically shuts down after 30 seconds of idle time to optimize resource usage and costs.

## Usage and Data Freshness

Dremio only uses Reflections in query plans when they refresh with the most recent data in tables on which they are based. If a Reflection is not yet refreshed, queries automatically fall back to the raw data source, ensuring query correctness is never compromised.

### Monitor Reflections

To view Autonomous Reflections created for your project and their metadata (including status, score, footprint, and queries accelerated), see [View Reflection Details](/dremio-cloud/admin/performance/manual-reflections/reflection-details).

To view the history of changes to Autonomous Reflections in the last 30 days:

1. Go to **Project Settings** > **Reflections**.
2. Click **History Log**.

## Remove Reflections

Autonomous Reflections can be removed in two ways:

1. **Automatic Removal** – When a Autonomous Reflection's score falls below the threshold, it is disabled for 7 days before being automatically dropped. Admins can view disabled Autonomous Reflections in the history log.
2. **Manual Removal** – Admins can manually drop Autonomous Reflections at any time. Autonomous Reflections cannot be modified by users. If an admin manually drops a Autonomous Reflection three times, Dremio will not recreate it for 90 days.

## Disable Reflections

Every project created in Dremio is automatically accelerated with Autonomous Reflections. To disable Autonomous Reflections for a project:

1. Go to **Project Settings** > **Preferences**.
2. Toggle the **Autonomous Reflections** setting to off.

## Related Topics

* [Data Product Fundamentals](https://university.dremio.com/course/data-product-fundamentals) – Enroll in this Dremio University course to learn more about Autonomous Reflections.

Was this page helpful?

* What Is a Reflection?
* How Workloads Are Autonomously Accelerated
  + Query Qualification
  + Reflection Limits
* How Autonomous Reflections Are Maintained
* Usage and Data Freshness
  + Monitor Reflections
* Remove Reflections
* Disable Reflections
* Related Topics

<div style="page-break-after: always;"></div>

# View Reflection Details | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/performance/manual-reflections/reflection-details

On this page

The Reflections page lists all raw and aggregation Reflections in Dremio.

To view this page, follow these steps:

1. In the Dremio console, hover over ![](/images/icons/settings.png) in the side navigation bar and select **Project Settings**.
2. Select **Reflections** in the project settings sidebar.

For any particular Reflection, the Reflections page presents information that answers these questions:

| Question | Column with the answer |
| --- | --- |
| What is the status of this Reflection? | Name |
| Is this a raw or aggregation Reflection? | Type |
| Which table or view is this Reflection defined on? | Dataset |
| How valuable is this Reflection? | Reflection Score |
| How Reflection was created and managed? | Mode |
| How can I see a list of the jobs that created and refreshed this Reflection? | Refresh Job History |
| How many times has the query planner chosen this Reflection? | Acceleration Count |
| How many times has the query planner considered using this Reflection? | Considered Count |
| How many times did the query planner match a query to this Reflection? | Matched Count |
| How do I find out how effective this Reflection is? | Acceleration Count |
| When was this Reflection last refreshed? | Last Refresh From Table |
| Is this Reflection being refreshed now? | Refresh Status |
| What type of refreshes are used for this Reflection? | Refresh Method |
| Are refreshes scheduled for this Reflection, or do they need to be triggered manually? | Refresh Status |
| How much time did the most recent refresh of this Reflection take? | Last Refresh Duration |
| How many records are in this Reflection? | Record Count |
| How much storage is this Reflection taking up? | Current Footprint |
| When does this Reflection expire? | Available Until |

## Columns

### Acceleration Count

Shows the number of times within the last 30 days that the query planner considered using a Reflection defined on a dataset referenced by a query, determined the Reflection could be used to satisfy the query, and chose to use the Reflection to satisfy the query.

If this count is low relative to the numbers in the **Considered Count** and **Matched Count**, the Reflection is not effective in reducing the execution times of queries on the dataset.

### Available Until

Shows the date and time when this Reflection expires, based on the refresh policy of the queried dataset.

If a Reflection is set to expire soon and you want to continue using it, you can take either of these actions:

* Change the expiration setting on the table which the Reflection is either directly or indirectly defined on. A Reflection is indirectly defined on a table when it is defined on a view that is derived from that table. When you change the setting by using this method, the change goes into effect after the next refresh.
* Change the expiration setting on the data source where the table is located.

For the steps, see [Set the Reflection Expiration Policy](/dremio-cloud/admin/performance/manual-reflections/reflection-refresh#set-the-reflection-expiration-policy).

### Mode

Shows how Reflection was created and managed.

* **autonomous**: Created and managed by Dremio
* **manual**: Created and managed by user

### Considered Count

Shows the number of queries, within the last 30 days, that referenced the dataset that a Reflection is defined on. Whenever a query references a dataset on which a Reflection is defined, the query planner considers whether to use the Reflection to help satisfy the query.

If the query planner determines that the Reflection can do that (that the Reflection matches the query), the query planner compares the Reflection to any others that might also be defined on the same dataset.

If the query planner does not determine this, it ignores the Reflection.

Reflections with high considered counts and no match counts are contributing to high logical planning times. Consider deleting them.

Reflections with a considered count of 0 should be removed. They are merely taking up storage and, during refreshes, resources on compute engines.

### Current Footprint

Shows the current size, in kilobytes, of a Reflection.

### Dataset

Shows the name of the table or view that a Reflection is defined on.

### Last Refresh Duration

Shows the length of time required for the most recent refresh of a Reflection.

### Last Refresh From Table

Shows the date and time that the Reflection data was last refreshed. If the refresh is running, failing, or disabled, the value is `12/31/1969 23:59:59`.

### Matched Count

Shows the number of times, within the last 30 days, that the query planner both considered a Reflection for satisfying a query and determined that the Reflection would in fact satisfy the query. However, the query planner might have decided to use a different Reflection that also matched the query. For example, a different query plan that did not include the Reflection might have had a lower cost.

This number does not show how many times the query planner used the Reflection to satisfy the query. For that number, see Acceleration Count.

If the matched count is high and the accelerating count is low, the query planner is more often deciding to use a different Reflection that also matches a query. In this case, consider deleting the Reflection.

### Name

Shows the name of the Reflection and its status. The tooltip on the icon represents a combination of the status of the Reflection (which you can filter on through the values in the **Acceleration Status** field above the list) and the value in the **Refresh Status** column.

### Record Count

Shows the number of records in the Reflection.

### Reflection Score

Shows the score for a Reflection on a scale of 0 (worst) to 100 (best). The score indicates the value that the Reflection provides to your workloads based on the jobs that have been executed in the last 7 days. Reflection scores are calculated once each day. Factors considered in the score include the number of jobs accelerated by the Reflection and the expected improvement in query run times due to the Reflection.

To help you interpret the scores, the scores have the following labels:

* **Good**: The score is more than 75.
* **Fair**: The score is 25 to 75.
* **Poor**: The score is less than 25.
* **New**: The score is blank because the Reflection was created within the past 24 hours.

note

If a Reflection's score is listed as **-**, the score needs to be recalculated due to an error or an upgraded instance.

### Refresh Job History

Opens a list of all of the jobs that created and refreshed a Reflection.

### Refresh Method

Shows which type of refresh was last used for a Reflection.

* **Full**: All of the data in the Reflection was replaced. The new data is based on the current data in the underlying dataset.
* **Incremental**:
  + For Reflections defined on Apache Iceberg tables: Either snapshot-based incremental refresh was used (if the changes were appends only) or partition-based incremental refresh was used (if the changes included DML operations).
  + For Reflections defined on Delta Lake tables: This value does not appear. Only full refreshes are supported for these Reflections.
  + For Reflections defined on all other tables: Data added to the underlying dataset since the last refresh of the Reflection was appended to the existing data in the Reflection.
* **None**: Incremental refreshes were selected in the settings for the table. However, Dremio has not confirmed that it is possible to refresh the Reflection incrementally. Applies only to Reflections that are not defined on Iceberg or Delta Lake tables.

For more information, see [Refresh Reflections](/dremio-cloud/admin/performance/manual-reflections/reflection-refresh).

### Refresh Status

Shows one of these values:

* **Manual**: Refreshes are not run on a schedule, but must be triggered manually. See [Trigger Reflection Refreshes](/dremio-cloud/admin/performance/manual-reflections/reflection-refresh#trigger-reflection-refreshes).
* **Pending**: If the Reflection depends on other Reflections, the refresh will begin after the refreshes of the other Reflections are finished.
* **Running**: The Reflection is currently being refreshed.
* **Scheduled**: Refreshes run on a schedule, but a refresh is not currently running.
* **Auto**: All of the Reflection’s underlying tables are in Iceberg format, and the Reflection automatically refreshes when new snapshots are created after an update to an underlying table, but a refresh is not currently running.
* **Failed**: Multiple attempts to refresh a Reflection have failed. You must disable and enable the Reflection to rebuild it and continue using it. Reflections in this state will not be considered to accelerate queries.

For more information, see [Refresh Reflections](/dremio-cloud/admin/performance/manual-reflections/reflection-refresh).

### Total Footprint

Shows the current size, in kilobytes, of all of the existing materializations of the Reflection. More than one materialization of a Reflection can exist at the same time, so that refreshes do not interrupt running queries that are being satisfied by the Reflection.

### Type

Shows whether the Reflection is a raw or aggregation Reflection.

Was this page helpful?

* Columns
  + Acceleration Count
  + Available Until
  + Mode
  + Considered Count
  + Current Footprint
  + Dataset
  + Last Refresh Duration
  + Last Refresh From Table
  + Matched Count
  + Name
  + Record Count
  + Reflection Score
  + Refresh Job History
  + Refresh Method
  + Refresh Status
  + Total Footprint
  + Type

<div style="page-break-after: always;"></div>

# Refresh Reflections | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/admin/performance/manual-reflections/reflection-refresh

On this page

The data in a Reflection can become stale and may need to be refreshed. Refreshing a Reflection triggers two updates:

* The data stored in the Apache Iceberg table for the Reflection is updated.
* The metadata that stores details about the Reflection is updated.

note

Dremio does not refresh the data that external Reflections are mapped to.

## Types of Reflection Refresh

How Reflections are refreshed depend on the format of the base table.

### Apache Iceberg Tables, Filesystem Sources, AWS Glue Sources, and Hive Sources

There are two methods that can be used to refresh Reflections that are defined either on Iceberg tables or on these types of datasets in filesystem, AWS Glue, and Hive sources:

* Parquet datasets in Filesystem sources (on S3, Azure Storage, Google Cloud Storage, or HDFS)
* Parquet datasets, Avro datasets, or non-transactional ORC datasets on AWS Glue or Hive (Hive 2 or Hive 3) sources

Iceberg tables in all supported file-system sources (Amazon S3, Azure Storage, Google Cloud Storage, and HDFS) and non-file-system sources (AWS Glue, Hive, and Nessie) can be refreshed with either of these methods.

* Incremental refreshes
* Full refreshes

#### Incremental Refreshes

There are two types of incremental refreshes:

* Incremental refreshes when changes to an anchor table are only append operations
* Incremental refreshes when changes to an anchor table include non-append operations

note

* Whether an incremental refresh can be performed depends on the outcome of an algorithm.
* The initial refresh of a Reflection is always a full refresh.

#### Incremental Refreshes When Changes to an Anchor Table Are Only Append Operations

note

Optimize operations on Iceberg tables are also supported for this type of incremental refresh.

This type of incremental refresh is used only when the changes to the anchor table are appends and do not include updates or deletes. There are two cases to consider:

* When a Reflection is defined on one anchor table

  When a Reflection is defined on an anchor table or on a view that is defined on one anchor table, an incremental refresh is based on the differences between the current snapshot of the anchor table and the snapshot at the time of the last refresh.
* When a Reflection is defined on a view that joins two or more anchor tables

  When a Reflection is defined on a view that joins two or more anchor tables, whether an incremental refresh can be performed depends on how many anchor tables have changed since the last refresh of the Reflection:

  + If just one of the anchor tables has changed since the last refresh, an incremental refresh can be performed. It is based on the differences between the current snapshot of the one changed anchor table and the snapshot at the time of the last refresh.
  + If two or more tables have been refreshed since the last refresh, then a full refresh is used to refresh the Reflection.

#### Incremental Refreshes When Changes to an Anchor Table Include Non-append Operations

For Iceberg tables, this type of incremental refresh is used when the changes are DML operations that delete or modify the data (UPDATE, DELETE, etc.) made either through the Copy-on-Write (COW) or the Merge-on-Read (MOR) storage mechanism. For more information about COW and MOR, see [Row-Level Changes on the Lakehouse: Copy-On-Write vs. Merge-On-Read in Apache Iceberg](https://www.dremio.com/blog/row-level-changes-on-the-lakehouse-copy-on-write-vs-merge-on-read-in-apache-iceberg/).

For sources in filesystems or AWS Glue, non-append operations can include, for example:

* In filesystem sources, files being deleted from Parquet datasets
* In AWS Glue sources, DML-equivalent operations being performed on Parquet datasets, Avro datasets, or non-transactional ORC datasets

Both the anchor table and the Reflection must be partitioned, and the partition transforms that they use must be compatible.

There are two cases to consider:

* When a Reflection is defined on one anchor table

  When a Reflection is defined on an anchor table or on a view that is defined on one anchor table, an incremental refresh is based on Iceberg metadata that is used to identify modified partitions and to restrict the scope of the refresh to only those partitions.
* When a Reflection is defined on a view that joins two or more anchor tables

  When a Reflection is defined on a view that joins two or more anchor tables, whether an incremental refresh can be performed depends on how many anchor tables have changed since the last refresh of the Reflection:

  + If just one of the anchor tables has changed since the last refresh, an incremental refresh can be performed. It is based on Iceberg metadata that is used to identify modified partitions and to restrict the scope of the refresh to only those partitions.
  + If two or more tables have been refreshed since the last refresh, then a full refresh is used to refresh the Reflection.

note

Dremio uses Iceberg tables to store metadata for filesystem and AWS Glue sources.

For information about partitioning Reflections and applying partition transforms, see the section [Horizontally Partition Reflections that Have Many Rows](/dremio-cloud/help-support/well-architected-framework/operational-excellence/#horizontally-partition-reflections-that-have-many-rows).

For information about partitioning Reflections in ways that are compatible with the partitioning of anchor tables, see [Partition Reflections to Allow for Partition-Based Incremental Refreshes](/dremio-cloud/help-support/well-architected-framework/operational-excellence/#partition-reflections-to-allow-for-partition-based-incremental-refreshes).

#### Full Refreshes

In a full refresh, a Reflection is dropped, recreated, and loaded.

note

* Whether a full refresh is performed depends on the outcome of an algorithm.
* The initial refresh of a Reflection is always a full refresh.

#### Algorithm for Determining Whether an Incremental or a Full Refresh Is Used

The following algorithm determines which refresh method is used:

1. If the Reflection has never been refreshed, then a full refresh is performed.
2. If the Reflection is created from a view that uses nested group-bys, unions, window functions, or joins other than inner or cross joins, then a full refresh is performed.
3. If the Reflection is created from a view that joins two or more anchor tables and more than one anchor table has changed since the previous refresh, then a full refresh is performed.
4. If the Reflection is based on a view and the changed anchor table is used multiple times in that view, then a full refresh is performed.
5. If the changes to the anchor table are only appends, then an incremental refresh based on table snapshots is performed.
6. If the changes to the anchor table include non-append operations, then the compatibility of the partitions of the anchor table and the partitions of the Reflection is checked:
   * If the partitions of the anchor table and the partitions of the Reflection are not compatible, or if either the anchor table or the Reflection is not partitioned, then a full refresh is performed.
   * If the partition scheme of the anchor table has been changed since the last refresh to be incompatible with the partitioning scheme of a Reflection, and if changes have occurred to data belonging to a prior partition scheme or the new partition scheme, then a full refresh is performed.
     To avoid a full refresh when these two conditions hold, update the partition scheme for Reflection to match the partition scheme for the table. You do so in the **Advanced** view of the Reflection editor or through the `ALTER DATASET` SQL command.
   * If the partitions of the anchor table and the partitions of the Reflection are compatible, then an incremental refresh is performed.

Because this algorithm is used to determine which type of refresh to perform, you do not select a type of refresh for Reflections in the settings of the anchor table.

However, no data is read in the `REFRESH REFLECTION` job for Reflections that are dependent only on Iceberg, Parquet, Avro, non-transactional ORC datasets, or other Reflections and that have no new data since the last refresh based on the table snapshots. Instead, a "no-op" Reflection refresh is planned and a materialization is created, eliminating redundancy and minimizing the cost of a full or incremental Reflection refresh.

### Delta Lake tables

Only full refreshes are supported. In a full refresh, the Reflection being refreshed is dropped, recreated, and loaded.

### All Other Tables

* **Incremental refreshes**

  Dremio appends data to the existing data for a Reflection. Incremental refreshes are faster than full refreshes for large Reflections, and are appropriate for Reflections that are defined on tables that are not partitioned.

  There are two ways in which Dremio can identify new records:

  + **For directory datasets in file-based data sources like S3 and HDFS:**
    Dremio can automatically identify new files in the directory that were added after the prior refresh.
  + **For all other datasets (such as datasets in relational or NoSQL databases):**
    An administrator specifies a strictly monotonically increasing field, such as an auto-incrementing key, that must be of type BigInt, Int, Timestamp, Date, Varchar, Float, Double, or Decimal. This allows Dremio to find and fetch the records that have been created since the last time the acceleration was incrementally refreshed.

  caution

  Use incremental refreshes only for Reflections that are based on tables and views that are appended to. If records can be updated or deleted in a table or view, use full refreshes for the Reflections that are based on that table or view.
* **Full refreshes**

  In a full refresh, the Reflection being refreshed is dropped, recreated, and loaded.

  Full refreshes are always used in these three cases:

  + A Reflection is partitioned on one or more fields.
  + A Reflection is created on a table that was promoted from a file, rather than from a folder, or is created on a view that is based on such a table.
  + A Reflection is created from a view that uses nested group-bys, joins, unions, or window functions.

## Specify the Reflection Refresh Policy

In the settings for a data source, you specify the refresh policy for refreshes of all Reflections that are on the tables in that data source. The default policy is period-based, with one hour between each refresh. If you select a schedule policy, the default is every day at 8:00 a.m. (UTC).

In the settings for a table that is not in the Iceberg or Delta Lake format, you can specify the type of refresh to use for all Reflections that are ultimately derived from the table. The default refresh type is **Full refresh**.

For tables in all supported table formats, you can specify a refresh policy for Reflection refreshes that overrides the policy specified in the settings for the table's data source. The default policy is the schedule set at the source of the table.

To set the refresh policy on a data source:

1. In the Dremio console, right-click a data lake or external source.
2. Select **Edit Details**.
3. In the sidebar of the Edit Source window, select **Reflection Refresh**.
4. When you are done making your selections, click **Save**. Your changes go into effect immediately.

To edit the refresh policy on a table:

1. Locate the table.
2. Hover over the row in which it appears and click ![The Settings icon](/images/cloud/settings-icon.png "The Settings icon") to the right.
3. Select **Reflection Refresh** in the dataset settings sidebar.
4. When you are done making your selections, click **Save**. Your changes go into effect immediately.

### Types of Refresh Policies

Datasets and sources can set Reflections to refresh according to the following policy types:

| Refresh policy type | Description |
| --- | --- |
| Never | Reflections are not refreshed. |
| Period (default) | Reflections refresh at the specified number of hours, days, or weeks. The default refresh period is one hour. |
| Schedule | Reflections refresh at a specific time on the specified days of the week, in UTC. The default is every day at 8:00 a.m. (UTC). |
| Auto refresh when Iceberg table data changes | Reflections automatically refresh for underlying Iceberg tables whenever new updates occur. Reflections under this policy type are known as Live Reflections. Live Reflections are also updated based on the minimum refresh frequency defined by the source-level policy. This refresh policy is only available for data sources that support the Iceberg table format. |

## Set the Reflection Expiration Policy

Rather than delete a Reflection manually, you can specify how long you want Dremio to retain the Reflection before deleting it automatically.

note

Dremio does not allow expiration policies to be set on external Reflections or Reflections that automatically refresh when Iceberg data changes according to the refresh policy.

To set the expiration policy for all Reflections derived from tables in a data source:

1. Right-click a data lake or external source.
2. Select **Edit Details**.
3. Select **Reflection Refresh** in the edit source sidebar.
4. After making your changes, click **Save**. The changes take effect on the next refresh.

To set the expiration policy on Reflections derived from a particular table:

note

The table must be based on more than one file.

1. Locate a table.
2. Click the ![The Settings icon](/images/cloud/settings-icon.png "The Settings icon") to its right.
3. Select **Reflection Refresh** in the dataset settings sidebar.
4. After making your changes, click **Save**. The changes take effect on the next refresh.

## View the Reflection Refresh History

You can find out whether a refresh job for a Reflection has run, and how many times refresh jobs for a Reflection have been run.

To view the refresh history:

1. In the Dremio console, go to the catalog or folder that lists the table or view from which the Reflection was created.
2. Hover over the row for the table or view.
3. In the **Actions** field, click ![The Settings icon](/images/cloud/settings-icon.png "The Settings icon").
4. Select **Reflections** in the dataset settings sidebar.
5. Click **History** in the heading for the Reflection.

The Jobs page is opened with the ID of the Reflection in the search box, and only jobs related to that ID are listed.

When a Reflection is refreshed, Dremio runs a single job with two steps:

* The first step writes the query results as a materialization to the distributed acceleration storage by running a `REFRESH REFLECTION` command.
* The second step registers the materialization table and its metadata with the catalog so that the query optimizer can find the Reflection's definition and structure.

The following screenshot shows the `REFRESH REFLECTION` command used to refresh the Reflection named `Super-duper reflection`:

![Reflection refresh job listed on the Jobs page in the Dremio console](/images/sw_reflection_creation_command.png "Reflection refresh job listed on the Jobs page")

The Reflection refresh is listed as a single job on the Jobs page, as shown in the example below:

![Reflection refresh job listed on the Jobs page in the Dremio console](/images/sw_reflection_creation_single_job.png "Reflection refresh job listed on the Jobs page")

To find out which type of refresh was performed:

1. Click the ID of the job that ran the `REFRESH REFLECTION` command.
2. Click the **Raw Profile** tab.
3. Click the **Planning** tab.
4. Scroll down to the **Refresh Decision** section.

## Retry a Reflection Refresh Policy

When a Reflection refresh job fails, Dremio retries the refresh according to a uniform policy. This policy is designed to balance resource consumption with the need to keep Reflection data up to date. It prioritizes newly failed Reflections to reduce excessive retries on persistent failures and helps ensure that Reflection data does not become overly stale.

After a refresh failure, Dremio's default is to repeat the refresh attempt at exponential intervals up to 4 hours: 1 minute, 2 minutes, 5 minutes, 15 minutes, 30 minutes, 1 hour, 2 hours, and 4 hours. Then, Dremio continues trying to refresh the Reflection every 4 hours.

There are two optimizations for special cases:

* **Long-running refresh jobs**: The backoff interval will never be shorter than the last successful duration.
* **Small maximum retry attempts**: At least one 4-hour backoff attempt is guaranteed to ensure meaningful coverage of the retry policy.

Dremio stops retrying after 24 attempts, which typically takes about 71 hours and 52 minutes, or when the 72-hour retry window is reached, whichever comes first.

To configure a different maximum number of retry attempts for Reflection refreshes than Dremio's default of 24 retries:

1. Click ![The Settings icon](/images/cloud/green-settings-icon.png "The Settings icon") in the left navbar.
2. Select **Reflections** in the left sidebar.
3. On the Reflections page, click ![The Settings icon](/images/cloud/settings-icon.png "The Settings icon") in the top-right corner and select **Acceleration Settings**.
4. In the field next to **Maximum attempts for Reflection job failures**, specify the maximum number of retries.
5. Click **Save**. The change goes into effect immediately.

Dremio applies the retry policy after a refresh failure for all types of Reflection refreshes, no matter whether the refresh was triggered or set by a refresh policy.

## Trigger Reflection Refreshes

You can click a button to start the refresh of all of the Reflections that are defined on a table or on views derived from that table.

To trigger a refresh manually:

1. Locate the table.
2. Hover over the row in which it appears and click ![The Settings icon](/images/cloud/settings-icon.png "The Settings icon") to the right.
3. In the sidebar of the Dataset Settings window, click **Reflection Refresh**.
4. Click **Refresh Now**. The message "All dependent Reflections will be refreshed." appears at the top of the screen.
5. Click **Save**.

You can refresh Reflections by using the Reflection API, the Catalog API, and the SQL commands [`ALTER TABLE`](/dremio-cloud/sql/commands/alter-table) and [`ALTER VIEW`](/dremio-cloud/sql/commands/alter-view).

* With the Reflection API, you specify the ID of a Reflection. See [Refresh a Reflection](/dremio-cloud/api/reflection/#refresh-a-reflection).
* With the Catalog API, you specify the ID of a table or view that the Reflections are defined on. See [Refresh the Reflections on a Table](/dremio-cloud/api/catalog/table#refresh-the-reflections-on-a-table) and [Refresh the Reflections on a View](/dremio-cloud/api/catalog/view#refresh-the-reflections-on-a-view).
* With the [`ALTER TABLE`](/dremio-cloud/sql/commands/alter-table) and [`ALTER VIEW`](/dremio-cloud/sql/commands/alter-view) commands, you specify the path and name of the table or view that the Reflections are defined on.

The refresh action follows this logic for the Reflection API:

* If the Reflection is defined on a view, the action refreshes all Reflections that are defined on the tables and on downstream/dependent views that the anchor view is itself defined on.
* If the Reflection is defined on a table, the action refreshes the Reflections that are defined on the table and all Reflections that are defined on the downstream/dependent views of the anchor table.

The refresh action follows similar logic for the Catalog API and the SQL commands:

* If the action is started on a view, it refreshes all Reflections that are defined on the tables and on downstream/dependent views that the view is itself defined on.
* If the action is started on a table, it refreshes the Reflections that are defined on the table and all Reflections that are defined on the downstream/dependent views of the anchor table.

For example, suppose that you had the following tables and views, with Reflections R1 through R5 defined on them:

```
         View2(R5)  
         /       \  
     View1(R3) Table3(R4)  
    /       \  
Table1(R1) Table2(R2)
```

* Refreshing Reflection R5 through the API also refreshes R1, R2, R3, and R4.
* Refreshing Reflection R4 through the API also refreshes R5.
* Refreshing Reflection R3 through the API also refreshes R1, R2, and R5.
* Refreshing Reflection R2 through the API also refreshes R3 and R5.
* Refreshing Reflection R1 through the API also refreshes R3 and R5.

## Obtain Reflection IDs

You will need one or more Reflection IDs for some of the Reflection hints. Reflection IDs can be found in three places: the Acceleration section of the raw profile of the job that ran a query using the Reflection, the [`SYS.PROJECT.REFLECTIONS`](/dremio-cloud/sql/system-tables/reflections) system table, and the Reflection summary objects that you retrieve with the Reflection API.

To find the ID of a Reflection in Acceleration section of the raw profile of job that ran a query that used the Reflection:

1. In the Dremio console, click ![The Jobs icon](/images/jobs-icon.png "The Jobs icon") in the side navigation bar.
2. In the list of jobs, locate the job that ran the query. If the query was satisfied by a Reflection, ![This is the icon that indicates a Reflection was used.](/images/icons/reflections.png "Reflections icon") appears after the name of the user who ran the query.
3. Click the ID of the job.
4. Click **Raw Profile** at the top of the page.
5. Click the **Acceleration** tab.
6. In the Reflection Outcome section, locate the ID of the Reflection.

  

To find the ID of a Reflection in the `SYS.PROJECT.REFLECTIONS` system table:

1. In the Dremio console, click ![The SQL Runner icon](/images/sql-runner-icon.png "The SQL Runner icon") in the left navbar.
2. Copy this query and paste it into the SQL editor:

   Query for listing info about all existing Reflections

   ```
   SELECT * FROM SYS.PROJECT.REFLECTIONS
   ```
3. Sort the results on the `dataset_name` column.
4. In the `dataset_name` column, locate the name of the dataset that the Reflection was defined on.
5. Scroll the table to the right to look through the display columns, dimensions, measures, sort columns, and partition columns to find the combination of attributes that define the Reflection.
6. Scroll the table all the way to the left to find the ID of the Reflection.

  

To find the ID of a Reflection by using REST APIs:

1. Obtain the ID of the table or view that the Reflection was defined on by using retrieving either the [table](/dremio-cloud/api/catalog/table#retrieve-a-table-by-path) or [view](/dremio-cloud/api/catalog/view#retrieve-a-view-by-path) by its path.
2. [Use the Reflections API to retrieve a list of all of the Reflections that are defined on the table or view](/dremio-cloud/api/reflection/#retrieve-all-reflections-for-a-dataset).
3. In the response, locate the Reflection by its combination of attributes.
4. Copy the Reflection's ID.

Was this page helpful?

* Types of Reflection Refresh
  + Apache Iceberg Tables, Filesystem Sources, AWS Glue Sources, and Hive Sources
  + Delta Lake tables
  + All Other Tables
* Specify the Reflection Refresh Policy
  + Types of Refresh Policies
* Set the Reflection Expiration Policy
* View the Reflection Refresh History
* Retry a Reflection Refresh Policy
* Trigger Reflection Refreshes
* Obtain Reflection IDs

<div style="page-break-after: always;"></div>

