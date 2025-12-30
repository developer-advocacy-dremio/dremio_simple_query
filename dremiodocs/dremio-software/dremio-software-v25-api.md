# Dremio API Documentation - dremio-software-v25-api.md



---

# Source: https://docs.dremio.com/25.x/reference/api/

Version: 25.x

On this page

# API Reference

The Dremio REST API is organized by resource types such as `sources` and is designed around RESTful principles. HTTP `GET` is used to retrieve existing resources,
`POST` creates new ones, `PUT` updates them and `DELETE` removes them.

## Base URL[​](#base-url "Direct link to Base URL")

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

## Authentication[​](#authentication "Direct link to Authentication")

The Dremio REST API requires authentication with either a personal access token created in the Dremio UI or an authentication token generated with your username and password. Follow the instructions in this section to learn how to authenticate to the Dremio REST API with a [personal access token](#personal-access-token) or an [authentication token](#authentication-token).

### Personal Access Token Enterprise[​](#personal-access-token-enterprise "Direct link to personal-access-token-enterprise")

Personal access tokens (PATs) are created in the Dremio UI. Follow the instructions in [Creating a PAT](/25.x/security/authentication/personal-access-tokens/#creating-a-pat) to get a PAT to use in API requests.

API requests that use a PAT token must use the Authorization header. The header's value must specify the `Bearer` type followed by a space and the PAT: `Bearer {PAT}`. This example request to retrieve a catalog demonstrates how to use a PAT in an API request:

Example Request Using PAT

```
curl -X GET 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer dJhGBUDAVv+9Wlsp/I/o/87Vq+omuvpC/YEy6U25S79i74KhD2W6q2sr44emKy==' \  
--header 'Content-Type: application/json'
```

### Authentication Token[​](#authentication-token "Direct link to Authentication Token")

Authentication tokens are generated from your Dremio username and password. They expire every 30 hours. When an authentication token expires, you must generate a new one. API requests that use an authentication token must use the Authorization header.

caution

API versions prior to v3 are considered internal and are subject to change without notice.

To generate an authentication token:

1. Send an API request to the login URL, with your Dremio username and password in the request body.

Example Request

```
curl -X POST 'http://{hostname}/apiv2/login' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
"userName": "dremio",  
"password": "dremio123"  
}'
```

The request returns a JSON user structure:

Example Response

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

If your password includes single or double quotes, you may need to escape the quotes in your authentication token request. The required escapes vary depending on how you send the request.

For example, if you use cURL and the password is `example'6852"`, the password value should be `example'\''6852\"` in the authentication token request.

2. Copy the value of the token attribute in the JSON user structure. This value is called the token string.
3. Append the token string to `_dremio` to compose the required Authorization header for API requests: `_dremio{tokenstring}`.

   This example request to retrieve a catalog demonstrates how to use the token string retrieved in step 1:

   Example Request Using Authentication Token

   ```
   curl -X GET 'https://{hostname}/api/v3/catalog' \  
   --header 'Authorization: _dremio4ksrt534vk7fkq64xh55g7776b' \  
   --header 'Content-Type: application/json'
   ```

## Errors[​](#errors "Direct link to Errors")

Error messages will be sent back in the response body using the following format:

Error message format

```
{  
  "errorMessage": "brief error message",  
  "moreInfo": "detailed error message"  
}
```

## Query Parameters[​](#query-parameters "Direct link to Query Parameters")

Dremio supports query parameters for many API endpoints. The documentation for each API lists the supported query parameters for specific endpoints, along with any default and maximum values for the query parameters for that endpoint.

### pageToken Query Parameter[​](#pagetoken-query-parameter "Direct link to pageToken Query Parameter")

Use the `pageToken` query parameter to split large sets of results into multiple pages.

Endpoints may support the `pageToken` query parameter based on either a [built-in maximum](/25.x/reference/api/#built-in-maximum) number of results per page or a [user-specified maximum](/25.x/reference/api/#user-specified-maximum) that is established with a separate query parameter. The documentation for each API lists the built-in maximum or the query parameter to use to specify a maximum, as applicable.

note

Do not change any other query parameters included in the request URL when you use `pageToken`.

#### Built-in Maximum[​](#built-in-maximum "Direct link to Built-in Maximum")

If the endpoint has a built-in maximum number of results per page, responses automatically include a page token attribute when the response contains more results than the built-in maximum. Use the value for this token in the request URL as the `pageToken` value to retrieve the next page of results.

As an example, the [Reflection summary](/25.x/reference/api/reflections/reflection-summary/#retrieving-a-reflection-summary) endpoint supports the `pageToken` parameter. If the Reflection summary contains more than 50 results, the response will include the `nextPageToken` attribute. To retrieve the next 50 results, add `?pageToken={nextPageToken_value}` to the request URL:

Example Request with pageToken Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?pageToken=BhQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

For subsequent requests, replace the `pageToken` value in the request URL with the token value from the previous response. If the response does not include a token attribute and value, you have retrieved the last page of available results.

#### User-Specified Maximum[​](#user-specified-maximum "Direct link to User-Specified Maximum")

For endpoints that require users to specify a maximum number of results per page with a separate query parameter, responses only include a page token attribute if your initial request URL includes the separate query parameter and the response contains more results than the maximum you specify. Add the value for this token to the request URL as the `pageToken` value, keeping the separate query parameter as well, to retrieve the next page of results.

Catalog API endpoints for retrieving non-filesystem [sources](/25.x/reference/api/catalog/source/#retrieving-a-source-by-id), [spaces](/25.x/reference/api/catalog/container-space#retrieving-a-space-by-id), and [folders](/25.x/reference/api/catalog/container-folder#retrieving-a-folder-by-id) by ID or path support the [`maxChildren` query parameter](/25.x/reference/api/#maxchildren-query-parameter) for specifying the maximum number of child objects to include in each response. If the response contains more than the specified number of child objects, the response includes the `nextPageToken` attribute. To retrieve the next page of results, add `?pageToken={nextPageToken_value}` to the request URL. This example shows a request URL that uses the `nextPageToken` query parameter with the `maxChildren` query parameter set to 25:

Example Request with maxChildren and pageToken Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/catalog/2b1be882-7012-4a99-8d6c-82e32e4562e4?maxChildren=25&pageToken=BhQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

For subsequent requests, replace the `pageToken` value in the request URL with the token value from the previous response. If the response does not include a token attribute and value, you have retrieved the last page of available results.

### maxResults Query Parameter[​](#maxresults-query-parameter "Direct link to maxResults Query Parameter")

Use the `maxResults` query parameter to specify the maximum number of results to retrieve in each request.

For example, if you want to retrieve no more than 25 results for an endpoint that supports the `maxResults` query parameter, append `?maxResults=25` to the request URL:

Example Request with maxResults Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?maxResults=25' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

### filter Query Parameter[​](#filter-query-parameter "Direct link to filter Query Parameter")

Use the `filter` query parameter to filter responses so that they include only results with the specified attributes and values. The value for the `filter` query parameter is a URL-encoded JSON string that represents a JSON object that specifies the desired attributes and values.

As an example, the [Reflection summary](/25.x/reference/api/reflections/reflection-summary/#retrieving-a-reflection-summary) endpoint supports the `filter` query parameter for certain specific attributes. To retrieve only the raw Reflections that are refreshed manually or by schedule, are enabled, and apply to datasets with `samples.dremio.com` in their paths, the `filter` JSON object would look like this:

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
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the endpoint-specific documentation to learn which attributes each endpoint supports for the `filter` query parameter.

### orderBy Query Parameter[​](#orderby-query-parameter "Direct link to orderBy Query Parameter")

Use the `orderBy` query parameter to organize the response in ascending or descending order based on the value of the specified attribute. The default is ascending order. To specify descending order, add a `-` character before the attribute name.

For example, the [Reflection summary](/25.x/reference/api/reflections/reflection-summary/#retrieving-a-reflection-summary) endpoint supports ordering the response by reflectionName, datasetName, or reflectionType. To organize the response in ascending order by reflectionName:

Example Request with orderBy Query Parameter (Ascending Order)

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?orderBy=reflectionName' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

To organize the response in descending order, add a `-` before the attribute name:

Example Request with orderBy Query Parameter (Descending Order)

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?orderBy=-reflectionName' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the endpoint-specific documentation to learn which attributes each endpoint supports for the `orderBy` query parameter.

### limit and offset Query Parameters[​](#limit-and-offset-query-parameters "Direct link to limit and offset Query Parameters")

The `limit` query parameter allows you to retrieve a specific number of results. For endpoints that support the `limit` query parameter, you can specify the number of results to retrieve. For example, if you only want to retrieve the first 10 available results, add `?limit=10` to the request URL:

Example Request for First 10 Results with Limit Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=10' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

The `offset` query parameter allows you to skip a specific number of results in the response. When a response contains many results, you can use the `limit` and `offset` query parameters together to break the response into pages.

For example, consider a job result response object that contains 5000 results. The Job API allows you to retrieve a maximum of 500 results per request. To retrieve all 5000 results, start by adding `?limit=500` to the request URL to retrieve the first 500:

Example Request for First 500 Results with Limit Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=500' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

In the next request, to retrieve the next 500 results (rows 501-1000), add `&offset=500` to the request URL:

Example Request for Results 501-1000 with limit and offset Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=500&offset=500' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

To retrieve the next 500 results (rows 1001-1500), increment the `offset` parameter to 1000 in the next request:

Example Request for Results 1001-1500 with limit and offset Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/job/{id}/results?limit=500&offset=1000' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Continue incrementing the `offset` parameter in requests until you have retrieved all 5000 results.

Read the documentation for each API to learn about endpoint-specific support for the `limit` and `offset` query parameters.

### type Query Parameter[​](#type-query-parameter "Direct link to type Query Parameter")

Use the `type` query parameter to limit your request so that the response includes only results for the type you specify.

For example, if an endpoint supports the `type` query parameter, and the endpoint's list of valid values includes `SOURCE`, you can limit the response so that it includes only results for sources. Append `?type=SOURCE` to the request URL:

Example Request with type Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/privileges?type=SOURCE' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the documentation for each API to learn about endpoint-specific support for the `type` query parameter, including lists of valid values.

### include and exclude Query Parameters[​](#include-and-exclude-query-parameters "Direct link to include and exclude Query Parameters")

Some APIs exclude non-default attributes or include lengthy attributes in the default GET responses. These APIs support the `include` and `exclude` query parameters, which you can use to include or exclude certain attributes in the responses for GET endpoints.

The `include` query parameter allows you to include non-default attributes in the response. For example, in the Catalog API, you can include a catalog object's `permissions` array in the response:

Example Request with include Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/ffbe8c1d-1db7-48d1-9c58-f452838fedc0?include=permissions' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

The `exclude` query parameter allows you to exclude supported attributes from the response. For example, this Catalog API request excludes the object's `children` attribute from the response:

Example Request with exclude Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/ffbe8c1d-1db7-48d1-9c58-f452838fedc0?exclude=children' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the documentation for each API to learn about endpoint-specific support for the `include` and `exclude` query parameters, including information about supported values.

### createdBy Query Parameter[​](#createdby-query-parameter "Direct link to createdBy Query Parameter")

Use the `createdBy` query parameter to limit the request to objects created by a specific user.

For example, this Scripts API request retrieves only scripts that were created by the user whose ID is `8be516f3-04c4-4d19-824d-5a70b3c4442e`:

Example Request with createdBy Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/scripts?createdBy=8be516f3-04c4-4d19-824d-5a70b3c4442e' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

### ownedBy Query Parameter[​](#ownedby-query-parameter "Direct link to ownedBy Query Parameter")

Use the `ownedBy` query parameter to limit the request to objects owned by a specific user.

For example, this Scripts API request retrieves only scripts that are owned by the user whose ID is `8be516f3-04c4-4d19-824d-5a70b3c4442e`:

Example Request with ownedBy Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/scripts?ownedBy=8be516f3-04c4-4d19-824d-5a70b3c4442e' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

### search Query Parameter[​](#search-query-parameter "Direct link to search Query Parameter")

Use the `search` query parameter to limit the request to objects that contain values that include the search string.

For example, the Scripts API supports the `search` query parameter for the name attribute. This Scripts API request retrieves only scripts whose values for the name attribute include `dev`:

Example Request with search Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/scripts?search=dev' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Read the documentation for each API to learn about endpoint-specific support for the `search` query parameter, including information about searchable attributes.

### maxChildren Query Parameter[​](#maxchildren-query-parameter "Direct link to maxChildren Query Parameter")

The `maxChildren` query parameter allows you to specify the maximum number of child objects to include in each response. This example shows a request URL that uses the `nextPageToken` query parameter with the `maxChildren` query parameter set to 25:

Example Request with maxChildren Query Parameter

```
curl -X GET 'https://{hostname}/api/v3/catalog/2b1be882-7012-4a99-8d6c-82e32e4562e4?maxChildren=25' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Use the `maxChildren` query parameter in concert with the [`pageToken` query parameter](/25.x/reference/api/#user-specified-maximum) to split large sets of results into multiple pages.

## Response Headers[​](#response-headers "Direct link to Response Headers")

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

Reference](/25.x/reference/)[Next

Catalog](/25.x/reference/api/catalog/)

* [Base URL](#base-url)
* [Authentication](#authentication)
  + [Personal Access Token Enterprise](#personal-access-token-enterprise)
  + [Authentication Token](#authentication-token)
* [Errors](#errors)
* [Query Parameters](#query-parameters)
  + [pageToken Query Parameter](#pagetoken-query-parameter)
  + [maxResults Query Parameter](#maxresults-query-parameter)
  + [filter Query Parameter](#filter-query-parameter)
  + [orderBy Query Parameter](#orderby-query-parameter)
  + [limit and offset Query Parameters](#limit-and-offset-query-parameters)
  + [type Query Parameter](#type-query-parameter)
  + [include and exclude Query Parameters](#include-and-exclude-query-parameters)
  + [createdBy Query Parameter](#createdby-query-parameter)
  + [ownedBy Query Parameter](#ownedby-query-parameter)
  + [search Query Parameter](#search-query-parameter)
  + [maxChildren Query Parameter](#maxchildren-query-parameter)
* [Response Headers](#response-headers)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/

Version: 25.x

On this page

# Catalog

Use the Catalog API to retrieve and manage [sources](/25.x/reference/api/catalog/source/) and [spaces](/25.x/reference/api/catalog/container-space/) as well as the [folders](/25.x/reference/api/catalog/container-folder/), [files](/25.x/reference/api/catalog/file/), [tables](/25.x/reference/api/catalog/table/), and [views](/25.x/reference/api/catalog/view/) they contain. The Catalog API also includes endpoints for retrieving [lineage](/25.x/reference/api/catalog/lineage/) information for datasets and for creating and managing [tags](/25.x/reference/api/catalog/tag/), [wikis](/25.x/reference/api/catalog/wiki/), [privileges](/25.x/reference/api/catalog/privileges/), and [grants](/25.x/reference/api/catalog/grants/) on catalog objects.

Use the Catalog API endpoint described on this page to retrieve a list of the spaces and sources in your Dremio organization. The response contains the IDs required to make requests to other Catalog API endpoints to create, retrieve, update, and delete objects in your catalog.

Catalog Object

```
{  
  "data": [  
    {  
      "id": "a7b1bc39-bffa-4c30-a5eb-5bdaf5bd0959",  
      "path": [  
        "@dremio"  
      ],  
      "tag": "0QVA7wGyiY0=",  
      "type": "CONTAINER",  
      "containerType": "HOME",  
      "stats": {  
        "datasetCount": 18,  
        "datasetCountBounded": false  
      },  
      "permissions": [  
        "READ",  
        "WRITE",  
        "ALTER_REFLECTION",  
        "SELECT",  
        "ALTER",  
        "VIEW_REFLECTION",  
        "MODIFY",  
        "MANAGE_GRANTS",  
        "CREATE_TABLE",  
        "DROP",  
        "EXTERNAL_QUERY",  
        "INSERT",  
        "TRUNCATE",  
        "DELETE",  
        "UPDATE",  
        "EXECUTE",  
        "CREATE_SOURCE",  
        "ALL"  
      ]  
    },  
    {  
      "id": "ed1013cb-4fea-6552-8d43-015215a38bcc",  
      "path": [  
        "Testing"  
      ],  
      "tag": "PR1M7B1Rhjs=",  
      "type": "CONTAINER",  
      "containerType": "SPACE",  
      "stats": {  
        "datasetCount": 3,  
        "datasetCountBounded": false  
      },  
      "createdAt": "2023-02-14T19:28:40.840Z",  
      "permissions": [  
        "READ",  
        "WRITE",  
        "ALTER_REFLECTION",  
        "SELECT",  
        "ALTER",  
        "VIEW_REFLECTION",  
        "MODIFY",  
        "MANAGE_GRANTS",  
        "CREATE_TABLE",  
        "DROP",  
        "EXTERNAL_QUERY",  
        "INSERT",  
        "TRUNCATE",  
        "DELETE",  
        "UPDATE",  
        "EXECUTE",  
        "CREATE_SOURCE",  
        "ALL"  
      ]  
    },  
    {  
      "id": "6b714877-760e-115b-aefd-799430b3ceab",  
      "path": [  
        "Samples"  
      ],  
      "tag": "nEjWZGnrAO0=",  
      "type": "CONTAINER",  
      "containerType": "SOURCE",  
      "stats": {  
        "datasetCount": 10,  
        "datasetCountBounded": false  
      },  
      "createdAt": "2023-01-04T22:13:02.536Z",  
      "permissions": [  
        "READ",  
        "WRITE",  
        "ALTER_REFLECTION",  
        "SELECT",  
        "ALTER",  
        "VIEW_REFLECTION",  
        "MODIFY",  
        "MANAGE_GRANTS",  
        "CREATE_TABLE",  
        "DROP",  
        "EXTERNAL_QUERY",  
        "INSERT",  
        "TRUNCATE",  
        "DELETE",  
        "UPDATE",  
        "EXECUTE",  
        "CREATE_SOURCE",  
        "ALL"  
      ]  
    }  
  ]  
}
```

## Catalog Attributes[​](#catalog-attributes "Direct link to Catalog Attributes")

[data](/25.x/reference/api/catalog/#attributes-of-objects-in-the-data-array) Array of Object

List of catalog objects in the Dremio organization.

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

id String (UUID)

Unique identifier of the catalog object.

Example: ed1013cb-4fea-6552-8d43-015215a38bcc

---

path Array of String

Path of the catalog object within Dremio, expressed as an array.

Example: ["Testing"]

---

tag String

Unique identifier of the version of the catalog object. Dremio changes the tag whenever the catalog object changes and uses the tag to ensure that PUT requests apply to the most recent version of the catalog object.

Example: PR1M7B1Rhjs=

---

type String

Type of the catalog object. For objects that can contain other catalog objects (the only objects this endpoint retrieves), the type is `CONTAINER`.

Example: CONTAINER

---

containerType String

For catalog objects with the type CONTAINER, the type of container.

Enum: SPACE, SOURCE, FOLDER, HOME

Example: SPACE

---

[stats](/25.x/reference/api/catalog/#attributes-of-the-stats-object) Object

Information about the number of datasets in the catalog object and whether the dataset count is bounded. Appears in the response only if the request URL includes the [datasetCount](/25.x/reference/api/catalog/#parameters) query parameter.

Example: {"datasetCount": 18,"datasetCountBounded": false}

---

createdAt String

Date and time that the catalog object was created, in UTC format.

Example: 2023-02-14T19:28:40.840Z

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the catalog object. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ,"WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

##### Attributes of the `stats` Object[​](#attributes-of-the-stats-object "Direct link to attributes-of-the-stats-object")

datasetCount Integer

Number of datasets the catalog object contains.

Example: 18

---

datasetCountBounded Boolean

If the dataset count is bounded, the value is `true`. Otherwise, the value is `false`.

Example: false

## Retrieving a Catalog[​](#retrieving-a-catalog "Direct link to Retrieving a Catalog")

Retrieve the catalog for the current Dremio instance.

Method and URL

```
GET /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

include Query   String   Optional

Include a non-default attribute in the response. The available values for the include query parameter are `permissions` (Enterprise-only) and `datasetCount`. Specify `permissions` to include each catalog object's permissions array in the response. Specify `datasetCount` to include the [stats object](/25.x/reference/api/catalog/#attributes-of-the-stats-object) in the response. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "id": "a7b1bc39-bffa-4c30-a5eb-5bdaf5bd0959",  
      "path": [  
        "@dremio"  
      ],  
      "tag": "0QVA7wGyiY0=",  
      "type": "CONTAINER",  
      "containerType": "HOME"  
    },  
    {  
      "id": "ed1013cb-4fea-6552-8d43-015215a38bcc",  
      "path": [  
        "Testing"  
      ],  
      "tag": "PR1M7B1Rhjs=",  
      "type": "CONTAINER",  
      "containerType": "SPACE",  
      "createdAt": "2023-02-14T19:28:40.840Z"  
    },  
    {  
      "id": "6b714877-760e-115b-aefd-799430b3ceab",  
      "path": [  
        "Samples"  
      ],  
      "tag": "nEjWZGnrAO0=",  
      "type": "CONTAINER",  
      "containerType": "SOURCE",  
      "createdAt": "2023-01-04T22:13:02.536Z"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

API Reference](/25.x/reference/api/)[Next

Source](/25.x/reference/api/catalog/source/)

* [Catalog Attributes](#catalog-attributes)
* [Retrieving a Catalog](#retrieving-a-catalog)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/datasets/

Version: 25.x

On this page

# Dataset

note

The Dataset API is supported in Dremio 25.0.5+.

Use the Dataset API to retrieve Dremio's Reflection recommendations for your datasets.

Dataset Object (All Reflections)

```
{  
  "data": [  
    {  
      "type": "RAW",  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "displayFields": [  
        {  
          "name": "pickup_datetime"  
        },  
        {  
          "name": "passenger_count"  
        },  
        {  
          "name": "trip_distance_mi"  
        },  
        {  
          "name": "fare_amount"  
        },  
        {  
          "name": "tip_amount"  
        },  
        {  
          "name": "total_amount"  
        }  
      ],  
      "partitionFields": [  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "passenger_count"  
        }  
      ],  
      "entityType": "reflection"  
    },  
    {  
      "type": "AGGREGATION",  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "dimensionFields": [  
        {  
          "name": "passenger_count",  
          "granularity": "DATE"  
        }  
      ],  
      "measureFields": [  
        {  
          "name": "total_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "trip_distance_mi",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "fare_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "tip_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        }  
      ],  
      "partitionFields": [  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "passenger_count"  
        }  
      ],  
      "entityType": "reflection"  
    }  
  ]  
}
```

## Dataset Attributes[​](#dataset-attributes "Direct link to Dataset Attributes")

[data](/25.x/reference/api/datasets/#attributes-of-objects-in-the-data-array) Array of Object

List of recommended Reflection objects for the specified dataset ID.

#### Attributes of objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

type String

Reflection type. For details, read [Types of Reflections](/25.x/sonar/reflections/types-and-benefits).

Enum: RAW, AGGREGATION

Example: RAW

---

enabled Boolean

If the Reflection is available for accelerating queries, `true`. Otherwise, `false`.

Example: true

---

arrowCachingEnabled Boolean

If Dremio converts data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, `true`. Otherwise, `false`.

Example: false

---

displayFields Array of Object

Information about the fields displayed from the anchor dataset. Each object in the displayFields array contains one attribute: name. Included only for raw Reflections. Not included for aggregation Reflections.

Example: [{"name":"pickup\_datetime"},{"name":"passenger\_count"},{"name":"trip\_distance\_mi"},{"name":"fare\_amount"},{"name":"tip\_amount"},{"name":"total\_amount"}]

---

dimensionFields Array of Object

Information about the dimension fields from the anchor dataset used in the Reflection. Dimension fields are the fields you expect to group by when analyzing data. Each object in the dimensionFields array contains two attributes: name and granularity. Included only for aggregation Reflections. If the anchor dataset does not include any dimension fields, the dimensionFields value is an empty array. Not included for raw Reflections.

Example: [{"name":"passenger\_count","granularity":"DATE"}]

---

measureFields Array of Object

Information about the measure fields from the anchor dataset used in the Reflection. Measure fields are the fields you expect to use for calculations when analyzing the data. Each object in the measureFields array contains two attributes: name and measureTypeList. Included only for aggregation Reflections. If the anchor dataset does not include any measure fields, the measureFields value is an empty array. Not included for raw Reflections.

Example: [{"name":"total\_amount","measureTypeList":["COUNT","SUM"]},{"name":"trip\_distance\_mi","measureTypeList":["COUNT","SUM"]},{"name":"fare\_amount","measureTypeList":["COUNT","SUM"]},{"name":"tip\_amount","measureTypeList":["COUNT","SUM"]}]

---

partitionFields Array of Object

Information about the fields from the anchor dataset used to partition data in the Reflection. Each object in the partitionFields array contains one attribute: name. Included only for aggregation Reflections. If the anchor dataset does not include any partition fields, the partitionFields value is an empty array. Not included for raw Reflections.

Example: [{"name": "dropoff\_date"},{"name": "passenger\_count"}]

---

entityType String

Type of entity. For objects in dataset responses, the entityType is `reflection`.

## Creating and Retrieving Reflection Recommendations for a Dataset[​](#creating-and-retrieving-reflection-recommendations-for-a-dataset "Direct link to Creating and Retrieving Reflection Recommendations for a Dataset")

Create Reflection recommendations for the specified dataset. The response contains the Reflection recommendations.

Method and URL

```
POST /api/v3/dataset/{id}/reflection/recommendation/{type}/
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

The id of the dataset for which you want to create and retrieve recommended Reflections.

Example: 88e5fbdf-4b56-4286-9b8b-bb48e1f350eb

---

type Path   String

The type of Reflection recommendations you want to create and retrieve.

* ALL: Create and retrieve both raw and aggregation Reflection recommendations.
* RAW: Create and retrieve only raw Reflection recommendations.
* AGG: Create and retrieve only aggregation Reflection recommendations.

**NOTE**: The type is not case-sensitive. For example, `AGG`, `agg`, and `aGg` are valid type values for aggregation Reflection recommendations.

Example: ALL

Example Request (All Reflections)

```
curl -X POST 'https://{hostname}/api/v3/dataset/88e5fbdf-4b56-4286-9b8b-bb48e1f350eb/reflection/recommendation/ALL/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response (All Reflections)

```
{  
  "data": [  
    {  
      "type": "RAW",  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "displayFields": [  
        {  
          "name": "pickup_datetime"  
        },  
        {  
          "name": "passenger_count"  
        },  
        {  
          "name": "trip_distance_mi"  
        },  
        {  
          "name": "fare_amount"  
        },  
        {  
          "name": "tip_amount"  
        },  
        {  
          "name": "total_amount"  
        }  
      ],  
      "partitionFields": [  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "passenger_count"  
        }  
      ],  
      "entityType": "reflection"  
    },  
    {  
      "type": "AGGREGATION",  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "dimensionFields": [  
        {  
          "name": "passenger_count",  
          "granularity": "DATE"  
        }  
      ],  
      "measureFields": [  
        {  
          "name": "total_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "trip_distance_mi",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "fare_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "tip_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        }  
      ],  
      "partitionFields": [  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "passenger_count"  
        }  
      ],  
      "entityType": "reflection"  
    }  
  ]  
}
```

Example Request (Raw Reflections)

```
curl -X POST 'https://{hostname}/api/v3/dataset/88e5fbdf-4b56-4286-9b8b-bb48e1f350eb/reflection/recommendation/RAW/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response (Raw Reflections)

```
{  
  "data": [  
    {  
      "type": "RAW",  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "displayFields": [  
        {  
          "name": "pickup_datetime"  
        },  
        {  
          "name": "passenger_count"  
        },  
        {  
          "name": "trip_distance_mi"  
        },  
        {  
          "name": "fare_amount"  
        },  
        {  
          "name": "tip_amount"  
        },  
        {  
          "name": "total_amount"  
        }  
      ],  
      "partitionFields": [  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "passenger_count"  
        }  
      ],  
      "entityType": "reflection"  
    }  
  ]  
}
```

Example Request (Aggregation Reflections)

```
curl -X POST 'https://{hostname}/api/v3/dataset/88e5fbdf-4b56-4286-9b8b-bb48e1f350eb/reflection/recommendation/AGG/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response (Aggregation Reflections)

```
{  
  "data": [  
    {  
      "type": "AGGREGATION",  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "dimensionFields": [  
        {  
          "name": "passenger_count",  
          "granularity": "DATE"  
        }  
      ],  
      "measureFields": [  
        {  
          "name": "total_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "trip_distance_mi",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "fare_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        },  
        {  
          "name": "tip_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
          ]  
        }  
      ],  
      "partitionFields": [  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "passenger_count"  
        }  
      ],  
      "entityType": "reflection"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

405   Method Not Allowed

500   Internal Server Error

Was this page helpful?

[Previous

Grants](/25.x/reference/api/catalog/grants)[Next

External Token Providers](/25.x/reference/api/external-token-providers/)

* [Dataset Attributes](#dataset-attributes)
* [Creating and Retrieving Reflection Recommendations for a Dataset](#creating-and-retrieving-reflection-recommendations-for-a-dataset)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/external-token-providers/

Version: 25.x

On this page

# External Token Providers Enterprise

Use the External Token Providers API to manage [external token providers](/25.x/security/authentication/external-token) that enable client applications to use a [JSON Web Token (JWT)](https://jwt.io/introduction) issued by an identity provider to authenticate to Dremio.

External Token Providers Object

```
{  
  "id": "a32191f2-ede6-4533-9a17-1532eea015aa",  
  "name": "My Token Provider",  
  "audience": [  
    "f7fdd9e0-8332-4131-95ce-b350c3bbeab2"  
  ],  
  "userClaim": "upn",  
  "issuer": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0",  
  "jwks": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys",  
  "type": "JWT",  
  "state": "ENABLED"  
}
```

## External Token Providers Attributes[​](#external-token-providers-attributes "Direct link to External Token Providers Attributes")

id String (UUID)

Unique identifier of the external token provider. Generated by Dremio and immutable.

Example: a32191f2-ede6-4533-9a17-1532eea015aa

---

name String

User-provided name of the external token provider. Used for display only.

Example: My Token Provider

---

audience Array of String

Intended recipients of the JSON Web Token (JWT). If there is only one audience for the JWT, then the audience value contains only one string.

Example: ["f7fdd9e0-8332-4131-95ce-b350c3bbeab2"]

---

userClaim String

Key name for the target claim in the JSON Web Token (JWT). The target claim's value corresponds to the Dremio username.

Example: upn

---

issuer String

URL that identifies the principal that issued the JSON Web Token (JWT).

Example: <https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0>

---

jwks String

Endpoint that hosts the [JWK Set (JWKS)](https://www.rfc-editor.org/rfc/rfc7800.html#section-3.5), a set of public keys used to verify the JSON Web Token (JWT) signature.

Example: <https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys>

---

type String

Type of the tokens associated with the external token provider. The type is always `JWT`.

---

state String

Current state of the external token provider: `ENABLED` (default) or `DISABLED`.

Example: ENABLED

## Listing All External Token Providers[​](#listing-all-external-token-providers "Direct link to Listing All External Token Providers")

Retrieve a list of all available external token providers and the metadata for each provider.

Method and URL

```
GET /api/v3/external-token-providers/
```

### Parameters[​](#parameters "Direct link to Parameters")

pageToken Query   Query   Optional

Token for retrieving the next page of external token providers. If the Dremio instance has more providers than the maximum per page (default 5), the response will include a nextPageToken after the data array. Use the nextPageToken value in your request URL as the pageToken value. Do not change any other query parameters included in the request URL when you use pageToken. Read [pageToken Query Parameter](/cloud/reference/api/#pagetoken-query-parameter) for usage examples.

---

limit Query   Integer   Optional

Number of rows to return. Maximum valid value is `99`. Default is `5`. Read [Limit and Offset Query Parameters](/25.x/reference/api/#limit-and-offset-query-parameters) for usage examples.

Example Request

```
curl -X GET 'https://{hostname}/api/v3/external-token-providers' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "id": "d21bbf72-6ab7-45e8-9466-ae1d9ffe92a7",  
      "name": "My First Provider",  
      "type": "JWT",  
      "state": "DISABLED"  
    },  
    {  
      "id": "a32191f2-ede6-4533-9a17-1532eea015aa",  
      "name": "My Token Provider",  
      "type": "JWT",  
      "state": "ENABLED"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

403   Forbidden

## Creating an External Token Provider[​](#creating-an-external-token-provider "Direct link to Creating an External Token Provider")

Create an external token provider.

Method and URL

```
POST /api/v3/external-token-providers
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

name Body   String

Name to use for the external token provider.

Example: My Token Provider

---

audience Body   Array of String

Intended recipients of the JSON Web Token (JWT).

Example: ["f7fdd9e0-8332-4131-95ce-b350c3bbeab2"]

---

userClaim Body   String

Key name for the target claim in the JSON Web Token (JWT). The target claim's value corresponds to the Dremio username.

Example: upn

---

issuer Body   String

URL that identifies the principal that issued the JSON Web Token (JWT).

Example: <https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0>

---

jwks Body   String   Optional

Endpoint that hosts the [JWK Set (JWKS)](https://www.rfc-editor.org/rfc/rfc7800.html#section-3.5), a set of public keys used to verify the JSON Web Token (JWT) signature. If you do not provide a jwks value, Dremio retrieves the value from `<issuer>/.well-known/openid-configuration`.

Example: <https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys>

Example Request

```
curl -X POST 'https://{hostname}/api/v3/external-token-providers' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "My Token Provider",  
  "audience": [  
    "f7fdd9e0-8332-4131-95ce-b350c3bbeab2"  
  ],  
  "issuer": "https://login.microsoftonline.com/3e334762-b0c6-4c36-9faf-93800f0d6c71/v2.0",  
  "jwks": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys",  
  "userClaim": "upn"  
}'
```

Example Response

```
{  
  "id": "a32191f2-ede6-4533-9a17-1532eea015aa",  
  "name": "My Token Provider",  
  "audience": [  
    "f7fdd9e0-8332-4131-95ce-b350c3bbeab2"  
  ],  
  "userClaim": "upn",  
  "issuer": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0",  
  "jwks": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys",  
  "type": "JWT",  
  "state": "ENABLED"  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

403   Forbidden

## Retrieving an External Token Provider by ID[​](#retrieving-an-external-token-provider-by-id "Direct link to Retrieving an External Token Provider by ID")

Retrieve a specific external token provider by the providers's ID.

Method and URL

```
GET /api/v3/external-token-providers/{id}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the external token provider.

Example:a32191f2-ede6-4533-9a17-1532eea015aa

Example Request

```
curl -X GET 'https://{hostname}/api/v3/external-token-providers/a32191f2-ede6-4533-9a17-1532eea015aa' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "a32191f2-ede6-4533-9a17-1532eea015aa",  
  "name": "My Token Provider",  
  "audience": [  
    "f7fdd9e0-8332-4131-95ce-b350c3bbeab2"  
  ],  
  "userClaim": "upn",  
  "issuer": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0",  
  "jwks": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys",  
  "type": "JWT",  
  "state": "ENABLED"  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

403   Forbidden

404   Not Found

## Updating an External Token Provider[​](#updating-an-external-token-provider "Direct link to Updating an External Token Provider")

Update the specified external token provider.

Method and URL

```
PUT /api/v3/external-token-providers/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the external token provider.

Example: a32191f2-ede6-4533-9a17-1532eea015aa

---

name Body   String

User-provided name of the external token provider.

Example: My Token Provider

---

audience Body   Array of String

Intended recipients of the JSON Web Token (JWT). If there is only one audience for the JWT, then the audience value contains only one string.

Example: ["28edee01-4d0d-46ed-b1ae-52139bc3b3ad"]

---

userClaim Body   String

Key name for the target claim in the JSON Web Token (JWT). The target claim's value corresponds to the Dremio username.

Example: preferred\_username

---

issuer Body   String

URL that identifies the principal that issued the JSON Web Token (JWT).

Example: <https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0>

---

jwks Body   String   Optional

Endpoint that hosts the [JWK Set (JWKS)](https://www.rfc-editor.org/rfc/rfc7800.html#section-3.5), a set of public keys used to verify the JSON Web Token (JWT) signature. If you do not provide a jwks value, Dremio retrieves the value from `<issuer>/.well-known/openid-configuration` using the updated issuer.

Example: <https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys>

---

type Body   String   Optional

Type of the tokens associated with the external token provider. The type is always `JWT`.

Example: JWT

---

state Body   String   Optional

Current state of the external token provider: `ENABLED` or `DISABLED`. If the update request does not include the state parameter, Dremio does not change the state.

Example: ENABLED

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/external-token-providers/a32191f2-ede6-4533-9a17-1532eea015aa' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "My Token Provider",  
  "audience": [  
    "28edee01-4d0d-46ed-b1ae-52139bc3b3ad"  
  ],  
  "userClaim": "preferred_username",  
  "issuer": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0"  
}'
```

Example Response

```
{  
  "id": "a32191f2-ede6-4533-9a17-1532eea015aa",  
  "name": "My Token Provider",  
  "audience": [  
    "28edee01-4d0d-46ed-b1ae-52139bc3b3ad"  
  ],  
  "userClaim": "preferred_username",  
  "issuer": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/v2.0",  
  "jwks": "https://login.microsoftonline.com/959d4644-91e6-4652-9d16-bddeb046c807/discovery/v2.0/keys",  
  "type": "JWT",  
  "state": "ENABLED"  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

403   Forbidden

404   Not Found

## Updating an External Token Provider's State[​](#updating-an-external-token-providers-state "Direct link to Updating an External Token Provider's State")

Update the state for the specified external token provider.

Method and URL

```
PATCH /api/v3/external-token-providers/{id}/state
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the external token provider.

Example: a32191f2-ede6-4533-9a17-1532eea015aa

---

state Body   String

Current state of the external token provider: `ENABLED` or `DISABLED`.

Example: DISABLED

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/external-token-providers/a32191f2-ede6-4533-9a17-1532eea015aa/state' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "state": "DISABLED"  
}'
```

A successful request to update the state for an external token provider returns an empty response with the HTTP `204 No Content` status response code.

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

403   Forbidden

404   Not Found

## Deleting an External Token Provider[​](#deleting-an-external-token-provider "Direct link to Deleting an External Token Provider")

Delete the specified external token provider.

Method and URL

```
DELETE /api/v3/external-token-providers/{id}
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the external token provider that you want to delete.

Example: a32191f2-ede6-4533-9a17-1532eea015aa

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/external-token-providers/a32191f2-ede6-4533-9a17-1532eea015aa' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

204   No Content

403   Forbidden

Was this page helpful?

[Previous

Dataset](/25.x/reference/api/datasets/)[Next

Job](/25.x/reference/api/job/)

* [External Token Providers Attributes](#external-token-providers-attributes)
* [Listing All External Token Providers](#listing-all-external-token-providers)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Creating an External Token Provider](#creating-an-external-token-provider)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving an External Token Provider by ID](#retrieving-an-external-token-provider-by-id)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating an External Token Provider](#updating-an-external-token-provider)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Updating an External Token Provider's State](#updating-an-external-token-providers-state)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting an External Token Provider](#deleting-an-external-token-provider)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/job/

Version: 25.x

On this page

# Job

Use the Job API to get information about a specific job and cancel a running job.

note

To retrieve results for a specific job, use the [Job Results](/25.x/reference/api/job/job-results/) endpoint.

Job Object

```
{  
  "jobState": "COMPLETED",  
  "rowCount": 1003904,  
  "errorMessage": "",  
  "startedAt": "2022-12-13T18:34:14.069Z",  
  "endedAt": "2022-12-13T18:35:09.963Z",  
  "acceleration": {  
    "reflectionRelationships": [  
      {  
        "datasetId": "ef99ab32-aa47-4f4c-4d1c-d40f8035b846",  
        "reflectionId": "63fd1c83-5cde-4133-9e2d-60543550580a",  
        "relationship": "CONSIDERED"  
      },  
      {  
        "datasetId": "596c489c-7949-485b-92a9-c32a4cb51fa2",  
        "reflectionId": "65747723-2319-430p-8a36-3d40b26f45ae",  
        "relationship": "MATCHED"  
      }  
    ]  
  },  
  "queryType": "UI_RUN",  
  "queueName": "LARGE",  
  "queueId": "f6a5ef4f-ce5c-4be4-95b2-092c36721dc5",  
  "resourceSchedulingStartedAt": "2022-12-13T18:34:14.977Z",  
  "resourceSchedulingEndedAt": "2022-12-13T18:34:14.995Z",  
  "cancellationReason": ""  
}
```

## Job Attributes[​](#job-attributes "Direct link to Job Attributes")

jobState String

The job's status. Values `COMPLETED`, `CANCELED`, and `FAILED` are final; other values are considered in running state.

Enum: NOT\_SUBMITTED, STARTING, RUNNING, COMPLETED, CANCELED, FAILED, CANCELLATION\_REQUESTED, PLANNING, PENDING, METADATA\_RETRIEVAL, QUEUED, ENGINE\_START, EXECUTION\_PLANNING, INVALID\_STATE

Example: COMPLETED

---

rowCount Integer

For jobs with `COMPLETED` jobState, the number of rows the job returned. If jobState is not `COMPLETED`, rowCount value is `0`.

Example: 11

---

errorMessage String

For jobs with `FAILED` jobState, the error that caused the failure. For all other jobs, the errorMessage value is empty.

Example: Column 'user\_id' not found in any table.

---

startedAt String

Date and time when the job started, in UTC format.

Example: 2022-12-09T20:16:15.694Z

---

endedAt String

Date and time when the job ended, in UTC format.

Example: 2022-12-09T20:16:19.939Z

---

[acceleration](/25.x/reference/api/job/#attributes-of-the-acceleration-object) Object

For jobs with applicable Reflections, provides more information about the Reflections and their relationships to the job. For jobs that do not have applicable Reflections, the response does not include the acceleration object.

---

queryType String

Job type. If the job's queryType is not set, the value is `UNKNOWN`.

Enum: UI\_RUN, UI\_PREVIEW, UI\_INTERNAL\_PREVIEW, UI\_INTERNAL\_RUN, UI\_EXPORT, ODBC, JDBC, REST, ACCELERATOR\_CREATE, ACCELERATOR\_DROP, UNKNOWN, PREPARE\_INTERNAL, ACCELERATOR\_EXPLAIN, UI\_INITIAL\_PREVIEW

Example: UI\_RUN

---

queueName String

Name of the workload management (WLM) queue to which the job was routed.

Example: SMALL

---

queueId String

ID of the workload management (WLM) queue to which the job was routed.

Example: f6a5ef4f-ce5c-4be4-95b2-092c36721dc5

---

resourceSchedulingStartedAt String

Date and time when the Dremio engine started scheduling the job.

Example: 2022-12-09T20:16:16.141Z

---

resourceSchedulingEndedAt String

Date and time when Dremio engine scheduling ended for the job.

Example: 2022-12-09T20:16:16.162Z

---

cancellationReason String

For canceled jobs, the reason for the cancellation. For all other jobs, the cancellationReason value is empty.

Example: Query was cancelled due to low memory.

#### Attributes of the `acceleration` Object[​](#attributes-of-the-acceleration-object "Direct link to attributes-of-the-acceleration-object")

[reflectionRelationships](/25.x/reference/api/job/#attributes-of-objects-in-the-reflectionrelationships-array) Array of Object

Information about the dataset, Reflection, and type of relationship for each applicable Reflection.

#### Attributes of Objects in the `reflectionRelationships` Array[​](#attributes-of-objects-in-the-reflectionrelationships-array "Direct link to attributes-of-objects-in-the-reflectionrelationships-array")

datasetId String (UUID)

Unique identifier of the dataset associated with the Reflection.

Example: 596c489c-7949-485b-92a9-c32a4cb51fa2

---

reflectionId String (UUID)

Unique identifier of the Reflection.

Example: 65747723-2319-430p-8a36-3d40b26f45ae

---

relationship String

Type of relationship between the Reflection and the job.

Enum: CONSIDERED, MATCHED, CHOSEN

Example: MATCHED

## Retrieving a Job[​](#retrieving-a-job "Direct link to Retrieving a Job")

Retrieve the specified job.

Method and URL

```
GET /api/v3/job/{id}
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the job to retrieve. Get the job ID from responses to [SQL API](/25.x/reference/api/sql/) requests.

Example: 6j6c34cf-9drf-b07a-5ab7-abea69a66d00

Example Request

```
curl -X GET 'https://{hostname}/api/v3/job/6j6c34cf-9drf-b07a-5ab7-abea69a66d00' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response for a COMPLETED Job

```
{  
  "jobState": "COMPLETED",  
  "rowCount": 1003904,  
  "errorMessage": "",  
  "startedAt": "2022-12-13T18:34:14.069Z",  
  "endedAt": "2022-12-13T18:35:09.963Z",  
  "acceleration": {  
    "reflectionRelationships": [  
      {  
        "datasetId": "ef99ab32-aa47-4f4c-4d1c-d40f8035b846",  
        "reflectionId": "63fd1c83-2319-5962-8a36-60543550580a",  
        "relationship": "CONSIDERED"  
      },  
      {  
        "datasetId": "596c489c-7949-485b-92a9-c32a4cb51fa2",  
        "reflectionId": "65747723-4133-9e2d-3k86-3d40b26f45ae",  
        "relationship": "MATCHED"  
      }  
    ]  
  },  
  "queryType": "UI_RUN",  
  "queueName": "LARGE",  
  "queueId": "f6a5ef4f-ce5c-4be4-95b2-092c36721dc5",  
  "resourceSchedulingStartedAt": "2022-12-13T18:34:14.977Z",  
  "resourceSchedulingEndedAt": "2022-12-13T18:34:14.995Z",  
  "cancellationReason": ""  
}
```

Example Response for a CANCELED Job

```
{  
    "jobState": "CANCELED",  
    "rowCount": 0,  
    "errorMessage": "",  
    "startedAt": "2023-02-01T15:07:16.165Z",  
    "endedAt": "2023-02-01T15:07:18.691Z",  
    "queryType": "UI_RUN",  
    "queueName": "LARGE",  
    "queueId": "6ed7841e-e446-4536-8d47-361508e78c18",  
    "resourceSchedulingStartedAt": "2023-02-01T15:07:17.124Z",  
    "resourceSchedulingEndedAt": "2023-02-01T15:07:17.140Z",  
    "cancellationReason": "Query cancelled by user 'USERNAME'"  
}
```

Example Response for a FAILED Job

```
{  
    "jobState": "FAILED",  
    "rowCount": 0,  
    "errorMessage": "ExecutionSetupException: One or more nodes lost connectivity during query.  Identified nodes were [automaster-2.c.dremio-1093.internal:0].",  
    "startedAt": "2023-02-01T16:36:35.897Z",  
    "endedAt": "2023-02-01T16:37:36.098Z",  
    "queryType": "UI_RUN",  
    "queueName": "LARGE",  
    "queueId": "3d04235f-3610-4dd3-95b6-6a29542eb600",  
    "resourceSchedulingStartedAt": "2023-02-01T16:36:37.389Z",  
    "resourceSchedulingEndedAt": "2023-02-01T16:36:37.437Z",  
    "cancellationReason": ""  
}
```

Example Response for a RUNNING Job

```
{  
    "jobState": "RUNNING",  
    "rowCount": 2682474,  
    "errorMessage": "",  
    "startedAt": "2023-02-01T21:30:10.755Z",  
    "queryType": "ACCELERATOR_CREATE",  
    "queueName": "LARGE",  
    "queueId": "f64ff0a0-a925-4dc9-be60-e0703ce3aa24",  
    "resourceSchedulingStartedAt": "2023-02-01T21:30:11.743Z",  
    "resourceSchedulingEndedAt": "2023-02-01T21:30:11.798Z",  
    "cancellationReason": ""  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

403   Forbidden

404   Not Found

## Canceling a Running Job[​](#canceling-a-running-job "Direct link to Canceling a Running Job")

Cancel the specified running job.

note

Canceling a job does not delete the job object. You can still retrieve job objects for canceled jobs.

Method and URL

```
POST /api/v3/job/{id}/cancel
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the job to cancel. Get the job ID from responses to [SQL API](/25.x/reference/api/sql/) requests.

Example: 6j6c34cf-9drf-b07a-5ab7-abea69a66d00

Example request

```
curl -X POST 'https://{hostname}/api/v3/job/6j6c34cf-9drf-b07a-5ab7-abea69a66d00/cancel' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example response

```
No response
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

External Token Providers](/25.x/reference/api/external-token-providers/)[Next

Job Results](/25.x/reference/api/job/job-results)

* [Job Attributes](#job-attributes)
* [Retrieving a Job](#retrieving-a-job)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Canceling a Running Job](#canceling-a-running-job)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)

---

# Source: https://docs.dremio.com/25.x/reference/api/ldap-authorization

Version: 25.x

On this page

# LDAP User Cache

Use the LDAP User Cache API to invalidate the authorization for all users and groups or a single user or group in the LDAP user cache.

note

You must be a member of the Dremio ADMIN role to send requests to the LDAP User Cache API.

## Invalidating LDAP Authorization for All Users and Groups[ ​](#invalidating-ldap-authorization-for-all-users-and-groups "Direct link to Invalidating LDAP Authorization for All Users and Groups")

Invalidate all users' and groups' LDAP authorizations.

Method and URL

```
DELETE /api/v3/cache/authorization
```

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/cache/authorization' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

## Invalidating LDAP Authorization for a Single User or Group by ID[​](#invalidating-ldap-authorization-for-a-single-user-or-group-by-id "Direct link to Invalidating LDAP Authorization for a Single User or Group by ID")

Invalidate LDAP authorization for a single user or group by specifying the ID for the user or group.

note

If you do not provide the ID of a user or group in the request URL, Dremio invalidates the LDAP authorization for all users and groups in the cache.

Method and URL

```
DELETE /api/v3/cache/authorization/{id}
```

### Parameters[​](#parameters "Direct link to Parameters")

name Path   String (UUID)

Unique identifier of the Dremio user or group whose LDAP authorization you want to invalidate.

Example: 2k8bdk96-b267-4d56-9154-e48v5884h5i8

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/cache/authorization/2k8bdk96-b267-4d56-9154-e48v5884h5i8' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

## Invalidating LDAP Authorization for a Single User or Group by Name[​](#invalidating-ldap-authorization-for-a-single-user-or-group-by-name "Direct link to Invalidating LDAP Authorization for a Single User or Group by Name")

Invalidate LDAP authorization for a single user or group by specifying the name for the user or group.

note

If you do not provide the name of a user or group in the request URL, Dremio invalidates the LDAP authorization for all users and groups in the cache.

Method and URL

```
DELETE /api/v3/cache/authorization/{name}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

name Path   String

Name for the Dremio user or group whose LDAP authorization you want to invalidate.

Example: exampleuser1

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/cache/authorization/exampleuser1' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

Was this page helpful?

[Previous

Job Results](/25.x/reference/api/job/job-results)[Next

Node Collections](/25.x/reference/api/nodeCollections/)

* [Invalidating LDAP Authorization for All Users and Groups](#invalidating-ldap-authorization-for-all-users-and-groups)
  + [Response Status Codes](#response-status-codes)
* [Invalidating LDAP Authorization for a Single User or Group by ID](#invalidating-ldap-authorization-for-a-single-user-or-group-by-id)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes-1)
* [Invalidating LDAP Authorization for a Single User or Group by Name](#invalidating-ldap-authorization-for-a-single-user-or-group-by-name)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-2)

---

# Source: https://docs.dremio.com/25.x/reference/api/nodeCollections/

Version: 25.x

On this page

# Node Collections

Use the Node Collections API to deny access to Dremio cluster nodes and retrieve the currently denied nodes for the Dremio instance.

The Node Collections API does not have a corresponding Node Collection object. The endpoints return a list of the currently denied nodes in the response.

note

You must be a member of the Dremio ADMIN role to send requests to the Node Collections API.

## Denying Nodes[​](#denying-nodes "Direct link to Denying Nodes")

Deny access to the specified Dremio cluster nodes.

Method and URL

```
POST /api/v3/nodeCollections/blacklist
```

The request body is a comma-separated list of the names for the nodes that you want to deny, including any currently denied nodes that should remain denied. Format the request body as an array of string, with each node name in double quotes. Use a comma to separate each node name in the list.

Any nodes omitted from the request body, including currently denied nodes, will be allowed.

Example Request

```
curl -X POST 'https://{hostname}/api/v3/nodeCollections/blacklist' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '["localhost-1.c.dremio-1093.external",  "localhost-2.c.dremio-1093.external"]'
```

Example Response

```
[  
  "localhost-1.c.dremio-1093.external",  
  "localhost-2.c.dremio-1093.external"  
]
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

## Retrieving Denied Nodes[​](#retrieving-denied-nodes "Direct link to Retrieving Denied Nodes")

Invalidate the LDAP authorization for a specific user or group by ID.

Method and URL

```
GET /api/v3/nodeCollections/blacklist
```

Example Request

```
curl -X GET 'https://{hostname}/api/v3/nodeCollections/blacklist' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
[  
  "localhost-1.c.dremio-1093.external",  
  "localhost-2.c.dremio-1093.external"  
]
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

## Allowing All Nodes[​](#allowing-all-nodes "Direct link to Allowing All Nodes")

Allow access to all Dremio cluster nodes.

Method and URL

```
POST /api/v3/nodeCollections/blacklist
```

To allow all nodes, send an empty array in the request body.

Example Request

```
curl -X POST 'https://{hostname}/api/v3/nodeCollections/blacklist' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '[]'
```

Example Response

```
[]
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

Was this page helpful?

[Previous

LDAP User Cache](/25.x/reference/api/ldap-authorization)[Next

Reflection](/25.x/reference/api/reflections/)

* [Denying Nodes](#denying-nodes)
  + [Response Status Codes](#response-status-codes)
* [Retrieving Denied Nodes](#retrieving-denied-nodes)
  + [Response Status Codes](#response-status-codes-1)
* [Allowing All Nodes](#allowing-all-nodes)
  + [Response Status Codes](#response-status-codes-2)

---

# Source: https://docs.dremio.com/25.x/reference/api/reflections/

Version: 25.x

On this page

# Reflection

Use the Reflection API to retrieve a list of raw and aggregation Reflections, retrieve individual Reflections, and create, update, and delete Reflections.

A Reflection is an optimized materialization of source data or a query, similar to a materialized view, that is derived from an existing table or view. The query optimizer can accelerate queries by using one or more Reflections to partially or entirely satisfy the queries rather than running queries against the raw data in the data source that underlies the table or view.

Reflection Object (Raw Reflection)

```
{  
  "id": "7a380a24-3b63-436c-9ea0-63cb534cc404",  
  "type": "RAW",  
  "name": "Raw Reflection",  
  "tag": "ureIY76RT7Y=",  
  "createdAt": "2023-01-30T14:11:43.826Z",  
  "updatedAt": "2023-01-30T14:11:43.826Z",  
  "datasetId": "tk973df7-ddf7-4d1e-fa9e-bccf28ae253f",  
  "currentSizeBytes": 4393709246,  
  "totalSizeBytes": 4393709246,  
  "enabled": true,  
  "arrowCachingEnabled": false,  
  "status": {  
    "config": "OK",  
    "refresh": "SCHEDULED",  
    "availability": "AVAILABLE",  
    "combinedStatus": "CAN_ACCELERATE",  
    "failureCount": 0,  
    "lastDataFetch": "2023-01-30T14:11:51.801Z",  
    "expiresAt": "2023-01-30T17:11:51.801Z"  
  },  
  "displayFields": [  
    {  
      "name": "pickup_datetime"  
    },  
    {  
      "name": "passenger_count"  
    },  
    {  
      "name": "trip_distance_mi"  
    },  
    {  
      "name": "fare_amount"  
    },  
    {  
      "name": "tip_amount"  
    },  
    {  
      "name": "total_amount"  
    }  
],  
  "distributionFields": [  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "partitionFields": [  
    {  
      "name": "passenger_count"  
    }  
],  
  "sortFields": [  
    {  
      "name": "pickup_datetime"  
    }  
],  
  "partitionDistributionStrategy": "CONSOLIDATED",  
  "canView": true,  
  "canAlter": true,  
  "entityType": "reflection"  
}
```

Reflection Object (Aggregation Reflection)

```
{  
  "id": "95dda9dd-2371-467f-b68d-fc4c5ea57a8b",  
  "type": "AGGREGATION",  
  "name": "Aggregation Reflection",  
  "tag": "ZpzGgxw2l04=",  
  "createdAt": "2022-07-05T19:19:40.244Z",  
  "updatedAt": "2023-01-10T17:12:40.244Z",  
  "datasetId": "df99ab32-c2d4-4d1c-9e91-2c8be861bb8a",  
  "currentSizeBytes": 18639885,  
  "totalSizeBytes": 142639924,  
  "enabled": true,  
  "arrowCachingEnabled": false,  
  "status": {  
    "config": "OK",  
    "refresh": "SCHEDULED",  
    "availability": "AVAILABLE",  
    "combinedStatus": "CAN_ACCELERATE",  
    "failureCount": 0,  
    "lastDataFetch": "2023-01-10T17:12:40.244Z",  
    "expiresAt": "3022-07-05T19:19:40.244Z"  
  },  
  "dimensionFields": [  
    {  
      "name": "pickup_date"  
    },  
    {  
      "name": "pickup_datetime",  
      "granularity": "DATE"  
    },  
    {  
      "name": "dropoff_date"  
    },  
    {  
      "name": "dropoff_datetime",  
      "granularity": "DATE"  
    },  
    {  
      "name": "passenger_count"  
    },  
    {  
      "name": "total_amount"  
    },  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "measureFields": [  
    {  
      "name": "passenger_count",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "trip_distance_mi",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "fare_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "surcharge",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "tip_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "total_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    }  
],  
  "distributionFields": [  
    {  
      "name": "trip_distance_mi"  
    },  
    {  
      "name": "total_amount"  
    }  
],  
  "partitionFields": [  
    {  
      "name": "dropoff_date"  
    },  
    {  
      "name": "passenger_count"  
    }  
],  
  "sortFields": [  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "partitionDistributionStrategy": "CONSOLIDATED",  
  "canView": true,  
  "canAlter": true,  
  "entityType": "reflection"  
}
```

## Reflection Attributes[​](#reflection-attributes "Direct link to Reflection Attributes")

id String (UUID)

Unique identifier of the Reflection.

Example: 95dda9dd-2371-467f-b68d-fc4c5ea57a8b

---

type String

Reflection type. For more information, read [Types of Reflections](/25.x/sonar/reflections/types-and-benefits).

Enum: RAW, AGGREGATION

Example: AGGREGATION

---

name String

User-provided name for the Reflection. For Reflections created in the Dremio UI, if the user did not provide a name, the default values are `Raw Reflection` and `Aggregation Reflection` (automatically assigned based on the Reflection type).

Example: Aggregation Reflection

---

tag String

Unique identifier of the Reflection instance. Dremio changes the tag whenever the Reflection changes and uses the tag to ensure that PUT requests apply to the most recent version of the Reflection.

Example: ZpzGgxw2l04=

---

createdAt String

Date and time that the Reflection was created, in UTC format.

Example: 2022-07-05T19:19:40.244Z

---

updatedAt String

Date and time that the Reflection was last updated, in UTC format.

Example: 2023-01-10T17:12:40.244Z

---

datasetId String (UUID)

Unique identifier of the anchor dataset that is associated with the Reflection.

Example: df99ab32-c2d4-4d1c-9e91-2c8be861bb8a

---

currentSizeBytes Integer

Data size of the latest Reflection job (if one exists), in bytes.

Example: 18639885

---

totalSizeBytes Integer

Data size of all Reflection jobs that have not been pruned (if any exist), in bytes.

Example: 142639924

---

enabled Boolean

If the Reflection is available for accelerating queries, the value is `true`. Otherwise, the value is `false`.

Example: true

---

arrowCachingEnabled Boolean

If Dremio converts data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, the value is `true`. Otherwise, the value is `false`.

Example: false

---

[status](/25.x/reference/api/reflections/#attributes-of-the-status-object) Object

Information about the status of the Reflection.

Example: {"config": "OK","refresh": "SCHEDULED","availability": "AVAILABLE","combinedStatus": "CAN\_ACCELERATE","failureCount": 0,"lastDataFetch": "2023-01-10T17:12:40.244Z","expiresAt": "3022-07-05T19:19:40.244Z"}

---

[displayFields](/25.x/reference/api/reflections/#attributes-of-objects-in-the-displayfields-array) Array of Object

Information about the fields displayed from the anchor dataset. Each displayFields object contains one attribute: name. Valid only for raw Reflections.

Example: [{"name": "pickup\_datetime"},{"name": "passenger\_count"},{"name": "trip\_distance\_mi"},{"name": "fare\_amount"},{"name": "tip\_amount"},{"name": "total\_amount"}]

---

[dimensionFields](/25.x/reference/api/reflections/#attributes-of-objects-in-the-dimensionfields-array) Array of Object

Information about the dimension fields from the anchor dataset used in the Reflection. Dimension fields are the fields you expect to group by when analyzing data. Each dimensionFields object contains two attributes: name and granularity. Valid only for aggregation Reflections.

Example: [{"name": "pickup\_date","granularity": "DATE"},{"name": "pickup\_datetime","granularity": "DATE"},{"name": "dropoff\_date","granularity": "DATE"},{"name": "dropoff\_datetime","granularity": "DATE"},{"name": "passenger\_count","granularity": "DATE"},{"name": "total\_amount","granularity": "DATE"}]

---

[measureFields](/25.x/reference/api/reflections/#attributes-of-objects-in-the-measurefields-array) Array of Object

Information about the measure fields from the anchor dataset used in the Reflection. Measure fields are the fields you expect to use for calculations when analyzing the data. Each measureFields object contains two attributes: name and measureTypeList. Valid only for aggregation Reflections.

Example: [{"name": "passenger\_count","measureTypeList": ["SUM", "COUNT"]},{"name": "trip\_distance\_mi","measureTypeList": ["SUM", "COUNT"]},{"name": "fare\_amount","measureTypeList": ["SUM", "COUNT"]},{"name": "surcharge","measureTypeList": ["SUM", "COUNT"]},{"name": "tip\_amount","measureTypeList": ["SUM", "COUNT"]},{"name": "total\_amount","measureTypeList": ["SUM", "COUNT"]}]

---

[distributionFields](/25.x/reference/api/reflections/#attributes-of-objects-in-the-distributionfields-array) Array of Object

Information about the distribution fields from the anchor dataset used in the Reflection. Distribution fields allow data from multiple datasets to be co-located and co-partitioned across nodes to minimize data movement during join operations. Each distributionFields object contains one attribute: name.

Example: [{"name": "trip\_distance\_mi"},{"name": "total\_amount"}]

---

[partitionFields](/25.x/reference/api/reflections/#attributes-of-objects-in-the-partitionfields-array) Array of Object

Information about the fields from the anchor dataset used to partition data in the Reflection. Each field name is listed as an individual object. For more information, read [Horizontally Partition Reflections that Have Many Rows](/25.x/sonar/reflections/best-practices#horizontally-partition-reflections-that-have-many-rows).

Example: [{"name": "dropoff\_date"},{"name": "passenger\_count"}]

---

[sortFields](/25.x/reference/api/reflections/#attributes-of-objects-in-the-sortfields-array) Array of Object

Information about the fields from the anchor dataset used for sorting in the Reflection. Each sortFields object contains one attribute: name. For more information, read [Sort Reflections on High-Cardinality Fields](/25.x/sonar/reflections/best-practices#sort-reflections-on-high-cardinality-fields).

Example: [{"name": "trip\_distance\_mi"}]

---

partitionDistributionStrategy String

Method used to optimize data compression when executing Reflections. `CONSOLIDATED` means Dremio minimizes the number of files produced. The query threads pool the data and ensure that the fewest number of files are written to the Reflection store. Optimizing for a smaller number of files generally improves read performance because users can perform fewer searches for a given query. `STRIPED` means Dremio minimizes the time required to refresh the Reflection. Each final-stage query thread opens its own writers to write the data, which can result in many small files if each query thread contains a small amount of data.

Enum: CONSOLIDATED, STRIPED

Example: CONSOLIDATED

---

canView Boolean

If you can view Reflections on all datasets of a source, system, space, or folder, the value is `true`. Otherwise, the value is `false`.

Example: true

---

canAlter Boolean

If you can create, edit, and view Reflections on all datasets of a source, system, space, or folder, the value is `true`. Otherwise, the value is `false`.

Example: true

---

entityType String

Type of the object. For Reflection objects, the entityType is `reflection`.

Example: reflection

#### Attributes of the `status` Object[​](#attributes-of-the-status-object "Direct link to attributes-of-the-status-object")

config String

Status of the Reflection configuration. If the value is `OK`, the Reflection configuration is free of errors. If the value is `INVALID`, the Reflection configuration contains one or more errors.

Enum: OK, INVALID

Example: OK

---

refresh String

Status of the Reflection refresh.

* `GIVEN_UP`: Dremio attempted to refresh the Reflection multiple times, but each attempt has failed and Dremio will not make further attempts.
* `MANUAL`: Refresh period is set to 0, so you must use the Dremio UI to manually refresh the Reflection.
* `RUNNING`: Dremio is currently refreshing the Reflection.
* `SCHEDULED`: The Reflection refreshes according to a schedule.

Enum: GIVEN\_UP, MANUAL, RUNNING, SCHEDULED

Example: SCHEDULED

---

availability String

Status of the Reflection's availability for accelerating queries.

Enum: NONE, INCOMPLETE, EXPIRED, AVAILABLE

Example: AVAILABLE

---

combinedStatus String

Status of the Reflection based on a combination of config, refresh, and availability.

* `CAN_ACCELERATE`: The Reflection is fully functional.
* `CAN_ACCELERATE_WITH_FAILURES`: The most recent refresh failed to obtain a status, but Dremio still has a valid materialization.
* `CANNOT_ACCELERATE_MANUAL`: The Reflection is unable to accelerate any queries, and the `Never Refresh` option is selected for the refresh policy.
* `CANNOT_ACCELERATE_SCHEDULED`: The Reflection is currently unable to accelerate any queries, but it has been scheduled for a refresh at a future time.
* `DISABLED`: The Reflection has been manually disabled.
* `EXPIRED`: The Reflection has expired and cannot be used.
* `FAILED`: The attempt to refresh the Reflection has failed, typically three times in a row. The Reflection is still usable.
* `INVALID`: The Reflection is invalid because the underlying dataset has changed.
* `INCOMPLETE`: One or more pseudo-distributed file system (PDFS) nodes that contain materialized files are down (PFDS is supported for v21 and earlier). Only partial data is available. Configurations that use the Hadoop Distributed File System (HDFS) to store Reflections should not experience incomplete status.
* `REFRESHING`: The Reflection is currently being refreshed.

Example: CAN\_ACCELERATE

---

failureCount Integer

Number of times that an attempt to refresh the Reflection failed.

Example: 0

---

lastDataFetch String

Date and time that the Reflection data was last refreshed, in UTC format. If the Reflection is running, failing, or disabled, the lastDataFetch value is `1969-12-31T23:59:59.999Z`.

Example: 2023-01-10T17:12:40.244Z

---

expiresAt String

Date and time that the Reflection expires, in UTC format. If the Reflection is running, failing, or disabled, the lastDataFetch value is `1969-12-31T23:59:59.999Z`.

Example: 3022-07-05T19:19:40.244Z

---

#### Attributes of Objects in the `displayFields` Array[​](#attributes-of-objects-in-the-displayfields-array "Direct link to attributes-of-objects-in-the-displayfields-array")

name String

Name of the field from the anchor dataset that is displayed in the raw Reflection.

Example: passenger\_count

#### Attributes of Objects in the `dimensionFields` Array[​](#attributes-of-objects-in-the-dimensionfields-array "Direct link to attributes-of-objects-in-the-dimensionfields-array")

name String

Name of the field from the anchor dataset that is configured as a dimension for the Reflection.

Example: pickup\_date

---

granularity String

Grouping used for the dimension field. When timestamp and date fields are configured as dimensions, Dremio can automatically extract and use the day-level date value (`DATE`) or use the field's original value (`NORMAL`).

Enum: DATE, NORMAL

Example: DATE

#### Attributes of Objects in the `measureFields` Array[​](#attributes-of-objects-in-the-measurefields-array "Direct link to attributes-of-objects-in-the-measurefields-array")

name String

Name of the field from the anchor dataset that is configured as a measure for the Reflection.

Example: passenger\_count

---

measureTypeList Array of String

Types of calculations for which Dremio uses the specified measure field.

Enum: APPROX\_COUNT\_DISTINCT, MIN, MAX, UNKNOWN, SUM, COUNT

Example: ["SUM","COUNT"]

#### Attributes of Objects in the `distributionFields` Array[​](#attributes-of-objects-in-the-distributionfields-array "Direct link to attributes-of-objects-in-the-distributionfields-array")

name String

Name of the field from the anchor dataset that is used for co-locating and co-partitioning data from multiple datasets across nodes.

Example: trip\_distance\_mi

#### Attributes of Objects in the `partitionFields` Array[​](#attributes-of-objects-in-the-partitionfields-array "Direct link to attributes-of-objects-in-the-partitionfields-array")

name String

Name of the field from the anchor dataset on which the rows in the Reflection are to be partitioned. If a column is listed as a partition column, it cannot also be listed as a sort column for the same Reflection. In aggregation Reflections, each column specified as a partition column or used in transform must also be listed as a dimension column. In raw Reflections, each column specified as a partition column or used in transform must also be listed as a display column.

Example: trip\_distance\_mi

---

transform Object

The type of partition transform that is applied. The value is an enum. The types are:

**IDENTITY**: Creates one partition per value. This is the default transform. If no transform is specified for a field named by the `name` property, an IDENTITY transform is performed.

IDENTITY Example

```
{  
  "name": "passenger_count",  
  "transform": {  
    "type": "IDENTITY"  
  }  
}
```

**YEAR**: Partitions by year. The field must use the TIMESTAMP or DATE data type.

YEAR Example

```
{  
  "name": "pickup_datetime",  
  "transform": {  
    "type": "YEAR"  
  }  
}
```

**MONTH**: Partitions by month. The field must use the TIMESTAMP or DATE data type.

MONTH Example

```
{  
  "name": "pickup_datetime",  
  "transform": {  
    "type": "MONTH"  
  }  
}
```

**DAY**: Partitions on the equivalent of dateint. The field must use the TIMESTAMP or DATE data type.

DAY Example

```
{  
  "name": "pickup_datetime",  
  "transform": {   
    "type": "DAY"  
  }  
}
```

**HOUR**: Partitions on the equivalent of dateint and hour. The field must use the TIMESTAMP data type.

HOUR Example

```
{  
  "name": "pickup_datetime",  
  "transform": {   
    "type": "HOUR"  
  }  
}
```

**BUCKET**: Partitions data into the number of partitions specified by an integer. For example, if the integer value N is specified, the data is partitioned into N, or (0 to (N-1)), partitions. The partition in which an individual row is stored is determined by hashing the field value and then calculating `<hash_value> mod N`. If the result is 0, the row is placed in partition 0; if the result is 1, the row is placed in partition 1; and so on.

This value must be followed by a `bucketTransform` object. This object takes one property: `bucketCount`. This property takes an integer value.

BUCKET Example

```
{  
  "name": "pickup_datetime",   
  "transform": {  
    "type": "BUCKET",   
    "bucketTransform": {  
      "bucketCount": 1000  
    }  
  }  
}
```

**TRUNCATE**: If the specified field uses the string data type, truncates strings to a maximum of the number of characters specified by an integer. For example, suppose the specified transform is `truncate(1, stateUS)`. A value of `CA` is truncated to `C`, and the row is placed in partition C. A value of `CO` is also truncated to `C`, and the row is also placed in partition C.

If the specified field uses the integer or long data type, truncates field values in the following way: For any `truncate(L, col)`, truncates the field value to the biggest multiple of L that is smaller than the field value. For example, suppose the specified transform is `truncate(10, intField)`. A value of 1 is truncated to 0 and the row is placed in the partition 0. A value of 247 is truncated to 240 and the row is placed in partition 240. If the transform is `truncate(3, intField)`, a value of 13 is truncated to 12 and the row is placed in partition 12. A value of 255 is not truncated, because it is divisble by 3, and the row is placed in partition 255. This value must be followed by a `truncateTransform` object.

This object takes one property: `truncateLength`. This property takes an integer value.

note

The truncate transform does not change field values. It uses field values to calculate the correct partitions in which to place rows.

TRUNCATE Example

```
{   
  "name": "pickup_hour",   
  "transform": {   
    "type": "TRUNCATE",  
    "truncateTransform": {   
      "truncateLength": 3   
    }   
  }   
}
```

#### Attributes of Objects in the `sortFields` Array[​](#attributes-of-objects-in-the-sortfields-array "Direct link to attributes-of-objects-in-the-sortfields-array")

name String

Name of the field from the anchor dataset that is used for sorting in the Reflection.

Example: dropoff\_date

## Creating a Reflection[​](#creating-a-reflection "Direct link to Creating a Reflection")

Create a new Reflection.

Method and URL

```
POST /api/v3/reflection
```

### Parameters[​](#parameters "Direct link to Parameters")

type Body   String

Reflection type. For more information, read [Types of Reflections](/25.x/sonar/reflections/types-and-benefits).

Enum: RAW, AGGREGATION

Example: AGGREGATION

---

name Body   String

Name to use for the Reflection.

Example: New Aggregation Reflection

---

datasetId Body   String (UUID)

Unique identifier of the anchor dataset to associate with the Reflection.

Example: df99ab32-c2d4-4d1c-9e91-2c8be861bb8a

---

enabled Body   Boolean

If the Reflection should be available for accelerating queries, set to `true`. Otherwise, set to `false`.

Example: true

---

arrowCachingEnabled Body   Boolean   Optional

If Dremio should convert data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, set to `true`. Otherwise, set to `false` (default).

Example: false

---

[displayFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-displayfields-array) Body   Array of Object   Optional

Information about the fields to display from the anchor dataset. The displayfields array must list every field in the anchor dataset or the Reflection fails. Each displayFields object contains one attribute: name. Valid only for raw Reflections.

Example: [{"name": "pickup\_datetime"},{"name": "passenger\_count"},{"name": "trip\_distance\_mi"},{"name": "fare\_amount"},{"name": "tip\_amount"},{"name": "total\_amount"}]

---

[dimensionFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-dimensionfields-array) Body   Array of Object   Optional

Information about the dimension fields from the anchor dataset to use in the Reflection. Dimension fields are the fields you expect to group by when analyzing data. Each dimensionFields object contains two attributes: name and granularity. Valid only for aggregation Reflections.

Example: [{"name": "pickup\_datetime","granularity": "DATE"},{"name": "passenger\_count","granularity": "DATE"},{"name": "total\_amount","granularity": "DATE"},{"name": "trip\_distance\_mi","granularity": "DATE"}]

---

[measureFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-measurefields-array) Body   Array of Object   Optional

Information about the measure fields from the anchor dataset to use in the Reflection. Measure fields are the fields you expect to use for calculations when analyzing the data. Each measureFields object contains two attributes: name and measureTypeList. Valid only for aggregation Reflections.

Example: [{"name": "passenger\_count","measureTypeList": ["SUM", "COUNT"]},{"name": "trip\_distance\_mi","measureTypeList": ["SUM", "COUNT"]},{"name": "fare\_amount","measureTypeList": ["SUM", "COUNT"]},{"name": "tip\_amount","measureTypeList": ["SUM", "COUNT"]},{"name": "total\_amount","measureTypeList": ["SUM", "COUNT"]}]

---

[distributionFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-distributionfields-array) Body   Array of Object   Optional

Information about the distribution fields from the anchor dataset to use for co-locating and co-partitioning data from multiple datasets across nodes. Each distributionFields object contains one attribute: name.

Example: [{"name": "trip\_distance\_mi"},{"name": "total\_amount"}]

---

[partitionFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-partitionfields-array) Body   Array of Object   Optional

Information about the fields from the anchor dataset to use to partition data in the Reflection. Each field name is listed as an individual object. For more information, read [Horizontally Partition Reflections that Have Many Rows](/25.x/sonar/reflections/best-practices#horizontally-partition-reflections-that-have-many-rows).

Example: [{"name": "pickup\_datetime"},{"name": "passenger\_count"}]

---

[sortFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-sortfields-array) Body   Array of Object   Optional

Information about the fields from the anchor dataset to use for sorting in the Reflection. Each sortFields object contains one attribute: name. For more information, read [Sort Reflections on High-Cardinality Fields](/25.x/sonar/reflections/best-practices#sort-reflections-on-high-cardinality-fields).

Example: [{"name": "trip\_distance\_mi"}]

---

partitionDistributionStrategy Body   String   Optional

Method to use to optimize data compression when executing Reflections. If set to `CONSOLIDATED` (default), Dremio minimizes the number of files produced. If set to `STRIPED`, Dremio minimizes the time required to refresh the Reflection.

Enum: CONSOLIDATED, STRIPED

Example: CONSOLIDATED

---

canView Body   Boolean   Optional

To view Reflections on all datasets of a source, system, space, or folder, set to `true` (default). Otherwise, set to `false`.

Example: true

---

canAlter Body   Boolean   Optional

To create, edit, and view Reflections on all datasets of a source, system, space, or folder, set to `true` (default). Otherwise, set to `false`.

Example: true

---

entityType Body   String   Optional

Type of the object. For Reflection objects, the entityType is `reflection`.

Example: reflection

#### Parameters of Objects in the `displayFields` Array[​](#parameters-of-objects-in-the-displayfields-array "Direct link to parameters-of-objects-in-the-displayfields-array")

name Body   String

Name of the field to display from the anchor dataset.

Example: "name": "pickup\_datetime"

#### Parameters of Objects in the `dimensionFields` Array[​](#parameters-of-objects-in-the-dimensionfields-array "Direct link to parameters-of-objects-in-the-dimensionfields-array")

name Body   String

Name of the field from the anchor dataset to configure as a dimension for the Reflection.

Example: "name": "pickup\_datetime"

---

granularity Body   String

Grouping to use for the dimension field. If Dremio should automatically extract the day-level date value and use it as the grouping value in the Reflection, `DATE`. If Dremio should use the original value for grouping, `NORMAL`.

Enum: DATE, NORMAL

Example: "granularity": "DATE"

#### Parameters of Objects in the `measureFields` Array[​](#parameters-of-objects-in-the-measurefields-array "Direct link to parameters-of-objects-in-the-measurefields-array")

name Body   String

Name of the field from the anchor dataset that you expect to use in calculations. Fields of types `LIST`, `MAP`, and `UNION` are not valid measureFields.

Example: "name": "passenger\_count"

---

measureTypeList Body   Array of String

Name of the field from the anchor dataset to use for co-locating and co-partitioning data from multiple datasets across nodes. In aggregation Reflections, every field listed as a distribution field must also be listed as a dimension field.

Enum: APPROX\_COUNT\_DISTINCT, MIN, MAX, UNKNOWN, SUM, COUNT

Example: ["SUM", "COUNT"]

#### Parameters of Objects in the `distributionFields` Array[​](#parameters-of-objects-in-the-distributionfields-array "Direct link to parameters-of-objects-in-the-distributionfields-array")

name Body   String

Name of the field from the anchor dataset to use for co-locating and co-partitioning data from multiple datasets across nodes. In aggregation Reflections, every field listed as a distribution field must also be listed as a dimension field.

Example: "name": "trip\_distance\_mi"

#### Parameters of Objects in the `partitionFields` Array[​](#parameters-of-objects-in-the-partitionfields-array "Direct link to parameters-of-objects-in-the-partitionfields-array")

name Body   String

Name of the field from the anchor dataset on which you want to be able to partition rows. If you are creating an aggregation Reflection, every field listed as a partition field must also be listed as a dimension field. If you list a field as a partition field, you cannot list the same field as a sort field in the same Reflection.

Example: "name": "pickup\_datetime"

---

transform Object

The type of partition transform that is applied. The value is an enum. The types are:

**IDENTITY**: Creates one partition per value. This is the default transform. If no transform is specified for a field named by the `name` property, an IDENTITY transform is performed.

IDENTITY Example

```
{  
  "name": "passenger_count",  
  "transform": {  
    "type": "IDENTITY"  
  }  
}
```

**YEAR**: Partitions by year. The field must use the TIMESTAMP or DATE data type.

YEAR Example

```
{  
  "name": "pickup_datetime",  
  "transform": {  
    "type": "YEAR"  
  }  
}
```

**MONTH**: Partitions by month. The field must use the TIMESTAMP or DATE data type.

MONTH Example

```
{  
  "name": "pickup_datetime",  
  "transform": {  
    "type": "MONTH"  
  }  
}
```

**DAY**: Partitions on the equivalent of dateint. The field must use the TIMESTAMP or DATE data type.

DAY Example

```
{  
  "name": "pickup_datetime",  
  "transform": {   
    "type": "DAY"  
  }  
}
```

**HOUR**: Partitions on the equivalent of dateint and hour. The field must use the TIMESTAMP data type.

HOUR Example

```
{  
  "name": "pickup_datetime",  
  "transform": {   
    "type": "HOUR"  
  }  
}
```

**BUCKET**: Partitions data into the number of partitions specified by an integer. For example, if the integer value N is specified, the data is partitioned into N, or (0 to (N-1)), partitions. The partition in which an individual row is stored is determined by hashing the field value and then calculating `<hash_value> mod N`. If the result is 0, the row is placed in partition 0; if the result is 1, the row is placed in partition 1; and so on.

This value must be followed by a `bucketTransform` object. This object takes one property: `bucketCount`. This property takes an integer value.

BUCKET Example

```
{  
  "name": "pickup_datetime",   
  "transform": {  
    "type": "BUCKET",   
    "bucketTransform": {  
      "bucketCount": 1000  
    }  
  }  
}
```

**TRUNCATE**: If the specified field uses the string data type, truncates strings to a maximum of the number of characters specified by an integer. For example, suppose the specified transform is `truncate(1, stateUS)`. A value of `CA` is truncated to `C`, and the row is placed in partition C. A value of `CO` is also truncated to `C`, and the row is also placed in partition C.

If the specified field uses the integer or long data type, truncates field values in the following way: For any `truncate(L, col)`, truncates the field value to the biggest multiple of L that is smaller than the field value. For example, suppose the specified transform is `truncate(10, intField)`. A value of 1 is truncated to 0 and the row is placed in the partition 0. A value of 247 is truncated to 240 and the row is placed in partition 240. If the transform is `truncate(3, intField)`, a value of 13 is truncated to 12 and the row is placed in partition 12. A value of 255 is not truncated, because it is divisble by 3, and the row is placed in partition 255. This value must be followed by a `truncateTransform` object.

This object takes one property: `truncateLength`. This property takes an integer value.

note

The truncate transform does not change field values. It uses field values to calculate the correct partitions in which to place rows.

TRUNCATE Example

```
{   
  "name": "pickup_hour",   
  "transform": {   
    "type": "TRUNCATE",  
    "truncateTransform": {   
      "truncateLength": 3   
    }   
  }   
}
```

#### Parameters of Objects in the `sortFields` Array[​](#parameters-of-objects-in-the-sortfields-array "Direct link to parameters-of-objects-in-the-sortfields-array")

name Body   String

Name of the field from the anchor dataset to use for sorting in the Reflection. Every field listed as a sort field must also be listed as a dimension field. If you list a field as a sort field, you cannot list the same field as a partition field in the same Reflection.

Example: "name": "trip\_distance\_mi"

Example Request

```
curl -X POST 'https://{hostname}/api/v3/reflection/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "type": "AGGREGATION",  
  "name": "New Aggregation Reflection",  
  "datasetId": "gc870df7-ddf7-4d1e-bb9e-beef28ae773f",  
  "enabled": true,  
  "arrowCachingEnabled": false,  
  "dimensionFields": [  
    {  
      "name": "pickup_datetime",  
      "granularity": "DATE"  
    },  
    {  
      "name": "passenger_count"  
    },  
    {  
      "name": "total_amount"  
    },  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "measureFields": [  
    {  
      "name": "passenger_count",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "trip_distance_mi",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "fare_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "tip_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "total_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    }  
],  
  "distributionFields": [  
    {  
      "name": "trip_distance_mi"  
    },  
    {  
      "name": "total_amount"  
    }  
],  
  "partitionFields": [  
    {  
      "name": "pickup_datetime"  
    },  
    {  
      "name": "passenger_count"  
    }  
],  
  "sortFields": [  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "entityType": "reflection"  
}'
```

Example Response

```
{  
    "id": "836eae91-306e-487b-a687-31c999653a86",  
    "type": "AGGREGATION",  
    "name": "New Aggregation Reflection",  
    "tag": "sEHieiuinqE=",  
    "createdAt": "2023-01-30T14:30:24.311Z",  
    "updatedAt": "2023-01-30T14:30:24.311Z",  
    "datasetId": "gc870df7-ddf7-4d1e-bb9e-beef28ae773f",  
    "currentSizeBytes": 0,  
    "totalSizeBytes": 0,  
    "enabled": true,  
    "arrowCachingEnabled": false,  
    "status": {  
        "config": "OK",  
        "refresh": "SCHEDULED",  
        "availability": "NONE",  
        "combinedStatus": "CANNOT_ACCELERATE_SCHEDULED",  
        "failureCount": 0,  
        "lastDataFetch": "1969-12-31T23:59:59.999Z",  
        "expiresAt": "1969-12-31T23:59:59.999Z"  
    },  
    "dimensionFields": [  
        {  
            "name": "pickup_datetime",  
            "granularity": "DATE"  
        },  
        {  
            "name": "passenger_count"  
        },  
        {  
            "name": "total_amount"  
        },  
        {  
            "name": "trip_distance_mi"  
        }  
  ],  
    "measureFields": [  
        {  
            "name": "passenger_count",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "trip_distance_mi",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "fare_amount",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "tip_amount",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "total_amount",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        }  
  ],  
    "distributionFields": [  
        {  
            "name": "trip_distance_mi"  
        },  
        {  
            "name": "total_amount"  
        }  
  ],  
    "partitionFields": [  
        {  
            "name": "pickup_datetime"  
        },  
        {  
            "name": "passenger_count"  
        }  
  ],  
    "sortFields": [  
        {  
            "name": "trip_distance_mi"  
        }  
  ],  
    "partitionDistributionStrategy": "CONSOLIDATED",  
    "canView": true,  
    "canAlter": true,  
    "entityType": "reflection"  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

500   Internal Server Error

## Retrieving All Reflections Enterprise[​](#retrieving-all-reflections-enterprise "Direct link to retrieving-all-reflections-enterprise")

Retrieve a list of Reflection objects that includes all raw and aggregation Reflections in the Dremio instance.

Method and URL

```
GET /api/v3/reflection
```

Example Request

```
curl -X GET 'https://{hostname}/api/v3/reflection/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

In the response for a request to retrieve all raw and aggregation Reflections, the Reflection objects are wrapped with a data array. Each object in the data array represents one Reflection.

Example Response

```
{  
  "data": [  
    {  
      "id": "95dda9dd-2371-467f-b68d-fc4c5ea57a8b",  
      "type": "AGGREGATION",  
      "name": "Aggregation Reflection",  
      "tag": "ZpzGgxw2l04=",  
      "createdAt": "2022-07-05T19:19:40.244Z",  
      "updatedAt": "2023-01-10T17:12:40.244Z",  
      "datasetId": "df99ab32-c2d4-4d1c-9e91-2c8be861bb8a",  
      "currentSizeBytes": 18639885,  
      "totalSizeBytes": 142639924,  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "status": {  
        "config": "OK",  
        "refresh": "SCHEDULED",  
        "availability": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "failureCount": 0,  
        "lastDataFetch": "2023-01-10T17:12:40.244Z",  
        "expiresAt": "3022-07-05T19:19:40.244Z"  
      },  
      "dimensionFields": [  
        {  
          "name": "pickup_date"  
        },  
        {  
          "name": "pickup_datetime",  
          "granularity": "DATE"  
        },  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "dropoff_datetime",  
          "granularity": "DATE"  
        },  
        {  
          "name": "passenger_count"  
        },  
        {  
          "name": "total_amount"  
        },  
        {  
          "name": "trip_distance_mi"  
        }  
    ],  
      "measureFields": [  
        {  
          "name": "passenger_count",  
          "measureTypeList": [  
            "SUM",  
            "COUNT"  
        ]  
        },  
        {  
          "name": "trip_distance_mi",  
          "measureTypeList": [  
            "SUM",  
            "COUNT"  
        ]  
        },  
        {  
          "name": "fare_amount",  
          "measureTypeList": [  
            "SUM",  
            "COUNT"  
        ]  
        },  
        {  
          "name": "surcharge",  
          "measureTypeList": [  
            "SUM",  
            "COUNT"  
        ]  
        },  
        {  
          "name": "tip_amount",  
          "measureTypeList": [  
            "SUM",  
            "COUNT"  
        ]  
        },  
        {  
          "name": "total_amount",  
          "measureTypeList": [  
            "SUM",  
            "COUNT"  
        ]  
        }  
    ],  
      "distributionFields": [  
        {  
          "name": "trip_distance_mi"  
        },  
        {  
          "name": "total_amount"  
        }  
    ],  
      "partitionFields": [  
        {  
          "name": "dropoff_date"  
        },  
        {  
          "name": "passenger_count"  
        }  
    ],  
      "sortFields": [  
        {  
          "name": "trip_distance_mi"  
        }  
    ],  
      "partitionDistributionStrategy": "CONSOLIDATED",  
      "canView": true,  
      "canAlter": true,  
      "entityType": "reflection"  
    },  
    {  
      "id": "14f22052-cbb3-4d5d-8bbc-6154cca98e49",  
      "type": "RAW",  
      "name": "listings",  
      "tag": "XAy4ccVFXO4=",  
      "createdAt": "2022-07-12T16:45:35.249Z",  
      "updatedAt": "2022-07-12T16:45:35.249Z",  
      "datasetId": "7707981c-cb33-42bc-a048-d27a8915f468",  
      "currentSizeBytes": 0,  
      "totalSizeBytes": 0,  
      "enabled": true,  
      "arrowCachingEnabled": true,  
      "status": {  
        "config": "OK",  
        "refresh": "MANUAL",  
        "availability": "NONE",  
        "combinedStatus": "CANNOT_ACCELERATE_MANUAL",  
        "failureCount": 0,  
        "lastDataFetch": "1969-12-31T23:59:59.999Z",  
        "expiresAt": "1969-12-31T23:59:59.999Z"  
      },  
      "displayFields": [  
        {  
          "name": "id"  
        }  
    ],  
      "partitionDistributionStrategy": "CONSOLIDATED",  
      "canView": true,  
      "canAlter": true,  
      "entityType": "reflection"  
    },  
    {  
      "id": "6c209200-b522-4f81-bbe0-d10668c7752c",  
      "type": "AGGREGATION",  
      "name": "Aggregation Reflection",  
      "tag": "SQeEAG3d6DA=",  
      "createdAt": "2021-09-29T15:47:44.806Z",  
      "updatedAt": "2021-09-29T15:47:44.806Z",  
      "datasetId": "746f867a-c27c-4711-bb8c-99546a4c25e0",  
      "currentSizeBytes": 0,  
      "totalSizeBytes": 1675978,  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "status": {  
        "config": "OK",  
        "refresh": "GIVEN_UP",  
        "availability": "NONE",  
        "combinedStatus": "FAILED",  
        "failureCount": 3,  
        "lastDataFetch": "1969-12-31T23:59:59.999Z",  
        "expiresAt": "1969-12-31T23:59:59.999Z"  
      },  
      "dimensionFields": [  
        {  
          "name": "passenger_count"  
        },  
        {  
          "name": "pickup_datetime",  
          "granularity": "DATE"  
        }  
    ],  
      "measureFields": [  
        {  
          "name": "trip_distance_mi",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "total_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "tip_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "fare_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        }  
    ],  
      "partitionDistributionStrategy": "CONSOLIDATED",  
      "canView": true,  
      "canAlter": true,  
      "entityType": "reflection"  
    },  
    {  
      "id": "c5c5b282-ffea-4a34-835f-cc591584412b",  
      "type": "AGGREGATION",  
      "name": "Test Reflection",  
      "tag": "lMxFcc2qjgE=",  
      "createdAt": "2021-10-11T18:44:27.064Z",  
      "updatedAt": "2021-10-11T18:44:27.064Z",  
      "datasetId": "316531b8-3c56-42f2-b05f-81f228ef3162",  
      "currentSizeBytes": 0,  
      "totalSizeBytes": 0,  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "status": {  
        "config": "OK",  
        "refresh": "MANUAL",  
        "availability": "NONE",  
        "combinedStatus": "CANNOT_ACCELERATE_MANUAL",  
        "failureCount": 0,  
        "lastDataFetch": "1969-12-31T23:59:59.999Z",  
        "expiresAt": "1969-12-31T23:59:59.999Z"  
      },  
      "dimensionFields": [  
        {  
          "name": "passenger_count"  
        }  
    ],  
      "measureFields": [  
        {  
          "name": "trip_distance_mi",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "total_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "tip_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "fare_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        }  
    ],  
      "partitionDistributionStrategy": "CONSOLIDATED",  
      "canView": true,  
      "canAlter": true,  
      "entityType": "reflection"  
    }  
],  
  "canAlterReflections": true  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

500   Internal Server Error

## Retrieving a Reflection[​](#retrieving-a-reflection "Direct link to Retrieving a Reflection")

Retrieve the specified Reflection.

Method and URL

```
GET /api/v3/reflection/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the Reflection that you want to retrieve.

Example: 95dda9dd-2371-467f-b68d-fc4c5ea57a8b

Example Request

```
curl -X GET 'https://{hostname}/api/v3/reflection/95dda9dd-2371-467f-b68d-fc4c5ea57a8b'  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "95dda9dd-2371-467f-b68d-fc4c5ea57a8b",  
  "type": "AGGREGATION",  
  "name": "Aggregation Reflection",  
  "tag": "ZpzGgxw2l04=",  
  "createdAt": "2022-07-05T19:19:40.244Z",  
  "updatedAt": "2023-01-10T17:12:40.244Z",  
  "datasetId": "df99ab32-c2d4-4d1c-9e91-2c8be861bb8a",  
  "currentSizeBytes": 18639885,  
  "totalSizeBytes": 142639924,  
  "enabled": true,  
  "arrowCachingEnabled": false,  
  "status": {  
    "config": "OK",  
    "refresh": "SCHEDULED",  
    "availability": "AVAILABLE",  
    "combinedStatus": "CAN_ACCELERATE",  
    "failureCount": 0,  
    "lastDataFetch": "2023-01-10T17:12:40.244Z",  
    "expiresAt": "3022-07-05T19:19:40.244Z"  
  },  
  "dimensionFields": [  
    {  
      "name": "pickup_date"  
    },  
    {  
      "name": "pickup_datetime",  
      "granularity": "DATE"  
    },  
    {  
      "name": "dropoff_date"  
    },  
    {  
      "name": "dropoff_datetime",  
      "granularity": "DATE"  
    },  
    {  
      "name": "passenger_count"  
    },  
    {  
      "name": "total_amount"  
    },  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "measureFields": [  
    {  
      "name": "passenger_count",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "trip_distance_mi",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "fare_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "surcharge",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "tip_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "total_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    }  
],  
  "distributionFields": [  
    {  
      "name": "trip_distance_mi"  
    },  
    {  
      "name": "total_amount"  
    }  
],  
  "partitionFields": [  
    {  
      "name": "dropoff_date"  
    },  
    {  
      "name": "passenger_count"  
    }  
],  
  "sortFields": [  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "partitionDistributionStrategy": "CONSOLIDATED",  
  "canView": true,  
  "canAlter": true,  
  "entityType": "reflection"  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

500   Internal Server Error

## Retrieving All Reflections for a Dataset[​](#retrieving-all-reflections-for-a-dataset "Direct link to Retrieving All Reflections for a Dataset")

Retrieve all raw and aggregation Reflections for the specified dataset.

Method and URL

```
GET /api/v3/dataset/{datasetId}/reflection
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

datasetId Path   String (UUID)

Unique identifier of the dataset whose Reflections you want to retrieve.

Example: 3cbab7b3-ee82-44c1-abcc-e86d56078d4d

Example Request

```
curl -X GET 'https://{hostname}/api/v3/dataset/3cbab7b3-ee82-44c1-abcc-e86d56078d4d/reflection'  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

In the response for a request to retrieve all Reflections for a dataset, the Reflection objects are wrapped with a data array. Each object in the data array represents one Reflection.

Example Response

```
{  
  "data": [  
    {  
      "id": "23f75eb1-045f-447f-b3fa-374377877569",  
      "type": "RAW",  
      "name": "Raw Reflection",  
      "tag": "K9J2SHE0c+Q=",  
      "createdAt": "2023-02-03T16:38:27.770Z",  
      "updatedAt": "2023-02-03T16:38:27.770Z",  
      "datasetId": "3cbab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "currentSizeBytes": 0,  
      "totalSizeBytes": 0,  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "status": {  
        "config": "OK",  
        "refresh": "MANUAL",  
        "availability": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "failureCount": 0,  
        "lastDataFetch": "2023-02-03T16:38:27.780Z",  
        "expiresAt": "3022-06-06T16:38:27.780Z"  
      },  
      "displayFields": [  
        {  
          "name": "pickup_datetime"  
        },  
        {  
          "name": "passenger_count"  
        },  
        {  
          "name": "trip_distance_mi"  
        },  
        {  
          "name": "fare_amount"  
        },  
        {  
          "name": "tip_amount"  
        },  
        {  
          "name": "total_amount"  
        }  
    ],  
      "partitionDistributionStrategy": "CONSOLIDATED",  
      "canView": true,  
      "canAlter": true,  
      "entityType": "reflection"  
    },  
    {  
      "id": "3cbab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "type": "AGGREGATION",  
      "name": "Aggregation Reflection",  
      "tag": "Mc4hDFk5JR8=",  
      "createdAt": "2023-02-03T16:39:40.556Z",  
      "updatedAt": "2023-02-03T16:39:40.556Z",  
      "datasetId": "1acab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "currentSizeBytes": 0,  
      "totalSizeBytes": 0,  
      "enabled": true,  
      "arrowCachingEnabled": false,  
      "status": {  
        "config": "OK",  
        "refresh": "MANUAL",  
        "availability": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "failureCount": 0,  
        "lastDataFetch": "2023-02-03T16:39:40.568Z",  
        "expiresAt": "3022-06-06T16:39:40.568Z"  
      },  
      "dimensionFields": [  
        {  
          "name": "passenger_count"  
        },  
        {  
          "name": "pickup_datetime",  
          "granularity": "DATE"  
        }  
    ],  
      "measureFields": [  
        {  
          "name": "trip_distance_mi",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "total_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "tip_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        },  
        {  
          "name": "fare_amount",  
          "measureTypeList": [  
            "COUNT",  
            "SUM"  
        ]  
        }  
    ],  
      "partitionDistributionStrategy": "CONSOLIDATED",  
      "canView": true,  
      "canAlter": true,  
      "entityType": "reflection"  
    }  
],  
  "canAlterReflections": true  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

500   Internal Server Error

## Refreshing a Reflection[​](#refreshing-a-reflection "Direct link to Refreshing a Reflection")

For information about the refresh action performed, see [Triggering Refreshes by Using the Reflection API, the Catalog API, or an SQL Command](/25.x/sonar/reflections/refreshing-reflections).

Method and URL

```
POST /api/v3/reflection/{id}/refresh
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier for the Reflection that you want to base the refresh action on.

Example: 836eae91-306e-487b-a687-31c999653a86

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

200   OK

400   Not supported

401   Unauthorized

404   Not Found

405   Method Not Allowed

500   Internal Server Error

## Updating a Reflection[​](#updating-a-reflection "Direct link to Updating a Reflection")

Update the specified Reflection.

Method and URL

```
PUT /api/v3/reflection/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the Reflection that you want to update.

Example: 836eae91-306e-487b-a687-31c999653a86

---

type Body   String

Reflection type. For more information, read [Types of Reflections](/25.x/sonar/reflections/types-and-benefits).

Enum: RAW, AGGREGATION

Example: AGGREGATION

---

name Body   String

Name to use for the Reflection.

Example: New Aggregation Reflection

---

tag Body   String

Unique identifier of the most recent version of the Reflection. Dremio uses the tag to ensure that you are updating the most recent version of the Reflection.

Example: ZpzGgxw2l04=

---

datasetId Body   String (UUID)

Unique identifier of the anchor dataset associated with the Reflection.

Example: gc870df7-ddf7-4d1e-bb9e-beef28ae773f

---

enabled Body   Boolean

If the Reflection should be available for accelerating queries, set to `true`. Otherwise, set to `false`.

Example: false

---

arrowCachingEnabled Body   Boolean   Optional

If Dremio should convert data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, set to `true`. Otherwise, set to `false` (default).

Example: true

---

[displayFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-displayfields-array-1) Body   Array of Object

Information about the fields to display from the anchor dataset. The displayfields array must list every field in the anchor dataset or the Reflection fails. Each displayFields object contains one attribute: name. Valid only for raw Reflections.

Example: [{"name": "pickup\_datetime"},{"name": "passenger\_count"},{"name": "trip\_distance\_mi"},{"name": "fare\_amount"},{"name": "tip\_amount"},{"name": "total\_amount"}]

---

[dimensionFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-dimensionfields-array-1) Body   Array of Object

Information about the dimension fields from the anchor dataset to use in the Reflection. Dimension fields are the fields you expect to group by when analyzing data. Each dimensionFields object contains two attributes: name and granularity. Valid only for aggregation Reflections. If you omit the dimensionFields object in a PUT request, Dremio removes all existing dimension fields from the Reflection. To keep existing dimension fields while making other updates, duplicate the existing dimensionFields array in the PUT request.

Example: [{"name": "pickup\_datetime","granularity": "DATE"},{"name": "passenger\_count","granularity": "DATE"},{"name": "total\_amount","granularity": "DATE"},{"name": "trip\_distance\_mi","granularity": "DATE"}]

---

[measureFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-measurefields-array-1) Body   Array of Object

Information about the measure fields from the anchor dataset to use in the Reflection. Measure fields are the fields you expect to use for calculations when analyzing the data. Each measureFields object contains two attributes: name and measureTypeList. Valid only for aggregation Reflections. If you omit the measureFields object in a PUT request, Dremio removes all existing measure fields from the Reflection. To keep existing measure fields while making other updates, duplicate the existing measureFields array in the PUT request.

Example: [{"name": "passenger\_count","measureTypeList": ["SUM", "COUNT"]},{"name": "trip\_distance\_mi","measureTypeList": ["SUM", "COUNT"]},{"name": "fare\_amount","measureTypeList": ["SUM", "COUNT"]},{"name": "tip\_amount","measureTypeList": ["SUM", "COUNT"]},{"name": "total\_amount","measureTypeList": ["SUM", "COUNT"]}]

---

[distributionFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-distributionfields-array-1) Body   Array of Object   Optional

Information about the distribution fields from the anchor dataset to use for co-locating and co-partitioning data from multiple datasets across nodes. Each distributionFields object contains one attribute: name.  
If you omit the distributionFields object in a PUT request, Dremio removes all existing distribution fields from the Reflection. To keep existing distribution fields while making other updates, duplicate the existing distributionFields array in the PUT request.

Example: [{"name": "trip\_distance\_mi"},{"name": "total\_amount"}]

---

[partitionFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-partitionfields-array-1) Body   Array of Object   Optional

Information about the fields from the anchor dataset to use to partition data in the Reflection. Each field name is listed as an individual object. If you omit the partitionFields object in a PUT request, Dremio removes all existing partition fields from the Reflection. To keep existing partition fields while making other updates, duplicate the existing partitionFields array in the PUT request. For more information, read [Horizontally Partition Reflections that Have Many Rows](/25.x/sonar/reflections/best-practices#horizontally-partition-reflections-that-have-many-rows).

Example: [{"name": "pickup\_datetime"},{"name": "passenger\_count"}]

---

[sortFields](/25.x/reference/api/reflections/#parameters-of-objects-in-the-sortfields-array-1) Body   Array of Object

Information about the fields from the anchor dataset to use for sorting in the Reflection. Each sortFields object contains one attribute: name. If you omit the sortFields object in a PUT request, Dremio removes all existing sort fields from the Reflection. To keep existing sort fields while making other updates, duplicate the existing sortFields array in the PUT request. For more information, read [Sort Reflections on High-Cardinality Fields](/25.x/sonar/reflections/best-practices#sort-reflections-on-high-cardinality-fields).

Example: "name": "trip\_distance\_mi"

---

partitionDistributionStrategy Body   String   Optional

Method to use to optimize data compression when executing Reflections. If set to `CONSOLIDATED` (default), Dremio minimizes the number of files produced. If set to `STRIPED`, Dremio minimizes the time required to refresh the Reflection.

Enum: CONSOLIDATED, STRIPED

Example: CONSOLIDATED

#### Parameters of Objects in the `displayFields` Array[​](#parameters-of-objects-in-the-displayfields-array-1 "Direct link to parameters-of-objects-in-the-displayfields-array-1")

name Body   String

Name of the field to display from the anchor dataset.

Example: "name": "pickup\_datetime"

#### Parameters of Objects in the `dimensionFields` Array[​](#parameters-of-objects-in-the-dimensionfields-array-1 "Direct link to parameters-of-objects-in-the-dimensionfields-array-1")

name Body   String

Name of the field from the anchor dataset to configure as a dimension for the Reflection.

Example: "name": "pickup\_datetime"

---

granularity Body   String

Grouping to use for the dimension field. If Dremio should automatically extract the day-level date value and use it as the grouping value in the Reflection, `DATE`. If Dremio should use the original value for grouping, `NORMAL`.

Enum: DATE, NORMAL

Example: "granularity": "DATE"

#### Parameters of Objects in the `measureFields` Array[​](#parameters-of-objects-in-the-measurefields-array-1 "Direct link to parameters-of-objects-in-the-measurefields-array-1")

name Body   String

Name of the field from the anchor dataset that you expect to use in calculations. Fields of types `LIST`, `MAP`, and `UNION` are not valid measureFields.

Example: "name": "passenger\_count"

---

measureTypeList Body   Array of String

Name of the field from the anchor dataset to use for co-locating and co-partitioning data from multiple datasets across nodes. Every field listed as a distribution field must also be listed as a dimension field.

Enum: APPROX\_COUNT\_DISTINCT, MIN, MAX, UNKNOWN, SUM, COUNT

Example: ["SUM", "COUNT"]

#### Parameters of Objects in the `distributionFields` Array[​](#parameters-of-objects-in-the-distributionfields-array-1 "Direct link to parameters-of-objects-in-the-distributionfields-array-1")

name Body   String

Name of the field from the anchor dataset to use for co-locating and co-partitioning data from multiple datasets across nodes. In aggregation Reflections, every field listed as a distribution field must also be listed as a dimension field.

Example: "name": "pickup\_datetime"

#### Parameters of Objects in the `partitionFields` Array[​](#parameters-of-objects-in-the-partitionfields-array-1 "Direct link to parameters-of-objects-in-the-partitionfields-array-1")

name Body   String

Name of the field from the anchor dataset on which the rows in the Reflection are to be partitioned. If a column is listed as a partition column, it cannot also be listed as a sort column for the same Reflection. In aggregation Reflections, each column specified as a partition column or used in transform must also be listed as a dimension column. In raw Reflections, each column specified as a partition column or used in transform must also be listed as a display column.

Example: "name": "dropoff\_date"

---

transform Object

The type of partition transform that is applied. The value is an enum. The types are:

**IDENTITY**: Creates one partition per value. This is the default transform. If no transform is specified for a field named by the `name` property, an IDENTITY transform is performed.

IDENTITY Example

```
{  
  "name": "passenger_count",  
  "transform": {  
    "type": "IDENTITY"  
  }  
}
```

**YEAR**: Partitions by year. The field must use the TIMESTAMP or DATE data type.

YEAR Example

```
{  
  "name": "pickup_datetime",  
  "transform": {  
    "type": "YEAR"  
  }  
}
```

**MONTH**: Partitions by month. The field must use the TIMESTAMP or DATE data type.

MONTH Example

```
{  
  "name": "pickup_datetime",  
  "transform": {  
    "type": "MONTH"  
  }  
}
```

**DAY**: Partitions on the equivalent of dateint. The field must use the TIMESTAMP or DATE data type.

DAY Example

```
{  
  "name": "pickup_datetime",  
  "transform": {   
    "type": "DAY"  
  }  
}
```

**HOUR**: Partitions on the equivalent of dateint and hour. The field must use the TIMESTAMP data type.

HOUR Example

```
{  
  "name": "pickup_datetime",  
  "transform": {   
    "type": "HOUR"  
  }  
}
```

**BUCKET**: Partitions data into the number of partitions specified by an integer. For example, if the integer value N is specified, the data is partitioned into N, or (0 to (N-1)), partitions. The partition in which an individual row is stored is determined by hashing the field value and then calculating `<hash_value> mod N`. If the result is 0, the row is placed in partition 0; if the result is 1, the row is placed in partition 1; and so on.

This value must be followed by a `bucketTransform` object. This object takes one property: `bucketCount`. This property takes an integer value.

BUCKET Example

```
{  
  "name": "pickup_datetime",   
  "transform": {  
    "type": "BUCKET",   
    "bucketTransform": {  
      "bucketCount": 1000  
    }  
  }  
}
```

**TRUNCATE**: If the specified field uses the string data type, truncates strings to a maximum of the number of characters specified by an integer. For example, suppose the specified transform is `truncate(1, stateUS)`. A value of `CA` is truncated to `C`, and the row is placed in partition C. A value of `CO` is also truncated to `C`, and the row is also placed in partition C.

If the specified field uses the integer or long data type, truncates field values in the following way: For any `truncate(L, col)`, truncates the field value to the biggest multiple of L that is smaller than the field value. For example, suppose the specified transform is `truncate(10, intField)`. A value of 1 is truncated to 0 and the row is placed in the partition 0. A value of 247 is truncated to 240 and the row is placed in partition 240. If the transform is `truncate(3, intField)`, a value of 13 is truncated to 12 and the row is placed in partition 12. A value of 255 is not truncated, because it is divisble by 3, and the row is placed in partition 255. This value must be followed by a `truncateTransform` object.

This object takes one property: `truncateLength`. This property takes an integer value.

note

The truncate transform does not change field values. It uses field values to calculate the correct partitions in which to place rows.

TRUNCATE Example

```
{   
  "name": "pickup_hour",   
  "transform": {   
    "type": "TRUNCATE",  
    "truncateTransform": {   
      "truncateLength": 3   
    }   
  }   
}
```

#### Parameters of Objects in the `sortFields` Array[​](#parameters-of-objects-in-the-sortfields-array-1 "Direct link to parameters-of-objects-in-the-sortfields-array-1")

name Body   String

Name of the field from the anchor dataset to use for sorting in the Reflection. Every field listed as a sort field must also be listed as a dimension field. If you list a field as a sort field, you cannot list the same field as a partition field in the same Reflection.

Example: "name": "pickup\_datetime"

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/reflection/836eae91-306e-487b-a687-31c999653a86' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "id": "836eae91-306e-487b-a687-31c999653a86",  
  "type": "AGGREGATION",  
  "name": "New Aggregation Reflection",  
  "tag": "sEHieiuinqE=",  
  "datasetId": "gc870df7-ddf7-4d1e-bb9e-beef28ae773f",  
  "enabled": false,  
  "arrowCachingEnabled": true,  
  "dimensionFields": [  
    {  
      "name": "pickup_datetime",  
      "granularity": "DATE"  
    },  
    {  
      "name": "passenger_count"  
    },  
    {  
      "name": "total_amount"  
    },  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "measureFields": [  
    {  
      "name": "passenger_count",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "trip_distance_mi",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "fare_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "tip_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    },  
    {  
      "name": "total_amount",  
      "measureTypeList": [  
        "SUM",  
        "COUNT"  
    ]  
    }  
],  
  "distributionFields": [  
    {  
      "name": "trip_distance_mi"  
    },  
    {  
      "name": "total_amount"  
    }  
],  
  "partitionFields": [  
    {  
      "name": "pickup_datetime"  
    },  
    {  
      "name": "passenger_count"  
    }  
],  
  "sortFields": [  
    {  
      "name": "trip_distance_mi"  
    }  
],  
  "entityType": "reflection"  
}'
```

Example Response

```
{  
    "id": "836eae91-306e-487b-a687-31c999653a86",  
    "type": "AGGREGATION",  
    "name": "New Aggregation Reflection",  
    "tag": "nRPbilwodqC=",  
    "createdAt": "2023-01-30T14:35:19.192Z",  
    "updatedAt": "2023-01-30T14:35:19.192Z",  
    "datasetId": "gc870df7-ddf7-4d1e-bb9e-beef28ae773f",  
    "currentSizeBytes": 0,  
    "totalSizeBytes": 0,  
    "enabled": false,  
    "arrowCachingEnabled": true,  
    "status": {  
        "config": "OK",  
        "refresh": "SCHEDULED",  
        "availability": "NONE",  
        "combinedStatus": "DISABLED",  
        "failureCount": 0,  
        "lastDataFetch": "1969-12-31T23:59:59.999Z",  
        "expiresAt": "1969-12-31T23:59:59.999Z"  
    },  
    "dimensionFields": [  
        {  
            "name": "pickup_datetime",  
            "granularity": "DATE"  
        },  
        {  
            "name": "passenger_count"  
        },  
        {  
            "name": "total_amount"  
        },  
        {  
            "name": "trip_distance_mi"  
        }  
  ],  
    "measureFields": [  
        {  
            "name": "passenger_count",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "trip_distance_mi",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "fare_amount",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "tip_amount",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        },  
        {  
            "name": "total_amount",  
            "measureTypeList": [  
                "SUM",  
                "COUNT"  
          ]  
        }  
  ],  
    "distributionFields": [  
        {  
            "name": "trip_distance_mi"  
        },  
        {  
            "name": "total_amount"  
        }  
  ],  
    "partitionFields": [  
        {  
            "name": "pickup_datetime"  
        },  
        {  
            "name": "passenger_count"  
        }  
  ],  
    "sortFields": [  
        {  
            "name": "trip_distance_mi"  
        }  
  ],  
    "partitionDistributionStrategy": "CONSOLIDATED",  
    "canView": true,  
    "canAlter": true,  
    "entityType": "reflection"  
}
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

409   Conflict

500   Internal Server Error

## Deleting a Reflection[​](#deleting-a-reflection "Direct link to Deleting a Reflection")

Delete the specified Reflection.

Method and URL

```
DELETE /api/v3/reflection/{id}
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the Reflection that you want to delete.

Example: 95dda9dd-2371-467f-b68d-fc4c5ea57a8b

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/reflection/95dda9dd-2371-467f-b68d-fc4c5ea57a8b'  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type:application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-6 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Node Collections](/25.x/reference/api/nodeCollections/)[Next

Recommendations](/25.x/reference/api/reflections/reflection-recommendations)

* [Reflection Attributes](#reflection-attributes)
* [Creating a Reflection](#creating-a-reflection)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving All Reflections Enterprise](#retrieving-all-reflections-enterprise)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Reflection](#retrieving-a-reflection)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-2)
* [Retrieving All Reflections for a Dataset](#retrieving-all-reflections-for-a-dataset)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-3)
* [Refreshing a Reflection](#refreshing-a-reflection)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-4)
* [Updating a Reflection](#updating-a-reflection)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-5)
* [Deleting a Reflection](#deleting-a-reflection)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-6)

---

# Source: https://docs.dremio.com/25.x/reference/api/roles/

Version: 25.x

On this page

# Role Enterprise

Use the Role API to manage [roles](/25.x/security/rbac/roles/).

Role Object

```
{  
  "id": "957a8af5-9211-4bc5-9fe5-1a44ff30304d",  
  "name": "Temporary Testing",  
  "type": "INTERNAL",  
  "roles": [  
    {  
      "id": "6f87a9c5-d733-4935-8331-875a4a8e09d7",  
      "name": "qa_team1",  
      "type": "INTERNAL"  
    },  
    {  
      "id": "f8426061-8413-46ec-a84d-1b481a97b248",  
      "name": "prod_testing",  
      "type": "INTERNAL"  
    }  
  ],  
  "memberCount": 3,  
  "description": "Role for testing the new feature"  
}
```

## Role Attributes[​](#role-attributes "Direct link to Role Attributes")

id String (UUID)

Unique identifier of the role.

Example: 957a8af5-9211-4bc5-9fe5-1a44ff30304d

---

name String

User-provided name of the role.

Example: Temporary Testing

---

type String

Origin of the role.

* `INTERNAL`: Role was created in the Dremio user interface (UI) or with the Role API.
* `EXTERNAL`: Role was imported from an external service like Microsoft Entra ID, Lightweight Directory Access Protocol (LDAP), or a System for Cross-domain Identity Management (SCIM) provider.
* `SYSTEM`: Role was predefined in Dremio.

Example: INTERNAL

---

[roles](/25.x/reference/api/roles/#attributes-of-objects-in-the-roles-array) Array of Object

Information about the roles to which the role belongs.

Example: [{"id": "6f87a9c5-d733-4935-8331-875a4a8e09d7","name": "SELECT and CREATE","type": "INTERNAL"},{"id": "f8426061-8413-46ec-a84d-1b481a97b248","name": "VIEW","type": "INTERNAL"}]

---

memberCount Integer

Number of users and roles that are members of the role.

Example: 3

---

description String

User-provided description of the role.

Example: Role for testing the new feature

#### Attributes of Objects in the `roles` Array[​](#attributes-of-objects-in-the-roles-array "Direct link to attributes-of-objects-in-the-roles-array")

id String (UUID)

Unique identifier of the role.

Example: 6f87a9c5-d733-4935-8331-875a4a8e09d7

---

name String

Name of the role.

Example: SELECT and CREATE

---

type String

Origin of the role.

* `INTERNAL`: Role was created in the Dremio user interface (UI) or with the Role API.
* `EXTERNAL`: Role was imported from an external service like Microsoft Entra ID, Lightweight Directory Access Protocol (LDAP), or a System for Cross-domain Identity Management (SCIM) provider.
* `SYSTEM`: Role was predefined in Dremio.

Example: INTERNAL

## Creating a Role[​](#creating-a-role "Direct link to Creating a Role")

Create a Dremio role.

Method and URL

```
POST /api/v3/role
```

### Parameters[​](#parameters "Direct link to Parameters")

name Body   String

Name for the role. The role name must be unique and cannot be updated after the role is created.

Example: Temporary Testing

---

[roles](/25.x/reference/api/roles/#parameters-of-objects-in-the-roles-array) Body   Array of Object   Optional

Information about the roles to which the role should be assigned.

Example: [{"id": "6f87a9c5-d733-4935-8331-875a4a8e09d7"},{"id": "f8426061-8413-46ec-a84d-1b481a97b248"}]

---

description Body   String   Optional

Description for the role.

Example: Role for testing the new feature

#### Parameters of Objects in the `roles` Array[​](#parameters-of-objects-in-the-roles-array "Direct link to parameters-of-objects-in-the-roles-array")

id Body   String (UUID)

Unique identifier of the role to which the role you create should be assigned.

Example: 6f87a9c5-d733-4935-8331-875a4a8e09d7

---

name Body   String   Optional

Name of the role to which the role you create should be assigned.

Example: qa\_team1

Example Request

```
curl -X POST 'https://{hostname}/api/v3/role' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "Temporary Testing",  
  "roles": [  
    {  
      "id": "6f87a9c5-d733-4935-8331-875a4a8e09d7"  
    },  
    {  
      "id": "f8426061-8413-46ec-a84d-1b481a97b248"  
    }  
  ],  
  "description": "Role for testing the new feature"  
}'
```

Example Response

```
{  
  "id": "957a8af5-9211-4bc5-9fe5-1a44ff30304d",  
  "name": "Temporary Testing",  
  "type": "INTERNAL",  
  "roles": [  
    {  
      "id": "6f87a9c5-d733-4935-8331-875a4a8e09d7",  
      "name": "qa_team1",  
      "type": "INTERNAL"  
    },  
    {  
      "id": "f8426061-8413-46ec-a84d-1b481a97b248",  
      "name": "prod_testing",  
      "type": "INTERNAL"  
    }  
  ],  
  "memberCount": 0,  
  "description": "Role for testing the new feature"  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

404   Not Found

405   Method Not Allowed

## Retrieving a Role by ID[​](#retrieving-a-role-by-id "Direct link to Retrieving a Role by ID")

Retrieve a specific role by the role's ID.

Method and URL

```
GET /api/v3/role/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the role you want to retrieve.

Example: 957a8af5-9211-4bc5-9fe5-1a44ff30304d

Example Request

```
curl -X GET 'https://{hostname}/api/v3/role/957a8af5-9211-4bc5-9fe5-1a44ff30304d' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "957a8af5-9211-4bc5-9fe5-1a44ff30304d",  
  "name": "Temporary Testing",  
  "type": "INTERNAL",  
  "roles": [  
    {  
      "id": "6f87a9c5-d733-4935-8331-875a4a8e09d7",  
      "name": "qa_team1",  
      "type": "INTERNAL"  
    },  
    {  
      "id": "f8426061-8413-46ec-a84d-1b481a97b248",  
      "name": "prod_testing",  
      "type": "INTERNAL"  
    }  
  ],  
  "memberCount": 3,  
  "description": "Role for testing the new feature"  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

500   Internal Server Error

## Retrieving a Role by Name[​](#retrieving-a-role-by-name "Direct link to Retrieving a Role by Name")

Retrieve a specific role by the role's name.

Method and URL

```
GET /api/v3/role/by-name/{name}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

name Path   String

Name of the role you want to retrieve. The role name is case-insensitive. If the role name includes special characters for a URL, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: Temporary%20Testing

Example Request

```
curl -X GET 'https://{hostname}/api/v3/role/by-name/Temporary%20Testing' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "957a8af5-9211-4bc5-9fe5-1a44ff30304d",  
  "name": "Temporary Testing",  
  "type": "INTERNAL",  
  "roles": [  
    {  
      "id": "6f87a9c5-d733-4935-8331-875a4a8e09d7",  
      "name": "qa_team1",  
      "type": "INTERNAL"  
    },  
    {  
      "id": "f8426061-8413-46ec-a84d-1b481a97b248",  
      "name": "prod_testing",  
      "type": "INTERNAL"  
    }  
  ],  
  "memberCount": 3,  
  "description": "Role for testing the new feature"  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

500   Internal Server Error

## Updating a Role[​](#updating-a-role "Direct link to Updating a Role")

Update the specified role.

Method and URL

```
PUT /api/v3/role/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the role you want to update.

Example: 957a8af5-9211-4bc5-9fe5-1a44ff30304d

---

id Body   String (UUID)

Unique identifier of the role you want to update.

Example: 957a8af5-9211-4bc5-9fe5-1a44ff30304d

---

name Body   String

Name of the role.

Example: Temporary Testing

---

[roles](/25.x/reference/api/roles/#parameters-of-objects-in-the-roles-array-1) Body   Array of Object   Optional

Information about the roles to which the role should be assigned. If you omit an existing role in a PUT request, Dremio removes the role. To keep all existing roles while making other updates, include all existing roles in the PUT request.

Example: [{"id": "f8426061-8413-46ec-a84d-1b481a97b248"}]

---

description Body   String   Optional

Description to use for the role. If you omit the description in a PUT request, Dremio removes the existing description. To keep the existing description while making other updates, include the description in the PUT request.

Example: Role for viewing the new feature

#### Parameters of Objects in the `roles` Array[​](#parameters-of-objects-in-the-roles-array-1 "Direct link to parameters-of-objects-in-the-roles-array-1")

id Body   String (UUID)

Unique identifier of the role to which the role you update should be assigned.

Example: f8426061-8413-46ec-a84d-1b481a97b248

---

name Body   String   Optional

Name of the role to which the role you update should be assigned.

Example: prod\_testing

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/role/957a8af5-9211-4bc5-9fe5-1a44ff30304d' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "id": "957a8af5-9211-4bc5-9fe5-1a44ff30304d",  
  "name": "Temporary Testing",  
  "roles": [  
    {  
      "id": "f8426061-8413-46ec-a84d-1b481a97b248"  
    }  
  ],  
  "description": "Role for viewing the new feature"  
}'
```

Example Response

```
{  
  "id": "957a8af5-9211-4bc5-9fe5-1a44ff30304d",  
  "name": "Temporary Testing",  
  "type": "INTERNAL",  
  "roles": [  
    {  
      "id": "f8426061-8413-46ec-a84d-1b481a97b248",  
      "name": "prod_testing",  
      "type": "INTERNAL"  
    }  
  ],  
  "memberCount": 3,  
  "description": "Role for viewing the new feature"  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

404   Not Found

405   Method Not Allowed

## Add and Remove Role Members[​](#add-and-remove-role-members "Direct link to Add and Remove Role Members")

Add and remove members (roles and users) of the specified role.

Method and URL

```
PATCH /api/v3/role/{id}/member
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the role for which you want to add or remove members.

Example: 957a8af5-9211-4bc5-9fe5-1a44ff30304d

---

op Body   String

Action to take for the user or role.

Enum: add, remove

Example: add

---

id Body   String (UUID)

Unique identifier of the user or role to add or remove.

Example: 957a8af5-9211-4bc5-9fe5-1a44ff30304d

---

type Body   String

Type of member you want to add or remove.

Enum: role, user

Example: role

The request body is an array of objects. Each object includes the three parameters for a single user or role that you want to add or remove:

Example Request

```
curl -X PATCH 'https://{hostname}/api/v3/role/957a8af5-9211-4bc5-9fe5-1a44ff30304d/member' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '[  
  {  
    "op": "add",  
    "id": "f8426061-8413-46ec-a84d-1b481a97b248",  
    "type": "role"  
  },  
  {  
    "op": "add",  
    "id": "671cdeb8-1af9-45b6-98ee-8ca1e0543a38",  
    "type": "user"  
  },  
  {  
    "op": "remove",  
    "id": "6f87a9c5-d733-4935-8331-875a4a8e09d7",  
    "type": "role"  
  },  
  {  
    "op": "remove",  
    "id": "614a6938-7a69-4f7c-ab96-00b50addb1f9",  
    "type": "user"  
  }  
]'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

404   Not Found

405   Method Not Allowed

## Deleting a Role[​](#deleting-a-role "Direct link to Deleting a Role")

Delete the specified role.

Method and URL

```
DELETE /api/v3/role/{id}
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the role that you want to delete.

note

It is not possible to delete a system role, like ADMIN or PUBLIC. Requests to delete a system role result in a `404 Not Found` response.

Example: 957a8af5-9211-4bc5-9fe5-1a44ff30304d

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/role/957a8af5-9211-4bc5-9fe5-1a44ff30304d' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Reflection Summary](/25.x/reference/api/reflections/reflection-summary)[Next

Role Privileges](/25.x/reference/api/roles/privilege)

* [Role Attributes](#role-attributes)
* [Creating a Role](#creating-a-role)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Role by ID](#retrieving-a-role-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Role by Name](#retrieving-a-role-by-name)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Role](#updating-a-role)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Add and Remove Role Members](#add-and-remove-role-members)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting a Role](#deleting-a-role)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/scripts/

Version: 25.x

On this page

# Scripts

Use the Scripts API to manage [scripts](/25.x/sonar/query-manage/querying-data/#2-scripts), retrieve the contents of scripts for use in a scheduler, retrieve and update privileges on scripts, and migrate scripts between different environments.

Scripts Object

```
{  
  "total": 3,  
  "data": [  
    {  
      "id": "74cfddfd-cb0b-4b2f-b555-cb8b827fec1e",  
      "name": "newScript",  
      "content": "SELECT * FROM sampledb",  
      "context": [  
        "@dremio",  
        "scriptsFolder"  
      ],  
      "owner": "8be516f3-04c4-4d19-824d-5a70b3c4442e",  
      "createdAt": "2024-05-24T17:42:00.304Z",  
      "createdBy": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
      "modifiedAt": "2024-05-24T17:42:00.304Z",  
      "modifiedBy": "a97c694f-1e55-4f34-91aa-97f99fee802e"  
    },  
    {  
      "id": "37dab994-3f1f-4de7-b2e7-49cb5ff0b395",  
      "name": "tmp_testing_04-15-24",  
      "content": "-- create table accounting_storage.\"tmp.dremio.com\".test1(id INT);\n-- refresh dataset test1\nalter table test1 REFRESH METADATA;",  
      "context": [  
        "accounting_storage",  
        "tmp.dremio.com"  
      ],  
      "owner": "ba92bf87-174d-422e-becb-d526757c8099",  
      "createdAt": "2024-04-15T10:38:31.433Z",  
      "createdBy": "ba92bf87-174d-422e-becb-d526757c8099",  
      "modifiedAt": "2024-04-15T11:03:27.542Z",  
      "modifiedBy": "ba92bf87-174d-422e-becb-d526757c8099"  
    },  
    {  
      "id": "02fef13e-cedd-46ac-b5bf-abcdcd092146",  
      "name": "pop10000_A",  
      "content": "SELECT * FROM Samples.\"samples.dremio.com\".\"zips.json\" WHERE pop > 10000 AND STARTS_WITH(city, 'A');\n\nCREATE OR REPLACE VIEW myView AS\nSELECT city, state, pop FROM Samples.\"samples.dremio.com\".\"zips.json\"\nWHERE pop > 10000;\n\nCREATE OR REPLACE VIEW myView2 AS\nSELECT * FROM myView\nWHERE STARTS_WITH(city, 'A');\n\nALTER TABLE myView2 \nCREATE RAW Reflection myReflection \nUSING DISPLAY(city, state, pop);\n\nSELECT * FROM myView2;\n\nCREATE OR REPLACE FUNCTION isMA(state VARCHAR)\n    RETURNS BOOLEAN\n    RETURN SELECT state = 'MA';\n\nALTER TABLE myView ADD ROW ACCESS POLICY isMA(\"state\");\n\nSELECT * FROM myView2;\n\n// Refresh the reflection\n\nSELECT * FROM myView2;",  
      "context": [  
        "@dev"  
      ],  
      "owner": "7a92baf7-646a-4bc5-b0f4-eaf18d0a9921",  
      "createdAt": "2024-05-16T18:08:06.363Z",  
      "createdBy": "7a92baf7-646a-4bc5-b0f4-eaf18d0a9921",  
      "modifiedAt": "2024-05-16T18:31:22.593Z",  
      "modifiedBy": "7a92baf7-646a-4bc5-b0f4-eaf18d0a9921"  
    }  
  ]  
}
```

## Scripts Attributes[​](#scripts-attributes "Direct link to Scripts Attributes")

total Integer

Total number of scripts in the organization.

Example: 3

---

[data](/25.x/reference/api/scripts/#attributes-of-objects-in-the-data-array) Array of Object

List of the scripts in the organization, with an individual object representing each script.

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

id String (UUID)

Unique identifier of the script. Generated by Dremio and immutable.

Example: 74cfddfd-cb0b-4b2f-b555-cb8b827fec1e

---

name String

User-provided name of the script.

Example: newScript

---

content String

The script's SQL.

Example: SELECT \* FROM sampledb

---

context Array of String

Path where the SQL query specified in the content attribute runs. If no context is specified for the script, the value is an empty array.

Example: ["@dremio","scriptsFolder"]

---

owner String

Unique identifier for the user who owns the script.

Example: 8be516f3-04c4-4d19-824d-5a70b3c4442e

---

createdAt String

Date and time that the script was created. In UTC format.

Example: 2024-05-24T17:42:00.304Z

---

createdBy String

The unique identifier for the user who created the script.

Example: a97c694f-1e55-4f34-91aa-97f99fee802e

---

modifiedAt String

Date and time that the script was last modified. In UTC format.

Example: 2024-05-24T17:42:00.304Z

---

modifiedBy String

The unique identifier for the user who last modified the script.

Example: a97c694f-1e55-4f34-91aa-97f99fee802e

## Creating a Script[​](#creating-a-script "Direct link to Creating a Script")

Create a script.

Method and URL

```
POST /api/v3/scripts
```

### Parameters[​](#parameters "Direct link to Parameters")

name Body   String

Name to use for the script.

Example: newScript

---

content Body   String

The SQL for the script.

Example: SELECT \* FROM sampledb

---

context Body   Array of String   Optional

Path where the SQL query specified in the content attribute should run.

Example: ["@dremio","scriptsFolder"]

---

owner Body   String   Optional

Unique identifier for the user who should own the script. Default is the ID for the user who creates the script.

Example: 8be516f3-04c4-4d19-824d-5a70b3c4442e

Example Request

```
curl -X POST 'https://{hostname}/api/v3/scripts' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "newScript",  
  "content": "SELECT * FROM sampledb",  
  "context": [  
    "@dremio",  
    "scriptsFolder"  
  ],  
  "owner": "8be516f3-04c4-4d19-824d-5a70b3c4442e"  
}'
```

Example Response

```
{  
  "id": "f873a72e-12a5-4537-a393-f9675da7c5f8",  
  "name": "newScript",  
  "content": "SELECT * FROM sampledb",  
  "context": [  
    "@dremio",  
    "scriptsFolder"  
  ],  
  "owner": "8be516f3-04c4-4d19-824d-5a70b3c4442e",  
  "createdAt": "2024-05-24T17:42:00.304Z",  
  "createdBy": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
  "modifiedAt": "2024-05-24T17:42:00.304Z",  
  "modifiedBy": "a97c694f-1e55-4f34-91aa-97f99fee802e"  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

## Retrieving All Scripts[​](#retrieving-all-scripts "Direct link to Retrieving All Scripts")

Retrieve a list of all scripts in the organization.

Method and URL

```
GET /api/v3/scripts/
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

createdBy Query   String   Optional

Unique identifier for the user who created the scripts you want to retrieve. For more information, read [createdBy Query Parameter](/25.x/reference/api/#createdby-query-parameter).

---

maxResults Query   Integer   Optional

Maximum number of scripts to return in the response. Maximum valid value is `100`. Default is `25`. For more information, read [maxResults Query Parameter](/25.x/reference/api/#maxresults-query-parameter).

---

offset Query   Integer   Optional

Number of rows to skip for pagination. Default is `0`. Read [limit and offset Query Parameters](/25.x/reference/api/#limit-and-offset-query-parameters) for usage examples.

---

orderBy Query   String   Optional

Organize the response in ascending (default) or descending order by name, createdAt, or modifiedAt. To specify descending order, precede the orderBy value with a `-` character. To organize the response by more than one attribute, use a comma-separated list: `?orderBy=createdAt,name`. For more information, read [orderBy Query Parameter](/25.x/reference/api/#orderby-query-parameter).

---

ownedBy Query   String   Optional

Unique identifier for the user who owns the scripts you want to retrieve. For more information, read [ownedBy Query Parameter](/25.x/reference/api/#ownedby-query-parameter).

---

search Query   String   Optional

The string for which to search the values of the name attributes in scripts. Read [search Query Parameter](/25.x/reference/api/#search-query-parameter) for usage examples.

Example Request

```
curl -X GET 'https://{hostname}/api/v3/scripts' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "total": 3,  
  "data": [  
    {  
      "id": "74cfddfd-cb0b-4b2f-b555-cb8b827fec1e",  
      "name": "newScript",  
      "content": "SELECT * FROM sampledb",  
      "context": [  
        "@dremio",  
        "scriptsFolder"  
      ],  
      "owner": "8be516f3-04c4-4d19-824d-5a70b3c4442e",  
      "createdAt": "2024-05-24T17:42:00.304Z",  
      "createdBy": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
      "modifiedAt": "2024-05-24T17:42:00.304Z",  
      "modifiedBy": "a97c694f-1e55-4f34-91aa-97f99fee802e"  
    },  
    {  
      "id": "37dab994-3f1f-4de7-b2e7-49cb5ff0b395",  
      "name": "tmp_testing_04-15-24",  
      "content": "-- create table accounting_storage.\"tmp.dremio.com\".test1(id INT);\n-- refresh dataset test1\nalter table test1 REFRESH METADATA;",  
      "context": [  
        "accounting_storage",  
        "tmp.dremio.com"  
      ],  
      "owner": "ba92bf87-174d-422e-becb-d526757c8099",  
      "createdAt": "2024-04-15T10:38:31.433Z",  
      "createdBy": "ba92bf87-174d-422e-becb-d526757c8099",  
      "modifiedAt": "2024-04-15T11:03:27.542Z",  
      "modifiedBy": "ba92bf87-174d-422e-becb-d526757c8099"  
    },  
    {  
      "id": "02fef13e-cedd-46ac-b5bf-abcdcd092146",  
      "name": "pop10000_A",  
      "content": "SELECT * FROM Samples.\"samples.dremio.com\".\"zips.json\" WHERE pop > 10000 AND STARTS_WITH(city, 'A');\n\nCREATE OR REPLACE VIEW myView AS\nSELECT city, state, pop FROM Samples.\"samples.dremio.com\".\"zips.json\"\nWHERE pop > 10000;\n\nCREATE OR REPLACE VIEW myView2 AS\nSELECT * FROM myView\nWHERE STARTS_WITH(city, 'A');\n\nALTER TABLE myView2 \nCREATE RAW Reflection myReflection \nUSING DISPLAY(city, state, pop);\n\nSELECT * FROM myView2;\n\nCREATE OR REPLACE FUNCTION isMA(state VARCHAR)\n    RETURNS BOOLEAN\n    RETURN SELECT state = 'MA';\n\nALTER TABLE myView ADD ROW ACCESS POLICY isMA(\"state\");\n\nSELECT * FROM myView2;\n\n// Refresh the reflection\n\nSELECT * FROM myView2;",  
      "context": [  
        "@dev"  
      ],  
      "owner": "7a92baf7-646a-4bc5-b0f4-eaf18d0a9921",  
      "createdAt": "2024-05-16T18:08:06.363Z",  
      "createdBy": "7a92baf7-646a-4bc5-b0f4-eaf18d0a9921",  
      "modifiedAt": "2024-05-16T18:31:22.593Z",  
      "modifiedBy": "7a92baf7-646a-4bc5-b0f4-eaf18d0a9921"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

## Retrieving a Script by ID[​](#retrieving-a-script-by-id "Direct link to Retrieving a Script by ID")

Retrieve the specified script.

Method and URL

```
GET /api/v3/scripts/{id}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the script you want to retrieve.

Example: 74cfddfd-cb0b-4b2f-b555-cb8b827fec1e

Example Request

```
curl -X GET 'https://{hostname}/api/v3/scripts/74cfddfd-cb0b-4b2f-b555-cb8b827fec1e' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "74cfddfd-cb0b-4b2f-b555-cb8b827fec1e",  
  "name": "newScript",  
  "content": "SELECT * FROM sampledb",  
  "context": [  
    "@dremio",  
    "scriptsFolder"  
  ],  
  "owner": "8be516f3-04c4-4d19-824d-5a70b3c4442e",  
  "createdAt": "2024-05-24T17:42:00.304Z",  
  "createdBy": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
  "modifiedAt": "2024-05-24T17:42:00.304Z",  
  "modifiedBy": "a97c694f-1e55-4f34-91aa-97f99fee802e"
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

## Updating a Script[​](#updating-a-script "Direct link to Updating a Script")

Update the specified script.

Method and URL

```
PATCH /api/v3/scripts/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the script.

Example: 74cfddfd-cb0b-4b2f-b555-cb8b827fec1e

---

name Body   String   Optional

User-provided name to use for the script.

Example: updatedScript

---

content Body   Array of String   Optional

The updated SQL for the script.

Example: SELECT \* FROM Samples."samples.dremio.com"."zips.json"

---

context Body   String   Optional

Path where the SQL query specified in the content attribute should run.

Example: ["@dremio","secondScriptsFolder"]

---

owner Body   String   Optional

Unique identifier for the user who should own the script.

Example: a97c694f-1e55-4f34-91aa-97f99fee802e

Example Request

```
curl -X PATCH 'https://{hostname}/api/v3/scripts/74cfddfd-cb0b-4b2f-b555-cb8b827fec1e' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "updatedScript",  
  "content": "SELECT * FROM Samples."samples.dremio.com"."zips.json"",  
  "context": [  
    "@dremio",  
    "secondScriptsFolder"  
  ],  
  "owner": "a97c694f-1e55-4f34-91aa-97f99fee802e"  
}'
```

Example Response

```
{  
  "id": "74cfddfd-cb0b-4b2f-b555-cb8b827fec1e",  
  "name": "updatedScript",  
  "content": "SELECT * FROM Samples.\"samples.dremio.com\".\"zips.json\"",  
  "context": [  
    "@dremio",  
    "secondScriptsFolder"  
  ],  
  "owner": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
  "createdAt": "2024-05-24T17:42:00.304Z",  
  "createdBy": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
  "modifiedAt": "2024-05-24T18:56:59.409Z",  
  "modifiedBy": "a97c694f-1e55-4f34-91aa-97f99fee802e"  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

404   Not Found

## Deleting a Script[​](#deleting-a-script "Direct link to Deleting a Script")

Delete the specified script.

Method and URL

```
DELETE /api/v3/scripts/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the script that you want to delete.

Example: 74cfddfd-cb0b-4b2f-b555-cb8b827fec1e

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/scripts/74cfddfd-cb0b-4b2f-b555-cb8b827fec1e' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

## Deleting a Group of Scripts[​](#deleting-a-group-of-scripts "Direct link to Deleting a Group of Scripts")

Delete the listed group of scripts.

Method and URL

```
POST /api/v3/scripts:batchDelete
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

ids Body   Array of String

Array of unique identifiers of the scripts that you want to delete.

Example: ["74cfddfd-cb0b-4b2f-b555-cb8b827fec1e","37dab994-3f1f-4de7-b2e7-49cb5ff0b395","02fef13e-cedd-46ac-b5bf-abcdcd092146"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/scripts:batchDelete' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "ids": [  
    "74cfddfd-cb0b-4b2f-b555-cb8b827fec1e",  
    "37dab994-3f1f-4de7-b2e7-49cb5ff0b395",  
    "02fef13e-cedd-46ac-b5bf-abcdcd092146"  
  ]  
}'
```

Example Response

```
{  
  "unauthorizedIds": [],  
  "notFoundIds": [],  
  "otherErrorIds": []  
}
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

## Retrieving Privilege Information for a Script[​](#retrieving-privilege-information-for-a-script "Direct link to Retrieving Privilege Information for a Script")

Retrieve information about the privileges granted on the specified script.

Method and URL

```
GET /api/v3/scripts/{id}/grants
```

### Parameters[​](#parameters-6 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the script whose privilege information you want to retrieve.

Example: 74cfddfd-cb0b-4b2f-b555-cb8b827fec1e

Example Request

```
curl -X GET 'https://{hostname}/api/v3/scripts/74cfddfd-cb0b-4b2f-b555-cb8b827fec1e/grants' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "users": [  
    {  
      "granteeId": "8be516f3-04c4-4d19-824d-5a70b3c4442e",  
      "privileges": [  
        "VIEW",  
        "MODIFY",  
        "DELETE",  
        "MANAGE_GRANTS"  
      ]  
    },  
    {  
      "granteeId": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
      "privileges": [  
        "VIEW",  
        "MODIFY",  
        "DELETE",  
        "MANAGE_GRANTS"  
      ]  
    }  
  ],  
  "roles": []  
}
```

### Response Status Codes[​](#response-status-codes-6 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

## Updating Privileges Granted on a Script[​](#updating-privileges-granted-on-a-script "Direct link to Updating Privileges Granted on a Script")

Update the privileges that are granted on the specified script.

Method and URL

```
PUT /api/v3/scripts/{id}/grants
```

### Parameters[​](#parameters-7 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the script whose privilege grants you want to update.

Example: 74cfddfd-cb0b-4b2f-b555-cb8b827fec1e

---

[users](/25.x/reference/api/scripts/#attributes-of-objects-in-the-users-array) Body   Array of Object   Optional

Array of objects that specify which users should have privileges on the script, as well as each user's specific privileges.

---

[roles](/25.x/reference/api/scripts/#attributes-of-objects-in-the-roles-array) Body   Array of Object   Optional

Array of objects that specify which roles should have privileges on the script, as well as each role's specific privileges.

#### Attributes of Objects in the `users` Array[​](#attributes-of-objects-in-the-users-array "Direct link to attributes-of-objects-in-the-users-array")

granteeId Body   String   Optional

Unique identifier for the user for whom you want to add or update privileges.

Example: 8be516f3-04c4-4d19-824d-5a70b3c4442e

---

privileges Body   Array of String   Optional

The array of privileges you want to add or update for the user.

Enum: VIEW, MODIFY, DELETE, MANAGE\_GRANTS

Example: ["VIEW","MODIFY","DELETE"]

#### Attributes of Objects in the `roles` Array[​](#attributes-of-objects-in-the-roles-array "Direct link to attributes-of-objects-in-the-roles-array")

granteeId Body   String   Optional

Unique identifier for the role for which you want to add or update privileges.

Example: 6a1725a3-5721-44e3-b64f-0b39a35749ab

---

privileges Body   Array of String   Optional

The array of privileges you want to add or update for the role.

Enum: VIEW, MODIFY, DELETE, MANAGE\_GRANTS

Example: ["VIEW","MODIFY","DELETE"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/scripts/74cfddfd-cb0b-4b2f-b555-cb8b827fec1e/grants' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "users": [  
    {  
      "granteeId": "8be516f3-04c4-4d19-824d-5a70b3c4442e",  
      "privileges": [  
        "VIEW",  
        "MODIFY",  
        "DELETE"  
      ]  
    }  
  ],  
  "roles": [  
    {  
      "granteeId": "6a1725a3-5721-44e3-b64f-0b39a35749ab",  
      "privileges": [  
        "VIEW",  
        "MODIFY",  
        "DELETE"  
      ]  
    }  
  ]  
}'
```

Example Response

```
{  
  "users": [  
    {  
      "granteeId": "8be516f3-04c4-4d19-824d-5a70b3c4442e",  
      "privileges": [  
        "VIEW",  
        "MODIFY",  
        "DELETE"  
      ]  
    },  
    {  
      "granteeId": "a97c694f-1e55-4f34-91aa-97f99fee802e",  
      "privileges": [  
        "VIEW",  
        "MODIFY",  
        "DELETE",  
        "MANAGE_GRANTS"  
      ]  
    }  
  ],  
  "roles": [  
    {  
      "granteeId": "6a1725a3-5721-44e3-b64f-0b39a35749ab",  
      "privileges": [  
        "VIEW",  
        "MODIFY",  
        "DELETE"  
      ]  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-7 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

Was this page helpful?

[Previous

Role Privileges](/25.x/reference/api/roles/privilege)[Next

Source](/25.x/reference/api/source)

* [Scripts Attributes](#scripts-attributes)
* [Creating a Script](#creating-a-script)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving All Scripts](#retrieving-all-scripts)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Script by ID](#retrieving-a-script-by-id)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Script](#updating-a-script)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a Script](#deleting-a-script)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting a Group of Scripts](#deleting-a-group-of-scripts)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-5)
* [Retrieving Privilege Information for a Script](#retrieving-privilege-information-for-a-script)
  + [Parameters](#parameters-6)
  + [Response Status Codes](#response-status-codes-6)
* [Updating Privileges Granted on a Script](#updating-privileges-granted-on-a-script)
  + [Parameters](#parameters-7)
  + [Response Status Codes](#response-status-codes-7)

---

# Source: https://docs.dremio.com/25.x/reference/api/source

Version: 25.x

On this page

# Source

Use the Source API to clear the [AWS Lake Formation](/25.x/sonar/data-sources/metastores/aws-glue-catalog#lake-formation-integration) permission cache for AWS Glue Data Catalog sources.

Dremio keeps a cache of permissions defined in AWS Lake Formation with a one-hour expiry time. When the cache for the queried table expires, Dremio requests permission information from AWS Lake Formation. After changing permissions on the AWS Lake Formation side, use the Source API to immediately invalidate Dremio's AWS Lake Formation permission cache.

note

The Source API is supported only for AWS Glue Data Catalog sources.

## Clearing the Permission Cache[​](#clearing-the-permission-cache "Direct link to Clearing the Permission Cache")

Clear the AWS Lake Formation permission cache for an AWS Glue Data Catalog source.

Method and URL

```
DELETE /api/v3/source/{source-name}/permission-cache
```

### Parameters[​](#parameters "Direct link to Parameters")

source-name Path   String

The name of the AWS Glue Data Catalog source whose Lake Formation permission cache you want to clear.

Example: glueProd

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/source/glueProd/permission-cache' \  
--header 'Authorization: Bearer <personal access token>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Responses[​](#responses "Direct link to Responses")

204   No Content

400   Bad Request

404   Not Found

415   Unsupported Media Type

500   Internal Server Error

Was this page helpful?

[Previous

Scripts](/25.x/reference/api/scripts/)[Next

SQL](/25.x/reference/api/sql/)

* [Clearing the Permission Cache](#clearing-the-permission-cache)
  + [Parameters](#parameters)
  + [Responses](#responses)

---

# Source: https://docs.dremio.com/25.x/reference/api/sql/

Version: 25.x

On this page

# SQL

Use the SQL API to submit SQL queries. The response contains the ID for the job associated with the SQL query. Use the job ID in [Job API](/25.x/reference/api/job/) requests to get more information about the job, including results.

## Submitting an SQL Query[​](#submitting-an-sql-query "Direct link to Submitting an SQL Query")

Submit an SQL query and retrieve the associated job ID for use in [Job API](/25.x/reference/api/job/) requests.

Method and URL

```
POST /api/v3/sql
```

### Parameters[​](#parameters "Direct link to Parameters")

sql Body   String

SQL query to run.

note

Double-quotation marks within a SQL statement need to be escaped.

Example: SELECT \* FROM Samples."samples.dremio.com"."SF weather 2018-2019.csv"

---

context Body   Array of String   Optional

Path to the container where the query should run within Dremio, expressed as an array. The path consists of the source or space, followed by the folder and subfolders.

Example: ["Samples","samples.dremio.com"]

---

[references](/25.x/reference/api/sql/#parameters-of-the-references-object) Body   Object   Optional

References to the specific versions (branches, tags, and commits) in Nessie sources where you want to run the SQL query. If references are not specified for a Nessie source, the SQL query runs on the default branch.

Example: {"nessieSource1": {"type": "BRANCH","value": "testing"},"nessieSource2": {"type": "TAG","value": "Test commit"},"nessieSource3": {"type": "COMMIT","value": "7a5edb57e035f52beccfab632cea070514eb8b773f616aaeaf668e2f0be8f10d"}}

#### Parameters of the `references` Object[​](#parameters-of-the-references-object "Direct link to parameters-of-the-references-object")

[<Nessie source>](/25.x/reference/api/sql/#parameters-of-the-nessie-source-object) Body   String   Optional

The name of the Nessie source where you want to run the SQL query.

Example: nessieSource1

##### Parameters of the `<Nessie source>` Object[​](#parameters-of-the-nessie-source-object "Direct link to parameters-of-the-nessie-source-object")

type Body   String   Optional

The type of Nessie source object where you want to run the SQL query.

Enum: BRANCH, TAG, COMMIT

Example: BRANCH

---

value Body   String   Optional

The branch or tag name or commit hash in the Nessie source on which you want to run the SQL query.

Example: testing

Example Request Using Only the SQL Parameter

```
curl -X POST 'https://{hostname}/api/v3/sql' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "sql": "SELECT * FROM Samples.\"samples.dremio.com\".\"SF weather 2018-2019.csv\""  
}'
```

Example Request Using Optional Parameters

```
curl -X POST 'https://{hostname}/api/v3/sql' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "sql": "SELECT * FROM \"SF weather 2018-2019.csv\"",  
  "context": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "references": {  
    "nessieSource1": {  
      "type": "BRANCH",  
      "value": "testing"  
    },  
    "nessieSource2": {  
      "type": "TAG",  
      "value": "Test commit"  
    },  
    "nessieSource3": {  
      "type": "COMMIT",  
      "value": "7a5edb57e035f52beccfab632cea070514eb8b773f616aaeaf668e2f0be8f10d"  
    }  
  }  
}'
```

Example Response

```
{  
  "id": "2f067496-7cf0-a70e-0222-34d53a5dc800"  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

404   Not Found

Was this page helpful?

[Previous

Source](/25.x/reference/api/source)[Next

Token](/25.x/reference/api/token/)

* [Submitting an SQL Query](#submitting-an-sql-query)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/token/

Version: 25.x

On this page

# Token Enterprise

Use the Token API to manage personal access tokens associated with Dremio users.

## Deleting All Tokens[​](#deleting-all-tokens "Direct link to Deleting All Tokens")

Delete all personal access tokens for the user sending the API request.

Method and URL

```
DELETE /api/v3/token
```

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/token' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

## Deleting a Single Token[​](#deleting-a-single-token "Direct link to Deleting a Single Token")

Delete the specified personal access token for the specified user.

Method and URL

```
DELETE /api/v3/user/{userName}/token/{id}
```

### Parameters[​](#parameters "Direct link to Parameters")

userName Path   String

Name of the Dremio user whose personal access token you want to delete.

Example: exampleuser1

---

id Path   String (UUID)

Token ID for the personal access token you want to delete.

Example: 3eca2b0e-d122-48d6-9a97-f81b18db2380

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/user/exampleuser1/token/3eca2b0e-d122-48d6-9a97-f81b18db2380' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

Was this page helpful?

[Previous

SQL](/25.x/reference/api/sql/)[Next

User](/25.x/reference/api/user/)

* [Deleting All Tokens](#deleting-all-tokens)
  + [Response Status Codes](#response-status-codes)
* [Deleting a Single Token](#deleting-a-single-token)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes-1)

---

# Source: https://docs.dremio.com/25.x/reference/api/user/

Version: 25.x

On this page

# User Enterprise

Use the User API to manage Dremio [users](/25.x/security/authentication/users/), their privileges, and their personal access tokens.

User Object

```
{  
  "@type": "EnterpriseUser",  
  "id": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
  "name": "dremio",  
  "firstName": "Dre",  
  "lastName": "Mio",  
  "email": "user@dremio.com",  
  "tag": "EuCNt1nnvdI=",  
  "roles": [  
    {  
      "id": "8ac1bbca-479c-4c47-87e9-7f946f665c13",  
      "name": "PUBLIC",  
      "type": "SYSTEM"  
    },  
    {  
      "id": "43dce6d7-40ff-4afa-9901-71c30eb92744",  
      "name": "ADMIN",  
      "type": "SYSTEM"  
    }  
  ],  
  "source": "local",  
  "active": true  
}
```

## User Attributes[​](#user-attributes "Direct link to User Attributes")

@type String

Type of user.

Enum: EnterpriseUser, User

Example: EnterpriseUser

---

id String (UUID)

Unique identifier of the user.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

---

name String

Username of the Dremio user account.

Example: dremio

---

firstName String

User's first name.

Example: Dre

---

lastName String

User's last name.

Example: Mio

---

email String

User's email address. If the user is managed with the Dremio Okta application, email is the primary email address in the user's Okta profile. If the user is managed with Microsoft Entra ID, email is the work email address in the user's Microsoft Entra ID profile.

Example: [user@dremio.com](mailto:user@dremio.com)

---

tag String

Unique identifier of the user version. Dremio changes the tag whenever the user changes and uses the tag to ensure that PUT requests apply to the most recent version of the user.

Example: EuCNt1nnvdI=

---

[roles](/25.x/reference/api/user/#attributes-of-objects-in-the-roles-array) Array of Object

Information about the local and referenced external roles to which the user belongs.

Example: [{"id": "8ac1bbca-479c-4c47-87e9-7f946f665c13","name": "PUBLIC","type": "SYSTEM"},{"id": "43dce6d7-40ff-4afa-9901-71c30eb92744","name": "ADMIN","type": "SYSTEM"}]

---

source String

Information about how the user was created.

* `external`: User was imported with an external service like Microsoft Entra ID, Lightweight Directory Access Protocol (LDAP), or a System for Cross-domain Identity Management (SCIM) provider.
* `local`: User was created manually in the Dremio user interface (UI) or with the User API.

Example: local

---

active Boolean

If the user account is active in Dremio, the value is `true`. Otherwise, the value is `false`. The active value is set to `true` when the user is created and only changes if the user's status changes in external System for Cross-domain Identity Management (SCIM) provisioning. When the user is activated in the SCIM application, Dremio sets the value to `true`. When the user is deactivated in the SCIM application, Dremio sets the value to `false`.

Example: true

#### Attributes of Objects in the `roles` Array[​](#attributes-of-objects-in-the-roles-array "Direct link to attributes-of-objects-in-the-roles-array")

id String (UUID)

Unique identifier of the role.

Example: 43dce6d7-40ff-4afa-9901-71c30eb92744

---

name String

Name of the role.

Example: ADMIN

---

type String

Origin of the role.

* `INTERNAL`: Role was created in the Dremio user interface (UI) or with the Role API.
* `EXTERNAL`: Role was imported from an external service like Microsoft Entra ID, Lightweight Directory Access Protocol (LDAP), or a System for Cross-domain Identity Management (SCIM) provider.
* `SYSTEM`: Role was predefined in Dremio.

Example: SYSTEM

## Creating a User[​](#creating-a-user "Direct link to Creating a User")

Create a Dremio user.

Method and URL

```
POST /api/v3/user
```

### Parameters[​](#parameters "Direct link to Parameters")

name Body   String

Username for the Dremio user account. The name must be unique and cannot be updated after the user is created.

Example: dremio

---

firstName Body   String   Optional

User's first name.

Example: Dre

---

lastName Body   String   Optional

User's last name.

Example: Mio

---

email Body   String   Optional

User's email address.

Example: [user@dremio.com](mailto:user@dremio.com)

---

[roles](/25.x/reference/api/user/#parameters-of-objects-in-the-roles-array) Body   Array of Object   Optional

Information about the roles to which the user should be assigned. All users are assigned to the PUBLIC role by default.

Example: [{"id": "8ac1bbca-479c-4c47-87e9-7f946f665c13","name": "PUBLIC","type": "SYSTEM"},{"id": "43dce6d7-40ff-4afa-9901-71c30eb92744","name": "ADMIN","type": "SYSTEM"}]

#### Parameters of Objects in the `roles` Array[​](#parameters-of-objects-in-the-roles-array "Direct link to parameters-of-objects-in-the-roles-array")

id Body   String (UUID)

Unique identifier of the role.

Example: 43dce6d7-40ff-4afa-9901-71c30eb92744

---

name Body   String

Name of the role. All users are assigned to the PUBLIC role by default.

Example: ADMIN

---

type Body   String   Optional

Origin of the role.

* `INTERNAL`: Role was created in the Dremio user interface (UI) or with the Role API.
* `EXTERNAL`: Role was imported from an external service like Microsoft Entra ID, Lightweight Directory Access Protocol (LDAP), or a System for Cross-domain Identity Management (SCIM) provider.
* `SYSTEM`: Role was predefined in Dremio.

Example: SYSTEM

Example Request

```
curl -X POST 'https://{hostname}/api/v3/user' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "dremio",  
  "firstName": "Dre",  
  "lastName": "Mio",  
  "email": "user@dremio.com",  
  "roles": [  
    {  
      "id": "8ac1bbca-479c-4c47-87e9-7f946f665c13",  
      "name": "PUBLIC",  
      "type": "SYSTEM"  
    },  
    {  
      "id": "43dce6d7-40ff-4afa-9901-71c30eb92744",  
      "name": "ADMIN",  
      "type": "SYSTEM"  
    }  
  ]  
}'
```

Example Response

```
{  
  "@type": "EnterpriseUser",  
  "id": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
  "name": "dremio",  
  "firstName": "Dre",  
  "lastName": "Mio",  
  "email": "user@dremio.com",  
  "tag": "EuCNt1nnvdI=",  
  "roles": [  
    {  
      "id": "8ac1bbca-479c-4c47-87e9-7f946f665c13",  
      "name": "PUBLIC",  
      "type": "SYSTEM"  
    },  
    {  
      "id": "43dce6d7-40ff-4afa-9901-71c30eb92744",  
      "name": "ADMIN",  
      "type": "SYSTEM"  
    }  
  ],  
  "source": "external",  
  "active": true  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

204   No Content

400   Bad Request

401   Unauthorized

404   Not Found

405   Method Not Allowed

500   Internal Server Error

## Retrieving a User by ID[​](#retrieving-a-user-by-id "Direct link to Retrieving a User by ID")

Retrieve a specific user by the user's ID.

Method and URL

```
GET /api/v3/user/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String

Unique identifier of the user you want to retrieve.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

Example Request

```
curl -X GET 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "@type": "EnterpriseUser",  
  "id": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
  "name": "dremio",  
  "firstName": "Dre",  
  "lastName": "Mio",  
  "email": "user@dremio.com",  
  "tag": "EuCNt1nnvdI=",  
  "roles": [  
    {  
      "id": "8ac1bbca-479c-4c47-87e9-7f946f665c13",  
      "name": "PUBLIC",  
      "type": "SYSTEM"  
    },  
    {  
      "id": "43dce6d7-40ff-4afa-9901-71c30eb92744",  
      "name": "ADMIN",  
      "type": "SYSTEM"  
    }  
  ],  
  "source": "local",  
  "active": true  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

500   Internal Server Error

## Retrieving a User by Name[​](#retrieving-a-user-by-name "Direct link to Retrieving a User by Name")

Retrieve a specific user by the user's name.

Method and URL

```
GET /api/v3/user/by-name/{name}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

name Path   String

User name of the user you want to retrieve. User names are case-insensitive. If the user name includes special characters for a URL, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

Example Request

```
curl -X GET 'https://{hostname}/api/v3/user/by-name/dremio' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

When you retrieve a user by name, the response is an abbreviated user object that does not include the @type, roles, or source attributes:

Example Response

```
{  
  "id": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
  "name": "dremio",  
  "firstName": "Dre",  
  "lastName": "Mio",  
  "email": "user@dremio.com",  
  "tag": "EuCNt1nnvdI=",  
  "active": true  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

500   Internal Server Error

## Updating a User[​](#updating-a-user "Direct link to Updating a User")

Update the specified user.

Method and URL

```
PUT /api/v3/user/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user you want to update.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

id Body   String (UUID)

Unique identifier of the user you want to update.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

tag Body   String

Unique identifier of the user version to update. Dremio uses the tag to ensure that you are updating the most recent version of the user.

Example: BNGRmgfEnDg=

---

name Body   String

Name of the user.

Example: dremio

---

firstName Body   String   Optional

User's first name.

Example: Dre

---

lastName Body   String   Optional

User's last name.

Example: Mio

---

email Body   String   Optional

User's email address.

Example: [user@dremio.com](mailto:user@dremio.com)

---

[roles](/25.x/reference/api/user/#parameters-of-objects-in-the-roles-array-1) Body   String   Optional

Information about the roles to which the user should be assigned. All users are assigned to the PUBLIC role by default.

Example: [{"id": "8ac1bbca-479c-4c47-87e9-7f946f665c13","name": "PUBLIC","type": "SYSTEM"},{"id": "43dce6d7-40ff-4afa-9901-71c30eb92744","name": "ADMIN","type": "SYSTEM"}]

#### Parameters of Objects in the `roles` Array[​](#parameters-of-objects-in-the-roles-array-1 "Direct link to parameters-of-objects-in-the-roles-array-1")

id Body   String (UUID)

Unique identifier of the role.

Example: 43dce6d7-40ff-4afa-9901-71c30eb92744

---

name Body   String

Name of the role. All users are assigned to the PUBLIC role by default.

Example: VIEWER

---

type Body   String   Optional

Origin of the role.

* `INTERNAL`: Role was created in the Dremio user interface (UI) or with the Role API.
* `EXTERNAL`: Role was imported from an external service like Microsoft Entra ID, Lightweight Directory Access Protocol (LDAP), or a System for Cross-domain Identity Management (SCIM) provider.
* `SYSTEM`: Role was predefined in Dremio.

Enum: SYSTEM, INTERNAL, EXTERNAL

Example: INTERNAL

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "id": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
  "name": "dremio",  
  "tag": "EuCNt1nnvdI=",  
  "firstName": "Dremio",  
  "lastName": "User",  
  "email": "user@dremio.com",  
  "roles": [  
    {  
      "id": "2f498015-9211-4b15-8fc0-493628ae7b6e",  
      "name": "VIEWER"  
    }  
  ]  
}'
```

Example Response

```
{  
  "@type": "EnterpriseUser",  
  "id": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
  "name": "dremio",  
  "firstName": "Dremio",  
  "lastName": "User",  
  "email": "user@dremio.com",  
  "tag": "BE1LYg3cmAk=",  
  "roles": [  
    {  
      "id": "8ac1bbca-479c-4c47-87e9-7f946f665c13",  
      "name": "PUBLIC",  
      "type": "SYSTEM"  
    },  
    {  
      "id": "2f498015-9211-4b15-8fc0-493628ae7b6e",  
      "name": "VIEWER",  
      "type": "INTERNAL"  
    }  
  ],  
  "source": "external",  
  "active": true  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

500   Internal Server Error

## Deleting a User[​](#deleting-a-user "Direct link to Deleting a User")

Delete the specified user.

Method and URL

```
DELETE /api/v3/user/{id}?version={tag}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user that you want to delete. You can only delete users that are *not* currently logged in to Dremio.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

---

version Query   String

Unique identifier of the user version to delete. The version value is the user's tag, which you can find in the response for a request to [Retrieve a User by ID](/25.x/reference/api/user/#retrieving-a-user-by-id) or [Retrieve a User by Name](/25.x/reference/api/user/#retrieving-a-user-by-name). Dremio uses the version value to ensure that you are deleting the most recent version of the user. If you provide an incorrect tag, the response includes an error message that lists the correct tag for the specified user ID.

Example: ?version=BE1LYg3cmAk=

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43?version=BE1LYg3cmAk=' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Token](/25.x/reference/api/token/)[Next

User Privileges](/25.x/reference/api/user/privilege)

* [User Attributes](#user-attributes)
* [Creating a User](#creating-a-user)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a User by ID](#retrieving-a-user-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a User by Name](#retrieving-a-user-by-name)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a User](#updating-a-user)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a User](#deleting-a-user)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)

---

# Source: https://docs.dremio.com/25.x/reference/api/wlm/

Version: 25.x

# Workload Management Enterprise

Use the Workload Management API to manage cluster resources and workloads by defining [queues](/25.x/reference/api/wlm/queue/) that have specific characteristics like memory limits, CPU priority, and queueing and runtime timeouts. You can also define [rules](/25.x/reference/api/wlm/rule/) that determine how to assign queries to specific queues.

See [Workload Management](/25.x/admin/workloads/workload-management/) for more information about Dremio's workload-management features.

Was this page helpful?

[Previous

User Tokens](/25.x/reference/api/user/token)[Next

Queue](/25.x/reference/api/wlm/queue)

---

# Source: https://docs.dremio.com/25.x/reference/api/reflections/reflection-summary/

Version: 25.x

On this page

# Reflection Summary Enterprise

Use the Reflection API to retrieve a Reflection summary that includes the raw and aggregation Reflections for the Dremio instance.

Reflection summary objects are different from Reflection objects. Reflection summaries do not include certain attributes that define the Reflection, like the display, dimension, measure, sort, and partition attributes. Reflection summaries do include several attributes that do not appear in Reflection objects, like datasetType, datasetPath, and counts and links for considered, matched, and chosen jobs.

Reflection Summary Object

```
{  
  "data": [  
    {  
      "createdAt": "2022-07-05T19:19:40.244Z",  
      "updatedAt": "2023-01-13T19:46:01.313Z",  
      "id": "27077c03-ae49-454c-a7bb-a9a8b5eca224",  
      "reflectionType": "AGGREGATION",  
      "name": "NYC_taxi_agg",  
      "currentSizeBytes": 9272,  
      "outputRecords": 51,  
      "totalSizeBytes": 9272,  
      "datasetId": "fa7c487f-9550-474e-8a41-4826564c6b09",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:05:03.532Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 46387  
      },  
      "consideredCount": 202,  
      "matchedCount": 45,  
      "chosenCount": 5,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-26T23:27:04.281Z",  
      "updatedAt": "2023-01-26T23:27:04.281Z",  
      "id": "0e3d765a-2291-4a04-81eb-2daf5477cc7d",  
      "reflectionType": "RAW",  
      "name": "Raw Reflection",  
      "currentSizeBytes": 0,  
      "outputRecords": -1,  
      "totalSizeBytes": 0,  
      "datasetId": "acdad4be-7049-47e4-b616-b471c5b3c60c",  
      "datasetType": "PHYSICAL_DATASET",  
      "datasetPath": [  
        "@dremio",  
        "test"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "GIVEN_UP",  
        "availabilityStatus": "NONE",  
        "combinedStatus": "FAILED",  
        "refreshMethod": "NONE",  
        "failureCount": 3,  
        "lastFailureMessage": "The Default engine is not online.",  
        "lastDataFetchAt": null,  
        "expiresAt": null,  
        "lastRefreshDurationMillis": -1  
      },  
      "consideredCount": 0,  
      "matchedCount": 0,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:19.030Z",  
      "updatedAt": "2023-01-13T19:50:19.030Z",  
      "id": "8eec62d7-3419-4cf3-997d-0a153d81ed8a",  
      "reflectionType": "AGGREGATION",  
      "name": "dataset991_agg991",  
      "currentSizeBytes": 9273,  
      "outputRecords": 51,  
      "totalSizeBytes": 9273,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.342Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 11697  
      },  
      "consideredCount": 60,  
      "matchedCount": 9,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:17.714Z",  
      "updatedAt": "2023-01-13T19:50:17.714Z",  
      "id": "167428eb-7936-4ea2-a1fb-23b1ac6e9454",  
      "reflectionType": "RAW",  
      "name": "dataset991_raw991",  
      "currentSizeBytes": 818790,  
      "outputRecords": 29467,  
      "totalSizeBytes": 818790,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.747Z",  
        "expiresAt": "3022-05-16T19:46:02.747Z",  
        "lastRefreshDurationMillis": 16666  
      },  
      "consideredCount": 54,  
      "matchedCount": 37,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    }  
  ],  
  "nextPageToken": "CiQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==",  
  "isCanAlterReflections": true  
}
```

## Reflection Summary Attributes[​](#reflection-summary-attributes "Direct link to Reflection Summary Attributes")

[data](/25.x/reference/api/reflections/reflection-summary#attributes-of-objects-in-the-data-array) Array of Object

List of Reflection-summary objects for each Reflection in the Dremio instance.

---

nextPageToken String

Opaque string to pass for the `pageToken` query parameter in the next request to retrieve the next set of results. If nextPageToken is not included in the response, all available resources have been returned.

Example: CiQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==

---

isCanAlterReflections Boolean

If the current user has project-level privileges to alter Reflections, the value is `true`. Otherwise, the value is `false`.

Example: true

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

createdAt String

Date and time that the Reflection was created, in UTC format.

Example: 2022-07-05T19:19:40.244Z

---

updatedAt String

Date and time that the Reflection was last updated, in UTC format.

Example: 2023-01-13T19:46:01.313Z

---

id String (UUID)

Unique identifier of the Reflection.

Example: 27077c03-ae49-454c-a7bb-a9a8b5eca224

---

reflectionType String

Reflection type. For more information, read [Types of Reflections](/25.x/sonar/reflections/types-and-benefits).

Enum: RAW, AGGREGATION

Example: AGGREGATION

---

name String

User-provided name for the Reflection. For Reflections created in the Dremio UI, if the user did not provide a name, the default values are `Raw Reflection` and `Aggregation Reflection` (automatically assigned based on the Reflection type).

Example: NYC\_taxi\_agg

---

currentSizeBytes Integer

Data size of the latest Reflection job (if one exists), in bytes.

Example: 9272

---

outputRecords Integer

Number of records returned for the latest Reflection.

Example: 51

---

totalSizeBytes Integer

Data size of all Reflection jobs that have not been pruned (if any exist), in bytes.

Example: 9272

---

datasetId String

Unique identifier of the anchor dataset that is associated with the Reflection.

Example: fa7c487f-9550-474e-8a41-4826564c6b09

---

datasetType String

Type for the anchor dataset that is associated with the Reflection. If the anchor dataset is a table, the type is `PHYSICAL_DATASET`. If the anchor dataset is a view, the type is `VIRTUAL_DATASET`.

Enum: PHYSICAL\_DATASET, VIRTUAL\_DATASET

Example: VIRTUAL\_DATASET

---

datasetPath String

Path to the anchor dataset that is associated with the Reflection within Dremio, expressed in an array. The path consists of the source or space, followed by any folder and subfolders, followed by the name of the dataset itself as the last item in the array.

Example: ["Samples","samples.dremio.com","NYC Taxi Trips"]

---

[status](/25.x/reference/api/reflections/reflection-summary#attributes-of-the-status-object) Object

Information about the status of the Reflection.

Example: {\n "configStatus": "OK",\n "refreshStatus": "MANUAL",\n "availabilityStatus": "AVAILABLE",\n "combinedStatus": "CAN\_ACCELERATE",\n "refreshMethod": "FULL",\n "failureCount": 0,\n "lastDataFetchAt": "2023-01-13T19:05:03.532Z",\n "expiresAt": "3022-05-16T19:46:02.342Z",\n "lastRefreshDurationMillis": 46387\n }

---

consideredCount Integer

Number of jobs that considered the Reflection during planning.

Example: 202

---

matchedCount Integer

Number of jobs that matched the Reflection during planning.

Example: 45

---

chosenCount Integer

Number of jobs accelerated by the Reflection.

Example: 5

---

consideredJobsLink String

Link to list of considered jobs for the Reflection.

Example: /jobs?filters=%7B%22cor%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D

---

matchedJobsLink String

Link to list of matched jobs for the Reflection.

Example: /jobs?filters=%7B%22mar%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D

---

chosenJobsLink String

Link to list of chosen jobs for the Reflection.

Example: /jobs?filters=%7B%22chr%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D

---

isArrowCachingEnabled Boolean

If Dremio converts data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, the value is `true`. Otherwise, the value is `false`.

Example: false

---

isCanView Boolean

If you can view Reflections on all datasets of a source, system, space, or folder, the value is `true`. Otherwise, the value is `false`.

Example: true

---

isCanAlter Boolean

If you can create, edit, and view Reflections on all datasets of a source, system, space, or folder, the value is `true`. Otherwise, the value is `false`.

Example: true

---

isEnabled Boolean

If the Reflection is available for accelerating queries, the value is `true`. Otherwise, the value is `false`.

Example: true

#### Attributes of the `status` Object[​](#attributes-of-the-status-object "Direct link to attributes-of-the-status-object")

configStatus String

Status of the Reflection configuration. If the value is `OK`, the Reflection configuration is free of errors. If the value is `INVALID`, the Reflection configuration contains one or more errors.

Enum: OK, INVALID

Example: OK

---

refreshStatus String

Status of the Reflection refresh.

* `GIVEN_UP`: Dremio attempted to refresh the Reflection multiple times, but each attempt has failed and Dremio will not make further attempts.
* `MANUAL`: Refresh period is set to 0, so you must use the Dremio UI to manually refresh the Reflection.
* `RUNNING`: Dremio is currently refreshing the Reflection.
* `SCHEDULED`: The Reflection refreshes according to a schedule.
* `ON_DATA_CHANGES`: All of the Reflection’s underlying tables are in Iceberg format, and the Reflection refreshes automatically if new snapshots are created after an update to the underlying tables.

Enum: GIVEN\_UP, MANUAL, RUNNING, SCHEDULED, ON\_DATA\_CHANGES

Example: MANUAL

---

availabilityStatus String

Status of the Reflection's availability for accelerating queries.

Enum: NONE, INCOMPLETE, EXPIRED, AVAILABLE

Example: AVAILABLE

---

combinedStatus String

Status of the Reflection based on a combination of config, refresh, and availability.

* `CAN_ACCELERATE`: The Reflection is fully functional.
* `CAN_ACCELERATE_WITH_FAILURES`: The most recent refresh failed to obtain a status, but Dremio still has a valid materialization.
* `CANNOT_ACCELERATE_INITIALIZING`: The Reflection is currently being loaded into the materialization cache. During this time, the Reflection is unable to accelerate queries.
* `CANNOT_ACCELERATE_MANUAL`: The Reflection is unable to accelerate any queries, and the `Never Refresh` option is selected for the refresh policy.
* `CANNOT_ACCELERATE_SCHEDULED`: The Reflection is currently unable to accelerate any queries, but it has been scheduled for a refresh at a future time.
* `DISABLED`: The Reflection has been manually disabled.
* `EXPIRED`: The Reflection has expired and cannot be used.
* `FAILED`: The attempt to refresh the Reflection has failed, typically three times in a row. The Reflection is still usable.
* `INVALID`: The Reflection is invalid because the underlying dataset has changed.
* `INCOMPLETE`: One or more pseudo-distributed file system (PDFS) nodes that contain materialized files are down (PFDS is supported for v21 and earlier). Only partial data is available. Configurations that use the Hadoop Distributed File System (HDFS) to store Reflections should not experience incomplete status.
* `REFRESHING`: The Reflection is currently being refreshed.

Example: CAN\_ACCELERATE

---

refreshMethod String

The method used for the most recent refresh of the Reflection. For new Reflections, the value is `NONE` until planned. For more information, read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections).

Enum: NONE, FULL, INCREMENTAL

Example: FULL

---

failureCount Integer

Number of times that an attempt to refresh the Reflection failed.

Example: 0

---

lastFailureMessage String

The error message from the last failed Reflection refresh. If the refresh of a Reflection never fails or succeeds after a failure, this attribute does not appear.

Example: "The Default engine is not online."

---

lastDataFetchAt String

Date and time that the Reflection data was last refreshed, in UTC format. If the Reflection is running, failing, or disabled, the lastDataFetchAt value is `1969-12-31T23:59:59.999Z`.

Example: 2023-01-13T19:05:03.532Z

---

expiresAt String

Date and time that the Reflection expires, in UTC format. If the Reflection is running, failing, or disabled, the expiresAt value is `1969-12-31T23:59:59.999Z`.

Example: 3022-05-16T19:46:02.342Z

---

lastRefreshDurationMillis Integer

Duration of the most recent refresh for the Reflection. In milliseconds.

Example: 46387

## Retrieving a Reflection Summary[​](#retrieving-a-reflection-summary "Direct link to Retrieving a Reflection Summary")

Retrieve a summary of the raw and aggregation Reflections in the Dremio instance.

Method and URL

```
GET /api/v3/reflection-summary
```

### Parameters[​](#parameters "Direct link to Parameters")

pageToken Query   String   Optional

Token for retrieving the next page of Reflection summary results. If the Dremio instance has more Reflection summary results than the maximum per page (default 50), the response includes a nextPageToken after the data array. Use the nextPageToken value in your request URL as the pageToken value. Do not change any other query parameters included in the request URL when you use pageToken. For more information, read [pageToken Query Parameter](/25.x/reference/api/#pagetoken-query-parameter).

---

maxResults Query   Integer   Optional

Maximum number of Reflection summaries to return in the response. Maximum valid value is `100`. Default is `50`. For more information, read [maxResults Query Parameter](/25.x/reference/api/#maxresults-query-parameter).

---

filter Query   Object   Optional

Filters for Reflection name, dataset name, availability status, and refresh status. Value is a URL-encoded string that represents a JSON object. The JSON object specifies the attributes to filter on and the values to match for each attribute. Available filter attributes:

* reflectionType: `RAW`, `AGGREGATION` (array of string)
* refreshStatus: `GIVEN_UP`, `MANUAL`, `RUNNING`, `SCHEDULED`, `ON_DATA_CHANGES` (array of string)
* availabilityStatus: `NONE`, `INCOMPLETE`, `EXPIRED`, `AVAILABLE` (array of string)
* configStatus: `OK`, `INVALID` (array of string)
* enabledFlag: `true`, `false` (Boolean)
* reflectionNameOrDatasetPath: full or partial Reflection name or dataset path; case insensitive (string)
* reflectionIds: IDs of Reflections to retrieve (array of string); must be used alone, with no other filters or query parameters

For more information, read [filter Query Parameter](/25.x/reference/api/#filter-query-parameter).

---

orderBy Query   String   Optional

Organize the response in ascending (default) or descending order by reflectionName, datasetName, or reflectionType. To specify descending order, precede the orderBy value with a `-` character. For more information, read [orderBy Query Parameter](/25.x/reference/api/#orderby-query-parameter).

Example Request Without Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary'  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header "Content-Type: application/json"
```

Example Response

```
{  
  "data": [  
    {  
      "createdAt": "2023-01-13T19:46:01.313Z",  
      "updatedAt": "2023-01-13T19:46:01.313Z",  
      "id": "27077c03-ae49-454c-a7bb-a9a8b5eca224",  
      "reflectionType": "AGGREGATION",  
      "name": "NYC_taxi_agg",  
      "currentSizeBytes": 9272,  
      "outputRecords": 51,  
      "totalSizeBytes": 9272,  
      "datasetId": "fa7c487f-9550-474e-8a41-4826564c6b09",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.342Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 46387  
      },  
      "consideredCount": 202,  
      "matchedCount": 45,  
      "chosenCount": 5,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-26T23:27:04.281Z",  
      "updatedAt": "2023-01-26T23:27:04.281Z",  
      "id": "0e3d765a-2291-4a04-81eb-2daf5477cc7d",  
      "reflectionType": "RAW",  
      "name": "Raw Reflection",  
      "currentSizeBytes": 0,  
      "outputRecords": -1,  
      "totalSizeBytes": 0,  
      "datasetId": "acdad4be-7049-47e4-b616-b471c5b3c60c",  
      "datasetType": "PHYSICAL_DATASET",  
      "datasetPath": [  
        "@dremio",  
        "test"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "GIVEN_UP",  
        "availabilityStatus": "NONE",  
        "combinedStatus": "FAILED",  
        "refreshMethod": "NONE",  
        "failureCount": 3,  
        "lastDataFetchAt": null,  
        "expiresAt": null,  
        "lastRefreshDurationMillis": -1  
      },  
      "consideredCount": 0,  
      "matchedCount": 0,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:19.030Z",  
      "updatedAt": "2023-01-13T19:50:19.030Z",  
      "id": "8eec62d7-3419-4cf3-997d-0a153d81ed8a",  
      "reflectionType": "AGGREGATION",  
      "name": "dataset991_agg991",  
      "currentSizeBytes": 9273,  
      "outputRecords": 51,  
      "totalSizeBytes": 9273,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.342Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 11697  
      },  
      "consideredCount": 60,  
      "matchedCount": 9,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:17.714Z",  
      "updatedAt": "2023-01-13T19:50:17.714Z",  
      "id": "167428eb-7936-4ea2-a1fb-23b1ac6e9454",  
      "reflectionType": "RAW",  
      "name": "dataset991_raw991",  
      "currentSizeBytes": 818790,  
      "outputRecords": 29467,  
      "totalSizeBytes": 818790,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.747Z",  
        "expiresAt": "3022-05-16T19:46:02.747Z",  
        "lastRefreshDurationMillis": 16666  
      },  
      "consideredCount": 54,  
      "matchedCount": 37,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    }  
  ],  
  "nextPageToken": "CiQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==",  
  "isCanAlterReflections": true  
}
```

This endpoint supports [query parameters](#parameters) that you can add to the request URL to include only specific types of Reflections in the Reflection summary, specify the maximum number of results to return, and sort the response to list Reflections in ascending or descending order.

For example, to order the Reflections within the summary in ascending order by reflectionName, add `?orderBy=reflectionName` to the request URL. For descending order, add a `-` character before the attribute name: `?orderBy=-reflectionName`.

In the same request, you can add the `filter` query parameter to retrieve only the raw Reflections that are refreshed manually or by schedule, are enabled, and apply to datasets with `samples.dremio.com` in their paths. The JSON object for such a filter would look like this:

Example JSON Object for Filter

```
{  
  "reflectionType": ["RAW"],  
  "refreshStatus": ["MANUAL","SCHEDULED"],  
  "enabledFlag": true,  
  "reflectionNameOrDatasetPath": "samples.dremio.com"  
}
```

However, to use the JSON object in the request URL, you must convert it to URL-encoded JSON, which looks like this:

Example JSON Object in URL-Encoded JSON

```
%7B%0A%20%20%22reflectionType%22%3A%20%5B%22RAW%22%5D%2C%0A%20%20%22refreshStatus%22%3A%20%5B%22MANUAL%22%2C%22SCHEDULED%22%5D%2C%0A%20%20%22enabledFlag%22%3A%20true%2C%0A%20%20%22reflectionNameOrDatasetPath%22%3A%20%22samples.dremio.com%22%0A%7D
```

Here is an example request URL that includes both the `orderBy` and `filter` query parameters:

Example Request with orderBy and filter Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?orderBy=reflectionName&filter=%7B%0A%20%20%22reflectionType%22%3A%20%5B%22RAW%22%5D%2C%0A%20%20%22refreshStatus%22%3A%20%5B%22MANUAL%22%2C%22SCHEDULED%22%5D%2C%0A%20%20%22enabledFlag%22%3A%20true%2C%0A%20%20%22reflectionNameOrDatasetPath%22%3A%20%22samples.dremio.com%22%0A%7D' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

For this request, the Reflection summary in the response will include only raw Reflections that are refreshed manually or by schedule, are enabled, and apply to datasets with `samples.dremio.com` in their paths, and the Reflections will be listed in ascending order by reflectionName.

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Recommendations](/25.x/reference/api/reflections/reflection-recommendations)[Next

Role](/25.x/reference/api/roles/)

* [Reflection Summary Attributes](#reflection-summary-attributes)
* [Retrieving a Reflection Summary](#retrieving-a-reflection-summary)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/source/

Version: 25.x

On this page

# Source

Use the Catalog API to retrieve information about [sources](/25.x/sonar/data-sources/) and the child objects they contain, as well as to create, update, and delete sources.

note

Dremio supports a number of different source types. Each source type has the same parameters *except* for the parameters within the `config` object. The available parameters in the `config` object are different for each source type. The examples on this page use an Amazon S3 source to demonstrate the available requests and responses for sources. Read [Source Configuration](/25.x/reference/api/catalog/source/container-source-config) for information about the available parameters in the `config` object for each supported source type.

Source Object

```
{  
  "entityType": "source",  
  "config": {  
    "accessKey": "EXAMPLE78HT89VS4YJEL",  
    "accessSecret": "$DREMIO_EXISTING_VALUE$",  
    "secure": true,  
    "rootPath": "/",  
    "enableAsync": true,  
    "compatibilityMode": false,  
    "isCachingEnabled": true,  
    "maxCacheSpacePct": 100,  
    "whitelistedBuckets": [  
      "archive.dremio.com",  
      "logs_east-1",  
      "logs_west-1"  
    ],  
    "requesterPays": false,  
    "enableFileStatusCheck": true,  
    "defaultCtasFormat": "ICEBERG",  
    "isPartitionInferenceEnabled": false,  
    "credentialType": "ACCESS_KEY"  
  },  
  "id": "2b1be882-7012-4a99-8d6c-82e32e4562e4",  
  "tag": "T0/Zr1FOY3A=",  
  "type": "S3",  
  "name": "AWS-S3_testgroup",  
  "createdAt": "2023-02-17T14:32:20.640Z",  
  "metadataPolicy": {  
    "authTTLMs": 86400000,  
    "namesRefreshMs": 3600000,  
    "datasetRefreshAfterMs": 3600000,  
    "datasetExpireAfterMs": 10800000,  
    "datasetUpdateMode": "PREFETCH_QUERIED",  
    "deleteUnavailableDatasets": true,  
    "autoPromoteDatasets": false  
  },  
  "accelerationGracePeriodMs": 10800000,  
  "accelerationRefreshPeriodMs": 3600000,  
  "accelerationNeverExpire": false,  
  "accelerationNeverRefresh": false,  
  "accelerationActivePolicyType": "NEVER",  
  "accelerationRefreshSchedule": "",  
  "children": [  
    {  
      "id": "dremio:/AWS-S3_testgroup/archive.dremio.com",  
      "path": [  
        "AWS-S3_testgroup",  
        "archive.dremio.com"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_east-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_east-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_west-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_west-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    }  
  ],  
  "allowCrossSourceSelection": false,  
  "disableMetadataValidityCheck": false,  
  "accessControlList": {  
    "users": [  
      {  
        "id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65",  
        "permissions": [  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "c45ff4d8-e910-4f85-89db-9b8c29188a56",  
        "permissions": [  
          "ALTER",  
          "CREATE_TABLE",  
          "DROP",  
          "INSERT",  
          "DELETE",  
          "UPDATE",  
          "TRUNCATE",  
          "VIEW_REFLECTION",  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "MANAGE_GRANTS",  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "checkTableAuthorizer": true,  
  "owner": {  
    "ownerId": "4fb93af3-acc2-4b10-ad4b-64dd7070d365",  
    "ownerType": "USER"  
  },  
  "accelerationRefreshOnDataChanges": false  
}
```

## Source Attributes[​](#source-attributes "Direct link to Source Attributes")

entityType String

Type of the catalog object. For sources, the entityType is `source`.

Example: source

---

[config](/25.x/reference/api/catalog/source/#attributes-of-the-config-object) Object

Configuration settings for the source. The available parameters in the config object are different for different source types. For more information, read [Source Configuration](/25.x/reference/api/catalog/source/container-source-config).

Example: {"accessKey": "EXAMPLE78HT89VS4YJEL","accessSecret": "$DREMIO\_EXISTING\_VALUE$","secure": true,"rootPath": "/","enableAsync": true,"compatibilityMode": false,"isCachingEnabled": true,"maxCacheSpacePct": 100,"requesterPays": false,"enableFileStatusCheck": true,"defaultCtasFormat": "ICEBERG","isPartitionInferenceEnabled": false,"credentialType": "ACCESS\_KEY"}

---

id String (UUID)

Unique identifier of the source.

Example: 2b1be882-7012-4a99-8d6c-82e32e4562e4

---

tag String

Unique identifier of the version of the source. Dremio changes the tag whenever the source changes and uses the tag to ensure that PUT requests apply to the most recent version of the source.

Example: T0/Zr1FOY3A=

---

type String

Type of source.

Enum: ADL, ADX, AMAZONELASTIC, AWSGLUE, AZURE\_STORAGE, DB2, DREMIOTODREMIO, ELASTIC, GCS, HDFS, HIVE, HIVE3, MONGO, MSSQL, MYSQL, NAS, NESSIE, ORACLE, POSTGRES, REDSHIFT, S3, SNOWFLAKE, SYNAPSE, TERADATA

Example: S3

---

name String

Name of the source.

Example: AWS-S3\_testgroup

---

createdAt String

Date and time that the source was created, in UTC format.

Example: 2023-02-17T14:32:20.640Z

---

[metadataPolicy](/25.x/reference/api/catalog/source/#attributes-of-the-metadatapolicy-object) Object

Information about the metadata policy for the source.

Example: {"authTTLMs": 86400000,"namesRefreshMs": 3600000,"datasetRefreshAfterMs": 3600000,"datasetExpireAfterMs": 10800000,"datasetUpdateMode": "PREFETCH\_QUERIED","deleteUnavailableDatasets": true,"autoPromoteDatasets": false}

---

accelerationGracePeriodMs Integer

Maximum age allowed for Reflection data used to accelerate queries on datasets in the source, in milliseconds. Default is `0`. For more information, read [Setting the Expiration Policy for Reflections](/25.x/sonar/reflections/setting-expiration-policy).

Example: 10800000

---

accelerationRefreshPeriodMs Integer

Refresh period for the data in all Reflections on datasets in the source, in milliseconds. Default is `0`.

Example: 3600000

---

accelerationNeverExpire Boolean

Option to set an expiration for Reflections. Default setting is `false`. Set to `true` to prevent Reflections from expiring and to override the `accelerationGracePeriodMs` setting.

Example: false

---

accelerationNeverRefresh Boolean

Option to set a refresh for Reflections. Default setting is `false`. Set to `true` to prevent Reflections from refreshing and to override the `accelerationRefreshPeriodMs` setting.

---

accelerationActivePolicyType String

Option to set the policy for refreshing Reflections that are defined on the source. For this option to take effect, `accelerationNeverRefresh` must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: The Reflections are refreshed at the end of every period that is defined by accelerationRefreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by accelerationRefreshSchedule.

---

accelerationRefreshSchedule String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source are refreshed.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:
`0 0 0 * * ?` : Refreshes every day at midnight.
`0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
`0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

[children](/25.x/reference/api/catalog/source/#attributes-of-objects-in-the-children-array) Array of Object

Information about each catalog object in the source.

Example: [{"id": "dremio:/AWS-S3\_testgroup/archive.dremio.com","path": ["AWS-S3\_testgroup","archive.dremio.com"],"type": "CONTAINER","containerType": "FOLDER"},{"id": "dremio:/AWS-S3\_testgroup/logs\_east-1","path": ["AWS-S3\_testgroup","logs\_east-1"],"type": "CONTAINER","containerType": "FOLDER"},{"id": "dremio:/AWS-S3\_testgroup/logs\_west-1","path": ["AWS-S3\_testgroup","logs\_west-1"],"type": "CONTAINER","containerType": "FOLDER"}]

---

allowCrossSourceSelection Boolean

If the source is available for queries that can select from multiple sources, set to `true`. Otherwise, set to `false` (default).

Example: false

---

disableMetadataValidityCheck Boolean

To disable the check for expired metadata and require users to refresh manually, set to `true`. Otherwise, set to `false` (default).

note

The disableMetadataValidityCheck attribute is not supported by default. Contact Dremio Support to enable it.

Example: false

---

[accessControlList](/25.x/reference/api/catalog/source/#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the source and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if source-specific access control privileges are not set.

Example: {"users": [{"id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65","permissions": ["VIEW\_REFLECTION","SELECT" ]}],"roles": [{"id": "c45ff4d8-e910-4f85-89db-9b8c29188a56","permissions": ["ALTER","CREATE\_TABLE","DROP","INSERT","DELETE","UPDATE","TRUNCATE","VIEW\_REFLECTION","ALTER\_REFLECTION","MODIFY","MANAGE\_GRANTS","SELECT"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the source. Empty unless the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

checkTableAuthorizer Boolean

Not used. Has the value `true`.

Example: true

---

[owner](/25.x/reference/api/catalog/source/#attributes-of-the-owner-object) Object

Information about the source's owner.

Example: {"ownerId": "4fb93af3-acc2-4b10-ad4b-64dd7070d365","ownerType": "USER"}

---

accelerationRefreshOnDataChanges Boolean

If Reflections automatically refresh for underlying tables that are in Iceberg format when new snapshots are created after an update, `true`. Otherwise, `false`.

#### Attributes of the `config` Object[​](#attributes-of-the-config-object "Direct link to attributes-of-the-config-object")

The `config` object attributes vary for different source types. Read [Source Configuration](/25.x/reference/api/catalog/source/container-source-config) for information about the available parameters in the `config` object for each supported source type.

#### Attributes of the `metadataPolicy` Object[​](#attributes-of-the-metadatapolicy-object "Direct link to attributes-of-the-metadatapolicy-object")

authTTLMs Integer

Length of time to cache the privileges that the user has on the source, in milliseconds. For example, if authTTLMs is set to `28800000` (8 hours), Dremio checks the user's permission status once every 8 hours. Default is `86400000` (24 hours). Minimum is `60000` (1 minute).

Example: 86400000

---

namesRefreshMs Integer

How often the source is refreshed, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 3600000

---

datasetRefreshAfterMs Integer

How often the metadata in the source's datasets is refreshed, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 3600000

---

datasetExpireAfterMs Integer

Maximum age allowed for the metadata in the source's datasets, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 10800000

---

datasetUpdateMode String

Approach Dremio uses for updating the metadata when updating datasets in the source.

* `PREFETCH`: (deprecated) Dremio updates details for all datasets in a source.
* `PREFETCH_QUERIED`: Dremio updates details for previously queried objects in a source.

Example: PREFETCH\_QUERIED

---

deleteUnavailableDatasets Boolean

If Dremio removes dataset definitions from the source when the underlying data is unavailable, set to `true` (default). Otherwise, set to `false`.

Example: true

---

autoPromoteDatasets Boolean

If Dremio automatically formats files into tables when a user issues a query, set to `true`. Otherwise, set to `false` (default). Available only for datalake sources, such as Amazon S3 and Hive.

Example: false

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String

Unique identifier of the child catalog object. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: dremio:/AWS-S3\_testgroup/archive.dremio.com

---

path Array of String

Path to the child catalog object within the source, expressed as an array. The path consists of the source, followed by the name of the folder, file, or dataset itself as the last item in the array.

Example: ["AWS-S3\_testgroup","archive.dremio.com"]

---

type String

Type of the catalog object.

Enum: CONTAINER, FILE, DATASET

Example: CONTAINER

---

containerType String

For catalog objects with the type `CONTAINER`, the containerType is `FOLDER`.

Example: FOLDER

---

datasetType String

For catalog objects with the type `DATASET`, the type of dataset. If the dataset is from an external source such as PostgreSQL, the datasetType is `DIRECT`. For tables, the datasetType is `PROMOTED`. For views, the datasetType is `VIRTUAL`.

Enum: DIRECT, PROMOTED, VIRTUAL

Example: VIRTUAL

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/source/#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the source and the specific privileges each user has.

Example: [{"id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65","permissions": ["VIEW\_REFLECTION","SELECT"]}]

---

[roles](/25.x/reference/api/catalog/source/#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the source and the specific privileges each role has.

Example: [{"id": "c45ff4d8-e910-4f85-89db-9b8c29188a56","permissions": ["ALTER", "CREATE\_TABLE", "DROP", "INSERT", "DELETE", "UPDATE", "TRUNCATE", "VIEW\_REFLECTION", "ALTER\_REFLECTION", "MODIFY", "MANAGE\_GRANTS", "SELECT"]}]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the source's owner.

Example: 4fb93af3-acc2-4b10-ad4b-64dd7070d365

---

ownerType String

Type of owner of the source.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String (UUID)

Enterprise only. Unique identifier of the user or role with access to the source.

Example: ebe519ab-20e3-43ff-9b4c-b3ec590c7e65

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the source. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["VIEW\_REFLECTION","SELECT"]

## Creating a Source[​](#creating-a-source "Direct link to Creating a Source")

Create a new source.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object to create. For sources, the entityType is `source`.

Example: source

---

[config](/25.x/reference/api/catalog/source/#parameters-of-the-config-object) Body   Object

Configuration settings for the source. The available parameters in the config object are different for different source types. For more information, read [Source Configuration](/25.x/reference/api/catalog/source/container-source-config).

Example: {"accessKey": "EXAMPLE78HT89VS4YJEL","accessSecret": "EXAMPLEe3bcpKnAwgJ2WBpX8d9kEdhMz24guiR7L","secure": true,"rootPath": "/","enableAsync": true,"compatibilityMode": false,"isCachingEnabled": true,"maxCacheSpacePct": 100,"requesterPays": false,"enableFileStatusCheck": true,"defaultCtasFormat": "ICEBERG","isPartitionInferenceEnabled": false,"credentialType": "ACCESS\_KEY"}

---

type Body   String

Type of source to create.

Enum: ADL, ADX, AMAZONELASTIC, AWSGLUE, AZURE\_STORAGE, DB2, DREMIOTODREMIO, ELASTIC, GCS, HDFS, HIVE, HIVE3, MONGO, MSSQL, MYSQL, NAS, NESSIE, ORACLE, POSTGRES, REDSHIFT, S3, SNOWFLAKE, SYNAPSE, TERADATA

Example: S3

---

name Body   String

Name for the source. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: AWS-S3\_testgroup

---

[metadataPolicy](/25.x/reference/api/catalog/source/#parameters-of-the-metadatapolicy-object) Body   Object   Optional

Information about the metadata policy for the source.

Example: {"authTTLMs": 86400000,"namesRefreshMs": 3600000,"datasetRefreshAfterMs": 3600000,"datasetExpireAfterMs": 10800000,"datasetUpdateMode": "PREFETCH\_QUERIED","deleteUnavailableDatasets": true,"autoPromoteDatasets": false}

---

accelerationGracePeriodMs Body   Integer   Optional

Maximum age to allow for Reflection data used to accelerate queries on datasets in the source, in milliseconds. Default is `0`. For more information, read [Setting the Expiration Policy for Reflections](/25.x/sonar/reflections/setting-expiration-policy).

Example: 10800000

---

accelerationRefreshPeriodMs Body   Integer   Optional

Refresh period to use for the data in all Reflections on datasets in the source, in milliseconds. Optional if you set accelerationActivePolicyType to `PERIOD`. The default setting is `3600000` milliseconds or one hour.

Example: 3600000

---

accelerationNeverExpire Body   Boolean   Optional

Option to set an expiration for Reflections. Default setting is `false`. Set to `true` to prevent Reflections from expiring and to override the `accelerationGracePeriodMs` setting.

Example: false

---

accelerationNeverRefresh Body   Boolean   Optional

Option to set a refresh for Reflections. Default setting is `false`. Set to `true` to prevent Reflections from refreshing and to override the `accelerationRefreshPeriodMs` setting.

---

accelerationActivePolicyType String

Option to set the policy for refreshing Reflections that are defined on the source. For this option to take effect, `accelerationNeverRefresh` must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: Default. The Reflections are refreshed at the end of every period that is defined by accelerationRefreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by accelerationRefreshSchedule.

---

accelerationRefreshSchedule String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source are refreshed. Optional if you set accelerationActivePolicyType to `SCHEDULE`. The default accelerationRefreshSchedule setting is to refresh every day at 8:00 a.m.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:
`0 0 0 * * ?` : Refreshes every day at midnight.
`0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
`0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

allowCrossSourceSelection Body   Boolean   Optional

If the source should be available for queries that can select from multiple sources, set to `true`. Otherwise, set to `false` (default).

Example: false

---

disableMetadataValidityCheck Body   Boolean   Optional

To disable the check for expired metadata and require users to refresh manually, set to `true`. Otherwise, set to `false` (default).

note

The disableMetadataValidityCheck parameter is not supported by default. Contact Dremio Support to enable it.

Example: false

---

accelerationRefreshOnDataChanges Body   Boolean

To refresh Reflections on underlying tables that are in Iceberg format in the source when new snapshots are created after an update, `true`. Otherwise, `false`. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency. For this option to take effect, the source must support Iceberg table format, the accelerationNeverRefresh parameter must be set to `false`, and the accelerationActivePolicyType parameter must be set to either `PERIOD` or `SCHEDULE`.

---

[accessControlList](/25.x/reference/api/catalog/source/#attributes-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Information about users and roles that should have access to the source and the specific privileges each user or role should have. May include an array of users, an array of roles, or both, depending on the configured access and privileges.

Example: {"users": [{"id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65","permissions": [ "VIEW\_REFLECTION","SELECT"]}],"roles": [{"id": "c45ff4d8-e910-4f85-89db-9b8c29188a56","permissions": ["ALTER","CREATE\_TABLE","DROP","INSERT","DELETE","UPDATE","TRUNCATE","VIEW\_REFLECTION","ALTER\_REFLECTION","MODIFY","MANAGE\_GRANTS","SELECT"]}]}

#### Parameters of the `config` Object[​](#parameters-of-the-config-object "Direct link to parameters-of-the-config-object")

The `config` object's parameters vary for different source types. Read [Source Configuration](/25.x/reference/api/catalog/source/container-source-config) for information about the available parameters in the `config` object for each supported source type.

#### Parameters of the `metadataPolicy` Object[​](#parameters-of-the-metadatapolicy-object "Direct link to parameters-of-the-metadatapolicy-object")

authTTLMs Body   Integer

Length of time to cache the privileges that the user has on the source, in milliseconds. For example, if authTTLMs is set to `28800000` (8 hours), Dremio checks the user's permission status once every 8 hours. Default is `86400000` (24 hours). Minimum is `60000` (1 minute).

Example: 86400000

---

namesRefreshMs Body   Integer   Optional

How often the source should be refreshed, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 3600000

---

datasetRefreshAfterMs Body   Integer   Optional

How often the metadata in the source's datasets should be refreshed, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 3600000

---

datasetExpireAfterMs Body   Integer   Optional

Maximum age to allow for the metadata in the source's datasets, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 10800000

---

datasetUpdateMode Body   String   Optional

Approach for Dremio to take for updating the metadata when updating datasets in the source.

* `PREFETCH`: (deprecated) Dremio updates details for all datasets in a source.
* `PREFETCH_QUERIED`: Dremio updates details for previously queried objects in a source.

Example: PREFETCH\_QUERIED

---

deleteUnavailableDatasets Body   Boolean   Optional

If Dremio should remove dataset definitions from the source when the underlying data is unavailable, set to `true` (default). Otherwise, set to `false`.

Example: true

---

autoPromoteDatasets Body   Boolean   Optional

If Dremio should automatically format files into tables using default options when users issue queries, set to `true`. Otherwise, set to `false` (default). Available only for datalake sources, such as Amazon S3 and Hive.

Example: false

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/source/#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the source and the specific privileges each user should have.

Example: [{"id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65", "permissions": ["VIEW\_REFLECTION","SELECT"]}]

---

[roles](/25.x/reference/api/catalog/source/#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

List of roles whose members should have access to the source and the specific privileges each role should have.

Example: [{"id": "c45ff4d8-e910-4f85-89db-9b8c29188a56", "permissions": ["ALTER","CREATE\_TABLE","DROP","INSERT","DELETE","UPDATE","TRUNCATE","VIEW\_REFLECTION","ALTER\_REFLECTION","MODIFY","MANAGE\_GRANTS","SELECT"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String (UUID)   Optional

Unique identifier of the user or role who should have access to the source.

Example: ebe519ab-20e3-43ff-9b4c-b3ec590c7e65

---

permissions Body   Array of String   Optional

List of privileges the user or role should have on the source. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["VIEW\_REFLECTION","SELECT"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "source",  
  "config": {  
    "accessKey": "EXAMPLE78HT89VS4YJEL",  
    "accessSecret": "EXAMPLEe3bcpKnAwgJ2WBpX8d9kEdhMz24guiR7L",  
    "secure": true,  
    "rootPath": "/",  
    "enableAsync": true,  
    "compatibilityMode": false,  
    "isCachingEnabled": true,  
    "maxCacheSpacePct": 100,  
    "whitelistedBuckets": [  
      "archive.dremio.com",  
      "logs_east-1",  
      "logs_west-1"  
    ],  
    "requesterPays": false,  
    "enableFileStatusCheck": true,  
    "defaultCtasFormat": "ICEBERG",  
    "isPartitionInferenceEnabled": false,  
    "credentialType": "ACCESS_KEY"  
  },  
  "type": "S3",  
  "name": "AWS-S3_testgroup",  
  "metadataPolicy": {  
    "authTTLMs": 86400000,  
    "namesRefreshMs": 3600000,  
    "datasetRefreshAfterMs": 3600000,  
    "datasetExpireAfterMs": 10800000,  
    "datasetUpdateMode": "PREFETCH_QUERIED",  
    "deleteUnavailableDatasets": true,  
    "autoPromoteDatasets": false  
  },  
  "accelerationGracePeriodMs": 10800000,  
  "accelerationRefreshPeriodMs": 3600000,  
  "accelerationNeverExpire": false,  
  "accelerationNeverRefresh": false,  
  "allowCrossSourceSelection": false,  
  "disableMetadataValidityCheck": false,  
  "accessControlList": {  
    "users": [  
      {  
        "id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65",  
        "permissions": [  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "c45ff4d8-e910-4f85-89db-9b8c29188a56",  
        "permissions": [  
          "ALTER",  
          "CREATE_TABLE",  
          "DROP",  
          "INSERT",  
          "DELETE",  
          "UPDATE",  
          "TRUNCATE",  
          "VIEW_REFLECTION",  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "MANAGE_GRANTS",  
          "SELECT"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "source",  
  "config": {  
    "accessKey": "EXAMPLE78HT89VS4YJEL",  
    "accessSecret": "$DREMIO_EXISTING_VALUE$",  
    "secure": true,  
    "rootPath": "/",  
    "enableAsync": true,  
    "compatibilityMode": false,  
    "isCachingEnabled": true,  
    "maxCacheSpacePct": 100,  
    "whitelistedBuckets": [  
      "archive.dremio.com",  
      "logs_east-1",  
      "logs_west-1"  
    ],  
    "requesterPays": false,  
    "enableFileStatusCheck": true,  
    "defaultCtasFormat": "ICEBERG",  
    "isPartitionInferenceEnabled": false,  
    "credentialType": "ACCESS_KEY"  
  },  
  "state": {  
    "status": "good",  
    "suggestedUserAction": "",  
    "messages": []  
  },  
  "id": "2b1be882-7012-4a99-8d6c-82e32e4562e4",  
  "tag": "T0/Zr1FOY3A=",  
  "type": "S3",  
  "name": "AWS-S3_testgroup",  
  "createdAt": "2023-02-17T14:32:20.640Z",  
  "metadataPolicy": {  
    "authTTLMs": 86400000,  
    "namesRefreshMs": 3600000,  
    "datasetRefreshAfterMs": 3600000,  
    "datasetExpireAfterMs": 10800000,  
    "datasetUpdateMode": "PREFETCH_QUERIED",  
    "deleteUnavailableDatasets": true,  
    "autoPromoteDatasets": false  
  },  
  "accelerationGracePeriodMs": 10800000,  
  "accelerationRefreshPeriodMs": 3600000,  
  "accelerationActivePolicyType": "PERIOD",  
  "accelerationNeverExpire": false,  
  "accelerationNeverRefresh": false,  
  "children": [  
    {  
      "id": "dremio:/AWS-S3_testgroup/archive.dremio.com",  
      "path": [  
        "AWS-S3_testgroup",  
        "archive.dremio.com"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_east-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_east-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_west-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_west-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    }  
  ],  
  "allowCrossSourceSelection": false,  
  "disableMetadataValidityCheck": false,  
  "accessControlList": {  
    "users": [  
      {  
        "id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65",  
        "permissions": [  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "c45ff4d8-e910-4f85-89db-9b8c29188a56",  
        "permissions": [  
          "ALTER",  
          "CREATE_TABLE",  
          "DROP",  
          "INSERT",  
          "DELETE",  
          "UPDATE",  
          "TRUNCATE",  
          "VIEW_REFLECTION",  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "MANAGE_GRANTS",  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "checkTableAuthorizer": true,  
  "owner": {  
    "ownerId": "4fb93af3-acc2-4b10-ad4b-64dd7070d365",  
    "ownerType": "USER"  
  },  
  "accelerationRefreshOnDataChanges": false  
}
```

When you use the Catalog API to create a new source, the response includes a `state` object that describes the status of the source as shown in the example response above. The `state` object contains the following attributes:

status String

Status of the created source.

Enum: good, bad, warn

Example: good

---

suggestedUserAction String

Recommended action to take, if any, based on the status of the created source.

---

messages Array of String

Status message, if any, for the created source.

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Retrieving a Source by ID[​](#retrieving-a-source-by-id "Direct link to Retrieving a Source by ID")

Retrieve a source and information about its contents by specifying the source's ID.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the source that you want to retrieve.

Example: 2b1be882-7012-4a99-8d6c-82e32e4562e4

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

**NOTE:** The maxChildren query parameter is not supported for filesystem sources.

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the source has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

**NOTE:** Dremio ignores the pageToken query parameter for filesystem sources.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/2b1be882-7012-4a99-8d6c-82e32e4562e4' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "source",  
  "config": {  
    "accessKey": "EXAMPLE78HT89VS4YJEL",  
    "accessSecret": "$DREMIO_EXISTING_VALUE$",  
    "secure": true,  
    "rootPath": "/",  
    "enableAsync": true,  
    "compatibilityMode": false,  
    "isCachingEnabled": true,  
    "maxCacheSpacePct": 100,  
    "whitelistedBuckets": [  
      "archive.dremio.com",  
      "logs_east-1",  
      "logs_west-1"  
    ],  
    "requesterPays": false,  
    "enableFileStatusCheck": true,  
    "defaultCtasFormat": "ICEBERG",  
    "isPartitionInferenceEnabled": false,  
    "credentialType": "ACCESS_KEY"  
  },  
  "id": "2b1be882-7012-4a99-8d6c-82e32e4562e4",  
  "tag": "T0/Zr1FOY3A=",  
  "type": "S3",  
  "name": "AWS-S3_testgroup",  
  "createdAt": "2023-02-17T14:32:20.640Z",  
  "metadataPolicy": {  
    "authTTLMs": 86400000,  
    "namesRefreshMs": 3600000,  
    "datasetRefreshAfterMs": 3600000,  
    "datasetExpireAfterMs": 10800000,  
    "datasetUpdateMode": "PREFETCH_QUERIED",  
    "deleteUnavailableDatasets": true,  
    "autoPromoteDatasets": false  
  },  
  "accelerationGracePeriodMs": 10800000,  
  "accelerationRefreshPeriodMs": 3600000,  
  "accelerationActivePolicyType": "PERIOD",  
  "accelerationNeverExpire": false,  
  "accelerationNeverRefresh": false,  
  "children": [  
    {  
      "id": "dremio:/AWS-S3_testgroup/archive.dremio.com",  
      "path": [  
        "AWS-S3_testgroup",  
        "archive.dremio.com"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_east-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_east-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_west-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_west-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    }  
  ],  
  "allowCrossSourceSelection": false,  
  "disableMetadataValidityCheck": false,  
  "accessControlList": {  
    "users": [  
      {  
        "id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65",  
        "permissions": [  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "c45ff4d8-e910-4f85-89db-9b8c29188a56",  
        "permissions": [  
          "ALTER",  
          "CREATE_TABLE",  
          "DROP",  
          "INSERT",  
          "DELETE",  
          "UPDATE",  
          "TRUNCATE",  
          "VIEW_REFLECTION",  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "MANAGE_GRANTS",  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "checkTableAuthorizer": true,  
  "owner": {  
    "ownerId": "4fb93af3-acc2-4b10-ad4b-64dd7070d365",  
    "ownerType": "USER"  
  },  
  "accelerationRefreshOnDataChanges": false  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Source by Path[​](#retrieving-a-source-by-path "Direct link to Retrieving a Source by Path")

Retrieve a source and information about its contents by specifying the source's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Name of the source that you want to retrieve. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: AWS-S3\_testgroup

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam1) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

**NOTE:** The maxChildren query parameter is not supported for filesystem sources.

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam1): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the source has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

**NOTE:** Dremio ignores the pageToken query parameter for filesystem sources.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/AWS-S3_testgroup' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "source",  
  "config": {  
    "accessKey": "EXAMPLE78HT89VS4YJEL",  
    "accessSecret": "$DREMIO_EXISTING_VALUE$",  
    "secure": true,  
    "rootPath": "/",  
    "enableAsync": true,  
    "compatibilityMode": false,  
    "isCachingEnabled": true,  
    "maxCacheSpacePct": 100,  
    "whitelistedBuckets": [  
      "archive.dremio.com",  
      "logs_east-1",  
      "logs_west-1"  
    ],  
    "requesterPays": false,  
    "enableFileStatusCheck": true,  
    "defaultCtasFormat": "ICEBERG",  
    "isPartitionInferenceEnabled": false,  
    "credentialType": "ACCESS_KEY"  
  },  
  "id": "2b1be882-7012-4a99-8d6c-82e32e4562e4",  
  "tag": "T0/Zr1FOY3A=",  
  "type": "S3",  
  "name": "AWS-S3_testgroup",  
  "createdAt": "2023-02-17T14:32:20.640Z",  
  "metadataPolicy": {  
    "authTTLMs": 86400000,  
    "namesRefreshMs": 3600000,  
    "datasetRefreshAfterMs": 3600000,  
    "datasetExpireAfterMs": 10800000,  
    "datasetUpdateMode": "PREFETCH_QUERIED",  
    "deleteUnavailableDatasets": true,  
    "autoPromoteDatasets": false  
  },  
  "accelerationGracePeriodMs": 10800000,  
  "accelerationRefreshPeriodMs": 3600000,  
  "accelerationActivePolicyType": "PERIOD",  
  "accelerationNeverExpire": false,  
  "accelerationNeverRefresh": false,  
  "children": [  
    {  
      "id": "dremio:/AWS-S3_testgroup/archive.dremio.com",  
      "path": [  
        "AWS-S3_testgroup",  
        "archive.dremio.com"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_east-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_east-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_west-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_west-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    }  
  ],  
  "allowCrossSourceSelection": false,  
  "disableMetadataValidityCheck": false,  
  "accessControlList": {  
    "users": [  
      {  
        "id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65",  
        "permissions": [  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "c45ff4d8-e910-4f85-89db-9b8c29188a56",  
        "permissions": [  
          "ALTER",  
          "CREATE_TABLE",  
          "DROP",  
          "INSERT",  
          "DELETE",  
          "UPDATE",  
          "TRUNCATE",  
          "VIEW_REFLECTION",  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "MANAGE_GRANTS",  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "checkTableAuthorizer": true,  
  "owner": {  
    "ownerId": "4fb93af3-acc2-4b10-ad4b-64dd7070d365",  
    "ownerType": "USER"  
  },  
  "accelerationRefreshOnDataChanges": false  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Source[​](#updating-a-source "Direct link to Updating a Source")

Update the specified source.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the source to update.

Example: 2b1be882-7012-4a99-8d6c-82e32e4562e4

---

entityType Body   String

Type of the catalog object to update. For sources, the entityType is `source`.

Example: source

---

[config](/25.x/reference/api/catalog/source/#parameters-of-the-config-object-1) Body   Object

Configuration settings for the source. The available parameters in the config object are different for different source types. For more information, read [Source Configuration](/25.x/reference/api/catalog/source/container-source-config).

Example: {"accessKey": "EXAMPLE78HT89VS4YJEL","accessSecret": "EXAMPLEe3bcpKnAwgJ2WBpX8d9kEdhMz24guiR7L","secure": true,"rootPath": "/","enableAsync": true,"compatibilityMode": false,"isCachingEnabled": true,"maxCacheSpacePct": 100,"requesterPays": false,"enableFileStatusCheck": true,"defaultCtasFormat": "ICEBERG","isPartitionInferenceEnabled": false,"credentialType": "ACCESS\_KEY"}

---

id Body   String

Unique identifier of the source to update.

Example: 2b1be882-7012-4a99-8d6c-82e32e4562e4

---

tag Body   String

Unique identifier of the version of the source that you want to update. Dremio uses the tag to ensure that you are requesting to update the most recent version of the source.

Example: T0/Zr1FOY3A=

---

type Body   String

Type of the source that you want to update.

Enum: ADL, ADX, AMAZONELASTIC, AWSGLUE, AZURE\_STORAGE, DB2, DREMIOTODREMIO, ELASTIC, GCS, HDFS, HIVE, HIVE3, MONGO, MSSQL, MYSQL, NAS, NESSIE, ORACLE, POSTGRES, REDSHIFT, S3, SNOWFLAKE, SYNAPSE, TERADATA

Example: S3

---

name Body   String

Name of the source that you want to update.

Example: AWS-S3\_testgroup

---

[metadataPolicy](/25.x/reference/api/catalog/source/#parameters-of-the-metadatapolicy-object-1) Body   Object   Optional

Information about the metadata policy for the source.

Example: {"authTTLMs": 86400000,"namesRefreshMs": 3600000,"datasetRefreshAfterMs": 3600000,"datasetExpireAfterMs": 10800000,"datasetUpdateMode": "PREFETCH\_QUERIED","deleteUnavailableDatasets": true,"autoPromoteDatasets": false}

---

accelerationGracePeriodMs Body   Integer   Optional

Maximum age to allow for Reflection data used to accelerate queries on datasets in the source, in milliseconds. For more information, read [Setting the Expiration Policy for Reflections](/25.x/sonar/reflections/setting-expiration-policy).

Example: 10800000

---

accelerationRefreshPeriodMs Body   Integer   Optional

Refresh period to use for the data in all Reflections on datasets in the source, in milliseconds. Default is `0`.

Example: 3600000

---

accelerationNeverExpire Body   Boolean   Optional

Option to set an expiration for Reflections. Default setting is `false`. Set to `true` to prevent Reflections from expiring and to override the `accelerationGracePeriodMs` setting.

Example: false

---

accelerationNeverRefresh Body   Boolean   Optional

Option to set a refresh for Reflections. Default setting is `false`. Set to `true` to prevent Reflections from refreshing and to override the `accelerationRefreshPeriodMs` setting.

---

accelerationActivePolicyType String

Option to set the policy for refreshing Reflections that are defined on the source. For this option to take effect, `accelerationNeverRefresh` must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: The Reflections are refreshed at the end of every period that is defined by accelerationRefreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by accelerationRefreshSchedule.

---

accelerationRefreshSchedule String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source are refreshed. Optional if you set accelerationActivePolicyType to `SCHEDULE`. The default accelerationRefreshSchedule setting is to refresh every day at 8:00 a.m.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:

* `0 0 0 * * ?` : Refreshes every day at midnight.
* `0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
* `0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

allowCrossSourceSelection Body   Boolean   Optional

If the source should be available for queries that can select from multiple sources, set to `true`. Otherwise, set to `false` (default).

Example: false

---

disableMetadataValidityCheck Body   Boolean   Optional

To disable the check for expired metadata and require users to refresh manually, set to `true`. Otherwise, set to `false` (default).

note

The disableMetadataValidityCheck parameter is not supported by default. Contact Dremio Support to enable it.

Example: false

---

accelerationRefreshOnDataChanges Body   Boolean

To refresh Reflections on underlying tables that are in Iceberg format in the source when new snapshots are created after an update, `true`. Otherwise, `false`. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency. For this option to take effect, the source must support Iceberg table format, the accelerationNeverRefresh parameter must be set to `false`, and the accelerationActivePolicyType parameter must be set to either `PERIOD` or `SCHEDULE`.

---

[accessControlList](/25.x/reference/api/catalog/source/#accesscontrollist-1) Body   String   Optional

Enterprise only. Information about users and roles that should have access to the source and the specific privileges each user or role should have. May include an array of users, an array of roles, or both, depending on the configured access and privileges. To keep existing accessControlList settings while making other updates, duplicate the existing accessControlList object in the PUT request.

Example: {"users": [{"id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65", "permissions": ["VIEW\_REFLECTION","SELECT" ]}],"roles": [{"id": "c45ff4d8-e910-4f85-89db-9b8c29188a56", "permissions": ["ALTER","CREATE\_TABLE","DROP","INSERT","DELETE","UPDATE","TRUNCATE","VIEW\_REFLECTION","ALTER\_REFLECTION","MODIFY","MANAGE\_GRANTS","SELECT"]}]}

#### Parameters of the `config` Object[​](#parameters-of-the-config-object-1 "Direct link to parameters-of-the-config-object-1")

The `config` object's parameters vary for different source types. Read [Source Configuration](/25.x/reference/api/catalog/source/container-source-config) for information about the available parameters in the `config` object for each supported source type.

#### Parameters of the `metadataPolicy` Object[​](#parameters-of-the-metadatapolicy-object-1 "Direct link to parameters-of-the-metadatapolicy-object-1")

authTTLMs Body   Integer   Optional

Length of time to cache the privileges that the user has on the source, in milliseconds. For example, if authTTLMs is set to `28800000` (8 hours), Dremio checks the user's privilege status once every 8 hours. Default is `86400000` (24 hours). Minimum is `60000` (1 minute).

Example: 86400000

---

namesRefreshMs Body   Integer   Optional

How often to refresh the source, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 3600000

---

datasetRefreshAfterMs Body   Integer   Optional

How often to refresh the metadata in the source's datasets, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 3600000

---

datasetExpireAfterMs Body   Integer   Optional

Maximum age to allow for the metadata in the source's datasets, in milliseconds. Default is `3600000` (1 hour). Minimum is `60000` (1 minute).

Example: 10800000

---

datasetUpdateMode Body   String   Optional

Approach for Dremio to take for updating the metadata when updating datasets in the source.

* `PREFETCH`: (deprecated) Dremio updates details for all datasets in a source.
* `PREFETCH_QUERIED`: Dremio updates details for previously queried objects in a source.

Example: PREFETCH\_QUERIED

---

deleteUnavailableDatasets Body    Boolean   Optional

If Dremio should remove dataset definitions from the source when the underlying data is unavailable, set to `true` (default). Otherwise, set to `false`.

Example: true

---

autoPromoteDatasets Body   Boolean   Optional

If Dremio should automatically format files into tables when a user issues a query, set to `true`. Otherwise, set to `false` (default). Available only for datalake sources, such as Amazon S3 and Hive.

Example: false

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/source/#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the source and the specific privileges each user should have.

Example: [{"id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65","permissions": ["VIEW\_REFLECTION","SELECT"]}]

---

[roles](/25.x/reference/api/catalog/source/#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the source and the specific privileges each role should have.

Example: [{"id": "c45ff4d8-e910-4f85-89db-9b8c29188a56","permissions": ["ALTER","CREATE\_TABLE","DROP","INSERT","DELETE","UPDATE","TRUNCATE","VIEW\_REFLECTION","ALTER\_REFLECTION","MODIFY","MANAGE\_GRANTS","SELECT"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the source.

Example: ebe519ab-20e3-43ff-9b4c-b3ec590c7e65

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the source. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["VIEW\_REFLECTION","SELECT"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/2b1be882-7012-4a99-8d6c-82e32e4562e4' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "source",  
  "config": {  
    "accessKey": "EXAMPLE78HT89VS4YJEL",  
    "accessSecret": "$DREMIO_EXISTING_VALUE$",  
    "secure": true,  
    "rootPath": "/",  
    "enableAsync": true,  
    "compatibilityMode": false,  
    "isCachingEnabled": true,  
    "maxCacheSpacePct": 100,  
    "whitelistedBuckets": [  
      "archive.dremio.com",  
      "logs_east-1",  
      "logs_west-1"  
    ],  
    "requesterPays": false,  
    "enableFileStatusCheck": true,  
    "defaultCtasFormat": "ICEBERG",  
    "isPartitionInferenceEnabled": false,  
    "credentialType": "ACCESS_KEY"  
  },  
  "id": "2b1be882-7012-4a99-8d6c-82e32e4562e4",  
  "tag": "T0/Zr1FOY3A=",  
  "type": "S3",  
  "name": "AWS-S3_testgroup",  
  "metadataPolicy": {  
    "authTTLMs": 86400000,  
    "namesRefreshMs": 3600000,  
    "datasetRefreshAfterMs": 3600000,  
    "datasetExpireAfterMs": 10800000,  
    "datasetUpdateMode": "PREFETCH_QUERIED",  
    "deleteUnavailableDatasets": true,  
    "autoPromoteDatasets": true  
  },  
  "accelerationGracePeriodMs": 10800000,  
  "accelerationRefreshPeriodMs": 3600000,  
  "accelerationActivePolicyType": "PERIOD",  
  "accelerationNeverExpire": false,  
  "accelerationNeverRefresh": false,  
  "allowCrossSourceSelection": false,  
  "disableMetadataValidityCheck": false,  
  "accelerationRefreshOnDataChanges": true,  
  "accessControlList": {  
    "users": [  
      {  
        "id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65",  
        "permissions": [  
          "ALTER",  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "c45ff4d8-e910-4f85-89db-9b8c29188a56",  
        "permissions": [  
          "ALTER",  
          "CREATE_TABLE",  
          "DROP",  
          "INSERT",  
          "DELETE",  
          "UPDATE",  
          "TRUNCATE",  
          "VIEW_REFLECTION",  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "MANAGE_GRANTS",  
          "SELECT"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "source",  
  "config": {  
    "accessKey": "EXAMPLE78HT89VS4YJEL",  
    "accessSecret": "$DREMIO_EXISTING_VALUE$",  
    "secure": true,  
    "rootPath": "/",  
    "enableAsync": true,  
    "compatibilityMode": false,  
    "isCachingEnabled": true,  
    "maxCacheSpacePct": 100,  
    "whitelistedBuckets": [  
      "archive.dremio.com",  
      "logs_east-1",  
      "logs_west-1"  
    ],  
    "requesterPays": false,  
    "enableFileStatusCheck": true,  
    "defaultCtasFormat": "ICEBERG",  
    "isPartitionInferenceEnabled": false,  
    "credentialType": "ACCESS_KEY"  
  },  
  "id": "2b1be882-7012-4a99-8d6c-82e32e4562e4",  
  "tag": "RfVMBBMWRvU=",  
  "type": "S3",  
  "name": "AWS-S3_testgroup",  
  "createdAt": "2023-02-17T14:32:20.640Z",  
  "metadataPolicy": {  
    "authTTLMs": 86400000,  
    "namesRefreshMs": 3600000,  
    "datasetRefreshAfterMs": 3600000,  
    "datasetExpireAfterMs": 10800000,  
    "datasetUpdateMode": "PREFETCH_QUERIED",  
    "deleteUnavailableDatasets": true,  
    "autoPromoteDatasets": true  
  },  
  "accelerationGracePeriodMs": 10800000,  
  "accelerationRefreshPeriodMs": 3600000,  
  "accelerationActivePolicyType": "PERIOD",  
  "accelerationNeverExpire": false,  
  "accelerationNeverRefresh": false,  
  "children": [  
    {  
      "id": "dremio:/AWS-S3_testgroup/archive.dremio.com",  
      "path": [  
        "AWS-S3_testgroup",  
        "archive.dremio.com"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_east-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_east-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "dremio:/AWS-S3_testgroup/logs_west-1",  
      "path": [  
        "AWS-S3_testgroup",  
        "logs_west-1"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    }  
  ],  
  "allowCrossSourceSelection": false,  
  "disableMetadataValidityCheck": false,  
  "accessControlList": {  
    "users": [  
      {  
        "id": "ebe519ab-20e3-43ff-9b4c-b3ec590c7e65",  
        "permissions": [  
          "ALTER",  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "c45ff4d8-e910-4f85-89db-9b8c29188a56",  
        "permissions": [  
          "ALTER",  
          "CREATE_TABLE",  
          "DROP",  
          "INSERT",  
          "DELETE",  
          "UPDATE",  
          "TRUNCATE",  
          "VIEW_REFLECTION",  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "MANAGE_GRANTS",  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "checkTableAuthorizer": true,  
  "owner": {  
    "ownerId": "4fb93af3-acc2-4b10-ad4b-64dd7070d365",  
    "ownerType": "USER"  
  },  
  "accelerationRefreshOnDataChanges": true  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting a Source[​](#deleting-a-source "Direct link to Deleting a Source")

Delete the specified source, including all of the source's contents.

note

If the source is in a bad state (for example, Dremio cannot authenticate to the source or the source is otherwise unavailable), only users who belong to the ADMIN role can delete the source.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the source that you want to delete.

Example: 2b1be882-7012-4a99-8d6c-82e32e4562e4

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/2b1be882-7012-4a99-8d6c-82e32e4562e4' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Catalog](/25.x/reference/api/catalog/)[Next

Source Configuration](/25.x/reference/api/catalog/source/container-source-config)

* [Source Attributes](#source-attributes)
* [Creating a Source](#creating-a-source)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Source by ID](#retrieving-a-source-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Source by Path](#retrieving-a-source-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Source](#updating-a-source)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a Source](#deleting-a-source)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/container-space

Version: 25.x

On this page

# Space

Use the Catalog API to retrieve information about [spaces](/25.x/sonar/query-manage/managing-data/spaces) and the child objects they contain, as well as to create, update, and delete spaces.

Space Object

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

## Space Attributes[​](#space-attributes "Direct link to Space Attributes")

entityType String

Type of the catalog object. For spaces, the entityType is `space`.

Example: space

---

id String (UUID)

Unique identifier of the space.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

name String

Name of the space.

Example: Example-Space

---

tag String

Unique identifier of the version of the space. Dremio changes the tag whenever the space changes and uses the tag to ensure that PUT requests apply to the most recent version of the space.

Example: zzOQfjY9lU0=

---

createdAt String

Date and time that the space was created, in UTC format.

Example: 2023-01-12T18:44:43.237Z

---

[children](/25.x/reference/api/catalog/container-space#attributes-of-objects-in-the-children-array) Array of Object

Information about each catalog object in the space.

Example: [{"id": "8da037a1-8e50-422b-9a2b-cafb03f57c71","path": ["Example-Space","testfolder"],"tag": "0McuCL4MzBU=","type": "CONTAINER","containerType": "FOLDER"},{"id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473","path": ["Example-Space","travel\_testing"],"tag": "i4mnlSmHqVM=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-01-30T17:54:25.547Z"},{"id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda","path": ["Example-Space","zips"],"tag": "ITlp8+qyIMQ=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-02-08T16:24:25.084Z"}]

---

[accessControlList](/25.x/reference/api/catalog/container-space#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the space and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if space-specific access control privileges are not set.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["MODIFY"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the space. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/container-space#attributes-of-the-owner-object) Object

Information about the space's owner.

Example: {"ownerId": "d01585a2-b267-4d56-9154-31762ab65a43","ownerType": "USER"}

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String (UUID)

Unique identifier of the catalog object.

Example: 8da037a1-8e50-422b-9a2b-cafb03f57c71

---

path Array of String

Path of the catalog object within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by the catalog object itself as the last item in the array.

Example: ["Example-Space","testfolder"]

---

tag String

Unique identifier of the version of the catalog object. Dremio changes the tag whenever the catalog object changes and uses the tag to ensure that PUT requests apply to the most recent version of the object.

Example: 0McuCL4MzBU=

---

type String

Type of the catalog object.

Enum: CONTAINER, DATASET, FILE

Example: CONTAINER

---

containerType String

For catalog entities with the type `CONTAINER`, the type of container.

Enum: FOLDER, FUNCTION

Example: FOLDER

---

datasetType String

For catalog objects in a space with the type `DATASET`, the datasetType is `VIRTUAL` (spaces cannot contain tables, only views).

Example: VIRTUAL

---

createdAt String

For catalog objects in a space with the type `DATASET`, date and time that the catalog object was created, in UTC format.

Example: 2023-01-30T17:54:25.547Z

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-space#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the space and the specific privileges each user has.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5", "permissions": ["MODIFY"]}]

---

[roles](/25.x/reference/api/catalog/container-space#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the space and the specific privileges each role has.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889", "permissions": ["MODIFY"]}]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the space's owner.

Example: d01585a2-b267-4d56-9154-31762ab65a43

---

ownerType String

Type of owner of the space.

Enum: USER, ROLE

Example: USER

##### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String (UUID)

Enterprise only. Unique identifier of the user or role with access to the space.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the space. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["MODIFY"]

## Creating a Space[​](#creating-a-space "Direct link to Creating a Space")

Create a new space.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object. For spaces, the entityType is `space`.

Example: space

---

name Body   String

Name of the space. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: Example-Space

---

[accessControlList](/25.x/reference/api/catalog/container-space#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the space and the specific privileges each user or role should have. May include an array of users, an array of roles, or both. Omit if you do not want to configure space-specific access control privileges.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["MODIFY"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the space and the specific privileges each user should have.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["MODIFY"]}]

---

[roles](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the space and the specific privileges each role should have.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the space.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the space. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["MODIFY"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "space",  
  "name": "Example-Space",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Retrieving a Space by ID[​](#retrieving-a-space-by-id "Direct link to Retrieving a Space by ID")

Retrieve a space and information about its contents by specifying the space's ID.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the space that you want to retrieve.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the space has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Space by Path[​](#retrieving-a-space-by-path "Direct link to Retrieving a Space by Path")

Retrieve a space and information about its contents by specifying the space's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Path of the space that you want to retrieve. The path is the name of the space.

Example: Example-Space

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam1) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam1): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the space has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Example-Space' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Space[​](#updating-a-space "Direct link to Updating a Space")

Update the specified space.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the space that you want to update.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

entityType Body   String

Type of the catalog object. For spaces, the entityType is `space`.

Example: space

---

id Body   String (UUID)

Unique identifier of the space to update.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

name Body   String

Name of the space to update.

Example: Example-Space

---

tag Body   String

Unique identifier of the version of the space that you want to update. Dremio uses the tag to ensure that you are requesting to update the most recent version of the space.

Example: zzOQfjY9lU0=

---

[accessControlList](/25.x/reference/api/catalog/container-space#parameters-of-the-accesscontrollist-object-1) Body   String   Optional

Enterprise only. Object used to specify which users and roles should have access to the space and the specific privileges each user or role should have. If you omit the accessControlList object in a PUT request, Dremio removes all existing user and role access settings from the space. To keep existing user and role access settings while making other updates, duplicate the existing accessControlList array in the PUT request.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALL"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the space and the specific privileges each user should have. If you omit the users object in a PUT request, Dremio removes all existing user access settings from the space. To keep existing user access settings while making other updates, duplicate the existing users array in the PUT request.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5", "permissions": ["ALL"]}]

---

[roles](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the space and the specific privileges each role should have. If you omit the roles object in a PUT request, Dremio removes all existing role access settings from the space. To keep existing role access settings while making other updates, duplicate the existing roles array in the PUT request.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889", "permissions": ["MODIFY"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the space.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the space. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["ALL"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALL"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "PwZ6e/axHUY=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "ALTER",  
          "MANAGE_GRANTS",  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting a Space[​](#deleting-a-space "Direct link to Deleting a Space")

Delete the specified space, including all of the space's contents.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the space that you want to delete.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Home](/25.x/reference/api/catalog/container-home)[Next

Folder](/25.x/reference/api/catalog/container-folder)

* [Space Attributes](#space-attributes)
* [Creating a Space](#creating-a-space)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Space by ID](#retrieving-a-space-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Space by Path](#retrieving-a-space-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Space](#updating-a-space)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a Space](#deleting-a-space)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/container-folder

Version: 25.x

On this page

# Folder

Use the Catalog API to retrieve information about [folders](/25.x/sonar/query-manage/managing-data/spaces/#folders) and the child objects they contain, as well as to create, update, and delete folders.

Folder Object

```
{  
  "entityType": "folder",  
  "id": "d4c2a8ba-a972-4db4-8deb-67e1ade684d1",  
  "path": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "tag": "pRmJ0BQ9SFw=",  
  "children": [  
    {  
      "id": "dremio:/Samples/samples.dremio.com/zip_lookup.csv",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zip_lookup.csv"  
      ],  
      "type": "FILE"  
    },  
    {  
      "id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips-iceberg"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "type": "DATASET",  
      "datasetType": "PROMOTED"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

## Folder Attributes[​](#folder-attributes "Direct link to Folder Attributes")

entityType String

Type of the catalog object. For folders, the entityType is `folder`.

Example: folder

---

id String

Unique identifier of the folder. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: d4c2a8ba-a972-4db4-8deb-67e1ade684d1

---

path Array of String

Path of the folder within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the target folder itself as the last item in the array.

Example: ["Samples","samples.dremio.com"]

---

tag String

Unique identifier of the version of the folder. Dremio changes the tag whenever the folder changes and uses the tag to ensure that PUT requests apply to the most recent version of the folder.

Example: pRmJ0BQ9SFw=

---

[children](/25.x/reference/api/catalog/container-folder#attributes-of-objects-in-the-children-array) Array of Object

Information about each catalog object in the folder.

Example: [{"id": "dremio:/Samples/samples.dremio.com/zip\_lookup.csv","path": ["Samples","samples.dremio.com","zip\_lookup.csv"],"type": "FILE"},{"id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg","path": ["Samples","samples.dremio.com","NYC-taxi-trips-iceberg"],"type": "CONTAINER","containerType": "FOLDER"},{"id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d","path": ["Samples","samples.dremio.com","NYC-taxi-trips"],"type": "DATASET","datasetType": "PROMOTED"}]

---

[accessControlList](/25.x/reference/api/catalog/container-folder#attributes-of-the-accesscontrollist-object) Object

Enterprise-only. Information about users and roles with access to the folder and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if folder-specific access control privileges are not set.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the folder. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/container-folder#attributes-of-the-owner-object) Object

Information about the folder's owner.

Example: {"ownerId": "d01585a2-b267-4d56-9154-31762ab65a43","ownerType": "USER"}

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String

Unique identifier of the catalog object. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: dremio:/Samples/samples.dremio.com/zip\_lookup.csv

---

path Array of String

Path of the catalog object within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the catalog object itself as the last item in the array.

Example: ["Samples","samples.dremio.com","zip\_lookup.csv"]

---

type String

Type of the catalog object. If the object is saved within a space (including the home space), valid types are `CONTAINER` and `DATASET`. If the object is saved within a source, valid types are `CONTAINER`, `FILE`, and `DATASET`.

Example: CONTAINER

---

containerType String

For catalog objects with the type `CONTAINER`, the containerType is `FOLDER`.

Example: FOLDER

---

datasetType String

For catalog objects with the type `DATASET`, the type of dataset. For tables, the datasetType is `PROMOTED`. For views, the datasetType is `VIRTUAL`.

Enum: PROMOTED, VIRTUAL

Example: VIRTUAL

---

createdAt String

Date and time that the catalog object was created, in UTC format. The createdAt attribute is included only for `DATASET` catalog objects that are saved in folders within spaces, not within sources.

Example: 2023-01-30T17:54:25.547Z

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-folder#attributes-of-objects-in-the-users-and-roles-arrays) String

Enterprise-only. List of users with access to the folder and the specific privileges each user has.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}]

---

[roles](/25.x/reference/api/catalog/container-folder#attributes-of-objects-in-the-users-and-roles-arrays) String

Enterprise-only. List of roles whose members have access to the folder and the specific privileges each role has.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the folder's owner.

Example: d01585a2-b267-4d56-9154-31762ab65a43

---

ownerType String

Type of owner of the folder.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String (UUID)

Enterprise-only. Unique identifier of the user or role with access to the folder.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Array of String

Enterprise-only. List of privileges the user or role has on the folder. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT","ALTER"]

## Creating a Folder[​](#creating-a-folder "Direct link to Creating a Folder")

Create a new folder within a space.

note

The Catalog API cannot create new folders within sources.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object. For folders, the entityType is `folder`.

Example: folder

---

path Body   Array of String

Path of the location where the folder should be created within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by a name for the target folder itself as the last item in the array. The name of the folder cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: ["Example-Space","First-Folder","New-Folder"]

---

[accessControlList](/25.x/reference/api/catalog/container-folder#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise-only. Object used to specify which users and roles should have access to the folder and the specific privileges each user or role should have. May include an array of users, an array of roles, or both. Omit if you do not want to configure folder-specific access control privileges.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays) Body   String   Optional

Enterprise-only. List of users who should have access to the folder and the specific privileges each user should have.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}]

---

[roles](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays) Body   String   Optional

Enterprise-only. List of roles whose members should have access to the folder and the specific privileges each role should have.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String (UUID)   Optional

Enterprise-only. Unique identifier of the user or role who should have access to the folder.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise-only. List of privileges the user or role should have on the folder. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALTER\_REFLECTION, SELECT, ALTER, VIEW\_REFLECTION, MANAGE\_GRANTS, ALL

Example: ["SELECT","ALTER"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "folder",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "598697c2-8be0-4050-9731-53563977a17d",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "tag": "R7COubQq8KE=",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Retrieving a Folder by ID[​](#retrieving-a-folder-by-id "Direct link to Retrieving a Folder by ID")

Retrieve a folder and information about its contents by specifying the folder's ID.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String

Unique identifier of the folder that you want to retrieve. If the ID is a text path, use URL encoding to replace any special characters with their UTF-8-equivalent characters, such as `%3A` for a colon; `%2F` for a forward slash; and `%20` for a space. For example, if the ID value is `dremio:/Samples/samples.dremio.com/Dremio University`, the URI-encoded ID is `dremio%3A%2FSamples%2Fsamples.dremio.com%2FDremio%20University`.

Example: d4c2a8ba-a972-4db4-8deb-67e1ade684d1

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

**NOTE:** The maxChildren query parameter is not supported for folders in filesystem sources.

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the folder has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

**NOTE:** Dremio ignores the pageToken query parameter for folders in filesystem sources.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/d4c2a8ba-a972-4db4-8deb-67e1ade684d1' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "d4c2a8ba-a972-4db4-8deb-67e1ade684d1",  
  "path": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "tag": "pRmJ0BQ9SFw=",  
  "children": [  
    {  
      "id": "dremio:/Samples/samples.dremio.com/zip_lookup.csv",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zip_lookup.csv"  
      ],  
      "type": "FILE"  
    },  
    {  
      "id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips-iceberg"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "type": "DATASET",  
      "datasetType": "PROMOTED"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Folder by Path[​](#retrieving-a-folder-by-path "Direct link to Retrieving a Folder by Path")

Retrieve a folder and information about its contents by specifying the folder's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Path of the folder that you want to retrieve, with a forward slash to separate each level of nesting. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: Samples/samples.dremio.com

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam1) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

**NOTE:** The maxChildren query parameter is not supported for filesystem sources.

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam1): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the folder has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

**NOTE:** Dremio ignores the pageToken query parameter for folders in filesystem sources.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Samples/samples.dremio.com' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "d4c2a8ba-a972-4db4-8deb-67e1ade684d1",  
  "path": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "tag": "pRmJ0BQ9SFw=",  
  "children": [  
    {  
      "id": "dremio:/Samples/samples.dremio.com/zip_lookup.csv",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zip_lookup.csv"  
      ],  
      "type": "FILE"  
    },  
    {  
      "id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips-iceberg"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "type": "DATASET",  
      "datasetType": "PROMOTED"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Folder[​](#updating-a-folder "Direct link to Updating a Folder")

Update the specified folder.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String

Unique identifier of the folder to update. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: 598697c2-8be0-4050-9731-53563977a17d

---

entityType Body   String

Type of the catalog object. For folders, the entityType is `folder`.

Example: folder

---

id Body   String

Unique identifier of the folder to update. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: 598697c2-8be0-4050-9731-53563977a17d

---

path Body   Array of String

Path of the location where the folder is saved within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by the target folder itself as the last item in the array.

Example: ["Example-Space","First-Folder","New-Folder"]

---

tag Body   String

Unique identifier of the version of the folder that you want to update. Dremio uses the tag to ensure that you are requesting to update the most recent version of the folder.

Example: R7COubQq8KE=

---

[accessControlList](/25.x/reference/api/catalog/container-folder#parameters-of-the-accesscontrollist-object-1) Body   Object   Optional

Enterprise-only. Object used to specify which users and roles should have access to the folder and the specific privileges each user or role should have. If you omit the accessControlList object in a PUT request, Dremio removes all existing user and role access settings from the folder. To keep existing user and role access settings while making other updates, duplicate the existing accessControlList array in the PUT request.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALL"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   String   Optional

Enterprise-only. List of users who should have access to the folder and the specific privileges each user should have. If you omit the users object in a PUT request, Dremio removes all existing user access settings from the folder. To keep existing user access settings while making other updates, duplicate the existing users array in the PUT request.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALL"]}]

---

[roles](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   String   Optional

Enterprise-only. List of roles whose members should have access to the folder and the specific privileges each role should have. If you omit the roles object in a PUT request, Dremio removes all existing role access settings from the folder. To keep existing role access settings while making other updates, duplicate the existing roles array in the PUT request.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String (UUID)   Optional

Enterprise-only. Unique identifier of the user or role who should have access to the folder.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise-only. List of privileges the user or role should have on the folder. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALTER\_REFLECTION, SELECT, ALTER, VIEW\_REFLECTION, MANAGE\_GRANTS, ALL

Example: ["ALL"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "folder",  
  "id": "598697c2-8be0-4050-9731-53563977a17d",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "tag": "R7COubQq8KE=",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALL"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "598697c2-8be0-4050-9731-53563977a17d",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "tag": "vnRnYLLpCFU=",  
  "children": [  
    {  
      "id": "d60f9258-e55a-4fc3-97b3-58c6720a70fc",  
      "path": [  
        "Example-Space",  
        "First-Folder",  
        "New-Folder",  
        "NYC-trips-weather"  
      ],  
      "tag": "IHXU7Oxs80c=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "acba8595-bfcf-4126-887c-d2a19b5afb1d",  
      "path": [  
        "Example-Space",  
        "First-Folder",  
        "New-Folder",  
        "short-distance-trips"  
      ],  
      "tag": "KYs/Qyw1ok8=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-09T19:09:58.789Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER_REFLECTION",  
          "ALTER",  
          "MANAGE_GRANTS",  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting a Folder[​](#deleting-a-folder "Direct link to Deleting a Folder")

Delete the specified folder, including all of the folder's contents.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String

Unique identifier of the folder that you want to delete. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: 598697c2-8be0-4050-9731-53563977a17d

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/598697c2-8be0-4050-9731-53563977a17d' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Space](/25.x/reference/api/catalog/container-space)[Next

File](/25.x/reference/api/catalog/file)

* [Folder Attributes](#folder-attributes)
* [Creating a Folder](#creating-a-folder)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Folder by ID](#retrieving-a-folder-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Folder by Path](#retrieving-a-folder-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Folder](#updating-a-folder)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a Folder](#deleting-a-folder)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/container-home

Version: 25.x

On this page

# Home

Use the Catalog API to retrieve information about the [home space](/25.x/sonar/query-manage/managing-data/spaces/#home-space) and the child objects it contains.

Home Object

```
{  
  "entityType": "home",  
  "id": "87049e43-8564-4ee7-8bb6-5bdaf5bd0959",  
  "name": "@user@dremio.com",  
  "tag": "8S9cTZ5IsWo=",  
  "children": [  
    {  
      "id": "1e16c0e5-c890-4f87-b1a6-ac9325aafa2c",  
      "path": [  
        "@user@dremio.com",  
        "Business"  
      ],  
      "tag": "KgFBPW3+Cyc=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "a59815d0-3c21-41ad-b9bc-2ba105251fa6",  
      "path": [  
        "@user@dremio.com",  
        "meeting_rooms_lookup"  
      ],  
      "tag": "OaQT64frevc=",  
      "type": "DATASET",  
      "datasetType": "PROMOTED",  
      "createdAt": "1970-01-01T00:00:00.000Z"  
    },  
    {  
      "id": "37401663-8666-4e00-bc03-668abb43ccd7",  
      "path": [  
        "@user@dremio.com",  
        "NYC-trips-quarterly"  
      ],  
      "tag": "+H5TpLYoosY=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-07T21:26:14.385Z"  
    }  
  ]  
}
```

## Home Attributes[​](#home-attributes "Direct link to Home Attributes")

entityType String

Type of the catalog object. For the home space, the entityType is `home`.

Example: home

---

id String (UUID)

Unique identifier of the home space.

Example: 87049e43-8564-4ee7-8bb6-5bdaf5bd0959

---

name String

Name of the home space. Automatically generated based on the username.

Example: @[user@dremio.com](mailto:user@dremio.com)

---

tag String

Unique identifier of the version of the home space. Dremio uses tags to ensure that PUT requests apply to the most recent version of the resource being updated. However, home spaces cannot be changed, so the tag is listed in the home space object but not used.

Example: 8S9cTZ5IsWo=

---

[children](/25.x/reference/api/catalog/container-home#attributes-of-objects-in-the-children-array) Array of Object

Information about each catalog object in the home space.

Example: [{"id":"1e16c0e5-c890-4f87-b1a6-ac9325aafa2c","path": ["@dremio","Business"],"tag":"KgFBPW3+Cyc=","type":"CONTAINER","containerType":"FOLDER"},{"id":"a59815d0-3c21-41ad-b9bc-2ba105251fa6","path": ["@dremio","meeting\_rooms\_lookup"],"tag":"OaQT64frevc=","type":"DATASET","datasetType":"PROMOTED","createdAt":"1970-01-01T00:00:00.000Z"},{"id":"37401663-8666-4e00-bc03-668abb43ccd7","path": ["@dremio","NYC-trips-quarterly"],"tag":"+H5TpLYoosY=","type":"DATASET","datasetType":"VIRTUAL","createdAt":"2023-02-07T21:26:14.385Z"}]

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String (UUID)

Unique identifier of the catalog object.

Example: 1e16c0e5-c890-4f87-b1a6-ac9325aafa2c

---

path Array of String

Path of the catalog object within Dremio, expressed as an array. The path consists of the home space, followed by any folder and subfolders, followed by the catalog object itself as the last item in the array.

Example: ["@[user@dremio.com](mailto:user@dremio.com)","Business"]

---

tag String

Unique identifier of the version of the catalog object. Dremio changes the tag whenever the catalog object changes and uses the tag to ensure that PUT requests apply to the most recent version of the object.

Example: KgFBPW3+Cyc=

---

type String

Type of the catalog object.

Enum: CONTAINER, DATASET

Example: CONTAINER

---

containerType String

For catalog entities with the type `CONTAINER`, the type of container.

Enum: FOLDER, FUNCTION

Example: FOLDER

---

datasetType String

For catalog entities with the type `DATASET`, the type of dataset. For tables, the datasetType is `PROMOTED`. For views, the datasetType is `VIRTUAL`.

Enum: PROMOTED, VIRTUAL

Example: PROMOTED

---

createdAt String

For catalog entities with the type `DATASET`, date and time that the catalog object was created, in UTC format.

Example: 2023-02-07T21:26:14.385Z

## Retrieving the Home Space by ID[​](#retrieving-the-home-space-by-id "Direct link to Retrieving the Home Space by ID")

Retrieve information about the home space and its contents by specifying the home space's ID.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters "Direct link to Parameters")

id Body   String (UUID)

Unique identifier of the home space that you want to retrieve.

Example: 87049e43-8564-4ee7-8bb6-5bdaf5bd0959

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the home space has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/63505c60-bc86-42aa-a622-24e5f22ce50b' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "home",  
  "id": "87049e43-8564-4ee7-8bb6-5bdaf5bd0959",  
  "name": "@user@dremio.com",  
  "tag": "8S9cTZ5IsWo=",  
  "children": [  
    {  
      "id": "1e16c0e5-c890-4f87-b1a6-ac9325aafa2c",  
      "path": [  
        "@user@dremio.com",  
        "Business"  
      ],  
      "tag": "KgFBPW3+Cyc=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "a59815d0-3c21-41ad-b9bc-2ba105251fa6",  
      "path": [  
        "@user@dremio.com",  
        "meeting_rooms_lookup"  
      ],  
      "tag": "OaQT64frevc=",  
      "type": "DATASET",  
      "datasetType": "PROMOTED",  
      "createdAt": "1970-01-01T00:00:00.000Z"  
    },  
    {  
      "id": "37401663-8666-4e00-bc03-668abb43ccd7",  
      "path": [  
        "@user@dremio.com",  
        "NYC-trips-quarterly"  
      ],  
      "tag": "+H5TpLYoosY=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-07T21:26:14.385Z"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving the Home Space by Path[​](#retrieving-the-home-space-by-path "Direct link to Retrieving the Home Space by Path")

Retrieve information about the home space and its contents by specifying the home space's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

path Path   String

Path of the home space whose information you want to retrieve. The home space path is the username, preceded with the `@` symbol.

Example: @[user@dremio.com](mailto:user@dremio.com)

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam1) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam1): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the home space has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/@user@dremio.com' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "home",  
  "id": "87049e43-8564-4ee7-8bb6-5bdaf5bd0959",  
  "name": "@user@dremio.com",  
  "tag": "8S9cTZ5IsWo=",  
  "children": [  
    {  
      "id": "1e16c0e5-c890-4f87-b1a6-ac9325aafa2c",  
      "path": [  
        "@user@dremio.com",  
        "Business"  
      ],  
      "tag": "KgFBPW3+Cyc=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "a59815d0-3c21-41ad-b9bc-2ba105251fa6",  
      "path": [  
        "@user@dremio.com",  
        "meeting_rooms_lookup"  
      ],  
      "tag": "OaQT64frevc=",  
      "type": "DATASET",  
      "datasetType": "PROMOTED",  
      "createdAt": "1970-01-01T00:00:00.000Z"  
    },  
    {  
      "id": "37401663-8666-4e00-bc03-668abb43ccd7",  
      "path": [  
        "@user@dremio.com",  
        "NYC-trips-quarterly"  
      ],  
      "tag": "+H5TpLYoosY=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-07T21:26:14.385Z"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Source Configuration](/25.x/reference/api/catalog/source/container-source-config)[Next

Space](/25.x/reference/api/catalog/container-space)

* [Home Attributes](#home-attributes)
* [Retrieving the Home Space by ID](#retrieving-the-home-space-by-id)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving the Home Space by Path](#retrieving-the-home-space-by-path)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/file

Version: 25.x

On this page

# File

Use the Catalog API to retrieve information about [formatting data to a table](/25.x/sonar/data-sources/entity-promotion).

File Object

```
{  
  "entityType": "file",  
  "id": "dremio:/Samples/samples.dremio.com/SF weather 2018-2019.csv",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "SF weather 2018-2019.csv"  
  ]  
}
```

## File Attributes[​](#file-attributes "Direct link to File Attributes")

entityType String

Type of the catalog object. For files, the entityType is `file`.

Example: file

---

id String

Unique identifier of the file. For files, the ID is the text path of the file within Dremio.

Example: dremio:/Samples/samples.dremio.com/SF weather 2018-2019.csv

---

path Array of String

Path of the file within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the target file itself as the last item in the array.

Example: ["Samples","samples.dremio.com","SF weather 2018-2019.csv"]

## Retrieving a File by Path[​](#retrieving-a-file-by-path "Direct link to Retrieving a File by Path")

Retrieve information about a file by specifying its path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters "Direct link to Parameters")

path Path   String

Path of the file that you want to retrieve, with a forward slash to separate each level of nesting. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, replace colons with `%3A` and replace spaces with `%20`.

Example: Samples/samples.dremio.com/SF%20weather%202018-2019.csv

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Samples/samples.dremio.com/SF%20weather%2018-2019.csv' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "file",  
  "id": "dremio:/Samples/samples.dremio.com/SF weather 2018-2019.csv",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "SF weather 2018-2019.csv"  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

405   Method Not Allowed

500   Internal Server Error

Was this page helpful?

[Previous

Folder](/25.x/reference/api/catalog/container-folder)[Next

Table](/25.x/reference/api/catalog/table)

* [File Attributes](#file-attributes)
* [Retrieving a File by Path](#retrieving-a-file-by-path)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/table

Version: 25.x

On this page

# Table

Use the Catalog API to retrieve [tables](/25.x/sonar/query-manage/managing-data/datasets/), format files and folders as tables, update and refresh tables, and revert tables to files and folders.

Table Object

```
{  
  "entityType": "dataset",  
  "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
  "type": "PHYSICAL_DATASET",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "Dremio University",  
    "restaurant_reviews.parquet"  
  ],  
  "createdAt": "2024-01-13T19:52:01.894Z",  
  "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
  "accelerationRefreshPolicy": {  
    "activePolicyType": "SCHEDULE",  
    "refreshPeriodMs": 3600000,  
    "gracePeriodMs": 10800000,  
    "refreshSchedule": "0 0 8 * * ?",  
    "method": "FULL",  
    "neverExpire": false,  
    "neverRefresh": false,  
    "sourceRefreshOnDataChanges": false  
  },  
  "isMetadataExpired": false,  
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "format": {  
    "type": "Parquet",  
    "name": "restaurant_reviews.parquet",  
    "fullPath": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "ctime": 0,  
    "isFolder": false,  
    "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
    "ignoreOtherFileFormats": false,  
    "autoCorrectCorruptDates": true  
  },  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "_id",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "name",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "city",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "state",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "categories",  
      "type": {  
        "name": "LIST",  
        "subSchema": [  
          {  
            "type": {  
              "name": "VARCHAR"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "review_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "stars",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "attributes",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "Parking",  
            "type": {  
              "name": "STRUCT",  
              "subSchema": [  
                {  
                  "name": "garage",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                },  
                {  
                  "name": "street",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                },  
                {  
                  "name": "lot",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                },  
                {  
                  "name": "valet",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                }  
              ]  
            }  
          },  
          {  
            "name": "Accepts Credit Cards",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "Wheelchair Accessible",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "Price Range",  
            "type": {  
              "name": "BIGINT"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "date",  
      "type": {  
        "name": "VARCHAR"  
      }  
    }  
  ],  
  "approximateStatisticsAllowed": false  
}
```

## Table Attributes[​](#table-attributes "Direct link to Table Attributes")

entityType String

Type of the catalog object. For tables, the entityType is `dataset`.

Example: dataset

---

id String (UUID)

Unique identifier of the table.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

type String

Type of dataset. For tables, the type is `PHYSICAL_DATASET`.

Example: PHYSICAL\_DATASET

---

path Array of String

Path of the table within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the table itself as the last item in the array.

Example: ["Samples","samples.dremio.com","Dremio University","restaurant\_reviews.parquet"]

---

createdAt String

Date and time that the table was created, in UTC format.

Example: 2024-01-13T19:52:01.894Z

---

tag String (UUID)

Unique identifier of the version of the table. Dremio changes the tag whenever the table changes and uses the tag to ensure that PUT requests apply to the most recent version of the table.

Example: cb2905bb-39c0-497f-ae74-4c310d534f25

---

[accelerationRefreshPolicy](/25.x/reference/api/catalog/table#attributes-of-the-accelerationrefreshpolicy-object) String

Attributes that define the acceleration refresh policy for the table.

---

isMetadataExpired Boolean

* If true, the metadata of the table needs to be refreshed. To refresh it, run the ALTER TABLE command, using the clause REFRESH METADATA.
* If false, the metadata can still be used for planning queries against the table.
* If NULL, metadata has never yet been collected for the table.

---

lastMetadataRefreshAt String

Date and time that the table metadata was last refreshed. In UTC format. If NULL, the metadata has never yet been refreshed.

Example: 2024-01-31T09:50:01.012Z

---

[format](/25.x/reference/api/catalog/table#attributes-of-the-format-object) Object

Table format attributes.

---

[accessControlList](/25.x/reference/api/catalog/table#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the table and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if table-specific access control privileges are not set.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the table. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/table#attributes-of-the-owner-object) String

Information about the table's owner.

---

[fields](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-fields-array) Object

Attributes that represent the table schema.

approximateStatisticsAllowed Boolean

If true, `COUNT DISTINCT` queries run on the table return approximate results. Otherwise, false.

Example: {"ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8","ownerType": "USER"}

#### Attributes of the `accelerationRefreshPolicy` Object[​](#attributes-of-the-accelerationrefreshpolicy-object "Direct link to attributes-of-the-accelerationrefreshpolicy-object")

activePolicyType String

Option to set the policy for refreshing Reflections that are defined on the source. For this option to take effect, `neverRefresh` must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: Default. The Reflections are refreshed at the end of every period that is defined by refreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by refreshSchedule.
* `REFRESH_ON_DATA_CHANGES`: Reflections automatically refresh for underlying tables that are in Iceberg format when new snapshots are created after an update. If the Reflection refresh job finds no changes, then no data is updated. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency.

---

refreshPeriodMs Integer

Refresh period for the data in all Reflections for the table, in milliseconds.

Example: 3600000

---

refreshSchedule String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source are refreshed.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:

* `0 0 0 * * ?` : Refreshes every day at midnight.
* `0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
* `0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

gracePeriodMs Integer

Maximum age allowed for Reflection data used to accelerate queries, in milliseconds.

Example: 10800000

---

method String

Approach used for refreshing the data in Reflections defined on tables that are not in the Apache Iceberg format. For more information, read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections).

Enum: FULL, INCREMENTAL

Example: FULL

---

refreshField String

For the `INCREMENTAL` refresh method, the field to refresh for the table. Used only if method is `INCREMENTAL`. This parameter applies only to tables that are not in the Apache Iceberg format.

Example: business\_id

---

neverExpire Boolean

If the Reflection never expires, the value is `true`. Otherwise, the value is `false`.

Example: false

---

neverRefresh Boolean

If the Reflection never refreshes, the value is `true`. Otherwise, the value is `false`.

Example: false

---

sourceRefreshOnDataChanges Boolean

If the table's source is configured so that Reflections on tables in Iceberg format in the source will refresh when new snapshots are created after an update, `true`. Otherwise, `false`.

#### Attributes of the `format` Object[​](#attributes-of-the-format-object "Direct link to attributes-of-the-format-object")

type String

Type of data in the table.

Enum: Delta, Excel, Iceberg, JSON, Parquet, Text, Unknown, XLS

Example: Parquet

---

name String

Table name. Dremio automatically duplicates the name of the origin file or folder to populate this value. The name of the origin file or folder cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: restaurant\_reviews.parquet

---

fullPath Array of String

Path of the table within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the table itself as the last item in the array.

Example: ["Samples", "samples.dremio.com", "Dremio University", "restaurant\_reviews.parquet"]

---

ctime Integer

Not used. Has the value `0`.

Example: 0

---

isFolder Boolean

If the value is `true`, the table was created from a folder. If the value is `false`, the table was created from a file.

Example: false

---

location String

Location, expressed as a string, where the table's metadata is stored within a Dremio source or space.

Example: /samples.dremio.com/Dremio University/restaurant\_reviews.parquet

---

ignoreOtherFileFormats Boolean

If true, Dremio ignores all non-Parquet files in the related folder structure, and the promoted table works as if only Parquet files are in the folder structure. Otherwise, false. Included only for Parquet folders.

Example: false

---

metaStoreType String

Not used. Has the value `HDFS`.

Example: HDFS

---

[parquetDataFormat](/25.x/reference/api/catalog/table#attributes-of-the-parquetdataformat-object) Object

Information about data format for Parquet tables.

---

dataFormatTypeList Array of String

List of data format types in the table. Included only for Iceberg tables, and `PARQUET` is the only valid value.

Example: ["PARQUET"]

---

sheetName String

For tables created from files that contain multiple sheets, the name of the sheet used to create the table.

Example: location\_1

---

extractHeader Boolean

For tables created from files, the value is `true` if Dremio extracted the table's column names from the first line of the file. Otherwise, the value is `false`.

Example: false

---

hasMergedCells Boolean

For tables created from files, the value is `true` if Dremio expanded merged cells in the file when creating the table. Otherwise, the value is `false`.

Example: true

---

fieldDelimiter String

Character used to indicate separate fields in the table. May be `,` for a comma (default), `\t` for a tab, `|` for a pipe, or a custom character.

---

quote String

Character used for quotation marks in the table. May be `\"` for a double quote (default), `'` for a single quote, or a custom character.

---

comment String

Character used to indicate comments in the table. May be `#` for a number sign (default) or a custom character.

---

escape String

Character used to indicate an escape in the table. May be `\"` for a double quote (default), `` ` `` for a back quote, `\\` for a backward slash, or a custom character.

---

lineDelimiter String

Character used to indicate separate lines in the table. May be `\r\n` for a carriage return and a new line (default), `\n` for a new line, or a custom character.

---

skipFirstLine Boolean

If Dremio skipped the first line in the file or folder when creating the table, the value is `true`. Otherwise, the value is `false`.

Example: false

---

autoGenerateColumnNames Boolean

If Dremio used the existing columnn names in the file or folder for the table columns, the value is `true`. Otherwise, the value is `false`.

Example: true

---

trimHeader Boolean

If Dremio trimmed column names to a specific number of characters when creating the table, the value is `true`. Otherwise, the value is `false`.

Example: true

---

autoCorrectCorruptDates Boolean

If Dremio automatically corrects corrupted date fields in the table, the value is `true`. Otherwise, the value is `false`.

Example: true

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the table and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT", "ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT", "ALTER", "MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the table and the specific privileges each role has.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT", "ALTER"]}]

##### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String

Enterprise only. Unique identifier of the user or role with access to the table.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the table. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the table's owner.

Example: 30fca499-4abc-4469-7142-fc8dd29acac8

---

ownerType String

Type of owner of the table.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `fields` Array[​](#attributes-of-objects-in-the-fields-array "Direct link to attributes-of-objects-in-the-fields-array")

name String

Name of the table field.

Example: review\_count

---

[type](/25.x/reference/api/catalog/table#attributes-of-the-type-object) Object

Information about the table field.

##### Attributes of the `type` Object[​](#attributes-of-the-type-object "Direct link to attributes-of-the-type-object")

name String

Name of the table field's type.

Enum: STRUCT, LIST, UNION, INTEGER, BIGINT, FLOAT, DOUBLE, VARCHAR, VARBINARY, BOOLEAN, DECIMAL, TIME, DATE, TIMESTAMP, INTERVAL DAY TO SECOND, INTERVAL YEAR TO MONTH

Example: BIGINT

---

precision Integer

Total number of digits in the number. Included only for the `DECIMAL` type.

Example: 38

---

scale Integer

Number of digits to the right of the decimal point. Included only for the `DECIMAL` type.

Example: 0

---

[subSchema](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-subschema-array) Array of Object

List of objects that represent the field's composition. For example, a field composed of data about a restaurant might have a subSchema with an object for parking options, another for payment methods, and so on. subSchemas may be nested within other subSchemas. subSchema appears only for the `STRUCT`, `LIST`, and `UNION` types.

##### Attributes of Objects in the `subSchema` Array[​](#attributes-of-objects-in-the-subschema-array "Direct link to attributes-of-objects-in-the-subschema-array")

name String

Name for the subSchema object.

Example: Parking

---

type Object

Object that contains a `name` attribute that provides the field's type.

Example: {"name": "BOOLEAN"}

#### Attributes of the `parquetDataFormat` Object[​](#attributes-of-the-parquetdataformat-object "Direct link to attributes-of-the-parquetdataformat-object")

type String

Type of data in the table. Within the parquetDataFormat object, the only valid type is `Parquet`.

Example: Parquet

---

ctime Integer

Not used. Has the value `0`.

Example: 0

---

isFolder Boolean

If the value is `true`, the table was created from a folder. If the value is `false`, the table was created from a file.

Example: true

---

autoCorrectCorruptDates Boolean

If the value is `true`, Dremio automatically corrects corrupted date fields in the table. Otherwise, the value is `false`.

Example: true

## Formatting a File or Folder as a Table[​](#formatting-a-file-or-folder-as-a-table "Direct link to Formatting a File or Folder as a Table")

Format a file or folder as a table so that you can query the data in Dremio.

note

To format a folder, all files in the folder must be the same format.

Method and URL

```
POST /api/v3/catalog/{id}
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String

Unique identifier of the file or folder you want to format. The ID can be a UUID or a text path. If the ID is a text path, use URL encoding to replace special characters with their UTF-8-equivalent characters: `%3A` for a colon; `%2F` for a forward slash, and `%20` for a space. For example, if the ID value is `dremio:/Samples/samples.dremio.com/Dremio University`, the URI-encoded ID is `dremio%3A%2FSamples%2Fsamples.dremio.com%2FDremio%20University`.

Example: c590ed7f-7142-4e1f-ba7d-94173afdc9a3

---

entityType Body   String

Type of the catalog object. To format a file or folder as a table, the entityType is `dataset`.

---

path Body   Array of String

Path of the file or folder you want to format, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the file or folder itself as the last item in the array. Get the path from the file or folder's children object in the response to a [Folder](/25.x/reference/api/catalog/container-folder) request.

Example: ["Samples", "samples.dremio.com", "Dremio University", "restaurant\_reviews.parquet"]

---

type Body   String

Type of dataset. For tables, the type is `PHYSICAL_DATASET`.

---

[accelerationRefreshPolicy](/25.x/reference/api/catalog/table#parameters-of-the-accelerationrefreshpolicy-object) Object

Attributes that define the acceleration refresh policy for the table.

---

[format](/25.x/reference/api/catalog/table#parameters-of-the-format-object) Body   String

Parameters that describe how to format the file or folder.

---

[accessControlList](/25.x/reference/api/catalog/table#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the table and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT", "ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT", "ALTER", "MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT", "ALTER"]}]}

#### Parameters of the `accelerationRefreshPolicy` Object[​](#parameters-of-the-accelerationrefreshpolicy-object "Direct link to parameters-of-the-accelerationrefreshpolicy-object")

activePolicyType Body   String

Policy to use for refreshing Reflections that are defined on the source. For this option to take effect, the neverRefresh parameter must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: Default. The Reflections are refreshed at the end of every period that is defined by refreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by refreshSchedule.
* `REFRESH_ON_DATA_CHANGES`: Reflections automatically refresh for underlying tables that are in Iceberg format when new snapshots are created after an update. If the Reflection refresh job finds no changes, then no data is updated. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency. Only available for tables in Iceberg format.

---

refreshPeriodMs Body   Integer

Refresh period to use for the data in all Reflections for the table. In milliseconds. Optional if you set activePolicyType to `PERIOD`. The default setting is `3600000` milliseconds or one hour, which is also the minimum amount of time that is supported.

Example: 3600000

---

refreshSchedule Body   String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source should be refreshed. Optional if you set activePolicyType to `SCHEDULE`. The default refreshSchedule setting is to refresh every day at 8:00 a.m.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:

* `0 0 0 * * ?` : Refreshes every day at midnight.
* `0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
* `0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

gracePeriodMs Body   Integer

Maximum age to allow for Reflection data used to accelerate queries. In milliseconds.

Example: 10800000

---

method Body   String

Method to use for refreshing the data in Reflections. For tables that are in the Apache Iceberg format; Parquet datasets in filesystems; or Parquet datasets, Avro datasets, or non-transactional ORC datasets in Glue, the value is `AUTO`. In this case, the method used depends on this algorithm:

1. The initial refresh of a Reflection is always a full refresh.
2. If the Reflection is created from a view that uses nested group-bys, joins, unions, or window functions, then a full refresh is performed.
3. If the changes to the base table are only appends, then an incremental refresh based on table snapshots is performed.
4. If the changes to the base table include non-append operations, then a partition-based incremental refresh is attempted.
5. If the partitions of the base table and the partitions of the Reflection are not compatible, or if either the base table or the Reflection is not partitioned, then a full refresh is performed.

Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections) for more information.

Enum: AUTO, FULL, INCREMENTAL

Example: FULL

---

refreshField Body   String

For the `INCREMENTAL` refresh method, the field to refresh for the table. Used only if the method is `INCREMENTAL`. This parameter applies only to tables that are not in the Apache Iceberg format.

Example: business\_id

---

neverExpire Body   Boolean

If the Reflection should never expire, `true`. Otherwise, `false`.

Example: false

---

neverRefresh Body   Boolean

If the Reflection should never refresh, `true`. Otherwise, `false`.

Example: false

#### Parameters of the `format` Object[​](#parameters-of-the-format-object "Direct link to parameters-of-the-format-object")

type Body   String

Type of data in the file or folder. All files in the folder must be the same format.

Enum: Delta, Excel, Iceberg, JSON, Parquet, Text, Unknown, XLS

---

ignoreOtherFileFormats Body   Boolean   Optional

If Dremio should ignore all non-Parquet files in the related folder structure so that the promoted table works as if only Parquet files are in the folder structure, set to `true`. Otherwise, set to `false` (default). Optional for Parquet folders.

Example: false

---

skipFirstLine Body   Boolean   Optional

If Dremio should skip the first line in the file or folder when creating the table, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Excel and Text types.

Example: true

---

extractHeader Body   Boolean   Optional

If Dremio should extract the table's column names from the first line of the file, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Excel and Text types.

Example: "

---

hasMergedCells Body   Boolean   Optional

If Dremio should expand merged cells in the file when creating the table, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Excel type.

Example: true

---

sheetName Body   String   Optional

For tables created from Excel files that contain multiple sheets, the name of the sheet to use to create the table. Default is the first sheet in the file (for files that contain multiple sheets).

Example: location\_1

---

fieldDelimiter Body   String   Optional

Character to use to indicate separate fields in the table. May be `,` for a comma (default), `\t` for a tab, `|` for a pipe, or a custom character. Optional for files or folders of the Text type.

---

quote Body   String   Optional

Character to use for quotes in the table. May be `"` for a double quote (default), `'` for a single quote, or a custom character. Optional for files or folders of the Text type.

---

comment Body   String   Optional

Character to use to indicate comments in the table. May be `#` for a number sign (default) or a custom character. Optional for files or folders of the Text type.

---

escape Body   String   Optional

Character used to indicate an escape in the table. May be `"` for a double quote (default), `` ` `` for a back quote, `\` for a backward slash, or a custom character. Optional for files or folders of the Text type.

---

lineDelimiter Body   String   Optional

Character used to indicate separate lines in the table. May be `\r\n` for a carriage return and a new line (default), `\n` for a new line, or a custom character. Optional for files or folders of the Text type.

---

autoGenerateColumnNames Body   Boolean   Optional

If Dremio should use the existing columnn names in the file or folder for the table columns, set to `true` (default). Otherwise, set to `false`. Optional for files or folders of the Text type.

Example: true

---

trimHeader Body   Boolean   Optional

If Dremio should trim column names to a specific number of characters when creating the table, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Text type.

Example: true

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the table and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the table and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT", "ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the table.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the table. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
    "Samples",  
    "Dremio University",  
    "restaurant_reviews.parquet"  
  ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Parquet"  
  },  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "createdAt": "2024-01-13T19:52:01.894Z",  
    "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
    "accelerationRefreshPolicy": {  
      "activePolicyType": "PERIOD",  
      "refreshPeriodMs": 3600000,  
      "refreshSchedule": "0 56 18 * * *",  
      "gracePeriodMs": 259200000,  
      "method": "FULL",  
      "neverExpire": true,  
      "neverRefresh": false,  
      "sourceRefreshOnDataChanges": false  
    },  
    "isMetadataExpired": false,  
    "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
    "format": {  
      "type": "Parquet",  
      "name": "restaurant_reviews.parquet",  
      "fullPath": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "restaurant_reviews.parquet"  
      ],  
      "ctime": 0,  
      "isFolder": false,  
      "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
      "ignoreOtherFileFormats": "false",  
      "autoCorrectCorruptDates": true  
    },  
    "accessControlList": {  
      "users": [  
        {  
          "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        },  
        {  
          "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
          "permissions": [  
            "SELECT",  
            "ALTER",  
            "MANAGE_GRANTS"  
          ]  
        }  
      ],  
      "roles": [  
        {  
          "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        }  
      ]  
    },  
    "owner": {  
      "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
      "ownerType": "USER"  
    },  
    "fields": [  
      {  
        "name": "_id",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "name",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "city",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "state",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "categories",  
        "type": {  
          "name": "LIST",  
          "subSchema": [  
            {  
              "type": {  
                "name": "VARCHAR"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "review_count",  
        "type": {  
          "name": "BIGINT"  
        }  
      },  
      {  
        "name": "stars",  
        "type": {  
          "name": "DOUBLE"  
        }  
      },  
      {  
        "name": "attributes",  
        "type": {  
          "name": "STRUCT",  
          "subSchema": [  
            {  
              "name": "Parking",  
              "type": {  
                "name": "STRUCT",  
                "subSchema": [  
                  {  
                    "name": "garage",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "street",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "lot",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "valet",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  }  
                ]  
              }  
            },  
            {  
              "name": "Accepts Credit Cards",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Wheelchair Accessible",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Price Range",  
              "type": {  
                "name": "BIGINT"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "date",  
        "type": {  
          "name": "VARCHAR"  
        }  
      }  
    ],  
    "approximateStatisticsAllowed": false  
  }
```

Example Request for Excel format type

```
curl -X POST 'https://{hostname}/api/v3/catalog/dremio%3A%2FSamples%2Fsamples.dremio.com%2FDremio%20University%2Foracle-departments.xlsx' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "oracle-departments.xlsx"  
    ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Excel",  
    "extractHeader": true,  
    "hasMergedCells": true,  
    "sheetName": "Sheet1"  
    }  
}'
```

Example Request for Text format type

```
curl -X POST 'https://{hostname}/api/v3/catalog/6ba3bd6e-fd27-4572-a535-77e1548283b3' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "Dremio University",  
    "airbnb_listings.csv"  
  ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Text",  
    "fieldDelimiter": ",",  
    "skipFirstLine": false,  
    "extractHeader": true,  
    "quote": "\"",  
    "comment": "#",  
    "escape": "\"",  
    "lineDelimiter": "\r\n",  
    "autoGenerateColumnNames": true,  
    "trimHeader": false  
  }  
}'
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a Table by ID[​](#retrieving-a-table-by-id "Direct link to Retrieving a Table by ID")

Retrieve a table by specifying the table's `id` value.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to retrieve.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "createdAt": "2024-01-13T19:52:01.894Z",  
    "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
    "accelerationRefreshPolicy": {  
      "activePolicyType": "PERIOD",  
      "refreshPeriodMs": 3600000,  
      "refreshSchedule": "0 56 18 * * *",  
      "gracePeriodMs": 259200000,  
      "method": "FULL",  
      "neverExpire": true,  
      "neverRefresh": false,  
      "sourceRefreshOnDataChanges": false  
    },  
    "isMetadataExpired": false,  
    "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
    "format": {  
      "type": "Parquet",  
      "name": "restaurant_reviews.parquet",  
      "fullPath": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "restaurant_reviews.parquet"  
      ],  
      "ctime": 0,  
      "isFolder": false,  
      "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
      "ignoreOtherFileFormats": false,  
      "autoCorrectCorruptDates": true  
    },  
    "accessControlList": {  
      "users": [  
        {  
          "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        },  
        {  
          "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
          "permissions": [  
            "SELECT",  
            "ALTER",  
            "MANAGE_GRANTS"  
          ]  
        }  
      ],  
      "roles": [  
        {  
          "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        }  
      ]  
    },  
    "owner": {  
      "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
      "ownerType": "USER"  
    },  
    "fields": [  
      {  
        "name": "_id",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "name",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "city",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "state",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "categories",  
        "type": {  
          "name": "LIST",  
          "subSchema": [  
            {  
              "type": {  
                "name": "VARCHAR"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "review_count",  
        "type": {  
          "name": "BIGINT"  
        }  
      },  
      {  
        "name": "stars",  
        "type": {  
          "name": "DOUBLE"  
        }  
      },  
      {  
        "name": "attributes",  
        "type": {  
          "name": "STRUCT",  
          "subSchema": [  
            {  
              "name": "Parking",  
              "type": {  
                "name": "STRUCT",  
                "subSchema": [  
                  {  
                    "name": "garage",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "street",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "lot",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "valet",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  }  
                ]  
              }  
            },  
            {  
              "name": "Accepts Credit Cards",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Wheelchair Accessible",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Price Range",  
              "type": {  
                "name": "BIGINT"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "date",  
        "type": {  
          "name": "VARCHAR"  
        }  
      }  
    ],  
    "approximateStatisticsAllowed": false  
  }
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Table by Path[​](#retrieving-a-table-by-path "Direct link to Retrieving a Table by Path")

Retrieve a table by specifying the table's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Table's location within Dremio, using forward slashes as separators. For example, for the "NYC-taxi-trips" table in the "samples.dremio.com" folder within the source "Samples," the path is `Samples/samples.dremio.com/NYC-taxi-trips`. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: Samples/samples.dremio.com/Dremio%20University/restaurant\_reviews.parquet

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Samples/samples.dremio.com/Dremio%20University/restaurant_reviews.parquet' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "createdAt": "2024-01-13T19:52:01.894Z",  
    "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
    "accelerationRefreshPolicy": {  
      "activePolicyType": "PERIOD",  
      "refreshPeriodMs": 3600000,  
      "refreshSchedule": "0 56 18 * * *",  
      "gracePeriodMs": 259200000,  
      "method": "FULL",  
      "neverExpire": true,  
      "neverRefresh": false,  
      "sourceRefreshOnDataChanges": false  
    },  
    "isMetadataExpired": false,  
    "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
    "format": {  
      "type": "Parquet",  
      "name": "restaurant_reviews.parquet",  
      "fullPath": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "restaurant_reviews.parquet"  
      ],  
      "ctime": 0,  
      "isFolder": false,  
      "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
      "ignoreOtherFileFormats": false,  
      "autoCorrectCorruptDates": true  
    },  
    "accessControlList": {  
      "users": [  
        {  
          "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        },  
        {  
          "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
          "permissions": [  
            "SELECT",  
            "ALTER",  
            "MANAGE_GRANTS"  
          ]  
        }  
      ],  
      "roles": [  
        {  
          "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        }  
      ]  
    },  
    "owner": {  
      "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
      "ownerType": "USER"  
    },  
    "fields": [  
      {  
        "name": "_id",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "name",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "city",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "state",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "categories",  
        "type": {  
          "name": "LIST",  
          "subSchema": [  
            {  
              "type": {  
                "name": "VARCHAR"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "review_count",  
        "type": {  
          "name": "BIGINT"  
        }  
      },  
      {  
        "name": "stars",  
        "type": {  
          "name": "DOUBLE"  
        }  
      },  
      {  
        "name": "attributes",  
        "type": {  
          "name": "STRUCT",  
          "subSchema": [  
            {  
              "name": "Parking",  
              "type": {  
                "name": "STRUCT",  
                "subSchema": [  
                  {  
                    "name": "garage",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "street",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "lot",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "valet",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  }  
                ]  
              }  
            },  
            {  
              "name": "Accepts Credit Cards",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Wheelchair Accessible",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Price Range",  
              "type": {  
                "name": "BIGINT"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "date",  
        "type": {  
          "name": "VARCHAR"  
        }  
      }  
    ],  
    "approximateStatisticsAllowed": false  
  }
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Table[​](#updating-a-table "Direct link to Updating a Table")

Update the specified table in Dremio.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to update.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

entityType Body   String

Type of the catalog object. For tables, the entityType is `dataset`.

---

id Body   String (UUID)

Unique identifier of the table that you want to update.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

path Body   Array of String

Path of the table that you want to update, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the table itself as the last item in the array. Get the path from the table's children object in the response to a [Folder](/25.x/reference/api/catalog/container-folder) request.

Example: ["Samples", "samples.dremio.com", "Dremio University", "restaurant\_reviews.parquet"]

---

tag Body   String (UUID)   Optional

Unique identifier of the version of the table that you want to update. If you provide a tag in the request body, Dremio uses the tag to ensure that you are requesting to update the most recent version of the table. If you do not provide a tag, Dremio automatically updates the most recent version of the table.

Example: cb2905bb-39c0-497f-ae74-4c310d534f25

---

type Body   String

Type of dataset. For tables, the type is `PHYSICAL_DATASET`.

Example:

---

[accelerationRefreshPolicy](/25.x/reference/api/catalog/table#parameters-of-the-accelerationrefreshpolicy-object-1) Object

Attributes that define the acceleration refresh policy for the table.

---

[format](/25.x/reference/api/catalog/table#parameters-of-the-format-object-1) Body   String

Parameters that describe the table's format.

---

[accessControlList](/25.x/reference/api/catalog/table#parameters-of-the-accesscontrollist-object-1) Body   String   Optional

Enterprise only. Object used to specify which users and roles should have access to the table and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]}

---

#### Parameters of the `accelerationRefreshPolicy` Object[​](#parameters-of-the-accelerationrefreshpolicy-object-1 "Direct link to parameters-of-the-accelerationrefreshpolicy-object-1")

activePolicyType Body   String

Policy to use for refreshing Reflections that are defined on the source. For this option to take effect, the neverRefresh parameter must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: Default. The Reflections are refreshed at the end of every period that is defined by refreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by refreshSchedule.
* `REFRESH_ON_DATA_CHANGES`: Reflections automatically refresh for underlying tables that are in Iceberg format when new snapshots are created after an update. If the Reflection refresh job finds no changes, then no data is updated. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency. Only available for tables in Iceberg format.

---

refreshPeriodMs Body   Integer

Refresh period to use for the data in all Reflections for the table. In milliseconds. Optional if you set activePolicyType to `PERIOD`. The default setting is `3600000` milliseconds or one hour, which is also the minimum amount of time that is supported.

Example: 3600000

---

refreshSchedule Body   String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source should be refreshed. Optional if you set activePolicyType to `SCHEDULE`. The default refreshSchedule setting is to refresh every day at 8:00 a.m.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:

* `0 0 0 * * ?` : Refreshes every day at midnight.
* `0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
* `0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

gracePeriodMs Body   Integer

Maximum age to allow for Reflection data used to accelerate queries. In milliseconds.

Example: 10800000

---

method Body   String

Method to use for refreshing the data in Reflections. For tables that are in the Apache Iceberg format; Parquet datasets in filesystems; or Parquet datasets, Avro datasets, or non-transactional ORC datasets in Glue, the value is `AUTO`. In this case, the method used depends on this algorithm:

1. The initial refresh of a Reflection is always a full refresh.
2. If the Reflection is created from a view that uses nested group-bys, joins, unions, or window functions, then a full refresh is performed.
3. If the changes to the base table are only appends, then an incremental refresh based on table snapshots is performed.
4. If the changes to the base table include non-append operations, then a partition-based incremental refresh is attempted.
5. If the partitions of the base table and the partitions of the Reflection are not compatible, or if either the base table or the Reflection is not partitioned, then a full refresh is performed.

Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections) for more information.

Enum: AUTO, FULL, INCREMENTAL

Example: FULL

---

refreshField Body   String

For the `INCREMENTAL` refresh method, the field to refresh for the table. Used only if the method is `INCREMENTAL`. This parameter applies only to tables that are not in the Apache Iceberg format.

Example: business\_id

---

neverExpire Body   Boolean

If the Reflection should never expire, `true`. Otherwise, `false`.

Example: false

---

neverRefresh Body   Boolean

If the Reflection should never refresh, `true`. Otherwise, `false`.

Example: false

#### Parameters of the `format` Object[​](#parameters-of-the-format-object-1 "Direct link to parameters-of-the-format-object-1")

type Body   String

Type of data in the table.

Enum: Delta, Excel, Iceberg, JSON, Parquet, Text, Unknown, XLS

---

skipFirstLine Body   Boolean   Optional

If Dremio should skip the first line in the table, set to `true`. Otherwise, set to `false` (default). Optional for Excel and Text types.

Example: true

---

extractHeader Body   Boolean   Optional

If Dremio should extract the table's column names from the first line of the file, set to `true`. Otherwise, set to `false` (default). Optional for tables created from files or folders of the Excel and Text types.

Example: true

---

hasMergedCells Body   Boolean   Optional

If Dremio should expand merged cells in the table, set to `true`. Otherwise, set to `false` (default). Optional for tables created from files or folders of the Excel type.

Example: true

---

fieldDelimiter Body   String   Optional

Character to use to indicate separate fields in the table. May be `,` for a comma (default), `\t` for a tab, `|` for a pipe, or a custom character. Optional for tables created from files or folders of the Text type.

---

quote Body   String   Optional

Character to use for quotes in the table. May be `\"` for a double quote (default), `'` for a single quote, or a custom character. Optional for tables created from files or folders of the Text type.

---

comment Body   String   Optional

Character to use to indicate comments for the table. May be `#` for a number sign (default) or a custom character. Optional for tables created from files or folders of the Text type.

---

escape Body   String   Optional

Character to use to indicate an escape for the table. May be `\"` for a double quote (default), `` ` `` for a back quote, `\\` for a backward slash, or a custom character. Optional for tables created from files or folders of the Text type.

---

lineDelimiter Body   String   Optional

Character to use to indicate separate lines for the table. May be `\r\n` for a carriage return and a new line (default), `\n` for a new line, or a custom character. Optional for tables created from files or folders of the Text type.

Example:

---

autoGenerateColumnNames Body   Boolean   Optional

If Dremio should use the existing columnn names for the table columns, set to `true` (default). Otherwise, set to `false`. Optional for tables created from files or folders of the Text type.

Example: true

---

trimHeader Body   Boolean   Optional

If Dremio should trim column names to a specific number of characters when updating the table, set to `true`. Otherwise, set to `false` (default). Optional for tables created from files or folders of the Text type.

Example: true

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the table and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the table and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String

Enterprise only. Unique identifier of the user or role that should have access to the table.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String

Enterprise only. List of privileges the user or role should have on the table. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/dba1e4fe-6351-44d2-a3e0-7aa20e782bf3' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "id": "dba1e4fe-6351-44d2-a3e0-7aa20e782bf3",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "Dremio University",  
    "airbnb_listings.csv"  
  ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Text",  
    "fieldDelimiter": ",",  
    "skipFirstLine": false,  
    "extractHeader": true,  
    "quote": "\"",  
    "comment": "#",  
    "escape": "\"",  
    "lineDelimiter": "\r\n",  
    "autoGenerateColumnNames": true,  
    "trimHeader": true  
  }  
}'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "dba1e4fe-6351-44d2-a3e0-7aa20e782bf3",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "airbnb_listings.csv"  
    ],  
    "createdAt": "2024-01-23T21:26:59.568Z",  
    "tag": "fc1707df-35a1-45c1-87d7-5f66fb11a729",  
    "format": {  
        "type": "Text",  
        "ctime": 0,  
        "isFolder": false,  
        "location": "/samples.dremio.com/Dremio University/airbnb_listings.csv",  
        "fieldDelimiter": ",",  
        "skipFirstLine": false,  
        "extractHeader": true,  
        "quote": "\"",  
        "comment": "#",  
        "escape": "\"",  
        "lineDelimiter": "\r\n",  
        "autoGenerateColumnNames": true,  
        "trimHeader": true  
    },  
    "accessControlList": {},  
    "owner": {  
        "ownerId": "c590ed7f-7142-4e1f-ba7d-94173afdc9a3",  
        "ownerType": "USER"  
    },  
    "fields": [  
        {  
            "name": "id",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "listing_url",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "scrape_id",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "last_scraped",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "name",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "summary",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "reviews_per_month",  
            "type": {  
                "name": "VARCHAR"  
            }  
        }  
    ],  
    "approximateStatisticsAllowed": false  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Refreshing the Reflections on a Table[​](#refreshing-the-reflections-on-a-table "Direct link to Refreshing the Reflections on a Table")

Refresh the Reflections associated with the specified table.

note

Refreshing a table's Reflections does not refresh its metadata. Read [Refreshing Metadata](/25.x/admin/metadata-caching/) to learn how to refresh table metadata. Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections/) for more information about refreshing Reflections.

Method and URL

```
POST /api/v3/catalog/{id}/refresh
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to refresh.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72/refresh' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Reverting a Table to a File or Folder[​](#reverting-a-table-to-a-file-or-folder "Direct link to Reverting a Table to a File or Folder")

Revert a table in a source to change the data in the table back to its original format, file or folder. For more information, read [Formatting Data to a Table](/25.x/sonar/data-sources/entity-promotion/) and [Removing Formatting on Data](/25.x/sonar/data-sources/entity-promotion/)

note

If a table is saved in your home space, the revert request will delete the table entirely. The revert endpoint only changes a table back to a file or folder if the table is saved in a source.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to revert to a file or folder.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

File](/25.x/reference/api/catalog/file)[Next

User-Defined Function](/25.x/reference/api/catalog/user-defined-function)

* [Table Attributes](#table-attributes)
* [Formatting a File or Folder as a Table](#formatting-a-file-or-folder-as-a-table)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Table by ID](#retrieving-a-table-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Table by Path](#retrieving-a-table-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Table](#updating-a-table)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Refreshing the Reflections on a Table](#refreshing-the-reflections-on-a-table)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)
* [Reverting a Table to a File or Folder](#reverting-a-table-to-a-file-or-folder)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/user-defined-function

Version: 25.x

On this page

# User-Defined Function

Use the Catalog API to retrieve information about user-defined functions (UDFs), as well as to create, update, and delete UDFs.

User-Defined Function Object

```
{  
  "entityType": "function",  
  "id": "1568aa06-4eac-48cf-bc30-2aa3053c2840",  
  "path": [  
    "team_folder",  
    "test_subfolder",  
    "filter_domain_orderdates"  
  ],  
  "tag": "qBWpD7x6+Ws=",  
  "createdAt": "2024-08-01T20:20:38.547Z",  
  "lastModified": "2024-08-01T20:20:38.547Z",  
  "isScalar": false,  
  "functionArgList": "\"domain\" CHARACTER VARYING, \"orderdate\" DATE",  
  "functionBody": "SELECT \"name\", \"email\", \"order_date\" FROM \"customer_data\" WHERE LOWER(\"email\") LIKE '%' || LOWER(domain) AND \"order_date\" >= orderdate",  
  "returnType": "\"name\" CHARACTER VARYING, \"email\" CHARACTER VARYING, \"order_date\" DATE",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "4740ab48-39c6-434c-9086-8f6e52e65349",  
    "ownerType": "USER"  
  }  
}
```

## User-Defined Function Attributes[​](#user-defined-function-attributes "Direct link to User-Defined Function Attributes")

entityType String

Type of the catalog object. For user-defined functions, the entityType is `function`.

---

id String (UUID)

Unique identifier of the user-defined function.

Example: 1568aa06-4eac-48cf-bc30-2aa3053c2840

---

path Array of String

Path of the user-defined function within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the name of the function itself as the last item in the array.

Example: ["team\_folder","test\_subfolder","filter\_domain\_orderdates"]

---

tag String

Unique identifier of the version of the user-defined function. Dremio changes the tag whenever the function changes and uses the tag to ensure that PUT requests apply to the most recent version of the function.

Example: qBWpD7x6+Ws=

---

createdAt String

Date and time at which the user-defined function was created, in UTC format.

Example: 2024-08-01T20:20:38.547Z

---

lastModified String

Date and time at which the user-defined function was last modified, in UTC format.

Example: 2024-08-01T20:20:38.547Z

---

isScalar Boolean

If the user-defined function is a scalar function, `true`. If the user-defined function is a tabular function, `false`.

Example: false

---

functionArgList String

The user-defined function's arguments and their [data types](/25.x/reference/sql/data-types/). If the function includes multiple arguments, the arguments are separated with a comma.

note

In response objects, the functionArgList value may contain aliases for data types, such as `CHARACTER VARYING` (an alias for `VARCHAR`).

Example: "domain" CHARACTER VARYING, "orderdate" DATE

---

functionBody String

The statement that the user-defined function executes.

Example: SELECT "name", "email", "order\_date" FROM "customer\_data" WHERE LOWER("email") LIKE '%' || LOWER(domain) AND "order\_date" >= orderdate

---

returnType String

The [data type](/25.x/reference/sql/data-types/) of the result that the function returns (for scalar functions) or of each column that the function returns, separated by commas (for tabular functions).

Example: "name" CHARACTER VARYING, "email" CHARACTER VARYING, "order\_date" DATE

---

[accessControlList](/25.x/reference/api/catalog/user-defined-function#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the user-defined function and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if function-specific access control privileges are not set.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALTER","EXECUTE"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["ALTER","EXECUTE"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the user-defined function. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [User-Defined Function (UDF) Privileges](/25.x/security/rbac/privileges/#user-defined-function-udf-privileges).

---

[owner](/25.x/reference/api/catalog/user-defined-function#attributes-of-the-owner-object) Object

Information about the user-defined function's owner.

Example: {"ownerId": "4740ab48-39c6-434c-9086-8f6e52e65349","ownerType": "USER"}

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/user-defined-function#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the user-defined function and the specific privileges each user has.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5", "permissions": ["ALTER","EXECUTE"]}]

---

[roles](/25.x/reference/api/catalog/user-defined-function#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the user-defined function and the specific privileges each role has.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889", "permissions": ["ALTER","EXECUTE"]}]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the user-defined function's owner.

Example: 4740ab48-39c6-434c-9086-8f6e52e65349

---

ownerType String

Type of owner of the user-defined function.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String

Enterprise only. Unique identifier of the user or role with access to the user-defined function.

Example: 4740ab48-39c6-434c-9086-8f6e52e65349

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the user-defined function. For more information, read [User-Defined Function (UDF) Privileges](/25.x/security/rbac/privileges/#user-defined-function-udf-privileges).

Enum: ALTER, EXECUTE, MANAGE\_GRANTS, OWNERSHIP

Example: ["ALTER","EXECUTE"]

## Creating a User-Defined Function[​](#creating-a-user-defined-function "Direct link to Creating a User-Defined Function")

Create a new user-defined function.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object. For user-defined functions, the entityType is `function`.

---

path Body   Array of String

Path where you want to create the user-defined function within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the name of the function itself as the last item in the array.

Example: ["team\_folder","test\_subfolder","filter\_domain\_orderdates"]

---

isScalar Body   Boolean

If the user-defined function is a scalar function, `true`. If the user-defined function is a tabular function, `false`.

Example: false

---

functionArgList Body   String

The name of each argument in the user-defined function and the argument's [data type](/25.x/reference/sql/data-types/). Separate the name and data type with a single space. If the function includes multiple arguments, separate the arguments with a comma.

note

In response objects, the functionArgList value may contain aliases for data types, such as `CHARACTER VARYING` (an alias for `VARCHAR`).

Example: domain VARCHAR, orderdate DATE

---

functionBody Body   String

The statement that the user-defined function should execute.

Example: SELECT name, email, order\_date FROM customer\_data WHERE LOWER(email) LIKE '%' || LOWER(domain) AND order\_date >= orderdate

---

returnType Body   String

The [data type](/25.x/reference/sql/data-types/) of each column that the user-defined function should return.

Example: name VARCHAR, email VARCHAR, order\_date DATE

---

[accessControlList](/25.x/reference/api/catalog/user-defined-function#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the user-defined function and the specific privileges each user or role should have. May include an array of users, an array of roles, or both. Omit if you do not want to configure function-specific access control privileges.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALTER","EXECUTE"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["ALTER","EXECUTE"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/user-defined-function#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the user-defined function and the specific privileges each user should have.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALTER","EXECUTE"]}]

---

[roles](/25.x/reference/api/catalog/user-defined-function#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the user-defined function and the specific privileges each role should have.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["ALTER","EXECUTE"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the user-defined function.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the user-defined function. For more information, read [User-Defined Function (UDF) Privileges](/25.x/security/rbac/privileges/#user-defined-function-udf-privileges).

Enum: ALTER, EXECUTE, MANAGE\_GRANTS, OWNERSHIP

Example: ["ALTER","EXECUTE"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "function",  
  "path": [  
    "team_folder",  
    "test_subfolder",  
    "filter_domain_orderdates"  
  ],  
  "isScalar": false,  
  "functionArgList": "domain VARCHAR, orderdate DATE",  
  "functionBody": "SELECT name, email, order_date FROM customer_data WHERE LOWER(email) LIKE '%' || LOWER(domain) AND order_date >= orderdate",  
  "returnType": "name VARCHAR, email VARCHAR, order_date DATE",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
        "ALTER",  
        "EXECUTE"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
        "ALTER",  
        "EXECUTE"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "function",  
  "id": "1568aa06-4eac-48cf-bc30-2aa3053c2840",  
  "path": [  
    "team_folder",  
    "test_subfolder",  
    "filter_domain_orderdates"  
  ],  
  "tag": "qBWpD7x6+Ws=",  
  "createdAt": "2024-08-01T20:20:38.547Z",  
  "lastModified": "2024-08-01T20:20:38.547Z",  
  "isScalar": false,  
  "functionArgList": "\"domain\" CHARACTER VARYING, \"orderdate\" DATE",  
  "functionBody": "SELECT \"name\", \"email\", \"order_date\" FROM \"customer_data\" WHERE LOWER(\"email\") LIKE '%' || LOWER(domain) AND \"order_date\" >= orderdate",  
  "returnType": "\"name\" CHARACTER VARYING, \"email\" CHARACTER VARYING, \"order_date\" DATE",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "4740ab48-39c6-434c-9086-8f6e52e65349",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

409   Conflict

## Retrieving a User-Defined Function by ID[​](#retrieving-a-user-defined-function-by-id "Direct link to Retrieving a User-Defined Function by ID")

Retrieve a user-defined function and information about its contents by specifying the function's ID.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user-defined function that you want to retrieve.

Example: 1568aa06-4eac-48cf-bc30-2aa3053c2840

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/1568aa06-4eac-48cf-bc30-2aa3053c2840' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "function",  
  "id": "1568aa06-4eac-48cf-bc30-2aa3053c2840",  
  "path": [  
    "team_folder",  
    "test_subfolder",  
    "filter_domain_orderdates"  
  ],  
  "tag": "qBWpD7x6+Ws=",  
  "createdAt": "2024-08-01T20:20:38.547Z",  
  "lastModified": "2024-08-01T20:20:38.547Z",  
  "isScalar": false,  
  "functionArgList": "\"domain\" CHARACTER VARYING, \"orderdate\" DATE",  
  "functionBody": "SELECT \"name\", \"email\", \"order_date\" FROM \"customer_data\" WHERE LOWER(\"email\") LIKE '%' || LOWER(domain) AND \"order_date\" >= orderdate",  
  "returnType": "\"name\" CHARACTER VARYING, \"email\" CHARACTER VARYING, \"order_date\" DATE",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "4740ab48-39c6-434c-9086-8f6e52e65349",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a User-Defined Function by Path[​](#retrieving-a-user-defined-function-by-path "Direct link to Retrieving a User-Defined Function by Path")

Retrieve a user-defined function and information about its contents by specifying the function's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Path of the user-defined function within Dremio. The path consists of the source or space, followed by any folder and subfolders, followed by the name of the function itself. Separate each level of the path with a forward slash.

Example: team\_folder/test\_subfolder/filter\_domain\_orderdates

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/team_folder/test_subfolder/filter_domain_orderdates' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "function",  
  "id": "1568aa06-4eac-48cf-bc30-2aa3053c2840",  
  "path": [  
    "team_folder",  
    "test_subfolder",  
    "filter_domain_orderdates"  
  ],  
  "tag": "qBWpD7x6+Ws=",  
  "createdAt": "2024-08-01T20:20:38.547Z",  
  "lastModified": "2024-08-01T20:20:38.547Z",  
  "isScalar": false,  
  "functionArgList": "\"domain\" CHARACTER VARYING, \"orderdate\" DATE",  
  "functionBody": "SELECT \"name\", \"email\", \"order_date\" FROM \"customer_data\" WHERE LOWER(\"email\") LIKE '%' || LOWER(domain) AND \"order_date\" >= orderdate",  
  "returnType": "\"name\" CHARACTER VARYING, \"email\" CHARACTER VARYING, \"order_date\" DATE",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "4740ab48-39c6-434c-9086-8f6e52e65349",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a User-Defined Function[​](#updating-a-user-defined-function "Direct link to Updating a User-Defined Function")

Update the specified user-defined function.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user-defined function that you want to update.

Example: 1568aa06-4eac-48cf-bc30-2aa3053c2840

---

entityType Body   String

Type of the catalog object. For user-defined functions, the entityType is `function`.

---

id Body   String (UUID)

Unique identifier of the user-defined function that you want to update.

Example: 1568aa06-4eac-48cf-bc30-2aa3053c2840

---

path Body   Array of String

Path of the user-defined function within Dremio, expressed as an array. The path consists of the source or user-defined function, followed by any folder and subfolders, followed by the name of the function itself as the last item in the array.

Example: ["team\_folder","test\_subfolder","filter\_domain\_orderdates"]

---

tag Body   String

Unique identifier of the version of the user-defined function that you want to update. Dremio uses the tag to ensure that you are requesting to update the most recent version of the user-defined function.

Example: qBWpD7x6+Ws=

---

isScalar Body   Boolean

If the user-defined function is a scalar function, `true`. If the user-defined function is a tabular function, `false`.

Example: false

---

functionArgList Body   String

The name of each argument in the user-defined function and the argument's [data type](/25.x/reference/sql/data-types/). Separate the name and data type with a single space. If the function includes multiple arguments, separate the arguments with a comma.

note

In response objects, the functionArgList value may contain aliases for data types, such as `CHARACTER VARYING` (an alias for `VARCHAR`).

Example: domain VARCHAR, orderdate DATE

---

functionBody Body   String

The statement that the user-defined function should execute.

Example: SELECT name, email, phone\_number, order\_date FROM customer\_data WHERE LOWER(email) LIKE '%' || LOWER(domain) AND order\_date >= orderdate

---

returnType Body   String

The [data type](/25.x/reference/sql/data-types/) of each column that the user-defined function should return.

Example: name VARCHAR, email VARCHAR, phone\_number VARCHAR, order\_date DATE

---

[accessControlList](/25.x/reference/api/catalog/user-defined-function#parameters-of-the-accesscontrollist-object-1) Body   String   Optional

Enterprise only. Object used to specify which users and roles should have access to the user-defined function and the specific privileges each user or role should have. If you omit the accessControlList object in a PUT request, Dremio removes all existing user and role access settings from the function. To keep existing user and role access settings while making other updates, duplicate the existing accessControlList array in the PUT request.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALTER","EXECUTE", "MANAGE\_GRANTS"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["ALTER","EXECUTE"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/user-defined-function#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the user-defined function and the specific privileges each user should have. If you omit the users object in a PUT request, Dremio removes all existing user access settings from the function. To keep existing user access settings while making other updates, duplicate the existing users array in the PUT request.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5", "permissions": ["ALTER","EXECUTE", "MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/user-defined-function#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the user-defined function and the specific privileges each role should have. If you omit the roles object in a PUT request, Dremio removes all existing role access settings from the function. To keep existing role access settings while making other updates, duplicate the existing roles array in the PUT request.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889", "permissions": ["ALTER","EXECUTE"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the user-defined function.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the user-defined function. For more information, read [User-Defined Function (UDF) Privileges](/25.x/security/rbac/privileges/#user-defined-function-udf-privileges).

Enum: ALTER, EXECUTE, MANAGE\_GRANTS, OWNERSHIP

Example: ["ALTER","EXECUTE", "MANAGE\_GRANTS"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/1568aa06-4eac-48cf-bc30-2aa3053c2840' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "function",  
  "id": "1568aa06-4eac-48cf-bc30-2aa3053c2840",  
  "path": [  
    "team_folder",  
    "test_subfolder",  
    "filter_domain_orderdates"  
  ],  
  "tag": "qBWpD7x6+Ws=",  
  "isScalar": false,  
  "functionArgList": "domain VARCHAR, orderdate DATE",  
  "functionBody": "SELECT name, email, phone_number, order_date FROM customer_data WHERE LOWER(email) LIKE '%' || LOWER(domain) AND order_date >= orderdate",  
  "returnType": "name VARCHAR, email VARCHAR, phone_number VARCHAR, order_date DATE",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER",  
          "EXECUTE",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
        "ALTER",  
        "EXECUTE"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "function",  
  "id": "1568aa06-4eac-48cf-bc30-2aa3053c2840",  
  "path": [  
    "team_folder",  
    "test_subfolder",  
    "filter_domain_orderdates"  
  ],  
  "tag": "4RuPbmWPoa9=",  
  "createdAt": "2024-08-01T20:20:38.547Z",  
  "lastModified": "2024-08-07T17:17:17.360Z",  
  "isScalar": false,  
  "functionArgList": "\"domain\" CHARACTER VARYING, \"orderdate\" DATE",  
  "functionBody": "SELECT \"name\", \"email\", \"phone_number\", \"order_date\" FROM \"customer_data\" WHERE LOWER(\"email\") LIKE '%' || LOWER(domain) AND \"order_date\" >= orderdate",  
  "returnType": "\"name\" CHARACTER VARYING, \"email\" CHARACTER VARYING, \"phone_number\" CHARACTER VARYING, \"order_date\" DATE",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER",  
          "EXECUTE",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "ALTER",  
          "EXECUTE"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "4740ab48-39c6-434c-9086-8f6e52e65349",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Deleting a User-Defined Function[​](#deleting-a-user-defined-function "Direct link to Deleting a User-Defined Function")

Delete the specified user-defined function.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user-defined function that you want to delete.

Example: 1568aa06-4eac-48cf-bc30-2aa3053c2840

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/1568aa06-4eac-48cf-bc30-2aa3053c2840' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Table](/25.x/reference/api/catalog/table)[Next

View](/25.x/reference/api/catalog/view)

* [User-Defined Function Attributes](#user-defined-function-attributes)
* [Creating a User-Defined Function](#creating-a-user-defined-function)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a User-Defined Function by ID](#retrieving-a-user-defined-function-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a User-Defined Function by Path](#retrieving-a-user-defined-function-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a User-Defined Function](#updating-a-user-defined-function)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a User-Defined Function](#deleting-a-user-defined-function)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/view

Version: 25.x

On this page

# View

Use the Catalog API to retrieve, create, update, and delete [views](/25.x/sonar/query-manage/managing-data/datasets/).

View Object

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",   
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

## View Attributes[​](#view-attributes "Direct link to View Attributes")

entityType String

Type of the catalog object. For views, the entityType is `dataset`.

Example: dataset

---

id String (UUID)

Unique identifier of the view.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

---

type String

Type of dataset. For views, the type is `VIRTUAL_DATASET`.

Example: VIRTUAL\_DATASET

---

path Array of String

Path of the view within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the view itself as the last item in the array.

Example: ["Business", "Transportation", "NYC-taxi-trips-short-distance"]

---

createdAt String

Date and time that the view was created, in UTC format.

Example: 2022-11-17T18:31:23.236Z

---

isMetadataExpired Boolean

* If true, the metadata of the tables that the view is defined on needs to be refreshed. To refresh it, run the ALTER VIEW command, using the clause REFRESH METADATA.
* If false, the metadata can still be used for planning queries against the view.
* If NULL, metadata has never yet been collected for the tables that the view is defined on.

---

lastMetadataRefreshAt String

Date and time that the metadata of the tables that the view is defined on was last refreshed. In UTC format.

Example: 2024-01-31T09:50:01.012Z

---

tag String (UUID)

Unique identifier of the version of the view. Dremio changes the tag whenever the view changes and uses the tag to ensure that PUT requests apply to the most recent version of the view.

Example: f90d1526-e64b-47b1-9ab0-d25df5247cab

---

sql String

SQL query used to create the view.

Example: SELECT \* FROM "NYC-taxi-trips" WHERE trip\_distance\_mi <= 2.0 ORDER BY trip\_distance\_mi ASC

---

sqlContext Array of String

Context for the SQL query used to create the view.

Example: ["Samples", "samples.dremio.com"]

---

[accessControlList](/25.x/reference/api/catalog/view#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the view and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if view-specific access control privileges are not set.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"] },{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"] }],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the view. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/view#attributes-of-the-owner-object) String

Information about the view's owner.

Example: {"ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8","ownerType": "USER"}

---

[fields](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-fields-array) Array of Object

Attributes that represent the dataset schema.

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the view and the specific privileges each user has.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT", "ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT", "ALTER", "MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the view and the specific privileges each role has.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String

Enterprise only. Unique identifier of the user or role with access to the view.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the view. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT","ALTER"]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the view's owner.

Example: 30fca499-4abc-4469-7142-fc8dd29acac8

---

ownerType String

Type of owner of the view.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `fields` Array[​](#attributes-of-objects-in-the-fields-array "Direct link to attributes-of-objects-in-the-fields-array")

name String

Name of the view field.

Example: pickup\_datetime

---

[type](/25.x/reference/api/catalog/view#attributes-of-the-type-object) Object

Information about the view field.

#### Attributes of the `type` Object[​](#attributes-of-the-type-object "Direct link to attributes-of-the-type-object")

name String

Name of the view field's type.

Enum: STRUCT, LIST, UNION, INTEGER, BIGINT, FLOAT, DOUBLE, VARCHAR, VARBINARY, BOOLEAN, DECIMAL, TIME, DATE, TIMESTAMP, INTERVAL DAY TO SECOND, INTERVAL YEAR TO MONTH

Example: TIMESTAMP

---

precision Integer

Total number of digits in the number. Included only for the `DECIMAL` type.

Example: 38

---

scale Integer

Number of digits to the right of the decimal point. Included only for the `DECIMAL` type.

Example: 2

---

[subSchema](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-subschema-array) Array of Object

List of objects that represent the field's composition. For example, a field composed of data about a restaurant might have a subSchema with an object for parking options, another for payment methods, and so on. subSchemas may be nested within other subSchemas. subSchema is listed only for the `STRUCT`, `LIST`, and `UNION` types.

#### Attributes of Objects in the `subSchema` Array[​](#attributes-of-objects-in-the-subschema-array "Direct link to attributes-of-objects-in-the-subschema-array")

name String

Name for the subSchema object.

Example: cash

---

type Object

Object that contains a `name` attribute that provides the field's type.

Example: {"name": "BOOLEAN"}

## Creating a View[​](#creating-a-view "Direct link to Creating a View")

Create a view from a table in Dremio.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object. For views, the entityType is `dataset`.

---

type Body   String

Type of dataset. For views, the type is `VIRTUAL_DATASET`.

---

path Body   Array of String

Path of the location where you want to save the view within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by a name for the view itself as the last item in the array. The name of the view cannot include the following special characters: `/`, `:`, `[`, or `]`. Views can only be created in spaces.

Example: ["Business", "Transportation", "NYC-taxi-trips-short-distance"]

---

sql Body   String

SQL query to use to create the view.

Example: SELECT \* FROM "NYC-taxi-trips" WHERE trip\_distance\_mi <= 2.0 ORDER BY trip\_distance\_mi ASC

---

sqlContext Body   Array of String

Context for the SQL query to use to create the view.

Example: ["Samples", "samples.dremio.com"]

---

[accessControlList](/25.x/reference/api/catalog/view#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the view and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3", "permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8", "permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390", "permissions": ["SELECT","ALTER"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) [Body]   Array of Object   Optional

Enterprise only. List of users who should have access to the view and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the view and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the view.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the view. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "type": "VIRTUAL_DATASET",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a View by ID[​](#retrieving-a-view-by-id "Direct link to Retrieving a View by ID")

Retrieve a view by specifying the view's `id` value.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the view that you want to retrieve.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/ef99ab32-89ca-4d1c-9e91-2c8be861bb8a' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a View by Path[​](#retrieving-a-view-by-path "Direct link to Retrieving a View by Path")

Retrieve a view by specifying the view's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

View's location within Dremio, using forward slashes as separators. For example, for the "NYC-taxi-trips" view in the "samples.dremio.com" folder within the space "Transportation," the path is `Transportation/samples.dremio.com/NYC-taxi-trips`. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: Business/Transportation/NYC-taxi-trips-short-distance

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Business/Transportation/NYC-taxi-trips-short-distance' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a View[​](#updating-a-view "Direct link to Updating a View")

Update a view in Dremio.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the view that you want to update.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

---

entityType Body   String

Type of the catalog object. For views, the entityType is `dataset`.

---

type Body   String

Type of dataset. For views, type is `VIRTUAL_DATASET`.

---

path Body   Array of String

Path of the location where you want to save the updated view within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by the name for the view itself as the last item in the array. Views can only be saved in spaces.

Example: ["Business", "Transportation", "NYC-taxi-trips-short-distance"]

---

tag Body   String (UUID)   Optional

Unique identifier of the version of the view that you want to update. If you provide a tag in the request body, Dremio uses the tag to ensure that you are requesting to update the most recent version of the view. If you do not provide a tag, Dremio automatically updates the most recent version of the view.

Example: f90d1526-e64b-47b1-9ab0-d25df5247cab

---

sql Body   String

SQL query to use to update the view.

Example: SELECT \* FROM "NYC-taxi-trips" WHERE trip\_distance\_mi <= 2.0 ORDER BY trip\_distance\_mi DESC

---

sqlContext Body   Array of String

Context for the SQL query to use for the updated view.

Example: ["Samples", "samples.dremio.com"]

---

[accessControlList](/25.x/reference/api/catalog/view#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the view and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the view and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the view and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the view.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the view. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/ef99ab32-89ca-4d1c-9e91-2c8be861bb8a' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "type": "VIRTUAL_DATASET",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT trip_distance_mi, fare_amount, tip_amount FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi DESC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ]  
}'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-by-distance"  
  ],  
  "createdAt": "2023-01-20T15:26:39.780Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "7cab1a42-8835-4d31-827b-fedee1ad38d1",  
  "sql": "SELECT trip_distance_mi, fare_amount, tip_amount FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi DESC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Refreshing the Reflections on a View[​](#refreshing-the-reflections-on-a-view "Direct link to Refreshing the Reflections on a View")

Refresh the Reflections associated with the specified view.

Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections) to learn how refreshing works.

Method and URL

```
POST /api/v3/catalog/{id}/refresh
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier for the view you want to refresh.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

Example Request

```
curl -X POST 'https://api.dremio.cloud//api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72/refresh' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Deleting a View[​](#deleting-a-view "Direct link to Deleting a View")

Delete the specified view.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the view that you want to delete.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/ef99ab32-89ca-4d1c-9e91-2c8be861bb8a' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

User-Defined Function](/25.x/reference/api/catalog/user-defined-function)[Next

Lineage](/25.x/reference/api/catalog/lineage)

* [View Attributes](#view-attributes)
* [Creating a View](#creating-a-view)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a View by ID](#retrieving-a-view-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a View by Path](#retrieving-a-view-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a View](#updating-a-view)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Refreshing the Reflections on a View](#refreshing-the-reflections-on-a-view)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting a View](#deleting-a-view)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/lineage

Version: 25.x

On this page

# Lineage Enterprise

Use the Catalog API to retrieve lineage information about datasets (tables and views). The lineage object includes information about the dataset's sources, parent objects, and child objects.

Lineage Object

```
{  
  "sources": [  
    {  
      "id": "21077e5d-fe6f-4a29-843f-58fa3acb17c2",  
      "path": [  
        "Samples"  
      ],  
      "tag": "Iz1v71CeTQY=",  
      "type": "CONTAINER",  
      "containerType": "SOURCE",  
      "createdAt": "2022-02-14T21:57:48.794Z"  
    }  
  ],  
  "parents": [  
    {  
      "id": "3419fa3a-b5b3-4438-b864-a27ec4e18752",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zips.json"  
      ],  
      "tag": "MAntohVzwLw=",  
      "type": "DATASET",  
      "datasetType": "PROMOTED",  
      "createdAt": "2023-01-18T18:49:09.669Z"  
    }  
  ],  
  "children": [  
    {  
      "id": "170e211e-4235-4d8d-acb5-3d4dbfe99c75",  
      "path": [  
        "@dremio",  
        "NYC_zip"  
      ],  
      "tag": "OWKrfpEKzW4=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T02:11:46.344Z"  
    },  
    {  
      "id": "7f79c068-a3c3-4af7-8cd4-35896ef0a0e0",  
      "path": [  
        "@dremio",  
        "Chicago_zip"  
      ],  
      "tag": "gsaDW5h4GCs=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T00:09:12.461Z"  
    }  
  ]  
}
```

## Lineage Attributes[​](#lineage-attributes "Direct link to Lineage Attributes")

[sources](/25.x/reference/api/catalog/lineage#attributes-of-objects-in-the-sources-array) Array of Object

Information about the sources the dataset uses. Each object in the sources array represents one source.

Example: [{"id": "21077e5d-fe6f-4a29-843f-58fa3acb17c2","path": ["Samples"],"tag": "Iz1v71CeTQY=","type": "CONTAINER","containerType": "SOURCE","createdAt": "2023-02-14T21:57:48.794Z"}]

---

[parents](/25.x/reference/api/catalog/lineage#attributes-of-objects-in-the-parents-array) Array of Object

Information about the parent objects for the dataset. Each object in the parents array represents one parent object. If a view represents a join of two other datsets, the parents array includes the two joined datasets. The parents array is empty if the dataset does not have parent objects.

Example: [{"id": "3419fa3a-b5b3-4438-b864-a27ec4e18752","path": ["Samples","samples.dremio.com","zips.json"],"tag": "MAntohVzwLw=","type": "DATASET","datasetType": "PROMOTED","createdAt": "2023-01-18T18:49:09.669Z"}]

---

[children](/25.x/reference/api/catalog/lineage#attributes-of-objects-in-the-children-array) Array of Object

Information about other catalog objects that reference the dataset. Each object in the children array represents one child object. The children array is empty if the dataset does not have child objects.

Example: [{"id": "170e211e-4235-4d8d-acb5-3d4dbfe99c75","path": ["@dremio","NYC\_zip"],"tag": "OWKrfpEKzW4=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-01-25T02:11:46.344Z"},{"id": "7f79c068-a3c3-4af7-8cd4-35896ef0a0e0","path": ["@dremio","Chicago\_zip"],"tag": "gsaDW5h4GCs=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-01-25T00:09:12.461Z"}]

#### Attributes of Objects in the `sources` Array[​](#attributes-of-objects-in-the-sources-array "Direct link to attributes-of-objects-in-the-sources-array")

id String (UUID)

Unique identifier of the source associated with the dataset.

Example: 21077e5d-fe6f-4a29-843f-58fa3acb17c2

---

path Array of String

Path of the source within Dremio, expressed as an array.

Example: ["Samples"]

---

tag String

Unique identifier of the version of the source. Dremio changes the tag whenever the source changes.

Example: Iz1v71CeTQY=

---

type String

Type of source. For sources in lineage responses, the type is `CONTAINER`.

Example: CONTAINER

---

containerType String

Type of container for the source.

Enum: HOME, SOURCE

Example: SOURCE

---

createdAt String

Date and time that the source was created, in UTC format. Not included for sources with the containerType `HOME`.

Example: 2022-02-14T21:57:48.794Z

#### Attributes of Objects in the `parents` Array[​](#attributes-of-objects-in-the-parents-array "Direct link to attributes-of-objects-in-the-parents-array")

id String (UUID)

Unique identifier of the parent object.

Example: 3419fa3a-b5b3-4438-b864-a27ec4e18752

---

path Array of String

Path of the parent object within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the parent object itself as the last item in the array.

Example: ["Samples","samples.dremio.com","zips.json"]

---

tag String

Unique identifier of the version of the parent object. Dremio changes the tag whenever the parent object changes.

Example: MAntohVzwLw=

---

type String

Type of parent object. For parent objects in lineage responses, the type is `DATASET`.

Example: DATASET

---

datasetType String

Dataset type for the parent object. If the parent object is a table, `PROMOTED`. If the parent object is a view, `VIRTUAL`.

Enum: PROMOTED, VIRTUAL

Example: PROMOTED

---

createdAt String

Date and time that the parent object was created, in UTC format.

Example: 2023-01-18T18:49:09.669Z

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String (UUID)

Unique identifier of the child object.

Example: 170e211e-4235-4d8d-acb5-3d4dbfe99c75

---

path Array of String

Path of the child object within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the child object itself as the last item in the array.

Example: ["@dremio","NYC\_zip"]

---

tag String

Unique identifier of the version of the child object. Dremio changes the tag whenever the child object changes.

Example: OWKrfpEKzW4=

---

type String

Type of child object. For child objects in lineage responses, the type is `DATASET`.

Example: DATASET

---

datasetType String

Dataset type for the child object. For child objects in lineage responses, the datasetType is `VIRTUAL`.

Example: VIRTUAL

---

createdAt String

Date and time that the child object was created, in UTC format.

Example: 2023-01-25T02:11:46.344Z

## Retrieving Lineage Information About a Dataset[​](#retrieving-lineage-information-about-a-dataset "Direct link to Retrieving Lineage Information About a Dataset")

Retrieve lineage information about the specified dataset.

Method and URL

```
GET /api/v3/catalog/{id}/graph
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the dataset whose lineage you want to retrieve.

Example: d69b25a3-31c8-4d55-a7cc-dfee2290779b

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/d69b25a3-31c8-4d55-a7cc-dfee2290779b/graph' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "sources": [  
    {  
      "id": "21077e5d-fe6f-4a29-843f-58fa3acb17c2",  
      "path": [  
        "Samples"  
      ],  
      "tag": "Iz1v71CeTQY=",  
      "type": "CONTAINER",  
      "containerType": "SOURCE",  
      "createdAt": "2022-02-14T21:57:48.794Z"  
    }  
  ],  
  "parents": [  
    {  
      "id": "3419fa3a-b5b3-4438-b864-a27ec4e18752",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zips.json"  
      ],  
      "tag": "MAntohVzwLw=",  
      "type": "DATASET",  
      "datasetType": "PROMOTED",  
      "createdAt": "2023-01-18T18:49:09.669Z"  
    }  
  ],  
  "children": [  
    {  
      "id": "170e211e-4235-4d8d-acb5-3d4dbfe99c75",  
      "path": [  
        "@dremio",  
        "NYC_zip"  
      ],  
      "tag": "OWKrfpEKzW4=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T02:11:46.344Z"  
    },  
    {  
      "id": "7f79c068-a3c3-4af7-8cd4-35896ef0a0e0",  
      "path": [  
        "@dremio",  
        "Chicago_zip"  
      ],  
      "tag": "gsaDW5h4GCs=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T00:09:12.461Z"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

View](/25.x/reference/api/catalog/view)[Next

Tag](/25.x/reference/api/catalog/tag)

* [Lineage Attributes](#lineage-attributes)
* [Retrieving Lineage Information About a Dataset](#retrieving-lineage-information-about-a-dataset)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/tag

Version: 25.x

On this page

# Tag

Use the Catalog API to create, update, and retrieve [tags](/25.x/sonar/query-manage/managing-data/data-curation/#tags).

Tag Object

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023"  
  ],  
  "version": "VJ3ijXH4m6k="  
}
```

## Tag Attributes[​](#tag-attributes "Direct link to Tag Attributes")

tags Array of String

List of tags that apply to the dataset.

Example: ["NYC","taxi","2023"]

---

version String

Unique identifier of the set of tags. Dremio changes the version whenever any of the tags change and uses the version value to ensure that updates apply to the most recent version of the set of tags.

Example: VJ3ijXH4m6k=

## Creating Tags[​](#creating-tags "Direct link to Creating Tags")

Create one or more tags for the specified dataset.

Method and URL

```
POST /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset for which you want to add tags.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

tags Body   Array of String

List of tags to apply to the dataset. Tags are case-insensitive. Each tag can be listed only once for each dataset. Each tag can have a maximum of 128 characters. Tags cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: ["NYC","taxi","2023"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tags": ["NYC", "taxi", "2023"]  
}'
```

Example Response

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023"  
  ],  
  "version": "VM3ijXH4m6k="  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving Tags[​](#retrieving-tags "Direct link to Retrieving Tags")

Retrieve the tags applied to the specified dataset.

Method and URL

```
GET /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset whose tags you want to retrieve.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023"  
  ],  
  "version": "VM3ijXH4m6k="  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Updating Tags[​](#updating-tags "Direct link to Updating Tags")

Update the tags for the specified dataset.

Method and URL

```
POST /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset whose tags you want to update.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

tags Body   Array of String

List of tags to apply to the dataset. If you want to keep any of the existing tags, include them in the tags array. Tags are case-insensitive and must be distinct (in other words, list each tag only once for each dataset). Each tag may have a maximum of 128 characters. Tags cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: ["NYC","taxi","2023","archived"]

---

version Body   String

Unique identifier of the most recent set of tags. Dremio uses the version value to ensure that you are updating the most recent version of the tags.

Example: VM3ijXH4m6k=

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tags": ["NYC", "taxi", "2023", "archived"],  
  "version": "VM3ijXH4m6k="  
}'
```

Example Response

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023",  
    "archived"  
  ],  
  "version": "yiZSE++9wiU="  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting Tags[​](#deleting-tags "Direct link to Deleting Tags")

Delete the tags for the specified dataset.

note

Deleting tags means sending an empty array to replace the existing tags with no tags. The tag object will still exist, but it will contain an empty `tags` array and no tags will appear for the dataset in the Dremio UI.

Method and URL

```
POST /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset whose tags you want to remove.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

tags Body   Array of String

Empty array to represent deletion of all tags for the dataset.

Example: []

---

version Body   String

Unique identifier of the most recent set of tags. Dremio uses the version value to ensure that you are deleting tags from the most recent version.

Example: yiZSE++9wiU=

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tags": [],  
  "version": "yiZSE++9wiU="  
}'
```

Example Response

```
{  
  "tags": [],  
  "version": "wuTAKuRcVas="  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

Was this page helpful?

[Previous

Lineage](/25.x/reference/api/catalog/lineage)[Next

Wiki](/25.x/reference/api/catalog/wiki)

* [Tag Attributes](#tag-attributes)
* [Creating Tags](#creating-tags)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving Tags](#retrieving-tags)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Updating Tags](#updating-tags)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Deleting Tags](#deleting-tags)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/wiki

Version: 25.x

On this page

# Wiki

Use the Catalog API to create, update, and retrieve the [wiki](/25.x/sonar/query-manage/managing-data/data-curation/#wikis) for a source, space, or dataset.

Wiki Object

```
{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 4  
}
```

## Wiki Attributes[​](#wiki-attributes "Direct link to Wiki Attributes")

text String

Text displayed in the wiki, formatted with [GitHub-flavored Markdown](https://github.github.com/gfm/).

---

version Integer

Number for the most recent version of the wiki, starting with `0`. Dremio increments the value by 1 each time the wiki changes and uses the version value to ensure that updates apply to the most recent version of the wiki.

Example: 4

## Creating a Wiki[​](#creating-a-wiki "Direct link to Creating a Wiki")

Create a wiki for the specified source, space, or dataset.

Method and URL

```
POST /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset for which you want to add the wiki.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

text Body   String

Text to display in the wiki. Use [GitHub-flavored Markdown](https://github.github.com/gfm/) for wiki formatting and `\\n` for new lines and blank lines. Each wiki may have a maximum of 100,000 characters.

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."  
}'
```

Example Response

```
{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 0  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Wiki[​](#retrieving-a-wiki "Direct link to Retrieving a Wiki")

Retrieve the wiki for the specified source, space, or dataset.

Method and URL

```
GET /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset whose wiki you want to retrieve.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 0  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Wiki[​](#updating-a-wiki "Direct link to Updating a Wiki")

Update the wiki for the specified source, space, or dataset.

Method and URL

```
POST /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset whose wiki you want to update.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

text Body   String

Text to display in the wiki, formatted with [GitHub-flavored Markdown](https://github.github.com/gfm/).

---

version Body   Integer

Number listed as the version value for the most recent existing wiki. Dremio uses the version value to ensure that you are updating the most recent version of the wiki.

Example: 0

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "text": "# New Title Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is an update to the bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 0  
}'
```

Example Response

```
{  
  "text": "# New Title Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is an update to the bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 1  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting a Wiki[​](#deleting-a-wiki "Direct link to Deleting a Wiki")

Delete the wiki for the specified source, space, or dataset.

note

Deleting the wiki entails sending an empty string to replace the existing wiki with no wiki. The wiki object will still exist, but it will contain an empty `text` value and no wiki will appear for the source, space, or dataset in the Dremio UI.

Method and URL

```
POST /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset whose wiki you want to delete.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

text Body   String

Empty string to represent deletion of the wiki.

Example: ""

---

version Body   Integer

Number listed as the version value for the most recent existing wiki. Dremio uses the version value to ensure that you are deleting the most recent version of the wiki.

Example: 1

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "text": "",  
  "version": 1  
}'
```

Example Response

```
{  
  "text": "",  
  "version": 2  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

Was this page helpful?

[Previous

Tag](/25.x/reference/api/catalog/tag)[Next

Privileges](/25.x/reference/api/catalog/privileges)

* [Wiki Attributes](#wiki-attributes)
* [Creating a Wiki](#creating-a-wiki)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Wiki](#retrieving-a-wiki)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Updating a Wiki](#updating-a-wiki)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Deleting a Wiki](#deleting-a-wiki)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/privileges

Version: 25.x

On this page

# Privileges Enterprise

caution

The Catalog API Privileges endpoint is deprecated. We expect to remove it by July 2025.

In place of the Privileges endpoint, use the Catalog API [Grants](/25.x/reference/api/catalog/grants#retrieving-privileges-and-grantees-on-a-catalog-object) endpoint to retrieve privileges and grantees on specific catalog objects.

Use the Catalog API to retrieve information about available privileges on the different types of catalog objects.

Privileges Object

```
{  
  "availablePrivileges": [  
    {  
      "grantType": "SPACE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "ARP_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "EXTERNAL_QUERY",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER_IN_MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "PDS",  
      "privileges": [  
        "ALTER",  
        "DELETE",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE"  
      ]  
    },  
    {  
      "grantType": "VDS",  
      "privileges": [  
        "ALTER",  
        "MANAGE_GRANTS",  
        "SELECT"  
      ]  
    },  
    {  
      "grantType": "FUNCTION",  
      "privileges": [  
        "ALTER",  
        "EXECUTE",  
        "MANAGE_GRANTS",  
        "MODIFY"  
      ]  
    }  
  ]  
}
```

## Privileges Attributes[​](#privileges-attributes "Direct link to Privileges Attributes")

[availablePrivileges](/25.x/reference/api/catalog/privileges#attributes-of-objects-in-the-availableprivileges-array) Array of Object

Information about the grant types and privileges that are available to assign to users and roles for each type of object in the catalog. Each availablePrivileges object contains two attributes: grantType and privileges.

Example: [{"grantType": "SPACE","privileges": ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]},{"grantType": "SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]},{"grantType": "MUTABLE\_SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","CREATE\_TABLE","DELETE","DROP","INSERT","MANAGE\_GRANTS","MODIFY","SELECT","TRUNCATE","UPDATE","VIEW\_REFLECTION"]},{"grantType": "ARP\_SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","EXTERNAL\_QUERY","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]},{"grantType": "FOLDER\_IN\_MUTABLE\_SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","CREATE\_TABLE","DELETE","DROP","INSERT","MANAGE\_GRANTS","SELECT","TRUNCATE","UPDATE","VIEW\_REFLECTION"]},{"grantType": "FOLDER","privileges": ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","SELECT","VIEW\_REFLECTION"]},{"grantType": "PDS","privileges": ["ALTER","DELETE","INSERT","MANAGE\_GRANTS","SELECT","TRUNCATE","UPDATE"]},{"grantType": "VDS","privileges": ["ALTER","MANAGE\_GRANTS","SELECT"]},{"grantType": "FUNCTION","privileges": ["ALTER","EXECUTE","MANAGE\_GRANTS","MODIFY"]}]

#### Attributes of Objects in the `availablePrivileges` Array[​](#attributes-of-objects-in-the-availableprivileges-array "Direct link to attributes-of-objects-in-the-availableprivileges-array")

grantType String

Type of the catalog object on which the listed privileges are available. `ARP_SOURCE` refers to relational-database sources.

Enum: SPACE, SOURCE, MUTABLE\_SOURCE, ARP\_SOURCE, FOLDER\_IN\_MUTABLE\_SOURCE, FOLDER, PDS, VDS, FUNCTION

Example: SPACE

---

privileges Array of String

List of available privileges on the type of the catalog object specified in grantType. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]

## Retrieving All Catalog Privileges[​](#retrieving-all-catalog-privileges "Direct link to Retrieving All Catalog Privileges")

Retrieve information about the available privileges on each type of object in the catalog.

caution

This endpoint is deprecated. We expect to remove it by July 2025.

In place of this endpoint, use the Catalog API [Grants](/25.x/reference/api/catalog/grants#retrieving-privileges-and-grantees-on-a-catalog-object) endpoint to retrieve privileges and grantees on specific catalog objects.

Method and URL

```
GET /api/v3/catalog/privileges
```

### Parameters[​](#parameters "Direct link to Parameters")

type Query   String   Optional

Type of the catalog object whose available privileges you want to retrieve. For more information, read [type Query Parameter](/25.x/reference/api/#type-query-parameter).

Enum: SPACE, SOURCE, MUTABLE\_SOURCE, ARP\_SOURCE, FOLDER\_IN\_MUTABLE\_SOURCE, FOLDER, PDS, VDS, FUNCTION

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/privileges' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "availablePrivileges": [  
    {  
      "grantType": "SPACE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "ARP_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "EXTERNAL_QUERY",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER_IN_MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "PDS",  
      "privileges": [  
        "ALTER",  
        "DELETE",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE"  
      ]  
    },  
    {  
      "grantType": "VDS",  
      "privileges": [  
        "ALTER",  
        "MANAGE_GRANTS",  
        "SELECT"  
      ]  
    },  
    {  
      "grantType": "FUNCTION",  
      "privileges": [  
        "ALTER",  
        "EXECUTE",  
        "MANAGE_GRANTS",  
        "MODIFY"  
      ]  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Wiki](/25.x/reference/api/catalog/wiki)[Next

Grants](/25.x/reference/api/catalog/grants)

* [Privileges Attributes](#privileges-attributes)
* [Retrieving All Catalog Privileges](#retrieving-all-catalog-privileges)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/grants

Version: 25.x

On this page

# Grants Enterprise

Use the Catalog API to grant user and role privileges on specific catalog objects.

Grants Object

```
{  
  "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
  "availablePrivileges": [  
    "ALTER",  
    "DELETE",  
    "INSERT",  
    "MANAGE_GRANTS",  
    "SELECT",  
    "TRUNCATE",  
    "UPDATE"  
  ],  
  "grants": [  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT",  
        "MANAGE_GRANTS"  
      ],  
      "granteeType": "USER",  
      "id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0",  
      "name": "jeansmith",  
      "firstName": "Jean",  
      "lastName": "Smith",  
      "email": "jean_smith@example.com"  
    },  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT"  
      ],  
      "granteeType": "ROLE",  
      "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
      "name": "examplerole"  
    }  
  ]  
}
```

## Grants Attributes[​](#grants-attributes "Direct link to Grants Attributes")

id String

Unique identifier of the Dremio catalog object.

Example: 7f1c4660-cd7b-40d0-97d1-b8a6f431cbda

---

availablePrivileges Array of String

List of available privileges on the catalog object.

Example: ["ALTER","DELETE","INSERT","MANAGE\_GRANTS","SELECT","TRUNCATE","UPDATE"]

---

[grants](/25.x/reference/api/catalog/grants#attributes-of-objects-in-the-grants-array) Array of Object

Information about the privileges and grantees for the catalog object. If the grants array is empty, there are no explicit grants for the object.

note

An empty grants array does not mean no users have access to the object at all. For example, admin users implicitly have all privileges on all catalog objects, owners implicitly have all privileges on everything they own, and children objects inherit the grants for their parent objects.

Example: [{"privileges": ["ALTER","SELECT","MANAGE\_GRANTS"],"granteeType": "USER","id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0","name": "jeansmith","firstName": "Jean","lastName": "Smith","email": "[jean\_smith@example.com](mailto:jean_smith@example.com)"},{"privileges": ["ALTER","SELECT"],"granteeType": "ROLE","id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","name": "examplerole"}]

#### Attributes of Objects in the `grants` Array[​](#attributes-of-objects-in-the-grants-array "Direct link to attributes-of-objects-in-the-grants-array")

privileges String

List of privileges granted to the user or role. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["ALTER","SELECT","MANAGE\_GRANTS"]

---

granteeType String

Type of grantee.

Enum: USER, ROLE

Example: USER

---

id String

Unique identifier of the user or role.

Example: 27937a63-e7e5-4478-8d3c-4ad3f20d43c0

---

name String

Name of the user or role.

Example: jeansmith

---

firstName String

For users, the user's first name. Not included for roles.

Example: Jean

---

lastName String

For users, the user's last name. Not included for roles.

Example: Smith

---

email String

For users, the user's email address. Not included for roles.

Example: [jean\_smith@example.com](mailto:jean_smith@example.com)

## Creating or Updating Privilege Grants on a Catalog Object[​](#creating-or-updating-privilege-grants-on-a-catalog-object "Direct link to Creating or Updating Privilege Grants on a Catalog Object")

Create or update the privileges granted to users and roles on the specified catalog object.

note

You must have the [MANAGE GRANTS privilege](/25.x/security/rbac/privileges/#dataset-privileges) to create or update privilege grants on catalog objects.

Method and URL

```
PUT /api/v3/catalog/{id}/grants
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the Dremio catalog object.

Example: 7f1c4660-cd7b-40d0-97d1-b8a6f431cbda

---

[grants](/25.x/reference/api/catalog/grants#parameters-of-objects-in-the-grants-array) Body   Array of Object

Array of objects that specify which users and roles should have privileges on the catalog object, as well as each user's and role's specific privileges. May include objects for users, roles, or both.

Example: [{"privileges": ["ALTER","SELECT","MANAGE\_GRANTS"],"granteeType": "USER","id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0"},{"privileges": ["SELECT","ALTER"],"granteeType": "ROLE","id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889"}]

#### Parameters of Objects in the `grants` Array[​](#parameters-of-objects-in-the-grants-array "Direct link to parameters-of-objects-in-the-grants-array")

privileges Body   Array of String

List of privileges to grant to the user or role. Use the [Privileges](/25.x/reference/api/catalog/privileges#retrieving-all-catalog-privileges) endpoint to retrieve a list of available privileges on the catalog object type. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["ALTER","SELECT","MANAGE\_GRANTS"]

---

granteeType Body   String

Type of grantee.

Enum: USER, ROLE

Example: USER

---

id Body   String

Unique identifier of the user or role.

Example: 27937a63-e7e5-4478-8d3c-4ad3f20d43c0

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/7f1c4660-cd7b-40d0-97d1-b8a6f431cbda/grants' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "grants": [  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT",  
        "MANAGE_GRANTS"  
      ],  
      "granteeType": "USER",  
      "id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0"  
    },  
    {  
      "privileges": [  
        "SELECT",  
        "ALTER"  
      ],  
      "granteeType": "ROLE",  
      "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889"  
    }  
  ]  
}'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving Privileges and Grantees on a Catalog Object[​](#retrieving-privileges-and-grantees-on-a-catalog-object "Direct link to Retrieving Privileges and Grantees on a Catalog Object")

Retrieve information about the privileges granted to users and roles on the specified catalog object.

note

Use this endpoint in place of the Catalog API [Privileges](/25.x/reference/api/catalog/privileges) endpoint, which is deprecated. We expect to remove the Privileges endpoint by July 2025.

You must have the [MANAGE GRANTS privilege](/25.x/security/rbac/privileges/#dataset-privileges) to retrieve privilege grants on catalog objects.

Method and URL

```
GET /api/v3/catalog/{id}/grants
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the object whose privilege grants you want to retrieve.

Example: 7f1c4660-cd7b-40d0-97d1-b8a6f431cbda

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/7f1c4660-cd7b-40d0-97d1-b8a6f431cbda/grants' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
  "availablePrivileges": [  
    "ALTER",  
    "DELETE",  
    "INSERT",  
    "MANAGE_GRANTS",  
    "SELECT",  
    "TRUNCATE",  
    "UPDATE"  
  ],  
  "grants": [  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT",  
        "MANAGE_GRANTS"  
      ],  
      "granteeType": "USER",  
      "id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0",  
      "name": "jeansmith",  
      "firstName": "Jean",  
      "lastName": "Smith",  
      "email": "jean_smith@example.com"  
    },  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT"  
      ],  
      "granteeType": "ROLE",  
      "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
      "name": "examplerole"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Privileges](/25.x/reference/api/catalog/privileges)[Next

Dataset](/25.x/reference/api/datasets/)

* [Grants Attributes](#grants-attributes)
* [Creating or Updating Privilege Grants on a Catalog Object](#creating-or-updating-privilege-grants-on-a-catalog-object)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving Privileges and Grantees on a Catalog Object](#retrieving-privileges-and-grantees-on-a-catalog-object)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/container-space/

Version: 25.x

On this page

# Space

Use the Catalog API to retrieve information about [spaces](/25.x/sonar/query-manage/managing-data/spaces) and the child objects they contain, as well as to create, update, and delete spaces.

Space Object

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

## Space Attributes[​](#space-attributes "Direct link to Space Attributes")

entityType String

Type of the catalog object. For spaces, the entityType is `space`.

Example: space

---

id String (UUID)

Unique identifier of the space.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

name String

Name of the space.

Example: Example-Space

---

tag String

Unique identifier of the version of the space. Dremio changes the tag whenever the space changes and uses the tag to ensure that PUT requests apply to the most recent version of the space.

Example: zzOQfjY9lU0=

---

createdAt String

Date and time that the space was created, in UTC format.

Example: 2023-01-12T18:44:43.237Z

---

[children](/25.x/reference/api/catalog/container-space#attributes-of-objects-in-the-children-array) Array of Object

Information about each catalog object in the space.

Example: [{"id": "8da037a1-8e50-422b-9a2b-cafb03f57c71","path": ["Example-Space","testfolder"],"tag": "0McuCL4MzBU=","type": "CONTAINER","containerType": "FOLDER"},{"id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473","path": ["Example-Space","travel\_testing"],"tag": "i4mnlSmHqVM=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-01-30T17:54:25.547Z"},{"id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda","path": ["Example-Space","zips"],"tag": "ITlp8+qyIMQ=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-02-08T16:24:25.084Z"}]

---

[accessControlList](/25.x/reference/api/catalog/container-space#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the space and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if space-specific access control privileges are not set.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["MODIFY"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the space. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/container-space#attributes-of-the-owner-object) Object

Information about the space's owner.

Example: {"ownerId": "d01585a2-b267-4d56-9154-31762ab65a43","ownerType": "USER"}

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String (UUID)

Unique identifier of the catalog object.

Example: 8da037a1-8e50-422b-9a2b-cafb03f57c71

---

path Array of String

Path of the catalog object within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by the catalog object itself as the last item in the array.

Example: ["Example-Space","testfolder"]

---

tag String

Unique identifier of the version of the catalog object. Dremio changes the tag whenever the catalog object changes and uses the tag to ensure that PUT requests apply to the most recent version of the object.

Example: 0McuCL4MzBU=

---

type String

Type of the catalog object.

Enum: CONTAINER, DATASET, FILE

Example: CONTAINER

---

containerType String

For catalog entities with the type `CONTAINER`, the type of container.

Enum: FOLDER, FUNCTION

Example: FOLDER

---

datasetType String

For catalog objects in a space with the type `DATASET`, the datasetType is `VIRTUAL` (spaces cannot contain tables, only views).

Example: VIRTUAL

---

createdAt String

For catalog objects in a space with the type `DATASET`, date and time that the catalog object was created, in UTC format.

Example: 2023-01-30T17:54:25.547Z

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-space#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the space and the specific privileges each user has.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5", "permissions": ["MODIFY"]}]

---

[roles](/25.x/reference/api/catalog/container-space#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the space and the specific privileges each role has.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889", "permissions": ["MODIFY"]}]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the space's owner.

Example: d01585a2-b267-4d56-9154-31762ab65a43

---

ownerType String

Type of owner of the space.

Enum: USER, ROLE

Example: USER

##### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String (UUID)

Enterprise only. Unique identifier of the user or role with access to the space.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the space. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["MODIFY"]

## Creating a Space[​](#creating-a-space "Direct link to Creating a Space")

Create a new space.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object. For spaces, the entityType is `space`.

Example: space

---

name Body   String

Name of the space. The name cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: Example-Space

---

[accessControlList](/25.x/reference/api/catalog/container-space#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the space and the specific privileges each user or role should have. May include an array of users, an array of roles, or both. Omit if you do not want to configure space-specific access control privileges.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["MODIFY"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the space and the specific privileges each user should have.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["MODIFY"]}]

---

[roles](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the space and the specific privileges each role should have.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the space.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the space. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["MODIFY"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "space",  
  "name": "Example-Space",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Retrieving a Space by ID[​](#retrieving-a-space-by-id "Direct link to Retrieving a Space by ID")

Retrieve a space and information about its contents by specifying the space's ID.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the space that you want to retrieve.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the space has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Space by Path[​](#retrieving-a-space-by-path "Direct link to Retrieving a Space by Path")

Retrieve a space and information about its contents by specifying the space's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Path of the space that you want to retrieve. The path is the name of the space.

Example: Example-Space

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam1) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam1): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the space has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Example-Space' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Space[​](#updating-a-space "Direct link to Updating a Space")

Update the specified space.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the space that you want to update.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

entityType Body   String

Type of the catalog object. For spaces, the entityType is `space`.

Example: space

---

id Body   String (UUID)

Unique identifier of the space to update.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

---

name Body   String

Name of the space to update.

Example: Example-Space

---

tag Body   String

Unique identifier of the version of the space that you want to update. Dremio uses the tag to ensure that you are requesting to update the most recent version of the space.

Example: zzOQfjY9lU0=

---

[accessControlList](/25.x/reference/api/catalog/container-space#parameters-of-the-accesscontrollist-object-1) Body   String   Optional

Enterprise only. Object used to specify which users and roles should have access to the space and the specific privileges each user or role should have. If you omit the accessControlList object in a PUT request, Dremio removes all existing user and role access settings from the space. To keep existing user and role access settings while making other updates, duplicate the existing accessControlList array in the PUT request.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALL"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["MODIFY"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the space and the specific privileges each user should have. If you omit the users object in a PUT request, Dremio removes all existing user access settings from the space. To keep existing user access settings while making other updates, duplicate the existing users array in the PUT request.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5", "permissions": ["ALL"]}]

---

[roles](/25.x/reference/api/catalog/container-space#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the space and the specific privileges each role should have. If you omit the roles object in a PUT request, Dremio removes all existing role access settings from the space. To keep existing role access settings while making other updates, duplicate the existing roles array in the PUT request.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889", "permissions": ["MODIFY"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the space.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the space. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALL, VIEW\_REFLECTION, TRUNCATE, UPDATE, DELETE, DROP, MANAGE\_GRANTS, EXTERNAL\_QUERY, EXECUTE, ALTER, INSERT, MODIFY, SELECT, CREATE\_SOURCE, WRITE, CREATE\_TABLE, ALTER\_REFLECTION, READ

Example: ["ALL"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "zzOQfjY9lU0=",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALL"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "space",  
  "id": "5442c00a-ada1-48c6-82fc-bb804b2e04e0",  
  "name": "Example-Space",  
  "tag": "PwZ6e/axHUY=",  
  "createdAt": "2023-01-12T18:44:43.237Z",  
  "children": [  
    {  
      "id": "8da037a1-8e50-422b-9a2b-cafb03f57c71",  
      "path": [  
        "Example-Space",  
        "testfolder"  
      ],  
      "tag": "0McuCL4MzBU=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "f32dfe85-32e2-4c31-b2b4-bfd62ab3f473",  
      "path": [  
        "Example-Space",  
        "travel_testing"  
      ],  
      "tag": "i4mnlSmHqVM=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-30T17:54:25.547Z"  
    },  
    {  
      "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
      "path": [  
        "Example-Space",  
        "zips"  
      ],  
      "tag": "ITlp8+qyIMQ=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-08T16:24:25.084Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER_REFLECTION",  
          "MODIFY",  
          "ALTER",  
          "MANAGE_GRANTS",  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "MODIFY"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting a Space[​](#deleting-a-space "Direct link to Deleting a Space")

Delete the specified space, including all of the space's contents.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the space that you want to delete.

Example: 5442c00a-ada1-48c6-82fc-bb804b2e04e0

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Home](/25.x/reference/api/catalog/container-home)[Next

Folder](/25.x/reference/api/catalog/container-folder)

* [Space Attributes](#space-attributes)
* [Creating a Space](#creating-a-space)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Space by ID](#retrieving-a-space-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Space by Path](#retrieving-a-space-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Space](#updating-a-space)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a Space](#deleting-a-space)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/container-folder/

Version: 25.x

On this page

# Folder

Use the Catalog API to retrieve information about [folders](/25.x/sonar/query-manage/managing-data/spaces/#folders) and the child objects they contain, as well as to create, update, and delete folders.

Folder Object

```
{  
  "entityType": "folder",  
  "id": "d4c2a8ba-a972-4db4-8deb-67e1ade684d1",  
  "path": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "tag": "pRmJ0BQ9SFw=",  
  "children": [  
    {  
      "id": "dremio:/Samples/samples.dremio.com/zip_lookup.csv",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zip_lookup.csv"  
      ],  
      "type": "FILE"  
    },  
    {  
      "id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips-iceberg"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "type": "DATASET",  
      "datasetType": "PROMOTED"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

## Folder Attributes[​](#folder-attributes "Direct link to Folder Attributes")

entityType String

Type of the catalog object. For folders, the entityType is `folder`.

Example: folder

---

id String

Unique identifier of the folder. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: d4c2a8ba-a972-4db4-8deb-67e1ade684d1

---

path Array of String

Path of the folder within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the target folder itself as the last item in the array.

Example: ["Samples","samples.dremio.com"]

---

tag String

Unique identifier of the version of the folder. Dremio changes the tag whenever the folder changes and uses the tag to ensure that PUT requests apply to the most recent version of the folder.

Example: pRmJ0BQ9SFw=

---

[children](/25.x/reference/api/catalog/container-folder#attributes-of-objects-in-the-children-array) Array of Object

Information about each catalog object in the folder.

Example: [{"id": "dremio:/Samples/samples.dremio.com/zip\_lookup.csv","path": ["Samples","samples.dremio.com","zip\_lookup.csv"],"type": "FILE"},{"id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg","path": ["Samples","samples.dremio.com","NYC-taxi-trips-iceberg"],"type": "CONTAINER","containerType": "FOLDER"},{"id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d","path": ["Samples","samples.dremio.com","NYC-taxi-trips"],"type": "DATASET","datasetType": "PROMOTED"}]

---

[accessControlList](/25.x/reference/api/catalog/container-folder#attributes-of-the-accesscontrollist-object) Object

Enterprise-only. Information about users and roles with access to the folder and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if folder-specific access control privileges are not set.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the folder. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/container-folder#attributes-of-the-owner-object) Object

Information about the folder's owner.

Example: {"ownerId": "d01585a2-b267-4d56-9154-31762ab65a43","ownerType": "USER"}

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String

Unique identifier of the catalog object. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: dremio:/Samples/samples.dremio.com/zip\_lookup.csv

---

path Array of String

Path of the catalog object within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the catalog object itself as the last item in the array.

Example: ["Samples","samples.dremio.com","zip\_lookup.csv"]

---

type String

Type of the catalog object. If the object is saved within a space (including the home space), valid types are `CONTAINER` and `DATASET`. If the object is saved within a source, valid types are `CONTAINER`, `FILE`, and `DATASET`.

Example: CONTAINER

---

containerType String

For catalog objects with the type `CONTAINER`, the containerType is `FOLDER`.

Example: FOLDER

---

datasetType String

For catalog objects with the type `DATASET`, the type of dataset. For tables, the datasetType is `PROMOTED`. For views, the datasetType is `VIRTUAL`.

Enum: PROMOTED, VIRTUAL

Example: VIRTUAL

---

createdAt String

Date and time that the catalog object was created, in UTC format. The createdAt attribute is included only for `DATASET` catalog objects that are saved in folders within spaces, not within sources.

Example: 2023-01-30T17:54:25.547Z

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-folder#attributes-of-objects-in-the-users-and-roles-arrays) String

Enterprise-only. List of users with access to the folder and the specific privileges each user has.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}]

---

[roles](/25.x/reference/api/catalog/container-folder#attributes-of-objects-in-the-users-and-roles-arrays) String

Enterprise-only. List of roles whose members have access to the folder and the specific privileges each role has.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the folder's owner.

Example: d01585a2-b267-4d56-9154-31762ab65a43

---

ownerType String

Type of owner of the folder.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String (UUID)

Enterprise-only. Unique identifier of the user or role with access to the folder.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Array of String

Enterprise-only. List of privileges the user or role has on the folder. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT","ALTER"]

## Creating a Folder[​](#creating-a-folder "Direct link to Creating a Folder")

Create a new folder within a space.

note

The Catalog API cannot create new folders within sources.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object. For folders, the entityType is `folder`.

Example: folder

---

path Body   Array of String

Path of the location where the folder should be created within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by a name for the target folder itself as the last item in the array. The name of the folder cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: ["Example-Space","First-Folder","New-Folder"]

---

[accessControlList](/25.x/reference/api/catalog/container-folder#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise-only. Object used to specify which users and roles should have access to the folder and the specific privileges each user or role should have. May include an array of users, an array of roles, or both. Omit if you do not want to configure folder-specific access control privileges.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays) Body   String   Optional

Enterprise-only. List of users who should have access to the folder and the specific privileges each user should have.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["SELECT","ALTER"]}]

---

[roles](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays) Body   String   Optional

Enterprise-only. List of roles whose members should have access to the folder and the specific privileges each role should have.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String (UUID)   Optional

Enterprise-only. Unique identifier of the user or role who should have access to the folder.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise-only. List of privileges the user or role should have on the folder. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALTER\_REFLECTION, SELECT, ALTER, VIEW\_REFLECTION, MANAGE\_GRANTS, ALL

Example: ["SELECT","ALTER"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "folder",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "598697c2-8be0-4050-9731-53563977a17d",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "tag": "R7COubQq8KE=",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "permissions": [],  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Retrieving a Folder by ID[​](#retrieving-a-folder-by-id "Direct link to Retrieving a Folder by ID")

Retrieve a folder and information about its contents by specifying the folder's ID.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String

Unique identifier of the folder that you want to retrieve. If the ID is a text path, use URL encoding to replace any special characters with their UTF-8-equivalent characters, such as `%3A` for a colon; `%2F` for a forward slash; and `%20` for a space. For example, if the ID value is `dremio:/Samples/samples.dremio.com/Dremio University`, the URI-encoded ID is `dremio%3A%2FSamples%2Fsamples.dremio.com%2FDremio%20University`.

Example: d4c2a8ba-a972-4db4-8deb-67e1ade684d1

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

**NOTE:** The maxChildren query parameter is not supported for folders in filesystem sources.

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the folder has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

**NOTE:** Dremio ignores the pageToken query parameter for folders in filesystem sources.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/d4c2a8ba-a972-4db4-8deb-67e1ade684d1' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "d4c2a8ba-a972-4db4-8deb-67e1ade684d1",  
  "path": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "tag": "pRmJ0BQ9SFw=",  
  "children": [  
    {  
      "id": "dremio:/Samples/samples.dremio.com/zip_lookup.csv",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zip_lookup.csv"  
      ],  
      "type": "FILE"  
    },  
    {  
      "id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips-iceberg"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "type": "DATASET",  
      "datasetType": "PROMOTED"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Folder by Path[​](#retrieving-a-folder-by-path "Direct link to Retrieving a Folder by Path")

Retrieve a folder and information about its contents by specifying the folder's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Path of the folder that you want to retrieve, with a forward slash to separate each level of nesting. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: Samples/samples.dremio.com

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

---

exclude Query   String   Optional

Exclude a default attribute from the response. The available value for the exclude query parameter is `children`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?exclude=children

---



maxChildren Query   Integer   Optional

Specify the maximum number of child objects to include in each page of results. Use in concert with the [pageToken query parameter](#pagetokenqueryparam1) to split large sets of results into multiple pages. For more information, read [maxChildren Query Parameter](/25.x/reference/api/#maxchildren-query-parameter).

**NOTE:** The maxChildren query parameter is not supported for filesystem sources.

Example: ?maxChildren=25

---



pageToken Query   String   Optional

Specify the token for retrieving the next page of results. Must be used in concert with the [maxChildren query parameter](#maxchildrenqueryparam1): the first request URL includes maxChildren set to the maximum number of child objects to include in each page of results. If the folder has more child objects than the specified maxChildren value, the response includes a nextPageToken attribute. Add the pageToken query parameter with the nextPageToken value to the request URL to retrieve the next page of results. Do not remove or change the maxChildren query parameter when you add pageToken to the request URL. Read [pageToken Query Parameter: User-Specified Maximum](/25.x/reference/api/#user-specified-maximum) for more information.

**NOTE:** Dremio ignores the pageToken query parameter for folders in filesystem sources.

Example: ?pageToken=cHAAFLceQCKsTVpwaEVisqgjDntZJUCuTqVNghPdkyBDUNoJvwrEXAMPLE

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Samples/samples.dremio.com' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "d4c2a8ba-a972-4db4-8deb-67e1ade684d1",  
  "path": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "tag": "pRmJ0BQ9SFw=",  
  "children": [  
    {  
      "id": "dremio:/Samples/samples.dremio.com/zip_lookup.csv",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zip_lookup.csv"  
      ],  
      "type": "FILE"  
    },  
    {  
      "id": "dremio:/Samples/samples.dremio.com/NYC-taxi-trips-iceberg",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips-iceberg"  
      ],  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "1acab7b3-ee82-44c1-abcc-e86d56078d4d",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "type": "DATASET",  
      "datasetType": "PROMOTED"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Folder[​](#updating-a-folder "Direct link to Updating a Folder")

Update the specified folder.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String

Unique identifier of the folder to update. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: 598697c2-8be0-4050-9731-53563977a17d

---

entityType Body   String

Type of the catalog object. For folders, the entityType is `folder`.

Example: folder

---

id Body   String

Unique identifier of the folder to update. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: 598697c2-8be0-4050-9731-53563977a17d

---

path Body   Array of String

Path of the location where the folder is saved within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by the target folder itself as the last item in the array.

Example: ["Example-Space","First-Folder","New-Folder"]

---

tag Body   String

Unique identifier of the version of the folder that you want to update. Dremio uses the tag to ensure that you are requesting to update the most recent version of the folder.

Example: R7COubQq8KE=

---

[accessControlList](/25.x/reference/api/catalog/container-folder#parameters-of-the-accesscontrollist-object-1) Body   Object   Optional

Enterprise-only. Object used to specify which users and roles should have access to the folder and the specific privileges each user or role should have. If you omit the accessControlList object in a PUT request, Dremio removes all existing user and role access settings from the folder. To keep existing user and role access settings while making other updates, duplicate the existing accessControlList array in the PUT request.

Example: {"users": [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALL"]}],"roles": [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   String   Optional

Enterprise-only. List of users who should have access to the folder and the specific privileges each user should have. If you omit the users object in a PUT request, Dremio removes all existing user access settings from the folder. To keep existing user access settings while making other updates, duplicate the existing users array in the PUT request.

Example: [{"id": "737a038f-c6cd-4fd3-a77a-59f692727ba5","permissions": ["ALL"]}]

---

[roles](/25.x/reference/api/catalog/container-folder#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   String   Optional

Enterprise-only. List of roles whose members should have access to the folder and the specific privileges each role should have. If you omit the roles object in a PUT request, Dremio removes all existing role access settings from the folder. To keep existing role access settings while making other updates, duplicate the existing roles array in the PUT request.

Example: [{"id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","permissions": ["SELECT"]}]

#### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String (UUID)   Optional

Enterprise-only. Unique identifier of the user or role who should have access to the folder.

Example: 737a038f-c6cd-4fd3-a77a-59f692727ba5

---

permissions Body   Array of String   Optional

Enterprise-only. List of privileges the user or role should have on the folder. For more information, read [Privileges](/25.x/security/rbac/privileges).

Enum: ALTER\_REFLECTION, SELECT, ALTER, VIEW\_REFLECTION, MANAGE\_GRANTS, ALL

Example: ["ALL"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/5442c00a-ada1-48c6-82fc-bb804b2e04e0' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "folder",  
  "id": "598697c2-8be0-4050-9731-53563977a17d",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "tag": "R7COubQq8KE=",  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALL"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "folder",  
  "id": "598697c2-8be0-4050-9731-53563977a17d",  
  "path": [  
    "Example-Space",  
    "First-Folder",  
    "New-Folder"  
  ],  
  "tag": "vnRnYLLpCFU=",  
  "children": [  
    {  
      "id": "d60f9258-e55a-4fc3-97b3-58c6720a70fc",  
      "path": [  
        "Example-Space",  
        "First-Folder",  
        "New-Folder",  
        "NYC-trips-weather"  
      ],  
      "tag": "IHXU7Oxs80c=",  
      "type": "CONTAINER",  
      "containerType": "FOLDER"  
    },  
    {  
      "id": "acba8595-bfcf-4126-887c-d2a19b5afb1d",  
      "path": [  
        "Example-Space",  
        "First-Folder",  
        "New-Folder",  
        "short-distance-trips"  
      ],  
      "tag": "KYs/Qyw1ok8=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-02-09T19:09:58.789Z"  
    }  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "737a038f-c6cd-4fd3-a77a-59f692727ba5",  
        "permissions": [  
          "ALTER_REFLECTION",  
          "ALTER",  
          "MANAGE_GRANTS",  
          "VIEW_REFLECTION",  
          "SELECT"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
        "permissions": [  
          "SELECT"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "d01585a2-b267-4d56-9154-31762ab65a43",  
    "ownerType": "USER"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting a Folder[​](#deleting-a-folder "Direct link to Deleting a Folder")

Delete the specified folder, including all of the folder's contents.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String

Unique identifier of the folder that you want to delete. The ID can be a UUID like `1acab7b3-ee82-44c1-abcc-e86d56078d4d` or a text path like `dremio:/Samples/samples.dremio.com/zip_lookup.csv`.

Example: 598697c2-8be0-4050-9731-53563977a17d

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/598697c2-8be0-4050-9731-53563977a17d' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Space](/25.x/reference/api/catalog/container-space)[Next

File](/25.x/reference/api/catalog/file)

* [Folder Attributes](#folder-attributes)
* [Creating a Folder](#creating-a-folder)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Folder by ID](#retrieving-a-folder-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Folder by Path](#retrieving-a-folder-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Folder](#updating-a-folder)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Deleting a Folder](#deleting-a-folder)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/file/

Version: 25.x

On this page

# File

Use the Catalog API to retrieve information about [formatting data to a table](/25.x/sonar/data-sources/entity-promotion).

File Object

```
{  
  "entityType": "file",  
  "id": "dremio:/Samples/samples.dremio.com/SF weather 2018-2019.csv",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "SF weather 2018-2019.csv"  
  ]  
}
```

## File Attributes[​](#file-attributes "Direct link to File Attributes")

entityType String

Type of the catalog object. For files, the entityType is `file`.

Example: file

---

id String

Unique identifier of the file. For files, the ID is the text path of the file within Dremio.

Example: dremio:/Samples/samples.dremio.com/SF weather 2018-2019.csv

---

path Array of String

Path of the file within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the target file itself as the last item in the array.

Example: ["Samples","samples.dremio.com","SF weather 2018-2019.csv"]

## Retrieving a File by Path[​](#retrieving-a-file-by-path "Direct link to Retrieving a File by Path")

Retrieve information about a file by specifying its path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters "Direct link to Parameters")

path Path   String

Path of the file that you want to retrieve, with a forward slash to separate each level of nesting. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, replace colons with `%3A` and replace spaces with `%20`.

Example: Samples/samples.dremio.com/SF%20weather%202018-2019.csv

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Samples/samples.dremio.com/SF%20weather%2018-2019.csv' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "file",  
  "id": "dremio:/Samples/samples.dremio.com/SF weather 2018-2019.csv",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "SF weather 2018-2019.csv"  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

405   Method Not Allowed

500   Internal Server Error

Was this page helpful?

[Previous

Folder](/25.x/reference/api/catalog/container-folder)[Next

Table](/25.x/reference/api/catalog/table)

* [File Attributes](#file-attributes)
* [Retrieving a File by Path](#retrieving-a-file-by-path)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/table/

Version: 25.x

On this page

# Table

Use the Catalog API to retrieve [tables](/25.x/sonar/query-manage/managing-data/datasets/), format files and folders as tables, update and refresh tables, and revert tables to files and folders.

Table Object

```
{  
  "entityType": "dataset",  
  "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
  "type": "PHYSICAL_DATASET",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "Dremio University",  
    "restaurant_reviews.parquet"  
  ],  
  "createdAt": "2024-01-13T19:52:01.894Z",  
  "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
  "accelerationRefreshPolicy": {  
    "activePolicyType": "SCHEDULE",  
    "refreshPeriodMs": 3600000,  
    "gracePeriodMs": 10800000,  
    "refreshSchedule": "0 0 8 * * ?",  
    "method": "FULL",  
    "neverExpire": false,  
    "neverRefresh": false,  
    "sourceRefreshOnDataChanges": false  
  },  
  "isMetadataExpired": false,  
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "format": {  
    "type": "Parquet",  
    "name": "restaurant_reviews.parquet",  
    "fullPath": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "ctime": 0,  
    "isFolder": false,  
    "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
    "ignoreOtherFileFormats": false,  
    "autoCorrectCorruptDates": true  
  },  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "_id",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "name",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "city",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "state",  
      "type": {  
        "name": "VARCHAR"  
      }  
    },  
    {  
      "name": "categories",  
      "type": {  
        "name": "LIST",  
        "subSchema": [  
          {  
            "type": {  
              "name": "VARCHAR"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "review_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "stars",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "attributes",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "Parking",  
            "type": {  
              "name": "STRUCT",  
              "subSchema": [  
                {  
                  "name": "garage",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                },  
                {  
                  "name": "street",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                },  
                {  
                  "name": "lot",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                },  
                {  
                  "name": "valet",  
                  "type": {  
                    "name": "BOOLEAN"  
                  }  
                }  
              ]  
            }  
          },  
          {  
            "name": "Accepts Credit Cards",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "Wheelchair Accessible",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "Price Range",  
            "type": {  
              "name": "BIGINT"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "date",  
      "type": {  
        "name": "VARCHAR"  
      }  
    }  
  ],  
  "approximateStatisticsAllowed": false  
}
```

## Table Attributes[​](#table-attributes "Direct link to Table Attributes")

entityType String

Type of the catalog object. For tables, the entityType is `dataset`.

Example: dataset

---

id String (UUID)

Unique identifier of the table.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

type String

Type of dataset. For tables, the type is `PHYSICAL_DATASET`.

Example: PHYSICAL\_DATASET

---

path Array of String

Path of the table within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the table itself as the last item in the array.

Example: ["Samples","samples.dremio.com","Dremio University","restaurant\_reviews.parquet"]

---

createdAt String

Date and time that the table was created, in UTC format.

Example: 2024-01-13T19:52:01.894Z

---

tag String (UUID)

Unique identifier of the version of the table. Dremio changes the tag whenever the table changes and uses the tag to ensure that PUT requests apply to the most recent version of the table.

Example: cb2905bb-39c0-497f-ae74-4c310d534f25

---

[accelerationRefreshPolicy](/25.x/reference/api/catalog/table#attributes-of-the-accelerationrefreshpolicy-object) String

Attributes that define the acceleration refresh policy for the table.

---

isMetadataExpired Boolean

* If true, the metadata of the table needs to be refreshed. To refresh it, run the ALTER TABLE command, using the clause REFRESH METADATA.
* If false, the metadata can still be used for planning queries against the table.
* If NULL, metadata has never yet been collected for the table.

---

lastMetadataRefreshAt String

Date and time that the table metadata was last refreshed. In UTC format. If NULL, the metadata has never yet been refreshed.

Example: 2024-01-31T09:50:01.012Z

---

[format](/25.x/reference/api/catalog/table#attributes-of-the-format-object) Object

Table format attributes.

---

[accessControlList](/25.x/reference/api/catalog/table#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the table and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if table-specific access control privileges are not set.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the table. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/table#attributes-of-the-owner-object) String

Information about the table's owner.

---

[fields](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-fields-array) Object

Attributes that represent the table schema.

approximateStatisticsAllowed Boolean

If true, `COUNT DISTINCT` queries run on the table return approximate results. Otherwise, false.

Example: {"ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8","ownerType": "USER"}

#### Attributes of the `accelerationRefreshPolicy` Object[​](#attributes-of-the-accelerationrefreshpolicy-object "Direct link to attributes-of-the-accelerationrefreshpolicy-object")

activePolicyType String

Option to set the policy for refreshing Reflections that are defined on the source. For this option to take effect, `neverRefresh` must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: Default. The Reflections are refreshed at the end of every period that is defined by refreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by refreshSchedule.
* `REFRESH_ON_DATA_CHANGES`: Reflections automatically refresh for underlying tables that are in Iceberg format when new snapshots are created after an update. If the Reflection refresh job finds no changes, then no data is updated. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency.

---

refreshPeriodMs Integer

Refresh period for the data in all Reflections for the table, in milliseconds.

Example: 3600000

---

refreshSchedule String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source are refreshed.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:

* `0 0 0 * * ?` : Refreshes every day at midnight.
* `0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
* `0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

gracePeriodMs Integer

Maximum age allowed for Reflection data used to accelerate queries, in milliseconds.

Example: 10800000

---

method String

Approach used for refreshing the data in Reflections defined on tables that are not in the Apache Iceberg format. For more information, read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections).

Enum: FULL, INCREMENTAL

Example: FULL

---

refreshField String

For the `INCREMENTAL` refresh method, the field to refresh for the table. Used only if method is `INCREMENTAL`. This parameter applies only to tables that are not in the Apache Iceberg format.

Example: business\_id

---

neverExpire Boolean

If the Reflection never expires, the value is `true`. Otherwise, the value is `false`.

Example: false

---

neverRefresh Boolean

If the Reflection never refreshes, the value is `true`. Otherwise, the value is `false`.

Example: false

---

sourceRefreshOnDataChanges Boolean

If the table's source is configured so that Reflections on tables in Iceberg format in the source will refresh when new snapshots are created after an update, `true`. Otherwise, `false`.

#### Attributes of the `format` Object[​](#attributes-of-the-format-object "Direct link to attributes-of-the-format-object")

type String

Type of data in the table.

Enum: Delta, Excel, Iceberg, JSON, Parquet, Text, Unknown, XLS

Example: Parquet

---

name String

Table name. Dremio automatically duplicates the name of the origin file or folder to populate this value. The name of the origin file or folder cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: restaurant\_reviews.parquet

---

fullPath Array of String

Path of the table within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the table itself as the last item in the array.

Example: ["Samples", "samples.dremio.com", "Dremio University", "restaurant\_reviews.parquet"]

---

ctime Integer

Not used. Has the value `0`.

Example: 0

---

isFolder Boolean

If the value is `true`, the table was created from a folder. If the value is `false`, the table was created from a file.

Example: false

---

location String

Location, expressed as a string, where the table's metadata is stored within a Dremio source or space.

Example: /samples.dremio.com/Dremio University/restaurant\_reviews.parquet

---

ignoreOtherFileFormats Boolean

If true, Dremio ignores all non-Parquet files in the related folder structure, and the promoted table works as if only Parquet files are in the folder structure. Otherwise, false. Included only for Parquet folders.

Example: false

---

metaStoreType String

Not used. Has the value `HDFS`.

Example: HDFS

---

[parquetDataFormat](/25.x/reference/api/catalog/table#attributes-of-the-parquetdataformat-object) Object

Information about data format for Parquet tables.

---

dataFormatTypeList Array of String

List of data format types in the table. Included only for Iceberg tables, and `PARQUET` is the only valid value.

Example: ["PARQUET"]

---

sheetName String

For tables created from files that contain multiple sheets, the name of the sheet used to create the table.

Example: location\_1

---

extractHeader Boolean

For tables created from files, the value is `true` if Dremio extracted the table's column names from the first line of the file. Otherwise, the value is `false`.

Example: false

---

hasMergedCells Boolean

For tables created from files, the value is `true` if Dremio expanded merged cells in the file when creating the table. Otherwise, the value is `false`.

Example: true

---

fieldDelimiter String

Character used to indicate separate fields in the table. May be `,` for a comma (default), `\t` for a tab, `|` for a pipe, or a custom character.

---

quote String

Character used for quotation marks in the table. May be `\"` for a double quote (default), `'` for a single quote, or a custom character.

---

comment String

Character used to indicate comments in the table. May be `#` for a number sign (default) or a custom character.

---

escape String

Character used to indicate an escape in the table. May be `\"` for a double quote (default), `` ` `` for a back quote, `\\` for a backward slash, or a custom character.

---

lineDelimiter String

Character used to indicate separate lines in the table. May be `\r\n` for a carriage return and a new line (default), `\n` for a new line, or a custom character.

---

skipFirstLine Boolean

If Dremio skipped the first line in the file or folder when creating the table, the value is `true`. Otherwise, the value is `false`.

Example: false

---

autoGenerateColumnNames Boolean

If Dremio used the existing columnn names in the file or folder for the table columns, the value is `true`. Otherwise, the value is `false`.

Example: true

---

trimHeader Boolean

If Dremio trimmed column names to a specific number of characters when creating the table, the value is `true`. Otherwise, the value is `false`.

Example: true

---

autoCorrectCorruptDates Boolean

If Dremio automatically corrects corrupted date fields in the table, the value is `true`. Otherwise, the value is `false`.

Example: true

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the table and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT", "ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT", "ALTER", "MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the table and the specific privileges each role has.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT", "ALTER"]}]

##### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String

Enterprise only. Unique identifier of the user or role with access to the table.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the table. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the table's owner.

Example: 30fca499-4abc-4469-7142-fc8dd29acac8

---

ownerType String

Type of owner of the table.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `fields` Array[​](#attributes-of-objects-in-the-fields-array "Direct link to attributes-of-objects-in-the-fields-array")

name String

Name of the table field.

Example: review\_count

---

[type](/25.x/reference/api/catalog/table#attributes-of-the-type-object) Object

Information about the table field.

##### Attributes of the `type` Object[​](#attributes-of-the-type-object "Direct link to attributes-of-the-type-object")

name String

Name of the table field's type.

Enum: STRUCT, LIST, UNION, INTEGER, BIGINT, FLOAT, DOUBLE, VARCHAR, VARBINARY, BOOLEAN, DECIMAL, TIME, DATE, TIMESTAMP, INTERVAL DAY TO SECOND, INTERVAL YEAR TO MONTH

Example: BIGINT

---

precision Integer

Total number of digits in the number. Included only for the `DECIMAL` type.

Example: 38

---

scale Integer

Number of digits to the right of the decimal point. Included only for the `DECIMAL` type.

Example: 0

---

[subSchema](/25.x/reference/api/catalog/table#attributes-of-objects-in-the-subschema-array) Array of Object

List of objects that represent the field's composition. For example, a field composed of data about a restaurant might have a subSchema with an object for parking options, another for payment methods, and so on. subSchemas may be nested within other subSchemas. subSchema appears only for the `STRUCT`, `LIST`, and `UNION` types.

##### Attributes of Objects in the `subSchema` Array[​](#attributes-of-objects-in-the-subschema-array "Direct link to attributes-of-objects-in-the-subschema-array")

name String

Name for the subSchema object.

Example: Parking

---

type Object

Object that contains a `name` attribute that provides the field's type.

Example: {"name": "BOOLEAN"}

#### Attributes of the `parquetDataFormat` Object[​](#attributes-of-the-parquetdataformat-object "Direct link to attributes-of-the-parquetdataformat-object")

type String

Type of data in the table. Within the parquetDataFormat object, the only valid type is `Parquet`.

Example: Parquet

---

ctime Integer

Not used. Has the value `0`.

Example: 0

---

isFolder Boolean

If the value is `true`, the table was created from a folder. If the value is `false`, the table was created from a file.

Example: true

---

autoCorrectCorruptDates Boolean

If the value is `true`, Dremio automatically corrects corrupted date fields in the table. Otherwise, the value is `false`.

Example: true

## Formatting a File or Folder as a Table[​](#formatting-a-file-or-folder-as-a-table "Direct link to Formatting a File or Folder as a Table")

Format a file or folder as a table so that you can query the data in Dremio.

note

To format a folder, all files in the folder must be the same format.

Method and URL

```
POST /api/v3/catalog/{id}
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String

Unique identifier of the file or folder you want to format. The ID can be a UUID or a text path. If the ID is a text path, use URL encoding to replace special characters with their UTF-8-equivalent characters: `%3A` for a colon; `%2F` for a forward slash, and `%20` for a space. For example, if the ID value is `dremio:/Samples/samples.dremio.com/Dremio University`, the URI-encoded ID is `dremio%3A%2FSamples%2Fsamples.dremio.com%2FDremio%20University`.

Example: c590ed7f-7142-4e1f-ba7d-94173afdc9a3

---

entityType Body   String

Type of the catalog object. To format a file or folder as a table, the entityType is `dataset`.

---

path Body   Array of String

Path of the file or folder you want to format, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the file or folder itself as the last item in the array. Get the path from the file or folder's children object in the response to a [Folder](/25.x/reference/api/catalog/container-folder) request.

Example: ["Samples", "samples.dremio.com", "Dremio University", "restaurant\_reviews.parquet"]

---

type Body   String

Type of dataset. For tables, the type is `PHYSICAL_DATASET`.

---

[accelerationRefreshPolicy](/25.x/reference/api/catalog/table#parameters-of-the-accelerationrefreshpolicy-object) Object

Attributes that define the acceleration refresh policy for the table.

---

[format](/25.x/reference/api/catalog/table#parameters-of-the-format-object) Body   String

Parameters that describe how to format the file or folder.

---

[accessControlList](/25.x/reference/api/catalog/table#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the table and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT", "ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT", "ALTER", "MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT", "ALTER"]}]}

#### Parameters of the `accelerationRefreshPolicy` Object[​](#parameters-of-the-accelerationrefreshpolicy-object "Direct link to parameters-of-the-accelerationrefreshpolicy-object")

activePolicyType Body   String

Policy to use for refreshing Reflections that are defined on the source. For this option to take effect, the neverRefresh parameter must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: Default. The Reflections are refreshed at the end of every period that is defined by refreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by refreshSchedule.
* `REFRESH_ON_DATA_CHANGES`: Reflections automatically refresh for underlying tables that are in Iceberg format when new snapshots are created after an update. If the Reflection refresh job finds no changes, then no data is updated. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency. Only available for tables in Iceberg format.

---

refreshPeriodMs Body   Integer

Refresh period to use for the data in all Reflections for the table. In milliseconds. Optional if you set activePolicyType to `PERIOD`. The default setting is `3600000` milliseconds or one hour, which is also the minimum amount of time that is supported.

Example: 3600000

---

refreshSchedule Body   String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source should be refreshed. Optional if you set activePolicyType to `SCHEDULE`. The default refreshSchedule setting is to refresh every day at 8:00 a.m.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:

* `0 0 0 * * ?` : Refreshes every day at midnight.
* `0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
* `0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

gracePeriodMs Body   Integer

Maximum age to allow for Reflection data used to accelerate queries. In milliseconds.

Example: 10800000

---

method Body   String

Method to use for refreshing the data in Reflections. For tables that are in the Apache Iceberg format; Parquet datasets in filesystems; or Parquet datasets, Avro datasets, or non-transactional ORC datasets in Glue, the value is `AUTO`. In this case, the method used depends on this algorithm:

1. The initial refresh of a Reflection is always a full refresh.
2. If the Reflection is created from a view that uses nested group-bys, joins, unions, or window functions, then a full refresh is performed.
3. If the changes to the base table are only appends, then an incremental refresh based on table snapshots is performed.
4. If the changes to the base table include non-append operations, then a partition-based incremental refresh is attempted.
5. If the partitions of the base table and the partitions of the Reflection are not compatible, or if either the base table or the Reflection is not partitioned, then a full refresh is performed.

Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections) for more information.

Enum: AUTO, FULL, INCREMENTAL

Example: FULL

---

refreshField Body   String

For the `INCREMENTAL` refresh method, the field to refresh for the table. Used only if the method is `INCREMENTAL`. This parameter applies only to tables that are not in the Apache Iceberg format.

Example: business\_id

---

neverExpire Body   Boolean

If the Reflection should never expire, `true`. Otherwise, `false`.

Example: false

---

neverRefresh Body   Boolean

If the Reflection should never refresh, `true`. Otherwise, `false`.

Example: false

#### Parameters of the `format` Object[​](#parameters-of-the-format-object "Direct link to parameters-of-the-format-object")

type Body   String

Type of data in the file or folder. All files in the folder must be the same format.

Enum: Delta, Excel, Iceberg, JSON, Parquet, Text, Unknown, XLS

---

ignoreOtherFileFormats Body   Boolean   Optional

If Dremio should ignore all non-Parquet files in the related folder structure so that the promoted table works as if only Parquet files are in the folder structure, set to `true`. Otherwise, set to `false` (default). Optional for Parquet folders.

Example: false

---

skipFirstLine Body   Boolean   Optional

If Dremio should skip the first line in the file or folder when creating the table, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Excel and Text types.

Example: true

---

extractHeader Body   Boolean   Optional

If Dremio should extract the table's column names from the first line of the file, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Excel and Text types.

Example: "

---

hasMergedCells Body   Boolean   Optional

If Dremio should expand merged cells in the file when creating the table, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Excel type.

Example: true

---

sheetName Body   String   Optional

For tables created from Excel files that contain multiple sheets, the name of the sheet to use to create the table. Default is the first sheet in the file (for files that contain multiple sheets).

Example: location\_1

---

fieldDelimiter Body   String   Optional

Character to use to indicate separate fields in the table. May be `,` for a comma (default), `\t` for a tab, `|` for a pipe, or a custom character. Optional for files or folders of the Text type.

---

quote Body   String   Optional

Character to use for quotes in the table. May be `"` for a double quote (default), `'` for a single quote, or a custom character. Optional for files or folders of the Text type.

---

comment Body   String   Optional

Character to use to indicate comments in the table. May be `#` for a number sign (default) or a custom character. Optional for files or folders of the Text type.

---

escape Body   String   Optional

Character used to indicate an escape in the table. May be `"` for a double quote (default), `` ` `` for a back quote, `\` for a backward slash, or a custom character. Optional for files or folders of the Text type.

---

lineDelimiter Body   String   Optional

Character used to indicate separate lines in the table. May be `\r\n` for a carriage return and a new line (default), `\n` for a new line, or a custom character. Optional for files or folders of the Text type.

---

autoGenerateColumnNames Body   Boolean   Optional

If Dremio should use the existing columnn names in the file or folder for the table columns, set to `true` (default). Otherwise, set to `false`. Optional for files or folders of the Text type.

Example: true

---

trimHeader Body   Boolean   Optional

If Dremio should trim column names to a specific number of characters when creating the table, set to `true`. Otherwise, set to `false` (default). Optional for files or folders of the Text type.

Example: true

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the table and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the table and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT", "ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the table.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the table. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
    "Samples",  
    "Dremio University",  
    "restaurant_reviews.parquet"  
  ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Parquet"  
  },  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "createdAt": "2024-01-13T19:52:01.894Z",  
    "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
    "accelerationRefreshPolicy": {  
      "activePolicyType": "PERIOD",  
      "refreshPeriodMs": 3600000,  
      "refreshSchedule": "0 56 18 * * *",  
      "gracePeriodMs": 259200000,  
      "method": "FULL",  
      "neverExpire": true,  
      "neverRefresh": false,  
      "sourceRefreshOnDataChanges": false  
    },  
    "isMetadataExpired": false,  
    "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
    "format": {  
      "type": "Parquet",  
      "name": "restaurant_reviews.parquet",  
      "fullPath": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "restaurant_reviews.parquet"  
      ],  
      "ctime": 0,  
      "isFolder": false,  
      "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
      "ignoreOtherFileFormats": "false",  
      "autoCorrectCorruptDates": true  
    },  
    "accessControlList": {  
      "users": [  
        {  
          "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        },  
        {  
          "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
          "permissions": [  
            "SELECT",  
            "ALTER",  
            "MANAGE_GRANTS"  
          ]  
        }  
      ],  
      "roles": [  
        {  
          "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        }  
      ]  
    },  
    "owner": {  
      "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
      "ownerType": "USER"  
    },  
    "fields": [  
      {  
        "name": "_id",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "name",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "city",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "state",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "categories",  
        "type": {  
          "name": "LIST",  
          "subSchema": [  
            {  
              "type": {  
                "name": "VARCHAR"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "review_count",  
        "type": {  
          "name": "BIGINT"  
        }  
      },  
      {  
        "name": "stars",  
        "type": {  
          "name": "DOUBLE"  
        }  
      },  
      {  
        "name": "attributes",  
        "type": {  
          "name": "STRUCT",  
          "subSchema": [  
            {  
              "name": "Parking",  
              "type": {  
                "name": "STRUCT",  
                "subSchema": [  
                  {  
                    "name": "garage",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "street",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "lot",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "valet",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  }  
                ]  
              }  
            },  
            {  
              "name": "Accepts Credit Cards",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Wheelchair Accessible",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Price Range",  
              "type": {  
                "name": "BIGINT"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "date",  
        "type": {  
          "name": "VARCHAR"  
        }  
      }  
    ],  
    "approximateStatisticsAllowed": false  
  }
```

Example Request for Excel format type

```
curl -X POST 'https://{hostname}/api/v3/catalog/dremio%3A%2FSamples%2Fsamples.dremio.com%2FDremio%20University%2Foracle-departments.xlsx' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "oracle-departments.xlsx"  
    ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Excel",  
    "extractHeader": true,  
    "hasMergedCells": true,  
    "sheetName": "Sheet1"  
    }  
}'
```

Example Request for Text format type

```
curl -X POST 'https://{hostname}/api/v3/catalog/6ba3bd6e-fd27-4572-a535-77e1548283b3' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "Dremio University",  
    "airbnb_listings.csv"  
  ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Text",  
    "fieldDelimiter": ",",  
    "skipFirstLine": false,  
    "extractHeader": true,  
    "quote": "\"",  
    "comment": "#",  
    "escape": "\"",  
    "lineDelimiter": "\r\n",  
    "autoGenerateColumnNames": true,  
    "trimHeader": false  
  }  
}'
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a Table by ID[​](#retrieving-a-table-by-id "Direct link to Retrieving a Table by ID")

Retrieve a table by specifying the table's `id` value.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to retrieve.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "createdAt": "2024-01-13T19:52:01.894Z",  
    "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
    "accelerationRefreshPolicy": {  
      "activePolicyType": "PERIOD",  
      "refreshPeriodMs": 3600000,  
      "refreshSchedule": "0 56 18 * * *",  
      "gracePeriodMs": 259200000,  
      "method": "FULL",  
      "neverExpire": true,  
      "neverRefresh": false,  
      "sourceRefreshOnDataChanges": false  
    },  
    "isMetadataExpired": false,  
    "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
    "format": {  
      "type": "Parquet",  
      "name": "restaurant_reviews.parquet",  
      "fullPath": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "restaurant_reviews.parquet"  
      ],  
      "ctime": 0,  
      "isFolder": false,  
      "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
      "ignoreOtherFileFormats": false,  
      "autoCorrectCorruptDates": true  
    },  
    "accessControlList": {  
      "users": [  
        {  
          "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        },  
        {  
          "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
          "permissions": [  
            "SELECT",  
            "ALTER",  
            "MANAGE_GRANTS"  
          ]  
        }  
      ],  
      "roles": [  
        {  
          "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        }  
      ]  
    },  
    "owner": {  
      "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
      "ownerType": "USER"  
    },  
    "fields": [  
      {  
        "name": "_id",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "name",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "city",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "state",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "categories",  
        "type": {  
          "name": "LIST",  
          "subSchema": [  
            {  
              "type": {  
                "name": "VARCHAR"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "review_count",  
        "type": {  
          "name": "BIGINT"  
        }  
      },  
      {  
        "name": "stars",  
        "type": {  
          "name": "DOUBLE"  
        }  
      },  
      {  
        "name": "attributes",  
        "type": {  
          "name": "STRUCT",  
          "subSchema": [  
            {  
              "name": "Parking",  
              "type": {  
                "name": "STRUCT",  
                "subSchema": [  
                  {  
                    "name": "garage",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "street",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "lot",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "valet",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  }  
                ]  
              }  
            },  
            {  
              "name": "Accepts Credit Cards",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Wheelchair Accessible",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Price Range",  
              "type": {  
                "name": "BIGINT"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "date",  
        "type": {  
          "name": "VARCHAR"  
        }  
      }  
    ],  
    "approximateStatisticsAllowed": false  
  }
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Table by Path[​](#retrieving-a-table-by-path "Direct link to Retrieving a Table by Path")

Retrieve a table by specifying the table's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

Table's location within Dremio, using forward slashes as separators. For example, for the "NYC-taxi-trips" table in the "samples.dremio.com" folder within the source "Samples," the path is `Samples/samples.dremio.com/NYC-taxi-trips`. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: Samples/samples.dremio.com/Dremio%20University/restaurant\_reviews.parquet

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Samples/samples.dremio.com/Dremio%20University/restaurant_reviews.parquet' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "c9c11d32-0576-4200-5a5b-8c7229cb3d72",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
      "Samples",  
      "samples.dremio.com",  
      "Dremio University",  
      "restaurant_reviews.parquet"  
    ],  
    "createdAt": "2024-01-13T19:52:01.894Z",  
    "tag": "cb2905bb-39c0-497f-ae74-4c310d534f25",  
    "accelerationRefreshPolicy": {  
      "activePolicyType": "PERIOD",  
      "refreshPeriodMs": 3600000,  
      "refreshSchedule": "0 56 18 * * *",  
      "gracePeriodMs": 259200000,  
      "method": "FULL",  
      "neverExpire": true,  
      "neverRefresh": false,  
      "sourceRefreshOnDataChanges": false  
    },  
    "isMetadataExpired": false,  
    "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
    "format": {  
      "type": "Parquet",  
      "name": "restaurant_reviews.parquet",  
      "fullPath": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "restaurant_reviews.parquet"  
      ],  
      "ctime": 0,  
      "isFolder": false,  
      "location": "/samples.dremio.com/Dremio University/restaurant_reviews.parquet",  
      "ignoreOtherFileFormats": false,  
      "autoCorrectCorruptDates": true  
    },  
    "accessControlList": {  
      "users": [  
        {  
          "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        },  
        {  
          "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
          "permissions": [  
            "SELECT",  
            "ALTER",  
            "MANAGE_GRANTS"  
          ]  
        }  
      ],  
      "roles": [  
        {  
          "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
          "permissions": [  
            "SELECT",  
            "ALTER"  
          ]  
        }  
      ]  
    },  
    "owner": {  
      "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
      "ownerType": "USER"  
    },  
    "fields": [  
      {  
        "name": "_id",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "name",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "city",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "state",  
        "type": {  
          "name": "VARCHAR"  
        }  
      },  
      {  
        "name": "categories",  
        "type": {  
          "name": "LIST",  
          "subSchema": [  
            {  
              "type": {  
                "name": "VARCHAR"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "review_count",  
        "type": {  
          "name": "BIGINT"  
        }  
      },  
      {  
        "name": "stars",  
        "type": {  
          "name": "DOUBLE"  
        }  
      },  
      {  
        "name": "attributes",  
        "type": {  
          "name": "STRUCT",  
          "subSchema": [  
            {  
              "name": "Parking",  
              "type": {  
                "name": "STRUCT",  
                "subSchema": [  
                  {  
                    "name": "garage",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "street",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "lot",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  },  
                  {  
                    "name": "valet",  
                    "type": {  
                      "name": "BOOLEAN"  
                    }  
                  }  
                ]  
              }  
            },  
            {  
              "name": "Accepts Credit Cards",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Wheelchair Accessible",  
              "type": {  
                "name": "BOOLEAN"  
              }  
            },  
            {  
              "name": "Price Range",  
              "type": {  
                "name": "BIGINT"  
              }  
            }  
          ]  
        }  
      },  
      {  
        "name": "date",  
        "type": {  
          "name": "VARCHAR"  
        }  
      }  
    ],  
    "approximateStatisticsAllowed": false  
  }
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Table[​](#updating-a-table "Direct link to Updating a Table")

Update the specified table in Dremio.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to update.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

entityType Body   String

Type of the catalog object. For tables, the entityType is `dataset`.

---

id Body   String (UUID)

Unique identifier of the table that you want to update.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

---

path Body   Array of String

Path of the table that you want to update, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the table itself as the last item in the array. Get the path from the table's children object in the response to a [Folder](/25.x/reference/api/catalog/container-folder) request.

Example: ["Samples", "samples.dremio.com", "Dremio University", "restaurant\_reviews.parquet"]

---

tag Body   String (UUID)   Optional

Unique identifier of the version of the table that you want to update. If you provide a tag in the request body, Dremio uses the tag to ensure that you are requesting to update the most recent version of the table. If you do not provide a tag, Dremio automatically updates the most recent version of the table.

Example: cb2905bb-39c0-497f-ae74-4c310d534f25

---

type Body   String

Type of dataset. For tables, the type is `PHYSICAL_DATASET`.

Example:

---

[accelerationRefreshPolicy](/25.x/reference/api/catalog/table#parameters-of-the-accelerationrefreshpolicy-object-1) Object

Attributes that define the acceleration refresh policy for the table.

---

[format](/25.x/reference/api/catalog/table#parameters-of-the-format-object-1) Body   String

Parameters that describe the table's format.

---

[accessControlList](/25.x/reference/api/catalog/table#parameters-of-the-accesscontrollist-object-1) Body   String   Optional

Enterprise only. Object used to specify which users and roles should have access to the table and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]}

---

#### Parameters of the `accelerationRefreshPolicy` Object[​](#parameters-of-the-accelerationrefreshpolicy-object-1 "Direct link to parameters-of-the-accelerationrefreshpolicy-object-1")

activePolicyType Body   String

Policy to use for refreshing Reflections that are defined on the source. For this option to take effect, the neverRefresh parameter must be set to `false`.

The possible values are:

* `NEVER`: The Reflections are never refreshed.
* `PERIOD`: Default. The Reflections are refreshed at the end of every period that is defined by refreshPeriodMs.
* `SCHEDULE`: The Reflections are refreshed according to the schedule that is set by refreshSchedule.
* `REFRESH_ON_DATA_CHANGES`: Reflections automatically refresh for underlying tables that are in Iceberg format when new snapshots are created after an update. If the Reflection refresh job finds no changes, then no data is updated. Reflections that are automatically updated based on Iceberg source table changes also update according to the source-level policy as the minimum refresh frequency. Only available for tables in Iceberg format.

---

refreshPeriodMs Body   Integer

Refresh period to use for the data in all Reflections for the table. In milliseconds. Optional if you set activePolicyType to `PERIOD`. The default setting is `3600000` milliseconds or one hour, which is also the minimum amount of time that is supported.

Example: 3600000

---

refreshSchedule Body   String

A cron expression that sets the schedule, in UTC time, according to which the Reflections that are defined on the source should be refreshed. Optional if you set activePolicyType to `SCHEDULE`. The default refreshSchedule setting is to refresh every day at 8:00 a.m.

| Field | Allowed Values | Allowed Special Characters |
| --- | --- | --- |
| Second | 0 | N/A |
| Minute | 0-59 | N/A |
| Hour | 0-23 | N/A |
| Day of month | N/A | \* ? |
| Month | N/A | \* ? |
| Days of week | 1-7 or SUN-SAT | , - \* ? |

| Special Character | Description |
| --- | --- |
| \* | Used to specify all values for a field. For `Day of month`, specifies every day of the month. For `Month`, specifies every month. For `Days of week`, specifies every day of the week. |
| ? | Equivalent to \*. |
| , | Used to specify two or more days in the `Days of week` field. For example, `MON,WED,FRI`. |
| - | Used to specify ranges in the `Days of week` field. For example, `1-3` is equivalent to `Sunday, Monday, and Tuesday`. |

Examples:

* `0 0 0 * * ?` : Refreshes every day at midnight.
* `0 45 15 * * 1,4,7` : Refreshes at 15:45 on Sunday, Wednesday, and Saturday.
* `0 15 7 ? * 2-6` : Refreshes at 7:15 on Monday and Friday.

---

gracePeriodMs Body   Integer

Maximum age to allow for Reflection data used to accelerate queries. In milliseconds.

Example: 10800000

---

method Body   String

Method to use for refreshing the data in Reflections. For tables that are in the Apache Iceberg format; Parquet datasets in filesystems; or Parquet datasets, Avro datasets, or non-transactional ORC datasets in Glue, the value is `AUTO`. In this case, the method used depends on this algorithm:

1. The initial refresh of a Reflection is always a full refresh.
2. If the Reflection is created from a view that uses nested group-bys, joins, unions, or window functions, then a full refresh is performed.
3. If the changes to the base table are only appends, then an incremental refresh based on table snapshots is performed.
4. If the changes to the base table include non-append operations, then a partition-based incremental refresh is attempted.
5. If the partitions of the base table and the partitions of the Reflection are not compatible, or if either the base table or the Reflection is not partitioned, then a full refresh is performed.

Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections) for more information.

Enum: AUTO, FULL, INCREMENTAL

Example: FULL

---

refreshField Body   String

For the `INCREMENTAL` refresh method, the field to refresh for the table. Used only if the method is `INCREMENTAL`. This parameter applies only to tables that are not in the Apache Iceberg format.

Example: business\_id

---

neverExpire Body   Boolean

If the Reflection should never expire, `true`. Otherwise, `false`.

Example: false

---

neverRefresh Body   Boolean

If the Reflection should never refresh, `true`. Otherwise, `false`.

Example: false

#### Parameters of the `format` Object[​](#parameters-of-the-format-object-1 "Direct link to parameters-of-the-format-object-1")

type Body   String

Type of data in the table.

Enum: Delta, Excel, Iceberg, JSON, Parquet, Text, Unknown, XLS

---

skipFirstLine Body   Boolean   Optional

If Dremio should skip the first line in the table, set to `true`. Otherwise, set to `false` (default). Optional for Excel and Text types.

Example: true

---

extractHeader Body   Boolean   Optional

If Dremio should extract the table's column names from the first line of the file, set to `true`. Otherwise, set to `false` (default). Optional for tables created from files or folders of the Excel and Text types.

Example: true

---

hasMergedCells Body   Boolean   Optional

If Dremio should expand merged cells in the table, set to `true`. Otherwise, set to `false` (default). Optional for tables created from files or folders of the Excel type.

Example: true

---

fieldDelimiter Body   String   Optional

Character to use to indicate separate fields in the table. May be `,` for a comma (default), `\t` for a tab, `|` for a pipe, or a custom character. Optional for tables created from files or folders of the Text type.

---

quote Body   String   Optional

Character to use for quotes in the table. May be `\"` for a double quote (default), `'` for a single quote, or a custom character. Optional for tables created from files or folders of the Text type.

---

comment Body   String   Optional

Character to use to indicate comments for the table. May be `#` for a number sign (default) or a custom character. Optional for tables created from files or folders of the Text type.

---

escape Body   String   Optional

Character to use to indicate an escape for the table. May be `\"` for a double quote (default), `` ` `` for a back quote, `\\` for a backward slash, or a custom character. Optional for tables created from files or folders of the Text type.

---

lineDelimiter Body   String   Optional

Character to use to indicate separate lines for the table. May be `\r\n` for a carriage return and a new line (default), `\n` for a new line, or a custom character. Optional for tables created from files or folders of the Text type.

Example:

---

autoGenerateColumnNames Body   Boolean   Optional

If Dremio should use the existing columnn names for the table columns, set to `true` (default). Otherwise, set to `false`. Optional for tables created from files or folders of the Text type.

Example: true

---

trimHeader Body   Boolean   Optional

If Dremio should trim column names to a specific number of characters when updating the table, set to `true`. Otherwise, set to `false` (default). Optional for tables created from files or folders of the Text type.

Example: true

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the table and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/table#parameters-of-objects-in-the-users-and-roles-arrays-1) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the table and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String

Enterprise only. Unique identifier of the user or role that should have access to the table.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String

Enterprise only. List of privileges the user or role should have on the table. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/dba1e4fe-6351-44d2-a3e0-7aa20e782bf3' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "id": "dba1e4fe-6351-44d2-a3e0-7aa20e782bf3",  
  "path": [  
    "Samples",  
    "samples.dremio.com",  
    "Dremio University",  
    "airbnb_listings.csv"  
  ],  
  "type": "PHYSICAL_DATASET",  
  "format": {  
    "type": "Text",  
    "fieldDelimiter": ",",  
    "skipFirstLine": false,  
    "extractHeader": true,  
    "quote": "\"",  
    "comment": "#",  
    "escape": "\"",  
    "lineDelimiter": "\r\n",  
    "autoGenerateColumnNames": true,  
    "trimHeader": true  
  }  
}'
```

Example Response

```
{  
    "entityType": "dataset",  
    "id": "dba1e4fe-6351-44d2-a3e0-7aa20e782bf3",  
    "type": "PHYSICAL_DATASET",  
    "path": [  
        "Samples",  
        "samples.dremio.com",  
        "Dremio University",  
        "airbnb_listings.csv"  
    ],  
    "createdAt": "2024-01-23T21:26:59.568Z",  
    "tag": "fc1707df-35a1-45c1-87d7-5f66fb11a729",  
    "format": {  
        "type": "Text",  
        "ctime": 0,  
        "isFolder": false,  
        "location": "/samples.dremio.com/Dremio University/airbnb_listings.csv",  
        "fieldDelimiter": ",",  
        "skipFirstLine": false,  
        "extractHeader": true,  
        "quote": "\"",  
        "comment": "#",  
        "escape": "\"",  
        "lineDelimiter": "\r\n",  
        "autoGenerateColumnNames": true,  
        "trimHeader": true  
    },  
    "accessControlList": {},  
    "owner": {  
        "ownerId": "c590ed7f-7142-4e1f-ba7d-94173afdc9a3",  
        "ownerType": "USER"  
    },  
    "fields": [  
        {  
            "name": "id",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "listing_url",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "scrape_id",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "last_scraped",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "name",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "summary",  
            "type": {  
                "name": "VARCHAR"  
            }  
        },  
        {  
            "name": "reviews_per_month",  
            "type": {  
                "name": "VARCHAR"  
            }  
        }  
    ],  
    "approximateStatisticsAllowed": false  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Refreshing the Reflections on a Table[​](#refreshing-the-reflections-on-a-table "Direct link to Refreshing the Reflections on a Table")

Refresh the Reflections associated with the specified table.

note

Refreshing a table's Reflections does not refresh its metadata. Read [Refreshing Metadata](/25.x/admin/metadata-caching/) to learn how to refresh table metadata. Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections/) for more information about refreshing Reflections.

Method and URL

```
POST /api/v3/catalog/{id}/refresh
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to refresh.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72/refresh' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Reverting a Table to a File or Folder[​](#reverting-a-table-to-a-file-or-folder "Direct link to Reverting a Table to a File or Folder")

Revert a table in a source to change the data in the table back to its original format, file or folder. For more information, read [Formatting Data to a Table](/25.x/sonar/data-sources/entity-promotion/) and [Removing Formatting on Data](/25.x/sonar/data-sources/entity-promotion/)

note

If a table is saved in your home space, the revert request will delete the table entirely. The revert endpoint only changes a table back to a file or folder if the table is saved in a source.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the table that you want to revert to a file or folder.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

File](/25.x/reference/api/catalog/file)[Next

User-Defined Function](/25.x/reference/api/catalog/user-defined-function)

* [Table Attributes](#table-attributes)
* [Formatting a File or Folder as a Table](#formatting-a-file-or-folder-as-a-table)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Table by ID](#retrieving-a-table-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Table by Path](#retrieving-a-table-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a Table](#updating-a-table)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Refreshing the Reflections on a Table](#refreshing-the-reflections-on-a-table)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)
* [Reverting a Table to a File or Folder](#reverting-a-table-to-a-file-or-folder)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/view/

Version: 25.x

On this page

# View

Use the Catalog API to retrieve, create, update, and delete [views](/25.x/sonar/query-manage/managing-data/datasets/).

View Object

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",   
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "permissions": [  
    "READ",  
    "WRITE",  
    "ALTER_REFLECTION",  
    "SELECT",  
    "ALTER",  
    "VIEW_REFLECTION",  
    "MODIFY",  
    "MANAGE_GRANTS",  
    "CREATE_TABLE",  
    "DROP",  
    "EXTERNAL_QUERY",  
    "INSERT",  
    "TRUNCATE",  
    "DELETE",  
    "UPDATE",  
    "EXECUTE",  
    "CREATE_SOURCE",  
    "ALL"  
  ],  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

## View Attributes[​](#view-attributes "Direct link to View Attributes")

entityType String

Type of the catalog object. For views, the entityType is `dataset`.

Example: dataset

---

id String (UUID)

Unique identifier of the view.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

---

type String

Type of dataset. For views, the type is `VIRTUAL_DATASET`.

Example: VIRTUAL\_DATASET

---

path Array of String

Path of the view within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the view itself as the last item in the array.

Example: ["Business", "Transportation", "NYC-taxi-trips-short-distance"]

---

createdAt String

Date and time that the view was created, in UTC format.

Example: 2022-11-17T18:31:23.236Z

---

isMetadataExpired Boolean

* If true, the metadata of the tables that the view is defined on needs to be refreshed. To refresh it, run the ALTER VIEW command, using the clause REFRESH METADATA.
* If false, the metadata can still be used for planning queries against the view.
* If NULL, metadata has never yet been collected for the tables that the view is defined on.

---

lastMetadataRefreshAt String

Date and time that the metadata of the tables that the view is defined on was last refreshed. In UTC format.

Example: 2024-01-31T09:50:01.012Z

---

tag String (UUID)

Unique identifier of the version of the view. Dremio changes the tag whenever the view changes and uses the tag to ensure that PUT requests apply to the most recent version of the view.

Example: f90d1526-e64b-47b1-9ab0-d25df5247cab

---

sql String

SQL query used to create the view.

Example: SELECT \* FROM "NYC-taxi-trips" WHERE trip\_distance\_mi <= 2.0 ORDER BY trip\_distance\_mi ASC

---

sqlContext Array of String

Context for the SQL query used to create the view.

Example: ["Samples", "samples.dremio.com"]

---

[accessControlList](/25.x/reference/api/catalog/view#attributes-of-the-accesscontrollist-object) Object

Enterprise only. Information about users and roles with access to the view and the specific privileges each user or role has. May include an array of users, an array of roles, or both, depending on the configured access and privileges. The accessControlList array is empty if view-specific access control privileges are not set.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"] },{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"] }],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]}

---

permissions Array of String

Enterprise-only. List of the privileges that you have on the view. Only appears in the response if the request URL includes the `permissions` query parameter. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["READ","WRITE","ALTER\_REFLECTION","SELECT","ALTER","VIEW\_REFLECTION","MODIFY","MANAGE\_GRANTS","CREATE\_TABLE","DROP","EXTERNAL\_QUERY","INSERT","TRUNCATE","DELETE","UPDATE","EXECUTE","CREATE\_SOURCE","ALL"]

---

[owner](/25.x/reference/api/catalog/view#attributes-of-the-owner-object) String

Information about the view's owner.

Example: {"ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8","ownerType": "USER"}

---

[fields](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-fields-array) Array of Object

Attributes that represent the dataset schema.

#### Attributes of the `accessControlList` Object[​](#attributes-of-the-accesscontrollist-object "Direct link to attributes-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of users with access to the view and the specific privileges each user has.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT", "ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT", "ALTER", "MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-users-and-roles-arrays) Array of Object

Enterprise only. List of roles whose members have access to the view and the specific privileges each role has.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Attributes of Objects in the `users` and `roles` Arrays[​](#attributes-of-objects-in-the-users-and-roles-arrays "Direct link to attributes-of-objects-in-the-users-and-roles-arrays")

id String

Enterprise only. Unique identifier of the user or role with access to the view.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Array of String

Enterprise only. List of privileges the user or role has on the view. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT","ALTER"]

#### Attributes of the `owner` Object[​](#attributes-of-the-owner-object "Direct link to attributes-of-the-owner-object")

ownerId String (UUID)

Unique identifier of the view's owner.

Example: 30fca499-4abc-4469-7142-fc8dd29acac8

---

ownerType String

Type of owner of the view.

Enum: USER, ROLE

Example: USER

#### Attributes of Objects in the `fields` Array[​](#attributes-of-objects-in-the-fields-array "Direct link to attributes-of-objects-in-the-fields-array")

name String

Name of the view field.

Example: pickup\_datetime

---

[type](/25.x/reference/api/catalog/view#attributes-of-the-type-object) Object

Information about the view field.

#### Attributes of the `type` Object[​](#attributes-of-the-type-object "Direct link to attributes-of-the-type-object")

name String

Name of the view field's type.

Enum: STRUCT, LIST, UNION, INTEGER, BIGINT, FLOAT, DOUBLE, VARCHAR, VARBINARY, BOOLEAN, DECIMAL, TIME, DATE, TIMESTAMP, INTERVAL DAY TO SECOND, INTERVAL YEAR TO MONTH

Example: TIMESTAMP

---

precision Integer

Total number of digits in the number. Included only for the `DECIMAL` type.

Example: 38

---

scale Integer

Number of digits to the right of the decimal point. Included only for the `DECIMAL` type.

Example: 2

---

[subSchema](/25.x/reference/api/catalog/view#attributes-of-objects-in-the-subschema-array) Array of Object

List of objects that represent the field's composition. For example, a field composed of data about a restaurant might have a subSchema with an object for parking options, another for payment methods, and so on. subSchemas may be nested within other subSchemas. subSchema is listed only for the `STRUCT`, `LIST`, and `UNION` types.

#### Attributes of Objects in the `subSchema` Array[​](#attributes-of-objects-in-the-subschema-array "Direct link to attributes-of-objects-in-the-subschema-array")

name String

Name for the subSchema object.

Example: cash

---

type Object

Object that contains a `name` attribute that provides the field's type.

Example: {"name": "BOOLEAN"}

## Creating a View[​](#creating-a-view "Direct link to Creating a View")

Create a view from a table in Dremio.

Method and URL

```
POST /api/v3/catalog
```

### Parameters[​](#parameters "Direct link to Parameters")

entityType Body   String

Type of the catalog object. For views, the entityType is `dataset`.

---

type Body   String

Type of dataset. For views, the type is `VIRTUAL_DATASET`.

---

path Body   Array of String

Path of the location where you want to save the view within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by a name for the view itself as the last item in the array. The name of the view cannot include the following special characters: `/`, `:`, `[`, or `]`. Views can only be created in spaces.

Example: ["Business", "Transportation", "NYC-taxi-trips-short-distance"]

---

sql Body   String

SQL query to use to create the view.

Example: SELECT \* FROM "NYC-taxi-trips" WHERE trip\_distance\_mi <= 2.0 ORDER BY trip\_distance\_mi ASC

---

sqlContext Body   Array of String

Context for the SQL query to use to create the view.

Example: ["Samples", "samples.dremio.com"]

---

[accessControlList](/25.x/reference/api/catalog/view#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the view and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

Example: {"users": [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3", "permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8", "permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}],"roles": [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390", "permissions": ["SELECT","ALTER"]}]}

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object "Direct link to parameters-of-the-accesscontrollist-object")

[users](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) [Body]   Array of Object   Optional

Enterprise only. List of users who should have access to the view and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the view and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays "Direct link to parameters-of-objects-in-the-users-and-roles-arrays")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the view.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the view. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "type": "VIRTUAL_DATASET",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  }  
}'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a View by ID[​](#retrieving-a-view-by-id "Direct link to Retrieving a View by ID")

Retrieve a view by specifying the view's `id` value.

Method and URL

```
GET /api/v3/catalog/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the view that you want to retrieve.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/ef99ab32-89ca-4d1c-9e91-2c8be861bb8a' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a View by Path[​](#retrieving-a-view-by-path "Direct link to Retrieving a View by Path")

Retrieve a view by specifying the view's path.

Method and URL

```
GET /api/v3/catalog/by-path/{path}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

path Path   String

View's location within Dremio, using forward slashes as separators. For example, for the "NYC-taxi-trips" view in the "samples.dremio.com" folder within the space "Transportation," the path is `Transportation/samples.dremio.com/NYC-taxi-trips`. If the name of any component in the path includes special characters for URLs, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: Business/Transportation/NYC-taxi-trips-short-distance

---

include Query   String   Optional

Include a non-default attribute in the response. The available value for the include query parameter is `permissions`. For more information, read [include and exclude Query Parameters](/25.x/reference/api/#include-and-exclude-query-parameters).

Example: ?include=permissions

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/by-path/Business/Transportation/NYC-taxi-trips-short-distance' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "createdAt": "2022-11-17T18:31:23.236Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT * FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a View[​](#updating-a-view "Direct link to Updating a View")

Update a view in Dremio.

Method and URL

```
PUT /api/v3/catalog/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the view that you want to update.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

---

entityType Body   String

Type of the catalog object. For views, the entityType is `dataset`.

---

type Body   String

Type of dataset. For views, type is `VIRTUAL_DATASET`.

---

path Body   Array of String

Path of the location where you want to save the updated view within Dremio, expressed as an array. The path consists of the space, followed by any folder and subfolders, followed by the name for the view itself as the last item in the array. Views can only be saved in spaces.

Example: ["Business", "Transportation", "NYC-taxi-trips-short-distance"]

---

tag Body   String (UUID)   Optional

Unique identifier of the version of the view that you want to update. If you provide a tag in the request body, Dremio uses the tag to ensure that you are requesting to update the most recent version of the view. If you do not provide a tag, Dremio automatically updates the most recent version of the view.

Example: f90d1526-e64b-47b1-9ab0-d25df5247cab

---

sql Body   String

SQL query to use to update the view.

Example: SELECT \* FROM "NYC-taxi-trips" WHERE trip\_distance\_mi <= 2.0 ORDER BY trip\_distance\_mi DESC

---

sqlContext Body   Array of String

Context for the SQL query to use for the updated view.

Example: ["Samples", "samples.dremio.com"]

---

[accessControlList](/25.x/reference/api/catalog/view#parameters-of-the-accesscontrollist-object) Body   Object   Optional

Enterprise only. Object used to specify which users and roles should have access to the view and the specific privileges each user or role should have. May include an array of users, an array of roles, or both.

#### Parameters of the `accessControlList` Object[​](#parameters-of-the-accesscontrollist-object-1 "Direct link to parameters-of-the-accesscontrollist-object-1")

[users](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of users who should have access to the view and the specific privileges each user should have.

Example: [{"id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3","permissions": ["SELECT","ALTER"]},{"id": "30fca499-4abc-4469-7142-fc8dd29acac8","permissions": ["SELECT","ALTER","MANAGE\_GRANTS"]}]

---

[roles](/25.x/reference/api/catalog/view#parameters-of-objects-in-the-users-and-roles-arrays) Body   Array of Object   Optional

Enterprise only. List of roles whose members should have access to the view and the specific privileges each role should have.

Example: [{"id": "76a9884b-aea5-46d5-a73a-000edf23f390","permissions": ["SELECT","ALTER"]}]

##### Parameters of Objects in the `users` and `roles` Arrays[​](#parameters-of-objects-in-the-users-and-roles-arrays-1 "Direct link to parameters-of-objects-in-the-users-and-roles-arrays-1")

id Body   String   Optional

Enterprise only. Unique identifier of the user or role who should have access to the view.

Example: c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3

---

permissions Body   Array of String   Optional

Enterprise only. List of privileges the user or role should have on the view. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["SELECT", "ALTER"]

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/ef99ab32-89ca-4d1c-9e91-2c8be861bb8a' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-short-distance"  
  ],  
  "type": "VIRTUAL_DATASET",  
  "tag": "f90d1526-e64b-47b1-9ab0-d25df5247cab",  
  "sql": "SELECT trip_distance_mi, fare_amount, tip_amount FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi DESC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ]  
}'
```

Example Response

```
{  
  "entityType": "dataset",  
  "id": "ef99ab32-89ca-4d1c-9e91-2c8be861bb8a",  
  "type": "VIRTUAL_DATASET",  
  "path": [  
    "Business",  
    "Transportation",  
    "NYC-taxi-trips-by-distance"  
  ],  
  "createdAt": "2023-01-20T15:26:39.780Z",  
  "isMetadataExpired": false,   
  "lastMetadataRefreshAt": "2024-01-31T09:50:01.012Z",  
  "tag": "7cab1a42-8835-4d31-827b-fedee1ad38d1",  
  "sql": "SELECT trip_distance_mi, fare_amount, tip_amount FROM \"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi DESC",  
  "sqlContext": [  
    "Samples",  
    "samples.dremio.com"  
  ],  
  "accessControlList": {  
    "users": [  
      {  
        "id": "c590ed7f-b2b4-4e1f-ba7d-94173afdc9a3",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      },  
      {  
        "id": "30fca499-4abc-4469-7142-fc8dd29acac8",  
        "permissions": [  
          "SELECT",  
          "ALTER",  
          "MANAGE_GRANTS"  
        ]  
      }  
    ],  
    "roles": [  
      {  
        "id": "76a9884b-aea5-46d5-a73a-000edf23f390",  
        "permissions": [  
          "SELECT",  
          "ALTER"  
        ]  
      }  
    ]  
  },  
  "owner": {  
    "ownerId": "30fca499-4abc-4469-7142-fc8dd29acac8",  
    "ownerType": "USER"  
  },  
  "fields": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "passenger_payment_method",  
      "type": {  
        "name": "STRUCT",  
        "subSchema": [  
          {  
            "name": "cash",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "credit-debit",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "payment-app",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          },  
          {  
            "name": "other",  
            "type": {  
              "name": "BOOLEAN"  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Refreshing the Reflections on a View[​](#refreshing-the-reflections-on-a-view "Direct link to Refreshing the Reflections on a View")

Refresh the Reflections associated with the specified view.

Read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections) to learn how refreshing works.

Method and URL

```
POST /api/v3/catalog/{id}/refresh
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier for the view you want to refresh.

Example: c9c11d32-0576-4200-5a5b-8c7229cb3d72

Example Request

```
curl -X POST 'https://api.dremio.cloud//api/v3/catalog/c9c11d32-0576-4200-5a5b-8c7229cb3d72/refresh' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Deleting a View[​](#deleting-a-view "Direct link to Deleting a View")

Delete the specified view.

Method and URL

```
DELETE /api/v3/catalog/{id}
```

### Parameters[​](#parameters-5 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the view that you want to delete.

Example: ef99ab32-89ca-4d1c-9e91-2c8be861bb8a

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/catalog/ef99ab32-89ca-4d1c-9e91-2c8be861bb8a' \  
-H 'Authorization: Bearer <PersonalAccessToken>' \  
-H 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

204   No Content

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

User-Defined Function](/25.x/reference/api/catalog/user-defined-function)[Next

Lineage](/25.x/reference/api/catalog/lineage)

* [View Attributes](#view-attributes)
* [Creating a View](#creating-a-view)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a View by ID](#retrieving-a-view-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a View by Path](#retrieving-a-view-by-path)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Updating a View](#updating-a-view)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)
* [Refreshing the Reflections on a View](#refreshing-the-reflections-on-a-view)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting a View](#deleting-a-view)
  + [Parameters](#parameters-5)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/lineage/

Version: 25.x

On this page

# Lineage Enterprise

Use the Catalog API to retrieve lineage information about datasets (tables and views). The lineage object includes information about the dataset's sources, parent objects, and child objects.

Lineage Object

```
{  
  "sources": [  
    {  
      "id": "21077e5d-fe6f-4a29-843f-58fa3acb17c2",  
      "path": [  
        "Samples"  
      ],  
      "tag": "Iz1v71CeTQY=",  
      "type": "CONTAINER",  
      "containerType": "SOURCE",  
      "createdAt": "2022-02-14T21:57:48.794Z"  
    }  
  ],  
  "parents": [  
    {  
      "id": "3419fa3a-b5b3-4438-b864-a27ec4e18752",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zips.json"  
      ],  
      "tag": "MAntohVzwLw=",  
      "type": "DATASET",  
      "datasetType": "PROMOTED",  
      "createdAt": "2023-01-18T18:49:09.669Z"  
    }  
  ],  
  "children": [  
    {  
      "id": "170e211e-4235-4d8d-acb5-3d4dbfe99c75",  
      "path": [  
        "@dremio",  
        "NYC_zip"  
      ],  
      "tag": "OWKrfpEKzW4=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T02:11:46.344Z"  
    },  
    {  
      "id": "7f79c068-a3c3-4af7-8cd4-35896ef0a0e0",  
      "path": [  
        "@dremio",  
        "Chicago_zip"  
      ],  
      "tag": "gsaDW5h4GCs=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T00:09:12.461Z"  
    }  
  ]  
}
```

## Lineage Attributes[​](#lineage-attributes "Direct link to Lineage Attributes")

[sources](/25.x/reference/api/catalog/lineage#attributes-of-objects-in-the-sources-array) Array of Object

Information about the sources the dataset uses. Each object in the sources array represents one source.

Example: [{"id": "21077e5d-fe6f-4a29-843f-58fa3acb17c2","path": ["Samples"],"tag": "Iz1v71CeTQY=","type": "CONTAINER","containerType": "SOURCE","createdAt": "2023-02-14T21:57:48.794Z"}]

---

[parents](/25.x/reference/api/catalog/lineage#attributes-of-objects-in-the-parents-array) Array of Object

Information about the parent objects for the dataset. Each object in the parents array represents one parent object. If a view represents a join of two other datsets, the parents array includes the two joined datasets. The parents array is empty if the dataset does not have parent objects.

Example: [{"id": "3419fa3a-b5b3-4438-b864-a27ec4e18752","path": ["Samples","samples.dremio.com","zips.json"],"tag": "MAntohVzwLw=","type": "DATASET","datasetType": "PROMOTED","createdAt": "2023-01-18T18:49:09.669Z"}]

---

[children](/25.x/reference/api/catalog/lineage#attributes-of-objects-in-the-children-array) Array of Object

Information about other catalog objects that reference the dataset. Each object in the children array represents one child object. The children array is empty if the dataset does not have child objects.

Example: [{"id": "170e211e-4235-4d8d-acb5-3d4dbfe99c75","path": ["@dremio","NYC\_zip"],"tag": "OWKrfpEKzW4=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-01-25T02:11:46.344Z"},{"id": "7f79c068-a3c3-4af7-8cd4-35896ef0a0e0","path": ["@dremio","Chicago\_zip"],"tag": "gsaDW5h4GCs=","type": "DATASET","datasetType": "VIRTUAL","createdAt": "2023-01-25T00:09:12.461Z"}]

#### Attributes of Objects in the `sources` Array[​](#attributes-of-objects-in-the-sources-array "Direct link to attributes-of-objects-in-the-sources-array")

id String (UUID)

Unique identifier of the source associated with the dataset.

Example: 21077e5d-fe6f-4a29-843f-58fa3acb17c2

---

path Array of String

Path of the source within Dremio, expressed as an array.

Example: ["Samples"]

---

tag String

Unique identifier of the version of the source. Dremio changes the tag whenever the source changes.

Example: Iz1v71CeTQY=

---

type String

Type of source. For sources in lineage responses, the type is `CONTAINER`.

Example: CONTAINER

---

containerType String

Type of container for the source.

Enum: HOME, SOURCE

Example: SOURCE

---

createdAt String

Date and time that the source was created, in UTC format. Not included for sources with the containerType `HOME`.

Example: 2022-02-14T21:57:48.794Z

#### Attributes of Objects in the `parents` Array[​](#attributes-of-objects-in-the-parents-array "Direct link to attributes-of-objects-in-the-parents-array")

id String (UUID)

Unique identifier of the parent object.

Example: 3419fa3a-b5b3-4438-b864-a27ec4e18752

---

path Array of String

Path of the parent object within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the parent object itself as the last item in the array.

Example: ["Samples","samples.dremio.com","zips.json"]

---

tag String

Unique identifier of the version of the parent object. Dremio changes the tag whenever the parent object changes.

Example: MAntohVzwLw=

---

type String

Type of parent object. For parent objects in lineage responses, the type is `DATASET`.

Example: DATASET

---

datasetType String

Dataset type for the parent object. If the parent object is a table, `PROMOTED`. If the parent object is a view, `VIRTUAL`.

Enum: PROMOTED, VIRTUAL

Example: PROMOTED

---

createdAt String

Date and time that the parent object was created, in UTC format.

Example: 2023-01-18T18:49:09.669Z

#### Attributes of Objects in the `children` Array[​](#attributes-of-objects-in-the-children-array "Direct link to attributes-of-objects-in-the-children-array")

id String (UUID)

Unique identifier of the child object.

Example: 170e211e-4235-4d8d-acb5-3d4dbfe99c75

---

path Array of String

Path of the child object within Dremio, expressed as an array. The path consists of the source or space, followed by any folder and subfolders, followed by the child object itself as the last item in the array.

Example: ["@dremio","NYC\_zip"]

---

tag String

Unique identifier of the version of the child object. Dremio changes the tag whenever the child object changes.

Example: OWKrfpEKzW4=

---

type String

Type of child object. For child objects in lineage responses, the type is `DATASET`.

Example: DATASET

---

datasetType String

Dataset type for the child object. For child objects in lineage responses, the datasetType is `VIRTUAL`.

Example: VIRTUAL

---

createdAt String

Date and time that the child object was created, in UTC format.

Example: 2023-01-25T02:11:46.344Z

## Retrieving Lineage Information About a Dataset[​](#retrieving-lineage-information-about-a-dataset "Direct link to Retrieving Lineage Information About a Dataset")

Retrieve lineage information about the specified dataset.

Method and URL

```
GET /api/v3/catalog/{id}/graph
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the dataset whose lineage you want to retrieve.

Example: d69b25a3-31c8-4d55-a7cc-dfee2290779b

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/d69b25a3-31c8-4d55-a7cc-dfee2290779b/graph' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "sources": [  
    {  
      "id": "21077e5d-fe6f-4a29-843f-58fa3acb17c2",  
      "path": [  
        "Samples"  
      ],  
      "tag": "Iz1v71CeTQY=",  
      "type": "CONTAINER",  
      "containerType": "SOURCE",  
      "createdAt": "2022-02-14T21:57:48.794Z"  
    }  
  ],  
  "parents": [  
    {  
      "id": "3419fa3a-b5b3-4438-b864-a27ec4e18752",  
      "path": [  
        "Samples",  
        "samples.dremio.com",  
        "zips.json"  
      ],  
      "tag": "MAntohVzwLw=",  
      "type": "DATASET",  
      "datasetType": "PROMOTED",  
      "createdAt": "2023-01-18T18:49:09.669Z"  
    }  
  ],  
  "children": [  
    {  
      "id": "170e211e-4235-4d8d-acb5-3d4dbfe99c75",  
      "path": [  
        "@dremio",  
        "NYC_zip"  
      ],  
      "tag": "OWKrfpEKzW4=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T02:11:46.344Z"  
    },  
    {  
      "id": "7f79c068-a3c3-4af7-8cd4-35896ef0a0e0",  
      "path": [  
        "@dremio",  
        "Chicago_zip"  
      ],  
      "tag": "gsaDW5h4GCs=",  
      "type": "DATASET",  
      "datasetType": "VIRTUAL",  
      "createdAt": "2023-01-25T00:09:12.461Z"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

View](/25.x/reference/api/catalog/view)[Next

Tag](/25.x/reference/api/catalog/tag)

* [Lineage Attributes](#lineage-attributes)
* [Retrieving Lineage Information About a Dataset](#retrieving-lineage-information-about-a-dataset)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/tag/

Version: 25.x

On this page

# Tag

Use the Catalog API to create, update, and retrieve [tags](/25.x/sonar/query-manage/managing-data/data-curation/#tags).

Tag Object

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023"  
  ],  
  "version": "VJ3ijXH4m6k="  
}
```

## Tag Attributes[​](#tag-attributes "Direct link to Tag Attributes")

tags Array of String

List of tags that apply to the dataset.

Example: ["NYC","taxi","2023"]

---

version String

Unique identifier of the set of tags. Dremio changes the version whenever any of the tags change and uses the version value to ensure that updates apply to the most recent version of the set of tags.

Example: VJ3ijXH4m6k=

## Creating Tags[​](#creating-tags "Direct link to Creating Tags")

Create one or more tags for the specified dataset.

Method and URL

```
POST /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset for which you want to add tags.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

tags Body   Array of String

List of tags to apply to the dataset. Tags are case-insensitive. Each tag can be listed only once for each dataset. Each tag can have a maximum of 128 characters. Tags cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: ["NYC","taxi","2023"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tags": ["NYC", "taxi", "2023"]  
}'
```

Example Response

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023"  
  ],  
  "version": "VM3ijXH4m6k="  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving Tags[​](#retrieving-tags "Direct link to Retrieving Tags")

Retrieve the tags applied to the specified dataset.

Method and URL

```
GET /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset whose tags you want to retrieve.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023"  
  ],  
  "version": "VM3ijXH4m6k="  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Updating Tags[​](#updating-tags "Direct link to Updating Tags")

Update the tags for the specified dataset.

Method and URL

```
POST /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset whose tags you want to update.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

tags Body   Array of String

List of tags to apply to the dataset. If you want to keep any of the existing tags, include them in the tags array. Tags are case-insensitive and must be distinct (in other words, list each tag only once for each dataset). Each tag may have a maximum of 128 characters. Tags cannot include the following special characters: `/`, `:`, `[`, or `]`.

Example: ["NYC","taxi","2023","archived"]

---

version Body   String

Unique identifier of the most recent set of tags. Dremio uses the version value to ensure that you are updating the most recent version of the tags.

Example: VM3ijXH4m6k=

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tags": ["NYC", "taxi", "2023", "archived"],  
  "version": "VM3ijXH4m6k="  
}'
```

Example Response

```
{  
  "tags": [  
    "NYC",  
    "taxi",  
    "2023",  
    "archived"  
  ],  
  "version": "yiZSE++9wiU="  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting Tags[​](#deleting-tags "Direct link to Deleting Tags")

Delete the tags for the specified dataset.

note

Deleting tags means sending an empty array to replace the existing tags with no tags. The tag object will still exist, but it will contain an empty `tags` array and no tags will appear for the dataset in the Dremio UI.

Method and URL

```
POST /api/v3/catalog/{dataset-id}/collaboration/tag
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

dataset-id Path   String (UUID)

Unique identifier of the dataset whose tags you want to remove.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

tags Body   Array of String

Empty array to represent deletion of all tags for the dataset.

Example: []

---

version Body   String

Unique identifier of the most recent set of tags. Dremio uses the version value to ensure that you are deleting tags from the most recent version.

Example: yiZSE++9wiU=

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/tag' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tags": [],  
  "version": "yiZSE++9wiU="  
}'
```

Example Response

```
{  
  "tags": [],  
  "version": "wuTAKuRcVas="  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

Was this page helpful?

[Previous

Lineage](/25.x/reference/api/catalog/lineage)[Next

Wiki](/25.x/reference/api/catalog/wiki)

* [Tag Attributes](#tag-attributes)
* [Creating Tags](#creating-tags)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving Tags](#retrieving-tags)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Updating Tags](#updating-tags)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Deleting Tags](#deleting-tags)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/wiki/

Version: 25.x

On this page

# Wiki

Use the Catalog API to create, update, and retrieve the [wiki](/25.x/sonar/query-manage/managing-data/data-curation/#wikis) for a source, space, or dataset.

Wiki Object

```
{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 4  
}
```

## Wiki Attributes[​](#wiki-attributes "Direct link to Wiki Attributes")

text String

Text displayed in the wiki, formatted with [GitHub-flavored Markdown](https://github.github.com/gfm/).

---

version Integer

Number for the most recent version of the wiki, starting with `0`. Dremio increments the value by 1 each time the wiki changes and uses the version value to ensure that updates apply to the most recent version of the wiki.

Example: 4

## Creating a Wiki[​](#creating-a-wiki "Direct link to Creating a Wiki")

Create a wiki for the specified source, space, or dataset.

Method and URL

```
POST /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset for which you want to add the wiki.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

text Body   String

Text to display in the wiki. Use [GitHub-flavored Markdown](https://github.github.com/gfm/) for wiki formatting and `\\n` for new lines and blank lines. Each wiki may have a maximum of 100,000 characters.

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."  
}'
```

Example Response

```
{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 0  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving a Wiki[​](#retrieving-a-wiki "Direct link to Retrieving a Wiki")

Retrieve the wiki for the specified source, space, or dataset.

Method and URL

```
GET /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset whose wiki you want to retrieve.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "text": "# Testspace Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is a bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 0  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

## Updating a Wiki[​](#updating-a-wiki "Direct link to Updating a Wiki")

Update the wiki for the specified source, space, or dataset.

Method and URL

```
POST /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset whose wiki you want to update.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

text Body   String

Text to display in the wiki, formatted with [GitHub-flavored Markdown](https://github.github.com/gfm/).

---

version Body   Integer

Number listed as the version value for the most recent existing wiki. Dremio uses the version value to ensure that you are updating the most recent version of the wiki.

Example: 0

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "text": "# New Title Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is an update to the bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 0  
}'
```

Example Response

```
{  
  "text": "# New Title Wiki\nThis is an example wiki for a catalog object in Dremio. Here is some text in **bold**. Here is some text in *italics*.\n\nHere is an example excerpt with quotation formatting:\n\n> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n\n## Heading Level 2\n\nHere is an update to the bulleted list:\n* An item in a bulleted list\n* A second item in a bulleted list\n* A third item in a bulleted list\n\n\n### Heading Level 3\n\nHere is a numbered list:\n1. An item in a numbered list\n1. A second item in a numbered list\n1. A third item in a numbered list\n\n\nHere is a sentence that includes an [external link to https://dremio.com](https://dremio.com).\n\nHere is an image:\n\n![](https://www.dremio.com/wp-content/uploads/2022/03/Dremio-logo.png)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",  
  "version": 1  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Deleting a Wiki[​](#deleting-a-wiki "Direct link to Deleting a Wiki")

Delete the wiki for the specified source, space, or dataset.

note

Deleting the wiki entails sending an empty string to replace the existing wiki with no wiki. The wiki object will still exist, but it will contain an empty `text` value and no wiki will appear for the source, space, or dataset in the Dremio UI.

Method and URL

```
POST /api/v3/catalog/{object-id}/collaboration/wiki
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

object-id Path   String (UUID)

Unique identifier of the source, space, or dataset whose wiki you want to delete.

Example: 1bcab7b3-ee82-44c1-abcc-e86d56078d4d

---

text Body   String

Empty string to represent deletion of the wiki.

Example: ""

---

version Body   Integer

Number listed as the version value for the most recent existing wiki. Dremio uses the version value to ensure that you are deleting the most recent version of the wiki.

Example: 1

Example Request

```
curl -X POST 'https://{hostname}/api/v3/catalog/1bcab7b3-ee82-44c1-abcc-e86d56078d4d/collaboration/wiki' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "text": "",  
  "version": 1  
}'
```

Example Response

```
{  
  "text": "",  
  "version": 2  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

Was this page helpful?

[Previous

Tag](/25.x/reference/api/catalog/tag)[Next

Privileges](/25.x/reference/api/catalog/privileges)

* [Wiki Attributes](#wiki-attributes)
* [Creating a Wiki](#creating-a-wiki)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving a Wiki](#retrieving-a-wiki)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Updating a Wiki](#updating-a-wiki)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Deleting a Wiki](#deleting-a-wiki)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/privileges/

Version: 25.x

On this page

# Privileges Enterprise

caution

The Catalog API Privileges endpoint is deprecated. We expect to remove it by July 2025.

In place of the Privileges endpoint, use the Catalog API [Grants](/25.x/reference/api/catalog/grants#retrieving-privileges-and-grantees-on-a-catalog-object) endpoint to retrieve privileges and grantees on specific catalog objects.

Use the Catalog API to retrieve information about available privileges on the different types of catalog objects.

Privileges Object

```
{  
  "availablePrivileges": [  
    {  
      "grantType": "SPACE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "ARP_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "EXTERNAL_QUERY",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER_IN_MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "PDS",  
      "privileges": [  
        "ALTER",  
        "DELETE",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE"  
      ]  
    },  
    {  
      "grantType": "VDS",  
      "privileges": [  
        "ALTER",  
        "MANAGE_GRANTS",  
        "SELECT"  
      ]  
    },  
    {  
      "grantType": "FUNCTION",  
      "privileges": [  
        "ALTER",  
        "EXECUTE",  
        "MANAGE_GRANTS",  
        "MODIFY"  
      ]  
    }  
  ]  
}
```

## Privileges Attributes[​](#privileges-attributes "Direct link to Privileges Attributes")

[availablePrivileges](/25.x/reference/api/catalog/privileges#attributes-of-objects-in-the-availableprivileges-array) Array of Object

Information about the grant types and privileges that are available to assign to users and roles for each type of object in the catalog. Each availablePrivileges object contains two attributes: grantType and privileges.

Example: [{"grantType": "SPACE","privileges": ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]},{"grantType": "SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]},{"grantType": "MUTABLE\_SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","CREATE\_TABLE","DELETE","DROP","INSERT","MANAGE\_GRANTS","MODIFY","SELECT","TRUNCATE","UPDATE","VIEW\_REFLECTION"]},{"grantType": "ARP\_SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","EXTERNAL\_QUERY","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]},{"grantType": "FOLDER\_IN\_MUTABLE\_SOURCE","privileges": ["ALTER","ALTER\_REFLECTION","CREATE\_TABLE","DELETE","DROP","INSERT","MANAGE\_GRANTS","SELECT","TRUNCATE","UPDATE","VIEW\_REFLECTION"]},{"grantType": "FOLDER","privileges": ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","SELECT","VIEW\_REFLECTION"]},{"grantType": "PDS","privileges": ["ALTER","DELETE","INSERT","MANAGE\_GRANTS","SELECT","TRUNCATE","UPDATE"]},{"grantType": "VDS","privileges": ["ALTER","MANAGE\_GRANTS","SELECT"]},{"grantType": "FUNCTION","privileges": ["ALTER","EXECUTE","MANAGE\_GRANTS","MODIFY"]}]

#### Attributes of Objects in the `availablePrivileges` Array[​](#attributes-of-objects-in-the-availableprivileges-array "Direct link to attributes-of-objects-in-the-availableprivileges-array")

grantType String

Type of the catalog object on which the listed privileges are available. `ARP_SOURCE` refers to relational-database sources.

Enum: SPACE, SOURCE, MUTABLE\_SOURCE, ARP\_SOURCE, FOLDER\_IN\_MUTABLE\_SOURCE, FOLDER, PDS, VDS, FUNCTION

Example: SPACE

---

privileges Array of String

List of available privileges on the type of the catalog object specified in grantType. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["ALTER","ALTER\_REFLECTION","MANAGE\_GRANTS","MODIFY","SELECT","VIEW\_REFLECTION"]

## Retrieving All Catalog Privileges[​](#retrieving-all-catalog-privileges "Direct link to Retrieving All Catalog Privileges")

Retrieve information about the available privileges on each type of object in the catalog.

caution

This endpoint is deprecated. We expect to remove it by July 2025.

In place of this endpoint, use the Catalog API [Grants](/25.x/reference/api/catalog/grants#retrieving-privileges-and-grantees-on-a-catalog-object) endpoint to retrieve privileges and grantees on specific catalog objects.

Method and URL

```
GET /api/v3/catalog/privileges
```

### Parameters[​](#parameters "Direct link to Parameters")

type Query   String   Optional

Type of the catalog object whose available privileges you want to retrieve. For more information, read [type Query Parameter](/25.x/reference/api/#type-query-parameter).

Enum: SPACE, SOURCE, MUTABLE\_SOURCE, ARP\_SOURCE, FOLDER\_IN\_MUTABLE\_SOURCE, FOLDER, PDS, VDS, FUNCTION

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/privileges' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "availablePrivileges": [  
    {  
      "grantType": "SPACE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "ARP_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "EXTERNAL_QUERY",  
        "MANAGE_GRANTS",  
        "MODIFY",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER_IN_MUTABLE_SOURCE",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "CREATE_TABLE",  
        "DELETE",  
        "DROP",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "FOLDER",  
      "privileges": [  
        "ALTER",  
        "ALTER_REFLECTION",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "VIEW_REFLECTION"  
      ]  
    },  
    {  
      "grantType": "PDS",  
      "privileges": [  
        "ALTER",  
        "DELETE",  
        "INSERT",  
        "MANAGE_GRANTS",  
        "SELECT",  
        "TRUNCATE",  
        "UPDATE"  
      ]  
    },  
    {  
      "grantType": "VDS",  
      "privileges": [  
        "ALTER",  
        "MANAGE_GRANTS",  
        "SELECT"  
      ]  
    },  
    {  
      "grantType": "FUNCTION",  
      "privileges": [  
        "ALTER",  
        "EXECUTE",  
        "MANAGE_GRANTS",  
        "MODIFY"  
      ]  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Wiki](/25.x/reference/api/catalog/wiki)[Next

Grants](/25.x/reference/api/catalog/grants)

* [Privileges Attributes](#privileges-attributes)
* [Retrieving All Catalog Privileges](#retrieving-all-catalog-privileges)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/catalog/grants/

Version: 25.x

On this page

# Grants Enterprise

Use the Catalog API to grant user and role privileges on specific catalog objects.

Grants Object

```
{  
  "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
  "availablePrivileges": [  
    "ALTER",  
    "DELETE",  
    "INSERT",  
    "MANAGE_GRANTS",  
    "SELECT",  
    "TRUNCATE",  
    "UPDATE"  
  ],  
  "grants": [  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT",  
        "MANAGE_GRANTS"  
      ],  
      "granteeType": "USER",  
      "id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0",  
      "name": "jeansmith",  
      "firstName": "Jean",  
      "lastName": "Smith",  
      "email": "jean_smith@example.com"  
    },  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT"  
      ],  
      "granteeType": "ROLE",  
      "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
      "name": "examplerole"  
    }  
  ]  
}
```

## Grants Attributes[​](#grants-attributes "Direct link to Grants Attributes")

id String

Unique identifier of the Dremio catalog object.

Example: 7f1c4660-cd7b-40d0-97d1-b8a6f431cbda

---

availablePrivileges Array of String

List of available privileges on the catalog object.

Example: ["ALTER","DELETE","INSERT","MANAGE\_GRANTS","SELECT","TRUNCATE","UPDATE"]

---

[grants](/25.x/reference/api/catalog/grants#attributes-of-objects-in-the-grants-array) Array of Object

Information about the privileges and grantees for the catalog object. If the grants array is empty, there are no explicit grants for the object.

note

An empty grants array does not mean no users have access to the object at all. For example, admin users implicitly have all privileges on all catalog objects, owners implicitly have all privileges on everything they own, and children objects inherit the grants for their parent objects.

Example: [{"privileges": ["ALTER","SELECT","MANAGE\_GRANTS"],"granteeType": "USER","id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0","name": "jeansmith","firstName": "Jean","lastName": "Smith","email": "[jean\_smith@example.com](mailto:jean_smith@example.com)"},{"privileges": ["ALTER","SELECT"],"granteeType": "ROLE","id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889","name": "examplerole"}]

#### Attributes of Objects in the `grants` Array[​](#attributes-of-objects-in-the-grants-array "Direct link to attributes-of-objects-in-the-grants-array")

privileges String

List of privileges granted to the user or role. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["ALTER","SELECT","MANAGE\_GRANTS"]

---

granteeType String

Type of grantee.

Enum: USER, ROLE

Example: USER

---

id String

Unique identifier of the user or role.

Example: 27937a63-e7e5-4478-8d3c-4ad3f20d43c0

---

name String

Name of the user or role.

Example: jeansmith

---

firstName String

For users, the user's first name. Not included for roles.

Example: Jean

---

lastName String

For users, the user's last name. Not included for roles.

Example: Smith

---

email String

For users, the user's email address. Not included for roles.

Example: [jean\_smith@example.com](mailto:jean_smith@example.com)

## Creating or Updating Privilege Grants on a Catalog Object[​](#creating-or-updating-privilege-grants-on-a-catalog-object "Direct link to Creating or Updating Privilege Grants on a Catalog Object")

Create or update the privileges granted to users and roles on the specified catalog object.

note

You must have the [MANAGE GRANTS privilege](/25.x/security/rbac/privileges/#dataset-privileges) to create or update privilege grants on catalog objects.

Method and URL

```
PUT /api/v3/catalog/{id}/grants
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the Dremio catalog object.

Example: 7f1c4660-cd7b-40d0-97d1-b8a6f431cbda

---

[grants](/25.x/reference/api/catalog/grants#parameters-of-objects-in-the-grants-array) Body   Array of Object

Array of objects that specify which users and roles should have privileges on the catalog object, as well as each user's and role's specific privileges. May include objects for users, roles, or both.

Example: [{"privileges": ["ALTER","SELECT","MANAGE\_GRANTS"],"granteeType": "USER","id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0"},{"privileges": ["SELECT","ALTER"],"granteeType": "ROLE","id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889"}]

#### Parameters of Objects in the `grants` Array[​](#parameters-of-objects-in-the-grants-array "Direct link to parameters-of-objects-in-the-grants-array")

privileges Body   Array of String

List of privileges to grant to the user or role. Use the [Privileges](/25.x/reference/api/catalog/privileges#retrieving-all-catalog-privileges) endpoint to retrieve a list of available privileges on the catalog object type. For more information, read [Privileges](/25.x/security/rbac/privileges).

Example: ["ALTER","SELECT","MANAGE\_GRANTS"]

---

granteeType Body   String

Type of grantee.

Enum: USER, ROLE

Example: USER

---

id Body   String

Unique identifier of the user or role.

Example: 27937a63-e7e5-4478-8d3c-4ad3f20d43c0

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/catalog/7f1c4660-cd7b-40d0-97d1-b8a6f431cbda/grants' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "grants": [  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT",  
        "MANAGE_GRANTS"  
      ],  
      "granteeType": "USER",  
      "id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0"  
    },  
    {  
      "privileges": [  
        "SELECT",  
        "ALTER"  
      ],  
      "granteeType": "ROLE",  
      "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889"  
    }  
  ]  
}'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

403   Forbidden

404   Not Found

## Retrieving Privileges and Grantees on a Catalog Object[​](#retrieving-privileges-and-grantees-on-a-catalog-object "Direct link to Retrieving Privileges and Grantees on a Catalog Object")

Retrieve information about the privileges granted to users and roles on the specified catalog object.

note

Use this endpoint in place of the Catalog API [Privileges](/25.x/reference/api/catalog/privileges) endpoint, which is deprecated. We expect to remove the Privileges endpoint by July 2025.

You must have the [MANAGE GRANTS privilege](/25.x/security/rbac/privileges/#dataset-privileges) to retrieve privilege grants on catalog objects.

Method and URL

```
GET /api/v3/catalog/{id}/grants
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the object whose privilege grants you want to retrieve.

Example: 7f1c4660-cd7b-40d0-97d1-b8a6f431cbda

Example Request

```
curl -X GET 'https://{hostname}/api/v3/catalog/7f1c4660-cd7b-40d0-97d1-b8a6f431cbda/grants' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "7f1c4660-cd7b-40d0-97d1-b8a6f431cbda",  
  "availablePrivileges": [  
    "ALTER",  
    "DELETE",  
    "INSERT",  
    "MANAGE_GRANTS",  
    "SELECT",  
    "TRUNCATE",  
    "UPDATE"  
  ],  
  "grants": [  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT",  
        "MANAGE_GRANTS"  
      ],  
      "granteeType": "USER",  
      "id": "27937a63-e7e5-4478-8d3c-4ad3f20d43c0",  
      "name": "jeansmith",  
      "firstName": "Jean",  
      "lastName": "Smith",  
      "email": "jean_smith@example.com"  
    },  
    {  
      "privileges": [  
        "ALTER",  
        "SELECT"  
      ],  
      "granteeType": "ROLE",  
      "id": "0f2d94e0-bb5e-4c03-8c6f-62d379d10889",  
      "name": "examplerole"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Privileges](/25.x/reference/api/catalog/privileges)[Next

Dataset](/25.x/reference/api/datasets/)

* [Grants Attributes](#grants-attributes)
* [Creating or Updating Privilege Grants on a Catalog Object](#creating-or-updating-privilege-grants-on-a-catalog-object)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving Privileges and Grantees on a Catalog Object](#retrieving-privileges-and-grantees-on-a-catalog-object)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)

---

# Source: https://docs.dremio.com/25.x/reference/api/job/job-results

Version: 25.x

On this page

# Job Results

Use the Job API to retrieve results for a specific job.

Job Results Object

```
{  
  "rowCount": 11,  
  "schema": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ],  
  "rows": [  
    {  
      "pickup_datetime": "2013-02-10 20:00:00.000",  
      "passenger_count": 9,  
      "trip_distance_mi": 3,  
      "fare_amount": 10,  
      "tip_amount": 3,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:15:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.26,  
      "fare_amount": 7.5,  
      "tip_amount": 0,  
      "total_amount": 8  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:40:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.73,  
      "fare_amount": 5,  
      "tip_amount": 1.2,  
      "total_amount": 7.7  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:03:00.000",  
      "passenger_count": 2,  
      "trip_distance_mi": 9.23,  
      "fare_amount": 27.5,  
      "tip_amount": 5,  
      "total_amount": 38.33  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:24:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.27,  
      "fare_amount": 12,  
      "tip_amount": 0,  
      "total_amount": 13.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:17:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.71,  
      "fare_amount": 5,  
      "tip_amount": 0,  
      "total_amount": 5.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:11:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.52,  
      "fare_amount": 10.5,  
      "tip_amount": 3.15,  
      "total_amount": 14.15  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:41:00.000",  
      "passenger_count": 5,  
      "trip_distance_mi": 1.01,  
      "fare_amount": 6,  
      "tip_amount": 1.1,  
      "total_amount": 8.6  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:37:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.25,  
      "fare_amount": 8.5,  
      "tip_amount": 0,  
      "total_amount": 10  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:39:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.04,  
      "fare_amount": 10,  
      "tip_amount": 1.5,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:02:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 11.73,  
      "fare_amount": 32.5,  
      "tip_amount": 8.12,  
      "total_amount": 41.12  
    }  
  ]  
}
```

## Job Results Attributes[​](#job-results-attributes "Direct link to Job Results Attributes")

rowCount Integer

Number of rows the job returned.

Example: 11

---

schema Array of Object

Array of schema definitions for the data the job returned.

---

rows Array of Object

Array of the data the job returned for each row of results.

## Retrieving Job Results[​](#retrieving-job-results "Direct link to Retrieving Job Results")

Method and URL

```
GET /api/v3/job/{id}/results
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the job to retrieve. Get the job ID from responses to [SQL API](/25.x/reference/api/sql/) requests.

Example: 6j6c34cf-9drf-b07a-5ab7-abea69a66d00

---

limit Query   Integer   Optional

Number of rows to retrieve. Maximum valid value is `500`. Default is `100`. Use with the `offset` query parameter to paginate and retrieve more than the first 500 results. Read [Limit and Offset Query Parameters](/25.x/reference/api/#limit-and-offset-query-parameters) for usage examples.

---

offset Query   Integer   Optional

Number of rows to skip for pagination. Default is `0`. Read [Limit and Offset Query Parameters](/25.x/reference/api/#limit-and-offset-query-parameters) for usage examples.

  
Example Request

```
curl -X GET 'https://{hostname}/api/v3/job/6j6c34cf-9drf-b07a-5ab7-abea69a66d00/results' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response for a COMPLETED Job

```
{  
  "rowCount": 11,  
  "schema": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ],  
  "rows": [  
    {  
      "pickup_datetime": "2013-02-10 20:00:00.000",  
      "passenger_count": 9,  
      "trip_distance_mi": 3,  
      "fare_amount": 10,  
      "tip_amount": 3,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:15:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.26,  
      "fare_amount": 7.5,  
      "tip_amount": 0,  
      "total_amount": 8  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:40:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.73,  
      "fare_amount": 5,  
      "tip_amount": 1.2,  
      "total_amount": 7.7  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:03:00.000",  
      "passenger_count": 2,  
      "trip_distance_mi": 9.23,  
      "fare_amount": 27.5,  
      "tip_amount": 5,  
      "total_amount": 38.33  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:24:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.27,  
      "fare_amount": 12,  
      "tip_amount": 0,  
      "total_amount": 13.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:17:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.71,  
      "fare_amount": 5,  
      "tip_amount": 0,  
      "total_amount": 5.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:11:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.52,  
      "fare_amount": 10.5,  
      "tip_amount": 3.15,  
      "total_amount": 14.15  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:41:00.000",  
      "passenger_count": 5,  
      "trip_distance_mi": 1.01,  
      "fare_amount": 6,  
      "tip_amount": 1.1,  
      "total_amount": 8.6  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:37:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.25,  
      "fare_amount": 8.5,  
      "tip_amount": 0,  
      "total_amount": 10  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:39:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.04,  
      "fare_amount": 10,  
      "tip_amount": 1.5,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:02:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 11.73,  
      "fare_amount": 32.5,  
      "tip_amount": 8.12,  
      "total_amount": 41.12  
    }  
  ]  
}
```

For jobs with a jobState value other than `COMPLETED`, the response includes an error message instead of the job results object. The job's status is listed inside brackets in the error message (`CANCELED`, `FAILED`, or `RUNNING`):

Example Response for a FAILED Job

```
{  
    "errorMessage": "Can not fetch details for a job that is in [FAILED] state.",  
    "moreInfo": ""  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Job](/25.x/reference/api/job/)[Next

LDAP User Cache](/25.x/reference/api/ldap-authorization)

* [Job Results Attributes](#job-results-attributes)
* [Retrieving Job Results](#retrieving-job-results)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/job/job-results/

Version: 25.x

On this page

# Job Results

Use the Job API to retrieve results for a specific job.

Job Results Object

```
{  
  "rowCount": 11,  
  "schema": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ],  
  "rows": [  
    {  
      "pickup_datetime": "2013-02-10 20:00:00.000",  
      "passenger_count": 9,  
      "trip_distance_mi": 3,  
      "fare_amount": 10,  
      "tip_amount": 3,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:15:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.26,  
      "fare_amount": 7.5,  
      "tip_amount": 0,  
      "total_amount": 8  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:40:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.73,  
      "fare_amount": 5,  
      "tip_amount": 1.2,  
      "total_amount": 7.7  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:03:00.000",  
      "passenger_count": 2,  
      "trip_distance_mi": 9.23,  
      "fare_amount": 27.5,  
      "tip_amount": 5,  
      "total_amount": 38.33  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:24:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.27,  
      "fare_amount": 12,  
      "tip_amount": 0,  
      "total_amount": 13.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:17:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.71,  
      "fare_amount": 5,  
      "tip_amount": 0,  
      "total_amount": 5.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:11:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.52,  
      "fare_amount": 10.5,  
      "tip_amount": 3.15,  
      "total_amount": 14.15  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:41:00.000",  
      "passenger_count": 5,  
      "trip_distance_mi": 1.01,  
      "fare_amount": 6,  
      "tip_amount": 1.1,  
      "total_amount": 8.6  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:37:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.25,  
      "fare_amount": 8.5,  
      "tip_amount": 0,  
      "total_amount": 10  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:39:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.04,  
      "fare_amount": 10,  
      "tip_amount": 1.5,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:02:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 11.73,  
      "fare_amount": 32.5,  
      "tip_amount": 8.12,  
      "total_amount": 41.12  
    }  
  ]  
}
```

## Job Results Attributes[​](#job-results-attributes "Direct link to Job Results Attributes")

rowCount Integer

Number of rows the job returned.

Example: 11

---

schema Array of Object

Array of schema definitions for the data the job returned.

---

rows Array of Object

Array of the data the job returned for each row of results.

## Retrieving Job Results[​](#retrieving-job-results "Direct link to Retrieving Job Results")

Method and URL

```
GET /api/v3/job/{id}/results
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the job to retrieve. Get the job ID from responses to [SQL API](/25.x/reference/api/sql/) requests.

Example: 6j6c34cf-9drf-b07a-5ab7-abea69a66d00

---

limit Query   Integer   Optional

Number of rows to retrieve. Maximum valid value is `500`. Default is `100`. Use with the `offset` query parameter to paginate and retrieve more than the first 500 results. Read [Limit and Offset Query Parameters](/25.x/reference/api/#limit-and-offset-query-parameters) for usage examples.

---

offset Query   Integer   Optional

Number of rows to skip for pagination. Default is `0`. Read [Limit and Offset Query Parameters](/25.x/reference/api/#limit-and-offset-query-parameters) for usage examples.

  
Example Request

```
curl -X GET 'https://{hostname}/api/v3/job/6j6c34cf-9drf-b07a-5ab7-abea69a66d00/results' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response for a COMPLETED Job

```
{  
  "rowCount": 11,  
  "schema": [  
    {  
      "name": "pickup_datetime",  
      "type": {  
        "name": "TIMESTAMP"  
      }  
    },  
    {  
      "name": "passenger_count",  
      "type": {  
        "name": "BIGINT"  
      }  
    },  
    {  
      "name": "trip_distance_mi",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "fare_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "tip_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    },  
    {  
      "name": "total_amount",  
      "type": {  
        "name": "DOUBLE"  
      }  
    }  
  ],  
  "rows": [  
    {  
      "pickup_datetime": "2013-02-10 20:00:00.000",  
      "passenger_count": 9,  
      "trip_distance_mi": 3,  
      "fare_amount": 10,  
      "tip_amount": 3,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:15:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.26,  
      "fare_amount": 7.5,  
      "tip_amount": 0,  
      "total_amount": 8  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:40:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.73,  
      "fare_amount": 5,  
      "tip_amount": 1.2,  
      "total_amount": 7.7  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:03:00.000",  
      "passenger_count": 2,  
      "trip_distance_mi": 9.23,  
      "fare_amount": 27.5,  
      "tip_amount": 5,  
      "total_amount": 38.33  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:24:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.27,  
      "fare_amount": 12,  
      "tip_amount": 0,  
      "total_amount": 13.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:17:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 0.71,  
      "fare_amount": 5,  
      "tip_amount": 0,  
      "total_amount": 5.5  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:11:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.52,  
      "fare_amount": 10.5,  
      "tip_amount": 3.15,  
      "total_amount": 14.15  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:41:00.000",  
      "passenger_count": 5,  
      "trip_distance_mi": 1.01,  
      "fare_amount": 6,  
      "tip_amount": 1.1,  
      "total_amount": 8.6  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:37:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 1.25,  
      "fare_amount": 8.5,  
      "tip_amount": 0,  
      "total_amount": 10  
    },  
    {  
      "pickup_datetime": "2013-05-31 16:39:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 2.04,  
      "fare_amount": 10,  
      "tip_amount": 1.5,  
      "total_amount": 13  
    },  
    {  
      "pickup_datetime": "2013-05-27 19:02:00.000",  
      "passenger_count": 1,  
      "trip_distance_mi": 11.73,  
      "fare_amount": 32.5,  
      "tip_amount": 8.12,  
      "total_amount": 41.12  
    }  
  ]  
}
```

For jobs with a jobState value other than `COMPLETED`, the response includes an error message instead of the job results object. The job's status is listed inside brackets in the error message (`CANCELED`, `FAILED`, or `RUNNING`):

Example Response for a FAILED Job

```
{  
    "errorMessage": "Can not fetch details for a job that is in [FAILED] state.",  
    "moreInfo": ""  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

403   Forbidden

404   Not Found

Was this page helpful?

[Previous

Job](/25.x/reference/api/job/)[Next

LDAP User Cache](/25.x/reference/api/ldap-authorization)

* [Job Results Attributes](#job-results-attributes)
* [Retrieving Job Results](#retrieving-job-results)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/reflections/reflection-recommendations

Version: 25.x

On this page

# Recommendations

Use the Recommendations API to get job-based recommendations and get and create usage-based Reflections that can accelerate your queries.

Getting **job-based recommendations** requires making the following two API requests:

1. [Submit the job IDs of jobs that have run SQL queries](/25.x/reference/api/reflections/reflection-recommendations#submitting-job-ids). These are job IDs of the queries for which you want to retrieve recommendations in further requests. This request returns the job ID to use in the second request.
2. [Retrieve job-based recommendations for Reflections](/25.x/reference/api/reflections/reflection-recommendations#retrieving-job-based-recommendations) that can accelerate your queries. Use the job ID that was returned in your first request to make the request for recommendations.

Creating Reflections from **usage-based recommendations** requires making the following two API requests:

1. [Retrieve usage-based recommendations](/25.x/reference/api/reflections/reflection-recommendations#retrieving-usage-based-recommendations) for Reflections. This request returns the parameters to use in the body of the second request.
2. [Create Reflections from usage-based recommendations](/25.x/reference/api/reflections/reflection-recommendations#creating-reflections-from-usage-based-recommendations) that can accelerate your queries from the usage-based recommendations. Use the recommendation ID and Reflection request body that were returned in your first request to create the Reflections.

note

Dremio supports creating only raw Reflections from usage-based recommendations.

caution

The [`POST /api/v3/reflection/recommendations` endpoint](/25.x/reference/api/reflections/reflection-recommendations#requesting-recommendations-deprecated) is deprecated. In its place, use the job-based and usage-based endpoints described on this page to retrieve and refresh Reflection recommendations.

Recommendation Object (Raw Reflection)

```
{  
  "data": [  
    {  
      "viewRequestBody": {  
        "entityType": "dataset",  
        "type": "VIRTUAL_DATASET",  
        "path": [  
          "azure_3",  
          "table_2"  
        ],  
        "sql": "--Default Raw Reflection"  
      },  
      "viewRequestEndpoint": "POST {hostname}/api/v3/catalog",  
      "reflectionRequestBody": {  
        "type": "RAW",  
        "name": "raw_47f54460-543f-430f-a9e5-ca71d246265e",  
        "datasetId": "45b9d98b-b0dc-4dd2-a271-d971ae998c0c",  
        "enabled": true,  
        "arrowCachingEnabled": false,  
        "dimensionFields": [],  
        "measureFields": [],  
        "displayFields": [  
          {  
            "name": "passenger_count"  
          },  
          {  
            "name": "EXPR$1"  
          }  
        ],  
        "entityType": "reflection"  
      },  
      "reflectionRequestEndpoint": "POST {hostname}/api/v3/reflection",  
      "jobIds": [  
        "13ffb629-9f0e-4265-97df-99bf0d425813"  
      ],  
      "jobCount": 1,  
      "recommendationId": "9be8a451-4190-4618-a72e-9932f790c744",  
      "reflectionScore": 50.67,  
      "avgImprovementFactor": 10.43,  
      "avgImprovementMs": 7196  
    }  
  ],  
  "canAlterReflections": true  
}
```

Recommendation Object (Aggregation Reflection)

```
{  
  "data": [  
    {  
      "viewRequestBody": {  
        "entityType": "dataset",  
        "type": "VIRTUAL_DATASET",  
        "path": [  
          "recommended_view",  
          "view_1"  
        ],  
        "sql": "SELECT * FROM Samples.samples.dremio.com.\"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC"  
      },  
      "viewRequestEndpoint": "POST {hostname}/api/v3/catalog",  
      "reflectionRequestBody": {  
        "type": "AGGREGATION",  
        "name": "agg_0e0c4ab9-def7-48da-81f1-ca8c1da11ed4",  
        "datasetId": "2df93b5a-eb46-4687-8460-b61e471d20ef",  
        "enabled": true,  
        "arrowCachingEnabled": false,  
        "dimensionFields": [  
          {  
            "name": "passenger_count",  
            "granularity": "DATE"  
          }  
        ],  
        "measureFields": [  
          {  
            "name": "fare_amount",  
            "measureTypeList": [  
              "SUM",  
              "COUNT"  
            ]  
          }  
        ],  
        "displayFields": [],  
        "entityType": "reflection"  
      },  
      "reflectionRequestEndpoint": "POST {hostname}/api/v3/reflection",  
      "jobIds": [  
        "1ded81f8-4d06-4d09-8163-9e2517027d8d"  
      ],  
      "jobCount": 1,  
      "recommendationId": "1855d2dd-4106-4359-a97a-e08a916096e6",  
      "reflectionScore": 60.12,  
      "avgImprovementFactor": 8.39,  
      "avgImprovementMs": 5400  
    }  
  ],  
  "canAlterReflections": true  
}
```

## Recommendation Attributes[​](#recommendation-attributes "Direct link to Recommendation Attributes")

[data](/25.x/reference/api/reflections/reflection-recommendations/#attributes-of-objects-in-the-data-array) Array of Object

List of recommended Reflection objects for the submitted job IDs.

---

canAlterReflections Boolean

If the columns in the recommended Reflection can be edited, added, and removed, `true`. Otherwise, `false`.

Example: true

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

[viewRequestBody](/25.x/reference/api/reflections/reflection-recommendations/#attributes-of-the-viewrequestbody-object) Object

The fields to include in a request to the [Catalog API](/25.x/reference/api/catalog/view#creating-a-view) to create the view on which to define the recommended Reflection.

---

viewRequestEndpoint String

The endpoint to use when submitting a request to the [Catalog API](/25.x/reference/api/catalog/view#creating-a-view) to create the view on which to define the recommended Reflection.

---

[reflectionRequestBody](/25.x/reference/api/reflections/reflection-recommendations/#attributes-of-the-reflectionrequestbody-object) Object

The fields to include in a request to the [Reflection API](/25.x/reference/api/reflections/#creating-a-reflection) to create the recommended Reflection.

---

reflectionRequestEndpoint String

The endpoint to use when submitting the request to the [Reflection API](/25.x/reference/api/reflections/#creating-a-reflection) to create the recommended Reflection.

---

jobIds Array of String

The job IDs of the queries for which the Reflection recommendations are given.

Example: ["13ffb629-9f0e-4265-97df-99bf0d425813"]

---

jobCount Array of String

The number of jobs for which Reflection recommendations are given.

Example: 1

---

recommendationId Array of String

The ID of the recommended Reflection.

Example: ["9be8a451-4190-4618-a72e-9932f790c744"]

---

reflectionScore Double

Score for the recommended Reflection's quality, on a scale of 0 (worst) to 100 (best). The reflectionScore value considers the recommended Reflection's anticipated quality compared to existing Reflections and other recommended Reflections, as well as the likely improvement in query run times if the recommended Reflection is implemented.

Example: 50.67

---

avgImprovementFactor Double

The likely average multiplicative rate of improvement for each query if you implement the recommended Reflection. For example, if the avgImprovementFactor value is 2.34, implementing the recommended Reflection is likely to speed up each query by 2.34 times, on average.

Example: 10.43

---

avgImprovementMs Double

The likely average improvement, in milliseconds, for each query if you implement the recommended Reflection. For example, if the avgImprovementMs value is 5400, implementing the recommended Reflection is likely to save an average of 5400 milliseconds for each query that uses the Reflection.

Example: 7196

#### Attributes of the `viewRequestBody` Object[​](#attributes-of-the-viewrequestbody-object "Direct link to attributes-of-the-viewrequestbody-object")

entityType String

Type of catalog entity. For views, the entityType is `dataset`.

---

type String

Type of dataset. For views, the type is `VIRTUAL_DATASET`.

---

path Array of String

Path to the location where the view should be created within Dremio, expressed in an array. The path lists each level of hierarchy in order, from outer to inner: Arctic source or catalog first, then folder and subfolders, then a name for the view itself as the last item in the array. Views can only be created in Arctic sources and the project's Arctic catalog.

Example: ["azure\_3","table\_2"]

---

sql String

For aggregation Reflections, the SQL query to use to create the view. For default raw Reflections, the sql value `--Default Raw Reflection`; creating a view is unnecessary because raw recommendations are given only for existing views.

#### Attributes of the `reflectionRequestBody` Object[​](#attributes-of-the-reflectionrequestbody-object "Direct link to attributes-of-the-reflectionrequestbody-object")

type String

Reflection type. For details, read [Types of Reflections](/25.x/sonar/reflections/types-and-benefits).

Enum: RAW, AGGREGATION

Example: AGGREGATION

---

name String

User-provided name for the Reflection. For Reflections created in the Dremio console, if the user did not provide a name, the default values are `Raw Reflection` and `Aggregation Reflection` (automatically assigned based on the Reflection type).

Example: raw\_47f54460-543f-430f-a9e5-ca71d246265e

---

datasetId String

Unique identifier for the anchor dataset to associate with the Reflection.

Example: 45b9d98b-b0dc-4dd2-a271-d971ae998c0c

---

enabled Boolean

If the Reflection is available for accelerating queries, `true`. Otherwise, `false`.

Example: true

---

arrowCachingEnabled Boolean

If Dremio converts data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, `true`. Otherwise, `false`.

Example: false

---

dimensionFields Array of Object

Information about the dimension fields from the anchor dataset used in the Reflection. Dimension fields are the fields you expect to group by when analyzing data. Valid only for aggregation Reflections. For raw Reflections or if the anchor dataset does not include any dimension fields, the dimensionFields value is an empty array. For aggregation Reflections, if the anchor dataset includes dimension fields, each object in the dimensionFields array contains two attributes: name and granularity.

Example: [{"name": "pickup\_date","granularity": "DATE"},{"name": "pickup\_datetime","granularity": "DATE"},{"name": "dropoff\_date","granularity": "DATE"},{"name": "dropoff\_datetime","granularity": "DATE"},{"name": "passenger\_count","granularity": "DATE"},{"name": "total\_amount","granularity": "DATE"}]

---

measureFields Array of Object

Information about the measure fields from the anchor dataset used in the Reflection. Measure fields are the fields you expect to use for calculations when analyzing the data. Valid only for aggregation Reflections. For raw Reflections or if the anchor dataset does not include any measure fields, the measureFields value is an empty array. For aggregation Reflections, if the anchor dataset includes measure fields, each object in the measureFields array contains two attributes: name and measureTypeList.

Example: [{"name": "passenger\_count","measureTypeList": ["SUM,"COUNT"]},{"name": "trip\_distance\_mi","measureTypeList": ["SUM","COUNT"]},{"name": "fare\_amount","measureTypeList": ["SUM","COUNT"]},{"name": "surcharge","measureTypeList": ["SUM","COUNT"]},{"name": "tip\_amount","measureTypeList": ["SUM","COUNT"]},{"name": "total\_amount","measureTypeList": ["SUM","COUNT"]}]

---

displayFields Array of Object

Information about the fields displayed from the anchor dataset. Valid only for raw Reflections. For aggregation Reflections or if the anchor dataset does not include any display fields, the value is an empty array. For raw Reflections, if the anchor dataset includes display fields, each object in the displayFields array contains one attribute: name.

Example: [{"name": "passenger\_count"},{"name": "EXPR$1"}]

---

entityType String

Type of entity. For Reflection objects, the entityType is `reflection`.

## Submitting Job IDs[​](#submitting-job-ids "Direct link to Submitting Job IDs")

Submit the job IDs of queries for which you want to request Reflection recommendations.

The response includes objects that contain an id attribute and value for each job ID you submit. Use these id values to [retrieve recommendations for Reflections](/25.x/reference/api/reflections/reflection-recommendations#retrieving-job-based-recommendations) to accelerate the queries.

Method and URL

```
POST /api/v3/reflection/recommendations/job-based/
```

### Parameters[​](#parameters "Direct link to Parameters")

jobIds Body   Array of String

The job IDs of the queries for which you want to request Reflection recommendations. To get the job IDs, use the [SQL API](/25.x/reference/api/sql/) or find them on the [Jobs page](/25.x/sonar/query-manage/querying-data/jobs/) in the Dremio console. Use a comma-separated list to submit multiple job IDs.

Example: ["a7efcd50-791a-48e8-bb05-391b4411e66b"]

Example Request

```
curl -X POST 'https://{hostname}/api/v3/reflection/recommendations/job-based/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
    "jobIds": ["a7efcd50-791a-48e8-bb05-391b4411e66b","c2485882-e6b7-4aa8-af5b-a825d2870589"]  
}'
```

Example Response

```
{  
  "id": "13ffb629-9f0e-4265-97df-99bf0d425813"  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

405   Method Not Allowed

500   Internal Server Error

## Retrieving Job-Based Recommendations[​](#retrieving-job-based-recommendations "Direct link to Retrieving Job-Based Recommendations")

Retrieve job-based recommended Reflections to accelerate the queries whose [job IDs you submitted](/25.x/reference/api/reflections/reflection-recommendations#submitting-job-ids).

* For default raw Reflections, each recommendation comprises the path to the view on which to define the Reflection and the parameters to use in a request to create the Reflection.
* For aggregation Reflections, each recommendation comprises the parameters to use in a request to create a view on which to define the recommended Reflection and the parameters to use in a request to create the Reflection.

After you retrieve the recommended Reflections for your queries, use the [Catalog API](/current/reference/api/catalog/view#creating-a-view) to create the recommended views. Then, use the [Reflection API](/current/reference/api/reflections/#creating-a-reflection) to create the desired Reflections.

note

Before submitting Catalog API requests to create the recommended views for aggregation Reflections, create a folder named `recommended_view`. In your Catalog API requests, the `path` parameter must include the full path to the `recommended_view` folder. If you prefer to use a different folder name, replace `recommended_view` with your folder name in the `path` parameter when making the Catalog API request.

Method and URL

```
GET /api/v3/reflection/recommendations/job-based/{id}/results/
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String

The id value returned in the response to your request to [submit the job ID or IDs](/25.x/reference/api/reflections/reflection-recommendations#submitting-job-ids) of the queries for which you want to retrieve recommended Reflections.

Example: 13ffb629-9f0e-4265-97df-99bf0d425813

Example Request

```
curl -X GET 'https://{hostname}/api/v3/reflection/recommendations/job-based/13ffb629-9f0e-4265-97df-99bf0d425813/results/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "viewRequestBody": {  
        "entityType": "dataset",  
        "type": "VIRTUAL_DATASET",  
        "path": [  
          "azure_3",  
          "table_2"  
        ],  
        "sql": "--Default Raw Reflection"  
      },  
      "viewRequestEndpoint": "{hostname}/api/v3/catalog",  
      "reflectionRequestBody": {  
        "type": "RAW",  
        "name": "raw_47f54460-543f-430f-a9e5-ca71d246265e",  
        "datasetId": "45b9d98b-b0dc-4dd2-a271-d971ae998c0c",  
        "enabled": true,  
        "arrowCachingEnabled": false,  
        "dimensionFields": [],  
        "measureFields": [],  
        "displayFields": [  
          {  
            "name": "passenger_count"  
          },  
          {  
            "name": "EXPR$1"  
          }  
        ],  
        "entityType": "reflection"  
      },  
      "reflectionRequestEndpoint": "POST {hostname}/api/v3/reflection",  
      "jobIds": [  
        "13ffb629-9f0e-4265-97df-99bf0d425813"  
      ],  
      "jobCount": 1,  
      "recommendationId": "9be8a451-4190-4618-a72e-9932f790c744",  
      "reflectionScore": 50.67,  
      "avgImprovementFactor": 10.43,  
      "avgImprovementMs": 7196  
    }  
  ],  
  "canAlterReflections": true  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

405   Method Not Allowed

500   Internal Server Error

## Retrieving Usage-Based Recommendations[​](#retrieving-usage-based-recommendations "Direct link to Retrieving Usage-Based Recommendations")

Retrieve usage-based Reflection recommendations. The response includes the `reflectionRequestBody` and `recommendationId` attributes to use as body parameters in your request to [create usage-based Reflections](/25.x/reference/api/reflections/reflection-recommendations#creating-reflections-from-usage-based-recommendations).

Method and URL

```
GET /api/v3/reflection/recommendations/usage-based/
```

Example Request

```
curl -X GET 'https://{hostname}/api/v3/reflection/recommendations/usage-based/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "viewRequestBody": {  
        "entityType": "dataset",  
        "type": "VIRTUAL_DATASET",  
        "path": [  
          "prodFolder",  
          "cost_based"  
        ],  
        "sql": "--Default Raw Reflection"  
      },  
      "viewRequestEndpoint": "POST {hostname}/api/v3/catalog",  
      "reflectionRequestBody": {  
        "type": "RAW",  
        "name": "AutoRef_cost_based_raw",  
        "datasetId": "61d689a2-cd04-4d5d-84a7-021bdc15bff6",  
        "enabled": true,  
        "arrowCachingEnabled": false,  
        "dimensionFields": [],  
        "measureFields": [],  
        "displayFields": [  
          {  
            "name": "passenger_count"  
          },  
          {  
            "name": "pickup_datetime"  
          },  
          {  
            "name": "EXPR$2"  
          }  
        ],  
        "entityType": "reflection"  
      },  
      "reflectionRequestEndpoint": "POST {hostname}/api/v3/reflection",  
      "jobIds": [  
        "1975ec43-349a-9310-2e40-acbd8d025c00",  
        "1975ac7c-6541-86db-ae43-dcef2ffee300",  
        "1974b533-8c88-946b-92ce-ee5ab7791500"  
      ],  
      "jobCount": 3,  
      "recommendationId": "prodFolder.cost_based",  
      "reflectionScore": 36.928031592652964,  
      "avgImprovementFactor": 10.00000020692081,  
      "avgImprovementMs": 7393.800016999235  
    }  
  ],  
  "canAlterReflections": true  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

500   Internal Server Error

## Creating Reflections from Usage-Based Recommendations[​](#creating-reflections-from-usage-based-recommendations "Direct link to Creating Reflections from Usage-Based Recommendations")

Create Reflections to accelerate queries using the [usage-based recommendations](/25.x/reference/api/reflections/reflection-recommendations#retrieving-usage-based-recommendations) that you retrieved.

note

You must [retrieve usage-based recommendations](/25.x/reference/api/reflections/reflection-recommendations#retrieving-usage-based-recommendations) to get the parameters you need for this request.

Dremio supports creating only raw Reflections from usage-based recommendations.

Method and URL

```
POST /api/v3/reflection/recommendations/usage-based/
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

[reflection](/25.x/reference/api/reflections/reflection-recommendations/#parameters-of-the-reflection-object) Body   Object

Information about the usage-based Reflection to create. The Reflection object includes the contents of the reflectionRequestBody included in the response for requests to [retrieve usage-based recommendations](/25.x/reference/api/reflections/reflection-recommendations#retrieving-usage-based-recommendations).

**NOTE**: If desired, you may change the name of the Reflection by changing the value for the Reflection.name parameter in the body of your request. Dremio ignores any changes to the values of other parameters in the Reflection object.

---

recommendationId Body   String

Identifier for the usage-based recommendation you want to use to create Reflections. The recommendationId is included in the response for requests to [retrieve usage-based recommendations](/25.x/reference/api/reflections/reflection-recommendations#retrieving-usage-based-recommendations).

Example: prodFolder.cost\_based

---

#### Parameters of the `reflection` Object[​](#parameters-of-the-reflection-object "Direct link to parameters-of-the-reflection-object")

type Body   String

Reflection [type](/25.x/sonar/reflections/types-and-benefits). Value must be `RAW`.

---

name Body   String

User-provided name for the Reflection.

**NOTE**: If desired, you may change the name of the Reflection by changing the value for the name parameter in the body of your request.

Example: AutoRef\_cost\_based\_raw

---

datasetId Body   String

Unique identifier for the anchor dataset to associate with the Reflection.

Example: 61d689a2-cd04-4d5d-84a7-021bdc15bff6

---

enabled Body   Boolean

If the Reflection is available for accelerating queries, `true`. Otherwise, `false`.

Example: true

---

arrowCachingEnabled Body   Boolean

If Dremio converts data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, `true`. Otherwise, `false`.

Example: false

---

dimensionFields Body   Array of Object

Information about the dimension fields from the anchor dataset used in the Reflection. For raw Reflections, the dimensionFields value is an empty array.

Example: []

---

measureFields Body   Array of Object

Information about the measure fields from the anchor dataset used in the Reflection. For raw Reflections, the measureFields value is an empty array.

Example: []

---

displayFields Body   Array of Object

Information about the fields displayed from the anchor dataset. Valid only for raw Reflections. If the anchor dataset includes display fields, each object in the displayFields array contains one attribute: name.

Example: [{"name": "passenger\_count"},{"name": "EXPR$1"}]

---

entityType Body   String

Type of entity. For Reflection objects, the entityType is `reflection`.

Example Request

```
curl -X POST 'https://{hostname}/api/v3/reflection/recommendations/usage-based/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "reflection": {  
    "type": "RAW",  
    "name": "AutoRef_cost_based_raw",  
    "datasetId": "61d689a2-cd04-4d5d-84a7-021bdc15bff6",  
    "enabled": true,  
    "arrowCachingEnabled": false,  
    "dimensionFields": [],  
    "measureFields": [],  
    "displayFields": [  
      {  
        "name": "passenger_count"  
      },  
      {  
        "name": "pickup_datetime"  
      },  
      {  
        "name": "EXPR$2"  
      }  
    ],  
    "entityType": "reflection"  
  },  
  "recommendationId": "prodFolder.cost_based"  
}
```

Example Response

```
{  
  "id": "c929b8d2-82bf-4175-9476-010ba17c4f7f",  
  "type": "RAW",  
  "name": "AutoRef_cost_based_raw",  
  "tag": "4p/COEkSud7=",  
  "createdAt": "2024-06-28T19:30:30.977Z",  
  "updatedAt": "2024-06-28T19:30:30.977Z",  
  "datasetId": "61d689a2-cd04-4d5d-84a7-021bdc15bff6",  
  "currentSizeBytes": 0,  
  "totalSizeBytes": 0,  
  "enabled": true,  
  "arrowCachingEnabled": false,  
  "status": {  
    "config": "OK",  
    "refresh": "SCHEDULED",  
    "availability": "NONE",  
    "combinedStatus": "CANNOT_ACCELERATE_SCHEDULED",  
    "failureCount": 0,  
    "lastDataFetch": "1969-12-31T23:59:59.999Z",  
    "expiresAt": "1969-12-31T23:59:59.999Z"  
  },  
  "displayFields": [  
    {  
      "name": "passenger_count"  
    },  
    {  
      "name": "pickup_datetime"  
    },  
    {  
      "name": "EXPR$2"  
    }  
  ],  
  "partitionDistributionStrategy": "CONSOLIDATED",  
  "canView": true,  
  "canAlter": true,  
  "entityType": "reflection"  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

500   Internal Server Error

## Refreshing Usage-Based Recommendations[​](#refreshing-usage-based-recommendations "Direct link to Refreshing Usage-Based Recommendations")

Process collected data about view usage, clear existing usage-based recommendations, and generate new usage-based recommendations.

Use the usage-based endpoints to [retrieve](/25.x/reference/api/reflections/reflection-recommendations#retrieving-usage-based-recommendations) and [create](/25.x/reference/api/reflections/reflection-recommendations#creating-reflections-from-usage-based-recommendations) Reflections based on the refreshed recommendations this endpoint creates.

Method and URL

```
POST /api/v3/reflection/recommendations/usage-based/refresh/
```

Example Request

```
curl -X POST 'https://{hostname}/api/v3/reflection/recommendations/usage-based/refresh/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

This endpoint returns an empty response body with a `202 Accepted` response status code. Dremio updates the recommendations asynchronously, so it may take several minutes before you can [retrieve](/25.x/reference/api/reflections/reflection-recommendations#retrieving-usage-based-recommendations) the updated recommendations.

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

202   Accepted

400   Bad Request

401   Unauthorized

500   Internal Server Error

## Deleting Usage-Based Recommendations[​](#deleting-usage-based-recommendations "Direct link to Deleting Usage-Based Recommendations")

Delete all collected usage data and all current Reflection recommendations.

note

We recommend deleting recommendations only when troubleshooting.

Method and URL

```
DELETE /api/v3/reflection/recommendations/usage-based/
```

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/reflection/recommendations/usage-based/' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

This endpoint returns an empty response body with a `202 Accepted` response status code. Dremio deletes the recommendations asynchronously, so it may take several minutes for the deletion to complete.

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

202   Accepted

400   Bad Request

401   Unauthorized

500   Internal Server Error

## Retrieving Recommendations (Deprecated)[​](#retrieving-recommendations-deprecated "Direct link to Retrieving Recommendations (Deprecated)")

caution

The [`POST /api/v3/reflection/recommendations` endpoint](/25.x/reference/api/reflections/reflection-recommendations#requesting-recommendations-deprecated) described in this section is deprecated. In its place, use the [job-based and usage-based](/25.x/reference/api/reflections/reflection-recommendations) endpoints to retrieve and refresh Reflection recommendations.

Use the Recommendations API to submit job IDs of jobs that ran SQL queries, and receive recommendations for aggregation Reflections that can accelerate those queries.

For more information, see [Sending Requests to the Recommendations API](/25.x/sonar/reflections/reflection-recommendations#sending-requests-to-the-recommendations-api/).

Recommendation Object

```
{  
    "data": [  
        {  
        "viewRequestBody": {  
            "entityType": "dataset",  
            "path": [  
                "recommended_view",  
                "Dataset_be919a56-f18b-421b-9612-711a1cc51b69"  
            ],  
            "type": "VIRTUAL_DATASET",  
            "sql": "SELECT * FROM Samples.samples.dremio.com.\"NYC-taxi-trips\" WHERE trip_distance_mi <= 2.0 ORDER BY trip_distance_mi ASC",  
        }  
        "viewRequestEndpoint": "POST {hostname}/api/v3/catalog",  
        "reflectionRequestBody": {  
            "type": "AGGREGATION",  
            "name": "agg_250e70d1-5e2a-4938-a1a1-95f664085099",  
            "datasetId": "be919a56-f18b-421b-9612-711a1cc51b69",   
            "enabled": true,  
            "dimensionFields": [  
                {  
                    "name": "passenger_count",  
                    "granularity": "DATE"  
                }  
            ],  
            "measureFields": [  
                {  
                    "name": "fare_amount",  
                    "measureTypeList": [  
                        "SUM",  
                        "COUNT"  
                    ]  
                }  
            ],  
            "entityType": "reflection"  
        }  
        "reflectionRequestEndpoint": "POST {hostname}/api/v3/reflection",  
        "jobIds": ["6j6c34cf-9drf-b07a-5ab7-abea69a66d00"]  
        }  
    ],  
    "canAlterReflections": true    
}
```

#### Recommendation Attributes (Deprecated)[​](#recommendation-attributes-deprecated "Direct link to Recommendation Attributes (Deprecated)")

viewRequestBody Array of Object

The fields that you can include in a request to the Catalog API for creating the view on which to define the recommended aggregation Reflection.

For descriptions of these fields, see [View](/25.x/reference/api/catalog/view/).

---

viewRequestEndpoint String

The endpoint to use when submitting the request to the Catalog API to create the view on which to define the Reflection.

---

reflectionRequestBody Array of Object

The fields that you can include in a request to the Reflection API for creating the recommended aggregation Reflection.

For descriptions of these fields, see [Reflection](/25.x/reference/api/reflections/).

---

reflectionRequestEndpoint String

The endpoint to use when submitting the request to the Reflection API to create the aggregation Reflection.

---

jobIds Array of String

The IDs of the jobs that ran the queries for which the recommendation is given.

---

canAlterReflections String

Indicates whether the columns in the Reflection can be edited, and whether columns can be added or removed.

#### Requesting Recommendations (Deprecated)[​](#requesting-recommendations-deprecated "Direct link to Requesting Recommendations (Deprecated)")

caution

This endpoint is deprecated. In its place, use the [job-based and usage-based](/25.x/reference/api/reflections/reflection-recommendations) endpoints to retrieve and refresh Reflection recommendations.

Request recommended aggregation Reflections to accelerate the queries associated with the provided job ID or IDs.

Method and URL

```
POST /api/v3/reflection/recommendations
```

##### Parameters (Deprecated)[​](#parameters-deprecated "Direct link to Parameters (Deprecated)")

jobIds Body   Array of String

A list of the job IDs of jobs that have run the SQL commands that you want to receive one or more recommended Reflections for.

Example Request

```
curl -X POST 'https://{hostname}/api/v3/reflection/recommendations' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data   
'{  
  "jobIds": [  
    "1a515250-7572-0f9b-f5e5-89f505b55200",   
    "1a515292-583c-e407-79ef-9f9b494fa600"  
  ]  
}'
```

Was this page helpful?

[Previous

Reflection](/25.x/reference/api/reflections/)[Next

Reflection Summary](/25.x/reference/api/reflections/reflection-summary)

* [Recommendation Attributes](#recommendation-attributes)
* [Submitting Job IDs](#submitting-job-ids)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving Job-Based Recommendations](#retrieving-job-based-recommendations)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving Usage-Based Recommendations](#retrieving-usage-based-recommendations)
  + [Response Status Codes](#response-status-codes-2)
* [Creating Reflections from Usage-Based Recommendations](#creating-reflections-from-usage-based-recommendations)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-3)
* [Refreshing Usage-Based Recommendations](#refreshing-usage-based-recommendations)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting Usage-Based Recommendations](#deleting-usage-based-recommendations)
  + [Response Status Codes](#response-status-codes-5)
* [Retrieving Recommendations (Deprecated)](#retrieving-recommendations-deprecated)

---

# Source: https://docs.dremio.com/25.x/reference/api/reflections/reflection-summary

Version: 25.x

On this page

# Reflection Summary Enterprise

Use the Reflection API to retrieve a Reflection summary that includes the raw and aggregation Reflections for the Dremio instance.

Reflection summary objects are different from Reflection objects. Reflection summaries do not include certain attributes that define the Reflection, like the display, dimension, measure, sort, and partition attributes. Reflection summaries do include several attributes that do not appear in Reflection objects, like datasetType, datasetPath, and counts and links for considered, matched, and chosen jobs.

Reflection Summary Object

```
{  
  "data": [  
    {  
      "createdAt": "2022-07-05T19:19:40.244Z",  
      "updatedAt": "2023-01-13T19:46:01.313Z",  
      "id": "27077c03-ae49-454c-a7bb-a9a8b5eca224",  
      "reflectionType": "AGGREGATION",  
      "name": "NYC_taxi_agg",  
      "currentSizeBytes": 9272,  
      "outputRecords": 51,  
      "totalSizeBytes": 9272,  
      "datasetId": "fa7c487f-9550-474e-8a41-4826564c6b09",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:05:03.532Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 46387  
      },  
      "consideredCount": 202,  
      "matchedCount": 45,  
      "chosenCount": 5,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-26T23:27:04.281Z",  
      "updatedAt": "2023-01-26T23:27:04.281Z",  
      "id": "0e3d765a-2291-4a04-81eb-2daf5477cc7d",  
      "reflectionType": "RAW",  
      "name": "Raw Reflection",  
      "currentSizeBytes": 0,  
      "outputRecords": -1,  
      "totalSizeBytes": 0,  
      "datasetId": "acdad4be-7049-47e4-b616-b471c5b3c60c",  
      "datasetType": "PHYSICAL_DATASET",  
      "datasetPath": [  
        "@dremio",  
        "test"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "GIVEN_UP",  
        "availabilityStatus": "NONE",  
        "combinedStatus": "FAILED",  
        "refreshMethod": "NONE",  
        "failureCount": 3,  
        "lastFailureMessage": "The Default engine is not online.",  
        "lastDataFetchAt": null,  
        "expiresAt": null,  
        "lastRefreshDurationMillis": -1  
      },  
      "consideredCount": 0,  
      "matchedCount": 0,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:19.030Z",  
      "updatedAt": "2023-01-13T19:50:19.030Z",  
      "id": "8eec62d7-3419-4cf3-997d-0a153d81ed8a",  
      "reflectionType": "AGGREGATION",  
      "name": "dataset991_agg991",  
      "currentSizeBytes": 9273,  
      "outputRecords": 51,  
      "totalSizeBytes": 9273,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.342Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 11697  
      },  
      "consideredCount": 60,  
      "matchedCount": 9,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:17.714Z",  
      "updatedAt": "2023-01-13T19:50:17.714Z",  
      "id": "167428eb-7936-4ea2-a1fb-23b1ac6e9454",  
      "reflectionType": "RAW",  
      "name": "dataset991_raw991",  
      "currentSizeBytes": 818790,  
      "outputRecords": 29467,  
      "totalSizeBytes": 818790,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.747Z",  
        "expiresAt": "3022-05-16T19:46:02.747Z",  
        "lastRefreshDurationMillis": 16666  
      },  
      "consideredCount": 54,  
      "matchedCount": 37,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    }  
  ],  
  "nextPageToken": "CiQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==",  
  "isCanAlterReflections": true  
}
```

## Reflection Summary Attributes[​](#reflection-summary-attributes "Direct link to Reflection Summary Attributes")

[data](/25.x/reference/api/reflections/reflection-summary#attributes-of-objects-in-the-data-array) Array of Object

List of Reflection-summary objects for each Reflection in the Dremio instance.

---

nextPageToken String

Opaque string to pass for the `pageToken` query parameter in the next request to retrieve the next set of results. If nextPageToken is not included in the response, all available resources have been returned.

Example: CiQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==

---

isCanAlterReflections Boolean

If the current user has project-level privileges to alter Reflections, the value is `true`. Otherwise, the value is `false`.

Example: true

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

createdAt String

Date and time that the Reflection was created, in UTC format.

Example: 2022-07-05T19:19:40.244Z

---

updatedAt String

Date and time that the Reflection was last updated, in UTC format.

Example: 2023-01-13T19:46:01.313Z

---

id String (UUID)

Unique identifier of the Reflection.

Example: 27077c03-ae49-454c-a7bb-a9a8b5eca224

---

reflectionType String

Reflection type. For more information, read [Types of Reflections](/25.x/sonar/reflections/types-and-benefits).

Enum: RAW, AGGREGATION

Example: AGGREGATION

---

name String

User-provided name for the Reflection. For Reflections created in the Dremio UI, if the user did not provide a name, the default values are `Raw Reflection` and `Aggregation Reflection` (automatically assigned based on the Reflection type).

Example: NYC\_taxi\_agg

---

currentSizeBytes Integer

Data size of the latest Reflection job (if one exists), in bytes.

Example: 9272

---

outputRecords Integer

Number of records returned for the latest Reflection.

Example: 51

---

totalSizeBytes Integer

Data size of all Reflection jobs that have not been pruned (if any exist), in bytes.

Example: 9272

---

datasetId String

Unique identifier of the anchor dataset that is associated with the Reflection.

Example: fa7c487f-9550-474e-8a41-4826564c6b09

---

datasetType String

Type for the anchor dataset that is associated with the Reflection. If the anchor dataset is a table, the type is `PHYSICAL_DATASET`. If the anchor dataset is a view, the type is `VIRTUAL_DATASET`.

Enum: PHYSICAL\_DATASET, VIRTUAL\_DATASET

Example: VIRTUAL\_DATASET

---

datasetPath String

Path to the anchor dataset that is associated with the Reflection within Dremio, expressed in an array. The path consists of the source or space, followed by any folder and subfolders, followed by the name of the dataset itself as the last item in the array.

Example: ["Samples","samples.dremio.com","NYC Taxi Trips"]

---

[status](/25.x/reference/api/reflections/reflection-summary#attributes-of-the-status-object) Object

Information about the status of the Reflection.

Example: {\n "configStatus": "OK",\n "refreshStatus": "MANUAL",\n "availabilityStatus": "AVAILABLE",\n "combinedStatus": "CAN\_ACCELERATE",\n "refreshMethod": "FULL",\n "failureCount": 0,\n "lastDataFetchAt": "2023-01-13T19:05:03.532Z",\n "expiresAt": "3022-05-16T19:46:02.342Z",\n "lastRefreshDurationMillis": 46387\n }

---

consideredCount Integer

Number of jobs that considered the Reflection during planning.

Example: 202

---

matchedCount Integer

Number of jobs that matched the Reflection during planning.

Example: 45

---

chosenCount Integer

Number of jobs accelerated by the Reflection.

Example: 5

---

consideredJobsLink String

Link to list of considered jobs for the Reflection.

Example: /jobs?filters=%7B%22cor%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D

---

matchedJobsLink String

Link to list of matched jobs for the Reflection.

Example: /jobs?filters=%7B%22mar%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D

---

chosenJobsLink String

Link to list of chosen jobs for the Reflection.

Example: /jobs?filters=%7B%22chr%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D

---

isArrowCachingEnabled Boolean

If Dremio converts data from the Reflection's Parquet files to Apache Arrow format when copying that data to executor nodes, the value is `true`. Otherwise, the value is `false`.

Example: false

---

isCanView Boolean

If you can view Reflections on all datasets of a source, system, space, or folder, the value is `true`. Otherwise, the value is `false`.

Example: true

---

isCanAlter Boolean

If you can create, edit, and view Reflections on all datasets of a source, system, space, or folder, the value is `true`. Otherwise, the value is `false`.

Example: true

---

isEnabled Boolean

If the Reflection is available for accelerating queries, the value is `true`. Otherwise, the value is `false`.

Example: true

#### Attributes of the `status` Object[​](#attributes-of-the-status-object "Direct link to attributes-of-the-status-object")

configStatus String

Status of the Reflection configuration. If the value is `OK`, the Reflection configuration is free of errors. If the value is `INVALID`, the Reflection configuration contains one or more errors.

Enum: OK, INVALID

Example: OK

---

refreshStatus String

Status of the Reflection refresh.

* `GIVEN_UP`: Dremio attempted to refresh the Reflection multiple times, but each attempt has failed and Dremio will not make further attempts.
* `MANUAL`: Refresh period is set to 0, so you must use the Dremio UI to manually refresh the Reflection.
* `RUNNING`: Dremio is currently refreshing the Reflection.
* `SCHEDULED`: The Reflection refreshes according to a schedule.
* `ON_DATA_CHANGES`: All of the Reflection’s underlying tables are in Iceberg format, and the Reflection refreshes automatically if new snapshots are created after an update to the underlying tables.

Enum: GIVEN\_UP, MANUAL, RUNNING, SCHEDULED, ON\_DATA\_CHANGES

Example: MANUAL

---

availabilityStatus String

Status of the Reflection's availability for accelerating queries.

Enum: NONE, INCOMPLETE, EXPIRED, AVAILABLE

Example: AVAILABLE

---

combinedStatus String

Status of the Reflection based on a combination of config, refresh, and availability.

* `CAN_ACCELERATE`: The Reflection is fully functional.
* `CAN_ACCELERATE_WITH_FAILURES`: The most recent refresh failed to obtain a status, but Dremio still has a valid materialization.
* `CANNOT_ACCELERATE_INITIALIZING`: The Reflection is currently being loaded into the materialization cache. During this time, the Reflection is unable to accelerate queries.
* `CANNOT_ACCELERATE_MANUAL`: The Reflection is unable to accelerate any queries, and the `Never Refresh` option is selected for the refresh policy.
* `CANNOT_ACCELERATE_SCHEDULED`: The Reflection is currently unable to accelerate any queries, but it has been scheduled for a refresh at a future time.
* `DISABLED`: The Reflection has been manually disabled.
* `EXPIRED`: The Reflection has expired and cannot be used.
* `FAILED`: The attempt to refresh the Reflection has failed, typically three times in a row. The Reflection is still usable.
* `INVALID`: The Reflection is invalid because the underlying dataset has changed.
* `INCOMPLETE`: One or more pseudo-distributed file system (PDFS) nodes that contain materialized files are down (PFDS is supported for v21 and earlier). Only partial data is available. Configurations that use the Hadoop Distributed File System (HDFS) to store Reflections should not experience incomplete status.
* `REFRESHING`: The Reflection is currently being refreshed.

Example: CAN\_ACCELERATE

---

refreshMethod String

The method used for the most recent refresh of the Reflection. For new Reflections, the value is `NONE` until planned. For more information, read [Refreshing Reflections](/25.x/sonar/reflections/refreshing-reflections).

Enum: NONE, FULL, INCREMENTAL

Example: FULL

---

failureCount Integer

Number of times that an attempt to refresh the Reflection failed.

Example: 0

---

lastFailureMessage String

The error message from the last failed Reflection refresh. If the refresh of a Reflection never fails or succeeds after a failure, this attribute does not appear.

Example: "The Default engine is not online."

---

lastDataFetchAt String

Date and time that the Reflection data was last refreshed, in UTC format. If the Reflection is running, failing, or disabled, the lastDataFetchAt value is `1969-12-31T23:59:59.999Z`.

Example: 2023-01-13T19:05:03.532Z

---

expiresAt String

Date and time that the Reflection expires, in UTC format. If the Reflection is running, failing, or disabled, the expiresAt value is `1969-12-31T23:59:59.999Z`.

Example: 3022-05-16T19:46:02.342Z

---

lastRefreshDurationMillis Integer

Duration of the most recent refresh for the Reflection. In milliseconds.

Example: 46387

## Retrieving a Reflection Summary[​](#retrieving-a-reflection-summary "Direct link to Retrieving a Reflection Summary")

Retrieve a summary of the raw and aggregation Reflections in the Dremio instance.

Method and URL

```
GET /api/v3/reflection-summary
```

### Parameters[​](#parameters "Direct link to Parameters")

pageToken Query   String   Optional

Token for retrieving the next page of Reflection summary results. If the Dremio instance has more Reflection summary results than the maximum per page (default 50), the response includes a nextPageToken after the data array. Use the nextPageToken value in your request URL as the pageToken value. Do not change any other query parameters included in the request URL when you use pageToken. For more information, read [pageToken Query Parameter](/25.x/reference/api/#pagetoken-query-parameter).

---

maxResults Query   Integer   Optional

Maximum number of Reflection summaries to return in the response. Maximum valid value is `100`. Default is `50`. For more information, read [maxResults Query Parameter](/25.x/reference/api/#maxresults-query-parameter).

---

filter Query   Object   Optional

Filters for Reflection name, dataset name, availability status, and refresh status. Value is a URL-encoded string that represents a JSON object. The JSON object specifies the attributes to filter on and the values to match for each attribute. Available filter attributes:

* reflectionType: `RAW`, `AGGREGATION` (array of string)
* refreshStatus: `GIVEN_UP`, `MANUAL`, `RUNNING`, `SCHEDULED`, `ON_DATA_CHANGES` (array of string)
* availabilityStatus: `NONE`, `INCOMPLETE`, `EXPIRED`, `AVAILABLE` (array of string)
* configStatus: `OK`, `INVALID` (array of string)
* enabledFlag: `true`, `false` (Boolean)
* reflectionNameOrDatasetPath: full or partial Reflection name or dataset path; case insensitive (string)
* reflectionIds: IDs of Reflections to retrieve (array of string); must be used alone, with no other filters or query parameters

For more information, read [filter Query Parameter](/25.x/reference/api/#filter-query-parameter).

---

orderBy Query   String   Optional

Organize the response in ascending (default) or descending order by reflectionName, datasetName, or reflectionType. To specify descending order, precede the orderBy value with a `-` character. For more information, read [orderBy Query Parameter](/25.x/reference/api/#orderby-query-parameter).

Example Request Without Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary'  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header "Content-Type: application/json"
```

Example Response

```
{  
  "data": [  
    {  
      "createdAt": "2023-01-13T19:46:01.313Z",  
      "updatedAt": "2023-01-13T19:46:01.313Z",  
      "id": "27077c03-ae49-454c-a7bb-a9a8b5eca224",  
      "reflectionType": "AGGREGATION",  
      "name": "NYC_taxi_agg",  
      "currentSizeBytes": 9272,  
      "outputRecords": 51,  
      "totalSizeBytes": 9272,  
      "datasetId": "fa7c487f-9550-474e-8a41-4826564c6b09",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "Samples",  
        "samples.dremio.com",  
        "NYC-taxi-trips"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.342Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 46387  
      },  
      "consideredCount": 202,  
      "matchedCount": 45,  
      "chosenCount": 5,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22422ace5b8a9a-bb7a-c454-94ea-30c77072%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-26T23:27:04.281Z",  
      "updatedAt": "2023-01-26T23:27:04.281Z",  
      "id": "0e3d765a-2291-4a04-81eb-2daf5477cc7d",  
      "reflectionType": "RAW",  
      "name": "Raw Reflection",  
      "currentSizeBytes": 0,  
      "outputRecords": -1,  
      "totalSizeBytes": 0,  
      "datasetId": "acdad4be-7049-47e4-b616-b471c5b3c60c",  
      "datasetType": "PHYSICAL_DATASET",  
      "datasetPath": [  
        "@dremio",  
        "test"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "GIVEN_UP",  
        "availabilityStatus": "NONE",  
        "combinedStatus": "FAILED",  
        "refreshMethod": "NONE",  
        "failureCount": 3,  
        "lastDataFetchAt": null,  
        "expiresAt": null,  
        "lastRefreshDurationMillis": -1  
      },  
      "consideredCount": 0,  
      "matchedCount": 0,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22d7cc7745fad2-be18-40a4-1922-a567d3e0%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:19.030Z",  
      "updatedAt": "2023-01-13T19:50:19.030Z",  
      "id": "8eec62d7-3419-4cf3-997d-0a153d81ed8a",  
      "reflectionType": "AGGREGATION",  
      "name": "dataset991_agg991",  
      "currentSizeBytes": 9273,  
      "outputRecords": 51,  
      "totalSizeBytes": 9273,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.342Z",  
        "expiresAt": "3022-05-16T19:46:02.342Z",  
        "lastRefreshDurationMillis": 11697  
      },  
      "consideredCount": 60,  
      "matchedCount": 9,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%22a8de18d351a0-d799-3fc4-9143-7d26cee8%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    },  
    {  
      "createdAt": "2023-01-13T19:50:17.714Z",  
      "updatedAt": "2023-01-13T19:50:17.714Z",  
      "id": "167428eb-7936-4ea2-a1fb-23b1ac6e9454",  
      "reflectionType": "RAW",  
      "name": "dataset991_raw991",  
      "currentSizeBytes": 818790,  
      "outputRecords": 29467,  
      "totalSizeBytes": 818790,  
      "datasetId": "a461bf97-8464-43ed-bd86-a8fb90d920e3",  
      "datasetType": "VIRTUAL_DATASET",  
      "datasetPath": [  
        "temp",  
        "dataset991"  
      ],  
      "status": {  
        "configStatus": "OK",  
        "refreshStatus": "MANUAL",  
        "availabilityStatus": "AVAILABLE",  
        "combinedStatus": "CAN_ACCELERATE",  
        "refreshMethod": "FULL",  
        "failureCount": 0,  
        "lastDataFetchAt": "2023-01-13T19:46:02.747Z",  
        "expiresAt": "3022-05-16T19:46:02.747Z",  
        "lastRefreshDurationMillis": 16666  
      },  
      "consideredCount": 54,  
      "matchedCount": 37,  
      "chosenCount": 0,  
      "consideredJobsLink": "/jobs?filters=%7B%22cor%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "matchedJobsLink": "/jobs?filters=%7B%22mar%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "chosenJobsLink": "/jobs?filters=%7B%22chr%22%3A%5B%224549e6ca1b32-bf1a-2ae4-6397-be824761%22%5D%2C%22qt%22%3A%5B%22UI%22%2C%22EXTERNAL%22%2C%22ACCELERATION%22%5D%7D",  
      "isArrowCachingEnabled": false,  
      "isCanView": true,  
      "isCanAlter": true,  
      "isEnabled": true  
    }  
  ],  
  "nextPageToken": "CiQxNjc0MjhlYi03OTM2LTRlYTItYTFmYi0yM2IxYWM2ZTk0NTQSAA==",  
  "isCanAlterReflections": true  
}
```

This endpoint supports [query parameters](#parameters) that you can add to the request URL to include only specific types of Reflections in the Reflection summary, specify the maximum number of results to return, and sort the response to list Reflections in ascending or descending order.

For example, to order the Reflections within the summary in ascending order by reflectionName, add `?orderBy=reflectionName` to the request URL. For descending order, add a `-` character before the attribute name: `?orderBy=-reflectionName`.

In the same request, you can add the `filter` query parameter to retrieve only the raw Reflections that are refreshed manually or by schedule, are enabled, and apply to datasets with `samples.dremio.com` in their paths. The JSON object for such a filter would look like this:

Example JSON Object for Filter

```
{  
  "reflectionType": ["RAW"],  
  "refreshStatus": ["MANUAL","SCHEDULED"],  
  "enabledFlag": true,  
  "reflectionNameOrDatasetPath": "samples.dremio.com"  
}
```

However, to use the JSON object in the request URL, you must convert it to URL-encoded JSON, which looks like this:

Example JSON Object in URL-Encoded JSON

```
%7B%0A%20%20%22reflectionType%22%3A%20%5B%22RAW%22%5D%2C%0A%20%20%22refreshStatus%22%3A%20%5B%22MANUAL%22%2C%22SCHEDULED%22%5D%2C%0A%20%20%22enabledFlag%22%3A%20true%2C%0A%20%20%22reflectionNameOrDatasetPath%22%3A%20%22samples.dremio.com%22%0A%7D
```

Here is an example request URL that includes both the `orderBy` and `filter` query parameters:

Example Request with orderBy and filter Query Parameters

```
curl -X GET 'https://{hostname}/api/v3/reflection-summary?orderBy=reflectionName&filter=%7B%0A%20%20%22reflectionType%22%3A%20%5B%22RAW%22%5D%2C%0A%20%20%22refreshStatus%22%3A%20%5B%22MANUAL%22%2C%22SCHEDULED%22%5D%2C%0A%20%20%22enabledFlag%22%3A%20true%2C%0A%20%20%22reflectionNameOrDatasetPath%22%3A%20%22samples.dremio.com%22%0A%7D' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

For this request, the Reflection summary in the response will include only raw Reflections that are refreshed manually or by schedule, are enabled, and apply to datasets with `samples.dremio.com` in their paths, and the Reflections will be listed in ascending order by reflectionName.

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Recommendations](/25.x/reference/api/reflections/reflection-recommendations)[Next

Role](/25.x/reference/api/roles/)

* [Reflection Summary Attributes](#reflection-summary-attributes)
* [Retrieving a Reflection Summary](#retrieving-a-reflection-summary)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/roles/privilege

Version: 25.x

On this page

# Role Privileges Enterprise

Use the Role API to retrieve information about the [privileges](/25.x/security/rbac/privileges/) assigned to roles.

Role Privileges Object

```
{  
  "data": [  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "CREATE_TABLE"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "INSERT"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "DROP"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "mysql",  
      "type": "SOURCE",  
      "privilege": "EXTERNAL_QUERY"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples.\"samples.dremio.com\"",  
      "type": "FOLDER",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples.\"samples.dremio.com\".\"SF_incidents2016.json\"",  
      "type": "DATASET",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "testing",  
      "type": "SPACE",  
      "privilege": "SELECT"  
    }  
  ]  
}
```

## Role Privileges Attributes[​](#role-privileges-attributes "Direct link to Role Privileges Attributes")

[data](/25.x/reference/api/roles/privilege#attributes-of-objects-in-the-data-array) Array of Object

Information about the privileges the specified role has for the entities in the current organization, up to a maximum of 100 privileges. Each object in the data array describes a privilege the role has for a specific entity.

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

name String (UUID)

Name of the object to which the privilege applies. The name includes the objects's parent objects, if any.

Example: hive

---

type String

Type of the object to which the privilege applies.

Enum: SPACE, SOURCE, HOME, FOLDER, DATASET, FUNCTION

Example: SOURCE

---

privilege String

Name of the privilege that the role has for the object. Available privileges vary for different object types.

Example: SELECT

## Retrieving Role Privileges[​](#retrieving-role-privileges "Direct link to Retrieving Role Privileges")

Retrieve the specified role's privileges.

Method and URL

```
GET /api/v3/role/{id}/privilege
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the role whose privileges you want to retrieve.

Example: 3d83e7d7-98ee-4afa-ebdd-41c30eb92744

Example Request

```
curl -X GET 'https://{hostname}/api/v3/role/3d83e7d7-98ee-4afa-ebdd-41c30eb92744/privilege' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "CREATE_TABLE"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "INSERT"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "DROP"  
    },  
    {  
      "name": "hive",  
      "type": "SOURCE",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "mysql",  
      "type": "SOURCE",  
      "privilege": "EXTERNAL_QUERY"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples.\"samples.dremio.com\"",  
      "type": "FOLDER",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples.\"samples.dremio.com\".\"SF_incidents2016.json\"",  
      "type": "DATASET",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "testing",  
      "type": "SPACE",  
      "privilege": "SELECT"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Role](/25.x/reference/api/roles/)[Next

Scripts](/25.x/reference/api/scripts/)

* [Role Privileges Attributes](#role-privileges-attributes)
* [Retrieving Role Privileges](#retrieving-role-privileges)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/user/privilege

Version: 25.x

On this page

# User Privileges Enterprise

Use the User API to retrieve [privilege](/25.x/security/rbac/privileges/) information for Dremio users.

User Privileges Object

```
{  
  "data": [  
    {  
      "name": "\"@dremio\".\"1c0accd3-e8c0-1d55-23a2-0ff6529f6c00\"",  
      "type": "PDS",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"@dremio\".\"1c0accd3-e8c0-1d55-23a2-0ff6529f6c00\"",  
      "type": "PDS",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "\"@dremio\".Business",  
      "type": "FOLDER",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"@dremio\".Business",  
      "type": "FOLDER",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "INSERT"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "DROP"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "CREATE_TABLE"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "MANAGE_GRANTS"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "MODIFY"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "ALTER_REFLECTION"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "VIEW_REFLECTION"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"testing\".\"NYC-taxi-trips\"",  
      "type": "VDS",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "\"testing\".\"NYC-taxi-trips\"",  
      "type": "VDS",  
      "privilege": "MANAGE_GRANTS"  
    },  
    {  
      "name": "\"testing\".\"NYC-taxi-trips\"",  
      "type": "VDS",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "MANAGE_GRANTS"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "DELETE"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "MODIFY"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "VIEW"  
    }  
  ]  
}
```

## User Privileges Attributes[​](#user-privileges-attributes "Direct link to User Privileges Attributes")

[data](/25.x/reference/api/user/privilege#attributes-of-objects-in-the-data-array) Array of Object

Information about the privileges the specified user has for the catalog objects in the current organization, up to a maximum of 100 privileges. Each object in the data array describes a privilege on a specific catalog object.

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

name String (UUID)

Name of the object to which the privilege applies. The name includes the entity's parent space or folder, if any.

Example: "@dremio"."1c0accd3-e8c0-1d55-23a2-0ff6529f6c00"

---

type String

Type of the object to which the privilege applies.

Enum: SPACE, SOURCE, HOME, FOLDER, PDS, VDS, FUNCTION

Example: PDS

---

privilege String

Name of the privilege that the user has for the object. Available privileges vary for different object types.

Example: ALTER

## Retrieving User Privileges[​](#retrieving-user-privileges "Direct link to Retrieving User Privileges")

Retrieve the specified user's privileges.

Method and URL

```
GET /api/v3/user/{id}/privilege
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String

Unique identifier of the user whose privileges you want to retrieve.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

Example Request

```
curl -X GET 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43/privilege' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "name": "\"@dremio\".\"1c0accd3-e8c0-1d55-23a2-0ff6529f6c00\"",  
      "type": "PDS",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"@dremio\".\"1c0accd3-e8c0-1d55-23a2-0ff6529f6c00\"",  
      "type": "PDS",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "\"@dremio\".Business",  
      "type": "FOLDER",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"@dremio\".Business",  
      "type": "FOLDER",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "INSERT"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "DROP"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "CREATE_TABLE"  
    },  
    {  
      "name": "Samples",  
      "type": "SOURCE",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "MANAGE_GRANTS"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "MODIFY"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "ALTER_REFLECTION"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "VIEW_REFLECTION"  
    },  
    {  
      "name": "\"testing\"",  
      "type": "SPACE",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "\"testing\".\"NYC-taxi-trips\"",  
      "type": "VDS",  
      "privilege": "SELECT"  
    },  
    {  
      "name": "\"testing\".\"NYC-taxi-trips\"",  
      "type": "VDS",  
      "privilege": "MANAGE_GRANTS"  
    },  
    {  
      "name": "\"testing\".\"NYC-taxi-trips\"",  
      "type": "VDS",  
      "privilege": "ALTER"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "MANAGE_GRANTS"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "DELETE"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "MODIFY"  
    },  
    {  
      "name": "taxi",  
      "type": "SCRIPT",  
      "privilege": "VIEW"  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

User](/25.x/reference/api/user/)[Next

User Tokens](/25.x/reference/api/user/token)

* [User Privileges Attributes](#user-privileges-attributes)
* [Retrieving User Privileges](#retrieving-user-privileges)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)

---

# Source: https://docs.dremio.com/25.x/reference/api/user/token

Version: 25.x

On this page

# User Tokens Enterprise

Use the User API to create and retrieve personal access tokens for the current Dremio user and delete personal access tokens for any Dremio user.

note

You must [enable the use of personal access tokens](/25.x/security/authentication/personal-access-tokens/#enabling-the-use-of-pats) to make API requests for user tokens.

User Tokens Object

```
{  
  "data": [  
    {  
      "tid": "98ec8f42-7764-4d9d-af5a-693f1f1cc444",  
      "uid": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
      "label": "Tableau",  
      "createdAt": "2023-02-19T15:41:15.323Z",  
      "expiresAt": "2023-03-21T15:41:15.323Z"  
    },  
    {  
      "tid": "3b76a1e4-6539-46de-8f06-b7c41c71b61e",  
      "uid": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
      "label": "Test Nessie Source",  
      "createdAt": "2023-03-02T19:39:52.159Z",  
      "expiresAt": "2023-04-01T19:39:52.159Z"  
    },  
    {  
      "tid": "9376ef58-7b4c-2419-b1cb-a4ce4c53dfa7",  
      "uid": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
      "label": "Feature Testing",  
      "createdAt": "2023-03-07T14:47:08.211Z",  
      "expiresAt": "2023-09-03T14:47:08.211Z"  
    }  
  ]  
}
```

## User Tokens Attributes[​](#user-tokens-attributes "Direct link to User Tokens Attributes")

[data](/25.x/reference/api/user/token#attributes-of-objects-in-the-data-array) Array of Object

Information about the user's tokens. Each object in the data array describes a different token of the user.

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

tid String (UUID)

Unique identifier of the token.

Example: 98ec8f42-7764-4d9d-af5a-693f1f1cc444

---

uid String (UUID)

Unique identifier of the user.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

---

label String

User-provided name of the token.

Example: Tableau

---

createdAt String

Date and time that the token was created, in UTC format.

Example: 2023-02-19T15:41:15.323Z

---

expiresAt String

Date and time that the token will expire, in UTC format.

Example: 2023-03-21T15:41:15.323Z

## Creating a Token for a User[​](#creating-a-token-for-a-user "Direct link to Creating a Token for a User")

Create a personal access token for the current user.

note

You can create personal access tokens only for your own user account, and only you may use the tokens you create. Administrators cannot create tokens for other users or distribute tokens to other users.

Method and URL

```
POST /api/v3/user/{id}/token
```

### Parameters[​](#parameters "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

---

label Body   String

User-provided name for the token

Example: Feature Testing

---

millisecondsToExpire Body   String

Number of milliseconds until the token should expire. Maximum value is `15552000000`, which is equivalent to 180 days. If you omit the millisecondsToExpire parameter, the new token's expireAt setting will default to the time that the token is created and the token will immediately expire.

Example: 15552000000

Example Request

```
curl -X POST 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43/token' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "label": "Feature Testing",  
  "millisecondsToExpire": 15552000000  
}'
```

The response contains the personal access token:

Example Response

```
EXAMPLETOKEN7TjB3mfPS6AZQ5aPcXPmJS2ofXpLL86dmpDXRbKKi52BQdthnk==
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

405   Method Not Allowed

## Retrieving All Tokens for a User[​](#retrieving-all-tokens-for-a-user "Direct link to Retrieving All Tokens for a User")

Retrieve all tokens for the current user.

note

You can only retrieve personal access tokens for your own user account. Administrators cannot retrieve other users' tokens.

Method and URL

```
GET /api/v3/user/{id}/token
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the current user. You can only retrieve personal access tokens for your own user account.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

Example Request

```
curl -X GET 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43/token' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "tid": "98ec8f42-7764-4d9d-af5a-693f1f1cc444",  
      "uid": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
      "label": "Tableau",  
      "createdAt": "2023-02-19T15:41:15.323Z",  
      "expiresAt": "2023-03-21T15:41:15.323Z"  
    },  
    {  
      "tid": "3b76a1e4-6539-46de-8f06-b7c41c71b61e",  
      "uid": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
      "label": "Test Nessie Source",  
      "createdAt": "2023-03-02T19:39:52.159Z",  
      "expiresAt": "2023-04-01T19:39:52.159Z"  
    },  
    {  
      "tid": "9376ef58-7b4c-2419-b1cb-a4ce4c53dfa7",  
      "uid": "b9dbebc7-bc3b-4d56-9154-31762ab65a43",  
      "label": "Feature Testing",  
      "createdAt": "2023-03-07T14:47:08.211Z",  
      "expiresAt": "2023-09-03T14:47:08.211Z"  
    }  
  ]  
}
```

note

If the user has no personal access tokens, the response contains an empty data array.

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

405   Method Not Allowed

## Deleting All Tokens for a User[​](#deleting-all-tokens-for-a-user "Direct link to Deleting All Tokens for a User")

Delete all tokens for the specified user.

note

You must be a member of the ADMIN role to delete other users' tokens.

Method and URL

```
DELETE /api/v3/user/{id}/token
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user whose tokens you want to delete.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43/token' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

405   Method Not Allowed

## Deleting a Token for a User[​](#deleting-a-token-for-a-user "Direct link to Deleting a Token for a User")

Delete the specified token for the specified user.

note

You must be a member of the ADMIN role to delete other users's tokens.

Method and URL

```
DELETE /api/v3/user/{id}/token/{token-id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the user whose token you want to delete.

Example: b9dbebc7-bc3b-4d56-9154-31762ab65a43

---

token-id Path   String (UUID)

Unique identifier of the token you want to delete.

Example: 98ec8f42-7764-4d9d-af5a-693f1f1cc444

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/user/b9dbebc7-bc3b-4d56-9154-31762ab65a43/token/98ec8f42-7764-4d9d-af5a-693f1f1cc444' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

204   No Content

401   Unauthorized

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

User Privileges](/25.x/reference/api/user/privilege)[Next

Workload Management](/25.x/reference/api/wlm/)

* [User Tokens Attributes](#user-tokens-attributes)
* [Creating a Token for a User](#creating-a-token-for-a-user)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving All Tokens for a User](#retrieving-all-tokens-for-a-user)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-1)
* [Deleting All Tokens for a User](#deleting-all-tokens-for-a-user)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-2)
* [Deleting a Token for a User](#deleting-a-token-for-a-user)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-3)

---

# Source: https://docs.dremio.com/25.x/reference/api/wlm/queue

Version: 25.x

On this page

# Queue Enterprise

Use the Workload Management (WLM) API to create, retrieve, update, and delete WLM queues.

Queue Object

```
{  
  "data": [  
    {  
      "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "tag": "BNGRmgfEnDg=",  
      "name": "High Cost Reflections",  
      "maxMemoryPerNodeBytes": 8589934592,  
      "maxQueryMemoryPerNodeBytes": 8589934592,  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000,  
      "maxRunTimeoutMs": 300000,  
      "engineId": "DATA"  
    },  
    {  
      "id": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "tag": "HM2D9XElG3U=",  
      "name": "Low Cost Reflections",  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 86400000  
    },  
    {  
      "id": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "tag": "p22KaFcaB7g=",  
      "name": "COPY & OPTIMIZATION Queue",  
      "maxMemoryPerNodeBytes": 4294967296,  
      "maxQueryMemoryPerNodeBytes": 4294967296,  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 2,  
      "maxStartTimeoutMs": 300000,  
      "engineId": "YARN"  
    },  
    {  
      "id": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "tag": "//gNL3Ta2bY=",  
      "name": "Low Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 100,  
      "maxStartTimeoutMs": 300000  
    },  
    {  
      "id": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "tag": "wa+vYmA73gU=",  
      "name": "High Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000  
    }  
  ]  
}
```

## Queue Attributes[​](#queue-attributes "Direct link to Queue Attributes")

[data](/25.x/reference/api/wlm/queue#attributes-of-objects-in-the-data-array) Array of Object

List of queue objects in the Dremio instance.

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

id String (UUID)

Unique identifier of the queue, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

tag String

Unique identifier of the version of the queue. Dremio changes the tag whenever the queue changes and uses the tag to ensure that PUT requests apply to the most recent version of the queue.

Example: BNGRmgfEnDg=

---

name String

User-provided name for the queue.

Example: High Cost Reflections

---

maxMemoryPerNodeBytes Integer

Total memory (in bytes) that all queries running in parallel in a given queue can use per executor node.

---

maxQueryMemoryPerNodeBytes Integer

Total memory (in bytes) that each query in a given queue can use per executor node.

Example: 8589934592

---

cpuTier String

Amount of CPU time that threads get compared to other threads.

Enum: BACKGROUND, LOW, MEDIUM, HIGH, CRITICAL

Example: BACKGROUND

---

maxAllowedRunningJobs Integer

Number of queries that are allowed to run in parallel.

Example: 10

---

maxStartTimeoutMs Integer

Maximum length of time that a query can wait in the queue before it is cancelled, in milliseconds.

Example: 300000

---

maxRunTimeoutMs Integer

Maximum length of time that a query can run before it is cancelled, in milliseconds.

Example: 300000

---

engineId String

Name of the execution engine to which the queue's queries are routed. If you do not specify an engineId, the queue's queries run on any engine that is available at the time of execution. The engineID attribute is omitted from the queue object if no engine is specified. For more information, read [Workload Management-based Routing](/25.x/get-started/cluster-deployments/deployment-models/amazon-deployments/aws/admin/aws-edition-managing-engines#workload-management-based-routing).

Example: DATA

## Creating a Queue[​](#creating-a-queue "Direct link to Creating a Queue")

Create a WLM queue.

Method and URL

```
POST /api/v3/wlm/queue
```

### Parameters[​](#parameters "Direct link to Parameters")

name Body   String

User-provided name for the queue.

Example: High Cost Reflections

---

maxMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that all queries running in parallel in a given queue can use per executor node.

Example: 8589934592

---

maxQueryMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that each query in a given queue can use per executor node.

Example: 8589934592

---

cpuTier Body   String   Optional

Amount of CPU time that threads should get compared to other threads. Default is `MEDIUM`.

Enum: BACKGROUND, LOW, MEDIUM, HIGH, CRITICAL

Example: BACKGROUND

---

maxAllowedRunningJobs Body   Integer   Optional

Number of queries that are allowed to run in parallel.

Example: 10

---

maxStartTimeoutMs Body   Integer   Optional

Maximum length of time that a query can wait in the queue before it is cancelled, in milliseconds.

Example: 300000

---

maxRunTimeoutMs Body   Integer   Optional

Maximum length of time that a query can run before it is cancelled, in milliseconds.

Example: 300000

---

engineId Body   String   Optional

Name of the execution engine to which the queue's queries should be routed. If you do not specify an engineId, the queue's queries run on any engine that is available at the time of execution. For more information, read [Workload Management-based Routing](/25.x/get-started/cluster-deployments/deployment-models/amazon-deployments/aws/admin/aws-edition-managing-engines#workload-management-based-routing).

Example: DATA

Example Request

```
curl -X POST 'https://{hostname}/api/v3/wlm/queue' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "High Cost Reflections",  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "maxMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

405   Method Not Allowed

409   Conflict

## Retrieving All Queues[​](#retrieving-all-queues "Direct link to Retrieving All Queues")

Retrieve all WLM queues.

Method and URL

```
GET /api/v3/wlm/queue
```

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/queue' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "tag": "BNGRmgfEnDg=",  
      "name": "High Cost Reflections",  
      "maxMemoryPerNodeBytes": 8589934592,  
      "maxQueryMemoryPerNodeBytes": 8589934592,  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000,  
      "maxRunTimeoutMs": 300000,  
      "engineId": "DATA"  
    },  
    {  
      "id": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "tag": "HM2D9XElG3U=",  
      "name": "Low Cost Reflections",  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 86400000  
    },  
    {  
      "id": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "tag": "p22KaFcaB7g=",  
      "name": "COPY & OPTIMIZATION Queue",  
      "maxMemoryPerNodeBytes": 4294967296,  
      "maxQueryMemoryPerNodeBytes": 4294967296,  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 2,  
      "maxStartTimeoutMs": 300000,  
      "engineId": "YARN"  
    },  
    {  
      "id": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "tag": "//gNL3Ta2bY=",  
      "name": "Low Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 100,  
      "maxStartTimeoutMs": 300000  
    },  
    {  
      "id": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "tag": "wa+vYmA73gU=",  
      "name": "High Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a Queue by ID[​](#retrieving-a-queue-by-id "Direct link to Retrieving a Queue by ID")

Retrieve a specific WLM queue by the queue's ID.

Method and URL

```
GET /api/v3/wlm/queue/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the queue you want to retrieve, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/queue/1990e713-3cd2-458c-89e1-68995c2c1047' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a Queue by Name[​](#retrieving-a-queue-by-name "Direct link to Retrieving a Queue by Name")

Retrieve a specific WLM queue by the queue's name.

Method and URL

```
GET /api/v3/wlm/queue/by-name/{name}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

name Path   String

Name for the queue you want to retrieve. If the queue name includes special characters for a URL, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: High%20Cost%20Reflections

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/queue/by-name/High%20Cost%20Reflections' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Updating a Queue[​](#updating-a-queue "Direct link to Updating a Queue")

Update the specified WLM queue.

Method and URL

```
PUT /api/v3/wlm/queue/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the queue you want to update, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

tag Body   String

Unique identifier of the version of the queue to update. Dremio uses the tag to ensure that you are updating the most recent version of the queue.

Example: BNGRmgfEnDg=

---

name Body   String

User-provided name for the queue.

Example: High Cost Reflections

---

maxMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that all queries running in parallel in a given queue can use per executor node. If you omit the maxMemoryPerNodeBytes parameter in a PUT request, Dremio removes the existing maxMemoryPerNodeBytes value from the queue. To keep the existing value while making other updates, include the existing maxMemoryPerNodeBytes parameter and value in the PUT request.

Example: 8589934592

---

maxQueryMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that each query in a given queue can use per executor node. If you omit the maxQueryMemoryPerNodeBytes parameter in a PUT request, Dremio removes the existing maxQueryMemoryPerNodeBytes value from the queue. To keep the existing value while making other updates, include the existing maxQueryMemoryPerNodeBytes parameter and value in the PUT request.

Example: 8589934592

---

cpuTier Body   String   Optional

Amount of CPU time that threads should get compared to other threads. Default is `MEDIUM`. If you omit the cpuTier parameter in a PUT request, Dremio replaces it with the default value. To keep the existing setting while making other updates, include the existing cpuTier parameter and setting in the PUT request.

Enum: BACKGROUND, LOW, MEDIUM, HIGH, CRITICAL

Example: LOW

---

maxAllowedRunningJobs Body   Integer   Optional

Number of queries that are allowed to run in parallel. If you omit the maxAllowedRunningJobs parameter in a PUT request, Dremio removes the existing maxAllowedRunningJobs value from the queue. To keep the existing value while making other updates, include the existing maxAllowedRunningJobs parameter and value in the PUT request.

Example: 100

---

maxStartTimeoutMs Body   Integer   Optional

Maximum length of time that a query can wait in the queue before it is cancelled, in milliseconds. If you omit the maxStartTimeoutMs parameter in a PUT request, Dremio removes the existing maxStartTimeoutMs setting from the queue. To keep the existing setting while making other updates, include the existing maxStartTimeoutMs parameter and setting in the PUT request.

Example: 300000

---

maxRunTimeoutMs Body   Integer   Optional

Maximum length of time that a query is allowed to run before it is cancelled, in milliseconds. If you omit the maxRunTimeoutMs parameter in a PUT request, Dremio removes the existing maxRunTimeoutMs value from the queue. To keep the existing value while making other updates, include the existing maxRunTimeoutMs parameter and value in the PUT request.

Example: 300000

---

engineId Body   String

Name of the execution engine to which the queue's queries should be routed. If you do not specify an engineId, the queue's queries run on any engine that is available at the time of execution. For more information, read [Workload Management-based Routing](/25.x/get-started/cluster-deployments/deployment-models/amazon-deployments/aws/admin/aws-edition-managing-engines#workload-management-based-routing).

Example: DATA

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/wlm/queue/1990e713-3cd2-458c-89e1-68995c2c1047' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "LOW",  
  "maxAllowedRunningJobs": 100,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "xQh6KNyEjus=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "LOW",  
  "maxAllowedRunningJobs": 100,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

500   Internal Server Error

## Deleting a Queue[​](#deleting-a-queue "Direct link to Deleting a Queue")

Delete the specified WLM queue.

Method and URL

```
DELETE /api/v3/wlm/queue/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the queue that you want to delete, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/wlm/queue/1990e713-3cd2-458c-89e1-68995c2c1047' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Workload Management](/25.x/reference/api/wlm/)[Next

Rule](/25.x/reference/api/wlm/rule)

* [Queue Attributes](#queue-attributes)
* [Creating a Queue](#creating-a-queue)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving All Queues](#retrieving-all-queues)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Queue by ID](#retrieving-a-queue-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-2)
* [Retrieving a Queue by Name](#retrieving-a-queue-by-name)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-3)
* [Updating a Queue](#updating-a-queue)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting a Queue](#deleting-a-queue)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/wlm/rule

Version: 25.x

On this page

# Rule Enterprise

Use the Workload Management (WLM) API to create, retrieve, update, and delete WLM rules.

The rule object includes a rules array (also called the ruleset). Each object in the rules array represents an individual rule. Dremio processes rules in the order they are listed within the rules array: the highest-priority rule is listed first, and the lowest-priority rule is listed last.

Rule Object

```
{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

## Rule Attributes[​](#rule-attributes "Direct link to Rule Attributes")

tag String

Unique identifier of the version of the rule. Dremio changes the tag whenever a rule changes and uses the tag to ensure that PUT requests apply to the most recent version of the rules.

Example: VmqwaZ90VY4=

---

[rules](/25.x/reference/api/wlm/rule#attributes-of-objects-in-the-rules-array) Array of Object

List of rule objects in the Dremio instance.

---

[defaultRule](/25.x/reference/api/wlm/rule#attributes-of-the-defaultrule-object) Object

Information about the default rule for queries. Dremio applies the default rule to queries that do not meet the conditions for any other rule.

Example: {"name": "All Other Queries","action": "REJECT","id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"}

#### Attributes of Objects in the `rules` Array[​](#attributes-of-objects-in-the-rules-array "Direct link to attributes-of-objects-in-the-rules-array")

name String

User-provided name for the rule.

Example: High Cost Reflections

---

conditions String

Conditions that queries must match to be placed in the queue.

Example: query\_type() = 'Reflections' AND query\_cost() >= 30000000

---

acceptId String (UUID)

Unique identifier of the queue in which the rule places queries.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

acceptName Integer

User-provided name for the queue in which the rule places queries.

Example: High Cost Reflections

---

rejectMessage Integer

For rules whose action is `REJECT`, a user-provided message for queries that do not match the rule conditions.

Example: Rejected because query does not meet the rule conditions

---

action Integer

Action the rule takes for queries that match the rule conditions.

Enum: PLACE, REJECT

Example: PLACE

---

id String (UUID)

Unique identifier of the rule, in UTC format.

Example: fa1ec87d-923b-414c-9064-e079f39f5c49

#### Attributes of the `defaultRule` Object[​](#attributes-of-the-defaultrule-object "Direct link to attributes-of-the-defaultrule-object")

name String

User-provided name for the default rule.

Example: All Other Queries

---

acceptId String (UUID)

For default rules whose action is `PLACE`, the unique identifier of the queue in which the default rule places queries.

Example: a254d63e-9b0e-41be-af4a-1acc5bfe2332

---

acceptName Integer

For default rules whose action is `PLACE`, the user-provided name for the queue in which the rule places queries.

Example: Low Cost User Queries

---

rejectMessage Integer

For default rules whose action is `REJECT`, a user-provided message for queries that do not match any rule conditions.

Example: Rejected because query does not meet any rule conditions

---

action String

Action the default rule takes for queries that do not match the conditions for any other rule.

Enum: PLACE, REJECT

Example: REJECT

---

id String (UUID)

Unique identifier of the default rule.

Example: 8df37560-68c5-45a6-8e1f-4ee2e8438f81

## Creating or Updating a Rule[​](#creating-or-updating-a-rule "Direct link to Creating or Updating a Rule")

Create or update a WLM rule.

In the WLM API, you interact with the ruleset in the rules array rather than individual rules themselves. To add or update an individual rule, you must include the entire rules array in the request body. It is not necessary to specify the ID for the rule you want to delete in the request URL.

Method and URL

```
PUT /api/v3/wlm/rule
```

### Parameters[​](#parameters "Direct link to Parameters")

tag Body   String

Unique identifier of the rules instance. Dremio uses the tag to ensure that PUT requests apply to the most recent version of the rules. Omit if you are creating rules for the organization for the first time.

Example: VmqwaZ90VY4=

---

[rules](/25.x/reference/api/wlm/rule#parameters-of-objects-in-the-rules-array) Body   Array of Object

List of rule objects in the Dremio instance. To add or update an individual rule, you must include the entire rules array in the request body.

Example:

---

[defaultRule](/25.x/reference/api/wlm/rule#parameters-of-the-defaultrule-object) Body   Object

Information about the default rule for queries. Dremio applies the default rule to queries that do not meet the conditions for any other rule. To add or update an individual rule, you must include the defaultRule object in the request body.

Example: {"name": "All Other Queries","action": "REJECT","id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"}

#### Parameters of Objects in the `rules` Array[​](#parameters-of-objects-in-the-rules-array "Direct link to parameters-of-objects-in-the-rules-array")

name Body   String

User-provided name for the rule.

Example: DevOps and Engineering

---

conditions Body   String

Conditions that queries must match to be placed in the queue.

Example: is\_member('DevOps') OR is\_member('Engineering')

---

acceptId Body   String (UUID)

For rules whose action is `PLACE`, the unique identifier of the queue in which the rule should place queries.

Example: b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1

---

acceptName Body   Integer   Optional

For rules whose action is `PLACE`, the user-provided name for the queue in which the rule should place queries.

Example: High Cost Reflections

---

rejectMessage Body   Integer

For rules whose action is `REJECT`, a user-provided message for queries that do not match the rule conditions.

Example: Rejected because query does not meet the rule conditions

---

action Body   Integer   Optional

Action the rule should take for queries that match the rule conditions. Default is `PLACE`.

Enum: PLACE, REJECT

Example: PLACE

#### Parameters of the `defaultRule` Object[​](#parameters-of-the-defaultrule-object "Direct link to parameters-of-the-defaultrule-object")

name Body   String

User-provided name for the default rule.

Example: All Other Queries

---

acceptId Body   String (UUID)

For default rules whose action is `PLACE`, the unique identifier of the queue in which the default rule places queries.

Example: a254d63e-9b0e-41be-af4a-1acc5bfe2332

---

acceptName Body   Integer

For default rules whose action is `PLACE`, the user-provided name for the queue in which the rule places queries.

Example: Low Cost User Queries

---

rejectMessage Body   Integer

For default rules whose action is `REJECT`, a user-provided message for queries that do not match any rule conditions.

Example: Rejected because query does not meet any rule conditions

---

action Body   String

Action the default rule should take for queries that do not match the conditions for any other rule.

Enum: PLACE, REJECT

Example: REJECT

---

id Body   String (UUID)

Unique identifier of the default rule.

Example: 8df37560-68c5-45a6-8e1f-4ee2e8438f81

This example request demonstrates how to add a `DevOps and Engineering` rule to the ruleset:

Example Request to Add a Rule

```
curl -X PUT 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "DevOps and Engineering",  
      "conditions": "is_member('DevOps') OR is_member('Engineering')",  
      "acceptId": "b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1",  
      "acceptName": "DevOps and Eng Testing",  
      "action": "PLACE"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}'
```

Example Response

```
{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "DevOps and Engineering",  
      "conditions": "is_member('DevOps') OR is_member('Engineering')",  
      "acceptId": "b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1",  
      "acceptName": "DevOps and Eng Testing",  
      "action": "PLACE",  
      "id": "e4983ad5-cd4b-4b4a-9410-b5c37021ce34"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

To change the order in which Dremio processes rules, send a PUT request that lists the rules in the desired order within the rules array, with the highest-priority rule listed first, and the lowest-priority rule listed last.

This example request reorders the rules so that the `COPY & OPTIMIZATION Rule` will be the highest-priority rule:

Example Request to Reorder Rules

```
curl -X PUT 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}'
```

Example Response

```
{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Retrieving All Rules[​](#retrieving-all-rules "Direct link to Retrieving All Rules")

Retrieve all WLM rules.

Method and URL

```
GET /api/v3/wlm/rule
```

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "DevOps and Engineering",  
      "conditions": "is_member('DevOps') OR is_member('Engineering')",  
      "acceptId": "b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1",  
      "acceptName": "DevOps and Eng Testing",  
      "action": "PLACE",  
      "id": "e4983ad5-cd4b-4b4a-9410-b5c37021ce34"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

409   Conflict

500   Internal Server Error

## Deleting a Rule[​](#deleting-a-rule "Direct link to Deleting a Rule")

Delete a WLM rule from the ruleset.

In the WLM API, you interact with the ruleset in the rules array rather than individual rules themselves. To delete a rule, send a PUT request that omits the rule from the rules array. It is not necessary to specify the ID for the rule you want to delete in the request URL.

note

The default rule can be updated but cannot be deleted.

Method and URL

```
PUT /api/v3/wlm/rule/
```

This example request demonstrates how to remove the `DevOps and Engineering` rule added in the [Creating or Updating a Rule](#creating-or-updating-a-rule) example:

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}'
```

Example Response

```
{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

409   Conflict

500   Internal Server Error

Was this page helpful?

[Previous

Queue](/25.x/reference/api/wlm/queue)[Next

SQL Reference](/25.x/reference/sql/)

* [Rule Attributes](#rule-attributes)
* [Creating or Updating a Rule](#creating-or-updating-a-rule)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving All Rules](#retrieving-all-rules)
  + [Response Status Codes](#response-status-codes-1)
* [Deleting a Rule](#deleting-a-rule)
  + [Response Status Codes](#response-status-codes-2)

---

# Source: https://docs.dremio.com/25.x/reference/api/wlm/queue/

Version: 25.x

On this page

# Queue Enterprise

Use the Workload Management (WLM) API to create, retrieve, update, and delete WLM queues.

Queue Object

```
{  
  "data": [  
    {  
      "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "tag": "BNGRmgfEnDg=",  
      "name": "High Cost Reflections",  
      "maxMemoryPerNodeBytes": 8589934592,  
      "maxQueryMemoryPerNodeBytes": 8589934592,  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000,  
      "maxRunTimeoutMs": 300000,  
      "engineId": "DATA"  
    },  
    {  
      "id": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "tag": "HM2D9XElG3U=",  
      "name": "Low Cost Reflections",  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 86400000  
    },  
    {  
      "id": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "tag": "p22KaFcaB7g=",  
      "name": "COPY & OPTIMIZATION Queue",  
      "maxMemoryPerNodeBytes": 4294967296,  
      "maxQueryMemoryPerNodeBytes": 4294967296,  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 2,  
      "maxStartTimeoutMs": 300000,  
      "engineId": "YARN"  
    },  
    {  
      "id": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "tag": "//gNL3Ta2bY=",  
      "name": "Low Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 100,  
      "maxStartTimeoutMs": 300000  
    },  
    {  
      "id": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "tag": "wa+vYmA73gU=",  
      "name": "High Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000  
    }  
  ]  
}
```

## Queue Attributes[​](#queue-attributes "Direct link to Queue Attributes")

[data](/25.x/reference/api/wlm/queue#attributes-of-objects-in-the-data-array) Array of Object

List of queue objects in the Dremio instance.

#### Attributes of Objects in the `data` Array[​](#attributes-of-objects-in-the-data-array "Direct link to attributes-of-objects-in-the-data-array")

id String (UUID)

Unique identifier of the queue, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

tag String

Unique identifier of the version of the queue. Dremio changes the tag whenever the queue changes and uses the tag to ensure that PUT requests apply to the most recent version of the queue.

Example: BNGRmgfEnDg=

---

name String

User-provided name for the queue.

Example: High Cost Reflections

---

maxMemoryPerNodeBytes Integer

Total memory (in bytes) that all queries running in parallel in a given queue can use per executor node.

---

maxQueryMemoryPerNodeBytes Integer

Total memory (in bytes) that each query in a given queue can use per executor node.

Example: 8589934592

---

cpuTier String

Amount of CPU time that threads get compared to other threads.

Enum: BACKGROUND, LOW, MEDIUM, HIGH, CRITICAL

Example: BACKGROUND

---

maxAllowedRunningJobs Integer

Number of queries that are allowed to run in parallel.

Example: 10

---

maxStartTimeoutMs Integer

Maximum length of time that a query can wait in the queue before it is cancelled, in milliseconds.

Example: 300000

---

maxRunTimeoutMs Integer

Maximum length of time that a query can run before it is cancelled, in milliseconds.

Example: 300000

---

engineId String

Name of the execution engine to which the queue's queries are routed. If you do not specify an engineId, the queue's queries run on any engine that is available at the time of execution. The engineID attribute is omitted from the queue object if no engine is specified. For more information, read [Workload Management-based Routing](/25.x/get-started/cluster-deployments/deployment-models/amazon-deployments/aws/admin/aws-edition-managing-engines#workload-management-based-routing).

Example: DATA

## Creating a Queue[​](#creating-a-queue "Direct link to Creating a Queue")

Create a WLM queue.

Method and URL

```
POST /api/v3/wlm/queue
```

### Parameters[​](#parameters "Direct link to Parameters")

name Body   String

User-provided name for the queue.

Example: High Cost Reflections

---

maxMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that all queries running in parallel in a given queue can use per executor node.

Example: 8589934592

---

maxQueryMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that each query in a given queue can use per executor node.

Example: 8589934592

---

cpuTier Body   String   Optional

Amount of CPU time that threads should get compared to other threads. Default is `MEDIUM`.

Enum: BACKGROUND, LOW, MEDIUM, HIGH, CRITICAL

Example: BACKGROUND

---

maxAllowedRunningJobs Body   Integer   Optional

Number of queries that are allowed to run in parallel.

Example: 10

---

maxStartTimeoutMs Body   Integer   Optional

Maximum length of time that a query can wait in the queue before it is cancelled, in milliseconds.

Example: 300000

---

maxRunTimeoutMs Body   Integer   Optional

Maximum length of time that a query can run before it is cancelled, in milliseconds.

Example: 300000

---

engineId Body   String   Optional

Name of the execution engine to which the queue's queries should be routed. If you do not specify an engineId, the queue's queries run on any engine that is available at the time of execution. For more information, read [Workload Management-based Routing](/25.x/get-started/cluster-deployments/deployment-models/amazon-deployments/aws/admin/aws-edition-managing-engines#workload-management-based-routing).

Example: DATA

Example Request

```
curl -X POST 'https://{hostname}/api/v3/wlm/queue' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "name": "High Cost Reflections",  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "maxMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

405   Method Not Allowed

409   Conflict

## Retrieving All Queues[​](#retrieving-all-queues "Direct link to Retrieving All Queues")

Retrieve all WLM queues.

Method and URL

```
GET /api/v3/wlm/queue
```

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/queue' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "data": [  
    {  
      "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "tag": "BNGRmgfEnDg=",  
      "name": "High Cost Reflections",  
      "maxMemoryPerNodeBytes": 8589934592,  
      "maxQueryMemoryPerNodeBytes": 8589934592,  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000,  
      "maxRunTimeoutMs": 300000,  
      "engineId": "DATA"  
    },  
    {  
      "id": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "tag": "HM2D9XElG3U=",  
      "name": "Low Cost Reflections",  
      "cpuTier": "BACKGROUND",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 86400000  
    },  
    {  
      "id": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "tag": "p22KaFcaB7g=",  
      "name": "COPY & OPTIMIZATION Queue",  
      "maxMemoryPerNodeBytes": 4294967296,  
      "maxQueryMemoryPerNodeBytes": 4294967296,  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 2,  
      "maxStartTimeoutMs": 300000,  
      "engineId": "YARN"  
    },  
    {  
      "id": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "tag": "//gNL3Ta2bY=",  
      "name": "Low Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 100,  
      "maxStartTimeoutMs": 300000  
    },  
    {  
      "id": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "tag": "wa+vYmA73gU=",  
      "name": "High Cost User Queries",  
      "cpuTier": "MEDIUM",  
      "maxAllowedRunningJobs": 10,  
      "maxStartTimeoutMs": 300000  
    }  
  ]  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a Queue by ID[​](#retrieving-a-queue-by-id "Direct link to Retrieving a Queue by ID")

Retrieve a specific WLM queue by the queue's ID.

Method and URL

```
GET /api/v3/wlm/queue/{id}
```

### Parameters[​](#parameters-1 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the queue you want to retrieve, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/queue/1990e713-3cd2-458c-89e1-68995c2c1047' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Retrieving a Queue by Name[​](#retrieving-a-queue-by-name "Direct link to Retrieving a Queue by Name")

Retrieve a specific WLM queue by the queue's name.

Method and URL

```
GET /api/v3/wlm/queue/by-name/{name}
```

### Parameters[​](#parameters-2 "Direct link to Parameters")

name Path   String

Name for the queue you want to retrieve. If the queue name includes special characters for a URL, such as spaces, use URL encoding to replace the special characters with their UTF-8-equivalent characters. For example, "Dremio University" should be `Dremio%20University` in the URL path.

Example: High%20Cost%20Reflections

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/queue/by-name/High%20Cost%20Reflections' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "BACKGROUND",  
  "maxAllowedRunningJobs": 10,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes-3 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

403   Forbidden

404   Not Found

500   Internal Server Error

## Updating a Queue[​](#updating-a-queue "Direct link to Updating a Queue")

Update the specified WLM queue.

Method and URL

```
PUT /api/v3/wlm/queue/{id}
```

### Parameters[​](#parameters-3 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the queue you want to update, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

tag Body   String

Unique identifier of the version of the queue to update. Dremio uses the tag to ensure that you are updating the most recent version of the queue.

Example: BNGRmgfEnDg=

---

name Body   String

User-provided name for the queue.

Example: High Cost Reflections

---

maxMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that all queries running in parallel in a given queue can use per executor node. If you omit the maxMemoryPerNodeBytes parameter in a PUT request, Dremio removes the existing maxMemoryPerNodeBytes value from the queue. To keep the existing value while making other updates, include the existing maxMemoryPerNodeBytes parameter and value in the PUT request.

Example: 8589934592

---

maxQueryMemoryPerNodeBytes Body   Integer   Optional

Total memory (in bytes) that each query in a given queue can use per executor node. If you omit the maxQueryMemoryPerNodeBytes parameter in a PUT request, Dremio removes the existing maxQueryMemoryPerNodeBytes value from the queue. To keep the existing value while making other updates, include the existing maxQueryMemoryPerNodeBytes parameter and value in the PUT request.

Example: 8589934592

---

cpuTier Body   String   Optional

Amount of CPU time that threads should get compared to other threads. Default is `MEDIUM`. If you omit the cpuTier parameter in a PUT request, Dremio replaces it with the default value. To keep the existing setting while making other updates, include the existing cpuTier parameter and setting in the PUT request.

Enum: BACKGROUND, LOW, MEDIUM, HIGH, CRITICAL

Example: LOW

---

maxAllowedRunningJobs Body   Integer   Optional

Number of queries that are allowed to run in parallel. If you omit the maxAllowedRunningJobs parameter in a PUT request, Dremio removes the existing maxAllowedRunningJobs value from the queue. To keep the existing value while making other updates, include the existing maxAllowedRunningJobs parameter and value in the PUT request.

Example: 100

---

maxStartTimeoutMs Body   Integer   Optional

Maximum length of time that a query can wait in the queue before it is cancelled, in milliseconds. If you omit the maxStartTimeoutMs parameter in a PUT request, Dremio removes the existing maxStartTimeoutMs setting from the queue. To keep the existing setting while making other updates, include the existing maxStartTimeoutMs parameter and setting in the PUT request.

Example: 300000

---

maxRunTimeoutMs Body   Integer   Optional

Maximum length of time that a query is allowed to run before it is cancelled, in milliseconds. If you omit the maxRunTimeoutMs parameter in a PUT request, Dremio removes the existing maxRunTimeoutMs value from the queue. To keep the existing value while making other updates, include the existing maxRunTimeoutMs parameter and value in the PUT request.

Example: 300000

---

engineId Body   String

Name of the execution engine to which the queue's queries should be routed. If you do not specify an engineId, the queue's queries run on any engine that is available at the time of execution. For more information, read [Workload Management-based Routing](/25.x/get-started/cluster-deployments/deployment-models/amazon-deployments/aws/admin/aws-edition-managing-engines#workload-management-based-routing).

Example: DATA

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/wlm/queue/1990e713-3cd2-458c-89e1-68995c2c1047' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "BNGRmgfEnDg=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "LOW",  
  "maxAllowedRunningJobs": 100,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}'
```

Example Response

```
{  
  "id": "1990e713-3cd2-458c-89e1-68995c2c1047",  
  "tag": "xQh6KNyEjus=",  
  "name": "High Cost Reflections",  
  "maxMemoryPerNodeBytes": 8589934592,  
  "maxQueryMemoryPerNodeBytes": 8589934592,  
  "cpuTier": "LOW",  
  "maxAllowedRunningJobs": 100,  
  "maxStartTimeoutMs": 300000,  
  "maxRunTimeoutMs": 300000,  
  "engineId": "DATA"  
}
```

### Response Status Codes[​](#response-status-codes-4 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

500   Internal Server Error

## Deleting a Queue[​](#deleting-a-queue "Direct link to Deleting a Queue")

Delete the specified WLM queue.

Method and URL

```
DELETE /api/v3/wlm/queue/{id}
```

### Parameters[​](#parameters-4 "Direct link to Parameters")

id Path   String (UUID)

Unique identifier of the queue that you want to delete, in UTC format.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

Example Request

```
curl -X DELETE 'https://{hostname}/api/v3/wlm/queue/1990e713-3cd2-458c-89e1-68995c2c1047' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
No response
```

### Response Status Codes[​](#response-status-codes-5 "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

405   Method Not Allowed

Was this page helpful?

[Previous

Workload Management](/25.x/reference/api/wlm/)[Next

Rule](/25.x/reference/api/wlm/rule)

* [Queue Attributes](#queue-attributes)
* [Creating a Queue](#creating-a-queue)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving All Queues](#retrieving-all-queues)
  + [Response Status Codes](#response-status-codes-1)
* [Retrieving a Queue by ID](#retrieving-a-queue-by-id)
  + [Parameters](#parameters-1)
  + [Response Status Codes](#response-status-codes-2)
* [Retrieving a Queue by Name](#retrieving-a-queue-by-name)
  + [Parameters](#parameters-2)
  + [Response Status Codes](#response-status-codes-3)
* [Updating a Queue](#updating-a-queue)
  + [Parameters](#parameters-3)
  + [Response Status Codes](#response-status-codes-4)
* [Deleting a Queue](#deleting-a-queue)
  + [Parameters](#parameters-4)
  + [Response Status Codes](#response-status-codes-5)

---

# Source: https://docs.dremio.com/25.x/reference/api/wlm/rule/

Version: 25.x

On this page

# Rule Enterprise

Use the Workload Management (WLM) API to create, retrieve, update, and delete WLM rules.

The rule object includes a rules array (also called the ruleset). Each object in the rules array represents an individual rule. Dremio processes rules in the order they are listed within the rules array: the highest-priority rule is listed first, and the lowest-priority rule is listed last.

Rule Object

```
{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

## Rule Attributes[​](#rule-attributes "Direct link to Rule Attributes")

tag String

Unique identifier of the version of the rule. Dremio changes the tag whenever a rule changes and uses the tag to ensure that PUT requests apply to the most recent version of the rules.

Example: VmqwaZ90VY4=

---

[rules](/25.x/reference/api/wlm/rule#attributes-of-objects-in-the-rules-array) Array of Object

List of rule objects in the Dremio instance.

---

[defaultRule](/25.x/reference/api/wlm/rule#attributes-of-the-defaultrule-object) Object

Information about the default rule for queries. Dremio applies the default rule to queries that do not meet the conditions for any other rule.

Example: {"name": "All Other Queries","action": "REJECT","id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"}

#### Attributes of Objects in the `rules` Array[​](#attributes-of-objects-in-the-rules-array "Direct link to attributes-of-objects-in-the-rules-array")

name String

User-provided name for the rule.

Example: High Cost Reflections

---

conditions String

Conditions that queries must match to be placed in the queue.

Example: query\_type() = 'Reflections' AND query\_cost() >= 30000000

---

acceptId String (UUID)

Unique identifier of the queue in which the rule places queries.

Example: 1990e713-3cd2-458c-89e1-68995c2c1047

---

acceptName Integer

User-provided name for the queue in which the rule places queries.

Example: High Cost Reflections

---

rejectMessage Integer

For rules whose action is `REJECT`, a user-provided message for queries that do not match the rule conditions.

Example: Rejected because query does not meet the rule conditions

---

action Integer

Action the rule takes for queries that match the rule conditions.

Enum: PLACE, REJECT

Example: PLACE

---

id String (UUID)

Unique identifier of the rule, in UTC format.

Example: fa1ec87d-923b-414c-9064-e079f39f5c49

#### Attributes of the `defaultRule` Object[​](#attributes-of-the-defaultrule-object "Direct link to attributes-of-the-defaultrule-object")

name String

User-provided name for the default rule.

Example: All Other Queries

---

acceptId String (UUID)

For default rules whose action is `PLACE`, the unique identifier of the queue in which the default rule places queries.

Example: a254d63e-9b0e-41be-af4a-1acc5bfe2332

---

acceptName Integer

For default rules whose action is `PLACE`, the user-provided name for the queue in which the rule places queries.

Example: Low Cost User Queries

---

rejectMessage Integer

For default rules whose action is `REJECT`, a user-provided message for queries that do not match any rule conditions.

Example: Rejected because query does not meet any rule conditions

---

action String

Action the default rule takes for queries that do not match the conditions for any other rule.

Enum: PLACE, REJECT

Example: REJECT

---

id String (UUID)

Unique identifier of the default rule.

Example: 8df37560-68c5-45a6-8e1f-4ee2e8438f81

## Creating or Updating a Rule[​](#creating-or-updating-a-rule "Direct link to Creating or Updating a Rule")

Create or update a WLM rule.

In the WLM API, you interact with the ruleset in the rules array rather than individual rules themselves. To add or update an individual rule, you must include the entire rules array in the request body. It is not necessary to specify the ID for the rule you want to delete in the request URL.

Method and URL

```
PUT /api/v3/wlm/rule
```

### Parameters[​](#parameters "Direct link to Parameters")

tag Body   String

Unique identifier of the rules instance. Dremio uses the tag to ensure that PUT requests apply to the most recent version of the rules. Omit if you are creating rules for the organization for the first time.

Example: VmqwaZ90VY4=

---

[rules](/25.x/reference/api/wlm/rule#parameters-of-objects-in-the-rules-array) Body   Array of Object

List of rule objects in the Dremio instance. To add or update an individual rule, you must include the entire rules array in the request body.

Example:

---

[defaultRule](/25.x/reference/api/wlm/rule#parameters-of-the-defaultrule-object) Body   Object

Information about the default rule for queries. Dremio applies the default rule to queries that do not meet the conditions for any other rule. To add or update an individual rule, you must include the defaultRule object in the request body.

Example: {"name": "All Other Queries","action": "REJECT","id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"}

#### Parameters of Objects in the `rules` Array[​](#parameters-of-objects-in-the-rules-array "Direct link to parameters-of-objects-in-the-rules-array")

name Body   String

User-provided name for the rule.

Example: DevOps and Engineering

---

conditions Body   String

Conditions that queries must match to be placed in the queue.

Example: is\_member('DevOps') OR is\_member('Engineering')

---

acceptId Body   String (UUID)

For rules whose action is `PLACE`, the unique identifier of the queue in which the rule should place queries.

Example: b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1

---

acceptName Body   Integer   Optional

For rules whose action is `PLACE`, the user-provided name for the queue in which the rule should place queries.

Example: High Cost Reflections

---

rejectMessage Body   Integer

For rules whose action is `REJECT`, a user-provided message for queries that do not match the rule conditions.

Example: Rejected because query does not meet the rule conditions

---

action Body   Integer   Optional

Action the rule should take for queries that match the rule conditions. Default is `PLACE`.

Enum: PLACE, REJECT

Example: PLACE

#### Parameters of the `defaultRule` Object[​](#parameters-of-the-defaultrule-object "Direct link to parameters-of-the-defaultrule-object")

name Body   String

User-provided name for the default rule.

Example: All Other Queries

---

acceptId Body   String (UUID)

For default rules whose action is `PLACE`, the unique identifier of the queue in which the default rule places queries.

Example: a254d63e-9b0e-41be-af4a-1acc5bfe2332

---

acceptName Body   Integer

For default rules whose action is `PLACE`, the user-provided name for the queue in which the rule places queries.

Example: Low Cost User Queries

---

rejectMessage Body   Integer

For default rules whose action is `REJECT`, a user-provided message for queries that do not match any rule conditions.

Example: Rejected because query does not meet any rule conditions

---

action Body   String

Action the default rule should take for queries that do not match the conditions for any other rule.

Enum: PLACE, REJECT

Example: REJECT

---

id Body   String (UUID)

Unique identifier of the default rule.

Example: 8df37560-68c5-45a6-8e1f-4ee2e8438f81

This example request demonstrates how to add a `DevOps and Engineering` rule to the ruleset:

Example Request to Add a Rule

```
curl -X PUT 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "DevOps and Engineering",  
      "conditions": "is_member('DevOps') OR is_member('Engineering')",  
      "acceptId": "b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1",  
      "acceptName": "DevOps and Eng Testing",  
      "action": "PLACE"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}'
```

Example Response

```
{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "DevOps and Engineering",  
      "conditions": "is_member('DevOps') OR is_member('Engineering')",  
      "acceptId": "b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1",  
      "acceptName": "DevOps and Eng Testing",  
      "action": "PLACE",  
      "id": "e4983ad5-cd4b-4b4a-9410-b5c37021ce34"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

To change the order in which Dremio processes rules, send a PUT request that lists the rules in the desired order within the rules array, with the highest-priority rule listed first, and the lowest-priority rule listed last.

This example request reorders the rules so that the `COPY & OPTIMIZATION Rule` will be the highest-priority rule:

Example Request to Reorder Rules

```
curl -X PUT 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}'
```

Example Response

```
{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

### Response Status Codes[​](#response-status-codes "Direct link to Response Status Codes")

200   OK

400   Bad Request

401   Unauthorized

403   Forbidden

404   Not Found

409   Conflict

## Retrieving All Rules[​](#retrieving-all-rules "Direct link to Retrieving All Rules")

Retrieve all WLM rules.

Method and URL

```
GET /api/v3/wlm/rule
```

Example Request

```
curl -X GET 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json'
```

Example Response

```
{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "DevOps and Engineering",  
      "conditions": "is_member('DevOps') OR is_member('Engineering')",  
      "acceptId": "b9g7r35c-bda9-e4fb-bagf-9ceaceb9f7c1",  
      "acceptName": "DevOps and Eng Testing",  
      "action": "PLACE",  
      "id": "e4983ad5-cd4b-4b4a-9410-b5c37021ce34"  
    },  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-1 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

409   Conflict

500   Internal Server Error

## Deleting a Rule[​](#deleting-a-rule "Direct link to Deleting a Rule")

Delete a WLM rule from the ruleset.

In the WLM API, you interact with the ruleset in the rules array rather than individual rules themselves. To delete a rule, send a PUT request that omits the rule from the rules array. It is not necessary to specify the ID for the rule you want to delete in the request URL.

note

The default rule can be updated but cannot be deleted.

Method and URL

```
PUT /api/v3/wlm/rule/
```

This example request demonstrates how to remove the `DevOps and Engineering` rule added in the [Creating or Updating a Rule](#creating-or-updating-a-rule) example:

Example Request

```
curl -X PUT 'https://{hostname}/api/v3/wlm/rule' \  
--header 'Authorization: Bearer <PersonalAccessToken>' \  
--header 'Content-Type: application/json' \  
--data-raw '{  
  "tag": "3uzixTFD134=",  
  "rules": [  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}'
```

Example Response

```
{  
  "tag": "VmqwaZ90VY4=",  
  "rules": [  
    {  
      "name": "High Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() >= 30000000",  
      "acceptId": "1990e713-3cd2-458c-89e1-68995c2c1047",  
      "acceptName": "High Cost Reflections",  
      "action": "PLACE",  
      "id": "fa1ec87d-923b-414c-9064-e079f39f5c49"  
    },  
    {  
      "name": "Low Cost Reflections",  
      "conditions": "query_type() = 'Reflections' AND query_cost() < 30000000",  
      "acceptId": "0dbc50a0-034d-40f6-92f7-ff11eda0c760",  
      "acceptName": "Low Cost Reflections",  
      "action": "PLACE",  
      "id": "dcf15b80-403c-4eba-b600-41ea9319e103"  
    },  
    {  
      "name": "COPY & OPTIMIZATION Rule",  
      "conditions": "query_label() in ('COPY','OPTIMIZATION')",  
      "acceptId": "450ea2a5-9a64-4679-99cb-7b01bf6bba27",  
      "acceptName": "COPY & OPTIMIZATION Queue",  
      "action": "PLACE",  
      "id": "a7f27aea-1e23-4699-8846-51e731c219e9"  
    },  
    {  
      "name": "High Cost User Queries",  
      "conditions": "query_cost() >= 30000000",  
      "acceptId": "c2917cce-b566-4c6a-be63-2e28488a6928",  
      "acceptName": "High Cost User Queries",  
      "action": "PLACE",  
      "id": "880d84a2-548d-4040-b6ba-a5371e87aecf"  
    },  
    {  
      "name": "Low Cost User Queries",  
      "conditions": "query_cost() < 30000000",  
      "acceptId": "a254d63e-9b0e-41be-af4a-1acc5bfe2332",  
      "acceptName": "Low Cost User Queries",  
      "action": "PLACE",  
      "id": "c0fa6e0b-e479-497b-846a-ad543009a309"  
    }  
  ],  
  "defaultRule": {  
    "name": "All Other Queries",  
    "action": "REJECT",  
    "id": "8df37560-68c5-45a6-8e1f-4ee2e8438f81"  
  }  
}
```

### Response Status Codes[​](#response-status-codes-2 "Direct link to Response Status Codes")

200   OK

401   Unauthorized

404   Not Found

409   Conflict

500   Internal Server Error

Was this page helpful?

[Previous

Queue](/25.x/reference/api/wlm/queue)[Next

SQL Reference](/25.x/reference/sql/)

* [Rule Attributes](#rule-attributes)
* [Creating or Updating a Rule](#creating-or-updating-a-rule)
  + [Parameters](#parameters)
  + [Response Status Codes](#response-status-codes)
* [Retrieving All Rules](#retrieving-all-rules)
  + [Response Status Codes](#response-status-codes-1)
* [Deleting a Rule](#deleting-a-rule)
  + [Response Status Codes](#response-status-codes-2)