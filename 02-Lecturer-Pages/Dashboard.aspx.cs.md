# Dashboard.aspx.cs
**Source:** `Pages/Lecturer/Dashboard.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 104
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 29:** `uid` — type `int`
- **Line 45:** `uid` — type `int`
- **Line 50:** `ctx` — type `var`
- **Line 72:** `uid` — type `int`
- **Line 88:** `uid` — type `int`
- **Line 90:** `csv` — type `string`

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
`  16`  `        }`

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

### `GetDashboardData` — lines 25–37

```
public static object GetDashboardData()
```

#### Explanation

- **Purpose:** Implements `GetDashboardData`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`

#### Line-by-line (this function)

`  25`  `        public static object GetDashboardData()`
`  26`  `        {`
`  27`  `            try`
  - → Error handling block.
`  28`  `            {`
`  29`  `                int uid = CurrentUid();`
`  30`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  31`  `                return LecturerRepository.GetDashboardData(uid);`
`  32`  `            }`
`  33`  `            catch`
  - → Handle/log exception.
`  34`  `            {`
`  35`  `                return new { success = false, message = "Could not load dashboard." };`
`  36`  `            }`
`  37`  `        }`

---

### `SaveGrade` — lines 41–64

```
public static object SaveGrade(int sid, int score, string review)
```

#### Explanation

- **Purpose:** Implements `SaveGrade`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Session:** Reads/writes ASP.NET Session.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int sid, int score, string review`
- **Local variables:** `uid`, `ctx`

#### Line-by-line (this function)

`  41`  `        public static object SaveGrade(int sid, int score, string review)`
`  42`  `        {`
`  43`  `            try`
  - → Error handling block.
`  44`  `            {`
`  45`  `                int uid = CurrentUid();`
`  46`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  47`  `                LecturerRepository.SaveGrade(uid, sid, score, review ?? "");`
`  48`  `                try`
  - → Error handling block.
`  49`  `                {`
`  50`  `                    var ctx = System.Web.HttpContext.Current;`
`  51`  `                    if (ctx != null && ctx.Session != null)`
`  52`  `                    {`
`  53`  `                        ctx.Session.Remove("PendingGradeCount");`
`  54`  `                        ctx.Session.Remove("PendingGradeCountAt");`
`  55`  `                    }`
`  56`  `                }`
`  57`  `                catch { }`
  - → Handle/log exception.
`  58`  `                return new { success = true };`
`  59`  `            }`
`  60`  `            catch`
  - → Handle/log exception.
`  61`  `            {`
`  62`  `                return new { success = false, message = "Could not save grade." };`
`  63`  `            }`
`  64`  `        }`

---

### `GetPendingCount` — lines 68–80

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

`  68`  `        public static object GetPendingCount()`
`  69`  `        {`
`  70`  `            try`
  - → Error handling block.
`  71`  `            {`
`  72`  `                int uid = CurrentUid();`
`  73`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  74`  `                return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };`
`  75`  `            }`
`  76`  `            catch`
  - → Handle/log exception.
`  77`  `            {`
`  78`  `                return new { success = false, pending = 0 };`
`  79`  `            }`
`  80`  `        }`

---

### `ExportGradesCsv` — lines 84–102

```
public static object ExportGradesCsv(int cid)
```

#### Explanation

- **Purpose:** Implements `ExportGradesCsv`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `int cid`
- **Local variables:** `uid`, `csv`

#### Line-by-line (this function)

`  84`  `        public static object ExportGradesCsv(int cid)`
  - → CSV export.
`  85`  `        {`
`  86`  `            try`
  - → Error handling block.
`  87`  `            {`
`  88`  `                int uid = CurrentUid();`
`  89`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  90`  `                string csv = LecturerRepository.BuildGradesCsv(uid, cid);`
  - → CSV export.
`  91`  `                return new`
`  92`  `                {`
`  93`  `                    success = true,`
`  94`  `                    csv = csv,`
  - → CSV export.
`  95`  `                    fileName = cid > 0 ? "grades-course-" + cid + ".csv" : "grades-all.csv"`
  - → CSV export.
`  96`  `                };`
`  97`  `            }`
`  98`  `            catch`
  - → Handle/log exception.
`  99`  `            {`
` 100`  `                return new { success = false, message = "Could not export grades." };`
` 101`  `            }`
` 102`  `        }`

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
`  10`  `    public partial class Dashboard : Page`
`  11`  `    {`
`  12`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  13`  `        {`
`  14`  `            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  15`  `                return;`
`  16`  `        }`
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
`  25`  `        public static object GetDashboardData()`
`  26`  `        {`
`  27`  `            try`
  - → Error handling block.
`  28`  `            {`
`  29`  `                int uid = CurrentUid();`
`  30`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  31`  `                return LecturerRepository.GetDashboardData(uid);`
`  32`  `            }`
`  33`  `            catch`
  - → Handle/log exception.
`  34`  `            {`
`  35`  `                return new { success = false, message = "Could not load dashboard." };`
`  36`  `            }`
`  37`  `        }`
`  38`  ``
`  39`  `        [WebMethod(EnableSession = true)]`
  - → Expose method to AJAX JSON calls.
`  40`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  41`  `        public static object SaveGrade(int sid, int score, string review)`
`  42`  `        {`
`  43`  `            try`
  - → Error handling block.
`  44`  `            {`
`  45`  `                int uid = CurrentUid();`
`  46`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  47`  `                LecturerRepository.SaveGrade(uid, sid, score, review ?? "");`
`  48`  `                try`
  - → Error handling block.
`  49`  `                {`
`  50`  `                    var ctx = System.Web.HttpContext.Current;`
`  51`  `                    if (ctx != null && ctx.Session != null)`
`  52`  `                    {`
`  53`  `                        ctx.Session.Remove("PendingGradeCount");`
`  54`  `                        ctx.Session.Remove("PendingGradeCountAt");`
`  55`  `                    }`
`  56`  `                }`
`  57`  `                catch { }`
  - → Handle/log exception.
`  58`  `                return new { success = true };`
`  59`  `            }`
`  60`  `            catch`
  - → Handle/log exception.
`  61`  `            {`
`  62`  `                return new { success = false, message = "Could not save grade." };`
`  63`  `            }`
`  64`  `        }`
`  65`  ``
`  66`  `        [WebMethod(EnableSession = true)]`
  - → Expose method to AJAX JSON calls.
`  67`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  68`  `        public static object GetPendingCount()`
`  69`  `        {`
`  70`  `            try`
  - → Error handling block.
`  71`  `            {`
`  72`  `                int uid = CurrentUid();`
`  73`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  74`  `                return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };`
`  75`  `            }`
`  76`  `            catch`
  - → Handle/log exception.
`  77`  `            {`
`  78`  `                return new { success = false, pending = 0 };`
`  79`  `            }`
`  80`  `        }`
`  81`  ``
`  82`  `        [WebMethod(EnableSession = true)]`
  - → Expose method to AJAX JSON calls.
`  83`  `        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]`
`  84`  `        public static object ExportGradesCsv(int cid)`
  - → CSV export.
`  85`  `        {`
`  86`  `            try`
  - → Error handling block.
`  87`  `            {`
`  88`  `                int uid = CurrentUid();`
`  89`  `                if (uid == 0) return AuthGate.NotAuthenticatedJson();`
  - → Authorization — block wrong role / anonymous.
`  90`  `                string csv = LecturerRepository.BuildGradesCsv(uid, cid);`
  - → CSV export.
`  91`  `                return new`
`  92`  `                {`
`  93`  `                    success = true,`
`  94`  `                    csv = csv,`
  - → CSV export.
`  95`  `                    fileName = cid > 0 ? "grades-course-" + cid + ".csv" : "grades-all.csv"`
  - → CSV export.
`  96`  `                };`
`  97`  `            }`
`  98`  `            catch`
  - → Handle/log exception.
`  99`  `            {`
` 100`  `                return new { success = false, message = "Could not export grades." };`
` 101`  `            }`
` 102`  `        }`
` 103`  `    }`
` 104`  `}`

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
    public partial class Dashboard : Page
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
        public static object GetDashboardData()
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                return LecturerRepository.GetDashboardData(uid);
            }
            catch
            {
                return new { success = false, message = "Could not load dashboard." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object SaveGrade(int sid, int score, string review)
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
            catch
            {
                return new { success = false, message = "Could not save grade." };
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

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object ExportGradesCsv(int cid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                string csv = LecturerRepository.BuildGradesCsv(uid, cid);
                return new
                {
                    success = true,
                    csv = csv,
                    fileName = cid > 0 ? "grades-course-" + cid + ".csv" : "grades-all.csv"
                };
            }
            catch
            {
                return new { success = false, message = "Could not export grades." };
            }
        }
    }
}

```
