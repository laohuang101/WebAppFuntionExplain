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


# Short names used heavily in this codebase → plain English
VAR_GLOSSARY = {
    # single / short
    "n": "Count or number of rows/items (often from COUNT(*) or list length).",
    "i": "Loop index (0-based counter in for-loops).",
    "j": "Inner loop index.",
    "k": "Key name when iterating object keys, or secondary index.",
    "e": "Event object (JS click/input) OR caught Exception (C# catch).",
    "ex": "Exception object in catch blocks.",
    "r": "One DataRow from a query result, or HTTP Response shorthand.",
    "c": "Often a course object/row, or a single character when looping strings.",
    "d": "Deserialized dictionary/JSON payload, or Date/day value.",
    "s": "String value being cleaned/built, or submission object.",
    "t": "Temporary string/token/time value.",
    "p": "Parameter, path, or password fragment depending on context.",
    "q": "Search query text, or SQL command text.",
    "v": "Generic value (version flag in JSON, or loop value).",
    "x": "Generic temporary / coordinate / exception alias.",
    "sb": "StringBuilder — efficient string concatenation.",
    "dt": "DataTable — full result set from SQL (many rows/columns).",
    "dr": "DataReader / DataRow depending on API.",
    "cmd": "SqlCommand — the SQL statement + parameters object.",
    "conn": "SqlConnection — open link to LocalDB/SQL Server.",
    "ctx": "Current HTTP request context (Request, Response, Session).",
    "uid": "User ID (Users.UID) of the logged-in or target user.",
    "cid": "Course ID (Courses.CID).",
    "cwid": "CourseWork ID (assignment) (CourseWorks.CWID).",
    "chid": "Chapter ID (Chapters.ChID).",
    "schid": "SubChapter / lesson ID.",
    "sid": "Submission ID (CWSubmissions.SID).",
    "qid": "Question ID (objective quiz).",
    "id": "Generic primary key / identifier.",
    "ok": "Boolean success flag.",
    "res": "Result object returned from fetch/WebMethod (`data.d` unwrapped).",
    "msg": "Human-readable message (error or success).",
    "err": "Error message string or error element.",
    "sql": "SQL query text (should use parameters, not raw user input).",
    "hash": "Password hash (PBKDF2) stored in DB.",
    "token": "JWT or CSRF token string.",
    "secret": "MFA TOTP Base32 secret for authenticator apps.",
    "code": "6-digit TOTP / OTP the user typed.",
    "email": "Account email address (usually lowercased).",
    "password": "Plain password from the form (never log this).",
    "role": "User role code or name (Admin/Student/Lecturer).",
    "name": "Display name of user/course/criterion.",
    "title": "Title of course work / page heading.",
    "path": "File path under Uploads or URL path.",
    "url": "HTTP URL to media or page.",
    "file": "Uploaded file object or file name.",
    "fileName": "Original file name for display/download.",
    "fileUrl": "Stored relative path or Media.ashx URL of upload.",
    "dueDate": "Assignment deadline (date); after end of that day submissions close.",
    "isClosed": "True when past due date — student cannot submit.",
    "isPublished": "Course visibility flag for Landing catalog.",
    "published": "UI/publish intent flag when saving a course/work.",
    "requireFile": "Assignment requires a file upload.",
    "maxScore": "Maximum points (usually 100).",
    "score": "Points earned or max points depending on context.",
    "rubric": "List of grading criteria (name + points).",
    "questions": "Objective quiz questions array.",
    "answers": "Student selected answers for quiz.",
    "content": "Submission body text or JSON payload in CWSubmissions.",
    "desc": "Description text (may embed <<<META>>> JSON).",
    "instructions": "Student-facing assignment instructions (plain part of Description).",
    "meta": "Extra settings packed as JSON (dueDate, requireFile, …).",
    "extra": "Dictionary of optional fields inside META.",
    "packed": "Parsed Description META structure.",
    "list": "In-memory collection being built for JSON return.",
    "items": "Array of rows for UI tables.",
    "row": "Single database or table row.",
    "rows": "Collection of rows.",
    "user": "AuthUser or user row (UID, Email, Role, MfaSecret, …).",
    "result": "AuthResult or API result { success, message, … }.",
    "success": "Boolean — operation succeeded.",
    "message": "Status text for the UI.",
    "lecturerUid": "Users.UID of the course owner (lecturer).",
    "studentUid": "Users.UID of the student.",
    "studentName": "Student display name.",
    "courseName": "Course display name.",
    "assignmentTitle": "CourseWork title.",
    "owner": "LecturerUID looked up for ownership check.",
    "exists": "Count > 0 check (email/user/row already exists).",
    "count": "Number of matching records.",
    "total": "Sum of points or total items.",
    "page": "Page number for pagination, or Page instance.",
    "filter": "Search/filter text for lists.",
    "json": "JSON string (to parse or serialize).",
    "dict": "Dictionary / map of key → value.",
    "payload": "Object about to be JSON-serialized or sent over network.",
    "headers": "HTTP headers object for fetch.",
    "body": "HTTP request body.",
    "method": "HTTP method (GET/POST) or MFA method (totp/email).",
    "window": "TOTP time-step window (± steps for clock skew).",
    "step": "TOTP 30-second time step counter.",
    "key": "HMAC key bytes or dictionary key.",
    "raw": "Raw bytes or unprocessed input string.",
    "normalized": "Cleaned secret/code (spaces removed, uppercased).",
    "parts": "Split path or name segments.",
    "folder": "Uploads subfolder (CourseMaterials, CourseVideos, …).",
    "relative": "Path relative to Uploads root.",
    "physical": "Absolute disk path on the server.",
    "root": "Root directory path (Uploads).",
    "full": "Fully resolved absolute path.",
    "allowed": "Boolean — path/role is permitted.",
    "locked": "Account locked by LoginThrottle.",
    "failures": "Failed login attempt count.",
    "bucket": "Throttle state for one email+IP.",
    "ip": "Client IP address for throttle/audit.",
    "at": "Timestamp (CreatedUtc / PwdResetAt).",
    "exp": "Expiry DateTime.",
    "now": "Current time (usually UTC or server local).",
    "ttl": "Time-to-live duration for pending session data.",
    "session": "ASP.NET Session state bag.",
    "cookie": "HTTP cookie (JWT or CSRF).",
    "issuer": "TOTP issuer label (EduLMS).",
    "label": "otpauth account label (issuer:email).",
    "uri": "otpauth:// or other URI string.",
    "qrUrl": "URL of QR image for authenticator setup.",
    "bytes": "Byte array (hash, random, file content).",
    "salt": "Random salt for PBKDF2.",
    "iter": "PBKDF2 iteration count.",
    "algo": "Hash algorithm name.",
    "plain": "Plain-text description without META trailer.",
    "start": "Range start (file stream) or string index.",
    "end": "Range end or string end index.",
    "len": "Length of string/array.",
    "ext": "File extension (.pdf, .mp4, …).",
    "mime": "MIME content type.",
    "kind": "Upload kind (material/video/thumbnail/submission).",
    "storePath": "Relative path where file was saved.",
    "serveUrl": "Public/handler URL to download/preview file.",
    "btn": "Button DOM element.",
    "el": "Generic DOM element.",
    "box": "Container element for lists/tables.",
    "ddl": "Drop-down list (select) element.",
    "opt": "Option element or optional label.",
    "img": "Image element or image path.",
    "canvas": "Chart/canvas element.",
    "chart": "Chart.js instance.",
    "builderType": "Assignment builder mode: Text vs Objective.",
    "rubricRows": "UI state: grading rubric criteria rows.",
    "objectiveQuestions": "UI state: quiz questions being edited.",
    "currentMeta": "Cached coursework flags (requireFile, isClosed, …).",
    "currentQuestions": "Quiz questions loaded for student submit.",
    "UserID": "Session key for logged-in Users.UID.",
    "UserRole": "Session key for role (Admin/Student/Lecturer).",
    "UserName": "Session key for display name.",
    "AuthToken": "Session copy of JWT string.",
    "MfaPendingUid": "Session: user waiting for MFA after password OK.",
    "MfaMethod": "Session: totp or email OTP method.",
    "PwdResetUid": "Session: user allowed to set new password after MFA.",
    "PwdResetEmail": "Session: email shown on reset step 2.",
    "PwdResetAt": "Session: when MFA for reset was verified (timeout).",
    "Reg.Name": "Pending registration name (Session until MFA).",
    "Reg.Email": "Pending registration email.",
    "Reg.PasswordHash": "Pending registration hashed password.",
    "Reg.MfaSecret": "Pending registration TOTP secret.",
    "Reg.CreatedUtc": "When pending registration started.",
    # more common in this project
    "adapter": "SqlDataAdapter — fills a DataTable from a SqlCommand.",
    "parameters": "Array of SQL parameters (@Name values) for a query.",
    "xff": "X-Forwarded-For header value (client IP when behind a proxy).",
    "comma": "Index of the first comma in a string (split helper).",
    "table": "DataTable or HTML table container.",
    "cmdText": "SQL command text.",
    "reader": "SqlDataReader for streaming query results.",
    "tran": "SqlTransaction for multi-statement commit/rollback.",
    "cs": "Connection string text.",
    "connString": "Database connection string from Web.config.",
    "connectionString": "Database connection string from Web.config.",
    "map": "Dictionary mapping keys to values (e.g. throttle buckets).",
    "bucket": "Throttle state for one email+IP (failures + lockout).",
    "failures": "Number of failed login attempts in the current window.",
    "lockMsg": "Message shown when the account is temporarily locked.",
    "lockout": "DateTime until which login is blocked.",
    "plain": "Text without META trailer (student-visible instructions).",
    "enableMfa": "Whether MFA should be enabled for the account.",
    "mfaOn": "1/0 flag written to Users.MfaEnabled.",
    "mfaSecret": "Authenticator secret stored for the user.",
    "totpCode": "User-entered 6-digit authenticator code.",
    "roleCode": "Stored role value (0 Admin / 1 Student / 2 Lecturer).",
    "roleNormalized": "Friendly role name (Admin, Student, Lecturer).",
    "roleChoice": "Role selected on the register form.",
    "p1": "New password field (first entry).",
    "p2": "Confirm password field (must match p1).",
    "pass": "Password from a form field.",
    "confirm": "Confirm-password form field.",
}


def split_camel(name: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    s = s.replace("_", " ").replace(".", " ")
    return s.strip()


def explain_variable(name: str, typ: str | None = None, rhs: str | None = None, lang: str = "cs") -> str:
    """
    Return plain-English meaning for a variable/parameter/field name.
    """
    if not name:
        return "Unnamed value."
    raw = name.strip()
    # strip common prefixes for lookup
    key = raw
    if key.startswith("_"):
        key = key[1:]
    low = key.lower()

    typ_l = (typ or "").lower()
    rhs_l = (rhs or "").lower()

    # Disambiguate short names using type / assignment
    meaning = None
    if low == "e":
        if "exception" in typ_l or "exception" in rhs_l:
            meaning = "Caught Exception object."
        elif "string" in typ_l or "email" in rhs_l or "tolower" in rhs_l:
            meaning = "Normalized email string (trimmed/lowercased)."
        else:
            meaning = "Often email string (C#) or DOM event (JS)."
    elif low == "r":
        if "datarow" in typ_l or "rows[" in rhs_l:
            meaning = "One DataRow from a SQL result."
        elif "response" in typ_l or "httpresponse" in typ_l:
            meaning = "HTTP response object."
        else:
            meaning = "Usually one database row (DataRow) in query loops."
    elif low == "c":
        if "char" in typ_l:
            meaning = "Single character while scanning a string."
        elif "course" in rhs_l or "cid" in rhs_l:
            meaning = "Course object/row."
        else:
            meaning = "Temporary value (character, course, or counter depending on loop)."
    elif low == "n":
        if "count" in rhs_l or "length" in rhs_l or "int" in typ_l:
            meaning = "Integer count (rows, items, or length)."
        else:
            meaning = "Numeric count or temporary integer."
    elif low == "d":
        if "dict" in typ_l or "dictionary" in typ_l or "deserialize" in rhs_l:
            meaning = "Dictionary/map from JSON or META payload."
        elif "datetime" in typ_l or "date" in rhs_l:
            meaning = "Date/time value."
        else:
            meaning = "Often a dictionary payload or date value."
    elif low == "s":
        if "string" in typ_l or "trim" in rhs_l or "tostring" in rhs_l:
            meaning = "String being cleaned or built."
        else:
            meaning = "String value or submission-related object."

    # exact glossary (if not disambiguated)
    if meaning is None:
        if key in VAR_GLOSSARY:
            meaning = VAR_GLOSSARY[key]
        elif low in VAR_GLOSSARY:
            meaning = VAR_GLOSSARY[low]
        else:
            # prefix/suffix heuristics
            if low.endswith("uid") or (low.endswith("id") and len(low) <= 6):
                meaning = f"Identifier (`{key}`) — database primary/foreign key."
            elif low.endswith("count") or low.startswith("num"):
                meaning = f"Numeric count of items related to `{split_camel(key)}`."
            elif low.startswith("is") or low.startswith("has") or low.startswith("can"):
                meaning = f"Boolean flag: {split_camel(key)}."
            elif low.startswith(("txt", "lbl", "btn", "ddl", "hf", "pnl", "lit", "gv", "img", "chk")):
                meaning = f"UI control reference ({split_camel(key)})."
            elif low.startswith("str"):
                meaning = f"String value: {split_camel(key[3:] or key)}."
            elif "password" in low or low in ("pass", "pwd"):
                meaning = "Password (plain input — hash before storing)."
            elif "email" in low:
                meaning = "Email address."
            elif "token" in low:
                meaning = "Security token (JWT or CSRF)."
            elif "secret" in low:
                meaning = "Secret key material (MFA Base32 or crypto secret)."
            elif "hash" in low:
                meaning = "Cryptographic hash string."
            elif "path" in low or "dir" in low or "folder" in low:
                meaning = "Filesystem or URL path."
            elif "url" in low or "href" in low:
                meaning = "URL string."
            elif "date" in low or "time" in low or low.endswith("at") or low.endswith("utc"):
                meaning = "Date/time value."
            elif "list" in low or "items" in low or "rows" in low:
                meaning = f"Collection / list related to {split_camel(key)}."
            elif low.endswith("s") and len(low) > 3 and low not in ("success", "status", "address", "process"):
                meaning = f"Often a collection related to {split_camel(key)} (plural name)."
            else:
                meaning = f"Holds “{split_camel(key)}” for this scope."

    # enrich from type (skip if glossary already covers the concept)
    type_note = ""
    if typ:
        t = typ.strip()
        tl = t.lower()
        glossed = low in VAR_GLOSSARY or key in VAR_GLOSSARY
        if "datatable" in tl and not glossed:
            type_note = " (`DataTable` = SQL result grid)"
        elif "datarow" in tl and not glossed:
            type_note = " (`DataRow` = one SQL row)"
        elif "sqlconnection" in tl and not glossed:
            type_note = " (open DB connection)"
        elif "sqlcommand" in tl and not glossed:
            type_note = " (SQL + parameters)"
        elif "httpcontext" in tl and not glossed:
            type_note = " (current HTTP request)"
        elif "stringbuilder" in tl and not glossed:
            type_note = " (string buffer)"
        elif "authuser" in tl and not glossed:
            type_note = " (user DTO)"
        elif "authresult" in tl and not glossed:
            type_note = " (auth result DTO)"
        elif tl == "var":
            type_note = ""  # inferred type
        elif tl in ("int", "int32", "long", "int64") and not glossed:
            type_note = " (integer)"
        elif tl in ("bool", "boolean") and not glossed:
            type_note = " (true/false)"
        elif "string" in tl and not glossed:
            type_note = " (text)"
        elif "datetime" in tl and not glossed:
            type_note = " (date/time)"
        elif ("decimal" in tl or "double" in tl or "float" in tl) and not glossed:
            type_note = " (number/score)"
        elif ("dictionary" in tl or "list<" in tl) and not glossed:
            type_note = f" (`{t}` collection)"
        elif not glossed and tl not in ("object",):
            type_note = f" (type `{t}`)"

    # enrich from RHS assignment snippet
    rhs_note = ""
    if rhs:
        r = rhs.strip()
        rl = r.lower()
        if "executequery" in rl:
            rhs_note = " Assigned from SQL SELECT result set."
        elif "executenonquery" in rl:
            rhs_note = " Assigned from rows-affected of INSERT/UPDATE/DELETE."
        elif "executescalar" in rl:
            rhs_note = " Assigned from single SQL scalar (COUNT/IDENTITY)."
        elif "getvalidateduserid" in rl or "requirelecturer" in rl or "requirestudent" in rl or "currentuserid" in rl:
            rhs_note = " Assigned from logged-in user id (0 if anonymous)."
        elif "hash(" in rl or "passwordhasher" in rl:
            rhs_note = " Assigned from password hash function."
        elif "verify" in rl:
            rhs_note = " Assigned from verification boolean/result."
        elif "generatesecret" in rl:
            rhs_note = " New random MFA secret."
        elif "generatecode" in rl or "verifycode" in rl:
            rhs_note = " TOTP related value."
        elif "json" in rl and ("serial" in rl or "parse" in rl or "stringify" in rl):
            rhs_note = " JSON serialize/parse result."
        elif "session[" in rl:
            rhs_note = " Read from ASP.NET Session."
        elif "request[" in rl or "querystring" in rl:
            rhs_note = " Comes from HTTP request."
        elif "configurationmanager" in rl:
            rhs_note = " Read from Web.config."
        elif "fetch(" in rl:
            rhs_note = " HTTP response from browser fetch."
        elif "getelementbyid" in rl:
            rhs_note = " DOM element from the page."
        elif "new " in rl:
            rhs_note = " Newly constructed object."
        elif re.match(r"^[\d.]+m?$", r):
            rhs_note = f" Literal number `{r}`."
        elif r.startswith('"') or r.startswith("'"):
            rhs_note = " Literal text string."

    return meaning + type_note + ((" " + rhs_note) if rhs_note else "")


def extract_locals_with_context(body: str, lang: str) -> list[tuple[str, str | None, str | None]]:
    """
    Return list of (name, type_or_None, rhs_snippet) for locals in a function body.
    Skips the signature line so parameters are not double-listed as locals.
    """
    found = []
    seen = set()
    # Drop first line (method signature) — params are documented separately
    body_lines = body.splitlines()
    if body_lines:
        scan = "\n".join(body_lines[1:])
    else:
        scan = body

    # Also mark parameter names so they are never listed as locals
    header_line = body_lines[0] if body_lines else ""
    for pname, _ in extract_params_from_header(header_line if "(" in header_line else "x()"):
        seen.add(pname)

    if lang == "cs":
        patterns = [
            re.compile(
                r"\b(?P<type>var|string|int|bool|decimal|double|float|object|long|byte\[\]|DateTime|DateTime\?|DataTable|DataRow|SqlConnection|SqlCommand|StringBuilder|AuthUser|AuthResult|HttpContext|List<[^>]+>|Dictionary<[^>]+>|IEnumerable<[^>]+>)\s+(?P<name>\w+)\s*=\s*(?P<rhs>[^;]+);",
                re.M,
            ),
            re.compile(r"\bforeach\s*\(\s*(?:var|[\w.<>\?]+)\s+(?P<name>\w+)\s+in\b", re.M),
        ]
    else:
        patterns = [
            re.compile(
                r"\b(?:const|let|var)\s+(?P<name>\w+)\s*=\s*(?P<rhs>[^;\n]+)",
                re.M,
            ),
            re.compile(r"\bfor\s*\(\s*(?:let|var|const)?\s*(?P<name>\w+)\s*=", re.M),
        ]

    for pat in patterns:
        for m in pat.finditer(scan):
            name = m.group("name")
            if name in seen:
                continue
            if name in ("if", "for", "return", "new", "this", "true", "false", "null"):
                continue
            seen.add(name)
            typ = m.groupdict().get("type")
            rhs = m.groupdict().get("rhs")
            if rhs:
                rhs = rhs.strip()
                if len(rhs) > 80:
                    rhs = rhs[:77] + "..."
            found.append((name, typ, rhs))
    return found[:40]


def extract_params_from_header(header: str) -> list[tuple[str, str | None]]:
    """Parse (Type name, Type name = default) from C#/JS signature."""
    pm = re.search(r"\((.*)\)", header, re.S)
    if not pm or not pm.group(1).strip():
        return []
    inner = pm.group(1).strip()
    if not inner or inner == "void":
        return []
    parts = []
    # naive split on commas not inside <>
    depth = 0
    cur = []
    for ch in inner:
        if ch == "<":
            depth += 1
            cur.append(ch)
        elif ch == ">":
            depth -= 1
            cur.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur:
        parts.append("".join(cur).strip())

    out = []
    for p in parts:
        p = re.sub(r"\s*=\s*.*$", "", p).strip()  # drop default
        p = p.replace("params ", "").replace("this ", "").replace("out ", "").replace("ref ", "")
        if not p:
            continue
        bits = p.split()
        if len(bits) == 1:
            out.append((bits[0], None))
        else:
            # last token is name, rest is type
            out.append((bits[-1].strip(","), " ".join(bits[:-1])))
    return out


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

    # Parameters with meanings
    params = extract_params_from_header(header)
    if params:
        notes.append("**Parameters (what each means):**")
        for pname, ptyp in params:
            meaning = explain_variable(pname, ptyp, None, lang)
            notes.append(
                f"- `{pname}`" + (f" (`{ptyp}`)" if ptyp else "") + f" — {meaning}"
            )

    # Locals with meanings
    locals_ = extract_locals_with_context(body, lang)
    if locals_:
        notes.append("**Local variables (what each means):**")
        for lname, ltyp, rhs in locals_:
            meaning = explain_variable(lname, ltyp, rhs, lang)
            notes.append(
                f"- `{lname}`" + (f" (`{ltyp}`)" if ltyp else "") + f" — {meaning}"
            )
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


def format_numbered_code(body_lines: list[str], start_line: int, fence_lang: str, max_lines: int = 250) -> str:
    """Pretty fenced block with line numbers: 001 | code"""
    chunk = body_lines[:max_lines]
    rows = []
    for i, raw in enumerate(chunk):
        abs_ln = start_line + i
        # keep tabs readable; strip only trailing CR
        display = raw.replace("\t", "    ").rstrip("\r")
        rows.append(f"{abs_ln:4d} | {display}")
    if len(body_lines) > max_lines:
        rows.append(f" ... | … {len(body_lines) - max_lines} more lines truncated …")
    return md_fence("\n".join(rows), fence_lang)


def format_line_notes(body_lines: list[str], start_line: int, max_lines: int = 250, lang: str = "cs") -> list[str]:
    """Bullet notes keyed by absolute line number (patterns + assignment variable meanings)."""
    out = []
    for i, raw in enumerate(body_lines[:max_lines]):
        abs_ln = start_line + i
        bits = []
        n = line_note(raw)
        if n:
            bits.append(n)
        # If this line declares/assigns a variable, explain it
        s = raw.strip()
        m_cs = re.match(
            r"^(?:var|string|int|bool|decimal|double|float|object|long|DateTime\??|DataTable|DataRow|SqlConnection|SqlCommand|StringBuilder|AuthUser|AuthResult|List<[^>]+>|Dictionary<[^>]+>)\s+(\w+)\s*=\s*(.+);?\s*$",
            s,
        )
        m_js = re.match(r"^(?:const|let|var)\s+(\w+)\s*=\s*(.+);?\s*$", s)
        m = m_cs or m_js
        if m:
            vname, rhs = m.group(1), m.group(2).rstrip(";").strip()
            typ = None
            if m_cs:
                typ = s.split()[0]
            meaning = explain_variable(vname, typ, rhs, "js" if m_js else "cs")
            bits.append(f"`{vname}` means: {meaning}")
        if bits:
            out.append(f"- **L{abs_ln}:** " + " | ".join(bits) + "\n")
    return out


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
    lines_out.append(
        "Each name is explained in plain English (what it stores / why it exists).\n\n"
    )
    if lang == "cs":
        fields = extract_fields_cs(text)
        if fields:
            for name, typ, ln in fields:
                meaning = explain_variable(name, typ, None, "cs")
                lines_out.append(
                    f"- **Line {ln}:** `{name}` (`{typ}`) — **{meaning}**\n"
                )
        else:
            lines_out.append(
                "_No classic field declarations detected (or mostly locals inside methods — "
                "see each function’s **Local variables** section)._\n"
            )
    elif lang == "js":
        vars_ = extract_vars_js(text)
        if vars_:
            for name, ln in vars_:
                meaning = explain_variable(name, None, None, "js")
                lines_out.append(
                    f"- **Line {ln}:** `{name}` — script-level `const`/`let`/`var` — **{meaning}**\n"
                )
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
        lines_out.append(md_fence(meth["header"][:400], fence_lang))
        lines_out.append("\n#### Explanation\n\n")
        for note in explain_method(meth["name"], meth["header"], meth["body"], "js" if lang == "js" else "cs"):
            # notes may already be markdown bullets ("- `x` — ...")
            if note.startswith("- ") or note.startswith("* "):
                lines_out.append(f"{note}\n")
            else:
                lines_out.append(f"- {note}\n")
        lines_out.append("\n#### Line-by-line (this function)\n\n")
        body_lines = meth["body"].splitlines()
        max_fn = 250
        lines_out.append(format_numbered_code(body_lines, meth["start"], fence_lang, max_fn))
        notes = format_line_notes(body_lines, meth["start"], max_fn, lang)
        if notes:
            lines_out.append("\n**Line notes** (what code + variables mean)\n\n")
            lines_out.extend(notes)
        if len(body_lines) > max_fn:
            lines_out.append(
                f"\n_… {len(body_lines) - max_fn} more lines in this function (see full listing)._\n"
            )
        lines_out.append("\n---\n\n")

    lines_out.append("## Full file listing with line notes\n\n")
    lines_out.append(
        "Source is shown as a single fenced code block with line numbers. "
        "Recognized patterns and **variable meanings** are listed under **Line notes**.\n\n"
    )
    max_full = min(len(lines), 900)
    lines_out.append(format_numbered_code(lines[:max_full], 1, fence_lang, max_full))
    full_notes = format_line_notes(lines[:max_full], 1, max_full, lang)
    if full_notes:
        lines_out.append("\n**Line notes** (what code + variables mean)\n\n")
        lines_out.extend(full_notes)
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
