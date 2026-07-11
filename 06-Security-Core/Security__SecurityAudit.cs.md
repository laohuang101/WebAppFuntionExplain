# SecurityAudit.cs
**Source:** `Data/Security/SecurityAudit.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Append-only security event log (login, register, reset, seed, uploads) for Admin AuditLog.

## File overview

- **Total lines:** 108
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 18:** `ip` — type `string`
- **Line 19:** `path` — type `string`
- **Line 22:** `ctx` — type `var`
- **Line 59:** `sql` — type `string`
- **Line 74:** `dt` — type `var`
- **Line 76:** `dt` — type `return`
- **Line 83:** `list` — type `var`
- **Line 84:** `dt` — type `var`
- **Line 99:** `list` — type `return`

## Functions / methods (4 found)

### `Log` — lines 13–53

```csharp
public static void Log(string action, int? userId = null, string detail = null, string email = null)
```

#### Explanation

- **Purpose:** Implements `Log`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `string action, int? userId = null, string detail = null, string email = null`
- **Local variables:** `detail`, `email`, `ip`, `path`, `ctx`, `conn`, `cmd`

#### Line-by-line (this function)

```csharp
  13 |         public static void Log(string action, int? userId = null, string detail = null, string email = null)
  14 |         {
  15 |             try
  16 |             {
  17 |                 AuthSchema.Ensure();
  18 |                 string ip = null;
  19 |                 string path = null;
  20 |                 try
  21 |                 {
  22 |                     var ctx = HttpContext.Current;
  23 |                     if (ctx != null && ctx.Request != null)
  24 |                     {
  25 |                         ip = ctx.Request.UserHostAddress;
  26 |                         path = ctx.Request.RawUrl;
  27 |                         if (userId == null && ctx.Session != null && ctx.Session["UserID"] != null)
  28 |                             userId = Convert.ToInt32(ctx.Session["UserID"]);
  29 |                     }
  30 |                 }
  31 |                 catch { }
  32 | 
  33 |                 using (var conn = DbHelper.OpenConnection())
  34 |                 using (var cmd = new SqlCommand(@"
  35 | INSERT INTO AuditLog (OccurredAt, Action, UserId, Email, Detail, IpAddress, Path)
  36 | VALUES (@At, @Action, @UserId, @Email, @Detail, @Ip, @Path)", conn))
  37 |                 {
  38 |                     cmd.Parameters.AddWithValue("@At", DateTime.UtcNow);
  39 |                     cmd.Parameters.AddWithValue("@Action", (action ?? "unknown").Length > 80
  40 |                         ? (action ?? "").Substring(0, 80) : (action ?? "unknown"));
  41 |                     cmd.Parameters.AddWithValue("@UserId", (object)userId ?? DBNull.Value);
  42 |                     cmd.Parameters.AddWithValue("@Email", (object)Truncate(email, 120) ?? DBNull.Value);
  43 |                     cmd.Parameters.AddWithValue("@Detail", (object)Truncate(detail, 500) ?? DBNull.Value);
  44 |                     cmd.Parameters.AddWithValue("@Ip", (object)Truncate(ip, 64) ?? DBNull.Value);
  45 |                     cmd.Parameters.AddWithValue("@Path", (object)Truncate(path, 260) ?? DBNull.Value);
  46 |                     cmd.ExecuteNonQuery();
  47 |                 }
  48 |             }
  49 |             catch
  50 |             {
  51 |                 // Never break main flow if audit fails
  52 |             }
  53 |         }
```

**Line notes**

- **L15:** Error handling block.
- **L20:** Error handling block.
- **L27:** Server session for logged-in user.
- **L28:** Server session for logged-in user.
- **L31:** Handle/log exception.
- **L33:** Import namespace/types.
- **L34:** Import namespace/types.
- **L35:** Write/read security audit events.
- **L38:** Parameterized SQL — prevents classic SQL injection.
- **L39:** Parameterized SQL — prevents classic SQL injection.
- **L41:** Parameterized SQL — prevents classic SQL injection.
- **L42:** Parameterized SQL — prevents classic SQL injection.
- **L43:** Parameterized SQL — prevents classic SQL injection.
- **L44:** Parameterized SQL — prevents classic SQL injection.
- **L45:** Parameterized SQL — prevents classic SQL injection.
- **L46:** Run SQL; return table / rows / scalar.
- **L49:** Handle/log exception.

---

### `Query` — lines 54–79

```csharp
public static DataTable Query(int take = 100, string actionFilter = null)
```

#### Explanation

- **Purpose:** Implements `Query`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `int take = 100, string actionFilter = null`
- **Local variables:** `take`, `actionFilter`, `sql`, `conn`, `cmd`, `da`, `dt`

#### Line-by-line (this function)

```csharp
  54 | 
  55 |         public static DataTable Query(int take = 100, string actionFilter = null)
  56 |         {
  57 |             AuthSchema.Ensure();
  58 |             take = Math.Max(1, Math.Min(500, take));
  59 |             string sql = @"
  60 | SELECT TOP (@Take) LogId, OccurredAt, Action, UserId, Email, Detail, IpAddress, Path
  61 | FROM AuditLog";
  62 |             if (!string.IsNullOrWhiteSpace(actionFilter))
  63 |                 sql += " WHERE Action LIKE @A";
  64 |             sql += " ORDER BY LogId DESC";
  65 | 
  66 |             using (var conn = DbHelper.OpenConnection())
  67 |             using (var cmd = new SqlCommand(sql, conn))
  68 |             {
  69 |                 cmd.Parameters.AddWithValue("@Take", take);
  70 |                 if (!string.IsNullOrWhiteSpace(actionFilter))
  71 |                     cmd.Parameters.AddWithValue("@A", "%" + actionFilter.Trim() + "%");
  72 |                 using (var da = new SqlDataAdapter(cmd))
  73 |                 {
  74 |                     var dt = new DataTable();
  75 |                     da.Fill(dt);
  76 |                     return dt;
  77 |                 }
  78 |             }
  79 |         }
```

**Line notes**

- **L55:** In-memory result set from ADO.NET.
- **L61:** Write/read security audit events.
- **L66:** Import namespace/types.
- **L67:** Import namespace/types.
- **L69:** Parameterized SQL — prevents classic SQL injection.
- **L71:** Parameterized SQL — prevents classic SQL injection.
- **L72:** Import namespace/types.
- **L74:** In-memory result set from ADO.NET.

---

### `QueryObjects` — lines 80–100

```csharp
public static List<object> QueryObjects(int take = 100, string actionFilter = null)
```

#### Explanation

- **Purpose:** Implements `QueryObjects`.
- **Parameters:** `int take = 100, string actionFilter = null`
- **Local variables:** `take`, `actionFilter`, `list`, `dt`

#### Line-by-line (this function)

```csharp
  80 | 
  81 |         public static List<object> QueryObjects(int take = 100, string actionFilter = null)
  82 |         {
  83 |             var list = new List<object>();
  84 |             var dt = Query(take, actionFilter);
  85 |             foreach (DataRow r in dt.Rows)
  86 |             {
  87 |                 list.Add(new
  88 |                 {
  89 |                     logId = Convert.ToInt32(r["LogId"]),
  90 |                     at = Convert.ToDateTime(r["OccurredAt"]).ToString("yyyy-MM-dd HH:mm:ss") + " UTC",
  91 |                     action = r["Action"] == DBNull.Value ? "" : r["Action"].ToString(),
  92 |                     userId = r["UserId"] == DBNull.Value ? (int?)null : Convert.ToInt32(r["UserId"]),
  93 |                     email = r["Email"] == DBNull.Value ? "" : r["Email"].ToString(),
  94 |                     detail = r["Detail"] == DBNull.Value ? "" : r["Detail"].ToString(),
  95 |                     ip = r["IpAddress"] == DBNull.Value ? "" : r["IpAddress"].ToString(),
  96 |                     path = r["Path"] == DBNull.Value ? "" : r["Path"].ToString()
  97 |                 });
  98 |             }
  99 |             return list;
 100 |         }
```

**Line notes**

- **L85:** In-memory result set from ADO.NET.
- **L91:** Null-safe read from database values.
- **L92:** Null-safe read from database values.
- **L93:** Null-safe read from database values.
- **L94:** Null-safe read from database values.
- **L95:** Null-safe read from database values.
- **L96:** Null-safe read from database values.

---

### `Truncate` — lines 101–106

```csharp
private static string Truncate(string s, int max)
```

#### Explanation

- **Purpose:** Implements `Truncate`.
- **Parameters:** `string s, int max`

#### Line-by-line (this function)

```csharp
 101 | 
 102 |         private static string Truncate(string s, int max)
 103 |         {
 104 |             if (string.IsNullOrEmpty(s)) return s;
 105 |             return s.Length <= max ? s : s.Substring(0, max);
 106 |         }
```

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```csharp
   1 | using System;
   2 | using System.Collections.Generic;
   3 | using System.Data;
   4 | using System.Data.SqlClient;
   5 | using System.Web;
   6 | using WebAppAssignment.Data;
   7 | 
   8 | namespace WebAppAssignment.Data.Security
   9 | {
  10 |     /// <summary>Append-only security / admin audit trail.</summary>
  11 |     public static class SecurityAudit
  12 |     {
  13 |         public static void Log(string action, int? userId = null, string detail = null, string email = null)
  14 |         {
  15 |             try
  16 |             {
  17 |                 AuthSchema.Ensure();
  18 |                 string ip = null;
  19 |                 string path = null;
  20 |                 try
  21 |                 {
  22 |                     var ctx = HttpContext.Current;
  23 |                     if (ctx != null && ctx.Request != null)
  24 |                     {
  25 |                         ip = ctx.Request.UserHostAddress;
  26 |                         path = ctx.Request.RawUrl;
  27 |                         if (userId == null && ctx.Session != null && ctx.Session["UserID"] != null)
  28 |                             userId = Convert.ToInt32(ctx.Session["UserID"]);
  29 |                     }
  30 |                 }
  31 |                 catch { }
  32 | 
  33 |                 using (var conn = DbHelper.OpenConnection())
  34 |                 using (var cmd = new SqlCommand(@"
  35 | INSERT INTO AuditLog (OccurredAt, Action, UserId, Email, Detail, IpAddress, Path)
  36 | VALUES (@At, @Action, @UserId, @Email, @Detail, @Ip, @Path)", conn))
  37 |                 {
  38 |                     cmd.Parameters.AddWithValue("@At", DateTime.UtcNow);
  39 |                     cmd.Parameters.AddWithValue("@Action", (action ?? "unknown").Length > 80
  40 |                         ? (action ?? "").Substring(0, 80) : (action ?? "unknown"));
  41 |                     cmd.Parameters.AddWithValue("@UserId", (object)userId ?? DBNull.Value);
  42 |                     cmd.Parameters.AddWithValue("@Email", (object)Truncate(email, 120) ?? DBNull.Value);
  43 |                     cmd.Parameters.AddWithValue("@Detail", (object)Truncate(detail, 500) ?? DBNull.Value);
  44 |                     cmd.Parameters.AddWithValue("@Ip", (object)Truncate(ip, 64) ?? DBNull.Value);
  45 |                     cmd.Parameters.AddWithValue("@Path", (object)Truncate(path, 260) ?? DBNull.Value);
  46 |                     cmd.ExecuteNonQuery();
  47 |                 }
  48 |             }
  49 |             catch
  50 |             {
  51 |                 // Never break main flow if audit fails
  52 |             }
  53 |         }
  54 | 
  55 |         public static DataTable Query(int take = 100, string actionFilter = null)
  56 |         {
  57 |             AuthSchema.Ensure();
  58 |             take = Math.Max(1, Math.Min(500, take));
  59 |             string sql = @"
  60 | SELECT TOP (@Take) LogId, OccurredAt, Action, UserId, Email, Detail, IpAddress, Path
  61 | FROM AuditLog";
  62 |             if (!string.IsNullOrWhiteSpace(actionFilter))
  63 |                 sql += " WHERE Action LIKE @A";
  64 |             sql += " ORDER BY LogId DESC";
  65 | 
  66 |             using (var conn = DbHelper.OpenConnection())
  67 |             using (var cmd = new SqlCommand(sql, conn))
  68 |             {
  69 |                 cmd.Parameters.AddWithValue("@Take", take);
  70 |                 if (!string.IsNullOrWhiteSpace(actionFilter))
  71 |                     cmd.Parameters.AddWithValue("@A", "%" + actionFilter.Trim() + "%");
  72 |                 using (var da = new SqlDataAdapter(cmd))
  73 |                 {
  74 |                     var dt = new DataTable();
  75 |                     da.Fill(dt);
  76 |                     return dt;
  77 |                 }
  78 |             }
  79 |         }
  80 | 
  81 |         public static List<object> QueryObjects(int take = 100, string actionFilter = null)
  82 |         {
  83 |             var list = new List<object>();
  84 |             var dt = Query(take, actionFilter);
  85 |             foreach (DataRow r in dt.Rows)
  86 |             {
  87 |                 list.Add(new
  88 |                 {
  89 |                     logId = Convert.ToInt32(r["LogId"]),
  90 |                     at = Convert.ToDateTime(r["OccurredAt"]).ToString("yyyy-MM-dd HH:mm:ss") + " UTC",
  91 |                     action = r["Action"] == DBNull.Value ? "" : r["Action"].ToString(),
  92 |                     userId = r["UserId"] == DBNull.Value ? (int?)null : Convert.ToInt32(r["UserId"]),
  93 |                     email = r["Email"] == DBNull.Value ? "" : r["Email"].ToString(),
  94 |                     detail = r["Detail"] == DBNull.Value ? "" : r["Detail"].ToString(),
  95 |                     ip = r["IpAddress"] == DBNull.Value ? "" : r["IpAddress"].ToString(),
  96 |                     path = r["Path"] == DBNull.Value ? "" : r["Path"].ToString()
  97 |                 });
  98 |             }
  99 |             return list;
 100 |         }
 101 | 
 102 |         private static string Truncate(string s, int max)
 103 |         {
 104 |             if (string.IsNullOrEmpty(s)) return s;
 105 |             return s.Length <= max ? s : s.Substring(0, max);
 106 |         }
 107 |     }
 108 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L8:** C# namespace grouping.
- **L11:** Write/read security audit events.
- **L15:** Error handling block.
- **L20:** Error handling block.
- **L27:** Server session for logged-in user.
- **L28:** Server session for logged-in user.
- **L31:** Handle/log exception.
- **L33:** Import namespace/types.
- **L34:** Import namespace/types.
- **L35:** Write/read security audit events.
- **L38:** Parameterized SQL — prevents classic SQL injection.
- **L39:** Parameterized SQL — prevents classic SQL injection.
- **L41:** Parameterized SQL — prevents classic SQL injection.
- **L42:** Parameterized SQL — prevents classic SQL injection.
- **L43:** Parameterized SQL — prevents classic SQL injection.
- **L44:** Parameterized SQL — prevents classic SQL injection.
- **L45:** Parameterized SQL — prevents classic SQL injection.
- **L46:** Run SQL; return table / rows / scalar.
- **L49:** Handle/log exception.
- **L55:** In-memory result set from ADO.NET.
- **L61:** Write/read security audit events.
- **L66:** Import namespace/types.
- **L67:** Import namespace/types.
- **L69:** Parameterized SQL — prevents classic SQL injection.
- **L71:** Parameterized SQL — prevents classic SQL injection.
- **L72:** Import namespace/types.
- **L74:** In-memory result set from ADO.NET.
- **L85:** In-memory result set from ADO.NET.
- **L91:** Null-safe read from database values.
- **L92:** Null-safe read from database values.
- **L93:** Null-safe read from database values.
- **L94:** Null-safe read from database values.
- **L95:** Null-safe read from database values.
- **L96:** Null-safe read from database values.

## Source snapshot (raw)

```csharp
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Web;
using WebAppAssignment.Data;

namespace WebAppAssignment.Data.Security
{
    /// <summary>Append-only security / admin audit trail.</summary>
    public static class SecurityAudit
    {
        public static void Log(string action, int? userId = null, string detail = null, string email = null)
        {
            try
            {
                AuthSchema.Ensure();
                string ip = null;
                string path = null;
                try
                {
                    var ctx = HttpContext.Current;
                    if (ctx != null && ctx.Request != null)
                    {
                        ip = ctx.Request.UserHostAddress;
                        path = ctx.Request.RawUrl;
                        if (userId == null && ctx.Session != null && ctx.Session["UserID"] != null)
                            userId = Convert.ToInt32(ctx.Session["UserID"]);
                    }
                }
                catch { }

                using (var conn = DbHelper.OpenConnection())
                using (var cmd = new SqlCommand(@"
INSERT INTO AuditLog (OccurredAt, Action, UserId, Email, Detail, IpAddress, Path)
VALUES (@At, @Action, @UserId, @Email, @Detail, @Ip, @Path)", conn))
                {
                    cmd.Parameters.AddWithValue("@At", DateTime.UtcNow);
                    cmd.Parameters.AddWithValue("@Action", (action ?? "unknown").Length > 80
                        ? (action ?? "").Substring(0, 80) : (action ?? "unknown"));
                    cmd.Parameters.AddWithValue("@UserId", (object)userId ?? DBNull.Value);
                    cmd.Parameters.AddWithValue("@Email", (object)Truncate(email, 120) ?? DBNull.Value);
                    cmd.Parameters.AddWithValue("@Detail", (object)Truncate(detail, 500) ?? DBNull.Value);
                    cmd.Parameters.AddWithValue("@Ip", (object)Truncate(ip, 64) ?? DBNull.Value);
                    cmd.Parameters.AddWithValue("@Path", (object)Truncate(path, 260) ?? DBNull.Value);
                    cmd.ExecuteNonQuery();
                }
            }
            catch
            {
                // Never break main flow if audit fails
            }
        }

        public static DataTable Query(int take = 100, string actionFilter = null)
        {
            AuthSchema.Ensure();
            take = Math.Max(1, Math.Min(500, take));
            string sql = @"
SELECT TOP (@Take) LogId, OccurredAt, Action, UserId, Email, Detail, IpAddress, Path
FROM AuditLog";
            if (!string.IsNullOrWhiteSpace(actionFilter))
                sql += " WHERE Action LIKE @A";
            sql += " ORDER BY LogId DESC";

            using (var conn = DbHelper.OpenConnection())
            using (var cmd = new SqlCommand(sql, conn))
            {
                cmd.Parameters.AddWithValue("@Take", take);
                if (!string.IsNullOrWhiteSpace(actionFilter))
                    cmd.Parameters.AddWithValue("@A", "%" + actionFilter.Trim() + "%");
                using (var da = new SqlDataAdapter(cmd))
                {
                    var dt = new DataTable();
                    da.Fill(dt);
                    return dt;
                }
            }
        }

        public static List<object> QueryObjects(int take = 100, string actionFilter = null)
        {
            var list = new List<object>();
            var dt = Query(take, actionFilter);
            foreach (DataRow r in dt.Rows)
            {
                list.Add(new
                {
                    logId = Convert.ToInt32(r["LogId"]),
                    at = Convert.ToDateTime(r["OccurredAt"]).ToString("yyyy-MM-dd HH:mm:ss") + " UTC",
                    action = r["Action"] == DBNull.Value ? "" : r["Action"].ToString(),
                    userId = r["UserId"] == DBNull.Value ? (int?)null : Convert.ToInt32(r["UserId"]),
                    email = r["Email"] == DBNull.Value ? "" : r["Email"].ToString(),
                    detail = r["Detail"] == DBNull.Value ? "" : r["Detail"].ToString(),
                    ip = r["IpAddress"] == DBNull.Value ? "" : r["IpAddress"].ToString(),
                    path = r["Path"] == DBNull.Value ? "" : r["Path"].ToString()
                });
            }
            return list;
        }

        private static string Truncate(string s, int max)
        {
            if (string.IsNullOrEmpty(s)) return s;
            return s.Length <= max ? s : s.Substring(0, max);
        }
    }
}

```
