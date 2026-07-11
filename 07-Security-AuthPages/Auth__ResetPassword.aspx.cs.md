# ResetPassword.aspx.cs
**Source:** `Pages/Authentication/ResetPassword.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

One-shot TOTP + new password form (uses AuthService.ResetPasswordWithTotp).

## File overview

- **Total lines:** 44
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 15:** `email` — type `string`
- **Line 24:** `p1` — type `string`
- **Line 25:** `p2` — type `string`
- **Line 31:** `result` — type `var`

## Functions / methods (2 found)

### `Page_Load` — lines 9–19

```
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`
- **Local variables:** `email`

#### Line-by-line (this function)

`   9`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  10`  `        {`
`  11`  `            AuthSchema.Ensure();`
`  12`  `            CsrfProtection.EnsureToken(Context);`
  - → CSRF anti-forgery protection.
`  13`  `            if (!IsPostBack)`
  - → False on first open; true after postback.
`  14`  `            {`
`  15`  `                string email = Request.QueryString["email"];`
`  16`  `                if (!string.IsNullOrEmpty(email))`
`  17`  `                    txtEmail.Text = email.Trim();`
`  18`  `            }`
`  19`  `        }`

---

### `btnReset_Click` — lines 20–42

```
protected void btnReset_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnReset_Click`.
- **Navigation:** Redirects the browser.
- **Parameters:** `object sender, EventArgs e`
- **Local variables:** `p1`, `p2`, `result`

#### Line-by-line (this function)

`  20`  ``
`  21`  `        protected void btnReset_Click(object sender, EventArgs e)`
`  22`  `        {`
`  23`  `            lblMsg.CssClass = "d-block mt-3 text-center small text-danger";`
`  24`  `            string p1 = txtPassword.Text ?? "";`
`  25`  `            string p2 = txtPassword2.Text ?? "";`
`  26`  `            if (p1 != p2)`
`  27`  `            {`
`  28`  `                lblMsg.Text = "Passwords do not match.";`
`  29`  `                return;`
`  30`  `            }`
`  31`  ``
`  32`  `            var result = AuthService.ResetPasswordWithTotp(txtEmail.Text, txtCode.Text, p1);`
`  33`  `            if (!result.Success)`
`  34`  `            {`
`  35`  `                lblMsg.Text = result.Message ?? "Could not reset password.";`
`  36`  `                return;`
`  37`  `            }`
`  38`  ``
`  39`  `            lblMsg.CssClass = "d-block mt-3 text-center small text-success";`
`  40`  `            lblMsg.Text = result.Message + " Redirecting to login…";`
`  41`  `            Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));`
`  42`  `        }`

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
`   7`  `    public partial class ResetPassword : Page`
`   8`  `    {`
`   9`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  10`  `        {`
`  11`  `            AuthSchema.Ensure();`
`  12`  `            CsrfProtection.EnsureToken(Context);`
  - → CSRF anti-forgery protection.
`  13`  `            if (!IsPostBack)`
  - → False on first open; true after postback.
`  14`  `            {`
`  15`  `                string email = Request.QueryString["email"];`
`  16`  `                if (!string.IsNullOrEmpty(email))`
`  17`  `                    txtEmail.Text = email.Trim();`
`  18`  `            }`
`  19`  `        }`
`  20`  ``
`  21`  `        protected void btnReset_Click(object sender, EventArgs e)`
`  22`  `        {`
`  23`  `            lblMsg.CssClass = "d-block mt-3 text-center small text-danger";`
`  24`  `            string p1 = txtPassword.Text ?? "";`
`  25`  `            string p2 = txtPassword2.Text ?? "";`
`  26`  `            if (p1 != p2)`
`  27`  `            {`
`  28`  `                lblMsg.Text = "Passwords do not match.";`
`  29`  `                return;`
`  30`  `            }`
`  31`  ``
`  32`  `            var result = AuthService.ResetPasswordWithTotp(txtEmail.Text, txtCode.Text, p1);`
`  33`  `            if (!result.Success)`
`  34`  `            {`
`  35`  `                lblMsg.Text = result.Message ?? "Could not reset password.";`
`  36`  `                return;`
`  37`  `            }`
`  38`  ``
`  39`  `            lblMsg.CssClass = "d-block mt-3 text-center small text-success";`
`  40`  `            lblMsg.Text = result.Message + " Redirecting to login…";`
`  41`  `            Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));`
`  42`  `        }`
`  43`  `    }`
`  44`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.Web.UI;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Authentication
{
    public partial class ResetPassword : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            AuthSchema.Ensure();
            CsrfProtection.EnsureToken(Context);
            if (!IsPostBack)
            {
                string email = Request.QueryString["email"];
                if (!string.IsNullOrEmpty(email))
                    txtEmail.Text = email.Trim();
            }
        }

        protected void btnReset_Click(object sender, EventArgs e)
        {
            lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
            string p1 = txtPassword.Text ?? "";
            string p2 = txtPassword2.Text ?? "";
            if (p1 != p2)
            {
                lblMsg.Text = "Passwords do not match.";
                return;
            }

            var result = AuthService.ResetPasswordWithTotp(txtEmail.Text, txtCode.Text, p1);
            if (!result.Success)
            {
                lblMsg.Text = result.Message ?? "Could not reset password.";
                return;
            }

            lblMsg.CssClass = "d-block mt-3 text-center small text-success";
            lblMsg.Text = result.Message + " Redirecting to login…";
            Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));
        }
    }
}

```
