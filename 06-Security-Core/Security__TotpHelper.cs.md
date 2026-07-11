# TotpHelper.cs
**Source:** `Data/Security/TotpHelper.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

RFC 6238 TOTP (Google Authenticator): secret generate, verify ± window, otpauth URI, Base32.

## File overview

- **Total lines:** 259
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 21:** `raw` (`var`) — **Raw bytes or unprocessed input string.**
- **Line 29:** `key` (`byte[]`) — **HMAC key bytes or dictionary key.**
- **Line 32:** `timestep` (`long`) — **Date/time value. (integer)**
- **Line 42:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 46:** `key` (`byte[]`) — **HMAC key bytes or dictionary key.**
- **Line 51:** `step` (`long`) — **TOTP 30-second time step counter.**
- **Line 55:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 57:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 64:** `cleaned` (`var`) — **Holds “cleaned” for this scope.**
- **Line 73:** `nv` (`double`) — **Holds “nv” for this scope. (number/score)**
- **Line 92:** `secret` (`string`) — **MFA TOTP Base32 secret for authenticator apps.**
- **Line 95:** `label` (`string`) — **otpauth account label (issuer:email).**
- **Line 96:** `qs` (`var`) — **Holds “qs” for this scope.**
- **Line 110:** `s` (`string`) — **String being cleaned or built.**
- **Line 112:** `sb` (`var`) — **StringBuilder — efficient string concatenation.**
- **Line 124:** `sb` (`var`) — **StringBuilder — efficient string concatenation.**
- **Line 138:** `bytes` (`var`) — **Byte array (hash, random, file content).**
- **Line 141:** `n` (`int`) — **Integer count (rows, items, or length).**
- **Line 154:** `utc` (`DateTime`) — **Date/time value. (date/time)**
- **Line 157:** `epoch` (`DateTime`) — **Holds “epoch” for this scope. (date/time)**
- **Line 158:** `unix` (`long`) — **Holds “unix” for this scope. (integer)**
- **Line 166:** `counter` (`byte[]`) — **Holds “counter” for this scope. (type `byte[]`)**
- **Line 167:** `ts` (`ulong`) — **Holds “ts” for this scope. (type `ulong`)**
- **Line 179:** `hash` (`byte[]`) — **Password hash (PBKDF2) stored in DB.**
- **Line 180:** `offset` (`int`) — **Holds “offset” for this scope. (integer)**
- **Line 181:** `binary` (`int`) — **Holds “binary” for this scope. (integer)**
- **Line 186:** `otp` (`int`) — **Holds “otp” for this scope. (integer)**
- **Line 194:** `diff` (`int`) — **Holds “diff” for this scope. (integer)**
- **Line 197:** `diff` (`return`) — **Holds “diff” for this scope. (type `return`)**
- **Line 203:** `sb` (`var`) — **StringBuilder — efficient string concatenation.**
- **Line 204:** `buffer` (`int`) — **Holds “buffer” for this scope. (integer)**
- **Line 205:** `next` (`int`) — **Holds “next” for this scope. (integer)**
- **Line 206:** `bitsLeft` (`int`) — **Holds “bits Left” for this scope. (integer)**
- **Line 219:** `pad` (`int`) — **Holds “pad” for this scope. (integer)**
- **Line 224:** `index` (`int`) — **Holds “index” for this scope. (integer)**
- **Line 233:** `s` (`string`) — **String being cleaned or built.**
- **Line 235:** `output` (`var`) — **Holds “output” for this scope.**
- **Line 237:** `buffer` (`int`) — **Holds “buffer” for this scope. (integer)**
- **Line 240:** `val` (`int`) — **Holds “val” for this scope. (integer)**
- **Line 252:** `trimmed` (`var`) — **Holds “trimmed” for this scope.**
- **Line 254:** `trimmed` (`return`) — **Holds “trimmed” for this scope. (type `return`)**
- **Line 256:** `output` (`return`) — **Holds “output” for this scope. (type `return`)**

## Functions / methods (14 found)

### `GenerateSecret` — lines 18–25

```csharp
public static string GenerateSecret(int bytes = 20)
```

#### Explanation

- **Purpose:** Implements `GenerateSecret`.
- **Parameters (what each means):**
- `bytes` (`int`) — Byte array (hash, random, file content).
- **Local variables (what each means):**
- `bytes` (`int`) — Byte array (hash, random, file content).  Newly constructed object.
- `rng` (`var`) — Holds “rng” for this scope.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L19:** Create new authenticator secret (Base32).
=======
**Line notes** (what code + variables mean)

- **L19:** Create new authenticator secret (Base32).
- **L21:** `raw` means: Raw bytes or unprocessed input string.  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L22:** Import namespace/types.
- **L24:** TOTP / authenticator (RFC 6238) helper.

---

### `GenerateCode` — lines 26–34

```csharp
public static string GenerateCode(string base32Secret, DateTime? utcNow = null)
```

#### Explanation

- **Purpose:** Implements `GenerateCode`.
- **Parameters (what each means):**
- `base32Secret` (`string`) — Secret key material (MFA Base32 or crypto secret). (text)
- `utcNow` (`DateTime?`) — Holds “utc Now” for this scope. (date/time)
- **Local variables (what each means):**
- `utcNow` (`DateTime?`) — Holds “utc Now” for this scope. (date/time)
- `timestep` (`long`) — Date/time value. (integer)

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L29:** TOTP / authenticator (RFC 6238) helper.
=======
**Line notes** (what code + variables mean)

- **L29:** TOTP / authenticator (RFC 6238) helper.
- **L32:** `timestep` means: Date/time value. (integer)
>>>>>>> eb8ce01 (update)

---

### `VerifyCode` — lines 39–58

```csharp
public static bool VerifyCode(string base32Secret, string code, int window = 4)
```

#### Explanation

- **Purpose:** Implements `VerifyCode`.
- **Parameters (what each means):**
- `base32Secret` (`string`) — Secret key material (MFA Base32 or crypto secret). (text)
- `code` (`string`) — 6-digit TOTP / OTP the user typed.
- `window` (`int`) — TOTP time-step window (± steps for clock skew).
- **Local variables (what each means):**
- `key` (`byte[]`) — HMAC key bytes or dictionary key.
- `step` (`long`) — TOTP 30-second time step counter.
- `w` (`int`) — Holds “w” for this scope. (integer)

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L39:** Verify multi-factor / TOTP code.
- **L47:** TOTP / authenticator (RFC 6238) helper.
=======
**Line notes** (what code + variables mean)

- **L39:** Verify multi-factor / TOTP code.
- **L47:** TOTP / authenticator (RFC 6238) helper.
- **L51:** `step` means: TOTP 30-second time step counter.
>>>>>>> eb8ce01 (update)
- **L54:** Constant-time string compare (reduce timing leaks).

---

### `NormalizeCode` — lines 61–78

```csharp
public static string NormalizeCode(string code)
```

#### Explanation

- **Purpose:** Implements `NormalizeCode`.
- **Parameters (what each means):**
- `code` (`string`) — 6-digit TOTP / OTP the user typed.
- **Local variables (what each means):**
- `cleaned` (`var`) — Holds “cleaned” for this scope.  Newly constructed object.
- `nv` (`double`) — Holds “nv” for this scope. (number/score)
- `c` — Temporary value (character, course, or counter depending on loop).

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L64:** `cleaned` means: Holds “cleaned” for this scope.  Newly constructed object.
- **L73:** `nv` means: Holds “nv” for this scope. (number/score)
>>>>>>> eb8ce01 (update)

---

### `BuildOtpAuthUri` — lines 85–105

```csharp
public static string BuildOtpAuthUri(string email, string base32Secret, string issuer = "EduLMS")
```

#### Explanation

- **Purpose:** Implements `BuildOtpAuthUri`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `base32Secret` (`string`) — Secret key material (MFA Base32 or crypto secret). (text)
- `issuer` (`string`) — TOTP issuer label (EduLMS).
- **Local variables (what each means):**
- `secret` (`string`) — MFA TOTP Base32 secret for authenticator apps.
- `label` (`string`) — otpauth account label (issuer:email).
- `qs` (`var`) — Holds “qs” for this scope.  Newly constructed object.

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L85:** Build otpauth:// URI for QR code.
=======
**Line notes** (what code + variables mean)

- **L85:** Build otpauth:// URI for QR code.
- **L92:** `secret` means: MFA TOTP Base32 secret for authenticator apps.
- **L95:** `label` means: otpauth account label (issuer:email).
- **L97:** `qs` means: Holds “qs” for this scope.  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L104:** TOTP / authenticator (RFC 6238) helper.

---

### `FormatSecretForDisplay` — lines 108–119

```csharp
public static string FormatSecretForDisplay(string base32Secret)
```

#### Explanation

- **Purpose:** Implements `FormatSecretForDisplay`.
- **Parameters (what each means):**
- `base32Secret` (`string`) — Secret key material (MFA Base32 or crypto secret). (text)
- **Local variables (what each means):**
- `s` (`string`) — String being cleaned or built.
- `sb` (`var`) — StringBuilder — efficient string concatenation.  Newly constructed object.
- `i` (`int`) — Loop index (0-based counter in for-loops).  Literal number `0`.

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L110:** `s` means: String being cleaned or built.
- **L112:** `sb` means: StringBuilder — efficient string concatenation.  Newly constructed object.
>>>>>>> eb8ce01 (update)

---

### `NormalizeSecret` — lines 120–133

```csharp
public static string NormalizeSecret(string base32Secret)
```

#### Explanation

- **Purpose:** Implements `NormalizeSecret`.
- **Parameters (what each means):**
- `base32Secret` (`string`) — Secret key material (MFA Base32 or crypto secret). (text)
- **Local variables (what each means):**
- `sb` (`var`) — StringBuilder — efficient string concatenation.  Newly constructed object.
- `c` — Temporary value (character, course, or counter depending on loop).

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L124:** `sb` means: StringBuilder — efficient string concatenation.  Newly constructed object.
>>>>>>> eb8ce01 (update)

---

### `GenerateEmailOtp` — lines 136–143

```csharp
public static string GenerateEmailOtp(int length = 6)
```

#### Explanation

- **Purpose:** Implements `GenerateEmailOtp`.
- **Parameters (what each means):**
- `length` (`int`) — Holds “length” for this scope. (integer)
- **Local variables (what each means):**
- `bytes` (`var`) — Byte array (hash, random, file content).  Newly constructed object.
- `rng` (`var`) — Holds “rng” for this scope.
- `n` (`int`) — Integer count (rows, items, or length).

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L139:** Import namespace/types.
=======
**Line notes** (what code + variables mean)

- **L138:** `bytes` means: Byte array (hash, random, file content).  Newly constructed object.
- **L139:** Import namespace/types.
- **L141:** `n` means: Integer count (rows, items, or length).
>>>>>>> eb8ce01 (update)

---

### `EncodePathSegment` — lines 144–149

```csharp
private static string EncodePathSegment(string value)
```

#### Explanation

- **Purpose:** Implements `EncodePathSegment`.
- **Parameters (what each means):**
- `value` (`string`) — Holds “value” for this scope. (text)

#### Line-by-line (this function)

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

```csharp
private static long GetTimeStep(DateTime when)
```

#### Explanation

- **Purpose:** Implements `GetTimeStep`.
- **Pattern:** Read/load data for display.
- **Parameters (what each means):**
- `when` (`DateTime`) — Holds “when” for this scope. (date/time)
- **Local variables (what each means):**
- `utc` (`DateTime`) — Date/time value. (date/time)
- `epoch` (`DateTime`) — Holds “epoch” for this scope. (date/time)  Newly constructed object.
- `unix` (`long`) — Holds “unix” for this scope. (integer)

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L154:** `utc` means: Date/time value. (date/time)
- **L157:** `epoch` means: Holds “epoch” for this scope. (date/time)  Newly constructed object.
- **L158:** `unix` means: Holds “unix” for this scope. (integer)
>>>>>>> eb8ce01 (update)

---

### `ComputeTotp` — lines 162–189

```csharp
private static string ComputeTotp(byte[] key, long timestep)
```

#### Explanation

- **Purpose:** Implements `ComputeTotp`.
- **Parameters (what each means):**
- `key` (`byte[]`) — HMAC key bytes or dictionary key.
- `timestep` (`long`) — Date/time value. (integer)
- **Local variables (what each means):**
- `counter` (`byte[]`) — Holds “counter” for this scope. (type `byte[]`)  Newly constructed object.
- `hmac` (`var`) — Holds “hmac” for this scope.  Newly constructed object.
- `offset` (`int`) — Holds “offset” for this scope. (integer)
- `binary` (`int`) — Holds “binary” for this scope. (integer)
- `otp` (`int`) — Holds “otp” for this scope. (integer)

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L177:** Import namespace/types.
=======
**Line notes** (what code + variables mean)

- **L177:** Import namespace/types.
- **L180:** `offset` means: Holds “offset” for this scope. (integer)
- **L186:** `otp` means: Holds “otp” for this scope. (integer)
>>>>>>> eb8ce01 (update)

---

### `FixedTimeEquals` — lines 190–198

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

<<<<<<< HEAD
**Line notes**

- **L191:** Constant-time string compare (reduce timing leaks).
=======
**Line notes** (what code + variables mean)

- **L191:** Constant-time string compare (reduce timing leaks).
- **L194:** `diff` means: Holds “diff” for this scope. (integer)  Literal number `0`.
>>>>>>> eb8ce01 (update)

---

### `Base32Encode` — lines 199–229

```csharp
private static string Base32Encode(byte[] data)
```

#### Explanation

- **Purpose:** Implements `Base32Encode`.
- **Parameters (what each means):**
- `data` (`byte[]`) — Holds “data” for this scope. (type `byte[]`)
- **Local variables (what each means):**
- `sb` (`var`) — StringBuilder — efficient string concatenation.  Newly constructed object.
- `buffer` (`int`) — Holds “buffer” for this scope. (integer)
- `next` (`int`) — Holds “next” for this scope. (integer)  Literal number `1`.
- `bitsLeft` (`int`) — Holds “bits Left” for this scope. (integer)  Literal number `8`.
- `pad` (`int`) — Holds “pad” for this scope. (integer)
- `index` (`int`) — Holds “index” for this scope. (integer)

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L200:** TOTP / authenticator (RFC 6238) helper.
=======
**Line notes** (what code + variables mean)

- **L200:** TOTP / authenticator (RFC 6238) helper.
- **L203:** `sb` means: StringBuilder — efficient string concatenation.  Newly constructed object.
- **L204:** `buffer` means: Holds “buffer” for this scope. (integer)
- **L205:** `next` means: Holds “next” for this scope. (integer)  Literal number `1`.
- **L206:** `bitsLeft` means: Holds “bits Left” for this scope. (integer)  Literal number `8`.
- **L219:** `pad` means: Holds “pad” for this scope. (integer)
- **L224:** `index` means: Holds “index” for this scope. (integer)
>>>>>>> eb8ce01 (update)

---

### `Base32Decode` — lines 230–257

```csharp
private static byte[] Base32Decode(string input)
```

#### Explanation

- **Purpose:** Implements `Base32Decode`.
- **Parameters (what each means):**
- `input` (`string`) — Holds “input” for this scope. (text)
- **Local variables (what each means):**
- `s` (`string`) — String being cleaned or built.
- `output` (`var`) — Holds “output” for this scope.  Newly constructed object.
- `buffer` (`int`) — Holds “buffer” for this scope. (integer)
- `val` (`int`) — Holds “val” for this scope. (integer)
- `trimmed` (`var`) — Holds “trimmed” for this scope.  Newly constructed object.
- `c` — Temporary value (character, course, or counter depending on loop).

#### Line-by-line (this function)

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

<<<<<<< HEAD
**Line notes**

- **L231:** TOTP / authenticator (RFC 6238) helper.
=======
**Line notes** (what code + variables mean)

- **L231:** TOTP / authenticator (RFC 6238) helper.
- **L233:** `s` means: String being cleaned or built.
- **L236:** `output` means: Holds “output” for this scope.  Newly constructed object.
- **L237:** `buffer` means: Holds “buffer” for this scope. (integer)
- **L240:** `val` means: Holds “val” for this scope. (integer)
- **L252:** `trimmed` means: Holds “trimmed” for this scope.  Newly constructed object.
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

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L7:** C# namespace grouping.
- **L13:** TOTP / authenticator (RFC 6238) helper.
- **L19:** Create new authenticator secret (Base32).
<<<<<<< HEAD
- **L22:** Import namespace/types.
- **L24:** TOTP / authenticator (RFC 6238) helper.
- **L29:** TOTP / authenticator (RFC 6238) helper.
- **L39:** Verify multi-factor / TOTP code.
- **L47:** TOTP / authenticator (RFC 6238) helper.
- **L54:** Constant-time string compare (reduce timing leaks).
- **L85:** Build otpauth:// URI for QR code.
- **L104:** TOTP / authenticator (RFC 6238) helper.
- **L139:** Import namespace/types.
- **L177:** Import namespace/types.
- **L191:** Constant-time string compare (reduce timing leaks).
- **L200:** TOTP / authenticator (RFC 6238) helper.
- **L231:** TOTP / authenticator (RFC 6238) helper.
=======
- **L21:** `raw` means: Raw bytes or unprocessed input string.  Newly constructed object.
- **L22:** Import namespace/types.
- **L24:** TOTP / authenticator (RFC 6238) helper.
- **L29:** TOTP / authenticator (RFC 6238) helper.
- **L32:** `timestep` means: Date/time value. (integer)
- **L39:** Verify multi-factor / TOTP code.
- **L47:** TOTP / authenticator (RFC 6238) helper.
- **L51:** `step` means: TOTP 30-second time step counter.
- **L54:** Constant-time string compare (reduce timing leaks).
- **L64:** `cleaned` means: Holds “cleaned” for this scope.  Newly constructed object.
- **L73:** `nv` means: Holds “nv” for this scope. (number/score)
- **L85:** Build otpauth:// URI for QR code.
- **L92:** `secret` means: MFA TOTP Base32 secret for authenticator apps.
- **L95:** `label` means: otpauth account label (issuer:email).
- **L97:** `qs` means: Holds “qs” for this scope.  Newly constructed object.
- **L104:** TOTP / authenticator (RFC 6238) helper.
- **L110:** `s` means: String being cleaned or built.
- **L112:** `sb` means: StringBuilder — efficient string concatenation.  Newly constructed object.
- **L124:** `sb` means: StringBuilder — efficient string concatenation.  Newly constructed object.
- **L138:** `bytes` means: Byte array (hash, random, file content).  Newly constructed object.
- **L139:** Import namespace/types.
- **L141:** `n` means: Integer count (rows, items, or length).
- **L154:** `utc` means: Date/time value. (date/time)
- **L157:** `epoch` means: Holds “epoch” for this scope. (date/time)  Newly constructed object.
- **L158:** `unix` means: Holds “unix” for this scope. (integer)
- **L177:** Import namespace/types.
- **L180:** `offset` means: Holds “offset” for this scope. (integer)
- **L186:** `otp` means: Holds “otp” for this scope. (integer)
- **L191:** Constant-time string compare (reduce timing leaks).
- **L194:** `diff` means: Holds “diff” for this scope. (integer)  Literal number `0`.
- **L200:** TOTP / authenticator (RFC 6238) helper.
- **L203:** `sb` means: StringBuilder — efficient string concatenation.  Newly constructed object.
- **L204:** `buffer` means: Holds “buffer” for this scope. (integer)
- **L205:** `next` means: Holds “next” for this scope. (integer)  Literal number `1`.
- **L206:** `bitsLeft` means: Holds “bits Left” for this scope. (integer)  Literal number `8`.
- **L219:** `pad` means: Holds “pad” for this scope. (integer)
- **L224:** `index` means: Holds “index” for this scope. (integer)
- **L231:** TOTP / authenticator (RFC 6238) helper.
- **L233:** `s` means: String being cleaned or built.
- **L236:** `output` means: Holds “output” for this scope.  Newly constructed object.
- **L237:** `buffer` means: Holds “buffer” for this scope. (integer)
- **L240:** `val` means: Holds “val” for this scope. (integer)
- **L252:** `trimmed` means: Holds “trimmed” for this scope.  Newly constructed object.
>>>>>>> eb8ce01 (update)

## Source snapshot (raw)

```csharp
using System;
using System.Globalization;
using System.Security.Cryptography;
using System.Text;
using System.Web;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// RFC 6238 TOTP (6 digits, 30s step, HMAC-SHA1) for Google Authenticator / Authy.
    /// Secret is standard Base32 (RFC 4648), no padding.
    /// </summary>
    public static class TotpHelper
    {
        private const int Digits = 6;
        private const int StepSeconds = 30;
        private const string Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";

        public static string GenerateSecret(int bytes = 20)
        {
            var raw = new byte[bytes];
            using (var rng = RandomNumberGenerator.Create())
            rng.GetBytes(raw);
            return Base32Encode(raw);
        }

        public static string GenerateCode(string base32Secret, DateTime? utcNow = null)
        {
            byte[] key = Base32Decode(base32Secret);
            if (key == null || key.Length == 0)
            throw new ArgumentException("Invalid TOTP secret.");
            long timestep = GetTimeStep(utcNow ?? DateTime.UtcNow);
            return ComputeTotp(key, timestep);
        }

        /// <summary>
        /// Verify a 6-digit code. Default window ±4 steps (±2 min) for phone/PC clock skew.
        /// </summary>
        public static bool VerifyCode(string base32Secret, string code, int window = 4)
        {
            if (string.IsNullOrWhiteSpace(base32Secret) || string.IsNullOrWhiteSpace(code))
                return false;

            code = NormalizeCode(code);
            if (code.Length != Digits) return false;

            byte[] key = Base32Decode(base32Secret);
            if (key == null || key.Length == 0) return false;

            // Always use UTC unix seconds (Kind-safe)
            long step = GetTimeStep(DateTime.UtcNow);
            for (int w = -window; w <= window; w++)
            {
                if (FixedTimeEquals(ComputeTotp(key, step + w), code))
                    return true;
            }
            return false;
        }

        /// <summary>Strip spaces/dashes; map full-width / Unicode digits to ASCII 0-9.</summary>
        public static string NormalizeCode(string code)
        {
            if (string.IsNullOrEmpty(code)) return "";
            var cleaned = new StringBuilder(code.Length);
            foreach (char c in code)
            {
                if (c >= '0' && c <= '9')
                {
                    cleaned.Append(c);
                    continue;
                }
                // Full-width digits ０-９ and other numeric chars
                double nv = char.GetNumericValue(c);
                if (nv >= 0 && nv <= 9 && nv == Math.Floor(nv))
                    cleaned.Append((char)('0' + (int)nv));
            }
            return cleaned.ToString();
        }

        /// <summary>
        /// Google Authenticator otpauth URI.
        /// Format: otpauth://totp/Issuer:account?secret=BASE32&amp;issuer=Issuer&amp;algorithm=SHA1&amp;digits=6&amp;period=30
        /// Colon between issuer and account must NOT be percent-encoded.
        /// </summary>
        public static string BuildOtpAuthUri(string email, string base32Secret, string issuer = "EduLMS")
        {
            if (string.IsNullOrWhiteSpace(base32Secret))
            throw new ArgumentException("secret required");

            issuer = string.IsNullOrWhiteSpace(issuer) ? "EduLMS" : issuer.Trim();
            email = (email ?? "user").Trim();
            string secret = NormalizeSecret(base32Secret);

            // Path label: Issuer:account - encode each part, keep colon literal
            string label = EncodePathSegment(issuer) + ":" + EncodePathSegment(email);

            var qs = new StringBuilder();
            qs.Append("secret=").Append(secret); // base32 A-Z2-7 only - safe unencoded
            qs.Append("&issuer=").Append(Uri.EscapeDataString(issuer));
            qs.Append("&algorithm=SHA1");
            qs.Append("&digits=").Append(Digits);
            qs.Append("&period=").Append(StepSeconds);

            return "otpauth://totp/" + label + "?" + qs;
        }

        /// <summary>Format secret in groups of 4 for easier manual entry.</summary>
        public static string FormatSecretForDisplay(string base32Secret)
        {
            string s = NormalizeSecret(base32Secret);
            if (s.Length == 0) return "";
            var sb = new StringBuilder();
            for (int i = 0; i < s.Length; i++)
            {
                if (i > 0 && i % 4 == 0) sb.Append(' ');
                sb.Append(s[i]);
            }
            return sb.ToString();
        }

        public static string NormalizeSecret(string base32Secret)
        {
            if (string.IsNullOrWhiteSpace(base32Secret)) return "";
            var sb = new StringBuilder(base32Secret.Length);
            foreach (char c in base32Secret.Trim().ToUpperInvariant())
            {
                if (c == ' ' || c == '-' || c == '=') continue;
                // common OCR/typo: 0/1/8 → O/I/B not in alphabet; skip invalid
                if (Alphabet.IndexOf(c) >= 0)
                sb.Append(c);
            }
            return sb.ToString();
        }

        /// <summary>Simple numeric OTP for email fallback (not TOTP).</summary>
        public static string GenerateEmailOtp(int length = 6)
        {
            var bytes = new byte[4];
            using (var rng = RandomNumberGenerator.Create())
            rng.GetBytes(bytes);
            int n = Math.Abs(BitConverter.ToInt32(bytes, 0)) % (int)Math.Pow(10, length);
            return n.ToString(CultureInfo.InvariantCulture).PadLeft(length, '0');
        }

        private static string EncodePathSegment(string value)
        {
            // Encode for URI path but keep @ unescaped is optional; EscapeDataString is safe
            return Uri.EscapeDataString(value ?? "");
        }

        private static long GetTimeStep(DateTime when)
        {
            // Kind.Unspecified: treat as UTC (server clock). Local would skew TOTP.
            DateTime utc = when.Kind == DateTimeKind.Local
                ? when.ToUniversalTime()
                : DateTime.SpecifyKind(when, DateTimeKind.Utc);
            DateTime epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
            long unix = (long)(utc - epoch).TotalSeconds;
            if (unix < 0) unix = 0;
            return unix / StepSeconds;
        }

        private static string ComputeTotp(byte[] key, long timestep)
        {
            // 8-byte big-endian counter (RFC 4226)
            byte[] counter = new byte[8];
            ulong ts = (ulong)timestep;
            counter[0] = (byte)(ts >> 56);
            counter[1] = (byte)(ts >> 48);
            counter[2] = (byte)(ts >> 40);
            counter[3] = (byte)(ts >> 32);
            counter[4] = (byte)(ts >> 24);
            counter[5] = (byte)(ts >> 16);
            counter[6] = (byte)(ts >> 8);
            counter[7] = (byte)ts;

            using (var hmac = new HMACSHA1(key))
            {
                byte[] hash = hmac.ComputeHash(counter);
                int offset = hash[hash.Length - 1] & 0x0F;
                int binary =
                ((hash[offset] & 0x7f) << 24) |
                ((hash[offset + 1] & 0xff) << 16) |
                ((hash[offset + 2] & 0xff) << 8) |
                (hash[offset + 3] & 0xff);
                int otp = binary % 1000000;
                return otp.ToString(CultureInfo.InvariantCulture).PadLeft(Digits, '0');
            }
        }

        private static bool FixedTimeEquals(string a, string b)
        {
            if (a == null || b == null || a.Length != b.Length) return false;
            int diff = 0;
            for (int i = 0; i < a.Length; i++)
            diff |= a[i] ^ b[i];
            return diff == 0;
        }

        private static string Base32Encode(byte[] data)
        {
            if (data == null || data.Length == 0) return "";
            var sb = new StringBuilder((data.Length * 8 + 4) / 5);
            int buffer = data[0];
            int next = 1;
            int bitsLeft = 8;
            while (bitsLeft > 0 || next < data.Length)
            {
                if (bitsLeft < 5)
                {
                    if (next < data.Length)
                    {
                        buffer <<= 8;
                        buffer |= data[next++] & 0xff;
                        bitsLeft += 8;
                    }
                    else
                    {
                        int pad = 5 - bitsLeft;
                        buffer <<= pad;
                        bitsLeft += pad;
                    }
                }
                int index = (buffer >> (bitsLeft - 5)) & 0x1f;
                bitsLeft -= 5;
                sb.Append(Alphabet[index]);
            }
            return sb.ToString();
        }

        private static byte[] Base32Decode(string input)
        {
            string s = NormalizeSecret(input);
            if (s.Length == 0) return new byte[0];

            var output = new byte[s.Length * 5 / 8];
            int buffer = 0, bitsLeft = 0, index = 0;
            foreach (char c in s)
            {
                int val = Alphabet.IndexOf(c);
                if (val < 0) continue;
                buffer = (buffer << 5) | val;
                bitsLeft += 5;
                if (bitsLeft >= 8)
                {
                    output[index++] = (byte)((buffer >> (bitsLeft - 8)) & 0xff);
                    bitsLeft -= 8;
                }
            }
            if (index != output.Length)
            {
                var trimmed = new byte[index];
                Array.Copy(output, trimmed, index);
                return trimmed;
            }
            return output;
        }
    }
}

```
