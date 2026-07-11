# AuthService.cs
**Source:** `Data/Security/AuthService.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Central auth orchestration: pending registration (no DB row until MFA), login password check, admin MFA bypass, TOTP verify, complete login (session + JWT), password reset (MFA then new password).

## File overview

- **Total lines:** 1027
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 46:** `PendingRegTtl` (`TimeSpan`) — **Holds “Pending Reg Ttl” for this scope. (type `TimeSpan`)**
- **Line 63:** `roleCode` (`string`) — **Stored role value (0 Admin / 1 Student / 2 Lecturer).**
- **Line 65:** `roleNormalized` (`string`) — **Friendly role name (Admin, Student, Lecturer).**
- **Line 66:** `rc` (`string`) — **Holds “rc” for this scope. (text)**
- **Line 80:** `exists` (`int`) — **Count > 0 check (email/user/row already exists).**
- **Line 85:** `mfaSecret` (`string`) — **Authenticator secret stored for the user.**
- **Line 126:** `createdUtc` (`DateTime`) — **Date/time value. (date/time)**
- **Line 152:** `exists` (`int`) — **Count > 0 check (email/user/row already exists).**
- **Line 160:** `mfaSecret` (`string`) — **Authenticator secret stored for the user.**
- **Line 162:** `mfaOn` (`int`) — **1/0 flag written to Users.MfaEnabled.**
- **Line 163:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 201:** `byEmail` (`object`) — **Email address.**
- **Line 232:** `stored` (`object`) — **Holds “stored” for this scope.**
- **Line 233:** `storedSecret` (`string`) — **Secret key material (MFA Base32 or crypto secret). (text)**
- **Line 273:** `at` (`DateTime`) — **Timestamp (CreatedUtc / PwdResetAt).**
- **Line 281:** `at` (`DateTime`) — **Timestamp (CreatedUtc / PwdResetAt).**
- **Line 320:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 324:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 325:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 344:** `ctx` (`var`) — **Current HTTP request context (Request, Response, Session).**
- **Line 348:** `lockMsg` (`string`) — **Message shown when the account is temporarily locked.**
- **Line 355:** `user` (`AuthUser`) — **AuthUser or user row (UID, Email, Role, MfaSecret, …).**
- **Line 362:** `stored` (`string`) — **Holds “stored” for this scope. (text)**
- **Line 379:** `newHash` (`string`) — **Cryptographic hash string. (text)**
- **Line 401:** `adminToken` (`string`) — **Security token (JWT or CSRF). (text)**
- **Line 441:** `user` (`AuthUser`) — **AuthUser or user row (UID, Email, Role, MfaSecret, …).**
- **Line 443:** `ok` (`bool`) — **Boolean success flag.**
- **Line 457:** `otp` (`string`) — **Holds “otp” for this scope. (text)**
- **Line 458:** `exp` (`DateTime?`) — **Expiry DateTime.**
- **Line 477:** `secret` (`string`) — **MFA TOTP Base32 secret for authenticator apps.**
- **Line 491:** `token` (`string`) — **JWT or CSRF token string.**
- **Line 518:** `uid` (`int?`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 519:** `email` (`string`) — **Account email address (usually lowercased).**
- **Line 551:** `lockMsg` (`string`) — **Message shown when the account is temporarily locked.**
- **Line 558:** `user` (`AuthUser`) — **AuthUser or user row (UID, Email, Role, MfaSecret, …).**
- **Line 559:** `bad` (`string`) — **Holds “bad” for this scope. (text)**
- **Line 566:** `secret` (`string`) — **MFA TOTP Base32 secret for authenticator apps.**
- **Line 580:** `msg` (`string`) — **Human-readable message (error or success).**
- **Line 591:** `expected` (`string`) — **Holds “expected” for this scope. (text)**
- **Line 592:** `you` (`string`) — **Holds “you” for this scope. (text)**
- **Line 645:** `user` (`AuthUser`) — **AuthUser or user row (UID, Email, Role, MfaSecret, …).**
- **Line 647:** `newHash` (`string`) — **Cryptographic hash string. (text)**
- **Line 684:** `v` (`var`) — **Generic value (version flag in JSON, or loop value).**
- **Line 713:** `o` (`object`) — **Holds “o” for this scope.**
- **Line 719:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 734:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 739:** `uid` (`return`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 751:** `0` (`return`) — **Holds “0” for this scope. (type `return`)**
- **Line 762:** `existing` (`int`) — **Holds “existing” for this scope. (integer)**
- **Line 766:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 776:** `token` (`string`) — **JWT or CSRF token string.**
- **Line 778:** `uid` (`int`) — **User ID (Users.UID) of the logged-in or target user.**
- **Line 783:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 790:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 819:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 825:** `r` (`var`) — **Usually one database row (DataRow) in query loops.**
- **Line 833:** `letter` (`bool`) — **Holds “letter” for this scope. (true/false)**
- **Line 923:** `mfa` (`bool`) — **Holds “mfa” for this scope. (true/false)**
- **Line 953:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 954:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 961:** `i` (`int`) — **Loop index (0-based counter in for-loops).**
- **Line 980:** `flag` (`string`) — **Holds “flag” for this scope. (text)**
- **Line 997:** `u` (`AuthUser`) — **Holds “u” for this scope. (user DTO)**
- **Line 998:** `u` (`return`) — **Holds “u” for this scope. (type `return`)**

## Functions / methods (32 found)

### `StartRegistration` — lines 52–114

```csharp
public static AuthResult StartRegistration(HttpContext ctx, string name, string email, string password, string roleChoice = "Student")
```

#### Explanation

- **Purpose:** Implements `StartRegistration`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- `name` (`string`) — Display name of user/course/criterion.
- `email` (`string`) — Account email address (usually lowercased).
- `password` (`string`) — Plain password from the form (never log this).
- `roleChoice` (`string`) — Role selected on the register form.
- **Local variables (what each means):**
- `rc` (`string`) — Holds “rc” for this scope. (text)
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `mfaSecret` (`string`) — Authenticator secret stored for the user.  New random MFA secret.

#### Line-by-line (this function)

```csharp
  52 |         public static AuthResult StartRegistration(HttpContext ctx, string name, string email, string password, string roleChoice = "Student")
  53 |         {
  54 |             AuthSchema.Ensure();
  55 |             name = (name ?? "").Trim();
  56 |             email = (email ?? "").Trim().ToLowerInvariant();
  57 |             password = password ?? "";
  58 | 
  59 |             if (name.Length < 2) return Fail("Name must be at least 2 characters.");
  60 |             if (!email.Contains("@") || email.Length < 5) return Fail("Enter a valid email address.");
  61 |             if (password.Length < 8) return Fail("Password must be at least 8 characters.");
  62 |             if (!HasComplexity(password)) return Fail("Password needs letters and numbers.");
  63 | 
  64 |             string roleCode;
  65 |             string roleNormalized;
  66 |             string rc = (roleChoice ?? "").Trim().ToLowerInvariant();
  67 |             if (rc == "lecturer" || rc == "teacher" || rc == "2")
  68 |             {
  69 |                 roleCode = "2";
  70 |                 roleNormalized = "Lecturer";
  71 |             }
  72 |             else
  73 |             {
  74 |                 roleCode = "1";
  75 |                 roleNormalized = "Student";
  76 |             }
  77 | 
  78 |             using (var conn = DbHelper.OpenConnection())
  79 |             {
  80 |                 int exists = Convert.ToInt32(Scalar(conn,
  81 |                     "SELECT COUNT(*) FROM Users WHERE Email = @Email",
  82 |                     P("@Email", email)));
  83 |                 if (exists > 0) return Fail("An account with this email already exists.");
  84 |             }
  85 | 
  86 |             string mfaSecret = TotpHelper.GenerateSecret();
  87 |             if (ctx != null && ctx.Session != null)
  88 |             {
  89 |                 ctx.Session[SessRegName] = name;
  90 |                 ctx.Session[SessRegEmail] = email;
  91 |                 ctx.Session[SessRegHash] = PasswordHasher.Hash(password);
  92 |                 ctx.Session[SessRegRole] = roleCode;
  93 |                 ctx.Session[SessRegRoleName] = roleNormalized;
  94 |                 ctx.Session[SessRegSecret] = mfaSecret;
  95 |                 ctx.Session[SessRegAt] = DateTime.UtcNow;
  96 |             }
  97 | 
  98 |             return new AuthResult
  99 |             {
 100 |                 Success = true,
 101 |                 Message = "Scan the QR code and enter the authenticator code to finish creating your account.",
 102 |                 RequiresMfa = true,
 103 |                 User = new AuthUser
 104 |                 {
 105 |                     UID = 0, // not created yet
 106 |                     Name = name,
 107 |                     Email = email,
 108 |                     Role = roleCode,
 109 |                     RoleNormalized = roleNormalized,
 110 |                     MfaEnabled = true,
 111 |                     MfaSecret = mfaSecret
 112 |                 }
 113 |             };
 114 |         }
```

**Line notes** (what code + variables mean)

- **L52:** Pending registration in Session until MFA confirmed.
- **L66:** `rc` means: Holds “rc” for this scope. (text)
- **L78:** Import namespace/types.
- **L80:** `exists` means: Count > 0 check (email/user/row already exists).
- **L82:** Parameterized SQL — prevents classic SQL injection.
- **L86:** TOTP / authenticator (RFC 6238) helper. | `mfaSecret` means: Authenticator secret stored for the user.  New random MFA secret.
- **L89:** Server session for logged-in user.
- **L90:** Server session for logged-in user.
- **L91:** Server session for logged-in user.
- **L92:** Server session for logged-in user.
- **L93:** Server session for logged-in user.
- **L94:** Server session for logged-in user.
- **L95:** Server session for logged-in user.

---

### `FinishRegistration` — lines 120–267

```csharp
public static AuthResult FinishRegistration(HttpContext ctx, string totpCode)
```

#### Explanation

- **Purpose:** Implements `FinishRegistration`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- `totpCode` (`string`) — User-entered 6-digit authenticator code.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `mfaSecret` (`string`) — Authenticator secret stored for the user.
- `mfaOn` (`int`) — 1/0 flag written to Users.MfaEnabled.  Literal number `1`.
- `byEmail` (`object`) — Email address.
- `stored` (`object`) — Holds “stored” for this scope.
- `storedSecret` (`string`) — Secret key material (MFA Base32 or crypto secret). (text)

#### Line-by-line (this function)

```csharp
 120 |         public static AuthResult FinishRegistration(HttpContext ctx, string totpCode)
 121 |         {
 122 |             AuthSchema.Ensure();
 123 |             totpCode = (totpCode ?? "").Trim();
 124 | 
 125 |             string name, email, hash, roleCode, roleNormalized, secret;
 126 |             DateTime createdUtc;
 127 |             if (!TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out createdUtc))
 128 |                 return Fail("Registration session expired. Start again from the form.");
 129 | 
 130 |             if (DateTime.UtcNow - createdUtc > PendingRegTtl)
 131 |             {
 132 |                 ClearPendingRegistration(ctx);
 133 |                 return Fail("Registration timed out (15 minutes). Please register again.");
 134 |             }
 135 | 
 136 |             if (string.IsNullOrEmpty(totpCode))
 137 |                 return Fail("Enter the 6-digit code from your authenticator app.");
 138 | 
 139 |             secret = TotpHelper.NormalizeSecret(secret);
 140 |             if (string.IsNullOrEmpty(secret))
 141 |             {
 142 |                 ClearPendingRegistration(ctx);
 143 |                 return Fail("MFA setup data missing. Please register again.");
 144 |             }
 145 | 
 146 |             if (!TotpHelper.VerifyCode(secret, totpCode))
 147 |                 return Fail("Invalid authenticator code. Open Google Authenticator and enter the current 6-digit code for EduLMS.");
 148 | 
 149 |             // Re-check email free (someone may have taken it while scanning QR)
 150 |             using (var conn = DbHelper.OpenConnection())
 151 |             {
 152 |                 int exists = Convert.ToInt32(Scalar(conn,
 153 |                     "SELECT COUNT(*) FROM Users WHERE Email = @Email",
 154 |                     P("@Email", email)));
 155 |                 if (exists > 0)
 156 |                 {
 157 |                     ClearPendingRegistration(ctx);
 158 |                     return Fail("An account with this email already exists. Sign in instead.");
 159 |                 }
 160 | 
 161 |                 string mfaSecret = secret;
 162 |                 int mfaOn = 1;
 163 |                 int uid;
 164 | 
 165 |                 try
 166 |                 {
 167 |                     uid = Convert.ToInt32(Scalar(conn, @"
 168 |                     INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaSecret, MfaEnabled, CreatedAt)
 169 |                     OUTPUT INSERTED.UID
 170 |                     VALUES (@Name, @Email, @Password, @Role, @PasswordHash, @MfaSecret, @MfaEnabled, @CreatedAt)",
 171 |                         P("@Name", name),
 172 |                         P("@Email", email),
 173 |                         P("@Password", hash),
 174 |                         P("@Role", roleCode),
 175 |                         P("@PasswordHash", hash),
 176 |                         P("@MfaSecret", (object)mfaSecret ?? DBNull.Value),
 177 |                         P("@MfaEnabled", mfaOn),
 178 |                         P("@CreatedAt", DateTime.UtcNow)));
 179 |                 }
 180 |                 catch
 181 |                 {
 182 |                     try
 183 |                     {
 184 |                         uid = Convert.ToInt32(Scalar(conn, @"
 185 |                         INSERT INTO Users (Name, Email, Password, Role)
 186 |                         OUTPUT INSERTED.UID
 187 |                         VALUES (@Name, @Email, @Password, @Role)",
 188 |                             P("@Name", name),
 189 |                             P("@Email", email),
 190 |                             P("@Password", hash),
 191 |                             P("@Role", roleCode)));
 192 |                     }
 193 |                     catch
 194 |                     {
 195 |                         return Fail("Could not create account. Check the Users table and try again.");
 196 |                     }
 197 |                 }
 198 | 
 199 |                 try
 200 |                 {
 201 |                     object byEmail = Scalar(conn, "SELECT UID FROM Users WHERE Email=@Email", P("@Email", email));
 202 |                     if (byEmail != null && byEmail != DBNull.Value)
 203 |                         uid = Convert.ToInt32(byEmail);
 204 |                 }
 205 |                 catch { }
 206 | 
 207 |                 if (uid <= 0)
 208 |                     return Fail("Account insert did not return a valid user id.");
 209 | 
 210 |                 try
 211 |                 {
 212 |                     Exec(conn, @"
 213 |                     UPDATE Users SET Password=@P, PasswordHash=@H, MfaSecret=@S, MfaEnabled=@E WHERE UID=@UID",
 214 |                         P("@P", hash),
 215 |                         P("@H", hash),
 216 |                         P("@S", (object)mfaSecret ?? DBNull.Value),
 217 |                         P("@E", mfaOn),
 218 |                         P("@UID", uid));
 219 |                 }
 220 |                 catch
 221 |                 {
 222 |                     try
 223 |                     {
 224 |                         Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",
 225 |                             P("@P", hash), P("@UID", uid));
 226 |                     }
 227 |                     catch { }
 228 |                 }
 229 | 
 230 |                 try
 231 |                 {
 232 |                     object stored = Scalar(conn, "SELECT MfaSecret FROM Users WHERE UID=@UID", P("@UID", uid));
 233 |                     string storedSecret = stored == null || stored == DBNull.Value
 234 |                         ? ""
 235 |                         : TotpHelper.NormalizeSecret(stored.ToString());
 236 |                     if (storedSecret != mfaSecret)
 237 |                     {
 238 |                         try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }
 239 |                         return Fail("Account could not save MFA secret. Check Users.MfaSecret column, then register again.");
 240 |                     }
 241 |                 }
 242 |                 catch
 243 |                 {
 244 |                     try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }
 245 |                     return Fail("MFA columns missing. Restart the app so schema can update, then register again.");
 246 |                 }
 247 | 
 248 |                 ClearPendingRegistration(ctx);
 249 |                 SecurityAudit.Log("register.ok", uid, roleNormalized, email);
 250 | 
 251 |                 return new AuthResult
 252 |                 {
 253 |                     Success = true,
 254 |                     Message = "Account created as " + roleNormalized + ". Sign in with your password and authenticator.",
 255 |                     User = new AuthUser
 256 |                     {
 257 |                         UID = uid,
 258 |                         Name = name,
 259 |                         Email = email,
 260 |                         Role = roleCode,
 261 |                         RoleNormalized = roleNormalized,
 262 |                         MfaEnabled = true,
 263 |                         MfaSecret = mfaSecret
 264 |                     }
 265 |                 };
 266 |             }
 267 |         }
```

**Line notes** (what code + variables mean)

- **L120:** Pending registration in Session until MFA confirmed.
- **L127:** Pending registration in Session until MFA confirmed.
- **L130:** Pending registration in Session until MFA confirmed.
- **L132:** Pending registration in Session until MFA confirmed.
- **L139:** TOTP / authenticator (RFC 6238) helper.
- **L142:** Pending registration in Session until MFA confirmed.
- **L146:** TOTP / authenticator (RFC 6238) helper.
- **L150:** Import namespace/types.
- **L152:** `exists` means: Count > 0 check (email/user/row already exists).
- **L154:** Parameterized SQL — prevents classic SQL injection.
- **L157:** Pending registration in Session until MFA confirmed.
- **L161:** `mfaSecret` means: Authenticator secret stored for the user.
- **L162:** `mfaOn` means: 1/0 flag written to Users.MfaEnabled.  Literal number `1`.
- **L165:** Error handling block.
- **L169:** Return new identity/UID after INSERT.
- **L171:** Parameterized SQL — prevents classic SQL injection.
- **L172:** Parameterized SQL — prevents classic SQL injection.
- **L173:** Parameterized SQL — prevents classic SQL injection.
- **L174:** Parameterized SQL — prevents classic SQL injection.
- **L175:** Parameterized SQL — prevents classic SQL injection.
- **L176:** Parameterized SQL — prevents classic SQL injection.
- **L177:** Parameterized SQL — prevents classic SQL injection.
- **L178:** Parameterized SQL — prevents classic SQL injection.
- **L180:** Handle/log exception.
- **L182:** Error handling block.
- **L186:** Return new identity/UID after INSERT.
- **L188:** Parameterized SQL — prevents classic SQL injection.
- **L189:** Parameterized SQL — prevents classic SQL injection.
- **L190:** Parameterized SQL — prevents classic SQL injection.
- **L191:** Parameterized SQL — prevents classic SQL injection.
- **L193:** Handle/log exception.
- **L199:** Error handling block.
- **L201:** Parameterized SQL — prevents classic SQL injection. | `byEmail` means: Email address.
- **L202:** Null-safe read from database values.
- **L205:** Handle/log exception.
- **L210:** Error handling block.
- **L214:** Parameterized SQL — prevents classic SQL injection.
- **L215:** Parameterized SQL — prevents classic SQL injection.
- **L216:** Parameterized SQL — prevents classic SQL injection.
- **L217:** Parameterized SQL — prevents classic SQL injection.
- **L218:** Parameterized SQL — prevents classic SQL injection.
- **L220:** Handle/log exception.
- **L222:** Error handling block.
- **L225:** Parameterized SQL — prevents classic SQL injection.
- **L227:** Handle/log exception.
- **L230:** Error handling block.
- **L232:** Parameterized SQL — prevents classic SQL injection. | `stored` means: Holds “stored” for this scope.
- **L233:** Null-safe read from database values. | `storedSecret` means: Secret key material (MFA Base32 or crypto secret). (text)
- **L235:** TOTP / authenticator (RFC 6238) helper.
- **L238:** Parameterized SQL — prevents classic SQL injection.
- **L242:** Handle/log exception.
- **L244:** Parameterized SQL — prevents classic SQL injection.
- **L248:** Pending registration in Session until MFA confirmed.
- **L249:** Write/read security audit events.

---

### `HasPendingRegistration` — lines 270–275

```csharp
public static bool HasPendingRegistration(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `HasPendingRegistration`.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).

#### Line-by-line (this function)

```csharp
 270 |         public static bool HasPendingRegistration(HttpContext ctx)
 271 |         {
 272 |             string name, email, hash, roleCode, roleNormalized, secret;
 273 |             DateTime at;
 274 |             return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out at);
 275 |         }
```

**Line notes** (what code + variables mean)

- **L270:** Pending registration in Session until MFA confirmed.
- **L274:** Pending registration in Session until MFA confirmed.

---

### `TryGetPendingMfaSetup` — lines 278–283

```csharp
public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)
```

#### Explanation

- **Purpose:** Implements `TryGetPendingMfaSetup`.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- `email` (`string`) — Account email address (usually lowercased).
- `mfaSecret` (`string`) — Authenticator secret stored for the user.

#### Line-by-line (this function)

```csharp
 278 |         public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)
 279 |         {
 280 |             string name, hash, roleCode, roleNormalized;
 281 |             DateTime at;
 282 |             return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out mfaSecret, out at);
 283 |         }
```

**Line notes** (what code + variables mean)

- **L282:** Pending registration in Session until MFA confirmed.

---

### `ClearPendingRegistration` — lines 284–299

```csharp
public static void ClearPendingRegistration(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `ClearPendingRegistration`.
- **Session:** Reads/writes ASP.NET Session.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).

#### Line-by-line (this function)

```csharp
 284 | 
 285 |         public static void ClearPendingRegistration(HttpContext ctx)
 286 |         {
 287 |             try
 288 |             {
 289 |                 if (ctx == null || ctx.Session == null) return;
 290 |                 ctx.Session.Remove(SessRegName);
 291 |                 ctx.Session.Remove(SessRegEmail);
 292 |                 ctx.Session.Remove(SessRegHash);
 293 |                 ctx.Session.Remove(SessRegRole);
 294 |                 ctx.Session.Remove(SessRegRoleName);
 295 |                 ctx.Session.Remove(SessRegSecret);
 296 |                 ctx.Session.Remove(SessRegAt);
 297 |             }
 298 |             catch { }
 299 |         }
```

**Line notes** (what code + variables mean)

- **L285:** Pending registration in Session until MFA confirmed.
- **L287:** Error handling block.
- **L290:** Pending registration in Session until MFA confirmed.
- **L291:** Pending registration in Session until MFA confirmed.
- **L292:** Pending registration in Session until MFA confirmed.
- **L293:** Pending registration in Session until MFA confirmed.
- **L294:** Pending registration in Session until MFA confirmed.
- **L295:** Pending registration in Session until MFA confirmed.
- **L296:** Pending registration in Session until MFA confirmed.
- **L298:** Handle/log exception.

---

### `TryReadPendingRegistration` — lines 300–328

```csharp
private static bool TryReadPendingRegistration(
            HttpContext ctx,
            out string name, out string email, out string hash,
            out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc)
```

#### Explanation

- **Purpose:** Implements `TryReadPendingRegistration`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- `name` (`string`) — Display name of user/course/criterion.
- `email` (`string`) — Account email address (usually lowercased).
- `hash` (`string`) — Password hash (PBKDF2) stored in DB.
- `roleCode` (`string`) — Stored role value (0 Admin / 1 Student / 2 Lecturer).
- `roleNormalized` (`string`) — Friendly role name (Admin, Student, Lecturer).
- `secret` (`string`) — MFA TOTP Base32 secret for authenticator apps.
- `createdUtc` (`DateTime`) — Date/time value. (date/time)

#### Line-by-line (this function)

```csharp
 300 | 
 301 |         private static bool TryReadPendingRegistration(
 302 |             HttpContext ctx,
 303 |             out string name, out string email, out string hash,
 304 |             out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc)
 305 |         {
 306 |             name = email = hash = roleCode = roleNormalized = secret = null;
 307 |             createdUtc = DateTime.MinValue;
 308 |             if (ctx == null || ctx.Session == null) return false;
 309 |             try
 310 |             {
 311 |                 name = ctx.Session[SessRegName] as string;
 312 |                 email = ctx.Session[SessRegEmail] as string;
 313 |                 hash = ctx.Session[SessRegHash] as string;
 314 |                 roleCode = ctx.Session[SessRegRole] as string;
 315 |                 roleNormalized = ctx.Session[SessRegRoleName] as string;
 316 |                 secret = ctx.Session[SessRegSecret] as string;
 317 |                 if (ctx.Session[SessRegAt] is DateTime)
 318 |                     createdUtc = (DateTime)ctx.Session[SessRegAt];
 319 |                 else
 320 |                     return false;
 321 | 
 322 |                 if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(email) ||
 323 |                     string.IsNullOrEmpty(hash) || string.IsNullOrEmpty(secret))
 324 |                     return false;
 325 |                 return true;
 326 |             }
 327 |             catch { return false; }
 328 |         }
```

**Line notes** (what code + variables mean)

- **L301:** Pending registration in Session until MFA confirmed.
- **L309:** Error handling block.
- **L311:** Server session for logged-in user.
- **L312:** Server session for logged-in user.
- **L313:** Server session for logged-in user.
- **L314:** Server session for logged-in user.
- **L315:** Server session for logged-in user.
- **L316:** Server session for logged-in user.
- **L317:** Server session for logged-in user.
- **L318:** Server session for logged-in user.
- **L327:** Handle/log exception.

---

### `Register` — lines 331–334

```csharp
public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")
```

#### Explanation

- **Purpose:** Implements `Register`.
- **Parameters (what each means):**
- `name` (`string`) — Display name of user/course/criterion.
- `email` (`string`) — Account email address (usually lowercased).
- `password` (`string`) — Plain password from the form (never log this).
- `enableMfa` (`bool`) — Whether MFA should be enabled for the account.
- `roleChoice` (`string`) — Role selected on the register form.

#### Line-by-line (this function)

```csharp
 331 |         public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")
 332 |         {
 333 |             return StartRegistration(HttpContext.Current, name, email, password, roleChoice);
 334 |         }
```

**Line notes** (what code + variables mean)

- **L333:** Pending registration in Session until MFA confirmed.

---

### `LoginPassword` — lines 339–430

```csharp
public static AuthResult LoginPassword(string email, string password)
```

#### Explanation

- **Purpose:** Implements `LoginPassword`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `password` (`string`) — Plain password from the form (never log this).
- **Local variables (what each means):**
- `ctx` (`var`) — Current HTTP request context (Request, Response, Session).
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `stored` (`string`) — Holds “stored” for this scope. (text)
- `newHash` (`string`) — Cryptographic hash string. (text)  Assigned from password hash function.
- `adminToken` (`string`) — Security token (JWT or CSRF). (text)

#### Line-by-line (this function)

```csharp
 339 |         public static AuthResult LoginPassword(string email, string password)
 340 |         {
 341 |             AuthSchema.Ensure();
 342 |             email = (email ?? "").Trim().ToLowerInvariant();
 343 |             password = password ?? "";
 344 |             var ctx = HttpContext.Current;
 345 | 
 346 |             if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
 347 |                 return Fail("Email and password are required.");
 348 | 
 349 |             string lockMsg;
 350 |             if (LoginThrottle.IsLocked(email, ctx, out lockMsg))
 351 |                 return Fail(lockMsg);
 352 | 
 353 |             using (var conn = DbHelper.OpenConnection())
 354 |             {
 355 |                 AuthUser user = LoadUserByEmail(conn, email);
 356 |                 if (user == null)
 357 |                 {
 358 |                     LoginThrottle.RegisterFailure(email, ctx);
 359 |                     SecurityAudit.Log("login.fail", null, "Unknown email", email);
 360 |                     return Fail("Invalid email or password.");
 361 |                 }
 362 | 
 363 |                 string stored = !string.IsNullOrEmpty(user.PasswordHash)
 364 |                     ? user.PasswordHash
 365 |                     : user.PasswordStored;
 366 | 
 367 |                 if (!PasswordHasher.Verify(password, stored))
 368 |                 {
 369 |                     LoginThrottle.RegisterFailure(email, ctx);
 370 |                     SecurityAudit.Log("login.fail", user.UID, "Bad password", email);
 371 |                     return Fail("Invalid email or password.");
 372 |                 }
 373 | 
 374 |                 LoginThrottle.RegisterSuccess(email, ctx);
 375 | 
 376 |                 // Upgrade plain-text → hash on successful login
 377 |                 if (!PasswordHasher.IsHashed(stored))
 378 |                 {
 379 |                     string newHash = PasswordHasher.Hash(password);
 380 |                     try
 381 |                     {
 382 |                         Exec(conn, "UPDATE Users SET Password=@P, PasswordHash=@H WHERE UID=@UID",
 383 |                         P("@P", newHash), P("@H", newHash), P("@UID", user.UID));
 384 |                     }
 385 |                     catch
 386 |                     {
 387 |                         try
 388 |                         {
 389 |                             Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",
 390 |                             P("@P", newHash), P("@UID", user.UID));
 391 |                         }
 392 |                         catch { }
 393 |                     }
 394 |                 }
 395 | 
 396 |                 user.RoleNormalized = NormalizeRole(user.Role);
 397 | 
 398 |                 // Admin: password only (no MFA). Student/Lecturer still require authenticator.
 399 |                 if (string.Equals(user.RoleNormalized, "Admin", StringComparison.OrdinalIgnoreCase))
 400 |                 {
 401 |                     string adminToken = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);
 402 |                     SecurityAudit.Log("login.ok", user.UID, "Admin MFA bypass", email);
 403 |                     return new AuthResult
 404 |                     {
 405 |                         Success = true,
 406 |                         RequiresMfa = false,
 407 |                         Message = "Signed in as Admin.",
 408 |                         User = user,
 409 |                         Token = adminToken
 410 |                     };
 411 |                 }
 412 | 
 413 |                 // Student / Lecturer: MFA required
 414 |                 if (string.IsNullOrEmpty(user.MfaSecret))
 415 |                 {
 416 |                     return Fail(
 417 |                         "This account has no authenticator set up. Register a new account with MFA, " +
 418 |                         "or ask an admin to reset MFA for you.");
 419 |                 }
 420 | 
 421 |                 return new AuthResult
 422 |                 {
 423 |                     Success = true,
 424 |                     RequiresMfa = true,
 425 |                     MfaMethod = "totp",
 426 |                     Message = "Enter the 6-digit code from your authenticator app.",
 427 |                     User = user
 428 |                 };
 429 |             }
 430 |         }
```

**Line notes** (what code + variables mean)

- **L344:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L350:** Brute-force lockout tracking.
- **L353:** Import namespace/types.
- **L355:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L358:** Brute-force lockout tracking.
- **L359:** Write/read security audit events.
- **L363:** `stored` means: Holds “stored” for this scope. (text)
- **L367:** Password hashing (PBKDF2).
- **L369:** Brute-force lockout tracking.
- **L370:** Write/read security audit events.
- **L374:** Brute-force lockout tracking.
- **L377:** Password hashing (PBKDF2).
- **L379:** Password hashing (PBKDF2). | `newHash` means: Cryptographic hash string. (text)  Assigned from password hash function.
- **L380:** Error handling block.
- **L383:** Parameterized SQL — prevents classic SQL injection.
- **L385:** Handle/log exception.
- **L387:** Error handling block.
- **L390:** Parameterized SQL — prevents classic SQL injection.
- **L392:** Handle/log exception.
- **L396:** Map role codes/names to Admin/Student/Lecturer.
- **L401:** JWT cookie create/validate/clear. | `adminToken` means: Security token (JWT or CSRF). (text)
- **L402:** Write/read security audit events.

---

### `VerifyMfa` — lines 431–500

```csharp
public static AuthResult VerifyMfa(int uid, string code, string method)
```

#### Explanation

- **Purpose:** Implements `VerifyMfa`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- `code` (`string`) — 6-digit TOTP / OTP the user typed.
- `method` (`string`) — HTTP method (GET/POST) or MFA method (totp/email).
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `ok` (`bool`) — Boolean success flag.
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- `r` (`var`) — Usually one database row (DataRow) in query loops.
- `exp` (`DateTime?`) — Expiry DateTime.
- `secret` (`string`) — MFA TOTP Base32 secret for authenticator apps.
- `token` (`string`) — JWT or CSRF token string.

#### Line-by-line (this function)

```csharp
 431 | 
 432 |         public static AuthResult VerifyMfa(int uid, string code, string method)
 433 |         {
 434 |             AuthSchema.Ensure();
 435 |             code = (code ?? "").Trim();
 436 |             if (uid <= 0 || string.IsNullOrEmpty(code))
 437 |             return Fail("Verification code is required.");
 438 | 
 439 |             using (var conn = DbHelper.OpenConnection())
 440 |             {
 441 |                 AuthUser user = LoadUserById(conn, uid);
 442 |                 if (user == null) return Fail("Session expired. Sign in again.");
 443 | 
 444 |                 bool ok = false;
 445 |                 if (string.Equals(method, "email", StringComparison.OrdinalIgnoreCase))
 446 |                 {
 447 |                     try
 448 |                     {
 449 |                         using (var cmd = new SqlCommand(
 450 |                         "SELECT EmailOtp, EmailOtpExpiry FROM Users WHERE UID=@UID", conn))
 451 |                         {
 452 |                             cmd.Parameters.AddWithValue("@UID", uid);
 453 |                             using (var r = cmd.ExecuteReader())
 454 |                             {
 455 |                                 if (r.Read())
 456 |                                 {
 457 |                                     string otp = r["EmailOtp"] == DBNull.Value ? null : r["EmailOtp"].ToString();
 458 |                                     DateTime? exp = r["EmailOtpExpiry"] == DBNull.Value
 459 |                                     ? (DateTime?)null
 460 |                                     : Convert.ToDateTime(r["EmailOtpExpiry"]);
 461 |                                     ok = otp != null && exp.HasValue && exp.Value > DateTime.UtcNow
 462 |                                     && string.Equals(otp, code, StringComparison.Ordinal);
 463 |                                 }
 464 |                             }
 465 |                         }
 466 |                         if (ok)
 467 |                         {
 468 |                             Exec(conn, "UPDATE Users SET EmailOtp=NULL, EmailOtpExpiry=NULL WHERE UID=@UID",
 469 |                             P("@UID", uid));
 470 |                         }
 471 |                     }
 472 |                     catch { ok = false; }
 473 |                 }
 474 |                 else
 475 |                 {
 476 |                     // TOTP (Google Authenticator) — same helper + window as password reset
 477 |                     string secret = TotpHelper.NormalizeSecret(user.MfaSecret);
 478 |                     if (string.IsNullOrEmpty(secret))
 479 |                         return Fail("MFA is not configured for this account. Register again with MFA, or contact admin.");
 480 |                     ok = TotpHelper.VerifyCode(secret, code);
 481 |                 }
 482 | 
 483 |                 if (!ok)
 484 |                 {
 485 |                     LoginThrottle.RegisterFailure(user.Email, HttpContext.Current);
 486 |                     return Fail("Invalid or expired verification code. Use the latest 6-digit code from the app (codes refresh every 30 seconds). Check that your phone time is set automatically.");
 487 |                 }
 488 | 
 489 |                 LoginThrottle.RegisterSuccess(user.Email, HttpContext.Current);
 490 |                 user.RoleNormalized = NormalizeRole(user.Role);
 491 |                 string token = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);
 492 |                 return new AuthResult
 493 |                 {
 494 |                     Success = true,
 495 |                     User = user,
 496 |                     Token = token,
 497 |                     Message = "OK"
 498 |                 };
 499 |             }
 500 |         }
```

**Line notes** (what code + variables mean)

- **L432:** Verify multi-factor / TOTP code.
- **L439:** Import namespace/types.
- **L441:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L444:** `ok` means: Boolean success flag.
- **L447:** Error handling block.
- **L449:** Import namespace/types.
- **L452:** Parameterized SQL — prevents classic SQL injection.
- **L453:** Import namespace/types.
- **L457:** Null-safe read from database values. | `otp` means: Holds “otp” for this scope. (text)
- **L458:** Null-safe read from database values. | `exp` means: Expiry DateTime.
- **L469:** Parameterized SQL — prevents classic SQL injection.
- **L472:** Handle/log exception.
- **L477:** TOTP / authenticator (RFC 6238) helper. | `secret` means: MFA TOTP Base32 secret for authenticator apps.
- **L480:** TOTP / authenticator (RFC 6238) helper.
- **L485:** Brute-force lockout tracking.
- **L489:** Brute-force lockout tracking.
- **L490:** Map role codes/names to Admin/Student/Lecturer.
- **L491:** JWT cookie create/validate/clear. | `token` means: JWT or CSRF token string.

---

### `CompleteLogin` — lines 501–513

```csharp
public static void CompleteLogin(HttpContext ctx, AuthUser user, string token)
```

#### Explanation

- **Purpose:** Implements `CompleteLogin`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- `user` (`AuthUser`) — AuthUser or user row (UID, Email, Role, MfaSecret, …).
- `token` (`string`) — JWT or CSRF token string.

#### Line-by-line (this function)

```csharp
 501 | 
 502 |         public static void CompleteLogin(HttpContext ctx, AuthUser user, string token)
 503 |         {
 504 |             if (ctx == null || user == null) return;
 505 |             // Always store as int so Course.LecturerUID FK gets a real UID
 506 |             ctx.Session["UserID"] = user.UID;
 507 |             ctx.Session["UserName"] = user.Name ?? "";
 508 |             ctx.Session["UserRole"] = user.RoleNormalized ?? NormalizeRole(user.Role);
 509 |             ctx.Session["AuthToken"] = token;
 510 |             JwtHelper.SetAuthCookie(ctx.Response, token);
 511 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
 512 |             SecurityAudit.Log("login.ok", user.UID, "Role=" + (user.RoleNormalized ?? NormalizeRole(user.Role)), user.Email);
 513 |         }
```

**Line notes** (what code + variables mean)

- **L502:** Issue Session + JWT after successful auth.
- **L506:** Server session for logged-in user.
- **L507:** Server session for logged-in user.
- **L508:** Server session for logged-in user.
- **L509:** Server session for logged-in user.
- **L510:** JWT cookie create/validate/clear.
- **L511:** CSRF anti-forgery protection.
- **L512:** Map role codes/names to Admin/Student/Lecturer.

---

### `Logout` — lines 514–535

```csharp
public static void Logout(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `Logout`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- **Local variables (what each means):**
- `email` (`string`) — Account email address (usually lowercased).

#### Line-by-line (this function)

```csharp
 514 | 
 515 |         public static void Logout(HttpContext ctx)
 516 |         {
 517 |             if (ctx == null) return;
 518 |             int? uid = null;
 519 |             string email = null;
 520 |             try
 521 |             {
 522 |                 if (ctx.Session != null && ctx.Session["UserID"] != null)
 523 |                     uid = Convert.ToInt32(ctx.Session["UserID"]);
 524 |                 email = ctx.Session != null ? ctx.Session["UserName"] as string : null;
 525 |             }
 526 |             catch { }
 527 |             SecurityAudit.Log("logout", uid, null, email);
 528 |             try
 529 |             {
 530 |                 ctx.Session.Clear();
 531 |                 ctx.Session.Abandon();
 532 |             }
 533 |             catch { }
 534 |             JwtHelper.ClearAuthCookie(ctx.Response);
 535 |         }
```

**Line notes** (what code + variables mean)

- **L519:** `email` means: Account email address (usually lowercased).
- **L520:** Error handling block.
- **L522:** Server session for logged-in user.
- **L523:** Server session for logged-in user.
- **L524:** Server session for logged-in user.
- **L526:** Handle/log exception.
- **L527:** Write/read security audit events.
- **L528:** Error handling block.
- **L533:** Handle/log exception.
- **L534:** JWT cookie create/validate/clear.

---

### `VerifyMfaForPasswordReset` — lines 541–630

```csharp
public static AuthResult VerifyMfaForPasswordReset(string email, string totpCode)
```

#### Explanation

- **Purpose:** Implements `VerifyMfaForPasswordReset`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `totpCode` (`string`) — User-entered 6-digit authenticator code.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `bad` (`string`) — Holds “bad” for this scope. (text)  Literal text string.
- `secret` (`string`) — MFA TOTP Base32 secret for authenticator apps.
- `msg` (`string`) — Human-readable message (error or success).  Literal text string.
- `expected` (`string`) — Holds “expected” for this scope. (text)  TOTP related value.
- `you` (`string`) — Holds “you” for this scope. (text)

#### Line-by-line (this function)

```csharp
 541 |         public static AuthResult VerifyMfaForPasswordReset(string email, string totpCode)
 542 |         {
 543 |             AuthSchema.Ensure();
 544 |             email = (email ?? "").Trim().ToLowerInvariant();
 545 |             totpCode = (totpCode ?? "").Trim();
 546 | 
 547 |             if (string.IsNullOrEmpty(email) || !email.Contains("@"))
 548 |                 return Fail("Enter a valid email address.");
 549 |             if (string.IsNullOrEmpty(totpCode))
 550 |                 return Fail("Enter the 6-digit code from your authenticator app.");
 551 | 
 552 |             string lockMsg;
 553 |             if (LoginThrottle.IsLocked(email, HttpContext.Current, out lockMsg))
 554 |                 return Fail(lockMsg);
 555 | 
 556 |             using (var conn = DbHelper.OpenConnection())
 557 |             {
 558 |                 AuthUser user = LoadUserByEmail(conn, email);
 559 |                 string bad = "Invalid email or authenticator code.";
 560 |                 if (user == null)
 561 |                 {
 562 |                     LoginThrottle.RegisterFailure(email, HttpContext.Current);
 563 |                     SecurityAudit.Log("password.reset.fail", null, "Unknown email", email);
 564 |                     return Fail(bad);
 565 |                 }
 566 | 
 567 |                 string secret = TotpHelper.NormalizeSecret(user.MfaSecret);
 568 |                 if (string.IsNullOrEmpty(secret))
 569 |                 {
 570 |                     SecurityAudit.Log("password.reset.fail", user.UID, "No MFA secret", email);
 571 |                     return Fail(
 572 |                         "This account has no authenticator linked. Register a new account (MFA required) or contact an admin.");
 573 |                 }
 574 | 
 575 |                 // Same algorithm + window as login MFA (TotpHelper default ±2 min)
 576 |                 if (!TotpHelper.VerifyCode(secret, totpCode))
 577 |                 {
 578 |                     LoginThrottle.RegisterFailure(email, HttpContext.Current);
 579 |                     SecurityAudit.Log("password.reset.fail", user.UID, "Bad TOTP", email);
 580 | 
 581 |                     string msg =
 582 |                         "Invalid authenticator code for this account. " +
 583 |                         "Login and password-reset use the same secret from the database. ";
 584 | 
 585 |                     // When debug is on, show what the SERVER secret expects right now so you can
 586 |                     // compare with Google Authenticator (mismatch = wrong/old QR entry or DB reset).
 587 |                     if (IsMfaDebugEnabled())
 588 |                     {
 589 |                         try
 590 |                         {
 591 |                             string expected = TotpHelper.GenerateCode(secret);
 592 |                             string you = TotpHelper.NormalizeCode(totpCode);
 593 |                             msg +=
 594 |                                 "<br/><br/><strong>Debug (local only)</strong><br/>" +
 595 |                                 "Server expects right now: <strong style=\"letter-spacing:.2em\">" + expected + "</strong><br/>" +
 596 |                                 "You entered: <strong style=\"letter-spacing:.2em\">" +
 597 |                                 System.Web.HttpUtility.HtmlEncode(you) + "</strong><br/>" +
 598 |                                 "Secret length in DB: " + secret.Length +
 599 |                                 " (fingerprint " + secret.Substring(0, Math.Min(4, secret.Length)) + "…" +
 600 |                                 secret.Substring(Math.Max(0, secret.Length - 4)) + ")<br/>" +
 601 |                                 "If the numbers differ, your app entry is for a <em>different</em> secret " +
 602 |                                 "(old QR / re-registered account / DB reseed). Delete the EduLMS row in " +
 603 |                                 "Authenticator and register again, scanning the new QR.";
 604 |                         }
 605 |                         catch
 606 |                         {
 607 |                             msg += " (Could not generate debug code — secret may be corrupt.)";
 608 |                         }
 609 |                     }
 610 |                     else
 611 |                     {
 612 |                         msg +=
 613 |                             "If your app code never matches: delete the old EduLMS entry in Google Authenticator, " +
 614 |                             "register a new account, and scan the new QR. Phone time must be set to automatic.";
 615 |                     }
 616 | 
 617 |                     return Fail(msg);
 618 |                 }
 619 | 
 620 |                 LoginThrottle.RegisterSuccess(email, HttpContext.Current);
 621 |                 SecurityAudit.Log("password.reset.mfa_ok", user.UID, "MFA verified for reset", email);
 622 |                 user.RoleNormalized = NormalizeRole(user.Role);
 623 |                 return new AuthResult
 624 |                 {
 625 |                     Success = true,
 626 |                     Message = "Authenticator verified. Choose a new password.",
 627 |                     User = user
 628 |                 };
 629 |             }
 630 |         }
```

**Line notes** (what code + variables mean)

- **L541:** Verify multi-factor / TOTP code.
- **L553:** Brute-force lockout tracking.
- **L556:** Import namespace/types.
- **L558:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L559:** `bad` means: Holds “bad” for this scope. (text)  Literal text string.
- **L562:** Brute-force lockout tracking.
- **L563:** Write/read security audit events.
- **L567:** TOTP / authenticator (RFC 6238) helper. | `secret` means: MFA TOTP Base32 secret for authenticator apps.
- **L570:** Write/read security audit events.
- **L576:** TOTP / authenticator (RFC 6238) helper.
- **L578:** Brute-force lockout tracking.
- **L579:** Write/read security audit events.
- **L587:** Debug-only TOTP leak switch (must stay false for demos).
- **L589:** Error handling block.
- **L591:** TOTP / authenticator (RFC 6238) helper. | `expected` means: Holds “expected” for this scope. (text)  TOTP related value.
- **L592:** TOTP / authenticator (RFC 6238) helper. | `you` means: Holds “you” for this scope. (text)
- **L597:** Encode text to reduce XSS risk.
- **L605:** Handle/log exception.
- **L620:** Brute-force lockout tracking.
- **L621:** Write/read security audit events.
- **L622:** Map role codes/names to Admin/Student/Lecturer.

---

### `CompletePasswordReset` — lines 635–679

```csharp
public static AuthResult CompletePasswordReset(int uid, string newPassword)
```

#### Explanation

- **Purpose:** Implements `CompletePasswordReset`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- `newPassword` (`string`) — Password (plain input — hash before storing). (text)
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `newHash` (`string`) — Cryptographic hash string. (text)  Assigned from password hash function.

#### Line-by-line (this function)

```csharp
 635 |         public static AuthResult CompletePasswordReset(int uid, string newPassword)
 636 |         {
 637 |             AuthSchema.Ensure();
 638 |             newPassword = newPassword ?? "";
 639 |             if (uid <= 0) return Fail("Session expired. Verify MFA again.");
 640 |             if (newPassword.Length < 8) return Fail("Password must be at least 8 characters.");
 641 |             if (!HasComplexity(newPassword)) return Fail("Password needs letters and numbers.");
 642 | 
 643 |             using (var conn = DbHelper.OpenConnection())
 644 |             {
 645 |                 AuthUser user = LoadUserById(conn, uid);
 646 |                 if (user == null) return Fail("Account not found. Start again.");
 647 | 
 648 |                 string newHash = PasswordHasher.Hash(newPassword);
 649 |                 try
 650 |                 {
 651 |                     Exec(conn, @"
 652 | UPDATE Users SET Password=@P, PasswordHash=@H, PasswordResetToken=NULL, PasswordResetExpiry=NULL
 653 | WHERE UID=@UID",
 654 |                         P("@P", newHash), P("@H", newHash), P("@UID", uid));
 655 |                 }
 656 |                 catch
 657 |                 {
 658 |                     try
 659 |                     {
 660 |                         Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",
 661 |                             P("@P", newHash), P("@UID", uid));
 662 |                     }
 663 |                     catch
 664 |                     {
 665 |                         return Fail("Could not update password.");
 666 |                     }
 667 |                 }
 668 | 
 669 |                 try { Exec(conn, "UPDATE Users SET MfaEnabled=1 WHERE UID=@UID", P("@UID", uid)); }
 670 |                 catch { }
 671 | 
 672 |                 SecurityAudit.Log("password.reset.ok", uid, "after MFA step", user.Email);
 673 |                 return new AuthResult
 674 |                 {
 675 |                     Success = true,
 676 |                     Message = "Password updated. Sign in with your new password and authenticator code."
 677 |                 };
 678 |             }
 679 |         }
```

**Line notes** (what code + variables mean)

- **L635:** Password-reset MFA then update password hash.
- **L643:** Import namespace/types.
- **L645:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L648:** Password hashing (PBKDF2). | `newHash` means: Cryptographic hash string. (text)  Assigned from password hash function.
- **L649:** Error handling block.
- **L654:** Parameterized SQL — prevents classic SQL injection.
- **L656:** Handle/log exception.
- **L658:** Error handling block.
- **L661:** Parameterized SQL — prevents classic SQL injection.
- **L663:** Handle/log exception.
- **L669:** Parameterized SQL — prevents classic SQL injection.
- **L670:** Handle/log exception.
- **L672:** Write/read security audit events.

---

### `ResetPasswordWithTotp` — lines 682–687

```csharp
public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)
```

#### Explanation

- **Purpose:** Implements `ResetPasswordWithTotp`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `totpCode` (`string`) — User-entered 6-digit authenticator code.
- `newPassword` (`string`) — Password (plain input — hash before storing). (text)
- **Local variables (what each means):**
- `v` (`var`) — Generic value (version flag in JSON, or loop value).  Assigned from verification boolean/result.

#### Line-by-line (this function)

```csharp
 682 |         public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)
 683 |         {
 684 |             var v = VerifyMfaForPasswordReset(email, totpCode);
 685 |             if (!v.Success || v.User == null) return v;
 686 |             return CompletePasswordReset(v.User.UID, newPassword);
 687 |         }
```

**Line notes** (what code + variables mean)

- **L684:** Verify multi-factor / TOTP code. | `v` means: Generic value (version flag in JSON, or loop value).  Assigned from verification boolean/result.
- **L686:** Password-reset MFA then update password hash.

---

### `ResetPasswordWithCode` — lines 690–693

```csharp
public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)
```

#### Explanation

- **Purpose:** Implements `ResetPasswordWithCode`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- `code` (`string`) — 6-digit TOTP / OTP the user typed.
- `newPassword` (`string`) — Password (plain input — hash before storing). (text)

#### Line-by-line (this function)

```csharp
 690 |         public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)
 691 |         {
 692 |             return ResetPasswordWithTotp(email, code, newPassword);
 693 |         }
```

---

### `RequestPasswordReset` — lines 696–703

```csharp
public static AuthResult RequestPasswordReset(string email)
```

#### Explanation

- **Purpose:** Implements `RequestPasswordReset`.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).

#### Line-by-line (this function)

```csharp
 696 |         public static AuthResult RequestPasswordReset(string email)
 697 |         {
 698 |             return new AuthResult
 699 |             {
 700 |                 Success = true,
 701 |                 Message = "Use your authenticator app code on the reset page (no email is sent)."
 702 |             };
 703 |         }
```

---

### `UserExists` — lines 706–721

```csharp
public static bool UserExists(int uid)
```

#### Explanation

- **Purpose:** Implements `UserExists`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.

#### Line-by-line (this function)

```csharp
 706 |         public static bool UserExists(int uid)
 707 |         {
 708 |             if (uid <= 0) return false;
 709 |             try
 710 |             {
 711 |                 using (var conn = DbHelper.OpenConnection())
 712 |                 {
 713 |                     object o = Scalar(conn, "SELECT COUNT(1) FROM Users WHERE UID = @UID", P("@UID", uid));
 714 |                     return o != null && Convert.ToInt32(o) > 0;
 715 |                 }
 716 |             }
 717 |             catch
 718 |             {
 719 |                 return false;
 720 |             }
 721 |         }
```

**Line notes** (what code + variables mean)

- **L709:** Error handling block.
- **L711:** Import namespace/types.
- **L713:** Parameterized SQL — prevents classic SQL injection. | `o` means: Holds “o” for this scope.
- **L717:** Handle/log exception.

---

### `GetValidatedUserId` — lines 727–752

```csharp
public static int GetValidatedUserId(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `GetValidatedUserId`.
- **Session:** Reads/writes ASP.NET Session.
- **Pattern:** Read/load data for display.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).

#### Line-by-line (this function)

```csharp
 727 |         public static int GetValidatedUserId(HttpContext ctx)
 728 |         {
 729 |             if (ctx == null || ctx.Session == null) return 0;
 730 | 
 731 |             TryRestoreSessionFromJwt(ctx);
 732 | 
 733 |             if (ctx.Session["UserID"] == null) return 0;
 734 |             int uid;
 735 |             try { uid = Convert.ToInt32(ctx.Session["UserID"]); }
 736 |             catch { return 0; }
 737 | 
 738 |             if (uid > 0 && UserExists(uid))
 739 |             return uid;
 740 | 
 741 |             // Stale session/JWT - user not in current EduDB
 742 |             try
 743 |             {
 744 |                 ctx.Session.Remove("UserID");
 745 |                 ctx.Session.Remove("UserName");
 746 |                 ctx.Session.Remove("UserRole");
 747 |                 ctx.Session.Remove("AuthToken");
 748 |             }
 749 |             catch { }
 750 |             JwtHelper.ClearAuthCookie(ctx.Response);
 751 |             return 0;
 752 |         }
```

**Line notes** (what code + variables mean)

- **L727:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L731:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L733:** Server session for logged-in user.
- **L735:** Server session for logged-in user.
- **L736:** Handle/log exception.
- **L742:** Error handling block.
- **L749:** Handle/log exception.
- **L750:** JWT cookie create/validate/clear.

---

### `TryRestoreSessionFromJwt` — lines 755–820

```csharp
public static bool TryRestoreSessionFromJwt(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `TryRestoreSessionFromJwt`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- **Local variables (what each means):**
- `token` (`string`) — JWT or CSRF token string.
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `r` (`var`) — Usually one database row (DataRow) in query loops.

#### Line-by-line (this function)

```csharp
 755 |         public static bool TryRestoreSessionFromJwt(HttpContext ctx)
 756 |         {
 757 |             if (ctx == null || ctx.Session == null) return false;
 758 | 
 759 |             // Existing session: ensure UID still exists in this database
 760 |             if (ctx.Session["UserID"] != null)
 761 |             {
 762 |                 int existing;
 763 |                 try { existing = Convert.ToInt32(ctx.Session["UserID"]); }
 764 |                 catch { existing = 0; }
 765 |                 if (existing > 0 && UserExists(existing))
 766 |                 return true;
 767 |                 // Bad/stale session id - fall through and try cookie, else clear
 768 |                 try
 769 |                 {
 770 |                     ctx.Session.Remove("UserID");
 771 |                     ctx.Session.Remove("UserName");
 772 |                     ctx.Session.Remove("UserRole");
 773 |                 }
 774 |                 catch { }
 775 |             }
 776 | 
 777 |             string token = JwtHelper.ReadToken(ctx.Request);
 778 |             int uid;
 779 |             string name, role;
 780 |             if (!JwtHelper.TryValidate(token, out uid, out name, out role))
 781 |             {
 782 |                 JwtHelper.ClearAuthCookie(ctx.Response);
 783 |                 return false;
 784 |             }
 785 | 
 786 |             // Reject JWT for users that no longer exist (MDF replaced / reseeded)
 787 |             if (!UserExists(uid))
 788 |             {
 789 |                 JwtHelper.ClearAuthCookie(ctx.Response);
 790 |                 return false;
 791 |             }
 792 | 
 793 |             // Prefer live name/role from DB over token claims
 794 |             try
 795 |             {
 796 |                 using (var conn = DbHelper.OpenConnection())
 797 |                 {
 798 |                     using (var cmd = new SqlCommand(
 799 |                     "SELECT Name, Role FROM Users WHERE UID=@UID", conn))
 800 |                     {
 801 |                         cmd.Parameters.AddWithValue("@UID", uid);
 802 |                         using (var r = cmd.ExecuteReader())
 803 |                         {
 804 |                             if (r.Read())
 805 |                             {
 806 |                                 name = r["Name"] == DBNull.Value ? name : r["Name"].ToString();
 807 |                                 role = NormalizeRole(r["Role"] == DBNull.Value ? role : r["Role"].ToString());
 808 |                             }
 809 |                         }
 810 |                     }
 811 |                 }
 812 |             }
 813 |             catch { /* keep token claims */ }
 814 | 
 815 |             ctx.Session["UserID"] = uid;
 816 |             ctx.Session["UserName"] = name ?? "";
 817 |             ctx.Session["UserRole"] = role ?? "Student";
 818 |             ctx.Session["AuthToken"] = token;
 819 |             return true;
 820 |         }
```

**Line notes** (what code + variables mean)

- **L755:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L760:** Server session for logged-in user.
- **L763:** Server session for logged-in user.
- **L764:** Handle/log exception.
- **L768:** Error handling block.
- **L774:** Handle/log exception.
- **L777:** JWT cookie create/validate/clear. | `token` means: JWT or CSRF token string.
- **L780:** JWT cookie create/validate/clear.
- **L782:** JWT cookie create/validate/clear.
- **L789:** JWT cookie create/validate/clear.
- **L794:** Error handling block.
- **L796:** Import namespace/types.
- **L798:** Import namespace/types.
- **L801:** Parameterized SQL — prevents classic SQL injection.
- **L802:** Import namespace/types.
- **L806:** Null-safe read from database values.
- **L807:** Null-safe read from database values.
- **L813:** Handle/log exception.
- **L815:** Server session for logged-in user.
- **L816:** Server session for logged-in user.
- **L817:** Server session for logged-in user.
- **L818:** Server session for logged-in user.

---

### `NormalizeRole` — lines 821–829

```csharp
public static string NormalizeRole(string role)
```

#### Explanation

- **Purpose:** Implements `NormalizeRole`.
- **Parameters (what each means):**
- `role` (`string`) — User role code or name (Admin/Student/Lecturer).
- **Local variables (what each means):**
- `r` (`var`) — Usually one database row (DataRow) in query loops.

#### Line-by-line (this function)

```csharp
 821 | 
 822 |         public static string NormalizeRole(string role)
 823 |         {
 824 |             if (string.IsNullOrWhiteSpace(role)) return "Student";
 825 |             var r = role.Trim().ToLowerInvariant();
 826 |             if (r == "0" || r == "admin" || r == "administrator") return "Admin";
 827 |             if (r == "2" || r == "teacher" || r == "lecturer") return "Lecturer";
 828 |             return "Student";
 829 |         }
```

**Line notes** (what code + variables mean)

- **L822:** Map role codes/names to Admin/Student/Lecturer.
- **L825:** `r` means: Usually one database row (DataRow) in query loops.

---

### `HasComplexity` — lines 830–840

```csharp
private static bool HasComplexity(string password)
```

#### Explanation

- **Purpose:** Implements `HasComplexity`.
- **Parameters (what each means):**
- `password` (`string`) — Plain password from the form (never log this).
- **Local variables (what each means):**
- `letter` (`bool`) — Holds “letter” for this scope. (true/false)
- `c` — Temporary value (character, course, or counter depending on loop).

#### Line-by-line (this function)

```csharp
 830 | 
 831 |         private static bool HasComplexity(string password)
 832 |         {
 833 |             bool letter = false, digit = false;
 834 |             foreach (char c in password)
 835 |             {
 836 |                 if (char.IsLetter(c)) letter = true;
 837 |                 if (char.IsDigit(c)) digit = true;
 838 |             }
 839 |             return letter && digit;
 840 |         }
```

**Line notes** (what code + variables mean)

- **L833:** `letter` means: Holds “letter” for this scope. (true/false)

---

### `LoadUserByEmail` — lines 841–880

```csharp
private static AuthUser LoadUserByEmail(SqlConnection conn, string email)
```

#### Explanation

- **Purpose:** Implements `LoadUserByEmail`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `email` (`string`) — Account email address (usually lowercased).
- **Local variables (what each means):**
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- `r` (`var`) — Usually one database row (DataRow) in query loops.

#### Line-by-line (this function)

```csharp
 841 | 
 842 |         private static AuthUser LoadUserByEmail(SqlConnection conn, string email)
 843 |         {
 844 |             // Prefer extended columns; fall back
 845 |             try
 846 |             {
 847 |                 using (var cmd = new SqlCommand(@"
 848 |                 SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret
 849 |                 FROM Users WHERE Email = @Email", conn))
 850 |                 {
 851 |                     cmd.Parameters.AddWithValue("@Email", email);
 852 |                     using (var r = cmd.ExecuteReader())
 853 |                     {
 854 |                         if (!r.Read()) return null;
 855 |                         return MapUser(r);
 856 |                     }
 857 |                 }
 858 |             }
 859 |             catch
 860 |             {
 861 |                 using (var cmd = new SqlCommand(@"
 862 |                 SELECT UID, Name, Email, Role, Password FROM Users WHERE Email = @Email", conn))
 863 |                 {
 864 |                     cmd.Parameters.AddWithValue("@Email", email);
 865 |                     using (var r = cmd.ExecuteReader())
 866 |                     {
 867 |                         if (!r.Read()) return null;
 868 |                         return new AuthUser
 869 |                         {
 870 |                             UID = Convert.ToInt32(r["UID"]),
 871 |                             Name = r["Name"] == DBNull.Value ? "" : r["Name"].ToString(),
 872 |                             Email = r["Email"] == DBNull.Value ? "" : r["Email"].ToString(),
 873 |                             Role = r["Role"] == DBNull.Value ? "1" : r["Role"].ToString(),
 874 |                             PasswordStored = r["Password"] == DBNull.Value ? "" : r["Password"].ToString(),
 875 |                             MfaEnabled = false
 876 |                         };
 877 |                     }
 878 |                 }
 879 |             }
 880 |         }
```

**Line notes** (what code + variables mean)

- **L842:** Database access (pure SQL).
- **L845:** Error handling block.
- **L847:** Import namespace/types.
- **L851:** Parameterized SQL — prevents classic SQL injection.
- **L852:** Import namespace/types.
- **L859:** Handle/log exception.
- **L861:** Import namespace/types.
- **L864:** Parameterized SQL — prevents classic SQL injection.
- **L865:** Import namespace/types.
- **L871:** Null-safe read from database values.
- **L872:** Null-safe read from database values.
- **L873:** Null-safe read from database values.
- **L874:** Null-safe read from database values.

---

### `LoadUserById` — lines 881–919

```csharp
private static AuthUser LoadUserById(SqlConnection conn, int uid)
```

#### Explanation

- **Purpose:** Implements `LoadUserById`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `uid` (`int`) — User ID (Users.UID) of the logged-in or target user.
- **Local variables (what each means):**
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- `r` (`var`) — Usually one database row (DataRow) in query loops.

#### Line-by-line (this function)

```csharp
 881 | 
 882 |         private static AuthUser LoadUserById(SqlConnection conn, int uid)
 883 |         {
 884 |             try
 885 |             {
 886 |                 using (var cmd = new SqlCommand(@"
 887 |                 SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret
 888 |                 FROM Users WHERE UID = @UID", conn))
 889 |                 {
 890 |                     cmd.Parameters.AddWithValue("@UID", uid);
 891 |                     using (var r = cmd.ExecuteReader())
 892 |                     {
 893 |                         if (!r.Read()) return null;
 894 |                         return MapUser(r);
 895 |                     }
 896 |                 }
 897 |             }
 898 |             catch
 899 |             {
 900 |                 using (var cmd = new SqlCommand(
 901 |                 "SELECT UID, Name, Email, Role, Password FROM Users WHERE UID=@UID", conn))
 902 |                 {
 903 |                     cmd.Parameters.AddWithValue("@UID", uid);
 904 |                     using (var r = cmd.ExecuteReader())
 905 |                     {
 906 |                         if (!r.Read()) return null;
 907 |                         return new AuthUser
 908 |                         {
 909 |                             UID = Convert.ToInt32(r["UID"]),
 910 |                             Name = r["Name"].ToString(),
 911 |                             Email = r["Email"].ToString(),
 912 |                             Role = r["Role"].ToString(),
 913 |                             PasswordStored = r["Password"].ToString(),
 914 |                             MfaEnabled = false
 915 |                         };
 916 |                     }
 917 |                 }
 918 |             }
 919 |         }
```

**Line notes** (what code + variables mean)

- **L882:** Database access (pure SQL).
- **L884:** Error handling block.
- **L886:** Import namespace/types.
- **L890:** Parameterized SQL — prevents classic SQL injection.
- **L891:** Import namespace/types.
- **L898:** Handle/log exception.
- **L900:** Import namespace/types.
- **L903:** Parameterized SQL — prevents classic SQL injection.
- **L904:** Import namespace/types.

---

### `MapUser` — lines 920–947

```csharp
private static AuthUser MapUser(SqlDataReader r)
```

#### Explanation

- **Purpose:** Implements `MapUser`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `r` (`SqlDataReader`) — Usually one database row (DataRow) in query loops.
- **Local variables (what each means):**
- `mfa` (`bool`) — Holds “mfa” for this scope. (true/false)

#### Line-by-line (this function)

```csharp
 920 | 
 921 |         private static AuthUser MapUser(SqlDataReader r)
 922 |         {
 923 |             bool mfa = false;
 924 |             try
 925 |             {
 926 |                 if (HasCol(r, "MfaEnabled") && r["MfaEnabled"] != DBNull.Value)
 927 |                 mfa = Convert.ToBoolean(r["MfaEnabled"]);
 928 |             }
 929 |             catch
 930 |             {
 931 |                 try { mfa = Convert.ToInt32(r["MfaEnabled"]) != 0; } catch { }
 932 |             }
 933 | 
 934 |             return new AuthUser
 935 |             {
 936 |                 UID = Convert.ToInt32(r["UID"]),
 937 |                 Name = Safe(r, "Name"),
 938 |                 Email = Safe(r, "Email"),
 939 |                 Role = Safe(r, "Role"),
 940 |                 PasswordStored = Safe(r, "Password"),
 941 |                 PasswordHash = HasCol(r, "PasswordHash") ? Safe(r, "PasswordHash") : null,
 942 |                 MfaEnabled = mfa,
 943 |                 MfaSecret = HasCol(r, "MfaSecret")
 944 |                 ? TotpHelper.NormalizeSecret(Safe(r, "MfaSecret"))
 945 |                 : null
 946 |             };
 947 |         }
```

**Line notes** (what code + variables mean)

- **L923:** `mfa` means: Holds “mfa” for this scope. (true/false)
- **L924:** Error handling block.
- **L926:** Null-safe read from database values.
- **L929:** Handle/log exception.
- **L931:** Error handling block.
- **L944:** TOTP / authenticator (RFC 6238) helper.

---

### `HasCol` — lines 948–955

```csharp
private static bool HasCol(SqlDataReader r, string name)
```

#### Explanation

- **Purpose:** Implements `HasCol`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `r` (`SqlDataReader`) — Usually one database row (DataRow) in query loops.
- `name` (`string`) — Display name of user/course/criterion.
- **Local variables (what each means):**
- `i` (`int`) — Loop index (0-based counter in for-loops).  Literal number `0`.

#### Line-by-line (this function)

```csharp
 948 | 
 949 |         private static bool HasCol(SqlDataReader r, string name)
 950 |         {
 951 |             for (int i = 0; i < r.FieldCount; i++)
 952 |             if (string.Equals(r.GetName(i), name, StringComparison.OrdinalIgnoreCase))
 953 |             return true;
 954 |             return false;
 955 |         }
```

---

### `Safe` — lines 956–965

```csharp
private static string Safe(SqlDataReader r, string col)
```

#### Explanation

- **Purpose:** Implements `Safe`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `r` (`SqlDataReader`) — Usually one database row (DataRow) in query loops.
- `col` (`string`) — Holds “col” for this scope. (text)
- **Local variables (what each means):**
- `i` (`int`) — Loop index (0-based counter in for-loops).

#### Line-by-line (this function)

```csharp
 956 | 
 957 |         private static string Safe(SqlDataReader r, string col)
 958 |         {
 959 |             try
 960 |             {
 961 |                 int i = r.GetOrdinal(col);
 962 |                 return r.IsDBNull(i) ? "" : r.GetValue(i).ToString();
 963 |             }
 964 |             catch { return ""; }
 965 |         }
```

**Line notes** (what code + variables mean)

- **L959:** Error handling block.
- **L961:** `i` means: Loop index (0-based counter in for-loops).
- **L962:** Null-safe read from database values.
- **L964:** Handle/log exception.

---

### `Fail` — lines 966–970

```csharp
private static AuthResult Fail(string msg)
```

#### Explanation

- **Purpose:** Implements `Fail`.
- **Parameters (what each means):**
- `msg` (`string`) — Human-readable message (error or success).

#### Line-by-line (this function)

```csharp
 966 | 
 967 |         private static AuthResult Fail(string msg)
 968 |         {
 969 |             return new AuthResult { Success = false, Message = msg };
 970 |         }
```

---

### `IsMfaDebugEnabled` — lines 976–984

```csharp
private static bool IsMfaDebugEnabled()
```

#### Explanation

- **Purpose:** Implements `IsMfaDebugEnabled`.
- **Local variables (what each means):**
- `flag` (`string`) — Holds “flag” for this scope. (text)  Read from Web.config.

#### Line-by-line (this function)

```csharp
 976 |         private static bool IsMfaDebugEnabled()
 977 |         {
 978 |             try
 979 |             {
 980 |                 string flag = System.Configuration.ConfigurationManager.AppSettings["MfaDebug"];
 981 |                 return string.Equals(flag, "true", StringComparison.OrdinalIgnoreCase);
 982 |             }
 983 |             catch { return false; }
 984 |         }
```

**Line notes** (what code + variables mean)

- **L976:** Debug-only TOTP leak switch (must stay false for demos).
- **L978:** Error handling block.
- **L980:** Debug-only TOTP leak switch (must stay false for demos). | `flag` means: Holds “flag” for this scope. (text)  Read from Web.config.
- **L983:** Handle/log exception.

---

### `GetStoredMfaSecretByEmail` — lines 989–1002

```csharp
public static string GetStoredMfaSecretByEmail(string email)
```

#### Explanation

- **Purpose:** Implements `GetStoredMfaSecretByEmail`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters (what each means):**
- `email` (`string`) — Account email address (usually lowercased).
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.

#### Line-by-line (this function)

```csharp
 989 |         public static string GetStoredMfaSecretByEmail(string email)
 990 |         {
 991 |             email = (email ?? "").Trim().ToLowerInvariant();
 992 |             if (string.IsNullOrEmpty(email)) return null;
 993 |             try
 994 |             {
 995 |                 using (var conn = DbHelper.OpenConnection())
 996 |                 {
 997 |                     AuthUser u = LoadUserByEmail(conn, email);
 998 |                     return u == null ? null : TotpHelper.NormalizeSecret(u.MfaSecret);
 999 |                 }
1000 |             }
1001 |             catch { return null; }
1002 |         }
```

**Line notes** (what code + variables mean)

- **L993:** Error handling block.
- **L995:** Import namespace/types.
- **L997:** `u` means: Holds “u” for this scope. (user DTO)
- **L998:** TOTP / authenticator (RFC 6238) helper.
- **L1001:** Handle/log exception.

---

### `P` — lines 1003–1007

```csharp
private static SqlParameter P(string n, object v)
```

#### Explanation

- **Purpose:** Implements `P`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `n` (`string`) — Numeric count or temporary integer.
- `v` (`object`) — Generic value (version flag in JSON, or loop value).

#### Line-by-line (this function)

```csharp
1003 | 
1004 |         private static SqlParameter P(string n, object v)
1005 |         {
1006 |             return new SqlParameter(n, v ?? DBNull.Value);
1007 |         }
```

**Line notes** (what code + variables mean)

- **L1004:** Parameterized SQL — prevents classic SQL injection.
- **L1006:** Parameterized SQL — prevents classic SQL injection.

---

### `Scalar` — lines 1008–1016

```csharp
private static object Scalar(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `Scalar`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `ps` (`SqlParameter[]`) — Holds “ps” for this scope. (type `SqlParameter[]`)
- **Local variables (what each means):**
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.

#### Line-by-line (this function)

```csharp
1008 | 
1009 |         private static object Scalar(SqlConnection conn, string sql, params SqlParameter[] ps)
1010 |         {
1011 |             using (var cmd = new SqlCommand(sql, conn))
1012 |             {
1013 |                 if (ps != null) cmd.Parameters.AddRange(ps);
1014 |                 return cmd.ExecuteScalar();
1015 |             }
1016 |         }
```

**Line notes** (what code + variables mean)

- **L1009:** Database access (pure SQL).
- **L1011:** Import namespace/types.
- **L1014:** Run SQL; return table / rows / scalar.

---

### `Exec` — lines 1017–1025

```csharp
private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `Exec`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `ps` (`SqlParameter[]`) — Holds “ps” for this scope. (type `SqlParameter[]`)
- **Local variables (what each means):**
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.

#### Line-by-line (this function)

```csharp
1017 | 
1018 |         private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
1019 |         {
1020 |             using (var cmd = new SqlCommand(sql, conn))
1021 |             {
1022 |                 if (ps != null) cmd.Parameters.AddRange(ps);
1023 |                 cmd.ExecuteNonQuery();
1024 |             }
1025 |         }
```

**Line notes** (what code + variables mean)

- **L1018:** Database access (pure SQL).
- **L1020:** Import namespace/types.
- **L1023:** Run SQL; return table / rows / scalar.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```csharp
   1 | using System;
   2 | using System.Data;
   3 | using System.Data.SqlClient;
   4 | using System.Web;
   5 | using WebAppAssignment.Data;
   6 | 
   7 | namespace WebAppAssignment.Data.Security
   8 | {
   9 |     public class AuthUser
  10 |     {
  11 |         public int UID { get; set; }
  12 |         public string Name { get; set; }
  13 |         public string Email { get; set; }
  14 |         public string Role { get; set; }
  15 |         public string RoleNormalized { get; set; }
  16 |         public string PasswordStored { get; set; }
  17 |         public string PasswordHash { get; set; }
  18 |         public bool MfaEnabled { get; set; }
  19 |         public string MfaSecret { get; set; }
  20 |     }
  21 | 
  22 |     public class AuthResult
  23 |     {
  24 |         public bool Success { get; set; }
  25 |         public string Message { get; set; }
  26 |         public bool RequiresMfa { get; set; }
  27 |         public string MfaMethod { get; set; } // "totp" | "email"
  28 |         public string DemoEmailOtp { get; set; } // shown when no email SMTP configured
  29 |         public AuthUser User { get; set; }
  30 |         public string Token { get; set; }
  31 |     }
  32 | 
  33 |     /// <summary>
  34 |     /// Pure-SQL authentication (SqlConnection + parameterized SQL only — no Entity Framework / ORM).
  35 |     /// </summary>
  36 |     public static class AuthService
  37 |     {
  38 |         // Pending registration held as plain Session strings (not a mapped entity). No Users row until MFA OK.
  39 |         private const string SessRegName = "Reg.Name";
  40 |         private const string SessRegEmail = "Reg.Email";
  41 |         private const string SessRegHash = "Reg.PasswordHash";
  42 |         private const string SessRegRole = "Reg.RoleCode";
  43 |         private const string SessRegRoleName = "Reg.RoleNormalized";
  44 |         private const string SessRegSecret = "Reg.MfaSecret";
  45 |         private const string SessRegAt = "Reg.CreatedUtc";
  46 |         private static readonly TimeSpan PendingRegTtl = TimeSpan.FromMinutes(15);
  47 | 
  48 |         /// <summary>
  49 |         /// Step 1 — validate form, ensure email free, generate MFA secret.
  50 |         /// Does NOT insert into Users. Data lives in Session until MFA is confirmed.
  51 |         /// </summary>
  52 |         public static AuthResult StartRegistration(HttpContext ctx, string name, string email, string password, string roleChoice = "Student")
  53 |         {
  54 |             AuthSchema.Ensure();
  55 |             name = (name ?? "").Trim();
  56 |             email = (email ?? "").Trim().ToLowerInvariant();
  57 |             password = password ?? "";
  58 | 
  59 |             if (name.Length < 2) return Fail("Name must be at least 2 characters.");
  60 |             if (!email.Contains("@") || email.Length < 5) return Fail("Enter a valid email address.");
  61 |             if (password.Length < 8) return Fail("Password must be at least 8 characters.");
  62 |             if (!HasComplexity(password)) return Fail("Password needs letters and numbers.");
  63 | 
  64 |             string roleCode;
  65 |             string roleNormalized;
  66 |             string rc = (roleChoice ?? "").Trim().ToLowerInvariant();
  67 |             if (rc == "lecturer" || rc == "teacher" || rc == "2")
  68 |             {
  69 |                 roleCode = "2";
  70 |                 roleNormalized = "Lecturer";
  71 |             }
  72 |             else
  73 |             {
  74 |                 roleCode = "1";
  75 |                 roleNormalized = "Student";
  76 |             }
  77 | 
  78 |             using (var conn = DbHelper.OpenConnection())
  79 |             {
  80 |                 int exists = Convert.ToInt32(Scalar(conn,
  81 |                     "SELECT COUNT(*) FROM Users WHERE Email = @Email",
  82 |                     P("@Email", email)));
  83 |                 if (exists > 0) return Fail("An account with this email already exists.");
  84 |             }
  85 | 
  86 |             string mfaSecret = TotpHelper.GenerateSecret();
  87 |             if (ctx != null && ctx.Session != null)
  88 |             {
  89 |                 ctx.Session[SessRegName] = name;
  90 |                 ctx.Session[SessRegEmail] = email;
  91 |                 ctx.Session[SessRegHash] = PasswordHasher.Hash(password);
  92 |                 ctx.Session[SessRegRole] = roleCode;
  93 |                 ctx.Session[SessRegRoleName] = roleNormalized;
  94 |                 ctx.Session[SessRegSecret] = mfaSecret;
  95 |                 ctx.Session[SessRegAt] = DateTime.UtcNow;
  96 |             }
  97 | 
  98 |             return new AuthResult
  99 |             {
 100 |                 Success = true,
 101 |                 Message = "Scan the QR code and enter the authenticator code to finish creating your account.",
 102 |                 RequiresMfa = true,
 103 |                 User = new AuthUser
 104 |                 {
 105 |                     UID = 0, // not created yet
 106 |                     Name = name,
 107 |                     Email = email,
 108 |                     Role = roleCode,
 109 |                     RoleNormalized = roleNormalized,
 110 |                     MfaEnabled = true,
 111 |                     MfaSecret = mfaSecret
 112 |                 }
 113 |             };
 114 |         }
 115 | 
 116 |         /// <summary>
 117 |         /// Step 2 — verify TOTP against session secret, then pure-SQL INSERT.
 118 |         /// Abandoning before this leaves no account in the database.
 119 |         /// </summary>
 120 |         public static AuthResult FinishRegistration(HttpContext ctx, string totpCode)
 121 |         {
 122 |             AuthSchema.Ensure();
 123 |             totpCode = (totpCode ?? "").Trim();
 124 | 
 125 |             string name, email, hash, roleCode, roleNormalized, secret;
 126 |             DateTime createdUtc;
 127 |             if (!TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out createdUtc))
 128 |                 return Fail("Registration session expired. Start again from the form.");
 129 | 
 130 |             if (DateTime.UtcNow - createdUtc > PendingRegTtl)
 131 |             {
 132 |                 ClearPendingRegistration(ctx);
 133 |                 return Fail("Registration timed out (15 minutes). Please register again.");
 134 |             }
 135 | 
 136 |             if (string.IsNullOrEmpty(totpCode))
 137 |                 return Fail("Enter the 6-digit code from your authenticator app.");
 138 | 
 139 |             secret = TotpHelper.NormalizeSecret(secret);
 140 |             if (string.IsNullOrEmpty(secret))
 141 |             {
 142 |                 ClearPendingRegistration(ctx);
 143 |                 return Fail("MFA setup data missing. Please register again.");
 144 |             }
 145 | 
 146 |             if (!TotpHelper.VerifyCode(secret, totpCode))
 147 |                 return Fail("Invalid authenticator code. Open Google Authenticator and enter the current 6-digit code for EduLMS.");
 148 | 
 149 |             // Re-check email free (someone may have taken it while scanning QR)
 150 |             using (var conn = DbHelper.OpenConnection())
 151 |             {
 152 |                 int exists = Convert.ToInt32(Scalar(conn,
 153 |                     "SELECT COUNT(*) FROM Users WHERE Email = @Email",
 154 |                     P("@Email", email)));
 155 |                 if (exists > 0)
 156 |                 {
 157 |                     ClearPendingRegistration(ctx);
 158 |                     return Fail("An account with this email already exists. Sign in instead.");
 159 |                 }
 160 | 
 161 |                 string mfaSecret = secret;
 162 |                 int mfaOn = 1;
 163 |                 int uid;
 164 | 
 165 |                 try
 166 |                 {
 167 |                     uid = Convert.ToInt32(Scalar(conn, @"
 168 |                     INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaSecret, MfaEnabled, CreatedAt)
 169 |                     OUTPUT INSERTED.UID
 170 |                     VALUES (@Name, @Email, @Password, @Role, @PasswordHash, @MfaSecret, @MfaEnabled, @CreatedAt)",
 171 |                         P("@Name", name),
 172 |                         P("@Email", email),
 173 |                         P("@Password", hash),
 174 |                         P("@Role", roleCode),
 175 |                         P("@PasswordHash", hash),
 176 |                         P("@MfaSecret", (object)mfaSecret ?? DBNull.Value),
 177 |                         P("@MfaEnabled", mfaOn),
 178 |                         P("@CreatedAt", DateTime.UtcNow)));
 179 |                 }
 180 |                 catch
 181 |                 {
 182 |                     try
 183 |                     {
 184 |                         uid = Convert.ToInt32(Scalar(conn, @"
 185 |                         INSERT INTO Users (Name, Email, Password, Role)
 186 |                         OUTPUT INSERTED.UID
 187 |                         VALUES (@Name, @Email, @Password, @Role)",
 188 |                             P("@Name", name),
 189 |                             P("@Email", email),
 190 |                             P("@Password", hash),
 191 |                             P("@Role", roleCode)));
 192 |                     }
 193 |                     catch
 194 |                     {
 195 |                         return Fail("Could not create account. Check the Users table and try again.");
 196 |                     }
 197 |                 }
 198 | 
 199 |                 try
 200 |                 {
 201 |                     object byEmail = Scalar(conn, "SELECT UID FROM Users WHERE Email=@Email", P("@Email", email));
 202 |                     if (byEmail != null && byEmail != DBNull.Value)
 203 |                         uid = Convert.ToInt32(byEmail);
 204 |                 }
 205 |                 catch { }
 206 | 
 207 |                 if (uid <= 0)
 208 |                     return Fail("Account insert did not return a valid user id.");
 209 | 
 210 |                 try
 211 |                 {
 212 |                     Exec(conn, @"
 213 |                     UPDATE Users SET Password=@P, PasswordHash=@H, MfaSecret=@S, MfaEnabled=@E WHERE UID=@UID",
 214 |                         P("@P", hash),
 215 |                         P("@H", hash),
 216 |                         P("@S", (object)mfaSecret ?? DBNull.Value),
 217 |                         P("@E", mfaOn),
 218 |                         P("@UID", uid));
 219 |                 }
 220 |                 catch
 221 |                 {
 222 |                     try
 223 |                     {
 224 |                         Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",
 225 |                             P("@P", hash), P("@UID", uid));
 226 |                     }
 227 |                     catch { }
 228 |                 }
 229 | 
 230 |                 try
 231 |                 {
 232 |                     object stored = Scalar(conn, "SELECT MfaSecret FROM Users WHERE UID=@UID", P("@UID", uid));
 233 |                     string storedSecret = stored == null || stored == DBNull.Value
 234 |                         ? ""
 235 |                         : TotpHelper.NormalizeSecret(stored.ToString());
 236 |                     if (storedSecret != mfaSecret)
 237 |                     {
 238 |                         try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }
 239 |                         return Fail("Account could not save MFA secret. Check Users.MfaSecret column, then register again.");
 240 |                     }
 241 |                 }
 242 |                 catch
 243 |                 {
 244 |                     try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }
 245 |                     return Fail("MFA columns missing. Restart the app so schema can update, then register again.");
 246 |                 }
 247 | 
 248 |                 ClearPendingRegistration(ctx);
 249 |                 SecurityAudit.Log("register.ok", uid, roleNormalized, email);
 250 | 
 251 |                 return new AuthResult
 252 |                 {
 253 |                     Success = true,
 254 |                     Message = "Account created as " + roleNormalized + ". Sign in with your password and authenticator.",
 255 |                     User = new AuthUser
 256 |                     {
 257 |                         UID = uid,
 258 |                         Name = name,
 259 |                         Email = email,
 260 |                         Role = roleCode,
 261 |                         RoleNormalized = roleNormalized,
 262 |                         MfaEnabled = true,
 263 |                         MfaSecret = mfaSecret
 264 |                     }
 265 |                 };
 266 |             }
 267 |         }
 268 | 
 269 |         /// <summary>True if Session still has an unfinished registration (no DB row yet).</summary>
 270 |         public static bool HasPendingRegistration(HttpContext ctx)
 271 |         {
 272 |             string name, email, hash, roleCode, roleNormalized, secret;
 273 |             DateTime at;
 274 |             return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out at);
 275 |         }
 276 | 
 277 |         /// <summary>Email + MFA secret for QR while registration is pending in Session.</summary>
 278 |         public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)
 279 |         {
 280 |             string name, hash, roleCode, roleNormalized;
 281 |             DateTime at;
 282 |             return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out mfaSecret, out at);
 283 |         }
 284 | 
 285 |         public static void ClearPendingRegistration(HttpContext ctx)
 286 |         {
 287 |             try
 288 |             {
 289 |                 if (ctx == null || ctx.Session == null) return;
 290 |                 ctx.Session.Remove(SessRegName);
 291 |                 ctx.Session.Remove(SessRegEmail);
 292 |                 ctx.Session.Remove(SessRegHash);
 293 |                 ctx.Session.Remove(SessRegRole);
 294 |                 ctx.Session.Remove(SessRegRoleName);
 295 |                 ctx.Session.Remove(SessRegSecret);
 296 |                 ctx.Session.Remove(SessRegAt);
 297 |             }
 298 |             catch { }
 299 |         }
 300 | 
 301 |         private static bool TryReadPendingRegistration(
 302 |             HttpContext ctx,
 303 |             out string name, out string email, out string hash,
 304 |             out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc)
 305 |         {
 306 |             name = email = hash = roleCode = roleNormalized = secret = null;
 307 |             createdUtc = DateTime.MinValue;
 308 |             if (ctx == null || ctx.Session == null) return false;
 309 |             try
 310 |             {
 311 |                 name = ctx.Session[SessRegName] as string;
 312 |                 email = ctx.Session[SessRegEmail] as string;
 313 |                 hash = ctx.Session[SessRegHash] as string;
 314 |                 roleCode = ctx.Session[SessRegRole] as string;
 315 |                 roleNormalized = ctx.Session[SessRegRoleName] as string;
 316 |                 secret = ctx.Session[SessRegSecret] as string;
 317 |                 if (ctx.Session[SessRegAt] is DateTime)
 318 |                     createdUtc = (DateTime)ctx.Session[SessRegAt];
 319 |                 else
 320 |                     return false;
 321 | 
 322 |                 if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(email) ||
 323 |                     string.IsNullOrEmpty(hash) || string.IsNullOrEmpty(secret))
 324 |                     return false;
 325 |                 return true;
 326 |             }
 327 |             catch { return false; }
 328 |         }
 329 | 
 330 |         /// <summary>Legacy name — starts pending registration only (no insert until FinishRegistration).</summary>
 331 |         public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")
 332 |         {
 333 |             return StartRegistration(HttpContext.Current, name, email, password, roleChoice);
 334 |         }
 335 | 
 336 |         /// <summary>
 337 |         /// Step 1 of login: password check. If MFA on, does not issue session yet.
 338 |         /// </summary>
 339 |         public static AuthResult LoginPassword(string email, string password)
 340 |         {
 341 |             AuthSchema.Ensure();
 342 |             email = (email ?? "").Trim().ToLowerInvariant();
 343 |             password = password ?? "";
 344 |             var ctx = HttpContext.Current;
 345 | 
 346 |             if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
 347 |                 return Fail("Email and password are required.");
 348 | 
 349 |             string lockMsg;
 350 |             if (LoginThrottle.IsLocked(email, ctx, out lockMsg))
 351 |                 return Fail(lockMsg);
 352 | 
 353 |             using (var conn = DbHelper.OpenConnection())
 354 |             {
 355 |                 AuthUser user = LoadUserByEmail(conn, email);
 356 |                 if (user == null)
 357 |                 {
 358 |                     LoginThrottle.RegisterFailure(email, ctx);
 359 |                     SecurityAudit.Log("login.fail", null, "Unknown email", email);
 360 |                     return Fail("Invalid email or password.");
 361 |                 }
 362 | 
 363 |                 string stored = !string.IsNullOrEmpty(user.PasswordHash)
 364 |                     ? user.PasswordHash
 365 |                     : user.PasswordStored;
 366 | 
 367 |                 if (!PasswordHasher.Verify(password, stored))
 368 |                 {
 369 |                     LoginThrottle.RegisterFailure(email, ctx);
 370 |                     SecurityAudit.Log("login.fail", user.UID, "Bad password", email);
 371 |                     return Fail("Invalid email or password.");
 372 |                 }
 373 | 
 374 |                 LoginThrottle.RegisterSuccess(email, ctx);
 375 | 
 376 |                 // Upgrade plain-text → hash on successful login
 377 |                 if (!PasswordHasher.IsHashed(stored))
 378 |                 {
 379 |                     string newHash = PasswordHasher.Hash(password);
 380 |                     try
 381 |                     {
 382 |                         Exec(conn, "UPDATE Users SET Password=@P, PasswordHash=@H WHERE UID=@UID",
 383 |                         P("@P", newHash), P("@H", newHash), P("@UID", user.UID));
 384 |                     }
 385 |                     catch
 386 |                     {
 387 |                         try
 388 |                         {
 389 |                             Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",
 390 |                             P("@P", newHash), P("@UID", user.UID));
 391 |                         }
 392 |                         catch { }
 393 |                     }
 394 |                 }
 395 | 
 396 |                 user.RoleNormalized = NormalizeRole(user.Role);
 397 | 
 398 |                 // Admin: password only (no MFA). Student/Lecturer still require authenticator.
 399 |                 if (string.Equals(user.RoleNormalized, "Admin", StringComparison.OrdinalIgnoreCase))
 400 |                 {
 401 |                     string adminToken = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);
 402 |                     SecurityAudit.Log("login.ok", user.UID, "Admin MFA bypass", email);
 403 |                     return new AuthResult
 404 |                     {
 405 |                         Success = true,
 406 |                         RequiresMfa = false,
 407 |                         Message = "Signed in as Admin.",
 408 |                         User = user,
 409 |                         Token = adminToken
 410 |                     };
 411 |                 }
 412 | 
 413 |                 // Student / Lecturer: MFA required
 414 |                 if (string.IsNullOrEmpty(user.MfaSecret))
 415 |                 {
 416 |                     return Fail(
 417 |                         "This account has no authenticator set up. Register a new account with MFA, " +
 418 |                         "or ask an admin to reset MFA for you.");
 419 |                 }
 420 | 
 421 |                 return new AuthResult
 422 |                 {
 423 |                     Success = true,
 424 |                     RequiresMfa = true,
 425 |                     MfaMethod = "totp",
 426 |                     Message = "Enter the 6-digit code from your authenticator app.",
 427 |                     User = user
 428 |                 };
 429 |             }
 430 |         }
 431 | 
 432 |         public static AuthResult VerifyMfa(int uid, string code, string method)
 433 |         {
 434 |             AuthSchema.Ensure();
 435 |             code = (code ?? "").Trim();
 436 |             if (uid <= 0 || string.IsNullOrEmpty(code))
 437 |             return Fail("Verification code is required.");
 438 | 
 439 |             using (var conn = DbHelper.OpenConnection())
 440 |             {
 441 |                 AuthUser user = LoadUserById(conn, uid);
 442 |                 if (user == null) return Fail("Session expired. Sign in again.");
 443 | 
 444 |                 bool ok = false;
 445 |                 if (string.Equals(method, "email", StringComparison.OrdinalIgnoreCase))
 446 |                 {
 447 |                     try
 448 |                     {
 449 |                         using (var cmd = new SqlCommand(
 450 |                         "SELECT EmailOtp, EmailOtpExpiry FROM Users WHERE UID=@UID", conn))
 451 |                         {
 452 |                             cmd.Parameters.AddWithValue("@UID", uid);
 453 |                             using (var r = cmd.ExecuteReader())
 454 |                             {
 455 |                                 if (r.Read())
 456 |                                 {
 457 |                                     string otp = r["EmailOtp"] == DBNull.Value ? null : r["EmailOtp"].ToString();
 458 |                                     DateTime? exp = r["EmailOtpExpiry"] == DBNull.Value
 459 |                                     ? (DateTime?)null
 460 |                                     : Convert.ToDateTime(r["EmailOtpExpiry"]);
 461 |                                     ok = otp != null && exp.HasValue && exp.Value > DateTime.UtcNow
 462 |                                     && string.Equals(otp, code, StringComparison.Ordinal);
 463 |                                 }
 464 |                             }
 465 |                         }
 466 |                         if (ok)
 467 |                         {
 468 |                             Exec(conn, "UPDATE Users SET EmailOtp=NULL, EmailOtpExpiry=NULL WHERE UID=@UID",
 469 |                             P("@UID", uid));
 470 |                         }
 471 |                     }
 472 |                     catch { ok = false; }
 473 |                 }
 474 |                 else
 475 |                 {
 476 |                     // TOTP (Google Authenticator) — same helper + window as password reset
 477 |                     string secret = TotpHelper.NormalizeSecret(user.MfaSecret);
 478 |                     if (string.IsNullOrEmpty(secret))
 479 |                         return Fail("MFA is not configured for this account. Register again with MFA, or contact admin.");
 480 |                     ok = TotpHelper.VerifyCode(secret, code);
 481 |                 }
 482 | 
 483 |                 if (!ok)
 484 |                 {
 485 |                     LoginThrottle.RegisterFailure(user.Email, HttpContext.Current);
 486 |                     return Fail("Invalid or expired verification code. Use the latest 6-digit code from the app (codes refresh every 30 seconds). Check that your phone time is set automatically.");
 487 |                 }
 488 | 
 489 |                 LoginThrottle.RegisterSuccess(user.Email, HttpContext.Current);
 490 |                 user.RoleNormalized = NormalizeRole(user.Role);
 491 |                 string token = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);
 492 |                 return new AuthResult
 493 |                 {
 494 |                     Success = true,
 495 |                     User = user,
 496 |                     Token = token,
 497 |                     Message = "OK"
 498 |                 };
 499 |             }
 500 |         }
 501 | 
 502 |         public static void CompleteLogin(HttpContext ctx, AuthUser user, string token)
 503 |         {
 504 |             if (ctx == null || user == null) return;
 505 |             // Always store as int so Course.LecturerUID FK gets a real UID
 506 |             ctx.Session["UserID"] = user.UID;
 507 |             ctx.Session["UserName"] = user.Name ?? "";
 508 |             ctx.Session["UserRole"] = user.RoleNormalized ?? NormalizeRole(user.Role);
 509 |             ctx.Session["AuthToken"] = token;
 510 |             JwtHelper.SetAuthCookie(ctx.Response, token);
 511 |             try { CsrfProtection.EnsureToken(ctx); } catch { }
 512 |             SecurityAudit.Log("login.ok", user.UID, "Role=" + (user.RoleNormalized ?? NormalizeRole(user.Role)), user.Email);
 513 |         }
 514 | 
 515 |         public static void Logout(HttpContext ctx)
 516 |         {
 517 |             if (ctx == null) return;
 518 |             int? uid = null;
 519 |             string email = null;
 520 |             try
 521 |             {
 522 |                 if (ctx.Session != null && ctx.Session["UserID"] != null)
 523 |                     uid = Convert.ToInt32(ctx.Session["UserID"]);
 524 |                 email = ctx.Session != null ? ctx.Session["UserName"] as string : null;
 525 |             }
 526 |             catch { }
 527 |             SecurityAudit.Log("logout", uid, null, email);
 528 |             try
 529 |             {
 530 |                 ctx.Session.Clear();
 531 |                 ctx.Session.Abandon();
 532 |             }
 533 |             catch { }
 534 |             JwtHelper.ClearAuthCookie(ctx.Response);
 535 |         }
 536 | 
 537 | 
 538 |         /// <summary>
 539 |         /// Step 1 — verify email + Google Authenticator TOTP only (no password change yet).
 540 |         /// </summary>
 541 |         public static AuthResult VerifyMfaForPasswordReset(string email, string totpCode)
 542 |         {
 543 |             AuthSchema.Ensure();
 544 |             email = (email ?? "").Trim().ToLowerInvariant();
 545 |             totpCode = (totpCode ?? "").Trim();
 546 | 
 547 |             if (string.IsNullOrEmpty(email) || !email.Contains("@"))
 548 |                 return Fail("Enter a valid email address.");
 549 |             if (string.IsNullOrEmpty(totpCode))
 550 |                 return Fail("Enter the 6-digit code from your authenticator app.");
 551 | 
 552 |             string lockMsg;
 553 |             if (LoginThrottle.IsLocked(email, HttpContext.Current, out lockMsg))
 554 |                 return Fail(lockMsg);
 555 | 
 556 |             using (var conn = DbHelper.OpenConnection())
 557 |             {
 558 |                 AuthUser user = LoadUserByEmail(conn, email);
 559 |                 string bad = "Invalid email or authenticator code.";
 560 |                 if (user == null)
 561 |                 {
 562 |                     LoginThrottle.RegisterFailure(email, HttpContext.Current);
 563 |                     SecurityAudit.Log("password.reset.fail", null, "Unknown email", email);
 564 |                     return Fail(bad);
 565 |                 }
 566 | 
 567 |                 string secret = TotpHelper.NormalizeSecret(user.MfaSecret);
 568 |                 if (string.IsNullOrEmpty(secret))
 569 |                 {
 570 |                     SecurityAudit.Log("password.reset.fail", user.UID, "No MFA secret", email);
 571 |                     return Fail(
 572 |                         "This account has no authenticator linked. Register a new account (MFA required) or contact an admin.");
 573 |                 }
 574 | 
 575 |                 // Same algorithm + window as login MFA (TotpHelper default ±2 min)
 576 |                 if (!TotpHelper.VerifyCode(secret, totpCode))
 577 |                 {
 578 |                     LoginThrottle.RegisterFailure(email, HttpContext.Current);
 579 |                     SecurityAudit.Log("password.reset.fail", user.UID, "Bad TOTP", email);
 580 | 
 581 |                     string msg =
 582 |                         "Invalid authenticator code for this account. " +
 583 |                         "Login and password-reset use the same secret from the database. ";
 584 | 
 585 |                     // When debug is on, show what the SERVER secret expects right now so you can
 586 |                     // compare with Google Authenticator (mismatch = wrong/old QR entry or DB reset).
 587 |                     if (IsMfaDebugEnabled())
 588 |                     {
 589 |                         try
 590 |                         {
 591 |                             string expected = TotpHelper.GenerateCode(secret);
 592 |                             string you = TotpHelper.NormalizeCode(totpCode);
 593 |                             msg +=
 594 |                                 "<br/><br/><strong>Debug (local only)</strong><br/>" +
 595 |                                 "Server expects right now: <strong style=\"letter-spacing:.2em\">" + expected + "</strong><br/>" +
 596 |                                 "You entered: <strong style=\"letter-spacing:.2em\">" +
 597 |                                 System.Web.HttpUtility.HtmlEncode(you) + "</strong><br/>" +
 598 |                                 "Secret length in DB: " + secret.Length +
 599 |                                 " (fingerprint " + secret.Substring(0, Math.Min(4, secret.Length)) + "…" +
 600 |                                 secret.Substring(Math.Max(0, secret.Length - 4)) + ")<br/>" +
 601 |                                 "If the numbers differ, your app entry is for a <em>different</em> secret " +
 602 |                                 "(old QR / re-registered account / DB reseed). Delete the EduLMS row in " +
 603 |                                 "Authenticator and register again, scanning the new QR.";
 604 |                         }
 605 |                         catch
 606 |                         {
 607 |                             msg += " (Could not generate debug code — secret may be corrupt.)";
 608 |                         }
 609 |                     }
 610 |                     else
 611 |                     {
 612 |                         msg +=
 613 |                             "If your app code never matches: delete the old EduLMS entry in Google Authenticator, " +
 614 |                             "register a new account, and scan the new QR. Phone time must be set to automatic.";
 615 |                     }
 616 | 
 617 |                     return Fail(msg);
 618 |                 }
 619 | 
 620 |                 LoginThrottle.RegisterSuccess(email, HttpContext.Current);
 621 |                 SecurityAudit.Log("password.reset.mfa_ok", user.UID, "MFA verified for reset", email);
 622 |                 user.RoleNormalized = NormalizeRole(user.Role);
 623 |                 return new AuthResult
 624 |                 {
 625 |                     Success = true,
 626 |                     Message = "Authenticator verified. Choose a new password.",
 627 |                     User = user
 628 |                 };
 629 |             }
 630 |         }
 631 | 
 632 |         /// <summary>
 633 |         /// Step 2 — set new password after MFA was verified (session holds UID).
 634 |         /// </summary>
 635 |         public static AuthResult CompletePasswordReset(int uid, string newPassword)
 636 |         {
 637 |             AuthSchema.Ensure();
 638 |             newPassword = newPassword ?? "";
 639 |             if (uid <= 0) return Fail("Session expired. Verify MFA again.");
 640 |             if (newPassword.Length < 8) return Fail("Password must be at least 8 characters.");
 641 |             if (!HasComplexity(newPassword)) return Fail("Password needs letters and numbers.");
 642 | 
 643 |             using (var conn = DbHelper.OpenConnection())
 644 |             {
 645 |                 AuthUser user = LoadUserById(conn, uid);
 646 |                 if (user == null) return Fail("Account not found. Start again.");
 647 | 
 648 |                 string newHash = PasswordHasher.Hash(newPassword);
 649 |                 try
 650 |                 {
 651 |                     Exec(conn, @"
 652 | UPDATE Users SET Password=@P, PasswordHash=@H, PasswordResetToken=NULL, PasswordResetExpiry=NULL
 653 | WHERE UID=@UID",
 654 |                         P("@P", newHash), P("@H", newHash), P("@UID", uid));
 655 |                 }
 656 |                 catch
 657 |                 {
 658 |                     try
 659 |                     {
 660 |                         Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",
 661 |                             P("@P", newHash), P("@UID", uid));
 662 |                     }
 663 |                     catch
 664 |                     {
 665 |                         return Fail("Could not update password.");
 666 |                     }
 667 |                 }
 668 | 
 669 |                 try { Exec(conn, "UPDATE Users SET MfaEnabled=1 WHERE UID=@UID", P("@UID", uid)); }
 670 |                 catch { }
 671 | 
 672 |                 SecurityAudit.Log("password.reset.ok", uid, "after MFA step", user.Email);
 673 |                 return new AuthResult
 674 |                 {
 675 |                     Success = true,
 676 |                     Message = "Password updated. Sign in with your new password and authenticator code."
 677 |                 };
 678 |             }
 679 |         }
 680 | 
 681 |         /// <summary>One-shot: verify TOTP then set password (ResetPassword.aspx).</summary>
 682 |         public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)
 683 |         {
 684 |             var v = VerifyMfaForPasswordReset(email, totpCode);
 685 |             if (!v.Success || v.User == null) return v;
 686 |             return CompletePasswordReset(v.User.UID, newPassword);
 687 |         }
 688 | 
 689 |         /// <summary>Legacy name — delegates to TOTP-based reset.</summary>
 690 |         public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)
 691 |         {
 692 |             return ResetPasswordWithTotp(email, code, newPassword);
 693 |         }
 694 | 
 695 |         /// <summary>Deprecated: password reset no longer issues email codes.</summary>
 696 |         public static AuthResult RequestPasswordReset(string email)
 697 |         {
 698 |             return new AuthResult
 699 |             {
 700 |                 Success = true,
 701 |                 Message = "Use your authenticator app code on the reset page (no email is sent)."
 702 |             };
 703 |         }
 704 | 
 705 |                 /// <summary>True if Users.UID exists (needed for Courses.LecturerUID FK).</summary>
 706 |         public static bool UserExists(int uid)
 707 |         {
 708 |             if (uid <= 0) return false;
 709 |             try
 710 |             {
 711 |                 using (var conn = DbHelper.OpenConnection())
 712 |                 {
 713 |                     object o = Scalar(conn, "SELECT COUNT(1) FROM Users WHERE UID = @UID", P("@UID", uid));
 714 |                     return o != null && Convert.ToInt32(o) > 0;
 715 |                 }
 716 |             }
 717 |             catch
 718 |             {
 719 |                 return false;
 720 |             }
 721 |         }
 722 | 
 723 |         /// <summary>
 724 |         /// Returns a session UID that exists in dbo.Users, or 0.
 725 |         /// Clears stale JWT/session when the user row is missing (e.g. after DB reset).
 726 |         /// </summary>
 727 |         public static int GetValidatedUserId(HttpContext ctx)
 728 |         {
 729 |             if (ctx == null || ctx.Session == null) return 0;
 730 | 
 731 |             TryRestoreSessionFromJwt(ctx);
 732 | 
 733 |             if (ctx.Session["UserID"] == null) return 0;
 734 |             int uid;
 735 |             try { uid = Convert.ToInt32(ctx.Session["UserID"]); }
 736 |             catch { return 0; }
 737 | 
 738 |             if (uid > 0 && UserExists(uid))
 739 |             return uid;
 740 | 
 741 |             // Stale session/JWT - user not in current EduDB
 742 |             try
 743 |             {
 744 |                 ctx.Session.Remove("UserID");
 745 |                 ctx.Session.Remove("UserName");
 746 |                 ctx.Session.Remove("UserRole");
 747 |                 ctx.Session.Remove("AuthToken");
 748 |             }
 749 |             catch { }
 750 |             JwtHelper.ClearAuthCookie(ctx.Response);
 751 |             return 0;
 752 |         }
 753 | 
 754 |         /// <summary>Restore session from JWT cookie if session expired; re-check Users table.</summary>
 755 |         public static bool TryRestoreSessionFromJwt(HttpContext ctx)
 756 |         {
 757 |             if (ctx == null || ctx.Session == null) return false;
 758 | 
 759 |             // Existing session: ensure UID still exists in this database
 760 |             if (ctx.Session["UserID"] != null)
 761 |             {
 762 |                 int existing;
 763 |                 try { existing = Convert.ToInt32(ctx.Session["UserID"]); }
 764 |                 catch { existing = 0; }
 765 |                 if (existing > 0 && UserExists(existing))
 766 |                 return true;
 767 |                 // Bad/stale session id - fall through and try cookie, else clear
 768 |                 try
 769 |                 {
 770 |                     ctx.Session.Remove("UserID");
 771 |                     ctx.Session.Remove("UserName");
 772 |                     ctx.Session.Remove("UserRole");
 773 |                 }
 774 |                 catch { }
 775 |             }
 776 | 
 777 |             string token = JwtHelper.ReadToken(ctx.Request);
 778 |             int uid;
 779 |             string name, role;
 780 |             if (!JwtHelper.TryValidate(token, out uid, out name, out role))
 781 |             {
 782 |                 JwtHelper.ClearAuthCookie(ctx.Response);
 783 |                 return false;
 784 |             }
 785 | 
 786 |             // Reject JWT for users that no longer exist (MDF replaced / reseeded)
 787 |             if (!UserExists(uid))
 788 |             {
 789 |                 JwtHelper.ClearAuthCookie(ctx.Response);
 790 |                 return false;
 791 |             }
 792 | 
 793 |             // Prefer live name/role from DB over token claims
 794 |             try
 795 |             {
 796 |                 using (var conn = DbHelper.OpenConnection())
 797 |                 {
 798 |                     using (var cmd = new SqlCommand(
 799 |                     "SELECT Name, Role FROM Users WHERE UID=@UID", conn))
 800 |                     {
 801 |                         cmd.Parameters.AddWithValue("@UID", uid);
 802 |                         using (var r = cmd.ExecuteReader())
 803 |                         {
 804 |                             if (r.Read())
 805 |                             {
 806 |                                 name = r["Name"] == DBNull.Value ? name : r["Name"].ToString();
 807 |                                 role = NormalizeRole(r["Role"] == DBNull.Value ? role : r["Role"].ToString());
 808 |                             }
 809 |                         }
 810 |                     }
 811 |                 }
 812 |             }
 813 |             catch { /* keep token claims */ }
 814 | 
 815 |             ctx.Session["UserID"] = uid;
 816 |             ctx.Session["UserName"] = name ?? "";
 817 |             ctx.Session["UserRole"] = role ?? "Student";
 818 |             ctx.Session["AuthToken"] = token;
 819 |             return true;
 820 |         }
 821 | 
 822 |         public static string NormalizeRole(string role)
 823 |         {
 824 |             if (string.IsNullOrWhiteSpace(role)) return "Student";
 825 |             var r = role.Trim().ToLowerInvariant();
 826 |             if (r == "0" || r == "admin" || r == "administrator") return "Admin";
 827 |             if (r == "2" || r == "teacher" || r == "lecturer") return "Lecturer";
 828 |             return "Student";
 829 |         }
 830 | 
 831 |         private static bool HasComplexity(string password)
 832 |         {
 833 |             bool letter = false, digit = false;
 834 |             foreach (char c in password)
 835 |             {
 836 |                 if (char.IsLetter(c)) letter = true;
 837 |                 if (char.IsDigit(c)) digit = true;
 838 |             }
 839 |             return letter && digit;
 840 |         }
 841 | 
 842 |         private static AuthUser LoadUserByEmail(SqlConnection conn, string email)
 843 |         {
 844 |             // Prefer extended columns; fall back
 845 |             try
 846 |             {
 847 |                 using (var cmd = new SqlCommand(@"
 848 |                 SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret
 849 |                 FROM Users WHERE Email = @Email", conn))
 850 |                 {
 851 |                     cmd.Parameters.AddWithValue("@Email", email);
 852 |                     using (var r = cmd.ExecuteReader())
 853 |                     {
 854 |                         if (!r.Read()) return null;
 855 |                         return MapUser(r);
 856 |                     }
 857 |                 }
 858 |             }
 859 |             catch
 860 |             {
 861 |                 using (var cmd = new SqlCommand(@"
 862 |                 SELECT UID, Name, Email, Role, Password FROM Users WHERE Email = @Email", conn))
 863 |                 {
 864 |                     cmd.Parameters.AddWithValue("@Email", email);
 865 |                     using (var r = cmd.ExecuteReader())
 866 |                     {
 867 |                         if (!r.Read()) return null;
 868 |                         return new AuthUser
 869 |                         {
 870 |                             UID = Convert.ToInt32(r["UID"]),
 871 |                             Name = r["Name"] == DBNull.Value ? "" : r["Name"].ToString(),
 872 |                             Email = r["Email"] == DBNull.Value ? "" : r["Email"].ToString(),
 873 |                             Role = r["Role"] == DBNull.Value ? "1" : r["Role"].ToString(),
 874 |                             PasswordStored = r["Password"] == DBNull.Value ? "" : r["Password"].ToString(),
 875 |                             MfaEnabled = false
 876 |                         };
 877 |                     }
 878 |                 }
 879 |             }
 880 |         }
 881 | 
 882 |         private static AuthUser LoadUserById(SqlConnection conn, int uid)
 883 |         {
 884 |             try
 885 |             {
 886 |                 using (var cmd = new SqlCommand(@"
 887 |                 SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret
 888 |                 FROM Users WHERE UID = @UID", conn))
 889 |                 {
 890 |                     cmd.Parameters.AddWithValue("@UID", uid);
 891 |                     using (var r = cmd.ExecuteReader())
 892 |                     {
 893 |                         if (!r.Read()) return null;
 894 |                         return MapUser(r);
 895 |                     }
 896 |                 }
 897 |             }
 898 |             catch
 899 |             {
 900 |                 using (var cmd = new SqlCommand(
```

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L7:** C# namespace grouping.
- **L9:** Class declaration for this page/service.
- **L22:** Class declaration for this page/service.
- **L39:** Pending registration in Session until MFA confirmed.
- **L40:** Pending registration in Session until MFA confirmed.
- **L41:** Pending registration in Session until MFA confirmed.
- **L42:** Pending registration in Session until MFA confirmed.
- **L43:** Pending registration in Session until MFA confirmed.
- **L44:** Pending registration in Session until MFA confirmed.
- **L45:** Pending registration in Session until MFA confirmed.
- **L46:** Pending registration in Session until MFA confirmed.
- **L52:** Pending registration in Session until MFA confirmed.
- **L66:** `rc` means: Holds “rc” for this scope. (text)
- **L78:** Import namespace/types.
- **L80:** `exists` means: Count > 0 check (email/user/row already exists).
- **L82:** Parameterized SQL — prevents classic SQL injection.
- **L86:** TOTP / authenticator (RFC 6238) helper. | `mfaSecret` means: Authenticator secret stored for the user.  New random MFA secret.
- **L89:** Server session for logged-in user.
- **L90:** Server session for logged-in user.
- **L91:** Server session for logged-in user.
- **L92:** Server session for logged-in user.
- **L93:** Server session for logged-in user.
- **L94:** Server session for logged-in user.
- **L95:** Server session for logged-in user.
- **L120:** Pending registration in Session until MFA confirmed.
- **L127:** Pending registration in Session until MFA confirmed.
- **L130:** Pending registration in Session until MFA confirmed.
- **L132:** Pending registration in Session until MFA confirmed.
- **L139:** TOTP / authenticator (RFC 6238) helper.
- **L142:** Pending registration in Session until MFA confirmed.
- **L146:** TOTP / authenticator (RFC 6238) helper.
- **L150:** Import namespace/types.
- **L152:** `exists` means: Count > 0 check (email/user/row already exists).
- **L154:** Parameterized SQL — prevents classic SQL injection.
- **L157:** Pending registration in Session until MFA confirmed.
- **L161:** `mfaSecret` means: Authenticator secret stored for the user.
- **L162:** `mfaOn` means: 1/0 flag written to Users.MfaEnabled.  Literal number `1`.
- **L165:** Error handling block.
- **L169:** Return new identity/UID after INSERT.
- **L171:** Parameterized SQL — prevents classic SQL injection.
- **L172:** Parameterized SQL — prevents classic SQL injection.
- **L173:** Parameterized SQL — prevents classic SQL injection.
- **L174:** Parameterized SQL — prevents classic SQL injection.
- **L175:** Parameterized SQL — prevents classic SQL injection.
- **L176:** Parameterized SQL — prevents classic SQL injection.
- **L177:** Parameterized SQL — prevents classic SQL injection.
- **L178:** Parameterized SQL — prevents classic SQL injection.
- **L180:** Handle/log exception.
- **L182:** Error handling block.
- **L186:** Return new identity/UID after INSERT.
- **L188:** Parameterized SQL — prevents classic SQL injection.
- **L189:** Parameterized SQL — prevents classic SQL injection.
- **L190:** Parameterized SQL — prevents classic SQL injection.
- **L191:** Parameterized SQL — prevents classic SQL injection.
- **L193:** Handle/log exception.
- **L199:** Error handling block.
- **L201:** Parameterized SQL — prevents classic SQL injection. | `byEmail` means: Email address.
- **L202:** Null-safe read from database values.
- **L205:** Handle/log exception.
- **L210:** Error handling block.
- **L214:** Parameterized SQL — prevents classic SQL injection.
- **L215:** Parameterized SQL — prevents classic SQL injection.
- **L216:** Parameterized SQL — prevents classic SQL injection.
- **L217:** Parameterized SQL — prevents classic SQL injection.
- **L218:** Parameterized SQL — prevents classic SQL injection.
- **L220:** Handle/log exception.
- **L222:** Error handling block.
- **L225:** Parameterized SQL — prevents classic SQL injection.
- **L227:** Handle/log exception.
- **L230:** Error handling block.
- **L232:** Parameterized SQL — prevents classic SQL injection. | `stored` means: Holds “stored” for this scope.
- **L233:** Null-safe read from database values. | `storedSecret` means: Secret key material (MFA Base32 or crypto secret). (text)
- **L235:** TOTP / authenticator (RFC 6238) helper.
- **L238:** Parameterized SQL — prevents classic SQL injection.
- **L242:** Handle/log exception.
- **L244:** Parameterized SQL — prevents classic SQL injection.
- **L248:** Pending registration in Session until MFA confirmed.
- **L249:** Write/read security audit events.
- **L270:** Pending registration in Session until MFA confirmed.
- **L274:** Pending registration in Session until MFA confirmed.
- **L282:** Pending registration in Session until MFA confirmed.
- **L285:** Pending registration in Session until MFA confirmed.
- **L287:** Error handling block.
- **L290:** Pending registration in Session until MFA confirmed.
- **L291:** Pending registration in Session until MFA confirmed.
- **L292:** Pending registration in Session until MFA confirmed.
- **L293:** Pending registration in Session until MFA confirmed.
- **L294:** Pending registration in Session until MFA confirmed.
- **L295:** Pending registration in Session until MFA confirmed.
- **L296:** Pending registration in Session until MFA confirmed.
- **L298:** Handle/log exception.
- **L301:** Pending registration in Session until MFA confirmed.
- **L309:** Error handling block.
- **L311:** Server session for logged-in user.
- **L312:** Server session for logged-in user.
- **L313:** Server session for logged-in user.
- **L314:** Server session for logged-in user.
- **L315:** Server session for logged-in user.
- **L316:** Server session for logged-in user.
- **L317:** Server session for logged-in user.
- **L318:** Server session for logged-in user.
- **L327:** Handle/log exception.
- **L333:** Pending registration in Session until MFA confirmed.
- **L344:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L350:** Brute-force lockout tracking.
- **L353:** Import namespace/types.
- **L355:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L358:** Brute-force lockout tracking.
- **L359:** Write/read security audit events.
- **L363:** `stored` means: Holds “stored” for this scope. (text)
- **L367:** Password hashing (PBKDF2).
- **L369:** Brute-force lockout tracking.
- **L370:** Write/read security audit events.
- **L374:** Brute-force lockout tracking.
- **L377:** Password hashing (PBKDF2).
- **L379:** Password hashing (PBKDF2). | `newHash` means: Cryptographic hash string. (text)  Assigned from password hash function.
- **L380:** Error handling block.
- **L383:** Parameterized SQL — prevents classic SQL injection.
- **L385:** Handle/log exception.
- **L387:** Error handling block.
- **L390:** Parameterized SQL — prevents classic SQL injection.
- **L392:** Handle/log exception.
- **L396:** Map role codes/names to Admin/Student/Lecturer.
- **L401:** JWT cookie create/validate/clear. | `adminToken` means: Security token (JWT or CSRF). (text)
- **L402:** Write/read security audit events.
- **L432:** Verify multi-factor / TOTP code.
- **L439:** Import namespace/types.
- **L441:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L444:** `ok` means: Boolean success flag.
- **L447:** Error handling block.
- **L449:** Import namespace/types.
- **L452:** Parameterized SQL — prevents classic SQL injection.
- **L453:** Import namespace/types.
- **L457:** Null-safe read from database values. | `otp` means: Holds “otp” for this scope. (text)
- **L458:** Null-safe read from database values. | `exp` means: Expiry DateTime.
- **L469:** Parameterized SQL — prevents classic SQL injection.
- **L472:** Handle/log exception.
- **L477:** TOTP / authenticator (RFC 6238) helper. | `secret` means: MFA TOTP Base32 secret for authenticator apps.
- **L480:** TOTP / authenticator (RFC 6238) helper.
- **L485:** Brute-force lockout tracking.
- **L489:** Brute-force lockout tracking.
- **L490:** Map role codes/names to Admin/Student/Lecturer.
- **L491:** JWT cookie create/validate/clear. | `token` means: JWT or CSRF token string.
- **L502:** Issue Session + JWT after successful auth.
- **L506:** Server session for logged-in user.
- **L507:** Server session for logged-in user.
- **L508:** Server session for logged-in user.
- **L509:** Server session for logged-in user.
- **L510:** JWT cookie create/validate/clear.
- **L511:** CSRF anti-forgery protection.
- **L512:** Map role codes/names to Admin/Student/Lecturer.
- **L519:** `email` means: Account email address (usually lowercased).
- **L520:** Error handling block.
- **L522:** Server session for logged-in user.
- **L523:** Server session for logged-in user.
- **L524:** Server session for logged-in user.
- **L526:** Handle/log exception.
- **L527:** Write/read security audit events.
- **L528:** Error handling block.
- **L533:** Handle/log exception.
- **L534:** JWT cookie create/validate/clear.
- **L541:** Verify multi-factor / TOTP code.
- **L553:** Brute-force lockout tracking.
- **L556:** Import namespace/types.
- **L558:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L559:** `bad` means: Holds “bad” for this scope. (text)  Literal text string.
- **L562:** Brute-force lockout tracking.
- **L563:** Write/read security audit events.
- **L567:** TOTP / authenticator (RFC 6238) helper. | `secret` means: MFA TOTP Base32 secret for authenticator apps.
- **L570:** Write/read security audit events.
- **L576:** TOTP / authenticator (RFC 6238) helper.
- **L578:** Brute-force lockout tracking.
- **L579:** Write/read security audit events.
- **L587:** Debug-only TOTP leak switch (must stay false for demos).
- **L589:** Error handling block.
- **L591:** TOTP / authenticator (RFC 6238) helper. | `expected` means: Holds “expected” for this scope. (text)  TOTP related value.
- **L592:** TOTP / authenticator (RFC 6238) helper. | `you` means: Holds “you” for this scope. (text)
- **L597:** Encode text to reduce XSS risk.
- **L605:** Handle/log exception.
- **L620:** Brute-force lockout tracking.
- **L621:** Write/read security audit events.
- **L622:** Map role codes/names to Admin/Student/Lecturer.
- **L635:** Password-reset MFA then update password hash.
- **L643:** Import namespace/types.
- **L645:** `user` means: AuthUser or user row (UID, Email, Role, MfaSecret, …).
- **L648:** Password hashing (PBKDF2). | `newHash` means: Cryptographic hash string. (text)  Assigned from password hash function.
- **L649:** Error handling block.
- **L654:** Parameterized SQL — prevents classic SQL injection.
- **L656:** Handle/log exception.
- **L658:** Error handling block.
- **L661:** Parameterized SQL — prevents classic SQL injection.
- **L663:** Handle/log exception.
- **L669:** Parameterized SQL — prevents classic SQL injection.
- **L670:** Handle/log exception.
- **L672:** Write/read security audit events.
- **L684:** Verify multi-factor / TOTP code. | `v` means: Generic value (version flag in JSON, or loop value).  Assigned from verification boolean/result.
- **L686:** Password-reset MFA then update password hash.
- **L709:** Error handling block.
- **L711:** Import namespace/types.
- **L713:** Parameterized SQL — prevents classic SQL injection. | `o` means: Holds “o” for this scope.
- **L717:** Handle/log exception.
- **L727:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L731:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L733:** Server session for logged-in user.
- **L735:** Server session for logged-in user.
- **L736:** Handle/log exception.
- **L742:** Error handling block.
- **L749:** Handle/log exception.
- **L750:** JWT cookie create/validate/clear.
- **L755:** Restore/validate user from Session or JWT; reject stale UIDs.
- **L760:** Server session for logged-in user.
- **L763:** Server session for logged-in user.
- **L764:** Handle/log exception.
- **L768:** Error handling block.
- **L774:** Handle/log exception.
- **L777:** JWT cookie create/validate/clear. | `token` means: JWT or CSRF token string.
- **L780:** JWT cookie create/validate/clear.
- **L782:** JWT cookie create/validate/clear.
- **L789:** JWT cookie create/validate/clear.
- **L794:** Error handling block.
- **L796:** Import namespace/types.
- **L798:** Import namespace/types.
- **L801:** Parameterized SQL — prevents classic SQL injection.
- **L802:** Import namespace/types.
- **L806:** Null-safe read from database values.
- **L807:** Null-safe read from database values.
- **L813:** Handle/log exception.
- **L815:** Server session for logged-in user.
- **L816:** Server session for logged-in user.
- **L817:** Server session for logged-in user.
- **L818:** Server session for logged-in user.
- **L822:** Map role codes/names to Admin/Student/Lecturer.
- **L825:** `r` means: Usually one database row (DataRow) in query loops.
- **L833:** `letter` means: Holds “letter” for this scope. (true/false)
- **L842:** Database access (pure SQL).
- **L845:** Error handling block.
- **L847:** Import namespace/types.
- **L851:** Parameterized SQL — prevents classic SQL injection.
- **L852:** Import namespace/types.
- **L859:** Handle/log exception.
- **L861:** Import namespace/types.
- **L864:** Parameterized SQL — prevents classic SQL injection.
- **L865:** Import namespace/types.
- **L871:** Null-safe read from database values.
- **L872:** Null-safe read from database values.
- **L873:** Null-safe read from database values.
- **L874:** Null-safe read from database values.
- **L882:** Database access (pure SQL).
- **L884:** Error handling block.
- **L886:** Import namespace/types.
- **L890:** Parameterized SQL — prevents classic SQL injection.
- **L891:** Import namespace/types.
- **L898:** Handle/log exception.
- **L900:** Import namespace/types.

_… truncated: 127 more lines in source. Open the original file for the rest._

## Source snapshot (raw)

_File has 1027 lines — raw dump omitted here to keep Markdown readable. Open `Data/Security/AuthService.cs` in the project._
