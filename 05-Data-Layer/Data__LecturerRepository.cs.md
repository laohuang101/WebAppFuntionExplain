# LecturerRepository.cs
**Source:** `Data/LecturerRepository.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Central pure-SQL data access for all lecturer features.

## File overview

- **Total lines:** 1697
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 23:** `Json` — type `JavaScriptSerializer`
- **Line 32:** `dt` — type `DataTable`
- **Line 87:** `list` — type `var`
- **Line 91:** `lessons` — type `int`
- **Line 92:** `published` — type `bool`
- **Line 95:** `published` — type `else`
- **Line 113:** `list` — type `return`
- **Line 120:** `owner` — type `int`
- **Line 138:** `published` — type `return`
- **Line 156:** `0` — type `return`
- **Line 163:** `sql` — type `string`
- **Line 176:** `dt` — type `DataTable`
- **Line 182:** `dt` — type `else`
- **Line 192:** `dt` — type `else`
- **Line 195:** `sb` — type `var`
- **Line 200:** `course` — type `string`
- **Line 201:** `asg` — type `string`
- **Line 202:** `student` — type `string`
- **Line 203:** `email` — type `string`
- **Line 204:** `submitted` — type `string`
- **Line 207:** `score` — type `string`
- **Line 208:** `fb` — type `string`
- **Line 219:** `s` — type `return`
- **Line 230:** `userOk` — type `int`
- **Line 241:** `owner` — type `int`
- **Line 249:** `Name` — type `SET`
- **Line 251:** `CID` — type `WHERE`
- **Line 263:** `insert` — type `string`
- **Line 308:** `owner` — type `int`
- **Line 363:** `chapters` — type `DataTable`
- **Line 378:** `result` — type `var`
- **Line 382:** `chid` — type `int`
- **Line 383:** `lessons` — type `var`
- **Line 384:** `chIndex` — type `int`
- **Line 386:** `subs` — type `DataTable`
- **Line 410:** `schid` — type `int`
- **Line 411:** `type` — type `string`
- **Line 412:** `content` — type `string`
- **Line 413:** `materials` — type `var`
- **Line 417:** `mats` — type `var`
- **Line 441:** `scIndex` — type `int`
- **Line 464:** `result` — type `return`
- **Line 483:** `nextIndex` — type `int`
- **Line 505:** `cid` — type `int`
- **Line 522:** `cid` — type `int`
- **Line 526:** `resolvedSchId` — type `int`
- **Line 530:** `updated` — type `int`
- **Line 543:** `last` — type `Exception`
- **Line 547:** `nextIndex` — type `int`
- **Line 578:** `matType` — type `string`
- **Line 582:** `textContent` — type `string`
- **Line 584:** `mediaLink` — type `string`
- **Line 603:** `materials` — type `var`
- **Line 606:** `matIndex` — type `int`
- **Line 610:** `url` — type `string`
- **Line 611:** `fileName` — type `string`
- **Line 613:** `extType` — type `string`
- **Line 614:** `lower` — type `var`
- **Line 628:** `resolvedSchId` — type `return`
- **Line 685:** `chid` — type `int`
- **Line 686:** `cid` — type `int`
- **Line 697:** `chDt` — type `var`
- **Line 723:** `dt` — type `DataTable`
- **Line 744:** `list` — type `var`
- **Line 748:** `title` — type `string`
- **Line 749:** `desc` — type `string`
- **Line 750:** `packed` — type `var`
- **Line 769:** `list` — type `return`
- **Line 785:** `chid` — type `int`
- **Line 786:** `desc` — type `string`
- **Line 787:** `dueDate` — type `DateTime?`
- **Line 793:** `extra` — type `var`
- **Line 796:** `ds` — type `var`
- **Line 803:** `resolvedCwid` — type `int`
- **Line 807:** `owner` — type `int`
- **Line 816:** `CWID` — type `WHERE`
- **Line 844:** `questions` — type `var`
- **Line 849:** `qText` — type `string`
- **Line 850:** `a` — type `string`
- **Line 855:** `opts` — type `var`
- **Line 860:** `keys` — type `var`
- **Line 869:** `correct` — type `string`
- **Line 873:** `n` — type `var`
- **Line 894:** `resolvedCwid` — type `return`
- **Line 900:** `owner` — type `int`
- **Line 920:** `totalStudents` — type `int`
- **Line 924:** `activeCourses` — type `int`
- **Line 928:** `pendingGrading` — type `int`
- **Line 951:** `trendDt` — type `var`
- **Line 957:** `trends` — type `var`
- **Line 959:** `running` — type `int`
- **Line 960:** `bucket` — type `int`
- **Line 961:** `i` — type `int`
- **Line 974:** `a` — type `int`
- **Line 976:** `sumPct` — type `decimal`
- **Line 977:** `n` — type `int`
- **Line 980:** `gradeDt` — type `DataTable`
- **Line 1009:** `mark` — type `decimal`
- **Line 1011:** `pct` — type `decimal`
- **Line 1022:** `gradeDistribution` — type `var`

## Functions / methods (24 found)

### `SetCoursePublished` — lines 117–139

```
public static bool SetCoursePublished(int lecturerUid, int cid, bool published)
```

#### Explanation

- **Purpose:** Implements `SetCoursePublished`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid, int cid, bool published`
- **Local variables:** `owner`

#### Line-by-line (this function)

` 117`  `        public static bool SetCoursePublished(int lecturerUid, int cid, bool published)`
` 118`  `        {`
` 119`  `            CourseSchema.Ensure();`
` 120`  `            int owner = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 121`  `                "SELECT LecturerUID FROM Courses WHERE CID = @CID", DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 122`  `            if (owner != lecturerUid)`
` 123`  `                throw new UnauthorizedAccessException("Course not found or access denied.");`
` 124`  ``
` 125`  `            try`
  - → Error handling block.
` 126`  `            {`
` 127`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 128`  `                    @"UPDATE Courses SET IsPublished = @P WHERE CID = @CID AND LecturerUID = @L",`
  - → Course publish flag for Landing catalog.
` 129`  `                    DbHelper.P("@P", published ? 1 : 0),`
  - → Database access (pure SQL).
` 130`  `                    DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 131`  `                    DbHelper.P("@L", lecturerUid));`
  - → Database access (pure SQL).
` 132`  `            }`
` 133`  `            catch (Exception ex)`
  - → Handle/log exception.
` 134`  `            {`
` 135`  `                throw new InvalidOperationException(`
` 136`  `                    "Could not update publish state. Ensure Courses.IsPublished exists.", ex);`
  - → Course publish flag for Landing catalog.
` 137`  `            }`
` 138`  `            return published;`
` 139`  `        }`

---

### `CountPendingGrading` — lines 140–158

```
public static int CountPendingGrading(int lecturerUid)
```

#### Explanation

- **Purpose:** Implements `CountPendingGrading`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Parameters:** `int lecturerUid`

#### Line-by-line (this function)

` 140`  ``
` 141`  `        public static int CountPendingGrading(int lecturerUid)`
` 142`  `        {`
` 143`  `            try`
  - → Error handling block.
` 144`  `            {`
` 145`  `                return DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
` 146`  `                SELECT COUNT(*) FROM CWSubmissions s`
` 147`  `                INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 148`  `                INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 149`  `                INNER JOIN Courses c ON c.CID = ch.CID`
` 150`  `                WHERE c.LecturerUID = @LecturerUID`
  - → Owner lecturer foreign key.
` 151`  `                AND NOT EXISTS (SELECT 1 FROM CWMarkings m WHERE m.SID = s.SID)",`
` 152`  `                    DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 153`  `            }`
` 154`  `            catch`
  - → Handle/log exception.
` 155`  `            {`
` 156`  `                return 0;`
` 157`  `            }`
` 158`  `        }`

---

### `BuildGradesCsv` — lines 161–212

```
public static string BuildGradesCsv(int lecturerUid, int cid)
```

#### Explanation

- **Purpose:** Implements `BuildGradesCsv`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Parameters:** `int lecturerUid, int cid`
- **Local variables:** `sql`, `sb`, `course`, `asg`, `student`, `email`, `submitted`, `score`, `fb`

#### Line-by-line (this function)

` 161`  `        public static string BuildGradesCsv(int lecturerUid, int cid)`
  - → CSV export.
` 162`  `        {`
` 163`  `            string sql = @"`
` 164`  `SELECT c.Name AS CourseName, cw.Title AS AssignmentTitle,`
` 165`  `u.Name AS StudentName, u.Email AS StudentEmail,`
` 166`  `s.SubmissionDate, m.Marks AS MarkScore, m.Feedback AS Review`
` 167`  `FROM CWSubmissions s`
` 168`  `INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 169`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 170`  `INNER JOIN Courses c ON c.CID = ch.CID`
` 171`  `INNER JOIN Users u ON u.UID = s.StudentUID`
` 172`  `LEFT JOIN CWMarkings m ON m.SID = s.SID`
` 173`  `WHERE c.LecturerUID = @L";`
  - → Owner lecturer foreign key.
` 174`  `            if (cid > 0) sql += " AND c.CID = @CID";`
` 175`  `            sql += " ORDER BY c.Name, cw.Title, u.Name";`
` 176`  ``
` 177`  `            DataTable dt;`
` 178`  `            try`
  - → Error handling block.
` 179`  `            {`
` 180`  `                if (cid > 0)`
` 181`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid), DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 182`  `                else`
` 183`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid));`
  - → Database access (pure SQL).
` 184`  `            }`
` 185`  `            catch`
  - → Handle/log exception.
` 186`  `            {`
` 187`  `                // legacy Score/Review`
` 188`  `                sql = sql.Replace("m.Marks AS MarkScore", "m.Score AS MarkScore")`
` 189`  `                         .Replace("m.Feedback AS Review", "m.Review AS Review");`
` 190`  `                if (cid > 0)`
` 191`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid), DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 192`  `                else`
` 193`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid));`
  - → Database access (pure SQL).
` 194`  `            }`
` 195`  ``
` 196`  `            var sb = new System.Text.StringBuilder();`
` 197`  `            sb.AppendLine("Course,Assignment,Student,Email,Submitted,Score,Feedback");`
` 198`  `            foreach (DataRow r in dt.Rows)`
` 199`  `            {`
` 200`  `                string course = Csv(DbHelper.SafeString(r["CourseName"]));`
  - → Database access (pure SQL).
` 201`  `                string asg = Csv(DbHelper.SafeString(r["AssignmentTitle"]));`
  - → Database access (pure SQL).
` 202`  `                string student = Csv(DbHelper.SafeString(r["StudentName"]));`
  - → Database access (pure SQL).
` 203`  `                string email = Csv(DbHelper.SafeString(r["StudentEmail"]));`
  - → Database access (pure SQL).
` 204`  `                string submitted = r["SubmissionDate"] == DBNull.Value`
` 205`  `                    ? ""`
` 206`  `                    : Convert.ToDateTime(r["SubmissionDate"]).ToString("yyyy-MM-dd HH:mm");`
` 207`  `                string score = r["MarkScore"] == DBNull.Value ? "" : Convert.ToDecimal(r["MarkScore"]).ToString("0.##");`
` 208`  `                string fb = Csv(r.Table.Columns.Contains("Review") ? DbHelper.SafeString(r["Review"]) : "");`
  - → Database access (pure SQL).
` 209`  `                sb.AppendLine(string.Join(",", course, asg, student, email, Csv(submitted), score, fb));`
  - → CSV export.
` 210`  `            }`
` 211`  `            return sb.ToString();`
` 212`  `        }`

---

### `Csv` — lines 213–220

```
private static string Csv(string s)
```

#### Explanation

- **Purpose:** Implements `Csv`.
- **Parameters:** `string s`

#### Line-by-line (this function)

` 213`  ``
` 214`  `        private static string Csv(string s)`
  - → CSV export.
` 215`  `        {`
` 216`  `            if (s == null) s = "";`
` 217`  `            if (s.IndexOfAny(new[] { ',', '"', '\n', '\r' }) >= 0)`
` 218`  `                return "\"" + s.Replace("\"", "\"\"") + "\"";`
` 219`  `            return s;`
` 220`  `        }`

---

### `SaveCourse` — lines 221–304

```
public static int SaveCourse(int lecturerUid, int? cid, string name, string description, string bgImg, string categories, string level)
```

#### Explanation

- **Purpose:** Implements `SaveCourse`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid, int? cid, string name, string description, string bgImg, string categories, string level`
- **Local variables:** `userOk`, `owner`, `insert`

#### Line-by-line (this function)

` 221`  ``
` 222`  `        public static int SaveCourse(int lecturerUid, int? cid, string name, string description, string bgImg, string categories, string level)`
` 223`  `        {`
` 224`  `            CourseSchema.Ensure();`
` 225`  `            if (lecturerUid <= 0)`
` 226`  `            throw new InvalidOperationException(`
` 227`  `            "Not signed in as a valid user. Log out and log in again as a Lecturer.");`
` 228`  ``
` 229`  `            // FK_Courses_Users_LecturerUID requires LecturerUID to exist in Users.UID`
` 230`  `            int userOk = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 231`  `            "SELECT COUNT(1) FROM Users WHERE UID = @UID",`
` 232`  `            DbHelper.P("@UID", lecturerUid));`
  - → Database access (pure SQL).
` 233`  `            if (userOk <= 0)`
` 234`  `            throw new InvalidOperationException(`
` 235`  `            "Your account (UID=" + lecturerUid + ") was not found in Users. " +`
` 236`  `            "This usually means the database was reset while you stayed logged in. " +`
` 237`  `            "Log out, register/log in again as Lecturer, then create the course.");`
` 238`  ``
` 239`  `            if (cid.HasValue && cid.Value > 0)`
` 240`  `            {`
` 241`  `                int owner = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 242`  `                "SELECT LecturerUID FROM Courses WHERE CID = @CID",`
  - → Owner lecturer foreign key.
` 243`  `                DbHelper.P("@CID", cid.Value));`
  - → Database access (pure SQL).
` 244`  `                if (owner != lecturerUid)`
` 245`  `                throw new UnauthorizedAccessException("Course not found or access denied.");`
` 246`  ``
` 247`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 248`  `                @"UPDATE Courses`
` 249`  `                SET Name = @Name, Description = @Description, BgImg = @BgImg,`
` 250`  `                Categories = @Categories, Level = @Level`
` 251`  `                WHERE CID = @CID AND LecturerUID = @LecturerUID",`
  - → Owner lecturer foreign key.
` 252`  `                DbHelper.P("@Name", name),`
  - → Database access (pure SQL).
` 253`  `                DbHelper.P("@Description", description ?? ""),`
  - → Database access (pure SQL).
` 254`  `                DbHelper.P("@BgImg", bgImg ?? ""),`
  - → Database access (pure SQL).
` 255`  `                DbHelper.P("@Categories", categories ?? ""),`
  - → Database access (pure SQL).
` 256`  `                DbHelper.P("@Level", level ?? ""),`
  - → Database access (pure SQL).
` 257`  `                DbHelper.P("@CID", cid.Value),`
  - → Database access (pure SQL).
` 258`  `                DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 259`  `                return cid.Value;`
` 260`  `            }`
` 261`  ``
` 262`  `            // New courses start as Draft (IsPublished = 0) when column exists`
` 263`  `            string insert = @"`
` 264`  `            INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level, IsPublished)`
  - → Course publish flag for Landing catalog.
` 265`  `            VALUES (@LecturerUID, @Name, @Description, 0, @BgImg, @Categories, @Level, 0);`
  - → Owner lecturer foreign key.
` 266`  `            SELECT CAST(SCOPE_IDENTITY() AS INT);";`
` 267`  `            try`
  - → Error handling block.
` 268`  `            {`
` 269`  `                return DbHelper.ExecuteScalarInt(insert,`
  - → Database access (pure SQL).
` 270`  `                DbHelper.P("@LecturerUID", lecturerUid),`
  - → Database access (pure SQL).
` 271`  `                DbHelper.P("@Name", name),`
  - → Database access (pure SQL).
` 272`  `                DbHelper.P("@Description", description ?? ""),`
  - → Database access (pure SQL).
` 273`  `                DbHelper.P("@BgImg", bgImg ?? ""),`
  - → Database access (pure SQL).
` 274`  `                DbHelper.P("@Categories", categories ?? ""),`
  - → Database access (pure SQL).
` 275`  `                DbHelper.P("@Level", level ?? ""));`
  - → Database access (pure SQL).
` 276`  `            }`
` 277`  `            catch`
  - → Handle/log exception.
` 278`  `            {`
` 279`  `                insert = @"`
` 280`  `                INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level)`
  - → Owner lecturer foreign key.
` 281`  `                VALUES (@LecturerUID, @Name, @Description, 0, @BgImg, @Categories, @Level);`
  - → Owner lecturer foreign key.
` 282`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);";`
` 283`  `                try`
  - → Error handling block.
` 284`  `                {`
` 285`  `                    return DbHelper.ExecuteScalarInt(insert,`
  - → Database access (pure SQL).
` 286`  `                    DbHelper.P("@LecturerUID", lecturerUid),`
  - → Database access (pure SQL).
` 287`  `                    DbHelper.P("@Name", name),`
  - → Database access (pure SQL).
` 288`  `                    DbHelper.P("@Description", description ?? ""),`
  - → Database access (pure SQL).
` 289`  `                    DbHelper.P("@BgImg", bgImg ?? ""),`
  - → Database access (pure SQL).
` 290`  `                    DbHelper.P("@Categories", categories ?? ""),`
  - → Database access (pure SQL).
` 291`  `                    DbHelper.P("@Level", level ?? ""));`
  - → Database access (pure SQL).
` 292`  `                }`
` 293`  `                catch (Exception ex)`
  - → Handle/log exception.
` 294`  `                {`
` 295`  `                    if (ex.Message != null && ex.Message.IndexOf("FK_Courses_Users", StringComparison.OrdinalIgnoreCase) >= 0)`
` 296`  `                    {`
` 297`  `                        throw new InvalidOperationException(`
` 298`  `                        "Cannot create course: lecturer UID " + lecturerUid +`
` 299`  `                        " is not a row in Users (FK_Courses_Users_LecturerUID). Log out and sign in again.", ex);`
  - → Owner lecturer foreign key.
` 300`  `                    }`
` 301`  `                    throw;`
` 302`  `                }`
` 303`  `            }`
` 304`  `        }`

---

### `DeleteCourse` — lines 305–354

```
public static void DeleteCourse(int lecturerUid, int cid)
```

#### Explanation

- **Purpose:** Implements `DeleteCourse`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Delete/clear data.
- **Parameters:** `int lecturerUid, int cid`
- **Local variables:** `owner`

#### Line-by-line (this function)

` 305`  ``
` 306`  `        public static void DeleteCourse(int lecturerUid, int cid)`
` 307`  `        {`
` 308`  `            int owner = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 309`  `            "SELECT LecturerUID FROM Courses WHERE CID = @CID", DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 310`  `            if (owner != lecturerUid)`
` 311`  `            throw new UnauthorizedAccessException("Course not found or access denied.");`
` 312`  ``
` 313`  `            // Best-effort cascade; ignore missing optional tables`
` 314`  `            TryExec(@"`
` 315`  `            DELETE m FROM CWMarkings m`
` 316`  `            INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 317`  `            INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 318`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 319`  `            WHERE ch.CID = @CID;", cid);`
` 320`  ``
` 321`  `            TryExec(@"`
` 322`  `            DELETE s FROM CWSubmissions s`
` 323`  `            INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 324`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 325`  `            WHERE ch.CID = @CID;", cid);`
` 326`  ``
` 327`  `            TryExec(@"`
` 328`  `            DELETE cwp FROM CourseWorkProgresses cwp`
` 329`  `            INNER JOIN CourseWorks cw ON cw.CWID = cwp.CWID`
` 330`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 331`  `            WHERE ch.CID = @CID;", cid);`
` 332`  ``
` 333`  `            TryExec(@"`
` 334`  `            DELETE cw FROM CourseWorks cw`
` 335`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 336`  `            WHERE ch.CID = @CID;", cid);`
` 337`  ``
` 338`  `            TryExec(@"`
` 339`  `            DELETE sm FROM StudyMats sm`
` 340`  `            INNER JOIN SubChapters sc ON sc.SchID = sm.SchID`
` 341`  `            INNER JOIN Chapters ch ON ch.ChID = sc.ChID`
` 342`  `            WHERE ch.CID = @CID;", cid);`
` 343`  ``
` 344`  `            TryExec(@"DELETE sc FROM SubChapters sc INNER JOIN Chapters ch ON ch.ChID = sc.ChID WHERE ch.CID = @CID;", cid);`
` 345`  `            TryExec(@"DELETE FROM Chapters WHERE CID = @CID;", cid);`
` 346`  `            TryExec(@"DELETE FROM Enrollments WHERE CID = @CID;", cid);`
` 347`  `            TryExec(@"DELETE FROM CourseProgresses WHERE CID = @CID;", cid);`
` 348`  `            TryExec(@"DELETE FROM Ratings WHERE CID = @CID;", cid);`
` 349`  ``
` 350`  `            DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 351`  `            "DELETE FROM Courses WHERE CID = @CID AND LecturerUID = @LecturerUID",`
  - → Owner lecturer foreign key.
` 352`  `            DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 353`  `            DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 354`  `        }`

---

### `SaveChapter` — lines 466–501

```
public static int SaveChapter(int lecturerUid, int? chid, int cid, string title)
```

#### Explanation

- **Purpose:** Implements `SaveChapter`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid, int? chid, int cid, string title`
- **Local variables:** `nextIndex`

#### Line-by-line (this function)

` 466`  ``
` 467`  `        public static int SaveChapter(int lecturerUid, int? chid, int cid, string title)`
` 468`  `        {`
` 469`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 470`  ``
` 471`  `            if (chid.HasValue && chid.Value > 0)`
` 472`  `            {`
` 473`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 474`  `                "UPDATE Chapters SET Title = @Title WHERE ChID = @ChID AND CID = @CID",`
` 475`  `                DbHelper.P("@Title", title),`
  - → Database access (pure SQL).
` 476`  `                DbHelper.P("@ChID", chid.Value),`
  - → Database access (pure SQL).
` 477`  `                DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 478`  `                return chid.Value;`
` 479`  `            }`
` 480`  ``
` 481`  `            try`
  - → Error handling block.
` 482`  `            {`
` 483`  `                int nextIndex = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 484`  `                "SELECT ISNULL(MAX([Index]), 0) + 1 FROM Chapters WHERE CID = @CID",`
` 485`  `                DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 486`  `                return DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 487`  `                @"INSERT INTO Chapters (CID, [Index], Title) VALUES (@CID, @Index, @Title);`
` 488`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 489`  `                DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 490`  `                DbHelper.P("@Index", nextIndex),`
  - → Database access (pure SQL).
` 491`  `                DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 492`  `            }`
` 493`  `            catch`
  - → Handle/log exception.
` 494`  `            {`
` 495`  `                return DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 496`  `                @"INSERT INTO Chapters (CID, Title) VALUES (@CID, @Title);`
` 497`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 498`  `                DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 499`  `                DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 500`  `            }`
` 501`  `        }`

---

### `DeleteChapter` — lines 502–518

```
public static void DeleteChapter(int lecturerUid, int chid)
```

#### Explanation

- **Purpose:** Implements `DeleteChapter`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Delete/clear data.
- **Parameters:** `int lecturerUid, int chid`
- **Local variables:** `cid`

#### Line-by-line (this function)

` 502`  ``
` 503`  `        public static void DeleteChapter(int lecturerUid, int chid)`
` 504`  `        {`
` 505`  `            int cid = DbHelper.ExecuteScalarInt("SELECT CID FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 506`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 507`  ``
` 508`  `            TryExec(@"`
` 509`  `            DELETE m FROM CWMarkings m`
` 510`  `            INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 511`  `            INNER JOIN CourseWorks cw ON cw.CWID = s.CWID WHERE cw.ChID = @ChID;", chid, "@ChID");`
` 512`  ``
` 513`  `            TryExec("DELETE s FROM CWSubmissions s INNER JOIN CourseWorks cw ON cw.CWID = s.CWID WHERE cw.ChID = @ChID;", chid, "@ChID");`
` 514`  `            TryExec("DELETE FROM CourseWorks WHERE ChID = @ChID;", chid, "@ChID");`
` 515`  `            TryExec("DELETE sm FROM StudyMats sm INNER JOIN SubChapters sc ON sc.SchID = sm.SchID WHERE sc.ChID = @ChID;", chid, "@ChID");`
` 516`  `            TryExec("DELETE FROM SubChapters WHERE ChID = @ChID;", chid, "@ChID");`
` 517`  `            DbHelper.ExecuteNonQuery("DELETE FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 518`  `        }`

---

### `SaveSubChapter` — lines 519–630

```
public static int SaveSubChapter(int lecturerUid, int? schid, int chid, string title, string type, string content, string materialsJson)
```

#### Explanation

- **Purpose:** Implements `SaveSubChapter`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid, int? schid, int chid, string title, string type, string content, string materialsJson`
- **Local variables:** `cid`, `updated`, `nextIndex`, `matType`, `textContent`, `mediaLink`, `materials`, `matIndex`, `url`, `fileName`, `extType`, `lower`

#### Line-by-line (this function)

` 519`  ``
` 520`  `        public static int SaveSubChapter(int lecturerUid, int? schid, int chid, string title, string type, string content, string materialsJson)`
` 521`  `        {`
` 522`  `            int cid = DbHelper.ExecuteScalarInt("SELECT CID FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 523`  `            if (cid <= 0)`
` 524`  `            throw new InvalidOperationException("Section/chapter not found (ChID=" + chid + "). Save a section first.");`
` 525`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 526`  ``
` 527`  `            int resolvedSchId;`
` 528`  `            if (schid.HasValue && schid.Value > 0)`
` 529`  `            {`
` 530`  `                int updated = DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 531`  `                "UPDATE SubChapters SET Title = @Title WHERE SchID = @SchID AND ChID = @ChID",`
` 532`  `                DbHelper.P("@Title", title),`
  - → Database access (pure SQL).
` 533`  `                DbHelper.P("@SchID", schid.Value),`
  - → Database access (pure SQL).
` 534`  `                DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 535`  `                if (updated <= 0)`
` 536`  `                throw new InvalidOperationException("Lesson not found or does not belong to this section.");`
` 537`  `                resolvedSchId = schid.Value;`
` 538`  `                TryExec("DELETE FROM StudyMats WHERE SchID = @SchID;", resolvedSchId, "@SchID");`
` 539`  `            }`
` 540`  `            else`
` 541`  `            {`
` 542`  `                resolvedSchId = 0;`
` 543`  `                Exception last = null;`
` 544`  `                // Try common column variants for SubChapters`
` 545`  `                try`
  - → Error handling block.
` 546`  `                {`
` 547`  `                    int nextIndex = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 548`  `                    "SELECT ISNULL(MAX([Index]), 0) + 1 FROM SubChapters WHERE ChID = @ChID",`
` 549`  `                    DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 550`  `                    resolvedSchId = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 551`  `                    @"INSERT INTO SubChapters (ChID, [Index], Title) VALUES (@ChID, @Index, @Title);`
` 552`  `                    SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 553`  `                    DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 554`  `                    DbHelper.P("@Index", nextIndex),`
  - → Database access (pure SQL).
` 555`  `                    DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 556`  `                }`
` 557`  `                catch (Exception ex1)`
  - → Handle/log exception.
` 558`  `                {`
` 559`  `                    last = ex1;`
` 560`  `                    try`
  - → Error handling block.
` 561`  `                    {`
` 562`  `                        resolvedSchId = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 563`  `                        @"INSERT INTO SubChapters (ChID, Title) VALUES (@ChID, @Title);`
` 564`  `                        SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 565`  `                        DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 566`  `                        DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 567`  `                    }`
` 568`  `                    catch (Exception ex2)`
  - → Handle/log exception.
` 569`  `                    {`
` 570`  `                        last = ex2;`
` 571`  `                    }`
` 572`  `                }`
` 573`  `                if (resolvedSchId <= 0)`
` 574`  `                throw new InvalidOperationException("Could not create lesson in SubChapters. " + (last != null ? last.Message : ""));`
` 575`  `            }`
` 576`  ``
` 577`  `            // Persist content into StudyMats (best-effort with schema variants)`
` 578`  `            string matType = string.IsNullOrWhiteSpace(type) ? "Text" : type.Trim();`
` 579`  `            // Normalize quiz → text storage`
` 580`  `            if (string.Equals(matType, "Quiz", StringComparison.OrdinalIgnoreCase))`
` 581`  `            matType = "Text";`
` 582`  ``
` 583`  `            string textContent = null;`
` 584`  `            string mediaLink = null;`
` 585`  `            if (string.Equals(matType, "Video", StringComparison.OrdinalIgnoreCase) ||`
` 586`  `            string.Equals(matType, "Image", StringComparison.OrdinalIgnoreCase) ||`
` 587`  `            string.Equals(matType, "PDF", StringComparison.OrdinalIgnoreCase))`
` 588`  `            {`
` 589`  `                mediaLink = content;`
` 590`  `            }`
` 591`  `            else`
` 592`  `            {`
` 593`  `                textContent = content;`
` 594`  `                matType = "Text";`
` 595`  `            }`
` 596`  ``
` 597`  `            InsertStudyMat(resolvedSchId, matType, textContent, mediaLink, 1);`
` 598`  ``
` 599`  `            if (!string.IsNullOrWhiteSpace(materialsJson) && materialsJson.Trim() != "[]")`
` 600`  `            {`
` 601`  `                try`
  - → Error handling block.
` 602`  `                {`
` 603`  `                    var materials = Json.Deserialize<List<Dictionary<string, object>>>(materialsJson);`
` 604`  `                    if (materials != null)`
` 605`  `                    {`
` 606`  `                        int matIndex = 1;`
` 607`  `                        foreach (var m in materials)`
` 608`  `                        {`
` 609`  `                            matIndex++;`
` 610`  `                            string url = m.ContainsKey("url") ? Convert.ToString(m["url"]) : "";`
` 611`  `                            string fileName = m.ContainsKey("fileName") ? Convert.ToString(m["fileName"]) : url;`
` 612`  `                            if (string.IsNullOrWhiteSpace(url)) continue;`
` 613`  `                            string extType = "PDF";`
` 614`  `                            var lower = url.ToLowerInvariant();`
` 615`  `                            if (lower.Contains(".mp4") || lower.Contains(".webm") || lower.Contains(".mov"))`
` 616`  `                            extType = "Video";`
` 617`  `                            else if (lower.Contains(".png") || lower.Contains(".jpg") || lower.Contains(".jpeg") || lower.Contains(".gif") || lower.Contains(".webp"))`
` 618`  `                            extType = "Image";`
` 619`  `                            InsertStudyMat(resolvedSchId, extType, fileName, url, matIndex);`
` 620`  `                        }`
` 621`  `                    }`
` 622`  `                }`
` 623`  `                catch (Exception ex)`
  - → Handle/log exception.
` 624`  `                {`
` 625`  `                    throw new InvalidOperationException("Lesson saved but materials failed: " + ex.Message);`
` 626`  `                }`
` 627`  `            }`
` 628`  ``
` 629`  `            return resolvedSchId;`
` 630`  `        }`

---

### `InsertStudyMat` — lines 631–681

```
private static void InsertStudyMat(int schid, string type, string textContent, string mediaLink, int index)
```

#### Explanation

- **Purpose:** Implements `InsertStudyMat`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Persist changes.
- **Parameters:** `int schid, string type, string textContent, string mediaLink, int index`

#### Line-by-line (this function)

` 631`  ``
` 632`  `        private static void InsertStudyMat(int schid, string type, string textContent, string mediaLink, int index)`
` 633`  `        {`
` 634`  `            // Variant 1: full schema with [Index]`
` 635`  `            try`
  - → Error handling block.
` 636`  `            {`
` 637`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 638`  `                @"INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink, [Index])`
` 639`  `                VALUES (@SchID, @Type, @TextContent, @MediaLink, @Index)",`
` 640`  `                DbHelper.P("@SchID", schid),`
  - → Database access (pure SQL).
` 641`  `                DbHelper.P("@Type", type ?? "Text"),`
  - → Database access (pure SQL).
` 642`  `                DbHelper.P("@TextContent", (object)textContent ?? DBNull.Value),`
  - → Database access (pure SQL).
` 643`  `                DbHelper.P("@MediaLink", (object)mediaLink ?? DBNull.Value),`
  - → Database access (pure SQL).
` 644`  `                DbHelper.P("@Index", index));`
  - → Database access (pure SQL).
` 645`  `                return;`
` 646`  `            }`
` 647`  `            catch { /* try next */ }`
  - → Handle/log exception.
` 648`  ``
` 649`  `            // Variant 2: without Index`
` 650`  `            try`
  - → Error handling block.
` 651`  `            {`
` 652`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 653`  `                @"INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink)`
` 654`  `                VALUES (@SchID, @Type, @TextContent, @MediaLink)",`
` 655`  `                DbHelper.P("@SchID", schid),`
  - → Database access (pure SQL).
` 656`  `                DbHelper.P("@Type", type ?? "Text"),`
  - → Database access (pure SQL).
` 657`  `                DbHelper.P("@TextContent", (object)textContent ?? DBNull.Value),`
  - → Database access (pure SQL).
` 658`  `                DbHelper.P("@MediaLink", (object)mediaLink ?? DBNull.Value));`
  - → Database access (pure SQL).
` 659`  `                return;`
` 660`  `            }`
` 661`  `            catch { /* try next */ }`
  - → Handle/log exception.
` 662`  ``
` 663`  `            // Variant 3: Content / Link column names`
` 664`  `            try`
  - → Error handling block.
` 665`  `            {`
` 666`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 667`  `                @"INSERT INTO StudyMats (SchID, Type, Content, Link)`
` 668`  `                VALUES (@SchID, @Type, @TextContent, @MediaLink)",`
` 669`  `                DbHelper.P("@SchID", schid),`
  - → Database access (pure SQL).
` 670`  `                DbHelper.P("@Type", type ?? "Text"),`
  - → Database access (pure SQL).
` 671`  `                DbHelper.P("@TextContent", (object)textContent ?? DBNull.Value),`
  - → Database access (pure SQL).
` 672`  `                DbHelper.P("@MediaLink", (object)mediaLink ?? DBNull.Value));`
  - → Database access (pure SQL).
` 673`  `                return;`
` 674`  `            }`
` 675`  `            catch (Exception ex)`
  - → Handle/log exception.
` 676`  `            {`
` 677`  `                // Do not fail the whole lesson if StudyMats schema is unknown - `
` 678`  `                // SubChapter row still exists for curriculum listing by title.`
` 679`  `                System.Diagnostics.Debug.WriteLine("StudyMats insert failed: " + ex.Message);`
` 680`  `            }`
` 681`  `        }`

---

### `DeleteSubChapter` — lines 682–691

```
public static void DeleteSubChapter(int lecturerUid, int schid)
```

#### Explanation

- **Purpose:** Implements `DeleteSubChapter`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Delete/clear data.
- **Parameters:** `int lecturerUid, int schid`
- **Local variables:** `chid`, `cid`

#### Line-by-line (this function)

` 682`  ``
` 683`  `        public static void DeleteSubChapter(int lecturerUid, int schid)`
` 684`  `        {`
` 685`  `            int chid = DbHelper.ExecuteScalarInt("SELECT ChID FROM SubChapters WHERE SchID = @SchID", DbHelper.P("@SchID", schid));`
  - → Database access (pure SQL).
` 686`  `            int cid = DbHelper.ExecuteScalarInt("SELECT CID FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 687`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 688`  ``
` 689`  `            TryExec("DELETE FROM StudyMats WHERE SchID = @SchID;", schid, "@SchID");`
` 690`  `            DbHelper.ExecuteNonQuery("DELETE FROM SubChapters WHERE SchID = @SchID", DbHelper.P("@SchID", schid));`
  - → Database access (pure SQL).
` 691`  `        }`

---

### `EnsureAssessmentChapter` — lines 694–703

```
public static int EnsureAssessmentChapter(int lecturerUid, int cid)
```

#### Explanation

- **Purpose:** Implements `EnsureAssessmentChapter`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Parameters:** `int lecturerUid, int cid`
- **Local variables:** `chDt`

#### Line-by-line (this function)

` 694`  `        public static int EnsureAssessmentChapter(int lecturerUid, int cid)`
` 695`  `        {`
` 696`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 697`  `            var chDt = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
` 698`  `            "SELECT TOP 1 ChID FROM Chapters WHERE CID = @CID AND Title = @Title",`
` 699`  `            DbHelper.P("@CID", cid), DbHelper.P("@Title", "Assessments"));`
  - → Database access (pure SQL).
` 700`  `            if (chDt.Rows.Count > 0)`
` 701`  `            return Convert.ToInt32(chDt.Rows[0]["ChID"]);`
` 702`  `            return SaveChapter(lecturerUid, null, cid, "Assessments");`
` 703`  `        }`

---

### `SaveCourseWork` — lines 771–896

```
public static int SaveCourseWork(
        int lecturerUid,
        int? cwid,
        int cid,
        string title,
        string instructions,
        string type,
        decimal score,
        decimal creditGiven,
        string rubricJson,
        string extraMetaJson,
        string objectiveQuestionsJson)
```

#### Explanation

- **Purpose:** Implements `SaveCourseWork`.
- **Due date:** Related to assignment closing after the due day.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid,
        int? cwid,
        int cid,
        string title,
        string instructions,
        string type,
        decimal score,
        decimal creditGiven,
        string rubricJson,
        string extraMetaJson,
      `
- **Local variables:** `chid`, `desc`, `extra`, `ds`, `owner`, `questions`, `qText`, `a`, `opts`, `keys`, `correct`, `n`

#### Line-by-line (this function)

` 771`  ``
` 772`  `        public static int SaveCourseWork(`
` 773`  `        int lecturerUid,`
` 774`  `        int? cwid,`
` 775`  `        int cid,`
` 776`  `        string title,`
` 777`  `        string instructions,`
` 778`  `        string type,`
` 779`  `        decimal score,`
` 780`  `        decimal creditGiven,`
` 781`  `        string rubricJson,`
` 782`  `        string extraMetaJson,`
` 783`  `        string objectiveQuestionsJson)`
` 784`  `        {`
` 785`  `            int chid = EnsureAssessmentChapter(lecturerUid, cid);`
` 786`  `            string desc = PackDescription(instructions, type, score, rubricJson, extraMetaJson, objectiveQuestionsJson);`
` 787`  ``
` 788`  `            DateTime? dueDate = null;`
  - → Assignment deadline; submissions close after due day.
` 789`  `            if (!string.IsNullOrWhiteSpace(extraMetaJson))`
` 790`  `            {`
` 791`  `                try`
  - → Error handling block.
` 792`  `                {`
` 793`  `                    var extra = Json.Deserialize<Dictionary<string, object>>(extraMetaJson);`
` 794`  `                    if (extra != null && extra.ContainsKey("dueDate") && extra["dueDate"] != null)`
  - → Assignment deadline; submissions close after due day.
` 795`  `                    {`
` 796`  `                        var ds = Convert.ToString(extra["dueDate"]);`
  - → Assignment deadline; submissions close after due day.
` 797`  `                        if (!string.IsNullOrWhiteSpace(ds) && DateTime.TryParse(ds, out var d))`
` 798`  `                        dueDate = d;`
  - → Assignment deadline; submissions close after due day.
` 799`  `                    }`
` 800`  `                }`
` 801`  `                catch { }`
  - → Handle/log exception.
` 802`  `            }`
` 803`  ``
` 804`  `            int resolvedCwid;`
` 805`  `            if (cwid.HasValue && cwid.Value > 0)`
` 806`  `            {`
` 807`  `                int owner = DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
` 808`  `                SELECT c.LecturerUID FROM CourseWorks cw`
  - → Owner lecturer foreign key.
` 809`  `                INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 810`  `                INNER JOIN Courses c ON c.CID = ch.CID`
` 811`  `                WHERE cw.CWID = @CWID", DbHelper.P("@CWID", cwid.Value));`
  - → Database access (pure SQL).
` 812`  `                if (owner != lecturerUid) throw new UnauthorizedAccessException("Access denied.");`
` 813`  ``
` 814`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 815`  `                @"UPDATE CourseWorks SET Title = @Title, Description = @Description, DueDate = @DueDate, ChID = @ChID`
  - → Assignment deadline; submissions close after due day.
` 816`  `                WHERE CWID = @CWID",`
` 817`  `                DbHelper.P("@Title", title ?? ""),`
  - → Database access (pure SQL).
` 818`  `                DbHelper.P("@Description", desc),`
  - → Database access (pure SQL).
` 819`  `                DbHelper.P("@DueDate", (object)dueDate ?? DBNull.Value),`
  - → Database access (pure SQL).
` 820`  `                DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 821`  `                DbHelper.P("@CWID", cwid.Value));`
  - → Database access (pure SQL).
` 822`  `                resolvedCwid = cwid.Value;`
` 823`  `            }`
` 824`  `            else`
` 825`  `            {`
` 826`  `                resolvedCwid = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 827`  `                @"INSERT INTO CourseWorks (ChID, Title, Description, DueDate)`
  - → Assignment deadline; submissions close after due day.
` 828`  `                VALUES (@ChID, @Title, @Description, @DueDate);`
  - → Assignment deadline; submissions close after due day.
` 829`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 830`  `                DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 831`  `                DbHelper.P("@Title", title ?? ""),`
  - → Database access (pure SQL).
` 832`  `                DbHelper.P("@Description", desc),`
  - → Database access (pure SQL).
` 833`  `                DbHelper.P("@DueDate", (object)dueDate ?? DBNull.Value));`
  - → Database access (pure SQL).
` 834`  `            }`
` 835`  ``
` 836`  `            // ObjectiveQuestions: QID, QuestionText, OptionA, OptionB, OptionC, OptionD, CorrectAnswer`
` 837`  `            // No CWID on this table in the live schema - store quiz defs also in Description JSON above.`
` 838`  `            // Optionally insert rows for grading auto-check later.`
` 839`  `            if (string.Equals(type, "Objective", StringComparison.OrdinalIgnoreCase) &&`
` 840`  `            !string.IsNullOrWhiteSpace(objectiveQuestionsJson))`
` 841`  `            {`
` 842`  `                try`
  - → Error handling block.
` 843`  `                {`
` 844`  `                    var questions = Json.Deserialize<List<Dictionary<string, object>>>(objectiveQuestionsJson);`
` 845`  `                    if (questions != null)`
` 846`  `                    {`
` 847`  `                        foreach (var q in questions)`
` 848`  `                        {`
` 849`  `                            string qText = q.ContainsKey("question") ? Convert.ToString(q["question"]) : "";`
` 850`  `                            string a = "", b = "", c = "", d = "";`
` 851`  `                            if (q.ContainsKey("options"))`
` 852`  `                            {`
` 853`  `                                try`
  - → Error handling block.
` 854`  `                                {`
` 855`  `                                    var opts = q["options"] as Dictionary<string, object>;`
` 856`  `                                    if (opts == null)`
` 857`  `                                    opts = Json.Deserialize<Dictionary<string, object>>(Json.Serialize(q["options"]));`
` 858`  `                                    if (opts != null)`
` 859`  `                                    {`
` 860`  `                                        var keys = opts.Keys.ToList();`
` 861`  `                                        if (keys.Count > 0) a = Convert.ToString(opts[keys[0]]);`
` 862`  `                                        if (keys.Count > 1) b = Convert.ToString(opts[keys[1]]);`
` 863`  `                                        if (keys.Count > 2) c = Convert.ToString(opts[keys[2]]);`
` 864`  `                                        if (keys.Count > 3) d = Convert.ToString(opts[keys[3]]);`
` 865`  `                                    }`
` 866`  `                                }`
` 867`  `                                catch { }`
  - → Handle/log exception.
` 868`  `                            }`
` 869`  `                            string correct = q.ContainsKey("answer") ? Convert.ToString(q["answer"]) : "A";`
` 870`  `                            // Map option1 -> A etc.`
` 871`  `                            if (correct != null && correct.StartsWith("option", StringComparison.OrdinalIgnoreCase))`
` 872`  `                            {`
` 873`  `                                var n = correct.Replace("option", "").Replace("Option", "");`
` 874`  `                                if (n == "1") correct = "A";`
` 875`  `                                else if (n == "2") correct = "B";`
` 876`  `                                else if (n == "3") correct = "C";`
` 877`  `                                else if (n == "4") correct = "D";`
` 878`  `                            }`
` 879`  ``
` 880`  `                            DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 881`  `                            @"INSERT INTO ObjectiveQuestions (QuestionText, OptionA, OptionB, OptionC, OptionD, CorrectAnswer)`
` 882`  `                            VALUES (@Q, @A, @B, @C, @D, @Correct)",`
` 883`  `                            DbHelper.P("@Q", qText),`
  - → Database access (pure SQL).
` 884`  `                            DbHelper.P("@A", a ?? ""),`
  - → Database access (pure SQL).
` 885`  `                            DbHelper.P("@B", b ?? ""),`
  - → Database access (pure SQL).
` 886`  `                            DbHelper.P("@C", c ?? ""),`
  - → Database access (pure SQL).
` 887`  `                            DbHelper.P("@D", d ?? ""),`
  - → Database access (pure SQL).
` 888`  `                            DbHelper.P("@Correct", correct ?? "A"));`
  - → Database access (pure SQL).
` 889`  `                        }`
` 890`  `                    }`
` 891`  `                }`
` 892`  `                catch { /* optional */ }`
  - → Handle/log exception.
` 893`  `            }`
` 894`  ``
` 895`  `            return resolvedCwid;`
` 896`  `        }`

---

### `DeleteCourseWork` — lines 897–911

```
public static void DeleteCourseWork(int lecturerUid, int cwid)
```

#### Explanation

- **Purpose:** Implements `DeleteCourseWork`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Delete/clear data.
- **Parameters:** `int lecturerUid, int cwid`
- **Local variables:** `owner`

#### Line-by-line (this function)

` 897`  ``
` 898`  `        public static void DeleteCourseWork(int lecturerUid, int cwid)`
` 899`  `        {`
` 900`  `            int owner = DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
` 901`  `            SELECT c.LecturerUID FROM CourseWorks cw`
  - → Owner lecturer foreign key.
` 902`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 903`  `            INNER JOIN Courses c ON c.CID = ch.CID`
` 904`  `            WHERE cw.CWID = @CWID", DbHelper.P("@CWID", cwid));`
  - → Database access (pure SQL).
` 905`  `            if (owner != lecturerUid) throw new UnauthorizedAccessException("Access denied.");`
` 906`  ``
` 907`  `            TryExec("DELETE m FROM CWMarkings m INNER JOIN CWSubmissions s ON s.SID = m.SID WHERE s.CWID = @CWID;", cwid, "@CWID");`
` 908`  `            TryExec("DELETE FROM CWSubmissions WHERE CWID = @CWID;", cwid, "@CWID");`
` 909`  `            TryExec("DELETE FROM CourseWorkProgresses WHERE CWID = @CWID;", cwid, "@CWID");`
` 910`  `            DbHelper.ExecuteNonQuery("DELETE FROM CourseWorks WHERE CWID = @CWID", DbHelper.P("@CWID", cwid));`
  - → Database access (pure SQL).
` 911`  `        }`

---

### `ParseSubmissionContent` — lines 1180–1216

```
public static void ParseSubmissionContent(string raw, out string text, out string file, out string fileName)
```

#### Explanation

- **Purpose:** Implements `ParseSubmissionContent`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `string raw, out string text, out string file, out string fileName`
- **Local variables:** `o`, `a`, `b`

#### Line-by-line (this function)

`1180`  `        public static void ParseSubmissionContent(string raw, out string text, out string file, out string fileName)`
`1181`  `        {`
`1182`  `            text = "";`
`1183`  `            file = "";`
`1184`  `            fileName = "";`
`1185`  `            if (string.IsNullOrWhiteSpace(raw)) return;`
`1186`  `            raw = raw.Trim();`
`1187`  `            if (raw.StartsWith("{"))`
`1188`  `            {`
`1189`  `                try`
  - → Error handling block.
`1190`  `                {`
`1191`  `                    var o = Json.Deserialize<Dictionary<string, object>>(raw);`
`1192`  `                    if (o != null)`
`1193`  `                    {`
`1194`  `                        if (o.ContainsKey("text")) text = Convert.ToString(o["text"]) ?? "";`
`1195`  `                        if (o.ContainsKey("file")) file = Convert.ToString(o["file"]) ?? "";`
`1196`  `                        if (string.IsNullOrEmpty(file) && o.ContainsKey("fileUrl"))`
`1197`  `                        file = Convert.ToString(o["fileUrl"]) ?? "";`
`1198`  `                        if (o.ContainsKey("fileName")) fileName = Convert.ToString(o["fileName"]) ?? "";`
`1199`  `                        if (string.IsNullOrEmpty(fileName) && !string.IsNullOrEmpty(file))`
`1200`  `                        fileName = System.IO.Path.GetFileName(file.Replace('\\', '/'));`
`1201`  `                        return;`
`1202`  `                    }`
`1203`  `                }`
`1204`  `                catch { /* plain text */ }`
  - → Handle/log exception.
`1205`  `            }`
`1206`  `            int a = raw.IndexOf("<<<FILE>>>", StringComparison.OrdinalIgnoreCase);`
`1207`  `            int b = raw.IndexOf("<<<ENDFILE>>>", StringComparison.OrdinalIgnoreCase);`
`1208`  `            if (a >= 0 && b > a)`
`1209`  `            {`
`1210`  `                file = raw.Substring(a + "<<<FILE>>>".Length, b - a - "<<<FILE>>>".Length).Trim();`
`1211`  `                text = (raw.Substring(0, a) + raw.Substring(b + "<<<ENDFILE>>>".Length)).Trim();`
`1212`  `                fileName = System.IO.Path.GetFileName(file.Replace('\\', '/'));`
`1213`  `                return;`
`1214`  `            }`
`1215`  `            text = raw;`
`1216`  `        }`

---

### `SaveGrade` — lines 1217–1296

```
public static void SaveGrade(int lecturerUid, int sid, decimal score, string review)
```

#### Explanation

- **Purpose:** Implements `SaveGrade`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid, int sid, decimal score, string review`
- **Local variables:** `owner`, `existing`

#### Line-by-line (this function)

`1217`  ``
`1218`  `        public static void SaveGrade(int lecturerUid, int sid, decimal score, string review)`
`1219`  `        {`
`1220`  `            int owner = DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
`1221`  `            SELECT c.LecturerUID FROM CWSubmissions s`
  - → Owner lecturer foreign key.
`1222`  `            INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
`1223`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
`1224`  `            INNER JOIN Courses c ON c.CID = ch.CID`
`1225`  `            WHERE s.SID = @SID", DbHelper.P("@SID", sid));`
  - → Database access (pure SQL).
`1226`  `            if (owner != lecturerUid) throw new UnauthorizedAccessException("Access denied.");`
`1227`  ``
`1228`  `            int existing = 0;`
`1229`  `            try`
  - → Error handling block.
`1230`  `            {`
`1231`  `                existing = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
`1232`  `                "SELECT COUNT(*) FROM CWMarkings WHERE SID = @SID", DbHelper.P("@SID", sid));`
  - → Database access (pure SQL).
`1233`  `            }`
`1234`  `            catch { existing = 0; }`
  - → Handle/log exception.
`1235`  ``
`1236`  `            // Live schema: Marks + Feedback`
`1237`  `            if (existing > 0)`
`1238`  `            {`
`1239`  `                try`
  - → Error handling block.
`1240`  `                {`
`1241`  `                    DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
`1242`  `                    @"UPDATE CWMarkings SET Marks = @Score, Feedback = @Review WHERE SID = @SID",`
`1243`  `                    DbHelper.P("@Score", score),`
  - → Database access (pure SQL).
`1244`  `                    DbHelper.P("@Review", review ?? ""),`
  - → Database access (pure SQL).
`1245`  `                    DbHelper.P("@SID", sid));`
  - → Database access (pure SQL).
`1246`  `                    return;`
`1247`  `                }`
`1248`  `                catch`
  - → Handle/log exception.
`1249`  `                {`
`1250`  `                    try`
  - → Error handling block.
`1251`  `                    {`
`1252`  `                        DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
`1253`  `                        @"UPDATE CWMarkings SET Score = @Score, Review = @Review WHERE SID = @SID",`
`1254`  `                        DbHelper.P("@Score", score),`
  - → Database access (pure SQL).
`1255`  `                        DbHelper.P("@Review", review ?? ""),`
  - → Database access (pure SQL).
`1256`  `                        DbHelper.P("@SID", sid));`
  - → Database access (pure SQL).
`1257`  `                        return;`
`1258`  `                    }`
`1259`  `                    catch`
  - → Handle/log exception.
`1260`  `                    {`
`1261`  `                        DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
`1262`  `                        @"UPDATE CWMarkings SET Marks = @Score WHERE SID = @SID",`
`1263`  `                        DbHelper.P("@Score", score),`
  - → Database access (pure SQL).
`1264`  `                        DbHelper.P("@SID", sid));`
  - → Database access (pure SQL).
`1265`  `                        return;`
`1266`  `                    }`
`1267`  `                }`
`1268`  `            }`
`1269`  ``
`1270`  `            try`
  - → Error handling block.
`1271`  `            {`
`1272`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
`1273`  `                @"INSERT INTO CWMarkings (SID, Marks, Feedback) VALUES (@SID, @Score, @Review)",`
`1274`  `                DbHelper.P("@SID", sid),`
  - → Database access (pure SQL).
`1275`  `                DbHelper.P("@Score", score),`
  - → Database access (pure SQL).
`1276`  `                DbHelper.P("@Review", review ?? ""));`
  - → Database access (pure SQL).
`1277`  `            }`
`1278`  `            catch`
  - → Handle/log exception.
`1279`  `            {`
`1280`  `                try`
  - → Error handling block.
`1281`  `                {`
`1282`  `                    DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
`1283`  `                    @"INSERT INTO CWMarkings (SID, Score, Review) VALUES (@SID, @Score, @Review)",`
`1284`  `                    DbHelper.P("@SID", sid),`
  - → Database access (pure SQL).
`1285`  `                    DbHelper.P("@Score", score),`
  - → Database access (pure SQL).
`1286`  `                    DbHelper.P("@Review", review ?? ""));`
  - → Database access (pure SQL).
`1287`  `                }`
`1288`  `                catch`
  - → Handle/log exception.
`1289`  `                {`
`1290`  `                    DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
`1291`  `                    @"INSERT INTO CWMarkings (SID, Marks) VALUES (@SID, @Score)",`
`1292`  `                    DbHelper.P("@SID", sid),`
  - → Database access (pure SQL).
`1293`  `                    DbHelper.P("@Score", score));`
  - → Database access (pure SQL).
`1294`  `                }`
`1295`  `            }`
`1296`  `        }`

---

### `AssertCourseOwner` — lines 1503–1510

```
private static void AssertCourseOwner(int lecturerUid, int cid)
```

#### Explanation

- **Purpose:** Implements `AssertCourseOwner`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Parameters:** `int lecturerUid, int cid`
- **Local variables:** `owner`

#### Line-by-line (this function)

`1503`  ``
`1504`  `        private static void AssertCourseOwner(int lecturerUid, int cid)`
  - → Ownership check — prevent IDOR.
`1505`  `        {`
`1506`  `            int owner = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
`1507`  `            "SELECT LecturerUID FROM Courses WHERE CID = @CID", DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
`1508`  `            if (owner != lecturerUid)`
`1509`  `            throw new UnauthorizedAccessException("Course not found or access denied.");`
`1510`  `        }`

---

### `TryExec` — lines 1511–1516

```
private static void TryExec(string sql, int id, string paramName = "@CID")
```

#### Explanation

- **Purpose:** Implements `TryExec`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string sql, int id, string paramName = "@CID"`
- **Local variables:** `paramName`

#### Line-by-line (this function)

`1511`  ``
`1512`  `        private static void TryExec(string sql, int id, string paramName = "@CID")`
`1513`  `        {`
`1514`  `            try { DbHelper.ExecuteNonQuery(sql, DbHelper.P(paramName, id)); }`
  - → Database access (pure SQL).
`1515`  `            catch { /* table/column may not exist */ }`
  - → Handle/log exception.
`1516`  `        }`

---

### `PackDescription` — lines 1532–1559

```
private static string PackDescription(string instructions, string type, decimal score,
        string rubricJson, string extraMetaJson, string objectiveQuestionsJson)
```

#### Explanation

- **Purpose:** Implements `PackDescription`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `string instructions, string type, decimal score,
        string rubricJson, string extraMetaJson, string objectiveQuestionsJson`
- **Local variables:** `payload`, `plain`

#### Line-by-line (this function)

`1532`  `        private static string PackDescription(string instructions, string type, decimal score,`
`1533`  `        string rubricJson, string extraMetaJson, string objectiveQuestionsJson)`
`1534`  `        {`
`1535`  `            var payload = new Dictionary<string, object>`
`1536`  `            {`
`1537`  `                { "instructions", instructions ?? "" },`
`1538`  `                { "type", string.IsNullOrWhiteSpace(type) ? "Text" : type },`
`1539`  `                { "score", score }`
`1540`  `            };`
`1541`  `            if (!string.IsNullOrWhiteSpace(rubricJson))`
`1542`  `            {`
`1543`  `                try { payload["rubric"] = Json.Deserialize<List<Dictionary<string, object>>>(rubricJson); }`
  - → Error handling block.
`1544`  `                catch { payload["rubric"] = rubricJson; }`
  - → Handle/log exception.
`1545`  `            }`
`1546`  `            if (!string.IsNullOrWhiteSpace(extraMetaJson))`
`1547`  `            {`
`1548`  `                try { payload["extra"] = Json.Deserialize<Dictionary<string, object>>(extraMetaJson); }`
  - → Error handling block.
`1549`  `                catch { payload["extra"] = extraMetaJson; }`
  - → Handle/log exception.
`1550`  `            }`
`1551`  `            if (!string.IsNullOrWhiteSpace(objectiveQuestionsJson))`
`1552`  `            {`
`1553`  `                try { payload["questions"] = Json.Deserialize<List<Dictionary<string, object>>>(objectiveQuestionsJson); }`
  - → Error handling block.
`1554`  `                catch { payload["questions"] = objectiveQuestionsJson; }`
  - → Handle/log exception.
`1555`  `            }`
`1556`  ``
`1557`  `            string plain = instructions ?? "";`
`1558`  `            return plain + "\n<<<META>>>" + Json.Serialize(payload) + "<<<END>>>";`
  - → Pack extra assignment fields into Description JSON meta.
`1559`  `        }`

---

### `ParseDescriptionMeta` — lines 1560–1596

```
private static DescMeta ParseDescriptionMeta(string desc)
```

#### Explanation

- **Purpose:** Implements `ParseDescriptionMeta`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `string desc`
- **Local variables:** `meta`, `start`, `end`, `json`, `dict`

#### Line-by-line (this function)

`1560`  ``
`1561`  `        private static DescMeta ParseDescriptionMeta(string desc)`
`1562`  `        {`
`1563`  `            var meta = new DescMeta`
`1564`  `            {`
`1565`  `                Instructions = desc ?? "",`
`1566`  `                Type = "Text",`
`1567`  `                Score = 100m`
`1568`  `            };`
`1569`  `            if (string.IsNullOrEmpty(desc)) return meta;`
`1570`  ``
`1571`  `            int start = desc.IndexOf("<<<META>>>", StringComparison.Ordinal);`
  - → Pack extra assignment fields into Description JSON meta.
`1572`  `            int end = desc.IndexOf("<<<END>>>", StringComparison.Ordinal);`
`1573`  `            if (start < 0 || end < 0 || end <= start)`
`1574`  `            {`
`1575`  `                meta.Instructions = desc;`
`1576`  `                return meta;`
`1577`  `            }`
`1578`  ``
`1579`  `            meta.Instructions = desc.Substring(0, start).Trim();`
`1580`  `            string json = desc.Substring(start + "<<<META>>>".Length, end - start - "<<<META>>>".Length);`
  - → Pack extra assignment fields into Description JSON meta.
`1581`  `            try`
  - → Error handling block.
`1582`  `            {`
`1583`  `                var dict = Json.Deserialize<Dictionary<string, object>>(json);`
`1584`  `                if (dict != null)`
`1585`  `                {`
`1586`  `                    if (dict.ContainsKey("instructions")) meta.Instructions = Convert.ToString(dict["instructions"]);`
`1587`  `                    if (dict.ContainsKey("type")) meta.Type = Convert.ToString(dict["type"]);`
`1588`  `                    if (dict.ContainsKey("score")) meta.Score = Convert.ToDecimal(dict["score"]);`
`1589`  `                    if (dict.ContainsKey("rubric")) meta.Rubric = dict["rubric"];`
`1590`  `                    if (dict.ContainsKey("extra")) meta.Extra = dict["extra"];`
`1591`  `                    if (dict.ContainsKey("questions")) meta.Questions = dict["questions"];`
`1592`  `                }`
`1593`  `            }`
`1594`  `            catch { }`
  - → Handle/log exception.
`1595`  `            return meta;`
`1596`  `        }`

---

### `LoadGradeScales` — lines 1597–1650

```
private static List<GradeScaleRow> LoadGradeScales()
```

#### Explanation

- **Purpose:** Implements `LoadGradeScales`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Local variables:** `dt`, `list`, `min`, `max`

#### Line-by-line (this function)

`1597`  ``
`1598`  `        private static List<GradeScaleRow> LoadGradeScales()`
`1599`  `        {`
`1600`  `            // Live schema: GID, GradeLetter, MinMarks, MaxMarks`
`1601`  `            try`
  - → Error handling block.
`1602`  `            {`
`1603`  `                var dt = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
`1604`  `                "SELECT GID, GradeLetter, MinMarks, MaxMarks FROM GradeScales ORDER BY MinMarks DESC");`
`1605`  `                var list = new List<GradeScaleRow>();`
`1606`  `                foreach (DataRow r in dt.Rows)`
`1607`  `                {`
`1608`  `                    decimal min = r["MinMarks"] == DBNull.Value ? 0 : Convert.ToDecimal(r["MinMarks"]);`
`1609`  `                    decimal max = r["MaxMarks"] == DBNull.Value ? 100 : Convert.ToDecimal(r["MaxMarks"]);`
`1610`  `                    list.Add(new GradeScaleRow`
`1611`  `                    {`
`1612`  `                        GSID = Convert.ToInt32(r["GID"]),`
`1613`  `                        ScoreRange = min.ToString("0") + "-" + max.ToString("0"),`
`1614`  `                        Grade = DbHelper.SafeString(r["GradeLetter"]),`
  - → Database access (pure SQL).
`1615`  `                        MinMarks = min,`
`1616`  `                        MaxMarks = max`
`1617`  `                    });`
`1618`  `                }`
`1619`  `                if (list.Count > 0) return list;`
`1620`  `            }`
`1621`  `            catch`
  - → Handle/log exception.
`1622`  `            {`
`1623`  `                try`
  - → Error handling block.
`1624`  `                {`
`1625`  `                    var dt = DbHelper.ExecuteQuery("SELECT GSID, ScoreRange, Grade FROM GradeScales");`
  - → Database access (pure SQL).
`1626`  `                    var list = new List<GradeScaleRow>();`
`1627`  `                    foreach (DataRow r in dt.Rows)`
`1628`  `                    {`
`1629`  `                        list.Add(new GradeScaleRow`
`1630`  `                        {`
`1631`  `                            GSID = Convert.ToInt32(r["GSID"]),`
`1632`  `                            ScoreRange = DbHelper.SafeString(r["ScoreRange"]),`
  - → Database access (pure SQL).
`1633`  `                            Grade = DbHelper.SafeString(r["Grade"])`
  - → Database access (pure SQL).
`1634`  `                        });`
`1635`  `                    }`
`1636`  `                    if (list.Count > 0) return list;`
`1637`  `                }`
`1638`  `                catch { }`
  - → Handle/log exception.
`1639`  `            }`
`1640`  ``
`1641`  `            return new List<GradeScaleRow>`
`1642`  `            {`
`1643`  `                new GradeScaleRow { ScoreRange = "90-100", Grade = "A+", MinMarks = 90, MaxMarks = 100 },`
`1644`  `                new GradeScaleRow { ScoreRange = "80-89", Grade = "A", MinMarks = 80, MaxMarks = 89 },`
`1645`  `                new GradeScaleRow { ScoreRange = "70-79", Grade = "B", MinMarks = 70, MaxMarks = 79 },`
`1646`  `                new GradeScaleRow { ScoreRange = "60-69", Grade = "C", MinMarks = 60, MaxMarks = 69 },`
`1647`  `                new GradeScaleRow { ScoreRange = "50-59", Grade = "D", MinMarks = 50, MaxMarks = 59 },`
`1648`  `                new GradeScaleRow { ScoreRange = "0-49", Grade = "F", MinMarks = 0, MaxMarks = 49 }`
`1649`  `            };`
`1650`  `        }`

---

### `MapGrade` — lines 1651–1675

```
private static string MapGrade(decimal pct, List<GradeScaleRow> scales)
```

#### Explanation

- **Purpose:** Implements `MapGrade`.
- **Parameters:** `decimal pct, List<GradeScaleRow> scales`
- **Local variables:** `parts`

#### Line-by-line (this function)

`1651`  ``
`1652`  `        private static string MapGrade(decimal pct, List<GradeScaleRow> scales)`
`1653`  `        {`
`1654`  `            foreach (var s in scales)`
`1655`  `            {`
`1656`  `                // Live GradeScales: MinMarks / MaxMarks`
`1657`  `                if (s.MaxMarks > 0 || s.MinMarks > 0 || string.Equals(s.Grade, "F", StringComparison.OrdinalIgnoreCase))`
`1658`  `                {`
`1659`  `                    if (pct >= s.MinMarks && pct <= s.MaxMarks)`
`1660`  `                    return s.Grade;`
`1661`  `                }`
`1662`  `                var parts = (s.ScoreRange ?? "").Split('-');`
`1663`  `                if (parts.Length == 2 &&`
`1664`  `                decimal.TryParse(parts[0].Trim(), out var lo) &&`
`1665`  `                decimal.TryParse(parts[1].Trim(), out var hi))`
`1666`  `                {`
`1667`  `                    if (pct >= lo && pct <= hi) return s.Grade;`
`1668`  `                }`
`1669`  `            }`
`1670`  `            if (pct >= 90) return "A";`
`1671`  `            if (pct >= 80) return "B";`
`1672`  `            if (pct >= 70) return "C";`
`1673`  `            if (pct >= 60) return "D";`
`1674`  `            return "F";`
`1675`  `        }`

---

### `GetInitials` — lines 1676–1684

```
public static string GetInitials(string name)
```

#### Explanation

- **Purpose:** Implements `GetInitials`.
- **Pattern:** Read/load data for display.
- **Parameters:** `string name`
- **Local variables:** `parts`

#### Line-by-line (this function)

`1676`  ``
`1677`  `        public static string GetInitials(string name)`
`1678`  `        {`
`1679`  `            if (string.IsNullOrWhiteSpace(name)) return "?";`
`1680`  `            var parts = name.Trim().Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);`
`1681`  `            if (parts.Length >= 2)`
`1682`  `            return (parts[0][0].ToString() + parts[parts.Length - 1][0]).ToUpperInvariant();`
`1683`  `            return parts[0].Substring(0, Math.Min(2, parts[0].Length)).ToUpperInvariant();`
`1684`  `        }`

---

### `FormatRelativeTime` — lines 1685–1695

```
public static string FormatRelativeTime(DateTime ts)
```

#### Explanation

- **Purpose:** Implements `FormatRelativeTime`.
- **Parameters:** `DateTime ts`
- **Local variables:** `span`

#### Line-by-line (this function)

`1685`  ``
`1686`  `        public static string FormatRelativeTime(DateTime ts)`
`1687`  `        {`
`1688`  `            var span = DateTime.Now - ts;`
`1689`  `            if (span.TotalMinutes < 1) return "Just now";`
`1690`  `            if (span.TotalMinutes < 60) return (int)span.TotalMinutes + " minutes ago";`
`1691`  `            if (span.TotalHours < 24) return (int)span.TotalHours + " hours ago";`
`1692`  `            if (span.TotalDays < 2) return "Yesterday";`
`1693`  `            if (span.TotalDays < 7) return (int)span.TotalDays + " days ago";`
`1694`  `            return ts.ToString("MMM dd, yyyy");`
`1695`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Collections.Generic;`
  - → Import namespace/types.
`   3`  `using System.Data;`
  - → Import namespace/types.
`   4`  `using System.Linq;`
  - → Import namespace/types.
`   5`  `using System.Web.Script.Serialization;`
  - → Import namespace/types.
`   6`  ``
`   7`  `namespace WebAppAssignment.Data`
  - → C# namespace grouping.
`   8`  `{`
`   9`  `    /// <summary>`
`  10`  `    /// Pure SQL matched to the LIVE EduDB.mdf schema (VS Server Explorer):`
`  11`  `    ///`
`  12`  `    /// Courses: CID, LecturerUID, Name, Description, Rating, BgImg, Categories, Level`
`  13`  `    /// Enrollments: CID, StudentUID, Progress`
`  14`  `    /// CourseWorks: CWID, ChID, Title, Description, DueDate`
`  15`  `    /// CWSubmissions: SID, CWID, StudentUID, SubmissionDate, Content`
`  16`  `    /// CWMarkings: MarkID, SID, Marks, Feedback (live Server Explorer)`
`  17`  `    /// ObjectiveQuestions: QID, QuestionText, OptionA-D, CorrectAnswer`
`  18`  `    /// ObjectiveAnswers: AnswerID, QID, StudentUID, SelectedAnswer, IsCorrect`
`  19`  `    /// GradeScales, CourseWorkProgresses, Chapters, SubChapters, StudyMats, Users`
`  20`  `    /// </summary>`
`  21`  `    public static class LecturerRepository`
`  22`  `    {`
`  23`  `        private static readonly JavaScriptSerializer Json = new JavaScriptSerializer();`
`  24`  ``
`  25`  `        // ═══════════════════════════════════════════════════════════════════`
`  26`  `        // Courses (CID, LecturerUID, Name, Description, Rating, BgImg, Categories, Level)`
`  27`  `        // ═══════════════════════════════════════════════════════════════════`
`  28`  ``
`  29`  `        public static List<Dictionary<string, object>> GetCoursesForLecturer(int lecturerUid)`
`  30`  `        {`
`  31`  `            CourseSchema.Ensure();`
`  32`  `            DataTable dt = null;`
`  33`  `            // Prefer IsPublished + set-based counts (faster than per-row correlated subqueries)`
`  34`  `            try`
  - → Error handling block.
`  35`  `            {`
`  36`  `                const string sql = @"`
`  37`  `                SELECT c.CID, c.LecturerUID, c.Name, c.Description, c.Rating, c.BgImg, c.Categories, c.Level,`
  - → Owner lecturer foreign key.
`  38`  `                ISNULL(c.IsPublished, 0) AS IsPublished,`
  - → Course publish flag for Landing catalog.
`  39`  `                ISNULL(ec.StudentsCount, 0) AS StudentsCount,`
`  40`  `                ISNULL(lc.LessonsCount, 0) AS LessonsCount`
`  41`  `                FROM Courses c`
`  42`  `                LEFT JOIN (`
`  43`  `                    SELECT e.CID, COUNT(*) AS StudentsCount`
`  44`  `                    FROM Enrollments e`
`  45`  `                    INNER JOIN Users u ON u.UID = e.StudentUID`
`  46`  `                    GROUP BY e.CID`
`  47`  `                ) ec ON ec.CID = c.CID`
`  48`  `                LEFT JOIN (`
`  49`  `                    SELECT ch.CID, COUNT(*) AS LessonsCount`
`  50`  `                    FROM Chapters ch`
`  51`  `                    INNER JOIN SubChapters sc ON sc.ChID = ch.ChID`
`  52`  `                    GROUP BY ch.CID`
`  53`  `                ) lc ON lc.CID = c.CID`
`  54`  `                WHERE c.LecturerUID = @LecturerUID`
  - → Owner lecturer foreign key.
`  55`  `                ORDER BY c.CID DESC";`
`  56`  `                dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
`  57`  `            }`
`  58`  `            catch`
  - → Handle/log exception.
`  59`  `            {`
`  60`  `                try`
  - → Error handling block.
`  61`  `                {`
`  62`  `                    const string sql2 = @"`
`  63`  `                    SELECT c.CID, c.LecturerUID, c.Name, c.Description, c.Rating, c.BgImg, c.Categories, c.Level,`
  - → Owner lecturer foreign key.
`  64`  `                    (SELECT COUNT(*) FROM Enrollments e`
`  65`  `                    INNER JOIN Users u ON u.UID = e.StudentUID`
`  66`  `                    WHERE e.CID = c.CID) AS StudentsCount,`
`  67`  `                    (SELECT COUNT(*) FROM Chapters ch`
`  68`  `                    INNER JOIN SubChapters sc ON sc.ChID = ch.ChID`
`  69`  `                    WHERE ch.CID = c.CID) AS LessonsCount`
`  70`  `                    FROM Courses c`
`  71`  `                    WHERE c.LecturerUID = @LecturerUID`
  - → Owner lecturer foreign key.
`  72`  `                    ORDER BY c.CID DESC";`
`  73`  `                    dt = DbHelper.ExecuteQuery(sql2, DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
`  74`  `                }`
`  75`  `                catch`
  - → Handle/log exception.
`  76`  `                {`
`  77`  `                    const string sql3 = @"`
`  78`  `                    SELECT c.CID, c.LecturerUID, c.Name, c.Description, c.Rating, c.BgImg, c.Categories, c.Level,`
  - → Owner lecturer foreign key.
`  79`  `                    (SELECT COUNT(*) FROM Enrollments e WHERE e.CID = c.CID) AS StudentsCount,`
`  80`  `                    (SELECT COUNT(*) FROM Chapters ch WHERE ch.CID = c.CID) AS LessonsCount`
`  81`  `                    FROM Courses c`
`  82`  `                    WHERE c.LecturerUID = @LecturerUID`
  - → Owner lecturer foreign key.
`  83`  `                    ORDER BY c.CID DESC";`
`  84`  `                    dt = DbHelper.ExecuteQuery(sql3, DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
`  85`  `                }`
`  86`  `            }`
`  87`  ``
`  88`  `            var list = new List<Dictionary<string, object>>();`
`  89`  `            foreach (DataRow r in dt.Rows)`
`  90`  `            {`
`  91`  `                int lessons = Convert.ToInt32(r["LessonsCount"]);`
`  92`  `                bool published;`
`  93`  `                if (r.Table.Columns.Contains("IsPublished") && r["IsPublished"] != DBNull.Value)`
  - → Course publish flag for Landing catalog.
`  94`  `                    published = Convert.ToBoolean(r["IsPublished"]) || Convert.ToInt32(r["IsPublished"]) != 0;`
  - → Course publish flag for Landing catalog.
`  95`  `                else`
`  96`  `                    published = lessons > 0; // legacy fallback`
`  97`  ``
`  98`  `                list.Add(new Dictionary<string, object>`
`  99`  `                {`
` 100`  `                    { "cid", Convert.ToInt32(r["CID"]) },`
` 101`  `                    { "name", DbHelper.SafeString(r["Name"]) },`
  - → Database access (pure SQL).
` 102`  `                    { "description", DbHelper.SafeString(r["Description"]) },`
  - → Database access (pure SQL).
` 103`  `                    { "bgImg", DbHelper.SafeString(r["BgImg"]) },`
  - → Database access (pure SQL).
` 104`  `                    { "rating", r["Rating"] == DBNull.Value ? 0m : Convert.ToDecimal(r["Rating"]) },`
` 105`  `                    { "studentsCount", Convert.ToInt32(r["StudentsCount"]) },`
` 106`  `                    { "lessonsCount", lessons },`
` 107`  `                    { "isPublished", published },`
` 108`  `                    { "status", published ? "Published" : "Draft" },`
` 109`  `                    { "category", DbHelper.SafeString(r["Categories"]) },`
  - → Database access (pure SQL).
` 110`  `                    { "level", DbHelper.SafeString(r["Level"]) }`
  - → Database access (pure SQL).
` 111`  `                });`
` 112`  `            }`
` 113`  `            return list;`
` 114`  `        }`
` 115`  ``
` 116`  `        /// <summary>Set course published/draft. Returns new state.</summary>`
` 117`  `        public static bool SetCoursePublished(int lecturerUid, int cid, bool published)`
` 118`  `        {`
` 119`  `            CourseSchema.Ensure();`
` 120`  `            int owner = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 121`  `                "SELECT LecturerUID FROM Courses WHERE CID = @CID", DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 122`  `            if (owner != lecturerUid)`
` 123`  `                throw new UnauthorizedAccessException("Course not found or access denied.");`
` 124`  ``
` 125`  `            try`
  - → Error handling block.
` 126`  `            {`
` 127`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 128`  `                    @"UPDATE Courses SET IsPublished = @P WHERE CID = @CID AND LecturerUID = @L",`
  - → Course publish flag for Landing catalog.
` 129`  `                    DbHelper.P("@P", published ? 1 : 0),`
  - → Database access (pure SQL).
` 130`  `                    DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 131`  `                    DbHelper.P("@L", lecturerUid));`
  - → Database access (pure SQL).
` 132`  `            }`
` 133`  `            catch (Exception ex)`
  - → Handle/log exception.
` 134`  `            {`
` 135`  `                throw new InvalidOperationException(`
` 136`  `                    "Could not update publish state. Ensure Courses.IsPublished exists.", ex);`
  - → Course publish flag for Landing catalog.
` 137`  `            }`
` 138`  `            return published;`
` 139`  `        }`
` 140`  ``
` 141`  `        public static int CountPendingGrading(int lecturerUid)`
` 142`  `        {`
` 143`  `            try`
  - → Error handling block.
` 144`  `            {`
` 145`  `                return DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
` 146`  `                SELECT COUNT(*) FROM CWSubmissions s`
` 147`  `                INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 148`  `                INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 149`  `                INNER JOIN Courses c ON c.CID = ch.CID`
` 150`  `                WHERE c.LecturerUID = @LecturerUID`
  - → Owner lecturer foreign key.
` 151`  `                AND NOT EXISTS (SELECT 1 FROM CWMarkings m WHERE m.SID = s.SID)",`
` 152`  `                    DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 153`  `            }`
` 154`  `            catch`
  - → Handle/log exception.
` 155`  `            {`
` 156`  `                return 0;`
` 157`  `            }`
` 158`  `        }`
` 159`  ``
` 160`  `        /// <summary>CSV of grades for one course (or all lecturer courses if cid null/0).</summary>`
` 161`  `        public static string BuildGradesCsv(int lecturerUid, int cid)`
  - → CSV export.
` 162`  `        {`
` 163`  `            string sql = @"`
` 164`  `SELECT c.Name AS CourseName, cw.Title AS AssignmentTitle,`
` 165`  `u.Name AS StudentName, u.Email AS StudentEmail,`
` 166`  `s.SubmissionDate, m.Marks AS MarkScore, m.Feedback AS Review`
` 167`  `FROM CWSubmissions s`
` 168`  `INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 169`  `INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 170`  `INNER JOIN Courses c ON c.CID = ch.CID`
` 171`  `INNER JOIN Users u ON u.UID = s.StudentUID`
` 172`  `LEFT JOIN CWMarkings m ON m.SID = s.SID`
` 173`  `WHERE c.LecturerUID = @L";`
  - → Owner lecturer foreign key.
` 174`  `            if (cid > 0) sql += " AND c.CID = @CID";`
` 175`  `            sql += " ORDER BY c.Name, cw.Title, u.Name";`
` 176`  ``
` 177`  `            DataTable dt;`
` 178`  `            try`
  - → Error handling block.
` 179`  `            {`
` 180`  `                if (cid > 0)`
` 181`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid), DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 182`  `                else`
` 183`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid));`
  - → Database access (pure SQL).
` 184`  `            }`
` 185`  `            catch`
  - → Handle/log exception.
` 186`  `            {`
` 187`  `                // legacy Score/Review`
` 188`  `                sql = sql.Replace("m.Marks AS MarkScore", "m.Score AS MarkScore")`
` 189`  `                         .Replace("m.Feedback AS Review", "m.Review AS Review");`
` 190`  `                if (cid > 0)`
` 191`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid), DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 192`  `                else`
` 193`  `                    dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@L", lecturerUid));`
  - → Database access (pure SQL).
` 194`  `            }`
` 195`  ``
` 196`  `            var sb = new System.Text.StringBuilder();`
` 197`  `            sb.AppendLine("Course,Assignment,Student,Email,Submitted,Score,Feedback");`
` 198`  `            foreach (DataRow r in dt.Rows)`
` 199`  `            {`
` 200`  `                string course = Csv(DbHelper.SafeString(r["CourseName"]));`
  - → Database access (pure SQL).
` 201`  `                string asg = Csv(DbHelper.SafeString(r["AssignmentTitle"]));`
  - → Database access (pure SQL).
` 202`  `                string student = Csv(DbHelper.SafeString(r["StudentName"]));`
  - → Database access (pure SQL).
` 203`  `                string email = Csv(DbHelper.SafeString(r["StudentEmail"]));`
  - → Database access (pure SQL).
` 204`  `                string submitted = r["SubmissionDate"] == DBNull.Value`
` 205`  `                    ? ""`
` 206`  `                    : Convert.ToDateTime(r["SubmissionDate"]).ToString("yyyy-MM-dd HH:mm");`
` 207`  `                string score = r["MarkScore"] == DBNull.Value ? "" : Convert.ToDecimal(r["MarkScore"]).ToString("0.##");`
` 208`  `                string fb = Csv(r.Table.Columns.Contains("Review") ? DbHelper.SafeString(r["Review"]) : "");`
  - → Database access (pure SQL).
` 209`  `                sb.AppendLine(string.Join(",", course, asg, student, email, Csv(submitted), score, fb));`
  - → CSV export.
` 210`  `            }`
` 211`  `            return sb.ToString();`
` 212`  `        }`
` 213`  ``
` 214`  `        private static string Csv(string s)`
  - → CSV export.
` 215`  `        {`
` 216`  `            if (s == null) s = "";`
` 217`  `            if (s.IndexOfAny(new[] { ',', '"', '\n', '\r' }) >= 0)`
` 218`  `                return "\"" + s.Replace("\"", "\"\"") + "\"";`
` 219`  `            return s;`
` 220`  `        }`
` 221`  ``
` 222`  `        public static int SaveCourse(int lecturerUid, int? cid, string name, string description, string bgImg, string categories, string level)`
` 223`  `        {`
` 224`  `            CourseSchema.Ensure();`
` 225`  `            if (lecturerUid <= 0)`
` 226`  `            throw new InvalidOperationException(`
` 227`  `            "Not signed in as a valid user. Log out and log in again as a Lecturer.");`
` 228`  ``
` 229`  `            // FK_Courses_Users_LecturerUID requires LecturerUID to exist in Users.UID`
` 230`  `            int userOk = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 231`  `            "SELECT COUNT(1) FROM Users WHERE UID = @UID",`
` 232`  `            DbHelper.P("@UID", lecturerUid));`
  - → Database access (pure SQL).
` 233`  `            if (userOk <= 0)`
` 234`  `            throw new InvalidOperationException(`
` 235`  `            "Your account (UID=" + lecturerUid + ") was not found in Users. " +`
` 236`  `            "This usually means the database was reset while you stayed logged in. " +`
` 237`  `            "Log out, register/log in again as Lecturer, then create the course.");`
` 238`  ``
` 239`  `            if (cid.HasValue && cid.Value > 0)`
` 240`  `            {`
` 241`  `                int owner = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 242`  `                "SELECT LecturerUID FROM Courses WHERE CID = @CID",`
  - → Owner lecturer foreign key.
` 243`  `                DbHelper.P("@CID", cid.Value));`
  - → Database access (pure SQL).
` 244`  `                if (owner != lecturerUid)`
` 245`  `                throw new UnauthorizedAccessException("Course not found or access denied.");`
` 246`  ``
` 247`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 248`  `                @"UPDATE Courses`
` 249`  `                SET Name = @Name, Description = @Description, BgImg = @BgImg,`
` 250`  `                Categories = @Categories, Level = @Level`
` 251`  `                WHERE CID = @CID AND LecturerUID = @LecturerUID",`
  - → Owner lecturer foreign key.
` 252`  `                DbHelper.P("@Name", name),`
  - → Database access (pure SQL).
` 253`  `                DbHelper.P("@Description", description ?? ""),`
  - → Database access (pure SQL).
` 254`  `                DbHelper.P("@BgImg", bgImg ?? ""),`
  - → Database access (pure SQL).
` 255`  `                DbHelper.P("@Categories", categories ?? ""),`
  - → Database access (pure SQL).
` 256`  `                DbHelper.P("@Level", level ?? ""),`
  - → Database access (pure SQL).
` 257`  `                DbHelper.P("@CID", cid.Value),`
  - → Database access (pure SQL).
` 258`  `                DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 259`  `                return cid.Value;`
` 260`  `            }`
` 261`  ``
` 262`  `            // New courses start as Draft (IsPublished = 0) when column exists`
` 263`  `            string insert = @"`
` 264`  `            INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level, IsPublished)`
  - → Course publish flag for Landing catalog.
` 265`  `            VALUES (@LecturerUID, @Name, @Description, 0, @BgImg, @Categories, @Level, 0);`
  - → Owner lecturer foreign key.
` 266`  `            SELECT CAST(SCOPE_IDENTITY() AS INT);";`
` 267`  `            try`
  - → Error handling block.
` 268`  `            {`
` 269`  `                return DbHelper.ExecuteScalarInt(insert,`
  - → Database access (pure SQL).
` 270`  `                DbHelper.P("@LecturerUID", lecturerUid),`
  - → Database access (pure SQL).
` 271`  `                DbHelper.P("@Name", name),`
  - → Database access (pure SQL).
` 272`  `                DbHelper.P("@Description", description ?? ""),`
  - → Database access (pure SQL).
` 273`  `                DbHelper.P("@BgImg", bgImg ?? ""),`
  - → Database access (pure SQL).
` 274`  `                DbHelper.P("@Categories", categories ?? ""),`
  - → Database access (pure SQL).
` 275`  `                DbHelper.P("@Level", level ?? ""));`
  - → Database access (pure SQL).
` 276`  `            }`
` 277`  `            catch`
  - → Handle/log exception.
` 278`  `            {`
` 279`  `                insert = @"`
` 280`  `                INSERT INTO Courses (LecturerUID, Name, Description, Rating, BgImg, Categories, Level)`
  - → Owner lecturer foreign key.
` 281`  `                VALUES (@LecturerUID, @Name, @Description, 0, @BgImg, @Categories, @Level);`
  - → Owner lecturer foreign key.
` 282`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);";`
` 283`  `                try`
  - → Error handling block.
` 284`  `                {`
` 285`  `                    return DbHelper.ExecuteScalarInt(insert,`
  - → Database access (pure SQL).
` 286`  `                    DbHelper.P("@LecturerUID", lecturerUid),`
  - → Database access (pure SQL).
` 287`  `                    DbHelper.P("@Name", name),`
  - → Database access (pure SQL).
` 288`  `                    DbHelper.P("@Description", description ?? ""),`
  - → Database access (pure SQL).
` 289`  `                    DbHelper.P("@BgImg", bgImg ?? ""),`
  - → Database access (pure SQL).
` 290`  `                    DbHelper.P("@Categories", categories ?? ""),`
  - → Database access (pure SQL).
` 291`  `                    DbHelper.P("@Level", level ?? ""));`
  - → Database access (pure SQL).
` 292`  `                }`
` 293`  `                catch (Exception ex)`
  - → Handle/log exception.
` 294`  `                {`
` 295`  `                    if (ex.Message != null && ex.Message.IndexOf("FK_Courses_Users", StringComparison.OrdinalIgnoreCase) >= 0)`
` 296`  `                    {`
` 297`  `                        throw new InvalidOperationException(`
` 298`  `                        "Cannot create course: lecturer UID " + lecturerUid +`
` 299`  `                        " is not a row in Users (FK_Courses_Users_LecturerUID). Log out and sign in again.", ex);`
  - → Owner lecturer foreign key.
` 300`  `                    }`
` 301`  `                    throw;`
` 302`  `                }`
` 303`  `            }`
` 304`  `        }`
` 305`  ``
` 306`  `        public static void DeleteCourse(int lecturerUid, int cid)`
` 307`  `        {`
` 308`  `            int owner = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 309`  `            "SELECT LecturerUID FROM Courses WHERE CID = @CID", DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 310`  `            if (owner != lecturerUid)`
` 311`  `            throw new UnauthorizedAccessException("Course not found or access denied.");`
` 312`  ``
` 313`  `            // Best-effort cascade; ignore missing optional tables`
` 314`  `            TryExec(@"`
` 315`  `            DELETE m FROM CWMarkings m`
` 316`  `            INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 317`  `            INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 318`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 319`  `            WHERE ch.CID = @CID;", cid);`
` 320`  ``
` 321`  `            TryExec(@"`
` 322`  `            DELETE s FROM CWSubmissions s`
` 323`  `            INNER JOIN CourseWorks cw ON cw.CWID = s.CWID`
` 324`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 325`  `            WHERE ch.CID = @CID;", cid);`
` 326`  ``
` 327`  `            TryExec(@"`
` 328`  `            DELETE cwp FROM CourseWorkProgresses cwp`
` 329`  `            INNER JOIN CourseWorks cw ON cw.CWID = cwp.CWID`
` 330`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 331`  `            WHERE ch.CID = @CID;", cid);`
` 332`  ``
` 333`  `            TryExec(@"`
` 334`  `            DELETE cw FROM CourseWorks cw`
` 335`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 336`  `            WHERE ch.CID = @CID;", cid);`
` 337`  ``
` 338`  `            TryExec(@"`
` 339`  `            DELETE sm FROM StudyMats sm`
` 340`  `            INNER JOIN SubChapters sc ON sc.SchID = sm.SchID`
` 341`  `            INNER JOIN Chapters ch ON ch.ChID = sc.ChID`
` 342`  `            WHERE ch.CID = @CID;", cid);`
` 343`  ``
` 344`  `            TryExec(@"DELETE sc FROM SubChapters sc INNER JOIN Chapters ch ON ch.ChID = sc.ChID WHERE ch.CID = @CID;", cid);`
` 345`  `            TryExec(@"DELETE FROM Chapters WHERE CID = @CID;", cid);`
` 346`  `            TryExec(@"DELETE FROM Enrollments WHERE CID = @CID;", cid);`
` 347`  `            TryExec(@"DELETE FROM CourseProgresses WHERE CID = @CID;", cid);`
` 348`  `            TryExec(@"DELETE FROM Ratings WHERE CID = @CID;", cid);`
` 349`  ``
` 350`  `            DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 351`  `            "DELETE FROM Courses WHERE CID = @CID AND LecturerUID = @LecturerUID",`
  - → Owner lecturer foreign key.
` 352`  `            DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 353`  `            DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 354`  `        }`
` 355`  ``
` 356`  `        // ═══════════════════════════════════════════════════════════════════`
` 357`  `        // Chapters / SubChapters / StudyMats (curriculum)`
` 358`  `        // ═══════════════════════════════════════════════════════════════════`
` 359`  ``
` 360`  `        public static List<Dictionary<string, object>> GetCurriculum(int lecturerUid, int cid)`
` 361`  `        {`
` 362`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 363`  ``
` 364`  `            DataTable chapters;`
` 365`  `            try`
  - → Error handling block.
` 366`  `            {`
` 367`  `                chapters = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
` 368`  `                "SELECT ChID, CID, [Index], Title FROM Chapters WHERE CID = @CID ORDER BY [Index], ChID",`
` 369`  `                DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 370`  `            }`
` 371`  `            catch`
  - → Handle/log exception.
` 372`  `            {`
` 373`  `                // Index column may be named differently`
` 374`  `                chapters = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
` 375`  `                "SELECT ChID, CID, Title FROM Chapters WHERE CID = @CID ORDER BY ChID",`
` 376`  `                DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 377`  `            }`
` 378`  ``
` 379`  `            var result = new List<Dictionary<string, object>>();`
` 380`  `            foreach (DataRow ch in chapters.Rows)`
` 381`  `            {`
` 382`  `                int chid = Convert.ToInt32(ch["ChID"]);`
` 383`  `                var lessons = new List<Dictionary<string, object>>();`
` 384`  `                int chIndex = ch.Table.Columns.Contains("Index") && ch["Index"] != DBNull.Value`
` 385`  `                ? Convert.ToInt32(ch["Index"]) : 0;`
` 386`  ``
` 387`  `                DataTable subs;`
` 388`  `                try`
  - → Error handling block.
` 389`  `                {`
` 390`  `                    subs = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
` 391`  `                    "SELECT SchID, ChID, [Index], Title FROM SubChapters WHERE ChID = @ChID ORDER BY [Index], SchID",`
` 392`  `                    DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 393`  `                }`
` 394`  `                catch`
  - → Handle/log exception.
` 395`  `                {`
` 396`  `                    try`
  - → Error handling block.
` 397`  `                    {`
` 398`  `                        subs = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
` 399`  `                        "SELECT SchID, ChID, Title FROM SubChapters WHERE ChID = @ChID ORDER BY SchID",`
` 400`  `                        DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 401`  `                    }`
` 402`  `                    catch`
  - → Handle/log exception.
` 403`  `                    {`
` 404`  `                        subs = new DataTable();`
` 405`  `                    }`
` 406`  `                }`
` 407`  ``
` 408`  `                foreach (DataRow sc in subs.Rows)`
` 409`  `                {`
` 410`  `                    int schid = Convert.ToInt32(sc["SchID"]);`
` 411`  `                    string type = "Text";`
` 412`  `                    string content = "";`
` 413`  `                    var materials = new List<object>();`
` 414`  ``
` 415`  `                    try`
  - → Error handling block.
` 416`  `                    {`
` 417`  `                        var mats = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
` 418`  `                        "SELECT SMID, Type, TextContent, MediaLink, [Index] FROM StudyMats WHERE SchID = @SchID ORDER BY [Index], SMID",`
` 419`  `                        DbHelper.P("@SchID", schid));`
  - → Database access (pure SQL).
` 420`  `                        if (mats.Rows.Count > 0)`
` 421`  `                        {`
` 422`  `                            type = DbHelper.SafeString(mats.Rows[0]["Type"]);`
  - → Database access (pure SQL).
` 423`  `                            if (string.IsNullOrEmpty(type)) type = "Text";`
` 424`  `                            content = !string.IsNullOrEmpty(DbHelper.SafeString(mats.Rows[0]["MediaLink"]))`
  - → Database access (pure SQL).
` 425`  `                            ? DbHelper.SafeString(mats.Rows[0]["MediaLink"])`
  - → Database access (pure SQL).
` 426`  `                            : DbHelper.SafeString(mats.Rows[0]["TextContent"]);`
  - → Database access (pure SQL).
` 427`  `                        }`
` 428`  `                        foreach (DataRow m in mats.Rows)`
` 429`  `                        {`
` 430`  `                            materials.Add(new`
` 431`  `                            {`
` 432`  `                                smid = Convert.ToInt32(m["SMID"]),`
` 433`  `                                type = DbHelper.SafeString(m["Type"]),`
  - → Database access (pure SQL).
` 434`  `                                textContent = DbHelper.SafeString(m["TextContent"]),`
  - → Database access (pure SQL).
` 435`  `                                mediaLink = DbHelper.SafeString(m["MediaLink"]),`
  - → Database access (pure SQL).
` 436`  `                                index = m.Table.Columns.Contains("Index") && m["Index"] != DBNull.Value ? Convert.ToInt32(m["Index"]) : 0`
` 437`  `                            });`
` 438`  `                        }`
` 439`  `                    }`
` 440`  `                    catch { /* StudyMats optional */ }`
  - → Handle/log exception.
` 441`  ``
` 442`  `                    int scIndex = sc.Table.Columns.Contains("Index") && sc["Index"] != DBNull.Value`
` 443`  `                    ? Convert.ToInt32(sc["Index"]) : 0;`
` 444`  ``
` 445`  `                    lessons.Add(new Dictionary<string, object>`
` 446`  `                    {`
` 447`  `                        { "schid", schid },`
` 448`  `                        { "title", DbHelper.SafeString(sc["Title"]) },`
  - → Database access (pure SQL).
` 449`  `                        { "type", type },`
` 450`  `                        { "content", content },`
` 451`  `                        { "index", scIndex },`
` 452`  `                        { "materials", materials }`
` 453`  `                    });`
` 454`  `                }`
` 455`  ``
` 456`  `                result.Add(new Dictionary<string, object>`
` 457`  `                {`
` 458`  `                    { "chid", chid },`
` 459`  `                    { "title", DbHelper.SafeString(ch["Title"]) },`
  - → Database access (pure SQL).
` 460`  `                    { "index", chIndex },`
` 461`  `                    { "lessons", lessons }`
` 462`  `                });`
` 463`  `            }`
` 464`  `            return result;`
` 465`  `        }`
` 466`  ``
` 467`  `        public static int SaveChapter(int lecturerUid, int? chid, int cid, string title)`
` 468`  `        {`
` 469`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 470`  ``
` 471`  `            if (chid.HasValue && chid.Value > 0)`
` 472`  `            {`
` 473`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 474`  `                "UPDATE Chapters SET Title = @Title WHERE ChID = @ChID AND CID = @CID",`
` 475`  `                DbHelper.P("@Title", title),`
  - → Database access (pure SQL).
` 476`  `                DbHelper.P("@ChID", chid.Value),`
  - → Database access (pure SQL).
` 477`  `                DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 478`  `                return chid.Value;`
` 479`  `            }`
` 480`  ``
` 481`  `            try`
  - → Error handling block.
` 482`  `            {`
` 483`  `                int nextIndex = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 484`  `                "SELECT ISNULL(MAX([Index]), 0) + 1 FROM Chapters WHERE CID = @CID",`
` 485`  `                DbHelper.P("@CID", cid));`
  - → Database access (pure SQL).
` 486`  `                return DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 487`  `                @"INSERT INTO Chapters (CID, [Index], Title) VALUES (@CID, @Index, @Title);`
` 488`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 489`  `                DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 490`  `                DbHelper.P("@Index", nextIndex),`
  - → Database access (pure SQL).
` 491`  `                DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 492`  `            }`
` 493`  `            catch`
  - → Handle/log exception.
` 494`  `            {`
` 495`  `                return DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 496`  `                @"INSERT INTO Chapters (CID, Title) VALUES (@CID, @Title);`
` 497`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 498`  `                DbHelper.P("@CID", cid),`
  - → Database access (pure SQL).
` 499`  `                DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 500`  `            }`
` 501`  `        }`
` 502`  ``
` 503`  `        public static void DeleteChapter(int lecturerUid, int chid)`
` 504`  `        {`
` 505`  `            int cid = DbHelper.ExecuteScalarInt("SELECT CID FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 506`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 507`  ``
` 508`  `            TryExec(@"`
` 509`  `            DELETE m FROM CWMarkings m`
` 510`  `            INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 511`  `            INNER JOIN CourseWorks cw ON cw.CWID = s.CWID WHERE cw.ChID = @ChID;", chid, "@ChID");`
` 512`  ``
` 513`  `            TryExec("DELETE s FROM CWSubmissions s INNER JOIN CourseWorks cw ON cw.CWID = s.CWID WHERE cw.ChID = @ChID;", chid, "@ChID");`
` 514`  `            TryExec("DELETE FROM CourseWorks WHERE ChID = @ChID;", chid, "@ChID");`
` 515`  `            TryExec("DELETE sm FROM StudyMats sm INNER JOIN SubChapters sc ON sc.SchID = sm.SchID WHERE sc.ChID = @ChID;", chid, "@ChID");`
` 516`  `            TryExec("DELETE FROM SubChapters WHERE ChID = @ChID;", chid, "@ChID");`
` 517`  `            DbHelper.ExecuteNonQuery("DELETE FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 518`  `        }`
` 519`  ``
` 520`  `        public static int SaveSubChapter(int lecturerUid, int? schid, int chid, string title, string type, string content, string materialsJson)`
` 521`  `        {`
` 522`  `            int cid = DbHelper.ExecuteScalarInt("SELECT CID FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 523`  `            if (cid <= 0)`
` 524`  `            throw new InvalidOperationException("Section/chapter not found (ChID=" + chid + "). Save a section first.");`
` 525`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 526`  ``
` 527`  `            int resolvedSchId;`
` 528`  `            if (schid.HasValue && schid.Value > 0)`
` 529`  `            {`
` 530`  `                int updated = DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 531`  `                "UPDATE SubChapters SET Title = @Title WHERE SchID = @SchID AND ChID = @ChID",`
` 532`  `                DbHelper.P("@Title", title),`
  - → Database access (pure SQL).
` 533`  `                DbHelper.P("@SchID", schid.Value),`
  - → Database access (pure SQL).
` 534`  `                DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 535`  `                if (updated <= 0)`
` 536`  `                throw new InvalidOperationException("Lesson not found or does not belong to this section.");`
` 537`  `                resolvedSchId = schid.Value;`
` 538`  `                TryExec("DELETE FROM StudyMats WHERE SchID = @SchID;", resolvedSchId, "@SchID");`
` 539`  `            }`
` 540`  `            else`
` 541`  `            {`
` 542`  `                resolvedSchId = 0;`
` 543`  `                Exception last = null;`
` 544`  `                // Try common column variants for SubChapters`
` 545`  `                try`
  - → Error handling block.
` 546`  `                {`
` 547`  `                    int nextIndex = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 548`  `                    "SELECT ISNULL(MAX([Index]), 0) + 1 FROM SubChapters WHERE ChID = @ChID",`
` 549`  `                    DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 550`  `                    resolvedSchId = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 551`  `                    @"INSERT INTO SubChapters (ChID, [Index], Title) VALUES (@ChID, @Index, @Title);`
` 552`  `                    SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 553`  `                    DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 554`  `                    DbHelper.P("@Index", nextIndex),`
  - → Database access (pure SQL).
` 555`  `                    DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 556`  `                }`
` 557`  `                catch (Exception ex1)`
  - → Handle/log exception.
` 558`  `                {`
` 559`  `                    last = ex1;`
` 560`  `                    try`
  - → Error handling block.
` 561`  `                    {`
` 562`  `                        resolvedSchId = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 563`  `                        @"INSERT INTO SubChapters (ChID, Title) VALUES (@ChID, @Title);`
` 564`  `                        SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 565`  `                        DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 566`  `                        DbHelper.P("@Title", title));`
  - → Database access (pure SQL).
` 567`  `                    }`
` 568`  `                    catch (Exception ex2)`
  - → Handle/log exception.
` 569`  `                    {`
` 570`  `                        last = ex2;`
` 571`  `                    }`
` 572`  `                }`
` 573`  `                if (resolvedSchId <= 0)`
` 574`  `                throw new InvalidOperationException("Could not create lesson in SubChapters. " + (last != null ? last.Message : ""));`
` 575`  `            }`
` 576`  ``
` 577`  `            // Persist content into StudyMats (best-effort with schema variants)`
` 578`  `            string matType = string.IsNullOrWhiteSpace(type) ? "Text" : type.Trim();`
` 579`  `            // Normalize quiz → text storage`
` 580`  `            if (string.Equals(matType, "Quiz", StringComparison.OrdinalIgnoreCase))`
` 581`  `            matType = "Text";`
` 582`  ``
` 583`  `            string textContent = null;`
` 584`  `            string mediaLink = null;`
` 585`  `            if (string.Equals(matType, "Video", StringComparison.OrdinalIgnoreCase) ||`
` 586`  `            string.Equals(matType, "Image", StringComparison.OrdinalIgnoreCase) ||`
` 587`  `            string.Equals(matType, "PDF", StringComparison.OrdinalIgnoreCase))`
` 588`  `            {`
` 589`  `                mediaLink = content;`
` 590`  `            }`
` 591`  `            else`
` 592`  `            {`
` 593`  `                textContent = content;`
` 594`  `                matType = "Text";`
` 595`  `            }`
` 596`  ``
` 597`  `            InsertStudyMat(resolvedSchId, matType, textContent, mediaLink, 1);`
` 598`  ``
` 599`  `            if (!string.IsNullOrWhiteSpace(materialsJson) && materialsJson.Trim() != "[]")`
` 600`  `            {`
` 601`  `                try`
  - → Error handling block.
` 602`  `                {`
` 603`  `                    var materials = Json.Deserialize<List<Dictionary<string, object>>>(materialsJson);`
` 604`  `                    if (materials != null)`
` 605`  `                    {`
` 606`  `                        int matIndex = 1;`
` 607`  `                        foreach (var m in materials)`
` 608`  `                        {`
` 609`  `                            matIndex++;`
` 610`  `                            string url = m.ContainsKey("url") ? Convert.ToString(m["url"]) : "";`
` 611`  `                            string fileName = m.ContainsKey("fileName") ? Convert.ToString(m["fileName"]) : url;`
` 612`  `                            if (string.IsNullOrWhiteSpace(url)) continue;`
` 613`  `                            string extType = "PDF";`
` 614`  `                            var lower = url.ToLowerInvariant();`
` 615`  `                            if (lower.Contains(".mp4") || lower.Contains(".webm") || lower.Contains(".mov"))`
` 616`  `                            extType = "Video";`
` 617`  `                            else if (lower.Contains(".png") || lower.Contains(".jpg") || lower.Contains(".jpeg") || lower.Contains(".gif") || lower.Contains(".webp"))`
` 618`  `                            extType = "Image";`
` 619`  `                            InsertStudyMat(resolvedSchId, extType, fileName, url, matIndex);`
` 620`  `                        }`
` 621`  `                    }`
` 622`  `                }`
` 623`  `                catch (Exception ex)`
  - → Handle/log exception.
` 624`  `                {`
` 625`  `                    throw new InvalidOperationException("Lesson saved but materials failed: " + ex.Message);`
` 626`  `                }`
` 627`  `            }`
` 628`  ``
` 629`  `            return resolvedSchId;`
` 630`  `        }`
` 631`  ``
` 632`  `        private static void InsertStudyMat(int schid, string type, string textContent, string mediaLink, int index)`
` 633`  `        {`
` 634`  `            // Variant 1: full schema with [Index]`
` 635`  `            try`
  - → Error handling block.
` 636`  `            {`
` 637`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 638`  `                @"INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink, [Index])`
` 639`  `                VALUES (@SchID, @Type, @TextContent, @MediaLink, @Index)",`
` 640`  `                DbHelper.P("@SchID", schid),`
  - → Database access (pure SQL).
` 641`  `                DbHelper.P("@Type", type ?? "Text"),`
  - → Database access (pure SQL).
` 642`  `                DbHelper.P("@TextContent", (object)textContent ?? DBNull.Value),`
  - → Database access (pure SQL).
` 643`  `                DbHelper.P("@MediaLink", (object)mediaLink ?? DBNull.Value),`
  - → Database access (pure SQL).
` 644`  `                DbHelper.P("@Index", index));`
  - → Database access (pure SQL).
` 645`  `                return;`
` 646`  `            }`
` 647`  `            catch { /* try next */ }`
  - → Handle/log exception.
` 648`  ``
` 649`  `            // Variant 2: without Index`
` 650`  `            try`
  - → Error handling block.
` 651`  `            {`
` 652`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 653`  `                @"INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink)`
` 654`  `                VALUES (@SchID, @Type, @TextContent, @MediaLink)",`
` 655`  `                DbHelper.P("@SchID", schid),`
  - → Database access (pure SQL).
` 656`  `                DbHelper.P("@Type", type ?? "Text"),`
  - → Database access (pure SQL).
` 657`  `                DbHelper.P("@TextContent", (object)textContent ?? DBNull.Value),`
  - → Database access (pure SQL).
` 658`  `                DbHelper.P("@MediaLink", (object)mediaLink ?? DBNull.Value));`
  - → Database access (pure SQL).
` 659`  `                return;`
` 660`  `            }`
` 661`  `            catch { /* try next */ }`
  - → Handle/log exception.
` 662`  ``
` 663`  `            // Variant 3: Content / Link column names`
` 664`  `            try`
  - → Error handling block.
` 665`  `            {`
` 666`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 667`  `                @"INSERT INTO StudyMats (SchID, Type, Content, Link)`
` 668`  `                VALUES (@SchID, @Type, @TextContent, @MediaLink)",`
` 669`  `                DbHelper.P("@SchID", schid),`
  - → Database access (pure SQL).
` 670`  `                DbHelper.P("@Type", type ?? "Text"),`
  - → Database access (pure SQL).
` 671`  `                DbHelper.P("@TextContent", (object)textContent ?? DBNull.Value),`
  - → Database access (pure SQL).
` 672`  `                DbHelper.P("@MediaLink", (object)mediaLink ?? DBNull.Value));`
  - → Database access (pure SQL).
` 673`  `                return;`
` 674`  `            }`
` 675`  `            catch (Exception ex)`
  - → Handle/log exception.
` 676`  `            {`
` 677`  `                // Do not fail the whole lesson if StudyMats schema is unknown - `
` 678`  `                // SubChapter row still exists for curriculum listing by title.`
` 679`  `                System.Diagnostics.Debug.WriteLine("StudyMats insert failed: " + ex.Message);`
` 680`  `            }`
` 681`  `        }`
` 682`  ``
` 683`  `        public static void DeleteSubChapter(int lecturerUid, int schid)`
` 684`  `        {`
` 685`  `            int chid = DbHelper.ExecuteScalarInt("SELECT ChID FROM SubChapters WHERE SchID = @SchID", DbHelper.P("@SchID", schid));`
  - → Database access (pure SQL).
` 686`  `            int cid = DbHelper.ExecuteScalarInt("SELECT CID FROM Chapters WHERE ChID = @ChID", DbHelper.P("@ChID", chid));`
  - → Database access (pure SQL).
` 687`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 688`  ``
` 689`  `            TryExec("DELETE FROM StudyMats WHERE SchID = @SchID;", schid, "@SchID");`
` 690`  `            DbHelper.ExecuteNonQuery("DELETE FROM SubChapters WHERE SchID = @SchID", DbHelper.P("@SchID", schid));`
  - → Database access (pure SQL).
` 691`  `        }`
` 692`  ``
` 693`  `        /// <summary>Ensure a Chapter exists for CourseWorks (CourseWorks.ChID).</summary>`
` 694`  `        public static int EnsureAssessmentChapter(int lecturerUid, int cid)`
` 695`  `        {`
` 696`  `            AssertCourseOwner(lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 697`  `            var chDt = DbHelper.ExecuteQuery(`
  - → Database access (pure SQL).
` 698`  `            "SELECT TOP 1 ChID FROM Chapters WHERE CID = @CID AND Title = @Title",`
` 699`  `            DbHelper.P("@CID", cid), DbHelper.P("@Title", "Assessments"));`
  - → Database access (pure SQL).
` 700`  `            if (chDt.Rows.Count > 0)`
` 701`  `            return Convert.ToInt32(chDt.Rows[0]["ChID"]);`
` 702`  `            return SaveChapter(lecturerUid, null, cid, "Assessments");`
` 703`  `        }`
` 704`  ``
` 705`  `        // ═══════════════════════════════════════════════════════════════════`
` 706`  `        // CourseWorks: CWID, ChID, Title, Description, DueDate`
` 707`  `        // ═══════════════════════════════════════════════════════════════════`
` 708`  ``
` 709`  `        public static List<Dictionary<string, object>> GetCourseWorksForLecturer(int lecturerUid)`
` 710`  `        {`
` 711`  `            const string sql = @"`
` 712`  `            SELECT cw.CWID, cw.ChID, cw.Title, cw.Description, cw.DueDate,`
  - → Assignment deadline; submissions close after due day.
` 713`  `            c.CID, c.Name AS CourseName,`
` 714`  `            (SELECT COUNT(*) FROM CWSubmissions s WHERE s.CWID = cw.CWID) AS SubmissionCount,`
` 715`  `            (SELECT COUNT(*) FROM CWMarkings m`
` 716`  `            INNER JOIN CWSubmissions s ON s.SID = m.SID`
` 717`  `            WHERE s.CWID = cw.CWID) AS GradedCount`
` 718`  `            FROM CourseWorks cw`
` 719`  `            INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 720`  `            INNER JOIN Courses c ON c.CID = ch.CID`
` 721`  `            WHERE c.LecturerUID = @LecturerUID`
  - → Owner lecturer foreign key.
` 722`  `            ORDER BY cw.CWID DESC";`
` 723`  ``
` 724`  `            DataTable dt;`
` 725`  `            try`
  - → Error handling block.
` 726`  `            {`
` 727`  `                dt = DbHelper.ExecuteQuery(sql, DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 728`  `            }`
` 729`  `            catch`
  - → Handle/log exception.
` 730`  `            {`
` 731`  `                // Without graded count / markings`
` 732`  `                const string sql2 = @"`
` 733`  `                SELECT cw.CWID, cw.ChID, cw.Title, cw.Description, cw.DueDate,`
  - → Assignment deadline; submissions close after due day.
` 734`  `                c.CID, c.Name AS CourseName,`
` 735`  `                (SELECT COUNT(*) FROM CWSubmissions s WHERE s.CWID = cw.CWID) AS SubmissionCount,`
` 736`  `                0 AS GradedCount`
` 737`  `                FROM CourseWorks cw`
` 738`  `                INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 739`  `                INNER JOIN Courses c ON c.CID = ch.CID`
` 740`  `                WHERE c.LecturerUID = @LecturerUID`
  - → Owner lecturer foreign key.
` 741`  `                ORDER BY cw.CWID DESC";`
` 742`  `                dt = DbHelper.ExecuteQuery(sql2, DbHelper.P("@LecturerUID", lecturerUid));`
  - → Database access (pure SQL).
` 743`  `            }`
` 744`  ``
` 745`  `            var list = new List<Dictionary<string, object>>();`
` 746`  `            foreach (DataRow r in dt.Rows)`
` 747`  `            {`
` 748`  `                string title = DbHelper.SafeString(r["Title"]);`
  - → Database access (pure SQL).
` 749`  `                string desc = DbHelper.SafeString(r["Description"]);`
  - → Database access (pure SQL).
` 750`  `                var packed = ParseDescriptionMeta(desc);`
` 751`  `                list.Add(new Dictionary<string, object>`
` 752`  `                {`
` 753`  `                    { "cwid", Convert.ToInt32(r["CWID"]) },`
` 754`  `                    { "chid", Convert.ToInt32(r["ChID"]) },`
` 755`  `                    { "cid", Convert.ToInt32(r["CID"]) },`
` 756`  `                    { "courseName", DbHelper.SafeString(r["CourseName"]) },`
  - → Database access (pure SQL).
` 757`  `                    { "title", title },`
` 758`  `                    { "instructions", packed.Instructions },`
` 759`  `                    { "type", packed.Type },`
` 760`  `                    { "score", packed.Score },`
` 761`  `                    { "creditGiven", packed.Score },`
` 762`  `                    { "dueDate", r["DueDate"] == DBNull.Value ? null : Convert.ToDateTime(r["DueDate"]).ToString("yyyy-MM-dd") },`
  - → Assignment deadline; submissions close after due day.
` 763`  `                    { "submissionCount", Convert.ToInt32(r["SubmissionCount"]) },`
` 764`  `                    { "gradedCount", Convert.ToInt32(r["GradedCount"]) },`
` 765`  `                    { "rubric", packed.Rubric },`
` 766`  `                    { "meta", packed.Extra }`
` 767`  `                });`
` 768`  `            }`
` 769`  `            return list;`
` 770`  `        }`
` 771`  ``
` 772`  `        public static int SaveCourseWork(`
` 773`  `        int lecturerUid,`
` 774`  `        int? cwid,`
` 775`  `        int cid,`
` 776`  `        string title,`
` 777`  `        string instructions,`
` 778`  `        string type,`
` 779`  `        decimal score,`
` 780`  `        decimal creditGiven,`
` 781`  `        string rubricJson,`
` 782`  `        string extraMetaJson,`
` 783`  `        string objectiveQuestionsJson)`
` 784`  `        {`
` 785`  `            int chid = EnsureAssessmentChapter(lecturerUid, cid);`
` 786`  `            string desc = PackDescription(instructions, type, score, rubricJson, extraMetaJson, objectiveQuestionsJson);`
` 787`  ``
` 788`  `            DateTime? dueDate = null;`
  - → Assignment deadline; submissions close after due day.
` 789`  `            if (!string.IsNullOrWhiteSpace(extraMetaJson))`
` 790`  `            {`
` 791`  `                try`
  - → Error handling block.
` 792`  `                {`
` 793`  `                    var extra = Json.Deserialize<Dictionary<string, object>>(extraMetaJson);`
` 794`  `                    if (extra != null && extra.ContainsKey("dueDate") && extra["dueDate"] != null)`
  - → Assignment deadline; submissions close after due day.
` 795`  `                    {`
` 796`  `                        var ds = Convert.ToString(extra["dueDate"]);`
  - → Assignment deadline; submissions close after due day.
` 797`  `                        if (!string.IsNullOrWhiteSpace(ds) && DateTime.TryParse(ds, out var d))`
` 798`  `                        dueDate = d;`
  - → Assignment deadline; submissions close after due day.
` 799`  `                    }`
` 800`  `                }`
` 801`  `                catch { }`
  - → Handle/log exception.
` 802`  `            }`
` 803`  ``
` 804`  `            int resolvedCwid;`
` 805`  `            if (cwid.HasValue && cwid.Value > 0)`
` 806`  `            {`
` 807`  `                int owner = DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).
` 808`  `                SELECT c.LecturerUID FROM CourseWorks cw`
  - → Owner lecturer foreign key.
` 809`  `                INNER JOIN Chapters ch ON ch.ChID = cw.ChID`
` 810`  `                INNER JOIN Courses c ON c.CID = ch.CID`
` 811`  `                WHERE cw.CWID = @CWID", DbHelper.P("@CWID", cwid.Value));`
  - → Database access (pure SQL).
` 812`  `                if (owner != lecturerUid) throw new UnauthorizedAccessException("Access denied.");`
` 813`  ``
` 814`  `                DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 815`  `                @"UPDATE CourseWorks SET Title = @Title, Description = @Description, DueDate = @DueDate, ChID = @ChID`
  - → Assignment deadline; submissions close after due day.
` 816`  `                WHERE CWID = @CWID",`
` 817`  `                DbHelper.P("@Title", title ?? ""),`
  - → Database access (pure SQL).
` 818`  `                DbHelper.P("@Description", desc),`
  - → Database access (pure SQL).
` 819`  `                DbHelper.P("@DueDate", (object)dueDate ?? DBNull.Value),`
  - → Database access (pure SQL).
` 820`  `                DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 821`  `                DbHelper.P("@CWID", cwid.Value));`
  - → Database access (pure SQL).
` 822`  `                resolvedCwid = cwid.Value;`
` 823`  `            }`
` 824`  `            else`
` 825`  `            {`
` 826`  `                resolvedCwid = DbHelper.ExecuteScalarInt(`
  - → Database access (pure SQL).
` 827`  `                @"INSERT INTO CourseWorks (ChID, Title, Description, DueDate)`
  - → Assignment deadline; submissions close after due day.
` 828`  `                VALUES (@ChID, @Title, @Description, @DueDate);`
  - → Assignment deadline; submissions close after due day.
` 829`  `                SELECT CAST(SCOPE_IDENTITY() AS INT);",`
` 830`  `                DbHelper.P("@ChID", chid),`
  - → Database access (pure SQL).
` 831`  `                DbHelper.P("@Title", title ?? ""),`
  - → Database access (pure SQL).
` 832`  `                DbHelper.P("@Description", desc),`
  - → Database access (pure SQL).
` 833`  `                DbHelper.P("@DueDate", (object)dueDate ?? DBNull.Value));`
  - → Database access (pure SQL).
` 834`  `            }`
` 835`  ``
` 836`  `            // ObjectiveQuestions: QID, QuestionText, OptionA, OptionB, OptionC, OptionD, CorrectAnswer`
` 837`  `            // No CWID on this table in the live schema - store quiz defs also in Description JSON above.`
` 838`  `            // Optionally insert rows for grading auto-check later.`
` 839`  `            if (string.Equals(type, "Objective", StringComparison.OrdinalIgnoreCase) &&`
` 840`  `            !string.IsNullOrWhiteSpace(objectiveQuestionsJson))`
` 841`  `            {`
` 842`  `                try`
  - → Error handling block.
` 843`  `                {`
` 844`  `                    var questions = Json.Deserialize<List<Dictionary<string, object>>>(objectiveQuestionsJson);`
` 845`  `                    if (questions != null)`
` 846`  `                    {`
` 847`  `                        foreach (var q in questions)`
` 848`  `                        {`
` 849`  `                            string qText = q.ContainsKey("question") ? Convert.ToString(q["question"]) : "";`
` 850`  `                            string a = "", b = "", c = "", d = "";`
` 851`  `                            if (q.ContainsKey("options"))`
` 852`  `                            {`
` 853`  `                                try`
  - → Error handling block.
` 854`  `                                {`
` 855`  `                                    var opts = q["options"] as Dictionary<string, object>;`
` 856`  `                                    if (opts == null)`
` 857`  `                                    opts = Json.Deserialize<Dictionary<string, object>>(Json.Serialize(q["options"]));`
` 858`  `                                    if (opts != null)`
` 859`  `                                    {`
` 860`  `                                        var keys = opts.Keys.ToList();`
` 861`  `                                        if (keys.Count > 0) a = Convert.ToString(opts[keys[0]]);`
` 862`  `                                        if (keys.Count > 1) b = Convert.ToString(opts[keys[1]]);`
` 863`  `                                        if (keys.Count > 2) c = Convert.ToString(opts[keys[2]]);`
` 864`  `                                        if (keys.Count > 3) d = Convert.ToString(opts[keys[3]]);`
` 865`  `                                    }`
` 866`  `                                }`
` 867`  `                                catch { }`
  - → Handle/log exception.
` 868`  `                            }`
` 869`  `                            string correct = q.ContainsKey("answer") ? Convert.ToString(q["answer"]) : "A";`
` 870`  `                            // Map option1 -> A etc.`
` 871`  `                            if (correct != null && correct.StartsWith("option", StringComparison.OrdinalIgnoreCase))`
` 872`  `                            {`
` 873`  `                                var n = correct.Replace("option", "").Replace("Option", "");`
` 874`  `                                if (n == "1") correct = "A";`
` 875`  `                                else if (n == "2") correct = "B";`
` 876`  `                                else if (n == "3") correct = "C";`
` 877`  `                                else if (n == "4") correct = "D";`
` 878`  `                            }`
` 879`  ``
` 880`  `                            DbHelper.ExecuteNonQuery(`
  - → Database access (pure SQL).
` 881`  `                            @"INSERT INTO ObjectiveQuestions (QuestionText, OptionA, OptionB, OptionC, OptionD, CorrectAnswer)`
` 882`  `                            VALUES (@Q, @A, @B, @C, @D, @Correct)",`
` 883`  `                            DbHelper.P("@Q", qText),`
  - → Database access (pure SQL).
` 884`  `                            DbHelper.P("@A", a ?? ""),`
  - → Database access (pure SQL).
` 885`  `                            DbHelper.P("@B", b ?? ""),`
  - → Database access (pure SQL).
` 886`  `                            DbHelper.P("@C", c ?? ""),`
  - → Database access (pure SQL).
` 887`  `                            DbHelper.P("@D", d ?? ""),`
  - → Database access (pure SQL).
` 888`  `                            DbHelper.P("@Correct", correct ?? "A"));`
  - → Database access (pure SQL).
` 889`  `                        }`
` 890`  `                    }`
` 891`  `                }`
` 892`  `                catch { /* optional */ }`
  - → Handle/log exception.
` 893`  `            }`
` 894`  ``
` 895`  `            return resolvedCwid;`
` 896`  `        }`
` 897`  ``
` 898`  `        public static void DeleteCourseWork(int lecturerUid, int cwid)`
` 899`  `        {`
` 900`  `            int owner = DbHelper.ExecuteScalarInt(@"`
  - → Database access (pure SQL).

_… truncated: 797 more lines in source. Open the original file for the rest._

## Source snapshot (raw)

_File has 1697 lines — raw dump omitted here to keep Markdown readable. Open `Data/LecturerRepository.cs` in the project._
