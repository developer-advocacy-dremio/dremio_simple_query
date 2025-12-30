# Dremio Software - Admin



---

# Source: https://docs.dremio.com/current/admin/

Version: current [26.x]

# Administration

This section includes administration topics.
If you're just getting started, we suggest using one of the guides under [Getting Started](/current/get-started/) for one of our platforms.

* [Dremio on Kubernetes](/current/admin/admin-dremio-kubernetes/)
* [Licensing](/current/admin/licensing/)
* [Service Telemetry](/current/admin/service-telemetry-kubernetes/)
* [Automated Backup](/current/admin/automated-backups)
* [Managing Job Workloads](/current/admin/workloads/)
* [Monitoring](/current/admin/monitoring/)
* [Backup and Restore for Open Catalog](/current/admin/open-catalog-backing-store-backuprestore)
* [Configure Model Providers](/current/admin/model-providers)

Was this page helpful?

[Previous

Security and Compliance](/current/security/)[Next

Dremio on Kubernetes](/current/admin/admin-dremio-kubernetes/)

---

# Source: https://docs.dremio.com/current/admin/admin-dremio-kubernetes/

Version: current [26.x]

On this page

# Administer Dremio on Kubernetes

This section includes topics about administering Dremio on supported Kubernetes environments, including information about monitoring logs, scaling pods, changing configurations, performing basic administrative tasks such as backing up, restoring, cleaning, and upgrading Dremio.

### Monitoring Logs and Usage

Monitoring the cluster's resource usage (e.g., heap and direct memory, CPU, disk I/O, etc.) is crucial to maintaining long-term stability as the system scales. For this reason, Dremio recommends setting up a monitoring stack, such as Prometheus and Grafana. For a detailed setup tutorial and an overview of which metrics to track, see [Dremio Monitoring in Kubernetes](https://www.dremio.com/wp-content/uploads/2024/01/Dremio-Monitoring-in-Kubernetes.pdf). For more information, see this PDF guide on the [Dremio Enterprise Edition (Software) Shared Responsibility Model](/assets/files/Dremio-Enterprise-Edition-Shared-Responsibility-Model-58e2fdb565de30a7b7862f2c4d094ca4.pdf).

### Managing Workloads

Most workloads can be handled with a Large (8 executors) or X-Large (12 executors) engine, each with 32 CPUs per executor. Larger engine sizes may be required for certain workloads. Over-parallelization of queries can cause performance degradation. Thus, packing workloads of all shapes or sizes onto a few very large engines is ill-advised. Workloads should be divided into high-cost and low-cost queries, and dedicated queues should be configured for tasks such as Reflections, metadata refresh, and table optimization jobs. These can then be divided between right-sized engines. For more information, see [Dremio's Well-Architected Framework](/current/help-support/well-architected-framework/).

### Changing Your Configuration

If you need to update your configuration, you can do so after the installation by editing the configuration files and then upgrading using an upgrade command, for example:

```
helm upgrade <chart release name> oci://quay.io/dremio/dremio-helm -f <your-local-path>/values-overrides.yaml --version <helm-chart-version>
```

The upgrade process pushes your changes to all pods in your Kubernetes cluster and restarts the pods.

For example, to permanently change the resources of your coordinator pod:

1. Edit the `values-overrides.yaml` file and change the resources specified for the coordinator. In this example, `memory` is `32Gi` and `cpu` is `8`.

   ```
   coordinator:  
       resources:  
         limits:  
           memory: 32Gi  
         requests:  
           cpu: 8  
           memory: 32Gi
   ```
2. Run the upgrade command. Replacing the template values:

   ```
   helm upgrade <chart release name> oci://quay.io/dremio/dremio-helm -f <your-local-path>/values-overrides.yaml --version <helm-chart-version>
   ```

   note

   If the command takes longer than a few minutes to finish, check the status of the pods with the `kubectl get pods` command. If the pods are pending scheduling due to limited memory or CPU, adjust the values you specified for the properties in the `values-overrides.yaml` file or add more resources to your Kubernetes cluster.

### Using Support Keys

Use [support keys](/current/help-support/support-settings/#support-keys) only when instructed by Dremio Support. If misused, they can alter the application's behavior and lead to unexpected failures.

### Using the Dremio Admin CLI on Kubernetes

The [Dremio Admin CLI](/current/reference/admin-cli/) is the mechanism to back up, restore, add internal users, etc. For more information on the various commands the see CLI reference previously linked. In order to run the CLI commands you need to access either the `dremio-master-0` or `dremio-admin` pod. This requires the use of the `kubectl` command line tool and access to the Kubernetes cluster and namespace where Dremio is deployed.

note

The term `master` is a legacy label used in this command. We now refer to this as the main coordinator pod.

Some CLI commands like [Back Up Dremio](/current/reference/admin-cli/backup) require Dremio to be **online**. This means Dremio must be deployed normally per [Deploying Dremio to Kubernetes](/current/deploy-dremio/deploy-on-kubernetes). When inspecting Dremio's pods, `dremio-master-0` must be present and `RUNNING` to be considered **online**.

Some CLI commands like [Clean](/current/reference/admin-cli/metadata-cleanup) require Dremio to be **offline**. To use them, Dremio must be deployed and running in admin mode. If not, you must redeploy Dremio in admin mode. The requirements section for each command will note whether Dremio should be online or offline. If it is not mentioned, then the command will work in either case.

To redeploy Dremio in admin mode, you must run a `helm upgrade` command where the `DremioAdmin` flag is set to `true`. Here is a templated example command:

```
helm upgrade <chart-release-name> oci://quay.io/dremio/dremio-helm -f <your-local-path>/values-overrides.yaml --version <helm-chart-version> --set DremioAdmin=true
```

This command will cause the shutdown of the Coordinators and Executors. In their place will start the `dremio-admin` pod. Crucially, this pod will mount the `dremio-master-0` volume allowing for operations on the constituent KV store.

To get command line access to the `dremio-master-0`, `dremio-admin`, or any pod for that matter, you would use the `kubectl exec` command. Here is an example using the `-it` option for interactive, and the `-- bash` option to enter a bash session:

```
kubectl exec -it <pod-name> -- bash
```

Once you've entered the pod, you can run typical shell commands to explore the file system and execute commands. For more information, see [kubectl exec](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec/).
The `dremio-admin` utility is within the `/opt/dremio/bin` directory of both the main and admin pods and can be used to execute the various [Dremio Admin CLI](/current/reference/admin-cli/) commands.

To exit Dremio admin mode and restart the normal service, you must redeploy Dremio again using the command above and setting only `DremioAdmin=false`.

Was this page helpful?

[Previous

Administration](/current/admin/)[Next

Upgrade Dremio](/current/admin/admin-dremio-kubernetes/upgrade)

* Monitoring Logs and Usage
* Managing Workloads
* Changing Your Configuration
* Using Support Keys
* Using the Dremio Admin CLI on Kubernetes

---

# Source: https://docs.dremio.com/current/admin/licensing/

Version: current [26.x]

On this page

# Licensing

As of Dremio 26.0, a new licensing model has been introduced, affecting Dremio deployments on Kubernetes. Understanding these requirements is crucial for ensuring a smooth deployment and uninterrupted operation.

## License Key Requirement

A valid license key is mandatory for deploying a Dremio cluster on Kubernetes. Without it, the cluster will fail to start. This requirement applies to both new installations and upgrades.

Additionally, Dremio's telemetry functionality relies on a valid license key. Without one, telemetry data will not be accurately reported, potentially affecting system monitoring and analytics. For more information about telemetry, see [Service Telemetry for Kubernetes Deployments](/current/admin/service-telemetry-kubernetes/).

tip

Do you know you can obtain a **free trial license key** for Dremio? Learn more about it in [Dremio Enterprise Edition Free Trial](/current/admin/licensing/free-trial/).

## Obtain a License Key

Acquiring a license key for Dremio 26.0+ is a fully automated process where customers generate their own license keys through the [Dremio Support Portal](https://support.dremio.com/hc/en-us), without needing to contact Dremio Support or Sales. The process is self-service:

1. Go to the [Dremio Support Portal](https://support.dremio.com/hc/en-us) and click `Submit a request`. Create a support ticket and, in the **Subject** field, be sure to include "License Request". This helps us identify and route your request quickly.
2. After the support ticket is created, you’ll receive an automated response message asking you to confirm whether you are requesting a new or replacement license specifically for deploying Dremio 26.0+ on Kubernetes. Reply to confirm. This step is important to ensure your ticket is routed correctly.

Once you confirm your request, you’ll automatically receive the appropriate license file required to deploy your Dremio cluster. No further action is needed unless Dremio Support or Sales follows up with additional questions.

![](/images/licensing-support-portal.jpeg)

When you download your license file, it should look like this:

![](/images/licensing-license-file.png)

## Use Your License Key for Kubernetes Deployment

To ensure your Dremio cluster starts up correctly, follow these steps to apply your license key:

1. Open the license file you have obtained in the support ticket (see the section above on How to Obtain a License Key), and copy the license key string.
2. Go to your Kubernetes deployment configuration file and paste the license key string to the `license:` property enclosed in double quotation marks (`" "`). For more information about the configuration file, see [Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/).

   ![](/images/licensing-configured-license.png)

With the license key set in your configuration file, you can proceed to [Deploying Dremio to Kubernetes](/current/deploy-dremio/deploy-on-kubernetes).

## Verify Your License

During startup, Dremio will validate the license key using its internal mechanisms (connectivity to the Internet is not required). If the key is missing, incorrect, expired, or invalid, the cluster will not start, and an error message will be logged to indicate the issue. If the license is valid, the cluster will start as expected.

## Troubleshooting Tips

If you encounter any verification issues, do the following:

* Double-check that the license key was copied correctly (no extra spaces or line breaks) and is enclosed in double-quotation marks (`" "`).
* Review the Dremio logs for license-related error messages.
* Reach out via your support ticket for further assistance.

Was this page helpful?

[Previous

Upgrade Dremio](/current/admin/admin-dremio-kubernetes/upgrade)[Next

Enterprise Edition Free Trial](/current/admin/licensing/free-trial)

* License Key Requirement
* Obtain a License Key
* Use Your License Key for Kubernetes Deployment
* Verify Your License
* Troubleshooting Tips

---

# Source: https://docs.dremio.com/current/admin/billing/

Version: current [26.x]

On this page

# Dremio Billing on Kubernetes

Dremio on Kubernetes uses a consumption-based billing model where costs are calculated based on your actual [usage](/current/admin/billing/usage/) of compute resources, measured in Dremio Consumption Units (DCUs). Billing is managed through [Orb](https://portal.withorb.com/), which tracks your DCUs and handles invoicing on a monthly basis (the billing period starts at 00:00:00 on the first day of the month and ends at 23:59:59 on the last day of the month).

## Prequisites

* Have an account in [Orb](https://portal.withorb.com/). To get access, contact Dremio Support.
* [Service Telemetry](/current/admin/service-telemetry-kubernetes/) must be enabled to transmit your usage data to Orb.

## View Your Billing

To access your billing information:

1. In your browser, navigate to [Orb](https://portal.withorb.com/).
2. Log in to your Orb account.

Once logged in, you will see a dashboard with your account information, unpaid invoices, and the DCUs for the current billing period. You will also have access to your invoice history, where you can view and download the details of each invoice.

Was this page helpful?

[Previous

Enterprise Edition Free Trial](/current/admin/licensing/free-trial)[Next

Usage](/current/admin/billing/usage)

* Prequisites
* View Your Billing

---

# Source: https://docs.dremio.com/current/admin/model-providers/

Version: current [26.x]

On this page

# Configure Model Providers Enterprise

Starting with Dremio Software 26.1, you can configure model providers for AI functionality when deploying Dremio clusters on Kubernetes. After you configure at least one model provider, you must set a default model provider and optionally set an allowlist of available models. Dremio uses this default provider for all Dremio's AI Agent interactions and whereas the allowlist models can be used by anyone writing AI functions.

## Supported Model Providers

Dremio supports configuration of the following model providers and models. Dremio recommends using enterprise-grade reasoning models for the best performance and experience.

| Category | Models | Connection Method(s) |
| --- | --- | --- |
| **OpenAI** | * gpt-5-2025-08-07 * gpt-5-mini-2025-08-07 * gpt-5-nano-2025-08-07 * gpt-4.1-2025-04-14 * gpt-4o-2024-11-20 * gpt-4-turbo-2024-04-09 * gpt-4.1-mini-2025-04-14 * o3-mini-2025-01-31 * o4-mini-2025-04-16 * o3-2025-04-16 | * Access Key |
| **Anthropic** | * claude-sonnet-4-5-20250929 * claude-opus-4-1-20250805 * claude-opus-4-20250514 * claude-sonnet-4-20250514 | * Access Key |
| **Google Gemini** | * gemini-2.5-pro | * Access Key |
| **AWS Bedrock** | * specify Model ID(s) * [AWS Bedrock Supported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) | * Access Key * IAM Role |
| **Azure OpenAI** | * specify Deployment Name(s) * [Azure Supported Models](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cstandard-chat-completions%2Cglobal-standard&pivots=azure-openai#azure-openai-in-azure-ai-foundry-models) | Combination of  1. Resource Name 2. Directory ID 3. Application ID 4. Client Secret Value |

## Add Model Provider

For steps on adding an AWS Bedrock model provider, see [Configure AWS Bedrock as a Model Provider](/current/admin/model-providers/aws-bedrock).

For all other model providers, follow these steps to add a model provider in the Dremio console:

1. Click ![This is the Settings icon.](/images/green-settings-icon.png "The Settings icon.") in the side navigation bar to go to the Settings page.
2. Select **Preferences** in the settings sidebar.
3. Enable the **AI Features** flag.
4. Click **Add model provider**.

## Default Model Provider

To delete the model provider, you must assign a new default unless you are deleting the last available model provider. To update the default model provider to a new one, you must have MODIFY privilege on both the current default and the new proposed default model provider.

Was this page helpful?

[Previous

Usage](/current/admin/billing/usage)[Next

AWS Bedrock](/current/admin/model-providers/aws-bedrock)

* Supported Model Providers
* Add Model Provider
* Default Model Provider

---

# Source: https://docs.dremio.com/current/admin/service-telemetry-kubernetes

Version: current [26.x]

On this page

# Service Telemetry for Kubernetes Deployments Enterprise

As of Dremio 26.0, enterprise customers deploying Dremio clusters on Kubernetes will automatically transmit telemetry data back to Dremio's corporate endpoint. This telemetry provides valuable insights into system performance and health, and is also used in the calculations for usage-based [billing](/current/admin/billing/). Telemetry can be disabled through configuration; however, this is not considered a best practice because telemetry helps Dremio ensure stability and timely support.

## Telemetry Data Collection

Dremio's telemetry data collection is strictly limited to operational and performance metrics. These metrics provide visibility into various components and services, ensuring optimal performance and reliability.
Importantly, no customer content (e.g., business data) or user-entered information is transmitted. If you would like to develop a deeper understanding of the metrics transmitted and their contents, you can set up your own internal monitoring of your Dremio cluster by following the steps in [Monitoring Dremio Nodes](https://docs.dremio.com/current/admin/monitoring/dremio-nodes).

The collected telemetry data is categorized as follows:

| Category | Description |
| --- | --- |
| **Application Metrics** | These metrics provide insights into the usage and performance of objects within a Dremio deployment, including:  * Number of queries, Reflections, sources, and views. * Success and failure rates of queries. * Success and failure rates of Reflection and source refresh operations. |
| **Java Metrics** | These metrics capture internal Java Virtual Machine (JVM) performance indicators from containers running the Dremio application, such as:  * Number of active threads. * Memory allocation and usage. * Garbage collection activity and pauses. |
| **Service Metrics** | These metrics measure the health of core components supporting Dremio's execution and coordination services, including:  * KVstore performance. * Zookeeper availability and network health. |
| **Kubernetes Metrics** | These metrics provide insight into container and pod behavior for all containers in a Dremio deployment, including:  * CPU, memory, and storage requests. * Container restarts and readiness. * StatefulSet desired and current pod count. |

## Telemetry Transmission Requirements

Telemetry transmission to Dremio follows the [Dremio Subscription Agreement](https://www.dremio.com/legal/dremio-subscription-agreement/).

### Network Requirements for Telemetry Transmission

To ensure successful telemetry transmission, the following network configurations must be in place:

* Your network must allow traffic egress to Dremio's endpoint `observability.dremio.com`.
* Dremio's OpenTelemetry collectors use port 443 for secure data transmission via TLS.

### Setting Up a Proxy

If traffic egresses to the endpoint and the port is restricted, a proxy can be configured to enable telemetry transmission:

1. Edit your `.yaml` configuration file to deploy Dremio to Kubernetes. For more information, refer to [Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/).
2. Add your proxy configuration values to the `.yaml` file using the following syntax:

   * HTTPS Proxy (Recommended)
   * HTTP Proxy

   ```
   telemetry:  
     extraEnvs: []  
       - name: HTTPS_PROXY  
         value: https://proxy.example.com:443
   ```

   ```
   telemetry:  
     extraEnvs: []  
       - name: HTTP_PROXY  
         value: http://proxy.example.com:3128
   ```

## Troubleshooting or Support

For troubleshooting or support, please contact your account representative or Dremio Support.

## Related Topics

* [Licensing](/current/admin/licensing/) - Learn more about Dremio's licensing and telemetry.
* [Billing](/current/admin/billing/) - Learn more about Dremio's billing and usage data.

Was this page helpful?

[Previous

AWS Bedrock](/current/admin/model-providers/aws-bedrock)[Next

Automated Backup](/current/admin/automated-backups)

* Telemetry Data Collection
* Telemetry Transmission Requirements
  + Network Requirements for Telemetry Transmission
  + Setting Up a Proxy
* Troubleshooting or Support
* Related Topics

---

# Source: https://docs.dremio.com/current/admin/automated-backups

Version: current [26.x]

# Automated Backup Enterprise

Backups are crucial to restoring Dremio's state in case of a critical failure, so we recommend creating regular backups to minimize loss from the restore point. Use Dremio's automated backups to create backups on a schedule and output the backups to a folder in distributed storage.

To enable automated backups, use the `dremio.automated_backups.enabled` [support key](/current/help-support/support-settings/#support-keys). By default, when `dremio.automated_backups.enabled` is enabled, Dremio creates a backup at midnight local time. To set your backup for a different time, set the `dremio.automated_backups.schedule` support key to the desired time in ISO format. For example, `13:45+02:00` or `14:12Z`.

note

Automated backups currently do not create backups for [Open Catalog](/current/data-sources/open-catalog/)'s metadata storage backend. Follow the instructions on [Open Catalog backup and restore processes](/current/admin/open-catalog-backing-store-backuprestore/) to back up the metadata storage backend for Open Catalog.

Was this page helpful?

[Previous

Service Telemetry](/current/admin/service-telemetry-kubernetes)[Next

Managing Job Workloads](/current/admin/workloads/)

---

# Source: https://docs.dremio.com/current/admin/workloads/

Version: current [26.x]

# Managing Job Workloads

Dremio job workloads are managed differently depending on which edition (Enterprise or Community) you are using.

* [Job History & Job Details](/current/admin/monitoring/jobs/)
  The results of each query, or job, is displayed here in table format. Individual job details may be viewed by clicking on each row.

Jobs may be sorted and arranged by data type based on the columns displaying. Additional information may also be seen for individual jobs by hovering over a row and column for condensed results. By clicking on the desired job, this launches the Job Details screen, which is rich with easy-to-read data regarding how a query was executed from start to finish.

* [Queue Control](/current/admin/workloads/job-queues/)  
  This feature provides basic capability to manage query queues, Reflection queues, query memory, and query thresholds.
* [Workload Management](/current/admin/workloads/workload-management) Enterprise

This feature provides advanced capability to manage cluster resources and workloads
by defining a queue with specific characteristics
(such as memory limits, CPU priority, and queueing and runtime timeouts)
and then defining rules that specify which query is assigned to which queue.

Was this page helpful?

[Previous

Monitoring](/current/admin/monitoring/)[Next

Queue Control](/current/admin/workloads/job-queues)

---

# Source: https://docs.dremio.com/current/admin/monitoring/

Version: current [26.x]

On this page

# Monitoring

As an administrator, you can monitor logs, usage, system telemetry, [jobs](/current/admin/monitoring/jobs/), and [Dremio nodes](/current/admin/monitoring/dremio-nodes).

As the [Dremio Shared Responsibility Models](/responsibility) outline, monitoring is a shared responsibility between Dremio and you. The Shared Responsibility Models lay out Dremio's responsibilities for providing monitoring technologies and logs and your responsibilities for implementation and use.

## Logs

Logs are primarily for troubleshooting issues and monitoring the health of the deployment.

note

By default, Dremio uses the following locations to write logs:

* Tarball - `<DREMIO_HOME>/log`
* RPM - `/var/log/dremio`
* Kubernetes - `/opt/dremio/log`

### Log Types

| Log Type | Description |
| --- | --- |
| Audit | The `audit.json` file tracks all activities that users perform within Dremio. For details, see [Audit Logging](/current/security/auditing/). |
| System | The following system logs are enabled by default:  * `access.log`: HTTP access log for the Dremio web server; generated by coordinator nodes only. * `server.gc`: Garbage collection log. * `server.log` and `json/server.json`: Server logs generated in a text format (server.log) and json format (json/server.json). Users granted the `ADMIN` role can disable one of these formats. * `server.out`: Log for Dremio daemon standard out. * `metadata_refresh.log`: Log for refreshing metadata. * `tracker.json`: Tracker log. * `vacuum.json`: Log for the files scanned and deleted by `VACUUM CATALOG` and `VACUUM TABLE` commands. |
| Query | Query logging is enabled by default. The `queries.json` file contains the log of completed queries; it does not include queries currently in planning or execution. You can retrieve the same information that is in `queries.json` using the [`sys.jobs_recent`](/current/reference/sql/system-tables/jobs_recent) system table. Query logs include the following information:  * `queryId`: Unique ID of the executed query. * `queryText`: SQL query text. * `start`: Start time of the query. * `finish`: End time of the query. * `outcome`: Whether the query was completed or failed. * `username`: User who executed the query. * `commandDescription`: Type of the command; may be a regular SQL query execution job or another SQL command.  The query log may contain additional information depending on your Dremio configuration. |
| Warning | The `hive.deprecated.function.warning.log` file contains warnings for Hive functions that have been deprecated. To resolve warnings that are listed in this file, replace deprecated functions with a [supported function](/current/reference/sql/sql-functions/ALL_FUNCTIONS/). For example, to resolve a warning that mentions `NVL`, replace `NVL` with `COALESCE`. |

### Retrieving Logs from the Dremio Console Enterprise

Retrieve logs for Kubernetes deployments in the Dremio console at **Settings** > **Support** > **Download Logs**.

#### Prerequisites

* You must be using Dremio 25.1+. Log collection is powered by Dremio Diagnostics Collector (DDC).
* You must have the EXPORT DIAGNOSTICS privilege to view **Download Logs** options in **Settings** > **Support**.

#### Downloading Logs

To download logs:

1. In the Dremio console, navigate to **Settings** > **Support** > **Download Logs** and click **Start collecting data**.

note

You may store a maximum of three log bundles. Delete log bundles as needed to start a new log collection if you reach the maximum.

We recommend the default `Light` collection, which provides 7 days of logs and completed queries in the `queries.json` file, for troubleshooting most issues. For more complex issues, select the `Standard` collection, which provides 7 days of logs and 28 days of completed queries in the `queries.json` file.

2. When Dremio completes log collection, the log bundle appears in a list below **Start collecting data**. To download a log bundle, click **Download** next to the applicable bundle. Log bundles are available to download for 24 hours.

### Logging in Kubernetes

By default, all logs are written to a persisted volume mounted at `/opt/dremio/log`.

To disable logging, set `writeLogsToFile: false` in the `values-overrides.yaml` configuration file either globally or individually for each `coordinator` and `executor` parent. For more information, see [Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/).

#### Using the Container Console

All logs are written to the container's console (stdout) simultaneously. These logs can be monitored using a `kubectl` command:

Command for viewing logs using kubectl logs

```
kubectl logs [-f] [container-name]
```

Use the `-f` flag to continuously print new log entries to your terminal as they are generated.

You can also write logs to a file on disk in addition to stdout. Read [Writing Logs to a File](https://github.com/dremio/dremio-cloud-tools/blob/master/charts/dremio_v2/docs/setup/Writing-Logs-To-A-File.md) for details.

#### Using the AKS Container

Azure provides integration with AKS clusters and Azure Log Analytics to monitor container logs. This is a standard practice that puts infrastructure in place to aggregate logs from containers into a central log store to analyze them.

AKS log monitoring is useful for the following reasons:

* Monitoring logs across lots of pods can be overwhelming.
* When a pod (for example, a Dremio executor) crashes and restarts, only the logs from the last pod are available.
* If a pod is crashing regularly, the logs are lost, which makes it difficult to analyze the reasons for the crash.

For more information regarding AKS, see [Azure Monitor features for Kubernetes monitoring](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview).

#### Enabling Log Monitoring

You can enable log monitoring when creating an AKS cluster or after the cluster has been created.

Once logging is enabled, all your container `stdout` and `stderr` logs are collected by the infrastructure for you to analyze.

1. While creating an AKS cluster, enable container monitoring. You can use an existing Log Analytics workspace or create a new one.
2. In an existing AKS cluster where monitoring was not enabled during creation, go to **Logs on the AKS cluster** and enable it.

#### Viewing Container Logs

To view all the container logs:

1. Go to **Monitoring** > **Logs**.
2. Use the filter option to see the logs from the containers that you are interested in.

## Usage

Monitoring usage across your cluster makes it easier to observe patterns, analyze the resources being consumed by your data platform, and understand the impact on your users.

### Catalog Usage Enterprise

Go to **Settings** > **Monitor** to view your catalog usage. You must be a member of the `ADMIN` role to access the Monitor page. When you open the Monitor page, you are directed to the Catalog Usage tab by default where you can see the following metrics:

* Top 10 most queried datasets and how often the jobs on the dataset were accelerated
* Top 10 most queried spaces and source folders

note

A source can be listed in the top 10 most queried spaces and source folders if the source contains a child dataset that was used in the query (for example, `postgres.accounts`). Queries of datasets in sub-folders (for example, `s3.mybucket.iceberg_table`) are classified by the sub-folder and not the source.

All datasets are assessed in the metrics on the Monitor page except for datasets in the [system tables](/current/reference/sql/system-tables/), the [information schema](https://docs.dremio.com/current/reference/sql/information-schema), and home spaces.

The metrics on the Monitor page analyze only user queries. Refreshes of data Reflections and metadata refreshes are excluded.

### Jobs Enterprise

Go to **Settings** > **Monitor** > **Jobs** to open the Jobs tab. You must be a member of the `ADMIN` role to access the Monitor page. The Jobs tab shows an aggregate view of the following metrics for the jobs that are running on your cluster:

* Total job count over the last 24 hours and the relative rate of failure/cancelation
* Top 10 most active users based on the number of jobs they ran
* Total jobs accelerated, total job time saved, and average job speedup from Autonomous Reflections over the past month.
* Total number of jobs accelerated by autonomous and manual Reflections over time
* Total number of completed and failed jobs over time
* Jobs (completed and failed) grouped by the [queue](/current/admin/workloads/workload-management/#default-queues) they ran on
* Percentage of time that jobs spent in each [state](/current/admin/monitoring/jobs/#job-states-and-statuses)
* Top 10 longest running jobs

To view all jobs and the details of specific jobs, see [Viewing Jobs](/current/admin/monitoring/jobs/).

### Resources Enterprise

Go to **Settings** > **Monitor** > **Resources** to open the Resources tab. You must be a member of the `ADMIN` role to access the Monitor page. The Resources tab shows an aggregate view of the following metrics for the jobs and nodes running on your cluster:

* Percentage of CPU and memory utilization for each coordinator and executor node
* Top 10 most CPU and memory intensive jobs
* Number of running executors

### Cluster Usage

Dremio displays the number of unique users who executed jobs on that day and the number of executed jobs.

1. Hover over ![Icon represents help](/images/icons/help.png "Help icon") in the side navigation bar.
2. Click **About Dremio** in the menu.
3. Click the **Cluster Usage Data** tab.

![](/images/cluster-usage.png "Viewing Cluster Usage")

## System Telemetry

Dremio exposes system telemetry metrics in Prometheus format by default. It is not necessary to configure an exporter to collect the metrics. Instead, you can specify the host and port number where metrics are exposed in the [dremio.conf](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/index.md) file and scrape the metrics with any Prometheus-compliant tool.

To specify the host and port number where metrics are exposed, add these two properties to the `dremio.conf` file:

* `services.web-admin.host`: set to the desired host address (typically `0.0.0.0` or the IP address of the host where Dremio is running).
* `services.web-admin.port`: set to any desired value that is greater than `1024`.

For example:

Example host and port settings in dremio.conf

```
services.web-admin.host: "127.0.0.1"  
services.web-admin.port: 9090
```

Restart Dremio after you update the `dremio.conf` file to make sure your changes take effect.

Access the exported Dremio system telemetry metrics at `http://<yourHost>:<yourPort>/metrics`.

For more information about Prometheus metrics, read [Types of Metrics](https://prometheus.io/docs/tutorials/understanding_metric_types/) in the Prometheus documentation.

Was this page helpful?

[Previous

Workload Management](/current/admin/workloads/workload-management)[Next

Viewing Jobs](/current/admin/monitoring/jobs/)

* Logs
  + Log Types
  + Retrieving Logs from the Dremio Console Enterprise
  + Logging in Kubernetes
* Usage
  + Catalog Usage Enterprise
  + Jobs Enterprise
  + Resources Enterprise
  + Cluster Usage
* System Telemetry

---

# Source: https://docs.dremio.com/current/admin/open-catalog-backing-store-backuprestore

Version: current [26.x]

On this page

# Open Catalog Backup and Restore Enterprise

Regular backups are essential for protecting Open Catalog metadata and ensuring business continuity. This section explains how to back up and restore the MongoDB cluster that stores Open Catalog's configuration, table metadata, and access control policies.

note

Ensure you have enabled [automated backup](/current/admin/automated-backups) for your Dremio cluster before backing up the Open Catalog.

## Automated Backups

Automated MongoDB backup is enabled in your `values-overrides.yaml`. The backups are automatically written to your distributed storage and must be taken while Dremio is operational. Not all object store authentication methods are supported by this feature. See [Configuring the Distributed Storage](/current/deploy-dremio/configuring-kubernetes/#configuring-the-distributed-storage) for details on supported configurations.

When enabled, a backup agent will be deployed into the cluster as a container of the first MongoDB pod `dremio-mongodb-rs0-0`. Inspect the agent logs with the command: `kubectl logs -f dremio-mongodb-rs0-0 -c backup-agent -n <your-namespace>`. Backups are written to the `catalog-backups` folder of Dremio's distributed storage. The backup names will follow a consistent pattern, for example, `cron-dremio-mongodb-20251112124000-87jl7`.

## Restore

### Prerequisites

1. Ensure that Dremio is in **Admin Mode**. See [Using the Dremio Admin CLI on Kubernetes](/current/admin/admin-dremio-kubernetes/#using-the-dremio-admin-cli-on-kubernetes) to understand how to switch to **Admin Mode**.
2. Export your Kubernetes namespace as an environment variable. Replace the `<namespace>` placeholder with your value:

   ```
   export NAMESPACE = <namespace>
   ```
3. Run the following command for a list of available backups for the restore:

   ```
   kubectl get psmdb-backup -n $NAMESPACE
   ```
4. Run the following command for MongoDB cluster information. The `clustername` will be required to start the restore.

   ```
   kubectl get psmdb -n $NAMESPACE
   ```

### Restore From a Full Backup

Restore based on the name of the specific backup.

1. Create a file named `restore.yaml`. Fill in the YAML based on the output from the prerequisites, namely: `<my-cluster-name>` and `<my-backup-name>`. Dremio recommends substituting `<my-restore-name>` with a name containing the date the restore was performed.

   ```
   apiVersion: psmdb.dremio.com/v1  
   kind: PerconaServerMongoDBRestore  
   metadata:  
    name: <my-restore-name>  
   spec:  
    clusterName: <my-cluster-name>  
    backupName: <my-backup-name>
   ```
2. Start the restore by applying the YAML created in the previous step:

   ```
   kubectl apply -f restore.yaml -n $NAMESPACE
   ```

Once completed, bring Dremio back online. See [Using the Dremio Admin CLI on Kubernetes](/current/admin/admin-dremio-kubernetes/#using-the-dremio-admin-cli-on-kubernetes) to understand how to leave **Admin Mode**.

### Point-in-time Recovery

Restore to a particular point in time within a given backup. This allows for a more granular restore.

1. Use this command to get a list of all restore times available within a backup.

   ```
   kubectl get psmdb-backup <backup_name> -n $NAMESPACE -o jsonpath='{.status.latestRestorableTime}
   ```
2. Modify the `restore.yaml` specifying your chosen restore date and time in the following format `YYYY-MM-DD HH:MM:SS` from those available.

   ```
   apiVersion: psmdb.dremio.com/v1  
   kind: PerconaServerMongoDBRestore  
   metadata:  
    name: <my-restore-name>  
   spec:  
    clusterName: <my-cluster-name>  
    backupName: <my-backup-name>  
    pitr:  
      type: date  
      date: YYYY-MM-DD hh:mm:ss
   ```
3. Start the restore by applying the YAML created in the previous step:

   ```
   kubectl apply -f restore.yaml -n $NAMESPACE
   ```

Once completed, bring Dremio back online. See [Using the Dremio Admin CLI on Kubernetes](/current/admin/admin-dremio-kubernetes/#using-the-dremio-admin-cli-on-kubernetes) to understand how to leave **Admin Mode**.

Was this page helpful?

[Previous

Splunk](/current/admin/monitoring/exporting/splunk)[Next

Developer Guide](/current/developer/)

* Automated Backups
* Restore
  + Prerequisites
  + Restore From a Full Backup
  + Point-in-time Recovery

---

# Source: https://docs.dremio.com/current/admin/service-telemetry-kubernetes/

Version: current [26.x]

On this page

# Service Telemetry for Kubernetes Deployments Enterprise

As of Dremio 26.0, enterprise customers deploying Dremio clusters on Kubernetes will automatically transmit telemetry data back to Dremio's corporate endpoint. This telemetry provides valuable insights into system performance and health, and is also used in the calculations for usage-based [billing](/current/admin/billing/). Telemetry can be disabled through configuration; however, this is not considered a best practice because telemetry helps Dremio ensure stability and timely support.

## Telemetry Data Collection

Dremio's telemetry data collection is strictly limited to operational and performance metrics. These metrics provide visibility into various components and services, ensuring optimal performance and reliability.
Importantly, no customer content (e.g., business data) or user-entered information is transmitted. If you would like to develop a deeper understanding of the metrics transmitted and their contents, you can set up your own internal monitoring of your Dremio cluster by following the steps in [Monitoring Dremio Nodes](https://docs.dremio.com/current/admin/monitoring/dremio-nodes).

The collected telemetry data is categorized as follows:

| Category | Description |
| --- | --- |
| **Application Metrics** | These metrics provide insights into the usage and performance of objects within a Dremio deployment, including:  * Number of queries, Reflections, sources, and views. * Success and failure rates of queries. * Success and failure rates of Reflection and source refresh operations. |
| **Java Metrics** | These metrics capture internal Java Virtual Machine (JVM) performance indicators from containers running the Dremio application, such as:  * Number of active threads. * Memory allocation and usage. * Garbage collection activity and pauses. |
| **Service Metrics** | These metrics measure the health of core components supporting Dremio's execution and coordination services, including:  * KVstore performance. * Zookeeper availability and network health. |
| **Kubernetes Metrics** | These metrics provide insight into container and pod behavior for all containers in a Dremio deployment, including:  * CPU, memory, and storage requests. * Container restarts and readiness. * StatefulSet desired and current pod count. |

## Telemetry Transmission Requirements

Telemetry transmission to Dremio follows the [Dremio Subscription Agreement](https://www.dremio.com/legal/dremio-subscription-agreement/).

### Network Requirements for Telemetry Transmission

To ensure successful telemetry transmission, the following network configurations must be in place:

* Your network must allow traffic egress to Dremio's endpoint `observability.dremio.com`.
* Dremio's OpenTelemetry collectors use port 443 for secure data transmission via TLS.

### Setting Up a Proxy

If traffic egresses to the endpoint and the port is restricted, a proxy can be configured to enable telemetry transmission:

1. Edit your `.yaml` configuration file to deploy Dremio to Kubernetes. For more information, refer to [Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/).
2. Add your proxy configuration values to the `.yaml` file using the following syntax:

   * HTTPS Proxy (Recommended)
   * HTTP Proxy

   ```
   telemetry:  
     extraEnvs: []  
       - name: HTTPS_PROXY  
         value: https://proxy.example.com:443
   ```

   ```
   telemetry:  
     extraEnvs: []  
       - name: HTTP_PROXY  
         value: http://proxy.example.com:3128
   ```

## Troubleshooting or Support

For troubleshooting or support, please contact your account representative or Dremio Support.

## Related Topics

* [Licensing](/current/admin/licensing/) - Learn more about Dremio's licensing and telemetry.
* [Billing](/current/admin/billing/) - Learn more about Dremio's billing and usage data.

Was this page helpful?

[Previous

AWS Bedrock](/current/admin/model-providers/aws-bedrock)[Next

Automated Backup](/current/admin/automated-backups)

* Telemetry Data Collection
* Telemetry Transmission Requirements
  + Network Requirements for Telemetry Transmission
  + Setting Up a Proxy
* Troubleshooting or Support
* Related Topics

---

# Source: https://docs.dremio.com/current/admin/model-providers

Version: current [26.x]

On this page

# Configure Model Providers Enterprise

Starting with Dremio Software 26.1, you can configure model providers for AI functionality when deploying Dremio clusters on Kubernetes. After you configure at least one model provider, you must set a default model provider and optionally set an allowlist of available models. Dremio uses this default provider for all Dremio's AI Agent interactions and whereas the allowlist models can be used by anyone writing AI functions.

## Supported Model Providers

Dremio supports configuration of the following model providers and models. Dremio recommends using enterprise-grade reasoning models for the best performance and experience.

| Category | Models | Connection Method(s) |
| --- | --- | --- |
| **OpenAI** | * gpt-5-2025-08-07 * gpt-5-mini-2025-08-07 * gpt-5-nano-2025-08-07 * gpt-4.1-2025-04-14 * gpt-4o-2024-11-20 * gpt-4-turbo-2024-04-09 * gpt-4.1-mini-2025-04-14 * o3-mini-2025-01-31 * o4-mini-2025-04-16 * o3-2025-04-16 | * Access Key |
| **Anthropic** | * claude-sonnet-4-5-20250929 * claude-opus-4-1-20250805 * claude-opus-4-20250514 * claude-sonnet-4-20250514 | * Access Key |
| **Google Gemini** | * gemini-2.5-pro | * Access Key |
| **AWS Bedrock** | * specify Model ID(s) * [AWS Bedrock Supported Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) | * Access Key * IAM Role |
| **Azure OpenAI** | * specify Deployment Name(s) * [Azure Supported Models](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cstandard-chat-completions%2Cglobal-standard&pivots=azure-openai#azure-openai-in-azure-ai-foundry-models) | Combination of  1. Resource Name 2. Directory ID 3. Application ID 4. Client Secret Value |

## Add Model Provider

For steps on adding an AWS Bedrock model provider, see [Configure AWS Bedrock as a Model Provider](/current/admin/model-providers/aws-bedrock).

For all other model providers, follow these steps to add a model provider in the Dremio console:

1. Click ![This is the Settings icon.](/images/green-settings-icon.png "The Settings icon.") in the side navigation bar to go to the Settings page.
2. Select **Preferences** in the settings sidebar.
3. Enable the **AI Features** flag.
4. Click **Add model provider**.

## Default Model Provider

To delete the model provider, you must assign a new default unless you are deleting the last available model provider. To update the default model provider to a new one, you must have MODIFY privilege on both the current default and the new proposed default model provider.

Was this page helpful?

[Previous

Usage](/current/admin/billing/usage)[Next

AWS Bedrock](/current/admin/model-providers/aws-bedrock)

* Supported Model Providers
* Add Model Provider
* Default Model Provider