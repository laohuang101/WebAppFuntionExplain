# Register.aspx.designer.cs
**Source:** `Pages/Authentication/Register.aspx.designer.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Two-step: form → Session pending → QR/MFA confirm → only then INSERT user.

## File overview

- **Total lines:** 26
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
`   3`  `    public partial class Register`
`   4`  `    {`
`   5`  `        protected global::System.Web.UI.HtmlControls.HtmlForm form1;`
`   6`  `        protected global::System.Web.UI.WebControls.Panel pnlForm;`
`   7`  `        protected global::System.Web.UI.WebControls.RadioButtonList rblRole;`
`   8`  `        protected global::System.Web.UI.WebControls.TextBox txtName;`
`   9`  `        protected global::System.Web.UI.WebControls.TextBox txtEmail;`
`  10`  `        protected global::System.Web.UI.WebControls.TextBox txtPassword;`
`  11`  `        protected global::System.Web.UI.WebControls.TextBox txtConfirm;`
`  12`  `        protected global::System.Web.UI.WebControls.Button btnRegister;`
`  13`  `        protected global::System.Web.UI.WebControls.Label lblError;`
`  14`  `        protected global::System.Web.UI.WebControls.Panel pnlMfaSetup;`
`  15`  `        protected global::System.Web.UI.WebControls.Image imgQr;`
`  16`  `        protected global::System.Web.UI.WebControls.Literal litMfaSecret;`
`  17`  `        protected global::System.Web.UI.WebControls.HiddenField hidMfaSecret;`
`  18`  `        protected global::System.Web.UI.WebControls.HiddenField hidMfaEmail;`
`  19`  `        protected global::System.Web.UI.WebControls.TextBox txtSetupCode;`
`  20`  `        protected global::System.Web.UI.WebControls.Button btnConfirmMfa;`
`  21`  `        protected global::System.Web.UI.WebControls.Label lblMfaError;`
`  22`  `        protected global::System.Web.UI.WebControls.LinkButton lnkCancelMfa;`
`  23`  `        protected global::System.Web.UI.WebControls.Panel pnlDone;`
`  24`  `        protected global::System.Web.UI.WebControls.Literal litDoneMsg;`
`  25`  `    }`
`  26`  `}`

## Source snapshot (raw)

```csharp
namespace WebAppAssignment.Pages.Authentication
{
    public partial class Register
    {
        protected global::System.Web.UI.HtmlControls.HtmlForm form1;
        protected global::System.Web.UI.WebControls.Panel pnlForm;
        protected global::System.Web.UI.WebControls.RadioButtonList rblRole;
        protected global::System.Web.UI.WebControls.TextBox txtName;
        protected global::System.Web.UI.WebControls.TextBox txtEmail;
        protected global::System.Web.UI.WebControls.TextBox txtPassword;
        protected global::System.Web.UI.WebControls.TextBox txtConfirm;
        protected global::System.Web.UI.WebControls.Button btnRegister;
        protected global::System.Web.UI.WebControls.Label lblError;
        protected global::System.Web.UI.WebControls.Panel pnlMfaSetup;
        protected global::System.Web.UI.WebControls.Image imgQr;
        protected global::System.Web.UI.WebControls.Literal litMfaSecret;
        protected global::System.Web.UI.WebControls.HiddenField hidMfaSecret;
        protected global::System.Web.UI.WebControls.HiddenField hidMfaEmail;
        protected global::System.Web.UI.WebControls.TextBox txtSetupCode;
        protected global::System.Web.UI.WebControls.Button btnConfirmMfa;
        protected global::System.Web.UI.WebControls.Label lblMfaError;
        protected global::System.Web.UI.WebControls.LinkButton lnkCancelMfa;
        protected global::System.Web.UI.WebControls.Panel pnlDone;
        protected global::System.Web.UI.WebControls.Literal litDoneMsg;
    }
}

```
