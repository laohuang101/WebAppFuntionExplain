# ServeUpload.ashx
**Source:** `Pages/Lecturer/ServeUpload.ashx`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 361
- **Kind:** `.ashx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (6 found)

### `ProcessRequest` — lines 17–47

```html
public void ProcessRequest(HttpContext context)
```

#### Explanation

- **Purpose:** Implements `ProcessRequest`.
- **Navigation:** Redirects the browser.
- **Parameters:** `HttpContext context`
- **Local variables:** `path`, `media`, `qs`

#### Line-by-line (this function)

```html
  17 | 
  18 |     public void ProcessRequest(HttpContext context)
  19 |     {
  20 |         // Always delegate to Media.ashx (auth + path policy live there). No direct stream.
  21 |         try
  22 |         {
  23 |             string path = context.Request.QueryString["path"]
  24 |                 ?? context.Request["path"]
  25 |                 ?? context.Request["f"]
  26 |                 ?? "";
  27 |             if (string.IsNullOrWhiteSpace(path))
  28 |             {
  29 |                 SafeError(context, 400, "Missing path. Use Media.ashx?f=CourseMaterials/file.pdf");
  30 |                 return;
  31 |             }
  32 |             string media = VirtualPathUtility.ToAbsolute("~/Media.ashx");
  33 |             string qs = "f=" + HttpUtility.UrlEncode(path);
  34 |             if (context.Request["dl"] == "1") qs += "&dl=1";
  35 |             context.Response.Redirect(media + "?" + qs, false);
  36 |             context.ApplicationInstance.CompleteRequest();
  37 |         }
  38 |         catch (HttpException hex)
  39 |         {
  40 |             if (IsClientAbort(hex)) return;
  41 |             SafeError(context, 500, "Redirect error.");
  42 |         }
  43 |         catch (Exception)
  44 |         {
  45 |             SafeError(context, 500, "Redirect error.");
  46 |         }
  47 |     }
```

**Line notes**

- **L18:** IHttpHandler entry for ashx.
- **L21:** Error handling block.
- **L35:** Navigate browser to another URL.
- **L38:** Handle/log exception.
- **L43:** Handle/log exception.

---

### `Serve` — lines 48–248

```html
private static void Serve(HttpContext context)
```

#### Explanation

- **Purpose:** Implements `Serve`.
- **Parameters:** `HttpContext context`
- **Local variables:** `path`, `parts`, `allowed`, `relativeUnderUploads`, `rootWithSep`, `fileName`, `ext`, `contentType`, `forceDownload`, `isRange`, `rangeHeader`, `spec`, `dash`, `s1`, `s2`, `disposition`, `safeName`, `fs`, `buffer`, `toRead`, `read`

#### Line-by-line (this function)

```html
  48 | 
  49 |     private static void Serve(HttpContext context)
  50 |     {
  51 |         if (context == null || context.Request == null || context.Response == null) return;
  52 | 
  53 |         string path = context.Request.QueryString["path"]
  54 |                       ?? context.Request["path"]
  55 |                       ?? "";
  56 |         // Request may already decode once — only decode if still percent-encoded
  57 |         if (path.IndexOf('%') >= 0)
  58 |         {
  59 |             try { path = HttpUtility.UrlDecode(path); } catch { /* keep raw */ }
  60 |         }
  61 |         path = (path ?? "").Replace('\\', '/').Trim();
  62 | 
  63 |         if (string.IsNullOrEmpty(path))
  64 |         {
  65 |             SafeError(context, 400, "Missing path. Use ?path=CourseMaterials/file.pdf");
  66 |             return;
  67 |         }
  68 | 
  69 |         path = NormalizeToUploadsRelative(path, context);
  70 |         if (string.IsNullOrEmpty(path))
  71 |         {
  72 |             SafeError(context, 400, "Invalid path.");
  73 |             return;
  74 |         }
  75 | 
  76 |         var parts = path.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
  77 |         if (parts.Length < 2)
  78 |         {
  79 |             SafeError(context, 400, "Path must be Folder/filename (got: " + path + ")");
  80 |             return;
  81 |         }
  82 | 
  83 |         bool allowed = false;
  84 |         foreach (var root in AllowedRoots)
  85 |         {
  86 |             if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))
  87 |             {
  88 |                 allowed = true;
  89 |                 break;
  90 |             }
  91 |         }
  92 |         if (!allowed)
  93 |         {
  94 |             SafeError(context, 403, "Folder not allowed: " + parts[0]);
  95 |             return;
  96 |         }
  97 | 
  98 |         foreach (var p in parts)
  99 |         {
 100 |             if (p == ".." || p == "." || p.IndexOf(':') >= 0)
 101 |             {
 102 |                 SafeError(context, 400, "Invalid path segment.");
 103 |                 return;
 104 |             }
 105 |         }
 106 | 
 107 |         string relativeUnderUploads = string.Join("/", parts);
 108 |         string physical;
 109 |         try
 110 |         {
 111 |             physical = context.Server.MapPath("~/Uploads/" + relativeUnderUploads);
 112 |         }
 113 |         catch (Exception ex)
 114 |         {
 115 |             SafeError(context, 400, "MapPath failed: " + ex.Message);
 116 |             return;
 117 |         }
 118 | 
 119 |         if (string.IsNullOrEmpty(physical) || !File.Exists(physical))
 120 |         {
 121 |             // Help debug: show what we looked for
 122 |             SafeError(context, 404, "File not found: Uploads/" + relativeUnderUploads);
 123 |             return;
 124 |         }
 125 | 
 126 |         string uploadsRoot;
 127 |         string full;
 128 |         try
 129 |         {
 130 |             uploadsRoot = Path.GetFullPath(context.Server.MapPath("~/Uploads"));
 131 |             full = Path.GetFullPath(physical);
 132 |         }
 133 |         catch (Exception ex)
 134 |         {
 135 |             SafeError(context, 500, "Path resolve failed: " + ex.Message);
 136 |             return;
 137 |         }
 138 | 
 139 |         // Ensure trailing separator so UploadsX is not treated as under Uploads
 140 |         string rootWithSep = uploadsRoot.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
 141 |                              + Path.DirectorySeparatorChar;
 142 |         if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)
 143 |             && !string.Equals(full, uploadsRoot, StringComparison.OrdinalIgnoreCase))
 144 |         {
 145 |             SafeError(context, 403, "Access denied.");
 146 |             return;
 147 |         }
 148 | 
 149 |         string fileName = Path.GetFileName(full);
 150 |         string ext = Path.GetExtension(fileName).ToLowerInvariant();
 151 |         string contentType = MimeFromExt(ext);
 152 |         bool forceDownload = context.Request["dl"] == "1" || context.Request["download"] == "1";
 153 | 
 154 |         if (ext == ".doc" || ext == ".docx" || ext == ".ppt" || ext == ".pptx" || ext == ".pptm")
 155 |             forceDownload = true;
 156 | 
 157 |         long fileLength;
 158 |         try { fileLength = new FileInfo(full).Length; }
 159 |         catch (Exception ex)
 160 |         {
 161 |             SafeError(context, 500, "Cannot read file size: " + ex.Message);
 162 |             return;
 163 |         }
 164 | 
 165 |         // Parse Range: bytes=start-end (required for HTML5 video)
 166 |         long start = 0;
 167 |         long end = fileLength - 1;
 168 |         bool isRange = false;
 169 |         string rangeHeader = context.Request.Headers["Range"];
 170 |         if (!forceDownload && !string.IsNullOrEmpty(rangeHeader) && rangeHeader.StartsWith("bytes=", StringComparison.OrdinalIgnoreCase))
 171 |         {
 172 |             isRange = true;
 173 |             string spec = rangeHeader.Substring("bytes=".Length).Trim();
 174 |             int dash = spec.IndexOf('-');
 175 |             if (dash >= 0)
 176 |             {
 177 |                 string s1 = spec.Substring(0, dash).Trim();
 178 |                 string s2 = spec.Substring(dash + 1).Trim();
 179 |                 if (s1.Length > 0) long.TryParse(s1, NumberStyles.Integer, CultureInfo.InvariantCulture, out start);
 180 |                 if (s2.Length > 0) long.TryParse(s2, NumberStyles.Integer, CultureInfo.InvariantCulture, out end);
 181 |                 else end = fileLength - 1;
 182 |             }
 183 |             if (start < 0) start = 0;
 184 |             if (end >= fileLength) end = fileLength - 1;
 185 |             if (start > end || start >= fileLength)
 186 |             {
 187 |                 context.Response.StatusCode = 416;
 188 |                 context.Response.AddHeader("Content-Range", "bytes */" + fileLength);
 189 |                 return;
 190 |             }
 191 |         }
 192 | 
 193 |         long contentLength = end - start + 1;
 194 | 
 195 |         try
 196 |         {
 197 |             context.Response.ClearHeaders();
 198 |             context.Response.ClearContent();
 199 |             context.Response.BufferOutput = false;
 200 |             context.Response.ContentType = contentType;
 201 |             context.Response.AddHeader("Accept-Ranges", "bytes");
 202 |             context.Response.AddHeader("Content-Length", contentLength.ToString(CultureInfo.InvariantCulture));
 203 | 
 204 |             string disposition = forceDownload ? "attachment" : "inline";
 205 |             string safeName = fileName.Replace("\"", "'");
 206 |             context.Response.AddHeader("Content-Disposition", disposition + "; filename=\"" + safeName + "\"");
 207 | 
 208 |             if (isRange)
 209 |             {
 210 |                 context.Response.StatusCode = 206;
 211 |                 context.Response.AddHeader("Content-Range",
 212 |                     string.Format(CultureInfo.InvariantCulture, "bytes {0}-{1}/{2}", start, end, fileLength));
 213 |             }
 214 |             else
 215 |             {
 216 |                 context.Response.StatusCode = 200;
 217 |             }
 218 | 
 219 |             // Stream file (works better than TransmitFile under IIS Express + video)
 220 |             using (var fs = new FileStream(full, FileMode.Open, FileAccess.Read, FileShare.Read))
 221 |             {
 222 |                 if (start > 0) fs.Seek(start, SeekOrigin.Begin);
 223 |                 var buffer = new byte[81920];
 224 |                 long remaining = contentLength;
 225 |                 while (remaining > 0)
 226 |                 {
 227 |                     if (!context.Response.IsClientConnected) return;
 228 |                     int toRead = remaining > buffer.Length ? buffer.Length : (int)remaining;
 229 |                     int read = fs.Read(buffer, 0, toRead);
 230 |                     if (read <= 0) break;
 231 |                     context.Response.OutputStream.Write(buffer, 0, read);
 232 |                     remaining -= read;
 233 |                 }
 234 |             }
 235 |             try { context.Response.Flush(); } catch { /* client gone */ }
 236 |         }
 237 |         catch (Exception ex)
 238 |         {
 239 |             if (IsClientAbort(ex)) return;
 240 |             // Headers may already be sent — avoid second write that throws again
 241 |             try
 242 |             {
 243 |                 if (!context.Response.HeadersWritten)
 244 |                     SafeError(context, 500, ex.Message);
 245 |             }
 246 |             catch { }
 247 |         }
 248 |     }
```

**Line notes**

- **L59:** Error handling block.
- **L109:** Error handling block.
- **L113:** Handle/log exception.
- **L128:** Error handling block.
- **L133:** Handle/log exception.
- **L158:** Error handling block.
- **L159:** Handle/log exception.
- **L195:** Error handling block.
- **L220:** Import namespace/types.
- **L235:** Error handling block.
- **L237:** Handle/log exception.
- **L241:** Error handling block.
- **L246:** Handle/log exception.

---

### `SafeError` — lines 249–263

```html
private static void SafeError(HttpContext context, int code, string message)
```

#### Explanation

- **Purpose:** Implements `SafeError`.
- **Parameters:** `HttpContext context, int code, string message`

#### Line-by-line (this function)

```html
 249 | 
 250 |     private static void SafeError(HttpContext context, int code, string message)
 251 |     {
 252 |         try
 253 |         {
 254 |             if (context == null || context.Response == null) return;
 255 |             if (context.Response.HeadersWritten) return;
 256 |             context.Response.ClearHeaders();
 257 |             context.Response.ClearContent();
 258 |             context.Response.StatusCode = code;
 259 |             context.Response.ContentType = "text/plain; charset=utf-8";
 260 |             context.Response.Write(message ?? "Error");
 261 |         }
 262 |         catch { /* ignore */ }
 263 |     }
```

**Line notes**

- **L252:** Error handling block.
- **L262:** Handle/log exception.

---

### `IsClientAbort` — lines 264–276

```html
private static bool IsClientAbort(Exception ex)
```

#### Explanation

- **Purpose:** Implements `IsClientAbort`.
- **Parameters:** `Exception ex`
- **Local variables:** `m`

#### Line-by-line (this function)

```html
 264 | 
 265 |     private static bool IsClientAbort(Exception ex)
 266 |     {
 267 |         if (ex == null) return false;
 268 |         string m = ex.Message ?? "";
 269 |         if (m.IndexOf("remote host closed", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 270 |         if (m.IndexOf("The client disconnected", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 271 |         if (m.IndexOf("operation was aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 272 |         if (m.IndexOf("thread was being aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 273 |         if (ex is HttpException && ((HttpException)ex).ErrorCode == unchecked((int)0x800704CD)) return true;
 274 |         if (ex.InnerException != null) return IsClientAbort(ex.InnerException);
 275 |         return false;
 276 |     }
```

---

### `NormalizeToUploadsRelative` — lines 281–336

```html
public static string NormalizeToUploadsRelative(string path, HttpContext context)
```

#### Explanation

- **Purpose:** Implements `NormalizeToUploadsRelative`.
- **Parameters:** `string path, HttpContext context`
- **Local variables:** `uri`, `q`, `pq`, `rest`, `amp`, `app`, `up`

#### Line-by-line (this function)

```html
 281 |     public static string NormalizeToUploadsRelative(string path, HttpContext context)
 282 |     {
 283 |         if (string.IsNullOrWhiteSpace(path)) return null;
 284 |         path = path.Replace('\\', '/').Trim();
 285 | 
 286 |         if (path.StartsWith("http://", StringComparison.OrdinalIgnoreCase) ||
 287 |             path.StartsWith("https://", StringComparison.OrdinalIgnoreCase))
 288 |         {
 289 |             try
 290 |             {
 291 |                 var uri = new Uri(path);
 292 |                 path = uri.AbsolutePath;
 293 |                 // Also handle ?path= nested (shouldn't happen)
 294 |             }
 295 |             catch { return null; }
 296 |         }
 297 | 
 298 |         // If someone passed the full ServeUpload URL as path, extract its path query
 299 |         int q = path.IndexOf("ServeUpload.ashx", StringComparison.OrdinalIgnoreCase);
 300 |         if (q >= 0)
 301 |         {
 302 |             int pq = path.IndexOf("path=", StringComparison.OrdinalIgnoreCase);
 303 |             if (pq >= 0)
 304 |             {
 305 |                 string rest = path.Substring(pq + 5);
 306 |                 int amp = rest.IndexOf('&');
 307 |                 if (amp >= 0) rest = rest.Substring(0, amp);
 308 |                 try { path = HttpUtility.UrlDecode(rest); } catch { path = rest; }
 309 |             }
 310 |             else return null;
 311 |         }
 312 | 
 313 |         if (path.StartsWith("~/")) path = path.Substring(2);
 314 |         path = path.TrimStart('/');
 315 | 
 316 |         string app = (context != null && context.Request != null)
 317 |             ? (context.Request.ApplicationPath ?? "/").Trim('/')
 318 |             : "";
 319 |         if (!string.IsNullOrEmpty(app) && path.StartsWith(app + "/", StringComparison.OrdinalIgnoreCase))
 320 |             path = path.Substring(app.Length + 1);
 321 | 
 322 |         // Drop "Pages/Lecturer/" if a bad relative path was stored
 323 |         if (path.StartsWith("Pages/", StringComparison.OrdinalIgnoreCase))
 324 |         {
 325 |             int up = path.IndexOf("Uploads/", StringComparison.OrdinalIgnoreCase);
 326 |             if (up >= 0) path = path.Substring(up);
 327 |         }
 328 | 
 329 |         if (path.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 330 |             path = path.Substring("Uploads/".Length);
 331 |         else if (path.StartsWith("Upload/", StringComparison.OrdinalIgnoreCase))
 332 |             path = path.Substring("Upload/".Length);
 333 | 
 334 |         path = path.TrimStart('/');
 335 |         return string.IsNullOrEmpty(path) ? null : path;
 336 |     }
```

**Line notes**

- **L289:** Error handling block.
- **L295:** Handle/log exception.
- **L308:** Error handling block.

---

### `MimeFromExt` — lines 337–358

```html
private static string MimeFromExt(string ext)
```

#### Explanation

- **Purpose:** Implements `MimeFromExt`.
- **Parameters:** `string ext`

#### Line-by-line (this function)

```html
 337 | 
 338 |     private static string MimeFromExt(string ext)
 339 |     {
 340 |         switch (ext)
 341 |         {
 342 |             case ".pdf": return "application/pdf";
 343 |             case ".mp4": return "video/mp4";
 344 |             case ".webm": return "video/webm";
 345 |             case ".mov": return "video/quicktime";
 346 |             case ".png": return "image/png";
 347 |             case ".jpg":
 348 |             case ".jpeg": return "image/jpeg";
 349 |             case ".gif": return "image/gif";
 350 |             case ".webp": return "image/webp";
 351 |             case ".bmp": return "image/bmp";
 352 |             case ".doc": return "application/msword";
 353 |             case ".docx": return "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
 354 |             case ".ppt": return "application/vnd.ms-powerpoint";
 355 |             case ".pptx": return "application/vnd.openxmlformats-officedocument.presentationml.presentation";
 356 |             default: return "application/octet-stream";
 357 |         }
 358 |     }
```

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```html
   1 | <%@ WebHandler Language="C#" Class="ServeUpload" %>
   2 | 
   3 | using System;
   4 | using System.Globalization;
   5 | using System.IO;
   6 | using System.Web;
   7 | 
   8 | /// <summary>
   9 | /// Serves files under ~/Uploads for inline preview (PDF/video/image) or download.
  10 | /// Supports HTTP Range requests so HTML5 video can seek without 500 errors.
  11 | /// Query: ?path=CourseMaterials/file.pdf  or  ?path=Uploads/CourseVideos/x.mp4
  12 | /// Optional: &amp;dl=1 forces download
  13 | /// </summary>
  14 | public class ServeUpload : IHttpHandler
  15 | {
  16 |     private static readonly string[] AllowedRoots = { "CourseMaterials", "CourseVideos", "CourseThumbnails" };
  17 | 
  18 |     public void ProcessRequest(HttpContext context)
  19 |     {
  20 |         // Always delegate to Media.ashx (auth + path policy live there). No direct stream.
  21 |         try
  22 |         {
  23 |             string path = context.Request.QueryString["path"]
  24 |                 ?? context.Request["path"]
  25 |                 ?? context.Request["f"]
  26 |                 ?? "";
  27 |             if (string.IsNullOrWhiteSpace(path))
  28 |             {
  29 |                 SafeError(context, 400, "Missing path. Use Media.ashx?f=CourseMaterials/file.pdf");
  30 |                 return;
  31 |             }
  32 |             string media = VirtualPathUtility.ToAbsolute("~/Media.ashx");
  33 |             string qs = "f=" + HttpUtility.UrlEncode(path);
  34 |             if (context.Request["dl"] == "1") qs += "&dl=1";
  35 |             context.Response.Redirect(media + "?" + qs, false);
  36 |             context.ApplicationInstance.CompleteRequest();
  37 |         }
  38 |         catch (HttpException hex)
  39 |         {
  40 |             if (IsClientAbort(hex)) return;
  41 |             SafeError(context, 500, "Redirect error.");
  42 |         }
  43 |         catch (Exception)
  44 |         {
  45 |             SafeError(context, 500, "Redirect error.");
  46 |         }
  47 |     }
  48 | 
  49 |     private static void Serve(HttpContext context)
  50 |     {
  51 |         if (context == null || context.Request == null || context.Response == null) return;
  52 | 
  53 |         string path = context.Request.QueryString["path"]
  54 |                       ?? context.Request["path"]
  55 |                       ?? "";
  56 |         // Request may already decode once — only decode if still percent-encoded
  57 |         if (path.IndexOf('%') >= 0)
  58 |         {
  59 |             try { path = HttpUtility.UrlDecode(path); } catch { /* keep raw */ }
  60 |         }
  61 |         path = (path ?? "").Replace('\\', '/').Trim();
  62 | 
  63 |         if (string.IsNullOrEmpty(path))
  64 |         {
  65 |             SafeError(context, 400, "Missing path. Use ?path=CourseMaterials/file.pdf");
  66 |             return;
  67 |         }
  68 | 
  69 |         path = NormalizeToUploadsRelative(path, context);
  70 |         if (string.IsNullOrEmpty(path))
  71 |         {
  72 |             SafeError(context, 400, "Invalid path.");
  73 |             return;
  74 |         }
  75 | 
  76 |         var parts = path.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
  77 |         if (parts.Length < 2)
  78 |         {
  79 |             SafeError(context, 400, "Path must be Folder/filename (got: " + path + ")");
  80 |             return;
  81 |         }
  82 | 
  83 |         bool allowed = false;
  84 |         foreach (var root in AllowedRoots)
  85 |         {
  86 |             if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))
  87 |             {
  88 |                 allowed = true;
  89 |                 break;
  90 |             }
  91 |         }
  92 |         if (!allowed)
  93 |         {
  94 |             SafeError(context, 403, "Folder not allowed: " + parts[0]);
  95 |             return;
  96 |         }
  97 | 
  98 |         foreach (var p in parts)
  99 |         {
 100 |             if (p == ".." || p == "." || p.IndexOf(':') >= 0)
 101 |             {
 102 |                 SafeError(context, 400, "Invalid path segment.");
 103 |                 return;
 104 |             }
 105 |         }
 106 | 
 107 |         string relativeUnderUploads = string.Join("/", parts);
 108 |         string physical;
 109 |         try
 110 |         {
 111 |             physical = context.Server.MapPath("~/Uploads/" + relativeUnderUploads);
 112 |         }
 113 |         catch (Exception ex)
 114 |         {
 115 |             SafeError(context, 400, "MapPath failed: " + ex.Message);
 116 |             return;
 117 |         }
 118 | 
 119 |         if (string.IsNullOrEmpty(physical) || !File.Exists(physical))
 120 |         {
 121 |             // Help debug: show what we looked for
 122 |             SafeError(context, 404, "File not found: Uploads/" + relativeUnderUploads);
 123 |             return;
 124 |         }
 125 | 
 126 |         string uploadsRoot;
 127 |         string full;
 128 |         try
 129 |         {
 130 |             uploadsRoot = Path.GetFullPath(context.Server.MapPath("~/Uploads"));
 131 |             full = Path.GetFullPath(physical);
 132 |         }
 133 |         catch (Exception ex)
 134 |         {
 135 |             SafeError(context, 500, "Path resolve failed: " + ex.Message);
 136 |             return;
 137 |         }
 138 | 
 139 |         // Ensure trailing separator so UploadsX is not treated as under Uploads
 140 |         string rootWithSep = uploadsRoot.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
 141 |                              + Path.DirectorySeparatorChar;
 142 |         if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)
 143 |             && !string.Equals(full, uploadsRoot, StringComparison.OrdinalIgnoreCase))
 144 |         {
 145 |             SafeError(context, 403, "Access denied.");
 146 |             return;
 147 |         }
 148 | 
 149 |         string fileName = Path.GetFileName(full);
 150 |         string ext = Path.GetExtension(fileName).ToLowerInvariant();
 151 |         string contentType = MimeFromExt(ext);
 152 |         bool forceDownload = context.Request["dl"] == "1" || context.Request["download"] == "1";
 153 | 
 154 |         if (ext == ".doc" || ext == ".docx" || ext == ".ppt" || ext == ".pptx" || ext == ".pptm")
 155 |             forceDownload = true;
 156 | 
 157 |         long fileLength;
 158 |         try { fileLength = new FileInfo(full).Length; }
 159 |         catch (Exception ex)
 160 |         {
 161 |             SafeError(context, 500, "Cannot read file size: " + ex.Message);
 162 |             return;
 163 |         }
 164 | 
 165 |         // Parse Range: bytes=start-end (required for HTML5 video)
 166 |         long start = 0;
 167 |         long end = fileLength - 1;
 168 |         bool isRange = false;
 169 |         string rangeHeader = context.Request.Headers["Range"];
 170 |         if (!forceDownload && !string.IsNullOrEmpty(rangeHeader) && rangeHeader.StartsWith("bytes=", StringComparison.OrdinalIgnoreCase))
 171 |         {
 172 |             isRange = true;
 173 |             string spec = rangeHeader.Substring("bytes=".Length).Trim();
 174 |             int dash = spec.IndexOf('-');
 175 |             if (dash >= 0)
 176 |             {
 177 |                 string s1 = spec.Substring(0, dash).Trim();
 178 |                 string s2 = spec.Substring(dash + 1).Trim();
 179 |                 if (s1.Length > 0) long.TryParse(s1, NumberStyles.Integer, CultureInfo.InvariantCulture, out start);
 180 |                 if (s2.Length > 0) long.TryParse(s2, NumberStyles.Integer, CultureInfo.InvariantCulture, out end);
 181 |                 else end = fileLength - 1;
 182 |             }
 183 |             if (start < 0) start = 0;
 184 |             if (end >= fileLength) end = fileLength - 1;
 185 |             if (start > end || start >= fileLength)
 186 |             {
 187 |                 context.Response.StatusCode = 416;
 188 |                 context.Response.AddHeader("Content-Range", "bytes */" + fileLength);
 189 |                 return;
 190 |             }
 191 |         }
 192 | 
 193 |         long contentLength = end - start + 1;
 194 | 
 195 |         try
 196 |         {
 197 |             context.Response.ClearHeaders();
 198 |             context.Response.ClearContent();
 199 |             context.Response.BufferOutput = false;
 200 |             context.Response.ContentType = contentType;
 201 |             context.Response.AddHeader("Accept-Ranges", "bytes");
 202 |             context.Response.AddHeader("Content-Length", contentLength.ToString(CultureInfo.InvariantCulture));
 203 | 
 204 |             string disposition = forceDownload ? "attachment" : "inline";
 205 |             string safeName = fileName.Replace("\"", "'");
 206 |             context.Response.AddHeader("Content-Disposition", disposition + "; filename=\"" + safeName + "\"");
 207 | 
 208 |             if (isRange)
 209 |             {
 210 |                 context.Response.StatusCode = 206;
 211 |                 context.Response.AddHeader("Content-Range",
 212 |                     string.Format(CultureInfo.InvariantCulture, "bytes {0}-{1}/{2}", start, end, fileLength));
 213 |             }
 214 |             else
 215 |             {
 216 |                 context.Response.StatusCode = 200;
 217 |             }
 218 | 
 219 |             // Stream file (works better than TransmitFile under IIS Express + video)
 220 |             using (var fs = new FileStream(full, FileMode.Open, FileAccess.Read, FileShare.Read))
 221 |             {
 222 |                 if (start > 0) fs.Seek(start, SeekOrigin.Begin);
 223 |                 var buffer = new byte[81920];
 224 |                 long remaining = contentLength;
 225 |                 while (remaining > 0)
 226 |                 {
 227 |                     if (!context.Response.IsClientConnected) return;
 228 |                     int toRead = remaining > buffer.Length ? buffer.Length : (int)remaining;
 229 |                     int read = fs.Read(buffer, 0, toRead);
 230 |                     if (read <= 0) break;
 231 |                     context.Response.OutputStream.Write(buffer, 0, read);
 232 |                     remaining -= read;
 233 |                 }
 234 |             }
 235 |             try { context.Response.Flush(); } catch { /* client gone */ }
 236 |         }
 237 |         catch (Exception ex)
 238 |         {
 239 |             if (IsClientAbort(ex)) return;
 240 |             // Headers may already be sent — avoid second write that throws again
 241 |             try
 242 |             {
 243 |                 if (!context.Response.HeadersWritten)
 244 |                     SafeError(context, 500, ex.Message);
 245 |             }
 246 |             catch { }
 247 |         }
 248 |     }
 249 | 
 250 |     private static void SafeError(HttpContext context, int code, string message)
 251 |     {
 252 |         try
 253 |         {
 254 |             if (context == null || context.Response == null) return;
 255 |             if (context.Response.HeadersWritten) return;
 256 |             context.Response.ClearHeaders();
 257 |             context.Response.ClearContent();
 258 |             context.Response.StatusCode = code;
 259 |             context.Response.ContentType = "text/plain; charset=utf-8";
 260 |             context.Response.Write(message ?? "Error");
 261 |         }
 262 |         catch { /* ignore */ }
 263 |     }
 264 | 
 265 |     private static bool IsClientAbort(Exception ex)
 266 |     {
 267 |         if (ex == null) return false;
 268 |         string m = ex.Message ?? "";
 269 |         if (m.IndexOf("remote host closed", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 270 |         if (m.IndexOf("The client disconnected", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 271 |         if (m.IndexOf("operation was aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 272 |         if (m.IndexOf("thread was being aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
 273 |         if (ex is HttpException && ((HttpException)ex).ErrorCode == unchecked((int)0x800704CD)) return true;
 274 |         if (ex.InnerException != null) return IsClientAbort(ex.InnerException);
 275 |         return false;
 276 |     }
 277 | 
 278 |     /// <summary>
 279 |     /// Accepts many stored URL shapes → "CourseMaterials/file.pdf"
 280 |     /// </summary>
 281 |     public static string NormalizeToUploadsRelative(string path, HttpContext context)
 282 |     {
 283 |         if (string.IsNullOrWhiteSpace(path)) return null;
 284 |         path = path.Replace('\\', '/').Trim();
 285 | 
 286 |         if (path.StartsWith("http://", StringComparison.OrdinalIgnoreCase) ||
 287 |             path.StartsWith("https://", StringComparison.OrdinalIgnoreCase))
 288 |         {
 289 |             try
 290 |             {
 291 |                 var uri = new Uri(path);
 292 |                 path = uri.AbsolutePath;
 293 |                 // Also handle ?path= nested (shouldn't happen)
 294 |             }
 295 |             catch { return null; }
 296 |         }
 297 | 
 298 |         // If someone passed the full ServeUpload URL as path, extract its path query
 299 |         int q = path.IndexOf("ServeUpload.ashx", StringComparison.OrdinalIgnoreCase);
 300 |         if (q >= 0)
 301 |         {
 302 |             int pq = path.IndexOf("path=", StringComparison.OrdinalIgnoreCase);
 303 |             if (pq >= 0)
 304 |             {
 305 |                 string rest = path.Substring(pq + 5);
 306 |                 int amp = rest.IndexOf('&');
 307 |                 if (amp >= 0) rest = rest.Substring(0, amp);
 308 |                 try { path = HttpUtility.UrlDecode(rest); } catch { path = rest; }
 309 |             }
 310 |             else return null;
 311 |         }
 312 | 
 313 |         if (path.StartsWith("~/")) path = path.Substring(2);
 314 |         path = path.TrimStart('/');
 315 | 
 316 |         string app = (context != null && context.Request != null)
 317 |             ? (context.Request.ApplicationPath ?? "/").Trim('/')
 318 |             : "";
 319 |         if (!string.IsNullOrEmpty(app) && path.StartsWith(app + "/", StringComparison.OrdinalIgnoreCase))
 320 |             path = path.Substring(app.Length + 1);
 321 | 
 322 |         // Drop "Pages/Lecturer/" if a bad relative path was stored
 323 |         if (path.StartsWith("Pages/", StringComparison.OrdinalIgnoreCase))
 324 |         {
 325 |             int up = path.IndexOf("Uploads/", StringComparison.OrdinalIgnoreCase);
 326 |             if (up >= 0) path = path.Substring(up);
 327 |         }
 328 | 
 329 |         if (path.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
 330 |             path = path.Substring("Uploads/".Length);
 331 |         else if (path.StartsWith("Upload/", StringComparison.OrdinalIgnoreCase))
 332 |             path = path.Substring("Upload/".Length);
 333 | 
 334 |         path = path.TrimStart('/');
 335 |         return string.IsNullOrEmpty(path) ? null : path;
 336 |     }
 337 | 
 338 |     private static string MimeFromExt(string ext)
 339 |     {
 340 |         switch (ext)
 341 |         {
 342 |             case ".pdf": return "application/pdf";
 343 |             case ".mp4": return "video/mp4";
 344 |             case ".webm": return "video/webm";
 345 |             case ".mov": return "video/quicktime";
 346 |             case ".png": return "image/png";
 347 |             case ".jpg":
 348 |             case ".jpeg": return "image/jpeg";
 349 |             case ".gif": return "image/gif";
 350 |             case ".webp": return "image/webp";
 351 |             case ".bmp": return "image/bmp";
 352 |             case ".doc": return "application/msword";
 353 |             case ".docx": return "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
 354 |             case ".ppt": return "application/vnd.ms-powerpoint";
 355 |             case ".pptx": return "application/vnd.openxmlformats-officedocument.presentationml.presentation";
 356 |             default: return "application/octet-stream";
 357 |         }
 358 |     }
 359 | 
 360 |     public bool IsReusable { get { return false; } }
 361 | }
```

**Line notes**

- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L14:** Class declaration for this page/service.
- **L18:** IHttpHandler entry for ashx.
- **L21:** Error handling block.
- **L35:** Navigate browser to another URL.
- **L38:** Handle/log exception.
- **L43:** Handle/log exception.
- **L59:** Error handling block.
- **L109:** Error handling block.
- **L113:** Handle/log exception.
- **L128:** Error handling block.
- **L133:** Handle/log exception.
- **L158:** Error handling block.
- **L159:** Handle/log exception.
- **L195:** Error handling block.
- **L220:** Import namespace/types.
- **L235:** Error handling block.
- **L237:** Handle/log exception.
- **L241:** Error handling block.
- **L246:** Handle/log exception.
- **L252:** Error handling block.
- **L262:** Handle/log exception.
- **L289:** Error handling block.
- **L295:** Handle/log exception.
- **L308:** Error handling block.

## Source snapshot (raw)

```html
<%@ WebHandler Language="C#" Class="ServeUpload" %>

using System;
using System.Globalization;
using System.IO;
using System.Web;

/// <summary>
/// Serves files under ~/Uploads for inline preview (PDF/video/image) or download.
/// Supports HTTP Range requests so HTML5 video can seek without 500 errors.
/// Query: ?path=CourseMaterials/file.pdf  or  ?path=Uploads/CourseVideos/x.mp4
/// Optional: &amp;dl=1 forces download
/// </summary>
public class ServeUpload : IHttpHandler
{
    private static readonly string[] AllowedRoots = { "CourseMaterials", "CourseVideos", "CourseThumbnails" };

    public void ProcessRequest(HttpContext context)
    {
        // Always delegate to Media.ashx (auth + path policy live there). No direct stream.
        try
        {
            string path = context.Request.QueryString["path"]
                ?? context.Request["path"]
                ?? context.Request["f"]
                ?? "";
            if (string.IsNullOrWhiteSpace(path))
            {
                SafeError(context, 400, "Missing path. Use Media.ashx?f=CourseMaterials/file.pdf");
                return;
            }
            string media = VirtualPathUtility.ToAbsolute("~/Media.ashx");
            string qs = "f=" + HttpUtility.UrlEncode(path);
            if (context.Request["dl"] == "1") qs += "&dl=1";
            context.Response.Redirect(media + "?" + qs, false);
            context.ApplicationInstance.CompleteRequest();
        }
        catch (HttpException hex)
        {
            if (IsClientAbort(hex)) return;
            SafeError(context, 500, "Redirect error.");
        }
        catch (Exception)
        {
            SafeError(context, 500, "Redirect error.");
        }
    }

    private static void Serve(HttpContext context)
    {
        if (context == null || context.Request == null || context.Response == null) return;

        string path = context.Request.QueryString["path"]
                      ?? context.Request["path"]
                      ?? "";
        // Request may already decode once — only decode if still percent-encoded
        if (path.IndexOf('%') >= 0)
        {
            try { path = HttpUtility.UrlDecode(path); } catch { /* keep raw */ }
        }
        path = (path ?? "").Replace('\\', '/').Trim();

        if (string.IsNullOrEmpty(path))
        {
            SafeError(context, 400, "Missing path. Use ?path=CourseMaterials/file.pdf");
            return;
        }

        path = NormalizeToUploadsRelative(path, context);
        if (string.IsNullOrEmpty(path))
        {
            SafeError(context, 400, "Invalid path.");
            return;
        }

        var parts = path.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length < 2)
        {
            SafeError(context, 400, "Path must be Folder/filename (got: " + path + ")");
            return;
        }

        bool allowed = false;
        foreach (var root in AllowedRoots)
        {
            if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))
            {
                allowed = true;
                break;
            }
        }
        if (!allowed)
        {
            SafeError(context, 403, "Folder not allowed: " + parts[0]);
            return;
        }

        foreach (var p in parts)
        {
            if (p == ".." || p == "." || p.IndexOf(':') >= 0)
            {
                SafeError(context, 400, "Invalid path segment.");
                return;
            }
        }

        string relativeUnderUploads = string.Join("/", parts);
        string physical;
        try
        {
            physical = context.Server.MapPath("~/Uploads/" + relativeUnderUploads);
        }
        catch (Exception ex)
        {
            SafeError(context, 400, "MapPath failed: " + ex.Message);
            return;
        }

        if (string.IsNullOrEmpty(physical) || !File.Exists(physical))
        {
            // Help debug: show what we looked for
            SafeError(context, 404, "File not found: Uploads/" + relativeUnderUploads);
            return;
        }

        string uploadsRoot;
        string full;
        try
        {
            uploadsRoot = Path.GetFullPath(context.Server.MapPath("~/Uploads"));
            full = Path.GetFullPath(physical);
        }
        catch (Exception ex)
        {
            SafeError(context, 500, "Path resolve failed: " + ex.Message);
            return;
        }

        // Ensure trailing separator so UploadsX is not treated as under Uploads
        string rootWithSep = uploadsRoot.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar)
                             + Path.DirectorySeparatorChar;
        if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)
            && !string.Equals(full, uploadsRoot, StringComparison.OrdinalIgnoreCase))
        {
            SafeError(context, 403, "Access denied.");
            return;
        }

        string fileName = Path.GetFileName(full);
        string ext = Path.GetExtension(fileName).ToLowerInvariant();
        string contentType = MimeFromExt(ext);
        bool forceDownload = context.Request["dl"] == "1" || context.Request["download"] == "1";

        if (ext == ".doc" || ext == ".docx" || ext == ".ppt" || ext == ".pptx" || ext == ".pptm")
            forceDownload = true;

        long fileLength;
        try { fileLength = new FileInfo(full).Length; }
        catch (Exception ex)
        {
            SafeError(context, 500, "Cannot read file size: " + ex.Message);
            return;
        }

        // Parse Range: bytes=start-end (required for HTML5 video)
        long start = 0;
        long end = fileLength - 1;
        bool isRange = false;
        string rangeHeader = context.Request.Headers["Range"];
        if (!forceDownload && !string.IsNullOrEmpty(rangeHeader) && rangeHeader.StartsWith("bytes=", StringComparison.OrdinalIgnoreCase))
        {
            isRange = true;
            string spec = rangeHeader.Substring("bytes=".Length).Trim();
            int dash = spec.IndexOf('-');
            if (dash >= 0)
            {
                string s1 = spec.Substring(0, dash).Trim();
                string s2 = spec.Substring(dash + 1).Trim();
                if (s1.Length > 0) long.TryParse(s1, NumberStyles.Integer, CultureInfo.InvariantCulture, out start);
                if (s2.Length > 0) long.TryParse(s2, NumberStyles.Integer, CultureInfo.InvariantCulture, out end);
                else end = fileLength - 1;
            }
            if (start < 0) start = 0;
            if (end >= fileLength) end = fileLength - 1;
            if (start > end || start >= fileLength)
            {
                context.Response.StatusCode = 416;
                context.Response.AddHeader("Content-Range", "bytes */" + fileLength);
                return;
            }
        }

        long contentLength = end - start + 1;

        try
        {
            context.Response.ClearHeaders();
            context.Response.ClearContent();
            context.Response.BufferOutput = false;
            context.Response.ContentType = contentType;
            context.Response.AddHeader("Accept-Ranges", "bytes");
            context.Response.AddHeader("Content-Length", contentLength.ToString(CultureInfo.InvariantCulture));

            string disposition = forceDownload ? "attachment" : "inline";
            string safeName = fileName.Replace("\"", "'");
            context.Response.AddHeader("Content-Disposition", disposition + "; filename=\"" + safeName + "\"");

            if (isRange)
            {
                context.Response.StatusCode = 206;
                context.Response.AddHeader("Content-Range",
                    string.Format(CultureInfo.InvariantCulture, "bytes {0}-{1}/{2}", start, end, fileLength));
            }
            else
            {
                context.Response.StatusCode = 200;
            }

            // Stream file (works better than TransmitFile under IIS Express + video)
            using (var fs = new FileStream(full, FileMode.Open, FileAccess.Read, FileShare.Read))
            {
                if (start > 0) fs.Seek(start, SeekOrigin.Begin);
                var buffer = new byte[81920];
                long remaining = contentLength;
                while (remaining > 0)
                {
                    if (!context.Response.IsClientConnected) return;
                    int toRead = remaining > buffer.Length ? buffer.Length : (int)remaining;
                    int read = fs.Read(buffer, 0, toRead);
                    if (read <= 0) break;
                    context.Response.OutputStream.Write(buffer, 0, read);
                    remaining -= read;
                }
            }
            try { context.Response.Flush(); } catch { /* client gone */ }
        }
        catch (Exception ex)
        {
            if (IsClientAbort(ex)) return;
            // Headers may already be sent — avoid second write that throws again
            try
            {
                if (!context.Response.HeadersWritten)
                    SafeError(context, 500, ex.Message);
            }
            catch { }
        }
    }

    private static void SafeError(HttpContext context, int code, string message)
    {
        try
        {
            if (context == null || context.Response == null) return;
            if (context.Response.HeadersWritten) return;
            context.Response.ClearHeaders();
            context.Response.ClearContent();
            context.Response.StatusCode = code;
            context.Response.ContentType = "text/plain; charset=utf-8";
            context.Response.Write(message ?? "Error");
        }
        catch { /* ignore */ }
    }

    private static bool IsClientAbort(Exception ex)
    {
        if (ex == null) return false;
        string m = ex.Message ?? "";
        if (m.IndexOf("remote host closed", StringComparison.OrdinalIgnoreCase) >= 0) return true;
        if (m.IndexOf("The client disconnected", StringComparison.OrdinalIgnoreCase) >= 0) return true;
        if (m.IndexOf("operation was aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
        if (m.IndexOf("thread was being aborted", StringComparison.OrdinalIgnoreCase) >= 0) return true;
        if (ex is HttpException && ((HttpException)ex).ErrorCode == unchecked((int)0x800704CD)) return true;
        if (ex.InnerException != null) return IsClientAbort(ex.InnerException);
        return false;
    }

    /// <summary>
    /// Accepts many stored URL shapes → "CourseMaterials/file.pdf"
    /// </summary>
    public static string NormalizeToUploadsRelative(string path, HttpContext context)
    {
        if (string.IsNullOrWhiteSpace(path)) return null;
        path = path.Replace('\\', '/').Trim();

        if (path.StartsWith("http://", StringComparison.OrdinalIgnoreCase) ||
            path.StartsWith("https://", StringComparison.OrdinalIgnoreCase))
        {
            try
            {
                var uri = new Uri(path);
                path = uri.AbsolutePath;
                // Also handle ?path= nested (shouldn't happen)
            }
            catch { return null; }
        }

        // If someone passed the full ServeUpload URL as path, extract its path query
        int q = path.IndexOf("ServeUpload.ashx", StringComparison.OrdinalIgnoreCase);
        if (q >= 0)
        {
            int pq = path.IndexOf("path=", StringComparison.OrdinalIgnoreCase);
            if (pq >= 0)
            {
                string rest = path.Substring(pq + 5);
                int amp = rest.IndexOf('&');
                if (amp >= 0) rest = rest.Substring(0, amp);
                try { path = HttpUtility.UrlDecode(rest); } catch { path = rest; }
            }
            else return null;
        }

        if (path.StartsWith("~/")) path = path.Substring(2);
        path = path.TrimStart('/');

        string app = (context != null && context.Request != null)
            ? (context.Request.ApplicationPath ?? "/").Trim('/')
            : "";
        if (!string.IsNullOrEmpty(app) && path.StartsWith(app + "/", StringComparison.OrdinalIgnoreCase))
            path = path.Substring(app.Length + 1);

        // Drop "Pages/Lecturer/" if a bad relative path was stored
        if (path.StartsWith("Pages/", StringComparison.OrdinalIgnoreCase))
        {
            int up = path.IndexOf("Uploads/", StringComparison.OrdinalIgnoreCase);
            if (up >= 0) path = path.Substring(up);
        }

        if (path.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
            path = path.Substring("Uploads/".Length);
        else if (path.StartsWith("Upload/", StringComparison.OrdinalIgnoreCase))
            path = path.Substring("Upload/".Length);

        path = path.TrimStart('/');
        return string.IsNullOrEmpty(path) ? null : path;
    }

    private static string MimeFromExt(string ext)
    {
        switch (ext)
        {
            case ".pdf": return "application/pdf";
            case ".mp4": return "video/mp4";
            case ".webm": return "video/webm";
            case ".mov": return "video/quicktime";
            case ".png": return "image/png";
            case ".jpg":
            case ".jpeg": return "image/jpeg";
            case ".gif": return "image/gif";
            case ".webp": return "image/webp";
            case ".bmp": return "image/bmp";
            case ".doc": return "application/msword";
            case ".docx": return "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
            case ".ppt": return "application/vnd.ms-powerpoint";
            case ".pptx": return "application/vnd.openxmlformats-officedocument.presentationml.presentation";
            default: return "application/octet-stream";
        }
    }

    public bool IsReusable { get { return false; } }
}

```
