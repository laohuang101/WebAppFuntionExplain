# ResetPassword.aspx.cs
**Source:** `Pages/Authentication/ResetPassword.aspx.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

One-shot TOTP + new password form (uses AuthService.ResetPasswordWithTotp).

## File overview

- **Total lines:** 44
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 15:** `email` (`string`) — **Account email address (usually lowercased).**
- **Line 24:** `p1` (`string`) — **New password field (first entry).**
- **Line 25:** `p2` (`string`) — **Confirm password field (must match p1).**
- **Line 31:** `result` (`var`) — **AuthResult or API result { success, message, … }.**

## Functions / methods (2 found)

### `Page_Load` — lines 9–19

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `email` (`string`) — Account email address (usually lowercased).  Comes from HTTP request.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L9:** Page load entry (GET or postback).
- **L12:** CSRF anti-forgery protection.
- **L13:** False on first open; true after postback.
<<<<<<< HEAD
=======
- **L15:** `email` means: Account email address (usually lowercased).  Comes from HTTP request.
>>>>>>> eb8ce01 (update)

---

### `btnReset_Click` — lines 20–42

```csharp
protected void btnReset_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnReset_Click`.
- **Navigation:** Redirects the browser.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `p1` (`string`) — New password field (first entry).
- `p2` (`string`) — Confirm password field (must match p1).
- `result` (`var`) — AuthResult or API result { success, message, … }.

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L24:** `p1` means: New password field (first entry).
- **L25:** `p2` means: Confirm password field (must match p1).
- **L32:** `result` means: AuthResult or API result { success, message, … }.
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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L9:** Page load entry (GET or postback).
- **L12:** CSRF anti-forgery protection.
- **L13:** False on first open; true after postback.
<<<<<<< HEAD
=======
- **L15:** `email` means: Account email address (usually lowercased).  Comes from HTTP request.
- **L24:** `p1` means: New password field (first entry).
- **L25:** `p2` means: Confirm password field (must match p1).
- **L32:** `result` means: AuthResult or API result { success, message, … }.
>>>>>>> eb8ce01 (update)

## Source snapshot (raw)

```csharp
using System;
using System.Web.UI;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Authentication
{
    public partial class ResetPassword : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            AuthSchema.Ensure();
            CsrfProtection.EnsureToken(Context);
            if (!IsPostBack)
            {
                string email = Request.QueryString["email"];
                if (!string.IsNullOrEmpty(email))
                    txtEmail.Text = email.Trim();
            }
        }

        protected void btnReset_Click(object sender, EventArgs e)
        {
            lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
            string p1 = txtPassword.Text ?? "";
            string p2 = txtPassword2.Text ?? "";
            if (p1 != p2)
            {
                lblMsg.Text = "Passwords do not match.";
                return;
            }

            var result = AuthService.ResetPasswordWithTotp(txtEmail.Text, txtCode.Text, p1);
            if (!result.Success)
            {
                lblMsg.Text = result.Message ?? "Could not reset password.";
                return;
            }

            lblMsg.CssClass = "d-block mt-3 text-center small text-success";
            lblMsg.Text = result.Message + " Redirecting to login…";
            Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));
        }
    }
}

```
