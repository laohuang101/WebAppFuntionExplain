# Dashboard.aspx.cs
**Source:** `Pages/Lecturer/Dashboard.aspx.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 104
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 29:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 45:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 50:** `ctx` (`var`) — **Current HTTP request context (Request, Response, Session).**
- **Line 72:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 88:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 90:** `csv` (`string`) — **Holds “csv” for this scope. (text)**

## Functions / methods (6 found)

### `Page_Load` — lines 12–16

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
  12 |         protected void Page_Load(object sender, EventArgs e)
  13 |         {
  14 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  15 |                 return;
  16 |         }
```

**Line notes** (what code + variables mean)

- **L12:** Page load entry (GET or postback).
- **L14:** Authorization — block wrong role / anonymous.

---

### `CurrentUid` — lines 17–21

```csharp
private static int CurrentUid()
```

#### Explanation

- **Purpose:** Implements `CurrentUid`.
- **Security:** Uses AuthGate — requires logged-in role.

#### Line-by-line (this function)

```csharp
  17 | 
  18 |         private static int CurrentUid()
  19 |         {
  20 |             return AuthGate.RequireLecturer();
  21 |         }
```

**Line notes** (what code + variables mean)

- **L20:** Authorization — block wrong role / anonymous.

---

### `GetDashboardData` — lines 25–37

```csharp
public static object GetDashboardData()
```

#### Explanation

- **Purpose:** Implements `GetDashboardData`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.

#### Line-by-line (this function)

```csharp
  25 |         public static object GetDashboardData()
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 return LecturerRepository.GetDashboardData(uid);
  32 |             }
  33 |             catch
  34 |             {
  35 |                 return new { success = false, message = "Could not load dashboard." };
  36 |             }
  37 |         }
```

**Line notes** (what code + variables mean)

- **L27:** Error handling block.
- **L29:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L30:** Authorization — block wrong role / anonymous.
- **L33:** Handle/log exception.

---

### `SaveGrade` — lines 41–64

```csharp
public static object SaveGrade(int sid, int score, string review)
```

#### Explanation

- **Purpose:** Implements `SaveGrade`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Session:** Reads/writes ASP.NET Session.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters (what each means):**
- `sid` (`int`) — Submission ID (CWSubmissions.SID).
- `score` (`int`) — Points earned or max points depending on context.
- `review` (`string`) — Holds “review” for this scope. (text)
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- `ctx` (`var`) — Current HTTP request context (Request, Response, Session).

#### Line-by-line (this function)

```csharp
  41 |         public static object SaveGrade(int sid, int score, string review)
  42 |         {
  43 |             try
  44 |             {
  45 |                 int uid = CurrentUid();
  46 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  47 |                 LecturerRepository.SaveGrade(uid, sid, score, review ?? "");
  48 |                 try
  49 |                 {
  50 |                     var ctx = System.Web.HttpContext.Current;
  51 |                     if (ctx != null && ctx.Session != null)
  52 |                     {
  53 |                         ctx.Session.Remove("PendingGradeCount");
  54 |                         ctx.Session.Remove("PendingGradeCountAt");
  55 |                     }
  56 |                 }
  57 |                 catch { }
  58 |                 return new { success = true };
  59 |             }
  60 |             catch
  61 |             {
  62 |                 return new { success = false, message = "Could not save grade." };
  63 |             }
  64 |         }
```

**Line notes** (what code + variables mean)

- **L43:** Error handling block.
- **L45:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L46:** Authorization — block wrong role / anonymous.
- **L48:** Error handling block.
- **L50:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L57:** Handle/log exception.
- **L60:** Handle/log exception.

---

### `GetPendingCount` — lines 68–80

```csharp
public static object GetPendingCount()
```

#### Explanation

- **Purpose:** Implements `GetPendingCount`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.

#### Line-by-line (this function)

```csharp
  68 |         public static object GetPendingCount()
  69 |         {
  70 |             try
  71 |             {
  72 |                 int uid = CurrentUid();
  73 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  74 |                 return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };
  75 |             }
  76 |             catch
  77 |             {
  78 |                 return new { success = false, pending = 0 };
  79 |             }
  80 |         }
```

**Line notes** (what code + variables mean)

- **L70:** Error handling block.
- **L72:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L73:** Authorization — block wrong role / anonymous.
- **L76:** Handle/log exception.

---

### `ExportGradesCsv` — lines 84–102

```csharp
public static object ExportGradesCsv(int cid)
```

#### Explanation

- **Purpose:** Implements `ExportGradesCsv`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `cid` (`int`) — Course ID (Courses.CID).
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- `csv` (`string`) — Holds “csv” for this scope. (text)

#### Line-by-line (this function)

```csharp
  84 |         public static object ExportGradesCsv(int cid)
  85 |         {
  86 |             try
  87 |             {
  88 |                 int uid = CurrentUid();
  89 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  90 |                 string csv = LecturerRepository.BuildGradesCsv(uid, cid);
  91 |                 return new
  92 |                 {
  93 |                     success = true,
  94 |                     csv = csv,
  95 |                     fileName = cid > 0 ? "grades-course-" + cid + ".csv" : "grades-all.csv"
  96 |                 };
  97 |             }
  98 |             catch
  99 |             {
 100 |                 return new { success = false, message = "Could not export grades." };
 101 |             }
 102 |         }
```

**Line notes** (what code + variables mean)

- **L84:** CSV export.
- **L86:** Error handling block.
- **L88:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L89:** Authorization — block wrong role / anonymous.
- **L90:** CSV export. | `csv` means: Holds “csv” for this scope. (text)
- **L94:** CSV export.
- **L95:** CSV export.
- **L98:** Handle/log exception.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```csharp
   1 | using System;
   2 | using System.Web.Script.Services;
   3 | using System.Web.Services;
   4 | using System.Web.UI;
   5 | using WebAppAssignment.Data;
   6 | using WebAppAssignment.Data.Security;
   7 | 
   8 | namespace WebAppAssignment.Pages.Lecturer
   9 | {
  10 |     public partial class Dashboard : Page
  11 |     {
  12 |         protected void Page_Load(object sender, EventArgs e)
  13 |         {
  14 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  15 |                 return;
  16 |         }
  17 | 
  18 |         private static int CurrentUid()
  19 |         {
  20 |             return AuthGate.RequireLecturer();
  21 |         }
  22 | 
  23 |         [WebMethod(EnableSession = true)]
  24 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  25 |         public static object GetDashboardData()
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 return LecturerRepository.GetDashboardData(uid);
  32 |             }
  33 |             catch
  34 |             {
  35 |                 return new { success = false, message = "Could not load dashboard." };
  36 |             }
  37 |         }
  38 | 
  39 |         [WebMethod(EnableSession = true)]
  40 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  41 |         public static object SaveGrade(int sid, int score, string review)
  42 |         {
  43 |             try
  44 |             {
  45 |                 int uid = CurrentUid();
  46 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  47 |                 LecturerRepository.SaveGrade(uid, sid, score, review ?? "");
  48 |                 try
  49 |                 {
  50 |                     var ctx = System.Web.HttpContext.Current;
  51 |                     if (ctx != null && ctx.Session != null)
  52 |                     {
  53 |                         ctx.Session.Remove("PendingGradeCount");
  54 |                         ctx.Session.Remove("PendingGradeCountAt");
  55 |                     }
  56 |                 }
  57 |                 catch { }
  58 |                 return new { success = true };
  59 |             }
  60 |             catch
  61 |             {
  62 |                 return new { success = false, message = "Could not save grade." };
  63 |             }
  64 |         }
  65 | 
  66 |         [WebMethod(EnableSession = true)]
  67 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  68 |         public static object GetPendingCount()
  69 |         {
  70 |             try
  71 |             {
  72 |                 int uid = CurrentUid();
  73 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  74 |                 return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };
  75 |             }
  76 |             catch
  77 |             {
  78 |                 return new { success = false, pending = 0 };
  79 |             }
  80 |         }
  81 | 
  82 |         [WebMethod(EnableSession = true)]
  83 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  84 |         public static object ExportGradesCsv(int cid)
  85 |         {
  86 |             try
  87 |             {
  88 |                 int uid = CurrentUid();
  89 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  90 |                 string csv = LecturerRepository.BuildGradesCsv(uid, cid);
  91 |                 return new
  92 |                 {
  93 |                     success = true,
  94 |                     csv = csv,
  95 |                     fileName = cid > 0 ? "grades-course-" + cid + ".csv" : "grades-all.csv"
  96 |                 };
  97 |             }
  98 |             catch
  99 |             {
 100 |                 return new { success = false, message = "Could not export grades." };
 101 |             }
 102 |         }
 103 |     }
 104 | }
```

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L8:** C# namespace grouping.
- **L12:** Page load entry (GET or postback).
- **L14:** Authorization — block wrong role / anonymous.
- **L20:** Authorization — block wrong role / anonymous.
- **L23:** Expose method to AJAX JSON calls.
- **L27:** Error handling block.
- **L29:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L30:** Authorization — block wrong role / anonymous.
- **L33:** Handle/log exception.
- **L39:** Expose method to AJAX JSON calls.
- **L43:** Error handling block.
- **L45:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L46:** Authorization — block wrong role / anonymous.
- **L48:** Error handling block.
- **L50:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L57:** Handle/log exception.
- **L60:** Handle/log exception.
- **L66:** Expose method to AJAX JSON calls.
- **L70:** Error handling block.
- **L72:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L73:** Authorization — block wrong role / anonymous.
- **L76:** Handle/log exception.
- **L82:** Expose method to AJAX JSON calls.
- **L84:** CSV export.
- **L86:** Error handling block.
- **L88:** `uid` means: User ID (Users.UID) of the logged-in or target user.
- **L89:** Authorization — block wrong role / anonymous.
- **L90:** CSV export. | `csv` means: Holds “csv” for this scope. (text)
- **L94:** CSV export.
- **L95:** CSV export.
- **L98:** Handle/log exception.

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
