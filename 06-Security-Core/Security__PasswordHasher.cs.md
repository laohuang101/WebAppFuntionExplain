# PasswordHasher.cs
**Source:** `Data/Security/PasswordHasher.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

PBKDF2 password hashing and verification; upgrades legacy plain-text on successful login.

## File overview

- **Total lines:** 81
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 21:** `salt` (`var`) — **Random salt for PBKDF2.**
- **Line 24:** `hash` (`var`) — **Password hash (PBKDF2) stored in DB.**
- **Line 40:** `parts` (`var`) — **Split path or name segments.**
- **Line 42:** `iterations` (`int`) — **Often a collection related to iterations (plural name). (integer)**
- **Line 51:** `actual` (`var`) — **Holds “actual” for this scope.**
- **Line 75:** `diff` (`int`) — **Holds “diff” for this scope. (integer)**
- **Line 78:** `diff` (`return`) — **Holds “diff” for this scope. (type `return`)**

## Functions / methods (5 found)

### `Hash` — lines 17–31

```csharp
public static string Hash(string password)
```

#### Explanation

- **Purpose:** Implements `Hash`.
- **Parameters (what each means):**
- `password` (`string`) — Plain password from the form (never log this).
- **Local variables (what each means):**
- `salt` (`var`) — Random salt for PBKDF2.  Newly constructed object.
- `rng` (`var`) — Holds “rng” for this scope.
- `hash` (`var`) — Password hash (PBKDF2) stored in DB.

#### Line-by-line (this function)

```csharp
  17 | 
  18 |         public static string Hash(string password)
  19 |         {
  20 |             if (password == null) password = "";
  21 |             var salt = new byte[SaltSize];
  22 |             using (var rng = RandomNumberGenerator.Create())
  23 |             rng.GetBytes(salt);
  24 | 
  25 |             var hash = Pbkdf2(password, salt, DefaultIterations, KeySize);
  26 |             return string.Format("{0}.{1}.{2}.{3}",
  27 |             Prefix,
  28 |             DefaultIterations,
  29 |             Convert.ToBase64String(salt),
  30 |             Convert.ToBase64String(hash));
  31 |         }
```

<<<<<<< HEAD
**Line notes**

- **L22:** Import namespace/types.
=======
**Line notes** (what code + variables mean)

- **L21:** `salt` means: Random salt for PBKDF2.  Newly constructed object.
- **L22:** Import namespace/types.
- **L25:** `hash` means: Password hash (PBKDF2) stored in DB.
>>>>>>> eb8ce01 (update)

---

### `Verify` — lines 32–58

```csharp
public static bool Verify(string password, string stored)
```

#### Explanation

- **Purpose:** Implements `Verify`.
- **Parameters (what each means):**
- `password` (`string`) — Plain password from the form (never log this).
- `stored` (`string`) — Holds “stored” for this scope. (text)
- **Local variables (what each means):**
- `parts` (`var`) — Split path or name segments.
- `actual` (`var`) — Holds “actual” for this scope.

#### Line-by-line (this function)

```csharp
  32 | 
  33 |         public static bool Verify(string password, string stored)
  34 |         {
  35 |             if (string.IsNullOrEmpty(stored)) return false;
  36 | 
  37 |             // Already hashed format
  38 |             if (stored.StartsWith(Prefix + ".", StringComparison.Ordinal))
  39 |             {
  40 |                 var parts = stored.Split('.');
  41 |                 if (parts.Length != 4) return false;
  42 |                 int iterations;
  43 |                 if (!int.TryParse(parts[1], out iterations)) return false;
  44 |                 byte[] salt, expected;
  45 |                 try
  46 |                 {
  47 |                     salt = Convert.FromBase64String(parts[2]);
  48 |                     expected = Convert.FromBase64String(parts[3]);
  49 |                 }
  50 |                 catch { return false; }
  51 | 
  52 |                 var actual = Pbkdf2(password ?? "", salt, iterations, expected.Length);
  53 |                 return FixedTimeEquals(actual, expected);
  54 |             }
  55 | 
  56 |             // Legacy plain-text (upgrade path)
  57 |             return string.Equals(password ?? "", stored, StringComparison.Ordinal);
  58 |         }
```

<<<<<<< HEAD
**Line notes**

- **L45:** Error handling block.
- **L50:** Handle/log exception.
=======
**Line notes** (what code + variables mean)

- **L40:** `parts` means: Split path or name segments.
- **L45:** Error handling block.
- **L50:** Handle/log exception.
- **L52:** `actual` means: Holds “actual” for this scope.
>>>>>>> eb8ce01 (update)
- **L53:** Constant-time string compare (reduce timing leaks).

---

### `IsHashed` — lines 59–63

```csharp
public static bool IsHashed(string stored)
```

#### Explanation

- **Purpose:** Implements `IsHashed`.
- **Parameters (what each means):**
- `stored` (`string`) — Holds “stored” for this scope. (text)

#### Line-by-line (this function)

```csharp
  59 | 
  60 |         public static bool IsHashed(string stored)
  61 |         {
  62 |             return !string.IsNullOrEmpty(stored) && stored.StartsWith(Prefix + ".", StringComparison.Ordinal);
  63 |         }
```

---

### `Pbkdf2` — lines 64–70

```csharp
private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)
```

#### Explanation

- **Purpose:** Implements `Pbkdf2`.
- **Parameters (what each means):**
- `password` (`string`) — Plain password from the form (never log this).
- `salt` (`byte[]`) — Random salt for PBKDF2.
- `iterations` (`int`) — Often a collection related to iterations (plural name). (integer)
- `length` (`int`) — Holds “length” for this scope. (integer)
- **Local variables (what each means):**
- `pbkdf2` (`var`) — Holds “pbkdf2” for this scope.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  64 | 
  65 |         private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)
  66 |         {
  67 |             // 3-arg ctor uses HMAC-SHA1 (widely available on .NET Framework 4.7.2)
  68 |             using (var pbkdf2 = new Rfc2898DeriveBytes(password, salt, iterations))
  69 |             return pbkdf2.GetBytes(length);
  70 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L68:** Import namespace/types.

---

### `FixedTimeEquals` — lines 71–79

```csharp
private static bool FixedTimeEquals(byte[] a, byte[] b)
```

#### Explanation

- **Purpose:** Implements `FixedTimeEquals`.
- **Parameters (what each means):**
- `a` (`byte[]`) — Holds “a” for this scope. (type `byte[]`)
- `b` (`byte[]`) — Holds “b” for this scope. (type `byte[]`)
- **Local variables (what each means):**
- `diff` (`int`) — Holds “diff” for this scope. (integer)  Literal number `0`.
- `i` (`int`) — Loop index (0-based counter in for-loops).  Literal number `0`.

#### Line-by-line (this function)

```csharp
  71 | 
  72 |         private static bool FixedTimeEquals(byte[] a, byte[] b)
  73 |         {
  74 |             if (a == null || b == null || a.Length != b.Length) return false;
  75 |             int diff = 0;
  76 |             for (int i = 0; i < a.Length; i++)
  77 |             diff |= a[i] ^ b[i];
  78 |             return diff == 0;
  79 |         }
```

<<<<<<< HEAD
**Line notes**

- **L72:** Constant-time string compare (reduce timing leaks).
=======
**Line notes** (what code + variables mean)

- **L72:** Constant-time string compare (reduce timing leaks).
- **L75:** `diff` means: Holds “diff” for this scope. (integer)  Literal number `0`.
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
   2 | using System.Security.Cryptography;
   3 | using System.Text;
   4 | 
   5 | namespace WebAppAssignment.Data.Security
   6 | {
   7 |     /// <summary>
   8 |     /// PBKDF2-SHA256 password hashing (no external packages).
   9 |     /// Stored format: v1.{iterations}.{saltB64}.{hashB64}
  10 |     /// </summary>
  11 |     public static class PasswordHasher
  12 |     {
  13 |         private const int SaltSize = 16;
  14 |         private const int KeySize = 32;
  15 |         private const int DefaultIterations = 100_000;
  16 |         private const string Prefix = "v1";
  17 | 
  18 |         public static string Hash(string password)
  19 |         {
  20 |             if (password == null) password = "";
  21 |             var salt = new byte[SaltSize];
  22 |             using (var rng = RandomNumberGenerator.Create())
  23 |             rng.GetBytes(salt);
  24 | 
  25 |             var hash = Pbkdf2(password, salt, DefaultIterations, KeySize);
  26 |             return string.Format("{0}.{1}.{2}.{3}",
  27 |             Prefix,
  28 |             DefaultIterations,
  29 |             Convert.ToBase64String(salt),
  30 |             Convert.ToBase64String(hash));
  31 |         }
  32 | 
  33 |         public static bool Verify(string password, string stored)
  34 |         {
  35 |             if (string.IsNullOrEmpty(stored)) return false;
  36 | 
  37 |             // Already hashed format
  38 |             if (stored.StartsWith(Prefix + ".", StringComparison.Ordinal))
  39 |             {
  40 |                 var parts = stored.Split('.');
  41 |                 if (parts.Length != 4) return false;
  42 |                 int iterations;
  43 |                 if (!int.TryParse(parts[1], out iterations)) return false;
  44 |                 byte[] salt, expected;
  45 |                 try
  46 |                 {
  47 |                     salt = Convert.FromBase64String(parts[2]);
  48 |                     expected = Convert.FromBase64String(parts[3]);
  49 |                 }
  50 |                 catch { return false; }
  51 | 
  52 |                 var actual = Pbkdf2(password ?? "", salt, iterations, expected.Length);
  53 |                 return FixedTimeEquals(actual, expected);
  54 |             }
  55 | 
  56 |             // Legacy plain-text (upgrade path)
  57 |             return string.Equals(password ?? "", stored, StringComparison.Ordinal);
  58 |         }
  59 | 
  60 |         public static bool IsHashed(string stored)
  61 |         {
  62 |             return !string.IsNullOrEmpty(stored) && stored.StartsWith(Prefix + ".", StringComparison.Ordinal);
  63 |         }
  64 | 
  65 |         private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)
  66 |         {
  67 |             // 3-arg ctor uses HMAC-SHA1 (widely available on .NET Framework 4.7.2)
  68 |             using (var pbkdf2 = new Rfc2898DeriveBytes(password, salt, iterations))
  69 |             return pbkdf2.GetBytes(length);
  70 |         }
  71 | 
  72 |         private static bool FixedTimeEquals(byte[] a, byte[] b)
  73 |         {
  74 |             if (a == null || b == null || a.Length != b.Length) return false;
  75 |             int diff = 0;
  76 |             for (int i = 0; i < a.Length; i++)
  77 |             diff |= a[i] ^ b[i];
  78 |             return diff == 0;
  79 |         }
  80 |     }
  81 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L11:** Password hashing (PBKDF2).
<<<<<<< HEAD
- **L22:** Import namespace/types.
- **L45:** Error handling block.
- **L50:** Handle/log exception.
- **L53:** Constant-time string compare (reduce timing leaks).
- **L68:** Import namespace/types.
- **L72:** Constant-time string compare (reduce timing leaks).
=======
- **L21:** `salt` means: Random salt for PBKDF2.  Newly constructed object.
- **L22:** Import namespace/types.
- **L25:** `hash` means: Password hash (PBKDF2) stored in DB.
- **L40:** `parts` means: Split path or name segments.
- **L45:** Error handling block.
- **L50:** Handle/log exception.
- **L52:** `actual` means: Holds “actual” for this scope.
- **L53:** Constant-time string compare (reduce timing leaks).
- **L68:** Import namespace/types.
- **L72:** Constant-time string compare (reduce timing leaks).
- **L75:** `diff` means: Holds “diff” for this scope. (integer)  Literal number `0`.
>>>>>>> eb8ce01 (update)

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
