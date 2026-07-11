# LoginThrottle.cs
**Source:** `Data/Security/LoginThrottle.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

In-memory brute-force protection per email+IP (failures, lockout window).

## File overview

- **Total lines:** 134
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 16:** `Failures` (`int`) — **Number of failed login attempts in the current window.**
- **Line 17:** `WindowStartUtc` (`DateTime`) — **Date/time value. (date/time)**
- **Line 18:** `LockedUntilUtc` (`DateTime?`) — **Date/time value. (date/time)**
- **Line 28:** `n` (`int`) — **Integer count (rows, items, or length).**
- **Line 30:** `n` (`return`) — **Numeric count or temporary integer.**
- **Line 31:** `5` (`return`) — **Holds “5” for this scope. (type `return`)**
- **Line 39:** `n` (`int`) — **Integer count (rows, items, or length).**
- **Line 41:** `n` (`return`) — **Numeric count or temporary integer.**
- **Line 42:** `15` (`return`) — **Holds “15” for this scope. (type `return`)**
- **Line 50:** `n` (`int`) — **Integer count (rows, items, or length).**
- **Line 52:** `n` (`return`) — **Numeric count or temporary integer.**
- **Line 53:** `15` (`return`) — **Holds “15” for this scope. (type `return`)**
- **Line 59:** `e` (`string`) — **Normalized email string (trimmed/lowercased).**
- **Line 60:** `ip` (`string`) — **Client IP address for throttle/audit.**
- **Line 67:** `xff` (`string`) — **X-Forwarded-For header value (client IP when behind a proxy).**
- **Line 70:** `comma` (`int`) — **Index of the first comma in a string (split helper).**
- **Line 82:** `key` (`string`) — **HMAC key bytes or dictionary key.**
- **Line 83:** `b` (`Bucket`) — **Holds “b” for this scope. (type `Bucket`)**
- **Line 90:** `remain` (`var`) — **Holds “remain” for this scope.**
- **Line 91:** `mins` (`int`) — **Often a collection related to mins (plural name). (integer)**
- **Line 93:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 100:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 105:** `key` (`string`) — **HMAC key bytes or dictionary key.**
- **Line 106:** `now` (`var`) — **Current time (usually UTC or server local).**
- **Line 123:** `b` (`return`) — **Holds “b” for this scope. (type `return`)**
- **Line 129:** `key` (`string`) — **HMAC key bytes or dictionary key.**
- **Line 130:** `removed` (`Bucket`) — **Holds “removed” for this scope. (type `Bucket`)**

## Functions / methods (4 found)

### `ClientKey` — lines 56–77

```csharp
public static string ClientKey(string email, HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `ClientKey`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- **Local variables (what each means):**
- `e` (`string`) — Normalized email string (trimmed/lowercased).
- `ip` (`string`) — Client IP address for throttle/audit.  Literal text string.
- `xff` (`string`) — X-Forwarded-For header value (client IP when behind a proxy).
- `comma` (`int`) — Index of the first comma in a string (split helper).

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L61:** Error handling block.
=======
**Line notes** (what code + variables mean)

- **L59:** `e` means: Normalized email string (trimmed/lowercased).
- **L60:** `ip` means: Client IP address for throttle/audit.  Literal text string.
- **L61:** Error handling block.
- **L67:** `xff` means: X-Forwarded-For header value (client IP when behind a proxy).
- **L70:** `comma` means: Index of the first comma in a string (split helper).
>>>>>>> eb8ce01 (update)
- **L75:** Handle/log exception.

---

### `IsLocked` — lines 78–101

```csharp
public static bool IsLocked(string email, HttpContext ctx, out string message)
```

#### Explanation

- **Purpose:** Implements `IsLocked`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- `message` (`string`) — Status text for the UI.
- **Local variables (what each means):**
- `key` (`string`) — HMAC key bytes or dictionary key.
- `remain` (`var`) — Holds “remain” for this scope.
- `mins` (`int`) — Often a collection related to mins (plural name). (integer)

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L79:** Brute-force lockout tracking.
=======
**Line notes** (what code + variables mean)

- **L79:** Brute-force lockout tracking.
- **L82:** `key` means: HMAC key bytes or dictionary key.
- **L90:** `remain` means: Holds “remain” for this scope.
- **L91:** `mins` means: Often a collection related to mins (plural name). (integer)
>>>>>>> eb8ce01 (update)

---

### `RegisterFailure` — lines 102–125

```csharp
public static void RegisterFailure(string email, HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `RegisterFailure`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- **Local variables (what each means):**
- `key` (`string`) — HMAC key bytes or dictionary key.
- `now` (`var`) — Current time (usually UTC or server local).

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L103:** Brute-force lockout tracking.
=======
**Line notes** (what code + variables mean)

- **L103:** Brute-force lockout tracking.
- **L105:** `key` means: HMAC key bytes or dictionary key.
- **L106:** `now` means: Current time (usually UTC or server local).
>>>>>>> eb8ce01 (update)

---

### `RegisterSuccess` — lines 126–132

```csharp
public static void RegisterSuccess(string email, HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `RegisterSuccess`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- **Local variables (what each means):**
- `key` (`string`) — HMAC key bytes or dictionary key.

#### Line-by-line (this function)

```csharp
 126 | 
 127 |         public static void RegisterSuccess(string email, HttpContext ctx)
 128 |         {
 129 |             string key = ClientKey(email, ctx);
 130 |             Bucket removed;
 131 |             Map.TryRemove(key, out removed);
 132 |         }
```
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L129:** `key` means: HMAC key bytes or dictionary key.
>>>>>>> eb8ce01 (update)

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L6:** C# namespace grouping.
- **L12:** Brute-force lockout tracking.
- **L14:** Class declaration for this page/service.
<<<<<<< HEAD
- **L61:** Error handling block.
- **L75:** Handle/log exception.
- **L79:** Brute-force lockout tracking.
- **L103:** Brute-force lockout tracking.
=======
- **L59:** `e` means: Normalized email string (trimmed/lowercased).
- **L60:** `ip` means: Client IP address for throttle/audit.  Literal text string.
- **L61:** Error handling block.
- **L67:** `xff` means: X-Forwarded-For header value (client IP when behind a proxy).
- **L70:** `comma` means: Index of the first comma in a string (split helper).
- **L75:** Handle/log exception.
- **L79:** Brute-force lockout tracking.
- **L82:** `key` means: HMAC key bytes or dictionary key.
- **L90:** `remain` means: Holds “remain” for this scope.
- **L91:** `mins` means: Often a collection related to mins (plural name). (integer)
- **L103:** Brute-force lockout tracking.
- **L105:** `key` means: HMAC key bytes or dictionary key.
- **L106:** `now` means: Current time (usually UTC or server local).
- **L129:** `key` means: HMAC key bytes or dictionary key.
>>>>>>> eb8ce01 (update)

## Source snapshot (raw)

```csharp
using System;
using System.Collections.Concurrent;
using System.Configuration;
using System.Web;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// In-memory login rate limit / lockout (per email + IP).
    /// Suitable for single-server / LocalDB assignment deploy.
    /// </summary>
    public static class LoginThrottle
    {
        private class Bucket
        {
            public int Failures;
            public DateTime WindowStartUtc;
            public DateTime? LockedUntilUtc;
        }

        private static readonly ConcurrentDictionary<string, Bucket> Map =
            new ConcurrentDictionary<string, Bucket>(StringComparer.OrdinalIgnoreCase);

        private static int MaxFailures
        {
            get
            {
                int n;
                if (int.TryParse(ConfigurationManager.AppSettings["LoginMaxFailures"], out n) && n > 0)
                    return n;
                return 5;
            }
        }

        private static int LockoutMinutes
        {
            get
            {
                int n;
                if (int.TryParse(ConfigurationManager.AppSettings["LoginLockoutMinutes"], out n) && n > 0)
                    return n;
                return 15;
            }
        }

        private static int WindowMinutes
        {
            get
            {
                int n;
                if (int.TryParse(ConfigurationManager.AppSettings["LoginWindowMinutes"], out n) && n > 0)
                    return n;
                return 15;
            }
        }

        public static string ClientKey(string email, HttpContext ctx)
        {
            string e = (email ?? "").Trim().ToLowerInvariant();
            string ip = "unknown";
            try
            {
                if (ctx != null && ctx.Request != null)
                {
                    ip = ctx.Request.UserHostAddress ?? "unknown";
                    // basic proxy header (first hop)
                    string xff = ctx.Request.Headers["X-Forwarded-For"];
                    if (!string.IsNullOrEmpty(xff))
                    {
                        int comma = xff.IndexOf(',');
                        ip = (comma > 0 ? xff.Substring(0, comma) : xff).Trim();
                    }
                }
            }
            catch { }
            return e + "|" + ip;
        }

        public static bool IsLocked(string email, HttpContext ctx, out string message)
        {
            message = null;
            string key = ClientKey(email, ctx);
            Bucket b;
            if (!Map.TryGetValue(key, out b) || b == null) return false;

            if (b.LockedUntilUtc.HasValue)
            {
                if (b.LockedUntilUtc.Value > DateTime.UtcNow)
                {
                    var remain = b.LockedUntilUtc.Value - DateTime.UtcNow;
                    int mins = Math.Max(1, (int)Math.Ceiling(remain.TotalMinutes));
                    message = "Too many failed sign-in attempts. Try again in about " + mins + " minute(s).";
                    return true;
                }
                // lock expired
                b.LockedUntilUtc = null;
                b.Failures = 0;
                b.WindowStartUtc = DateTime.UtcNow;
            }
            return false;
        }

        public static void RegisterFailure(string email, HttpContext ctx)
        {
            string key = ClientKey(email, ctx);
            var now = DateTime.UtcNow;
            Map.AddOrUpdate(key,
                _ => new Bucket { Failures = 1, WindowStartUtc = now },
                (_, b) =>
                {
                    if (b.WindowStartUtc.AddMinutes(WindowMinutes) < now)
                    {
                        b.Failures = 1;
                        b.WindowStartUtc = now;
                        b.LockedUntilUtc = null;
                    }
                    else
                    {
                        b.Failures++;
                        if (b.Failures >= MaxFailures)
                            b.LockedUntilUtc = now.AddMinutes(LockoutMinutes);
                    }
                    return b;
                });
        }

        public static void RegisterSuccess(string email, HttpContext ctx)
        {
            string key = ClientKey(email, ctx);
            Bucket removed;
            Map.TryRemove(key, out removed);
        }
    }
}

```
