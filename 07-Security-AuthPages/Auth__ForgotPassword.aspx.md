# ForgotPassword.aspx
**Source:** `Pages/Authentication/ForgotPassword.aspx`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Two-step reset: verify email+TOTP first, then set new password (session window).

## File overview

- **Total lines:** 113
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
   1 | <%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ForgotPassword.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.ForgotPassword" %>
   2 | 
   3 | <!DOCTYPE html>
   4 | <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
   5 | <head runat="server">
   6 |     <meta charset="utf-8" />
   7 |     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   8 |     <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
   9 |     <title>EduLMS - Forgot password</title>
  10 |     <meta name="viewport" content="width=device-width, initial-scale=1" />
  11 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  12 |     <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />
  13 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  14 |     <style type="text/css">
  15 |         .step-pill {
  16 |             display: inline-flex; align-items: center; gap: 0.35rem;
  17 |             font-size: 0.75rem; font-weight: 600; color: #9ca3af;
  18 |         }
  19 |         .step-pill .n {
  20 |             width: 22px; height: 22px; border-radius: 50%;
  21 |             background: #f3f4f6; color: #6b7280;
  22 |             display: inline-flex; align-items: center; justify-content: center;
  23 |             font-size: 0.7rem;
  24 |         }
  25 |         .step-pill.active { color: #f17f54; }
  26 |         .step-pill.active .n { background: #fff0eb; color: #f17f54; }
  27 |         .step-pill.done { color: #10b981; }
  28 |         .step-pill.done .n { background: #ecfdf5; color: #10b981; }
  29 |     </style>
  30 | </head>
  31 | <body>
  32 |     <form id="form1" runat="server">
  33 |         <div class="container d-flex justify-content-center align-items-center vh-100">
  34 |             <div class="card card-auth p-4 w-100" style="max-width: 400px;">
  35 |                 <div class="text-center mb-2">
  36 |                     <i class="fa-solid fa-key fa-2x" style="color:#f17f54;"></i>
  37 |                     <h3 class="mt-2 fw-bold">Forgot password</h3>
  38 |                 </div>
  39 | 
  40 |                 <div class="d-flex justify-content-center gap-3 mb-3">
  41 |                     <span id="pill1" runat="server" class="step-pill active">
  42 |                         <span class="n">1</span> Verify MFA
  43 |                     </span>
  44 |                     <span id="pill2" runat="server" class="step-pill">
  45 |                         <span class="n">2</span> New password
  46 |                     </span>
  47 |                 </div>
  48 | 
  49 |                 <%-- STEP 1: email + authenticator code --%>
  50 |                 <asp:Panel ID="pnlStep1" runat="server">
  51 |                     <p class="text-muted small text-center mb-3">
  52 |                         Open <strong>Google Authenticator</strong> now and type the
  53 |                         <strong>live 6-digit code</strong> for EduLMS (it changes every 30 seconds).
  54 |                     </p>
  55 |                     <div class="alert alert-warning py-2 px-3 small mb-3" role="alert">
  56 |                         Use a <strong>live code from Google Authenticator</strong> for this account
  57 |                         (same entry you scanned at register). Codes change every 30s.
  58 |                         If codes from your app never work: the app entry is for a
  59 |                         <strong>different secret</strong> (old QR / DB reseed) — delete it,
  60 |                         register again, and scan the new QR. Wait until the app matches the
  61 |                         server code on the register page before confirming.
  62 |                     </div>
  63 |                     <div class="mb-3">
  64 |                         <label class="form-label small fw-semibold text-muted">Account email</label>
  65 |                         <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email"
  66 |                             placeholder="you@example.com"></asp:TextBox>
  67 |                     </div>
  68 |                     <div class="mb-3">
  69 |                         <label class="form-label small fw-semibold text-muted">Current authenticator code</label>
  70 |                         <asp:TextBox ID="txtMfaCode" runat="server" CssClass="form-control text-center"
  71 |                             MaxLength="8" placeholder="000000" autocomplete="one-time-code"
  72 |                             style="letter-spacing:.3em;font-weight:700;font-size:1.15rem;"></asp:TextBox>
  73 |                         <div class="form-text small">Same app entry you use at login — not the setup code you wrote down.</div>
  74 |                     </div>
  75 |                     <asp:Button ID="btnVerify" runat="server" Text="Verify MFA and continue"
  76 |                         CssClass="btn btn-accent w-100 text-white" OnClick="btnVerify_Click" />
  77 |                 </asp:Panel>
  78 | 
  79 |                 <%-- STEP 2: new password only (after MFA verified) --%>
  80 |                 <asp:Panel ID="pnlStep2" runat="server" Visible="false">
  81 |                     <p class="text-muted small text-center mb-2">
  82 |                         MFA verified for
  83 |                         <strong><asp:Literal ID="litVerifiedEmail" runat="server" Mode="Encode" /></strong>.
  84 |                         Choose a new password.
  85 |                     </p>
  86 |                     <div class="mb-3">
  87 |                         <label class="form-label small fw-semibold text-muted">New password</label>
  88 |                         <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password"
  89 |                             placeholder="Min 8 chars, letters + numbers"></asp:TextBox>
  90 |                     </div>
  91 |                     <div class="mb-3">
  92 |                         <label class="form-label small fw-semibold text-muted">Confirm new password</label>
  93 |                         <asp:TextBox ID="txtPassword2" runat="server" CssClass="form-control" TextMode="Password"></asp:TextBox>
  94 |                     </div>
  95 |                     <asp:Button ID="btnReset" runat="server" Text="Update password"
  96 |                         CssClass="btn btn-accent w-100 text-white" OnClick="btnReset_Click" />
  97 |                     <div class="text-center mt-2">
  98 |                         <asp:LinkButton ID="lnkBack" runat="server" CssClass="small text-muted text-decoration-none"
  99 |                             OnClick="lnkBack_Click" CausesValidation="false">Use a different account</asp:LinkButton>
 100 |                     </div>
 101 |                 </asp:Panel>
 102 | 
 103 |                 <asp:Label ID="lblMsg" runat="server" CssClass="d-block mt-3 text-center small"></asp:Label>
 104 | 
 105 |                 <div class="text-center mt-3">
 106 |                     <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>"
 107 |                        class="small text-decoration-none" style="color:#f17f54;">Back to login</a>
 108 |                 </div>
 109 |             </div>
 110 |         </div>
 111 |     </form>
 112 | </body>
 113 | </html>
```

**Line notes**

- **L8:** CSRF anti-forgery protection.

## Source snapshot (raw)

```html
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ForgotPassword.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.ForgotPassword" %>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta charset="utf-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
    <title>EduLMS - Forgot password</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style type="text/css">
        .step-pill {
            display: inline-flex; align-items: center; gap: 0.35rem;
            font-size: 0.75rem; font-weight: 600; color: #9ca3af;
        }
        .step-pill .n {
            width: 22px; height: 22px; border-radius: 50%;
            background: #f3f4f6; color: #6b7280;
            display: inline-flex; align-items: center; justify-content: center;
            font-size: 0.7rem;
        }
        .step-pill.active { color: #f17f54; }
        .step-pill.active .n { background: #fff0eb; color: #f17f54; }
        .step-pill.done { color: #10b981; }
        .step-pill.done .n { background: #ecfdf5; color: #10b981; }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div class="container d-flex justify-content-center align-items-center vh-100">
            <div class="card card-auth p-4 w-100" style="max-width: 400px;">
                <div class="text-center mb-2">
                    <i class="fa-solid fa-key fa-2x" style="color:#f17f54;"></i>
                    <h3 class="mt-2 fw-bold">Forgot password</h3>
                </div>

                <div class="d-flex justify-content-center gap-3 mb-3">
                    <span id="pill1" runat="server" class="step-pill active">
                        <span class="n">1</span> Verify MFA
                    </span>
                    <span id="pill2" runat="server" class="step-pill">
                        <span class="n">2</span> New password
                    </span>
                </div>

                <%-- STEP 1: email + authenticator code --%>
                <asp:Panel ID="pnlStep1" runat="server">
                    <p class="text-muted small text-center mb-3">
                        Open <strong>Google Authenticator</strong> now and type the
                        <strong>live 6-digit code</strong> for EduLMS (it changes every 30 seconds).
                    </p>
                    <div class="alert alert-warning py-2 px-3 small mb-3" role="alert">
                        Use a <strong>live code from Google Authenticator</strong> for this account
                        (same entry you scanned at register). Codes change every 30s.
                        If codes from your app never work: the app entry is for a
                        <strong>different secret</strong> (old QR / DB reseed) — delete it,
                        register again, and scan the new QR. Wait until the app matches the
                        server code on the register page before confirming.
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-semibold text-muted">Account email</label>
                        <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email"
                            placeholder="you@example.com"></asp:TextBox>
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-semibold text-muted">Current authenticator code</label>
                        <asp:TextBox ID="txtMfaCode" runat="server" CssClass="form-control text-center"
                            MaxLength="8" placeholder="000000" autocomplete="one-time-code"
                            style="letter-spacing:.3em;font-weight:700;font-size:1.15rem;"></asp:TextBox>
                        <div class="form-text small">Same app entry you use at login — not the setup code you wrote down.</div>
                    </div>
                    <asp:Button ID="btnVerify" runat="server" Text="Verify MFA and continue"
                        CssClass="btn btn-accent w-100 text-white" OnClick="btnVerify_Click" />
                </asp:Panel>

                <%-- STEP 2: new password only (after MFA verified) --%>
                <asp:Panel ID="pnlStep2" runat="server" Visible="false">
                    <p class="text-muted small text-center mb-2">
                        MFA verified for
                        <strong><asp:Literal ID="litVerifiedEmail" runat="server" Mode="Encode" /></strong>.
                        Choose a new password.
                    </p>
                    <div class="mb-3">
                        <label class="form-label small fw-semibold text-muted">New password</label>
                        <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password"
                            placeholder="Min 8 chars, letters + numbers"></asp:TextBox>
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-semibold text-muted">Confirm new password</label>
                        <asp:TextBox ID="txtPassword2" runat="server" CssClass="form-control" TextMode="Password"></asp:TextBox>
                    </div>
                    <asp:Button ID="btnReset" runat="server" Text="Update password"
                        CssClass="btn btn-accent w-100 text-white" OnClick="btnReset_Click" />
                    <div class="text-center mt-2">
                        <asp:LinkButton ID="lnkBack" runat="server" CssClass="small text-muted text-decoration-none"
                            OnClick="lnkBack_Click" CausesValidation="false">Use a different account</asp:LinkButton>
                    </div>
                </asp:Panel>

                <asp:Label ID="lblMsg" runat="server" CssClass="d-block mt-3 text-center small"></asp:Label>

                <div class="text-center mt-3">
                    <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>"
                       class="small text-decoration-none" style="color:#f17f54;">Back to login</a>
                </div>
            </div>
        </div>
    </form>
</body>
</html>

```
