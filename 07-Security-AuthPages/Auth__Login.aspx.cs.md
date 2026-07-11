# Login.aspx.cs
**Source:** `Pages/Authentication/Login.aspx.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Email + password; Student/Lecturer redirected to MFA; Admin password-only complete login.

## File overview

- **Total lines:** 80
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 14:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 25:** `email` (`string`) — **Account email address (usually lowercased).**
- **Line 26:** `password` (`string`) — **Plain password from the form (never log this).**
- **Line 37:** `result` (`var`) — **AuthResult or API result { success, message, … }.**
- **Line 70:** `normalizedRole` (`string`) — **Holds “normalized Role” for this scope. (text)**

## Functions / methods (3 found)

### `Page_Load` — lines 10–21

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
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).

#### Line-by-line (this function)

```csharp
  10 |         protected void Page_Load(object sender, EventArgs e)
  11 |         {
  12 |             AuthSchema.Ensure();
  13 |             // Only treat as logged-in if UID still exists in Users (avoids stale JWT after DB reset)
  14 |             int uid = AuthService.GetValidatedUserId(Context);
  15 | 
  16 |             if (!IsPostBack && uid > 0)
  17 |             {
  18 |                 Logger.Info("User already logged in. Redirecting. " + uid + " " + Session["UserRole"]);
  19 |                 RedirectUser(Session["UserRole"] as string ?? "");
  20 |             }
  21 |         }
```

<<<<<<< HEAD
**Line notes**

- **L10:** Page load entry (GET or postback).
- **L14:** Restore/validate user from Session or JWT; reject stale UIDs.
=======
**Line notes** (what code + variables mean)

- **L10:** Page load entry (GET or postback).
- **L14:** Restore/validate user from Session or JWT; reject stale UIDs. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
>>>>>>> eb8ce01 (update)
- **L16:** False on first open; true after postback.
- **L18:** Server session for logged-in user.
- **L19:** Server session for logged-in user.

---

### `btnLogin_Click` — lines 22–66

```csharp
protected void btnLogin_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnLogin_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Navigation:** Redirects the browser.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `password` (`string`) — Plain password from the form (never log this).
- `result` (`var`) — AuthResult or API result { success, message, … }.

#### Line-by-line (this function)

```csharp
  22 | 
  23 |         protected void btnLogin_Click(object sender, EventArgs e)
  24 |         {
  25 |             string email = (txtEmail.Text ?? "").Trim();
  26 |             string password = txtPassword.Text ?? "";
  27 | 
  28 |             if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
  29 |             {
  30 |                 lblError.Text = "Please enter email and password.";
  31 |                 return;
  32 |             }
  33 | 
  34 |             try
  35 |             {
  36 |                 Logger.Info("Login attempt for: " + email);
  37 |                 var result = AuthService.LoginPassword(email, password);
  38 | 
  39 |                 if (!result.Success)
  40 |                 {
  41 |                     lblError.Text = result.Message ?? "Invalid email or password.";
  42 |                     Logger.Info("Login failed for: " + email);
  43 |                     return;
  44 |                 }
  45 | 
  46 |                 if (result.RequiresMfa)
  47 |                 {
  48 |                     Session["MfaPendingUid"] = result.User.UID;
  49 |                     Session["MfaMethod"] = result.MfaMethod ?? "totp";
  50 |                     if (!string.IsNullOrEmpty(result.DemoEmailOtp))
  51 |                     Session["MfaDemoOtp"] = result.DemoEmailOtp;
  52 |                     Response.Redirect("~/Pages/Authentication/MfaVerify.aspx", false);
  53 |                     Context.ApplicationInstance.CompleteRequest();
  54 |                     return;
  55 |                 }
  56 | 
  57 |                 AuthService.CompleteLogin(Context, result.User, result.Token);
  58 |                 Logger.Info("Authenticated user role: " + result.User.RoleNormalized);
  59 |                 RedirectUser(result.User.RoleNormalized);
  60 |             }
  61 |             catch (Exception ex)
  62 |             {
  63 |                 Logger.Error(ex, "Login failed");
  64 |                 lblError.Text = "Sign-in error. Please try again.";
  65 |             }
  66 |         }
```

<<<<<<< HEAD
**Line notes**

- **L34:** Error handling block.
=======
**Line notes** (what code + variables mean)

- **L25:** `email` means: Account email address (usually lowercased).
- **L26:** `password` means: Plain password from the form (never log this).
- **L34:** Error handling block.
- **L37:** `result` means: AuthResult or API result { success, message, … }.
>>>>>>> eb8ce01 (update)
- **L48:** Server session for logged-in user.
- **L49:** Server session for logged-in user.
- **L51:** Server session for logged-in user.
- **L52:** Navigate browser to another URL.
- **L57:** Issue Session + JWT after successful auth.
- **L61:** Handle/log exception.

---

### `RedirectUser` — lines 67–78

```csharp
private void RedirectUser(string role)
```

#### Explanation

- **Purpose:** Implements `RedirectUser`.
- **Navigation:** Redirects the browser.
- **Parameters (what each means):**
- `role` (`string`) — User role code or name (Admin/Student/Lecturer).
- **Local variables (what each means):**
- `normalizedRole` (`string`) — Holds “normalized Role” for this scope. (text)

#### Line-by-line (this function)

```csharp
  67 | 
  68 |         private void RedirectUser(string role)
  69 |         {
  70 |             string normalizedRole = AuthService.NormalizeRole(role).ToLowerInvariant();
  71 | 
  72 |             if (normalizedRole == "admin")
  73 |             Response.Redirect("~/Pages/Admin/ADashboard.aspx");
  74 |             else if (normalizedRole == "lecturer")
  75 |             Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");
  76 |             else
  77 |             Response.Redirect("~/Pages/Landing/Landing.aspx");
  78 |         }
```

<<<<<<< HEAD
**Line notes**

- **L70:** Map role codes/names to Admin/Student/Lecturer.
=======
**Line notes** (what code + variables mean)

- **L70:** Map role codes/names to Admin/Student/Lecturer. | `normalizedRole` means: Holds “normalized Role” for this scope. (text)
>>>>>>> eb8ce01 (update)
- **L73:** Navigate browser to another URL.
- **L75:** Navigate browser to another URL.
- **L77:** Navigate browser to another URL.

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

```csharp
   1 | using System;
   2 | using System.Web.UI;
   3 | using WebAppAssignment.Data.Security;
   4 | using WebAppAssignment.Shared.DebugLog;
   5 | 
   6 | namespace WebAppAssignment.Pages.Authentication
   7 | {
   8 |     public partial class Login : Page
   9 |     {
  10 |         protected void Page_Load(object sender, EventArgs e)
  11 |         {
  12 |             AuthSchema.Ensure();
  13 |             // Only treat as logged-in if UID still exists in Users (avoids stale JWT after DB reset)
  14 |             int uid = AuthService.GetValidatedUserId(Context);
  15 | 
  16 |             if (!IsPostBack && uid > 0)
  17 |             {
  18 |                 Logger.Info("User already logged in. Redirecting. " + uid + " " + Session["UserRole"]);
  19 |                 RedirectUser(Session["UserRole"] as string ?? "");
  20 |             }
  21 |         }
  22 | 
  23 |         protected void btnLogin_Click(object sender, EventArgs e)
  24 |         {
  25 |             string email = (txtEmail.Text ?? "").Trim();
  26 |             string password = txtPassword.Text ?? "";
  27 | 
  28 |             if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
  29 |             {
  30 |                 lblError.Text = "Please enter email and password.";
  31 |                 return;
  32 |             }
  33 | 
  34 |             try
  35 |             {
  36 |                 Logger.Info("Login attempt for: " + email);
  37 |                 var result = AuthService.LoginPassword(email, password);
  38 | 
  39 |                 if (!result.Success)
  40 |                 {
  41 |                     lblError.Text = result.Message ?? "Invalid email or password.";
  42 |                     Logger.Info("Login failed for: " + email);
  43 |                     return;
  44 |                 }
  45 | 
  46 |                 if (result.RequiresMfa)
  47 |                 {
  48 |                     Session["MfaPendingUid"] = result.User.UID;
  49 |                     Session["MfaMethod"] = result.MfaMethod ?? "totp";
  50 |                     if (!string.IsNullOrEmpty(result.DemoEmailOtp))
  51 |                     Session["MfaDemoOtp"] = result.DemoEmailOtp;
  52 |                     Response.Redirect("~/Pages/Authentication/MfaVerify.aspx", false);
  53 |                     Context.ApplicationInstance.CompleteRequest();
  54 |                     return;
  55 |                 }
  56 | 
  57 |                 AuthService.CompleteLogin(Context, result.User, result.Token);
  58 |                 Logger.Info("Authenticated user role: " + result.User.RoleNormalized);
  59 |                 RedirectUser(result.User.RoleNormalized);
  60 |             }
  61 |             catch (Exception ex)
  62 |             {
  63 |                 Logger.Error(ex, "Login failed");
  64 |                 lblError.Text = "Sign-in error. Please try again.";
  65 |             }
  66 |         }
  67 | 
  68 |         private void RedirectUser(string role)
  69 |         {
  70 |             string normalizedRole = AuthService.NormalizeRole(role).ToLowerInvariant();
  71 | 
  72 |             if (normalizedRole == "admin")
  73 |             Response.Redirect("~/Pages/Admin/ADashboard.aspx");
  74 |             else if (normalizedRole == "lecturer")
  75 |             Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");
  76 |             else
  77 |             Response.Redirect("~/Pages/Landing/Landing.aspx");
  78 |         }
  79 |     }
  80 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L6:** C# namespace grouping.
- **L10:** Page load entry (GET or postback).
<<<<<<< HEAD
- **L14:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L16:** False on first open; true after postback.
- **L18:** Server session for logged-in user.
- **L19:** Server session for logged-in user.
- **L34:** Error handling block.
=======
- **L14:** Restore/validate user from Session or JWT; reject stale UIDs. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous).
- **L16:** False on first open; true after postback.
- **L18:** Server session for logged-in user.
- **L19:** Server session for logged-in user.
- **L25:** `email` means: Account email address (usually lowercased).
- **L26:** `password` means: Plain password from the form (never log this).
- **L34:** Error handling block.
- **L37:** `result` means: AuthResult or API result { success, message, … }.
>>>>>>> eb8ce01 (update)
- **L48:** Server session for logged-in user.
- **L49:** Server session for logged-in user.
- **L51:** Server session for logged-in user.
- **L52:** Navigate browser to another URL.
- **L57:** Issue Session + JWT after successful auth.
- **L61:** Handle/log exception.
<<<<<<< HEAD
- **L70:** Map role codes/names to Admin/Student/Lecturer.
=======
- **L70:** Map role codes/names to Admin/Student/Lecturer. | `normalizedRole` means: Holds “normalized Role” for this scope. (text)
>>>>>>> eb8ce01 (update)
- **L73:** Navigate browser to another URL.
- **L75:** Navigate browser to another URL.
- **L77:** Navigate browser to another URL.

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
