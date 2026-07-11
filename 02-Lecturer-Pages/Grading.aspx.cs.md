# Grading.aspx.cs
**Source:** `Pages/Lecturer/Grading.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

List submissions for lecturer courses; assign marks and feedback; CSV export.

## File overview

- **Total lines:** 114
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
  16 | }
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

### `GetSubmissions` — lines 25–49

#### Signature

```csharp
public static object GetSubmissions()
```

#### What it is

Reads/loads data related to **Submissions** and returns it for display or further use.

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `list` | `var` | In-memory collection being built for JSON return. |
| `graded` | `int` | Holds “graded” for this scope. (integer)  Literal number `0`. |
| `s` | `—` | String value or submission-related object. |

#### Code

```csharp
  25 |         public static object GetSubmissions()
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 var list = LecturerRepository.GetRecentSubmissions(uid, 200);
  32 |                 int graded = 0;
  33 |                 foreach (var s in list)
  34 |                 {
  35 |                     if (s.ContainsKey("isGraded") && Convert.ToBoolean(s["isGraded"])) graded++;
  36 |                 }
  37 |                 return new
  38 |                 {
  39 |                     success = true,
  40 |                     submissions = list,
  41 |                     gradedCount = graded,
  42 |                     totalCount = list.Count
  43 |                 };
  44 |             }
  45 |             catch (Exception ex)
  46 |             {
  47 |                 return new { success = false, message = "Request failed." };
  48 |             }
  49 |         }
```

---

### `SaveGrade` — lines 53–76

#### Signature

```csharp
public static object SaveGrade(int sid, decimal score, string review)
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
| `score` | `decimal` | Points earned or max points depending on context. |
| `review` | `string` | Holds “review” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `ctx` | `var` | Current HTTP request context (Request, Response, Session). |

#### Code

```csharp
  53 |         public static object SaveGrade(int sid, decimal score, string review)
  54 |         {
  55 |             try
  56 |             {
  57 |                 int uid = CurrentUid();
  58 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  59 |                 LecturerRepository.SaveGrade(uid, sid, score, review ?? "");
  60 |                 try
  61 |                 {
  62 |                     var ctx = System.Web.HttpContext.Current;
  63 |                     if (ctx != null && ctx.Session != null)
  64 |                     {
  65 |                         ctx.Session.Remove("PendingGradeCount");
  66 |                         ctx.Session.Remove("PendingGradeCountAt");
  67 |                     }
  68 |                 }
  69 |                 catch { }
  70 |                 return new { success = true };
  71 |             }
  72 |             catch (Exception ex)
  73 |             {
  74 |                 return new { success = false, message = "Request failed." };
  75 |             }
  76 |         }
```

---

### `ExportGradesCsv` — lines 80–96

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
| `name` | `string` | Display name of user/course/criterion. |

#### Code

```csharp
  80 |         public static object ExportGradesCsv(int cid)
  81 |         {
  82 |             try
  83 |             {
  84 |                 int uid = CurrentUid();
  85 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  86 |                 string csv = LecturerRepository.BuildGradesCsv(uid, cid);
  87 |                 string name = cid > 0
  88 |                     ? "grades-course-" + cid + ".csv"
  89 |                     : "grades-all.csv";
  90 |                 return new { success = true, csv = csv, fileName = name };
  91 |             }
  92 |             catch
  93 |             {
  94 |                 return new { success = false, message = "Could not export grades." };
  95 |             }
  96 |         }
```

---

### `GetPendingCount` — lines 100–112

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
 100 |         public static object GetPendingCount()
 101 |         {
 102 |             try
 103 |             {
 104 |                 int uid = CurrentUid();
 105 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 106 |                 return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };
 107 |             }
 108 |             catch
 109 |             {
 110 |                 return new { success = false, pending = 0 };
 111 |             }
 112 |         }
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
  10 |     public partial class Grading : Page
  11 |     {
  12 |         protected void Page_Load(object sender, EventArgs e)
  13 |         {
  14 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  15 |                 return;
  16 | }
  17 | 
  18 |         private static int CurrentUid()
  19 |         {
  20 |             return AuthGate.RequireLecturer();
  21 |         }
  22 | 
  23 |         [WebMethod(EnableSession = true)]
  24 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  25 |         public static object GetSubmissions()
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 var list = LecturerRepository.GetRecentSubmissions(uid, 200);
  32 |                 int graded = 0;
  33 |                 foreach (var s in list)
  34 |                 {
  35 |                     if (s.ContainsKey("isGraded") && Convert.ToBoolean(s["isGraded"])) graded++;
  36 |                 }
  37 |                 return new
  38 |                 {
  39 |                     success = true,
  40 |                     submissions = list,
  41 |                     gradedCount = graded,
  42 |                     totalCount = list.Count
  43 |                 };
  44 |             }
  45 |             catch (Exception ex)
  46 |             {
  47 |                 return new { success = false, message = "Request failed." };
  48 |             }
  49 |         }
  50 | 
  51 |         [WebMethod(EnableSession = true)]
  52 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  53 |         public static object SaveGrade(int sid, decimal score, string review)
  54 |         {
  55 |             try
  56 |             {
  57 |                 int uid = CurrentUid();
  58 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  59 |                 LecturerRepository.SaveGrade(uid, sid, score, review ?? "");
  60 |                 try
  61 |                 {
  62 |                     var ctx = System.Web.HttpContext.Current;
  63 |                     if (ctx != null && ctx.Session != null)
  64 |                     {
  65 |                         ctx.Session.Remove("PendingGradeCount");
  66 |                         ctx.Session.Remove("PendingGradeCountAt");
  67 |                     }
  68 |                 }
  69 |                 catch { }
  70 |                 return new { success = true };
  71 |             }
  72 |             catch (Exception ex)
  73 |             {
  74 |                 return new { success = false, message = "Request failed." };
  75 |             }
  76 |         }
  77 | 
  78 |         [WebMethod(EnableSession = true)]
  79 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  80 |         public static object ExportGradesCsv(int cid)
  81 |         {
  82 |             try
  83 |             {
  84 |                 int uid = CurrentUid();
  85 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  86 |                 string csv = LecturerRepository.BuildGradesCsv(uid, cid);
  87 |                 string name = cid > 0
  88 |                     ? "grades-course-" + cid + ".csv"
  89 |                     : "grades-all.csv";
  90 |                 return new { success = true, csv = csv, fileName = name };
  91 |             }
  92 |             catch
  93 |             {
  94 |                 return new { success = false, message = "Could not export grades." };
  95 |             }
  96 |         }
  97 | 
  98 |         [WebMethod(EnableSession = true)]
  99 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 100 |         public static object GetPendingCount()
 101 |         {
 102 |             try
 103 |             {
 104 |                 int uid = CurrentUid();
 105 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 106 |                 return new { success = true, pending = LecturerRepository.CountPendingGrading(uid) };
 107 |             }
 108 |             catch
 109 |             {
 110 |                 return new { success = false, pending = 0 };
 111 |             }
 112 |         }
 113 |     }
 114 | }
```
