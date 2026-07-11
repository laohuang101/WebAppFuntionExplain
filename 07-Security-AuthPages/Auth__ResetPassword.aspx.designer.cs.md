# ResetPassword.aspx.designer.cs
**Source:** `Pages/Authentication/ResetPassword.aspx.designer.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

One-shot TOTP + new password form (uses AuthService.ResetPasswordWithTotp).

## File overview

- **Total lines:** 13
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
   3 |     public partial class ResetPassword
   4 |     {
   5 |         protected global::System.Web.UI.HtmlControls.HtmlForm form1;
   6 |         protected global::System.Web.UI.WebControls.TextBox txtEmail;
   7 |         protected global::System.Web.UI.WebControls.TextBox txtCode;
   8 |         protected global::System.Web.UI.WebControls.TextBox txtPassword;
   9 |         protected global::System.Web.UI.WebControls.TextBox txtPassword2;
  10 |         protected global::System.Web.UI.WebControls.Button btnReset;
  11 |         protected global::System.Web.UI.WebControls.Label lblMsg;
  12 |     }
  13 | }
```

**Line notes**

- **L1:** C# namespace grouping.

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
