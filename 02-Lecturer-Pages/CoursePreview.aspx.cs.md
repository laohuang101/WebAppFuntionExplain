# CoursePreview.aspx.cs
**Source:** `Pages/Lecturer/CoursePreview.aspx.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 21
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

_No classic field declarations detected (or mostly locals inside methods — see each function’s **Local variables** section)._

## Functions / methods (1 found)

### `Page_Load` — lines 9–19

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **ASP.NET WebMethod:** Called from browser JS via `Page.aspx/MethodName` POST JSON.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

```csharp
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  12 |                 return;
  13 | // Preview data is loaded client-side via CourseCreation WebMethods
  14 |             // (same pure-SQL endpoints) using ?cid=
  15 |             if (string.IsNullOrWhiteSpace(Request.QueryString["cid"]))
  16 |             {
  17 |                 Response.Redirect("~/Pages/Lecturer/CourseCreation.aspx");
  18 |             }
  19 |         }
```

**Line notes** (what code + variables mean)

- **L9:** Page load entry (GET or postback).
- **L11:** Authorization — block wrong role / anonymous.
- **L17:** Navigate browser to another URL.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```csharp
   1 | using System;
   2 | using System.Web.UI;
   3 | using WebAppAssignment.Data.Security;
   4 | 
   5 | namespace WebAppAssignment.Pages.Lecturer
   6 | {
   7 |     public partial class CoursePreview : Page
   8 |     {
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
  12 |                 return;
  13 | // Preview data is loaded client-side via CourseCreation WebMethods
  14 |             // (same pure-SQL endpoints) using ?cid=
  15 |             if (string.IsNullOrWhiteSpace(Request.QueryString["cid"]))
  16 |             {
  17 |                 Response.Redirect("~/Pages/Lecturer/CourseCreation.aspx");
  18 |             }
  19 |         }
  20 |     }
  21 | }
```

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L9:** Page load entry (GET or postback).
- **L11:** Authorization — block wrong role / anonymous.
- **L17:** Navigate browser to another URL.

## Source snapshot (raw)

```csharp
using System;
using System.Web.UI;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Lecturer
{
    public partial class CoursePreview : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))
                return;
// Preview data is loaded client-side via CourseCreation WebMethods
            // (same pure-SQL endpoints) using ?cid=
            if (string.IsNullOrWhiteSpace(Request.QueryString["cid"]))
            {
                Response.Redirect("~/Pages/Lecturer/CourseCreation.aspx");
            }
        }
    }
}

```
