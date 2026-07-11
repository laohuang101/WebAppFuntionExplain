# Login.aspx.cs
**Source:** `Pages/Authentication/Login.aspx.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Email + password; Student/Lecturer redirected to MFA; Admin password-only complete login.

## File overview

- **Total lines:** 80
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 14:** `uid` — type `int`
- **Line 25:** `email` — type `string`
- **Line 26:** `password` — type `string`
- **Line 37:** `result` — type `var`
- **Line 70:** `normalizedRole` — type `string`

## Functions / methods (3 found)

### `Page_Load` — lines 10–21

```
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Session:** Reads/writes ASP.NET Session.
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters:** `object sender, EventArgs e`
- **Local variables:** `uid`

#### Line-by-line (this function)

`  10`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  11`  `        {`
`  12`  `            AuthSchema.Ensure();`
`  13`  `            // Only treat as logged-in if UID still exists in Users (avoids stale JWT after DB reset)`
`  14`  `            int uid = AuthService.GetValidatedUserId(Context);`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
`  15`  ``
`  16`  `            if (!IsPostBack && uid > 0)`
  - → False on first open; true after postback.
`  17`  `            {`
`  18`  `                Logger.Info("User already logged in. Redirecting. " + uid + " " + Session["UserRole"]);`
  - → Server session for logged-in user.
`  19`  `                RedirectUser(Session["UserRole"] as string ?? "");`
  - → Server session for logged-in user.
`  20`  `            }`
`  21`  `        }`

---

### `btnLogin_Click` — lines 22–66

```
protected void btnLogin_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnLogin_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Navigation:** Redirects the browser.
- **Parameters:** `object sender, EventArgs e`
- **Local variables:** `email`, `password`, `result`

#### Line-by-line (this function)

`  22`  ``
`  23`  `        protected void btnLogin_Click(object sender, EventArgs e)`
`  24`  `        {`
`  25`  `            string email = (txtEmail.Text ?? "").Trim();`
`  26`  `            string password = txtPassword.Text ?? "";`
`  27`  ``
`  28`  `            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))`
`  29`  `            {`
`  30`  `                lblError.Text = "Please enter email and password.";`
`  31`  `                return;`
`  32`  `            }`
`  33`  ``
`  34`  `            try`
  - → Error handling block.
`  35`  `            {`
`  36`  `                Logger.Info("Login attempt for: " + email);`
`  37`  `                var result = AuthService.LoginPassword(email, password);`
`  38`  ``
`  39`  `                if (!result.Success)`
`  40`  `                {`
`  41`  `                    lblError.Text = result.Message ?? "Invalid email or password.";`
`  42`  `                    Logger.Info("Login failed for: " + email);`
`  43`  `                    return;`
`  44`  `                }`
`  45`  ``
`  46`  `                if (result.RequiresMfa)`
`  47`  `                {`
`  48`  `                    Session["MfaPendingUid"] = result.User.UID;`
  - → Server session for logged-in user.
`  49`  `                    Session["MfaMethod"] = result.MfaMethod ?? "totp";`
  - → Server session for logged-in user.
`  50`  `                    if (!string.IsNullOrEmpty(result.DemoEmailOtp))`
`  51`  `                    Session["MfaDemoOtp"] = result.DemoEmailOtp;`
  - → Server session for logged-in user.
`  52`  `                    Response.Redirect("~/Pages/Authentication/MfaVerify.aspx", false);`
  - → Navigate browser to another URL.
`  53`  `                    Context.ApplicationInstance.CompleteRequest();`
`  54`  `                    return;`
`  55`  `                }`
`  56`  ``
`  57`  `                AuthService.CompleteLogin(Context, result.User, result.Token);`
  - → Issue Session + JWT after successful auth.
`  58`  `                Logger.Info("Authenticated user role: " + result.User.RoleNormalized);`
`  59`  `                RedirectUser(result.User.RoleNormalized);`
`  60`  `            }`
`  61`  `            catch (Exception ex)`
  - → Handle/log exception.
`  62`  `            {`
`  63`  `                Logger.Error(ex, "Login failed");`
`  64`  `                lblError.Text = "Sign-in error. Please try again.";`
`  65`  `            }`
`  66`  `        }`

---

### `RedirectUser` — lines 67–78

```
private void RedirectUser(string role)
```

#### Explanation

- **Purpose:** Implements `RedirectUser`.
- **Navigation:** Redirects the browser.
- **Parameters:** `string role`
- **Local variables:** `normalizedRole`

#### Line-by-line (this function)

`  67`  ``
`  68`  `        private void RedirectUser(string role)`
`  69`  `        {`
`  70`  `            string normalizedRole = AuthService.NormalizeRole(role).ToLowerInvariant();`
  - → Map role codes/names to Admin/Student/Lecturer.
`  71`  ``
`  72`  `            if (normalizedRole == "admin")`
`  73`  `            Response.Redirect("~/Pages/Admin/ADashboard.aspx");`
  - → Navigate browser to another URL.
`  74`  `            else if (normalizedRole == "lecturer")`
`  75`  `            Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");`
  - → Navigate browser to another URL.
`  76`  `            else`
`  77`  `            Response.Redirect("~/Pages/Landing/Landing.aspx");`
  - → Navigate browser to another URL.
`  78`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Web.UI;`
  - → Import namespace/types.
`   3`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`   4`  `using WebAppAssignment.Shared.DebugLog;`
  - → Import namespace/types.
`   5`  ``
`   6`  `namespace WebAppAssignment.Pages.Authentication`
  - → C# namespace grouping.
`   7`  `{`
`   8`  `    public partial class Login : Page`
`   9`  `    {`
`  10`  `        protected void Page_Load(object sender, EventArgs e)`
  - → Page load entry (GET or postback).
`  11`  `        {`
`  12`  `            AuthSchema.Ensure();`
`  13`  `            // Only treat as logged-in if UID still exists in Users (avoids stale JWT after DB reset)`
`  14`  `            int uid = AuthService.GetValidatedUserId(Context);`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
`  15`  ``
`  16`  `            if (!IsPostBack && uid > 0)`
  - → False on first open; true after postback.
`  17`  `            {`
`  18`  `                Logger.Info("User already logged in. Redirecting. " + uid + " " + Session["UserRole"]);`
  - → Server session for logged-in user.
`  19`  `                RedirectUser(Session["UserRole"] as string ?? "");`
  - → Server session for logged-in user.
`  20`  `            }`
`  21`  `        }`
`  22`  ``
`  23`  `        protected void btnLogin_Click(object sender, EventArgs e)`
`  24`  `        {`
`  25`  `            string email = (txtEmail.Text ?? "").Trim();`
`  26`  `            string password = txtPassword.Text ?? "";`
`  27`  ``
`  28`  `            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))`
`  29`  `            {`
`  30`  `                lblError.Text = "Please enter email and password.";`
`  31`  `                return;`
`  32`  `            }`
`  33`  ``
`  34`  `            try`
  - → Error handling block.
`  35`  `            {`
`  36`  `                Logger.Info("Login attempt for: " + email);`
`  37`  `                var result = AuthService.LoginPassword(email, password);`
`  38`  ``
`  39`  `                if (!result.Success)`
`  40`  `                {`
`  41`  `                    lblError.Text = result.Message ?? "Invalid email or password.";`
`  42`  `                    Logger.Info("Login failed for: " + email);`
`  43`  `                    return;`
`  44`  `                }`
`  45`  ``
`  46`  `                if (result.RequiresMfa)`
`  47`  `                {`
`  48`  `                    Session["MfaPendingUid"] = result.User.UID;`
  - → Server session for logged-in user.
`  49`  `                    Session["MfaMethod"] = result.MfaMethod ?? "totp";`
  - → Server session for logged-in user.
`  50`  `                    if (!string.IsNullOrEmpty(result.DemoEmailOtp))`
`  51`  `                    Session["MfaDemoOtp"] = result.DemoEmailOtp;`
  - → Server session for logged-in user.
`  52`  `                    Response.Redirect("~/Pages/Authentication/MfaVerify.aspx", false);`
  - → Navigate browser to another URL.
`  53`  `                    Context.ApplicationInstance.CompleteRequest();`
`  54`  `                    return;`
`  55`  `                }`
`  56`  ``
`  57`  `                AuthService.CompleteLogin(Context, result.User, result.Token);`
  - → Issue Session + JWT after successful auth.
`  58`  `                Logger.Info("Authenticated user role: " + result.User.RoleNormalized);`
`  59`  `                RedirectUser(result.User.RoleNormalized);`
`  60`  `            }`
`  61`  `            catch (Exception ex)`
  - → Handle/log exception.
`  62`  `            {`
`  63`  `                Logger.Error(ex, "Login failed");`
`  64`  `                lblError.Text = "Sign-in error. Please try again.";`
`  65`  `            }`
`  66`  `        }`
`  67`  ``
`  68`  `        private void RedirectUser(string role)`
`  69`  `        {`
`  70`  `            string normalizedRole = AuthService.NormalizeRole(role).ToLowerInvariant();`
  - → Map role codes/names to Admin/Student/Lecturer.
`  71`  ``
`  72`  `            if (normalizedRole == "admin")`
`  73`  `            Response.Redirect("~/Pages/Admin/ADashboard.aspx");`
  - → Navigate browser to another URL.
`  74`  `            else if (normalizedRole == "lecturer")`
`  75`  `            Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");`
  - → Navigate browser to another URL.
`  76`  `            else`
`  77`  `            Response.Redirect("~/Pages/Landing/Landing.aspx");`
  - → Navigate browser to another URL.
`  78`  `        }`
`  79`  `    }`
`  80`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.Web.UI;
using WebAppAssignment.Data.Security;
using WebAppAssignment.Shared.DebugLog;

namespace WebAppAssignment.Pages.Authentication
{
    public partial class Login : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            AuthSchema.Ensure();
            // Only treat as logged-in if UID still exists in Users (avoids stale JWT after DB reset)
            int uid = AuthService.GetValidatedUserId(Context);

            if (!IsPostBack && uid > 0)
            {
                Logger.Info("User already logged in. Redirecting. " + uid + " " + Session["UserRole"]);
                RedirectUser(Session["UserRole"] as string ?? "");
            }
        }

        protected void btnLogin_Click(object sender, EventArgs e)
        {
            string email = (txtEmail.Text ?? "").Trim();
            string password = txtPassword.Text ?? "";

            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
            {
                lblError.Text = "Please enter email and password.";
                return;
            }

            try
            {
                Logger.Info("Login attempt for: " + email);
                var result = AuthService.LoginPassword(email, password);

                if (!result.Success)
                {
                    lblError.Text = result.Message ?? "Invalid email or password.";
                    Logger.Info("Login failed for: " + email);
                    return;
                }

                if (result.RequiresMfa)
                {
                    Session["MfaPendingUid"] = result.User.UID;
                    Session["MfaMethod"] = result.MfaMethod ?? "totp";
                    if (!string.IsNullOrEmpty(result.DemoEmailOtp))
                    Session["MfaDemoOtp"] = result.DemoEmailOtp;
                    Response.Redirect("~/Pages/Authentication/MfaVerify.aspx", false);
                    Context.ApplicationInstance.CompleteRequest();
                    return;
                }

                AuthService.CompleteLogin(Context, result.User, result.Token);
                Logger.Info("Authenticated user role: " + result.User.RoleNormalized);
                RedirectUser(result.User.RoleNormalized);
            }
            catch (Exception ex)
            {
                Logger.Error(ex, "Login failed");
                lblError.Text = "Sign-in error. Please try again.";
            }
        }

        private void RedirectUser(string role)
        {
            string normalizedRole = AuthService.NormalizeRole(role).ToLowerInvariant();

            if (normalizedRole == "admin")
            Response.Redirect("~/Pages/Admin/ADashboard.aspx");
            else if (normalizedRole == "lecturer")
            Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");
            else
            Response.Redirect("~/Pages/Landing/Landing.aspx");
        }
    }
}

```
