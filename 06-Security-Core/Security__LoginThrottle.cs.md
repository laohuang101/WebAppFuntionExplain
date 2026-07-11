# LoginThrottle.cs
**Source:** `Data/Security/LoginThrottle.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

In-memory brute-force protection per email+IP (failures, lockout window).

## File overview

- **Total lines:** 134
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `Failures` | `int` | Number of failed login attempts in the current window. |
| `WindowStartUtc` | `DateTime` | Date/time value. (date/time) |
| `LockedUntilUtc` | `DateTime?` | Date/time value. (date/time) |

## Functions / methods (4 found)

### `ClientKey` — lines 56–77

#### Signature

```csharp
public static string ClientKey(string email, HttpContext ctx)
```

#### What it is

Function `ClientKey` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `ClientKey`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `e` | `string` | Normalized email string (trimmed/lowercased). |
| `ip` | `string` | Client IP address for throttle/audit.  Literal text string. |
| `xff` | `string` | X-Forwarded-For header value (client IP when behind a proxy). |
| `comma` | `int` | Index of the first comma in a string (split helper). |

#### Code

```csharp
  56 | 
  57 |         public static string ClientKey(string email, HttpContext ctx)
  58 |         {
  59 |             string e = (email ?? "").Trim().ToLowerInvariant();
  60 |             string ip = "unknown";
  61 |             try
  62 |             {
  63 |                 if (ctx != null && ctx.Request != null)
  64 |                 {
  65 |                     ip = ctx.Request.UserHostAddress ?? "unknown";
  66 |                     // basic proxy header (first hop)
  67 |                     string xff = ctx.Request.Headers["X-Forwarded-For"];
  68 |                     if (!string.IsNullOrEmpty(xff))
  69 |                     {
  70 |                         int comma = xff.IndexOf(',');
  71 |                         ip = (comma > 0 ? xff.Substring(0, comma) : xff).Trim();
  72 |                     }
  73 |                 }
  74 |             }
  75 |             catch { }
  76 |             return e + "|" + ip;
  77 |         }
```

---

### `IsLocked` — lines 78–101

#### Signature

```csharp
public static bool IsLocked(string email, HttpContext ctx, out string message)
```

#### What it is

Returns true if this email/IP is temporarily blocked after too many failed logins.

#### How it works

1. Return `true` to the caller.
2. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `message` | `string` | Status text for the UI. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `key` | `string` | HMAC key bytes or dictionary key. |
| `remain` | `var` | Holds “remain” for this scope. |
| `mins` | `int` | Often a collection related to mins (plural name). (integer) |

#### Code

```csharp
  78 | 
  79 |         public static bool IsLocked(string email, HttpContext ctx, out string message)
  80 |         {
  81 |             message = null;
  82 |             string key = ClientKey(email, ctx);
  83 |             Bucket b;
  84 |             if (!Map.TryGetValue(key, out b) || b == null) return false;
  85 | 
  86 |             if (b.LockedUntilUtc.HasValue)
  87 |             {
  88 |                 if (b.LockedUntilUtc.Value > DateTime.UtcNow)
  89 |                 {
  90 |                     var remain = b.LockedUntilUtc.Value - DateTime.UtcNow;
  91 |                     int mins = Math.Max(1, (int)Math.Ceiling(remain.TotalMinutes));
  92 |                     message = "Too many failed sign-in attempts. Try again in about " + mins + " minute(s).";
  93 |                     return true;
  94 |                 }
  95 |                 // lock expired
  96 |                 b.LockedUntilUtc = null;
  97 |                 b.Failures = 0;
  98 |                 b.WindowStartUtc = DateTime.UtcNow;
  99 |             }
 100 |             return false;
 101 |         }
```

---

### `RegisterFailure` — lines 102–125

#### Signature

```csharp
public static void RegisterFailure(string email, HttpContext ctx)
```

#### What it is

Records a failed login attempt (may trigger lockout).

#### How it works

1. Starts when something calls `RegisterFailure`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `key` | `string` | HMAC key bytes or dictionary key. |
| `now` | `var` | Current time (usually UTC or server local). |

#### Code

```csharp
 102 | 
 103 |         public static void RegisterFailure(string email, HttpContext ctx)
 104 |         {
 105 |             string key = ClientKey(email, ctx);
 106 |             var now = DateTime.UtcNow;
 107 |             Map.AddOrUpdate(key,
 108 |                 _ => new Bucket { Failures = 1, WindowStartUtc = now },
 109 |                 (_, b) =>
 110 |                 {
 111 |                     if (b.WindowStartUtc.AddMinutes(WindowMinutes) < now)
 112 |                     {
 113 |                         b.Failures = 1;
 114 |                         b.WindowStartUtc = now;
 115 |                         b.LockedUntilUtc = null;
 116 |                     }
 117 |                     else
 118 |                     {
 119 |                         b.Failures++;
 120 |                         if (b.Failures >= MaxFailures)
 121 |                             b.LockedUntilUtc = now.AddMinutes(LockoutMinutes);
 122 |                     }
 123 |                     return b;
 124 |                 });
 125 |         }
```

---

### `RegisterSuccess` — lines 126–132

#### Signature

```csharp
public static void RegisterSuccess(string email, HttpContext ctx)
```

#### What it is

Clears the failure counter after a good login.

#### How it works

1. Starts when something calls `RegisterSuccess`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `key` | `string` | HMAC key bytes or dictionary key. |

#### Code

```csharp
 126 | 
 127 |         public static void RegisterSuccess(string email, HttpContext ctx)
 128 |         {
 129 |             string key = ClientKey(email, ctx);
 130 |             Bucket removed;
 131 |             Map.TryRemove(key, out removed);
 132 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Collections.Concurrent;
   3 | using System.Configuration;
   4 | using System.Web;
   5 | 
   6 | namespace WebAppAssignment.Data.Security
   7 | {
   8 |     /// <summary>
   9 |     /// In-memory login rate limit / lockout (per email + IP).
  10 |     /// Suitable for single-server / LocalDB assignment deploy.
  11 |     /// </summary>
  12 |     public static class LoginThrottle
  13 |     {
  14 |         private class Bucket
  15 |         {
  16 |             public int Failures;
  17 |             public DateTime WindowStartUtc;
  18 |             public DateTime? LockedUntilUtc;
  19 |         }
  20 | 
  21 |         private static readonly ConcurrentDictionary<string, Bucket> Map =
  22 |             new ConcurrentDictionary<string, Bucket>(StringComparer.OrdinalIgnoreCase);
  23 | 
  24 |         private static int MaxFailures
  25 |         {
  26 |             get
  27 |             {
  28 |                 int n;
  29 |                 if (int.TryParse(ConfigurationManager.AppSettings["LoginMaxFailures"], out n) && n > 0)
  30 |                     return n;
  31 |                 return 5;
  32 |             }
  33 |         }
  34 | 
  35 |         private static int LockoutMinutes
  36 |         {
  37 |             get
  38 |             {
  39 |                 int n;
  40 |                 if (int.TryParse(ConfigurationManager.AppSettings["LoginLockoutMinutes"], out n) && n > 0)
  41 |                     return n;
  42 |                 return 15;
  43 |             }
  44 |         }
  45 | 
  46 |         private static int WindowMinutes
  47 |         {
  48 |             get
  49 |             {
  50 |                 int n;
  51 |                 if (int.TryParse(ConfigurationManager.AppSettings["LoginWindowMinutes"], out n) && n > 0)
  52 |                     return n;
  53 |                 return 15;
  54 |             }
  55 |         }
  56 | 
  57 |         public static string ClientKey(string email, HttpContext ctx)
  58 |         {
  59 |             string e = (email ?? "").Trim().ToLowerInvariant();
  60 |             string ip = "unknown";
  61 |             try
  62 |             {
  63 |                 if (ctx != null && ctx.Request != null)
  64 |                 {
  65 |                     ip = ctx.Request.UserHostAddress ?? "unknown";
  66 |                     // basic proxy header (first hop)
  67 |                     string xff = ctx.Request.Headers["X-Forwarded-For"];
  68 |                     if (!string.IsNullOrEmpty(xff))
  69 |                     {
  70 |                         int comma = xff.IndexOf(',');
  71 |                         ip = (comma > 0 ? xff.Substring(0, comma) : xff).Trim();
  72 |                     }
  73 |                 }
  74 |             }
  75 |             catch { }
  76 |             return e + "|" + ip;
  77 |         }
  78 | 
  79 |         public static bool IsLocked(string email, HttpContext ctx, out string message)
  80 |         {
  81 |             message = null;
  82 |             string key = ClientKey(email, ctx);
  83 |             Bucket b;
  84 |             if (!Map.TryGetValue(key, out b) || b == null) return false;
  85 | 
  86 |             if (b.LockedUntilUtc.HasValue)
  87 |             {
  88 |                 if (b.LockedUntilUtc.Value > DateTime.UtcNow)
  89 |                 {
  90 |                     var remain = b.LockedUntilUtc.Value - DateTime.UtcNow;
  91 |                     int mins = Math.Max(1, (int)Math.Ceiling(remain.TotalMinutes));
  92 |                     message = "Too many failed sign-in attempts. Try again in about " + mins + " minute(s).";
  93 |                     return true;
  94 |                 }
  95 |                 // lock expired
  96 |                 b.LockedUntilUtc = null;
  97 |                 b.Failures = 0;
  98 |                 b.WindowStartUtc = DateTime.UtcNow;
  99 |             }
 100 |             return false;
 101 |         }
 102 | 
 103 |         public static void RegisterFailure(string email, HttpContext ctx)
 104 |         {
 105 |             string key = ClientKey(email, ctx);
 106 |             var now = DateTime.UtcNow;
 107 |             Map.AddOrUpdate(key,
 108 |                 _ => new Bucket { Failures = 1, WindowStartUtc = now },
 109 |                 (_, b) =>
 110 |                 {
 111 |                     if (b.WindowStartUtc.AddMinutes(WindowMinutes) < now)
 112 |                     {
 113 |                         b.Failures = 1;
 114 |                         b.WindowStartUtc = now;
 115 |                         b.LockedUntilUtc = null;
 116 |                     }
 117 |                     else
 118 |                     {
 119 |                         b.Failures++;
 120 |                         if (b.Failures >= MaxFailures)
 121 |                             b.LockedUntilUtc = now.AddMinutes(LockoutMinutes);
 122 |                     }
 123 |                     return b;
 124 |                 });
 125 |         }
 126 | 
 127 |         public static void RegisterSuccess(string email, HttpContext ctx)
 128 |         {
 129 |             string key = ClientKey(email, ctx);
 130 |             Bucket removed;
 131 |             Map.TryRemove(key, out removed);
 132 |         }
 133 |     }
 134 | }
```
