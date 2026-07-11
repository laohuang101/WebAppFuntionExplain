# DashboardService.cs
**Source:** `Pages/Lecturer/Services/DashboardService.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 256
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `ConnString` | `string` | Holds “Conn String” for this scope. (text) |

## Functions / methods (4 found)

### `DetectOwnerColumn` — lines 14–24

#### Signature

```csharp
private static string DetectOwnerColumn(SqlConnection conn)
```

#### What it is

Function `DetectOwnerColumn` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `DetectOwnerColumn`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cols` | `var` | Often a collection related to cols (plural name).  Newly constructed object. |
| `cc` | `var` | Holds “cc” for this scope. |
| `r` | `var` | Usually one database row (DataRow) in query loops. |

#### Code

```csharp
  14 | 
  15 |         private static string DetectOwnerColumn(SqlConnection conn)
  16 |         {
  17 |             var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
  18 |             using (var cc = conn.CreateCommand())
  19 |             {
  20 |                 cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'";
  21 |                 using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); }
  22 |             }
  23 |             return cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));
  24 |         }
```

---

### `GetDashboardData` — lines 25–168

#### Signature

```csharp
public static object GetDashboardData(int uid)
```

#### What it is

Reads/loads data related to **Dashboard Data** and returns it for display or further use.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.
2. Run SQL that returns one value (count, id, flag).
3. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `ownerCol` | `string` | Holds “owner Col” for this scope. (text) |
| `activeCourses` | `int` | Often a collection related to active Courses (plural name). (integer)  Assigned from single SQL scalar (COUNT/IDENTITY). |
| `totalStudents` | `int` | Often a collection related to total Students (plural name). (integer)  Assigned from single SQL scalar (COUNT/IDENTITY). |
| `pending` | `int` | Holds “pending” for this scope. (integer)  Assigned from single SQL scalar (COUNT/IDENTITY). |
| `avgObj` | `var` | Holds “avg Obj” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY). |
| `avg` | `double` | Holds “avg” for this scope. (number/score)  Literal number `0`. |
| `hasGrades` | `bool` | Boolean flag: has Grades. (true/false) |
| `submissions` | `var` | Often a collection related to submissions (plural name).  Newly constructed object. |
| `rdr` | `var` | Holds “rdr” for this scope. |
| `studentName` | `string` | Student display name. |
| `assign` | `string` | Holds “assign” for this scope. (text) |
| `courseName` | `string` | Course display name. |
| `answer` | `string` | Holds “answer” for this scope. (text) |
| `timeText` | `string` | Date/time value. (text) |
| `isGraded` | `bool` | Boolean flag: is Graded. (true/false) |
| `maxScore` | `int` | Maximum points (usually 100). |
| `initials` | `var` | Often a collection related to initials (plural name).  Literal text string. |
| `parts` | `var` | Split path or name segments. |
| `gradeDist` | `var` | Holds “grade Dist” for this scope.  Newly constructed object. |
| `enrollTrend` | `var` | Holds “enroll Trend” for this scope.  Newly constructed object. |

#### Code

```csharp
  25 | 
  26 |         public static object GetDashboardData(int uid)
  27 |         {
  28 |             try
  29 |             {
  30 |                 if (uid == 0) return new { notAuthenticated = true };
  31 | 
  32 |                 using (var conn = new SqlConnection(ConnString))
  33 |                 using (var cmd = conn.CreateCommand())
  34 |                 {
  35 |                     conn.Open();
  36 |                     string ownerCol = DetectOwnerColumn(conn);
  37 | 
  38 |                     // Active courses
  39 |                     cmd.CommandText = $"SELECT COUNT(1) FROM Courses WHERE [{ownerCol}] = @uid";
  40 |                     cmd.Parameters.AddWithValue("@uid", uid);
  41 |                     int activeCourses = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
  42 |                     cmd.Parameters.Clear();
  43 | 
  44 |                     // Total distinct students
  45 |                     cmd.CommandText = $@"SELECT COUNT(DISTINCT e.UID) FROM Enrollments e
  46 |                     JOIN Courses c ON e.CID = c.CID
  47 |                     WHERE c.[{ownerCol}] = @uid";
  48 |                     cmd.Parameters.AddWithValue("@uid", uid);
  49 |                     int totalStudents = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
  50 |                     cmd.Parameters.Clear();
  51 | 
  52 |                     // Pending grading
  53 |                     cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s
  54 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
  55 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  56 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  57 |                     JOIN Courses c ON ch.CID = c.CID
  58 |                     LEFT JOIN CWMarkings m ON m.SID = s.SID
  59 |                     WHERE c.[{ownerCol}] = @uid AND m.SID IS NULL";
  60 |                     cmd.Parameters.AddWithValue("@uid", uid);
  61 |                     int pending = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
  62 |                     cmd.Parameters.Clear();
  63 | 
  64 |                     // Average grade
  65 |                     cmd.CommandText = $@"SELECT AVG(CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0) * 100.0) FROM CWMarkings m
  66 |                     JOIN CWSubmissions s ON m.SID = s.SID
  67 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
  68 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  69 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  70 |                     JOIN Courses c ON ch.CID = c.CID
  71 |                     WHERE c.[{ownerCol}] = @uid";
  72 |                     cmd.Parameters.AddWithValue("@uid", uid);
  73 |                     var avgObj = cmd.ExecuteScalar();
  74 |                     double avg = 0; bool hasGrades = false;
  75 |                     if (avgObj != null && avgObj != DBNull.Value) { avg = Convert.ToDouble(avgObj); hasGrades = true; }
  76 |                     cmd.Parameters.Clear();
  77 | 
  78 |                     // Recent submissions (top 8)
  79 |                     cmd.CommandText = $@"SELECT TOP 8 s.SID, ISNULL(u.Name,'') AS StudentName, ISNULL(cw.Title,'') AS AssignmentTitle, ISNULL(c.Name,'') AS CourseName,
  80 |                     ISNULL(s.Text, ISNULL(s.Content, '')) AS StudentAnswer, ISNULL(s.CreatedAt, GETDATE()) AS SubmittedAt,
  81 |                     CASE WHEN m.SID IS NULL THEN 0 ELSE 1 END AS IsGraded, ISNULL(cw.MaxScore,0) AS MaxScore
  82 |                     FROM CWSubmissions s
  83 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
  84 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  85 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  86 |                     JOIN Courses c ON ch.CID = c.CID
  87 |                     LEFT JOIN CWMarkings m ON m.SID = s.SID
  88 |                     LEFT JOIN Users u ON u.UID = s.UID
  89 |                     WHERE c.[{ownerCol}] = @uid
  90 |                     ORDER BY ISNULL(s.CreatedAt, GETDATE()) DESC";
  91 |                     cmd.Parameters.AddWithValue("@uid", uid);
  92 |                     var submissions = new List<object>();
  93 |                     using (var rdr = cmd.ExecuteReader())
  94 |                     {
  95 |                         while (rdr.Read())
  96 |                         {
  97 |                             int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);
  98 |                             string studentName = rdr.IsDBNull(1) ? "" : rdr.GetString(1);
  99 |                             string assign = rdr.IsDBNull(2) ? "" : rdr.GetString(2);
 100 |                             string courseName = rdr.IsDBNull(3) ? "" : rdr.GetString(3);
 101 |                             string answer = rdr.IsDBNull(4) ? "" : rdr.GetString(4);
 102 |                             string timeText = rdr.IsDBNull(5) ? "" : Convert.ToDateTime(rdr.GetValue(5)).ToString("g");
 103 |                             bool isGraded = rdr.IsDBNull(6) ? false : rdr.GetInt32(6) != 0;
 104 |                             int maxScore = rdr.IsDBNull(7) ? 0 : Convert.ToInt32(rdr.GetValue(7));
 105 |                             var initials = "";
 106 |                             if (!string.IsNullOrEmpty(studentName))
 107 |                             {
 108 |                                 var parts = studentName.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
 109 |                                 if (parts.Length > 1) initials = (parts[0][0].ToString() + parts[parts.Length - 1][0].ToString()).ToUpper(); else initials = parts[0][0].ToString().ToUpper();
 110 |                             }
 111 |                             submissions.Add(new { sid = sid, studentName = studentName, initials = initials, assignmentTitle = assign, courseName = courseName, studentAnswer = answer, timeText = timeText, isGraded = isGraded, maxScore = maxScore });
 112 |                         }
 113 |                     }
 114 | 
 115 |                     // Grade distribution (A/B/C/D/F) based on percentage of MaxScore
 116 |                     cmd.Parameters.Clear();
 117 |                     cmd.CommandText = $@"SELECT GradeLabel, COUNT(1) AS Cnt FROM (
 118 |                     SELECT CASE
 119 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.85 THEN 'A'
 120 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.70 THEN 'B'
 121 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.60 THEN 'C'
 122 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.50 THEN 'D'
 123 |                     ELSE 'F' END AS GradeLabel
 124 |                     FROM CWMarkings m
 125 |                     JOIN CWSubmissions s ON m.SID = s.SID
 126 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
 127 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
 128 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
 129 |                     JOIN Courses c ON ch.CID = c.CID
 130 |                     WHERE c.[{ownerCol}] = @uid
 131 |                     ) t GROUP BY GradeLabel";
 132 |                     cmd.Parameters.AddWithValue("@uid", uid);
 133 |                     var gradeDist = new List<object>();
 134 |                     using (var rdr = cmd.ExecuteReader())
 135 |                     {
 136 |                         while (rdr.Read())
 137 |                         {
 138 |                             gradeDist.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });
 139 |                         }
 140 |                     }
 141 |                     cmd.Parameters.Clear();
 142 | 
 143 |                     // Enrollment trends: count per month for last 6 months
 144 |                     cmd.CommandText = $@"SELECT FORMAT(e.CreatedAt,'yyyy-MM') AS Mon, COUNT(1) AS Cnt
 145 |                     FROM Enrollments e
 146 |                     JOIN Courses c ON e.CID = c.CID
 147 |                     WHERE c.[{ownerCol}] = @uid AND e.CreatedAt >= DATEADD(month, -6, GETDATE())
 148 |                     GROUP BY FORMAT(e.CreatedAt,'yyyy-MM')
 149 |                     ORDER BY Mon ASC";
 150 |                     cmd.Parameters.AddWithValue("@uid", uid);
 151 |                     var enrollTrend = new List<object>();
 152 |                     using (var rdr = cmd.ExecuteReader())
 153 |                     {
 154 |                         while (rdr.Read())
 155 |                         {
 156 |                             enrollTrend.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });
 157 |                         }
 158 |                     }
 159 | 
 160 |                     return new { success = true, totalStudents = totalStudents, activeCourses = activeCourses, pendingGrading = pending, averageGrade = Math.Round(avg, 0), hasGrades = hasGrades, submissions = submissions, gradeDistribution = gradeDist, enrollmentTrends = enrollTrend };
 161 |                 }
 162 |             }
 163 |             catch (Exception ex)
 164 |             {
 165 |                 try { Logger.Error(ex, "DashboardService.GetDashboardData"); } catch { }
 166 |                 return new { success = false, message = ex.Message };
 167 |             }
 168 |         }
```

---

### `SaveGrade` — lines 169–226

#### Signature

```csharp
public static object SaveGrade(int uid, int sid, int score, string review)
```

#### What it is

Saves marks and feedback for a student submission.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.
2. Run SQL that returns one value (count, id, flag).
3. Run INSERT/UPDATE/DELETE SQL against the database.
4. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `sid` | `int` | Submission ID (CWSubmissions.SID). |
| `score` | `int` | Points earned or max points depending on context. |
| `review` | `string` | Holds “review” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `ownerCol` | `string` | Holds “owner Col” for this scope. (text) |
| `cnt` | `int` | Holds “cnt” for this scope. (integer)  Assigned from single SQL scalar (COUNT/IDENTITY). |
| `exist` | `int` | Holds “exist” for this scope. (integer)  Assigned from single SQL scalar (COUNT/IDENTITY). |

#### Code

```csharp
 169 | 
 170 |         public static object SaveGrade(int uid, int sid, int score, string review)
 171 |         {
 172 |             try
 173 |             {
 174 |                 if (uid == 0) return new { notAuthenticated = true };
 175 | 
 176 |                 using (var conn = new SqlConnection(ConnString))
 177 |                 using (var cmd = conn.CreateCommand())
 178 |                 {
 179 |                     conn.Open();
 180 |                     string ownerCol = DetectOwnerColumn(conn);
 181 | 
 182 |                     // verify submission belongs to this lecturer's course
 183 |                     cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s
 184 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
 185 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
 186 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
 187 |                     JOIN Courses c ON ch.CID = c.CID
 188 |                     WHERE s.SID = @sid AND c.[{ownerCol}] = @uid";
 189 |                     cmd.Parameters.AddWithValue("@sid", sid);
 190 |                     cmd.Parameters.AddWithValue("@uid", uid);
 191 |                     int cnt = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
 192 |                     cmd.Parameters.Clear();
 193 |                     if (cnt == 0) return new { success = false, message = "Unauthorized or submission not found" };
 194 | 
 195 |                     // upsert marking
 196 |                     cmd.CommandText = "SELECT COUNT(1) FROM CWMarkings WHERE SID = @sid";
 197 |                     cmd.Parameters.AddWithValue("@sid", sid);
 198 |                     int exist = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
 199 |                     cmd.Parameters.Clear();
 200 | 
 201 |                     if (exist > 0)
 202 |                     {
 203 |                         cmd.CommandText = "UPDATE CWMarkings SET Score = @score, Review = @review, Timestamp = GETDATE() WHERE SID = @sid";
 204 |                         cmd.Parameters.AddWithValue("@score", score);
 205 |                         cmd.Parameters.AddWithValue("@review", review ?? string.Empty);
 206 |                         cmd.Parameters.AddWithValue("@sid", sid);
 207 |                         cmd.ExecuteNonQuery();
 208 |                     }
 209 |                     else
 210 |                     {
 211 |                         cmd.CommandText = "INSERT INTO CWMarkings (SID, Score, Review, Timestamp) VALUES (@sid, @score, @review, GETDATE())";
 212 |                         cmd.Parameters.AddWithValue("@sid", sid);
 213 |                         cmd.Parameters.AddWithValue("@score", score);
 214 |                         cmd.Parameters.AddWithValue("@review", review ?? string.Empty);
 215 |                         cmd.ExecuteNonQuery();
 216 |                     }
 217 | 
 218 |                     return new { success = true };
 219 |                 }
 220 |             }
 221 |             catch (Exception ex)
 222 |             {
 223 |                 try { Logger.Error(ex, "DashboardService.SaveGrade"); } catch { }
 224 |                 return new { success = false, message = ex.Message };
 225 |             }
 226 |         }
```

---

### `DeleteCourse` — lines 227–254

#### Signature

```csharp
public static bool DeleteCourse(int uid, int courseId)
```

#### What it is

Deletes or clears **Delete Course** (data or temporary state).

#### How it works

1. Open a connection to the LocalDB / SQL Server database.
2. Run INSERT/UPDATE/DELETE SQL against the database.
3. Return `true` to the caller.
4. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `courseId` | `int` | Holds “course Id” for this scope. (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `ownerCol` | `string` | Holds “owner Col” for this scope. (text) |

#### Code

```csharp
 227 | 
 228 |         public static bool DeleteCourse(int uid, int courseId)
 229 |         {
 230 |             try
 231 |             {
 232 |                 if (uid == 0) return false;
 233 |                 using (var conn = new SqlConnection(ConnString))
 234 |                 using (var cmd = conn.CreateCommand())
 235 |                 {
 236 |                     conn.Open();
 237 |                     string ownerCol = DetectOwnerColumn(conn);
 238 |                     cmd.CommandText = $@"DELETE FROM StudyMats WHERE SchID IN (SELECT SchID FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid));
 239 |                     DELETE FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid);
 240 |                     DELETE FROM Chapters WHERE CID = @cid;
 241 |                     DELETE FROM Enrollments WHERE CID = @cid;
 242 |                     DELETE FROM Courses WHERE CID = @cid AND [{ownerCol}] = @uid;";
 243 |                     cmd.Parameters.AddWithValue("@cid", courseId);
 244 |                     cmd.Parameters.AddWithValue("@uid", uid);
 245 |                     cmd.ExecuteNonQuery();
 246 |                     return true;
 247 |                 }
 248 |             }
 249 |             catch (Exception ex)
 250 |             {
 251 |                 try { Logger.Error(ex, "DashboardService.DeleteCourse"); } catch { }
 252 |                 return false;
 253 |             }
 254 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Collections.Generic;
   3 | using System.Configuration;
   4 | using System.Data;
   5 | using System.Data.SqlClient;
   6 | using System.Linq;
   7 | using WebAppAssignment.Shared.DebugLog;
   8 | 
   9 | namespace WebAppAssignment.Pages.Lecturer.Services
  10 | {
  11 |     public static class DashboardService
  12 |     {
  13 |         private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"]?.ConnectionString ?? string.Empty;
  14 | 
  15 |         private static string DetectOwnerColumn(SqlConnection conn)
  16 |         {
  17 |             var cols = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
  18 |             using (var cc = conn.CreateCommand())
  19 |             {
  20 |                 cc.CommandText = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Courses'";
  21 |                 using (var r = cc.ExecuteReader()) { while (r.Read()) cols.Add(r.GetString(0)); }
  22 |             }
  23 |             return cols.Contains("UID") ? "UID" : (cols.Contains("LecturerUID") ? "LecturerUID" : (cols.Contains("UserID") ? "UserID" : "UID"));
  24 |         }
  25 | 
  26 |         public static object GetDashboardData(int uid)
  27 |         {
  28 |             try
  29 |             {
  30 |                 if (uid == 0) return new { notAuthenticated = true };
  31 | 
  32 |                 using (var conn = new SqlConnection(ConnString))
  33 |                 using (var cmd = conn.CreateCommand())
  34 |                 {
  35 |                     conn.Open();
  36 |                     string ownerCol = DetectOwnerColumn(conn);
  37 | 
  38 |                     // Active courses
  39 |                     cmd.CommandText = $"SELECT COUNT(1) FROM Courses WHERE [{ownerCol}] = @uid";
  40 |                     cmd.Parameters.AddWithValue("@uid", uid);
  41 |                     int activeCourses = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
  42 |                     cmd.Parameters.Clear();
  43 | 
  44 |                     // Total distinct students
  45 |                     cmd.CommandText = $@"SELECT COUNT(DISTINCT e.UID) FROM Enrollments e
  46 |                     JOIN Courses c ON e.CID = c.CID
  47 |                     WHERE c.[{ownerCol}] = @uid";
  48 |                     cmd.Parameters.AddWithValue("@uid", uid);
  49 |                     int totalStudents = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
  50 |                     cmd.Parameters.Clear();
  51 | 
  52 |                     // Pending grading
  53 |                     cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s
  54 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
  55 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  56 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  57 |                     JOIN Courses c ON ch.CID = c.CID
  58 |                     LEFT JOIN CWMarkings m ON m.SID = s.SID
  59 |                     WHERE c.[{ownerCol}] = @uid AND m.SID IS NULL";
  60 |                     cmd.Parameters.AddWithValue("@uid", uid);
  61 |                     int pending = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
  62 |                     cmd.Parameters.Clear();
  63 | 
  64 |                     // Average grade
  65 |                     cmd.CommandText = $@"SELECT AVG(CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0) * 100.0) FROM CWMarkings m
  66 |                     JOIN CWSubmissions s ON m.SID = s.SID
  67 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
  68 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  69 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  70 |                     JOIN Courses c ON ch.CID = c.CID
  71 |                     WHERE c.[{ownerCol}] = @uid";
  72 |                     cmd.Parameters.AddWithValue("@uid", uid);
  73 |                     var avgObj = cmd.ExecuteScalar();
  74 |                     double avg = 0; bool hasGrades = false;
  75 |                     if (avgObj != null && avgObj != DBNull.Value) { avg = Convert.ToDouble(avgObj); hasGrades = true; }
  76 |                     cmd.Parameters.Clear();
  77 | 
  78 |                     // Recent submissions (top 8)
  79 |                     cmd.CommandText = $@"SELECT TOP 8 s.SID, ISNULL(u.Name,'') AS StudentName, ISNULL(cw.Title,'') AS AssignmentTitle, ISNULL(c.Name,'') AS CourseName,
  80 |                     ISNULL(s.Text, ISNULL(s.Content, '')) AS StudentAnswer, ISNULL(s.CreatedAt, GETDATE()) AS SubmittedAt,
  81 |                     CASE WHEN m.SID IS NULL THEN 0 ELSE 1 END AS IsGraded, ISNULL(cw.MaxScore,0) AS MaxScore
  82 |                     FROM CWSubmissions s
  83 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
  84 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
  85 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
  86 |                     JOIN Courses c ON ch.CID = c.CID
  87 |                     LEFT JOIN CWMarkings m ON m.SID = s.SID
  88 |                     LEFT JOIN Users u ON u.UID = s.UID
  89 |                     WHERE c.[{ownerCol}] = @uid
  90 |                     ORDER BY ISNULL(s.CreatedAt, GETDATE()) DESC";
  91 |                     cmd.Parameters.AddWithValue("@uid", uid);
  92 |                     var submissions = new List<object>();
  93 |                     using (var rdr = cmd.ExecuteReader())
  94 |                     {
  95 |                         while (rdr.Read())
  96 |                         {
  97 |                             int sid = rdr.IsDBNull(0) ? 0 : rdr.GetInt32(0);
  98 |                             string studentName = rdr.IsDBNull(1) ? "" : rdr.GetString(1);
  99 |                             string assign = rdr.IsDBNull(2) ? "" : rdr.GetString(2);
 100 |                             string courseName = rdr.IsDBNull(3) ? "" : rdr.GetString(3);
 101 |                             string answer = rdr.IsDBNull(4) ? "" : rdr.GetString(4);
 102 |                             string timeText = rdr.IsDBNull(5) ? "" : Convert.ToDateTime(rdr.GetValue(5)).ToString("g");
 103 |                             bool isGraded = rdr.IsDBNull(6) ? false : rdr.GetInt32(6) != 0;
 104 |                             int maxScore = rdr.IsDBNull(7) ? 0 : Convert.ToInt32(rdr.GetValue(7));
 105 |                             var initials = "";
 106 |                             if (!string.IsNullOrEmpty(studentName))
 107 |                             {
 108 |                                 var parts = studentName.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
 109 |                                 if (parts.Length > 1) initials = (parts[0][0].ToString() + parts[parts.Length - 1][0].ToString()).ToUpper(); else initials = parts[0][0].ToString().ToUpper();
 110 |                             }
 111 |                             submissions.Add(new { sid = sid, studentName = studentName, initials = initials, assignmentTitle = assign, courseName = courseName, studentAnswer = answer, timeText = timeText, isGraded = isGraded, maxScore = maxScore });
 112 |                         }
 113 |                     }
 114 | 
 115 |                     // Grade distribution (A/B/C/D/F) based on percentage of MaxScore
 116 |                     cmd.Parameters.Clear();
 117 |                     cmd.CommandText = $@"SELECT GradeLabel, COUNT(1) AS Cnt FROM (
 118 |                     SELECT CASE
 119 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.85 THEN 'A'
 120 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.70 THEN 'B'
 121 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.60 THEN 'C'
 122 |                     WHEN (CAST(m.Score AS FLOAT) / NULLIF(ISNULL(cw.MaxScore,0),0)) >= 0.50 THEN 'D'
 123 |                     ELSE 'F' END AS GradeLabel
 124 |                     FROM CWMarkings m
 125 |                     JOIN CWSubmissions s ON m.SID = s.SID
 126 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
 127 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
 128 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
 129 |                     JOIN Courses c ON ch.CID = c.CID
 130 |                     WHERE c.[{ownerCol}] = @uid
 131 |                     ) t GROUP BY GradeLabel";
 132 |                     cmd.Parameters.AddWithValue("@uid", uid);
 133 |                     var gradeDist = new List<object>();
 134 |                     using (var rdr = cmd.ExecuteReader())
 135 |                     {
 136 |                         while (rdr.Read())
 137 |                         {
 138 |                             gradeDist.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });
 139 |                         }
 140 |                     }
 141 |                     cmd.Parameters.Clear();
 142 | 
 143 |                     // Enrollment trends: count per month for last 6 months
 144 |                     cmd.CommandText = $@"SELECT FORMAT(e.CreatedAt,'yyyy-MM') AS Mon, COUNT(1) AS Cnt
 145 |                     FROM Enrollments e
 146 |                     JOIN Courses c ON e.CID = c.CID
 147 |                     WHERE c.[{ownerCol}] = @uid AND e.CreatedAt >= DATEADD(month, -6, GETDATE())
 148 |                     GROUP BY FORMAT(e.CreatedAt,'yyyy-MM')
 149 |                     ORDER BY Mon ASC";
 150 |                     cmd.Parameters.AddWithValue("@uid", uid);
 151 |                     var enrollTrend = new List<object>();
 152 |                     using (var rdr = cmd.ExecuteReader())
 153 |                     {
 154 |                         while (rdr.Read())
 155 |                         {
 156 |                             enrollTrend.Add(new { label = rdr.GetString(0), value = rdr.GetInt32(1) });
 157 |                         }
 158 |                     }
 159 | 
 160 |                     return new { success = true, totalStudents = totalStudents, activeCourses = activeCourses, pendingGrading = pending, averageGrade = Math.Round(avg, 0), hasGrades = hasGrades, submissions = submissions, gradeDistribution = gradeDist, enrollmentTrends = enrollTrend };
 161 |                 }
 162 |             }
 163 |             catch (Exception ex)
 164 |             {
 165 |                 try { Logger.Error(ex, "DashboardService.GetDashboardData"); } catch { }
 166 |                 return new { success = false, message = ex.Message };
 167 |             }
 168 |         }
 169 | 
 170 |         public static object SaveGrade(int uid, int sid, int score, string review)
 171 |         {
 172 |             try
 173 |             {
 174 |                 if (uid == 0) return new { notAuthenticated = true };
 175 | 
 176 |                 using (var conn = new SqlConnection(ConnString))
 177 |                 using (var cmd = conn.CreateCommand())
 178 |                 {
 179 |                     conn.Open();
 180 |                     string ownerCol = DetectOwnerColumn(conn);
 181 | 
 182 |                     // verify submission belongs to this lecturer's course
 183 |                     cmd.CommandText = $@"SELECT COUNT(1) FROM CWSubmissions s
 184 |                     JOIN CourseWorks cw ON s.CWID = cw.CWID
 185 |                     JOIN SubChapters sc ON cw.SchID = sc.SchID
 186 |                     JOIN Chapters ch ON sc.ChID = ch.ChID
 187 |                     JOIN Courses c ON ch.CID = c.CID
 188 |                     WHERE s.SID = @sid AND c.[{ownerCol}] = @uid";
 189 |                     cmd.Parameters.AddWithValue("@sid", sid);
 190 |                     cmd.Parameters.AddWithValue("@uid", uid);
 191 |                     int cnt = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
 192 |                     cmd.Parameters.Clear();
 193 |                     if (cnt == 0) return new { success = false, message = "Unauthorized or submission not found" };
 194 | 
 195 |                     // upsert marking
 196 |                     cmd.CommandText = "SELECT COUNT(1) FROM CWMarkings WHERE SID = @sid";
 197 |                     cmd.Parameters.AddWithValue("@sid", sid);
 198 |                     int exist = Convert.ToInt32(cmd.ExecuteScalar() ?? 0);
 199 |                     cmd.Parameters.Clear();
 200 | 
 201 |                     if (exist > 0)
 202 |                     {
 203 |                         cmd.CommandText = "UPDATE CWMarkings SET Score = @score, Review = @review, Timestamp = GETDATE() WHERE SID = @sid";
 204 |                         cmd.Parameters.AddWithValue("@score", score);
 205 |                         cmd.Parameters.AddWithValue("@review", review ?? string.Empty);
 206 |                         cmd.Parameters.AddWithValue("@sid", sid);
 207 |                         cmd.ExecuteNonQuery();
 208 |                     }
 209 |                     else
 210 |                     {
 211 |                         cmd.CommandText = "INSERT INTO CWMarkings (SID, Score, Review, Timestamp) VALUES (@sid, @score, @review, GETDATE())";
 212 |                         cmd.Parameters.AddWithValue("@sid", sid);
 213 |                         cmd.Parameters.AddWithValue("@score", score);
 214 |                         cmd.Parameters.AddWithValue("@review", review ?? string.Empty);
 215 |                         cmd.ExecuteNonQuery();
 216 |                     }
 217 | 
 218 |                     return new { success = true };
 219 |                 }
 220 |             }
 221 |             catch (Exception ex)
 222 |             {
 223 |                 try { Logger.Error(ex, "DashboardService.SaveGrade"); } catch { }
 224 |                 return new { success = false, message = ex.Message };
 225 |             }
 226 |         }
 227 | 
 228 |         public static bool DeleteCourse(int uid, int courseId)
 229 |         {
 230 |             try
 231 |             {
 232 |                 if (uid == 0) return false;
 233 |                 using (var conn = new SqlConnection(ConnString))
 234 |                 using (var cmd = conn.CreateCommand())
 235 |                 {
 236 |                     conn.Open();
 237 |                     string ownerCol = DetectOwnerColumn(conn);
 238 |                     cmd.CommandText = $@"DELETE FROM StudyMats WHERE SchID IN (SELECT SchID FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid));
 239 |                     DELETE FROM SubChapters WHERE ChID IN (SELECT ChID FROM Chapters WHERE CID = @cid);
 240 |                     DELETE FROM Chapters WHERE CID = @cid;
 241 |                     DELETE FROM Enrollments WHERE CID = @cid;
 242 |                     DELETE FROM Courses WHERE CID = @cid AND [{ownerCol}] = @uid;";
 243 |                     cmd.Parameters.AddWithValue("@cid", courseId);
 244 |                     cmd.Parameters.AddWithValue("@uid", uid);
 245 |                     cmd.ExecuteNonQuery();
 246 |                     return true;
 247 |                 }
 248 |             }
 249 |             catch (Exception ex)
 250 |             {
 251 |                 try { Logger.Error(ex, "DashboardService.DeleteCourse"); } catch { }
 252 |                 return false;
 253 |             }
 254 |         }
 255 |     }
 256 | }
```
