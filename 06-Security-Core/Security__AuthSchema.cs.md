# AuthSchema.cs
**Source:** `Data/Security/AuthSchema.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Ensures Users security columns exist (PasswordHash, MfaSecret, MfaEnabled, JWT-related helpers).

## File overview

- **Total lines:** 109
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 12:** `Gate` (`object`) — **Holds “Gate” for this scope.**
- **Line 13:** `_ready` (`bool`) — **Holds “ready” for this scope. (true/false)**
- **Line 77:** `TABLE_NAME` (`WHERE`) — **Holds “TABLE NAME” for this scope. (type `WHERE`)**
- **Line 94:** `simple` (`string`) — **Holds “simple” for this scope. (text)**

## Functions / methods (4 found)

### `Ensure` — lines 14–43

```csharp
public static void Ensure()
```

#### Explanation

- **Purpose:** Implements `Ensure`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L21:** Error handling block.
- **L23:** Import namespace/types.
- **L25:** Idempotent schema/index ensure (safe to run many times).
- **L26:** Idempotent schema/index ensure (safe to run many times).
- **L27:** Idempotent schema/index ensure (safe to run many times).
- **L28:** Idempotent schema/index ensure (safe to run many times).
- **L29:** Idempotent schema/index ensure (safe to run many times).
- **L30:** Idempotent schema/index ensure (safe to run many times).
- **L31:** Idempotent schema/index ensure (safe to run many times).
- **L32:** Idempotent schema/index ensure (safe to run many times).
- **L37:** Handle/log exception.

---

### `EnsureAuditTable` — lines 44–71

```csharp
private static void EnsureAuditTable(SqlConnection conn)
```

#### Explanation

- **Purpose:** Implements `EnsureAuditTable`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- **Local variables (what each means):**
- `check` (`var`) — Holds “check” for this scope.  Newly constructed object.
- `create` (`var`) — Holds “create” for this scope.  Newly constructed object.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L45:** Database access (pure SQL).
- **L47:** Error handling block.
- **L49:** Import namespace/types.
- **L50:** Write/read security audit events.
- **L52:** Run SQL; return table / rows / scalar.
- **L55:** Import namespace/types.
- **L56:** Write/read security audit events.
- **L67:** Run SQL; return table / rows / scalar.
- **L70:** Handle/log exception.

---

### `NVARCHAR` — lines 59–68

```csharp
Action NVARCHAR(80) NOT NULL,
    UserId INT NULL,
    Email NVARCHAR(120) NULL,
    Detail NVARCHAR(500) NULL,
    IpAddress NVARCHAR(64) NULL,
    Path NVARCHAR(260) NULL
)", conn))
```

#### Explanation

- **Purpose:** Implements `NVARCHAR`.
- **Parameters (what each means):**
- `NULL` (`80) NOT`) — Holds “NULL” for this scope. (type `80) NOT`)
- `NULL` (`UserId INT`) — Holds “NULL” for this scope. (type `UserId INT`)
- `NULL` (`Email NVARCHAR(120)`) — Holds “NULL” for this scope. (type `Email NVARCHAR(120)`)
- `NULL` (`Detail NVARCHAR(500)`) — Holds “NULL” for this scope. (type `Detail NVARCHAR(500)`)
- `NULL` (`IpAddress NVARCHAR(64)`) — Holds “NULL” for this scope. (type `IpAddress NVARCHAR(64)`)
- `)"` (`Path NVARCHAR(260) NULL`) — Holds “)"” for this scope. (type `Path NVARCHAR(260) NULL`)
- `conn)` — Holds “conn)” for this scope.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L67:** Run SQL; return table / rows / scalar.

---

### `EnsureColumn` — lines 72–107

```csharp
private static void EnsureColumn(SqlConnection conn, string table, string column, string definition)
```

#### Explanation

- **Purpose:** Implements `EnsureColumn`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `table` (`string`) — DataTable or HTML table container.
- `column` (`string`) — Holds “column” for this scope. (text)
- `definition` (`string`) — Holds “definition” for this scope. (text)
- **Local variables (what each means):**
- `check` (`var`) — Holds “check” for this scope.  Newly constructed object.
- `alter` (`var`) — Holds “alter” for this scope.  Newly constructed object.
- `simple` (`string`) — Holds “simple” for this scope. (text)

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L73:** Database access (pure SQL).
- **L75:** Import namespace/types.
- **L79:** Parameterized SQL — prevents classic SQL injection.
- **L80:** Parameterized SQL — prevents classic SQL injection.
- **L81:** Run SQL; return table / rows / scalar.
- **L84:** Error handling block.
- **L86:** Import namespace/types.
- **L89:** Run SQL; return table / rows / scalar.
- **L92:** Handle/log exception.
<<<<<<< HEAD
=======
- **L94:** `simple` means: Holds “simple” for this scope. (text)
>>>>>>> eb8ce01 (update)
- **L97:** Error handling block.
- **L99:** Import namespace/types.
- **L102:** Run SQL; return table / rows / scalar.
- **L105:** Handle/log exception.

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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L21:** Error handling block.
- **L23:** Import namespace/types.
- **L25:** Idempotent schema/index ensure (safe to run many times).
- **L26:** Idempotent schema/index ensure (safe to run many times).
- **L27:** Idempotent schema/index ensure (safe to run many times).
- **L28:** Idempotent schema/index ensure (safe to run many times).
- **L29:** Idempotent schema/index ensure (safe to run many times).
- **L30:** Idempotent schema/index ensure (safe to run many times).
- **L31:** Idempotent schema/index ensure (safe to run many times).
- **L32:** Idempotent schema/index ensure (safe to run many times).
- **L37:** Handle/log exception.
- **L45:** Database access (pure SQL).
- **L47:** Error handling block.
- **L49:** Import namespace/types.
- **L50:** Write/read security audit events.
- **L52:** Run SQL; return table / rows / scalar.
- **L55:** Import namespace/types.
- **L56:** Write/read security audit events.
- **L67:** Run SQL; return table / rows / scalar.
- **L70:** Handle/log exception.
- **L73:** Database access (pure SQL).
- **L75:** Import namespace/types.
- **L79:** Parameterized SQL — prevents classic SQL injection.
- **L80:** Parameterized SQL — prevents classic SQL injection.
- **L81:** Run SQL; return table / rows / scalar.
- **L84:** Error handling block.
- **L86:** Import namespace/types.
- **L89:** Run SQL; return table / rows / scalar.
- **L92:** Handle/log exception.
<<<<<<< HEAD
=======
- **L94:** `simple` means: Holds “simple” for this scope. (text)
>>>>>>> eb8ce01 (update)
- **L97:** Error handling block.
- **L99:** Import namespace/types.
- **L102:** Run SQL; return table / rows / scalar.
- **L105:** Handle/log exception.

## Source snapshot (raw)

```csharp
using System;
using System.Data.SqlClient;
using WebAppAssignment.Data;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// Ensures auth-related columns / audit tables exist (pure SQL ALTER - no EF).
    /// </summary>
    public static class AuthSchema
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
                        EnsureColumn(conn, "Users", "PasswordHash", "NVARCHAR(200) NULL");
                        EnsureColumn(conn, "Users", "MfaSecret", "NVARCHAR(64) NULL");
                        EnsureColumn(conn, "Users", "MfaEnabled", "BIT NOT NULL CONSTRAINT DF_Users_MfaEnabled DEFAULT(0)");
                        EnsureColumn(conn, "Users", "EmailOtp", "NVARCHAR(12) NULL");
                        EnsureColumn(conn, "Users", "EmailOtpExpiry", "DATETIME NULL");
                        EnsureColumn(conn, "Users", "CreatedAt", "DATETIME NULL");
                        EnsureColumn(conn, "Users", "PasswordResetToken", "NVARCHAR(128) NULL");
                        EnsureColumn(conn, "Users", "PasswordResetExpiry", "DATETIME NULL");
                        EnsureAuditTable(conn);
                    }
                    _ready = true;
                }
                catch
                {
                    // Table might use different name; don't crash app start
                    _ready = true;
                }
            }
        }

        private static void EnsureAuditTable(SqlConnection conn)
        {
            try
            {
                using (var check = new SqlCommand(@"
SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'AuditLog'", conn))
                {
                    if (check.ExecuteScalar() != null) return;
                }

                using (var create = new SqlCommand(@"
CREATE TABLE AuditLog (
    LogId INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    OccurredAt DATETIME NOT NULL,
    Action NVARCHAR(80) NOT NULL,
    UserId INT NULL,
    Email NVARCHAR(120) NULL,
    Detail NVARCHAR(500) NULL,
    IpAddress NVARCHAR(64) NULL,
    Path NVARCHAR(260) NULL
)", conn))
                {
                    create.ExecuteNonQuery();
                }
            }
            catch { }
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
                {
                    alter.ExecuteNonQuery();
                }
            }
            catch
            {
                string simple = definition
                .Replace(" CONSTRAINT DF_Users_MfaEnabled DEFAULT(0)", " NULL")
                .Replace("NOT NULL", "NULL");
                try
                {
                    using (var alter = new SqlCommand(
                    "ALTER TABLE [" + table + "] ADD [" + column + "] " + simple, conn))
                    {
                        alter.ExecuteNonQuery();
                    }
                }
                catch { /* column may already exist under race */ }
            }
        }
    }
}

```
