# DbIndexes.cs
**Source:** `Data/DbIndexes.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 91
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 12:** `Gate` — type `object`
- **Line 13:** `_done` — type `bool`
- **Line 67:** `table` — type `string`
- **Line 68:** `on` — type `int`
- **Line 71:** `rest` — type `string`
- **Line 72:** `sp` — type `int`

## Functions / methods (2 found)

### `Ensure` — lines 14–57

```
public static void Ensure()
```

#### Explanation

- **Purpose:** Implements `Ensure`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Local variables:** `conn`

#### Line-by-line (this function)

`  14`  ``
`  15`  `        public static void Ensure()`
`  16`  `        {`
`  17`  `            if (_done) return;`
`  18`  `            lock (Gate)`
`  19`  `            {`
`  20`  `                if (_done) return;`
`  21`  `                try`
  - → Error handling block.
`  22`  `                {`
`  23`  `                    using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  24`  `                    {`
`  25`  `                        // Courses by lecturer (course manager, ownership)`
`  26`  `                        EnsureIndex(conn, "IX_Courses_LecturerUID",`
  - → Owner lecturer foreign key.
`  27`  `                            "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID) INCLUDE (Name, IsPublished)");`
  - → Course publish flag for Landing catalog.
`  28`  ``
`  29`  `                        // Fallback without IsPublished if include failed`
`  30`  `                        EnsureIndex(conn, "IX_Courses_LecturerUID",`
  - → Owner lecturer foreign key.
`  31`  `                            "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID)");`
  - → Owner lecturer foreign key.
`  32`  ``
`  33`  `                        // Published catalogue`
`  34`  `                        EnsureIndex(conn, "IX_Courses_IsPublished",`
  - → Course publish flag for Landing catalog.
`  35`  `                            "CREATE NONCLUSTERED INDEX IX_Courses_IsPublished ON Courses (IsPublished) INCLUDE (Name, Rating, Categories, Level)");`
  - → Course publish flag for Landing catalog.
`  36`  ``
`  37`  `                        // Submissions by coursework (grading queue)`
`  38`  `                        EnsureIndex(conn, "IX_CWSubmissions_CWID",`
`  39`  `                            "CREATE NONCLUSTERED INDEX IX_CWSubmissions_CWID ON CWSubmissions (CWID) INCLUDE (StudentUID, SubmissionDate)");`
`  40`  ``
`  41`  `                        // Markings by submission (pending grade NOT EXISTS)`
`  42`  `                        EnsureIndex(conn, "IX_CWMarkings_SID",`
`  43`  `                            "CREATE NONCLUSTERED INDEX IX_CWMarkings_SID ON CWMarkings (SID)");`
`  44`  ``
`  45`  `                        // Chapters by course (curriculum)`
`  46`  `                        EnsureIndex(conn, "IX_Chapters_CID",`
`  47`  `                            "CREATE NONCLUSTERED INDEX IX_Chapters_CID ON Chapters (CID)");`
`  48`  ``
`  49`  `                        // Enrollments by course`
`  50`  `                        EnsureIndex(conn, "IX_Enrollments_CID",`
`  51`  `                            "CREATE NONCLUSTERED INDEX IX_Enrollments_CID ON Enrollments (CID) INCLUDE (StudentUID, Progress)");`
`  52`  `                    }`
`  53`  `                }`
`  54`  `                catch { }`
  - → Handle/log exception.
`  55`  `                _done = true;`
`  56`  `            }`
`  57`  `        }`

---

### `EnsureIndex` — lines 58–89

```
private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)
```

#### Explanation

- **Purpose:** Implements `EnsureIndex`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string indexName, string createSql`
- **Local variables:** `check`, `table`, `on`, `rest`, `sp`, `create`

#### Line-by-line (this function)

`  58`  ``
`  59`  `        private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)`
  - → Database access (pure SQL).
`  60`  `        {`
`  61`  `            try`
  - → Error handling block.
`  62`  `            {`
`  63`  `                using (var check = new SqlCommand(`
  - → Import namespace/types.
`  64`  `                    "SELECT 1 FROM sys.indexes WHERE name = @n AND object_id = OBJECT_ID(@t)", conn))`
`  65`  `                {`
`  66`  `                    // Infer table from CREATE ... ON TableName`
`  67`  `                    string table = null;`
`  68`  `                    int on = createSql.IndexOf(" ON ", StringComparison.OrdinalIgnoreCase);`
`  69`  `                    if (on > 0)`
`  70`  `                    {`
`  71`  `                        string rest = createSql.Substring(on + 4).Trim();`
`  72`  `                        int sp = rest.IndexOfAny(new[] { ' ', '(' });`
`  73`  `                        table = sp > 0 ? rest.Substring(0, sp).Trim() : rest;`
`  74`  `                    }`
`  75`  `                    if (string.IsNullOrEmpty(table)) return;`
`  76`  ``
`  77`  `                    check.Parameters.AddWithValue("@n", indexName);`
`  78`  `                    check.Parameters.AddWithValue("@t", "dbo." + table);`
`  79`  `                    if (check.ExecuteScalar() != null) return;`
  - → Run SQL; return table / rows / scalar.
`  80`  `                }`
`  81`  ``
`  82`  `                using (var create = new SqlCommand(createSql, conn))`
  - → Import namespace/types.
`  83`  `                    create.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  84`  `            }`
`  85`  `            catch`
  - → Handle/log exception.
`  86`  `            {`
`  87`  `                // Column/table missing or include list invalid — ignore`
`  88`  `            }`
`  89`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Data.SqlClient;`
  - → Import namespace/types.
`   3`  ``
`   4`  `namespace WebAppAssignment.Data`
  - → C# namespace grouping.
`   5`  `{`
`   6`  `    /// <summary>`
`   7`  `    /// Best-effort nonclustered indexes for common lecturer/landing queries.`
`   8`  `    /// Safe to run repeatedly (checks sys.indexes first).`
`   9`  `    /// </summary>`
`  10`  `    public static class DbIndexes`
`  11`  `    {`
`  12`  `        private static readonly object Gate = new object();`
`  13`  `        private static bool _done;`
`  14`  ``
`  15`  `        public static void Ensure()`
`  16`  `        {`
`  17`  `            if (_done) return;`
`  18`  `            lock (Gate)`
`  19`  `            {`
`  20`  `                if (_done) return;`
`  21`  `                try`
  - → Error handling block.
`  22`  `                {`
`  23`  `                    using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  24`  `                    {`
`  25`  `                        // Courses by lecturer (course manager, ownership)`
`  26`  `                        EnsureIndex(conn, "IX_Courses_LecturerUID",`
  - → Owner lecturer foreign key.
`  27`  `                            "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID) INCLUDE (Name, IsPublished)");`
  - → Course publish flag for Landing catalog.
`  28`  ``
`  29`  `                        // Fallback without IsPublished if include failed`
`  30`  `                        EnsureIndex(conn, "IX_Courses_LecturerUID",`
  - → Owner lecturer foreign key.
`  31`  `                            "CREATE NONCLUSTERED INDEX IX_Courses_LecturerUID ON Courses (LecturerUID)");`
  - → Owner lecturer foreign key.
`  32`  ``
`  33`  `                        // Published catalogue`
`  34`  `                        EnsureIndex(conn, "IX_Courses_IsPublished",`
  - → Course publish flag for Landing catalog.
`  35`  `                            "CREATE NONCLUSTERED INDEX IX_Courses_IsPublished ON Courses (IsPublished) INCLUDE (Name, Rating, Categories, Level)");`
  - → Course publish flag for Landing catalog.
`  36`  ``
`  37`  `                        // Submissions by coursework (grading queue)`
`  38`  `                        EnsureIndex(conn, "IX_CWSubmissions_CWID",`
`  39`  `                            "CREATE NONCLUSTERED INDEX IX_CWSubmissions_CWID ON CWSubmissions (CWID) INCLUDE (StudentUID, SubmissionDate)");`
`  40`  ``
`  41`  `                        // Markings by submission (pending grade NOT EXISTS)`
`  42`  `                        EnsureIndex(conn, "IX_CWMarkings_SID",`
`  43`  `                            "CREATE NONCLUSTERED INDEX IX_CWMarkings_SID ON CWMarkings (SID)");`
`  44`  ``
`  45`  `                        // Chapters by course (curriculum)`
`  46`  `                        EnsureIndex(conn, "IX_Chapters_CID",`
`  47`  `                            "CREATE NONCLUSTERED INDEX IX_Chapters_CID ON Chapters (CID)");`
`  48`  ``
`  49`  `                        // Enrollments by course`
`  50`  `                        EnsureIndex(conn, "IX_Enrollments_CID",`
`  51`  `                            "CREATE NONCLUSTERED INDEX IX_Enrollments_CID ON Enrollments (CID) INCLUDE (StudentUID, Progress)");`
`  52`  `                    }`
`  53`  `                }`
`  54`  `                catch { }`
  - → Handle/log exception.
`  55`  `                _done = true;`
`  56`  `            }`
`  57`  `        }`
`  58`  ``
`  59`  `        private static void EnsureIndex(SqlConnection conn, string indexName, string createSql)`
  - → Database access (pure SQL).
`  60`  `        {`
`  61`  `            try`
  - → Error handling block.
`  62`  `            {`
`  63`  `                using (var check = new SqlCommand(`
  - → Import namespace/types.
`  64`  `                    "SELECT 1 FROM sys.indexes WHERE name = @n AND object_id = OBJECT_ID(@t)", conn))`
`  65`  `                {`
`  66`  `                    // Infer table from CREATE ... ON TableName`
`  67`  `                    string table = null;`
`  68`  `                    int on = createSql.IndexOf(" ON ", StringComparison.OrdinalIgnoreCase);`
`  69`  `                    if (on > 0)`
`  70`  `                    {`
`  71`  `                        string rest = createSql.Substring(on + 4).Trim();`
`  72`  `                        int sp = rest.IndexOfAny(new[] { ' ', '(' });`
`  73`  `                        table = sp > 0 ? rest.Substring(0, sp).Trim() : rest;`
`  74`  `                    }`
`  75`  `                    if (string.IsNullOrEmpty(table)) return;`
`  76`  ``
`  77`  `                    check.Parameters.AddWithValue("@n", indexName);`
`  78`  `                    check.Parameters.AddWithValue("@t", "dbo." + table);`
`  79`  `                    if (check.ExecuteScalar() != null) return;`
  - → Run SQL; return table / rows / scalar.
`  80`  `                }`
`  81`  ``
`  82`  `                using (var create = new SqlCommand(createSql, conn))`
  - → Import namespace/types.
`  83`  `                    create.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  84`  `            }`
`  85`  `            catch`
  - → Handle/log exception.
`  86`  `            {`
`  87`  `                // Column/table missing or include list invalid — ignore`
`  88`  `            }`
`  89`  `        }`
`  90`  `    }`
`  91`  `}`

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
