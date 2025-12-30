# Dremio Cloud API Reference

The Dremio REST API provides programmatic access to manage your data infrastructure, execute queries, and configure data sources.

## Base URLs

All REST endpoints build on one of the supported base URLs:

*   **Dremio API**: `https://api.dremio.cloud/v0/`
*   **Dremio Login**: `https://login.dremio.cloud/`
*   **Iceberg Catalog REST**: `https://catalog.dremio.cloud/api/iceberg/v1/`

## Prerequisites

*   **Access Token**: Create a personal access token (PAT) for authenticating each of your API calls.
*   **Project ID**: Most Dremio API operations manage or use project resources. You can find your Project ID in the Project Settings.

## Common Concepts

*   **UUIDs**: Many Dremio entities use Universally Unique Identifiers (UUIDs) as identifiers (36 characters).
*   **Idempotent Requests**: Add a `requestId` parameter (unique UUID) to POST requests to safely retry them.
*   **Timestamps**: Dremio timestamps use ISO 8601 format in UTC: `YYYY-MM-DDTHH:mm:ss.sssZ`.

## Query Parameters

Common query parameters supported by many endpoints:

*   `pageToken`: Token for retrieving the next page of results.
*   `maxChildren` / `maxResults`: Maximum number of items to return.
*   `include`: Include non-default response fields (e.g., `permissions`).
*   `exclude`: Exclude fields from the response (e.g., `children`).
*   `filter`: Filter results.
*   `orderBy`: Sort results.

---

## Catalog

### Catalog Attributes

*   `data`: Array of container objects in the catalog.
    *   `id`: UUID of the object.
    *   `path`: Array of strings representing the path.
    *   `tag`: UUID version tag.
    *   `type`: `CONTAINER`.
    *   `containerType`: `SOURCE`, `FOLDER`, or `FUNCTION`.
*   `stats`: Object containing `datasetCount` and `datasetCountBounded`.

### Retrieve a Catalog

```http
GET /v0/projects/{project_id}/catalog
```

#### Example

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## Source

### Source Attributes

*   `entityType`: `source`.
*   `id`: UUID of the source.
*   `type`: Source type (e.g., `AWSGLUE`, `S3`, `SNOWFLAKE`).
*   `name`: User-defined name.
*   `config`: Configuration options for the source.
*   `metadataPolicy`: Metadata update policies.

### Create a Source

```http
POST /v0/projects/{project_id}/catalog
```

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "source",
    "name": "MySource",
    "type": "S3",
    "config": {
      "bucketName": "my-bucket",
      "authenticationType": "ACCESS_KEY",
      "accessKey": "MY_ACCESS_KEY",
      "accessSecret": "MY_SECRET_KEY"
    }
  }'
```

### Retrieve a Source

**By ID:**
```http
GET /v0/projects/{project_id}/catalog/{id}
```

#### Example (By ID)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$SOURCE_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

**By Path:**
```http
GET /v0/projects/{project_id}/catalog/by-path/{path}
```

#### Example (By Path)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/by-path/MySource" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Update a Source

```http
PUT /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X PUT "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$SOURCE_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "source",
    "id": "'"$SOURCE_ID"'",
    "type": "S3",
    "name": "MySourceRenamed",
    "tag": "'"$TAG_VERSION"'",
    "config": {
      "bucketName": "my-new-bucket"
    }
  }'
```

### Delete a Source

```http
DELETE /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X DELETE "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$SOURCE_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## Folder

### Folder Attributes

*   `entityType`: `folder`.
*   `id`: UUID of the folder.
*   `path`: Array of strings.
*   `children`: List of items inside the folder.
*   `accessControlList`: User/role privileges.

### Add a Folder

```http
POST /v0/projects/{project_id}/catalog
```
**Body:** `{"entityType": "folder", "path": ["source", "newFolder"]}`

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "folder",
    "path": ["MySource", "MyNewFolder"]
  }'
```

### Retrieve a Folder

**By ID:**
```http
GET /v0/projects/{project_id}/catalog/{id}
```

#### Example (By ID)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$FOLDER_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

**By Path:**
```http
GET /v0/projects/{project_id}/catalog/by-path/{path}
```

#### Example (By Path)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/by-path/MySource/MyFolder" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Update a Folder

```http
PUT /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X PUT "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$FOLDER_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "folder",
    "id": "'"$FOLDER_ID"'",
    "path": ["MySource", "MyRenamedFolder"],
    "tag": "'"$TAG_VERSION"'"
  }'
```

### Delete a Folder

```http
DELETE /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X DELETE "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$FOLDER_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## File

### File Attributes

*   `type`: `FILE`.
*   `id`: Text path of the file (e.g., `dremio:/path/to/file.csv`).
*   `path`: Array of strings.

### Retrieve a File by Path

```http
GET /v0/projects/{project_id}/catalog/by-path/{path}
```

#### Example

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/by-path/MySource/path/to/file.csv" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## Table

### Table Attributes

*   `entityType`: `dataset`.
*   `type`: `PHYSICAL_DATASET`.
*   `id`: UUID of the table.
*   `path`: Array of strings.
*   `format`: Table format attributes (e.g., Parquet, Text).
*   `accelerationRefreshPolicy`: Reflection refresh policy.
*   `fields`: Table schema.

### Format a File or Folder as a Table

```http
POST /v0/projects/{project_id}/catalog
```
**Body:** `{"entityType": "dataset", "type": "PHYSICAL_DATASET", ...}`

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "dataset",
    "type": "PHYSICAL_DATASET",
    "path": ["MySource", "path", "to", "file.csv"],
    "format": {
      "type": "Text",
      "fieldDelimiter": ","
    }
  }'
```

### Retrieve a Table

**By ID:**
```http
GET /v0/projects/{project_id}/catalog/{id}
```

#### Example (By ID)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$TABLE_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

**By Path:**
```http
GET /v0/projects/{project_id}/catalog/by-path/{path}
```

#### Example (By Path)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/by-path/MySource/MyTable" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Update a Table

```http
PUT /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X PUT "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$TABLE_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "dataset",
    "id": "'"$TABLE_ID"'",
    "type": "PHYSICAL_DATASET",
    "path": ["MySource", "MyTable"],
    "tag": "'"$TAG_VERSION"'",
    "accelerationRefreshPolicy": {
      "refreshPeriodMs": 3600000,
      "gracePeriodMs": 10800000
    }
  }'
```

### Refresh Reflections on a Table

```http
POST /v0/projects/{project_id}/catalog/{id}/refresh
```

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$TABLE_ID/refresh" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Revert a Table to a File or Folder

```http
DELETE /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X DELETE "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$TABLE_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## Lineage

### Lineage Attributes

*   `sources`: Array of source objects used by the dataset.
*   `parents`: Array of parent objects (e.g., joined datasets).
*   `children`: Array of child objects referencing the dataset.

### Retrieve Lineage

```http
GET /v0/projects/{project_id}/catalog/{id}/graph
```

#### Example

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$DATASET_ID/graph" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## User-Defined Function (UDF)

### UDF Attributes

*   `entityType`: `function`.
*   `id`: UUID of the function.
*   `functionBody`: The SQL statement of the function.
*   `functionArgList`: Arguments and data types.
*   `returnType`: Return data type(s).
*   `isScalar`: Boolean (true for scalar, false for tabular).

### Create a UDF

```http
POST /v0/projects/{project_id}/catalog
```
**Body:** `{"entityType": "function", ...}`

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "function",
    "path": ["MySource", "my_udf"],
    "functionBody": "SELECT 1",
    "returnType": "INTEGER",
    "functionArgList": []
  }'
```

### Retrieve a UDF

**By ID:**
```http
GET /v0/projects/{project_id}/catalog/{id}
```

#### Example (By ID)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$UDF_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

**By Path:**
```http
GET /v0/projects/{project_id}/catalog/by-path/{path}
```

#### Example (By Path)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/by-path/MySource/my_udf" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Update a UDF

```http
PUT /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X PUT "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$UDF_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "function",
    "id": "'"$UDF_ID"'",
    "tag": "'"$TAG_VERSION"'",
    "path": ["MySource", "my_udf"],
    "functionBody": "SELECT 2",
    "returnType": "INTEGER",
    "functionArgList": []
  }'
```

### Delete a UDF

```http
DELETE /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X DELETE "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$UDF_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## Tag

### Tag Attributes

*   `tags`: Array of strings.
*   `version`: UUID version of the tag set.

### Create/Modify Tags

```http
POST /v0/projects/{project_id}/catalog/{id}/collaboration/tag
```

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$DATASET_ID/collaboration/tag" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "tags": ["tag1", "tag2"]
  }'
```

### Retrieve Tags

```http
GET /v0/projects/{project_id}/catalog/{id}/collaboration/tag
```

#### Example

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$DATASET_ID/collaboration/tag" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Delete Tags

Send an empty array to the create/modify endpoint.

---

## Wiki

### Wiki Attributes

*   `text`: Markdown text content.
*   `version`: Version number.

### Create/Update Wiki

```http
POST /v0/projects/{project_id}/catalog/{id}/collaboration/wiki
```

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$DATASET_ID/collaboration/wiki" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "# My Wiki Content\nThis is a description."
  }'
```

### Retrieve Wiki

```http
GET /v0/projects/{project_id}/catalog/{id}/collaboration/wiki
```

#### Example

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$DATASET_ID/collaboration/wiki" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Delete Wiki

Send an empty string to the create/update endpoint.

---

## View

### View Attributes

*   `entityType`: `dataset`.
*   `type`: `VIRTUAL_DATASET`.
*   `id`: UUID of the view.
*   `sql`: SQL query defining the view.
*   `sqlContext`: Context for the SQL query.
*   `fields`: View schema.

### Create a View

```http
POST /v0/projects/{project_id}/catalog
```
**Body:** `{"entityType": "dataset", "type": "VIRTUAL_DATASET", ...}`

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "dataset",
    "type": "VIRTUAL_DATASET",
    "path": ["MySpace", "MyView"],
    "sql": "SELECT * FROM MySource.MyTable"
  }'
```

### Retrieve a View

**By ID:**
```http
GET /v0/projects/{project_id}/catalog/{id}
```

#### Example (By ID)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$VIEW_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

**By Path:**
```http
GET /v0/projects/{project_id}/catalog/by-path/{path}
```

#### Example (By Path)

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/by-path/MySpace/MyView" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Update a View

```http
PUT /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X PUT "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$VIEW_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "entityType": "dataset",
    "id": "'"$VIEW_ID"'",
    "type": "VIRTUAL_DATASET",
    "path": ["MySpace", "MyView"],
    "tag": "'"$TAG_VERSION"'",
    "sql": "SELECT * FROM MySource.MyTable WHERE id > 100"
  }'
```

### Refresh Reflections on a View

```http
POST /v0/projects/{project_id}/catalog/{id}/refresh
```

#### Example

```bash
curl -X POST "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$VIEW_ID/refresh" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

### Delete a View

```http
DELETE /v0/projects/{project_id}/catalog/{id}
```

#### Example

```bash
curl -X DELETE "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$VIEW_ID" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```

---

## Grants

### Grants Attributes

*   `availablePrivileges`: List of available privileges.
*   `grants`: Array of grant objects (privileges, granteeType, id).

### Create or Update Grants

```http
PUT /v0/projects/{project_id}/catalog/{id}/grants
```

#### Example

```bash
curl -X PUT "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$CATALOG_ID/grants" \
  -H "Authorization: Bearer $DREMIO_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "grants": [
      {
        "granteeType": "USER",
        "id": "'"$USER_ID"'",
        "privileges": ["SELECT", "ALTER"]
      }
    ]
  }'
```

### Retrieve Grants

```http
GET /v0/projects/{project_id}/catalog/{id}/grants
```

#### Example

```bash
curl -X GET "https://api.dremio.cloud/v0/projects/$PROJECT_ID/catalog/$CATALOG_ID/grants" \
  -H "Authorization: Bearer $DREMIO_TOKEN"
```
