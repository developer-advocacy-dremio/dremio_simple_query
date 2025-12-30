# Security and Compliance | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/

On this page

Dremio offers extensive security measures to help protect the integrity of your data, including access control and the ability to use external identity providers (IdPs). Dremio provides flexible native security features and integration with a wide range of third-party tools so that your organization can adhere to compliance and regulatory standards, enforce fine-grained permissions for your users, and retain your existing tools for authentication and authorization.

## Authentication and Identity Management

Dremio supports industry-standard [authentication](/dremio-cloud/security/authentication/) and single sign-on (SSO) services, including OAuth 2.0/OpenID Connect. Organizations can configure integrated authentication (Active Directory or OpenID Connect) to centrally manage user accounts with strong password policies and SSO/multi-factor authentication (MFA).

## Access Control

Dremio provides a comprehensive hierarchical privilege system for fine-grained access control across your organization.

* **Privileges** – Complete [privilege system](/dremio-cloud/security/privileges) with hierarchical inheritance from organization to individual objects.
* **Role-Based Access Control (RBAC)** – Manage access [through roles](/dremio-cloud/security/roles) rather than individual user grants for easier administration.
* **Hierarchical Inheritance** – Privileges granted at higher levels (Organization → Projects → Sources → Folders → Tables) automatically apply to nested objects.
* **Object Ownership** – Automatic ownership assignment when creating objects, with transferable ownership capabilities.
* **Open Catalog Security** – Structured access control for managed catalog systems.

## Data Protection

* **Encryption in Transit** – Your content is transmitted using TLS 1.2 or higher between client and control plane, and between control plane and data plane.
* **Encryption at Rest** – Your data is encrypted at rest within the control plane using AES-256 or higher.
* **Customer-Managed Encryption** – Deploy and manage your encryption keys for enhanced security.

## Compliance and Certifications

* **Compliance** – Review current [compliance measures](/dremio-cloud/security/compliance) and audits Dremio has completed.

**Current Certifications:**

* **ISO 27001** – Information security management systems.
* **SOC 2 Type II** – Security, availability, and confidentiality controls.
* **HIPAA** – Healthcare data protection compliance.

**Privacy Regulations:**

* **GDPR** – General Data Protection Regulation compliance.
* **CCPA** – California Consumer Privacy Act compliance.

Was this page helpful?

* Authentication and Identity Management
* Access Control
* Data Protection
* Compliance and Certifications

<div style="page-break-after: always;"></div>

# Roles | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/roles

On this page

Roles are a set of [privileges](/dremio-cloud/security/privileges) that can be assigned to users as needed. Roles can also be assigned to other roles to create a child-role hierarchy, where child roles inherit all privileges from their parent roles. This hierarchical system allows you to organize privileges at scale rather than managing privileges for each individual user (also called members).

You can define roles based on the types of users in your organization. For example, *Data\_Analyst* and *Security\_Admin* roles can be created to manage privileges for users with different job functions within an organization.

See the following role design guidelines:

* Keep the number of ADMIN role members to 1-2 administrators for security.
* Begin with 2-3 custom roles based on primary job functions.
* Create parent roles for common privilege sets, then add specific child roles as needed.
* Choose clear names that reflect the role's purpose (e.g., Sales\_Analyst, Data\_Engineer).
* Use prefixes such as DEPT\_, PROJ\_, or TEAM\_ for consistency.
* Use the description field to explain each role's intent.

## How Role Inheritance Works

Child roles automatically inherit all privileges from their parent roles, creating a cascading effect that simplifies privilege management.

Example Role Hierarchy

```
Data_Viewer (SELECT on public datasets only)  
  └── Data_Analyst (inherits Data_Viewer + SELECT on specific datasets)  
      └── Data_Engineer (inherits Data_Analyst + CREATE, ALTER privileges)  
          └── Data_Admin (inherits Data_Engineer + admin privileges on data sources)
```

In this example, a Data\_Engineer automatically gets all the privileges of Data\_Analyst and Data\_Viewer, plus their own additional CREATE and ALTER privileges.

## System Roles

Dremio has two predefined system roles: ADMIN and PUBLIC. These roles can be used to manage privileges.

### ADMIN

The ADMIN role is designed for administrative users who require superuser/global access. Users who are assigned this role are granted every privilege across all objects and resources in an organization. The privileges for the ADMIN role are immutable by users.

The first user in an organization is automatically assigned the ADMIN role.

Be cautious when assigning the ADMIN role. Users with ADMIN privileges can modify any data, delete objects, and manage other users' access.

### PUBLIC

The PUBLIC role is assigned by default to all new users added to the organization and cannot be revoked from any user. Think of PUBLIC as the baseline access level that every user in your organization receives.

This role grants the following privileges to its members:

* USAGE on all engines
* USAGE on any predefined [OAuth apps](/dremio-cloud/security/authentication/app-authentication/oauth-apps) and [External Token Providers](/dremio-cloud/security/authentication/app-authentication/external-token).

SELECT and ALTER privileges are not granted for any sources and must be assigned by a user with the ADMIN role or through additional custom roles.

Additional privileges can be granted to the PUBLIC role to provide organization-wide baseline access.

## Custom Roles

Custom roles can be created by any user or role that has the [CREATE ROLE](/dremio-cloud/security/privileges#organization-privileges) organization privilege, or by members of the ADMIN role.

You can assign a custom role to users or other roles (to create a child role). The custom role can then be assigned a set of privileges.

### View All Roles

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.

#### Use SQL

ADMIN users can also list all roles using the [`sys.organization.roles`](/dremio-cloud/sql/system-tables/roles) system table:

Review all roles and their owners

```
SELECT r.role_name,   
       r.role_type,   
       r.owner_type,  
       u.user_name as owner_name  
FROM sys.organization.roles r  
LEFT JOIN sys.organization.users u ON r.owner_id = u.user_id  
ORDER BY r.role_name;
```

### Create a Custom Role

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.
3. Click **Add Role** at the top-right corner of the screen.
4. In the Add Role dialog, for **Name**, enter the name to associate with the role, such as the position title or employee type that will be associated with the role.
5. (Optional) For **Description**, provide any details regarding the purpose of the role or its associated privileges.
6. Click **Add**.

#### Use SQL

You can also create custom roles using the [`CREATE ROLE`](/dremio-cloud/sql/commands/create-role/) command.

### Edit a Custom Role

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.
3. On the Roles page, select the role.
4. On the Edit Role page, make any desired changes, such as adding or removing a child role and adding or removing a member.
5. Click **Save**.

#### Use SQL

You can also add or remove child roles and members using the [GRANT ROLE](/dremio-cloud/sql/commands/grant-role) and [REVOKE ROLE](/dremio-cloud/sql/commands/revoke-role) SQL commands.

### Remove a Custom Role

Removing a role will immediately revoke all associated privileges from its members. Ensure users have alternative access before deleting roles.

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.
3. On the Roles page, hover over the row of the role and click ![Delete](/images/icons/trash.png "Delete") that appears next to the role.
4. Confirm that you want to delete the role.

Once confirmed, the role is deleted and cannot be retrieved.

#### Use SQL

You can also remove custom roles using the [`DROP ROLE`](/dremio-cloud/sql/commands/drop-role/) command.

### Add a Child Role

Child roles inherit all privileges from their parent roles. This creates a hierarchy where more specific roles build upon broader ones.

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.
3. On the Roles page, select the parent role, then select the **Roles** tab.
4. Click the dropdown multi-select field and either select the desired role or enter a role name to search for it.
5. Click *Add*\* when you have selected the desired entry or entries. When a child role is added, it will display below the dropdown in a list.
6. Click **Save**.

The child role appears in the table along the left side of the screen.

#### Use SQL

You can also add child roles to parent roles using the [`GRANT ROLE`](/dremio-cloud/sql/commands/grant-role) SQL command:

Example Association of a Child Role

```
-- Make Data_Analyst a child role of Analytics_Team  
GRANT ROLE Data_Analyst TO ROLE Analytics_Team;
```

### Remove a Child Role

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.
3. On the Roles page, select the parent role, then select the **Roles** tab.
4. Hover over the row of the role and click ![Delete](/images/icons/trash.png "Delete") that appears next to the role.
5. Click **Save**.

#### Use SQL

You can also remove child roles from parent roles using the [`REVOKE ROLE`](/dremio-cloud/sql/commands/revoke-role) SQL command.

### Add a Member

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.
3. On the Roles page, select the role, then select the **Members** tab.
4. Click the dropdown multi-select field and either select the desired user (listed by email address) or enter an email address to search for it.
5. Click **Add** when you have selected the desired entry or entries. When a member is added, it will display below the dropdown in a list.
6. Click **Save**.

#### Use SQL

You can also add members to roles using the [`GRANT ROLE`](/dremio-cloud/sql/commands/grant-role) SQL command:

Example creating a role member

```
-- Assign Data_Analyst role to a user  
GRANT ROLE Data_Analyst TO USER 'jane.doe@company.com';
```

### Remove a Member

Users cannot remove themselves from the ADMIN role. If you are a member of the ADMIN role and wish to be removed from it, another user who has the necessary privileges must remove you.

#### Use the Dremio Console

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and choose **Organization settings**.
2. Select **Roles** in the organization settings sidebar.
3. On the Roles page, select the role, then select the **Members** tab.
4. Hover over the row of the member and click ![Delete](/images/icons/trash.png "Delete") that appears next to the member.
5. Click **Save**.

This removes them as a member of this role, and they will no longer possess the privileges associated with that role. However, the user still retains privileges associated with any other roles where they are members.

#### Use SQL

You can also remove members from roles using the [`REVOKE ROLE`](/dremio-cloud/sql/commands/revoke-role) SQL command.

## Limits and Considerations

* There is a limit of 10 nested roles in a hierarchy. For more information, see [Limits](/dremio-cloud/help-support/limits/).

Was this page helpful?

* How Role Inheritance Works
* System Roles
  + ADMIN
  + PUBLIC
* Custom Roles
  + View All Roles
  + Create a Custom Role
  + Edit a Custom Role
  + Remove a Custom Role
  + Add a Child Role
  + Remove a Child Role
  + Add a Member
  + Remove a Member
* Limits and Considerations

<div style="page-break-after: always;"></div>

# Compliance | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/compliance

On this page

Dremio meets the IT control requirements for several compliance frameworks and certifications, as described below.

## SOC 2 Type II Report

Dremio maintains compliance with the American Institute of Certified Public Accountants (AICPA) System and Organization Controls - Trust Services Criteria, commonly known as SOC 2.

### Key Benefits

[SOC 2 Type II reports](https://us.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report) provide an in-depth analysis of cloud service providers regarding the safeguards used to protect data and how controls are performed. These reports are issued by independent, third-party auditors and cover the key areas of security, availability, confidentiality, and privacy.

This independent assessment of Dremio provides a detailed report regarding the environments used to provide security and data privacy. The report includes descriptions of these controls, the tests performed to assess their effectiveness, the results of those tests, and an overall opinion regarding the design and operational effectiveness of the environments.

## ISO 27001 Certification

ISO 27001 is an internationally recognized specification for an Information Security Management System (ISMS). ISO 27001 is the only auditable standard that addresses the overall management of information security rather than just which technical controls to implement.

### Key Benefits

Obtaining [ISO 27001:2022 certification](https://www.iso.org/isoiec-27001-information-security.html) demonstrates that Dremio employs a comprehensive framework of legal, physical, and technical controls for information risk management.

## GDPR Compliance

Dremio is compliant with the storage and security of its data according to Article 27 of the General Data Protection Regulation (GDPR). Please see [Dremio's Privacy Policy](https://www.dremio.com/legal/privacy-policy/) for additional information regarding our appointed European Data Protection Officer (EDPO) in the EU.

### Key Benefits

As part of the European Union, specific regulations exist that require companies to [maintain compliance with GDPR](https://gdpr.org/). This regulation governs the way user data is stored, processed, and utilized on Dremio. Specifically, it prevents the exploitation of user data and standardizes the data protection laws that services must follow throughout Europe.

## CCPA Compliance

Dremio maintains compliance with the California Consumer Privacy Act (CCPA), which regulates the handling of personal data and prevents any unauthorized use or sale. Please see [Dremio's Privacy Notice for California Residents](https://www.dremio.com/legal/privacy-policy/) for additional information.

### Key Benefits

Adherence to [CCPA](https://oag.ca.gov/privacy/ccpa) by an organization ensures that California residents have the right to opt out of having their data sold to third parties, request disclosure of data collected, and request deletion of that data.

## HIPAA Compliance

Dremio is compliant with the Health Insurance Portability and Accountability Act (HIPAA), a series of federal regulatory standards that outline the lawful use and disclosure of protected health information in the United States. HIPAA compliance is regulated by the Department of Health and Human Services (HHS) and enforced by the Office for Civil Rights (OCR).

### Key Benefits

Adherence to [HIPAA](https://www.cdc.gov/phlp/publications/topic/hipaa.html) ensures that healthcare providers, health plans, healthcare clearinghouses, and business associates of HIPAA-covered entities must implement multiple safeguards to protect sensitive personal and health information.

Was this page helpful?

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

<div style="page-break-after: always;"></div>

# Privileges | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/privileges

On this page

Dremio provides a range of privileges for each type of securable object. These privileges work together to control access across your organization.

## Key Concepts

### Grants

Dremio privileges are granted to users and roles. Users possess all the privileges granted to their user identity and their roles. See [`GRANT TO USER`](/dremio-cloud/sql/commands/grant-to-user) and [`GRANT TO ROLE`](/dremio-cloud/sql/commands/grant-to-role) for example grants.

### Privilege Inheritance

Dremio uses a hierarchical privilege system where most higher-level privileges apply to all objects within their scope:

**Organization** → **Projects** → **Sources** → **Folders** → **Tables and Views**

When you grant a privilege at a higher level, it applies to all relevant objects at lower levels. For example, granting SELECT at the project level gives SELECT access to all datasets in that project across all sources.

### Ownership and Object Creation

The OWNERSHIP privilege is unique—it applies only to the specific object where it's assigned and is never inherited by nested objects. When you create any object, you automatically become its owner. This design maintains clear ownership boundaries, so a project owner doesn't automatically own every table in that project. OWNERSHIP grants full control of the specific object. Ownership can be transferred using the [`GRANT OWNERSHIP`](/dremio-cloud/sql/commands/grant-to-role) command.

### Sharing Data Through Views

When you create a view based on a table, you become the owner of that view. Your privileges as the view owner determine whether the view can access the underlying table—creating a privilege chain. You can then grant other users access to your view, allowing them to see the table's data even though they don't have direct permission to access that table themselves. However, if you (or whoever last modified the view) lose access to the underlying table, the entire privilege chain breaks and the view stops working for everyone.

## Organization Privileges

Organization privileges are the highest level in the hierarchy and control organization-wide operations and resources.

| Privilege Type | Description |
| --- | --- |
| ALL | Shorthand to grant all supported privileges except OWNERSHIP. |
| CALL MODEL | Use the AI models available across all model providers. The PUBLIC role has this privilege on the organization by default, but it can be revoked. |
| CONFIGURE BILLING | Create and manage billing accounts for usage invoices. |
| CONFIGURE SECURITY | Configure organization security features including [identity providers](/dremio-cloud/security/authentication/idp), [external token providers](/dremio-cloud/security/authentication/app-authentication/external-token), and custom [OAuth applications](/dremio-cloud/security/authentication/app-authentication/oauth-apps). |
| CREATE MODEL PROVIDER | Create model providers for the organization. |
| CREATE PROJECT | Create new projects, each including an Open Catalog. |
| CREATE ROLE | Create and edit roles. See [Custom Roles](/dremio-cloud/security/roles#custom-roles) for details. |
| CREATE USER | Create and edit users. See [Add a User](/dremio-cloud/admin/users#add-a-user) for details. |
| MANAGE GRANTS | Grant or revoke privileges on the organization and all objects it contains. |
| OWNERSHIP | Full control of the organization; not inherited by nested objects. |

## Project Privileges

Project privileges control access to projects and apply to different categories of objects within the project. These privileges provide broad control across all sources, catalogs, and engines in the project.

| Privilege Type | Applies To | Description |
| --- | --- | --- |
| OWNERSHIP | Project | Full control of the project. |
| USAGE | Project | Access the project and its engines. Required for any other project operations. |
| VIEW JOB HISTORY | Project | View the job history page for all users across the entire project. |
| CREATE SOURCE | Sources | Create new data sources and modify source configurations throughout the project. |
| EXTERNAL QUERY | Sources | Run [external queries](/dremio-cloud/bring-data/connect/databases/#external-queries) on compatible sources. |
| ALTER | Datasets | Edit definitions, settings, wikis, and manage metadata. Create or remove folders and datasets where supported. |
| CREATE TABLE | Datasets | Create tables using [`CREATE TABLE`](/dremio-cloud/sql/commands/create-table) and [`CREATE TABLE AS`](/dremio-cloud/sql/commands/create-table-as) on sources that support table creation. |
| DELETE INSERT TRUNCATE UPDATE | Datasets | Execute DML operations on Apache Iceberg tables in compatible object storage. |
| DROP | Datasets | Remove tables and folders from all sources that support deletion operations. |
| SELECT | Datasets | Query contained datasets and view schema definitions, lineages, wikis, and labels. |
| ALTER REFLECTION | Reflections | Create, edit, and view all Reflections across the project. Includes access to Reflection pages, API endpoints, and job history. |
| VIEW REFLECTION | Reflections | View all Reflections across the project, including pages, API endpoints, and job history. |
| MODIFY | Engines | Complete engine management including workload settings, routing, and queues. Includes MONITOR and OPERATE. |
| MONITOR | Engines | View all engine settings including replicas, auto-stop settings, time limits, and tags across all engines. |
| OPERATE | Engines | Start, stop, enable, and disable all engines in the project. |
| MANAGE GRANTS | All Objects | Grant and revoke privileges on the project and all objects it contains. |

## Open Catalog Privileges

[Open Catalog](/dremio-cloud/bring-data/connect/catalogs/open-catalog/) is a specialized source whose privileges control access to folders and datasets within the catalog.

You can grant each of these privileges at the indicated scopes:

* **Catalog scope:** Privileges are granted on the catalog and apply to all the catalog folders and datasets.
* **Folder scope:** Privileges are granted to a specific folder and apply to all contained folders and datasets.
* **Dataset scope:** Privileges are granted to a single table or view and apply only to that dataset.

| Privilege Type | Catalog Scope | Folder Scope | Dataset Scope | Description |
| --- | --- | --- | --- | --- |
| ALL | ✔ | ✔ | ✔ | Shorthand to grant all supported privileges except OWNERSHIP. |
| ALTER | ✔ | ✔ | ✔ | Edit contained table definitions, settings, wikis, and manage metadata operations. Add or remove folders. |
| ALTER REFLECTION | ✔ | ✔ | ✔ | Create, edit, and view Reflections on contained datasets, including pages, APIs, and job history. |
| DROP | ✔ | ✔ |  | Remove contained datasets and folders. |
| MANAGE GRANTS | ✔ | ✔ | ✔ | Grant and revoke privileges on contained objects. |
| OWNERSHIP | ✔ | ✔ | ✔ | Full control; not inherited by nested objects. |
| READ METADATA | ✔ | ✔ | ✔ | View metadata including column information and job history, limited to jobs you have permission to see. |
| SELECT | ✔ | ✔ | ✔ | Query contained datasets and view schema definitions, lineages, wikis, and labels. |
| USAGE | ✔ | ✔ |  | Use the immediate namespace or folder. Must be granted on every folder in the hierarchy path. |
| VIEW REFLECTION | ✔ | ✔ | ✔ | View Reflections on contained datasets, including pages, APIs, and job history. |
| WRITE | ✔ | ✔ | ✔ | Execute write operations [`INSERT`](/dremio-cloud/sql/commands/insert), [`UPDATE`](/dremio-cloud/sql/commands/update), [`TRUNCATE`](/dremio-cloud/sql/commands/truncate), [`DELETE`](/dremio-cloud/sql/commands/delete) on contained Apache Iceberg tables. |

## Source Privileges

Source privileges control access to external data sources and datasets. All sources and other catalogs utilize these privileges in Dremio.

You can grant each of these privileges at the indicated scopes:

* **Source scope:** Privileges are granted on the source and apply to all the source folders and datasets.
* **Folder scope:** Privileges are granted to a specific folder and apply to all contained folders and datasets.
* **Dataset scope:** Privileges are granted to a specific table or view and apply only to that dataset.

| Privilege Type | Source Scope | Folder Scope | Dataset Scope | Description |
| --- | --- | --- | --- | --- |
| ALL | ✔ | ✔ | ✔ | Shorthand to grant all supported privileges except OWNERSHIP. |
| ALTER | ✔ | ✔ | ✔ | Edit contained dataset definitions, settings, wikis, and manage metadata. Add or remove folders, promote or demote tables. |
| ALTER REFLECTION | ✔ | ✔ | ✔ | Create, edit, and view all Reflections on contained datasets, including pages, APIs, and job history. |
| CREATE TABLE | ✔ | ✔ |  | Create new tables using [`CREATE TABLE`](/dremio-cloud/sql/commands/create-table) and [`CREATE TABLE AS`](/dremio-cloud/sql/commands/create-table-as) (requires source to support table creation). |
| DELETE INSERT TRUNCATE UPDATE | ✔ | ✔ | ✔ | Execute associated DML operations [`DELETE`](/dremio-cloud/sql/commands/delete), [`INSERT`](/dremio-cloud/sql/commands/insert), [`TRUNCATE`](/dremio-cloud/sql/commands/truncate), [`UPDATE`](/dremio-cloud/sql/commands/update) on all contained Apache Iceberg tables (requires compatible object storage). |
| DROP | ✔ | ✔ |  | Remove contained datasets and folders (requires source deletion support). |
| EXTERNAL QUERY | ✔ |  |  | Run [external queries](/dremio-cloud/bring-data/connect/databases/#external-queries) on compatible sources. |
| MANAGE GRANTS | ✔ | ✔ | ✔ | Grant and revoke privileges on contained objects. |
| MODIFY | ✔ |  |  | Access and modify configuration settings, connection parameters, and source-level properties. |
| OWNERSHIP | ✔ | ✔ | ✔ | Full control; not inherited by nested objects. |
| READ METADATA | ✔ | ✔ | ✔ | View metadata including column information and job history, limited to jobs you have permission to see. |
| SELECT | ✔ | ✔ | ✔ | Query contained datasets and view schema definitions, lineages, wikis, and labels. |
| VIEW REFLECTION | ✔ | ✔ | ✔ | View Reflections on contained datasets, including pages, APIs, and job history. |

## User-Defined Function Privileges

User-defined functions (UDFs) allow you to create reusable custom functions using SQL expressions.

| Privilege Type | Description |
| --- | --- |
| ALL | Shorthand to grant all supported privileges except OWNERSHIP. |
| ALTER | Edit the function's wiki, definitions, and settings. |
| EXECUTE | Ability to run the UDF. Use the function as row-access and column-masking policies for tables and views. |
| MANAGE GRANTS | Grant and revoke privileges on the UDF. |
| OWNERSHIP | Full control of the UDF; not inherited by nested objects. |

## Engine Privileges

Engine privileges control access to specific named engines. Use engine privileges at the project level to manage all engines collectively.

| Privilege Type | Description |
| --- | --- |
| ALL | Shorthand to grant all supported privileges except OWNERSHIP. |
| MANAGE GRANTS | Grant and revoke privileges on the specific engine. |
| MODIFY | Access and modify all engine settings including replicas, auto-stop configuration, time limits, and tags. |
| MONITOR | View all engine settings and configuration details without modification rights. |
| OPERATE | Start, stop, enable, and disable the engine. |
| OWNERSHIP | Full control of the engine; not inherited by nested objects. |
| USAGE | Execute queries using the engine. The PUBLIC role has this privilege on all engines by default, but it can be revoked. |

## Model Provider Privileges

Model provider privileges control access to AI model providers configured at the organization level. These privileges determine who can use, manage, and configure model providers for your organization.

| Privilege Type | Description |
| --- | --- |
| CALL MODEL | Use the AI models available. |
| MODIFY | Access and modify all model provider settings. |
| MANAGE GRANTS | Grant and revoke privileges on the model provider. |
| OWNERSHIP | Full control of the model provider. |

## Script Privileges

Script privileges enable sharing of individual saved scripts with other users and roles.

| Privilege Type | Description |
| --- | --- |
| ALL | Shorthand to grant all supported privileges except OWNERSHIP. |
| DELETE | Remove the script permanently. |
| MANAGE GRANTS | Grant and revoke privileges on the script. |
| MODIFY | Edit the script content and settings. |
| OWNERSHIP | Full control of the script; not inherited by nested objects. |
| VIEW | Access, view, and execute the script. |

## Identity Provider Privileges

[Identity provider](/dremio-cloud/security/authentication/idp) privileges control access to organization-level authentication and identity management settings.

| Privilege Type | Description |
| --- | --- |
| ALL | Shorthand to grant all supported privileges except OWNERSHIP. |
| MODIFY | Access and modify identity provider settings, including configuration changes and updates. |
| MONITOR | View all identity provider settings and configuration details without modification rights. |
| OWNERSHIP | Full control of the identity provider; not inherited by nested objects. |

## Related Topics

* [Security Pillar](/dremio-cloud/help-support/well-architected-framework/security) – See the security design principles and best practices of the Dremio Well-Architected Framework.

Was this page helpful?

* Key Concepts
  + Grants
  + Privilege Inheritance
  + Ownership and Object Creation
  + Sharing Data Through Views
* Organization Privileges
* Project Privileges
* Open Catalog Privileges
* Source Privileges
* User-Defined Function Privileges
* Engine Privileges
* Model Provider Privileges
* Script Privileges
* Identity Provider Privileges
* Related Topics

<div style="page-break-after: always;"></div>

# PrivateLink | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/privatelink

On this page

Dremio PrivateLink enables secure, private connectivity between your AWS VPC and Dremio services without exposing traffic to the public internet. This service allows you to access all Dremio control plane services, including the UI, REST APIs, and query execution endpoints.

When you enable PrivateLink for your Dremio organization, all Dremio services are accessible only through your VPC endpoint. However, the following Dremio services remain publicly accessible:

* `login.dremio.cloud` – OAuth server for programmatic authentication (API clients, JDBC/ODBC)
* `scim.dremio.cloud` – SCIM provisioning endpoint for identity provider integration (Microsoft Entra ID, Okta, etc.)
* `sql.dremio.cloud` – Dremio JDBC driver (Legacy) endpoint.

If your organization restricts outbound internet access, ensure the `accounts.dremio.cloud` (or `accounts.eu.dremio.cloud` for EU regions) domain is allowed in your firewall rules for authentication to function properly. This authentication service is used during single sign-on (SSO) login flows.

Upon activation of PrivateLink, Dremio console sessions terminate immediately, JDBC/ODBC/API sessions terminate within one hour, and running queries may be interrupted.

Before activating PrivateLink in your Dremio organization:

* Verify your VPC endpoint is available.
* Confirm DNS resolution is working and connections through the endpoint are functioning.
* Schedule a maintenance window and notify users.

PrivateLink uses a **service-based routing** approach with the following domain structure:

`<orgAlias>.<resource>.privatelink.dremio.cloud`

### Domain Components

* **orgAlias** – Your organization's unique identifier that routes connections to your Dremio organization. Requirements:
  + Starts with a letter (a-z, A-Z)
  + Contains only letters, digits, and hyphens
  + Ends with a letter or digit (not a hyphen)
  + Length: 3-63 characters
  + Case-insensitive (stored as lowercase)
  + Follows RFC 1035 DNS naming conventions
* **resource** – The [Dremio services](/dremio-cloud/about/regions/#connection-endpoints) in the connection. The following interfaces are not supported by PrivateLink:
  + `sql.dremio.cloud` for the Dremio JDBC driver (Legacy). Dremio recommends the Arrow Flight SQL JDBC driver using the `data.dremio.cloud` service endpoint when using PrivateLink.
  + `mcp.dremio.cloud` for AI agent integration. Once PrivateLink is activated, this endpoint will not be available.
* **privatelink.dremio.cloud** – The PrivateLink domain suffix for all private connections

**Examples:**

* `acme-corp.app.privatelink.dremio.cloud` – Routes to the Dremio console at `app.dremio.cloud`
* `acme-corp.api.privatelink.dremio.cloud` – Routes to the REST API at `api.dremio.cloud`

### Network Components

PrivateLink uses a VPC endpoint in your AWS VPC to provide secure, private connectivity to Dremio services. Users and applications within the VPC connect through the VPC endpoint using your privately hosted DNS name resolution. Remote users connect via VPN to access the VPC and its resources.

### Certificate Management

Dremio uses wildcard certificates for `*.privatelink.dremio.cloud`. No additional certificate management is required. Server certificates are managed by Dremio, and standard TLS verification applies to client vertification. All certificates are publicly logged.

## Prerequisites

Before setting up PrivateLink, ensure you have:

* AWS Requirements
  + **VPC**: Your VPC in the same region as your Dremio service, where you want to enable PrivateLink connectivity.
  + **Subnets**: At least one subnet in your VPC. When you create a VPC endpoint, you select one or more subnets, and AWS creates an Elastic Network Interface (ENI) in each selected subnet. All ENIs belong to the same VPC endpoint. Select subnets in multiple availability zones for high availability—if one availability zone fails, traffic continues to flow through ENIs in other zones.
  + **VPC Endpoints**: Permission to create and manage VPC endpoints.
  + **Security Groups**: Ability to create or modify security groups.
* Network Requirements
  + **DNS Resolution**: Ability to configure private DNS (such as Route 53 Private Hosted Zones) or CNAME records in your VPC. You will need to create CNAME records that map PrivateLink URLs like `acme-corp.app.privatelink.dremio.cloud` to your VPC endpoint DNS name. While you could technically connect using the VPC endpoint DNS name directly, DNS configuration is required for proper TLS certificate validation and to enable host-based routing to different Dremio services, including `app`, `api`, `data`, and `login`.
  + **TLS/SSL**: Your environment must support TLS 1.2 or higher.
* Client Requirements
  + **Arrow Flight Drivers**: All SQL clients and BI tools must use Arrow Flight-based drivers. Some clients and tools provide their own embedded drivers, but you must use the Dremio Arrow Flight JDBC and ODBC drivers in place of those embedded drivers.

## Configuration Steps

To create a PrivateLink connection:

1. **Create a VPC Endpoint** – In the Amazon Management Console, create a VPC endpoint for [connecting to an endpoint service as the service consumer](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html#connect-to-endpoint-service), using the steps defined by AWS.

   * For **Type**, choose **Endpoint services that use NLBs and GWLBs**.
   * For **Service Name**, enter the Dremio service name for your Dremio region:
     + us-east-1: `com.amazonaws.vpce.us-east-1.vpce-svc-0c795b359782ac685`
     + us-west-2: `com.amazonaws.vpce.us-west-2.vpce-svc-0b42aeb4681d6f4a4`
   * Select your VPC, subnets, and additional configurations.
   * Optionally define a DNS name for your VPC endpoint and enter that name in your privately hosted DNS.
   * Click **Create endpoint**.
2. **Configure a Security Group** – Attach a security group with the following rules:

   * Inbound Rules:

     | Type | Protocol | Port Range | Source | Description |
     | --- | --- | --- | --- | --- |
     | HTTPS | TCP | 443 | Your VPC CIDR or specific security groups | Allow HTTPS traffic from your resources |
   * Outbound Rules:

     | Type | Protocol | Port Range | Destination | Description |
     | --- | --- | --- | --- | --- |
     | HTTPS | TCP | 443 | 0.0.0.0/0 | Allow outbound HTTPS (required for SSO authentication) |
3. **Configure Private DNS** – Create CNAME records in your private DNS (Route 53 Private Hosted Zone or equivalent) to map Dremio service domains to your VPC endpoint DNS name. See AWS documentation for [creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html). Create one CNAME record for each PrivateLink URL associated with a Dremio service. Replace `<orgAlias>` with your organization alias and `<vpc-endpoint-dns-name>` with the DNS name of your VPC endpoint (found in the AWS Console under VPC > Endpoints).

   * `<orgAlias>.app.privatelink.dremio.cloud` → `<vpc-endpoint-dns-name>`
   * `<orgAlias>.api.privatelink.dremio.cloud` → `<vpc-endpoint-dns-name>`
   * `<orgAlias>.data.privatelink.dremio.cloud` → `<vpc-endpoint-dns-name>`
   * `<orgAlias>.login.privatelink.dremio.cloud` → `<vpc-endpoint-dns-name>`
4. **Configure Client Tools** – Configure client applications to use the PrivateLink endpoints:

   * **Power BI Desktop** - See [Connect to Dremio via PrivateLink](/dremio-cloud/explore-analyze/client-apps/microsoft-power-bi#connect-to-dremio-via-privatelink).
   * **JDBC/ODBC Drivers** - Update connection strings to use `<orgAlias>.data.privatelink.dremio.cloud`.
   * **REST API Clients** - Update base URL to `https://<orgAlias>.api.privatelink.dremio.cloud`.
5. **Verify Connectivity** – Test connectivity to Dremio using the VPC endpoint and private DNS:

   * Test DNS resolution using `nslookup <orgAlias>.app.privatelink.dremio.cloud`. This should resolve to private IP addresses in your VPC.
   * From a system within your VPC, test access to the Dremio console by navigating to `https://<orgAlias>.app.privatelink.dremio.cloud`. You should see the Dremio login page.
   * From a system within your VPC, test API access by calling an API endpoint with a base URL of `curl https://<orgAlias>.api.privatelink.dremio.cloud/api/v0/`.
6. **Enable PrivateLink** – Enable PrivateLink by filing a support ticket with Dremio Support at the [Dremio Support Portal](https://support.dremio.com/). In the support ticket, provide:

   * Your **orgAlias**
   * Your Dremio **Organization ID** by clicking ![Settings](/images/icons/settings.png "Settings") in the side navigation bar, choosing **Organization Settings**, and then copying the **Organization ID**.
   * Your VPC endpoint ID from the AWS Console.
   * Confirmation that connectivity works using your new VPC endpoint.
7. **Resume Operation** – Resume operation utilizing your PrivateLink connections.

Was this page helpful?

* Domain Components
* Network Components
* Certificate Management
* Prerequisites
* Configuration Steps

<div style="page-break-after: always;"></div>

# Authentication | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/

On this page

Dremio supports multiple authentication methods for different connection types and user scenarios.

| Use Case | Connection Type | Recommended Method |
| --- | --- | --- |
| **Interactive web access** | Dremio console | Single Sign-On or Username/Password |
| **SQL clients** | JDBC/ODBC clients | Personal Access Tokens (PAT) or Username/Password |
| **Development & testing** | Client applications, REST API | Personal Access Tokens (PAT) |
| **Production scripts & automation** | Client applications, REST API | OAuth access tokens via PAT Exchange |
| **Custom apps with existing IdP** | Client applications, REST API | OAuth access tokens via External JWT Exchange |

### Username/Password

Username and password authentication allows users to sign in directly to Dremio using their email address and a password managed within Dremio. This method is suitable for users who don't have access to an enterprise identity provider or need standalone accounts. Users can reset their passwords through the Dremio console or via email reset links.

### Single Sign-On

Users authenticate through configured identity providers using OIDC protocols. Dremio supports all OIDC-compliant enterprise identity providers, such as Microsoft Entra ID and Okta, as well as social identity providers like Google and GitHub. Users experience automatic login if already signed in to their identity provider.

### Personal Access Tokens (PAT)

[Personal access tokens](/dremio-cloud/security/authentication/personal-access-token) are long-lived authentication credentials that allow programmatic access to Dremio without using passwords. PATs function like API keys and can be used in scripts, applications, and automated processes to authenticate requests.

**Token lifespan:** PATs can be configured with custom expiration periods up to 180 days or set to never expire. You control the lifespan when creating the token.

**Security considerations:**

* PATs can have lifespans up to 180 days, making them convenient but potentially risky if compromised.
* Store PATs securely using environment variables or secret management systems.
* Never include PATs in code repositories or logs.
* Regularly rotate PATs and revoke unused tokens.
* Consider using PAT Exchange for enhanced security in production environments.

Users can create and manage PATs through their Account Settings in the Dremio console.

### OAuth Access Tokens

[OAuth access tokens](/dremio-cloud/api/oauth-token) are short-lived credentials obtained by exchanging other authentication methods (such as PATs or external JWTs). These tokens provide several security advantages:

* **Limited lifespan:** Tokens expire after 1 hour, reducing risk if compromised.
* **Reduced credential exposure:** Your primary credentials (PAT or password) are only used to obtain the token.
* **Standardized format:** Compatible with OAuth 2.0 standards and tooling.
* **Automatic refresh:** Can be programmatically renewed without re-entering credentials.

**Token lifespan:** OAuth access tokens expire after 1 hour. Applications should implement refresh logic to obtain new tokens before expiration. When a token expires, API requests will return an authentication error, requiring your application to exchange credentials again for a new token.

OAuth access tokens are the recommended authentication method for production applications accessing Dremio's REST API and client drivers. You can obtain OAuth access tokens through [PAT Exchange](/dremio-cloud/api/oauth-token#exchange-a-pat) or [External JWT Exchange](/dremio-cloud/api/oauth-token#exchange-an-external-jwt).

#### PAT Exchange

Converting PATs to short-lived OAuth access tokens improves security by reducing exposure windows for compromised tokens. This is the [recommended method](/dremio-cloud/api/oauth-token/#exchange-a-pat) for obtaining OAuth access tokens for REST API access.

The process:

1. Create a PAT in your Dremio account settings.
2. Exchange the PAT for an OAuth access token via the `/oauth/token` REST API.
3. Use the OAuth access token for all subsequent API requests.
4. Refresh the token before it expires (within 1 hour).

#### External JWT Exchange

Applications can exchange JSON Web Tokens (JWTs) from [external token providers](/dremio-cloud/security/authentication/app-authentication/external-token) for Dremio OAuth access tokens, enabling authentication without exposing user credentials. This method is useful for custom applications that need to authenticate users through their existing identity provider (such as Microsoft Entra ID or Okta) and then [access Dremio](/dremio-cloud/api/oauth-token/#exchange-an-external-jwt) on their behalf.

The process:

1. User authenticates with the external identity provider.
2. Application receives a JWT from the identity provider.
3. Application exchanges the JWT for a Dremio OAuth access token via the `/oauth/token` REST API.
4. Application uses the Dremio OAuth access token to make authenticated requests.
5. Application refreshes the token before it expires.

This approach allows applications to maintain a seamless authentication experience while securing access to Dremio resources.

Was this page helpful?

* Username/Password
* Single Sign-On
* Personal Access Tokens (PAT)
* OAuth Access Tokens

<div style="page-break-after: always;"></div>

# Identity Providers | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/idp/

On this page

Identity providers (IdPs) are services that store and manage digital identities. An IdP authenticates users via username-password combinations and other credentials, as typically used for cloud computing and managing user identities. The following IdPs are supported with Dremio:

* Enterprise identity providers, including [Microsoft Entra ID](/dremio-cloud/security/authentication/idp/microsoft-entra-id), [Okta](/dremio-cloud/security/authentication/idp/okta), and other [OpenID Connect (OIDC) providers](/dremio-cloud/security/authentication/idp/generic-oidc-provider).
* [Social identity providers](/dremio-cloud/security/authentication/idp/social-idp/), including GitHub, Microsoft, and Google.

## View an IdP

To view an IdP configured for Dremio:

1. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and then select **Organization settings**.
2. Select **Authentication** from the organization settings sidebar.

## Remove an IdP

You can only remove enterprise IdPs. Social IdPs cannot be removed as they are preconfigured with Dremio.

To remove an enterprise IdP:

1. Click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and then select **Organization settings**.
2. Select **Authentication** from the organization settings sidebar.
3. Click ![Delete](/images/icons/trash.png "Delete") on the row of the IdP to remove. Removing an activated IdP removes it as a login option for all users within your organization. You must manually reconfigure the IdP if you want to use it again as a login option.
4. Confirm that you want to remove the IdP. The IdP is then deleted along with any associated settings.

## SCIM

System for Cross-domain Identity Management (SCIM) automates the synchronization of user accounts between your identity provider (IdP) and Dremio, eliminating the need for manual user management. When configured, IdPs send the credentials of assigned users securely via SCIM to your Dremio organization, automatically creating new user accounts if needed. These new users, also referred to as external users, can then log in to Dremio according to the policies set by your credential manager.

You cannot reset or change an external user's email address or password from Dremio because these tasks are governed by your organization's credential manager. If you delete an external user from Dremio, the IdP automatically re-adds the user's account the next time that user attempts to log in. To properly revoke access to Dremio, follow the steps for [Microsoft Entra ID](/dremio-cloud/security/authentication/idp/microsoft-entra-id#revoke-microsoft-entra-id-sso-login-for-a-user-or-group) or [Okta](/dremio-cloud/security/authentication/idp/okta#revoke-okta-sso-login-for-a-user-or-group).

### Configure Microsoft Entra ID with SCIM

You can use Microsoft Entra ID to securely provision external users in Dremio with SCIM. See [SCIM Provisioning with Microsoft Entra ID](/dremio-cloud/security/authentication/idp/microsoft-entra-id#configure-microsoft-entra-id-with-scim) for more information and instructions.

### Configure Okta with SCIM

Dremio supports the Okta SCIM provisioning feature, which allows you to automatically create Dremio user accounts if they do not already exist, update user attributes in Dremio, and deactivate user accounts, all from Okta.

Before you can configure Okta SCIM provisioning, you must configure Okta as an IdP in Dremio. Follow the instructions in [Okta as an Identity Provider](/dremio-cloud/security/authentication/idp/okta/) to integrate the Dremio application in your Okta organization and add Okta as an OpenID Connect (OIDC) IdP in Dremio.

After you configure Okta as an IdP, you can configure [Okta to use SCIM](/dremio-cloud/security/authentication/idp/okta#configure-okta-with-scim) for secure user provisioning.

## Limits and Considerations

* To provide a consistent experience, Dremio uses rate limits for SCIM provisioning requests. For more information, see [Limits](/dremio-cloud/help-support/limits#rate-limits).
* Dremio allows one update to a user or group at a time. While the update is in progress, Dremio locks the user or group and rejects concurrent requests to update the same user or group.

Was this page helpful?

* View an IdP
* Remove an IdP
* SCIM
  + Configure Microsoft Entra ID with SCIM
  + Configure Okta with SCIM
* Limits and Considerations

<div style="page-break-after: always;"></div>

# Okta | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/idp/okta

On this page

Dremio supports Okta as an enterprise identity provider. Okta administrators can enable single sign-on (SSO) authentication using Okta as the trusted third party.

## Prerequisites

Configuring OIDC SSO in Okta requires:

* [Super Administrator](https://help.okta.com/en-us/Content/Topics/Security/administrators-super-admin.htm) access in Okta
* The CONFIGURE SECURITY [organization-level privilege](/dremio-cloud/security/privileges#organization-privileges) or membership in the [ADMIN role](/dremio-cloud/security/roles#admin).

## Supported Features

Dremio supports the following Okta SSO features:

* **Service provider-initiated (SP-initiated) SSO**: Dremio uses the [OpenID Connect (OIDC)](https://www.okta.com/openid-connect/) protocol for SP-initiated SSO. When users provide their email address to log in to Dremio, Dremio sends an authentication request to Okta. Okta then authenticates the user's identity, and the user is logged in to Dremio.
* **SCIM**: Dremio also allows you to take advantage of Okta's System for Cross-domain Identity Management (SCIM) provisioning feature and manage Dremio user access from Okta. After you configure Okta for OIDC SSO in this guide, see [SCIM with Okta](/dremio-cloud/security/authentication/idp/okta#configure-okta-with-scim) to configure SCIM provisioning.

## Configure OIDC SSO

To configure Okta OIDC SSO for Dremio users:

1. In Okta, navigate to **Applications** > **Applications** and click **Browse App Catalog**.
2. Type `Dremio` in the search field and select **Dremio** from the list of search results.
3. Click **Add Integration**.
4. (Optional) Type a custom label in the *Application label* field.
5. Select your Dremio [control plane region](/dremio-cloud/about/regions) from the *Region* dropdown menu: US or EU.
6. Click **Done**. Okta creates the Dremio application and displays the application's *Assignments* tab.
7. Click the **Sign On** tab.
8. Copy and save the client ID and client secret listed under *OpenID Connect*. The client ID and client secret are sensitive information and should be kept secure. You will use them to configure authentication in Dremio later in this procedure.
9. Click the **OpenID Provider Metadata** link to open the OpenID configuration for the application.
10. Copy and save the URL value for the `issuer` key at the top of the OpenID configuration. You will use it to configure authentication in Dremio later in this procedure.
11. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and select **Organization settings**.
12. Select **Authentication** in the organization settings sidebar.
13. In the Enterprise section, click **Add Provider** to open the Add Provider dialog.
14. In Step 1, select **Okta** from the dropdown menu.
15. In Step 3, enter the issuer URL, client ID, and client secret information that you copied from Okta in the corresponding fields.
16. Click **Add**. After the page loads, you should see Okta as an authentication provider in the *Enterprise* section.
17. Click the **Enabled** toggle to activate the Okta authentication provider.

Okta is now configured as an enterprise authentication provider. **Log in with Okta** appears in the list of login options for your Dremio users.

### Assign People and Groups to the Dremio Application

Follow the instructions in the Okta documentation to [assign people](https://help.okta.com/en-us/Content/Topics/Provisioning/lcm/lcm-assign-app-user.htm) or [assign groups](https://help.okta.com/en-us/Content/Topics/Provisioning/lcm/lcm-assign-app-groups.htm) to the Dremio application to ensure that users can use Okta for SSO login. The users you assign, whether individually or through their membership in an assigned group, can use **Log in with Okta** immediately.

Use [privileges](/dremio-cloud/security/privileges/) and [roles](/dremio-cloud/security/roles/) to manage user access to objects in Dremio.

### Use Okta SSO to Log In to Dremio

Any Okta user who is assigned to the Dremio application can log in with Okta immediately. To use Okta SSO to log in to Dremio:

1. Open the Dremio login page.
2. Type your email address in the *Email* field and click **Continue**.
3. Click **Log in with Okta**.
4. When you are redirected to the Okta website for authentication, enter your Okta username and password and click **Sign In**.

Okta authenticates your identity and redirects you to Dremio, which then logs you in.

To configure Okta's SCIM provisioning feature and use Okta to manage access for Dremio users, see [SCIM with Okta](/dremio-cloud/security/authentication/idp/okta#configure-okta-with-scim).

### Revoke Okta SSO Login for a User or Group

To revoke users' access to Okta SSO login for Dremio:

1. In Okta, open your Dremio application and select the **Assignments** tab.
2. In the left menu, under *Filters*, select **People** to deactivate a user or **Groups** to deactivate a group of users.
3. Find the row for the user or group you want to deactivate and click the **X** on the right side of the row.
4. In the confirmation dialog that appears, click **OK**.

Starting immediately, the deactivated users cannot use Okta OIDC SSO to log in to Dremio. To completely delete Dremio users, you must also [manually remove their user accounts in Dremio](/dremio-cloud/admin/users#remove-a-user).

### Troubleshoot

This section describes some things to keep in mind about OIDC SSO in Okta.

* To add the Dremio application in Okta and configure OIDC SSO, you must be a [super administrator](https://help.okta.com/en-us/Content/Topics/Security/administrators-super-admin.htm) in the Okta organization.
* If you revoke a user's access to use Okta SSO login in Okta, the user can still log in to Dremio with their Dremio username and password. To completely delete the user so that they cannot log in to Dremio at all, you must [manually remove their user accounts in Dremio](/dremio-cloud/admin/users#remove-a-user).

## Configure Okta with SCIM

System for Cross-domain Identity Management (SCIM) automates the synchronization of user accounts between your identity provider (IdP) and Dremio, eliminating the need for manual user management. When configured, your IdP securely sends user credentials to Dremio via SCIM, automatically creating accounts for new users as needed. These users can then log in to Dremio according to your organization's authentication policies.

Before you can configure SCIM provisioning, you must configure Okta as an identity provider (IdP) in Dremio. See [Okta as an Identity Provider](/dremio-cloud/security/authentication/idp/okta/) to integrate the Dremio application in your Okta organization and add Okta as an OpenID Connect (OIDC) single sign-on (SSO) IdP in Dremio. When that is complete, follow this guide to configure Okta to use SCIM for secure user provisioning.

### Prerequisites

Configuring SCIM provisioning in Okta requires:

* [Super Administrator](https://help.okta.com/en-us/Content/Topics/Security/administrators-super-admin.htm) access in Okta
* The CONFIGURE SECURITY [organization-level privilege](/dremio-cloud/security/privileges#organization-privileges) or membership in the [ADMIN role](/dremio-cloud/security/roles#admin).
* A Dremio [personal access token (PAT)](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat)
* You must configure [Okta as an identity provider](/dremio-cloud/security/authentication/idp/okta/) using the Dremio application **before** you proceed with SCIM provisioning.

### Supported Features

Dremio supports the following Okta SCIM provisioning features:

* **Create Users**: Automatically create a new user account in Dremio for Okta users who are assigned to the Dremio application, whether they are assigned individually or as members of a group that is assigned to the application.
* **Update User Attributes**: Automatically update user information in Dremio when a user's profile information is updated in Okta.
* **Deactivate Users**: Prevent users from logging in to Dremio when they are deactivated in Okta.
* **Group Push**: Push Okta groups and their members to Dremio to automatically create Dremio roles and members.

### Configure SCIM Provisioning

To configure and enable SCIM provisioning in Okta:

1. Confirm that you have configured [Okta as an identity provider](/dremio-cloud/security/authentication/idp/okta/) using the Dremio application.
2. In Okta, navigate to **Applications** > **Applications**.
3. Find the Dremio application in the list of applications and click to open it.
4. Click the **Provisioning** tab.
5. Click **Configure API Integration**.
6. Select **Enable API integration**.
7. Enter the Dremio PAT in the *API Token* field.
8. Click **Test API Credentials**. You should see a confirmation message that the connection was verified successfully.
9. Click **Save**. Okta displays the *Provisioning to App* page.
10. Click **Edit**.
11. Select **Enable** for the *Create Users*, *Update User Attributes*, and *Deactivate Users* options.
12. Click **Save**.

SCIM provisioning is now configured and enabled. You can create new users, update user attributes, and deactivate users in Dremio, all from Okta.

### Create Users

After you configure Okta's SCIM provisioning and enable the *Create Users* option, Dremio automatically creates a new Dremio user account for anyone you assign to Dremio who does not already have an account. New Dremio users can log in to Dremio with Okta SSO immediately, and administrators can [view their user accounts in Dremio](/dremio-cloud/admin/users#view-all-users).

* New users are automatically members of the PUBLIC role in Dremio.
* User email addresses are controlled by Okta rather than Dremio. If a user's email address changes, you must create a new user in Okta and assign them to the Dremio application. Then, the user can use the new email address to log in to Dremio as a new user.

### Update User Attributes

With SCIM provisioning configured, updates to user attributes in Okta are propagated to the user account in Dremio. Follow the instructions in the Okta documentation to [edit user attributes](https://help.okta.com/oie/en-us/Content/Topics/users-groups-profiles/usgp-edit-user-attributes.htm).

The *First name* and *Last name* attributes are mapped to user accounts in Dremio. After you configure Okta's SCIM provisioning and enable the *Update User Attributes* option, you can change these user attributes in Okta to update the corresponding user information in Dremio.

### Deactivate Users

When you [revoke a user or group](/dremio-cloud/security/authentication/idp/okta/#revoke-okta-sso-login-for-a-user-or-group) in Okta, the affected users cannot use Okta OIDC SSO to log in to Dremio. After you configure Okta's SCIM provisioning and enable the *Deactivate Users* option, deactivated users become inactive in Dremio and cannot log in to Dremio at all, whether with Okta OIDC SSO or username and password.

To completely delete Dremio users, you must also [manually remove their user accounts in Dremio](/dremio-cloud/admin/users#remove-a-user).

### Group Push

If you enable the group push feature, Okta pushes your designated groups to Dremio as roles and populates the roles with the Okta group's members. Follow the instructions in the Okta documentation to [enable group push](https://help.okta.com/en-us/Content/Topics/users-groups-profiles/usgp-enable-group-push.htm).

Before you enable group push, make sure to follow Okta's instructions to [assign the group](https://help.okta.com/en-us/Content/Topics/Provisioning/lcm/lcm-assign-app-groups.htm) to the Dremio application.

Use Okta to manage any roles you create with group push. Any changes you make to a role or its membership in Dremio are immediately overwritten by the next push from Okta. Making changes in Dremio can result in synchronization errors.

To remove a Dremio role created by group push, unlink the pushed group in the Dremio application. Unlinking the pushed group deletes the corresponding role in Dremio but does not delete the group members' Dremio user accounts.

### Troubleshoot

This section describes some things to keep in mind about SCIM provisioning in Okta with the Dremio application.

* Group push is not supported for groups that do not have any members. Pushing a group that does not have any members will result in an error.
* In Okta, it is possible to change a user's username. Dremio does not allow username updates. If you change a user's Okta username after the user is assigned to the Dremio application, Okta sends a request to update the username in Dremio. Dremio denies the request because Dremio username changes are not allowed.
* Changing an existing user's primary email address in Okta has no effect on the user's account in Dremio. To permit a user to authenticate to Dremio with the new email address, add the user to Okta as a new person using the new email address. Then, assign the new Okta user to the Dremio application, either individually or by adding them to an assigned group. Okta creates a new Dremio user who can use Okta SSO to log in to Dremio with the new email address.
* If you remove a user from an assigned group and the user is still listed as ACTIVE in Dremio, check the *Assignments* tab in the Dremio application to make sure the user isn't separately assigned as a person. Okta only sends deactivate requests for users who are both unassigned as a person and removed from assigned groups.

Was this page helpful?

* Prerequisites
* Supported Features
* Configure OIDC SSO
  + Assign People and Groups to the Dremio Application
  + Use Okta SSO to Log In to Dremio
  + Revoke Okta SSO Login for a User or Group
  + Troubleshoot
* Configure Okta with SCIM
  + Prerequisites
  + Supported Features
  + Configure SCIM Provisioning
  + Create Users
  + Update User Attributes
  + Deactivate Users
  + Group Push
  + Troubleshoot

<div style="page-break-after: always;"></div>

# Social Identity Providers | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/idp/social-idp

On this page

A social identity provider (IdP) enables users to log in to Dremio using their existing accounts from these services. You can use the following providers:

* GitHub
* Google
* Microsoft

By default, these options are preconfigured and active, which means they are immediately available as login options for users unless deactivated by an admin.

## Log In with a Social IdP

Follow these steps to log in to your organization with an enabled social IdP:

1. Navigate to Dremio's login screen, enter your email address, and proceed to the next screen.
2. Click the icon of the desired social IdP (GitHub, Google, or Microsoft) that you want to use. You will be redirected to the corresponding provider's login page.

   ![Social login interface](/images/cloud/social-login.png)
3. Enter your credentials. If successful, you will be redirected to the Dremio homepage.

## Activate and Deactivate Social IdPs

You must be an admin to activate or deactivate a social IdP. Follow these steps to deactivate or activate social providers:

1. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar and then select **Organization settings**.
2. Select **Authentication** from the organization settings sidebar.
3. To deactivate a provider, toggle **Enabled** to off. Deactivating a social IdP removes this IdP as a login option for all users in your organization.
4. To activate a deactivated, toggle **Enabled** to on.

Was this page helpful?

* Log In with a Social IdP
* Activate and Deactivate Social IdPs

<div style="page-break-after: always;"></div>

# Application Authentication | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/app-authentication/

On this page

Application authentication enables programmatic access to Dremio for automated workflows, integrations, and service-to-service communication. Unlike user authentication, which is designed for interactive sessions, application authentication provides secure, token-based access for applications, scripts, and third-party tools.

Application authentication is essential for:

* **API Integrations**: Connecting BI tools, ETL pipelines, and custom applications.
* **Automated Workflows**: Scheduled data processing and reporting tasks.
* **Service-to-Service Communication**: Microservices accessing Dremio resources.
* **CI/CD Pipelines**: Automated testing and deployment processes.

Dremio supports two primary application authentication methods that differ fundamentally in their authentication flow and token issuance:

| Method | Authentication Flow | Token Issuer | Best For |
| --- | --- | --- | --- |
| **OAuth Applications** | Redirect to Dremio login, user authenticates, redirect back with token | OAuth access token from Dremio | Third-party applications, custom applications requiring standard OAuth |
| **External Token Providers** | User authenticates with enterprise IdP, JWT used directly with Dremio | JWT from your identity provider, OAuth access token from Dremio | Enterprise SSO environments, existing JWT infrastructure |

### OAuth Applications

OAuth 2.0 provides secure, standardized authorization for third-party applications. This method is ideal when you need user consent or want to integrate with applications that already support OAuth flows.

**Key Features:**

* Supports industry-standard OAuth 2.0 flows
* Manages granular permissions through Dremio [role-based access control](/dremio-cloud/security/privileges) and [access policies](/dremio-cloud/manage-govern/row-column-policies)
* Logs user activity

### External Token Providers

External token providers allow you to use JSON Web Tokens (JWTs) issued by your existing OAuth server or identity provider. This approach is ideal for enterprises with established identity infrastructure.

**Key Features:**

* Leverages existing identity systems
* Supports custom claims and token validation
* Integrates with enterprise SSO
* Manages centralized tokens

Was this page helpful?

* OAuth Applications
* External Token Providers

<div style="page-break-after: always;"></div>

# Personal Access Tokens | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/personal-access-token

On this page

Personal access tokens (PATs) are randomly generated tokens associated with a user that are used in place of a password to authenticate with Dremio. PATs can last up to 180 days before they expire and provide a secure way to enable programmatic access, automation, and CI/CD workflows.

When using a PAT, you have the same [privileges](/dremio-cloud/security/privileges) and [roles](/dremio-cloud/security/roles) as the user who created the token. This means a PAT can only access what the user can access.

## When to Use PATs

Dremio recommends using [OAuth access tokens](/dremio-cloud/api/oauth-token) for most use cases, as they provide enhanced security through shorter lifespans and centralized management. PATs should primarily be used in scenarios where OAuth tokens are not supported or practical.

PATs may be appropriate for:

* **Legacy systems:** Applications that cannot support OAuth authentication flows.
* **Simple scripts:** Quick automation tasks where OAuth setup overhead is not justified.
* **Development and testing:** Temporary access for development workflows.
* **ODBC/JDBC connections:** When OAuth is not supported by the client application.

## Create a PAT

To create a PAT:

1. Click the User icon (user initials) on the side navigation bar and select **Account Settings**.
2. Select **Personal Access Tokens** in the account settings sidebar.
3. On the Personal Access Tokens page, click **Generate Token** in the top-right corner of the screen.
4. In the Generate Token dialog, for **Label**, add a descriptive identifier explaining what the PAT is for (e.g., "CI Pipeline - Data Tests" or "Tableau Integration").
5. For **Lifetime**, enter the number of days the PAT will be valid. The default PAT lifetime is 30 days, and the maximum lifetime is 180 days.
6. Click **Generate**.
7. **Important:** Copy the generated PAT immediately and save it to a secure location. The token is shown only once and cannot be retrieved later.

## Manage PATs

### View PAT Metadata

A PAT is shown only once during creation. However, you can view the token ID, label, creation date, and expiration status for all PATs in your account.

To view the metadata for all the PATs you have created:

1. Click the User icon (user initials) on the side navigation bar and select **Account Settings**.
2. Select **Personal Access Tokens** from the settings sidebar.

The Personal Access Tokens page displays all the metadata for PATs, both active and expired, for your account.

### Delete a PAT

Each user can delete PATs in their own account.

To delete an existing PAT:

1. Click the User icon (user initials) on the side navigation bar and select **Account Settings**.
2. Select **Personal Access Tokens** in the account settings sidebar.
3. On the Personal Access Tokens page, click ![Delete](/images/icons/trash.png "Delete") for the PAT that you want to delete.
4. In the Delete Token dialog, click **Delete** to confirm. The PAT is deleted and cannot be retrieved.

### Delete All PATs

Any user can delete all PATs from their own account. ADMIN users cannot delete PATs on behalf of other users.

To delete all PATs for your account:

1. Click the User icon (user initials) on the side navigation bar and select **Account Settings**.
2. Select **Personal Access Tokens** in the account settings sidebar.
3. On the Personal Access Tokens page, click **Delete All** in the top-right corner of the screen.
4. In the Delete All Tokens dialog, click **Delete** to confirm that you want to delete all PATs in the list. After a PAT has been deleted, it cannot be retrieved.

## Use PATs

PATs can be used to authenticate with various Dremio interfaces:

* **[REST API](/dremio-cloud/api):** Use PATs for programmatic access and automation.
* **[JDBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-jdbc):** Connect applications using JDBC drivers.
* **[ODBC](/dremio-cloud/explore-analyze/client-apps/drivers/arrow-flight-sql-odbc):** Connect applications using ODBC drivers.
* **Dremio web application:** Use your PAT as a password to log in.

For specific connection details and examples, see the documentation for each connection method.

## Limits and Considerations

* **Self-service only:** Users can only create and manage PATs for themselves—even ADMIN users cannot create or manage PATs on behalf of other users.
* **User permissions:** PATs are tied to user accounts—if a user is deactivated, their PATs stop working.
* **No privilege restriction:** PATs cannot be scoped to fewer privileges than the user has.
* **Token management:** Use descriptive labels and set appropriate expiration times for each token.

Was this page helpful?

* When to Use PATs
* Create a PAT
* Manage PATs
  + View PAT Metadata
  + Delete a PAT
  + Delete All PATs
* Use PATs
* Limits and Considerations

<div style="page-break-after: always;"></div>

# Microsoft Entra ID | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/idp/microsoft-entra-id

On this page

Dremio supports Microsoft Entra ID as an enterprise identity provider. Microsoft Entra ID administrators can follow these instructions to enable single sign-on (SSO) authentication and allow users to log in to Dremio using Microsoft Entra ID as the trusted third party.

## Prerequisites

Configuring SSO in Microsoft Entra ID requires:

* Privileges in Microsoft Entra ID that permit you to add, configure, and register applications.
* The CONFIGURE SECURITY [organization-level privilege](/dremio-cloud/security/privileges/#organization-privileges) or membership in the [ADMIN role](/dremio-cloud/security/roles/).

## Configure an Application for SSO

To configure SSO in Microsoft Entra ID for Dremio users:

1. In the [Azure portal](https://portal.azure.com/#home) under **Azure services**, click the **Microsoft Entra ID** tile.
2. In the left navigation menu under **Manage**, click **App registrations**.
3. Click **New registration**.
4. Type a name for the application in the **Name** field.
5. Select your desired account type in the **Supported account types** list. The default selection is `Accounts in this organizational directory only (<your org> only - Single tenant)`.
6. Under **Redirect URI**, in the **Select a platform** dropdown list, select **Web** and enter the following URI in the provided field:

   * US region: <https://accounts.dremio.cloud/login/callback>
   * EMEA region: <https://accounts.eu.dremio.cloud/login/callback>
7. Click **Register**.
8. Copy and save the value for the `Application (client) ID`. You will use it to configure authentication in Dremio later in this procedure.
9. In the left navigation menu under **Manage**, click **Certificates & secrets**.
10. Click **New client secret**.
11. In the **Add a client secret** panel, type a description for the secret in the **Description** field and select your desired lifespan for the secret in the **Expires** dropdown list.
12. Click **Add**.
13. Copy and save the value for the secret. The secret value is sensitive information and should be kept private. You will use it to configure authentication in Dremio later in this procedure.
14. In the left navigation menu under **Manage**, click **API permissions**.
15. Confirm that the following permission is listed under \**API / Permissions name*:

    * **User.Read**: Permits users to log in to the application and permits the application to read the profiles and basic company information for logged-in users.
16. Click **Add a permission**.
17. In the **Request API permissions** panel, click the **Microsoft Graph** tile.
18. Click the **Delegated permissions** tile.
19. Under **OpenId permissions**, click the checkboxes next to the following options:

    * **email**: Permits the application to read users' primary email addresses.
    * **openid**: Permits users to sign in to the application with their work or school accounts and permits the application to view basic user profile information.
    * **profile**: Permits the application to view basic user profile information (name, avatar, and email address).
20. Click **Add permissions**. The list of configured permissions should now include the following permissions:

    * email
    * openid
    * profile
21. In the left navigation menu under **Manage**, click **Branding & properties**.
22. Copy and save the **Publisher domain** (`<domain_name>.onmicrosoft.com`). You will use it to configure authentication in Dremio later in this procedure.
23. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and then select **Organization settings**.
24. Click the **Authentication** tab in the left sidebar.
25. In the **Enterprise** section, click **Add Provider** to open the Add Provider dialog.
26. In Step 1, select **Microsoft Entra ID** in the dropdown list.
27. In Step 3, enter the domain, client ID, and secret information that you copied from Microsoft Entra ID in the corresponding fields.
28. Click **Add**. After the page loads, you should see Microsoft Entra ID listed as an authentication provider in the **Enterprise** section.
29. Click the **Enabled** toggle to activate the Microsoft Entra ID authentication provider.

Microsoft Entra ID is now configured as an enterprise authentication provider. **Log in with Microsoft Entra ID** appears in the list of login options for your Dremio users. Any Microsoft Entra ID user in your organization can use **Log in with Microsoft Entra ID** for SSO login.

### Assign People and Groups to the Microsoft Entra ID Application

The Microsoft Entra ID application is configured to allow SSO login for any Microsoft Entra ID user in your organization. To adjust the application settings so that only users who are assigned to the app can use Microsoft Entra ID SSO to log in to Dremio:

1. In the [Azure portal](https://portal.azure.com/#home) under **Azure services**, click the **Microsoft Entra ID** tile.
2. In the left navigation menu under **Manage**, click **Enterprise applications**.
3. Click the name of the SSO application.
4. In the left navigation menu under **Manage**, click **Properties**.
5. Find the **Assignment required?** toggle and click **Yes**.
6. Click **Save**.

With user assignment required, users who are not assigned to the application receive an error message from Microsoft when they try to use Microsoft Entra ID SSO for Dremio.

Follow the instructions in the Microsoft Entra ID documentation to [assign users and groups](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal?pivots=portal) to your application.

Before the user can click **Log in with Microsoft Entra ID** in the list of login options for Dremio, one of the following conditions must be met:

* The user has been invited by an admin and has activated their account through an email link.
* An admin has set up SCIM provisioning and synced the user via SCIM.

Use [privileges](/dremio-cloud/security/privileges/) and [roles](/dremio-cloud/security/roles/) to manage user access to objects in Dremio.

### Use Microsoft Entra ID SSO to Log in to Dremio

To use Microsoft Entra ID SSO to log in to Dremio:

1. Open the Dremio console login page:

   * US region: <https://app.dremio.cloud/>
   * EMEA region: <https://app.eu.dremio.cloud/>
2. Type your email address in the **Email** field and click **Continue**.
3. Click **Log in with Microsoft Entra ID**.
4. You will be redirected to the Microsoft website for authentication.
5. Microsoft Entra ID authenticates your identity and redirects you to Dremio, which then logs you in.

You can use the Microsoft Entra ID SCIM provisioning feature to sync groups and memberships from Microsoft Entra ID to Dremio and manage access for Dremio users and groups. To configure, see Configure Microsoft Entra ID with SCIM.

### Revoke Microsoft Entra ID SSO Login for a User or Group

To revoke users' access to Microsoft Entra ID SSO login for Dremio:

1. In Microsoft Entra ID, navigate to your application.
2. Find the row for the user or group you want to deactivate and click to select the checkbox for the user or group.
3. Click **Remove**.
4. In the confirmation dialog, click **Yes**.

Starting immediately, the users cannot use Microsoft Entra ID SSO to log in to Dremio.

If you revoke a user's access to use Microsoft Entra ID SSO login in Microsoft Entra ID and the user has created a Dremio password for login, they can still log in to Dremio with their Dremio username and password. To completely delete Dremio users so that they cannot log in to Dremio at all, you must also delete or deactivate the user through SCIM provisioning or [manually remove their user accounts in Dremio](/dremio-cloud/admin/users#remove-a-user).

## Configure Microsoft Entra ID with SCIM

System for Cross-domain Identity Management (SCIM) automates the synchronization of user accounts between your identity provider (IdP) and Dremio, eliminating the need for manual user management. When configured, your IdP securely sends user credentials to Dremio via SCIM, automatically creating accounts for new users as needed. These users can then log in to Dremio according to your organization's authentication policies.

### Prerequisites

Configuring SCIM provisioning in Microsoft Entra ID requires:

* Privileges in Microsoft Entra ID that permit you to register and configure applications.
* A Dremio [personal access token (PAT)](/dremio-cloud/security/authentication/personal-access-token#create-a-pat) for a Dremio user who is a member of the ADMIN role.

### Configure an Application for SCIM Provisioning

To create an application for SCIM provisioning in Microsoft Entra ID:

1. In the [Azure portal](https://portal.azure.com/#home) under **Azure services**, click the **Microsoft Entra ID** tile.
2. In the left navigation menu under **Manage**, click **Enterprise applications**.
3. Click **New application**.
4. Click **Create your own application**.
5. In the **Create your own application** panel, type a name for the application in the provided field.
6. Under **What are you looking to do with your application?** select the **Integrate any other application you don't find in the gallery (Non-gallery)** option.
7. Click **Create**.
8. In the left navigation menu under **Manage**, click **Provisioning**.
9. Click **Get started**.
10. In the **Provisioning Mode** dropdown list, select **Automatic**.
11. Under **Admin Credentials**, enter the correct **Tenant URL** for your control plane:

    * US control plane: `https://scim.dremio.cloud/scim/v2/?aadOptscim062020`
    * EU control plane: `https://scim.eu.dremio.cloud/scim/v2/?aadOptscim062020`

    note

    The Tenant URL must include the `aadOptscim062020` query parameter due to a [Microsoft Entra ID issue with SCIM 2.0 compliance](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/application-provisioning-config-problem-scim-compatibility).

    If you previously configured a SCIM app with Microsoft Entra ID, SCIM syncing may fail for requests to deactivate users, add and update user attributes, and remove group members. If you observe these failures, follow the Microsoft documentation to [upgrade from the older customappsso job to the SCIM job](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/application-provisioning-config-problem-scim-compatibility#upgrading-from-the-older-customappsso-job-to-the-scim-job).
12. Enter your Dremio PAT in the **Secret Token** field.
13. (Optional) Click **Test Connection** to confirm that Microsoft Entra ID can connect to the tenant URL.
14. Click **Save**.
15. (Optional) Click the down arrow next to **Settings** and adjust the settings as desired. Click **Save** when you are finished.
16. Return to the **Provisioning Overview** page for the application.
17. In the left navigation menu under **Manage**, click **Provisioning**.
18. Under **Provisioning Status**, toggle the setting to **On**.
19. Click **Save**.

SCIM provisioning is now configured and enabled. You can create users, update user attributes, and deactivate users in Dremio, all from Microsoft Entra ID.

Read Microsoft's documentation about [how long it takes to provision users](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/application-provisioning-when-will-provisioning-finish-specific-user#how-long-will-it-take-to-provision-users) for details about Microsoft Entra ID's initial and incremental provisioning cycles.

If desired, you can use Microsoft Entra ID's scoping filters to apply attribute-based rules for user provisioning. Read [Scoping users or groups to be provisioned with scoping filters](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/define-conditional-rules-for-provisioning-user-accounts?pivots=app-provisioning) in the Microsoft documentation for more information.

### Create Users

After you configure a Microsoft Entra ID application for SCIM provisioning, you must assign users and groups to the application. Dremio automatically creates a new Dremio user account for anyone you assign to the SCIM application who does not already have an account. Follow the instructions in the Microsoft documentation to [assign users and groups to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal?pivots=portal).

### Create Roles

If you add a group to your SCIM application in Microsoft Entra ID, your designated group becomes a role in Dremio populated with the group's members. Follow the instructions in the Microsoft documentation to [assign users and groups to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal?pivots=portal).

Use Microsoft Entra ID to manage any roles you create with groups. Any changes you make to a role or its membership in Dremio are immediately overwritten by the next provisioning cycle from Microsoft Entra ID. Making changes in Dremio can result in synchronization errors.

### Update User Attributes

With SCIM provisioning configured, updates to user attributes in Microsoft Entra ID are propagated to the user account in Dremio. Follow the instructions in the Microsoft documentation to [edit user profile information](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info).

* **First name** and **Last name** attributes in Microsoft Entra ID are mapped to user accounts in Dremio. After you configure an application for SCIM provisioning in Microsoft Entra ID and assign users to it, you can change these user attributes in Microsoft Entra ID to update the corresponding user information in Dremio.
* Microsoft Entra ID controls user **email addresses**. If a user's email address changes, you must create a new user in Microsoft Entra ID and assign them to the application for SCIM provisioning. Then, assign the new Microsoft Entra ID user to the SCIM application (either individually as a user or by adding them to an assigned group). Microsoft Entra ID creates a new Dremio user who can log in to Dremio with the new email address as a new user.

### Deactivate Users

When you delete a user or group from the application for SCIM provisioning in Microsoft Entra ID, the affected users become inactive in Dremio and cannot log in to Dremio at all, whether with Microsoft Entra ID SSO or username and password.

To delete a user or group from your SCIM application in Microsoft Entra ID:

1. In the [Azure portal](https://portal.azure.com/#home) under **Azure services**, click the **Microsoft Entra ID** tile.
2. In the left navigation menu under **Manage**, click **Enterprise applications**.
3. Find your SCIM application in the list and click the application's name.
4. In the left navigation menu under **Manage**, click **Users and groups**.
5. Click to select the checkbox for the user or group you want to remove.
6. Click **Remove**.
7. In the confirmation dialog, click **Yes**.

The users you deleted, whether individually or by their group membership, become inactive in Dremio. If you delete a group, Microsoft Entra ID automatically removes the group's corresponding role in Dremio.

If you delete a group in Microsoft Entra ID, the group's corresponding role is automatically removed in Dremio and the group members' Dremio user accounts are set to inactive. Deleting a Microsoft Entra ID group does not delete the group members' Dremio user accounts.

To completely delete Dremio users, you must [manually remove their user accounts in Dremio](/dremio-cloud/admin/users#remove-a-user) in addition to deleting the users and any groups they belong to from the SCIM application in Microsoft Entra ID.

Was this page helpful?

* Prerequisites
* Configure an Application for SSO
  + Assign People and Groups to the Microsoft Entra ID Application
  + Use Microsoft Entra ID SSO to Log in to Dremio
  + Revoke Microsoft Entra ID SSO Login for a User or Group
* Configure Microsoft Entra ID with SCIM
  + Prerequisites
  + Configure an Application for SCIM Provisioning
  + Create Users
  + Create Roles
  + Update User Attributes
  + Deactivate Users

<div style="page-break-after: always;"></div>

# Generic OIDC | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/idp/generic-oidc-provider

On this page

Dremio supports the generic [OpenID Connect (OIDC)](https://openid.net/) authentication protocol as an enterprise identity provider. OIDC provider administrators can register a Dremio application and use it to enable single sign-on (SSO) and allow users to log in using an OIDC provider as the trusted third party.

note

To configure Microsoft Entra ID or Okta as an identity provider, see:

* [Microsoft Entra ID as an Identity Provider](/dremio-cloud/security/authentication/idp/microsoft-entra-id)
* [Okta as an Identity Provider](/dremio-cloud/security/authentication/idp/okta)

Dremio also allows you to use System for Cross-domain Identity Management (SCIM) provisioning to manage Dremio user access from your OIDC provider. After you configure your provider for OIDC SSO, refer to your OIDC provider's documentation to configure SCIM. See [SCIM with a Generic OpenID Connect Provider](/dremio-cloud/security/authentication/idp/generic-oidc-provider/#configure-a-generic-openid-connect-provider-with-scim) to use SCIM provisioning in Dremio.

## Prerequisites

Configuring SSO in a generic OIDC provider requires:

* Privileges in the OIDC provider that permit you to add, configure, and register applications.
* The CONFIGURE SECURITY [organization-level privilege](/dremio-cloud/security/privileges#organization-privileges) or membership in the [ADMIN role](/dremio-cloud/security/roles#admin).

## Configure OIDC SSO

To configure OIDC SSO for Dremio users:

1. **In Dremio**, on the organization page, click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar, then select **Organization settings**.
2. Select **Authentication** in the organization settings sidebar.
3. Click **Add Provider** to open the Add Provider dialog.
4. In Step 1, select **OpenID Connect (OIDC)** from the dropdown menu.
5. Copy and save the **Redirect URL** listed in Step 2. The redirect URL is sensitive information and should be kept secure. You will need it to register the `Dremio` application in your OIDC provider portal in the next step.
6. **In your OIDC provider portal**, register `Dremio` as an application.
7. Copy and save the client ID and client secret for your OIDC provider. The client ID and client secret are sensitive information and should be kept secure. You will use them to configure authentication in Dremio later in this procedure.
8. Copy and save the `issuer` value from the OIDC configuration. You will use it to configure authentication in Dremio later in this procedure.
9. **In Dremio**, in Step 3 of the **Add Provider** dialog, enter the issuer URL, client ID, and client secret that you copied from your OIDC provider portal in the corresponding fields.
10. Click **Add**. After the page loads, you should see your OIDC provider in the **Enterprise** section.
11. Click the **Enabled** toggle to activate your OIDC provider.

OIDC as an enterprise identity provider is now configured. **Log in with SSO** appears in the list of login options for your Dremio users.

### Use SSO to Log In to Dremio

Any user who is assigned to the `Dremio` application in your OIDC provider can log in with SSO immediately. To use SSO to log in to Dremio:

1. Open the Dremio login page.
2. Type your email address in the **Email** field and click **Continue**.
3. If you belong to more than one Dremio organization, select the organization to log in to.
4. Click **Log in with SSO**.
5. When you are redirected to your OIDC provider for authentication, enter your username and password.

The OIDC provider authenticates your identity and redirects you to Dremio, which then logs you in.

To configure SCIM provisioning to manage access for Dremio users, see [SCIM with a Generic OpenID Connect Provider](/dremio-cloud/security/authentication/idp/generic-oidc-provider/#configure-a-generic-openid-connect-provider-with-scim).

### Revoke SSO Login for a User or Group

To revoke users' access to SSO login for Dremio:

1. In your OIDC provider's portal, navigate to the `Dremio` application.
2. Open the assignment settings for the `Dremio` application.
3. Find the user or group whose access you want to revoke and follow your OIDC provider's procedures to revoke access.

Starting immediately, the deactivated users cannot use OIDC SSO to log in to Dremio.

To completely delete Dremio users, you must also [manually remove their user accounts in Dremio](/dremio-cloud/admin/users#remove-a-user).

## Configure a Generic OpenID Connect Provider with SCIM

System for Cross-domain Identity Management (SCIM) automates the synchronization of user accounts between your identity provider (IdP) and Dremio, eliminating the need for manual user management. When configured, your IdP securely sends user credentials to Dremio via SCIM, automatically creating accounts for new users as needed. These users can then log in to Dremio according to your organization's authentication policies.

Before you can configure SCIM provisioning, you must configure a generic OIDC provider as an enterprise identity provider in Dremio. Follow the instructions in [Generic OpenID Connect Identity Provider](/dremio-cloud/security/authentication/idp/generic-oidc-provider) to integrate a `Dremio` application in a generic OIDC provider for single sign-on (SSO) in Dremio. When that is done, follow this guide to configure SCIM for secure user provisioning.

### Prerequisites

Configuring SCIM provisioning requires:

* Privileges in your OIDC provider that permit you to register and configure applications.
* The CONFIGURE SECURITY [organization-level privilege](/dremio-cloud/security/privileges#organization-privileges) or membership in the [ADMIN role](/dremio-cloud/security/roles#admin).
* A Dremio [personal access token (PAT)](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat) for a Dremio user who is a member of the ADMIN role.

### Configure SCIM Provisioning

The steps required to configure and enable SCIM provisioning vary for different OIDC providers. Follow the instructions in your OIDC provider's documentation.

Use a Dremio [PAT](/dremio-cloud/security/authentication/personal-access-token/#create-a-pat) as the **API Token** or **Secret Token** value when you configure authentication for SCIM requests in your OIDC provider's portal.

US Control Plane

```
https://scim.dremio.cloud/scim/v2
```

EU Control Plane

```
https://scim.eu.dremio.cloud/scim/v2
```

After SCIM provisioning is configured and enabled, you can create users, update user attributes, and deactivate users in Dremio from your OIDC provider's portal.

### Create Users

After you configure SCIM provisioning, Dremio automatically creates a new Dremio user account for anyone you assign to the `Dremio` application in your OIDC provider who does not already have an account. New Dremio users can log in to Dremio with SSO immediately, and administrators can [view their user accounts in Dremio](/dremio-cloud/admin/users#view-all-users).

* New users are automatically members of the PUBLIC role in Dremio.
* User email addresses are controlled by your OIDC provider rather than Dremio. If a user's email address changes, you must create a new user in your OIDC provider and assign them to the `Dremio` application. Then, the user can use the new email address to log in to Dremio as a new user.

### Update User Attributes

With SCIM provisioning configured, updates to user attributes in your OIDC provider are propagated to the user account in Dremio.

The first name and last name attributes are mapped to user accounts in Dremio. After you configure SCIM provisioning and allow user attributes to be updated, you can change these user attributes in your OIDC provider to update the corresponding user information in Dremio.

### Deactivate Users

When you revoke a user or group in your OIDC provider, the affected users cannot use OIDC SSO to log in to Dremio. After you configure SCIM provisioning and deactivate users, they become inactive in Dremio and cannot log in to Dremio at all with SSO.

To completely delete Dremio users, you must also [manually remove their user accounts in Dremio](/dremio-cloud/admin/users/#remove-a-user).

## Troubleshoot

This section describes some considerations about OIDC SSO and SCIM provisioning with the `Dremio` application in your OIDC provider.

* **SCIM provisioning**
  + Dremio does not allow username updates. If you change a user's username in your OIDC provider after the user is assigned to the `Dremio` application, the OIDC provider sends a request to update the username in Dremio. Dremio denies the request because Dremio username changes are not allowed.
  + Changing an existing user's primary email address in the OIDC provider has no effect on the user's account in Dremio. To permit a user to authenticate to Dremio with the new email address, add the user to your OIDC provider as a new person using the new email address. Then, assign the new user to the `Dremio` application (either individually as a person or by adding them to an assigned group). The OIDC provider creates a new Dremio user who can use SSO to log in to Dremio with the new email address.
* **OIDC SSO**
  + Refer to your OIDC provider's documentation to ensure that you have privileges that permit you to add the `Dremio` application in your OIDC provider and configure OIDC SSO.
  + If you revoke a user's access to SSO login, the user can still log in to Dremio with their Dremio username and password. To completely delete the user so that they cannot log in to Dremio at all, you must [manually remove their user accounts in Dremio](/dremio-cloud/admin/users#remove-a-user).

Was this page helpful?

* Prerequisites
* Configure OIDC SSO
  + Use SSO to Log In to Dremio
  + Revoke SSO Login for a User or Group
* Configure a Generic OpenID Connect Provider with SCIM
  + Prerequisites
  + Configure SCIM Provisioning
  + Create Users
  + Update User Attributes
  + Deactivate Users
* Troubleshoot

<div style="page-break-after: always;"></div>

# Prerequisites

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/app-authentication/oauth-apps

On this page

This topic describes how to configure OAuth applications to integrate third-party applications with Dremio. This allows Dremio and third-party applications to interact without exposing user login credentials. For example, an organization might use GitLab accounts to access Dremio. In the unlikely event of a Dremio data breach, the organization's login credentials would remain unaffected and protected.

Additional authentication and security measures are available in [Authentication](/dremio-cloud/security/authentication/).

* **Native** – Mobile, desktop, CLI, and smart device apps that run natively on their respective operating systems, such as iOS and Chrome OS.
* **Single-Page Application (SPA)** – JavaScript-enabled, front-end applications that use an API, such as Angular, React, and Vue.
* **Web** – Traditional web applications that utilize redirects, such as Java, PHP, and ASP.NET.

# Prerequisites

Before setting up OAuth applications, ensure you have:

* Dremio admin privileges or the CONFIGURE SECURITY privilege.
* An OIDC-compliant Identity Provider (IDP) configured in Dremio if OAuth applications will rely on external authentication.

## Add an OAuth App

To add a new OAuth application in Dremio:

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and select **Organization settings**, then select **OAuth Applications**.
2. Click **Add Application** in the top-right corner of the screen.
3. Enter a value for **OAuth Application Name** to identify the associated service.
4. Enter a value for **Redirect URI**. This value is used as the destination for return responses (tokens) after successfully authenticating a user. If there is an issue with the provided URI's format, red text will display below the field to indicate the required format.
5. Select the desired **OAuth Application Type** from the dropdown menu. The type of application selected determines which authentication flow Dremio will follow. This cannot be changed after the application is added.
6. Click **Add** to create the application service. A success message will appear at the top of the screen.

Upon creating the application, the dialog will refresh with a new field: **Client ID**. Copy this value, as it is needed to link with the third-party OAuth application. Include this string where the **Client ID** is required by your respective OAuth application.

## Edit an OAuth App

To edit an existing OAuth application in Dremio:

1. Click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar and select **Organization settings**, then select **OAuth Applications**.
2. Click the edit icon for the desired application.
3. Make any necessary changes to the application name or redirect URI. You cannot change the **Client ID** or **OAuth Application Type**.
4. Click **Save**.

Was this page helpful?

* Add an OAuth App
* Edit an OAuth App

<div style="page-break-after: always;"></div>

# External Token Providers | Dremio Documentation

Original URL: https://docs.dremio.com/dremio-cloud/security/authentication/app-authentication/external-token

On this page

External token providers are OIDC identity providers that issue [JSON Web Tokens (JWTs)](https://jwt.io/introduction) when a user authenticates using an application client. After receiving a JWT from the external token provider, the client application uses [Dremio token exchange](/dremio-cloud/api/oauth-token/#exchange-an-external-jwt) to obtain an OAuth access token used to create connections to Dremio.

![](/assets/images/token-flowchart-7badc94d022760d37f480ecb5fee43ec.png)

The OIDC external token provider does not need to be the same identity provider used by the Dremio console for single sign-on (SSO). The provider requires an application registration specifying the OAuth authorization flow to be used between the external token provider and the client to obtain the JWT that will be sent to Dremio.

This page outlines the steps for configuring an external token provider so Dremio can interpret and validate the JWTs issued by your provider.

The [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) describes the content of the JWT and the authorization process. Claims in a JWT contain information asserted about a subject. They are key/value pairs in which the key is a string, and the value can be any JSON type (a string, a number, a boolean, an array, or a JSON object).

Example: External JWT Claims from Microsoft Entra ID

```
{  
  "aud": "0853fce0-c748-4c54-aa58-f5b9af279840",  
  "iss": "https://login.microsoftonline.com/3e334762-b0c6-4c36-9faf-93800f0d6c71/v2.0",  
  "upn": "gnarly@dremio.com"  
}
```

## Prerequisites

Before setting up External Token Providers, ensure you have:

* Dremio admin privileges or the CONFIGURE SECURITY privilege.
* An OIDC-compliant Identity Provider configured with an application registration for your client.
* Access to the following information from your IDP:
  + **Audience** – Application ID or resource URI
  + **User claim mapping** – The claim containing the Dremio username
  + **Issuer URL** – Identity provider identification
  + **JWKS URL** – Optional location of public keys

## Define an External Token Provider

Dremio requires the following configuration values from your OIDC identity provider.

tip

The examples below are specific to Microsoft Entra ID. Your identity provider may require additional configuration of a client application registration that depends on the OAuth authorization flow used between your client and your provider. To configure your application registration, consult your identity provider documentation.

### Audience

The audience value identifies the intended recipients of the external JWT. It can generally be an array of case-sensitive strings or URI values. The audience is contained in the `aud` claim in the external JWT.

When using Microsoft Entra ID, the audience can be the Application ID assigned to your app in the Microsoft Entra ID portal or the resource URI. In v2.0 tokens, this value is always the [Application ID](https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference). In v1.0 tokens, it can be the Application ID or the [resource URI](https://learn.microsoft.com/en-us/entra/identity-platform/access-token-claims-reference) used in the request, depending on how the client requested the token. Dremio supports v1.0 and v2.0 JWTs from Microsoft Entra ID.

Example Audience Claim with Microsoft Entra ID Application ID

```
"aud": "0853fce0-c748-4c54-aa58-f5b9af279840"
```

### User Claim Mapping

The user claim mapping identifies the claim in the external JWT that contains the Dremio username.

When using Microsoft Entra ID authentication, Dremio usernames must align with the [User Principal Name (UPN)](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-userprincipalname#upn-in-microsoft-entra-id) claim for correct linking of user group memberships via the Azure Graph Client.

When a user is added to a Power BI workspace, the user's identity is also represented by the [User Principal Name (UPN)](https://learn.microsoft.com/en-us/answers/questions/1663403/upn-changing-when-adding-external-user-to-bi-works), which has the format of an email address.

The JWT contains the UPN claim, named `upn`, and its value.

Example: UPN Claim from Microsoft Entra ID

```
"upn": "gnarly@dremio.com"
```

The `user claim mapping` field of the external token provider requires the name of the claim used in the JWT, which in this case is `upn`.

### Issuer URL

The issuer URL identifies the identity provider that issued the JWT. It is contained in the external JWT's `iss` claim. When using Microsoft Entra ID, [the issuer claim](https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference) includes the Microsoft Entra ID tenant identifier. Only one external token provider in the system should use the combination of a given audience and issuer.

Example Issuer Claim with Microsoft Entra ID

```
"iss": "https://login.microsoftonline.com/3e334762-b0c6-4c36-9faf-93800f0d6c71/v2.0"
```

### JWKS URL

The JWKS URL is an endpoint that hosts the [JWK Set (JWKS)](https://datatracker.ietf.org/doc/html/rfc7517), a set of public keys used for verifying the JWT signature. This value is optional; if you do not provide a JWKS URL value when configuring the external token provider, Dremio retrieves the JWKS URL from `{issuer URL}/.well-known/openid-configuration`.

For Microsoft Entra ID, the [JWKS URL](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens) is typically of the form `https://login.microsoftonline.com/{tenant_id}/discovery/v2.0/keys`.

Example: JWKS URL from Microsoft Entra ID

```
https://login.microsoftonline.com/58a43618-7933-4e0d-906e-1c1a2a867ad6/discovery/v2.0/keys
```

## Manage External Token Providers

The Dremio administrator or a user with the [CONFIGURE SECURITY](/dremio-cloud/security/privileges#organization-privileges) privilege can view and manage external token providers in Dremio.

### View External Token Providers

To view external token providers:

1. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") on the left navigation bar, and select **Organization settings**.
2. Click **External Token Providers**. The External Token Providers page lists the external token providers configured for Dremio.

### Add an External Token Provider

To add an external token provider:

1. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar, and select **Organization settings**.
2. Click **External Token Providers**.
3. Click **Add Provider** at the top-right corner of the External Token Providers page.
4. In the Add Provider dialog, complete the configuration using the fields described in Define an External Token Provider.
5. Click **Add**.

When you add an external token provider, Dremio automatically enables it. To deactivate it, toggle the Enabled switch on the External Token Providers page.

Each external token provider must use a different combination of issuer and audience. If multiple external token providers share the same issuer and audience, authentication will fail regardless of whether the token providers are enabled.

### Edit an External Token Provider

To edit an external token provider:

1. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar, and select **Organization settings**.
2. Click **External Token Providers**.
3. On the External Token Providers page, find the row for the external token provider you want to edit and click ![Edit](/images/icons/edit.png "Edit") at the right side of the row.
4. In the Edit Provider dialog, update the values using the fields described in Define an External Token Provider.
5. Click **Save**.

### Delete an External Token Provider

To delete an external token provider:

1. In the Dremio console, click ![Settings](/images/icons/settings.png "Settings") in the side navigation bar, and select **Organization settings**.
2. Click **External Token Providers**.
3. On the External Token Providers page, find the row for the external token provider you want to delete and click ![Delete](/images/icons/trash.png "Delete") at the right side of the row.
4. In the Delete External Provider dialog, click **Delete**.

## Use the External Token Provider

### Retrieve an External JWT

This sample application uses the [Microsoft Authentication Library](https://learn.microsoft.com/en-us/entra/identity-platform/msal-overview) to authenticate a user with the OAuth authorization code flow.

* `client_id` is the [Application (Client) ID](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration#client-id) assigned to your app by Microsoft Entra ID when the app was registered.
* `app_redirect_url` or [reply URL](https://learn.microsoft.com/en-us/entra/identity-platform/reply-url) is the location of the client app where Microsoft Entra ID sends an external JWT after the user has successfully logged in, such as `https://myapp.com/auth/callback` or `http://localhost:3000/auth/callback`. The redirect URI is defined in the Microsoft Entra ID application registration for the client.
* `dremio_scope_name` is the [API scope](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc) you defined for the client in the Microsoft Entra ID application profile. Dremio requires a scope of `dremio.all` in token exchange, regardless of the scope configured in the application registration.
* `tenant_id` is your Microsoft Entra ID [tenant identifier](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id).

Example: Retrieving a Microsoft JWT

```
import msal  
  
client_id = "TODO"  
app_redirect_url = "TODO"  
dremio_scope_name = "TODO"    
tenant_id = "TODO"  
  
authority_url = "https://login.microsoftonline.com/" + tenant_id  
app = msal.PublicClientApplication(client_id, authority=authority_url)  
auth_code_flow = app.initiate_auth_code_flow(  
    scopes=[dremio_scope_name],  
    redirect_uri=app_redirect_url  
)  # PKCE is included in the MSAL Python library  
  
state = auth_code_flow['state']  
  
authorization_code = "TODO: retrieved from the browser"  
  
external_access_token = ""  
  
if authorization_code:  
    auth_result = app.acquire_token_by_auth_code_flow(  
        auth_code_flow=auth_code_flow,  
        auth_response={"code": authorization_code, "state": state}  
    )  
    if "access_token" in auth_result:  
        external_access_token = auth_result["access_token"]  
    else:  
        print("Error: no access token")  
    if "refresh_token" in auth_result:  
        refresh_token = auth_result["refresh_token"]  
    else:  
        print("Error: no refresh token")  
else:  
    print("Error: no auth code")
```

### Exchange a JWT

The client must use the Dremio `/oauth/token` REST API to [exchange the JWT for an OAuth access token](/dremio-cloud/api/oauth-token#exchange-an-external-jwt).

Was this page helpful?

* Prerequisites
* Define an External Token Provider
  + Audience
  + User Claim Mapping
  + Issuer URL
  + JWKS URL
* Manage External Token Providers
  + View External Token Providers
  + Add an External Token Provider
  + Edit an External Token Provider
  + Delete an External Token Provider
* Use the External Token Provider
  + Retrieve an External JWT
  + Exchange a JWT

<div style="page-break-after: always;"></div>

