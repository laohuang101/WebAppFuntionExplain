# MfaVerify.aspx
**Source:** `Pages/Authentication/MfaVerify.aspx`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Post-login TOTP (or demo email OTP) step before CompleteLogin issues session/JWT.

## File overview

- **Total lines:** 62
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="MfaVerify.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.MfaVerify" %>`
`   2`  ``
`   3`  `<!DOCTYPE html>`
`   4`  `<html xmlns="http://www.w3.org/1999/xhtml">`
`   5`  `  <head runat="server">`
`   6`  `    <meta charset="utf-8" />`
`   7`  `    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />`
`   8`  `    <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>`
  - → CSRF anti-forgery protection.
`   9`  `    <title>EduLMS - Verify identity</title>`
`  10`  `    <meta name="viewport" content="width=device-width, initial-scale=1" />`
`  11`  `    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />`
`  12`  `    <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />`
`  13`  `    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />`
`  14`  `    <style>`
`  15`  `      .otp-input { letter-spacing: .35em; font-size: 1.4rem; text-align: center; font-weight: 700; }`
`  16`  `      .demo-otp { background: #fff0eb; border-radius: 10px; padding: .75rem 1rem; font-size: .85rem; }`
`  17`  `    </style>`
`  18`  `</head>`
`  19`  `  <body>`
`  20`  `    <form id="form1" runat="server">`
`  21`  `      <div class="container d-flex justify-content-center align-items-center" style="min-height:100vh;">`
`  22`  `        <div class="card card-auth p-4 p-md-5 w-100" style="max-width:400px;">`
`  23`  `          <div class="text-center mb-4">`
`  24`  `            <i class="fa-solid fa-shield-halved fa-3x brand"></i>`
`  25`  `            <h3 class="mt-2 fw-bold">Two-factor verification</h3>`
`  26`  `            <p class="text-muted small mb-0">`
`  27`  `              <asp:Literal ID="litHint" runat="server" Text="Enter the 6-digit code from Google Authenticator." />`
`  28`  `            </p>`
`  29`  `          </div>`
`  30`  ``
`  31`  `          <asp:Panel ID="pnlDemoOtp" runat="server" Visible="false" CssClass="demo-otp mb-3">`
`  32`  `            <strong>Demo email OTP</strong> (no SMTP configured):`
`  33`  `            <div class="fs-4 fw-bold mt-1" style="color:#f17f54;letter-spacing:.2em;">`
`  34`  `              <asp:Literal ID="litDemoOtp" runat="server" />`
`  35`  `            </div>`
`  36`  `          </asp:Panel>`
`  37`  ``
`  38`  `          <div class="mb-3">`
`  39`  `            <asp:TextBox ID="txtCode" runat="server" CssClass="form-control otp-input"`
`  40`  `            MaxLength="8" placeholder="000000" autocomplete="one-time-code" inputmode="numeric" />`
`  41`  `          </div>`
`  42`  ``
`  43`  `          <asp:Button ID="btnVerify" runat="server" Text="Verify and continue"`
`  44`  `          CssClass="btn btn-accent w-100" OnClick="btnVerify_Click" />`
`  45`  ``
`  46`  `          <asp:Label ID="lblError" runat="server" CssClass="d-block mt-3 text-center text-danger small" />`
`  47`  ``
`  48`  `          <p class="text-muted small text-center mt-3 mb-0">`
`  49`  `            Codes refresh every 30 seconds. Phone date/time must be automatic.`
`  50`  `          </p>`
`  51`  ``
`  52`  `          <div class="text-center mt-3">`
`  53`  `            <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>" class="text-muted small text-decoration-none">`
`  54`  `              ← Back to login`
`  55`  `            </a>`
`  56`  `          </div>`
`  57`  `        </div>`
`  58`  `      </div>`
`  59`  `    </form>`
`  60`  `      <script src="<%= ResolveUrl("~/Shared/Scripts/csrf.js") %>"></script>`
  - → CSRF anti-forgery protection.
`  61`  `</body>`
`  62`  `</html>`

## Source snapshot (raw)

```html
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="MfaVerify.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.MfaVerify" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head runat="server">
    <meta charset="utf-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
    <title>EduLMS - Verify identity</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style>
      .otp-input { letter-spacing: .35em; font-size: 1.4rem; text-align: center; font-weight: 700; }
      .demo-otp { background: #fff0eb; border-radius: 10px; padding: .75rem 1rem; font-size: .85rem; }
    </style>
</head>
  <body>
    <form id="form1" runat="server">
      <div class="container d-flex justify-content-center align-items-center" style="min-height:100vh;">
        <div class="card card-auth p-4 p-md-5 w-100" style="max-width:400px;">
          <div class="text-center mb-4">
            <i class="fa-solid fa-shield-halved fa-3x brand"></i>
            <h3 class="mt-2 fw-bold">Two-factor verification</h3>
            <p class="text-muted small mb-0">
              <asp:Literal ID="litHint" runat="server" Text="Enter the 6-digit code from Google Authenticator." />
            </p>
          </div>

          <asp:Panel ID="pnlDemoOtp" runat="server" Visible="false" CssClass="demo-otp mb-3">
            <strong>Demo email OTP</strong> (no SMTP configured):
            <div class="fs-4 fw-bold mt-1" style="color:#f17f54;letter-spacing:.2em;">
              <asp:Literal ID="litDemoOtp" runat="server" />
            </div>
          </asp:Panel>

          <div class="mb-3">
            <asp:TextBox ID="txtCode" runat="server" CssClass="form-control otp-input"
            MaxLength="8" placeholder="000000" autocomplete="one-time-code" inputmode="numeric" />
          </div>

          <asp:Button ID="btnVerify" runat="server" Text="Verify and continue"
          CssClass="btn btn-accent w-100" OnClick="btnVerify_Click" />

          <asp:Label ID="lblError" runat="server" CssClass="d-block mt-3 text-center text-danger small" />

          <p class="text-muted small text-center mt-3 mb-0">
            Codes refresh every 30 seconds. Phone date/time must be automatic.
          </p>

          <div class="text-center mt-3">
            <a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>" class="text-muted small text-decoration-none">
              ← Back to login
            </a>
          </div>
        </div>
      </div>
    </form>
      <script src="<%= ResolveUrl("~/Shared/Scripts/csrf.js") %>"></script>
</body>
</html>

```
