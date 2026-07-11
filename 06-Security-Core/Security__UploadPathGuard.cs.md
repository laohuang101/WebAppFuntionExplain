# UploadPathGuard.cs
**Source:** `Data/Security/UploadPathGuard.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Normalize/sanitize paths under ~/Uploads; block traversal and illegal folders.

## File overview

- **Total lines:** 103
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 13:** `AllowedRoots` (`string[]`) — **Often a collection related to Allowed Roots (plural name). (text)**
- **Line 24:** `f` (`string`) — **Holds “f” for this scope. (text)**
- **Line 40:** `parts` (`var`) — **Split path or name segments.**
- **Line 47:** `null` (`return`) — **Holds “null” for this scope. (type `return`)**
- **Line 51:** `allowed` (`bool`) — **Boolean — path/role is permitted.**
- **Line 72:** `rel` (`string`) — **Holds “rel” for this scope. (text)**
- **Line 74:** `uploadsRoot` (`string`) — **Holds “uploads Root” for this scope. (text)**
- **Line 80:** `full` (`string`) — **Fully resolved absolute path.**
- **Line 81:** `rootFull` (`string`) — **Holds “root Full” for this scope. (text)**
- **Line 84:** `rootWithSep` (`string`) — **Holds “root With Sep” for this scope. (text)**
- **Line 89:** `null` (`return`) — **Holds “null” for this scope. (type `return`)**
- **Line 91:** `full` (`return`) — **Fully resolved absolute path.**
- **Line 100:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**

## Functions / methods (3 found)

### `NormalizeRelative` — lines 21–64

```csharp
public static string NormalizeRelative(string raw)
```

#### Explanation

- **Purpose:** Implements `NormalizeRelative`.
- **Parameters (what each means):**
- `raw` (`string`) — Raw bytes or unprocessed input string.
- **Local variables (what each means):**
- `f` (`string`) — Holds “f” for this scope. (text)
- `parts` (`var`) — Split path or name segments.
- `allowed` (`bool`) — Boolean — path/role is permitted.
- `p` — Parameter, path, or password fragment depending on context.
- `root` — Root directory path (Uploads).

#### Line-by-line (this function)

```csharp
  21 |         public static string NormalizeRelative(string raw)
  22 |         {
  23 |             if (string.IsNullOrWhiteSpace(raw)) return null;
  24 |             string f = raw.Replace('\\', '/').Trim();
  25 |             if (f.IndexOf('%') >= 0)
  26 |             {
  27 |                 try { f = HttpUtility.UrlDecode(f); } catch { }
  28 |                 f = (f ?? "").Replace('\\', '/').Trim();
  29 |             }
  30 | 
  31 |             while (f.StartsWith("/")) f = f.Substring(1);
  32 |             if (f.StartsWith("~/")) f = f.Substring(2);
  33 |             if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
  34 |                 f = f.Substring("Uploads/".Length);
  35 |             if (f.StartsWith("Uploads\\", StringComparison.OrdinalIgnoreCase))
  36 |                 f = f.Substring("Uploads\\".Length);
  37 | 
  38 |             if (string.IsNullOrEmpty(f)) return null;
  39 |             if (f.IndexOf(':') >= 0) return null; // drive letter / scheme
  40 | 
  41 |             var parts = f.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
  42 |             if (parts.Length < 1) return null;
  43 | 
  44 |             foreach (var p in parts)
  45 |             {
  46 |                 if (p == "." || p == ".." || p.IndexOf('\0') >= 0)
  47 |                     return null;
  48 |             }
  49 | 
  50 |             // Must start with allowed root when multi-segment or single-folder style
  51 |             bool allowed = false;
  52 |             foreach (var root in AllowedRoots)
  53 |             {
  54 |                 if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))
  55 |                 {
  56 |                     allowed = true;
  57 |                     parts[0] = root; // canonical casing
  58 |                     break;
  59 |                 }
  60 |             }
  61 |             if (!allowed) return null;
  62 | 
  63 |             return string.Join("/", parts);
  64 |         }
```

<<<<<<< HEAD
**Line notes**

- **L21:** Path sandbox under Uploads.
- **L27:** Error handling block.
=======
**Line notes** (what code + variables mean)

- **L21:** Path sandbox under Uploads.
- **L24:** `f` means: Holds “f” for this scope. (text)
- **L27:** Error handling block.
- **L41:** `parts` means: Split path or name segments.
- **L51:** `allowed` means: Boolean — path/role is permitted.
>>>>>>> eb8ce01 (update)

---

### `ToPhysical` — lines 69–92

```csharp
public static string ToPhysical(HttpContext ctx, string relativeUnderUploads)
```

#### Explanation

- **Purpose:** Implements `ToPhysical`.
- **Parameters (what each means):**
- `ctx` (`HttpContext`) — Current HTTP request context (Request, Response, Session).
- `relativeUnderUploads` (`string`) — Often a collection related to relative Under Uploads (plural name). (text)
- **Local variables (what each means):**
- `rel` (`string`) — Holds “rel” for this scope. (text)
- `full` (`string`) — Fully resolved absolute path.
- `rootFull` (`string`) — Holds “root Full” for this scope. (text)
- `rootWithSep` (`string`) — Holds “root With Sep” for this scope. (text)

#### Line-by-line (this function)

```csharp
  69 |         public static string ToPhysical(HttpContext ctx, string relativeUnderUploads)
  70 |         {
  71 |             if (ctx == null || string.IsNullOrEmpty(relativeUnderUploads)) return null;
  72 |             string rel = NormalizeRelative(relativeUnderUploads);
  73 |             if (string.IsNullOrEmpty(rel)) return null;
  74 | 
  75 |             string uploadsRoot;
  76 |             try { uploadsRoot = ctx.Server.MapPath("~/Uploads"); }
  77 |             catch { return null; }
  78 | 
  79 |             if (string.IsNullOrEmpty(uploadsRoot)) return null;
  80 |             string full = Path.GetFullPath(Path.Combine(uploadsRoot, rel.Replace('/', Path.DirectorySeparatorChar)));
  81 |             string rootFull = Path.GetFullPath(uploadsRoot);
  82 | 
  83 |             // Ensure full is under root (trailing separator avoids prefix tricks)
  84 |             string rootWithSep = rootFull.TrimEnd(Path.DirectorySeparatorChar)
  85 |                                  + Path.DirectorySeparatorChar;
  86 |             if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)
  87 |                 && !string.Equals(full, rootFull, StringComparison.OrdinalIgnoreCase))
  88 |             {
  89 |                 return null;
  90 |             }
  91 |             return full;
  92 |         }
```

<<<<<<< HEAD
**Line notes**

- **L72:** Path sandbox under Uploads.
- **L76:** Error handling block.
- **L77:** Handle/log exception.
=======
**Line notes** (what code + variables mean)

- **L72:** Path sandbox under Uploads. | `rel` means: Holds “rel” for this scope. (text)
- **L76:** Error handling block.
- **L77:** Handle/log exception.
- **L80:** `full` means: Fully resolved absolute path.
- **L81:** `rootFull` means: Holds “root Full” for this scope. (text)
- **L84:** `rootWithSep` means: Holds “root With Sep” for this scope. (text)
>>>>>>> eb8ce01 (update)

---

### `IsAllowedExtension` — lines 93–101

```csharp
public static bool IsAllowedExtension(string ext, string[] allow)
```

#### Explanation

- **Purpose:** Implements `IsAllowedExtension`.
- **Parameters (what each means):**
- `ext` (`string`) — File extension (.pdf, .mp4, …).
- `allow` (`string[]`) — Holds “allow” for this scope. (text)
- **Local variables (what each means):**
- `a` — Holds “a” for this scope.

#### Line-by-line (this function)

```csharp
  93 | 
  94 |         public static bool IsAllowedExtension(string ext, string[] allow)
  95 |         {
  96 |             if (string.IsNullOrEmpty(ext) || allow == null) return false;
  97 |             ext = ext.ToLowerInvariant();
  98 |             foreach (var a in allow)
  99 |                 if (string.Equals(a, ext, StringComparison.OrdinalIgnoreCase)) return true;
 100 |             return false;
 101 |         }
```

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

```csharp
   1 | using System;
   2 | using System.IO;
   3 | using System.Web;
   4 | 
   5 | namespace WebAppAssignment.Data.Security
   6 | {
   7 |     /// <summary>
   8 |     /// Resolve upload paths only under ~/Uploads and known subfolders.
   9 |     /// Blocks path traversal and absolute paths.
  10 |     /// </summary>
  11 |     public static class UploadPathGuard
  12 |     {
  13 |         public static readonly string[] AllowedRoots =
  14 |         {
  15 |             "CourseMaterials", "CourseVideos", "CourseThumbnails", "CourseSubmissions"
  16 |         };
  17 | 
  18 |         /// <summary>
  19 |         /// Normalize client path to "Folder/file.ext" under Uploads, or null if invalid.
  20 |         /// </summary>
  21 |         public static string NormalizeRelative(string raw)
  22 |         {
  23 |             if (string.IsNullOrWhiteSpace(raw)) return null;
  24 |             string f = raw.Replace('\\', '/').Trim();
  25 |             if (f.IndexOf('%') >= 0)
  26 |             {
  27 |                 try { f = HttpUtility.UrlDecode(f); } catch { }
  28 |                 f = (f ?? "").Replace('\\', '/').Trim();
  29 |             }
  30 | 
  31 |             while (f.StartsWith("/")) f = f.Substring(1);
  32 |             if (f.StartsWith("~/")) f = f.Substring(2);
  33 |             if (f.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))
  34 |                 f = f.Substring("Uploads/".Length);
  35 |             if (f.StartsWith("Uploads\\", StringComparison.OrdinalIgnoreCase))
  36 |                 f = f.Substring("Uploads\\".Length);
  37 | 
  38 |             if (string.IsNullOrEmpty(f)) return null;
  39 |             if (f.IndexOf(':') >= 0) return null; // drive letter / scheme
  40 | 
  41 |             var parts = f.Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
  42 |             if (parts.Length < 1) return null;
  43 | 
  44 |             foreach (var p in parts)
  45 |             {
  46 |                 if (p == "." || p == ".." || p.IndexOf('\0') >= 0)
  47 |                     return null;
  48 |             }
  49 | 
  50 |             // Must start with allowed root when multi-segment or single-folder style
  51 |             bool allowed = false;
  52 |             foreach (var root in AllowedRoots)
  53 |             {
  54 |                 if (string.Equals(parts[0], root, StringComparison.OrdinalIgnoreCase))
  55 |                 {
  56 |                     allowed = true;
  57 |                     parts[0] = root; // canonical casing
  58 |                     break;
  59 |                 }
  60 |             }
  61 |             if (!allowed) return null;
  62 | 
  63 |             return string.Join("/", parts);
  64 |         }
  65 | 
  66 |         /// <summary>
  67 |         /// Map relative Folder/file to physical path under Uploads; null if outside sandbox.
  68 |         /// </summary>
  69 |         public static string ToPhysical(HttpContext ctx, string relativeUnderUploads)
  70 |         {
  71 |             if (ctx == null || string.IsNullOrEmpty(relativeUnderUploads)) return null;
  72 |             string rel = NormalizeRelative(relativeUnderUploads);
  73 |             if (string.IsNullOrEmpty(rel)) return null;
  74 | 
  75 |             string uploadsRoot;
  76 |             try { uploadsRoot = ctx.Server.MapPath("~/Uploads"); }
  77 |             catch { return null; }
  78 | 
  79 |             if (string.IsNullOrEmpty(uploadsRoot)) return null;
  80 |             string full = Path.GetFullPath(Path.Combine(uploadsRoot, rel.Replace('/', Path.DirectorySeparatorChar)));
  81 |             string rootFull = Path.GetFullPath(uploadsRoot);
  82 | 
  83 |             // Ensure full is under root (trailing separator avoids prefix tricks)
  84 |             string rootWithSep = rootFull.TrimEnd(Path.DirectorySeparatorChar)
  85 |                                  + Path.DirectorySeparatorChar;
  86 |             if (!full.StartsWith(rootWithSep, StringComparison.OrdinalIgnoreCase)
  87 |                 && !string.Equals(full, rootFull, StringComparison.OrdinalIgnoreCase))
  88 |             {
  89 |                 return null;
  90 |             }
  91 |             return full;
  92 |         }
  93 | 
  94 |         public static bool IsAllowedExtension(string ext, string[] allow)
  95 |         {
  96 |             if (string.IsNullOrEmpty(ext) || allow == null) return false;
  97 |             ext = ext.ToLowerInvariant();
  98 |             foreach (var a in allow)
  99 |                 if (string.Equals(a, ext, StringComparison.OrdinalIgnoreCase)) return true;
 100 |             return false;
 101 |         }
 102 |     }
 103 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L11:** Sandbox path under ~/Uploads.
- **L21:** Path sandbox under Uploads.
<<<<<<< HEAD
- **L27:** Error handling block.
- **L72:** Path sandbox under Uploads.
- **L76:** Error handling block.
- **L77:** Handle/log exception.
=======
- **L24:** `f` means: Holds “f” for this scope. (text)
- **L27:** Error handling block.
- **L41:** `parts` means: Split path or name segments.
- **L51:** `allowed` means: Boolean — path/role is permitted.
- **L72:** Path sandbox under Uploads. | `rel` means: Holds “rel” for this scope. (text)
- **L76:** Error handling block.
- **L77:** Handle/log exception.
- **L80:** `full` means: Fully resolved absolute path.
- **L81:** `rootFull` means: Holds “root Full” for this scope. (text)
- **L84:** `rootWithSep` means: Holds “root With Sep” for this scope. (text)
>>>>>>> eb8ce01 (update)

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
