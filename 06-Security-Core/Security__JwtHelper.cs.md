# JwtHelper.cs
**Source:** `Data/Security/JwtHelper.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

HS256 JWT create/validate and EduLMS.Auth cookie set/clear for session restore.

## File overview

- **Total lines:** 195
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `Json` | `JavaScriptSerializer` | JSON string (to parse or serialize). |

## Functions / methods (10 found)

### `CreateToken` — lines 41–63

#### Signature

```csharp
public static string CreateToken(int uid, string name, string role)
```

#### What it is

Builds a signed JWT string for the logged-in user.

#### How it works

1. Starts when something calls `CreateToken`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `name` | `string` | Display name of user/course/criterion. |
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `header` | `var` | Holds “header” for this scope.  Newly constructed object. |
| `now` | `long` | Current time (usually UTC or server local). |
| `payload` | `var` | Object about to be JSON-serialized or sent over network.  Newly constructed object. |
| `h` | `string` | Holds “h” for this scope. (text)  JSON serialize/parse result. |
| `p` | `string` | Parameter, path, or password fragment depending on context.  JSON serialize/parse result. |
| `sig` | `string` | Holds “sig” for this scope. (text) |

#### Code

```csharp
  41 | 
  42 |         public static string CreateToken(int uid, string name, string role)
  43 |         {
  44 |             var header = new Dictionary<string, object>
  45 |             {
  46 |                 { "alg", "HS256" },
  47 |                 { "typ", "JWT" }
  48 |             };
  49 |             long now = UnixNow();
  50 |             var payload = new Dictionary<string, object>
  51 |             {
  52 |                 { "sub", uid.ToString() },
  53 |                 { "name", name ?? "" },
  54 |                 { "role", role ?? "Student" },
  55 |                 { "iat", now },
  56 |                 { "exp", now + (ExpiryHours * 3600L) }
  57 |             };
  58 | 
  59 |             string h = Base64UrlEncode(Encoding.UTF8.GetBytes(Json.Serialize(header)));
  60 |             string p = Base64UrlEncode(Encoding.UTF8.GetBytes(Json.Serialize(payload)));
  61 |             string sig = Sign(h + "." + p);
  62 |             return h + "." + p + "." + sig;
  63 |         }
```

---

### `TryValidate` — lines 64–97

#### Signature

```csharp
public static bool TryValidate(string token, out int uid, out string name, out string role)
```

#### What it is

Checks whether a JWT cookie is valid and extracts user claims.

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `token` | `string` | JWT or CSRF token string. |
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `name` | `string` | Display name of user/course/criterion. |
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `parts` | `var` | Split path or name segments. |
| `data` | `string` | Holds “data” for this scope. (text) |
| `expected` | `string` | Holds “expected” for this scope. (text) |
| `json` | `var` | JSON string (to parse or serialize). |
| `payload` | `var` | Object about to be JSON-serialized or sent over network.  JSON serialize/parse result. |
| `exp` | `long` | Expiry DateTime. |

#### Code

```csharp
  64 | 
  65 |         public static bool TryValidate(string token, out int uid, out string name, out string role)
  66 |         {
  67 |             uid = 0;
  68 |             name = null;
  69 |             role = null;
  70 |             if (string.IsNullOrWhiteSpace(token)) return false;
  71 | 
  72 |             var parts = token.Split('.');
  73 |             if (parts.Length != 3) return false;
  74 | 
  75 |             string data = parts[0] + "." + parts[1];
  76 |             string expected = Sign(data);
  77 |             if (!FixedTimeEquals(expected, parts[2])) return false;
  78 | 
  79 |             try
  80 |             {
  81 |                 var json = Encoding.UTF8.GetString(Base64UrlDecode(parts[1]));
  82 |                 var payload = Json.Deserialize<Dictionary<string, object>>(json);
  83 |                 if (payload == null) return false;
  84 | 
  85 |                 long exp = Convert.ToInt64(payload["exp"]);
  86 |                 if (UnixNow() > exp) return false;
  87 | 
  88 |                 uid = Convert.ToInt32(payload["sub"].ToString());
  89 |                 name = payload.ContainsKey("name") ? Convert.ToString(payload["name"]) : "";
  90 |                 role = payload.ContainsKey("role") ? Convert.ToString(payload["role"]) : "Student";
  91 |                 return uid > 0;
  92 |             }
  93 |             catch
  94 |             {
  95 |                 return false;
  96 |             }
  97 |         }
```

---

### `SetAuthCookie` — lines 115–133

#### Signature

```csharp
public static void SetAuthCookie(HttpResponse response, string token)
```

#### What it is

Saves the JWT into the browser cookie `EduLMS.Auth`.

#### How it works

1. Starts when something calls `SetAuthCookie`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `response` | `HttpResponse` | Holds “response” for this scope. (type `HttpResponse`) |
| `token` | `string` | JWT or CSRF token string. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cookie` | `var` | HTTP cookie (JWT or CSRF).  Newly constructed object. |

#### Code

```csharp
 115 | 
 116 |         public static void SetAuthCookie(HttpResponse response, string token)
 117 |         {
 118 |             if (response == null) return;
 119 |             var cookie = new HttpCookie(CookieName, token)
 120 |             {
 121 |                 HttpOnly = true,
 122 |                 Secure = UseSecureCookie,
 123 |                 Path = "/",
 124 |                 Expires = DateTime.UtcNow.AddHours(ExpiryHours)
 125 |             };
 126 |             try
 127 |             {
 128 |                 // .NET 4.7.2+ SameSite
 129 |                 cookie.SameSite = SameSiteMode.Lax;
 130 |             }
 131 |             catch { }
 132 |             response.Cookies.Set(cookie);
 133 |         }
```

---

### `ClearAuthCookie` — lines 134–147

#### Signature

```csharp
public static void ClearAuthCookie(HttpResponse response)
```

#### What it is

Removes the JWT auth cookie (logout).

#### How it works

1. Starts when something calls `ClearAuthCookie`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `response` | `HttpResponse` | Holds “response” for this scope. (type `HttpResponse`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cookie` | `var` | HTTP cookie (JWT or CSRF).  Newly constructed object. |

#### Code

```csharp
 134 | 
 135 |         public static void ClearAuthCookie(HttpResponse response)
 136 |         {
 137 |             if (response == null) return;
 138 |             var cookie = new HttpCookie(CookieName, "")
 139 |             {
 140 |                 HttpOnly = true,
 141 |                 Secure = UseSecureCookie,
 142 |                 Path = "/",
 143 |                 Expires = DateTime.UtcNow.AddDays(-1)
 144 |             };
 145 |             try { cookie.SameSite = SameSiteMode.Lax; } catch { }
 146 |             response.Cookies.Set(cookie);
 147 |         }
```

---

### `ReadToken` — lines 148–154

#### Signature

```csharp
public static string ReadToken(HttpRequest request)
```

#### What it is

Reads/loads data related to **Read Token** and returns it for display or further use.

#### How it works

1. Starts when something calls `ReadToken`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `request` | `HttpRequest` | Holds “request” for this scope. (type `HttpRequest`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `c` | `var` | Temporary value (character, course, or counter depending on loop). |

#### Code

```csharp
 148 | 
 149 |         public static string ReadToken(HttpRequest request)
 150 |         {
 151 |             if (request == null) return null;
 152 |             var c = request.Cookies[CookieName];
 153 |             return c != null ? c.Value : null;
 154 |         }
```

---

### `Sign` — lines 155–163

#### Signature

```csharp
private static string Sign(string data)
```

#### What it is

Function `Sign` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Sign`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `data` | `string` | Holds “data” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `hmac` | `var` | Holds “hmac” for this scope.  Newly constructed object. |

#### Code

```csharp
 155 | 
 156 |         private static string Sign(string data)
 157 |         {
 158 |             using (var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(Secret)))
 159 |             {
 160 |                 var hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(data));
 161 |                 return Base64UrlEncode(hash);
 162 |             }
 163 |         }
```

---

### `Base64UrlEncode` — lines 164–168

#### Signature

```csharp
private static string Base64UrlEncode(byte[] input)
```

#### What it is

Function `Base64UrlEncode` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Base64UrlEncode`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `input` | `byte[]` | Holds “input” for this scope. (type `byte[]`) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 164 | 
 165 |         private static string Base64UrlEncode(byte[] input)
 166 |         {
 167 |             return Convert.ToBase64String(input).TrimEnd('=').Replace('+', '-').Replace('/', '_');
 168 |         }
```

---

### `Base64UrlDecode` — lines 169–179

#### Signature

```csharp
private static byte[] Base64UrlDecode(string input)
```

#### What it is

Function `Base64UrlDecode` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Base64UrlDecode`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `input` | `string` | Holds “input” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `string` | String being cleaned or built. |

#### Code

```csharp
 169 | 
 170 |         private static byte[] Base64UrlDecode(string input)
 171 |         {
 172 |             string s = input.Replace('-', '+').Replace('_', '/');
 173 |             switch (s.Length % 4)
 174 |             {
 175 |                 case 2: s += "=="; break;
 176 |                 case 3: s += "="; break;
 177 |             }
 178 |             return Convert.FromBase64String(s);
 179 |         }
```

---

### `FixedTimeEquals` — lines 180–188

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
 180 | 
 181 |         private static bool FixedTimeEquals(string a, string b)
 182 |         {
 183 |             if (a == null || b == null || a.Length != b.Length) return false;
 184 |             int diff = 0;
 185 |             for (int i = 0; i < a.Length; i++)
 186 |             diff |= a[i] ^ b[i];
 187 |             return diff == 0;
 188 |         }
```

---

### `UnixNow` — lines 189–193

#### Signature

```csharp
private static long UnixNow()
```

#### What it is

Function `UnixNow` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `UnixNow`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 189 | 
 190 |         private static long UnixNow()
 191 |         {
 192 |             return (long)(DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc)).TotalSeconds;
 193 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Collections.Generic;
   3 | using System.Configuration;
   4 | using System.Security.Cryptography;
   5 | using System.Text;
   6 | using System.Web;
   7 | using System.Web.Script.Serialization;
   8 | 
   9 | namespace WebAppAssignment.Data.Security
  10 | {
  11 |     /// <summary>
  12 |     /// Compact HS256 JWT (no NuGet). Cookie name: EduLMS.Auth
  13 |     /// Claims: sub (uid), name, role, exp, iat
  14 |     /// </summary>
  15 |     public static class JwtHelper
  16 |     {
  17 |         public const string CookieName = "EduLMS.Auth";
  18 |         private static readonly JavaScriptSerializer Json = new JavaScriptSerializer();
  19 | 
  20 |         private static string Secret
  21 |         {
  22 |             get
  23 |             {
  24 |                 var s = ConfigurationManager.AppSettings["JwtSecret"];
  25 |                 if (string.IsNullOrWhiteSpace(s))
  26 |                 s = "EduLMS-Dev-Secret-Change-Me-In-Production-2026!";
  27 |                 return s;
  28 |             }
  29 |         }
  30 | 
  31 |         private static int ExpiryHours
  32 |         {
  33 |             get
  34 |             {
  35 |                 int h;
  36 |                 if (int.TryParse(ConfigurationManager.AppSettings["JwtExpiryHours"], out h) && h > 0)
  37 |                 return h;
  38 |                 return 12;
  39 |             }
  40 |         }
  41 | 
  42 |         public static string CreateToken(int uid, string name, string role)
  43 |         {
  44 |             var header = new Dictionary<string, object>
  45 |             {
  46 |                 { "alg", "HS256" },
  47 |                 { "typ", "JWT" }
  48 |             };
  49 |             long now = UnixNow();
  50 |             var payload = new Dictionary<string, object>
  51 |             {
  52 |                 { "sub", uid.ToString() },
  53 |                 { "name", name ?? "" },
  54 |                 { "role", role ?? "Student" },
  55 |                 { "iat", now },
  56 |                 { "exp", now + (ExpiryHours * 3600L) }
  57 |             };
  58 | 
  59 |             string h = Base64UrlEncode(Encoding.UTF8.GetBytes(Json.Serialize(header)));
  60 |             string p = Base64UrlEncode(Encoding.UTF8.GetBytes(Json.Serialize(payload)));
  61 |             string sig = Sign(h + "." + p);
  62 |             return h + "." + p + "." + sig;
  63 |         }
  64 | 
  65 |         public static bool TryValidate(string token, out int uid, out string name, out string role)
  66 |         {
  67 |             uid = 0;
  68 |             name = null;
  69 |             role = null;
  70 |             if (string.IsNullOrWhiteSpace(token)) return false;
  71 | 
  72 |             var parts = token.Split('.');
  73 |             if (parts.Length != 3) return false;
  74 | 
  75 |             string data = parts[0] + "." + parts[1];
  76 |             string expected = Sign(data);
  77 |             if (!FixedTimeEquals(expected, parts[2])) return false;
  78 | 
  79 |             try
  80 |             {
  81 |                 var json = Encoding.UTF8.GetString(Base64UrlDecode(parts[1]));
  82 |                 var payload = Json.Deserialize<Dictionary<string, object>>(json);
  83 |                 if (payload == null) return false;
  84 | 
  85 |                 long exp = Convert.ToInt64(payload["exp"]);
  86 |                 if (UnixNow() > exp) return false;
  87 | 
  88 |                 uid = Convert.ToInt32(payload["sub"].ToString());
  89 |                 name = payload.ContainsKey("name") ? Convert.ToString(payload["name"]) : "";
  90 |                 role = payload.ContainsKey("role") ? Convert.ToString(payload["role"]) : "Student";
  91 |                 return uid > 0;
  92 |             }
  93 |             catch
  94 |             {
  95 |                 return false;
  96 |             }
  97 |         }
  98 | 
  99 |         private static bool UseSecureCookie
 100 |         {
 101 |             get
 102 |             {
 103 |                 // Prefer HTTPS when request is secure, or when forced in config
 104 |                 string forced = ConfigurationManager.AppSettings["JwtCookieSecure"];
 105 |                 if (string.Equals(forced, "true", StringComparison.OrdinalIgnoreCase)) return true;
 106 |                 if (string.Equals(forced, "false", StringComparison.OrdinalIgnoreCase)) return false;
 107 |                 try
 108 |                 {
 109 |                     var req = HttpContext.Current != null ? HttpContext.Current.Request : null;
 110 |                     return req != null && req.IsSecureConnection;
 111 |                 }
 112 |                 catch { return false; }
 113 |             }
 114 |         }
 115 | 
 116 |         public static void SetAuthCookie(HttpResponse response, string token)
 117 |         {
 118 |             if (response == null) return;
 119 |             var cookie = new HttpCookie(CookieName, token)
 120 |             {
 121 |                 HttpOnly = true,
 122 |                 Secure = UseSecureCookie,
 123 |                 Path = "/",
 124 |                 Expires = DateTime.UtcNow.AddHours(ExpiryHours)
 125 |             };
 126 |             try
 127 |             {
 128 |                 // .NET 4.7.2+ SameSite
 129 |                 cookie.SameSite = SameSiteMode.Lax;
 130 |             }
 131 |             catch { }
 132 |             response.Cookies.Set(cookie);
 133 |         }
 134 | 
 135 |         public static void ClearAuthCookie(HttpResponse response)
 136 |         {
 137 |             if (response == null) return;
 138 |             var cookie = new HttpCookie(CookieName, "")
 139 |             {
 140 |                 HttpOnly = true,
 141 |                 Secure = UseSecureCookie,
 142 |                 Path = "/",
 143 |                 Expires = DateTime.UtcNow.AddDays(-1)
 144 |             };
 145 |             try { cookie.SameSite = SameSiteMode.Lax; } catch { }
 146 |             response.Cookies.Set(cookie);
 147 |         }
 148 | 
 149 |         public static string ReadToken(HttpRequest request)
 150 |         {
 151 |             if (request == null) return null;
 152 |             var c = request.Cookies[CookieName];
 153 |             return c != null ? c.Value : null;
 154 |         }
 155 | 
 156 |         private static string Sign(string data)
 157 |         {
 158 |             using (var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(Secret)))
 159 |             {
 160 |                 var hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(data));
 161 |                 return Base64UrlEncode(hash);
 162 |             }
 163 |         }
 164 | 
 165 |         private static string Base64UrlEncode(byte[] input)
 166 |         {
 167 |             return Convert.ToBase64String(input).TrimEnd('=').Replace('+', '-').Replace('/', '_');
 168 |         }
 169 | 
 170 |         private static byte[] Base64UrlDecode(string input)
 171 |         {
 172 |             string s = input.Replace('-', '+').Replace('_', '/');
 173 |             switch (s.Length % 4)
 174 |             {
 175 |                 case 2: s += "=="; break;
 176 |                 case 3: s += "="; break;
 177 |             }
 178 |             return Convert.FromBase64String(s);
 179 |         }
 180 | 
 181 |         private static bool FixedTimeEquals(string a, string b)
 182 |         {
 183 |             if (a == null || b == null || a.Length != b.Length) return false;
 184 |             int diff = 0;
 185 |             for (int i = 0; i < a.Length; i++)
 186 |             diff |= a[i] ^ b[i];
 187 |             return diff == 0;
 188 |         }
 189 | 
 190 |         private static long UnixNow()
 191 |         {
 192 |             return (long)(DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc)).TotalSeconds;
 193 |         }
 194 |     }
 195 | }
```
