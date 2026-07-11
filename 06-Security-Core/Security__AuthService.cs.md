# AuthService.cs
**Source:** `Data/Security/AuthService.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Central auth orchestration: pending registration (no DB row until MFA), login password check, admin MFA bypass, TOTP verify, complete login (session + JWT), password reset (MFA then new password).

## File overview

- **Total lines:** 1027
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `PendingRegTtl` | `TimeSpan` | Holds “Pending Reg Ttl” for this scope. (type `TimeSpan`) |

## Functions / methods (32 found)

### `StartRegistration` — lines 52–114

#### Signature

```csharp
public static AuthResult StartRegistration(HttpContext ctx, string name, string email, string password, string roleChoice = "Student")
```

#### What it is

Validates the register form and stores pending account data in Session (does NOT create the user yet).

#### How it works

1. Validate name, email, password strength, and role (Student/Lecturer only).
2. Check the email is not already in Users.
3. Hash the password and generate a new MFA secret.
4. Store everything in Session only (pending registration) — do not insert into the database yet.
5. Return the MFA secret to the page so it can show the QR code.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `name` | `string` | Display name of user/course/criterion. |
| `email` | `string` | Account email address (usually lowercased). |
| `password` | `string` | Plain password from the form (never log this). |
| `roleChoice` | `string` | Role selected on the register form. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `rc` | `string` | Holds “rc” for this scope. (text) |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `mfaSecret` | `string` | Authenticator secret stored for the user.  New random MFA secret. |

#### Code

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

---

### `FinishRegistration` — lines 120–267

#### Signature

```csharp
public static AuthResult FinishRegistration(HttpContext ctx, string totpCode)
```

#### What it is

After a valid MFA code, inserts the new user into the database and clears the pending Session.

#### How it works

1. Read the pending registration from Session; fail if missing or timed out.
2. Verify the 6-digit authenticator code against the pending secret.
3. Insert the new user into Users (hash + MfaSecret + role).
4. Clear the pending Session data.
5. Return success so the UI can send the user to Login.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `totpCode` | `string` | User-entered 6-digit authenticator code. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `mfaSecret` | `string` | Authenticator secret stored for the user. |
| `mfaOn` | `int` | 1/0 flag written to Users.MfaEnabled.  Literal number `1`. |
| `byEmail` | `object` | Email address. |
| `stored` | `object` | Holds “stored” for this scope. |
| `storedSecret` | `string` | Secret key material (MFA Base32 or crypto secret). (text) |

#### Code

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

---

### `HasPendingRegistration` — lines 270–275

#### Signature

```csharp
public static bool HasPendingRegistration(HttpContext ctx)
```

#### What it is

Checks a condition related to **Has Pending Registration** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `HasPendingRegistration`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 270 |         public static bool HasPendingRegistration(HttpContext ctx)
 271 |         {
 272 |             string name, email, hash, roleCode, roleNormalized, secret;
 273 |             DateTime at;
 274 |             return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out at);
 275 |         }
```

---

### `TryGetPendingMfaSetup` — lines 278–283

#### Signature

```csharp
public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)
```

#### What it is

Checks a condition related to **Try Get Pending Mfa Setup** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `TryGetPendingMfaSetup`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `email` | `string` | Account email address (usually lowercased). |
| `mfaSecret` | `string` | Authenticator secret stored for the user. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 278 |         public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)
 279 |         {
 280 |             string name, hash, roleCode, roleNormalized;
 281 |             DateTime at;
 282 |             return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out mfaSecret, out at);
 283 |         }
```

---

### `ClearPendingRegistration` — lines 284–299

#### Signature

```csharp
public static void ClearPendingRegistration(HttpContext ctx)
```

#### What it is

Deletes or clears **Clear Pending Registration** (data or temporary state).

#### How it works

1. Clear Session data (logout or end of multi-step flow).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `TryReadPendingRegistration` — lines 300–328

#### Signature

```csharp
private static bool TryReadPendingRegistration(
            HttpContext ctx,
            out string name, out string email, out string hash,
            out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc)
```

#### What it is

Checks a condition related to **Try Read Pending Registration** and returns true/false (or tries an action safely).

#### How it works

1. Save temporary state in Session (`Session[SessRegName] as string;`).
2. Save temporary state in Session (`Session[SessRegEmail] as string;`).
3. Save temporary state in Session (`Session[SessRegHash] as string;`).
4. Save temporary state in Session (`Session[SessRegRole] as string;`).
5. Save temporary state in Session (`Session[SessRegRoleName] as string;`).
6. Save temporary state in Session (`Session[SessRegSecret] as string;`).
7. Save temporary state in Session (`Session[SessRegAt];`).
8. Return `false` to the caller.
9. Return `true` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `name` | `string` | Display name of user/course/criterion. |
| `email` | `string` | Account email address (usually lowercased). |
| `hash` | `string` | Password hash (PBKDF2) stored in DB. |
| `roleCode` | `string` | Stored role value (0 Admin / 1 Student / 2 Lecturer). |
| `roleNormalized` | `string` | Friendly role name (Admin, Student, Lecturer). |
| `secret` | `string` | MFA TOTP Base32 secret for authenticator apps. |
| `createdUtc` | `DateTime` | Date/time value. (date/time) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `Register` — lines 331–334

#### Signature

```csharp
public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")
```

#### What it is

Function `Register` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate the form and keep pending registration only in Session (no database user yet).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `name` | `string` | Display name of user/course/criterion. |
| `email` | `string` | Account email address (usually lowercased). |
| `password` | `string` | Plain password from the form (never log this). |
| `enableMfa` | `bool` | Whether MFA should be enabled for the account. |
| `roleChoice` | `string` | Role selected on the register form. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 331 |         public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")
 332 |         {
 333 |             return StartRegistration(HttpContext.Current, name, email, password, roleChoice);
 334 |         }
```

---

### `LoginPassword` — lines 339–430

#### Signature

```csharp
public static AuthResult LoginPassword(string email, string password)
```

#### What it is

Checks email + password; Admin finishes login; Student/Lecturer must do MFA next.

#### How it works

1. Clean the email (trim + lowercase) and read the password.
2. If LoginThrottle says this email/IP is locked, return an error and stop.
3. Open the database and load the user row by email.
4. If the user is missing or the password hash does not match, record a failure and return “invalid login”.
5. On success, clear the failure counter; if the stored password was plain text, upgrade it to a PBKDF2 hash.
6. If the role is Admin: create a JWT and return success without MFA.
7. If the role is Student/Lecturer: return success with RequiresMfa = true so the next page asks for the authenticator code.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `password` | `string` | Plain password from the form (never log this). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `var` | Current HTTP request context (Request, Response, Session). |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `stored` | `string` | Holds “stored” for this scope. (text) |
| `newHash` | `string` | Cryptographic hash string. (text)  Assigned from password hash function. |
| `adminToken` | `string` | Security token (JWT or CSRF). (text) |

#### Code

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

---

### `VerifyMfa` — lines 431–500

#### Signature

```csharp
public static AuthResult VerifyMfa(int uid, string code, string method)
```

#### What it is

Checks the authenticator code after password login, then allows full sign-in.

#### How it works

1. Load the user by UID from the pending MFA session.
2. Verify the TOTP code with TotpHelper (or email OTP if that method is used).
3. On success, build a JWT and return the user for CompleteLogin.
4. On failure, record a throttle failure and return an error.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `code` | `string` | 6-digit TOTP / OTP the user typed. |
| `method` | `string` | HTTP method (GET/POST) or MFA method (totp/email). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `ok` | `bool` | Boolean success flag. |
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |
| `r` | `var` | Usually one database row (DataRow) in query loops. |
| `exp` | `DateTime?` | Expiry DateTime. |
| `secret` | `string` | MFA TOTP Base32 secret for authenticator apps. |
| `token` | `string` | JWT or CSRF token string. |

#### Code

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

---

### `CompleteLogin` — lines 501–513

#### Signature

```csharp
public static void CompleteLogin(HttpContext ctx, AuthUser user, string token)
```

#### What it is

Writes Session keys and JWT cookie so the user is fully signed in.

#### How it works

1. Write Session keys: UserID, UserName, UserRole, AuthToken.
2. Set the JWT cookie on the browser response.
3. Optionally refresh the CSRF token.
4. Log a successful login in the security audit table.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |
| `user` | `AuthUser` | AuthUser or user row (UID, Email, Role, MfaSecret, …). |
| `token` | `string` | JWT or CSRF token string. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `Logout` — lines 514–535

#### Signature

```csharp
public static void Logout(HttpContext ctx)
```

#### What it is

Clears Session and JWT cookie so the user is signed out.

#### How it works

1. Save temporary state in Session (`Session !`).
2. Save temporary state in Session (`Session["UserID"]);`).
3. Save temporary state in Session (`Session !`).
4. Write an audit-log row for this security event.
5. Clear Session data (logout or end of multi-step flow).
6. Delete the JWT cookie (sign out).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |

#### Code

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

---

### `VerifyMfaForPasswordReset` — lines 541–630

#### Signature

```csharp
public static AuthResult VerifyMfaForPasswordReset(string email, string totpCode)
```

#### What it is

Step 1 of forgot-password: prove identity with email + authenticator code.

#### How it works

1. Validate email and TOTP code are present.
2. Load the user and check the authenticator code.
3. On success, the page stores UID in Session for the new-password step.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `totpCode` | `string` | User-entered 6-digit authenticator code. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `bad` | `string` | Holds “bad” for this scope. (text)  Literal text string. |
| `secret` | `string` | MFA TOTP Base32 secret for authenticator apps. |
| `msg` | `string` | Human-readable message (error or success).  Literal text string. |
| `expected` | `string` | Holds “expected” for this scope. (text)  TOTP related value. |
| `you` | `string` | Holds “you” for this scope. (text) |

#### Code

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

---

### `CompletePasswordReset` — lines 635–679

#### Signature

```csharp
public static AuthResult CompletePasswordReset(int uid, string newPassword)
```

#### What it is

Step 2 of forgot-password: save the new password hash for that user.

#### How it works

1. Validate the new password (length/complexity).
2. Hash it with PBKDF2.
3. UPDATE Users.Password / PasswordHash for that UID.
4. Return success so the UI can send the user to Login.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |
| `newPassword` | `string` | Password (plain input — hash before storing). (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `newHash` | `string` | Cryptographic hash string. (text)  Assigned from password hash function. |

#### Code

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

---

### `ResetPasswordWithTotp` — lines 682–687

#### Signature

```csharp
public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)
```

#### What it is

One-shot password reset: verify TOTP then set new password.

#### How it works

1. Verify email + authenticator code for password reset (step 1).
2. If the previous step failed, show the error and stop.
3. Update the user’s password hash (step 2 of reset).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `totpCode` | `string` | User-entered 6-digit authenticator code. |
| `newPassword` | `string` | Password (plain input — hash before storing). (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `v` | `var` | Generic value (version flag in JSON, or loop value).  Assigned from verification boolean/result. |

#### Code

```csharp
 682 |         public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)
 683 |         {
 684 |             var v = VerifyMfaForPasswordReset(email, totpCode);
 685 |             if (!v.Success || v.User == null) return v;
 686 |             return CompletePasswordReset(v.User.UID, newPassword);
 687 |         }
```

---

### `ResetPasswordWithCode` — lines 690–693

#### Signature

```csharp
public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)
```

#### What it is

Function `ResetPasswordWithCode` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `ResetPasswordWithCode`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |
| `code` | `string` | 6-digit TOTP / OTP the user typed. |
| `newPassword` | `string` | Password (plain input — hash before storing). (text) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 690 |         public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)
 691 |         {
 692 |             return ResetPasswordWithTotp(email, code, newPassword);
 693 |         }
```

---

### `RequestPasswordReset` — lines 696–703

#### Signature

```csharp
public static AuthResult RequestPasswordReset(string email)
```

#### What it is

Function `RequestPasswordReset` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `RequestPasswordReset`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

#### Signature

```csharp
public static bool UserExists(int uid)
```

#### What it is

Function `UserExists` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Open a connection to the LocalDB / SQL Server database.
3. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |

#### Code

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

---

### `GetValidatedUserId` — lines 727–752

#### Signature

```csharp
public static int GetValidatedUserId(HttpContext ctx)
```

#### What it is

Returns a real Users.UID from Session/JWT, or 0 if missing/stale.

#### How it works

1. If Session is empty, try to rebuild it from the JWT cookie.
2. Save temporary state in Session (`Session["UserID"]`).
3. Save temporary state in Session (`Session["UserID"]); }`).
4. Clear Session data (logout or end of multi-step flow).
5. Delete the JWT cookie (sign out).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `TryRestoreSessionFromJwt` — lines 755–820

#### Signature

```csharp
public static bool TryRestoreSessionFromJwt(HttpContext ctx)
```

#### What it is

If Session expired, rebuilds Session from a valid JWT cookie.

#### How it works

1. Save temporary state in Session (`Session["UserID"] !`).
2. Save temporary state in Session (`Session["UserID"]); }`).
3. Return `true` to the caller.
4. Clear Session data (logout or end of multi-step flow).
5. Delete the JWT cookie (sign out).
6. Return `false` to the caller.
7. Delete the JWT cookie (sign out).
8. Return `false` to the caller.
9. Open a connection to the LocalDB / SQL Server database.
10. Save temporary state in Session (`Session["UserID"]`).
11. Save temporary state in Session (`Session["UserName"]`).
12. Save temporary state in Session (`Session["UserRole"]`).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `HttpContext` | Current HTTP request context (Request, Response, Session). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `token` | `string` | JWT or CSRF token string. |
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `r` | `var` | Usually one database row (DataRow) in query loops. |

#### Code

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

---

### `NormalizeRole` — lines 821–829

#### Signature

```csharp
public static string NormalizeRole(string role)
```

#### What it is

Converts role codes (`0`/`1`/`2`) or names into Admin / Student / Lecturer.

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Branch for Admin (often skips MFA) vs Student/Lecturer.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `r` | `var` | Usually one database row (DataRow) in query loops. |

#### Code

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

---

### `HasComplexity` — lines 830–840

#### Signature

```csharp
private static bool HasComplexity(string password)
```

#### What it is

Checks a condition related to **Has Complexity** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `HasComplexity`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `password` | `string` | Plain password from the form (never log this). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `letter` | `bool` | Holds “letter” for this scope. (true/false) |
| `c` | `—` | Temporary value (character, course, or counter depending on loop). |

#### Code

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

---

### `LoadUserByEmail` — lines 841–880

#### Signature

```csharp
private static AuthUser LoadUserByEmail(SqlConnection conn, string email)
```

#### What it is

Reads/loads data related to **User By Email** and returns it for display or further use.

#### How it works

1. Starts when something calls `LoadUserByEmail`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `email` | `string` | Account email address (usually lowercased). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |
| `r` | `var` | Usually one database row (DataRow) in query loops. |

#### Code

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

---

### `LoadUserById` — lines 881–919

#### Signature

```csharp
private static AuthUser LoadUserById(SqlConnection conn, int uid)
```

#### What it is

Reads/loads data related to **User By Id** and returns it for display or further use.

#### How it works

1. Starts when something calls `LoadUserById`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |
| `r` | `var` | Usually one database row (DataRow) in query loops. |

#### Code

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

---

### `MapUser` — lines 920–947

#### Signature

```csharp
private static AuthUser MapUser(SqlDataReader r)
```

#### What it is

Function `MapUser` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `MapUser`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `r` | `SqlDataReader` | Usually one database row (DataRow) in query loops. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `mfa` | `bool` | Holds “mfa” for this scope. (true/false) |

#### Code

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

---

### `HasCol` — lines 948–955

#### Signature

```csharp
private static bool HasCol(SqlDataReader r, string name)
```

#### What it is

Checks a condition related to **Has Col** and returns true/false (or tries an action safely).

#### How it works

1. Return `true` to the caller.
2. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `r` | `SqlDataReader` | Usually one database row (DataRow) in query loops. |
| `name` | `string` | Display name of user/course/criterion. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `i` | `int` | Loop index (0-based counter in for-loops).  Literal number `0`. |

#### Code

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

#### Signature

```csharp
private static string Safe(SqlDataReader r, string col)
```

#### What it is

Function `Safe` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Safe`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `r` | `SqlDataReader` | Usually one database row (DataRow) in query loops. |
| `col` | `string` | Holds “col” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `i` | `int` | Loop index (0-based counter in for-loops). |

#### Code

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

---

### `Fail` — lines 966–970

#### Signature

```csharp
private static AuthResult Fail(string msg)
```

#### What it is

Function `Fail` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Fail`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `msg` | `string` | Human-readable message (error or success). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 966 | 
 967 |         private static AuthResult Fail(string msg)
 968 |         {
 969 |             return new AuthResult { Success = false, Message = msg };
 970 |         }
```

---

### `IsMfaDebugEnabled` — lines 976–984

#### Signature

```csharp
private static bool IsMfaDebugEnabled()
```

#### What it is

Checks a condition related to **Is Mfa Debug Enabled** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `IsMfaDebugEnabled`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `flag` | `string` | Holds “flag” for this scope. (text)  Read from Web.config. |

#### Code

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

---

### `GetStoredMfaSecretByEmail` — lines 989–1002

#### Signature

```csharp
public static string GetStoredMfaSecretByEmail(string email)
```

#### What it is

Reads/loads data related to **Stored Mfa Secret By Email** and returns it for display or further use.

#### How it works

1. Validate input; if invalid, stop and return an error/message.
2. Open a connection to the LocalDB / SQL Server database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `email` | `string` | Account email address (usually lowercased). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |

#### Code

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

---

### `P` — lines 1003–1007

#### Signature

```csharp
private static SqlParameter P(string n, object v)
```

#### What it is

Creates one SQL parameter (`@Name` + value) so user input is never concatenated into SQL.

#### How it works

1. Starts when something calls `P`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `n` | `string` | Numeric count or temporary integer. |
| `v` | `object` | Generic value (version flag in JSON, or loop value). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
1003 | 
1004 |         private static SqlParameter P(string n, object v)
1005 |         {
1006 |             return new SqlParameter(n, v ?? DBNull.Value);
1007 |         }
```

---

### `Scalar` — lines 1008–1016

#### Signature

```csharp
private static object Scalar(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### What it is

Function `Scalar` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `ps` | `SqlParameter[]` | Holds “ps” for this scope. (type `SqlParameter[]`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |

#### Code

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

---

### `Exec` — lines 1017–1025

#### Signature

```csharp
private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### What it is

Function `Exec` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run INSERT/UPDATE/DELETE SQL against the database.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `ps` | `SqlParameter[]` | Holds “ps” for this scope. (type `SqlParameter[]`) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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

_… truncated: 127 more lines. Open `Data/Security/AuthService.cs` for the rest._
