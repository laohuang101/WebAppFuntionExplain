# ManageSubmissions.aspx.cs
**Source:** `Pages/Lecturer/ManageSubmissions.aspx.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 130
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 16:** `ConnString` (`string`) — **Holds “Conn String” for this scope. (text)**
- **Line 31:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 39:** `cols` (`var`) — **Often a collection related to cols (plural name).**
- **Line 41:** `ownerCol` (`string`) — **Holds “owner Col” for this scope. (text)**
- **Line 49:** `list` (`var`) — **In-memory collection being built for JSON return.**
- **Line 70:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 85:** `list` (`var`) — **In-memory collection being built for JSON return.**
- **Line 90:** `sid` (`int`) — **Submission ID (CWSubmissions.SID).**
- **Line 91:** `studentUid` (`int`) — **Users.UID of the student.**
- **Line 92:** `studentName` (`string`) — **Student display name.**
- **Line 93:** `text` (`string`) — **Holds “text” for this scope. (text)**
- **Line 94:** `time` (`string`) — **Date/time value. (text)**
- **Line 95:** `score` (`int`) — **Points earned or max points depending on context.**
- **Line 96:** `review` (`string`) — **Holds “review” for this scope. (text)**
- **Line 116:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 120:** `res` (`var`) — **Result object returned from fetch/WebMethod (`data.d` unwrapped).**
- **Line 121:** `res` (`return`) — **Result object returned from fetch/WebMethod (`data.d` unwrapped).**

## Functions / methods (4 found)

### `Page_Load` — lines 17–23

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

```csharp
  17 | 
  18 |         protected void Page_Load(object sender, EventArgs e)
  19 |         {
  20 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  21 |                 return;
  22 | 
  23 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L18:** Page load entry (GET or postback).
- **L20:** Authorization — block wrong role / anonymous.

---

### `GetAssignments` — lines 27–62

```csharp
public static object GetAssignments()
```

#### Explanation

- **Purpose:** Implements `GetAssignments`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.
- `cols` (`var`) — Often a collection related to cols (plural name).  Newly constructed object.
- `cc` (`var`) — Holds “cc” for this scope.
- `r` (`var`) — Usually one database row (DataRow) in query loops.
- `ownerCol` (`string`) — Holds “owner Col” for this scope. (text)
- `list` (`var`) — In-memory collection being built for JSON return.  Newly constructed object.
- `rdr` (`var`) — Holds “rdr” for this scope.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L29:** Error handling block.
- **L31:** Authorization — block wrong role / anonymous.
- **L32:** Authorization — block wrong role / anonymous.
- **L34:** Import namespace/types.
- **L35:** Import namespace/types.
- **L40:** Import namespace/types.
- **L41:** Owner lecturer foreign key.
- **L48:** Parameterized SQL — prevents classic SQL injection.
=======
**Line notes** (what code + variables mean)

- **L29:** Error handling block.
- **L31:** Authorization — block wrong role / anonymous. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- **L32:** Authorization — block wrong role / anonymous.
- **L34:** Import namespace/types.
- **L35:** Import namespace/types.
- **L39:** `cols` means: Often a collection related to cols (plural name).  Newly constructed object.
- **L40:** Import namespace/types.
- **L41:** Owner lecturer foreign key. | `ownerCol` means: Holds “owner Col” for this scope. (text)
- **L48:** Parameterized SQL — prevents classic SQL injection.
- **L49:** `list` means: In-memory collection being built for JSON return.  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L50:** Import namespace/types.
- **L52:** Null-safe read from database values.
- **L57:** Handle/log exception.
- **L59:** Error handling block.

---

### `GetSubmissions` — lines 66–108

```csharp
public static object GetSubmissions(int cwid)
```

#### Explanation

- **Purpose:** Implements `GetSubmissions`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Parameters (what each means):**
- `cwid` (`int`) — CourseWork ID (assignment) (CourseWorks.CWID).
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.
- `list` (`var`) — In-memory collection being built for JSON return.  Newly constructed object.
- `rdr` (`var`) — Holds “rdr” for this scope.
- `studentUid` (`int`) — Users.UID of the student.
- `studentName` (`string`) — Student display name.
- `text` (`string`) — Holds “text” for this scope. (text)
- `time` (`string`) — Date/time value. (text)
- `score` (`int`) — Points earned or max points depending on context.
- `review` (`string`) — Holds “review” for this scope. (text)

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L68:** Error handling block.
- **L70:** Authorization — block wrong role / anonymous.
=======
**Line notes** (what code + variables mean)

- **L68:** Error handling block.
- **L70:** Authorization — block wrong role / anonymous. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
>>>>>>> eb8ce01 (update)
- **L71:** Authorization — block wrong role / anonymous.
- **L73:** Import namespace/types.
- **L74:** Import namespace/types.
- **L80:** Join related tables (courses ↔ chapters ↔ works ↔ users).
- **L81:** Join related tables (courses ↔ chapters ↔ works ↔ users).
- **L84:** Parameterized SQL — prevents classic SQL injection.
<<<<<<< HEAD
- **L86:** Import namespace/types.
- **L90:** Null-safe read from database values.
- **L91:** Null-safe read from database values.
- **L92:** Null-safe read from database values.
- **L93:** Null-safe read from database values.
- **L94:** Null-safe read from database values.
- **L95:** Null-safe read from database values.
- **L96:** Null-safe read from database values.
=======
- **L85:** `list` means: In-memory collection being built for JSON return.  Newly constructed object.
- **L86:** Import namespace/types.
- **L90:** Null-safe read from database values. | `sid` means: Submission ID (CWSubmissions.SID).
- **L91:** Null-safe read from database values. | `studentUid` means: Users.UID of the student.
- **L92:** Null-safe read from database values. | `studentName` means: Student display name.
- **L93:** Null-safe read from database values. | `text` means: Holds “text” for this scope. (text)
- **L94:** Null-safe read from database values. | `time` means: Date/time value. (text)
- **L95:** Null-safe read from database values. | `score` means: Points earned or max points depending on context.
- **L96:** Null-safe read from database values. | `review` means: Holds “review” for this scope. (text)
>>>>>>> eb8ce01 (update)
- **L103:** Handle/log exception.
- **L105:** Error handling block.

---

### `GradeSubmission` — lines 112–128

```csharp
public static object GradeSubmission(int sid, int score, string review)
```

#### Explanation

- **Purpose:** Implements `GradeSubmission`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `sid` (`int`) — Submission ID (CWSubmissions.SID).
- `score` (`int`) — Points earned or max points depending on context.
- `review` (`string`) — Holds “review” for this scope. (text)
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- `res` (`var`) — Result object returned from fetch/WebMethod (`data.d` unwrapped).

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L114:** Error handling block.
- **L116:** Authorization — block wrong role / anonymous.
- **L117:** Authorization — block wrong role / anonymous.
=======
**Line notes** (what code + variables mean)

- **L114:** Error handling block.
- **L116:** Authorization — block wrong role / anonymous. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- **L117:** Authorization — block wrong role / anonymous.
- **L120:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
>>>>>>> eb8ce01 (update)
- **L123:** Handle/log exception.
- **L125:** Error handling block.

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L7:** Import namespace/types.
- **L8:** Import namespace/types.
- **L9:** Import namespace/types.
- **L10:** Import namespace/types.
- **L12:** C# namespace grouping.
- **L18:** Page load entry (GET or postback).
- **L20:** Authorization — block wrong role / anonymous.
- **L25:** Expose method to AJAX JSON calls.
- **L29:** Error handling block.
<<<<<<< HEAD
- **L31:** Authorization — block wrong role / anonymous.
- **L32:** Authorization — block wrong role / anonymous.
- **L34:** Import namespace/types.
- **L35:** Import namespace/types.
- **L40:** Import namespace/types.
- **L41:** Owner lecturer foreign key.
- **L48:** Parameterized SQL — prevents classic SQL injection.
=======
- **L31:** Authorization — block wrong role / anonymous. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- **L32:** Authorization — block wrong role / anonymous.
- **L34:** Import namespace/types.
- **L35:** Import namespace/types.
- **L39:** `cols` means: Often a collection related to cols (plural name).  Newly constructed object.
- **L40:** Import namespace/types.
- **L41:** Owner lecturer foreign key. | `ownerCol` means: Holds “owner Col” for this scope. (text)
- **L48:** Parameterized SQL — prevents classic SQL injection.
- **L49:** `list` means: In-memory collection being built for JSON return.  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L50:** Import namespace/types.
- **L52:** Null-safe read from database values.
- **L57:** Handle/log exception.
- **L59:** Error handling block.
- **L64:** Expose method to AJAX JSON calls.
- **L68:** Error handling block.
<<<<<<< HEAD
- **L70:** Authorization — block wrong role / anonymous.
=======
- **L70:** Authorization — block wrong role / anonymous. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
>>>>>>> eb8ce01 (update)
- **L71:** Authorization — block wrong role / anonymous.
- **L73:** Import namespace/types.
- **L74:** Import namespace/types.
- **L80:** Join related tables (courses ↔ chapters ↔ works ↔ users).
- **L81:** Join related tables (courses ↔ chapters ↔ works ↔ users).
- **L84:** Parameterized SQL — prevents classic SQL injection.
<<<<<<< HEAD
- **L86:** Import namespace/types.
- **L90:** Null-safe read from database values.
- **L91:** Null-safe read from database values.
- **L92:** Null-safe read from database values.
- **L93:** Null-safe read from database values.
- **L94:** Null-safe read from database values.
- **L95:** Null-safe read from database values.
- **L96:** Null-safe read from database values.
=======
- **L85:** `list` means: In-memory collection being built for JSON return.  Newly constructed object.
- **L86:** Import namespace/types.
- **L90:** Null-safe read from database values. | `sid` means: Submission ID (CWSubmissions.SID).
- **L91:** Null-safe read from database values. | `studentUid` means: Users.UID of the student.
- **L92:** Null-safe read from database values. | `studentName` means: Student display name.
- **L93:** Null-safe read from database values. | `text` means: Holds “text” for this scope. (text)
- **L94:** Null-safe read from database values. | `time` means: Date/time value. (text)
- **L95:** Null-safe read from database values. | `score` means: Points earned or max points depending on context.
- **L96:** Null-safe read from database values. | `review` means: Holds “review” for this scope. (text)
>>>>>>> eb8ce01 (update)
- **L103:** Handle/log exception.
- **L105:** Error handling block.
- **L110:** Expose method to AJAX JSON calls.
- **L114:** Error handling block.
<<<<<<< HEAD
- **L116:** Authorization — block wrong role / anonymous.
- **L117:** Authorization — block wrong role / anonymous.
=======
- **L116:** Authorization — block wrong role / anonymous. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- **L117:** Authorization — block wrong role / anonymous.
- **L120:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
>>>>>>> eb8ce01 (update)
- **L123:** Handle/log exception.
- **L125:** Error handling block.

## Source snapshot (raw)

```csharp
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data.SqlClient;
using System.Web.Script.Services;
using System.Web.Services;
using System.Web.UI;
using WebAppAssignment.Shared.DebugLog;
using WebAppAssignment.Pages.Lecturer.Services;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Lecturer
{
    public partial class ManageSubmissions : Page
    {
        private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"]?.ConnectionString ?? string.Empty;

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
                return;

        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetAssignments()
        {
            try
            {
                int uid = AuthGate.RequireLecturer();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();

                using (var conn = new SqlConnection(ConnString))
                using (var cmd = conn.CreateCommand())
                {
                    conn.Open();
                    // detect owner column
                    var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
                    using (var cc = conn.CreateCommand()) { cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'"; using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); } }
                    string ownerCol = cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));

                    cmd.CommandText = $@"SELECT cw.CWID, cw.Title, c.Name AS CourseName FROM CourseWorks cw
                    JOIN SubChapters sc ON cw.SchID = sc.SchID
                    JOIN Chapters ch ON sc.ChID = ch.ChID
                    JOIN Courses c ON ch.CID = c.CID
                    WHERE c.[{ownerCol}] = @uid ORDER BY cw.CreatedAt DESC";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    var list = new List<object>();
                    using (var rdr = cmd.ExecuteReader())
                    {
                        while (rdr.Read()) list.Add(new { cwid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0), title = rdr.IsDBNull(1) ? "" : rdr.GetString(1), course = rdr.IsDBNull(2) ? "" : rdr.GetString(2) });
                    }
                    return new { success = true, assignments = list };
                }
            }
            catch (Exception ex)
            {
                try { Logger.Error(ex, "ManageSubmissions.GetAssignments"); } catch { }
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetSubmissions(int cwid)
        {
            try
            {
                int uid = AuthGate.RequireLecturer();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();

                using (var conn = new SqlConnection(ConnString))
                using (var cmd = conn.CreateCommand())
                {
                    conn.Open();
                    cmd.CommandText = @"SELECT s.SID, s.UID, ISNULL(u.Name,'') AS StudentName, ISNULL(s.Text,'') AS Text, ISNULL(s.CreatedAt,GETDATE()) AS SubmittedAt,
                    ISNULL(m.Score, -1) AS Score, ISNULL(m.Review,'') AS Review
                    FROM CWSubmissions s
                    LEFT JOIN CWMarkings m ON m.SID = s.SID
                    LEFT JOIN Users u ON u.UID = s.UID
                    WHERE s.CWID = @cwid
                    ORDER BY s.CreatedAt DESC";
                    cmd.Parameters.AddWithValue("@cwid", cwid);
                    var list = new List<object>();
                    using (var rdr = cmd.ExecuteReader())
                    {
                        while (rdr.Read())
                        {
                            int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);
                            int studentUid = rdr.IsDBNull(1) ? 0 : rdr.GetInt32(1);
                            string studentName = rdr.IsDBNull(2) ? "" : rdr.GetString(2);
                            string text = rdr.IsDBNull(3) ? "" : rdr.GetString(3);
                            string time = rdr.IsDBNull(4) ? "" : Convert.ToDateTime(rdr.GetValue(4)).ToString("g");
                            int score = rdr.IsDBNull(5) ? -1 : Convert.ToInt32(rdr.GetValue(5));
                            string review = rdr.IsDBNull(6) ? "" : rdr.GetString(6);
                            list.Add(new { sid = sid, studentUid = studentUid, studentName = studentName, text = text, time = time, score = score, review = review });
                        }
                    }
                    return new { success = true, submissions = list };
                }
            }
            catch (Exception ex)
            {
                try { Logger.Error(ex, "ManageSubmissions.GetSubmissions"); } catch { }
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GradeSubmission(int sid, int score, string review)
        {
            try
            {
                int uid = AuthGate.RequireLecturer();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();

                // Delegate to DashboardService which enforces ownership
                var res = DashboardService.SaveGrade(uid, sid, score, review);
                return res;
            }
            catch (Exception ex)
            {
                try { Logger.Error(ex, "ManageSubmissions.GradeSubmission"); } catch { }
                return new { success = false, message = "Request failed." };
            }
        }
    }
}

```
