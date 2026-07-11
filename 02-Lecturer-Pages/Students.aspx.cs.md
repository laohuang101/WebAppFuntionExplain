# Students.aspx.cs
**Source:** `Pages/Lecturer/Students.aspx.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Enrolled students per course with progress counts.

## File overview

- **Total lines:** 58
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 29:** `uid` — type `int`
- **Line 31:** `list` — type `var`
- **Line 46:** `uid` — type `int`
- **Line 48:** `detail` — type `var`

## Functions / methods (4 found)

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

### `GetStudents` — lines 25–38

```csharp
public static object GetStudents(string search)
```

#### Explanation

- **Purpose:** Implements `GetStudents`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Parameters:** `string search`
- **Local variables:** `uid`, `list`

#### Line-by-line (this function)

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

**Line notes**

- **L27:** Error handling block.
- **L30:** Authorization — block wrong role / anonymous.
- **L34:** Handle/log exception.

---

### `GetStudentDetail` — lines 42–56

```csharp
public static object GetStudentDetail(int studentUid, int cid)
```

#### Explanation

- **Purpose:** Implements `GetStudentDetail`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Parameters:** `int studentUid, int cid`
- **Local variables:** `uid`, `detail`

#### Line-by-line (this function)

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

**Line notes**

- **L44:** Error handling block.
- **L47:** Authorization — block wrong role / anonymous.
- **L52:** Handle/log exception.

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
- **L34:** Handle/log exception.
- **L40:** Expose method to AJAX JSON calls.
- **L44:** Error handling block.
- **L47:** Authorization — block wrong role / anonymous.
- **L52:** Handle/log exception.

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
    public partial class Students : Page
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
        public static object GetStudents(string search)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                var list = LecturerRepository.GetStudentPerformance(uid, search);
                return new { success = true, students = list };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object GetStudentDetail(int studentUid, int cid)
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                var detail = LecturerRepository.GetStudentDetail(uid, studentUid, cid);
                if (detail == null) return new { success = false, message = "Student not found." };
                return new { success = true, detail = detail };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }
    }
}

```
