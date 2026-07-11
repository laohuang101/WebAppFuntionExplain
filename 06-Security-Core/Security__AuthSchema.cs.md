# AuthSchema.cs
**Source:** `Data/Security/AuthSchema.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Ensures Users security columns exist (PasswordHash, MfaSecret, MfaEnabled, JWT-related helpers).

## File overview

- **Total lines:** 109
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `Gate` | `object` | Holds “Gate” for this scope. |
| `_ready` | `bool` | Holds “ready” for this scope. (true/false) |

## Functions / methods (4 found)

### `Ensure` — lines 14–43

#### Signature

```csharp
public static void Ensure()
```

#### What it is

Makes sure **** exists or is valid before the rest of the code continues.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |

#### Code

```csharp
  14 | 
  15 |         public static void Ensure()
  16 |         {
  17 |             if (_ready) return;
  18 |             lock (Gate)
  19 |             {
  20 |                 if (_ready) return;
  21 |                 try
  22 |                 {
  23 |                     using (var conn = DbHelper.OpenConnection())
  24 |                     {
  25 |                         EnsureColumn(conn, "Users", "PasswordHash", "NVARCHAR(200) NULL");
  26 |                         EnsureColumn(conn, "Users", "MfaSecret", "NVARCHAR(64) NULL");
  27 |                         EnsureColumn(conn, "Users", "MfaEnabled", "BIT NOT NULL CONSTRAINT DF_Users_MfaEnabled DEFAULT(0)");
  28 |                         EnsureColumn(conn, "Users", "EmailOtp", "NVARCHAR(12) NULL");
  29 |                         EnsureColumn(conn, "Users", "EmailOtpExpiry", "DATETIME NULL");
  30 |                         EnsureColumn(conn, "Users", "CreatedAt", "DATETIME NULL");
  31 |                         EnsureColumn(conn, "Users", "PasswordResetToken", "NVARCHAR(128) NULL");
  32 |                         EnsureColumn(conn, "Users", "PasswordResetExpiry", "DATETIME NULL");
  33 |                         EnsureAuditTable(conn);
  34 |                     }
  35 |                     _ready = true;
  36 |                 }
  37 |                 catch
  38 |                 {
  39 |                     // Table might use different name; don't crash app start
  40 |                     _ready = true;
  41 |                 }
  42 |             }
  43 |         }
```

---

### `EnsureAuditTable` — lines 44–71

#### Signature

```csharp
private static void EnsureAuditTable(SqlConnection conn)
```

#### What it is

Makes sure **Audit Table** exists or is valid before the rest of the code continues.

#### How it works

1. Run SQL that returns one value (count, id, flag).
2. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `check` | `var` | Holds “check” for this scope.  Newly constructed object. |
| `create` | `var` | Holds “create” for this scope.  Newly constructed object. |

#### Code

```csharp
  44 | 
  45 |         private static void EnsureAuditTable(SqlConnection conn)
  46 |         {
  47 |             try
  48 |             {
  49 |                 using (var check = new SqlCommand(@"
  50 | SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'AuditLog'", conn))
  51 |                 {
  52 |                     if (check.ExecuteScalar() != null) return;
  53 |                 }
  54 | 
  55 |                 using (var create = new SqlCommand(@"
  56 | CREATE TABLE AuditLog (
  57 |     LogId INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  58 |     OccurredAt DATETIME NOT NULL,
  59 |     Action NVARCHAR(80) NOT NULL,
  60 |     UserId INT NULL,
  61 |     Email NVARCHAR(120) NULL,
  62 |     Detail NVARCHAR(500) NULL,
  63 |     IpAddress NVARCHAR(64) NULL,
  64 |     Path NVARCHAR(260) NULL
  65 | )", conn))
  66 |                 {
  67 |                     create.ExecuteNonQuery();
  68 |                 }
  69 |             }
  70 |             catch { }
  71 |         }
```

---

### `NVARCHAR` — lines 59–68

#### Signature

```csharp
Action NVARCHAR(80) NOT NULL,
    UserId INT NULL,
    Email NVARCHAR(120) NULL,
    Detail NVARCHAR(500) NULL,
    IpAddress NVARCHAR(64) NULL,
    Path NVARCHAR(260) NULL
)", conn))
```

#### What it is

Function `NVARCHAR` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `NULL` | `80) NOT` | Holds “NULL” for this scope. (type `80) NOT`) |
| `NULL` | `UserId INT` | Holds “NULL” for this scope. (type `UserId INT`) |
| `NULL` | `Email NVARCHAR(120)` | Holds “NULL” for this scope. (type `Email NVARCHAR(120)`) |
| `NULL` | `Detail NVARCHAR(500)` | Holds “NULL” for this scope. (type `Detail NVARCHAR(500)`) |
| `NULL` | `IpAddress NVARCHAR(64)` | Holds “NULL” for this scope. (type `IpAddress NVARCHAR(64)`) |
| `)"` | `Path NVARCHAR(260) NULL` | Holds “)"” for this scope. (type `Path NVARCHAR(260) NULL`) |
| `conn)` | `—` | Holds “conn)” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  59 |     Action NVARCHAR(80) NOT NULL,
  60 |     UserId INT NULL,
  61 |     Email NVARCHAR(120) NULL,
  62 |     Detail NVARCHAR(500) NULL,
  63 |     IpAddress NVARCHAR(64) NULL,
  64 |     Path NVARCHAR(260) NULL
  65 | )", conn))
  66 |                 {
  67 |                     create.ExecuteNonQuery();
  68 |                 }
```

---

### `EnsureColumn` — lines 72–107

#### Signature

```csharp
private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
```

#### What it is

Makes sure **Column** exists or is valid before the rest of the code continues.

#### How it works

1. Run SQL that returns one value (count, id, flag).
2. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `table` | `string` | DataTable or HTML table container. |
| `column` | `string` | Holds “column” for this scope. (text) |
| `definition` | `string` | Holds “definition” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `check` | `var` | Holds “check” for this scope.  Newly constructed object. |
| `alter` | `var` | Holds “alter” for this scope.  Newly constructed object. |
| `simple` | `string` | Holds “simple” for this scope. (text) |

#### Code

```csharp
  72 | 
  73 |         private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
  74 |         {
  75 |             using (var check = new SqlCommand(@"
  76 |             SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS
  77 |             WHERE TABLE_NAME = @t AND COLUMN_NAME = @c", conn))
  78 |             {
  79 |                 check.Parameters.AddWithValue("@t", table);
  80 |                 check.Parameters.AddWithValue("@c", column);
  81 |                 if (check.ExecuteScalar() != null) return;
  82 |             }
  83 | 
  84 |             try
  85 |             {
  86 |                 using (var alter = new SqlCommand(
  87 |                 "ALTER TABLE [" + table + "] ADD [" + column + "] " + definition, conn))
  88 |                 {
  89 |                     alter.ExecuteNonQuery();
  90 |                 }
  91 |             }
  92 |             catch
  93 |             {
  94 |                 string simple = definition
  95 |                 .Replace(" CONSTRAINT DF_Users_MfaEnabled DEFAULT(0)", " NULL")
  96 |                 .Replace("NOT NULL", "NULL");
  97 |                 try
  98 |                 {
  99 |                     using (var alter = new SqlCommand(
 100 |                     "ALTER TABLE [" + table + "] ADD [" + column + "] " + simple, conn))
 101 |                     {
 102 |                         alter.ExecuteNonQuery();
 103 |                     }
 104 |                 }
 105 |                 catch { /* column may already exist under race */ }
 106 |             }
 107 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Data.SqlClient;
   3 | using WebAppAssignment.Data;
   4 | 
   5 | namespace WebAppAssignment.Data.Security
   6 | {
   7 |     /// <summary>
   8 |     /// Ensures auth-related columns / audit tables exist (pure SQL ALTER - no EF).
   9 |     /// </summary>
  10 |     public static class AuthSchema
  11 |     {
  12 |         private static readonly object Gate = new object();
  13 |         private static bool _ready;
  14 | 
  15 |         public static void Ensure()
  16 |         {
  17 |             if (_ready) return;
  18 |             lock (Gate)
  19 |             {
  20 |                 if (_ready) return;
  21 |                 try
  22 |                 {
  23 |                     using (var conn = DbHelper.OpenConnection())
  24 |                     {
  25 |                         EnsureColumn(conn, "Users", "PasswordHash", "NVARCHAR(200) NULL");
  26 |                         EnsureColumn(conn, "Users", "MfaSecret", "NVARCHAR(64) NULL");
  27 |                         EnsureColumn(conn, "Users", "MfaEnabled", "BIT NOT NULL CONSTRAINT DF_Users_MfaEnabled DEFAULT(0)");
  28 |                         EnsureColumn(conn, "Users", "EmailOtp", "NVARCHAR(12) NULL");
  29 |                         EnsureColumn(conn, "Users", "EmailOtpExpiry", "DATETIME NULL");
  30 |                         EnsureColumn(conn, "Users", "CreatedAt", "DATETIME NULL");
  31 |                         EnsureColumn(conn, "Users", "PasswordResetToken", "NVARCHAR(128) NULL");
  32 |                         EnsureColumn(conn, "Users", "PasswordResetExpiry", "DATETIME NULL");
  33 |                         EnsureAuditTable(conn);
  34 |                     }
  35 |                     _ready = true;
  36 |                 }
  37 |                 catch
  38 |                 {
  39 |                     // Table might use different name; don't crash app start
  40 |                     _ready = true;
  41 |                 }
  42 |             }
  43 |         }
  44 | 
  45 |         private static void EnsureAuditTable(SqlConnection conn)
  46 |         {
  47 |             try
  48 |             {
  49 |                 using (var check = new SqlCommand(@"
  50 | SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'AuditLog'", conn))
  51 |                 {
  52 |                     if (check.ExecuteScalar() != null) return;
  53 |                 }
  54 | 
  55 |                 using (var create = new SqlCommand(@"
  56 | CREATE TABLE AuditLog (
  57 |     LogId INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  58 |     OccurredAt DATETIME NOT NULL,
  59 |     Action NVARCHAR(80) NOT NULL,
  60 |     UserId INT NULL,
  61 |     Email NVARCHAR(120) NULL,
  62 |     Detail NVARCHAR(500) NULL,
  63 |     IpAddress NVARCHAR(64) NULL,
  64 |     Path NVARCHAR(260) NULL
  65 | )", conn))
  66 |                 {
  67 |                     create.ExecuteNonQuery();
  68 |                 }
  69 |             }
  70 |             catch { }
  71 |         }
  72 | 
  73 |         private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
  74 |         {
  75 |             using (var check = new SqlCommand(@"
  76 |             SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS
  77 |             WHERE TABLE_NAME = @t AND COLUMN_NAME = @c", conn))
  78 |             {
  79 |                 check.Parameters.AddWithValue("@t", table);
  80 |                 check.Parameters.AddWithValue("@c", column);
  81 |                 if (check.ExecuteScalar() != null) return;
  82 |             }
  83 | 
  84 |             try
  85 |             {
  86 |                 using (var alter = new SqlCommand(
  87 |                 "ALTER TABLE [" + table + "] ADD [" + column + "] " + definition, conn))
  88 |                 {
  89 |                     alter.ExecuteNonQuery();
  90 |                 }
  91 |             }
  92 |             catch
  93 |             {
  94 |                 string simple = definition
  95 |                 .Replace(" CONSTRAINT DF_Users_MfaEnabled DEFAULT(0)", " NULL")
  96 |                 .Replace("NOT NULL", "NULL");
  97 |                 try
  98 |                 {
  99 |                     using (var alter = new SqlCommand(
 100 |                     "ALTER TABLE [" + table + "] ADD [" + column + "] " + simple, conn))
 101 |                     {
 102 |                         alter.ExecuteNonQuery();
 103 |                     }
 104 |                 }
 105 |                 catch { /* column may already exist under race */ }
 106 |             }
 107 |         }
 108 |     }
 109 | }
```
