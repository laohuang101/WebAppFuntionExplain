# FileMagic.cs
**Source:** `Data/Security/FileMagic.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Upload content-type validation by magic bytes (PDF, images, video, office docs).

## File overview

- **Total lines:** 143
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 18:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 29:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 31:** `ext` (`string`) — **File extension (.pdf, .mp4, …).**
- **Line 34:** `pos` (`long`) — **Holds “pos” for this scope. (integer)**
- **Line 37:** `header` (`byte[]`) — **Holds “header” for this scope. (type `byte[]`)**
- **Line 39:** `read` (`int`) — **Holds “read” for this scope. (integer)**
- **Line 47:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 57:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 65:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 70:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 76:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 81:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 87:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 92:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 99:** `false` (`return`) — **Holds “false” for this scope. (type `return`)**
- **Line 104:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 113:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 120:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 125:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 130:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**
- **Line 136:** `bytes` (`var`) — **Byte array (hash, random, file content).**
- **Line 140:** `true` (`return`) — **Holds “true” for this scope. (type `return`)**

## Functions / methods (3 found)

### `LooksValid` — lines 12–21

```csharp
public static bool LooksValid(HttpPostedFile file, string extension, out string message)
```

#### Explanation

- **Purpose:** Implements `LooksValid`.
- **Parameters (what each means):**
- `file` (`HttpPostedFile`) — Uploaded file object or file name.
- `extension` (`string`) — Holds “extension” for this scope. (text)
- `message` (`string`) — Status text for the UI.

#### Line-by-line (this function)

```csharp
  12 |         public static bool LooksValid(HttpPostedFile file, string extension, out string message)
  13 |         {
  14 |             message = null;
  15 |             if (file == null || file.ContentLength <= 0 || file.InputStream == null)
  16 |             {
  17 |                 message = "Empty upload.";
  18 |                 return false;
  19 |             }
  20 |             return LooksValid(file.InputStream, extension, out message);
  21 |         }
```

---

### `LooksValid` — lines 22–132

```csharp
public static bool LooksValid(Stream stream, string extension, out string message)
```

#### Explanation

- **Purpose:** Implements `LooksValid`.
- **Parameters (what each means):**
- `stream` (`Stream`) — String value: eam. (type `Stream`)
- `extension` (`string`) — Holds “extension” for this scope. (text)
- `message` (`string`) — Status text for the UI.
- **Local variables (what each means):**
- `ext` (`string`) — File extension (.pdf, .mp4, …).
- `pos` (`long`) — Holds “pos” for this scope. (integer)  Literal number `0`.
- `header` (`byte[]`) — Holds “header” for this scope. (type `byte[]`)  Newly constructed object.

#### Line-by-line (this function)

```csharp
  22 | 
  23 |         public static bool LooksValid(Stream stream, string extension, out string message)
  24 |         {
  25 |             message = null;
  26 |             if (stream == null || !stream.CanRead)
  27 |             {
  28 |                 message = "Cannot read upload stream.";
  29 |                 return false;
  30 |             }
  31 | 
  32 |             string ext = (extension ?? "").ToLowerInvariant();
  33 |             if (!ext.StartsWith(".")) ext = "." + ext;
  34 | 
  35 |             long pos = 0;
  36 |             try { pos = stream.Position; } catch { }
  37 | 
  38 |             byte[] header = new byte[16];
  39 |             int read;
  40 |             try
  41 |             {
  42 |                 read = stream.Read(header, 0, header.Length);
  43 |             }
  44 |             catch
  45 |             {
  46 |                 message = "Failed to read file header.";
  47 |                 return false;
  48 |             }
  49 |             finally
  50 |             {
  51 |                 try { stream.Position = pos; } catch { }
  52 |             }
  53 | 
  54 |             if (read < 4)
  55 |             {
  56 |                 message = "File is too small or empty.";
  57 |                 return false;
  58 |             }
  59 | 
  60 |             switch (ext)
  61 |             {
  62 |                 case ".pdf":
  63 |                     if (!StartsWith(header, read, "%PDF"))
  64 |                     { message = "Not a valid PDF (magic bytes)."; return false; }
  65 |                     return true;
  66 | 
  67 |                 case ".png":
  68 |                     if (!(read >= 8 && header[0] == 0x89 && header[1] == 0x50 && header[2] == 0x4E && header[3] == 0x47))
  69 |                     { message = "Not a valid PNG."; return false; }
  70 |                     return true;
  71 | 
  72 |                 case ".jpg":
  73 |                 case ".jpeg":
  74 |                     if (!(header[0] == 0xFF && header[1] == 0xD8 && header[2] == 0xFF))
  75 |                     { message = "Not a valid JPEG."; return false; }
  76 |                     return true;
  77 | 
  78 |                 case ".gif":
  79 |                     if (!StartsWith(header, read, "GIF8"))
  80 |                     { message = "Not a valid GIF."; return false; }
  81 |                     return true;
  82 | 
  83 |                 case ".webp":
  84 |                     if (!(read >= 12 && header[0] == 'R' && header[1] == 'I' && header[2] == 'F' && header[3] == 'F'
  85 |                           && header[8] == 'W' && header[9] == 'E' && header[10] == 'B' && header[11] == 'P'))
  86 |                     { message = "Not a valid WEBP."; return false; }
  87 |                     return true;
  88 | 
  89 |                 case ".bmp":
  90 |                     if (!(header[0] == 'B' && header[1] == 'M'))
  91 |                     { message = "Not a valid BMP."; return false; }
  92 |                     return true;
  93 | 
  94 |                 case ".mp4":
  95 |                 case ".mov":
  96 |                     // ISO BMFF — ftyp often at offset 4; be permissive for assignment demos
  97 |                     if (read >= 8) return true;
  98 |                     message = "Not a valid MP4/MOV container.";
  99 |                     return false;
 100 | 
 101 |                 case ".webm":
 102 |                     if (!(header[0] == 0x1A && header[1] == 0x45 && header[2] == 0xDF && header[3] == 0xA3))
 103 |                     { message = "Not a valid WebM."; return false; }
 104 |                     return true;
 105 | 
 106 |                 case ".zip":
 107 |                 case ".docx":
 108 |                 case ".pptx":
 109 |                 case ".xlsx":
 110 |                 case ".pptm":
 111 |                     if (!(header[0] == 'P' && header[1] == 'K'))
 112 |                     { message = "Not a valid Office/ZIP package."; return false; }
 113 |                     return true;
 114 | 
 115 |                 case ".doc":
 116 |                 case ".ppt":
 117 |                 case ".xls":
 118 |                     if (!(header[0] == 0xD0 && header[1] == 0xCF && header[2] == 0x11 && header[3] == 0xE0))
 119 |                     { message = "Not a valid legacy Office document."; return false; }
 120 |                     return true;
 121 | 
 122 |                 case ".txt":
 123 |                     if (header[0] == 'M' && header[1] == 'Z')
 124 |                     { message = "Executable content not allowed as text."; return false; }
 125 |                     return true;
 126 | 
 127 |                 default:
 128 |                     if (header[0] == 'M' && header[1] == 'Z')
 129 |                     { message = "Executable files are not allowed."; return false; }
 130 |                     return true;
 131 |             }
 132 |         }
```

**Line notes** (what code + variables mean)

- **L32:** `ext` means: File extension (.pdf, .mp4, …).
- **L35:** `pos` means: Holds “pos” for this scope. (integer)  Literal number `0`.
- **L36:** Error handling block.
- **L40:** Error handling block.
- **L44:** Handle/log exception.
- **L51:** Error handling block.
- **L64:** File magic-byte validation on upload.

---

### `StartsWith` — lines 133–141

```csharp
private static bool StartsWith(byte[] buf, int len, string ascii)
```

#### Explanation

- **Purpose:** Implements `StartsWith`.
- **Parameters (what each means):**
- `buf` (`byte[]`) — Holds “buf” for this scope. (type `byte[]`)
- `len` (`int`) — Length of string/array.
- `ascii` (`string`) — Holds “ascii” for this scope. (text)
- **Local variables (what each means):**
- `bytes` (`var`) — Byte array (hash, random, file content).
- `i` (`int`) — Loop index (0-based counter in for-loops).  Literal number `0`.

#### Line-by-line (this function)

```csharp
 133 | 
 134 |         private static bool StartsWith(byte[] buf, int len, string ascii)
 135 |         {
 136 |             var bytes = Encoding.ASCII.GetBytes(ascii);
 137 |             if (len < bytes.Length) return false;
 138 |             for (int i = 0; i < bytes.Length; i++)
 139 |                 if (buf[i] != bytes[i]) return false;
 140 |             return true;
 141 |         }
```

**Line notes** (what code + variables mean)

- **L136:** `bytes` means: Byte array (hash, random, file content).

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```csharp
   1 | using System.IO;
   2 | using System.Text;
   3 | using System.Web;
   4 | 
   5 | namespace WebAppAssignment.Data.Security
   6 | {
   7 |     /// <summary>
   8 |     /// Lightweight magic-byte checks so extension spoofing is harder.
   9 |     /// </summary>
  10 |     public static class FileMagic
  11 |     {
  12 |         public static bool LooksValid(HttpPostedFile file, string extension, out string message)
  13 |         {
  14 |             message = null;
  15 |             if (file == null || file.ContentLength <= 0 || file.InputStream == null)
  16 |             {
  17 |                 message = "Empty upload.";
  18 |                 return false;
  19 |             }
  20 |             return LooksValid(file.InputStream, extension, out message);
  21 |         }
  22 | 
  23 |         public static bool LooksValid(Stream stream, string extension, out string message)
  24 |         {
  25 |             message = null;
  26 |             if (stream == null || !stream.CanRead)
  27 |             {
  28 |                 message = "Cannot read upload stream.";
  29 |                 return false;
  30 |             }
  31 | 
  32 |             string ext = (extension ?? "").ToLowerInvariant();
  33 |             if (!ext.StartsWith(".")) ext = "." + ext;
  34 | 
  35 |             long pos = 0;
  36 |             try { pos = stream.Position; } catch { }
  37 | 
  38 |             byte[] header = new byte[16];
  39 |             int read;
  40 |             try
  41 |             {
  42 |                 read = stream.Read(header, 0, header.Length);
  43 |             }
  44 |             catch
  45 |             {
  46 |                 message = "Failed to read file header.";
  47 |                 return false;
  48 |             }
  49 |             finally
  50 |             {
  51 |                 try { stream.Position = pos; } catch { }
  52 |             }
  53 | 
  54 |             if (read < 4)
  55 |             {
  56 |                 message = "File is too small or empty.";
  57 |                 return false;
  58 |             }
  59 | 
  60 |             switch (ext)
  61 |             {
  62 |                 case ".pdf":
  63 |                     if (!StartsWith(header, read, "%PDF"))
  64 |                     { message = "Not a valid PDF (magic bytes)."; return false; }
  65 |                     return true;
  66 | 
  67 |                 case ".png":
  68 |                     if (!(read >= 8 && header[0] == 0x89 && header[1] == 0x50 && header[2] == 0x4E && header[3] == 0x47))
  69 |                     { message = "Not a valid PNG."; return false; }
  70 |                     return true;
  71 | 
  72 |                 case ".jpg":
  73 |                 case ".jpeg":
  74 |                     if (!(header[0] == 0xFF && header[1] == 0xD8 && header[2] == 0xFF))
  75 |                     { message = "Not a valid JPEG."; return false; }
  76 |                     return true;
  77 | 
  78 |                 case ".gif":
  79 |                     if (!StartsWith(header, read, "GIF8"))
  80 |                     { message = "Not a valid GIF."; return false; }
  81 |                     return true;
  82 | 
  83 |                 case ".webp":
  84 |                     if (!(read >= 12 && header[0] == 'R' && header[1] == 'I' && header[2] == 'F' && header[3] == 'F'
  85 |                           && header[8] == 'W' && header[9] == 'E' && header[10] == 'B' && header[11] == 'P'))
  86 |                     { message = "Not a valid WEBP."; return false; }
  87 |                     return true;
  88 | 
  89 |                 case ".bmp":
  90 |                     if (!(header[0] == 'B' && header[1] == 'M'))
  91 |                     { message = "Not a valid BMP."; return false; }
  92 |                     return true;
  93 | 
  94 |                 case ".mp4":
  95 |                 case ".mov":
  96 |                     // ISO BMFF — ftyp often at offset 4; be permissive for assignment demos
  97 |                     if (read >= 8) return true;
  98 |                     message = "Not a valid MP4/MOV container.";
  99 |                     return false;
 100 | 
 101 |                 case ".webm":
 102 |                     if (!(header[0] == 0x1A && header[1] == 0x45 && header[2] == 0xDF && header[3] == 0xA3))
 103 |                     { message = "Not a valid WebM."; return false; }
 104 |                     return true;
 105 | 
 106 |                 case ".zip":
 107 |                 case ".docx":
 108 |                 case ".pptx":
 109 |                 case ".xlsx":
 110 |                 case ".pptm":
 111 |                     if (!(header[0] == 'P' && header[1] == 'K'))
 112 |                     { message = "Not a valid Office/ZIP package."; return false; }
 113 |                     return true;
 114 | 
 115 |                 case ".doc":
 116 |                 case ".ppt":
 117 |                 case ".xls":
 118 |                     if (!(header[0] == 0xD0 && header[1] == 0xCF && header[2] == 0x11 && header[3] == 0xE0))
 119 |                     { message = "Not a valid legacy Office document."; return false; }
 120 |                     return true;
 121 | 
 122 |                 case ".txt":
 123 |                     if (header[0] == 'M' && header[1] == 'Z')
 124 |                     { message = "Executable content not allowed as text."; return false; }
 125 |                     return true;
 126 | 
 127 |                 default:
 128 |                     if (header[0] == 'M' && header[1] == 'Z')
 129 |                     { message = "Executable files are not allowed."; return false; }
 130 |                     return true;
 131 |             }
 132 |         }
 133 | 
 134 |         private static bool StartsWith(byte[] buf, int len, string ascii)
 135 |         {
 136 |             var bytes = Encoding.ASCII.GetBytes(ascii);
 137 |             if (len < bytes.Length) return false;
 138 |             for (int i = 0; i < bytes.Length; i++)
 139 |                 if (buf[i] != bytes[i]) return false;
 140 |             return true;
 141 |         }
 142 |     }
 143 | }
```

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L5:** C# namespace grouping.
- **L10:** Validate upload by file signature.
- **L32:** `ext` means: File extension (.pdf, .mp4, …).
- **L35:** `pos` means: Holds “pos” for this scope. (integer)  Literal number `0`.
- **L36:** Error handling block.
- **L40:** Error handling block.
- **L44:** Handle/log exception.
- **L51:** Error handling block.
- **L64:** File magic-byte validation on upload.
- **L136:** `bytes` means: Byte array (hash, random, file content).

## Source snapshot (raw)

```csharp
using System.IO;
using System.Text;
using System.Web;

namespace WebAppAssignment.Data.Security
{
    /// <summary>
    /// Lightweight magic-byte checks so extension spoofing is harder.
    /// </summary>
    public static class FileMagic
    {
        public static bool LooksValid(HttpPostedFile file, string extension, out string message)
        {
            message = null;
            if (file == null || file.ContentLength <= 0 || file.InputStream == null)
            {
                message = "Empty upload.";
                return false;
            }
            return LooksValid(file.InputStream, extension, out message);
        }

        public static bool LooksValid(Stream stream, string extension, out string message)
        {
            message = null;
            if (stream == null || !stream.CanRead)
            {
                message = "Cannot read upload stream.";
                return false;
            }

            string ext = (extension ?? "").ToLowerInvariant();
            if (!ext.StartsWith(".")) ext = "." + ext;

            long pos = 0;
            try { pos = stream.Position; } catch { }

            byte[] header = new byte[16];
            int read;
            try
            {
                read = stream.Read(header, 0, header.Length);
            }
            catch
            {
                message = "Failed to read file header.";
                return false;
            }
            finally
            {
                try { stream.Position = pos; } catch { }
            }

            if (read < 4)
            {
                message = "File is too small or empty.";
                return false;
            }

            switch (ext)
            {
                case ".pdf":
                    if (!StartsWith(header, read, "%PDF"))
                    { message = "Not a valid PDF (magic bytes)."; return false; }
                    return true;

                case ".png":
                    if (!(read >= 8 && header[0] == 0x89 && header[1] == 0x50 && header[2] == 0x4E && header[3] == 0x47))
                    { message = "Not a valid PNG."; return false; }
                    return true;

                case ".jpg":
                case ".jpeg":
                    if (!(header[0] == 0xFF && header[1] == 0xD8 && header[2] == 0xFF))
                    { message = "Not a valid JPEG."; return false; }
                    return true;

                case ".gif":
                    if (!StartsWith(header, read, "GIF8"))
                    { message = "Not a valid GIF."; return false; }
                    return true;

                case ".webp":
                    if (!(read >= 12 && header[0] == 'R' && header[1] == 'I' && header[2] == 'F' && header[3] == 'F'
                          && header[8] == 'W' && header[9] == 'E' && header[10] == 'B' && header[11] == 'P'))
                    { message = "Not a valid WEBP."; return false; }
                    return true;

                case ".bmp":
                    if (!(header[0] == 'B' && header[1] == 'M'))
                    { message = "Not a valid BMP."; return false; }
                    return true;

                case ".mp4":
                case ".mov":
                    // ISO BMFF — ftyp often at offset 4; be permissive for assignment demos
                    if (read >= 8) return true;
                    message = "Not a valid MP4/MOV container.";
                    return false;

                case ".webm":
                    if (!(header[0] == 0x1A && header[1] == 0x45 && header[2] == 0xDF && header[3] == 0xA3))
                    { message = "Not a valid WebM."; return false; }
                    return true;

                case ".zip":
                case ".docx":
                case ".pptx":
                case ".xlsx":
                case ".pptm":
                    if (!(header[0] == 'P' && header[1] == 'K'))
                    { message = "Not a valid Office/ZIP package."; return false; }
                    return true;

                case ".doc":
                case ".ppt":
                case ".xls":
                    if (!(header[0] == 0xD0 && header[1] == 0xCF && header[2] == 0x11 && header[3] == 0xE0))
                    { message = "Not a valid legacy Office document."; return false; }
                    return true;

                case ".txt":
                    if (header[0] == 'M' && header[1] == 'Z')
                    { message = "Executable content not allowed as text."; return false; }
                    return true;

                default:
                    if (header[0] == 'M' && header[1] == 'Z')
                    { message = "Executable files are not allowed."; return false; }
                    return true;
            }
        }

        private static bool StartsWith(byte[] buf, int len, string ascii)
        {
            var bytes = Encoding.ASCII.GetBytes(ascii);
            if (len < bytes.Length) return false;
            for (int i = 0; i < bytes.Length; i++)
                if (buf[i] != bytes[i]) return false;
            return true;
        }
    }
}

```
