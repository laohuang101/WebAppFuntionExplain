# LoginThrottle.cs
**Source:** `Data/Security/LoginThrottle.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

In-memory brute-force protection per email+IP (failures, lockout window).

## File overview

- **Total lines:** 134
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 16:** `Failures` — type `int`
- **Line 17:** `WindowStartUtc` — type `DateTime`
- **Line 18:** `LockedUntilUtc` — type `DateTime?`
- **Line 28:** `n` — type `int`
- **Line 30:** `n` — type `return`
- **Line 31:** `5` — type `return`
- **Line 39:** `n` — type `int`
- **Line 41:** `n` — type `return`
- **Line 42:** `15` — type `return`
- **Line 50:** `n` — type `int`
- **Line 52:** `n` — type `return`
- **Line 53:** `15` — type `return`
- **Line 59:** `e` — type `string`
- **Line 60:** `ip` — type `string`
- **Line 67:** `xff` — type `string`
- **Line 70:** `comma` — type `int`
- **Line 82:** `key` — type `string`
- **Line 83:** `b` — type `Bucket`
- **Line 90:** `remain` — type `var`
- **Line 91:** `mins` — type `int`
- **Line 93:** `true` — type `return`
- **Line 100:** `false` — type `return`
- **Line 105:** `key` — type `string`
- **Line 106:** `now` — type `var`
- **Line 123:** `b` — type `return`
- **Line 129:** `key` — type `string`
- **Line 130:** `removed` — type `Bucket`

## Functions / methods (4 found)

### `ClientKey` — lines 56–77

```
public static string ClientKey(string email, HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `ClientKey`.
- **Parameters:** `string email, HttpContext ctx`
- **Local variables:** `e`, `ip`, `xff`, `comma`

#### Line-by-line (this function)

`  56`  ``
`  57`  `        public static string ClientKey(string email, HttpContext ctx)`
`  58`  `        {`
`  59`  `            string e = (email ?? "").Trim().ToLowerInvariant();`
`  60`  `            string ip = "unknown";`
`  61`  `            try`
  - → Error handling block.
`  62`  `            {`
`  63`  `                if (ctx != null && ctx.Request != null)`
`  64`  `                {`
`  65`  `                    ip = ctx.Request.UserHostAddress ?? "unknown";`
`  66`  `                    // basic proxy header (first hop)`
`  67`  `                    string xff = ctx.Request.Headers["X-Forwarded-For"];`
`  68`  `                    if (!string.IsNullOrEmpty(xff))`
`  69`  `                    {`
`  70`  `                        int comma = xff.IndexOf(',');`
`  71`  `                        ip = (comma > 0 ? xff.Substring(0, comma) : xff).Trim();`
`  72`  `                    }`
`  73`  `                }`
`  74`  `            }`
`  75`  `            catch { }`
  - → Handle/log exception.
`  76`  `            return e + "|" + ip;`
`  77`  `        }`

---

### `IsLocked` — lines 78–101

```
public static bool IsLocked(string email, HttpContext ctx, out string message)
```

#### Explanation

- **Purpose:** Implements `IsLocked`.
- **Parameters:** `string email, HttpContext ctx, out string message`
- **Local variables:** `key`, `remain`, `mins`

#### Line-by-line (this function)

`  78`  ``
`  79`  `        public static bool IsLocked(string email, HttpContext ctx, out string message)`
  - → Brute-force lockout tracking.
`  80`  `        {`
`  81`  `            message = null;`
`  82`  `            string key = ClientKey(email, ctx);`
`  83`  `            Bucket b;`
`  84`  `            if (!Map.TryGetValue(key, out b) || b == null) return false;`
`  85`  ``
`  86`  `            if (b.LockedUntilUtc.HasValue)`
`  87`  `            {`
`  88`  `                if (b.LockedUntilUtc.Value > DateTime.UtcNow)`
`  89`  `                {`
`  90`  `                    var remain = b.LockedUntilUtc.Value - DateTime.UtcNow;`
`  91`  `                    int mins = Math.Max(1, (int)Math.Ceiling(remain.TotalMinutes));`
`  92`  `                    message = "Too many failed sign-in attempts. Try again in about " + mins + " minute(s).";`
`  93`  `                    return true;`
`  94`  `                }`
`  95`  `                // lock expired`
`  96`  `                b.LockedUntilUtc = null;`
`  97`  `                b.Failures = 0;`
`  98`  `                b.WindowStartUtc = DateTime.UtcNow;`
`  99`  `            }`
` 100`  `            return false;`
` 101`  `        }`

---

### `RegisterFailure` — lines 102–125

```
public static void RegisterFailure(string email, HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `RegisterFailure`.
- **Parameters:** `string email, HttpContext ctx`
- **Local variables:** `key`, `now`

#### Line-by-line (this function)

` 102`  ``
` 103`  `        public static void RegisterFailure(string email, HttpContext ctx)`
  - → Brute-force lockout tracking.
` 104`  `        {`
` 105`  `            string key = ClientKey(email, ctx);`
` 106`  `            var now = DateTime.UtcNow;`
` 107`  `            Map.AddOrUpdate(key,`
` 108`  `                _ => new Bucket { Failures = 1, WindowStartUtc = now },`
` 109`  `                (_, b) =>`
` 110`  `                {`
` 111`  `                    if (b.WindowStartUtc.AddMinutes(WindowMinutes) < now)`
` 112`  `                    {`
` 113`  `                        b.Failures = 1;`
` 114`  `                        b.WindowStartUtc = now;`
` 115`  `                        b.LockedUntilUtc = null;`
` 116`  `                    }`
` 117`  `                    else`
` 118`  `                    {`
` 119`  `                        b.Failures++;`
` 120`  `                        if (b.Failures >= MaxFailures)`
` 121`  `                            b.LockedUntilUtc = now.AddMinutes(LockoutMinutes);`
` 122`  `                    }`
` 123`  `                    return b;`
` 124`  `                });`
` 125`  `        }`

---

### `RegisterSuccess` — lines 126–132

```
public static void RegisterSuccess(string email, HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `RegisterSuccess`.
- **Parameters:** `string email, HttpContext ctx`
- **Local variables:** `key`

#### Line-by-line (this function)

` 126`  ``
` 127`  `        public static void RegisterSuccess(string email, HttpContext ctx)`
` 128`  `        {`
` 129`  `            string key = ClientKey(email, ctx);`
` 130`  `            Bucket removed;`
` 131`  `            Map.TryRemove(key, out removed);`
` 132`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Collections.Concurrent;`
  - → Import namespace/types.
`   3`  `using System.Configuration;`
  - → Import namespace/types.
`   4`  `using System.Web;`
  - → Import namespace/types.
`   5`  ``
`   6`  `namespace WebAppAssignment.Data.Security`
  - → C# namespace grouping.
`   7`  `{`
`   8`  `    /// <summary>`
`   9`  `    /// In-memory login rate limit / lockout (per email + IP).`
`  10`  `    /// Suitable for single-server / LocalDB assignment deploy.`
`  11`  `    /// </summary>`
`  12`  `    public static class LoginThrottle`
  - → Brute-force lockout tracking.
`  13`  `    {`
`  14`  `        private class Bucket`
  - → Class declaration for this page/service.
`  15`  `        {`
`  16`  `            public int Failures;`
`  17`  `            public DateTime WindowStartUtc;`
`  18`  `            public DateTime? LockedUntilUtc;`
`  19`  `        }`
`  20`  ``
`  21`  `        private static readonly ConcurrentDictionary<string, Bucket> Map =`
`  22`  `            new ConcurrentDictionary<string, Bucket>(StringComparer.OrdinalIgnoreCase);`
`  23`  ``
`  24`  `        private static int MaxFailures`
`  25`  `        {`
`  26`  `            get`
`  27`  `            {`
`  28`  `                int n;`
`  29`  `                if (int.TryParse(ConfigurationManager.AppSettings["LoginMaxFailures"], out n) && n > 0)`
`  30`  `                    return n;`
`  31`  `                return 5;`
`  32`  `            }`
`  33`  `        }`
`  34`  ``
`  35`  `        private static int LockoutMinutes`
`  36`  `        {`
`  37`  `            get`
`  38`  `            {`
`  39`  `                int n;`
`  40`  `                if (int.TryParse(ConfigurationManager.AppSettings["LoginLockoutMinutes"], out n) && n > 0)`
`  41`  `                    return n;`
`  42`  `                return 15;`
`  43`  `            }`
`  44`  `        }`
`  45`  ``
`  46`  `        private static int WindowMinutes`
`  47`  `        {`
`  48`  `            get`
`  49`  `            {`
`  50`  `                int n;`
`  51`  `                if (int.TryParse(ConfigurationManager.AppSettings["LoginWindowMinutes"], out n) && n > 0)`
`  52`  `                    return n;`
`  53`  `                return 15;`
`  54`  `            }`
`  55`  `        }`
`  56`  ``
`  57`  `        public static string ClientKey(string email, HttpContext ctx)`
`  58`  `        {`
`  59`  `            string e = (email ?? "").Trim().ToLowerInvariant();`
`  60`  `            string ip = "unknown";`
`  61`  `            try`
  - → Error handling block.
`  62`  `            {`
`  63`  `                if (ctx != null && ctx.Request != null)`
`  64`  `                {`
`  65`  `                    ip = ctx.Request.UserHostAddress ?? "unknown";`
`  66`  `                    // basic proxy header (first hop)`
`  67`  `                    string xff = ctx.Request.Headers["X-Forwarded-For"];`
`  68`  `                    if (!string.IsNullOrEmpty(xff))`
`  69`  `                    {`
`  70`  `                        int comma = xff.IndexOf(',');`
`  71`  `                        ip = (comma > 0 ? xff.Substring(0, comma) : xff).Trim();`
`  72`  `                    }`
`  73`  `                }`
`  74`  `            }`
`  75`  `            catch { }`
  - → Handle/log exception.
`  76`  `            return e + "|" + ip;`
`  77`  `        }`
`  78`  ``
`  79`  `        public static bool IsLocked(string email, HttpContext ctx, out string message)`
  - → Brute-force lockout tracking.
`  80`  `        {`
`  81`  `            message = null;`
`  82`  `            string key = ClientKey(email, ctx);`
`  83`  `            Bucket b;`
`  84`  `            if (!Map.TryGetValue(key, out b) || b == null) return false;`
`  85`  ``
`  86`  `            if (b.LockedUntilUtc.HasValue)`
`  87`  `            {`
`  88`  `                if (b.LockedUntilUtc.Value > DateTime.UtcNow)`
`  89`  `                {`
`  90`  `                    var remain = b.LockedUntilUtc.Value - DateTime.UtcNow;`
`  91`  `                    int mins = Math.Max(1, (int)Math.Ceiling(remain.TotalMinutes));`
`  92`  `                    message = "Too many failed sign-in attempts. Try again in about " + mins + " minute(s).";`
`  93`  `                    return true;`
`  94`  `                }`
`  95`  `                // lock expired`
`  96`  `                b.LockedUntilUtc = null;`
`  97`  `                b.Failures = 0;`
`  98`  `                b.WindowStartUtc = DateTime.UtcNow;`
`  99`  `            }`
` 100`  `            return false;`
` 101`  `        }`
` 102`  ``
` 103`  `        public static void RegisterFailure(string email, HttpContext ctx)`
  - → Brute-force lockout tracking.
` 104`  `        {`
` 105`  `            string key = ClientKey(email, ctx);`
` 106`  `            var now = DateTime.UtcNow;`
` 107`  `            Map.AddOrUpdate(key,`
` 108`  `                _ => new Bucket { Failures = 1, WindowStartUtc = now },`
` 109`  `                (_, b) =>`
` 110`  `                {`
` 111`  `                    if (b.WindowStartUtc.AddMinutes(WindowMinutes) < now)`
` 112`  `                    {`
` 113`  `                        b.Failures = 1;`
` 114`  `                        b.WindowStartUtc = now;`
` 115`  `                        b.LockedUntilUtc = null;`
` 116`  `                    }`
` 117`  `                    else`
` 118`  `                    {`
` 119`  `                        b.Failures++;`
` 120`  `                        if (b.Failures >= MaxFailures)`
` 121`  `                            b.LockedUntilUtc = now.AddMinutes(LockoutMinutes);`
` 122`  `                    }`
` 123`  `                    return b;`
` 124`  `                });`
` 125`  `        }`
` 126`  ``
` 127`  `        public static void RegisterSuccess(string email, HttpContext ctx)`
` 128`  `        {`
` 129`  `            string key = ClientKey(email, ctx);`
` 130`  `            Bucket removed;`
` 131`  `            Map.TryRemove(key, out removed);`
` 132`  `        }`
` 133`  `    }`
` 134`  `}`

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
