# ManageSubmissions.aspx.cs
**Source:** `Pages/Lecturer/ManageSubmissions.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 130
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `ConnString` | `string` | Holds “Conn String” for this scope. (text) |

## Functions / methods (4 found)

### `Page_Load` — lines 17–23

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. ASP.NET calls this automatically on every request.
2. On first load (`!IsPostBack`), initialize UI or redirect if already logged in.
3. On postback, button handlers run separately after this method.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  17 | 
  18 |         protected void Page_Load(object sender, EventArgs e)
  19 |         {
  20 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  21 |                 return;
  22 | 
  23 |         }
```

---

### `GetAssignments` — lines 27–62

#### Signature

```csharp
public static object GetAssignments()
```

#### What it is

Reads/loads data related to **Assignments** and returns it for display or further use.

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.
2. Open a connection to the LocalDB / SQL Server database.
3. Build and return the result object (success or data for the UI).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous). |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `cols` | `var` | Often a collection related to cols (plural name).  Newly constructed object. |
| `cc` | `var` | Holds “cc” for this scope. |
| `r` | `var` | Usually one database row (DataRow) in query loops. |
| `ownerCol` | `string` | Holds “owner Col” for this scope. (text) |
| `list` | `var` | In-memory collection being built for JSON return.  Newly constructed object. |
| `rdr` | `var` | Holds “rdr” for this scope. |

#### Code

```csharp
  27 |         public static object GetAssignments()
  28 |         {
  29 |             try
  30 |             {
  31 |                 int uid = AuthGate.RequireLecturer();
  32 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  33 | 
  34 |                 using (var conn = new SqlConnection(ConnString))
  35 |                 using (var cmd = conn.CreateCommand())
  36 |                 {
  37 |                     conn.Open();
  38 |                     // detect owner column
  39 |                     var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
  40 |                     using (var cc = conn.CreateCommand()) { cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'"; using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); } }
  41 |                     string ownerCol = cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));
  42 | 
  43 |                     cmd.CommandText = $@"SELECT cw.CWID, cw.Title, c.Name AS CourseName FROM CourseWorks cw
  44 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  45 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  46 |                     JOIN Courses c ON ch.CID = c.CID
  47 |                     WHERE c.[{ownerCol}] = @uid ORDER BY cw.CreatedAt DESC";
  48 |                     cmd.Parameters.AddWithValue("@uid", uid);
  49 |                     var list = new List<object>();
  50 |                     using (var rdr = cmd.ExecuteReader())
  51 |                     {
  52 |                         while (rdr.Read()) list.Add(new { cwid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0), title = rdr.IsDBNull(1) ? "" : rdr.GetString(1), course = rdr.IsDBNull(2) ? "" : rdr.GetString(2) });
  53 |                     }
  54 |                     return new { success = true, assignments = list };
  55 |                 }
  56 |             }
  57 |             catch (Exception ex)
  58 |             {
  59 |                 try { Logger.Error(ex, "ManageSubmissions.GetAssignments"); } catch { }
  60 |                 return new { success = false, message = "Request failed." };
  61 |             }
  62 |         }
```

---

### `GetSubmissions` — lines 66–108

#### Signature

```csharp
public static object GetSubmissions(int cwid)
```

#### What it is

Reads/loads data related to **Submissions** and returns it for display or further use.

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.
2. Open a connection to the LocalDB / SQL Server database.
3. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `int` | CourseWork ID (assignment) (CourseWorks.CWID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous). |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `list` | `var` | In-memory collection being built for JSON return.  Newly constructed object. |
| `rdr` | `var` | Holds “rdr” for this scope. |
| `studentUid` | `int` | Users.UID of the student. |
| `studentName` | `string` | Student display name. |
| `text` | `string` | Holds “text” for this scope. (text) |
| `time` | `string` | Date/time value. (text) |
| `score` | `int` | Points earned or max points depending on context. |
| `review` | `string` | Holds “review” for this scope. (text) |

#### Code

```csharp
  66 |         public static object GetSubmissions(int cwid)
  67 |         {
  68 |             try
  69 |             {
  70 |                 int uid = AuthGate.RequireLecturer();
  71 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  72 | 
  73 |                 using (var conn = new SqlConnection(ConnString))
  74 |                 using (var cmd = conn.CreateCommand())
  75 |                 {
  76 |                     conn.Open();
  77 |                     cmd.CommandText = @"SELECT s.SID, s.UID, ISNULL(u.Name,'') AS StudentName, ISNULL(s.Text,'') AS Text, ISNULL(s.CreatedAt,GETDATE()) AS SubmittedAt,
  78 |                     ISNULL(m.Score, -1) AS Score, ISNULL(m.Review,'') AS Review
  79 |                     FROM CWSubmissions s
  80 |                     LEFT JOIN CWMarkings m ON m.SID = s.SID
  81 |                     LEFT JOIN Users u ON u.UID = s.UID
  82 |                     WHERE s.CWID = @cwid
  83 |                     ORDER BY s.CreatedAt DESC";
  84 |                     cmd.Parameters.AddWithValue("@cwid", cwid);
  85 |                     var list = new List<object>();
  86 |                     using (var rdr = cmd.ExecuteReader())
  87 |                     {
  88 |                         while (rdr.Read())
  89 |                         {
  90 |                             int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);
  91 |                             int studentUid = rdr.IsDBNull(1) ? 0 : rdr.GetInt32(1);
  92 |                             string studentName = rdr.IsDBNull(2) ? "" : rdr.GetString(2);
  93 |                             string text = rdr.IsDBNull(3) ? "" : rdr.GetString(3);
  94 |                             string time = rdr.IsDBNull(4) ? "" : Convert.ToDateTime(rdr.GetValue(4)).ToString("g");
  95 |                             int score = rdr.IsDBNull(5) ? -1 : Convert.ToInt32(rdr.GetValue(5));
  96 |                             string review = rdr.IsDBNull(6) ? "" : rdr.GetString(6);
  97 |                             list.Add(new { sid = sid, studentUid = studentUid, studentName = studentName, text = text, time = time, score = score, review = review });
  98 |                         }
  99 |                     }
 100 |                     return new { success = true, submissions = list };
 101 |                 }
 102 |             }
 103 |             catch (Exception ex)
 104 |             {
 105 |                 try { Logger.Error(ex, "ManageSubmissions.GetSubmissions"); } catch { }
 106 |                 return new { success = false, message = "Request failed." };
 107 |             }
 108 |         }
```

---

### `GradeSubmission` — lines 112–128

#### Signature

```csharp
public static object GradeSubmission(int sid, int score, string review)
```

#### What it is

Function `GradeSubmission` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.
2. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sid` | `int` | Submission ID (CWSubmissions.SID). |
| `score` | `int` | Points earned or max points depending on context. |
| `review` | `string` | Holds “review” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous). |
| `res` | `var` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |

#### Code

```csharp
 112 |         public static object GradeSubmission(int sid, int score, string review)
 113 |         {
 114 |             try
 115 |             {
 116 |                 int uid = AuthGate.RequireLecturer();
 117 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 118 | 
 119 |                 // Delegate to DashboardService which enforces ownership
 120 |                 var res = DashboardService.SaveGrade(uid, sid, score, review);
 121 |                 return res;
 122 |             }
 123 |             catch (Exception ex)
 124 |             {
 125 |                 try { Logger.Error(ex, "ManageSubmissions.GradeSubmission"); } catch { }
 126 |                 return new { success = false, message = "Request failed." };
 127 |             }
 128 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Collections.Generic;
   3 | using System.Configuration;
   4 | using System.Data.SqlClient;
   5 | using System.Web.Script.Services;
   6 | using System.Web.Services;
   7 | using System.Web.UI;
   8 | using WebAppAssignment.Shared.DebugLog;
   9 | using WebAppAssignment.Pages.Lecturer.Services;
  10 | using WebAppAssignment.Data.Security;
  11 | 
  12 | namespace WebAppAssignment.Pages.Lecturer
  13 | {
  14 |     public partial class ManageSubmissions : Page
  15 |     {
  16 |         private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"]?.ConnectionString ?? string.Empty;
  17 | 
  18 |         protected void Page_Load(object sender, EventArgs e)
  19 |         {
  20 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  21 |                 return;
  22 | 
  23 |         }
  24 | 
  25 |         [WebMethod]
  26 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  27 |         public static object GetAssignments()
  28 |         {
  29 |             try
  30 |             {
  31 |                 int uid = AuthGate.RequireLecturer();
  32 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  33 | 
  34 |                 using (var conn = new SqlConnection(ConnString))
  35 |                 using (var cmd = conn.CreateCommand())
  36 |                 {
  37 |                     conn.Open();
  38 |                     // detect owner column
  39 |                     var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
  40 |                     using (var cc = conn.CreateCommand()) { cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'"; using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); } }
  41 |                     string ownerCol = cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));
  42 | 
  43 |                     cmd.CommandText = $@"SELECT cw.CWID, cw.Title, c.Name AS CourseName FROM CourseWorks cw
  44 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  45 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  46 |                     JOIN Courses c ON ch.CID = c.CID
  47 |                     WHERE c.[{ownerCol}] = @uid ORDER BY cw.CreatedAt DESC";
  48 |                     cmd.Parameters.AddWithValue("@uid", uid);
  49 |                     var list = new List<object>();
  50 |                     using (var rdr = cmd.ExecuteReader())
  51 |                     {
  52 |                         while (rdr.Read()) list.Add(new { cwid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0), title = rdr.IsDBNull(1) ? "" : rdr.GetString(1), course = rdr.IsDBNull(2) ? "" : rdr.GetString(2) });
  53 |                     }
  54 |                     return new { success = true, assignments = list };
  55 |                 }
  56 |             }
  57 |             catch (Exception ex)
  58 |             {
  59 |                 try { Logger.Error(ex, "ManageSubmissions.GetAssignments"); } catch { }
  60 |                 return new { success = false, message = "Request failed." };
  61 |             }
  62 |         }
  63 | 
  64 |         [WebMethod]
  65 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  66 |         public static object GetSubmissions(int cwid)
  67 |         {
  68 |             try
  69 |             {
  70 |                 int uid = AuthGate.RequireLecturer();
  71 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  72 | 
  73 |                 using (var conn = new SqlConnection(ConnString))
  74 |                 using (var cmd = conn.CreateCommand())
  75 |                 {
  76 |                     conn.Open();
  77 |                     cmd.CommandText = @"SELECT s.SID, s.UID, ISNULL(u.Name,'') AS StudentName, ISNULL(s.Text,'') AS Text, ISNULL(s.CreatedAt,GETDATE()) AS SubmittedAt,
  78 |                     ISNULL(m.Score, -1) AS Score, ISNULL(m.Review,'') AS Review
  79 |                     FROM CWSubmissions s
  80 |                     LEFT JOIN CWMarkings m ON m.SID = s.SID
  81 |                     LEFT JOIN Users u ON u.UID = s.UID
  82 |                     WHERE s.CWID = @cwid
  83 |                     ORDER BY s.CreatedAt DESC";
  84 |                     cmd.Parameters.AddWithValue("@cwid", cwid);
  85 |                     var list = new List<object>();
  86 |                     using (var rdr = cmd.ExecuteReader())
  87 |                     {
  88 |                         while (rdr.Read())
  89 |                         {
  90 |                             int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);
  91 |                             int studentUid = rdr.IsDBNull(1) ? 0 : rdr.GetInt32(1);
  92 |                             string studentName = rdr.IsDBNull(2) ? "" : rdr.GetString(2);
  93 |                             string text = rdr.IsDBNull(3) ? "" : rdr.GetString(3);
  94 |                             string time = rdr.IsDBNull(4) ? "" : Convert.ToDateTime(rdr.GetValue(4)).ToString("g");
  95 |                             int score = rdr.IsDBNull(5) ? -1 : Convert.ToInt32(rdr.GetValue(5));
  96 |                             string review = rdr.IsDBNull(6) ? "" : rdr.GetString(6);
  97 |                             list.Add(new { sid = sid, studentUid = studentUid, studentName = studentName, text = text, time = time, score = score, review = review });
  98 |                         }
  99 |                     }
 100 |                     return new { success = true, submissions = list };
 101 |                 }
 102 |             }
 103 |             catch (Exception ex)
 104 |             {
 105 |                 try { Logger.Error(ex, "ManageSubmissions.GetSubmissions"); } catch { }
 106 |                 return new { success = false, message = "Request failed." };
 107 |             }
 108 |         }
 109 | 
 110 |         [WebMethod]
 111 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 112 |         public static object GradeSubmission(int sid, int score, string review)
 113 |         {
 114 |             try
 115 |             {
 116 |                 int uid = AuthGate.RequireLecturer();
 117 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 118 | 
 119 |                 // Delegate to DashboardService which enforces ownership
 120 |                 var res = DashboardService.SaveGrade(uid, sid, score, review);
 121 |                 return res;
 122 |             }
 123 |             catch (Exception ex)
 124 |             {
 125 |                 try { Logger.Error(ex, "ManageSubmissions.GradeSubmission"); } catch { }
 126 |                 return new { success = false, message = "Request failed." };
 127 |             }
 128 |         }
 129 |     }
 130 | }
```
