# Dremio Software - Security



---

# Source: https://docs.dremio.com/current/security/

Version: current [26.x]

# Security and Compliance Enterprise

Dremio offers extensive security measures to help protect the integrity of your data, such as access control and federation with external identity providers. Dremio provides flexible native security features and integration with a wide range of third-party tools so that your organization can adhere to compliance and regulatory standards, enforce fine-grained permissions for your users, and retain your existing tools for authentication and authorization.

* [Authentication](/current/security/authentication/) – Manage user identities, authentication, and enterprise identity providers.
* [Access Control](/current/security/rbac) – Grant fine-grained permissions at the user or role level using native Dremio features or an integrated external data security product.
* [Integrations](/current/security/integrations/) – Manage access control and data governance through third-party integrations.
* [Secrets Management](/current/security/secrets-management/) – Use a secrets management service to provide sensitive information like passwords and secret access keys instead of providing it in plaintext.
* [Audit Logging](/current/security/auditing/) – Ensure the integrity of your network using virtual network (VNet) configurations for outbound connections from Dremio executors.
* [Compliance](/current/security/compliance) – Review the current compliance measures and audits Dremio has undergone to ensure top-level security for your data.

As the [Dremio Shared Responsibility Models](/responsibility) outline, platform security is a shared responsibility between Dremio and you. The Shared Responsibility Models lay out Dremio's responsibilities for providing vulnerability management and application security and your responsibilities for deployment and operations.

To configure external services, read:

* [Integrate with Lake Formation](/current/security/integrations/lake-formation/)
* [Integrate with Privacera](/current/security/integrations/privacera/)
* [Apache Ranger Row-Level Filtering & Column-Masking](/current/security/integrations/row-column-policies-ranger/)
* [LDAP](/current/security/authentication/identity-providers/ldap)

Was this page helpful?

[Previous

Use Reflections in Nessie Source Branches](/current/acceleration/manual-reflections/using-nessie-branches-with-reflections)[Next

Authentication](/current/security/authentication/)

---

# Source: https://docs.dremio.com/current/security/authentication/

Version: current [26.x]

On this page

# Authentication

Dremio supports several types of authentication for identity providers, client connections, and user types, including both regular users and service users.

## Authentication Methods by Application Type

| App Type | [Enterprise OIDC Provider](/current/security/authentication/identity-providers/#openid-connect-oidc-providers) | [LDAP](/current/security/authentication/identity-providers/#ldap-lightweight-directory-access-protocol) or Dremio Local Provider |
| --- | --- | --- |
| **Dremio Console** | * Single Sign-On * Personal Access Token | * Username and Password * Personal Access Token |
| **User Clients & Applications** | * Personal Access Token * **OAuth-based authentication**: External JWT Exchange or External JWT with Legacy JDBC | * Personal Access Token * Username and Password with JDBC/ODBC |
| **M2M Applications** | * Service Users with External Service Principals | * OAuth Client Credentials * **Legacy Migration**: PAT Exchange or Obtaining OAuth Tokens with Username and Password |

## Dremio Console Authentication Methods

### Single Sign-On

The user is authenticated by the configured OIDC identity provider, including automatic authentication if the user is already signed in to the identity provider.

### Username and Password

The user provides a username and password combination for authentication. See [User Management](/current/security/user-management/) for information on adding and managing local and external users.

### Personal Access Token

A personal access token (PAT) is used in place of a user password. PATs provide a convenient way to create a client connection without exposing a user's password, but can pose a security risk if not properly managed. PATs can be configured with long lifetimes, and lost or compromised tokens may allow access to sensitive data until the token expires. Before use, the administrator must [activate PATs](/current/security/authentication/personal-access-tokens/) for the Dremio cluster.

To use a PAT, the user must follow these steps:

1. [Create a PAT](/current/security/authentication/personal-access-tokens/#creating-a-token) in the Dremio console. Users can create additional PATs using the Dremio console or the [PAT creation](/current/api-reference/dremio-rest-api/#tag/Personal-Access-Tokens) REST API.
2. Use the PAT to connect with the Dremio console, [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/), [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/), [Legacy JDBC](/current/client-applications/drivers/jdbc/), or [Dremio REST](/current/api-reference/dremio-rest-api/).

## User Applications Authentication Methods

### External JWT

Client apps can request OAuth 2.0 JSON Web Tokens (JWTs) from external token providers, allowing users to authenticate through custom or third-party applications without exposing their credentials to the client application.

After obtaining an external JWT, the client app can create connections to Dremio using the [Legacy JDBC driver](/current/client-applications/drivers/jdbc/). However, Dremio recommends external JWT token exchange because Dremio OAuth access tokens are smaller and verification is faster.

To use an external JWT, the administrator must configure Dremio to use the Enterprise OIDC provider as an [external token provider](/current/security/authentication/application-authentication/external-token-providers/).

After configuration, a client application performs the following steps:

1. A user authenticates with the external token provider and the client [receives a JWT](/current/security/authentication/application-authentication/external-token-providers/#retrieving-an-external-jwt).
2. Create a connection to Dremio using the [Legacy JDBC](/current/client-applications/drivers/jdbc/) and the external JWT.

### External JWT Exchange

Exchanging the external JWT for an OAuth access token enables additional connection choices after authenticating with the external token provider. A client application performs the following steps:

1. A user authenticates with the external token provider and the client [receives a JWT](/current/security/authentication/application-authentication/external-token-providers/#retrieving-an-external-jwt).
2. Use the `/oauth/token` [REST API](/current/reference/api/oauth-token) to [exchange the JWT for an OAuth access token](/current/security/authentication/oauth-token-exchange/).
3. Create a connection to Dremio using [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/), [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/), [Legacy JDBC](/current/client-applications/drivers/jdbc/), or [Dremio REST](/current/api-reference/dremio-rest-api/) and the OAuth access token.

## M2M Applications Authentication Methods

### OAuth Client Credentials

Service users authenticate using the OAuth 2.0 client credentials flow, where a client ID and client secret are exchanged for access tokens. This is the primary authentication method for service users and provides:

* **Automated authentication** without manual login processes
* **Short-lived access tokens** that enhance security
* **Centralized credential management** through the OAuth system
* **Audit trails** for programmatic access

To use OAuth client credentials:

1. Create a service user in the Dremio console under **Settings > User Management > Service Users**. Upon creation, Dremio generates a unique client ID and client secret.
2. Use the `/oauth/token` [REST API](/current/reference/api/oauth-token) to exchange the client ID and client secret for an OAuth access token.
3. Create a connection to Dremio using [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/), [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/), [Legacy JDBC](/current/client-applications/drivers/jdbc/), or [Dremio REST](/current/api-reference/dremio-rest-api/) and the OAuth access token.

### External Service Principal Authentication

You can configure Dremio [service users](/current/security/authentication/users#user-types) to authenticate using service principals from Microsoft Entra ID or another OIDC provider. This allows service users to authenticate using JWTs from external identity providers, which are then exchanged for Dremio OAuth access tokens.

This method is useful for organizations that want to:

* Centralize service principal management in their identity provider
* Use existing Microsoft Entra ID service principals for Dremio access
* Maintain consistent authentication patterns across multiple systems

To use external service principal authentication:

1. Create a [service user](/current/security/authentication/users#user-types) in the Dremio console and configure external credentials linking to your service principal in Microsoft Entra ID or another OIDC provider.
2. The service user authenticates with the external identity provider and receives a JWT.
3. Use the `/oauth/token` [REST API](/current/reference/api/oauth-token) to exchange the external JWT for an OAuth access token.
4. Create a connection to Dremio using [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/), [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/), [Legacy JDBC](/current/client-applications/drivers/jdbc/), or [Dremio REST](/current/api-reference/dremio-rest-api/) and the OAuth access token.

## Legacy Authentication Methods

### Obtain OAuth Access Tokens with Username and Password

Organizations transitioning to OAuth-based authentication can use a username and password from a traditional user account to obtain an OAuth access token. This method allows teams to implement OAuth-based authentication immediately while planning their migration to dedicated service users and any associated configuration of an external identity provider.

Users follow these steps to exchange a username and password:

1. Use the `/oauth/token` [REST API](/current/reference/api/oauth-token#obtain-tokens-via-username-and-password) to obtain OAuth access tokens using a username and password.
2. Create a connection to Dremio using [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/), [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/), [Legacy JDBC](/current/client-applications/drivers/jdbc/), or [Dremio REST](/current/api-reference/dremio-rest-api/) and the OAuth access token.
3. Use the optional [refresh token to create OAuth access tokens](/current/reference/api/oauth-token#exchange-a-refresh-token) to obtain fresh OAuth access tokens as they expire.

### PAT Exchange

PAT Exchange serves as a migration bridge for existing applications that currently use PATs but need to integrate with systems expecting OAuth access tokens. This method allows organizations to maintain existing PAT-based workflows while transitioning to proper service user authentication.

Users follow these steps to exchange a PAT:

1. [Create a PAT](/current/security/authentication/personal-access-tokens/#creating-a-token) in the Dremio console or using the [REST API](/current/reference/api/personal-access-token) after creating the first token.
2. Use the `/oauth/token` [REST API](/current/reference/api/oauth-token#exchange-a-pat) to exchange the PAT for an OAuth access token.
3. Create a connection to Dremio using [Arrow Flight SQL JDBC](/current/client-applications/drivers/arrow-flight-sql-jdbc-driver/), [Arrow Flight SQL ODBC](/current/client-applications/drivers/arrow-flight-sql-odbc-driver/), [Legacy JDBC](/current/client-applications/drivers/jdbc/), or [Dremio REST](/current/api-reference/dremio-rest-api/) and the OAuth access token.

### Dremio Authentication Token

Dremio authentication tokens are generated from your Dremio username and password. This authentication method uses the prior generation `/apiv2/login` endpoint, now internal and subject to change without notice. See [Dremio Authentication Tokens](/current/security/authentication/dremio-authentication-tokens/) for additional information.

Was this page helpful?

[Previous

Security and Compliance](/current/security/)[Next

Manage Users](/current/security/authentication/users)

* Authentication Methods by Application Type
* Dremio Console Authentication Methods
  + Single Sign-On
  + Username and Password
  + Personal Access Token
* User Applications Authentication Methods
  + External JWT
  + External JWT Exchange
* M2M Applications Authentication Methods
  + OAuth Client Credentials
  + External Service Principal Authentication
* Legacy Authentication Methods
  + Obtain OAuth Access Tokens with Username and Password
  + PAT Exchange
  + Dremio Authentication Token

---

# Source: https://docs.dremio.com/current/security/rbac/

Version: current [26.x]

On this page

# Access Control Enterprise

Dremio allows for the implementation of granular-level privileges, which defines a user/role’s access privilege and available actions for specific objects, such as folders and datasets. This is called access management, and gives administrators the ability to restrict access to any object in Dremio.

* [Privileges](/current/security/rbac/privileges/) – Privileges enable users to perform explicit operations on objects in Dremio. Additionally, privileges may be set on individual datasets (tables or views) or whole schemas, allowing for a simplified configuration with larger catalogs.
* [Row-access and column-masking policies](/current/data-products/govern/row-column-policies-udf/) – Row-access and column-masking policies enable you to grant users access to particular rows or columns.

The following APIs are available for managing access control:

* [Grants APIs](/current/reference/api/catalog/grants/)
* [Privileges API](/current/reference/api/catalog/privileges/)
* [Roles API](/current/reference/api/roles/)
* [Users API](/current/reference/api/user/)

A wide range of SQL commands are also available:

* [Privileges SQL Commands](/current/reference/sql/commands/rbac/)
* [Roles SQL Commands](/current/reference/sql/commands/roles/)
* [Users SQL Commands](/current/reference/sql/commands/users/)

## Object Hierarchy

Each object resides within a container in a hierarchy of containers. The upper-most container exists as the system user, or administrator account. All other objects are contained within sources or spaces, organized into folders. The hierarchy of these objects is illustrated below.

![](/assets/images/rbac-object-hierarchy-a829e25a2980a7f00d7cc2a85ccbbf00.png)

## Inheritance

The objects to which privileges are granted depend on the inheritance model. In other words, granting access to a parent object, such as a folder, also gives that user access to any existing and future datasets contained in that folder. For example, giving a user privileges to ALL DATASETS will only grant the user access to existing datasets, not the folders that contain the datasets. In comparison, granting privileges at the source level will extend that user's access to the source's existing and future folders/schema and datasets. The object to which a user's privileges are applied is also known as the scope, and follow a parent-child relationship.

By the rules of inheritance, user or group access may be granted as high or low in the object hierarchy as you wish for access to reach.

Permissions granted to an individual table or view mean that a user's access only extends to that dataset, not to the parent folder or other datasets created in the same folder. So if a user only needs access to a single dataset, administrators need only grant privileges to that object.

![](/assets/images/rbac-inheritance-5ad539f979430ed0b6b949a9d4a50830.png)

Consider the image above, which shows an example of object structure in Dremio. If a user is granted privileges to a single dataset, such as `TableA1`, then that is the one object they have access to. However, if a user is granted privileges at the folder level, such as `Folder1`, then that user's access extends to any existing and future child objects created, including `FolderA`, `TableA1`, `TableB1`, and so on.

note

If a user has privileges for a single table, they may create views based on that dataset, but with the user now having `ALTER` and `MANAGE GRANTS` privileges for any view. However, the user still retains the same privileges as before with the original dataset. For more information, read View Delegation.

## Scope

Scope is a concept used to describe what objects a user or group has access to. Privileges are assigned by object, which ultimately determines what a grantee may perform set functions upon. For example, you may set a user's scope to `FolderA`, which will give the user access to all existing and future datasets contained in the folder, as well as the datasets' wikis. But they will not have access to any other folders or the source. The object a user is granted access to is dependent on the inheritance model, which means based on the object type, it may contain child objects. For example, if a user is granted privilege to a folder, the user's access also extends to all existing and future datasets contained in that folder.

For example, `user1` is granted the `SELECT` privilege to the folder `FolderC`. This object contains multiple datasets, which the user may now access. However, there exists a parent folder and another subfolder with its own datasets.

![](/assets/images/rbac-scope-55174fe1a171329a6f9194c775e27f77.png)

Because of the established scope, `user1` may not access `FolderD` because they were only granted access to `FolderC`'s objects.

### Current vs. Future Objects

Based on the selected scope, you may restrict a user's access to future and existing datasets. For example, if you select a single table as the scope of a user's privilege, then that user may only perform that action to the existing dataset, as well as any future views they create using that table. However, they may not access any views created from a table by another user (see the example below). However, if the scope is instead set at the folder level, then the user may perform the granted privilege to all tables and views contained in that folder (see the example below).

## Ownership

Object ownership is a security feature used to control access to an object. In Dremio, each object must have an owner, and may have only one owner. Ownership is automatically granted to the user who initially created the object. For example, when `user1` creates an S3 data source, Dremio automatically assigns ownership of the source to `user1`.

The privileges included in object ownership depend on your configuration.

* By default, ownership includes all privileges for that object. The object owner can grant or revoke access privileges to the object and its child objects, modify an object's settings, and delete the object as desired. See Granting Privileges Using SQL Commands for more information.
* Managed access spaces centralize the administration of access privileges in shared spaces to a limited set of users and roles, including the space owner. By limiting privilege grant authority, managed access spaces help ensure consistent and controlled access policies and reduce the risk of unauthorized access. See Managed Access Spaces.

The following behaviors and limitations apply to ownership:

* Each object may only have one owner.
* An object's creator is automatically granted ownership.
* Object ownership may be assigned or modified to a new user or role with the [`GRANT OWNERSHIP`](/current/reference/sql/commands/rbac) command.
* The object's access control settings may not work if the owner is deleted or removed. See View Delegation.
* Object owners may be identified by querying the [`sys."tables"`](/current/reference/sql/system-tables/tables) table or [`sys.views`](/current/reference/sql/system-tables/views) table. If an object has no owner, the `owner_id` will display as `$unowned`.

### Managed Access Spaces

Managed access spaces centralize the administration of access privileges to a limited set of users and roles, including:

* Owner of the space
* Dremio administrator
* Users or roles explicitly granted the MANAGE GRANTS privilege on the object or any of its parents

When using managed access spaces, Dremio displays shared spaces with a lock icon ![](/images/icons/managed-access-icon.png) on the [Datasets](/current/get-started/quick_tour#datasets-page) and [SQL Runner](/current/get-started/quick_tour#sql-runner) pages. Owners of folders, views, and functions in a locked space cannot grant or revoke privileges on those objects to other users or roles.

| User or role | Grants/revokes privileges in default spaces | Grants/revokes privileges in managed access spaces |
| --- | --- | --- |
| Dremio administrator | Yes | Yes |
| Owner of a shared space | Yes | Yes |
| Owner of a folder in a shared space | Yes | No |
| Owner of a view in a shared space | Yes | No |
| Owner of a function in a shared space | Yes | No |
| User or role with MANAGE GRANTS | Yes | Yes |

Managed access spaces do not impact:

* Any user home space
* Sources, including Nessie catalogs
* Global objects, such as scripts and user-defined functions

Managed access spaces do not override a MANAGE GRANT privilege granted at system scope.

The Dremio administrator can activate managed access spaces by setting the `security.access-control.managed-access-spaces.enabled` [support key](/current/help-support/support-settings/#support-keys) on the Support Settings page.

### View Delegation

View delegation means that the data in tables with restricted access may be available to other Dremio users by creating views. View delegation is the critical capability of the Dremio semantic layer that allows users to run queries without accessing the underlying tables and views directly.

The fundamental principles of view delegation include the following:

* The privileges of a view's owner determine whether the view can use dependent tables and views.
* Additional user access to a view is controlled by privilege grants directly on the view, forming a privilege chain from the view to the underlying table.

note

A shared view selects from the underlying dataset using the view owner's permissions at the time of the view's last modification, even if the end user querying the view lacks privileges to modify the underlying table. This applies to each table on the data graph and chain of datasets.

View delegation is different from privilege assignment. View delegation is an implicit delegation of the SELECT privilege on underlying objects, which means that users who run queries on a view must have access privileges on the view but do not need privileges on underlying tables. Privilege assignment is an explicit delegation providing direct access to an object.

#### Example 1: View Delegation

`user1` has the SELECT privilege on `table1` and creates `view1` to filter and transform data in `table1`. `user2` asks for access privileges to run queries on `view1` as well. `user2` may obtain the SELECT privilege for `view1` from the following authorized users:

* By default, view owners such as `user1` can grant and revoke privileges to other users, as appropriate.
* A limited set of users and roles, such as the space owner, can grant or revoke privileges in managed access spaces.
* Dremio administrators or other users with the MANAGE GRANTS privilege can grant privileges to other users.

If access for `user2` is appropriate, the authorized user runs `GRANT SELECT ON VIEW view1 TO USER user2` to grant the SELECT privilege to `user2`. After `user2` obtains the SELECT privilege, they can run queries on `view1`, utilizing the privilege of `user1` as owner to `view1` to SELECT from `table1`.

| Object | `user1` | `user2` |
| --- | --- | --- |
| `view1` | OWNERSHIP | SELECT |
| `table1` | SELECT | None |

*Privileges by user in Example 1*

The following table describes the actions that each user may perform based on their privileges:

| Task | Works for `user1` | Works for `user2` |
| --- | --- | --- |
| Use `view1` in queries | Yes, `user1` owns `view1` and has the SELECT privilege on `table1`. | Yes, `user2` has the SELECT privilege on `view1` and the owner of `view1` has the SELECT privilege on `table1`. |
| Modify the query in `view1` | Yes, `user1` is the owner of `view1`. Ownership includes the ALTER privilege to modify the view definition. | No, `user2` is not the owner of `view1` and does not have the ALTER privilege. |
| Use `table1` in queries | Yes, `user1` has the SELECT privilege on `table1`. | No, `user2` has no privileges on `table1` and cannot see it in the Dremio user interface. |

*Tasks by user in Example 1*

#### Example 2: View Delegation with Revoked Access to the Original Table

To continue the previous example, `user1` has SELECT access to `table1`, which gives `user1` access through `view1`. An administrator revokes the SELECT access of `user1` on `table1`.

| Object | `user1` | `user2` |
| --- | --- | --- |
| `view1` | OWNERSHIP | SELECT |
| `table1` | None | None |

*Privileges by user in Example 2*

The following table describes the actions that each user may perform based on their privileges:

| Task | Works for `user1` | Works for `user2` |
| --- | --- | --- |
| Use `view1` in queries | No, `user1` no longer has SELECT on the underlying `table1`. | No, `user2` no longer has a chain of permission through `user1` to `table1`. |
| Modify the query in `view1` | No, `user1` is the owner of `view1` but any attempts to edit `view1` will fail unless the references to `table1` are removed since `user1` can no longer access `table1`. | No, `user2` is not the owner of `view1` and does not possess the ALTER privilege. |
| Use `table1` in queries | No, `user1` has no privileges on `table1`. | No, `user2` has no privileges on `table1`. |

*Tasks by user in Example 2*

## Privileges

Privileges refer to the defined levels of access or permissions that are assigned to roles or users within Dremio. Privileges determine the operations a user or role can perform on securable objects. Examples of privileges in Dremio include SELECT on a table or view, INSERT on a table, DELETE on a table, CREATE TABLE on a folder, and MANAGE GRANTS on any object.

The assignment of privileges to roles, or users, should be based on the principle of least privilege, where users or roles are given only the minimum privileges required to perform their tasks effectively.

Privileges can be managed using SQL, APIs, or the Dremio Console.

For more information, please refer to [Privileges](/current/security/rbac/privileges).

### Granting Privileges Using the Dremio Console

You can share catalog objects with others in your organization by granting privileges on the objects to users and roles as follows:

1. Locate the desired object.
2. Click ![This is the icon that represents more actions.](/images/icons/settings.png "Settings") or ![This is the icon that represents more actions.](/images/icons/more.png "Icon represents more actions.") depending on the object.
3. In the object settings dialog, select **Privileges** from the settings sidebar.

note

For some object types, the settings dialog automatically opens to display the privilege settings, and you do not need to select the Privileges tab.

4. In the Privileges dialog, in the field under **Add User/Role**, enter the exact names of the users and roles to which you want to grant privileges.

note

Because all users are members of the PUBLIC role, you can use the PUBLIC role to grant privileges to all users.

5. Click **Add to Privileges**.

For each entry in the **Add User/Role** field that matches a user or role in Dremio, a record appears in the USERS/ROLES table.

6. In the USERS/ROLES table, toggle the checkbox for each privilege you want to grant for that user or role. For a description of the privilege, hover over the column name in the USERS/ROLES table. See the example below:

![](/assets/images/privileges-users-table-5eb046e1d2acd0cc1a6d1bd87d3afc35.png)

7. (Optional) Repeat steps 4-6 if you want to add more users or roles and grant them privileges.
8. When finished, click **Save**.

### Revoking Privileges Using the Dremio Console

To revoke user and role privileges, complete the following steps:

1. Locate the desired object.
2. Click ![This is the icon that represents more actions.](/images/icons/settings.png "Settings") or ![This is the icon that represents more actions.](/images/icons/more.png "Icon represents more actions.") depending on the object.
3. In the object settings dialog, select **Privileges** from the settings sidebar.

   note

   For some object types, the settings dialog automatically opens to display the privilege settings, and you do not need to select the Privileges tab.
4. In the USERS/ROLES table, locate the desired user or role record. If the user or role is not listed, then they do not have specific privileges on the object.

   * To revoke some but not all privileges for the user or role, clear the checkboxes in the columns for the privileges you wish to revoke.
   * To revoke all privileges for a user or role, click ![This is the icon that represents more actions.](/images/ellipsis-icon.png) next to the user or role name and select **Remove**.

   For a description of the privilege, hover over the column name in the USERS/ROLES table. See the example below:

![](/assets/images/privileges-users-table-5eb046e1d2acd0cc1a6d1bd87d3afc35.png)

5. When finished, click **Save**.

note

If a user has a specific privilege on an object through their memberships in multiple roles and the privilege is revoked for one of the roles, the user retains the privilege until it is revoked on the same object for all roles to which the user belongs.

tip

You can also grant or revoke privileges using [SQL commands](/current/reference/sql/commands/rbac/) or [APIs](/current/reference/api/catalog/grants/).

### Granting Privileges Using SQL Commands

When granting privileges to users and roles with SQL commands, you may follow one of three methods: granting to a single dataset, granting to ALL DATASETS, and granting to a scope. Examples of these methods may be found under each section.

Each example includes an SQL command. For more information about command syntax, review the [Privileges (GRANT/REVOKE) SQL commands](/current/reference/sql/commands/rbac).

note

Because all users are members of the PUBLIC role, you can use the PUBLIC role to grant privileges to all users.

#### Granting to a Single Dataset

When you have a user that needs access to only one table and no other objects, then you would simply assign them privileges for that dataset (see the example scenario outlined below).

You should use this method if you want to restrict a user's access to any other existing or future datasets.

note

If you're granting the user access to a table, then remember that they'll be able to create views based on that dataset, which that user can then grant access to other users.

##### Example: Single Dataset

You have a user that you only want to give access to an individual table. You would need to navigate to the *Privileges* screen from that dataset's settings and grant the user the `SELECT` privilege, or perform the following command from the SQL Editor:

Single dataset example

```
GRANT SELECT ON TABLE TableA1 TO USER user1
```

The image below illustrates the objects `user1` now has access to.

![](/assets/images/rbac-privilege-1-ab4d9d59f7940dddc05d90ba62556db9.png)

This restricts `user1` so that they may only access the `TableA1` table, not any other datasets contained in the same folder. However, `user1` may still create views based on `TableA1`.

#### Granting to ALL DATASETS

When you have a user that needs access to all existing datasets, then you would use the SQL syntax `ON ALL DATASETS` (see the example scenario outlined below). This gives the user access to all existing datasets. The user would not, however, automatically receive access to any future datasets created by other users.

You should use this method of privilege assignment if you want to restrict a user's access to parent objects, but still wish for them to have access to all existing datasets.

##### Example: All Datasets

You have a specific user that needs access to all datasets in a specific folder, but they do not require privileges for the folders containing these tables. You would then execute the following command from the SQL Editor:

All datasets example

```
GRANT SELECT ON ALL DATASETS IN SYSTEM TO USER user1
```

The image below illustrates the objects `user1` now has access to.

![](/assets/images/rbac-privilege-2-22c128dbaec6b244cca0f812b40f7d06.png)

This command restricts the scope of `user1` to all datasets presently found in `source1`, such as `TableC1` and `TableD1`. Should additional datasets be created in the future, `user1` will not have access to them.

#### Granting to a Scope

When you want to grant a user access to a parent object, such as a folder, this will also grant the user access to any datasets contained (see the example scenario outlined below).

You should use this method of privilege management if you wanted to grant a user access to all existing and future datasets contained under a parent object.

##### Example: Scope

This method grants a user access to all existing and future datasets contained under a specified object. To accomplish this, you need to navigate to the *Privileges* screen from that folder's settings and grant the user the `SELECT` privilege, or execute the following command from the SQL Editor:

Scope example

```
GRANT SELECT ON FOLDER Folder3 TO USER user1
```

The image below illustrates the objects `user1` now has access to.

![](/assets/images/rbac-privilege-3-121f99249e16dfe376040d3c4cae2b40.png)

This grants `user1` the `SELECT` privilege on `Folder3`, which means they now have access to all existing and future datasets contained in that folder and its subfolders.

Was this page helpful?

[Previous

Personal Access Tokens](/current/security/authentication/personal-access-tokens)[Next

Privileges](/current/security/rbac/privileges)

* Object Hierarchy
* Inheritance
* Scope
  + Current vs. Future Objects
* Ownership
  + Managed Access Spaces
  + View Delegation
* Privileges
  + Granting Privileges Using the Dremio Console
  + Revoking Privileges Using the Dremio Console
  + Granting Privileges Using SQL Commands

---

# Source: https://docs.dremio.com/current/security/integrations/

Version: current [26.x]

# Integrations with Third-Party Access Control and Data Governance Platforms Enterprise

Dremio supports the following third-party integrations for managing access control and data governance:

* [AWS Lake Formation](/current/security/integrations/lake-formation/)
* [Privacera](/current/security/integrations/integrations/privacera)
* [Apache Ranger: Row-Level Filtering & Column-Masking](/current/security/integrations/row-column-policies-ranger)

Was this page helpful?

[Previous

Inbound Impersonation](/current/security/rbac/inbound-impersonation)[Next

AWS Lake Formation](/current/security/integrations/lake-formation/)

---

# Source: https://docs.dremio.com/current/security/secrets-management/

Version: current [26.x]

# Secrets Management Enterprise

When you connect to data sources in Dremio or list secrets in Dremio configuration files, you can use a secrets management service to provide sensitive information like passwords and secret access keys instead of providing it in plaintext. When Dremio needs the value of one of these secrets to authenticate to a data source or another service, Dremio retrieves the value directly from the secrets management service using the secret reference you provide.

Dremio supports the following secrets management providers:

* [AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager/)
* [Azure Key Vault](/current/security/secrets-management/azure-key-vault/)
* [HashiCorp Vault](/current/security/secrets-management/hashicorp-vault/)

Was this page helpful?

[Previous

Apache Ranger](/current/security/integrations/row-column-policies-ranger)[Next

AWS Secrets Manager](/current/security/secrets-management/aws-secrets-manager)

---

# Source: https://docs.dremio.com/current/security/auditing/

Version: current [26.x]

On this page

# Audit Logging Enterprise

For organizations subject to compliance and regulation where auditing is regularly required, Dremio offers full audit logging, wherein all user activities performed within Dremio are tracked and traceable via the `audit.json` file. Each time a user performs an action within Dremio, such as logging in or creating a view, the audit log captures the user's ID and username, objects affected, action performed, event type, SQL statements used, and more.

Audit logging is enabled by default and is available only to users with administrative rights at the System level.

## Audit Log Location

The log-file location may be configured via the `dremio.log.path` property in the [`dremio-env` file](/current/deploy-dremio/other-options/standalone/dremio-config/dremio-env/). You can specify their location, size, and rotation schedule.

## Tracked Events and Actions

Dremio supports audit logging for the following objects (event types) and actions:

| Event Type | Actions |
| --- | --- |
| AI\_AGENT | REQUEST, RESPONSE |
| AUTHENTICATION | LOGIN |
| ENGINE | CREATE\_STARTED, UPDATE\_STARTED, DELETE\_STARTED |
| ENGINE\_CONFIG | CREATE, UPDATE, DELETE, START, STOP, SCALE\_UP, SCALE\_DOWN |
| ENGINE\_SCALING | SCALE\_UP\_STARTED, SCALE\_DOWN\_STARTED |
| FOLDER | CREATE, UPDATE, DELETE |
| LABEL | CREATE, UPDATE, DELETE |
| MODEL\_PROVIDER\_CONFIG | CREATE, UPDATE, DELETE, SET\_DEFAULT |
| PERSONAL\_ACCESS\_TOKEN | CREATE, DELETE |
| PHYSICAL\_DATASET | CREATE, UPDATE, DELETE |
| PRIVILEGE | UPDATE, DELETE |
| QUEUE | CREATE, UPDATE, DELETE |
| REFLECTION | CREATE, UPDATE, DELETE |
| ROLE | CREATE, UPDATE, DELETE |
| SOURCE | CREATE, UPDATE, DELETE |
| SPACE | CREATE, UPDATE, DELETE |
| SUPPORT\_SETTING | RESET, SET |
| UDF | CREATE, UPDATE, DELETE |
| USER\_ACCOUNT | CREATE, UPDATE, DELETE |
| VIRTUAL\_DATASET | CREATE, RENAME, UPDATE, DELETE |
| WIKI | CREATE, EDIT, DELETE |

## Audit Log Format

Audit logs include the following information in JSON format:

| Key | Value |
| --- | --- |
| `timestamp` | The date and time when the event was recorded. |
| `userId` | The ID value associated with the user's account.  The following values are placeholders that represent internal system users, which Dremio uses to log events before the user authenticates: `1` and `678cc92c-01ed-4db3-9a28-d1f871042d9f`. |
| `userName` | The username associated with the user account (which is typically used to log in). |
| `status` | The status of the action, which is typically used to indicate whether the event was approved or allowed. |
| `eventType` | The object or scope of the interaction that occurred. |
| `action` | The actual activity performed within the specified scope.  This varies based on the `eventType`, but most often would be `CREATE`, `DELETE`, and `UPDATE`. |
| `details` | The data altered or created.  This varies based on the `eventType`. |

### Audit Log Examples

The following examples show the types of audit records that Dremio captures and the information included in an audit entry for each event type.

* AUTHENTICATION
* ENGINE
* REFLECTION
* VIRTUAL\_DATASET

User `dremio` logged in on the Dremio application.

The audit log would have the following information:

Authentication log

```
{  
  "timestamp": "2021-11-23 16:30:53,400",  
  "userContext": {  
    "userId": "1",  
    "userName": "$dremio$"  
  },  
  "status": "OK",  
  "eventType": "AUTHENTICATION",  
  "action": "LOGIN",  
  "details": {  
    "userName": "dremio",  
    "userId": "",  
    "source": "FLIGHT"  
  }  
}
```

User `dremio` created an engine called `preview`.

The audit log would have the following information:

Engine log

```
{  
  "timestamp": "2025-04-07 13:25:41,193",  
  "userContext": {  
    "userId": "b8c3f553-93ca-4b6b-95dc-4d6c03cdb58f",  
    "userName": "dremio"  
  },  
  "status": "OK",  
  "eventType": "ENGINE",  
  "action": "CREATE_STARTED",  
  "details": {  
    "engineId": "541bf413-b66d-4fc0-8e33-e103efdf6bdc",  
    "engineName": "preview",  
    "engineSize": "2XSmall",  
    "resourceAllocationOffset": "reserve-2-8",  
    "targetCpuCapacity": "16C"  
    "autoStopDelaySecs": 3600,  
  }  
}
```

User `dremio` created a Reflection called `Raw Reflection (1)` in the Dremio console.

The audit log would have the following information:

Reflection log

```
{  
  "timestamp": "2021-11-22 10:06:38,432",  
  "userContext": {  
    "userId": "6ab04602-410b-4031-87ae-2d3d5f7dc",  
    "userName": "dremio"  
  },  
  "status": "OK",  
  "eventType": "REFLECTION",  
  "action": "CREATE",  
  "details": {  
    "reflectionId": "a5251b05-4873-4a9d-a008-303eeeeed",  
    "name": "Raw Reflection (1)",  
    "dataset": "7e3d4a8a-b92d-41ab-96dc-6a76a6248",  
    "type": "RAW",  
    "sortColumns": [  
      {  
        "name": "fare_amount"  
      }  
    ],  
    "partitionColumns": [  
      {  
        "name": "passenger_count"  
      }  
    ],  
    "distributionColumns": [],  
    "dimensions": [],  
    "measures": [],  
    "displayColumns": [  
      {  
        "name": "passenger_count"  
      },  
      {  
        "name": "pickup_datetime"  
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
    "partitiondistributionstrategy": "CONSOLIDATED",  
    "arrowCachingEnabled": false,  
    "targetDataset": ""  
  }  
}
```

User `dremio` issued a SQL command to `CREATE` a view in Dremio's SQL editor.

The audit log would have the following information:

View (virtual dataset) log

```
{  
  "timestamp": "2021-11-17 14:31:43,594",  
  "userContext": {  
    "userId": "4a3ea2fa-a3f6-4adb-8852-041a28cac",  
    "userName": "dremio"  
  },  
  "status": "OK",  
  "eventType": "VIRTUAL_DATASET",  
  "action": "CREATE",  
  "details": {  
    "id": "da08848d-d80d-4414-aaf4-40ce866ea",  
    "name": "a_employees",  
    "tag": "gwN/p7E5E1Q=",  
    "path": "myView.a_employees",  
    "sql": "SELECT \"firstname\", \"zipcode\"\nFROM \"local-msql\".\"dremio_db1\".\"Employees\"\nWHERE \"zipcode\" LIKE 'a%'",  
    "sqlContext": "myView",  
    "fields": [  
      {  
        "name": "firstname",  
        "dataType": "TEXT"  
      },  
      {  
        "name": "zipcode",  
        "dataType": "TEXT"  
      }  
    ],  
    "oldName": "",  
    "oldPath": ""  
  }  
}
```

Was this page helpful?

[Previous

HashiCorp Vault](/current/security/secrets-management/hashicorp-vault)[Next

Compliance](/current/security/compliance)

* Audit Log Location
* Tracked Events and Actions
* Audit Log Format
  + Audit Log Examples

---

# Source: https://docs.dremio.com/current/security/compliance

Version: current [26.x]

On this page

# Regulatory Compliance

Dremio meets the IT control requirements for several compliance frameworks and certifications, as described below.

As the [Dremio Shared Responsibility Models](/responsibility) outline, compliance is a shared responsibility between Dremio and you. The Shared Responsibility Models lay out Dremio's responsibilities for providing standards and compliance and your responsibilities for adhering to those standards.

## SOC 2 Type II Report

Dremio maintains compliance with the American Institute of Certified Public Accountants (AICPA) System and Organization Controls - Trust Services Criteria, commonly known as SOC 2.

### Key Benefits

[SOC 2 Type II reports](https://us.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report) provide an in-depth analysis of cloud service providers regarding the safeguards a company uses to protect customer data and how these controls are performing overall. These reports are issued by independent, third-party auditors and cover the key points of Security, Availability, Confidentiality, and Privacy.

This independent assessment of Dremio Software provides a detailed report regarding the environments used to provide security and privacy of customer data overall. The report provide descriptions of these controls, the tests performed to assess their effectiveness, the results of said tests, and then an overall opinion regarding the design and operational effectiveness of the environments.

## ISO 27001 Certification

ISO 27001 is an internationally recognized specification for an Information Security Management System (ISMS). ISO 27001 is the only auditable standard that deals with the overall management of information security, rather than just which technical controls to implement.

### Key Benefits

Obtaining [ISO 27001:2022 certification](https://www.iso.org/isoiec-27001-information-security.html) demonstrates that Dremio employs a comprehensive framework of legal, physical, and technical controls for information risk management.

## GDPR Compliance

Dremio is compliant with the storage and security of its data according to Article 27 of the General Data Protection Regulation (GDPR). Please see [Dremio's Privacy Policy](https://www.dremio.com/legal/privacy-policy/) for additional information regarding our appointed European Data Protection Office (EDPO) in the EU.

### Key Benefits

As part of the European Union, specific regulations exist that require companies to [maintain compliance with GDPR](https://gdpr.org/). This governs the way user data is stored, processed, and utilized on Dremio Software. Specifically, this prevents the exploitation of user data and standardizes the data protection laws that services must follow throughout Europe.

## CCPA Compliance

Dremio maintains compliance with the California Consumer Privacy Act (CCPA), which regulates the handling of personal data and prevents any unauthorized use or sale. Please see [Dremio's Privacy Notice For California Residents](https://www.dremio.com/legal/privacy-policy/) for additional information.

### Key Benefits

Adherence to [CCPA](https://oag.ca.gov/privacy/ccpa) by an organization ensures that California residents have the right to opt out of having their data sold to third parties, request disclosure of data collected, and request deletion of said data.

## HIPAA Compliance

Dremio is compliant with the Health Insurance Portability and Accountability Act (HIPAA), a series of federal regulatory standards that outline the lawful use and disclosure of protected health information in the United States. HIPAA compliance is regulated by the Department of Health and Human Services (HHS) and enforced by the Office for Civil Rights (OCR).

### Key Benefits

Adherence to [HIPAA](https://www.cdc.gov/phlp/publications/topic/hipaa.html) ensures that healthcare providers, health plans, healthcare clearinghouses, and business associates of HIPAA-covered entities must implement multiple safeguards to protect sensitive personal and health information.

Was this page helpful?

[Previous

Audit Logging](/current/security/auditing/)[Next

Administration](/current/admin/)

* SOC 2 Type II Report
  + Key Benefits
* ISO 27001 Certification
  + Key Benefits
* GDPR Compliance
  + Key Benefits
* CCPA Compliance
  + Key Benefits
* HIPAA Compliance
  + Key Benefits

---

# Source: https://docs.dremio.com/current/security/rbac

Version: current [26.x]

On this page

# Access Control Enterprise

Dremio allows for the implementation of granular-level privileges, which defines a user/role’s access privilege and available actions for specific objects, such as folders and datasets. This is called access management, and gives administrators the ability to restrict access to any object in Dremio.

* [Privileges](/current/security/rbac/privileges/) – Privileges enable users to perform explicit operations on objects in Dremio. Additionally, privileges may be set on individual datasets (tables or views) or whole schemas, allowing for a simplified configuration with larger catalogs.
* [Row-access and column-masking policies](/current/data-products/govern/row-column-policies-udf/) – Row-access and column-masking policies enable you to grant users access to particular rows or columns.

The following APIs are available for managing access control:

* [Grants APIs](/current/reference/api/catalog/grants/)
* [Privileges API](/current/reference/api/catalog/privileges/)
* [Roles API](/current/reference/api/roles/)
* [Users API](/current/reference/api/user/)

A wide range of SQL commands are also available:

* [Privileges SQL Commands](/current/reference/sql/commands/rbac/)
* [Roles SQL Commands](/current/reference/sql/commands/roles/)
* [Users SQL Commands](/current/reference/sql/commands/users/)

## Object Hierarchy

Each object resides within a container in a hierarchy of containers. The upper-most container exists as the system user, or administrator account. All other objects are contained within sources or spaces, organized into folders. The hierarchy of these objects is illustrated below.

![](/assets/images/rbac-object-hierarchy-a829e25a2980a7f00d7cc2a85ccbbf00.png)

## Inheritance

The objects to which privileges are granted depend on the inheritance model. In other words, granting access to a parent object, such as a folder, also gives that user access to any existing and future datasets contained in that folder. For example, giving a user privileges to ALL DATASETS will only grant the user access to existing datasets, not the folders that contain the datasets. In comparison, granting privileges at the source level will extend that user's access to the source's existing and future folders/schema and datasets. The object to which a user's privileges are applied is also known as the scope, and follow a parent-child relationship.

By the rules of inheritance, user or group access may be granted as high or low in the object hierarchy as you wish for access to reach.

Permissions granted to an individual table or view mean that a user's access only extends to that dataset, not to the parent folder or other datasets created in the same folder. So if a user only needs access to a single dataset, administrators need only grant privileges to that object.

![](/assets/images/rbac-inheritance-5ad539f979430ed0b6b949a9d4a50830.png)

Consider the image above, which shows an example of object structure in Dremio. If a user is granted privileges to a single dataset, such as `TableA1`, then that is the one object they have access to. However, if a user is granted privileges at the folder level, such as `Folder1`, then that user's access extends to any existing and future child objects created, including `FolderA`, `TableA1`, `TableB1`, and so on.

note

If a user has privileges for a single table, they may create views based on that dataset, but with the user now having `ALTER` and `MANAGE GRANTS` privileges for any view. However, the user still retains the same privileges as before with the original dataset. For more information, read View Delegation.

## Scope

Scope is a concept used to describe what objects a user or group has access to. Privileges are assigned by object, which ultimately determines what a grantee may perform set functions upon. For example, you may set a user's scope to `FolderA`, which will give the user access to all existing and future datasets contained in the folder, as well as the datasets' wikis. But they will not have access to any other folders or the source. The object a user is granted access to is dependent on the inheritance model, which means based on the object type, it may contain child objects. For example, if a user is granted privilege to a folder, the user's access also extends to all existing and future datasets contained in that folder.

For example, `user1` is granted the `SELECT` privilege to the folder `FolderC`. This object contains multiple datasets, which the user may now access. However, there exists a parent folder and another subfolder with its own datasets.

![](/assets/images/rbac-scope-55174fe1a171329a6f9194c775e27f77.png)

Because of the established scope, `user1` may not access `FolderD` because they were only granted access to `FolderC`'s objects.

### Current vs. Future Objects

Based on the selected scope, you may restrict a user's access to future and existing datasets. For example, if you select a single table as the scope of a user's privilege, then that user may only perform that action to the existing dataset, as well as any future views they create using that table. However, they may not access any views created from a table by another user (see the example below). However, if the scope is instead set at the folder level, then the user may perform the granted privilege to all tables and views contained in that folder (see the example below).

## Ownership

Object ownership is a security feature used to control access to an object. In Dremio, each object must have an owner, and may have only one owner. Ownership is automatically granted to the user who initially created the object. For example, when `user1` creates an S3 data source, Dremio automatically assigns ownership of the source to `user1`.

The privileges included in object ownership depend on your configuration.

* By default, ownership includes all privileges for that object. The object owner can grant or revoke access privileges to the object and its child objects, modify an object's settings, and delete the object as desired. See Granting Privileges Using SQL Commands for more information.
* Managed access spaces centralize the administration of access privileges in shared spaces to a limited set of users and roles, including the space owner. By limiting privilege grant authority, managed access spaces help ensure consistent and controlled access policies and reduce the risk of unauthorized access. See Managed Access Spaces.

The following behaviors and limitations apply to ownership:

* Each object may only have one owner.
* An object's creator is automatically granted ownership.
* Object ownership may be assigned or modified to a new user or role with the [`GRANT OWNERSHIP`](/current/reference/sql/commands/rbac) command.
* The object's access control settings may not work if the owner is deleted or removed. See View Delegation.
* Object owners may be identified by querying the [`sys."tables"`](/current/reference/sql/system-tables/tables) table or [`sys.views`](/current/reference/sql/system-tables/views) table. If an object has no owner, the `owner_id` will display as `$unowned`.

### Managed Access Spaces

Managed access spaces centralize the administration of access privileges to a limited set of users and roles, including:

* Owner of the space
* Dremio administrator
* Users or roles explicitly granted the MANAGE GRANTS privilege on the object or any of its parents

When using managed access spaces, Dremio displays shared spaces with a lock icon ![](/images/icons/managed-access-icon.png) on the [Datasets](/current/get-started/quick_tour#datasets-page) and [SQL Runner](/current/get-started/quick_tour#sql-runner) pages. Owners of folders, views, and functions in a locked space cannot grant or revoke privileges on those objects to other users or roles.

| User or role | Grants/revokes privileges in default spaces | Grants/revokes privileges in managed access spaces |
| --- | --- | --- |
| Dremio administrator | Yes | Yes |
| Owner of a shared space | Yes | Yes |
| Owner of a folder in a shared space | Yes | No |
| Owner of a view in a shared space | Yes | No |
| Owner of a function in a shared space | Yes | No |
| User or role with MANAGE GRANTS | Yes | Yes |

Managed access spaces do not impact:

* Any user home space
* Sources, including Nessie catalogs
* Global objects, such as scripts and user-defined functions

Managed access spaces do not override a MANAGE GRANT privilege granted at system scope.

The Dremio administrator can activate managed access spaces by setting the `security.access-control.managed-access-spaces.enabled` [support key](/current/help-support/support-settings/#support-keys) on the Support Settings page.

### View Delegation

View delegation means that the data in tables with restricted access may be available to other Dremio users by creating views. View delegation is the critical capability of the Dremio semantic layer that allows users to run queries without accessing the underlying tables and views directly.

The fundamental principles of view delegation include the following:

* The privileges of a view's owner determine whether the view can use dependent tables and views.
* Additional user access to a view is controlled by privilege grants directly on the view, forming a privilege chain from the view to the underlying table.

note

A shared view selects from the underlying dataset using the view owner's permissions at the time of the view's last modification, even if the end user querying the view lacks privileges to modify the underlying table. This applies to each table on the data graph and chain of datasets.

View delegation is different from privilege assignment. View delegation is an implicit delegation of the SELECT privilege on underlying objects, which means that users who run queries on a view must have access privileges on the view but do not need privileges on underlying tables. Privilege assignment is an explicit delegation providing direct access to an object.

#### Example 1: View Delegation

`user1` has the SELECT privilege on `table1` and creates `view1` to filter and transform data in `table1`. `user2` asks for access privileges to run queries on `view1` as well. `user2` may obtain the SELECT privilege for `view1` from the following authorized users:

* By default, view owners such as `user1` can grant and revoke privileges to other users, as appropriate.
* A limited set of users and roles, such as the space owner, can grant or revoke privileges in managed access spaces.
* Dremio administrators or other users with the MANAGE GRANTS privilege can grant privileges to other users.

If access for `user2` is appropriate, the authorized user runs `GRANT SELECT ON VIEW view1 TO USER user2` to grant the SELECT privilege to `user2`. After `user2` obtains the SELECT privilege, they can run queries on `view1`, utilizing the privilege of `user1` as owner to `view1` to SELECT from `table1`.

| Object | `user1` | `user2` |
| --- | --- | --- |
| `view1` | OWNERSHIP | SELECT |
| `table1` | SELECT | None |

*Privileges by user in Example 1*

The following table describes the actions that each user may perform based on their privileges:

| Task | Works for `user1` | Works for `user2` |
| --- | --- | --- |
| Use `view1` in queries | Yes, `user1` owns `view1` and has the SELECT privilege on `table1`. | Yes, `user2` has the SELECT privilege on `view1` and the owner of `view1` has the SELECT privilege on `table1`. |
| Modify the query in `view1` | Yes, `user1` is the owner of `view1`. Ownership includes the ALTER privilege to modify the view definition. | No, `user2` is not the owner of `view1` and does not have the ALTER privilege. |
| Use `table1` in queries | Yes, `user1` has the SELECT privilege on `table1`. | No, `user2` has no privileges on `table1` and cannot see it in the Dremio user interface. |

*Tasks by user in Example 1*

#### Example 2: View Delegation with Revoked Access to the Original Table

To continue the previous example, `user1` has SELECT access to `table1`, which gives `user1` access through `view1`. An administrator revokes the SELECT access of `user1` on `table1`.

| Object | `user1` | `user2` |
| --- | --- | --- |
| `view1` | OWNERSHIP | SELECT |
| `table1` | None | None |

*Privileges by user in Example 2*

The following table describes the actions that each user may perform based on their privileges:

| Task | Works for `user1` | Works for `user2` |
| --- | --- | --- |
| Use `view1` in queries | No, `user1` no longer has SELECT on the underlying `table1`. | No, `user2` no longer has a chain of permission through `user1` to `table1`. |
| Modify the query in `view1` | No, `user1` is the owner of `view1` but any attempts to edit `view1` will fail unless the references to `table1` are removed since `user1` can no longer access `table1`. | No, `user2` is not the owner of `view1` and does not possess the ALTER privilege. |
| Use `table1` in queries | No, `user1` has no privileges on `table1`. | No, `user2` has no privileges on `table1`. |

*Tasks by user in Example 2*

## Privileges

Privileges refer to the defined levels of access or permissions that are assigned to roles or users within Dremio. Privileges determine the operations a user or role can perform on securable objects. Examples of privileges in Dremio include SELECT on a table or view, INSERT on a table, DELETE on a table, CREATE TABLE on a folder, and MANAGE GRANTS on any object.

The assignment of privileges to roles, or users, should be based on the principle of least privilege, where users or roles are given only the minimum privileges required to perform their tasks effectively.

Privileges can be managed using SQL, APIs, or the Dremio Console.

For more information, please refer to [Privileges](/current/security/rbac/privileges).

### Granting Privileges Using the Dremio Console

You can share catalog objects with others in your organization by granting privileges on the objects to users and roles as follows:

1. Locate the desired object.
2. Click ![This is the icon that represents more actions.](/images/icons/settings.png "Settings") or ![This is the icon that represents more actions.](/images/icons/more.png "Icon represents more actions.") depending on the object.
3. In the object settings dialog, select **Privileges** from the settings sidebar.

note

For some object types, the settings dialog automatically opens to display the privilege settings, and you do not need to select the Privileges tab.

4. In the Privileges dialog, in the field under **Add User/Role**, enter the exact names of the users and roles to which you want to grant privileges.

note

Because all users are members of the PUBLIC role, you can use the PUBLIC role to grant privileges to all users.

5. Click **Add to Privileges**.

For each entry in the **Add User/Role** field that matches a user or role in Dremio, a record appears in the USERS/ROLES table.

6. In the USERS/ROLES table, toggle the checkbox for each privilege you want to grant for that user or role. For a description of the privilege, hover over the column name in the USERS/ROLES table. See the example below:

![](/assets/images/privileges-users-table-5eb046e1d2acd0cc1a6d1bd87d3afc35.png)

7. (Optional) Repeat steps 4-6 if you want to add more users or roles and grant them privileges.
8. When finished, click **Save**.

### Revoking Privileges Using the Dremio Console

To revoke user and role privileges, complete the following steps:

1. Locate the desired object.
2. Click ![This is the icon that represents more actions.](/images/icons/settings.png "Settings") or ![This is the icon that represents more actions.](/images/icons/more.png "Icon represents more actions.") depending on the object.
3. In the object settings dialog, select **Privileges** from the settings sidebar.

   note

   For some object types, the settings dialog automatically opens to display the privilege settings, and you do not need to select the Privileges tab.
4. In the USERS/ROLES table, locate the desired user or role record. If the user or role is not listed, then they do not have specific privileges on the object.

   * To revoke some but not all privileges for the user or role, clear the checkboxes in the columns for the privileges you wish to revoke.
   * To revoke all privileges for a user or role, click ![This is the icon that represents more actions.](/images/ellipsis-icon.png) next to the user or role name and select **Remove**.

   For a description of the privilege, hover over the column name in the USERS/ROLES table. See the example below:

![](/assets/images/privileges-users-table-5eb046e1d2acd0cc1a6d1bd87d3afc35.png)

5. When finished, click **Save**.

note

If a user has a specific privilege on an object through their memberships in multiple roles and the privilege is revoked for one of the roles, the user retains the privilege until it is revoked on the same object for all roles to which the user belongs.

tip

You can also grant or revoke privileges using [SQL commands](/current/reference/sql/commands/rbac/) or [APIs](/current/reference/api/catalog/grants/).

### Granting Privileges Using SQL Commands

When granting privileges to users and roles with SQL commands, you may follow one of three methods: granting to a single dataset, granting to ALL DATASETS, and granting to a scope. Examples of these methods may be found under each section.

Each example includes an SQL command. For more information about command syntax, review the [Privileges (GRANT/REVOKE) SQL commands](/current/reference/sql/commands/rbac).

note

Because all users are members of the PUBLIC role, you can use the PUBLIC role to grant privileges to all users.

#### Granting to a Single Dataset

When you have a user that needs access to only one table and no other objects, then you would simply assign them privileges for that dataset (see the example scenario outlined below).

You should use this method if you want to restrict a user's access to any other existing or future datasets.

note

If you're granting the user access to a table, then remember that they'll be able to create views based on that dataset, which that user can then grant access to other users.

##### Example: Single Dataset

You have a user that you only want to give access to an individual table. You would need to navigate to the *Privileges* screen from that dataset's settings and grant the user the `SELECT` privilege, or perform the following command from the SQL Editor:

Single dataset example

```
GRANT SELECT ON TABLE TableA1 TO USER user1
```

The image below illustrates the objects `user1` now has access to.

![](/assets/images/rbac-privilege-1-ab4d9d59f7940dddc05d90ba62556db9.png)

This restricts `user1` so that they may only access the `TableA1` table, not any other datasets contained in the same folder. However, `user1` may still create views based on `TableA1`.

#### Granting to ALL DATASETS

When you have a user that needs access to all existing datasets, then you would use the SQL syntax `ON ALL DATASETS` (see the example scenario outlined below). This gives the user access to all existing datasets. The user would not, however, automatically receive access to any future datasets created by other users.

You should use this method of privilege assignment if you want to restrict a user's access to parent objects, but still wish for them to have access to all existing datasets.

##### Example: All Datasets

You have a specific user that needs access to all datasets in a specific folder, but they do not require privileges for the folders containing these tables. You would then execute the following command from the SQL Editor:

All datasets example

```
GRANT SELECT ON ALL DATASETS IN SYSTEM TO USER user1
```

The image below illustrates the objects `user1` now has access to.

![](/assets/images/rbac-privilege-2-22c128dbaec6b244cca0f812b40f7d06.png)

This command restricts the scope of `user1` to all datasets presently found in `source1`, such as `TableC1` and `TableD1`. Should additional datasets be created in the future, `user1` will not have access to them.

#### Granting to a Scope

When you want to grant a user access to a parent object, such as a folder, this will also grant the user access to any datasets contained (see the example scenario outlined below).

You should use this method of privilege management if you wanted to grant a user access to all existing and future datasets contained under a parent object.

##### Example: Scope

This method grants a user access to all existing and future datasets contained under a specified object. To accomplish this, you need to navigate to the *Privileges* screen from that folder's settings and grant the user the `SELECT` privilege, or execute the following command from the SQL Editor:

Scope example

```
GRANT SELECT ON FOLDER Folder3 TO USER user1
```

The image below illustrates the objects `user1` now has access to.

![](/assets/images/rbac-privilege-3-121f99249e16dfe376040d3c4cae2b40.png)

This grants `user1` the `SELECT` privilege on `Folder3`, which means they now have access to all existing and future datasets contained in that folder and its subfolders.

Was this page helpful?

[Previous

Personal Access Tokens](/current/security/authentication/personal-access-tokens)[Next

Privileges](/current/security/rbac/privileges)

* Object Hierarchy
* Inheritance
* Scope
  + Current vs. Future Objects
* Ownership
  + Managed Access Spaces
  + View Delegation
* Privileges
  + Granting Privileges Using the Dremio Console
  + Revoking Privileges Using the Dremio Console
  + Granting Privileges Using SQL Commands

---

# Source: https://docs.dremio.com/current/security/integrations/lake-formation/

Version: current [26.x]

On this page

# Integrate with AWS Lake Formation Enterprise

Lake Formation provides access controls for datasets in the AWS Glue Data Catalog and is used to define security policies from a centralized location that may be shared across multiple tools. Dremio may be configured to refer to this service to verify access for a user to contained datasets.

## Requirements

* [Dremio v19.0+](/current/release-notes/version-1900-release-notes/#lake-formation)
* Identity Provider service (e.g., Microsoft Entra ID, [LDAP](/current/security/authentication/ldap/)) set up
  + (Recommended) [SAML connection](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html) with AWS
* [Permissions set up in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html)
* [AWS Glue Data Catalog](/current/data-sources/lakehouse-catalogs/aws-glue-catalog/) connected to Dremio
  + User and Group ARN prefixes specified and enabled

## Lake Formation Workflow

When Lake Formation is properly configured, Dremio adheres to the following workflow each time an end user attempts to access, edit, or query datasets with managed privileges:

1. Dremio enforces [access control](/current/security/rbac/). See Configuring Sources for Lake Formation below for access control recommendations.
2. Dremio checks each table to determine if those stored in the AWS Glue source are configured to use Lake Formation for security.
   * If one or more datasets leverage Lake Formation, Dremio determines the user ARNs to use when checking against Lake Formation.
3. Dremio queries Lake Formation to determine a user's access level to the datasets using the user/group ARNs.
   * If the user has access to the datasets specified within the query's scope, the query proceeds.
   * If the user lacks access, the query fails with a permission error.

## Demoing Lake Formation

[Demo files and a walkthrough](/current/security/integrations/lake-formation/lake-formation-demo/) are available to help you test Lake Formation functionality. The demo files and walkthrough are intended for users who have not configured all of the requirements listed above.

## Configuring Sources for Lake Formation

Lake Formation integration is dependent on the mapping of user/group names in Dremio to the IAM user/group ARNs used by AWS.

To configure an existing or new AWS Glue source, you must set the following options:

1. From your existing source or upon creating an **AWS Glue Catalog** source, navigate to the Advanced Options tab.
2. Enable **Enforce AWS Lake Formation access permissions on datasets**.
3. Fill in the user and group prefix settings as instructed with the [Lake Formation Permissions Reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html). For example, if you are using a SAML provider in AWS:
   * User prefix with SAML: `arn:aws:iam::<AWS_ACCOUNT_ID>:saml-provider/<PROVIDER_NAME_IN_AWS>:user/`
   * Group prefix with SAML: `arn:aws:iam::<AWS_ACCOUNT_ID>:saml-provider/<PROVIDER_NAME_IN_AWS>:group/`

   note

   Best Practice: On the Privileges tab, we recommend enabling the **Select** privilege for **All Users** to allow non-admin users to access the AWS Glue source from Dremio.
4. Click **Save**.

## Lake Formation Cell-Level Security

Dremio supports AWS Lake Formation [cell-level security](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) with row-level access permissions based on AWS Lake Formation [PartiQL expressions](https://docs.aws.amazon.com/lake-formation/latest/dg/partiql-support.html). If the user does not have read permissions on a column or cell, Dremio masks the data in that column or cell with a `NULL` value.

To speed up query planning, Dremio uses the AWS Lake Formation permissions cache for each table. By default, the cache is enabled and reuses previously loaded permissions for up to 3600 seconds (1 hour).

Use [support keys](/current/help-support/support-settings/#support-keys) to disable the cache or customize the cache time-to-live (TTL):

* `dremio.glue.lakeformation.cache.enable`: To disable permissions caching, set to `FALSE`.
* `dremio.glue.lakeformation.cache.ttl`: To specify a TTL for the cache instead of the default 3600 seconds, set to the desired value in seconds.

After you change the value for either support key, you must restart the coordinator node in your Dremio cluster for the change to take effect.

Was this page helpful?

[Previous

Integrations](/current/security/integrations/)[Next

Lake Formation Demo](/current/security/integrations/lake-formation/lake-formation-demo)

* Requirements
* Lake Formation Workflow
* Demoing Lake Formation
* Configuring Sources for Lake Formation
* Lake Formation Cell-Level Security

---

# Source: https://docs.dremio.com/current/security/integrations/privacera/

Version: current [26.x]

On this page

# Integrate with Privacera Enterprise

Dremio and Privacera have partnered to provide an integration that allows organizations to implement fine-grained access controls on their open data lakehouse. The integration provides the following capabilities:

* **Privacera Policy Sync:** Data governance and access control policies in Privacera are translated into SQL and pushed to Dremio using Dremio’s native RBAC and fine-grained access control, ensuring that data remains secure and compliant with the centrally-defined policies in Privacera. You can learn more about how this works in Privacera's [Dremio connector](https://docs.privacera.com/connectors/dremio/) documentation.
* **Dremio Auditing and Query Tracking:** Audit details related to user-executed queries in Dremio can be accessed through the Jobs page in the Dremio console. Job lists and job details provide insights into user-executed queries. See [Viewing Jobs](/current/admin/monitoring/jobs/) for more information.
* **Support for all Data Sources:** The Privacera integration supports all Dremio data sources. See [Connect to Your Data](/current/data-sources/) for a full list of sources.

note

When using the Privacera plugin for Dremio, no additional or external tools should be used for the policy synchronization between Privacera and Dremio.

## Prerequisites

Ensure that you meet the following prerequisites before you begin the integration:

* An on-premise or SaaS Privacera Manager host that is running Privacera services
* A deployment of Dremio Enterprise Edition 24.1 or later -- Community Edition and Dremio Cloud *are not* supported at this time

## Installation

Refer to the [Privacera documentation](https://docs.privacera.com/latest/platform/pm-ig/dremio/) to learn how to install and configure Privacera's plugin for Dremio.

note

After installing the Privacera plugin, ensure that the **Enable external authorization plugin** option is selected under **Settings > Advanced Options** on all sources that should utilize the integration with Privacera. After updating any source configurations, restart Dremio.

Was this page helpful?

[Previous

Lake Formation Demo](/current/security/integrations/lake-formation/lake-formation-demo)[Next

Apache Ranger](/current/security/integrations/row-column-policies-ranger)

* Prerequisites
* Installation

---

# Source: https://docs.dremio.com/current/security/integrations/row-column-policies-ranger/

Version: current [26.x]

On this page

# Apache Ranger: Row-Level Filtering & Column-Masking Enterprise

Dremio offers both Apache Ranger security policy support and built-in SQL functions for applying row-level filtering and column-masking.

## Column-Masking Overview

Column-masking is a secure and flexible resource-based solution to hiding sensitive information rapidly on a Hive source. Via Apache-Ranger-based security policies or using Dremio's built-in masking, you may mask or scramble private data at the column-level in a dynamic fashion for Hive query outputs. Utilizing masking methods, you may set a column to only display the year of a data, the first or last four digits of a value, and more.

Utilizing services like Apache Ranger allow you to apply access policies to a Hive source so that filters may be based upon specific users, groups, and conditions. Thus, sensitive information never leaves the source and no changes are required by the source. This likewise removes the need to produce a secondary set of data with protected information manually removed.

The following conditions apply to column-masking:

* Multiple masking types are available
* Masks may be applied to users, groups, and conditions
* Each column must have its own masking policy
* Masks are evaluated in the order they are presented in a query or on a security policy
* Wildcard matching is not supported

For Apache Ranger implementations, additional use cases may be found at [3. Use cases: data-masking](https://cwiki.apache.org/confluence/display/RANGER/Row-level+filtering+and+column-masking+using+Apache+Ranger+policies+in+Apache+Hive).

### Row-Level Filtering Overview

Row-level filtering both simplifies queries and adds a layer of security to the data returned for user/role queries. Either SQL functions or Apache-Ranger-based security policies limit access down to the dataset layer, which then affects how queries are handled upon execution. Row-level security on supported tables helps reduce exposure of sensitive data to specific users or groups. Row segmentation and restricted access together ensures that upon query completion, only specific rows based on both the user's characteristics (username or group/role) and the runtime context of the query are displayed from Dremio's SQL Editor.

Row-level restrictions may be set by user, group/role, and other conditions (conditions only available for Ranger implementations, as described further under Row Filter Conditions).

The following examples serve as use cases where row-level filtering would prove beneficial:

* Hospitals may create security policies enabling 1) doctors to view only the rows containing their patients, 2) insurance claims adjusters to view only rows pertaining to their site/facility, and 3) medical billing coders to only view rows pertaining to specific medical disciplines.
* Financial institutes may create policies restricting access to rows pertaining to a user's specific division, geographic location or site, or role, meaning only employees in Collections would only be allowed to see outstanding unpaid claims, collection payment plans, and so on.
* Organizations utilizing multi-tenant applications may use row-level filters to set logical separations of each tenant's data, thus ensuring a tenant only has access to their own data rows.

For Apache Ranger implementations, additional use cases may be found at [2. Use cases: row-level filters](https://cwiki.apache.org/confluence/display/RANGER/Row-level+filtering+and+column-masking+using+Apache+Ranger+policies+in+Apache+Hive).

## Using Apache Ranger Security Policies

For organizations configured to use [Apache Ranger](/current/data-sources/lakehouse-catalogs/hive/hive-ranger) and Hive sources, support automatically exists in Dremio to handle security policies set from Ranger. Based on the user, group/role, and conditions set externally, Dremio automatically applies restrictions to a user's query and applies row-level filtering and column-masking in the background. Upon query completion, you will then only see the results for rows and columns you have access to, without any visual indication that rows have been removed from view.

### Requirements

* [Dremio 20.0+](/current/release-notes/version-200-release/#ranger-row-filtering--column-masking)
* [Apache Ranger](/current/help-support/advanced-topics/hive-ranger/) configured
  + Admin privileges to add access control policies
* [Hive source](/current/data-sources/lakehouse-catalogs/hive/)

## How It Works

Ranger-based row filtering and column-masking functions as an "implicit view," replacing a table/view reference in an SQL statement prior to processing the statement. This implicit view is created through an examination of user permissions. For example, consider a user with access to `table_1`, while also having a mask applied on `table_1.column_1`, effectively translating the column to "xxx." Simultaneously, a row filter exists for `table_1.column_2`.

The original query would appear as:

Original query

```
SELECT column_1  
FROM table_1  
WHERE column_3
```

With both column-masking and row-level filtering policies applied from Ranger, the query above is rewritten to the following:

Query with column-masking and row-level filtering policies

```
WITH filtered_and_masked_table_1  
AS (  
  SELECT 'xxx' AS column_1, column_2, column_3  
  FROM table_1  
  WHERE column_2  
)  
SELECT column_1  
FROM filtered_and_masked_table_1  
WHERE column_3;
```

## Setting Policies in Apache Ranger

For organizations currently utilizing Apache Ranger and configured to apply policies to Dremio, the application of row-level filtering and column-masking is automatic. However, in order to apply these security measures, you must also create security policies from Ranger, which will then propagate down to Dremio when the affected users perform a query.

To create a security policy in Apache Ranger:

1. Navigate to the *Service Manager* page, and then select the desired **Hive Service**.
2. Click the **Column Masking** or **Row Level Filter** tab.

![](/assets/images/ranger-row-tab-816339a932b061bab4a17d81e77be873.png)

3. Click **Add New Policy**.

Now you are at the **Add Policy** screen. The sections below describe the elements contained on that page.

### Policy Details

The following table describes the **Policy Details** section of the *Create Policy* screen.

| Field | Required | Description |
| --- | --- | --- |
| Policy Name | YES | The name of the policy. This value cannot be duplicated in another policy. |
| Policy Label |  | Tags to help categorize and make the policy more searchable. |
| Hive Database | YES | The name of the database(s) to which this policy applies. The field will display auto-complete options based on what matches the current entered value. The database must be a parent to any specified table(s) below, otherwise it will fail to apply. |
| Hive Table | YES | The name of the table(s) to apply the policy toward. Please ensure the tables are associated with the database(s) specified above, otherwise they will not be accessible. |
| Description |  | A description of the policy to explain its intended purpose, its audience, and any other relevant details. |
| enabled/disabled | YES | Determines whether the specific policy apply to the specified users, groups/roles, and conditions. If disabled, the security policy will not affect user queries. |
| normal/override | YES | Controls how the policy is prioritized against other existing security policies. If set to **override**, this policy will ignore other policies that may restrict or grant access beyond the scope specified here. |
| Audit Logging | YES | Controls whether auditing is enabled and is set to **YES** by default. Auditing tracks all user actions impacted by this policy. |

### Row Filter Conditions

The following table describes the **Row Filter Conditions** section of the *Create Policy* screen.

![](/assets/images/ranger-row-filter-2-7445a72be0f63c9cf236b7ddd3d9de9d.png)

| Field | Description |
| --- | --- |
| Select Group | The group(s) of users to which this policy applies. The public group will apply to all users. If no group is specified, a user must be provided. |
| Select User | The individual user(s) to which this policy applies. If no user is specified, a group must be provided. |
| Access Types | The action which the specified group(s) or user(s) may utilize from the Dremio SQL Editor. Currently, the only type available is select. This is used in tandem with the WHERE clause as specified in the Row Level Filter field. |
| Row Level Filter | A valid WHERE clause as entered in the Enter filter expression pop-up upon clicking the Add Row Filter button. To allow full SELECT access to users without row-level filtering, do not click this button. Filters are applied based on top-down order, meaning the filter at the top is applied first, then the second filter, and so on. |

### Mask Conditions

![](/assets/images/ranger-masking-1-2043318099b6431a5a3145350a8743b2.png)

| Field | Description |
| --- | --- |
| Select Group | The group(s) of users to which this policy applies. The public group will apply to all users. If no group is specified, a user must be provided. |
| Select User | The individual user(s) to which this policy applies. If no user is specified, a group must be provided. |
| Access Types | The action which the specified group(s) or user(s) may utilize from the Dremio SQL Editor. Currently, the only type available is select. This is used in tandem with the WHERE clause as specified in the Row Level Filter field. |
| Select Masking Type | The type of column-masking behavior to apply to the associated users/groups when they query the table specified on this policy.  * **Redact -** Replaces all alphabetic characters with `x` and all numeric characters with `n`. * **Partial mask: show last 4 -** Displays only the last four characters of the full column value's. * **Partial mask: show first 4 -** Displays only the first four characters of the full column value's. * **Hash -** Replaces all characters with a hash of the entire cell's value. * **Nullify -** Replaces all characters in the cell with a `NULL` value. * **Unmasked (retain original value) -** No masking is applied to the cell. * **Date: show only year -** Displays the year portion of a date string, defaulting the month and day to `01/01`. * **Custom -** Specifies a custom column masked value or valid Dremio expression. Custom masking may not use [Hive UDFs]<https://cwiki.apache.org/confluence/display/hive/languagemanual+udf#LanguageManualUDF-DataMaskingFunctions>.   Masks are applied based on top-down order, meaning the mask at the top is applied first, then the second mask, and so on. |

## Adding a Row-Level Filter Policy

This section outlines how to create a row-level filter policy from the Apache Ranger console.

For additional instructions and information about row-level filtering, see [Row-level filtering and column-masking using Apache Ranger policies in Apache Hive](https://cwiki.apache.org/confluence/display/RANGER/Row-level+filtering+and+column-masking+using+Apache+Ranger+policies+in+Apache+Hive).

To create a policy that enforces row-level access control, perform the following steps:

1. From the Apache Ranger console, navigate to the *Serivce Manager* page, and then select the desired **Hive Service**.
2. Click the **Row Level Filter** tab.

![](/assets/images/ranger-row-tab-816339a932b061bab4a17d81e77be873.png)

3. Click **Add New Policy**.
4. From the *Create Policy* page, provide values for the **Policy Details** and **Row Filter Conditions** sections.
5. Add any desired conditions, or else leave the **Row Filter Conditions** section blank to apply no filtering.

![](/assets/images/ranger-row-filter-2-7445a72be0f63c9cf236b7ddd3d9de9d.png)

6. To move a condition under the **Row Filter Conditions** section, click the dotted icon on the left-hand side of the row, and then drag it to the desired new location,
7. Click **Add** to save the new policy.

## Adding a Column-Masking Policy

This section outlines how to create a column-masking policy from the Apache Ranger console.

For additional instructions and information about column-masking, see [Row-level filtering and column-masking using Apache Ranger policies in Apache Hive](https://cwiki.apache.org/confluence/display/RANGER/Row-level+filtering+and+column-masking+using+Apache+Ranger+policies+in+Apache+Hive).

To create a policy that enforces row-level access control, perform the following steps:

1. From the Apache Ranger console, navigate to the *Serivce Manager* page, and then select the desired **Hive Service**.
2. Click the **Row Level Filter** tab.

![](/assets/images/ranger-masking-tab-1713107d595300f3d5cbd4ff21f4ad70.png)

3. Click **Add New Policy**.
4. From the *Create Policy* page, provide values for the **Policy Details** and **Mask Conditions** sections.
5. Create any desired masking conditions under the **Mask Conditions** section, or else select **Unmasked (retain original value)** to not apply masking for a user or group.

![](/assets/images/ranger-masking-1-2043318099b6431a5a3145350a8743b2.png)

5. To move a condition under the **Mask Conditions** section, click the dotted icon on the left-hand side of the row, and then drag it to the desired new location,
6. Click **Add** to save the new policy.

## Using Dremio's Built-In Filtering/Masking

For organizations not using Apache Ranger, Dremio offers column-masking and row-level filtering for views via SQL functions. However, this implementation is limited in comparison to the security policies possible with [Ranger implementations](/current/help-support/advanced-topics/hive-ranger/). Where possible, utilize this service to enforce row-level permissions and column-masking as described above.

note

We recommend using [Dremio 20.0+](/current/release-notes/version-200-release/#ranger-row-filtering--column-masking) in tandem with Apache Ranger to apply [user/role-based](/current/security/rbac/) security policies across all datasets while querying a table/view. Otherwise, you may utilize Dremio's built-in SQL functions (as describe below) to manually enforce filtering and masking.

### Creating a View with Column-Masking

By using the [query\_user()](/current/reference/sql/sql-functions/functions/QUERY_USER/) or `is_member()` SQL functions, a view can be configured manually to allow selective masking of columns for different [users/roles](/current/security/rbac/) without the need to create multiple datasets.

The following is a sample SQL command for a view using column-masking syntax:

Example for view using column-masking

```
SELECT  
    CASE  
        WHEN query_user() IN ('dave','mike') OR is_member('Accounting') THEN SSN  
        ELSE CONCAT('XXX-XX-',SUBSTR(SSN,8,4))  
    END  
FROM ss.crm.dbo.employees
```

The SQL function `is_member()` is case-insensitive by default. This may be circumvented by adding a boolean `is_member(groupname, <case-sensitivity boolean>)` to control case-sensitivity. Simply set it to `true` to enable case-sensitivity or `false` to disable. If omitted from the SQL command, the boolean defaults to `false`.

### Creating a View with Row-Level Permissions

By using the [query\_user()](/current/reference/sql/sql-functions/functions/QUERY_USER/) or `is_member()` SQL functions, a view can be configured to allow manual selective filtering of rows for different [users/roles](/current/security/rbac/) without the need to create multiple datasets.

The following is a sample SQL command for a view using row-level filtering syntax:

Example for view using row-level filtering

```
SELECT *  
    FROM mongo.view.business  
    WHERE  
        (state = 'NV' AND query_user() IN ('dave','mike'))  
        OR  
        (state = 'CA' AND is_member('Marketing'))
```

The SQL function `is_member()` is case-insensitive by default. This may be circumvented by adding a boolean `is_member(groupname, <case-sensitivity boolean>)` to control case-sensitivity. Simply set it to `true` to enable case-sensitivity or `false` to disable. If omitted from the SQL command, the boolean defaults to `false`.

Was this page helpful?

[Previous

Privacera](/current/security/integrations/privacera)[Next

Secrets Management](/current/security/secrets-management/)

* Column-Masking Overview
  + Row-Level Filtering Overview
* Using Apache Ranger Security Policies
  + Requirements
* How It Works
* Setting Policies in Apache Ranger
  + Policy Details
  + Row Filter Conditions
  + Mask Conditions
* Adding a Row-Level Filter Policy
* Adding a Column-Masking Policy
* Using Dremio's Built-In Filtering/Masking
  + Creating a View with Column-Masking
  + Creating a View with Row-Level Permissions

---

# Source: https://docs.dremio.com/current/security/authentication/identity-providers/ldap

Version: current [26.x]

On this page

# LDAP Enterprise

## Configuring Dremio for LDAP

To configure Dremio for LDAP, perform the following steps:

1. Create a new `ad.json` file that contains your LDAP server configuration. See the LDAP Properties below for more information.
2. Adding your configuration:

   * Kubernetes
   * Standalone

   1. Update the `coordinator.web.auth.type` configuration in your `values-overrides.yaml` with the value `ldap`. See the configuration of [Identity Providers](/current/deploy-dremio/configuring-kubernetes/#identity-provider).
   2. Optionally, to configure Dremio to use TLS when connecting to LDAP, perform the following steps:

      1. Configure the LDAP `connectionMode` in `ad.json` for the required level of TLS functionality. See LDAP Connection Mode.
      2. To configure a truststore for the validation of TLS LDAP certificates, add the following to `values-override.yaml`

         New configuration for TLS to LDAP

         ```
         dremio:  
           advancedConfigs:  
             trustStore:  
               enabled: true  
               password: "changeit"
         ```
   3. Add the `ad.json` file to your Dremio deployment. This can be done in one of two ways:

      **Method 1 (Preferred)**

      * Add the content of your JSON file into your `values-override.yaml` via the `ssoFile` option. This method is detailed in the [Identity Provider](/current/deploy-dremio/configuring-kubernetes/#identity-provider) section.
      * If TLS with a custom truststore is required, use the `configBinaries` option in your `values-overrides.yaml` and pass in the content of your `.jks` truststore file. For more details, see [Additional Config Binary Files](/current/deploy-dremio/configuring-kubernetes/#additional-config-binary-files).

      **Method 2**

      * Perform a `helm install` with the `--set-file coordinator.web.auth.ssoFile=<your-local-path>/ad.json` option indicating the location of the `ad.json`. See [Deploying Dremio to Kubernetes](/current/deploy-dremio/deploy-on-kubernetes#step-1-deploying-dremio-to-kubernetes) for additional information.
      * Use `--set-file dremio.configBinaries.trustStore=<path/to/truststore/jks/file/on/local/machine>` to pass in a local truststore file, if TLS is required.

   1. Edit the `dremio.conf` file, and add the following properties:

       Example Dremio Service Configuration 

      ```
      services: {  
          coordinator.enabled: true,  
          coordinator.web.auth.type: "ldap",  
          coordinator.web.auth.config: "ad.json"  
      }
      ```
   2. Optionally, to configure Dremio to use TLS when connecting to LDAP, perform the following steps:

      1. Configure the LDAP `connectionMode` in `ad.json` for the required level of TLS functionality. See LDAP Connection Mode.
      2. To configure a truststore for the validation of LDAP TLS certificates, update `dremio.conf` with `javax.net.ssl` settings for the trustStore and trustStorePassword.

          Example Truststore Configuration 

         ```
         javax.net.ssl {  
             trustStore: "<path/to/truststore/jks/file>",  
             trustStorePassword: "trustStorePassword"  
         }
         ```
   3. Copy the modified `dremio.conf` and `ad.json` files to every coordinator node in the Dremio cluster. The location of the `ad.json` file is relative to the `/conf` directory. The path to the file can be absolute; the file can live anywhere in the system.

   Scale-Out Coordinators

   When using [scale-out coordinators](/current/what-is-dremio/architecture/#scale-out-coordinators), you must ensure that both the `dremio.conf` configuration and the `ad.json` file are present on every coordinator node. Scale-out coordinators require the authentication configuration even when `coordinator.web.enabled: false` is set.

## LDAP Properties

The `ad.json` file is a JSON-formatted config file that defines how Dremio connects to and communicates with your LDAP/AD server, including how it finds users, groups, and handles secure authentication.

 Example Configuration for LDAP using Group List 

```
{  
    "connectionMode": "PLAIN",  
    "servers": [  
        {  
            "hostname": "ldap.example.com",    
            "port": 389  
        }  
    ],  
    "names": {  
        "bindDN": "CN=admin,DC=drem,DC=io",  
        "bindMethod": "UNAUTHENTICATED",  
        "bindPassword": "admin",  
        "baseDN": "dc=drem,dc=io",  
        "userFilter": "&(objectClass=posixAccount)",  
        "userAttributes": {  
            "baseDNs": [  
                "OU=Users,OU=ldaptest,DC=drem,DC=io",  
            ],  
            "id": "uid",  
            "firstname": "givenName",  
            "lastname": "sn",  
            "email": "mail"  
        },  
        "userGroupRelationship": "GROUP_ENTRY_LISTS_USERS",  
        "groupEntryListsUsers": {  
            "userEntryUserIdAttribute": "uid",  
            "groupEntryUserIdAttribute": "memberUid"  
        },  
        "groupDNs": ["cn={0},OU=test,OU=ldaptest,DC=drem,DC=io",  
                     "cn={0},OU=dev,OU=ldaptest,DC=drem,DC=io"],  
        "groupFilter": "|(objectClass=posixGroup)(objectClass=sub)",  
        "autoAdminFirstUser": false  
    }  
}
```

### LDAP Connection Mode

The `connectionMode` property configures how Dremio establishes connections to the LDAP/Active Directory servers. The two main secure options — ANY\_SSL and TRUSTED\_SSL — both use SSL/TLS but differ in how SSL certificates are validated. The modes are:

* `PLAIN`: The connection between Dremio and the LDAP server is unencrypted. Dremio connects over port 389 by default, the standard LDAP port for unencrypted communication. This mode is appropriate for internal networks and isolated or trusted environments.
* `ANY_SSL`: Encrypts the connection using SSL/TLS. This mode does not validate the LDAP server's SSL certificate, so it is useful for testing or internal environments where strict certificate checks are not required.
* `TRUSTED_SSL`: This mode encrypts the connection using SSL/TLS and validates the LDAP server’s SSL certificate against the Java truststore. This mode requires additional configuration in `dremio.conf` with the location of the trust store and its password.

### LDAP Server Configuration

The `servers` section of an `ad.json` file defines the LDAP servers that Dremio can use for authentication and directory lookups. Each server accepts the following properties:

* `hostname`: The Fully Qualified Domain Name or IP address of the LDAP server.
* `port`: The port where the LDAP server accepts connections. Port 389 is the default LDAP when the `connectionMode` is `PLAIN`; port 636 is the default port when using SSL/TLS.

### LDAP User and Groups

The `names` section maps LDAP attributes to Dremio’s internal user and group fields. LDAP `names` are defined using the following properties:

| Property | Required | Description |
| --- | --- | --- |
| `autoAdminFirstUser` | No | The first valid LDAP user to log in to Dremio is given the Admin role by default. This behavior, defined by `autoAdminFirstUser: true`, is included in the `ad.json` file. Alternatively, you can specify a list of users and/or groups to be given the Admin role during initial login; it is used for bootstrapping only. See Admin Users for additional configuration information. |
| `baseDN` | Yes | A base distinguished name is the search's root path. If `userAttributes.baseDNs` or `groupAttributes.baseDNs` are specified, they override `baseDN` for search purposes. |
| `bindDN` | No | A bind distinguished name is a client's username to authenticate (bind) to the LDAP directory server. This property is not required when using a `bindMethod` of `ANONYMOUS`. In particular, `CN=admin,DC=drem,DC=io` must not be used. |
| `bindMethod` | No | The authentication method:  * `ANONYMOUS`: Connect anonymously to the LDAP server. When authenticating to Dremio, empty passwords for users are not allowed. * `SIMPLE_BIND`: Default. Connect and authenticate to the LDAP server using `bindDN` and `bindPassword`. * `UNAUTHENTICATED`: Connect to the LDAP server using an unauthenticated bind. `bindDN` is required. |
| `bindPassword` | No | Password credential for the user who connects from the Dremio LDAP client to the LDAP server. `bindPassword` can be encrypted using the `dremio-admin encrypt` CLI command. This property must not be present if you are using `ANONYMOUS` or `UNAUTHENTICATED` for `bindMethod` mode. See Bind Password Options for additional configuration information. |
| `email` | No | Attribute for the email address. |
| `firstname` | No | Attribute for the first name. |
| `groupAttributes` | No | A mapping of LDAP group attributes to Dremio group attributes. The `baseDN`, `searchScope`, and `id` properties are used. |
| `groupDNs` | No | A group distinguished name refers to the full path of a specific group object used for organizing users. |
| `groupFilter` | Yes | LDAP filter for groups. |
| `groupMembership` | No | Value returned by the Dremio `memberOf()` function. This attribute specifies the groups containing a user or a group. |
| `groupRecursive` | No | Attribute of a user or a group that lists transitive group membership. |
| `id` | No | If used with the `userAttributes` property, `id` is the attribute for the login name, defaulting to `sAMAccountName`. If used with the `groupAttributes` property, `id` is the attribute for the group name, defaulting to `CN`. |
| `lastname` | No | Attribute for the last name. |
| `searchScope` | No | Scope of user searches:  * `BASE`: Match the exact entry. * `ONE`: Searches immediate children below the specified `baseDN`. * `SUB_TREE`: Default. Searches subtrees below the specified `baseDN`. |
| `userAttributes` | No | A mapping of LDAP user attributes to Dremio user attributes. This property should include `firstname`, `lastname`, and `email`. |
| `userDNs` | No | A user distinguished name is the unique path that identifies a specific user object. |
| `userFilter` | Yes | LDAP filter for validating users. Only users who fit the specific criteria are allowed to authenticate. |
| `userGroupRelationship` | No | Determines whether you are implementing lists based on users or groups.  * `GROUP_ENTRY_LISTS_USERS`: Specifies whether the group entry in LDAP lists the users that belong to it. * `USER_ENTRY_LISTS_GROUPS`: Default. Specifies whether the user entry in LDAP lists the groups to which the user belongs. The group attribute in LDAP is configured by the `groupMembership` property. |

#### Defining Users

##### Using User Distinguished Names

This approach specifies a list of templates for `userDN`. The placeholder `{0}` is replaced with the username entered by the user, and that Distinguished Name (DN) is used during LDAP bind. In the specified order, Dremio attempts to bind to the provided `userDN`. In the DN-based approach, the `baseDN`, `searchScope`, and `id` properties cannot be specified under `userAttributes`.

userDNs example

```
"userDNs": ["cn={0},dc=staticsecurity,dc=dremio,dc=com"],  
    "userAttributes": {  
    "firstname": "givenName",  
    "lastname": "sn",  
    "email": "mail"  
}
```

##### Using User Attributes

In this approach, you map LDAP user attributes to Dremio user attributes. The `userDN` field must not be specified in the attribute-based approach. Do not change the value of `id` in the `ad.conf` file after you start Dremio. Changing the value can result in the loss of user privileges.

userAttributes example

```
"userAttributes": {  
    "baseDNs": [  
        "OU=test,OU=ad,DC=drem,DC=io"  
    ],  
    "searchScope": "SUB_TREE",  
    "id": "sAMAccountName",  
    "firstname": "givenName",  
    "lastname": "sn",  
    "email": "mail"  
}
```

##### Using userFilter

The following example uses the `userFilter` property to limit access to engineering group members.

userFilter example

```
"userFilter": "&(objectClass=user)(memberOf=cn=engineering,OU=Groups,OU=ad,DC=drem,DC=io)",
```

#### Defining Groups

##### Using Group Distinguished Names

This approach specifies a list of templates for group Distinguished Names (DNs). The placeholder `{0}` is replaced with the group name entered by the user. Dremio attempts to search for the given `groupDNs` in the specified order. The `groupAttributes` property must not be specified in the DN-based approach.

Example using Group Distinguised Names 

```
"groupDNs": ["cn={0},OU=engg,OU=test,OU=ad,DC=drem,DC=io"]
```

##### Using Group Attributes

In this method, use the `groupAttributes` property to specify a list of `baseDNs` and group name IDs. These properties map LDAP group attributes to Dremio group attributes. The `baseDNs`, `searchScope`, and `id` properties are required. The `groupDNs` field must not be specified in the attribute-based approach.

groupAttributes example

```
"groupAttributes": {  
    "baseDNs": ["dc=roles,dc=dremio,dc=com"],  
    "searchScope": "SUB_TREE",  
    "id": "CN"  
}
```

#### Defining User-Group Relationships

The relationship between users and groups can be defined with one of the following methods:

* Group memberships
* Group lists

##### Group Membership Method

The group membership method implements user entries in LDAP that list the groups to which the user belongs. The user entries in LDAP are configured to list their group membership via the internal field `memberOf`.

For example,

* Dan is part of the **BI** group
* The BI group is part of the engineering group,
* `groupMembership` property will contain only the BI group, but the `groupRecursive` property will contain the engineering group.

Example settings for groupMembership and groupRecursive properties

```
"groupMembership": "memberOf",  
"groupRecursive": "transitive-memberOf",
```

To establish this user-group relationship:

* Specify `groupMembership` property.
* Specify (if applicable) the `groupRecursive` property.

tip

If you include the `groupRecursive` key, ensure the value is the correct property for recursive lookups for your LDAP implementation. If you do not specify the proper property, Dremio skips recursive lookup and finds only the group membership. If you omit the `groupRecursive` key-value pair from your configuration, Dremio defaults to recursive lookup.

You can also specify the `"userGroupRelationship": "USER_ENTRY_LISTS_GROUPS"` property-value. However, this property is optional since it is the default.

Example Group Membership Configuration 

```
{  
    "connectionMode": "PLAIN",  
    "servers": [  
        {  
            "hostname": "<LDAP_HOST>",  
            "port": 389  
        }  
    ],  
    "names": {  
        "bindDN": "CN=Admin,OU=Users,OU=ad,DC=drem,DC=io",  
        "bindPassword": "password",  
        "baseDN": "dc=dremio,dc=io",  
        "userFilter": "&(objectClass=user)(|(memberOf=CN=QA,OU=temps,OU=test,OU=ad,DC=drem,DC=io)(memberOf=CN=qa,OU=engg,OU=test,OU=ad,DC=drem,DC=io))",  
        "userAttributes": {  
            "baseDNs": [  
                "OU=test,OU=ad,DC=drem,DC=io"  
            ],  
            "searchScope": "SUB_TREE",  
            "id": "sAMAccountName",  
            "firstname": "givenName",  
            "lastname": "sn",  
            "email": "mail"  
        },  
        "groupMembership": "memberOf",  
        "groupRecursive": "transitive-memberOf",  
        "groupDNs": ["cn={0},OU=engg,OU=test,OU=ad,DC=drem,DC=io"],  
        "groupFilter": "(objectClass=group)",  
        "autoAdminFirstUser": true  
    }  
}
```

##### Group List Method

The group list method implements user-group relationships where the group entry lists the users that belong to that group.

For example,

* `uid` is the ID attribute used for the user entry, and `memberUid` is the ID attribute used for the group entry.
* Dan's ID is 1234, represented by the attribute `uid` in Dan's LDAP records.
* Dan is part of the **BI** group
* The LDAP entry for group **BI** lists `memberUid = 1234`, indicating that Dan is a valid group member.

Example Group List 

```
"userGroupRelationship": "GROUP_ENTRY_LISTS_USERS",  
"groupEntryListsUsers": {  
    "userEntryUserIdAttribute": "uid",  
    "groupEntryUserIdAttribute": "memberUid"  
}
```

To establish user-group relationships in `ad.json` using the group list method:

* Set `userGroupRelationship` to `GROUP_ENTRY_LISTS_USERS`.
* Specify the `groupEntryListsUsers` property and its sub-properties, `userEntryUserIdAttribute` and `groupEntryUserIdAttribute`.

Example Group List Configuration

```
{  
    "connectionMode": "PLAIN",  
    "servers": [  
        {  
            "hostname": "host_ip",  
            "port": 389  
        }  
    ],  
    "names": {  
        "bindDN": "CN=admin,DC=drem,DC=io",  
        "bindMethod": "UNAUTHENTICATED",  
        "bindPassword": "admin",  
        "baseDN": "dc=drem,dc=io",  
        "userFilter": "&(objectClass=posixAccount)",  
        "userAttributes": {  
            "baseDNs": [  
                "OU=Users,OU=ldaptest,DC=drem,DC=io",  
            ],  
            "id": "uid",  
            "firstname": "givenName",  
            "lastname": "sn",  
            "email": "mail"  
        },  
        "userGroupRelationship": "GROUP_ENTRY_LISTS_USERS",  
        "groupEntryListsUsers": {  
            "userEntryUserIdAttribute": "uid",  
            "groupEntryUserIdAttribute": "memberUid"  
        },  
        "groupDNs": ["cn={0},OU=test,OU=ldaptest,DC=drem,DC=io",  
                     "cn={0},OU=dev,OU=ldaptest,DC=drem,DC=io"],  
        "groupFilter": "|(objectClass=posixGroup)(objectClass=sub)",  
        "autoAdminFirstUser": false  
    }  
}
```

### Bind Password Options

Dremio offers several options for managing the bind password.

#### Encryption

For customers with stringent security standards and requirements, password encryption provides a secure method for communicating key information with the LDAP service. Encryption is accomplished using the CLI command [`dremio-admin encrypt`](/current/reference/admin-cli/encryption/).

To encrypt the bind password, follow these steps:

1. Run `dremio-admin encrypt` as the `dremio` service user.

   LDAP secret Encryption 

   ```
   sudo su - dremio bin/dremio-admin encrypt <yourSecret>
   ```

   If running the command as the `dremio` user is impossible, change the owner and group of the `$DREMIO_HOME/data/security` folder and underlying files to the `dremio` service user.

   Dremio outputs:

   Example LDAP Encryption Output

   ```
   secret:1.FxLevnDdoHx58x7VZmBpNExUiM76_u7XAXo1SJ8mCJxzeC1SirK2Jm5aBRR-h2_r8iypOAcRYSzH4uyP33Vg6Fh94bV6evuQ.wENZ7fgdJBw92wy4DiPhpJRzNP07wBaVpspv8KygjMfYV2en3YPFZw==
   ```
2. Copy the entire output to `bindPassword` in `ad.json`.
3. Copy the modified `ad.json` file to every coordinator node in the Dremio cluster.

#### Other Bind Password Options

Other options are available for `bindPassword`:

* `env`: the `bindPassword` is set to `env:ldap` with the environment variable set by the command `export ldap <secret>` where `<secret>` is the output.
* `file`: the `bindPassword` is set to `file:///tmp/test.file` where the file specified contains the output secret.
* `data`: The secret is in base64 format. The bindPassword is then set to `data:text/plain;base64,SGVsbG8sIFdvcmxkIQ==`.

Options `env` and `file` apply to the local node. If you use a multi-coordinator configuration, you must do this for each coordinator node. However, this method contains the raw secret in the `env` scheme and file. Only `secret` uses an encrypted secret.

### Admin Users

To specify users/groups as administrators up-front, during initial login:

1. In the `ad.json` file, set `autoAdminFirstUser` to false.

   Example property for defining Admin users

   ```
   "autoAdminFirstUser": false
   ```
2. Create a file called `bootstrap-admin-users.json` that contains `users` and `groups` arrays to specify the names of the users and groups that should belong to the `ADMIN` role. Use the Common Name (CN) for each user and group you list in the arrays.

   Example settings for users and groups properties

   ```
   {  
       users: ["joe", "bob"],  
       groups: ["marketers", "sales wizards"]  
   }
   ```

   When you set `autoAdminFirstUser` to `false`, then you **must** specify users/groups in a `bootstrap-admin-users.json` file. Otherwise, an administrator won't be specified. The users/groups specified in the `bootstrap-admin-users.json` file are used only during initial login and when `autoAdminFirstUser` is set to `false`. To add other users or groups to the `Admin` role **after the initial login**, use the Dremio console.
3. Add the configuration to your deployment:

   * Kubernetes
   * Standalone

   This can be done in one of two ways:

   **Method 1 (Preferred)**

   Add the configuration of your `bootstrap-admin-users.json` file to your `values-override.yaml` via the `configFiles` option. This approach is detailed in [Additional Config Files](/current/deploy-dremio/configuring-kubernetes/#additional-config-files).

   **Method 2**

   Perform a `helm install` with the `--set-file "dremio.configFiles.bootstrap-admin-users\.json"=/your/local/path/here` option, indicating the location of the `bootstrap-admin-users.json` file. For additional information, see step 1 in [Deploying Dremio to Kubernetes](/current/deploy-dremio/deploy-on-kubernetes/#step-1-deploy-dremio).

   1. Place `bootstrap-admin-users.json` under the Dremio configuration directory.
   2. Start Dremio

Was this page helpful?

[Previous

Identity Providers](/current/security/authentication/identity-providers/)[Next

Microsoft Entra ID](/current/security/authentication/identity-providers/microsoft-entra-id)

* Configuring Dremio for LDAP
* LDAP Properties
  + LDAP Connection Mode
  + LDAP Server Configuration
  + LDAP User and Groups
    - Defining Users
      * Using User Distinguished Names
      * Using User Attributes
      * Using userFilter
    - Defining Groups
      * Using Group Distinguished Names
      * Using Group Attributes
    - Defining User-Group Relationships
      * Group Membership Method
      * Group List Method
  + Bind Password Options
    - Encryption
    - Other Bind Password Options
  + Admin Users