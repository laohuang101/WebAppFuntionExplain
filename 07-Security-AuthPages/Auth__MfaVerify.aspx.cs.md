# MfaVerify.aspx.cs
**Source:** `Pages/Authentication/MfaVerify.aspx.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Post-login TOTP (or demo email OTP) step before CompleteLogin issues session/JWT.

## File overview

- **Total lines:** 66
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 19:** `method` (`string`) — **HTTP method (GET/POST) or MFA method (totp/email).**
- **Line 35:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 36:** `method` (`string`) — **HTTP method (GET/POST) or MFA method (totp/email).**
- **Line 37:** `code` (`string`) — **6-digit TOTP / OTP the user typed.**
- **Line 38:** `result` (`var`) — **AuthResult or API result { success, message, … }.**
- **Line 57:** `r` (`string`) — **Usually one database row (DataRow) in query loops.**

## Functions / methods (3 found)

### `Page_Load` — lines 9–30

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
- `method` (`string`) — HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L9:** Page load entry (GET or postback).
- **L11:** Server session for logged-in user.
- **L13:** Navigate browser to another URL.
- **L17:** False on first open; true after postback.
- **L19:** Server session for logged-in user. | `method` means: HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session.
- **L23:** Server session for logged-in user.
- **L26:** Server session for logged-in user.

---

### `btnVerify_Click` — lines 31–53

```csharp
protected void btnVerify_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnVerify_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Navigation:** Redirects the browser.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session.
- `method` (`string`) — HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session.
- `code` (`string`) — 6-digit TOTP / OTP the user typed.
- `result` (`var`) — AuthResult or API result { success, message, … }.  Assigned from verification boolean/result.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L35:** Server session for logged-in user. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session.
- **L36:** Server session for logged-in user. | `method` means: HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session.
- **L37:** `code` means: 6-digit TOTP / OTP the user typed.
- **L39:** Verify multi-factor / TOTP code. | `result` means: AuthResult or API result { success, message, … }.  Assigned from verification boolean/result.
- **L51:** Issue Session + JWT after successful auth.

---

### `RedirectUser` — lines 54–64

```csharp
private void RedirectUser(string role)
```

#### Explanation

- **Purpose:** Implements `RedirectUser`.
- **Navigation:** Redirects the browser.
- **Parameters (what each means):**
- `role` (`string`) — User role code or name (Admin/Student/Lecturer).
- **Local variables (what each means):**
- `r` (`string`) — Usually one database row (DataRow) in query loops.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L57:** `r` means: Usually one database row (DataRow) in query loops.
- **L59:** Navigate browser to another URL.
- **L61:** Navigate browser to another URL.
- **L63:** Navigate browser to another URL.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L9:** Page load entry (GET or postback).
- **L11:** Server session for logged-in user.
- **L13:** Navigate browser to another URL.
- **L17:** False on first open; true after postback.
- **L19:** Server session for logged-in user. | `method` means: HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session.
- **L23:** Server session for logged-in user.
- **L26:** Server session for logged-in user.
- **L35:** Server session for logged-in user. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session.
- **L36:** Server session for logged-in user. | `method` means: HTTP method (GET/POST) or MFA method (totp/email).  Read from ASP.NET Session.
- **L37:** `code` means: 6-digit TOTP / OTP the user typed.
- **L39:** Verify multi-factor / TOTP code. | `result` means: AuthResult or API result { success, message, … }.  Assigned from verification boolean/result.
- **L51:** Issue Session + JWT after successful auth.
- **L57:** `r` means: Usually one database row (DataRow) in query loops.
- **L59:** Navigate browser to another URL.
- **L61:** Navigate browser to another URL.
- **L63:** Navigate browser to another URL.

## Source snapshot (raw)

```csharp
using System;
using System.Web.UI;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Authentication
{
    public partial class MfaVerify : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (Session["MfaPendingUid"] == null)
            {
                Response.Redirect("~/Pages/Authentication/Login.aspx");
                return;
            }

            if (!IsPostBack)
            {
                string method = Session["MfaMethod"] as string ?? "totp";
                if (method == "email")
                {
                    litHint.Text = "Enter the one-time code for your email.";
                    if (Session["MfaDemoOtp"] != null)
                    {
                        pnlDemoOtp.Visible = true;
                        litDemoOtp.Text = Session["MfaDemoOtp"].ToString();
                    }
                }
            }
        }

        protected void btnVerify_Click(object sender, EventArgs e)
        {
            lblError.Text = "";
            int uid = Convert.ToInt32(Session["MfaPendingUid"]);
            string method = Session["MfaMethod"] as string ?? "totp";
            string code = (txtCode.Text ?? "").Trim();

            var result = AuthService.VerifyMfa(uid, code, method);
            if (!result.Success)
            {
                lblError.Text = result.Message;
                return;
            }

            // Clear MFA pending state
            Session.Remove("MfaPendingUid");
            Session.Remove("MfaMethod");
            Session.Remove("MfaDemoOtp");

            AuthService.CompleteLogin(Context, result.User, result.Token);
            RedirectUser(result.User.RoleNormalized);
        }

        private void RedirectUser(string role)
        {
            string r = (role ?? "").ToLowerInvariant();
            if (r == "admin")
            Response.Redirect("~/Pages/Admin/ADashboard.aspx");
            else if (r == "lecturer")
            Response.Redirect("~/Pages/Lecturer/Dashboard.aspx");
            else
            Response.Redirect("~/Pages/Landing/Landing.aspx");
        }
    }
}

```
