# CourseCreation.aspx.cs
**Source:** `Pages/Lecturer/CourseCreation.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Create/edit courses, curriculum (chapters/lessons), media, publish/draft.

## File overview

- **Total lines:** 251
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (13 found)

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

### `CurrentUid` — lines 17–22

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
  20 |             // Lecturer or Admin only for course APIs
  21 |             return AuthGate.RequireLecturer();
  22 |         }
```

---

### `Fail` — lines 23–27

#### Signature

```csharp
private static object Fail(string message)
```

#### What it is

Function `Fail` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `message` | `string` | Status text for the UI. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  23 | 
  24 |         private static object Fail(string message)
  25 |         {
  26 |             return new { success = false, message = message ?? "Request failed." };
  27 |         }
```

---

### `GetCoursesData` — lines 31–44

#### Signature

```csharp
public static object GetCoursesData()
```

#### What it is

Reads/loads data related to **Courses Data** and returns it for display or further use.

#### How it works

1. Build and return the result object (success or data for the UI).
2. On bad input or failed check, return a failure message and stop.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `courses` | `var` | Often a collection related to courses (plural name). |

#### Code

```csharp
  31 |         public static object GetCoursesData()
  32 |         {
  33 |             try
  34 |             {
  35 |                 int uid = CurrentUid();
  36 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  37 |                 var courses = LecturerRepository.GetCoursesForLecturer(uid);
  38 |                 return new { success = true, courses = courses };
  39 |             }
  40 |             catch
  41 |             {
  42 |                 return Fail("Could not load courses.");
  43 |             }
  44 |         }
```

---

### `SaveCourseInfo` — lines 48–66

#### Signature

```csharp
public static object SaveCourseInfo(string name, string desc, string category, string level, string bgImg, int cid)
```

#### What it is

Saves or updates **Save Course Info** in the database or UI state.

#### How it works

1. On bad input or failed check, return a failure message and stop.
2. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `name` | `string` | Display name of user/course/criterion. |
| `desc` | `string` | Description text (may embed <<<META>>> JSON). |
| `category` | `string` | Holds “category” for this scope. (text) |
| `level` | `string` | Holds “level” for this scope. (text) |
| `bgImg` | `string` | Holds “bg Img” for this scope. (text) |
| `cid` | `int` | Course ID (Courses.CID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `newCid` | `int` | Identifier (`newCid`) — database primary/foreign key. (integer) |

#### Code

```csharp
  48 |         public static object SaveCourseInfo(string name, string desc, string category, string level, string bgImg, int cid)
  49 |         {
  50 |             try
  51 |             {
  52 |                 int uid = CurrentUid();
  53 |                 if (uid == 0)
  54 |                     return AuthGate.NotAuthenticatedJson("Lecturer sign-in required. Please log out and log in again.");
  55 |                 if (string.IsNullOrWhiteSpace(name)) return Fail("Course title is required.");
  56 | 
  57 |                 int? existing = cid > 0 ? cid : (int?)null;
  58 |                 int newCid = LecturerRepository.SaveCourse(
  59 |                     uid, existing, name.Trim(), desc ?? "", bgImg, category ?? "", level ?? "");
  60 |                 return new { success = true, cid = newCid };
  61 |             }
  62 |             catch
  63 |             {
  64 |                 return Fail("Could not save course.");
  65 |             }
  66 |         }
```

---

### `SetCoursePublished` — lines 70–88

#### Signature

```csharp
public static object SetCoursePublished(int cid, bool published)
```

#### What it is

Sets Courses.IsPublished so the course shows or hides on Landing.

#### How it works

1. On bad input or failed check, return a failure message and stop.
2. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `int` | Course ID (Courses.CID). |
| `published` | `bool` | UI/publish intent flag when saving a course/work. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `state` | `bool` | Holds “state” for this scope. (true/false) |

#### Code

```csharp
  70 |         public static object SetCoursePublished(int cid, bool published)
  71 |         {
  72 |             try
  73 |             {
  74 |                 int uid = CurrentUid();
  75 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  76 |                 if (cid <= 0) return Fail("Invalid course.");
  77 |                 bool state = LecturerRepository.SetCoursePublished(uid, cid, published);
  78 |                 return new { success = true, isPublished = state, status = state ? "Published" : "Draft" };
  79 |             }
  80 |             catch (UnauthorizedAccessException)
  81 |             {
  82 |                 return AuthGate.ForbiddenJson();
  83 |             }
  84 |             catch
  85 |             {
  86 |                 return Fail("Could not update publish state.");
  87 |             }
  88 |         }
```

---

### `GetCourseCurriculum` — lines 92–105

#### Signature

```csharp
public static object GetCourseCurriculum(int cid)
```

#### What it is

Reads/loads data related to **Course Curriculum** and returns it for display or further use.

#### How it works

1. Build and return the result object (success or data for the UI).
2. On bad input or failed check, return a failure message and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `int` | Course ID (Courses.CID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `chapters` | `var` | Often a collection related to chapters (plural name). |

#### Code

```csharp
  92 |         public static object GetCourseCurriculum(int cid)
  93 |         {
  94 |             try
  95 |             {
  96 |                 int uid = CurrentUid();
  97 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  98 |                 var chapters = LecturerRepository.GetCurriculum(uid, cid);
  99 |                 return new { success = true, chapters = chapters };
 100 |             }
 101 |             catch (Exception ex)
 102 |             {
 103 |                 return Fail("Request failed.");
 104 |             }
 105 |         }
```

---

### `SaveChapter` — lines 109–126

#### Signature

```csharp
public static object SaveChapter(int chid, int cid, string title)
```

#### What it is

Saves or updates **Save Chapter** in the database or UI state.

#### How it works

1. On bad input or failed check, return a failure message and stop.
2. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `chid` | `int` | Chapter ID (Chapters.ChID). |
| `cid` | `int` | Course ID (Courses.CID). |
| `title` | `string` | Title of course work / page heading. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `id` | `int` | Generic primary key / identifier. |

#### Code

```csharp
 109 |         public static object SaveChapter(int chid, int cid, string title)
 110 |         {
 111 |             try
 112 |             {
 113 |                 int uid = CurrentUid();
 114 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 115 |                 if (string.IsNullOrWhiteSpace(title)) return Fail("Section title is required.");
 116 |                 if (cid <= 0) return Fail("Invalid course id.");
 117 |                 // chid == 0 means create new section
 118 |                 int? existing = chid > 0 ? chid : (int?)null;
 119 |                 int id = LecturerRepository.SaveChapter(uid, existing, cid, title.Trim());
 120 |                 return new { success = true, chid = id };
 121 |             }
 122 |             catch (Exception ex)
 123 |             {
 124 |                 return Fail("Request failed.");
 125 |             }
 126 |         }
```

---

### `DeleteChapter` — lines 130–143

#### Signature

```csharp
public static object DeleteChapter(int chid)
```

#### What it is

Deletes or clears **Delete Chapter** (data or temporary state).

#### How it works

1. Build and return the result object (success or data for the UI).
2. On bad input or failed check, return a failure message and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `chid` | `int` | Chapter ID (Chapters.ChID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Code

```csharp
 130 |         public static object DeleteChapter(int chid)
 131 |         {
 132 |             try
 133 |             {
 134 |                 int uid = CurrentUid();
 135 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 136 |                 LecturerRepository.DeleteChapter(uid, chid);
 137 |                 return new { success = true };
 138 |             }
 139 |             catch (Exception ex)
 140 |             {
 141 |                 return Fail("Request failed.");
 142 |             }
 143 |         }
```

---

### `SaveSubChapter` — lines 147–175

#### Signature

```csharp
public static object SaveSubChapter(int schid, int chid, string title, string type, string content)
```

#### What it is

Saves or updates **Save Sub Chapter** in the database or UI state.

#### How it works

1. On bad input or failed check, return a failure message and stop.
2. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `schid` | `int` | SubChapter / lesson ID. |
| `chid` | `int` | Chapter ID (Chapters.ChID). |
| `title` | `string` | Title of course work / page heading. |
| `type` | `string` | Holds “type” for this scope. (text) |
| `content` | `string` | Submission body text or JSON payload in CWSubmissions. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `body` | `string` | HTTP request body. |
| `materialsJson` | `string` | Holds “materials Json” for this scope. (text) |
| `sep` | `string` | Holds “sep” for this scope. (text)  Literal text string. |
| `idx` | `int` | Holds “idx” for this scope. (integer) |
| `id` | `int` | Generic primary key / identifier. |

#### Code

```csharp
 147 |         public static object SaveSubChapter(int schid, int chid, string title, string type, string content)
 148 |         {
 149 |             try
 150 |             {
 151 |                 int uid = CurrentUid();
 152 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 153 |                 if (string.IsNullOrWhiteSpace(title)) return Fail("Lesson title is required.");
 154 |                 if (chid <= 0) return Fail("Invalid section id.");
 155 | 
 156 |                 // Materials may be appended after separator from client
 157 |                 string body = content ?? "";
 158 |                 string materialsJson = null;
 159 |                 const string sep = "\n--MATERIALS--\n";
 160 |                 int idx = body.IndexOf(sep, StringComparison.Ordinal);
 161 |                 if (idx >= 0)
 162 |                 {
 163 |                     materialsJson = body.Substring(idx + sep.Length);
 164 |                     body = body.Substring(0, idx);
 165 |                 }
 166 | 
 167 |                 int? existing = schid > 0 ? schid : (int?)null;
 168 |                 int id = LecturerRepository.SaveSubChapter(uid, existing, chid, title.Trim(), type, body, materialsJson);
 169 |                 return new { success = true, schid = id };
 170 |             }
 171 |             catch (Exception ex)
 172 |             {
 173 |                 return Fail("Request failed.");
 174 |             }
 175 |         }
```

---

### `DeleteSubChapter` — lines 179–192

#### Signature

```csharp
public static object DeleteSubChapter(int schid)
```

#### What it is

Deletes or clears **Delete Sub Chapter** (data or temporary state).

#### How it works

1. Build and return the result object (success or data for the UI).
2. On bad input or failed check, return a failure message and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `schid` | `int` | SubChapter / lesson ID. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Code

```csharp
 179 |         public static object DeleteSubChapter(int schid)
 180 |         {
 181 |             try
 182 |             {
 183 |                 int uid = CurrentUid();
 184 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 185 |                 LecturerRepository.DeleteSubChapter(uid, schid);
 186 |                 return new { success = true };
 187 |             }
 188 |             catch (Exception ex)
 189 |             {
 190 |                 return Fail("Request failed.");
 191 |             }
 192 |         }
```

---

### `DeleteCourse` — lines 196–209

#### Signature

```csharp
public static object DeleteCourse(int cid)
```

#### What it is

Deletes or clears **Delete Course** (data or temporary state).

#### How it works

1. Build and return the result object (success or data for the UI).
2. On bad input or failed check, return a failure message and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `int` | Course ID (Courses.CID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Code

```csharp
 196 |         public static object DeleteCourse(int cid)
 197 |         {
 198 |             try
 199 |             {
 200 |                 int uid = CurrentUid();
 201 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 202 |                 LecturerRepository.DeleteCourse(uid, cid);
 203 |                 return new { success = true };
 204 |             }
 205 |             catch (Exception ex)
 206 |             {
 207 |                 return Fail("Request failed.");
 208 |             }
 209 |         }
```

---

### `GetLessonDetails` — lines 213–249

#### Signature

```csharp
public static object GetLessonDetails(int schid)
```

#### What it is

Reads/loads data related to **Lesson Details** and returns it for display or further use.

#### How it works

1. Run SQL that returns one value (count, id, flag).
2. On bad input or failed check, return a failure message and stop.
3. Run a SELECT query and load the matching rows into memory.
4. Build and return the result object (success or data for the UI).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `schid` | `int` | SubChapter / lesson ID. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `titleObj` | `var` | Holds “title Obj” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY). |
| `title` | `string` | Title of course work / page heading. |
| `type` | `string` | Holds “type” for this scope. (text)  Literal text string. |
| `content` | `string` | Submission body text or JSON payload in CWSubmissions.  Literal text string. |
| `mats` | `var` | Often a collection related to mats (plural name).  Assigned from SQL SELECT result set. |

#### Code

```csharp
 213 |         public static object GetLessonDetails(int schid)
 214 |         {
 215 |             try
 216 |             {
 217 |                 int uid = CurrentUid();
 218 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 219 | 
 220 |                 // Pure SQL: SubChapters (plural) + first StudyMat for type/content
 221 |                 var titleObj = DbHelper.ExecuteScalar(
 222 |                 "SELECT Title FROM SubChapters WHERE SchID = @SchID",
 223 |                 DbHelper.P("@SchID", schid));
 224 |                 if (titleObj == null || titleObj == System.DBNull.Value)
 225 |                 return Fail("Lesson not found.");
 226 | 
 227 |                 string title = titleObj.ToString();
 228 |                 string type = "Text";
 229 |                 string content = "";
 230 | 
 231 |                 var mats = DbHelper.ExecuteQuery(
 232 |                 "SELECT TOP 1 Type, TextContent, MediaLink FROM StudyMats WHERE SchID = @SchID ORDER BY [Index], SMID",
 233 |                 DbHelper.P("@SchID", schid));
 234 |                 if (mats.Rows.Count > 0)
 235 |                 {
 236 |                     type = DbHelper.SafeString(mats.Rows[0]["Type"]);
 237 |                     if (string.IsNullOrEmpty(type)) type = "Text";
 238 |                     content = !string.IsNullOrEmpty(DbHelper.SafeString(mats.Rows[0]["MediaLink"]))
 239 |                     ? DbHelper.SafeString(mats.Rows[0]["MediaLink"])
 240 |                     : DbHelper.SafeString(mats.Rows[0]["TextContent"]);
 241 |                 }
 242 | 
 243 |                 return new { success = true, title = title, type = type, content = content };
 244 |             }
 245 |             catch (Exception ex)
 246 |             {
 247 |                 return Fail("Request failed.");
 248 |             }
 249 |         }
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
  10 |     public partial class Course_Creation : Page
  11 |     {
  12 |         protected void Page_Load(object sender, EventArgs e)
  13 |         {
  14 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  15 |                 return;
  16 |         }
  17 | 
  18 |         private static int CurrentUid()
  19 |         {
  20 |             // Lecturer or Admin only for course APIs
  21 |             return AuthGate.RequireLecturer();
  22 |         }
  23 | 
  24 |         private static object Fail(string message)
  25 |         {
  26 |             return new { success = false, message = message ?? "Request failed." };
  27 |         }
  28 | 
  29 |         [WebMethod(EnableSession = true)]
  30 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  31 |         public static object GetCoursesData()
  32 |         {
  33 |             try
  34 |             {
  35 |                 int uid = CurrentUid();
  36 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  37 |                 var courses = LecturerRepository.GetCoursesForLecturer(uid);
  38 |                 return new { success = true, courses = courses };
  39 |             }
  40 |             catch
  41 |             {
  42 |                 return Fail("Could not load courses.");
  43 |             }
  44 |         }
  45 | 
  46 |         [WebMethod(EnableSession = true)]
  47 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  48 |         public static object SaveCourseInfo(string name, string desc, string category, string level, string bgImg, int cid)
  49 |         {
  50 |             try
  51 |             {
  52 |                 int uid = CurrentUid();
  53 |                 if (uid == 0)
  54 |                     return AuthGate.NotAuthenticatedJson("Lecturer sign-in required. Please log out and log in again.");
  55 |                 if (string.IsNullOrWhiteSpace(name)) return Fail("Course title is required.");
  56 | 
  57 |                 int? existing = cid > 0 ? cid : (int?)null;
  58 |                 int newCid = LecturerRepository.SaveCourse(
  59 |                     uid, existing, name.Trim(), desc ?? "", bgImg, category ?? "", level ?? "");
  60 |                 return new { success = true, cid = newCid };
  61 |             }
  62 |             catch
  63 |             {
  64 |                 return Fail("Could not save course.");
  65 |             }
  66 |         }
  67 | 
  68 |         [WebMethod(EnableSession = true)]
  69 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  70 |         public static object SetCoursePublished(int cid, bool published)
  71 |         {
  72 |             try
  73 |             {
  74 |                 int uid = CurrentUid();
  75 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  76 |                 if (cid <= 0) return Fail("Invalid course.");
  77 |                 bool state = LecturerRepository.SetCoursePublished(uid, cid, published);
  78 |                 return new { success = true, isPublished = state, status = state ? "Published" : "Draft" };
  79 |             }
  80 |             catch (UnauthorizedAccessException)
  81 |             {
  82 |                 return AuthGate.ForbiddenJson();
  83 |             }
  84 |             catch
  85 |             {
  86 |                 return Fail("Could not update publish state.");
  87 |             }
  88 |         }
  89 | 
  90 |         [WebMethod(EnableSession = true)]
  91 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
  92 |         public static object GetCourseCurriculum(int cid)
  93 |         {
  94 |             try
  95 |             {
  96 |                 int uid = CurrentUid();
  97 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
  98 |                 var chapters = LecturerRepository.GetCurriculum(uid, cid);
  99 |                 return new { success = true, chapters = chapters };
 100 |             }
 101 |             catch (Exception ex)
 102 |             {
 103 |                 return Fail("Request failed.");
 104 |             }
 105 |         }
 106 | 
 107 |         [WebMethod(EnableSession = true)]
 108 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 109 |         public static object SaveChapter(int chid, int cid, string title)
 110 |         {
 111 |             try
 112 |             {
 113 |                 int uid = CurrentUid();
 114 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 115 |                 if (string.IsNullOrWhiteSpace(title)) return Fail("Section title is required.");
 116 |                 if (cid <= 0) return Fail("Invalid course id.");
 117 |                 // chid == 0 means create new section
 118 |                 int? existing = chid > 0 ? chid : (int?)null;
 119 |                 int id = LecturerRepository.SaveChapter(uid, existing, cid, title.Trim());
 120 |                 return new { success = true, chid = id };
 121 |             }
 122 |             catch (Exception ex)
 123 |             {
 124 |                 return Fail("Request failed.");
 125 |             }
 126 |         }
 127 | 
 128 |         [WebMethod(EnableSession = true)]
 129 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 130 |         public static object DeleteChapter(int chid)
 131 |         {
 132 |             try
 133 |             {
 134 |                 int uid = CurrentUid();
 135 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 136 |                 LecturerRepository.DeleteChapter(uid, chid);
 137 |                 return new { success = true };
 138 |             }
 139 |             catch (Exception ex)
 140 |             {
 141 |                 return Fail("Request failed.");
 142 |             }
 143 |         }
 144 | 
 145 |         [WebMethod(EnableSession = true)]
 146 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 147 |         public static object SaveSubChapter(int schid, int chid, string title, string type, string content)
 148 |         {
 149 |             try
 150 |             {
 151 |                 int uid = CurrentUid();
 152 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 153 |                 if (string.IsNullOrWhiteSpace(title)) return Fail("Lesson title is required.");
 154 |                 if (chid <= 0) return Fail("Invalid section id.");
 155 | 
 156 |                 // Materials may be appended after separator from client
 157 |                 string body = content ?? "";
 158 |                 string materialsJson = null;
 159 |                 const string sep = "\n--MATERIALS--\n";
 160 |                 int idx = body.IndexOf(sep, StringComparison.Ordinal);
 161 |                 if (idx >= 0)
 162 |                 {
 163 |                     materialsJson = body.Substring(idx + sep.Length);
 164 |                     body = body.Substring(0, idx);
 165 |                 }
 166 | 
 167 |                 int? existing = schid > 0 ? schid : (int?)null;
 168 |                 int id = LecturerRepository.SaveSubChapter(uid, existing, chid, title.Trim(), type, body, materialsJson);
 169 |                 return new { success = true, schid = id };
 170 |             }
 171 |             catch (Exception ex)
 172 |             {
 173 |                 return Fail("Request failed.");
 174 |             }
 175 |         }
 176 | 
 177 |         [WebMethod(EnableSession = true)]
 178 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 179 |         public static object DeleteSubChapter(int schid)
 180 |         {
 181 |             try
 182 |             {
 183 |                 int uid = CurrentUid();
 184 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 185 |                 LecturerRepository.DeleteSubChapter(uid, schid);
 186 |                 return new { success = true };
 187 |             }
 188 |             catch (Exception ex)
 189 |             {
 190 |                 return Fail("Request failed.");
 191 |             }
 192 |         }
 193 | 
 194 |         [WebMethod(EnableSession = true)]
 195 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 196 |         public static object DeleteCourse(int cid)
 197 |         {
 198 |             try
 199 |             {
 200 |                 int uid = CurrentUid();
 201 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 202 |                 LecturerRepository.DeleteCourse(uid, cid);
 203 |                 return new { success = true };
 204 |             }
 205 |             catch (Exception ex)
 206 |             {
 207 |                 return Fail("Request failed.");
 208 |             }
 209 |         }
 210 | 
 211 |         [WebMethod(EnableSession = true)]
 212 |         [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
 213 |         public static object GetLessonDetails(int schid)
 214 |         {
 215 |             try
 216 |             {
 217 |                 int uid = CurrentUid();
 218 |                 if (uid == 0) return AuthGate.NotAuthenticatedJson();
 219 | 
 220 |                 // Pure SQL: SubChapters (plural) + first StudyMat for type/content
 221 |                 var titleObj = DbHelper.ExecuteScalar(
 222 |                 "SELECT Title FROM SubChapters WHERE SchID = @SchID",
 223 |                 DbHelper.P("@SchID", schid));
 224 |                 if (titleObj == null || titleObj == System.DBNull.Value)
 225 |                 return Fail("Lesson not found.");
 226 | 
 227 |                 string title = titleObj.ToString();
 228 |                 string type = "Text";
 229 |                 string content = "";
 230 | 
 231 |                 var mats = DbHelper.ExecuteQuery(
 232 |                 "SELECT TOP 1 Type, TextContent, MediaLink FROM StudyMats WHERE SchID = @SchID ORDER BY [Index], SMID",
 233 |                 DbHelper.P("@SchID", schid));
 234 |                 if (mats.Rows.Count > 0)
 235 |                 {
 236 |                     type = DbHelper.SafeString(mats.Rows[0]["Type"]);
 237 |                     if (string.IsNullOrEmpty(type)) type = "Text";
 238 |                     content = !string.IsNullOrEmpty(DbHelper.SafeString(mats.Rows[0]["MediaLink"]))
 239 |                     ? DbHelper.SafeString(mats.Rows[0]["MediaLink"])
 240 |                     : DbHelper.SafeString(mats.Rows[0]["TextContent"]);
 241 |                 }
 242 | 
 243 |                 return new { success = true, title = title, type = type, content = content };
 244 |             }
 245 |             catch (Exception ex)
 246 |             {
 247 |                 return Fail("Request failed.");
 248 |             }
 249 |         }
 250 |     }
 251 | }
```
