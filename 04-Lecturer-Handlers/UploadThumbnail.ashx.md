# UploadThumbnail.ashx
**Source:** `Pages/Lecturer/UploadThumbnail.ashx`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 101
- **Kind:** `.ashx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (2 found)

### `ProcessRequest` — lines 14–92

```html
public void ProcessRequest(HttpContext context)
```

#### Explanation

- **Purpose:** Implements `ProcessRequest`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext context`
- **Local variables:** `file`, `ext`, `uploadsFolder`, `fileName`, `savePath`, `full`, `root`, `under`, `mediaUrl`, `staticUrl`

#### Line-by-line (this function)

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

**Line notes**

- **L15:** IHttpHandler entry for ashx.
- **L20:** Error handling block.
- **L23:** Authorization — block wrong role / anonymous.
- **L40:** Sandbox path under ~/Uploads.
- **L52:** File magic-byte validation on upload.
- **L53:** Validate upload by file signature.
- **L55:** Write/read security audit events.
- **L56:** File magic-byte validation on upload.
- **L88:** Handle/log exception.

---

### `WriteJson` — lines 93–98

```html
private void WriteJson(HttpContext context, object obj)
```

#### Explanation

- **Purpose:** Implements `WriteJson`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext context, object obj`
- **Local variables:** `js`

#### Line-by-line (this function)

```html
  93 | 
  94 |     private void WriteJson(HttpContext context, object obj)
  95 |     {
  96 |         var js = new JavaScriptSerializer();
  97 |         context.Response.Write(js.Serialize(obj));
  98 |     }
```

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

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

**Line notes**

- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L7:** Import namespace/types.
- **L8:** Import namespace/types.
- **L11:** Class declaration for this page/service.
- **L15:** IHttpHandler entry for ashx.
- **L20:** Error handling block.
- **L23:** Authorization — block wrong role / anonymous.
- **L40:** Sandbox path under ~/Uploads.
- **L52:** File magic-byte validation on upload.
- **L53:** Validate upload by file signature.
- **L55:** Write/read security audit events.
- **L56:** File magic-byte validation on upload.
- **L88:** Handle/log exception.

## Source snapshot (raw)

```html
<%@ WebHandler Language="C#" Class="UploadThumbnail" %>

using System;
using System.IO;
using System.Web;
using System.Web.Script.Serialization;
using System.Web.SessionState;
using WebAppAssignment.Data.Security;

/// <summary>Course thumbnail upload — Lecturer/Admin only.</summary>
public class UploadThumbnail : IHttpHandler, IRequiresSessionState
{
    private static readonly string[] ImageExts = { ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp" };

    public void ProcessRequest(HttpContext context)
    {
        context.Response.ContentType = "application/json; charset=utf-8";
        context.Response.Cache.SetCacheability(HttpCacheability.NoCache);

        try
        {
            int uid;
            if (!AuthGate.EnsureHandlerRole(context, out uid, "Lecturer", "Admin"))
                return;

            if (context.Request.Files.Count == 0)
            {
                WriteJson(context, new { success = false, message = "No file uploaded." });
                return;
            }

            var file = context.Request.Files[0];
            if (file == null || file.ContentLength <= 0)
            {
                WriteJson(context, new { success = false, message = "Empty file." });
                return;
            }

            var ext = Path.GetExtension(file.FileName).ToLowerInvariant();
            if (!UploadPathGuard.IsAllowedExtension(ext, ImageExts))
            {
                WriteJson(context, new { success = false, message = "Only image files are allowed." });
                return;
            }

            if (file.ContentLength > 5 * 1024 * 1024)
            {
                WriteJson(context, new { success = false, message = "Thumbnail must be under 5 MB." });
                return;
            }

            string magicMsg;
            if (!FileMagic.LooksValid(file, ext, out magicMsg))
            {
                SecurityAudit.Log("upload.reject", uid, magicMsg + " thumb");
                WriteJson(context, new { success = false, message = magicMsg ?? "Invalid image content." });
                return;
            }

            var uploadsFolder = context.Server.MapPath("~/Uploads/CourseThumbnails");
            if (!Directory.Exists(uploadsFolder)) Directory.CreateDirectory(uploadsFolder);

            var fileName = Guid.NewGuid().ToString("N") + ext;
            var savePath = Path.Combine(uploadsFolder, fileName);
            // Ensure still under thumbnails folder
            string full = Path.GetFullPath(savePath);
            string root = Path.GetFullPath(uploadsFolder) + Path.DirectorySeparatorChar;
            if (!full.StartsWith(root, StringComparison.OrdinalIgnoreCase))
            {
                WriteJson(context, new { success = false, message = "Invalid save path." });
                return;
            }

            file.SaveAs(savePath);

            string under = "CourseThumbnails/" + fileName;
            string mediaUrl = VirtualPathUtility.ToAbsolute("~/Media.ashx") + "?f=" + HttpUtility.UrlEncode(under);
            string staticUrl = VirtualPathUtility.ToAbsolute("~/Uploads/" + under);

            WriteJson(context, new
            {
                success = true,
                url = mediaUrl,
                staticUrl = staticUrl,
                storePath = "Uploads/" + under
            });
        }
        catch
        {
            WriteJson(context, new { success = false, message = "Thumbnail upload failed." });
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
