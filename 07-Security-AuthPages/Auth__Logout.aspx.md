# Logout.aspx
**Source:** `Pages/Authentication/Logout.aspx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Clears session, abandons session, clears JWT auth cookie.

## File overview

- **Total lines:** 19
- **Kind:** `.aspx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See the code listing at the bottom._

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Logout.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.Logout" %>
   2 | 
   3 | <!DOCTYPE html>
   4 | <html xmlns="http://www.w3.org/1999/xhtml">
   5 |   <head runat="server">
   6 |     <meta charset="utf-8" />
   7 |     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   8 |     <title>Signing out... - EduLMS</title>
   9 |     <meta http-equiv="refresh" content="0;url=<%= ResolveUrl("~/Pages/Landing/Landing.aspx") %>" />
  10 |     <style>
  11 |       body { font-family: Inter, system-ui, sans-serif; background: #f5f6f8; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; color: #6b7280; }
  12 |     </style>
  13 |   </head>
  14 |   <body>
  15 |     <form id="form1" runat="server">
  16 |       <div>Signing you out...</div>
  17 |     </form>
  18 |   </body>
  19 | </html>
```
