# AuthGate.cs
**Source:** `Data/Security/AuthGate.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Shared gate for pages, WebMethods, and ashx handlers — role checks, CSRF on mutating requests, validated UserID from session/JWT.

## File overview

- **Total lines:** 213
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 52:** `n` — type `string`
- **Line 57:** `true` — type `return`
- **Line 59:** `false` — type `return`
- **Line 78:** `0` — type `return`
- **Line 80:** `uid` — type `int`
- **Line 84:** `0` — type `return`
- **Line 112:** `ctx` — type `var`
- **Line 114:** `uid` — type `int`
- **Line 120:** `false` — type `return`
- **Line 126:** `false` — type `return`
- **Line 128:** `true` — type `return`
- **Line 133:** `ctx` — type `var`
- **Line 172:** `false` — type `return`
- **Line 186:** `false` — type `return`
- **Line 191:** `false` — type `return`
- **Line 193:** `true` — type `return`
- **Line 206:** `json` — type `string`

## Functions / methods (17 found)

### `CurrentUserId` — lines 18–24

```csharp
public static int CurrentUserId(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `CurrentUserId`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
  18 |         public static int CurrentUserId(HttpContext ctx = null)
  19 |         {
  20 |             ctx = ctx ?? Ctx;
  21 |             if (ctx == null) return 0;
  22 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
  23 |             return AuthService.GetValidatedUserId(ctx);
  24 |         }
```

**Line notes**

- **L22:** CSRF anti-forgery protection.
- **L23:** Restore/validate user from Session or JWT; reject stale UIDs.

---

### `EnsureCsrf` — lines 27–33

```csharp
public static bool EnsureCsrf(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `EnsureCsrf`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
  27 |         public static bool EnsureCsrf(HttpContext ctx = null)
  28 |         {
  29 |             ctx = ctx ?? Ctx;
  30 |             if (ctx == null) return false;
  31 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
  32 |             return CsrfProtection.ValidateOrReject(ctx, writeJsonError: true);
  33 |         }
```

**Line notes**

- **L27:** CSRF anti-forgery protection.
- **L31:** CSRF anti-forgery protection.
- **L32:** CSRF anti-forgery protection.

---

### `CurrentRole` — lines 34–41

```csharp
public static string CurrentRole(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `CurrentRole`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
  34 | 
  35 |         public static string CurrentRole(HttpContext ctx = null)
  36 |         {
  37 |             ctx = ctx ?? Ctx;
  38 |             if (ctx == null || ctx.Session == null) return "";
  39 |             AuthService.GetValidatedUserId(ctx);
  40 |             return AuthService.NormalizeRole(ctx.Session["UserRole"] as string ?? "");
  41 |         }
```

**Line notes**

- **L39:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L40:** Server session for logged-in user.

---

### `CurrentUserName` — lines 42–48

```csharp
public static string CurrentUserName(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `CurrentUserName`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
  42 | 
  43 |         public static string CurrentUserName(HttpContext ctx = null)
  44 |         {
  45 |             ctx = ctx ?? Ctx;
  46 |             if (ctx == null || ctx.Session == null) return "";
  47 |             return ctx.Session["UserName"] as string ?? "";
  48 |         }
```

**Line notes**

- **L47:** Server session for logged-in user.

---

### `IsInRole` — lines 49–60

```csharp
public static bool IsInRole(string role, params string[] allowed)
```

#### Explanation

- **Purpose:** Implements `IsInRole`.
- **Parameters:** `string role, params string[] allowed`
- **Local variables:** `n`

#### Line-by-line (this function)

```csharp
  49 | 
  50 |         public static bool IsInRole(string role, params string[] allowed)
  51 |         {
  52 |             string n = AuthService.NormalizeRole(role ?? "");
  53 |             if (string.IsNullOrEmpty(n) || allowed == null || allowed.Length == 0) return false;
  54 |             foreach (var a in allowed)
  55 |             {
  56 |                 if (string.Equals(n, AuthService.NormalizeRole(a), StringComparison.OrdinalIgnoreCase))
  57 |                     return true;
  58 |             }
  59 |             return false;
  60 |         }
```

**Line notes**

- **L52:** Map role codes/names to Admin/Student/Lecturer.
- **L56:** Map role codes/names to Admin/Student/Lecturer.

---

### `RequireUser` — lines 63–66

```csharp
public static int RequireUser(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `RequireUser`.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
  63 |         public static int RequireUser(HttpContext ctx = null)
  64 |         {
  65 |             return CurrentUserId(ctx);
  66 |         }
```

---

### `RequireRole` — lines 69–85

```csharp
public static int RequireRole(HttpContext ctx, params string[] roles)
```

#### Explanation

- **Purpose:** Implements `RequireRole`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Parameters:** `HttpContext ctx, params string[] roles`
- **Local variables:** `uid`

#### Line-by-line (this function)

```csharp
  69 |         public static int RequireRole(HttpContext ctx, params string[] roles)
  70 |         {
  71 |             ctx = ctx ?? Ctx;
  72 |             if (ctx != null) ctx.Items["CsrfFailed"] = false;
  73 |             if (ctx != null && ctx.Request != null
  74 |                 && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod)
  75 |                 && !CsrfProtection.Validate(ctx))
  76 |             {
  77 |                 ctx.Items["CsrfFailed"] = true;
  78 |                 return 0;
  79 |             }
  80 |             int uid = CurrentUserId(ctx);
  81 |             if (uid <= 0) return 0;
  82 |             if (roles == null || roles.Length == 0) return uid;
  83 |             if (IsInRole(CurrentRole(ctx), roles)) return uid;
  84 |             return 0;
  85 |         }
```

**Line notes**

- **L69:** Role authorization for pages/handlers.
- **L72:** CSRF anti-forgery protection.
- **L74:** CSRF anti-forgery protection.
- **L75:** CSRF anti-forgery protection.
- **L77:** CSRF anti-forgery protection.

---

### `RequireRole` — lines 86–90

```csharp
public static int RequireRole(params string[] roles)
```

#### Explanation

- **Purpose:** Implements `RequireRole`.
- **Parameters:** `params string[] roles`

#### Line-by-line (this function)

```csharp
  86 | 
  87 |         public static int RequireRole(params string[] roles)
  88 |         {
  89 |             return RequireRole(Ctx, roles);
  90 |         }
```

**Line notes**

- **L87:** Role authorization for pages/handlers.
- **L89:** Role authorization for pages/handlers.

---

### `RequireLecturer` — lines 91–95

```csharp
public static int RequireLecturer(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `RequireLecturer`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
  91 | 
  92 |         public static int RequireLecturer(HttpContext ctx = null)
  93 |         {
  94 |             return RequireRole(ctx ?? Ctx, "Lecturer", "Admin");
  95 |         }
```

**Line notes**

- **L94:** Role authorization for pages/handlers.

---

### `RequireAdmin` — lines 96–100

```csharp
public static int RequireAdmin(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `RequireAdmin`.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
  96 | 
  97 |         public static int RequireAdmin(HttpContext ctx = null)
  98 |         {
  99 |             return RequireRole(ctx ?? Ctx, "Admin");
 100 |         }
```

**Line notes**

- **L99:** Role authorization for pages/handlers.

---

### `RequireStudent` — lines 101–105

```csharp
public static int RequireStudent(HttpContext ctx = null)
```

#### Explanation

- **Purpose:** Implements `RequireStudent`.
- **Parameters:** `HttpContext ctx = null`

#### Line-by-line (this function)

```csharp
 101 | 
 102 |         public static int RequireStudent(HttpContext ctx = null)
 103 |         {
 104 |             return RequireRole(ctx ?? Ctx, "Student", "Admin");
 105 |         }
```

**Line notes**

- **L104:** Role authorization for pages/handlers.

---

### `EnsurePage` — lines 108–129

```csharp
public static bool EnsurePage(Page page, params string[] roles)
```

#### Explanation

- **Purpose:** Implements `EnsurePage`.
- **Security:** Uses AuthGate — requires logged-in role.
- **Navigation:** Redirects the browser.
- **Parameters:** `Page page, params string[] roles`
- **Local variables:** `ctx`, `uid`

#### Line-by-line (this function)

```csharp
 108 |         public static bool EnsurePage(Page page, params string[] roles)
 109 |         {
 110 |             if (page == null) return false;
 111 |             // Page.Context is protected internal — use HttpContext.Current instead
 112 |             var ctx = HttpContext.Current;
 113 |             if (ctx == null) return false;
 114 | 
 115 |             int uid = CurrentUserId(ctx);
 116 |             if (uid <= 0)
 117 |             {
 118 |                 page.Response.Redirect("~/Pages/Authentication/Login.aspx", false);
 119 |                 try { ctx.ApplicationInstance.CompleteRequest(); } catch { }
 120 |                 return false;
 121 |             }
 122 |             if (roles != null && roles.Length > 0 && !IsInRole(CurrentRole(ctx), roles))
 123 |             {
 124 |                 page.Response.Redirect("~/Pages/Landing/Landing.aspx", false);
 125 |                 try { ctx.ApplicationInstance.CompleteRequest(); } catch { }
 126 |                 return false;
 127 |             }
 128 |             return true;
 129 |         }
```

**Line notes**

- **L108:** Role authorization for pages/handlers.
- **L118:** Navigate browser to another URL.
- **L119:** Error handling block.
- **L124:** Navigate browser to another URL.
- **L125:** Error handling block.

---

### `NotAuthenticatedJson` — lines 130–149

```csharp
public static object NotAuthenticatedJson(string message = null)
```

#### Explanation

- **Purpose:** Implements `NotAuthenticatedJson`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `string message = null`
- **Local variables:** `message`, `ctx`

#### Line-by-line (this function)

```csharp
 130 | 
 131 |         public static object NotAuthenticatedJson(string message = null)
 132 |         {
 133 |             var ctx = Ctx;
 134 |             if (ctx != null && ctx.Items["CsrfFailed"] as bool? == true)
 135 |             {
 136 |                 return new
 137 |                 {
 138 |                     success = false,
 139 |                     csrf = true,
 140 |                     message = "CSRF validation failed. Refresh the page and try again."
 141 |                 };
 142 |             }
 143 |             return new
 144 |             {
 145 |                 success = false,
 146 |                 notAuthenticated = true,
 147 |                 message = message ?? "Not authenticated. Please sign in again."
 148 |             };
 149 |         }
```

**Line notes**

- **L134:** CSRF anti-forgery protection.
- **L139:** CSRF anti-forgery protection.

---

### `ForbiddenJson` — lines 150–159

```csharp
public static object ForbiddenJson(string message = null)
```

#### Explanation

- **Purpose:** Implements `ForbiddenJson`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `string message = null`
- **Local variables:** `message`

#### Line-by-line (this function)

```csharp
 150 | 
 151 |         public static object ForbiddenJson(string message = null)
 152 |         {
 153 |             return new
 154 |             {
 155 |                 success = false,
 156 |                 forbidden = true,
 157 |                 message = message ?? "You do not have permission to perform this action."
 158 |             };
 159 |         }
```

---

### `EnsureHandlerUser` — lines 162–173

```csharp
public static bool EnsureHandlerUser(HttpContext ctx, out int uid)
```

#### Explanation

- **Purpose:** Implements `EnsureHandlerUser`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Parameters:** `HttpContext ctx, out int uid`

#### Line-by-line (this function)

```csharp
 162 |         public static bool EnsureHandlerUser(HttpContext ctx, out int uid)
 163 |         {
 164 |             uid = 0;
 165 |             if (ctx != null && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod))
 166 |             {
 167 |                 if (!CsrfProtection.ValidateOrReject(ctx, true)) return false;
 168 |             }
 169 |             uid = CurrentUserId(ctx);
 170 |             if (uid > 0) return true;
 171 |             WriteHandlerError(ctx, 401, "Authentication required.");
 172 |             return false;
 173 |         }
```

**Line notes**

- **L165:** CSRF anti-forgery protection.
- **L167:** CSRF anti-forgery protection.

---

### `EnsureHandlerRole` — lines 174–194

```csharp
public static bool EnsureHandlerRole(HttpContext ctx, out int uid, params string[] roles)
```

#### Explanation

- **Purpose:** Implements `EnsureHandlerRole`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Parameters:** `HttpContext ctx, out int uid, params string[] roles`

#### Line-by-line (this function)

```csharp
 174 | 
 175 |         public static bool EnsureHandlerRole(HttpContext ctx, out int uid, params string[] roles)
 176 |         {
 177 |             uid = 0;
 178 |             if (ctx != null && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod))
 179 |             {
 180 |                 if (!CsrfProtection.ValidateOrReject(ctx, true)) return false;
 181 |             }
 182 |             uid = CurrentUserId(ctx);
 183 |             if (uid <= 0)
 184 |             {
 185 |                 WriteHandlerError(ctx, 401, "Authentication required.");
 186 |                 return false;
 187 |             }
 188 |             if (roles != null && roles.Length > 0 && !IsInRole(CurrentRole(ctx), roles))
 189 |             {
 190 |                 WriteHandlerError(ctx, 403, "Forbidden for your role.");
 191 |                 return false;
 192 |             }
 193 |             return true;
 194 |         }
```

**Line notes**

- **L175:** Role authorization for pages/handlers.
- **L178:** CSRF anti-forgery protection.
- **L180:** CSRF anti-forgery protection.

---

### `WriteHandlerError` — lines 195–211

```csharp
public static void WriteHandlerError(HttpContext ctx, int status, string message)
```

#### Explanation

- **Purpose:** Implements `WriteHandlerError`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext ctx, int status, string message`
- **Local variables:** `json`

#### Line-by-line (this function)

```csharp
 195 | 
 196 |         public static void WriteHandlerError(HttpContext ctx, int status, string message)
 197 |         {
 198 |             if (ctx == null || ctx.Response == null) return;
 199 |             try
 200 |             {
 201 |                 ctx.Response.Clear();
 202 |                 ctx.Response.StatusCode = status;
 203 |                 ctx.Response.TrySkipIisCustomErrors = true;
 204 |                 ctx.Response.ContentType = "application/json; charset=utf-8";
 205 |                 ctx.Response.Cache.SetCacheability(HttpCacheability.NoCache);
 206 |                 string json = "{\"success\":false,\"message\":\"" +
 207 |                               (message ?? "Error").Replace("\\", "\\\\").Replace("\"", "\\\"") + "\"}";
 208 |                 ctx.Response.Write(json);
 209 |             }
 210 |             catch { }
 211 |         }
```

**Line notes**

- **L199:** Error handling block.
- **L210:** Handle/log exception.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```csharp
   1 | using System;
   2 | using System.Web;
   3 | using System.Web.UI;
   4 | 
   5 | namespace WebAppAssignment.Data.Security
   6 | {
   7 |     /// <summary>
   8 |     /// Shared login / role gate for pages, WebMethods, and ashx handlers.
   9 |     /// </summary>
  10 |     public static class AuthGate
  11 |     {
  12 |         public static HttpContext Ctx
  13 |         {
  14 |             get { return HttpContext.Current; }
  15 |         }
  16 | 
  17 |         /// <summary>Valid session UID (JWT restored), or 0.</summary>
  18 |         public static int CurrentUserId(HttpContext ctx = null)
  19 |         {
  20 |             ctx = ctx ?? Ctx;
  21 |             if (ctx == null) return 0;
  22 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
  23 |             return AuthService.GetValidatedUserId(ctx);
  24 |         }
  25 | 
  26 |         /// <summary>Validate CSRF on mutating requests. Returns false if invalid.</summary>
  27 |         public static bool EnsureCsrf(HttpContext ctx = null)
  28 |         {
  29 |             ctx = ctx ?? Ctx;
  30 |             if (ctx == null) return false;
  31 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
  32 |             return CsrfProtection.ValidateOrReject(ctx, writeJsonError: true);
  33 |         }
  34 | 
  35 |         public static string CurrentRole(HttpContext ctx = null)
  36 |         {
  37 |             ctx = ctx ?? Ctx;
  38 |             if (ctx == null || ctx.Session == null) return "";
  39 |             AuthService.GetValidatedUserId(ctx);
  40 |             return AuthService.NormalizeRole(ctx.Session["UserRole"] as string ?? "");
  41 |         }
  42 | 
  43 |         public static string CurrentUserName(HttpContext ctx = null)
  44 |         {
  45 |             ctx = ctx ?? Ctx;
  46 |             if (ctx == null || ctx.Session == null) return "";
  47 |             return ctx.Session["UserName"] as string ?? "";
  48 |         }
  49 | 
  50 |         public static bool IsInRole(string role, params string[] allowed)
  51 |         {
  52 |             string n = AuthService.NormalizeRole(role ?? "");
  53 |             if (string.IsNullOrEmpty(n) || allowed == null || allowed.Length == 0) return false;
  54 |             foreach (var a in allowed)
  55 |             {
  56 |                 if (string.Equals(n, AuthService.NormalizeRole(a), StringComparison.OrdinalIgnoreCase))
  57 |                     return true;
  58 |             }
  59 |             return false;
  60 |         }
  61 | 
  62 |         /// <summary>Require any authenticated user. Returns uid or 0.</summary>
  63 |         public static int RequireUser(HttpContext ctx = null)
  64 |         {
  65 |             return CurrentUserId(ctx);
  66 |         }
  67 | 
  68 |         /// <summary>Require authenticated user in one of the roles. Returns uid or 0.</summary>
  69 |         public static int RequireRole(HttpContext ctx, params string[] roles)
  70 |         {
  71 |             ctx = ctx ?? Ctx;
  72 |             if (ctx != null) ctx.Items["CsrfFailed"] = false;
  73 |             if (ctx != null && ctx.Request != null
  74 |                 && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod)
  75 |                 && !CsrfProtection.Validate(ctx))
  76 |             {
  77 |                 ctx.Items["CsrfFailed"] = true;
  78 |                 return 0;
  79 |             }
  80 |             int uid = CurrentUserId(ctx);
  81 |             if (uid <= 0) return 0;
  82 |             if (roles == null || roles.Length == 0) return uid;
  83 |             if (IsInRole(CurrentRole(ctx), roles)) return uid;
  84 |             return 0;
  85 |         }
  86 | 
  87 |         public static int RequireRole(params string[] roles)
  88 |         {
  89 |             return RequireRole(Ctx, roles);
  90 |         }
  91 | 
  92 |         public static int RequireLecturer(HttpContext ctx = null)
  93 |         {
  94 |             return RequireRole(ctx ?? Ctx, "Lecturer", "Admin");
  95 |         }
  96 | 
  97 |         public static int RequireAdmin(HttpContext ctx = null)
  98 |         {
  99 |             return RequireRole(ctx ?? Ctx, "Admin");
 100 |         }
 101 | 
 102 |         public static int RequireStudent(HttpContext ctx = null)
 103 |         {
 104 |             return RequireRole(ctx ?? Ctx, "Student", "Admin");
 105 |         }
 106 | 
 107 |         /// <summary>Page gate: redirect to login (or landing) if not allowed.</summary>
 108 |         public static bool EnsurePage(Page page, params string[] roles)
 109 |         {
 110 |             if (page == null) return false;
 111 |             // Page.Context is protected internal — use HttpContext.Current instead
 112 |             var ctx = HttpContext.Current;
 113 |             if (ctx == null) return false;
 114 | 
 115 |             int uid = CurrentUserId(ctx);
 116 |             if (uid <= 0)
 117 |             {
 118 |                 page.Response.Redirect("~/Pages/Authentication/Login.aspx", false);
 119 |                 try { ctx.ApplicationInstance.CompleteRequest(); } catch { }
 120 |                 return false;
 121 |             }
 122 |             if (roles != null && roles.Length > 0 && !IsInRole(CurrentRole(ctx), roles))
 123 |             {
 124 |                 page.Response.Redirect("~/Pages/Landing/Landing.aspx", false);
 125 |                 try { ctx.ApplicationInstance.CompleteRequest(); } catch { }
 126 |                 return false;
 127 |             }
 128 |             return true;
 129 |         }
 130 | 
 131 |         public static object NotAuthenticatedJson(string message = null)
 132 |         {
 133 |             var ctx = Ctx;
 134 |             if (ctx != null && ctx.Items["CsrfFailed"] as bool? == true)
 135 |             {
 136 |                 return new
 137 |                 {
 138 |                     success = false,
 139 |                     csrf = true,
 140 |                     message = "CSRF validation failed. Refresh the page and try again."
 141 |                 };
 142 |             }
 143 |             return new
 144 |             {
 145 |                 success = false,
 146 |                 notAuthenticated = true,
 147 |                 message = message ?? "Not authenticated. Please sign in again."
 148 |             };
 149 |         }
 150 | 
 151 |         public static object ForbiddenJson(string message = null)
 152 |         {
 153 |             return new
 154 |             {
 155 |                 success = false,
 156 |                 forbidden = true,
 157 |                 message = message ?? "You do not have permission to perform this action."
 158 |             };
 159 |         }
 160 | 
 161 |         /// <summary>For ashx: write 401 JSON and return false if not logged in.</summary>
 162 |         public static bool EnsureHandlerUser(HttpContext ctx, out int uid)
 163 |         {
 164 |             uid = 0;
 165 |             if (ctx != null && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod))
 166 |             {
 167 |                 if (!CsrfProtection.ValidateOrReject(ctx, true)) return false;
 168 |             }
 169 |             uid = CurrentUserId(ctx);
 170 |             if (uid > 0) return true;
 171 |             WriteHandlerError(ctx, 401, "Authentication required.");
 172 |             return false;
 173 |         }
 174 | 
 175 |         public static bool EnsureHandlerRole(HttpContext ctx, out int uid, params string[] roles)
 176 |         {
 177 |             uid = 0;
 178 |             if (ctx != null && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod))
 179 |             {
 180 |                 if (!CsrfProtection.ValidateOrReject(ctx, true)) return false;
 181 |             }
 182 |             uid = CurrentUserId(ctx);
 183 |             if (uid <= 0)
 184 |             {
 185 |                 WriteHandlerError(ctx, 401, "Authentication required.");
 186 |                 return false;
 187 |             }
 188 |             if (roles != null && roles.Length > 0 && !IsInRole(CurrentRole(ctx), roles))
 189 |             {
 190 |                 WriteHandlerError(ctx, 403, "Forbidden for your role.");
 191 |                 return false;
 192 |             }
 193 |             return true;
 194 |         }
 195 | 
 196 |         public static void WriteHandlerError(HttpContext ctx, int status, string message)
 197 |         {
 198 |             if (ctx == null || ctx.Response == null) return;
 199 |             try
 200 |             {
 201 |                 ctx.Response.Clear();
 202 |                 ctx.Response.StatusCode = status;
 203 |                 ctx.Response.TrySkipIisCustomErrors = true;
 204 |                 ctx.Response.ContentType = "application/json; charset=utf-8";
 205 |                 ctx.Response.Cache.SetCacheability(HttpCacheability.NoCache);
 206 |                 string json = "{\"success\":false,\"message\":\"" +
 207 |                               (message ?? "Error").Replace("\\", "\\\\").Replace("\"", "\\\"") + "\"}";
 208 |                 ctx.Response.Write(json);
 209 |             }
 210 |             catch { }
 211 |         }
 212 |     }
 213 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L10:** Authorization — block wrong role / anonymous.
- **L22:** CSRF anti-forgery protection.
- **L23:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L27:** CSRF anti-forgery protection.
- **L31:** CSRF anti-forgery protection.
- **L32:** CSRF anti-forgery protection.
- **L39:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L40:** Server session for logged-in user.
- **L47:** Server session for logged-in user.
- **L52:** Map role codes/names to Admin/Student/Lecturer.
- **L56:** Map role codes/names to Admin/Student/Lecturer.
- **L69:** Role authorization for pages/handlers.
- **L72:** CSRF anti-forgery protection.
- **L74:** CSRF anti-forgery protection.
- **L75:** CSRF anti-forgery protection.
- **L77:** CSRF anti-forgery protection.
- **L87:** Role authorization for pages/handlers.
- **L89:** Role authorization for pages/handlers.
- **L94:** Role authorization for pages/handlers.
- **L99:** Role authorization for pages/handlers.
- **L104:** Role authorization for pages/handlers.
- **L108:** Role authorization for pages/handlers.
- **L118:** Navigate browser to another URL.
- **L119:** Error handling block.
- **L124:** Navigate browser to another URL.
- **L125:** Error handling block.
- **L134:** CSRF anti-forgery protection.
- **L139:** CSRF anti-forgery protection.
- **L165:** CSRF anti-forgery protection.
- **L167:** CSRF anti-forgery protection.
- **L175:** Role authorization for pages/handlers.
- **L178:** CSRF anti-forgery protection.
- **L180:** CSRF anti-forgery protection.
- **L199:** Error handling block.
- **L210:** Handle/log exception.

## Source snapshot (raw)

```csharp
using System;
using System.Web;
using System.Web.UI;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// Shared login / role gate for pages, WebMethods, and ashx handlers.
    /// </summary>
    public static class AuthGate
    {
        public static HttpContext Ctx
        {
            get { return HttpContext.Current; }
        }

        /// <summary>Valid session UID (JWT restored), or 0.</summary>
        public static int CurrentUserId(HttpContext ctx = null)
        {
            ctx = ctx ?? Ctx;
            if (ctx == null) return 0;
            try { CsrfProtection.EnsureToken(ctx); } catch { }
            return AuthService.GetValidatedUserId(ctx);
        }

        /// <summary>Validate CSRF on mutating requests. Returns false if invalid.</summary>
        public static bool EnsureCsrf(HttpContext ctx = null)
        {
            ctx = ctx ?? Ctx;
            if (ctx == null) return false;
            try { CsrfProtection.EnsureToken(ctx); } catch { }
            return CsrfProtection.ValidateOrReject(ctx, writeJsonError: true);
        }

        public static string CurrentRole(HttpContext ctx = null)
        {
            ctx = ctx ?? Ctx;
            if (ctx == null || ctx.Session == null) return "";
            AuthService.GetValidatedUserId(ctx);
            return AuthService.NormalizeRole(ctx.Session["UserRole"] as string ?? "");
        }

        public static string CurrentUserName(HttpContext ctx = null)
        {
            ctx = ctx ?? Ctx;
            if (ctx == null || ctx.Session == null) return "";
            return ctx.Session["UserName"] as string ?? "";
        }

        public static bool IsInRole(string role, params string[] allowed)
        {
            string n = AuthService.NormalizeRole(role ?? "");
            if (string.IsNullOrEmpty(n) || allowed == null || allowed.Length == 0) return false;
            foreach (var a in allowed)
            {
                if (string.Equals(n, AuthService.NormalizeRole(a), StringComparison.OrdinalIgnoreCase))
                    return true;
            }
            return false;
        }

        /// <summary>Require any authenticated user. Returns uid or 0.</summary>
        public static int RequireUser(HttpContext ctx = null)
        {
            return CurrentUserId(ctx);
        }

        /// <summary>Require authenticated user in one of the roles. Returns uid or 0.</summary>
        public static int RequireRole(HttpContext ctx, params string[] roles)
        {
            ctx = ctx ?? Ctx;
            if (ctx != null) ctx.Items["CsrfFailed"] = false;
            if (ctx != null && ctx.Request != null
                && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod)
                && !CsrfProtection.Validate(ctx))
            {
                ctx.Items["CsrfFailed"] = true;
                return 0;
            }
            int uid = CurrentUserId(ctx);
            if (uid <= 0) return 0;
            if (roles == null || roles.Length == 0) return uid;
            if (IsInRole(CurrentRole(ctx), roles)) return uid;
            return 0;
        }

        public static int RequireRole(params string[] roles)
        {
            return RequireRole(Ctx, roles);
        }

        public static int RequireLecturer(HttpContext ctx = null)
        {
            return RequireRole(ctx ?? Ctx, "Lecturer", "Admin");
        }

        public static int RequireAdmin(HttpContext ctx = null)
        {
            return RequireRole(ctx ?? Ctx, "Admin");
        }

        public static int RequireStudent(HttpContext ctx = null)
        {
            return RequireRole(ctx ?? Ctx, "Student", "Admin");
        }

        /// <summary>Page gate: redirect to login (or landing) if not allowed.</summary>
        public static bool EnsurePage(Page page, params string[] roles)
        {
            if (page == null) return false;
            // Page.Context is protected internal — use HttpContext.Current instead
            var ctx = HttpContext.Current;
            if (ctx == null) return false;

            int uid = CurrentUserId(ctx);
            if (uid <= 0)
            {
                page.Response.Redirect("~/Pages/Authentication/Login.aspx", false);
                try { ctx.ApplicationInstance.CompleteRequest(); } catch { }
                return false;
            }
            if (roles != null && roles.Length > 0 && !IsInRole(CurrentRole(ctx), roles))
            {
                page.Response.Redirect("~/Pages/Landing/Landing.aspx", false);
                try { ctx.ApplicationInstance.CompleteRequest(); } catch { }
                return false;
            }
            return true;
        }

        public static object NotAuthenticatedJson(string message = null)
        {
            var ctx = Ctx;
            if (ctx != null && ctx.Items["CsrfFailed"] as bool? == true)
            {
                return new
                {
                    success = false,
                    csrf = true,
                    message = "CSRF validation failed. Refresh the page and try again."
                };
            }
            return new
            {
                success = false,
                notAuthenticated = true,
                message = message ?? "Not authenticated. Please sign in again."
            };
        }

        public static object ForbiddenJson(string message = null)
        {
            return new
            {
                success = false,
                forbidden = true,
                message = message ?? "You do not have permission to perform this action."
            };
        }

        /// <summary>For ashx: write 401 JSON and return false if not logged in.</summary>
        public static bool EnsureHandlerUser(HttpContext ctx, out int uid)
        {
            uid = 0;
            if (ctx != null && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod))
            {
                if (!CsrfProtection.ValidateOrReject(ctx, true)) return false;
            }
            uid = CurrentUserId(ctx);
            if (uid > 0) return true;
            WriteHandlerError(ctx, 401, "Authentication required.");
            return false;
        }

        public static bool EnsureHandlerRole(HttpContext ctx, out int uid, params string[] roles)
        {
            uid = 0;
            if (ctx != null && !CsrfProtection.IsSafeMethod(ctx.Request.HttpMethod))
            {
                if (!CsrfProtection.ValidateOrReject(ctx, true)) return false;
            }
            uid = CurrentUserId(ctx);
            if (uid <= 0)
            {
                WriteHandlerError(ctx, 401, "Authentication required.");
                return false;
            }
            if (roles != null && roles.Length > 0 && !IsInRole(CurrentRole(ctx), roles))
            {
                WriteHandlerError(ctx, 403, "Forbidden for your role.");
                return false;
            }
            return true;
        }

        public static void WriteHandlerError(HttpContext ctx, int status, string message)
        {
            if (ctx == null || ctx.Response == null) return;
            try
            {
                ctx.Response.Clear();
                ctx.Response.StatusCode = status;
                ctx.Response.TrySkipIisCustomErrors = true;
                ctx.Response.ContentType = "application/json; charset=utf-8";
                ctx.Response.Cache.SetCacheability(HttpCacheability.NoCache);
                string json = "{\"success\":false,\"message\":\"" +
                              (message ?? "Error").Replace("\\", "\\\\").Replace("\"", "\\\"") + "\"}";
                ctx.Response.Write(json);
            }
            catch { }
        }
    }
}

```
