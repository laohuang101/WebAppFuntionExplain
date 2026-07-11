# ForgotPassword.aspx.cs
**Source:** `Pages/Authentication/ForgotPassword.aspx.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Two-step reset: verify email+TOTP first, then set new password (session window).

## File overview

- **Total lines:** 155
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 12:** `ResetWindow` (`TimeSpan`) — **Holds “Reset Window” for this scope. (type `TimeSpan`)**
- **Line 43:** `result` (`var`) — **AuthResult or API result { success, message, … }.**
- **Line 77:** `p1` (`string`) — **New password field (first entry).**
- **Line 79:** `p2` (`string`) — **Confirm password field (must match p1).**
- **Line 86:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 88:** `result` (`var`) — **AuthResult or API result { success, message, … }.**
- **Line 118:** `at` (`var`) — **Timestamp (CreatedUtc / PwdResetAt).**
- **Line 121:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 150:** `on2` (`bool`) — **Holds “on2” for this scope. (true/false)**

## Functions / methods (9 found)

### `Page_Load` — lines 13–36

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Session:** Reads/writes ASP.NET Session.
- **Navigation:** Redirects the browser.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

```csharp
  13 | 
  14 |         protected void Page_Load(object sender, EventArgs e)
  15 |         {
  16 |             AuthSchema.Ensure();
  17 |             CsrfProtection.EnsureToken(Context);
  18 | 
  19 |             if (!IsPostBack && AuthService.GetValidatedUserId(Context) > 0)
  20 |             {
  21 |                 Response.Redirect("~/Pages/Landing/Landing.aspx");
  22 |                 return;
  23 |             }
  24 | 
  25 |             if (!IsPostBack)
  26 |             {
  27 |                 if (HasValidResetSession())
  28 |                     ShowStep2();
  29 |                 else
  30 |                     ShowStep1();
  31 |             }
  32 |             else
  33 |             {
  34 |                 UpdatePills();
  35 |             }
  36 |         }
```

**Line notes** (what code + variables mean)

- **L14:** Page load entry (GET or postback).
- **L17:** CSRF anti-forgery protection.
- **L19:** False on first open; true after postback.
- **L21:** Navigate browser to another URL.
- **L25:** False on first open; true after postback.

---

### `btnVerify_Click` — lines 39–62

```csharp
protected void btnVerify_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnVerify_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `result` (`var`) — AuthResult or API result { success, message, … }.  Assigned from verification boolean/result.

#### Line-by-line (this function)

```csharp
  39 |         protected void btnVerify_Click(object sender, EventArgs e)
  40 |         {
  41 |             lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
  42 |             lblMsg.Text = "";
  43 | 
  44 |             var result = AuthService.VerifyMfaForPasswordReset(txtEmail.Text, txtMfaCode.Text);
  45 |             if (!result.Success || result.User == null)
  46 |             {
  47 |                 // Message may include debug HTML when compilation debug=true
  48 |                 lblMsg.Text = result.Message ?? "Could not verify MFA.";
  49 |                 ShowStep1();
  50 |                 return;
  51 |             }
  52 | 
  53 |             Session[SessUid] = result.User.UID;
  54 |             Session[SessEmail] = result.User.Email
  55 |                 ?? (txtEmail.Text ?? "").Trim().ToLowerInvariant();
  56 |             Session[SessAt] = DateTime.UtcNow;
  57 | 
  58 |             txtMfaCode.Text = "";
  59 |             ShowStep2();
  60 |             lblMsg.CssClass = "d-block mt-3 text-center small text-success";
  61 |             lblMsg.Text = result.Message ?? "MFA verified. Set your new password below.";
  62 |         }
```

**Line notes** (what code + variables mean)

- **L44:** Verify multi-factor / TOTP code. | `result` means: AuthResult or API result { success, message, … }.  Assigned from verification boolean/result.
- **L53:** Server session for logged-in user.
- **L54:** Server session for logged-in user.
- **L56:** Server session for logged-in user.

---

### `btnReset_Click` — lines 65–102

```csharp
protected void btnReset_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `btnReset_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).
- **Local variables (what each means):**
- `p1` (`string`) — New password field (first entry).
- `p2` (`string`) — Confirm password field (must match p1).
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session.
- `result` (`var`) — AuthResult or API result { success, message, … }.

#### Line-by-line (this function)

```csharp
  65 |         protected void btnReset_Click(object sender, EventArgs e)
  66 |         {
  67 |             lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
  68 |             lblMsg.Text = "";
  69 | 
  70 |             if (!HasValidResetSession())
  71 |             {
  72 |                 ClearResetSession();
  73 |                 ShowStep1();
  74 |                 lblMsg.Text = "Session expired. Verify MFA again.";
  75 |                 return;
  76 |             }
  77 | 
  78 |             string p1 = txtPassword.Text ?? "";
  79 |             string p2 = txtPassword2.Text ?? "";
  80 |             if (p1 != p2)
  81 |             {
  82 |                 lblMsg.Text = "Passwords do not match.";
  83 |                 ShowStep2();
  84 |                 return;
  85 |             }
  86 | 
  87 |             int uid = Convert.ToInt32(Session[SessUid]);
  88 |             var result = AuthService.CompletePasswordReset(uid, p1);
  89 |             if (!result.Success)
  90 |             {
  91 |                 lblMsg.Text = result.Message ?? "Could not update password.";
  92 |                 ShowStep2();
  93 |                 return;
  94 |             }
  95 | 
  96 |             ClearResetSession();
  97 |             pnlStep1.Visible = false;
  98 |             pnlStep2.Visible = false;
  99 |             lblMsg.CssClass = "d-block mt-3 text-center small text-success";
 100 |             lblMsg.Text = result.Message + " Redirecting to login…";
 101 |             Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));
 102 |         }
```

**Line notes** (what code + variables mean)

- **L78:** `p1` means: New password field (first entry).
- **L79:** `p2` means: Confirm password field (must match p1).
- **L87:** Server session for logged-in user. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session.
- **L88:** Password-reset MFA then update password hash. | `result` means: AuthResult or API result { success, message, … }.

---

### `lnkBack_Click` — lines 103–111

```csharp
protected void lnkBack_Click(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `lnkBack_Click`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

```csharp
 103 | 
 104 |         protected void lnkBack_Click(object sender, EventArgs e)
 105 |         {
 106 |             ClearResetSession();
 107 |             ShowStep1();
 108 |             lblMsg.Text = "";
 109 |             txtPassword.Text = "";
 110 |             txtPassword2.Text = "";
 111 |         }
```

---

### `HasValidResetSession` — lines 112–124

```csharp
private bool HasValidResetSession()
```

#### Explanation

- **Purpose:** Implements `HasValidResetSession`.
- **Session:** Reads/writes ASP.NET Session.
- **Local variables (what each means):**
- `at` (`var`) — Timestamp (CreatedUtc / PwdResetAt).  Read from ASP.NET Session.

#### Line-by-line (this function)

```csharp
 112 | 
 113 |         private bool HasValidResetSession()
 114 |         {
 115 |             if (Session[SessUid] == null || Session[SessAt] == null) return false;
 116 |             try
 117 |             {
 118 |                 var at = (DateTime)Session[SessAt];
 119 |                 if (DateTime.UtcNow - at > ResetWindow) return false;
 120 |                 Convert.ToInt32(Session[SessUid]);
 121 |                 return true;
 122 |             }
 123 |             catch { return false; }
 124 |         }
```

**Line notes** (what code + variables mean)

- **L115:** Server session for logged-in user.
- **L116:** Error handling block.
- **L118:** Server session for logged-in user. | `at` means: Timestamp (CreatedUtc / PwdResetAt).  Read from ASP.NET Session.
- **L120:** Server session for logged-in user.
- **L123:** Handle/log exception.

---

### `ClearResetSession` — lines 125–131

```csharp
private void ClearResetSession()
```

#### Explanation

- **Purpose:** Implements `ClearResetSession`.
- **Session:** Reads/writes ASP.NET Session.
- **Pattern:** Delete/clear data.

#### Line-by-line (this function)

```csharp
 125 | 
 126 |         private void ClearResetSession()
 127 |         {
 128 |             Session.Remove(SessUid);
 129 |             Session.Remove(SessEmail);
 130 |             Session.Remove(SessAt);
 131 |         }
```

---

### `ShowStep1` — lines 132–138

```csharp
private void ShowStep1()
```

#### Explanation

- **Purpose:** Implements `ShowStep1`.

#### Line-by-line (this function)

```csharp
 132 | 
 133 |         private void ShowStep1()
 134 |         {
 135 |             pnlStep1.Visible = true;
 136 |             pnlStep2.Visible = false;
 137 |             UpdatePills();
 138 |         }
```

---

### `ShowStep2` — lines 139–146

```csharp
private void ShowStep2()
```

#### Explanation

- **Purpose:** Implements `ShowStep2`.
- **Session:** Reads/writes ASP.NET Session.

#### Line-by-line (this function)

```csharp
 139 | 
 140 |         private void ShowStep2()
 141 |         {
 142 |             pnlStep1.Visible = false;
 143 |             pnlStep2.Visible = true;
 144 |             litVerifiedEmail.Text = Session[SessEmail] as string ?? "";
 145 |             UpdatePills();
 146 |         }
```

**Line notes** (what code + variables mean)

- **L144:** Server session for logged-in user.

---

### `UpdatePills` — lines 147–153

```csharp
private void UpdatePills()
```

#### Explanation

- **Purpose:** Implements `UpdatePills`.
- **Pattern:** Persist changes.
- **Local variables (what each means):**
- `on2` (`bool`) — Holds “on2” for this scope. (true/false)

#### Line-by-line (this function)

```csharp
 147 | 
 148 |         private void UpdatePills()
 149 |         {
 150 |             bool on2 = pnlStep2.Visible;
 151 |             pill1.Attributes["class"] = "step-pill" + (on2 ? " done" : " active");
 152 |             pill2.Attributes["class"] = "step-pill" + (on2 ? " active" : "");
 153 |         }
```

**Line notes** (what code + variables mean)

- **L150:** `on2` means: Holds “on2” for this scope. (true/false)

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
   7 |     public partial class ForgotPassword : Page
   8 |     {
   9 |         private const string SessUid = "PwdResetUid";
  10 |         private const string SessEmail = "PwdResetEmail";
  11 |         private const string SessAt = "PwdResetAt";
  12 |         private static readonly TimeSpan ResetWindow = TimeSpan.FromMinutes(10);
  13 | 
  14 |         protected void Page_Load(object sender, EventArgs e)
  15 |         {
  16 |             AuthSchema.Ensure();
  17 |             CsrfProtection.EnsureToken(Context);
  18 | 
  19 |             if (!IsPostBack && AuthService.GetValidatedUserId(Context) > 0)
  20 |             {
  21 |                 Response.Redirect("~/Pages/Landing/Landing.aspx");
  22 |                 return;
  23 |             }
  24 | 
  25 |             if (!IsPostBack)
  26 |             {
  27 |                 if (HasValidResetSession())
  28 |                     ShowStep2();
  29 |                 else
  30 |                     ShowStep1();
  31 |             }
  32 |             else
  33 |             {
  34 |                 UpdatePills();
  35 |             }
  36 |         }
  37 | 
  38 |         /// <summary>Step 1: verify email + MFA code only.</summary>
  39 |         protected void btnVerify_Click(object sender, EventArgs e)
  40 |         {
  41 |             lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
  42 |             lblMsg.Text = "";
  43 | 
  44 |             var result = AuthService.VerifyMfaForPasswordReset(txtEmail.Text, txtMfaCode.Text);
  45 |             if (!result.Success || result.User == null)
  46 |             {
  47 |                 // Message may include debug HTML when compilation debug=true
  48 |                 lblMsg.Text = result.Message ?? "Could not verify MFA.";
  49 |                 ShowStep1();
  50 |                 return;
  51 |             }
  52 | 
  53 |             Session[SessUid] = result.User.UID;
  54 |             Session[SessEmail] = result.User.Email
  55 |                 ?? (txtEmail.Text ?? "").Trim().ToLowerInvariant();
  56 |             Session[SessAt] = DateTime.UtcNow;
  57 | 
  58 |             txtMfaCode.Text = "";
  59 |             ShowStep2();
  60 |             lblMsg.CssClass = "d-block mt-3 text-center small text-success";
  61 |             lblMsg.Text = result.Message ?? "MFA verified. Set your new password below.";
  62 |         }
  63 | 
  64 |         /// <summary>Step 2: set new password (MFA already verified in session).</summary>
  65 |         protected void btnReset_Click(object sender, EventArgs e)
  66 |         {
  67 |             lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
  68 |             lblMsg.Text = "";
  69 | 
  70 |             if (!HasValidResetSession())
  71 |             {
  72 |                 ClearResetSession();
  73 |                 ShowStep1();
  74 |                 lblMsg.Text = "Session expired. Verify MFA again.";
  75 |                 return;
  76 |             }
  77 | 
  78 |             string p1 = txtPassword.Text ?? "";
  79 |             string p2 = txtPassword2.Text ?? "";
  80 |             if (p1 != p2)
  81 |             {
  82 |                 lblMsg.Text = "Passwords do not match.";
  83 |                 ShowStep2();
  84 |                 return;
  85 |             }
  86 | 
  87 |             int uid = Convert.ToInt32(Session[SessUid]);
  88 |             var result = AuthService.CompletePasswordReset(uid, p1);
  89 |             if (!result.Success)
  90 |             {
  91 |                 lblMsg.Text = result.Message ?? "Could not update password.";
  92 |                 ShowStep2();
  93 |                 return;
  94 |             }
  95 | 
  96 |             ClearResetSession();
  97 |             pnlStep1.Visible = false;
  98 |             pnlStep2.Visible = false;
  99 |             lblMsg.CssClass = "d-block mt-3 text-center small text-success";
 100 |             lblMsg.Text = result.Message + " Redirecting to login…";
 101 |             Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));
 102 |         }
 103 | 
 104 |         protected void lnkBack_Click(object sender, EventArgs e)
 105 |         {
 106 |             ClearResetSession();
 107 |             ShowStep1();
 108 |             lblMsg.Text = "";
 109 |             txtPassword.Text = "";
 110 |             txtPassword2.Text = "";
 111 |         }
 112 | 
 113 |         private bool HasValidResetSession()
 114 |         {
 115 |             if (Session[SessUid] == null || Session[SessAt] == null) return false;
 116 |             try
 117 |             {
 118 |                 var at = (DateTime)Session[SessAt];
 119 |                 if (DateTime.UtcNow - at > ResetWindow) return false;
 120 |                 Convert.ToInt32(Session[SessUid]);
 121 |                 return true;
 122 |             }
 123 |             catch { return false; }
 124 |         }
 125 | 
 126 |         private void ClearResetSession()
 127 |         {
 128 |             Session.Remove(SessUid);
 129 |             Session.Remove(SessEmail);
 130 |             Session.Remove(SessAt);
 131 |         }
 132 | 
 133 |         private void ShowStep1()
 134 |         {
 135 |             pnlStep1.Visible = true;
 136 |             pnlStep2.Visible = false;
 137 |             UpdatePills();
 138 |         }
 139 | 
 140 |         private void ShowStep2()
 141 |         {
 142 |             pnlStep1.Visible = false;
 143 |             pnlStep2.Visible = true;
 144 |             litVerifiedEmail.Text = Session[SessEmail] as string ?? "";
 145 |             UpdatePills();
 146 |         }
 147 | 
 148 |         private void UpdatePills()
 149 |         {
 150 |             bool on2 = pnlStep2.Visible;
 151 |             pill1.Attributes["class"] = "step-pill" + (on2 ? " done" : " active");
 152 |             pill2.Attributes["class"] = "step-pill" + (on2 ? " active" : "");
 153 |         }
 154 |     }
 155 | }
```

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L14:** Page load entry (GET or postback).
- **L17:** CSRF anti-forgery protection.
- **L19:** False on first open; true after postback.
- **L21:** Navigate browser to another URL.
- **L25:** False on first open; true after postback.
- **L44:** Verify multi-factor / TOTP code. | `result` means: AuthResult or API result { success, message, … }.  Assigned from verification boolean/result.
- **L53:** Server session for logged-in user.
- **L54:** Server session for logged-in user.
- **L56:** Server session for logged-in user.
- **L78:** `p1` means: New password field (first entry).
- **L79:** `p2` means: Confirm password field (must match p1).
- **L87:** Server session for logged-in user. | `uid` means: User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session.
- **L88:** Password-reset MFA then update password hash. | `result` means: AuthResult or API result { success, message, … }.
- **L115:** Server session for logged-in user.
- **L116:** Error handling block.
- **L118:** Server session for logged-in user. | `at` means: Timestamp (CreatedUtc / PwdResetAt).  Read from ASP.NET Session.
- **L120:** Server session for logged-in user.
- **L123:** Handle/log exception.
- **L144:** Server session for logged-in user.
- **L150:** `on2` means: Holds “on2” for this scope. (true/false)

## Source snapshot (raw)

```csharp
using System;
using System.Web.UI;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Pages.Authentication
{
    public partial class ForgotPassword : Page
    {
        private const string SessUid = "PwdResetUid";
        private const string SessEmail = "PwdResetEmail";
        private const string SessAt = "PwdResetAt";
        private static readonly TimeSpan ResetWindow = TimeSpan.FromMinutes(10);

        protected void Page_Load(object sender, EventArgs e)
        {
            AuthSchema.Ensure();
            CsrfProtection.EnsureToken(Context);

            if (!IsPostBack && AuthService.GetValidatedUserId(Context) > 0)
            {
                Response.Redirect("~/Pages/Landing/Landing.aspx");
                return;
            }

            if (!IsPostBack)
            {
                if (HasValidResetSession())
                    ShowStep2();
                else
                    ShowStep1();
            }
            else
            {
                UpdatePills();
            }
        }

        /// <summary>Step 1: verify email + MFA code only.</summary>
        protected void btnVerify_Click(object sender, EventArgs e)
        {
            lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
            lblMsg.Text = "";

            var result = AuthService.VerifyMfaForPasswordReset(txtEmail.Text, txtMfaCode.Text);
            if (!result.Success || result.User == null)
            {
                // Message may include debug HTML when compilation debug=true
                lblMsg.Text = result.Message ?? "Could not verify MFA.";
                ShowStep1();
                return;
            }

            Session[SessUid] = result.User.UID;
            Session[SessEmail] = result.User.Email
                ?? (txtEmail.Text ?? "").Trim().ToLowerInvariant();
            Session[SessAt] = DateTime.UtcNow;

            txtMfaCode.Text = "";
            ShowStep2();
            lblMsg.CssClass = "d-block mt-3 text-center small text-success";
            lblMsg.Text = result.Message ?? "MFA verified. Set your new password below.";
        }

        /// <summary>Step 2: set new password (MFA already verified in session).</summary>
        protected void btnReset_Click(object sender, EventArgs e)
        {
            lblMsg.CssClass = "d-block mt-3 text-center small text-danger";
            lblMsg.Text = "";

            if (!HasValidResetSession())
            {
                ClearResetSession();
                ShowStep1();
                lblMsg.Text = "Session expired. Verify MFA again.";
                return;
            }

            string p1 = txtPassword.Text ?? "";
            string p2 = txtPassword2.Text ?? "";
            if (p1 != p2)
            {
                lblMsg.Text = "Passwords do not match.";
                ShowStep2();
                return;
            }

            int uid = Convert.ToInt32(Session[SessUid]);
            var result = AuthService.CompletePasswordReset(uid, p1);
            if (!result.Success)
            {
                lblMsg.Text = result.Message ?? "Could not update password.";
                ShowStep2();
                return;
            }

            ClearResetSession();
            pnlStep1.Visible = false;
            pnlStep2.Visible = false;
            lblMsg.CssClass = "d-block mt-3 text-center small text-success";
            lblMsg.Text = result.Message + " Redirecting to login…";
            Response.AddHeader("Refresh", "2;url=" + ResolveUrl("~/Pages/Authentication/Login.aspx"));
        }

        protected void lnkBack_Click(object sender, EventArgs e)
        {
            ClearResetSession();
            ShowStep1();
            lblMsg.Text = "";
            txtPassword.Text = "";
            txtPassword2.Text = "";
        }

        private bool HasValidResetSession()
        {
            if (Session[SessUid] == null || Session[SessAt] == null) return false;
            try
            {
                var at = (DateTime)Session[SessAt];
                if (DateTime.UtcNow - at > ResetWindow) return false;
                Convert.ToInt32(Session[SessUid]);
                return true;
            }
            catch { return false; }
        }

        private void ClearResetSession()
        {
            Session.Remove(SessUid);
            Session.Remove(SessEmail);
            Session.Remove(SessAt);
        }

        private void ShowStep1()
        {
            pnlStep1.Visible = true;
            pnlStep2.Visible = false;
            UpdatePills();
        }

        private void ShowStep2()
        {
            pnlStep1.Visible = false;
            pnlStep2.Visible = true;
            litVerifiedEmail.Text = Session[SessEmail] as string ?? "";
            UpdatePills();
        }

        private void UpdatePills()
        {
            bool on2 = pnlStep2.Visible;
            pill1.Attributes["class"] = "step-pill" + (on2 ? " done" : " active");
            pill2.Attributes["class"] = "step-pill" + (on2 ? " active" : "");
        }
    }
}

```
