# DbHelper.cs
**Source:** `Data/DbHelper.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Primary SQL helper: open connection from Web.config MyDbConn, ExecuteQuery / NonQuery / Scalar, parameter factory P(), SafeString. All business SQL should go through this (or AuthService helpers).

## File overview

- **Total lines:** 112
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (11 found)

### `OpenConnection` — lines 23–29

#### Signature

```csharp
public static SqlConnection OpenConnection()
```

#### What it is

Opens a new SQL Server / LocalDB connection using the `MyDbConn` connection string.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |

#### Code

```csharp
  23 | 
  24 |         public static SqlConnection OpenConnection()
  25 |         {
  26 |             var conn = new SqlConnection(ConnectionString);
  27 |             conn.Open();
  28 |             return conn;
  29 |         }
```

---

### `ExecuteQuery` — lines 30–45

#### Signature

```csharp
public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
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
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `adapter` | `var` | SqlDataAdapter — fills a DataTable from a SqlCommand.  Newly constructed object. |

#### Code

```csharp
  30 | 
  31 |         public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
  32 |         {
  33 |             using (var conn = OpenConnection())
  34 |             using (var cmd = new SqlCommand(sql, conn))
  35 |             {
  36 |                 if (parameters != null && parameters.Length > 0)
  37 |                 cmd.Parameters.AddRange(parameters);
  38 |                 using (var adapter = new SqlDataAdapter(cmd))
  39 |                 {
  40 |                     var dt = new DataTable();
  41 |                     adapter.Fill(dt);
  42 |                     return dt;
  43 |                 }
  44 |             }
  45 |         }
```

---

### `ExecuteNonQuery` — lines 46–56

#### Signature

```csharp
public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
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
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |

#### Code

```csharp
  46 | 
  47 |         public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
  48 |         {
  49 |             using (var conn = OpenConnection())
  50 |             using (var cmd = new SqlCommand(sql, conn))
  51 |             {
  52 |                 if (parameters != null && parameters.Length > 0)
  53 |                 cmd.Parameters.AddRange(parameters);
  54 |                 return cmd.ExecuteNonQuery();
  55 |             }
  56 |         }
```

---

### `ExecuteScalar` — lines 57–67

#### Signature

```csharp
public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
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
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |

#### Code

```csharp
  57 | 
  58 |         public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
  59 |         {
  60 |             using (var conn = OpenConnection())
  61 |             using (var cmd = new SqlCommand(sql, conn))
  62 |             {
  63 |                 if (parameters != null && parameters.Length > 0)
  64 |                 cmd.Parameters.AddRange(parameters);
  65 |                 return cmd.ExecuteScalar();
  66 |             }
  67 |         }
```

---

### `ExecuteScalarInt` — lines 68–74

#### Signature

```csharp
public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
```

#### What it is

Runs SQL and returns a single integer value (COUNT or identity).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `result` | `var` | AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY). |

#### Code

```csharp
  68 | 
  69 |         public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
  70 |         {
  71 |             var result = ExecuteScalar(sql, parameters);
  72 |             if (result == null || result == DBNull.Value) return 0;
  73 |             return Convert.ToInt32(result);
  74 |         }
```

---

### `ExecuteScalarDecimal` — lines 75–81

#### Signature

```csharp
public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
```

#### What it is

Function `ExecuteScalarDecimal` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `parameters` | `SqlParameter[]` | Array of SQL parameters (@Name values) for a query. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `result` | `var` | AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY). |

#### Code

```csharp
  75 | 
  76 |         public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
  77 |         {
  78 |             var result = ExecuteScalar(sql, parameters);
  79 |             if (result == null || result == DBNull.Value) return 0m;
  80 |             return Convert.ToDecimal(result);
  81 |         }
```

---

### `P` — lines 82–86

#### Signature

```csharp
public static SqlParameter P(string name, object value)
```

#### What it is

Creates one SQL parameter (`@Name` + value) so user input is never concatenated into SQL.

#### How it works

1. Starts when something calls `P`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `name` | `string` | Display name of user/course/criterion. |
| `value` | `object` | Holds “value” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  82 | 
  83 |         public static SqlParameter P(string name, object value)
  84 |         {
  85 |             return new SqlParameter(name, value ?? DBNull.Value);
  86 |         }
```

---

### `SafeString` — lines 87–92

#### Signature

```csharp
public static string SafeString(object value)
```

#### What it is

Reads a database column as text safely (empty string if the value is NULL).

#### How it works

1. Starts when something calls `SafeString`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `value` | `object` | Holds “value” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  87 | 
  88 |         public static string SafeString(object value)
  89 |         {
  90 |             if (value == null || value == DBNull.Value) return string.Empty;
  91 |             return value.ToString();
  92 |         }
```

---

### `SafeInt` — lines 93–98

#### Signature

```csharp
public static int? SafeInt(object value)
```

#### What it is

Function `SafeInt` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `SafeInt`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `value` | `object` | Holds “value” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  93 | 
  94 |         public static int? SafeInt(object value)
  95 |         {
  96 |             if (value == null || value == DBNull.Value) return null;
  97 |             return Convert.ToInt32(value);
  98 |         }
```

---

### `SafeDecimal` — lines 99–104

#### Signature

```csharp
public static decimal? SafeDecimal(object value)
```

#### What it is

Function `SafeDecimal` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `SafeDecimal`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `value` | `object` | Holds “value” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  99 | 
 100 |         public static decimal? SafeDecimal(object value)
 101 |         {
 102 |             if (value == null || value == DBNull.Value) return null;
 103 |             return Convert.ToDecimal(value);
 104 |         }
```

---

### `SafeDate` — lines 105–110

#### Signature

```csharp
public static DateTime? SafeDate(object value)
```

#### What it is

Function `SafeDate` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `SafeDate`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `value` | `object` | Holds “value” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 105 | 
 106 |         public static DateTime? SafeDate(object value)
 107 |         {
 108 |             if (value == null || value == DBNull.Value) return null;
 109 |             return Convert.ToDateTime(value);
 110 |         }
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
   8 |     /// <summary>
   9 |     /// Centralized SQL helper bound to EduDB.mdf via Web.config MyDbConn.
  10 |     /// </summary>
  11 |     public static class DbHelper
  12 |     {
  13 |         public static string ConnectionString
  14 |         {
  15 |             get
  16 |             {
  17 |                 var cs = ConfigurationManager.ConnectionStrings["MyDbConn"];
  18 |                 if (cs == null || string.IsNullOrWhiteSpace(cs.ConnectionString))
  19 |                 throw new InvalidOperationException("Connection string 'MyDbConn' is missing from Web.config.");
  20 |                 return cs.ConnectionString;
  21 |             }
  22 |         }
  23 | 
  24 |         public static SqlConnection OpenConnection()
  25 |         {
  26 |             var conn = new SqlConnection(ConnectionString);
  27 |             conn.Open();
  28 |             return conn;
  29 |         }
  30 | 
  31 |         public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
  32 |         {
  33 |             using (var conn = OpenConnection())
  34 |             using (var cmd = new SqlCommand(sql, conn))
  35 |             {
  36 |                 if (parameters != null && parameters.Length > 0)
  37 |                 cmd.Parameters.AddRange(parameters);
  38 |                 using (var adapter = new SqlDataAdapter(cmd))
  39 |                 {
  40 |                     var dt = new DataTable();
  41 |                     adapter.Fill(dt);
  42 |                     return dt;
  43 |                 }
  44 |             }
  45 |         }
  46 | 
  47 |         public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
  48 |         {
  49 |             using (var conn = OpenConnection())
  50 |             using (var cmd = new SqlCommand(sql, conn))
  51 |             {
  52 |                 if (parameters != null && parameters.Length > 0)
  53 |                 cmd.Parameters.AddRange(parameters);
  54 |                 return cmd.ExecuteNonQuery();
  55 |             }
  56 |         }
  57 | 
  58 |         public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
  59 |         {
  60 |             using (var conn = OpenConnection())
  61 |             using (var cmd = new SqlCommand(sql, conn))
  62 |             {
  63 |                 if (parameters != null && parameters.Length > 0)
  64 |                 cmd.Parameters.AddRange(parameters);
  65 |                 return cmd.ExecuteScalar();
  66 |             }
  67 |         }
  68 | 
  69 |         public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
  70 |         {
  71 |             var result = ExecuteScalar(sql, parameters);
  72 |             if (result == null || result == DBNull.Value) return 0;
  73 |             return Convert.ToInt32(result);
  74 |         }
  75 | 
  76 |         public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
  77 |         {
  78 |             var result = ExecuteScalar(sql, parameters);
  79 |             if (result == null || result == DBNull.Value) return 0m;
  80 |             return Convert.ToDecimal(result);
  81 |         }
  82 | 
  83 |         public static SqlParameter P(string name, object value)
  84 |         {
  85 |             return new SqlParameter(name, value ?? DBNull.Value);
  86 |         }
  87 | 
  88 |         public static string SafeString(object value)
  89 |         {
  90 |             if (value == null || value == DBNull.Value) return string.Empty;
  91 |             return value.ToString();
  92 |         }
  93 | 
  94 |         public static int? SafeInt(object value)
  95 |         {
  96 |             if (value == null || value == DBNull.Value) return null;
  97 |             return Convert.ToInt32(value);
  98 |         }
  99 | 
 100 |         public static decimal? SafeDecimal(object value)
 101 |         {
 102 |             if (value == null || value == DBNull.Value) return null;
 103 |             return Convert.ToDecimal(value);
 104 |         }
 105 | 
 106 |         public static DateTime? SafeDate(object value)
 107 |         {
 108 |             if (value == null || value == DBNull.Value) return null;
 109 |             return Convert.ToDateTime(value);
 110 |         }
 111 |     }
 112 | }
```
