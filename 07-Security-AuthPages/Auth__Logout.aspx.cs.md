# Logout.aspx.cs
**Source:** `Pages/Authentication/Logout.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Clears session, abandons session, clears JWT auth cookie.

## File overview

- **Total lines:** 15
- **Kind:** `.cs`

## Variables / fields (file level)

_No classic field declarations detected (or mostly locals inside methods)._

## Functions / methods (1 found)

### `Page_Load` — lines 9–13

```
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`

#### Line-by-line (this function)

`   9`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  10`  `        {`
`  11`  `            AuthService.Logout(Context);`
`  12`  `            Response.Redirect("~/Pages/Landing/Landing.aspx", true);`
  - → Navigate browser to another URL.
`  13`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Web.UI;`
  - → Import namespace/types.
`   3`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`   4`  ``
`   5`  `namespace WebAppAssignment.Pages.Authentication`
  - → C# namespace grouping.
`   6`  `{`
`   7`  `    public partial class Logout : Page`
`   8`  `    {`
`   9`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  10`  `        {`
`  11`  `            AuthService.Logout(Context);`
`  12`  `            Response.Redirect("~/Pages/Landing/Landing.aspx", true);`
  - → Navigate browser to another URL.
`  13`  `        }`
`  14`  `    }`
`  15`  `}`

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
