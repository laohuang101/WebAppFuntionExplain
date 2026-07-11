# Register.aspx.cs
**Source:** `Pages/Authentication/Register.aspx.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Two-step: form → Session pending → QR/MFA confirm → only then INSERT user.

## File overview

- **Total lines:** 138
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 34:** `name` (`string`) — **Display name of user/course/criterion.**
- **Line 35:** `email` (`string`) — **Account email address (usually lowercased).**
- **Line 36:** `pass` (`string`) — **Password from a form field.**
- **Line 37:** `confirm` (`string`) — **Confirm-password form field.**
- **Line 38:** `role` (`string`) — **User role code or name (Admin/Student/Lecturer).**
- **Line 45:** `result` (`var`) — **AuthResult or API result { success, message, … }.**
- **Line 55:** `secret` (`string`) — **MFA TOTP Base32 secret for authenticator apps.**
- **Line 71:** `code` (`string`) — **6-digit TOTP / OTP the user typed.**
- **Line 89:** `result` (`var`) — **AuthResult or API result { success, message, … }.**
- **Line 126:** `normalized` (`string`) — **Cleaned secret/code (spaces removed, uppercased).**
- **Line 130:** `uri` (`string`) — **otpauth:// or other URI string.**
- **Line 132:** `qrUrl` (`string`) — **URL of QR image for authenticator setup.**

## Functions / methods (5 found)

### `Page_Load` — lines 10–28

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Session:** Reads/writes ASP.NET Session.
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L10:** Page load entry (GET or postback).
- **L12:** Server session for logged-in user.
- **L14:** Navigate browser to another URL.
- **L18:** False on first open; true after postback.

---

### `btnRegister_Click` — lines 31–65

```csharp
protected void btnRegister_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnRegister_Click`.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `name` (`string`) — Display name of user/course/criterion.
- `email` (`string`) — Account email address (usually lowercased).
- `pass` (`string`) — Password from a form field.
- `confirm` (`string`) — Confirm-password form field.
- `role` (`string`) — User role code or name (Admin/Student/Lecturer).
- `result` (`var`) — AuthResult or API result { success, message, … }.
- `secret` (`string`) — MFA TOTP Base32 secret for authenticator apps.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L46:** Pending registration in Session until MFA confirmed.
=======
**Line notes** (what code + variables mean)

- **L34:** `name` means: Display name of user/course/criterion.
- **L35:** `email` means: Account email address (usually lowercased).
- **L36:** `pass` means: Password from a form field.
- **L37:** `confirm` means: Confirm-password form field.
- **L38:** `role` means: User role code or name (Admin/Student/Lecturer).
- **L46:** Pending registration in Session until MFA confirmed. | `result` means: AuthResult or API result { success, message, … }.
- **L55:** `secret` means: MFA TOTP Base32 secret for authenticator apps.
>>>>>>> eb8ce01 (update)
- **L58:** Pending registration in Session until MFA confirmed.

---

### `btnConfirmMfa_Click` — lines 68–109

```csharp
protected void btnConfirmMfa_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnConfirmMfa_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `code` (`string`) — 6-digit TOTP / OTP the user typed.
- `result` (`var`) — AuthResult or API result { success, message, … }.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L90:** Pending registration in Session until MFA confirmed.
=======
**Line notes** (what code + variables mean)

- **L71:** `code` means: 6-digit TOTP / OTP the user typed.
- **L90:** Pending registration in Session until MFA confirmed. | `result` means: AuthResult or API result { success, message, … }.
>>>>>>> eb8ce01 (update)
- **L94:** Pending registration in Session until MFA confirmed.

---

### `lnkCancelMfa_Click` — lines 110–121

```csharp
protected void lnkCancelMfa_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `lnkCancelMfa_Click`.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L113:** Pending registration in Session until MFA confirmed.

---

### `ShowMfaSetup` — lines 122–136

```csharp
private void ShowMfaSetup(string email, string secret)
```

#### Explanation

- **Purpose:** Implements `ShowMfaSetup`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `secret` (`string`) — MFA TOTP Base32 secret for authenticator apps.
- **Local variables (what each means):**
- `normalized` (`string`) — Cleaned secret/code (spaces removed, uppercased).
- `uri` (`string`) — otpauth:// or other URI string.
- `qrUrl` (`string`) — URL of QR image for authenticator setup.  Literal text string.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L126:** TOTP / authenticator (RFC 6238) helper.
- **L127:** TOTP / authenticator (RFC 6238) helper.
- **L131:** TOTP / authenticator (RFC 6238) helper.
=======
**Line notes** (what code + variables mean)

- **L126:** TOTP / authenticator (RFC 6238) helper. | `normalized` means: Cleaned secret/code (spaces removed, uppercased).
- **L127:** TOTP / authenticator (RFC 6238) helper.
- **L131:** TOTP / authenticator (RFC 6238) helper. | `uri` means: otpauth:// or other URI string.
- **L132:** `qrUrl` means: URL of QR image for authenticator setup.  Literal text string.
>>>>>>> eb8ce01 (update)

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L6:** C# namespace grouping.
- **L10:** Page load entry (GET or postback).
- **L12:** Server session for logged-in user.
- **L14:** Navigate browser to another URL.
- **L18:** False on first open; true after postback.
<<<<<<< HEAD
- **L46:** Pending registration in Session until MFA confirmed.
- **L58:** Pending registration in Session until MFA confirmed.
- **L90:** Pending registration in Session until MFA confirmed.
- **L94:** Pending registration in Session until MFA confirmed.
- **L113:** Pending registration in Session until MFA confirmed.
- **L126:** TOTP / authenticator (RFC 6238) helper.
- **L127:** TOTP / authenticator (RFC 6238) helper.
- **L131:** TOTP / authenticator (RFC 6238) helper.
=======
- **L34:** `name` means: Display name of user/course/criterion.
- **L35:** `email` means: Account email address (usually lowercased).
- **L36:** `pass` means: Password from a form field.
- **L37:** `confirm` means: Confirm-password form field.
- **L38:** `role` means: User role code or name (Admin/Student/Lecturer).
- **L46:** Pending registration in Session until MFA confirmed. | `result` means: AuthResult or API result { success, message, … }.
- **L55:** `secret` means: MFA TOTP Base32 secret for authenticator apps.
- **L58:** Pending registration in Session until MFA confirmed.
- **L71:** `code` means: 6-digit TOTP / OTP the user typed.
- **L90:** Pending registration in Session until MFA confirmed. | `result` means: AuthResult or API result { success, message, … }.
- **L94:** Pending registration in Session until MFA confirmed.
- **L113:** Pending registration in Session until MFA confirmed.
- **L126:** TOTP / authenticator (RFC 6238) helper. | `normalized` means: Cleaned secret/code (spaces removed, uppercased).
- **L127:** TOTP / authenticator (RFC 6238) helper.
- **L131:** TOTP / authenticator (RFC 6238) helper. | `uri` means: otpauth:// or other URI string.
- **L132:** `qrUrl` means: URL of QR image for authenticator setup.  Literal text string.
>>>>>>> eb8ce01 (update)

## Source snapshot (raw)

```csharp
using System;
using System.Web;
using System.Web.UI;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Authentication
{
    public partial class Register : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack && Session["UserID"] != null)
            {
                Response.Redirect("~/Pages/Landing/Landing.aspx");
                return;
            }

            if (!IsPostBack)
            {
                // Resume MFA step if user refreshed mid-setup (account still NOT in DB)
                string email, secret;
                if (AuthService.TryGetPendingMfaSetup(Context, out email, out secret))
                {
                    pnlForm.Visible = false;
                    ShowMfaSetup(email, secret);
                }
            }
        }

        /// <summary>Step 1: validate form only — no Users row yet.</summary>
        protected void btnRegister_Click(object sender, EventArgs e)
        {
            lblError.Text = "";
            string name = (txtName.Text ?? "").Trim();
            string email = (txtEmail.Text ?? "").Trim();
            string pass = txtPassword.Text ?? "";
            string confirm = txtConfirm.Text ?? "";
            string role = rblRole.SelectedValue ?? "Student";

            if (pass != confirm)
            {
                lblError.Text = "Passwords do not match.";
                return;
            }

            var result = AuthService.StartRegistration(Context, name, email, pass, role);
            if (!result.Success)
            {
                lblError.Text = result.Message;
                return;
            }

            pnlForm.Visible = false;
            pnlDone.Visible = false;
            string secret = result.User != null ? result.User.MfaSecret : null;
            if (string.IsNullOrEmpty(secret))
            {
                AuthService.ClearPendingRegistration(Context);
                lblError.Text = "Could not start MFA setup. Please try again.";
                pnlForm.Visible = true;
                return;
            }

            ShowMfaSetup(email, secret);
        }

        /// <summary>Step 2: verify authenticator, then pure-SQL INSERT user.</summary>
        protected void btnConfirmMfa_Click(object sender, EventArgs e)
        {
            lblMfaError.Text = "";
            string code = (txtSetupCode.Text ?? "").Trim();

            string email, secret;
            if (!AuthService.TryGetPendingMfaSetup(Context, out email, out secret))
            {
                lblMfaError.Text = "Registration session expired. Please start again.";
                pnlMfaSetup.Visible = false;
                pnlForm.Visible = true;
                return;
            }

            ShowMfaSetup(email, secret);

            if (string.IsNullOrEmpty(code))
            {
                lblMfaError.Text = "Enter the 6-digit code from Google Authenticator to create your account.";
                return;
            }

            var result = AuthService.FinishRegistration(Context, code);
            if (!result.Success)
            {
                lblMfaError.Text = result.Message ?? "Could not complete registration.";
                if (!AuthService.HasPendingRegistration(Context))
                {
                    pnlMfaSetup.Visible = false;
                    pnlForm.Visible = true;
                    lblError.Text = result.Message;
                }
                return;
            }

            pnlMfaSetup.Visible = false;
            pnlForm.Visible = false;
            pnlDone.Visible = true;
            litDoneMsg.Text =
                "Account created. Sign in with your password and a <strong>new</strong> 6-digit code " +
                "from the same Google Authenticator entry (codes change every 30 seconds).";
        }

        protected void lnkCancelMfa_Click(object sender, EventArgs e)
        {
            AuthService.ClearPendingRegistration(Context);
            pnlMfaSetup.Visible = false;
            pnlDone.Visible = false;
            pnlForm.Visible = true;
            lblError.Text = "";
            lblMfaError.Text = "";
            txtPassword.Text = "";
            txtConfirm.Text = "";
        }

        private void ShowMfaSetup(string email, string secret)
        {
            pnlMfaSetup.Visible = true;
            string normalized = TotpHelper.NormalizeSecret(secret);
            litMfaSecret.Text = TotpHelper.FormatSecretForDisplay(normalized);
            hidMfaSecret.Value = normalized;
            hidMfaEmail.Value = email ?? "";

            string uri = TotpHelper.BuildOtpAuthUri(email, normalized, "EduLMS");
            string qrUrl = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&ecc=M&data="
                + HttpUtility.UrlEncode(uri);
            imgQr.ImageUrl = qrUrl;
            imgQr.AlternateText = "Scan with Google Authenticator";
        }
    }
}

```
