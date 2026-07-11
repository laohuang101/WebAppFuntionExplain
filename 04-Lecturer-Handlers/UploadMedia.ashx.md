# UploadMedia.ashx
**Source:** `Pages/Lecturer/UploadMedia.ashx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Authenticated upload of materials/videos/submissions with magic-byte validation.

## File overview

- **Total lines:** 231
- **Kind:** `.ashx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (2 found)

### `ProcessRequest` — lines 17–222

#### Signature

```html
public void ProcessRequest(HttpContext context)
```

#### What it is

Main entry point for an `.ashx` HTTP handler — handles one browser request from start to finish.

#### How it works

1. Check the caller’s role (Lecturer/Student/Admin). If not allowed, return an error and stop.
2. Write an audit-log row for this security event.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `kind` | `string` | Upload kind (material/video/thumbnail/submission).  Comes from HTTP request. |
| `isSubmission` | `bool` | Boolean flag: is Submission. (true/false) |
| `originalName` | `var` | Holds “original Name” for this scope. |
| `ext` | `var` | File extension (.pdf, .mp4, …). |
| `videoExts` | `var` | Often a collection related to video Exts (plural name). |
| `materialExts` | `var` | Often a collection related to material Exts (plural name). |
| `imageExts` | `var` | Often a collection related to image Exts (plural name). |
| `uploadsRoot` | `string` | Holds “uploads Root” for this scope. (text) |
| `uploadsFolder` | `string` | Filesystem or URL path. (text) |
| `keep` | `string` | Holds “keep” for this scope. (text) |
| `savedName` | `var` | Holds “saved Name” for this scope. |
| `savePath` | `var` | Filesystem or URL path. |
| `written` | `long` | Holds “written” for this scope. (integer)  Newly constructed object. |
| `under` | `string` | Holds “under” for this scope. (text) |
| `storePath` | `string` | Relative path where file was saved.  Literal text string. |
| `mediaBase` | `string` | Holds “media Base” for this scope. (text) |
| `serveUrl` | `string` | Public/handler URL to download/preview file. |
| `downloadUrl` | `string` | URL string. (text) |
| `absUrl` | `string` | URL string. (text) |
| `logDir` | `string` | Filesystem or URL path. (text) |

#### Code

```html
  17 |     public void ProcessRequest(HttpContext context)
  18 |     {
  19 |         context.Response.ContentType = "application/json; charset=utf-8";
  20 |         context.Response.Cache.SetCacheability(HttpCacheability.NoCache);
  21 | 
  22 |         try
  23 |         {
  24 |             string kind = (context.Request["kind"] ?? context.Request.Form["kind"] ?? "").Trim().ToLowerInvariant();
  25 |             bool isSubmission = kind == "submission" || kind == "submissions" || kind == "answer";
  26 | 
  27 |             int uid;
  28 |             if (isSubmission)
  29 |             {
  30 |                 if (!AuthGate.EnsureHandlerUser(context, out uid)) return;
  31 |             }
  32 |             else
  33 |             {
  34 |                 if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin")) return;
  35 |             }
  36 | 
  37 |             HttpPostedFile file = null;
  38 |             if (context.Request.Files.Count > 0)
  39 |                 file = context.Request.Files["file"] ?? context.Request.Files[0];
  40 | 
  41 |             if (file == null || file.ContentLength <= 0)
  42 |             {
  43 |                 WriteJson(context, new { success = false, message = "No file uploaded. Use multipart form field 'file'." });
  44 |                 return;
  45 |             }
  46 | 
  47 |             var originalName = Path.GetFileName(file.FileName);
  48 |             var ext = Path.GetExtension(originalName).ToLowerInvariant();
  49 |             if (string.IsNullOrEmpty(ext))
  50 |             {
  51 |                 WriteJson(context, new { success = false, message = "File must have an extension." });
  52 |                 return;
  53 |             }
  54 | 
  55 |             string magicMsg;
  56 |             if (!FileMagic.LooksValid(file, ext, out magicMsg))
  57 |             {
  58 |                 SecurityAudit.Log("upload.reject", uid, magicMsg + " ext=" + ext);
  59 |                 WriteJson(context, new { success = false, message = magicMsg ?? "File content does not match extension." });
  60 |                 return;
  61 |             }
  62 | 
  63 |             var videoExts = new[] { ".mp4", ".webm", ".mov" };
  64 |             var materialExts = new[] { ".pdf", ".ppt", ".pptx", ".docx", ".pptm", ".doc", ".txt", ".zip" };
  65 |             var imageExts = new[] { ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp" };
  66 | 
  67 |             // kind already resolved above (auth)
  68 |             string subFolder;
  69 |             long maxSize;
  70 | 
  71 |             if (isSubmission)
  72 |             {
  73 |                 // Student assessment files (prefer PDF; allow office/images too)
  74 |                 if (Array.IndexOf(videoExts, ext) >= 0)
  75 |                 {
  76 |                     subFolder = "CourseSubmissions";
  77 |                     maxSize = 100L * 1024 * 1024;
  78 |                 }
  79 |                 else if (Array.IndexOf(materialExts, ext) >= 0 || Array.IndexOf(imageExts, ext) >= 0)
  80 |                 {
  81 |                     subFolder = "CourseSubmissions";
  82 |                     maxSize = 30L * 1024 * 1024;
  83 |                 }
  84 |                 else
  85 |                 {
  86 |                     WriteJson(context, new { success = false, message = "Submission file type not allowed: " + ext });
  87 |                     return;
  88 |                 }
  89 |             }
  90 |             else if (Array.IndexOf(videoExts, ext) >= 0)
  91 |             {
  92 |                 subFolder = "CourseVideos";
  93 |                 maxSize = 200L * 1024 * 1024;
  94 |             }
  95 |             else if (Array.IndexOf(materialExts, ext) >= 0)
  96 |             {
  97 |                 subFolder = "CourseMaterials";
  98 |                 maxSize = 30L * 1024 * 1024;
  99 |             }
 100 |             else if (Array.IndexOf(imageExts, ext) >= 0)
 101 |             {
 102 |                 subFolder = "CourseMaterials";
 103 |                 maxSize = 10L * 1024 * 1024;
 104 |             }
 105 |             else
 106 |             {
 107 |                 WriteJson(context, new
 108 |                 {
 109 |                     success = false,
 110 |                     message = "File type not allowed: " + ext
 111 |                 });
 112 |                 return;
 113 |             }
 114 | 
 115 |             if (file.ContentLength > maxSize)
 116 |             {
 117 |                 WriteJson(context, new
 118 |                 {
 119 |                     success = false,
 120 |                     message = "File too large (" + (file.ContentLength / (1024 * 1024)) + " MB)."
 121 |                 });
 122 |                 return;
 123 |             }
 124 | 
 125 |             // Ensure uploads root + subfolder exist (physical under site)
 126 |             string uploadsRoot = context.Server.MapPath("~/Uploads");
 127 |             if (!Directory.Exists(uploadsRoot))
 128 |                 Directory.CreateDirectory(uploadsRoot);
 129 | 
 130 |             string uploadsFolder = Path.Combine(uploadsRoot, subFolder);
 131 |             if (!Directory.Exists(uploadsFolder))
 132 |                 Directory.CreateDirectory(uploadsFolder);
 133 | 
 134 |             // Write a marker so folder is never empty/missing in git/IIS
 135 |             string keep = Path.Combine(uploadsFolder, ".keep");
 136 |             if (!File.Exists(keep))
 137 |             {
 138 |                 try { File.WriteAllText(keep, "keep"); } catch { }
 139 |             }
 140 | 
 141 |             // ALWAYS save as GUID on disk — never the original file name
 142 |             var savedName = Guid.NewGuid().ToString("N") + ext;
 143 |             var savePath = Path.Combine(uploadsFolder, savedName);
 144 |             file.SaveAs(savePath);
 145 | 
 146 |             // Verify write
 147 |             if (!File.Exists(savePath))
 148 |             {
 149 |                 WriteJson(context, new
 150 |                 {
 151 |                     success = false,
 152 |                     message = "Save reported OK but file missing on disk: " + savePath
 153 |                 });
 154 |                 return;
 155 |             }
 156 | 
 157 |             long written = new FileInfo(savePath).Length;
 158 |             if (written <= 0)
 159 |             {
 160 |                 WriteJson(context, new { success = false, message = "Saved file is empty: " + savePath });
 161 |                 return;
 162 |             }
 163 | 
 164 |             // Sidecar maps GUID file → original name (for Media.ashx fallback + download filename)
 165 |             try
 166 |             {
 167 |                 File.WriteAllText(savePath + ".meta", originalName ?? savedName, Encoding.UTF8);
 168 |             }
 169 |             catch { }
 170 | 
 171 |             // Portable store path for DB — MUST be the GUID path, not original name
 172 |             string under = subFolder + "/" + savedName;            // CourseMaterials/{guid}.pdf
 173 |             string storePath = "Uploads/" + under;                 // Uploads/CourseMaterials/{guid}.pdf
 174 | 
 175 |             // ALWAYS use root Media.ashx for view/download
 176 |             string mediaBase = VirtualPathUtility.ToAbsolute("~/Media.ashx");
 177 |             string serveUrl = mediaBase + "?f=" + HttpUtility.UrlEncode(under);
 178 |             string downloadUrl = serveUrl + "&dl=1";
 179 |             string absUrl = VirtualPathUtility.ToAbsolute("~/" + storePath);
 180 | 
 181 |             try
 182 |             {
 183 |                 string logDir = context.Server.MapPath("~/App_Data/Logs");
 184 |                 if (!Directory.Exists(logDir)) Directory.CreateDirectory(logDir);
 185 |                 File.AppendAllText(Path.Combine(logDir, "uploads.log"),
 186 |                     DateTime.Now.ToString("s") + " OK under=" + under +
 187 |                     " original=" + originalName + " bytes=" + written + Environment.NewLine);
 188 |             }
 189 |             catch { }
 190 | 
 191 |             try { SecurityAudit.Log("upload.ok", uid, under + " original=" + originalName); } catch { }
 192 | 
 193 |             WriteJson(context, new
 194 |             {
 195 |                 success = true,
 196 |                 // Prefer GUID store path for DB fields (not original name, not Media.ashx URL)
 197 |                 url = storePath,
 198 |                 storePath = storePath,
 199 |                 under = under,
 200 |                 serveUrl = serveUrl,
 201 |                 downloadUrl = downloadUrl,
 202 |                 staticUrl = absUrl,
 203 |                 fileName = originalName,
 204 |                 size = written,
 205 |                 physical = savePath,
 206 |                 ext = ext
 207 |             });
 208 |         }
 209 |         catch (Exception ex)
 210 |         {
 211 |             try
 212 |             {
 213 |                 string logDir = context.Server.MapPath("~/App_Data/Logs");
 214 |                 if (!Directory.Exists(logDir)) Directory.CreateDirectory(logDir);
 215 |                 File.AppendAllText(Path.Combine(logDir, "uploads.log"),
 216 |                     DateTime.Now.ToString("s") + " FAIL " + ex.Message + Environment.NewLine);
 217 |             }
 218 |             catch { }
 219 |             // Do not leak exception details to client
 220 |             WriteJson(context, new { success = false, message = "Upload failed. Check file type/size and try again." });
 221 |         }
 222 |     }
```

---

### `WriteJson` — lines 223–228

#### Signature

```html
private void WriteJson(HttpContext context, object obj)
```

#### What it is

Function `WriteJson` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Write the HTTP response body (JSON, file bytes, or text).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `context` | `HttpContext` | Holds “context” for this scope. (current HTTP request) |
| `obj` | `object` | Holds “obj” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `js` | `var` | Holds “js” for this scope.  Newly constructed object. |

#### Code

```html
 223 | 
 224 |     private void WriteJson(HttpContext context, object obj)
 225 |     {
 226 |         var js = new JavaScriptSerializer();
 227 |         context.Response.Write(js.Serialize(obj));
 228 |     }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ WebHandler Language="C#" Class="UploadMedia" %>
   2 | 
   3 | using System;
   4 | using System.IO;
   5 | using System.Text;
   6 | using System.Web;
   7 | using System.Web.Script.Serialization;
   8 | using System.Web.SessionState;
   9 | using WebAppAssignment.Data.Security;
  10 | 
  11 | /// <summary>
  12 | /// Saves lesson media under ~/Uploads/{CourseVideos|CourseMaterials}/
  13 | /// Requires authentication. Submissions: any logged-in user. Materials/videos: Lecturer/Admin.
  14 | /// </summary>
  15 | public class UploadMedia : IHttpHandler, IRequiresSessionState
  16 | {
  17 |     public void ProcessRequest(HttpContext context)
  18 |     {
  19 |         context.Response.ContentType = "application/json; charset=utf-8";
  20 |         context.Response.Cache.SetCacheability(HttpCacheability.NoCache);
  21 | 
  22 |         try
  23 |         {
  24 |             string kind = (context.Request["kind"] ?? context.Request.Form["kind"] ?? "").Trim().ToLowerInvariant();
  25 |             bool isSubmission = kind == "submission" || kind == "submissions" || kind == "answer";
  26 | 
  27 |             int uid;
  28 |             if (isSubmission)
  29 |             {
  30 |                 if (!AuthGate.EnsureHandlerUser(context, out uid)) return;
  31 |             }
  32 |             else
  33 |             {
  34 |                 if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin")) return;
  35 |             }
  36 | 
  37 |             HttpPostedFile file = null;
  38 |             if (context.Request.Files.Count > 0)
  39 |                 file = context.Request.Files["file"] ?? context.Request.Files[0];
  40 | 
  41 |             if (file == null || file.ContentLength <= 0)
  42 |             {
  43 |                 WriteJson(context, new { success = false, message = "No file uploaded. Use multipart form field 'file'." });
  44 |                 return;
  45 |             }
  46 | 
  47 |             var originalName = Path.GetFileName(file.FileName);
  48 |             var ext = Path.GetExtension(originalName).ToLowerInvariant();
  49 |             if (string.IsNullOrEmpty(ext))
  50 |             {
  51 |                 WriteJson(context, new { success = false, message = "File must have an extension." });
  52 |                 return;
  53 |             }
  54 | 
  55 |             string magicMsg;
  56 |             if (!FileMagic.LooksValid(file, ext, out magicMsg))
  57 |             {
  58 |                 SecurityAudit.Log("upload.reject", uid, magicMsg + " ext=" + ext);
  59 |                 WriteJson(context, new { success = false, message = magicMsg ?? "File content does not match extension." });
  60 |                 return;
  61 |             }
  62 | 
  63 |             var videoExts = new[] { ".mp4", ".webm", ".mov" };
  64 |             var materialExts = new[] { ".pdf", ".ppt", ".pptx", ".docx", ".pptm", ".doc", ".txt", ".zip" };
  65 |             var imageExts = new[] { ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp" };
  66 | 
  67 |             // kind already resolved above (auth)
  68 |             string subFolder;
  69 |             long maxSize;
  70 | 
  71 |             if (isSubmission)
  72 |             {
  73 |                 // Student assessment files (prefer PDF; allow office/images too)
  74 |                 if (Array.IndexOf(videoExts, ext) >= 0)
  75 |                 {
  76 |                     subFolder = "CourseSubmissions";
  77 |                     maxSize = 100L * 1024 * 1024;
  78 |                 }
  79 |                 else if (Array.IndexOf(materialExts, ext) >= 0 || Array.IndexOf(imageExts, ext) >= 0)
  80 |                 {
  81 |                     subFolder = "CourseSubmissions";
  82 |                     maxSize = 30L * 1024 * 1024;
  83 |                 }
  84 |                 else
  85 |                 {
  86 |                     WriteJson(context, new { success = false, message = "Submission file type not allowed: " + ext });
  87 |                     return;
  88 |                 }
  89 |             }
  90 |             else if (Array.IndexOf(videoExts, ext) >= 0)
  91 |             {
  92 |                 subFolder = "CourseVideos";
  93 |                 maxSize = 200L * 1024 * 1024;
  94 |             }
  95 |             else if (Array.IndexOf(materialExts, ext) >= 0)
  96 |             {
  97 |                 subFolder = "CourseMaterials";
  98 |                 maxSize = 30L * 1024 * 1024;
  99 |             }
 100 |             else if (Array.IndexOf(imageExts, ext) >= 0)
 101 |             {
 102 |                 subFolder = "CourseMaterials";
 103 |                 maxSize = 10L * 1024 * 1024;
 104 |             }
 105 |             else
 106 |             {
 107 |                 WriteJson(context, new
 108 |                 {
 109 |                     success = false,
 110 |                     message = "File type not allowed: " + ext
 111 |                 });
 112 |                 return;
 113 |             }
 114 | 
 115 |             if (file.ContentLength > maxSize)
 116 |             {
 117 |                 WriteJson(context, new
 118 |                 {
 119 |                     success = false,
 120 |                     message = "File too large (" + (file.ContentLength / (1024 * 1024)) + " MB)."
 121 |                 });
 122 |                 return;
 123 |             }
 124 | 
 125 |             // Ensure uploads root + subfolder exist (physical under site)
 126 |             string uploadsRoot = context.Server.MapPath("~/Uploads");
 127 |             if (!Directory.Exists(uploadsRoot))
 128 |                 Directory.CreateDirectory(uploadsRoot);
 129 | 
 130 |             string uploadsFolder = Path.Combine(uploadsRoot, subFolder);
 131 |             if (!Directory.Exists(uploadsFolder))
 132 |                 Directory.CreateDirectory(uploadsFolder);
 133 | 
 134 |             // Write a marker so folder is never empty/missing in git/IIS
 135 |             string keep = Path.Combine(uploadsFolder, ".keep");
 136 |             if (!File.Exists(keep))
 137 |             {
 138 |                 try { File.WriteAllText(keep, "keep"); } catch { }
 139 |             }
 140 | 
 141 |             // ALWAYS save as GUID on disk — never the original file name
 142 |             var savedName = Guid.NewGuid().ToString("N") + ext;
 143 |             var savePath = Path.Combine(uploadsFolder, savedName);
 144 |             file.SaveAs(savePath);
 145 | 
 146 |             // Verify write
 147 |             if (!File.Exists(savePath))
 148 |             {
 149 |                 WriteJson(context, new
 150 |                 {
 151 |                     success = false,
 152 |                     message = "Save reported OK but file missing on disk: " + savePath
 153 |                 });
 154 |                 return;
 155 |             }
 156 | 
 157 |             long written = new FileInfo(savePath).Length;
 158 |             if (written <= 0)
 159 |             {
 160 |                 WriteJson(context, new { success = false, message = "Saved file is empty: " + savePath });
 161 |                 return;
 162 |             }
 163 | 
 164 |             // Sidecar maps GUID file → original name (for Media.ashx fallback + download filename)
 165 |             try
 166 |             {
 167 |                 File.WriteAllText(savePath + ".meta", originalName ?? savedName, Encoding.UTF8);
 168 |             }
 169 |             catch { }
 170 | 
 171 |             // Portable store path for DB — MUST be the GUID path, not original name
 172 |             string under = subFolder + "/" + savedName;            // CourseMaterials/{guid}.pdf
 173 |             string storePath = "Uploads/" + under;                 // Uploads/CourseMaterials/{guid}.pdf
 174 | 
 175 |             // ALWAYS use root Media.ashx for view/download
 176 |             string mediaBase = VirtualPathUtility.ToAbsolute("~/Media.ashx");
 177 |             string serveUrl = mediaBase + "?f=" + HttpUtility.UrlEncode(under);
 178 |             string downloadUrl = serveUrl + "&dl=1";
 179 |             string absUrl = VirtualPathUtility.ToAbsolute("~/" + storePath);
 180 | 
 181 |             try
 182 |             {
 183 |                 string logDir = context.Server.MapPath("~/App_Data/Logs");
 184 |                 if (!Directory.Exists(logDir)) Directory.CreateDirectory(logDir);
 185 |                 File.AppendAllText(Path.Combine(logDir, "uploads.log"),
 186 |                     DateTime.Now.ToString("s") + " OK under=" + under +
 187 |                     " original=" + originalName + " bytes=" + written + Environment.NewLine);
 188 |             }
 189 |             catch { }
 190 | 
 191 |             try { SecurityAudit.Log("upload.ok", uid, under + " original=" + originalName); } catch { }
 192 | 
 193 |             WriteJson(context, new
 194 |             {
 195 |                 success = true,
 196 |                 // Prefer GUID store path for DB fields (not original name, not Media.ashx URL)
 197 |                 url = storePath,
 198 |                 storePath = storePath,
 199 |                 under = under,
 200 |                 serveUrl = serveUrl,
 201 |                 downloadUrl = downloadUrl,
 202 |                 staticUrl = absUrl,
 203 |                 fileName = originalName,
 204 |                 size = written,
 205 |                 physical = savePath,
 206 |                 ext = ext
 207 |             });
 208 |         }
 209 |         catch (Exception ex)
 210 |         {
 211 |             try
 212 |             {
 213 |                 string logDir = context.Server.MapPath("~/App_Data/Logs");
 214 |                 if (!Directory.Exists(logDir)) Directory.CreateDirectory(logDir);
 215 |                 File.AppendAllText(Path.Combine(logDir, "uploads.log"),
 216 |                     DateTime.Now.ToString("s") + " FAIL " + ex.Message + Environment.NewLine);
 217 |             }
 218 |             catch { }
 219 |             // Do not leak exception details to client
 220 |             WriteJson(context, new { success = false, message = "Upload failed. Check file type/size and try again." });
 221 |         }
 222 |     }
 223 | 
 224 |     private void WriteJson(HttpContext context, object obj)
 225 |     {
 226 |         var js = new JavaScriptSerializer();
 227 |         context.Response.Write(js.Serialize(obj));
 228 |     }
 229 | 
 230 |     public bool IsReusable { get { return false; } }
 231 | }
```
