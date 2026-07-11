# Assignments.aspx.cs
**Source:** `Pages/Lecturer/Assignments.aspx.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 113
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 29:** `uid` — type `int`
- **Line 45:** `uid` — type `int`
- **Line 75:** `uid` — type `int`
- **Line 83:** `id` — type `int`
- **Line 102:** `uid` — type `int`

## Functions / methods (6 found)

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
  16 | }
```

**Line notes**

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

**Line notes**

- **L20:** Authorization — block wrong role / anonymous.

---

### `GetCourses` — lines 25–37

```csharp
public static object GetCourses()
```

#### Explanation

- **Purpose:** Implements `GetCourses`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`

#### Line-by-line (this function)

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

**Line notes**

- **L27:** Error handling block.
- **L30:** Authorization — block wrong role / anonymous.
- **L33:** Handle/log exception.

---

### `GetCourseWorks` — lines 41–53

```csharp
public static object GetCourseWorks()
```

#### Explanation

- **Purpose:** Implements `GetCourseWorks`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`

#### Line-by-line (this function)

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

**Line notes**

- **L43:** Error handling block.
- **L46:** Authorization — block wrong role / anonymous.
- **L49:** Handle/log exception.

---

### `SaveCourseWork` — lines 61–94

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

#### Explanation

- **Purpose:** Implements `SaveCourseWork`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int? cwid,
        int cid,
        string title,
        string instructions,
        string type,
        decimal score,
        decimal creditGiven,
        string rubricJson,
        string extraMetaJson,
        string objectiveQuestio`
- **Local variables:** `uid`, `id`

#### Line-by-line (this function)

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

**Line notes**

- **L73:** Error handling block.
- **L76:** Authorization — block wrong role / anonymous.
- **L90:** Handle/log exception.

---

### `DeleteCourseWork` — lines 98–111

```csharp
public static object DeleteCourseWork(int cwid)
```

#### Explanation

- **Purpose:** Implements `DeleteCourseWork`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Delete/clear data.
- **Parameters:** `int cwid`
- **Local variables:** `uid`

#### Line-by-line (this function)

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

**Line notes**

- **L100:** Error handling block.
- **L103:** Authorization — block wrong role / anonymous.
- **L107:** Handle/log exception.

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
- **L20:** Authorization — block wrong role / anonymous.
- **L23:** Expose method to AJAX JSON calls.
- **L27:** Error handling block.
- **L30:** Authorization — block wrong role / anonymous.
- **L33:** Handle/log exception.
- **L39:** Expose method to AJAX JSON calls.
- **L43:** Error handling block.
- **L46:** Authorization — block wrong role / anonymous.
- **L49:** Handle/log exception.
- **L59:** Expose method to AJAX JSON calls.
- **L73:** Error handling block.
- **L76:** Authorization — block wrong role / anonymous.
- **L90:** Handle/log exception.
- **L96:** Expose method to AJAX JSON calls.
- **L100:** Error handling block.
- **L103:** Authorization — block wrong role / anonymous.
- **L107:** Handle/log exception.

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
    public partial class Assignments : Page
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
        public static object GetCourses()
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                return new { success = true, courses = LecturerRepository.GetLecturerCoursesSimple(uid) };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetCourseWorks()
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                return new { success = true, items = LecturerRepository.GetCourseWorksForLecturer(uid) };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }

        /// <summary>
        /// Saves into CourseWorks (CWID, ChID, Title, Description, DueDate)
        /// and optionally ObjectiveQuestions (QID, QuestionText, OptionA-D, CorrectAnswer).
        /// </summary>
        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
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
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                if (cid <= 0) return new { success = false, message = "Select a target course." };
                if (string.IsNullOrWhiteSpace(title)) return new { success = false, message = "Title is required." };

                // All assessments are graded out of 100 pts
                score = 100m;
                creditGiven = 100m;

                int id = LecturerRepository.SaveCourseWork(
                uid, cwid, cid, title.Trim(), instructions, type,
                score, creditGiven, rubricJson, extraMetaJson, objectiveQuestionsJson);

                return new { success = true, cwid = id };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object DeleteCourseWork(int cwid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                LecturerRepository.DeleteCourseWork(uid, cwid);
                return new { success = true };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }
    }
}

```
