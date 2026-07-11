# CourseSchema.cs
**Source:** `Data/CourseSchema.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Ensures optional Courses columns exist at runtime (e.g. IsPublished BIT) and backfills defaults when safe.

## File overview

- **Total lines:** 69
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `Gate` | `object` | Holds “Gate” for this scope. |
| `_ready` | `bool` | Holds “ready” for this scope. (true/false) |

## Functions / methods (3 found)

### `Ensure` — lines 11–36

#### Signature

```csharp
public static void Ensure()
```

#### What it is

Makes sure **** exists or is valid before the rest of the code continues.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.
2. Update the course publish flag so Landing can show/hide it.
3. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `up` | `var` | Holds “up” for this scope.  Newly constructed object. |

#### Code

```csharp
  11 | 
  12 |         public static void Ensure()
  13 |         {
  14 |             if (_ready) return;
  15 |             lock (Gate)
  16 |             {
  17 |                 if (_ready) return;
  18 |                 try
  19 |                 {
  20 |                     using (var conn = DbHelper.OpenConnection())
  21 |                     {
  22 |                         EnsureColumn(conn, "Courses", "IsPublished", "BIT NULL");
  23 |                         // Default existing rows: treat as published if they already have content history
  24 |                         try
  25 |                         {
  26 |                             using (var up = new SqlCommand(
  27 |                                 "UPDATE Courses SET IsPublished = 1 WHERE IsPublished IS NULL", conn))
  28 |                                 up.ExecuteNonQuery();
  29 |                         }
  30 |                         catch { }
  31 |                     }
  32 |                 }
  33 |                 catch { }
  34 |                 _ready = true;
  35 |             }
  36 |         }
```

---

### `EnsureColumn` — lines 37–55

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

#### Code

```csharp
  37 | 
  38 |         private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
  39 |         {
  40 |             using (var check = new SqlCommand(@"
  41 | SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS
  42 | WHERE TABLE_NAME = @t AND COLUMN_NAME = @c", conn))
  43 |             {
  44 |                 check.Parameters.AddWithValue("@t", table);
  45 |                 check.Parameters.AddWithValue("@c", column);
  46 |                 if (check.ExecuteScalar() != null) return;
  47 |             }
  48 |             try
  49 |             {
  50 |                 using (var alter = new SqlCommand(
  51 |                     "ALTER TABLE [" + table + "] ADD [" + column + "] " + definition, conn))
  52 |                     alter.ExecuteNonQuery();
  53 |             }
  54 |             catch { }
  55 |         }
```

---

### `HasIsPublished` — lines 56–67

#### Signature

```csharp
public static bool HasIsPublished()
```

#### What it is

Checks a condition related to **Has Is Published** and returns true/false (or tries an action safely).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  56 | 
  57 |         public static bool HasIsPublished()
  58 |         {
  59 |             Ensure();
  60 |             try
  61 |             {
  62 |                 return DbHelper.ExecuteScalarInt(@"
  63 | SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
  64 | WHERE TABLE_NAME = 'Courses' AND COLUMN_NAME = 'IsPublished'") > 0;
  65 |             }
  66 |             catch { return false; }
  67 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Data.SqlClient;
   3 | 
   4 | namespace WebAppAssignment.Data
   5 | {
   6 |     /// <summary>Ensures optional Courses columns exist (e.g. IsPublished).</summary>
   7 |     public static class CourseSchema
   8 |     {
   9 |         private static readonly object Gate = new object();
  10 |         private static bool _ready;
  11 | 
  12 |         public static void Ensure()
  13 |         {
  14 |             if (_ready) return;
  15 |             lock (Gate)
  16 |             {
  17 |                 if (_ready) return;
  18 |                 try
  19 |                 {
  20 |                     using (var conn = DbHelper.OpenConnection())
  21 |                     {
  22 |                         EnsureColumn(conn, "Courses", "IsPublished", "BIT NULL");
  23 |                         // Default existing rows: treat as published if they already have content history
  24 |                         try
  25 |                         {
  26 |                             using (var up = new SqlCommand(
  27 |                                 "UPDATE Courses SET IsPublished = 1 WHERE IsPublished IS NULL", conn))
  28 |                                 up.ExecuteNonQuery();
  29 |                         }
  30 |                         catch { }
  31 |                     }
  32 |                 }
  33 |                 catch { }
  34 |                 _ready = true;
  35 |             }
  36 |         }
  37 | 
  38 |         private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
  39 |         {
  40 |             using (var check = new SqlCommand(@"
  41 | SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS
  42 | WHERE TABLE_NAME = @t AND COLUMN_NAME = @c", conn))
  43 |             {
  44 |                 check.Parameters.AddWithValue("@t", table);
  45 |                 check.Parameters.AddWithValue("@c", column);
  46 |                 if (check.ExecuteScalar() != null) return;
  47 |             }
  48 |             try
  49 |             {
  50 |                 using (var alter = new SqlCommand(
  51 |                     "ALTER TABLE [" + table + "] ADD [" + column + "] " + definition, conn))
  52 |                     alter.ExecuteNonQuery();
  53 |             }
  54 |             catch { }
  55 |         }
  56 | 
  57 |         public static bool HasIsPublished()
  58 |         {
  59 |             Ensure();
  60 |             try
  61 |             {
  62 |                 return DbHelper.ExecuteScalarInt(@"
  63 | SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
  64 | WHERE TABLE_NAME = 'Courses' AND COLUMN_NAME = 'IsPublished'") > 0;
  65 |             }
  66 |             catch { return false; }
  67 |         }
  68 |     }
  69 | }
```
