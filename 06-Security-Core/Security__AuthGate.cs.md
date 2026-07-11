# AuthGate.cs
**Source:** `Data/Security/AuthGate.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Shared gate for pages, WebMethods, and ashx handlers — role checks, CSRF on mutating requests, validated UserID from session/JWT.

## File overview

- **Total lines:** 213
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (17 found)

### `CurrentUserId` — lines 18–24

#### Signature

```csharp
public static int CurrentUserId(HttpContext ctx = null)
```

#### What it is

Returns the logged-in user’s ID (from Session/JWT), or `0` if nobody is signed in.

#### How it works

1. Use the given HttpContext, or the current request context.
2. If there is no context, return 0 (not logged in).
3. Ensure a CSRF token exists for this session.
4. Return AuthService.GetValidatedUserId (real UID or 0).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  18 |         public static int CurrentUserId(HttpContext ctx = null)
  19 |         {
  20 |             ctx = ctx ?? Ctx;
  21 |             if (ctx == null) return 0;
  22 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
  23 |             return AuthService.GetValidatedUserId(ctx);
  24 |         }
```

---

### `EnsureCsrf` — lines 27–33

#### Signature

```csharp
public static bool EnsureCsrf(HttpContext ctx = null)
```

#### What it is

Checks that a POST/AJAX request includes a valid anti-forgery (CSRF) token.

#### How it works

1. Make sure a CSRF token exists in Session (create one if missing).
2. Validate the CSRF anti-forgery token on this mutating request.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  27 |         public static bool EnsureCsrf(HttpContext ctx = null)
  28 |         {
  29 |             ctx = ctx ?? Ctx;
  30 |             if (ctx == null) return false;
  31 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
  32 |             return CsrfProtection.ValidateOrReject(ctx, writeJsonError: true);
  33 |         }
```

---

### `CurrentRole` — lines 34–41

#### Signature

```csharp
public static string CurrentRole(HttpContext ctx = null)
```

#### What it is

Returns the logged-in user’s role name (Admin / Lecturer / Student).

#### How it works

1. Read the logged-in user id from Session/JWT (0 means not signed in).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Code

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

---

### `CurrentUserName` — lines 42–48

#### Signature

```csharp
public static string CurrentUserName(HttpContext ctx = null)
```

#### What it is

Function `CurrentUserName` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `CurrentUserName`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Code

```csharp
  42 | 
  43 |         public static string CurrentUserName(HttpContext ctx = null)
  44 |         {
  45 |             ctx = ctx ?? Ctx;
  46 |             if (ctx == null || ctx.Session == null) return "";
  47 |             return ctx.Session["UserName"] as string ?? "";
  48 |         }
```

---

### `IsInRole` — lines 49–60

#### Signature

```csharp
public static bool IsInRole(string role, params string[] allowed)
```

#### What it is

Checks a condition related to **Is In Role** and returns true/false (or tries an action safely).

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Return `true` to the caller.
3. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |
| `allowed` | `string[]` | Boolean — path/role is permitted. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `n` | `string` | Numeric count or temporary integer. |
| `a` | `—` | Holds “a” for this scope. |

#### Code

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

---

### `RequireUser` — lines 63–66

#### Signature

```csharp
public static int RequireUser(HttpContext ctx = null)
```

#### What it is

Function `RequireUser` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Read the logged-in user id from Session/JWT (0 means not signed in).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  63 |         public static int RequireUser(HttpContext ctx = null)
  64 |         {
  65 |             return CurrentUserId(ctx);
  66 |         }
```

---

### `RequireRole` — lines 69–85

#### Signature

```csharp
public static int RequireRole(HttpContext ctx, params string[] roles)
```

#### What it is

Function `RequireRole` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate the CSRF anti-forgery token on this mutating request.
2. Read the logged-in user id from Session/JWT (0 means not signed in).
3. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `roles` | `string[]` | Often a collection related to roles (plural name). (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous). |

#### Code

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

---

### `RequireRole` — lines 86–90

#### Signature

```csharp
public static int RequireRole(params string[] roles)
```

#### What it is

Function `RequireRole` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `roles` | `string[]` | Often a collection related to roles (plural name). (text) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  86 | 
  87 |         public static int RequireRole(params string[] roles)
  88 |         {
  89 |             return RequireRole(Ctx, roles);
  90 |         }
```

---

### `RequireLecturer` — lines 91–95

#### Signature

```csharp
public static int RequireLecturer(HttpContext ctx = null)
```

#### What it is

Function `RequireLecturer` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Code

```csharp
  91 | 
  92 |         public static int RequireLecturer(HttpContext ctx = null)
  93 |         {
  94 |             return RequireRole(ctx ?? Ctx, "Lecturer", "Admin");
  95 |         }
```

---

### `RequireAdmin` — lines 96–100

#### Signature

```csharp
public static int RequireAdmin(HttpContext ctx = null)
```

#### What it is

Function `RequireAdmin` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Code

```csharp
  96 | 
  97 |         public static int RequireAdmin(HttpContext ctx = null)
  98 |         {
  99 |             return RequireRole(ctx ?? Ctx, "Admin");
 100 |         }
```

---

### `RequireStudent` — lines 101–105

#### Signature

```csharp
public static int RequireStudent(HttpContext ctx = null)
```

#### What it is

Function `RequireStudent` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Code

```csharp
 101 | 
 102 |         public static int RequireStudent(HttpContext ctx = null)
 103 |         {
 104 |             return RequireRole(ctx ?? Ctx, "Student", "Admin");
 105 |         }
```

---

### `EnsurePage` — lines 108–129

#### Signature

```csharp
public static bool EnsurePage(Page page, params string[] roles)
```

#### What it is

Blocks the page unless the visitor is logged in with an allowed role (redirects to login otherwise).

#### How it works

1. Read the logged-in user id from Session/JWT (0 means not signed in).
2. Redirect the browser to another page.
3. Return `false` to the caller.
4. Redirect the browser to another page.
5. Return `false` to the caller.
6. Return `true` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `page` | `Page` | Page number for pagination, or Page instance. |
| `roles` | `string[]` | Often a collection related to roles (plural name). (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `var` | Current HTTP request context (Request, Response, Session). |
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous). |

#### Code

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

---

### `NotAuthenticatedJson` — lines 130–149

#### Signature

```csharp
public static object NotAuthenticatedJson(string message = null)
```

#### What it is

Function `NotAuthenticatedJson` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `NotAuthenticatedJson`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `message` | `string` | Status text for the UI. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `message` | `string` | Status text for the UI. |

#### Code

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

---

### `ForbiddenJson` — lines 150–159

#### Signature

```csharp
public static object ForbiddenJson(string message = null)
```

#### What it is

Function `ForbiddenJson` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `ForbiddenJson`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `message` | `string` | Status text for the UI. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `message` | `string` | Status text for the UI. |

#### Code

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

#### Signature

```csharp
public static bool EnsureHandlerUser(HttpContext ctx, out int uid)
```

#### What it is

Makes sure **Handler User** exists or is valid before the rest of the code continues.

#### How it works

1. Validate the CSRF anti-forgery token on this mutating request.
2. Read the logged-in user id from Session/JWT (0 means not signed in).
3. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `EnsureHandlerRole` — lines 174–194

#### Signature

```csharp
public static bool EnsureHandlerRole(HttpContext ctx, out int uid, params string[] roles)
```

#### What it is

Same as EnsurePage but for `.ashx` APIs — returns an error JSON instead of a redirect.

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.
2. Validate the CSRF anti-forgery token on this mutating request.
3. Read the logged-in user id from Session/JWT (0 means not signed in).
4. Return `false` to the caller.
5. Return `true` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `roles` | `string[]` | Often a collection related to roles (plural name). (text) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `WriteHandlerError` — lines 195–211

#### Signature

```csharp
public static void WriteHandlerError(HttpContext ctx, int status, string message)
```

#### What it is

Function `WriteHandlerError` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Write the HTTP response body (JSON, file bytes, or text).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `status` | `int` | Holds “status” for this scope. (integer) |
| `message` | `string` | Status text for the UI. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `json` | `string` | JSON string (to parse or serialize).  Literal text string. |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
