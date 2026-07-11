# SchemaMap.cs
**Source:** `Data/SchemaMap.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Discovers real table/column names in the attached MDF (SubChapters vs Lessons, etc.) so curriculum SQL adapts.

## File overview

- **Total lines:** 238
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 15:** `Gate` (`object`) — **Holds “Gate” for this scope.**
- **Line 16:** `_loaded` (`bool`) — **Holds “loaded” for this scope. (true/false)**
- **Line 17:** `_loadError` (`string`) — **Holds “load Error” for this scope. (text)**
- **Line 20:** `SubTable` (`string`) — **Holds “Sub Table” for this scope. (text)**
- **Line 21:** `SubPk` (`string`) — **Holds “Sub Pk” for this scope. (text)**
- **Line 22:** `SubChapterFk` (`string`) — **Holds “Sub Chapter Fk” for this scope. (text)**
- **Line 23:** `SubTitle` (`string`) — **Holds “Sub Title” for this scope. (text)**
- **Line 24:** `SubIndex` (`string`) — **Holds “Sub Index” for this scope. (text)**
- **Line 27:** `MatTable` (`string`) — **Holds “Mat Table” for this scope. (text)**
- **Line 28:** `MatPk` (`string`) — **Holds “Mat Pk” for this scope. (text)**
- **Line 29:** `MatSubFk` (`string`) — **Holds “Mat Sub Fk” for this scope. (text)**
- **Line 30:** `MatLinksToSub` (`bool`) — **Holds “Mat Links To Sub” for this scope. (true/false)**
- **Line 31:** `MatType` (`string`) — **Holds “Mat Type” for this scope. (text)**
- **Line 32:** `MatText` (`string`) — **Holds “Mat Text” for this scope. (text)**
- **Line 33:** `MatMedia` (`string`) — **Holds “Mat Media” for this scope. (text)**
- **Line 34:** `MatIndex` (`string`) — **Holds “Mat Index” for this scope. (text)**
- **Line 37:** `ChTable` (`string`) — **Holds “Ch Table” for this scope. (text)**
- **Line 38:** `ChPk` (`string`) — **Holds “Ch Pk” for this scope. (text)**
- **Line 39:** `ChCourseFk` (`string`) — **Holds “Ch Course Fk” for this scope. (text)**
- **Line 40:** `ChTitle` (`string`) — **Holds “Ch Title” for this scope. (text)**
- **Line 41:** `ChIndex` (`string`) — **Holds “Ch Index” for this scope. (text)**
- **Line 74:** `chCols` (`var`) — **Often a collection related to ch Cols (plural name).**
- **Line 79:** `chPk` (`var`) — **Holds “ch Pk” for this scope.**
- **Line 87:** `subTable` (`string`) — **Holds “sub Table” for this scope. (text)**
- **Line 96:** `sc` (`var`) — **Holds “sc” for this scope.**
- **Line 97:** `pk` (`var`) — **Holds “pk” for this scope.**
- **Line 107:** `matTable` (`string`) — **Holds “mat Table” for this scope. (text)**
- **Line 115:** `mc` (`var`) — **Holds “mc” for this scope.**
- **Line 116:** `mPk` (`var`) — **Holds “m Pk” for this scope.**
- **Line 163:** `list` (`var`) — **In-memory collection being built for JSON return.**
- **Line 173:** `list` (`return`) — **In-memory collection being built for JSON return.**
- **Line 192:** `o` (`var`) — **Holds “o” for this scope.**
- **Line 193:** `o` (`return`) — **Holds “o” for this scope. (type `return`)**
- **Line 201:** `hit` (`var`) — **Holds “hit” for this scope.**
- **Line 213:** `hit` (`var`) — **Holds “hit” for this scope.**
- **Line 216:** `null` (`return`) — **Holds “null” for this scope. (type `return`)**

## Functions / methods (11 found)

### `Ensure` — lines 44–62

```csharp
public static void Ensure()
```

#### Explanation

- **Purpose:** Implements `Ensure`.

#### Line-by-line (this function)

```csharp
  44 | 
  45 |         public static void Ensure()
  46 |         {
  47 |             if (_loaded) return;
  48 |             lock (Gate)
  49 |             {
  50 |                 if (_loaded) return;
  51 |                 try
  52 |                 {
  53 |                     Discover();
  54 |                     _loadError = null;
  55 |                 }
  56 |                 catch (Exception ex)
  57 |                 {
  58 |                     _loadError = ex.Message;
  59 |                 }
  60 |                 _loaded = true;
  61 |             }
  62 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L51:** Error handling block.
- **L56:** Handle/log exception.

---

### `Reset` — lines 63–67

```csharp
public static void Reset()
```

#### Explanation

- **Purpose:** Implements `Reset`.

#### Line-by-line (this function)

```csharp
  63 | 
  64 |         public static void Reset()
  65 |         {
  66 |             lock (Gate) { _loaded = false; _loadError = null; }
  67 |         }
```

---

### `Discover` — lines 68–149

```csharp
private static void Discover()
```

#### Explanation

- **Purpose:** Implements `Discover`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.
- `chPk` (`var`) — Holds “ch Pk” for this scope.
- `subTable` (`string`) — Holds “sub Table” for this scope. (text)
- `sc` (`var`) — Holds “sc” for this scope.
- `pk` (`var`) — Holds “pk” for this scope.
- `matTable` (`string`) — Holds “mat Table” for this scope. (text)
- `mc` (`var`) — Holds “mc” for this scope.
- `mPk` (`var`) — Holds “m Pk” for this scope.
- `t` — Temporary string/token/time value.

#### Line-by-line (this function)

```csharp
  68 | 
  69 |         private static void Discover()
  70 |         {
  71 |             using (var conn = DbHelper.OpenConnection())
  72 |             {
  73 |                 // Chapters
  74 |                 var chCols = Cols(conn, "Chapters");
  75 |                 if (chCols.Count == 0) chCols = Cols(conn, "Chapter");
  76 |                 if (chCols.Count > 0)
  77 |                 {
  78 |                     ChTable = TableExists(conn, "Chapters") ? "Chapters" : "Chapter";
  79 |                     var chPk = PrimaryKey(conn, ChTable);
  80 |                     ChPk = !string.IsNullOrEmpty(chPk) ? chPk : Pick(chCols, "ChID", "ChapterID", "ID", "Id");
  81 |                     ChCourseFk = Pick(chCols, "CID", "CourseID", "CourseId");
  82 |                     ChTitle = Pick(chCols, "Title", "Name");
  83 |                     ChIndex = PickOptional(chCols, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
  84 |                 }
  85 | 
  86 |                 // SubChapters / SubChapter / Lessons
  87 |                 string subTable = null;
  88 |                 foreach (var t in new[] { "SubChapters", "SubChapter", "Lessons", "Lesson" })
  89 |                 {
  90 |                     if (TableExists(conn, t)) { subTable = t; break; }
  91 |                 }
  92 | 
  93 |                 if (subTable != null)
  94 |                 {
  95 |                     SubTable = subTable;
  96 |                     var sc = Cols(conn, subTable);
  97 |                     var pk = PrimaryKey(conn, subTable);
  98 |                     SubPk = !string.IsNullOrEmpty(pk)
  99 |                     ? pk
 100 |                     : Pick(sc, "SchID", "SChID", "SubChapterID", "SubChapterId", "LessonID", "LessonId", "ID", "Id");
 101 |                     SubChapterFk = Pick(sc, "ChID", "ChapterID", "ChapterId");
 102 |                     SubTitle = Pick(sc, "Title", "Name", "LessonTitle");
 103 |                     SubIndex = PickOptional(sc, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
 104 |                 }
 105 | 
 106 |                 // StudyMats
 107 |                 string matTable = null;
 108 |                 foreach (var t in new[] { "StudyMats", "StudyMat", "StudyMaterials", "Materials" })
 109 |                 {
 110 |                     if (TableExists(conn, t)) { matTable = t; break; }
 111 |                 }
 112 |                 if (matTable != null)
 113 |                 {
 114 |                     MatTable = matTable;
 115 |                     var mc = Cols(conn, matTable);
 116 |                     var mPk = PrimaryKey(conn, matTable);
 117 |                     MatPk = !string.IsNullOrEmpty(mPk) ? mPk : Pick(mc, "SMID", "MID", "MaterialID", "ID", "Id");
 118 |                     MatType = PickOptional(mc, "Type", "MaterialType", "ContentType");
 119 |                     MatText = PickOptional(mc, "TextContent", "Content", "Text", "Body");
 120 |                     MatMedia = PickOptional(mc, "MediaLink", "MediaUrl", "Link", "Url", "FilePath");
 121 |                     MatIndex = PickOptional(mc, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
 122 | 
 123 |                     // Prefer SubChapter FK if present, else Chapter FK (legacy)
 124 |                     if (Has(mc, "SchID") || Has(mc, "SChID") || Has(mc, "SubChapterID") || Has(mc, "LessonID"))
 125 |                     {
 126 |                         MatSubFk = Pick(mc, "SchID", "SChID", "SubChapterID", "SubChapterId", "LessonID", "LessonId");
 127 |                         MatLinksToSub = true;
 128 |                     }
 129 |                     else if (Has(mc, "ChID") || Has(mc, "ChapterID"))
 130 |                     {
 131 |                         MatSubFk = Pick(mc, "ChID", "ChapterID", "ChapterId");
 132 |                         MatLinksToSub = false;
 133 |                     }
 134 |                     else if (!string.IsNullOrEmpty(SubTable) && !string.IsNullOrEmpty(SubPk) && Has(mc, SubPk))
 135 |                     {
 136 |                         MatSubFk = SubPk;
 137 |                         MatLinksToSub = true;
 138 |                     }
 139 | 
 140 |                     // Need at least one content column
 141 |                     if (string.IsNullOrEmpty(MatType) && string.IsNullOrEmpty(MatText) && string.IsNullOrEmpty(MatMedia))
 142 |                     {
 143 |                         MatText = mc.FirstOrDefault(c =>
 144 |                         !string.Equals(c, MatPk, StringComparison.OrdinalIgnoreCase) &&
 145 |                         !string.Equals(c, MatSubFk, StringComparison.OrdinalIgnoreCase));
 146 |                     }
 147 |                 }
 148 |             }
 149 |         }
```

<<<<<<< HEAD
**Line notes**

- **L71:** Import namespace/types.
=======
**Line notes** (what code + variables mean)

- **L71:** Import namespace/types.
- **L74:** `chCols` means: Often a collection related to ch Cols (plural name).
- **L79:** `chPk` means: Holds “ch Pk” for this scope.
- **L87:** `subTable` means: Holds “sub Table” for this scope. (text)
- **L96:** `sc` means: Holds “sc” for this scope.
- **L97:** `pk` means: Holds “pk” for this scope.
- **L107:** `matTable` means: Holds “mat Table” for this scope. (text)
- **L115:** `mc` means: Holds “mc” for this scope.
- **L116:** `mPk` means: Holds “m Pk” for this scope.
>>>>>>> eb8ce01 (update)

---

### `TableExists` — lines 150–159

```csharp
private static bool TableExists(SqlConnection conn, string name)
```

#### Explanation

- **Purpose:** Implements `TableExists`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `name` (`string`) — Display name of user/course/criterion.
- **Local variables (what each means):**
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.

#### Line-by-line (this function)

```csharp
 150 | 
 151 |         private static bool TableExists(SqlConnection conn, string name)
 152 |         {
 153 |             using (var cmd = new SqlCommand(
 154 |             "SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = @t", conn))
 155 |             {
 156 |                 cmd.Parameters.AddWithValue("@t", name);
 157 |                 return cmd.ExecuteScalar() != null;
 158 |             }
 159 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L151:** Database access (pure SQL).
- **L153:** Import namespace/types.
- **L156:** Parameterized SQL — prevents classic SQL injection.
- **L157:** Run SQL; return table / rows / scalar.

---

### `Cols` — lines 160–174

```csharp
private static List<string> Cols(SqlConnection conn, string table)
```

#### Explanation

- **Purpose:** Implements `Cols`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `table` (`string`) — DataTable or HTML table container.
- **Local variables (what each means):**
- `list` (`var`) — In-memory collection being built for JSON return.  Newly constructed object.
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- `r` (`var`) — Usually one database row (DataRow) in query loops.

#### Line-by-line (this function)

```csharp
 160 | 
 161 |         private static List<string> Cols(SqlConnection conn, string table)
 162 |         {
 163 |             var list = new List<string>();
 164 |             using (var cmd = new SqlCommand(
 165 |             "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = @t", conn))
 166 |             {
 167 |                 cmd.Parameters.AddWithValue("@t", table);
 168 |                 using (var r = cmd.ExecuteReader())
 169 |                 {
 170 |                     while (r.Read()) list.Add(r.GetString(0));
 171 |                 }
 172 |             }
 173 |             return list;
 174 |         }
```

<<<<<<< HEAD
**Line notes**

- **L161:** Database access (pure SQL).
=======
**Line notes** (what code + variables mean)

- **L161:** Database access (pure SQL).
- **L163:** `list` means: In-memory collection being built for JSON return.  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L164:** Import namespace/types.
- **L167:** Parameterized SQL — prevents classic SQL injection.
- **L168:** Import namespace/types.

---

### `Has` — lines 175–179

```csharp
private static bool Has(List<string> cols, string name)
```

#### Explanation

- **Purpose:** Implements `Has`.
- **Parameters (what each means):**
- `cols` (`List<string>`) — Often a collection related to cols (plural name). (text)
- `name` (`string`) — Display name of user/course/criterion.

#### Line-by-line (this function)

```csharp
 175 | 
 176 |         private static bool Has(List<string> cols, string name)
 177 |         {
 178 |             return cols.Any(c => string.Equals(c, name, StringComparison.OrdinalIgnoreCase));
 179 |         }
```

---

### `PrimaryKey` — lines 180–195

```csharp
private static string PrimaryKey(SqlConnection conn, string table)
```

#### Explanation

- **Purpose:** Implements `PrimaryKey`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `table` (`string`) — DataTable or HTML table container.
- **Local variables (what each means):**
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- `o` (`var`) — Holds “o” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY).

#### Line-by-line (this function)

```csharp
 180 | 
 181 |         private static string PrimaryKey(SqlConnection conn, string table)
 182 |         {
 183 |             using (var cmd = new SqlCommand(@"
 184 |             SELECT TOP 1 ku.COLUMN_NAME
 185 |             FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
 186 |             INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE ku
 187 |             ON tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME AND tc.TABLE_NAME = ku.TABLE_NAME
 188 |             WHERE tc.TABLE_NAME = @t AND tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
 189 |             ORDER BY ku.ORDINAL_POSITION", conn))
 190 |             {
 191 |                 cmd.Parameters.AddWithValue("@t", table);
 192 |                 var o = cmd.ExecuteScalar();
 193 |                 return o == null || o == DBNull.Value ? null : o.ToString();
 194 |             }
 195 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L181:** Database access (pure SQL).
- **L183:** Import namespace/types.
- **L186:** Join related tables (courses ↔ chapters ↔ works ↔ users).
- **L191:** Parameterized SQL — prevents classic SQL injection.
<<<<<<< HEAD
- **L192:** Run SQL; return table / rows / scalar.
=======
- **L192:** Run SQL; return table / rows / scalar. | `o` means: Holds “o” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY).
>>>>>>> eb8ce01 (update)
- **L193:** Null-safe read from database values.

---

### `Pick` — lines 196–207

```csharp
private static string Pick(List<string> cols, params string[] candidates)
```

#### Explanation

- **Purpose:** Implements `Pick`.
- **Parameters (what each means):**
- `cols` (`List<string>`) — Often a collection related to cols (plural name). (text)
- `candidates` (`string[]`) — Boolean flag: candidates. (text)
- **Local variables (what each means):**
- `hit` (`var`) — Holds “hit” for this scope.
- `c` — Temporary value (character, course, or counter depending on loop).

#### Line-by-line (this function)

```csharp
 196 | 
 197 |         private static string Pick(List<string> cols, params string[] candidates)
 198 |         {
 199 |             foreach (var c in candidates)
 200 |             {
 201 |                 var hit = cols.FirstOrDefault(x => string.Equals(x, c, StringComparison.OrdinalIgnoreCase));
 202 |                 if (hit != null) return hit;
 203 |             }
 204 |             // last resort: first column (often PK)
 205 |             if (cols.Count > 0) return cols[0];
 206 |             throw new InvalidOperationException("No columns found; candidates: " + string.Join(",", candidates));
 207 |         }
```
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L201:** `hit` means: Holds “hit” for this scope.
>>>>>>> eb8ce01 (update)

---

### `PickOptional` — lines 208–217

```csharp
private static string PickOptional(List<string> cols, params string[] candidates)
```

#### Explanation

- **Purpose:** Implements `PickOptional`.
- **Parameters (what each means):**
- `cols` (`List<string>`) — Often a collection related to cols (plural name). (text)
- `candidates` (`string[]`) — Boolean flag: candidates. (text)
- **Local variables (what each means):**
- `hit` (`var`) — Holds “hit” for this scope.
- `c` — Temporary value (character, course, or counter depending on loop).

#### Line-by-line (this function)

```csharp
 208 | 
 209 |         private static string PickOptional(List<string> cols, params string[] candidates)
 210 |         {
 211 |             foreach (var c in candidates)
 212 |             {
 213 |                 var hit = cols.FirstOrDefault(x => string.Equals(x, c, StringComparison.OrdinalIgnoreCase));
 214 |                 if (hit != null) return hit;
 215 |             }
 216 |             return null;
 217 |         }
```
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L213:** `hit` means: Holds “hit” for this scope.
>>>>>>> eb8ce01 (update)

---

### `Q` — lines 218–224

```csharp
public static string Q(string ident)
```

#### Explanation

- **Purpose:** Implements `Q`.
- **Parameters (what each means):**
- `ident` (`string`) — Holds “ident” for this scope. (text)

#### Line-by-line (this function)

```csharp
 218 | 
 219 |         public static string Q(string ident)
 220 |         {
 221 |             if (string.IsNullOrEmpty(ident)) return ident;
 222 |             // bracket-quote for reserved words like Index
 223 |             return "[" + ident.Replace("]", "]]") + "]";
 224 |         }
```

---

### `DebugInfo` — lines 225–236

```csharp
public static object DebugInfo()
```

#### Explanation

- **Purpose:** Implements `DebugInfo`.

#### Line-by-line (this function)

```csharp
 225 | 
 226 |         public static object DebugInfo()
 227 |         {
 228 |             Ensure();
 229 |             return new
 230 |             {
 231 |                 loadError = _loadError,
 232 |                 chapters = new { ChTable, ChPk, ChCourseFk, ChTitle, ChIndex },
 233 |                 sub = new { SubTable, SubPk, SubChapterFk, SubTitle, SubIndex },
 234 |                 mats = new { MatTable, MatPk, MatSubFk, MatLinksToSub, MatType, MatText, MatMedia, MatIndex }
 235 |             };
 236 |         }
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
   2 | using System.Collections.Generic;
   3 | using System.Data;
   4 | using System.Data.SqlClient;
   5 | using System.Linq;
   6 | 
   7 | namespace WebAppAssignment.Data
   8 | {
   9 |     /// <summary>
  10 |     /// Discovers real column names from EduDB via INFORMATION_SCHEMA
  11 |     /// so curriculum SQL works even when PK names differ (SchID vs ID etc.).
  12 |     /// </summary>
  13 |     public static class SchemaMap
  14 |     {
  15 |         private static readonly object Gate = new object();
  16 |         private static bool _loaded;
  17 |         private static string _loadError;
  18 | 
  19 |         // SubChapters
  20 |         public static string SubTable = null;
  21 |         public static string SubPk = null;
  22 |         public static string SubChapterFk = null;
  23 |         public static string SubTitle = null;
  24 |         public static string SubIndex = null; // optional
  25 | 
  26 |         // StudyMats
  27 |         public static string MatTable = null;
  28 |         public static string MatPk = null;
  29 |         public static string MatSubFk = null; // SchID or ChID
  30 |         public static bool MatLinksToSub = false;
  31 |         public static string MatType = null;
  32 |         public static string MatText = null;
  33 |         public static string MatMedia = null;
  34 |         public static string MatIndex = null;
  35 | 
  36 |         // Chapters
  37 |         public static string ChTable = "Chapters";
  38 |         public static string ChPk = "ChID";
  39 |         public static string ChCourseFk = "CID";
  40 |         public static string ChTitle = "Title";
  41 |         public static string ChIndex = null;
  42 | 
  43 |         public static string LoadError { get { Ensure(); return _loadError; } }
  44 | 
  45 |         public static void Ensure()
  46 |         {
  47 |             if (_loaded) return;
  48 |             lock (Gate)
  49 |             {
  50 |                 if (_loaded) return;
  51 |                 try
  52 |                 {
  53 |                     Discover();
  54 |                     _loadError = null;
  55 |                 }
  56 |                 catch (Exception ex)
  57 |                 {
  58 |                     _loadError = ex.Message;
  59 |                 }
  60 |                 _loaded = true;
  61 |             }
  62 |         }
  63 | 
  64 |         public static void Reset()
  65 |         {
  66 |             lock (Gate) { _loaded = false; _loadError = null; }
  67 |         }
  68 | 
  69 |         private static void Discover()
  70 |         {
  71 |             using (var conn = DbHelper.OpenConnection())
  72 |             {
  73 |                 // Chapters
  74 |                 var chCols = Cols(conn, "Chapters");
  75 |                 if (chCols.Count == 0) chCols = Cols(conn, "Chapter");
  76 |                 if (chCols.Count > 0)
  77 |                 {
  78 |                     ChTable = TableExists(conn, "Chapters") ? "Chapters" : "Chapter";
  79 |                     var chPk = PrimaryKey(conn, ChTable);
  80 |                     ChPk = !string.IsNullOrEmpty(chPk) ? chPk : Pick(chCols, "ChID", "ChapterID", "ID", "Id");
  81 |                     ChCourseFk = Pick(chCols, "CID", "CourseID", "CourseId");
  82 |                     ChTitle = Pick(chCols, "Title", "Name");
  83 |                     ChIndex = PickOptional(chCols, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
  84 |                 }
  85 | 
  86 |                 // SubChapters / SubChapter / Lessons
  87 |                 string subTable = null;
  88 |                 foreach (var t in new[] { "SubChapters", "SubChapter", "Lessons", "Lesson" })
  89 |                 {
  90 |                     if (TableExists(conn, t)) { subTable = t; break; }
  91 |                 }
  92 | 
  93 |                 if (subTable != null)
  94 |                 {
  95 |                     SubTable = subTable;
  96 |                     var sc = Cols(conn, subTable);
  97 |                     var pk = PrimaryKey(conn, subTable);
  98 |                     SubPk = !string.IsNullOrEmpty(pk)
  99 |                     ? pk
 100 |                     : Pick(sc, "SchID", "SChID", "SubChapterID", "SubChapterId", "LessonID", "LessonId", "ID", "Id");
 101 |                     SubChapterFk = Pick(sc, "ChID", "ChapterID", "ChapterId");
 102 |                     SubTitle = Pick(sc, "Title", "Name", "LessonTitle");
 103 |                     SubIndex = PickOptional(sc, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
 104 |                 }
 105 | 
 106 |                 // StudyMats
 107 |                 string matTable = null;
 108 |                 foreach (var t in new[] { "StudyMats", "StudyMat", "StudyMaterials", "Materials" })
 109 |                 {
 110 |                     if (TableExists(conn, t)) { matTable = t; break; }
 111 |                 }
 112 |                 if (matTable != null)
 113 |                 {
 114 |                     MatTable = matTable;
 115 |                     var mc = Cols(conn, matTable);
 116 |                     var mPk = PrimaryKey(conn, matTable);
 117 |                     MatPk = !string.IsNullOrEmpty(mPk) ? mPk : Pick(mc, "SMID", "MID", "MaterialID", "ID", "Id");
 118 |                     MatType = PickOptional(mc, "Type", "MaterialType", "ContentType");
 119 |                     MatText = PickOptional(mc, "TextContent", "Content", "Text", "Body");
 120 |                     MatMedia = PickOptional(mc, "MediaLink", "MediaUrl", "Link", "Url", "FilePath");
 121 |                     MatIndex = PickOptional(mc, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
 122 | 
 123 |                     // Prefer SubChapter FK if present, else Chapter FK (legacy)
 124 |                     if (Has(mc, "SchID") || Has(mc, "SChID") || Has(mc, "SubChapterID") || Has(mc, "LessonID"))
 125 |                     {
 126 |                         MatSubFk = Pick(mc, "SchID", "SChID", "SubChapterID", "SubChapterId", "LessonID", "LessonId");
 127 |                         MatLinksToSub = true;
 128 |                     }
 129 |                     else if (Has(mc, "ChID") || Has(mc, "ChapterID"))
 130 |                     {
 131 |                         MatSubFk = Pick(mc, "ChID", "ChapterID", "ChapterId");
 132 |                         MatLinksToSub = false;
 133 |                     }
 134 |                     else if (!string.IsNullOrEmpty(SubTable) && !string.IsNullOrEmpty(SubPk) && Has(mc, SubPk))
 135 |                     {
 136 |                         MatSubFk = SubPk;
 137 |                         MatLinksToSub = true;
 138 |                     }
 139 | 
 140 |                     // Need at least one content column
 141 |                     if (string.IsNullOrEmpty(MatType) && string.IsNullOrEmpty(MatText) && string.IsNullOrEmpty(MatMedia))
 142 |                     {
 143 |                         MatText = mc.FirstOrDefault(c =>
 144 |                         !string.Equals(c, MatPk, StringComparison.OrdinalIgnoreCase) &&
 145 |                         !string.Equals(c, MatSubFk, StringComparison.OrdinalIgnoreCase));
 146 |                     }
 147 |                 }
 148 |             }
 149 |         }
 150 | 
 151 |         private static bool TableExists(SqlConnection conn, string name)
 152 |         {
 153 |             using (var cmd = new SqlCommand(
 154 |             "SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = @t", conn))
 155 |             {
 156 |                 cmd.Parameters.AddWithValue("@t", name);
 157 |                 return cmd.ExecuteScalar() != null;
 158 |             }
 159 |         }
 160 | 
 161 |         private static List<string> Cols(SqlConnection conn, string table)
 162 |         {
 163 |             var list = new List<string>();
 164 |             using (var cmd = new SqlCommand(
 165 |             "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = @t", conn))
 166 |             {
 167 |                 cmd.Parameters.AddWithValue("@t", table);
 168 |                 using (var r = cmd.ExecuteReader())
 169 |                 {
 170 |                     while (r.Read()) list.Add(r.GetString(0));
 171 |                 }
 172 |             }
 173 |             return list;
 174 |         }
 175 | 
 176 |         private static bool Has(List<string> cols, string name)
 177 |         {
 178 |             return cols.Any(c => string.Equals(c, name, StringComparison.OrdinalIgnoreCase));
 179 |         }
 180 | 
 181 |         private static string PrimaryKey(SqlConnection conn, string table)
 182 |         {
 183 |             using (var cmd = new SqlCommand(@"
 184 |             SELECT TOP 1 ku.COLUMN_NAME
 185 |             FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
 186 |             INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE ku
 187 |             ON tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME AND tc.TABLE_NAME = ku.TABLE_NAME
 188 |             WHERE tc.TABLE_NAME = @t AND tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
 189 |             ORDER BY ku.ORDINAL_POSITION", conn))
 190 |             {
 191 |                 cmd.Parameters.AddWithValue("@t", table);
 192 |                 var o = cmd.ExecuteScalar();
 193 |                 return o == null || o == DBNull.Value ? null : o.ToString();
 194 |             }
 195 |         }
 196 | 
 197 |         private static string Pick(List<string> cols, params string[] candidates)
 198 |         {
 199 |             foreach (var c in candidates)
 200 |             {
 201 |                 var hit = cols.FirstOrDefault(x => string.Equals(x, c, StringComparison.OrdinalIgnoreCase));
 202 |                 if (hit != null) return hit;
 203 |             }
 204 |             // last resort: first column (often PK)
 205 |             if (cols.Count > 0) return cols[0];
 206 |             throw new InvalidOperationException("No columns found; candidates: " + string.Join(",", candidates));
 207 |         }
 208 | 
 209 |         private static string PickOptional(List<string> cols, params string[] candidates)
 210 |         {
 211 |             foreach (var c in candidates)
 212 |             {
 213 |                 var hit = cols.FirstOrDefault(x => string.Equals(x, c, StringComparison.OrdinalIgnoreCase));
 214 |                 if (hit != null) return hit;
 215 |             }
 216 |             return null;
 217 |         }
 218 | 
 219 |         public static string Q(string ident)
 220 |         {
 221 |             if (string.IsNullOrEmpty(ident)) return ident;
 222 |             // bracket-quote for reserved words like Index
 223 |             return "[" + ident.Replace("]", "]]") + "]";
 224 |         }
 225 | 
 226 |         public static object DebugInfo()
 227 |         {
 228 |             Ensure();
 229 |             return new
 230 |             {
 231 |                 loadError = _loadError,
 232 |                 chapters = new { ChTable, ChPk, ChCourseFk, ChTitle, ChIndex },
 233 |                 sub = new { SubTable, SubPk, SubChapterFk, SubTitle, SubIndex },
 234 |                 mats = new { MatTable, MatPk, MatSubFk, MatLinksToSub, MatType, MatText, MatMedia, MatIndex }
 235 |             };
 236 |         }
 237 |     }
 238 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L7:** C# namespace grouping.
- **L51:** Error handling block.
- **L56:** Handle/log exception.
- **L71:** Import namespace/types.
<<<<<<< HEAD
=======
- **L74:** `chCols` means: Often a collection related to ch Cols (plural name).
- **L79:** `chPk` means: Holds “ch Pk” for this scope.
- **L87:** `subTable` means: Holds “sub Table” for this scope. (text)
- **L96:** `sc` means: Holds “sc” for this scope.
- **L97:** `pk` means: Holds “pk” for this scope.
- **L107:** `matTable` means: Holds “mat Table” for this scope. (text)
- **L115:** `mc` means: Holds “mc” for this scope.
- **L116:** `mPk` means: Holds “m Pk” for this scope.
>>>>>>> eb8ce01 (update)
- **L151:** Database access (pure SQL).
- **L153:** Import namespace/types.
- **L156:** Parameterized SQL — prevents classic SQL injection.
- **L157:** Run SQL; return table / rows / scalar.
- **L161:** Database access (pure SQL).
<<<<<<< HEAD
=======
- **L163:** `list` means: In-memory collection being built for JSON return.  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L164:** Import namespace/types.
- **L167:** Parameterized SQL — prevents classic SQL injection.
- **L168:** Import namespace/types.
- **L181:** Database access (pure SQL).
- **L183:** Import namespace/types.
- **L186:** Join related tables (courses ↔ chapters ↔ works ↔ users).
- **L191:** Parameterized SQL — prevents classic SQL injection.
<<<<<<< HEAD
- **L192:** Run SQL; return table / rows / scalar.
- **L193:** Null-safe read from database values.
=======
- **L192:** Run SQL; return table / rows / scalar. | `o` means: Holds “o” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY).
- **L193:** Null-safe read from database values.
- **L201:** `hit` means: Holds “hit” for this scope.
- **L213:** `hit` means: Holds “hit” for this scope.
>>>>>>> eb8ce01 (update)

## Source snapshot (raw)

```csharp
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;

namespace WebAppAssignment.Data
{
    /// <summary>
    /// Discovers real column names from EduDB via INFORMATION_SCHEMA
    /// so curriculum SQL works even when PK names differ (SchID vs ID etc.).
    /// </summary>
    public static class SchemaMap
    {
        private static readonly object Gate = new object();
        private static bool _loaded;
        private static string _loadError;

        // SubChapters
        public static string SubTable = null;
        public static string SubPk = null;
        public static string SubChapterFk = null;
        public static string SubTitle = null;
        public static string SubIndex = null; // optional

        // StudyMats
        public static string MatTable = null;
        public static string MatPk = null;
        public static string MatSubFk = null; // SchID or ChID
        public static bool MatLinksToSub = false;
        public static string MatType = null;
        public static string MatText = null;
        public static string MatMedia = null;
        public static string MatIndex = null;

        // Chapters
        public static string ChTable = "Chapters";
        public static string ChPk = "ChID";
        public static string ChCourseFk = "CID";
        public static string ChTitle = "Title";
        public static string ChIndex = null;

        public static string LoadError { get { Ensure(); return _loadError; } }

        public static void Ensure()
        {
            if (_loaded) return;
            lock (Gate)
            {
                if (_loaded) return;
                try
                {
                    Discover();
                    _loadError = null;
                }
                catch (Exception ex)
                {
                    _loadError = ex.Message;
                }
                _loaded = true;
            }
        }

        public static void Reset()
        {
            lock (Gate) { _loaded = false; _loadError = null; }
        }

        private static void Discover()
        {
            using (var conn = DbHelper.OpenConnection())
            {
                // Chapters
                var chCols = Cols(conn, "Chapters");
                if (chCols.Count == 0) chCols = Cols(conn, "Chapter");
                if (chCols.Count > 0)
                {
                    ChTable = TableExists(conn, "Chapters") ? "Chapters" : "Chapter";
                    var chPk = PrimaryKey(conn, ChTable);
                    ChPk = !string.IsNullOrEmpty(chPk) ? chPk : Pick(chCols, "ChID", "ChapterID", "ID", "Id");
                    ChCourseFk = Pick(chCols, "CID", "CourseID", "CourseId");
                    ChTitle = Pick(chCols, "Title", "Name");
                    ChIndex = PickOptional(chCols, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
                }

                // SubChapters / SubChapter / Lessons
                string subTable = null;
                foreach (var t in new[] { "SubChapters", "SubChapter", "Lessons", "Lesson" })
                {
                    if (TableExists(conn, t)) { subTable = t; break; }
                }

                if (subTable != null)
                {
                    SubTable = subTable;
                    var sc = Cols(conn, subTable);
                    var pk = PrimaryKey(conn, subTable);
                    SubPk = !string.IsNullOrEmpty(pk)
                    ? pk
                    : Pick(sc, "SchID", "SChID", "SubChapterID", "SubChapterId", "LessonID", "LessonId", "ID", "Id");
                    SubChapterFk = Pick(sc, "ChID", "ChapterID", "ChapterId");
                    SubTitle = Pick(sc, "Title", "Name", "LessonTitle");
                    SubIndex = PickOptional(sc, "Index", "Order", "OrderIndex", "SortOrder", "Idx");
                }

                // StudyMats
                string matTable = null;
                foreach (var t in new[] { "StudyMats", "StudyMat", "StudyMaterials", "Materials" })
                {
                    if (TableExists(conn, t)) { matTable = t; break; }
                }
                if (matTable != null)
                {
                    MatTable = matTable;
                    var mc = Cols(conn, matTable);
                    var mPk = PrimaryKey(conn, matTable);
                    MatPk = !string.IsNullOrEmpty(mPk) ? mPk : Pick(mc, "SMID", "MID", "MaterialID", "ID", "Id");
                    MatType = PickOptional(mc, "Type", "MaterialType", "ContentType");
                    MatText = PickOptional(mc, "TextContent", "Content", "Text", "Body");
                    MatMedia = PickOptional(mc, "MediaLink", "MediaUrl", "Link", "Url", "FilePath");
                    MatIndex = PickOptional(mc, "Index", "Order", "OrderIndex", "SortOrder", "Idx");

                    // Prefer SubChapter FK if present, else Chapter FK (legacy)
                    if (Has(mc, "SchID") || Has(mc, "SChID") || Has(mc, "SubChapterID") || Has(mc, "LessonID"))
                    {
                        MatSubFk = Pick(mc, "SchID", "SChID", "SubChapterID", "SubChapterId", "LessonID", "LessonId");
                        MatLinksToSub = true;
                    }
                    else if (Has(mc, "ChID") || Has(mc, "ChapterID"))
                    {
                        MatSubFk = Pick(mc, "ChID", "ChapterID", "ChapterId");
                        MatLinksToSub = false;
                    }
                    else if (!string.IsNullOrEmpty(SubTable) && !string.IsNullOrEmpty(SubPk) && Has(mc, SubPk))
                    {
                        MatSubFk = SubPk;
                        MatLinksToSub = true;
                    }

                    // Need at least one content column
                    if (string.IsNullOrEmpty(MatType) && string.IsNullOrEmpty(MatText) && string.IsNullOrEmpty(MatMedia))
                    {
                        MatText = mc.FirstOrDefault(c =>
                        !string.Equals(c, MatPk, StringComparison.OrdinalIgnoreCase) &&
                        !string.Equals(c, MatSubFk, StringComparison.OrdinalIgnoreCase));
                    }
                }
            }
        }

        private static bool TableExists(SqlConnection conn, string name)
        {
            using (var cmd = new SqlCommand(
            "SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = @t", conn))
            {
                cmd.Parameters.AddWithValue("@t", name);
                return cmd.ExecuteScalar() != null;
            }
        }

        private static List<string> Cols(SqlConnection conn, string table)
        {
            var list = new List<string>();
            using (var cmd = new SqlCommand(
            "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = @t", conn))
            {
                cmd.Parameters.AddWithValue("@t", table);
                using (var r = cmd.ExecuteReader())
                {
                    while (r.Read()) list.Add(r.GetString(0));
                }
            }
            return list;
        }

        private static bool Has(List<string> cols, string name)
        {
            return cols.Any(c => string.Equals(c, name, StringComparison.OrdinalIgnoreCase));
        }

        private static string PrimaryKey(SqlConnection conn, string table)
        {
            using (var cmd = new SqlCommand(@"
            SELECT TOP 1 ku.COLUMN_NAME
            FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
            INNER JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE ku
            ON tc.CONSTRAINT_NAME = ku.CONSTRAINT_NAME AND tc.TABLE_NAME = ku.TABLE_NAME
            WHERE tc.TABLE_NAME = @t AND tc.CONSTRAINT_TYPE = 'PRIMARY KEY'
            ORDER BY ku.ORDINAL_POSITION", conn))
            {
                cmd.Parameters.AddWithValue("@t", table);
                var o = cmd.ExecuteScalar();
                return o == null || o == DBNull.Value ? null : o.ToString();
            }
        }

        private static string Pick(List<string> cols, params string[] candidates)
        {
            foreach (var c in candidates)
            {
                var hit = cols.FirstOrDefault(x => string.Equals(x, c, StringComparison.OrdinalIgnoreCase));
                if (hit != null) return hit;
            }
            // last resort: first column (often PK)
            if (cols.Count > 0) return cols[0];
            throw new InvalidOperationException("No columns found; candidates: " + string.Join(",", candidates));
        }

        private static string PickOptional(List<string> cols, params string[] candidates)
        {
            foreach (var c in candidates)
            {
                var hit = cols.FirstOrDefault(x => string.Equals(x, c, StringComparison.OrdinalIgnoreCase));
                if (hit != null) return hit;
            }
            return null;
        }

        public static string Q(string ident)
        {
            if (string.IsNullOrEmpty(ident)) return ident;
            // bracket-quote for reserved words like Index
            return "[" + ident.Replace("]", "]]") + "]";
        }

        public static object DebugInfo()
        {
            Ensure();
            return new
            {
                loadError = _loadError,
                chapters = new { ChTable, ChPk, ChCourseFk, ChTitle, ChIndex },
                sub = new { SubTable, SubPk, SubChapterFk, SubTitle, SubIndex },
                mats = new { MatTable, MatPk, MatSubFk, MatLinksToSub, MatType, MatText, MatMedia, MatIndex }
            };
        }
    }
}

```
