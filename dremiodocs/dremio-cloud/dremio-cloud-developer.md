# Developer Guide | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/

On this page

You can develop applications that connect to Dremio using Arrow Flight for high-performance data access, APIs for management operations, or by integrating with development tools and frameworks.

## Build Custom Applications

Use Arrow Flight and Python SDKs to build applications that connect to Dremio:

* [Arrow Flight](/dremio-cloud/developer/arrow-flight) – High-performance data access for analytics applications
* [Arrow Flight SQL](/dremio-cloud/developer/arrow-flight-sql) – Standardized SQL database interactions with prepared statements
* [Python](/dremio-cloud/developer/python) – Build applications using Arrow Flight or REST APIs
* [Dremio MCP Server](/dremio-cloud/developer/mcp-server) – AI Agent integration for natural language interactions

## Build Pipelines and Transformations

Use your tool of choice to build pipelines, perform transformations, and work with Dremio:

* [dbt Integration](/dremio-cloud/developer/dbt) – Transform data with version control and testing
* [VS Code Extension](/dremio-cloud/developer/vs-code) – Query Dremio from Visual Studio Code

## Customize and Automate

Use APIs to power any type of customization or automation:

* [API Reference](/dremio-cloud/api/) – Web applications and administrative automation

For sample applications, connectors, and additional integrations, see [Dremio Hub](https://github.com/dremio-hub).

## Supported Data Formats

For a deep dive into open table and data formats that Dremio supports, see [Data Formats](/dremio-cloud/developer/data-formats/).

Was this page helpful?

* Build Custom Applications
* Build Pipelines and Transformations
* Customize and Automate
* Supported Data Formats

<div style="page-break-after: always;"></div>

# dbt | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/dbt

On this page

dbt enables analytics engineers to transform their data using the same practices that software engineers use to build applications.

You can use Dremio's dbt connector `dbt-dremio` to transform data that is in data sources that are connected to a Dremio project.

## Prerequisites

* Download the `dbt-dremio` package from <https://github.com/dremio/dbt-dremio>.
* Ensure that Python 3.9.x or later is installed.
* Before connecting from a dbt project to Dremio, follow these prerequisite steps:
  + Ensure that you have the ID of the Dremio project that you want to use. See [Obtain the ID of a Project](/dremio-cloud/admin/projects/#obtain-the-id-of-a-project).
  + Ensure that you have a personal access token (PAT) for authenticating to Dremio. See [Create a PAT](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).

## Install

Install this package from PyPi by running this command:

Install dbt-dremio package

```
pip install dbt-dremio
```

note

`dbt-dremio` works exclusively with dbt-core versions 1.8-1.9. Previous versions of dbt-core are outside of official support.

## Initialize a dbt Project

1. Run the command `dbt init <project_name>`.
2. Select `dremio` as the database to use.
3. Select the `dremio_cloud` option.
4. Provide a value for `cloud_host`.
5. Enter your username, PAT, and the ID of your Dremio project.
6. Select the `enterprise_catalog` option.
7. For `enterprise_catalog_namespace`, enter the name of an existing namespace within the catalog.
8. For `enterprise_catalog_folder`, enter the name of a folder which already exists within the namespace.

For descriptions of the configurations in the above steps, see Configurations.

After these steps are completed, you will now have a profile for your new dbt project. This file will typically be named `profiles.yml`.

This file can be edited to add multiple profiles, one for each `target` configuration of Dremio.
A common pattern is to have a `dev` target a dbt project is tested, and then another `prod` target where changes to the model are promoted after testing:

Example Profile

```
[project name]:  
  outputs:  
    dev:  
      cloud_host: api.dremio.cloud  
      cloud_project_id: 1ab23456-78c9-01d2-de3f-456g7h890ij1  
      enterprise_catalog_folder: sales  
      enterprise_catalog_namespace: dev  
      pat: A1BCDrE2FwgH3IJkLM4123qrsT5uV6WXyza7I8bcDEFgJ9hIj0Kl1MNOPq2Rstu==  
      threads: 1  
      type: dremio  
      use_ssl: true  
      user: name@company.com  
    prod:  
      cloud_host: api.dremio.cloud  
      cloud_project_id: 1ab23456-78c9-01d2-de3f-456g7h890ij1  
      enterprise_catalog_folder: sales  
      enterprise_catalog_namespace: prod  
      pat: A1BCDrE2FwgH3IJkLM4123qrsT5uV6WXyza7I8bcDEFgJ9hIj0Kl1MNOPq2Rstu==  
      threads: 1  
      type: dremio  
      use_ssl: true  
      user: name@company.com  
  target: dev
```

Note that the `target` value inside of the profiles.yml file can be overriden when invoking the `dbt run`.

Specify target for dbt run command

```
dbt run --target <target_name>
```

## Configurations

| Configuration | Required | Default Value | Description |
| --- | --- | --- | --- |
| `cloud_host` | Yes | `api.dremio.cloud` | US Control Plane: `api.dremio.cloud`  EU Control Plane: `api.eu.dremio.cloud` |
| `cloud_project_id` | Yes | None | The ID of the Dremio project in which to run transformations. |
| `enterprise_catalog_namespace` | Yes | None | The namespace in which to create tables, views, etc. The dbt aliases are `datalake` (for objects) and `database` (for views). |
| `enterprise_catalog_folder` | Yes | None | The path in the catalog in which to create catalog objects. The dbt aliases are `root_path` (for objects) and `schema` (for views). Nested folders in the path are separated with periods. |
| `pat` | Yes | None | The personal access token to use for authentication. See [Personal Access Tokens](/dremio-cloud/security/authentication/personal-access-token/) for instructions about obtaining a token. |
| `threads` | Yes | 1 | The number of threads the dbt project runs on. |
| `type` | Yes | `dremio` | Auto-populated when creating a Dremio project. Do not change this value. |
| `use_ssl` | Yes | `true` | The value must be `true`. |
| `user` | Yes | None | Email address used as a username in Dremio. |

## Known Limitations

[Model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts) are not supported.

Was this page helpful?

* Prerequisites
* Install
* Initialize a dbt Project
* Configurations
* Known Limitations

<div style="page-break-after: always;"></div>

# Python | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/python

On this page

You can develop client applications in Python that use that use [Arrow Flight](/dremio-cloud/developer/arrow-flight/) and connect to Dremio's Arrow Flight server endpoint. For help getting started, try out the sample application.

## Sample Python Arrow Flight Client Application

This lightweight sample Python client application connects to the Dremio Arrow Flight server endpoint. You can use token-based credentials for authentication. Any datasets in Dremio that are accessible by the provided Dremio user can be queried. You can change settings in a `.yaml` configuration file before running the client.

The Sample Python Client Application

```
"""  
  Copyright (C) 2017-2021 Dremio Corporation  
  
  Licensed under the Apache License, Version 2.0 (the "License");  
  you may not use this file except in compliance with the License.  
  You may obtain a copy of the License at  
  
      http://www.apache.org/licenses/LICENSE-2.0  
  
  Unless required by applicable law or agreed to in writing, software  
  distributed under the License is distributed on an "AS IS" BASIS,  
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
  See the License for the specific language governing permissions and  
  limitations under the License.  
"""  
from dremio.arguments.parse import get_config  
from dremio.flight.endpoint import DremioFlightEndpoint  
  
if __name__ == "__main__":  
    # Parse the config file.  
    args = get_config()  
  
    # Instantiate DremioFlightEndpoint object  
    dremio_flight_endpoint = DremioFlightEndpoint(args)  
  
    # Connect to Dremio Arrow Flight server endpoint.  
    flight_client = dremio_flight_endpoint.connect()  
  
    # Execute query  
    dataframe = dremio_flight_endpoint.execute_query(flight_client)  
  
    # Print out the data  
    print(dataframe)
```

### Steps

1. Install [Python 3](https://www.python.org/downloads/).
2. Download the [Dremio Flight endpoint .whl file](https://github.com/dremio-hub/arrow-flight-client-examples/releases).
3. Install the `.whl` file:
   Command for installing the file

   ```
   python3 -m pip install <path to .whl file>
   ```
4. Create a local folder to store the client file and config file.
5. Create a file named `example.py` in the folder that you created.
6. Copy the contents of `arrow-flight-client-examples/python/example.py` (available [here](https://github.com/dremio-hub/arrow-flight-client-examples/blob/main/python/example.py)) into `example.py`.
7. Create a file named `config.yaml` in the folder that you created.
8. Copy the contents of `arrow-flight-client-examples/python/config_template.yaml` (available [here](https://github.com/dremio-hub/arrow-flight-client-examples/blob/main/python/config_template.yaml)) into `config.yaml`.
9. Uncomment the options in `config.yaml`, as needed, appending arguments after their keys (i.e., `username: my_username`). You can either delete the options that are not being used or leave them commented.

   Example config file for connecting to Dremio

   ```
   hostname: data.dremio.cloud  
   port: 443  
   pat: my_PAT  
   tls: true  
   query: SELECT * FROM Samples."samples.dremio.com"."NYC-taxi-trips" limit 10
   ```
10. Run the Python Arrow Flight Client by navigating to the folder that you created in the previous step and running this command:
    Command for running the client

    ```
    python3 example.py [-config CONFIG_REL_PATH | --config-path CONFIG_REL_PATH]
    ```

    * `[-config CONFIG_REL_PATH | --config-path CONFIG_REL_PATH]`: Use either of these options to set the relative path to the config file. The default is "./config.yaml".

### Config File Options

Default content of the config file

```
hostname:   
port:   
username:   
password:   
token:   
query:   
tls:   
disable_certificate_verification:   
path_to_certs:   
session_properties:  
engine:
```

| Name | Type | Required? | Default | Description |
| --- | --- | --- | --- | --- |
| `hostname` | string | No | `localhost` | Must be `data.dremio.cloud`. |
| `port` | integer | No | 32010 | Dremio's Arrow Flight server port. Must be `443`. |
| `username` | string | No | N/A | Not applicable when connecting to Dremio. |
| `password` | string | No | N/A | Not applicable when connecting to Dremio. |
| `token` | string | Yes | N/A | Either a Personal Access Token or an OAuth2 Token. |
| `query` | string | Yes | N/A | The SQL query to test. |
| `tls` | boolean | No | false | Enables encryption on a connection. |
| `disable_certificate_verification` | boolean | No | false | Disables TLS server verification. |
| `path_to_certs` | string | No | System Certificates | Path to trusted certificates for encrypted connections. |
| `session_properties` | list of strings | No | N/A | Key value pairs of `session_properties`. Example:  ``` session_properties:   - schema='Samples."samples.dremio.com"' ```  For a list of the available properties, see [Manage Workloads](/dremio-cloud/developer/arrow-flight#manage-workloads). |
| `engine` | string | No | N/A | The specific engine to run against. |

Was this page helpful?

* Sample Python Arrow Flight Client Application
  + Steps
  + Config File Options

<div style="page-break-after: always;"></div>

# What You Can Do

Original URL: https://docs.dremio.com/dremio-cloud/developer/vs-code

On this page

The Dremio Visual Studio (VS) Code extension transforms VS Code into an AI-ready workspace, enabling you to discover, explore, and analyze enterprise data with natural language and SQL side by side, directly in your IDE.

# What You Can Do

The VS Code extension for Dremio allows you to:

* Connect across projects – Access one or more Dremio Cloud projects from within VS Code.
* Browse & discover with context – Explore governed objects in your catalog, complete with metadata and semantic context.
* Query with intelligence – Write and run SQL with autocomplete, formatting, and syntax highlighting—or let AI agents generate SQL for you.
* Explore and get insights using natural language – Use the built-in Microsoft Copilot integration to ask questions in plain English, moving from questions to insights faster, without leaving your development environment.

## Prerequisites

Before you begin, ensure you have:

* Access to a Dremio Cloud project.
* Personal access token (PAT) for connectivity to your project. For instructions, see [Create a PAT](/cloud/security/authentication/personal-access-token/#creating-a-pat).
* Visual Studio Code installed with access to the Extensions tab in the tool.

## Install VS Code Extension for Dremio

1. Launch VS Code and click the Extensions button on the left navigation toolbar.
2. Search for and click on the **Dremio** extension.
3. On the Dremio extension page, click **Install**.
   Once the installation is complete, you're ready to start querying Dremio from VS Code.

## Connect to Dremio from VS Code

To create a connection from VS Code:

1. From the extension for Dremio, click the + button that appears when you hover over the **Connections** heading on the left panel.
2. For **Select your Dremio deployment**, select **Dremio Cloud**.
3. From the **Select a control plane** menu, select **US Control Plane** or **European Control Plane** based on where your Dremio Cloud organization is located.
4. Click **Personal Access Token** and enter the PAT that you have previously generated and press Enter.
5. The connection to your Dremio Cloud project will appear on the left under **Connections**.
6. To browse your data, click `<your_dremio_account_email>` under your connection.

## Use the Copilot Integration

With Copilot in VS Code set to Agent mode, you can interact with your data through plain-language queries powered by Dremio’s semantic layer. For example, try asking:

* "What curated views are available for financial analysis?"
* "Summarize sales trends over the last 90 days by product category."
* "Write SQL to compare revenue growth in North America vs. Europe."

Behind the scenes, Copilot taps into Dremio’s AI Semantic Layer and autonomous optimization to ensure queries run with sub-second performance — whether executed by humans or AI agents.

Was this page helpful?

* Prerequisites
* Install VS Code Extension for Dremio
* Connect to Dremio from VS Code
* Use the Copilot Integration

<div style="page-break-after: always;"></div>

# Dremio MCP Server | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/mcp-server

On this page

The [Dremio MCP Server](https://github.com/dremio/dremio-mcp) is an open-source project that enables AI chat clients or agents to securely interact with your Dremio deployment using natural language. Connecting to the Dremio-hosted MCP Server is the fastest path to enabling external AI chat clients to work with Dremio. The Dremio-hosted MCP Server provides OAuth support, which guarantees and propagates the user identity, authentication, and authorization for all interactions with Dremio. Once connected, you can use natural language to explore and query data, perform analysis and create visualizations, create views, and analyze system performance. While you can fork the open-source Dremio MCP Server for customization or install it locally for use with a personal AI chat client account we recommend using the Dremio-hosted MCP Server available to all projects for experimentation, development and production when possible.

## Configure Connectivity

Review the documentation below from AI chat client providers to verify you meet the requirements for creating custom connectors before proceeding.

* [Claude Custom Connector Documentation](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp#h_3d1a65aded)
* [ChatGPT Custom Connector Documentation](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt#h_a454f0d0b6)

To configure connectivity to your Dremio-hosted MCP Server, you first need to set up a [Native OAUth application](/dremio-cloud/security/authentication/app-authentication/oauth-apps) and provide the redirect URLs for the AI chat client you are using.

* If you are using Claude, fill in `https://claude.ai/api/mcp/auth_callback,https://claude.com/api/mcp/auth_callback,http://localhost/callback,http://localhost` as redirect URLs for the OAuth Application
* If you are using ChatGPT, fill in `https://chatgpt.com/connector_platform_oauth_redirect,http://localhost` as the redirect URLs for the OAuth Application
* For a custom AI chat client, you will need to speak to your administrator.

Then configure the custom connector to the Dremio-hosted MCP Server by providing the client ID from the OAuth application and the MCP endpoint for your control plane.

* For Dremio instances using the US control plane, your MCP endpoint is `mcp.dremio.cloud/mcp/{project_id}`.
* For Dremio instances using the European control plane, your MCP endpoint is `mcp.eu.dremio.cloud/mcp/{project_id}`.
* If you are unsure of your endpoint, you can copy the **MCP endpoint** from the Project Overview page in Project Settings.

Was this page helpful?

* Configure Connectivity

<div style="page-break-after: always;"></div>

# Arrow Flight | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/arrow-flight

On this page

You can create client applications that use [Arrow Flight](https://arrow.apache.org/docs/format/Flight.html) to query data lakes at data-transfer speeds greater than speeds possible with ODBC and JDBC, without incurring the cost in time and CPU resources of deserializing data. As the volumes of data that are transferred increase in size, the performance benefits from the use of Apache Flight rather than ODBC or JDBC also increase.

You can run queries on datasets that are in the default project of a Dremio organization. Dremio is able to determine the organization and the default project from the authentication token that a Flight client uses. To query datasets in a non-default project, you can pass in the ID for the non-default project.

Dremio provides these endpoints for Arrow Flight connections:

* In the US control plane: `data.dremio.cloud:443`
* In the EU control plane: `data.eu.dremio.cloud:443`

All traffic within a control plane between Flight clients and Dremio go through the endpoint for that control plane. However, Dremio can scale up or down automatically to accommodate increasing and decreasing traffic on the endpoint.

Unless you pass in a different project ID, Arrow Flight clients run queries only against datasets that are in the default project or on datasources that are associated with the default project. By default, Dremio uses the oldest project in an organization as that organization's default project.

## Supported Versions of Apache Arrow

Dremio supports client applications that use Arrow Flight in Apache Arrow version 6.0.

## Supported Authentication Method

Client applications can authenticate to Dremio with personal access tokens (PATs). To create a PAT, follow the steps in the section [Creating a Token](/dremio-cloud/security/authentication/personal-access-token#create-a-pat).

## Flight Sessions

A Flight session has a duration of 120 minutes during which a Flight client interacts with Dremio. A Flight client initiates a new session by passing a `getFlightInfo()` request that does not include a Cookie header that specifies a session ID that was obtained from Dremio. All requests that pass the same session ID are considered to be in the same session.

![](/images/cloud/arrow-flight-session.png)

1. The Flight client, having obtained a PAT from Dremio, sends a `getFlightInfo()` request that includes the query to run, the URI for the endpoint, and the bearer token (PAT). A single bearer token can be used for requests until it expires.
2. If Dremio is able to authenticate the Flight client by using the bearer token, it sends a response that includes FlightInfo, a Set-Cookie header with the session ID, the bearer token, and a Set-Cookie header with the ID of the default project in the organization.

   FlightInfo responses from Dremio include the single endpoint for the control plane being used and the ticket for that endpoint. There is only one endpoint listed in FlightInfo responses.

   Session IDs are generated by Dremio.
3. The client sends a `getStream()` request that includes the ticket, a Cookie header for the session ID, the bearer token, and a Cookie header for the ID of the default project.
4. Dremio returns the query results in one flight.
5. The Flight client sends another `getFlightInfo()` request using the same session ID and bearer token. If this second request did not include the session ID that Dremio sent in response to the first request, then Dremio would send a new session ID and a new session would begin.

### Use a Non-Default Project

To run queries on datasets and data sources in non-default projects in Dremio, the `project_id` of the projects must be passed as a session option. The `project_id` is stored in the user session, and the server responds with a `Set-Cookie` header containing the session ID. The client must include this cookie in all subsequent requests.

To enable this behavior, a cookie middleware must be added to the Flight client. This middleware is responsible for managing cookies and will add the previous session ID to all subsequent requests.

After adding the middleware when initializing the client object, the `project_id` can be passed as a session option.

Here are examples of how to implement the `project_id` in Java and Go:

* Java
* Go

Pass in the ID for a non-default project in [Java](https://arrow.apache.org/docs/java/)

```
// Create a ClientCookieMiddleware  
final FlightClient.Builder flightClientBuilder = FlightClient.builder();  
final ClientCookieMiddleware.Factory cookieFactory = new ClientCookieMiddleware.Factory();  
flightClientBuilder.intercept(cookieFactory);  
  
// Add the project ID to the session options  
final SetSessionOptionsRequest setSessionOptionRequest =  
new SetSessionOptionsRequest(ImmutableMap.<String, SessionOptionValue>  
builder().put("project_id",  
SessionOptionValueFactory.makeSessionOptionValue(yourprojectid)).build());  
  
// Close your session later once query is done  
client.closeSession(new CloseSessionRequest(), bearerToken, headerCallOption);
```

Pass in the ID for a non-default project in [Go](https://github.com/apache/arrow-go)

```
// Create a ClientCookieMiddleware  
client, err := flight.NewClientWithMiddleware(  
     net.JoinHostPort(config.Host, config.Port),  
     nil,  
     []flight.ClientMiddleware{flight.NewClientCookieMiddleware(),},  
     grpc.WithTransportCredentials(creds),  
 )  
// Close the session once the query is done  
defer client.CloseSession(ctx, &flight.CloseSessionRequest{})  
// Add the project ID to the session options  
projectIdSessionOption, err := flight.NewSessionOptionValue(projectID)  
 sessionOptionsRequest := flight.SetSessionOptionsRequest{  
     SessionOptions: map[string]*flight.SessionOptionValue{  
         "project_id": &projectIdSessionOption,  
     },  
 }  
response, err = client.SetSessionOptions(ctx, &sessionOptionsRequest)
```

note

In Dremio, the term catalog is sometimes used interchangeably with `project_id`. Therefore, using catalog instead of `project_id` will also work when selecting a non-default project. We recommend using `project_id` for clarity. Throughout this documentation, we will consistently use `project_id`.

## Manage Workloads

Dremio administrators can use the Arrow Flight server endpoint to manage query workloads by adding the following connection properties to Flight clients:

| Flight Client Property | Description |
| --- | --- |
| `ENGINE` | Name of the engine to use to process all queries issued during the current session. |
| `SCHEMA` | The name of the schema (datasource or folder, including child paths, such as `mySource.folder1` and `folder1.folder2`) to use by default when a schema is not specified in a query. |

## Sample Arrow Flight Client Applications

Dremio provides sample Arrow Flight client applications in several languages at [Dremio Hub](https://github.com/dremio-hub/arrow-flight-client-examples).

Both sample clients use the hostname `local` and the port number `32010` by default. Make sure you override these defaults with the hostname `data.dremio.cloud` or `data.eu.dremio.cloud` and the port number `443`.

note

The Python sample application only supports connecting to the default project in Dremio.

Was this page helpful?

* Supported Versions of Apache Arrow
* Supported Authentication Method
* Flight Sessions
  + Use a Non-Default Project
* Manage Workloads
* Sample Arrow Flight Client Applications

<div style="page-break-after: always;"></div>

# Data Formats | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/data-formats/

Dremio supports the following data formats:

* File Formats

  + Delimited text files, such as comma-separated values
  + JSON
  + ORC
  + [Parquet](/dremio-cloud/developer/data-formats/parquet)
* Table Formats

  + [Apache Iceberg](/dremio-cloud/developer/data-formats/iceberg)
  + [Delta Lake](/dremio-cloud/developer/data-formats/delta-lake)

Was this page helpful?

<div style="page-break-after: always;"></div>

# Arrow Flight SQL | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/arrow-flight-sql

On this page

You can use Apache Arrow Flight SQL to develop client applications that interact with Dremio. Apache Arrow Flight SQL is a new API developed by the Apache Arrow community for interacting with SQL databases. For more information about Apache Arrow Flight SQL, see the documentation for the [Apache Arrow project](https://arrow.apache.org/docs/format/FlightSql.html#).

Through Flight SQL, client applications can run queries, create prepared statements, and fetch metadata about the SQL dialect supported by datasource in Dremio, available types, defined tables, and more.

The requests for running queries are

* CommandExecute
* CommandStatementUpdate

The commands on prepared statements are:

* ActionClosePreparedStatementRequest: Closes a prepared statement.
* ActionCreatePreparedStatementRequest: Creates a prepared statement.
* CommandPreparedStatementQuery: Runs a prepared statement.
* CommandPreparedStatementUpdate: Runs a prepared statement that updates data.

The metadata requests that Dremio supports are:

* CommandGetDbSchemas: Lists the schemas that are in a catalog.
* CommandGetTables: Lists that tables that are in a catalog or schema.
* CommandGetTableTypes: Lists the table types that are supported in a catalog or schema. The types are Table, View, and System Table.
* CommandGetSqlInfo: Retrieves information about the datasource and the SQL dialect that it supports.

There are two clients already implemented and available in the Apache Arrow repository on GitHub for you to make use of:

* [Client in C++](https://github.com/apache/arrow/blob/dfca6a704ad7e8e87e1c8c3d0224ba13b25786ea/cpp/src/arrow/flight/sql/client.h)
* [Client in Java](https://github.com/apache/arrow/blob/dfca6a704ad7e8e87e1c8c3d0224ba13b25786ea/java/flight/flight-sql/src/main/java/org/apache/arrow/flight/sql/FlightSqlClient.java)

note

At this time, you can only connect to the default project in Dremio.

## Use the Sample Client

You can download and try out the sample client from <https://github.com/dremio-hub/arrow-flight-sql-clients>. Extract the content of the file and then, in a terminal window, change to the `flight-sql-client-example` directory.

Before running the sample client, ensure that you have met these prerequisites:

* Add the Samples data lake to your Dremio project by clicking the ![This is the Add Source icon.](/images/icons/plus.png "This is the Add Source icon.") icon in the **Data Lakes** section of the Datasets page.
* Ensure that Java 8 or later (up to Java 15) is installed on the system on which you run the example commands.

### Command Syntax for the Sample Client

Use this syntax when sending commands to the sample client:

Sample client usage

```
Usage: java -jar flight-sql-sample-client-application.jar  -host data.dremio.cloud -port 443 ...  
  
 -command,--command <arg>                 Method to run  
 -dsv,--disableServerVerification <arg>   Disable TLS server verification.  
                                          Defaults to false.  
 -host,--hostname <arg>                   `data.dremio.cloud` for Dremio's US control plane  
                                          `data.eu.dremio.cloud` for Dremio's European control plane  
 -kstpass,--keyStorePassword <arg>        The jks keystore password.  
 -kstpath,--keyStorePath <arg>            Path to the jks keystore.  
 -pat,--personalAccessToken <arg>         Personal access token  
 -port,--flightport <arg>                 443  
 -query,--query <arg>                     The query to run  
 -schema,--schema <arg>                   The schema to use  
 -sp,--sessionProperty <arg>              Key value pairs of  
                                          SessionProperty, example: -sp  
                                          schema='Samples."samples.dremio.  
                                          com"' -sp key=value  
 -table,--table <arg>                     The table to query  
 -tls,--tls <arg>                         Enable encrypted connection.  
                                          Defaults to true.
```

### Examples

The examples demonstrate what is returned for each of these requests:

* CommandGetDbSchemas
* CommandGetTables
* CommandGetTableTypes
* CommandExecute

note

These examples use the Flight endpoint for Dremio's US control plane: `data.dremio.cloud`. To use Dremio's European control plane, use this endpoint instead: `data.eu.dremio.cloud`.

#### Flight SQL Request: CommandGetDbSchemas

This command submits a `CommandGetDbSchemas` request to list the schemas in a catalog.

Example CommandGetDbSchemas request

```
java -jar flight-sql-sample-client-application.jar -tls true -host data.dremio.cloud -port 443 --pat '<personal-access-token>' -command GetSchemas
```

Example output for CommandGetDbSchemas request

```
catalog_name	db_schema_name  
null	        @myUserName  
null	        INFORMATION_SCHEMA  
null	        Samples  
null	        sys
```

#### Flight SQL Request: CommandGetTables

This command submits a `CommandGetTables` request to list the tables that are in a catalog or schema.

Example CommandGetTables request

```
java -jar flight-sql-sample-client-application.jar -tls true -host data.dremio.cloud -port 443 --pat '<personal-access-token>' -command GetTables -schema INFORMATION_SCHEMA
```

If you have a folder in your schema, you can escape it like this:

Example CommandGetTables request with folder in schema

```
java -jar flight-sql-sample-client-application.jar -tls true -host data.dremio.cloud -port 443 --pat '<personal-access-token>' -command GetTables -schema "Samples\ (1).samples.dremio.com"
```

Example output for CommandGetTables request

```
catalog_name  db_schema_name	        table_name	table_type  
null	      INFORMATION_SCHEMA	CATALOGS	SYSTEM_TABLE  
null	      INFORMATION_SCHEMA	COLUMNS         SYSTEM_TABLE  
null	      INFORMATION_SCHEMA	SCHEMATA	SYSTEM_TABLE  
null	      INFORMATION_SCHEMA	TABLES          SYSTEM_TABLE  
null	      INFORMATION_SCHEMA	VIEWS           SYSTEM_TABLE
```

#### Flight SQL Request: CommandGetTableTypes

This command submits a `CommandTableTypes` request to list the table types supported.

Example CommandTableTypes request

```
java -jar flight-sql-sample-client-application.jar -tls true -host data.dremio.cloud -port 443 --pat '<personal-access-token>' -command GetTableTypes
```

Example output for CommandTableTypes request

```
table_type  
TABLE  
SYSTEM_TABLE  
VIEW
```

#### Flight SQL Request: CommandExecute

This command submits a `CommandExecute` request to run a single SQL statement.

Example CommandExecute request

```
java -jar flight-sql-sample-client-application.jar -tls true -host data.dremio.cloud -port 443 --pat '<personal-access-token>' -command Execute -query 'SELECT * FROM Samples."samples.<Dremio-user-name>.com"."NYC-taxi-trips" limit 10'
```

Example output for CommandExecute request

```
pickup_datetime	passenger_count	trip_distance_mi fare_amount tip_amount total_amount  
2013-05-27T19:15              1             1.26         7.5        0.0          8.0  
2013-05-31T16:40              1             0.73         5.0        1.2          7.7  
2013-05-27T19:03              2             9.23        27.5        5.0        38.33  
2013-05-31T16:24              1             2.27        12.0        0.0         13.5  
2013-05-27T19:17              1             0.71         5.0        0.0          5.5  
2013-05-27T19:11              1             2.52        10.5       3.15        14.15  
2013-05-31T16:41              5             1.01         6.0        1.1          8.6  
2013-05-31T16:37              1             1.25         8.5        0.0         10.0  
2013-05-31T16:39              1             2.04        10.0        1.5         13.0  
2013-05-27T19:02              1            11.73        32.5       8.12        41.12
```

## Code Samples

### Create a FlightSqlClient

Refer to [this code sample](https://github.com/dremio-hub/arrow-flight-client-examples/blob/main/java/src/main/java/com/adhoc/flight/client/AdhocFlightClient.java) to create a `FlightClient`. Then, wrap your `FlightClient` in a `FlightSqlClient`:

Wrap FlightClient in FlightSqlClient

```
// Wraps a FlightClient in a FlightSqlClient  
FlightSqlClient flightSqlClient = new FlightSqlClient(flightClient);  
  
// Be sure to close the FlightSqlClient after using it  
flightSqlClient.close();
```

### Retrieve a List of Database Schemas

This code issues a CommandGetSchemas metadata request:

CommandGetSchemas metadata request

```
String catalog = null; // The catalog. (may be null)  
String dbSchemaFilterPattern = null; // The schema filter pattern. (may be null)  
FlightInfo flightInfo = flightSqlClient.getSchemas(catalog, dbSchemaFilterPattern);
```

### Retrieve a List of Tables

This code issues a CommandGetTables metadata request:

CommandGetTables metadata request

```
String catalog = null;  // The catalog. (may be null)  
String dbSchemaFilterPattern = "Samples\\ (1).samples.dremio.com";  // The schema filter pattern. (may be null)  
String tableFilterPattern = null;  // The table filter pattern. (may be null)  
List<String> tableTypes = null;  // The table types to include. (may be null)  
boolean includeSchema = false;  // True to include the schema upon return, false to not include the schema.  
FlightInfo flightInfo = flightSqlClient.getTables(catalog, dbSchemaFilterPattern, tableFilterPattern, tableTypes, includeSchema);
```

### Retrieve a List of Table Types That a Database Supports

This code issues a CommandGetTableTypes metadata request:

CommandGetTableTypes metadata request

```
FlightInfo flightInfo = flightSqlClient.getTableTypes();
```

### Run a Query

This code issues a CommandExecute request:

CommandExecute request

```
FlightInfo flightInfo = flightSqlClient.execute("SELECT * FROM Samples.\"samples.myUserName.com\".\"NYC-taxi-trips\" limit 10");
```

### Consume Data Returned for a Query

Consume data returned for query

```
FlightInfo flightInfo; // Use a FlightSqlClient method to get a FlightInfo  
  
// 1. Fetch each partition sequentially (though this can be done in parallel)  
for (FlightEndpoint endpoint : flightInfo.getEndpoints()) {  
  
  // 2. Get a stream of results as Arrow vectors  
  try (FlightStream stream = flightSqlClient.getStream(endpoint.getTicket())) {  
  
    // 3. Iterate through the stream until the end  
    while (stream.next()) {  
  
      // 4. Get a chunk of results (VectorSchemaRoot) and print it to the console  
      VectorSchemaRoot vectorSchemaRoot = stream.getRoot();  
      System.out.println(vectorSchemaRoot.contentToTSVString());  
    }  
  }  
}
```

## Client Interactions with Dremio

This diagram shows an example of how an Arrow Flight SQL client initiates a Flight session and runs a query. It also shows what messages pass between the proxy at the Arrow Flight SQL endpoint, the control plane, and the execution plane.

![](/images/cloud/arrow-flight-sql-session.png)

1. The Flight client, having obtained a PAT from Dremio, calls the `execute()` method, which then sends a `getFlightInfo()` request. This request includes the query to run, the URI for the endpoint, and the bearer token (PAT). A single bearer token can be used for requests until it expires.

   A `getFlightInfo()` request initiates a new Flight session, which has a duration of 120 minutes. A Flight session is identified by its ID. Session IDs are generated by the proxy at the Arrow Flight SQL endpoint. All requests that pass the same session ID are considered to be in the same Flight session.
2. The bearer token includes the user ID and the organization ID. From those two pieces of information, the proxy at the endpoint determines the project ID, and then passes the organization ID, project ID, and user ID in the `getFlightInfo()` request that it forwards to the control plane.
3. If the control plane is able to authenticate the Flight client by using the bearer token, it sends a response that includes FlightInfo to the proxy.

   FlightInfo responses include the single endpoint for the control plane being used and the ticket for that endpoint. There is only one endpoint listed in FlightInfo responses.
4. The proxy at the endpoint adds the session ID and the project ID, and passes the response to the client.
5. The client sends a `getStream()` request that includes the ticket, a Cookie header for the session ID, the bearer token, and a Cookie header for the ID of the default project.
6. The proxy adds the organization ID and passes the `getStream()` request to the control plane.
7. The control plane devises the query plan and sends that to the execution plane.
8. The execution plane runs the query and sends the results to the control plane in one flight.
9. The control plane passes the results to the proxy.
10. The proxy passes the results to the client.

Was this page helpful?

* Use the Sample Client
  + Command Syntax for the Sample Client
  + Examples
* Code Samples
  + Create a FlightSqlClient
  + Retrieve a List of Database Schemas
  + Retrieve a List of Tables
  + Retrieve a List of Table Types That a Database Supports
  + Run a Query
  + Consume Data Returned for a Query
* Client Interactions with Dremio

<div style="page-break-after: always;"></div>

# Apache Iceberg | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/data-formats/iceberg

On this page

[Apache Iceberg](https://iceberg.apache.org/docs/latest/) enables Dremio to provide powerful, SQL database-like functionality on data lakes using industry-standard SQL commands. Dremio currently supports [Iceberg v2](https://iceberg.apache.org/spec/#version-2) tables, offering a solid foundation for building and managing data lakehouse tables. Certain features, such as Iceberg native branching and tagging, and the UUID data type, are not yet supported.

For a deeper dive into Apache Iceberg, see:

* [Apache Iceberg: An Architectural Look Under the Covers](https://www.dremio.com/apache-iceberg-an-architectural-look-under-the-covers/)
* [What is Apache Iceberg?](https://www.dremio.com/data-lake/apache-iceberg/)

### Benefits of Iceberg Tables

Iceberg tables offer the following benefits over other formats traditionally used in the data lake, including:

* **[Schema evolution](https://iceberg.apache.org/docs/latest/evolution/):** Supports add, drop, update, or rename column commands with no side effects or inconsistency.
* **[Partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution):** Facilitates the modification of partition layouts in a table, such as data volume or query pattern changes without needing to rewrite the entire table.
* **Transactional consistency:** Helps users avoid partial or uncommitted changes by tracking atomic transactions with atomicity, consistency, isolation, and durability (ACID) properties.
* **Increased performance:** Ensures data files are intelligently filtered for accelerated processing via advanced partition pruning and column-level statistics.
* **Time travel:** Allows users to query any previous versions of the table to examine and compare data or reproduce results using previous queries.
* **[Automatic optimization](/dremio-cloud/manage-govern/optimization):** Optimize query performance to maximize the speed and efficiency with which data is retrieved.
* **Version rollback:** Corrects any discovered problems quickly by resetting tables to a known good state.

## Clustering

Clustered Iceberg tables in Dremio makes use of Z-Ordering to provide a more intuitive data layout with comparable or better performance characteristics to Iceberg partitioning.

Iceberg clustering sorts individual records in data files based on the clustered columns provided in the [`CREATE TABLE`](/dremio-cloud/sql/commands/create-table) or [`ALTER TABLE`](/dremio-cloud/sql/commands/alter-table/) statement. The data file level clustering of data allows Parquet metadata to be used in query planning and execution to reduce the amount of data scanned as part of the query. In addition, clustering eliminates common problems with partitioned data, such as over-partitioned tables and partition skew.

Clustering provides a general-purpose file layout that enables both efficient reads and writes. However, you may not see immediate benefits from clustering if the tables are too small.

A common pattern is to choose clustered columns that are either primary keys of the table or commonly used for query filters. These column choices will effectively filter the working dataset, thereby improving query times. Clustered columns are ordered in precedence of filtering or cardinality with the most commonly queried columns of highest cardinality first.

#### Supported Data Types for Clustered Columns

Dremio Iceberg clustering supports clustered columns of the following data types:

* `DECIMAL`
* `INT`
* `BIGINT`
* `FLOAT`
* `DOUBLE`
* `VARCHAR`
* `VARBINARY`
* `DATE`
* `TIME`
* `TIMESTAMP`

Automated table maintenance eliminates the need to run optimizations for clustered Iceberg tables manually, although if using manual optimization, its behavior differs based on whether or not tables are clustered.

For clustered tables, [`OPTIMIZE TABLE`](/dremio-cloud/sql/commands/optimize-table) incrementally reorders data to achieve the optimal data layout and manages file sizes. This mechanism may take longer to run on newly loaded or unsorted tables. Additionally, you may be required to run multiple `OPTIMIZE TABLE` SQL commands to converge on an optimal file layout.

For unclustered tables, `OPTIMIZE TABLE` combines small files or splits large files to achieve an optimal file size, reducing metadata overhead and runtime file open costs.

#### CTAS Behavior and Clustering

When running a [`CREATE TABLE AS`](/dremio-cloud/sql/commands/create-table-as) statement with clustering, the data is written in an unordered way. For the best performance, you should run an `OPTIMIZE TABLE` SQL command after creating a table using a [`CREATE TABLE AS`](/dremio-cloud/sql/commands/create-table-as) statement.

## Iceberg Table Management

Learn how to manage Iceberg tables in Dremio with supported Iceberg features such as expiring snapshots and optimizing tables.

### Vacuum

Each write to an Iceberg table creates a snapshot of that table, which is a timestamped version of the table. As snapshots accumulate, data files that are no longer referenced in recent snapshots take up more and more storage. Additionally, the more snapshots a table has, the larger its metadata becomes. You can expire older snapshots to delete the data files that are unique to them and to remove them from table metadata. It is recommended that you expire snapshots regularly. For the SQL command to expire snapshots, see [`VACUUM TABLE`](/dremio-cloud/sql/commands/vacuum-table/).

Sometimes failed SQL commands may leave orphan data files in the table location that are no longer referenced by any active snapshot of the table. You can remove orphan files in the table location by running `remove_orphan_files`. See [`VACUUM TABLE`](/dremio-cloud/sql/commands/vacuum-table/) for details.

### Optimization

Dremio provides [automatic optimization](/dremio-cloud/manage-govern/optimization/), which automatically maintains Iceberg tables in the Open Catalog using a dedicated engine configured by Dremio. However, for immediate optimization, you can use the [`OPTIMIZE TABLE`](/dremio-cloud/sql/commands/optimize-table) SQL command and route jobs to specific engines in your project by creating a routing rule with the `query_label()` condition and the `OPTIMIZATION` label. For more information, see [Workload Management](/dremio-cloud/admin/engines/workload-management).

When optimizing tables manually, you can use:

* [`FOR PARTITIONS`](/dremio-cloud/sql/commands/optimize-table/) to optimize selected partitions.
* [`MIN_INPUT_FILES`](/dremio-cloud/sql/commands/optimize-table/) to consider the minimum number of qualified files needed for compaction. Delete files count towards determining whether the minimum threshold is reached.

## Iceberg Catalogs in Dremio

The Apache Iceberg table format uses an Iceberg catalog service to track snapshots and ensure transactional consistency between tools. For more information about how Iceberg catalogs and tables work together, see [Iceberg Catalog](https://www.dremio.com/resources/guides/apache-iceberg-an-architectural-look-under-the-covers/#toc_item_Iceberg%20catalog).

note

Currently, Dremio does not support the Amazon DynamoDB nor JDBC catalogs. For additional information on limitations of Apache Iceberg as implemented in Dremio, see Limitations.

The catalog is the source of truth for the current metadata pointer for a table. You can use [Dremio's Open Catalog](/dremio-cloud/developer/data-formats/iceberg/#iceberg-catalogs-in-dremio) as a catalog for all your tables. You can also add external Iceberg catalogs as a source in Dremio, which allows you to work with Iceberg tables that are not cataloged in Dremio's Open Catalog.The list of Iceberg catalogs that can be added as a source can be found here:

* AWS Glue Data Catalog
* Iceberg REST Catalog
* Snowflake Open Catalog
* Unity Catalog

Once a table is created with a specific catalog, you must continue using that same catalog to access the table. For example, if you create a table using AWS Glue as the catalog, you cannot later access that table by adding its S3 location as a source in Dremio. You must add the AWS Glue Data Catalog as a source and access the table through it.

## Rollbacks

When you modify an Iceberg table using data definition language (DDL) or data manipulation language (DML), each change creates a new [snapshot](https://iceberg.apache.org/terms/#snapshot) in the table's metadata. The Iceberg [catalog](/dremio-cloud/developer/data-formats/iceberg/#iceberg-catalogs-in-dremio) tracks the current snapshot through a root pointer.
You can use the [`ROLLBACK TABLE`](/dremio-cloud/sql/commands/rollback-table) SQL command to roll back a table by redirecting this pointer to an earlier snapshot—useful for undoing recent data errors. Rollbacks can target a specific timestamp or snapshot ID.
When you perform a rollback, Dremio creates a new snapshot identical to the selected one. For example, if a table has snapshots (1) `first_snapshot`, (2) `second_snapshot`, and (3) `third_snapshot`, rolling back to `first_snapshot` restores the table to that state while preserving all snapshots for time travel queries.

## SQL Command Compatibility

Dremio supports running most combinations of concurrent SQL commands on Iceberg tables. To take a few examples, two [`INSERT`](/dremio-cloud/sql/commands/insert) commands can run concurrently on the same table, as can two [`SELECT`](/dremio-cloud/sql/commands/SELECT) commands, or an [`UPDATE`](/dremio-cloud/sql/commands/update) and an [`ALTER`](/dremio-cloud/sql/commands/alter-table) command.

However, Apache Iceberg’s Serializable Isolation level with non-locking table semantics can result in scenarios in which write collisions occur. In these circumstances, the SQL command that finishes second fails with an error. Such failures occur only for a subset of combinations of two SQL commands running concurrently on a single Iceberg table.

This table shows which types of SQL commands can and cannot run concurrently with other types on a single Iceberg table:

* Y: Running these two types of commands concurrently is supported.
* N: Running these two types of commands concurrently is not supported. The second command to complete fails with an error.
* D: Running two [`OPTIMIZE`](/cloud/reference/sql/commands/optimize-table) commands concurrently is supported if they run against different table partitions.

![SQL commands that cause concurrency conflicts](/images/concurrency-table.png "SQL commands that cause concurrency conflicts")

## Table Properties

The following Apache Iceberg table properties are supported in Dremio. You can use these properties to configure aspects of Apache Iceberg tables:

| Property | Description | Default |
| --- | --- | --- |
| commit.manifest.target-size-bytes | The target size when merging manifest files. | `8 MB` |
| commit.status-check.num-retries | The number of times to check whether a commit succeeded after a connection is lost before failing due to an unknown commit state. | `3` |
| compatibility.snapshot-id-inheritance.enabled | Enables committing snapshots without explicit snapshot IDs. | `false` (always `true` if the format version is > 1) |
| format-version | The table’s format version defined in the Spec. Options: `1` or `2` | `2` |
| history.expire.max-snapshot-age-ms | The maximum age (in milliseconds) of snapshots to keep as expiring snapshots. | `432000000` (5 days) |
| history.expire.min-snapshots-to-keep | The default minimum number of snapshots to keep as expiring snapshots. | `1` |
| write.delete.mode | The table’s method for handling row-level deletes. See [Row-Level Changes on the Lakehouse: Copy-On-Write vs. Merge-On-Read in Apache Iceberg](https://www.dremio.com/blog/row-level-changes-on-the-lakehouse-copy-on-write-vs-merge-on-read-in-apache-iceberg/) for more information on which mode is best for your table’s DML operations. Options: `copy-on-write` or `merge-on-read` | `copy-on-write` |
| write.merge.mode | The table’s method for handling row-level merges. See [Row-Level Changes on the Lakehouse: Copy-On-Write vs. Merge-On-Read in Apache Iceberg](https://www.dremio.com/blog/row-level-changes-on-the-lakehouse-copy-on-write-vs-merge-on-read-in-apache-iceberg/) for more information on which mode is best for your table’s DML operations. Options: `copy-on-write` or `merge-on-read` | `copy-on-write` |
| write.metadata.compression-codec | The Metadata compression codec. Options: `none` or `gzip` | `none` |
| write.metadata.delete-after-commit.enabled | Controls whether to delete the oldest tracked version metadata files after commit. | `false` |
| write.metadata.metrics.column.col1 | Metrics mode for column `col1` to allow per-column tuning. Options: `none`, `counts`, `truncate(length)`, or `full` | (not set) |
| write.metadata.metrics.default | Default metrics mode for all columns in the table. Options: `none`, `counts`, `truncate(length)`, or `full` | `truncate(16)` |
| write.metadata.metrics.max-inferred-column-defaults | Defines the maximum number of top-level columns for which metrics are collected. The number of stored metrics can be higher than this limit for a table with nested fields. | `100` |
| write.metadata.previous-versions-max | The maximum number of previous version metadata files to keep before deleting after commit. | `100` |
| write.parquet.compression-codec | The Parquet compression codec. Options: `zstd`, `gzip`, `snappy`, or `uncompressed` | `zstd` |
| write.parquet.compression-level | The Parquet compression level. Supported for `gzip` and `zstd`. | `null` |
| write.parquet.dict-size-bytes | The Parquet dictionary page size (in bytes). | `2097152` (2 MB) |
| write.parquet.page-row-limit | The Parquet page row limit. | `20000` |
| write.parquet.page-size-bytes | The Parquet page size (in bytes). | `1048576` (1 MB) |
| write.parquet.row-group-size-bytes | Parquet row group size. Dremio uses this property as a target file size since it writes one row-group per Parquet file. Ignores the `store.parquet.block-size` and `dremio.iceberg.optimize.target_file_size_mb` support keys. | `134217728` (128 MB) |
| write.summary.partition-limit | Includes partition-level summary stats in snapshot summaries if the changed partition count is less than this limit. | `0` |
| write.update.mode | The table’s method for handling row-level updates. See [Row-Level Changes on the Lakehouse: Copy-On-Write vs. Merge-On-Read in Apache Iceberg](https://www.dremio.com/blog/row-level-changes-on-the-lakehouse-copy-on-write-vs-merge-on-read-in-apache-iceberg/) for more information on which mode is best for your table’s DML operations. Options: `copy-on-write` or `merge-on-read` | `copy-on-write` |

You can configure these properties when you [create](/dremio-cloud/sql/commands/create-table) or [alter](/dremio-cloud/sql/commands/alter-table) Iceberg tables.

Dremio uses the Iceberg default value for table properties that are not set. See Iceberg's documentation for the full list of [table properties](https://iceberg.apache.org/docs/latest/configuration/#table-properties). To view the properties that are set for a table, use the SQL command [`SHOW TBLPROPERTIES`](/dremio-cloud/sql/commands/show-table-properties).

In cases where Dremio has a support key for a feature covered by a table property, Dremio uses the table property instead of the support key.

## Limitations

The following are limitations with Apache Iceberg as implemented in Dremio:

* Only Parquet file formats are currently supported. Other formats (such as ORC and Avro) are not supported at this time.
* Amazon DynamoDB and JDBC catalogs are currently not supported.
* Unable to use DynamoDB as a lock manager with the Hadoop catalog on Amazon S3.
* Dremio caches query plans for recently executed statements to improve query performance. However, running a rollback query using a snapshot ID invalidates all cached query plans that reference the affected table.
* If a table is running DML operations when a rollback query using a snapshot ID executes, the DML operations can fail to complete because the current snapshot ID has changed to a new value due to the rollback query. However, `SELECT` queries that are in the midst of executing can be completed.
* Clustering keys must be columns in the table. Transformations are not supported.
* You can run only one optimize query at a time on the selected Iceberg table partition.
* The optimize functionality does not support sort ordering.

## Related Topics

* [Automatic Optimization](/dremio-cloud/manage-govern/optimization/) – Learn how Dremio optimizes Iceberg tables automatically.
* [Load Data Into Tables](/dremio-cloud/bring-data/load/) - Load data from CSV, JSON, or Parquet files into existing Iceberg tables.
* [SQL Commands](/dremio-cloud/sql/commands/) – See the syntax of the SQL commands that Dremio supports for Iceberg tables.

Was this page helpful?

* Benefits of Iceberg Tables
* Clustering
* Iceberg Table Management
  + Vacuum
  + Optimization
* Iceberg Catalogs in Dremio
* Rollbacks
* SQL Command Compatibility
* Table Properties
* Limitations
* Related Topics

<div style="page-break-after: always;"></div>

# Parquet | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/data-formats/parquet

On this page

This topic provides general information and recommendations for Parquet files.

## Read Parquet Files

Dremio's vectorized Parquet file reader improves parallelism on columnar data, reduces latencies, and enables more efficient resource and memory usage.

Dremio supports off-heap memory buffers for reading Parquet files.

Dremio supports file compression with `snappy`, `gzip`, and `zstd` for reading Parquet files.

## Parquet Limitations

Take into consideration the following limitations when generating and configuring Parquet files. Failure to adhere to these restrictions may cause errors to trigger when using Parquet files with Dremio.

* **Maximum nested levels are restricted to 16.** Multiple structs may be defined up to a total nesting level of 16. Exceeding this results in a failed query.
* **Maximum allowable elements in an array are restricted to 128.** The maximum allowable number of elements in an array may not exceed this quantity. Additional elements beyond the allowed 128 results in a query failure.
* **Maximum footer size is restricted to 16MB.** The footer consists of metadata. This includes information about the version of the format, the schema, extra key-value pairs, and metadata for columns in the file. When the footer exceeds this size, a query failure occurs.

## Recommended Configuration

When using other tools to generate Parquet files for consumption in Dremio, we recommend the following configuration:

| Type | Implementation |
| --- | --- |
| Row Groups | Implement your row groups using the following: A single row group per file, and a target of 1MB-25MB column stripes for most datasets (ideally). By default, Dremio uses 256 MB row groups for the Parquet files that it generates. |
| Pages | Implement your pages using the following: Snappy compression, and a target of ~100K page size. Use a recent Parquet library to avoid bad statistics issues. |
| Statistics | Use a recent Parquet library to avoid bad statistics issues. |

Was this page helpful?

* Read Parquet Files
* Parquet Limitations
* Recommended Configuration

<div style="page-break-after: always;"></div>

# Delta Lake | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/developer/data-formats/delta-lake

On this page

[Delta Lake](https://docs.delta.io/latest/index.html) is an open-source table format that provides transactional consistency and increased scale for datasets by creating a consistent definition of datasets and including schema evolution changes and data mutations. With Delta Lake, updates to datasets are viewed in a consistent manner across all applications consuming the datasets, and users are kept from seeing inconsistent views of data during transformations. Consistent and reliable views of datasets in a data lake are maintained even as the datasets are updated and modified over time.

Data consistency for a dataset is enabled through the creation of a series of manifest files which define the schema and data for a given point in time, as well as a transaction log that defines an ordered record of every transaction on the dataset. By reading the transaction log and manifest files, applications are guaranteed to see a consistent view of data at any point in time, and users can ensure intermediate changes are invisible until a write operation is complete.

Delta Lake provides the following benefits:

* Large-scale support: Efficient metadata handling enables applications to readily process petabyte-sized datasets with millions of files
* Schema consistency: All applications processing a dataset operate on a consistent and shared definition of the dataset metadata such as columns, data types, partitions.

## Supported Data Sources

The Delta Lake table format is supported with the following sources in the Parquet file format:

* [Amazon S3](/dremio-cloud/bring-data/connect/object-storage/amazon-s3)
* [AWS Glue Data Catalog](/dremio-cloud/bring-data/connect/catalogs/aws-glue-data-catalog)

## Analyze Delta Lake Datasets

Dremio supports analyzing Delta Lake datasets on the sources listed above through a native and high-performance reader. It automatically identifies which datasets are saved in the Delta Lake format, and imports table information from the Delta Lake manifest files. Dataset promotion is seamless and operates the same as any other data format in Dremio, where users can promote file system directories containing a Delta Lake dataset to a table manually or automatically by querying the directory. When using Delta Lake format, Dremio supports datasets of any size including petabyte-sized datasets with billions of files.

Dremio reads Delta Lake tables created or updated by another engine, such as Spark and others, with transactional consistency. Dremio automatically identifies tables that are in the Delta Lake format and selects the appropriate format for the user.

### Refresh Metadata

Metadata refresh is required to query the latest version of a Delta Lake table. You can wait for an automatic refresh of metadata or manually refresh it.

#### Example of Querying a Delta Lake Table

Perform the following steps to query a Delta Lake table:

1. In Dremio, open the **Datasets** page.
2. Go to the data source that contains the Delta Lake table.
3. If the data source is not an AWS Glu Data Catalog, follow these steps:
   1. Hover over the row for the table and click ![The Format Folder icon](/images/cloud/format-data.png "The Format Folder icon") to the right. Dremio automatically identifies tables that are in the Delta Lake format and selects the appropriate format.
   2. Click **Save**.
4. If the data source is an AWS Glue Data Catalog, hover over the row for the table and click ![The Go To Table icon](/images/cloud/go-to-table.png "The Go To Table icon") to the right.
5. Run a query on the Delta Lake table to see the results.
6. Update the table in the data source.
7. Go back to the **Datasets** UI and wait for the table metadata to refresh or manually refresh it using the syntax below.

Syntax to manually refresh table metadata

```
ALTER TABLE `<path_of_the_dataset>`   
REFRESH METADATA
```

The following statement shows refreshing metadata of a Delta Lake table.

Example command to manually refresh table metadata

```
ALTER TABLE s3."data.dremio.com".data.deltalake."tpcds10_delta"."call_center"  
REFRESH METADATA
```

8. Run the previous query on the Delta Lake table to retrieve the results from the updated Delta Lake table.

## Limitations

* Creating Delta Lake tables is not supported.
* DML operations are not supported.
* Incremental Reflections are not supported.
* Metadata refresh is required to query the latest version of a Delta Lake table.
* Time travel or data versioning is not supported.
* Only Delta Lake tables with minReaderVersion 1 or 2 can be read. Column Mapping is supported with minReaderVersion 2.

Was this page helpful?

* Supported Data Sources
* Analyze Delta Lake Datasets
  + Refresh Metadata
* Limitations

<div style="page-break-after: always;"></div>

