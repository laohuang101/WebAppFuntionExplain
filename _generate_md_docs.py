#!/usr/bin/env python3
"""
Generate Markdown documentation for EduLMS Landing + Lecturer + Security.
One .md file per source file, with per-function sections and line notes.
Output: /home/loke/Documents/WebAppFuntionExplain
"""
from __future__ import annotations

import re
from pathlib import Path
from datetime import datetime

ROOT = Path("/home/loke/Documents/WebappAss/WebAppAssignment")
OUT = Path("/home/loke/Documents/WebAppFuntionExplain")

GROUPS = {
    "00-Overview": [],
    "01-Landing": [
        "Pages/Landing/Landing.aspx",
        "Pages/Landing/Landing.aspx.cs",
        "Pages/Landing/Landing.aspx.designer.cs",
        "Pages/Landing/Scripts/landing.js",
    ],
    "02-Lecturer-Pages": [
        "Pages/Lecturer/Dashboard.aspx",
        "Pages/Lecturer/Dashboard.aspx.cs",
        "Pages/Lecturer/CourseCreation.aspx",
        "Pages/Lecturer/CourseCreation.aspx.cs",
        "Pages/Lecturer/CoursePreview.aspx",
        "Pages/Lecturer/CoursePreview.aspx.cs",
        "Pages/Lecturer/Assignments.aspx",
        "Pages/Lecturer/Assignments.aspx.cs",
        "Pages/Lecturer/Grading.aspx",
        "Pages/Lecturer/Grading.aspx.cs",
        "Pages/Lecturer/Students.aspx",
        "Pages/Lecturer/Students.aspx.cs",
        "Pages/Lecturer/ManageSubmissions.aspx",
        "Pages/Lecturer/ManageSubmissions.aspx.cs",
        "Pages/Lecturer/Services/DashboardService.cs",
    ],
    "03-Lecturer-Scripts": [
        "Pages/Lecturer/Scripts/dashboard.js",
        "Pages/Lecturer/Scripts/assignments.js",
        "Pages/Lecturer/Scripts/assignments-edit.js",
        "Pages/Lecturer/Scripts/grading.js",
        "Pages/Lecturer/Scripts/students.js",
        "Pages/Lecturer/Scripts/cc-core.js",
        "Pages/Lecturer/Scripts/cc-curriculum.js",
        "Pages/Lecturer/Scripts/cc-grid.js",
        "Pages/Lecturer/Scripts/cc-media.js",
        "Pages/Lecturer/Scripts/cc-wizard.js",
        "Pages/Lecturer/Scripts/dropdowns.js",
        "Pages/Lecturer/Scripts/editor.js",
        "Pages/Lecturer/Scripts/uploader.js",
        "Pages/Lecturer/Scripts/wizard.js",
        "Pages/Lecturer/Scripts/manage-submissions.js",
        "Pages/Lecturer/course-creation.js",
    ],
    "04-Lecturer-Handlers": [
        "Pages/Lecturer/CurriculumApi.ashx",
        "Pages/Lecturer/UploadMedia.ashx",
        "Pages/Lecturer/UploadThumbnail.ashx",
        "Pages/Lecturer/SeedMockData.ashx",
        "Pages/Lecturer/ServeUpload.ashx",
        "Media.ashx",
    ],
    "05-Data-Layer": [
        "Data/DbHelper.cs",
        "Data/DatabaseHelper.cs",
        "Data/LecturerRepository.cs",
        "Data/Models.cs",
        "Data/CourseSchema.cs",
        "Data/SchemaMap.cs",
        "Data/SchemaBootstrap.cs",
        "Data/DbIndexes.cs",
    ],
    "06-Security-Core": [
        "Data/Security/AuthService.cs",
        "Data/Security/AuthGate.cs",
        "Data/Security/AuthSchema.cs",
        "Data/Security/PasswordHasher.cs",
        "Data/Security/JwtHelper.cs",
        "Data/Security/TotpHelper.cs",
        "Data/Security/CsrfProtection.cs",
        "Data/Security/LoginThrottle.cs",
        "Data/Security/SecurityAudit.cs",
        "Data/Security/FileMagic.cs",
        "Data/Security/UploadPathGuard.cs",
    ],
    "07-Security-AuthPages": [
        "Pages/Authentication/Login.aspx",
        "Pages/Authentication/Login.aspx.cs",
        "Pages/Authentication/Login.aspx.designer.cs",
        "Pages/Authentication/Register.aspx",
        "Pages/Authentication/Register.aspx.cs",
        "Pages/Authentication/Register.aspx.designer.cs",
        "Pages/Authentication/MfaVerify.aspx",
        "Pages/Authentication/MfaVerify.aspx.cs",
        "Pages/Authentication/MfaVerify.aspx.designer.cs",
        "Pages/Authentication/ForgotPassword.aspx",
        "Pages/Authentication/ForgotPassword.aspx.cs",
        "Pages/Authentication/ForgotPassword.aspx.designer.cs",
        "Pages/Authentication/ResetPassword.aspx",
        "Pages/Authentication/ResetPassword.aspx.cs",
        "Pages/Authentication/ResetPassword.aspx.designer.cs",
        "Pages/Authentication/Logout.aspx",
        "Pages/Authentication/Logout.aspx.cs",
        "Pages/Authentication/Logout.aspx.designer.cs",
        "Shared/Scripts/csrf.js",
    ],
}

FEATURE_BLURBS = {
    "Landing": (
        "Public marketing + course catalog. Shows published courses only (`IsPublished`). "
        "Guests can browse; Enroll sends unauthenticated users to Login."
    ),
    "Dashboard": "Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.",
    "CourseCreation": "Create/edit courses, curriculum (chapters/lessons), media, publish/draft.",
    "Assignments": "Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.",
    "Grading": "List submissions for lecturer courses; assign marks and feedback; CSV export.",
    "Students": "Enrolled students per course with progress counts.",
    "CurriculumApi": "JSON ashx API for curriculum CRUD with ownership (`LecturerUID`) checks.",
    "UploadMedia": "Authenticated upload of materials/videos/submissions with magic-byte validation.",
    "Media": "Serve files under Uploads with path sandbox + auth policy by folder.",
    "LecturerRepository": (
        "Central pure-SQL data access for lecturer features: courses, publish, curriculum helpers, "
        "CourseWorks/assignments, submissions, grades, students/enrollments, CSV-related queries. "
        "Ownership always filtered by LecturerUID."
    ),
    "DbHelper": (
        "Primary SQL helper: open connection from Web.config MyDbConn, ExecuteQuery / NonQuery / Scalar, "
        "parameter factory P(), SafeString. All business SQL should go through this (or AuthService helpers)."
    ),
    "DatabaseHelper": (
        "Legacy/alternate connection helper (same MyDbConn). Prefer DbHelper for new code; kept for older call sites."
    ),
    "CourseSchema": (
        "Ensures optional Courses columns exist at runtime (e.g. IsPublished BIT) and backfills defaults when safe."
    ),
    "SchemaMap": (
        "Discovers real table/column names in the attached MDF (SubChapters vs Lessons, etc.) so curriculum SQL adapts."
    ),
    "SchemaBootstrap": (
        "App-start (or first request) orchestration: run AuthSchema, CourseSchema, DbIndexes, and other Ensure* once."
    ),
    "DbIndexes": (
        "Creates useful nonclustered indexes if missing (LecturerUID, IsPublished, CWSubmissions.CWID, …) for LocalDB demos."
    ),
    "Models": (
        "Lightweight POCOs / row shapes (CourseRow, CourseWorkRow, CWSubmissionRow, …) — not Entity Framework entities."
    ),
    # Security core
    "AuthService": (
        "Central auth orchestration: pending registration (no DB row until MFA), login password check, "
        "admin MFA bypass, TOTP verify, complete login (session + JWT), password reset (MFA then new password)."
    ),
    "AuthGate": (
        "Shared gate for pages, WebMethods, and ashx handlers — role checks, CSRF on mutating requests, "
        "validated UserID from session/JWT."
    ),
    "AuthSchema": "Ensures Users security columns exist (PasswordHash, MfaSecret, MfaEnabled, JWT-related helpers).",
    "PasswordHasher": "PBKDF2 password hashing and verification; upgrades legacy plain-text on successful login.",
    "JwtHelper": "HS256 JWT create/validate and EduLMS.Auth cookie set/clear for session restore.",
    "TotpHelper": "RFC 6238 TOTP (Google Authenticator): secret generate, verify ± window, otpauth URI, Base32.",
    "CsrfProtection": "Session CSRF token + cookie + meta tag; validates X-CSRF-Token / form field on POST.",
    "LoginThrottle": "In-memory brute-force protection per email+IP (failures, lockout window).",
    "SecurityAudit": "Append-only security event log (login, register, reset, seed, uploads) for Admin AuditLog.",
    "FileMagic": "Upload content-type validation by magic bytes (PDF, images, video, office docs).",
    "UploadPathGuard": "Normalize/sanitize paths under ~/Uploads; block traversal and illegal folders.",
    # Auth pages
    "Login": "Email + password; Student/Lecturer redirected to MFA; Admin password-only complete login.",
    "Register": "Two-step: form → Session pending → QR/MFA confirm → only then INSERT user.",
    "MfaVerify": "Post-login TOTP (or demo email OTP) step before CompleteLogin issues session/JWT.",
    "ForgotPassword": "Two-step reset: verify email+TOTP first, then set new password (session window).",
    "ResetPassword": "One-shot TOTP + new password form (uses AuthService.ResetPasswordWithTotp).",
    "Logout": "Clears session, abandons session, clears JWT auth cookie.",
    "csrf.js": "Client helper: attach X-CSRF-Token header to fetch/XHR from meta/cookie.",
}


def infer_feature(path: str) -> str:
    for k, v in FEATURE_BLURBS.items():
        if k.lower() in path.lower():
            return v
    return "Part of EduLMS Landing or Lecturer area. See function sections below."


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return f"// ERROR reading file: {e}\n"


CS_METHOD = re.compile(
    r"(?P<header>^\s*(?:public|private|protected|internal|static|\s)+"
    r"(?:async\s+)?[\w.<>,\[\]\?]+\s+(?P<name>\w+)\s*\([^;]*\)\s*(?:where[^{]+)?\{)",
    re.MULTILINE,
)

JS_FUNC = re.compile(
    r"(?:^|\n)\s*(?:async\s+)?function\s+(?P<name>\w+)\s*\((?P<params>[^)]*)\)\s*\{"
    r"|^\s*(?:const|let|var)\s+(?P<name2>\w+)\s*=\s*(?:async\s*)?\((?P<params2>[^)]*)\)\s*=>\s*\{"
    r"|^\s*(?:const|let|var)\s+(?P<name3>\w+)\s*=\s*(?:async\s+)?function\s*\((?P<params3>[^)]*)\)\s*\{"
    r"|^\s*(?P<name4>\w+)\s*:\s*(?:async\s+)?function\s*\((?P<params4>[^)]*)\)\s*\{",
    re.MULTILINE,
)

CS_FIELD = re.compile(
    r"^\s*(?:public|private|protected|internal|static|readonly|\s)+"
    r"(?:readonly\s+)?([\w.<>,\[\]\?]+)\s+(\w+)\s*(?:=|;)",
    re.MULTILINE,
)

JS_VAR = re.compile(r"^\s*(?:const|let|var)\s+(\w+)\s*=", re.MULTILINE)


def find_block_end(text: str, open_brace_index: int) -> int:
    depth = 0
    i = open_brace_index
    in_str = None
    in_line_comment = False
    in_block_comment = False
    while i < len(text):
        c = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if in_line_comment:
            if c == "\n":
                in_line_comment = False
            i += 1
            continue
        if in_block_comment:
            if c == "*" and nxt == "/":
                in_block_comment = False
                i += 2
                continue
            i += 1
            continue
        if in_str:
            if c == "\\" and in_str != "`":
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c == "/" and nxt == "/":
            in_line_comment = True
            i += 2
            continue
        if c == "/" and nxt == "*":
            in_block_comment = True
            i += 2
            continue
        if c in ("'", '"', "`"):
            in_str = c
            i += 1
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return len(text)


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def extract_cs_methods(text: str):
    methods = []
    for m in CS_METHOD.finditer(text):
        name = m.group("name")
        if name in ("if", "while", "for", "switch", "catch", "using", "lock", "get", "set"):
            continue
        brace = text.find("{", m.start())
        if brace < 0:
            continue
        end = find_block_end(text, brace)
        methods.append({
            "name": name,
            "header": m.group("header").split("{")[0].strip(),
            "start": line_of(text, m.start()),
            "end": line_of(text, end - 1),
            "body": text[m.start():end],
        })
    methods.sort(key=lambda x: (x["start"], -(x["end"] - x["start"])))
    return methods


def extract_js_functions(text: str):
    funcs = []
    for m in JS_FUNC.finditer(text):
        name = m.group("name") or m.group("name2") or m.group("name3") or m.group("name4")
        params = m.group("params") or m.group("params2") or m.group("params3") or m.group("params4") or ""
        brace = text.find("{", m.start())
        if brace < 0 or not name:
            continue
        end = find_block_end(text, brace)
        funcs.append({
            "name": name,
            "header": f"function {name}({params.strip()})",
            "start": line_of(text, m.start()),
            "end": line_of(text, end - 1),
            "body": text[m.start():end],
            "params": params.strip(),
        })
    funcs.sort(key=lambda x: x["start"])
    return funcs


def extract_fields_cs(text: str):
    fields = []
    for m in CS_FIELD.finditer(text):
        typ, name = m.group(1), m.group(2)
        if name in ("class", "namespace", "using", "return", "if"):
            continue
        fields.append((name, typ, line_of(text, m.start())))
    return fields[:100]


def extract_vars_js(text: str):
    vars_ = []
    seen = set()
    for m in JS_VAR.finditer(text):
        name = m.group(1)
        if name in seen or name == "function":
            continue
        seen.add(name)
        vars_.append((name, line_of(text, m.start())))
    return vars_[:120]


def explain_method(name: str, header: str, body: str, lang: str) -> list[str]:
    notes = []
    low = (name + " " + header + " " + body[:1200]).lower()
    notes.append(f"**Purpose:** Implements `{name}`.")
    if "webmethod" in body.lower() or "[WebMethod" in body:
        notes.append("**ASP.NET WebMethod:** Called from browser JS via `Page.aspx/MethodName` POST JSON.")
    if "authgate" in low or "requirelecturer" in low or "ensurepage" in low:
        notes.append("**Security:** Uses AuthGate — requires logged-in role.")
    if "csrf" in low:
        notes.append("**CSRF:** Validates anti-forgery token on mutating request.")
    if any(x in low for x in ("sql", "executequery", "sqlcommand", "dbhelper")):
        notes.append("**Data:** Pure SQL via DbHelper/SqlClient (parameterized).")
    if "due" in low and any(x in low for x in ("closed", "pastdue", "duedate")):
        notes.append("**Due date:** Related to assignment closing after the due day.")
    if "ispublished" in low or "publish" in low:
        notes.append("**Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.")
    if "lectureruid" in low or "assertowner" in low:
        notes.append("**Ownership:** Checks course belongs to current lecturer (IDOR protection).")
    if "session" in low:
        notes.append("**Session:** Reads/writes ASP.NET Session.")
    if "json" in low or "javascriptserializer" in low or "json.stringify" in low:
        notes.append("**JSON:** Serializes/deserializes UI or META payloads.")
    if "fetch(" in body:
        notes.append("**AJAX:** Browser calls server endpoints asynchronously.")
    if "redirect" in low:
        notes.append("**Navigation:** Redirects the browser.")
    if name.lower().startswith(("get", "load")):
        notes.append("**Pattern:** Read/load data for display.")
    if name.lower().startswith(("save", "set", "update", "insert")):
        notes.append("**Pattern:** Persist changes.")
    if name.lower().startswith(("delete", "remove", "clear")):
        notes.append("**Pattern:** Delete/clear data.")
    if name.lower() in ("pageload", "page_load"):
        notes.append("**Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.")
    pm = re.search(r"\((.*?)\)", header, re.S)
    if pm and pm.group(1).strip():
        notes.append(f"**Parameters:** `{pm.group(1).strip()[:240]}`")
    if lang == "cs":
        locals_ = re.findall(
            r"\b(?:var|string|int|bool|decimal|object|DateTime|DataTable|List<[^>]+>)\s+(\w+)\s*=",
            body,
        )
    else:
        locals_ = re.findall(r"\b(?:const|let|var)\s+(\w+)\s*=", body)
    if locals_:
        uniq = []
        for x in locals_:
            if x not in uniq:
                uniq.append(x)
        notes.append("**Local variables:** " + ", ".join(f"`{x}`" for x in uniq[:30]))
    return notes


def line_note(line: str) -> str | None:
    s = line.strip()
    if not s or s.startswith("//") or s.startswith("/*") or s.startswith("*") or s.startswith("<!--"):
        return None
    low = s.lower()
    if re.match(r"using\s+", s):
        return "Import namespace/types."
    if re.match(r"namespace\s+", s):
        return "C# namespace grouping."
    if re.match(r"(public|private|partial)\s+class\s+", s):
        return "Class declaration for this page/service."
    if "Page_Load" in s:
        return "Page load entry (GET or postback)."
    if "AuthGate" in s:
        return "Authorization — block wrong role / anonymous."
    if "DbHelper" in s or "SqlCommand" in s or "SqlConnection" in s:
        return "Database access (pure SQL)."
    if "ExecuteQuery" in s or "ExecuteNonQuery" in s or "ExecuteScalar" in s:
        return "Run SQL; return table / rows / scalar."
    if "OpenConnection" in s or "SqlConnection" in s:
        return "Open SQL Server / LocalDB connection."
    if "AddWithValue" in s or "SqlParameter" in s or 'P("@' in s or "DbHelper.P" in s:
        return "Parameterized SQL — prevents classic SQL injection."
    if "EnsureColumn" in s or "EnsureIndex" in s or "EnsureTable" in s:
        return "Idempotent schema/index ensure (safe to run many times)."
    if "Information_Schema" in s or "sys." in low or "COL_LENGTH" in s:
        return "Inspect live database catalog for existing columns/tables."
    if "SCOPE_IDENTITY" in s or "OUTPUT INSERTED" in s:
        return "Return new identity/UID after INSERT."
    if "INNER JOIN" in s or "LEFT JOIN" in s:
        return "Join related tables (courses ↔ chapters ↔ works ↔ users)."
    if "DataTable" in s or "DataRow" in s:
        return "In-memory result set from ADO.NET."
    if "SafeString" in s or "DBNull" in s:
        return "Null-safe read from database values."
    if "Session[" in s:
        return "Server session for logged-in user."
    if "Response.Redirect" in s:
        return "Navigate browser to another URL."
    if "[WebMethod" in s:
        return "Expose method to AJAX JSON calls."
    if "IsPostBack" in s:
        return "False on first open; true after postback."
    if "IsPublished" in s:
        return "Course publish flag for Landing catalog."
    if "DueDate" in s or "dueDate" in s:
        return "Assignment deadline; submissions close after due day."
    if "LecturerUID" in s:
        return "Owner lecturer foreign key."
    if "Csrf" in s or "csrf" in s:
        return "CSRF anti-forgery protection."
    if "fetch(" in s:
        return "HTTP request to server WebMethod/ashx."
    if "addEventListener" in s:
        return "DOM event handler."
    if "getElementById" in s:
        return "Get HTML element by id."
    if "JSON.stringify" in s or "JSON.parse" in s:
        return "JS object ↔ JSON text."
    if s.startswith("try") or s.strip() == "try":
        return "Error handling block."
    if s.startswith("catch"):
        return "Handle/log exception."
    if "<<<META>>>" in s:
        return "Pack extra assignment fields into Description JSON meta."
    if "FileMagic" in s:
        return "Validate upload by file signature."
    if "UploadPathGuard" in s:
        return "Sandbox path under ~/Uploads."
    if "NormalizeRole" in s:
        return "Map role codes/names to Admin/Student/Lecturer."
    if "innerHTML" in s:
        return "Update page HTML."
    if "escapeHtml" in s or "HtmlEncode" in s:
        return "Encode text to reduce XSS risk."
    if "Chart" in s or "chart.js" in low:
        return "Dashboard chart/visualization."
    if "csv" in low:
        return "CSV export."
    if "AssertOwner" in s or "AssertCourseOwner" in s:
        return "Ownership check — prevent IDOR."
    if "ProcessRequest" in s:
        return "IHttpHandler entry for ashx."
    # Security-specific
    if "PasswordHasher" in s or "Rfc2898DeriveBytes" in s or "PBKDF2" in s:
        return "Password hashing (PBKDF2)."
    if "JwtHelper" in s or "HS256" in s or "EduLMS.Auth" in s:
        return "JWT cookie create/validate/clear."
    if "TotpHelper" in s or "HMACSHA1" in s or "otpauth" in s or "Base32" in s:
        return "TOTP / authenticator (RFC 6238) helper."
    if "LoginThrottle" in s or "IsLocked" in s or "RegisterFailure" in s:
        return "Brute-force lockout tracking."
    if "SecurityAudit" in s or "AuditLog" in s:
        return "Write/read security audit events."
    if "StartRegistration" in s or "FinishRegistration" in s or "PendingReg" in s or "SessReg" in s:
        return "Pending registration in Session until MFA confirmed."
    if "VerifyMfa" in s or "VerifyCode" in s:
        return "Verify multi-factor / TOTP code."
    if "CompleteLogin" in s:
        return "Issue Session + JWT after successful auth."
    if "CompletePasswordReset" in s or "VerifyMfaForPasswordReset" in s:
        return "Password-reset MFA then update password hash."
    if "MfaDebug" in s or "IsMfaDebugEnabled" in s:
        return "Debug-only TOTP leak switch (must stay false for demos)."
    if "FileMagic" in s or "magic" in low:
        return "File magic-byte validation on upload."
    if "UploadPathGuard" in s or "NormalizeRelative" in s:
        return "Path sandbox under Uploads."
    if "EnsureToken" in s or "X-CSRF" in s or "CsrfProtection" in s:
        return "CSRF token ensure/validate."
    if "GetValidatedUserId" in s or "TryRestoreSessionFromJwt" in s:
        return "Restore/validate user from Session or JWT; reject stale UIDs."
    if "RequireRole" in s or "EnsurePage" in s or "EnsureHandlerRole" in s:
        return "Role authorization for pages/handlers."
    if "FixedTimeEquals" in s:
        return "Constant-time string compare (reduce timing leaks)."
    if "GenerateSecret" in s:
        return "Create new authenticator secret (Base32)."
    if "BuildOtpAuthUri" in s:
        return "Build otpauth:// URI for QR code."
    return None


def md_fence(code: str, lang: str = "") -> str:
    # avoid breaking fence if code contains ```
    safe = code.replace("```", "``\u200b`")
    return f"```{lang}\n{safe}\n```\n"


def pdf_name_for(rel: str) -> str:
    p = Path(rel)
    safe = re.sub(r"[^\w.\-]+", "_", p.name)
    parent = p.parent.name
    if p.name == "Media.ashx":
        return "Media_ashx.md"
    if parent == "Scripts":
        return f"Scripts__{safe}.md"
    if parent == "Services":
        return f"Services__{safe}.md"
    if parent == "Security":
        return f"Security__{safe}.md"
    if parent == "Authentication":
        return f"Auth__{safe}.md"
    if p.parts[0] == "Data" and parent != "Security":
        return f"Data__{safe}.md"
    return f"{safe}.md"


def write_file_md(path: Path, out_md: Path, title: str, feature_blurb: str, rel: str):
    lines_out = []
    lines_out.append(f"# {title}\n")
    lines_out.append(f"**Source:** `{rel}`  \n")
    lines_out.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  \n")
    lines_out.append("\n---\n\n")
    lines_out.append("## Feature / role in EduLMS\n\n")
    lines_out.append(feature_blurb + "\n\n")

    if not path.exists():
        lines_out.append("> File not found on disk.\n")
        out_md.parent.mkdir(parents=True, exist_ok=True)
        out_md.write_text("".join(lines_out), encoding="utf-8")
        return

    text = read_text(path)
    lines = text.splitlines()
    ext = path.suffix.lower()
    lang = "js" if ext == ".js" else ("aspx" if ext in (".aspx", ".ashx") else "cs")
    fence_lang = "javascript" if lang == "js" else ("html" if lang == "aspx" else "csharp")

    lines_out.append("## File overview\n\n")
    lines_out.append(f"- **Total lines:** {len(lines)}\n")
    lines_out.append(f"- **Kind:** `{ext or 'unknown'}`\n\n")

    lines_out.append("## Variables / fields (file level)\n\n")
    if lang == "cs":
        fields = extract_fields_cs(text)
        if fields:
            for name, typ, ln in fields:
                lines_out.append(f"- **Line {ln}:** `{name}` — type `{typ}`\n")
        else:
            lines_out.append("_No classic field declarations detected (or mostly locals inside methods)._\n")
    elif lang == "js":
        vars_ = extract_vars_js(text)
        if vars_:
            for name, ln in vars_:
                lines_out.append(f"- **Line {ln}:** `{name}` — script-level `const`/`let`/`var`\n")
        else:
            lines_out.append("_No top-level variables detected by scanner._\n")
    else:
        lines_out.append(
            "Markup/mixed file. Server controls and expressions are explained with "
            "code-behind and script companions.\n"
        )
    lines_out.append("\n")

    if lang == "cs" or ext == ".ashx":
        methods = extract_cs_methods(text)
    elif lang == "js":
        methods = extract_js_functions(text)
    else:
        methods = []

    lines_out.append(f"## Functions / methods ({len(methods)} found)\n\n")
    if not methods:
        lines_out.append(
            "_No methods matched the scanner (markup-only or unconventional structure). "
            "See full file listing below._\n\n"
        )

    for meth in methods:
        lines_out.append(f"### `{meth['name']}` — lines {meth['start']}–{meth['end']}\n\n")
        lines_out.append(f"```\n{meth['header'][:400]}\n```\n\n")
        lines_out.append("#### Explanation\n\n")
        for note in explain_method(meth["name"], meth["header"], meth["body"], "js" if lang == "js" else "cs"):
            lines_out.append(f"- {note}\n")
        lines_out.append("\n#### Line-by-line (this function)\n\n")
        body_lines = meth["body"].splitlines()
        max_fn = 250
        for i, raw in enumerate(body_lines[:max_fn]):
            abs_ln = meth["start"] + i
            lines_out.append(f"`{abs_ln:4d}`  `{raw}`\n")
            n = line_note(raw)
            if n:
                lines_out.append(f"  - → {n}\n")
        if len(body_lines) > max_fn:
            lines_out.append(f"\n_… {len(body_lines) - max_fn} more lines in this function (see full listing)._\n")
        lines_out.append("\n---\n\n")

    lines_out.append("## Full file listing with line notes\n\n")
    lines_out.append(
        "Every line of the source is listed (truncated only if extremely long). "
        "Notes appear under lines the analyzer recognizes.\n\n"
    )
    max_full = min(len(lines), 900)
    for i, raw in enumerate(lines[:max_full], start=1):
        # Use indented code style without breaking tables
        display = raw.replace("\t", "    ")
        lines_out.append(f"`{i:4d}`  `{display}`\n")
        n = line_note(raw)
        if n:
            lines_out.append(f"  - → {n}\n")
    if len(lines) > max_full:
        lines_out.append(
            f"\n_… truncated: {len(lines) - max_full} more lines in source. Open the original file for the rest._\n"
        )

    lines_out.append("\n## Source snapshot (raw)\n\n")
    # include full source in a fence for easy copy (cap large files)
    if len(lines) <= 600:
        lines_out.append(md_fence(text, fence_lang))
    else:
        lines_out.append(
            f"_File has {len(lines)} lines — raw dump omitted here to keep Markdown readable. "
            f"Open `{rel}` in the project._\n"
        )

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("".join(lines_out), encoding="utf-8")


def write_index(file_list: list[tuple[str, str, str]]):
    """file_list: (group, rel, md_name)"""
    p = OUT / "00-Overview" / "00-INDEX.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    o = []
    o.append("# EduLMS — Landing & Lecturer Function Explain (Markdown)\n\n")
    o.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  \n")
    o.append(f"**Project root:** `{ROOT}`  \n")
    o.append(f"**This pack:** `{OUT}`  \n\n")
    o.append("---\n\n")
    o.append("## What this pack is\n\n")
    o.append(
        "Markdown documentation for the **Landing** public site and the full **Lecturer** workspace "
        "(ASP.NET Web Forms 4.7.2, pure `SqlClient`).\n\n"
        "Each important source file has its own `.md` file with:\n\n"
        "1. Feature overview\n"
        "2. File-level variables/fields\n"
        "3. **Every detected function** — purpose, parameters, locals, line-by-line notes\n"
        "4. Full file listing with line numbers + annotations\n\n"
    )
    o.append("## How Landing and Lecturer connect\n\n")
    for b in [
        "Lecturer creates a course (CourseCreation) → starts as draft (`IsPublished = 0`).",
        "Lecturer builds curriculum (CurriculumApi + media uploads).",
        "Lecturer publishes course → Landing catalog shows it (`IsPublished = 1`).",
        "Lecturer creates assignments with `DueDate` → students submit until end of due day.",
        "Submissions appear on Dashboard/Grading → marks in `CWMarkings`.",
        "Media.ashx serves files; materials/videos/submissions need login; thumbnails public for cards.",
    ]:
        o.append(f"- {b}\n")

    o.append("\n## Security architecture (quick map)\n\n")
    o.append("```\n")
    o.append("Register form\n")
    o.append("  → AuthService.StartRegistration  (Session only, NO Users row)\n")
    o.append("  → QR + TotpHelper secret\n")
    o.append("  → AuthService.FinishRegistration (TOTP OK → INSERT Users + hash + MfaSecret)\n\n")
    o.append("Login\n")
    o.append("  → LoginThrottle (lockout)\n")
    o.append("  → AuthService.LoginPassword (PBKDF2 verify)\n")
    o.append("  → Admin: CompleteLogin (session + JWT)  [MFA bypass]\n")
    o.append("  → Student/Lecturer: MfaVerify → TotpHelper.VerifyCode → CompleteLogin\n\n")
    o.append("Every protected page/ashx\n")
    o.append("  → AuthGate (role) + CsrfProtection on POST/AJAX\n")
    o.append("  → Optional JWT restore via AuthService.GetValidatedUserId\n\n")
    o.append("Forgot password\n")
    o.append("  → VerifyMfaForPasswordReset → session window → CompletePasswordReset\n\n")
    o.append("Uploads\n")
    o.append("  → AuthGate + FileMagic + UploadPathGuard → Media.ashx auth by folder\n")
    o.append("```\n\n")
    o.append("### Security components\n\n")
    o.append("| Component | Role |\n|-----------|------|\n")
    for t, d in [
        ("PasswordHasher", "PBKDF2 hash/verify"),
        ("JwtHelper", "HS256 cookie JWT"),
        ("TotpHelper", "Google Authenticator TOTP"),
        ("AuthService", "Register/login/MFA/reset orchestration"),
        ("AuthGate", "Page/handler role + CSRF"),
        ("CsrfProtection", "Anti-forgery token"),
        ("LoginThrottle", "Brute-force lockout"),
        ("SecurityAudit", "Event log for Admin"),
        ("FileMagic / UploadPathGuard", "Safe uploads"),
    ]:
        o.append(f"| `{t}` | {d} |\n")

    o.append("\n## Folder map\n\n")
    for name, desc in [
        ("00-Overview", "This index"),
        ("01-Landing", "Landing.aspx + code-behind + landing.js"),
        ("02-Lecturer-Pages", "Dashboard, CourseCreation, Assignments, Grading, Students, …"),
        ("03-Lecturer-Scripts", "Client JS modules (cc-*, dashboard, grading, …)"),
        ("04-Lecturer-Handlers", "ashx APIs: Curriculum, Upload, Seed, Media"),
        ("05-Data-Layer", "DbHelper, LecturerRepository, Models, schema bootstrap & indexes"),
        ("06-Security-Core", "AuthService, JWT, TOTP, CSRF, throttle, audit, upload guards"),
        ("07-Security-AuthPages", "Login, Register, MFA, Forgot/Reset password, Logout, csrf.js"),
    ]:
        o.append(f"- **`{name}/`** — {desc}\n")

    o.append("\n### Data layer (pure SQL)\n\n")
    o.append("| File | Role |\n|------|------|\n")
    for t, d in [
        ("DbHelper", "Main ADO.NET helper (connection, query, params)"),
        ("DatabaseHelper", "Legacy connection helper"),
        ("LecturerRepository", "All lecturer SQL (courses, works, grades, students)"),
        ("Models", "Simple DTOs / row classes (not EF)"),
        ("CourseSchema", "Ensure IsPublished etc."),
        ("SchemaMap", "Map real MDF table/column names"),
        ("SchemaBootstrap", "Run all Ensure* at startup"),
        ("DbIndexes", "Create performance indexes if missing"),
        ("Data/Security/*", "Auth SQL + security helpers (see folder 06)"),
    ]:
        o.append(f"| `{t}` | {d} |\n")

    o.append("\n## Key SQL tables\n\n")
    o.append("| Table | Role |\n|-------|------|\n")
    for t, d in [
        ("Courses", "CID, LecturerUID, Name, IsPublished, …"),
        ("Chapters / SubChapters / StudyMats", "Curriculum + lesson media"),
        ("CourseWorks", "Assignments: DueDate + Description META"),
        ("CWSubmissions", "Student answers"),
        ("CWMarkings", "Grades / feedback"),
        ("Enrollments", "Student ↔ course"),
        ("Users", "Auth; Role 0=Admin 1=Student 2=Lecturer"),
    ]:
        o.append(f"| `{t}` | {d} |\n")

    o.append("\n## Document index\n\n")
    cur = None
    for group, rel, md_name in file_list:
        if group != cur:
            cur = group
            o.append(f"\n### {group}\n\n")
        o.append(f"- [{md_name}](../{group}/{md_name}) — `{rel}`\n")

    o.append("\n## Regenerate\n\n")
    o.append("```bash\n")
    o.append(f"python3 {OUT}/_generate_md_docs.py\n")
    o.append("```\n")
    p.write_text("".join(o), encoding="utf-8")
    # root README
    (OUT / "README.md").write_text(
        f"""# WebApp Function Explain (Markdown)

Detailed **Landing + Lecturer + Security** documentation for EduLMS.

## Start here

→ **[00-Overview/00-INDEX.md](00-Overview/00-INDEX.md)**

## Folders

| Folder | Content |
|--------|---------|
| `00-Overview` | Index & architecture |
| `01-Landing` | Landing page |
| `02-Lecturer-Pages` | ASPX + code-behind |
| `03-Lecturer-Scripts` | JavaScript |
| `04-Lecturer-Handlers` | ashx + Media |
| `05-Data-Layer` | DbHelper, LecturerRepository, schema, indexes |
| `06-Security-Core` | AuthService, JWT, TOTP, CSRF, throttle, audit |
| `07-Security-AuthPages` | Login, Register, MFA, Forgot/Reset, Logout |

### Quick links

**Data**

- [02-DATA-OVERVIEW.md](00-Overview/02-DATA-OVERVIEW.md)
- [Data__DbHelper.cs.md](05-Data-Layer/Data__DbHelper.cs.md)
- [Data__LecturerRepository.cs.md](05-Data-Layer/Data__LecturerRepository.cs.md)
- [Data__Models.cs.md](05-Data-Layer/Data__Models.cs.md)

**Security**

- [01-SECURITY-OVERVIEW.md](00-Overview/01-SECURITY-OVERVIEW.md)
- [Security__AuthService.cs.md](06-Security-Core/Security__AuthService.cs.md)
- [Security__AuthGate.cs.md](06-Security-Core/Security__AuthGate.cs.md)
- [Auth__Login.aspx.cs.md](07-Security-AuthPages/Auth__Login.aspx.cs.md)

Generated: {datetime.now().isoformat(timespec='seconds')}

```bash
python3 {OUT}/_generate_md_docs.py
```
""",
        encoding="utf-8",
    )


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    file_list = []
    count = 0
    for group, files in GROUPS.items():
        if group == "00-Overview":
            continue
        for rel in files:
            src = ROOT / rel
            md_name = pdf_name_for(rel)
            out_md = OUT / group / md_name
            print("Building", out_md.relative_to(OUT), "...")
            write_file_md(src, out_md, Path(rel).name, infer_feature(rel), rel)
            file_list.append((group, rel, md_name))
            count += 1
    write_index(file_list)
    print(f"Done. {count} Markdown files under {OUT}")


if __name__ == "__main__":
    main()
