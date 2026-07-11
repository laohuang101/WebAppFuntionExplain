# JwtHelper.cs
**Source:** `Data/Security/JwtHelper.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

HS256 JWT create/validate and EduLMS.Auth cookie set/clear for session restore.

## File overview

- **Total lines:** 195
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 18:** `Json` (`JavaScriptSerializer`) — **JSON string (to parse or serialize).**
- **Line 24:** `s` (`var`) — **String value or submission-related object.**
- **Line 27:** `s` (`return`) — **String value or submission-related object.**
- **Line 35:** `h` (`int`) — **Holds “h” for this scope. (integer)**
- **Line 37:** `h` (`return`) — **Holds “h” for this scope. (type `return`)**
- **Line 38:** `12` (`return`) — **Holds “12” for this scope. (type `return`)**
- **Line 44:** `header` (`var`) — **Holds “header” for this scope.**
- **Line 49:** `now` (`long`) — **Current time (usually UTC or server local).**
- **Line 50:** `payload` (`var`) — **Object about to be JSON-serialized or sent over network.**
- **Line 58:** `h` (`string`) — **Holds “h” for this scope. (text)**
- **Line 60:** `p` (`string`) — **Parameter, path, or password fragment depending on context.**
- **Line 61:** `sig` (`string`) — **Holds “sig” for this scope. (text)**
- **Line 71:** `parts` (`var`) — **Split path or name segments.**
- **Line 74:** `data` (`string`) — **Holds “data” for this scope. (text)**
- **Line 76:** `expected` (`string`) — **Holds “expected” for this scope. (text)**
- **Line 81:** `json` (`var`) — **JSON string (to parse or serialize).**
- **Line 82:** `payload` (`var`) — **Object about to be JSON-serialized or sent over network.**
- **Line 84:** `exp` (`long`) — **Expiry DateTime.**
- **Line 95:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 104:** `forced` (`string`) — **Holds “forced” for this scope. (text)**
- **Line 109:** `req` (`var`) — **Holds “req” for this scope.**
- **Line 119:** `cookie` (`var`) — **HTTP cookie (JWT or CSRF).**
- **Line 138:** `cookie` (`var`) — **HTTP cookie (JWT or CSRF).**
- **Line 152:** `c` (`var`) — **Temporary value (character, course, or counter depending on loop).**
- **Line 160:** `hash` (`var`) — **Password hash (PBKDF2) stored in DB.**
- **Line 172:** `s` (`string`) — **String being cleaned or built.**
- **Line 184:** `diff` (`int`) — **Holds “diff” for this scope. (integer)**
- **Line 187:** `diff` (`return`) — **Holds “diff” for this scope. (type `return`)**

## Functions / methods (10 found)

### `CreateToken` — lines 41–63

```csharp
public static string CreateToken(int uid, string name, string role)
```

#### Explanation

- **Purpose:** Implements `CreateToken`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- `name` (`string`) — Display name of user/course/criterion.
- `role` (`string`) — User role code or name (Admin/Student/Lecturer).
- **Local variables (what each means):**
- `header` (`var`) — Holds “header” for this scope.  Newly constructed object.
- `now` (`long`) — Current time (usually UTC or server local).
- `payload` (`var`) — Object about to be JSON-serialized or sent over network.  Newly constructed object.
- `h` (`string`) — Holds “h” for this scope. (text)  JSON serialize/parse result.
- `p` (`string`) — Parameter, path, or password fragment depending on context.  JSON serialize/parse result.
- `sig` (`string`) — Holds “sig” for this scope. (text)

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L44:** `header` means: Holds “header” for this scope.  Newly constructed object.
- **L46:** JWT cookie create/validate/clear.
- **L49:** `now` means: Current time (usually UTC or server local).
- **L50:** `payload` means: Object about to be JSON-serialized or sent over network.  Newly constructed object.
- **L59:** `h` means: Holds “h” for this scope. (text)  JSON serialize/parse result.
- **L60:** `p` means: Parameter, path, or password fragment depending on context.  JSON serialize/parse result.
- **L61:** `sig` means: Holds “sig” for this scope. (text)

---

### `TryValidate` — lines 64–97

```csharp
public static bool TryValidate(string token, out int uid, out string name, out string role)
```

#### Explanation

- **Purpose:** Implements `TryValidate`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `token` (`string`) — JWT or CSRF token string.
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- `name` (`string`) — Display name of user/course/criterion.
- `role` (`string`) — User role code or name (Admin/Student/Lecturer).
- **Local variables (what each means):**
- `parts` (`var`) — Split path or name segments.
- `data` (`string`) — Holds “data” for this scope. (text)
- `expected` (`string`) — Holds “expected” for this scope. (text)
- `json` (`var`) — JSON string (to parse or serialize).
- `payload` (`var`) — Object about to be JSON-serialized or sent over network.  JSON serialize/parse result.
- `exp` (`long`) — Expiry DateTime.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L72:** `parts` means: Split path or name segments.
- **L75:** `data` means: Holds “data” for this scope. (text)
- **L76:** `expected` means: Holds “expected” for this scope. (text)
- **L77:** Constant-time string compare (reduce timing leaks).
- **L79:** Error handling block.
- **L81:** `json` means: JSON string (to parse or serialize).
- **L82:** `payload` means: Object about to be JSON-serialized or sent over network.  JSON serialize/parse result.
- **L85:** `exp` means: Expiry DateTime.
- **L93:** Handle/log exception.

---

### `SetAuthCookie` — lines 115–133

```csharp
public static void SetAuthCookie(HttpResponse response, string token)
```

#### Explanation

- **Purpose:** Implements `SetAuthCookie`.
- **Pattern:** Persist changes.
- **Parameters (what each means):**
- `response` (`HttpResponse`) — Holds “response” for this scope. (type `HttpResponse`)
- `token` (`string`) — JWT or CSRF token string.
- **Local variables (what each means):**
- `cookie` (`var`) — HTTP cookie (JWT or CSRF).  Newly constructed object.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L119:** `cookie` means: HTTP cookie (JWT or CSRF).  Newly constructed object.
- **L126:** Error handling block.
- **L131:** Handle/log exception.

---

### `ClearAuthCookie` — lines 134–147

```csharp
public static void ClearAuthCookie(HttpResponse response)
```

#### Explanation

- **Purpose:** Implements `ClearAuthCookie`.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `response` (`HttpResponse`) — Holds “response” for this scope. (type `HttpResponse`)
- **Local variables (what each means):**
- `cookie` (`var`) — HTTP cookie (JWT or CSRF).  Newly constructed object.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L138:** `cookie` means: HTTP cookie (JWT or CSRF).  Newly constructed object.
- **L145:** Error handling block.

---

### `ReadToken` — lines 148–154

```csharp
public static string ReadToken(HttpRequest request)
```

#### Explanation

- **Purpose:** Implements `ReadToken`.
- **Parameters (what each means):**
- `request` (`HttpRequest`) — Holds “request” for this scope. (type `HttpRequest`)
- **Local variables (what each means):**
- `c` (`var`) — Temporary value (character, course, or counter depending on loop).

#### Line-by-line (this function)

```csharp
 148 | 
 149 |         public static string ReadToken(HttpRequest request)
 150 |         {
 151 |             if (request == null) return null;
 152 |             var c = request.Cookies[CookieName];
 153 |             return c != null ? c.Value : null;
 154 |         }
```

**Line notes** (what code + variables mean)

- **L152:** `c` means: Temporary value (character, course, or counter depending on loop).

---

### `Sign` — lines 155–163

```csharp
private static string Sign(string data)
```

#### Explanation

- **Purpose:** Implements `Sign`.
- **Parameters (what each means):**
- `data` (`string`) — Holds “data” for this scope. (text)
- **Local variables (what each means):**
- `hmac` (`var`) — Holds “hmac” for this scope.  Newly constructed object.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L158:** Import namespace/types.
- **L160:** `hash` means: Password hash (PBKDF2) stored in DB.  Assigned from password hash function.

---

### `Base64UrlEncode` — lines 164–168

```csharp
private static string Base64UrlEncode(byte[] input)
```

#### Explanation

- **Purpose:** Implements `Base64UrlEncode`.
- **Parameters (what each means):**
- `input` (`byte[]`) — Holds “input” for this scope. (type `byte[]`)

#### Line-by-line (this function)

```csharp
 164 | 
 165 |         private static string Base64UrlEncode(byte[] input)
 166 |         {
 167 |             return Convert.ToBase64String(input).TrimEnd('=').Replace('+', '-').Replace('/', '_');
 168 |         }
```

---

### `Base64UrlDecode` — lines 169–179

```csharp
private static byte[] Base64UrlDecode(string input)
```

#### Explanation

- **Purpose:** Implements `Base64UrlDecode`.
- **Parameters (what each means):**
- `input` (`string`) — Holds “input” for this scope. (text)
- **Local variables (what each means):**
- `s` (`string`) — String being cleaned or built.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L172:** `s` means: String being cleaned or built.

---

### `FixedTimeEquals` — lines 180–188

```csharp
private static bool FixedTimeEquals(string a, string b)
```

#### Explanation

- **Purpose:** Implements `FixedTimeEquals`.
- **Parameters (what each means):**
- `a` (`string`) — Holds “a” for this scope. (text)
- `b` (`string`) — Holds “b” for this scope. (text)
- **Local variables (what each means):**
- `diff` (`int`) — Holds “diff” for this scope. (integer)  Literal number `0`.
- `i` (`int`) — Loop index (0-based counter in for-loops).  Literal number `0`.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L181:** Constant-time string compare (reduce timing leaks).
- **L184:** `diff` means: Holds “diff” for this scope. (integer)  Literal number `0`.

---

### `UnixNow` — lines 189–193

```csharp
private static long UnixNow()
```

#### Explanation

- **Purpose:** Implements `UnixNow`.

#### Line-by-line (this function)

```csharp
 189 | 
 190 |         private static long UnixNow()
 191 |         {
 192 |             return (long)(DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc)).TotalSeconds;
 193 |         }
```

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L7:** Import namespace/types.
- **L9:** C# namespace grouping.
- **L15:** JWT cookie create/validate/clear.
- **L17:** JWT cookie create/validate/clear.
- **L24:** `s` means: String value or submission-related object.  Read from Web.config.
- **L44:** `header` means: Holds “header” for this scope.  Newly constructed object.
- **L46:** JWT cookie create/validate/clear.
- **L49:** `now` means: Current time (usually UTC or server local).
- **L50:** `payload` means: Object about to be JSON-serialized or sent over network.  Newly constructed object.
- **L59:** `h` means: Holds “h” for this scope. (text)  JSON serialize/parse result.
- **L60:** `p` means: Parameter, path, or password fragment depending on context.  JSON serialize/parse result.
- **L61:** `sig` means: Holds “sig” for this scope. (text)
- **L72:** `parts` means: Split path or name segments.
- **L75:** `data` means: Holds “data” for this scope. (text)
- **L76:** `expected` means: Holds “expected” for this scope. (text)
- **L77:** Constant-time string compare (reduce timing leaks).
- **L79:** Error handling block.
- **L81:** `json` means: JSON string (to parse or serialize).
- **L82:** `payload` means: Object about to be JSON-serialized or sent over network.  JSON serialize/parse result.
- **L85:** `exp` means: Expiry DateTime.
- **L93:** Handle/log exception.
- **L104:** `forced` means: Holds “forced” for this scope. (text)  Read from Web.config.
- **L107:** Error handling block.
- **L109:** `req` means: Holds “req” for this scope.
- **L112:** Handle/log exception.
- **L119:** `cookie` means: HTTP cookie (JWT or CSRF).  Newly constructed object.
- **L126:** Error handling block.
- **L131:** Handle/log exception.
- **L138:** `cookie` means: HTTP cookie (JWT or CSRF).  Newly constructed object.
- **L145:** Error handling block.
- **L152:** `c` means: Temporary value (character, course, or counter depending on loop).
- **L158:** Import namespace/types.
- **L160:** `hash` means: Password hash (PBKDF2) stored in DB.  Assigned from password hash function.
- **L172:** `s` means: String being cleaned or built.
- **L181:** Constant-time string compare (reduce timing leaks).
- **L184:** `diff` means: Holds “diff” for this scope. (integer)  Literal number `0`.

## Source snapshot (raw)

```csharp
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Security.Cryptography;
using System.Text;
using System.Web;
using System.Web.Script.Serialization;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// Compact HS256 JWT (no NuGet). Cookie name: EduLMS.Auth
    /// Claims: sub (uid), name, role, exp, iat
    /// </summary>
    public static class JwtHelper
    {
        public const string CookieName = "EduLMS.Auth";
        private static readonly JavaScriptSerializer Json = new JavaScriptSerializer();

        private static string Secret
        {
            get
            {
                var s = ConfigurationManager.AppSettings["JwtSecret"];
                if (string.IsNullOrWhiteSpace(s))
                s = "EduLMS-Dev-Secret-Change-Me-In-Production-2026!";
                return s;
            }
        }

        private static int ExpiryHours
        {
            get
            {
                int h;
                if (int.TryParse(ConfigurationManager.AppSettings["JwtExpiryHours"], out h) && h > 0)
                return h;
                return 12;
            }
        }

        public static string CreateToken(int uid, string name, string role)
        {
            var header = new Dictionary<string, object>
            {
                { "alg", "HS256" },
                { "typ", "JWT" }
            };
            long now = UnixNow();
            var payload = new Dictionary<string, object>
            {
                { "sub", uid.ToString() },
                { "name", name ?? "" },
                { "role", role ?? "Student" },
                { "iat", now },
                { "exp", now + (ExpiryHours * 3600L) }
            };

            string h = Base64UrlEncode(Encoding.UTF8.GetBytes(Json.Serialize(header)));
            string p = Base64UrlEncode(Encoding.UTF8.GetBytes(Json.Serialize(payload)));
            string sig = Sign(h + "." + p);
            return h + "." + p + "." + sig;
        }

        public static bool TryValidate(string token, out int uid, out string name, out string role)
        {
            uid = 0;
            name = null;
            role = null;
            if (string.IsNullOrWhiteSpace(token)) return false;

            var parts = token.Split('.');
            if (parts.Length != 3) return false;

            string data = parts[0] + "." + parts[1];
            string expected = Sign(data);
            if (!FixedTimeEquals(expected, parts[2])) return false;

            try
            {
                var json = Encoding.UTF8.GetString(Base64UrlDecode(parts[1]));
                var payload = Json.Deserialize<Dictionary<string, object>>(json);
                if (payload == null) return false;

                long exp = Convert.ToInt64(payload["exp"]);
                if (UnixNow() > exp) return false;

                uid = Convert.ToInt32(payload["sub"].ToString());
                name = payload.ContainsKey("name") ? Convert.ToString(payload["name"]) : "";
                role = payload.ContainsKey("role") ? Convert.ToString(payload["role"]) : "Student";
                return uid > 0;
            }
            catch
            {
                return false;
            }
        }

        private static bool UseSecureCookie
        {
            get
            {
                // Prefer HTTPS when request is secure, or when forced in config
                string forced = ConfigurationManager.AppSettings["JwtCookieSecure"];
                if (string.Equals(forced, "true", StringComparison.OrdinalIgnoreCase)) return true;
                if (string.Equals(forced, "false", StringComparison.OrdinalIgnoreCase)) return false;
                try
                {
                    var req = HttpContext.Current != null ? HttpContext.Current.Request : null;
                    return req != null && req.IsSecureConnection;
                }
                catch { return false; }
            }
        }

        public static void SetAuthCookie(HttpResponse response, string token)
        {
            if (response == null) return;
            var cookie = new HttpCookie(CookieName, token)
            {
                HttpOnly = true,
                Secure = UseSecureCookie,
                Path = "/",
                Expires = DateTime.UtcNow.AddHours(ExpiryHours)
            };
            try
            {
                // .NET 4.7.2+ SameSite
                cookie.SameSite = SameSiteMode.Lax;
            }
            catch { }
            response.Cookies.Set(cookie);
        }

        public static void ClearAuthCookie(HttpResponse response)
        {
            if (response == null) return;
            var cookie = new HttpCookie(CookieName, "")
            {
                HttpOnly = true,
                Secure = UseSecureCookie,
                Path = "/",
                Expires = DateTime.UtcNow.AddDays(-1)
            };
            try { cookie.SameSite = SameSiteMode.Lax; } catch { }
            response.Cookies.Set(cookie);
        }

        public static string ReadToken(HttpRequest request)
        {
            if (request == null) return null;
            var c = request.Cookies[CookieName];
            return c != null ? c.Value : null;
        }

        private static string Sign(string data)
        {
            using (var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(Secret)))
            {
                var hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(data));
                return Base64UrlEncode(hash);
            }
        }

        private static string Base64UrlEncode(byte[] input)
        {
            return Convert.ToBase64String(input).TrimEnd('=').Replace('+', '-').Replace('/', '_');
        }

        private static byte[] Base64UrlDecode(string input)
        {
            string s = input.Replace('-', '+').Replace('_', '/');
            switch (s.Length % 4)
            {
                case 2: s += "=="; break;
                case 3: s += "="; break;
            }
            return Convert.FromBase64String(s);
        }

        private static bool FixedTimeEquals(string a, string b)
        {
            if (a == null || b == null || a.Length != b.Length) return false;
            int diff = 0;
            for (int i = 0; i < a.Length; i++)
            diff |= a[i] ^ b[i];
            return diff == 0;
        }

        private static long UnixNow()
        {
            return (long)(DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc)).TotalSeconds;
        }
    }
}

```
