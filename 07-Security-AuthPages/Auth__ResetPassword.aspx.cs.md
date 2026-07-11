# ResetPassword.aspx.cs
**Source:** `Pages/Authentication/ResetPassword.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

One-shot TOTP + new password form (uses AuthService.ResetPasswordWithTotp).

## File overview

- **Total lines:** 44
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (2 found)

### `Page_Load` — lines 9–19

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. ASP.NET calls this automatically on every request.
2. On first load (`!IsPostBack`), initialize UI or redirect if already logged in.
3. On postback, button handlers run separately after this method.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased).  Comes from HTTP request. |

#### Code

```csharp
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             AuthSchema.Ensure();
  12 |             CsrfProtection.EnsureToken(Context);
  13 |             if (!IsPostBack)
  14 |             {
  15 |                 string email = Request.QueryString["email"];
  16 |                 if (!string.IsNullOrEmpty(email))
  17 |                     txtEmail.Text = email.Trim();
  18 |             }
  19 |         }
```

---

### `btnReset_Click` — lines 20–42

#### Signature

```csharp
protected void btnReset_Click(object sender, EventArgs e)
```

#### What it is

Button handler: save the new password after MFA was already verified.

#### How it works

1. Starts when something calls `btnReset_Click`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `p1` | `string` | New password field (first entry). |
| `p2` | `string` | Confirm password field (must match p1). |
| `result` | `var` | AuthResult or API result { success, message, … }. |

#### Code

```csharp
  20 | 
  21 |         protected void btnReset_Click(object sender, EventArgs e)
  22 |         {
  23 |             lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
  24 |             string p1 = txtPassword.Text ?? "";
  25 |             string p2 = txtPassword2.Text ?? "";
  26 |             if (p1 != p2)
  27 |             {
  28 |                 lblMsg.Text = "Passwords do not match.";
  29 |                 return;
  30 |             }
  31 | 
  32 |             var result = AuthService.ResetPasswordWithTotp(txtEmail.Text, txtCode.Text, p1);
  33 |             if (!result.Success)
  34 |             {
  35 |                 lblMsg.Text = result.Message ?? "Could not reset password.";
  36 |                 return;
  37 |             }
  38 | 
  39 |             lblMsg.CssClass = "d-block mt-3 text-center small text-success";
  40 |             lblMsg.Text = result.Message + " Redirecting to login…";
  41 |             Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));
  42 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Web.UI;
   3 | using WebAppAssignment.Data.Security;
   4 | 
   5 | namespace WebAppAssignment.Pages.Authentication
   6 | {
   7 |     public partial class ResetPassword : Page
   8 |     {
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             AuthSchema.Ensure();
  12 |             CsrfProtection.EnsureToken(Context);
  13 |             if (!IsPostBack)
  14 |             {
  15 |                 string email = Request.QueryString["email"];
  16 |                 if (!string.IsNullOrEmpty(email))
  17 |                     txtEmail.Text = email.Trim();
  18 |             }
  19 |         }
  20 | 
  21 |         protected void btnReset_Click(object sender, EventArgs e)
  22 |         {
  23 |             lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
  24 |             string p1 = txtPassword.Text ?? "";
  25 |             string p2 = txtPassword2.Text ?? "";
  26 |             if (p1 != p2)
  27 |             {
  28 |                 lblMsg.Text = "Passwords do not match.";
  29 |                 return;
  30 |             }
  31 | 
  32 |             var result = AuthService.ResetPasswordWithTotp(txtEmail.Text, txtCode.Text, p1);
  33 |             if (!result.Success)
  34 |             {
  35 |                 lblMsg.Text = result.Message ?? "Could not reset password.";
  36 |                 return;
  37 |             }
  38 | 
  39 |             lblMsg.CssClass = "d-block mt-3 text-center small text-success";
  40 |             lblMsg.Text = result.Message + " Redirecting to login…";
  41 |             Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));
  42 |         }
  43 |     }
  44 | }
```
