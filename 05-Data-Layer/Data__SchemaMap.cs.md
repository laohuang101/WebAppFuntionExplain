# SchemaMap.cs
**Source:** `Data/SchemaMap.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Discovers real table/column names in the attached MDF (SubChapters vs Lessons, etc.) so curriculum SQL adapts.

## File overview

- **Total lines:** 238
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `Gate` | `object` | Holds “Gate” for this scope. |
| `_loaded` | `bool` | Holds “loaded” for this scope. (true/false) |
| `_loadError` | `string` | Holds “load Error” for this scope. (text) |
| `SubTable` | `string` | Holds “Sub Table” for this scope. (text) |
| `SubPk` | `string` | Holds “Sub Pk” for this scope. (text) |
| `SubChapterFk` | `string` | Holds “Sub Chapter Fk” for this scope. (text) |
| `SubTitle` | `string` | Holds “Sub Title” for this scope. (text) |
| `SubIndex` | `string` | Holds “Sub Index” for this scope. (text) |
| `MatTable` | `string` | Holds “Mat Table” for this scope. (text) |
| `MatPk` | `string` | Holds “Mat Pk” for this scope. (text) |
| `MatSubFk` | `string` | Holds “Mat Sub Fk” for this scope. (text) |
| `MatLinksToSub` | `bool` | Holds “Mat Links To Sub” for this scope. (true/false) |
| `MatType` | `string` | Holds “Mat Type” for this scope. (text) |
| `MatText` | `string` | Holds “Mat Text” for this scope. (text) |
| `MatMedia` | `string` | Holds “Mat Media” for this scope. (text) |
| `MatIndex` | `string` | Holds “Mat Index” for this scope. (text) |
| `ChTable` | `string` | Holds “Ch Table” for this scope. (text) |
| `ChPk` | `string` | Holds “Ch Pk” for this scope. (text) |
| `ChCourseFk` | `string` | Holds “Ch Course Fk” for this scope. (text) |
| `ChTitle` | `string` | Holds “Ch Title” for this scope. (text) |
| `ChIndex` | `string` | Holds “Ch Index” for this scope. (text) |

## Functions / methods (11 found)

### `Ensure` — lines 44–62

#### Signature

```csharp
public static void Ensure()
```

#### What it is

Makes sure **** exists or is valid before the rest of the code continues.

#### How it works

1. Starts when something calls `Ensure`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `Reset` — lines 63–67

#### Signature

```csharp
public static void Reset()
```

#### What it is

Function `Reset` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Reset`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  63 | 
  64 |         public static void Reset()
  65 |         {
  66 |             lock (Gate) { _loaded = false; _loadError = null; }
  67 |         }
```

---

### `Discover` — lines 68–149

#### Signature

```csharp
private static void Discover()
```

#### What it is

Function `Discover` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Open a connection to the LocalDB / SQL Server database.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server. |
| `chPk` | `var` | Holds “ch Pk” for this scope. |
| `subTable` | `string` | Holds “sub Table” for this scope. (text) |
| `sc` | `var` | Holds “sc” for this scope. |
| `pk` | `var` | Holds “pk” for this scope. |
| `matTable` | `string` | Holds “mat Table” for this scope. (text) |
| `mc` | `var` | Holds “mc” for this scope. |
| `mPk` | `var` | Holds “m Pk” for this scope. |
| `t` | `—` | Temporary string/token/time value. |

#### Code

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

---

### `TableExists` — lines 150–159

#### Signature

```csharp
private static bool TableExists(SqlConnection conn, string name)
```

#### What it is

Function `TableExists` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `name` | `string` | Display name of user/course/criterion. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |

#### Code

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

---

### `Cols` — lines 160–174

#### Signature

```csharp
private static List<string> Cols(SqlConnection conn, string table)
```

#### What it is

Function `Cols` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Cols`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `table` | `string` | DataTable or HTML table container. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `list` | `var` | In-memory collection being built for JSON return.  Newly constructed object. |
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |
| `r` | `var` | Usually one database row (DataRow) in query loops. |

#### Code

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

---

### `Has` — lines 175–179

#### Signature

```csharp
private static bool Has(List<string> cols, string name)
```

#### What it is

Checks a condition related to **Has** and returns true/false (or tries an action safely).

#### How it works

1. Starts when something calls `Has`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cols` | `List<string>` | Often a collection related to cols (plural name). (text) |
| `name` | `string` | Display name of user/course/criterion. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 175 | 
 176 |         private static bool Has(List<string> cols, string name)
 177 |         {
 178 |             return cols.Any(c => string.Equals(c, name, StringComparison.OrdinalIgnoreCase));
 179 |         }
```

---

### `PrimaryKey` — lines 180–195

#### Signature

```csharp
private static string PrimaryKey(SqlConnection conn, string table)
```

#### What it is

Function `PrimaryKey` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `table` | `string` | DataTable or HTML table container. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |
| `o` | `var` | Holds “o” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY). |

#### Code

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

---

### `Pick` — lines 196–207

#### Signature

```csharp
private static string Pick(List<string> cols, params string[] candidates)
```

#### What it is

Function `Pick` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Stop with an error (invalid access or bad input).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cols` | `List<string>` | Often a collection related to cols (plural name). (text) |
| `candidates` | `string[]` | Boolean flag: candidates. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `hit` | `var` | Holds “hit” for this scope. |
| `c` | `—` | Temporary value (character, course, or counter depending on loop). |

#### Code

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

---

### `PickOptional` — lines 208–217

#### Signature

```csharp
private static string PickOptional(List<string> cols, params string[] candidates)
```

#### What it is

Function `PickOptional` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `PickOptional`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cols` | `List<string>` | Often a collection related to cols (plural name). (text) |
| `candidates` | `string[]` | Boolean flag: candidates. (text) |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `hit` | `var` | Holds “hit” for this scope. |
| `c` | `—` | Temporary value (character, course, or counter depending on loop). |

#### Code

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

---

### `Q` — lines 218–224

#### Signature

```csharp
public static string Q(string ident)
```

#### What it is

Function `Q` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `ident` | `string` | Holds “ident” for this scope. (text) |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

#### Signature

```csharp
public static object DebugInfo()
```

#### What it is

Function `DebugInfo` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `DebugInfo`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
