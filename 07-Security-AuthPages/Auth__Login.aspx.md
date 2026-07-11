# Login.aspx
**Source:** `Pages/Authentication/Login.aspx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Email + password; Student/Lecturer redirected to MFA; Admin password-only complete login.

## File overview

- **Total lines:** 66
- **Kind:** `.aspx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See the code listing at the bottom._

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Login.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.Login" %>
   2 | 
   3 | <!DOCTYPE html>
   4 | <html xmlns="http://www.w3.org/1999/xhtml">
   5 |   <head runat="server">
   6 |     <meta charset="utf-8" />
   7 |     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   8 |     <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
   9 |     <title>EduLMS - Login</title>
  10 |     <meta name="viewport" content="width=device-width, initial-scale=1" />
  11 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  12 |     <link href="<%= ResolveUrl("~/Shared/Style/auth.css") %>" rel="stylesheet" />
  13 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  14 |     </head>
  15 |   <body>
  16 |     <form id="form1" runat="server">
  17 |       <div class="container d-flex justify-content-center align-items-center vh-100">
  18 |         <div class="card card-auth p-4 w-100" style="max-width: 380px;">
  19 |           <div class="text-center mb-4">
  20 |             <a href="<%= ResolveUrl("~/Pages/Landing/Landing.aspx") %>" class="text-decoration-none">
  21 |               <i class="fa-solid fa-graduation-cap fa-3x" style="color: #f17f54 !important;"></i>
  22 |             </a>
  23 |             <h3 class="mt-2 fw-bold">EduLMS Login</h3>
  24 |             <p class="text-muted small mb-0">Secure sign-in · Student/Lecturer use MFA · Admin password only</p>
  25 |           </div>
  26 | 
  27 |           <div class="mb-3">
  28 |             <label class="form-label small fw-semibold text-muted">Email Address</label>
  29 |             <asp:TextBox ID="txtEmail" runat="server" CssClass="form-control" placeholder="you@example.com"></asp:TextBox>
  30 |           </div>
  31 | 
  32 |           <div class="mb-3">
  33 |             <label class="form-label small fw-semibold text-muted">Password</label>
  34 |             <asp:TextBox ID="txtPassword" runat="server" CssClass="form-control" TextMode="Password" placeholder="••••••••"></asp:TextBox>
  35 |           </div>
  36 | 
  37 |           <asp:Button ID="btnLogin" runat="server" Text="Login" CssClass="btn btn-accent w-100 fw-bold text-white"
  38 |           OnClick="btnLogin_Click" />
  39 | 
  40 |           <asp:Label ID="lblError" runat="server" ForeColor="Red" CssClass="d-block mt-3 text-center" style="font-size: 0.85rem;"></asp:Label>
  41 | 
  42 |           <div class="text-center mt-3">
  43 |             <a href="<%= ResolveUrl("~/Pages/Authentication/ForgotPassword.aspx") %>" class="small text-decoration-none text-muted d-block mb-2">
  44 |               Forgot password?
  45 |             </a>
  46 |             <a href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>" class="small text-decoration-none" style="color:#f17f54;font-weight:600;">
  47 |               Create a Student or Lecturer account
  48 |             </a>
  49 |           </div>
  50 | 
  51 |           <div class="text-center mt-3">
  52 |             <a href="<%= ResolveUrl("~/Pages/Landing/Landing.aspx") %>" class="text-muted small text-decoration-none">
  53 |               <i class="fa-solid fa-arrow-left me-1"></i> Back to home
  54 |             </a>
  55 |           </div>
  56 | 
  57 |           <div class="text-center mt-3 sec-badge">
  58 |             <i class="fa-solid fa-lock me-1"></i> PBKDF2 · JWT · MFA required
  59 |           </div>
  60 |         </div>
  61 |       </div>
  62 |     </form>
  63 |     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  64 |     <script src="<%= ResolveUrl("~/Shared/Scripts/csrf.js") %>"></script>
  65 |   </body>
  66 | </html>
```
