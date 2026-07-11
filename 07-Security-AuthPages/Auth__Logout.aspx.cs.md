# Logout.aspx.cs
**Source:** `Pages/Authentication/Logout.aspx.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Clears session, abandons session, clears JWT auth cookie.

## File overview

- **Total lines:** 15
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

_No classic field declarations detected (or mostly locals inside methods — see each function’s **Local variables** section)._

## Functions / methods (1 found)

### `Page_Load` — lines 9–13

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

```csharp
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             AuthService.Logout(Context);
  12 |             Response.Redirect("~/Pages/Landing/Landing.aspx", true);
  13 |         }
```

**Line notes** (what code + variables mean)

- **L9:** Page load entry (GET or postback).
- **L12:** Navigate browser to another URL.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L9:** Page load entry (GET or postback).
- **L12:** Navigate browser to another URL.

## Source snapshot (raw)

```csharp
using System;
using System.Web.UI;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Authentication
{
    public partial class Logout : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            AuthService.Logout(Context);
            Response.Redirect("~/Pages/Landing/Landing.aspx", true);
        }
    }
}

```
