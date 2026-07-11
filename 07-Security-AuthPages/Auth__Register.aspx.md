# Register.aspx
**Source:** `Pages/Authentication/Register.aspx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Two-step: form → Session pending → QR/MFA confirm → only then INSERT user.

## File overview

- **Total lines:** 131
- **Kind:** `.aspx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See the code listing at the bottom._

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Register.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.Register" %>
   2 | 
   3 | <!DOCTYPE html>
   4 | <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
   5 | <head runat="server">
   6 |     <meta charset="utf-8" />
   7 |     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   8 |     <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
   9 |     <title>EduLMS - Register</title>
  10 |     <meta name="viewport" content="width=device-width, initial-scale=1" />
  11 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  12 |     <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />
  13 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  14 |     <style type="text/css">
  15 |         .step { font-weight: 700; color: #f17f54; margin-right: .25rem; }
  16 |         .secret-box {
  17 |             font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  18 |             letter-spacing: .08em; word-break: break-all;
  19 |             background: #f9fafb; border-radius: 8px; padding: .5rem .75rem;
  20 |         }
  21 |         .hint { font-size: .75rem; color: #6b7280; }
  22 |     </style>
  23 | </head>
  24 | <body>
  25 |     <form id="form1" runat="server">
  26 |         <div class="container d-flex justify-content-center align-items-center" style="min-height:100vh;padding:1.5rem 0;">
  27 |             <div class="card card-auth p-4 w-100" style="max-width: 420px;">
  28 | 
  29 |                 <%-- STEP 1: account form — nothing written to DB yet --%>
  30 |                 <asp:Panel ID="pnlForm" runat="server">
  31 |                     <div class="text-center mb-3">
  32 |                         <i class="fa-solid fa-user-plus fa-2x" style="color:#f17f54;"></i>
  33 |                         <h3 class="mt-2 fw-bold">Create account</h3>
  34 |                         <p class="text-muted small mb-0">Student or Lecturer · password + MFA required</p>
  35 |                     </div>
  36 | 
  37 |                     <div class="mb-3">
  38 |                         <label class="form-label d-block small fw-semibold text-muted">I am a…</label>
  39 |                         <asp:RadioButtonList ID="rblRole" runat="server" RepeatDirection="Horizontal" CssClass="form-check">
  40 |                             <asp:ListItem Text="Student" Value="Student" Selected="True" />
  41 |                             <asp:ListItem Text="Lecturer" Value="Lecturer" />
  42 |                         </asp:RadioButtonList>
  43 |                     </div>
  44 |                     <div class="mb-3">
  45 |                         <label class="form-label small fw-semibold text-muted">Full name</label>
  46 |                         <asp:TextBox ID="txtName" runat="server" CssClass="form-control" placeholder="Your name"></asp:TextBox>
  47 |                     </div>
  48 |                     <div class="mb-3">
  49 |                         <label class="form-label small fw-semibold text-muted">Email</label>
  50 |                         <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" TextMode="Email" placeholder="you@example.com"></asp:TextBox>
  51 |                     </div>
  52 |                     <div class="mb-3">
  53 |                         <label class="form-label small fw-semibold text-muted">Password</label>
  54 |                         <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password" placeholder="Min 8 chars, letters + numbers"></asp:TextBox>
  55 |                     </div>
  56 |                     <div class="mb-3">
  57 |                         <label class="form-label small fw-semibold text-muted">Confirm password</label>
  58 |                         <asp:TextBox ID="txtConfirm" runat="server" CssClass="form-control" TextMode="Password"></asp:TextBox>
  59 |                     </div>
  60 |                     <asp:Button ID="btnRegister" runat="server" Text="Continue to MFA setup"
  61 |                         CssClass="btn btn-accent w-100 text-white" OnClick="btnRegister_Click" />
  62 |                     <asp:Label ID="lblError" runat="server" CssClass="d-block mt-3 text-center text-danger small"></asp:Label>
  63 |                     <p class="hint text-center mt-2 mb-0">
  64 |                         Your account is only created after you confirm the authenticator code.
  65 |                     </p>
  66 |                     <div class="text-center mt-3">
  67 |                         <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>" class="small" style="color:#f17f54;">Already have an account? Login</a>
  68 |                     </div>
  69 |                 </asp:Panel>
  70 | 
  71 |                 <%-- STEP 2: MFA setup — still no DB row until Confirm --%>
  72 |                 <asp:Panel ID="pnlMfaSetup" runat="server" Visible="false">
  73 |                     <div class="text-center mb-2">
  74 |                         <i class="fa-solid fa-shield-halved fa-2x" style="color:#f17f54;"></i>
  75 |                         <h3 class="mt-2 fw-bold">Set up authenticator</h3>
  76 |                         <p class="text-muted small mb-0">
  77 |                             Account is <strong>not created yet</strong>. Scan the QR, then enter a code to finish.
  78 |                         </p>
  79 |                     </div>
  80 | 
  81 |                     <p class="small mb-2"><span class="step">1.</span> Scan with <strong>Google Authenticator</strong> (or Authy):</p>
  82 |                     <div class="text-center mb-3">
  83 |                         <asp:Image ID="imgQr" runat="server" Width="200" Height="200" CssClass="img-fluid border rounded" />
  84 |                     </div>
  85 | 
  86 |                     <p class="small mb-1"><span class="step">2.</span> Or type this key manually:</p>
  87 |                     <div class="secret-box text-center mb-3">
  88 |                         <asp:Literal ID="litMfaSecret" runat="server" Mode="Encode" />
  89 |                     </div>
  90 |                     <asp:HiddenField ID="hidMfaSecret" runat="server" />
  91 |                     <asp:HiddenField ID="hidMfaEmail" runat="server" />
  92 | 
  93 |                     <p class="small mb-2"><span class="step">3.</span> Enter the <strong>current 6-digit code</strong> from your app:</p>
  94 |                     <div class="mb-3">
  95 |                         <asp:TextBox ID="txtSetupCode" runat="server" CssClass="form-control text-center"
  96 |                             MaxLength="8" placeholder="000000" autocomplete="one-time-code"
  97 |                             style="letter-spacing:.3em;font-weight:700;font-size:1.15rem;"></asp:TextBox>
  98 |                         <div class="form-text hint">Codes refresh every 30 seconds. Phone time must be automatic.</div>
  99 |                     </div>
 100 | 
 101 |                     <asp:Button ID="btnConfirmMfa" runat="server" Text="Confirm MFA and create account"
 102 |                         CssClass="btn btn-accent w-100 text-white" OnClick="btnConfirmMfa_Click" />
 103 |                     <asp:Label ID="lblMfaError" runat="server" CssClass="d-block mt-3 text-center text-danger small"></asp:Label>
 104 | 
 105 |                     <div class="text-center mt-3">
 106 |                         <asp:LinkButton ID="lnkCancelMfa" runat="server" CssClass="small text-muted text-decoration-none"
 107 |                             OnClick="lnkCancelMfa_Click" CausesValidation="false">
 108 |                             Cancel — discard setup (no account will be saved)
 109 |                         </asp:LinkButton>
 110 |                     </div>
 111 |                 </asp:Panel>
 112 | 
 113 |                 <%-- Done — account exists only after step 2 succeeded --%>
 114 |                 <asp:Panel ID="pnlDone" runat="server" Visible="false">
 115 |                     <div class="text-center">
 116 |                         <i class="fa-solid fa-circle-check fa-3x text-success"></i>
 117 |                         <h3 class="mt-3 fw-bold">You are all set</h3>
 118 |                         <p class="text-muted small">
 119 |                             <asp:Literal ID="litDoneMsg" runat="server" />
 120 |                         </p>
 121 |                         <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>"
 122 |                            class="btn btn-accent text-white mt-2">Go to login</a>
 123 |                     </div>
 124 |                 </asp:Panel>
 125 | 
 126 |             </div>
 127 |         </div>
 128 |     </form>
 129 |     <script src="<%= ResolveUrl("~/Shared/Scripts/csrf.js") %>"></script>
 130 | </body>
 131 | </html>
```
