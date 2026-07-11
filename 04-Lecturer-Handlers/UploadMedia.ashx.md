# UploadMedia.ashx
**Source:** `Pages/Lecturer/UploadMedia.ashx`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Authenticated upload of materials/videos/submissions with magic-byte validation.

## File overview

- **Total lines:** 231
- **Kind:** `.ashx`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (2 found)

### `ProcessRequest` — lines 17–222

```html
public void ProcessRequest(HttpContext context)
```

#### Explanation

- **Purpose:** Implements `ProcessRequest`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `context` (`HttpContext`) — Holds “context” for this scope. (current HTTP request)
- **Local variables (what each means):**
- `kind` (`string`) — Upload kind (material/video/thumbnail/submission).  Comes from HTTP request.
- `isSubmission` (`bool`) — Boolean flag: is Submission. (true/false)
- `originalName` (`var`) — Holds “original Name” for this scope.
- `ext` (`var`) — File extension (.pdf, .mp4, …).
- `videoExts` (`var`) — Often a collection related to video Exts (plural name).
- `materialExts` (`var`) — Often a collection related to material Exts (plural name).
- `imageExts` (`var`) — Often a collection related to image Exts (plural name).
- `uploadsRoot` (`string`) — Holds “uploads Root” for this scope. (text)
- `uploadsFolder` (`string`) — Filesystem or URL path. (text)
- `keep` (`string`) — Holds “keep” for this scope. (text)
- `savedName` (`var`) — Holds “saved Name” for this scope.
- `savePath` (`var`) — Filesystem or URL path.
- `written` (`long`) — Holds “written” for this scope. (integer)  Newly constructed object.
- `under` (`string`) — Holds “under” for this scope. (text)
- `storePath` (`string`) — Relative path where file was saved.  Literal text string.
- `mediaBase` (`string`) — Holds “media Base” for this scope. (text)
- `serveUrl` (`string`) — Public/handler URL to download/preview file.
- `downloadUrl` (`string`) — URL string. (text)
- `absUrl` (`string`) — URL string. (text)
- `logDir` (`string`) — Filesystem or URL path. (text)

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L17:** IHttpHandler entry for ashx.
- **L22:** Error handling block.
- **L24:** `kind` means: Upload kind (material/video/thumbnail/submission).  Comes from HTTP request.
- **L25:** `isSubmission` means: Boolean flag: is Submission. (true/false)
- **L30:** Authorization — block wrong role / anonymous.
- **L34:** Authorization — block wrong role / anonymous.
- **L47:** `originalName` means: Holds “original Name” for this scope.
- **L48:** `ext` means: File extension (.pdf, .mp4, …).
- **L55:** File magic-byte validation on upload.
- **L56:** Validate upload by file signature.
- **L58:** Write/read security audit events.
- **L59:** File magic-byte validation on upload.
- **L63:** `videoExts` means: Often a collection related to video Exts (plural name).
- **L64:** `materialExts` means: Often a collection related to material Exts (plural name).
- **L65:** `imageExts` means: Often a collection related to image Exts (plural name).
- **L126:** `uploadsRoot` means: Holds “uploads Root” for this scope. (text)
- **L130:** `uploadsFolder` means: Filesystem or URL path. (text)
- **L135:** `keep` means: Holds “keep” for this scope. (text)
- **L138:** Error handling block.
- **L142:** `savedName` means: Holds “saved Name” for this scope.
- **L143:** `savePath` means: Filesystem or URL path.
- **L157:** `written` means: Holds “written” for this scope. (integer)  Newly constructed object.
- **L165:** Error handling block.
- **L169:** Handle/log exception.
- **L172:** `under` means: Holds “under” for this scope. (text)
- **L173:** `storePath` means: Relative path where file was saved.  Literal text string.
- **L176:** `mediaBase` means: Holds “media Base” for this scope. (text)
- **L177:** `serveUrl` means: Public/handler URL to download/preview file.
- **L178:** `downloadUrl` means: URL string. (text)
- **L179:** `absUrl` means: URL string. (text)
- **L181:** Error handling block.
- **L183:** `logDir` means: Filesystem or URL path. (text)
- **L189:** Handle/log exception.
- **L191:** Error handling block.
- **L209:** Handle/log exception.
- **L211:** Error handling block.
- **L213:** `logDir` means: Filesystem or URL path. (text)
- **L218:** Handle/log exception.

---

### `WriteJson` — lines 223–228

```html
private void WriteJson(HttpContext context, object obj)
```

#### Explanation

- **Purpose:** Implements `WriteJson`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `context` (`HttpContext`) — Holds “context” for this scope. (current HTTP request)
- `obj` (`object`) — Holds “obj” for this scope.
- **Local variables (what each means):**
- `js` (`var`) — Holds “js” for this scope.  Newly constructed object.

#### Line-by-line (this function)

```html
 223 | 
 224 |     private void WriteJson(HttpContext context, object obj)
 225 |     {
 226 |         var js = new JavaScriptSerializer();
 227 |         context.Response.Write(js.Serialize(obj));
 228 |     }
```

**Line notes** (what code + variables mean)

- **L226:** `js` means: Holds “js” for this scope.  Newly constructed object.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L7:** Import namespace/types.
- **L8:** Import namespace/types.
- **L9:** Import namespace/types.
- **L15:** Class declaration for this page/service.
- **L17:** IHttpHandler entry for ashx.
- **L22:** Error handling block.
- **L24:** `kind` means: Upload kind (material/video/thumbnail/submission).  Comes from HTTP request.
- **L25:** `isSubmission` means: Boolean flag: is Submission. (true/false)
- **L30:** Authorization — block wrong role / anonymous.
- **L34:** Authorization — block wrong role / anonymous.
- **L47:** `originalName` means: Holds “original Name” for this scope.
- **L48:** `ext` means: File extension (.pdf, .mp4, …).
- **L55:** File magic-byte validation on upload.
- **L56:** Validate upload by file signature.
- **L58:** Write/read security audit events.
- **L59:** File magic-byte validation on upload.
- **L63:** `videoExts` means: Often a collection related to video Exts (plural name).
- **L64:** `materialExts` means: Often a collection related to material Exts (plural name).
- **L65:** `imageExts` means: Often a collection related to image Exts (plural name).
- **L126:** `uploadsRoot` means: Holds “uploads Root” for this scope. (text)
- **L130:** `uploadsFolder` means: Filesystem or URL path. (text)
- **L135:** `keep` means: Holds “keep” for this scope. (text)
- **L138:** Error handling block.
- **L142:** `savedName` means: Holds “saved Name” for this scope.
- **L143:** `savePath` means: Filesystem or URL path.
- **L157:** `written` means: Holds “written” for this scope. (integer)  Newly constructed object.
- **L165:** Error handling block.
- **L169:** Handle/log exception.
- **L172:** `under` means: Holds “under” for this scope. (text)
- **L173:** `storePath` means: Relative path where file was saved.  Literal text string.
- **L176:** `mediaBase` means: Holds “media Base” for this scope. (text)
- **L177:** `serveUrl` means: Public/handler URL to download/preview file.
- **L178:** `downloadUrl` means: URL string. (text)
- **L179:** `absUrl` means: URL string. (text)
- **L181:** Error handling block.
- **L183:** `logDir` means: Filesystem or URL path. (text)
- **L189:** Handle/log exception.
- **L191:** Error handling block.
- **L209:** Handle/log exception.
- **L211:** Error handling block.
- **L213:** `logDir` means: Filesystem or URL path. (text)
- **L218:** Handle/log exception.
- **L226:** `js` means: Holds “js” for this scope.  Newly constructed object.

## Source snapshot (raw)

```html
<%@ WebHandler Language="C#" Class="UploadMedia" %>

using System;
using System.IO;
using System.Text;
using System.Web;
using System.Web.Script.Serialization;
using System.Web.SessionState;
using WebAppAssignment.Data.Security;

/// <summary>
/// Saves lesson media under ~/Uploads/{CourseVideos|CourseMaterials}/
/// Requires authentication. Submissions: any logged-in user. Materials/videos: Lecturer/Admin.
/// </summary>
public class UploadMedia : IHttpHandler, IRequiresSessionState
{
    public void ProcessRequest(HttpContext context)
    {
        context.Response.ContentType = "application/json; charset=utf-8";
        context.Response.Cache.SetCacheability(HttpCacheability.NoCache);

        try
        {
            string kind = (context.Request["kind"] ?? context.Request.Form["kind"] ?? "").Trim().ToLowerInvariant();
            bool isSubmission = kind == "submission" || kind == "submissions" || kind == "answer";

            int uid;
            if (isSubmission)
            {
                if (!AuthGate.EnsureHandlerUser(context, out uid)) return;
            }
            else
            {
                if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin")) return;
            }

            HttpPostedFile file = null;
            if (context.Request.Files.Count > 0)
                file = context.Request.Files["file"] ?? context.Request.Files[0];

            if (file == null || file.ContentLength <= 0)
            {
                WriteJson(context, new { success = false, message = "No file uploaded. Use multipart form field 'file'." });
                return;
            }

            var originalName = Path.GetFileName(file.FileName);
            var ext = Path.GetExtension(originalName).ToLowerInvariant();
            if (string.IsNullOrEmpty(ext))
            {
                WriteJson(context, new { success = false, message = "File must have an extension." });
                return;
            }

            string magicMsg;
            if (!FileMagic.LooksValid(file, ext, out magicMsg))
            {
                SecurityAudit.Log("upload.reject", uid, magicMsg + " ext=" + ext);
                WriteJson(context, new { success = false, message = magicMsg ?? "File content does not match extension." });
                return;
            }

            var videoExts = new[] { ".mp4", ".webm", ".mov" };
            var materialExts = new[] { ".pdf", ".ppt", ".pptx", ".docx", ".pptm", ".doc", ".txt", ".zip" };
            var imageExts = new[] { ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp" };

            // kind already resolved above (auth)
            string subFolder;
            long maxSize;

            if (isSubmission)
            {
                // Student assessment files (prefer PDF; allow office/images too)
                if (Array.IndexOf(videoExts, ext) >= 0)
                {
                    subFolder = "CourseSubmissions";
                    maxSize = 100L * 1024 * 1024;
                }
                else if (Array.IndexOf(materialExts, ext) >= 0 || Array.IndexOf(imageExts, ext) >= 0)
                {
                    subFolder = "CourseSubmissions";
                    maxSize = 30L * 1024 * 1024;
                }
                else
                {
                    WriteJson(context, new { success = false, message = "Submission file type not allowed: " + ext });
                    return;
                }
            }
            else if (Array.IndexOf(videoExts, ext) >= 0)
            {
                subFolder = "CourseVideos";
                maxSize = 200L * 1024 * 1024;
            }
            else if (Array.IndexOf(materialExts, ext) >= 0)
            {
                subFolder = "CourseMaterials";
                maxSize = 30L * 1024 * 1024;
            }
            else if (Array.IndexOf(imageExts, ext) >= 0)
            {
                subFolder = "CourseMaterials";
                maxSize = 10L * 1024 * 1024;
            }
            else
            {
                WriteJson(context, new
                {
                    success = false,
                    message = "File type not allowed: " + ext
                });
                return;
            }

            if (file.ContentLength > maxSize)
            {
                WriteJson(context, new
                {
                    success = false,
                    message = "File too large (" + (file.ContentLength / (1024 * 1024)) + " MB)."
                });
                return;
            }

            // Ensure uploads root + subfolder exist (physical under site)
            string uploadsRoot = context.Server.MapPath("~/Uploads");
            if (!Directory.Exists(uploadsRoot))
                Directory.CreateDirectory(uploadsRoot);

            string uploadsFolder = Path.Combine(uploadsRoot, subFolder);
            if (!Directory.Exists(uploadsFolder))
                Directory.CreateDirectory(uploadsFolder);

            // Write a marker so folder is never empty/missing in git/IIS
            string keep = Path.Combine(uploadsFolder, ".keep");
            if (!File.Exists(keep))
            {
                try { File.WriteAllText(keep, "keep"); } catch { }
            }

            // ALWAYS save as GUID on disk — never the original file name
            var savedName = Guid.NewGuid().ToString("N") + ext;
            var savePath = Path.Combine(uploadsFolder, savedName);
            file.SaveAs(savePath);

            // Verify write
            if (!File.Exists(savePath))
            {
                WriteJson(context, new
                {
                    success = false,
                    message = "Save reported OK but file missing on disk: " + savePath
                });
                return;
            }

            long written = new FileInfo(savePath).Length;
            if (written <= 0)
            {
                WriteJson(context, new { success = false, message = "Saved file is empty: " + savePath });
                return;
            }

            // Sidecar maps GUID file → original name (for Media.ashx fallback + download filename)
            try
            {
                File.WriteAllText(savePath + ".meta", originalName ?? savedName, Encoding.UTF8);
            }
            catch { }

            // Portable store path for DB — MUST be the GUID path, not original name
            string under = subFolder + "/" + savedName;            // CourseMaterials/{guid}.pdf
            string storePath = "Uploads/" + under;                 // Uploads/CourseMaterials/{guid}.pdf

            // ALWAYS use root Media.ashx for view/download
            string mediaBase = VirtualPathUtility.ToAbsolute("~/Media.ashx");
            string serveUrl = mediaBase + "?f=" + HttpUtility.UrlEncode(under);
            string downloadUrl = serveUrl + "&dl=1";
            string absUrl = VirtualPathUtility.ToAbsolute("~/" + storePath);

            try
            {
                string logDir = context.Server.MapPath("~/App_Data/Logs");
                if (!Directory.Exists(logDir)) Directory.CreateDirectory(logDir);
                File.AppendAllText(Path.Combine(logDir, "uploads.log"),
                    DateTime.Now.ToString("s") + " OK under=" + under +
                    " original=" + originalName + " bytes=" + written + Environment.NewLine);
            }
            catch { }

            try { SecurityAudit.Log("upload.ok", uid, under + " original=" + originalName); } catch { }

            WriteJson(context, new
            {
                success = true,
                // Prefer GUID store path for DB fields (not original name, not Media.ashx URL)
                url = storePath,
                storePath = storePath,
                under = under,
                serveUrl = serveUrl,
                downloadUrl = downloadUrl,
                staticUrl = absUrl,
                fileName = originalName,
                size = written,
                physical = savePath,
                ext = ext
            });
        }
        catch (Exception ex)
        {
            try
            {
                string logDir = context.Server.MapPath("~/App_Data/Logs");
                if (!Directory.Exists(logDir)) Directory.CreateDirectory(logDir);
                File.AppendAllText(Path.Combine(logDir, "uploads.log"),
                    DateTime.Now.ToString("s") + " FAIL " + ex.Message + Environment.NewLine);
            }
            catch { }
            // Do not leak exception details to client
            WriteJson(context, new { success = false, message = "Upload failed. Check file type/size and try again." });
        }
    }

    private void WriteJson(HttpContext context, object obj)
    {
        var js = new JavaScriptSerializer();
        context.Response.Write(js.Serialize(obj));
    }

    public bool IsReusable { get { return false; } }
}

```
