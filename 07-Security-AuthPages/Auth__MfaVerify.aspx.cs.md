# MfaVerify.aspx.cs
**Source:** `Pages/Authentication/MfaVerify.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Post-login TOTP (or demo email OTP) step before CompleteLogin issues session/JWT.

## File overview

- **Total lines:** 66
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (3 found)

### `Page_Load` — lines 9–30

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. Save temporary state in Session (`Session["MfaPendingUid"]`).
2. Redirect the browser to another page.
3. Save temporary state in Session (`Session["MfaMethod"] as string ?? "totp";`).
4. Save temporary state in Session (`Session["MfaDemoOtp"] !`).
5. Save temporary state in Session (`Session["MfaDemoOtp"].ToString();`).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `method` | `string` | HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session. |

#### Code

```csharp
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             if (Session["MfaPendingUid"] == null)
  12 |             {
  13 |                 Response.Redirect("~/Pages/Authentication/Login.aspx");
  14 |                 return;
  15 |             }
  16 | 
  17 |             if (!IsPostBack)
  18 |             {
  19 |                 string method = Session["MfaMethod"] as string ?? "totp";
  20 |                 if (method == "email")
  21 |                 {
  22 |                     litHint.Text = "Enter the one-time code for your email.";
  23 |                     if (Session["MfaDemoOtp"] != null)
  24 |                     {
  25 |                         pnlDemoOtp.Visible = true;
  26 |                         litDemoOtp.Text = Session["MfaDemoOtp"].ToString();
  27 |                     }
  28 |                 }
  29 |             }
  30 |         }
```

---

### `btnVerify_Click` — lines 31–53

#### Signature

```csharp
protected void btnVerify_Click(object sender, EventArgs e)
```

#### What it is

Button handler: verify MFA or password-reset code and continue to the next step.

#### How it works

1. Save temporary state in Session (`Session["MfaPendingUid"]);`).
2. Save temporary state in Session (`Session["MfaMethod"] as string ?? "totp";`).
3. Clear Session data (logout or end of multi-step flow).
4. Finish sign-in: write Session (UserID, UserName, UserRole) and set the JWT cookie.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session. |
| `method` | `string` | HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session. |
| `code` | `string` | 6-digit TOTP / OTP the user typed. |
| `result` | `var` | AuthResult or API result { success, message, … }.  Assigned from verification boolean/result. |

#### Code

```csharp
  31 | 
  32 |         protected void btnVerify_Click(object sender, EventArgs e)
  33 |         {
  34 |             lblError.Text = "";
  35 |             int uid = Convert.ToInt32(Session["MfaPendingUid"]);
  36 |             string method = Session["MfaMethod"] as string ?? "totp";
  37 |             string code = (txtCode.Text ?? "").Trim();
  38 | 
  39 |             var result = AuthService.VerifyMfa(uid, code, method);
  40 |             if (!result.Success)
  41 |             {
  42 |                 lblError.Text = result.Message;
  43 |                 return;
  44 |             }
  45 | 
  46 |             // Clear MFA pending state
  47 |             Session.Remove("MfaPendingUid");
  48 |             Session.Remove("MfaMethod");
  49 |             Session.Remove("MfaDemoOtp");
  50 | 
  51 |             AuthService.CompleteLogin(Context, result.User, result.Token);
  52 |             RedirectUser(result.User.RoleNormalized);
  53 |         }
```

---

### `RedirectUser` — lines 54–64

#### Signature

```csharp
private void RedirectUser(string role)
```

#### What it is

Function `RedirectUser` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Redirect the browser to another page.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `r` | `string` | Usually one database row (DataRow) in query loops. |

#### Code

```csharp
  54 | 
  55 |         private void RedirectUser(string role)
  56 |         {
  57 |             string r = (role ?? "").ToLowerInvariant();
  58 |             if (r == "admin")
  59 |             Response.Redirect("~/Pages/Admin/ADashboard.aspx");
  60 |             else if (r == "lecturer")
  61 |             Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");
  62 |             else
  63 |             Response.Redirect("~/Pages/Landing/Landing.aspx");
  64 |         }
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
   7 |     public partial class MfaVerify : Page
   8 |     {
   9 |         protected void Page_Load(object sender, EventArgs e)
  10 |         {
  11 |             if (Session["MfaPendingUid"] == null)
  12 |             {
  13 |                 Response.Redirect("~/Pages/Authentication/Login.aspx");
  14 |                 return;
  15 |             }
  16 | 
  17 |             if (!IsPostBack)
  18 |             {
  19 |                 string method = Session["MfaMethod"] as string ?? "totp";
  20 |                 if (method == "email")
  21 |                 {
  22 |                     litHint.Text = "Enter the one-time code for your email.";
  23 |                     if (Session["MfaDemoOtp"] != null)
  24 |                     {
  25 |                         pnlDemoOtp.Visible = true;
  26 |                         litDemoOtp.Text = Session["MfaDemoOtp"].ToString();
  27 |                     }
  28 |                 }
  29 |             }
  30 |         }
  31 | 
  32 |         protected void btnVerify_Click(object sender, EventArgs e)
  33 |         {
  34 |             lblError.Text = "";
  35 |             int uid = Convert.ToInt32(Session["MfaPendingUid"]);
  36 |             string method = Session["MfaMethod"] as string ?? "totp";
  37 |             string code = (txtCode.Text ?? "").Trim();
  38 | 
  39 |             var result = AuthService.VerifyMfa(uid, code, method);
  40 |             if (!result.Success)
  41 |             {
  42 |                 lblError.Text = result.Message;
  43 |                 return;
  44 |             }
  45 | 
  46 |             // Clear MFA pending state
  47 |             Session.Remove("MfaPendingUid");
  48 |             Session.Remove("MfaMethod");
  49 |             Session.Remove("MfaDemoOtp");
  50 | 
  51 |             AuthService.CompleteLogin(Context, result.User, result.Token);
  52 |             RedirectUser(result.User.RoleNormalized);
  53 |         }
  54 | 
  55 |         private void RedirectUser(string role)
  56 |         {
  57 |             string r = (role ?? "").ToLowerInvariant();
  58 |             if (r == "admin")
  59 |             Response.Redirect("~/Pages/Admin/ADashboard.aspx");
  60 |             else if (r == "lecturer")
  61 |             Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");
  62 |             else
  63 |             Response.Redirect("~/Pages/Landing/Landing.aspx");
  64 |         }
  65 |     }
  66 | }
```
