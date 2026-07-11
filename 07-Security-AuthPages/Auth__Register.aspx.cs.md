# Register.aspx.cs
**Source:** `Pages/Authentication/Register.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Two-step: form → Session pending → QR/MFA confirm → only then INSERT user.

## File overview

- **Total lines:** 138
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 34:** `name` — type `string`
- **Line 35:** `email` — type `string`
- **Line 36:** `pass` — type `string`
- **Line 37:** `confirm` — type `string`
- **Line 38:** `role` — type `string`
- **Line 45:** `result` — type `var`
- **Line 55:** `secret` — type `string`
- **Line 71:** `code` — type `string`
- **Line 89:** `result` — type `var`
- **Line 126:** `normalized` — type `string`
- **Line 130:** `uri` — type `string`
- **Line 132:** `qrUrl` — type `string`

## Functions / methods (5 found)

### `Page_Load` — lines 10–28

```
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Session:** Reads/writes ASP.NET Session.
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`

#### Line-by-line (this function)

`  10`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  11`  `        {`
`  12`  `            if (!IsPostBack && Session["UserID"] != null)`
  - → Server session for logged-in user.
`  13`  `            {`
`  14`  `                Response.Redirect("~/Pages/Landing/Landing.aspx");`
  - → Navigate browser to another URL.
`  15`  `                return;`
`  16`  `            }`
`  17`  ``
`  18`  `            if (!IsPostBack)`
  - → False on first open; true after postback.
`  19`  `            {`
`  20`  `                // Resume MFA step if user refreshed mid-setup (account still NOT in DB)`
`  21`  `                string email, secret;`
`  22`  `                if (AuthService.TryGetPendingMfaSetup(Context, out email, out secret))`
`  23`  `                {`
`  24`  `                    pnlForm.Visible = false;`
`  25`  `                    ShowMfaSetup(email, secret);`
`  26`  `                }`
`  27`  `            }`
`  28`  `        }`

---

### `btnRegister_Click` — lines 31–65

```
protected void btnRegister_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnRegister_Click`.
- **Parameters:** `object sender, EventArgs e`
- **Local variables:** `name`, `email`, `pass`, `confirm`, `role`, `result`, `secret`

#### Line-by-line (this function)

`  31`  `        protected void btnRegister_Click(object sender, EventArgs e)`
`  32`  `        {`
`  33`  `            lblError.Text = "";`
`  34`  `            string name = (txtName.Text ?? "").Trim();`
`  35`  `            string email = (txtEmail.Text ?? "").Trim();`
`  36`  `            string pass = txtPassword.Text ?? "";`
`  37`  `            string confirm = txtConfirm.Text ?? "";`
`  38`  `            string role = rblRole.SelectedValue ?? "Student";`
`  39`  ``
`  40`  `            if (pass != confirm)`
`  41`  `            {`
`  42`  `                lblError.Text = "Passwords do not match.";`
`  43`  `                return;`
`  44`  `            }`
`  45`  ``
`  46`  `            var result = AuthService.StartRegistration(Context, name, email, pass, role);`
  - → Pending registration in Session until MFA confirmed.
`  47`  `            if (!result.Success)`
`  48`  `            {`
`  49`  `                lblError.Text = result.Message;`
`  50`  `                return;`
`  51`  `            }`
`  52`  ``
`  53`  `            pnlForm.Visible = false;`
`  54`  `            pnlDone.Visible = false;`
`  55`  `            string secret = result.User != null ? result.User.MfaSecret : null;`
`  56`  `            if (string.IsNullOrEmpty(secret))`
`  57`  `            {`
`  58`  `                AuthService.ClearPendingRegistration(Context);`
  - → Pending registration in Session until MFA confirmed.
`  59`  `                lblError.Text = "Could not start MFA setup. Please try again.";`
`  60`  `                pnlForm.Visible = true;`
`  61`  `                return;`
`  62`  `            }`
`  63`  ``
`  64`  `            ShowMfaSetup(email, secret);`
`  65`  `        }`

---

### `btnConfirmMfa_Click` — lines 68–109

```
protected void btnConfirmMfa_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnConfirmMfa_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `object sender, EventArgs e`
- **Local variables:** `code`, `result`

#### Line-by-line (this function)

`  68`  `        protected void btnConfirmMfa_Click(object sender, EventArgs e)`
`  69`  `        {`
`  70`  `            lblMfaError.Text = "";`
`  71`  `            string code = (txtSetupCode.Text ?? "").Trim();`
`  72`  ``
`  73`  `            string email, secret;`
`  74`  `            if (!AuthService.TryGetPendingMfaSetup(Context, out email, out secret))`
`  75`  `            {`
`  76`  `                lblMfaError.Text = "Registration session expired. Please start again.";`
`  77`  `                pnlMfaSetup.Visible = false;`
`  78`  `                pnlForm.Visible = true;`
`  79`  `                return;`
`  80`  `            }`
`  81`  ``
`  82`  `            ShowMfaSetup(email, secret);`
`  83`  ``
`  84`  `            if (string.IsNullOrEmpty(code))`
`  85`  `            {`
`  86`  `                lblMfaError.Text = "Enter the 6-digit code from Google Authenticator to create your account.";`
`  87`  `                return;`
`  88`  `            }`
`  89`  ``
`  90`  `            var result = AuthService.FinishRegistration(Context, code);`
  - → Pending registration in Session until MFA confirmed.
`  91`  `            if (!result.Success)`
`  92`  `            {`
`  93`  `                lblMfaError.Text = result.Message ?? "Could not complete registration.";`
`  94`  `                if (!AuthService.HasPendingRegistration(Context))`
  - → Pending registration in Session until MFA confirmed.
`  95`  `                {`
`  96`  `                    pnlMfaSetup.Visible = false;`
`  97`  `                    pnlForm.Visible = true;`
`  98`  `                    lblError.Text = result.Message;`
`  99`  `                }`
` 100`  `                return;`
` 101`  `            }`
` 102`  ``
` 103`  `            pnlMfaSetup.Visible = false;`
` 104`  `            pnlForm.Visible = false;`
` 105`  `            pnlDone.Visible = true;`
` 106`  `            litDoneMsg.Text =`
` 107`  `                "Account created. Sign in with your password and a <strong>new</strong> 6-digit code " +`
` 108`  `                "from the same Google Authenticator entry (codes change every 30 seconds).";`
` 109`  `        }`

---

### `lnkCancelMfa_Click` — lines 110–121

```
protected void lnkCancelMfa_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `lnkCancelMfa_Click`.
- **Parameters:** `object sender, EventArgs e`

#### Line-by-line (this function)

` 110`  ``
` 111`  `        protected void lnkCancelMfa_Click(object sender, EventArgs e)`
` 112`  `        {`
` 113`  `            AuthService.ClearPendingRegistration(Context);`
  - → Pending registration in Session until MFA confirmed.
` 114`  `            pnlMfaSetup.Visible = false;`
` 115`  `            pnlDone.Visible = false;`
` 116`  `            pnlForm.Visible = true;`
` 117`  `            lblError.Text = "";`
` 118`  `            lblMfaError.Text = "";`
` 119`  `            txtPassword.Text = "";`
` 120`  `            txtConfirm.Text = "";`
` 121`  `        }`

---

### `ShowMfaSetup` — lines 122–136

```
private void ShowMfaSetup(string email, string secret)
```

#### Explanation

- **Purpose:** Implements `ShowMfaSetup`.
- **Parameters:** `string email, string secret`
- **Local variables:** `normalized`, `uri`, `qrUrl`

#### Line-by-line (this function)

` 122`  ``
` 123`  `        private void ShowMfaSetup(string email, string secret)`
` 124`  `        {`
` 125`  `            pnlMfaSetup.Visible = true;`
` 126`  `            string normalized = TotpHelper.NormalizeSecret(secret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 127`  `            litMfaSecret.Text = TotpHelper.FormatSecretForDisplay(normalized);`
  - → TOTP / authenticator (RFC 6238) helper.
` 128`  `            hidMfaSecret.Value = normalized;`
` 129`  `            hidMfaEmail.Value = email ?? "";`
` 130`  ``
` 131`  `            string uri = TotpHelper.BuildOtpAuthUri(email, normalized, "EduLMS");`
  - → TOTP / authenticator (RFC 6238) helper.
` 132`  `            string qrUrl = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&ecc=M&data="`
` 133`  `                + HttpUtility.UrlEncode(uri);`
` 134`  `            imgQr.ImageUrl = qrUrl;`
` 135`  `            imgQr.AlternateText = "Scan with Google Authenticator";`
` 136`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Web;`
  - → Import namespace/types.
`   3`  `using System.Web.UI;`
  - → Import namespace/types.
`   4`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`   5`  ``
`   6`  `namespace WebAppAssignment.Pages.Authentication`
  - → C# namespace grouping.
`   7`  `{`
`   8`  `    public partial class Register : Page`
`   9`  `    {`
`  10`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  11`  `        {`
`  12`  `            if (!IsPostBack && Session["UserID"] != null)`
  - → Server session for logged-in user.
`  13`  `            {`
`  14`  `                Response.Redirect("~/Pages/Landing/Landing.aspx");`
  - → Navigate browser to another URL.
`  15`  `                return;`
`  16`  `            }`
`  17`  ``
`  18`  `            if (!IsPostBack)`
  - → False on first open; true after postback.
`  19`  `            {`
`  20`  `                // Resume MFA step if user refreshed mid-setup (account still NOT in DB)`
`  21`  `                string email, secret;`
`  22`  `                if (AuthService.TryGetPendingMfaSetup(Context, out email, out secret))`
`  23`  `                {`
`  24`  `                    pnlForm.Visible = false;`
`  25`  `                    ShowMfaSetup(email, secret);`
`  26`  `                }`
`  27`  `            }`
`  28`  `        }`
`  29`  ``
`  30`  `        /// <summary>Step 1: validate form only — no Users row yet.</summary>`
`  31`  `        protected void btnRegister_Click(object sender, EventArgs e)`
`  32`  `        {`
`  33`  `            lblError.Text = "";`
`  34`  `            string name = (txtName.Text ?? "").Trim();`
`  35`  `            string email = (txtEmail.Text ?? "").Trim();`
`  36`  `            string pass = txtPassword.Text ?? "";`
`  37`  `            string confirm = txtConfirm.Text ?? "";`
`  38`  `            string role = rblRole.SelectedValue ?? "Student";`
`  39`  ``
`  40`  `            if (pass != confirm)`
`  41`  `            {`
`  42`  `                lblError.Text = "Passwords do not match.";`
`  43`  `                return;`
`  44`  `            }`
`  45`  ``
`  46`  `            var result = AuthService.StartRegistration(Context, name, email, pass, role);`
  - → Pending registration in Session until MFA confirmed.
`  47`  `            if (!result.Success)`
`  48`  `            {`
`  49`  `                lblError.Text = result.Message;`
`  50`  `                return;`
`  51`  `            }`
`  52`  ``
`  53`  `            pnlForm.Visible = false;`
`  54`  `            pnlDone.Visible = false;`
`  55`  `            string secret = result.User != null ? result.User.MfaSecret : null;`
`  56`  `            if (string.IsNullOrEmpty(secret))`
`  57`  `            {`
`  58`  `                AuthService.ClearPendingRegistration(Context);`
  - → Pending registration in Session until MFA confirmed.
`  59`  `                lblError.Text = "Could not start MFA setup. Please try again.";`
`  60`  `                pnlForm.Visible = true;`
`  61`  `                return;`
`  62`  `            }`
`  63`  ``
`  64`  `            ShowMfaSetup(email, secret);`
`  65`  `        }`
`  66`  ``
`  67`  `        /// <summary>Step 2: verify authenticator, then pure-SQL INSERT user.</summary>`
`  68`  `        protected void btnConfirmMfa_Click(object sender, EventArgs e)`
`  69`  `        {`
`  70`  `            lblMfaError.Text = "";`
`  71`  `            string code = (txtSetupCode.Text ?? "").Trim();`
`  72`  ``
`  73`  `            string email, secret;`
`  74`  `            if (!AuthService.TryGetPendingMfaSetup(Context, out email, out secret))`
`  75`  `            {`
`  76`  `                lblMfaError.Text = "Registration session expired. Please start again.";`
`  77`  `                pnlMfaSetup.Visible = false;`
`  78`  `                pnlForm.Visible = true;`
`  79`  `                return;`
`  80`  `            }`
`  81`  ``
`  82`  `            ShowMfaSetup(email, secret);`
`  83`  ``
`  84`  `            if (string.IsNullOrEmpty(code))`
`  85`  `            {`
`  86`  `                lblMfaError.Text = "Enter the 6-digit code from Google Authenticator to create your account.";`
`  87`  `                return;`
`  88`  `            }`
`  89`  ``
`  90`  `            var result = AuthService.FinishRegistration(Context, code);`
  - → Pending registration in Session until MFA confirmed.
`  91`  `            if (!result.Success)`
`  92`  `            {`
`  93`  `                lblMfaError.Text = result.Message ?? "Could not complete registration.";`
`  94`  `                if (!AuthService.HasPendingRegistration(Context))`
  - → Pending registration in Session until MFA confirmed.
`  95`  `                {`
`  96`  `                    pnlMfaSetup.Visible = false;`
`  97`  `                    pnlForm.Visible = true;`
`  98`  `                    lblError.Text = result.Message;`
`  99`  `                }`
` 100`  `                return;`
` 101`  `            }`
` 102`  ``
` 103`  `            pnlMfaSetup.Visible = false;`
` 104`  `            pnlForm.Visible = false;`
` 105`  `            pnlDone.Visible = true;`
` 106`  `            litDoneMsg.Text =`
` 107`  `                "Account created. Sign in with your password and a <strong>new</strong> 6-digit code " +`
` 108`  `                "from the same Google Authenticator entry (codes change every 30 seconds).";`
` 109`  `        }`
` 110`  ``
` 111`  `        protected void lnkCancelMfa_Click(object sender, EventArgs e)`
` 112`  `        {`
` 113`  `            AuthService.ClearPendingRegistration(Context);`
  - → Pending registration in Session until MFA confirmed.
` 114`  `            pnlMfaSetup.Visible = false;`
` 115`  `            pnlDone.Visible = false;`
` 116`  `            pnlForm.Visible = true;`
` 117`  `            lblError.Text = "";`
` 118`  `            lblMfaError.Text = "";`
` 119`  `            txtPassword.Text = "";`
` 120`  `            txtConfirm.Text = "";`
` 121`  `        }`
` 122`  ``
` 123`  `        private void ShowMfaSetup(string email, string secret)`
` 124`  `        {`
` 125`  `            pnlMfaSetup.Visible = true;`
` 126`  `            string normalized = TotpHelper.NormalizeSecret(secret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 127`  `            litMfaSecret.Text = TotpHelper.FormatSecretForDisplay(normalized);`
  - → TOTP / authenticator (RFC 6238) helper.
` 128`  `            hidMfaSecret.Value = normalized;`
` 129`  `            hidMfaEmail.Value = email ?? "";`
` 130`  ``
` 131`  `            string uri = TotpHelper.BuildOtpAuthUri(email, normalized, "EduLMS");`
  - → TOTP / authenticator (RFC 6238) helper.
` 132`  `            string qrUrl = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&ecc=M&data="`
` 133`  `                + HttpUtility.UrlEncode(uri);`
` 134`  `            imgQr.ImageUrl = qrUrl;`
` 135`  `            imgQr.AlternateText = "Scan with Google Authenticator";`
` 136`  `        }`
` 137`  `    }`
` 138`  `}`

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
