# ForgotPassword.aspx.cs
**Source:** `Pages/Authentication/ForgotPassword.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Two-step reset: verify email+TOTP first, then set new password (session window).

## File overview

- **Total lines:** 155
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `ResetWindow` | `TimeSpan` | Holds “Reset Window” for this scope. (type `TimeSpan`) |

## Functions / methods (9 found)

### `Page_Load` — lines 13–36

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. Make sure a CSRF token exists in Session (create one if missing).
2. Read the logged-in user id from Session/JWT (0 means not signed in).
3. Redirect the browser to another page.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `btnVerify_Click` — lines 39–62

#### Signature

```csharp
protected void btnVerify_Click(object sender, EventArgs e)
```

#### What it is

Button handler: verify MFA or password-reset code and continue to the next step.

#### How it works

1. Verify email + authenticator code for password reset (step 1).
2. Save temporary state in Session (`Session[SessUid]`).
3. Save temporary state in Session (`Session[SessEmail]`).
4. Save temporary state in Session (`Session[SessAt]`).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `result` | `var` | AuthResult or API result { success, message, … }.  Assigned from verification boolean/result. |

#### Code

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

---

### `btnReset_Click` — lines 65–102

#### Signature

```csharp
protected void btnReset_Click(object sender, EventArgs e)
```

#### What it is

Button handler: save the new password after MFA was already verified.

#### How it works

1. Save temporary state in Session (`Session[SessUid]);`).
2. Update the user’s password hash (step 2 of reset).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `p1` | `string` | New password field (first entry). |
| `p2` | `string` | Confirm password field (must match p1). |
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Read from ASP.NET Session. |
| `result` | `var` | AuthResult or API result { success, message, … }. |

#### Code

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

---

### `lnkBack_Click` — lines 103–111

#### Signature

```csharp
protected void lnkBack_Click(object sender, EventArgs e)
```

#### What it is

Function `lnkBack_Click` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `lnkBack_Click`.
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

#### Signature

```csharp
private bool HasValidResetSession()
```

#### What it is

Checks a condition related to **Has Valid Reset Session** and returns true/false (or tries an action safely).

#### How it works

1. Save temporary state in Session (`Session[SessUid]`).
2. Save temporary state in Session (`Session[SessAt];`).
3. Return `true` to the caller.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `at` | `var` | Timestamp (CreatedUtc / PwdResetAt).  Read from ASP.NET Session. |

#### Code

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

---

### `ClearResetSession` — lines 125–131

#### Signature

```csharp
private void ClearResetSession()
```

#### What it is

Deletes or clears **Clear Reset Session** (data or temporary state).

#### How it works

1. Clear Session data (logout or end of multi-step flow).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

#### Signature

```csharp
private void ShowStep1()
```

#### What it is

Updates the page HTML for **Show Step1**.

#### How it works

1. Starts when something calls `ShowStep1`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

#### Signature

```csharp
private void ShowStep2()
```

#### What it is

Updates the page HTML for **Show Step2**.

#### How it works

1. Save temporary state in Session (`Session[SessEmail] as string ?? "";`).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `UpdatePills` — lines 147–153

#### Signature

```csharp
private void UpdatePills()
```

#### What it is

Saves or updates **Update Pills** in the database or UI state.

#### How it works

1. Starts when something calls `UpdatePills`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `on2` | `bool` | Holds “on2” for this scope. (true/false) |

#### Code

```csharp
 147 | 
 148 |         private void UpdatePills()
 149 |         {
 150 |             bool on2 = pnlStep2.Visible;
 151 |             pill1.Attributes["class"] = "step-pill" + (on2 ? " done" : " active");
 152 |             pill2.Attributes["class"] = "step-pill" + (on2 ? " active" : "");
 153 |         }
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
