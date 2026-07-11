# SecurityAudit.cs
**Source:** `Data/Security/SecurityAudit.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Append-only security event log (login, register, reset, seed, uploads) for Admin AuditLog.

## File overview

- **Total lines:** 108
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (4 found)

### `Log` — lines 13–53

#### Signature

```csharp
public static void Log(string action, int? userId = null, string detail = null, string email = null)
```

#### What it is

Writes one security event row (login, register, reset, etc.) for the audit log.

#### How it works

1. Save temporary state in Session (`Session !`).
2. Save temporary state in Session (`Session["UserID"]);`).
3. Open a connection to the LocalDB / SQL Server database.
4. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `action` | `string` | Holds “action” for this scope. (text) |
| `userId` | `int?` | Identifier (`userId`) — database primary/foreign key. (type `int?`) |
| `detail` | `string` | Holds “detail” for this scope. (text) |
| `email` | `string` | Account email address (usually lowercased). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ip` | `string` | Client IP address for throttle/audit. |
| `path` | `string` | File path under Uploads or URL path. |
| `ctx` | `var` | Current HTTP request context (Request, Response, Session). |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |

#### Code

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

---

### `Query` — lines 54–79

#### Signature

```csharp
public static DataTable Query(int take = 100, string actionFilter = null)
```

#### What it is

Reads recent security audit events for the Admin audit page.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `take` | `int` | Holds “take” for this scope. (integer) |
| `actionFilter` | `string` | Holds “action Filter” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `take` | `int` | Holds “take” for this scope. (integer) |
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `da` | `var` | Holds “da” for this scope.  Newly constructed object. |

#### Code

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

---

### `QueryObjects` — lines 80–100

#### Signature

```csharp
public static List<object> QueryObjects(int take = 100, string actionFilter = null)
```

#### What it is

Function `QueryObjects` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `QueryObjects`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `take` | `int` | Holds “take” for this scope. (integer) |
| `actionFilter` | `string` | Holds “action Filter” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `take` | `int` | Holds “take” for this scope. (integer)  Newly constructed object. |
| `dt` | `var` | DataTable — full result set from SQL (many rows/columns). |
| `r` | `—` | Usually one database row (DataRow) in query loops. |

#### Code

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

---

### `Truncate` — lines 101–106

#### Signature

```csharp
private static string Truncate(string s, int max)
```

#### What it is

Function `Truncate` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `string` | String being cleaned or built. |
| `max` | `int` | Holds “max” for this scope. (integer) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 101 | 
 102 |         private static string Truncate(string s, int max)
 103 |         {
 104 |             if (string.IsNullOrEmpty(s)) return s;
 105 |             return s.Length <= max ? s : s.Substring(0, max);
 106 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
