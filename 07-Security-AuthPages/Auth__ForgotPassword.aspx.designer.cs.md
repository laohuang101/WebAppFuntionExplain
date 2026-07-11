# ForgotPassword.aspx.designer.cs
**Source:** `Pages/Authentication/ForgotPassword.aspx.designer.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Two-step reset: verify email+TOTP first, then set new password (session window).

## File overview

- **Total lines:** 20
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See the code listing at the bottom._

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
