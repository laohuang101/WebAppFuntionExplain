# CsrfProtection.cs
**Source:** `Data/Security/CsrfProtection.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Session CSRF token + cookie + meta tag; validates X-CSRF-Token / form field on POST.

## File overview

- **Total lines:** 124
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (6 found)

### `EnsureToken` — lines 17–47

#### Signature

```csharp
public static string EnsureToken(HttpContext ctx)
```

#### What it is

Makes sure **Token** exists or is valid before the rest of the code continues.

#### How it works

1. Save temporary state in Session (`Session[SessionKey] as string;`).
2. Save temporary state in Session (`Session[SessionKey]`).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `token` | `string` | JWT or CSRF token string.  Read from ASP.NET Session. |
| `bytes` | `var` | Byte array (hash, random, file content).  Newly constructed object. |
| `rng` | `var` | Holds “rng” for this scope. |
| `cookie` | `var` | HTTP cookie (JWT or CSRF).  Newly constructed object. |

#### Code

```csharp
  17 | 
  18 |         public static string EnsureToken(HttpContext ctx)
  19 |         {
  20 |             if (ctx == null || ctx.Session == null) return "";
  21 |             string token = ctx.Session[SessionKey] as string;
  22 |             if (string.IsNullOrEmpty(token))
  23 |             {
  24 |                 var bytes = new byte[32];
  25 |                 using (var rng = RandomNumberGenerator.Create())
  26 |                     rng.GetBytes(bytes);
  27 |                 token = Convert.ToBase64String(bytes)
  28 |                     .TrimEnd('=').Replace('+', '-').Replace('/', '_');
  29 |                 ctx.Session[SessionKey] = token;
  30 |             }
  31 | 
  32 |             // Non-HttpOnly so JS can read for AJAX (double-submit with session)
  33 |             try
  34 |             {
  35 |                 var cookie = new HttpCookie(CookieName, token)
  36 |                 {
  37 |                     HttpOnly = false,
  38 |                     Path = "/",
  39 |                     Secure = ctx.Request != null && ctx.Request.IsSecureConnection
  40 |                 };
  41 |                 try { cookie.SameSite = SameSiteMode.Lax; } catch { }
  42 |                 ctx.Response.Cookies.Set(cookie);
  43 |             }
  44 |             catch { }
  45 | 
  46 |             return token;
  47 |         }
```

---

### `IsSafeMethod` — lines 48–54

#### Signature

```csharp
public static bool IsSafeMethod(string method)
```

#### What it is

Checks a condition related to **Is Safe Method** and returns true/false (or tries an action safely).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `method` | `string` | HTTP method (GET/POST) or MFA method (totp/email). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  48 | 
  49 |         public static bool IsSafeMethod(string method)
  50 |         {
  51 |             if (string.IsNullOrEmpty(method)) return true;
  52 |             method = method.ToUpperInvariant();
  53 |             return method == "GET" || method == "HEAD" || method == "OPTIONS" || method == "TRACE";
  54 |         }
```

---

### `Validate` — lines 57–89

#### Signature

```csharp
public static bool Validate(HttpContext ctx)
```

#### What it is

Function `Validate` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Save temporary state in Session (`Session[SessionKey] as string;`).
2. Return `false` to the caller.
3. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sessionToken` | `string` | Security token (JWT or CSRF). (text)  Read from ASP.NET Session. |
| `provided` | `string` | Holds “provided” for this scope. (text) |
| `c` | `var` | Temporary value (character, course, or counter depending on loop). |

#### Code

```csharp
  57 |         public static bool Validate(HttpContext ctx)
  58 |         {
  59 |             if (ctx == null || ctx.Request == null) return false;
  60 |             if (IsSafeMethod(ctx.Request.HttpMethod)) return true;
  61 | 
  62 |             // Ensure session exists
  63 |             if (ctx.Session == null) return false;
  64 |             string sessionToken = ctx.Session[SessionKey] as string;
  65 |             if (string.IsNullOrEmpty(sessionToken))
  66 |             {
  67 |                 // First mutating call without prior page load — issue token but reject this request
  68 |                 EnsureToken(ctx);
  69 |                 return false;
  70 |             }
  71 | 
  72 |             string provided = ctx.Request.Headers[HeaderName];
  73 |             if (string.IsNullOrEmpty(provided))
  74 |                 provided = ctx.Request.Headers["RequestVerificationToken"];
  75 |             if (string.IsNullOrEmpty(provided))
  76 |                 provided = ctx.Request.Form[FormFieldName];
  77 |             if (string.IsNullOrEmpty(provided))
  78 |                 provided = ctx.Request[FormFieldName];
  79 | 
  80 |             // Fallback: cookie must match session (double-submit)
  81 |             if (string.IsNullOrEmpty(provided))
  82 |             {
  83 |                 var c = ctx.Request.Cookies[CookieName];
  84 |                 if (c != null) provided = c.Value;
  85 |             }
  86 | 
  87 |             if (string.IsNullOrEmpty(provided)) return false;
  88 |             return FixedTimeEquals(sessionToken, provided.Trim());
  89 |         }
```

---

### `ValidateOrReject` — lines 90–107

#### Signature

```csharp
public static bool ValidateOrReject(HttpContext ctx, bool writeJsonError = true)
```

#### What it is

Function `ValidateOrReject` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Write the HTTP response body (JSON, file bytes, or text).
2. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `writeJsonError` | `bool` | Holds “write Json Error” for this scope. (true/false) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `writeJsonError` | `bool` | Holds “write Json Error” for this scope. (true/false) |

#### Code

```csharp
  90 | 
  91 |         public static bool ValidateOrReject(HttpContext ctx, bool writeJsonError = true)
  92 |         {
  93 |             if (Validate(ctx)) return true;
  94 |             if (writeJsonError && ctx != null && ctx.Response != null)
  95 |             {
  96 |                 try
  97 |                 {
  98 |                     ctx.Response.Clear();
  99 |                     ctx.Response.StatusCode = 403;
 100 |                     ctx.Response.TrySkipIisCustomErrors = true;
 101 |                     ctx.Response.ContentType = "application/json; charset=utf-8";
 102 |                     ctx.Response.Write("{\"success\":false,\"csrf\":true,\"message\":\"CSRF validation failed. Refresh the page and try again.\"}");
 103 |                 }
 104 |                 catch { }
 105 |             }
 106 |             return false;
 107 |         }
```

---

### `FixedTimeEquals` — lines 108–116

#### Signature

```csharp
private static bool FixedTimeEquals(string a, string b)
```

#### What it is

Function `FixedTimeEquals` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `FixedTimeEquals`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `a` | `string` | Holds “a” for this scope. (text) |
| `b` | `string` | Holds “b” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `diff` | `int` | Holds “diff” for this scope. (integer)  Literal number `0`. |
| `i` | `int` | Loop index (0-based counter in for-loops).  Literal number `0`. |

#### Code

```csharp
 108 | 
 109 |         private static bool FixedTimeEquals(string a, string b)
 110 |         {
 111 |             if (a == null || b == null || a.Length != b.Length) return false;
 112 |             int diff = 0;
 113 |             for (int i = 0; i < a.Length; i++)
 114 |                 diff |= a[i] ^ b[i];
 115 |             return diff == 0;
 116 |         }
```

---

### `MetaTag` — lines 117–122

#### Signature

```csharp
public static string MetaTag(HttpContext ctx)
```

#### What it is

Function `MetaTag` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `MetaTag`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `t` | `string` | Temporary string/token/time value. |

#### Code

```csharp
 117 | 
 118 |         public static string MetaTag(HttpContext ctx)
 119 |         {
 120 |             string t = HttpUtility.HtmlAttributeEncode(EnsureToken(ctx));
 121 |             return "<meta name=\"csrf-token\" content=\"" + t + "\" />";
 122 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Security.Cryptography;
   3 | using System.Text;
   4 | using System.Web;
   5 | 
   6 | namespace WebAppAssignment.Data.Security
   7 | {
   8 |     /// <summary>
   9 |     /// Session CSRF token + JS-readable cookie. Clients send X-CSRF-Token on mutating requests.
  10 |     /// </summary>
  11 |     public static class CsrfProtection
  12 |     {
  13 |         public const string HeaderName = "X-CSRF-Token";
  14 |         public const string FormFieldName = "__RequestVerificationToken";
  15 |         public const string CookieName = "EduLMS.Csrf";
  16 |         public const string SessionKey = "EduLMS.CsrfToken";
  17 | 
  18 |         public static string EnsureToken(HttpContext ctx)
  19 |         {
  20 |             if (ctx == null || ctx.Session == null) return "";
  21 |             string token = ctx.Session[SessionKey] as string;
  22 |             if (string.IsNullOrEmpty(token))
  23 |             {
  24 |                 var bytes = new byte[32];
  25 |                 using (var rng = RandomNumberGenerator.Create())
  26 |                     rng.GetBytes(bytes);
  27 |                 token = Convert.ToBase64String(bytes)
  28 |                     .TrimEnd('=').Replace('+', '-').Replace('/', '_');
  29 |                 ctx.Session[SessionKey] = token;
  30 |             }
  31 | 
  32 |             // Non-HttpOnly so JS can read for AJAX (double-submit with session)
  33 |             try
  34 |             {
  35 |                 var cookie = new HttpCookie(CookieName, token)
  36 |                 {
  37 |                     HttpOnly = false,
  38 |                     Path = "/",
  39 |                     Secure = ctx.Request != null && ctx.Request.IsSecureConnection
  40 |                 };
  41 |                 try { cookie.SameSite = SameSiteMode.Lax; } catch { }
  42 |                 ctx.Response.Cookies.Set(cookie);
  43 |             }
  44 |             catch { }
  45 | 
  46 |             return token;
  47 |         }
  48 | 
  49 |         public static bool IsSafeMethod(string method)
  50 |         {
  51 |             if (string.IsNullOrEmpty(method)) return true;
  52 |             method = method.ToUpperInvariant();
  53 |             return method == "GET" || method == "HEAD" || method == "OPTIONS" || method == "TRACE";
  54 |         }
  55 | 
  56 |         /// <summary>Validate CSRF for mutating requests. Safe methods always pass.</summary>
  57 |         public static bool Validate(HttpContext ctx)
  58 |         {
  59 |             if (ctx == null || ctx.Request == null) return false;
  60 |             if (IsSafeMethod(ctx.Request.HttpMethod)) return true;
  61 | 
  62 |             // Ensure session exists
  63 |             if (ctx.Session == null) return false;
  64 |             string sessionToken = ctx.Session[SessionKey] as string;
  65 |             if (string.IsNullOrEmpty(sessionToken))
  66 |             {
  67 |                 // First mutating call without prior page load — issue token but reject this request
  68 |                 EnsureToken(ctx);
  69 |                 return false;
  70 |             }
  71 | 
  72 |             string provided = ctx.Request.Headers[HeaderName];
  73 |             if (string.IsNullOrEmpty(provided))
  74 |                 provided = ctx.Request.Headers["RequestVerificationToken"];
  75 |             if (string.IsNullOrEmpty(provided))
  76 |                 provided = ctx.Request.Form[FormFieldName];
  77 |             if (string.IsNullOrEmpty(provided))
  78 |                 provided = ctx.Request[FormFieldName];
  79 | 
  80 |             // Fallback: cookie must match session (double-submit)
  81 |             if (string.IsNullOrEmpty(provided))
  82 |             {
  83 |                 var c = ctx.Request.Cookies[CookieName];
  84 |                 if (c != null) provided = c.Value;
  85 |             }
  86 | 
  87 |             if (string.IsNullOrEmpty(provided)) return false;
  88 |             return FixedTimeEquals(sessionToken, provided.Trim());
  89 |         }
  90 | 
  91 |         public static bool ValidateOrReject(HttpContext ctx, bool writeJsonError = true)
  92 |         {
  93 |             if (Validate(ctx)) return true;
  94 |             if (writeJsonError && ctx != null && ctx.Response != null)
  95 |             {
  96 |                 try
  97 |                 {
  98 |                     ctx.Response.Clear();
  99 |                     ctx.Response.StatusCode = 403;
 100 |                     ctx.Response.TrySkipIisCustomErrors = true;
 101 |                     ctx.Response.ContentType = "application/json; charset=utf-8";
 102 |                     ctx.Response.Write("{\"success\":false,\"csrf\":true,\"message\":\"CSRF validation failed. Refresh the page and try again.\"}");
 103 |                 }
 104 |                 catch { }
 105 |             }
 106 |             return false;
 107 |         }
 108 | 
 109 |         private static bool FixedTimeEquals(string a, string b)
 110 |         {
 111 |             if (a == null || b == null || a.Length != b.Length) return false;
 112 |             int diff = 0;
 113 |             for (int i = 0; i < a.Length; i++)
 114 |                 diff |= a[i] ^ b[i];
 115 |             return diff == 0;
 116 |         }
 117 | 
 118 |         public static string MetaTag(HttpContext ctx)
 119 |         {
 120 |             string t = HttpUtility.HtmlAttributeEncode(EnsureToken(ctx));
 121 |             return "<meta name=\"csrf-token\" content=\"" + t + "\" />";
 122 |         }
 123 |     }
 124 | }
```
