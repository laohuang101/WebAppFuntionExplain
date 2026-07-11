# CourseCreation.aspx.cs
**Source:** `Pages/Lecturer/CourseCreation.aspx.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Create/edit courses, curriculum (chapters/lessons), media, publish/draft.

## File overview

- **Total lines:** 251
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 35:** `uid` — type `int`
- **Line 37:** `courses` — type `var`
- **Line 52:** `uid` — type `int`
- **Line 56:** `existing` — type `int?`
- **Line 58:** `newCid` — type `int`
- **Line 74:** `uid` — type `int`
- **Line 77:** `state` — type `bool`
- **Line 96:** `uid` — type `int`
- **Line 98:** `chapters` — type `var`
- **Line 113:** `uid` — type `int`
- **Line 118:** `existing` — type `int?`
- **Line 119:** `id` — type `int`
- **Line 134:** `uid` — type `int`
- **Line 151:** `uid` — type `int`
- **Line 157:** `body` — type `string`
- **Line 158:** `materialsJson` — type `string`
- **Line 160:** `idx` — type `int`
- **Line 166:** `existing` — type `int?`
- **Line 168:** `id` — type `int`
- **Line 183:** `uid` — type `int`
- **Line 200:** `uid` — type `int`
- **Line 217:** `uid` — type `int`
- **Line 221:** `titleObj` — type `var`
- **Line 226:** `title` — type `string`
- **Line 228:** `type` — type `string`
- **Line 229:** `content` — type `string`
- **Line 230:** `mats` — type `var`

## Functions / methods (13 found)

### `Page_Load` — lines 12–16

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`

#### Line-by-line (this function)

```csharp
  12 |         protected void Page_Load(object sender, EventArgs e)
  13 |         {
  14 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  15 |                 return;
  16 |         }
```

**Line notes**

- **L12:** Page load entry (GET or postback).
- **L14:** Authorization — block wrong role / anonymous.

---

### `CurrentUid` — lines 17–22

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
  20 |             // Lecturer or Admin only for course APIs
  21 |             return AuthGate.RequireLecturer();
  22 |         }
```

**Line notes**

- **L21:** Authorization — block wrong role / anonymous.

---

### `Fail` — lines 23–27

```csharp
private static object Fail(string message)
```

#### Explanation

- **Purpose:** Implements `Fail`.
- **Parameters:** `string message`

#### Line-by-line (this function)

```csharp
  23 | 
  24 |         private static object Fail(string message)
  25 |         {
  26 |             return new { success = false, message = message ?? "Request failed." };
  27 |         }
```

---

### `GetCoursesData` — lines 31–44

```csharp
public static object GetCoursesData()
```

#### Explanation

- **Purpose:** Implements `GetCoursesData`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`, `courses`

#### Line-by-line (this function)

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

**Line notes**

- **L33:** Error handling block.
- **L36:** Authorization — block wrong role / anonymous.
- **L40:** Handle/log exception.

---

### `SaveCourseInfo` — lines 48–66

```csharp
public static object SaveCourseInfo(string name, string desc, string category, string level, string bgImg, int cid)
```

#### Explanation

- **Purpose:** Implements `SaveCourseInfo`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `string name, string desc, string category, string level, string bgImg, int cid`
- **Local variables:** `uid`, `newCid`

#### Line-by-line (this function)

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

**Line notes**

- **L50:** Error handling block.
- **L54:** Authorization — block wrong role / anonymous.
- **L62:** Handle/log exception.

---

### `SetCoursePublished` — lines 70–88

```csharp
public static object SetCoursePublished(int cid, bool published)
```

#### Explanation

- **Purpose:** Implements `SetCoursePublished`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int cid, bool published`
- **Local variables:** `uid`, `state`

#### Line-by-line (this function)

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

**Line notes**

- **L72:** Error handling block.
- **L75:** Authorization — block wrong role / anonymous.
- **L80:** Handle/log exception.
- **L82:** Authorization — block wrong role / anonymous.
- **L84:** Handle/log exception.

---

### `GetCourseCurriculum` — lines 92–105

```csharp
public static object GetCourseCurriculum(int cid)
```

#### Explanation

- **Purpose:** Implements `GetCourseCurriculum`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Parameters:** `int cid`
- **Local variables:** `uid`, `chapters`

#### Line-by-line (this function)

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

**Line notes**

- **L94:** Error handling block.
- **L97:** Authorization — block wrong role / anonymous.
- **L101:** Handle/log exception.

---

### `SaveChapter` — lines 109–126

```csharp
public static object SaveChapter(int chid, int cid, string title)
```

#### Explanation

- **Purpose:** Implements `SaveChapter`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int chid, int cid, string title`
- **Local variables:** `uid`, `id`

#### Line-by-line (this function)

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

**Line notes**

- **L111:** Error handling block.
- **L114:** Authorization — block wrong role / anonymous.
- **L122:** Handle/log exception.

---

### `DeleteChapter` — lines 130–143

```csharp
public static object DeleteChapter(int chid)
```

#### Explanation

- **Purpose:** Implements `DeleteChapter`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Delete/clear data.
- **Parameters:** `int chid`
- **Local variables:** `uid`

#### Line-by-line (this function)

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

**Line notes**

- **L132:** Error handling block.
- **L135:** Authorization — block wrong role / anonymous.
- **L139:** Handle/log exception.

---

### `SaveSubChapter` — lines 147–175

```csharp
public static object SaveSubChapter(int schid, int chid, string title, string type, string content)
```

#### Explanation

- **Purpose:** Implements `SaveSubChapter`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int schid, int chid, string title, string type, string content`
- **Local variables:** `uid`, `body`, `materialsJson`, `sep`, `idx`, `id`

#### Line-by-line (this function)

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

**Line notes**

- **L149:** Error handling block.
- **L152:** Authorization — block wrong role / anonymous.
- **L171:** Handle/log exception.

---

### `DeleteSubChapter` — lines 179–192

```csharp
public static object DeleteSubChapter(int schid)
```

#### Explanation

- **Purpose:** Implements `DeleteSubChapter`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Delete/clear data.
- **Parameters:** `int schid`
- **Local variables:** `uid`

#### Line-by-line (this function)

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

**Line notes**

- **L181:** Error handling block.
- **L184:** Authorization — block wrong role / anonymous.
- **L188:** Handle/log exception.

---

### `DeleteCourse` — lines 196–209

```csharp
public static object DeleteCourse(int cid)
```

#### Explanation

- **Purpose:** Implements `DeleteCourse`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Delete/clear data.
- **Parameters:** `int cid`
- **Local variables:** `uid`

#### Line-by-line (this function)

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

**Line notes**

- **L198:** Error handling block.
- **L201:** Authorization — block wrong role / anonymous.
- **L205:** Handle/log exception.

---

### `GetLessonDetails` — lines 213–249

```csharp
public static object GetLessonDetails(int schid)
```

#### Explanation

- **Purpose:** Implements `GetLessonDetails`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Parameters:** `int schid`
- **Local variables:** `uid`, `titleObj`, `title`, `type`, `content`, `mats`

#### Line-by-line (this function)

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

**Line notes**

- **L215:** Error handling block.
- **L218:** Authorization — block wrong role / anonymous.
- **L221:** Database access (pure SQL).
- **L223:** Database access (pure SQL).
- **L224:** Null-safe read from database values.
- **L231:** Database access (pure SQL).
- **L233:** Database access (pure SQL).
- **L236:** Database access (pure SQL).
- **L238:** Database access (pure SQL).
- **L239:** Database access (pure SQL).
- **L240:** Database access (pure SQL).
- **L245:** Handle/log exception.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L8:** C# namespace grouping.
- **L12:** Page load entry (GET or postback).
- **L14:** Authorization — block wrong role / anonymous.
- **L21:** Authorization — block wrong role / anonymous.
- **L29:** Expose method to AJAX JSON calls.
- **L33:** Error handling block.
- **L36:** Authorization — block wrong role / anonymous.
- **L40:** Handle/log exception.
- **L46:** Expose method to AJAX JSON calls.
- **L50:** Error handling block.
- **L54:** Authorization — block wrong role / anonymous.
- **L62:** Handle/log exception.
- **L68:** Expose method to AJAX JSON calls.
- **L72:** Error handling block.
- **L75:** Authorization — block wrong role / anonymous.
- **L80:** Handle/log exception.
- **L82:** Authorization — block wrong role / anonymous.
- **L84:** Handle/log exception.
- **L90:** Expose method to AJAX JSON calls.
- **L94:** Error handling block.
- **L97:** Authorization — block wrong role / anonymous.
- **L101:** Handle/log exception.
- **L107:** Expose method to AJAX JSON calls.
- **L111:** Error handling block.
- **L114:** Authorization — block wrong role / anonymous.
- **L122:** Handle/log exception.
- **L128:** Expose method to AJAX JSON calls.
- **L132:** Error handling block.
- **L135:** Authorization — block wrong role / anonymous.
- **L139:** Handle/log exception.
- **L145:** Expose method to AJAX JSON calls.
- **L149:** Error handling block.
- **L152:** Authorization — block wrong role / anonymous.
- **L171:** Handle/log exception.
- **L177:** Expose method to AJAX JSON calls.
- **L181:** Error handling block.
- **L184:** Authorization — block wrong role / anonymous.
- **L188:** Handle/log exception.
- **L194:** Expose method to AJAX JSON calls.
- **L198:** Error handling block.
- **L201:** Authorization — block wrong role / anonymous.
- **L205:** Handle/log exception.
- **L211:** Expose method to AJAX JSON calls.
- **L215:** Error handling block.
- **L218:** Authorization — block wrong role / anonymous.
- **L221:** Database access (pure SQL).
- **L223:** Database access (pure SQL).
- **L224:** Null-safe read from database values.
- **L231:** Database access (pure SQL).
- **L233:** Database access (pure SQL).
- **L236:** Database access (pure SQL).
- **L238:** Database access (pure SQL).
- **L239:** Database access (pure SQL).
- **L240:** Database access (pure SQL).
- **L245:** Handle/log exception.

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
    public partial class Course_Creation : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
                return;
        }

        private static int CurrentUid()
        {
            // Lecturer or Admin only for course APIs
            return AuthGate.RequireLecturer();
        }

        private static object Fail(string message)
        {
            return new { success = false, message = message ?? "Request failed." };
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetCoursesData()
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                var courses = LecturerRepository.GetCoursesForLecturer(uid);
                return new { success = true, courses = courses };
            }
            catch
            {
                return Fail("Could not load courses.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object SaveCourseInfo(string name, string desc, string category, string level, string bgImg, int cid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0)
                    return AuthGate.NotAuthenticatedJson("Lecturer sign-in required. Please log out and log in again.");
                if (string.IsNullOrWhiteSpace(name)) return Fail("Course title is required.");

                int? existing = cid > 0 ? cid : (int?)null;
                int newCid = LecturerRepository.SaveCourse(
                    uid, existing, name.Trim(), desc ?? "", bgImg, category ?? "", level ?? "");
                return new { success = true, cid = newCid };
            }
            catch
            {
                return Fail("Could not save course.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object SetCoursePublished(int cid, bool published)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                if (cid <= 0) return Fail("Invalid course.");
                bool state = LecturerRepository.SetCoursePublished(uid, cid, published);
                return new { success = true, isPublished = state, status = state ? "Published" : "Draft" };
            }
            catch (UnauthorizedAccessException)
            {
                return AuthGate.ForbiddenJson();
            }
            catch
            {
                return Fail("Could not update publish state.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetCourseCurriculum(int cid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                var chapters = LecturerRepository.GetCurriculum(uid, cid);
                return new { success = true, chapters = chapters };
            }
            catch (Exception ex)
            {
                return Fail("Request failed.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object SaveChapter(int chid, int cid, string title)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                if (string.IsNullOrWhiteSpace(title)) return Fail("Section title is required.");
                if (cid <= 0) return Fail("Invalid course id.");
                // chid == 0 means create new section
                int? existing = chid > 0 ? chid : (int?)null;
                int id = LecturerRepository.SaveChapter(uid, existing, cid, title.Trim());
                return new { success = true, chid = id };
            }
            catch (Exception ex)
            {
                return Fail("Request failed.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object DeleteChapter(int chid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                LecturerRepository.DeleteChapter(uid, chid);
                return new { success = true };
            }
            catch (Exception ex)
            {
                return Fail("Request failed.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object SaveSubChapter(int schid, int chid, string title, string type, string content)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                if (string.IsNullOrWhiteSpace(title)) return Fail("Lesson title is required.");
                if (chid <= 0) return Fail("Invalid section id.");

                // Materials may be appended after separator from client
                string body = content ?? "";
                string materialsJson = null;
                const string sep = "\n--MATERIALS--\n";
                int idx = body.IndexOf(sep, StringComparison.Ordinal);
                if (idx >= 0)
                {
                    materialsJson = body.Substring(idx + sep.Length);
                    body = body.Substring(0, idx);
                }

                int? existing = schid > 0 ? schid : (int?)null;
                int id = LecturerRepository.SaveSubChapter(uid, existing, chid, title.Trim(), type, body, materialsJson);
                return new { success = true, schid = id };
            }
            catch (Exception ex)
            {
                return Fail("Request failed.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object DeleteSubChapter(int schid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                LecturerRepository.DeleteSubChapter(uid, schid);
                return new { success = true };
            }
            catch (Exception ex)
            {
                return Fail("Request failed.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object DeleteCourse(int cid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                LecturerRepository.DeleteCourse(uid, cid);
                return new { success = true };
            }
            catch (Exception ex)
            {
                return Fail("Request failed.");
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetLessonDetails(int schid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();

                // Pure SQL: SubChapters (plural) + first StudyMat for type/content
                var titleObj = DbHelper.ExecuteScalar(
                "SELECT Title FROM SubChapters WHERE SchID = @SchID",
                DbHelper.P("@SchID", schid));
                if (titleObj == null || titleObj == System.DBNull.Value)
                return Fail("Lesson not found.");

                string title = titleObj.ToString();
                string type = "Text";
                string content = "";

                var mats = DbHelper.ExecuteQuery(
                "SELECT TOP 1 Type, TextContent, MediaLink FROM StudyMats WHERE SchID = @SchID ORDER BY [Index], SMID",
                DbHelper.P("@SchID", schid));
                if (mats.Rows.Count > 0)
                {
                    type = DbHelper.SafeString(mats.Rows[0]["Type"]);
                    if (string.IsNullOrEmpty(type)) type = "Text";
                    content = !string.IsNullOrEmpty(DbHelper.SafeString(mats.Rows[0]["MediaLink"]))
                    ? DbHelper.SafeString(mats.Rows[0]["MediaLink"])
                    : DbHelper.SafeString(mats.Rows[0]["TextContent"]);
                }

                return new { success = true, title = title, type = type, content = content };
            }
            catch (Exception ex)
            {
                return Fail("Request failed.");
            }
        }
    }
}

```
