# Security overview — EduLMS

**Generated for:** `/home/loke/Documents/WebAppFuntionExplain`  
**Source:** `Data/Security/*` + `Pages/Authentication/*` + `Shared/Scripts/csrf.js`

---

## Flow diagrams

### Register (MFA required before account exists)

```
[Register form]  name, email, password, Student|Lecturer
       │
       ▼
AuthService.StartRegistration
  • validate complexity / email free
  • PasswordHasher.Hash(password)
  • TotpHelper.GenerateSecret()
  • store ONLY in Session (Reg.Name, Reg.Email, …)
  • NO INSERT into Users yet
       │
       ▼
[QR + manual key]  TotpHelper.BuildOtpAuthUri
       │
       ▼
User enters 6-digit code from Google Authenticator
       │
       ▼
AuthService.FinishRegistration
  • TotpHelper.VerifyCode
  • INSERT Users (hash, MfaSecret, MfaEnabled=1)
  • clear Session pending
       │
       ▼
[Done] → Login
```

If the browser is closed before MFA confirm → **no account** in the database.

### Login

```
[Login] email + password
       │
       ▼
LoginThrottle.IsLocked? ──yes──► error (wait lockout)
       │ no
       ▼
AuthService.LoginPassword
  • load user by email
  • PasswordHasher.Verify
  • upgrade plain-text → hash if needed
       │
       ├─ Role = Admin ──► CompleteLogin (Session + JWT)  [no MFA]
       │
       └─ Student/Lecturer
              │
              ▼
         RequiresMfa = true
              │
              ▼
         [MfaVerify]  TotpHelper.VerifyCode
              │
              ▼
         CompleteLogin (Session + JWT cookie)
              │
              ▼
         Redirect by role (Admin / Lecturer / Student Landing)
```

### Forgot password (two steps)

```
Step 1: email + TOTP
  → AuthService.VerifyMfaForPasswordReset
  → Session: PwdResetUid / PwdResetEmail / PwdResetAt (10 min)

Step 2: new password + confirm
  → AuthService.CompletePasswordReset(uid, password)
  → update Password + PasswordHash; clear reset session
```

Admin accounts typically have no MFA secret → use Manage Users / known admin password for recovery demos (login bypasses MFA).

### Protected page / API request

```
Request
  → AuthService.TryRestoreSessionFromJwt (if Session empty)
  → AuthGate.EnsurePage / EnsureHandlerRole
  → if POST/AJAX: CsrfProtection.Validate
  → business logic (often LecturerUID ownership)
  → SecurityAudit.Log on sensitive actions
```

---

## Component map

| File | Responsibility |
|------|----------------|
| [Security__AuthService.cs.md](../06-Security-Core/Security__AuthService.cs.md) | Register, login, MFA, reset, session/JWT complete |
| [Security__AuthGate.cs.md](../06-Security-Core/Security__AuthGate.cs.md) | Role gate for pages + handlers + CSRF |
| [Security__PasswordHasher.cs.md](../06-Security-Core/Security__PasswordHasher.cs.md) | PBKDF2 hash/verify |
| [Security__JwtHelper.cs.md](../06-Security-Core/Security__JwtHelper.cs.md) | HS256 JWT + cookie |
| [Security__TotpHelper.cs.md](../06-Security-Core/Security__TotpHelper.cs.md) | TOTP generate/verify/QR URI |
| [Security__CsrfProtection.cs.md](../06-Security-Core/Security__CsrfProtection.cs.md) | Token + validation |
| [Security__LoginThrottle.cs.md](../06-Security-Core/Security__LoginThrottle.cs.md) | Brute-force lockout |
| [Security__SecurityAudit.cs.md](../06-Security-Core/Security__SecurityAudit.cs.md) | Audit log table + query |
| [Security__FileMagic.cs.md](../06-Security-Core/Security__FileMagic.cs.md) | Upload magic bytes |
| [Security__UploadPathGuard.cs.md](../06-Security-Core/Security__UploadPathGuard.cs.md) | Uploads path sandbox |
| [Security__AuthSchema.cs.md](../06-Security-Core/Security__AuthSchema.cs.md) | Ensure MFA/hash columns |

### Auth pages

| Page | Doc |
|------|-----|
| Login | [Auth__Login.aspx.cs.md](../07-Security-AuthPages/Auth__Login.aspx.cs.md) |
| Register | [Auth__Register.aspx.cs.md](../07-Security-AuthPages/Auth__Register.aspx.cs.md) |
| MFA verify | [Auth__MfaVerify.aspx.cs.md](../07-Security-AuthPages/Auth__MfaVerify.aspx.cs.md) |
| Forgot password | [Auth__ForgotPassword.aspx.cs.md](../07-Security-AuthPages/Auth__ForgotPassword.aspx.cs.md) |
| Reset password | [Auth__ResetPassword.aspx.cs.md](../07-Security-AuthPages/Auth__ResetPassword.aspx.cs.md) |
| Logout | [Auth__Logout.aspx.cs.md](../07-Security-AuthPages/Auth__Logout.aspx.cs.md) |
| csrf.js | [Scripts__csrf.js.md](../07-Security-AuthPages/Scripts__csrf.js.md) |

---

## Web.config security keys

| Key | Purpose |
|-----|---------|
| `JwtSecret` | HS256 signing key (must be long random) |
| `JwtExpiryHours` | Token lifetime |
| `JwtCookieSecure` | `auto` / HTTPS Secure flag |
| `LoginMaxFailures` | Failures before lockout (default 5) |
| `LoginLockoutMinutes` | Lock duration |
| `LoginWindowMinutes` | Failure window |
| `AllowSeedMockData` | Seed ashx on/off |
| `MfaDebug` | **Keep false** — never show server TOTP in demos |

---

## Role behaviour

| Role | Register | Login MFA | Notes |
|------|----------|-----------|--------|
| Student | Self-register + TOTP | Required | Landing after login |
| Lecturer | Self-register + TOTP | Required | Lecturer dashboard |
| Admin | Not self-register | **Bypassed** | Password only |

---

## Demo checklist (security)

1. Register Student/Lecturer → cancel before MFA → email must **not** exist in Users  
2. Complete MFA → login with password + **new** authenticator code  
3. Admin login without MFA page  
4. 5 wrong passwords → lockout message  
5. Forgot password: MFA step then new password  
6. DevTools: WebMethod POST has `X-CSRF-Token`  
7. Admin → Audit Log shows login/register/reset events  

---

## Related media security

Also documented under handlers:

- [Media_ashx.md](../04-Lecturer-Handlers/Media_ashx.md) — folder auth policy  
- [UploadMedia.ashx.md](../04-Lecturer-Handlers/UploadMedia.ashx.md) — authenticated uploads  

---

[← Back to full index](00-INDEX.md)
