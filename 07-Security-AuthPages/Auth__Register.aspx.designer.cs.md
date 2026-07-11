# Register.aspx.designer.cs
**Source:** `Pages/Authentication/Register.aspx.designer.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Two-step: form → Session pending → QR/MFA confirm → only then INSERT user.

## File overview

- **Total lines:** 26
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

_No classic field declarations detected (or mostly locals inside methods — see each function’s **Local variables** section)._

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

```csharp
   1 | namespace WebAppAssignment.Pages.Authentication
   2 | {
   3 |     public partial class Register
   4 |     {
   5 |         protected global::System.Web.UI.HtmlControls.HtmlForm form1;
   6 |         protected global::System.Web.UI.WebControls.Panel pnlForm;
   7 |         protected global::System.Web.UI.WebControls.RadioButtonList rblRole;
   8 |         protected global::System.Web.UI.WebControls.TextBox txtName;
   9 |         protected global::System.Web.UI.WebControls.TextBox txtEmail;
  10 |         protected global::System.Web.UI.WebControls.TextBox txtPassword;
  11 |         protected global::System.Web.UI.WebControls.TextBox txtConfirm;
  12 |         protected global::System.Web.UI.WebControls.Button btnRegister;
  13 |         protected global::System.Web.UI.WebControls.Label lblError;
  14 |         protected global::System.Web.UI.WebControls.Panel pnlMfaSetup;
  15 |         protected global::System.Web.UI.WebControls.Image imgQr;
  16 |         protected global::System.Web.UI.WebControls.Literal litMfaSecret;
  17 |         protected global::System.Web.UI.WebControls.HiddenField hidMfaSecret;
  18 |         protected global::System.Web.UI.WebControls.HiddenField hidMfaEmail;
  19 |         protected global::System.Web.UI.WebControls.TextBox txtSetupCode;
  20 |         protected global::System.Web.UI.WebControls.Button btnConfirmMfa;
  21 |         protected global::System.Web.UI.WebControls.Label lblMfaError;
  22 |         protected global::System.Web.UI.WebControls.LinkButton lnkCancelMfa;
  23 |         protected global::System.Web.UI.WebControls.Panel pnlDone;
  24 |         protected global::System.Web.UI.WebControls.Literal litDoneMsg;
  25 |     }
  26 | }
```

**Line notes**

- **L1:** C# namespace grouping.

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
