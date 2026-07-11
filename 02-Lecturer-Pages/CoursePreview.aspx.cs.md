# CoursePreview.aspx.cs
**Source:** `Pages/Lecturer/CoursePreview.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 21
- **Kind:** `.cs`

## Variables / fields (file level)

_No classic field declarations detected (or mostly locals inside methods)._

## Functions / methods (1 found)

### `Page_Load` — lines 9–19

```
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **ASP.NET WebMethod:** Called from browser JS via `Page.aspx/MethodName` POST JSON.
- **Security:** Uses AuthGate — requires logged-in role.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`

#### Line-by-line (this function)

`   9`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  10`  `        {`
`  11`  `            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  12`  `                return;`
`  13`  `// Preview data is loaded client-side via CourseCreation WebMethods`
`  14`  `            // (same pure-SQL endpoints) using ?cid=`
`  15`  `            if (string.IsNullOrWhiteSpace(Request.QueryString["cid"]))`
`  16`  `            {`
`  17`  `                Response.Redirect("~/Pages/Lecturer/CourseCreation.aspx");`
  - → Navigate browser to another URL.
`  18`  `            }`
`  19`  `        }`

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
`   5`  `namespace WebAppAssignment.Pages.Lecturer`
  - → C# namespace grouping.
`   6`  `{`
`   7`  `    public partial class CoursePreview : Page`
`   8`  `    {`
`   9`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  10`  `        {`
`  11`  `            if (!AuthGate.EnsurePage(this, "Lecturer", "Admin"))`
  - → Authorization — block wrong role / anonymous.
`  12`  `                return;`
`  13`  `// Preview data is loaded client-side via CourseCreation WebMethods`
`  14`  `            // (same pure-SQL endpoints) using ?cid=`
`  15`  `            if (string.IsNullOrWhiteSpace(Request.QueryString["cid"]))`
`  16`  `            {`
`  17`  `                Response.Redirect("~/Pages/Lecturer/CourseCreation.aspx");`
  - → Navigate browser to another URL.
`  18`  `            }`
`  19`  `        }`
`  20`  `    }`
`  21`  `}`

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
