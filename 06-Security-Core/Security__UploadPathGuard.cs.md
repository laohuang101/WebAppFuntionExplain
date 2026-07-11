# UploadPathGuard.cs
**Source:** `Data/Security/UploadPathGuard.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Normalize/sanitize paths under ~/Uploads; block traversal and illegal folders.

## File overview

- **Total lines:** 103
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 13:** `AllowedRoots` — type `string[]`
- **Line 24:** `f` — type `string`
- **Line 40:** `parts` — type `var`
- **Line 47:** `null` — type `return`
- **Line 51:** `allowed` — type `bool`
- **Line 72:** `rel` — type `string`
- **Line 74:** `uploadsRoot` — type `string`
- **Line 80:** `full` — type `string`
- **Line 81:** `rootFull` — type `string`
- **Line 84:** `rootWithSep` — type `string`
- **Line 89:** `null` — type `return`
- **Line 91:** `full` — type `return`
- **Line 100:** `false` — type `return`

## Functions / methods (3 found)

### `NormalizeRelative` — lines 21–64

```
public static string NormalizeRelative(string raw)
```

#### Explanation

- **Purpose:** Implements `NormalizeRelative`.
- **Parameters:** `string raw`
- **Local variables:** `f`, `parts`, `allowed`

#### Line-by-line (this function)

`  21`  `        public static string NormalizeRelative(string raw)`
  - → Path sandbox under Uploads.
`  22`  `        {`
`  23`  `            if (string.IsNullOrWhiteSpace(raw)) return null;`
`  24`  `            string f = raw.Replace('\\', '/').Trim();`
`  25`  `            if (f.IndexOf('%') >= 0)`
`  26`  `            {`
`  27`  `                try { f = HttpUtility.UrlDecode(f); } catch { }`
  - → Error handling block.
`  28`  `                f = (f ?? "").Replace('\\', '/').Trim();`
`  29`  `            }`
`  30`  ``
`  31`  `            while (f.StartsWith("/")) f = f.Substring(1);`
`  32`  `            if (f.StartsWith("~/")) f = f.Substring(2);`
`  33`  `            if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))`
`  34`  `                f = f.Substring("Uploads/".Length);`
`  35`  `            if (f.StartsWith("Uploads\\", StringComparison.OrdinalIgnoreCase))`
`  36`  `                f = f.Substring("Uploads\\".Length);`
`  37`  ``
`  38`  `            if (string.IsNullOrEmpty(f)) return null;`
`  39`  `            if (f.IndexOf(':') >= 0) return null; // drive letter / scheme`
`  40`  ``
`  41`  `            var parts = f.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);`
`  42`  `            if (parts.Length < 1) return null;`
`  43`  ``
`  44`  `            foreach (var p in parts)`
`  45`  `            {`
`  46`  `                if (p == "." || p == ".." || p.IndexOf('\0') >= 0)`
`  47`  `                    return null;`
`  48`  `            }`
`  49`  ``
`  50`  `            // Must start with allowed root when multi-segment or single-folder style`
`  51`  `            bool allowed = false;`
`  52`  `            foreach (var root in AllowedRoots)`
`  53`  `            {`
`  54`  `                if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))`
`  55`  `                {`
`  56`  `                    allowed = true;`
`  57`  `                    parts[0] = root; // canonical casing`
`  58`  `                    break;`
`  59`  `                }`
`  60`  `            }`
`  61`  `            if (!allowed) return null;`
`  62`  ``
`  63`  `            return string.Join("/", parts);`
`  64`  `        }`

---

### `ToPhysical` — lines 69–92

```
public static string ToPhysical(HttpContext ctx, string relativeUnderUploads)
```

#### Explanation

- **Purpose:** Implements `ToPhysical`.
- **Parameters:** `HttpContext ctx, string relativeUnderUploads`
- **Local variables:** `rel`, `full`, `rootFull`, `rootWithSep`

#### Line-by-line (this function)

`  69`  `        public static string ToPhysical(HttpContext ctx, string relativeUnderUploads)`
`  70`  `        {`
`  71`  `            if (ctx == null || string.IsNullOrEmpty(relativeUnderUploads)) return null;`
`  72`  `            string rel = NormalizeRelative(relativeUnderUploads);`
  - → Path sandbox under Uploads.
`  73`  `            if (string.IsNullOrEmpty(rel)) return null;`
`  74`  ``
`  75`  `            string uploadsRoot;`
`  76`  `            try { uploadsRoot = ctx.Server.MapPath("~/Uploads"); }`
  - → Error handling block.
`  77`  `            catch { return null; }`
  - → Handle/log exception.
`  78`  ``
`  79`  `            if (string.IsNullOrEmpty(uploadsRoot)) return null;`
`  80`  `            string full = Path.GetFullPath(Path.Combine(uploadsRoot, rel.Replace('/', Path.DirectorySeparatorChar)));`
`  81`  `            string rootFull = Path.GetFullPath(uploadsRoot);`
`  82`  ``
`  83`  `            // Ensure full is under root (trailing separator avoids prefix tricks)`
`  84`  `            string rootWithSep = rootFull.TrimEnd(Path.DirectorySeparatorChar)`
`  85`  `                                 + Path.DirectorySeparatorChar;`
`  86`  `            if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)`
`  87`  `                && !string.Equals(full, rootFull, StringComparison.OrdinalIgnoreCase))`
`  88`  `            {`
`  89`  `                return null;`
`  90`  `            }`
`  91`  `            return full;`
`  92`  `        }`

---

### `IsAllowedExtension` — lines 93–101

```
public static bool IsAllowedExtension(string ext, string[] allow)
```

#### Explanation

- **Purpose:** Implements `IsAllowedExtension`.
- **Parameters:** `string ext, string[] allow`

#### Line-by-line (this function)

`  93`  ``
`  94`  `        public static bool IsAllowedExtension(string ext, string[] allow)`
`  95`  `        {`
`  96`  `            if (string.IsNullOrEmpty(ext) || allow == null) return false;`
`  97`  `            ext = ext.ToLowerInvariant();`
`  98`  `            foreach (var a in allow)`
`  99`  `                if (string.Equals(a, ext, StringComparison.OrdinalIgnoreCase)) return true;`
` 100`  `            return false;`
` 101`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.IO;`
  - → Import namespace/types.
`   3`  `using System.Web;`
  - → Import namespace/types.
`   4`  ``
`   5`  `namespace WebAppAssignment.Data.Security`
  - → C# namespace grouping.
`   6`  `{`
`   7`  `    /// <summary>`
`   8`  `    /// Resolve upload paths only under ~/Uploads and known subfolders.`
`   9`  `    /// Blocks path traversal and absolute paths.`
`  10`  `    /// </summary>`
`  11`  `    public static class UploadPathGuard`
  - → Sandbox path under ~/Uploads.
`  12`  `    {`
`  13`  `        public static readonly string[] AllowedRoots =`
`  14`  `        {`
`  15`  `            "CourseMaterials", "CourseVideos", "CourseThumbnails", "CourseSubmissions"`
`  16`  `        };`
`  17`  ``
`  18`  `        /// <summary>`
`  19`  `        /// Normalize client path to "Folder/file.ext" under Uploads, or null if invalid.`
`  20`  `        /// </summary>`
`  21`  `        public static string NormalizeRelative(string raw)`
  - → Path sandbox under Uploads.
`  22`  `        {`
`  23`  `            if (string.IsNullOrWhiteSpace(raw)) return null;`
`  24`  `            string f = raw.Replace('\\', '/').Trim();`
`  25`  `            if (f.IndexOf('%') >= 0)`
`  26`  `            {`
`  27`  `                try { f = HttpUtility.UrlDecode(f); } catch { }`
  - → Error handling block.
`  28`  `                f = (f ?? "").Replace('\\', '/').Trim();`
`  29`  `            }`
`  30`  ``
`  31`  `            while (f.StartsWith("/")) f = f.Substring(1);`
`  32`  `            if (f.StartsWith("~/")) f = f.Substring(2);`
`  33`  `            if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))`
`  34`  `                f = f.Substring("Uploads/".Length);`
`  35`  `            if (f.StartsWith("Uploads\\", StringComparison.OrdinalIgnoreCase))`
`  36`  `                f = f.Substring("Uploads\\".Length);`
`  37`  ``
`  38`  `            if (string.IsNullOrEmpty(f)) return null;`
`  39`  `            if (f.IndexOf(':') >= 0) return null; // drive letter / scheme`
`  40`  ``
`  41`  `            var parts = f.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);`
`  42`  `            if (parts.Length < 1) return null;`
`  43`  ``
`  44`  `            foreach (var p in parts)`
`  45`  `            {`
`  46`  `                if (p == "." || p == ".." || p.IndexOf('\0') >= 0)`
`  47`  `                    return null;`
`  48`  `            }`
`  49`  ``
`  50`  `            // Must start with allowed root when multi-segment or single-folder style`
`  51`  `            bool allowed = false;`
`  52`  `            foreach (var root in AllowedRoots)`
`  53`  `            {`
`  54`  `                if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))`
`  55`  `                {`
`  56`  `                    allowed = true;`
`  57`  `                    parts[0] = root; // canonical casing`
`  58`  `                    break;`
`  59`  `                }`
`  60`  `            }`
`  61`  `            if (!allowed) return null;`
`  62`  ``
`  63`  `            return string.Join("/", parts);`
`  64`  `        }`
`  65`  ``
`  66`  `        /// <summary>`
`  67`  `        /// Map relative Folder/file to physical path under Uploads; null if outside sandbox.`
`  68`  `        /// </summary>`
`  69`  `        public static string ToPhysical(HttpContext ctx, string relativeUnderUploads)`
`  70`  `        {`
`  71`  `            if (ctx == null || string.IsNullOrEmpty(relativeUnderUploads)) return null;`
`  72`  `            string rel = NormalizeRelative(relativeUnderUploads);`
  - → Path sandbox under Uploads.
`  73`  `            if (string.IsNullOrEmpty(rel)) return null;`
`  74`  ``
`  75`  `            string uploadsRoot;`
`  76`  `            try { uploadsRoot = ctx.Server.MapPath("~/Uploads"); }`
  - → Error handling block.
`  77`  `            catch { return null; }`
  - → Handle/log exception.
`  78`  ``
`  79`  `            if (string.IsNullOrEmpty(uploadsRoot)) return null;`
`  80`  `            string full = Path.GetFullPath(Path.Combine(uploadsRoot, rel.Replace('/', Path.DirectorySeparatorChar)));`
`  81`  `            string rootFull = Path.GetFullPath(uploadsRoot);`
`  82`  ``
`  83`  `            // Ensure full is under root (trailing separator avoids prefix tricks)`
`  84`  `            string rootWithSep = rootFull.TrimEnd(Path.DirectorySeparatorChar)`
`  85`  `                                 + Path.DirectorySeparatorChar;`
`  86`  `            if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)`
`  87`  `                && !string.Equals(full, rootFull, StringComparison.OrdinalIgnoreCase))`
`  88`  `            {`
`  89`  `                return null;`
`  90`  `            }`
`  91`  `            return full;`
`  92`  `        }`
`  93`  ``
`  94`  `        public static bool IsAllowedExtension(string ext, string[] allow)`
`  95`  `        {`
`  96`  `            if (string.IsNullOrEmpty(ext) || allow == null) return false;`
`  97`  `            ext = ext.ToLowerInvariant();`
`  98`  `            foreach (var a in allow)`
`  99`  `                if (string.Equals(a, ext, StringComparison.OrdinalIgnoreCase)) return true;`
` 100`  `            return false;`
` 101`  `        }`
` 102`  `    }`
` 103`  `}`

## Source snapshot (raw)

```csharp
using System;
using System.IO;
using System.Web;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// Resolve upload paths only under ~/Uploads and known subfolders.
    /// Blocks path traversal and absolute paths.
    /// </summary>
    public static class UploadPathGuard
    {
        public static readonly string[] AllowedRoots =
        {
            "CourseMaterials", "CourseVideos", "CourseThumbnails", "CourseSubmissions"
        };

        /// <summary>
        /// Normalize client path to "Folder/file.ext" under Uploads, or null if invalid.
        /// </summary>
        public static string NormalizeRelative(string raw)
        {
            if (string.IsNullOrWhiteSpace(raw)) return null;
            string f = raw.Replace('\\', '/').Trim();
            if (f.IndexOf('%') >= 0)
            {
                try { f = HttpUtility.UrlDecode(f); } catch { }
                f = (f ?? "").Replace('\\', '/').Trim();
            }

            while (f.StartsWith("/")) f = f.Substring(1);
            if (f.StartsWith("~/")) f = f.Substring(2);
            if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
                f = f.Substring("Uploads/".Length);
            if (f.StartsWith("Uploads\\", StringComparison.OrdinalIgnoreCase))
                f = f.Substring("Uploads\\".Length);

            if (string.IsNullOrEmpty(f)) return null;
            if (f.IndexOf(':') >= 0) return null; // drive letter / scheme

            var parts = f.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
            if (parts.Length < 1) return null;

            foreach (var p in parts)
            {
                if (p == "." || p == ".." || p.IndexOf('\0') >= 0)
                    return null;
            }

            // Must start with allowed root when multi-segment or single-folder style
            bool allowed = false;
            foreach (var root in AllowedRoots)
            {
                if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))
                {
                    allowed = true;
                    parts[0] = root; // canonical casing
                    break;
                }
            }
            if (!allowed) return null;

            return string.Join("/", parts);
        }

        /// <summary>
        /// Map relative Folder/file to physical path under Uploads; null if outside sandbox.
        /// </summary>
        public static string ToPhysical(HttpContext ctx, string relativeUnderUploads)
        {
            if (ctx == null || string.IsNullOrEmpty(relativeUnderUploads)) return null;
            string rel = NormalizeRelative(relativeUnderUploads);
            if (string.IsNullOrEmpty(rel)) return null;

            string uploadsRoot;
            try { uploadsRoot = ctx.Server.MapPath("~/Uploads"); }
            catch { return null; }

            if (string.IsNullOrEmpty(uploadsRoot)) return null;
            string full = Path.GetFullPath(Path.Combine(uploadsRoot, rel.Replace('/', Path.DirectorySeparatorChar)));
            string rootFull = Path.GetFullPath(uploadsRoot);

            // Ensure full is under root (trailing separator avoids prefix tricks)
            string rootWithSep = rootFull.TrimEnd(Path.DirectorySeparatorChar)
                                 + Path.DirectorySeparatorChar;
            if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)
                && !string.Equals(full, rootFull, StringComparison.OrdinalIgnoreCase))
            {
                return null;
            }
            return full;
        }

        public static bool IsAllowedExtension(string ext, string[] allow)
        {
            if (string.IsNullOrEmpty(ext) || allow == null) return false;
            ext = ext.ToLowerInvariant();
            foreach (var a in allow)
                if (string.Equals(a, ext, StringComparison.OrdinalIgnoreCase)) return true;
            return false;
        }
    }
}

```
