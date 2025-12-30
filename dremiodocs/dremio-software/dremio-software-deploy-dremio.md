# Dremio Software - Deploy Dremio



---

# Source: https://docs.dremio.com/current/deploy-dremio/

Version: current [26.x]

On this page

# Deploy Dremio

This topic describes the deployment models. Dremio is a distributed system that can be deployed in a public cloud or on-premises. A Dremio cluster can be co-located with one of the data sources (Hadoop or NoSQL database) or deployed separately.

## Deploy on Kubernetes

Kubernetes is the recommended deployment option for Dremio. For more information, see the following topics in this section:

* [Kubernetes Environments](/current/deploy-dremio/kubernetes-environments/) – Learn about the Kubernetes environments used to deploy Dremio.
* [Deploying on Kubernetes](/current/deploy-dremio/deploy-on-kubernetes/) – Deploy Dremio on your Kubernetes environment.
* [Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/) – Understand the configuration of your deployments in more detail.
* [Managing Engines](/current/deploy-dremio/managing-engines-kubernetes/) – Manage Dremio engines to optimize query execution.

## Other Deployment Options

Besides Kubernetes, Dremio provides other options for deployment described in this section.

### Shared Multi-Tenant Environment

If you plan on using a shared multi-tenant environment, Dremio provides a model that uses YARN for deployment:

* [**Hadoop using YARN**](/current/deploy-dremio/other-options/yarn-hadoop.md) - Dremio on Hadoop in YARN deployment. Dremio integrates with YARN ResourceManager to secure compute resources in a shared multi-tenant environment.

note

Co-locating Dremio with Hadoop/NoSQL: When Dremio is co-located with a Hadoop cluster (such as HDFS) or distributed NoSQL database (such as Elasticsearch or MongoDB), it is important to utilize containers (cgroups, Docker, and YARN containers) to ensure adequate resources for each process.

Dremio features a high-performance asynchronous engine that minimizes the number of threads and context switches under heavy load. So, unless containers are utilized, the operating system may over-allocate resources to other thread-hungry processes on the nodes.

### Standalone Cluster

If you plan on creating a standalone cluster, Dremio provides the flexibility to deploy Dremio as a standalone on-premise cluster:

* [**Standalone Cluster**](/current/deploy-dremio/other-options/standalone/index.md) - Dremio on a standalone on-premise cluster. In this scenario, a Hadoop cluster is not available and the data is not in a single distributed NoSQL database.

Was this page helpful?

[Previous

Architecture](/current/what-is-dremio/architecture)[Next

Kubernetes Environments](/current/deploy-dremio/kubernetes-environments)

* Deploy on Kubernetes
* Other Deployment Options
  + Shared Multi-Tenant Environment
  + Standalone Cluster

---

# Source: https://docs.dremio.com/current/deploy-dremio/kubernetes-environments

Version: current [26.x]

On this page

# Kubernetes Environments for Dremio

Dremio is designed to run Kubernetes environments, providing enterprise-grade data lakehouse capabilities. To successfully [deploy Dremio on Kubernetes](/current/deploy-dremio/deploy-on-kubernetes), you need a compatible hosted Kubernetes environment.

Dremio is tested and supported on the following Kubernetes environments:

* Elastic Kubernetes Service (EKS)
* Azure Kubernetes Service (AKS)
* Google Kubernetes Engine (GKE)
* Red Hat OpenShift

The sections on this page detail recommendations for AWS and Azure. Please use the information provided as a guide for your vendors' equivalent options.

note

If you're using a containerization platform built on Kubernetes that isn't listed here, please contact your provider and Dremio Account team to discuss compatibility and support options.

## Requirements

### Versions

Dremio requires regular updates to your Kubernetes version. You must be on an officially supported version, and preferably not one on extended support. See the following examples for AWS [Available versions on standard support](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#available-versions) and Azure [Kubernetes versions](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions).

### Recommendations

See this table for resource request recommendations of the variours parts of the deployment, [Recommended Resources Configuration](/current/deploy-dremio/configuring-kubernetes/#recommended-resources-configuration).

For a list of all Dremio engine sizes see, [Add an Engine](/current/deploy-dremio/managing-engines-kubernetes/add-an-engine). Engines will make up the lions share of any Dremio deployment.

#### Node Sizes

The following sections suggest AWS and Azure machines that could be used to meet our recommendations.

Dremio recommends having separate EKS node groups for the different components of our services to allow each node group to autoscale independently:

**Core Services**

* **Coordinators**

  For [coordinators](/current/what-is-dremio/architecture/#main-coordinator), Dremio recommends at least 32 CPUs and 64 GB of memory, hence, a `c6i.8xlarge` or `Standard_F32s_v2` is a good option, offering a CPU-to-memory ratio of 1:2. In the Helm charts, this would result in 30 CPUs and 60 GB of memory allocated to the Dremio pod.
* **Executors**

  For [executors](/current/what-is-dremio/architecture/#engines), Dremio recommends either:

  + 16 CPUs and 128 GB of memory, hence, a `r5d.4xlarge` or `Standard_E16_v5` is a good option, offering a CPU-to-memory ratio of 1:8. In the Helm charts, this results in 15 CPUs and 120 GB of memory allocated to the Dremio pod.
  + 32 CPUs and 128 GB of memory, hence, a `m5d.8xlarge` or `Standard_D32_v5` is a good option, offering a CPU-to-memory ratio of 1:4 for high-concurrency workloads. In the Helm charts, this results in 30 CPUs and 120 GB of memory allocated to the Dremio pod.

**Auxiliary Services**

* [Open Catalog](/current/what-is-dremio/architecture/#open-catalog) and [Semantic Search](/current/deploy-dremio/current/what-is-dremio/architecture/#ai-enabled-semantic-search).

Catalog is made up of 4 key components: Catalog Service, Catalog Server, Catalog External, and MongoDB. Search has one key component, OpenSearch.

Each of these components needs between 2-4 CPUs and 4-16 GB of memory; hence, a `m5d.2xlarge` or `Standard_D8_v5` is a good option and could be used to host multiple containers that are part of these services.

* ZooKeeper, NATS, Operators, and Open Telemetry:

Each of these need between 0.5-1 CPUs and 0.5-1 GB, `m5d.large`, `t2.medium`, `Standard_D2_v5` or `Standard_A2_v2` are good options and could be used to host multiple containers that are part of these services.

#### Disk Storage Class

Dremio recommends:

* For AWS, GP3 or IO2 as the storage type for all nodes.
* For Azure managed-premium as the storage type for all nodes.

Additionally, for [coordinators](/current/what-is-dremio/architecture/#main-coordinator) and [executors](/current/what-is-dremio/architecture/#engines), you can further use local NVMe SSD storage for C3 and spill on executors. For more information on storage classes, see the following resources [AWS Storage Class](https://docs.aws.amazon.com/eks/latest/userguide/create-storage-class.html) and [Azure Storage Class](https://learn.microsoft.com/en-us/azure/aks/concepts-storage).

Storage size requirements are:

* Coordinator volume #1: 128-512 GB (key-value store).
* Coordinator volume #2: 16 GB (logs).
* Executor volume #1: 128-512 GB (spilling).
* Executor volume #2: 128-512 GB (C3).
* Executor volume #3: 16 GB (logs).
* MongoDB volume: 128-512 GB.
* OpenSearch volume: 128 GB.
* Zookeeper volume: 16 GB.

### EKS Add-Ons

The following add-ons are required for EKS clusters:

* Amazon EBS CSI Driver
* EKS Pod Identity Agent

Was this page helpful?

[Previous

Deploy Dremio](/current/deploy-dremio/)[Next

Deploy on Kubernetes](/current/deploy-dremio/deploy-on-kubernetes)

* Requirements
  + Versions
  + Recommendations
  + EKS Add-Ons

---

# Source: https://docs.dremio.com/current/deploy-dremio/deploy-on-kubernetes

Version: current [26.x]

On this page

# Deploy Dremio on Kubernetes

You can follow these instructions to deploy Dremio on Kubernetes provisioned through a cloud provider or running in an on-premises environment.

FREE TRIAL

If you are using an **Enterprise Edition free trial**, go to [Get Started with the Enterprise Edition Free Trial](/current/get-started/kubernetes-trial).

## Prerequisites

Before deploying Dremio on Kubernetes, ensure you have the following:

* A hosted Kubernetes environment to deploy and manage the Dremio cluster.  
  Each Dremio release is tested against [Amazon Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/what-is-aks), and [Google Kubernetes Engines (GKE)](https://cloud.google.com/kubernetes-engine?hl=en#how-it-works) to ensure compatibility. If you have a containerization platform built on top of Kubernetes that is not listed here, please contact your provider and the Dremio Account Team regarding compatibility.
* Helm 3 installed on your local machine to run Helm commands. For installation instructions, refer to [Installing Helm](https://helm.sh/docs/intro/install/) in the Helm documentation.
* A local kubectl configured to access your Kubernetes cluster. For installation instructions, refer to [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) in the Kubernetes documentation.
* Object Storage: Amazon S3 (including S3-compatible, e.g., MinIO), Azure Storage, or Google Cloud Storage (GCS).
* Storage classes that support ReadWriteOnce (RWO) access mode and ideally can create expandable volumes.
* The ability to connect to [Quay.io](http://quay.io/) to access the [new v3 Helm chart](https://quay.io/repository/dremio/dremio-helm?tab=tags) for Dremio 26+, since the [older v2 Helm chart](https://github.com/dremio/dremio-cloud-tools/tree/master/charts/dremio_v2) will not function.

### Additional Prerequisites for the Enterprise Edition

For the Enterprise Edition, you must:

* Create an account on [Quay.io](https://quay.io/) to access [Dremio's OCI repository](https://quay.io/organization/dremio), which stores Dremio's Helm charts and images.  
  To get access, contact your Dremio account executive or Dremio Support.

  note

  If your internet access doesn't allow reaching Dremio's OCI repository in Quay.io, consider using a private mirror to fetch Dremio's Helm chart images.
* Get a valid license key issued by Dremio to put in the Helm chart. To obtain the license, refer to [Licensing](/current/admin/licensing/).

### Additional Prerequisites for the OpenShift

Before deploying Dremio onto OpenShift, you additionally need the following:

* Have the OpenShift `oc` CLI command configured and authenticated. For the installation instructions, see [OpenShift CLI (oc)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.11/html/cli_tools/openshift-cli-oc).

#### Node Tuning for OpenSearch on OpenShift

OpenSearch requires the `vm.max_map_count` kernel parameter to be set to at least **262144**.

This parameter controls the maximum number of memory map areas a process can have, and OpenSearch uses memory-mapped files extensively for performance.

Without this setting, OpenSearch pods will fail to start with errors related to virtual memory limits.

Since the Helm chart sets `setVMMaxMapCount: false` for OpenShift compatibility (to avoid privileged init containers), you need to configure this kernel parameter at the node level. The **recommended way** to do it is a Node Tuning Operator. This Operator ships with OpenShift and provides a declarative way to configure kernel parameters.

Create a `Tuned` resource to configure the required kernel parameter:

The `tuned-opensearch.yaml` configuration file

```
apiVersion: tuned.openshift.io/v1  
kind: Tuned  
metadata:  
  name: openshift-opensearch  
  namespace: openshift-cluster-node-tuning-operator  
spec:  
  profile:  
  - data: |  
      [main]  
      summary=Optimize systems running OpenSearch on OpenShift nodes  
      include=openshift-node  
      [sysctl]  
      vm.max_map_count=262144  
    name: openshift-opensearch  
  recommend:  
  - match:  
    - label: tuned.openshift.io/opensearch  
      type: pod  
    priority: 20  
    profile: openshift-opensearch
```

This YAML should be saved locally and applied to any cluster you intend to deploy Dremio:

```
oc apply -f tuned-opensearch.yaml
```

## Step 1: Deploy Dremio

To deploy the Dremio cluster in Kubernetes, do the following:

1. Configure your values to deploy Dremio to Kubernetes in the file `values-overrides.yaml`. For that, go to [Configuring Your Values to Deploy Dremio to Kubernetes](/current/deploy-dremio/configuring-kubernetes/) and get back here to continue with the deployment.
2. On your terminal, start the deployment by installing Dremio's Helm chart:

   * Standard Kubernetes
   * OpenShift

   Run the following command for any Kubernetes environment except for OpenShift:

   ```
   helm install <your-dremio-install-release> oci://quay.io/dremio/dremio-helm \  
   --values <your-local-path>/values-overrides.yaml \  
   --version <optional-helm-chart-version> \  
   --set-file <optional-config-files> \  
   --wait
   ```

   Where:

   * `<your-dremio-install-release>` - The name that identifies your Dremio installation. For example, `dremio-1-0`.
   * `<your-local-path>` - The path to reach your `values-overrides.yaml` configuration file.
   * (Optional) `--version <optional-helm-chart-version>` - The version of Dremio's Helm chart to be used. If not provided, defaults to the latest.
   * (Optional) `--set-file <optional-config-file>` - An optional configuration file for deploying Dremio. For example, an [Identity Provider](/current/security/authentication/identity-providers/) configuration file, which is not defined in the `values-overrides.yaml` and can be provided here through this option.

   For OpenShift, the command requires an additional `--values` option with the path to the OpenShift-specific `values-openshift-overrides.yaml` configuration file. This additional option must be placed before the `--values` option with the `values-overrides.yaml` configuration file, resulting in its substitution first.

   Run the following command for OpenShift:

   ```
   helm install <your-dremio-install-release> oci://quay.io/dremio/dremio-helm \  
   --values <your-local-path1>/values-openshift-overrides.yaml \  
   --values <your-local-path2>/values-overrides.yaml \  
   --version <optional-helm-chart-version> \  
   --set-file <optional-config-files> \  
   --wait
   ```

   Where:

   * `<your-dremio-install-release>` - The name that identifies your Dremio installation. For example, `dremio-1-0`.
   * `<your-local-path1>` - The path to reach your `values-openshift-overrides.yaml` configuration file. Only required for OpenShift.
   * `<your-local-path2>` - The path to reach your `values-overrides.yaml` configuration file.
   * (Optional) `--version <optional-helm-chart-version>` - The version of Dremio's Helm chart to be used. If not provided, defaults to the latest.
   * (Optional) `--set-file <optional-config-file>` - An optional configuration file for deploying Dremio. For example, an [Identity Provider](/current/security/authentication/identity-providers/) configuration file, which is not defined in the `values-overrides.yaml` and can be provided here through this option.
3. Monitor the deployment using the following commands:

   * Standard Kubernetes
   * OpenShift

   Run the following command for any Kubernetes environment except for OpenShift:

   ```
   kubectl get pods
   ```

   For OpenShift, run the following command:

   ```
   oc get pods
   ```

   When all of the pods are in the `Ready` state, the deployment is complete.

   Troubleshooting

   * If a pod remains in `Pending` state for more than a few minutes, run the following command to view its status to check for issues, such as insufficient resources for scheduling:

     ```
     kubectl describe pods <pod-name>
     ```
   * If the events at the bottom of the output mention insufficient CPU or memory, do one of the following:

     + Adjust the values in the `values-overrides.yaml` configuration file and redeploy.
     + Add more resources to your Kubernetes cluster.
   * If a pod returns a failed state (especially `dremio-master-0`, the most important pod), use the following commands to collect the logs:

     + Standard Kubernetes
     + OpenShift

     Run the following command for any Kubernetes environment except for OpenShift:

     ```
     kubectl logs dremio-master-0
     ```

     For OpenShift, run the following command:

     ```
     oc logs deployment/dremio-master
     ```

## Step 2: Connecting to Dremio

Now that you've installed the Helm chart and deployed Dremio on Kubernetes, the next step is connecting to Dremio, where you have the following options:

* Dremio Console
* OpenShift Route
* BI Tools via ODBC/JDBC
* BI Tools via Apache Arrow Flight

To connect to Dremio via [the Dremio console](/current/get-started/quick_tour), run the following command to use the `services dremio-client` in Kubernetes to find the host for the Dremio console:

```
$ kubectl get services dremio-client  
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
...             ...            ...             ...               ...                              ...
```

* If the value in the `TYPE` column of the output is `LoadBalancer`, access the Dremio console through the address in the `EXTERNAL_IP` column and port **9047**.  
  For example, in the output below, the value under the `EXTERNAL-IP` column is `8.8.8.8`. Therefore, access the Dremio console through <http://8.8.8.8:9047>.

  ```
  $ kubectl get services dremio-client  
  NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
  dremio-client   LoadBalancer   10.99.227.180   8.8.8.8           31010:32260/TCP,9047:30620/TCP   2d
  ```

  If you want to change the exposed port on the load balancer, change the value of the setting `coordinator.web.port` in the file `values-overrides.yaml`.
* If the value in the `TYPE` column of the output is `NodePort`, access the Dremio console through <http://localhost:30670>.

To expose Dremio externally using OpenShift Routes, do the following:

```
$ oc expose service dremio-client --port=9047 --name=dremio-ui  
  
$ oc get route dremio-ui -o jsonpath='{.spec.host}'
```

To connect your BI tools to Dremio via ODBC/JDBC, run the following command to use the `services dremio-client` in Kubernetes to find the host for ODBC/JDBC connections by using the following command:

```
$ kubectl get services dremio-client  
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
...             ...            ...             ...               ...                              ...
```

* If the value in the `TYPE` column of the output is `LoadBalancer`, access Dremio using ODBC/JDBC through the address in the `EXTERNAL_IP` column and port **31010**.  
  For example, in the output below, the value under the `EXTERNAL-IP` column is `8.8.8.8`. Therefore, access Dremio using ODBC/JDBC on port 31010 through <http://8.8.8.8:31010>.

  ```
  $ kubectl get services dremio-client  
  NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
  dremio-client   LoadBalancer   10.99.227.180   8.8.8.8           31010:32260/TCP,9047:30620/TCP   2d
  ```

  If you want to change the exposed port on the load balancer, change the value of the setting `coordinator.client.port` in the file `values-overrides.yaml`.
* If the value in the `TYPE` column of the output is `NodePort`, access Dremio using ODBC/JDBC through <http://localhost:32390>.

To connect your BI tools to Dremio via Apache Arrow Flight, run the following command to use the `services dremio-client` in Kubernetes to find the host for Apache Arrow Flight connections by using the following command:

```
$ kubectl get services dremio-client  
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
...             ...            ...             ...               ...                              ...
```

* If the value in the `TYPE` column of the output is `LoadBalancer`, access Dremio using Apache Arrow Flight through the address in the `EXTERNAL_IP` column and port **32010**.  
  For example, in the output below, the value under the `EXTERNAL-IP` column is `8.8.8.8`. Therefore, access Dremio using Apache Arrow Flight through <http://8.8.8.8:32010>.

  ```
  $ kubectl get services dremio-client  
  NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
  dremio-client   LoadBalancer   10.99.227.180   8.8.8.8           31010:32260/TCP,9047:30620/TCP   2d
  ```

  If you want to change the exposed port on the load balancer, change the value of the setting `coordinator.flight.port` in the file `values-overrides.yaml`.
* If the value in the `TYPE` column of the output is `NodePort`, access Dremio using Apache Arrow Flight through <http://localhost:31357>.

Was this page helpful?

[Previous

Kubernetes Environments](/current/deploy-dremio/kubernetes-environments)[Next

Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/)

* Prerequisites
  + Additional Prerequisites for the Enterprise Edition
  + Additional Prerequisites for the OpenShift
* Step 1: Deploy Dremio
* Step 2: Connecting to Dremio

---

# Source: https://docs.dremio.com/current/deploy-dremio/configuring-kubernetes/

Version: current [26.x]

On this page

# Configuring Your Values to Deploy Dremio to Kubernetes

[Helm](https://helm.sh/) is a standard for managing Kubernetes applications, and the [Helm chart](https://helm.sh/docs/topics/charts/) defines how applications are deployed to Kubernetes. Dremio's Helm chart contains the default deployment configurations, which are specified in the `values.yaml`.

Dremio recommends configuring your deployment values in a separate `.yaml` file since it will allow simpler updates to the latest version of the Helm chart by copying the separate configuration file across Helm chart updates.

FREE TRIAL

If you are using an **Enterprise Edition free trial**, you don't need to do all the configurations described on this page. Instead, follow the configuration steps described in [Get Started with the Enterprise Edition Free Trial](/current/get-started/kubernetes-trial).

## Configure Your Values

To configure your deployment values, do the following:

1. Get the `values-overrides.yaml` configuration file and save it locally. [Click here](/downloads/values-overrides.yaml) to download the file.

   The `values-overrides.yaml` configuration file

   ```
   # A Dremio License is required  
   dremio:  
     license: "<your-license-key>"  
     image:  
       repository: quay.io/dremio/dremio-enterprise-jdk21  
     
     # Configuration file customization  
     # The configFiles and configBinaries options provide the ability to override or add configuration files  
     # included in the Dremio ConfigMap. Both use a map where keys correspond to the filenames   
     # and values are the file contents.  
     
     # configFiles: Use this to provide text-based configuration files that will be mounted in /opt/dremio/conf/  
     # Note: The dremio.conf file is controlled by multiple settings in this values file and  
     # should not be directly overridden here.  
     # Example:  
     #configFiles:  
     # vault_config.json: |  
     #   {  
     #     <your-vault-json-config>  
     #   }  
     
     # configBinaries: Use this to provide binary configuration files (encoded as base64)  
     # These files will also be mounted in /opt/dremio/conf/  
     # Example:  
     #configBinaries:  
     #  custom-truststore.jks: "base64EncodedBinaryContent"  
     
     # dremioConfExtraOptions: Use this to add settings in dremio.conf  
     # Example:  
     #dremioConfExtraOptions:  
     #  # Enable SSL for fabric services  
     #  "services.fabric.ssl.enabled": true  
     #  "services.fabric.ssl.auto-certificate.enabled": false  
     
     # Hive 2 and 3 configuration files - can be provided here too. See: https://docs.dremio.com/current/deploy-dremio/configuring-kubernetes/#hive  
     #hive2ConfigFiles:  
     #  
     #hive3ConfigFiles:  
     #  
     
   # To pull images from Dremio's Quay, you must create an image pull secret. For more info, see:  
   # https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod  
   # All of the images are pulled using this same secret.  
   imagePullSecrets:  
     -  <your-pull-secret-name>  
     
   # Dremio Coordinator  
   coordinator:  
     web:  
       auth:  
         enabled: true  
         type: "internal" # Valid types are: internal, ldap, azuread, oauth, oauth+ldap  
         # if enabled is true and type ldap, azuread, oauth, or oauth+ldap  
         # Uncomment the entry below and provide the JSON configuration inline  
         # OR use --set-file coordinator.web.auth.ssoFile=/path/to/file for the SSO provider configuration file during Helm install  
         # for more information about the file format for your SSO provider  
         # see https://docs.dremio.com/current/get-started/cluster-deployments/customizing-configuration/dremio-conf/sso-config/   
         # ssoFile: |  
         # {  
         # <your-sso-json-file-content>  
         # }  
       tls:  
         enabled: false  
         secret: "<your-tls-secret-name>"  
     client:  
       tls:  
         enabled: false  
         secret: "<your-tls-secret-name>"  
     flight:  
       tls:  
         enabled: false  
         secret: "<your-tls-secret-name>"  
     resources:  
       requests:  
         cpu: "32"  
         memory: "64Gi"  
       limits:  
         memory: "64Gi"  
     volumeSize: 512Gi   
     
   # Where Dremio stores metadata, Reflections, uploaded files, and backups.  The distributed store is required for Dremio to be operational.  
   # For more information, see https://docs.dremio.com/current/get-started/cluster-deployments/architecture/distributed-storage/  
   distStorage:  
     # The supported distributed storage types are: aws, gcp, or azureStorage. For S3-compatible storage use aws.  
     type: <your-distributed-storage-type> # Add here your distributed storage template from http://docs.dremio.com/current/deploy-dremio/configuring-kubernetes/#configuring-the-distributed-storage  
     
   # MongoDB is the backing store for the Open Catalog. Backups are enabled by default and will take place automatically. Dremio will write these backups to your distributed storage location. Not all authentication types are supported. See our distributed storage docs link above. Lack of support will be noted where applicable.  
   mongodb:  
     backup:  
       enabled: true  
     
   # Dremio Catalog  
   catalog:  
     externalAccess:  
       enabled: true  
       tls:   
         enabled: false  
         secret: "<your-catalog-tls-secret-name>"  
     # This is where Iceberg tables created in your catalog will reside  
     storage:  
   # The supported catalog storage types are: S3, azure and GCS. For S3-compatible storage use S3.  
       type: <your-catalog-storage-type>   
   # Add here your catalog storage template from https://docs.dremio.com/current/deploy-dremio/configuring-kubernetes/#configuring-storage-for-dremio-catalog  
     
   service:  
     type: LoadBalancer
   ```
2. Edit the `values-overrides.yaml` file to configure your values. See the following sections for details on each configuration option:

   * License
   * Pull Secret
   * Coordinator
   * Coordinator's Distributed Storage
   * Open Catalog
   * Advanced Values Configurations

   IMPORTANT

   In all code examples, `...` denotes additional values that have been omitted.

   Group all values associated with a given parent key in the YAML under a single instance of that parent, for example:

   Do

   ```
   dremio:  
     key-one: <value-one>  
     key-two:  
       key-three: <value-two>
   ```

   Do not

   ```
   dremio:  
     key-one: <value-one>  
     
   dremio:    
     key-two:  
       key-three: <value-two>
   ```

   Please note the parent relationships at the top of each YAML snippet and subsequent values throughout this section. The hierarchy of keys and indentations in YAML must be respected.
3. Save the `values-overrides.yaml` file.

Once done with the configuration, deploy Dremio to Kubernetes. See how in [Deploying Dremio to Kubernetes](/current/deploy-dremio/deploy-on-kubernetes/).

### License

Provide your license key. To obtain a license, see [Licensing](/current/admin/licensing).  
Add this configuration under the parent, as shown in the following example:

Configuration of the license key

```
dremio:  
  license: "<your-license-key>"  
  ...
```

### Pull Secret

Provide the secret used to pull the images from Quay.io as follows:

1. Log in to [Quay.io](https://quay.io/), select your account name at the top right corner, and select **Account Settings** in the drop-down menu.
2. Click **Generate Encrypted Password**, type your password, and click **Verify**.
3. On the next dialog, select **Kubernetes Secret**, and follow steps 1 and 2 to download the secret and run the command to submit the secret to the cluster.
4. Add the configuration under the parent, as shown in the following example:

   Configuration of the secret to pull images from Quay.io

   ```
   imagePullSecrets:  
     - <your-quayio-secret-name>
   ```

### Coordinator

#### Resource Configuration

Configure the volume size, resources limits, and resources requests. To configure these values, see Recommended Resources Configuration.

Add this configuration under the parents, as shown in the following example:

Configuration of the coordinator's resources with example values

```
coordinator:  
  resources:  
    requests:  
      cpu: 15  
      memory: 30Gi  
  volumeSize: 100Gi  
  ...
```

#### Identity Provider

Optionally, you can configure authentication via an identity provider. Each type of identity provider requires an additional configuration file provided during Dremio's deployment.

Select the authentication `type`, and follow the corresponding link for instructions on how to create the associated configuration file:

* `azuread` - See how to [configure Microsoft Entra ID with user and group lookup](/current/security/authentication/identity-providers/microsoft-entra-id#configuring-microsoft-entra-id).
* `ldap` - See how to [configure Dremio for LDAP](/current/security/authentication/identity-providers/ldap).
* `oauth` - See how to [configure Dremio for OpenID](/current/security/authentication/identity-providers/oidc/#configuring-dremio-for-openid).
* `oauth+ldap` - See how to [configure Dremio for Hybrid OpenID+LDAP](/current/security/authentication/identity-providers/oidc/#configuring-dremio-for-hybrid-openidldap).

Add this configuration under the parents, as shown in the following example:

Configuration of the coordinator's identity provider

```
coordinator:  
  web:  
    auth:  
      type: <your-auth-type>  
  ...
```

The identity provider configuration file can be embedded in your `values-overrides.yaml`. To do this, use the `ssoFile` option and provide the JSON content constructed per the instructions linked above. Here is an example for Microsoft Entra ID:

Configuration of an embedded identity provider file with an example for Microsoft Entra ID

```
coordinator:  
  web:  
    auth:  
      enabled: true  
      type: "azuread"  
      ssoFile: |  
      {  
        "oAuthConfig": {  
          "clientId": "<your-client-id>",  
          "clientSecret": "<your-secret>",  
          "redirectUrl": "<your-redirect-url>",  
          "authorityUrl": "https://login.microsoftonline.com/<your-tenant-id>/v2.0",  
          "scope": "openid profile",  
          "jwtClaims": {  
            "userName": "<your-preferred-username>"  
          }  
        }  
      }  
  ...
```

For examples for the other types, see [Identity Providers](/current/security/authentication/identity-providers)

This is not the only configuration file that can be embedded inside the `values-overrides.yaml` file. However, these are generally used for advanced configurations. For more information, see Additional Configuration.

#### Transport Level Security

Optionally enable the desired level of Transport Level Security (TLS) by setting `enabled: true` for client, Arrow Flight, or web TLS. To provide the TLS secret, see Creating a TLS Secret.

Add this configuration under the parent, as shown in the following example:

Configuration of TLS for the coordinator

```
coordinator:  
  client:  
    tls:  
      enabled: false  
      secret: <your-tls-secret>  
  flight:  
    tls:  
      enabled: false  
      secret: <your-tls-secret>  
  web:  
    tls:  
      enabled: false  
      secret: <your-tls-secret>  
  ...
```

note

If Web TLS is enabled, see Configuring Open Catalog when the Coordinator Web is Using TLS.

### Coordinator's Distributed Storage

This is where Dremio stores metadata, Reflections, uploaded files, and backups. A distributed store is required for Dremio to be operational. The supported types are Amazon S3 or S3-compatible storage, Azure Storage, and Google Cloud Storage (GCS). For examples of configurations, see Configuring the Distributed Storage.

Add this configuration under the parent, as shown in the following example:

Configuration of the coordinator's distributed storage

```
distStorage:  
  type: "<your-dist-store-type>"  
  ...
```

### Open Catalog

The configuration for the Open Catalog has several options:

* Configuring storage for the Open Catalog is mandatory since this is the location where Iceberg tables created in the catalog will be written. For configuring the storage, see Configuring Storage for the Open Catalog.

  Add this configuration under the parent, as shown in the following example:

  Configuration of the storage for the Open Catalog

  ```
  catalog:  
    storage:  
      location: <your-object-store-path>  
      type: <your-object-store-type>  
    ...
  ```
* (Optional) MongoDB is the backing store for Open Catalog. Its backup is enabled by default. This backup is written to distributed storage. Open Catalog backup can be disabled by setting enabled to false. The configuration shown here performs an automatic Open Catalog backup every day at midnight, and keeps the last three backups.

  Enablement of the Open Catalog Backing Store Backup

  ```
  mongodb:  
    backup:  
      enabled: true  
      schedule: "0 0 * * *"  
      keep: 3
  ```
* (Optional) Configure external access if you want to connect to the Open Catalog with an engine other than Dremio that supports Iceberg REST. For example, Spark.

  Add this configuration under the parent, as shown in the following example:

  Configuration of external access for the Open Catalog

  ```
  catalog:  
    externalAccess:  
      enabled: true  
    ...
  ```
* (Optional) Use Transport Level Security (TLS) for external access to require clients connecting to the Open Catalog from outside the namespace to use TLS. To configure it, see Configuring TLS for Open Catalog External Access.

  Add this configuration under the parent, as shown in the following example:

  Configuration of TLS for external access to the Open Catalog

  ```
  catalog:  
    externalAccess:   
      enabled: true  
      tls:  
        enabled: true  
        secret: <your-catalog-tls-secret>  
    ...
  ```
* (Optional) If Dremio coordinator web access is using TLS, additional configuration is necessary. To configure it, see Configuring Open Catalog When the Coordinator Web is Using TLS.

  Add this configuration under the parent, as shown in the following example:

  Configuration of the Open Catalog when the coordinator web access is using TLS

  ```
  catalog:  
    externalAccess:  
      enabled: true  
      authentication:  
        authServerHostname: <your-auth-server-host>  
    ...
  ```

Save the `values-overrides.yaml` file.

Once done with the configuration, deploy Dremio to Kubernetes. See how in the topic [Deploying Dremio to Kubernetes](/current/deploy-dremio/deploy-on-kubernetes/).

## Configuring Your Values - Advanced

### OpenShift

warning

OpenShift has additional prerequisites that must be applied before installing Dremio. For more information, see [Deploy on Kubernetes - Prerequisites](/current/deploy-dremio/deploy-on-kubernetes#prerequisites).

To deploy successfully on OpenShift, you must deploy with two override files. The YAML file you've been using to this point (`values-overrides.yaml`), and an additional YAML file mentioned below (`openshift-overrides.yaml`) with security settings required by OpenShift per its default configuration. Both can be provided in a single Helm install command.

Get the `openshift-overrides.yaml` configuration file and save it locally.
[Click here](/downloads/values-openshift-overrides.yaml) to download the file.

### Dremio Platform Images

The Dremio platform requires 18 images when running fully featured. All images are published by Dremio to our Quay and are listed below. If you want to use a private mirror of our repository, add the snippets below to `values-overrides.yaml` to repoint to your own.

Dremio Platform Images

note

If creating a private mirror, use the same repository names and tags from [Dremio's Quay.io](https://quay.io/organization/dremio).
This is important for supportability.

```
dremio:  
  image:  
    repository: quay.io/dremio/dremio-enterprise-jdk21  
    tag: <the-image-tag-from-quayio>
```

```
busyBox:  
  image:  
    repository: quay.io/dremio/busybox  
    tag: <the-image-tag-from-quayio>
```

```
k8s:  
  image:  
    repository: quay.io/dremio/alpine/k8s  
    tag: <the-image-tag-from-quay-io>
```

```
engine:  
  operator:  
    image:  
      repository: quay.io/dremio/dremio-engine-operator  
      tag: <the-image-tag-from-quay-io>
```

```
zookeeper:  
  image:  
    repository: quay.io/dremio/zookeeper  
    tag: <the-image-tag-from-quay-io>
```

```
opensearch:  
  image:  
    repository: quay.io/dremio/dremio-search-opensearch  
    tag: <the-image-tag-from-quay-io> # The tag version must be a valid OpenSearch version as listed here https://opensearch.org/docs/latest/version-history/  
  preInstallJob:  
    image:  
      repository: quay.io/dremio/dremio-search-init  
      tag: <the-image-tag-from-quay-io>
```

```
opensearchOperator:  
  manager:  
    image:  
      repository: quay.io/dremio/dremio-opensearch-operator  
      tag: <the-image-tag-from-quay-io>  
  kubeRbacProxy:  
    image:  
      repository: quay.io/dremio/kubebuilder/kube-rbac-proxy  
      tag: <the-image-tag-from-quay-io>
```

```
mongodbOperator:  
  image:  
    repository: quay.io/dremio/dremio-mongodb-operator  
    tag: <the-image-tag-from-quay-io>
```

```
mongodb:  
  image:  
    repository: quay.io/dremio/percona/percona-server-mongodb  
    tag: <the-image-tag-from-quay-io>
```

```
catalogservices:  
  image:  
    repository: quay.io/dremio/dremio-catalog-services-server  
    tag: <the-image-tag-from-quay-io>
```

```
catalog:  
  image:  
    repository: quay.io/dremio/dremio-catalog-server  
    tag: <the-image-tag-from-quay-io>  
  externaAccess:  
    image:  
      repository: quay.io/dremio/dremio-catalog-server-external  
      tag: <the-image-tag-from-quay-io>
```

```
nats:  
  container:  
    image:  
      repository: quay.io/dremio/nats  
      tag: <the-image-tag-from-quay-io>  
  reloader:  
    image:  
      repository: quay.io/dremio/natsio/nats-server-config-reloader  
      tag: <the-image-tag-from-quay-io>  
  natsBox:  
    container:  
      image:  
        repository: quay.io/dremio/natsio/nats-box  
        tag: <the-image-tag-from-quay-io>
```

```
telemetry:  
  image:  
    repository: quay.io/dremio/otel/opentelemetry-collector-contrib  
    tag: <the-image-tag-from-quay-io>
```

### Scale-out Coordinators

Dremio can scale to support high-concurrency use cases through scaling coordinators. Multiple stateless coordinators rely on the primary coordinator to manage Dremio's state, enabling Dremio to support many more concurrent users. These scale-out coordinators are intended for high query throughput and are not applicable for standby or disaster recovery. While scale-out coordinators generally reduce the load on the primary coordinator, the primary coordinator's vCPU request should be increased for every two scale-outs added to avoid negatively impacting performance.

Perform this configuration in this section of the file, where count refers to the number of scale-outs. A count of 0 will provision only the primary coordinator:

Configuration of scale-out coordinators with an example value

```
coordinator:  
  count: 1  
  ...
```

note

When using scale-out coordinators, the load balancer session affinity should be enhanced. See: Advanced Load Balancer Configuration.

### Configuring Kubernetes Pod Metadata (including Node Selector)

It's possible to add metadata both globally and to each of the StatefulSets (coordinators, classic engines, ZooKeeper, etc.), including configuring a node selector for pods to use specific node pools.

warning

Define these values with caution and foreknowledge of expected entries because any misconfiguration may result in Kubernetes being unable to schedule your pods.

Use the following options to add metadata:

* `labels:` - Configured using key-value pairs as shown in the following examples:

  Configuration of a global label with a key-value example

  ```
  labels:  
    foo: bar
  ```

  Configuration of a StatefulSet label for the Open Catalog with a key-value example

  ```
  catalog:  
    labels:  
      foo: bar  
    ...
  ```

  For more information on labels, see the Kubernetes documentation on [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
* `annotations:` - Configured using key-value pairs as shown in the following examples.

  Configuration of a global annotation with a key-value example

  ```
  annotations:  
    foo: bar
  ```

  Configuration of a StatefulSet annotation for MongoDB with a key-value example

  ```
  mongodb:  
    annotations:  
      foo: bar  
    ...
  ```

  For more information on annotations, see the Kubernetes documentation on [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
* `tolerations:` - Configured using a specific structure as shown in the following examples:

  Configuration of a global toleration with example values

  ```
  tolerations:  
  - key: "key1"  
    operator: "Equal"  
    value: "value1"  
    effect: "NoSchedule"
  ```

  Configuration of a StatefulSet toleration for the Open Catalog with example values

  ```
  catalog:  
    tolerations:  
    - key: "key1"  
      operator: "Equal"  
      value: "value1"  
      effect: "NoSchedule"  
    ...
  ```

  For more information on tolerations, see the Kubernetes documentation on [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).
* `nodeSelector:` - Configured using a specific structure as shown in the following examples.

  Configuration of a global node selector with an example value

  ```
  nodeSelector:  
    nodetype: coordinator
  ```

  Configuration of a StatefulSet node selector for the coordinator with an example value

  ```
  coordinator:  
    nodeSelector:  
      nodetype: coordinator  
    ...
  ```

To understand the structure and values to use in the configurations, expand "Metadata Structure and Values" below:

Metadata Structure and Values

For global metadata:

Global metadata structure 

```
annotations: {}  
labels: {}  
tolerations: []  
nodeSelector: {}
```

For StatefulSet metadata:

StatefulSet metadata structure for the coordinator

```
coordinator:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:   
    nodetype: coordinator
```

StatefulSet metadata structure for the executors

```
executor:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:  
    nodetype: coordinator
```

StatefulSet metadata structure for the Open Catalog

```
catalog:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:  
    nodetype: catalog
```

StatefulSet metadata structure for the Open Catalog services

```
catalogservices:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:  
    nodetype: catalogservices
```

StatefulSet metadata structure for MongoDB

```
mongodb:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:  
    nodetype: mongo
```

StatefulSet metadata structure for OpenSearch

```
opensearch:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:  
    nodetype: operators  
  oidcProxy:  
    annotations: {}  
    labels: {}  
    tolerations: []  
    nodeSelector:  
      nodeType: utils  
  preInstallJob:  
    annotations: {}  
    labels: {}  
    tolerations: []  
    nodeSelector:  
      nodeType: jobs
```

StatefulSet metadata structure for NATS

```
nats:  
  podTemplate:  
    merge:  
      spec:  
        annotations: {}  
        labels: {}  
        tolerations: []  
        nodeSelector:  
          nodetype: nats
```

StatefulSet metadata structure for the MongoDB operator

```
mongodbOperator:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:  
    nodetype: operators
```

StatefulSet metadata structure for the OpenSearch operator

```
opensearchOperator:  
  annotations: {}  
  labels: {}  
  tolerations: []  
  nodeSelector:  
    nodetype: operators
```

### Configuring Pods Priority

You can configure the priority of Dremio pods through priority classes. First, define the priority class, as shown in the following example:

Definition of a `high-priority` priority class

```
apiVersion: scheduling.k8s.io/v1  
kind: PriorityClass  
metadata:  
  name: high-priority  
value: 1000000  
globalDefault: false  
description: "This priority class should be used for coordinator pods only."
```

Then, apply the priority class under the parents, as shown in the following example:

Configuration of the `high-priority` priority class for the coordinator

```
coordinator:  
  priorityClassName: high-priority
```

To understand the structure and values to use in the configurations, expand "Priority Class Configuration Structure and Values" below:

Priority Class Configuration Structure and Values

Priority class configuration for the coordinator

```
coordinator:  
  priorityClassName: <your-priority-class-name>
```

Priority class configuration for the Open Catalog

```
catalog:  
  priorityClassName: <your-priority-class-name>  
  externalAccess:  
    priorityClassName: <your-priority-class-name>
```

Priority class configuration for the Open Catalog services

```
catalogservices:  
  priorityClassName: <your-priority-class-name>
```

Priority class configuration for the engine

```
engine:  
  executor:  
    priorityClassName: <your-priority-class-name>  
  operator:  
    priorityClassName: <your-priority-class-name>
```

Priority class configuration for OpenSearch

```
opensearch:  
  priorityClassName: <your-priority-class-name>
```

Priority class configuration for the OpenSearch operator

```
opensearchOperator:  
  priorityClassName: <your-priority-class-name>
```

Priority class configuration for MongoDB

```
mongodb:  
  priorityClassName: <your-priority-class-name>
```

Priority class configuration for the MongoDB hooks

```
mongodbHooks:  
  priorityClassName: <your-priority-class-name>
```

Priority class configuration for NATS

```
nats:  
  podTemplate:  
    merge:  
      spec:  
        priorityClassName: <your-priority-class-name>  
  natsBox:  
    podTemplate:  
      merge:  
        spec:  
          priorityClassName: <your-priority-class-name>
```

Priority class configuration for ZooKeeper

```
zookeeper:  
  priorityClassName: <your-priority-class-name>
```

Priority class configuration for telemetry

```
telemetry:  
  priorityClassName: <your-priority-class-name>
```

note

To verify which priority class is applied to each pod, run the command below, and check the `PRIORITY_CLASS` column:

Run kubectl to list the pods and their priority class

```
kubectl get pods -o custom-columns="NAME:.metadata.name,PRIORITY_CLASS:.spec.priorityClassName" -n dremio
```

### Configuring Extra Environment Variables

Optionally, you can define extra environment variables to be passed to either coordinators or executors. This can be done by adding the configuration under the parents as shown in the following examples:

Configuration of extra environment variables for the coordinator

```
coordinator:  
  extraEnvs:  
    - name: <your-variable-name>  
      value: "<your-variable-value>"  
  ...
```

Configuration of extra environment variables for the executors

```
executor:  
  extraEnvs:  
    - name: <your-variable-name>  
      value: "<your-variable-value>"  
  ...
```

Environment variables defined as shown will be applied to Executors of both [Classic Engines](/current/deploy-dremio/configuring-kubernetes/#configuration-of-classic-engines) and [New Engines](/current/deploy-dremio/managing-engines-kubernetes).

### Advanced Load Balancer Configuration

Dremio will create a public load balancer by default, and the Dremio Client service will provide an external IP to connect to Dremio. For more information, see [Connecting to the Dremio Console](/current/deploy-dremio/deploy-on-kubernetes#connecting-to-the-dremio-console).

* **Private Cluster** - For private Kubernetes clusters (no public endpoint), set `internalLoadBalancer: true`. Add this configuration under the parent as shown in the following example:

  Configuration of an internal load balancer

  ```
  service:  
    type: LoadBalancer  
    internalLoadBalancer: true  
    ...
  ```
* **Static IP** - To define a static IP for your load balancer, set `loadBalancerIP: <your-static-IP>`. If unset, an available IP will be assigned upon creation of the load balancer. Add this configuration under the parent as shown in the following example:

  Configuration of a static IP for the load balancer

  ```
  service:  
    type: LoadBalancer  
    loadBalancerIP: <your-desired-ip>  
    ...
  ```

  tip

  This can be helpful if DNS is configured to expect Dremio to have a specific IP.
* **Session Affinity** - If leveraging scale-out coordinators, set this to `ClientIP`, otherwise leave unset. Add this configuration under the parent as shown in the following example:

  Configuration of session affinity for scale-out coordinators

  ```
  service:  
    type: LoadBalancer  
    sessionAffinity: ClientIP  
    ...
  ```

#### Additional Load Balancer Configuration for Amazon EKS in Auto Mode

If deploying Dremio to Amazon EKS (Elastic Kubernetes Service) in Auto Mode, you need to add service annotations for the load balancer to start (for more information, see [Use Service Annotations to configure Network Load Balancers](https://docs.aws.amazon.com/eks/latest/userguide/auto-configure-nlb.html)). Add this configuration under the parent as shown in the following example:

Configuration of service annotations for Amazon EKS in Auto Mode

```
service:  
  type: LoadBalancer  
  annotations:  
    service.beta.kubernetes.io/aws-load-balancer-scheme: internet-facing  
  ...
```

### Advanced TLS Configuration for OpenSearch

Dremio generates Transport Level Security (TLS) certificates by default for OpenSearch, and they are rotated monthly. However, if you want to have your own, you need to create two secrets containing the relevant certificates. The format of the secrets is different from the other TLS secrets shown on this page, and the `tls.crt`, `tls.key`, and `ca.crt` files must be in PEM format. Use the example below as a reference to create your secrets:

Run kubetcl to create two secrets for your own TLS certificates for OpenSearch

```
kubectl create secret generic opensearch-tls-certs \  
  --from-file=tls.crt --from-file=tls.key --from-file=ca.crt  
  
kubectl create secret generic opensearch-tls-certs-admin \  
  --from-file=tls.crt --from-file=tls.key --from-file=ca.crt
```

Add the snippet below to the `values-overrides.yaml` file before deploying Dremio. Because OpenSearch requires TLS, if certificate generation is disabled, you must provide a certificate.

Configuration of TLS certificates for OpenSearch

```
opensearch:  
  tlsCertsSecretName: <opensearch-tls-certs>  
  disableTlsCertGeneration: true  
 ...
```

### Advanced Configuration of Engines

Dremio's default resource offset is `reserve-2-8`, where the first value represents 2 vCPUs and the second represents 8 GB of RAM. If you need to change this default for your created engines, add the following snippet to `values-overrides.yaml` and set the `defaultOffset` to one of the configurable offsets listed below, which are available out of the box:

* `reserve-0-0`
* `reserve-2-4`
* `reserve-2-8`
* `reserve-2-16`

The listed values are keys and thus must be provided in this exact format in the snippet below.

Configuration of the default resource offset for engines with an example value

```
engine:  
  options:  
    resourceAllocationOffsets:  
      defaultOffset: reserve-2-8  
  ...
```

### Configuration of Classic Engines

note

* You should only use classic engines if the new ones introduced in Dremio 26.0 are not appropriate for your use case. Classic and new engines are not intended to be used side by side.
* Classic engines will not auto-start/auto-stop, which is only possible with the new engines.

The classic way of configuring engines is still supported, and you can add this snippet to `values-overrides.yaml` as part of the deployment. Note that this snippet is a configuration example, and you should adjust the values to your own case.

Configuration of classic engines with example values

```
executor:  
  resources:  
    requests:  
      cpu: "16"  
      memory: "120Gi"  
    limits:  
      memory: "120Gi"  
  engines: ["default"]  
  count: 3  
  volumeSize: 128Gi  
  cloudCache:  
    enabled: true  
    volumes:  
      - size: 128Gi  
  ...
```

#### Engine Overrides

Engine overrides are primarily used in conjunction with classic engines to modify the configuration of one or more named engines. By default, every engine inside the `engines` list under `executor` will be the same. The values set under `executor` act as the default for all engines. Thus, the engine overrides do not need to be exhaustive.

Configuration of overrides for an engine named 'small'

```
engineOverride:  
 small:  
   cpu: "8"  
   memory: "60Gi"  
   count: 2  
   cloudCache:  
     enabled: false
```

Engine overrides can also be used with the new engines, but only to disable the Cloud Columnar Cache (C3) option. C3 is enabled by default on all new engines, but you can choose to disable it if needed.

### Telemetry

[Telemetry](/current/admin/service-telemetry-kubernetes) egress is enabled by default. These metrics provide visibility into various components and services, ensuring optimal performance and reliability. To disable egress, add the following to your `values-override.yaml`:

Configuration to disable telemetry

```
telemetry:  
  enabled: false  
  ...
```

### Logging

By default, Dremio enables logging with a pre-defined volume size, which you can check in the `values.yaml` file by downloading Dremio's Helm chart. To override the default configuration, add the following to your `values-overrides.yaml`:

Configuration of logging

```
dremio:  
  log:  
    enabled: true  
    volume:  
      size: 10Gi  
      storageClass: ""  
  ...
```

### Disabling Parts of the Deployment

You can disable some components of the Dremio platform if their functionality does not pertain to your use case. Dremio's functionality will continue to work if any of these components described in this section are disabled.

#### Semantic Search

To disable Semantic Search, add this configuration under the parent as shown in the following example:

Configuration to disable Semantic Search

```
opensearch:  
  enabled: false  
  replicas: 0
```

## Additional Configuration

Dremio has several configuration and binary files to define the behavior for enabling authentication via an identity provider, logging, connecting to Hive, etc. During the deployment, these files are combined and used to create a [Kubernetes ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/). This ConfigMap is, in turn, used by the Dremio deployment as the source of truth for various settings. Options can be used to embed these in the `values-override.yaml` configuration file.

To inspect Dremio's configuration files or perform a more complex operation not shown here, see Downloading Dremio's Helm Charts.

### Additional Config Files

Use the `configFiles` option to add configuration files to your Dremio deployment. You can add multiple files, each of which is a key-value pair. The key is the file name, and the value is the file content. These can be TXT, XML, or JSON files. For example, here is how to embed the configuration for Hashicorp Vault, followed by a separate example file:

Configuration of additional configuration files with example JSONs

```
dremio:  
  configFiles:  
    vault_config.json: |  
      {  
        "vaultUrl": "https://your-vault.com",  
        "namespace": "optional/dremio/global/vault/namespace",  
        "auth": {  
          "kubernetes": {  
            "vaultRole": "dremio-vault-role",  
            "serviceAccountJwt": "file:///optional/custom/path/to/serviceAccount/jwt",  
            "loginMountPath": "optional/custom/kubernetes/login/path"  
          }  
        }  
      }  
    another_config.json: |  
      {  
        "key-in-this-file": "content-of-this-key"  
      }  
  ...
```

### Additional Config Variables

Use the `dremioConfExtraOptions` option to add new variables to your Dremio deployment. For example, here is how to enable Transport Layer Security (TLS) between executors and coordinators, leveraging auto-generated self-signed certificates.

Configuration of additional configuration variables with an example to enable TLS

```
dremio:  
  dremioConfExtraOptions:  
    "services.fabric.ssl.enabled": true  
    "services.fabric.ssl.auto-certificate.enabled": true  
  ...
```

### Additional Java Truststore

Use the `trustStore` option under `advancedConfigs` to provide the password and content of a Java truststore file. The content must be base64-encoded. To extract the encoded content, you can use `cat truststore.jks | base64`. Add this configuration under the parents as shown in the following example:

Configuration of an additional Java truststore with a truststore password

```
dremio:  
  advancedConfigs:  
    trustStore:  
      enabled: true  
      password: "<your-truststore-password>"  
      binaryData: "base64EncodedBinaryContent"
```

### Additional Config Binary Files

Use the `configBinaries` option to provide binary configuration files. Provided content must be base64-encoded. Add this configuration under the parents as shown in the following example:

Configuration of additional binary configuration files

```
dremio:    
  configBinaries:  
    custom-binary.conf: "base64EncodedBinaryContent"  
  ...
```

### Hive

Use the `hive2ConfigFiles` option to configure Hive 2. Add this configuration under the parents as shown in the following example:

Configuration of Hive 2 with an example for the `hive-site.xml` file

```
dremio:  
  hive2ConfigFiles:  
    hive-site.xml: |  
      <?xml version="1.0" encoding="UTF-8"?>  
      <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>  
      <configuration>  
        <property>  
          <n>hive.metastore.uris</n>  
          <value>thrift://hive-metastore:9083</value>  
        </property>  
      </configuration>  
  ...
```

Use the `hive3ConfigFiles` option to configure Hive 3. Add this configuration under the parents as shown in the following example:

Configuration of Hive 3 with an example for the `hive-site.xml` file

```
dremio:  
  hive3ConfigFiles:  
    hive-site.xml: |  
      <?xml version="1.0" encoding="UTF-8"?>  
      <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>  
      <configuration>  
        <property>  
          <n>hive.metastore.uris</n>  
          <value>thrift://hive3-metastore:9083</value>  
        </property>  
      </configuration>  
  ...
```

## References

### Recommended Resources Configuration

The table in this section contains the recommended values for resources requests and volume size to configure Dremio components. In the `values-overrides.yaml` file, set the following values:

Configuration of resources in Dremio components

```
  resources:  
    requests:  
      memory: # Refer to the Memory column in the tables below for recommended values  
      cpu: # Refer to the CPU column in the tables below for recommended values  
  volumeSize: # Refer to the Volume Size column in the tables below for recommended values
```

Dremio recommends the following configuration values:

* Production Configuration
* Minimal Configuration

Dremio recommends the following configuration values to operate in a production environment:

| Dremio Component | Memory | CPU | Volume Size | Pod Count |
| --- | --- | --- | --- | --- |
| Coordinator | 64Gi | 32 | 512Gi | 1 |
| Catalog Server | 8Gi | 4 | - | 1 |
| Catalog Server (External) | 8Gi | 4 | - | 1 |
| Catalog Service Server | 8Gi | 4 | - | 1 |
| Engine Operator | 1Gi | 1 | - | 1 |
| OpenSearch | 16Gi | 2 | 100Gi | 3 |
| MongoDB | 4Gi | 8 | 512Gi1 | 3 |
| NATS | 1Gi | 700m | - | 3 |
| ZooKeeper | 1Gi | 500m | - | 3 |
| Open Telemetry | 1Gi | 1 | - | 1 |
| M Engine | 120Gi | 16 | 521Gi | 4 |

1 You can use a smaller volume size if you do not heavily use Iceberg.

The following configuration will deploy a functional Dremio Platform, sized to fit onto a more modest cluster. It is appropriate for a single user to check out Dremio's various features, leveraging our sample data set. For any multi-user and performance-oriented evaluation, the Production Configuration should be used.

| Dremio Component | Memory | CPU | Volume Size | Pod Count |
| --- | --- | --- | --- | --- |
| Coordinator | 8Gi | 2 | 20Gi | 1 |
| Catalog Server | 1Gi | 1 | - | 1 |
| Catalog Server (External) | 1Gi | 1 | - | 1 |
| Catalog Service Server | 1Gi | 1 | - | 1 |
| Engine Operator | 1Gi | 1 | - | 1 |
| OpenSearch | 3Gi | 1500m | 10Gi | 3 |
| MongoDB | 1Gi | 1 | 10Gi | 3 |
| NATS | 1Gi | 700m | - | 3 |
| ZooKeeper | 1Gi | 500m | - | 1 |
| Open Telemetry | 1Gi | 1 | - | 1 |
| XS Engine | 8Gi | 2 | 20Gi | 1 |

Expand the widget below for Dremio platform components resource YAML snippets:

Dremio Platform Resource Configuration YAML

Coordinator

```
coordinator:  
  resources:  
    requests:  
      cpu: "32"  
      memory: "64Gi"  
    limits:  
      memory: "64Gi"  
  volumeSize: "512Gi"
```

Catalog Server

```
catalog:  
  requests:  
    cpu: "4"  
    memory: "8Gi"  
  limits:  
    cpu: "4"  
    memory: "8Gi"
```

Catalog Service Server

```
catalogservices:  
  resources:  
    requests:  
      cpu: "4"  
      memory: "8Gi"  
    limits:  
      cpu: "4"  
      memory: "8Gi"
```

OpenSearch

```
opensearch:  
  resources:  
    requests:  
      memory: "16Gi"  
      cpu: "2"  
    limits:  
      memory: "16Gi"  
      cpu: "2"
```

MongoDB

```
mongodb:  
  resources:  
    requests:  
      cpu: "2"  
      memory: "2Gi"  
    limits:  
      cpu: "4"  
      memory: "2Gi"  
  storage:  
    resources:  
      requests:  
        storage: "512Gi"
```

NATS

```
nats:  
  resources:  
    requests:  
      cpu: "500m"  
      memory: "1024Mi"  
    limits:  
      cpu: "750m"  
      memory: "1536Mi"
```

ZooKeeper

```
zookeeper:  
  resources:  
    requests:  
      cpu: "500m"  
      memory: "1Gi"  
    limits:  
      memory: "1Gi"  
  volumeSize: "10Gi"
```

Open Telemetry

```
telemetry:  
  resources:  
    requests:  
      cpu: "1"  
      memory: "1Gi"  
    limits:  
      cpu: "2"  
      memory: "2Gi"
```

### Creating a TLS Secret

If you have enabled Transport Layer Security (TLS) in your `values-overrides.yaml`, the corresponding secrets must be created before deploying Dremio. To create a secret, run the following command:

Run kubectl to create a TLS secret

```
kubectl create secret tls <your-tls-secret-name> --key privkey.pem --cert cert.pem
```

For more information, see [kubectl create secret tls](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_tls/#synopsis) in the Kubernetes documentation.

caution

TLS for OpenSearch requires a secret of a different makeup. See Advanced TLS Configuration for OpenSearch.

### Configuring the Distributed Storage

Dremio’s distributed store uses scalable and fault-tolerant storage, and it is configured as follows:

1. In the `values-overrides.yaml` file, find the section with `distStorage:` and `type:`

   Configuration of the distributed storage

   ```
   distStorage:  
     type: "<your-dist-store-type>"  
     ...
   ```
2. In `type:`, configure your storage provider with one of the following values:

   * `"aws"` - For Amazon S3 or S3-compatible storage.
   * `"azureStorage"` - For Azure Storage.
   * `"gcp"` - For Google Cloud Storage (GCS) in Google Cloud Platform (GCP).
3. Select the tab below for the storage provider you chose in step 2, and follow the example to configure your distributed storage:

note

Distributed storage is also used to store Open Catalog backups. You may be required to provide two authentication methods to enable storage of these backups.

* Amazon S3 and S3-Compatible
* Azure Storage
* Google Cloud Storage

For Amazon S3 and S3-Compatible, select the tab below for your type of authentication:

* Metadata
* Access Key
* AWS Profile
* EKS Pod Identity

Dremio uses the Identity and Access Management (IAM) role to retrieve the credentials to authenticate. Metadata is only supported in Amazon Web Services Elastic Kubernetes Service (AWS EKS) and requires that the EKS worker node IAM role is configured with sufficient access rights.

Add the configuration under the parent as shown in the following example:

Metadata authentication for the distributed storage

```
distStorage:  
  type: "aws"  
  aws:  
    bucketName: "<your-bucket-name>"  
    path: "/"  
    authentication: "metadata"  
    region: "<your-bucket-region>"  
    #  
    # Extra Properties  
    # Use the extra properties block to provide additional parameters  
    # to configure the distributed storage in the generated core-site.xml file.  
    #  
    #extraProperties: |  
    #  <property>  
    #    <name>the-property-name</name>  
    #    <value>the-property-value</value>  
    #  </property>
```

Where:

* `bucketName` - The name of your S3 bucket for distributed storage.
* `path` - The path relative to your bucket to create Dremio's directories.
* `authentication` - Set as `"metadata"`.
* `region` - The AWS region in which your bucket resides. Required even if using S3-compatible.
* `extraProperties` - Additional parameters to configure the distributed storage in the generated `core-site.xml` file. Important for S3-compatible and customer-managed KMS encryption.

Dremio uses a configured Amazon Web Services (AWS) Access Key and Secret to authenticate.

Add the configuration under the parent as shown in the following example:

Access Key authentication for the distributed storage

```
distStorage:  
  type: "aws"  
  aws:  
    bucketName: "<your-bucket-name>"  
    path: "/"  
    authentication: "accessKeySecret"  
    region: "<your-bucket-region>"  
    credentials:  
      accessKey: "<your-access-key>"  
      secret: "<your-access-key-secret>"  
    #  
    # Extra Properties  
    # Use the extra properties block to provide additional parameters   
    # to configure the distributed storage in the generated core-site.xml file.  
    #  
    #extraProperties: |  
    #  <property>  
    #    <name>the-property-name</name>  
    #    <value>the-property-value</value>  
    #  </property>
```

Where:

* `bucketName` - The name of your S3 bucket for distributed storage.
* `path` - The path relative to your bucket to create Dremio's directories.
* `authentication` - Set as `"accessKeySecret"`.
* `region` - The AWS region in which your bucket resides. Required even if using S3-compatible.
* `credentials` - The credentials configuration:
  + `accessKey` - Your AWS access key ID.
  + `secret` - Your AWS access key secret.
* `extraProperties` - Additional parameters to configure the distributed storage in the generated `core-site.xml` file. Important for S3-compatible and customer-managed KMS encryption.

Dremio uses the default Amazon Web Services (AWS) profile to retrieve the credentials to authenticate.

note

You need to add an AWS Access Key to store Open Catalog backups.

Add the configuration under the parent as shown in the following example:

AWS profile authentication for the distributed storage

```
distStorage:  
  type: "aws"  
  aws:  
    bucketName: "<your-bucket-name>"  
    path: "/"  
    authentication: "awsProfile"  
    region: "<your-bucket-region>"  
    credentials:  
      awsProfileName: "default"  
      #accessKey: "<your-access-key>" for Open Catalog Backup  
      #secret: "<your-access-key-secret>" for Open Catalog Backup  
    #  
    # Extra Properties  
    # Use the extra properties block to provide additional parameters to configure the distributed  
    # storage in the generated core-site.xml file.  
    #  
    #extraProperties: |  
    #  <property>  
    #    <name>the-property-name</name>  
    #    <value>the-property-value</value>  
    #  </property>
```

Where:

* `bucketName` - The name of your S3 bucket for distributed storage.
* `path` - The path relative to your bucket to create Dremio's directories.
* `authentication` - Set as `"awsProfile"`.
* `region` - The AWS region your bucket resides in. Required even if using S3-compatible.
* `credentials` - The credentials configuration:
  + `awsProfileName` - Set as `"default"`.
  + `accessKey` - AWS access key ID for Open Catalog backup storage.
  + `secret` - AWS access key secret for Open Catalog backup storage.
* `extraProperties` - Additional parameters to configure the distributed storage in the generated `core-site.xml` file. Important for S3-compatible and customer-managed KMS encryption.

EKS Pod Identities allow for Kubernetes service accounts to be associated with an IAM role. Dremio, in turn, can use this IAM role to retrieve the credentials to authenticate. As both the coordinators and engines require access to distributed storage, both of their `ServiceAccounts` must be associated with an IAM role with sufficient access rights. By default, their `ServiceAccounts` are `dremio-coordinator`, `dremio-engine-executor` for [New Engines](/current/deploy-dremio/managing-engines-kubernetes), and (optional) `dremio-executor` for [Classic Engines](/current/deploy-dremio/configuring-kubernetes/#configuration-of-classic-engines).

Add the configuration under the parent as shown in the following example:

AWS profile authentication for the distributed storage

```
distStorage:  
  type: "aws"  
  aws:  
    bucketName: "<your-bucket-name>"  
    path: "/"  
    authentication: "podIdentity"  
    region: "<your-bucket-region>"  
    #  
    # Extra Properties  
    # Use the extra properties block to provide additional parameters to configure the distributed  
    # storage in the generated core-site.xml file.  
    #  
    #extraProperties: |  
    #  <property>  
    #    <name>the-property-name</name>  
    #    <value>the-property-value</value>  
    #  </property>
```

Where:

* `bucketName` - The name of your S3 bucket for distributed storage.
* `path` - The path relative to your bucket to create Dremio's directories.
* `authentication` - Set as `"podIdentity"`.
* `region` - The AWS reigon your bucket resides. Required even if using S3-Compatible.
* `extraProperties` - Additional parameters to configure the distributed storage in the generated `core-site.xml` file. Important for S3-compatible and customer-managed KMS encryption.

**Extra Properties**

Example extra properties for S3-compatible storage and for providing a customer-managed KMS key for an encrypted bucket.

S3-Compatible extra properties

```
extraProperties: |  
  <property>  
    <name>fs.s3a.endpoint</name>  
    <value>0.0.0.0</value>  
  </property>  
  <property>  
    <name>fs.s3a.path.style.access</name>  
    <value>true</value>  
  </property>  
  <property>  
    <name>dremio.s3.compat</name>  
    <value>true</value>  
  </property>  
  <property>  
    <name>fs.s3a.connection.ssl.enabled</name>  
    <value>false</value>  
  </property>
```

Customer-managed KMS extra properties

```
extraProperties: |  
  <property>  
      <name>fs.s3a.connection.ssl.enabled</name>  
      <value>true</value>  
  </property>  
  <property>  
      <name>fs.s3a.server-side-encryption-algorithm</name>  
      <value>SSE-KMS</value>  
  </property>  
  <property>  
      <name>fs.s3a.server-side-encryption.key</name>  
      <value>KEY_ARN</value>  
  </property>
```

For Azure Storage, select the tab below for your type of authentication:

* Access Key
* Entra ID

Dremio uses the configured Azure Storage account access key to authenticate.

Add the configuration under the parent as shown in the following example:

Access Key authentication for the distributed storage

```
distStorage:  
  type: "azureStorage"  
  azureStorage:  
    accountName: "<your-account-name>"  
    authentication: "accessKey"  
    filesystem: "<your-blob-container>"  
    path: "/"  
    credentials:  
      accessKey: "<your-access-key>"  
    #  
    # Extra Properties  
    # Use the extra properties block to provide additional parameters to configure the distributed  
    # storage in the generated core-site.xml file.  
    #  
    #extraProperties: |  
    #  <property>  
    #    <name>the-property-name</name>  
    #    <value>the-property-value</value>  
    #  </property>
```

Where:

* `accountName` - The name of your storage account.
* `authentication` - Set as `"accessKey"`.
* `filesystem` - The name of your blob container to use within the storage account.
* `path` - The path relative to the filesystem to create Dremio's directories.
* `credentials` - The credentials configuration:
  + `accessKey` - Your Azure Storage account access key.
* `extraProperties` - Additional parameters to configure the distributed storage in the generated `core-site.xml` file.

Dremio uses the configured Azure client ID (application ID), Microsoft Entra ID token endpoint, and Azure client secret (application password) to authenticate.

note

You need to add an Azure Access Key to store Dremio Catalog backups.

Add the configuration under the parent as shown in the following example:

Entra ID authentication for the distributed storage

```
distStorage:  
  type: "azureStorage"  
  azureStorage:  
    accountName: "<your-account-name>"  
    authentication: "entraID"  
    filesystem: "<your-blob-container>"  
    path: "/"  
    credentials:  
      clientId: "<your-application-client-id>"  
      tokenEndpoint: "<your-token-endpoint>"  
      clientSecret: "<your-client-secret>"  
      #accessKey: "<your-access-key>" for Open Catalog Backup.  
    #  
    # Extra Properties  
    # Use the extra properties block to provide additional parameters to configure the distributed  
    # storage in the generated core-site.xml file.  
    #  
    #extraProperties: |  
    #  <property>  
    #    <name>the-property-name</name>  
    #    <value>the-property-value</value>  
    #  </property>
```

Where:

* `accountName` - The name of your storage account.
* `authentication` - Set as `"entraID"`.
* `filesystem` - The name of your blob container to use within the storage account.
* `path` - The path relative to the filesystem to create Dremio's directories.
* `credentials` - The credentials configuration:
  + `clientId` - Your Azure client ID (application ID).
  + `tokenEndpoint` - Your Microsoft Entra ID token endpoint.
  + `clientSecret` - Your Azure client secret (application password).
  + `accessKey` - Your access key for Open Catalog Backup.
* `extraProperties` - Additional parameters to configure the distributed storage in the generated `core-site.xml` file.

**Extra Properties**

Example extra properties to configure the Azure Storage data source to access data on the Azure Government Cloud platform.

Azure Government Cloud endpoint extra properties

```
extraProperties: |  
  <property>  
      <name>fs.azure.endpoint</name>  
      <description>The azure storage endpoint to use.</description>  
      <value>dfs.core.usgovcloudapi.net</value>  
  </property>
```

For Google Cloud Storage (GCS) in Google Cloud Platform (GCP), select the tab below for your type of authentication:

* Automatic
* Service Account

Dremio uses Google Application Default Credentials to authenticate. This is platform-dependent and may not be available in all Kubernetes clusters.

note

You need to add a service account key to store Open Catalog backups.

Add the configuration under the parent as shown in the following example:

```
distStorage:  
  type: "gcp"  
  gcp:  
    bucketName: "<your-bucket-name>"  
    path: "/"  
    authentication: "auto"  
    #credentials: for Open Catalog backup.  
    # clientEmail: "<your-email-for-the-service-account>"  
    # privateKey: |-  
    #    -----BEGIN PRIVATE KEY-----\n <your-full-private-key-value> \n-----END PRIVATE KEY-----\n
```

Where:

* `bucketName` - The name of your GCS bucket for distributed storage.
* `path` - The path relative to the bucket to create Dremio's directories.
* `authentication` - Set as `"auto"`.
* `credentials` - The credentials configuration, for Open Catalog backup:
  + `clientEmail` - Your email for the service account that has access to the GCS bucket, for Open Catalog backup.
  + `privateKey` - Your full private key value, for Open Catalog backup.

Dremio uses a JSON key file generated from the GCP console to authenticate.

Add the configuration under the parent as shown in the following example:

```
distStorage:  
  type: "gcp"  
  gcp:  
    bucketName: "<your-bucket-name>"  
    path: "/"  
    authentication: "serviceAccountKeys"  
    credentials:  
      projectId: "<your-project-id>"  
      clientId: "<your-client-id>"  
      clientEmail: "<your-email-for-the-service-account>"  
      privateKeyId: "<your-private-key-id>"  
      privateKey: |-  
        -----BEGIN PRIVATE KEY-----\n <your-full-private-key-value> \n-----END PRIVATE KEY-----\n
```

Where:

* `bucketName` - The name of your GCS bucket for distributed storage.
* `path` - The path relative to your bucket to create Dremio's directories.
* `authentication` - Set as `"serviceAccountKeys"`.
* `credentials` - The credentials configuration:
  + `projectId` - Your GCP Project ID that the GCS bucket belongs to.
  + `clientId` - Your Client ID for the service account that has access to the GCS bucket.
  + `clientEmail` - Your email for the service account that has access to the GCS bucket.
  + `privateKeyId` - Your private key ID for the service account that has access to GCS bucket.
  + `privateKey` - Your full private key value.

note

When using a GCS bucket on Google Kubernetes Engine (GKE), we recommend enabling **Workload Identity** and configuring a Kubernetes service account for Dremio with an associated workload identity that has access to the GCS bucket.

### Configuring Storage for the Open Catalog

To use the Open Catalog, configure the storage settings based on your storage provider (for example, Amazon S3, Azure Storage, or Google Cloud Storage). This configuration is required to enable support for vended credentials and to allow access to the table metadata necessary for Iceberg table operations.

1. In the `values-overrides.yaml` file, find the section to configure your storage provider under the parents, as shown in the following example:

   Configuration of the storage for the Open Catalog

   ```
   catalog:  
     storage:  
       location: <your-object-store-path>  
       type: <your-object-store-type>  
     ...
   ```
2. To configure it, select the tab for your storage provider, and follow the steps:

   * Amazon S3
   * S3-compatible
   * Azure Storage
   * Google Cloud Storage

   To use the Open Catalog with Amazon S3, do the following:

   1. Configure the access to the storage, as described in [Configure Storage Access](/current/data-sources/open-catalog/#configure-storage-access). Creating a Kubernetes secret may be required.
   2. Configure the Open Catalog in the `values-overrides.yaml` file as follows:

      Configuration of the storage for the Open Catalog in Amazon S3

      ```
      catalog:  
        storage:  
          location: s3://<your-bucket>/<your-folder>  
          type: S3  
          s3:  
            region: <bucket_region>  
            roleArn: <dremio_catalog_iam_role> // The role that was configured in the previous step  
            userArn: <dremio_catalog_user_arn> // The IAM user that was created in the previous step  
            externalId: <dremio_catalog_external_id> // The external id that was created in the previous step  
            useAccessKeys: false // Set it to true if you intend to use accessKeys.  
        ...
      ```
   3. If using EKS Pod Identities, ensure the catalog's Kubernetes `ServiceAccount`, which is `dremio-catalog-server` by default, is associated with the `userArn` which you also provided above.

   To use the Open Catalog with S3-compatible storage, do the following:

   1. Configure the access to the storage, as described in [Configure Storage Access](/current/data-sources/open-catalog/#configure-storage-access). Creating a Kubernetes secret is required.
   2. For this step, select the tab for whether the S3-compatible storage has STS support or not, and follow the instructions:

      * Has STS support
      * No STS support

      The Open Catalog uses STS as a mechanism to perform credentials vending, so configure Open Catalog in the `values-overrides.yaml` file as follows:

      caution

      roleArn must be provided even when using S3-compatible storage. A dummy value is provided in the template below.

      Configuration of the storage for the Open Catalog in S3-compatible with STS support

      ```
      catalog:  
        storage:  
          location: s3://<your-bucket/<your-folder>  
          type: S3  
          s3:  
            region: <your-bucket-region> // Optional, bucket region  
            roleArn: arn:aws:iam::000000000000:role/catalog-access-role // Mandatory, a dummy role, as shown here, must be provided  
            endpoint: <s3-compatible-server-url> // This is the S3 server url, for example, http://<minio-host>:<minio-port> for MinIO  
            stsEndpoint: <s3-compatible-sts-server-url> // This is the STS server url, for example http://<minio-host>:<minio-port> for MinIO  
            pathStyleAccess: true // Mandatory to be true  
            useAccessKeys: true // Mandatory to be true  
        ...
      ```

      Vended credentials will not work, and, in such cases, you must select `Use master storage credentials` and in the Dremio console, and provide explicit access keys for external engines where they are required.

      Once the Kubernetes secrets for the access keys have been created, configure the Open Catalog in the `values-overrides.yaml` file as follows:

      caution

      roleArn must be provided even when using S3-compatible storage. A dummy value is provided in the template below.

      Configuration of the storage for the Open Catalog in S3-compatible with no STS support

      ```
      catalog:  
        storage:  
          location: s3://<your-bucket/<your-folder>  
          type: S3  
          s3:  
            region: <your-bucket-region> // Optional, bucket region  
            roleArn: arn:aws:iam::000000000000:role/catalog-access-role // Mandatory, a dummy role, as shown here, must be provided  
            endpoint: <s3-compatible-server-url> // This is the S3 server url, for example to MinIO http://<minio-host>:<minio-port  
            pathStyleAccess: true // Mandatory to be true  
            skipSts: true // Mandatory to be true  
            useAccessKeys: true // Mandatory to be true  
        ...
      ```

   To use the Open Catalog with Azure Storage, do the following:

   1. Configure the access to the storage, as described in [Configure Storage Access](/current/data-sources/open-catalog/#configure-storage-access).
   2. Configure the Open Catalog in the `values-overrides.yaml` file as follows:

      Configuration of the storage for the Open Catalog in Azure Storage 

      ```
      catalog:  
        storage:  
          location: abfss://<your-container-name>@<your-storage-account>.dfs.core.windows.net/<path>  
          type: azure  
          azure:  
            tenantId: <your-azure-directory-tenant-id>  
            multiTenantAppName: ~ // Optional: Used only if you register an app with multi-tenants.  
            useClientSecrets: true // Has to be true  
        ...
      ```

   To use the Open Catalog with Google Cloud Storage (GCS), do the following:

   1. Configure the access to the storage, as described in [Configure Storage Access](/current/data-sources/open-catalog/#configure-storage-access).
   2. Configure the Open Catalog in the `values-overrides.yaml` file as follows:

      Configuration of the storage for the Open Catalog in Google Cloud Storage

      ```
      catalog:  
        ...  
        storage:  
          location: gs://<your-bucket>/<your-path>  
          type: GCS  
          gcs:  
            useCredentialsFile: True
      ```

### Configuring TLS for Open Catalog External Access

For clients connecting to the Open Catalog from outside the namespace, Transport Layer Security (TLS) can be enabled for Open Catalog external access as follows:

1. Enable external access with TLS and provide the TLS secret. See the section Creating a TLS Secret.
2. In the `values-overrides.yaml` file, find the Open Catalog configuration section:

   Configuration section for the Open Catalog

   ```
   catalog:  
     ...
   ```
3. Configure TLS for the Open Catalog as follows:

   Configuration of TLS for external access to the Open Catalog

   ```
   catalog:  
     externalAccess:  
       enabled: true  
       tls:  
         enabled: true  
         secret: <dremio-tls-secret-catalog></dremio-tls-secret-catalog>  
     ...
   ```

### Configuring Open Catalog When the Coordinator Web is Using TLS

When the Dremio coordinator uses Transport Layer Security (TLS)for Web access (i.e., when `coordinator.web.tls` is set to `true`), the Open Catalog external access must be configured appropriately, or client authentication will fail. For that, configure the Open Catalog as follows:

1. In the `values-overrides.yaml` file, find the Open Catalog configuration section:

   Configuration section for the Open Catalog

   ```
   catalog:  
     ...
   ```
2. Configure the Open Catalog as follows:

   Configuration of the Open Catalog when the coordinator web is using TLS

   ```
   catalog:  
     externalAccess:  
       enabled: true  
       authentication:  
         authServerHostname: dremio-master-0.dremio-cluster-pod.{{ .Release.Namespace }}.svc.cluster.local  
     ...
   ```

   The `authServerHostname` must match the CN (or the SAN) field of the (master) coordinator Web TLS certificate.

   In case it does not match the CN or SAN fields of the TLS certificate, as a last resort, it is possible to disable hostname verification (`disableHostnameVerification: true`):

   Configuration of the Open Catalog with hostname verification disabled

   ```
   catalog:  
     externalAccess:  
       enabled: true  
       authentication:  
         authServerHostname: dremio-master-0.dremio-cluster-pod.{{ .Release.Namespace }}.svc.cluster.local  
         disableHostnameVerification: true  
     ...
   ```

## Downloading Dremio's Helm Charts

You can download Dremio's Helm charts to implement advanced configurations beyond those outlined in this topic.

However, please proceed with caution. Modifications made without a clear understanding can lead to unexpected behavior and compromise the Dremio Support team's ability to provide effective assistance.

To ensure success, Dremio recommends engaging with the Professional Services team through your Account Executive or Customer Success Manager. Please note that such engagements may require additional time and could involve consulting fees.

To download Dremio’s Helm charts, use the following command:

Run helm pull to download Dremio’s Helm charts

```
helm pull oci://quay.io/dremio/dremio-helm --version <tag> --untar
```

Where:

* (Optional) `--version <tag>` - The Helm chart version to pull. For example, `--version 3.0.0`. If not specified, the latest version is pulled.

The command creates a new local directory called `dremio-helm` containing the Helm charts.

For more information on the command, see [Helm Pull](https://helm.sh/docs/helm/helm_pull/) in Helm's documentation.

### Overriding Additional Values

After completing the `helm pull`:

1. Find the `values.yaml` file, open it, and check the configurations you want to override.
2. Copy what you want to override from the `values.yaml` to `values-overrides.yaml` and configure the file with your values.
3. Save the `values-overrides.yaml` file.

Once done with the configuration, deploy Dremio to Kubernetes via the OCI Repo. See how in [Deploying Dremio to Kubernetes](/current/deploy-dremio/deploy-on-kubernetes).

### Manual Modifications to Deployment Files

important

For modifications in these files to take effect, you need to install Dremio using a local version of the Helm charts. Thus, the `helm install` command must reference a local folder, not the OCI repo like Quay. For more information and sample commands, see [Helm install](https://helm.sh/docs/helm/helm_install/).

After completing the `helm pull`, you can edit the charts directly. This may be necessary to add deployment-specific modifications not catered for in the Additional Configuration section. These would typically require modifications to files in the `/config` directory. Any customizations to your Dremio environment are propagated to all the pods when installing or upgrading the deployment.

Was this page helpful?

[Previous

Deploy on Kubernetes](/current/deploy-dremio/deploy-on-kubernetes)[Next

Managing Engines](/current/deploy-dremio/managing-engines-kubernetes)

* Configure Your Values
  + License
  + Pull Secret
  + Coordinator
    - Resource Configuration
    - Identity Provider
    - Transport Level Security
  + Coordinator's Distributed Storage
  + Open Catalog
* Configuring Your Values - Advanced
  + OpenShift
  + Dremio Platform Images
  + Scale-out Coordinators
  + Configuring Kubernetes Pod Metadata (including Node Selector)
  + Configuring Pods Priority
  + Configuring Extra Environment Variables
  + Advanced Load Balancer Configuration
    - Additional Load Balancer Configuration for Amazon EKS in Auto Mode
  + Advanced TLS Configuration for OpenSearch
  + Advanced Configuration of Engines
  + Configuration of Classic Engines
    - Engine Overrides
  + Telemetry
  + Logging
  + Disabling Parts of the Deployment
    - Semantic Search
* Additional Configuration
  + Additional Config Files
  + Additional Config Variables
  + Additional Java Truststore
  + Additional Config Binary Files
  + Hive
* References
  + Recommended Resources Configuration
  + Creating a TLS Secret
  + Configuring the Distributed Storage
  + Configuring Storage for the Open Catalog
  + Configuring TLS for Open Catalog External Access
  + Configuring Open Catalog When the Coordinator Web is Using TLS
* Downloading Dremio's Helm Charts
  + Overriding Additional Values
  + Manual Modifications to Deployment Files

---

# Source: https://docs.dremio.com/current/deploy-dremio/managing-engines-kubernetes

Version: current [26.x]

On this page

# Managing Engines in Kubernetes Enterprise

note

This feature is for Enterprise Edition only.
For Community Edition, see [Configuration of Classic Engines](/current/deploy-dremio/configuring-kubernetes/#configuration-of-classic-engines).

Dremio supports the ability to provision multiple separate execution engines in Kubernetes from a Dremio main coordinator node, and automatically start and stop based on workload requirements at runtime. This provides several benefits, including:

* Creating a new engine doesn't require restarting Dremio, which enables administrators to achieve workload isolation efficiently.
* When creating a new engine, you can use Kubernetes metadata to label engines to keep track of resources.
* Right-size execution resources for each distinct workload, instead of implementing a one-size-fits-all model.
* Easily experiment with different execution resource sizes at any scale.

To manage your engines, open the Engines page as follows:

1. Open your Dremio console.
2. Click ![The Settings icon](/images/settings-icon.png "The Settings icon") in the side navigation bar to open the Settings sidebar.
3. Select **Engines**.

![Engines page under Project Settings listing all engines.](/images/settings/engine/settings-engines.png "Engines Page")

## Monitoring Engines

You can monitor the status and properties of your engines on the Engines page.

![Engines page under Project Settings showing all the current engines and their statuses.](/images/settings/engine/settings-engines-monitoring.png "Engines Page")

Each engine has the following information available:

* **Name** - The name of the engine, which you can click to see its details. See the section about Viewing Engine Details.
* **Size** - The size configured for the engine.
* **Status** - The engine status. For more information, see the section in this topic about Engine Statuses.
* **Auto start/stop** - Whether the engine has auto start/stop enabled for autoscaling.
* **Idle period** - The idle time to auto stop when the engine has **Auto start/stop** enabled.
* **Queues** - Query queues routed to the engine.
* **Labels** - Labels associated with the engine.

## Performing Actions on Engines

While monitoring engines, you have actions you can perform on each engine through the icons displayed on the right-hand side when hovering over the engine row.

![Engines page showing the icons with the actions for each engine.](/images/settings/engine/settings-engines-actions.png "Engines Page with Actions")

### Stopping/Starting an Engine

You can click ![The stop engine icon](/images/icons/engine-stop.png "The stop engine icon")/![The start engine icon](/images/icons/engine-start.png "The start engine icon") to stop/start an engine manually at any time. Stopping an engine will cause running queries to fail while new queries will remain queued, which can also fail by timeout if the engine isn't started. To prevent query failures, reroute queries to another engine, and stop the engine only when no queries are running or queued for the engine.

note

You can enable **autoscaling on an engine** to make it stop automatically after an idle time without queries and start again automatically when new queries are issued, all without any human intervention.

Autoscaling is configured when you add an engine or edit an engine:

#### Stopping All Engines

Some complex operations, like upgrading or uninstalling Dremio, require all engines to be stopped beforehand. You can stop engines manually one by one as described above, or automate the procedure using the [Engine Management API](/current/reference/api/engine-management) to stop all engines. Expand the sample below of a bash script executing the necessary endpoints to stop all engines.

Sample bash script to stop all engines

```
#!/bin/bash  
# Check if the bearer token is provided  
if [ -z "$1" ]; then  
echo "Error: Bearer token is required."  
exit 1  
fi  
BEARER_TOKEN=$1  
BASE_URL=${2:-https://localhost:9047}  
# Make an HTTP GET request to retrieve engine IDs  
RESPONSE=$(curl -k -s -H "Authorization: Bearer $BEARER_TOKEN" "$BASE_URL/api/v3/engines")  
# Check if the response contains the "id" field  
if ! echo "$RESPONSE" | grep -q '"id"'; then  
echo "Error: No 'id' field found in the response."  
exit 1  
fi  
# Extract IDs from the response  
IDS=$(echo "$RESPONSE" | jq -r '.data[] | .id')  
# Loop through each ID and make an HTTP PUT request  
for ID in $IDS; do  
RESPONSE=$(curl -k -s -o /dev/null -w "%{http_code}" -X PUT -H "Authorization: Bearer $BEARER_TOKEN" "$BASE_URL/api/v3/engines/$ID/stop")  
if [ "$RESPONSE" -eq 200 ]; then  
    echo "Successfully stopped engine with ID: $ID"  
else  
    echo "Failed to stop the engine with ID: $ID, HTTP status code: $RESPONSE"  
fi  
done  
echo "All engines processed."
```

### Editing the Engine Settings

You can click ![The edit engine icon](/images/icons/engine-edit.png "The edit engine icon") to edit the engine settings. After saving the new settings, the engine may restart, causing running queries to fail and new queries to be queued.

![Edit engine showing the general settings.](/images/settings/engine/settings-engine-edit.png "Edit Engine - General Settings")

note

The name of the engine must follow these rules:

* Must start with a lowercase alphanumeric character (`[a-z0-9]`).
* Must end with a lowercase alphanumeric character (`[a-z0-9]`).
* Must contain only lowercase alphanumeric characters or a hyphen (`[\-a-z0-9]`).
* Must be under 30 characters in length.
* Must be unique and not previously used for any existing or deleted engines.

### Deleting an Engine

You can click ![The delete engine icon](/images/icons/engine-delete.png "The delete engine icon") to delete an engine. Deleting an engine will cause running, queued, and new queries to fail. To prevent query failures, you can reroute queries to another engine, and only delete when no more queries are running or queued for the engine.

## Viewing Engine Details

While monitoring engines, if you need to know more details about engines, click the engine's name to view all the information about it.

![Engine details page showing all the information about the engine.](/images/settings/engine/settings-engine-details.png "Engine Details Page")

On this page, you will also find a set of buttons at the top to delete the engine, stop/start the engine, and edit the engine settings.

## Adding an Engine

You can create more engines by clicking **Add Engine** at the top-right corner of the Engines page.

![The general settings to add a new engine.](/images/settings/engine/settings-new-engine.png "Adding a New Engine - General Settings")

In the New engine dialog, do the following:

1. Fill out the **General** section:

   1. **Name** - Type the name of the engine. Use a meaningful name that helps you to identify the engine better. For example, `low-cost-query`.

      note

      The name of the engine must follow these rules:

      * Must start with a lowercase alphanumeric character (`[a-z0-9]`).
      * Must end with a lowercase alphanumeric character (`[a-z0-9]`).
      * Must contain only lowercase alphanumeric characters or a hyphen (`[\-a-z0-9]`).
      * Must be under 30 characters in length.
      * Must be unique and not previously used for any existing or deleted engines.
   2. **CPU** and **Size** – Select the number of CPUs per executor pod and the size of the engine.
      Dremio provides nine engine sizes, each with two CPU options targeting 16 or 32 CPU nodes. By default, Dremio will subtract 2 CPUs and 8 GB of memory from its request, resulting in requests for 14 or 30 CPUs and 120 GB of memory. This adjustment helps optimize the packing of executors on the most common node sizes. The table below shows the engine sizes:

      | Engine Size | Executors per Replica | Memory per Executor |
      | --- | --- | --- |
      | 2XSmall | 1 | 56 GB |
      | XSmall | 1 | 120 GB |
      | Small | 2 | 120 GB |
      | Medium | 4 | 120 GB |
      | Large | 8 | 120 GB |
      | XLarge | 12 | 120 GB |
      | 2XLarge | 16 | 120 GB |
      | 3XLarge | 24 | 120 GB |
      | 4XLarge | 32 | 120 GB |
   3. **Automatically start/stop** - If checked, the engine automatically stops after the specified idle time and automatically starts when new queries are issued to the engine. If not checked, the engine only stops and starts through manual intervention. By default, this setting is checked and the engine stops automatically after `15 min` of idle time. For more information, see the section Stopping/Starting an Engine.
   4. (Optional) Expand **Advanced Options** for further settings.

      ![The advanced options to add a new engine.](/images/settings/engine/settings-new-engine-advanced-options.png "Adding a New Engine - Advanced Options")

      Fill out the advanced options as follows:

      1. **Cloud cache volume (c3)** - Specify the amount of local storage for caching data.
      2. **Spill volume** - Specify the disk size allocated for temporary storage when operations exceed memory limits.
2. (Optional) Select **Kubernetes pod metadata** to define pod metadata for the engine, such as labels, annotations, node selectors, and tolerations. Define those values with care and foreknowledge of expected entries because any misconfiguration may result in Kubernetes being unable to start the executors that make up the engine.

   ![The metadata to add an engine.](/images/settings/engine/settings-new-engine-pod-metadata.png "Adding a New Engine - Metadata Settings")

   Fill out the pod's metadata with:

   1. **Labels** - Add labels as key/value pairs to identify and organize pods. Use them to group, filter, and select subsets of resources efficiently.

      note

      The engine label must follow these rules:

      * Must start with an alphanumeric character ([a-z0-9]).
      * Must end with an alphanumeric character ([a-z0-9]).
      * Must contain only lowercase alphanumeric characters, a hyphen, or a underscore ([-\_a-z0-9]).
      * The maximum length is 63 characters.
   2. **Annotations** - Add annotations as key/value pairs to store non-identifying metadata, such as build information or pointers to logging services. Unlike labels, they're not used for selection or grouping.

      note

      The engine annotation must follow these rules:

      * Must be UTF-8 encoded and can include any valid UTF-8 character.
      * Can be in plain text, JSON, or any other UTF-8 compatible format.
      * The maximum size is 256KB.
      * The maximum size of all engine annotations is 1MB.
   3. **Node selectors** - Add node selectors as key/value pairs for node-specific constraints to schedule pods on nodes matching specified labels. Use this to target nodes with specific configurations or roles.
   4. **Tolerations** - Add tolerations to allow pods to be scheduled on nodes with matching taints, but they don’t restrict scheduling to only those nodes; the pod can still land on a node without the taint.
3. Click **Add** to add the engine.

The newly added engine will be displayed in the listed engines.

![Engines page showing the current engines, which now includes the newly added engine.](/images/settings/engine/settings-new-engine-added.png "Engines Page with the Newly Added Engine")

## Engine Statuses

The following table describes each engine status:

| Status | Icon | Description |
| --- | --- | --- |
| Starting | The starting engine icon | The engine is starting. This is the initial state of an engine after being created. New queries are queued to be processed. |
| Running | The running engine icon | The engine is running. New queries are queued and processed. |
| Stopping | The stopping engine icon | The engine is stopping. Running queries will fail. New queries will remain queued, which can also fail by timeout if the engine isn't started. |
| Stopped | The stopped engine icon | The engine is stopped. New queries will remain queued, which can fail by timeout if the engine isn't started. |
| Recovering | The recovering engine icon | The engine is recovering. New queries will remain queued, which can fail by timeout if the engine doesn't recover. |
| Failed | The failed engine icon | The engine failed. New queries will remain queued, which can fail by timeout if the engine doesn't start. |

## Related Topics

* [Engine Management API](/current/reference/api/engine-management/) - The API to manage your engines using REST API calls.
* [sys.engines](/current/reference/sql/system-tables/engines/) - The system table to query for information about your engines.
* [Audit Logs](/current/security/auditing/) - Audit logs for your engines.

Was this page helpful?

[Previous

Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/)[Next

Other Options](/current/deploy-dremio/other-options/)

* Monitoring Engines
* Performing Actions on Engines
  + Stopping/Starting an Engine
  + Editing the Engine Settings
  + Deleting an Engine
* Viewing Engine Details
* Adding an Engine
* Engine Statuses
* Related Topics

---

# Source: https://docs.dremio.com/current/deploy-dremio/other-options/

Version: current [26.x]

# Other Deployment Options

Besides the [Kubernetes deployment](/current/deploy-dremio/deploy-on-kubernetes), there are other alternative supported options for deploying Dremio:

* [Hadoop Deployment (YARN)](/current/deploy-dremio/other-options/yarn-hadoop) - Deploy Dremio on a Hadoop cluster using YARN.
* [Dremio on Your Infrastructure](/current/deploy-dremio/other-options/standalone/) - Deploy Dremio as a standalone cluster.

Was this page helpful?

[Previous

Managing Engines](/current/deploy-dremio/managing-engines-kubernetes)[Next

Dremio with Hadoop](/current/deploy-dremio/other-options/yarn-hadoop)

---

# Source: https://docs.dremio.com/current/deploy-dremio/kubernetes-environments/

Version: current [26.x]

On this page

# Kubernetes Environments for Dremio

Dremio is designed to run Kubernetes environments, providing enterprise-grade data lakehouse capabilities. To successfully [deploy Dremio on Kubernetes](/current/deploy-dremio/deploy-on-kubernetes), you need a compatible hosted Kubernetes environment.

Dremio is tested and supported on the following Kubernetes environments:

* Elastic Kubernetes Service (EKS)
* Azure Kubernetes Service (AKS)
* Google Kubernetes Engine (GKE)
* Red Hat OpenShift

The sections on this page detail recommendations for AWS and Azure. Please use the information provided as a guide for your vendors' equivalent options.

note

If you're using a containerization platform built on Kubernetes that isn't listed here, please contact your provider and Dremio Account team to discuss compatibility and support options.

## Requirements

### Versions

Dremio requires regular updates to your Kubernetes version. You must be on an officially supported version, and preferably not one on extended support. See the following examples for AWS [Available versions on standard support](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#available-versions) and Azure [Kubernetes versions](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions).

### Recommendations

See this table for resource request recommendations of the variours parts of the deployment, [Recommended Resources Configuration](/current/deploy-dremio/configuring-kubernetes/#recommended-resources-configuration).

For a list of all Dremio engine sizes see, [Add an Engine](/current/deploy-dremio/managing-engines-kubernetes/add-an-engine). Engines will make up the lions share of any Dremio deployment.

#### Node Sizes

The following sections suggest AWS and Azure machines that could be used to meet our recommendations.

Dremio recommends having separate EKS node groups for the different components of our services to allow each node group to autoscale independently:

**Core Services**

* **Coordinators**

  For [coordinators](/current/what-is-dremio/architecture/#main-coordinator), Dremio recommends at least 32 CPUs and 64 GB of memory, hence, a `c6i.8xlarge` or `Standard_F32s_v2` is a good option, offering a CPU-to-memory ratio of 1:2. In the Helm charts, this would result in 30 CPUs and 60 GB of memory allocated to the Dremio pod.
* **Executors**

  For [executors](/current/what-is-dremio/architecture/#engines), Dremio recommends either:

  + 16 CPUs and 128 GB of memory, hence, a `r5d.4xlarge` or `Standard_E16_v5` is a good option, offering a CPU-to-memory ratio of 1:8. In the Helm charts, this results in 15 CPUs and 120 GB of memory allocated to the Dremio pod.
  + 32 CPUs and 128 GB of memory, hence, a `m5d.8xlarge` or `Standard_D32_v5` is a good option, offering a CPU-to-memory ratio of 1:4 for high-concurrency workloads. In the Helm charts, this results in 30 CPUs and 120 GB of memory allocated to the Dremio pod.

**Auxiliary Services**

* [Open Catalog](/current/what-is-dremio/architecture/#open-catalog) and [Semantic Search](/current/deploy-dremio/current/what-is-dremio/architecture/#ai-enabled-semantic-search).

Catalog is made up of 4 key components: Catalog Service, Catalog Server, Catalog External, and MongoDB. Search has one key component, OpenSearch.

Each of these components needs between 2-4 CPUs and 4-16 GB of memory; hence, a `m5d.2xlarge` or `Standard_D8_v5` is a good option and could be used to host multiple containers that are part of these services.

* ZooKeeper, NATS, Operators, and Open Telemetry:

Each of these need between 0.5-1 CPUs and 0.5-1 GB, `m5d.large`, `t2.medium`, `Standard_D2_v5` or `Standard_A2_v2` are good options and could be used to host multiple containers that are part of these services.

#### Disk Storage Class

Dremio recommends:

* For AWS, GP3 or IO2 as the storage type for all nodes.
* For Azure managed-premium as the storage type for all nodes.

Additionally, for [coordinators](/current/what-is-dremio/architecture/#main-coordinator) and [executors](/current/what-is-dremio/architecture/#engines), you can further use local NVMe SSD storage for C3 and spill on executors. For more information on storage classes, see the following resources [AWS Storage Class](https://docs.aws.amazon.com/eks/latest/userguide/create-storage-class.html) and [Azure Storage Class](https://learn.microsoft.com/en-us/azure/aks/concepts-storage).

Storage size requirements are:

* Coordinator volume #1: 128-512 GB (key-value store).
* Coordinator volume #2: 16 GB (logs).
* Executor volume #1: 128-512 GB (spilling).
* Executor volume #2: 128-512 GB (C3).
* Executor volume #3: 16 GB (logs).
* MongoDB volume: 128-512 GB.
* OpenSearch volume: 128 GB.
* Zookeeper volume: 16 GB.

### EKS Add-Ons

The following add-ons are required for EKS clusters:

* Amazon EBS CSI Driver
* EKS Pod Identity Agent

Was this page helpful?

[Previous

Deploy Dremio](/current/deploy-dremio/)[Next

Deploy on Kubernetes](/current/deploy-dremio/deploy-on-kubernetes)

* Requirements
  + Versions
  + Recommendations
  + EKS Add-Ons

---

# Source: https://docs.dremio.com/current/deploy-dremio/deploy-on-kubernetes/

Version: current [26.x]

On this page

# Deploy Dremio on Kubernetes

You can follow these instructions to deploy Dremio on Kubernetes provisioned through a cloud provider or running in an on-premises environment.

FREE TRIAL

If you are using an **Enterprise Edition free trial**, go to [Get Started with the Enterprise Edition Free Trial](/current/get-started/kubernetes-trial).

## Prerequisites

Before deploying Dremio on Kubernetes, ensure you have the following:

* A hosted Kubernetes environment to deploy and manage the Dremio cluster.  
  Each Dremio release is tested against [Amazon Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/what-is-aks), and [Google Kubernetes Engines (GKE)](https://cloud.google.com/kubernetes-engine?hl=en#how-it-works) to ensure compatibility. If you have a containerization platform built on top of Kubernetes that is not listed here, please contact your provider and the Dremio Account Team regarding compatibility.
* Helm 3 installed on your local machine to run Helm commands. For installation instructions, refer to [Installing Helm](https://helm.sh/docs/intro/install/) in the Helm documentation.
* A local kubectl configured to access your Kubernetes cluster. For installation instructions, refer to [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) in the Kubernetes documentation.
* Object Storage: Amazon S3 (including S3-compatible, e.g., MinIO), Azure Storage, or Google Cloud Storage (GCS).
* Storage classes that support ReadWriteOnce (RWO) access mode and ideally can create expandable volumes.
* The ability to connect to [Quay.io](http://quay.io/) to access the [new v3 Helm chart](https://quay.io/repository/dremio/dremio-helm?tab=tags) for Dremio 26+, since the [older v2 Helm chart](https://github.com/dremio/dremio-cloud-tools/tree/master/charts/dremio_v2) will not function.

### Additional Prerequisites for the Enterprise Edition

For the Enterprise Edition, you must:

* Create an account on [Quay.io](https://quay.io/) to access [Dremio's OCI repository](https://quay.io/organization/dremio), which stores Dremio's Helm charts and images.  
  To get access, contact your Dremio account executive or Dremio Support.

  note

  If your internet access doesn't allow reaching Dremio's OCI repository in Quay.io, consider using a private mirror to fetch Dremio's Helm chart images.
* Get a valid license key issued by Dremio to put in the Helm chart. To obtain the license, refer to [Licensing](/current/admin/licensing/).

### Additional Prerequisites for the OpenShift

Before deploying Dremio onto OpenShift, you additionally need the following:

* Have the OpenShift `oc` CLI command configured and authenticated. For the installation instructions, see [OpenShift CLI (oc)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.11/html/cli_tools/openshift-cli-oc).

#### Node Tuning for OpenSearch on OpenShift

OpenSearch requires the `vm.max_map_count` kernel parameter to be set to at least **262144**.

This parameter controls the maximum number of memory map areas a process can have, and OpenSearch uses memory-mapped files extensively for performance.

Without this setting, OpenSearch pods will fail to start with errors related to virtual memory limits.

Since the Helm chart sets `setVMMaxMapCount: false` for OpenShift compatibility (to avoid privileged init containers), you need to configure this kernel parameter at the node level. The **recommended way** to do it is a Node Tuning Operator. This Operator ships with OpenShift and provides a declarative way to configure kernel parameters.

Create a `Tuned` resource to configure the required kernel parameter:

The `tuned-opensearch.yaml` configuration file

```
apiVersion: tuned.openshift.io/v1  
kind: Tuned  
metadata:  
  name: openshift-opensearch  
  namespace: openshift-cluster-node-tuning-operator  
spec:  
  profile:  
  - data: |  
      [main]  
      summary=Optimize systems running OpenSearch on OpenShift nodes  
      include=openshift-node  
      [sysctl]  
      vm.max_map_count=262144  
    name: openshift-opensearch  
  recommend:  
  - match:  
    - label: tuned.openshift.io/opensearch  
      type: pod  
    priority: 20  
    profile: openshift-opensearch
```

This YAML should be saved locally and applied to any cluster you intend to deploy Dremio:

```
oc apply -f tuned-opensearch.yaml
```

## Step 1: Deploy Dremio

To deploy the Dremio cluster in Kubernetes, do the following:

1. Configure your values to deploy Dremio to Kubernetes in the file `values-overrides.yaml`. For that, go to [Configuring Your Values to Deploy Dremio to Kubernetes](/current/deploy-dremio/configuring-kubernetes/) and get back here to continue with the deployment.
2. On your terminal, start the deployment by installing Dremio's Helm chart:

   * Standard Kubernetes
   * OpenShift

   Run the following command for any Kubernetes environment except for OpenShift:

   ```
   helm install <your-dremio-install-release> oci://quay.io/dremio/dremio-helm \  
   --values <your-local-path>/values-overrides.yaml \  
   --version <optional-helm-chart-version> \  
   --set-file <optional-config-files> \  
   --wait
   ```

   Where:

   * `<your-dremio-install-release>` - The name that identifies your Dremio installation. For example, `dremio-1-0`.
   * `<your-local-path>` - The path to reach your `values-overrides.yaml` configuration file.
   * (Optional) `--version <optional-helm-chart-version>` - The version of Dremio's Helm chart to be used. If not provided, defaults to the latest.
   * (Optional) `--set-file <optional-config-file>` - An optional configuration file for deploying Dremio. For example, an [Identity Provider](/current/security/authentication/identity-providers/) configuration file, which is not defined in the `values-overrides.yaml` and can be provided here through this option.

   For OpenShift, the command requires an additional `--values` option with the path to the OpenShift-specific `values-openshift-overrides.yaml` configuration file. This additional option must be placed before the `--values` option with the `values-overrides.yaml` configuration file, resulting in its substitution first.

   Run the following command for OpenShift:

   ```
   helm install <your-dremio-install-release> oci://quay.io/dremio/dremio-helm \  
   --values <your-local-path1>/values-openshift-overrides.yaml \  
   --values <your-local-path2>/values-overrides.yaml \  
   --version <optional-helm-chart-version> \  
   --set-file <optional-config-files> \  
   --wait
   ```

   Where:

   * `<your-dremio-install-release>` - The name that identifies your Dremio installation. For example, `dremio-1-0`.
   * `<your-local-path1>` - The path to reach your `values-openshift-overrides.yaml` configuration file. Only required for OpenShift.
   * `<your-local-path2>` - The path to reach your `values-overrides.yaml` configuration file.
   * (Optional) `--version <optional-helm-chart-version>` - The version of Dremio's Helm chart to be used. If not provided, defaults to the latest.
   * (Optional) `--set-file <optional-config-file>` - An optional configuration file for deploying Dremio. For example, an [Identity Provider](/current/security/authentication/identity-providers/) configuration file, which is not defined in the `values-overrides.yaml` and can be provided here through this option.
3. Monitor the deployment using the following commands:

   * Standard Kubernetes
   * OpenShift

   Run the following command for any Kubernetes environment except for OpenShift:

   ```
   kubectl get pods
   ```

   For OpenShift, run the following command:

   ```
   oc get pods
   ```

   When all of the pods are in the `Ready` state, the deployment is complete.

   Troubleshooting

   * If a pod remains in `Pending` state for more than a few minutes, run the following command to view its status to check for issues, such as insufficient resources for scheduling:

     ```
     kubectl describe pods <pod-name>
     ```
   * If the events at the bottom of the output mention insufficient CPU or memory, do one of the following:

     + Adjust the values in the `values-overrides.yaml` configuration file and redeploy.
     + Add more resources to your Kubernetes cluster.
   * If a pod returns a failed state (especially `dremio-master-0`, the most important pod), use the following commands to collect the logs:

     + Standard Kubernetes
     + OpenShift

     Run the following command for any Kubernetes environment except for OpenShift:

     ```
     kubectl logs dremio-master-0
     ```

     For OpenShift, run the following command:

     ```
     oc logs deployment/dremio-master
     ```

## Step 2: Connecting to Dremio

Now that you've installed the Helm chart and deployed Dremio on Kubernetes, the next step is connecting to Dremio, where you have the following options:

* Dremio Console
* OpenShift Route
* BI Tools via ODBC/JDBC
* BI Tools via Apache Arrow Flight

To connect to Dremio via [the Dremio console](/current/get-started/quick_tour), run the following command to use the `services dremio-client` in Kubernetes to find the host for the Dremio console:

```
$ kubectl get services dremio-client  
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
...             ...            ...             ...               ...                              ...
```

* If the value in the `TYPE` column of the output is `LoadBalancer`, access the Dremio console through the address in the `EXTERNAL_IP` column and port **9047**.  
  For example, in the output below, the value under the `EXTERNAL-IP` column is `8.8.8.8`. Therefore, access the Dremio console through <http://8.8.8.8:9047>.

  ```
  $ kubectl get services dremio-client  
  NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
  dremio-client   LoadBalancer   10.99.227.180   8.8.8.8           31010:32260/TCP,9047:30620/TCP   2d
  ```

  If you want to change the exposed port on the load balancer, change the value of the setting `coordinator.web.port` in the file `values-overrides.yaml`.
* If the value in the `TYPE` column of the output is `NodePort`, access the Dremio console through <http://localhost:30670>.

To expose Dremio externally using OpenShift Routes, do the following:

```
$ oc expose service dremio-client --port=9047 --name=dremio-ui  
  
$ oc get route dremio-ui -o jsonpath='{.spec.host}'
```

To connect your BI tools to Dremio via ODBC/JDBC, run the following command to use the `services dremio-client` in Kubernetes to find the host for ODBC/JDBC connections by using the following command:

```
$ kubectl get services dremio-client  
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
...             ...            ...             ...               ...                              ...
```

* If the value in the `TYPE` column of the output is `LoadBalancer`, access Dremio using ODBC/JDBC through the address in the `EXTERNAL_IP` column and port **31010**.  
  For example, in the output below, the value under the `EXTERNAL-IP` column is `8.8.8.8`. Therefore, access Dremio using ODBC/JDBC on port 31010 through <http://8.8.8.8:31010>.

  ```
  $ kubectl get services dremio-client  
  NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
  dremio-client   LoadBalancer   10.99.227.180   8.8.8.8           31010:32260/TCP,9047:30620/TCP   2d
  ```

  If you want to change the exposed port on the load balancer, change the value of the setting `coordinator.client.port` in the file `values-overrides.yaml`.
* If the value in the `TYPE` column of the output is `NodePort`, access Dremio using ODBC/JDBC through <http://localhost:32390>.

To connect your BI tools to Dremio via Apache Arrow Flight, run the following command to use the `services dremio-client` in Kubernetes to find the host for Apache Arrow Flight connections by using the following command:

```
$ kubectl get services dremio-client  
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
...             ...            ...             ...               ...                              ...
```

* If the value in the `TYPE` column of the output is `LoadBalancer`, access Dremio using Apache Arrow Flight through the address in the `EXTERNAL_IP` column and port **32010**.  
  For example, in the output below, the value under the `EXTERNAL-IP` column is `8.8.8.8`. Therefore, access Dremio using Apache Arrow Flight through <http://8.8.8.8:32010>.

  ```
  $ kubectl get services dremio-client  
  NAME            TYPE           CLUSTER-IP      EXTERNAL-IP       PORT(S)                          AGE  
  dremio-client   LoadBalancer   10.99.227.180   8.8.8.8           31010:32260/TCP,9047:30620/TCP   2d
  ```

  If you want to change the exposed port on the load balancer, change the value of the setting `coordinator.flight.port` in the file `values-overrides.yaml`.
* If the value in the `TYPE` column of the output is `NodePort`, access Dremio using Apache Arrow Flight through <http://localhost:31357>.

Was this page helpful?

[Previous

Kubernetes Environments](/current/deploy-dremio/kubernetes-environments)[Next

Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/)

* Prerequisites
  + Additional Prerequisites for the Enterprise Edition
  + Additional Prerequisites for the OpenShift
* Step 1: Deploy Dremio
* Step 2: Connecting to Dremio

---

# Source: https://docs.dremio.com/current/deploy-dremio/managing-engines-kubernetes/

Version: current [26.x]

On this page

# Managing Engines in Kubernetes Enterprise

note

This feature is for Enterprise Edition only.
For Community Edition, see [Configuration of Classic Engines](/current/deploy-dremio/configuring-kubernetes/#configuration-of-classic-engines).

Dremio supports the ability to provision multiple separate execution engines in Kubernetes from a Dremio main coordinator node, and automatically start and stop based on workload requirements at runtime. This provides several benefits, including:

* Creating a new engine doesn't require restarting Dremio, which enables administrators to achieve workload isolation efficiently.
* When creating a new engine, you can use Kubernetes metadata to label engines to keep track of resources.
* Right-size execution resources for each distinct workload, instead of implementing a one-size-fits-all model.
* Easily experiment with different execution resource sizes at any scale.

To manage your engines, open the Engines page as follows:

1. Open your Dremio console.
2. Click ![The Settings icon](/images/settings-icon.png "The Settings icon") in the side navigation bar to open the Settings sidebar.
3. Select **Engines**.

![Engines page under Project Settings listing all engines.](/images/settings/engine/settings-engines.png "Engines Page")

## Monitoring Engines

You can monitor the status and properties of your engines on the Engines page.

![Engines page under Project Settings showing all the current engines and their statuses.](/images/settings/engine/settings-engines-monitoring.png "Engines Page")

Each engine has the following information available:

* **Name** - The name of the engine, which you can click to see its details. See the section about Viewing Engine Details.
* **Size** - The size configured for the engine.
* **Status** - The engine status. For more information, see the section in this topic about Engine Statuses.
* **Auto start/stop** - Whether the engine has auto start/stop enabled for autoscaling.
* **Idle period** - The idle time to auto stop when the engine has **Auto start/stop** enabled.
* **Queues** - Query queues routed to the engine.
* **Labels** - Labels associated with the engine.

## Performing Actions on Engines

While monitoring engines, you have actions you can perform on each engine through the icons displayed on the right-hand side when hovering over the engine row.

![Engines page showing the icons with the actions for each engine.](/images/settings/engine/settings-engines-actions.png "Engines Page with Actions")

### Stopping/Starting an Engine

You can click ![The stop engine icon](/images/icons/engine-stop.png "The stop engine icon")/![The start engine icon](/images/icons/engine-start.png "The start engine icon") to stop/start an engine manually at any time. Stopping an engine will cause running queries to fail while new queries will remain queued, which can also fail by timeout if the engine isn't started. To prevent query failures, reroute queries to another engine, and stop the engine only when no queries are running or queued for the engine.

note

You can enable **autoscaling on an engine** to make it stop automatically after an idle time without queries and start again automatically when new queries are issued, all without any human intervention.

Autoscaling is configured when you add an engine or edit an engine:

#### Stopping All Engines

Some complex operations, like upgrading or uninstalling Dremio, require all engines to be stopped beforehand. You can stop engines manually one by one as described above, or automate the procedure using the [Engine Management API](/current/reference/api/engine-management) to stop all engines. Expand the sample below of a bash script executing the necessary endpoints to stop all engines.

Sample bash script to stop all engines

```
#!/bin/bash  
# Check if the bearer token is provided  
if [ -z "$1" ]; then  
echo "Error: Bearer token is required."  
exit 1  
fi  
BEARER_TOKEN=$1  
BASE_URL=${2:-https://localhost:9047}  
# Make an HTTP GET request to retrieve engine IDs  
RESPONSE=$(curl -k -s -H "Authorization: Bearer $BEARER_TOKEN" "$BASE_URL/api/v3/engines")  
# Check if the response contains the "id" field  
if ! echo "$RESPONSE" | grep -q '"id"'; then  
echo "Error: No 'id' field found in the response."  
exit 1  
fi  
# Extract IDs from the response  
IDS=$(echo "$RESPONSE" | jq -r '.data[] | .id')  
# Loop through each ID and make an HTTP PUT request  
for ID in $IDS; do  
RESPONSE=$(curl -k -s -o /dev/null -w "%{http_code}" -X PUT -H "Authorization: Bearer $BEARER_TOKEN" "$BASE_URL/api/v3/engines/$ID/stop")  
if [ "$RESPONSE" -eq 200 ]; then  
    echo "Successfully stopped engine with ID: $ID"  
else  
    echo "Failed to stop the engine with ID: $ID, HTTP status code: $RESPONSE"  
fi  
done  
echo "All engines processed."
```

### Editing the Engine Settings

You can click ![The edit engine icon](/images/icons/engine-edit.png "The edit engine icon") to edit the engine settings. After saving the new settings, the engine may restart, causing running queries to fail and new queries to be queued.

![Edit engine showing the general settings.](/images/settings/engine/settings-engine-edit.png "Edit Engine - General Settings")

note

The name of the engine must follow these rules:

* Must start with a lowercase alphanumeric character (`[a-z0-9]`).
* Must end with a lowercase alphanumeric character (`[a-z0-9]`).
* Must contain only lowercase alphanumeric characters or a hyphen (`[\-a-z0-9]`).
* Must be under 30 characters in length.
* Must be unique and not previously used for any existing or deleted engines.

### Deleting an Engine

You can click ![The delete engine icon](/images/icons/engine-delete.png "The delete engine icon") to delete an engine. Deleting an engine will cause running, queued, and new queries to fail. To prevent query failures, you can reroute queries to another engine, and only delete when no more queries are running or queued for the engine.

## Viewing Engine Details

While monitoring engines, if you need to know more details about engines, click the engine's name to view all the information about it.

![Engine details page showing all the information about the engine.](/images/settings/engine/settings-engine-details.png "Engine Details Page")

On this page, you will also find a set of buttons at the top to delete the engine, stop/start the engine, and edit the engine settings.

## Adding an Engine

You can create more engines by clicking **Add Engine** at the top-right corner of the Engines page.

![The general settings to add a new engine.](/images/settings/engine/settings-new-engine.png "Adding a New Engine - General Settings")

In the New engine dialog, do the following:

1. Fill out the **General** section:

   1. **Name** - Type the name of the engine. Use a meaningful name that helps you to identify the engine better. For example, `low-cost-query`.

      note

      The name of the engine must follow these rules:

      * Must start with a lowercase alphanumeric character (`[a-z0-9]`).
      * Must end with a lowercase alphanumeric character (`[a-z0-9]`).
      * Must contain only lowercase alphanumeric characters or a hyphen (`[\-a-z0-9]`).
      * Must be under 30 characters in length.
      * Must be unique and not previously used for any existing or deleted engines.
   2. **CPU** and **Size** – Select the number of CPUs per executor pod and the size of the engine.
      Dremio provides nine engine sizes, each with two CPU options targeting 16 or 32 CPU nodes. By default, Dremio will subtract 2 CPUs and 8 GB of memory from its request, resulting in requests for 14 or 30 CPUs and 120 GB of memory. This adjustment helps optimize the packing of executors on the most common node sizes. The table below shows the engine sizes:

      | Engine Size | Executors per Replica | Memory per Executor |
      | --- | --- | --- |
      | 2XSmall | 1 | 56 GB |
      | XSmall | 1 | 120 GB |
      | Small | 2 | 120 GB |
      | Medium | 4 | 120 GB |
      | Large | 8 | 120 GB |
      | XLarge | 12 | 120 GB |
      | 2XLarge | 16 | 120 GB |
      | 3XLarge | 24 | 120 GB |
      | 4XLarge | 32 | 120 GB |
   3. **Automatically start/stop** - If checked, the engine automatically stops after the specified idle time and automatically starts when new queries are issued to the engine. If not checked, the engine only stops and starts through manual intervention. By default, this setting is checked and the engine stops automatically after `15 min` of idle time. For more information, see the section Stopping/Starting an Engine.
   4. (Optional) Expand **Advanced Options** for further settings.

      ![The advanced options to add a new engine.](/images/settings/engine/settings-new-engine-advanced-options.png "Adding a New Engine - Advanced Options")

      Fill out the advanced options as follows:

      1. **Cloud cache volume (c3)** - Specify the amount of local storage for caching data.
      2. **Spill volume** - Specify the disk size allocated for temporary storage when operations exceed memory limits.
2. (Optional) Select **Kubernetes pod metadata** to define pod metadata for the engine, such as labels, annotations, node selectors, and tolerations. Define those values with care and foreknowledge of expected entries because any misconfiguration may result in Kubernetes being unable to start the executors that make up the engine.

   ![The metadata to add an engine.](/images/settings/engine/settings-new-engine-pod-metadata.png "Adding a New Engine - Metadata Settings")

   Fill out the pod's metadata with:

   1. **Labels** - Add labels as key/value pairs to identify and organize pods. Use them to group, filter, and select subsets of resources efficiently.

      note

      The engine label must follow these rules:

      * Must start with an alphanumeric character ([a-z0-9]).
      * Must end with an alphanumeric character ([a-z0-9]).
      * Must contain only lowercase alphanumeric characters, a hyphen, or a underscore ([-\_a-z0-9]).
      * The maximum length is 63 characters.
   2. **Annotations** - Add annotations as key/value pairs to store non-identifying metadata, such as build information or pointers to logging services. Unlike labels, they're not used for selection or grouping.

      note

      The engine annotation must follow these rules:

      * Must be UTF-8 encoded and can include any valid UTF-8 character.
      * Can be in plain text, JSON, or any other UTF-8 compatible format.
      * The maximum size is 256KB.
      * The maximum size of all engine annotations is 1MB.
   3. **Node selectors** - Add node selectors as key/value pairs for node-specific constraints to schedule pods on nodes matching specified labels. Use this to target nodes with specific configurations or roles.
   4. **Tolerations** - Add tolerations to allow pods to be scheduled on nodes with matching taints, but they don’t restrict scheduling to only those nodes; the pod can still land on a node without the taint.
3. Click **Add** to add the engine.

The newly added engine will be displayed in the listed engines.

![Engines page showing the current engines, which now includes the newly added engine.](/images/settings/engine/settings-new-engine-added.png "Engines Page with the Newly Added Engine")

## Engine Statuses

The following table describes each engine status:

| Status | Icon | Description |
| --- | --- | --- |
| Starting | The starting engine icon | The engine is starting. This is the initial state of an engine after being created. New queries are queued to be processed. |
| Running | The running engine icon | The engine is running. New queries are queued and processed. |
| Stopping | The stopping engine icon | The engine is stopping. Running queries will fail. New queries will remain queued, which can also fail by timeout if the engine isn't started. |
| Stopped | The stopped engine icon | The engine is stopped. New queries will remain queued, which can fail by timeout if the engine isn't started. |
| Recovering | The recovering engine icon | The engine is recovering. New queries will remain queued, which can fail by timeout if the engine doesn't recover. |
| Failed | The failed engine icon | The engine failed. New queries will remain queued, which can fail by timeout if the engine doesn't start. |

## Related Topics

* [Engine Management API](/current/reference/api/engine-management/) - The API to manage your engines using REST API calls.
* [sys.engines](/current/reference/sql/system-tables/engines/) - The system table to query for information about your engines.
* [Audit Logs](/current/security/auditing/) - Audit logs for your engines.

Was this page helpful?

[Previous

Configuring Your Values](/current/deploy-dremio/configuring-kubernetes/)[Next

Other Options](/current/deploy-dremio/other-options/)

* Monitoring Engines
* Performing Actions on Engines
  + Stopping/Starting an Engine
  + Editing the Engine Settings
  + Deleting an Engine
* Viewing Engine Details
* Adding an Engine
* Engine Statuses
* Related Topics