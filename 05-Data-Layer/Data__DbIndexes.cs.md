# DbIndexes.cs
**Source:** `Data/DbIndexes.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Creates useful nonclustered indexes if missing (LecturerUID, IsPublished, CWSubmissions.CWID, …) for LocalDB demos.

## File overview

- **Total lines:** 91
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `Gate` | `object` | Holds “Gate” for this scope. |
| `_done` | `bool` | Holds “done” for this scope. (true/false) |

## Functions / methods (2 found)

### `Ensure` — lines 14–57

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
  17 |             if (_done) return;
  18 |             lock (Gate)
  19 |             {
  20 |                 if (_done) return;
  21 |                 try
  22 |                 {
  23 |                     using (var conn = DbHelper.OpenConnection())
  24 |                     {
  25 |                         // Courses by lecturer (course manager, ownership)
  26 |                         EnsureIndex(conn, "IX_Courses_LecturerUID",
  27 |                             "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID) INCLUDE (Name, IsPublished)");
  28 | 
  29 |                         // Fallback without IsPublished if include failed
  30 |                         EnsureIndex(conn, "IX_Courses_LecturerUID",
  31 |                             "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID)");
  32 | 
  33 |                         // Published catalogue
  34 |                         EnsureIndex(conn, "IX_Courses_IsPublished",
  35 |                             "CREATE NONCLUSTERED INDEX IX_Courses_IsPublished ON Courses (IsPublished) INCLUDE (Name, Rating, Categories, Level)");
  36 | 
  37 |                         // Submissions by coursework (grading queue)
  38 |                         EnsureIndex(conn, "IX_CWSubmissions_CWID",
  39 |                             "CREATE NONCLUSTERED INDEX IX_CWSubmissions_CWID ON CWSubmissions (CWID) INCLUDE (StudentUID, SubmissionDate)");
  40 | 
  41 |                         // Markings by submission (pending grade NOT EXISTS)
  42 |                         EnsureIndex(conn, "IX_CWMarkings_SID",
  43 |                             "CREATE NONCLUSTERED INDEX IX_CWMarkings_SID ON CWMarkings (SID)");
  44 | 
  45 |                         // Chapters by course (curriculum)
  46 |                         EnsureIndex(conn, "IX_Chapters_CID",
  47 |                             "CREATE NONCLUSTERED INDEX IX_Chapters_CID ON Chapters (CID)");
  48 | 
  49 |                         // Enrollments by course
  50 |                         EnsureIndex(conn, "IX_Enrollments_CID",
  51 |                             "CREATE NONCLUSTERED INDEX IX_Enrollments_CID ON Enrollments (CID) INCLUDE (StudentUID, Progress)");
  52 |                     }
  53 |                 }
  54 |                 catch { }
  55 |                 _done = true;
  56 |             }
  57 |         }
```

---

### `EnsureIndex` — lines 58–89

#### Signature

```csharp
private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)
```

#### What it is

Makes sure **Index** exists or is valid before the rest of the code continues.

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Run SQL that returns one value (count, id, flag).
3. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `indexName` | `string` | Holds “index Name” for this scope. (text) |
| `createSql` | `string` | Holds “create Sql” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `check` | `var` | Holds “check” for this scope.  Newly constructed object. |
| `on` | `int` | Holds “on” for this scope. (integer) |
| `rest` | `string` | Holds “rest” for this scope. (text) |
| `sp` | `int` | Holds “sp” for this scope. (integer) |
| `create` | `var` | Holds “create” for this scope.  Assigned from rows-affected of INSERT/UPDATE/DELETE. |

#### Code

```csharp
  58 | 
  59 |         private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)
  60 |         {
  61 |             try
  62 |             {
  63 |                 using (var check = new SqlCommand(
  64 |                     "SELECT 1 FROM sys.indexes WHERE name = @n AND object_id = OBJECT_ID(@t)", conn))
  65 |                 {
  66 |                     // Infer table from CREATE ... ON TableName
  67 |                     string table = null;
  68 |                     int on = createSql.IndexOf(" ON ", StringComparison.OrdinalIgnoreCase);
  69 |                     if (on > 0)
  70 |                     {
  71 |                         string rest = createSql.Substring(on + 4).Trim();
  72 |                         int sp = rest.IndexOfAny(new[] { ' ', '(' });
  73 |                         table = sp > 0 ? rest.Substring(0, sp).Trim() : rest;
  74 |                     }
  75 |                     if (string.IsNullOrEmpty(table)) return;
  76 | 
  77 |                     check.Parameters.AddWithValue("@n", indexName);
  78 |                     check.Parameters.AddWithValue("@t", "dbo." + table);
  79 |                     if (check.ExecuteScalar() != null) return;
  80 |                 }
  81 | 
  82 |                 using (var create = new SqlCommand(createSql, conn))
  83 |                     create.ExecuteNonQuery();
  84 |             }
  85 |             catch
  86 |             {
  87 |                 // Column/table missing or include list invalid — ignore
  88 |             }
  89 |         }
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
   6 |     /// <summary>
   7 |     /// Best-effort nonclustered indexes for common lecturer/landing queries.
   8 |     /// Safe to run repeatedly (checks sys.indexes first).
   9 |     /// </summary>
  10 |     public static class DbIndexes
  11 |     {
  12 |         private static readonly object Gate = new object();
  13 |         private static bool _done;
  14 | 
  15 |         public static void Ensure()
  16 |         {
  17 |             if (_done) return;
  18 |             lock (Gate)
  19 |             {
  20 |                 if (_done) return;
  21 |                 try
  22 |                 {
  23 |                     using (var conn = DbHelper.OpenConnection())
  24 |                     {
  25 |                         // Courses by lecturer (course manager, ownership)
  26 |                         EnsureIndex(conn, "IX_Courses_LecturerUID",
  27 |                             "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID) INCLUDE (Name, IsPublished)");
  28 | 
  29 |                         // Fallback without IsPublished if include failed
  30 |                         EnsureIndex(conn, "IX_Courses_LecturerUID",
  31 |                             "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID)");
  32 | 
  33 |                         // Published catalogue
  34 |                         EnsureIndex(conn, "IX_Courses_IsPublished",
  35 |                             "CREATE NONCLUSTERED INDEX IX_Courses_IsPublished ON Courses (IsPublished) INCLUDE (Name, Rating, Categories, Level)");
  36 | 
  37 |                         // Submissions by coursework (grading queue)
  38 |                         EnsureIndex(conn, "IX_CWSubmissions_CWID",
  39 |                             "CREATE NONCLUSTERED INDEX IX_CWSubmissions_CWID ON CWSubmissions (CWID) INCLUDE (StudentUID, SubmissionDate)");
  40 | 
  41 |                         // Markings by submission (pending grade NOT EXISTS)
  42 |                         EnsureIndex(conn, "IX_CWMarkings_SID",
  43 |                             "CREATE NONCLUSTERED INDEX IX_CWMarkings_SID ON CWMarkings (SID)");
  44 | 
  45 |                         // Chapters by course (curriculum)
  46 |                         EnsureIndex(conn, "IX_Chapters_CID",
  47 |                             "CREATE NONCLUSTERED INDEX IX_Chapters_CID ON Chapters (CID)");
  48 | 
  49 |                         // Enrollments by course
  50 |                         EnsureIndex(conn, "IX_Enrollments_CID",
  51 |                             "CREATE NONCLUSTERED INDEX IX_Enrollments_CID ON Enrollments (CID) INCLUDE (StudentUID, Progress)");
  52 |                     }
  53 |                 }
  54 |                 catch { }
  55 |                 _done = true;
  56 |             }
  57 |         }
  58 | 
  59 |         private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)
  60 |         {
  61 |             try
  62 |             {
  63 |                 using (var check = new SqlCommand(
  64 |                     "SELECT 1 FROM sys.indexes WHERE name = @n AND object_id = OBJECT_ID(@t)", conn))
  65 |                 {
  66 |                     // Infer table from CREATE ... ON TableName
  67 |                     string table = null;
  68 |                     int on = createSql.IndexOf(" ON ", StringComparison.OrdinalIgnoreCase);
  69 |                     if (on > 0)
  70 |                     {
  71 |                         string rest = createSql.Substring(on + 4).Trim();
  72 |                         int sp = rest.IndexOfAny(new[] { ' ', '(' });
  73 |                         table = sp > 0 ? rest.Substring(0, sp).Trim() : rest;
  74 |                     }
  75 |                     if (string.IsNullOrEmpty(table)) return;
  76 | 
  77 |                     check.Parameters.AddWithValue("@n", indexName);
  78 |                     check.Parameters.AddWithValue("@t", "dbo." + table);
  79 |                     if (check.ExecuteScalar() != null) return;
  80 |                 }
  81 | 
  82 |                 using (var create = new SqlCommand(createSql, conn))
  83 |                     create.ExecuteNonQuery();
  84 |             }
  85 |             catch
  86 |             {
  87 |                 // Column/table missing or include list invalid — ignore
  88 |             }
  89 |         }
  90 |     }
  91 | }
```
