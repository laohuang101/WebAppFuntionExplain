# CsrfProtection.cs
**Source:** `Data/Security/CsrfProtection.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Session CSRF token + cookie + meta tag; validates X-CSRF-Token / form field on POST.

## File overview

- **Total lines:** 124
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 21:** `token` — type `string`
- **Line 24:** `bytes` — type `var`
- **Line 35:** `cookie` — type `var`
- **Line 45:** `token` — type `return`
- **Line 53:** `method` — type `return`
- **Line 64:** `sessionToken` — type `string`
- **Line 69:** `false` — type `return`
- **Line 71:** `provided` — type `string`
- **Line 83:** `c` — type `var`
- **Line 106:** `false` — type `return`
- **Line 112:** `diff` — type `int`
- **Line 115:** `diff` — type `return`
- **Line 120:** `t` — type `string`

## Functions / methods (6 found)

### `EnsureToken` — lines 17–47

```
public static string EnsureToken(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `EnsureToken`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx`
- **Local variables:** `token`, `bytes`, `rng`, `cookie`

#### Line-by-line (this function)

`  17`  ``
`  18`  `        public static string EnsureToken(HttpContext ctx)`
  - → CSRF token ensure/validate.
`  19`  `        {`
`  20`  `            if (ctx == null || ctx.Session == null) return "";`
`  21`  `            string token = ctx.Session[SessionKey] as string;`
  - → Server session for logged-in user.
`  22`  `            if (string.IsNullOrEmpty(token))`
`  23`  `            {`
`  24`  `                var bytes = new byte[32];`
`  25`  `                using (var rng = RandomNumberGenerator.Create())`
  - → Import namespace/types.
`  26`  `                    rng.GetBytes(bytes);`
`  27`  `                token = Convert.ToBase64String(bytes)`
`  28`  `                    .TrimEnd('=').Replace('+', '-').Replace('/', '_');`
`  29`  `                ctx.Session[SessionKey] = token;`
  - → Server session for logged-in user.
`  30`  `            }`
`  31`  ``
`  32`  `            // Non-HttpOnly so JS can read for AJAX (double-submit with session)`
`  33`  `            try`
  - → Error handling block.
`  34`  `            {`
`  35`  `                var cookie = new HttpCookie(CookieName, token)`
`  36`  `                {`
`  37`  `                    HttpOnly = false,`
`  38`  `                    Path = "/",`
`  39`  `                    Secure = ctx.Request != null && ctx.Request.IsSecureConnection`
`  40`  `                };`
`  41`  `                try { cookie.SameSite = SameSiteMode.Lax; } catch { }`
  - → Error handling block.
`  42`  `                ctx.Response.Cookies.Set(cookie);`
`  43`  `            }`
`  44`  `            catch { }`
  - → Handle/log exception.
`  45`  ``
`  46`  `            return token;`
`  47`  `        }`

---

### `IsSafeMethod` — lines 48–54

```
public static bool IsSafeMethod(string method)
```

#### Explanation

- **Purpose:** Implements `IsSafeMethod`.
- **Parameters:** `string method`

#### Line-by-line (this function)

`  48`  ``
`  49`  `        public static bool IsSafeMethod(string method)`
`  50`  `        {`
`  51`  `            if (string.IsNullOrEmpty(method)) return true;`
`  52`  `            method = method.ToUpperInvariant();`
`  53`  `            return method == "GET" || method == "HEAD" || method == "OPTIONS" || method == "TRACE";`
`  54`  `        }`

---

### `Validate` — lines 57–89

```
public static bool Validate(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `Validate`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx`
- **Local variables:** `sessionToken`, `provided`, `c`

#### Line-by-line (this function)

`  57`  `        public static bool Validate(HttpContext ctx)`
`  58`  `        {`
`  59`  `            if (ctx == null || ctx.Request == null) return false;`
`  60`  `            if (IsSafeMethod(ctx.Request.HttpMethod)) return true;`
`  61`  ``
`  62`  `            // Ensure session exists`
`  63`  `            if (ctx.Session == null) return false;`
`  64`  `            string sessionToken = ctx.Session[SessionKey] as string;`
  - → Server session for logged-in user.
`  65`  `            if (string.IsNullOrEmpty(sessionToken))`
`  66`  `            {`
`  67`  `                // First mutating call without prior page load — issue token but reject this request`
`  68`  `                EnsureToken(ctx);`
  - → CSRF token ensure/validate.
`  69`  `                return false;`
`  70`  `            }`
`  71`  ``
`  72`  `            string provided = ctx.Request.Headers[HeaderName];`
`  73`  `            if (string.IsNullOrEmpty(provided))`
`  74`  `                provided = ctx.Request.Headers["RequestVerificationToken"];`
`  75`  `            if (string.IsNullOrEmpty(provided))`
`  76`  `                provided = ctx.Request.Form[FormFieldName];`
`  77`  `            if (string.IsNullOrEmpty(provided))`
`  78`  `                provided = ctx.Request[FormFieldName];`
`  79`  ``
`  80`  `            // Fallback: cookie must match session (double-submit)`
`  81`  `            if (string.IsNullOrEmpty(provided))`
`  82`  `            {`
`  83`  `                var c = ctx.Request.Cookies[CookieName];`
`  84`  `                if (c != null) provided = c.Value;`
`  85`  `            }`
`  86`  ``
`  87`  `            if (string.IsNullOrEmpty(provided)) return false;`
`  88`  `            return FixedTimeEquals(sessionToken, provided.Trim());`
  - → Constant-time string compare (reduce timing leaks).
`  89`  `        }`

---

### `ValidateOrReject` — lines 90–107

```
public static bool ValidateOrReject(HttpContext ctx, bool writeJsonError = true)
```

#### Explanation

- **Purpose:** Implements `ValidateOrReject`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext ctx, bool writeJsonError = true`
- **Local variables:** `writeJsonError`

#### Line-by-line (this function)

`  90`  ``
`  91`  `        public static bool ValidateOrReject(HttpContext ctx, bool writeJsonError = true)`
`  92`  `        {`
`  93`  `            if (Validate(ctx)) return true;`
`  94`  `            if (writeJsonError && ctx != null && ctx.Response != null)`
`  95`  `            {`
`  96`  `                try`
  - → Error handling block.
`  97`  `                {`
`  98`  `                    ctx.Response.Clear();`
`  99`  `                    ctx.Response.StatusCode = 403;`
` 100`  `                    ctx.Response.TrySkipIisCustomErrors = true;`
` 101`  `                    ctx.Response.ContentType = "application/json; charset=utf-8";`
` 102`  `                    ctx.Response.Write("{\"success\":false,\"csrf\":true,\"message\":\"CSRF validation failed. Refresh the page and try again.\"}");`
  - → CSRF anti-forgery protection.
` 103`  `                }`
` 104`  `                catch { }`
  - → Handle/log exception.
` 105`  `            }`
` 106`  `            return false;`
` 107`  `        }`

---

### `FixedTimeEquals` — lines 108–116

```
private static bool FixedTimeEquals(string a, string b)
```

#### Explanation

- **Purpose:** Implements `FixedTimeEquals`.
- **Parameters:** `string a, string b`
- **Local variables:** `diff`, `i`

#### Line-by-line (this function)

` 108`  ``
` 109`  `        private static bool FixedTimeEquals(string a, string b)`
  - → Constant-time string compare (reduce timing leaks).
` 110`  `        {`
` 111`  `            if (a == null || b == null || a.Length != b.Length) return false;`
` 112`  `            int diff = 0;`
` 113`  `            for (int i = 0; i < a.Length; i++)`
` 114`  `                diff |= a[i] ^ b[i];`
` 115`  `            return diff == 0;`
` 116`  `        }`

---

### `MetaTag` — lines 117–122

```
public static string MetaTag(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `MetaTag`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Parameters:** `HttpContext ctx`
- **Local variables:** `t`

#### Line-by-line (this function)

` 117`  ``
` 118`  `        public static string MetaTag(HttpContext ctx)`
` 119`  `        {`
` 120`  `            string t = HttpUtility.HtmlAttributeEncode(EnsureToken(ctx));`
  - → CSRF token ensure/validate.
` 121`  `            return "<meta name=\"csrf-token\" content=\"" + t + "\" />";`
  - → CSRF anti-forgery protection.
` 122`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Security.Cryptography;`
  - → Import namespace/types.
`   3`  `using System.Text;`
  - → Import namespace/types.
`   4`  `using System.Web;`
  - → Import namespace/types.
`   5`  ``
`   6`  `namespace WebAppAssignment.Data.Security`
  - → C# namespace grouping.
`   7`  `{`
`   8`  `    /// <summary>`
`   9`  `    /// Session CSRF token + JS-readable cookie. Clients send X-CSRF-Token on mutating requests.`
`  10`  `    /// </summary>`
`  11`  `    public static class CsrfProtection`
  - → CSRF anti-forgery protection.
`  12`  `    {`
`  13`  `        public const string HeaderName = "X-CSRF-Token";`
  - → CSRF token ensure/validate.
`  14`  `        public const string FormFieldName = "__RequestVerificationToken";`
`  15`  `        public const string CookieName = "EduLMS.Csrf";`
  - → CSRF anti-forgery protection.
`  16`  `        public const string SessionKey = "EduLMS.CsrfToken";`
  - → CSRF anti-forgery protection.
`  17`  ``
`  18`  `        public static string EnsureToken(HttpContext ctx)`
  - → CSRF token ensure/validate.
`  19`  `        {`
`  20`  `            if (ctx == null || ctx.Session == null) return "";`
`  21`  `            string token = ctx.Session[SessionKey] as string;`
  - → Server session for logged-in user.
`  22`  `            if (string.IsNullOrEmpty(token))`
`  23`  `            {`
`  24`  `                var bytes = new byte[32];`
`  25`  `                using (var rng = RandomNumberGenerator.Create())`
  - → Import namespace/types.
`  26`  `                    rng.GetBytes(bytes);`
`  27`  `                token = Convert.ToBase64String(bytes)`
`  28`  `                    .TrimEnd('=').Replace('+', '-').Replace('/', '_');`
`  29`  `                ctx.Session[SessionKey] = token;`
  - → Server session for logged-in user.
`  30`  `            }`
`  31`  ``
`  32`  `            // Non-HttpOnly so JS can read for AJAX (double-submit with session)`
`  33`  `            try`
  - → Error handling block.
`  34`  `            {`
`  35`  `                var cookie = new HttpCookie(CookieName, token)`
`  36`  `                {`
`  37`  `                    HttpOnly = false,`
`  38`  `                    Path = "/",`
`  39`  `                    Secure = ctx.Request != null && ctx.Request.IsSecureConnection`
`  40`  `                };`
`  41`  `                try { cookie.SameSite = SameSiteMode.Lax; } catch { }`
  - → Error handling block.
`  42`  `                ctx.Response.Cookies.Set(cookie);`
`  43`  `            }`
`  44`  `            catch { }`
  - → Handle/log exception.
`  45`  ``
`  46`  `            return token;`
`  47`  `        }`
`  48`  ``
`  49`  `        public static bool IsSafeMethod(string method)`
`  50`  `        {`
`  51`  `            if (string.IsNullOrEmpty(method)) return true;`
`  52`  `            method = method.ToUpperInvariant();`
`  53`  `            return method == "GET" || method == "HEAD" || method == "OPTIONS" || method == "TRACE";`
`  54`  `        }`
`  55`  ``
`  56`  `        /// <summary>Validate CSRF for mutating requests. Safe methods always pass.</summary>`
`  57`  `        public static bool Validate(HttpContext ctx)`
`  58`  `        {`
`  59`  `            if (ctx == null || ctx.Request == null) return false;`
`  60`  `            if (IsSafeMethod(ctx.Request.HttpMethod)) return true;`
`  61`  ``
`  62`  `            // Ensure session exists`
`  63`  `            if (ctx.Session == null) return false;`
`  64`  `            string sessionToken = ctx.Session[SessionKey] as string;`
  - → Server session for logged-in user.
`  65`  `            if (string.IsNullOrEmpty(sessionToken))`
`  66`  `            {`
`  67`  `                // First mutating call without prior page load — issue token but reject this request`
`  68`  `                EnsureToken(ctx);`
  - → CSRF token ensure/validate.
`  69`  `                return false;`
`  70`  `            }`
`  71`  ``
`  72`  `            string provided = ctx.Request.Headers[HeaderName];`
`  73`  `            if (string.IsNullOrEmpty(provided))`
`  74`  `                provided = ctx.Request.Headers["RequestVerificationToken"];`
`  75`  `            if (string.IsNullOrEmpty(provided))`
`  76`  `                provided = ctx.Request.Form[FormFieldName];`
`  77`  `            if (string.IsNullOrEmpty(provided))`
`  78`  `                provided = ctx.Request[FormFieldName];`
`  79`  ``
`  80`  `            // Fallback: cookie must match session (double-submit)`
`  81`  `            if (string.IsNullOrEmpty(provided))`
`  82`  `            {`
`  83`  `                var c = ctx.Request.Cookies[CookieName];`
`  84`  `                if (c != null) provided = c.Value;`
`  85`  `            }`
`  86`  ``
`  87`  `            if (string.IsNullOrEmpty(provided)) return false;`
`  88`  `            return FixedTimeEquals(sessionToken, provided.Trim());`
  - → Constant-time string compare (reduce timing leaks).
`  89`  `        }`
`  90`  ``
`  91`  `        public static bool ValidateOrReject(HttpContext ctx, bool writeJsonError = true)`
`  92`  `        {`
`  93`  `            if (Validate(ctx)) return true;`
`  94`  `            if (writeJsonError && ctx != null && ctx.Response != null)`
`  95`  `            {`
`  96`  `                try`
  - → Error handling block.
`  97`  `                {`
`  98`  `                    ctx.Response.Clear();`
`  99`  `                    ctx.Response.StatusCode = 403;`
` 100`  `                    ctx.Response.TrySkipIisCustomErrors = true;`
` 101`  `                    ctx.Response.ContentType = "application/json; charset=utf-8";`
` 102`  `                    ctx.Response.Write("{\"success\":false,\"csrf\":true,\"message\":\"CSRF validation failed. Refresh the page and try again.\"}");`
  - → CSRF anti-forgery protection.
` 103`  `                }`
` 104`  `                catch { }`
  - → Handle/log exception.
` 105`  `            }`
` 106`  `            return false;`
` 107`  `        }`
` 108`  ``
` 109`  `        private static bool FixedTimeEquals(string a, string b)`
  - → Constant-time string compare (reduce timing leaks).
` 110`  `        {`
` 111`  `            if (a == null || b == null || a.Length != b.Length) return false;`
` 112`  `            int diff = 0;`
` 113`  `            for (int i = 0; i < a.Length; i++)`
` 114`  `                diff |= a[i] ^ b[i];`
` 115`  `            return diff == 0;`
` 116`  `        }`
` 117`  ``
` 118`  `        public static string MetaTag(HttpContext ctx)`
` 119`  `        {`
` 120`  `            string t = HttpUtility.HtmlAttributeEncode(EnsureToken(ctx));`
  - → CSRF token ensure/validate.
` 121`  `            return "<meta name=\"csrf-token\" content=\"" + t + "\" />";`
  - → CSRF anti-forgery protection.
` 122`  `        }`
` 123`  `    }`
` 124`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.Security.Cryptography;
using System.Text;
using System.Web;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// Session CSRF token + JS-readable cookie. Clients send X-CSRF-Token on mutating requests.
    /// </summary>
    public static class CsrfProtection
    {
        public const string HeaderName = "X-CSRF-Token";
        public const string FormFieldName = "__RequestVerificationToken";
        public const string CookieName = "EduLMS.Csrf";
        public const string SessionKey = "EduLMS.CsrfToken";

        public static string EnsureToken(HttpContext ctx)
        {
            if (ctx == null || ctx.Session == null) return "";
            string token = ctx.Session[SessionKey] as string;
            if (string.IsNullOrEmpty(token))
            {
                var bytes = new byte[32];
                using (var rng = RandomNumberGenerator.Create())
                    rng.GetBytes(bytes);
                token = Convert.ToBase64String(bytes)
                    .TrimEnd('=').Replace('+', '-').Replace('/', '_');
                ctx.Session[SessionKey] = token;
            }

            // Non-HttpOnly so JS can read for AJAX (double-submit with session)
            try
            {
                var cookie = new HttpCookie(CookieName, token)
                {
                    HttpOnly = false,
                    Path = "/",
                    Secure = ctx.Request != null && ctx.Request.IsSecureConnection
                };
                try { cookie.SameSite = SameSiteMode.Lax; } catch { }
                ctx.Response.Cookies.Set(cookie);
            }
            catch { }

            return token;
        }

        public static bool IsSafeMethod(string method)
        {
            if (string.IsNullOrEmpty(method)) return true;
            method = method.ToUpperInvariant();
            return method == "GET" || method == "HEAD" || method == "OPTIONS" || method == "TRACE";
        }

        /// <summary>Validate CSRF for mutating requests. Safe methods always pass.</summary>
        public static bool Validate(HttpContext ctx)
        {
            if (ctx == null || ctx.Request == null) return false;
            if (IsSafeMethod(ctx.Request.HttpMethod)) return true;

            // Ensure session exists
            if (ctx.Session == null) return false;
            string sessionToken = ctx.Session[SessionKey] as string;
            if (string.IsNullOrEmpty(sessionToken))
            {
                // First mutating call without prior page load — issue token but reject this request
                EnsureToken(ctx);
                return false;
            }

            string provided = ctx.Request.Headers[HeaderName];
            if (string.IsNullOrEmpty(provided))
                provided = ctx.Request.Headers["RequestVerificationToken"];
            if (string.IsNullOrEmpty(provided))
                provided = ctx.Request.Form[FormFieldName];
            if (string.IsNullOrEmpty(provided))
                provided = ctx.Request[FormFieldName];

            // Fallback: cookie must match session (double-submit)
            if (string.IsNullOrEmpty(provided))
            {
                var c = ctx.Request.Cookies[CookieName];
                if (c != null) provided = c.Value;
            }

            if (string.IsNullOrEmpty(provided)) return false;
            return FixedTimeEquals(sessionToken, provided.Trim());
        }

        public static bool ValidateOrReject(HttpContext ctx, bool writeJsonError = true)
        {
            if (Validate(ctx)) return true;
            if (writeJsonError && ctx != null && ctx.Response != null)
            {
                try
                {
                    ctx.Response.Clear();
                    ctx.Response.StatusCode = 403;
                    ctx.Response.TrySkipIisCustomErrors = true;
                    ctx.Response.ContentType = "application/json; charset=utf-8";
                    ctx.Response.Write("{\"success\":false,\"csrf\":true,\"message\":\"CSRF validation failed. Refresh the page and try again.\"}");
                }
                catch { }
            }
            return false;
        }

        private static bool FixedTimeEquals(string a, string b)
        {
            if (a == null || b == null || a.Length != b.Length) return false;
            int diff = 0;
            for (int i = 0; i < a.Length; i++)
                diff |= a[i] ^ b[i];
            return diff == 0;
        }

        public static string MetaTag(HttpContext ctx)
        {
            string t = HttpUtility.HtmlAttributeEncode(EnsureToken(ctx));
            return "<meta name=\"csrf-token\" content=\"" + t + "\" />";
        }
    }
}

```
