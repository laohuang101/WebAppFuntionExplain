# UploadThumbnail.ashx
**Source:** `Pages/Lecturer/UploadThumbnail.ashx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 101
- **Kind:** `.ashx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (2 found)

### `ProcessRequest` — lines 14–92

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
| `file` | `var` | Uploaded file object or file name. |
| `ext` | `var` | File extension (.pdf, .mp4, …). |
| `uploadsFolder` | `var` | Filesystem or URL path. |
| `fileName` | `var` | Original file name for display/download. |
| `savePath` | `var` | Filesystem or URL path. |
| `full` | `string` | Fully resolved absolute path. |
| `root` | `string` | Root directory path (Uploads). |
| `under` | `string` | Holds “under” for this scope. (text)  Literal text string. |
| `mediaUrl` | `string` | URL string. (text) |
| `staticUrl` | `string` | URL string. (text) |

#### Code

```html
  14 | 
  15 |     public void ProcessRequest(HttpContext context)
  16 |     {
  17 |         context.Response.ContentType = "application/json; charset=utf-8";
  18 |         context.Response.Cache.SetCacheability(HttpCacheability.NoCache);
  19 | 
  20 |         try
  21 |         {
  22 |             int uid;
  23 |             if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin"))
  24 |                 return;
  25 | 
  26 |             if (context.Request.Files.Count == 0)
  27 |             {
  28 |                 WriteJson(context, new { success = false, message = "No file uploaded." });
  29 |                 return;
  30 |             }
  31 | 
  32 |             var file = context.Request.Files[0];
  33 |             if (file == null || file.ContentLength <= 0)
  34 |             {
  35 |                 WriteJson(context, new { success = false, message = "Empty file." });
  36 |                 return;
  37 |             }
  38 | 
  39 |             var ext = Path.GetExtension(file.FileName).ToLowerInvariant();
  40 |             if (!UploadPathGuard.IsAllowedExtension(ext, ImageExts))
  41 |             {
  42 |                 WriteJson(context, new { success = false, message = "Only image files are allowed." });
  43 |                 return;
  44 |             }
  45 | 
  46 |             if (file.ContentLength > 5 * 1024 * 1024)
  47 |             {
  48 |                 WriteJson(context, new { success = false, message = "Thumbnail must be under 5 MB." });
  49 |                 return;
  50 |             }
  51 | 
  52 |             string magicMsg;
  53 |             if (!FileMagic.LooksValid(file, ext, out magicMsg))
  54 |             {
  55 |                 SecurityAudit.Log("upload.reject", uid, magicMsg + " thumb");
  56 |                 WriteJson(context, new { success = false, message = magicMsg ?? "Invalid image content." });
  57 |                 return;
  58 |             }
  59 | 
  60 |             var uploadsFolder = context.Server.MapPath("~/Uploads/CourseThumbnails");
  61 |             if (!Directory.Exists(uploadsFolder)) Directory.CreateDirectory(uploadsFolder);
  62 | 
  63 |             var fileName = Guid.NewGuid().ToString("N") + ext;
  64 |             var savePath = Path.Combine(uploadsFolder, fileName);
  65 |             // Ensure still under thumbnails folder
  66 |             string full = Path.GetFullPath(savePath);
  67 |             string root = Path.GetFullPath(uploadsFolder) + Path.DirectorySeparatorChar;
  68 |             if (!full.StartsWith(root, StringComparison.OrdinalIgnoreCase))
  69 |             {
  70 |                 WriteJson(context, new { success = false, message = "Invalid save path." });
  71 |                 return;
  72 |             }
  73 | 
  74 |             file.SaveAs(savePath);
  75 | 
  76 |             string under = "CourseThumbnails/" + fileName;
  77 |             string mediaUrl = VirtualPathUtility.ToAbsolute("~/Media.ashx") + "?f=" + HttpUtility.UrlEncode(under);
  78 |             string staticUrl = VirtualPathUtility.ToAbsolute("~/Uploads/" + under);
  79 | 
  80 |             WriteJson(context, new
  81 |             {
  82 |                 success = true,
  83 |                 url = mediaUrl,
  84 |                 staticUrl = staticUrl,
  85 |                 storePath = "Uploads/" + under
  86 |             });
  87 |         }
  88 |         catch
  89 |         {
  90 |             WriteJson(context, new { success = false, message = "Thumbnail upload failed." });
  91 |         }
  92 |     }
```

---

### `WriteJson` — lines 93–98

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
  93 | 
  94 |     private void WriteJson(HttpContext context, object obj)
  95 |     {
  96 |         var js = new JavaScriptSerializer();
  97 |         context.Response.Write(js.Serialize(obj));
  98 |     }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ WebHandler Language="C#" Class="UploadThumbnail" %>
   2 | 
   3 | using System;
   4 | using System.IO;
   5 | using System.Web;
   6 | using System.Web.Script.Serialization;
   7 | using System.Web.SessionState;
   8 | using WebAppAssignment.Data.Security;
   9 | 
  10 | /// <summary>Course thumbnail upload — Lecturer/Admin only.</summary>
  11 | public class UploadThumbnail : IHttpHandler, IRequiresSessionState
  12 | {
  13 |     private static readonly string[] ImageExts = { ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp" };
  14 | 
  15 |     public void ProcessRequest(HttpContext context)
  16 |     {
  17 |         context.Response.ContentType = "application/json; charset=utf-8";
  18 |         context.Response.Cache.SetCacheability(HttpCacheability.NoCache);
  19 | 
  20 |         try
  21 |         {
  22 |             int uid;
  23 |             if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin"))
  24 |                 return;
  25 | 
  26 |             if (context.Request.Files.Count == 0)
  27 |             {
  28 |                 WriteJson(context, new { success = false, message = "No file uploaded." });
  29 |                 return;
  30 |             }
  31 | 
  32 |             var file = context.Request.Files[0];
  33 |             if (file == null || file.ContentLength <= 0)
  34 |             {
  35 |                 WriteJson(context, new { success = false, message = "Empty file." });
  36 |                 return;
  37 |             }
  38 | 
  39 |             var ext = Path.GetExtension(file.FileName).ToLowerInvariant();
  40 |             if (!UploadPathGuard.IsAllowedExtension(ext, ImageExts))
  41 |             {
  42 |                 WriteJson(context, new { success = false, message = "Only image files are allowed." });
  43 |                 return;
  44 |             }
  45 | 
  46 |             if (file.ContentLength > 5 * 1024 * 1024)
  47 |             {
  48 |                 WriteJson(context, new { success = false, message = "Thumbnail must be under 5 MB." });
  49 |                 return;
  50 |             }
  51 | 
  52 |             string magicMsg;
  53 |             if (!FileMagic.LooksValid(file, ext, out magicMsg))
  54 |             {
  55 |                 SecurityAudit.Log("upload.reject", uid, magicMsg + " thumb");
  56 |                 WriteJson(context, new { success = false, message = magicMsg ?? "Invalid image content." });
  57 |                 return;
  58 |             }
  59 | 
  60 |             var uploadsFolder = context.Server.MapPath("~/Uploads/CourseThumbnails");
  61 |             if (!Directory.Exists(uploadsFolder)) Directory.CreateDirectory(uploadsFolder);
  62 | 
  63 |             var fileName = Guid.NewGuid().ToString("N") + ext;
  64 |             var savePath = Path.Combine(uploadsFolder, fileName);
  65 |             // Ensure still under thumbnails folder
  66 |             string full = Path.GetFullPath(savePath);
  67 |             string root = Path.GetFullPath(uploadsFolder) + Path.DirectorySeparatorChar;
  68 |             if (!full.StartsWith(root, StringComparison.OrdinalIgnoreCase))
  69 |             {
  70 |                 WriteJson(context, new { success = false, message = "Invalid save path." });
  71 |                 return;
  72 |             }
  73 | 
  74 |             file.SaveAs(savePath);
  75 | 
  76 |             string under = "CourseThumbnails/" + fileName;
  77 |             string mediaUrl = VirtualPathUtility.ToAbsolute("~/Media.ashx") + "?f=" + HttpUtility.UrlEncode(under);
  78 |             string staticUrl = VirtualPathUtility.ToAbsolute("~/Uploads/" + under);
  79 | 
  80 |             WriteJson(context, new
  81 |             {
  82 |                 success = true,
  83 |                 url = mediaUrl,
  84 |                 staticUrl = staticUrl,
  85 |                 storePath = "Uploads/" + under
  86 |             });
  87 |         }
  88 |         catch
  89 |         {
  90 |             WriteJson(context, new { success = false, message = "Thumbnail upload failed." });
  91 |         }
  92 |     }
  93 | 
  94 |     private void WriteJson(HttpContext context, object obj)
  95 |     {
  96 |         var js = new JavaScriptSerializer();
  97 |         context.Response.Write(js.Serialize(obj));
  98 |     }
  99 | 
 100 |     public bool IsReusable { get { return false; } }
 101 | }
```
