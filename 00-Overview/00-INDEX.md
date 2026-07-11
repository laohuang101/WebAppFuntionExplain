# EduLMS — Landing & Lecturer Function Explain (Markdown)

<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)
**Project root:** `/home/loke/Documents/WebappAss/WebAppAssignment`  
**This pack:** `/home/loke/Documents/WebAppFuntionExplain`  

---

## What this pack is

Markdown documentation for the **Landing** public site and the full **Lecturer** workspace (ASP.NET Web Forms 4.7.2, pure `SqlClient`).

Each important source file has its own `.md` file with:

1. Feature overview
2. File-level variables/fields
3. **Every detected function** — purpose, parameters, locals, line-by-line notes
4. Full file listing with line numbers + annotations

## How Landing and Lecturer connect

- Lecturer creates a course (CourseCreation) → starts as draft (`IsPublished = 0`).
- Lecturer builds curriculum (CurriculumApi + media uploads).
- Lecturer publishes course → Landing catalog shows it (`IsPublished = 1`).
- Lecturer creates assignments with `DueDate` → students submit until end of due day.
- Submissions appear on Dashboard/Grading → marks in `CWMarkings`.
- Media.ashx serves files; materials/videos/submissions need login; thumbnails public for cards.

## Security architecture (quick map)

```
Register form
  → AuthService.StartRegistration  (Session only, NO Users row)
  → QR + TotpHelper secret
  → AuthService.FinishRegistration (TOTP OK → INSERT Users + hash + MfaSecret)

Login
  → LoginThrottle (lockout)
  → AuthService.LoginPassword (PBKDF2 verify)
  → Admin: CompleteLogin (session + JWT)  [MFA bypass]
  → Student/Lecturer: MfaVerify → TotpHelper.VerifyCode → CompleteLogin

Every protected page/ashx
  → AuthGate (role) + CsrfProtection on POST/AJAX
  → Optional JWT restore via AuthService.GetValidatedUserId

Forgot password
  → VerifyMfaForPasswordReset → session window → CompletePasswordReset

Uploads
  → AuthGate + FileMagic + UploadPathGuard → Media.ashx auth by folder
```

### Security components

| Component | Role |
|-----------|------|
| `PasswordHasher` | PBKDF2 hash/verify |
| `JwtHelper` | HS256 cookie JWT |
| `TotpHelper` | Google Authenticator TOTP |
| `AuthService` | Register/login/MFA/reset orchestration |
| `AuthGate` | Page/handler role + CSRF |
| `CsrfProtection` | Anti-forgery token |
| `LoginThrottle` | Brute-force lockout |
| `SecurityAudit` | Event log for Admin |
| `FileMagic / UploadPathGuard` | Safe uploads |

## Folder map

- **`00-Overview/`** — This index
- **`01-Landing/`** — Landing.aspx + code-behind + landing.js
- **`02-Lecturer-Pages/`** — Dashboard, CourseCreation, Assignments, Grading, Students, …
- **`03-Lecturer-Scripts/`** — Client JS modules (cc-*, dashboard, grading, …)
- **`04-Lecturer-Handlers/`** — ashx APIs: Curriculum, Upload, Seed, Media
- **`05-Data-Layer/`** — DbHelper, LecturerRepository, Models, schema bootstrap & indexes
- **`06-Security-Core/`** — AuthService, JWT, TOTP, CSRF, throttle, audit, upload guards
- **`07-Security-AuthPages/`** — Login, Register, MFA, Forgot/Reset password, Logout, csrf.js

### Data layer (pure SQL)

| File | Role |
|------|------|
| `DbHelper` | Main ADO.NET helper (connection, query, params) |
| `DatabaseHelper` | Legacy connection helper |
| `LecturerRepository` | All lecturer SQL (courses, works, grades, students) |
| `Models` | Simple DTOs / row classes (not EF) |
| `CourseSchema` | Ensure IsPublished etc. |
| `SchemaMap` | Map real MDF table/column names |
| `SchemaBootstrap` | Run all Ensure* at startup |
| `DbIndexes` | Create performance indexes if missing |
| `Data/Security/*` | Auth SQL + security helpers (see folder 06) |

## Key SQL tables

| Table | Role |
|-------|------|
| `Courses` | CID, LecturerUID, Name, IsPublished, … |
| `Chapters / SubChapters / StudyMats` | Curriculum + lesson media |
| `CourseWorks` | Assignments: DueDate + Description META |
| `CWSubmissions` | Student answers |
| `CWMarkings` | Grades / feedback |
| `Enrollments` | Student ↔ course |
| `Users` | Auth; Role 0=Admin 1=Student 2=Lecturer |

## Document index


### 01-Landing

- [Landing.aspx.md](../01-Landing/Landing.aspx.md) — `Pages/Landing/Landing.aspx`
- [Landing.aspx.cs.md](../01-Landing/Landing.aspx.cs.md) — `Pages/Landing/Landing.aspx.cs`
- [Landing.aspx.designer.cs.md](../01-Landing/Landing.aspx.designer.cs.md) — `Pages/Landing/Landing.aspx.designer.cs`
- [Scripts__landing.js.md](../01-Landing/Scripts__landing.js.md) — `Pages/Landing/Scripts/landing.js`

### 02-Lecturer-Pages

- [Dashboard.aspx.md](../02-Lecturer-Pages/Dashboard.aspx.md) — `Pages/Lecturer/Dashboard.aspx`
- [Dashboard.aspx.cs.md](../02-Lecturer-Pages/Dashboard.aspx.cs.md) — `Pages/Lecturer/Dashboard.aspx.cs`
- [CourseCreation.aspx.md](../02-Lecturer-Pages/CourseCreation.aspx.md) — `Pages/Lecturer/CourseCreation.aspx`
- [CourseCreation.aspx.cs.md](../02-Lecturer-Pages/CourseCreation.aspx.cs.md) — `Pages/Lecturer/CourseCreation.aspx.cs`
- [CoursePreview.aspx.md](../02-Lecturer-Pages/CoursePreview.aspx.md) — `Pages/Lecturer/CoursePreview.aspx`
- [CoursePreview.aspx.cs.md](../02-Lecturer-Pages/CoursePreview.aspx.cs.md) — `Pages/Lecturer/CoursePreview.aspx.cs`
- [Assignments.aspx.md](../02-Lecturer-Pages/Assignments.aspx.md) — `Pages/Lecturer/Assignments.aspx`
- [Assignments.aspx.cs.md](../02-Lecturer-Pages/Assignments.aspx.cs.md) — `Pages/Lecturer/Assignments.aspx.cs`
- [Grading.aspx.md](../02-Lecturer-Pages/Grading.aspx.md) — `Pages/Lecturer/Grading.aspx`
- [Grading.aspx.cs.md](../02-Lecturer-Pages/Grading.aspx.cs.md) — `Pages/Lecturer/Grading.aspx.cs`
- [Students.aspx.md](../02-Lecturer-Pages/Students.aspx.md) — `Pages/Lecturer/Students.aspx`
- [Students.aspx.cs.md](../02-Lecturer-Pages/Students.aspx.cs.md) — `Pages/Lecturer/Students.aspx.cs`
- [ManageSubmissions.aspx.md](../02-Lecturer-Pages/ManageSubmissions.aspx.md) — `Pages/Lecturer/ManageSubmissions.aspx`
- [ManageSubmissions.aspx.cs.md](../02-Lecturer-Pages/ManageSubmissions.aspx.cs.md) — `Pages/Lecturer/ManageSubmissions.aspx.cs`
- [Services__DashboardService.cs.md](../02-Lecturer-Pages/Services__DashboardService.cs.md) — `Pages/Lecturer/Services/DashboardService.cs`

### 03-Lecturer-Scripts

- [Scripts__dashboard.js.md](../03-Lecturer-Scripts/Scripts__dashboard.js.md) — `Pages/Lecturer/Scripts/dashboard.js`
- [Scripts__assignments.js.md](../03-Lecturer-Scripts/Scripts__assignments.js.md) — `Pages/Lecturer/Scripts/assignments.js`
- [Scripts__assignments-edit.js.md](../03-Lecturer-Scripts/Scripts__assignments-edit.js.md) — `Pages/Lecturer/Scripts/assignments-edit.js`
- [Scripts__grading.js.md](../03-Lecturer-Scripts/Scripts__grading.js.md) — `Pages/Lecturer/Scripts/grading.js`
- [Scripts__students.js.md](../03-Lecturer-Scripts/Scripts__students.js.md) — `Pages/Lecturer/Scripts/students.js`
- [Scripts__cc-core.js.md](../03-Lecturer-Scripts/Scripts__cc-core.js.md) — `Pages/Lecturer/Scripts/cc-core.js`
- [Scripts__cc-curriculum.js.md](../03-Lecturer-Scripts/Scripts__cc-curriculum.js.md) — `Pages/Lecturer/Scripts/cc-curriculum.js`
- [Scripts__cc-grid.js.md](../03-Lecturer-Scripts/Scripts__cc-grid.js.md) — `Pages/Lecturer/Scripts/cc-grid.js`
- [Scripts__cc-media.js.md](../03-Lecturer-Scripts/Scripts__cc-media.js.md) — `Pages/Lecturer/Scripts/cc-media.js`
- [Scripts__cc-wizard.js.md](../03-Lecturer-Scripts/Scripts__cc-wizard.js.md) — `Pages/Lecturer/Scripts/cc-wizard.js`
- [Scripts__dropdowns.js.md](../03-Lecturer-Scripts/Scripts__dropdowns.js.md) — `Pages/Lecturer/Scripts/dropdowns.js`
- [Scripts__editor.js.md](../03-Lecturer-Scripts/Scripts__editor.js.md) — `Pages/Lecturer/Scripts/editor.js`
- [Scripts__uploader.js.md](../03-Lecturer-Scripts/Scripts__uploader.js.md) — `Pages/Lecturer/Scripts/uploader.js`
- [Scripts__wizard.js.md](../03-Lecturer-Scripts/Scripts__wizard.js.md) — `Pages/Lecturer/Scripts/wizard.js`
- [Scripts__manage-submissions.js.md](../03-Lecturer-Scripts/Scripts__manage-submissions.js.md) — `Pages/Lecturer/Scripts/manage-submissions.js`
- [course-creation.js.md](../03-Lecturer-Scripts/course-creation.js.md) — `Pages/Lecturer/course-creation.js`

### 04-Lecturer-Handlers

- [CurriculumApi.ashx.md](../04-Lecturer-Handlers/CurriculumApi.ashx.md) — `Pages/Lecturer/CurriculumApi.ashx`
- [UploadMedia.ashx.md](../04-Lecturer-Handlers/UploadMedia.ashx.md) — `Pages/Lecturer/UploadMedia.ashx`
- [UploadThumbnail.ashx.md](../04-Lecturer-Handlers/UploadThumbnail.ashx.md) — `Pages/Lecturer/UploadThumbnail.ashx`
- [SeedMockData.ashx.md](../04-Lecturer-Handlers/SeedMockData.ashx.md) — `Pages/Lecturer/SeedMockData.ashx`
- [ServeUpload.ashx.md](../04-Lecturer-Handlers/ServeUpload.ashx.md) — `Pages/Lecturer/ServeUpload.ashx`
- [Media_ashx.md](../04-Lecturer-Handlers/Media_ashx.md) — `Media.ashx`

### 05-Data-Layer

- [Data__DbHelper.cs.md](../05-Data-Layer/Data__DbHelper.cs.md) — `Data/DbHelper.cs`
- [Data__DatabaseHelper.cs.md](../05-Data-Layer/Data__DatabaseHelper.cs.md) — `Data/DatabaseHelper.cs`
- [Data__LecturerRepository.cs.md](../05-Data-Layer/Data__LecturerRepository.cs.md) — `Data/LecturerRepository.cs`
- [Data__Models.cs.md](../05-Data-Layer/Data__Models.cs.md) — `Data/Models.cs`
- [Data__CourseSchema.cs.md](../05-Data-Layer/Data__CourseSchema.cs.md) — `Data/CourseSchema.cs`
- [Data__SchemaMap.cs.md](../05-Data-Layer/Data__SchemaMap.cs.md) — `Data/SchemaMap.cs`
- [Data__SchemaBootstrap.cs.md](../05-Data-Layer/Data__SchemaBootstrap.cs.md) — `Data/SchemaBootstrap.cs`
- [Data__DbIndexes.cs.md](../05-Data-Layer/Data__DbIndexes.cs.md) — `Data/DbIndexes.cs`

### 06-Security-Core

- [Security__AuthService.cs.md](../06-Security-Core/Security__AuthService.cs.md) — `Data/Security/AuthService.cs`
- [Security__AuthGate.cs.md](../06-Security-Core/Security__AuthGate.cs.md) — `Data/Security/AuthGate.cs`
- [Security__AuthSchema.cs.md](../06-Security-Core/Security__AuthSchema.cs.md) — `Data/Security/AuthSchema.cs`
- [Security__PasswordHasher.cs.md](../06-Security-Core/Security__PasswordHasher.cs.md) — `Data/Security/PasswordHasher.cs`
- [Security__JwtHelper.cs.md](../06-Security-Core/Security__JwtHelper.cs.md) — `Data/Security/JwtHelper.cs`
- [Security__TotpHelper.cs.md](../06-Security-Core/Security__TotpHelper.cs.md) — `Data/Security/TotpHelper.cs`
- [Security__CsrfProtection.cs.md](../06-Security-Core/Security__CsrfProtection.cs.md) — `Data/Security/CsrfProtection.cs`
- [Security__LoginThrottle.cs.md](../06-Security-Core/Security__LoginThrottle.cs.md) — `Data/Security/LoginThrottle.cs`
- [Security__SecurityAudit.cs.md](../06-Security-Core/Security__SecurityAudit.cs.md) — `Data/Security/SecurityAudit.cs`
- [Security__FileMagic.cs.md](../06-Security-Core/Security__FileMagic.cs.md) — `Data/Security/FileMagic.cs`
- [Security__UploadPathGuard.cs.md](../06-Security-Core/Security__UploadPathGuard.cs.md) — `Data/Security/UploadPathGuard.cs`

### 07-Security-AuthPages

- [Auth__Login.aspx.md](../07-Security-AuthPages/Auth__Login.aspx.md) — `Pages/Authentication/Login.aspx`
- [Auth__Login.aspx.cs.md](../07-Security-AuthPages/Auth__Login.aspx.cs.md) — `Pages/Authentication/Login.aspx.cs`
- [Auth__Login.aspx.designer.cs.md](../07-Security-AuthPages/Auth__Login.aspx.designer.cs.md) — `Pages/Authentication/Login.aspx.designer.cs`
- [Auth__Register.aspx.md](../07-Security-AuthPages/Auth__Register.aspx.md) — `Pages/Authentication/Register.aspx`
- [Auth__Register.aspx.cs.md](../07-Security-AuthPages/Auth__Register.aspx.cs.md) — `Pages/Authentication/Register.aspx.cs`
- [Auth__Register.aspx.designer.cs.md](../07-Security-AuthPages/Auth__Register.aspx.designer.cs.md) — `Pages/Authentication/Register.aspx.designer.cs`
- [Auth__MfaVerify.aspx.md](../07-Security-AuthPages/Auth__MfaVerify.aspx.md) — `Pages/Authentication/MfaVerify.aspx`
- [Auth__MfaVerify.aspx.cs.md](../07-Security-AuthPages/Auth__MfaVerify.aspx.cs.md) — `Pages/Authentication/MfaVerify.aspx.cs`
- [Auth__MfaVerify.aspx.designer.cs.md](../07-Security-AuthPages/Auth__MfaVerify.aspx.designer.cs.md) — `Pages/Authentication/MfaVerify.aspx.designer.cs`
- [Auth__ForgotPassword.aspx.md](../07-Security-AuthPages/Auth__ForgotPassword.aspx.md) — `Pages/Authentication/ForgotPassword.aspx`
- [Auth__ForgotPassword.aspx.cs.md](../07-Security-AuthPages/Auth__ForgotPassword.aspx.cs.md) — `Pages/Authentication/ForgotPassword.aspx.cs`
- [Auth__ForgotPassword.aspx.designer.cs.md](../07-Security-AuthPages/Auth__ForgotPassword.aspx.designer.cs.md) — `Pages/Authentication/ForgotPassword.aspx.designer.cs`
- [Auth__ResetPassword.aspx.md](../07-Security-AuthPages/Auth__ResetPassword.aspx.md) — `Pages/Authentication/ResetPassword.aspx`
- [Auth__ResetPassword.aspx.cs.md](../07-Security-AuthPages/Auth__ResetPassword.aspx.cs.md) — `Pages/Authentication/ResetPassword.aspx.cs`
- [Auth__ResetPassword.aspx.designer.cs.md](../07-Security-AuthPages/Auth__ResetPassword.aspx.designer.cs.md) — `Pages/Authentication/ResetPassword.aspx.designer.cs`
- [Auth__Logout.aspx.md](../07-Security-AuthPages/Auth__Logout.aspx.md) — `Pages/Authentication/Logout.aspx`
- [Auth__Logout.aspx.cs.md](../07-Security-AuthPages/Auth__Logout.aspx.cs.md) — `Pages/Authentication/Logout.aspx.cs`
- [Auth__Logout.aspx.designer.cs.md](../07-Security-AuthPages/Auth__Logout.aspx.designer.cs.md) — `Pages/Authentication/Logout.aspx.designer.cs`
- [Scripts__csrf.js.md](../07-Security-AuthPages/Scripts__csrf.js.md) — `Shared/Scripts/csrf.js`

## Regenerate

```bash
python3 /home/loke/Documents/WebAppFuntionExplain/_generate_md_docs.py
```
