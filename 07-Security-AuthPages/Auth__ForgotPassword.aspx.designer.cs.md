# ForgotPassword.aspx.designer.cs
**Source:** `Pages/Authentication/ForgotPassword.aspx.designer.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Two-step reset: verify email+TOTP first, then set new password (session window).

## File overview

- **Total lines:** 20
- **Kind:** `.cs`

## Variables / fields (file level)

_No classic field declarations detected (or mostly locals inside methods)._

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```csharp
   1 | namespace WebAppAssignment.Pages.Authentication
   2 | {
   3 |     public partial class ForgotPassword
   4 |     {
   5 |         protected global::System.Web.UI.HtmlControls.HtmlForm form1;
   6 |         protected global::System.Web.UI.HtmlControls.HtmlGenericControl pill1;
   7 |         protected global::System.Web.UI.HtmlControls.HtmlGenericControl pill2;
   8 |         protected global::System.Web.UI.WebControls.Panel pnlStep1;
   9 |         protected global::System.Web.UI.WebControls.TextBox txtEmail;
  10 |         protected global::System.Web.UI.WebControls.TextBox txtMfaCode;
  11 |         protected global::System.Web.UI.WebControls.Button btnVerify;
  12 |         protected global::System.Web.UI.WebControls.Panel pnlStep2;
  13 |         protected global::System.Web.UI.WebControls.Literal litVerifiedEmail;
  14 |         protected global::System.Web.UI.WebControls.TextBox txtPassword;
  15 |         protected global::System.Web.UI.WebControls.TextBox txtPassword2;
  16 |         protected global::System.Web.UI.WebControls.Button btnReset;
  17 |         protected global::System.Web.UI.WebControls.LinkButton lnkBack;
  18 |         protected global::System.Web.UI.WebControls.Label lblMsg;
  19 |     }
  20 | }
```

**Line notes**

- **L1:** C# namespace grouping.

## Source snapshot (raw)

```csharp
namespace WebAppAssignment.Pages.Authentication
{
    public partial class ForgotPassword
    {
        protected global::System.Web.UI.HtmlControls.HtmlForm form1;
        protected global::System.Web.UI.HtmlControls.HtmlGenericControl pill1;
        protected global::System.Web.UI.HtmlControls.HtmlGenericControl pill2;
        protected global::System.Web.UI.WebControls.Panel pnlStep1;
        protected global::System.Web.UI.WebControls.TextBox txtEmail;
        protected global::System.Web.UI.WebControls.TextBox txtMfaCode;
        protected global::System.Web.UI.WebControls.Button btnVerify;
        protected global::System.Web.UI.WebControls.Panel pnlStep2;
        protected global::System.Web.UI.WebControls.Literal litVerifiedEmail;
        protected global::System.Web.UI.WebControls.TextBox txtPassword;
        protected global::System.Web.UI.WebControls.TextBox txtPassword2;
        protected global::System.Web.UI.WebControls.Button btnReset;
        protected global::System.Web.UI.WebControls.LinkButton lnkBack;
        protected global::System.Web.UI.WebControls.Label lblMsg;
    }
}

```
