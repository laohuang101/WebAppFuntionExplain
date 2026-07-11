# PasswordHasher.cs
**Source:** `Data/Security/PasswordHasher.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

PBKDF2 password hashing and verification; upgrades legacy plain-text on successful login.

## File overview

- **Total lines:** 81
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 21:** `salt` — type `var`
- **Line 24:** `hash` — type `var`
- **Line 40:** `parts` — type `var`
- **Line 42:** `iterations` — type `int`
- **Line 51:** `actual` — type `var`
- **Line 75:** `diff` — type `int`
- **Line 78:** `diff` — type `return`

## Functions / methods (5 found)

### `Hash` — lines 17–31

```
public static string Hash(string password)
```

#### Explanation

- **Purpose:** Implements `Hash`.
- **Parameters:** `string password`
- **Local variables:** `salt`, `rng`, `hash`

#### Line-by-line (this function)

`  17`  ``
`  18`  `        public static string Hash(string password)`
`  19`  `        {`
`  20`  `            if (password == null) password = "";`
`  21`  `            var salt = new byte[SaltSize];`
`  22`  `            using (var rng = RandomNumberGenerator.Create())`
  - → Import namespace/types.
`  23`  `            rng.GetBytes(salt);`
`  24`  ``
`  25`  `            var hash = Pbkdf2(password, salt, DefaultIterations, KeySize);`
`  26`  `            return string.Format("{0}.{1}.{2}.{3}",`
`  27`  `            Prefix,`
`  28`  `            DefaultIterations,`
`  29`  `            Convert.ToBase64String(salt),`
`  30`  `            Convert.ToBase64String(hash));`
`  31`  `        }`

---

### `Verify` — lines 32–58

```
public static bool Verify(string password, string stored)
```

#### Explanation

- **Purpose:** Implements `Verify`.
- **Parameters:** `string password, string stored`
- **Local variables:** `parts`, `actual`

#### Line-by-line (this function)

`  32`  ``
`  33`  `        public static bool Verify(string password, string stored)`
`  34`  `        {`
`  35`  `            if (string.IsNullOrEmpty(stored)) return false;`
`  36`  ``
`  37`  `            // Already hashed format`
`  38`  `            if (stored.StartsWith(Prefix + ".", StringComparison.Ordinal))`
`  39`  `            {`
`  40`  `                var parts = stored.Split('.');`
`  41`  `                if (parts.Length != 4) return false;`
`  42`  `                int iterations;`
`  43`  `                if (!int.TryParse(parts[1], out iterations)) return false;`
`  44`  `                byte[] salt, expected;`
`  45`  `                try`
  - → Error handling block.
`  46`  `                {`
`  47`  `                    salt = Convert.FromBase64String(parts[2]);`
`  48`  `                    expected = Convert.FromBase64String(parts[3]);`
`  49`  `                }`
`  50`  `                catch { return false; }`
  - → Handle/log exception.
`  51`  ``
`  52`  `                var actual = Pbkdf2(password ?? "", salt, iterations, expected.Length);`
`  53`  `                return FixedTimeEquals(actual, expected);`
  - → Constant-time string compare (reduce timing leaks).
`  54`  `            }`
`  55`  ``
`  56`  `            // Legacy plain-text (upgrade path)`
`  57`  `            return string.Equals(password ?? "", stored, StringComparison.Ordinal);`
`  58`  `        }`

---

### `IsHashed` — lines 59–63

```
public static bool IsHashed(string stored)
```

#### Explanation

- **Purpose:** Implements `IsHashed`.
- **Parameters:** `string stored`

#### Line-by-line (this function)

`  59`  ``
`  60`  `        public static bool IsHashed(string stored)`
`  61`  `        {`
`  62`  `            return !string.IsNullOrEmpty(stored) && stored.StartsWith(Prefix + ".", StringComparison.Ordinal);`
`  63`  `        }`

---

### `Pbkdf2` — lines 64–70

```
private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)
```

#### Explanation

- **Purpose:** Implements `Pbkdf2`.
- **Parameters:** `string password, byte[] salt, int iterations, int length`
- **Local variables:** `pbkdf2`

#### Line-by-line (this function)

`  64`  ``
`  65`  `        private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)`
`  66`  `        {`
`  67`  `            // 3-arg ctor uses HMAC-SHA1 (widely available on .NET Framework 4.7.2)`
`  68`  `            using (var pbkdf2 = new Rfc2898DeriveBytes(password, salt, iterations))`
  - → Import namespace/types.
`  69`  `            return pbkdf2.GetBytes(length);`
`  70`  `        }`

---

### `FixedTimeEquals` — lines 71–79

```
private static bool FixedTimeEquals(byte[] a, byte[] b)
```

#### Explanation

- **Purpose:** Implements `FixedTimeEquals`.
- **Parameters:** `byte[] a, byte[] b`
- **Local variables:** `diff`, `i`

#### Line-by-line (this function)

`  71`  ``
`  72`  `        private static bool FixedTimeEquals(byte[] a, byte[] b)`
  - → Constant-time string compare (reduce timing leaks).
`  73`  `        {`
`  74`  `            if (a == null || b == null || a.Length != b.Length) return false;`
`  75`  `            int diff = 0;`
`  76`  `            for (int i = 0; i < a.Length; i++)`
`  77`  `            diff |= a[i] ^ b[i];`
`  78`  `            return diff == 0;`
`  79`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Security.Cryptography;`
  - → Import namespace/types.
`   3`  `using System.Text;`
  - → Import namespace/types.
`   4`  ``
`   5`  `namespace WebAppAssignment.Data.Security`
  - → C# namespace grouping.
`   6`  `{`
`   7`  `    /// <summary>`
`   8`  `    /// PBKDF2-SHA256 password hashing (no external packages).`
`   9`  `    /// Stored format: v1.{iterations}.{saltB64}.{hashB64}`
`  10`  `    /// </summary>`
`  11`  `    public static class PasswordHasher`
  - → Password hashing (PBKDF2).
`  12`  `    {`
`  13`  `        private const int SaltSize = 16;`
`  14`  `        private const int KeySize = 32;`
`  15`  `        private const int DefaultIterations = 100_000;`
`  16`  `        private const string Prefix = "v1";`
`  17`  ``
`  18`  `        public static string Hash(string password)`
`  19`  `        {`
`  20`  `            if (password == null) password = "";`
`  21`  `            var salt = new byte[SaltSize];`
`  22`  `            using (var rng = RandomNumberGenerator.Create())`
  - → Import namespace/types.
`  23`  `            rng.GetBytes(salt);`
`  24`  ``
`  25`  `            var hash = Pbkdf2(password, salt, DefaultIterations, KeySize);`
`  26`  `            return string.Format("{0}.{1}.{2}.{3}",`
`  27`  `            Prefix,`
`  28`  `            DefaultIterations,`
`  29`  `            Convert.ToBase64String(salt),`
`  30`  `            Convert.ToBase64String(hash));`
`  31`  `        }`
`  32`  ``
`  33`  `        public static bool Verify(string password, string stored)`
`  34`  `        {`
`  35`  `            if (string.IsNullOrEmpty(stored)) return false;`
`  36`  ``
`  37`  `            // Already hashed format`
`  38`  `            if (stored.StartsWith(Prefix + ".", StringComparison.Ordinal))`
`  39`  `            {`
`  40`  `                var parts = stored.Split('.');`
`  41`  `                if (parts.Length != 4) return false;`
`  42`  `                int iterations;`
`  43`  `                if (!int.TryParse(parts[1], out iterations)) return false;`
`  44`  `                byte[] salt, expected;`
`  45`  `                try`
  - → Error handling block.
`  46`  `                {`
`  47`  `                    salt = Convert.FromBase64String(parts[2]);`
`  48`  `                    expected = Convert.FromBase64String(parts[3]);`
`  49`  `                }`
`  50`  `                catch { return false; }`
  - → Handle/log exception.
`  51`  ``
`  52`  `                var actual = Pbkdf2(password ?? "", salt, iterations, expected.Length);`
`  53`  `                return FixedTimeEquals(actual, expected);`
  - → Constant-time string compare (reduce timing leaks).
`  54`  `            }`
`  55`  ``
`  56`  `            // Legacy plain-text (upgrade path)`
`  57`  `            return string.Equals(password ?? "", stored, StringComparison.Ordinal);`
`  58`  `        }`
`  59`  ``
`  60`  `        public static bool IsHashed(string stored)`
`  61`  `        {`
`  62`  `            return !string.IsNullOrEmpty(stored) && stored.StartsWith(Prefix + ".", StringComparison.Ordinal);`
`  63`  `        }`
`  64`  ``
`  65`  `        private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)`
`  66`  `        {`
`  67`  `            // 3-arg ctor uses HMAC-SHA1 (widely available on .NET Framework 4.7.2)`
`  68`  `            using (var pbkdf2 = new Rfc2898DeriveBytes(password, salt, iterations))`
  - → Import namespace/types.
`  69`  `            return pbkdf2.GetBytes(length);`
`  70`  `        }`
`  71`  ``
`  72`  `        private static bool FixedTimeEquals(byte[] a, byte[] b)`
  - → Constant-time string compare (reduce timing leaks).
`  73`  `        {`
`  74`  `            if (a == null || b == null || a.Length != b.Length) return false;`
`  75`  `            int diff = 0;`
`  76`  `            for (int i = 0; i < a.Length; i++)`
`  77`  `            diff |= a[i] ^ b[i];`
`  78`  `            return diff == 0;`
`  79`  `        }`
`  80`  `    }`
`  81`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.Security.Cryptography;
using System.Text;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// PBKDF2-SHA256 password hashing (no external packages).
    /// Stored format: v1.{iterations}.{saltB64}.{hashB64}
    /// </summary>
    public static class PasswordHasher
    {
        private const int SaltSize = 16;
        private const int KeySize = 32;
        private const int DefaultIterations = 100_000;
        private const string Prefix = "v1";

        public static string Hash(string password)
        {
            if (password == null) password = "";
            var salt = new byte[SaltSize];
            using (var rng = RandomNumberGenerator.Create())
            rng.GetBytes(salt);

            var hash = Pbkdf2(password, salt, DefaultIterations, KeySize);
            return string.Format("{0}.{1}.{2}.{3}",
            Prefix,
            DefaultIterations,
            Convert.ToBase64String(salt),
            Convert.ToBase64String(hash));
        }

        public static bool Verify(string password, string stored)
        {
            if (string.IsNullOrEmpty(stored)) return false;

            // Already hashed format
            if (stored.StartsWith(Prefix + ".", StringComparison.Ordinal))
            {
                var parts = stored.Split('.');
                if (parts.Length != 4) return false;
                int iterations;
                if (!int.TryParse(parts[1], out iterations)) return false;
                byte[] salt, expected;
                try
                {
                    salt = Convert.FromBase64String(parts[2]);
                    expected = Convert.FromBase64String(parts[3]);
                }
                catch { return false; }

                var actual = Pbkdf2(password ?? "", salt, iterations, expected.Length);
                return FixedTimeEquals(actual, expected);
            }

            // Legacy plain-text (upgrade path)
            return string.Equals(password ?? "", stored, StringComparison.Ordinal);
        }

        public static bool IsHashed(string stored)
        {
            return !string.IsNullOrEmpty(stored) && stored.StartsWith(Prefix + ".", StringComparison.Ordinal);
        }

        private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)
        {
            // 3-arg ctor uses HMAC-SHA1 (widely available on .NET Framework 4.7.2)
            using (var pbkdf2 = new Rfc2898DeriveBytes(password, salt, iterations))
            return pbkdf2.GetBytes(length);
        }

        private static bool FixedTimeEquals(byte[] a, byte[] b)
        {
            if (a == null || b == null || a.Length != b.Length) return false;
            int diff = 0;
            for (int i = 0; i < a.Length; i++)
            diff |= a[i] ^ b[i];
            return diff == 0;
        }
    }
}

```
