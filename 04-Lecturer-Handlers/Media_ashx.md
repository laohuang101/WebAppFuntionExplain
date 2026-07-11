# Media.ashx
**Source:** `Media.ashx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Serve files under Uploads with path sandbox + auth policy by folder.

## File overview

- **Total lines:** 463
- **Kind:** `.ashx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (11 found)

### `ProcessRequest` — lines 19–116

#### Signature

```html
public void ProcessRequest(HttpContext context)
```

#### What it is

Main entry point for an `.ashx` HTTP handler — handles one browser request from start to finish.

#### How it works

1. Starts when something calls `ProcessRequest`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `f` | `string` | Holds “f” for this scope. (text)  Comes from HTTP request. |
| `relative` | `string` | Path relative to Uploads root. |
| `bare` | `string` | Holds “bare” for this scope. (text) |
| `foundBare` | `string` | Holds “found Bare” for this scope. (text) |
| `relBare` | `string` | Holds “rel Bare” for this scope. (text) |
| `folderBare` | `string` | Filesystem or URL path. (text) |
| `parts` | `var` | Split path or name segments. |
| `folder` | `string` | Uploads subfolder (CourseMaterials, CourseVideos, …). |
| `physical` | `string` | Absolute disk path on the server. |
| `byMeta` | `string` | Holds “by Meta” for this scope. (text) |
| `sb` | `var` | StringBuilder — efficient string concatenation.  Newly constructed object. |
| `rootFull` | `string` | Holds “root Full” for this scope. (text) |
| `full` | `string` | Fully resolved absolute path. |

#### Code

```html
  19 | 
  20 |     public void ProcessRequest(HttpContext context)
  21 |     {
  22 |         try
  23 |         {
  24 |             if (context.Request["diag"] == "1" || context.Request["debug"] == "1")
  25 |             {
  26 |                 if (!context.IsDebuggingEnabled)
  27 |                 {
  28 |                     WriteText(context, 403, "Diagnostics disabled.");
  29 |                     return;
  30 |                 }
  31 |                 // Diag lists upload folders — lecturers/admins only
  32 |                 if (!AuthorizeFolder(context, "CourseMaterials"))
  33 |                     return;
  34 |                 WriteDiag(context);
  35 |                 return;
  36 |             }
  37 | 
  38 |             string f = context.Request["f"]
  39 |                        ?? context.Request["path"]
  40 |                        ?? context.Request["file"]
  41 |                        ?? "";
  42 | 
  43 |             string relative = UploadPathGuard.NormalizeRelative(f);
  44 |             if (string.IsNullOrEmpty(relative))
  45 |             {
  46 |                 // Bare filename → search allowed folders via .meta
  47 |                 string bare = (f ?? "").Replace('\\', '/').Trim().TrimStart('/');
  48 |                 if (!string.IsNullOrEmpty(bare) && bare.IndexOf('/') < 0 && bare.IndexOf("..") < 0)
  49 |                 {
  50 |                     // Never resolve bare names into submissions without a folder hint
  51 |                     string foundBare = FindByOriginalName(context, null, bare);
  52 |                     if (foundBare != null)
  53 |                     {
  54 |                         string relBare = ToRelativeUnderUploads(context, foundBare);
  55 |                         string folderBare = FirstFolder(relBare);
  56 |                         if (!AuthorizeFolder(context, folderBare))
  57 |                             return;
  58 |                         StreamFile(context, foundBare);
  59 |                         return;
  60 |                     }
  61 |                 }
  62 |                 WriteText(context, 400, "Missing or invalid f= parameter. Example: Media.ashx?f=CourseMaterials/abc123.pdf");
  63 |                 return;
  64 |             }
  65 | 
  66 |             var parts = relative.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
  67 |             string folder = parts.Length > 0 ? parts[0] : "";
  68 |             if (!AuthorizeFolder(context, folder))
  69 |                 return;
  70 | 
  71 |             string physical = UploadPathGuard.ToPhysical(context, relative);
  72 | 
  73 |             if (physical == null || !File.Exists(physical))
  74 |             {
  75 |                 // Resolve original display name → GUID file via .meta sidecars
  76 |                 string byMeta = parts.Length >= 2
  77 |                     ? FindByOriginalName(context, parts[0], parts[parts.Length - 1])
  78 |                     : null;
  79 |                 if (byMeta != null)
  80 |                 {
  81 |                     StreamFile(context, byMeta);
  82 |                     return;
  83 |                 }
  84 | 
  85 |                 if (context.IsDebuggingEnabled)
  86 |                 {
  87 |                     var sb = new StringBuilder();
  88 |                     sb.AppendLine("404 File not found");
  89 |                     sb.AppendLine("Requested: Uploads/" + relative);
  90 |                     WriteText(context, 404, sb.ToString());
  91 |                 }
  92 |                 else
  93 |                 {
  94 |                     WriteText(context, 404, "File not found.");
  95 |                 }
  96 |                 return;
  97 |             }
  98 | 
  99 |             string rootFull = Path.GetFullPath(context.Server.MapPath("~/Uploads"))
 100 |                 .TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
 101 |                 + Path.DirectorySeparatorChar;
 102 |             string full = Path.GetFullPath(physical);
 103 |             if (!full.StartsWith(rootFull, StringComparison.OrdinalIgnoreCase))
 104 |             {
 105 |                 WriteText(context, 403, "Access denied.");
 106 |                 return;
 107 |             }
 108 | 
 109 |             StreamFile(context, full);
 110 |         }
 111 |         catch (Exception ex)
 112 |         {
 113 |             if (IsClientAbort(ex)) return;
 114 |             try { WriteText(context, 500, context.IsDebuggingEnabled ? ("Media error: " + ex.Message) : "Media error."); } catch { }
 115 |         }
 116 |     }
```

---

### `AuthorizeFolder` — lines 124–166

#### Signature

```html
private static bool AuthorizeFolder(HttpContext context, string folder)
```

#### What it is

Decides if the current user may download a file from that Uploads folder.

#### How it works

1. Return `false` to the caller.
2. Return `true` to the caller.
3. Read the logged-in user id from Session/JWT (0 means not signed in).
4. Return `false` to the caller.
5. Save temporary state in Session (`Session !`).
6. Return `true` to the caller.
7. If the user is Admin, complete login without MFA; otherwise require MFA.
8. Return `true` to the caller.
9. Return `false` to the caller.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |
| `folder` | `string` | Uploads subfolder (CourseMaterials, CourseVideos, …). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `int` | User ID (Users.UID) of the logged-in or target user.  Assigned from logged-in user id (0 if anonymous). |
| `role` | `string` | User role code or name (Admin/Student/Lecturer). |

#### Code

```html
 124 |     private static bool AuthorizeFolder(HttpContext context, string folder)
 125 |     {
 126 |         folder = (folder ?? "").Trim();
 127 |         if (string.IsNullOrEmpty(folder))
 128 |         {
 129 |             WriteText(context, 400, "Missing folder.");
 130 |             return false;
 131 |         }
 132 | 
 133 |         // Public catalog images only
 134 |         if (string.Equals(folder, "CourseThumbnails", StringComparison.OrdinalIgnoreCase))
 135 |             return true;
 136 | 
 137 |         int uid = AuthService.GetValidatedUserId(context);
 138 |         if (uid <= 0)
 139 |         {
 140 |             WriteText(context, 401, "Sign in required to access this file.");
 141 |             return false;
 142 |         }
 143 | 
 144 |         string role = AuthService.NormalizeRole(
 145 |             context.Session != null ? context.Session["UserRole"] as string : null);
 146 | 
 147 |         // Lesson materials / videos: any authenticated role
 148 |         if (string.Equals(folder, "CourseMaterials", StringComparison.OrdinalIgnoreCase) ||
 149 |             string.Equals(folder, "CourseVideos", StringComparison.OrdinalIgnoreCase))
 150 |             return true;
 151 | 
 152 |         // Student submission files: no anonymous; role must be Student/Lecturer/Admin
 153 |         if (string.Equals(folder, "CourseSubmissions", StringComparison.OrdinalIgnoreCase))
 154 |         {
 155 |             if (string.Equals(role, "Student", StringComparison.OrdinalIgnoreCase) ||
 156 |                 string.Equals(role, "Lecturer", StringComparison.OrdinalIgnoreCase) ||
 157 |                 string.Equals(role, "Admin", StringComparison.OrdinalIgnoreCase))
 158 |                 return true;
 159 | 
 160 |             WriteText(context, 403, "You do not have access to submission files.");
 161 |             return false;
 162 |         }
 163 | 
 164 |         WriteText(context, 403, "Folder not allowed.");
 165 |         return false;
 166 |     }
```

---

### `FirstFolder` — lines 167–173

#### Signature

```html
private static string FirstFolder(string relative)
```

#### What it is

Function `FirstFolder` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `relative` | `string` | Path relative to Uploads root. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `slash` | `int` | Holds “slash” for this scope. (integer) |

#### Code

```html
 167 | 
 168 |     private static string FirstFolder(string relative)
 169 |     {
 170 |         if (string.IsNullOrEmpty(relative)) return "";
 171 |         int slash = relative.IndexOf('/');
 172 |         return slash < 0 ? relative : relative.Substring(0, slash);
 173 |     }
```

---

### `ToRelativeUnderUploads` — lines 174–187

#### Signature

```html
private static string ToRelativeUnderUploads(HttpContext context, string physical)
```

#### What it is

Function `ToRelativeUnderUploads` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `ToRelativeUnderUploads`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |
| `physical` | `string` | Absolute disk path on the server. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `root` | `string` | Root directory path (Uploads). |
| `full` | `string` | Fully resolved absolute path. |

#### Code

```html
 174 | 
 175 |     private static string ToRelativeUnderUploads(HttpContext context, string physical)
 176 |     {
 177 |         try
 178 |         {
 179 |             string root = Path.GetFullPath(context.Server.MapPath("~/Uploads"))
 180 |                 .TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
 181 |                 + Path.DirectorySeparatorChar;
 182 |             string full = Path.GetFullPath(physical);
 183 |             if (!full.StartsWith(root, StringComparison.OrdinalIgnoreCase)) return null;
 184 |             return full.Substring(root.Length).Replace('\\', '/');
 185 |         }
 186 |         catch { return null; }
 187 |     }
```

---

### `FindByOriginalName` — lines 192–263

#### Signature

```html
private static string FindByOriginalName(HttpContext context, string folderOrNull, string originalName)
```

#### What it is

Function `FindByOriginalName` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |
| `folderOrNull` | `string` | Filesystem or URL path. (text) |
| `originalName` | `string` | Holds “original Name” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `uploads` | `string` | Often a collection related to uploads (plural name). (text) |
| `dir` | `string` | Filesystem or URL path. (text) |
| `exact` | `string` | Holds “exact” for this scope. (text) |
| `content` | `string` | Submission body text or JSON payload in CWSubmissions. |
| `dataFile` | `string` | Holds “data File” for this scope. (text) |
| `log` | `string` | Holds “log” for this scope. (text) |
| `o` | `int` | Holds “o” for this scope. (integer) |
| `orig` | `string` | Holds “orig” for this scope. (text) |
| `sp` | `int` | Holds “sp” for this scope. (integer) |
| `u` | `int` | Holds “u” for this scope. (integer) |
| `under` | `string` | Holds “under” for this scope. (text) |
| `sp2` | `int` | Holds “sp2” for this scope. (integer) |
| `phys` | `string` | Often a collection related to phys (plural name). (text) |
| `folder` | `—` | Uploads subfolder (CourseMaterials, CourseVideos, …). |
| `meta` | `—` | Extra settings packed as JSON (dueDate, requireFile, …). |
| `line` | `—` | Holds “line” for this scope. |

#### Code

```html
 192 |     private static string FindByOriginalName(HttpContext context, string folderOrNull, string originalName)
 193 |     {
 194 |         if (string.IsNullOrWhiteSpace(originalName)) return null;
 195 |         originalName = Path.GetFileName(originalName.Trim().Replace('\\', '/'));
 196 |         string uploads = context.Server.MapPath("~/Uploads");
 197 |         if (!Directory.Exists(uploads)) return null;
 198 | 
 199 |         string[] folders = string.IsNullOrEmpty(folderOrNull)
 200 |             ? AllowedRoots
 201 |             : new[] { folderOrNull };
 202 | 
 203 |         foreach (var folder in folders)
 204 |         {
 205 |             string dir = Path.Combine(uploads, folder);
 206 |             if (!Directory.Exists(dir)) continue;
 207 | 
 208 |             string exact = Path.Combine(dir, originalName);
 209 |             if (File.Exists(exact)) return exact;
 210 | 
 211 |             foreach (var meta in Directory.GetFiles(dir, "*.meta"))
 212 |             {
 213 |                 try
 214 |                 {
 215 |                     string content = Path.GetFileName(File.ReadAllText(meta).Trim().Replace('\\', '/'));
 216 |                     if (string.Equals(content, originalName, StringComparison.OrdinalIgnoreCase))
 217 |                     {
 218 |                         string dataFile = meta.Substring(0, meta.Length - 5);
 219 |                         if (File.Exists(dataFile)) return dataFile;
 220 |                     }
 221 |                 }
 222 |                 catch { }
 223 |             }
 224 |         }
 225 | 
 226 |         // Scan uploads.log: "OK under=CourseMaterials/{guid}.pdf original=My File.pdf"
 227 |         try
 228 |         {
 229 |             string log = Path.Combine(context.Server.MapPath("~/App_Data/Logs"), "uploads.log");
 230 |             if (File.Exists(log))
 231 |             {
 232 |                 foreach (var line in File.ReadAllLines(log))
 233 |                 {
 234 |                     if (line.IndexOf("original=", StringComparison.OrdinalIgnoreCase) < 0) continue;
 235 |                     if (line.IndexOf("under=", StringComparison.OrdinalIgnoreCase) < 0) continue;
 236 |                     int o = line.IndexOf("original=", StringComparison.OrdinalIgnoreCase);
 237 |                     string orig = line.Substring(o + 9).Trim();
 238 |                     int sp = orig.IndexOf(" bytes=");
 239 |                     if (sp > 0) orig = orig.Substring(0, sp).Trim();
 240 |                     orig = Path.GetFileName(orig.Replace('\\', '/'));
 241 |                     if (!string.Equals(orig, originalName, StringComparison.OrdinalIgnoreCase)) continue;
 242 | 
 243 |                     int u = line.IndexOf("under=", StringComparison.OrdinalIgnoreCase);
 244 |                     string under = line.Substring(u + 6).Trim();
 245 |                     int sp2 = under.IndexOf(' ');
 246 |                     if (sp2 > 0) under = under.Substring(0, sp2).Trim();
 247 |                     under = under.Replace('\\', '/').TrimStart('/');
 248 |                     if (under.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 249 |                         under = under.Substring(8);
 250 |                     string phys = context.Server.MapPath("~/Uploads/" + under);
 251 |                     if (File.Exists(phys))
 252 |                     {
 253 |                         // Write .meta for next time
 254 |                         try { File.WriteAllText(phys + ".meta", originalName, Encoding.UTF8); } catch { }
 255 |                         return phys;
 256 |                     }
 257 |                 }
 258 |             }
 259 |         }
 260 |         catch { }
 261 | 
 262 |         return null;
 263 |     }
```

---

### `NormalizeRequestPath` — lines 264–294

#### Signature

```html
private static string NormalizeRequestPath(string f)
```

#### What it is

Converts or cleans **Normalize Request Path** into a usable form.

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `f` | `string` | Holds “f” for this scope. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `up` | `int` | Holds “up” for this scope. (integer) |
| `p` | `int` | Parameter, path, or password fragment depending on context. |
| `rest` | `string` | Holds “rest” for this scope. (text) |
| `eq` | `int` | Holds “eq” for this scope. (integer) |
| `amp` | `int` | Holds “amp” for this scope. (integer) |

#### Code

```html
 264 | 
 265 |     private static string NormalizeRequestPath(string f)
 266 |     {
 267 |         if (string.IsNullOrWhiteSpace(f)) return "";
 268 |         f = f.Replace('\\', '/').Trim().TrimStart('/');
 269 | 
 270 |         if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 271 |             f = f.Substring("Uploads/".Length);
 272 |         int up = f.IndexOf("/Uploads/", StringComparison.OrdinalIgnoreCase);
 273 |         if (up >= 0) f = f.Substring(up + "/Uploads/".Length);
 274 | 
 275 |         if (f.IndexOf("ServeUpload.ashx", StringComparison.OrdinalIgnoreCase) >= 0 ||
 276 |             f.IndexOf("Media.ashx", StringComparison.OrdinalIgnoreCase) >= 0)
 277 |         {
 278 |             int p = f.IndexOf("f=", StringComparison.OrdinalIgnoreCase);
 279 |             if (p < 0) p = f.IndexOf("path=", StringComparison.OrdinalIgnoreCase);
 280 |             if (p >= 0)
 281 |             {
 282 |                 string rest = f.Substring(p);
 283 |                 int eq = rest.IndexOf('=');
 284 |                 rest = eq >= 0 ? rest.Substring(eq + 1) : rest;
 285 |                 int amp = rest.IndexOf('&');
 286 |                 if (amp >= 0) rest = rest.Substring(0, amp);
 287 |                 try { f = HttpUtility.UrlDecode(rest); } catch { f = rest; }
 288 |                 f = f.TrimStart('/');
 289 |                 if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 290 |                     f = f.Substring("Uploads/".Length);
 291 |             }
 292 |         }
 293 |         return f;
 294 |     }
```

---

### `StreamFile` — lines 295–383

#### Signature

```html
private static void StreamFile(HttpContext context, string physical)
```

#### What it is

Function `StreamFile` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `StreamFile`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |
| `physical` | `string` | Absolute disk path on the server. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `fileName` | `string` | Original file name for display/download. |
| `metaPath` | `string` | Filesystem or URL path. (text) |
| `downloadName` | `string` | Holds “download Name” for this scope. (text) |
| `orig` | `string` | Holds “orig” for this scope. (text) |
| `ext` | `string` | File extension (.pdf, .mp4, …). |
| `contentType` | `string` | Holds “content Type” for this scope. (text) |
| `forceDownload` | `bool` | Holds “force Download” for this scope. (true/false)  Comes from HTTP request. |
| `fileLength` | `long` | Holds “file Length” for this scope. (integer)  Newly constructed object. |
| `start` | `long` | Range start (file stream) or string index.  Literal number `0`. |
| `end` | `long` | Range end or string end index. |
| `isRange` | `bool` | Boolean flag: is Range. (true/false) |
| `rangeHeader` | `string` | Holds “range Header” for this scope. (text) |
| `spec` | `string` | Holds “spec” for this scope. (text) |
| `dash` | `int` | Holds “dash” for this scope. (integer) |
| `s1` | `string` | Holds “s1” for this scope. (text) |
| `s2` | `string` | Holds “s2” for this scope. (text) |
| `contentLength` | `long` | Holds “content Length” for this scope. (integer) |
| `fs` | `var` | Holds “fs” for this scope.  Newly constructed object. |
| `buffer` | `var` | Holds “buffer” for this scope.  Newly constructed object. |
| `remaining` | `long` | Holds “remaining” for this scope. (integer) |
| `toRead` | `int` | Holds “to Read” for this scope. (integer) |
| `read` | `int` | Holds “read” for this scope. (integer) |

#### Code

```html
 295 | 
 296 |     private static void StreamFile(HttpContext context, string physical)
 297 |     {
 298 |         string fileName = Path.GetFileName(physical);
 299 |         // Prefer original name from .meta for Content-Disposition
 300 |         string metaPath = physical + ".meta";
 301 |         string downloadName = fileName;
 302 |         if (File.Exists(metaPath))
 303 |         {
 304 |             try
 305 |             {
 306 |                 string orig = File.ReadAllText(metaPath).Trim();
 307 |                 if (!string.IsNullOrEmpty(orig)) downloadName = Path.GetFileName(orig);
 308 |             }
 309 |             catch { }
 310 |         }
 311 | 
 312 |         string ext = Path.GetExtension(fileName).ToLowerInvariant();
 313 |         string contentType = MimeFromExt(ext);
 314 |         bool forceDownload = context.Request["dl"] == "1" || context.Request["download"] == "1";
 315 |         if (ext == ".doc" || ext == ".docx" || ext == ".ppt" || ext == ".pptx" || ext == ".pptm")
 316 |             forceDownload = true;
 317 | 
 318 |         long fileLength = new FileInfo(physical).Length;
 319 |         long start = 0;
 320 |         long end = fileLength - 1;
 321 |         bool isRange = false;
 322 | 
 323 |         string rangeHeader = context.Request.Headers["Range"];
 324 |         if (!forceDownload && !string.IsNullOrEmpty(rangeHeader) &&
 325 |             rangeHeader.StartsWith("bytes=", StringComparison.OrdinalIgnoreCase))
 326 |         {
 327 |             isRange = true;
 328 |             string spec = rangeHeader.Substring(6).Trim();
 329 |             int dash = spec.IndexOf('-');
 330 |             if (dash >= 0)
 331 |             {
 332 |                 string s1 = spec.Substring(0, dash).Trim();
 333 |                 string s2 = spec.Substring(dash + 1).Trim();
 334 |                 if (s1.Length > 0) long.TryParse(s1, NumberStyles.Integer, CultureInfo.InvariantCulture, out start);
 335 |                 if (s2.Length > 0) long.TryParse(s2, NumberStyles.Integer, CultureInfo.InvariantCulture, out end);
 336 |                 else end = fileLength - 1;
 337 |             }
 338 |             if (start < 0) start = 0;
 339 |             if (end >= fileLength) end = fileLength - 1;
 340 |             if (start > end || start >= fileLength)
 341 |             {
 342 |                 context.Response.StatusCode = 416;
 343 |                 context.Response.AddHeader("Content-Range", "bytes */" + fileLength);
 344 |                 return;
 345 |             }
 346 |         }
 347 | 
 348 |         long contentLength = end - start + 1;
 349 | 
 350 |         context.Response.ClearHeaders();
 351 |         context.Response.ClearContent();
 352 |         context.Response.BufferOutput = false;
 353 |         context.Response.ContentType = contentType;
 354 |         context.Response.AddHeader("Accept-Ranges", "bytes");
 355 |         context.Response.AddHeader("Content-Length", contentLength.ToString(CultureInfo.InvariantCulture));
 356 |         context.Response.AddHeader("Content-Disposition",
 357 |             (forceDownload ? "attachment" : "inline") + "; filename=\"" + downloadName.Replace("\"", "'") + "\"");
 358 | 
 359 |         if (isRange)
 360 |         {
 361 |             context.Response.StatusCode = 206;
 362 |             context.Response.AddHeader("Content-Range",
 363 |                 string.Format(CultureInfo.InvariantCulture, "bytes {0}-{1}/{2}", start, end, fileLength));
 364 |         }
 365 |         else context.Response.StatusCode = 200;
 366 | 
 367 |         using (var fs = new FileStream(physical, FileMode.Open, FileAccess.Read, FileShare.Read))
 368 |         {
 369 |             if (start > 0) fs.Seek(start, SeekOrigin.Begin);
 370 |             var buffer = new byte[81920];
 371 |             long remaining = contentLength;
 372 |             while (remaining > 0)
 373 |             {
 374 |                 if (!context.Response.IsClientConnected) return;
 375 |                 int toRead = remaining > buffer.Length ? buffer.Length : (int)remaining;
 376 |                 int read = fs.Read(buffer, 0, toRead);
 377 |                 if (read <= 0) break;
 378 |                 context.Response.OutputStream.Write(buffer, 0, read);
 379 |                 remaining -= read;
 380 |             }
 381 |         }
 382 |         try { context.Response.Flush(); } catch { }
 383 |     }
```

---

### `WriteDiag` — lines 384–420

#### Signature

```html
private static void WriteDiag(HttpContext context)
```

#### What it is

Function `WriteDiag` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `WriteDiag`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sb` | `var` | StringBuilder — efficient string concatenation.  Newly constructed object. |
| `uploads` | `string` | Often a collection related to uploads (plural name). (text) |
| `dir` | `string` | Filesystem or URL path. (text) |
| `files` | `var` | Often a collection related to files (plural name). |
| `n` | `int` | Integer count (rows, items, or length).  Literal number `0`. |
| `fi` | `var` | Holds “fi” for this scope.  Newly constructed object. |
| `note` | `string` | Holds “note” for this scope. (text)  Literal text string. |
| `root` | `—` | Root directory path (Uploads). |
| `file` | `—` | Uploaded file object or file name. |

#### Code

```html
 384 | 
 385 |     private static void WriteDiag(HttpContext context)
 386 |     {
 387 |         var sb = new StringBuilder();
 388 |         string uploads = context.Server.MapPath("~/Uploads");
 389 |         sb.AppendLine("EduLMS Media diagnostics");
 390 |         sb.AppendLine("AppPath: " + context.Request.ApplicationPath);
 391 |         sb.AppendLine("MapPath ~/Uploads: " + uploads);
 392 |         sb.AppendLine("Exists: " + Directory.Exists(uploads));
 393 |         if (Directory.Exists(uploads))
 394 |         {
 395 |             foreach (var root in AllowedRoots)
 396 |             {
 397 |                 string dir = Path.Combine(uploads, root);
 398 |                 sb.AppendLine();
 399 |                 sb.AppendLine("[" + root + "] exists=" + Directory.Exists(dir));
 400 |                 if (!Directory.Exists(dir)) continue;
 401 |                 var files = Directory.GetFiles(dir);
 402 |                 sb.AppendLine("  fileCount=" + files.Length);
 403 |                 int n = 0;
 404 |                 foreach (var file in files)
 405 |                 {
 406 |                     var fi = new FileInfo(file);
 407 |                     string note = "";
 408 |                     if (file.EndsWith(".meta", StringComparison.OrdinalIgnoreCase))
 409 |                     {
 410 |                         try { note = " => " + File.ReadAllText(file).Trim(); } catch { }
 411 |                     }
 412 |                     sb.AppendLine("  - " + fi.Name + " (" + fi.Length + " bytes)" + note);
 413 |                     if (++n >= 40) { sb.AppendLine("  ..."); break; }
 414 |                 }
 415 |             }
 416 |         }
 417 |         sb.AppendLine();
 418 |         sb.AppendLine("Test: " + VirtualPathUtility.ToAbsolute("~/Media.ashx") + "?f=CourseMaterials/YOUR_GUID.pdf");
 419 |         WriteText(context, 200, sb.ToString());
 420 |     }
```

---

### `WriteText` — lines 421–428

#### Signature

```html
private static void WriteText(HttpContext context, int code, string message)
```

#### What it is

Function `WriteText` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Write the HTTP response body (JSON, file bytes, or text).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |
| `code` | `int` | 6-digit TOTP / OTP the user typed. |
| `message` | `string` | Status text for the UI. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```html
 421 | 
 422 |     private static void WriteText(HttpContext context, int code, string message)
 423 |     {
 424 |         context.Response.Clear();
 425 |         context.Response.StatusCode = code;
 426 |         context.Response.ContentType = "text/plain; charset=utf-8";
 427 |         context.Response.Write(message ?? "");
 428 |     }
```

---

### `IsClientAbort` — lines 429–438

#### Signature

```html
private static bool IsClientAbort(Exception ex)
```

#### What it is

Checks a condition related to **Is Client Abort** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `IsClientAbort`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ex` | `Exception` | Exception object in catch blocks. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `m` | `string` | Holds “m” for this scope. (text) |

#### Code

```html
 429 | 
 430 |     private static bool IsClientAbort(Exception ex)
 431 |     {
 432 |         if (ex == null) return false;
 433 |         string m = ex.Message ?? "";
 434 |         if (m.IndexOf("remote host closed", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 435 |         if (m.IndexOf("client disconnected", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 436 |         if (m.IndexOf("aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 437 |         return ex.InnerException != null && IsClientAbort(ex.InnerException);
 438 |     }
```

---

### `MimeFromExt` — lines 439–460

#### Signature

```html
private static string MimeFromExt(string ext)
```

#### What it is

Function `MimeFromExt` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `MimeFromExt`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ext` | `string` | File extension (.pdf, .mp4, …). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```html
 439 | 
 440 |     private static string MimeFromExt(string ext)
 441 |     {
 442 |         switch (ext)
 443 |         {
 444 |             case ".pdf": return "application/pdf";
 445 |             case ".mp4": return "video/mp4";
 446 |             case ".webm": return "video/webm";
 447 |             case ".mov": return "video/quicktime";
 448 |             case ".png": return "image/png";
 449 |             case ".jpg":
 450 |             case ".jpeg": return "image/jpeg";
 451 |             case ".gif": return "image/gif";
 452 |             case ".webp": return "image/webp";
 453 |             case ".bmp": return "image/bmp";
 454 |             case ".doc": return "application/msword";
 455 |             case ".docx": return "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
 456 |             case ".ppt": return "application/vnd.ms-powerpoint";
 457 |             case ".pptx": return "application/vnd.openxmlformats-officedocument.presentationml.presentation";
 458 |             default: return "application/octet-stream";
 459 |         }
 460 |     }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ WebHandler Language="C#" Class="MediaHandler" %>
   2 | 
   3 | using System;
   4 | using System.Globalization;
   5 | using System.IO;
   6 | using System.Text;
   7 | using System.Web;
   8 | using WebAppAssignment.Data.Security;
   9 | 
  10 | /// <summary>
  11 | /// Serves lesson media from ~/Uploads/ only (path-sandboxed).
  12 | ///   /Media.ashx?f=CourseMaterials/{guid}.pdf
  13 | ///   /Media.ashx?f=CourseVideos/{guid}.mp4&amp;dl=1
  14 | ///   /Media.ashx?diag=1  (debug builds only)
  15 | /// </summary>
  16 | public class MediaHandler : IHttpHandler
  17 | {
  18 |     private static readonly string[] AllowedRoots = UploadPathGuard.AllowedRoots;
  19 | 
  20 |     public void ProcessRequest(HttpContext context)
  21 |     {
  22 |         try
  23 |         {
  24 |             if (context.Request["diag"] == "1" || context.Request["debug"] == "1")
  25 |             {
  26 |                 if (!context.IsDebuggingEnabled)
  27 |                 {
  28 |                     WriteText(context, 403, "Diagnostics disabled.");
  29 |                     return;
  30 |                 }
  31 |                 // Diag lists upload folders — lecturers/admins only
  32 |                 if (!AuthorizeFolder(context, "CourseMaterials"))
  33 |                     return;
  34 |                 WriteDiag(context);
  35 |                 return;
  36 |             }
  37 | 
  38 |             string f = context.Request["f"]
  39 |                        ?? context.Request["path"]
  40 |                        ?? context.Request["file"]
  41 |                        ?? "";
  42 | 
  43 |             string relative = UploadPathGuard.NormalizeRelative(f);
  44 |             if (string.IsNullOrEmpty(relative))
  45 |             {
  46 |                 // Bare filename → search allowed folders via .meta
  47 |                 string bare = (f ?? "").Replace('\\', '/').Trim().TrimStart('/');
  48 |                 if (!string.IsNullOrEmpty(bare) && bare.IndexOf('/') < 0 && bare.IndexOf("..") < 0)
  49 |                 {
  50 |                     // Never resolve bare names into submissions without a folder hint
  51 |                     string foundBare = FindByOriginalName(context, null, bare);
  52 |                     if (foundBare != null)
  53 |                     {
  54 |                         string relBare = ToRelativeUnderUploads(context, foundBare);
  55 |                         string folderBare = FirstFolder(relBare);
  56 |                         if (!AuthorizeFolder(context, folderBare))
  57 |                             return;
  58 |                         StreamFile(context, foundBare);
  59 |                         return;
  60 |                     }
  61 |                 }
  62 |                 WriteText(context, 400, "Missing or invalid f= parameter. Example: Media.ashx?f=CourseMaterials/abc123.pdf");
  63 |                 return;
  64 |             }
  65 | 
  66 |             var parts = relative.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
  67 |             string folder = parts.Length > 0 ? parts[0] : "";
  68 |             if (!AuthorizeFolder(context, folder))
  69 |                 return;
  70 | 
  71 |             string physical = UploadPathGuard.ToPhysical(context, relative);
  72 | 
  73 |             if (physical == null || !File.Exists(physical))
  74 |             {
  75 |                 // Resolve original display name → GUID file via .meta sidecars
  76 |                 string byMeta = parts.Length >= 2
  77 |                     ? FindByOriginalName(context, parts[0], parts[parts.Length - 1])
  78 |                     : null;
  79 |                 if (byMeta != null)
  80 |                 {
  81 |                     StreamFile(context, byMeta);
  82 |                     return;
  83 |                 }
  84 | 
  85 |                 if (context.IsDebuggingEnabled)
  86 |                 {
  87 |                     var sb = new StringBuilder();
  88 |                     sb.AppendLine("404 File not found");
  89 |                     sb.AppendLine("Requested: Uploads/" + relative);
  90 |                     WriteText(context, 404, sb.ToString());
  91 |                 }
  92 |                 else
  93 |                 {
  94 |                     WriteText(context, 404, "File not found.");
  95 |                 }
  96 |                 return;
  97 |             }
  98 | 
  99 |             string rootFull = Path.GetFullPath(context.Server.MapPath("~/Uploads"))
 100 |                 .TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
 101 |                 + Path.DirectorySeparatorChar;
 102 |             string full = Path.GetFullPath(physical);
 103 |             if (!full.StartsWith(rootFull, StringComparison.OrdinalIgnoreCase))
 104 |             {
 105 |                 WriteText(context, 403, "Access denied.");
 106 |                 return;
 107 |             }
 108 | 
 109 |             StreamFile(context, full);
 110 |         }
 111 |         catch (Exception ex)
 112 |         {
 113 |             if (IsClientAbort(ex)) return;
 114 |             try { WriteText(context, 500, context.IsDebuggingEnabled ? ("Media error: " + ex.Message) : "Media error."); } catch { }
 115 |         }
 116 |     }
 117 | 
 118 |     /// <summary>
 119 |     /// Access policy:
 120 |     /// - CourseThumbnails: public (Landing cards without login)
 121 |     /// - CourseMaterials / CourseVideos: any signed-in user (student/lecturer/admin)
 122 |     /// - CourseSubmissions: signed-in Student, Lecturer, or Admin only
 123 |     /// </summary>
 124 |     private static bool AuthorizeFolder(HttpContext context, string folder)
 125 |     {
 126 |         folder = (folder ?? "").Trim();
 127 |         if (string.IsNullOrEmpty(folder))
 128 |         {
 129 |             WriteText(context, 400, "Missing folder.");
 130 |             return false;
 131 |         }
 132 | 
 133 |         // Public catalog images only
 134 |         if (string.Equals(folder, "CourseThumbnails", StringComparison.OrdinalIgnoreCase))
 135 |             return true;
 136 | 
 137 |         int uid = AuthService.GetValidatedUserId(context);
 138 |         if (uid <= 0)
 139 |         {
 140 |             WriteText(context, 401, "Sign in required to access this file.");
 141 |             return false;
 142 |         }
 143 | 
 144 |         string role = AuthService.NormalizeRole(
 145 |             context.Session != null ? context.Session["UserRole"] as string : null);
 146 | 
 147 |         // Lesson materials / videos: any authenticated role
 148 |         if (string.Equals(folder, "CourseMaterials", StringComparison.OrdinalIgnoreCase) ||
 149 |             string.Equals(folder, "CourseVideos", StringComparison.OrdinalIgnoreCase))
 150 |             return true;
 151 | 
 152 |         // Student submission files: no anonymous; role must be Student/Lecturer/Admin
 153 |         if (string.Equals(folder, "CourseSubmissions", StringComparison.OrdinalIgnoreCase))
 154 |         {
 155 |             if (string.Equals(role, "Student", StringComparison.OrdinalIgnoreCase) ||
 156 |                 string.Equals(role, "Lecturer", StringComparison.OrdinalIgnoreCase) ||
 157 |                 string.Equals(role, "Admin", StringComparison.OrdinalIgnoreCase))
 158 |                 return true;
 159 | 
 160 |             WriteText(context, 403, "You do not have access to submission files.");
 161 |             return false;
 162 |         }
 163 | 
 164 |         WriteText(context, 403, "Folder not allowed.");
 165 |         return false;
 166 |     }
 167 | 
 168 |     private static string FirstFolder(string relative)
 169 |     {
 170 |         if (string.IsNullOrEmpty(relative)) return "";
 171 |         int slash = relative.IndexOf('/');
 172 |         return slash < 0 ? relative : relative.Substring(0, slash);
 173 |     }
 174 | 
 175 |     private static string ToRelativeUnderUploads(HttpContext context, string physical)
 176 |     {
 177 |         try
 178 |         {
 179 |             string root = Path.GetFullPath(context.Server.MapPath("~/Uploads"))
 180 |                 .TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
 181 |                 + Path.DirectorySeparatorChar;
 182 |             string full = Path.GetFullPath(physical);
 183 |             if (!full.StartsWith(root, StringComparison.OrdinalIgnoreCase)) return null;
 184 |             return full.Substring(root.Length).Replace('\\', '/');
 185 |         }
 186 |         catch { return null; }
 187 |     }
 188 | 
 189 |     /// <summary>
 190 |     /// Find a file by original upload name using .meta sidecars and uploads.log.
 191 |     /// </summary>
 192 |     private static string FindByOriginalName(HttpContext context, string folderOrNull, string originalName)
 193 |     {
 194 |         if (string.IsNullOrWhiteSpace(originalName)) return null;
 195 |         originalName = Path.GetFileName(originalName.Trim().Replace('\\', '/'));
 196 |         string uploads = context.Server.MapPath("~/Uploads");
 197 |         if (!Directory.Exists(uploads)) return null;
 198 | 
 199 |         string[] folders = string.IsNullOrEmpty(folderOrNull)
 200 |             ? AllowedRoots
 201 |             : new[] { folderOrNull };
 202 | 
 203 |         foreach (var folder in folders)
 204 |         {
 205 |             string dir = Path.Combine(uploads, folder);
 206 |             if (!Directory.Exists(dir)) continue;
 207 | 
 208 |             string exact = Path.Combine(dir, originalName);
 209 |             if (File.Exists(exact)) return exact;
 210 | 
 211 |             foreach (var meta in Directory.GetFiles(dir, "*.meta"))
 212 |             {
 213 |                 try
 214 |                 {
 215 |                     string content = Path.GetFileName(File.ReadAllText(meta).Trim().Replace('\\', '/'));
 216 |                     if (string.Equals(content, originalName, StringComparison.OrdinalIgnoreCase))
 217 |                     {
 218 |                         string dataFile = meta.Substring(0, meta.Length - 5);
 219 |                         if (File.Exists(dataFile)) return dataFile;
 220 |                     }
 221 |                 }
 222 |                 catch { }
 223 |             }
 224 |         }
 225 | 
 226 |         // Scan uploads.log: "OK under=CourseMaterials/{guid}.pdf original=My File.pdf"
 227 |         try
 228 |         {
 229 |             string log = Path.Combine(context.Server.MapPath("~/App_Data/Logs"), "uploads.log");
 230 |             if (File.Exists(log))
 231 |             {
 232 |                 foreach (var line in File.ReadAllLines(log))
 233 |                 {
 234 |                     if (line.IndexOf("original=", StringComparison.OrdinalIgnoreCase) < 0) continue;
 235 |                     if (line.IndexOf("under=", StringComparison.OrdinalIgnoreCase) < 0) continue;
 236 |                     int o = line.IndexOf("original=", StringComparison.OrdinalIgnoreCase);
 237 |                     string orig = line.Substring(o + 9).Trim();
 238 |                     int sp = orig.IndexOf(" bytes=");
 239 |                     if (sp > 0) orig = orig.Substring(0, sp).Trim();
 240 |                     orig = Path.GetFileName(orig.Replace('\\', '/'));
 241 |                     if (!string.Equals(orig, originalName, StringComparison.OrdinalIgnoreCase)) continue;
 242 | 
 243 |                     int u = line.IndexOf("under=", StringComparison.OrdinalIgnoreCase);
 244 |                     string under = line.Substring(u + 6).Trim();
 245 |                     int sp2 = under.IndexOf(' ');
 246 |                     if (sp2 > 0) under = under.Substring(0, sp2).Trim();
 247 |                     under = under.Replace('\\', '/').TrimStart('/');
 248 |                     if (under.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 249 |                         under = under.Substring(8);
 250 |                     string phys = context.Server.MapPath("~/Uploads/" + under);
 251 |                     if (File.Exists(phys))
 252 |                     {
 253 |                         // Write .meta for next time
 254 |                         try { File.WriteAllText(phys + ".meta", originalName, Encoding.UTF8); } catch { }
 255 |                         return phys;
 256 |                     }
 257 |                 }
 258 |             }
 259 |         }
 260 |         catch { }
 261 | 
 262 |         return null;
 263 |     }
 264 | 
 265 |     private static string NormalizeRequestPath(string f)
 266 |     {
 267 |         if (string.IsNullOrWhiteSpace(f)) return "";
 268 |         f = f.Replace('\\', '/').Trim().TrimStart('/');
 269 | 
 270 |         if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 271 |             f = f.Substring("Uploads/".Length);
 272 |         int up = f.IndexOf("/Uploads/", StringComparison.OrdinalIgnoreCase);
 273 |         if (up >= 0) f = f.Substring(up + "/Uploads/".Length);
 274 | 
 275 |         if (f.IndexOf("ServeUpload.ashx", StringComparison.OrdinalIgnoreCase) >= 0 ||
 276 |             f.IndexOf("Media.ashx", StringComparison.OrdinalIgnoreCase) >= 0)
 277 |         {
 278 |             int p = f.IndexOf("f=", StringComparison.OrdinalIgnoreCase);
 279 |             if (p < 0) p = f.IndexOf("path=", StringComparison.OrdinalIgnoreCase);
 280 |             if (p >= 0)
 281 |             {
 282 |                 string rest = f.Substring(p);
 283 |                 int eq = rest.IndexOf('=');
 284 |                 rest = eq >= 0 ? rest.Substring(eq + 1) : rest;
 285 |                 int amp = rest.IndexOf('&');
 286 |                 if (amp >= 0) rest = rest.Substring(0, amp);
 287 |                 try { f = HttpUtility.UrlDecode(rest); } catch { f = rest; }
 288 |                 f = f.TrimStart('/');
 289 |                 if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 290 |                     f = f.Substring("Uploads/".Length);
 291 |             }
 292 |         }
 293 |         return f;
 294 |     }
 295 | 
 296 |     private static void StreamFile(HttpContext context, string physical)
 297 |     {
 298 |         string fileName = Path.GetFileName(physical);
 299 |         // Prefer original name from .meta for Content-Disposition
 300 |         string metaPath = physical + ".meta";
 301 |         string downloadName = fileName;
 302 |         if (File.Exists(metaPath))
 303 |         {
 304 |             try
 305 |             {
 306 |                 string orig = File.ReadAllText(metaPath).Trim();
 307 |                 if (!string.IsNullOrEmpty(orig)) downloadName = Path.GetFileName(orig);
 308 |             }
 309 |             catch { }
 310 |         }
 311 | 
 312 |         string ext = Path.GetExtension(fileName).ToLowerInvariant();
 313 |         string contentType = MimeFromExt(ext);
 314 |         bool forceDownload = context.Request["dl"] == "1" || context.Request["download"] == "1";
 315 |         if (ext == ".doc" || ext == ".docx" || ext == ".ppt" || ext == ".pptx" || ext == ".pptm")
 316 |             forceDownload = true;
 317 | 
 318 |         long fileLength = new FileInfo(physical).Length;
 319 |         long start = 0;
 320 |         long end = fileLength - 1;
 321 |         bool isRange = false;
 322 | 
 323 |         string rangeHeader = context.Request.Headers["Range"];
 324 |         if (!forceDownload && !string.IsNullOrEmpty(rangeHeader) &&
 325 |             rangeHeader.StartsWith("bytes=", StringComparison.OrdinalIgnoreCase))
 326 |         {
 327 |             isRange = true;
 328 |             string spec = rangeHeader.Substring(6).Trim();
 329 |             int dash = spec.IndexOf('-');
 330 |             if (dash >= 0)
 331 |             {
 332 |                 string s1 = spec.Substring(0, dash).Trim();
 333 |                 string s2 = spec.Substring(dash + 1).Trim();
 334 |                 if (s1.Length > 0) long.TryParse(s1, NumberStyles.Integer, CultureInfo.InvariantCulture, out start);
 335 |                 if (s2.Length > 0) long.TryParse(s2, NumberStyles.Integer, CultureInfo.InvariantCulture, out end);
 336 |                 else end = fileLength - 1;
 337 |             }
 338 |             if (start < 0) start = 0;
 339 |             if (end >= fileLength) end = fileLength - 1;
 340 |             if (start > end || start >= fileLength)
 341 |             {
 342 |                 context.Response.StatusCode = 416;
 343 |                 context.Response.AddHeader("Content-Range", "bytes */" + fileLength);
 344 |                 return;
 345 |             }
 346 |         }
 347 | 
 348 |         long contentLength = end - start + 1;
 349 | 
 350 |         context.Response.ClearHeaders();
 351 |         context.Response.ClearContent();
 352 |         context.Response.BufferOutput = false;
 353 |         context.Response.ContentType = contentType;
 354 |         context.Response.AddHeader("Accept-Ranges", "bytes");
 355 |         context.Response.AddHeader("Content-Length", contentLength.ToString(CultureInfo.InvariantCulture));
 356 |         context.Response.AddHeader("Content-Disposition",
 357 |             (forceDownload ? "attachment" : "inline") + "; filename=\"" + downloadName.Replace("\"", "'") + "\"");
 358 | 
 359 |         if (isRange)
 360 |         {
 361 |             context.Response.StatusCode = 206;
 362 |             context.Response.AddHeader("Content-Range",
 363 |                 string.Format(CultureInfo.InvariantCulture, "bytes {0}-{1}/{2}", start, end, fileLength));
 364 |         }
 365 |         else context.Response.StatusCode = 200;
 366 | 
 367 |         using (var fs = new FileStream(physical, FileMode.Open, FileAccess.Read, FileShare.Read))
 368 |         {
 369 |             if (start > 0) fs.Seek(start, SeekOrigin.Begin);
 370 |             var buffer = new byte[81920];
 371 |             long remaining = contentLength;
 372 |             while (remaining > 0)
 373 |             {
 374 |                 if (!context.Response.IsClientConnected) return;
 375 |                 int toRead = remaining > buffer.Length ? buffer.Length : (int)remaining;
 376 |                 int read = fs.Read(buffer, 0, toRead);
 377 |                 if (read <= 0) break;
 378 |                 context.Response.OutputStream.Write(buffer, 0, read);
 379 |                 remaining -= read;
 380 |             }
 381 |         }
 382 |         try { context.Response.Flush(); } catch { }
 383 |     }
 384 | 
 385 |     private static void WriteDiag(HttpContext context)
 386 |     {
 387 |         var sb = new StringBuilder();
 388 |         string uploads = context.Server.MapPath("~/Uploads");
 389 |         sb.AppendLine("EduLMS Media diagnostics");
 390 |         sb.AppendLine("AppPath: " + context.Request.ApplicationPath);
 391 |         sb.AppendLine("MapPath ~/Uploads: " + uploads);
 392 |         sb.AppendLine("Exists: " + Directory.Exists(uploads));
 393 |         if (Directory.Exists(uploads))
 394 |         {
 395 |             foreach (var root in AllowedRoots)
 396 |             {
 397 |                 string dir = Path.Combine(uploads, root);
 398 |                 sb.AppendLine();
 399 |                 sb.AppendLine("[" + root + "] exists=" + Directory.Exists(dir));
 400 |                 if (!Directory.Exists(dir)) continue;
 401 |                 var files = Directory.GetFiles(dir);
 402 |                 sb.AppendLine("  fileCount=" + files.Length);
 403 |                 int n = 0;
 404 |                 foreach (var file in files)
 405 |                 {
 406 |                     var fi = new FileInfo(file);
 407 |                     string note = "";
 408 |                     if (file.EndsWith(".meta", StringComparison.OrdinalIgnoreCase))
 409 |                     {
 410 |                         try { note = " => " + File.ReadAllText(file).Trim(); } catch { }
 411 |                     }
 412 |                     sb.AppendLine("  - " + fi.Name + " (" + fi.Length + " bytes)" + note);
 413 |                     if (++n >= 40) { sb.AppendLine("  ..."); break; }
 414 |                 }
 415 |             }
 416 |         }
 417 |         sb.AppendLine();
 418 |         sb.AppendLine("Test: " + VirtualPathUtility.ToAbsolute("~/Media.ashx") + "?f=CourseMaterials/YOUR_GUID.pdf");
 419 |         WriteText(context, 200, sb.ToString());
 420 |     }
 421 | 
 422 |     private static void WriteText(HttpContext context, int code, string message)
 423 |     {
 424 |         context.Response.Clear();
 425 |         context.Response.StatusCode = code;
 426 |         context.Response.ContentType = "text/plain; charset=utf-8";
 427 |         context.Response.Write(message ?? "");
 428 |     }
 429 | 
 430 |     private static bool IsClientAbort(Exception ex)
 431 |     {
 432 |         if (ex == null) return false;
 433 |         string m = ex.Message ?? "";
 434 |         if (m.IndexOf("remote host closed", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 435 |         if (m.IndexOf("client disconnected", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 436 |         if (m.IndexOf("aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 437 |         return ex.InnerException != null && IsClientAbort(ex.InnerException);
 438 |     }
 439 | 
 440 |     private static string MimeFromExt(string ext)
 441 |     {
 442 |         switch (ext)
 443 |         {
 444 |             case ".pdf": return "application/pdf";
 445 |             case ".mp4": return "video/mp4";
 446 |             case ".webm": return "video/webm";
 447 |             case ".mov": return "video/quicktime";
 448 |             case ".png": return "image/png";
 449 |             case ".jpg":
 450 |             case ".jpeg": return "image/jpeg";
 451 |             case ".gif": return "image/gif";
 452 |             case ".webp": return "image/webp";
 453 |             case ".bmp": return "image/bmp";
 454 |             case ".doc": return "application/msword";
 455 |             case ".docx": return "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
 456 |             case ".ppt": return "application/vnd.ms-powerpoint";
 457 |             case ".pptx": return "application/vnd.openxmlformats-officedocument.presentationml.presentation";
 458 |             default: return "application/octet-stream";
 459 |         }
 460 |     }
 461 | 
 462 |     public bool IsReusable { get { return false; } }
 463 | }
```
