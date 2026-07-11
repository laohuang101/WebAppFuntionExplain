# ResetPassword.aspx.designer.cs
**Source:** `Pages/Authentication/ResetPassword.aspx.designer.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

One-shot TOTP + new password form (uses AuthService.ResetPasswordWithTotp).

## File overview

- **Total lines:** 13
- **Kind:** `.cs`

## Variables / fields (file level)

_No classic field declarations detected (or mostly locals inside methods)._

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `namespace WebAppAssignment.Pages.Authentication`
  - → C# namespace grouping.
`   2`  `{`
`   3`  `    public partial class ResetPassword`
`   4`  `    {`
`   5`  `        protected global::System.Web.UI.HtmlControls.HtmlForm form1;`
`   6`  `        protected global::System.Web.UI.WebControls.TextBox txtEmail;`
`   7`  `        protected global::System.Web.UI.WebControls.TextBox txtCode;`
`   8`  `        protected global::System.Web.UI.WebControls.TextBox txtPassword;`
`   9`  `        protected global::System.Web.UI.WebControls.TextBox txtPassword2;`
`  10`  `        protected global::System.Web.UI.WebControls.Button btnReset;`
`  11`  `        protected global::System.Web.UI.WebControls.Label lblMsg;`
`  12`  `    }`
`  13`  `}`

## Source snapshot (raw)

```csharp
namespace WebAppAssignment.Pages.Authentication
{
    public partial class ResetPassword
    {
        protected global::System.Web.UI.HtmlControls.HtmlForm form1;
        protected global::System.Web.UI.WebControls.TextBox txtEmail;
        protected global::System.Web.UI.WebControls.TextBox txtCode;
        protected global::System.Web.UI.WebControls.TextBox txtPassword;
        protected global::System.Web.UI.WebControls.TextBox txtPassword2;
        protected global::System.Web.UI.WebControls.Button btnReset;
        protected global::System.Web.UI.WebControls.Label lblMsg;
    }
}

```
