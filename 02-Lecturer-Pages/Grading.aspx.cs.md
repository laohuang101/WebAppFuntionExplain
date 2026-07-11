# Grading.aspx.cs
**Source:** `Pages/Lecturer/Grading.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

List submissions for lecturer courses; assign marks and feedback; CSV export.

## File overview

- **Total lines:** 114
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 29:** `uid` — type `int`
- **Line 31:** `list` — type `var`
- **Line 32:** `graded` — type `int`
- **Line 57:** `uid` — type `int`
- **Line 62:** `ctx` — type `var`
- **Line 84:** `uid` — type `int`
- **Line 86:** `csv` — type `string`
- **Line 87:** `name` — type `string`
- **Line 104:** `uid` — type `int`

## Functions / methods (6 found)

### `Page_Load` — lines 12–16

```
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`

#### Line-by-line (this function)

`  12`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  13`  `        {`
`  14`  `            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  15`  `                return;`
`  16`  `}`

---

### `CurrentUid` — lines 17–21

```
private static int CurrentUid()
```

#### Explanation

- **Purpose:** Implements `CurrentUid`.
- **Security:** Uses AuthGate — requires logged-in role.

#### Line-by-line (this function)

`  17`  ``
`  18`  `        private static int CurrentUid()`
`  19`  `        {`
`  20`  `            return AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
`  21`  `        }`

---

### `GetSubmissions` — lines 25–49

```
public static object GetSubmissions()
```

#### Explanation

- **Purpose:** Implements `GetSubmissions`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`, `list`, `graded`

#### Line-by-line (this function)

`  25`  `        public static object GetSubmissions()`
`  26`  `        {`
`  27`  `            try`
  - → Error handling block.
`  28`  `            {`
`  29`  `                int uid = CurrentUid();`
`  30`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  31`  `                var list = LecturerRepository.GetRecentSubmissions(uid, 200);`
`  32`  `                int graded = 0;`
`  33`  `                foreach (var s in list)`
`  34`  `                {`
`  35`  `                    if (s.ContainsKey("isGraded") && Convert.ToBoolean(s["isGraded"])) graded++;`
`  36`  `                }`
`  37`  `                return new`
`  38`  `                {`
`  39`  `                    success = true,`
`  40`  `                    submissions = list,`
`  41`  `                    gradedCount = graded,`
`  42`  `                    totalCount = list.Count`
`  43`  `                };`
`  44`  `            }`
`  45`  `            catch (Exception ex)`
  - → Handle/log exception.
`  46`  `            {`
`  47`  `                return new { success = false, message = "Request failed." };`
`  48`  `            }`
`  49`  `        }`

---

### `SaveGrade` — lines 53–76

```
public static object SaveGrade(int sid, decimal score, string review)
```

#### Explanation

- **Purpose:** Implements `SaveGrade`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Session:** Reads/writes ASP.NET Session.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int sid, decimal score, string review`
- **Local variables:** `uid`, `ctx`

#### Line-by-line (this function)

`  53`  `        public static object SaveGrade(int sid, decimal score, string review)`
`  54`  `        {`
`  55`  `            try`
  - → Error handling block.
`  56`  `            {`
`  57`  `                int uid = CurrentUid();`
`  58`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  59`  `                LecturerRepository.SaveGrade(uid, sid, score, review ?? "");`
`  60`  `                try`
  - → Error handling block.
`  61`  `                {`
`  62`  `                    var ctx = System.Web.HttpContext.Current;`
`  63`  `                    if (ctx != null && ctx.Session != null)`
`  64`  `                    {`
`  65`  `                        ctx.Session.Remove("PendingGradeCount");`
`  66`  `                        ctx.Session.Remove("PendingGradeCountAt");`
`  67`  `                    }`
`  68`  `                }`
`  69`  `                catch { }`
  - → Handle/log exception.
`  70`  `                return new { success = true };`
`  71`  `            }`
`  72`  `            catch (Exception ex)`
  - → Handle/log exception.
`  73`  `            {`
`  74`  `                return new { success = false, message = "Request failed." };`
`  75`  `            }`
`  76`  `        }`

---

### `ExportGradesCsv` — lines 80–96

```
public static object ExportGradesCsv(int cid)
```

#### Explanation

- **Purpose:** Implements `ExportGradesCsv`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `int cid`
- **Local variables:** `uid`, `csv`, `name`

#### Line-by-line (this function)

`  80`  `        public static object ExportGradesCsv(int cid)`
  - → CSV export.
`  81`  `        {`
`  82`  `            try`
  - → Error handling block.
`  83`  `            {`
`  84`  `                int uid = CurrentUid();`
`  85`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  86`  `                string csv = LecturerRepository.BuildGradesCsv(uid, cid);`
  - → CSV export.
`  87`  `                string name = cid > 0`
`  88`  `                    ? "grades-course-" + cid + ".csv"`
  - → CSV export.
`  89`  `                    : "grades-all.csv";`
  - → CSV export.
`  90`  `                return new { success = true, csv = csv, fileName = name };`
  - → CSV export.
`  91`  `            }`
`  92`  `            catch`
  - → Handle/log exception.
`  93`  `            {`
`  94`  `                return new { success = false, message = "Could not export grades." };`
`  95`  `            }`
`  96`  `        }`

---

### `GetPendingCount` — lines 100–112

```
public static object GetPendingCount()
```

#### Explanation

- **Purpose:** Implements `GetPendingCount`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`

#### Line-by-line (this function)

` 100`  `        public static object GetPendingCount()`
` 101`  `        {`
` 102`  `            try`
  - → Error handling block.
` 103`  `            {`
` 104`  `                int uid = CurrentUid();`
` 105`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
` 106`  `                return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };`
` 107`  `            }`
` 108`  `            catch`
  - → Handle/log exception.
` 109`  `            {`
` 110`  `                return new { success = false, pending = 0 };`
` 111`  `            }`
` 112`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Web.Script.Services;`
  - → Import namespace/types.
`   3`  `using System.Web.Services;`
  - → Import namespace/types.
`   4`  `using System.Web.UI;`
  - → Import namespace/types.
`   5`  `using WebAppAssignment.Data;`
  - → Import namespace/types.
`   6`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`   7`  ``
`   8`  `namespace WebAppAssignment.Pages.Lecturer`
  - → C# namespace grouping.
`   9`  `{`
`  10`  `    public partial class Grading : Page`
`  11`  `    {`
`  12`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  13`  `        {`
`  14`  `            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  15`  `                return;`
`  16`  `}`
`  17`  ``
`  18`  `        private static int CurrentUid()`
`  19`  `        {`
`  20`  `            return AuthGate.RequireLecturer();`
  - → Authorization — block wrong role / anonymous.
`  21`  `        }`
`  22`  ``
`  23`  `        [WebMethod(EnableSession = true)]`
  - → Expose method to AJAX JSON calls.
`  24`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  25`  `        public static object GetSubmissions()`
`  26`  `        {`
`  27`  `            try`
  - → Error handling block.
`  28`  `            {`
`  29`  `                int uid = CurrentUid();`
`  30`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  31`  `                var list = LecturerRepository.GetRecentSubmissions(uid, 200);`
`  32`  `                int graded = 0;`
`  33`  `                foreach (var s in list)`
`  34`  `                {`
`  35`  `                    if (s.ContainsKey("isGraded") && Convert.ToBoolean(s["isGraded"])) graded++;`
`  36`  `                }`
`  37`  `                return new`
`  38`  `                {`
`  39`  `                    success = true,`
`  40`  `                    submissions = list,`
`  41`  `                    gradedCount = graded,`
`  42`  `                    totalCount = list.Count`
`  43`  `                };`
`  44`  `            }`
`  45`  `            catch (Exception ex)`
  - → Handle/log exception.
`  46`  `            {`
`  47`  `                return new { success = false, message = "Request failed." };`
`  48`  `            }`
`  49`  `        }`
`  50`  ``
`  51`  `        [WebMethod(EnableSession = true)]`
  - → Expose method to AJAX JSON calls.
`  52`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  53`  `        public static object SaveGrade(int sid, decimal score, string review)`
`  54`  `        {`
`  55`  `            try`
  - → Error handling block.
`  56`  `            {`
`  57`  `                int uid = CurrentUid();`
`  58`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  59`  `                LecturerRepository.SaveGrade(uid, sid, score, review ?? "");`
`  60`  `                try`
  - → Error handling block.
`  61`  `                {`
`  62`  `                    var ctx = System.Web.HttpContext.Current;`
`  63`  `                    if (ctx != null && ctx.Session != null)`
`  64`  `                    {`
`  65`  `                        ctx.Session.Remove("PendingGradeCount");`
`  66`  `                        ctx.Session.Remove("PendingGradeCountAt");`
`  67`  `                    }`
`  68`  `                }`
`  69`  `                catch { }`
  - → Handle/log exception.
`  70`  `                return new { success = true };`
`  71`  `            }`
`  72`  `            catch (Exception ex)`
  - → Handle/log exception.
`  73`  `            {`
`  74`  `                return new { success = false, message = "Request failed." };`
`  75`  `            }`
`  76`  `        }`
`  77`  ``
`  78`  `        [WebMethod(EnableSession = true)]`
  - → Expose method to AJAX JSON calls.
`  79`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  80`  `        public static object ExportGradesCsv(int cid)`
  - → CSV export.
`  81`  `        {`
`  82`  `            try`
  - → Error handling block.
`  83`  `            {`
`  84`  `                int uid = CurrentUid();`
`  85`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  86`  `                string csv = LecturerRepository.BuildGradesCsv(uid, cid);`
  - → CSV export.
`  87`  `                string name = cid > 0`
`  88`  `                    ? "grades-course-" + cid + ".csv"`
  - → CSV export.
`  89`  `                    : "grades-all.csv";`
  - → CSV export.
`  90`  `                return new { success = true, csv = csv, fileName = name };`
  - → CSV export.
`  91`  `            }`
`  92`  `            catch`
  - → Handle/log exception.
`  93`  `            {`
`  94`  `                return new { success = false, message = "Could not export grades." };`
`  95`  `            }`
`  96`  `        }`
`  97`  ``
`  98`  `        [WebMethod(EnableSession = true)]`
  - → Expose method to AJAX JSON calls.
`  99`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
` 100`  `        public static object GetPendingCount()`
` 101`  `        {`
` 102`  `            try`
  - → Error handling block.
` 103`  `            {`
` 104`  `                int uid = CurrentUid();`
` 105`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
` 106`  `                return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };`
` 107`  `            }`
` 108`  `            catch`
  - → Handle/log exception.
` 109`  `            {`
` 110`  `                return new { success = false, pending = 0 };`
` 111`  `            }`
` 112`  `        }`
` 113`  `    }`
` 114`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.Web.Script.Services;
using System.Web.Services;
using System.Web.UI;
using WebAppAssignment.Data;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Lecturer
{
    public partial class Grading : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
                return;
}

        private static int CurrentUid()
        {
            return AuthGate.RequireLecturer();
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetSubmissions()
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                var list = LecturerRepository.GetRecentSubmissions(uid, 200);
                int graded = 0;
                foreach (var s in list)
                {
                    if (s.ContainsKey("isGraded") && Convert.ToBoolean(s["isGraded"])) graded++;
                }
                return new
                {
                    success = true,
                    submissions = list,
                    gradedCount = graded,
                    totalCount = list.Count
                };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object SaveGrade(int sid, decimal score, string review)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                LecturerRepository.SaveGrade(uid, sid, score, review ?? "");
                try
                {
                    var ctx = System.Web.HttpContext.Current;
                    if (ctx != null && ctx.Session != null)
                    {
                        ctx.Session.Remove("PendingGradeCount");
                        ctx.Session.Remove("PendingGradeCountAt");
                    }
                }
                catch { }
                return new { success = true };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object ExportGradesCsv(int cid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                string csv = LecturerRepository.BuildGradesCsv(uid, cid);
                string name = cid > 0
                    ? "grades-course-" + cid + ".csv"
                    : "grades-all.csv";
                return new { success = true, csv = csv, fileName = name };
            }
            catch
            {
                return new { success = false, message = "Could not export grades." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetPendingCount()
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };
            }
            catch
            {
                return new { success = false, pending = 0 };
            }
        }
    }
}

```
