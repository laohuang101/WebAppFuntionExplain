# CoursePreview.aspx.cs
**Source:** `Pages/Lecturer/CoursePreview.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 21
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (1 found)

### `Page_Load` — lines 9–19

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. Check the visitor is logged in with an allowed role; if not, redirect to login and stop.
2. Redirect the browser to another page.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
