# PasswordHasher.cs
**Source:** `Data/Security/PasswordHasher.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

PBKDF2 password hashing and verification; upgrades legacy plain-text on successful login.

## File overview

- **Total lines:** 81
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (5 found)

### `Hash` — lines 17–31

#### Signature

```csharp
public static string Hash(string password)
```

#### What it is

Turns a plain password into a stored PBKDF2 hash.

#### How it works

1. Starts when something calls `Hash`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `password` | `string` | Plain password from the form (never log this). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `salt` | `var` | Random salt for PBKDF2.  Newly constructed object. |
| `rng` | `var` | Holds “rng” for this scope. |
| `hash` | `var` | Password hash (PBKDF2) stored in DB. |

#### Code

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

---

### `Verify` — lines 32–58

#### Signature

```csharp
public static bool Verify(string password, string stored)
```

#### What it is

Checks whether a typed password matches the stored hash.

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `password` | `string` | Plain password from the form (never log this). |
| `stored` | `string` | Holds “stored” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `parts` | `var` | Split path or name segments. |
| `actual` | `var` | Holds “actual” for this scope. |

#### Code

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

---

### `IsHashed` — lines 59–63

#### Signature

```csharp
public static bool IsHashed(string stored)
```

#### What it is

Checks a condition related to **Is Hashed** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `IsHashed`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `stored` | `string` | Holds “stored” for this scope. (text) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  59 | 
  60 |         public static bool IsHashed(string stored)
  61 |         {
  62 |             return !string.IsNullOrEmpty(stored) && stored.StartsWith(Prefix + ".", StringComparison.Ordinal);
  63 |         }
```

---

### `Pbkdf2` — lines 64–70

#### Signature

```csharp
private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)
```

#### What it is

Function `Pbkdf2` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Pbkdf2`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `password` | `string` | Plain password from the form (never log this). |
| `salt` | `byte[]` | Random salt for PBKDF2. |
| `iterations` | `int` | Often a collection related to iterations (plural name). (integer) |
| `length` | `int` | Holds “length” for this scope. (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `pbkdf2` | `var` | Holds “pbkdf2” for this scope.  Newly constructed object. |

#### Code

```csharp
  64 | 
  65 |         private static byte[] Pbkdf2(string password, byte[] salt, int iterations, int length)
  66 |         {
  67 |             // 3-arg ctor uses HMAC-SHA1 (widely available on .NET Framework 4.7.2)
  68 |             using (var pbkdf2 = new Rfc2898DeriveBytes(password, salt, iterations))
  69 |             return pbkdf2.GetBytes(length);
  70 |         }
```

---

### `FixedTimeEquals` — lines 71–79

#### Signature

```csharp
private static bool FixedTimeEquals(byte[] a, byte[] b)
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
| `a` | `byte[]` | Holds “a” for this scope. (type `byte[]`) |
| `b` | `byte[]` | Holds “b” for this scope. (type `byte[]`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `diff` | `int` | Holds “diff” for this scope. (integer)  Literal number `0`. |
| `i` | `int` | Loop index (0-based counter in for-loops).  Literal number `0`. |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
