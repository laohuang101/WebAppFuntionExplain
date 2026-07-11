# ResetPassword.aspx
**Source:** `Pages/Authentication/ResetPassword.aspx`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

One-shot TOTP + new password form (uses AuthService.ResetPasswordWithTotp).

## File overview

- **Total lines:** 59
- **Kind:** `.aspx`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

```html
   1 | <%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ResetPassword.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.ResetPassword" %>
   2 | 
   3 | <!DOCTYPE html>
   4 | <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
   5 | <head runat="server">
   6 |     <meta charset="utf-8" />
   7 |     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   8 |     <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
   9 |     <title>EduLMS - Reset password</title>
  10 |     <meta name="viewport" content="width=device-width, initial-scale=1" />
  11 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  12 |     <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />
  13 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  14 | </head>
  15 | <body>
  16 |     <form id="form1" runat="server">
  17 |         <div class="container d-flex justify-content-center align-items-center vh-100">
  18 |             <div class="card card-auth p-4 w-100" style="max-width: 400px;">
  19 |                 <div class="text-center mb-3">
  20 |                     <i class="fa-solid fa-lock-open fa-2x" style="color:#f17f54;"></i>
  21 |                     <h3 class="mt-2 fw-bold">Set new password</h3>
  22 |                     <p class="text-muted small mb-0">
  23 |                         Prove identity with your <strong>authenticator MFA code</strong>, then choose a new password.
  24 |                     </p>
  25 |                 </div>
  26 | 
  27 |                 <div class="mb-3">
  28 |                     <label class="form-label small fw-semibold text-muted">Email</label>
  29 |                     <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email"></asp:TextBox>
  30 |                 </div>
  31 |                 <div class="mb-3">
  32 |                     <label class="form-label small fw-semibold text-muted">Authenticator code (MFA)</label>
  33 |                     <asp:TextBox ID="txtCode" runat="server" CssClass="form-control text-center"
  34 |                         MaxLength="8" placeholder="000000" autocomplete="one-time-code"
  35 |                         style="letter-spacing:.3em;font-weight:700;font-size:1.15rem;"></asp:TextBox>
  36 |                 </div>
  37 |                 <div class="mb-3">
  38 |                     <label class="form-label small fw-semibold text-muted">New password</label>
  39 |                     <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password" placeholder="Min 8 chars, letters + numbers"></asp:TextBox>
  40 |                 </div>
  41 |                 <div class="mb-3">
  42 |                     <label class="form-label small fw-semibold text-muted">Confirm password</label>
  43 |                     <asp:TextBox ID="txtPassword2" runat="server" CssClass="form-control" TextMode="Password"></asp:TextBox>
  44 |                 </div>
  45 | 
  46 |                 <asp:Button ID="btnReset" runat="server" Text="Update password" CssClass="btn btn-accent w-100 text-white"
  47 |                     OnClick="btnReset_Click" />
  48 |                 <asp:Label ID="lblMsg" runat="server" CssClass="d-block mt-3 text-center small"></asp:Label>
  49 | 
  50 |                 <div class="text-center mt-3">
  51 |                     <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>" class="small text-decoration-none" style="color:#f17f54;">Back to login</a>
  52 |                     ·
  53 |                     <a href="<%= ResolveUrl("~/Pages/Authentication/ForgotPassword.aspx") %>" class="small text-decoration-none text-muted">Forgot password</a>
  54 |                 </div>
  55 |             </div>
  56 |         </div>
  57 |     </form>
  58 | </body>
  59 | </html>
```

**Line notes**

- **L8:** CSRF anti-forgery protection.

## Source snapshot (raw)

```html
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ResetPassword.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.ResetPassword" %>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta charset="utf-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
    <title>EduLMS - Reset password</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
</head>
<body>
    <form id="form1" runat="server">
        <div class="container d-flex justify-content-center align-items-center vh-100">
            <div class="card card-auth p-4 w-100" style="max-width: 400px;">
                <div class="text-center mb-3">
                    <i class="fa-solid fa-lock-open fa-2x" style="color:#f17f54;"></i>
                    <h3 class="mt-2 fw-bold">Set new password</h3>
                    <p class="text-muted small mb-0">
                        Prove identity with your <strong>authenticator MFA code</strong>, then choose a new password.
                    </p>
                </div>

                <div class="mb-3">
                    <label class="form-label small fw-semibold text-muted">Email</label>
                    <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email"></asp:TextBox>
                </div>
                <div class="mb-3">
                    <label class="form-label small fw-semibold text-muted">Authenticator code (MFA)</label>
                    <asp:TextBox ID="txtCode" runat="server" CssClass="form-control text-center"
                        MaxLength="8" placeholder="000000" autocomplete="one-time-code"
                        style="letter-spacing:.3em;font-weight:700;font-size:1.15rem;"></asp:TextBox>
                </div>
                <div class="mb-3">
                    <label class="form-label small fw-semibold text-muted">New password</label>
                    <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password" placeholder="Min 8 chars, letters + numbers"></asp:TextBox>
                </div>
                <div class="mb-3">
                    <label class="form-label small fw-semibold text-muted">Confirm password</label>
                    <asp:TextBox ID="txtPassword2" runat="server" CssClass="form-control" TextMode="Password"></asp:TextBox>
                </div>

                <asp:Button ID="btnReset" runat="server" Text="Update password" CssClass="btn btn-accent w-100 text-white"
                    OnClick="btnReset_Click" />
                <asp:Label ID="lblMsg" runat="server" CssClass="d-block mt-3 text-center small"></asp:Label>

                <div class="text-center mt-3">
                    <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>" class="small text-decoration-none" style="color:#f17f54;">Back to login</a>
                    ·
                    <a href="<%= ResolveUrl("~/Pages/Authentication/ForgotPassword.aspx") %>" class="small text-decoration-none text-muted">Forgot password</a>
                </div>
            </div>
        </div>
    </form>
</body>
</html>

```
