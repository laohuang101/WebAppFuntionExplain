# Login.aspx.cs
**Source:** `Pages/Authentication/Login.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Email + password; Student/Lecturer redirected to MFA; Admin password-only complete login.

## File overview

- **Total lines:** 80
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (3 found)

### `Page_Load` — lines 10–21

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
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous). |

#### Code

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

---

### `btnLogin_Click` — lines 22–66

#### Signature

```csharp
protected void btnLogin_Click(object sender, EventArgs e)
```

#### What it is

Button handler: when the user clicks Login, check password and go to MFA or dashboard.

#### How it works

1. Read email and password from the text boxes.
2. If either is empty, show an error and stop.
3. Call AuthService.LoginPassword.
4. If login failed, show the error message.
5. If MFA is required, store MfaPendingUid in Session and redirect to MfaVerify.
6. Otherwise call CompleteLogin and redirect by role (Admin / Lecturer / Student).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `password` | `string` | Plain password from the form (never log this). |
| `result` | `var` | AuthResult or API result { success, message, … }. |

#### Code

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

---

### `RedirectUser` — lines 67–78

#### Signature

```csharp
private void RedirectUser(string role)
```

#### What it is

Function `RedirectUser` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. If the user is Admin, complete login without MFA; otherwise require MFA.
2. Redirect the browser to another page.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `normalizedRole` | `string` | Holds “normalized Role” for this scope. (text) |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
