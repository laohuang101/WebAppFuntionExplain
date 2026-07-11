# ManageSubmissions.aspx.cs
**Source:** `Pages/Lecturer/ManageSubmissions.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 130
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 16:** `ConnString` — type `string`
- **Line 31:** `uid` — type `int`
- **Line 39:** `cols` — type `var`
- **Line 41:** `ownerCol` — type `string`
- **Line 49:** `list` — type `var`
- **Line 70:** `uid` — type `int`
- **Line 85:** `list` — type `var`
- **Line 90:** `sid` — type `int`
- **Line 91:** `studentUid` — type `int`
- **Line 92:** `studentName` — type `string`
- **Line 93:** `text` — type `string`
- **Line 94:** `time` — type `string`
- **Line 95:** `score` — type `int`
- **Line 96:** `review` — type `string`
- **Line 116:** `uid` — type `int`
- **Line 120:** `res` — type `var`
- **Line 121:** `res` — type `return`

## Functions / methods (4 found)

### `Page_Load` — lines 17–23

```
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`

#### Line-by-line (this function)

`  17`  ``
`  18`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  19`  `        {`
`  20`  `            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  21`  `                return;`
`  22`  ``
`  23`  `        }`

---

### `GetAssignments` — lines 27–62

```
public static object GetAssignments()
```

#### Explanation

- **Purpose:** Implements `GetAssignments`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`, `conn`, `cmd`, `cols`, `cc`, `r`, `ownerCol`, `list`, `rdr`

#### Line-by-line (this function)

`  27`  `        public static object GetAssignments()`
`  28`  `        {`
`  29`  `            try`
  - → Error handling block.
`  30`  `            {`
`  31`  `                int uid = AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
`  32`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  33`  ``
`  34`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  35`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
`  36`  `                {`
`  37`  `                    conn.Open();`
`  38`  `                    // detect owner column`
`  39`  `                    var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);`
`  40`  `                    using (var cc = conn.CreateCommand()) { cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'"; using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); } }`
  - → Import namespace/types.
`  41`  `                    string ownerCol = cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));`
  - → Owner lecturer foreign key.
`  42`  ``
`  43`  `                    cmd.CommandText = $@"SELECT cw.CWID, cw.Title, c.Name AS CourseName FROM CourseWorks cw`
`  44`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  45`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  46`  `                    JOIN Courses c ON ch.CID = c.CID`
`  47`  `                    WHERE c.[{ownerCol}] = @uid ORDER BY cw.CreatedAt DESC";`
`  48`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  49`  `                    var list = new List<object>();`
`  50`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
`  51`  `                    {`
`  52`  `                        while (rdr.Read()) list.Add(new { cwid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0), title = rdr.IsDBNull(1) ? "" : rdr.GetString(1), course = rdr.IsDBNull(2) ? "" : rdr.GetString(2) });`
`  53`  `                    }`
`  54`  `                    return new { success = true, assignments = list };`
`  55`  `                }`
`  56`  `            }`
`  57`  `            catch (Exception ex)`
  - → Handle/log exception.
`  58`  `            {`
`  59`  `                try { Logger.Error(ex, "ManageSubmissions.GetAssignments"); } catch { }`
  - → Error handling block.
`  60`  `                return new { success = false, message = "Request failed." };`
`  61`  `            }`
`  62`  `        }`

---

### `GetSubmissions` — lines 66–108

```
public static object GetSubmissions(int cwid)
```

#### Explanation

- **Purpose:** Implements `GetSubmissions`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Parameters:** `int cwid`
- **Local variables:** `uid`, `conn`, `cmd`, `list`, `rdr`, `sid`, `studentUid`, `studentName`, `text`, `time`, `score`, `review`

#### Line-by-line (this function)

`  66`  `        public static object GetSubmissions(int cwid)`
`  67`  `        {`
`  68`  `            try`
  - → Error handling block.
`  69`  `            {`
`  70`  `                int uid = AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
`  71`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  72`  ``
`  73`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  74`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
`  75`  `                {`
`  76`  `                    conn.Open();`
`  77`  `                    cmd.CommandText = @"SELECT s.SID, s.UID, ISNULL(u.Name,'') AS StudentName, ISNULL(s.Text,'') AS Text, ISNULL(s.CreatedAt,GETDATE()) AS SubmittedAt,`
`  78`  `                    ISNULL(m.Score, -1) AS Score, ISNULL(m.Review,'') AS Review`
`  79`  `                    FROM CWSubmissions s`
`  80`  `                    LEFT JOIN CWMarkings m ON m.SID = s.SID`
`  81`  `                    LEFT JOIN Users u ON u.UID = s.UID`
`  82`  `                    WHERE s.CWID = @cwid`
`  83`  `                    ORDER BY s.CreatedAt DESC";`
`  84`  `                    cmd.Parameters.AddWithValue("@cwid", cwid);`
`  85`  `                    var list = new List<object>();`
`  86`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
`  87`  `                    {`
`  88`  `                        while (rdr.Read())`
`  89`  `                        {`
`  90`  `                            int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);`
`  91`  `                            int studentUid = rdr.IsDBNull(1) ? 0 : rdr.GetInt32(1);`
`  92`  `                            string studentName = rdr.IsDBNull(2) ? "" : rdr.GetString(2);`
`  93`  `                            string text = rdr.IsDBNull(3) ? "" : rdr.GetString(3);`
`  94`  `                            string time = rdr.IsDBNull(4) ? "" : Convert.ToDateTime(rdr.GetValue(4)).ToString("g");`
`  95`  `                            int score = rdr.IsDBNull(5) ? -1 : Convert.ToInt32(rdr.GetValue(5));`
`  96`  `                            string review = rdr.IsDBNull(6) ? "" : rdr.GetString(6);`
`  97`  `                            list.Add(new { sid = sid, studentUid = studentUid, studentName = studentName, text = text, time = time, score = score, review = review });`
`  98`  `                        }`
`  99`  `                    }`
` 100`  `                    return new { success = true, submissions = list };`
` 101`  `                }`
` 102`  `            }`
` 103`  `            catch (Exception ex)`
  - → Handle/log exception.
` 104`  `            {`
` 105`  `                try { Logger.Error(ex, "ManageSubmissions.GetSubmissions"); } catch { }`
  - → Error handling block.
` 106`  `                return new { success = false, message = "Request failed." };`
` 107`  `            }`
` 108`  `        }`

---

### `GradeSubmission` — lines 112–128

```
public static object GradeSubmission(int sid, int score, string review)
```

#### Explanation

- **Purpose:** Implements `GradeSubmission`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `int sid, int score, string review`
- **Local variables:** `uid`, `res`

#### Line-by-line (this function)

` 112`  `        public static object GradeSubmission(int sid, int score, string review)`
` 113`  `        {`
` 114`  `            try`
  - → Error handling block.
` 115`  `            {`
` 116`  `                int uid = AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
` 117`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
` 118`  ``
` 119`  `                // Delegate to DashboardService which enforces ownership`
` 120`  `                var res = DashboardService.SaveGrade(uid, sid, score, review);`
` 121`  `                return res;`
` 122`  `            }`
` 123`  `            catch (Exception ex)`
  - → Handle/log exception.
` 124`  `            {`
` 125`  `                try { Logger.Error(ex, "ManageSubmissions.GradeSubmission"); } catch { }`
  - → Error handling block.
` 126`  `                return new { success = false, message = "Request failed." };`
` 127`  `            }`
` 128`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Collections.Generic;`
  - → Import namespace/types.
`   3`  `using System.Configuration;`
  - → Import namespace/types.
`   4`  `using System.Data.SqlClient;`
  - → Import namespace/types.
`   5`  `using System.Web.Script.Services;`
  - → Import namespace/types.
`   6`  `using System.Web.Services;`
  - → Import namespace/types.
`   7`  `using System.Web.UI;`
  - → Import namespace/types.
`   8`  `using WebAppAssignment.Shared.DebugLog;`
  - → Import namespace/types.
`   9`  `using WebAppAssignment.Pages.Lecturer.Services;`
  - → Import namespace/types.
`  10`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`  11`  ``
`  12`  `namespace WebAppAssignment.Pages.Lecturer`
  - → C# namespace grouping.
`  13`  `{`
`  14`  `    public partial class ManageSubmissions : Page`
`  15`  `    {`
`  16`  `        private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"]?.ConnectionString ?? string.Empty;`
`  17`  ``
`  18`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  19`  `        {`
`  20`  `            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  21`  `                return;`
`  22`  ``
`  23`  `        }`
`  24`  ``
`  25`  `        [WebMethod]`
  - → Expose method to AJAX JSON calls.
`  26`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  27`  `        public static object GetAssignments()`
`  28`  `        {`
`  29`  `            try`
  - → Error handling block.
`  30`  `            {`
`  31`  `                int uid = AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
`  32`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  33`  ``
`  34`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  35`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
`  36`  `                {`
`  37`  `                    conn.Open();`
`  38`  `                    // detect owner column`
`  39`  `                    var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);`
`  40`  `                    using (var cc = conn.CreateCommand()) { cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'"; using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); } }`
  - → Import namespace/types.
`  41`  `                    string ownerCol = cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));`
  - → Owner lecturer foreign key.
`  42`  ``
`  43`  `                    cmd.CommandText = $@"SELECT cw.CWID, cw.Title, c.Name AS CourseName FROM CourseWorks cw`
`  44`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  45`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  46`  `                    JOIN Courses c ON ch.CID = c.CID`
`  47`  `                    WHERE c.[{ownerCol}] = @uid ORDER BY cw.CreatedAt DESC";`
`  48`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  49`  `                    var list = new List<object>();`
`  50`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
`  51`  `                    {`
`  52`  `                        while (rdr.Read()) list.Add(new { cwid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0), title = rdr.IsDBNull(1) ? "" : rdr.GetString(1), course = rdr.IsDBNull(2) ? "" : rdr.GetString(2) });`
`  53`  `                    }`
`  54`  `                    return new { success = true, assignments = list };`
`  55`  `                }`
`  56`  `            }`
`  57`  `            catch (Exception ex)`
  - → Handle/log exception.
`  58`  `            {`
`  59`  `                try { Logger.Error(ex, "ManageSubmissions.GetAssignments"); } catch { }`
  - → Error handling block.
`  60`  `                return new { success = false, message = "Request failed." };`
`  61`  `            }`
`  62`  `        }`
`  63`  ``
`  64`  `        [WebMethod]`
  - → Expose method to AJAX JSON calls.
`  65`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  66`  `        public static object GetSubmissions(int cwid)`
`  67`  `        {`
`  68`  `            try`
  - → Error handling block.
`  69`  `            {`
`  70`  `                int uid = AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
`  71`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  72`  ``
`  73`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  74`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
`  75`  `                {`
`  76`  `                    conn.Open();`
`  77`  `                    cmd.CommandText = @"SELECT s.SID, s.UID, ISNULL(u.Name,'') AS StudentName, ISNULL(s.Text,'') AS Text, ISNULL(s.CreatedAt,GETDATE()) AS SubmittedAt,`
`  78`  `                    ISNULL(m.Score, -1) AS Score, ISNULL(m.Review,'') AS Review`
`  79`  `                    FROM CWSubmissions s`
`  80`  `                    LEFT JOIN CWMarkings m ON m.SID = s.SID`
`  81`  `                    LEFT JOIN Users u ON u.UID = s.UID`
`  82`  `                    WHERE s.CWID = @cwid`
`  83`  `                    ORDER BY s.CreatedAt DESC";`
`  84`  `                    cmd.Parameters.AddWithValue("@cwid", cwid);`
`  85`  `                    var list = new List<object>();`
`  86`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
`  87`  `                    {`
`  88`  `                        while (rdr.Read())`
`  89`  `                        {`
`  90`  `                            int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);`
`  91`  `                            int studentUid = rdr.IsDBNull(1) ? 0 : rdr.GetInt32(1);`
`  92`  `                            string studentName = rdr.IsDBNull(2) ? "" : rdr.GetString(2);`
`  93`  `                            string text = rdr.IsDBNull(3) ? "" : rdr.GetString(3);`
`  94`  `                            string time = rdr.IsDBNull(4) ? "" : Convert.ToDateTime(rdr.GetValue(4)).ToString("g");`
`  95`  `                            int score = rdr.IsDBNull(5) ? -1 : Convert.ToInt32(rdr.GetValue(5));`
`  96`  `                            string review = rdr.IsDBNull(6) ? "" : rdr.GetString(6);`
`  97`  `                            list.Add(new { sid = sid, studentUid = studentUid, studentName = studentName, text = text, time = time, score = score, review = review });`
`  98`  `                        }`
`  99`  `                    }`
` 100`  `                    return new { success = true, submissions = list };`
` 101`  `                }`
` 102`  `            }`
` 103`  `            catch (Exception ex)`
  - → Handle/log exception.
` 104`  `            {`
` 105`  `                try { Logger.Error(ex, "ManageSubmissions.GetSubmissions"); } catch { }`
  - → Error handling block.
` 106`  `                return new { success = false, message = "Request failed." };`
` 107`  `            }`
` 108`  `        }`
` 109`  ``
` 110`  `        [WebMethod]`
  - → Expose method to AJAX JSON calls.
` 111`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
` 112`  `        public static object GradeSubmission(int sid, int score, string review)`
` 113`  `        {`
` 114`  `            try`
  - → Error handling block.
` 115`  `            {`
` 116`  `                int uid = AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
` 117`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
` 118`  ``
` 119`  `                // Delegate to DashboardService which enforces ownership`
` 120`  `                var res = DashboardService.SaveGrade(uid, sid, score, review);`
` 121`  `                return res;`
` 122`  `            }`
` 123`  `            catch (Exception ex)`
  - → Handle/log exception.
` 124`  `            {`
` 125`  `                try { Logger.Error(ex, "ManageSubmissions.GradeSubmission"); } catch { }`
  - → Error handling block.
` 126`  `                return new { success = false, message = "Request failed." };`
` 127`  `            }`
` 128`  `        }`
` 129`  `    }`
` 130`  `}`

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
