# Dremio Software - Client Applications



---

# Source: https://docs.dremio.com/current/client-applications/

Version: current [26.x]

On this page

# Connect Client Applications to Dremio

You can connect to Dremio from a variety of client applications. Connections are established using JDBC or ODBC.

Dremio supports a broad range of clients including the following applications:

* [Alteryx Designer](/current/client-applications/alteryx-designer)
* [DataGrip](/current/client-applications/datagrip)
* [DBeaver](/current/client-applications/dbeaver)
* [DbVisualizer](/current/client-applications/dbvisualizer)
* [Domo](/current/client-applications/domo)
* [IBM Cognos Analytics](/current/client-applications/cognos)
* [Looker](/current/client-applications/looker)
* [Microsoft Excel](/current/client-applications/microsoft-excel/)
* [Microsoft Excel PowerPivot](/current/client-applications/microsoft-excel/microsoft-excel-powerpivot)
* [Microsoft Power BI](/current/client-applications/microsoft-power-bi)
* [Microstrategy Workstation](/current/client-applications/microstrategy)
* [Preset](/current/client-applications/preset)
* [SAP Business Objects](/current/client-applications/business-objects)
* [Superset](/current/client-applications/superset)
* [Tableau](/current/client-applications/tableau)

## Drivers

* [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver)
* [Dremio JDBC (Legacy)](/current/client-applications/drivers/jdbc)
* [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver)

## Developing Custom Applications

To create a connection to Dremio and run queries, you can use [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver). You can also use [PyArrow](/current/developer/python).

## Client Encryption

Transport Layer Security (TLS) communication is supported for encrypting communication between JDBC client applications and Dremio servers. See the configuration of client TLS for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#legacy-jdbc-and-power-bi-clients-with-legacy-odbc-driver-enterprise) for more information.

Transport Layer Security (TLS) communication is enabled by default for Arrow Flight client applications. See the configuration of Arrow Flight encryption for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#arrow-flight-encryption-enterprise-edition-only) for more information. If you want to connect via unencrypted connections, you must explicitly disable `useEncryption` by setting it to `false` in the [connection parameters](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/#ssl-connection-parameters) for the Arrow Flight SQL ODBC driver.

Was this page helpful?

[Previous

Wikis and Tags](/current/data-products/govern/wikis-tags)[Next

Alteryx Designer](/current/client-applications/alteryx-designer)

* Drivers
* Developing Custom Applications
* Client Encryption

---

# Source: https://docs.dremio.com/current/client-applications/alteryx-designer

Version: current [26.x]

On this page

# Alteryx Designer

You can use Alteryx Designer to quickly prepare, blend, conform, and analyze data from datasets in Dremio.

## Supported Versions

Alteryx Designer 10.6+

## Prerequisites

* Ensure that your operating system is 64-bit Windows 10 or later.
* Download, install, and configure the [Arrow Flight SQL ODBC driver](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/).
* If you want to authenticate to Dremio by using a personal access token (PAT), rather than by using a password, generate a PAT. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for the steps.

## Selecting Dremio as a Data Source

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

   b. Specify the username to use for the connection to Dremio.

   c. Specify either a password or a personal access token to use with the username.

   d. Click **OK**.
6. If you clicked **OleDB**, follow these steps in the Data Link Properties dialog:

   a. On the **Provider** tab, select **Microsoft OLE DB Provider for ODBC Drivers**.

   b. Click **Next>>**.

   c. For step 1 on the **Connection** tab, select **Use data source name**, and then select the data source name for the Arrow Flight SQL ODBC driver.

   d. For step 2 on the **Connection** tab, specify the username to use for connections to Dremio, then specify either a password or a personal access token to use with the username.

   e. (Optional) Click **Test Connection** to find out whether the info you specified on this tab is correct.

   f. Click **OK**.

You can now browse and query datasets that are in Dremio.

warning

If you are using an Arrow Flight SQL ODBC driver, it only supports a single connection, and to load multiple tables (or datasets), you should do it sequentially. Otherwise, if you try to do it in parallel, the driver raises an error.

Was this page helpful?

[Previous

Connect Client Applications](/current/client-applications/)[Next

Apache Superset](/current/client-applications/superset)

* Supported Versions
* Prerequisites
* Selecting Dremio as a Data Source

---

# Source: https://docs.dremio.com/current/client-applications/superset

Version: current [26.x]

On this page

# Apache Superset

You can use [Superset](https://superset.apache.org/) to query and visualize data.

## Supported Versions

* Superset 1.5.3 and later
* Dremio SQLAlchemy connector 3.0.2 and later

## Supported Authentication Methods

* Use the username and password of an account in your Dremio cluster.
* Use the username of an account in your Dremio cluster and a personal access token (PAT) created in Dremio. To create a PAT, follow the steps in [Creating a PAT](/current/security/authentication/personal-access-tokens#creating-a-pat). After you obtain a PAT, it is recommended that you URL-encode it. To encode it locally on your system, you can follow these steps:
  1. In a browser window, right-click an empty area of the page and select **Inspect** or **Inspect Element**, depending on your browser.
  2. In the top bar of the inspection pane, click **Console**.
  3. Type `encodeURIComponent("<PAT>")`, where `<PAT>` is the personal access token. The URL-encoded PAT appears in red on the next line. You can highlight it and copy it to your clipboard.

## Prerequisites

If you installed Superset according to [the instructions for installing from scratch](https://superset.apache.org/docs/installation/installing-superset-from-scratch), install the Dremio SQLAlchemy Connector on the system or in the VM where Apache Superset is running. Instructions are in the [sqlalchemy\_dremio repository](https://github.com/narendrans/sqlalchemy_dremio) in GitHub.

## Creating a Connection

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
   3. If you want to authenticate by using a username and password, specify in the **SQLAlchemy URI** field a URI that is in this format:
      Format of URIs with username and password authentication

      ```
      dremio+flight://<username>:<password>@<host>:<port>/<schema>[?option1=value[&,...]]
      ```

      * `<username>`: The username of the Dremio account to use.
      * `<password>`: The password of the Dremio account to use.
      * `<host>`: The hostname or IP address of the coordinator node of the Dremio cluster.
      * `<port>`: The port to connect to on the coordinator node. Unless explicitly changed on the node, the port is 32010.
      * `<schema>`: The name of the database schema to use by default when a schema is not given in a query. Providing a schema is optional. Specifying a schema does not prevent queries from being issued for other schemas; such queries must explicitly include the schema.
      * `[?option1=value[&,...]]`: One or more optional properties, separated by ampersands (`&`). See SSL Connection Properties and Advanced Properties.Example URI with username and password authentication

      ```
      dremio+flight://myUserID:myPassword@myHost:32010/Samples?UseEncryption=false
      ```
   4. If you want to authenticate by using a personal access token, specify in the **SQLAlchemy URI** field a URI that is in this format:
      Format of URIs with PAT authentication

      ```
      dremio+flight://<username>:<PAT>@<host>:<port>/<schema>[?option1=value[&,...]]
      ```

      * `<username>`: The username of the Dremio account to use.
      * `<PAT>`: The URL-encoded personal access token that you obtained from Dremio Cloud. See Supported Authentication Methods.
      * `<host>`: The hostname or IP address of the coordinator node of the Dremio cluster.
      * `<port>`: The port to connect to on the coordinator node. Unless explicitly changed on the node, the port is 32010.
      * `<schema>`: The name of the database schema to use by default when a schema is not given in a query. Providing a schema is optional. Specifying a schema does not prevent queries from being issued for other schemas; such queries must explicitly include the schema.
      * `[?option=value[;...]]`: One or more optional properties, separated by semicolons. See SSL Connection Properties and Advanced Properties.Example URI with PAT authentication

      ```
      dremio+flight://myUserID:myPAT@myHost:32010/Samples?UseEncryption=false
      ```
   5. Test the connection. If the test fails, check the syntax and values in the connection URI.
   6. Click **Connect**.

## SSL Connection Parameters

Use the following parameters to configure SSL encryption and verification methods:

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| UseEncryption | integer | Forces the client to use an SSL-encrypted connection to communicate with Dremio. Accepted values: `true`, the client communicates with Dremio by using SSL encryption; `false`, the client does not communicate with Dremio by using SSL encryption. | true |
| disableCertificateVerification | integer | Specifies whether to verify the host certificate against the trust store. Accepted values: `false`, verifies the certificate against the trust store; `true`, does not verify the certificate against the trust store. | false |
| trustedCerts | string | The full path of the .pem file containing certificates trusted by a CA, for the purpose of verifying the server. If this option is not set, defaults to using the trusted CA certificates .pem file. The TLS connection fails if you do not specify a value when UseEncryption is true and disableCertificateVerification is false. | N/A |

## Advanced Parameters

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| routing\_queue | string | Specifies the queue to route queries to during a session. Direct Routing is used to specify the exact queue and execution cluster to run queries on for a given ODBC session. With Direct Routing, workload-management (WLM) rules are not considered; instead, queries are routed directly to the specified queue. For more information, see [Workload Management](/current/admin/workloads/workload-management). | N/A |
| routing\_tag | string | When this parameter is set, the specified tag is associated with all queries executed within a session. Rules can check for the presence of a tag with the function "tag()". For more information, see [Workload Management](/current/admin/workloads/workload-management). | N/A |

Was this page helpful?

[Previous

Alteryx Designer](/current/client-applications/alteryx-designer)[Next

DataGrip](/current/client-applications/datagrip)

* Supported Versions
* Supported Authentication Methods
* Prerequisites
* Creating a Connection
* SSL Connection Parameters
* Advanced Parameters

---

# Source: https://docs.dremio.com/current/client-applications/datagrip

Version: current [26.x]

On this page

# DataGrip

You can run SQL from [DataGrip](https://www.jetbrains.com/datagrip/) to explore your data through Dremio. DataGrip supports connections to Dremio through the Arrow Flight SQL JDBC driver.

## Supported Versions

Dremio connectivity is supported from DataGrip running on Windows, macOS, or Linux. It is recommended that you use the latest available version of DataGrip.

## Supported Authentication Methods

You can authenticate your connection to Dremio using your Dremio username and password.

## Prerequisites

Download the [Arrow Flight SQL JDBC driver](https://www.dremio.com/drivers/jdbc/).

## Connecting to Dremio

Follow the steps below to connect to Dremio:

1. Create a project in DataGrip (see [Quick start with DataGrip](https://www.jetbrains.com/help/datagrip/quick-start-with-datagrip.html#step-1-configure-initial-settings) for more information).
2. Open the Database Explorer, click the **+** icon, then click **Driver and Data Source**.

   ![Add Driver and Data Source](/assets/images/dg-driver-source-0b823e7e7af753e19313c89b47140f8d.png)
3. Select the **Drivers** tab, then click **+** to add a new driver.
4. Fill in the following details for the new driver:

   * **Name:** Provide a name to identify the driver in DataGrip (e.g., Arrow Flight SQL 10).
   * **Driver Files:** Click **+**, click **Custom JARs…**, then select the Arrow Flight SQL driver (*flight-sql-jdbc-driver-10.0.0.jar*) from the location where you downloaded it.
   * **Class:** org.apache.arrow.driver.jdbc.ArrowFlightJdbcDriver

     ![Driver Details](/assets/images/dg-driver-source2-5efa292a301626acfeaa8e13d81e8396.png)
5. At the bottom of the Data Sources and Drivers panel, click **Create Data Source**.
6. Ensure that the driver you just created is selected under **Project Data Sources**.
7. For Authentication, select **User & Password**, and provide the Dremio username and password to send for authentication.
8. For URL, follow the guidance under [Connecting to Databases](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/#connecting-to-databases).

   The following is an example URL for a local Dremio installation that does not use an encrypted flight port:

   Example Flight SQL URL

   ```
   jdbc:arrow-flight-sql://localhost:32010?useEncryption=false
   ```
9. Click **Test Connection** to confirm a valid connection to Dremio.

   ![Test Connection](/assets/images/dg-driver-source3-5be4a9ef9beb1668d0d4d361bd617d1b.png)
10. Click **OK** to save driver and data source.
11. Run a simple query to see how results are displayed in DataGrip.

    ![Run a Query](/assets/images/dg-driver-source4-1477039a90516d3ca920b129d560e68f.png)

    note

    When querying tables and views in Dremio, ensure you are using the fully qualified path. For example, `SELECT * FROM Samples."samples.dremio.com"."NYC-taxi-trips"`.

Was this page helpful?

[Previous

Apache Superset](/current/client-applications/superset)[Next

DBeaver](/current/client-applications/dbeaver)

* Supported Versions
* Supported Authentication Methods
* Prerequisites
* Connecting to Dremio

---

# Source: https://docs.dremio.com/current/client-applications/dbeaver

Version: current [26.x]

On this page

# DBeaver

You can run SQL from [DBeaver](https://dbeaver.io/) to explore your data in your data lakes and relational databases through Dremio and the Arrow Flight SQL JDBC driver.

note

If you want to use DBeaver with the legacy JDBC driver, see the instructions [here](/current/client-applications/dbeaver-legacy/).

## Supported Authentication Methods

You can use your Dremio username and password, or you can use a personal access token (PAT) that you obtained from Dremio.

## Prerequisites

* Download the [Arrow Flight SQL JDBC driver](https://www.dremio.com/drivers/jdbc/).
* If you want to authenticate your connection to Dremio by using a personal access token, see [Creating a PAT](/current/security/authentication/personal-access-tokens/#creating-a-pat) for the steps to obtain one.

## Connecting to Dremio

1. In DBeaver, add the JDBC driver as a new driver. You need to do this only once, and can skip this step if DBeaver already lists this driver in its Driver Manager dialog:

   a. In the menubar, select **Database** > **Driver Manager**.

   b. In the Driver Manager dialog, click **New**.

   c. In the Settings section, follow these steps:

   1. In the **Name** field, specify a name for the driver, such as "Arrow Flight SQL JDBC".
   2. In the **Driver Type** field, ensure that **Generic** is the selected driver type.
   3. In the **Class Name** field, specify `org.apache.arrow.driver.jdbc.ArrowFlightJdbcDriver`.
   4. In the **URL Template** field, specify `jdbc:arrow-flight-sql://{host}:{port}`.
   5. In the **Default Port** field, specify `32010`.

   d. In the Libraries section, click **Add File** and select the `.jar` file for the Arrow Flight SQL JDBC.

   e. Click **OK**.
2. Create a connection to Dremio that uses the driver:

   a. Select **Database** > **New Connection from JDBC URL**.

   b. In the Create New Connection from JDBC URL dialog, type `jdbc:arrow-flight-sql://<hostname>:32010`, where `<hostname>` is the hostname of your coordinator node. DBeaver lists the driver in the **Drivers** field.

   c. Select the driver and click **Next**.

   d. In the Connect to a Database dialog, provide your authentication credentials by following either of these sets of steps:

   * To use a personal access token that you obtained from Dremio:

     1. In the **Username** field, specify the username for which the PAT was generated.
     2. In the **Password** field, paste your personal access token.
   * To use your Dremio username and password:

     1. In the **Username** field, specify your username.
     2. In the **Password** field, your password.

   e. If connections to Dremio Software will not be encrypted, add the `useEncryption` property as a driver property, and set the value to `false`. The default for this property is `true`.

   f. (Optional) Click **Test Connection**. If the connection works, the **Connection Test** dialog opens and indicates that DBeaver is able to connect to Dremio. The connection is not held open. Click **OK**.

   g. Click **Finish**.

Was this page helpful?

[Previous

DataGrip](/current/client-applications/datagrip)[Next

DbVisualizer](/current/client-applications/dbvisualizer)

* Supported Authentication Methods
* Prerequisites
* Connecting to Dremio

---

# Source: https://docs.dremio.com/current/client-applications/dbvisualizer

Version: current [26.x]

On this page

# DbVisualizer

[DbVisualizer](https://www.dbvis.com/) is a SQL runner that works with any JDBC-compliant data source. You can run SQL from it to explore your data in your data lakes and relational databases through Dremio and the Arrow Flight SQL JDBC driver.

## Supported Versions

You can use any version of DbVisualizer, as long as you use Dremio 21 or later.

## Supported Authentication Methods

You can use your Dremio username and password, or you can use a personal access token (PAT) that you obtained from Dremio.

## Prerequisites

* Download the [Arrow Flight SQL JDBC driver](https://www.dremio.com/drivers/jdbc/).
* If you want to authenticate your connection to Dremio by using a personal access token, see [Creating a PAT](/current/security/authentication/personal-access-tokens/#creating-a-pat) for the steps to obtain one.

## Connecting to Dremio

1. Add the Arrow Flight SQL JDBC driver to DbVisualizer's Driver Manager. You need to do this only once, and can skip this step if DbVisualizer already lists this driver in its Driver Manager dialog:

   a. Select **Tools** > **Driver Manager**.

   b. Above the **Driver Name** list of the **Driver Manager** dialog, click the plus (+) symbol.

   c. In the **Name** field, name the driver.

   d. Under **Driver artifacts and jar files**, click the plus icon, browse to the `.jar` file that you downloaded, select it, and click **Open**. DbVisualizer loads the `.jar` file.

   e. If you are not using TLS encryption for connections to Dremio, turn off encryption:

   1. Click **Properties** next to **Driver Settings**.
   2. Click the plus icon to add a new property.
   3. Name the parameter `useEncryption` and set the value to `false`.
   4. Click **Apply**.

   f. Close the **Driver Manager** dialog.
2. Create a connection to Dremio:

   a. In the menubar, select **Database** > **Create Database Connection**.

   b. Double-click **Custom** at the bottom of the **Driver Name** list.

   c. Name the connection.

   d. In the **Settings Format** field, select **Database URL**.

   e. Click in the **Driver Type** field and then double-click the name that you gave to the Arrow Flight SQL JDBC driver.

   f. In the **Database URL** field, specify a URL in this format, where `host` is the hostname of your coordinator node: `jdbc:arrow-flight-sql://{host}:32010`

   g. In the **Database Userid** and **Database Password** fields, specify your authentication credentials:

   * To use a personal access token that you obtained from Dremio:

     1. In the **Database Userid** field, specify the username for which the PAT was generated.
     2. In the **Database Password** field, paste your personal access token.
   * To use your Dremio username and password:

     1. In the **Database Userid** field, specify your username.
     2. In the **Database Password** field, your password.

   h. If you are not using TLS encryptions for connections to Dremio, click the **Properties** tab and ensure that the property `useEncryption` is listed and that the value is `false`. Then, click the **Connection** tab.

   f. Click **Finish**.

DbVisualizer creates the connection and opens it.

note

If you want to use DbVisualizer with the legacy JDBC driver, see the instructions [here](/current/client-applications/dbvisualizer-legacy/).

Was this page helpful?

[Previous

DBeaver](/current/client-applications/dbeaver)[Next

Domo](/current/client-applications/domo)

* Supported Versions
* Supported Authentication Methods
* Prerequisites
* Connecting to Dremio

---

# Source: https://docs.dremio.com/current/client-applications/domo

Version: current [26.x]

On this page

# Domo

[Domo](https://www.domo.com/) is a cloud-based platform designed to provide direct, simplified, real-time access to business data for decision makers across the company with minimal IT involvement.

## Supported Authentication Methods

* Use the username and password of an account in your Dremio cluster.
* Use a username and a personal access token (PAT). To create one, see [Creating a PAT](/current/security/authentication/personal-access-tokens/#creating-a-pat).

## Creating a Cloud Integration with Dremio Software

1. Click the **Data** tab to open the Datasets page.
2. Click the **Federated** tab to open the **Amplify existing cloud warehouses** dialog.
3. Next to **Native integration**, click **Dremio**.
4. In the **Cloud integrations** dialog, click **Add new integration**.
5. In step 1 of the **Connect a Dremio cloud integration** wizard, follow these sub-steps:
   1. In the **Integration name** field, specify a unique name for the integration.
   2. (Optional) In the **Integration description** field, briefly describe the integration.
   3. Select **Dremio Software** as the connection type.
6. Click **Next**.
7. In step 2 of the wizard, follow these sub-steps:
   1. In the **Dremio connection URL** field, specify the following connection URL:

      Connection URL

      ```
      jdbc:dremio:direct=<hostname>:<port>;ssl=<true-or-false>
      ```

      `ssl`: Specifies whether to encrypt communication with the Dremio cluster. Set to `true` only if encryption for communication with JDBC clients is configured in the cluster. See the configuration of client TLS for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#legacy-jdbc-and-power-bi-clients-with-legacy-odbc-driver-enterprise) for more information.
   2. In the **Username** field, specify the username of the Dremio account that you want to use for authenticating to Dremio.
   3. In the **Password** field, specify either the password for the Dremio account or a PAT.
8. Click **Next**.
9. Select the tables that you want to use with Domo through this integration.
10. Click **Create Datasets**.

Datasets are created from the tables, though no data is moved or copied. Datasets in Domo are connections to data in data sources.

Was this page helpful?

[Previous

DbVisualizer](/current/client-applications/dbvisualizer)[Next

IBM Cognos Analytics](/current/client-applications/cognos)

* Supported Authentication Methods
* Creating a Cloud Integration with Dremio Software

---

# Source: https://docs.dremio.com/current/client-applications/cognos

Version: current [26.x]

On this page

# IBM Cognos Analytics

You can run SQL from [Cognos Analytics](https://www.ibm.com/products/cognos-analytics) to explore your data through Dremio. Cognos Analytics Dynamic Query supports connections to Dremio through the Dremio JDBC driver.

## Supported Versions

To find out which versions of Dremio are supported with IBM Cognos 11.2.x, see [DQM testing of vendor-supported client driver versions for each Cognos Analytics 11.2.x release](https://www.ibm.com/support/pages/node/6441017#11.2.4fp2r).

To find out which versions of Dremio are supported with IBM Cognos 12.0.x, see [DQM testing of vendor-supported client driver versions for each Cognos Analytics 12.0.x release](https://www.ibm.com/support/pages/node/6989513#12.0.2r).

## Supported Authentication Methods

You can use your Dremio username and password, a personal access token (PAT), or an access token from an identity provider that supports OpenID.

If you want to use a PAT, follow these steps before creating a connection to your Dremio cluster from Cognos:

1. Ensure that your Dremio administrator has followed the steps in [Enabling the Use of PATs](/current/security/authentication/personal-access-tokens/#enabling-the-use-of-pats).
2. [Create a PAT](/current/security/authentication/personal-access-tokens/#creating-a-pat).

If you want to use an access token from an identity provider that supports OpenID, ensure that your Dremio administrator has followed the steps in [OpenID Authentication](/current/security/authentication/identity-providers/oidc).

## Creating a Connection

1. Launch Cognos Analytics.
2. Navigate to **Manage** > **Data Server Connections**.
3. Click **Add Data Server** and select **Dremio** as the type of connection.
4. In the **JDBC URL** field, specify the URL for the Dremio coordinator by using this template:

   JDBC URL template

   ```
   jdbc:dremio:direct=<DREMIO_COORDINATOR>:31010[;schema=<OPTIONAL_SCHEMA>]
   ```
5. Follow one of these steps to configure a method for authenticating to Dremio:

   * If you want to connect to Dremio by using a username and a password, specify the username and password.
   * If you want to connect to Dremio by using a personal access token (PAT), specify `$token` as the username and paste the PAT into the **Password** field.
   * If you want to connect to Dremio by using access tokens, select a Cognos namespace which has been configured to use OpenID Connect.
6. Save the connection definition.
7. Click **Test** to confirm that the connection succeeds.

Was this page helpful?

[Previous

Domo](/current/client-applications/domo)[Next

Looker](/current/client-applications/looker)

* Supported Versions
* Supported Authentication Methods
* Creating a Connection

---

# Source: https://docs.dremio.com/current/client-applications/looker

Version: current [26.x]

On this page

# Looker

You can use [Looker](https://looker.com/) to query and visualize data by means of Dremio.

## Supported Authentication Methods

There are two methods of authenticating that you can choose from when you connect from Looker to Dremio:

* Use a username and password for your Dremio cluster.
* Use a personal access token (PAT) obtained from Dremio. To create a PAT, follow the steps in [Creating a PAT](/current/security/authentication/personal-access-tokens#creating-a-pat).

## Creating a Connection

1. Log into Looker.
2. In the menu bar at the top of the page, select **Admin**, and then select **Connections** under **Database**.
3. Click the **Add Connection** button in the top-right corner of the page to open the Connection Settings page for creating a connection.
4. Specify a name for the connection.
5. In the **Dialect** field, select **Dremio 11+**.
6. In the **Remote Host:Port** fields, specify the hostname or IP address of your Dremio cluster, as well as the port to connect to. By default, the port number is 31010.
7. In the **Database** field, specify any value. Though Looker requires a value in this field, Dremio does not use the value.
8. In the **Username** and **Password** fields, specify your authentication credentials:

   * If you want to authenticate by using a Dremio username and a password, specify them in the **Username** and **Password** fields.
   * If you want to authenticate by using a personal access token, specify these values:

     + In the **Username** field, specify your Dremio username.
     + In the **Password** field, paste the personal access token.
9. If your Dremio cluster is configured to use TLS, ensure that the **SSL** check box is selected.
10. Click **Test These Settings** at the bottom of the page to check that the information that you specified is all valid.
11. Click **Add Connection** if the test of the connection is successful.

The new connection is listed on the Connections page.

Was this page helpful?

[Previous

IBM Cognos Analytics](/current/client-applications/cognos)[Next

Microsoft Excel](/current/client-applications/microsoft-excel/)

* Supported Authentication Methods
* Creating a Connection

---

# Source: https://docs.dremio.com/current/client-applications/microsoft-excel/

Version: current [26.x]

On this page

# Microsoft Excel

## Supported Versions

warning

Microsoft Excel version 16.95 (25030928) for Mac introduces a change that causes Excel to crash when using the Arrow Flight SQL ODBC driver. The crash occurs immediately after authentication, before the query/source selection dialog appears. This issue only affects Excel 16.95 on macOS. Excel on Windows is not impacted. See Hiding the SQL Tables Listing for a fix.

Microsoft Excel in Microsoft 365

## Prerequisites

* Ensure that you are using Dremio v22.0 or later.
* Ensure that your operating system is 64-bit Windows 10 or later.
* Download, install, and configure the [Arrow Flight SQL ODBC driver](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/).
* If you want to authenticate to Dremio by using a personal access token (PAT), rather than by using a password, generate a PAT. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for the steps.

## Connecting to Dremio

1. In Excel, select **Data** from the menu bar.
2. Click **Get Data**.
3. Select **From Other Sources** > **From ODBC**.
4. In the From ODBC dialog, select the data source name that you specified when you configured the Arrow Flight SQL ODBC driver.
5. Specify the username to use for the connection to Dremio.
6. Specify either a password or a personal access token to use with the username
7. In the Navigator dialog, select a dataset.
8. Click **Load**.

## Hiding the SQL Tables Listing

You can prevent Excel from crashing by enabling the `hideSQLTablesListing` flag to hide the list of available sources in the query/source selection dialog. This flag can be used for Mac computers with an Apple silicon or an Intel processor.

To set the configuration:

1. Go to the **System DSN** tab of the ODBC Manager.
2. Click **Configure**.
3. Change the value of the `hideSQLTablesListing` keyword to `true`.
4. Click **OK**.

## Using the Extended Flight SQL Buffer

Apple Silicon Not Supported

The Extended Flight SQL Buffer feature was designed for Apple Silicon processors, but the Arrow Flight SQL ODBC driver is not supported on Apple Silicon M1, M2, and M3 processors. This feature is no longer available.

Was this page helpful?

[Previous

Looker](/current/client-applications/looker)[Next

Microsoft Excel PowerPivot](/current/client-applications/microsoft-excel/microsoft-excel-powerpivot)

* Supported Versions
* Prerequisites
* Connecting to Dremio
* Hiding the SQL Tables Listing
* Using the Extended Flight SQL Buffer

---

# Source: https://docs.dremio.com/current/client-applications/microsoft-power-bi/

Version: current [26.x]

On this page

# Microsoft Power BI

Connect [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) to visualize your data and create reports.

You can connect Power BI to Dremio in one of the following ways:

* Configure a reusable connection to use in Power BI Desktop, Power BI Gateway, or Power BI Service. Power BI Service can connect to Dremio through DirectQuery or through Power BI Gateway.
* Connect to a specific dataset by downloading the `.pbids` file from Dremio and opening it in Power BI Desktop.

## Supported Authentication Methods

From Power BI, you can authenticate to Dremio with one of the following methods:

* **Username and password**: Use your Dremio credentials.
* **Personal access token (PAT)**: For details, see [Personal Access Tokens](/current/security/authentication/personal-access-tokens/).
* **Single sign-on (SSO) through OAuth 2.0**: For steps on how to configure SSO, see Enable SSO to Dremio from Power BI.

## Connect to Dremio from Power BI

The Power BI connector for Dremio now supports connectivity through the open-source [Arrow Database Connectivity (ADBC) driver](https://arrow.apache.org/docs/format/ADBC.html), which Dremio highly recommends using to connect to Dremio. To enable reports to use ADBC, see Enable Connectivity with ADBC.

Existing connections will continue to work, but we recommend using the embedded ADBC driver for all new reports and migrating existing reports to ADBC to benefit from improved performance and supportability.

To connect to Dremio from Power BI Desktop:

1. Click **Get data**, search for `Dremio`, select **Dremio Software**, and click **Connect**.
2. In the Dremio Software dialog, follow these steps:

   a. Use the Flight SQL ADBC driver and in the **Server** field specify your Dremio hostname with the `adbc://` prefix. Example: `adbc://acme-company.dremio.com`

   b. (Optional) Complete the other fields in the dialog as you normally would.

   c. Under **Data Connectivity mode**, select either **Import** or **DirectQuery**. Click **OK**.

   d. For **Authentication Method**, select **Basic** or **Key**.

   * **Basic**: Enter your Dremio username and password.
   * **Key**: Paste in the personal access token you obtained from Dremio. For details, see [Personal Access Tokens](/current/security/authentication/personal-access-tokens/).
3. Click **Connect**.

note

Creating Dataflows through Power BI Service is also supported. To create a dataflow, click **New** > **Dataflow**. For the data source connection, follow the steps above.

### Create a Live Connection to a Dataset from Dremio

You can generate a Microsoft Power BI Data Source (`.pbids`) file that represents a live connection to a dataset that is in Dremio. No actual data is stored in this file, and you can think of it as a shortcut to a Power BI Desktop session with a preconfigured view of your data.

note

The `.pbids` file download option must be enabled for users to have access to this feature. To enable this feature, see Enable the `.pbids` file download.

To create a live connection to a dataset:

1. In Dremio, navigate to the dataset.
2. Click the ellipsis (**...**) next to the dataset name.
3. Select **Download .pbids file**.
4. Open the downloaded file in Power BI Desktop.
5. Authenticate using your preferred method.

## Power BI Gateway

To enable Power BI users to connect to Dremio via Power BI Gateway:

1. Install and configure [Power BI Gateway](https://docs.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem) on a machine that can connect to your Dremio cluster.
2. In the Power BI Gateway configuration, add Dremio as a data source using the same connection details as above.

## Advanced Configuration

### Enable Connectivity with ADBC

Dremio supports connectivity through Arrow Database Connectivity (ADBC). To enable this for Power BI Service, see the following options.

#### Enable the ADBC Option for a New Connection

1. In Power BI Desktop, click **Get data**.
2. In the Get Data dialog, locate and select **Dremio Software**, and click **Connect**.
3. In the Dremio Software dialog, in the **Server** field, specify your hostname with the `adbc://` prefix. Example: `adbc://acme-company.dremio.com`
4. (Optional) Complete the other fields in the dialog as you normally would.
5. Click **OK**.
6. Authenticate using your preferred method, and click **Connect**.

#### Enable the ADBC Option for an Existing Connection

1. In Power BI Desktop, go to **Data source settings**, select your source, and click **Change source**.
2. In the Dremio Software dialog, update the **Server** field by adding the `adbc://` prefix before the hostname. Example: `adbc://acme-company.dremio.com`. If you're unable to edit the source this way, click **Transform data**, then click **Advanced Editor** in the **Home** tab. In the dialog that appears, update the hostname/server with the `adbc://` prefix, and click **Done**.
3. Click **OK**.
4. Reauthenticate using your preferred method, and click **Connect**.

### Enable the `.pbids` File Download in the Dremio Console

To enable the `.pbids` file download feature:

1. In Dremio, go to **Admin** > **Settings**.
2. In the **Support** section, enable **Allow downloading of .pbids files**.
3. Click **Save**.

### Enable SSO to Dremio from Power BI

SSO is supported only for datasets that use DirectQuery.

note

SSO only works for reports created using the Dremio Cloud connector in Power BI Desktop. Reports created with the Dremio Software connector cannot use SSO by simply changing credentials, they must be converted first.

To convert existing reports from the Dremio Software connector to the Dremio Cloud connector, you'll need to modify the connection in Power BI's Advanced Editor to change the function from `Dremio.Databases` to `DremioCloud.DatabasesByServerV370`.

Prerequisites: Configure Dremio for Microsoft Entra ID

Before enabling SSO for Power BI reports, Dremio must be configured to use Microsoft Entra ID (Azure AD) as an identity provider.

**Required configuration:**

* Set `services.coordinator.web.auth.type` to the Microsoft Entra ID / OIDC provider type configured for your deployment (for example, `azuread`)
* Provide the required OIDC or Azure AD configuration file (`azuread.json` or equivalent)
* Deploy configuration files to all coordinator nodes
* Restart Dremio cluster after applying changes

For complete setup steps, see [Configure Microsoft Entra ID](/current/security/authentication/identity-providers/microsoft-entra-id/).

note

All authentication setup must be done through configuration files before enabling SSO in Power BI.

The following steps configure the Power BI side of SSO. These steps assume your Dremio deployment is already configured to authenticate users via Microsoft Entra ID.

To enable SSO for Power BI reports:

#### Enable SSO for a DirectQuery Report

To enable SSO for a report that uses DirectQuery:

1. In Power BI Service, open the workspace to which you published the report.
2. Find the dataset that is associated with the report, click the three dots next to its name, and select **Settings**.
3. In the settings for the dataset, expand **Data source credentials**.
4. Click **Edit credentials**.
5. For **Authentication method**, select **OAuth2**.
6. In the **Privacy level setting for this data source** field, ensure that **Private** is selected.
7. Select the check box **Report viewers can only access this data source with their own Power BI identities using DirectQuery**.
8. Click **Sign in**.

#### Enable SSO for Reports with Power BI Gateway

To enable SSO when you are using Power BI Gateway:

1. In Power BI Service, open the workspace to which you published the report.
2. Find the dataset that is associated with the report, click the three dots next to its name, and select **Settings**.
3. In the settings for the dataset, expand **Gateway connection**.
4. Recreate your data source by following these steps:

   1. Select the **Maps to** field.
   2. Select **Manually add to gateway**.
   3. For **Data Source Name**, enter a name for the data source.
   4. For **Data Source Type**, select **Dremio Software**.
   5. For **Server**, enter your Dremio hostname with the `adbc://` prefix. Example: `adbc://acme-company.dremio.com`
   6. For **Authentication Method**, select **OAuth2**.
   7. Click **Add**.
5. In the **Data source credentials** section, click **Edit credentials**.
6. For **Authentication method**, select **OAuth2**.
7. In the **Privacy level setting for this data source** field, ensure that **Private** is selected.
8. Select the check box **Report viewers can only access this data source with their own Power BI identities using DirectQuery**.
9. Click **Sign in**.

note

SSO requires the OAuth2 authentication method. Basic authentication and personal access tokens do not support SSO when used through Power BI Gateway.

## Arrow Database Connectivity (ADBC) Limitations

* ADBC is not enabled by default. It must be enabled by the owner of the report.
* NativeQuery is not supported.
* Metadata calls are not cached.
* Power BI Desktop occasionally caches errors that might affect future connection attempts until the cache is cleared.
* Complex data types such as `MAP` and `INTERVAL` are not supported.
* When using DirectQuery, chaining functions is supported, but some complex scenarios may not work as expected. Complex optional parameters for functions are not supported.

## Troubleshoot Power BI

### Cached Data Issues

If you have previously installed older versions of Power BI Desktop, cached data may interfere with the newer versions of the Flight SQL drivers resulting in connection errors.

#### Problem

For example, when using Flight SQL ADBC, cached connection data in Power BI could cause the following errors:

* `ADBC: IOError [] [FlightSQL] [FlightSQL] unresolved address (Unavailable; GetObjects(GetDBSchemas))`
* `ADBC: IOError [] [FlightSQL] [FlightSQL] connection error: desc = "transport: authentication handshake failed: credentials: cannot check peer: missing selected ALPN property. If you upgraded from a grpc-go version earlier than 1.67, your TLS connections may have stopped working due to ALPN enforcement. For more details, see: https://github.com/grpc/grpc-go/issues/434" (Unavailable; GetObjects(GetDBSchemas))"`

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
    Source = DremioCloud.DatabasesByServerV370("your-server-here", [  
        MaxMessageSize = 67108864  // 64 MiB  
    ])  
in  
    Source
```

Replace `your-server-here` with your actual Dremio server address. The `MaxMessageSize` parameter sets the maximum message size in bytes (67108864 = 64 MiB).

Was this page helpful?

[Previous

Microsoft Excel PowerPivot](/current/client-applications/microsoft-excel/microsoft-excel-powerpivot)[Next

Microstrategy Workstation](/current/client-applications/microstrategy)

* Supported Authentication Methods
* Connect to Dremio from Power BI
  + Create a Live Connection to a Dataset from Dremio
* Power BI Gateway
* Advanced Configuration
  + Enable Connectivity with ADBC
  + Enable the `.pbids` File Download in the Dremio Console
  + Enable SSO to Dremio from Power BI
* Arrow Database Connectivity (ADBC) Limitations
* Troubleshoot Power BI
  + Cached Data Issues
  + Large Result Sets

---

# Source: https://docs.dremio.com/current/client-applications/microstrategy

Version: current [26.x]

On this page

# Microstrategy Workstation

[MicroStrategy Workstation](https://www2.microstrategy.com/producthelp/Current/Workstation/en-us/Content/home_workstation.htm) makes it easy to build compelling visualizations and interactive dossiers in a matter of minutes and then easily share those dossiers with others.

## Supported Versions

Microstrategy Workstation 2021 Update 9 and later.

## Supported Authentication Methods

* Use a Dremio username and password.
* Use a Dremio username and a personal access token (PAT) that you obtained from Dremio.

## Prerequisites

* Install the latest version of Dremio's legacy JDBC driver:
  1. [Download the driver](https://download.dremio.com/jdbc-driver/dremio-jdbc-driver-LATEST.jar).
  2. Move the `.jar` file to one of these locations:
     + On Windows: `C:\Program Files (x86)\Common Files\MicroStrategy\JDBC`
     + On Linux: `/opt/mstr/MicroStrategy/install/JDBC`
* If you want to authenticate your connection to Dremio by using a PAT, see [Creating a PAT](/current/security/authentication/personal-access-tokens/#creating-a-pat) for the steps to obtain one.
* In Microstrategy Workstation, select **Help** > **Enable New Data Import Experience**.

## Creating an Environment-level Integration with Dremio

You can create an integration with Dremio that can be used in more than one dossier.

1. In Microstrategy Workstation, connect to the environment that you plan to use.
2. Under **Administration** on the left side of the screen, click the + sign to the right of **Data Sources**.
3. In the Data Source Types dialog, click **Dremio**.
4. In the Add Data Source - Dremio dialog, follow these steps:
   1. In the **Name** field, specify a name for the integration.
   2. (Optional) In the **Description** field, describe the integration.
   3. In the **Database Version** field, ensure that **Dremio** is selected.
   4. In the **Default Database Connection** field, either select an existing connection to a Dremio cluster, or select **Add New Database Connection**.
5. If you selected **Add New Database Connection**, follow these steps in the Create New Database Connection dialog:
   1. In the **Name** field, specify a name for the connection.
   2. In the **Basic** section, follow these steps:
      1. In the **Host Name** field, specify the IP address or hostname of the coordinator node of the Dremio cluster that you want to use this connection with.
      2. In the **Port Number** field, specify the port number to use. The default port number is 31010.
      3. In the **Authentication Mode** field, ensure that **Standard** is selected.
      4. In the **Default Database Login** field, either select an existing set of authentication credentials for the Dremio Cluster, or click **Add New Database Login** to add a new set.
      5. If you clicked **Add New Database Login** in the previous step, specify the name to associate with the credentials, and then follow either of these steps:
         * Specify the username and password of the Dremio account to use.
         * Specify the username of the Dremio account to use and a PAT, which you can paste into the **Password** field.
   3. (Optional) In the **Advanced** section, set additional properties for Microstrategy Workstation to use when connecting to Dremio. See [Optional Advanced JDBC Driver Properties](/current/client-applications/drivers/jdbc/#optional-advanced-jdbc-driver-properties) for a list of the properties that you can use.
   4. (Optional) In the **Security** section, toggle on the **Use TLS Encryption** switch if the Dremio cluster is configured to encrypt communication between it and JDBC clients. For more information, see the configuration of client TLS for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#legacy-jdbc-and-power-bi-clients-with-legacy-odbc-driver-enterprise).
   5. (Optional) In the **Properties** section, specify non-default values for various properties of the connection.
   6. Click **Save**.
6. In the Add Data Source - Dremio dialog, follow these steps:
   1. (Optional) Click **Test** to find out whether Microstrategy Workstation can connect to the Dremio cluster by using the database connection. If the test fails, ensure that the connection is configured correctly.
   2. Click **Save**.

You can now select this database connection when you create dossiers.

Was this page helpful?

[Previous

Microsoft Power BI](/current/client-applications/microsoft-power-bi/)[Next

Preset](/current/client-applications/preset)

* Supported Versions
* Supported Authentication Methods
* Prerequisites
* Creating an Environment-level Integration with Dremio

---

# Source: https://docs.dremio.com/current/client-applications/preset

Version: current [26.x]

On this page

# Preset

You can use [Preset](https://preset.io/), a cloud service for Superset, to query and visualize data.

## Supported Authentication Methods

* Use the username and password of an account in your Dremio cluster.
* Use the username of an account in your Dremio cluster and a personal access token (PAT) created in Dremio. To create a PAT, follow the steps in [Creating a PAT](/current/security/authentication/personal-access-tokens#creating-a-pat). After you obtain a PAT, it is recommended that you URL-encode it. To encode it locally on your system, you can follow these steps:
  1. In a browser window, right-click an empty area of the page and select **Inspect** or **Inspect Element**, depending on your browser.
  2. In the top bar of the inspection pane, click **Console**.
  3. Type `encodeURIComponent("<PAT>")`, where `<PAT>` is the personal access token. The URL-encoded PAT appears in red on the next line. You can highlight it and copy it to your clipboard.

## Creating a Connection

1. Click **Settings** in the top-right corner, and select **Database Connections** under **Data**.
2. Click the **+Database** button in the top-right corner.
3. Select **Other** from the **Supported Databases** field of the Connect a Database dialog.
4. In the **Display Name** field, specify any name you prefer.
5. In the **Connect a Database** dialog, follow these steps:
   1. Select **Other** from the **Supported Databases** field.
   2. In the **Display Name** field, name the new connection.
   3. If you want to authenticate by using a username and password, specify in the **SQLAlchemy URI** field a URI that is in this format:

      Format of URIs with username and password authentication

      ```
      dremio://<username>:<password>@<host>:<port>[/option=value[;...]]
      ```

      * `<username>`: The username of the Dremio account to use.
      * `<password>`: The password of the Dremio account to use.
      * `<host>`: The hostname or IP address of the coordinator node of the Dremio cluster.
      * `<port>`: The port to connect to on the coordinator node. Unless explicitly changed on the node, the port is 31010.
      * `[/option=value[;...]]`: One or more optional properties, separated by semicolons. See SSL Connection Properties and Advanced Properties.Example URI with username and password authentication

      ```
      dremio://myUserID:myPassword@myHost:31010/ssl=true;schema=Samples;routing_tag=thisTag
      ```
   4. If you want to authenticate by using a personal access token, specify in the **SQLAlchemy URI** field a URI that is in this format:

      Format of URIs with PAT authentication

      ```
      dremio://<username>:<PAT>@<host>:<port>[/option=value[;...]]
      ```

      * `<username>`: The username of the Dremio account to use.
      * `<PAT>`: The personal access token to use.
      * `<host>`: The hostname or IP address of the coordinator node of the Dremio cluster.
      * `<port>`: The port to connect to on the coordinator node. Unless explicitly changed on the node, the port is 31010.
      * `[/option=value[;...]]`: One or more optional properties, separated by semicolons. See SSL Connection Properties and Advanced Properties.Example URI with PAT authentication

      ```
      dremio://myUserID:myPAT@myHost:31010/ssl=true;schema=Samples;routing_tag=thisTag
      ```
   5. Test the connection. If the test fails, check the syntax and values in the connection URI.
   6. Click **Connect**.

## SSL Connection Properties

Use the following properties to configure SSL encryption and verification methods:

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| UseEncryption | integer | Forces the client to use an SSL-encrypted connection to communicate with Dremio. Accepted values: `true`, the client communicates with Dremio by using SSL encryption; `false`, the client does not communicate with Dremio by using SSL encryption. | true |
| disableCertificateVerification | integer | Specifies whether to verify the host certificate against the trust store. Accepted values: `false`, verifies the certificate against the trust store; `true`, does not verify the certificate against the trust store. | false |
| trustedCerts | string | The full path of the .pem file containing certificates trusted by a CA, for the purpose of verifying the server. If this option is not set, defaults to using the trusted CA certificates .pem file.The TLS connection fails if you do not specify a value when UseEncryption is true and disableCertificateVerification is false. | N/A |

## Advanced Properties

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| routing\_queue | string | Specifies the queue to route queries to during a session. Direct Routing is used to specify the exact queue and execution cluster to run queries on for a given session. With Direct Routing, workload-management (WLM) rules are not considered; instead, queries are routed directly to the specified queue. For more information, see [Workload Management](/current/admin/workloads/workload-management). | N/A |
| routing\_tag | string | When this property is set, the specified tag is associated with all queries executed within a session. Rules can check for the presence of a tag with the function "tag()". For more information, see [Workload Management](/current/admin/workloads/workload-management). | N/A |

Was this page helpful?

[Previous

Microstrategy Workstation](/current/client-applications/microstrategy)[Next

SAP Business Objects](/current/client-applications/business-objects)

* Supported Authentication Methods
* Creating a Connection
* SSL Connection Properties
* Advanced Properties

---

# Source: https://docs.dremio.com/current/client-applications/business-objects

Version: current [26.x]

On this page

# SAP Business Objects

## Prerequisites

Dremio Business Objects integration requires:

* SAP Business Objects 4.0+
* Download, install, and configure the [Arrow Flight SQL ODBC driver](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/).

## Connecting to a Dremio cluster using Information Design Tool

1. Open Information Design Tool and a new project.
2. Create a new Relational Connection using the Generic ODBC3 datasource driver.
3. Select the Arrow Flight SQL ODBC DSN and test the connection.

Dremio schemas and tables are now available.

## Using Dremio datasets in Web Intelligence Reports

1. In Information Design Tool, publish the Dremio connection to a repository.
2. Create a new Data Foundation.
3. Create a new Business Layer.
4. Publish the universe to a repository.
5. Open a web browser, go to Web Intelligence tool and select the published universe.
6. Configure the query.

Your Dremio dataset is ready to be used in Web Intelligence.

Was this page helpful?

[Previous

Preset](/current/client-applications/preset)[Next

Tableau](/current/client-applications/tableau)

* Prerequisites
* Connecting to a Dremio cluster using Information Design Tool
* Using Dremio datasets in Web Intelligence Reports

---

# Source: https://docs.dremio.com/current/client-applications/tableau

Version: current [26.x]

On this page

# Tableau

Connect [Tableau](https://www.tableau.com/) to Dremio to derive powerful insights from your data and create real-time dashboards.

You can connect your Tableau application to Dremio in one of two ways:

* Configure a reusable connection in Tableau Desktop, Tableau Server, or Tableau Cloud.
* Connect to a specific dataset by downloading the `.tds` file from Dremio and opening it in Tableau Desktop.

## Supported Tableau Versions

| Product | Supported Versions |
| --- | --- |
| Tableau Desktop | 2022.1 and later |
| Tableau Server | 2022.1 and later |
| Tableau Cloud | Latest version deployed by Tableau |

## Supported Authentication Methods

From Tableau, you can authenticate to Dremio with a username and password, or with a [personal access token (PAT)](/current/security/authentication/personal-access-tokens/#creating-a-pat) that can be obtained from the Dremio console.

You can also configure single sign-on (SSO) through OAuth 2.0. For steps on how to configure SSO, see Enabling SSO to Dremio from Tableau.

## Tableau Desktop

Tableau Desktop includes a native connector that you can use to connect to Dremio.

### Prerequisites for Using the Dremio JDBC Driver (Legacy)

To connect to Dremio, you'll also need to install the Dremio JDBC driver. Download the Dremio JDBC driver and copy it to Tableau Desktop's `Drivers` folder.

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

1. Open Tableau Desktop. Under the **To a Server** section in the **Connect** panel, click **More**.
2. Select **Dremio**. The **Dremio** connection dialog opens.
3. In the connection dialog, for the **Product** field, select **Dremio Software**.
4. For the **Server** field, specify the hostname or IP address of your Dremio coordinator node.
5. In the **Port** field, specify the port, if it differs from the default port, which is `31010`.
6. In the **Authentication** field, select **Username and Password** or **OAuth 2.0**.
   * If you selected **Username and Password**, in the **Username** and **Password** fields, specify your Dremio credentials. If you have a personal access token, specify your username and then paste the token into the **Password** field.
   * If you selected **OAuth 2.0**, specify one of these URLs in the **Dremio Authorization Server** field, replacing `<dremio-host>` with the hostname or IP address for your Dremio coordinator node:
     + If your Dremio cluster does not use SSL: `http://<dremio-host>:9047`
     + If your Dremio cluster does use SSL: `https://<dremio-host>:9047`
7. (Optional) If your Dremio cluster is configured for secure connections, select the **Require SSL** option.
8. (Optional for Tableau 2025.1+) If you are using the Arrow Flight SQL JDBC driver, in the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option. Ensure that you have the Arrow Flight SQL JDBC driver downloaded.
9. (Optional) In the **Advanced** tab, specify the **Engine**, **Queue**, and **Tag**. For information about how these values are used, see [Workload Management](/current/admin/workloads/workload-management/).
10. Click **Sign In**.

### Creating a Live Connection to a Dataset from Dremio

You can generate a Tableau Datasource (`.tds`) file that represents a live connection to a dataset that is in Dremio. No actual data is stored in this file, and you can think of it as a shortcut to a Tableau session with a preconfigured view of your data.

note

* The `.tds` file download option must be enabled for users to have access to this feature. To enable this feature, see Enabling the .tds file download.

To download a `.tds` file:

1. On the Datasets page in Dremio, find the dataset you want to work with and open the Details panel for the dataset.
2. Click the button that displays the Tableau logo. Dremio downloads a `.tds` file to your system.
3. Open the `.tds` file.
4. Authenticate using your username and password. To authenticate using SSO, follow these steps:
   1. Sign into your identity provider. You are taken to the sign-in screen only the first time that you log into Dremio during a session in Tableau.
   2. Click **Accept** in the Authorize App dialog. This dialog appears only the first time that you authenticate from Tableau through your identity provider.

## Tableau Server

Tableau Server includes a native connector that you can use to connect to Dremio.

### Prerequisites for Using the Dremio JDBC Driver (Legacy)

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
Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/16.1.0/flight-sql-jdbc-driver-16.1.0.jar" -OutFile "C:\Program Files\Tableau\Drivers\flight-sql-jdbc-driver-16.1.0.jar"
```

Download driver for Linux by running this command in a command-line window

```
curl -L https://repo1.maven.org/maven2/org/apache/arrow/flight-sql-jdbc-driver/16.1.0/flight-sql-jdbc-driver-16.1.0.jar -o /opt/tableau/tableau_driver/jdbc/flight-sql-jdbc-driver-16.1.0.jar
```

### Steps for Connecting

To create a Dremio source in Tableau Server:

1. In a web browser, navigate to your Tableau Server site.
2. In your workbook, click **Add a Data Source**. Alternatively, you can [publish an existing data source](https://help.tableau.com/current/pro/desktop/en-us/publish_datasources.htm) to Tableau Server.
3. In the **Connect to Data** dialog, select **Dremio** under the **Connectors** tab.
4. In the connection dialog, for the **Product** field, select **Dremio Software**.
5. For the **Server** field, specify the hostname or IP address of your Dremio coordinator node.
6. For **Port**, enter the port if it differs from the default `31010` port.
7. In the **Authentication** field, select **Username and Password** or **OAuth 2.0**.
   * If you selected **Username and Password**, in the **Username** and **Password** fields, specify your Dremio credentials. If you have a personal access token, specify your username and then paste the token into the **Password** field.
   * If you selected **OAuth 2.0**, specify one of these URLs in the **Dremio Authorization Server** field, replacing `<dremio-host>` with the hostname or IP address for your Dremio coordinator node:
     + If your Dremio cluster does not use SSL: `http://<dremio-host>:9047`
     + If your Dremio cluster does use SSL: `https://<dremio-host>:9047`
8. (Optional) If your Dremio cluster is configured for secure connections, select the **Require SSL** option.
9. (Optional for Tableau 2025.1+) If you are using the Arrow Flight SQL JDBC driver, in the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option. Ensure that you have the Arrow Flight SQL JDBC driver downloaded.
10. (Optional) In the **Advanced** tab, you can specify the **Engine**, **Queue**, and **Tag**.
11. Click **Sign In**.

## Tableau Cloud

Tableau Cloud includes a native connector that you can use to connect to Dremio.

note

The Tableau Cloud 2025.1 connector for Dremio has an option to use the [Arrow Flight SQL JDBC](/cloud/sonar/client-apps/drivers/arrow-flight-sql-jdbc) driver in place of the Dremio JDBC driver to power the connection to Dremio. In the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option.

### Steps for Connecting

To create a Dremio source in Tableau Cloud:

1. In a web browser, navigate to your Tableau Cloud site.
2. Click **New** > **Published Data Source** to create a reusable data source or **Data** > **Add a Data Source** from within a workbook. Alternatively, you can [publish an existing data source](https://help.tableau.com/current/pro/desktop/en-us/publish_datasources.htm) to Tableau Cloud.
3. In the **Connect to Data** dialog, select **Dremio** under the **Connectors** tab.
4. In the connection dialog, for the **Product** field, select **Dremio Software**.
5. For the **Server** field, specify the hostname or IP address of your Dremio coordinator node.
6. In the **Port** field, enter the port if it differs from the default `31010` port.
7. In the **Authentication** field, select **Username and Password** or **OAuth 2.0**.
   * If you selected **Username and Password**, in the **Username** and **Password** fields, specify your Dremio credentials. If you have a personal access token, specify your username and then paste the token into the **Password** field.
   * If you selected **OAuth 2.0**, specify one of these URLs in the **Dremio Authorization Server** field, replacing `<dremio-host>` with the hostname or IP address for your Dremio coordinator node:
     + If your Dremio cluster does not use SSL: `http://<dremio-host>:9047`
     + If your Dremio cluster does use SSL: `https://<dremio-host>:9047`
8. (Optional for Tableau 2025.1+) If you are using the Arrow Flight SQL JDBC driver, in the **Advanced** tab, select the **Use Arrow Flight SQL Driver (preview)** option.
9. (Optional) If your Dremio cluster is configured for secure connections, select the **Require SSL** option.
10. (Optional) In the **Advanced** tab, you can specify the **Engine**, **Queue**, and **Tag**.
11. Click **Sign In**.
12. If you're authenticating using SSO (OAuth 2.0), follow these steps:
    1. Sign into your identity provider. You are taken to the sign-in screen only the first time that you log into Dremio during a session in Tableau Cloud.
    2. Click **Accept** in the Authorize App dialog. This dialog appears only the first time that you authenticate from Tableau Cloud through your identity provider.

## Advanced Configuration

### Enabling the `.tds` File Download in the Dremio console

`ADMIN` privileges are required to make updates to this setting.

To enable users to download `.tds` files for datasets in Dremio, follow these steps:

1. Click the Settings icon in the left sidebar of a project.
2. Select **Project Settings**.
3. Select **BI Applications**.
4. Select the **Tableau** tab.
5. Toggle the **Enable Tableau Desktop** setting on.

After the organization administrator completes these steps, refresh your browser window.

### Enabling SSO to Dremio from Tableau Enterprise

SSO using OAuth 2.0 is supported by Tableau Desktop 2022.3 or later, Tableau Server, and Tableau Cloud.

Users of Tableau Desktop will use SSO authentication whether connecting directly to Dremio or connecting through a `.tds` file downloaded from Dremio. If you want to use SSO to authenticate when connecting to Dremio through a `.tds` file, ensure that SSO is enabled and configured for your Dremio cluster before the file is downloaded.

To enable SSO to Dremio from Tableau, ensure that your Dremio cluster has SSO configured with [Microsoft Entra ID](/current/security/authentication/identity-providers/microsoft-entra-id) or an [OIDC identity provider](/current/security/authentication/identity-providers/oidc) and follow these steps:

1. For Tableau Server only, follow the configuration steps.
2. Follow the steps to enable SSO to Dremio from Tableau.

#### Configuring SSO for Tableau Server

To configure SSO using [OAuth for Tableau Server](https://tableau.github.io/connector-plugin-sdk/docs/oauth), follow these steps:

1. Run the following command in the Tableau Services Manager (TSM) command line. Set a value for the `<tableau-server-domain-name-or-ip>`parameter, which is the domain name or IP of your Tableau Server deployment:

   Configure OAuth for Tableau Server

   ```
   tsm configuration set -k oauth.config.clients -v "[{\"oauth.config.id\":\"dremio\", \"oauth.config.client_id\":\"https\:\/\/connectors.dremio.app\/tableau\", \"oauth.config.client_secret\":\"test-client-secret\", \"oauth.config.redirect_uri\":\"https://<tableau-server-domain-name-or-ip>/auth/add_oauth_token\"}]" --force-keys
   ```
2. To apply the changes to Tableau Server, run the command `tsm pending-changes apply`.

#### Configuring Dremio

To enable SSO authentication to Dremio from Tableau:

1. In the Dremio console, click the Settings icon and select the BI Applications page.
2. On the BI Applications page, click **Tableau**.
3. Ensure that **Enable single sign-on for Tableau** is toggled on.
4. **For Tableau Server only:** In the **Redirect URIs** field, paste in the redirect URI for your Tableau Server. If you have set up more than one Tableau Server, you can add multiple URIs, separating them with commas. Each URI uses this format, where `<tableau-server>` is the hostname or IP address of Tableau Server:

   Redirect URI for Tableau Server

   ```
   https://<tableau-server>/auth/add_oauth_token
   ```

#### Configuring an Identity Provider

Register an additional redirect URI: `https://<dremio-host>:xxxx/oauth/callback` or `http://<dremio-host>:xxxx/oauth/callback` in the SSO application configured in your identity provider. See the configuration instructions for [Microsoft Entra ID](/current/security/authentication/identity-providers/microsoft-entra-id#configuring-microsoft-entra-id) or [OpenID Identity Providers](/current/security/authentication/identity-providers/oidc#configuring-openid) for additional information.

### Customizing the Connection String

To add JDBC parameters to the JDBC URL that Tableau generates for connections to Dremio using the parameters from the connection dialog, see [Use a Properties file to customize a JDBC connection](https://help.tableau.com/current/pro/desktop/en-us/connect_customize.htm#use-a-properties-file-to-customize-a-jdbc-connection) in the Tableau documentation.

### Manually Installing the Dremio Connector

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
4. Now you can connect to Dremio from Tableau Desktop or Tableau Server.

### Exporting a Dremio Dataset with SSL Placeholder

If you have SSL enabled on Dremio, and you want to export a `.tds` file to use in a Tableau application for quickly connecting to a dataset,
you can do so by add the support key `export.tableau.extra-native-connection-properties` and set the value to `SSL=true`.
This property allows you to set the JDBC connection string when exporting a `.tds` file. The default is an empty string. This is the only property currently supported for `export.tableau.extra-native-connection-properties`, and `true` is the only supported value.

To know how to set the `export.tableau.extra-native-connection-properties` support key, see [Support Keys](/current/help-support/support-settings/#support-keys).

#### Changing the Hostname

You can use the `export.bi.hostname` support key to change the default hostname of the SQL endpoint for generating TDS files.

To know how to set the `export.bi.hostname` support key, see [Support Keys](/current/help-support/support-settings/#support-keys).

#### Example: SSL setting

In the following example, SSL is enabled in the **dremio.conf** file. See [Using Wire Encryption](/current/what-is-dremio/architecture/encrypting-dremio/#odbcjdbc-client-encryption--enterprise-edition-only)
for more information.

Example SSL settings for generating a self-signed certificate with JDBC Dremio config

```
services.coordinator.client-endpoint.ssl.enabled: true  
services.coordinator.client-endpoint.ssl.auto-certificate.enabled: true
```

#### Example: export.tableau.extra-native-connection-properties value

Example SSL property value

```
SSL=true
```

## Limitations

* When using Tableau with Dremio, avoid using periods in space or dataset names. Due to differences in hierarchy support, periods in paths are treated as separators, resulting in errors when navigating or selecting spaces or datasets with periods in their names.

Was this page helpful?

[Previous

SAP Business Objects](/current/client-applications/business-objects)[Next

ThoughtSpot](/current/client-applications/thoughtspot)

* Supported Tableau Versions
* Supported Authentication Methods
* Tableau Desktop
  + Prerequisites for Using the Dremio JDBC Driver (Legacy)
  + Prerequisites for Using the Arrow Flight SQL JDBC Driver
  + Steps for Connecting
  + Creating a Live Connection to a Dataset from Dremio
* Tableau Server
  + Prerequisites for Using the Dremio JDBC Driver (Legacy)
  + Prerequisites for Using the Arrow Flight SQL JDBC Driver
  + Steps for Connecting
* Tableau Cloud
  + Steps for Connecting
* Advanced Configuration
  + Enabling the `.tds` File Download in the Dremio console
  + Enabling SSO to Dremio from Tableau Enterprise
  + Customizing the Connection String
  + Manually Installing the Dremio Connector
  + Exporting a Dremio Dataset with SSL Placeholder
* Limitations

---

# Source: https://docs.dremio.com/current/client-applications/thoughtspot

Version: current [26.x]

On this page

# ThoughtSpot

You can use [ThoughtSpot](https://www.thoughtspot.com/) to search directly against your data in Dremio for live analytics and actionable insights.

## Supported Versions

Dremio supports ThoughtSpot cloud 8.3 and ThoughtSpot software 7.2.1.

## Supported Authentication Methods

You can use your Dremio username and password.

## Creating a Connection

note

While you're using the connection, the data fields that you create, modify, and delete in Dremio are reflected as table columns in ThoughtSpot. To account for new or outdated fields, you will need to go back into the data connection to check or uncheck the columns that you want added or removed on the Select Tables page.

1. Log into ThoughtSpot.
2. Go to **Data** > **Connections** > **Add Connection**.
3. On the Choose Your Data Warehouse page, specify your data connection details:

   a. In the **Name your connection** field, enter a name.

   b. (Optional) In the **Describe your connection** field, enter a brief description.

   c. For the **Choose your data warehouse** field, select **Dremio**.
4. Click **Continue**.
5. On the Dremio Connection Details page, specify your account credentials:

   a. To provide your Dremio username and password for authentication, select **Use Service Account**.

   b. In the **Host** field, enter the IP address for one of the coordinator nodes in your cluster.

   c. In the **Port** field, enter 31010.

   d. In the **User** field, enter your username.

   e. In the **Password** field, enter your password.
6. Click **Continue**.
7. On the Select Tables page, you can see all the data tables and views from Dremio. To select tables and columns from that list, select a table and check the boxes next to the columns for that table.
8. Click **Create Connection**.
9. In the **Create Connection** dialog, click **Confirm**.

Was this page helpful?

[Previous

Tableau](/current/client-applications/tableau)[Next

Drivers](/current/client-applications/drivers/)

* Supported Versions
* Supported Authentication Methods
* Creating a Connection

---

# Source: https://docs.dremio.com/current/client-applications/drivers/

Version: current [26.x]

# Drivers

Dremio provides Arrow Flight SQL ODBC and JDBC drivers:

* [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver)
* [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver)

Dremio also supports the [Dremio JDBC driver (Legacy)](/current/client-applications/drivers/jdbc).

Was this page helpful?

[Previous

ThoughtSpot](/current/client-applications/thoughtspot)[Next

Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver)

---

# Source: https://docs.dremio.com/current/client-applications/dbvisualizer-legacy

Version: current [26.x]

On this page

# DbVisualizer

You can use the legacy Dremio JDBC driver to run [DbVisualizer](https://www.dbvis.com/), a SQL runner that works with any JDBC-compliant data source.

## Supported Versions

You can use any version of DbVisualizer, if you use the legacy Dremio JDBC Driver 14.0.0 or later.

## Supported Authentication Methods

You can use your Dremio username and password, or you can use a personal access token (PAT) that you obtained from Dremio.

## Prerequisites

* Download the [legacy Dremio JDBC driver](/current/client-applications/drivers/jdbc/).
* If you want to authenticate your connection to Dremio by using a personal access token, see [Creating a PAT](/current/security/authentication/personal-access-tokens/#creating-a-pat) for the steps to obtain one.

## Connecting to Dremio

1. Add the legacy Dremio JDBC Driver to DbVisualizer's Driver Manager. You need to do this only once, and can skip this step if DbVisualizer already lists this driver in its Driver Manager dialog:

   a. In the menubar, select **Tools** > **Driver Manager**.

   b. In the **Driver Name** list of the **Driver Manager** dialog, select **Dremio**.

   c. Click the folder icon to find and select the downloaded Dremio JDBC driver.

   d. Close the **Driver Manager** dialog.
2. Create a connection to Dremio:

   a. In the menubar, select **Database** > **Create Database Connection**.

   b. Double-click **Dremio** in the **Driver Name** list.

   c. Name the connection.

   d. Ensure that these default values are set:

   | Field | Value |
   | --- | --- |
   | **Settings Format** | Server Info |
   | **Connection Type** | Direct |
   | **Database Port** | 31010 |

   e. In the **Database Server** field, specify the hostname of your coordinator node.

   f. In the **Database Userid** and **Database Password** fields, specify your authentication credentials:

   * To use a personal access token that you obtained from Dremio:

     1. In the **Database Userid** field, specify the username for which the PAT was generated.
     2. In the **Database Password** field, paste your personal access token.
   * To use your Dremio username and password:

     1. In the **Database Userid** field, specify your username.
     2. In the **Database Password** field, your password.

   g. (Optional) Click **Ping Server** to test the connection.

   h. Click **Finish**.

DbVisualizer creates the connection and opens it.

Was this page helpful?

[Previous

Dremio JDBC Driver (Legacy)](/current/client-applications/drivers/jdbc)[Next

Accelerate Queries](/current/acceleration/)

* Supported Versions
* Supported Authentication Methods
* Prerequisites
* Connecting to Dremio

---

# Source: https://docs.dremio.com/current/client-applications/microsoft-excel/microsoft-excel-powerpivot

Version: current [26.x]

On this page

# Microsoft Excel PowerPivot

## Prerequisites

* Ensure that you are using Dremio v22.0 or later.
* Ensure that your operating system is 64-bit Windows 10 or later.
* Download, install, and configure the [Arrow Flight SQL ODBC driver](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/).
* If you want to authenticate to Dremio by using a personal access token (PAT), rather than by using a password, generate a PAT. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for the steps.

## Updating the DSN Configuration

1. Launch ODBC Data Sources on your Windows system.
2. Select the **System DSN** tab.
3. Select the DSN entry that you created when you configured the Arrow Flight SQL ODBC driver.
4. Click **Configure**.
5. In the **Advanced Properties** section, add the following key/value pair:  
   * **Key:** quoting
   * **Value:** BRACKET

## Connecting to Dremio

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

   d. For step 2 on the **Connection** tab, specify the username to use for connections to Dremio, then specify either a password or a personal access token to use with the username.

   e. (Optional) Click **Test Connection** to find out whether the info you specified on this tab is correct.

   f. Click **OK**.
8. (Optional) Click **Test Connection** to find out whether you can connect to Dremio.
9. Click **Next**.
10. Ensure that the option **Select from a list of tables and views to choose the data to import**.
11. Click **Next**.
12. Select the tables and views that you want to import data from.
13. Click **Finish**.

Was this page helpful?

[Previous

Microsoft Excel](/current/client-applications/microsoft-excel/)[Next

Microsoft Power BI](/current/client-applications/microsoft-power-bi/)

* Prerequisites
* Updating the DSN Configuration
* Connecting to Dremio

---

# Source: https://docs.dremio.com/current/client-applications/microsoft-power-bi

Version: current [26.x]

On this page

# Microsoft Power BI

Connect [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) to visualize your data and create reports.

You can connect Power BI to Dremio in one of the following ways:

* Configure a reusable connection to use in Power BI Desktop, Power BI Gateway, or Power BI Service. Power BI Service can connect to Dremio through DirectQuery or through Power BI Gateway.
* Connect to a specific dataset by downloading the `.pbids` file from Dremio and opening it in Power BI Desktop.

## Supported Authentication Methods

From Power BI, you can authenticate to Dremio with one of the following methods:

* **Username and password**: Use your Dremio credentials.
* **Personal access token (PAT)**: For details, see [Personal Access Tokens](/current/security/authentication/personal-access-tokens/).
* **Single sign-on (SSO) through OAuth 2.0**: For steps on how to configure SSO, see Enable SSO to Dremio from Power BI.

## Connect to Dremio from Power BI

The Power BI connector for Dremio now supports connectivity through the open-source [Arrow Database Connectivity (ADBC) driver](https://arrow.apache.org/docs/format/ADBC.html), which Dremio highly recommends using to connect to Dremio. To enable reports to use ADBC, see Enable Connectivity with ADBC.

Existing connections will continue to work, but we recommend using the embedded ADBC driver for all new reports and migrating existing reports to ADBC to benefit from improved performance and supportability.

To connect to Dremio from Power BI Desktop:

1. Click **Get data**, search for `Dremio`, select **Dremio Software**, and click **Connect**.
2. In the Dremio Software dialog, follow these steps:

   a. Use the Flight SQL ADBC driver and in the **Server** field specify your Dremio hostname with the `adbc://` prefix. Example: `adbc://acme-company.dremio.com`

   b. (Optional) Complete the other fields in the dialog as you normally would.

   c. Under **Data Connectivity mode**, select either **Import** or **DirectQuery**. Click **OK**.

   d. For **Authentication Method**, select **Basic** or **Key**.

   * **Basic**: Enter your Dremio username and password.
   * **Key**: Paste in the personal access token you obtained from Dremio. For details, see [Personal Access Tokens](/current/security/authentication/personal-access-tokens/).
3. Click **Connect**.

note

Creating Dataflows through Power BI Service is also supported. To create a dataflow, click **New** > **Dataflow**. For the data source connection, follow the steps above.

### Create a Live Connection to a Dataset from Dremio

You can generate a Microsoft Power BI Data Source (`.pbids`) file that represents a live connection to a dataset that is in Dremio. No actual data is stored in this file, and you can think of it as a shortcut to a Power BI Desktop session with a preconfigured view of your data.

note

The `.pbids` file download option must be enabled for users to have access to this feature. To enable this feature, see Enable the `.pbids` file download.

To create a live connection to a dataset:

1. In Dremio, navigate to the dataset.
2. Click the ellipsis (**...**) next to the dataset name.
3. Select **Download .pbids file**.
4. Open the downloaded file in Power BI Desktop.
5. Authenticate using your preferred method.

## Power BI Gateway

To enable Power BI users to connect to Dremio via Power BI Gateway:

1. Install and configure [Power BI Gateway](https://docs.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem) on a machine that can connect to your Dremio cluster.
2. In the Power BI Gateway configuration, add Dremio as a data source using the same connection details as above.

## Advanced Configuration

### Enable Connectivity with ADBC

Dremio supports connectivity through Arrow Database Connectivity (ADBC). To enable this for Power BI Service, see the following options.

#### Enable the ADBC Option for a New Connection

1. In Power BI Desktop, click **Get data**.
2. In the Get Data dialog, locate and select **Dremio Software**, and click **Connect**.
3. In the Dremio Software dialog, in the **Server** field, specify your hostname with the `adbc://` prefix. Example: `adbc://acme-company.dremio.com`
4. (Optional) Complete the other fields in the dialog as you normally would.
5. Click **OK**.
6. Authenticate using your preferred method, and click **Connect**.

#### Enable the ADBC Option for an Existing Connection

1. In Power BI Desktop, go to **Data source settings**, select your source, and click **Change source**.
2. In the Dremio Software dialog, update the **Server** field by adding the `adbc://` prefix before the hostname. Example: `adbc://acme-company.dremio.com`. If you're unable to edit the source this way, click **Transform data**, then click **Advanced Editor** in the **Home** tab. In the dialog that appears, update the hostname/server with the `adbc://` prefix, and click **Done**.
3. Click **OK**.
4. Reauthenticate using your preferred method, and click **Connect**.

### Enable the `.pbids` File Download in the Dremio Console

To enable the `.pbids` file download feature:

1. In Dremio, go to **Admin** > **Settings**.
2. In the **Support** section, enable **Allow downloading of .pbids files**.
3. Click **Save**.

### Enable SSO to Dremio from Power BI

SSO is supported only for datasets that use DirectQuery.

note

SSO only works for reports created using the Dremio Cloud connector in Power BI Desktop. Reports created with the Dremio Software connector cannot use SSO by simply changing credentials, they must be converted first.

To convert existing reports from the Dremio Software connector to the Dremio Cloud connector, you'll need to modify the connection in Power BI's Advanced Editor to change the function from `Dremio.Databases` to `DremioCloud.DatabasesByServerV370`.

Prerequisites: Configure Dremio for Microsoft Entra ID

Before enabling SSO for Power BI reports, Dremio must be configured to use Microsoft Entra ID (Azure AD) as an identity provider.

**Required configuration:**

* Set `services.coordinator.web.auth.type` to the Microsoft Entra ID / OIDC provider type configured for your deployment (for example, `azuread`)
* Provide the required OIDC or Azure AD configuration file (`azuread.json` or equivalent)
* Deploy configuration files to all coordinator nodes
* Restart Dremio cluster after applying changes

For complete setup steps, see [Configure Microsoft Entra ID](/current/security/authentication/identity-providers/microsoft-entra-id/).

note

All authentication setup must be done through configuration files before enabling SSO in Power BI.

The following steps configure the Power BI side of SSO. These steps assume your Dremio deployment is already configured to authenticate users via Microsoft Entra ID.

To enable SSO for Power BI reports:

#### Enable SSO for a DirectQuery Report

To enable SSO for a report that uses DirectQuery:

1. In Power BI Service, open the workspace to which you published the report.
2. Find the dataset that is associated with the report, click the three dots next to its name, and select **Settings**.
3. In the settings for the dataset, expand **Data source credentials**.
4. Click **Edit credentials**.
5. For **Authentication method**, select **OAuth2**.
6. In the **Privacy level setting for this data source** field, ensure that **Private** is selected.
7. Select the check box **Report viewers can only access this data source with their own Power BI identities using DirectQuery**.
8. Click **Sign in**.

#### Enable SSO for Reports with Power BI Gateway

To enable SSO when you are using Power BI Gateway:

1. In Power BI Service, open the workspace to which you published the report.
2. Find the dataset that is associated with the report, click the three dots next to its name, and select **Settings**.
3. In the settings for the dataset, expand **Gateway connection**.
4. Recreate your data source by following these steps:

   1. Select the **Maps to** field.
   2. Select **Manually add to gateway**.
   3. For **Data Source Name**, enter a name for the data source.
   4. For **Data Source Type**, select **Dremio Software**.
   5. For **Server**, enter your Dremio hostname with the `adbc://` prefix. Example: `adbc://acme-company.dremio.com`
   6. For **Authentication Method**, select **OAuth2**.
   7. Click **Add**.
5. In the **Data source credentials** section, click **Edit credentials**.
6. For **Authentication method**, select **OAuth2**.
7. In the **Privacy level setting for this data source** field, ensure that **Private** is selected.
8. Select the check box **Report viewers can only access this data source with their own Power BI identities using DirectQuery**.
9. Click **Sign in**.

note

SSO requires the OAuth2 authentication method. Basic authentication and personal access tokens do not support SSO when used through Power BI Gateway.

## Arrow Database Connectivity (ADBC) Limitations

* ADBC is not enabled by default. It must be enabled by the owner of the report.
* NativeQuery is not supported.
* Metadata calls are not cached.
* Power BI Desktop occasionally caches errors that might affect future connection attempts until the cache is cleared.
* Complex data types such as `MAP` and `INTERVAL` are not supported.
* When using DirectQuery, chaining functions is supported, but some complex scenarios may not work as expected. Complex optional parameters for functions are not supported.

## Troubleshoot Power BI

### Cached Data Issues

If you have previously installed older versions of Power BI Desktop, cached data may interfere with the newer versions of the Flight SQL drivers resulting in connection errors.

#### Problem

For example, when using Flight SQL ADBC, cached connection data in Power BI could cause the following errors:

* `ADBC: IOError [] [FlightSQL] [FlightSQL] unresolved address (Unavailable; GetObjects(GetDBSchemas))`
* `ADBC: IOError [] [FlightSQL] [FlightSQL] connection error: desc = "transport: authentication handshake failed: credentials: cannot check peer: missing selected ALPN property. If you upgraded from a grpc-go version earlier than 1.67, your TLS connections may have stopped working due to ALPN enforcement. For more details, see: https://github.com/grpc/grpc-go/issues/434" (Unavailable; GetObjects(GetDBSchemas))"`

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
    Source = DremioCloud.DatabasesByServerV370("your-server-here", [  
        MaxMessageSize = 67108864  // 64 MiB  
    ])  
in  
    Source
```

Replace `your-server-here` with your actual Dremio server address. The `MaxMessageSize` parameter sets the maximum message size in bytes (67108864 = 64 MiB).

Was this page helpful?

[Previous

Microsoft Excel PowerPivot](/current/client-applications/microsoft-excel/microsoft-excel-powerpivot)[Next

Microstrategy Workstation](/current/client-applications/microstrategy)

* Supported Authentication Methods
* Connect to Dremio from Power BI
  + Create a Live Connection to a Dataset from Dremio
* Power BI Gateway
* Advanced Configuration
  + Enable Connectivity with ADBC
  + Enable the `.pbids` File Download in the Dremio Console
  + Enable SSO to Dremio from Power BI
* Arrow Database Connectivity (ADBC) Limitations
* Troubleshoot Power BI
  + Cached Data Issues
  + Large Result Sets

---

# Source: https://docs.dremio.com/current/client-applications/drivers/arrow-flight-sql-jdbc-driver

Version: current [26.x]

On this page

# Arrow Flight SQL JDBC

The Arrow Flight SQL JDBC driver is an open-source driver that is based on the specifications for the Java Database Connectivity (JDBC) API. However, the Flight SQL JDBC driver uses Apache Arrow, so it is able to move large amounts of data faster, in part because it does not need to serialize and then deserialize data.

This driver solves a problem that is common to many BI tools that access databases through JDBC. These tools bundle a different JDBC driver for each type of database they support, because each of these databases has their own proprietary driver. Bundling multiple JDBC drivers for multiple databases can be difficult to maintain, and responding to support issues for multiple drivers can be costly. Now, provided that a database has an Apache Arrow Flight SQL endpoint enabled, the JDBC driver can connect to it.

This driver is developed and maintained by the Apache Arrow community. For full technical documentation, see Apache's [Arrow Flight SQL JDBC Driver](https://arrow.apache.org/docs/java/flight_sql_jdbc_driver.html). For Dremio-specific compatibility, version guidance, and release notes, see Dremio's [Arrow Flight SQL JDBC Release Notes](/current/release-notes/arrow-flight-sql-jdbc).

This driver is licensed under [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).

tip

Query planning is done on the specified node. To distribute query planning for JDBC connections, configure [secondary coordinator nodes](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/#dremio-coordinators) for your deployment.

## Prerequisites

* One of the following operating systems: Windows, MacOS, or Linux
* Supported Java versions: Java 11+
* Supported JDK versions: 11, 17, and 21
* Requires the following option to be present:

  Java 11+ Requirement

  ```
  --add-opens=java.base/java.nio=ALL-UNNAMED
  ```

## Supported Authentication Methods

* Use the username and password of the Dremio account that you want to connect with.
* Use a username and personal access token (PAT).
* Use an OAuth Access Token

### Username and Password

Pass a username and password with the `user` and `password` properties.

### Personal Access Tokens Enterprise

Pass a username and personal access token (PAT) with the `user` and `password` properties. You must URL-encode PATs that you include in JDBC URLs. To encode a PAT locally on your system, you can follow the steps in URL-encoding Values. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for enabling and creating PATs.

tip

Dremio recommends OAuth access tokens to improve security by reducing the risk of compromised passwords or personal access tokens.

### OAuth Access Tokens Enterprise

To create a connection with an OAuth access token, configure the following properties:

* `token` property with the vaue of the OAuth access token.
* `user` property with the empty string `""` to default to the username included in the access token. If the username is configured in the property value, it must match the username in the access token.

Example Arrow Flight SQL JDBC Connection Using OAuth Access Token

```
import jaydebeapi  
jdbc_arrow_flight_url = "jdbc:arrow-flight-sql://{}:{}".format("localhost", 32010)  
jdbc_arrow_flight_args = { "user": "", "token": dremio_access_token }  
jdbc_driver_location_example = "/Users/me/workspace/drivers/flight-sql-jdbc-driver-18.3.0.jar"  
jdbc_arrow_flight_conn = jaydebeapi.connect("org.apache.arrow.driver.jdbc.ArrowFlightJdbcDriver",  
                                            jdbc_arrow_flight_url,  
                                            jdbc_arrow_flight_args,  
                                            jdbc_driver_location_example)
```

Users can create OAuth access tokens using a local or LDAP username and password, a PAT, or an external JWT. Dremio provides [sample code](/current/reference/api/oauth-token/) for each of these cases.

## Connecting to Databases

* Use this template to create a direct connection to a database that has enabled an Apache Arrow Flight SQL endpoint:

  Create direct connection to database

  ```
  jdbc:arrow-flight-sql://<hostname-or-IP-address>:<port-number>/?useEncryption=false[&schema=<optional_schema>][&<properties>]
  ```

  + `<optional_schema>`: The name of the schema (datasource or space, including child paths, such as `myDatasource.folder1` and `mySpace.folder1.folder2`) to use by default when a schema is not specified in a query.
  + `<properties>`: A list of JDBC properties. Values must be URI-encoded.
* Use this template to create a direct connection to a Dremio coordinator node:

  Create direct connection to Dremio coordinator node

  ```
  jdbc:arrow-flight-sql://<Dremio_coordinator>:32010[/?schema=<optional_schema>][&<properties>]
  ```

  + `<Dremio_coordinator>`: The hostname or IP address of the coordinator node in your Dremio cluster.
  + `<optional_schema>`: The name of the schema (datasource or space, including child paths, such as `myDatasource.folder1` and `mySpace.folder1.folder2`) to use by default when a schema is not specified in a query.
  + `<properties>`: A list of JDBC properties. Values must be URL-encoded. See URL-encoding Values for suggested steps.

## Downloading the Driver

To download the driver, go to [Apache Arrow Flight SQL JDBC](https://www.dremio.com/drivers/jdbc/).

## Integrating the driver

To integrate the driver into your development environment, add it to your classpath.

## Name of the Class

The name of the class is `org.apache.arrow.driver.jdbc.ArrowFlightJdbcDriver`.

## JDBC Properties for Dremio Wire Encryption

If you are setting up encrypted communication between your JDBC client applications and the Dremio server, use the SSL JDBC connection parameters and fully qualified hostname to
configure the JDBC connection string and connect to Dremio.

note

This driver does not yet support these features:

* Disabling host verification
* Impersonation

| Properties | Value | Required | Description |
| --- | --- | --- | --- |
| `useEncryption` | `true` or `false` | [Optional] | If `true`, SSL is enabled. If set to `false`, SSL is not enabled. The default is `true`. If you do not want to use encryption, you must set the value to `false`. |
| `disableCertificateVerification` | `true` or `false` | [Optional] | If `true`, Dremio does not verify the host certificate against the truststore. The default value is `false`. |
| `trustStoreType` | string | [Optional] | Default: JKS The trustStore type. Allowed values are : `JKS`, `PKCS12`   If the useSystemTrustStore option is set to true (on Windows only), the allowed values are: `Windows-MY`, `Windows-ROOT`  Import the certificate into the **Trusted Root Certificate Authorities** and set `trustStoreType=Windows-ROOT`.  Also import the certificate into **Trusted Root Certificate Authorities** or **Personal** and set `trustStoreType=Windows-MY`. |
| `trustStore` | string | [Optional] | Path to the truststore.  If not provided, the default Java truststore is used (usually `$JAVA_HOME/lib/security/cacerts`) and the trustStorePassword parameter is ignored. |
| `useSystemTrustStore` | `true` or `false` | [Optional] | By default, the value is `true`. Bypasses trustStoreType and automatically picks the correct Truststore based on the operating system: Keychain on MacOS, [Local Machine and Current User Certificate Stores](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores) on Windows, and default truststore on other operating systems. If you are using an operating system other than MacOS or Windows, you must use the `trustStorePassword` property to pass the password of the truststore. Here is an example of a connection string for Linux:  `jdbc:arrow-flight-sql://localhost:32010?trustStorePassword=Pc0_lL'Opjn$vSDcv:%Q0@@buc` |
| `trustStorePassword` | string | [Optional] | Password to the truststore. |

## Parameterized Queries with Prepared Statements

Prepared statements allow you to dynamically pass parameters to SQL queries using placeholders, ensuring safer query execution by separating the query structure from the values in parameters. With a prepared statement, you can set parameters (`?`) at runtime using set methods to reuse queries with different values.

note

This feature requires Apache Arrow 18.3.0 or later. It supports `SELECT` statements and `DML` statements.

To use parameterized queries with prepared statements, follow these steps:

1. Use the `prepareStatement()` method to define a query with parameters, which act as placeholders for dynamic values.
2. Set the values by replacing each parameter with a value using the appropriate set methods.
3. Ensure all parameters are set before running the query, with indexing starting at 1. If parameters are not set before running the query, JBDC throws an exception.
4. Call `executeQuery()` to run the SELECT query and retrieve results, or `executeUpdate()` to run the DML query and retrieve the count of modified records.

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

## Managing Workloads

Dremio administrators can use the Arrow Flight server endpoint to [manage query workloads](/current/admin/workloads/workload-management) by adding the following properties to connections created by Flight clients:

| Flight Client Property | Description |
| --- | --- |
| `ROUTING_ENGINE` | Name of the engine to use to process all queries issued during the current session. |
| `ROUTING_QUEUE` | Name of the workload management queue. Used only during authentication. |
| `ROUTING_TAG` | Tag name associated with all queries executed within a Flight session. Used only during authentication. |
| `SCHEMA` | Default schema path to the dataset that the user wants to query. |

## URL-encoding Values

To encode a personal access token (PAT) or property value locally on your system, you can follow these steps:

1. In a browser window, right-click an empty area of the page and select **Inspect**.
2. Click **Console**.
3. Type `encodeURIComponent("<PAT-or-value>")`, where `<PAT-or-value>` is the personal access token that you obtained from Dremio or the value of a supported JDBC property. The URL-encoded PAT or value appears on the next line. You can highlight it and copy it to your clipboard.

## Differences between the Arrow Flight SQL JDBC Driver and the Legacy Dremio JDBC Driver

The Arrow Flight SQL JDBC driver differs from the Dremio JDBC driver (legacy) in the following:

* Requires Java 11+.
* Supports `ResultSet.getBoolean()` on `varchar` columns in which boolean values are represented as these strings: "0", "1", "true", "false".
* Supports null Calendar in calls to `ResultSet.getDate()`, `ResultSet.getTime()`, and `ResultSet.getTimestamp()`  
  When a call to one of these methods has no `Calendar` parameter, or the `Calendar` parameter is `null`, the Flight JDBC driver uses the default timezone when it constructs the returned object.
* Supports `ResultSet.getDate()`, `ResultSet.getTime()`, and `ResultSet.getTimestamp()` on `varchar` columns in which dates, times, or timestamps are represented as strings.
* Supports varchar values that represents numeric values in calls to `ResultSet.getInteger()`, `ResultSet.getFloat()`, `ResultSet.getDouble()`, `ResultSet.getShort()`, `ResultSet.getLong()`, and `ResultSet.getBigDecimal()`
* Supports integer values in calls to `getFloat()`  
  Integers returned gain one decimal place.
* Supports the native SQL complex types `List`, `Map`, and `Struct`  
  The Dremio JDBC driver (legacy) uses String representations of these types.
* Supports using the Interval data type in SQL functions.
* Removes support for calling `ResultSet.getBinaryStream()` on non-binary data types. Though such support exists in traditional JDBC drivers, it is not in the specification for the JDBC API.

note

Calling `DatabaseMetadata.getCatalog()` when connected to Dremio returns empty. Other `DatabaseMetadata` methods return null values in the `TABLE_CAT` column. This is expected behavior because Dremio does not have a catalog.

## Limitations

Impersonation is not supported.

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

Was this page helpful?

[Previous

Drivers](/current/client-applications/drivers/)[Next

Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver)

* Prerequisites
* Supported Authentication Methods
  + Username and Password
  + Personal Access Tokens Enterprise
  + OAuth Access Tokens Enterprise
* Connecting to Databases
* Downloading the Driver
* Integrating the driver
* Name of the Class
* JDBC Properties for Dremio Wire Encryption
* Parameterized Queries with Prepared Statements
  + Supported Data Types and Set Methods
  + Limitations
* Managing Workloads
* URL-encoding Values
* Differences between the Arrow Flight SQL JDBC Driver and the Legacy Dremio JDBC Driver
* Limitations
* Supported Conversions from Dremio Datatypes to JDBC Datatypes

---

# Source: https://docs.dremio.com/current/client-applications/drivers/jdbc

Version: current [26.x]

On this page

# Dremio JDBC Driver (Legacy)

note

The [Arrow Flight SQL JDBC driver](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver) is recommended for use for connectivity to Dremio. If you are using a client application that bundles or is certified with the Dremio JDBC driver, you can continue to use this driver. The Dremio JDBC driver will be not enhanced or fixed with the exception of critical security fixes.

The legacy [Dremio JDBC driver](https://download.dremio.com/jdbc-driver/?_ga=2.109401093.1016122501.1667783452-235854462.1630284576&_gac=1.258688760.1664550761.CjwKCAjwp9qZBhBkEiwAsYFsb0x4InlcRP7Rv4XsjamZQHhJILHJWOtBOu30xZC1QwvEXF8cPFs1HhoCB-kQAvD_BwE) is included as a part of Dremio installations under `<DREMIO_HOME>/jars/jdbc-driver/`. The main JAR Class is `com.dremio.jdbc.Driver`. You can also download the JDBC driver from [here](https://download.dremio.com/jdbc-driver/). This driver is licensed under [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).

A new version of the JDBC driver is made available with every release of Dremio software. However, this doesn't mean changes or new features were introduced in a driver release. Only when actual changes are made to a driver will the [JDBC driver release notes](/current/release-notes/arrow-flight-sql-jdbc) be published.

## Prerequisites

* As of Dremio JDBC driver 25.0+, supported Java versions: Java 11+
* Supported JDK versions: 11, 17, and 21
* Requires the following option to be present:

  Java 11+ Requirement

  ```
  --add-opens=java.base/java.nio=ALL-UNNAMED
  ```

## Supported Authentication Methods

### Username and Password

Use the username and password of the Dremio account that you want to connect with.

### Personal Access Tokens Enterprise

Use a username and personal access token (PAT). To generate a PAT, see [Creating a PAT](/current/security/authentication/personal-access-tokens/#creating-a-pat).

tip

Dremio recommends OAuth access tokens to improve security by reducing the risk of compromised passwords or personal access tokens.

### OAuth Access Tokens Enterprise

To create a connection with an OAuth access token, configure the following properties:

* `token_type` with a value of `access_token`
* `password` with the value of the access token
* `user` with an empty string `""` to default to the username included in the access token. If the username is configured in the property value, it must match the username in the access token.

Example Legacy JDBC Connection Using Dremio Access Token

```
import jaydebeapi  
jdbc_url = "jdbc:dremio:direct={}:{}".format("localhost", 31010)  
jdbc_args = {"user": "", "password": dremio_access_token, "token_type": "access_token"}  
jdbc_driver_location_example = "/Users/me/workspace/drivers/dremio-jdbc-driver-25.3.0-SNAPSHOT.jar"  
jdbc_conn = jaydebeapi.connect("com.dremio.jdbc.Driver",  
                               jdbc_url,    
                               jdbc_args,  
                               jdbc_driver_location_example)
```

Users can create OAuth access tokens using a local or LDAP username and password, a PAT, or an external JWT. Dremio provides [sample code](/current/reference/api/oauth-token) for each of these cases.

### External JWT

To use an external JWT directly from an [external token provider](/current/security/authentication/application-authentication/external-token), configure the following properties:

* `token_type` with a value of `jwt`
* `password` with the value of the external JWT
* `user` with the empty string `""` to default to the username included in the external JWT. If the username is configured in the property value, it must match the username in the external JWT.

Dremio provides [sample code](/current/security/authentication/application-authentication/external-token#retrieving-an-external-jwt) for requesting an external JWT from Microsoft Entra ID.

tip

Dremio recommends OAuth access tokens obtained through token exchange over an external JWT. The Dremio OAuth access token is typically smaller than an external JWT and verification is faster.

## Setup

You can set up the JDBC driver in the following manner:

* Connect directly to the Dremio server
* Connect to the Dremio server via Zookeeper

**Tip:** To distribute query planning for JDBC connections, configure [secondary coordinator nodes](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/#dremio-coordinators) for your deployment.

#### Connecting directly to Dremio

The following configuration establishes a direct connection to a Dremio coordinator node.
Planning is done on the specified node.

Connect directly to Dremio coordinator node

```
jdbc:dremio:direct=<DREMIO_COORDINATOR>:31010[;schema=<OPTIONAL_SCHEMA>]
```

#### Connecting to ZooKeeper

The following configuration establishes a distributed connection to Dremio coordinator nodes through a
Zookeeper quorum. Planning is distributed across the available coordinator nodes.

Connect to Dremio coordinator node with ZooKeeper

```
jdbc:dremio:zk=<ZOOKEEPER_QUORUM>:2181[;schema=<OPTIONAL_SCHEMA>]
```

**Multiple Dremio Clusters in the same ZooKeeper Quorum**

Cluster A

```
jdbc:dremio:zk=<ZOOKEEPER_QUORUM>:2181/path/to/ClusterA
```

Cluster B

```
jdbc:dremio:zk=<ZOOKEEPER_QUORUM>:2181/path/to/ClusterB
```

## Construct a Prepared Statement with Dynamic Parameters

Dremio supports using parameters in prepared statements for SELECT queries.

The parameter marker is `?` in prepared statements. To execute a prepared statement, you must set the parameter marker with one of the [supported set methods](/current/client-applications/drivers/jdbc/#set-methods-for-prepared-statements-with-parameters).

The example below uses the Date type parameter and the `setDate` set method. For set methods, the first argument is the index of the parameter marker in the SQL query, starting from 1. The second argument is the value for the parameter marker. After you set the parameter, you can execute the prepared statement by calling the `executeQuery()` method on the prepared statement.

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

### Set Methods for Prepared Statements with Parameters

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

## JDBC Parameters for Dremio Wire Encryption

If you are setting up encrypted communication between your JDBC client applications and the Dremio server,
use the SSL JDBC connection parameters and a fully qualified host name to
configure the JDBC connection string and connect to Dremio:

| Parameter | Value | Required | Description |
| --- | --- | --- | --- |
| ssl | true/false | [Optional] | If true, SSL is enabled. If not set or set to false, SSL is not enabled. |
| trustStoreType | string | [Optional] | Default: JKS The trustStore type. Allowed values are : JKS PKCS12   If the useSystemTrustStore option is set to true (on Windows only), the allowed values are: Windows-MY Windows-ROOT  Import the certificate into the **Trusted Root Certificate Authorities** and set `trustStoreType=Windows-ROOT`.  Also import the certificate into **Trusted Root Certificate Authorities** or **Personal** and set `trustStoreType=Windows-MY`. |
| trustStore | string | [Optional] | Path to the truststore.  If not provided, the default Java truststore is used (usually $JAVA\_HOME/lib/security/cacerts) and the trustStorePassword parameter is ignored. |
| useSystemTrustStore | true/false | [Optional] | By default, the value is `true`. Bypasses trustStoreType and automatically picks the correct Truststore based on the operating system: Keychain on MacOS, [Local Machine and Current User Certificate Stores](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores) on Windows, and default truststore on other systems. |
| trustStorePassword | string | [Optional] | Password to the truststore. |
| disableHostVerification | true/false | [Optional] | If true, Dremio does not verify that the host in the certificate is the host we are connecting to. False by default.   (Hostname verification follows the specification in RFC2818) |
| disableCertificateVerification | true/false | [Optional] | If true, Dremio does not verify the host certificate against the truststore. False by default. |

## Optional Advanced JDBC Driver Properties

| Parameter | Value | Description |
| --- | --- | --- |
| impersonation\_target | string | When inbound impersonation is configured, `impersonation_target` is used for authorization, so it must have permission to the queried datasets, and `impersonation_target` appears as the identity that submitted the queries. The username used to establish the connection must be mapped to `impersonation_target` in the impersonation policy for the Dremio service, otherwise, the connection fails with an authorization error. In the policy, the user used to establish the connection is the `proxy_principle` and `impersonation_target` is its `target_principle`. For more information on configuring policies, see [Inbound Impersonation](/current/security/rbac/inbound-impersonation). |
| routing\_queue | string | Specifies the queue to use for processing queries while a connection is open. For more information, see [Query Tagging & Direct Routing Configuration](/current/admin/workloads/workload-management/#query-tagging--direct-routing-configuration). |
| routing\_tag | string | Sets a tag for rule processing. The specified tag is associated with all queries executed while a connection is open. Rules can check for the presence of a tag with the function `tag()`. For more information, see [Query Tagging & Direct Routing Configuration](/current/admin/workloads/workload-management/#query-tagging--direct-routing-configuration). |
| token\_type | string | The type of the token in the `password` field. Valid values are `jwt` for [external tokens](/current/security/authentication/application-authentication/external-token), `access_token` for OAuth access token, or `personal_access_token` for [personal access tokens](/current/security/authentication/personal-access-tokens/). If you are using your Dremio password, omit the `token_type` property. |

## SOCKS Proxy Connection Parameters

If you want to connect to Dremio Cloud through a SOCKS proxy, use these connection parameters:

| Parameter | Type | Description | Default Value | Required? |
| --- | --- | --- | --- | --- |
| socksProxyHost | string | The IP address or hostname of the SOCKS proxy. | N/A | Yes |
| socksProxyPort | integer | The port to use on the SOCKS proxy. | 1080 | No |
| socksProxyUsername | string | The username to use for connections. | N/A | No |
| socksProxyPassword | string | The password to use for connections. | N/A | Only if a username is specified. |

Was this page helpful?

[Previous

Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver)

* Prerequisites
* Supported Authentication Methods
  + Username and Password
  + Personal Access Tokens Enterprise
  + OAuth Access Tokens Enterprise
  + External JWT
* Setup
* Construct a Prepared Statement with Dynamic Parameters
  + Set Methods for Prepared Statements with Parameters
* JDBC Parameters for Dremio Wire Encryption
* Optional Advanced JDBC Driver Properties
* SOCKS Proxy Connection Parameters

---

# Source: https://docs.dremio.com/current/client-applications/drivers/arrow-flight-sql-odbc-driver

Version: current [26.x]

On this page

# Arrow Flight SQL ODBC

Starting with Dremio v22.0, you can use the Arrow Flight SQL ODBC driver to connect to Dremio from ODBC client applications. This driver is licensed under [GNU Library General Public License, Version 2](https://github.com/dremio/warpdrive/blob/master/license.txt).

## Supported Operating Systems

You can use the driver on systems that run the following 64-bit operating systems:

* Linux: RedHat/CentOS
* Windows 10 and later
* macOS (Intel processors only)

Apple Silicon Compatibility

The Arrow Flight SQL ODBC driver is not supported on Apple Silicon M1, M2, and M3 processors. While previous workarounds using Rosetta may have been available, they are no longer reliable and may not work with current versions. For Apple Silicon Mac computers, consider using alternative connection methods such as the [Arrow Flight SQL JDBC driver](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/).

## Authentication Methods

Dremio supports several authentication methods for client connections.

### Username and Password

Pass a username and password with the **UID** and **PWD** properties.

### Personal Access Tokens Enterprise

Pass a username and personal access token (PAT) with the **UID** and **PWD** properties, respectively. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for enabling and creating PATs.

tip

Dremio recommends OAuth access tokens to improve security by reducing the risk of compromised passwords or personal access tokens.

### OAuth Access Tokens Enterprise

To create a connection with an OAuth access token, configure the **TOKEN** property with the value of the OAuth access token.

Example Arrow Flight SQL ODBC Connection using OAuth Access Tokens

```
import pyodbc  
  
with pyodbc.connect(  
        # Default location on Linux  
        Driver='/opt/arrow-flight-sql-odbc-driver/lib64/libarrow-odbc.so.0.9.1.168',  
        HOST='my.odbc.host',  
        PORT=32010,  
        useEncryption='true',  
        TOKEN=dremio_access_token,  
        autocommit=True,  
    ) as conn:  
        with conn.cursor() as cursor:  
            cursor.execute('select * from test_table')  
            results = cursor.fetchall()
```

Users can create OAuth access tokens using a local or LDAP username and password, a PAT, or an external JWT. Dremio provides [sample code](/current/reference/api/oauth-token/) for each of these cases.

## Downloading and Installing

* Windows
* Linux
* macOS

### Downloading and Installing on Windows

note

The Arrow Flight SQL ODBC driver is not available for 32-bit Windows versions.

note

If you plan to use Microsoft Power BI Desktop April 2022 or later to connect to Dremio, you do not need to use this driver. Power BI Desktop April 2022 and later includes a connector that you can use to connect to Dremio. See [Connecting from Microsoft Power BI](/current/client-applications/microsoft-power-bi/).

To download and install the Arrow Flight SQL ODBC driver:

1. Download the Windows 64-bit version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Run the installer.
3. (Optional) In the **User Account Control** page, click **Yes**. This page appears only if there is user account control configured on your Windows machine.
4. In the **Welcome to Dremio** page, click **Next**.
5. Click **Install**.
6. In the **Installation Complete** page, click **Next**.
7. In the **Completing Arrow Flight SQL ODBC Driver Setup Wizard** page, click **Finish**.

Next, configure the driver.

### Downloading and Installing on Linux

To download and install the Arrow Flight SQL ODBC driver:

1. Download the Linux version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Run the following command to install the driver and automatically create the data source name (DSN) `Arrow Flight SQL ODBC DSN`:

   Install driver and create data source name (DSN)

   ```
   sudo yum localinstall <dremio-odbc-rpm-path>
   ```

Next, configure the driver.

### Downloading and Installing on macOS

To download and install the Arrow Flight SQL ODBC driver:

Intel Macs Only

This driver only supports Intel-based Macs. It is not compatible with Apple Silicon M1, M2, and M3 processors.

1. Download the macOS version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Go to the download location and double-click the downloaded `.dmg` file.
3. Double-click the `.pkg` file.
4. In the **Welcome to the ODBC Driver for Arrow Flight SQL Installer** page, click **Continue**.
5. In the **Standard Install on "Macintosh HD"** page, Click **Install**. Optionally, if you want to change the install location, click **Change Install Location** and navigate to the new location.
6. In the **Installer is trying to install new software** dialog, specify your macOS password. Then, click **Install Software**.
7. After the installation is complete, click **Close**.

Next, configure the driver.

## Configuring

### Configuring on Windows

To configure the System DSN:

danger

Do not follow these steps if you are using Microsoft Power BI Desktop to connect to Dremio. For the steps for configuring Power BI, see [Connecting from Microsoft Power BI](/current/client-applications/microsoft-power-bi/).

note

If you want to use a personal access token (PAT), rather than a password, for authenticating to Dremio, generate a PAT. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for the steps.

1. Go to **Start Menu** > **Window Administrative Tools**. Click **ODBC Data Sources (64-bit)**.
2. In the **ODBC Data Source Administrator (64-bit)** dialog, click **System DSN**.
3. Select **Arrow Flight SQL ODBC DSN** and click **Configure**.
4. In the **HOST** field, specify the hostname of the server or its IP address.
5. In the **PORT** field, specify the port to use for connections from Arrow Flight SQL ODBC client applications, which is 32010 by default.
6. Specify client information in the appropriate fields for your authentication type:

   | Field | Username and Password | Personal Access Token | OAuth Access Token |
   | --- | --- | --- | --- |
   | **UID** | Username | Username | Do not specify |
   | **PWD** | Password | Personal access token | Do not specify |
   | **TOKEN** | Do not specify | Do not specify | OAuth access token |
7. In the **UseEncryption** field, specify one of these values:

   * `true`, if Dremio is configured for encrypted communication with your Arrow Flight SQL ODBC client applications.
   * `false`, if Dremio is not configured for encrypted communication with your Arrow Flight SQL ODBC client applications. Dremio is unencrypted by default.

For additional parameters, see Connection Parameters.

If you ever need to enable tracing for troubleshooting problems with the driver, click the **Tracing** tab in the **ODBC Data Source Administrator (64-bit)** dialog, set the log-file path, and then click **Start Tracing Now**.

### Configuring on Linux

note

* Before configuring, ensure that unixODBC is installed.
* If you want to base your configuration on examples, copy the content of the `odbc.ini` and `odbcinst.ini` files in the `/opt/arrow-flight-sql-odbc-driver/conf` directory and paste the content into your system `/etc/odbc.ini` and `/etc/odbcinst.ini` files.

To configure the properties in the odbc.ini file:

1. In the **HOST** field, specify the hostname of the server or its IP address.
2. In the **PORT** field, specify the port to use for connections from Arrow Flight SQL ODBC client applications, which is 32010 by default.
3. Specify client information in the appropriate fields for your authentication type:

   | Field | Username and Password | Personal Access Token | OAuth Access Token |
   | --- | --- | --- | --- |
   | **UID** | Username | Username | Do not specify |
   | **PWD** | Password | Personal access token | Do not specify |
   | **TOKEN** | Do not specify | Do not specify | OAuth access token |
4. In the **UseEncryption** field, specify one of these values:

   * `true`, if Dremio is configured for encrypted communication with your Arrow Flight SQL ODBC client applications.
   * `false`, if Dremio is not configured for encrypted communication with your Arrow Flight SQL ODBC client applications. Dremio is unencrypted by default.

For additional parameters, see Connection Parameters.

note

To find out unixODBC has created your `odbc.ini` and `odbcinst.ini` files, run this command:

```
odbcinst -j
```

If you ever need to enable tracing for troubleshooting problems with the driver, see the help for unixODBC.

### Configuring on macOS

note

Before configuring, ensure that [ODBC Manager](http://www.odbcmanager.net/) is installed.

1. Launch ODBC Manager.
2. On the System DSN page, select **Arrow Flight SQL ODBC DSN** and click **Configure**.
3. (Optional) Change the DSN.
4. In the **Host** field, specify the hostname of the server or its IP address.
5. In the **Port** field, specify the port to use for connections from Arrow Flight SQL ODBC client applications, which is 32010 by default.
6. Specify client information in the appropriate fields for your authentication type:

   | Field | Username and Password | Personal Access Token | OAuth Access Token |
   | --- | --- | --- | --- |
   | **UID** | Username | Username | Do not specify |
   | **PWD** | Password | Personal access token | Do not specify |
   | **TOKEN** | Do not specify | Do not specify | OAuth access token |
7. In the **UseEncryption** field, specify one of these values:

   * `true`, if Dremio is configured for encrypted communication with your Arrow Flight SQL ODBC client applications.
   * `false`, if Dremio is not configured for encrypted communication with your Arrow Flight SQL ODBC client applications. Dremio is unencrypted by default.

For additional parameters, see Connection Parameters.

If you ever need to enable tracing for troubleshooting problems with the driver, see the help for your driver manager.

## Connection Parameters

### Primary Connection Parameters

Use these parameters to configure basic connection details such as what data source to connect with.

note

The Arrow Flight SQL ODBC driver does not support password-protected `.pem` / `.crt` files or multiple `.crt` certificates in a single `.pem` / `.crt` file.

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Host | string | Sets the IP address or hostname for the Dremio server. If you specify an IP address and you set the TLS connection parameter `useEncryption` to `true`, ensure that the `/etc/hosts/` file includes an entry to map the IP address to the host. | None |
| Port | integer | Sets the TCP port number that Dremio uses to listen to connections from Arrow Flight SQL ODBC clients. | 32010 |
| Schema | string | Provides the name of the database schema to use by default when a schema is not specified in a query. However, this does not prevent queries from being issued for otsher schemas. Such queries must explicitly include the schema. | None |

Specify client information in the appropriate fields for your authentication type:

| Field | Username and Password | Personal Access Token | OAuth Access Token |
| --- | --- | --- | --- |
| **UID** | Username | Username | Do not specify |
| **PWD** | Password | Personal access token | Do not specify |
| **TOKEN** | Do not specify | Do not specify | OAuth access token |

### TLS Connection Parameters

Use the following parameters to configure TLS encryption and verification methods for regular connections.

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| useEncryption | integer | Configures the client to use a TLS-encrypted connection to communicate with the Dremio server. Accepted values:  * `true`, the client communicates with the Dremio server only using TLS encryption. This is the default value. Therefore, communication between the client application and your Dremio server must be encrypted if you do not override this default value. See the configuration of Arrow Flight TLS for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#arrow-flight-and-arrow-flight-sql-jdbc-and-odbc-enterprise) for more information. * `false`, TLS encryption is disabled with the client. If you specify this value, ensure that the encryption of communication between the client application and your Dremio server is not configured. | true |
| disableCertificateVerification | integer | Specifies whether the driver should verify the host certificate against the trust store. Accepted values:  * `false`, the driver verifies the certificate against the trust store. * `true`, the driver does not verify the certificate against the trust store. | false |
| useSystemTrustStore | integer | Controls whether to use a CA certificate from the system's trust store, or from a specified `.pem` file. Accepted values:  * `true`, the driver verifies the connection using a certificate in the system trust store. * `false`, the driver verifies the connection using the `.pem` file specified by the `trustedCerts` parameter. | `true` on Windows and macOS, `false` on Linux (which does not have a system truststore) |
| trustedCerts | string | The full path of the `.pem` file containing certificates trusted by a CA, for the purpose of verifying the server. If this option is not set, the driver defaults to using the trusted CA certificates `.pem` file installed by the driver. The exact file path varies according to the operating system on which the driver is installed. The path for the Windows driver differs from the path set for the macOS driver. The TLS connection fails if you do not specify a value when `useEncryption` is `true` and `disableCertificateVerification` is `false`. | N/A |
| hideSQLTablesListing | boolean | Prevents Microsoft Excel 16.95+ from crashing by hiding the list of available sources in Microsoft Excel’s Query Dialog. Set to `true` to enable. Only for Intel-based Mac computers. | `false` |

### Advanced Parameters

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| quoting | string | Specifies which type of character to use to delimit values in queries. The value can be BACK\_TICK, BRACKET, or DOUBLE\_QUOTE. | DOUBLE\_QUOTE |
| routing\_queue | string | Specifies the queue to route queries to during a session. Direct Routing is used to specify the exact queue and execution cluster to run queries on for a given ODBC session. With Direct Routing, workload-management (WLM) rules are not considered; instead, queries are routed directly to the specified queue. For more information, see [Workload Management](/current/admin/workloads/workload-management/). | N/A |
| routing\_tag | string | When this parameter is set, the specified tag is associated with all queries executed within a session. Rules can check for the presence of a tag with the function "tag()". For more information, see [Workload Management](/current/admin/workloads/workload-management/). | N/A |
| stringColumnLength | string | The maximum length of data in columns of the STRING datatype and of complex datatypes. The range is 1 to 2147483647. | 1024. |

## Logging

You can inspect and extract client-side driver logs through the macOS logging infrastructure, because every macOS installation comes with an embedded Console application that allows you to filter by log types. This feature is only available for Intel-based Mac computers, and the log activity of the ODBC driver mostly consists of ODBC API calls.

To start logging:

1. Open the Console application.
2. In the search box, select **Excel** in the **PROCESS** dropdown, and **odbc** in the **ANY** dropdown.

   ![Filter by Excel and ODBC for logs in the Console application.](/images/odbc-driver-log-excel-filter.png "Logging Filter")
3. Click **Start**.

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

[Previous

Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver)[Next

Dremio JDBC Driver (Legacy)](/current/client-applications/drivers/jdbc)

* Supported Operating Systems
* Authentication Methods
  + Username and Password
  + Personal Access Tokens Enterprise
  + OAuth Access Tokens Enterprise
* Downloading and Installing
  + Downloading and Installing on Windows
  + Downloading and Installing on Linux
  + Downloading and Installing on macOS
* Configuring
  + Configuring on Windows
  + Configuring on Linux
  + Configuring on macOS
* Connection Parameters
  + Primary Connection Parameters
  + TLS Connection Parameters
  + Advanced Parameters
* Logging
* Supported Conversions from Dremio Datatypes to ODBC Datatypes

---

# Source: https://docs.dremio.com/current/client-applications/drivers/arrow-flight-sql-odbc-driver/

Version: current [26.x]

On this page

# Arrow Flight SQL ODBC

Starting with Dremio v22.0, you can use the Arrow Flight SQL ODBC driver to connect to Dremio from ODBC client applications. This driver is licensed under [GNU Library General Public License, Version 2](https://github.com/dremio/warpdrive/blob/master/license.txt).

## Supported Operating Systems

You can use the driver on systems that run the following 64-bit operating systems:

* Linux: RedHat/CentOS
* Windows 10 and later
* macOS (Intel processors only)

Apple Silicon Compatibility

The Arrow Flight SQL ODBC driver is not supported on Apple Silicon M1, M2, and M3 processors. While previous workarounds using Rosetta may have been available, they are no longer reliable and may not work with current versions. For Apple Silicon Mac computers, consider using alternative connection methods such as the [Arrow Flight SQL JDBC driver](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/).

## Authentication Methods

Dremio supports several authentication methods for client connections.

### Username and Password

Pass a username and password with the **UID** and **PWD** properties.

### Personal Access Tokens Enterprise

Pass a username and personal access token (PAT) with the **UID** and **PWD** properties, respectively. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for enabling and creating PATs.

tip

Dremio recommends OAuth access tokens to improve security by reducing the risk of compromised passwords or personal access tokens.

### OAuth Access Tokens Enterprise

To create a connection with an OAuth access token, configure the **TOKEN** property with the value of the OAuth access token.

Example Arrow Flight SQL ODBC Connection using OAuth Access Tokens

```
import pyodbc  
  
with pyodbc.connect(  
        # Default location on Linux  
        Driver='/opt/arrow-flight-sql-odbc-driver/lib64/libarrow-odbc.so.0.9.1.168',  
        HOST='my.odbc.host',  
        PORT=32010,  
        useEncryption='true',  
        TOKEN=dremio_access_token,  
        autocommit=True,  
    ) as conn:  
        with conn.cursor() as cursor:  
            cursor.execute('select * from test_table')  
            results = cursor.fetchall()
```

Users can create OAuth access tokens using a local or LDAP username and password, a PAT, or an external JWT. Dremio provides [sample code](/current/reference/api/oauth-token/) for each of these cases.

## Downloading and Installing

* Windows
* Linux
* macOS

### Downloading and Installing on Windows

note

The Arrow Flight SQL ODBC driver is not available for 32-bit Windows versions.

note

If you plan to use Microsoft Power BI Desktop April 2022 or later to connect to Dremio, you do not need to use this driver. Power BI Desktop April 2022 and later includes a connector that you can use to connect to Dremio. See [Connecting from Microsoft Power BI](/current/client-applications/microsoft-power-bi/).

To download and install the Arrow Flight SQL ODBC driver:

1. Download the Windows 64-bit version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Run the installer.
3. (Optional) In the **User Account Control** page, click **Yes**. This page appears only if there is user account control configured on your Windows machine.
4. In the **Welcome to Dremio** page, click **Next**.
5. Click **Install**.
6. In the **Installation Complete** page, click **Next**.
7. In the **Completing Arrow Flight SQL ODBC Driver Setup Wizard** page, click **Finish**.

Next, configure the driver.

### Downloading and Installing on Linux

To download and install the Arrow Flight SQL ODBC driver:

1. Download the Linux version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Run the following command to install the driver and automatically create the data source name (DSN) `Arrow Flight SQL ODBC DSN`:

   Install driver and create data source name (DSN)

   ```
   sudo yum localinstall <dremio-odbc-rpm-path>
   ```

Next, configure the driver.

### Downloading and Installing on macOS

To download and install the Arrow Flight SQL ODBC driver:

Intel Macs Only

This driver only supports Intel-based Macs. It is not compatible with Apple Silicon M1, M2, and M3 processors.

1. Download the macOS version of the driver from the [ODBC driver download page](https://www.dremio.com/drivers/odbc/).
2. Go to the download location and double-click the downloaded `.dmg` file.
3. Double-click the `.pkg` file.
4. In the **Welcome to the ODBC Driver for Arrow Flight SQL Installer** page, click **Continue**.
5. In the **Standard Install on "Macintosh HD"** page, Click **Install**. Optionally, if you want to change the install location, click **Change Install Location** and navigate to the new location.
6. In the **Installer is trying to install new software** dialog, specify your macOS password. Then, click **Install Software**.
7. After the installation is complete, click **Close**.

Next, configure the driver.

## Configuring

### Configuring on Windows

To configure the System DSN:

danger

Do not follow these steps if you are using Microsoft Power BI Desktop to connect to Dremio. For the steps for configuring Power BI, see [Connecting from Microsoft Power BI](/current/client-applications/microsoft-power-bi/).

note

If you want to use a personal access token (PAT), rather than a password, for authenticating to Dremio, generate a PAT. See [Personal Access Tokens](/current/security/authentication/personal-access-tokens/) for the steps.

1. Go to **Start Menu** > **Window Administrative Tools**. Click **ODBC Data Sources (64-bit)**.
2. In the **ODBC Data Source Administrator (64-bit)** dialog, click **System DSN**.
3. Select **Arrow Flight SQL ODBC DSN** and click **Configure**.
4. In the **HOST** field, specify the hostname of the server or its IP address.
5. In the **PORT** field, specify the port to use for connections from Arrow Flight SQL ODBC client applications, which is 32010 by default.
6. Specify client information in the appropriate fields for your authentication type:

   | Field | Username and Password | Personal Access Token | OAuth Access Token |
   | --- | --- | --- | --- |
   | **UID** | Username | Username | Do not specify |
   | **PWD** | Password | Personal access token | Do not specify |
   | **TOKEN** | Do not specify | Do not specify | OAuth access token |
7. In the **UseEncryption** field, specify one of these values:

   * `true`, if Dremio is configured for encrypted communication with your Arrow Flight SQL ODBC client applications.
   * `false`, if Dremio is not configured for encrypted communication with your Arrow Flight SQL ODBC client applications. Dremio is unencrypted by default.

For additional parameters, see Connection Parameters.

If you ever need to enable tracing for troubleshooting problems with the driver, click the **Tracing** tab in the **ODBC Data Source Administrator (64-bit)** dialog, set the log-file path, and then click **Start Tracing Now**.

### Configuring on Linux

note

* Before configuring, ensure that unixODBC is installed.
* If you want to base your configuration on examples, copy the content of the `odbc.ini` and `odbcinst.ini` files in the `/opt/arrow-flight-sql-odbc-driver/conf` directory and paste the content into your system `/etc/odbc.ini` and `/etc/odbcinst.ini` files.

To configure the properties in the odbc.ini file:

1. In the **HOST** field, specify the hostname of the server or its IP address.
2. In the **PORT** field, specify the port to use for connections from Arrow Flight SQL ODBC client applications, which is 32010 by default.
3. Specify client information in the appropriate fields for your authentication type:

   | Field | Username and Password | Personal Access Token | OAuth Access Token |
   | --- | --- | --- | --- |
   | **UID** | Username | Username | Do not specify |
   | **PWD** | Password | Personal access token | Do not specify |
   | **TOKEN** | Do not specify | Do not specify | OAuth access token |
4. In the **UseEncryption** field, specify one of these values:

   * `true`, if Dremio is configured for encrypted communication with your Arrow Flight SQL ODBC client applications.
   * `false`, if Dremio is not configured for encrypted communication with your Arrow Flight SQL ODBC client applications. Dremio is unencrypted by default.

For additional parameters, see Connection Parameters.

note

To find out unixODBC has created your `odbc.ini` and `odbcinst.ini` files, run this command:

```
odbcinst -j
```

If you ever need to enable tracing for troubleshooting problems with the driver, see the help for unixODBC.

### Configuring on macOS

note

Before configuring, ensure that [ODBC Manager](http://www.odbcmanager.net/) is installed.

1. Launch ODBC Manager.
2. On the System DSN page, select **Arrow Flight SQL ODBC DSN** and click **Configure**.
3. (Optional) Change the DSN.
4. In the **Host** field, specify the hostname of the server or its IP address.
5. In the **Port** field, specify the port to use for connections from Arrow Flight SQL ODBC client applications, which is 32010 by default.
6. Specify client information in the appropriate fields for your authentication type:

   | Field | Username and Password | Personal Access Token | OAuth Access Token |
   | --- | --- | --- | --- |
   | **UID** | Username | Username | Do not specify |
   | **PWD** | Password | Personal access token | Do not specify |
   | **TOKEN** | Do not specify | Do not specify | OAuth access token |
7. In the **UseEncryption** field, specify one of these values:

   * `true`, if Dremio is configured for encrypted communication with your Arrow Flight SQL ODBC client applications.
   * `false`, if Dremio is not configured for encrypted communication with your Arrow Flight SQL ODBC client applications. Dremio is unencrypted by default.

For additional parameters, see Connection Parameters.

If you ever need to enable tracing for troubleshooting problems with the driver, see the help for your driver manager.

## Connection Parameters

### Primary Connection Parameters

Use these parameters to configure basic connection details such as what data source to connect with.

note

The Arrow Flight SQL ODBC driver does not support password-protected `.pem` / `.crt` files or multiple `.crt` certificates in a single `.pem` / `.crt` file.

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Host | string | Sets the IP address or hostname for the Dremio server. If you specify an IP address and you set the TLS connection parameter `useEncryption` to `true`, ensure that the `/etc/hosts/` file includes an entry to map the IP address to the host. | None |
| Port | integer | Sets the TCP port number that Dremio uses to listen to connections from Arrow Flight SQL ODBC clients. | 32010 |
| Schema | string | Provides the name of the database schema to use by default when a schema is not specified in a query. However, this does not prevent queries from being issued for otsher schemas. Such queries must explicitly include the schema. | None |

Specify client information in the appropriate fields for your authentication type:

| Field | Username and Password | Personal Access Token | OAuth Access Token |
| --- | --- | --- | --- |
| **UID** | Username | Username | Do not specify |
| **PWD** | Password | Personal access token | Do not specify |
| **TOKEN** | Do not specify | Do not specify | OAuth access token |

### TLS Connection Parameters

Use the following parameters to configure TLS encryption and verification methods for regular connections.

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| useEncryption | integer | Configures the client to use a TLS-encrypted connection to communicate with the Dremio server. Accepted values:  * `true`, the client communicates with the Dremio server only using TLS encryption. This is the default value. Therefore, communication between the client application and your Dremio server must be encrypted if you do not override this default value. See the configuration of Arrow Flight TLS for [Dremio on Kubernetes](/current/deploy-dremio/configuring-kubernetes/#transport-level-security) or [Dremio standalone clusters](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-conf/wire-encryption-config/#arrow-flight-and-arrow-flight-sql-jdbc-and-odbc-enterprise) for more information. * `false`, TLS encryption is disabled with the client. If you specify this value, ensure that the encryption of communication between the client application and your Dremio server is not configured. | true |
| disableCertificateVerification | integer | Specifies whether the driver should verify the host certificate against the trust store. Accepted values:  * `false`, the driver verifies the certificate against the trust store. * `true`, the driver does not verify the certificate against the trust store. | false |
| useSystemTrustStore | integer | Controls whether to use a CA certificate from the system's trust store, or from a specified `.pem` file. Accepted values:  * `true`, the driver verifies the connection using a certificate in the system trust store. * `false`, the driver verifies the connection using the `.pem` file specified by the `trustedCerts` parameter. | `true` on Windows and macOS, `false` on Linux (which does not have a system truststore) |
| trustedCerts | string | The full path of the `.pem` file containing certificates trusted by a CA, for the purpose of verifying the server. If this option is not set, the driver defaults to using the trusted CA certificates `.pem` file installed by the driver. The exact file path varies according to the operating system on which the driver is installed. The path for the Windows driver differs from the path set for the macOS driver. The TLS connection fails if you do not specify a value when `useEncryption` is `true` and `disableCertificateVerification` is `false`. | N/A |
| hideSQLTablesListing | boolean | Prevents Microsoft Excel 16.95+ from crashing by hiding the list of available sources in Microsoft Excel’s Query Dialog. Set to `true` to enable. Only for Intel-based Mac computers. | `false` |

### Advanced Parameters

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| quoting | string | Specifies which type of character to use to delimit values in queries. The value can be BACK\_TICK, BRACKET, or DOUBLE\_QUOTE. | DOUBLE\_QUOTE |
| routing\_queue | string | Specifies the queue to route queries to during a session. Direct Routing is used to specify the exact queue and execution cluster to run queries on for a given ODBC session. With Direct Routing, workload-management (WLM) rules are not considered; instead, queries are routed directly to the specified queue. For more information, see [Workload Management](/current/admin/workloads/workload-management/). | N/A |
| routing\_tag | string | When this parameter is set, the specified tag is associated with all queries executed within a session. Rules can check for the presence of a tag with the function "tag()". For more information, see [Workload Management](/current/admin/workloads/workload-management/). | N/A |
| stringColumnLength | string | The maximum length of data in columns of the STRING datatype and of complex datatypes. The range is 1 to 2147483647. | 1024. |

## Logging

You can inspect and extract client-side driver logs through the macOS logging infrastructure, because every macOS installation comes with an embedded Console application that allows you to filter by log types. This feature is only available for Intel-based Mac computers, and the log activity of the ODBC driver mostly consists of ODBC API calls.

To start logging:

1. Open the Console application.
2. In the search box, select **Excel** in the **PROCESS** dropdown, and **odbc** in the **ANY** dropdown.

   ![Filter by Excel and ODBC for logs in the Console application.](/images/odbc-driver-log-excel-filter.png "Logging Filter")
3. Click **Start**.

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

[Previous

Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver)[Next

Dremio JDBC Driver (Legacy)](/current/client-applications/drivers/jdbc)

* Supported Operating Systems
* Authentication Methods
  + Username and Password
  + Personal Access Tokens Enterprise
  + OAuth Access Tokens Enterprise
* Downloading and Installing
  + Downloading and Installing on Windows
  + Downloading and Installing on Linux
  + Downloading and Installing on macOS
* Configuring
  + Configuring on Windows
  + Configuring on Linux
  + Configuring on macOS
* Connection Parameters
  + Primary Connection Parameters
  + TLS Connection Parameters
  + Advanced Parameters
* Logging
* Supported Conversions from Dremio Datatypes to ODBC Datatypes