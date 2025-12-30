# Dremio Software - Reference



---

# Source: https://docs.dremio.com/current/reference/

Version: current [26.x]

# Reference

This section contains details about using Dremio's REST API, SQL commands and functions, and security advisories.

* [**Admin CLI**](/current/reference/admin-cli/) - The reference documentation on the `dremio-admin` CLI commands.
* [**API Reference**](/current/reference/api/) - The reference documentation on the Dremio REST APIs.
* [**SQL Reference**](/current/reference/sql/) - The reference documentation on Dremio SQL to manage your data.
* [**Security Bulletins**](/current/reference/bulletins/) - Security bulletins that disclose vulnerabilities found in Dremio's supported products.

Was this page helpful?

[Previous

API Reference](/current/reference/api/)[Next

Admin CLI](/current/reference/admin-cli/)

---

# Source: https://docs.dremio.com/current/reference/admin-cli/

Version: current [26.x]

On this page

# Admin CLI

This topic summarizes the `dremio-admin` CLI commands.

## Syntax

Syntax for dremio-admin commands

```
dremio-admin [--config <conf-dir>] (encrypt|set-password|upgrade|recommend-reflections|delete-user-homespace|optimize-acls|export-profiles|remove-duplicate-users|clean|remove-duplicate-roles|reset-catalog-search|backup|delete-all-users|restore|repair-acls|nessie-maintenance) [args...]
```

## Options

| Option | Description |
| --- | --- |
| `--help, -h` | Displays usage information for the CLI commands. |
| `--config <conf-dir>` | Used when the configuration file location is different than the `/opt/dremio/conf` default directory.  For example, if `dremio.conf`, `dremio-env`, `logbook.xml`, and `logbook-admin.xml` are located in `/etc/dremio`, you will have to run all of the `dremio-admin` commands as `./dremio-admin --config /etc/dremio <command> <arguments>`. |

## Commands

| Command | Description |
| --- | --- |
| `backup` | Backs up Dremio metadata and user-uploaded files. |
| `clean` | Cleans Dremio metadata. |
| `delete-all-users` | Deletes all internal Dremio users. |
| `delete-user-homespace` | Deletes the user's home space. |
| `encrypt` | [Encrypt](/current/reference/admin-cli/encryption/) a user-supplied string. |
| `export-pats` | Exports personal access tokens (PATs). |
| `export-profiles` | Exports profiles of jobs from Dremio. |
| `import-pats` | Imports personal access tokens (PATs). |
| `nessie-maintenance` | Runs embedded Nessie repository maintenance tasks. |
| `optimize-acls` | Optimizes access control lists of sources, spaces, and datasets. |
| `recommend-reflections` | Recommend Reflections. |
| `remove-duplicate-roles` | Removes duplicate roles from Dremio. |
| `remove-duplicate-users` | Removes duplicate users from Dremio. |
| `reset-catalog-search` | Resets index to recover catalog search. |
| `repair-acls` | Repairs access control lists of sources, spaces, and datasets. |
| `restore` | Restores Dremio metadata and user-uploaded files. |
| `set-password` | Sets passwords for Dremio users (non-LDAP). |
| `upgrade` | Upgrades the KV store version. There are no options available for this command. |

## Log Directory

The default value for `DREMIO_ADMIN_LOG_DIR` is null (not set). When this parameter is *not* set, log files are *not* created.

To set the log directory, provide the log directory path by running the following:

Set log directory

```
export DREMIO_ADMIN_LOG_DIR=<path>
```

note

The export option must be set and access must be available for the user running the `dremio-admin` command.

## Log Verbosity

Log verbosity is used in conjunction with `DREMIO_ADMIN_LOG_DIR`. Otherwise, all the output is printed to `stdout`; there is no control on setting verbosity for `stdout`.

Verbosity options include:

* TRACE
* DEBUG
* INFO (default)
* WARN
* ERROR

To set the log verbosity (default: INFO), provide the verbose level by running the following:

Set log verbosity

```
export DREMIO_ADMIN_LOG_VERBOSITY=<value>
```

## For More Information

* [Backup](/current/reference/admin-cli/backup/)
* [Clean Metadata](/current/reference/admin-cli/metadata-cleanup/)
* [Encrypt Credentials](/current/reference/admin-cli/encryption/)
* [Export and Import Personal Access Tokens (PATs)](/current/reference/admin-cli/export-import-pat/)
* [Export Profiles](/current/reference/admin-cli/export-profiles/)
* [Perform Nessie Maintenance](/current/reference/admin-cli/nessie-maintenance/)
* [Remove Duplicate Roles](/current/reference/admin-cli/remove-roles/)
* [Repair ACLs](/current/reference/admin-cli/repair-acls/)
* [Restore](/current/reference/admin-cli/restore/)
* [Reset Password](/current/reference/admin-cli/reset-password/)
* [Upgrade KV Store](/current/reference/admin-cli/upgrade-KVstore/)

Was this page helpful?

[Previous

Dremio on Kubernetes](/current/admin/admin-dremio-kubernetes/)[Next

Back up Dremio](/current/reference/admin-cli/backup)

* Syntax
* Options
* Commands
* Log Directory
* Log Verbosity
* For More Information

---

# Source: https://docs.dremio.com/current/reference/api/

Version: current [26.x]

On this page

# API Reference

The Dremio REST API is organized by resource types such as `sources` and is designed around RESTful principles.

* `GET` is used to retrieve existing resources
* `POST` creates new resources
* `PUT` updates resources
* `DELETE` removes resources

## Base URL

All API URLs referenced in this documentation have the following base URL unless otherwise specified:

Base URL

```
{hostname}/api/v3
```

Versions prior to `v3` are considered internal and are subject to change without notice.

In this documentation, curly braces (`{}`) are used to indicate sections of URLs where you have to supply a value. For example:

User-supplied values in URLs

```
/api/v3/source/{id}
```

## Authentication

Each REST request requires an authorization header with a Dremio access token to authenticate the requester unless otherwise indicated. Dremio accepts three types of access tokens for authenticating REST requests.

* **OAuth access tokens** are created in Dremio using the Dremio REST API.
* **Personal access tokens** are created in the Dremio console or with REST.
* **Authentication tokens** are generated from a username and password using the Dremio v2 API.

All Dremio access tokens are Bearer tokens and can be used in the REST authorization header of each REST request.

Example Dremio REST request

```
curl -X GET 'https://{hostname}/api/v3/{path_to_endpoint}' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

### OAuth Access Tokens Enterprise

Users can create OAuth access tokens by exchanging a local or LDAP username and password, a PAT, or an external JWT using the `/oauth/token` REST API. Dremio provides [sample code](/current/reference/api/oauth-token) for each of these cases.

Dremio recommends OAuth access tokens to improve system security:

* OAuth access tokens are typically short-lived, reducing the window of opportunity for attackers if a token is compromised.
* Users must manually revoke compromised or suspected PATs, often leading to forgotten, unused tokens.

### Personal Access Tokens Enterprise

Any user can create personal access tokens (PATs) [in the Dremio console](/current/security/authentication/personal-access-tokens/#creating-a-pat) or [using REST](/current/reference/api/personal-access-token#creating-a-pat). Users can configure the lifetime of each personal access token, from 1 day to a maximum defined by the `auth.personal-access-token.max_lifetime_days` [support setting](/current/admin/support-settings#support-keys).

### Dremio Authentication Tokens

Users can generate authentication tokens from their Dremio username and password. Authentication tokens have a nonconfigurable lifetime of 30 hours.

caution

Generating an authentication token requires API v2. API versions prior to v3 are considered internal and are subject to change without notice.

To generate an authentication token:

* Send an API request to the login URL with your Dremio username and password in the request body.

### Example

Request

```
curl -X POST 'http://{hostname}/apiv2/login' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
"userName": "dremio",  
"password": "dremio123"  
}'
```

Response

```
{  
  "token": "4ksrt534vk7fkq64xh55g7776b",  
  "userName": "dremio",  
  "firstName": "Dre",  
  "lastName": "Mio",  
  "expires": 1686578200000,  
  "email": "dremio@dremio.test",  
  "userId": "5a679dd5-52d7-402a-871d-7fbee3fe8007",  
  "admin": true,  
  "clusterId": "7468ce46-58af-4dce-a42f-4c51048968f5",  
  "clusterCreatedAt": 1681311939728,  
  "version": "24.0.0-main-202305040803350903-2d5579e3",  
  "permissions": {  
    "canUploadProfiles": true,  
    "canDownloadProfiles": true,  
    "canEmailForSupport": true,  
    "canChatForSupport": false,  
    "canViewAllJobs": true,  
    "canCreateUser": true,  
    "canCreateRole": true,  
    "canCreateSource": true,  
    "canUploadFile": true,  
    "canManageNodeActivity": true,  
    "canManageEngines": true,  
    "canManageQueues": true,  
    "canManageEngineRouting": true,  
    "canManageSupportSettings": true  
  },  
  "userCreatedAt": 1681311939789  
}
```

note

If your password includes single or double quotes, you may need to escape the quotes in your authentication token request. The required escapes vary depending on how you send the request. For example, if you use cURL and the password is `example'6852"`, the password value should be `example'\''6852\"` in the authentication token request.

* Use the `token` attribute of the JSON return object as a Bearer token, or append the prefix `_dremio` to compose a self-contained token as `_dremio<tokenstring>`.

Example: Request Using A Self-Contained Authorization Token 

```
curl -X GET 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: _dremio4ksrt534vk7fkq64xh55g7776b' \  
--header 'Content-Type: application/json'
```

## Errors

Error messages will be sent back in the response body using the following format:

Error Messages Format

```
{  
  "errorMessage": "brief error message",  
  "moreInfo": "detailed error message"  
}
```

## Query Parameters

Dremio supports query parameters for many API endpoints. The documentation for each API lists the supported query parameters for specific endpoints, along with any default and maximum values for the query parameters for that endpoint.

### pageToken Query Parameter

Use the `pageToken` query parameter to split large sets of results into multiple pages.

Endpoints may support the `pageToken` query parameter based on either a [built-in maximum](/current/reference/api/#built-in-maximum) number of results per page or a [user-specified maximum](/current/reference/api/#user-specified-maximum) that is established with a separate query parameter. The documentation for each API lists the built-in maximum or the query parameter to use to specify a maximum, as applicable.

note

Do not change any other query parameters included in the request URL when you use `pageToken`.

#### Built-in Maximum

If the endpoint has a built-in maximum number of results per page, responses automatically include a page token attribute when the response contains more results than the built-in maximum. Use the value for this token in the request URL as the `pageToken` value to retrieve the next page of results.

As an example, the [Reflection summary](/current/reference/api/reflections/reflection-summary/#retrieving-a-reflection-summary) endpoint supports the `pageToken` parameter. If the Reflection summary contains more than 50 results, the response will include the `nextPageToken` attribute. To retrieve the next 50 results, add `?pageToken={nextPageToken_value}` to the request URL:

Example Request with pageToken Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?pageToken=BhQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

For subsequent requests, replace the `pageToken` value in the request URL with the token value from the previous response. If the response does not include a token attribute and value, you have retrieved the last page of available results.

#### User-Specified Maximum

For endpoints that require users to specify a maximum number of results per page with a separate query parameter, responses only include a page token attribute if your initial request URL includes the separate query parameter and the response contains more results than the maximum you specify. Add the value for this token to the request URL as the `pageToken` value, keeping the separate query parameter as well, to retrieve the next page of results.

Catalog API endpoints for retrieving non-filesystem [sources](/current/reference/api/catalog/source/#retrieving-a-source-by-id), [spaces](/current/reference/api/catalog/container-space#retrieving-a-space-by-id), and [folders](/current/reference/api/catalog/container-folder#retrieving-a-folder-by-id) by ID or path support the [`maxChildren` query parameter](/current/reference/api/#maxchildren-query-parameter) for specifying the maximum number of child objects to include in each response. If the response contains more than the specified number of child objects, the response includes the `nextPageToken` attribute. To retrieve the next page of results, add `?pageToken={nextPageToken_value}` to the request URL. This example shows a request URL that uses the `nextPageToken` query parameter with the `maxChildren` query parameter set to 25:

Example Request with maxChildren and pageToken Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/catalog/2b1be882-7012-4a99-8d6c-82e32e4562e4?maxChildren=25&pageToken=BhQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

For subsequent requests, replace the `pageToken` value in the request URL with the token value from the previous response. If the response does not include a token attribute and value, you have retrieved the last page of available results.

### maxResults Query Parameter

Use the `maxResults` query parameter to specify the maximum number of results to retrieve in each request.

For example, if you want to retrieve no more than 25 results for an endpoint that supports the `maxResults` query parameter, append `?maxResults=25` to the request URL:

Example Request with maxResults Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?maxResults=25' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

### filter Query Parameter

Use the `filter` query parameter to filter responses so that they include only results with the specified attributes and values. The value for the `filter` query parameter is a URL-encoded JSON string that represents a JSON object that specifies the desired attributes and values.

As an example, the [Reflection summary](/current/reference/api/reflections/reflection-summary/#retrieving-a-reflection-summary) endpoint supports the `filter` query parameter for certain specific attributes. To retrieve only the raw Reflections that are refreshed manually or by schedule, are enabled, and apply to datasets with `samples.dremio.com` in their paths, the `filter` JSON object would look like this:

Example JSON Object for Filter

```
{  
  "reflectionType": ["RAW"],  
  "refreshStatus": ["MANUAL","SCHEDULED"],  
  "enabledFlag": true,  
  "reflectionNameOrDatasetPath": "samples.dremio.com"  
}
```

To use the JSON object as the `filter` value, convert it to URL-encoded JSON and add it to the request URL:

Example Request with filter Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?filter=%7B%0A%20%20%22reflectionType%22%3A%20%5B%22RAW%22%5D%2C%0A%20%20%22refreshStatus%22%3A%20%5B%22MANUAL%22%2C%22SCHEDULED%22%5D%2C%0A%20%20%22enabledFlag%22%3A%20true%2C%0A%20%20%22reflectionNameOrDatasetPath%22%3A%20%22samples.dremio.com%22%0A%7D' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the endpoint-specific documentation to learn which attributes each endpoint supports for the `filter` query parameter.

### orderBy Query Parameter

Use the `orderBy` query parameter to organize the response in ascending or descending order based on the value of the specified attribute. The default is ascending order. To specify descending order, add a `-` character before the attribute name.

For example, the [Reflection summary](/current/reference/api/reflections/reflection-summary/#retrieving-a-reflection-summary) endpoint supports ordering the response by ReflectionName, datasetName, or reflectionType. To organize the response in ascending order by ReflectionName:

Example Request with orderBy Query Parameter (Ascending Order)

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?orderBy=reflectionName' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

To organize the response in descending order, add a `-` before the attribute name:

Example Request with orderBy Query Parameter (Descending Order)

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?orderBy=-reflectionName' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the endpoint-specific documentation to learn which attributes each endpoint supports for the `orderBy` query parameter.

### limit and offset Query Parameters

The `limit` query parameter allows you to retrieve a specific number of results. For endpoints that support the `limit` query parameter, you can specify the number of results to retrieve. For example, if you only want to retrieve the first 10 available results, add `?limit=10` to the request URL:

Example Request for First 10 Results with Limit Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=10' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

The `offset` query parameter allows you to skip a specific number of results in the response. When a response contains many results, you can use the `limit` and `offset` query parameters together to break the response into pages.

For example, consider a job result response object that contains 5000 results. The Job API allows you to retrieve a maximum of 500 results per request. To retrieve all 5000 results, start by adding `?limit=500` to the request URL to retrieve the first 500:

Example Request for First 500 Results with Limit Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=500' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

In the next request, to retrieve the next 500 results (rows 501-1000), add `&offset=500` to the request URL:

Example Request for Results 501-1000 with limit and offset Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=500&offset=500' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

To retrieve the next 500 results (rows 1001-1500), increment the `offset` parameter to 1000 in the next request:

Example Request for Results 1001-1500 with limit and offset Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=500&offset=1000' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

Continue incrementing the `offset` parameter in requests until you have retrieved all 5000 results.

Read the documentation for each API to learn about endpoint-specific support for the `limit` and `offset` query parameters.

### type Query Parameter

Use the `type` query parameter to limit your request so that the response includes only results for the type you specify.

For example, if an endpoint supports the `type` query parameter, and the endpoint's list of valid values includes `SOURCE`, you can limit the response so that it includes only results for sources. Append `?type=SOURCE` to the request URL:

Example Request with type Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/privileges?type=SOURCE' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the documentation for each API to learn about endpoint-specific support for the `type` query parameter, including lists of valid values.

### include and exclude Query Parameters

Some APIs exclude non-default attributes or include lengthy attributes in the default GET responses. These APIs support the `include` and `exclude` query parameters, which you can use to include or exclude certain attributes in the responses for GET endpoints.

The `include` query parameter allows you to include non-default attributes in the response. For example, in the Catalog API, you can include a catalog object's `permissions` array in the response:

Example Request with include Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/ffbe8c1d-1db7-48d1-9c58-f452838fedc0?include=permissions' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

The `exclude` query parameter allows you to exclude supported attributes from the response. For example, this Catalog API request excludes the object's `children` attribute from the response:

Example Request with exclude Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/ffbe8c1d-1db7-48d1-9c58-f452838fedc0?exclude=children' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the documentation for each API to learn about endpoint-specific support for the `include` and `exclude` query parameters, including information about supported values.

### createdBy Query Parameter

Use the `createdBy` query parameter to limit the request to objects created by a specific user.

For example, this Scripts API request retrieves only scripts that were created by the user whose ID is `8be516f3-04c4-4d19-824d-5a70b3c4442e`:

Example Request with createdBy Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/scripts?createdBy=8be516f3-04c4-4d19-824d-5a70b3c4442e' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

### ownedBy Query Parameter

Use the `ownedBy` query parameter to limit the request to objects owned by a specific user.

For example, this Scripts API request retrieves only scripts that are owned by the user whose ID is `8be516f3-04c4-4d19-824d-5a70b3c4442e`:

Example Request with ownedBy Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/scripts?ownedBy=8be516f3-04c4-4d19-824d-5a70b3c4442e' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

### search Query Parameter

Use the `search` query parameter to limit the request to objects that contain values that include the search string.

For example, the Scripts API supports the `search` query parameter for the name attribute. This Scripts API request retrieves only scripts whose values for the name attribute include `dev`:

Example Request with search Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/scripts?search=dev' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the documentation for each API to learn about endpoint-specific support for the `search` query parameter, including information about searchable attributes.

### maxChildren Query Parameter

The `maxChildren` query parameter allows you to specify the maximum number of child objects to include in each response. This example shows a request URL that uses the `nextPageToken` query parameter with the `maxChildren` query parameter set to 25:

Example Request with maxChildren Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/2b1be882-7012-4a99-8d6c-82e32e4562e4?maxChildren=25' \  
--header 'Authorization: Bearer <dremioAccessToken>' \  
--header 'Content-Type: application/json'
```

Use the `maxChildren` query parameter in concert with the [`pageToken` query parameter](/current/reference/api/#user-specified-maximum) to split large sets of results into multiple pages.

## Response Headers

Dremio API responses include HTTP headers that provide additional information about responses. Each header includes a case-insensitive name and a value, separated by a colon.

The following response headers are common to Dremio API endpoints:

| Header Name | Example Value | Description |
| --- | --- | --- |
| Allow | GET,OPTIONS | Request methods the endpoint supports. |
| Cache-Control | no-cache, no-store | Caching instructions for browsers and shared caches. |
| Content-Length | 2188 | Size of the response body, in bytes. |
| Content-Type | application/json | MIME type of the object. |
| Date | Fri, 14 Apr 2023 19:39:53 GMT | Date and time when the response originated. |
| Vary | Accept-Encoding, User-Agent | Names of request headers that could have affected the response's generation. |
| x-content-type-options | nosniff | Instructions about following the MIME type in the content-type header. Blocks content sniffing. |
| x-xss-protection | 1; mode=block | Instructions used to stop pages from loading when a browser detects reflected cross-site scripting attacks. |

Was this page helpful?

[Previous

Admin CLI](/current/reference/admin-cli/)[Next

Catalog](/current/reference/api/catalog/)

* Base URL
* Authentication
  + OAuth Access Tokens Enterprise
  + Personal Access Tokens Enterprise
  + Dremio Authentication Tokens
  + Example
* Errors
* Query Parameters
  + pageToken Query Parameter
  + maxResults Query Parameter
  + filter Query Parameter
  + orderBy Query Parameter
  + limit and offset Query Parameters
  + type Query Parameter
  + include and exclude Query Parameters
  + createdBy Query Parameter
  + ownedBy Query Parameter
  + search Query Parameter
  + maxChildren Query Parameter
* Response Headers

---

# Source: https://docs.dremio.com/current/reference/sql/

Version: current [26.x]

On this page

# SQL Reference

Dremio provides comprehensive SQL access to your data, no matter where it is stored.

* [Data Types](/current/reference/sql/data-types/)
* [SQL Functions](/current/reference/sql/sql-functions/)
* [SQL Commands](/current/reference/sql/commands/)
* [Reserved Words](/current/reference/sql/reserved-keywords)
* [System Tables](/current/reference/sql/system-tables)
* [Table Functions](/current/reference/sql/table-functions)
* [Information Schema](/current/reference/sql/information-schema)

## Additional Resources

Find out more about using SQL by enrolling in the [SQL for Data Analysts course in Dremio University](https://university.dremio.com/course/sql-data-analysts).

Was this page helpful?

[Previous

API Reference](/current/reference/api/)[Next

Data Types](/current/reference/sql/data-types/)

* Additional Resources

---

# Source: https://docs.dremio.com/current/reference/bulletins/

Version: current [26.x]

# Security Bulletins

Dremio publishes security bulletins that disclose vulnerabilities found in our supported products to inform customers about risks that may be present in their production environments.

Security bulletins are usually published when fixes are available in the affected products. In some cases, we may disclose a vulnerability before the fix is available.

Security bulletins include the following information:

* Type
* Qualitative rating as determined by CVSSv3.1 analysis
* Issue description
* Issue impact
* Available mitigations or fixes

| Bulletin | Type | CVSS Rating | Subject | Description |
| --- | --- | --- | --- | --- |
| [2025-04-21-01](/current/reference/bulletins/2025-04-21-01) | Vulnerability | High | Security Update | An authenticated API endpoint allows arbitrary file deletion. |
| [2024-02-07-01](/current/reference/bulletins/2024-02-07-01) | Vulnerability | Medium | Security Update | The COPY INTO command does not verify users' SELECT privileges. |
| [2024-01-12-01](/current/reference/bulletins/2024-01-12-01) | Vulnerability | High | Security Update | Path traversal vulnerability bypassed folder-level role-based access control (RBAC). |
| [2024-01-09-01](/current/reference/bulletins/2024-01-09-01) | Vulnerability | High | Security Update | The Dremio-to-Dremio connector does not fully validate table-level access in certain cases. |
| [2023-07-22-03](/current/reference/bulletins/2023-07-22-03) | Vulnerability | Medium | Security Update | Potential unintended user access to restricted data as a result of previously cached view. |
| [2023-07-22-02](/current/reference/bulletins/2023-07-22-02) | Vulnerability | Medium | Security Update | Potential unintended user access to restricted data as a result of accelerated DML operation. |
| [2023-07-22-01](/current/reference/bulletins/2023-07-22-01) | Vulnerability | Medium | Security Update | Potential unintended user access to restricted data as a result of previously-executed cached plans. |

Was this page helpful?

[Previous

SQL Reference](/current/reference/sql/)[Next

2025-04-21-01](/current/reference/bulletins/2025-04-21-01)