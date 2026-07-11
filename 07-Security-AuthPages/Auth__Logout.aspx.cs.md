# Logout.aspx.cs
**Source:** `Pages/Authentication/Logout.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Clears session, abandons session, clears JWT auth cookie.

## File overview

- **Total lines:** 15
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (1 found)

### `Page_Load` — lines 9–13

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
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             AuthService.Logout(Context);
  12 |             Response.Redirect("~/Pages/Landing/Landing.aspx", true);
  13 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Web.UI;
   3 | using WebAppAssignment.Data.Security;
   4 | 
   5 | namespace WebAppAssignment.Pages.Authentication
   6 | {
   7 |     public partial class Logout : Page
   8 |     {
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             AuthService.Logout(Context);
  12 |             Response.Redirect("~/Pages/Landing/Landing.aspx", true);
  13 |         }
  14 |     }
  15 | }
```
