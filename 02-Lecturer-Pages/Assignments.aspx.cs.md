# Assignments.aspx.cs
**Source:** `Pages/Lecturer/Assignments.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 113
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

### `GetCourses` — lines 25–37

#### Signature

```csharp
public static object GetCourses()
```

#### What it is

Reads/loads data related to **Courses** and returns it for display or further use.

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
  25 |         public static object GetCourses()
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 return new { success = true, courses = LecturerRepository.GetLecturerCoursesSimple(uid) };
  32 |             }
  33 |             catch (Exception ex)
  34 |             {
  35 |                 return new { success = false, message = "Request failed." };
  36 |             }
  37 |         }
```

---

### `GetCourseWorks` — lines 41–53

#### Signature

```csharp
public static object GetCourseWorks()
```

#### What it is

Reads/loads data related to **Course Works** and returns it for display or further use.

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
  41 |         public static object GetCourseWorks()
  42 |         {
  43 |             try
  44 |             {
  45 |                 int uid = CurrentUid();
  46 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  47 |                 return new { success = true, items = LecturerRepository.GetCourseWorksForLecturer(uid) };
  48 |             }
  49 |             catch (Exception ex)
  50 |             {
  51 |                 return new { success = false, message = "Request failed." };
  52 |             }
  53 |         }
```

---

### `SaveCourseWork` — lines 61–94

#### Signature

```csharp
public static object SaveCourseWork(
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

#### What it is

Creates or updates an assignment (CourseWorks) including due date and META.

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `int?` | CourseWork ID (assignment) (CourseWorks.CWID). |
| `cid` | `int` | Course ID (Courses.CID). |
| `title` | `string` | Title of course work / page heading. |
| `instructions` | `string` | Student-facing assignment instructions (plain part of Description). |
| `type` | `string` | Holds “type” for this scope. (text) |
| `score` | `decimal` | Points earned or max points depending on context. |
| `creditGiven` | `decimal` | Holds “credit Given” for this scope. (number/score) |
| `rubricJson` | `string` | Holds “rubric Json” for this scope. (text) |
| `extraMetaJson` | `string` | Holds “extra Meta Json” for this scope. (text) |
| `objectiveQuestionsJson` | `string` | Holds “objective Questions Json” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `id` | `int` | Generic primary key / identifier. |

#### Code

```csharp
  61 |         public static object SaveCourseWork(
  62 |         int? cwid,
  63 |         int cid,
  64 |         string title,
  65 |         string instructions,
  66 |         string type,
  67 |         decimal score,
  68 |         decimal creditGiven,
  69 |         string rubricJson,
  70 |         string extraMetaJson,
  71 |         string objectiveQuestionsJson)
  72 |         {
  73 |             try
  74 |             {
  75 |                 int uid = CurrentUid();
  76 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  77 |                 if (cid <= 0) return new { success = false, message = "Select a target course." };
  78 |                 if (string.IsNullOrWhiteSpace(title)) return new { success = false, message = "Title is required." };
  79 | 
  80 |                 // All assessments are graded out of 100 pts
  81 |                 score = 100m;
  82 |                 creditGiven = 100m;
  83 | 
  84 |                 int id = LecturerRepository.SaveCourseWork(
  85 |                 uid, cwid, cid, title.Trim(), instructions, type,
  86 |                 score, creditGiven, rubricJson, extraMetaJson, objectiveQuestionsJson);
  87 | 
  88 |                 return new { success = true, cwid = id };
  89 |             }
  90 |             catch (Exception ex)
  91 |             {
  92 |                 return new { success = false, message = "Request failed." };
  93 |             }
  94 |         }
```

---

### `DeleteCourseWork` — lines 98–111

#### Signature

```csharp
public static object DeleteCourseWork(int cwid)
```

#### What it is

Deletes or clears **Delete Course Work** (data or temporary state).

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `int` | CourseWork ID (assignment) (CourseWorks.CWID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Code

```csharp
  98 |         public static object DeleteCourseWork(int cwid)
  99 |         {
 100 |             try
 101 |             {
 102 |                 int uid = CurrentUid();
 103 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 104 |                 LecturerRepository.DeleteCourseWork(uid, cwid);
 105 |                 return new { success = true };
 106 |             }
 107 |             catch (Exception ex)
 108 |             {
 109 |                 return new { success = false, message = "Request failed." };
 110 |             }
 111 |         }
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
  10 |     public partial class Assignments : Page
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
  25 |         public static object GetCourses()
  26 |         {
  27 |             try
  28 |             {
  29 |                 int uid = CurrentUid();
  30 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  31 |                 return new { success = true, courses = LecturerRepository.GetLecturerCoursesSimple(uid) };
  32 |             }
  33 |             catch (Exception ex)
  34 |             {
  35 |                 return new { success = false, message = "Request failed." };
  36 |             }
  37 |         }
  38 | 
  39 |         [WebMethod(EnableSession = true)]
  40 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  41 |         public static object GetCourseWorks()
  42 |         {
  43 |             try
  44 |             {
  45 |                 int uid = CurrentUid();
  46 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  47 |                 return new { success = true, items = LecturerRepository.GetCourseWorksForLecturer(uid) };
  48 |             }
  49 |             catch (Exception ex)
  50 |             {
  51 |                 return new { success = false, message = "Request failed." };
  52 |             }
  53 |         }
  54 | 
  55 |         /// <summary>
  56 |         /// Saves into CourseWorks (CWID, ChID, Title, Description, DueDate)
  57 |         /// and optionally ObjectiveQuestions (QID, QuestionText, OptionA-D, CorrectAnswer).
  58 |         /// </summary>
  59 |         [WebMethod(EnableSession = true)]
  60 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  61 |         public static object SaveCourseWork(
  62 |         int? cwid,
  63 |         int cid,
  64 |         string title,
  65 |         string instructions,
  66 |         string type,
  67 |         decimal score,
  68 |         decimal creditGiven,
  69 |         string rubricJson,
  70 |         string extraMetaJson,
  71 |         string objectiveQuestionsJson)
  72 |         {
  73 |             try
  74 |             {
  75 |                 int uid = CurrentUid();
  76 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  77 |                 if (cid <= 0) return new { success = false, message = "Select a target course." };
  78 |                 if (string.IsNullOrWhiteSpace(title)) return new { success = false, message = "Title is required." };
  79 | 
  80 |                 // All assessments are graded out of 100 pts
  81 |                 score = 100m;
  82 |                 creditGiven = 100m;
  83 | 
  84 |                 int id = LecturerRepository.SaveCourseWork(
  85 |                 uid, cwid, cid, title.Trim(), instructions, type,
  86 |                 score, creditGiven, rubricJson, extraMetaJson, objectiveQuestionsJson);
  87 | 
  88 |                 return new { success = true, cwid = id };
  89 |             }
  90 |             catch (Exception ex)
  91 |             {
  92 |                 return new { success = false, message = "Request failed." };
  93 |             }
  94 |         }
  95 | 
  96 |         [WebMethod(EnableSession = true)]
  97 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  98 |         public static object DeleteCourseWork(int cwid)
  99 |         {
 100 |             try
 101 |             {
 102 |                 int uid = CurrentUid();
 103 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 104 |                 LecturerRepository.DeleteCourseWork(uid, cwid);
 105 |                 return new { success = true };
 106 |             }
 107 |             catch (Exception ex)
 108 |             {
 109 |                 return new { success = false, message = "Request failed." };
 110 |             }
 111 |         }
 112 |     }
 113 | }
```
