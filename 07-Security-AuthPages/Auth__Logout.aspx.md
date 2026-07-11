# Logout.aspx
**Source:** `Pages/Authentication/Logout.aspx`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Clears session, abandons session, clears JWT auth cookie.

## File overview

- **Total lines:** 19
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Logout.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.Logout" %>`
`   2`  ``
`   3`  `<!DOCTYPE html>`
`   4`  `<html xmlns="http://www.w3.org/1999/xhtml">`
`   5`  `  <head runat="server">`
`   6`  `    <meta charset="utf-8" />`
`   7`  `    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />`
`   8`  `    <title>Signing out... - EduLMS</title>`
`   9`  `    <meta http-equiv="refresh" content="0;url=<%= ResolveUrl("~/Pages/Landing/Landing.aspx") %>" />`
`  10`  `    <style>`
`  11`  `      body { font-family: Inter, system-ui, sans-serif; background: #f5f6f8; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; color: #6b7280; }`
`  12`  `    </style>`
`  13`  `  </head>`
`  14`  `  <body>`
`  15`  `    <form id="form1" runat="server">`
`  16`  `      <div>Signing you out...</div>`
`  17`  `    </form>`
`  18`  `  </body>`
`  19`  `</html>`

## Source snapshot (raw)

```html
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Logout.aspx.cs" Inherits="WebAppAssignment.Pages.Authentication.Logout" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head runat="server">
    <meta charset="utf-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Signing out... - EduLMS</title>
    <meta http-equiv="refresh" content="0;url=<%= ResolveUrl("~/Pages/Landing/Landing.aspx") %>" />
    <style>
      body { font-family: Inter, system-ui, sans-serif; background: #f5f6f8; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; color: #6b7280; }
    </style>
  </head>
  <body>
    <form id="form1" runat="server">
      <div>Signing you out...</div>
    </form>
  </body>
</html>

```
