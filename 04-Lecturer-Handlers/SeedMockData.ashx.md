# SeedMockData.ashx
**Source:** `Pages/Lecturer/SeedMockData.ashx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 645
- **Kind:** `.ashx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (17 found)

### `IsSeedAllowed` — lines 30–43

#### Signature

```html
private static bool IsSeedAllowed()
```

#### What it is

Checks a condition related to **Is Seed Allowed** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `IsSeedAllowed`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `allow` | `string` | Holds “allow” for this scope. (text)  Read from Web.config. |

#### Code

```html
  30 | 
  31 |     private static bool IsSeedAllowed()
  32 |     {
  33 |         string allow = ConfigurationManager.AppSettings["AllowSeedMockData"];
  34 |         if (string.Equals(allow, "true", StringComparison.OrdinalIgnoreCase)) return true;
  35 |         if (string.Equals(allow, "false", StringComparison.OrdinalIgnoreCase)) return false;
  36 |         // default: only when compilation debug
  37 |         try
  38 |         {
  39 |             return HttpContext.Current != null
  40 |                 && HttpContext.Current.IsDebuggingEnabled;
  41 |         }
  42 |         catch { return false; }
  43 |     }
```

---

### `ProcessRequest` — lines 54–271

#### Signature

```html
public void ProcessRequest(HttpContext context)
```

#### What it is

Main entry point for an `.ashx` HTTP handler — handles one browser request from start to finish.

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.
2. Write an audit-log row for this security event.
3. Open a connection to the LocalDB / SQL Server database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `teacherEmail` | `string` | Email address. (text)  Comes from HTTP request. |
| `reset` | `bool` | Holds “reset” for this scope. (true/false)  Comes from HTTP request. |
| `log` | `var` | Holds “log” for this scope.  Newly constructed object. |
| `courseSummaries` | `var` | Often a collection related to course Summaries (plural name).  Newly constructed object. |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `lecturerUid` | `int` | Users.UID of the course owner (lecturer). |
| `s1` | `int` | Holds “s1” for this scope. (integer) |
| `s2` | `int` | Holds “s2” for this scope. (integer) |
| `s3` | `int` | Holds “s3” for this scope. (integer) |
| `s4` | `int` | Holds “s4” for this scope. (integer) |
| `s5` | `int` | Holds “s5” for this scope. (integer) |
| `studentIds` | `var` | Often a collection related to student Ids (plural name).  Newly constructed object. |
| `defs` | `var` | Often a collection related to defs (plural name).  Newly constructed object. |
| `enrollCount` | `int` | Numeric count of items related to `enroll Count`. (integer) |
| `cid` | `int` | Course ID (Courses.CID). |
| `i` | `int` | Loop index (0-based counter in for-loops).  Literal number `0`. |
| `progress` | `int` | Often a collection related to progress (plural name). (integer) |
| `assessCh` | `int` | Holds “assess Ch” for this scope. (integer) |
| `cwid1` | `int` | Holds “cwid1” for this scope. (integer) |
| `cwid2` | `int` | Holds “cwid2” for this scope. (integer) |
| `cwid3` | `int` | Holds “cwid3” for this scope. (integer) |
| `sid1` | `int` | Holds “sid1” for this scope. (integer) |
| `sid2` | `int` | Holds “sid2” for this scope. (integer) |
| `fileJson` | `string` | Holds “file Json” for this scope. (text)  Literal text string. |
| `sc` | `int` | Holds “sc” for this scope. (integer) |
| `cw` | `int` | Holds “cw” for this scope. (integer) |
| `subs` | `int` | Often a collection related to subs (plural name). (integer) |
| `marks` | `int` | Often a collection related to marks (plural name). (integer) |
| `def` | `—` | Holds “def” for this scope. |
| `chTitle` | `—` | Holds “ch Title” for this scope. |
| `stuid` | `—` | Identifier (`stuid`) — database primary/foreign key. |

#### Code

```html
  54 | 
  55 |     public void ProcessRequest(HttpContext context)
  56 |     {
  57 |         context.Response.ContentType = "application/json; charset=utf-8";
  58 |         context.Response.Cache.SetCacheability(HttpCacheability.NoCache);
  59 | 
  60 |         try
  61 |         {
  62 |             if (!IsSeedAllowed())
  63 |             {
  64 |                 AuthGate.WriteHandlerError(context, 403, "Seed endpoint is disabled. Set AllowSeedMockData=true in Web.config (debug only).");
  65 |                 return;
  66 |             }
  67 | 
  68 |             int uid;
  69 |             if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin"))
  70 |                 return;
  71 | 
  72 |             SecurityAudit.Log("seed.start", uid, "email=" + (context.Request["email"] ?? DefaultTeacherEmail));
  73 | 
  74 |             string teacherEmail = (context.Request["email"] ?? DefaultTeacherEmail).Trim().ToLowerInvariant();
  75 |             if (string.IsNullOrEmpty(teacherEmail)) teacherEmail = DefaultTeacherEmail;
  76 |             bool reset = context.Request["reset"] == "1";
  77 | 
  78 |             var log = new List<string>();
  79 |             var courseSummaries = new List<object>();
  80 | 
  81 |             using (var conn = DbHelper.OpenConnection())
  82 |             {
  83 |                 if (reset) ClearMockStudentData(conn, log);
  84 | 
  85 |                 // ── Teacher 1: t@t.com ────────────────────────────────────
  86 |                 int lecturerUid = EnsureTeacher(conn, teacherEmail, "Teacher One", DefaultTeacherPassword, log);
  87 |                 if (lecturerUid <= 0)
  88 |                 {
  89 |                     Write(context, new { success = false, message = "Could not create/find teacher " + teacherEmail });
  90 |                     return;
  91 |                 }
  92 | 
  93 |                 // ── Students ──────────────────────────────────────────────
  94 |                 int s1 = EnsureStudent(conn, "Alice Tan", "student1@edulms.local", log);
  95 |                 int s2 = EnsureStudent(conn, "Bob Lee", "student2@edulms.local", log);
  96 |                 int s3 = EnsureStudent(conn, "Cara Ng", "student3@edulms.local", log);
  97 |                 int s4 = EnsureStudent(conn, "Daniel Ong", "student4@edulms.local", log);
  98 |                 int s5 = EnsureStudent(conn, "Emily Wong", "student5@edulms.local", log);
  99 |                 var studentIds = new List<int> { s1, s2, s3, s4, s5 };
 100 | 
 101 |                 EnsureGradeScales(conn, log);
 102 | 
 103 |                 // ── 3 courses owned by t@t.com ────────────────────────────
 104 |                 var defs = new[]
 105 |                 {
 106 |                     new MockCourseDef
 107 |                     {
 108 |                         Name = "Product Design Fundamentals",
 109 |                         Description = "UI/UX basics, wireframes, and design critique for beginners.",
 110 |                         Category = "Design",
 111 |                         Level = "Beginner",
 112 |                         Rating = 4.3m,
 113 |                         Chapters = new[] { "Intro & Tools", "Wireframing", "Assessments" }
 114 |                     },
 115 |                     new MockCourseDef
 116 |                     {
 117 |                         Name = "Web App Programming",
 118 |                         Description = "ASP.NET Web Forms, pure SQL, and auth for EduLMS-style apps.",
 119 |                         Category = "Programming",
 120 |                         Level = "Intermediate",
 121 |                         Rating = 4.6m,
 122 |                         Chapters = new[] { "Web Forms Basics", "Data Access", "Assessments" }
 123 |                     },
 124 |                     new MockCourseDef
 125 |                     {
 126 |                         Name = "Database Essentials",
 127 |                         Description = "ER modelling, SQL queries, and LocalDB for coursework.",
 128 |                         Category = "Database",
 129 |                         Level = "Beginner",
 130 |                         Rating = 4.1m,
 131 |                         Chapters = new[] { "ER Diagrams", "SQL Queries", "Assessments" }
 132 |                     }
 133 |                 };
 134 | 
 135 |                 int enrollCount = 0, workCount = 0, subCount = 0, markCount = 0, courseCreated = 0;
 136 | 
 137 |                 foreach (var def in defs)
 138 |                 {
 139 |                     int cid = EnsureCourse(conn, lecturerUid, def, log, ref courseCreated);
 140 |                     if (cid <= 0)
 141 |                     {
 142 |                         log.Add("FAILED to create/find course: " + def.Name);
 143 |                         continue;
 144 |                     }
 145 | 
 146 |                     foreach (var chTitle in def.Chapters)
 147 |                         EnsureChapter(conn, cid, chTitle);
 148 | 
 149 |                     // Enroll all 5 students
 150 |                     int i = 0;
 151 |                     foreach (int stuid in studentIds)
 152 |                     {
 153 |                         int progress = 25 + ((stuid + i * 13) % 70);
 154 |                         if (EnsureEnrollment(conn, cid, stuid, progress))
 155 |                             enrollCount++;
 156 |                         i++;
 157 |                     }
 158 | 
 159 |                     int assessCh = EnsureChapter(conn, cid, "Assessments");
 160 | 
 161 |                     // Text-only, file-required, and mixed assessments
 162 |                     int cwid1 = EnsureCourseWork(conn, assessCh,
 163 |                         "Week 3 Written Task",
 164 |                         BuildCwDescription("Write a short reflection on the module materials.", "Text", 100, false),
 165 |                         DateTime.Today.AddDays(14), ref workCount);
 166 | 
 167 |                     int cwid2 = EnsureCourseWork(conn, assessCh,
 168 |                         "Midterm Quiz Pack",
 169 |                         BuildCwDescription("Answer all objective questions.", "Objective", 50, false),
 170 |                         DateTime.Today.AddDays(21), ref workCount);
 171 | 
 172 |                     // File-upload required — PDF essay
 173 |                     int cwid3 = EnsureCourseWork(conn, assessCh,
 174 |                         "PDF Essay Upload",
 175 |                         BuildCwDescription("Upload your essay as a PDF (file upload required). You may also add notes.", "File", 100, true),
 176 |                         DateTime.Today.AddDays(30), ref workCount);
 177 | 
 178 |                     foreach (int stuid in studentIds)
 179 |                     {
 180 |                         int sid1 = EnsureSubmission(conn, cwid1, stuid,
 181 |                             "Written answer from student " + stuid + " for " + def.Name + ".",
 182 |                             DateTime.Now.AddDays(-4), ref subCount);
 183 |                         if (sid1 > 0)
 184 |                             EnsureMarking(conn, sid1, 62 + (stuid % 30), "Solid effort — keep going.", ref markCount);
 185 | 
 186 |                         int sid2 = EnsureSubmission(conn, cwid2, stuid,
 187 |                             "Quiz answers A,C,B,D (student " + stuid + ").",
 188 |                             DateTime.Now.AddDays(-2), ref subCount);
 189 |                         // Leave odd UIDs ungraded for grading queue
 190 |                         if (sid2 > 0 && stuid % 2 == 0)
 191 |                             EnsureMarking(conn, sid2, 45 + (stuid % 40), "Quiz auto mock grade.", ref markCount);
 192 | 
 193 |                         // File-required assessment: store JSON content with a placeholder path
 194 |                         // (students re-upload a real PDF via Submit.aspx for full preview)
 195 |                         if (stuid % 3 != 0)
 196 |                         {
 197 |                             string fileJson = "{\"v\":1,\"text\":\"See attached essay PDF.\",\"file\":\"\",\"fileName\":\"essay-student-" + stuid + ".pdf\"}";
 198 |                             // Prefer real note-only until student uploads; mark require via assignment meta
 199 |                             EnsureSubmission(conn, cwid3, stuid,
 200 |                                 "Essay notes from student " + stuid + " — PDF should be uploaded via Submit page.",
 201 |                                 DateTime.Now.AddDays(-1), ref subCount);
 202 |                         }
 203 |                     }
 204 | 
 205 |                     int sc = ScalarInt(conn, "SELECT COUNT(*) FROM Enrollments WHERE CID=@C", P("@C", cid));
 206 |                     int cw = ScalarInt(conn, @"
 207 | SELECT COUNT(*) FROM CourseWorks cw
 208 | INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));
 209 |                     int subs = ScalarInt(conn, @"
 210 | SELECT COUNT(*) FROM CWSubmissions s
 211 | INNER JOIN CourseWorks cw ON cw.CWID = s.CWID
 212 | INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));
 213 |                     int marks = ScalarInt(conn, @"
 214 | SELECT COUNT(*) FROM CWMarkings m
 215 | INNER JOIN CWSubmissions s ON s.SID = m.SID
 216 | INNER JOIN CourseWorks cw ON cw.CWID = s.CWID
 217 | INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));
 218 | 
 219 |                     log.Add(string.Format("CID={0} \"{1}\" students={2} assessments={3} submissions={4} markings={5}",
 220 |                         cid, def.Name, sc, cw, subs, marks));
 221 | 
 222 |                     courseSummaries.Add(new
 223 |                     {
 224 |                         cid = cid,
 225 |                         name = def.Name,
 226 |                         students = sc,
 227 |                         assessments = cw,
 228 |                         submissions = subs,
 229 |                         markings = marks
 230 |                     });
 231 |                 }
 232 | 
 233 |                 try { Exec(conn, "UPDATE Enrollments SET Progress=40 WHERE Progress IS NULL"); } catch { }
 234 | 
 235 |                 Write(context, new
 236 |                 {
 237 |                     success = true,
 238 |                     message = "Seeded 3 courses for teacher " + teacherEmail + ". Log in as t@t.com and open My Courses.",
 239 |                     teacher = new
 240 |                     {
 241 |                         email = teacherEmail,
 242 |                         password = DefaultTeacherPassword,
 243 |                         uid = lecturerUid,
 244 |                         role = "Lecturer (2)"
 245 |                     },
 246 |                     coursesCreated = courseCreated,
 247 |                     courses = courseSummaries,
 248 |                     added = new
 249 |                     {
 250 |                         enrollments = enrollCount,
 251 |                         courseWorks = workCount,
 252 |                         submissions = subCount,
 253 |                         markings = markCount
 254 |                     },
 255 |                     students = new object[]
 256 |                     {
 257 |                         new { email = "student1@edulms.local", password = "Student123", name = "Alice Tan", uid = s1 },
 258 |                         new { email = "student2@edulms.local", password = "Student123", name = "Bob Lee", uid = s2 },
 259 |                         new { email = "student3@edulms.local", password = "Student123", name = "Cara Ng", uid = s3 },
 260 |                         new { email = "student4@edulms.local", password = "Student123", name = "Daniel Ong", uid = s4 },
 261 |                         new { email = "student5@edulms.local", password = "Student123", name = "Emily Wong", uid = s5 }
 262 |                     },
 263 |                     log = log
 264 |                 });
 265 |             }
 266 |         }
 267 |         catch (Exception ex)
 268 |         {
 269 |             Write(context, new { success = false, message = "Seed failed. Check server logs." });
 270 |         }
 271 |     }
```

---

### `EnsureTeacher` — lines 272–320

#### Signature

```html
private static int EnsureTeacher(SqlConnection conn, string email, string name, string password, List<string> log)
```

#### What it is

Makes sure **Teacher** exists or is valid before the rest of the code continues.

#### How it works

1. Hash the password with PBKDF2 before saving it.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `email` | `string` | Account email address (usually lowercased). |
| `name` | `string` | Display name of user/course/criterion. |
| `password` | `string` | Plain password from the form (never log this). |
| `log` | `List<string>` | Holds “log” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `hash` | `string` | Password hash (PBKDF2) stored in DB.  Assigned from password hash function. |

#### Code

```html
 272 | 
 273 |     private static int EnsureTeacher(SqlConnection conn, string email, string name, string password, List<string> log)
 274 |     {
 275 |         int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));
 276 |         if (uid > 0)
 277 |         {
 278 |             try
 279 |             {
 280 |                 Exec(conn, "UPDATE Users SET Role=N'2', Name=ISNULL(NULLIF(LTRIM(RTRIM(Name)),N''),@N) WHERE UID=@UID",
 281 |                     P("@UID", uid), P("@N", name));
 282 |             }
 283 |             catch
 284 |             {
 285 |                 try { Exec(conn, "UPDATE Users SET Role=N'2' WHERE UID=@UID", P("@UID", uid)); } catch { }
 286 |             }
 287 |             log.Add("Using existing teacher " + email + " UID=" + uid + " (Role=2).");
 288 |             return uid;
 289 |         }
 290 | 
 291 |         // Create lecturer
 292 |         try
 293 |         {
 294 |             string hash = PasswordHasher.Hash(password);
 295 |             try
 296 |             {
 297 |                 uid = ScalarInt(conn, @"
 298 | INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)
 299 | VALUES (@N, @E, @P, N'2', @H, 0);
 300 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 301 |                     P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));
 302 |             }
 303 |             catch
 304 |             {
 305 |                 uid = ScalarInt(conn, @"
 306 | INSERT INTO Users (Name, Email, Password, Role)
 307 | VALUES (@N, @E, @P, N'2');
 308 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 309 |                     P("@N", name), P("@E", email), P("@P", password));
 310 |             }
 311 |         }
 312 |         catch (Exception ex)
 313 |         {
 314 |             log.Add("Create teacher failed: " + ex.Message);
 315 |             return 0;
 316 |         }
 317 | 
 318 |         log.Add("Created teacher " + email + " UID=" + uid + " password=" + password);
 319 |         return uid;
 320 |     }
```

---

### `ClearMockStudentData` — lines 321–342

#### Signature

```html
private static void ClearMockStudentData(SqlConnection conn, List<string> log)
```

#### What it is

Deletes or clears **Clear Mock Student Data** (data or temporary state).

#### How it works

1. Starts when something calls `ClearMockStudentData`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `log` | `List<string>` | Holds “log” for this scope. (text) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```html
 321 | 
 322 |     private static void ClearMockStudentData(SqlConnection conn, List<string> log)
 323 |     {
 324 |         try
 325 |         {
 326 |             Exec(conn, @"
 327 | DELETE m FROM CWMarkings m
 328 | INNER JOIN CWSubmissions s ON s.SID = m.SID
 329 | INNER JOIN Users u ON u.UID = s.StudentUID
 330 | WHERE u.Email LIKE 'student%@edulms.local'");
 331 |             Exec(conn, @"
 332 | DELETE s FROM CWSubmissions s
 333 | INNER JOIN Users u ON u.UID = s.StudentUID
 334 | WHERE u.Email LIKE 'student%@edulms.local'");
 335 |             Exec(conn, @"
 336 | DELETE e FROM Enrollments e
 337 | INNER JOIN Users u ON u.UID = e.StudentUID
 338 | WHERE u.Email LIKE 'student%@edulms.local'");
 339 |             log.Add("Cleared prior mock enrollments/submissions for student*@edulms.local");
 340 |         }
 341 |         catch (Exception ex) { log.Add("Reset partial: " + ex.Message); }
 342 |     }
```

---

### `EnsureCourse` — lines 343–402

#### Signature

```html
private static int EnsureCourse(SqlConnection conn, int lecturerUid, MockCourseDef def, List<string> log, ref int created)
```

#### What it is

Makes sure **Course** exists or is valid before the rest of the code continues.

#### How it works

1. Starts when something calls `EnsureCourse`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `lecturerUid` | `int` | Users.UID of the course owner (lecturer). |
| `def` | `MockCourseDef` | Holds “def” for this scope. (type `MockCourseDef`) |
| `log` | `List<string>` | Holds “log” for this scope. (text) |
| `created` | `int` | Holds “created” for this scope. (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `int` | Course ID (Courses.CID). |

#### Code

```html
 343 | 
 344 |     private static int EnsureCourse(SqlConnection conn, int lecturerUid, MockCourseDef def, List<string> log, ref int created)
 345 |     {
 346 |         // Match by name + this lecturer
 347 |         int cid = ScalarInt(conn,
 348 |             "SELECT TOP 1 CID FROM Courses WHERE LecturerUID=@L AND Name=@N",
 349 |             P("@L", lecturerUid), P("@N", def.Name));
 350 |         if (cid > 0)
 351 |         {
 352 |             log.Add("Course already exists CID=" + cid + " \"" + def.Name + "\"");
 353 |             return cid;
 354 |         }
 355 | 
 356 |         try
 357 |         {
 358 |             cid = ScalarInt(conn, @"
 359 | INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level)
 360 | VALUES (@L, @N, @D, @R, N'', @Cat, @Lv);
 361 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 362 |                 P("@L", lecturerUid),
 363 |                 P("@N", def.Name),
 364 |                 P("@D", def.Description),
 365 |                 P("@R", def.Rating),
 366 |                 P("@Cat", def.Category),
 367 |                 P("@Lv", def.Level));
 368 |         }
 369 |         catch
 370 |         {
 371 |             try
 372 |             {
 373 |                 cid = ScalarInt(conn, @"
 374 | INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level, Status)
 375 | VALUES (@L, @N, @D, @R, N'', @Cat, @Lv, N'Published');
 376 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 377 |                     P("@L", lecturerUid),
 378 |                     P("@N", def.Name),
 379 |                     P("@D", def.Description),
 380 |                     P("@R", def.Rating),
 381 |                     P("@Cat", def.Category),
 382 |                     P("@Lv", def.Level));
 383 |             }
 384 |             catch
 385 |             {
 386 |                 cid = ScalarInt(conn, @"
 387 | INSERT INTO Courses (LecturerUID, Name, Description)
 388 | VALUES (@L, @N, @D);
 389 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 390 |                     P("@L", lecturerUid),
 391 |                     P("@N", def.Name),
 392 |                     P("@D", def.Description));
 393 |             }
 394 |         }
 395 | 
 396 |         if (cid > 0)
 397 |         {
 398 |             created++;
 399 |             log.Add("Created course CID=" + cid + " \"" + def.Name + "\" for LecturerUID=" + lecturerUid);
 400 |         }
 401 |         return cid;
 402 |     }
```

---

### `EnsureChapter` — lines 403–436

#### Signature

```html
private static int EnsureChapter(SqlConnection conn, int cid, string title)
```

#### What it is

Makes sure **Chapter** exists or is valid before the rest of the code continues.

#### How it works

1. Starts when something calls `EnsureChapter`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `cid` | `int` | Course ID (Courses.CID). |
| `title` | `string` | Title of course work / page heading. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `chid` | `int` | Chapter ID (Chapters.ChID). |
| `idx` | `int` | Holds “idx” for this scope. (integer) |

#### Code

```html
 403 | 
 404 |     private static int EnsureChapter(SqlConnection conn, int cid, string title)
 405 |     {
 406 |         int chid = ScalarInt(conn,
 407 |             "SELECT TOP 1 ChID FROM Chapters WHERE CID=@C AND Title=@T",
 408 |             P("@C", cid), P("@T", title));
 409 |         if (chid > 0) return chid;
 410 |         try
 411 |         {
 412 |             int idx = ScalarInt(conn, "SELECT ISNULL(MAX([Index]),0)+1 FROM Chapters WHERE CID=@C", P("@C", cid));
 413 |             chid = ScalarInt(conn, @"
 414 | INSERT INTO Chapters (CID, [Index], Title) VALUES (@C, @I, @T);
 415 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 416 |                 P("@C", cid), P("@I", idx), P("@T", title));
 417 |         }
 418 |         catch
 419 |         {
 420 |             try
 421 |             {
 422 |                 chid = ScalarInt(conn, @"
 423 | INSERT INTO Chapters (CID, Title, Description) VALUES (@C, @T, N'');
 424 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 425 |                     P("@C", cid), P("@T", title));
 426 |             }
 427 |             catch
 428 |             {
 429 |                 chid = ScalarInt(conn, @"
 430 | INSERT INTO Chapters (CID, Title) VALUES (@C, @T);
 431 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 432 |                     P("@C", cid), P("@T", title));
 433 |             }
 434 |         }
 435 |         return chid;
 436 |     }
```

---

### `EnsureEnrollment` — lines 437–458

#### Signature

```html
private static bool EnsureEnrollment(SqlConnection conn, int cid, int studentUid, int progress)
```

#### What it is

Makes sure **Enrollment** exists or is valid before the rest of the code continues.

#### How it works

1. Return `false` to the caller.
2. Return `true` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `cid` | `int` | Course ID (Courses.CID). |
| `studentUid` | `int` | Users.UID of the student. |
| `progress` | `int` | Often a collection related to progress (plural name). (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `exists` | `int` | Count > 0 check (email/user/row already exists). |

#### Code

```html
 437 | 
 438 |     private static bool EnsureEnrollment(SqlConnection conn, int cid, int studentUid, int progress)
 439 |     {
 440 |         int exists = ScalarInt(conn,
 441 |             "SELECT COUNT(1) FROM Enrollments WHERE CID=@C AND StudentUID=@S",
 442 |             P("@C", cid), P("@S", studentUid));
 443 |         if (exists > 0)
 444 |         {
 445 |             try
 446 |             {
 447 |                 Exec(conn,
 448 |                     "UPDATE Enrollments SET Progress=@P WHERE CID=@C AND StudentUID=@S AND (Progress IS NULL OR Progress=0)",
 449 |                     P("@C", cid), P("@S", studentUid), P("@P", progress));
 450 |             }
 451 |             catch { }
 452 |             return false;
 453 |         }
 454 |         Exec(conn,
 455 |             "INSERT INTO Enrollments (CID, StudentUID, Progress) VALUES (@C,@S,@P)",
 456 |             P("@C", cid), P("@S", studentUid), P("@P", progress));
 457 |         return true;
 458 |     }
```

---

### `EnsureGradeScales` — lines 459–480

#### Signature

```html
private static void EnsureGradeScales(SqlConnection conn, List<string> log)
```

#### What it is

Makes sure **Grade Scales** exists or is valid before the rest of the code continues.

#### How it works

1. Starts when something calls `EnsureGradeScales`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `log` | `List<string>` | Holds “log” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sql` | `—` | SQL query text (should use parameters, not raw user input). |

#### Code

```html
 459 | 
 460 |     private static void EnsureGradeScales(SqlConnection conn, List<string> log)
 461 |     {
 462 |         try
 463 |         {
 464 |             if (ScalarInt(conn, "SELECT COUNT(*) FROM GradeScales") > 0) return;
 465 |             string[] rows = {
 466 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A+', 90, 100)",
 467 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A', 80, 89)",
 468 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'B', 70, 79)",
 469 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'C', 60, 69)",
 470 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'D', 50, 59)",
 471 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'F', 0, 49)"
 472 |             };
 473 |             foreach (var sql in rows)
 474 |             {
 475 |                 try { Exec(conn, sql); } catch { }
 476 |             }
 477 |             log.Add("Inserted GradeScales defaults.");
 478 |         }
 479 |         catch { }
 480 |     }
```

---

### `EnsureStudent` — lines 481–513

#### Signature

```html
private static int EnsureStudent(SqlConnection conn, string name, string email, List<string> log)
```

#### What it is

Makes sure **Student** exists or is valid before the rest of the code continues.

#### How it works

1. Hash the password with PBKDF2 before saving it.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `name` | `string` | Display name of user/course/criterion. |
| `email` | `string` | Account email address (usually lowercased). |
| `log` | `List<string>` | Holds “log” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `hash` | `string` | Password hash (PBKDF2) stored in DB.  Assigned from password hash function. |

#### Code

```html
 481 | 
 482 |     private static int EnsureStudent(SqlConnection conn, string name, string email, List<string> log)
 483 |     {
 484 |         int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));
 485 |         if (uid > 0) return uid;
 486 |         try
 487 |         {
 488 |             string hash = PasswordHasher.Hash("Student123");
 489 |             try
 490 |             {
 491 |                 uid = ScalarInt(conn, @"
 492 | INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)
 493 | VALUES (@N, @E, @P, N'1', @H, 0);
 494 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 495 |                     P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));
 496 |             }
 497 |             catch
 498 |             {
 499 |                 uid = ScalarInt(conn, @"
 500 | INSERT INTO Users (Name, Email, Password, Role)
 501 | VALUES (@N, @E, @P, N'1');
 502 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 503 |                     P("@N", name), P("@E", email), P("@P", "Student123"));
 504 |             }
 505 |         }
 506 |         catch (Exception ex)
 507 |         {
 508 |             log.Add("Student create failed " + email + ": " + ex.Message);
 509 |             return 0;
 510 |         }
 511 |         log.Add("Created student " + email + " UID=" + uid);
 512 |         return uid;
 513 |     }
```

---

### `BuildCwDescription` — lines 516–531

#### Signature

```html
private static string BuildCwDescription(string instructions, string type, int score, bool requireFile)
```

#### What it is

Creates/builds **Build Cw Description** (object, string, secret, or UI content).

#### How it works

1. Use the assignment due date to decide if submissions are still open.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `instructions` | `string` | Student-facing assignment instructions (plain part of Description). |
| `type` | `string` | Holds “type” for this scope. (text) |
| `score` | `int` | Points earned or max points depending on context. |
| `requireFile` | `bool` | Assignment requires a file upload. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `extra` | `var` | Dictionary of optional fields inside META.  Newly constructed object. |
| `payload` | `var` | Object about to be JSON-serialized or sent over network.  Newly constructed object. |

#### Code

```html
 516 |     private static string BuildCwDescription(string instructions, string type, int score, bool requireFile)
 517 |     {
 518 |         var extra = new Dictionary<string, object>
 519 |         {
 520 |             { "requireFile", requireFile },
 521 |             { "dueDate", null }
 522 |         };
 523 |         var payload = new Dictionary<string, object>
 524 |         {
 525 |             { "instructions", instructions ?? "" },
 526 |             { "type", type ?? "Text" },
 527 |             { "score", score },
 528 |             { "extra", extra }
 529 |         };
 530 |         return (instructions ?? "") + "\n<<<META>>>" + Json.Serialize(payload) + "<<<END>>>";
 531 |     }
```

---

### `EnsureCourseWork` — lines 532–558

#### Signature

```html
private static int EnsureCourseWork(SqlConnection conn, int chid, string title, string desc, DateTime due, ref int workCount)
```

#### What it is

Makes sure **Course Work** exists or is valid before the rest of the code continues.

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Use the assignment due date to decide if submissions are still open.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `chid` | `int` | Chapter ID (Chapters.ChID). |
| `title` | `string` | Title of course work / page heading. |
| `desc` | `string` | Description text (may embed <<<META>>> JSON). |
| `due` | `DateTime` | Holds “due” for this scope. (date/time) |
| `workCount` | `int` | Numeric count of items related to `work Count`. (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `int` | CourseWork ID (assignment) (CourseWorks.CWID). |

#### Code

```html
 532 | 
 533 |     private static int EnsureCourseWork(SqlConnection conn, int chid, string title, string desc, DateTime due, ref int workCount)
 534 |     {
 535 |         if (chid <= 0) return 0;
 536 |         int cwid = ScalarInt(conn,
 537 |             "SELECT TOP 1 CWID FROM CourseWorks WHERE ChID=@Ch AND Title=@T",
 538 |             P("@Ch", chid), P("@T", title));
 539 |         if (cwid > 0) return cwid;
 540 |         try
 541 |         {
 542 |             cwid = ScalarInt(conn, @"
 543 | INSERT INTO CourseWorks (ChID, Title, Description, DueDate)
 544 | VALUES (@Ch, @T, @D, @Due);
 545 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 546 |                 P("@Ch", chid), P("@T", title), P("@D", desc), P("@Due", due));
 547 |         }
 548 |         catch
 549 |         {
 550 |             cwid = ScalarInt(conn, @"
 551 | INSERT INTO CourseWorks (ChID, Title, Description)
 552 | VALUES (@Ch, @T, @D);
 553 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 554 |                 P("@Ch", chid), P("@T", title), P("@D", desc));
 555 |         }
 556 |         if (cwid > 0) workCount++;
 557 |         return cwid;
 558 |     }
```

---

### `EnsureSubmission` — lines 559–589

#### Signature

```html
private static int EnsureSubmission(SqlConnection conn, int cwid, int studentUid, string content, DateTime when, ref int subCount)
```

#### What it is

Makes sure **Submission** exists or is valid before the rest of the code continues.

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `cwid` | `int` | CourseWork ID (assignment) (CourseWorks.CWID). |
| `studentUid` | `int` | Users.UID of the student. |
| `content` | `string` | Submission body text or JSON payload in CWSubmissions. |
| `when` | `DateTime` | Holds “when” for this scope. (date/time) |
| `subCount` | `int` | Numeric count of items related to `sub Count`. (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sid` | `int` | Submission ID (CWSubmissions.SID). |

#### Code

```html
 559 | 
 560 |     private static int EnsureSubmission(SqlConnection conn, int cwid, int studentUid, string content, DateTime when, ref int subCount)
 561 |     {
 562 |         if (cwid <= 0 || studentUid <= 0) return 0;
 563 |         int sid = ScalarInt(conn,
 564 |             "SELECT TOP 1 SID FROM CWSubmissions WHERE CWID=@C AND StudentUID=@S ORDER BY SID DESC",
 565 |             P("@C", cwid), P("@S", studentUid));
 566 |         if (sid > 0) return sid;
 567 |         try
 568 |         {
 569 |             sid = ScalarInt(conn, @"
 570 | INSERT INTO CWSubmissions (CWID, StudentUID, SubmissionDate, Content)
 571 | VALUES (@C, @S, @When, @Content);
 572 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 573 |                 P("@C", cwid), P("@S", studentUid), P("@When", when), P("@Content", content));
 574 |         }
 575 |         catch
 576 |         {
 577 |             try
 578 |             {
 579 |                 sid = ScalarInt(conn, @"
 580 | INSERT INTO CWSubmissions (CWID, StudentUID, Content)
 581 | VALUES (@C, @S, @Content);
 582 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 583 |                     P("@C", cwid), P("@S", studentUid), P("@Content", content));
 584 |             }
 585 |             catch { return 0; }
 586 |         }
 587 |         if (sid > 0) subCount++;
 588 |         return sid;
 589 |     }
```

---

### `EnsureMarking` — lines 590–612

#### Signature

```html
private static bool EnsureMarking(SqlConnection conn, int sid, int score, string feedback, ref int markCount)
```

#### What it is

Makes sure **Marking** exists or is valid before the rest of the code continues.

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Return `false` to the caller.
3. Return `true` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `sid` | `int` | Submission ID (CWSubmissions.SID). |
| `score` | `int` | Points earned or max points depending on context. |
| `feedback` | `string` | Holds “feedback” for this scope. (text) |
| `markCount` | `int` | Numeric count of items related to `mark Count`. (integer) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```html
 590 | 
 591 |     private static bool EnsureMarking(SqlConnection conn, int sid, int score, string feedback, ref int markCount)
 592 |     {
 593 |         if (sid <= 0) return false;
 594 |         if (ScalarInt(conn, "SELECT COUNT(1) FROM CWMarkings WHERE SID=@S", P("@S", sid)) > 0)
 595 |             return false;
 596 |         try
 597 |         {
 598 |             Exec(conn, "INSERT INTO CWMarkings (SID, Marks, Feedback) VALUES (@S, @Sc, @R)",
 599 |                 P("@S", sid), P("@Sc", score), P("@R", feedback ?? ""));
 600 |         }
 601 |         catch
 602 |         {
 603 |             try
 604 |             {
 605 |                 Exec(conn, "INSERT INTO CWMarkings (SID, Marks) VALUES (@S, @Sc)",
 606 |                     P("@S", sid), P("@Sc", score));
 607 |             }
 608 |             catch { return false; }
 609 |         }
 610 |         markCount++;
 611 |         return true;
 612 |     }
```

---

### `P` — lines 613–617

#### Signature

```html
private static SqlParameter P(string n, object v)
```

#### What it is

Creates one SQL parameter (`@Name` + value) so user input is never concatenated into SQL.

#### How it works

1. Starts when something calls `P`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `n` | `string` | Numeric count or temporary integer. |
| `v` | `object` | Generic value (version flag in JSON, or loop value). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```html
 613 | 
 614 |     private static SqlParameter P(string n, object v)
 615 |     {
 616 |         return new SqlParameter(n, v ?? DBNull.Value);
 617 |     }
```

---

### `Exec` — lines 618–626

#### Signature

```html
private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### What it is

Function `Exec` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `ps` | `SqlParameter[]` | Holds “ps” for this scope. (type `SqlParameter[]`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |

#### Code

```html
 618 | 
 619 |     private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
 620 |     {
 621 |         using (var cmd = new SqlCommand(sql, conn))
 622 |         {
 623 |             if (ps != null) cmd.Parameters.AddRange(ps);
 624 |             cmd.ExecuteNonQuery();
 625 |         }
 626 |     }
```

---

### `ScalarInt` — lines 627–637

#### Signature

```html
private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### What it is

Function `ScalarInt` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `ps` | `SqlParameter[]` | Holds “ps” for this scope. (type `SqlParameter[]`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |
| `o` | `var` | Holds “o” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY). |

#### Code

```html
 627 | 
 628 |     private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)
 629 |     {
 630 |         using (var cmd = new SqlCommand(sql, conn))
 631 |         {
 632 |             if (ps != null) cmd.Parameters.AddRange(ps);
 633 |             var o = cmd.ExecuteScalar();
 634 |             if (o == null || o == DBNull.Value) return 0;
 635 |             return Convert.ToInt32(o);
 636 |         }
 637 |     }
```

---

### `Write` — lines 638–642

#### Signature

```html
private static void Write(HttpContext ctx, object o)
```

#### What it is

Function `Write` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Write the HTTP response body (JSON, file bytes, or text).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `o` | `object` | Holds “o” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```html
 638 | 
 639 |     private static void Write(HttpContext ctx, object o)
 640 |     {
 641 |         ctx.Response.Write(Json.Serialize(o));
 642 |     }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ WebHandler Language="C#" Class="SeedMockData" %>
   2 | 
   3 | using System;
   4 | using System.Collections.Generic;
   5 | using System.Data;
   6 | using System.Data.SqlClient;
   7 | using System.Web;
   8 | using System.Web.Script.Serialization;
   9 | using System.Configuration;
  10 | using System.Web.SessionState;
  11 | using WebAppAssignment.Data;
  12 | using WebAppAssignment.Data.Security;
  13 | 
  14 | /// <summary>
  15 | /// Seeds mock courses for teacher t@t.com + students + enrollments + assessments.
  16 | ///
  17 | /// GET /Pages/Lecturer/SeedMockData.ashx
  18 | /// Optional:
  19 | ///   ?email=t@t.com     (default teacher)
  20 | ///   ?reset=1           clear prior mock student enrollments/submissions
  21 | ///
  22 | /// Requires Lecturer or Admin session. Disabled unless compilation debug
  23 | /// or appSetting AllowSeedMockData=true.
  24 | /// </summary>
  25 | public class SeedMockData : IHttpHandler, IRequiresSessionState
  26 | {
  27 |     private static readonly JavaScriptSerializer Json = new JavaScriptSerializer();
  28 |     private const string DefaultTeacherEmail = "t@t.com";
  29 |     private const string DefaultTeacherPassword = "Teacher123";
  30 | 
  31 |     private static bool IsSeedAllowed()
  32 |     {
  33 |         string allow = ConfigurationManager.AppSettings["AllowSeedMockData"];
  34 |         if (string.Equals(allow, "true", StringComparison.OrdinalIgnoreCase)) return true;
  35 |         if (string.Equals(allow, "false", StringComparison.OrdinalIgnoreCase)) return false;
  36 |         // default: only when compilation debug
  37 |         try
  38 |         {
  39 |             return HttpContext.Current != null
  40 |                 && HttpContext.Current.IsDebuggingEnabled;
  41 |         }
  42 |         catch { return false; }
  43 |     }
  44 | 
  45 |     private class MockCourseDef
  46 |     {
  47 |         public string Name;
  48 |         public string Description;
  49 |         public string Category;
  50 |         public string Level;
  51 |         public decimal Rating;
  52 |         public string[] Chapters;
  53 |     }
  54 | 
  55 |     public void ProcessRequest(HttpContext context)
  56 |     {
  57 |         context.Response.ContentType = "application/json; charset=utf-8";
  58 |         context.Response.Cache.SetCacheability(HttpCacheability.NoCache);
  59 | 
  60 |         try
  61 |         {
  62 |             if (!IsSeedAllowed())
  63 |             {
  64 |                 AuthGate.WriteHandlerError(context, 403, "Seed endpoint is disabled. Set AllowSeedMockData=true in Web.config (debug only).");
  65 |                 return;
  66 |             }
  67 | 
  68 |             int uid;
  69 |             if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin"))
  70 |                 return;
  71 | 
  72 |             SecurityAudit.Log("seed.start", uid, "email=" + (context.Request["email"] ?? DefaultTeacherEmail));
  73 | 
  74 |             string teacherEmail = (context.Request["email"] ?? DefaultTeacherEmail).Trim().ToLowerInvariant();
  75 |             if (string.IsNullOrEmpty(teacherEmail)) teacherEmail = DefaultTeacherEmail;
  76 |             bool reset = context.Request["reset"] == "1";
  77 | 
  78 |             var log = new List<string>();
  79 |             var courseSummaries = new List<object>();
  80 | 
  81 |             using (var conn = DbHelper.OpenConnection())
  82 |             {
  83 |                 if (reset) ClearMockStudentData(conn, log);
  84 | 
  85 |                 // ── Teacher 1: t@t.com ────────────────────────────────────
  86 |                 int lecturerUid = EnsureTeacher(conn, teacherEmail, "Teacher One", DefaultTeacherPassword, log);
  87 |                 if (lecturerUid <= 0)
  88 |                 {
  89 |                     Write(context, new { success = false, message = "Could not create/find teacher " + teacherEmail });
  90 |                     return;
  91 |                 }
  92 | 
  93 |                 // ── Students ──────────────────────────────────────────────
  94 |                 int s1 = EnsureStudent(conn, "Alice Tan", "student1@edulms.local", log);
  95 |                 int s2 = EnsureStudent(conn, "Bob Lee", "student2@edulms.local", log);
  96 |                 int s3 = EnsureStudent(conn, "Cara Ng", "student3@edulms.local", log);
  97 |                 int s4 = EnsureStudent(conn, "Daniel Ong", "student4@edulms.local", log);
  98 |                 int s5 = EnsureStudent(conn, "Emily Wong", "student5@edulms.local", log);
  99 |                 var studentIds = new List<int> { s1, s2, s3, s4, s5 };
 100 | 
 101 |                 EnsureGradeScales(conn, log);
 102 | 
 103 |                 // ── 3 courses owned by t@t.com ────────────────────────────
 104 |                 var defs = new[]
 105 |                 {
 106 |                     new MockCourseDef
 107 |                     {
 108 |                         Name = "Product Design Fundamentals",
 109 |                         Description = "UI/UX basics, wireframes, and design critique for beginners.",
 110 |                         Category = "Design",
 111 |                         Level = "Beginner",
 112 |                         Rating = 4.3m,
 113 |                         Chapters = new[] { "Intro & Tools", "Wireframing", "Assessments" }
 114 |                     },
 115 |                     new MockCourseDef
 116 |                     {
 117 |                         Name = "Web App Programming",
 118 |                         Description = "ASP.NET Web Forms, pure SQL, and auth for EduLMS-style apps.",
 119 |                         Category = "Programming",
 120 |                         Level = "Intermediate",
 121 |                         Rating = 4.6m,
 122 |                         Chapters = new[] { "Web Forms Basics", "Data Access", "Assessments" }
 123 |                     },
 124 |                     new MockCourseDef
 125 |                     {
 126 |                         Name = "Database Essentials",
 127 |                         Description = "ER modelling, SQL queries, and LocalDB for coursework.",
 128 |                         Category = "Database",
 129 |                         Level = "Beginner",
 130 |                         Rating = 4.1m,
 131 |                         Chapters = new[] { "ER Diagrams", "SQL Queries", "Assessments" }
 132 |                     }
 133 |                 };
 134 | 
 135 |                 int enrollCount = 0, workCount = 0, subCount = 0, markCount = 0, courseCreated = 0;
 136 | 
 137 |                 foreach (var def in defs)
 138 |                 {
 139 |                     int cid = EnsureCourse(conn, lecturerUid, def, log, ref courseCreated);
 140 |                     if (cid <= 0)
 141 |                     {
 142 |                         log.Add("FAILED to create/find course: " + def.Name);
 143 |                         continue;
 144 |                     }
 145 | 
 146 |                     foreach (var chTitle in def.Chapters)
 147 |                         EnsureChapter(conn, cid, chTitle);
 148 | 
 149 |                     // Enroll all 5 students
 150 |                     int i = 0;
 151 |                     foreach (int stuid in studentIds)
 152 |                     {
 153 |                         int progress = 25 + ((stuid + i * 13) % 70);
 154 |                         if (EnsureEnrollment(conn, cid, stuid, progress))
 155 |                             enrollCount++;
 156 |                         i++;
 157 |                     }
 158 | 
 159 |                     int assessCh = EnsureChapter(conn, cid, "Assessments");
 160 | 
 161 |                     // Text-only, file-required, and mixed assessments
 162 |                     int cwid1 = EnsureCourseWork(conn, assessCh,
 163 |                         "Week 3 Written Task",
 164 |                         BuildCwDescription("Write a short reflection on the module materials.", "Text", 100, false),
 165 |                         DateTime.Today.AddDays(14), ref workCount);
 166 | 
 167 |                     int cwid2 = EnsureCourseWork(conn, assessCh,
 168 |                         "Midterm Quiz Pack",
 169 |                         BuildCwDescription("Answer all objective questions.", "Objective", 50, false),
 170 |                         DateTime.Today.AddDays(21), ref workCount);
 171 | 
 172 |                     // File-upload required — PDF essay
 173 |                     int cwid3 = EnsureCourseWork(conn, assessCh,
 174 |                         "PDF Essay Upload",
 175 |                         BuildCwDescription("Upload your essay as a PDF (file upload required). You may also add notes.", "File", 100, true),
 176 |                         DateTime.Today.AddDays(30), ref workCount);
 177 | 
 178 |                     foreach (int stuid in studentIds)
 179 |                     {
 180 |                         int sid1 = EnsureSubmission(conn, cwid1, stuid,
 181 |                             "Written answer from student " + stuid + " for " + def.Name + ".",
 182 |                             DateTime.Now.AddDays(-4), ref subCount);
 183 |                         if (sid1 > 0)
 184 |                             EnsureMarking(conn, sid1, 62 + (stuid % 30), "Solid effort — keep going.", ref markCount);
 185 | 
 186 |                         int sid2 = EnsureSubmission(conn, cwid2, stuid,
 187 |                             "Quiz answers A,C,B,D (student " + stuid + ").",
 188 |                             DateTime.Now.AddDays(-2), ref subCount);
 189 |                         // Leave odd UIDs ungraded for grading queue
 190 |                         if (sid2 > 0 && stuid % 2 == 0)
 191 |                             EnsureMarking(conn, sid2, 45 + (stuid % 40), "Quiz auto mock grade.", ref markCount);
 192 | 
 193 |                         // File-required assessment: store JSON content with a placeholder path
 194 |                         // (students re-upload a real PDF via Submit.aspx for full preview)
 195 |                         if (stuid % 3 != 0)
 196 |                         {
 197 |                             string fileJson = "{\"v\":1,\"text\":\"See attached essay PDF.\",\"file\":\"\",\"fileName\":\"essay-student-" + stuid + ".pdf\"}";
 198 |                             // Prefer real note-only until student uploads; mark require via assignment meta
 199 |                             EnsureSubmission(conn, cwid3, stuid,
 200 |                                 "Essay notes from student " + stuid + " — PDF should be uploaded via Submit page.",
 201 |                                 DateTime.Now.AddDays(-1), ref subCount);
 202 |                         }
 203 |                     }
 204 | 
 205 |                     int sc = ScalarInt(conn, "SELECT COUNT(*) FROM Enrollments WHERE CID=@C", P("@C", cid));
 206 |                     int cw = ScalarInt(conn, @"
 207 | SELECT COUNT(*) FROM CourseWorks cw
 208 | INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));
 209 |                     int subs = ScalarInt(conn, @"
 210 | SELECT COUNT(*) FROM CWSubmissions s
 211 | INNER JOIN CourseWorks cw ON cw.CWID = s.CWID
 212 | INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));
 213 |                     int marks = ScalarInt(conn, @"
 214 | SELECT COUNT(*) FROM CWMarkings m
 215 | INNER JOIN CWSubmissions s ON s.SID = m.SID
 216 | INNER JOIN CourseWorks cw ON cw.CWID = s.CWID
 217 | INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));
 218 | 
 219 |                     log.Add(string.Format("CID={0} \"{1}\" students={2} assessments={3} submissions={4} markings={5}",
 220 |                         cid, def.Name, sc, cw, subs, marks));
 221 | 
 222 |                     courseSummaries.Add(new
 223 |                     {
 224 |                         cid = cid,
 225 |                         name = def.Name,
 226 |                         students = sc,
 227 |                         assessments = cw,
 228 |                         submissions = subs,
 229 |                         markings = marks
 230 |                     });
 231 |                 }
 232 | 
 233 |                 try { Exec(conn, "UPDATE Enrollments SET Progress=40 WHERE Progress IS NULL"); } catch { }
 234 | 
 235 |                 Write(context, new
 236 |                 {
 237 |                     success = true,
 238 |                     message = "Seeded 3 courses for teacher " + teacherEmail + ". Log in as t@t.com and open My Courses.",
 239 |                     teacher = new
 240 |                     {
 241 |                         email = teacherEmail,
 242 |                         password = DefaultTeacherPassword,
 243 |                         uid = lecturerUid,
 244 |                         role = "Lecturer (2)"
 245 |                     },
 246 |                     coursesCreated = courseCreated,
 247 |                     courses = courseSummaries,
 248 |                     added = new
 249 |                     {
 250 |                         enrollments = enrollCount,
 251 |                         courseWorks = workCount,
 252 |                         submissions = subCount,
 253 |                         markings = markCount
 254 |                     },
 255 |                     students = new object[]
 256 |                     {
 257 |                         new { email = "student1@edulms.local", password = "Student123", name = "Alice Tan", uid = s1 },
 258 |                         new { email = "student2@edulms.local", password = "Student123", name = "Bob Lee", uid = s2 },
 259 |                         new { email = "student3@edulms.local", password = "Student123", name = "Cara Ng", uid = s3 },
 260 |                         new { email = "student4@edulms.local", password = "Student123", name = "Daniel Ong", uid = s4 },
 261 |                         new { email = "student5@edulms.local", password = "Student123", name = "Emily Wong", uid = s5 }
 262 |                     },
 263 |                     log = log
 264 |                 });
 265 |             }
 266 |         }
 267 |         catch (Exception ex)
 268 |         {
 269 |             Write(context, new { success = false, message = "Seed failed. Check server logs." });
 270 |         }
 271 |     }
 272 | 
 273 |     private static int EnsureTeacher(SqlConnection conn, string email, string name, string password, List<string> log)
 274 |     {
 275 |         int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));
 276 |         if (uid > 0)
 277 |         {
 278 |             try
 279 |             {
 280 |                 Exec(conn, "UPDATE Users SET Role=N'2', Name=ISNULL(NULLIF(LTRIM(RTRIM(Name)),N''),@N) WHERE UID=@UID",
 281 |                     P("@UID", uid), P("@N", name));
 282 |             }
 283 |             catch
 284 |             {
 285 |                 try { Exec(conn, "UPDATE Users SET Role=N'2' WHERE UID=@UID", P("@UID", uid)); } catch { }
 286 |             }
 287 |             log.Add("Using existing teacher " + email + " UID=" + uid + " (Role=2).");
 288 |             return uid;
 289 |         }
 290 | 
 291 |         // Create lecturer
 292 |         try
 293 |         {
 294 |             string hash = PasswordHasher.Hash(password);
 295 |             try
 296 |             {
 297 |                 uid = ScalarInt(conn, @"
 298 | INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)
 299 | VALUES (@N, @E, @P, N'2', @H, 0);
 300 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 301 |                     P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));
 302 |             }
 303 |             catch
 304 |             {
 305 |                 uid = ScalarInt(conn, @"
 306 | INSERT INTO Users (Name, Email, Password, Role)
 307 | VALUES (@N, @E, @P, N'2');
 308 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 309 |                     P("@N", name), P("@E", email), P("@P", password));
 310 |             }
 311 |         }
 312 |         catch (Exception ex)
 313 |         {
 314 |             log.Add("Create teacher failed: " + ex.Message);
 315 |             return 0;
 316 |         }
 317 | 
 318 |         log.Add("Created teacher " + email + " UID=" + uid + " password=" + password);
 319 |         return uid;
 320 |     }
 321 | 
 322 |     private static void ClearMockStudentData(SqlConnection conn, List<string> log)
 323 |     {
 324 |         try
 325 |         {
 326 |             Exec(conn, @"
 327 | DELETE m FROM CWMarkings m
 328 | INNER JOIN CWSubmissions s ON s.SID = m.SID
 329 | INNER JOIN Users u ON u.UID = s.StudentUID
 330 | WHERE u.Email LIKE 'student%@edulms.local'");
 331 |             Exec(conn, @"
 332 | DELETE s FROM CWSubmissions s
 333 | INNER JOIN Users u ON u.UID = s.StudentUID
 334 | WHERE u.Email LIKE 'student%@edulms.local'");
 335 |             Exec(conn, @"
 336 | DELETE e FROM Enrollments e
 337 | INNER JOIN Users u ON u.UID = e.StudentUID
 338 | WHERE u.Email LIKE 'student%@edulms.local'");
 339 |             log.Add("Cleared prior mock enrollments/submissions for student*@edulms.local");
 340 |         }
 341 |         catch (Exception ex) { log.Add("Reset partial: " + ex.Message); }
 342 |     }
 343 | 
 344 |     private static int EnsureCourse(SqlConnection conn, int lecturerUid, MockCourseDef def, List<string> log, ref int created)
 345 |     {
 346 |         // Match by name + this lecturer
 347 |         int cid = ScalarInt(conn,
 348 |             "SELECT TOP 1 CID FROM Courses WHERE LecturerUID=@L AND Name=@N",
 349 |             P("@L", lecturerUid), P("@N", def.Name));
 350 |         if (cid > 0)
 351 |         {
 352 |             log.Add("Course already exists CID=" + cid + " \"" + def.Name + "\"");
 353 |             return cid;
 354 |         }
 355 | 
 356 |         try
 357 |         {
 358 |             cid = ScalarInt(conn, @"
 359 | INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level)
 360 | VALUES (@L, @N, @D, @R, N'', @Cat, @Lv);
 361 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 362 |                 P("@L", lecturerUid),
 363 |                 P("@N", def.Name),
 364 |                 P("@D", def.Description),
 365 |                 P("@R", def.Rating),
 366 |                 P("@Cat", def.Category),
 367 |                 P("@Lv", def.Level));
 368 |         }
 369 |         catch
 370 |         {
 371 |             try
 372 |             {
 373 |                 cid = ScalarInt(conn, @"
 374 | INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level, Status)
 375 | VALUES (@L, @N, @D, @R, N'', @Cat, @Lv, N'Published');
 376 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 377 |                     P("@L", lecturerUid),
 378 |                     P("@N", def.Name),
 379 |                     P("@D", def.Description),
 380 |                     P("@R", def.Rating),
 381 |                     P("@Cat", def.Category),
 382 |                     P("@Lv", def.Level));
 383 |             }
 384 |             catch
 385 |             {
 386 |                 cid = ScalarInt(conn, @"
 387 | INSERT INTO Courses (LecturerUID, Name, Description)
 388 | VALUES (@L, @N, @D);
 389 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 390 |                     P("@L", lecturerUid),
 391 |                     P("@N", def.Name),
 392 |                     P("@D", def.Description));
 393 |             }
 394 |         }
 395 | 
 396 |         if (cid > 0)
 397 |         {
 398 |             created++;
 399 |             log.Add("Created course CID=" + cid + " \"" + def.Name + "\" for LecturerUID=" + lecturerUid);
 400 |         }
 401 |         return cid;
 402 |     }
 403 | 
 404 |     private static int EnsureChapter(SqlConnection conn, int cid, string title)
 405 |     {
 406 |         int chid = ScalarInt(conn,
 407 |             "SELECT TOP 1 ChID FROM Chapters WHERE CID=@C AND Title=@T",
 408 |             P("@C", cid), P("@T", title));
 409 |         if (chid > 0) return chid;
 410 |         try
 411 |         {
 412 |             int idx = ScalarInt(conn, "SELECT ISNULL(MAX([Index]),0)+1 FROM Chapters WHERE CID=@C", P("@C", cid));
 413 |             chid = ScalarInt(conn, @"
 414 | INSERT INTO Chapters (CID, [Index], Title) VALUES (@C, @I, @T);
 415 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 416 |                 P("@C", cid), P("@I", idx), P("@T", title));
 417 |         }
 418 |         catch
 419 |         {
 420 |             try
 421 |             {
 422 |                 chid = ScalarInt(conn, @"
 423 | INSERT INTO Chapters (CID, Title, Description) VALUES (@C, @T, N'');
 424 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 425 |                     P("@C", cid), P("@T", title));
 426 |             }
 427 |             catch
 428 |             {
 429 |                 chid = ScalarInt(conn, @"
 430 | INSERT INTO Chapters (CID, Title) VALUES (@C, @T);
 431 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 432 |                     P("@C", cid), P("@T", title));
 433 |             }
 434 |         }
 435 |         return chid;
 436 |     }
 437 | 
 438 |     private static bool EnsureEnrollment(SqlConnection conn, int cid, int studentUid, int progress)
 439 |     {
 440 |         int exists = ScalarInt(conn,
 441 |             "SELECT COUNT(1) FROM Enrollments WHERE CID=@C AND StudentUID=@S",
 442 |             P("@C", cid), P("@S", studentUid));
 443 |         if (exists > 0)
 444 |         {
 445 |             try
 446 |             {
 447 |                 Exec(conn,
 448 |                     "UPDATE Enrollments SET Progress=@P WHERE CID=@C AND StudentUID=@S AND (Progress IS NULL OR Progress=0)",
 449 |                     P("@C", cid), P("@S", studentUid), P("@P", progress));
 450 |             }
 451 |             catch { }
 452 |             return false;
 453 |         }
 454 |         Exec(conn,
 455 |             "INSERT INTO Enrollments (CID, StudentUID, Progress) VALUES (@C,@S,@P)",
 456 |             P("@C", cid), P("@S", studentUid), P("@P", progress));
 457 |         return true;
 458 |     }
 459 | 
 460 |     private static void EnsureGradeScales(SqlConnection conn, List<string> log)
 461 |     {
 462 |         try
 463 |         {
 464 |             if (ScalarInt(conn, "SELECT COUNT(*) FROM GradeScales") > 0) return;
 465 |             string[] rows = {
 466 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A+', 90, 100)",
 467 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A', 80, 89)",
 468 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'B', 70, 79)",
 469 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'C', 60, 69)",
 470 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'D', 50, 59)",
 471 |                 "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'F', 0, 49)"
 472 |             };
 473 |             foreach (var sql in rows)
 474 |             {
 475 |                 try { Exec(conn, sql); } catch { }
 476 |             }
 477 |             log.Add("Inserted GradeScales defaults.");
 478 |         }
 479 |         catch { }
 480 |     }
 481 | 
 482 |     private static int EnsureStudent(SqlConnection conn, string name, string email, List<string> log)
 483 |     {
 484 |         int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));
 485 |         if (uid > 0) return uid;
 486 |         try
 487 |         {
 488 |             string hash = PasswordHasher.Hash("Student123");
 489 |             try
 490 |             {
 491 |                 uid = ScalarInt(conn, @"
 492 | INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)
 493 | VALUES (@N, @E, @P, N'1', @H, 0);
 494 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 495 |                     P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));
 496 |             }
 497 |             catch
 498 |             {
 499 |                 uid = ScalarInt(conn, @"
 500 | INSERT INTO Users (Name, Email, Password, Role)
 501 | VALUES (@N, @E, @P, N'1');
 502 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 503 |                     P("@N", name), P("@E", email), P("@P", "Student123"));
 504 |             }
 505 |         }
 506 |         catch (Exception ex)
 507 |         {
 508 |             log.Add("Student create failed " + email + ": " + ex.Message);
 509 |             return 0;
 510 |         }
 511 |         log.Add("Created student " + email + " UID=" + uid);
 512 |         return uid;
 513 |     }
 514 | 
 515 |     /// <summary>Pack description meta so Submit.aspx reads requireFile + type.</summary>
 516 |     private static string BuildCwDescription(string instructions, string type, int score, bool requireFile)
 517 |     {
 518 |         var extra = new Dictionary<string, object>
 519 |         {
 520 |             { "requireFile", requireFile },
 521 |             { "dueDate", null }
 522 |         };
 523 |         var payload = new Dictionary<string, object>
 524 |         {
 525 |             { "instructions", instructions ?? "" },
 526 |             { "type", type ?? "Text" },
 527 |             { "score", score },
 528 |             { "extra", extra }
 529 |         };
 530 |         return (instructions ?? "") + "\n<<<META>>>" + Json.Serialize(payload) + "<<<END>>>";
 531 |     }
 532 | 
 533 |     private static int EnsureCourseWork(SqlConnection conn, int chid, string title, string desc, DateTime due, ref int workCount)
 534 |     {
 535 |         if (chid <= 0) return 0;
 536 |         int cwid = ScalarInt(conn,
 537 |             "SELECT TOP 1 CWID FROM CourseWorks WHERE ChID=@Ch AND Title=@T",
 538 |             P("@Ch", chid), P("@T", title));
 539 |         if (cwid > 0) return cwid;
 540 |         try
 541 |         {
 542 |             cwid = ScalarInt(conn, @"
 543 | INSERT INTO CourseWorks (ChID, Title, Description, DueDate)
 544 | VALUES (@Ch, @T, @D, @Due);
 545 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 546 |                 P("@Ch", chid), P("@T", title), P("@D", desc), P("@Due", due));
 547 |         }
 548 |         catch
 549 |         {
 550 |             cwid = ScalarInt(conn, @"
 551 | INSERT INTO CourseWorks (ChID, Title, Description)
 552 | VALUES (@Ch, @T, @D);
 553 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 554 |                 P("@Ch", chid), P("@T", title), P("@D", desc));
 555 |         }
 556 |         if (cwid > 0) workCount++;
 557 |         return cwid;
 558 |     }
 559 | 
 560 |     private static int EnsureSubmission(SqlConnection conn, int cwid, int studentUid, string content, DateTime when, ref int subCount)
 561 |     {
 562 |         if (cwid <= 0 || studentUid <= 0) return 0;
 563 |         int sid = ScalarInt(conn,
 564 |             "SELECT TOP 1 SID FROM CWSubmissions WHERE CWID=@C AND StudentUID=@S ORDER BY SID DESC",
 565 |             P("@C", cwid), P("@S", studentUid));
 566 |         if (sid > 0) return sid;
 567 |         try
 568 |         {
 569 |             sid = ScalarInt(conn, @"
 570 | INSERT INTO CWSubmissions (CWID, StudentUID, SubmissionDate, Content)
 571 | VALUES (@C, @S, @When, @Content);
 572 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 573 |                 P("@C", cwid), P("@S", studentUid), P("@When", when), P("@Content", content));
 574 |         }
 575 |         catch
 576 |         {
 577 |             try
 578 |             {
 579 |                 sid = ScalarInt(conn, @"
 580 | INSERT INTO CWSubmissions (CWID, StudentUID, Content)
 581 | VALUES (@C, @S, @Content);
 582 | SELECT CAST(SCOPE_IDENTITY() AS INT);",
 583 |                     P("@C", cwid), P("@S", studentUid), P("@Content", content));
 584 |             }
 585 |             catch { return 0; }
 586 |         }
 587 |         if (sid > 0) subCount++;
 588 |         return sid;
 589 |     }
 590 | 
 591 |     private static bool EnsureMarking(SqlConnection conn, int sid, int score, string feedback, ref int markCount)
 592 |     {
 593 |         if (sid <= 0) return false;
 594 |         if (ScalarInt(conn, "SELECT COUNT(1) FROM CWMarkings WHERE SID=@S", P("@S", sid)) > 0)
 595 |             return false;
 596 |         try
 597 |         {
 598 |             Exec(conn, "INSERT INTO CWMarkings (SID, Marks, Feedback) VALUES (@S, @Sc, @R)",
 599 |                 P("@S", sid), P("@Sc", score), P("@R", feedback ?? ""));
 600 |         }
 601 |         catch
 602 |         {
 603 |             try
 604 |             {
 605 |                 Exec(conn, "INSERT INTO CWMarkings (SID, Marks) VALUES (@S, @Sc)",
 606 |                     P("@S", sid), P("@Sc", score));
 607 |             }
 608 |             catch { return false; }
 609 |         }
 610 |         markCount++;
 611 |         return true;
 612 |     }
 613 | 
 614 |     private static SqlParameter P(string n, object v)
 615 |     {
 616 |         return new SqlParameter(n, v ?? DBNull.Value);
 617 |     }
 618 | 
 619 |     private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
 620 |     {
 621 |         using (var cmd = new SqlCommand(sql, conn))
 622 |         {
 623 |             if (ps != null) cmd.Parameters.AddRange(ps);
 624 |             cmd.ExecuteNonQuery();
 625 |         }
 626 |     }
 627 | 
 628 |     private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)
 629 |     {
 630 |         using (var cmd = new SqlCommand(sql, conn))
 631 |         {
 632 |             if (ps != null) cmd.Parameters.AddRange(ps);
 633 |             var o = cmd.ExecuteScalar();
 634 |             if (o == null || o == DBNull.Value) return 0;
 635 |             return Convert.ToInt32(o);
 636 |         }
 637 |     }
 638 | 
 639 |     private static void Write(HttpContext ctx, object o)
 640 |     {
 641 |         ctx.Response.Write(Json.Serialize(o));
 642 |     }
 643 | 
 644 |     public bool IsReusable { get { return false; } }
 645 | }
```
