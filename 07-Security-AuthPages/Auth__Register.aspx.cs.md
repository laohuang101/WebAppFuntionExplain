# Register.aspx.cs
**Source:** `Pages/Authentication/Register.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Two-step: form → Session pending → QR/MFA confirm → only then INSERT user.

## File overview

- **Total lines:** 138
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (5 found)

### `Page_Load` — lines 10–28

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. Save temporary state in Session (`Session["UserID"] !`).
2. Redirect the browser to another page.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  10 |         protected void Page_Load(object sender, EventArgs e)
  11 |         {
  12 |             if (!IsPostBack && Session["UserID"] != null)
  13 |             {
  14 |                 Response.Redirect("~/Pages/Landing/Landing.aspx");
  15 |                 return;
  16 |             }
  17 | 
  18 |             if (!IsPostBack)
  19 |             {
  20 |                 // Resume MFA step if user refreshed mid-setup (account still NOT in DB)
  21 |                 string email, secret;
  22 |                 if (AuthService.TryGetPendingMfaSetup(Context, out email, out secret))
  23 |                 {
  24 |                     pnlForm.Visible = false;
  25 |                     ShowMfaSetup(email, secret);
  26 |                 }
  27 |             }
  28 |         }
```

---

### `btnRegister_Click` — lines 31–65

#### Signature

```csharp
protected void btnRegister_Click(object sender, EventArgs e)
```

#### What it is

Button handler: start registration and show the MFA setup panel.

#### How it works

1. Read name, email, passwords, and role from the form.
2. If passwords do not match, show an error.
3. Call StartRegistration (Session pending only).
4. Hide the form and show the MFA QR / secret panel.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `name` | `string` | Display name of user/course/criterion. |
| `email` | `string` | Account email address (usually lowercased). |
| `pass` | `string` | Password from a form field. |
| `confirm` | `string` | Confirm-password form field. |
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |
| `result` | `var` | AuthResult or API result { success, message, … }. |
| `secret` | `string` | MFA TOTP Base32 secret for authenticator apps. |

#### Code

```csharp
  31 |         protected void btnRegister_Click(object sender, EventArgs e)
  32 |         {
  33 |             lblError.Text = "";
  34 |             string name = (txtName.Text ?? "").Trim();
  35 |             string email = (txtEmail.Text ?? "").Trim();
  36 |             string pass = txtPassword.Text ?? "";
  37 |             string confirm = txtConfirm.Text ?? "";
  38 |             string role = rblRole.SelectedValue ?? "Student";
  39 | 
  40 |             if (pass != confirm)
  41 |             {
  42 |                 lblError.Text = "Passwords do not match.";
  43 |                 return;
  44 |             }
  45 | 
  46 |             var result = AuthService.StartRegistration(Context, name, email, pass, role);
  47 |             if (!result.Success)
  48 |             {
  49 |                 lblError.Text = result.Message;
  50 |                 return;
  51 |             }
  52 | 
  53 |             pnlForm.Visible = false;
  54 |             pnlDone.Visible = false;
  55 |             string secret = result.User != null ? result.User.MfaSecret : null;
  56 |             if (string.IsNullOrEmpty(secret))
  57 |             {
  58 |                 AuthService.ClearPendingRegistration(Context);
  59 |                 lblError.Text = "Could not start MFA setup. Please try again.";
  60 |                 pnlForm.Visible = true;
  61 |                 return;
  62 |             }
  63 | 
  64 |             ShowMfaSetup(email, secret);
  65 |         }
```

---

### `btnConfirmMfa_Click` — lines 68–109

#### Signature

```csharp
protected void btnConfirmMfa_Click(object sender, EventArgs e)
```

#### What it is

Button handler: finish registration only after a valid authenticator code.

#### How it works

1. Read the 6-digit code the user typed.
2. Call FinishRegistration (creates the Users row only if the code is valid).
3. On success, show the “done” panel with a link to Login.
4. On failure, keep the MFA panel and show the error.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `code` | `string` | 6-digit TOTP / OTP the user typed. |
| `result` | `var` | AuthResult or API result { success, message, … }. |

#### Code

```csharp
  68 |         protected void btnConfirmMfa_Click(object sender, EventArgs e)
  69 |         {
  70 |             lblMfaError.Text = "";
  71 |             string code = (txtSetupCode.Text ?? "").Trim();
  72 | 
  73 |             string email, secret;
  74 |             if (!AuthService.TryGetPendingMfaSetup(Context, out email, out secret))
  75 |             {
  76 |                 lblMfaError.Text = "Registration session expired. Please start again.";
  77 |                 pnlMfaSetup.Visible = false;
  78 |                 pnlForm.Visible = true;
  79 |                 return;
  80 |             }
  81 | 
  82 |             ShowMfaSetup(email, secret);
  83 | 
  84 |             if (string.IsNullOrEmpty(code))
  85 |             {
  86 |                 lblMfaError.Text = "Enter the 6-digit code from Google Authenticator to create your account.";
  87 |                 return;
  88 |             }
  89 | 
  90 |             var result = AuthService.FinishRegistration(Context, code);
  91 |             if (!result.Success)
  92 |             {
  93 |                 lblMfaError.Text = result.Message ?? "Could not complete registration.";
  94 |                 if (!AuthService.HasPendingRegistration(Context))
  95 |                 {
  96 |                     pnlMfaSetup.Visible = false;
  97 |                     pnlForm.Visible = true;
  98 |                     lblError.Text = result.Message;
  99 |                 }
 100 |                 return;
 101 |             }
 102 | 
 103 |             pnlMfaSetup.Visible = false;
 104 |             pnlForm.Visible = false;
 105 |             pnlDone.Visible = true;
 106 |             litDoneMsg.Text =
 107 |                 "Account created. Sign in with your password and a <strong>new</strong> 6-digit code " +
 108 |                 "from the same Google Authenticator entry (codes change every 30 seconds).";
 109 |         }
```

---

### `lnkCancelMfa_Click` — lines 110–121

#### Signature

```csharp
protected void lnkCancelMfa_Click(object sender, EventArgs e)
```

#### What it is

Function `lnkCancelMfa_Click` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `lnkCancelMfa_Click`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 110 | 
 111 |         protected void lnkCancelMfa_Click(object sender, EventArgs e)
 112 |         {
 113 |             AuthService.ClearPendingRegistration(Context);
 114 |             pnlMfaSetup.Visible = false;
 115 |             pnlDone.Visible = false;
 116 |             pnlForm.Visible = true;
 117 |             lblError.Text = "";
 118 |             lblMfaError.Text = "";
 119 |             txtPassword.Text = "";
 120 |             txtConfirm.Text = "";
 121 |         }
```

---

### `ShowMfaSetup` — lines 122–136

#### Signature

```csharp
private void ShowMfaSetup(string email, string secret)
```

#### What it is

Updates the page HTML for **Show Mfa Setup**.

#### How it works

1. Build the otpauth URI used to show the QR code.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `secret` | `string` | MFA TOTP Base32 secret for authenticator apps. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `normalized` | `string` | Cleaned secret/code (spaces removed, uppercased). |
| `uri` | `string` | otpauth:// or other URI string. |
| `qrUrl` | `string` | URL of QR image for authenticator setup.  Literal text string. |

#### Code

```csharp
 122 | 
 123 |         private void ShowMfaSetup(string email, string secret)
 124 |         {
 125 |             pnlMfaSetup.Visible = true;
 126 |             string normalized = TotpHelper.NormalizeSecret(secret);
 127 |             litMfaSecret.Text = TotpHelper.FormatSecretForDisplay(normalized);
 128 |             hidMfaSecret.Value = normalized;
 129 |             hidMfaEmail.Value = email ?? "";
 130 | 
 131 |             string uri = TotpHelper.BuildOtpAuthUri(email, normalized, "EduLMS");
 132 |             string qrUrl = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&ecc=M&data="
 133 |                 + HttpUtility.UrlEncode(uri);
 134 |             imgQr.ImageUrl = qrUrl;
 135 |             imgQr.AlternateText = "Scan with Google Authenticator";
 136 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Web;
   3 | using System.Web.UI;
   4 | using WebAppAssignment.Data.Security;
   5 | 
   6 | namespace WebAppAssignment.Pages.Authentication
   7 | {
   8 |     public partial class Register : Page
   9 |     {
  10 |         protected void Page_Load(object sender, EventArgs e)
  11 |         {
  12 |             if (!IsPostBack && Session["UserID"] != null)
  13 |             {
  14 |                 Response.Redirect("~/Pages/Landing/Landing.aspx");
  15 |                 return;
  16 |             }
  17 | 
  18 |             if (!IsPostBack)
  19 |             {
  20 |                 // Resume MFA step if user refreshed mid-setup (account still NOT in DB)
  21 |                 string email, secret;
  22 |                 if (AuthService.TryGetPendingMfaSetup(Context, out email, out secret))
  23 |                 {
  24 |                     pnlForm.Visible = false;
  25 |                     ShowMfaSetup(email, secret);
  26 |                 }
  27 |             }
  28 |         }
  29 | 
  30 |         /// <summary>Step 1: validate form only — no Users row yet.</summary>
  31 |         protected void btnRegister_Click(object sender, EventArgs e)
  32 |         {
  33 |             lblError.Text = "";
  34 |             string name = (txtName.Text ?? "").Trim();
  35 |             string email = (txtEmail.Text ?? "").Trim();
  36 |             string pass = txtPassword.Text ?? "";
  37 |             string confirm = txtConfirm.Text ?? "";
  38 |             string role = rblRole.SelectedValue ?? "Student";
  39 | 
  40 |             if (pass != confirm)
  41 |             {
  42 |                 lblError.Text = "Passwords do not match.";
  43 |                 return;
  44 |             }
  45 | 
  46 |             var result = AuthService.StartRegistration(Context, name, email, pass, role);
  47 |             if (!result.Success)
  48 |             {
  49 |                 lblError.Text = result.Message;
  50 |                 return;
  51 |             }
  52 | 
  53 |             pnlForm.Visible = false;
  54 |             pnlDone.Visible = false;
  55 |             string secret = result.User != null ? result.User.MfaSecret : null;
  56 |             if (string.IsNullOrEmpty(secret))
  57 |             {
  58 |                 AuthService.ClearPendingRegistration(Context);
  59 |                 lblError.Text = "Could not start MFA setup. Please try again.";
  60 |                 pnlForm.Visible = true;
  61 |                 return;
  62 |             }
  63 | 
  64 |             ShowMfaSetup(email, secret);
  65 |         }
  66 | 
  67 |         /// <summary>Step 2: verify authenticator, then pure-SQL INSERT user.</summary>
  68 |         protected void btnConfirmMfa_Click(object sender, EventArgs e)
  69 |         {
  70 |             lblMfaError.Text = "";
  71 |             string code = (txtSetupCode.Text ?? "").Trim();
  72 | 
  73 |             string email, secret;
  74 |             if (!AuthService.TryGetPendingMfaSetup(Context, out email, out secret))
  75 |             {
  76 |                 lblMfaError.Text = "Registration session expired. Please start again.";
  77 |                 pnlMfaSetup.Visible = false;
  78 |                 pnlForm.Visible = true;
  79 |                 return;
  80 |             }
  81 | 
  82 |             ShowMfaSetup(email, secret);
  83 | 
  84 |             if (string.IsNullOrEmpty(code))
  85 |             {
  86 |                 lblMfaError.Text = "Enter the 6-digit code from Google Authenticator to create your account.";
  87 |                 return;
  88 |             }
  89 | 
  90 |             var result = AuthService.FinishRegistration(Context, code);
  91 |             if (!result.Success)
  92 |             {
  93 |                 lblMfaError.Text = result.Message ?? "Could not complete registration.";
  94 |                 if (!AuthService.HasPendingRegistration(Context))
  95 |                 {
  96 |                     pnlMfaSetup.Visible = false;
  97 |                     pnlForm.Visible = true;
  98 |                     lblError.Text = result.Message;
  99 |                 }
 100 |                 return;
 101 |             }
 102 | 
 103 |             pnlMfaSetup.Visible = false;
 104 |             pnlForm.Visible = false;
 105 |             pnlDone.Visible = true;
 106 |             litDoneMsg.Text =
 107 |                 "Account created. Sign in with your password and a <strong>new</strong> 6-digit code " +
 108 |                 "from the same Google Authenticator entry (codes change every 30 seconds).";
 109 |         }
 110 | 
 111 |         protected void lnkCancelMfa_Click(object sender, EventArgs e)
 112 |         {
 113 |             AuthService.ClearPendingRegistration(Context);
 114 |             pnlMfaSetup.Visible = false;
 115 |             pnlDone.Visible = false;
 116 |             pnlForm.Visible = true;
 117 |             lblError.Text = "";
 118 |             lblMfaError.Text = "";
 119 |             txtPassword.Text = "";
 120 |             txtConfirm.Text = "";
 121 |         }
 122 | 
 123 |         private void ShowMfaSetup(string email, string secret)
 124 |         {
 125 |             pnlMfaSetup.Visible = true;
 126 |             string normalized = TotpHelper.NormalizeSecret(secret);
 127 |             litMfaSecret.Text = TotpHelper.FormatSecretForDisplay(normalized);
 128 |             hidMfaSecret.Value = normalized;
 129 |             hidMfaEmail.Value = email ?? "";
 130 | 
 131 |             string uri = TotpHelper.BuildOtpAuthUri(email, normalized, "EduLMS");
 132 |             string qrUrl = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&ecc=M&data="
 133 |                 + HttpUtility.UrlEncode(uri);
 134 |             imgQr.ImageUrl = qrUrl;
 135 |             imgQr.AlternateText = "Scan with Google Authenticator";
 136 |         }
 137 |     }
 138 | }
```
