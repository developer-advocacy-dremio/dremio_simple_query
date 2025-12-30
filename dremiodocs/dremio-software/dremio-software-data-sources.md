# Dremio Software - Data Sources



---

# Source: https://docs.dremio.com/current/data-sources/

Version: current [26.x]

On this page

# Manage Sources

Dremio supports a variety of data sources, including lakehouse catalogs, object storage, and databases.

As the [Dremio Shared Responsibility Models](/responsibility) outline, metadata is a shared responsibility between Dremio and you. The Shared Responsibility Models lay out Dremio's responsibilities for enabling data source configurations and your responsibilities for managing metadata.

## Open Catalog

Dremio comes with a built-in lakehouse catalog, built on [Apache Polaris (incubating)](https://polaris.io/). The catalog enables centralized, secure read and write access to your Iceberg tables across various REST-compatible query engines and automates data maintenance operations to maximize query performance.

* [Open Catalog](/current/data-sources/open-catalog/)

## Lakehouse Catalogs

Lakehouse catalogs provide you with the ability to connect to centralized catalogs. The Open Catalog, Snowflake Open Catalog, Unity Catalog, and Iceberg REST Catalog all connect to the destination sources over the Apache Iceberg REST API.

* [AWS Glue Data Catalog](/current/data-sources/lakehouse-catalogs/aws-glue-catalog/)
* [Open Catalog (External)](/current/data-sources/lakehouse-catalogs/open-catalog-external)
* [Hive](/current/data-sources/lakehouse-catalogs/hive/)
* [Iceberg REST Catalog](/current/data-sources/lakehouse-catalogs/iceberg-rest-catalog/)
* [Nessie](/current/data-sources/lakehouse-catalogs/nessie/)
* [Snowflake Open Catalog](/current/data-sources/lakehouse-catalogs/snowflake-open/)
* [Unity Catalog](/current/data-sources/lakehouse-catalogs/unity/)
* [Microsoft OneLake](/current/data-sources/lakehouse-catalogs/onelake)

## Object Storage

* [Amazon S3](/current/data-sources/object/s3/)
* [Azure Storage](/current/data-sources/object/azure-storage/)
* [Google Cloud Storage](/current/data-sources/object/gcs/)
* [HDFS](/current/data-sources/object/hdfs/)
* [NAS](/current/data-sources/object/nas/)

## Databases

* [Amazon OpenSearch Service](/current/data-sources/databases/opensearch)
* [Amazon Redshift](/current/data-sources/databases/redshift)
* [Apache Druid](/current/data-sources/databases/apache-druid)
* [Dremio Cluster](/current/data-sources/databases/dremio) (you can connect to one or more other Dremio Software clusters and run queries on the data sources to which they are connected, and you can run queries that federate data across connected clusters)
* [Google BigQuery](/current/data-sources/databases/google-bigquery)
* [Elasticsearch](/current/data-sources/databases/elasticsearch)
* [IBM Db2](/current/data-sources/databases/ibm-db2)
* [Microsoft Azure Data Explorer](/current/data-sources/databases/azure-data-explorer)
* [Microsoft Azure Synapse Analytics](/current/data-sources/databases/azure-synapse-analytics)
* [Microsoft SQL Server](/current/data-sources/databases/sql-server)
* [MongoDB](/current/data-sources/databases/mongo)
* [MySQL](/current/data-sources/databases/mysql)
* [Oracle](/current/data-sources/databases/oracle)
* [PostgreSQL](/current/data-sources/databases/postgres)
* [SAP HANA](/current/data-sources/databases/sap-hana)
* [Snowflake](/current/data-sources/databases/snowflake)
* [Teradata](/current/data-sources/databases/teradata)
* [Vertica](/current/data-sources/databases/vertica)

Dremio enables users to run external queries, queries that use the native syntax of the relational database, to process SQL statements that are not yet supported by Dremio or are too complex to convert. Dremio administrators enable the feature for each data source and specify which Dremio users can edit that source. See [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/) for more information.

Dremio improves query performance for relational database datasets with [Runtime Filtering](/current/help-support/advanced-topics/runtime-filtering/), which applies dimension table filters to joined fact tables at runtime.

note

* **Decimal Support:** Decimal-to-decimal mappings are supported for relational database sources.
* **Collation:** Relational database sources must have a collation equivalent to `LATIN1_GENERAL_BIN2` to ensure consistent results when operations are pushed down. For non-equivalent collations, create a view that coerces the collation to one that is equivalent to `LATIN1_GENERAL_BIN2` and access that view.
* For all sources, case-sensitive source data file/table names are not supported. In Dremio, case is ignored in the names of data files. `file1.parquet`, `File1.parquet`, and `FILE1.parquet` are considered to be equivalent names. Therefore, searching on one of these names can result in unanticipated results.  
  In addition, columns in a table that have the same name with different cases are not supported. For example, if two columns named `Trip_Pickup_DateTime` and `trip_pickup_datetime` exist in the same table, one of the columns may disappear when the header is extracted.

## Files and Folders

* [Formatting Data to a Table](/current/developer/data-formats/table/)
* [Upload Files](/current/data-sources/file-upload)

  note Case-sensitive source data file/table names are not supported. In Dremio, data filenames in your data source are "seen" in a case-insensitive manner. So, if you have three file names with difference cases (for example, `JOE` `Joe`, and `joe`), Dremio "sees" the files as having the same name. Thus, searching on `Joe`, `JOE`, or `joe`, can result in unanticipated data results.  
    
  In addition, columns in a table that have the same name with different cases are not supported. For example, if two columns named `Trip_Pickup_DateTime` and `trip_pickup_datetime` exist in the same table, one of the columns may disappear when the header is extracted.

Was this page helpful?

[Previous

AI](/current/ai)[Next

Open Catalog](/current/data-sources/open-catalog/)

* Open Catalog
* Lakehouse Catalogs
* Object Storage
* Databases
* Files and Folders

---

# Source: https://docs.dremio.com/current/data-sources/open-catalog/

Version: current [26.x]

On this page

# Open Catalog Enterprise

Dremio's built-in lakehouse catalog is built on [Apache Polaris (incubating)](https://polaris.apache.org/). The catalog enables centralized, secure read and write access to your Iceberg tables across different REST-compatible query engines and [automates data maintenance operations](/current/developer/data-formats/apache-iceberg/table-maintenance-optimization/automated-maintenance) to maximize query performance. Key features include:

* **Iceberg REST compatibility**: Read and write from the Open Catalog using any engine or framework compatible with the Iceberg REST API. For example, use Spark or Flink to ingest data into the catalog, and then use Dremio to curate and serve data products built on that data.
* **Role-Based Access Control and Fine-Grained Access Control**: Secure data using [Role-Based Access Control (RBAC) privileges](/current/security/rbac/privileges/) and create [row filters and column masks](/current/data-products/govern/row-column-policies-udf) to ensure users only access the data they need. For example, create a column mask to obfuscate credit card numbers or create a row filter on your employee details table that only returns rows with employees in your region.
* **Automated table maintenance**: Open Catalog [automates Iceberg maintenance operations](/current/developer/data-formats/apache-iceberg/table-maintenance-optimization/automated-maintenance) like compaction and vacuum, which maximizes query performance, minimizes storage costs, and eliminates the need to run manual data maintenance. Open Catalog also simplifies Iceberg table management and eliminates the risk of poor performance from suboptimal data layouts with support for Iceberg clustering keys.
* **Enable data analysts**: Open Catalog is fully compatible with Dremio's built-in data product capabilities, including semantic search (use natural language to discover AI-ready data products), descriptions (use built-in descriptions and labels to understand how to use data products to answer business questions), and lineage (use lineage graphs to understand how data products are derived and transformed and assess the impact of changes on downstream datasets).

This page provides instructions for configuring the Open Catalog. If you would like to connect to Open Catalogs deployed in other Dremio instances, see [Open Catalog (External)](/current/data-sources/lakehouse-catalogs/open-catalog-external).

## Prerequisites

Before you configure Open Catalog, make sure you do the following:

* Configure access to your storage provider, as described in Configure Storage Access.
* Configure the settings of your storage provider in Dremio's Helm chart, as described in [Configuring Storage for the Open Catalog](/current/deploy-dremio/configuring-kubernetes/#configuring-storage-for-the-open-catalog).

These configurations are required to enable support for vended credentials and to allow access to the table metadata necessary for Iceberg table operations.

## Configure the Open Catalog

To configure Open Catalog:

* When creating the first Open Catalog, select **Add an Open Catalog**. Add a **Name** for the catalog.
* When configuring an existing Open Catalog, right-click on your catalog and select **Settings** from the dropdown.

### Storage

1. The **Default storage URI** field displays the default storage location you configured in [Dremio's Helm chart](/current/deploy-dremio/configuring-kubernetes/).
2. Use the **Storage access** field to configure your preferred authentication method. Open Catalog supports two types of credentials for authentication:
   * **Use credential vending (Recommended)**: Credential vending is a security mechanism where the catalog service issues temporary, scoped access credentials to the query engine for accessing table storage. The engine is "vended" a temporary credential just in time for the query.
   * **Use master storage credentials**: The credentials authenticate access to all storage URIs within this catalog. These credentials ensure all resources are accessible through a single authentication method. This should be used if STS is unavailable or the vended credentials mechanism is disabled. Select the object storage provider that hosts the location specified in the **Default storage URI** field:
     + **AWS** – Select **AWS** for Amazon S3 and S3-compatible storage. You can refer to the Dremio documentation for connecting to [Amazon S3](/current/data-sources/object/s3/#configuring-amazon-s3-as-a-source), which is also applicable here. When selecting to assume an IAM role, ensure that the role policy grants access to the bucket or folder specified in the **Default storage URI** field.
     + **Azure** – Select **Azure** for Azure Blob Storage. You can refer to the Dremio documentation for connecting to [Azure Storage](/current/data-sources/object/azure-storage/#configuring-azure-storage-as-a-source), which is also applicable here.
     + **Google Cloud Storage** – Select **Google** for Google Cloud Storage (GCS). You can refer to the Dremio documentation for connecting to [GCS](/current/data-sources/object/gcs/#configuring-gcs-as-a-source), which is also applicable here.
3. Enter any required storage connection properties in the **Connection Properties** field. Refer to the Advanced Options section for your storage provider (Amazon S3, Azure, or GCS) for available properties.

### Advanced Options

To set advanced options:

1. Under **Cache Options**, review the following table and edit the options to meet your needs.

   | Cache Options | Description |
   | --- | --- |
   | **Enable local caching when possible** | Selected by default. Along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details. |
   | **Max percent of total available cache space to use when possible** | Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage. |
2. Under **Table maintenance**, manage settings for [automated table maintenance operations](/current/developer/data-formats/apache-iceberg/table-maintenance-optimization/automated-maintenance):

   * **Enable auto optimization**: Compacts small files into larger files. Clusters data if Iceberg clustering keys are set on the table.
   * **Enable table cleanup**: Deletes expired snapshots and orphaned metadata files.

### Reflection Refresh

You can set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed. See the following options:

| Option | Description |
| --- | --- |
| **Never refresh** | Select to prevent automatic Reflection refresh. The default is to automatically refresh. |
| **Refresh every** | How often to refresh Reflections, specified in hours, days, or weeks. This option is ignored if **Never refresh** is selected. |
| **Set refresh schedule** | Specify the daily or weekly schedule. |
| **Never expire** | Select to prevent Reflections from expiring. The default is to automatically expire after the time limit below. |
| **Expire after** | The time limit after which Reflections expire and are removed from Dremio, specified in hours, days, or weeks. This option is ignored if **Never expire** is selected. |

### Metadata

Specifying metadata options is handled with the following settings:

#### Dataset Handling

* Remove dataset definitions if the underlying data is unavailable (default).
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names, such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | **Fetch every** | You can choose to set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning, such as information needed for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can choose to fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**. |
  | **Fetch every** | You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

You have the option to grant privileges to specific users or roles. See [Access Control](/current/security/rbac/) for additional information about privileges.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Configure Storage Access

To configure access to the storage, select your storage provider below and follow the steps:

* Amazon S3
* S3-compatible
* Azure Storage
* Google Cloud Storage

### S3 and STS Access via IAM Role (Preferred)

1. Create an Identity and Access Management (IAM) user or use an existing IAM user for Open Catalog.
2. Create an IAM policy that grants access to your S3 location. For example:

   Example of a policy

   ```
   {  
     "Version": "2012-10-17",  
     "Statement": [  
       {  
         "Effect": "Allow",  
         "Action": [  
           "s3:PutObject",  
           "s3:GetObject",  
           "s3:GetObjectVersion",  
           "s3:DeleteObject",  
           "s3:DeleteObjectVersion"  
         ],  
         "Resource": "arn:aws:s3:::<my_bucket>/*"  
       },  
       {  
         "Effect": "Allow",  
         "Action": [  
           "s3:ListBucket",  
           "s3:GetBucketLocation"  
         ],  
         "Resource": "arn:aws:s3:::<my_bucket>",  
         "Condition": {  
           "StringLike": {  
             "s3:prefix": [  
               "*"  
             ]  
           }  
         }  
       }  
     ]  
   }
   ```
3. Create an IAM role to grant privileges to the S3 location.

   1. In your AWS console, select **Create Role**.
   2. Enter an **externalId**. For example, `my_catalog_external_id`.
   3. Attach the policy created in the previous step and create the role.
4. Create IAM user permissions to access the bucket via STS:

   The `sts:AssumeRole` permission is required for Open Catalog to function with vended credentials, as it relies on the STS temporary token to perform these validations.

   1. Select the IAM role created in the previous step.
   2. Edit the trust policy and add the following:

      Trust policy

      ```
      {  
        "Version": "2012-10-17",  
        "Statement": [  
          {  
            "Sid": "",  
            "Effect": "Allow",  
            "Principal": {  
              "AWS": "<dremio_catalog_user_arn>"  
            },  
            "Action": "sts:AssumeRole",  
            "Condition": {  
              "StringEquals": {  
                "sts:ExternalId": "<dremio_catalog_external_id>"  
              }  
            }  
          }  
        ]  
      }
      ```

      Replace the following values with the ones obtained in the previous steps:

      * `<dremio_catalog_user_arn>` - The IAM user that was created in the first step.
      * `<dremio_catalog_external_id>` - The external ID that was created in the third step.

### S3 and STS Access via Access Key

1. In the Dremio console, select **Use master storage credentials** when adding Open Catalog.
2. The access keys must have permissions to access the bucket and the STS server.
3. Create a Kubernetes secret named `catalog-server-s3-storage-creds` to access the configured location. Here is an example for S3 using an access key and secret key:

   Run kubectl to create the Kubernetes secret

   ```
   export AWS_ACCESS_KEY_ID=<username>  
   export AWS_SECRET_ACCESS_KEY=<password>  
   kubectl create secret generic catalog-server-s3-storage-creds \  
   --namespace $NAMESPACE \  
   --from-literal awsAccessKeyId=$AWS_ACCESS_KEY_ID \  
   --from-literal awsSecretAccessKey=$AWS_SECRET_ACCESS_KEY
   ```

1. The access keys must have permissions to access the bucket.

   1. To use vended credentials, the access key must also have access to an STS server.
   2. If you cannot leverage an STS server, when setting up the catalog for the first time in the Dremio console, you must select master storage credentials.
2. Create a Kubernetes secret named `catalog-server-s3-storage-creds` to access the configured location. Here is an example for S3 using an access key and secret key:

   Run kubectl to create the Kubernetes secret

   ```
   export AWS_ACCESS_KEY_ID=<username>  
   export AWS_SECRET_ACCESS_KEY=<password>  
   kubectl create secret generic catalog-server-s3-storage-creds \  
   --namespace $NAMESPACE \  
   --from-literal awsAccessKeyId=$AWS_ACCESS_KEY_ID \  
   --from-literal awsSecretAccessKey=$AWS_SECRET_ACCESS_KEY
   ```

   For S3-compatible storage providers (e.g., MinIO), the access keys should be the username and password.

note

* Soft delete for blobs is not supported for Azure Storage accounts. Soft delete should be disabled to establish a successful connection.
* Although not mandatory, Dremio recommends enabling **Hierarchical Namespace** when using Azure Data Lake Storage. For more information, see [Azure Data Lake Storage Gen2 hierarchical namespace](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-namespace).

1. Register an application and create secrets:

   1. Go to Azure Active Directory > App Registrations.
   2. Register your app and take note of the **Client ID** and **Tenant ID**. For more information on these steps, refer to [Register an application with Microsoft Entra ID and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#register-an-application-with-microsoft-entra-id-and-create-a-service-principal).
   3. Go to Certificates & Secrets > New Client Secret.
   4. Create a secret and take note of the **Secret Value**.
   5. Create a Kubernetes secret named `catalog-server-azure-storage-creds` using the following command:

      Run kubectl to create the Kubernetes secret

      ```
      export AZURE_CLIENT_ID=<Azure App client id>  
      export AZURE_CLIENT_SECRET=<App secret value>  
      kubectl create secret generic catalog-server-azure-storage-creds \  
        --namespace $NAMESPACE \  
        --from-literal azureClientId=$AZURE_CLIENT_ID \  
        --from-literal azureClientSecret=$AZURE_CLIENT_SECRET
      ```
2. Create an Identity and Access Management (IAM) role in your Storage Account and set up the permission for your new application to access the storage account by following these steps:

   1. In the Azure console, go to your Storage Account and navigate to Access Control (IAM) > Role assignments > Add role assignment.
   2. Select the `Storage Blob Data Contributor` role and click **Next**.
   3. In the **Members** section, click **Select members**, search for your app registration from step 1, and click **Select**.
   4. Review and assign the roles.

1. Go to your Google Cloud Platform (GCP), [create a service account](https://cloud.google.com/iam/docs/service-accounts-create#iam-service-accounts-create-console), and grant an Identity and Access Management (IAM) role with the following permissions:

   Permissions for the IAM role

   ```
   storage.buckets.get  
   storage.objects.create  
   storage.objects.delete  
   storage.objects.get  
   storage.objects.list
   ```
2. [Obtain the JSON file](https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account) with the GCP credentials from the Google service account.
3. Create the Kubernetes secret where Dremio is deployed using the following command:

   Run kubectl to create the Kubernetes secret

   ```
   kubectl create secret generic catalog-server-gcs-storage-creds --from-file=<filename>.json
   ```

## Update an Open Catalog Source

To update an Open Catalog source:

1. On the Datasets page, in the panel on the left, find the name of the Open Catalog source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the Source Settings dialog, edit the settings you wish to update. Dremio does not support updating the source name.
4. Click **Save**. Once you have configured Open Catalog, the Catalog REST APIs are accessible via `http://{DREMIO_ADDRESS}:8181/api/catalog`, where `DREMIO_ADDRESS` is the IP address of your Dremio cluster.

## Using the Open Catalog with Multiple Storage Locations

You can use one Open Catalog instance to work with data stored in multiple storage buckets. For example, you can create different folders (namespaces) in one Open Catalog instance, such that data in Folder A is stored in Storage Bucket 1, and data in Folder B is stored in Storage Bucket 2. This feature is named **Storage URIs (Uniform Resource Identifiers)**.

A Storage URI is an optional attribute that can be attached to a folder and consists of a path to an object storage location. When you create a folder, you can either configure the folder to use the "inherited" storage location you defined when you configured Open Catalog or when you set the Storage URI on one of its parent folders, or you can configure the folder to use a custom Storage URI. To configure the folder to use a custom Storage URI, add the path to the object storage location you would like to use during folder creation. Ensure that the storage credentials you are using for the Open Catalog can access the object storage location you added for your newly created folder.

### Storage URIs Example

The diagram below depicts an Open Catalog that contains two namespaces (`NS1`, `NS2`), where its underlying folders utilize Storage URIs to store data in custom storage locations:

![](/images/open-catalog-storage-uris.png)

In this example:

1. TBL1 would be stored in `<Uri1>/NS3/TBL1`
2. TBL3 would be stored in `<Uri2>/NS5/NS6/TBL3`
3. TBL4 would be stored in `<Default URI>/NS2/TBL4`

When creating a table from an [external Open Catalog](/current/data-sources/lakehouse-catalogs/open-catalog-external/) source, the default Storage URI that the table will use is the root path of the external Open Catalog source, unless one of the folders on the table's path has been set with a custom Storage URI.

Was this page helpful?

[Previous

Manage Sources](/current/data-sources/)[Next

Connect to Open Catalog from Apache Spark](/current/data-sources/open-catalog/connecting-from-spark)

* Prerequisites
* Configure the Open Catalog
  + Storage
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Configure Storage Access
  + S3 and STS Access via IAM Role (Preferred)
  + S3 and STS Access via Access Key
* Update an Open Catalog Source
* Using the Open Catalog with Multiple Storage Locations
  + Storage URIs Example

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/

Version: current [26.x]

# Lakehouse Catalogs

The following lakehouse catalogs are supported as data sources in Dremio:

* [Open Catalog (External)](/current/data-sources/lakehouse-catalogs/open-catalog-external/)
* [AWS Glue Data Catalog](/current/data-sources/lakehouse-catalogs/aws-glue-catalog/)
* [Microsoft OneLake](/current/data-sources/lakehouse-catalogs/onelake)
* [Snowflake Open Catalog](/current/data-sources/lakehouse-catalogs/snowflake-open/)
* [Unity Catalog](/current/data-sources/lakehouse-catalogs/unity/)
* [Iceberg REST Catalog](/current/data-sources/lakehouse-catalogs/iceberg-rest-catalog/)
* [Hive](/current/data-sources/lakehouse-catalogs/hive/)
* [Nessie](/current/data-sources/lakehouse-catalogs/nessie/)

Was this page helpful?

[Previous

Connect to Open Catalog from Apache Spark](/current/data-sources/open-catalog/connecting-from-spark)[Next

Open Catalog (External)](/current/data-sources/lakehouse-catalogs/open-catalog-external)

---

# Source: https://docs.dremio.com/current/data-sources/object/

Version: current [26.x]

# Object Storage

You can run queries directly on the data in your data lake by formatting directories and files into tables. The following types of object storage are supported:

* [Amazon S3](/current/data-sources/object/s3/)
* [Azure Storage](/current/data-sources/object/azure-storage/)
* [Google Cloud Storage](/current/data-sources/object/gcs/)
* [HDFS](/current/data-sources/object/hdfs/)
* [NAS](/current/data-sources/object/nas/)

Was this page helpful?

[Previous

Lakehouse Catalogs](/current/data-sources/lakehouse-catalogs/)[Next

Amazon S3](/current/data-sources/object/s3)

---

# Source: https://docs.dremio.com/current/data-sources/databases/

Version: current [26.x]

# Databases

You can run queries directly against relational databases, NoSQL databases, and data warehouses, referred to in Dremio as databases. Using these databases, you can perform “external queries.” External queries use native syntax for a source and can be used for SQL statements that are not supported directly in Dremio or are too complex to convert.

The following databases are supported:

* [Amazon OpenSearch Service](/current/data-sources/databases/opensearch)
* [Amazon Redshift](/current/data-sources/databases/redshift/)
* [Apache Druid](/current/data-sources/databases/apache-druid/)
* [Dremio Cluster](/current/data-sources/databases/dremio/)
* [Google BigQuery](/current/data-sources/databases/google-bigquery/)
* [Elasticsearch](/current/data-sources/databases/elasticsearch/)
* [IBM Db2](/current/data-sources/databases/ibm-db2/)
* [Microsoft Azure Data Explorer](/current/data-sources/databases/azure-data-explorer/)
* [Microsoft Azure Synapse Analytics](/current/data-sources/databases/azure-synapse-analytics/)
* [Microsoft SQL Server](/current/data-sources/databases/sql-server/)
* [MongoDB](/current/data-sources/databases/mongo/)
* [MySQL](/current/data-sources/databases/mysql/)
* [Oracle](/current/data-sources/databases/oracle/)
* [PostgreSQL](/current/data-sources/databases/postgres/)
* [SAP HANA](/current/data-sources/databases/sap-hana/)
* [Snowflake](/current/data-sources/databases/snowflake/)
* [Teradata](/current/data-sources/databases/teradata)
* [Vertica](/current/data-sources/databases/vertica)

Was this page helpful?

[Previous

Object Storage](/current/data-sources/object/)[Next

Amazon OpenSearch Service](/current/data-sources/databases/opensearch)

---

# Source: https://docs.dremio.com/current/data-sources/file-upload

Version: current [26.x]

On this page

# Upload Files

You can upload files to your home space for experimentation. Excel, JSON, Parquet, and CSV files are supported for upload. Once it is uploaded, you can query the file just like a table by specifying the path, "@[home-space-name].[file-name]".

## Upload File to Your Home Space

1. In the Dremio console, navigate to your home space by clicking on the home icon and your username.
2. Click ![This is the Add icon to upload a file or add a folder.](/images/icons/add.png "Add a folder or upload a file.") in the upper right side and select **Upload File**.
3. Select the file and click **Next**. If the file is large, it may take a few moments to upload, depending on your connection speed.
4. (Optional) During the upload process, configure the file settings. For example, configure how the file is delimited.
5. Click **Save**.

Once the file has been uploaded, it is displayed in your home space as a table. You can query it by running `SELECT * FROM "@username"."table_name"`.

## Limits

* Uploaded files are copies of your local file. Updates to your local file are not automatically reflected in Dremio.
* Bulk upload of multiple files is not supported.
* Files uploaded to your home space cannot be shared with other users. To share it with others, upload the file into a shared source or use [COPY INTO](/current/reference/sql/commands/apache-iceberg-tables/copy-into-table/) to create an Iceberg table in your Open Catalog.

Was this page helpful?

[Previous

Vertica](/current/data-sources/databases/vertica)[Next

Load Data](/current/load-data/)

* Upload File to Your Home Space
* Limits

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/aws-glue-catalog/

Version: current [26.x]

On this page

# AWS Glue Data Catalog

Dremio supports Amazon S3 datasets cataloged in [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) as a Dremio data source. Files in S3 must be one of the following file formats or table formats:

* Apache Iceberg
* Delimited text files (CSV/TSV)
* Delta Lake (Dremio supports reading Native Delta Lake tables in AWS Glue. Delta Lake symlink tables must be crawled and native Delta Lake tables created from them. See [Introducing native Delta Lake table support with AWS Glue crawlers](https://aws.amazon.com/blogs/big-data/introducing-native-delta-lake-table-support-with-aws-glue-crawlers/) in the AWS Big Data blog.)
* ORC
* Parquet

AWS Glue data sources added to projects default to using the Apache Iceberg table format. When upgrading, AWS Glue data sources added to projects before Dremio 22 are modified to use the Apache Iceberg table format as the default format.

## AWS Glue Credentials

Dremio administrators need credentials to access files in Amazon S3 and list databases and tables in the AWS Glue Catalog. Dremio recommends using the provided sample [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) when configuring a new AWS Glue Catalog data source. See Dremio Configuration for more information about supported authentication mechanisms.

Dremio reads the table metadata from AWS Glue and directly scans the data on S3 using its high-performance, massively parallel processing (MPP) engine. For this reason, you need to give permissions to connect to Glue as well as the permissions to read the data on S3 for those tables.

## AWS IAM Policy for Accessing Amazon S3 and AWS Glue

Dremio recommends using the following AWS managed policy:

IAM policy for accessing Amazon S3 and AWS Glue

```
{  
    "Version": "2012-10-17",  
    "Statement": [  
        # Allow Dremio to run the listed AWS Glue API operations.  
        {  
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
        # Allow Dremio to read and write files in a bucket.  
        {  
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
        # Allow Dremio to access the Amazon S3 buckets or folders with names containing either the 'aws-glue-' or 'crawler-public' prefixes.  
        {  
            "Effect": "Allow",  
            "Action": [  
                "s3:GetObject"  
            ],  
            "Resource": [  
                "arn:aws:s3:::crawler-public*",  
                "arn:aws:s3:::aws-glue-*"  
            ]  
        },  
        # Allow Dremio to create or delete tags in the AWS Glue catalog.  
        {  
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

## Configuring AWS Glue Data Catalog as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **AWS Glue Data Catalog**.

### General

Users with proper [privileges](/current/security/rbac/) can configure access to AWS Glue Catalog with one of the three authentication methods.

#### Name

Specify a name for the data source. You cannot change the name after the source is created. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### AWS Region Selection

Specify a region from which you want to see the tables from AWS Glue. Only tables from this region will be shown after the connection is made.

#### Authentication

Choose one of the following authentication methods:

* AWS Access Key: All or allowed (if specified) buckets associated with this access key or IAM role to assume, if provided, will be available.
  + Under **AWS Access Key**, enter the [AWS access key ID](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).
  + Under **AWS Access Secret**, provide the [AWS access secret](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) using one of the following methods:
    - Dremio: Provide the access secret in plain text. Dremio stores the access secret.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the access secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the access secret reference in the correct format.
  + Under **IAM Role to Assume**, enter the [IAM role](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html) that Dremio should assume in conjunction with the AWS Access Key authentication method.
* EC2 Metadata: All or allowed (if specified) buckets associated with the specified IAM role attached to EC2 or IAM role to assume, if provided, will be available.
  + Under **IAM Role to Assume**, enter the [IAM role](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html) that Dremio should assume in conjunction with the EC2 Metadata authentication method.
* EKS Pod Identity: Dremio can access all S3 buckets linked to the IAM role associated with the Kubernetes service account or the assumed IAM role. If you specify certain buckets, only those will be available.
  + Under **IAM Role to Assume**, enter the [IAM role](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html) that Dremio should assume when using the Pod Identity authentication method.
* AWS Profile: Dremio sources profile credentials from the specified AWS profile. For information on how to set up a configuration or credentials file for AWS, see [AWS Custom Authentication](/current/data-sources/object/s3#aws-custom-authentication).
  + AWS profile (optional): The AWS profile name. If this is left blank, then the default profile will be used. For more information about using profiles in a credentials or configuration file, see AWS's documentation on [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

The **Encrypt connection** option is enabled by default to encrypt the connection to AWS Glue. Clear the checkbox to disable encryption.

#### Allowed Databases

The allowed databases configuration is a post-connection filter on the databases visible from AWS Glue. When selective access to the databases within AWS Glue is required, the allowed databases filter will limit access within Dremio to only the needed databases per source connection, thus improving data security and source metadata refresh performance.

When the allowed database filter is empty, all databases from the AWS Glue source are visible in Dremio. When a database is added or removed from the filter, Dremio performs an asynchronous update to expose new databases and remove databases not included in the filter. Each entry in the allowed database filter must be a valid database name; misspelled or nonexistent databases are ignored.

### Advanced Options

All configurations are optional.

#### Connection Properties

A list of additional connection properties that can be specified to use with the connection.

##### Locations in which Iceberg Tables are Created

Where the CREATE TABLE command creates an Iceberg table depends on the type of data source being used. For AWS Glue Data Sources, the root directory is assumed by default to be `/user/hive/warehouse`. If you want to create tables in a different location, you must specify the S3 address of an Amazon S3 bucket in which to create them:

1. On the Advanced Options page of the Edit Source dialog, add this connection property: `hive.metastore.warehouse.dir`.
2. Set the value to the S3 address of an S3 bucket.

The schema path and table name are appended to the root location to determine the default physical location for a new Iceberg table.

#### Lake Formation Integration

Lake Formation provides access controls and allows administrators to define security policies. Enabling this functionality and additional details on the configuration options below are described in more detail on the [Integrating with Lake Formation](/current/security/integrations/lake-formation/) page.

* **Enforce AWS Lake Formation access permissions on datasets.** Dremio checks any datasets included in the AWS Glue source for the required permissions to perform queries.
* **Prefix to map Dremio users to AWS ARNs.** Leave blank to default to the end user's username, or enter a REGEX expression.
* **Prefix to map Dremio groups to AWS ARNs.** Leave blank to default to the end user's group, or enter a REGEX expression.

### Reflection Refresh

Specify how frequently Dremio refreshes Data Reflections based on the AWS Glue data source in the `Reflection Refresh` tab. Dremio refreshes every hour and expires after three hours by default.

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

Specify how and how frequently Dremio refreshes metadata on the `Metadata` tab. By default, Dremio fetches top-level objects and dataset details every hour. Dremio retrieves details only for queried datasets by default to improve query performance.

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an AWS Glue Data Catalog Source

To update an AWS Glue Data Catalog source:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring AWS Glue Data Catalog as a Source.
4. Click **Save**.

## Deleting an AWS Glue Data Catalog Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an AWS Glue Data Catalog source, perform these steps:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

Was this page helpful?

[Previous

Open Catalog (External)](/current/data-sources/lakehouse-catalogs/open-catalog-external)[Next

Microsoft OneLake](/current/data-sources/lakehouse-catalogs/onelake)

* AWS Glue Credentials
* AWS IAM Policy for Accessing Amazon S3 and AWS Glue
* Configuring AWS Glue Data Catalog as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an AWS Glue Data Catalog Source
* Deleting an AWS Glue Data Catalog Source

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/open-catalog-external

Version: current [26.x]

On this page

# Open Catalog (External) Enterprise

The Open Catalog (External) source enables you to connect to Open Catalogs deployed in other Dremio instances. Connectivity to the external Open Catalog is achieved using the Iceberg REST API. Once connectivity is established, users can read from and write to external catalogs. Additionally, user impersonation and vended credentials are enabled by default, providing a consistent governance and security experience across your Dremio deployments.

Key use cases for connecting to external Open Catalogs include:

* **Cross-cluster data federation**: Query and join data from multiple Dremio deployments as if they were local tables, enabling unified analytics across geographically distributed or organizationally separate clusters.
* **Data mesh architecture**: Connect domain-specific Dremio clusters (e.g., finance, marketing, operations) while maintaining data ownership boundaries, allowing controlled cross-domain data access and collaboration.
* **Hybrid cloud analytics**: Access data from on-premises Dremio clusters while running analytics workloads in cloud-based clusters, or vice versa, supporting gradual cloud migration strategies.
* **Environment promotion workflows**: Connect production analytics clusters to development/staging Dremio instances to validate queries, test data products, or promote curated datasets across environments.
* **Multi-tenant analytics**: Enable secure data sharing between different business units or customers, each with their own Dremio cluster, while maintaining isolation and access controls.

When connecting to an external Open Catalog:

* **Query processing**: All local queries run on local engines only. The local Dremio directly reads and writes data from the external catalog's object store but does not delegate processing to the external Dremio cluster. The external Dremio can process queries on its own engines.
* **User authentication**: With impersonation enabled, the local Dremio passes the current user's identity to the external Dremio for privilege checks. User accounts must exist on both clusters with matching identities. Using a shared identity provider (such as LDAP or OIDC) across both clusters simplifies this requirement.
* **Network requirements**: The local Dremio needs direct network access to both the external Dremio catalog and the external catalog's object store (such as S3 or ADLS) to read and write data.

## Configure the External Dremio

1. Log in to the external Dremio as the administrator.
2. Create a service account that will be used to accept Open Catalog connections.
3. Create an [Inbound Impersonation policy](/current/security/rbac/inbound-impersonation) that allows the service user to impersonate the users or groups who will be issuing queries. When creating the impersonation policy, the service account is configured as the `proxy_principal`, and the users or groups submitting data requests are the `target_principals`. The `target_principal` users and groups must match on the local and external Dremio clusters.

   Example Inbound Impersonation Policy

   ```
   ALTER SYSTEM SET "exec.impersonation.inbound_policies"='[  
      {  
         proxy_principals:{  
            users:["service-account"]  
         },  
         target_principals:{  
            groups:["external-catalog-users"]  
         }  
      }  
   ]'
   ```
4. Grant the service account the `USAGE` privilege on each folder and `SELECT` on the catalog:

   * `GRANT USAGE ON CATALOG <external-catalog> TO USER <service-account>`
   * `GRANT USAGE` on each folder in the catalog `TO USER <service-account>`
   * `GRANT SELECT ON CATALOG <external-catalog> TO USER <service-account>`
5. Grant catalog or dataset permissions to the `target_principal` users or groups. The privileges of the `target_principals` will determine whether a data request from that user is granted.
6. Log in to the external Dremio as the new service account and generate a [personal access token (PAT)](/current/security/authentication/personal-access-tokens). This PAT will be used to create connections to the external Dremio.

## Configure the Local Dremio

On the Datasets page, to the right of **Sources** in the left panel, click ![Add Source icon](/images/icons/plus.png "Add Source icon").

In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Open Catalog (External)**.

### General

To configure the source connection:

1. **Name**: Enter a name for the source. The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: `0-9`, `A-Z`, `a-z`, underscore `_`, or hyphen `-`.
2. **Open Catalog Endpoint URL**: Specify the Open Catalog endpoint URL of the target Open Catalog. An example is `http://dremio.example.com:8181/api/catalog`.
3. **OAuth Token Endpoint**: Specify the OAuth token endpoint of the target Dremio. An example for this endpoint is `http://dremio.example.com:9047/oauth/token`.
4. **PAT Token**: Specify the PAT created in the target cluster for the `service-account`. This PAT is used to authenticate to the cluster.
5. **Allow Impersonation**: Enabled by default. This setting directs Dremio to execute queries as the user that submits them, utilizing the inbound impersonation policy created on the external Dremio. If user impersonation is disabled, the source credentials will be used to access the catalog.

### Storage

1. Use the **Storage access** field to configure your preferred authentication method. Open Catalog (External) supports two types of credentials for authentication:
   * **Use credential vending (Recommended)**: Credential vending is a security mechanism where the catalog service issues temporary, scoped access credentials to the query engine for accessing table storage. The engine is "vended" a temporary credential just in time for the query.
   * **Use master storage credentials**: Enter the credentials for accessing all storage URIs within this catalog. If the Iceberg tables' data resides in storage locations other than those listed, Dremio will not be able to access the data.
     + **AWS** – Select **AWS** for Amazon S3 and S3-compatible storage. You can refer to the Dremio documentation for connecting to [Amazon S3](/current/data-sources/object/s3/#configuring-amazon-s3-as-a-source), which is also applicable here. When selecting to assume an IAM role, ensure that the [role policy grants access](/current/data-sources/open-catalog/#configure-storage-access) to the bucket or folder specified by the external catalog.
     + **Azure** – Select **Azure** for Azure Blob Storage. You can refer to the Dremio documentation for connecting to [Azure Storage](/current/data-sources/object/azure-storage/#configuring-azure-storage-as-a-source), which is also applicable here.
     + **Google Cloud Storage** – Select **Google** for Google Cloud Storage (GCS). You can refer to the Dremio documentation for connecting to [GCS](/current/data-sources/object/gcs/#configuring-gcs-as-a-source), which is also applicable here.
2. The **Connection Properties** are the same as the Advanced Options connection properties from the selected object storage provider above. Refer to the documentation links for your chosen provider (S3, Azure, or GCS) for details on available connection properties and their configuration.

### Advanced Options

#### Cache Options

* **Enable local caching when possible**: Selected by default. Along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details.
* **Max percent of total available cache space to use when possible**: Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage.

### Reflection Refresh

You can set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed. See the following options.

#### Refresh Settings

* **Never refresh**: Select to prevent automatic reflection refresh. The default is to refresh automatically.
* **Refresh every**: How often to refresh reflections, specified in hours, days, or weeks. This option is ignored if **Never refresh** is selected.
* **Set refresh schedule**: Specify the daily or weekly schedule.

#### Expire Settings

* **Never expire**: Select to prevent reflections from expiring. The default is to expire automatically after the time limit below.
* **Expire after**: The time limit after which reflections expire and are removed from Dremio, specified in hours, days, or weeks. This option is ignored if **Never expire** is selected.

### Metadata

Specifying metadata options is handled with the following settings.

#### Dataset Handling

* Remove dataset definitions if the underlying data is unavailable (default).
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and then replaced with new sets of files.

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**:
  + **Fetch every**: The refresh interval for fetching top-level source object names, such as databases and tables. Set the time interval using this parameter. You can choose to set the frequency for fetching object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour.
* **Dataset Details**: The metadata that Dremio needs for query planning, such as information needed for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information:
  + **Fetch mode**: You can choose to fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**.
  + **Fetch every**: You can choose to set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour.
  + **Expire after**: You can choose to set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours.

### Privileges

You have the option to grant privileges to specific users or roles. See [Access Control](/current/security/rbac/) for additional information about privileges.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an Open Catalog (External)

To update an Open Catalog (External) source:

1. On the Datasets page, under **Sources** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![Settings icon](/images/settings-icon.png "Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name.
4. Click **Save**.

## Deleting an Open Catalog (External) Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Open Catalog (External) source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

Was this page helpful?

[Previous

Lakehouse Catalogs](/current/data-sources/lakehouse-catalogs/)[Next

AWS Glue Data Catalog](/current/data-sources/lakehouse-catalogs/aws-glue-catalog)

* Configure the External Dremio
* Configure the Local Dremio
  + General
  + Storage
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an Open Catalog (External)
* Deleting an Open Catalog (External) Source

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/hive/

Version: current [26.x]

On this page

# Hive

This topic describes Hive data source considerations and Dremio configuration.

## Dremio and Hive

Dremio supports the following:

* Hive 2.1
* Hive 3.x

### Data Sources

The following data sources are supported:

* HDFS
* Azure Storage
* S3 - See [S3 on Amazon EMR Configuration](/current/data-sources/lakehouse-catalogs/hive/hive-s3/) for more information about S3-backed Hive tables on Amazon EMR.
* Hive external tables backed by HBase storage handler

### Formats

The following formats are supported:

* Apache Avro
* Apache Iceberg
* Apache Parquet
* Delta Lake
* ORC
* RCFile
* SequenceFile
* Text, including CSV (Comma-separated values)

In addition, the following interfaces and reading file formats are supported:

* Hive table access using Hive's out-of-the-box SerDes interface, as well as custom SerDes or InputFormat/OutputFormat.
* Hive-supported reading file format using Hive's own readers -- even if Dremio does not support them natively.

  note

  Dremio does ***not*** support Hive views. However, you can create and query [views](/current/what-is-dremio/key-concepts#tables--views) instead.

## Hive Configuration

This section provides information about Hive configuration.

### Adding additional elements to Hive plugin classpaths

Hive plugins can be extended to use additional resource files and classes.
The plugins can be added as either directories or JAR files. Note that any resources
that are part of the server's classpath are not exposed to the Hive plugin.

To add additional classpath elements, follow these steps on every node of your Dremio cluster:

1. Create the following directory:  
    `<dremio-root>/plugins/connectors/<hive-plugin-id>.d/`  
   where:

   * `<dremio-root>` is the root directory of the Dremio instance.
   * `<hive-plugin-id>` is either of these values:

     + If you are using Dremio Community/OSS and either Hive 2 or Hive 3: `hive3`
     + If you are using Dremio Enterprise and either Hive 2 or Hive 3: `hive3-ee`
2. Either place each JAR file in the new directory or add a symlink to each JAR file from the new directory.
3. Either place a copy of each resource directory in the new directory or add a symlink to each resource directory from the new directory.
4. Ensure the directory and its contents are readable by the Dremio process user.

### Configuration Files

Hive plugins do not use elements present in the main
Dremio server classpath. This includes any Hadoop/Hive configuration files such as
core-site.xml and hive-site.xml that the user may have added themselves.

You can add these files to the Hive plugin classpath by following the instructions above.

For example you can create conf files here:
`<dremio-root>/plugins/connectors/**hive3-ee.d**/conf` for the Hive 3 plugin
in Enterprise mode.

An easy way to use the same configuration as Dremio is to use a symlink. From `<dremio-root>`:

Use symlink

```
ln -s conf plugins/connectors/hive3-ee.d/conf
```

### Impersonation

note

If you are using Ranger-based authorization for your Hive source, refer to Disabling Impersonation for Ranger-Based Authorization.

To grant the Dremio service user the privilege to connect from any host and to impersonate a user belonging to any group,
modify the **core-site.xml** file with the following values:

Grant user impersonation privileges

```
<property>  
  <name>hadoop.proxyuser.dremio.hosts</name>  
  <value>*</value>  
</property>  
<property>  
  <name>hadoop.proxyuser.dremio.groups</name>  
  <value>*</value>  
</property>  
<property>  
  <name>hadoop.proxyuser.dremio.users</name>  
  <value>*</value>  
</property>
```

To modify the properties to be more restrictive by passing actual hostnames and group names,
modify the **core-site.xml** file with the following values:

Grant more restrictive user impersonation privileges

```
<property>  
  <name>hadoop.proxyuser.super.hosts</name>  
  <value>10.222.0.0/16,10.113.221.221</value>  
</property>  
<property>  
  <name>hadoop.proxyuser.dremio.users</name>  
  <value>user1,user2</value>  
</property>
```

#### Disabling Impersonation for Ranger-Based Authorization

If you are using Ranger-based authorization, we recommend that you disable impersonation for your Hive source:

1. In the Dremio console, open the **Source Settings** for the Hive source and click **Advanced Options**.
2. Under **Connection Properties**, add the property `hive.server2.enable.doAs` in the **Name** field and add the setting `false` in the **Value** field.
3. Click **Save**.

### Table Statistics

By default, Dremio utilizes its own estimates for Hive table statistics when planning queries.

However, if you want to use Hive's own statistics, do the following:

1. Set the `store.hive.use_stats_in_metastore` parameter to true.  
   Example: `true`: `store.hive.use_stats_in_metastore`
2. Run the `ANALYZE TABLE COMPUTE STATISTICS` command for relevant Hive tables in Hive.
   This step is required so that all of the tables (that Dremio interacts with), have up-to-date statistics.

ANALYZE TABLE COMPUTE STATISTICS command

```
ANALYZE TABLE <Table1> [PARTITION(col1,...)] COMPUTE STATISTICS;
```

### Hive Metastores

If you are using a Hive source and an HA metastore (multiple Hive metastores),
then you need to specify the following `hive.metastore.uris` parameter and value in the **hive-site.xml** file.

Specify hive.metastore.uris

```
<name>hive.metastore.uris</name>  
<value>thrift://metastore1:9083,thrift://metastore2:9083</value>
```

## Configuring Hive as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Metastores**, select **Hive 2.x** or **Hive 3.x**.

### General Options

* **Name** -- Hive source name. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
* **Connection** -- Hive connection and security

  + Hive Metastore Host -- IP address. Example: 123.123.123.123
  + Port -- Port number. Default: 9083
  + Enable SASL -- Box to enable SASL. If you enable SASL, specify the Hive Kerberos Principal.
* **Authorization** -- Authorization type for the client.
  When adding a new Hive source, you have the following client options for Hive authorization:

  + Storage Based with User Impersonation -- A storage-based authorization in the Metastore Server
    which is commonly used to add authorization to metastore server API calls.
    Dremio utilizes user impersonation to implement Storage Based authorization

    - When **Allow VDS-based Access Delegation** is enabled (default),
      the owner of the view is used as the impersonated username.
    - When **Allow VDS-based Access Delegation** is disabled (unchecked),
      the query user is used as the impersonated username.
  + SQL Based -- **Not Currently Supported**
  + Ranger Based -- An Apache Ranger plug-in that provides a security framework for authorization.

    - Ranger Service Name - This field corresponds to the security profile in Ranger. Example: `hivedev`
    - Ranger Host URL - This field is the path to the actual Ranger server. Example: `http://yourhostname.com:6080`

### Advanced Options

The following options allow you to specify either impersonsation users and Hive connection properties.

For example, to add a new Hive source, you can specify a single metastore host
by adding a `hive.metastore.uris` parameter and value in the Hive connection properties.
This connection property overrides the value specified in the Hive source.

note

**Multiple Hive Metastore Hosts:** If you need to specify multiple Hive metastore hosts, update the **hive-site.xml** file.
See Hive Metastores for more information.

* **Impersonation User Delegation** -- Specifies whether an impersonation username is As is (Default), Lowercase, or Uppercase
* **Connection Properties** -- Name and value of each Hive connection property.
* **Credentials** -- Name and hidden value of each Hive connection property for which you want to keep the value secret.

![Dremio Advanced Options](/assets/images/hive-adv-options-700333cdd76fb673870898376d244a26.png)

#### Kerberized Hive

To connect to a Kerberized Hive source, add the following connection property in the Advanced Options:

| Property | Description | Value |
| --- | --- | --- |
| yarn.resourcemanager.principal | Name of the Kerberos principal for the YARN resource manager. | `<user>/<localhost>@<YOUR-REALM.COM>` |

### Reflection Refresh

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

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

  + Fetch mode -- Specify either Only Queried Datasets, or All Datasets. Default: Only Queried Datasets

    - Only Queried Datasets -- Dremio updates details for previously queried objects in a source.  
      This mode increases query performance because less work is needed at query time for these datasets.
    - All Datasets -- Dremio updates details for all datasets in a source.
      This mode increases query performance because less work is needed at query time.
  + Fetch every -- Specify fetch time based on minutes, hours, days, or weeks. Default: 1 hour
  + Expire after -- Specify expiration time based on minutes, hours, days, or weeks. Default: 3 hours
* **Authorization** -- Used when impersonation is enabled.
  Specifies the maximum of time that Dremio caches authorization information before expiring.

  + Expire after - Specifies the expiration time based on minutes, hours, days, or weeks. Default: 1 day

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Hive Source

To update a Hive source:

1. On the Datasets page, under **Metastores** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Hive as a Source.
4. Click **Save**.

## Deleting a Hive Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Hive source, perform these steps:

1. On the Datasets page, click **Sources** > **Metastores** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## For More Information

See [Hive Data Types](/current/reference/sql/data-types/mappings/hive/) for information about mapping to Dremio data types.

Was this page helpful?

[Previous

Iceberg REST Catalog](/current/data-sources/lakehouse-catalogs/iceberg-rest-catalog)[Next

Nessie](/current/data-sources/lakehouse-catalogs/nessie)

* Dremio and Hive
  + Data Sources
  + Formats
* Hive Configuration
  + Adding additional elements to Hive plugin classpaths
  + Configuration Files
  + Impersonation
  + Table Statistics
  + Hive Metastores
* Configuring Hive as a Source
  + General Options
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Hive Source
* Deleting a Hive Source
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/iceberg-rest-catalog/

Version: current [26.x]

On this page

# Iceberg REST Catalog Enterprise

The Iceberg REST Catalog source allows you to connect to your Iceberg Metastores via the Iceberg REST API. This may require configuring specific Advanced Options to set up the correct authentication flows.

## Configuring an Iceberg REST Catalog Source

To add an Iceberg REST Catalog source:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "Add Source icon").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Iceberg REST Catalog Source**.

   The New Iceberg REST Catalog Source dialog box appears, which contains the following tabs:

   * **General**: Create a name for your Iceberg REST Catalog source, specify the endpoint URI, and set the authentication Vended credentials (on by default).
   * **Advanced Options**: Use catalog properties and credentials to set up storage authentication and authorization.
   * **Reflection Refresh**: (Optional) Set a policy to control how often Reflections are refreshed and expired.
   * **Metadata**: (Optional) Specify dataset handling and metadata refresh.
   * **Privileges**: (Optional) Add privileges for users or roles.

   Refer to the following sections for guidance on how to edit each tab.

### General

To configure the source connection:

1. For **Name**, enter a name for the source.

   note

   The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore(\_), or hyphen (-)
2. For **Endpoint URI**, specify the catalog service URI.
3. By default, **Use vended credentials** is turned on. This allows Dremio to connect to the catalog and receive temporary credentials for the underlying storage location. When this setting is enabled, you don't need to add the storage authentication in **Advanced Options**.

   note

   If you experience errors using vended credentials, please turn the setting off and provide credentials via **Advanced Options** to establish a connection.
4. (Optional) For **Allowed Namespaces**, add each namespace and check the option if you want to include their whole subtrees. Tables are organized into namespaces, which can be at the top level or nested within one another. Namespace names cannot contain periods or spaces.

### Advanced Options

To set the advanced options:

1. (Optional) For **Catalog Properties** and **Catalog Credentials**, you can manually provide the storage authentication if you choose to not use vended credentials.

   Dremio supports Amazon S3 and Azure Storage as object storage services. For acceptable storage authentication configurations, see the following catalog properties and credentials for each service option.

   **Amazon S3 Access Key**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | property | `fs.s3a.aws.credentials.provider` | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` | Required field for a Iceberg REST Catalog source |
   | credential | `fs.s3a.access.key` | `<your_access_key>` | AWS access key ID used by S3A file system. Omit for IAM role-based or provider-based authentication |
   | credential | `fs.s3a.secret.key` | `<your_secret_key>` | AWS access key used by S3A file system. Omit for IAM role-based or provider-based authentication |

   **Amazon S3 Assumed Role**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | property | `fs.s3a.assumed.role.arn` | `arn:aws:iam::*******:role/OrganizationAccountAccessRole` | AWS ARN for the role to be assumed |
   | property | `fs.s3a.aws.credentials.provider` | `com.dremio.plugins.s3.store.STSCredentialProviderV1` | Required field for an Iceberg REST Catalog source |
   | property | `fs.s3a.assumed.role.credentials.provider` | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` | Use only if the credential provider is `AssumedRoleCredentialProvider`; lists credential providers to authenticate with the STS endpoint and retrieve short-lived role credentials |

   **Azure Storage Shared Key**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | credential | `fs.azure.account.key` | `<your_account_key>` | Storage account key |
2. Under **Cache Options**, review the following table and edit the options to meet your needs.

   | Cache Options | Description |
   | --- | --- |
   | **Enable local caching when possible** | Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details. |
   | **Max percent of total available cache space to use when possible** | Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter in a percentage in the value field or use the arrows to the far right to adjust the percentage. |

### Reflection Refresh

You can set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed. See the following options.

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
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

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

You have the option to grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an Iceberg REST Catalog Source

To update an Iceberg REST Catalog:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the Source Settings dialog, edit the settings you wish to update. Dremio does not support updating the source name.
4. Click **Save**.

## Deleting an Iceberg REST Catalog Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Iceberg REST Catalog source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Supported Configurations

The list below contains supported configurations that have been tested with Dremio. The tables outline the parameters needed to connect to the various catalogs. These configurations can be adjusted into REST API calls using the `RESTCATALOG` source type and the `propertyList` and `secretPropertyList` property groups.

All the values below for URI, warehouse, and credentials are example values. These values will need to be changed based on your environment.

---

### Apache Polaris OSS Backed by S3

| UI Tab | Field | Value |
| --- | --- | --- |
| General | Endpoint URI | `<http://localhost:8181/api/catalog>` |
| General | Use vended credentials | Unchecked |
| Advanced Options - Catalog Properties | warehouse | `<polaris_oss_catalog>` |
| Advanced Options - Catalog Properties | scope | `PRINCIPAL_ROLE:ALL` |
| Advanced Options - Catalog Properties | fs.s3a.aws.credentials.provider | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` |
| Advanced Options - Catalog Credentials | fs.s3a.access.key | `<s3AccessKey>` |
| Advanced Options - Catalog Credentials | fs.s3a.secret.key | `<s3SecretKey>` |
| Advanced Options - Catalog Credentials | credential | `<client_id:client_secret>` |

---

### Nessie Catalog Backed by S3

| UI Tab | Field | Value |
| --- | --- | --- |
| General | Endpoint URI | `<http://127.0.0.1:19120/iceberg/>` |
| General | Use vended credentials | Unchecked |
| Advanced Options - Catalog Properties | warehouse | `<s3://mybucket/restcatalog/>` |
| Advanced Options - Catalog Properties | fs.s3a.aws.credentials.provider | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` |
| Advanced Options - Catalog Credentials | fs.s3a.access.key | `<s3AccessKey>` |
| Advanced Options - Catalog Credentials | fs.s3a.secret.key | `<s3SecretKey>` |

---

### AWS Glue Iceberg REST Catalog

Please replace `region` uses with a valid AWS region where you are working with the Glue Iceberg REST endpoint (for example, `us-west-2`). You will also need your `AWS account number` and the name of the `Table Bucket` being used.

| UI Tab | Field | Value |
| --- | --- | --- |
| General | Endpoint URI | `<https://glue.region.amazonaws.com/iceberg>` |
| General | Use vended credentials | Unchecked |
| Advanced Options - Catalog Properties | warehouse | `<accountnumber:s3tablescatalog/tablebucketname>` |
| Advanced Options - Catalog Properties | rest.sigv4-enabled | `true` |
| Advanced Options - Catalog Properties | rest.signing-name | `glue` |
| Advanced Options - Catalog Properties | rest.signing-region | `<region>` |
| Advanced Options - Catalog Properties | fs.s3a.aws.credentials.provider | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` |
| Advanced Options - Catalog Properties | dremio.bucket.discovery.enabled | false |
| Advanced Options - Catalog Properties | dremio.s3.region | `<region>` |
| Advanced Options - Catalog Properties | fs.s3a.audit.enabled | `false` |
| Advanced Options - Catalog Properties | fs.s3a.create.file-status-check | false |
| Advanced Options - Catalog Credentials | rest.access-key-id | `<s3AccessKey>` |
| Advanced Options - Catalog Credentials | rest.secret-access-key | `<s3SecretKey>` |
| Advanced Options - Catalog Credentials | fs.s3a.access.key | `<s3AccessKey>` |
| Advanced Options - Catalog Credentials | fs.s3a.secret.key | `<s3SecretKey>` |

---

### S3 Tables Iceberg REST Catalog

Please replace `region` uses with a valid AWS region where you are working with the Glue Iceberg REST endpoint (for example, us-west-2). You will also need your `AWS account number` and the name of the `Table Bucket` being used.

| UI Tab | Field | Value |
| --- | --- | --- |
| General | Endpoint URI | `<https://s3tables.region.amazonaws.com/iceberg>` |
| General | Use vended credentials | Unchecked |
| Advanced Options - Catalog Properties | warehouse | `<arn:aws:s3tables:region:accountnumber:bucket/tablebucketname>` |
| Advanced Options - Catalog Properties | rest.sigv4-enabled | `true` |
| Advanced Options - Catalog Properties | rest.signing-name | `s3tables` |
| Advanced Options - Catalog Properties | rest.signing-region | `<region>` |
| Advanced Options - Catalog Properties | fs.s3a.aws.credentials.provider | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` |
| Advanced Options - Catalog Properties | dremio.bucket.discovery.enabled | false |
| Advanced Options - Catalog Properties | dremio.s3.region | `<region>` |
| Advanced Options - Catalog Properties | fs.s3a.audit.enabled | `false` |
| Advanced Options - Catalog Properties | fs.s3a.create.file-status-check | `false` |
| Advanced Options - Catalog Credentials | rest.access-key-id | `<s3AccessKey>` |
| Advanced Options - Catalog Credentials | rest.secret-access-key | `<s3SecretKey>` |
| Advanced Options - Catalog Credentials | fs.s3a.access.key | `<s3AccessKey>` |
| Advanced Options - Catalog Credentials | fs.s3a.secret.key | `<s3SecretKey>` |

---

### Tableflow Catalog backed by AWS

Note that namespaces for the Tableflow Catalog are the Kafka clusters within your environment.

| UI Tab | Field | Value |
| --- | --- | --- |
| General | Endpoint URI | `<https://tableflow.us-west-2.aws.confluent.cloud/iceberg/catalog/organizations/f140b886-a3e9-4e1d-ba9d-5b96b8bf4ea8/environments/env-7kn93o>` |
| General | Allowed Namespaces | `<kafkaClusterID>` |
| General | Allowed Namespaces include their whole subtrees | Unchecked |
| General | Use vended credentials | Checked |
| Advanced Options - Catalog Credentials | credential | `<api_key:secret_key>` |

Was this page helpful?

[Previous

Unity Catalog](/current/data-sources/lakehouse-catalogs/unity)[Next

Hive](/current/data-sources/lakehouse-catalogs/hive)

* Configuring an Iceberg REST Catalog Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an Iceberg REST Catalog Source
* Deleting an Iceberg REST Catalog Source
* Supported Configurations
  + Apache Polaris OSS Backed by S3
  + Nessie Catalog Backed by S3
  + AWS Glue Iceberg REST Catalog
  + S3 Tables Iceberg REST Catalog
  + Tableflow Catalog backed by AWS

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/nessie/

Version: current [26.x]

On this page

# Nessie

[Nessie](https://projectnessie.org/features/) is an intelligent metastore and catalog for Apache Iceberg. It provides a modern alternative to Hive Metastore for Iceberg tables and views and provides many advanced features for more effective data lakes. These features include:

* Adding or changing data on a versioned branch, testing that branch for quality, and merging the changes to general user availability, all within the same data lake and without impacting production data.
* Creating specialized versions of data for specific use cases.
* Atomically updating many tables, with many changes, thus eliminating data inconsistencies and aberrations in the middle of a change sequence.

## Concepts

### Architecture

The Nessie service is a lightweight Java-based REST API server. Nessie uses configurable authentication and a configurable backend datastore (which currently supports multiple database types). This architecture allows Nessie to run in one or more Docker instances according to capacity requirements. The [Nessie Helm chart](https://projectnessie.org/try/kubernetes/) deploys the front end load balancer and assists with other details such as the configuration HTTPS. The Nessie JAR file can be deployed when a single Nessie instance is required for test purposes, or for a local development or test environment.

![Nessie diagram showing how Dremio communicates with a standalone Nessie server.](/images/Nessie-diagram2.png "Nessie diagram showing how Dremio communicates with a standalone Nessie server.")

### Objects in Nessie

When working with a Nessie source, you work in or with the following objects:

* Branch: A named reference and a movable pointer to a commit.
* Folders: Used to help you organize your tables in a Nessie source.
* Tables: Contains the data from your source, formatted as rows and columns. A table can be modified by query engines that connect to your Nessie source.
* Views: A virtual table, created by running SQL statements or functions on a table or another view.

You can create and store Apache Iceberg tables and views in the Nessie catalog. No other file or source types can be stored in the Nessie catalog.

### Git-like Data Management

Nessie is a native [Apache Iceberg catalog](https://iceberg.apache.org/docs/latest/nessie/) that provides Git-like data management. As a result, data engineering teams can use commits, branches, and tags to be able to experiment on Apache Iceberg tables.

* **Commit:** A transaction affecting one or more tables or views. It may take place over a short or long period of time. Examples include:
  + Updating a table using Dremio (`INSERT`, `UPDATE`, `DELETE`, `MERGE`, `TRUNCATE`) or another engine such as Spark
  + Updating a view or the definition of a view
  + Updating the schema of a table via SQL (`ALTER TABLE`) or Spark
* **Branch:** A movable pointer to a commit. Every time you commit, the branch pointer moves forward automatically. Branches can be merged via a commit.
* **Tag:** A named commit. You can tag a commit with a specific name so that users can refer to it without specifying a commit hash.

These capabilities enable a variety of use cases such as:

* **Multi-statement transactions:** With branches, data is updated in isolation and changes are merged atomically. The updates can be performed through a single engine (for example, SQL DML statements in Dremio) or through multiple engines (for example, ingest data in Spark and delete a record in Dremio), and may span any period of time and any number of users.
* **Experimentation:** Experimenting on the live lakehouse risks exposing incorrect or inconsistent data to other users. Instead, you can easily create a sandbox branch and experiment there. Because the data is not duplicated, there is no cost to creating a sandbox. And when you are done, the branch can be either deleted or your changes can be merged into the main branch.
* **Reproducibility:** The ability to retrain machine learning models and BI dashboards based on historical data is important for reproducible research and regulation. Nessie enables any engine to access previous versions of the lakehouse by referencing a specific commit, tag (a named commit), or timestamp.
* **Governance:** Nessie provides a user interface familiar to users of GitHub and GitLab that makes it easy to see every commit in every branch, so that you don’t have to wonder who updated or deleted a table, or where a table originated.

The following illustration shows an example of a new branch that is forked from the main branch, then merged back atomically after multiple commits:

![Example of Git branching.](/images/concept-git-branching-nessie-sm.png "Example of Git branching.")

## Prerequisites

Dremio supports Nessie version 0.59.0 and later. If you have not yet set up a Nessie server and connected it with your dataset, you can choose to either set up a server in a [fast-start Docker image](https://projectnessie.org/try/docker/) or with [secure HTTPS transport in Minikube](https://projectnessie.org/guides/tls/).

When using Nessie as a source, Dremio can connect to Amazon S3 buckets, Azure Storage, Google Cloud Storage (GCS), or S3-compatible storage providers like MinIO and Dell ECS. Read Storage for details about the required credentials for connecting to each storage provider.

## Configuring Nessie as a Source

To add a Nessie source to your project:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Nessie Catalogs**, select **Nessie**.

   The New Nessie Source dialog box appears, which contains the following sections:

   * **General:** Create a name for your Nessie source, specify the endpoint URL, and set the authentication type. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
   * **Storage:** Set the storage option by setting up the authentication type and the connection properties.
   * **Advanced Options:** (Optional) Use the default settings or, optionally, configure access preferences and cache options.
   * **Privileges:** (Optional) Add privileges for users or roles.

   Refer to the following for guidance on how to edit each section.

### General

This tab provides options for configuring connections to a Nessie source.

1. In the **Name** field, enter a name.

note

The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore(\_), or hyphen (-).

2. In the **Nessie endpoint URL** field, specify the IP address and port that you have set up for your Nessie server (e.g., `https://localhost:19120/api/v2`). For more information, see [Project Nessie Configuration](https://projectnessie.org/try/configuration/).
3. Under **Nessie authentication type**, select either **None** or **Bearer**:

   * **None:** The Nessie server does not require authentication.
   * **Bearer:** Set authentication using an OpenID bearer token. For more information about setting up this type of authentication, see [Project Nessie's Authentication page](https://projectnessie.org/try/authentication/). Then, choose a method for providing the password from the dropdown menu:
     + Dremio: Provide the bearer token in plain text. Dremio stores the password.
     + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Store the bearer token securely using URI format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
     + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the bearer token, which is available in the AWS web console or using command line tools.
     + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Choose the HashiCorp secrets engine you're using from the dropdown menu and enter the secret reference for the bearer token in the correct format in the provided field.

### Storage

Nessie sources can use Amazon S3 buckets (AWS), Azure Storage (Azure), Google Cloud Storage (Google), or S3-compatible storage providers like MinIO and Dell ECS as storage.

* AWS
* Azure
* Google

To connect an Amazon S3 bucket or a S3-compatible storage provider to the Nessie source, select the **AWS** storage provider option.

#### S3 Storage

In the field under **AWS root path**, provide the root path of the S3 bucket to use. We recommend that you have either a dedicated S3 bucket or a dedicated folder in which to store Nessie objects.

#### Authentication

Under **Authentication method**, choose the method you want to use to authenticate to Amazon S3.

* **AWS Access Key**:
  + In the field under **AWS access key**, provide the access key for the Amazon S3 account.
  + Under **AWS access secret**, use the dropdown menu to choose a method for providing the access secret for the Amazon S3 account:
    - Dremio: Provide the access secret in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored access secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the access secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the access secret reference in the required format.
  + In the field under **IAM role to assume**, provide the ARN of the IAM role.
* **EC2 Metadata**: In the field under **IAM role to assume**, provide the ARN of an IAM role with privileges on the S3 bucket. This role could be attached to the EC2 instance or to an IAM role to assume for connecting to the S3 bucket. In either case, the role must provide privileges to use the S3 bucket.
* **AWS Profile**: In the field under **AWS profile (optional)**, provide the AWS Profile name. If you leave the field blank, Dremio uses the default AWS Profile.
* **No Authentication**: Select this option if no credentials are required because you are connecting the Nessie source to a public Amazon S3 bucket.

If you are connecting to S3-compatible storage like MinIO or Dell ECS, choose **AWS access key** for authentication and provide the access key and secret.

#### Other: Connection Properties

Provide the custom key-value pairs for the connection relevant to the source.

(Optional) If you are connecting to S3 storage, complete the following:

1. Click **Add Property**.
2. For **Name**, provide a connection property.
3. For **Value**, provide the corresponding value for the connection property.

If you are connecting to S3-compatible storage like MinIO or Dell ECS, complete the following:

1. Add `fs.s3a.path.style.access` and set the value to `true` This setting ensures that the request path is created correctly when using IP addresses or hostnames as the endpoint.
2. Add `fs.s3a.endpoint` property and its corresponding server endpoint value (IP address). The endpoint value cannot contain the `http(s)://` prefix nor can it start with the string `s3`. For example, if the endpoint is `http://123.1.2.3:9000`, the value is `123.1.2.3:9000`
3. Add `dremio.s3.compat` and set the value to `true`.

#### Other: Encrypt connection

Optional: To secure the connections between the Amazon S3 bucket and Dremio, select the **Encrypt connection** checkbox.

To save the configuration, click **Save**. To configure additional settings, proceed to [Advanced Options](/current/data-sources/lakehouse-catalogs/nessie#advanced-options).

To connect Azure Storage to the Nessie source, select the **Azure** storage provider option.

#### Azure Storage

* In the field under **Storage Account Name**, provide the name of the Azure Storage account to use.
* In the field under **Azure root path**, provide the path in your Azure Storage account to the write location that Dremio should use for Iceberg metadata and data. The root path includes the name of the Azure Storage container, followed by the names of any folders (for example, `/containername/optional/folder/path`).

#### Azure Authentication

Under **Authentication method**, choose whether you want to authenticate to Azure Storage with a shared access key or Microsoft Entra ID.

* **Shared access key**: Use the dropdown menu to choose a method for providing the shared access key for the Azure Storage account:
  + Dremio: Provide the access key in plain text. Dremio stores the password.
  + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored access key using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
  + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the access key, which is available in the AWS web console or using command line tools.
  + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the access key reference in the required format.
* **Microsoft Entra ID**:
  + In the field under **Application ID**, provide the ID for the application (client) in Azure.
  + Under **Client secret**, use the dropdown menu to choose a method for providing the client secret for the Azure Storage account:
    - Dremio: Provide the client secret in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored client secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the client secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the client secret reference in the required format.
  + In the field under **OAuth 2.0 token endpoint**, provide the OAuth 2.0 token endpoint (v1.0), including the tenant ID, that the application uses to get an access token or a refresh token.

#### Other: Connection Properties (Optional)

Provide the custom key-value pairs for the connection relevant to the source.

1. Click **Add Property**.
2. For **Name**, provide a connection property.
3. For **Value**, provide the corresponding value for the connection property.

#### Other: Encrypt connection

Optional: To secure the connections between Azure Storage and Dremio, select the **Encrypt connection** checkbox.

To save the configuration, click **Save**. To configure additional settings, proceed to [Advanced Options](/current/data-sources/lakehouse-catalogs/nessie/#advanced-options).

To connect Google Cloud Storage (GCS) to the Nessie source, select the **Google** storage provider option.

#### GCS Storage

* In the field under **Google Project ID**, provide the ID for your GCS project. You can find the ID in the **Project info** pane at the top-left of your screen on the GCS Home page.
* In the field under **Google root path**, provide the path for the GCS source that Dremio should use for Iceberg metadata and data.

#### GCS Authentication

Under **Authentication method**, choose whether you want to authenticate to GCS with a service account key or by automatic/service account.

* **Service Account Keys**:
  + In the field under **Client Email**, provide the email address associated with the GCS service account.
  + In the field under **Client ID**, provide the client ID for your GCS key pair.
  + In the field under **Private Key ID**, provide the key ID for your GCS key pair.
  + Under **Private Key**, use the dropdown menu to choose a method for providing the private key for your GCS key pair:
    - Dremio: Provide the private key in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored private key using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the private key, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the private key secret reference in the required format.
* **Automatic/Service Account**: If you are running Dremio on a Google Compute instance, Dremio uses the active service account for your instance and does not require any additional information to integrate with your data.

#### Other: Connection Properties (Optional)

Provide the custom key-value pairs for the connection relevant to the source.

1. Click **Add Property**.
2. For **Name**, provide a connection property.
3. For **Value**, provide the corresponding value for the connection property.

#### Other: Encrypt connection

Optional: To secure the connections between GCS and Dremio, select the **Encrypt connection** checkbox.

To save the configuration, click **Save**. To configure additional settings, proceed to [Advanced Options](/current/data-sources/lakehouse-catalogs/nessie/#advanced-options).

### Advanced Options

Click **Advanced Options** in the left menu sidebar.

Under Cache Options, review the following table and edit the options to meet your needs.

| Cache Options | Description |
| --- | --- |
| **Enable local caching when possible** | Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details. |
| **Max percent of total available cache space to use when possible** | Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter in a percentage in the value field or use the arrows to the far right to adjust the percentage. |

### Reflection Refresh

The **Reflection Refresh** section allows you to set a schedule for refreshing all of the Reflections that are defined on tables in the catalog. You can override this schedule on individual tables in different branches. This section also lets you specify how long all Reflections in the catalog exist until they expire. Again, you can override this setting on individual tables in different branches.

To learn more, see [Refreshing Reflections](/current/acceleration/manual-reflections/refreshing-reflections/) and [Setting the Expiration Policy for Reflections](/current/reflections/setting-expiration-policy/).

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

At this point, a connection with the Nessie server is attempted. If a connection cannot be made, report the issue to the Project Nessie community's [Zulip channel](https://project-nessie.zulipchat.com/login/). You can also file a ticket on the Project Nessie community's [GitHub page](https://github.com/projectnessie/nessie/issues).

## Retrieving a Table Definition

You can retrieve the table definition for Nessie tables if you have the `SELECT` privilege on the table. Because tables cannot be modified, you can't make edits to the table definition but you can retrieve the definition to understand where the table was derived from and to use it as a template for creating new views.

To see a table definition on the Datasets page, choose any one of these options:

* Hover over the table name and click ![](/images/icons/go-to-table.png) in the top right corner of the metadata card.
* Hover over the line containing the table and click ![](/images/icons/go-to-table.png) on the right.
* Hover over the line containing the dataset, click ![](/images/icons/more.png) on the right, and select **Go to Table**.

The table definition opens in the SQL editor.

If you want to use this table definition to create a view, see Creating a View.

tip

If you have the `SELECT` privilege on a Nessie table, you can run `SHOW CREATE TABLE <table_name>` in the SQL editor to see the table definition. See [SHOW CREATE TABLE](/current/reference/sql/commands/show-create-table).

## Updating a Nessie Source

To update a Nessie source:

1. On the Datasets page, under **Nessie Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Nessie as a Source.
4. Click **Save**.

## Deleting a Nessie Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Nessie source, perform these steps:

1. On the Datasets page, click **Sources** > **Nessie Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Limitations

* Changes to tables and views that are in Nessie sources are not logged. Nessie sources do not have audit logs.

  DX-64988
* The [Catalog API](/current/reference/api/catalog/) is unable to retrieve or manage Nessie sources.

  DX-64994
* Dremio does not support moving, copying, or renaming tables and views in Nessie sources or removing the format from tables in Nessie sources.

Was this page helpful?

[Previous

Hive](/current/data-sources/lakehouse-catalogs/hive)[Next

Object Storage](/current/data-sources/object/)

* Concepts
  + Architecture
  + Objects in Nessie
  + Git-like Data Management
* Prerequisites
* Configuring Nessie as a Source
  + General
  + Storage
  + Advanced Options
  + Reflection Refresh
  + Privileges
* Retrieving a Table Definition
* Updating a Nessie Source
* Deleting a Nessie Source
* Limitations

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/snowflake-open/

Version: current [26.x]

On this page

# Snowflake Open Catalog Enterprise

Dremio supports Snowflake Open Catalog as an Iceberg catalog source. With this source connector, you can connect and read from internal and external Snowflake Open Catalogs and write to External Snowflake Open Catalogs.

## Prerequisites

You will need the catalog **Service URI**, **Client ID**, and **Client Secret** from the Snowflake setup. For a walkthrough of the Snowflake setup, please refer to [Query a table in Snowflake Open Catalog using a third-party engine](https://other-docs.snowflake.com/opencatalog/query-table-using-third-party-engine).

## Configuring Snowflake Open Catalog as a Source

To add a Snowflake Open Catalog source:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Snowflake Open Catalog**.

   The New Snowflake Open Catalog dialog box appears, which contains the following tabs:

   * **General**: Create a name for your Snowflake Open Catalog source, specify the endpoint URI and Snowflake Open Catalog, and set the authentication.
   * **Advanced Options**: Use catalog properties and credentials to set up storage authentication and authorization.
   * **Reflection Refresh**: (Optional) Set a policy to control how often Reflections are refreshed and expired.
   * **Metadata**: (Optional) Specify dataset handling and metadata refresh.
   * **Privileges**: (Optional) Add privileges for users or roles.

   Refer to the following sections for guidance on how to edit each tab.

### General

To configure the source connection:

1. For **Name**, enter a name for the source.

   note

   The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore(\_), or hyphen (-)
2. Enter the name of the Snowflake Open Catalog.
3. For **Endpoint URI**, specify the catalog service URI.
4. In the Authentication section, use the **Client ID** and **Client Secret** created during the [configuration of a service connection](https://other-docs.snowflake.com/opencatalog/configure-service-connection) for the Snowflake Open Catalog.
5. By default, `Use vended credentials` is on. This allows Dremio to connect to the catalog and receive temporary credentials to the underlying storage location. If this is enabled, there is no need to add the storage authentication in Advanced Options.
6. (Optional) For **Allowed Namespaces**, add each namespace and check the option if you want to include their whole subtrees. Tables are organized into namespaces, which can be at the top level or nested within one another. Namespace names cannot contain periods or spaces.

### Advanced Options

To set the advanced options:

1. (Optional) For **Catalog Properties** and **Catalog Credentials**, you can manually provide the storage authentication if you choose to not use vended credentials.

   Dremio supports Amazon S3, Azure Storage, and Google Cloud Storage (GCS) as object storage services. For acceptable storage authentication configurations, see the following catalog properties and credentials for each service option.

   **Amazon S3 Access Key**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | property | `fs.s3a.aws.credentials.provider` | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` | Required value for a Snowflake Open Catalog source |
   | credential | `fs.s3a.access.key` | `<your_access_key>` | AWS access key ID used by S3A file system |
   | credential | `fs.s3a.secret.key` | `<your_secret_key>` | AWS secret key used by S3A file system |

   **Amazon S3 Assumed Role**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | property | `fs.s3a.assumed.role.arn` | `arn:aws:iam::*******:role/OrganizationAccountAccessRole` | AWS ARN for the role to be assumed |
   | property | `fs.s3a.aws.credentials.provider` | `com.dremio.plugins.s3.store.STSCredentialProviderV1` | Required value for a Snowflake Open Catalog source |
   | property | `fs.s3a.assumed.role.credentials.provider` | `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` | Use only if the credential provider is `AssumedRoleCredentialProvider`; lists credential providers to authenticate with the STS endpoint and retrieve short-lived role credentials |
   | credential | `fs.s3a.access.key` | `<your_access_key>` | AWS access key ID used by S3A file system |
   | credential | `fs.s3a.secret.key` | `<your_secret_key>` | AWS secret key used by S3A file system |

   **Azure Storage with Microsoft Entra ID**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | property | `fs.azure.account.auth.type` | OAuth |  |
   | property | `fs.azure.account.oauth2.client.id` | `<your_client_ID>` | Client ID from App Registration within Azure Portal |
   | property | `fs.azure.account.oauth2.client.endpoint` | `https://login.microsoftonline.com/<ENTRA ID>/oauth2/token` | Microsoft Entra ID from Azure Portal |
   | credential | `fs.azure.account.oauth2.client.secret` | `<your_client_secret>` | Client secret from App Registration within Azure Portal |

   **Azure Storage Shared Key**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | credential | `fs.azure.account.key` | `<your_account_key>` | Storage account key |

   **Google Cloud Storage (GCS) Using Default Credentials**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | property | `dremio.gcs.use_keyfile` | false | Required value for a Snowflake Open Catalog source |

   **Google Cloud Storage (GCS) Using KeyFile**

   | Type | Name | Value | Description |
   | --- | --- | --- | --- |
   | property | `dremio.gcs.clientId` | `<your_client_ID>` | Client ID from GCS |
   | property | `dremio.gcs.projectId` | `<your_project_ID>` | Project ID from GCS |
   | property | `dremio.gcs.clientEmail` | `<your_client_email>` | Client email from GCS |
   | property | `dremio.gcs.privateKeyId` | `<your_private_key_ID>` | Private key ID from GCS |
   | property | `dremio.gcs.use_keyfile` | true | Required value for a Snowflake Open Catalog source |
   | credential | `dremio.gcs.privateKey` | `<your_private_key>` | Private key from GCS |
2. Under **Cache Options**, review the following table and edit the options to meet your needs.

   | Cache Options | Description |
   | --- | --- |
   | **Enable local caching when possible** | Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details. |
   | **Max percent of total available cache space to use when possible** | Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter in a percentage in the value field or use the arrows to the far right to adjust the percentage. |

### Reflection Refresh

You can set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed. See the following options.

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
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

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

You have the option to grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Snowflake Open Catalog Source

To update a Snowflake Open Catalog source:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Snowflake Open Catalog as a Source.
4. Click **Save**.

## Deleting a Snowflake Open Catalog Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Snowflake Open Catalog source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Additional Resources

Learn more about Polaris by enrolling in the [Apache Polaris course in Dremio University](https://university.dremio.com/course/apache-polaris).

Was this page helpful?

[Previous

Microsoft OneLake](/current/data-sources/lakehouse-catalogs/onelake)[Next

Unity Catalog](/current/data-sources/lakehouse-catalogs/unity)

* Prerequisites
* Configuring Snowflake Open Catalog as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Snowflake Open Catalog Source
* Deleting a Snowflake Open Catalog Source
* Additional Resources

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/unity/

Version: current [26.x]

On this page

# Unity Catalog Enterprise

Unity Catalog provides a metastore for Delta tables within the Databricks ecosystem, and Dremio supports these Delta Lake Universal Format (UniForm) tables in Unity Catalog as a Dremio data source.

## UniForm Iceberg

UniForm is an Iceberg metadata layer that provides a read-only interoperability layer for Iceberg clients. To query Delta tables, you must use UniForm to read Delta tables with Iceberg clients. For guidance, see [Enable UniForm Iceberg](https://docs.databricks.com/en/delta/uniform.html#enable-uniform-iceberg) in the Databricks documentation. The minReaderVersion of UniForm required is 2, as noted in [Features by protocol version](https://docs.databricks.com/en/delta/feature-compatibility.html#features-by-protocol-version).

For the limitations of UniForm tables, see [Limitations](https://docs.databricks.com/en/delta/uniform.html#limitations) in the Databricks documentation.

## Configuring Unity Catalog as a Source

To add a Unity Catalog source:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "Add Source icon").
2. In the Add Data Source dialog, under **Lakehouse Catalogs**, select **Unity Catalog**.

### General

To configure the source connection:

* **Name**: Enter a name for the source. The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore(\_), or hyphen (-)
* **Endpoint URI**: Specify the catalog service URI. For more information on how to find your Unity Catalog URI, see [Read using the Unity Catalog Iceberg catalog endpoint](https://docs.databricks.com/en/delta/uniform.html#read-using-the-unity-catalog-iceberg-catalog-endpoint) for more details.
* **Unity Catalog**, enter the catalog name.

#### Authentication

Select an authentication option:

* **Databricks Personal Access Token (PAT)**: Depending on your deployment, choose from the following options to create a PAT:

  + AWS-based Unity deployment: See [Databricks personal access tokens for service principals](https://docs.databricks.com/en/dev-tools/auth/pat.html#databricks-personal-access-tokens-for-service-principals) to create a PAT.
  + Azure Databricks-based Unity deployment: See [Azure Databricks personal access tokens for service principals](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth/pat#azure-databricks-personal-access-tokens-for-service-principals) to create a PAT.

  Select a method to store the PAT:

  + Dremio: Provide the PAT in plain text. Dremio stores the PAT.
  + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored PAT using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
  + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the PAT, which is available in the AWS web console or using command line tools.
  + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the PAT reference in the required format.
* **Microsoft Entra ID**: To register a Microsoft Entra ID application and obtain the required IDs and client secret, see [How to register an app in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app), then complete the Dremio configuration:

  + **Application ID**: Enter the application (client) ID
  + **OAuth 2.0 Token Endpoint**: The OAuth 2.0 token endpoint that the application uses to get an access token
  + **Application Secret**:
    - Dremio: Provide the application secret in plain text. Dremio stores the application secret.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored application secret securely using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the application secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine using from the dropdown and enter the secret reference for the application secret in the required format.
  + By default, **Use vended credentials** is turned on. This allows Dremio to connect to the catalog and receive temporary credentials for the underlying storage location. When this option is enabled, you don't need to add the storage authentication in **Advanced Options**.

#### Allowed Namespaces

For **Allowed Namespaces**, optionally add each namespace and check the option if you want to include their whole subtrees. Tables are organized into namespaces, which can be at the top level or nested within one another. Namespace names cannot contain periods or spaces.

### Advanced Options

To set the advanced options:

* (Optional) For **Catalog Properties** and **Catalog Credentials**, you must manually provide the storage authentication if you choose to not use vended credentials.

  Dremio supports Amazon S3, Azure Storage, and Google Cloud Storage (GCS) as object storage services. For acceptable storage authentication configurations, see the following catalog properties and credentials for each service option.

  **Amazon S3 Access Key**

  | Type | **Name** Value | Description |
  | --- | --- | --- |
  | property | **`fs.s3a.aws.credentials.provider`** `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` | Required field for a Unity Catalog source |
  | credential | **`fs.s3a.access.key`** `<your_access_key>` | AWS access key ID used by S3A file system. Omit for IAM role-based or provider-based authentication |
  | credential | **`fs.s3a.secret.key`** `<your_secret_key>` | AWS access key used by S3A file system. Omit for IAM role-based or provider-based authentication |

  **Amazon S3 Assumed Role**

  | Type | **Name** Value | Description |
  | --- | --- | --- |
  | property | **`fs.s3a.assumed.role.arn`** `arn:aws:iam::*******:role/OrganizationAccountAccessRole` | AWS ARN for the role to be assumed |
  | property | **`fs.s3a.aws.credentials.provider`** `com.dremio.plugins.s3.store.STSCredentialProviderV1` | Required field for a Unity Catalog source |
  | property | **`fs.s3a.assumed.role.credentials.provider`** `org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider` | Use only if the credential provider is `AssumedRoleCredentialProvider`; lists credential providers to authenticate with the STS endpoint and retrieve short-lived role credentials |

  **Azure Storage Shared Key**

  | Type | **Name**  Value | Description |
  | --- | --- | --- |
  | credential | **`fs.azure.account.key`** `<your_account_key>` | Storage account key |

  **Google Cloud Storage (GCS) Using KeyFile**
  `

  | Type | **Name**  Value | Description |
  | --- | --- | --- |
  | property | **`fs.AbstractFileSystem.gs.impl`** `com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS` | Required field for a Unity Catalog source |
  | property | **`fs.gs.auth.service.account.enable`** `true` | Required field for a Unity Catalog source |
  | property | **`fs.gs.impl`** `com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem` | Required field for a Unity Catalog source |
  | property | **`fs.gs.bucket`** `<your_bucket>` | Bucket where your data is stored for Unity Catalog in GCS |
  | property | **`fs.gs.project.id`** `<your_project_ID>` | Project ID from GCS |
  | property | **`fs.gs.auth.service.account.email`** `<your_client_email>` | Client email from GCS |
  | property | **`fs.gs.auth.service.account.private.key.id`** `<your_private_key_id>` | Private key ID from GCS |
  | property | **`dremio.gcs.use_keyfile`** `true` | Required field for a Unity Catalog source |
  | credential | **`fs.gs.auth.service.account.private.key`** `<your_private_key>` | Private key from GCS |
* Under **Cache Options**, review the following table and edit the options to meet your needs.

  | Cache Options | Description |
  | --- | --- |
  | **Enable local caching when possible** | Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details. |
  | **Max percent of total available cache space to use when possible** | Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter in a percentage in the value field or use the arrows to the far right to adjust the percentage. |

### Reflection Refresh

You can set the policy that controls how often Reflections are scheduled to be refreshed automatically, as well as the time limit after which Reflections expire and are removed. See the following options.

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
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

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

You have the option to grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Unity Catalog Source

To update a Unity Catalog source:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name, and then click the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top-right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Unity Catalog as a Source.
4. Click **Save**.

## Deleting a Unity Catalog Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Unity Catalog source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

Was this page helpful?

[Previous

Snowflake Open Catalog](/current/data-sources/lakehouse-catalogs/snowflake-open)[Next

Iceberg REST Catalog](/current/data-sources/lakehouse-catalogs/iceberg-rest-catalog)

* UniForm Iceberg
* Configuring Unity Catalog as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Unity Catalog Source
* Deleting a Unity Catalog Source

---

# Source: https://docs.dremio.com/current/data-sources/lakehouse-catalogs/onelake

Version: current [26.x]

On this page

# Microsoft OneLake Enterprise

[Microsoft OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview) is a single, unified, logical data lake that comes automatically with every Microsoft Fabric tenant. It is built on top of Azure Data Lake Storage (ADLS) Gen2. All Fabric data items, such as data warehouses and lakehouses, store their data automatically in OneLake.

Dremio creates connections to Microsoft OneLake using its Iceberg REST Catalog connector.

## Configure a Microsoft OneLake Source

To add a Microsoft OneLake source connection:

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "Add Source icon").
2. In the Add Source dialog, under **Lakehouse Catalogs**, select **Iceberg REST Catalog Source**.

### General

To configure the source connection:

1. For **Name**, enter a name for the source. The name you enter must be unique in the organization. Also, consider a name that is easy for users to reference. This name cannot be edited once the source is created. The name cannot exceed 255 characters and must contain only the following characters: 0-9, A-Z, a-z, underscore (\_), or hyphen (-).
2. For **Endpoint URI**, specify the catalog service URI as `https://onelake.table.fabric.microsoft.com/iceberg`.
3. Clear **Use vended credentials**.
4. (Optional) For **Allowed Namespaces**, add each namespace and check the option if you want to include their entire subtrees. Tables are organized into namespaces, which can be at the top level or nested within one another. Namespace names cannot contain periods or spaces.

### Advanced Options

Replace the placeholders inside `<...>` with your respective values. For example, a warehouse value could be `icy/icelake.Lakehouse`. The `fs.*` properties are used to establish connections to the storage underlying your catalog in OneLake.

1. Add the following **Catalog Properties** with their associated values.

   * `rest.auth.type`: `oauth2`
   * `oauth2-server-uri`: `https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/token`
   * `scope`: `https://storage.azure.com/.default`
   * `warehouse`: `<catalog>`
   * `fs.azure.endpoint`: `dfs.fabric.microsoft.com`
   * `fs.azure.account.auth.type`: `OAuth`
   * `fs.azure.account.oauth2.client.endpoint`: `https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/token`
   * `fs.azure.account.oauth2.client.id`: `<oauth_client_id>`
2. Add the following **Catalog Credentials** with their associated values:

   * `fs.azure.account.oauth2.client.secret`: `<oauth_client_secret>`
   * `credential`: `<oauth_client_id:oauth_client_secret>`
3. Under **Cache Options**, review the following table and edit the options to meet your needs.

   * **Enable local caching when possible** – Selected by default. Along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details.
   * **Max percent of total available cache space to use when possible** – Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter a percentage in the value field or use the arrows to the far right to adjust the percentage.

### Reflection Refresh

You can set the policy that controls how often reflections are scheduled to be refreshed automatically, as well as the time limit after which reflections expire and are removed. See the following options:

| Option | Description |
| --- | --- |
| **Never refresh** | Select to prevent automatic reflection refresh. The default is to automatically refresh. |
| **Refresh every** | How often to refresh reflections, specified in hours, days, or weeks. This option is ignored if **Never refresh** is selected. |
| **Set refresh schedule** | Specify the daily or weekly schedule. |
| **Never expire** | Select to prevent reflections from expiring. The default is to automatically expire after the time limit below. |
| **Expire after** | The time limit after which reflections expire and are removed from Dremio, specified in hours, days, or weeks. This option is ignored if **Never expire** is selected. |

### Metadata

Metadata options are configured using the following settings.

#### Dataset Handling

* **Remove dataset definitions if underlying data is unavailable** (default).
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

#### Metadata Refresh

These are the optional **Metadata Refresh** parameters:

* **Dataset Discovery**: The refresh interval for fetching top-level source object names such as databases and tables. Set the time interval using this parameter.

  | Parameter | Description |
  | --- | --- |
  | **Fetch every** | You can set the frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour. |
* **Dataset Details**: The metadata that Dremio needs for query planning, such as information needed for fields, types, shards, statistics, and locality. These are the parameters to fetch the dataset information.

  | Parameter | Description |
  | --- | --- |
  | **Fetch mode** | You can fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**. |
  | **Fetch every** | You can set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour. |
  | **Expire after** | You can set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours. |

### Privileges

You have the option to grant privileges to specific users or roles. See [Access Control](/current/security/rbac/) for additional information about privileges.

To grant access to a user or role:

1. For **Privileges**, enter the user name or role name to which you want to grant access and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Update a Microsoft OneLake Source

To update a Microsoft OneLake source connection:

1. On the Datasets page, under **Lakehouse Catalogs** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the Source Settings dialog, edit the settings you want to update. Dremio does not support updating the source name.
4. Click **Save**.

## Delete a Microsoft OneLake Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Microsoft OneLake source:

1. On the Datasets page, click **Sources** > **Lakehouse Catalogs** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

Deleting a source causes all downstream views that depend on objects in the source to break.

Was this page helpful?

[Previous

AWS Glue Data Catalog](/current/data-sources/lakehouse-catalogs/aws-glue-catalog)[Next

Snowflake Open Catalog](/current/data-sources/lakehouse-catalogs/snowflake-open)

* Configure a Microsoft OneLake Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Update a Microsoft OneLake Source
* Delete a Microsoft OneLake Source

---

# Source: https://docs.dremio.com/current/data-sources/object/s3/

Version: current [26.x]

On this page

# Amazon S3

This topic provides information for configuring the Amazon S3 data source.

## Working with files stored in S3

You can query files and folders stored in your S3 buckets.
Dremio supports a number of different file formats.
See [Formatting Data to a Table](/current/developer/data-formats/table) for more information.

note

Amazon S3 data sources added to projects default to using the Apache Parquet table format. Follow these steps to ensure that the default table format for new tables is Apache Iceberg:

1. In Dremio, click the Amazon S3 data source.
2. Click the gear icon in the top-right corner above the list of the data source's contents.
3. On the Advanced Options page of the Edit Source dialog, select **ICEBERG** under **Default CTAS Format**.
4. Click **Save**.

Amazon S3 data sources added to projects before Dremio 22 continue to use the Parquet table format for tables. For the SQL commands that you can use to create and query tables in such data sources, see [Tables](/current/reference/sql/commands/tables/).

## Amazon Configuration

Amazon configuration involves:

* Providing AWS credentials
* Providing IAM Policy requirements

### Amazon S3 Credentials

To list your AWS account's S3 buckets as a source, you must provide your AWS credentials in the
form of your access and secret keys. You can find instructions for creating these keys in
[Amazon's Access Key documentation](http://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html).

AWS credentials are not necessary if you are accessing only public S3 buckets.

### Sample IAM Policy for Accessing S3

The following sample IAM Policy shows the minimum policy requirements that allow Dremio to read and query S3.

Sample IAM policy for accessing Amazon S3

```
{  
    "Version": "2012-10-17",  
    "Statement": [  
        {  
            "Sid": "Stmt1554422960000",  
            "Effect": "Allow",  
            "Action": [  
                "s3:GetBucketLocation",  
                "s3:ListAllMyBuckets"  
            ],  
            "Resource": [  
                "arn:aws:s3:::*"  
            ]  
        },  
        {  
            "Sid": "Stmt1554423012000",  
            "Effect": "Allow",  
            "Action": [  
                "s3:ListBucket"  
            ],  
            "Resource": [  
                "arn:aws:s3:::BUCKET-NAME"  
            ]  
        },  
        {  
            "Sid": "Stmt1554423050000",  
            "Effect": "Allow",  
            "Action": [  
                "s3:GetObject"  
            ],  
            "Resource": [  
                "arn:aws:s3:::BUCKET-NAME/*"  
            ]  
        }  
    ]  
}
```

### Sample IAM Policy for Writing to S3

The following sample IAM Policy shows the minimum policy requirements that allows Dremio to write to S3.  
For example, to store Reflections on S3.

Sample IAM policy for writing to Amazon S3

```
{  
    "Version": "2012-10-17",  
    "Statement": [  
        {  
            "Effect": "Allow",  
            "Action": [  
                "s3:PutObject",  
                "s3:GetObject",  
                "s3:ListBucket",  
                "s3:DeleteObject"  
            ],  
            "Resource": [  
                "arn:aws:s3:::BUCKET-NAME",  
                "arn:aws:s3:::BUCKET-NAME/*"  
            ]  
        },  
        {  
            "Effect": "Allow",  
            "Action": [  
                "s3:ListAllMyBuckets",  
                "s3:GetBucketLocation"  
            ],  
            "Resource": "*"  
        }  
    ]  
}
```

## Configuring Amazon S3 as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Object Storage**, select **Amazon S3**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Authentication

Choose one of the following authentication methods:

* AWS Access Key: All or allowed (if specified) buckets associated with this access key or IAM role to assume, if provided, will be available. See Advanced Options for whitelisted information.
  + Under **AWS Access Key**, enter the [AWS access key ID](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).
  + Under **AWS Access Secret**, provide the [AWS access secret](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) using one of the following methods:
    - Dremio: Provide the access secret in plain text. Dremio stores the access secret.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored access set using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the access secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the access secret reference in the required format.
  + Under **IAM Role to Assume**, enter the [IAM role](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html) that Dremio should assume in conjunction with the AWS Access Key authentication method.
* EC2 Metadata: All or whitelisted (if specified) buckets associated with the IAM role attached to EC2 or IAM role to assume (if specified) will be available. See Advanced Options for whitelisted information.
  + Under **IAM Role to Assume**, enter the [IAM role](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html) that Dremio should assume in conjunction with the EC2 Metadata authentication method.
* EKS Pod Identity: Dremio can access all S3 buckets linked to the IAM role associated with the Kubernetes service account or the assumed IAM role. If you specify certain buckets, only those will be available.
  + Under **IAM Role to Assume**, enter the [IAM role](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html) that Dremio should assume when using the Pod Identity authentication method.
* AWS Profile: Dremio sources profile credentials from the specified AWS profile. For information on how to set up a configuration or credentials file for AWS, see AWS Custom Authentication.
  + Profile Name (Optional): The AWS profile name. If this is left blank, then the default profile will be used. For more information about using profiles in a credentials or configuration file, see AWS's documentation on [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
* No Authentication: Only the buckets provided under **Public Buckets** will be available.

The **Encrypt connection** option is enabled by default to encrypt the connection to S3. Clear the checkbox to disable encryption.

#### AWS Custom Authentication

[AWS Glue](/current/data-sources/metastores/aws-glue-catalog/), [S3](/current/data-sources/object/s3/), and [Amazon OpenSearch](/current/data-sources/databases/opensearch/) sources allow Dremio to use your AWS profile to authenticate users accessing your AWS-hosted data.

This authentication is performed by selecting the **AWS Profile** option for a source. Dremio will use credentials from the selected profile in the credentials file to authenticate with the source. Multiple methods are available for authentication, such as an external process. However, such processes must be created and validated for security by the users themselves.

note

We recommend using supported and secure methods via the AWS SDK and AWS application to minimize the potential for security risks.

Users with methods of generating or retrieving credentials that may not be supported by the AWS SDK can still use the tool by using additional configurations to alter the SDK, such as using the `credential_process` setting in the `credentials` file. Again, additional options are available for authenticating users via AWS. For more details regarding the storage of configuration settings and credentials maintained by AWS SDK, read AWS's [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) documentation. This topic discusses both the supported settings available for inclusion in the configuration and credential files, as well as details regarding the storage of credentials.

Further information regarding this setting is found at AWS's documentation for [Sourcing credentials with an external process](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html). This help topic outlines not only how to execute your command, but also how to structure the expected JSON-formatted output from a Credentials program, which Dremio requires.

#### Public Buckets

Add any external buckets that are not included with the provided AWS account credentials.

### Advanced Options

Click **Advanced Options** in the left menu sidebar. All advanced options are optional.

Review each option provided in the following table to set up the advanced options to meet your needs.

| Advanced Option | Description |
| --- | --- |
| **Enable compatibility mode** | Enables the use of S3-compatible storage such as MinIO. |
| **Apply requester-pays to S3 requests** | The requester (instead of the bucket owner) pays the cost of the S3 request and the data downloaded from the S3 bucket. |
| **Enable file status check** | Activated by default, uncheck the box to deactivate. Enables Dremio to check if a file exists in the S3 bucket before proceeding to handle errors gracefully. Disable this option when there are no files missing from the S3 bucket or when the file’s access permissions have not changed. Disabling this option reduces the amount of communication to the S3 bucket. |
| **Enable partition column inference** | Enable this option to change how Dremio handles partition columns (see [Partition Column Inference](/current/developer/data-formats/table#partition-column-inference) for more information.) |
| **Root Path** | The root path for the Amazon S3 bucket. The default root path is /. |
| **Server side encryption key ARN** | Add the ARN key created in [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS) if you want to store passwords in AWS KMS. Ensure that the AWS credentials that you share with Dremio have access to this ARN key. |
| **Default CTAS Format** | Choose the default format for tables you create in Dremio, either Parquet or Iceberg. |
| **Connection Properties** | Provide the custom key value pairs for the connection relevant to the source.  1. Click **Add Property**. 2. For Name, enter a connection property. 3. For Value, enter the corresponding connection property value. |
| **Allowlisted buckets** | Add an approved S3 bucket in the text field. You can add multiple S3 buckets this way. When using this option to add specific S3 buckets, you will only be able to see those buckets and not all the buckets that may be available in the source. Buckets entered must be valid. Misspelled or non-existent buckets will not appear in the resulting source. |

To configure your S3 source to use server-side encryption based on a provided key (SSE-C) or KMS (SSE-KMS), set the following connection properties:

* SSE-C
  + `fs.s3a.server-side-encryption-algorithm` set to `SSE-C`
  + `fs.s3a.server-side-encryption.key` set to the key used on the objects in S3
* SSE-KMS
  + `fs.s3a.server-side-encryption-algorithm` set to `SSE-KMS`
  + `fs.s3a.server-side-encryption.key` set to the ARN used on the objects in S3

#### Cache Options

Under Cache Options, review the following table and edit the options to meet your needs.

| Cache Options | Description |
| --- | --- |
| **Enable local caching when possible** | Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details. |
| **Max percent of total available cache space to use when possible** | Specifies the disk quota, as a percentage, that a source can use on any single executor node only when local caching is enabled. The default is 100 percent of the total disk space available on the mount point provided for caching. You can either manually enter in a percentage in the value field or use the arrows to the far right to adjust the percentage. |

#### Locations in which Iceberg Tables are Created

Where the CREATE TABLE command creates a table depends on the type of data source being used. For Amazon S3 sources, the root physical location is the main root directory for the filesystem. From this location, the path and table name are appended to determine the physical location for a new table.

caution

If your S3 datasets include large Parquet files with 100 or more columns, then you must edit the number of maximum connections to S3 that each processing unit of Dremio is allowed to spawn. To change the maximum connections:

1. Under Connection Properties, click **Add Property**.
2. For Name, enter `fs.s3a.connection.maximum`.
3. For Value, enter a custom value greater than the default 100.

![Advanced Options](/assets/images/s3-adv-options-c0deb8a7e0e0819b2f8a381d2a2e3409.png) !

#### Connecting through a proxy server

Optionally, you can configure your S3 source to connect through a proxy.
You can achieve this by adding the following `Properties` in the settings for your S3 source:

| Property Name | Description |
| --- | --- |
| fs.s3a.proxy.host | Proxy host. |
| fs.s3a.proxy.port | Proxy port number. |
| fs.s3a.proxy.username | Username for authenticated connections, optional. |
| fs.s3a.proxy.password | Password for authenticated connections, optional. |

#### Connecting to a bucket in AWS GovCloud

To connect to a bucket in AWS GovCloud, set the correct GovCloud endpoint for your S3 source.
You can achieve this by adding the following `Properties` in the settings:

| Property Name | Description |
| --- | --- |
| fs.s3a.endpoint | The GovCloud endpoint (e.g., `s3-us-gov-west-1.amazonaws.com`). |

#### Connecting to a bucket via AWS PrivateLink

To connect to a bucket using an AWS PrivateLink URL, set the correct server endpoint for your S3 source.
You can achieve this by adding the following `Properties` in the settings:

| Property Name | Description |
| --- | --- |
| fs.s3a.endpoint.region | VPC region name (e.g., `us-east-1`). |
| fs.s3a.endpoint | PrivateLink DNS name (e.g., `bucket.vpce-xxx-xx.s3.us-east-1.vpce.amazonaws.com`). |

note

The `fs.s3a.endpoint.region` setting ensures that the PrivateLink is created in the desired region, and it allows access only to buckets in the specified region.  
  
The `fs.s3a.endpoint` value cannot contain the `http(s)://` prefix.

### Reflection Refresh

![](/assets/images/hdfs-refresh-policy-9ae71114907887b859a9d01425390739.png) !

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

![](/assets/images/s3-metadata-eed8286e9d457256b62c1a95f6653cde.png) !

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).  
  If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.
* Automatically format files into tables when users issue queries.
  If this box is checked and a query runs against the un-promoted table/folder,
  Dremio automatically promotes using default options.
  If you have CSV files, especially with non-default options, it might be useful to *not* check this box.

#### Metadata Refresh

* **Dataset Discovery** -- Refresh interval for top-level source object names such as names of DBs and tables.

  note

  Dataset Discovery is available for [Google Cloud Storage (GCS)](/current/data-sources/object/gcs#metadata) and databases. For Amazon S3, Dremio lists folders and files in real time unless they have been converted to tables.

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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an Amazon S3 Source

To update an Amazon S3 source:

1. On the Datasets page, under **Object Storage** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Amazon S3 as a Source.
4. Click **Save**.

## Deleting an Amazon S3 Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Amazon S3 source, perform these steps:

1. On the Datasets page, click **Sources** > **Object Storage** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Configuring S3-Compatible Storage

You can use S3-compatible storage, such as MinIO or IBM Cloud Object Storage, as a Dremio data source as long as the storage is completely S3-compatible. We recommend confirming S3 compatibility with the storage provider before you start the configuration steps.

To configure S3-compatible storage as a data source in the Dremio console:

1. Under **Advanced Options**, check **Enable compatibility mode**.
2. Under **Advanced Options > Connection Properties**, add `fs.s3a.path.style.access` and set the value to `true`.  
   Note: This setting ensure that the request path is created correctly when using IP addresses or hostnames as the endpoint.
3. Under **Advanced Options > Connection Properties**, add the `fs.s3a.endpoint` property and its
   corresponding server endpoint value (IP address).  
   Limitation: The endpoint value cannot contain the `http(s)://` prefix nor can it start with the string `s3`.
   For example, if the endpoint is `http://123.1.2.3:9000`, the value is `123.1.2.3:9000`.
4. For IBM Cloud Object Storage and other S3-compatible storage where required, you must add the following property to the `core-site.xml` file to whitelist the bucket:

   Whitelist the S3-compatible bucket

   ```
   <property>  
       <name>dremio.s3.whitelisted.buckets</name>  
       <value>your-S3-compatible-bucket-name</value>  
   </property>
   ```

As an example for a specific S3-compatible storage product, the following steps describe how to configure your S3 source for MinIO with an encrypted connection in the Dremio console:

1. Use OpenSSL to generate a self signed certificate.
   See [Securing Access to Minio Servers](https://docs.min.io/docs/how-to-secure-access-to-minio-server-with-tls) or use an existing self signed certificate.
2. Start up Minio server with `./minio server [data folder] --certs-dir [certs directory]`.
3. Install Dremio.
4. In your client environment where Dremio is located, install the certificate into **<JAVA\_HOME>/jre/lib/security** with the following command:

   Install certificate

   ```
   <JAVA_HOME>/keytool -import -v -trustcacerts -alias alias -file cert-file -keystore cacerts -keypass changeit -storepass changeit
   ```

   note

   Replace `alias` with the alias name you want and replace `cert-file` with the absolute path of the certificate file used to startup Minio server.
5. Start up Dremio.
6. In the Dremio console, add and configure an Amazon S3 data source with the Minio plug-in.

   1. Under the **General** tab, specify the **AWS Access Key** and **AWS Access Secret** provided by your Minio server.
   2. Under the **General** tab, check **Encrypt Connection**.
   3. Under **Advanced Options**, check **Enable compatibility mode**.
   4. Under **Advanced Options > Connection Properties**, add `fs.s3a.path.style.access` and set the value to `true`.  
      Note: This setting ensure that the request path is created correctly when using IP addresses or hostnames as the endpoint.
   5. Under **Advanced Options > Connection Properties**, add the `fs.s3a.endpoint` property and its
      corresponding server endpoint value (IP address).  
      Limitation: The endpoint value cannot contain the `http(s)://` prefix nor can it start with the string `s3`.
      For example, if the endpoint is `http://123.1.2.3:9000`, the value is `123.1.2.3:9000`.

## Distributed Storage

Dremio requires object storage to be configured as [distributed storage](/current/what-is-dremio/architecture/#distributed-storage). See the configuration of distributed storage for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#configuring-the-distributed-storage) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/dist-store-config/#amazon-s3) for more information.

## Configuring Minio as a Distributed Store

Minio can be be used as a distributed store. Note that Minio works as a distributed store for both SSL and unencrypted connections. See the configuration of S3-compatible distributed storage for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#configuring-the-distributed-storage) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/dist-store-config/#configuring-dremio-for-minio) for more information.

## Configuring Cloud Cache

See [Configuring Cloud Cache](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/cloud-cache-config/) for more information.

## Configuring KMS Encryption for Distributed Store

AWS Key Managment Service (KMS) is available for S3 distributed store.
See the configuration of distributed storage for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#configuring-the-distributed-storage) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/dist-store-config/#amazon-s3) for more information.

## For More Information

See the following Minio documentation for more information:

* [Setting Up Minio](https://docs.min.io/docs/how-to-secure-access-to-minio-server-with-tls.html)
* [Loading Certificates in Minio](https://github.com/minio/minio/issues/5232#issuecomment-347413072)
* [Securing Access to Minio Servers](https://docs.min.io/docs/how-to-secure-access-to-minio-server-with-tls)

Was this page helpful?

[Previous

Object Storage](/current/data-sources/object/)[Next

Azure Storage](/current/data-sources/object/azure-storage)

* Working with files stored in S3
* Amazon Configuration
  + Amazon S3 Credentials
  + Sample IAM Policy for Accessing S3
  + Sample IAM Policy for Writing to S3
* Configuring Amazon S3 as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an Amazon S3 Source
* Deleting an Amazon S3 Source
* Configuring S3-Compatible Storage
* Distributed Storage
* Configuring Minio as a Distributed Store
* Configuring Cloud Cache
* Configuring KMS Encryption for Distributed Store
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/object/azure-storage/

Version: current [26.x]

On this page

# Azure Storage

The Dremio Azure Storage Connector includes support for the following Azure Storage services:

**Azure Blob Storage**

Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data, such as text or binary data.

**Azure Data Lake Storage Gen2**

Azure Data Lake Storage Gen2 is a set of capabilities dedicated to big data analytics, built on top of Azure Blob storage. Features, such as file system semantics, directory, and file-level security and scale, are combined with the low-cost, tiered storage, and high availability/disaster recovery capabilities of Azure Blob storage.

note

Soft delete for blobs is not supported for Azure Storage accounts. Soft delete should be disabled to establish a successful connection.

## Configuring Azure Storage as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Object Storage**, select **Azure Storage**.

### General

Under **Name**, enter the name to use for the Azure Storage source. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

* **Account Name**: Name of the Azure Storage account.
* **Encrypt connection**: Select to encrypt network traffic over SSL.
* **Storage Connection Protocol (Driver)**: Select the Azure Storage driver connection protocol you would like to use. The options are WASBS (Legacy) and ABFSS (Recommended). ABFSS is the default based on Azure best practices.

#### Authentication

Azure Storage authentication options include the following:

* **Shared access key**: Select the secret store method from the dropdown menu:
  + Dremio: Provide the shared access key in plain text. Dremio stores the key.
  + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
  + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the Azure Storage shared access key, which is available in the AWS web console or using command line tools.
  + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the shared access key secret reference in the required format.
* **Microsoft Entra ID**:
  + **Application ID**: Specify the Application (Client) ID in Microsoft Entra ID.
  + **OAuth 2.0 Token Endpoint**: Specify the OAuth 2.0 token endpoint for your Azure application.
  + **Application Secret Store**: Select the secret store for the Application Secret from the dropdown menu:
    - Dremio: Provide the Application Secret in plain text. Dremio stores the key.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the Application Secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the application secret reference in the required format.

### Advanced Options

* **Enable partition column inference**: Select if Dremio should use [partition column inference](/current/developer/data-formats/table#partition-column-inference) to handle partition columns.
* **Root Path**: Root path for the source. The default is `/`.
* **Advanced Properties**: Add connection properties, specifying their names and values.
* **Blob Containers & Filesystem Allowlist** Add the names of containers to include in the source. This setting disables automatic container and filesystem discovery. Dremio limits the available containers and filesystems to those you add to the allowlist.

#### Cache Options

* **Enable local caching when possible**: Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details.
* **Max percent of total available cache space to use when possible**: Maximum amount of cache space, as a percentage, that a source can use on any single executor node when local caching is enabled The default value is `100`.

### Reflection Refresh

The Reflection refresh options control how often Dremio refreshes Reflections automatically and the time limit after which Reflections expire and are removed.

#### Refresh Policy

* **Never refresh**: Select to prevent the automatic refresh of Reflections. The default is to allow automatic refreshes.
* **Refresh every**: If using automatic refresh, how often to refresh Reflections, specified in minutes, hours, days, or weeks. The default is 1 hour. Ignored if you select *Never refresh*.
* **Never expire**: Select to prevent the expiration of Reflections. The default is expiration after the specified time limit.
* **Expire after**: Time limit after which Reflections expire and are removed from Dremio, specified in minutes, hours, days, or weeks. The default is 3 hours. Ignored if you select *Never expire*.

### Metadata

Metadata settings include options for dataset handling and metadata refresh.

#### Dataset Handling

* **Remove dataset definitions if underlying data is unavailable**: Select to automatically remove datasets if their underlying files and folders are removed from Azure Storage or if the folder or source is not accessible. This option is selected by default. If *not* selected, Dremio does not remove dataset definitions even if their underlying files and folders are removed from Azure Storage, which is useful when files are temporarily deleted and replaced with a new set of files.
* **Automatically format files into tables when users issue queries**: Select to automatically promote folders to tables using the default options when a user runs a query on the folder data for the first time. This option is not selected by default. For Azure Storage sources that contain CSV files, especially CSV files with non-default formatting, consider leaving this option unselected.

#### Metadata Refresh

Metadata Refresh settings allow you to configure the refresh interval for gathering detailed information about promoted tables, including fields, data types, shards, statistics, and locality. Dremio uses this information during query planning and optimization.

* **Fetch mode**: The default is **Only Queried Datasets**, which only updates details only for previously queried objects in a source. This option increases query performance because the datasets require less work at query time. Other options are deprecated.
* **Fetch every**: How often to refresh dataset details, specified in minutes, hours, days, or weeks. The default is 1 hour.
* **Expire after**: Time limit after which dataset details expire, specified in minutes, hours, days, or weeks. The default is 3 hours.

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an Azure Storage Source

To update an Azure Storage source:

1. On the Datasets page, under **Object Storage** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Azure Storage as a Source.
4. Click **Save**.

## Deleting an Azure Storage Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Azure Storage source, perform these steps:

1. On the Datasets page, click **Sources** > **Object Storage** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Distributed Storage

Dremio requires object storage to be configured as [distributed storage](/current/what-is-dremio/architecture/#distributed-storage). See the configuration of distributed storage for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#configuring-the-distributed-storage) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/dist-store-config/#azure-storage) for more information.

## Azure Government

To configure Azure Storage for the Azure Government platform, add one of the following properties to the **Advanced Options** tab under **Advanced Properties**:

* **Storage V1**: Add the following property and value if the Azure Storage source is of Account Kind Storage V1

  Property and value for Storage V1

  ```
  fs.azure.endpoint = blob.core.usgovcloudapi.net
  ```
* **Storage V2**: Add the following property and value if the Azure Storage source is of Account Kind Storage V2

  Property and value for Storage V2

  ```
  fs.azure.endpoint = dfs.core.usgovcloudapi.net
  ```

## Troubleshooting

If you see 0 byte files being created with your Iceberg tables in your Azure Storage account, these files do not impact Dremio’s functionality and can be ignored if you cannot update your storage container. If you can update your container, see [Azure Data Lake Storage Gen2 hierarchical namespace](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-namespace) for more information on how to enable **Hierarchical Namespace** to prevent the creation of these files.

## For More Information

* [A closer look at Azure Data Lake Storage Gen2](https://azure.microsoft.com/en-us/blog/a-closer-look-at-azure-data-lake-storage-gen2/)
* [Azure Data Lake Storage Gen2 Introduction](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction)
* [Azure Government cloud platform](https://azure.microsoft.com/en-us/global-infrastructure/government/)

Was this page helpful?

[Previous

Amazon S3](/current/data-sources/object/s3)[Next

Google Cloud Storage (GCS)](/current/data-sources/object/gcs)

* Configuring Azure Storage as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an Azure Storage Source
* Deleting an Azure Storage Source
* Distributed Storage
* Azure Government
* Troubleshooting
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/object/gcs/

Version: current [26.x]

On this page

# Google Cloud Storage (GCS)

Dremio allows for integration with environments using the Google Cloud Storage (GCS) web service for storing data. Configuration of this source allows for direct access to GCS data through the Dremio interface.

## Configuring GCS as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Object Storage**, select **Google Cloud Storage**.

### General

The following options are available from the *General* tab:

**Name**: Provide a name to identify the GCS data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

**Google Project Id**: The specific ID for your GCS project. This can be found in the **Project info** pane at the top-left of your screen when at the Home page.

**Authentication**

Choose the authentication method:

* Service Account Keys
  + Client Email: Provide the email address associated with the GCS service account.
  + Client ID: Provide the client ID for your key pair. The value is found by following the steps to create a service account key.
  + Private Key ID: Provide the key ID for your key pair. The value is found by following the steps to create a service account key.
  + Private Key: Choose a method for providing the private key for your key pair. The value is found by following the steps to create a service account key.
    - Dremio: Provide the private key in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored private key using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the private key, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the private key secret reference in the required format.
* Automatic/Service Account: If you are currently running Dremio on a Google Compute instance, Dremio uses the active service account for your GCS data source and does not require any additional information to integrate with your data.

#### Creating Service Account Keys

In order to use Dremio to access your Google Cloud Storage source, you need to first identify the service account. This is done by creating public/private key pairs. When creating service account keys, the public portion is stored on Google Cloud, while the private portion is made available to you for entry on Dremio.

The steps below outline the most simple method of creating a service account key.

1. From the Google Cloud Console, navigate to the Service Accounts page.
2. Select the desired project.
3. Click on the email address of the service account that you'll be creating a key for.
4. Click on the *Keys* tab.
5. Click the **Add Key** drop-down menu and then select **Create new key**.
6. Select **JSON** as the **Key Type** and then click **Create**.

Your browser then downloads a service account key file. It should look similar to the example below:

Example service account key file

```
{  
  "type": "service_account",  
  "project_id": "project-id",  
  "private_key_id": "key-id",  
  "private_key": "-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n",  
  "client_email": "service-account-email",  
  "client_id": "client-id",  
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",  
  "token_uri": "https://accounts.google.com/o/oauth2/token",  
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",  
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-account-email"  
}
```

Copy and paste each value from this file to the corresponding fields on the Dremio interface.

For additional methods of creating a key (e.g., `gcloud` tool, REST APIs, etc.), [view Google's documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys).

### Advanced Options

The following settings control more advanced functionalities in Dremio.

| Field | Description |
| --- | --- |
| Root Path | The root path for the GCS source. |
| Properties | Additional connection properties, consisting of the property and its specified value. |
| Whitelisted buckets | A list of buckets to whitelist, or allow access to. |
| Cache Options |  |
| Enable local caching when possible | Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details. |
| Max percent of total available cache space to use when possible | Sets the allowable amount of local caching, based on percentage. Only the percent specified of the cached files will be stored locally. By default, this is set to 100. |

### Reflection Refresh

This tab controls the frequency of Reflection refreshes or the timespan for expiration for any queries performed using this data source.

| Field | Description |
| --- | --- |
| Never refresh | Prevents any query Reflections associated with this source from refreshing. |
| Refresh every | Sets the time interval by which Reflections for this source are refreshed. This may be set to hours, days, and weeks. |
| Never expire | Prevents any query Reflections associated with this source from expiring. |
| Expire after | Sets the time after a Reflection is created that it then expires and can no longer be used for queries. This may be set to hours, days, and weeks. |

### Metadata

This tab offers settings that control how dataset details are fetched and refreshed.

| Field | Description |
| --- | --- |
| Dataset Handling |  |
| Remove dataset definitions if underlying data is unavailable | If this box is not checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files. |
| Automatically format files into tables when users issue queries | If this box is checked and a query runs against the un-promoted table/folder, Dremio automatically promotes using default options. If you have CSV files, especially with non-default options, it might be useful to not check this box. |
| Metadata Refresh |  |
| Dataset Discovery | Specifies the refresh interval for top-level source object names, such as database and table names. This is a lightweight operation. Fetch every. Specifies the time interval by which Dremio fetches object names. This can be set by minutes, hours, days, and weeks. |
| Dataset Details | Specifies the metadata that Dremio needs for query planning, such as information regarding fields, types, shards, statistics, and locality.  Fetch mode. Restricts when metadata is retrieved. Only Queried Datasets. Dremio updates metadata details for previously-queried objects in a source. This mode increases query performance as it requires less work to be done at query time for these datasets. All Datasets (deprecated). Dremio updates the details for all datasets in a source. This mode increases query performance as less work is needed to be done at the time of query. Fetch every. Specifies the time interval by which metadata is fetched. This can be set by minutes, hours, days, and weeks. Expire after. Specifies the timespan for when dataset details expire after a dataset is queried. This can be set by minutes, hours, days, and weeks. |

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a GCS Source

To update a GCS source:

1. On the Datasets page, under **Object Storage** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring GCS as a Source.
4. Click **Save**.

## Deleting a GCS Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a GCS source, perform these steps:

1. On the Datasets page, click **Sources** > **Object Storage** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

Was this page helpful?

[Previous

Azure Storage](/current/data-sources/object/azure-storage)[Next

HDFS](/current/data-sources/object/hdfs)

* Configuring GCS as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a GCS Source
* Deleting a GCS Source

---

# Source: https://docs.dremio.com/current/data-sources/object/hdfs/

Version: current [26.x]

On this page

# HDFS

This topic describes HDFS data source considerations and Dremio configuration.

## HBase

HBase is an open-source, non-relational database that is built on top of HDFS and enables real-time analysis of data.

note

Although HBase is no longer officially supported by Dremio as a source connection, you can still add HBase as a Dremio source by using a [community connector](https://github.com/dremio-hub/dremio-hbase-connector).

## Files stored in HDFS

You can query files and folders stored in your HDFS cluster. Dremio supports a number of different file formats.
See [Formatting Data to a Table](/current/developer/data-formats/table) for more information.

## Co-location

Co-locating Dremio nodes with HDFS datanodes can lead to noticeably
reduced data transfer times and more performant query execution.

## Parquet File Performance

When HDFS data is stored in the Parquet file format, then optimal performance is achieved
by storing one Parquet row group per file, with a file size less than or equal to the HDFS block size.
Parquet files that overrun the HDFS block size can negatively impact query times
by incurring a considerable amount of filesystem overhead.

note

Ensure that your Dremio cluster has access to the appropriate ports for each node of your HDFS source. By default, this should be port 8020 for an HDFS NameNode (which should be the one specified when adding the source), and either port 50010 or port 9866 for HDFS DataNodes (dfs.datanode.address, used internally for data transfer).

## HDFS Configuration

This section provides HDFS configuration.

### Impersonation

To grant the Dremio service user the privilege to connect from any host and to impersonate a user belonging to any group,
modify the **core-site.xml** file with the following values:

User impersonation settings for core-site.xml file

```
<property>  
    <name>hadoop.proxyuser.dremio.hosts</name>  
    <value>*</value>  
</property>  
  
<property>  
    <name>hadoop.proxyuser.dremio.groups</name>  
    <value>*</value>  
</property>  
<property>  
    <name>hadoop.proxyuser.dremio.users</name>  
    <value>*</value>  
</property>
```

To modify the properties to be more restrictive by passing actual hostnames and group names,
modify the **core-site.xml** file with the following values:

More restrictive user impersonation settings for core-site.xml file

```
 <property>  
     <name>hadoop.proxyuser.super.hosts</name>  
     <value>10.222.0.0/16,10.113.221.221</value>  
   </property>  
   <property>  
     <name>hadoop.proxyuser.dremio.users</name>  
     <value>user1,user2</value>  
   </property>
```

### Impersonation and Privilege Delegation

You can enable user-specific file access permissions by turning on impersonation in HDFS sources
(check the 'impersonation' box in the source connection dialog).
Users who access data stored on an HDFS source with impersonation enabled will have their access mediated by the
HDFS privileges associated with their Dremio login name, rather than the ones associated with the Dremio daemon.

For example, let's say a Dremio user named `bobsmith` has been granted read access to the
file `/accounts/CustomerA.txt` under the same username in HDFS. However, the `dremio` system user
(the user that the Dremio daemon runs as) does not have read access to this file.
Unless impersonation was enabled when this HDFS source was added to Dremio, `bobsmith` will be unable to query the file.

Enabling impersonation also permits a kind of behavior called 'privilege delegation.'
Under privilege delegation, HDFS data which is subject to restricted access can be shared
with any other Dremio users via the creation of a view in a public (non-Home) space.

### NameNode HA Configuration

If you have configured a secondary NameNode and a Dremio HA configuration,
you must configure Dremio to reconnect with the secondary NameNode in the event the first NameNode goes down.

To configure a secondary NameNode:

1. Ensure that `fs.defaultFs` parameter and value is specified in the **core-site.xml** file *without* the port number.
   (The port is already specified in the URI.)

Specify fs.defaultFs parameter and value

```
<name>fs.defaultFS</name>  
<value>hdfs://xyzcluster</value>
```

1. Configure the NameNode HA parameters via one of the following methods:
   * Copy/symlink the Hadoop **core-site.xml** file to the Dremio **conf** folder if you haven't already done so.
   * Add the following parameters and values to the HDFS source in the Dremio UI under Advanced Options.

     HDFS source parameters and values

     ```
     dfs.nameservices - (say this value is my cluster)  
     dfs.ha.namenodes.mycluster - (say this value is nn1, nn2)  
     dfs.namenode.rpc-address.mycluster.nn1  
     dfs.namenode.rpc-address.mycluster.nn2  
     dfs.client.failover.proxy.provider.mycluster
     ```
2. (Optional) Configure your distributed storage to **hdfs** in the `dremio.conf` file.

For more information on NameNode HA in Cloudera or Hortonworks, see:

* [Setting up NameNode HA on Cloudera](https://www.cloudera.com/documentation/enterprise/5-4-x/topics/cdh_hag_hdfs_ha_enabling.html#cmug_topic_5_12)
* [Setting up NameNode HA on Hortonworks](https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.6.5/bk_hadoop-high-availability/content/ha-nn-config-cluster.html)

## Configuring HDFS as a Source

The HDFS source is usually configured when you are adding a new source, especially the name and connection parameters. However, additional options can be changed or added by editing an existing source.

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Object Storage**, select **HDFS**.

### General

* **Name** -- HDFS Name for the source. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
* **Connection** -- HDFS connection and impersonation

  + NameNode Host

    - No HA - HDFS NameNode hostname.
    - HA - value for `dfs.nameservices` from `hdfs-site.xml`.
  + NameNode Port -- HDFS NameNode port
  + Enable Impersonation -- When enabled, Dremio executes queries against HDFS on behalf of the user.

    - When **Allow VDS-based Access Delegation** is enabled (default),
      the owner of the view is used as the impersonated username.
    - When **Allow VDS-based Access Delegation** is disabled (unchecked),
      the query user is used as the impersonated username.

### Advanced Options

The advanced options tab has the following values:

* Enable exports into the source (CTAS and DROP)
* Root Path -- Root path for the HDFS source
* Short-Circuit Local Reads -- Implementation of short-circuit local reads on which clients directly open the HDFS block files.
  + HDFS Default
  + Enabled
  + Disabled (Default)
* Impersonation User Delegate -- Specifies whether an impersonation username is one of the following:
  + As is (Default)
  + Lowercase
  + Uppercase
* Connection Properties -- A list of additional HDFS connection properties.
* Cache Options
  + Enable local caching when possible -- Selected by default, along with asynchronous access for cloud caching, local caching can improve query performance. See [Cloud Columnar Cache](/current/what-is-dremio/architecture/#cloud-columnar-cache) for details.
  + Max percent of total available cache space to use when possible. Default: 100

### Reflection Refresh

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).  
  If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.
* Automatically format files into tables when users issue queries.
  If this box is checked and a query runs against the un-promoted table/folder,
  Dremio automatically promotes using default options.
  If you have CSV files, especially with non-default options, it might be useful to *not* check this box.

#### Metadata Refresh

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
* **Authorization** -- When impersonation is enabled, the maximum amount of time that Dremio will cache
  authorization information.

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an HDFS Source

To update an HDFS source:

1. On the Datasets page, under **Object Storage** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring HDFS as a Source.
4. Click **Save**.

## Deleting an HDFS Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an HDFS source, perform these steps:

1. On the Datasets page, click **Sources** > **Object Storage** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

Was this page helpful?

[Previous

Google Cloud Storage (GCS)](/current/data-sources/object/gcs)[Next

NAS](/current/data-sources/object/nas)

* HBase
* Files stored in HDFS
* Co-location
* Parquet File Performance
* HDFS Configuration
  + Impersonation
  + Impersonation and Privilege Delegation
  + NameNode HA Configuration
* Configuring HDFS as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an HDFS Source
* Deleting an HDFS Source

---

# Source: https://docs.dremio.com/current/data-sources/object/nas/

Version: current [26.x]

On this page

# NAS

## Working with files and folders in your NAS

If your Dremio cluster is connected to your NAS, you can query folders and files stored in this data source.

All nodes in your Dremio cluster should be able to connect to your NAS.

## Configuring NAS as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Object Storage**, select **NAS**.

### General

* **Name** -- Enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
* **Mount Path** -- Path on the filesystem to use as the root for the source. Needs to be accessible on all nodes.

### Advanced Options

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAicAAAB3CAYAAADYQeADAAABfGlDQ1BJQ0MgUHJvZmlsZQAAKJFjYGAqSSwoyGFhYGDIzSspCnJ3UoiIjFJgv8PAzcDDIMRgxSCemFxc4BgQ4MOAE3y7xsAIoi/rgsxK8/x506a1fP4WNq+ZclYlOrj1gQF3SmpxMgMDIweQnZxSnJwLZOcA2TrJBUUlQPYMIFu3vKQAxD4BZIsUAR0IZN8BsdMh7A8gdhKYzcQCVhMS5AxkSwDZAkkQtgaInQ5hW4DYyRmJKUC2B8guiBvAgNPDRcHcwFLXkYC7SQa5OaUwO0ChxZOaFxoMcgcQyzB4MLgwKDCYMxgwWDLoMjiWpFaUgBQ65xdUFmWmZ5QoOAJDNlXBOT+3oLQktUhHwTMvWU9HwcjA0ACkDhRnEKM/B4FNZxQ7jxDLX8jAYKnMwMDcgxBLmsbAsH0PA4PEKYSYyjwGBn5rBoZt5woSixLhDmf8xkKIX5xmbARh8zgxMLDe+///sxoDA/skBoa/E////73o//+/i4H2A+PsQA4AJHdp4IxrEg8AAAGdaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA1LjQuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjU1MTwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4xMTk8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KUFEt6wAAIbRJREFUeAHtnQe4JEUVRmthyTlHYcmSMwhIEkmSJEoUkCCSJOewJMkoIBlxyUEByZJkASVnkCRZWHLO8dmn/Gpevd6Z3nn7hmHYPff73k5Pd3V11emevn/dut3br6uwoElAAhKQgAQkIIEOITBKh7TDZkhAAhKQgAQkIIFIQHHihSABCUhAAhKQQEcRUJx01OmwMRKQgAQkIAEJKE68BiQgAQlIQAIS6CgCipOOOh02RgISkIAEJCABxYnXgAQkIAEJSEACHUVAcdJRp8PGSEACEpCABCSgOPEakIAEJCABCUigowgoTjrqdNgYCUhAAhKQgAQUJ14DEpCABCQgAQl0FAHFSUedDhsjAQlIQAISkIDixGtAAhKQgAQkIIGOIqA46ajTYWMkIAEJSEACElCceA1IQAISkIAEJNBRBBQnHXU6bIwEJCABCUhAAooTrwEJSEACEpCABDqKgOKko06HjZGABCQgAQlIQHHiNSABCUhAAhKQQEcRUJx01OmwMRKQgAQkIAEJfOfipKurKwwaNCjceuutI+zZePXVV8N+++0XPv/886b6+M0334R33303vP/++wE+34Z98MEH4auvvvo2qrZOCUhAAhKQQJ8ItEyc4ESPPfbYsPjii4dPP/20V4365z//GR5++OFe7fN9KowQuOaaa8Inn3xS2WzEywknnBDmm2++sPTSS4cll1wyLLLIIuHqq6/uk0jhuLnI4Tirr756OPnkkyvb40YJSEACEpDAd0GgZeLkww8/DJdeemn46KOPwoMPPtirvow11lhhjDHG6NU+36fC/fv3D/z169evYbOJYqy33nrhzDPPDDvuuGO45JJLwnnnnRdWXnnlsM8++4Tjjjuuh8BoWFFpw7PPPhuWWGKJ8N5779W2jDrqqGG55ZYLc8wxR22dCxKQgAQkIIFOIdC/VQ258847ozChvgsvvDD86Ec/CqOM0jLt06pmdmw9F1xwQXj++ecDn3PNNVetnfPMM0+MpAwcODAsu+yyYYEFFqhta2ZhtNFGi8IoF38Ipf3337+Z3S0jAQlIQAISaDuBlqgHciROPfXUsOWWW0bnyjTNkCFDhuoMUwvXXXddjAbgdFdcccWAqMFZYkQPdt5553DbbbcNte+LL74YNtlkk/D222/HbUQEdt1110A9/BFteOSRR2r7cSyiEFdeeWWM5Gy00Uax3PLLLz/UNAllb7rpprDqqqvGMgsvvHDct5wj8sorr4Q99tijdsyDDjoovPPOO7VjsvDmm2+GAw44oFaGiAf7VdmXX34Zzj777LDddtv1ECZpnzXXXDPMP//8cRoG1qlvCJkrrrgi0F4YEHm566674m6w3GuvvcLaa68dc1223XbbAAMiW+xPu+hzbvfee2/YeuutY10c7/DDD4/9SWWoc6eddgqPPfZY5MoUHsfddNNNe7CnPFNJp5xySq1t9OGyyy4LtF+TgAQkIAEJVBFoiThhxI9YwPHPNttsYeKJJx7K8dGIiy++OOy5555hwQUXjGJmnXXWCdtss024+eab47QO0w2M9BE6ZSdGzgYCZfzxx4/5KTi7l156KRx//PHh9NNPD+R1bLzxxuHJJ5+s9feJJ56Iiag4T9pGvbPMMkucJrnnnntq5RAGu+yyS1hsscWiKNl+++1j7sfmm28evv7661juqaeeiqKKvpJbc9hhh4Xrr78+ChocPsbU1rrrrhsFGNsRAExxUR99a2QIOUTNUkstVbcI00GrrLJKeP3112vb6dsRRxwRDj300LD33nuHE088MYw99thRXNxxxx3xeD/96U8DnDg2QhChAl/s8ccfj3+pQoTDFltsEcsi6g455JBw1VVXhZ/97Gfh5ZdfjsUQaw899FDYcMMN43aOSx85L+xLHzDO3VZbbRXPCwLptNNOiyKG6M9JJ50Uy/iPBCQgAQlIoCGBYhTdZyucdVeRvNlVjKxjXWeccUb8/sUXX9TqLp486SqcfxdlcyvERNfcc8/dVTiwuLpw5vF7ITxqxT777LOun/zkJ11FDkZX4fi6fvGLX3QVUY7a8ShYiIiuwoF3FWIl7ke53XffvatILu169NFHa3VRrkgG7SqESlz3xhtvxOOdf/75tTIspHbcf//9se6f//znXYVY6XHMIiIS9y1EV9z33HPP7VpooYW6Cmdeq4t2FFMocX3xBE5tfb7wzDPPVG6nbCHgamWosxBTXSuttFJXXid9K4RDDzaFcIj7ffzxx7VDsn8hmGoMClER+8G5YVuyQvBF7oXwiAyKROf4nfOYHzft/8ADD8Rd6T/n9JZbbklVxU/qZ99C5PRY7xcJSEACEpBATqDPkZPC6cUQfx4dIEpBAmYhCmqiiFE1T/Ew6s5t1llnjU+mFI2Kq+ecc84w1VRTxWhKKsc0AtMnhUCJSaVECchryaMRRBdmmGGGHom1HI9oQZ7DQR4MUYT77rsvjvCZBiHiwNMruc0777yByAP1vvDCCzEytMMOO/Q4Ju0kMnHDDTfECMvdd98d1lhjjTDNNNPUqmJ/Ijd9tZlmmqlHFYXwC4VgChNOOGFtPX2jja+99lqMJLGBKSOM8o3s9ttvjwyIdtDeZOONN14g2sGTVDzWjBFJIiqUH5dIGeyJ5mDsR45LIexqx2c901YXXXRRLXrDOk0CEpCABCRQJvD/ZI/y2l58L0bL0XGRrJlsuummizkSOCJyF3B4TF2QWzLmmGOmYnU/mXYgt4SpGnIk2Ie8kSIiEaaYYoq4z2STTRbFAo/dXn755T3eH1KM2HvUS9myISrIfcFw3tSLQMmNNjNlgTFlhTUSGdNPP3102s8XUz7099swppWasdTfXGQMaz+E4YwzzhjGGWecoYpyLrFUHyInFyZpG+IkCRim3pjOISeHKbMiwhOFHtNmqb5Yqf9IQAISkIAE6hDokzjBqZGrwGiaR1PLxuj5rbfeCjjMYb3jI9+XCMlRRx0V80dwmtdee2045phjak//kOtRTNlEIUC5ySefPIoYkmJTBCavr7xMmfxJonpOubwP34nYTDrppD2iAawnUkCdCJ0UqWB9s4YAI5+Dl7WVHX+qg5eyTTnllDHnJq1r52fONV9ObeAayJkSseKaIOemmN4Ju+22WyyK4CMipUlAAhKQgAQaEeiTOMGZkszKUzMkwuZPt6SnRXjyBkc188wzx6dx6jlvpmeKXIdaG4lsECkhurHooovGqRSSaDH2x8HxZBBiJDfe25HXk29rtExEgGkb2s77VnJjOglBQF8wplamnXbavEhtGYfNFFXOIG1MTyOl7+XPqaeeOgo4WM4+++zlzbFPRI9S5CgVGH300dNi7bPIz4nL9QRErVBpITEgKlKObCEue2ucA8QoQouIGn/77rtvOPDAA2OCMo+ZjzvuuL2t1vISkIAEJDCSEOhTzgmPouJkNthgg/heE95qmv4YNZOPMah4NT2j6kkmmSRGN4iC5EYuCU+AlPNHeFKGl5CRQ8H0TnJmOFCeiilPD5BnwSi9LDDyY9Vb5g2sPG3D48+54ZTJjyGPYsCAATEPhqdjyuKHp17Ip8HBk6fC4735C8+oc/DgwXnVQy0zlcWUEVNZCKKywYz8HR4HTtEJhAm5IrBNhiA566yzIgOiOckQTFVv7U0MiILlRl8RgjzhxFRNs0Z7ESScp2RE0cj1ob31BGoq56cEJCABCUhguMUJDo98grXWWivUG8GDluRQHjN9+umn4ygaB1w8sRHOOeec+BgwznW11VYb6l0h7MvLxki0xMhZSEZuCLkL5DPwqCvOnM8VVlgh1sNjr81EDZLIIGrB+0GI/uCcaS+JrTzmjCAihwXHyv+NQxSIxF8ECzk0PBq9/vrrx4RY2kd/cb6INd658txzz0XnTp+HZcUTSDGpFEGEoCPPhTwTBBFviGU7r7VPhpgjqZdHeBFIPFZ99NFHhxtvvDE+WpyiNUR+6EfxNFKsMxcMiQEJvLzfhGMVT1rF97LQR9Yhijh+Lh5TG8qfqT6iXlwfcCUnCVZMxfGOGITOBBNMUN7V7xKQgAQkIIEageGe1kEEEDHgiZFGxlQPEQ5etMZ0BU9r4MDIH+EPwwHi9Mt5H3xHIODUyDtJRoSCt5uSfMlUQTJefMa7TojmIE4oRxSlnnBiG04bY5l6iAwMHDgwruMfxBHOPuWA8P/c8P4PXkKGUEjGVAUCDSO3pnicOL67hXeuYDh+9iEqkgRD3FD6BwHEK+t5JwjRCv4wRAHtgnOKmrCeCBKvpUfAIZCS8e6RspgjCkW+DKIQ8UGkBMujIZybiSaaKBx55JGxLNuZXiN6lZ52Skwb9SPVB1v6wjttNttsM6qKxntcDj744B79SNv8lIAEJCABCSQC/QpH/u38t7fpCHU+mWJI+Q045eE18hrIByGa0shh9qZu2kTbEARpGqne/jw+jXFcHHY9QyhhTK80KlNvP9Yh4IhwsF+9/Tll5NsgoBAecGCqBEHXiENiVa++vB35sZPYyLf3djm1jVyWvpzr3h7X8hKQgAQk8P0lMNyRk750mYhGb3ND6h2v/PhvvTK9WUeUpV6kpVxHOcpT3s73vjh2IiTNTH0gprBmODRThrqaPTZlm7Fmj9tMXZaRgAQkIIGRg8Bw55yMHHg6t5dEb+o9GdS5LbZlEpCABCQggeYIfCeRk+aaZqlGBJju4UkonoDSJCABCUhAAiMage8k52REg2h/JCABCUhAAhJoHQGndVrH0pokIAEJSEACEmgBAcVJCyBahQQkIAEJSEACrSOgOGkdS2uSgAQkIAEJSKAFBBQnLYBoFRKQgAQkIAEJtI6A4qR1LK1JAhKQgAQkIIEWEFCctACiVUhAAhKQgAQk0DoCipPWsbQmCUhAAhKQgARaQEBx0gKIViEBCUhAAhKQQOsIKE5ax9KaJCABCUhAAhJoAYE+vb5+yJAhLWiCVUhAAhKQgAQkIIFuAr6+vpuFSxKQgAQkIAEJdAABp3U64CTYBAlIQAISkIAEugkoTrpZuCQBCUhAAhKQQAcQUJx0wEmwCRKQgAQkIAEJdBNQnHSzcEkCEpCABCQggQ4goDjpgJNgEyQgAQlIQAIS6CagOOlm4ZIEJCABCUhAAh1AQHHSASfBJkhAAhKQgAQk0E1AcdLNwiUJSEACEpCABDqAgOKkA06CTZCABCQgAQlIoJuA4qSbhUsSkIAEJCABCXQAAcVJB5wEmyABCUhAAhKQQDcBxUk3C5ckIAEJSEACEugAAoqTDjgJNkECEpCABCQggW4CipNuFi5JQAISkIAEJNABBBQnHXASbIIEJCABCUhAAt0EFCfdLFySgAQkIAEJSKADCPTvSxtuv/328N577/WqigknnDAsueSSvdrHwhKQgAQkIAEJjDwE+iROECarrbZar2hdddVVvSo/vIX//e9/h/HHHz/84Ac/GKqKBx98MK6fdNJJh9o2Iqz46quvQv/+fTq1TWEYMmRIeOONN8K8884b+vXr19Q+37dCb775Zthwww3DtddeG0YbbbTY/G+++SZ8+eWXYYwxxmhpd7744ovQ1dXV8nrzRvK7GGecccKAAQPy1S1b/vzzz+O1N+qoozZV5yWXXBK4XmGsSUACEkgEOmZa5/LLLw/zzDNPjz+ED46gt8YN/pBDDgmXXnrpULuy7Xe/+1149tlnh9rWaSto63/+85948262bbfddltYaqmlovOs2gen+9prr1UVqbvtxRdfDB999FHcRuRsp512ig61buHv+Uqc5sYbbxy22267KExwvAMHDgzzzTdfWHjhhcOKK64Yr6PPPvssLL744j2u3XQt43TTNfzkk0+G+eefP7z88ss9yHAe1l577bDQQgvFerfffvvw/vvv9yjTii/pd/G3v/2tR3Ws32+//Wrtp41nnnlmrd30b7nllqttp29HHHFE+OSTT2r1IPhhAJfy/vzWEo/0mfZfeeWVwx//+Mdwzz331OpyQQISkEDHiBNOxbjjjhuuvvrqcM0118TP0047bbhH5JNNNlmYYIIJ6p7h8cYbry2RhboH78VKnCNOK3cCw9qdm//JJ588zP7dcMMN4bzzzhtWdT2248T23HPPgJPFiCRMM800PcqMSF+uvPLKQHRt9dVXjwJsn332CXD761//Gm6++ebw4x//OGyyySZRCBIB+Pvf/x5OPPHEQNTgnHPOid//8Ic/hFFG+f/PjOv666+/DjfddFMNE+d40003DT/84Q9j3Vz/b731Vth1111r4qBWuAUL0003Xd3IDGKIwcCNN94YTj311Hht/Pa3v621gXYffPDBse1nnXVW7BtCjWsCwUofNthgg3DLLbeEU045JZxwwgmRQd7kxCTfn9/8scceG3bbbbdeifC8XpclIIERj0DHiBNucjPMMEOYdtpp45QLN9Gpp546EOreaqut4oiVkRmjMpxAsvvuuy8ss8wycWS2xx57hI8//jhuGmusseINkpEZDvukk06q3WjTvny+8MILYY011ohldthhh7ojVtr25z//OZZhZIhzYTS84447hkGDBsXqiETQjsceeyxcf/31gbZss802cZ98JJzXRV8uuuiiWBej8i233DJsttlmcR+mERZccMFYN07wkUceCR9++GHYa6+94nZG7Q899FDcnv+Dk/nLX/4SnQYOFKex8847x31+9atfxRyhww47LBx55JHRedA2+sLoNnGgHFM2udG+lVZaKTz++OOB7WeffXYUjnzHicGY9WnEn/czMcvrYzkvA4vLLrssrmNbo/YktikagcOnLdSFQ1x33XXj6B1hy7TjtttuG9vG+qeffpqqo916662xHO3Gmab60na+40TZH3Hx0ksvRcd9wQUXhFlnnTUgfnffffcoTJ544ol43XK9cv0ypTbTTDPF63fyySePVXJdEsnj/FIv00IYXDmva621VphyyikD1/1RRx0VhV8qEwsW/xBh+c1vflPrT4r+1TvP6TxQP6KCfq633nrxt8Nvo55NP/30YYoppgiLLrpoFGAwSkKU3+GMM84Y6A8RHiJm9BtO/La49rmWJplkkrDEEkvEdaxPUTamwBIT9kcAEeWDC98RulxLmgQkIAEIdIw4IWfh+eefD88880x0Ik899VS8sTGyZGrj7rvvjqFmBMT+++8fb+ivvvpqdIjcFBlxsg+OJhlOgtHu8ccfH3BWuaihDDdGwu4k6DLyff311wOOG0eXG9uIRuBUqG+XXXaJo0Wc8XHHHRcdFzdinNMcc8wRIx0ca/nll48C4IEHHghHH310rPL888+PTpS6GGUzxcQInX7Sd/rESBKHTpmxxx473sgRbqzHQV1xxRVhlVVWiaINx5YbIfi77rorrvrggw8C4XamIc4999zw3HPPBabPaDcjfkbKOFjq4DtOgpwgRrPrrLNOoK5ko48+egy/0w4EEqIPY0TNfql+BAZWjxnnNzdG2XDF4SOWBhYj8UcffTTQ7kbt4ZzhFJPh/JIjZgQPw7333jtOuWy++ebhnXfeibwQtr/85S/jNUXeRbqOzjjjjMj5uuuuS1XGT9rwyiuvRCHCCs4PDhbnm2zMMccM//rXv+K5SuvSJ1xyY9oCUYDYwREjYjHOL2IAYQo7BBUChes4z2nh+BtttFGYeOKJY4RlkUUWCVtssUXkX+88p/Pwpz/9KZ5TPhFGGEKjnuXXPf3kGKmdeXnKMShIBmN+Q3neEUIGywVWnoeCsOaaggm/07nnnjvcf//9qUo/JSCBkZxA/07qP44Gp5iMaMWcc84Zv+LEcfzc9E4//fToLLiBIkqYvsEZ4DAZSRMp+PTTT6MTTk8GEcXghk3EIRmCB8OJ4ZDJLUD4UFdKKOXmikhgpIiTJ/xOtATBhPhYf/31w6qrrhpD+Th2RtncvHHia665ZvzOSJhICo6HPiGAcOgY9bJuhRVWiN+ZiyeKgPFkEzdwbty0j/35nGiiiaJzZbSaOzD2Se1mObUDR0+7iEC9/fbbYaqppgqMktmXT6IRGKIDx3nooYfGHANGsgsssEDchuOZeeaZY8RgttlmiyPoRvVXMYNLMkQFxyNxea655oqChujBnXfeGYvUaw8b0jRJqid94nS33nrrGIUgkkVkgb7RX8QIybsILiJLSy+9dDx/HJ/pCI6J4EuGUIUl25PRTpJJc+P8DMvghHhDRCNoON6FF14Yrye4IlyZ8kCc8cc1ynXI8ZLh2IkQ4czZB/GKAESYVJ0HojUHHXRQLE85RDOfzRjHSnlJLBOFm2WWWeIgArHEdcu5IHrCNZEbERb2SUYEh98AEad77703Cnr6mAQL4jEdK+3jpwQkMPIS6Bhxwg0TR0lUIHc+OBOcTn5DTQ6BckREEAXc9HBIyelzSvN6cFA4nNxwjgiiZZddtrYah00kAQGAcWxurIzs+UtGFAAngTMkGoFDIaRfz3hiCLHEqJ/PvBwhcKIpWLmfafSNI+BYJC0y8ibhlXYSeUks6h23vC53tDlP2jWgeHojOQpychBEeZlUV3n6I63nM9VfxSwvT+QGkYe4w/bdd98YqehNe/L6WE7nnNE8jJKDRGgcfvjhsU+cX6YsiFgkQxzRt7R/LvJSGYQAbYNPMvKBOAf1yqcyXHdEGhDWMH744YdjdIvrDwHKvkSzcP5sIzIHCyJ+qT3URQIyfaAOrg36x3VRtvw8lK+3ctmq7/Q1Pe3G8RDx/L4QOwhzxDrXCG0k4sXUUTKEIMfODWFP5IdBBtcX3zUJSEAC9Qh0jDihcfmNuF5jy+sIOTM1cMcdd8SIAnkaiJVkueNGhMw+++xD3cxxDiQBcpNPzjl9Uk9aZnSLAElCIbX14osvjuKFETqjc+bssXyETcQDh8ZImDbh5JIRnSC0X2U4L5wAfUDIEJkgQsTxSNBMQqqqDraVxUZyYvSdHJO0HXHBFFAjS0zK29P+aXsjZmk/nDbijuRPnDeRHaIzw2pPzraec6Z+Ikycq9QmPplKwCHSP5JceaKL5SQs0jlN7cs/KYNI5UkbriMM573YYovFiEaKduX7pGVylBASOHiu1fQIO8tEHIhsUYbrgEgVkUGmcBAv6dwiqBAmREvoA+eLHKF6lvpMm8vXG+emkcDMWVI/54RpPwxOiHhEBeKE3BeeZOJ6R2wPHjw4RoQSQ6ZYOVa6xug/AqzRtZ7/Jur1yXUSkMDIRaCjck7efffdGNrlxpj+Gt1IOU3c7HHU5BqQ7EhORsoJ4KZMPkHKQyBZklB4fgPGsSAcCH1TF0KHaZb8mNxUSQTlhkxSZMrPIFGQ3AXEEAKFGzejXfblGEQEyI2gTwcccEAcZeJUiRYQ3qZ/LxTJuDjwNP1TvvRoEw6WPArq/fWvfx0dFPXjINnWF6P9CB44EGmgH0SqBhXTVjheEhjrGftVHbuKWV4fUx2IBJwwUQVG1fS5qj3UDdv//ve/8Q/+rCsbkTKmFsgFYgSfkkZZJvmUPJ80rUcZ+p4bTyHhWDnfGHkgTAUR1eA6oM3kGyGCkljJ908CgeuTfg4spmsOPPDA+AgunyRTk1eC+KDM73//+/iUDueBKR8iPnmEJl2TROyISnA9D8vSeUjXG+eN3JckHsv781th2g8uJBATocuna2gnRi7KgCLSxiPAGBGVlBPG74k8J35HTKXCJxnirp7BCnEGY00CEpAABDoqcsKNDSGQjJsrOSUIjTS6Tdv45OVfOHvm8DFupNy4cXDcgBnVsR0j6oEIwNLojvwGnhrgJkquB/vgqNJ2yiIEcCQ4jTT9QF04L5JpSbLEOeG0yBsh9I5xI07t4gbNaJh6yTsgYpD6SZsI5+Psy/1klInoYTvvnSB5lCRIHmXFcHJEfsqWRqc419w55MIMduS+0Kd//OMfPTjAHWFXrpv9KY+jZQoN8VKv/kbMmLbLDa4knS5T5M5gsGCqAA75ecnbA3um8dJ5ZVvqFw6dfTFYwxx2RBs4twgZBBDH43wRtcE4l3nEjXXUy/QDycVMbXCMlLSbrgMEEMKDPJKypesVIcO1k08hUZb3hiBMmRbiiS3akwQS1zECMdVBec4F55tHubEkGhCXVeeZPCoSstP1xr70rWywgyt/sGI/REf6LeTXJuvIS+L6JpF3QCFUyMsimpIEC0Ka30ZuKYqSr2MZAUgEMT2dVt7udwlIYOQj0K8YtTSXHVeHTe4k6myuu2p49qlbUbaSkDM3zPxmnjYz4mS0nE8FpG35J2KCG3BydPm2tFx1nFSGTxJvicbguIhEcOMv10tdoK/nKPK6WMaB5XXwnf1wIn0x2DAazttAxARxU25vfpxmObBPM2Wr8jYatYfzRf/rnfO8rSyX+aXt9fqftvHJNBA5PoOLKYskeljfm3NH+WatmXqH1eZGx2rEoFH54V1fdS4b1clUJYwRiEkMNSrreglIYOQg0DHTOn3BnY/qyvVwsxuWMGEfHHSVQ6ZM1XHYngyHT0QAa+ToqSsXBWnfep/lOvjeV2HCcWBTbgOsWsWBYzTDjP40EhmN2kO7G+3DcXMr80vb6vU/beOT6BLRsPIL0Xpz7vL6hrXcTL3DanOjYzRi0Kj88K6vOpf16kQAHnPMMTESQ980CUhAAhDo07QOoWYiIb2x8lRBb/b9vpTl8WXC7sNy8t+X/oys7eT8kS9EDkgfAowjK76m+s20FNNaKZG8qZ0sJAEJjPAE+jStM8LTsYMSkIAEJCABCbSdgHHUtiP3gBKQgAQkIAEJVBFQnFTRcZsEJCABCUhAAm0noDhpO3IPKAEJSEACEpBAFQHFSRUdt0lAAhKQgAQk0HYCipO2I/eAEpCABCQgAQlUEVCcVNFxmwQkIAEJSEACbSegOGk7cg8oAQlIQAISkEAVAcVJFR23SUACEpCABCTQdgKKk7Yj94ASkIAEJCABCVQRUJxU0XGbBCQgAQlIQAJtJ6A4aTtyDygBCUhAAhKQQBUBxUkVHbdJQAISkIAEJNB2AoqTtiP3gBKQgAQkIAEJVBFQnFTRcZsEJCABCUhAAm0noDhpO3IPKAEJSEACEpBAFQHFSRUdt0lAAhKQgAQk0HYCipO2I/eAEpCABCQgAQlUEVCcVNFxmwQkIAEJSEACbSegOGk7cg8oAQlIQAISkEAVAcVJFR23SUACEpCABCTQdgKKk7Yj94ASkIAEJCABCVQRUJxU0XGbBCQgAQlIQAJtJ6A4aTtyDygBCUhAAhKQQBUBxUkVHbdJQAISkIAEJNB2AoqTtiP3gBKQgAQkIAEJVBFQnFTRcZsEJCABCUhAAm0noDhpO3IPKAEJSEACEpBAFQHFSRUdt0lAAhKQgAQk0HYCipO2I/eAEpCABCQgAQlUEVCcVNFxmwQkIAEJSEACbSegOGk7cg8oAQlIQAISkEAVAcVJFR23SUACEpCABCTQdgKKk7Yj94ASkIAEJCABCVQRUJxU0XGbBCQgAQlIQAJtJ6A4aTtyDygBCUhAAhKQQBUBxUkVHbdJQAISkIAEJNB2AoqTtiP3gBKQgAQkIAEJVBFQnFTRcZsEJCABCUhAAm0n8D9a8zriANfDLgAAAABJRU5ErkJggg==) !

* Enable exports into the source (CTAS and DROP).

### Reflection Refresh

![](/assets/images/hdfs-refresh-policy-9ae71114907887b859a9d01425390739.png) !

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

![](/assets/images/nas-metadataD-404041022ad0b766a1ab8584df7b0668.png) !

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).  
  If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.
* Automatically format files into tables when users issue queries.
  If this box is checked and a query runs against the un-promoted table/folder,
  Dremio automatically promotes using default options.
  If you have CSV files, especially with non-default options, it might be useful to *not* check this box.

#### Metadata Refresh

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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an NAS Source

To update an NAS source:

1. On the Datasets page, under **Object Storage** in the panel on the left, find the name of the source you want to edit.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring NAS as a Source.
4. Click **Save**.

## Deleting an NAS Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an NAS source, perform these steps:

1. On the Datasets page, click **Sources** > **Object Storage** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

Was this page helpful?

[Previous

HDFS](/current/data-sources/object/hdfs)

* Working with files and folders in your NAS
* Configuring NAS as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an NAS Source
* Deleting an NAS Source

---

# Source: https://docs.dremio.com/current/data-sources/databases/opensearch

Version: current [26.x]

On this page

# Amazon OpenSearch Service

[Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) is a managed service that makes it easy to deploy, operate, and scale OpenSearch clusters in the AWS Cloud.

## Compatibility

Dremio supports the following Amazon OpenSearch Service versions:

* 5.x
* 6.0
* 6.2
* 6.3
* 7.0+

Amazon OpenSearch is supported as a data source in Dremio Software on-premises deployments.

## Configuring Amazon OpenSearch Service as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Amazon OpenSearch Service**.

### General

On the General tab, enter a name for the source, connection details, and authentication credentials. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

| Name | Description |
| --- | --- |
| Host | AWS OpenSearch Host name. |
| Port | Port on which the AWS OpenSearch service is running (usually 443). |

#### Authentication

Choose one of the following authentication methods:

* **AWS Access Key**: Used for key-based authentication.
  + Under **AWS Access Key**, enter the [AWS access key ID](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).
  + Under **AWS Access Secret**, store the [AWS access secret](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) using one of the following methods:
    - Dremio: Provide the secret in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the secret reference in the required format.
* **EC2 Metadata**: Dremio uses the IAM policy from the EC2 instance.
* **EKS Pod Identity**: Dremio uses the IAM policy associated with the coordinator's Kubernetes service account.
* **AWS Profile**: Dremio sources profile credentials from the specified AWS profile. For information on how to set up a configuration or credentials file for AWS, see [AWS Custom Authentication](/current/data-sources/object/s3#aws-custom-authentication).
  Under AWS Profile (Optional), enter the AWS profile name. If this is left blank, then the default profile will be used. For more information about using profiles in a credentials or configuration file, see AWS's documentation on [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
* **No Authentication**: No credentials required.

Select the option to perform keyword searches when pushing down fields mapped as text and keyword if desired.

### Advanced Options

On the Advanced Options tab, enter the options specific to the OpenSearch Service, encryption, and AWS.

#### OpenSearch options

* Show hidden indices that start with a dot (.).
* Use Painless scripting with OpenSearch 5.0+ (Checked as a default).
* Show \_id columns.
* Use index/doc fields when pushing down aggregates and filters on analyzed and normalized fields (may produce unexpected results).
* Use scripts for query pushdown\*\* (Checked as a default).
* If the number of records returned from OpenSearch is less than the expected number, warn instead of failing the query.
* **Read timeout (seconds)** (default: 60)
* **Scroll timeout (seconds)** (default: 300)
* **Scroll size** -- This setting must be less than or equal to your OpenSearch value for the
  `index.max_result-window` setting. (default: 4000)

#### Encryption

Validation modes include:

* Validate certificate and hostname (default)
* Validate certificate only
* Do not validate certificate or hostname

#### AWS

* **Overwrite reqion** -- If the box is checked, provide the region.

### Reflection Refresh

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).  
  If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions.
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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an Amazon OpenSearch Service Source

To update an Amazon OpenSearch Service source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Amazon OpenSearch Service as a Source.
4. Click **Save**.

## Deleting an Amazon OpenSearch Service Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Amazon OpenSearch Service source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

Was this page helpful?

[Previous

Databases](/current/data-sources/databases/)[Next

Amazon Redshift](/current/data-sources/databases/redshift)

* Compatibility
* Configuring Amazon OpenSearch Service as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an Amazon OpenSearch Service Source
* Deleting an Amazon OpenSearch Service Source

---

# Source: https://docs.dremio.com/current/data-sources/databases/redshift

Version: current [26.x]

On this page

# Amazon Redshift

## Configuring Amazon Redshift as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Amazon Redshift**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

* **JDBC Connection String** -- Connection string. The connection URL can be found in AWS console.

#### Authentication

Select an authentication option:

* No Authentication
* Master Credentials (default):
  + Username: Redshift username
  + Password: Select the password store from the dropdown menu:
    - Dremio: Provide the password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the correct format.
* Secret Resource URL: Provide the Username and Secret Resource URL to use for authentication.
* EKS Pod Identity: Dremio uses the IAM policy associated with the coordinator's Kubernetes service account.
* AWS Profile: Dremio sources profile credentials from the specified AWS profile. For information on how to set up a configuration or credentials file for AWS, see [AWS Custom Authentication](/current/data-sources/object/s3#aws-custom-authentication).
  + AWS Profile (Optional): The AWS profile name. If this is left blank, then the default profile will be used. For more information about using profiles in a credentials or configuration file, see AWS's documentation on [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
  + DbUser (Optional): The name of the Redshift DbUser to use for authentication. If this is left blank, the default user name for your AWS IAM role will be used (generally this is the same as your AWS username).

### Advanced Options

![](/assets/images/redshift-adv-options-54c04307ef59c6c77f1393333f29e0a4.png) !

* **Record fetch size**: Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. Default: 10
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to *8*.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to *60*.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Enable legacy dialect**

### Reflection Refresh

![](/assets/images/hdfs-refresh-policy-9ae71114907887b859a9d01425390739.png)

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

![](/assets/images/mongodb-metadataA-4215ce9cc791254ae9684171d87714d6.png)

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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an Amazon Redshift Source

To update an Amazon Redshift source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Amazon Redshift as a Source.
4. Click **Save**.

## Deleting an Amazon Redshift Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Amazon Redshift source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

`*`, `+`, `-`, `/`  
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
DATE\_SUB  
DATE\_TRUNC\_CENTURY  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_DECADE  
DATE\_TRUNC\_HOUR  
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
MEDIAN  
MIN  
MOD  
PERCENT\_CONT  
PERCENT\_DISC  
PI  
POSITION  
POW  
POWER  
RADIANS  
REPLACE  
REVERSE  
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
TIMESTAMPADD\_WEEK  
TIMESTAMPADD\_YEAR  
TIMESTAMPDIFF\_DAY  
TIMESTAMPDIFF\_HOUR  
TIMESTAMPDIFF\_MINUTE  
TIMESTAMPDIFF\_MONTH  
TIMESTAMPDIFF\_QUARTER  
TIMESTAMPDIFF\_SECOND  
TIMESTAMPDIFF\_WEEK  
TIMESTAMPDIFF\_YEAR  
TO\_CHAR  
TO\_DATE  
TRIM  
TRUNC  
TRUNCATE  
UCASE  
UPPER  
VAR\_POP  
VAR\_SAMP

## Running Queries Directly on Redshift Through Dremio

Dremio users can run pass queries through Dremio to run on Redshift. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

## For More Information

* See [Redshift Data Types](/current/reference/sql/data-types/mappings/amazon-redshift/)
  for information about mapping to Dremio data types.

Was this page helpful?

[Previous

Amazon OpenSearch Service](/current/data-sources/databases/opensearch)[Next

Apache Druid](/current/data-sources/databases/apache-druid)

* Configuring Amazon Redshift as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an Amazon Redshift Source
* Deleting an Amazon Redshift Source
* Predicate Pushdowns
* Running Queries Directly on Redshift Through Dremio
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/apache-druid

Version: current [26.x]

On this page

# Apache Druid

[Apache Druid](https://druid.apache.org/) is a high performance, real-time analytics database that delivers sub-second queries on streaming and batch data at scale and under load.

## Prerequisite

Ensure that your Dremio cluster is at version 24.2 or later.

## Configuring Apache Druid as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Druid**.

### General

1. In the **Name** field, specify the name by which you want the Druid source to appear in the list of data sources. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, follow these steps:
   1. In the **Host** field, specify the hostname or IP address of the Druid source.
   2. In the **Port** field, specify the port to use. The default port is 8888.
   3. (Optional) Select **Use SSL** to use SSL to secure connections.
3. Under **Authentication**, specify the Apache Druid username. Then, choose a method for storing the Apache Druid password from the dropdown menu:
   * Dremio: Provide the password in plain text. Dremio stores the password.
   * [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
   * [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
   * [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown menu and enter the secret reference in the required format.

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

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Druid Source

To update a Druid source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Apache Druid as a Source.
4. Click **Save**.

## Deleting a Druid Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Druid source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

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

[Previous

Amazon Redshift](/current/data-sources/databases/redshift)[Next

Dremio Cluster](/current/data-sources/databases/dremio)

* Prerequisite
* Configuring Apache Druid as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Druid Source
* Deleting a Druid Source
* Predicate Pushdowns

---

# Source: https://docs.dremio.com/current/data-sources/databases/dremio

Version: current [26.x]

On this page

# Connecting to Another Dremio Software Cluster

You can add a Dremio Software cluster as a data source. Such a cluster is referred to as a *data-source cluster*. The Dremio cluster that you add it to is referred to as a *querying cluster*.

caution

Only Dremio Software can serve as a data-source cluster. Using Dremio Cloud as a data-source cluster is not supported.

A data-source cluster gives a querying cluster access to one or more data sources, such as Amazon S3, Hive, and Postgres, that are connected to the data-source cluster. Dremio treats the connected Dremio cluster as any other supported data source. The data sources that are connected to the data-source cluster are represented as schemas. From a querying cluster, you can drill down into the schemas to see source datasets. You can then promote source datasets to tables, create Reflections and views on those tables, and views on the views, and so on.

## Example

In this diagram, there are two Dremio Software clusters: **Dremio\_1** and **Dremio\_2**. Suppose that you wanted to access **DataSource\_2** from **Dremio\_1**. To do so, you would add **Dremio\_2** as a data source to **Dremio\_1**. In fact, you could add any number of Dremio Software clusters as data sources.

![Connecting one Dremio Software cluster to another](/images/D-to-D-intro.png)

In the UI for **Dremio\_1**, **Dremio\_2** is listed under **Sources** > **Databases**. If you were to select **Dremio\_2** there, you would see the folder **DataSource\_2**. Double-clicking that folder would show a list of the folders or schemas in that data source.

An administrator can promote a table on a data source connected through a data-source cluster, just as it is possible to do on data source that is directly connected to a querying cluster. For example, an administrator promotes table `DataSource_1.Table_1` from `DataSource_1.Source_1` on the data source directly connected to **Dremio\_1**, and also promotes table `Dremio_2.DataSource_2.Table_2` from `DataSource_2.Source_2` via the data-source cluster.

![Connecting to a data source directly and through a Dremio Software cluster](/images/D-to-D-mix.png)

The administrator can then use the tables as any other table, by querying them, creating views on them, and creating Reflections on them.

If **Dremio\_1** were connected to two Dremio clusters, the administrator could promote tables on both. Then, business users could run queries and view reports that federated data across the two data-source clusters.

![Queries can federate data that is in two or more clusters.](/images/D-to-D-federation-2.png)

And while business users run queries through the querying-cluster, other business users can continue running queries directly through a data-source cluster.

![Business users can still query data-source clusters directly.](/images/D-to-D-federation-3.png)

caution

* Ensure that the Dremio instance that you connect to does not itself connect to your original Dremio instance. For example, if **Dremio\_1** connects to **Dremio\_2** as a data source, ensure that **Dremio\_2** does not connect to **Dremio\_1** as a data source.

![Avoid recursive loops.](/images/D-to-D-mix-recursion.png)

* Querying across more than one region or more than one cloud vendor might increase query latency. Querying across cloud vendors also might result in egress charges from cloud vendors. For example, in this diagram **DataSource\_1** is using one cloud vendor, while **DataSource\_2** is using a different cloud vendor. Queries from **Dremio\_1** across **Dremio\_2** and **Dremio\_3** against those two data sources might incur egress charges from the cloud vendors.

![Federating data across cloud vendors can incur egress charges.](/images/D-to-D-federation-4.png)

tip

Dremio recommends full TLS wire encryption on querying clusters and data-source clusters. For more information, see the configuration of TLS for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#full-wire-encryption-enterprise).

## User Impersonation

When you connect a querying cluster to a data-source cluster, you provide the username and password of an account on the data-source cluster. By default, queries that run from the querying cluster against the data-source cluster run under the username of that account.

You can instead allow users running queries from the querying cluster to run them under their own usernames on the data-source cluster. For example, User 1 on the querying cluster Dremio 1 can run queries as User 1 on the data-source cluster. User 1 must have an account on the data-source cluster, and that account must use the same username. User impersonation (also known as *inbound impersonation*) must be set up on the data-source cluster. The policy for user impersonation would look like this:

Example policy

```
ALTER SYSTEM SET "exec.impersonation.inbound_policies"='[  
   {  
      "proxy_principals":{  
         "users":[  
            "User 1"  
         ]  
      },  
      "target_principals":{  
         "users":[  
            "User 1"  
         ]  
      }  
   }  
]'
```

See [Inbound Impersonation](/current/security/rbac/inbound-impersonation/) for more information.

## Limitation

You cannot query columns that use complex data types, such as LIST, STRUCT, and MAP. Columns of complex data types do not appear in result sets.

## Prerequisites

* You must have a username and password for the account on a data-source cluster to use for connections from the querying cluster.
* The querying cluster and data-source clusters must all be at version 23.1 or later.

## Configuring Another Dremio Software Cluster as a Source

note

If the cluster that you are connecting to has a self-signed certificate, ensure that the cluster that you are connecting from has a copy of that certificate in its truststore.

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Dremio**.

### General Options

1. In the **Name** field, specify the name by which you want the data-source cluster to appear in the **Databases** section. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, specify how you want to connect to the data-source cluster.
   * **Direct**: Connect directly to a coordinator node of the cluster.
   * **ZooKeeper**: Connect to an external ZooKeeper instance that is coordinating the nodes of the cluster.
3. In the **Host** and Port **field**, specify the hostname or IP address, and the port number, of the coordinator node or ZooKeeper instance.
4. If the data-source cluster is configured to use TLS for connections to it, select the **Use SSL** option.
5. Under **Authentication**, specify the username for the querying cluster to use when connecting to the data-source cluster. Then, choose a method for storing the password for the querying cluster from the dropdown menu:
   * Dremio: Provide the password in plain text. Dremio stores the password.
   * [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
   * [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
   * [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the secret reference in the required format.

### Advanced Options

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |
| **User Impersonation** | Allows users to run queries on the data-source cluster under their own user IDs, not the user ID for the account used to authenticate with the data-source cluster. Inbound impersonation must be configured on the data-source cluster. See [Inbound Impersonation](/current/security/rbac/inbound-impersonation/). |

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

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges.

note

All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Dremio Source

To update a Dremio source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Another Dremio Software Cluster as a Source.
4. Click **Save**.

## Deleting a Dremio Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Dremio source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Predicate Pushdowns

Querying clusters offload these operations to data-source clusters. Data-source clusters either process these operations or offload them to their connected data sources.

`&&`, `||`, `!`, `AND`, `OR`  
`+`, `-`, `/`, `*`, `%`  
`<=`, `<`, `>`, `>=`, `=`, `<>`, `!=`  
ABS  
ADD\_MONTHS  
AVG  
BETWEEN  
CASE  
CAST  
CEIL  
CEILING  
CHARACTER\_LENGTH  
CHAR\_LENGTH  
COALESCE  
CONCAT  
CONTAINS  
COUNT  
COUNT\_DISTINCT  
COUNT\_DISTINCT\_MULTI  
COUNT\_FUNCTIONS  
COUNT\_MULTI  
COUNT\_STAR  
CURRENT\_DATE  
CURRENT\_TIMESTAMP  
DATE\_ADD  
DATE\_DIFF  
DATE\_SUB  
DATE\_TRUNC  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_QUARTER  
DATE\_TRUNC\_WEEK  
DATE\_TRUNC\_YEAR  
DAYOFMONTH  
DAYOFWEEK  
DAYOFYEAR  
EXTRACT  
FLATTEN  
FLOOR  
ILIKE  
IN  
IS DISTINCT FROM  
IS NOT DISTINCT FROM  
IS NOT NULL  
IS NULL  
LAST\_DAY  
LCASE  
LEFT  
LENGTH  
LIKE  
LOCATE  
LOWER  
LPAD  
LTRIM  
MAX  
MEDIAN  
MIN  
MOD  
NEXT\_DAY  
NOT  
NVL  
PERCENTILE\_CONT  
PERCENTILE\_DISC  
PERCENT\_RANK  
POSITION  
REGEXP\_LIKE  
REPLACE  
REVERSE  
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
UCASE  
UPPER  
VAR\_POP  
VAR\_SAMP

## Related Information

[ZooKeeper](/current/what-is-dremio/architecture/)

Was this page helpful?

[Previous

Apache Druid](/current/data-sources/databases/apache-druid)[Next

Elasticsearch](/current/data-sources/databases/elasticsearch)

* Example
* User Impersonation
* Limitation
* Prerequisites
* Configuring Another Dremio Software Cluster as a Source
  + General Options
  + Advanced Options
  + Reflection Refresh Options
  + Metadata Options
  + Privileges
* Updating a Dremio Source
* Deleting a Dremio Source
* Predicate Pushdowns
* Related Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/google-bigquery

Version: current [26.x]

On this page

# Google BigQuery Enterprise

Dremio supports connecting to Google BigQuery as an external source. The connector uses Google service account keys for authentication. To learn more about creating and managing service account keys, see [Create and delete service account keys](https://cloud.google.com/iam/docs/keys-create-delete).

## Requirements

To connect to Google BigQuery, you need:

* Google BigQuery
* Source configuration for authentication

## User Impersonation

Dremio supports authentication using Google Workforce Identity Pool impersonation, which allows external identities to securely access BigQuery datasets without requiring a dedicated Google service account for each user.

note

Reflections are not supported on data sources with user impersonation enabled to ensure that all security and governance policies defined in the underlying data source are enforced.
Reflections created prior to enabling user impersonation must be manually dropped, as they will fail to refresh once impersonation is active.

### Prerequisites

Before configuring a Bigquery source with user impersonation, ensure you have:

* Access to a Google Cloud Organization
* An Organization Admin role (`roles/iam.organizationAdmin`) or Workforce Pool Admin role (`roles/iam.workforcePoolAdmin`) within that organization

### Configure Google Workforce Identity Pool

In the following steps, you will configure Google Cloud to recognize and verify assertions (signed JWTs) sent from Dremio. Google uses Dremio’s public key to validate the digital signatures of these assertions. Creating a Workforce Identity Pool establishes trust between Google Cloud and Dremio for OAuth-based authentication.

To allow federated identities from your Workforce Identity Pool to execute BigQuery jobs, you must assign the BigQuery Job User role (`roles/bigquery.jobUser`) at the project level. This allows federated users to submit and manage their own query and load jobs within the project.

To set up your Google Workforce Identity Pool:

1. Run the following command to create a Workforce Identity Pool, replacing `<your-organization-id>` with your Google Cloud Organization ID:

   Create a Workforce Identity Pool

   ```
   gcloud iam workforce-pools create my-org-workforce-pool \  
        --organization=organizations/<your-organization-id> \  
        --display-name="My Organization Workforce Pool" \  
        --description="Workforce Identity Pool for my organization"
   ```

   Note the value of `my-org-workforce-pool` as this will be your `your-workforce-pool-id`.
2. Obtain Dremio’s public JWKS and Dremio’s issuer from the BigQuery source configuration in Dremio. Retrieve these values by performing one of the following:

   a. Click the Workforce Identity Federation button in the Dremio console.

   b. Run these API calls:

   1. Retrieve Dremio’s public JWKS by sending a GET request:

      Retrieve Dremio’s public JWKS

      ```
      /v3/external-oauth/discovery/jwks
      ```

      Save the response as `public_jwk_set.json`. This file contains Dremio’s public key set, which Google will use to verify signed JWTs.
   2. Retrieve Dremio’s issuer by sending a GET request:

      Retrieve Dremio’s issuer

      ```
      /v3/external-oauth/discovery/jwt-issuer
      ```

      Note the issuer value returned. You’ll need it when configuring Google Cloud to establish the trust relationship.
3. Run following bash command, replacing `<Dremio_issuer_value>` with the value obtained in the previous step:

   Create a Workforce identity provider

   ```
   gcloud iam workforce-pools providers create-oidc my-workforce-provider \  
         --workforce-pool=my-org-workforce-pool \  
         --display-name='My Dremio Provider' \  
         --description='Dremio Provider for BQ impersonation' \  
         --issuer-uri='<Dremio_issuer_value>' \  
         --client-id='dremio-bq-client-id' \  
         --web-sso-response-type="id-token" \  
         --web-sso-assertion-claims-behavior="only-id-token-claims" \  
         --attribute-mapping="google.subject=assertion.sub" \  
         --jwk-json-path=./public_jwk_set.json \  
         --detailed-audit-logging \  
         --location=global \  
         --organization=organizations/`<your-organization-id>`
   ```

   | Parameter | Description |
   | --- | --- |
   | `my-workforce-provider` | The ID you assign to your Workforce identity provider. Note this value for future reference as `<your-workforce-provider-id>`. |
   | `workforce-pool=my-org-workforce-pool` | Specifies the Workforce Identity Pool this provider belong to. |
   | `display-name='My Dremio Provider'` | A human-readable name for the provider, as it appears in the Google Cloud Console. |
   | `description='Dremio Provider for BQ impersonation'` | A short description of the provider’s purpose, for example, used for Dremio ↔ BigQuery impersonation. |
   | `issuer-uri='https://internal-issuer.dremio.com'` | The issuer (iss) claim expected in the JWT signed by Dremio. This should uniquely identify your Dremio instance or the asserting entity. It doesn’t need to be publicly resolvable, but it must be consistent. |
   | `client-id='dremio-bq-client-id'` | The aud (audience) claim that Google expects in the JWT. For this workflow, this typically represent the Dremio client or the Google resource. |
   | `web-sso-response-type="id-token"` | Specifies the OIDC response type for SSO flows. "id-token" means the Dremio returns an ID token directly. |
   | `web-sso-assertion-claims-behavior="only-id-token-claims"` | Controls which claims are included in the assertion. "only-id-token-claims" limits it to claims present in the ID token. |
   | `attribute-mapping="google.subject=assertion.sub"` | Maps the sub (subject) claim from Dremio’s JWT to the google.subject attribute (required). |
   | `jwk-json-path=./public_jwk_set.json` | Path to Dremio’s public JWK file. Google uses this to verify Dremio’s JWT signatures. |
   | `detailed-audit-logging` | Enables detailed logging in Cloud Logging — recommended for troubleshooting. |
   | `location=global` | Sets the Workforce Identity Pool resource location (typically global). |
   | `organization=organizations/<your-organization-id>` | Specifies your Google Cloud Organization ID. |
4. Run the following command to grant IAM policy binding for BigQuery job execution, replacing `<project-id>` with the Google Cloud project where your BigQuery data resides:

   Grant IAM policy binding for BigQuery job execution

   ```
   gcloud projects add-iam-policy-binding <project-id> \  
        --role="roles/bigquery.jobUser" \  
        --member='principalSet://iam.googleapis.com/locations/global/workforcePools/my-org-workforce-pool/*'
   ```

   If you are using Google Groups mapping, replace `<your-gcp-access-group>` with the mapped group name (for example, "BigQueryUsers"):

   Grant IAM policy binding for BigQuery job execution with Google groups mapping

   ```
   gcloud projects add-iam-policy-binding <project-id> \  
         --role="roles/bigquery.jobUser" \  
         --member="principalSet://iam.googleapis.com/locations/global/workforcePools/my-org-workforce-pool/group/your-gcp-access-group"
   ```

## Dremio Configuration

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select the source.

   The new source dialog box appears, which contains the following tabs:

   * **General**: Create a name for your database, specify the connection details, and set the authentication.
   * **Advanced Options**: (Optional) Set the advanced configuration options for your database.
   * **Reflection Refresh**: (Optional) Set a policy to control how often Reflections are refreshed and expired.
   * **Metadata**: (Optional) Specify dataset handling and metadata refresh.
   * **Privileges**: (Optional) Add privileges for users or roles.

   Refer to the following sections for guidance on how to edit each tab.

### General

To configure the source connection:

1. For **Name**, enter the name to identify the database in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

2. For **Host**, enter the hostname or IP address for the Google BigQuery source.
3. For **Port**, enter the Google BigQuery port number. The default port is `443`.
4. For **Project ID**, specify the Google Cloud Project ID that contains your BigQuery datasets (for example, `<your-bigquery-project-id>`).
5. For **Authentication**, choose between **Service Account** or **Workforce Identity Federation**.

   a. If you choose **Service Account**, complete the following:

   1. For **Client Email**, enter the client email.
   2. For **Service Account Key**, choose an authentication method:

      * **Dremio**: Provide the database password in plain text. Dremio stores the password.
      * **Azure Key Vault**: Provide the URI for the Azure Key Vault secret that stores the Vertica password. The URI format is `https://<vault_name>.vault.azure.net/secrets/<secret_name>` (for example, <https://myvault.vault.azure.net/secrets/mysecret>).

        note

        To use Azure Key Vault as your application secret store, you must:
        Deploy Dremio on Azure.
        Complete the Requirements for Authenticating with Azure Key Vault.
        It is not necessary to restart the Dremio coordinator when you rotate secrets stored in Azure Key Vault. Read Requirements for Secrets Rotation for more information.
      * **AWS Secrets Manager**: Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS console or command line tools.
      * **HashiCorp Vault**: Choose the HashiCorp secrets engine you're using from the dropdown menu and enter the secret reference for the password in the correct format in the provided field.

   b. If you choose **Workforce Identity Federation**, complete the following:

   1. For **Default User**, enter the default user identifier that Dremio will use to fetch metadata and execute reflection jobs. This user must have sufficient privileges to perform these operations. Example: [dremio-svc-user@yourcompany.com](mailto:dremio-svc-user@yourcompany.com)
   2. For **Audience**, enter the client identifier used by Dremio during authentication (e.g., `value: dremio-bq-client-id`). This must exactly match the `--client-id` from Step 2 of prerequisites setup.
   3. For **Client ID**, enter the client identifier used by Dremio during authentication (e.g., `value: dremio-bq-client-id`). This must exactly match the `--client-id` from Step 2 of the prerequisites setup. In this configuration, the client ID and audience values are the same.

note

Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### Advanced Options

Set the advanced configuration options for your database:

* **Record fetch size**: Number of records to fetch at once. Set to `0` to have Dremio automatically decide. By default, this is set to `10`.
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to `8`.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to `60`.
* **Query timeout (s)**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Enable external authorization plugin**: When enabled, authorizes an external plugin.
* **Connection Properties**: Connection properties and values for the data source.

### Reflection Refresh

Set the policy that controls how often Reflections are refreshed or expired, using the following options:

* **Never refresh**: Select to prevent automatic Reflection refresh; otherwise, the default is to refresh automatically.
* **Refresh every**: How often to refresh Reflections, specified in hours, days or weeks. This option is ignored if **Never refresh** is selected.
* **Set refresh schedule**: Specify the daily or weekly schedule.
* **Never expire**: Select to prevent Reflections from expiring; otherwise, the default is to expire automatically after the time limit specified in **Expire after**.
* **Expire after**: The time limit after which Reflections expire and are removed from Dremio, specified in hours, days or weeks. This option is ignored if **Never expire** is selected.

### Metadata

Set the following metadata options:

* **Remove dataset definitions if underlying data is unavailable**: Checked by default. If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.
* **Data Discovery**: Set the time interval for fetching top-level source object names such as databases and tables. You can choose to set the **Fetch every** frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour.
* **Dataset Details**: The metadata that Dremio needs for query planning such as information needed for fields, types, shards, statistics, and locality. Use these parameters to fetch or expire the metadata:

  + **Fetch mode**: Fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**.
  + **Fetch every**: Set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour.
  + **Expire after**: Set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours.

### Privileges

To grant privileges to specific users or roles:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

See [Access Control](/current/security/rbac/) for additional information about privileges.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

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

## Data Source Management

### Updating the Source

To update the source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the dropdown.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name.
4. Click **Save**.

### Deleting the Source

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the `ADMIN` role can delete the source.

To delete the source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and click ![The Settings icon](/images/settings-icon.png "The Settings icon") to the right.
3. From the dropdown, select **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

* Deleting a source causes all downstream views that depend on objects in the source to break.
* Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Querying the Google BigQuery Source Directly

Dremio users can run pass queries through Dremio to run on your database. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

Was this page helpful?

[Previous

Elasticsearch](/current/data-sources/databases/elasticsearch)[Next

IBM Db2](/current/data-sources/databases/ibm-db2)

* Requirements
* User Impersonation
  + Prerequisites
  + Configure Google Workforce Identity Pool
* Dremio Configuration
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Predicate Pushdowns
* Data Source Management
  + Updating the Source
  + Deleting the Source
* Querying the Google BigQuery Source Directly

---

# Source: https://docs.dremio.com/current/data-sources/databases/elasticsearch

Version: current [26.x]

On this page

# Elasticsearch

This topic describes how to configure Elasticsearch as a source in Dremio.

note

If your organization upgrades to Elasticsearch v7.0+, you will need to remove and re-add it as a source in Dremio.

### Compatibility

Supported Versions:

* Elasticsearch versions 7.x, 8.x, and 9.x (8.x and 9.x in version 7 compatibility mode)
* Dremio Software only
* Pushdown Scripting Support: Painless

### Metadata Concepts

In order to plan and execute queries, Dremio captures and stores Elastic metadata in Dremio’s internal metadata database to efficiently plan and execute queries. This captured metadata is broken into two broad categories:

* **Dataset Discovery**: Names of available Indices, Mappings and Aliases.
  This information is required to expose databases and tables in the Dremio UI and BI tool
  connections.
* **Dataset Details**: Complete information including definition of mapping,
  sampled schema and shard locations. This information is required to complete a
  query against a particular table.

Dremio will interact with the `/_cluster/state/metadata` api to understand the nature of the objects inside your Elasticsearch install. From this API endpoint, Dremio can learn metadata about each of these object type. By default, Dataset Discovery has an hourly refresh interval. Additionally, Dataset Details has an hourly refresh interval for Elastic tables that have been queried at least once.

### Accessing Objects

The Dremio Elastic Connector is designed to provide a consistent and understandable
view of Elastic Indices and Mappings, through the use of a two level hierarchy.
In Dremio, these two levels can be thought of as database and table.
Elastic Indices and Aliases are exposed as databases and each mapping within those index
or alias is exposed as a table.

Dremio also supports exposing data inside Elastic aliases.
In Dremio, aliases and indices are not visually distinguished and a user can easily interact
with either entity. Additionally, Dremio understands filtered aliases and
will correctly apply those filters as part of its operations.

Dremio also allows users access to Elastic’s capability to expose synthetic tables through wildcards and comma separated lists. A user can use wildcards in both the name of the database (index) or the name of the table (mapping). This is done by modifying the from clause in a standard SQL query. Once that query is executed, if Elastic recognizes the name, those entities will show up in the product as additional datasets available for query and access (and will be maintained and secured like any other table). If you want to have Dremio forget about those entities, an administrator can use `ALTER TABLE <TABLE> FORGET METADATA` to remove those synthetic entities.

Access objects examples

```
SELECT * from elastic."feb*"."big"  
SELECT * from elastic."feb,march"."big"  
SELECT * from elastic."feb"."big,small"
```

### Execution Metadata

When Dremio executes queries against Elastic, it usually parallelizes the query to interact with each shard in your Elastic cluster to move data as quickly as possible back to Dremio. Dremio does this by probing the `/<indexOrAlias>/_search_shards` API.

### List Promotion Rules

Elastic does not distinguish between scalar and list of scalars but Dremio does.
In order to ensure the best possible user experience,
Dremio uses the schema analysis phases outlined above to expose the final user schema.
To simplify things, once Dremio detects at least one field with a list of scalars,
it exposes all records for that field as a list of scalars.
This allows users to avoid having to deal with union types. An example:

* Elastic mapping is defined as field ‘A’ and type integer.
* Records 1-4 exist and each have a single integer for field ‘A’.
* Dremio samples the schema and exposes field ‘A’ as a scalar.
* Record five is inserted into the index
* Dremio now exposes field 'A' as an `int[]` for all records 1-5.

Dremio does this promotion both at initial sampling time and during execution.
If during execution Dremio discovers a value for a field that is of scalar type is actually
a list type, Dremio will learn this schema and re-execute the query.

### Special Handling for Geoshape

Geoshape is a special type in the Elastic ecosystem.
This is because has a different schema depending on which type is exposed.
Despite this, they are all represented at the type system level as a single type.
In this situation, Dremio exposes the Geoshape type and specifically its potential
coordinates fields as a group of union fields supporting from 1 to 4-dimensional double arrays
to reflect the various types of Elastic geoshapes.

### Mapping Consistency and Schema Learning

In some cases, it is possible that Dremio will query an index and find a schema change that was previously unknown to Dremio (different type for field or new field). In both cases, Dremio will do a two step verification process to correctly learn the new schema. Dremio maintains a mapping checksum for all identified schemas. When it encounters an unexpected change, it will first verify that the canonical schema from Elastic is consistent with Dremio’s previously known mapping. If it is, Dremio will follow its standard promotion rules. If it is not, Dremio will halt execution and request the user to use the `ALTER TABLE <TABLE> REFRESH METADATA`  
operation to have Dremio immediately reread the updated Elastic mapping information. Note, this is an optional step as the mapping will also be updated on the schedule defined for automated metadata updates.

### Discovery of New Fields

As part of the Dataset Details refresh, Dremio will automatically reload all Elastic mappings to learn about any new fields. Each time this happens, Dremio will resample and update its understanding of schema.

### Mapping Merging

If you compose a query that includes multiple mappings, Dremio will do its best to merge those mappings. Mappings are merged on a field by field basis. Mappings can be merged if at least one of the following is true:

1. Fields with overlapping positions are the same type (`mapping1.a::int` and `mapping2.a::int`)
2. Fields are in non-overlapping positions (`mapping1.a::int` versus `mapping2.b::float`)

When Dremio merges a mapping, it does so linearly, inheriting the initial field order based on the first index queried.

### Elastic Pushdowns

Dremio supports multiple types of pushdowns for different Elastic version and configuration combinations including:

* Predicate (e.g. x < 5) pushdowns using Elastic queries
* Lucene search queries using the `CONTAINS` syntax (starting from 5.3.x)
* Optional source field/inclusion exclusion (disabled for performance reasons but can be enabled if Dremio has a slow connection to Elastic nodes).
* Group by pushdowns for grouping by strings, dates, times, timestamps, integer, longs, doubles, floats, booleans using the Elastic Term Aggregation capabilities
* Aggregate Measure pushdown including `COUNT`, `COUNT(DISTINCT)`, `SUM`, `AVG`, `STDDEV`, `VAR` using Elastic aggregation framework.
* Support for converting many arbitrary expressions and ~50 common functions through the use of Groovy (ES2) or Painless (ES5+) scripts for use in both filter and aggregate expressions.

### Expression and Function Pushdowns

Dremio supports pushing down the following expressions and functions:

| Type | Expression/Function |
| --- | --- |
| Comparison | Equals |
| Comparison | Not equals |
| Comparison | Greater than |
| Comparison | Greater or equal to |
| Comparison | Less than |
| Comparison | Less or equal to |
| Comparison | LIKE |
| Comparison | ILIKE |
| Boolean | NOT |
| Boolean | OR |
| Boolean | AND |
| NULL Check | IS NULL |
| NULL Check | IS NOT NULL |
| Flow | CASE |
| Type Conversion | CAST |
| String | CHAR LENGTH |
| String | UPPER |
| String | LOWER |
| String | TRIM |
| String | CONCAT |
| Numeric | Add |
| Numeric | Subtract |
| Numeric | Multiply |
| Numeric | Divide |
| Numeric | POWER |
| Numeric | MOD |
| Numeric | ABS |
| Numeric | EXP |
| Numeric | FLOOR |
| Numeric | CEIL |
| Numeric | LOG |
| Numeric | LOG10 |
| Numeric | SQRT |
| Numeric | SIGN |
| Numeric | COT |
| Numeric | ACOS |
| Numeric | ASIN |
| Numeric | ATAN |
| Numeric | DEGREES |
| Numeric | RADIANS |
| Numeric | SIN |
| Numeric | COS |
| Numeric | TAN |

### How Dremio Decides What To Pushdown

Dremio works hard to pushdown as many operations as possible to Elastic to try to provide the highest performance experience. Dremio is also focused on maintaining a consistent SQL experience for users who may not understand Elastic or its APIs. As such, Dremio is very focused on providing a correct SQL experience. This includes respecting null semantics through the use of missing aggregation, expression evaluation consistency, correct aggregation semantics on analyzed fields, etc. Dremio also works well with Groovy and Painless to pushdown many more types of operations. It will work without scripts enabled but it is strongly recommended to enable scripts.

Given the nature of Elastic’s API, Dremio utilizes the following pieces of functionality to provide a SQL experience: Bucket Aggregations, Pipeline Aggregations, Filter Aggregations and searches using Elastic Query DSL.

### Script Construction

Dremio builds custom Groovy (ES2) or Painless (ES5) scripts to interact with Elastic. Because of the many small differences in these languages (type handling, dynamic dispatch, type coercion, function signatures, primitive handling, etc), these scripts are different for each version of Elasticsearch. These scripts utilize Elastic’s doc values columnar capability where possible but also rely on `_source` fields for certain operations (e.g. aggregations on analyzed fields for example). As Dremio analyzes a user’s SQL expression, it decomposes the expression into a script that can be understood by Elastic’s scripting capability.

There are many situations where Dremio uses an expression that might at first be unexpected. These are because of the nature of some of Elastic apis. Some examples behaviors that Dremio does to ensure correct results:

* Dremio uses \_source fields for accessing IP addresses when aggregating or filtering in ES2 because the type has changed between ES2 and ES5
* Dremio doesn’t push down multi-index complex expressions (`table1.a[2].b[3].c[4]`) using `doc` values because doc values can only reference leaf fields and leaf arrays
* Dremio doesn’t do any array dereferencing using `_source` fields because they are not canonicalized to the Elastic mapping. This means that nested arrays `[1,[2,3]]` haven’t been flattened to the Elastic canonical representation `[1,2,3]`. This is done as otherwise scripts would produce wrong result.
* Dremio won’t use a doc field reference for a field that has it implicitly disabled (`string/text`) or explicitly disabled (`doc_values: false`).
* Dremio won’t use `doc` fields for GeoShapes. This is because Dremio doesn’t expose a first class shape objects and the fields exposed in Dremio (lists of arrays of doubles) are not directly related to Elastic’s internal representation or query capabilities.
* Dremio won’t pushdown operations against nested fields. This is because nested fields are stored out of line of the core document (not in the original document’s doc values) and have semantics inconsistent with traditional SQL aggregation. (Dremio is exploring future work to expose this through enhancements to the language.) Note that Dremio also doesn’t use `_source` field scripts to interact with nested documents because they are exposed as arrays of values and suffer from the canonicalization issue described above.

### Debugging and Logging

If you want to better understand how Dremio is interacting with your Elastic cluster, you can enable Dremio Elastic logging on each Dremio node. This will record each response and request to the Elastic cluster, including a portion of each message body.

You can do this by adding the following configuration to your `conf/logback.xml` file on all nodes:

Configuration for conf/logback.xml file

```
  <appender name="elasticoutput" class="ch.qos.logback.core.rolling.RollingFileAppender">  
    <file>${dremio.log.path}/elastic.log</file>  
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">  
      <fileNamePattern>${dremio.log.path}/archive/elastic.%d{yyyy-MM-dd}.log.gz  
      </fileNamePattern>  
      <maxHistory>30</maxHistory>  
    </rollingPolicy>  
    <encoder>  
      <pattern>%date{ISO8601} [%thread] %-5level %logger{36} - %msg%n  
      </pattern>  
    </encoder>  
  </appender>  
  <logger name="elastic.requests" additivity="false">  
    <level value="info"/>  
    <appender-ref ref="elasticoutput"/>  
  </logger>
```

### Working with Elasticsearch and x-pack

If your Elasticsearch source uses Shield, then your Elasticsearch user account must have the
'monitor' privilege at the cluster level (an admin user has this by default).
In addition, for each index you want to query upon, your user account need to have the
'read' and 'view\_index\_metadata' privilleges as well. Both privilleges are included in 'all'.

The following is an example to set up a role 'dremio' with necessary privilleges to access
'test\_schema\_1' index:

Grant privileges to 'dremio' role

```
POST /_xpack/security/role/dremio  
  
{  
  "cluster": [ "monitor" ],  
  "indices": [  
    {  
      "names": [ "test_schema_1" ],  
      "privileges": [ "read", "view_index_metadata" ]  
    }  
  ]  
}
```

### Working with Elasticsearch and Shield

If your Elasticsearch source uses Shield, then your Elasticsearch user account must have the 'monitor' privilege at the cluster level (an admin user has this by default). If your account lacks the 'monitor' privilege, and you don't have access to an admin user, you can create a new account with 'monitor' by following these steps:

* Log in to a search node, go the Elasticsearch install's home directory, and open the file ./config/shield located inside.
* Append this text, which gives monitor privileges to an Elasticsearch index called `books` for any user with the `dremio_user` role:

  Text to append to ./config/shield file

  ```
  dremio_user:  
  cluster:  
  - cluster:monitor/nodes/info  
  - cluster:monitor/state  
  - cluster:monitor/health  
  indices:  
  'books' :  
  - read  
  - indices:monitor/stats  
  - indices:admin/get  
  - indices:admin/mappings/get  
  - indices:admin/shards/search_shards
  ```
* Run this command, adding a new user to Shield that has the 'dremio\_user' role:

  Add new user to Shield

  ```
  ./bin/shield/esusers useradd <username> -r dremio_user
  ```
* Copy the Shield config file you edited to every other node in the Elasticsearch cluster:

  Copy Shield config file to other nodes

  ```
  scp -r ./config/shield root@<other-es-node>:<elastic-install-dir>/config
  ```

## Configuring Elasticsearch as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Elasticsearch**.

### General

**Name**

Specify the name you want to use for the Elasticsearch data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

**Connection**

* Host: Provide the name of the host to use to connect to the Elasticsearch data source.
* Port: Provide the port to use with the specified hostname to connect to the Elasticsearch data source (default is `9200`).
* Encrypt connection: Select or deselect the checkbox to specify whether Dremio should encrypt the connection to the Elasticsearch data source.
* Managed Elasticsearch service: Select the checkbox if you are connecting to a managed Elasticsearch instance or Dremio only has access to the specified host.

**Authentication**

* No Authentication
* Master Credentials (default):
  + Username: Elasticsearch username
  + Password: Select the password store from the dropdown menu:
    - Dremio: Provide the password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.

### Advanced Options

Select or deselect the checkboxes to configure settings for the following options:

* Show hidden indices that start with a dot (.)
* Use Painless scripting with Elasticsearch 5.0+ (experimental)
* Show \_id columns
* Use index/doc fields when pushing down aggregates and filters on analyzed and normalized fields (may produce unexpected results)
* Perform keyword searches when pushing down fields mapped as text and keyword
* Use scripts for query pushdown
* If the number of records returned from Elasticsearch is less than the expected number, warn instead of failing the query
* Force Double Precision

Specify the desired settings for the following options:

* Read timeout (seconds)
* Scroll timeout (seconds)
* Scroll size: Setting must be less than or equal to your Elasticsearch setting for `index.max_result_window`, which typically defaults to 10,000.

Under **Encryption**, choose a Validation Mode option:

* Validate certificate and hostname
* Validate certificate only
* Do not validate certificate or hostname

### Reflection Refresh

* **Refresh Settings**: Select whether to never refresh Reflections; refresh at an interval based on hours, days, or weeks; or refresh at the specified schedule.
* **Expire Settings**: Select whether Reflections should never expire or expire at an interval based on hours, days, or weeks.

### Metadata

Under **Dataset Handling**, select or deselect the checkbox to specify whether Dremio should remove dataset definitions if underlying data is unavailable.

Under **Metadata Refresh**:

* Dataset Discovery: Specify the refresh interval to use for the names of top-level source objects such as tables.
* Dataset Details: Specify refresh and expiration intervals for the metadata Dremio needs for query planning, such as information on fields, types, shards, statistics and locality.

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an Elasticsearch Source

To update an Elasticsearch source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Elasticsearch as a Source.
4. Click **Save**.

## Deleting an Elasticsearch Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Elasticsearch source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## For More Information

* See [Elasticsearch Data Types](/current/reference/sql/data-types/mappings/elasticsearch/)
  for information about mapping to Dremio data types.

Was this page helpful?

[Previous

Dremio Cluster](/current/data-sources/databases/dremio)[Next

Google BigQuery](/current/data-sources/databases/google-bigquery)

* Compatibility
* Metadata Concepts
* Accessing Objects
* Execution Metadata
* List Promotion Rules
* Special Handling for Geoshape
* Mapping Consistency and Schema Learning
* Discovery of New Fields
* Mapping Merging
* Elastic Pushdowns
* Expression and Function Pushdowns
* How Dremio Decides What To Pushdown
* Script Construction
* Debugging and Logging
* Working with Elasticsearch and x-pack
* Working with Elasticsearch and Shield
* Configuring Elasticsearch as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating an Elasticsearch Source
* Deleting an Elasticsearch Source
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/ibm-db2

Version: current [26.x]

On this page

# IBM Db2

You can add Db2 databases as sources to Dremio.

See [IBM Db2 Data Types](/current/reference/sql/data-types/mappings/db2/) for information about mapping to Dremio data types.

## Limitations

Only IBM Db2 for Linux, UNIX, and Windows is supported.

## Configuring IBM Db2 as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **IBM Db2**.

### General Options

1. In the **Name** field, specify the name by which you want the Db2 source to appear in the **Databases** section. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, follow these steps:
   1. In the **Host** field, specify the hostname or IP address of the database to connect to.
   2. In the **Port** field, specify the port to use when connecting. The default is 50000.
   3. In the **Database** field, specify the name of the database.
3. Under **Authentication**, specify the Db2 username. Then, choose a method for providing the Db2 password from the dropdown menu:
   * Dremio: Provide the password in plain text. Dremio stores the password.
   * [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
   * [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
   * [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.

### Advanced Options

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |

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

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an IBM Db2 Source

To update an IBM Db2 source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring IBM Db2 as a Source.
4. Click **Save**.

## Deleting an IBM Db2 Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an IBM Db2 source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

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

## Running Queries Directly on IBM Db2 Through Dremio

Dremio users can run pass queries through Dremio to run on IBM Db2. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

Was this page helpful?

[Previous

Google BigQuery](/current/data-sources/databases/google-bigquery)[Next

Microsoft Azure Data Explorer](/current/data-sources/databases/azure-data-explorer)

* Limitations
* Configuring IBM Db2 as a Source
  + General Options
  + Advanced Options
  + Reflection Refresh Options
  + Metadata Options
  + Privileges
* Updating an IBM Db2 Source
* Deleting an IBM Db2 Source
* Predicate Pushdowns
* Running Queries Directly on IBM Db2 Through Dremio

---

# Source: https://docs.dremio.com/current/data-sources/databases/azure-data-explorer

Version: current [26.x]

On this page

# Microsoft Azure Data Explorer

You can add a source to Dremio that is a database in [Azure Data Explorer (ADX)](https://docs.microsoft.com/en-us/azure/data-explorer/data-explorer-overview).

## Prerequisites

* Ensure that you have the URI for connecting to the ADX cluster in which the database is located.
* Ensure that you know the name of the database that you want to add as a source.

## Configuring Azure Data Explorer as a Source

To add a database that is in an ADX cluster as a source in Dremio:

1. Click the Settings icon in the left navigation bar and select **Support**.
2. In the **Support Keys** section of the Support Settings page, add the support key `plugins.jdbc.adx.enabled`and toggle it on.
3. Navigate to the Datasets page. To the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
4. In the Add Data Source dialog, under **Databases**, select **Microsoft Azure Data Explorer**.

### General

Under **Name**, enter the name to use for the Azure Data Explorer source. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

Describe the Data Explorer cluster used in this connection.

* **Cluster URI**: Enter the cluster URI.
* **Tenant ID**: Enter the directory (tenant) ID.

#### Authentication

Select an authentication option:

* **Microsoft Entra ID**: To register a Microsoft Entra ID application and obtain the required IDs and client secret, see [How to register an app in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app), then complete the Dremio configuration:

  + **Application ID**: Enter the application (client) ID
  + **Application Secret**: Select the application secret store from the dropdown menu:
    - Dremio: Provide the application secret in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the application secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the secret reference in the required format.
* **Azure Managed Identity**: Passwordless authentication using Azure's managed identity service, eliminating credential management overhead.

  1. Create a [managed identity](https://learn.microsoft.com/en-us/azure/data-explorer/configure-managed-identities-cluster?tabs=portal), system-assigned or user-assigned for your Data Explorer cluster.
  2. Attach the managed identity to your Dremio AKS cluster's [Virtual Machine Scale Set (VMSS)](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-configure-managed-identities-scale-sets?pivots=identity-mi-methods-azp)
  3. Configure the Dremio source:
     + When using a user-assigned managed identity, add the **Client ID** to the Dremio source configuration.
     + When using a system-assigned managed identity, leave the **Client ID** blank.
* Under **Database Name**, enter the name of the database that you want to add as a source. Names are case-sensitive.

### Advanced Options

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |

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

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating an ADX Source

To update an ADX source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Azure Data Explorer as a Source.
4. Click **Save**.

## Deleting an ADX Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an ADX source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the ADX source and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Query Pushdowns

Dremio can delegate the execution of these expressions and functions to the database being queried, often dramatically improving query performance.

`-`, `=`, `+`, `*`, `/`  
`<`, `<=`, `<>`, `>=`, `>`, `!=`  
ADD\_MONTHS  
AND, LIKE, NOT, OR, ||  
AVG  
CAST  
CONCAT  
COUNT \*  
COUNT DISTINCT  
COUNT DISTINCT MULTI  
COUNT MULTI  
DATE\_ADD  
DATE\_SUB  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_YEAR  
FULL JOIN  
INNER JOIN  
IS DISTINCT FROM  
IS NOT DISTINCT FROM  
IS NOT NULL  
IS NULL  
JOIN  
LAST\_DAY  
LEFT JOIN  
MAX  
MIN  
MOD  
RIGHT JOIN  
SIGN  
SORT  
SUM

## Running Queries Directly on Azure Data Explorer Through Dremio

Dremio users can run pass queries through Dremio to run on Azure Data Explorer. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

Was this page helpful?

[Previous

IBM Db2](/current/data-sources/databases/ibm-db2)[Next

Microsoft Azure Synapse Analytics](/current/data-sources/databases/azure-synapse-analytics)

* Prerequisites
* Configuring Azure Data Explorer as a Source
  + General
  + Advanced Options
  + Reflection Refresh Options
  + Metadata Options
  + Privileges
* Updating an ADX Source
* Deleting an ADX Source
* Query Pushdowns
* Running Queries Directly on Azure Data Explorer Through Dremio

---

# Source: https://docs.dremio.com/current/data-sources/databases/azure-synapse-analytics

Version: current [26.x]

On this page

# Microsoft Azure Synapse Analytics

Dremio supports integrations with organizations using Azure Synapse Analytics dedicated SQL pools via the external source.

## Requirements

* [Dremio v19.3+](/current/release-notes/version-1900-release-notes/#1930-release-notes-january-2022)

## Configuring Synapse Analytics as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Microsoft Azure Synapse Analytics**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

Describe the Synapse Analytics SQL Server workspace used in this connection.

* Under **Host**, enter the URL for your dedicated SQL pool, which typically ends in `.sql.azuresynapse.net`.
* Under **Port (optional)**, enter the port required to access the data source.
* Under **Database**, enter the database's name. Only this database is accessed by Dremio.

#### Authentication

Select an authentication option:

* **No Authentication**: Dremio does not attempt to provide any authentication when connecting with the SQL pool.
* **Master Credentials**: Dremio must provide a specified username and password in order to access the SQL pool.
  + Username: Enter the Microsoft Azure Synapse Analytics username.
  + Password: Select the password store from the dropdown menu:
    - Dremio: Provide the Microsoft Azure Synapse Analytics password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the Microsoft SQL Server password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.
* **Microsoft Entra ID**: To register a Microsoft Entra ID application and obtain the required IDs and client secret, see [How to register an app in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app), then complete the Dremio configuration:
  + **Tenant ID**: Unique identifier of your Microsoft Entra ID tenant.
  + **Application ID**: Enter the application (client) ID
  + **Application Secret**: Select the application secret store from the dropdown menu:
    - Dremio: Provide the application secret in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the application secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the secret reference in the required format.
* **Azure Managed Identity**: Passwordless authentication using Azure's managed identity service, eliminating credential management overhead.
  1. Create a [managed identity](https://learn.microsoft.com/en-us/azure/synapse-analytics/synapse-service-identity), system-assigned or user-assigned for your Synapse workspace.
  2. Attach the managed identity to your Dremio AKS cluster's [Virtual Machine Scale Set (VMSS)](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-configure-managed-identities-scale-sets?pivots=identity-mi-methods-azp)
  3. Configure the Dremio source:
     + When using a user-assigned managed identity, add the **Client ID** to the Dremio source configuration.
     + When using a system-assigned managed identity, leave the **Client ID** blank.

Select the **Encrypt connection** option to encrypt the connection to Microsoft Azure Synapse Analytics. Clear the checkbox to disable encryption.

### Advanced Options

The following settings control more advanced functionalities in Dremio.

* **Advanced Options**
  + **Show only the initial database used for connecting -** This restricts Dremio's access only to a default database as specified on the **General** table.
  + **Record fetch size -** Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. The default value is `10`.
  + **Maximum idle connections -** The maximum number of idle connections to keep.
  + **Connection idle time (s) -** Idle time, in seconds, before a connection is considered for closure.
  + **Query timeout (s) -** The timeout, in seconds, for query execution before it is canceled. Set to `0` for no timeout.
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

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Microsoft Azure Synapse Analytics Source

To update a Microsoft Azure Synapse Analytics source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Microsoft Azure Synapse Analytics as a Source.
4. Click **Save**.

## Deleting a Microsoft Azure Synapse Analytics Source

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

## Running Queries Directly on Azure Synapse Analytics Through Dremio

Dremio users can pass queries through Dremio to run on Azure Synapse Analytics. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

Was this page helpful?

[Previous

Microsoft Azure Data Explorer](/current/data-sources/databases/azure-data-explorer)[Next

Microsoft SQL Server](/current/data-sources/databases/sql-server)

* Requirements
* Configuring Synapse Analytics as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Microsoft Azure Synapse Analytics Source
* Deleting a Microsoft Azure Synapse Analytics Source
* Predicate Pushdowns
* Running Queries Directly on Azure Synapse Analytics Through Dremio

---

# Source: https://docs.dremio.com/current/data-sources/databases/sql-server

Version: current [26.x]

On this page

# Microsoft SQL Server

This topic provides Microsoft SQL Server data source setup and configuration information.

## Supported Versions

Dremio supports Microsoft SQL Server 2012 and later.

note

Ensure that your Dremio cluster has access to the appropriate port for your Microsoft SQL Server source. By default, this is port 1433.

## Initial Connection

Depending on the number of tables in your SQL Server source, the final step of adding it to Dremio can take anywhere
from a few seconds to a few minutes as the source's metadata is processed.
However, this is a one-time cost and further queries to the source will not incur additional metadata reads.

## User Impersonation

The Microsoft SQL Server username provided in the source configuration is the default username that is used for running queries. When queries are run against Microsoft SQL Server in Dremio, users use the privileges associated with the Microsoft SQL Server username and run queries under that username.

You can change this default in Dremio by enabling user impersonation in the Advanced Options, which allows users to run queries under their own usernames and restricts their access. For example, `user_1` can run queries as `user_1` rather than `sqlsvr_svc`. Before enabling user impersonation, some setup is required in Microsoft SQL Server to allow one user to impersonate another user because the username of the user in Dremio must be the same as their username in Microsoft SQL Server and the user must be able to connect through the Microsoft SQL Server username.

note

Reflections are not supported on data sources with user impersonation enabled to ensure that all security and governance policies defined in the underlying data source are enforced.
Reflections created prior to enabling user impersonation must be manually dropped, as they will fail to refresh once impersonation is active.

To set up user impersonation, follow these steps:

1. Ensure the user's username in Microsoft SQL Server matches their username in Dremio. If the usernames do not match, modify one of the usernames or create a new user account with a matching username.
2. Run a GRANT IMPERSONATE command in Microsoft SQL Server to allow the user to connect through their Microsoft SQL Server username:

Example of granting impersonate privilege in Microsoft SQL Server

```
GRANT IMPERSONATE ON USER::testuser1 TO proxyuser;
```

In this example, the user can log in as `testuser1` in Dremio and in Microsoft SQL Server, and they can connect through the `proxyuser`. The `proxyuser` is the Microsoft SQL Server username provided in the source configuration.

3. Log in to Dremio as a member of the ADMIN role.
4. Follow the steps for Configuring Microsoft SQL Server as a Source using the Microsoft SQL Server username `proxyuser` and enable **User Impersonation** in the **Advanced Options**.
5. Grant [source privileges](/current/security/rbac/privileges#source-privileges) to the user.

Now that you have enabled user impersonation, a user who logs in to Dremio with their username can access the Microsoft SQL Server source and its datasets according to their privileges. The user can also run queries against Microsoft SQL Server under their username.

## Configuring Microsoft SQL Server as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Microsoft SQL Server**.

### General

#### Name

Enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

Describe the SQL Server instance used in this connection.

* **Host**: The SQL Server host name or IP address.
* **Port** (Optional): The SQL Server port number. If you do not specify a port number, the SQL Server instance is queried to retrieve the port that the named instance is listening on.
* **Database** (Optional): The database instance name

#### Authentication

Select an authentication option:

* **No Authentication**: Connects without credentials. Only use when the SQL Server allows anonymous connections or when network-level security controls access.
* **Master Credentials** (default):
  + **Username**: Enter the Microsoft SQL Server username
  + **Secret Store**: Select the password secret store from the dropdown menu:
    - Dremio: Provide the password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the secret reference in the required format.
* **Microsoft Entra ID**: To register a Microsoft Entra ID application and obtain the required IDs and client secret, see [How to register an app in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app), then complete the Dremio configuration:
  + **Tenant ID**: Enter the unique identifier of your Microsoft Entra ID tenant.
  + **Application ID**: Enter the application (client) ID
  + **Application Secret**: Select the application secret store from the dropdown menu:
    - Dremio: Provide the application secret in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the application secret, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the secret reference in the required format.
* **Azure Managed Identity** (Azure-hosted SQL Server): Passwordless authentication using Azure's managed identity service, eliminating credential management overhead.
  1. Create a [managed identity](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-azure-ad-user-assigned-managed-identity?view=azuresql), system-assigned or user-assigned for your SQL Server.
  2. Attach the managed identity to your Dremio AKS cluster's [Virtual Machine Scale Set (VMSS)](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-configure-managed-identities-scale-sets?pivots=identity-mi-methods-azp)
  3. Configure the Dremio source:
     + When using a user-assigned managed identity, add the **Client ID** to the Dremio source configuration.
     + When using a system-assigned managed identity, leave the **Client ID** blank.

Select the **Encrypt connection** option to encrypt the connection to Microsoft SQL Server. Clear the checkbox to disable encryption.

### Advanced Options

* **Show only the initial database used for connecting**:
  If selected, hides the other DBs that the credential has access to.
* **Record fetch size**: Number of records to fetch at once.
  Set to 0 (zero) to have Dremio automatically decide. Default: 10
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to *8*.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to *60*.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Enable legacy dialect**

### Reflection Refresh

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Microsoft SQL Server Source

To update a Microsoft SQL Server source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Microsoft SQL Server as a Source.
4. Click **Save**.

## Deleting a Microsoft SQL Server Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Microsoft SQL Server source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

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
MEDIAN  
MIN  
MOD  
MONTH  
PERCENT\_CONT  
PERCENT\_DISC  
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

note

Since Microsoft SQL Server has no Boolean type, project operations that contain SQL expressions which evaluate to true or false (e.g., `SELECT username, friends > 0`), and filter operations that include Boolean literals in a filter (e.g., `WHERE currentAccount = true`) cannot be executed as pushdowns.

## Running Queries Directly on SQL Server Through Dremio

Dremio users can pass queries through Dremio to run on SQL Server. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

## For More Information

* See [Microsoft SQL Server Data Types](/current/reference/sql/data-types/mappings/microsoft-sql-server/) for information about mapping to Dremio data types.

Was this page helpful?

[Previous

Microsoft Azure Synapse Analytics](/current/data-sources/databases/azure-synapse-analytics)[Next

MongoDB](/current/data-sources/databases/mongo)

* Supported Versions
* Initial Connection
* User Impersonation
* Configuring Microsoft SQL Server as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Microsoft SQL Server Source
* Deleting a Microsoft SQL Server Source
* Predicate Pushdowns
* Running Queries Directly on SQL Server Through Dremio
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/mongo

Version: current [26.x]

On this page

# MongoDB

## Requirements

To connect to MongoDB, you need:

* MongoDB (Dremio supports MongoDB 6.0+)
* Access to execute the [`dbStats`](https://www.mongodb.com/docs/manual/reference/command/dbStats/#mongodb-dbcommand-dbcmd.dbStats) command

## Limitation

DX-29932

Queries that un-nest nested fields are not allowed as they would cause incorrect schemas. This may be easily circumvented by pushing filters into the subquery or by simply not referencing the alias.

## Configuring MongoDB as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **MongoDB**.

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

* No Authentication
* Master Credentials (default):
  + Username: MongoDB username
  + Password: Select the password store from the dropdown menu:
    - Dremio: Provide the password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.
  + Authentication database: Provide the name of the database that Dremio should authenticate against.

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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a MongoDB Source

To update a MongoDB source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring MongoDB as a Source.
4. Click **Save**.

## Deleting a MongoDB Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a MongoDB source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

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

* See [MongoDB Data Types](/current/reference/sql/data-types/mappings/mongo/)
  for information about mapping to Dremio data types.

Was this page helpful?

[Previous

Microsoft SQL Server](/current/data-sources/databases/sql-server)[Next

MySQL](/current/data-sources/databases/mysql)

* Requirements
* Limitation
* Configuring MongoDB as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a MongoDB Source
* Deleting a MongoDB Source
* Predicate Pushdowns
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/mysql

Version: current [26.x]

On this page

# MySQL

**Supported Versions**

* MySQL versions that are 5.5.3 or higher

## Configuring MySQL as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **MySQL**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Host

| Name | Description |
| --- | --- |
| Host | MySQL host name. |
| Port | MySQL port number. Defaults to 3306. |

#### Authentication

* No Authentication
* Master Credentials (default):
  + Username: MySQL user name
  + Password secret store:
    - Dremio: Provide the password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Store the password securely using URI format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Choose the HashiCorp secrets engine you're using from the dropdown menu and enter the secret reference for the password in the correct format in the provided field.

### Advanced Options

![](/assets/images/mysql-adv-options-3887b0b6f7e688153ad2e281536b78ce.png) !

* **Net write timeout (in seconds)**: Seconds to wait for data from the server before aborting the connection. Default: 60
* **Record fetch size**: Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. Default: 10
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to *8*.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to *60*.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Connection Properties**: Connection properties and values for the data source. If you enable `require_secure_transport` in MySQL, you must add the connection properties `useSSL` and trustServerCertificate and set both to the value `true` to prevent errors.

### Reflection Refresh

![](/assets/images/hdfs-refresh-policy-9ae71114907887b859a9d01425390739.png) !

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

![](/assets/images/mongodb-metadataA-4215ce9cc791254ae9684171d87714d6.png) !

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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a MySQL Source

To update a MySQL source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring MySQL as a Source.
4. Click **Save**.

## Deleting a MySQL Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a MySQL source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

`*`, `+`, `-`, `/`, `%`  
`<`, `<=`, `<>`, `=`, `>`, `>=`, `!=`  
AND, NOT, NOT LIKE, OR, `||`  
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
CURRENT\_DATE  
CURRENT\_TIME  
CURRENT\_TIMESTAMP  
DATE\_ADD  
DATE\_SUB  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_DECADE  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_SECOND  
DATE\_TRUNC\_WEEK  
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
STDDEV  
STDDEV\_POP  
STDDEV\_SAMP  
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
VAR\_POP  
VAR\_SAMP

## Running Queries Directly on MySQL Through Dremio

Dremio users can run pass queries through Dremio to run on MySQL. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

## For More Information

* See [MySQL Data Types](/current/reference/sql/data-types/mappings/mysql/) for information about mapping to Dremio data types.

Was this page helpful?

[Previous

MongoDB](/current/data-sources/databases/mongo)[Next

Oracle](/current/data-sources/databases/oracle)

* Configuring MySQL as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a MySQL Source
* Deleting a MySQL Source
* Predicate Pushdowns
* Running Queries Directly on MySQL Through Dremio
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/oracle

Version: current [26.x]

On this page

# Oracle

This topic describes Oracle data source considerations and Dremio configuration.

## User Impersonation

The Oracle database username provided in the source configuration is the default username that is used for running queries. When queries are run against Oracle in Dremio, users use the privileges associated with the Oracle database username and run queries under that username.

You can change this default in Dremio by enabling user impersonation in the Advanced Options, which allows users to run queries under their own usernames and restricts their access. For example, `user_1` can run queries as `user_1` rather than `oracle_svc`. Before enabling user impersonation, some setup is required in Oracle to allow one user to impersonate another user, because the username of the user in Dremio must be the same as their username in Oracle and the user must be able to connect through the Oracle database username.

note

Reflections are not supported on data sources with user impersonation enabled to ensure that all security and governance policies defined in the underlying data source are enforced.
Reflections created prior to enabling user impersonation must be manually dropped, as they will fail to refresh once impersonation is active.

To set up user impersonation, follow these steps:

1. Ensure the user's username in Oracle matches their username in Dremio. If the usernames do not match, modify one of the usernames or create a new user account with a matching username.
2. Run a ALTER USER command in Oracle to allow the user to connect through the Oracle database username:

Example of altering the user in Oracle

```
ALTER USER testuser1 GRANT CONNECT THROUGH proxyuser;
```

In this example, the user can log in as `testuser1` in Dremio and in Oracle, and they can connect through the `proxyuser`. The `proxyuser` is the Oracle database username provided in the source configuration.

3. Log in as an admin to Dremio.
4. Follow the steps for Dremio Configuration using the Oracle database username and enable **User Impersonation** in the **Advanced Options**.
5. Grant [source privileges](/current/security/rbac/privileges#source-privileges) to the user.

Now that you have enabled user impersonation, a user logging in to Dremio with their username can access the Oracle source and its datasets according to their privileges. The user also runs queries against Oracle under their username.

## Connection Information

The following connection information is needed prior to adding Oracle as a data source.

* Hostname or IP
* Port
* Site Identifier (SID) of the Oracle server

note

Ensure that your Dremio cluster has access to the appropriate port for your Oracle source.
By default this is port 1521.

### Initial Connection

Depending on the number of tables in your Oracle source, the final step of adding it to Dremio can take anywhere from a few seconds to a few minutes as the source's metadata is processed. However, this is a one-time cost and further queries to the source will not incur additional metadata reads.

## Configuring Oracle as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Oracle**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Host

| Name | Description |
| --- | --- |
| Host | Oracle host name. |
| Port | Oracle port number. Defaults to 1521. |
| Service Name | Service Name of your database. |
| Encrypt connection | Enables secure connections. |

#### Authentication

Select an authentication option:

* No Authentication
* Master Credentials (default):
  + Username: Oracle username
  + Password: Select the password store from the dropdown menu:
    - Dremio: Provide the password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored secret using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.
* Secret Resource Url: Provide the username and secret resource URL for Dremio to use for the source.
* Kerberos

### Advanced Options

![](/assets/images/oracle-adv-options-e952f2b5e51d2c3b81500386987b577c.png) !

* **Use timezone as connection region**: If checked, uses timezone to set connection region.
* **Include synonyms**: If checked, includes synonyms as datasets.
* **Map Oracle DATE columns to TIMESTAMP**: If selected, the DATE column will display values in timestamp format.
* **Record fetch size**: Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. Default: 10
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to *8*.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to *60*.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Enable legacy dialect**
* **Encryption**: Provide the **SSL/TLS server certificate distinguished name**, otherwise,
  leave blank to disable the DN match.

### Reflection Refresh

![](/assets/images/hdfs-refresh-policy-9ae71114907887b859a9d01425390739.png) !

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

![](/assets/images/mongodb-metadataA-4215ce9cc791254ae9684171d87714d6.png) !

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).  
  If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

#### Metadata Refresh

* **Dataset Discovery**: Refresh interval for top-level source object names such as names of DBs and tables.
  + Fetch every -- Specify fetch time based on minutes, hours, days, or weeks. Default: 1 hour
* **Dataset Details**: The metadata that Dremio needs for query planning such as information needed for
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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Oracle TLS Configuration

To use TLS to connect to an Oracle source, do the following:

1. Select the option **Connect using SSL/TLS** during initial configuration.
2. If you want to ensure that the server you’re connecting to exactly matches a
   particular certificate string, add the Server Certificate Distinguished Name
   under **SSL/TLS** in **Advanced Options**.
3. Add the Certificate Authority certificate to Dremio's trust store. To add the CA certificate that is used to sign the Oracle certificate into Dremio's trust store:
   1. Import the CA certificate and convert the certificate into DER format (required by Java keytool).
      For example, using OpenSSL tool:  
      `$ openssl x509 -outform der -in oracle-ca.pem -out oracle-ca.der`
   2. Add the certificate to a new or existing truststore.  
      `$ keytool -import -alias oracle-ca -keystore dremio-truststore.jks -file oracle-ca.der`
   3. Modify the `DREMIO_JAVA_SERVER_EXTRA_OPTS` section of the `dremio-env` configuration
      file to use the trust store by adding the following:  
      `Djavax.net.ssl.trustStore=<path/to>/dremio-truststore.jks`
      `Djavax.net.ssl.trustStoreType=JKS`  
      `Djavax.net.ssl.trustStorePassword=<password>`

## Updating an Oracle Source

To update an Oracle source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Oracle as a Source.
4. Click **Save**.

## Deleting an Oracle Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete an Oracle source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

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
CAST  
CEIL  
CEILING  
CHAR\_LENGTH  
CHARACTER\_LENGTH  
CONCAT  
COS  
COSH  
COT  
COVAR\_POP  
COVAR\_SAMP  
DATE\_ADD  
DATE\_SUB  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_QUARTER  
DATE\_TRUNC\_WEEK  
DATE\_TRUNC\_YEAR  
DEGREES  
E  
EXP  
EXTRACT\_CENTURY  
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
MEDIAN  
MIN  
MOD  
PERCENT\_CONT  
PERCENT\_DISC  
PI  
POSITION  
POW  
POWER  
RADIANS  
REGEXP\_LIKE  
REPLACE  
REVERSE  
RIGHT  
ROUND  
RPAD  
RTRIM  
SIGN  
SIN  
SINH  
SQRT  
STDDEV  
STDDEV\_POP  
STDDEV\_SAMP  
SUBSTR  
SUBSTRING  
SUM  
TAN  
TANH  
TO\_CHAR  
TO\_DATE  
TRIM  
TRUNC  
TRUNCATE  
UCASE  
UPPER  
VAR\_POP  
VAR\_SAMP

note

Since Oracle has no Boolean type, project operations that contain SQL expressions which evaluate to true or false (e.g. `SELECT username, friends > 0`), and filter operations that include boolean literals in a filter (e.g. `WHERE currentAccount = true`) cannot be executed as pushdowns.

## Running Queries Directly on Oracle Through Dremio

Dremio users can run pass queries through Dremio to run on Oracle. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

## For More Information

* See [Oracle Data Types](/current/reference/sql/data-types/mappings/oracle/)
  for information about mapping to Dremio data types.

Was this page helpful?

[Previous

MySQL](/current/data-sources/databases/mysql)[Next

PostgreSQL](/current/data-sources/databases/postgres)

* User Impersonation
* Connection Information
  + Initial Connection
* Configuring Oracle as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Oracle TLS Configuration
* Updating an Oracle Source
* Deleting an Oracle Source
* Predicate Pushdowns
* Running Queries Directly on Oracle Through Dremio
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/postgres

Version: current [26.x]

On this page

# PostgreSQL

## Configuring PostgreSQL as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **PostgreSQL**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

| Name | Description |
| --- | --- |
| Host | Postgres host name. |
| Port | Postgres port number. Defaults to 5432. |
| Database | Database name. |
| Encrypt connection | Enables encrypted connections to Postgres using SSL. Encryption validation mode can be modified under Advanced Options. |

#### Authentication

Select an authentication option:

* No Authentication
* Master Credentials (default):
  + Username: PostgreSQL username
  + Password: Select the password store from the dropdown menu:
    - Dremio: Provide the password in plain text. Dremio stores the password.
    - [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
    - [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
    - [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.
  + Secret Resource Url: Provide the username and secret resource URL for Dremio to use for the source.

### Advanced Options

* **Record Fetch Size**: Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. By default, this is set to *10*.
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to *8*.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to *60*.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Enable legacy dialect**

#### Encryption

Validation modes include:

* Validate certificate and hostname (default)
* Validate certificate only
* Do not validate certificate or hostname

### Reflection Refresh

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a PostgreSQL Source

To update a PostgreSQL source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring PostgreSQL as a Source.
4. Click **Save**.

## Deleting a PostgreSQL Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a PostgreSQL source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

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
CAST  
CBRT  
CEIL  
CEILING  
CHAR\_LENGTH  
CHARACTER\_LENGTH  
CONCAT  
COS  
COT  
COVAR\_POP  
COVAR\_SAMP  
DATE\_ADD  
DATE\_SUB  
DATE\_TRUNC\_CENTURY  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_DECADE  
DATE\_TRUNC\_HOUR  
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
MEDIAN  
MIN  
MOD  
PERCENT\_CONT  
PERCENT\_DISC  
PI  
POSITION  
POW  
POWER  
RADIANS  
REGEXP\_LIKE  
REPLACE  
REVERSE  
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
VAR\_POP  
VAR\_SAMP

## Running Queries Directly on PostgreSQL Through Dremio

Dremio users can run pass queries through Dremio to run on PostgreSQL. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

## For More Information

* See [Postgres Data Types](/current/reference/sql/data-types/mappings/postgres/)
  for information about mapping to Dremio data types.

Was this page helpful?

[Previous

Oracle](/current/data-sources/databases/oracle)[Next

SAP HANA](/current/data-sources/databases/sap-hana)

* Configuring PostgreSQL as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a PostgreSQL Source
* Deleting a PostgreSQL Source
* Predicate Pushdowns
* Running Queries Directly on PostgreSQL Through Dremio
* For More Information

---

# Source: https://docs.dremio.com/current/data-sources/databases/sap-hana

Version: current [26.x]

On this page

# SAP HANA Enterprise

Dremio supports connecting to SAP HANA directly via username and password. The connector was tested against [HANA Express](https://hub.docker.com/r/saplabs/hanaexpress).

## Requirements

To connect to SAP HANA, you need:

* SAP HANA 2.0
* SAP username and password

## Dremio Configuration

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select the source.

   The new source dialog box appears, which contains the following tabs:

   * **General**: Create a name for your database, specify the connection details, and set the authentication.
   * **Advanced Options**: (Optional) Set the advanced configuration options for your database.
   * **Reflection Refresh**: (Optional) Set a policy to control how often Reflections are refreshed and expired.
   * **Metadata**: (Optional) Specify dataset handling and metadata refresh.
   * **Privileges**: (Optional) Add privileges for users or roles.

   Refer to the following sections for guidance on how to edit each tab.

### General

To configure the source connection:

1. For **Name**, enter the name to identify the database in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

2. For **Host**, enter the hostname or IP address for the SAP HANA source.
3. For **Port**, enter the SAP HANA port number. The default port is `39017`.
4. For **Database**, enter the service name of your database.

5. For **Username**, enter the database username.
6. For **Password**, choose an authentication method:

   * **No Authentication**: Dremio does not attempt to provide any authentication when connecting with the SQL pool.
   * **Master Credentials**: Dremio must provide a specified username and password in order to access the SQL pool.

     + For **Username**, enter the database username.
     + For **Password**, choose a method:
     + Dremio: Provide the database password in plain text. Dremio stores the password.
     + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for the Azure Key Vault secret that stores the Vertica password. The URI format is `https://<vault_name>.vault.azure.net/secrets/<secret_name>` (for example, `https://myvault.vault.azure.net/secrets/mysecret`).

       note

       To use Azure Key Vault as your application secret store, you must:

       - [Deploy Dremio on Azure](/current/get-started/cluster-deployments/deployment-models/azure-deployments/).
       - Complete the [Requirements for Authenticating with Azure Key Vault](/current/data-sources/object/azure-storage/#requirements-for-authenticating-with-azure-key-vault).

       It is not necessary to restart the Dremio coordinator when you rotate secrets stored in Azure Key Vault. Read [Requirements for Secrets Rotation](/current/data-sources/object/azure-storage/#requirements-for-secrets-rotation) for more information.
     + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
     + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Choose the HashiCorp secrets engine you're using from the dropdown menu and enter the secret reference for the password in the correct format in the provided field.

   note

   Sources containing a large number of files or tables may take longer to be added. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being added. Once complete, the source becomes accessible.

### Advanced Options

Set the advanced configuration options for your database:

* **Record fetch size**: Number of records to fetch at once. Set to `0` to have Dremio automatically decide. By default, this is set to `10`.
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to `8`.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to `60`.
* **Query timeout (s)**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **Enable external authorization plugin**: When enabled, authorizes an external plugin.
* **Connection Properties**: Connection properties and values for the data source.

### Reflection Refresh

Set the policy that controls how often Reflections are refreshed or expired, using the following options:

* **Never refresh**: Select to prevent automatic Reflection refresh; otherwise, the default is to refresh automatically.
* **Refresh every**: How often to refresh Reflections, specified in hours, days or weeks. This option is ignored if **Never refresh** is selected.
* **Set refresh schedule**: Specify the daily or weekly schedule.
* **Never expire**: Select to prevent Reflections from expiring; otherwise, the default is to expire automatically after the time limit specified in **Expire after**.
* **Expire after**: The time limit after which Reflections expire and are removed from Dremio, specified in hours, days or weeks. This option is ignored if **Never expire** is selected.

### Metadata

Set the following metadata options:

* **Remove dataset definitions if underlying data is unavailable**: Checked by default. If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible, Dremio does not remove the dataset definitions. This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.
* **Data Discovery**: Set the time interval for fetching top-level source object names such as databases and tables. You can choose to set the **Fetch every** frequency to fetch object names in minutes, hours, days, or weeks. The default frequency to fetch object names is 1 hour.
* **Dataset Details**: The metadata that Dremio needs for query planning such as information needed for fields, types, shards, statistics, and locality. Use these parameters to fetch or expire the metadata:

  + **Fetch mode**: Fetch only from queried datasets. Dremio updates details for previously queried objects in a source. By default, this is set to **Only Queried Datasets**.
  + **Fetch every**: Set the frequency to fetch dataset details in minutes, hours, days, or weeks. The default frequency to fetch dataset details is 1 hour.
  + **Expire after**: Set the expiry time of dataset details in minutes, hours, days, or weeks. The default expiry time of dataset details is 3 hours.

### Privileges

To grant privileges to specific users or roles:

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

See [Access Control](/current/security/rbac/) for additional information about privileges.

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

## Data Source Management

### Updating the Source

To update the source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the dropdown.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name.
4. Click **Save**.

### Deleting the Source

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the `ADMIN` role can delete the source.

To delete the source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and click ![The Settings icon](/images/settings-icon.png "The Settings icon") to the right.
3. From the dropdown, select **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

* Deleting a source causes all downstream views that depend on objects in the source to break.
* Sources containing a large number of files or tables may take longer to be removed. During this time, the source name is grayed out and shows a spinner icon, indicating the source is being removed. Once complete, the source disappears.

## Querying the SAP HANA Source Directly

Dremio users can run pass queries through Dremio to run on your database. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

Was this page helpful?

[Previous

PostgreSQL](/current/data-sources/databases/postgres)[Next

Snowflake](/current/data-sources/databases/snowflake)

* Requirements
* Dremio Configuration
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Predicate Pushdowns
* Data Source Management
  + Updating the Source
  + Deleting the Source
* Querying the SAP HANA Source Directly

---

# Source: https://docs.dremio.com/current/data-sources/databases/snowflake

Version: current [26.x]

On this page

# Snowflake

[Snowflake](http://www.snowflake.com) is a cloud data warehouse.

## Prerequisite

* Ensure that your Dremio cluster is at version 23.1 or later.

## User Impersonation

Dremio supports OAuth with impersonation for Snowflake. This allows Dremio users to authenticate via external OAuth and map to Snowflake roles securely. For reference, see [Snowflake's Create Security Integration (External OAuth) documentation](https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-oauth-external).

note

Reflections are not supported on data sources with user impersonation enabled to ensure that all security and governance policies defined in the underlying data source are enforced.
Reflections created prior to enabling user impersonation must be manually dropped, as they will fail to refresh once impersonation is active.

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

## Configuring Snowflake as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Snowflake**.

### General

1. In the **Name** field, specify the name by which you want the Snowflake source to appear in the **Databases** section. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.
2. Under **Connection**, follow these steps:

   note

   The optional connection parameters are case-sensitive. For example, if the name of a warehouse uses upper case only (e.g., WAREHOUSE1), specify it the same way in the **Warehouse** field.

   1. In the **Host** field, specify the hostname of the Snowflake source in this format: `LOCATOR_ID.snowflakecomputing.com`.
   2. (Optional) In the **Database** field, specify the default database to use.
   3. (Optional) In the **Role** field, specify the default access-control role to use.
   4. (Optional) In the **Schema** field, specify the default schema to use.
   5. (Optional) In the **Warehouse** field, specify the warehouse that will provide resources for executing DML statements and queries.
3. Under **Authentication**, select either Login-password authentication, Key-pair authentication or OAuth with impersonation:

   * Login-password authentication: In the **Username** field, specify the Snowflake username. Under **Password**, in the dropdown menu, choose a method for providing the Snowflake password. If you choose Dremio, provide the Snowflake password in plain text in the provided field. Dremio stores the password. You may also choose to use one of the supported secrets managers to provide the Snowflake password:

     + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for the Azure Key Vault secret that stores the Snowflake password. The URI format is `https://<vault_name>.vault.azure.net/secrets/<secret_name>` (for example, `https://myvault.vault.azure.net/secrets/mysecret`).

       note

       To use Azure Key Vault as your application secret store, you must:  
       - Deploy Dremio on [Azure AKS](/current/deploy-dremio/deploy-on-kubernetes).  
       - Complete the [Requirements for Authenticating with Azure Key Vault](/current/data-sources/object/azure-storage/#requirements-for-authenticating-with-azure-key-vault).

       It is not necessary to restart the Dremio coordinator when you rotate secrets stored in Azure Key Vault. Read [Requirements for Secrets Rotation](/current/data-sources/object/azure-storage/#requirements-for-secrets-rotation) for more information.
     + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the Snowflake password, which is available in the AWS web console or using command line tools.
     + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Choose the HashiCorp secrets engine you're using from the dropdown menu and enter the secret reference for the Snowflake password in the correct format in the provided field.
   * Key-pair authentication (see [Snowflake's key-pair documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth)): In the **Username** field, specify the Snowflake username. Under **Private Key** and **Private key passphrase**, in the dropdown menus, choose a method for providing the Snowflake private key and private key passphrase, respectively. If you choose Dremio, provide the Snowflake private key and private key passphrase in plain text in the provided fields. Dremio stores the private key and private key passphrase. You may also choose to use one of the supported secrets managers to provide the Snowflake private key and private key passphrase:

     + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for the Azure Key Vault secret that stores the Snowflake private key and private key passphrase. The URI format is `https://<vault_name>.vault.azure.net/secrets/<secret_name>` (for example, `https://myvault.vault.azure.net/secrets/mysecret`).

       note

       To use Azure Key Vault as your application secret store, you must:  
       - Deploy Dremio on [Azure AKS](/current/deploy-dremio/deploy-on-kubernetes).  
       - Complete the [Requirements for Authenticating with Azure Key Vault](/current/data-sources/object/azure-storage/#requirements-for-authenticating-with-azure-key-vault).

       It is not necessary to restart the Dremio coordinator when you rotate secrets stored in Azure Key Vault. Read [Requirements for Secrets Rotation](/current/data-sources/object/azure-storage/#requirements-for-secrets-rotation) for more information.
     + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the Snowflake private key and private key passphrase, which is available in the AWS web console or using command line tools.
     + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Choose the HashiCorp secrets engine you're using from the dropdown menu and enter the secret reference for the Snowflake private key and private key passphrase in the correct format in the provided field.
   * **OAuth with impersonation**: This allows Dremio users to authenticate via external OAuth and map to Snowflake roles securely. If you have not already, complete the steps in User Impersonation.
     + Set the JWT `audience` parameter to match Snowflake’s `EXTERNAL_OAUTH_AUDIENCE_LIST`. This ensures proper token validation and role mapping between Dremio and Snowflake.

### Advanced Options

On the Advanced Options page, you can set values for these non-required options:

| Option | Description |
| --- | --- |
| **Maximum Idle Connections** | The total number of connections allowed to be idle at a given time. The default maximum idle connections is 8. |
| **Connection Idle Time** | The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. The default connection idle time is 60 seconds. |
| **Query Timeout** | The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state. |
| **Record Fetch Size** | The maximum number of records to allow a single query to fetch. This setting prevents queries from using too many resources. |

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

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Snowflake Source

To update a Snowflake source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Snowflake as a Source.
4. Click **Save**.

## Deleting a Snowflake Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Snowflake source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Upgrading from Dremio Hub's Community Snowflake Plugin

caution

Removing a Snowflake source will drop all tables in the source. If you have any Reflections configured on tables or table-level ACLs (customized privileges) in your Snowflake sources, copy the details of those items before you remove any sources. After upgrading and re-adding your sources, you will need to recreate those Reflections and ACLs.  
  
Views are not affected by removing and re-adding Snowflake sources, provided the sources are re-added with the same names.

note

The community Snowflake plugin from Dremio Hub is not compatible with Dremio version 23.0 and later.
You should use Dremio version 23.1 or later if you have Snowflake sources because it comes with
an official Snowflake plugin.

If you are upgrading an older version of Dremio to version 23.1 or later, you must do the following:

1. Note the details of any Reflections and ACLs configured on tables in Snowflake sources.
2. Remove your Snowflake sources from Dremio.
3. Remove the community Snowflake plugin and the existing Snowflake JDBC driver.
4. Upgrade Dremio to version 23.1 or later.
5. Add your Snowflake sources to Dremio with the same names.
6. Recreate any table-level Reflections and ACLs on your Snowflake sources.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

`||`, AND, OR  
`+`, `-`, `/`, `*`  
`<=`, `<`, `>`, `>=`, `=`, `<>`, `!=`  
ABS  
ADD\_MONTHS  
AVG  
BETWEEN  
CASE  
CAST  
CEIL  
CEILING  
CHARACTER\_LENGTH  
CHAR\_LENGTH  
COALESCE  
CONCAT  
COUNT  
COUNT\_DISTINCT  
COUNT\_DISTINCT\_MULTI  
COUNT\_FUNCTIONS  
COUNT\_MULTI  
COUNT\_STAR  
DATE\_ADD  
DATE\_SUB  
DATE\_TRUNC  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_HOUR  
DATE\_TRUNC\_MINUTE  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_QUARTER  
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
MEDIAN  
MIN  
MOD  
NOT  
PERCENT\_CONT  
PERCENT\_DISC  
PERCENT\_RANK  
POSITION  
REGEXP\_LIKE  
REPLACE  
REVERSE  
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

## Running Queries Directly on Snowflake Through Dremio

Dremio users can run pass queries through Dremio to run on Snowflake. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

Was this page helpful?

[Previous

SAP HANA](/current/data-sources/databases/sap-hana)[Next

Teradata](/current/data-sources/databases/teradata)

* Prerequisite
* User Impersonation
* Configuring Snowflake as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Snowflake Source
* Deleting a Snowflake Source
* Upgrading from Dremio Hub's Community Snowflake Plugin
* Predicate Pushdowns
* Running Queries Directly on Snowflake Through Dremio

---

# Source: https://docs.dremio.com/current/data-sources/databases/teradata

Version: current [26.x]

On this page

# Teradata Enterprise

This topic describes Teradata data source setup and Dremio configuration.

## User Impersonation

The Teradata database username provided in the source configuration is the default username that is used for running queries. When queries are run against Teradata in Dremio, users use the privileges associated with the Teradata database username and run queries under that username.

You can change this default in Dremio by enabling user impersonation in the Advanced Options, which allows users to run queries under their own usernames and restricts their access. For example, `user_1` can run queries as `user_1` rather than `Teradata_svc`. Before enabling user impersonation, some setup is required in Teradata to allow one user to impersonate another user, because the username of the user in Dremio must be the same as their username in Teradata and the user must be able to connect through the Teradata database username.

To set up user impersonation, follow these steps:

1. Ensure the user's username in Teradata matches their username in Dremio. If the usernames do not match, modify one of the usernames or create a new user account with a matching username.
2. Run a GRANT CONNECT THROUGH command in Teradata to allow the user to connect through the Teradata database username:

Example of granting the CONNECT THROUGH privilege in Teradata

```
GRANT CONNECT THROUGH proxyuser TO PERMANENT testuser1 WITHOUT ROLE;
```

In this example, the user can log in as `testuser1` in Dremio and in Teradata, and they can connect through the `proxyuser`. The `proxyuser` is the Teradata database username provided in the source configuration.

3. Log in as an admin to Dremio.
4. Follow the steps for Dremio Configuration using the Teradata database username and enable **User Impersonation** in the **Advanced Options**.
5. Grant [source privileges](/current/security/rbac/privileges#source-privileges) to the user.

Now that you have enabled user impersonation, a user logging in to Dremio with their username can access the Teradata source and its datasets according to their privileges. The user also runs queries against Teradata under their username.

## Teradata Setup

Dremio provides the Teradata connector with Dremio Enterprise Edition. You must install the proprietary Teradata JDBC driver in order to connect to a Teradata source.

To setup Teradata as a data source:

1. Download the Teradata JDBC jars: **tdgssconfig.jar** and **TeraJDBC.jar**. The Teradata JDBC driver version 16.20+ does not need the **tdgssconfig.jar** file.
2. Move the jar files into the **/opt/dremio/jars/3rdparty** directory on every Dremio node.
3. Restart Dremio coordinators and executors to pick up the newly-installed JDBC driver.

1. Download [Teradata Dremio plugin JAR](https://console.cloud.google.com/storage/browser/releases.drem.io/ee/teradata/?project=dremio-1093&pli=1)
   and move it into the **/opt/dremio/jars** directory.

## Configuring Teradata as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Teradata**.

### General

Under **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

| Name | Description |
| --- | --- |
| Host | Teradata host name. |
| Port | Teradata port number. Defaults to 1025. |
| Service Name | Service Name of your database. |

#### Authentication

Select an authentication option:

* Username: Teradata username
* Password: Select the password store from the dropdown menu:
  + Dremio: Provide the password in plain text. Dremio stores the password.
  + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
  + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
  + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.

Select the **Encrypt connection** option to encrypt the connection to Teradata. Clear the checkbox to disable encryption.

### Advanced Options

Specify advanced options with the following settings.

* **Show only the initial database used for connecting.**
* **Record fetch size**: Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. Default: 10
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to *8*.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to *60*.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
* **User Impersonation**: Allows users to run queries using their credentials rather than the username provided in the source credentials. Some setup is required in Teradata to allow one user to impersonate another user. See User Impersonation.

### Reflection Refresh

Specify refresh policy options with the following settings.

* Never refresh -- Specifies how often to refresh based on hours, days, weeks, or never.
* Never expire -- Specifies how often to expire based on hours, days, weeks, or never.

### Metadata

Specify metadata options with the following settings.

#### Dataset Handling

* Remove dataset definitions if underlying data is unavailable (Default).
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
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

### Privileges

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges.

note

All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Teradata Source

To update a Teradata source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Teradata as a Source.
4. Click **Save**.

## Deleting a Teradata Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Teradata source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

## Predicate Pushdowns

Dremio delegates the execution of these expressions and functions to the database being queried, often dramatically improving query performance. It can also offload entire SQL queries that include one or more of these expressions and functions.

`<`, `<=`, `<>`, `=`, `>=`, `>`, `!=`  
`*`, `+`, `-`, `/`  
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
COSH  
COT  
COVAR\_POP  
COVAR\_SAMP  
DATE\_ADD  
DATE\_SUB  
DATE\_TRUNC\_DAY  
DATE\_TRUNC\_MONTH  
DATE\_TRUNC\_QUARTER  
DATE\_TRUNC\_WEEK  
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
PI  
POSITION  
POW  
POWER  
RADIANS  
REPLACE  
REVERSE  
RIGHT  
ROUND  
RPAD  
RTRIM  
SIGN  
SIN  
SINH  
SQRT  
STDDEV  
STDDEV\_POP  
STDDEV\_SAMP  
SUBSTR  
SUBSTRING  
SUM  
TAN  
TANH  
TIMESTAMPADD\_DAY  
TIMESTAMPADD\_HOUR  
TIMESTAMPADD\_MINUTE  
TIMESTAMPADD\_MONTH  
TIMESTAMPADD\_SECOND  
TIMESTAMPADD\_YEAR  
TIMESTAMPDIFF\_YEAR  
TO\_CHAR  
TO\_DATE  
TRIM  
TRUNC  
TRUNCATE  
UCASE  
UPPER  
VAR\_POP  
VAR\_SAMP

## Running Queries Directly on Teradata Through Dremio

Dremio users can run pass queries through Dremio to run on Teradata. Doing so can sometimes decrease query execution times. For more information, see [Querying Relational-Database Sources Directly](/current/help-support/advanced-topics/external-queries/).

Was this page helpful?

[Previous

Snowflake](/current/data-sources/databases/snowflake)[Next

Vertica](/current/data-sources/databases/vertica)

* User Impersonation
* Teradata Setup
* Configuring Teradata as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Teradata Source
* Deleting a Teradata Source
* Predicate Pushdowns
* Running Queries Directly on Teradata Through Dremio

---

# Source: https://docs.dremio.com/current/data-sources/databases/vertica

Version: current [26.x]

On this page

# Vertica

[Vertica](https://www.vertica.com/) is an analytical database.

## Prerequisites

Ensure that you have the following details before configuring Vertica as a source:

* Database name
* Hostname or IP address
* Port

## Configuring Vertica as a Source

1. On the Datasets page, to the right of **Sources** in the left panel, click ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.").
2. In the Add Data Source dialog, under **Databases**, select **Vertica**.

### General

For **Name**, enter the name to identify the data source in Dremio. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

#### Connection

| Name | Description |
| --- | --- |
| Host | Vertica host name. |
| Port | Vertica port number. Defaults to 5433. |
| Database | Service name of your database. |

#### Authentication

Select an authentication option:

* Username: Vertica username
* Password: Select the password store from the dropdown menu:
  + Dremio: Provide the password in plain text. Dremio stores the password.
  + [Azure Key Vault](/current/security/secrets-management/azure-key-vault): Provide the URI for your stored password using the format `https://<vault_name>.vault.azure.net/secrets/<secret_name>`
  + [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager): Provide the Amazon Resource Name (ARN) for the AWS Secrets Manager secret that holds the password, which is available in the AWS web console or using command line tools.
  + [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/): Select your HashiCorp secrets engine from the dropdown and enter the password reference in the required format.

### Advanced Options

Specify advanced options with the following settings.

* **Record fetch size**: Number of records to fetch at once. Set to 0 (zero) to have Dremio automatically decide. By default, this is set to **10**.
* **Maximum idle connections**: The total number of connections allowed to be idle at a given time. By default, this is set to **8**.
* **Connection idle time (s)**: The amount of time (in seconds) allowed for a connection to remain idle before the connection is terminated. By default, this is set to **60**.
* **Query timeout**: The amount of time (in seconds) allowed to wait for the results of a query. If this time expires, the connection being used is returned to an idle state.
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
* If this box is *not* checked and the underlying files under a folder are removed or the folder/source is not accessible,
  Dremio does not remove the dataset definitions.
  This option is useful in cases when files are temporarily deleted and put back in place with new sets of files.

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

On the Privileges tab, you can grant privileges to specific users or roles. See [Access Controls](/current/security/rbac/) for additional information about privileges. All privileges are optional.

1. For **Privileges**, enter the user name or role name that you want to grant access to and click the **Add to Privileges** button. The added user or role is displayed in the **USERS/ROLES** table.
2. For the users or roles in the **USERS/ROLES** table, toggle the checkmark for each privilege you want to grant on the Dremio source that is being created.
3. Click **Save** after setting the configuration.

## Updating a Vertica Source

To update a Vertica source:

1. On the Datasets page, under **Databases** in the panel on the left, find the name of the source you want to update.
2. Right-click the source name and select **Settings** from the list of actions. Alternatively, click the source name and then the ![The Settings icon](/images/settings-icon.png "The Settings icon") at the top right corner of the page.
3. In the **Source Settings** dialog, edit the settings you wish to update. Dremio does not support updating the source name. For information about the settings options, see Configuring Vertica as a Source.
4. Click **Save**.

## Deleting a Vertica Source

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

To delete a Vertica source, perform these steps:

1. On the Datasets page, click **Sources** > **Databases** in the panel on the left.
2. In the list of data sources, hover over the name of the source you want to remove and right-click.
3. From the list of actions, click **Delete**.
4. In the Delete Source dialog, click **Delete** to confirm that you want to remove the source.

note

Deleting a source causes all downstream views that depend on objects in the source to break.

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

[Previous

Teradata](/current/data-sources/databases/teradata)

* Prerequisites
* Configuring Vertica as a Source
  + General
  + Advanced Options
  + Reflection Refresh
  + Metadata
  + Privileges
* Updating a Vertica Source
* Deleting a Vertica Source
* Predicate Pushdowns