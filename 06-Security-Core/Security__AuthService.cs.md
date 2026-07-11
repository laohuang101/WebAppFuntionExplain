# AuthService.cs
**Source:** `Data/Security/AuthService.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Central auth orchestration: pending registration (no DB row until MFA), login password check, admin MFA bypass, TOTP verify, complete login (session + JWT), password reset (MFA then new password).

## File overview

- **Total lines:** 1027
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 46:** `PendingRegTtl` — type `TimeSpan`
- **Line 63:** `roleCode` — type `string`
- **Line 65:** `roleNormalized` — type `string`
- **Line 66:** `rc` — type `string`
- **Line 80:** `exists` — type `int`
- **Line 85:** `mfaSecret` — type `string`
- **Line 126:** `createdUtc` — type `DateTime`
- **Line 152:** `exists` — type `int`
- **Line 160:** `mfaSecret` — type `string`
- **Line 162:** `mfaOn` — type `int`
- **Line 163:** `uid` — type `int`
- **Line 201:** `byEmail` — type `object`
- **Line 232:** `stored` — type `object`
- **Line 233:** `storedSecret` — type `string`
- **Line 273:** `at` — type `DateTime`
- **Line 281:** `at` — type `DateTime`
- **Line 320:** `false` — type `return`
- **Line 324:** `false` — type `return`
- **Line 325:** `true` — type `return`
- **Line 344:** `ctx` — type `var`
- **Line 348:** `lockMsg` — type `string`
- **Line 355:** `user` — type `AuthUser`
- **Line 362:** `stored` — type `string`
- **Line 379:** `newHash` — type `string`
- **Line 401:** `adminToken` — type `string`
- **Line 441:** `user` — type `AuthUser`
- **Line 443:** `ok` — type `bool`
- **Line 457:** `otp` — type `string`
- **Line 458:** `exp` — type `DateTime?`
- **Line 477:** `secret` — type `string`
- **Line 491:** `token` — type `string`
- **Line 518:** `uid` — type `int?`
- **Line 519:** `email` — type `string`
- **Line 551:** `lockMsg` — type `string`
- **Line 558:** `user` — type `AuthUser`
- **Line 559:** `bad` — type `string`
- **Line 566:** `secret` — type `string`
- **Line 580:** `msg` — type `string`
- **Line 591:** `expected` — type `string`
- **Line 592:** `you` — type `string`
- **Line 645:** `user` — type `AuthUser`
- **Line 647:** `newHash` — type `string`
- **Line 684:** `v` — type `var`
- **Line 713:** `o` — type `object`
- **Line 719:** `false` — type `return`
- **Line 734:** `uid` — type `int`
- **Line 739:** `uid` — type `return`
- **Line 751:** `0` — type `return`
- **Line 762:** `existing` — type `int`
- **Line 766:** `true` — type `return`
- **Line 776:** `token` — type `string`
- **Line 778:** `uid` — type `int`
- **Line 783:** `false` — type `return`
- **Line 790:** `false` — type `return`
- **Line 819:** `true` — type `return`
- **Line 825:** `r` — type `var`
- **Line 833:** `letter` — type `bool`
- **Line 923:** `mfa` — type `bool`
- **Line 953:** `true` — type `return`
- **Line 954:** `false` — type `return`
- **Line 961:** `i` — type `int`
- **Line 980:** `flag` — type `string`
- **Line 997:** `u` — type `AuthUser`
- **Line 998:** `u` — type `return`

## Functions / methods (32 found)

### `StartRegistration` — lines 52–114

```
public static AuthResult StartRegistration(HttpContext ctx, string name, string email, string password, string roleChoice = "Student")
```

#### Explanation

- **Purpose:** Implements `StartRegistration`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `HttpContext ctx, string name, string email, string password, string roleChoice = "Student"`
- **Local variables:** `roleChoice`, `rc`, `conn`, `exists`, `mfaSecret`

#### Line-by-line (this function)

`  52`  `        public static AuthResult StartRegistration(HttpContext ctx, string name, string email, string password, string roleChoice = "Student")`
  - → Pending registration in Session until MFA confirmed.
`  53`  `        {`
`  54`  `            AuthSchema.Ensure();`
`  55`  `            name = (name ?? "").Trim();`
`  56`  `            email = (email ?? "").Trim().ToLowerInvariant();`
`  57`  `            password = password ?? "";`
`  58`  ``
`  59`  `            if (name.Length < 2) return Fail("Name must be at least 2 characters.");`
`  60`  `            if (!email.Contains("@") || email.Length < 5) return Fail("Enter a valid email address.");`
`  61`  `            if (password.Length < 8) return Fail("Password must be at least 8 characters.");`
`  62`  `            if (!HasComplexity(password)) return Fail("Password needs letters and numbers.");`
`  63`  ``
`  64`  `            string roleCode;`
`  65`  `            string roleNormalized;`
`  66`  `            string rc = (roleChoice ?? "").Trim().ToLowerInvariant();`
`  67`  `            if (rc == "lecturer" || rc == "teacher" || rc == "2")`
`  68`  `            {`
`  69`  `                roleCode = "2";`
`  70`  `                roleNormalized = "Lecturer";`
`  71`  `            }`
`  72`  `            else`
`  73`  `            {`
`  74`  `                roleCode = "1";`
`  75`  `                roleNormalized = "Student";`
`  76`  `            }`
`  77`  ``
`  78`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  79`  `            {`
`  80`  `                int exists = Convert.ToInt32(Scalar(conn,`
`  81`  `                    "SELECT COUNT(*) FROM Users WHERE Email = @Email",`
`  82`  `                    P("@Email", email)));`
`  83`  `                if (exists > 0) return Fail("An account with this email already exists.");`
`  84`  `            }`
`  85`  ``
`  86`  `            string mfaSecret = TotpHelper.GenerateSecret();`
  - → TOTP / authenticator (RFC 6238) helper.
`  87`  `            if (ctx != null && ctx.Session != null)`
`  88`  `            {`
`  89`  `                ctx.Session[SessRegName] = name;`
  - → Server session for logged-in user.
`  90`  `                ctx.Session[SessRegEmail] = email;`
  - → Server session for logged-in user.
`  91`  `                ctx.Session[SessRegHash] = PasswordHasher.Hash(password);`
  - → Server session for logged-in user.
`  92`  `                ctx.Session[SessRegRole] = roleCode;`
  - → Server session for logged-in user.
`  93`  `                ctx.Session[SessRegRoleName] = roleNormalized;`
  - → Server session for logged-in user.
`  94`  `                ctx.Session[SessRegSecret] = mfaSecret;`
  - → Server session for logged-in user.
`  95`  `                ctx.Session[SessRegAt] = DateTime.UtcNow;`
  - → Server session for logged-in user.
`  96`  `            }`
`  97`  ``
`  98`  `            return new AuthResult`
`  99`  `            {`
` 100`  `                Success = true,`
` 101`  `                Message = "Scan the QR code and enter the authenticator code to finish creating your account.",`
` 102`  `                RequiresMfa = true,`
` 103`  `                User = new AuthUser`
` 104`  `                {`
` 105`  `                    UID = 0, // not created yet`
` 106`  `                    Name = name,`
` 107`  `                    Email = email,`
` 108`  `                    Role = roleCode,`
` 109`  `                    RoleNormalized = roleNormalized,`
` 110`  `                    MfaEnabled = true,`
` 111`  `                    MfaSecret = mfaSecret`
` 112`  `                }`
` 113`  `            };`
` 114`  `        }`

---

### `FinishRegistration` — lines 120–267

```
public static AuthResult FinishRegistration(HttpContext ctx, string totpCode)
```

#### Explanation

- **Purpose:** Implements `FinishRegistration`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx, string totpCode`
- **Local variables:** `conn`, `exists`, `mfaSecret`, `mfaOn`, `byEmail`, `stored`, `storedSecret`

#### Line-by-line (this function)

` 120`  `        public static AuthResult FinishRegistration(HttpContext ctx, string totpCode)`
  - → Pending registration in Session until MFA confirmed.
` 121`  `        {`
` 122`  `            AuthSchema.Ensure();`
` 123`  `            totpCode = (totpCode ?? "").Trim();`
` 124`  ``
` 125`  `            string name, email, hash, roleCode, roleNormalized, secret;`
` 126`  `            DateTime createdUtc;`
` 127`  `            if (!TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out createdUtc))`
  - → Pending registration in Session until MFA confirmed.
` 128`  `                return Fail("Registration session expired. Start again from the form.");`
` 129`  ``
` 130`  `            if (DateTime.UtcNow - createdUtc > PendingRegTtl)`
  - → Pending registration in Session until MFA confirmed.
` 131`  `            {`
` 132`  `                ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 133`  `                return Fail("Registration timed out (15 minutes). Please register again.");`
` 134`  `            }`
` 135`  ``
` 136`  `            if (string.IsNullOrEmpty(totpCode))`
` 137`  `                return Fail("Enter the 6-digit code from your authenticator app.");`
` 138`  ``
` 139`  `            secret = TotpHelper.NormalizeSecret(secret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 140`  `            if (string.IsNullOrEmpty(secret))`
` 141`  `            {`
` 142`  `                ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 143`  `                return Fail("MFA setup data missing. Please register again.");`
` 144`  `            }`
` 145`  ``
` 146`  `            if (!TotpHelper.VerifyCode(secret, totpCode))`
  - → TOTP / authenticator (RFC 6238) helper.
` 147`  `                return Fail("Invalid authenticator code. Open Google Authenticator and enter the current 6-digit code for EduLMS.");`
` 148`  ``
` 149`  `            // Re-check email free (someone may have taken it while scanning QR)`
` 150`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 151`  `            {`
` 152`  `                int exists = Convert.ToInt32(Scalar(conn,`
` 153`  `                    "SELECT COUNT(*) FROM Users WHERE Email = @Email",`
` 154`  `                    P("@Email", email)));`
` 155`  `                if (exists > 0)`
` 156`  `                {`
` 157`  `                    ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 158`  `                    return Fail("An account with this email already exists. Sign in instead.");`
` 159`  `                }`
` 160`  ``
` 161`  `                string mfaSecret = secret;`
` 162`  `                int mfaOn = 1;`
` 163`  `                int uid;`
` 164`  ``
` 165`  `                try`
  - → Error handling block.
` 166`  `                {`
` 167`  `                    uid = Convert.ToInt32(Scalar(conn, @"`
` 168`  `                    INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaSecret, MfaEnabled, CreatedAt)`
` 169`  `                    OUTPUT INSERTED.UID`
` 170`  `                    VALUES (@Name, @Email, @Password, @Role, @PasswordHash, @MfaSecret, @MfaEnabled, @CreatedAt)",`
` 171`  `                        P("@Name", name),`
` 172`  `                        P("@Email", email),`
` 173`  `                        P("@Password", hash),`
` 174`  `                        P("@Role", roleCode),`
` 175`  `                        P("@PasswordHash", hash),`
` 176`  `                        P("@MfaSecret", (object)mfaSecret ?? DBNull.Value),`
` 177`  `                        P("@MfaEnabled", mfaOn),`
` 178`  `                        P("@CreatedAt", DateTime.UtcNow)));`
` 179`  `                }`
` 180`  `                catch`
  - → Handle/log exception.
` 181`  `                {`
` 182`  `                    try`
  - → Error handling block.
` 183`  `                    {`
` 184`  `                        uid = Convert.ToInt32(Scalar(conn, @"`
` 185`  `                        INSERT INTO Users (Name, Email, Password, Role)`
` 186`  `                        OUTPUT INSERTED.UID`
` 187`  `                        VALUES (@Name, @Email, @Password, @Role)",`
` 188`  `                            P("@Name", name),`
` 189`  `                            P("@Email", email),`
` 190`  `                            P("@Password", hash),`
` 191`  `                            P("@Role", roleCode)));`
` 192`  `                    }`
` 193`  `                    catch`
  - → Handle/log exception.
` 194`  `                    {`
` 195`  `                        return Fail("Could not create account. Check the Users table and try again.");`
` 196`  `                    }`
` 197`  `                }`
` 198`  ``
` 199`  `                try`
  - → Error handling block.
` 200`  `                {`
` 201`  `                    object byEmail = Scalar(conn, "SELECT UID FROM Users WHERE Email=@Email", P("@Email", email));`
` 202`  `                    if (byEmail != null && byEmail != DBNull.Value)`
` 203`  `                        uid = Convert.ToInt32(byEmail);`
` 204`  `                }`
` 205`  `                catch { }`
  - → Handle/log exception.
` 206`  ``
` 207`  `                if (uid <= 0)`
` 208`  `                    return Fail("Account insert did not return a valid user id.");`
` 209`  ``
` 210`  `                try`
  - → Error handling block.
` 211`  `                {`
` 212`  `                    Exec(conn, @"`
` 213`  `                    UPDATE Users SET Password=@P, PasswordHash=@H, MfaSecret=@S, MfaEnabled=@E WHERE UID=@UID",`
` 214`  `                        P("@P", hash),`
` 215`  `                        P("@H", hash),`
` 216`  `                        P("@S", (object)mfaSecret ?? DBNull.Value),`
` 217`  `                        P("@E", mfaOn),`
` 218`  `                        P("@UID", uid));`
` 219`  `                }`
` 220`  `                catch`
  - → Handle/log exception.
` 221`  `                {`
` 222`  `                    try`
  - → Error handling block.
` 223`  `                    {`
` 224`  `                        Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",`
` 225`  `                            P("@P", hash), P("@UID", uid));`
` 226`  `                    }`
` 227`  `                    catch { }`
  - → Handle/log exception.
` 228`  `                }`
` 229`  ``
` 230`  `                try`
  - → Error handling block.
` 231`  `                {`
` 232`  `                    object stored = Scalar(conn, "SELECT MfaSecret FROM Users WHERE UID=@UID", P("@UID", uid));`
` 233`  `                    string storedSecret = stored == null || stored == DBNull.Value`
` 234`  `                        ? ""`
` 235`  `                        : TotpHelper.NormalizeSecret(stored.ToString());`
  - → TOTP / authenticator (RFC 6238) helper.
` 236`  `                    if (storedSecret != mfaSecret)`
` 237`  `                    {`
` 238`  `                        try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }`
  - → Error handling block.
` 239`  `                        return Fail("Account could not save MFA secret. Check Users.MfaSecret column, then register again.");`
` 240`  `                    }`
` 241`  `                }`
` 242`  `                catch`
  - → Handle/log exception.
` 243`  `                {`
` 244`  `                    try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }`
  - → Error handling block.
` 245`  `                    return Fail("MFA columns missing. Restart the app so schema can update, then register again.");`
` 246`  `                }`
` 247`  ``
` 248`  `                ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 249`  `                SecurityAudit.Log("register.ok", uid, roleNormalized, email);`
  - → Write/read security audit events.
` 250`  ``
` 251`  `                return new AuthResult`
` 252`  `                {`
` 253`  `                    Success = true,`
` 254`  `                    Message = "Account created as " + roleNormalized + ". Sign in with your password and authenticator.",`
` 255`  `                    User = new AuthUser`
` 256`  `                    {`
` 257`  `                        UID = uid,`
` 258`  `                        Name = name,`
` 259`  `                        Email = email,`
` 260`  `                        Role = roleCode,`
` 261`  `                        RoleNormalized = roleNormalized,`
` 262`  `                        MfaEnabled = true,`
` 263`  `                        MfaSecret = mfaSecret`
` 264`  `                    }`
` 265`  `                };`
` 266`  `            }`
` 267`  `        }`

---

### `HasPendingRegistration` — lines 270–275

```
public static bool HasPendingRegistration(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `HasPendingRegistration`.
- **Parameters:** `HttpContext ctx`

#### Line-by-line (this function)

` 270`  `        public static bool HasPendingRegistration(HttpContext ctx)`
  - → Pending registration in Session until MFA confirmed.
` 271`  `        {`
` 272`  `            string name, email, hash, roleCode, roleNormalized, secret;`
` 273`  `            DateTime at;`
` 274`  `            return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out at);`
  - → Pending registration in Session until MFA confirmed.
` 275`  `        }`

---

### `TryGetPendingMfaSetup` — lines 278–283

```
public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)
```

#### Explanation

- **Purpose:** Implements `TryGetPendingMfaSetup`.
- **Parameters:** `HttpContext ctx, out string email, out string mfaSecret`

#### Line-by-line (this function)

` 278`  `        public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)`
` 279`  `        {`
` 280`  `            string name, hash, roleCode, roleNormalized;`
` 281`  `            DateTime at;`
` 282`  `            return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out mfaSecret, out at);`
  - → Pending registration in Session until MFA confirmed.
` 283`  `        }`

---

### `ClearPendingRegistration` — lines 284–299

```
public static void ClearPendingRegistration(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `ClearPendingRegistration`.
- **Session:** Reads/writes ASP.NET Session.
- **Pattern:** Delete/clear data.
- **Parameters:** `HttpContext ctx`

#### Line-by-line (this function)

` 284`  ``
` 285`  `        public static void ClearPendingRegistration(HttpContext ctx)`
  - → Pending registration in Session until MFA confirmed.
` 286`  `        {`
` 287`  `            try`
  - → Error handling block.
` 288`  `            {`
` 289`  `                if (ctx == null || ctx.Session == null) return;`
` 290`  `                ctx.Session.Remove(SessRegName);`
  - → Pending registration in Session until MFA confirmed.
` 291`  `                ctx.Session.Remove(SessRegEmail);`
  - → Pending registration in Session until MFA confirmed.
` 292`  `                ctx.Session.Remove(SessRegHash);`
  - → Pending registration in Session until MFA confirmed.
` 293`  `                ctx.Session.Remove(SessRegRole);`
  - → Pending registration in Session until MFA confirmed.
` 294`  `                ctx.Session.Remove(SessRegRoleName);`
  - → Pending registration in Session until MFA confirmed.
` 295`  `                ctx.Session.Remove(SessRegSecret);`
  - → Pending registration in Session until MFA confirmed.
` 296`  `                ctx.Session.Remove(SessRegAt);`
  - → Pending registration in Session until MFA confirmed.
` 297`  `            }`
` 298`  `            catch { }`
  - → Handle/log exception.
` 299`  `        }`

---

### `TryReadPendingRegistration` — lines 300–328

```
private static bool TryReadPendingRegistration(
            HttpContext ctx,
            out string name, out string email, out string hash,
            out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc)
```

#### Explanation

- **Purpose:** Implements `TryReadPendingRegistration`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx,
            out string name, out string email, out string hash,
            out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc`

#### Line-by-line (this function)

` 300`  ``
` 301`  `        private static bool TryReadPendingRegistration(`
  - → Pending registration in Session until MFA confirmed.
` 302`  `            HttpContext ctx,`
` 303`  `            out string name, out string email, out string hash,`
` 304`  `            out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc)`
` 305`  `        {`
` 306`  `            name = email = hash = roleCode = roleNormalized = secret = null;`
` 307`  `            createdUtc = DateTime.MinValue;`
` 308`  `            if (ctx == null || ctx.Session == null) return false;`
` 309`  `            try`
  - → Error handling block.
` 310`  `            {`
` 311`  `                name = ctx.Session[SessRegName] as string;`
  - → Server session for logged-in user.
` 312`  `                email = ctx.Session[SessRegEmail] as string;`
  - → Server session for logged-in user.
` 313`  `                hash = ctx.Session[SessRegHash] as string;`
  - → Server session for logged-in user.
` 314`  `                roleCode = ctx.Session[SessRegRole] as string;`
  - → Server session for logged-in user.
` 315`  `                roleNormalized = ctx.Session[SessRegRoleName] as string;`
  - → Server session for logged-in user.
` 316`  `                secret = ctx.Session[SessRegSecret] as string;`
  - → Server session for logged-in user.
` 317`  `                if (ctx.Session[SessRegAt] is DateTime)`
  - → Server session for logged-in user.
` 318`  `                    createdUtc = (DateTime)ctx.Session[SessRegAt];`
  - → Server session for logged-in user.
` 319`  `                else`
` 320`  `                    return false;`
` 321`  ``
` 322`  `                if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(email) ||`
` 323`  `                    string.IsNullOrEmpty(hash) || string.IsNullOrEmpty(secret))`
` 324`  `                    return false;`
` 325`  `                return true;`
` 326`  `            }`
` 327`  `            catch { return false; }`
  - → Handle/log exception.
` 328`  `        }`

---

### `Register` — lines 331–334

```
public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")
```

#### Explanation

- **Purpose:** Implements `Register`.
- **Parameters:** `string name, string email, string password, bool enableMfa, string roleChoice = "Student"`
- **Local variables:** `roleChoice`

#### Line-by-line (this function)

` 331`  `        public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")`
` 332`  `        {`
` 333`  `            return StartRegistration(HttpContext.Current, name, email, password, roleChoice);`
  - → Pending registration in Session until MFA confirmed.
` 334`  `        }`

---

### `LoginPassword` — lines 339–430

```
public static AuthResult LoginPassword(string email, string password)
```

#### Explanation

- **Purpose:** Implements `LoginPassword`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string email, string password`
- **Local variables:** `ctx`, `conn`, `stored`, `newHash`, `adminToken`

#### Line-by-line (this function)

` 339`  `        public static AuthResult LoginPassword(string email, string password)`
` 340`  `        {`
` 341`  `            AuthSchema.Ensure();`
` 342`  `            email = (email ?? "").Trim().ToLowerInvariant();`
` 343`  `            password = password ?? "";`
` 344`  `            var ctx = HttpContext.Current;`
` 345`  ``
` 346`  `            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))`
` 347`  `                return Fail("Email and password are required.");`
` 348`  ``
` 349`  `            string lockMsg;`
` 350`  `            if (LoginThrottle.IsLocked(email, ctx, out lockMsg))`
  - → Brute-force lockout tracking.
` 351`  `                return Fail(lockMsg);`
` 352`  ``
` 353`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 354`  `            {`
` 355`  `                AuthUser user = LoadUserByEmail(conn, email);`
` 356`  `                if (user == null)`
` 357`  `                {`
` 358`  `                    LoginThrottle.RegisterFailure(email, ctx);`
  - → Brute-force lockout tracking.
` 359`  `                    SecurityAudit.Log("login.fail", null, "Unknown email", email);`
  - → Write/read security audit events.
` 360`  `                    return Fail("Invalid email or password.");`
` 361`  `                }`
` 362`  ``
` 363`  `                string stored = !string.IsNullOrEmpty(user.PasswordHash)`
` 364`  `                    ? user.PasswordHash`
` 365`  `                    : user.PasswordStored;`
` 366`  ``
` 367`  `                if (!PasswordHasher.Verify(password, stored))`
  - → Password hashing (PBKDF2).
` 368`  `                {`
` 369`  `                    LoginThrottle.RegisterFailure(email, ctx);`
  - → Brute-force lockout tracking.
` 370`  `                    SecurityAudit.Log("login.fail", user.UID, "Bad password", email);`
  - → Write/read security audit events.
` 371`  `                    return Fail("Invalid email or password.");`
` 372`  `                }`
` 373`  ``
` 374`  `                LoginThrottle.RegisterSuccess(email, ctx);`
  - → Brute-force lockout tracking.
` 375`  ``
` 376`  `                // Upgrade plain-text → hash on successful login`
` 377`  `                if (!PasswordHasher.IsHashed(stored))`
  - → Password hashing (PBKDF2).
` 378`  `                {`
` 379`  `                    string newHash = PasswordHasher.Hash(password);`
  - → Password hashing (PBKDF2).
` 380`  `                    try`
  - → Error handling block.
` 381`  `                    {`
` 382`  `                        Exec(conn, "UPDATE Users SET Password=@P, PasswordHash=@H WHERE UID=@UID",`
` 383`  `                        P("@P", newHash), P("@H", newHash), P("@UID", user.UID));`
` 384`  `                    }`
` 385`  `                    catch`
  - → Handle/log exception.
` 386`  `                    {`
` 387`  `                        try`
  - → Error handling block.
` 388`  `                        {`
` 389`  `                            Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",`
` 390`  `                            P("@P", newHash), P("@UID", user.UID));`
` 391`  `                        }`
` 392`  `                        catch { }`
  - → Handle/log exception.
` 393`  `                    }`
` 394`  `                }`
` 395`  ``
` 396`  `                user.RoleNormalized = NormalizeRole(user.Role);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 397`  ``
` 398`  `                // Admin: password only (no MFA). Student/Lecturer still require authenticator.`
` 399`  `                if (string.Equals(user.RoleNormalized, "Admin", StringComparison.OrdinalIgnoreCase))`
` 400`  `                {`
` 401`  `                    string adminToken = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);`
  - → JWT cookie create/validate/clear.
` 402`  `                    SecurityAudit.Log("login.ok", user.UID, "Admin MFA bypass", email);`
  - → Write/read security audit events.
` 403`  `                    return new AuthResult`
` 404`  `                    {`
` 405`  `                        Success = true,`
` 406`  `                        RequiresMfa = false,`
` 407`  `                        Message = "Signed in as Admin.",`
` 408`  `                        User = user,`
` 409`  `                        Token = adminToken`
` 410`  `                    };`
` 411`  `                }`
` 412`  ``
` 413`  `                // Student / Lecturer: MFA required`
` 414`  `                if (string.IsNullOrEmpty(user.MfaSecret))`
` 415`  `                {`
` 416`  `                    return Fail(`
` 417`  `                        "This account has no authenticator set up. Register a new account with MFA, " +`
` 418`  `                        "or ask an admin to reset MFA for you.");`
` 419`  `                }`
` 420`  ``
` 421`  `                return new AuthResult`
` 422`  `                {`
` 423`  `                    Success = true,`
` 424`  `                    RequiresMfa = true,`
` 425`  `                    MfaMethod = "totp",`
` 426`  `                    Message = "Enter the 6-digit code from your authenticator app.",`
` 427`  `                    User = user`
` 428`  `                };`
` 429`  `            }`
` 430`  `        }`

---

### `VerifyMfa` — lines 431–500

```
public static AuthResult VerifyMfa(int uid, string code, string method)
```

#### Explanation

- **Purpose:** Implements `VerifyMfa`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `int uid, string code, string method`
- **Local variables:** `conn`, `ok`, `cmd`, `r`, `otp`, `secret`, `token`

#### Line-by-line (this function)

` 431`  ``
` 432`  `        public static AuthResult VerifyMfa(int uid, string code, string method)`
  - → Verify multi-factor / TOTP code.
` 433`  `        {`
` 434`  `            AuthSchema.Ensure();`
` 435`  `            code = (code ?? "").Trim();`
` 436`  `            if (uid <= 0 || string.IsNullOrEmpty(code))`
` 437`  `            return Fail("Verification code is required.");`
` 438`  ``
` 439`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 440`  `            {`
` 441`  `                AuthUser user = LoadUserById(conn, uid);`
` 442`  `                if (user == null) return Fail("Session expired. Sign in again.");`
` 443`  ``
` 444`  `                bool ok = false;`
` 445`  `                if (string.Equals(method, "email", StringComparison.OrdinalIgnoreCase))`
` 446`  `                {`
` 447`  `                    try`
  - → Error handling block.
` 448`  `                    {`
` 449`  `                        using (var cmd = new SqlCommand(`
  - → Import namespace/types.
` 450`  `                        "SELECT EmailOtp, EmailOtpExpiry FROM Users WHERE UID=@UID", conn))`
` 451`  `                        {`
` 452`  `                            cmd.Parameters.AddWithValue("@UID", uid);`
` 453`  `                            using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 454`  `                            {`
` 455`  `                                if (r.Read())`
` 456`  `                                {`
` 457`  `                                    string otp = r["EmailOtp"] == DBNull.Value ? null : r["EmailOtp"].ToString();`
` 458`  `                                    DateTime? exp = r["EmailOtpExpiry"] == DBNull.Value`
` 459`  `                                    ? (DateTime?)null`
` 460`  `                                    : Convert.ToDateTime(r["EmailOtpExpiry"]);`
` 461`  `                                    ok = otp != null && exp.HasValue && exp.Value > DateTime.UtcNow`
` 462`  `                                    && string.Equals(otp, code, StringComparison.Ordinal);`
` 463`  `                                }`
` 464`  `                            }`
` 465`  `                        }`
` 466`  `                        if (ok)`
` 467`  `                        {`
` 468`  `                            Exec(conn, "UPDATE Users SET EmailOtp=NULL, EmailOtpExpiry=NULL WHERE UID=@UID",`
` 469`  `                            P("@UID", uid));`
` 470`  `                        }`
` 471`  `                    }`
` 472`  `                    catch { ok = false; }`
  - → Handle/log exception.
` 473`  `                }`
` 474`  `                else`
` 475`  `                {`
` 476`  `                    // TOTP (Google Authenticator) — same helper + window as password reset`
` 477`  `                    string secret = TotpHelper.NormalizeSecret(user.MfaSecret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 478`  `                    if (string.IsNullOrEmpty(secret))`
` 479`  `                        return Fail("MFA is not configured for this account. Register again with MFA, or contact admin.");`
` 480`  `                    ok = TotpHelper.VerifyCode(secret, code);`
  - → TOTP / authenticator (RFC 6238) helper.
` 481`  `                }`
` 482`  ``
` 483`  `                if (!ok)`
` 484`  `                {`
` 485`  `                    LoginThrottle.RegisterFailure(user.Email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 486`  `                    return Fail("Invalid or expired verification code. Use the latest 6-digit code from the app (codes refresh every 30 seconds). Check that your phone time is set automatically.");`
` 487`  `                }`
` 488`  ``
` 489`  `                LoginThrottle.RegisterSuccess(user.Email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 490`  `                user.RoleNormalized = NormalizeRole(user.Role);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 491`  `                string token = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);`
  - → JWT cookie create/validate/clear.
` 492`  `                return new AuthResult`
` 493`  `                {`
` 494`  `                    Success = true,`
` 495`  `                    User = user,`
` 496`  `                    Token = token,`
` 497`  `                    Message = "OK"`
` 498`  `                };`
` 499`  `            }`
` 500`  `        }`

---

### `CompleteLogin` — lines 501–513

```
public static void CompleteLogin(HttpContext ctx, AuthUser user, string token)
```

#### Explanation

- **Purpose:** Implements `CompleteLogin`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx, AuthUser user, string token`

#### Line-by-line (this function)

` 501`  ``
` 502`  `        public static void CompleteLogin(HttpContext ctx, AuthUser user, string token)`
  - → Issue Session + JWT after successful auth.
` 503`  `        {`
` 504`  `            if (ctx == null || user == null) return;`
` 505`  `            // Always store as int so Course.LecturerUID FK gets a real UID`
` 506`  `            ctx.Session["UserID"] = user.UID;`
  - → Server session for logged-in user.
` 507`  `            ctx.Session["UserName"] = user.Name ?? "";`
  - → Server session for logged-in user.
` 508`  `            ctx.Session["UserRole"] = user.RoleNormalized ?? NormalizeRole(user.Role);`
  - → Server session for logged-in user.
` 509`  `            ctx.Session["AuthToken"] = token;`
  - → Server session for logged-in user.
` 510`  `            JwtHelper.SetAuthCookie(ctx.Response, token);`
  - → JWT cookie create/validate/clear.
` 511`  `            try { CsrfProtection.EnsureToken(ctx); } catch { }`
  - → CSRF anti-forgery protection.
` 512`  `            SecurityAudit.Log("login.ok", user.UID, "Role=" + (user.RoleNormalized ?? NormalizeRole(user.Role)), user.Email);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 513`  `        }`

---

### `Logout` — lines 514–535

```
public static void Logout(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `Logout`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx`
- **Local variables:** `email`

#### Line-by-line (this function)

` 514`  ``
` 515`  `        public static void Logout(HttpContext ctx)`
` 516`  `        {`
` 517`  `            if (ctx == null) return;`
` 518`  `            int? uid = null;`
` 519`  `            string email = null;`
` 520`  `            try`
  - → Error handling block.
` 521`  `            {`
` 522`  `                if (ctx.Session != null && ctx.Session["UserID"] != null)`
  - → Server session for logged-in user.
` 523`  `                    uid = Convert.ToInt32(ctx.Session["UserID"]);`
  - → Server session for logged-in user.
` 524`  `                email = ctx.Session != null ? ctx.Session["UserName"] as string : null;`
  - → Server session for logged-in user.
` 525`  `            }`
` 526`  `            catch { }`
  - → Handle/log exception.
` 527`  `            SecurityAudit.Log("logout", uid, null, email);`
  - → Write/read security audit events.
` 528`  `            try`
  - → Error handling block.
` 529`  `            {`
` 530`  `                ctx.Session.Clear();`
` 531`  `                ctx.Session.Abandon();`
` 532`  `            }`
` 533`  `            catch { }`
  - → Handle/log exception.
` 534`  `            JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 535`  `        }`

---

### `VerifyMfaForPasswordReset` — lines 541–630

```
public static AuthResult VerifyMfaForPasswordReset(string email, string totpCode)
```

#### Explanation

- **Purpose:** Implements `VerifyMfaForPasswordReset`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string email, string totpCode`
- **Local variables:** `conn`, `bad`, `secret`, `msg`, `expected`, `you`

#### Line-by-line (this function)

` 541`  `        public static AuthResult VerifyMfaForPasswordReset(string email, string totpCode)`
  - → Verify multi-factor / TOTP code.
` 542`  `        {`
` 543`  `            AuthSchema.Ensure();`
` 544`  `            email = (email ?? "").Trim().ToLowerInvariant();`
` 545`  `            totpCode = (totpCode ?? "").Trim();`
` 546`  ``
` 547`  `            if (string.IsNullOrEmpty(email) || !email.Contains("@"))`
` 548`  `                return Fail("Enter a valid email address.");`
` 549`  `            if (string.IsNullOrEmpty(totpCode))`
` 550`  `                return Fail("Enter the 6-digit code from your authenticator app.");`
` 551`  ``
` 552`  `            string lockMsg;`
` 553`  `            if (LoginThrottle.IsLocked(email, HttpContext.Current, out lockMsg))`
  - → Brute-force lockout tracking.
` 554`  `                return Fail(lockMsg);`
` 555`  ``
` 556`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 557`  `            {`
` 558`  `                AuthUser user = LoadUserByEmail(conn, email);`
` 559`  `                string bad = "Invalid email or authenticator code.";`
` 560`  `                if (user == null)`
` 561`  `                {`
` 562`  `                    LoginThrottle.RegisterFailure(email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 563`  `                    SecurityAudit.Log("password.reset.fail", null, "Unknown email", email);`
  - → Write/read security audit events.
` 564`  `                    return Fail(bad);`
` 565`  `                }`
` 566`  ``
` 567`  `                string secret = TotpHelper.NormalizeSecret(user.MfaSecret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 568`  `                if (string.IsNullOrEmpty(secret))`
` 569`  `                {`
` 570`  `                    SecurityAudit.Log("password.reset.fail", user.UID, "No MFA secret", email);`
  - → Write/read security audit events.
` 571`  `                    return Fail(`
` 572`  `                        "This account has no authenticator linked. Register a new account (MFA required) or contact an admin.");`
` 573`  `                }`
` 574`  ``
` 575`  `                // Same algorithm + window as login MFA (TotpHelper default ±2 min)`
` 576`  `                if (!TotpHelper.VerifyCode(secret, totpCode))`
  - → TOTP / authenticator (RFC 6238) helper.
` 577`  `                {`
` 578`  `                    LoginThrottle.RegisterFailure(email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 579`  `                    SecurityAudit.Log("password.reset.fail", user.UID, "Bad TOTP", email);`
  - → Write/read security audit events.
` 580`  ``
` 581`  `                    string msg =`
` 582`  `                        "Invalid authenticator code for this account. " +`
` 583`  `                        "Login and password-reset use the same secret from the database. ";`
` 584`  ``
` 585`  `                    // When debug is on, show what the SERVER secret expects right now so you can`
` 586`  `                    // compare with Google Authenticator (mismatch = wrong/old QR entry or DB reset).`
` 587`  `                    if (IsMfaDebugEnabled())`
  - → Debug-only TOTP leak switch (must stay false for demos).
` 588`  `                    {`
` 589`  `                        try`
  - → Error handling block.
` 590`  `                        {`
` 591`  `                            string expected = TotpHelper.GenerateCode(secret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 592`  `                            string you = TotpHelper.NormalizeCode(totpCode);`
  - → TOTP / authenticator (RFC 6238) helper.
` 593`  `                            msg +=`
` 594`  `                                "<br/><br/><strong>Debug (local only)</strong><br/>" +`
` 595`  `                                "Server expects right now: <strong style=\"letter-spacing:.2em\">" + expected + "</strong><br/>" +`
` 596`  `                                "You entered: <strong style=\"letter-spacing:.2em\">" +`
` 597`  `                                System.Web.HttpUtility.HtmlEncode(you) + "</strong><br/>" +`
  - → Encode text to reduce XSS risk.
` 598`  `                                "Secret length in DB: " + secret.Length +`
` 599`  `                                " (fingerprint " + secret.Substring(0, Math.Min(4, secret.Length)) + "…" +`
` 600`  `                                secret.Substring(Math.Max(0, secret.Length - 4)) + ")<br/>" +`
` 601`  `                                "If the numbers differ, your app entry is for a <em>different</em> secret " +`
` 602`  `                                "(old QR / re-registered account / DB reseed). Delete the EduLMS row in " +`
` 603`  `                                "Authenticator and register again, scanning the new QR.";`
` 604`  `                        }`
` 605`  `                        catch`
  - → Handle/log exception.
` 606`  `                        {`
` 607`  `                            msg += " (Could not generate debug code — secret may be corrupt.)";`
` 608`  `                        }`
` 609`  `                    }`
` 610`  `                    else`
` 611`  `                    {`
` 612`  `                        msg +=`
` 613`  `                            "If your app code never matches: delete the old EduLMS entry in Google Authenticator, " +`
` 614`  `                            "register a new account, and scan the new QR. Phone time must be set to automatic.";`
` 615`  `                    }`
` 616`  ``
` 617`  `                    return Fail(msg);`
` 618`  `                }`
` 619`  ``
` 620`  `                LoginThrottle.RegisterSuccess(email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 621`  `                SecurityAudit.Log("password.reset.mfa_ok", user.UID, "MFA verified for reset", email);`
  - → Write/read security audit events.
` 622`  `                user.RoleNormalized = NormalizeRole(user.Role);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 623`  `                return new AuthResult`
` 624`  `                {`
` 625`  `                    Success = true,`
` 626`  `                    Message = "Authenticator verified. Choose a new password.",`
` 627`  `                    User = user`
` 628`  `                };`
` 629`  `            }`
` 630`  `        }`

---

### `CompletePasswordReset` — lines 635–679

```
public static AuthResult CompletePasswordReset(int uid, string newPassword)
```

#### Explanation

- **Purpose:** Implements `CompletePasswordReset`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `int uid, string newPassword`
- **Local variables:** `conn`, `newHash`

#### Line-by-line (this function)

` 635`  `        public static AuthResult CompletePasswordReset(int uid, string newPassword)`
  - → Password-reset MFA then update password hash.
` 636`  `        {`
` 637`  `            AuthSchema.Ensure();`
` 638`  `            newPassword = newPassword ?? "";`
` 639`  `            if (uid <= 0) return Fail("Session expired. Verify MFA again.");`
` 640`  `            if (newPassword.Length < 8) return Fail("Password must be at least 8 characters.");`
` 641`  `            if (!HasComplexity(newPassword)) return Fail("Password needs letters and numbers.");`
` 642`  ``
` 643`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 644`  `            {`
` 645`  `                AuthUser user = LoadUserById(conn, uid);`
` 646`  `                if (user == null) return Fail("Account not found. Start again.");`
` 647`  ``
` 648`  `                string newHash = PasswordHasher.Hash(newPassword);`
  - → Password hashing (PBKDF2).
` 649`  `                try`
  - → Error handling block.
` 650`  `                {`
` 651`  `                    Exec(conn, @"`
` 652`  `UPDATE Users SET Password=@P, PasswordHash=@H, PasswordResetToken=NULL, PasswordResetExpiry=NULL`
` 653`  `WHERE UID=@UID",`
` 654`  `                        P("@P", newHash), P("@H", newHash), P("@UID", uid));`
` 655`  `                }`
` 656`  `                catch`
  - → Handle/log exception.
` 657`  `                {`
` 658`  `                    try`
  - → Error handling block.
` 659`  `                    {`
` 660`  `                        Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",`
` 661`  `                            P("@P", newHash), P("@UID", uid));`
` 662`  `                    }`
` 663`  `                    catch`
  - → Handle/log exception.
` 664`  `                    {`
` 665`  `                        return Fail("Could not update password.");`
` 666`  `                    }`
` 667`  `                }`
` 668`  ``
` 669`  `                try { Exec(conn, "UPDATE Users SET MfaEnabled=1 WHERE UID=@UID", P("@UID", uid)); }`
  - → Error handling block.
` 670`  `                catch { }`
  - → Handle/log exception.
` 671`  ``
` 672`  `                SecurityAudit.Log("password.reset.ok", uid, "after MFA step", user.Email);`
  - → Write/read security audit events.
` 673`  `                return new AuthResult`
` 674`  `                {`
` 675`  `                    Success = true,`
` 676`  `                    Message = "Password updated. Sign in with your new password and authenticator code."`
` 677`  `                };`
` 678`  `            }`
` 679`  `        }`

---

### `ResetPasswordWithTotp` — lines 682–687

```
public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)
```

#### Explanation

- **Purpose:** Implements `ResetPasswordWithTotp`.
- **Parameters:** `string email, string totpCode, string newPassword`
- **Local variables:** `v`

#### Line-by-line (this function)

` 682`  `        public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)`
` 683`  `        {`
` 684`  `            var v = VerifyMfaForPasswordReset(email, totpCode);`
  - → Verify multi-factor / TOTP code.
` 685`  `            if (!v.Success || v.User == null) return v;`
` 686`  `            return CompletePasswordReset(v.User.UID, newPassword);`
  - → Password-reset MFA then update password hash.
` 687`  `        }`

---

### `ResetPasswordWithCode` — lines 690–693

```
public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)
```

#### Explanation

- **Purpose:** Implements `ResetPasswordWithCode`.
- **Parameters:** `string email, string code, string newPassword`

#### Line-by-line (this function)

` 690`  `        public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)`
` 691`  `        {`
` 692`  `            return ResetPasswordWithTotp(email, code, newPassword);`
` 693`  `        }`

---

### `RequestPasswordReset` — lines 696–703

```
public static AuthResult RequestPasswordReset(string email)
```

#### Explanation

- **Purpose:** Implements `RequestPasswordReset`.
- **Parameters:** `string email`

#### Line-by-line (this function)

` 696`  `        public static AuthResult RequestPasswordReset(string email)`
` 697`  `        {`
` 698`  `            return new AuthResult`
` 699`  `            {`
` 700`  `                Success = true,`
` 701`  `                Message = "Use your authenticator app code on the reset page (no email is sent)."`
` 702`  `            };`
` 703`  `        }`

---

### `UserExists` — lines 706–721

```
public static bool UserExists(int uid)
```

#### Explanation

- **Purpose:** Implements `UserExists`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `int uid`
- **Local variables:** `conn`, `o`

#### Line-by-line (this function)

` 706`  `        public static bool UserExists(int uid)`
` 707`  `        {`
` 708`  `            if (uid <= 0) return false;`
` 709`  `            try`
  - → Error handling block.
` 710`  `            {`
` 711`  `                using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 712`  `                {`
` 713`  `                    object o = Scalar(conn, "SELECT COUNT(1) FROM Users WHERE UID = @UID", P("@UID", uid));`
` 714`  `                    return o != null && Convert.ToInt32(o) > 0;`
` 715`  `                }`
` 716`  `            }`
` 717`  `            catch`
  - → Handle/log exception.
` 718`  `            {`
` 719`  `                return false;`
` 720`  `            }`
` 721`  `        }`

---

### `GetValidatedUserId` — lines 727–752

```
public static int GetValidatedUserId(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `GetValidatedUserId`.
- **Session:** Reads/writes ASP.NET Session.
- **Pattern:** Read/load data for display.
- **Parameters:** `HttpContext ctx`

#### Line-by-line (this function)

` 727`  `        public static int GetValidatedUserId(HttpContext ctx)`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
` 728`  `        {`
` 729`  `            if (ctx == null || ctx.Session == null) return 0;`
` 730`  ``
` 731`  `            TryRestoreSessionFromJwt(ctx);`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
` 732`  ``
` 733`  `            if (ctx.Session["UserID"] == null) return 0;`
  - → Server session for logged-in user.
` 734`  `            int uid;`
` 735`  `            try { uid = Convert.ToInt32(ctx.Session["UserID"]); }`
  - → Server session for logged-in user.
` 736`  `            catch { return 0; }`
  - → Handle/log exception.
` 737`  ``
` 738`  `            if (uid > 0 && UserExists(uid))`
` 739`  `            return uid;`
` 740`  ``
` 741`  `            // Stale session/JWT - user not in current EduDB`
` 742`  `            try`
  - → Error handling block.
` 743`  `            {`
` 744`  `                ctx.Session.Remove("UserID");`
` 745`  `                ctx.Session.Remove("UserName");`
` 746`  `                ctx.Session.Remove("UserRole");`
` 747`  `                ctx.Session.Remove("AuthToken");`
` 748`  `            }`
` 749`  `            catch { }`
  - → Handle/log exception.
` 750`  `            JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 751`  `            return 0;`
` 752`  `        }`

---

### `TryRestoreSessionFromJwt` — lines 755–820

```
public static bool TryRestoreSessionFromJwt(HttpContext ctx)
```

#### Explanation

- **Purpose:** Implements `TryRestoreSessionFromJwt`.
- **Session:** Reads/writes ASP.NET Session.
- **Parameters:** `HttpContext ctx`
- **Local variables:** `token`, `conn`, `cmd`, `r`

#### Line-by-line (this function)

` 755`  `        public static bool TryRestoreSessionFromJwt(HttpContext ctx)`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
` 756`  `        {`
` 757`  `            if (ctx == null || ctx.Session == null) return false;`
` 758`  ``
` 759`  `            // Existing session: ensure UID still exists in this database`
` 760`  `            if (ctx.Session["UserID"] != null)`
  - → Server session for logged-in user.
` 761`  `            {`
` 762`  `                int existing;`
` 763`  `                try { existing = Convert.ToInt32(ctx.Session["UserID"]); }`
  - → Server session for logged-in user.
` 764`  `                catch { existing = 0; }`
  - → Handle/log exception.
` 765`  `                if (existing > 0 && UserExists(existing))`
` 766`  `                return true;`
` 767`  `                // Bad/stale session id - fall through and try cookie, else clear`
` 768`  `                try`
  - → Error handling block.
` 769`  `                {`
` 770`  `                    ctx.Session.Remove("UserID");`
` 771`  `                    ctx.Session.Remove("UserName");`
` 772`  `                    ctx.Session.Remove("UserRole");`
` 773`  `                }`
` 774`  `                catch { }`
  - → Handle/log exception.
` 775`  `            }`
` 776`  ``
` 777`  `            string token = JwtHelper.ReadToken(ctx.Request);`
  - → JWT cookie create/validate/clear.
` 778`  `            int uid;`
` 779`  `            string name, role;`
` 780`  `            if (!JwtHelper.TryValidate(token, out uid, out name, out role))`
  - → JWT cookie create/validate/clear.
` 781`  `            {`
` 782`  `                JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 783`  `                return false;`
` 784`  `            }`
` 785`  ``
` 786`  `            // Reject JWT for users that no longer exist (MDF replaced / reseeded)`
` 787`  `            if (!UserExists(uid))`
` 788`  `            {`
` 789`  `                JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 790`  `                return false;`
` 791`  `            }`
` 792`  ``
` 793`  `            // Prefer live name/role from DB over token claims`
` 794`  `            try`
  - → Error handling block.
` 795`  `            {`
` 796`  `                using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 797`  `                {`
` 798`  `                    using (var cmd = new SqlCommand(`
  - → Import namespace/types.
` 799`  `                    "SELECT Name, Role FROM Users WHERE UID=@UID", conn))`
` 800`  `                    {`
` 801`  `                        cmd.Parameters.AddWithValue("@UID", uid);`
` 802`  `                        using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 803`  `                        {`
` 804`  `                            if (r.Read())`
` 805`  `                            {`
` 806`  `                                name = r["Name"] == DBNull.Value ? name : r["Name"].ToString();`
` 807`  `                                role = NormalizeRole(r["Role"] == DBNull.Value ? role : r["Role"].ToString());`
  - → Map role codes/names to Admin/Student/Lecturer.
` 808`  `                            }`
` 809`  `                        }`
` 810`  `                    }`
` 811`  `                }`
` 812`  `            }`
` 813`  `            catch { /* keep token claims */ }`
  - → Handle/log exception.
` 814`  ``
` 815`  `            ctx.Session["UserID"] = uid;`
  - → Server session for logged-in user.
` 816`  `            ctx.Session["UserName"] = name ?? "";`
  - → Server session for logged-in user.
` 817`  `            ctx.Session["UserRole"] = role ?? "Student";`
  - → Server session for logged-in user.
` 818`  `            ctx.Session["AuthToken"] = token;`
  - → Server session for logged-in user.
` 819`  `            return true;`
` 820`  `        }`

---

### `NormalizeRole` — lines 821–829

```
public static string NormalizeRole(string role)
```

#### Explanation

- **Purpose:** Implements `NormalizeRole`.
- **Parameters:** `string role`
- **Local variables:** `r`

#### Line-by-line (this function)

` 821`  ``
` 822`  `        public static string NormalizeRole(string role)`
  - → Map role codes/names to Admin/Student/Lecturer.
` 823`  `        {`
` 824`  `            if (string.IsNullOrWhiteSpace(role)) return "Student";`
` 825`  `            var r = role.Trim().ToLowerInvariant();`
` 826`  `            if (r == "0" || r == "admin" || r == "administrator") return "Admin";`
` 827`  `            if (r == "2" || r == "teacher" || r == "lecturer") return "Lecturer";`
` 828`  `            return "Student";`
` 829`  `        }`

---

### `HasComplexity` — lines 830–840

```
private static bool HasComplexity(string password)
```

#### Explanation

- **Purpose:** Implements `HasComplexity`.
- **Parameters:** `string password`
- **Local variables:** `letter`

#### Line-by-line (this function)

` 830`  ``
` 831`  `        private static bool HasComplexity(string password)`
` 832`  `        {`
` 833`  `            bool letter = false, digit = false;`
` 834`  `            foreach (char c in password)`
` 835`  `            {`
` 836`  `                if (char.IsLetter(c)) letter = true;`
` 837`  `                if (char.IsDigit(c)) digit = true;`
` 838`  `            }`
` 839`  `            return letter && digit;`
` 840`  `        }`

---

### `LoadUserByEmail` — lines 841–880

```
private static AuthUser LoadUserByEmail(SqlConnection conn, string email)
```

#### Explanation

- **Purpose:** Implements `LoadUserByEmail`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters:** `SqlConnection conn, string email`
- **Local variables:** `cmd`, `r`

#### Line-by-line (this function)

` 841`  ``
` 842`  `        private static AuthUser LoadUserByEmail(SqlConnection conn, string email)`
  - → Database access (pure SQL).
` 843`  `        {`
` 844`  `            // Prefer extended columns; fall back`
` 845`  `            try`
  - → Error handling block.
` 846`  `            {`
` 847`  `                using (var cmd = new SqlCommand(@"`
  - → Import namespace/types.
` 848`  `                SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret`
` 849`  `                FROM Users WHERE Email = @Email", conn))`
` 850`  `                {`
` 851`  `                    cmd.Parameters.AddWithValue("@Email", email);`
` 852`  `                    using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 853`  `                    {`
` 854`  `                        if (!r.Read()) return null;`
` 855`  `                        return MapUser(r);`
` 856`  `                    }`
` 857`  `                }`
` 858`  `            }`
` 859`  `            catch`
  - → Handle/log exception.
` 860`  `            {`
` 861`  `                using (var cmd = new SqlCommand(@"`
  - → Import namespace/types.
` 862`  `                SELECT UID, Name, Email, Role, Password FROM Users WHERE Email = @Email", conn))`
` 863`  `                {`
` 864`  `                    cmd.Parameters.AddWithValue("@Email", email);`
` 865`  `                    using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 866`  `                    {`
` 867`  `                        if (!r.Read()) return null;`
` 868`  `                        return new AuthUser`
` 869`  `                        {`
` 870`  `                            UID = Convert.ToInt32(r["UID"]),`
` 871`  `                            Name = r["Name"] == DBNull.Value ? "" : r["Name"].ToString(),`
` 872`  `                            Email = r["Email"] == DBNull.Value ? "" : r["Email"].ToString(),`
` 873`  `                            Role = r["Role"] == DBNull.Value ? "1" : r["Role"].ToString(),`
` 874`  `                            PasswordStored = r["Password"] == DBNull.Value ? "" : r["Password"].ToString(),`
` 875`  `                            MfaEnabled = false`
` 876`  `                        };`
` 877`  `                    }`
` 878`  `                }`
` 879`  `            }`
` 880`  `        }`

---

### `LoadUserById` — lines 881–919

```
private static AuthUser LoadUserById(SqlConnection conn, int uid)
```

#### Explanation

- **Purpose:** Implements `LoadUserById`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters:** `SqlConnection conn, int uid`
- **Local variables:** `cmd`, `r`

#### Line-by-line (this function)

` 881`  ``
` 882`  `        private static AuthUser LoadUserById(SqlConnection conn, int uid)`
  - → Database access (pure SQL).
` 883`  `        {`
` 884`  `            try`
  - → Error handling block.
` 885`  `            {`
` 886`  `                using (var cmd = new SqlCommand(@"`
  - → Import namespace/types.
` 887`  `                SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret`
` 888`  `                FROM Users WHERE UID = @UID", conn))`
` 889`  `                {`
` 890`  `                    cmd.Parameters.AddWithValue("@UID", uid);`
` 891`  `                    using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 892`  `                    {`
` 893`  `                        if (!r.Read()) return null;`
` 894`  `                        return MapUser(r);`
` 895`  `                    }`
` 896`  `                }`
` 897`  `            }`
` 898`  `            catch`
  - → Handle/log exception.
` 899`  `            {`
` 900`  `                using (var cmd = new SqlCommand(`
  - → Import namespace/types.
` 901`  `                "SELECT UID, Name, Email, Role, Password FROM Users WHERE UID=@UID", conn))`
` 902`  `                {`
` 903`  `                    cmd.Parameters.AddWithValue("@UID", uid);`
` 904`  `                    using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 905`  `                    {`
` 906`  `                        if (!r.Read()) return null;`
` 907`  `                        return new AuthUser`
` 908`  `                        {`
` 909`  `                            UID = Convert.ToInt32(r["UID"]),`
` 910`  `                            Name = r["Name"].ToString(),`
` 911`  `                            Email = r["Email"].ToString(),`
` 912`  `                            Role = r["Role"].ToString(),`
` 913`  `                            PasswordStored = r["Password"].ToString(),`
` 914`  `                            MfaEnabled = false`
` 915`  `                        };`
` 916`  `                    }`
` 917`  `                }`
` 918`  `            }`
` 919`  `        }`

---

### `MapUser` — lines 920–947

```
private static AuthUser MapUser(SqlDataReader r)
```

#### Explanation

- **Purpose:** Implements `MapUser`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlDataReader r`
- **Local variables:** `mfa`

#### Line-by-line (this function)

` 920`  ``
` 921`  `        private static AuthUser MapUser(SqlDataReader r)`
` 922`  `        {`
` 923`  `            bool mfa = false;`
` 924`  `            try`
  - → Error handling block.
` 925`  `            {`
` 926`  `                if (HasCol(r, "MfaEnabled") && r["MfaEnabled"] != DBNull.Value)`
` 927`  `                mfa = Convert.ToBoolean(r["MfaEnabled"]);`
` 928`  `            }`
` 929`  `            catch`
  - → Handle/log exception.
` 930`  `            {`
` 931`  `                try { mfa = Convert.ToInt32(r["MfaEnabled"]) != 0; } catch { }`
  - → Error handling block.
` 932`  `            }`
` 933`  ``
` 934`  `            return new AuthUser`
` 935`  `            {`
` 936`  `                UID = Convert.ToInt32(r["UID"]),`
` 937`  `                Name = Safe(r, "Name"),`
` 938`  `                Email = Safe(r, "Email"),`
` 939`  `                Role = Safe(r, "Role"),`
` 940`  `                PasswordStored = Safe(r, "Password"),`
` 941`  `                PasswordHash = HasCol(r, "PasswordHash") ? Safe(r, "PasswordHash") : null,`
` 942`  `                MfaEnabled = mfa,`
` 943`  `                MfaSecret = HasCol(r, "MfaSecret")`
` 944`  `                ? TotpHelper.NormalizeSecret(Safe(r, "MfaSecret"))`
  - → TOTP / authenticator (RFC 6238) helper.
` 945`  `                : null`
` 946`  `            };`
` 947`  `        }`

---

### `HasCol` — lines 948–955

```
private static bool HasCol(SqlDataReader r, string name)
```

#### Explanation

- **Purpose:** Implements `HasCol`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlDataReader r, string name`
- **Local variables:** `i`

#### Line-by-line (this function)

` 948`  ``
` 949`  `        private static bool HasCol(SqlDataReader r, string name)`
` 950`  `        {`
` 951`  `            for (int i = 0; i < r.FieldCount; i++)`
` 952`  `            if (string.Equals(r.GetName(i), name, StringComparison.OrdinalIgnoreCase))`
` 953`  `            return true;`
` 954`  `            return false;`
` 955`  `        }`

---

### `Safe` — lines 956–965

```
private static string Safe(SqlDataReader r, string col)
```

#### Explanation

- **Purpose:** Implements `Safe`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlDataReader r, string col`
- **Local variables:** `i`

#### Line-by-line (this function)

` 956`  ``
` 957`  `        private static string Safe(SqlDataReader r, string col)`
` 958`  `        {`
` 959`  `            try`
  - → Error handling block.
` 960`  `            {`
` 961`  `                int i = r.GetOrdinal(col);`
` 962`  `                return r.IsDBNull(i) ? "" : r.GetValue(i).ToString();`
` 963`  `            }`
` 964`  `            catch { return ""; }`
  - → Handle/log exception.
` 965`  `        }`

---

### `Fail` — lines 966–970

```
private static AuthResult Fail(string msg)
```

#### Explanation

- **Purpose:** Implements `Fail`.
- **Parameters:** `string msg`

#### Line-by-line (this function)

` 966`  ``
` 967`  `        private static AuthResult Fail(string msg)`
` 968`  `        {`
` 969`  `            return new AuthResult { Success = false, Message = msg };`
` 970`  `        }`

---

### `IsMfaDebugEnabled` — lines 976–984

```
private static bool IsMfaDebugEnabled()
```

#### Explanation

- **Purpose:** Implements `IsMfaDebugEnabled`.
- **Local variables:** `flag`

#### Line-by-line (this function)

` 976`  `        private static bool IsMfaDebugEnabled()`
  - → Debug-only TOTP leak switch (must stay false for demos).
` 977`  `        {`
` 978`  `            try`
  - → Error handling block.
` 979`  `            {`
` 980`  `                string flag = System.Configuration.ConfigurationManager.AppSettings["MfaDebug"];`
  - → Debug-only TOTP leak switch (must stay false for demos).
` 981`  `                return string.Equals(flag, "true", StringComparison.OrdinalIgnoreCase);`
` 982`  `            }`
` 983`  `            catch { return false; }`
  - → Handle/log exception.
` 984`  `        }`

---

### `GetStoredMfaSecretByEmail` — lines 989–1002

```
public static string GetStoredMfaSecretByEmail(string email)
```

#### Explanation

- **Purpose:** Implements `GetStoredMfaSecretByEmail`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters:** `string email`
- **Local variables:** `conn`

#### Line-by-line (this function)

` 989`  `        public static string GetStoredMfaSecretByEmail(string email)`
` 990`  `        {`
` 991`  `            email = (email ?? "").Trim().ToLowerInvariant();`
` 992`  `            if (string.IsNullOrEmpty(email)) return null;`
` 993`  `            try`
  - → Error handling block.
` 994`  `            {`
` 995`  `                using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 996`  `                {`
` 997`  `                    AuthUser u = LoadUserByEmail(conn, email);`
` 998`  `                    return u == null ? null : TotpHelper.NormalizeSecret(u.MfaSecret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 999`  `                }`
`1000`  `            }`
`1001`  `            catch { return null; }`
  - → Handle/log exception.
`1002`  `        }`

---

### `P` — lines 1003–1007

```
private static SqlParameter P(string n, object v)
```

#### Explanation

- **Purpose:** Implements `P`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string n, object v`

#### Line-by-line (this function)

`1003`  ``
`1004`  `        private static SqlParameter P(string n, object v)`
`1005`  `        {`
`1006`  `            return new SqlParameter(n, v ?? DBNull.Value);`
`1007`  `        }`

---

### `Scalar` — lines 1008–1016

```
private static object Scalar(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `Scalar`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string sql, params SqlParameter[] ps`
- **Local variables:** `cmd`

#### Line-by-line (this function)

`1008`  ``
`1009`  `        private static object Scalar(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
`1010`  `        {`
`1011`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`1012`  `            {`
`1013`  `                if (ps != null) cmd.Parameters.AddRange(ps);`
`1014`  `                return cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`1015`  `            }`
`1016`  `        }`

---

### `Exec` — lines 1017–1025

```
private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `Exec`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string sql, params SqlParameter[] ps`
- **Local variables:** `cmd`

#### Line-by-line (this function)

`1017`  ``
`1018`  `        private static void Exec(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
`1019`  `        {`
`1020`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`1021`  `            {`
`1022`  `                if (ps != null) cmd.Parameters.AddRange(ps);`
`1023`  `                cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`1024`  `            }`
`1025`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Data;`
  - → Import namespace/types.
`   3`  `using System.Data.SqlClient;`
  - → Import namespace/types.
`   4`  `using System.Web;`
  - → Import namespace/types.
`   5`  `using WebAppAssignment.Data;`
  - → Import namespace/types.
`   6`  ``
`   7`  `namespace WebAppAssignment.Data.Security`
  - → C# namespace grouping.
`   8`  `{`
`   9`  `    public class AuthUser`
  - → Class declaration for this page/service.
`  10`  `    {`
`  11`  `        public int UID { get; set; }`
`  12`  `        public string Name { get; set; }`
`  13`  `        public string Email { get; set; }`
`  14`  `        public string Role { get; set; }`
`  15`  `        public string RoleNormalized { get; set; }`
`  16`  `        public string PasswordStored { get; set; }`
`  17`  `        public string PasswordHash { get; set; }`
`  18`  `        public bool MfaEnabled { get; set; }`
`  19`  `        public string MfaSecret { get; set; }`
`  20`  `    }`
`  21`  ``
`  22`  `    public class AuthResult`
  - → Class declaration for this page/service.
`  23`  `    {`
`  24`  `        public bool Success { get; set; }`
`  25`  `        public string Message { get; set; }`
`  26`  `        public bool RequiresMfa { get; set; }`
`  27`  `        public string MfaMethod { get; set; } // "totp" | "email"`
`  28`  `        public string DemoEmailOtp { get; set; } // shown when no email SMTP configured`
`  29`  `        public AuthUser User { get; set; }`
`  30`  `        public string Token { get; set; }`
`  31`  `    }`
`  32`  ``
`  33`  `    /// <summary>`
`  34`  `    /// Pure-SQL authentication (SqlConnection + parameterized SQL only — no Entity Framework / ORM).`
`  35`  `    /// </summary>`
`  36`  `    public static class AuthService`
`  37`  `    {`
`  38`  `        // Pending registration held as plain Session strings (not a mapped entity). No Users row until MFA OK.`
`  39`  `        private const string SessRegName = "Reg.Name";`
  - → Pending registration in Session until MFA confirmed.
`  40`  `        private const string SessRegEmail = "Reg.Email";`
  - → Pending registration in Session until MFA confirmed.
`  41`  `        private const string SessRegHash = "Reg.PasswordHash";`
  - → Pending registration in Session until MFA confirmed.
`  42`  `        private const string SessRegRole = "Reg.RoleCode";`
  - → Pending registration in Session until MFA confirmed.
`  43`  `        private const string SessRegRoleName = "Reg.RoleNormalized";`
  - → Pending registration in Session until MFA confirmed.
`  44`  `        private const string SessRegSecret = "Reg.MfaSecret";`
  - → Pending registration in Session until MFA confirmed.
`  45`  `        private const string SessRegAt = "Reg.CreatedUtc";`
  - → Pending registration in Session until MFA confirmed.
`  46`  `        private static readonly TimeSpan PendingRegTtl = TimeSpan.FromMinutes(15);`
  - → Pending registration in Session until MFA confirmed.
`  47`  ``
`  48`  `        /// <summary>`
`  49`  `        /// Step 1 — validate form, ensure email free, generate MFA secret.`
`  50`  `        /// Does NOT insert into Users. Data lives in Session until MFA is confirmed.`
`  51`  `        /// </summary>`
`  52`  `        public static AuthResult StartRegistration(HttpContext ctx, string name, string email, string password, string roleChoice = "Student")`
  - → Pending registration in Session until MFA confirmed.
`  53`  `        {`
`  54`  `            AuthSchema.Ensure();`
`  55`  `            name = (name ?? "").Trim();`
`  56`  `            email = (email ?? "").Trim().ToLowerInvariant();`
`  57`  `            password = password ?? "";`
`  58`  ``
`  59`  `            if (name.Length < 2) return Fail("Name must be at least 2 characters.");`
`  60`  `            if (!email.Contains("@") || email.Length < 5) return Fail("Enter a valid email address.");`
`  61`  `            if (password.Length < 8) return Fail("Password must be at least 8 characters.");`
`  62`  `            if (!HasComplexity(password)) return Fail("Password needs letters and numbers.");`
`  63`  ``
`  64`  `            string roleCode;`
`  65`  `            string roleNormalized;`
`  66`  `            string rc = (roleChoice ?? "").Trim().ToLowerInvariant();`
`  67`  `            if (rc == "lecturer" || rc == "teacher" || rc == "2")`
`  68`  `            {`
`  69`  `                roleCode = "2";`
`  70`  `                roleNormalized = "Lecturer";`
`  71`  `            }`
`  72`  `            else`
`  73`  `            {`
`  74`  `                roleCode = "1";`
`  75`  `                roleNormalized = "Student";`
`  76`  `            }`
`  77`  ``
`  78`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
`  79`  `            {`
`  80`  `                int exists = Convert.ToInt32(Scalar(conn,`
`  81`  `                    "SELECT COUNT(*) FROM Users WHERE Email = @Email",`
`  82`  `                    P("@Email", email)));`
`  83`  `                if (exists > 0) return Fail("An account with this email already exists.");`
`  84`  `            }`
`  85`  ``
`  86`  `            string mfaSecret = TotpHelper.GenerateSecret();`
  - → TOTP / authenticator (RFC 6238) helper.
`  87`  `            if (ctx != null && ctx.Session != null)`
`  88`  `            {`
`  89`  `                ctx.Session[SessRegName] = name;`
  - → Server session for logged-in user.
`  90`  `                ctx.Session[SessRegEmail] = email;`
  - → Server session for logged-in user.
`  91`  `                ctx.Session[SessRegHash] = PasswordHasher.Hash(password);`
  - → Server session for logged-in user.
`  92`  `                ctx.Session[SessRegRole] = roleCode;`
  - → Server session for logged-in user.
`  93`  `                ctx.Session[SessRegRoleName] = roleNormalized;`
  - → Server session for logged-in user.
`  94`  `                ctx.Session[SessRegSecret] = mfaSecret;`
  - → Server session for logged-in user.
`  95`  `                ctx.Session[SessRegAt] = DateTime.UtcNow;`
  - → Server session for logged-in user.
`  96`  `            }`
`  97`  ``
`  98`  `            return new AuthResult`
`  99`  `            {`
` 100`  `                Success = true,`
` 101`  `                Message = "Scan the QR code and enter the authenticator code to finish creating your account.",`
` 102`  `                RequiresMfa = true,`
` 103`  `                User = new AuthUser`
` 104`  `                {`
` 105`  `                    UID = 0, // not created yet`
` 106`  `                    Name = name,`
` 107`  `                    Email = email,`
` 108`  `                    Role = roleCode,`
` 109`  `                    RoleNormalized = roleNormalized,`
` 110`  `                    MfaEnabled = true,`
` 111`  `                    MfaSecret = mfaSecret`
` 112`  `                }`
` 113`  `            };`
` 114`  `        }`
` 115`  ``
` 116`  `        /// <summary>`
` 117`  `        /// Step 2 — verify TOTP against session secret, then pure-SQL INSERT.`
` 118`  `        /// Abandoning before this leaves no account in the database.`
` 119`  `        /// </summary>`
` 120`  `        public static AuthResult FinishRegistration(HttpContext ctx, string totpCode)`
  - → Pending registration in Session until MFA confirmed.
` 121`  `        {`
` 122`  `            AuthSchema.Ensure();`
` 123`  `            totpCode = (totpCode ?? "").Trim();`
` 124`  ``
` 125`  `            string name, email, hash, roleCode, roleNormalized, secret;`
` 126`  `            DateTime createdUtc;`
` 127`  `            if (!TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out createdUtc))`
  - → Pending registration in Session until MFA confirmed.
` 128`  `                return Fail("Registration session expired. Start again from the form.");`
` 129`  ``
` 130`  `            if (DateTime.UtcNow - createdUtc > PendingRegTtl)`
  - → Pending registration in Session until MFA confirmed.
` 131`  `            {`
` 132`  `                ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 133`  `                return Fail("Registration timed out (15 minutes). Please register again.");`
` 134`  `            }`
` 135`  ``
` 136`  `            if (string.IsNullOrEmpty(totpCode))`
` 137`  `                return Fail("Enter the 6-digit code from your authenticator app.");`
` 138`  ``
` 139`  `            secret = TotpHelper.NormalizeSecret(secret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 140`  `            if (string.IsNullOrEmpty(secret))`
` 141`  `            {`
` 142`  `                ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 143`  `                return Fail("MFA setup data missing. Please register again.");`
` 144`  `            }`
` 145`  ``
` 146`  `            if (!TotpHelper.VerifyCode(secret, totpCode))`
  - → TOTP / authenticator (RFC 6238) helper.
` 147`  `                return Fail("Invalid authenticator code. Open Google Authenticator and enter the current 6-digit code for EduLMS.");`
` 148`  ``
` 149`  `            // Re-check email free (someone may have taken it while scanning QR)`
` 150`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 151`  `            {`
` 152`  `                int exists = Convert.ToInt32(Scalar(conn,`
` 153`  `                    "SELECT COUNT(*) FROM Users WHERE Email = @Email",`
` 154`  `                    P("@Email", email)));`
` 155`  `                if (exists > 0)`
` 156`  `                {`
` 157`  `                    ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 158`  `                    return Fail("An account with this email already exists. Sign in instead.");`
` 159`  `                }`
` 160`  ``
` 161`  `                string mfaSecret = secret;`
` 162`  `                int mfaOn = 1;`
` 163`  `                int uid;`
` 164`  ``
` 165`  `                try`
  - → Error handling block.
` 166`  `                {`
` 167`  `                    uid = Convert.ToInt32(Scalar(conn, @"`
` 168`  `                    INSERT INTO Users (Name, Email, Password, Role, PasswordHash, MfaSecret, MfaEnabled, CreatedAt)`
` 169`  `                    OUTPUT INSERTED.UID`
` 170`  `                    VALUES (@Name, @Email, @Password, @Role, @PasswordHash, @MfaSecret, @MfaEnabled, @CreatedAt)",`
` 171`  `                        P("@Name", name),`
` 172`  `                        P("@Email", email),`
` 173`  `                        P("@Password", hash),`
` 174`  `                        P("@Role", roleCode),`
` 175`  `                        P("@PasswordHash", hash),`
` 176`  `                        P("@MfaSecret", (object)mfaSecret ?? DBNull.Value),`
` 177`  `                        P("@MfaEnabled", mfaOn),`
` 178`  `                        P("@CreatedAt", DateTime.UtcNow)));`
` 179`  `                }`
` 180`  `                catch`
  - → Handle/log exception.
` 181`  `                {`
` 182`  `                    try`
  - → Error handling block.
` 183`  `                    {`
` 184`  `                        uid = Convert.ToInt32(Scalar(conn, @"`
` 185`  `                        INSERT INTO Users (Name, Email, Password, Role)`
` 186`  `                        OUTPUT INSERTED.UID`
` 187`  `                        VALUES (@Name, @Email, @Password, @Role)",`
` 188`  `                            P("@Name", name),`
` 189`  `                            P("@Email", email),`
` 190`  `                            P("@Password", hash),`
` 191`  `                            P("@Role", roleCode)));`
` 192`  `                    }`
` 193`  `                    catch`
  - → Handle/log exception.
` 194`  `                    {`
` 195`  `                        return Fail("Could not create account. Check the Users table and try again.");`
` 196`  `                    }`
` 197`  `                }`
` 198`  ``
` 199`  `                try`
  - → Error handling block.
` 200`  `                {`
` 201`  `                    object byEmail = Scalar(conn, "SELECT UID FROM Users WHERE Email=@Email", P("@Email", email));`
` 202`  `                    if (byEmail != null && byEmail != DBNull.Value)`
` 203`  `                        uid = Convert.ToInt32(byEmail);`
` 204`  `                }`
` 205`  `                catch { }`
  - → Handle/log exception.
` 206`  ``
` 207`  `                if (uid <= 0)`
` 208`  `                    return Fail("Account insert did not return a valid user id.");`
` 209`  ``
` 210`  `                try`
  - → Error handling block.
` 211`  `                {`
` 212`  `                    Exec(conn, @"`
` 213`  `                    UPDATE Users SET Password=@P, PasswordHash=@H, MfaSecret=@S, MfaEnabled=@E WHERE UID=@UID",`
` 214`  `                        P("@P", hash),`
` 215`  `                        P("@H", hash),`
` 216`  `                        P("@S", (object)mfaSecret ?? DBNull.Value),`
` 217`  `                        P("@E", mfaOn),`
` 218`  `                        P("@UID", uid));`
` 219`  `                }`
` 220`  `                catch`
  - → Handle/log exception.
` 221`  `                {`
` 222`  `                    try`
  - → Error handling block.
` 223`  `                    {`
` 224`  `                        Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",`
` 225`  `                            P("@P", hash), P("@UID", uid));`
` 226`  `                    }`
` 227`  `                    catch { }`
  - → Handle/log exception.
` 228`  `                }`
` 229`  ``
` 230`  `                try`
  - → Error handling block.
` 231`  `                {`
` 232`  `                    object stored = Scalar(conn, "SELECT MfaSecret FROM Users WHERE UID=@UID", P("@UID", uid));`
` 233`  `                    string storedSecret = stored == null || stored == DBNull.Value`
` 234`  `                        ? ""`
` 235`  `                        : TotpHelper.NormalizeSecret(stored.ToString());`
  - → TOTP / authenticator (RFC 6238) helper.
` 236`  `                    if (storedSecret != mfaSecret)`
` 237`  `                    {`
` 238`  `                        try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }`
  - → Error handling block.
` 239`  `                        return Fail("Account could not save MFA secret. Check Users.MfaSecret column, then register again.");`
` 240`  `                    }`
` 241`  `                }`
` 242`  `                catch`
  - → Handle/log exception.
` 243`  `                {`
` 244`  `                    try { Exec(conn, "DELETE FROM Users WHERE UID=@UID", P("@UID", uid)); } catch { }`
  - → Error handling block.
` 245`  `                    return Fail("MFA columns missing. Restart the app so schema can update, then register again.");`
` 246`  `                }`
` 247`  ``
` 248`  `                ClearPendingRegistration(ctx);`
  - → Pending registration in Session until MFA confirmed.
` 249`  `                SecurityAudit.Log("register.ok", uid, roleNormalized, email);`
  - → Write/read security audit events.
` 250`  ``
` 251`  `                return new AuthResult`
` 252`  `                {`
` 253`  `                    Success = true,`
` 254`  `                    Message = "Account created as " + roleNormalized + ". Sign in with your password and authenticator.",`
` 255`  `                    User = new AuthUser`
` 256`  `                    {`
` 257`  `                        UID = uid,`
` 258`  `                        Name = name,`
` 259`  `                        Email = email,`
` 260`  `                        Role = roleCode,`
` 261`  `                        RoleNormalized = roleNormalized,`
` 262`  `                        MfaEnabled = true,`
` 263`  `                        MfaSecret = mfaSecret`
` 264`  `                    }`
` 265`  `                };`
` 266`  `            }`
` 267`  `        }`
` 268`  ``
` 269`  `        /// <summary>True if Session still has an unfinished registration (no DB row yet).</summary>`
` 270`  `        public static bool HasPendingRegistration(HttpContext ctx)`
  - → Pending registration in Session until MFA confirmed.
` 271`  `        {`
` 272`  `            string name, email, hash, roleCode, roleNormalized, secret;`
` 273`  `            DateTime at;`
` 274`  `            return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out secret, out at);`
  - → Pending registration in Session until MFA confirmed.
` 275`  `        }`
` 276`  ``
` 277`  `        /// <summary>Email + MFA secret for QR while registration is pending in Session.</summary>`
` 278`  `        public static bool TryGetPendingMfaSetup(HttpContext ctx, out string email, out string mfaSecret)`
` 279`  `        {`
` 280`  `            string name, hash, roleCode, roleNormalized;`
` 281`  `            DateTime at;`
` 282`  `            return TryReadPendingRegistration(ctx, out name, out email, out hash, out roleCode, out roleNormalized, out mfaSecret, out at);`
  - → Pending registration in Session until MFA confirmed.
` 283`  `        }`
` 284`  ``
` 285`  `        public static void ClearPendingRegistration(HttpContext ctx)`
  - → Pending registration in Session until MFA confirmed.
` 286`  `        {`
` 287`  `            try`
  - → Error handling block.
` 288`  `            {`
` 289`  `                if (ctx == null || ctx.Session == null) return;`
` 290`  `                ctx.Session.Remove(SessRegName);`
  - → Pending registration in Session until MFA confirmed.
` 291`  `                ctx.Session.Remove(SessRegEmail);`
  - → Pending registration in Session until MFA confirmed.
` 292`  `                ctx.Session.Remove(SessRegHash);`
  - → Pending registration in Session until MFA confirmed.
` 293`  `                ctx.Session.Remove(SessRegRole);`
  - → Pending registration in Session until MFA confirmed.
` 294`  `                ctx.Session.Remove(SessRegRoleName);`
  - → Pending registration in Session until MFA confirmed.
` 295`  `                ctx.Session.Remove(SessRegSecret);`
  - → Pending registration in Session until MFA confirmed.
` 296`  `                ctx.Session.Remove(SessRegAt);`
  - → Pending registration in Session until MFA confirmed.
` 297`  `            }`
` 298`  `            catch { }`
  - → Handle/log exception.
` 299`  `        }`
` 300`  ``
` 301`  `        private static bool TryReadPendingRegistration(`
  - → Pending registration in Session until MFA confirmed.
` 302`  `            HttpContext ctx,`
` 303`  `            out string name, out string email, out string hash,`
` 304`  `            out string roleCode, out string roleNormalized, out string secret, out DateTime createdUtc)`
` 305`  `        {`
` 306`  `            name = email = hash = roleCode = roleNormalized = secret = null;`
` 307`  `            createdUtc = DateTime.MinValue;`
` 308`  `            if (ctx == null || ctx.Session == null) return false;`
` 309`  `            try`
  - → Error handling block.
` 310`  `            {`
` 311`  `                name = ctx.Session[SessRegName] as string;`
  - → Server session for logged-in user.
` 312`  `                email = ctx.Session[SessRegEmail] as string;`
  - → Server session for logged-in user.
` 313`  `                hash = ctx.Session[SessRegHash] as string;`
  - → Server session for logged-in user.
` 314`  `                roleCode = ctx.Session[SessRegRole] as string;`
  - → Server session for logged-in user.
` 315`  `                roleNormalized = ctx.Session[SessRegRoleName] as string;`
  - → Server session for logged-in user.
` 316`  `                secret = ctx.Session[SessRegSecret] as string;`
  - → Server session for logged-in user.
` 317`  `                if (ctx.Session[SessRegAt] is DateTime)`
  - → Server session for logged-in user.
` 318`  `                    createdUtc = (DateTime)ctx.Session[SessRegAt];`
  - → Server session for logged-in user.
` 319`  `                else`
` 320`  `                    return false;`
` 321`  ``
` 322`  `                if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(email) ||`
` 323`  `                    string.IsNullOrEmpty(hash) || string.IsNullOrEmpty(secret))`
` 324`  `                    return false;`
` 325`  `                return true;`
` 326`  `            }`
` 327`  `            catch { return false; }`
  - → Handle/log exception.
` 328`  `        }`
` 329`  ``
` 330`  `        /// <summary>Legacy name — starts pending registration only (no insert until FinishRegistration).</summary>`
` 331`  `        public static AuthResult Register(string name, string email, string password, bool enableMfa, string roleChoice = "Student")`
` 332`  `        {`
` 333`  `            return StartRegistration(HttpContext.Current, name, email, password, roleChoice);`
  - → Pending registration in Session until MFA confirmed.
` 334`  `        }`
` 335`  ``
` 336`  `        /// <summary>`
` 337`  `        /// Step 1 of login: password check. If MFA on, does not issue session yet.`
` 338`  `        /// </summary>`
` 339`  `        public static AuthResult LoginPassword(string email, string password)`
` 340`  `        {`
` 341`  `            AuthSchema.Ensure();`
` 342`  `            email = (email ?? "").Trim().ToLowerInvariant();`
` 343`  `            password = password ?? "";`
` 344`  `            var ctx = HttpContext.Current;`
` 345`  ``
` 346`  `            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))`
` 347`  `                return Fail("Email and password are required.");`
` 348`  ``
` 349`  `            string lockMsg;`
` 350`  `            if (LoginThrottle.IsLocked(email, ctx, out lockMsg))`
  - → Brute-force lockout tracking.
` 351`  `                return Fail(lockMsg);`
` 352`  ``
` 353`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 354`  `            {`
` 355`  `                AuthUser user = LoadUserByEmail(conn, email);`
` 356`  `                if (user == null)`
` 357`  `                {`
` 358`  `                    LoginThrottle.RegisterFailure(email, ctx);`
  - → Brute-force lockout tracking.
` 359`  `                    SecurityAudit.Log("login.fail", null, "Unknown email", email);`
  - → Write/read security audit events.
` 360`  `                    return Fail("Invalid email or password.");`
` 361`  `                }`
` 362`  ``
` 363`  `                string stored = !string.IsNullOrEmpty(user.PasswordHash)`
` 364`  `                    ? user.PasswordHash`
` 365`  `                    : user.PasswordStored;`
` 366`  ``
` 367`  `                if (!PasswordHasher.Verify(password, stored))`
  - → Password hashing (PBKDF2).
` 368`  `                {`
` 369`  `                    LoginThrottle.RegisterFailure(email, ctx);`
  - → Brute-force lockout tracking.
` 370`  `                    SecurityAudit.Log("login.fail", user.UID, "Bad password", email);`
  - → Write/read security audit events.
` 371`  `                    return Fail("Invalid email or password.");`
` 372`  `                }`
` 373`  ``
` 374`  `                LoginThrottle.RegisterSuccess(email, ctx);`
  - → Brute-force lockout tracking.
` 375`  ``
` 376`  `                // Upgrade plain-text → hash on successful login`
` 377`  `                if (!PasswordHasher.IsHashed(stored))`
  - → Password hashing (PBKDF2).
` 378`  `                {`
` 379`  `                    string newHash = PasswordHasher.Hash(password);`
  - → Password hashing (PBKDF2).
` 380`  `                    try`
  - → Error handling block.
` 381`  `                    {`
` 382`  `                        Exec(conn, "UPDATE Users SET Password=@P, PasswordHash=@H WHERE UID=@UID",`
` 383`  `                        P("@P", newHash), P("@H", newHash), P("@UID", user.UID));`
` 384`  `                    }`
` 385`  `                    catch`
  - → Handle/log exception.
` 386`  `                    {`
` 387`  `                        try`
  - → Error handling block.
` 388`  `                        {`
` 389`  `                            Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",`
` 390`  `                            P("@P", newHash), P("@UID", user.UID));`
` 391`  `                        }`
` 392`  `                        catch { }`
  - → Handle/log exception.
` 393`  `                    }`
` 394`  `                }`
` 395`  ``
` 396`  `                user.RoleNormalized = NormalizeRole(user.Role);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 397`  ``
` 398`  `                // Admin: password only (no MFA). Student/Lecturer still require authenticator.`
` 399`  `                if (string.Equals(user.RoleNormalized, "Admin", StringComparison.OrdinalIgnoreCase))`
` 400`  `                {`
` 401`  `                    string adminToken = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);`
  - → JWT cookie create/validate/clear.
` 402`  `                    SecurityAudit.Log("login.ok", user.UID, "Admin MFA bypass", email);`
  - → Write/read security audit events.
` 403`  `                    return new AuthResult`
` 404`  `                    {`
` 405`  `                        Success = true,`
` 406`  `                        RequiresMfa = false,`
` 407`  `                        Message = "Signed in as Admin.",`
` 408`  `                        User = user,`
` 409`  `                        Token = adminToken`
` 410`  `                    };`
` 411`  `                }`
` 412`  ``
` 413`  `                // Student / Lecturer: MFA required`
` 414`  `                if (string.IsNullOrEmpty(user.MfaSecret))`
` 415`  `                {`
` 416`  `                    return Fail(`
` 417`  `                        "This account has no authenticator set up. Register a new account with MFA, " +`
` 418`  `                        "or ask an admin to reset MFA for you.");`
` 419`  `                }`
` 420`  ``
` 421`  `                return new AuthResult`
` 422`  `                {`
` 423`  `                    Success = true,`
` 424`  `                    RequiresMfa = true,`
` 425`  `                    MfaMethod = "totp",`
` 426`  `                    Message = "Enter the 6-digit code from your authenticator app.",`
` 427`  `                    User = user`
` 428`  `                };`
` 429`  `            }`
` 430`  `        }`
` 431`  ``
` 432`  `        public static AuthResult VerifyMfa(int uid, string code, string method)`
  - → Verify multi-factor / TOTP code.
` 433`  `        {`
` 434`  `            AuthSchema.Ensure();`
` 435`  `            code = (code ?? "").Trim();`
` 436`  `            if (uid <= 0 || string.IsNullOrEmpty(code))`
` 437`  `            return Fail("Verification code is required.");`
` 438`  ``
` 439`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 440`  `            {`
` 441`  `                AuthUser user = LoadUserById(conn, uid);`
` 442`  `                if (user == null) return Fail("Session expired. Sign in again.");`
` 443`  ``
` 444`  `                bool ok = false;`
` 445`  `                if (string.Equals(method, "email", StringComparison.OrdinalIgnoreCase))`
` 446`  `                {`
` 447`  `                    try`
  - → Error handling block.
` 448`  `                    {`
` 449`  `                        using (var cmd = new SqlCommand(`
  - → Import namespace/types.
` 450`  `                        "SELECT EmailOtp, EmailOtpExpiry FROM Users WHERE UID=@UID", conn))`
` 451`  `                        {`
` 452`  `                            cmd.Parameters.AddWithValue("@UID", uid);`
` 453`  `                            using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 454`  `                            {`
` 455`  `                                if (r.Read())`
` 456`  `                                {`
` 457`  `                                    string otp = r["EmailOtp"] == DBNull.Value ? null : r["EmailOtp"].ToString();`
` 458`  `                                    DateTime? exp = r["EmailOtpExpiry"] == DBNull.Value`
` 459`  `                                    ? (DateTime?)null`
` 460`  `                                    : Convert.ToDateTime(r["EmailOtpExpiry"]);`
` 461`  `                                    ok = otp != null && exp.HasValue && exp.Value > DateTime.UtcNow`
` 462`  `                                    && string.Equals(otp, code, StringComparison.Ordinal);`
` 463`  `                                }`
` 464`  `                            }`
` 465`  `                        }`
` 466`  `                        if (ok)`
` 467`  `                        {`
` 468`  `                            Exec(conn, "UPDATE Users SET EmailOtp=NULL, EmailOtpExpiry=NULL WHERE UID=@UID",`
` 469`  `                            P("@UID", uid));`
` 470`  `                        }`
` 471`  `                    }`
` 472`  `                    catch { ok = false; }`
  - → Handle/log exception.
` 473`  `                }`
` 474`  `                else`
` 475`  `                {`
` 476`  `                    // TOTP (Google Authenticator) — same helper + window as password reset`
` 477`  `                    string secret = TotpHelper.NormalizeSecret(user.MfaSecret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 478`  `                    if (string.IsNullOrEmpty(secret))`
` 479`  `                        return Fail("MFA is not configured for this account. Register again with MFA, or contact admin.");`
` 480`  `                    ok = TotpHelper.VerifyCode(secret, code);`
  - → TOTP / authenticator (RFC 6238) helper.
` 481`  `                }`
` 482`  ``
` 483`  `                if (!ok)`
` 484`  `                {`
` 485`  `                    LoginThrottle.RegisterFailure(user.Email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 486`  `                    return Fail("Invalid or expired verification code. Use the latest 6-digit code from the app (codes refresh every 30 seconds). Check that your phone time is set automatically.");`
` 487`  `                }`
` 488`  ``
` 489`  `                LoginThrottle.RegisterSuccess(user.Email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 490`  `                user.RoleNormalized = NormalizeRole(user.Role);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 491`  `                string token = JwtHelper.CreateToken(user.UID, user.Name, user.RoleNormalized);`
  - → JWT cookie create/validate/clear.
` 492`  `                return new AuthResult`
` 493`  `                {`
` 494`  `                    Success = true,`
` 495`  `                    User = user,`
` 496`  `                    Token = token,`
` 497`  `                    Message = "OK"`
` 498`  `                };`
` 499`  `            }`
` 500`  `        }`
` 501`  ``
` 502`  `        public static void CompleteLogin(HttpContext ctx, AuthUser user, string token)`
  - → Issue Session + JWT after successful auth.
` 503`  `        {`
` 504`  `            if (ctx == null || user == null) return;`
` 505`  `            // Always store as int so Course.LecturerUID FK gets a real UID`
` 506`  `            ctx.Session["UserID"] = user.UID;`
  - → Server session for logged-in user.
` 507`  `            ctx.Session["UserName"] = user.Name ?? "";`
  - → Server session for logged-in user.
` 508`  `            ctx.Session["UserRole"] = user.RoleNormalized ?? NormalizeRole(user.Role);`
  - → Server session for logged-in user.
` 509`  `            ctx.Session["AuthToken"] = token;`
  - → Server session for logged-in user.
` 510`  `            JwtHelper.SetAuthCookie(ctx.Response, token);`
  - → JWT cookie create/validate/clear.
` 511`  `            try { CsrfProtection.EnsureToken(ctx); } catch { }`
  - → CSRF anti-forgery protection.
` 512`  `            SecurityAudit.Log("login.ok", user.UID, "Role=" + (user.RoleNormalized ?? NormalizeRole(user.Role)), user.Email);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 513`  `        }`
` 514`  ``
` 515`  `        public static void Logout(HttpContext ctx)`
` 516`  `        {`
` 517`  `            if (ctx == null) return;`
` 518`  `            int? uid = null;`
` 519`  `            string email = null;`
` 520`  `            try`
  - → Error handling block.
` 521`  `            {`
` 522`  `                if (ctx.Session != null && ctx.Session["UserID"] != null)`
  - → Server session for logged-in user.
` 523`  `                    uid = Convert.ToInt32(ctx.Session["UserID"]);`
  - → Server session for logged-in user.
` 524`  `                email = ctx.Session != null ? ctx.Session["UserName"] as string : null;`
  - → Server session for logged-in user.
` 525`  `            }`
` 526`  `            catch { }`
  - → Handle/log exception.
` 527`  `            SecurityAudit.Log("logout", uid, null, email);`
  - → Write/read security audit events.
` 528`  `            try`
  - → Error handling block.
` 529`  `            {`
` 530`  `                ctx.Session.Clear();`
` 531`  `                ctx.Session.Abandon();`
` 532`  `            }`
` 533`  `            catch { }`
  - → Handle/log exception.
` 534`  `            JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 535`  `        }`
` 536`  ``
` 537`  ``
` 538`  `        /// <summary>`
` 539`  `        /// Step 1 — verify email + Google Authenticator TOTP only (no password change yet).`
` 540`  `        /// </summary>`
` 541`  `        public static AuthResult VerifyMfaForPasswordReset(string email, string totpCode)`
  - → Verify multi-factor / TOTP code.
` 542`  `        {`
` 543`  `            AuthSchema.Ensure();`
` 544`  `            email = (email ?? "").Trim().ToLowerInvariant();`
` 545`  `            totpCode = (totpCode ?? "").Trim();`
` 546`  ``
` 547`  `            if (string.IsNullOrEmpty(email) || !email.Contains("@"))`
` 548`  `                return Fail("Enter a valid email address.");`
` 549`  `            if (string.IsNullOrEmpty(totpCode))`
` 550`  `                return Fail("Enter the 6-digit code from your authenticator app.");`
` 551`  ``
` 552`  `            string lockMsg;`
` 553`  `            if (LoginThrottle.IsLocked(email, HttpContext.Current, out lockMsg))`
  - → Brute-force lockout tracking.
` 554`  `                return Fail(lockMsg);`
` 555`  ``
` 556`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 557`  `            {`
` 558`  `                AuthUser user = LoadUserByEmail(conn, email);`
` 559`  `                string bad = "Invalid email or authenticator code.";`
` 560`  `                if (user == null)`
` 561`  `                {`
` 562`  `                    LoginThrottle.RegisterFailure(email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 563`  `                    SecurityAudit.Log("password.reset.fail", null, "Unknown email", email);`
  - → Write/read security audit events.
` 564`  `                    return Fail(bad);`
` 565`  `                }`
` 566`  ``
` 567`  `                string secret = TotpHelper.NormalizeSecret(user.MfaSecret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 568`  `                if (string.IsNullOrEmpty(secret))`
` 569`  `                {`
` 570`  `                    SecurityAudit.Log("password.reset.fail", user.UID, "No MFA secret", email);`
  - → Write/read security audit events.
` 571`  `                    return Fail(`
` 572`  `                        "This account has no authenticator linked. Register a new account (MFA required) or contact an admin.");`
` 573`  `                }`
` 574`  ``
` 575`  `                // Same algorithm + window as login MFA (TotpHelper default ±2 min)`
` 576`  `                if (!TotpHelper.VerifyCode(secret, totpCode))`
  - → TOTP / authenticator (RFC 6238) helper.
` 577`  `                {`
` 578`  `                    LoginThrottle.RegisterFailure(email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 579`  `                    SecurityAudit.Log("password.reset.fail", user.UID, "Bad TOTP", email);`
  - → Write/read security audit events.
` 580`  ``
` 581`  `                    string msg =`
` 582`  `                        "Invalid authenticator code for this account. " +`
` 583`  `                        "Login and password-reset use the same secret from the database. ";`
` 584`  ``
` 585`  `                    // When debug is on, show what the SERVER secret expects right now so you can`
` 586`  `                    // compare with Google Authenticator (mismatch = wrong/old QR entry or DB reset).`
` 587`  `                    if (IsMfaDebugEnabled())`
  - → Debug-only TOTP leak switch (must stay false for demos).
` 588`  `                    {`
` 589`  `                        try`
  - → Error handling block.
` 590`  `                        {`
` 591`  `                            string expected = TotpHelper.GenerateCode(secret);`
  - → TOTP / authenticator (RFC 6238) helper.
` 592`  `                            string you = TotpHelper.NormalizeCode(totpCode);`
  - → TOTP / authenticator (RFC 6238) helper.
` 593`  `                            msg +=`
` 594`  `                                "<br/><br/><strong>Debug (local only)</strong><br/>" +`
` 595`  `                                "Server expects right now: <strong style=\"letter-spacing:.2em\">" + expected + "</strong><br/>" +`
` 596`  `                                "You entered: <strong style=\"letter-spacing:.2em\">" +`
` 597`  `                                System.Web.HttpUtility.HtmlEncode(you) + "</strong><br/>" +`
  - → Encode text to reduce XSS risk.
` 598`  `                                "Secret length in DB: " + secret.Length +`
` 599`  `                                " (fingerprint " + secret.Substring(0, Math.Min(4, secret.Length)) + "…" +`
` 600`  `                                secret.Substring(Math.Max(0, secret.Length - 4)) + ")<br/>" +`
` 601`  `                                "If the numbers differ, your app entry is for a <em>different</em> secret " +`
` 602`  `                                "(old QR / re-registered account / DB reseed). Delete the EduLMS row in " +`
` 603`  `                                "Authenticator and register again, scanning the new QR.";`
` 604`  `                        }`
` 605`  `                        catch`
  - → Handle/log exception.
` 606`  `                        {`
` 607`  `                            msg += " (Could not generate debug code — secret may be corrupt.)";`
` 608`  `                        }`
` 609`  `                    }`
` 610`  `                    else`
` 611`  `                    {`
` 612`  `                        msg +=`
` 613`  `                            "If your app code never matches: delete the old EduLMS entry in Google Authenticator, " +`
` 614`  `                            "register a new account, and scan the new QR. Phone time must be set to automatic.";`
` 615`  `                    }`
` 616`  ``
` 617`  `                    return Fail(msg);`
` 618`  `                }`
` 619`  ``
` 620`  `                LoginThrottle.RegisterSuccess(email, HttpContext.Current);`
  - → Brute-force lockout tracking.
` 621`  `                SecurityAudit.Log("password.reset.mfa_ok", user.UID, "MFA verified for reset", email);`
  - → Write/read security audit events.
` 622`  `                user.RoleNormalized = NormalizeRole(user.Role);`
  - → Map role codes/names to Admin/Student/Lecturer.
` 623`  `                return new AuthResult`
` 624`  `                {`
` 625`  `                    Success = true,`
` 626`  `                    Message = "Authenticator verified. Choose a new password.",`
` 627`  `                    User = user`
` 628`  `                };`
` 629`  `            }`
` 630`  `        }`
` 631`  ``
` 632`  `        /// <summary>`
` 633`  `        /// Step 2 — set new password after MFA was verified (session holds UID).`
` 634`  `        /// </summary>`
` 635`  `        public static AuthResult CompletePasswordReset(int uid, string newPassword)`
  - → Password-reset MFA then update password hash.
` 636`  `        {`
` 637`  `            AuthSchema.Ensure();`
` 638`  `            newPassword = newPassword ?? "";`
` 639`  `            if (uid <= 0) return Fail("Session expired. Verify MFA again.");`
` 640`  `            if (newPassword.Length < 8) return Fail("Password must be at least 8 characters.");`
` 641`  `            if (!HasComplexity(newPassword)) return Fail("Password needs letters and numbers.");`
` 642`  ``
` 643`  `            using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 644`  `            {`
` 645`  `                AuthUser user = LoadUserById(conn, uid);`
` 646`  `                if (user == null) return Fail("Account not found. Start again.");`
` 647`  ``
` 648`  `                string newHash = PasswordHasher.Hash(newPassword);`
  - → Password hashing (PBKDF2).
` 649`  `                try`
  - → Error handling block.
` 650`  `                {`
` 651`  `                    Exec(conn, @"`
` 652`  `UPDATE Users SET Password=@P, PasswordHash=@H, PasswordResetToken=NULL, PasswordResetExpiry=NULL`
` 653`  `WHERE UID=@UID",`
` 654`  `                        P("@P", newHash), P("@H", newHash), P("@UID", uid));`
` 655`  `                }`
` 656`  `                catch`
  - → Handle/log exception.
` 657`  `                {`
` 658`  `                    try`
  - → Error handling block.
` 659`  `                    {`
` 660`  `                        Exec(conn, "UPDATE Users SET Password=@P WHERE UID=@UID",`
` 661`  `                            P("@P", newHash), P("@UID", uid));`
` 662`  `                    }`
` 663`  `                    catch`
  - → Handle/log exception.
` 664`  `                    {`
` 665`  `                        return Fail("Could not update password.");`
` 666`  `                    }`
` 667`  `                }`
` 668`  ``
` 669`  `                try { Exec(conn, "UPDATE Users SET MfaEnabled=1 WHERE UID=@UID", P("@UID", uid)); }`
  - → Error handling block.
` 670`  `                catch { }`
  - → Handle/log exception.
` 671`  ``
` 672`  `                SecurityAudit.Log("password.reset.ok", uid, "after MFA step", user.Email);`
  - → Write/read security audit events.
` 673`  `                return new AuthResult`
` 674`  `                {`
` 675`  `                    Success = true,`
` 676`  `                    Message = "Password updated. Sign in with your new password and authenticator code."`
` 677`  `                };`
` 678`  `            }`
` 679`  `        }`
` 680`  ``
` 681`  `        /// <summary>One-shot: verify TOTP then set password (ResetPassword.aspx).</summary>`
` 682`  `        public static AuthResult ResetPasswordWithTotp(string email, string totpCode, string newPassword)`
` 683`  `        {`
` 684`  `            var v = VerifyMfaForPasswordReset(email, totpCode);`
  - → Verify multi-factor / TOTP code.
` 685`  `            if (!v.Success || v.User == null) return v;`
` 686`  `            return CompletePasswordReset(v.User.UID, newPassword);`
  - → Password-reset MFA then update password hash.
` 687`  `        }`
` 688`  ``
` 689`  `        /// <summary>Legacy name — delegates to TOTP-based reset.</summary>`
` 690`  `        public static AuthResult ResetPasswordWithCode(string email, string code, string newPassword)`
` 691`  `        {`
` 692`  `            return ResetPasswordWithTotp(email, code, newPassword);`
` 693`  `        }`
` 694`  ``
` 695`  `        /// <summary>Deprecated: password reset no longer issues email codes.</summary>`
` 696`  `        public static AuthResult RequestPasswordReset(string email)`
` 697`  `        {`
` 698`  `            return new AuthResult`
` 699`  `            {`
` 700`  `                Success = true,`
` 701`  `                Message = "Use your authenticator app code on the reset page (no email is sent)."`
` 702`  `            };`
` 703`  `        }`
` 704`  ``
` 705`  `                /// <summary>True if Users.UID exists (needed for Courses.LecturerUID FK).</summary>`
` 706`  `        public static bool UserExists(int uid)`
` 707`  `        {`
` 708`  `            if (uid <= 0) return false;`
` 709`  `            try`
  - → Error handling block.
` 710`  `            {`
` 711`  `                using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 712`  `                {`
` 713`  `                    object o = Scalar(conn, "SELECT COUNT(1) FROM Users WHERE UID = @UID", P("@UID", uid));`
` 714`  `                    return o != null && Convert.ToInt32(o) > 0;`
` 715`  `                }`
` 716`  `            }`
` 717`  `            catch`
  - → Handle/log exception.
` 718`  `            {`
` 719`  `                return false;`
` 720`  `            }`
` 721`  `        }`
` 722`  ``
` 723`  `        /// <summary>`
` 724`  `        /// Returns a session UID that exists in dbo.Users, or 0.`
` 725`  `        /// Clears stale JWT/session when the user row is missing (e.g. after DB reset).`
` 726`  `        /// </summary>`
` 727`  `        public static int GetValidatedUserId(HttpContext ctx)`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
` 728`  `        {`
` 729`  `            if (ctx == null || ctx.Session == null) return 0;`
` 730`  ``
` 731`  `            TryRestoreSessionFromJwt(ctx);`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
` 732`  ``
` 733`  `            if (ctx.Session["UserID"] == null) return 0;`
  - → Server session for logged-in user.
` 734`  `            int uid;`
` 735`  `            try { uid = Convert.ToInt32(ctx.Session["UserID"]); }`
  - → Server session for logged-in user.
` 736`  `            catch { return 0; }`
  - → Handle/log exception.
` 737`  ``
` 738`  `            if (uid > 0 && UserExists(uid))`
` 739`  `            return uid;`
` 740`  ``
` 741`  `            // Stale session/JWT - user not in current EduDB`
` 742`  `            try`
  - → Error handling block.
` 743`  `            {`
` 744`  `                ctx.Session.Remove("UserID");`
` 745`  `                ctx.Session.Remove("UserName");`
` 746`  `                ctx.Session.Remove("UserRole");`
` 747`  `                ctx.Session.Remove("AuthToken");`
` 748`  `            }`
` 749`  `            catch { }`
  - → Handle/log exception.
` 750`  `            JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 751`  `            return 0;`
` 752`  `        }`
` 753`  ``
` 754`  `        /// <summary>Restore session from JWT cookie if session expired; re-check Users table.</summary>`
` 755`  `        public static bool TryRestoreSessionFromJwt(HttpContext ctx)`
  - → Restore/validate user from Session or JWT; reject stale UIDs.
` 756`  `        {`
` 757`  `            if (ctx == null || ctx.Session == null) return false;`
` 758`  ``
` 759`  `            // Existing session: ensure UID still exists in this database`
` 760`  `            if (ctx.Session["UserID"] != null)`
  - → Server session for logged-in user.
` 761`  `            {`
` 762`  `                int existing;`
` 763`  `                try { existing = Convert.ToInt32(ctx.Session["UserID"]); }`
  - → Server session for logged-in user.
` 764`  `                catch { existing = 0; }`
  - → Handle/log exception.
` 765`  `                if (existing > 0 && UserExists(existing))`
` 766`  `                return true;`
` 767`  `                // Bad/stale session id - fall through and try cookie, else clear`
` 768`  `                try`
  - → Error handling block.
` 769`  `                {`
` 770`  `                    ctx.Session.Remove("UserID");`
` 771`  `                    ctx.Session.Remove("UserName");`
` 772`  `                    ctx.Session.Remove("UserRole");`
` 773`  `                }`
` 774`  `                catch { }`
  - → Handle/log exception.
` 775`  `            }`
` 776`  ``
` 777`  `            string token = JwtHelper.ReadToken(ctx.Request);`
  - → JWT cookie create/validate/clear.
` 778`  `            int uid;`
` 779`  `            string name, role;`
` 780`  `            if (!JwtHelper.TryValidate(token, out uid, out name, out role))`
  - → JWT cookie create/validate/clear.
` 781`  `            {`
` 782`  `                JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 783`  `                return false;`
` 784`  `            }`
` 785`  ``
` 786`  `            // Reject JWT for users that no longer exist (MDF replaced / reseeded)`
` 787`  `            if (!UserExists(uid))`
` 788`  `            {`
` 789`  `                JwtHelper.ClearAuthCookie(ctx.Response);`
  - → JWT cookie create/validate/clear.
` 790`  `                return false;`
` 791`  `            }`
` 792`  ``
` 793`  `            // Prefer live name/role from DB over token claims`
` 794`  `            try`
  - → Error handling block.
` 795`  `            {`
` 796`  `                using (var conn = DbHelper.OpenConnection())`
  - → Import namespace/types.
` 797`  `                {`
` 798`  `                    using (var cmd = new SqlCommand(`
  - → Import namespace/types.
` 799`  `                    "SELECT Name, Role FROM Users WHERE UID=@UID", conn))`
` 800`  `                    {`
` 801`  `                        cmd.Parameters.AddWithValue("@UID", uid);`
` 802`  `                        using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 803`  `                        {`
` 804`  `                            if (r.Read())`
` 805`  `                            {`
` 806`  `                                name = r["Name"] == DBNull.Value ? name : r["Name"].ToString();`
` 807`  `                                role = NormalizeRole(r["Role"] == DBNull.Value ? role : r["Role"].ToString());`
  - → Map role codes/names to Admin/Student/Lecturer.
` 808`  `                            }`
` 809`  `                        }`
` 810`  `                    }`
` 811`  `                }`
` 812`  `            }`
` 813`  `            catch { /* keep token claims */ }`
  - → Handle/log exception.
` 814`  ``
` 815`  `            ctx.Session["UserID"] = uid;`
  - → Server session for logged-in user.
` 816`  `            ctx.Session["UserName"] = name ?? "";`
  - → Server session for logged-in user.
` 817`  `            ctx.Session["UserRole"] = role ?? "Student";`
  - → Server session for logged-in user.
` 818`  `            ctx.Session["AuthToken"] = token;`
  - → Server session for logged-in user.
` 819`  `            return true;`
` 820`  `        }`
` 821`  ``
` 822`  `        public static string NormalizeRole(string role)`
  - → Map role codes/names to Admin/Student/Lecturer.
` 823`  `        {`
` 824`  `            if (string.IsNullOrWhiteSpace(role)) return "Student";`
` 825`  `            var r = role.Trim().ToLowerInvariant();`
` 826`  `            if (r == "0" || r == "admin" || r == "administrator") return "Admin";`
` 827`  `            if (r == "2" || r == "teacher" || r == "lecturer") return "Lecturer";`
` 828`  `            return "Student";`
` 829`  `        }`
` 830`  ``
` 831`  `        private static bool HasComplexity(string password)`
` 832`  `        {`
` 833`  `            bool letter = false, digit = false;`
` 834`  `            foreach (char c in password)`
` 835`  `            {`
` 836`  `                if (char.IsLetter(c)) letter = true;`
` 837`  `                if (char.IsDigit(c)) digit = true;`
` 838`  `            }`
` 839`  `            return letter && digit;`
` 840`  `        }`
` 841`  ``
` 842`  `        private static AuthUser LoadUserByEmail(SqlConnection conn, string email)`
  - → Database access (pure SQL).
` 843`  `        {`
` 844`  `            // Prefer extended columns; fall back`
` 845`  `            try`
  - → Error handling block.
` 846`  `            {`
` 847`  `                using (var cmd = new SqlCommand(@"`
  - → Import namespace/types.
` 848`  `                SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret`
` 849`  `                FROM Users WHERE Email = @Email", conn))`
` 850`  `                {`
` 851`  `                    cmd.Parameters.AddWithValue("@Email", email);`
` 852`  `                    using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 853`  `                    {`
` 854`  `                        if (!r.Read()) return null;`
` 855`  `                        return MapUser(r);`
` 856`  `                    }`
` 857`  `                }`
` 858`  `            }`
` 859`  `            catch`
  - → Handle/log exception.
` 860`  `            {`
` 861`  `                using (var cmd = new SqlCommand(@"`
  - → Import namespace/types.
` 862`  `                SELECT UID, Name, Email, Role, Password FROM Users WHERE Email = @Email", conn))`
` 863`  `                {`
` 864`  `                    cmd.Parameters.AddWithValue("@Email", email);`
` 865`  `                    using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 866`  `                    {`
` 867`  `                        if (!r.Read()) return null;`
` 868`  `                        return new AuthUser`
` 869`  `                        {`
` 870`  `                            UID = Convert.ToInt32(r["UID"]),`
` 871`  `                            Name = r["Name"] == DBNull.Value ? "" : r["Name"].ToString(),`
` 872`  `                            Email = r["Email"] == DBNull.Value ? "" : r["Email"].ToString(),`
` 873`  `                            Role = r["Role"] == DBNull.Value ? "1" : r["Role"].ToString(),`
` 874`  `                            PasswordStored = r["Password"] == DBNull.Value ? "" : r["Password"].ToString(),`
` 875`  `                            MfaEnabled = false`
` 876`  `                        };`
` 877`  `                    }`
` 878`  `                }`
` 879`  `            }`
` 880`  `        }`
` 881`  ``
` 882`  `        private static AuthUser LoadUserById(SqlConnection conn, int uid)`
  - → Database access (pure SQL).
` 883`  `        {`
` 884`  `            try`
  - → Error handling block.
` 885`  `            {`
` 886`  `                using (var cmd = new SqlCommand(@"`
  - → Import namespace/types.
` 887`  `                SELECT UID, Name, Email, Role, Password, PasswordHash, MfaEnabled, MfaSecret`
` 888`  `                FROM Users WHERE UID = @UID", conn))`
` 889`  `                {`
` 890`  `                    cmd.Parameters.AddWithValue("@UID", uid);`
` 891`  `                    using (var r = cmd.ExecuteReader())`
  - → Import namespace/types.
` 892`  `                    {`
` 893`  `                        if (!r.Read()) return null;`
` 894`  `                        return MapUser(r);`
` 895`  `                    }`
` 896`  `                }`
` 897`  `            }`
` 898`  `            catch`
  - → Handle/log exception.
` 899`  `            {`
` 900`  `                using (var cmd = new SqlCommand(`
  - → Import namespace/types.

_… truncated: 127 more lines in source. Open the original file for the rest._

## Source snapshot (raw)

_File has 1027 lines — raw dump omitted here to keep Markdown readable. Open `Data/Security/AuthService.cs` in the project._
