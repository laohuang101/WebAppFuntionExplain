# Grading.aspx.cs
**Source:** `Pages/Lecturer/Grading.aspx.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

List submissions for lecturer courses; assign marks and feedback; CSV export.

## File overview

- **Total lines:** 114
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 29:** `uid` — type `int`
- **Line 31:** `list` — type `var`
- **Line 32:** `graded` — type `int`
- **Line 57:** `uid` — type `int`
- **Line 62:** `ctx` — type `var`
- **Line 84:** `uid` — type `int`
- **Line 86:** `csv` — type `string`
- **Line 87:** `name` — type `string`
- **Line 104:** `uid` — type `int`

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

### `GetSubmissions` — lines 25–49

```csharp
public static object GetSubmissions()
```

#### Explanation

- **Purpose:** Implements `GetSubmissions`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`, `list`, `graded`

#### Line-by-line (this function)

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

**Line notes**

- **L27:** Error handling block.
- **L30:** Authorization — block wrong role / anonymous.
- **L45:** Handle/log exception.

---

### `SaveGrade` — lines 53–76

```csharp
public static object SaveGrade(int sid, decimal score, string review)
```

#### Explanation

- **Purpose:** Implements `SaveGrade`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Session:** Reads/writes ASP.NET Session.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int sid, decimal score, string review`
- **Local variables:** `uid`, `ctx`

#### Line-by-line (this function)

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

**Line notes**

- **L55:** Error handling block.
- **L58:** Authorization — block wrong role / anonymous.
- **L60:** Error handling block.
- **L69:** Handle/log exception.
- **L72:** Handle/log exception.

---

### `ExportGradesCsv` — lines 80–96

```csharp
public static object ExportGradesCsv(int cid)
```

#### Explanation

- **Purpose:** Implements `ExportGradesCsv`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `int cid`
- **Local variables:** `uid`, `csv`, `name`

#### Line-by-line (this function)

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

**Line notes**

- **L80:** CSV export.
- **L82:** Error handling block.
- **L85:** Authorization — block wrong role / anonymous.
- **L86:** CSV export.
- **L88:** CSV export.
- **L89:** CSV export.
- **L90:** CSV export.
- **L92:** Handle/log exception.

---

### `GetPendingCount` — lines 100–112

```csharp
public static object GetPendingCount()
```

#### Explanation

- **Purpose:** Implements `GetPendingCount`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.
- **Local variables:** `uid`

#### Line-by-line (this function)

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

**Line notes**

- **L102:** Error handling block.
- **L105:** Authorization — block wrong role / anonymous.
- **L108:** Handle/log exception.

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
- **L45:** Handle/log exception.
- **L51:** Expose method to AJAX JSON calls.
- **L55:** Error handling block.
- **L58:** Authorization — block wrong role / anonymous.
- **L60:** Error handling block.
- **L69:** Handle/log exception.
- **L72:** Handle/log exception.
- **L78:** Expose method to AJAX JSON calls.
- **L80:** CSV export.
- **L82:** Error handling block.
- **L85:** Authorization — block wrong role / anonymous.
- **L86:** CSV export.
- **L88:** CSV export.
- **L89:** CSV export.
- **L90:** CSV export.
- **L92:** Handle/log exception.
- **L98:** Expose method to AJAX JSON calls.
- **L102:** Error handling block.
- **L105:** Authorization — block wrong role / anonymous.
- **L108:** Handle/log exception.

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
    public partial class Grading : Page
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
        public static object GetSubmissions()
        {
            try
            {
                int uid = CurrentUid();
                if (uid == 0) return AuthGate.NotAuthenticatedJson();
                var list = LecturerRepository.GetRecentSubmissions(uid, 200);
                int graded = 0;
                foreach (var s in list)
                {
                    if (s.ContainsKey("isGraded") && Convert.ToBoolean(s["isGraded"])) graded++;
                }
                return new
                {
                    success = true,
                    submissions = list,
                    gradedCount = graded,
                    totalCount = list.Count
                };
            }
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
            }
        }

        [WebMethod(EnableSession = true)]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static object SaveGrade(int sid, decimal score, string review)
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
            catch (Exception ex)
            {
                return new { success = false, message = "Request failed." };
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
                string name = cid > 0
                    ? "grades-course-" + cid + ".csv"
                    : "grades-all.csv";
                return new { success = true, csv = csv, fileName = name };
            }
            catch
            {
                return new { success = false, message = "Could not export grades." };
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
    }
}

```
