# DbIndexes.cs
**Source:** `Data/DbIndexes.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Creates useful nonclustered indexes if missing (LecturerUID, IsPublished, CWSubmissions.CWID, …) for LocalDB demos.

## File overview

- **Total lines:** 91
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 12:** `Gate` (`object`) — **Holds “Gate” for this scope.**
- **Line 13:** `_done` (`bool`) — **Holds “done” for this scope. (true/false)**
- **Line 67:** `table` (`string`) — **DataTable or HTML table container.**
- **Line 68:** `on` (`int`) — **Holds “on” for this scope. (integer)**
- **Line 71:** `rest` (`string`) — **Holds “rest” for this scope. (text)**
- **Line 72:** `sp` (`int`) — **Holds “sp” for this scope. (integer)**

## Functions / methods (2 found)

### `Ensure` — lines 14–57

```csharp
public static void Ensure()
```

#### Explanation

- **Purpose:** Implements `Ensure`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L21:** Error handling block.
- **L23:** Import namespace/types.
- **L26:** Idempotent schema/index ensure (safe to run many times).
- **L27:** Course publish flag for Landing catalog.
- **L30:** Idempotent schema/index ensure (safe to run many times).
- **L31:** Owner lecturer foreign key.
- **L34:** Idempotent schema/index ensure (safe to run many times).
- **L35:** Course publish flag for Landing catalog.
- **L38:** Idempotent schema/index ensure (safe to run many times).
- **L42:** Idempotent schema/index ensure (safe to run many times).
- **L46:** Idempotent schema/index ensure (safe to run many times).
- **L50:** Idempotent schema/index ensure (safe to run many times).
- **L54:** Handle/log exception.

---

### `EnsureIndex` — lines 58–89

```csharp
private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)
```

#### Explanation

- **Purpose:** Implements `EnsureIndex`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `indexName` (`string`) — Holds “index Name” for this scope. (text)
- `createSql` (`string`) — Holds “create Sql” for this scope. (text)
- **Local variables (what each means):**
- `check` (`var`) — Holds “check” for this scope.  Newly constructed object.
- `on` (`int`) — Holds “on” for this scope. (integer)
- `rest` (`string`) — Holds “rest” for this scope. (text)
- `sp` (`int`) — Holds “sp” for this scope. (integer)
- `create` (`var`) — Holds “create” for this scope.  Assigned from rows-affected of INSERT/UPDATE/DELETE.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L59:** Database access (pure SQL).
- **L61:** Error handling block.
- **L63:** Import namespace/types.
- **L64:** Inspect live database catalog for existing columns/tables.
<<<<<<< HEAD
=======
- **L67:** `table` means: DataTable or HTML table container.
- **L68:** `on` means: Holds “on” for this scope. (integer)
- **L71:** `rest` means: Holds “rest” for this scope. (text)
- **L72:** `sp` means: Holds “sp” for this scope. (integer)
>>>>>>> eb8ce01 (update)
- **L77:** Parameterized SQL — prevents classic SQL injection.
- **L78:** Parameterized SQL — prevents classic SQL injection.
- **L79:** Run SQL; return table / rows / scalar.
- **L82:** Import namespace/types.
- **L83:** Run SQL; return table / rows / scalar.
- **L85:** Handle/log exception.

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L4:** C# namespace grouping.
- **L21:** Error handling block.
- **L23:** Import namespace/types.
- **L26:** Idempotent schema/index ensure (safe to run many times).
- **L27:** Course publish flag for Landing catalog.
- **L30:** Idempotent schema/index ensure (safe to run many times).
- **L31:** Owner lecturer foreign key.
- **L34:** Idempotent schema/index ensure (safe to run many times).
- **L35:** Course publish flag for Landing catalog.
- **L38:** Idempotent schema/index ensure (safe to run many times).
- **L42:** Idempotent schema/index ensure (safe to run many times).
- **L46:** Idempotent schema/index ensure (safe to run many times).
- **L50:** Idempotent schema/index ensure (safe to run many times).
- **L54:** Handle/log exception.
- **L59:** Database access (pure SQL).
- **L61:** Error handling block.
- **L63:** Import namespace/types.
- **L64:** Inspect live database catalog for existing columns/tables.
<<<<<<< HEAD
=======
- **L67:** `table` means: DataTable or HTML table container.
- **L68:** `on` means: Holds “on” for this scope. (integer)
- **L71:** `rest` means: Holds “rest” for this scope. (text)
- **L72:** `sp` means: Holds “sp” for this scope. (integer)
>>>>>>> eb8ce01 (update)
- **L77:** Parameterized SQL — prevents classic SQL injection.
- **L78:** Parameterized SQL — prevents classic SQL injection.
- **L79:** Run SQL; return table / rows / scalar.
- **L82:** Import namespace/types.
- **L83:** Run SQL; return table / rows / scalar.
- **L85:** Handle/log exception.

## Source snapshot (raw)

```csharp
using System;
using System.Data.SqlClient;

namespace WebAppAssignment.Data
{
    /// <summary>
    /// Best-effort nonclustered indexes for common lecturer/landing queries.
    /// Safe to run repeatedly (checks sys.indexes first).
    /// </summary>
    public static class DbIndexes
    {
        private static readonly object Gate = new object();
        private static bool _done;

        public static void Ensure()
        {
            if (_done) return;
            lock (Gate)
            {
                if (_done) return;
                try
                {
                    using (var conn = DbHelper.OpenConnection())
                    {
                        // Courses by lecturer (course manager, ownership)
                        EnsureIndex(conn, "IX_Courses_LecturerUID",
                            "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID) INCLUDE (Name, IsPublished)");

                        // Fallback without IsPublished if include failed
                        EnsureIndex(conn, "IX_Courses_LecturerUID",
                            "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID)");

                        // Published catalogue
                        EnsureIndex(conn, "IX_Courses_IsPublished",
                            "CREATE NONCLUSTERED INDEX IX_Courses_IsPublished ON Courses (IsPublished) INCLUDE (Name, Rating, Categories, Level)");

                        // Submissions by coursework (grading queue)
                        EnsureIndex(conn, "IX_CWSubmissions_CWID",
                            "CREATE NONCLUSTERED INDEX IX_CWSubmissions_CWID ON CWSubmissions (CWID) INCLUDE (StudentUID, SubmissionDate)");

                        // Markings by submission (pending grade NOT EXISTS)
                        EnsureIndex(conn, "IX_CWMarkings_SID",
                            "CREATE NONCLUSTERED INDEX IX_CWMarkings_SID ON CWMarkings (SID)");

                        // Chapters by course (curriculum)
                        EnsureIndex(conn, "IX_Chapters_CID",
                            "CREATE NONCLUSTERED INDEX IX_Chapters_CID ON Chapters (CID)");

                        // Enrollments by course
                        EnsureIndex(conn, "IX_Enrollments_CID",
                            "CREATE NONCLUSTERED INDEX IX_Enrollments_CID ON Enrollments (CID) INCLUDE (StudentUID, Progress)");
                    }
                }
                catch { }
                _done = true;
            }
        }

        private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)
        {
            try
            {
                using (var check = new SqlCommand(
                    "SELECT 1 FROM sys.indexes WHERE name = @n AND object_id = OBJECT_ID(@t)", conn))
                {
                    // Infer table from CREATE ... ON TableName
                    string table = null;
                    int on = createSql.IndexOf(" ON ", StringComparison.OrdinalIgnoreCase);
                    if (on > 0)
                    {
                        string rest = createSql.Substring(on + 4).Trim();
                        int sp = rest.IndexOfAny(new[] { ' ', '(' });
                        table = sp > 0 ? rest.Substring(0, sp).Trim() : rest;
                    }
                    if (string.IsNullOrEmpty(table)) return;

                    check.Parameters.AddWithValue("@n", indexName);
                    check.Parameters.AddWithValue("@t", "dbo." + table);
                    if (check.ExecuteScalar() != null) return;
                }

                using (var create = new SqlCommand(createSql, conn))
                    create.ExecuteNonQuery();
            }
            catch
            {
                // Column/table missing or include list invalid — ignore
            }
        }
    }
}

```
