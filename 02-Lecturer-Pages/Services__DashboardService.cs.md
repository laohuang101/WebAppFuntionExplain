# DashboardService.cs
**Source:** `Pages/Lecturer/Services/DashboardService.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 256
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 13:** `ConnString` — type `string`
- **Line 17:** `cols` — type `var`
- **Line 36:** `ownerCol` — type `string`
- **Line 41:** `activeCourses` — type `int`
- **Line 49:** `totalStudents` — type `int`
- **Line 61:** `pending` — type `int`
- **Line 73:** `avgObj` — type `var`
- **Line 74:** `avg` — type `double`
- **Line 92:** `submissions` — type `var`
- **Line 97:** `sid` — type `int`
- **Line 98:** `studentName` — type `string`
- **Line 99:** `assign` — type `string`
- **Line 100:** `courseName` — type `string`
- **Line 101:** `answer` — type `string`
- **Line 102:** `timeText` — type `string`
- **Line 103:** `isGraded` — type `bool`
- **Line 104:** `maxScore` — type `int`
- **Line 105:** `initials` — type `var`
- **Line 108:** `parts` — type `var`
- **Line 133:** `gradeDist` — type `var`
- **Line 151:** `enrollTrend` — type `var`
- **Line 180:** `ownerCol` — type `string`
- **Line 191:** `cnt` — type `int`
- **Line 198:** `exist` — type `int`
- **Line 237:** `ownerCol` — type `string`
- **Line 246:** `true` — type `return`
- **Line 252:** `false` — type `return`

## Functions / methods (4 found)

### `DetectOwnerColumn` — lines 14–24

```
private static string DetectOwnerColumn(SqlConnection conn)
```

#### Explanation

- **Purpose:** Implements `DetectOwnerColumn`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Parameters:** `SqlConnection conn`
- **Local variables:** `cols`, `cc`, `r`

#### Line-by-line (this function)

`  14`  ``
`  15`  `        private static string DetectOwnerColumn(SqlConnection conn)`
  - → Database access (pure SQL).
`  16`  `        {`
`  17`  `            var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);`
`  18`  `            using (var cc = conn.CreateCommand())`
  - → Import namespace/types.
`  19`  `            {`
`  20`  `                cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'";`
`  21`  `                using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); }`
  - → Import namespace/types.
`  22`  `            }`
`  23`  `            return cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));`
  - → Owner lecturer foreign key.
`  24`  `        }`

---

### `GetDashboardData` — lines 25–168

```
public static object GetDashboardData(int uid)
```

#### Explanation

- **Purpose:** Implements `GetDashboardData`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters:** `int uid`
- **Local variables:** `conn`, `cmd`, `ownerCol`, `activeCourses`, `totalStudents`, `pending`, `avgObj`, `hasGrades`, `submissions`, `rdr`, `sid`, `studentName`, `assign`, `courseName`, `answer`, `timeText`, `isGraded`, `maxScore`, `initials`, `parts`, `gradeDist`, `enrollTrend`

#### Line-by-line (this function)

`  25`  ``
`  26`  `        public static object GetDashboardData(int uid)`
`  27`  `        {`
`  28`  `            try`
  - → Error handling block.
`  29`  `            {`
`  30`  `                if (uid == 0) return new { notAuthenticated = true };`
`  31`  ``
`  32`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  33`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
`  34`  `                {`
`  35`  `                    conn.Open();`
`  36`  `                    string ownerCol = DetectOwnerColumn(conn);`
`  37`  ``
`  38`  `                    // Active courses`
`  39`  `                    cmd.CommandText = $"SELECT COUNT(1) FROM Courses WHERE [{ownerCol}] = @uid";`
`  40`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  41`  `                    int activeCourses = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
`  42`  `                    cmd.Parameters.Clear();`
`  43`  ``
`  44`  `                    // Total distinct students`
`  45`  `                    cmd.CommandText = $@"SELECT COUNT(DISTINCT e.UID) FROM Enrollments e`
`  46`  `                    JOIN Courses c ON e.CID = c.CID`
`  47`  `                    WHERE c.[{ownerCol}] = @uid";`
`  48`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  49`  `                    int totalStudents = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
`  50`  `                    cmd.Parameters.Clear();`
`  51`  ``
`  52`  `                    // Pending grading`
`  53`  `                    cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s`
`  54`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
`  55`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  56`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  57`  `                    JOIN Courses c ON ch.CID = c.CID`
`  58`  `                    LEFT JOIN CWMarkings m ON m.SID = s.SID`
`  59`  `                    WHERE c.[{ownerCol}] = @uid AND m.SID IS NULL";`
`  60`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  61`  `                    int pending = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
`  62`  `                    cmd.Parameters.Clear();`
`  63`  ``
`  64`  `                    // Average grade`
`  65`  `                    cmd.CommandText = $@"SELECT AVG(CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0) * 100.0) FROM CWMarkings m`
`  66`  `                    JOIN CWSubmissions s ON m.SID = s.SID`
`  67`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
`  68`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  69`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  70`  `                    JOIN Courses c ON ch.CID = c.CID`
`  71`  `                    WHERE c.[{ownerCol}] = @uid";`
`  72`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  73`  `                    var avgObj = cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`  74`  `                    double avg = 0; bool hasGrades = false;`
`  75`  `                    if (avgObj != null && avgObj != DBNull.Value) { avg = Convert.ToDouble(avgObj); hasGrades = true; }`
`  76`  `                    cmd.Parameters.Clear();`
`  77`  ``
`  78`  `                    // Recent submissions (top 8)`
`  79`  `                    cmd.CommandText = $@"SELECT TOP 8 s.SID, ISNULL(u.Name,'') AS StudentName, ISNULL(cw.Title,'') AS AssignmentTitle, ISNULL(c.Name,'') AS CourseName,`
`  80`  `                    ISNULL(s.Text, ISNULL(s.Content, '')) AS StudentAnswer, ISNULL(s.CreatedAt, GETDATE()) AS SubmittedAt,`
`  81`  `                    CASE WHEN m.SID IS NULL THEN 0 ELSE 1 END AS IsGraded, ISNULL(cw.MaxScore,0) AS MaxScore`
`  82`  `                    FROM CWSubmissions s`
`  83`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
`  84`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  85`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  86`  `                    JOIN Courses c ON ch.CID = c.CID`
`  87`  `                    LEFT JOIN CWMarkings m ON m.SID = s.SID`
`  88`  `                    LEFT JOIN Users u ON u.UID = s.UID`
`  89`  `                    WHERE c.[{ownerCol}] = @uid`
`  90`  `                    ORDER BY ISNULL(s.CreatedAt, GETDATE()) DESC";`
`  91`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  92`  `                    var submissions = new List<object>();`
`  93`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
`  94`  `                    {`
`  95`  `                        while (rdr.Read())`
`  96`  `                        {`
`  97`  `                            int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);`
`  98`  `                            string studentName = rdr.IsDBNull(1) ? "" : rdr.GetString(1);`
`  99`  `                            string assign = rdr.IsDBNull(2) ? "" : rdr.GetString(2);`
` 100`  `                            string courseName = rdr.IsDBNull(3) ? "" : rdr.GetString(3);`
` 101`  `                            string answer = rdr.IsDBNull(4) ? "" : rdr.GetString(4);`
` 102`  `                            string timeText = rdr.IsDBNull(5) ? "" : Convert.ToDateTime(rdr.GetValue(5)).ToString("g");`
` 103`  `                            bool isGraded = rdr.IsDBNull(6) ? false : rdr.GetInt32(6) != 0;`
` 104`  `                            int maxScore = rdr.IsDBNull(7) ? 0 : Convert.ToInt32(rdr.GetValue(7));`
` 105`  `                            var initials = "";`
` 106`  `                            if (!string.IsNullOrEmpty(studentName))`
` 107`  `                            {`
` 108`  `                                var parts = studentName.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);`
` 109`  `                                if (parts.Length > 1) initials = (parts[0][0].ToString() + parts[parts.Length - 1][0].ToString()).ToUpper(); else initials = parts[0][0].ToString().ToUpper();`
` 110`  `                            }`
` 111`  `                            submissions.Add(new { sid = sid, studentName = studentName, initials = initials, assignmentTitle = assign, courseName = courseName, studentAnswer = answer, timeText = timeText, isGraded = isGraded, maxScore = maxScore });`
` 112`  `                        }`
` 113`  `                    }`
` 114`  ``
` 115`  `                    // Grade distribution (A/B/C/D/F) based on percentage of MaxScore`
` 116`  `                    cmd.Parameters.Clear();`
` 117`  `                    cmd.CommandText = $@"SELECT GradeLabel, COUNT(1) AS Cnt FROM (`
` 118`  `                    SELECT CASE`
` 119`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.85 THEN 'A'`
` 120`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.70 THEN 'B'`
` 121`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.60 THEN 'C'`
` 122`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.50 THEN 'D'`
` 123`  `                    ELSE 'F' END AS GradeLabel`
` 124`  `                    FROM CWMarkings m`
` 125`  `                    JOIN CWSubmissions s ON m.SID = s.SID`
` 126`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
` 127`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
` 128`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
` 129`  `                    JOIN Courses c ON ch.CID = c.CID`
` 130`  `                    WHERE c.[{ownerCol}] = @uid`
` 131`  `                    ) t GROUP BY GradeLabel";`
` 132`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 133`  `                    var gradeDist = new List<object>();`
` 134`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
` 135`  `                    {`
` 136`  `                        while (rdr.Read())`
` 137`  `                        {`
` 138`  `                            gradeDist.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });`
` 139`  `                        }`
` 140`  `                    }`
` 141`  `                    cmd.Parameters.Clear();`
` 142`  ``
` 143`  `                    // Enrollment trends: count per month for last 6 months`
` 144`  `                    cmd.CommandText = $@"SELECT FORMAT(e.CreatedAt,'yyyy-MM') AS Mon, COUNT(1) AS Cnt`
` 145`  `                    FROM Enrollments e`
` 146`  `                    JOIN Courses c ON e.CID = c.CID`
` 147`  `                    WHERE c.[{ownerCol}] = @uid AND e.CreatedAt >= DATEADD(month, -6, GETDATE())`
` 148`  `                    GROUP BY FORMAT(e.CreatedAt,'yyyy-MM')`
` 149`  `                    ORDER BY Mon ASC";`
` 150`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 151`  `                    var enrollTrend = new List<object>();`
` 152`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
` 153`  `                    {`
` 154`  `                        while (rdr.Read())`
` 155`  `                        {`
` 156`  `                            enrollTrend.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });`
` 157`  `                        }`
` 158`  `                    }`
` 159`  ``
` 160`  `                    return new { success = true, totalStudents = totalStudents, activeCourses = activeCourses, pendingGrading = pending, averageGrade = Math.Round(avg, 0), hasGrades = hasGrades, submissions = submissions, gradeDistribution = gradeDist, enrollmentTrends = enrollTrend };`
` 161`  `                }`
` 162`  `            }`
` 163`  `            catch (Exception ex)`
  - → Handle/log exception.
` 164`  `            {`
` 165`  `                try { Logger.Error(ex, "DashboardService.GetDashboardData"); } catch { }`
  - → Error handling block.
` 166`  `                return new { success = false, message = ex.Message };`
` 167`  `            }`
` 168`  `        }`

---

### `SaveGrade` — lines 169–226

```
public static object SaveGrade(int uid, int sid, int score, string review)
```

#### Explanation

- **Purpose:** Implements `SaveGrade`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Persist changes.
- **Parameters:** `int uid, int sid, int score, string review`
- **Local variables:** `conn`, `cmd`, `ownerCol`, `cnt`, `exist`

#### Line-by-line (this function)

` 169`  ``
` 170`  `        public static object SaveGrade(int uid, int sid, int score, string review)`
` 171`  `        {`
` 172`  `            try`
  - → Error handling block.
` 173`  `            {`
` 174`  `                if (uid == 0) return new { notAuthenticated = true };`
` 175`  ``
` 176`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
` 177`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
` 178`  `                {`
` 179`  `                    conn.Open();`
` 180`  `                    string ownerCol = DetectOwnerColumn(conn);`
` 181`  ``
` 182`  `                    // verify submission belongs to this lecturer's course`
` 183`  `                    cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s`
` 184`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
` 185`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
` 186`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
` 187`  `                    JOIN Courses c ON ch.CID = c.CID`
` 188`  `                    WHERE s.SID = @sid AND c.[{ownerCol}] = @uid";`
` 189`  `                    cmd.Parameters.AddWithValue("@sid", sid);`
` 190`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 191`  `                    int cnt = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
` 192`  `                    cmd.Parameters.Clear();`
` 193`  `                    if (cnt == 0) return new { success = false, message = "Unauthorized or submission not found" };`
` 194`  ``
` 195`  `                    // upsert marking`
` 196`  `                    cmd.CommandText = "SELECT COUNT(1) FROM CWMarkings WHERE SID = @sid";`
` 197`  `                    cmd.Parameters.AddWithValue("@sid", sid);`
` 198`  `                    int exist = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
` 199`  `                    cmd.Parameters.Clear();`
` 200`  ``
` 201`  `                    if (exist > 0)`
` 202`  `                    {`
` 203`  `                        cmd.CommandText = "UPDATE CWMarkings SET Score = @score, Review = @review, Timestamp = GETDATE() WHERE SID = @sid";`
` 204`  `                        cmd.Parameters.AddWithValue("@score", score);`
` 205`  `                        cmd.Parameters.AddWithValue("@review", review ?? string.Empty);`
` 206`  `                        cmd.Parameters.AddWithValue("@sid", sid);`
` 207`  `                        cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 208`  `                    }`
` 209`  `                    else`
` 210`  `                    {`
` 211`  `                        cmd.CommandText = "INSERT INTO CWMarkings (SID, Score, Review, Timestamp) VALUES (@sid, @score, @review, GETDATE())";`
` 212`  `                        cmd.Parameters.AddWithValue("@sid", sid);`
` 213`  `                        cmd.Parameters.AddWithValue("@score", score);`
` 214`  `                        cmd.Parameters.AddWithValue("@review", review ?? string.Empty);`
` 215`  `                        cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 216`  `                    }`
` 217`  ``
` 218`  `                    return new { success = true };`
` 219`  `                }`
` 220`  `            }`
` 221`  `            catch (Exception ex)`
  - → Handle/log exception.
` 222`  `            {`
` 223`  `                try { Logger.Error(ex, "DashboardService.SaveGrade"); } catch { }`
  - → Error handling block.
` 224`  `                return new { success = false, message = ex.Message };`
` 225`  `            }`
` 226`  `        }`

---

### `DeleteCourse` — lines 227–254

```
public static bool DeleteCourse(int uid, int courseId)
```

#### Explanation

- **Purpose:** Implements `DeleteCourse`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Delete/clear data.
- **Parameters:** `int uid, int courseId`
- **Local variables:** `conn`, `cmd`, `ownerCol`

#### Line-by-line (this function)

` 227`  ``
` 228`  `        public static bool DeleteCourse(int uid, int courseId)`
` 229`  `        {`
` 230`  `            try`
  - → Error handling block.
` 231`  `            {`
` 232`  `                if (uid == 0) return false;`
` 233`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
` 234`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
` 235`  `                {`
` 236`  `                    conn.Open();`
` 237`  `                    string ownerCol = DetectOwnerColumn(conn);`
` 238`  `                    cmd.CommandText = $@"DELETE FROM StudyMats WHERE SchID IN (SELECT SchID FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid));`
` 239`  `                    DELETE FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid);`
` 240`  `                    DELETE FROM Chapters WHERE CID = @cid;`
` 241`  `                    DELETE FROM Enrollments WHERE CID = @cid;`
` 242`  `                    DELETE FROM Courses WHERE CID = @cid AND [{ownerCol}] = @uid;";`
` 243`  `                    cmd.Parameters.AddWithValue("@cid", courseId);`
` 244`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 245`  `                    cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 246`  `                    return true;`
` 247`  `                }`
` 248`  `            }`
` 249`  `            catch (Exception ex)`
  - → Handle/log exception.
` 250`  `            {`
` 251`  `                try { Logger.Error(ex, "DashboardService.DeleteCourse"); } catch { }`
  - → Error handling block.
` 252`  `                return false;`
` 253`  `            }`
` 254`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Collections.Generic;`
  - → Import namespace/types.
`   3`  `using System.Configuration;`
  - → Import namespace/types.
`   4`  `using System.Data;`
  - → Import namespace/types.
`   5`  `using System.Data.SqlClient;`
  - → Import namespace/types.
`   6`  `using System.Linq;`
  - → Import namespace/types.
`   7`  `using WebAppAssignment.Shared.DebugLog;`
  - → Import namespace/types.
`   8`  ``
`   9`  `namespace WebAppAssignment.Pages.Lecturer.Services`
  - → C# namespace grouping.
`  10`  `{`
`  11`  `    public static class DashboardService`
`  12`  `    {`
`  13`  `        private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"]?.ConnectionString ?? string.Empty;`
`  14`  ``
`  15`  `        private static string DetectOwnerColumn(SqlConnection conn)`
  - → Database access (pure SQL).
`  16`  `        {`
`  17`  `            var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);`
`  18`  `            using (var cc = conn.CreateCommand())`
  - → Import namespace/types.
`  19`  `            {`
`  20`  `                cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'";`
`  21`  `                using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); }`
  - → Import namespace/types.
`  22`  `            }`
`  23`  `            return cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));`
  - → Owner lecturer foreign key.
`  24`  `        }`
`  25`  ``
`  26`  `        public static object GetDashboardData(int uid)`
`  27`  `        {`
`  28`  `            try`
  - → Error handling block.
`  29`  `            {`
`  30`  `                if (uid == 0) return new { notAuthenticated = true };`
`  31`  ``
`  32`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  33`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
`  34`  `                {`
`  35`  `                    conn.Open();`
`  36`  `                    string ownerCol = DetectOwnerColumn(conn);`
`  37`  ``
`  38`  `                    // Active courses`
`  39`  `                    cmd.CommandText = $"SELECT COUNT(1) FROM Courses WHERE [{ownerCol}] = @uid";`
`  40`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  41`  `                    int activeCourses = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
`  42`  `                    cmd.Parameters.Clear();`
`  43`  ``
`  44`  `                    // Total distinct students`
`  45`  `                    cmd.CommandText = $@"SELECT COUNT(DISTINCT e.UID) FROM Enrollments e`
`  46`  `                    JOIN Courses c ON e.CID = c.CID`
`  47`  `                    WHERE c.[{ownerCol}] = @uid";`
`  48`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  49`  `                    int totalStudents = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
`  50`  `                    cmd.Parameters.Clear();`
`  51`  ``
`  52`  `                    // Pending grading`
`  53`  `                    cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s`
`  54`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
`  55`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  56`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  57`  `                    JOIN Courses c ON ch.CID = c.CID`
`  58`  `                    LEFT JOIN CWMarkings m ON m.SID = s.SID`
`  59`  `                    WHERE c.[{ownerCol}] = @uid AND m.SID IS NULL";`
`  60`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  61`  `                    int pending = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
`  62`  `                    cmd.Parameters.Clear();`
`  63`  ``
`  64`  `                    // Average grade`
`  65`  `                    cmd.CommandText = $@"SELECT AVG(CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0) * 100.0) FROM CWMarkings m`
`  66`  `                    JOIN CWSubmissions s ON m.SID = s.SID`
`  67`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
`  68`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  69`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  70`  `                    JOIN Courses c ON ch.CID = c.CID`
`  71`  `                    WHERE c.[{ownerCol}] = @uid";`
`  72`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  73`  `                    var avgObj = cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`  74`  `                    double avg = 0; bool hasGrades = false;`
`  75`  `                    if (avgObj != null && avgObj != DBNull.Value) { avg = Convert.ToDouble(avgObj); hasGrades = true; }`
`  76`  `                    cmd.Parameters.Clear();`
`  77`  ``
`  78`  `                    // Recent submissions (top 8)`
`  79`  `                    cmd.CommandText = $@"SELECT TOP 8 s.SID, ISNULL(u.Name,'') AS StudentName, ISNULL(cw.Title,'') AS AssignmentTitle, ISNULL(c.Name,'') AS CourseName,`
`  80`  `                    ISNULL(s.Text, ISNULL(s.Content, '')) AS StudentAnswer, ISNULL(s.CreatedAt, GETDATE()) AS SubmittedAt,`
`  81`  `                    CASE WHEN m.SID IS NULL THEN 0 ELSE 1 END AS IsGraded, ISNULL(cw.MaxScore,0) AS MaxScore`
`  82`  `                    FROM CWSubmissions s`
`  83`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
`  84`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
`  85`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
`  86`  `                    JOIN Courses c ON ch.CID = c.CID`
`  87`  `                    LEFT JOIN CWMarkings m ON m.SID = s.SID`
`  88`  `                    LEFT JOIN Users u ON u.UID = s.UID`
`  89`  `                    WHERE c.[{ownerCol}] = @uid`
`  90`  `                    ORDER BY ISNULL(s.CreatedAt, GETDATE()) DESC";`
`  91`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
`  92`  `                    var submissions = new List<object>();`
`  93`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
`  94`  `                    {`
`  95`  `                        while (rdr.Read())`
`  96`  `                        {`
`  97`  `                            int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);`
`  98`  `                            string studentName = rdr.IsDBNull(1) ? "" : rdr.GetString(1);`
`  99`  `                            string assign = rdr.IsDBNull(2) ? "" : rdr.GetString(2);`
` 100`  `                            string courseName = rdr.IsDBNull(3) ? "" : rdr.GetString(3);`
` 101`  `                            string answer = rdr.IsDBNull(4) ? "" : rdr.GetString(4);`
` 102`  `                            string timeText = rdr.IsDBNull(5) ? "" : Convert.ToDateTime(rdr.GetValue(5)).ToString("g");`
` 103`  `                            bool isGraded = rdr.IsDBNull(6) ? false : rdr.GetInt32(6) != 0;`
` 104`  `                            int maxScore = rdr.IsDBNull(7) ? 0 : Convert.ToInt32(rdr.GetValue(7));`
` 105`  `                            var initials = "";`
` 106`  `                            if (!string.IsNullOrEmpty(studentName))`
` 107`  `                            {`
` 108`  `                                var parts = studentName.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);`
` 109`  `                                if (parts.Length > 1) initials = (parts[0][0].ToString() + parts[parts.Length - 1][0].ToString()).ToUpper(); else initials = parts[0][0].ToString().ToUpper();`
` 110`  `                            }`
` 111`  `                            submissions.Add(new { sid = sid, studentName = studentName, initials = initials, assignmentTitle = assign, courseName = courseName, studentAnswer = answer, timeText = timeText, isGraded = isGraded, maxScore = maxScore });`
` 112`  `                        }`
` 113`  `                    }`
` 114`  ``
` 115`  `                    // Grade distribution (A/B/C/D/F) based on percentage of MaxScore`
` 116`  `                    cmd.Parameters.Clear();`
` 117`  `                    cmd.CommandText = $@"SELECT GradeLabel, COUNT(1) AS Cnt FROM (`
` 118`  `                    SELECT CASE`
` 119`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.85 THEN 'A'`
` 120`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.70 THEN 'B'`
` 121`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.60 THEN 'C'`
` 122`  `                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.50 THEN 'D'`
` 123`  `                    ELSE 'F' END AS GradeLabel`
` 124`  `                    FROM CWMarkings m`
` 125`  `                    JOIN CWSubmissions s ON m.SID = s.SID`
` 126`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
` 127`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
` 128`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
` 129`  `                    JOIN Courses c ON ch.CID = c.CID`
` 130`  `                    WHERE c.[{ownerCol}] = @uid`
` 131`  `                    ) t GROUP BY GradeLabel";`
` 132`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 133`  `                    var gradeDist = new List<object>();`
` 134`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
` 135`  `                    {`
` 136`  `                        while (rdr.Read())`
` 137`  `                        {`
` 138`  `                            gradeDist.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });`
` 139`  `                        }`
` 140`  `                    }`
` 141`  `                    cmd.Parameters.Clear();`
` 142`  ``
` 143`  `                    // Enrollment trends: count per month for last 6 months`
` 144`  `                    cmd.CommandText = $@"SELECT FORMAT(e.CreatedAt,'yyyy-MM') AS Mon, COUNT(1) AS Cnt`
` 145`  `                    FROM Enrollments e`
` 146`  `                    JOIN Courses c ON e.CID = c.CID`
` 147`  `                    WHERE c.[{ownerCol}] = @uid AND e.CreatedAt >= DATEADD(month, -6, GETDATE())`
` 148`  `                    GROUP BY FORMAT(e.CreatedAt,'yyyy-MM')`
` 149`  `                    ORDER BY Mon ASC";`
` 150`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 151`  `                    var enrollTrend = new List<object>();`
` 152`  `                    using (var rdr = cmd.ExecuteReader())`
  - → Import namespace/types.
` 153`  `                    {`
` 154`  `                        while (rdr.Read())`
` 155`  `                        {`
` 156`  `                            enrollTrend.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });`
` 157`  `                        }`
` 158`  `                    }`
` 159`  ``
` 160`  `                    return new { success = true, totalStudents = totalStudents, activeCourses = activeCourses, pendingGrading = pending, averageGrade = Math.Round(avg, 0), hasGrades = hasGrades, submissions = submissions, gradeDistribution = gradeDist, enrollmentTrends = enrollTrend };`
` 161`  `                }`
` 162`  `            }`
` 163`  `            catch (Exception ex)`
  - → Handle/log exception.
` 164`  `            {`
` 165`  `                try { Logger.Error(ex, "DashboardService.GetDashboardData"); } catch { }`
  - → Error handling block.
` 166`  `                return new { success = false, message = ex.Message };`
` 167`  `            }`
` 168`  `        }`
` 169`  ``
` 170`  `        public static object SaveGrade(int uid, int sid, int score, string review)`
` 171`  `        {`
` 172`  `            try`
  - → Error handling block.
` 173`  `            {`
` 174`  `                if (uid == 0) return new { notAuthenticated = true };`
` 175`  ``
` 176`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
` 177`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
` 178`  `                {`
` 179`  `                    conn.Open();`
` 180`  `                    string ownerCol = DetectOwnerColumn(conn);`
` 181`  ``
` 182`  `                    // verify submission belongs to this lecturer's course`
` 183`  `                    cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s`
` 184`  `                    JOIN CourseWorks cw ON s.CWID = cw.CWID`
` 185`  `                    JOIN SubChapters sc ON cw.SchID = sc.SchID`
` 186`  `                    JOIN Chapters ch ON sc.ChID = ch.ChID`
` 187`  `                    JOIN Courses c ON ch.CID = c.CID`
` 188`  `                    WHERE s.SID = @sid AND c.[{ownerCol}] = @uid";`
` 189`  `                    cmd.Parameters.AddWithValue("@sid", sid);`
` 190`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 191`  `                    int cnt = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
` 192`  `                    cmd.Parameters.Clear();`
` 193`  `                    if (cnt == 0) return new { success = false, message = "Unauthorized or submission not found" };`
` 194`  ``
` 195`  `                    // upsert marking`
` 196`  `                    cmd.CommandText = "SELECT COUNT(1) FROM CWMarkings WHERE SID = @sid";`
` 197`  `                    cmd.Parameters.AddWithValue("@sid", sid);`
` 198`  `                    int exist = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);`
  - → Run SQL; return table / rows / scalar.
` 199`  `                    cmd.Parameters.Clear();`
` 200`  ``
` 201`  `                    if (exist > 0)`
` 202`  `                    {`
` 203`  `                        cmd.CommandText = "UPDATE CWMarkings SET Score = @score, Review = @review, Timestamp = GETDATE() WHERE SID = @sid";`
` 204`  `                        cmd.Parameters.AddWithValue("@score", score);`
` 205`  `                        cmd.Parameters.AddWithValue("@review", review ?? string.Empty);`
` 206`  `                        cmd.Parameters.AddWithValue("@sid", sid);`
` 207`  `                        cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 208`  `                    }`
` 209`  `                    else`
` 210`  `                    {`
` 211`  `                        cmd.CommandText = "INSERT INTO CWMarkings (SID, Score, Review, Timestamp) VALUES (@sid, @score, @review, GETDATE())";`
` 212`  `                        cmd.Parameters.AddWithValue("@sid", sid);`
` 213`  `                        cmd.Parameters.AddWithValue("@score", score);`
` 214`  `                        cmd.Parameters.AddWithValue("@review", review ?? string.Empty);`
` 215`  `                        cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 216`  `                    }`
` 217`  ``
` 218`  `                    return new { success = true };`
` 219`  `                }`
` 220`  `            }`
` 221`  `            catch (Exception ex)`
  - → Handle/log exception.
` 222`  `            {`
` 223`  `                try { Logger.Error(ex, "DashboardService.SaveGrade"); } catch { }`
  - → Error handling block.
` 224`  `                return new { success = false, message = ex.Message };`
` 225`  `            }`
` 226`  `        }`
` 227`  ``
` 228`  `        public static bool DeleteCourse(int uid, int courseId)`
` 229`  `        {`
` 230`  `            try`
  - → Error handling block.
` 231`  `            {`
` 232`  `                if (uid == 0) return false;`
` 233`  `                using (var conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
` 234`  `                using (var cmd = conn.CreateCommand())`
  - → Import namespace/types.
` 235`  `                {`
` 236`  `                    conn.Open();`
` 237`  `                    string ownerCol = DetectOwnerColumn(conn);`
` 238`  `                    cmd.CommandText = $@"DELETE FROM StudyMats WHERE SchID IN (SELECT SchID FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid));`
` 239`  `                    DELETE FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid);`
` 240`  `                    DELETE FROM Chapters WHERE CID = @cid;`
` 241`  `                    DELETE FROM Enrollments WHERE CID = @cid;`
` 242`  `                    DELETE FROM Courses WHERE CID = @cid AND [{ownerCol}] = @uid;";`
` 243`  `                    cmd.Parameters.AddWithValue("@cid", courseId);`
` 244`  `                    cmd.Parameters.AddWithValue("@uid", uid);`
` 245`  `                    cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 246`  `                    return true;`
` 247`  `                }`
` 248`  `            }`
` 249`  `            catch (Exception ex)`
  - → Handle/log exception.
` 250`  `            {`
` 251`  `                try { Logger.Error(ex, "DashboardService.DeleteCourse"); } catch { }`
  - → Error handling block.
` 252`  `                return false;`
` 253`  `            }`
` 254`  `        }`
` 255`  `    }`
` 256`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using WebAppAssignment.Shared.DebugLog;

namespace WebAppAssignment.Pages.Lecturer.Services
{
    public static class DashboardService
    {
        private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"]?.ConnectionString ?? string.Empty;

        private static string DetectOwnerColumn(SqlConnection conn)
        {
            var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
            using (var cc = conn.CreateCommand())
            {
                cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'";
                using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); }
            }
            return cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));
        }

        public static object GetDashboardData(int uid)
        {
            try
            {
                if (uid == 0) return new { notAuthenticated = true };

                using (var conn = new SqlConnection(ConnString))
                using (var cmd = conn.CreateCommand())
                {
                    conn.Open();
                    string ownerCol = DetectOwnerColumn(conn);

                    // Active courses
                    cmd.CommandText = $"SELECT COUNT(1) FROM Courses WHERE [{ownerCol}] = @uid";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    int activeCourses = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
                    cmd.Parameters.Clear();

                    // Total distinct students
                    cmd.CommandText = $@"SELECT COUNT(DISTINCT e.UID) FROM Enrollments e
                    JOIN Courses c ON e.CID = c.CID
                    WHERE c.[{ownerCol}] = @uid";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    int totalStudents = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
                    cmd.Parameters.Clear();

                    // Pending grading
                    cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s
                    JOIN CourseWorks cw ON s.CWID = cw.CWID
                    JOIN SubChapters sc ON cw.SchID = sc.SchID
                    JOIN Chapters ch ON sc.ChID = ch.ChID
                    JOIN Courses c ON ch.CID = c.CID
                    LEFT JOIN CWMarkings m ON m.SID = s.SID
                    WHERE c.[{ownerCol}] = @uid AND m.SID IS NULL";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    int pending = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
                    cmd.Parameters.Clear();

                    // Average grade
                    cmd.CommandText = $@"SELECT AVG(CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0) * 100.0) FROM CWMarkings m
                    JOIN CWSubmissions s ON m.SID = s.SID
                    JOIN CourseWorks cw ON s.CWID = cw.CWID
                    JOIN SubChapters sc ON cw.SchID = sc.SchID
                    JOIN Chapters ch ON sc.ChID = ch.ChID
                    JOIN Courses c ON ch.CID = c.CID
                    WHERE c.[{ownerCol}] = @uid";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    var avgObj = cmd.ExecuteScalar();
                    double avg = 0; bool hasGrades = false;
                    if (avgObj != null && avgObj != DBNull.Value) { avg = Convert.ToDouble(avgObj); hasGrades = true; }
                    cmd.Parameters.Clear();

                    // Recent submissions (top 8)
                    cmd.CommandText = $@"SELECT TOP 8 s.SID, ISNULL(u.Name,'') AS StudentName, ISNULL(cw.Title,'') AS AssignmentTitle, ISNULL(c.Name,'') AS CourseName,
                    ISNULL(s.Text, ISNULL(s.Content, '')) AS StudentAnswer, ISNULL(s.CreatedAt, GETDATE()) AS SubmittedAt,
                    CASE WHEN m.SID IS NULL THEN 0 ELSE 1 END AS IsGraded, ISNULL(cw.MaxScore,0) AS MaxScore
                    FROM CWSubmissions s
                    JOIN CourseWorks cw ON s.CWID = cw.CWID
                    JOIN SubChapters sc ON cw.SchID = sc.SchID
                    JOIN Chapters ch ON sc.ChID = ch.ChID
                    JOIN Courses c ON ch.CID = c.CID
                    LEFT JOIN CWMarkings m ON m.SID = s.SID
                    LEFT JOIN Users u ON u.UID = s.UID
                    WHERE c.[{ownerCol}] = @uid
                    ORDER BY ISNULL(s.CreatedAt, GETDATE()) DESC";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    var submissions = new List<object>();
                    using (var rdr = cmd.ExecuteReader())
                    {
                        while (rdr.Read())
                        {
                            int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);
                            string studentName = rdr.IsDBNull(1) ? "" : rdr.GetString(1);
                            string assign = rdr.IsDBNull(2) ? "" : rdr.GetString(2);
                            string courseName = rdr.IsDBNull(3) ? "" : rdr.GetString(3);
                            string answer = rdr.IsDBNull(4) ? "" : rdr.GetString(4);
                            string timeText = rdr.IsDBNull(5) ? "" : Convert.ToDateTime(rdr.GetValue(5)).ToString("g");
                            bool isGraded = rdr.IsDBNull(6) ? false : rdr.GetInt32(6) != 0;
                            int maxScore = rdr.IsDBNull(7) ? 0 : Convert.ToInt32(rdr.GetValue(7));
                            var initials = "";
                            if (!string.IsNullOrEmpty(studentName))
                            {
                                var parts = studentName.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                                if (parts.Length > 1) initials = (parts[0][0].ToString() + parts[parts.Length - 1][0].ToString()).ToUpper(); else initials = parts[0][0].ToString().ToUpper();
                            }
                            submissions.Add(new { sid = sid, studentName = studentName, initials = initials, assignmentTitle = assign, courseName = courseName, studentAnswer = answer, timeText = timeText, isGraded = isGraded, maxScore = maxScore });
                        }
                    }

                    // Grade distribution (A/B/C/D/F) based on percentage of MaxScore
                    cmd.Parameters.Clear();
                    cmd.CommandText = $@"SELECT GradeLabel, COUNT(1) AS Cnt FROM (
                    SELECT CASE
                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.85 THEN 'A'
                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.70 THEN 'B'
                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.60 THEN 'C'
                    WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.50 THEN 'D'
                    ELSE 'F' END AS GradeLabel
                    FROM CWMarkings m
                    JOIN CWSubmissions s ON m.SID = s.SID
                    JOIN CourseWorks cw ON s.CWID = cw.CWID
                    JOIN SubChapters sc ON cw.SchID = sc.SchID
                    JOIN Chapters ch ON sc.ChID = ch.ChID
                    JOIN Courses c ON ch.CID = c.CID
                    WHERE c.[{ownerCol}] = @uid
                    ) t GROUP BY GradeLabel";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    var gradeDist = new List<object>();
                    using (var rdr = cmd.ExecuteReader())
                    {
                        while (rdr.Read())
                        {
                            gradeDist.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });
                        }
                    }
                    cmd.Parameters.Clear();

                    // Enrollment trends: count per month for last 6 months
                    cmd.CommandText = $@"SELECT FORMAT(e.CreatedAt,'yyyy-MM') AS Mon, COUNT(1) AS Cnt
                    FROM Enrollments e
                    JOIN Courses c ON e.CID = c.CID
                    WHERE c.[{ownerCol}] = @uid AND e.CreatedAt >= DATEADD(month, -6, GETDATE())
                    GROUP BY FORMAT(e.CreatedAt,'yyyy-MM')
                    ORDER BY Mon ASC";
                    cmd.Parameters.AddWithValue("@uid", uid);
                    var enrollTrend = new List<object>();
                    using (var rdr = cmd.ExecuteReader())
                    {
                        while (rdr.Read())
                        {
                            enrollTrend.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });
                        }
                    }

                    return new { success = true, totalStudents = totalStudents, activeCourses = activeCourses, pendingGrading = pending, averageGrade = Math.Round(avg, 0), hasGrades = hasGrades, submissions = submissions, gradeDistribution = gradeDist, enrollmentTrends = enrollTrend };
                }
            }
            catch (Exception ex)
            {
                try { Logger.Error(ex, "DashboardService.GetDashboardData"); } catch { }
                return new { success = false, message = ex.Message };
            }
        }

        public static object SaveGrade(int uid, int sid, int score, string review)
        {
            try
            {
                if (uid == 0) return new { notAuthenticated = true };

                using (var conn = new SqlConnection(ConnString))
                using (var cmd = conn.CreateCommand())
                {
                    conn.Open();
                    string ownerCol = DetectOwnerColumn(conn);

                    // verify submission belongs to this lecturer's course
                    cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s
                    JOIN CourseWorks cw ON s.CWID = cw.CWID
                    JOIN SubChapters sc ON cw.SchID = sc.SchID
                    JOIN Chapters ch ON sc.ChID = ch.ChID
                    JOIN Courses c ON ch.CID = c.CID
                    WHERE s.SID = @sid AND c.[{ownerCol}] = @uid";
                    cmd.Parameters.AddWithValue("@sid", sid);
                    cmd.Parameters.AddWithValue("@uid", uid);
                    int cnt = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
                    cmd.Parameters.Clear();
                    if (cnt == 0) return new { success = false, message = "Unauthorized or submission not found" };

                    // upsert marking
                    cmd.CommandText = "SELECT COUNT(1) FROM CWMarkings WHERE SID = @sid";
                    cmd.Parameters.AddWithValue("@sid", sid);
                    int exist = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
                    cmd.Parameters.Clear();

                    if (exist > 0)
                    {
                        cmd.CommandText = "UPDATE CWMarkings SET Score = @score, Review = @review, Timestamp = GETDATE() WHERE SID = @sid";
                        cmd.Parameters.AddWithValue("@score", score);
                        cmd.Parameters.AddWithValue("@review", review ?? string.Empty);
                        cmd.Parameters.AddWithValue("@sid", sid);
                        cmd.ExecuteNonQuery();
                    }
                    else
                    {
                        cmd.CommandText = "INSERT INTO CWMarkings (SID, Score, Review, Timestamp) VALUES (@sid, @score, @review, GETDATE())";
                        cmd.Parameters.AddWithValue("@sid", sid);
                        cmd.Parameters.AddWithValue("@score", score);
                        cmd.Parameters.AddWithValue("@review", review ?? string.Empty);
                        cmd.ExecuteNonQuery();
                    }

                    return new { success = true };
                }
            }
            catch (Exception ex)
            {
                try { Logger.Error(ex, "DashboardService.SaveGrade"); } catch { }
                return new { success = false, message = ex.Message };
            }
        }

        public static bool DeleteCourse(int uid, int courseId)
        {
            try
            {
                if (uid == 0) return false;
                using (var conn = new SqlConnection(ConnString))
                using (var cmd = conn.CreateCommand())
                {
                    conn.Open();
                    string ownerCol = DetectOwnerColumn(conn);
                    cmd.CommandText = $@"DELETE FROM StudyMats WHERE SchID IN (SELECT SchID FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid));
                    DELETE FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid);
                    DELETE FROM Chapters WHERE CID = @cid;
                    DELETE FROM Enrollments WHERE CID = @cid;
                    DELETE FROM Courses WHERE CID = @cid AND [{ownerCol}] = @uid;";
                    cmd.Parameters.AddWithValue("@cid", courseId);
                    cmd.Parameters.AddWithValue("@uid", uid);
                    cmd.ExecuteNonQuery();
                    return true;
                }
            }
            catch (Exception ex)
            {
                try { Logger.Error(ex, "DashboardService.DeleteCourse"); } catch { }
                return false;
            }
        }
    }
}

```
