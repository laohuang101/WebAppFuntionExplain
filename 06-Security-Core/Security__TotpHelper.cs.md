# TotpHelper.cs
**Source:** `Data/Security/TotpHelper.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

RFC 6238 TOTP (Google Authenticator): secret generate, verify ± window, otpauth URI, Base32.

## File overview

- **Total lines:** 259
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (14 found)

### `GenerateSecret` — lines 18–25

#### Signature

```csharp
public static string GenerateSecret(int bytes = 20)
```

#### What it is

Creates a new random Base32 secret for Google Authenticator.

#### How it works

1. Starts when something calls `GenerateSecret`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `bytes` | `int` | Byte array (hash, random, file content). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `bytes` | `int` | Byte array (hash, random, file content).  Newly constructed object. |
| `rng` | `var` | Holds “rng” for this scope. |

#### Code

```csharp
  18 | 
  19 |         public static string GenerateSecret(int bytes = 20)
  20 |         {
  21 |             var raw = new byte[bytes];
  22 |             using (var rng = RandomNumberGenerator.Create())
  23 |             rng.GetBytes(raw);
  24 |             return Base32Encode(raw);
  25 |         }
```

---

### `GenerateCode` — lines 26–34

#### Signature

```csharp
public static string GenerateCode(string base32Secret, DateTime? utcNow = null)
```

#### What it is

Computes the current 6-digit TOTP code for a secret (server-side).

#### How it works

1. Stop with an error (invalid access or bad input).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `base32Secret` | `string` | Secret key material (MFA Base32 or crypto secret). (text) |
| `utcNow` | `DateTime?` | Holds “utc Now” for this scope. (date/time) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `utcNow` | `DateTime?` | Holds “utc Now” for this scope. (date/time) |
| `timestep` | `long` | Date/time value. (integer) |

#### Code

```csharp
  26 | 
  27 |         public static string GenerateCode(string base32Secret, DateTime? utcNow = null)
  28 |         {
  29 |             byte[] key = Base32Decode(base32Secret);
  30 |             if (key == null || key.Length == 0)
  31 |             throw new ArgumentException("Invalid TOTP secret.");
  32 |             long timestep = GetTimeStep(utcNow ?? DateTime.UtcNow);
  33 |             return ComputeTotp(key, timestep);
  34 |         }
```

---

### `VerifyCode` — lines 39–58

#### Signature

```csharp
public static bool VerifyCode(string base32Secret, string code, int window = 4)
```

#### What it is

Checks if the 6-digit code from the authenticator app is correct (with clock skew window).

#### How it works

1. Return `false` to the caller.
2. Return `true` to the caller.
3. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `base32Secret` | `string` | Secret key material (MFA Base32 or crypto secret). (text) |
| `code` | `string` | 6-digit TOTP / OTP the user typed. |
| `window` | `int` | TOTP time-step window (± steps for clock skew). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `key` | `byte[]` | HMAC key bytes or dictionary key. |
| `step` | `long` | TOTP 30-second time step counter. |
| `w` | `int` | Holds “w” for this scope. (integer) |

#### Code

```csharp
  39 |         public static bool VerifyCode(string base32Secret, string code, int window = 4)
  40 |         {
  41 |             if (string.IsNullOrWhiteSpace(base32Secret) || string.IsNullOrWhiteSpace(code))
  42 |                 return false;
  43 | 
  44 |             code = NormalizeCode(code);
  45 |             if (code.Length != Digits) return false;
  46 | 
  47 |             byte[] key = Base32Decode(base32Secret);
  48 |             if (key == null || key.Length == 0) return false;
  49 | 
  50 |             // Always use UTC unix seconds (Kind-safe)
  51 |             long step = GetTimeStep(DateTime.UtcNow);
  52 |             for (int w = -window; w <= window; w++)
  53 |             {
  54 |                 if (FixedTimeEquals(ComputeTotp(key, step + w), code))
  55 |                     return true;
  56 |             }
  57 |             return false;
  58 |         }
```

---

### `NormalizeCode` — lines 61–78

#### Signature

```csharp
public static string NormalizeCode(string code)
```

#### What it is

Cleans a typed OTP (digits only).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `code` | `string` | 6-digit TOTP / OTP the user typed. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cleaned` | `var` | Holds “cleaned” for this scope.  Newly constructed object. |
| `nv` | `double` | Holds “nv” for this scope. (number/score) |
| `c` | `—` | Temporary value (character, course, or counter depending on loop). |

#### Code

```csharp
  61 |         public static string NormalizeCode(string code)
  62 |         {
  63 |             if (string.IsNullOrEmpty(code)) return "";
  64 |             var cleaned = new StringBuilder(code.Length);
  65 |             foreach (char c in code)
  66 |             {
  67 |                 if (c >= '0' && c <= '9')
  68 |                 {
  69 |                     cleaned.Append(c);
  70 |                     continue;
  71 |                 }
  72 |                 // Full-width digits ０-９ and other numeric chars
  73 |                 double nv = char.GetNumericValue(c);
  74 |                 if (nv >= 0 && nv <= 9 && nv == Math.Floor(nv))
  75 |                     cleaned.Append((char)('0' + (int)nv));
  76 |             }
  77 |             return cleaned.ToString();
  78 |         }
```

---

### `BuildOtpAuthUri` — lines 85–105

#### Signature

```csharp
public static string BuildOtpAuthUri(string email, string base32Secret, string issuer = "EduLMS")
```

#### What it is

Builds the `otpauth://` link used to draw the MFA QR code.

#### How it works

1. Stop with an error (invalid access or bad input).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `base32Secret` | `string` | Secret key material (MFA Base32 or crypto secret). (text) |
| `issuer` | `string` | TOTP issuer label (EduLMS). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `secret` | `string` | MFA TOTP Base32 secret for authenticator apps. |
| `label` | `string` | otpauth account label (issuer:email). |
| `qs` | `var` | Holds “qs” for this scope.  Newly constructed object. |

#### Code

```csharp
  85 |         public static string BuildOtpAuthUri(string email, string base32Secret, string issuer = "EduLMS")
  86 |         {
  87 |             if (string.IsNullOrWhiteSpace(base32Secret))
  88 |             throw new ArgumentException("secret required");
  89 | 
  90 |             issuer = string.IsNullOrWhiteSpace(issuer) ? "EduLMS" : issuer.Trim();
  91 |             email = (email ?? "user").Trim();
  92 |             string secret = NormalizeSecret(base32Secret);
  93 | 
  94 |             // Path label: Issuer:account - encode each part, keep colon literal
  95 |             string label = EncodePathSegment(issuer) + ":" + EncodePathSegment(email);
  96 | 
  97 |             var qs = new StringBuilder();
  98 |             qs.Append("secret=").Append(secret); // base32 A-Z2-7 only - safe unencoded
  99 |             qs.Append("&issuer=").Append(Uri.EscapeDataString(issuer));
 100 |             qs.Append("&algorithm=SHA1");
 101 |             qs.Append("&digits=").Append(Digits);
 102 |             qs.Append("&period=").Append(StepSeconds);
 103 | 
 104 |             return "otpauth://totp/" + label + "?" + qs;
 105 |         }
```

---

### `FormatSecretForDisplay` — lines 108–119

#### Signature

```csharp
public static string FormatSecretForDisplay(string base32Secret)
```

#### What it is

Converts or cleans **Format Secret For Display** into a usable form.

#### How it works

1. Starts when something calls `FormatSecretForDisplay`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `base32Secret` | `string` | Secret key material (MFA Base32 or crypto secret). (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `string` | String being cleaned or built. |
| `sb` | `var` | StringBuilder — efficient string concatenation.  Newly constructed object. |
| `i` | `int` | Loop index (0-based counter in for-loops).  Literal number `0`. |

#### Code

```csharp
 108 |         public static string FormatSecretForDisplay(string base32Secret)
 109 |         {
 110 |             string s = NormalizeSecret(base32Secret);
 111 |             if (s.Length == 0) return "";
 112 |             var sb = new StringBuilder();
 113 |             for (int i = 0; i < s.Length; i++)
 114 |             {
 115 |                 if (i > 0 && i % 4 == 0) sb.Append(' ');
 116 |                 sb.Append(s[i]);
 117 |             }
 118 |             return sb.ToString();
 119 |         }
```

---

### `NormalizeSecret` — lines 120–133

#### Signature

```csharp
public static string NormalizeSecret(string base32Secret)
```

#### What it is

Cleans an MFA secret (remove spaces, uppercase Base32).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `base32Secret` | `string` | Secret key material (MFA Base32 or crypto secret). (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sb` | `var` | StringBuilder — efficient string concatenation.  Newly constructed object. |
| `c` | `—` | Temporary value (character, course, or counter depending on loop). |

#### Code

```csharp
 120 | 
 121 |         public static string NormalizeSecret(string base32Secret)
 122 |         {
 123 |             if (string.IsNullOrWhiteSpace(base32Secret)) return "";
 124 |             var sb = new StringBuilder(base32Secret.Length);
 125 |             foreach (char c in base32Secret.Trim().ToUpperInvariant())
 126 |             {
 127 |                 if (c == ' ' || c == '-' || c == '=') continue;
 128 |                 // common OCR/typo: 0/1/8 → O/I/B not in alphabet; skip invalid
 129 |                 if (Alphabet.IndexOf(c) >= 0)
 130 |                 sb.Append(c);
 131 |             }
 132 |             return sb.ToString();
 133 |         }
```

---

### `GenerateEmailOtp` — lines 136–143

#### Signature

```csharp
public static string GenerateEmailOtp(int length = 6)
```

#### What it is

Creates/builds **Generate Email Otp** (object, string, secret, or UI content).

#### How it works

1. Starts when something calls `GenerateEmailOtp`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `length` | `int` | Holds “length” for this scope. (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `bytes` | `var` | Byte array (hash, random, file content).  Newly constructed object. |
| `rng` | `var` | Holds “rng” for this scope. |
| `n` | `int` | Integer count (rows, items, or length). |

#### Code

```csharp
 136 |         public static string GenerateEmailOtp(int length = 6)
 137 |         {
 138 |             var bytes = new byte[4];
 139 |             using (var rng = RandomNumberGenerator.Create())
 140 |             rng.GetBytes(bytes);
 141 |             int n = Math.Abs(BitConverter.ToInt32(bytes, 0)) % (int)Math.Pow(10, length);
 142 |             return n.ToString(CultureInfo.InvariantCulture).PadLeft(length, '0');
 143 |         }
```

---

### `EncodePathSegment` — lines 144–149

#### Signature

```csharp
private static string EncodePathSegment(string value)
```

#### What it is

Function `EncodePathSegment` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `EncodePathSegment`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `value` | `string` | Holds “value” for this scope. (text) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 144 | 
 145 |         private static string EncodePathSegment(string value)
 146 |         {
 147 |             // Encode for URI path but keep @ unescaped is optional; EscapeDataString is safe
 148 |             return Uri.EscapeDataString(value ?? "");
 149 |         }
```

---

### `GetTimeStep` — lines 150–161

#### Signature

```csharp
private static long GetTimeStep(DateTime when)
```

#### What it is

Reads/loads data related to **Time Step** and returns it for display or further use.

#### How it works

1. Starts when something calls `GetTimeStep`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `when` | `DateTime` | Holds “when” for this scope. (date/time) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `utc` | `DateTime` | Date/time value. (date/time) |
| `epoch` | `DateTime` | Holds “epoch” for this scope. (date/time)  Newly constructed object. |
| `unix` | `long` | Holds “unix” for this scope. (integer) |

#### Code

```csharp
 150 | 
 151 |         private static long GetTimeStep(DateTime when)
 152 |         {
 153 |             // Kind.Unspecified: treat as UTC (server clock). Local would skew TOTP.
 154 |             DateTime utc = when.Kind == DateTimeKind.Local
 155 |                 ? when.ToUniversalTime()
 156 |                 : DateTime.SpecifyKind(when, DateTimeKind.Utc);
 157 |             DateTime epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
 158 |             long unix = (long)(utc - epoch).TotalSeconds;
 159 |             if (unix < 0) unix = 0;
 160 |             return unix / StepSeconds;
 161 |         }
```

---

### `ComputeTotp` — lines 162–189

#### Signature

```csharp
private static string ComputeTotp(byte[] key, long timestep)
```

#### What it is

Function `ComputeTotp` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `ComputeTotp`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `key` | `byte[]` | HMAC key bytes or dictionary key. |
| `timestep` | `long` | Date/time value. (integer) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `counter` | `byte[]` | Holds “counter” for this scope. (type `byte[]`)  Newly constructed object. |
| `hmac` | `var` | Holds “hmac” for this scope.  Newly constructed object. |
| `offset` | `int` | Holds “offset” for this scope. (integer) |
| `binary` | `int` | Holds “binary” for this scope. (integer) |
| `otp` | `int` | Holds “otp” for this scope. (integer) |

#### Code

```csharp
 162 | 
 163 |         private static string ComputeTotp(byte[] key, long timestep)
 164 |         {
 165 |             // 8-byte big-endian counter (RFC 4226)
 166 |             byte[] counter = new byte[8];
 167 |             ulong ts = (ulong)timestep;
 168 |             counter[0] = (byte)(ts >> 56);
 169 |             counter[1] = (byte)(ts >> 48);
 170 |             counter[2] = (byte)(ts >> 40);
 171 |             counter[3] = (byte)(ts >> 32);
 172 |             counter[4] = (byte)(ts >> 24);
 173 |             counter[5] = (byte)(ts >> 16);
 174 |             counter[6] = (byte)(ts >> 8);
 175 |             counter[7] = (byte)ts;
 176 | 
 177 |             using (var hmac = new HMACSHA1(key))
 178 |             {
 179 |                 byte[] hash = hmac.ComputeHash(counter);
 180 |                 int offset = hash[hash.Length - 1] & 0x0F;
 181 |                 int binary =
 182 |                 ((hash[offset] & 0x7f) << 24) |
 183 |                 ((hash[offset + 1] & 0xff) << 16) |
 184 |                 ((hash[offset + 2] & 0xff) << 8) |
 185 |                 (hash[offset + 3] & 0xff);
 186 |                 int otp = binary % 1000000;
 187 |                 return otp.ToString(CultureInfo.InvariantCulture).PadLeft(Digits, '0');
 188 |             }
 189 |         }
```

---

### `FixedTimeEquals` — lines 190–198

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
 190 | 
 191 |         private static bool FixedTimeEquals(string a, string b)
 192 |         {
 193 |             if (a == null || b == null || a.Length != b.Length) return false;
 194 |             int diff = 0;
 195 |             for (int i = 0; i < a.Length; i++)
 196 |             diff |= a[i] ^ b[i];
 197 |             return diff == 0;
 198 |         }
```

---

### `Base32Encode` — lines 199–229

#### Signature

```csharp
private static string Base32Encode(byte[] data)
```

#### What it is

Function `Base32Encode` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Base32Encode`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `data` | `byte[]` | Holds “data” for this scope. (type `byte[]`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sb` | `var` | StringBuilder — efficient string concatenation.  Newly constructed object. |
| `buffer` | `int` | Holds “buffer” for this scope. (integer) |
| `next` | `int` | Holds “next” for this scope. (integer)  Literal number `1`. |
| `bitsLeft` | `int` | Holds “bits Left” for this scope. (integer)  Literal number `8`. |
| `pad` | `int` | Holds “pad” for this scope. (integer) |
| `index` | `int` | Holds “index” for this scope. (integer) |

#### Code

```csharp
 199 | 
 200 |         private static string Base32Encode(byte[] data)
 201 |         {
 202 |             if (data == null || data.Length == 0) return "";
 203 |             var sb = new StringBuilder((data.Length * 8 + 4) / 5);
 204 |             int buffer = data[0];
 205 |             int next = 1;
 206 |             int bitsLeft = 8;
 207 |             while (bitsLeft > 0 || next < data.Length)
 208 |             {
 209 |                 if (bitsLeft < 5)
 210 |                 {
 211 |                     if (next < data.Length)
 212 |                     {
 213 |                         buffer <<= 8;
 214 |                         buffer |= data[next++] & 0xff;
 215 |                         bitsLeft += 8;
 216 |                     }
 217 |                     else
 218 |                     {
 219 |                         int pad = 5 - bitsLeft;
 220 |                         buffer <<= pad;
 221 |                         bitsLeft += pad;
 222 |                     }
 223 |                 }
 224 |                 int index = (buffer >> (bitsLeft - 5)) & 0x1f;
 225 |                 bitsLeft -= 5;
 226 |                 sb.Append(Alphabet[index]);
 227 |             }
 228 |             return sb.ToString();
 229 |         }
```

---

### `Base32Decode` — lines 230–257

#### Signature

```csharp
private static byte[] Base32Decode(string input)
```

#### What it is

Function `Base32Decode` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Base32Decode`.
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
| `output` | `var` | Holds “output” for this scope.  Newly constructed object. |
| `buffer` | `int` | Holds “buffer” for this scope. (integer) |
| `val` | `int` | Holds “val” for this scope. (integer) |
| `trimmed` | `var` | Holds “trimmed” for this scope.  Newly constructed object. |
| `c` | `—` | Temporary value (character, course, or counter depending on loop). |

#### Code

```csharp
 230 | 
 231 |         private static byte[] Base32Decode(string input)
 232 |         {
 233 |             string s = NormalizeSecret(input);
 234 |             if (s.Length == 0) return new byte[0];
 235 | 
 236 |             var output = new byte[s.Length * 5 / 8];
 237 |             int buffer = 0, bitsLeft = 0, index = 0;
 238 |             foreach (char c in s)
 239 |             {
 240 |                 int val = Alphabet.IndexOf(c);
 241 |                 if (val < 0) continue;
 242 |                 buffer = (buffer << 5) | val;
 243 |                 bitsLeft += 5;
 244 |                 if (bitsLeft >= 8)
 245 |                 {
 246 |                     output[index++] = (byte)((buffer >> (bitsLeft - 8)) & 0xff);
 247 |                     bitsLeft -= 8;
 248 |                 }
 249 |             }
 250 |             if (index != output.Length)
 251 |             {
 252 |                 var trimmed = new byte[index];
 253 |                 Array.Copy(output, trimmed, index);
 254 |                 return trimmed;
 255 |             }
 256 |             return output;
 257 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using System.Globalization;
   3 | using System.Security.Cryptography;
   4 | using System.Text;
   5 | using System.Web;
   6 | 
   7 | namespace WebAppAssignment.Data.Security
   8 | {
   9 |     /// <summary>
  10 |     /// RFC 6238 TOTP (6 digits, 30s step, HMAC-SHA1) for Google Authenticator / Authy.
  11 |     /// Secret is standard Base32 (RFC 4648), no padding.
  12 |     /// </summary>
  13 |     public static class TotpHelper
  14 |     {
  15 |         private const int Digits = 6;
  16 |         private const int StepSeconds = 30;
  17 |         private const string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
  18 | 
  19 |         public static string GenerateSecret(int bytes = 20)
  20 |         {
  21 |             var raw = new byte[bytes];
  22 |             using (var rng = RandomNumberGenerator.Create())
  23 |             rng.GetBytes(raw);
  24 |             return Base32Encode(raw);
  25 |         }
  26 | 
  27 |         public static string GenerateCode(string base32Secret, DateTime? utcNow = null)
  28 |         {
  29 |             byte[] key = Base32Decode(base32Secret);
  30 |             if (key == null || key.Length == 0)
  31 |             throw new ArgumentException("Invalid TOTP secret.");
  32 |             long timestep = GetTimeStep(utcNow ?? DateTime.UtcNow);
  33 |             return ComputeTotp(key, timestep);
  34 |         }
  35 | 
  36 |         /// <summary>
  37 |         /// Verify a 6-digit code. Default window ±4 steps (±2 min) for phone/PC clock skew.
  38 |         /// </summary>
  39 |         public static bool VerifyCode(string base32Secret, string code, int window = 4)
  40 |         {
  41 |             if (string.IsNullOrWhiteSpace(base32Secret) || string.IsNullOrWhiteSpace(code))
  42 |                 return false;
  43 | 
  44 |             code = NormalizeCode(code);
  45 |             if (code.Length != Digits) return false;
  46 | 
  47 |             byte[] key = Base32Decode(base32Secret);
  48 |             if (key == null || key.Length == 0) return false;
  49 | 
  50 |             // Always use UTC unix seconds (Kind-safe)
  51 |             long step = GetTimeStep(DateTime.UtcNow);
  52 |             for (int w = -window; w <= window; w++)
  53 |             {
  54 |                 if (FixedTimeEquals(ComputeTotp(key, step + w), code))
  55 |                     return true;
  56 |             }
  57 |             return false;
  58 |         }
  59 | 
  60 |         /// <summary>Strip spaces/dashes; map full-width / Unicode digits to ASCII 0-9.</summary>
  61 |         public static string NormalizeCode(string code)
  62 |         {
  63 |             if (string.IsNullOrEmpty(code)) return "";
  64 |             var cleaned = new StringBuilder(code.Length);
  65 |             foreach (char c in code)
  66 |             {
  67 |                 if (c >= '0' && c <= '9')
  68 |                 {
  69 |                     cleaned.Append(c);
  70 |                     continue;
  71 |                 }
  72 |                 // Full-width digits ０-９ and other numeric chars
  73 |                 double nv = char.GetNumericValue(c);
  74 |                 if (nv >= 0 && nv <= 9 && nv == Math.Floor(nv))
  75 |                     cleaned.Append((char)('0' + (int)nv));
  76 |             }
  77 |             return cleaned.ToString();
  78 |         }
  79 | 
  80 |         /// <summary>
  81 |         /// Google Authenticator otpauth URI.
  82 |         /// Format: otpauth://totp/Issuer:account?secret=BASE32&amp;issuer=Issuer&amp;algorithm=SHA1&amp;digits=6&amp;period=30
  83 |         /// Colon between issuer and account must NOT be percent-encoded.
  84 |         /// </summary>
  85 |         public static string BuildOtpAuthUri(string email, string base32Secret, string issuer = "EduLMS")
  86 |         {
  87 |             if (string.IsNullOrWhiteSpace(base32Secret))
  88 |             throw new ArgumentException("secret required");
  89 | 
  90 |             issuer = string.IsNullOrWhiteSpace(issuer) ? "EduLMS" : issuer.Trim();
  91 |             email = (email ?? "user").Trim();
  92 |             string secret = NormalizeSecret(base32Secret);
  93 | 
  94 |             // Path label: Issuer:account - encode each part, keep colon literal
  95 |             string label = EncodePathSegment(issuer) + ":" + EncodePathSegment(email);
  96 | 
  97 |             var qs = new StringBuilder();
  98 |             qs.Append("secret=").Append(secret); // base32 A-Z2-7 only - safe unencoded
  99 |             qs.Append("&issuer=").Append(Uri.EscapeDataString(issuer));
 100 |             qs.Append("&algorithm=SHA1");
 101 |             qs.Append("&digits=").Append(Digits);
 102 |             qs.Append("&period=").Append(StepSeconds);
 103 | 
 104 |             return "otpauth://totp/" + label + "?" + qs;
 105 |         }
 106 | 
 107 |         /// <summary>Format secret in groups of 4 for easier manual entry.</summary>
 108 |         public static string FormatSecretForDisplay(string base32Secret)
 109 |         {
 110 |             string s = NormalizeSecret(base32Secret);
 111 |             if (s.Length == 0) return "";
 112 |             var sb = new StringBuilder();
 113 |             for (int i = 0; i < s.Length; i++)
 114 |             {
 115 |                 if (i > 0 && i % 4 == 0) sb.Append(' ');
 116 |                 sb.Append(s[i]);
 117 |             }
 118 |             return sb.ToString();
 119 |         }
 120 | 
 121 |         public static string NormalizeSecret(string base32Secret)
 122 |         {
 123 |             if (string.IsNullOrWhiteSpace(base32Secret)) return "";
 124 |             var sb = new StringBuilder(base32Secret.Length);
 125 |             foreach (char c in base32Secret.Trim().ToUpperInvariant())
 126 |             {
 127 |                 if (c == ' ' || c == '-' || c == '=') continue;
 128 |                 // common OCR/typo: 0/1/8 → O/I/B not in alphabet; skip invalid
 129 |                 if (Alphabet.IndexOf(c) >= 0)
 130 |                 sb.Append(c);
 131 |             }
 132 |             return sb.ToString();
 133 |         }
 134 | 
 135 |         /// <summary>Simple numeric OTP for email fallback (not TOTP).</summary>
 136 |         public static string GenerateEmailOtp(int length = 6)
 137 |         {
 138 |             var bytes = new byte[4];
 139 |             using (var rng = RandomNumberGenerator.Create())
 140 |             rng.GetBytes(bytes);
 141 |             int n = Math.Abs(BitConverter.ToInt32(bytes, 0)) % (int)Math.Pow(10, length);
 142 |             return n.ToString(CultureInfo.InvariantCulture).PadLeft(length, '0');
 143 |         }
 144 | 
 145 |         private static string EncodePathSegment(string value)
 146 |         {
 147 |             // Encode for URI path but keep @ unescaped is optional; EscapeDataString is safe
 148 |             return Uri.EscapeDataString(value ?? "");
 149 |         }
 150 | 
 151 |         private static long GetTimeStep(DateTime when)
 152 |         {
 153 |             // Kind.Unspecified: treat as UTC (server clock). Local would skew TOTP.
 154 |             DateTime utc = when.Kind == DateTimeKind.Local
 155 |                 ? when.ToUniversalTime()
 156 |                 : DateTime.SpecifyKind(when, DateTimeKind.Utc);
 157 |             DateTime epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
 158 |             long unix = (long)(utc - epoch).TotalSeconds;
 159 |             if (unix < 0) unix = 0;
 160 |             return unix / StepSeconds;
 161 |         }
 162 | 
 163 |         private static string ComputeTotp(byte[] key, long timestep)
 164 |         {
 165 |             // 8-byte big-endian counter (RFC 4226)
 166 |             byte[] counter = new byte[8];
 167 |             ulong ts = (ulong)timestep;
 168 |             counter[0] = (byte)(ts >> 56);
 169 |             counter[1] = (byte)(ts >> 48);
 170 |             counter[2] = (byte)(ts >> 40);
 171 |             counter[3] = (byte)(ts >> 32);
 172 |             counter[4] = (byte)(ts >> 24);
 173 |             counter[5] = (byte)(ts >> 16);
 174 |             counter[6] = (byte)(ts >> 8);
 175 |             counter[7] = (byte)ts;
 176 | 
 177 |             using (var hmac = new HMACSHA1(key))
 178 |             {
 179 |                 byte[] hash = hmac.ComputeHash(counter);
 180 |                 int offset = hash[hash.Length - 1] & 0x0F;
 181 |                 int binary =
 182 |                 ((hash[offset] & 0x7f) << 24) |
 183 |                 ((hash[offset + 1] & 0xff) << 16) |
 184 |                 ((hash[offset + 2] & 0xff) << 8) |
 185 |                 (hash[offset + 3] & 0xff);
 186 |                 int otp = binary % 1000000;
 187 |                 return otp.ToString(CultureInfo.InvariantCulture).PadLeft(Digits, '0');
 188 |             }
 189 |         }
 190 | 
 191 |         private static bool FixedTimeEquals(string a, string b)
 192 |         {
 193 |             if (a == null || b == null || a.Length != b.Length) return false;
 194 |             int diff = 0;
 195 |             for (int i = 0; i < a.Length; i++)
 196 |             diff |= a[i] ^ b[i];
 197 |             return diff == 0;
 198 |         }
 199 | 
 200 |         private static string Base32Encode(byte[] data)
 201 |         {
 202 |             if (data == null || data.Length == 0) return "";
 203 |             var sb = new StringBuilder((data.Length * 8 + 4) / 5);
 204 |             int buffer = data[0];
 205 |             int next = 1;
 206 |             int bitsLeft = 8;
 207 |             while (bitsLeft > 0 || next < data.Length)
 208 |             {
 209 |                 if (bitsLeft < 5)
 210 |                 {
 211 |                     if (next < data.Length)
 212 |                     {
 213 |                         buffer <<= 8;
 214 |                         buffer |= data[next++] & 0xff;
 215 |                         bitsLeft += 8;
 216 |                     }
 217 |                     else
 218 |                     {
 219 |                         int pad = 5 - bitsLeft;
 220 |                         buffer <<= pad;
 221 |                         bitsLeft += pad;
 222 |                     }
 223 |                 }
 224 |                 int index = (buffer >> (bitsLeft - 5)) & 0x1f;
 225 |                 bitsLeft -= 5;
 226 |                 sb.Append(Alphabet[index]);
 227 |             }
 228 |             return sb.ToString();
 229 |         }
 230 | 
 231 |         private static byte[] Base32Decode(string input)
 232 |         {
 233 |             string s = NormalizeSecret(input);
 234 |             if (s.Length == 0) return new byte[0];
 235 | 
 236 |             var output = new byte[s.Length * 5 / 8];
 237 |             int buffer = 0, bitsLeft = 0, index = 0;
 238 |             foreach (char c in s)
 239 |             {
 240 |                 int val = Alphabet.IndexOf(c);
 241 |                 if (val < 0) continue;
 242 |                 buffer = (buffer << 5) | val;
 243 |                 bitsLeft += 5;
 244 |                 if (bitsLeft >= 8)
 245 |                 {
 246 |                     output[index++] = (byte)((buffer >> (bitsLeft - 8)) & 0xff);
 247 |                     bitsLeft -= 8;
 248 |                 }
 249 |             }
 250 |             if (index != output.Length)
 251 |             {
 252 |                 var trimmed = new byte[index];
 253 |                 Array.Copy(output, trimmed, index);
 254 |                 return trimmed;
 255 |             }
 256 |             return output;
 257 |         }
 258 |     }
 259 | }
```
