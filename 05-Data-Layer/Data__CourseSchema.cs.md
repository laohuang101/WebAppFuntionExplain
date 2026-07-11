# CourseSchema.cs
**Source:** `Data/CourseSchema.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Ensures optional Courses columns exist at runtime (e.g. IsPublished BIT) and backfills defaults when safe.

## File overview

- **Total lines:** 69
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 9:** `Gate` — type `object`
- **Line 10:** `_ready` — type `bool`

## Functions / methods (3 found)

### `Ensure` — lines 11–36

```csharp
public static void Ensure()
```

#### Explanation

- **Purpose:** Implements `Ensure`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Local variables:** `conn`, `up`

#### Line-by-line (this function)

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

**Line notes**

- **L18:** Error handling block.
- **L20:** Import namespace/types.
- **L22:** Idempotent schema/index ensure (safe to run many times).
- **L24:** Error handling block.
- **L26:** Import namespace/types.
- **L27:** Course publish flag for Landing catalog.
- **L28:** Run SQL; return table / rows / scalar.
- **L30:** Handle/log exception.
- **L33:** Handle/log exception.

---

### `EnsureColumn` — lines 37–55

```csharp
private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
```

#### Explanation

- **Purpose:** Implements `EnsureColumn`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string table, string column, string definition`
- **Local variables:** `check`, `alter`

#### Line-by-line (this function)

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

**Line notes**

- **L38:** Database access (pure SQL).
- **L40:** Import namespace/types.
- **L44:** Parameterized SQL — prevents classic SQL injection.
- **L45:** Parameterized SQL — prevents classic SQL injection.
- **L46:** Run SQL; return table / rows / scalar.
- **L48:** Error handling block.
- **L50:** Import namespace/types.
- **L52:** Run SQL; return table / rows / scalar.
- **L54:** Handle/log exception.

---

### `HasIsPublished` — lines 56–67

```csharp
public static bool HasIsPublished()
```

#### Explanation

- **Purpose:** Implements `HasIsPublished`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.

#### Line-by-line (this function)

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

**Line notes**

- **L57:** Course publish flag for Landing catalog.
- **L60:** Error handling block.
- **L62:** Database access (pure SQL).
- **L64:** Course publish flag for Landing catalog.
- **L66:** Handle/log exception.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L4:** C# namespace grouping.
- **L18:** Error handling block.
- **L20:** Import namespace/types.
- **L22:** Idempotent schema/index ensure (safe to run many times).
- **L24:** Error handling block.
- **L26:** Import namespace/types.
- **L27:** Course publish flag for Landing catalog.
- **L28:** Run SQL; return table / rows / scalar.
- **L30:** Handle/log exception.
- **L33:** Handle/log exception.
- **L38:** Database access (pure SQL).
- **L40:** Import namespace/types.
- **L44:** Parameterized SQL — prevents classic SQL injection.
- **L45:** Parameterized SQL — prevents classic SQL injection.
- **L46:** Run SQL; return table / rows / scalar.
- **L48:** Error handling block.
- **L50:** Import namespace/types.
- **L52:** Run SQL; return table / rows / scalar.
- **L54:** Handle/log exception.
- **L57:** Course publish flag for Landing catalog.
- **L60:** Error handling block.
- **L62:** Database access (pure SQL).
- **L64:** Course publish flag for Landing catalog.
- **L66:** Handle/log exception.

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
