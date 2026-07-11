# SeedMockData.ashx
**Source:** `Pages/Lecturer/SeedMockData.ashx`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 645
- **Kind:** `.ashx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (17 found)

### `IsSeedAllowed` — lines 30–43

```
private static bool IsSeedAllowed()
```

#### Explanation

- **Purpose:** Implements `IsSeedAllowed`.
- **Local variables:** `allow`

#### Line-by-line (this function)

`  30`  ``
`  31`  `    private static bool IsSeedAllowed()`
`  32`  `    {`
`  33`  `        string allow = ConfigurationManager.AppSettings["AllowSeedMockData"];`
`  34`  `        if (string.Equals(allow, "true", StringComparison.OrdinalIgnoreCase)) return true;`
`  35`  `        if (string.Equals(allow, "false", StringComparison.OrdinalIgnoreCase)) return false;`
`  36`  `        // default: only when compilation debug`
`  37`  `        try`
  - → Error handling block.
`  38`  `        {`
`  39`  `            return HttpContext.Current != null`
`  40`  `                && HttpContext.Current.IsDebuggingEnabled;`
`  41`  `        }`
`  42`  `        catch { return false; }`
  - → Handle/log exception.
`  43`  `    }`

---

### `ProcessRequest` — lines 54–271

```
public void ProcessRequest(HttpContext context)
```

#### Explanation

- **Purpose:** Implements `ProcessRequest`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext context`
- **Local variables:** `teacherEmail`, `reset`, `log`, `courseSummaries`, `conn`, `lecturerUid`, `s1`, `s2`, `s3`, `s4`, `s5`, `studentIds`, `defs`, `enrollCount`, `cid`, `i`, `progress`, `assessCh`, `cwid1`, `cwid2`, `cwid3`, `sid1`, `sid2`, `fileJson`, `sc`, `cw`, `subs`, `marks`

#### Line-by-line (this function)

`  54`  ``
`  55`  `    public void ProcessRequest(HttpContext context)`
  - → IHttpHandler entry for ashx.
`  56`  `    {`
`  57`  `        context.Response.ContentType = "application/json; charset=utf-8";`
`  58`  `        context.Response.Cache.SetCacheability(HttpCacheability.NoCache);`
`  59`  ``
`  60`  `        try`
  - → Error handling block.
`  61`  `        {`
`  62`  `            if (!IsSeedAllowed())`
`  63`  `            {`
`  64`  `                AuthGate.WriteHandlerError(context, 403, "Seed endpoint is disabled. Set AllowSeedMockData=true in Web.config (debug only).");`
  - → Authorization — block wrong role / anonymous.
`  65`  `                return;`
`  66`  `            }`
`  67`  ``
`  68`  `            int uid;`
`  69`  `            if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  70`  `                return;`
`  71`  ``
`  72`  `            SecurityAudit.Log("seed.start", uid, "email=" + (context.Request["email"] ?? DefaultTeacherEmail));`
  - → Write/read security audit events.
`  73`  ``
`  74`  `            string teacherEmail = (context.Request["email"] ?? DefaultTeacherEmail).Trim().ToLowerInvariant();`
`  75`  `            if (string.IsNullOrEmpty(teacherEmail)) teacherEmail = DefaultTeacherEmail;`
`  76`  `            bool reset = context.Request["reset"] == "1";`
`  77`  ``
`  78`  `            var log = new List<string>();`
`  79`  `            var courseSummaries = new List<object>();`
`  80`  ``
`  81`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  82`  `            {`
`  83`  `                if (reset) ClearMockStudentData(conn, log);`
`  84`  ``
`  85`  `                // ── Teacher 1: t@t.com ────────────────────────────────────`
`  86`  `                int lecturerUid = EnsureTeacher(conn, teacherEmail, "Teacher One", DefaultTeacherPassword, log);`
`  87`  `                if (lecturerUid <= 0)`
`  88`  `                {`
`  89`  `                    Write(context, new { success = false, message = "Could not create/find teacher " + teacherEmail });`
`  90`  `                    return;`
`  91`  `                }`
`  92`  ``
`  93`  `                // ── Students ──────────────────────────────────────────────`
`  94`  `                int s1 = EnsureStudent(conn, "Alice Tan", "student1@edulms.local", log);`
`  95`  `                int s2 = EnsureStudent(conn, "Bob Lee", "student2@edulms.local", log);`
`  96`  `                int s3 = EnsureStudent(conn, "Cara Ng", "student3@edulms.local", log);`
`  97`  `                int s4 = EnsureStudent(conn, "Daniel Ong", "student4@edulms.local", log);`
`  98`  `                int s5 = EnsureStudent(conn, "Emily Wong", "student5@edulms.local", log);`
`  99`  `                var studentIds = new List<int> { s1, s2, s3, s4, s5 };`
` 100`  ``
` 101`  `                EnsureGradeScales(conn, log);`
` 102`  ``
` 103`  `                // ── 3 courses owned by t@t.com ────────────────────────────`
` 104`  `                var defs = new[]`
` 105`  `                {`
` 106`  `                    new MockCourseDef`
` 107`  `                    {`
` 108`  `                        Name = "Product Design Fundamentals",`
` 109`  `                        Description = "UI/UX basics, wireframes, and design critique for beginners.",`
` 110`  `                        Category = "Design",`
` 111`  `                        Level = "Beginner",`
` 112`  `                        Rating = 4.3m,`
` 113`  `                        Chapters = new[] { "Intro & Tools", "Wireframing", "Assessments" }`
` 114`  `                    },`
` 115`  `                    new MockCourseDef`
` 116`  `                    {`
` 117`  `                        Name = "Web App Programming",`
` 118`  `                        Description = "ASP.NET Web Forms, pure SQL, and auth for EduLMS-style apps.",`
` 119`  `                        Category = "Programming",`
` 120`  `                        Level = "Intermediate",`
` 121`  `                        Rating = 4.6m,`
` 122`  `                        Chapters = new[] { "Web Forms Basics", "Data Access", "Assessments" }`
` 123`  `                    },`
` 124`  `                    new MockCourseDef`
` 125`  `                    {`
` 126`  `                        Name = "Database Essentials",`
` 127`  `                        Description = "ER modelling, SQL queries, and LocalDB for coursework.",`
` 128`  `                        Category = "Database",`
` 129`  `                        Level = "Beginner",`
` 130`  `                        Rating = 4.1m,`
` 131`  `                        Chapters = new[] { "ER Diagrams", "SQL Queries", "Assessments" }`
` 132`  `                    }`
` 133`  `                };`
` 134`  ``
` 135`  `                int enrollCount = 0, workCount = 0, subCount = 0, markCount = 0, courseCreated = 0;`
` 136`  ``
` 137`  `                foreach (var def in defs)`
` 138`  `                {`
` 139`  `                    int cid = EnsureCourse(conn, lecturerUid, def, log, ref courseCreated);`
` 140`  `                    if (cid <= 0)`
` 141`  `                    {`
` 142`  `                        log.Add("FAILED to create/find course: " + def.Name);`
` 143`  `                        continue;`
` 144`  `                    }`
` 145`  ``
` 146`  `                    foreach (var chTitle in def.Chapters)`
` 147`  `                        EnsureChapter(conn, cid, chTitle);`
` 148`  ``
` 149`  `                    // Enroll all 5 students`
` 150`  `                    int i = 0;`
` 151`  `                    foreach (int stuid in studentIds)`
` 152`  `                    {`
` 153`  `                        int progress = 25 + ((stuid + i * 13) % 70);`
` 154`  `                        if (EnsureEnrollment(conn, cid, stuid, progress))`
` 155`  `                            enrollCount++;`
` 156`  `                        i++;`
` 157`  `                    }`
` 158`  ``
` 159`  `                    int assessCh = EnsureChapter(conn, cid, "Assessments");`
` 160`  ``
` 161`  `                    // Text-only, file-required, and mixed assessments`
` 162`  `                    int cwid1 = EnsureCourseWork(conn, assessCh,`
` 163`  `                        "Week 3 Written Task",`
` 164`  `                        BuildCwDescription("Write a short reflection on the module materials.", "Text", 100, false),`
` 165`  `                        DateTime.Today.AddDays(14), ref workCount);`
` 166`  ``
` 167`  `                    int cwid2 = EnsureCourseWork(conn, assessCh,`
` 168`  `                        "Midterm Quiz Pack",`
` 169`  `                        BuildCwDescription("Answer all objective questions.", "Objective", 50, false),`
` 170`  `                        DateTime.Today.AddDays(21), ref workCount);`
` 171`  ``
` 172`  `                    // File-upload required — PDF essay`
` 173`  `                    int cwid3 = EnsureCourseWork(conn, assessCh,`
` 174`  `                        "PDF Essay Upload",`
` 175`  `                        BuildCwDescription("Upload your essay as a PDF (file upload required). You may also add notes.", "File", 100, true),`
` 176`  `                        DateTime.Today.AddDays(30), ref workCount);`
` 177`  ``
` 178`  `                    foreach (int stuid in studentIds)`
` 179`  `                    {`
` 180`  `                        int sid1 = EnsureSubmission(conn, cwid1, stuid,`
` 181`  `                            "Written answer from student " + stuid + " for " + def.Name + ".",`
` 182`  `                            DateTime.Now.AddDays(-4), ref subCount);`
` 183`  `                        if (sid1 > 0)`
` 184`  `                            EnsureMarking(conn, sid1, 62 + (stuid % 30), "Solid effort — keep going.", ref markCount);`
` 185`  ``
` 186`  `                        int sid2 = EnsureSubmission(conn, cwid2, stuid,`
` 187`  `                            "Quiz answers A,C,B,D (student " + stuid + ").",`
` 188`  `                            DateTime.Now.AddDays(-2), ref subCount);`
` 189`  `                        // Leave odd UIDs ungraded for grading queue`
` 190`  `                        if (sid2 > 0 && stuid % 2 == 0)`
` 191`  `                            EnsureMarking(conn, sid2, 45 + (stuid % 40), "Quiz auto mock grade.", ref markCount);`
` 192`  ``
` 193`  `                        // File-required assessment: store JSON content with a placeholder path`
` 194`  `                        // (students re-upload a real PDF via Submit.aspx for full preview)`
` 195`  `                        if (stuid % 3 != 0)`
` 196`  `                        {`
` 197`  `                            string fileJson = "{\"v\":1,\"text\":\"See attached essay PDF.\",\"file\":\"\",\"fileName\":\"essay-student-" + stuid + ".pdf\"}";`
` 198`  `                            // Prefer real note-only until student uploads; mark require via assignment meta`
` 199`  `                            EnsureSubmission(conn, cwid3, stuid,`
` 200`  `                                "Essay notes from student " + stuid + " — PDF should be uploaded via Submit page.",`
` 201`  `                                DateTime.Now.AddDays(-1), ref subCount);`
` 202`  `                        }`
` 203`  `                    }`
` 204`  ``
` 205`  `                    int sc = ScalarInt(conn, "SELECT COUNT(*) FROM Enrollments WHERE CID=@C", P("@C", cid));`
` 206`  `                    int cw = ScalarInt(conn, @"`
` 207`  `SELECT COUNT(*) FROM CourseWorks cw`
` 208`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));`
` 209`  `                    int subs = ScalarInt(conn, @"`
` 210`  `SELECT COUNT(*) FROM CWSubmissions s`
` 211`  `INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 212`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));`
` 213`  `                    int marks = ScalarInt(conn, @"`
` 214`  `SELECT COUNT(*) FROM CWMarkings m`
` 215`  `INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 216`  `INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 217`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));`
` 218`  ``
` 219`  `                    log.Add(string.Format("CID={0} \"{1}\" students={2} assessments={3} submissions={4} markings={5}",`
` 220`  `                        cid, def.Name, sc, cw, subs, marks));`
` 221`  ``
` 222`  `                    courseSummaries.Add(new`
` 223`  `                    {`
` 224`  `                        cid = cid,`
` 225`  `                        name = def.Name,`
` 226`  `                        students = sc,`
` 227`  `                        assessments = cw,`
` 228`  `                        submissions = subs,`
` 229`  `                        markings = marks`
` 230`  `                    });`
` 231`  `                }`
` 232`  ``
` 233`  `                try { Exec(conn, "UPDATE Enrollments SET Progress=40 WHERE Progress IS NULL"); } catch { }`
  - → Error handling block.
` 234`  ``
` 235`  `                Write(context, new`
` 236`  `                {`
` 237`  `                    success = true,`
` 238`  `                    message = "Seeded 3 courses for teacher " + teacherEmail + ". Log in as t@t.com and open My Courses.",`
` 239`  `                    teacher = new`
` 240`  `                    {`
` 241`  `                        email = teacherEmail,`
` 242`  `                        password = DefaultTeacherPassword,`
` 243`  `                        uid = lecturerUid,`
` 244`  `                        role = "Lecturer (2)"`
` 245`  `                    },`
` 246`  `                    coursesCreated = courseCreated,`
` 247`  `                    courses = courseSummaries,`
` 248`  `                    added = new`
` 249`  `                    {`
` 250`  `                        enrollments = enrollCount,`
` 251`  `                        courseWorks = workCount,`
` 252`  `                        submissions = subCount,`
` 253`  `                        markings = markCount`
` 254`  `                    },`
` 255`  `                    students = new object[]`
` 256`  `                    {`
` 257`  `                        new { email = "student1@edulms.local", password = "Student123", name = "Alice Tan", uid = s1 },`
` 258`  `                        new { email = "student2@edulms.local", password = "Student123", name = "Bob Lee", uid = s2 },`
` 259`  `                        new { email = "student3@edulms.local", password = "Student123", name = "Cara Ng", uid = s3 },`
` 260`  `                        new { email = "student4@edulms.local", password = "Student123", name = "Daniel Ong", uid = s4 },`
` 261`  `                        new { email = "student5@edulms.local", password = "Student123", name = "Emily Wong", uid = s5 }`
` 262`  `                    },`
` 263`  `                    log = log`
` 264`  `                });`
` 265`  `            }`
` 266`  `        }`
` 267`  `        catch (Exception ex)`
  - → Handle/log exception.
` 268`  `        {`
` 269`  `            Write(context, new { success = false, message = "Seed failed. Check server logs." });`
` 270`  `        }`
` 271`  `    }`

---

### `EnsureTeacher` — lines 272–320

```
private static int EnsureTeacher(SqlConnection conn, string email, string name, string password, List<string> log)
```

#### Explanation

- **Purpose:** Implements `EnsureTeacher`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string email, string name, string password, List<string> log`
- **Local variables:** `uid`, `hash`

#### Line-by-line (this function)

` 272`  ``
` 273`  `    private static int EnsureTeacher(SqlConnection conn, string email, string name, string password, List<string> log)`
  - → Database access (pure SQL).
` 274`  `    {`
` 275`  `        int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));`
` 276`  `        if (uid > 0)`
` 277`  `        {`
` 278`  `            try`
  - → Error handling block.
` 279`  `            {`
` 280`  `                Exec(conn, "UPDATE Users SET Role=N'2', Name=ISNULL(NULLIF(LTRIM(RTRIM(Name)),N''),@N) WHERE UID=@UID",`
` 281`  `                    P("@UID", uid), P("@N", name));`
` 282`  `            }`
` 283`  `            catch`
  - → Handle/log exception.
` 284`  `            {`
` 285`  `                try { Exec(conn, "UPDATE Users SET Role=N'2' WHERE UID=@UID", P("@UID", uid)); } catch { }`
  - → Error handling block.
` 286`  `            }`
` 287`  `            log.Add("Using existing teacher " + email + " UID=" + uid + " (Role=2).");`
` 288`  `            return uid;`
` 289`  `        }`
` 290`  ``
` 291`  `        // Create lecturer`
` 292`  `        try`
  - → Error handling block.
` 293`  `        {`
` 294`  `            string hash = PasswordHasher.Hash(password);`
  - → Password hashing (PBKDF2).
` 295`  `            try`
  - → Error handling block.
` 296`  `            {`
` 297`  `                uid = ScalarInt(conn, @"`
` 298`  `INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)`
` 299`  `VALUES (@N, @E, @P, N'2', @H, 0);`
` 300`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 301`  `                    P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));`
` 302`  `            }`
` 303`  `            catch`
  - → Handle/log exception.
` 304`  `            {`
` 305`  `                uid = ScalarInt(conn, @"`
` 306`  `INSERT INTO Users (Name, Email, Password, Role)`
` 307`  `VALUES (@N, @E, @P, N'2');`
` 308`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 309`  `                    P("@N", name), P("@E", email), P("@P", password));`
` 310`  `            }`
` 311`  `        }`
` 312`  `        catch (Exception ex)`
  - → Handle/log exception.
` 313`  `        {`
` 314`  `            log.Add("Create teacher failed: " + ex.Message);`
` 315`  `            return 0;`
` 316`  `        }`
` 317`  ``
` 318`  `        log.Add("Created teacher " + email + " UID=" + uid + " password=" + password);`
` 319`  `        return uid;`
` 320`  `    }`

---

### `ClearMockStudentData` — lines 321–342

```
private static void ClearMockStudentData(SqlConnection conn, List<string> log)
```

#### Explanation

- **Purpose:** Implements `ClearMockStudentData`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Delete/clear data.
- **Parameters:** `SqlConnection conn, List<string> log`

#### Line-by-line (this function)

` 321`  ``
` 322`  `    private static void ClearMockStudentData(SqlConnection conn, List<string> log)`
  - → Database access (pure SQL).
` 323`  `    {`
` 324`  `        try`
  - → Error handling block.
` 325`  `        {`
` 326`  `            Exec(conn, @"`
` 327`  `DELETE m FROM CWMarkings m`
` 328`  `INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 329`  `INNER JOIN Users u ON u.UID = s.StudentUID`
` 330`  `WHERE u.Email LIKE 'student%@edulms.local'");`
` 331`  `            Exec(conn, @"`
` 332`  `DELETE s FROM CWSubmissions s`
` 333`  `INNER JOIN Users u ON u.UID = s.StudentUID`
` 334`  `WHERE u.Email LIKE 'student%@edulms.local'");`
` 335`  `            Exec(conn, @"`
` 336`  `DELETE e FROM Enrollments e`
` 337`  `INNER JOIN Users u ON u.UID = e.StudentUID`
` 338`  `WHERE u.Email LIKE 'student%@edulms.local'");`
` 339`  `            log.Add("Cleared prior mock enrollments/submissions for student*@edulms.local");`
` 340`  `        }`
` 341`  `        catch (Exception ex) { log.Add("Reset partial: " + ex.Message); }`
  - → Handle/log exception.
` 342`  `    }`

---

### `EnsureCourse` — lines 343–402

```
private static int EnsureCourse(SqlConnection conn, int lecturerUid, MockCourseDef def, List<string> log, ref int created)
```

#### Explanation

- **Purpose:** Implements `EnsureCourse`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Parameters:** `SqlConnection conn, int lecturerUid, MockCourseDef def, List<string> log, ref int created`
- **Local variables:** `cid`

#### Line-by-line (this function)

` 343`  ``
` 344`  `    private static int EnsureCourse(SqlConnection conn, int lecturerUid, MockCourseDef def, List<string> log, ref int created)`
  - → Database access (pure SQL).
` 345`  `    {`
` 346`  `        // Match by name + this lecturer`
` 347`  `        int cid = ScalarInt(conn,`
` 348`  `            "SELECT TOP 1 CID FROM Courses WHERE LecturerUID=@L AND Name=@N",`
  - → Owner lecturer foreign key.
` 349`  `            P("@L", lecturerUid), P("@N", def.Name));`
` 350`  `        if (cid > 0)`
` 351`  `        {`
` 352`  `            log.Add("Course already exists CID=" + cid + " \"" + def.Name + "\"");`
` 353`  `            return cid;`
` 354`  `        }`
` 355`  ``
` 356`  `        try`
  - → Error handling block.
` 357`  `        {`
` 358`  `            cid = ScalarInt(conn, @"`
` 359`  `INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level)`
  - → Owner lecturer foreign key.
` 360`  `VALUES (@L, @N, @D, @R, N'', @Cat, @Lv);`
` 361`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 362`  `                P("@L", lecturerUid),`
` 363`  `                P("@N", def.Name),`
` 364`  `                P("@D", def.Description),`
` 365`  `                P("@R", def.Rating),`
` 366`  `                P("@Cat", def.Category),`
` 367`  `                P("@Lv", def.Level));`
` 368`  `        }`
` 369`  `        catch`
  - → Handle/log exception.
` 370`  `        {`
` 371`  `            try`
  - → Error handling block.
` 372`  `            {`
` 373`  `                cid = ScalarInt(conn, @"`
` 374`  `INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level, Status)`
  - → Owner lecturer foreign key.
` 375`  `VALUES (@L, @N, @D, @R, N'', @Cat, @Lv, N'Published');`
` 376`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 377`  `                    P("@L", lecturerUid),`
` 378`  `                    P("@N", def.Name),`
` 379`  `                    P("@D", def.Description),`
` 380`  `                    P("@R", def.Rating),`
` 381`  `                    P("@Cat", def.Category),`
` 382`  `                    P("@Lv", def.Level));`
` 383`  `            }`
` 384`  `            catch`
  - → Handle/log exception.
` 385`  `            {`
` 386`  `                cid = ScalarInt(conn, @"`
` 387`  `INSERT INTO Courses (LecturerUID, Name, Description)`
  - → Owner lecturer foreign key.
` 388`  `VALUES (@L, @N, @D);`
` 389`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 390`  `                    P("@L", lecturerUid),`
` 391`  `                    P("@N", def.Name),`
` 392`  `                    P("@D", def.Description));`
` 393`  `            }`
` 394`  `        }`
` 395`  ``
` 396`  `        if (cid > 0)`
` 397`  `        {`
` 398`  `            created++;`
` 399`  `            log.Add("Created course CID=" + cid + " \"" + def.Name + "\" for LecturerUID=" + lecturerUid);`
  - → Owner lecturer foreign key.
` 400`  `        }`
` 401`  `        return cid;`
` 402`  `    }`

---

### `EnsureChapter` — lines 403–436

```
private static int EnsureChapter(SqlConnection conn, int cid, string title)
```

#### Explanation

- **Purpose:** Implements `EnsureChapter`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, int cid, string title`
- **Local variables:** `chid`, `idx`

#### Line-by-line (this function)

` 403`  ``
` 404`  `    private static int EnsureChapter(SqlConnection conn, int cid, string title)`
  - → Database access (pure SQL).
` 405`  `    {`
` 406`  `        int chid = ScalarInt(conn,`
` 407`  `            "SELECT TOP 1 ChID FROM Chapters WHERE CID=@C AND Title=@T",`
` 408`  `            P("@C", cid), P("@T", title));`
` 409`  `        if (chid > 0) return chid;`
` 410`  `        try`
  - → Error handling block.
` 411`  `        {`
` 412`  `            int idx = ScalarInt(conn, "SELECT ISNULL(MAX([Index]),0)+1 FROM Chapters WHERE CID=@C", P("@C", cid));`
` 413`  `            chid = ScalarInt(conn, @"`
` 414`  `INSERT INTO Chapters (CID, [Index], Title) VALUES (@C, @I, @T);`
` 415`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 416`  `                P("@C", cid), P("@I", idx), P("@T", title));`
` 417`  `        }`
` 418`  `        catch`
  - → Handle/log exception.
` 419`  `        {`
` 420`  `            try`
  - → Error handling block.
` 421`  `            {`
` 422`  `                chid = ScalarInt(conn, @"`
` 423`  `INSERT INTO Chapters (CID, Title, Description) VALUES (@C, @T, N'');`
` 424`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 425`  `                    P("@C", cid), P("@T", title));`
` 426`  `            }`
` 427`  `            catch`
  - → Handle/log exception.
` 428`  `            {`
` 429`  `                chid = ScalarInt(conn, @"`
` 430`  `INSERT INTO Chapters (CID, Title) VALUES (@C, @T);`
` 431`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 432`  `                    P("@C", cid), P("@T", title));`
` 433`  `            }`
` 434`  `        }`
` 435`  `        return chid;`
` 436`  `    }`

---

### `EnsureEnrollment` — lines 437–458

```
private static bool EnsureEnrollment(SqlConnection conn, int cid, int studentUid, int progress)
```

#### Explanation

- **Purpose:** Implements `EnsureEnrollment`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, int cid, int studentUid, int progress`
- **Local variables:** `exists`

#### Line-by-line (this function)

` 437`  ``
` 438`  `    private static bool EnsureEnrollment(SqlConnection conn, int cid, int studentUid, int progress)`
  - → Database access (pure SQL).
` 439`  `    {`
` 440`  `        int exists = ScalarInt(conn,`
` 441`  `            "SELECT COUNT(1) FROM Enrollments WHERE CID=@C AND StudentUID=@S",`
` 442`  `            P("@C", cid), P("@S", studentUid));`
` 443`  `        if (exists > 0)`
` 444`  `        {`
` 445`  `            try`
  - → Error handling block.
` 446`  `            {`
` 447`  `                Exec(conn,`
` 448`  `                    "UPDATE Enrollments SET Progress=@P WHERE CID=@C AND StudentUID=@S AND (Progress IS NULL OR Progress=0)",`
` 449`  `                    P("@C", cid), P("@S", studentUid), P("@P", progress));`
` 450`  `            }`
` 451`  `            catch { }`
  - → Handle/log exception.
` 452`  `            return false;`
` 453`  `        }`
` 454`  `        Exec(conn,`
` 455`  `            "INSERT INTO Enrollments (CID, StudentUID, Progress) VALUES (@C,@S,@P)",`
` 456`  `            P("@C", cid), P("@S", studentUid), P("@P", progress));`
` 457`  `        return true;`
` 458`  `    }`

---

### `EnsureGradeScales` — lines 459–480

```
private static void EnsureGradeScales(SqlConnection conn, List<string> log)
```

#### Explanation

- **Purpose:** Implements `EnsureGradeScales`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, List<string> log`

#### Line-by-line (this function)

` 459`  ``
` 460`  `    private static void EnsureGradeScales(SqlConnection conn, List<string> log)`
  - → Database access (pure SQL).
` 461`  `    {`
` 462`  `        try`
  - → Error handling block.
` 463`  `        {`
` 464`  `            if (ScalarInt(conn, "SELECT COUNT(*) FROM GradeScales") > 0) return;`
` 465`  `            string[] rows = {`
` 466`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A+', 90, 100)",`
` 467`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A', 80, 89)",`
` 468`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'B', 70, 79)",`
` 469`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'C', 60, 69)",`
` 470`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'D', 50, 59)",`
` 471`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'F', 0, 49)"`
` 472`  `            };`
` 473`  `            foreach (var sql in rows)`
` 474`  `            {`
` 475`  `                try { Exec(conn, sql); } catch { }`
  - → Error handling block.
` 476`  `            }`
` 477`  `            log.Add("Inserted GradeScales defaults.");`
` 478`  `        }`
` 479`  `        catch { }`
  - → Handle/log exception.
` 480`  `    }`

---

### `EnsureStudent` — lines 481–513

```
private static int EnsureStudent(SqlConnection conn, string name, string email, List<string> log)
```

#### Explanation

- **Purpose:** Implements `EnsureStudent`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string name, string email, List<string> log`
- **Local variables:** `uid`, `hash`

#### Line-by-line (this function)

` 481`  ``
` 482`  `    private static int EnsureStudent(SqlConnection conn, string name, string email, List<string> log)`
  - → Database access (pure SQL).
` 483`  `    {`
` 484`  `        int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));`
` 485`  `        if (uid > 0) return uid;`
` 486`  `        try`
  - → Error handling block.
` 487`  `        {`
` 488`  `            string hash = PasswordHasher.Hash("Student123");`
  - → Password hashing (PBKDF2).
` 489`  `            try`
  - → Error handling block.
` 490`  `            {`
` 491`  `                uid = ScalarInt(conn, @"`
` 492`  `INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)`
` 493`  `VALUES (@N, @E, @P, N'1', @H, 0);`
` 494`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 495`  `                    P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));`
` 496`  `            }`
` 497`  `            catch`
  - → Handle/log exception.
` 498`  `            {`
` 499`  `                uid = ScalarInt(conn, @"`
` 500`  `INSERT INTO Users (Name, Email, Password, Role)`
` 501`  `VALUES (@N, @E, @P, N'1');`
` 502`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 503`  `                    P("@N", name), P("@E", email), P("@P", "Student123"));`
` 504`  `            }`
` 505`  `        }`
` 506`  `        catch (Exception ex)`
  - → Handle/log exception.
` 507`  `        {`
` 508`  `            log.Add("Student create failed " + email + ": " + ex.Message);`
` 509`  `            return 0;`
` 510`  `        }`
` 511`  `        log.Add("Created student " + email + " UID=" + uid);`
` 512`  `        return uid;`
` 513`  `    }`

---

### `BuildCwDescription` — lines 516–531

```
private static string BuildCwDescription(string instructions, string type, int score, bool requireFile)
```

#### Explanation

- **Purpose:** Implements `BuildCwDescription`.
- **Due date:** Related to assignment closing after the due day.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `string instructions, string type, int score, bool requireFile`
- **Local variables:** `extra`, `payload`

#### Line-by-line (this function)

` 516`  `    private static string BuildCwDescription(string instructions, string type, int score, bool requireFile)`
` 517`  `    {`
` 518`  `        var extra = new Dictionary<string, object>`
` 519`  `        {`
` 520`  `            { "requireFile", requireFile },`
` 521`  `            { "dueDate", null }`
  - → Assignment deadline; submissions close after due day.
` 522`  `        };`
` 523`  `        var payload = new Dictionary<string, object>`
` 524`  `        {`
` 525`  `            { "instructions", instructions ?? "" },`
` 526`  `            { "type", type ?? "Text" },`
` 527`  `            { "score", score },`
` 528`  `            { "extra", extra }`
` 529`  `        };`
` 530`  `        return (instructions ?? "") + "\n<<<META>>>" + Json.Serialize(payload) + "<<<END>>>";`
  - → Pack extra assignment fields into Description JSON meta.
` 531`  `    }`

---

### `EnsureCourseWork` — lines 532–558

```
private static int EnsureCourseWork(SqlConnection conn, int chid, string title, string desc, DateTime due, ref int workCount)
```

#### Explanation

- **Purpose:** Implements `EnsureCourseWork`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Due date:** Related to assignment closing after the due day.
- **Parameters:** `SqlConnection conn, int chid, string title, string desc, DateTime due, ref int workCount`
- **Local variables:** `cwid`

#### Line-by-line (this function)

` 532`  ``
` 533`  `    private static int EnsureCourseWork(SqlConnection conn, int chid, string title, string desc, DateTime due, ref int workCount)`
  - → Database access (pure SQL).
` 534`  `    {`
` 535`  `        if (chid <= 0) return 0;`
` 536`  `        int cwid = ScalarInt(conn,`
` 537`  `            "SELECT TOP 1 CWID FROM CourseWorks WHERE ChID=@Ch AND Title=@T",`
` 538`  `            P("@Ch", chid), P("@T", title));`
` 539`  `        if (cwid > 0) return cwid;`
` 540`  `        try`
  - → Error handling block.
` 541`  `        {`
` 542`  `            cwid = ScalarInt(conn, @"`
` 543`  `INSERT INTO CourseWorks (ChID, Title, Description, DueDate)`
  - → Assignment deadline; submissions close after due day.
` 544`  `VALUES (@Ch, @T, @D, @Due);`
` 545`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 546`  `                P("@Ch", chid), P("@T", title), P("@D", desc), P("@Due", due));`
` 547`  `        }`
` 548`  `        catch`
  - → Handle/log exception.
` 549`  `        {`
` 550`  `            cwid = ScalarInt(conn, @"`
` 551`  `INSERT INTO CourseWorks (ChID, Title, Description)`
` 552`  `VALUES (@Ch, @T, @D);`
` 553`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 554`  `                P("@Ch", chid), P("@T", title), P("@D", desc));`
` 555`  `        }`
` 556`  `        if (cwid > 0) workCount++;`
` 557`  `        return cwid;`
` 558`  `    }`

---

### `EnsureSubmission` — lines 559–589

```
private static int EnsureSubmission(SqlConnection conn, int cwid, int studentUid, string content, DateTime when, ref int subCount)
```

#### Explanation

- **Purpose:** Implements `EnsureSubmission`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, int cwid, int studentUid, string content, DateTime when, ref int subCount`
- **Local variables:** `sid`

#### Line-by-line (this function)

` 559`  ``
` 560`  `    private static int EnsureSubmission(SqlConnection conn, int cwid, int studentUid, string content, DateTime when, ref int subCount)`
  - → Database access (pure SQL).
` 561`  `    {`
` 562`  `        if (cwid <= 0 || studentUid <= 0) return 0;`
` 563`  `        int sid = ScalarInt(conn,`
` 564`  `            "SELECT TOP 1 SID FROM CWSubmissions WHERE CWID=@C AND StudentUID=@S ORDER BY SID DESC",`
` 565`  `            P("@C", cwid), P("@S", studentUid));`
` 566`  `        if (sid > 0) return sid;`
` 567`  `        try`
  - → Error handling block.
` 568`  `        {`
` 569`  `            sid = ScalarInt(conn, @"`
` 570`  `INSERT INTO CWSubmissions (CWID, StudentUID, SubmissionDate, Content)`
` 571`  `VALUES (@C, @S, @When, @Content);`
` 572`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 573`  `                P("@C", cwid), P("@S", studentUid), P("@When", when), P("@Content", content));`
` 574`  `        }`
` 575`  `        catch`
  - → Handle/log exception.
` 576`  `        {`
` 577`  `            try`
  - → Error handling block.
` 578`  `            {`
` 579`  `                sid = ScalarInt(conn, @"`
` 580`  `INSERT INTO CWSubmissions (CWID, StudentUID, Content)`
` 581`  `VALUES (@C, @S, @Content);`
` 582`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 583`  `                    P("@C", cwid), P("@S", studentUid), P("@Content", content));`
` 584`  `            }`
` 585`  `            catch { return 0; }`
  - → Handle/log exception.
` 586`  `        }`
` 587`  `        if (sid > 0) subCount++;`
` 588`  `        return sid;`
` 589`  `    }`

---

### `EnsureMarking` — lines 590–612

```
private static bool EnsureMarking(SqlConnection conn, int sid, int score, string feedback, ref int markCount)
```

#### Explanation

- **Purpose:** Implements `EnsureMarking`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, int sid, int score, string feedback, ref int markCount`

#### Line-by-line (this function)

` 590`  ``
` 591`  `    private static bool EnsureMarking(SqlConnection conn, int sid, int score, string feedback, ref int markCount)`
  - → Database access (pure SQL).
` 592`  `    {`
` 593`  `        if (sid <= 0) return false;`
` 594`  `        if (ScalarInt(conn, "SELECT COUNT(1) FROM CWMarkings WHERE SID=@S", P("@S", sid)) > 0)`
` 595`  `            return false;`
` 596`  `        try`
  - → Error handling block.
` 597`  `        {`
` 598`  `            Exec(conn, "INSERT INTO CWMarkings (SID, Marks, Feedback) VALUES (@S, @Sc, @R)",`
` 599`  `                P("@S", sid), P("@Sc", score), P("@R", feedback ?? ""));`
` 600`  `        }`
` 601`  `        catch`
  - → Handle/log exception.
` 602`  `        {`
` 603`  `            try`
  - → Error handling block.
` 604`  `            {`
` 605`  `                Exec(conn, "INSERT INTO CWMarkings (SID, Marks) VALUES (@S, @Sc)",`
` 606`  `                    P("@S", sid), P("@Sc", score));`
` 607`  `            }`
` 608`  `            catch { return false; }`
  - → Handle/log exception.
` 609`  `        }`
` 610`  `        markCount++;`
` 611`  `        return true;`
` 612`  `    }`

---

### `P` — lines 613–617

```
private static SqlParameter P(string n, object v)
```

#### Explanation

- **Purpose:** Implements `P`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string n, object v`

#### Line-by-line (this function)

` 613`  ``
` 614`  `    private static SqlParameter P(string n, object v)`
` 615`  `    {`
` 616`  `        return new SqlParameter(n, v ?? DBNull.Value);`
` 617`  `    }`

---

### `Exec` — lines 618–626

```
private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `Exec`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string sql, params SqlParameter[] ps`
- **Local variables:** `cmd`

#### Line-by-line (this function)

` 618`  ``
` 619`  `    private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
` 620`  `    {`
` 621`  `        using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
` 622`  `        {`
` 623`  `            if (ps != null) cmd.Parameters.AddRange(ps);`
` 624`  `            cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 625`  `        }`
` 626`  `    }`

---

### `ScalarInt` — lines 627–637

```
private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `ScalarInt`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string sql, params SqlParameter[] ps`
- **Local variables:** `cmd`, `o`

#### Line-by-line (this function)

` 627`  ``
` 628`  `    private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
` 629`  `    {`
` 630`  `        using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
` 631`  `        {`
` 632`  `            if (ps != null) cmd.Parameters.AddRange(ps);`
` 633`  `            var o = cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
` 634`  `            if (o == null || o == DBNull.Value) return 0;`
` 635`  `            return Convert.ToInt32(o);`
` 636`  `        }`
` 637`  `    }`

---

### `Write` — lines 638–642

```
private static void Write(HttpContext ctx, object o)
```

#### Explanation

- **Purpose:** Implements `Write`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext ctx, object o`

#### Line-by-line (this function)

` 638`  ``
` 639`  `    private static void Write(HttpContext ctx, object o)`
` 640`  `    {`
` 641`  `        ctx.Response.Write(Json.Serialize(o));`
` 642`  `    }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `<%@ WebHandler Language="C#" Class="SeedMockData" %>`
`   2`  ``
`   3`  `using System;`
  - → Import namespace/types.
`   4`  `using System.Collections.Generic;`
  - → Import namespace/types.
`   5`  `using System.Data;`
  - → Import namespace/types.
`   6`  `using System.Data.SqlClient;`
  - → Import namespace/types.
`   7`  `using System.Web;`
  - → Import namespace/types.
`   8`  `using System.Web.Script.Serialization;`
  - → Import namespace/types.
`   9`  `using System.Configuration;`
  - → Import namespace/types.
`  10`  `using System.Web.SessionState;`
  - → Import namespace/types.
`  11`  `using WebAppAssignment.Data;`
  - → Import namespace/types.
`  12`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`  13`  ``
`  14`  `/// <summary>`
`  15`  `/// Seeds mock courses for teacher t@t.com + students + enrollments + assessments.`
`  16`  `///`
`  17`  `/// GET /Pages/Lecturer/SeedMockData.ashx`
`  18`  `/// Optional:`
`  19`  `///   ?email=t@t.com     (default teacher)`
`  20`  `///   ?reset=1           clear prior mock student enrollments/submissions`
`  21`  `///`
`  22`  `/// Requires Lecturer or Admin session. Disabled unless compilation debug`
`  23`  `/// or appSetting AllowSeedMockData=true.`
`  24`  `/// </summary>`
`  25`  `public class SeedMockData : IHttpHandler, IRequiresSessionState`
  - → Class declaration for this page/service.
`  26`  `{`
`  27`  `    private static readonly JavaScriptSerializer Json = new JavaScriptSerializer();`
`  28`  `    private const string DefaultTeacherEmail = "t@t.com";`
`  29`  `    private const string DefaultTeacherPassword = "Teacher123";`
`  30`  ``
`  31`  `    private static bool IsSeedAllowed()`
`  32`  `    {`
`  33`  `        string allow = ConfigurationManager.AppSettings["AllowSeedMockData"];`
`  34`  `        if (string.Equals(allow, "true", StringComparison.OrdinalIgnoreCase)) return true;`
`  35`  `        if (string.Equals(allow, "false", StringComparison.OrdinalIgnoreCase)) return false;`
`  36`  `        // default: only when compilation debug`
`  37`  `        try`
  - → Error handling block.
`  38`  `        {`
`  39`  `            return HttpContext.Current != null`
`  40`  `                && HttpContext.Current.IsDebuggingEnabled;`
`  41`  `        }`
`  42`  `        catch { return false; }`
  - → Handle/log exception.
`  43`  `    }`
`  44`  ``
`  45`  `    private class MockCourseDef`
  - → Class declaration for this page/service.
`  46`  `    {`
`  47`  `        public string Name;`
`  48`  `        public string Description;`
`  49`  `        public string Category;`
`  50`  `        public string Level;`
`  51`  `        public decimal Rating;`
`  52`  `        public string[] Chapters;`
`  53`  `    }`
`  54`  ``
`  55`  `    public void ProcessRequest(HttpContext context)`
  - → IHttpHandler entry for ashx.
`  56`  `    {`
`  57`  `        context.Response.ContentType = "application/json; charset=utf-8";`
`  58`  `        context.Response.Cache.SetCacheability(HttpCacheability.NoCache);`
`  59`  ``
`  60`  `        try`
  - → Error handling block.
`  61`  `        {`
`  62`  `            if (!IsSeedAllowed())`
`  63`  `            {`
`  64`  `                AuthGate.WriteHandlerError(context, 403, "Seed endpoint is disabled. Set AllowSeedMockData=true in Web.config (debug only).");`
  - → Authorization — block wrong role / anonymous.
`  65`  `                return;`
`  66`  `            }`
`  67`  ``
`  68`  `            int uid;`
`  69`  `            if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  70`  `                return;`
`  71`  ``
`  72`  `            SecurityAudit.Log("seed.start", uid, "email=" + (context.Request["email"] ?? DefaultTeacherEmail));`
  - → Write/read security audit events.
`  73`  ``
`  74`  `            string teacherEmail = (context.Request["email"] ?? DefaultTeacherEmail).Trim().ToLowerInvariant();`
`  75`  `            if (string.IsNullOrEmpty(teacherEmail)) teacherEmail = DefaultTeacherEmail;`
`  76`  `            bool reset = context.Request["reset"] == "1";`
`  77`  ``
`  78`  `            var log = new List<string>();`
`  79`  `            var courseSummaries = new List<object>();`
`  80`  ``
`  81`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  82`  `            {`
`  83`  `                if (reset) ClearMockStudentData(conn, log);`
`  84`  ``
`  85`  `                // ── Teacher 1: t@t.com ────────────────────────────────────`
`  86`  `                int lecturerUid = EnsureTeacher(conn, teacherEmail, "Teacher One", DefaultTeacherPassword, log);`
`  87`  `                if (lecturerUid <= 0)`
`  88`  `                {`
`  89`  `                    Write(context, new { success = false, message = "Could not create/find teacher " + teacherEmail });`
`  90`  `                    return;`
`  91`  `                }`
`  92`  ``
`  93`  `                // ── Students ──────────────────────────────────────────────`
`  94`  `                int s1 = EnsureStudent(conn, "Alice Tan", "student1@edulms.local", log);`
`  95`  `                int s2 = EnsureStudent(conn, "Bob Lee", "student2@edulms.local", log);`
`  96`  `                int s3 = EnsureStudent(conn, "Cara Ng", "student3@edulms.local", log);`
`  97`  `                int s4 = EnsureStudent(conn, "Daniel Ong", "student4@edulms.local", log);`
`  98`  `                int s5 = EnsureStudent(conn, "Emily Wong", "student5@edulms.local", log);`
`  99`  `                var studentIds = new List<int> { s1, s2, s3, s4, s5 };`
` 100`  ``
` 101`  `                EnsureGradeScales(conn, log);`
` 102`  ``
` 103`  `                // ── 3 courses owned by t@t.com ────────────────────────────`
` 104`  `                var defs = new[]`
` 105`  `                {`
` 106`  `                    new MockCourseDef`
` 107`  `                    {`
` 108`  `                        Name = "Product Design Fundamentals",`
` 109`  `                        Description = "UI/UX basics, wireframes, and design critique for beginners.",`
` 110`  `                        Category = "Design",`
` 111`  `                        Level = "Beginner",`
` 112`  `                        Rating = 4.3m,`
` 113`  `                        Chapters = new[] { "Intro & Tools", "Wireframing", "Assessments" }`
` 114`  `                    },`
` 115`  `                    new MockCourseDef`
` 116`  `                    {`
` 117`  `                        Name = "Web App Programming",`
` 118`  `                        Description = "ASP.NET Web Forms, pure SQL, and auth for EduLMS-style apps.",`
` 119`  `                        Category = "Programming",`
` 120`  `                        Level = "Intermediate",`
` 121`  `                        Rating = 4.6m,`
` 122`  `                        Chapters = new[] { "Web Forms Basics", "Data Access", "Assessments" }`
` 123`  `                    },`
` 124`  `                    new MockCourseDef`
` 125`  `                    {`
` 126`  `                        Name = "Database Essentials",`
` 127`  `                        Description = "ER modelling, SQL queries, and LocalDB for coursework.",`
` 128`  `                        Category = "Database",`
` 129`  `                        Level = "Beginner",`
` 130`  `                        Rating = 4.1m,`
` 131`  `                        Chapters = new[] { "ER Diagrams", "SQL Queries", "Assessments" }`
` 132`  `                    }`
` 133`  `                };`
` 134`  ``
` 135`  `                int enrollCount = 0, workCount = 0, subCount = 0, markCount = 0, courseCreated = 0;`
` 136`  ``
` 137`  `                foreach (var def in defs)`
` 138`  `                {`
` 139`  `                    int cid = EnsureCourse(conn, lecturerUid, def, log, ref courseCreated);`
` 140`  `                    if (cid <= 0)`
` 141`  `                    {`
` 142`  `                        log.Add("FAILED to create/find course: " + def.Name);`
` 143`  `                        continue;`
` 144`  `                    }`
` 145`  ``
` 146`  `                    foreach (var chTitle in def.Chapters)`
` 147`  `                        EnsureChapter(conn, cid, chTitle);`
` 148`  ``
` 149`  `                    // Enroll all 5 students`
` 150`  `                    int i = 0;`
` 151`  `                    foreach (int stuid in studentIds)`
` 152`  `                    {`
` 153`  `                        int progress = 25 + ((stuid + i * 13) % 70);`
` 154`  `                        if (EnsureEnrollment(conn, cid, stuid, progress))`
` 155`  `                            enrollCount++;`
` 156`  `                        i++;`
` 157`  `                    }`
` 158`  ``
` 159`  `                    int assessCh = EnsureChapter(conn, cid, "Assessments");`
` 160`  ``
` 161`  `                    // Text-only, file-required, and mixed assessments`
` 162`  `                    int cwid1 = EnsureCourseWork(conn, assessCh,`
` 163`  `                        "Week 3 Written Task",`
` 164`  `                        BuildCwDescription("Write a short reflection on the module materials.", "Text", 100, false),`
` 165`  `                        DateTime.Today.AddDays(14), ref workCount);`
` 166`  ``
` 167`  `                    int cwid2 = EnsureCourseWork(conn, assessCh,`
` 168`  `                        "Midterm Quiz Pack",`
` 169`  `                        BuildCwDescription("Answer all objective questions.", "Objective", 50, false),`
` 170`  `                        DateTime.Today.AddDays(21), ref workCount);`
` 171`  ``
` 172`  `                    // File-upload required — PDF essay`
` 173`  `                    int cwid3 = EnsureCourseWork(conn, assessCh,`
` 174`  `                        "PDF Essay Upload",`
` 175`  `                        BuildCwDescription("Upload your essay as a PDF (file upload required). You may also add notes.", "File", 100, true),`
` 176`  `                        DateTime.Today.AddDays(30), ref workCount);`
` 177`  ``
` 178`  `                    foreach (int stuid in studentIds)`
` 179`  `                    {`
` 180`  `                        int sid1 = EnsureSubmission(conn, cwid1, stuid,`
` 181`  `                            "Written answer from student " + stuid + " for " + def.Name + ".",`
` 182`  `                            DateTime.Now.AddDays(-4), ref subCount);`
` 183`  `                        if (sid1 > 0)`
` 184`  `                            EnsureMarking(conn, sid1, 62 + (stuid % 30), "Solid effort — keep going.", ref markCount);`
` 185`  ``
` 186`  `                        int sid2 = EnsureSubmission(conn, cwid2, stuid,`
` 187`  `                            "Quiz answers A,C,B,D (student " + stuid + ").",`
` 188`  `                            DateTime.Now.AddDays(-2), ref subCount);`
` 189`  `                        // Leave odd UIDs ungraded for grading queue`
` 190`  `                        if (sid2 > 0 && stuid % 2 == 0)`
` 191`  `                            EnsureMarking(conn, sid2, 45 + (stuid % 40), "Quiz auto mock grade.", ref markCount);`
` 192`  ``
` 193`  `                        // File-required assessment: store JSON content with a placeholder path`
` 194`  `                        // (students re-upload a real PDF via Submit.aspx for full preview)`
` 195`  `                        if (stuid % 3 != 0)`
` 196`  `                        {`
` 197`  `                            string fileJson = "{\"v\":1,\"text\":\"See attached essay PDF.\",\"file\":\"\",\"fileName\":\"essay-student-" + stuid + ".pdf\"}";`
` 198`  `                            // Prefer real note-only until student uploads; mark require via assignment meta`
` 199`  `                            EnsureSubmission(conn, cwid3, stuid,`
` 200`  `                                "Essay notes from student " + stuid + " — PDF should be uploaded via Submit page.",`
` 201`  `                                DateTime.Now.AddDays(-1), ref subCount);`
` 202`  `                        }`
` 203`  `                    }`
` 204`  ``
` 205`  `                    int sc = ScalarInt(conn, "SELECT COUNT(*) FROM Enrollments WHERE CID=@C", P("@C", cid));`
` 206`  `                    int cw = ScalarInt(conn, @"`
` 207`  `SELECT COUNT(*) FROM CourseWorks cw`
` 208`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));`
` 209`  `                    int subs = ScalarInt(conn, @"`
` 210`  `SELECT COUNT(*) FROM CWSubmissions s`
` 211`  `INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 212`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));`
` 213`  `                    int marks = ScalarInt(conn, @"`
` 214`  `SELECT COUNT(*) FROM CWMarkings m`
` 215`  `INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 216`  `INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 217`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID WHERE ch.CID=@C", P("@C", cid));`
` 218`  ``
` 219`  `                    log.Add(string.Format("CID={0} \"{1}\" students={2} assessments={3} submissions={4} markings={5}",`
` 220`  `                        cid, def.Name, sc, cw, subs, marks));`
` 221`  ``
` 222`  `                    courseSummaries.Add(new`
` 223`  `                    {`
` 224`  `                        cid = cid,`
` 225`  `                        name = def.Name,`
` 226`  `                        students = sc,`
` 227`  `                        assessments = cw,`
` 228`  `                        submissions = subs,`
` 229`  `                        markings = marks`
` 230`  `                    });`
` 231`  `                }`
` 232`  ``
` 233`  `                try { Exec(conn, "UPDATE Enrollments SET Progress=40 WHERE Progress IS NULL"); } catch { }`
  - → Error handling block.
` 234`  ``
` 235`  `                Write(context, new`
` 236`  `                {`
` 237`  `                    success = true,`
` 238`  `                    message = "Seeded 3 courses for teacher " + teacherEmail + ". Log in as t@t.com and open My Courses.",`
` 239`  `                    teacher = new`
` 240`  `                    {`
` 241`  `                        email = teacherEmail,`
` 242`  `                        password = DefaultTeacherPassword,`
` 243`  `                        uid = lecturerUid,`
` 244`  `                        role = "Lecturer (2)"`
` 245`  `                    },`
` 246`  `                    coursesCreated = courseCreated,`
` 247`  `                    courses = courseSummaries,`
` 248`  `                    added = new`
` 249`  `                    {`
` 250`  `                        enrollments = enrollCount,`
` 251`  `                        courseWorks = workCount,`
` 252`  `                        submissions = subCount,`
` 253`  `                        markings = markCount`
` 254`  `                    },`
` 255`  `                    students = new object[]`
` 256`  `                    {`
` 257`  `                        new { email = "student1@edulms.local", password = "Student123", name = "Alice Tan", uid = s1 },`
` 258`  `                        new { email = "student2@edulms.local", password = "Student123", name = "Bob Lee", uid = s2 },`
` 259`  `                        new { email = "student3@edulms.local", password = "Student123", name = "Cara Ng", uid = s3 },`
` 260`  `                        new { email = "student4@edulms.local", password = "Student123", name = "Daniel Ong", uid = s4 },`
` 261`  `                        new { email = "student5@edulms.local", password = "Student123", name = "Emily Wong", uid = s5 }`
` 262`  `                    },`
` 263`  `                    log = log`
` 264`  `                });`
` 265`  `            }`
` 266`  `        }`
` 267`  `        catch (Exception ex)`
  - → Handle/log exception.
` 268`  `        {`
` 269`  `            Write(context, new { success = false, message = "Seed failed. Check server logs." });`
` 270`  `        }`
` 271`  `    }`
` 272`  ``
` 273`  `    private static int EnsureTeacher(SqlConnection conn, string email, string name, string password, List<string> log)`
  - → Database access (pure SQL).
` 274`  `    {`
` 275`  `        int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));`
` 276`  `        if (uid > 0)`
` 277`  `        {`
` 278`  `            try`
  - → Error handling block.
` 279`  `            {`
` 280`  `                Exec(conn, "UPDATE Users SET Role=N'2', Name=ISNULL(NULLIF(LTRIM(RTRIM(Name)),N''),@N) WHERE UID=@UID",`
` 281`  `                    P("@UID", uid), P("@N", name));`
` 282`  `            }`
` 283`  `            catch`
  - → Handle/log exception.
` 284`  `            {`
` 285`  `                try { Exec(conn, "UPDATE Users SET Role=N'2' WHERE UID=@UID", P("@UID", uid)); } catch { }`
  - → Error handling block.
` 286`  `            }`
` 287`  `            log.Add("Using existing teacher " + email + " UID=" + uid + " (Role=2).");`
` 288`  `            return uid;`
` 289`  `        }`
` 290`  ``
` 291`  `        // Create lecturer`
` 292`  `        try`
  - → Error handling block.
` 293`  `        {`
` 294`  `            string hash = PasswordHasher.Hash(password);`
  - → Password hashing (PBKDF2).
` 295`  `            try`
  - → Error handling block.
` 296`  `            {`
` 297`  `                uid = ScalarInt(conn, @"`
` 298`  `INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)`
` 299`  `VALUES (@N, @E, @P, N'2', @H, 0);`
` 300`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 301`  `                    P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));`
` 302`  `            }`
` 303`  `            catch`
  - → Handle/log exception.
` 304`  `            {`
` 305`  `                uid = ScalarInt(conn, @"`
` 306`  `INSERT INTO Users (Name, Email, Password, Role)`
` 307`  `VALUES (@N, @E, @P, N'2');`
` 308`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 309`  `                    P("@N", name), P("@E", email), P("@P", password));`
` 310`  `            }`
` 311`  `        }`
` 312`  `        catch (Exception ex)`
  - → Handle/log exception.
` 313`  `        {`
` 314`  `            log.Add("Create teacher failed: " + ex.Message);`
` 315`  `            return 0;`
` 316`  `        }`
` 317`  ``
` 318`  `        log.Add("Created teacher " + email + " UID=" + uid + " password=" + password);`
` 319`  `        return uid;`
` 320`  `    }`
` 321`  ``
` 322`  `    private static void ClearMockStudentData(SqlConnection conn, List<string> log)`
  - → Database access (pure SQL).
` 323`  `    {`
` 324`  `        try`
  - → Error handling block.
` 325`  `        {`
` 326`  `            Exec(conn, @"`
` 327`  `DELETE m FROM CWMarkings m`
` 328`  `INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 329`  `INNER JOIN Users u ON u.UID = s.StudentUID`
` 330`  `WHERE u.Email LIKE 'student%@edulms.local'");`
` 331`  `            Exec(conn, @"`
` 332`  `DELETE s FROM CWSubmissions s`
` 333`  `INNER JOIN Users u ON u.UID = s.StudentUID`
` 334`  `WHERE u.Email LIKE 'student%@edulms.local'");`
` 335`  `            Exec(conn, @"`
` 336`  `DELETE e FROM Enrollments e`
` 337`  `INNER JOIN Users u ON u.UID = e.StudentUID`
` 338`  `WHERE u.Email LIKE 'student%@edulms.local'");`
` 339`  `            log.Add("Cleared prior mock enrollments/submissions for student*@edulms.local");`
` 340`  `        }`
` 341`  `        catch (Exception ex) { log.Add("Reset partial: " + ex.Message); }`
  - → Handle/log exception.
` 342`  `    }`
` 343`  ``
` 344`  `    private static int EnsureCourse(SqlConnection conn, int lecturerUid, MockCourseDef def, List<string> log, ref int created)`
  - → Database access (pure SQL).
` 345`  `    {`
` 346`  `        // Match by name + this lecturer`
` 347`  `        int cid = ScalarInt(conn,`
` 348`  `            "SELECT TOP 1 CID FROM Courses WHERE LecturerUID=@L AND Name=@N",`
  - → Owner lecturer foreign key.
` 349`  `            P("@L", lecturerUid), P("@N", def.Name));`
` 350`  `        if (cid > 0)`
` 351`  `        {`
` 352`  `            log.Add("Course already exists CID=" + cid + " \"" + def.Name + "\"");`
` 353`  `            return cid;`
` 354`  `        }`
` 355`  ``
` 356`  `        try`
  - → Error handling block.
` 357`  `        {`
` 358`  `            cid = ScalarInt(conn, @"`
` 359`  `INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level)`
  - → Owner lecturer foreign key.
` 360`  `VALUES (@L, @N, @D, @R, N'', @Cat, @Lv);`
` 361`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 362`  `                P("@L", lecturerUid),`
` 363`  `                P("@N", def.Name),`
` 364`  `                P("@D", def.Description),`
` 365`  `                P("@R", def.Rating),`
` 366`  `                P("@Cat", def.Category),`
` 367`  `                P("@Lv", def.Level));`
` 368`  `        }`
` 369`  `        catch`
  - → Handle/log exception.
` 370`  `        {`
` 371`  `            try`
  - → Error handling block.
` 372`  `            {`
` 373`  `                cid = ScalarInt(conn, @"`
` 374`  `INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level, Status)`
  - → Owner lecturer foreign key.
` 375`  `VALUES (@L, @N, @D, @R, N'', @Cat, @Lv, N'Published');`
` 376`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 377`  `                    P("@L", lecturerUid),`
` 378`  `                    P("@N", def.Name),`
` 379`  `                    P("@D", def.Description),`
` 380`  `                    P("@R", def.Rating),`
` 381`  `                    P("@Cat", def.Category),`
` 382`  `                    P("@Lv", def.Level));`
` 383`  `            }`
` 384`  `            catch`
  - → Handle/log exception.
` 385`  `            {`
` 386`  `                cid = ScalarInt(conn, @"`
` 387`  `INSERT INTO Courses (LecturerUID, Name, Description)`
  - → Owner lecturer foreign key.
` 388`  `VALUES (@L, @N, @D);`
` 389`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 390`  `                    P("@L", lecturerUid),`
` 391`  `                    P("@N", def.Name),`
` 392`  `                    P("@D", def.Description));`
` 393`  `            }`
` 394`  `        }`
` 395`  ``
` 396`  `        if (cid > 0)`
` 397`  `        {`
` 398`  `            created++;`
` 399`  `            log.Add("Created course CID=" + cid + " \"" + def.Name + "\" for LecturerUID=" + lecturerUid);`
  - → Owner lecturer foreign key.
` 400`  `        }`
` 401`  `        return cid;`
` 402`  `    }`
` 403`  ``
` 404`  `    private static int EnsureChapter(SqlConnection conn, int cid, string title)`
  - → Database access (pure SQL).
` 405`  `    {`
` 406`  `        int chid = ScalarInt(conn,`
` 407`  `            "SELECT TOP 1 ChID FROM Chapters WHERE CID=@C AND Title=@T",`
` 408`  `            P("@C", cid), P("@T", title));`
` 409`  `        if (chid > 0) return chid;`
` 410`  `        try`
  - → Error handling block.
` 411`  `        {`
` 412`  `            int idx = ScalarInt(conn, "SELECT ISNULL(MAX([Index]),0)+1 FROM Chapters WHERE CID=@C", P("@C", cid));`
` 413`  `            chid = ScalarInt(conn, @"`
` 414`  `INSERT INTO Chapters (CID, [Index], Title) VALUES (@C, @I, @T);`
` 415`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 416`  `                P("@C", cid), P("@I", idx), P("@T", title));`
` 417`  `        }`
` 418`  `        catch`
  - → Handle/log exception.
` 419`  `        {`
` 420`  `            try`
  - → Error handling block.
` 421`  `            {`
` 422`  `                chid = ScalarInt(conn, @"`
` 423`  `INSERT INTO Chapters (CID, Title, Description) VALUES (@C, @T, N'');`
` 424`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 425`  `                    P("@C", cid), P("@T", title));`
` 426`  `            }`
` 427`  `            catch`
  - → Handle/log exception.
` 428`  `            {`
` 429`  `                chid = ScalarInt(conn, @"`
` 430`  `INSERT INTO Chapters (CID, Title) VALUES (@C, @T);`
` 431`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 432`  `                    P("@C", cid), P("@T", title));`
` 433`  `            }`
` 434`  `        }`
` 435`  `        return chid;`
` 436`  `    }`
` 437`  ``
` 438`  `    private static bool EnsureEnrollment(SqlConnection conn, int cid, int studentUid, int progress)`
  - → Database access (pure SQL).
` 439`  `    {`
` 440`  `        int exists = ScalarInt(conn,`
` 441`  `            "SELECT COUNT(1) FROM Enrollments WHERE CID=@C AND StudentUID=@S",`
` 442`  `            P("@C", cid), P("@S", studentUid));`
` 443`  `        if (exists > 0)`
` 444`  `        {`
` 445`  `            try`
  - → Error handling block.
` 446`  `            {`
` 447`  `                Exec(conn,`
` 448`  `                    "UPDATE Enrollments SET Progress=@P WHERE CID=@C AND StudentUID=@S AND (Progress IS NULL OR Progress=0)",`
` 449`  `                    P("@C", cid), P("@S", studentUid), P("@P", progress));`
` 450`  `            }`
` 451`  `            catch { }`
  - → Handle/log exception.
` 452`  `            return false;`
` 453`  `        }`
` 454`  `        Exec(conn,`
` 455`  `            "INSERT INTO Enrollments (CID, StudentUID, Progress) VALUES (@C,@S,@P)",`
` 456`  `            P("@C", cid), P("@S", studentUid), P("@P", progress));`
` 457`  `        return true;`
` 458`  `    }`
` 459`  ``
` 460`  `    private static void EnsureGradeScales(SqlConnection conn, List<string> log)`
  - → Database access (pure SQL).
` 461`  `    {`
` 462`  `        try`
  - → Error handling block.
` 463`  `        {`
` 464`  `            if (ScalarInt(conn, "SELECT COUNT(*) FROM GradeScales") > 0) return;`
` 465`  `            string[] rows = {`
` 466`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A+', 90, 100)",`
` 467`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'A', 80, 89)",`
` 468`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'B', 70, 79)",`
` 469`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'C', 60, 69)",`
` 470`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'D', 50, 59)",`
` 471`  `                "INSERT INTO GradeScales (GradeLetter, MinMarks, MaxMarks) VALUES (N'F', 0, 49)"`
` 472`  `            };`
` 473`  `            foreach (var sql in rows)`
` 474`  `            {`
` 475`  `                try { Exec(conn, sql); } catch { }`
  - → Error handling block.
` 476`  `            }`
` 477`  `            log.Add("Inserted GradeScales defaults.");`
` 478`  `        }`
` 479`  `        catch { }`
  - → Handle/log exception.
` 480`  `    }`
` 481`  ``
` 482`  `    private static int EnsureStudent(SqlConnection conn, string name, string email, List<string> log)`
  - → Database access (pure SQL).
` 483`  `    {`
` 484`  `        int uid = ScalarInt(conn, "SELECT UID FROM Users WHERE Email=@E", P("@E", email));`
` 485`  `        if (uid > 0) return uid;`
` 486`  `        try`
  - → Error handling block.
` 487`  `        {`
` 488`  `            string hash = PasswordHasher.Hash("Student123");`
  - → Password hashing (PBKDF2).
` 489`  `            try`
  - → Error handling block.
` 490`  `            {`
` 491`  `                uid = ScalarInt(conn, @"`
` 492`  `INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaEnabled)`
` 493`  `VALUES (@N, @E, @P, N'1', @H, 0);`
` 494`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 495`  `                    P("@N", name), P("@E", email), P("@P", hash), P("@H", hash));`
` 496`  `            }`
` 497`  `            catch`
  - → Handle/log exception.
` 498`  `            {`
` 499`  `                uid = ScalarInt(conn, @"`
` 500`  `INSERT INTO Users (Name, Email, Password, Role)`
` 501`  `VALUES (@N, @E, @P, N'1');`
` 502`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 503`  `                    P("@N", name), P("@E", email), P("@P", "Student123"));`
` 504`  `            }`
` 505`  `        }`
` 506`  `        catch (Exception ex)`
  - → Handle/log exception.
` 507`  `        {`
` 508`  `            log.Add("Student create failed " + email + ": " + ex.Message);`
` 509`  `            return 0;`
` 510`  `        }`
` 511`  `        log.Add("Created student " + email + " UID=" + uid);`
` 512`  `        return uid;`
` 513`  `    }`
` 514`  ``
` 515`  `    /// <summary>Pack description meta so Submit.aspx reads requireFile + type.</summary>`
` 516`  `    private static string BuildCwDescription(string instructions, string type, int score, bool requireFile)`
` 517`  `    {`
` 518`  `        var extra = new Dictionary<string, object>`
` 519`  `        {`
` 520`  `            { "requireFile", requireFile },`
` 521`  `            { "dueDate", null }`
  - → Assignment deadline; submissions close after due day.
` 522`  `        };`
` 523`  `        var payload = new Dictionary<string, object>`
` 524`  `        {`
` 525`  `            { "instructions", instructions ?? "" },`
` 526`  `            { "type", type ?? "Text" },`
` 527`  `            { "score", score },`
` 528`  `            { "extra", extra }`
` 529`  `        };`
` 530`  `        return (instructions ?? "") + "\n<<<META>>>" + Json.Serialize(payload) + "<<<END>>>";`
  - → Pack extra assignment fields into Description JSON meta.
` 531`  `    }`
` 532`  ``
` 533`  `    private static int EnsureCourseWork(SqlConnection conn, int chid, string title, string desc, DateTime due, ref int workCount)`
  - → Database access (pure SQL).
` 534`  `    {`
` 535`  `        if (chid <= 0) return 0;`
` 536`  `        int cwid = ScalarInt(conn,`
` 537`  `            "SELECT TOP 1 CWID FROM CourseWorks WHERE ChID=@Ch AND Title=@T",`
` 538`  `            P("@Ch", chid), P("@T", title));`
` 539`  `        if (cwid > 0) return cwid;`
` 540`  `        try`
  - → Error handling block.
` 541`  `        {`
` 542`  `            cwid = ScalarInt(conn, @"`
` 543`  `INSERT INTO CourseWorks (ChID, Title, Description, DueDate)`
  - → Assignment deadline; submissions close after due day.
` 544`  `VALUES (@Ch, @T, @D, @Due);`
` 545`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 546`  `                P("@Ch", chid), P("@T", title), P("@D", desc), P("@Due", due));`
` 547`  `        }`
` 548`  `        catch`
  - → Handle/log exception.
` 549`  `        {`
` 550`  `            cwid = ScalarInt(conn, @"`
` 551`  `INSERT INTO CourseWorks (ChID, Title, Description)`
` 552`  `VALUES (@Ch, @T, @D);`
` 553`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 554`  `                P("@Ch", chid), P("@T", title), P("@D", desc));`
` 555`  `        }`
` 556`  `        if (cwid > 0) workCount++;`
` 557`  `        return cwid;`
` 558`  `    }`
` 559`  ``
` 560`  `    private static int EnsureSubmission(SqlConnection conn, int cwid, int studentUid, string content, DateTime when, ref int subCount)`
  - → Database access (pure SQL).
` 561`  `    {`
` 562`  `        if (cwid <= 0 || studentUid <= 0) return 0;`
` 563`  `        int sid = ScalarInt(conn,`
` 564`  `            "SELECT TOP 1 SID FROM CWSubmissions WHERE CWID=@C AND StudentUID=@S ORDER BY SID DESC",`
` 565`  `            P("@C", cwid), P("@S", studentUid));`
` 566`  `        if (sid > 0) return sid;`
` 567`  `        try`
  - → Error handling block.
` 568`  `        {`
` 569`  `            sid = ScalarInt(conn, @"`
` 570`  `INSERT INTO CWSubmissions (CWID, StudentUID, SubmissionDate, Content)`
` 571`  `VALUES (@C, @S, @When, @Content);`
` 572`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 573`  `                P("@C", cwid), P("@S", studentUid), P("@When", when), P("@Content", content));`
` 574`  `        }`
` 575`  `        catch`
  - → Handle/log exception.
` 576`  `        {`
` 577`  `            try`
  - → Error handling block.
` 578`  `            {`
` 579`  `                sid = ScalarInt(conn, @"`
` 580`  `INSERT INTO CWSubmissions (CWID, StudentUID, Content)`
` 581`  `VALUES (@C, @S, @Content);`
` 582`  `SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 583`  `                    P("@C", cwid), P("@S", studentUid), P("@Content", content));`
` 584`  `            }`
` 585`  `            catch { return 0; }`
  - → Handle/log exception.
` 586`  `        }`
` 587`  `        if (sid > 0) subCount++;`
` 588`  `        return sid;`
` 589`  `    }`
` 590`  ``
` 591`  `    private static bool EnsureMarking(SqlConnection conn, int sid, int score, string feedback, ref int markCount)`
  - → Database access (pure SQL).
` 592`  `    {`
` 593`  `        if (sid <= 0) return false;`
` 594`  `        if (ScalarInt(conn, "SELECT COUNT(1) FROM CWMarkings WHERE SID=@S", P("@S", sid)) > 0)`
` 595`  `            return false;`
` 596`  `        try`
  - → Error handling block.
` 597`  `        {`
` 598`  `            Exec(conn, "INSERT INTO CWMarkings (SID, Marks, Feedback) VALUES (@S, @Sc, @R)",`
` 599`  `                P("@S", sid), P("@Sc", score), P("@R", feedback ?? ""));`
` 600`  `        }`
` 601`  `        catch`
  - → Handle/log exception.
` 602`  `        {`
` 603`  `            try`
  - → Error handling block.
` 604`  `            {`
` 605`  `                Exec(conn, "INSERT INTO CWMarkings (SID, Marks) VALUES (@S, @Sc)",`
` 606`  `                    P("@S", sid), P("@Sc", score));`
` 607`  `            }`
` 608`  `            catch { return false; }`
  - → Handle/log exception.
` 609`  `        }`
` 610`  `        markCount++;`
` 611`  `        return true;`
` 612`  `    }`
` 613`  ``
` 614`  `    private static SqlParameter P(string n, object v)`
` 615`  `    {`
` 616`  `        return new SqlParameter(n, v ?? DBNull.Value);`
` 617`  `    }`
` 618`  ``
` 619`  `    private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
` 620`  `    {`
` 621`  `        using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
` 622`  `        {`
` 623`  `            if (ps != null) cmd.Parameters.AddRange(ps);`
` 624`  `            cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
` 625`  `        }`
` 626`  `    }`
` 627`  ``
` 628`  `    private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
` 629`  `    {`
` 630`  `        using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
` 631`  `        {`
` 632`  `            if (ps != null) cmd.Parameters.AddRange(ps);`
` 633`  `            var o = cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
` 634`  `            if (o == null || o == DBNull.Value) return 0;`
` 635`  `            return Convert.ToInt32(o);`
` 636`  `        }`
` 637`  `    }`
` 638`  ``
` 639`  `    private static void Write(HttpContext ctx, object o)`
` 640`  `    {`
` 641`  `        ctx.Response.Write(Json.Serialize(o));`
` 642`  `    }`
` 643`  ``
` 644`  `    public bool IsReusable { get { return false; } }`
` 645`  `}`

## Source snapshot (raw)

_File has 645 lines — raw dump omitted here to keep Markdown readable. Open `Pages/Lecturer/SeedMockData.ashx` in the project._
