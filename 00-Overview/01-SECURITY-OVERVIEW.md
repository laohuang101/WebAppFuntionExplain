# Security overview — EduLMS

**Docs:** `06-Security-Core/` + `07-Security-AuthPages/`

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
```

### Forgot password (two steps)

```
Step 1: email + TOTP
  → AuthService.VerifyMfaForPasswordReset
  → Session: PwdResetUid / PwdResetEmail / PwdResetAt (10 min)

Step 2: new password + confirm
  → AuthService.CompletePasswordReset(uid, password)
```

### Protected page / API

```
Request
  → AuthService.TryRestoreSessionFromJwt (if Session empty)
  → AuthGate.EnsurePage / EnsureHandlerRole
  → if POST/AJAX: CsrfProtection.Validate
  → business logic
  → SecurityAudit.Log on sensitive actions
```

---

## Component map

| File | Doc |
|------|-----|
| AuthService | [Security__AuthService.cs.md](../06-Security-Core/Security__AuthService.cs.md) |
| AuthGate | [Security__AuthGate.cs.md](../06-Security-Core/Security__AuthGate.cs.md) |
| PasswordHasher | [Security__PasswordHasher.cs.md](../06-Security-Core/Security__PasswordHasher.cs.md) |
| JwtHelper | [Security__JwtHelper.cs.md](../06-Security-Core/Security__JwtHelper.cs.md) |
| TotpHelper | [Security__TotpHelper.cs.md](../06-Security-Core/Security__TotpHelper.cs.md) |
| CsrfProtection | [Security__CsrfProtection.cs.md](../06-Security-Core/Security__CsrfProtection.cs.md) |
| LoginThrottle | [Security__LoginThrottle.cs.md](../06-Security-Core/Security__LoginThrottle.cs.md) |
| SecurityAudit | [Security__SecurityAudit.cs.md](../06-Security-Core/Security__SecurityAudit.cs.md) |
| FileMagic | [Security__FileMagic.cs.md](../06-Security-Core/Security__FileMagic.cs.md) |
| UploadPathGuard | [Security__UploadPathGuard.cs.md](../06-Security-Core/Security__UploadPathGuard.cs.md) |
| Login page | [Auth__Login.aspx.cs.md](../07-Security-AuthPages/Auth__Login.aspx.cs.md) |
| Register page | [Auth__Register.aspx.cs.md](../07-Security-AuthPages/Auth__Register.aspx.cs.md) |
| Forgot password | [Auth__ForgotPassword.aspx.cs.md](../07-Security-AuthPages/Auth__ForgotPassword.aspx.cs.md) |

---

## Web.config keys

| Key | Purpose |
|-----|---------|
| `JwtSecret` | HS256 signing key |
| `LoginMaxFailures` | Failures before lockout |
| `AllowSeedMockData` | Seed endpoint on/off |
| `MfaDebug` | **Keep false** in demos |

---

[← Full index](00-INDEX.md)
