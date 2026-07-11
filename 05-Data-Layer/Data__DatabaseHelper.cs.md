# DatabaseHelper.cs
**Source:** `Data/DatabaseHelper.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Legacy/alternate connection helper (same MyDbConn). Prefer DbHelper for new code; kept for older call sites.

## File overview

- **Total lines:** 64
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `ConnString` | `string` | Holds “Conn String” for this scope. (text) |

## Functions / methods (3 found)

### `ExecuteQuery` — lines 11–30

#### Signature

```csharp
public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
```

#### What it is

Runs a SELECT SQL query and returns all matching rows as a DataTable.

#### How it works

1. Open a database connection.
2. Create a SqlCommand with the SQL text and attach any parameters.
3. Use a SqlDataAdapter to fill a DataTable with all result rows.
4. Return that DataTable to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `query` | `string` | Holds “query” for this scope. (text) |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `dt` | `DataTable` | DataTable — full result set from SQL (many rows/columns).  Newly constructed object. |

#### Code

```csharp
  11 | 
  12 |         public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
  13 |         {
  14 |             using (SqlConnection conn = new SqlConnection(ConnString))
  15 |             {
  16 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  17 |                 {
  18 |                     if (parameters != null)
  19 |                     {
  20 |                         cmd.Parameters.AddRange(parameters);
  21 |                     }
  22 |                     using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
  23 |                     {
  24 |                         DataTable dt = new DataTable();
  25 |                         adapter.Fill(dt);
  26 |                         return dt;
  27 |                     }
  28 |                 }
  29 |             }
  30 |         }
```

---

### `ExecuteNonQuery` — lines 31–46

#### Signature

```csharp
public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
```

#### What it is

Runs INSERT/UPDATE/DELETE SQL and returns how many rows changed.

#### How it works

1. Open a database connection.
2. Create a SqlCommand with INSERT/UPDATE/DELETE SQL and parameters.
3. Execute the command and return how many rows were changed.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `query` | `string` | Holds “query” for this scope. (text) |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |

#### Code

```csharp
  31 | 
  32 |         public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
  33 |         {
  34 |             using (SqlConnection conn = new SqlConnection(ConnString))
  35 |             {
  36 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  37 |                 {
  38 |                     if (parameters != null)
  39 |                     {
  40 |                         cmd.Parameters.AddRange(parameters);
  41 |                     }
  42 |                     conn.Open();
  43 |                     return cmd.ExecuteNonQuery();
  44 |                 }
  45 |             }
  46 |         }
```

---

### `ExecuteScalar` — lines 47–62

#### Signature

```csharp
public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
```

#### What it is

Runs SQL that returns a single value (for example COUNT or a new ID).

#### How it works

1. Run SQL that returns one value (count, id, flag).
2. Open a connection to the LocalDB / SQL Server database.
3. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `query` | `string` | Holds “query” for this scope. (text) |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |

#### Code

```csharp
  47 | 
  48 |         public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
  49 |         {
  50 |             using (SqlConnection conn = new SqlConnection(ConnString))
  51 |             {
  52 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  53 |                 {
  54 |                     if (parameters != null)
  55 |                     {
  56 |                         cmd.Parameters.AddRange(parameters);
  57 |                     }
  58 |                     conn.Open();
  59 |                     return cmd.ExecuteScalar();
  60 |                 }
  61 |             }
  62 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Configuration;
   3 | using System.Data;
   4 | using System.Data.SqlClient;
   5 | 
   6 | namespace WebAppAssignment.Data
   7 | {
   8 |     public static class DatabaseHelper
   9 |     {
  10 |         private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"].ConnectionString;
  11 | 
  12 |         public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
  13 |         {
  14 |             using (SqlConnection conn = new SqlConnection(ConnString))
  15 |             {
  16 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  17 |                 {
  18 |                     if (parameters != null)
  19 |                     {
  20 |                         cmd.Parameters.AddRange(parameters);
  21 |                     }
  22 |                     using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
  23 |                     {
  24 |                         DataTable dt = new DataTable();
  25 |                         adapter.Fill(dt);
  26 |                         return dt;
  27 |                     }
  28 |                 }
  29 |             }
  30 |         }
  31 | 
  32 |         public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
  33 |         {
  34 |             using (SqlConnection conn = new SqlConnection(ConnString))
  35 |             {
  36 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  37 |                 {
  38 |                     if (parameters != null)
  39 |                     {
  40 |                         cmd.Parameters.AddRange(parameters);
  41 |                     }
  42 |                     conn.Open();
  43 |                     return cmd.ExecuteNonQuery();
  44 |                 }
  45 |             }
  46 |         }
  47 | 
  48 |         public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
  49 |         {
  50 |             using (SqlConnection conn = new SqlConnection(ConnString))
  51 |             {
  52 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  53 |                 {
  54 |                     if (parameters != null)
  55 |                     {
  56 |                         cmd.Parameters.AddRange(parameters);
  57 |                     }
  58 |                     conn.Open();
  59 |                     return cmd.ExecuteScalar();
  60 |                 }
  61 |             }
  62 |         }
  63 |     }
  64 | }
```
