# CourseSchema.cs
**Source:** `Data/CourseSchema.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Ensures optional columns like `IsPublished` exist.

## File overview

- **Total lines:** 69
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 9:** `Gate` — type `object`
- **Line 10:** `_ready` — type `bool`

## Functions / methods (3 found)

### `Ensure` — lines 11–36

```
public static void Ensure()
```

#### Explanation

- **Purpose:** Implements `Ensure`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Local variables:** `conn`, `up`

#### Line-by-line (this function)

`  11`  ``
`  12`  `        public static void Ensure()`
`  13`  `        {`
`  14`  `            if (_ready) return;`
`  15`  `            lock (Gate)`
`  16`  `            {`
`  17`  `                if (_ready) return;`
`  18`  `                try`
  - → Error handling block.
`  19`  `                {`
`  20`  `                    using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  21`  `                    {`
`  22`  `                        EnsureColumn(conn, "Courses", "IsPublished", "BIT NULL");`
  - → Course publish flag for Landing catalog.
`  23`  `                        // Default existing rows: treat as published if they already have content history`
`  24`  `                        try`
  - → Error handling block.
`  25`  `                        {`
`  26`  `                            using (var up = new SqlCommand(`
  - → Import namespace/types.
`  27`  `                                "UPDATE Courses SET IsPublished = 1 WHERE IsPublished IS NULL", conn))`
  - → Course publish flag for Landing catalog.
`  28`  `                                up.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  29`  `                        }`
`  30`  `                        catch { }`
  - → Handle/log exception.
`  31`  `                    }`
`  32`  `                }`
`  33`  `                catch { }`
  - → Handle/log exception.
`  34`  `                _ready = true;`
`  35`  `            }`
`  36`  `        }`

---

### `EnsureColumn` — lines 37–55

```
private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
```

#### Explanation

- **Purpose:** Implements `EnsureColumn`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string table, string column, string definition`
- **Local variables:** `check`, `alter`

#### Line-by-line (this function)

`  37`  ``
`  38`  `        private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)`
  - → Database access (pure SQL).
`  39`  `        {`
`  40`  `            using (var check = new SqlCommand(@"`
  - → Import namespace/types.
`  41`  `SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS`
`  42`  `WHERE TABLE_NAME = @t AND COLUMN_NAME = @c", conn))`
`  43`  `            {`
`  44`  `                check.Parameters.AddWithValue("@t", table);`
`  45`  `                check.Parameters.AddWithValue("@c", column);`
`  46`  `                if (check.ExecuteScalar() != null) return;`
  - → Run SQL; return table / rows / scalar.
`  47`  `            }`
`  48`  `            try`
  - → Error handling block.
`  49`  `            {`
`  50`  `                using (var alter = new SqlCommand(`
  - → Import namespace/types.
`  51`  `                    "ALTER TABLE [" + table + "] ADD [" + column + "] " + definition, conn))`
`  52`  `                    alter.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  53`  `            }`
`  54`  `            catch { }`
  - → Handle/log exception.
`  55`  `        }`

---

### `HasIsPublished` — lines 56–67

```
public static bool HasIsPublished()
```

#### Explanation

- **Purpose:** Implements `HasIsPublished`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.

#### Line-by-line (this function)

`  56`  ``
`  57`  `        public static bool HasIsPublished()`
  - → Course publish flag for Landing catalog.
`  58`  `        {`
`  59`  `            Ensure();`
`  60`  `            try`
  - → Error handling block.
`  61`  `            {`
`  62`  `                return DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
`  63`  `SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS`
`  64`  `WHERE TABLE_NAME = 'Courses' AND COLUMN_NAME = 'IsPublished'") > 0;`
  - → Course publish flag for Landing catalog.
`  65`  `            }`
`  66`  `            catch { return false; }`
  - → Handle/log exception.
`  67`  `        }`

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
`   6`  `    /// <summary>Ensures optional Courses columns exist (e.g. IsPublished).</summary>`
`   7`  `    public static class CourseSchema`
`   8`  `    {`
`   9`  `        private static readonly object Gate = new object();`
`  10`  `        private static bool _ready;`
`  11`  ``
`  12`  `        public static void Ensure()`
`  13`  `        {`
`  14`  `            if (_ready) return;`
`  15`  `            lock (Gate)`
`  16`  `            {`
`  17`  `                if (_ready) return;`
`  18`  `                try`
  - → Error handling block.
`  19`  `                {`
`  20`  `                    using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  21`  `                    {`
`  22`  `                        EnsureColumn(conn, "Courses", "IsPublished", "BIT NULL");`
  - → Course publish flag for Landing catalog.
`  23`  `                        // Default existing rows: treat as published if they already have content history`
`  24`  `                        try`
  - → Error handling block.
`  25`  `                        {`
`  26`  `                            using (var up = new SqlCommand(`
  - → Import namespace/types.
`  27`  `                                "UPDATE Courses SET IsPublished = 1 WHERE IsPublished IS NULL", conn))`
  - → Course publish flag for Landing catalog.
`  28`  `                                up.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  29`  `                        }`
`  30`  `                        catch { }`
  - → Handle/log exception.
`  31`  `                    }`
`  32`  `                }`
`  33`  `                catch { }`
  - → Handle/log exception.
`  34`  `                _ready = true;`
`  35`  `            }`
`  36`  `        }`
`  37`  ``
`  38`  `        private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)`
  - → Database access (pure SQL).
`  39`  `        {`
`  40`  `            using (var check = new SqlCommand(@"`
  - → Import namespace/types.
`  41`  `SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS`
`  42`  `WHERE TABLE_NAME = @t AND COLUMN_NAME = @c", conn))`
`  43`  `            {`
`  44`  `                check.Parameters.AddWithValue("@t", table);`
`  45`  `                check.Parameters.AddWithValue("@c", column);`
`  46`  `                if (check.ExecuteScalar() != null) return;`
  - → Run SQL; return table / rows / scalar.
`  47`  `            }`
`  48`  `            try`
  - → Error handling block.
`  49`  `            {`
`  50`  `                using (var alter = new SqlCommand(`
  - → Import namespace/types.
`  51`  `                    "ALTER TABLE [" + table + "] ADD [" + column + "] " + definition, conn))`
`  52`  `                    alter.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  53`  `            }`
`  54`  `            catch { }`
  - → Handle/log exception.
`  55`  `        }`
`  56`  ``
`  57`  `        public static bool HasIsPublished()`
  - → Course publish flag for Landing catalog.
`  58`  `        {`
`  59`  `            Ensure();`
`  60`  `            try`
  - → Error handling block.
`  61`  `            {`
`  62`  `                return DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
`  63`  `SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS`
`  64`  `WHERE TABLE_NAME = 'Courses' AND COLUMN_NAME = 'IsPublished'") > 0;`
  - → Course publish flag for Landing catalog.
`  65`  `            }`
`  66`  `            catch { return false; }`
  - → Handle/log exception.
`  67`  `        }`
`  68`  `    }`
`  69`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.Data.SqlClient;

namespace WebAppAssignment.Data
{
    /// <summary>Ensures optional Courses columns exist (e.g. IsPublished).</summary>
    public static class CourseSchema
    {
        private static readonly object Gate = new object();
        private static bool _ready;

        public static void Ensure()
        {
            if (_ready) return;
            lock (Gate)
            {
                if (_ready) return;
                try
                {
                    using (var conn = DbHelper.OpenConnection())
                    {
                        EnsureColumn(conn, "Courses", "IsPublished", "BIT NULL");
                        // Default existing rows: treat as published if they already have content history
                        try
                        {
                            using (var up = new SqlCommand(
                                "UPDATE Courses SET IsPublished = 1 WHERE IsPublished IS NULL", conn))
                                up.ExecuteNonQuery();
                        }
                        catch { }
                    }
                }
                catch { }
                _ready = true;
            }
        }

        private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
        {
            using (var check = new SqlCommand(@"
SELECT 1 FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = @t AND COLUMN_NAME = @c", conn))
            {
                check.Parameters.AddWithValue("@t", table);
                check.Parameters.AddWithValue("@c", column);
                if (check.ExecuteScalar() != null) return;
            }
            try
            {
                using (var alter = new SqlCommand(
                    "ALTER TABLE [" + table + "] ADD [" + column + "] " + definition, conn))
                    alter.ExecuteNonQuery();
            }
            catch { }
        }

        public static bool HasIsPublished()
        {
            Ensure();
            try
            {
                return DbHelper.ExecuteScalarInt(@"
SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Courses' AND COLUMN_NAME = 'IsPublished'") > 0;
            }
            catch { return false; }
        }
    }
}

```
