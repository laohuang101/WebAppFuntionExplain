# Students.aspx.cs
**Source:** `Pages/Lecturer/Students.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Enrolled students per course with progress counts.

## File overview

- **Total lines:** 58
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (4 found)

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

### `GetStudents` — lines 25–38

#### Signature

```csharp
public static object GetStudents(string search)
```

#### What it is

Reads/loads data related to **Students** and returns it for display or further use.

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `search` | `string` | Holds “search” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `list` | `var` | In-memory collection being built for JSON return. |

#### Code

```csharp
  25 |         public static object GetStudents(string search)
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 var list = LecturerRepository.GetStudentPerformance(uid, search);
  32 |                 return new { success = true, students = list };
  33 |             }
  34 |             catch (Exception ex)
  35 |             {
  36 |                 return new { success = false, message = "Request failed." };
  37 |             }
  38 |         }
```

---

### `GetStudentDetail` — lines 42–56

#### Signature

```csharp
public static object GetStudentDetail(int studentUid, int cid)
```

#### What it is

Reads/loads data related to **Student Detail** and returns it for display or further use.

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `studentUid` | `int` | Users.UID of the student. |
| `cid` | `int` | Course ID (Courses.CID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `detail` | `var` | Holds “detail” for this scope. |

#### Code

```csharp
  42 |         public static object GetStudentDetail(int studentUid, int cid)
  43 |         {
  44 |             try
  45 |             {
  46 |                 int uid = CurrentUid();
  47 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  48 |                 var detail = LecturerRepository.GetStudentDetail(uid, studentUid, cid);
  49 |                 if (detail == null) return new { success = false, message = "Student not found." };
  50 |                 return new { success = true, detail = detail };
  51 |             }
  52 |             catch (Exception ex)
  53 |             {
  54 |                 return new { success = false, message = "Request failed." };
  55 |             }
  56 |         }
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
  10 |     public partial class Students : Page
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
  25 |         public static object GetStudents(string search)
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 var list = LecturerRepository.GetStudentPerformance(uid, search);
  32 |                 return new { success = true, students = list };
  33 |             }
  34 |             catch (Exception ex)
  35 |             {
  36 |                 return new { success = false, message = "Request failed." };
  37 |             }
  38 |         }
  39 | 
  40 |         [WebMethod(EnableSession = true)]
  41 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  42 |         public static object GetStudentDetail(int studentUid, int cid)
  43 |         {
  44 |             try
  45 |             {
  46 |                 int uid = CurrentUid();
  47 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  48 |                 var detail = LecturerRepository.GetStudentDetail(uid, studentUid, cid);
  49 |                 if (detail == null) return new { success = false, message = "Student not found." };
  50 |                 return new { success = true, detail = detail };
  51 |             }
  52 |             catch (Exception ex)
  53 |             {
  54 |                 return new { success = false, message = "Request failed." };
  55 |             }
  56 |         }
  57 |     }
  58 | }
```
