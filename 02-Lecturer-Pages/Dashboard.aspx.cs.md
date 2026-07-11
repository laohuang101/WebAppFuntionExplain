# Dashboard.aspx.cs
**Source:** `Pages/Lecturer/Dashboard.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 104
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (6 found)

### `Page_Load` — lines 12–16

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. ASP.NET calls this automatically on every request.
2. On first load (`!IsPostBack`), initialize UI or redirect if already logged in.
3. On postback, button handlers run separately after this method.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  12 |         protected void Page_Load(object sender, EventArgs e)
  13 |         {
  14 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  15 |                 return;
  16 |         }
```

---

### `CurrentUid` — lines 17–21

#### Signature

```csharp
private static int CurrentUid()
```

#### What it is

Function `CurrentUid` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  17 | 
  18 |         private static int CurrentUid()
  19 |         {
  20 |             return AuthGate.RequireLecturer();
  21 |         }
```

---

### `GetDashboardData` — lines 25–37

#### Signature

```csharp
public static object GetDashboardData()
```

#### What it is

Reads/loads data related to **Dashboard Data** and returns it for display or further use.

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Code

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

---

### `SaveGrade` — lines 41–64

#### Signature

```csharp
public static object SaveGrade(int sid, int score, string review)
```

#### What it is

Saves marks and feedback for a student submission.

#### How it works

1. Clear Session data (logout or end of multi-step flow).
2. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sid` | `int` | Submission ID (CWSubmissions.SID). |
| `score` | `int` | Points earned or max points depending on context. |
| `review` | `string` | Holds “review” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `ctx` | `var` | Current HTTP request context (Request, Response, Session). |

#### Code

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

---

### `GetPendingCount` — lines 68–80

#### Signature

```csharp
public static object GetPendingCount()
```

#### What it is

Reads/loads data related to **Pending Count** and returns it for display or further use.

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Code

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

---

### `ExportGradesCsv` — lines 84–102

#### Signature

```csharp
public static object ExportGradesCsv(int cid)
```

#### What it is

Function `ExportGradesCsv` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `int` | Course ID (Courses.CID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `csv` | `string` | Holds “csv” for this scope. (text) |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
