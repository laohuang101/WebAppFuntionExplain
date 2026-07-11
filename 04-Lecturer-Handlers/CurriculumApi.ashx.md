# CurriculumApi.ashx
**Source:** `Pages/Lecturer/CurriculumApi.ashx`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

JSON ashx API for curriculum CRUD with ownership (`LecturerUID`) checks.

## File overview

- **Total lines:** 1284
- **Kind:** `.ashx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (32 found)

### `ProcessRequest` — lines 22–94

```
public void ProcessRequest(HttpContext context)
```

#### Explanation

- **Purpose:** Implements `ProcessRequest`.
- **Security:** Uses AuthGate — requires logged-in role.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext context`
- **Local variables:** `uid`, `action`, `body`, `reader`

#### Line-by-line (this function)

`  22`  ``
`  23`  `    public void ProcessRequest(HttpContext context)`
  - → IHttpHandler entry for ashx.
`  24`  `    {`
`  25`  `        context.Response.ContentType = "application/json; charset=utf-8";`
`  26`  `        context.Response.Cache.SetCacheability(HttpCacheability.NoCache);`
`  27`  ``
`  28`  `        try`
  - → Error handling block.
`  29`  `        {`
`  30`  `            int uid = AuthGate.RequireLecturer(context);`
  - → Authorization — block wrong role / anonymous.
`  31`  `            if (uid <= 0)`
`  32`  `            {`
`  33`  `                Write(context, AuthGate.NotAuthenticatedJson("Lecturer sign-in required."));`
  - → Authorization — block wrong role / anonymous.
`  34`  `                return;`
`  35`  `            }`
`  36`  ``
`  37`  `            SchemaMap.Ensure();`
`  38`  ``
`  39`  `            string action = (context.Request["action"] ?? "").Trim().ToLowerInvariant();`
`  40`  `            string body = null;`
`  41`  `            if (context.Request.HttpMethod == "POST" &&`
`  42`  `                (context.Request.ContentType ?? "").IndexOf("json", StringComparison.OrdinalIgnoreCase) >= 0)`
`  43`  `            {`
`  44`  `                using (var reader = new StreamReader(context.Request.InputStream))`
  - → Import namespace/types.
`  45`  `                    body = reader.ReadToEnd();`
`  46`  `            }`
`  47`  ``
`  48`  `            Dictionary<string, object> data = null;`
`  49`  `            if (!string.IsNullOrWhiteSpace(body))`
`  50`  `            {`
`  51`  `                try { data = Json.Deserialize<Dictionary<string, object>>(body); } catch { data = null; }`
  - → Error handling block.
`  52`  `                if (data != null && data.ContainsKey("action") && string.IsNullOrEmpty(action))`
`  53`  `                    action = Convert.ToString(data["action"]).ToLowerInvariant();`
`  54`  `            }`
`  55`  ``
`  56`  `            switch (action)`
`  57`  `            {`
`  58`  `                case "schema":`
`  59`  `                    Write(context, new { success = true, schema = SchemaMap.DebugInfo() });`
`  60`  `                    break;`
`  61`  `                case "get":`
`  62`  `                    Write(context, GetCurriculum(uid, GetInt(data, context, "cid")));`
`  63`  `                    break;`
`  64`  `                case "save_section":`
`  65`  `                    Write(context, SaveSection(uid, GetInt(data, context, "chid"), GetInt(data, context, "cid"), GetStr(data, context, "title")));`
`  66`  `                    break;`
`  67`  `                case "delete_section":`
`  68`  `                    Write(context, DeleteSection(uid, GetInt(data, context, "chid")));`
`  69`  `                    break;`
`  70`  `                case "save_lesson":`
`  71`  `                    Write(context, SaveLesson(uid,`
`  72`  `                        GetInt(data, context, "schid"),`
`  73`  `                        GetInt(data, context, "chid"),`
`  74`  `                        GetStr(data, context, "title"),`
`  75`  `                        GetStr(data, context, "type"),`
`  76`  `                        GetStr(data, context, "content"),`
`  77`  `                        GetStr(data, context, "materialsJson")));`
`  78`  `                    break;`
`  79`  `                case "delete_lesson":`
`  80`  `                    Write(context, DeleteLesson(uid, GetInt(data, context, "schid")));`
`  81`  `                    break;`
`  82`  `                case "get_lesson":`
`  83`  `                    Write(context, GetLesson(uid, GetInt(data, context, "schid")));`
`  84`  `                    break;`
`  85`  `                default:`
`  86`  `                    Write(context, new { success = false, message = "Unknown action: " + action, schema = SchemaMap.DebugInfo() });`
`  87`  `                    break;`
`  88`  `            }`
`  89`  `        }`
`  90`  `        catch (Exception ex)`
  - → Handle/log exception.
`  91`  `        {`
`  92`  `            Write(context, new { success = false, message = ex.Message, detail = ex.ToString(), schema = SchemaMap.DebugInfo() });`
`  93`  `        }`
`  94`  `    }`

---

### `GetCurriculum` — lines 99–276

```
private object GetCurriculum(int lecturerUid, int cid)
```

#### Explanation

- **Purpose:** Implements `GetCurriculum`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Read/load data for display.
- **Parameters:** `int lecturerUid, int cid`
- **Local variables:** `chapters`, `conn`, `chDt`, `chid`, `lessons`, `schid`, `materials`, `matSql`, `mats`, `lessonTitle`, `text`, `media`, `t`, `smid`, `i`, `type`, `content`, `p`

#### Line-by-line (this function)

`  99`  ``
` 100`  `    private object GetCurriculum(int lecturerUid, int cid)`
` 101`  `    {`
` 102`  `        if (cid <= 0) return new { success = false, message = "Invalid course id." };`
` 103`  ``
` 104`  `        var chapters = new List<object>();`
` 105`  `        using (var conn = Open())`
  - → Import namespace/types.
` 106`  `        {`
` 107`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 108`  ``
` 109`  `            string chSql;`
` 110`  `            if (!string.IsNullOrEmpty(SchemaMap.ChIndex))`
` 111`  `            {`
` 112`  `                chSql = string.Format(`
` 113`  `                    "SELECT {0} AS ChID, {1} AS CID, {2} AS Idx, {3} AS Title FROM {4} WHERE {1}=@CID ORDER BY {2}, {0}",`
` 114`  `                    Q(SchemaMap.ChPk), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChIndex), Q(SchemaMap.ChTitle), Q(SchemaMap.ChTable));`
` 115`  `            }`
` 116`  `            else`
` 117`  `            {`
` 118`  `                chSql = string.Format(`
` 119`  `                    "SELECT {0} AS ChID, {1} AS CID, {2} AS Title FROM {3} WHERE {1}=@CID ORDER BY {0}",`
` 120`  `                    Q(SchemaMap.ChPk), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTitle), Q(SchemaMap.ChTable));`
` 121`  `            }`
` 122`  ``
` 123`  `            DataTable chDt = Query(conn, chSql, P("@CID", cid));`
` 124`  ``
` 125`  `            foreach (DataRow ch in chDt.Rows)`
` 126`  `            {`
` 127`  `                int chid = Convert.ToInt32(ch["ChID"]);`
` 128`  `                var lessons = new List<object>();`
` 129`  ``
` 130`  `                // Preferred: SubChapters/Lessons table holds one row per lesson`
` 131`  `                if (!string.IsNullOrEmpty(SchemaMap.SubTable) && !string.IsNullOrEmpty(SchemaMap.SubPk))`
` 132`  `                {`
` 133`  `                    string scSql;`
` 134`  `                    if (!string.IsNullOrEmpty(SchemaMap.SubIndex))`
` 135`  `                    {`
` 136`  `                        scSql = string.Format(`
` 137`  `                            "SELECT {0} AS SchID, {1} AS ChID, {2} AS Idx, {3} AS Title FROM {4} WHERE {1}=@ChID ORDER BY {2}, {0}",`
` 138`  `                            Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubIndex), Q(SchemaMap.SubTitle), Q(SchemaMap.SubTable));`
` 139`  `                    }`
` 140`  `                    else`
` 141`  `                    {`
` 142`  `                        scSql = string.Format(`
` 143`  `                            "SELECT {0} AS SchID, {1} AS ChID, {2} AS Title FROM {3} WHERE {1}=@ChID ORDER BY {0}",`
` 144`  `                            Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTitle), Q(SchemaMap.SubTable));`
` 145`  `                    }`
` 146`  ``
` 147`  `                    DataTable scDt;`
` 148`  `                    try`
  - → Error handling block.
` 149`  `                    {`
` 150`  `                        scDt = Query(conn, scSql, P("@ChID", chid));`
` 151`  `                    }`
` 152`  `                    catch (Exception ex)`
  - → Handle/log exception.
` 153`  `                    {`
` 154`  `                        return new`
` 155`  `                        {`
` 156`  `                            success = false,`
` 157`  `                            message = "Sub-lessons query failed: " + ex.Message,`
` 158`  `                            schema = SchemaMap.DebugInfo(),`
` 159`  `                            sql = scSql`
` 160`  `                        };`
` 161`  `                    }`
` 162`  ``
` 163`  `                    foreach (DataRow sc in scDt.Rows)`
` 164`  `                    {`
` 165`  `                        int schid = Convert.ToInt32(sc["SchID"]);`
` 166`  `                        string type, content;`
` 167`  `                        // mats may hang on lesson id OR chapter id depending on schema`
` 168`  `                        var materials = SchemaMap.MatLinksToSub`
` 169`  `                            ? LoadMats(conn, schid, out type, out content)`
` 170`  `                            : LoadMats(conn, chid, out type, out content);`
` 171`  ``
` 172`  `                        // If mats hang on chapter, try to pick body for this lesson title`
` 173`  `                        if (!SchemaMap.MatLinksToSub && !string.IsNullOrEmpty(content) && content.Contains("<<<BODY>>>"))`
` 174`  `                        {`
` 175`  `                            // content may be for a different lesson; re-scan mats`
` 176`  `                            try`
  - → Error handling block.
` 177`  `                            {`
` 178`  `                                string matSql = BuildMatSelect() + " WHERE " + Q(SchemaMap.MatSubFk) + "=@Key ORDER BY " + Q(SchemaMap.MatPk);`
` 179`  `                                var mats = Query(conn, matSql, P("@Key", chid));`
` 180`  `                                string lessonTitle = Safe(sc["Title"]);`
` 181`  `                                type = "Text";`
` 182`  `                                content = "";`
` 183`  `                                materials = new List<object>();`
` 184`  `                                foreach (DataRow m in mats.Rows)`
` 185`  `                                {`
` 186`  `                                    var text = Col(m, "TextCol");`
` 187`  `                                    var media = Col(m, "MediaCol");`
` 188`  `                                    var t = Col(m, "TypeCol");`
` 189`  `                                    if (!string.IsNullOrEmpty(text) && text.StartsWith(lessonTitle + "\n<<<BODY>>>", StringComparison.Ordinal))`
` 190`  `                                    {`
` 191`  `                                        type = string.IsNullOrEmpty(t) ? "Text" : t;`
` 192`  `                                        content = text.Substring((lessonTitle + "\n<<<BODY>>>\n").Length);`
` 193`  `                                        if (!string.IsNullOrEmpty(media)) content = media;`
` 194`  `                                    }`
` 195`  `                                    else if (!string.IsNullOrEmpty(text) && text == lessonTitle)`
` 196`  `                                    {`
` 197`  `                                        type = string.IsNullOrEmpty(t) ? "Text" : t;`
` 198`  `                                        content = media ?? "";`
` 199`  `                                    }`
` 200`  `                                    int smid = 0;`
` 201`  `                                    try { smid = Convert.ToInt32(m["SMID"]); } catch { }`
  - → Error handling block.
` 202`  `                                    materials.Add(new { smid = smid, type = t, textContent = text, mediaLink = media, url = media, fileName = text });`
` 203`  `                                }`
` 204`  `                            }`
` 205`  `                            catch { }`
  - → Handle/log exception.
` 206`  `                        }`
` 207`  ``
` 208`  `                        lessons.Add(new`
` 209`  `                        {`
` 210`  `                            schid = schid,`
` 211`  `                            title = Safe(sc["Title"]),`
` 212`  `                            type = type,`
` 213`  `                            content = content,`
` 214`  `                            materials = materials`
` 215`  `                        });`
` 216`  `                    }`
` 217`  `                }`
` 218`  `                else if (!string.IsNullOrEmpty(SchemaMap.MatTable))`
` 219`  `                {`
` 220`  `                    // Fallback: each StudyMat row is a lesson under the chapter`
` 221`  `                    try`
  - → Error handling block.
` 222`  `                    {`
` 223`  `                        string matSql = BuildMatSelect() + " WHERE " + Q(SchemaMap.MatSubFk) + "=@Key ORDER BY " + Q(SchemaMap.MatPk);`
` 224`  `                        var mats = Query(conn, matSql, P("@Key", chid));`
` 225`  `                        int i = 0;`
` 226`  `                        foreach (DataRow m in mats.Rows)`
` 227`  `                        {`
` 228`  `                            i++;`
` 229`  `                            string type = Col(m, "TypeCol");`
` 230`  `                            if (string.IsNullOrEmpty(type)) type = "Text";`
` 231`  `                            var media = Col(m, "MediaCol");`
` 232`  `                            var text = Col(m, "TextCol");`
` 233`  `                            string content = text ?? "";`
` 234`  `                            string lessonTitle = "Lesson " + i;`
` 235`  `                            if (!string.IsNullOrEmpty(text) && text.Contains("<<<BODY>>>"))`
` 236`  `                            {`
` 237`  `                                int p = text.IndexOf("\n<<<BODY>>>\n", StringComparison.Ordinal);`
` 238`  `                                if (p > 0)`
` 239`  `                                {`
` 240`  `                                    lessonTitle = text.Substring(0, p);`
` 241`  `                                    content = text.Substring(p + "\n<<<BODY>>>\n".Length);`
` 242`  `                                }`
` 243`  `                            }`
` 244`  `                            else if (!string.IsNullOrEmpty(text) && text.Length < 80)`
` 245`  `                            {`
` 246`  `                                lessonTitle = text;`
` 247`  `                            }`
` 248`  `                            if (!string.IsNullOrEmpty(media)) content = media;`
` 249`  ``
` 250`  `                            int smid = 0;`
` 251`  `                            try { smid = Convert.ToInt32(m["SMID"]); } catch { smid = i; }`
  - → Error handling block.
` 252`  ``
` 253`  `                            lessons.Add(new`
` 254`  `                            {`
` 255`  `                                schid = smid,`
` 256`  `                                title = lessonTitle,`
` 257`  `                                type = type,`
` 258`  `                                content = content,`
` 259`  `                                materials = new object[0]`
` 260`  `                            });`
` 261`  `                        }`
` 262`  `                    }`
` 263`  `                    catch { /* no mats */ }`
  - → Handle/log exception.
` 264`  `                }`
` 265`  ``
` 266`  `                chapters.Add(new`
` 267`  `                {`
` 268`  `                    chid = chid,`
` 269`  `                    title = Safe(ch["Title"]),`
` 270`  `                    lessons = lessons`
` 271`  `                });`
` 272`  `            }`
` 273`  `        }`
` 274`  ``
` 275`  `        return new { success = true, chapters = chapters, schema = SchemaMap.DebugInfo() };`
` 276`  `    }`

---

### `LoadMats` — lines 277–426

```
private List<object> LoadMats(SqlConnection conn, int parentId, out string type, out string content)
```

#### Explanation

- **Purpose:** Implements `LoadMats`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Read/load data for display.
- **Parameters:** `SqlConnection conn, int parentId, out string type, out string content`
- **Local variables:** `materials`, `mats`, `orderBy`, `sql`, `media0`, `t0`, `mediaB`, `textB`, `smid`, `media`, `text`, `t`, `bareName`, `fn`, `rel`, `linkOut`

#### Line-by-line (this function)

` 277`  ``
` 278`  `    private List<object> LoadMats(SqlConnection conn, int parentId, out string type, out string content)`
  - → Database access (pure SQL).
` 279`  `    {`
` 280`  `        type = "Text";`
` 281`  `        content = "";`
` 282`  `        var materials = new List<object>();`
` 283`  `        try`
  - → Error handling block.
` 284`  `        {`
` 285`  `            DataTable mats = null;`
` 286`  `            // Prefer SchemaMap query; fall back to classic StudyMats`
` 287`  `            try`
  - → Error handling block.
` 288`  `            {`
` 289`  `                if (!string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 290`  `                {`
` 291`  `                    string orderBy = !string.IsNullOrEmpty(SchemaMap.MatIndex)`
` 292`  `                        ? Q(SchemaMap.MatIndex) + ", " + Q(SchemaMap.MatPk)`
` 293`  `                        : Q(SchemaMap.MatPk);`
` 294`  `                    string sql = BuildMatSelect() +`
` 295`  `                                 " WHERE " + Q(SchemaMap.MatSubFk) + "=@Key ORDER BY " + orderBy;`
` 296`  `                    mats = Query(conn, sql, P("@Key", parentId));`
` 297`  `                }`
` 298`  `            }`
` 299`  `            catch { mats = null; }`
  - → Handle/log exception.
` 300`  ``
` 301`  `            if (mats == null || mats.Rows.Count == 0)`
` 302`  `            {`
` 303`  `                try`
  - → Error handling block.
` 304`  `                {`
` 305`  `                    mats = Query(conn, @"`
` 306`  `SELECT SMID, Type AS TypeCol, TextContent AS TextCol, MediaLink AS MediaCol`
` 307`  `FROM StudyMats WHERE SchID=@Key ORDER BY [Index], SMID", P("@Key", parentId));`
` 308`  `                }`
` 309`  `                catch`
  - → Handle/log exception.
` 310`  `                {`
` 311`  `                    try`
  - → Error handling block.
` 312`  `                    {`
` 313`  `                        mats = Query(conn, @"`
` 314`  `SELECT SMID, Type AS TypeCol, TextContent AS TextCol, MediaLink AS MediaCol`
` 315`  `FROM StudyMats WHERE SchID=@Key ORDER BY SMID", P("@Key", parentId));`
` 316`  `                    }`
` 317`  `                    catch { mats = new DataTable(); }`
  - → Handle/log exception.
` 318`  `                }`
` 319`  `            }`
` 320`  ``
` 321`  `            if (mats.Rows.Count > 0)`
` 322`  `            {`
` 323`  `                // Prefer first file row as primary content when present (preview)`
` 324`  `                DataRow bodyRow = mats.Rows[0];`
` 325`  `                DataRow fileRow = null;`
` 326`  `                foreach (DataRow r in mats.Rows)`
` 327`  `                {`
` 328`  `                    var media0 = Col(r, "MediaCol");`
` 329`  `                    var t0 = Col(r, "TypeCol") ?? "";`
` 330`  `                    if (LooksLikeFileUrl(media0) ||`
` 331`  `                        string.Equals(t0, "Video", StringComparison.OrdinalIgnoreCase) ||`
` 332`  `                        string.Equals(t0, "PDF", StringComparison.OrdinalIgnoreCase) ||`
` 333`  `                        string.Equals(t0, "Image", StringComparison.OrdinalIgnoreCase) ||`
` 334`  `                        string.Equals(t0, "File", StringComparison.OrdinalIgnoreCase))`
` 335`  `                    {`
` 336`  `                        if (fileRow == null) fileRow = r;`
` 337`  `                    }`
` 338`  `                }`
` 339`  `                // Body text row if any`
` 340`  `                foreach (DataRow r in mats.Rows)`
` 341`  `                {`
` 342`  `                    var t0 = Col(r, "TypeCol") ?? "";`
` 343`  `                    var media0 = Col(r, "MediaCol");`
` 344`  `                    if (string.Equals(t0, "Text", StringComparison.OrdinalIgnoreCase) ||`
` 345`  `                        string.IsNullOrEmpty(media0) || !LooksLikeFileUrl(media0))`
` 346`  `                    {`
` 347`  `                        bodyRow = r;`
` 348`  `                        break;`
` 349`  `                    }`
` 350`  `                }`
` 351`  ``
` 352`  `                if (fileRow != null)`
` 353`  `                {`
` 354`  `                    type = Col(fileRow, "TypeCol");`
` 355`  `                    if (string.IsNullOrEmpty(type)) type = GuessTypeFromUrl(Col(fileRow, "MediaCol"));`
` 356`  `                    content = Col(fileRow, "MediaCol");`
` 357`  `                    if (string.IsNullOrEmpty(content)) content = Col(fileRow, "TextCol");`
` 358`  `                }`
` 359`  `                else`
` 360`  `                {`
` 361`  `                    type = Col(bodyRow, "TypeCol");`
` 362`  `                    if (string.IsNullOrEmpty(type)) type = "Text";`
` 363`  `                    var mediaB = Col(bodyRow, "MediaCol");`
` 364`  `                    var textB = Col(bodyRow, "TextCol");`
` 365`  `                    content = !string.IsNullOrEmpty(mediaB) && LooksLikeFileUrl(mediaB) ? mediaB : textB;`
` 366`  `                    if (string.IsNullOrEmpty(content)) content = mediaB;`
` 367`  `                }`
` 368`  `            }`
` 369`  ``
` 370`  `            foreach (DataRow m in mats.Rows)`
` 371`  `            {`
` 372`  `                int smid = 0;`
` 373`  `                try { smid = Convert.ToInt32(m["SMID"]); } catch { }`
  - → Error handling block.
` 374`  `                var media = Col(m, "MediaCol");`
` 375`  `                var text = Col(m, "TextCol");`
` 376`  `                var t = Col(m, "TypeCol");`
` 377`  `                // ONLY promote TextContent → media when it is a real store path (GUID / Uploads/...)`
` 378`  `                // Never use original display names like "My Report.pdf" as paths.`
` 379`  `                if (string.IsNullOrEmpty(media) && IsStoredMediaPath(text))`
` 380`  `                    media = text;`
` 381`  `                // If media is a bare original name, keep fileName for Media.ashx .meta lookup`
` 382`  `                string bareName = null;`
` 383`  `                if (!string.IsNullOrEmpty(media) && !IsStoredMediaPath(media))`
` 384`  `                {`
` 385`  `                    bareName = Path.GetFileName(media.Replace('\\', '/'));`
` 386`  `                    media = null;`
` 387`  `                }`
` 388`  ``
` 389`  `                string fn = !string.IsNullOrEmpty(text) ? text : bareName;`
` 390`  `                if (string.IsNullOrEmpty(fn) && IsStoredMediaPath(media))`
` 391`  `                    fn = Path.GetFileName(media.Replace('\\', '/'));`
` 392`  ``
` 393`  `                // When we have GUID path + original name, write .meta so Media.ashx can resolve name→guid`
` 394`  `                if (IsStoredMediaPath(media) && !string.IsNullOrEmpty(fn))`
` 395`  `                {`
` 396`  `                    try`
  - → Error handling block.
` 397`  `                    {`
` 398`  `                        string rel = media.Replace('\\', '/');`
` 399`  `                        if (rel.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))`
` 400`  `                            rel = rel.Substring(8);`
` 401`  `                        // HttpContext available via Open() callers — use MapPath from connection's... `
` 402`  `                        // Skip here; UploadMedia writes .meta. Repair via Media.ashx log/meta only.`
` 403`  `                    }`
` 404`  `                    catch { }`
  - → Handle/log exception.
` 405`  `                }`
` 406`  ``
` 407`  `                // For preview: prefer GUID mediaLink; else pass original name for .meta lookup`
` 408`  `                string linkOut = media;`
` 409`  `                if (string.IsNullOrEmpty(linkOut) && !string.IsNullOrEmpty(fn) &&`
` 410`  `                    fn.IndexOf('.') > 0)`
` 411`  `                    linkOut = fn; // Media.ashx FindByOriginalName`
` 412`  ``
` 413`  `                materials.Add(new`
` 414`  `                {`
` 415`  `                    smid = smid,`
` 416`  `                    type = string.IsNullOrEmpty(t) ? GuessTypeFromUrl(media ?? text ?? "") : t,`
` 417`  `                    textContent = text,`
` 418`  `                    mediaLink = linkOut,`
` 419`  `                    url = linkOut,`
` 420`  `                    fileName = fn`
` 421`  `                });`
` 422`  `            }`
` 423`  `        }`
` 424`  `        catch { }`
  - → Handle/log exception.
` 425`  `        return materials;`
` 426`  `    }`

---

### `BuildMatSelect` — lines 427–442

```
private static string BuildMatSelect()
```

#### Explanation

- **Purpose:** Implements `BuildMatSelect`.
- **Local variables:** `typeExpr`, `textExpr`, `mediaExpr`

#### Line-by-line (this function)

` 427`  ``
` 428`  `    private static string BuildMatSelect()`
` 429`  `    {`
` 430`  `        string typeExpr = string.IsNullOrEmpty(SchemaMap.MatType)`
` 431`  `            ? "CAST(NULL AS nvarchar(100))" : Q(SchemaMap.MatType);`
` 432`  `        string textExpr = string.IsNullOrEmpty(SchemaMap.MatText)`
` 433`  `            ? "CAST(NULL AS nvarchar(max))" : Q(SchemaMap.MatText);`
` 434`  `        string mediaExpr = string.IsNullOrEmpty(SchemaMap.MatMedia)`
` 435`  `            ? "CAST(NULL AS nvarchar(max))" : Q(SchemaMap.MatMedia);`
` 436`  `        return "SELECT " +`
` 437`  `               Q(SchemaMap.MatPk) + " AS SMID, " +`
` 438`  `               typeExpr + " AS TypeCol, " +`
` 439`  `               textExpr + " AS TextCol, " +`
` 440`  `               mediaExpr + " AS MediaCol " +`
` 441`  `               "FROM " + Q(SchemaMap.MatTable);`
` 442`  `    }`

---

### `SaveSection` — lines 447–485

```
private object SaveSection(int lecturerUid, int chid, int cid, string title)
```

#### Explanation

- **Purpose:** Implements `SaveSection`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid, int chid, int cid, string title`
- **Local variables:** `conn`, `sql`, `next`

#### Line-by-line (this function)

` 447`  ``
` 448`  `    private object SaveSection(int lecturerUid, int chid, int cid, string title)`
` 449`  `    {`
` 450`  `        if (cid <= 0) return new { success = false, message = "Invalid course id." };`
` 451`  `        if (string.IsNullOrWhiteSpace(title)) return new { success = false, message = "Section title required." };`
` 452`  ``
` 453`  `        using (var conn = Open())`
  - → Import namespace/types.
` 454`  `        {`
` 455`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 456`  `            if (chid > 0)`
` 457`  `            {`
` 458`  `                string sql = string.Format("UPDATE {0} SET {1}=@Title WHERE {2}=@ChID AND {3}=@CID",`
` 459`  `                    Q(SchemaMap.ChTable), Q(SchemaMap.ChTitle), Q(SchemaMap.ChPk), Q(SchemaMap.ChCourseFk));`
` 460`  `                Exec(conn, sql, P("@Title", title.Trim()), P("@ChID", chid), P("@CID", cid));`
` 461`  `                return new { success = true, chid = chid };`
` 462`  `            }`
` 463`  ``
` 464`  `            int newId;`
` 465`  `            if (!string.IsNullOrEmpty(SchemaMap.ChIndex))`
` 466`  `            {`
` 467`  `                int next = ScalarInt(conn,`
` 468`  `                    string.Format("SELECT ISNULL(MAX({0}),0)+1 FROM {1} WHERE {2}=@CID",`
` 469`  `                        Q(SchemaMap.ChIndex), Q(SchemaMap.ChTable), Q(SchemaMap.ChCourseFk)),`
` 470`  `                    P("@CID", cid));`
` 471`  `                newId = ScalarInt(conn,`
` 472`  `                    string.Format("INSERT INTO {0} ({1}, {2}, {3}) OUTPUT INSERTED.{4} VALUES (@CID, @Idx, @Title)",`
` 473`  `                        Q(SchemaMap.ChTable), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChIndex), Q(SchemaMap.ChTitle), Q(SchemaMap.ChPk)),`
` 474`  `                    P("@CID", cid), P("@Idx", next), P("@Title", title.Trim()));`
` 475`  `            }`
` 476`  `            else`
` 477`  `            {`
` 478`  `                newId = ScalarInt(conn,`
` 479`  `                    string.Format("INSERT INTO {0} ({1}, {2}) OUTPUT INSERTED.{3} VALUES (@CID, @Title)",`
` 480`  `                        Q(SchemaMap.ChTable), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTitle), Q(SchemaMap.ChPk)),`
` 481`  `                    P("@CID", cid), P("@Title", title.Trim()));`
` 482`  `            }`
` 483`  `            return new { success = true, chid = newId };`
` 484`  `        }`
` 485`  `    }`

---

### `DeleteSection` — lines 486–531

```
private object DeleteSection(int lecturerUid, int chid)
```

#### Explanation

- **Purpose:** Implements `DeleteSection`.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Delete/clear data.
- **Parameters:** `int lecturerUid, int chid`
- **Local variables:** `conn`, `cid`

#### Line-by-line (this function)

` 486`  ``
` 487`  `    private object DeleteSection(int lecturerUid, int chid)`
` 488`  `    {`
` 489`  `        if (chid <= 0) return new { success = false, message = "Invalid section id." };`
` 490`  `        using (var conn = Open())`
  - → Import namespace/types.
` 491`  `        {`
` 492`  `            int cid = ScalarInt(conn,`
` 493`  `                string.Format("SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 494`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 495`  `                P("@ChID", chid));`
` 496`  `            if (cid <= 0) return new { success = false, message = "Section not found." };`
` 497`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 498`  ``
` 499`  `            // delete children lessons + mats`
` 500`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && SchemaMap.MatLinksToSub)`
` 501`  `            {`
` 502`  `                try`
  - → Error handling block.
` 503`  `                {`
` 504`  `                    Exec(conn, string.Format(`
` 505`  `                        "DELETE m FROM {0} m INNER JOIN {1} s ON s.{2}=m.{3} WHERE s.{4}=@ChID",`
` 506`  `                        Q(SchemaMap.MatTable), Q(SchemaMap.SubTable), Q(SchemaMap.SubPk), Q(SchemaMap.MatSubFk), Q(SchemaMap.SubChapterFk)),`
` 507`  `                        P("@ChID", chid));`
` 508`  `                }`
` 509`  `                catch { }`
  - → Handle/log exception.
` 510`  `                try`
  - → Error handling block.
` 511`  `                {`
` 512`  `                    Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@ChID", Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk)),`
` 513`  `                        P("@ChID", chid));`
` 514`  `                }`
` 515`  `                catch { }`
  - → Handle/log exception.
` 516`  `            }`
` 517`  `            else if (!SchemaMap.MatLinksToSub)`
` 518`  `            {`
` 519`  `                try`
  - → Error handling block.
` 520`  `                {`
` 521`  `                    Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@ChID", Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 522`  `                        P("@ChID", chid));`
` 523`  `                }`
` 524`  `                catch { }`
  - → Handle/log exception.
` 525`  `            }`
` 526`  ``
` 527`  `            Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@ChID", Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 528`  `                P("@ChID", chid));`
` 529`  `        }`
` 530`  `        return new { success = true };`
` 531`  `    }`

---

### `SaveLesson` — lines 536–690

```
private object SaveLesson(int lecturerUid, int schid, int chid, string title, string type, string content, string materialsJson)
```

#### Explanation

- **Purpose:** Implements `SaveLesson`.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `int lecturerUid, int schid, int chid, string title, string type, string content, string materialsJson`
- **Local variables:** `conn`, `cid`, `matType`, `n`, `next`, `matParent`, `storeText`, `warn`, `matsSaved`, `extra`, `updErr`

#### Line-by-line (this function)

` 536`  ``
` 537`  `    private object SaveLesson(int lecturerUid, int schid, int chid, string title, string type, string content, string materialsJson)`
` 538`  `    {`
` 539`  `        if (chid <= 0) return new { success = false, message = "Invalid section id (chid)." };`
` 540`  `        if (string.IsNullOrWhiteSpace(title)) return new { success = false, message = "Lesson title is required." };`
` 541`  ``
` 542`  `        using (var conn = Open())`
  - → Import namespace/types.
` 543`  `        {`
` 544`  `            int cid = ScalarInt(conn,`
` 545`  `                string.Format("SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 546`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 547`  `                P("@ChID", chid));`
` 548`  `            if (cid <= 0) return new { success = false, message = "Section not found (ChID=" + chid + ").", schema = SchemaMap.DebugInfo() };`
` 549`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 550`  ``
` 551`  `            string matType = NormalizeType(type);`
` 552`  `            string textContent, mediaLink;`
` 553`  `            SplitContent(matType, content, title, out textContent, out mediaLink);`
` 554`  `            if (string.IsNullOrEmpty(textContent) && string.IsNullOrEmpty(mediaLink))`
` 555`  `                textContent = title;`
` 556`  ``
` 557`  `            // ── Preferred: SubChapters (or Lessons) row per lesson ─────`
` 558`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && !string.IsNullOrEmpty(SchemaMap.SubPk))`
` 559`  `            {`
` 560`  `                int resolvedId;`
` 561`  `                if (schid > 0)`
` 562`  `                {`
` 563`  `                    int n = Exec(conn, string.Format(`
` 564`  `                        "UPDATE {0} SET {1}=@Title WHERE {2}=@SchID AND {3}=@ChID",`
` 565`  `                        Q(SchemaMap.SubTable), Q(SchemaMap.SubTitle), Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk)),`
` 566`  `                        P("@Title", title.Trim()), P("@SchID", schid), P("@ChID", chid));`
` 567`  `                    if (n <= 0) return new { success = false, message = "Lesson not found for update." };`
` 568`  `                    resolvedId = schid;`
` 569`  `                    // clear prior mats for this lesson (schema map + classic StudyMats)`
` 570`  `                    if (SchemaMap.MatLinksToSub && !string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 571`  `                    {`
` 572`  `                        try`
  - → Error handling block.
` 573`  `                        {`
` 574`  `                            Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@SchID", Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 575`  `                                P("@SchID", resolvedId));`
` 576`  `                        }`
` 577`  `                        catch { }`
  - → Handle/log exception.
` 578`  `                    }`
` 579`  `                    try { Exec(conn, "DELETE FROM StudyMats WHERE SchID=@SchID", P("@SchID", resolvedId)); } catch { }`
  - → Error handling block.
` 580`  `                    try { Exec(conn, "DELETE FROM StudyMat WHERE SchID=@SchID", P("@SchID", resolvedId)); } catch { }`
  - → Error handling block.
` 581`  `                }`
` 582`  `                else`
` 583`  `                {`
` 584`  `                    try`
  - → Error handling block.
` 585`  `                    {`
` 586`  `                        if (!string.IsNullOrEmpty(SchemaMap.SubIndex))`
` 587`  `                        {`
` 588`  `                            int next = ScalarInt(conn, string.Format(`
` 589`  `                                "SELECT ISNULL(MAX({0}),0)+1 FROM {1} WHERE {2}=@ChID",`
` 590`  `                                Q(SchemaMap.SubIndex), Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk)),`
` 591`  `                                P("@ChID", chid));`
` 592`  `                            resolvedId = ScalarInt(conn, string.Format(`
` 593`  `                                "INSERT INTO {0} ({1}, {2}, {3}) OUTPUT INSERTED.{4} VALUES (@ChID, @Idx, @Title)",`
` 594`  `                                Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubIndex), Q(SchemaMap.SubTitle), Q(SchemaMap.SubPk)),`
` 595`  `                                P("@ChID", chid), P("@Idx", next), P("@Title", title.Trim()));`
` 596`  `                        }`
` 597`  `                        else`
` 598`  `                        {`
` 599`  `                            resolvedId = ScalarInt(conn, string.Format(`
` 600`  `                                "INSERT INTO {0} ({1}, {2}) OUTPUT INSERTED.{3} VALUES (@ChID, @Title)",`
` 601`  `                                Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTitle), Q(SchemaMap.SubPk)),`
` 602`  `                                P("@ChID", chid), P("@Title", title.Trim()));`
` 603`  `                        }`
` 604`  `                    }`
` 605`  `                    catch (Exception ex)`
  - → Handle/log exception.
` 606`  `                    {`
` 607`  `                        return new`
` 608`  `                        {`
` 609`  `                            success = false,`
` 610`  `                            message = "INSERT into " + SchemaMap.SubTable + " failed: " + ex.Message,`
` 611`  `                            schema = SchemaMap.DebugInfo()`
` 612`  `                        };`
` 613`  `                    }`
` 614`  `                }`
` 615`  ``
` 616`  `                if (resolvedId <= 0)`
` 617`  `                    return new { success = false, message = "Lesson insert returned invalid id.", schema = SchemaMap.DebugInfo() };`
` 618`  ``
` 619`  `                // Attach content: prefer StudyMats keyed by lesson id; else by chapter id`
` 620`  `                int matParent = SchemaMap.MatLinksToSub ? resolvedId : chid;`
` 621`  `                // Encode title into text so content is recoverable when mats hang on chapter`
` 622`  `                string storeText = textContent;`
` 623`  `                if (!SchemaMap.MatLinksToSub)`
` 624`  `                    storeText = title.Trim() + "\n<<<BODY>>>\n" + (textContent ?? "");`
` 625`  ``
` 626`  `                // If lesson is Text but client sent file materials, promote first file`
` 627`  `                // so Course Preview always has a playable/viewable primary media path.`
` 628`  `                PromotePrimaryFromMaterials(ref matType, ref textContent, ref mediaLink, materialsJson);`
` 629`  `                storeText = textContent;`
` 630`  `                if (!SchemaMap.MatLinksToSub)`
` 631`  `                    storeText = title.Trim() + "\n<<<BODY>>>\n" + (textContent ?? "");`
` 632`  ``
` 633`  `                string warn = null;`
` 634`  `                int matsSaved = 0;`
` 635`  `                // Always attempt StudyMats (hardcoded + schema map)`
` 636`  `                warn = InsertMat(conn, matParent, matType, storeText, mediaLink, 1);`
` 637`  `                if (warn == null) matsSaved++;`
` 638`  `                int extra = InsertExtraMaterials(conn, matParent, materialsJson);`
` 639`  `                matsSaved += extra;`
` 640`  `                if (extra == 0 && !string.IsNullOrWhiteSpace(materialsJson) && materialsJson.Trim() != "[]")`
` 641`  `                {`
` 642`  `                    warn = (warn ?? "") + " Materials JSON was provided but 0 file rows were saved. Check StudyMats.MediaLink column.";`
` 643`  `                }`
` 644`  ``
` 645`  `                // Lesson row exists even if StudyMats fails — still success`
` 646`  `                return new`
` 647`  `                {`
` 648`  `                    success = true,`
` 649`  `                    schid = resolvedId,`
` 650`  `                    chid = chid,`
` 651`  `                    warning = warn,`
` 652`  `                    materialsSaved = matsSaved,`
` 653`  `                    type = matType,`
` 654`  `                    schema = SchemaMap.DebugInfo()`
` 655`  `                };`
` 656`  `            }`
` 657`  ``
` 658`  `            // ── Fallback: StudyMats only (no SubChapters table) ────────`
` 659`  `            if (!string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 660`  `            {`
` 661`  `                string storeText = title.Trim() + "\n<<<BODY>>>\n" + (textContent ?? "");`
` 662`  `                int matParent = chid; // mats on chapter`
` 663`  `                int resolvedId;`
` 664`  `                if (schid > 0)`
` 665`  `                {`
` 666`  `                    string updErr = UpdateMat(conn, schid, matType, storeText, mediaLink);`
` 667`  `                    if (updErr != null) return new { success = false, message = updErr, schema = SchemaMap.DebugInfo() };`
` 668`  `                    resolvedId = schid;`
` 669`  `                }`
` 670`  `                else`
` 671`  `                {`
` 672`  `                    string warn = InsertMat(conn, matParent, matType, storeText, mediaLink, 1);`
` 673`  `                    resolvedId = ScalarInt(conn, string.Format(`
` 674`  `                        "SELECT MAX({0}) FROM {1} WHERE {2}=@Parent",`
` 675`  `                        Q(SchemaMap.MatPk), Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 676`  `                        P("@Parent", matParent));`
` 677`  `                    if (resolvedId <= 0)`
` 678`  `                        return new { success = false, message = "StudyMats insert failed. " + warn, schema = SchemaMap.DebugInfo() };`
` 679`  `                }`
` 680`  `                return new { success = true, schid = resolvedId, chid = chid, schema = SchemaMap.DebugInfo() };`
` 681`  `            }`
` 682`  ``
` 683`  `            return new`
` 684`  `            {`
` 685`  `                success = false,`
` 686`  `                message = "Could not determine how lessons are stored. Open CurriculumApi.ashx?action=schema while logged in.",`
` 687`  `                schema = SchemaMap.DebugInfo()`
` 688`  `            };`
` 689`  `        }`
` 690`  `    }`

---

### `DeleteLesson` — lines 691–735

```
private object DeleteLesson(int lecturerUid, int schid)
```

#### Explanation

- **Purpose:** Implements `DeleteLesson`.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Delete/clear data.
- **Parameters:** `int lecturerUid, int schid`
- **Local variables:** `conn`, `chid`, `cid`

#### Line-by-line (this function)

` 691`  ``
` 692`  `    private object DeleteLesson(int lecturerUid, int schid)`
` 693`  `    {`
` 694`  `        if (schid <= 0) return new { success = false, message = "Invalid lesson id." };`
` 695`  `        using (var conn = Open())`
  - → Import namespace/types.
` 696`  `        {`
` 697`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && SchemaMap.MatLinksToSub)`
` 698`  `            {`
` 699`  `                int chid = ScalarInt(conn, string.Format(`
` 700`  `                    "SELECT {0} FROM {1} WHERE {2}=@Id",`
` 701`  `                    Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTable), Q(SchemaMap.SubPk)),`
` 702`  `                    P("@Id", schid));`
` 703`  `                int cid = ScalarInt(conn, string.Format(`
` 704`  `                    "SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 705`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 706`  `                    P("@ChID", chid));`
` 707`  `                if (cid <= 0) return new { success = false, message = "Lesson not found." };`
` 708`  `                AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 709`  `                try`
  - → Error handling block.
` 710`  `                {`
` 711`  `                    Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@Id", Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 712`  `                        P("@Id", schid));`
` 713`  `                }`
` 714`  `                catch { }`
  - → Handle/log exception.
` 715`  `                Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@Id", Q(SchemaMap.SubTable), Q(SchemaMap.SubPk)),`
` 716`  `                    P("@Id", schid));`
` 717`  `            }`
` 718`  `            else`
` 719`  `            {`
` 720`  `                // legacy mat id`
` 721`  `                int chid = ScalarInt(conn, string.Format(`
` 722`  `                    "SELECT {0} FROM {1} WHERE {2}=@Id",`
` 723`  `                    Q(SchemaMap.MatSubFk), Q(SchemaMap.MatTable), Q(SchemaMap.MatPk)),`
` 724`  `                    P("@Id", schid));`
` 725`  `                int cid = ScalarInt(conn, string.Format(`
` 726`  `                    "SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 727`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 728`  `                    P("@ChID", chid));`
` 729`  `                if (cid > 0) AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 730`  `                Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@Id", Q(SchemaMap.MatTable), Q(SchemaMap.MatPk)),`
` 731`  `                    P("@Id", schid));`
` 732`  `            }`
` 733`  `        }`
` 734`  `        return new { success = true };`
` 735`  `    }`

---

### `GetLesson` — lines 736–789

```
private object GetLesson(int lecturerUid, int schid)
```

#### Explanation

- **Purpose:** Implements `GetLesson`.
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Read/load data for display.
- **Parameters:** `int lecturerUid, int schid`
- **Local variables:** `conn`, `dt`, `chid`, `cid`, `materials`, `sql`, `type2`, `media2`, `text2`

#### Line-by-line (this function)

` 736`  ``
` 737`  `    private object GetLesson(int lecturerUid, int schid)`
` 738`  `    {`
` 739`  `        using (var conn = Open())`
  - → Import namespace/types.
` 740`  `        {`
` 741`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && SchemaMap.MatLinksToSub)`
` 742`  `            {`
` 743`  `                var dt = Query(conn, string.Format(`
` 744`  `                    "SELECT {0} AS SchID, {1} AS ChID, {2} AS Title FROM {3} WHERE {0}=@Id",`
` 745`  `                    Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTitle), Q(SchemaMap.SubTable)),`
` 746`  `                    P("@Id", schid));`
` 747`  `                if (dt.Rows.Count == 0) return new { success = false, message = "Lesson not found." };`
` 748`  `                int chid = Convert.ToInt32(dt.Rows[0]["ChID"]);`
` 749`  `                int cid = ScalarInt(conn, string.Format(`
` 750`  `                    "SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 751`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 752`  `                    P("@ChID", chid));`
` 753`  `                AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 754`  ``
` 755`  `                string type, content;`
` 756`  `                var materials = LoadMats(conn, schid, out type, out content);`
` 757`  `                return new`
` 758`  `                {`
` 759`  `                    success = true,`
` 760`  `                    schid = schid,`
` 761`  `                    chid = chid,`
` 762`  `                    title = Safe(dt.Rows[0]["Title"]),`
` 763`  `                    type = type,`
` 764`  `                    content = content,`
` 765`  `                    materials = FilterFileMaterials(materials)`
` 766`  `                };`
` 767`  `            }`
` 768`  `            else`
` 769`  `            {`
` 770`  `                string sql = BuildMatSelect() + " WHERE " + Q(SchemaMap.MatPk) + "=@Id";`
` 771`  `                var dt = Query(conn, sql, P("@Id", schid));`
` 772`  `                if (dt.Rows.Count == 0) return new { success = false, message = "Lesson not found." };`
` 773`  `                string type2 = Col(dt.Rows[0], "TypeCol");`
` 774`  `                if (string.IsNullOrEmpty(type2)) type2 = "Text";`
` 775`  `                var media2 = Col(dt.Rows[0], "MediaCol");`
` 776`  `                var text2 = Col(dt.Rows[0], "TextCol");`
` 777`  `                return new`
` 778`  `                {`
` 779`  `                    success = true,`
` 780`  `                    schid = schid,`
` 781`  `                    chid = 0,`
` 782`  `                    title = text2,`
` 783`  `                    type = type2,`
` 784`  `                    content = !string.IsNullOrEmpty(media2) ? media2 : text2,`
` 785`  `                    materials = new object[0]`
` 786`  `                };`
` 787`  `            }`
` 788`  `        }`
` 789`  `    }`

---

### `FilterFileMaterials` — lines 792–834

```
private static List<object> FilterFileMaterials(List<object> materials)
```

#### Explanation

- **Purpose:** Implements `FilterFileMaterials`.
- **Parameters:** `List<object> materials`
- **Local variables:** `list`, `d`, `media`, `smid`, `t`, `pMedia`, `pText`, `pType`, `pId`, `fn`

#### Line-by-line (this function)

` 792`  `    private static List<object> FilterFileMaterials(List<object> materials)`
` 793`  `    {`
` 794`  `        var list = new List<object>();`
` 795`  `        if (materials == null) return list;`
` 796`  `        foreach (var o in materials)`
` 797`  `        {`
` 798`  `            var d = o as Dictionary<string, object>;`
` 799`  `            string media = null, text = null, type = null;`
` 800`  `            int smid = 0;`
` 801`  `            if (d != null)`
` 802`  `            {`
` 803`  `                media = d.ContainsKey("mediaLink") ? Convert.ToString(d["mediaLink"]) : (d.ContainsKey("url") ? Convert.ToString(d["url"]) : null);`
` 804`  `                text = d.ContainsKey("fileName") ? Convert.ToString(d["fileName"]) : (d.ContainsKey("textContent") ? Convert.ToString(d["textContent"]) : null);`
` 805`  `                type = d.ContainsKey("type") ? Convert.ToString(d["type"]) : null;`
` 806`  `                if (d.ContainsKey("smid") && d["smid"] != null) try { smid = Convert.ToInt32(d["smid"]); } catch { }`
` 807`  `            }`
` 808`  `            else`
` 809`  `            {`
` 810`  `                // anonymous type fallback`
` 811`  `                var t = o.GetType();`
` 812`  `                var pMedia = t.GetProperty("mediaLink") ?? t.GetProperty("url");`
` 813`  `                var pText = t.GetProperty("fileName") ?? t.GetProperty("textContent");`
` 814`  `                var pType = t.GetProperty("type");`
` 815`  `                var pId = t.GetProperty("smid");`
` 816`  `                if (pMedia != null) media = pMedia.GetValue(o, null) as string;`
` 817`  `                if (pText != null) text = pText.GetValue(o, null) as string;`
` 818`  `                if (pType != null) type = pType.GetValue(o, null) as string;`
` 819`  `                if (pId != null && pId.GetValue(o, null) != null)`
` 820`  `                    try { smid = Convert.ToInt32(pId.GetValue(o, null)); } catch { }`
  - → Error handling block.
` 821`  `            }`
` 822`  `            if (string.IsNullOrWhiteSpace(media) || !LooksLikeFileUrl(media)) continue;`
` 823`  `            string fn = string.IsNullOrWhiteSpace(text) ? Path.GetFileName(media.Replace('\\', '/')) : text;`
` 824`  `            list.Add(new`
` 825`  `            {`
` 826`  `                smid = smid,`
` 827`  `                url = media,`
` 828`  `                mediaLink = media,`
` 829`  `                fileName = fn,`
` 830`  `                type = string.IsNullOrEmpty(type) ? GuessTypeFromUrl(media) : type`
` 831`  `            });`
` 832`  `        }`
` 833`  `        return list;`
` 834`  `    }`

---

### `LooksLikeFileUrl` — lines 835–840

```
private static bool LooksLikeFileUrl(string s)
```

#### Explanation

- **Purpose:** Implements `LooksLikeFileUrl`.
- **Parameters:** `string s`

#### Line-by-line (this function)

` 835`  ``
` 836`  `    private static bool LooksLikeFileUrl(string s)`
` 837`  `    {`
` 838`  `        // Only treat as a file URL if it is a real stored path — NOT bare "report.pdf"`
` 839`  `        return IsStoredMediaPath(s);`
` 840`  `    }`

---

### `GuessTypeFromUrl` — lines 841–849

```
private static string GuessTypeFromUrl(string url)
```

#### Explanation

- **Purpose:** Implements `GuessTypeFromUrl`.
- **Parameters:** `string url`
- **Local variables:** `low`

#### Line-by-line (this function)

` 841`  ``
` 842`  `    private static string GuessTypeFromUrl(string url)`
` 843`  `    {`
` 844`  `        var low = (url ?? "").ToLowerInvariant();`
` 845`  `        if (low.Contains(".mp4") || low.Contains(".webm") || low.Contains(".mov")) return "Video";`
` 846`  `        if (low.Contains(".png") || low.Contains(".jpg") || low.Contains(".jpeg") || low.Contains(".gif") || low.Contains(".webp")) return "Image";`
` 847`  `        if (low.Contains(".pdf")) return "PDF";`
` 848`  `        return "File";`
` 849`  `    }`

---

### `InsertMat` — lines 854–936

```
private string InsertMat(SqlConnection conn, int parentId, string type, string text, string media, int index)
```

#### Explanation

- **Purpose:** Implements `InsertMat`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Persist changes.
- **Parameters:** `SqlConnection conn, int parentId, string type, string text, string media, int index`
- **Local variables:** `errors`, `cols`, `vals`, `pars`, `sql`

#### Line-by-line (this function)

` 854`  ``
` 855`  `    private string InsertMat(SqlConnection conn, int parentId, string type, string text, string media, int index)`
  - → Database access (pure SQL).
` 856`  `    {`
` 857`  `        // Normalize media path for storage`
` 858`  `        if (!string.IsNullOrWhiteSpace(media))`
` 859`  `            media = NormalizeStoredMediaPath(media);`
` 860`  ``
` 861`  `        var errors = new List<string>();`
` 862`  ``
` 863`  `        // 1) Standard EduDB StudyMats (preferred — matches ER diagram)`
` 864`  `        string[] attempts = new[]`
` 865`  `        {`
` 866`  `            "INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink, [Index]) VALUES (@Parent, @Type, @Text, @Media, @Idx)",`
` 867`  `            "INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink) VALUES (@Parent, @Type, @Text, @Media)",`
` 868`  `            "INSERT INTO StudyMat (SchID, Type, TextContent, MediaLink, [Index]) VALUES (@Parent, @Type, @Text, @Media, @Idx)",`
` 869`  `            "INSERT INTO StudyMat (SchID, Type, TextContent, MediaLink) VALUES (@Parent, @Type, @Text, @Media)"`
` 870`  `        };`
` 871`  `        foreach (var sql in attempts)`
` 872`  `        {`
` 873`  `            try`
  - → Error handling block.
` 874`  `            {`
` 875`  `                Exec(conn, sql,`
` 876`  `                    P("@Parent", parentId),`
` 877`  `                    P("@Type", type ?? "Text"),`
` 878`  `                    P("@Text", (object)text ?? DBNull.Value),`
` 879`  `                    P("@Media", (object)media ?? DBNull.Value),`
` 880`  `                    P("@Idx", index));`
` 881`  `                return null;`
` 882`  `            }`
` 883`  `            catch (Exception ex) { errors.Add(ex.Message); }`
  - → Handle/log exception.
` 884`  `        }`
` 885`  ``
` 886`  `        // 2) SchemaMap dynamic columns`
` 887`  `        try`
  - → Error handling block.
` 888`  `        {`
` 889`  `            if (!string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 890`  `            {`
` 891`  `                var cols = new List<string>();`
` 892`  `                var vals = new List<string>();`
` 893`  `                var pars = new List<SqlParameter>();`
` 894`  ``
` 895`  `                cols.Add(Q(SchemaMap.MatSubFk));`
` 896`  `                vals.Add("@Parent");`
` 897`  `                pars.Add(P("@Parent", parentId));`
` 898`  ``
` 899`  `                if (!string.IsNullOrEmpty(SchemaMap.MatType))`
` 900`  `                {`
` 901`  `                    cols.Add(Q(SchemaMap.MatType));`
` 902`  `                    vals.Add("@Type");`
` 903`  `                    pars.Add(P("@Type", type ?? "Text"));`
` 904`  `                }`
` 905`  `                if (!string.IsNullOrEmpty(SchemaMap.MatText))`
` 906`  `                {`
` 907`  `                    cols.Add(Q(SchemaMap.MatText));`
` 908`  `                    vals.Add("@Text");`
` 909`  `                    pars.Add(P("@Text", (object)text ?? DBNull.Value));`
` 910`  `                }`
` 911`  `                if (!string.IsNullOrEmpty(SchemaMap.MatMedia))`
` 912`  `                {`
` 913`  `                    cols.Add(Q(SchemaMap.MatMedia));`
` 914`  `                    vals.Add("@Media");`
` 915`  `                    pars.Add(P("@Media", (object)media ?? DBNull.Value));`
` 916`  `                }`
` 917`  `                if (!string.IsNullOrEmpty(SchemaMap.MatIndex))`
` 918`  `                {`
` 919`  `                    cols.Add(Q(SchemaMap.MatIndex));`
` 920`  `                    vals.Add("@Idx");`
` 921`  `                    pars.Add(P("@Idx", index));`
` 922`  `                }`
` 923`  ``
` 924`  `                if (cols.Count >= 2)`
` 925`  `                {`
` 926`  `                    string sql = "INSERT INTO " + Q(SchemaMap.MatTable) + " (" + string.Join(", ", cols.ToArray()) +`
` 927`  `                                 ") VALUES (" + string.Join(", ", vals.ToArray()) + ")";`
` 928`  `                    Exec(conn, sql, pars.ToArray());`
` 929`  `                    return null;`
` 930`  `                }`
` 931`  `            }`
` 932`  `        }`
` 933`  `        catch (Exception ex) { errors.Add(ex.Message); }`
  - → Handle/log exception.
` 934`  ``
` 935`  `        return "StudyMats insert failed: " + string.Join(" | ", errors.ToArray());`
` 936`  `    }`

---

### `PromotePrimaryFromMaterials` — lines 937–970

```
private static void PromotePrimaryFromMaterials(
        ref string matType, ref string textContent, ref string mediaLink, string materialsJson)
```

#### Explanation

- **Purpose:** Implements `PromotePrimaryFromMaterials`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `ref string matType, ref string textContent, ref string mediaLink, string materialsJson`
- **Local variables:** `hasMedia`, `mats`, `m`, `url`, `fn`

#### Line-by-line (this function)

` 937`  ``
` 938`  `    private static void PromotePrimaryFromMaterials(`
` 939`  `        ref string matType, ref string textContent, ref string mediaLink, string materialsJson)`
` 940`  `    {`
` 941`  `        if (string.IsNullOrWhiteSpace(materialsJson) || materialsJson.Trim() == "[]") return;`
` 942`  `        // Only promote when primary media empty / text lesson`
` 943`  `        bool hasMedia = !string.IsNullOrWhiteSpace(mediaLink) && LooksLikeFileUrl(mediaLink);`
` 944`  `        if (hasMedia) return;`
` 945`  `        if (!string.Equals(matType, "Text", StringComparison.OrdinalIgnoreCase)`
` 946`  `            && !string.IsNullOrWhiteSpace(matType)`
` 947`  `            && !string.Equals(matType, "Quiz", StringComparison.OrdinalIgnoreCase))`
` 948`  `            return;`
` 949`  ``
` 950`  `        try`
  - → Error handling block.
` 951`  `        {`
` 952`  `            var mats = Json.Deserialize<List<Dictionary<string, object>>>(materialsJson);`
` 953`  `            if (mats == null || mats.Count == 0) return;`
` 954`  `            var m = mats[0];`
` 955`  `            string url = "";`
` 956`  `            if (m.ContainsKey("storePath")) url = Convert.ToString(m["storePath"]);`
` 957`  `            if (string.IsNullOrWhiteSpace(url) && m.ContainsKey("url")) url = Convert.ToString(m["url"]);`
` 958`  `            if (string.IsNullOrWhiteSpace(url) && m.ContainsKey("mediaLink")) url = Convert.ToString(m["mediaLink"]);`
` 959`  `            if (string.IsNullOrWhiteSpace(url)) return;`
` 960`  `            url = NormalizeStoredMediaPath(url);`
` 961`  `            string fn = m.ContainsKey("fileName") ? Convert.ToString(m["fileName"]) : Path.GetFileName(url.Replace('\\', '/'));`
` 962`  `            matType = GuessTypeFromUrl(url + " " + fn);`
` 963`  `            if (matType == "File") matType = "PDF";`
` 964`  `            mediaLink = url;`
` 965`  `            // Keep short text label as title-ish; don't overwrite rich HTML body if long`
` 966`  `            if (string.IsNullOrWhiteSpace(textContent) || textContent.Trim().Length < 40)`
` 967`  `                textContent = fn;`
` 968`  `        }`
` 969`  `        catch { }`
  - → Handle/log exception.
` 970`  `    }`

---

### `UpdateMat` — lines 971–1004

```
private string UpdateMat(SqlConnection conn, int id, string type, string text, string media)
```

#### Explanation

- **Purpose:** Implements `UpdateMat`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Pattern:** Persist changes.
- **Parameters:** `SqlConnection conn, int id, string type, string text, string media`
- **Local variables:** `sets`, `pars`, `sql`

#### Line-by-line (this function)

` 971`  ``
` 972`  `    private string UpdateMat(SqlConnection conn, int id, string type, string text, string media)`
  - → Database access (pure SQL).
` 973`  `    {`
` 974`  `        try`
  - → Error handling block.
` 975`  `        {`
` 976`  `            var sets = new List<string>();`
` 977`  `            var pars = new List<SqlParameter>();`
` 978`  `            if (!string.IsNullOrEmpty(SchemaMap.MatType))`
` 979`  `            {`
` 980`  `                sets.Add(Q(SchemaMap.MatType) + "=@Type");`
` 981`  `                pars.Add(P("@Type", type ?? "Text"));`
` 982`  `            }`
` 983`  `            if (!string.IsNullOrEmpty(SchemaMap.MatText))`
` 984`  `            {`
` 985`  `                sets.Add(Q(SchemaMap.MatText) + "=@Text");`
` 986`  `                pars.Add(P("@Text", (object)text ?? DBNull.Value));`
` 987`  `            }`
` 988`  `            if (!string.IsNullOrEmpty(SchemaMap.MatMedia))`
` 989`  `            {`
` 990`  `                sets.Add(Q(SchemaMap.MatMedia) + "=@Media");`
` 991`  `                pars.Add(P("@Media", (object)media ?? DBNull.Value));`
` 992`  `            }`
` 993`  `            if (sets.Count == 0) return "No updatable StudyMats columns.";`
` 994`  `            pars.Add(P("@Id", id));`
` 995`  `            string sql = "UPDATE " + Q(SchemaMap.MatTable) + " SET " + string.Join(", ", sets.ToArray()) +`
` 996`  `                         " WHERE " + Q(SchemaMap.MatPk) + "=@Id";`
` 997`  `            Exec(conn, sql, pars.ToArray());`
` 998`  `            return null;`
` 999`  `        }`
`1000`  `        catch (Exception ex)`
  - → Handle/log exception.
`1001`  `        {`
`1002`  `            return "Update StudyMats failed: " + ex.Message;`
`1003`  `        }`
`1004`  `    }`

---

### `InsertExtraMaterials` — lines 1007–1052

```
private int InsertExtraMaterials(SqlConnection conn, int parentId, string materialsJson)
```

#### Explanation

- **Purpose:** Implements `InsertExtraMaterials`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Persist changes.
- **Parameters:** `SqlConnection conn, int parentId, string materialsJson`
- **Local variables:** `mats`, `i`, `saved`, `url`, `fn`, `t`, `low`, `warn`

#### Line-by-line (this function)

`1007`  `    private int InsertExtraMaterials(SqlConnection conn, int parentId, string materialsJson)`
  - → Database access (pure SQL).
`1008`  `    {`
`1009`  `        if (string.IsNullOrWhiteSpace(materialsJson) || materialsJson.Trim() == "[]") return 0;`
`1010`  `        var mats = Json.Deserialize<List<Dictionary<string, object>>>(materialsJson);`
`1011`  `        if (mats == null) return 0;`
`1012`  `        int i = 1;`
`1013`  `        int saved = 0;`
`1014`  `        foreach (var m in mats)`
`1015`  `        {`
`1016`  `            i++;`
`1017`  `            // Prefer storePath / under (GUID paths) — NEVER bare fileName as MediaLink`
`1018`  `            string url = "";`
`1019`  `            if (m.ContainsKey("storePath") && m["storePath"] != null) url = Convert.ToString(m["storePath"]);`
`1020`  `            if (string.IsNullOrWhiteSpace(url) && m.ContainsKey("under")) url = Convert.ToString(m["under"]);`
`1021`  `            if (string.IsNullOrWhiteSpace(url) && m.ContainsKey("url")) url = Convert.ToString(m["url"]);`
`1022`  `            if (string.IsNullOrWhiteSpace(url) && m.ContainsKey("mediaLink")) url = Convert.ToString(m["mediaLink"]);`
`1023`  `            if (string.IsNullOrWhiteSpace(url) && m.ContainsKey("serveUrl")) url = Convert.ToString(m["serveUrl"]);`
`1024`  ``
`1025`  `            string fn = m.ContainsKey("fileName") ? Convert.ToString(m["fileName"]) : null;`
`1026`  `            if (string.IsNullOrWhiteSpace(fn)) fn = Path.GetFileName((url ?? "").Replace('\\', '/'));`
`1027`  `            if (string.IsNullOrWhiteSpace(url)) continue;`
`1028`  ``
`1029`  `            // Normalize → Uploads/CourseMaterials/{guid}.ext  (rejects bare original names)`
`1030`  `            url = NormalizeStoredMediaPath(url);`
`1031`  `            if (string.IsNullOrWhiteSpace(url) || !IsStoredMediaPath(url))`
`1032`  `            {`
`1033`  `                System.Diagnostics.Debug.WriteLine("Skip material without GUID store path. fileName=" + fn + " raw url rejected.");`
`1034`  `                continue;`
`1035`  `            }`
`1036`  ``
`1037`  `            string t = GuessTypeFromUrl(url + " " + fn);`
`1038`  `            if (t == "File")`
`1039`  `            {`
`1040`  `                var low = (url + " " + fn).ToLowerInvariant();`
`1041`  `                if (low.Contains(".docx") || low.Contains(".doc") || low.Contains(".pptx") || low.Contains(".ppt"))`
`1042`  `                    t = "File";`
`1043`  `                else`
`1044`  `                    t = "PDF";`
`1045`  `            }`
`1046`  ``
`1047`  `            string warn = InsertMat(conn, parentId, t, fn, url, i);`
`1048`  `            if (warn == null) saved++;`
`1049`  `            else System.Diagnostics.Debug.WriteLine("InsertExtraMaterials failed: " + warn);`
`1050`  `        }`
`1051`  `        return saved;`
`1052`  `    }`

---

### `IsStoredMediaPath` — lines 1057–1080

```
private static bool IsStoredMediaPath(string s)
```

#### Explanation

- **Purpose:** Implements `IsStoredMediaPath`.
- **Parameters:** `string s`
- **Local variables:** `name`, `hex`

#### Line-by-line (this function)

`1057`  `    private static bool IsStoredMediaPath(string s)`
`1058`  `    {`
`1059`  `        if (string.IsNullOrWhiteSpace(s)) return false;`
`1060`  `        s = s.Trim().Replace('\\', '/');`
`1061`  `        if (s.IndexOf("Media.ashx", StringComparison.OrdinalIgnoreCase) >= 0) return true;`
`1062`  `        if (s.IndexOf("ServeUpload", StringComparison.OrdinalIgnoreCase) >= 0) return true;`
`1063`  `        if (s.IndexOf("Uploads/", StringComparison.OrdinalIgnoreCase) >= 0) return true;`
`1064`  `        if (s.StartsWith("CourseMaterials/", StringComparison.OrdinalIgnoreCase) ||`
`1065`  `            s.StartsWith("CourseVideos/", StringComparison.OrdinalIgnoreCase) ||`
`1066`  `            s.StartsWith("CourseThumbnails/", StringComparison.OrdinalIgnoreCase))`
`1067`  `            return true;`
`1068`  `        // GUID-like file name (32 hex chars)`
`1069`  `        string name = Path.GetFileNameWithoutExtension(s);`
`1070`  `        if (!string.IsNullOrEmpty(name) && name.Length == 32)`
`1071`  `        {`
`1072`  `            foreach (char c in name)`
`1073`  `            {`
`1074`  `                bool hex = (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f') || (c >= 'A' && c <= 'F');`
`1075`  `                if (!hex) return false;`
`1076`  `            }`
`1077`  `            return true;`
`1078`  `        }`
`1079`  `        return false;`
`1080`  `    }`

---

### `NormalizeStoredMediaPath` — lines 1083–1137

```
private static string NormalizeStoredMediaPath(string url)
```

#### Explanation

- **Purpose:** Implements `NormalizeStoredMediaPath`.
- **Parameters:** `string url`
- **Local variables:** `uri`, `sp`, `rest`, `eq`, `amp`, `up`

#### Line-by-line (this function)

`1083`  `    private static string NormalizeStoredMediaPath(string url)`
`1084`  `    {`
`1085`  `        if (string.IsNullOrWhiteSpace(url)) return url;`
`1086`  `        url = url.Trim().Replace('\\', '/');`
`1087`  `        try`
  - → Error handling block.
`1088`  `        {`
`1089`  `            if (url.StartsWith("http://", StringComparison.OrdinalIgnoreCase) ||`
`1090`  `                url.StartsWith("https://", StringComparison.OrdinalIgnoreCase))`
`1091`  `            {`
`1092`  `                var uri = new Uri(url);`
`1093`  `                // Keep query for Media.ashx?f=`
`1094`  `                if (uri.AbsolutePath.IndexOf("Media.ashx", StringComparison.OrdinalIgnoreCase) >= 0 ||`
`1095`  `                    uri.AbsolutePath.IndexOf("ServeUpload", StringComparison.OrdinalIgnoreCase) >= 0)`
`1096`  `                    url = uri.PathAndQuery;`
`1097`  `                else`
`1098`  `                    url = uri.AbsolutePath;`
`1099`  `            }`
`1100`  `        }`
`1101`  `        catch { }`
  - → Handle/log exception.
`1102`  ``
`1103`  `        // Media.ashx?f=CourseMaterials/guid.pdf  OR  ServeUpload.ashx?path=...`
`1104`  `        if (url.IndexOf("Media.ashx", StringComparison.OrdinalIgnoreCase) >= 0 ||`
`1105`  `            url.IndexOf("ServeUpload", StringComparison.OrdinalIgnoreCase) >= 0)`
`1106`  `        {`
`1107`  `            int sp = url.IndexOf("f=", StringComparison.OrdinalIgnoreCase);`
`1108`  `            if (sp < 0) sp = url.IndexOf("path=", StringComparison.OrdinalIgnoreCase);`
`1109`  `            if (sp >= 0)`
`1110`  `            {`
`1111`  `                string rest = url.Substring(sp);`
`1112`  `                int eq = rest.IndexOf('=');`
`1113`  `                rest = eq >= 0 ? rest.Substring(eq + 1) : rest;`
`1114`  `                int amp = rest.IndexOf('&');`
`1115`  `                if (amp >= 0) rest = rest.Substring(0, amp);`
`1116`  `                try { rest = HttpUtility.UrlDecode(rest); } catch { }`
  - → Error handling block.
`1117`  `                rest = rest.TrimStart('/');`
`1118`  `                if (rest.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))`
`1119`  `                    return rest;`
`1120`  `                return "Uploads/" + rest;`
`1121`  `            }`
`1122`  `        }`
`1123`  ``
`1124`  `        int up = url.IndexOf("/Uploads/", StringComparison.OrdinalIgnoreCase);`
`1125`  `        if (up >= 0) return url.Substring(up + 1);`
`1126`  `        if (url.StartsWith("~/")) url = url.Substring(2);`
`1127`  `        url = url.TrimStart('/');`
`1128`  `        if (url.StartsWith("CourseMaterials/", StringComparison.OrdinalIgnoreCase) ||`
`1129`  `            url.StartsWith("CourseVideos/", StringComparison.OrdinalIgnoreCase) ||`
`1130`  `            url.StartsWith("CourseThumbnails/", StringComparison.OrdinalIgnoreCase))`
`1131`  `            return "Uploads/" + url;`
`1132`  ``
`1133`  `        // Bare original filename is NOT a valid store path — return empty so callers skip it`
`1134`  `        if (!IsStoredMediaPath(url))`
`1135`  `            return "";`
`1136`  `        return url;`
`1137`  `    }`

---

### `NormalizeType` — lines 1138–1150

```
private static string NormalizeType(string type)
```

#### Explanation

- **Purpose:** Implements `NormalizeType`.
- **Parameters:** `string type`

#### Line-by-line (this function)

`1138`  ``
`1139`  `    private static string NormalizeType(string type)`
`1140`  `    {`
`1141`  `        if (string.IsNullOrWhiteSpace(type)) return "Text";`
`1142`  `        type = type.Trim();`
`1143`  `        if (string.Equals(type, "Quiz", StringComparison.OrdinalIgnoreCase)) return "Text";`
`1144`  `        // Preserve media types for StudyMats + Course Preview`
`1145`  `        if (string.Equals(type, "Video", StringComparison.OrdinalIgnoreCase)) return "Video";`
`1146`  `        if (string.Equals(type, "PDF", StringComparison.OrdinalIgnoreCase)) return "PDF";`
`1147`  `        if (string.Equals(type, "Image", StringComparison.OrdinalIgnoreCase)) return "Image";`
`1148`  `        if (string.Equals(type, "File", StringComparison.OrdinalIgnoreCase)) return "File";`
`1149`  `        return type;`
`1150`  `    }`

---

### `SplitContent` — lines 1151–1176

```
private static void SplitContent(string matType, string content, string title, out string text, out string media)
```

#### Explanation

- **Purpose:** Implements `SplitContent`.
- **Parameters:** `string matType, string content, string title, out string text, out string media`

#### Line-by-line (this function)

`1151`  ``
`1152`  `    private static void SplitContent(string matType, string content, string title, out string text, out string media)`
`1153`  `    {`
`1154`  `        text = null;`
`1155`  `        media = null;`
`1156`  `        // If content itself is a file path, treat as media even for "Text"`
`1157`  `        if (LooksLikeFileUrl(content))`
`1158`  `        {`
`1159`  `            media = NormalizeStoredMediaPath(content);`
`1160`  `            text = title;`
`1161`  `            return;`
`1162`  `        }`
`1163`  `        if (string.Equals(matType, "Video", StringComparison.OrdinalIgnoreCase) ||`
`1164`  `            string.Equals(matType, "Image", StringComparison.OrdinalIgnoreCase) ||`
`1165`  `            string.Equals(matType, "PDF", StringComparison.OrdinalIgnoreCase) ||`
`1166`  `            string.Equals(matType, "File", StringComparison.OrdinalIgnoreCase))`
`1167`  `        {`
`1168`  `            media = content ?? "";`
`1169`  `            if (!string.IsNullOrEmpty(media)) media = NormalizeStoredMediaPath(media);`
`1170`  `            text = title; // keep title as text label`
`1171`  `        }`
`1172`  `        else`
`1173`  `        {`
`1174`  `            text = string.IsNullOrWhiteSpace(content) ? title : content;`
`1175`  `        }`
`1176`  `    }`

---

### `Q` — lines 1181–1182

```
private static string Q(string ident)
```

#### Explanation

- **Purpose:** Implements `Q`.
- **Parameters:** `string ident`

#### Line-by-line (this function)

`1181`  ``
`1182`  `    private static string Q(string ident) { return SchemaMap.Q(ident); }`

---

### `AssertOwner` — lines 1183–1189

```
private static void AssertOwner(SqlConnection conn, int lecturerUid, int cid)
```

#### Explanation

- **Purpose:** Implements `AssertOwner`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Parameters:** `SqlConnection conn, int lecturerUid, int cid`
- **Local variables:** `owner`

#### Line-by-line (this function)

`1183`  ``
`1184`  `    private static void AssertOwner(SqlConnection conn, int lecturerUid, int cid)`
  - → Database access (pure SQL).
`1185`  `    {`
`1186`  `        int owner = ScalarInt(conn, "SELECT LecturerUID FROM Courses WHERE CID=@CID", P("@CID", cid));`
  - → Owner lecturer foreign key.
`1187`  `        if (owner != lecturerUid)`
`1188`  `            throw new UnauthorizedAccessException("Course not found or access denied (CID=" + cid + ").");`
`1189`  `    }`

---

### `Open` — lines 1195–1201

```
private static SqlConnection Open()
```

#### Explanation

- **Purpose:** Implements `Open`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Local variables:** `c`

#### Line-by-line (this function)

`1195`  ``
`1196`  `    private static SqlConnection Open()`
  - → Database access (pure SQL).
`1197`  `    {`
`1198`  `        var c = new SqlConnection(ConnStr);`
  - → Database access (pure SQL).
`1199`  `        c.Open();`
`1200`  `        return c;`
`1201`  `    }`

---

### `P` — lines 1202–1206

```
private static SqlParameter P(string n, object v)
```

#### Explanation

- **Purpose:** Implements `P`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string n, object v`

#### Line-by-line (this function)

`1202`  ``
`1203`  `    private static SqlParameter P(string n, object v)`
`1204`  `    {`
`1205`  `        return new SqlParameter(n, v ?? DBNull.Value);`
`1206`  `    }`

---

### `Query` — lines 1207–1220

```
private static DataTable Query(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `Query`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string sql, params SqlParameter[] ps`
- **Local variables:** `cmd`, `da`, `dt`

#### Line-by-line (this function)

`1207`  ``
`1208`  `    private static DataTable Query(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
`1209`  `    {`
`1210`  `        using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`1211`  `        {`
`1212`  `            if (ps != null) cmd.Parameters.AddRange(ps);`
`1213`  `            using (var da = new SqlDataAdapter(cmd))`
  - → Import namespace/types.
`1214`  `            {`
`1215`  `                var dt = new DataTable();`
`1216`  `                da.Fill(dt);`
`1217`  `                return dt;`
`1218`  `            }`
`1219`  `        }`
`1220`  `    }`

---

### `Exec` — lines 1221–1229

```
private static int Exec(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `Exec`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string sql, params SqlParameter[] ps`
- **Local variables:** `cmd`

#### Line-by-line (this function)

`1221`  ``
`1222`  `    private static int Exec(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
`1223`  `    {`
`1224`  `        using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`1225`  `        {`
`1226`  `            if (ps != null) cmd.Parameters.AddRange(ps);`
`1227`  `            return cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`1228`  `        }`
`1229`  `    }`

---

### `ScalarInt` — lines 1230–1240

```
private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)
```

#### Explanation

- **Purpose:** Implements `ScalarInt`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `SqlConnection conn, string sql, params SqlParameter[] ps`
- **Local variables:** `cmd`, `o`

#### Line-by-line (this function)

`1230`  ``
`1231`  `    private static int ScalarInt(SqlConnection conn, string sql, params SqlParameter[] ps)`
  - → Database access (pure SQL).
`1232`  `    {`
`1233`  `        using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`1234`  `        {`
`1235`  `            if (ps != null) cmd.Parameters.AddRange(ps);`
`1236`  `            var o = cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`1237`  `            if (o == null || o == DBNull.Value) return 0;`
`1238`  `            return Convert.ToInt32(o);`
`1239`  `        }`
`1240`  `    }`

---

### `Safe` — lines 1241–1246

```
private static string Safe(object o)
```

#### Explanation

- **Purpose:** Implements `Safe`.
- **Parameters:** `object o`

#### Line-by-line (this function)

`1241`  ``
`1242`  `    private static string Safe(object o)`
`1243`  `    {`
`1244`  `        if (o == null || o == DBNull.Value) return "";`
`1245`  `        return o.ToString();`
`1246`  `    }`

---

### `Col` — lines 1247–1257

```
private static string Col(DataRow r, params string[] names)
```

#### Explanation

- **Purpose:** Implements `Col`.
- **Parameters:** `DataRow r, params string[] names`

#### Line-by-line (this function)

`1247`  ``
`1248`  `    private static string Col(DataRow r, params string[] names)`
`1249`  `    {`
`1250`  `        foreach (var n in names)`
`1251`  `        {`
`1252`  `            if (string.IsNullOrEmpty(n)) continue;`
`1253`  `            if (r.Table.Columns.Contains(n) && r[n] != DBNull.Value)`
`1254`  `                return r[n].ToString();`
`1255`  `        }`
`1256`  `        return "";`
`1257`  `    }`

---

### `GetInt` — lines 1258–1269

```
private static int GetInt(Dictionary<string, object> data, HttpContext ctx, string key)
```

#### Explanation

- **Purpose:** Implements `GetInt`.
- **Pattern:** Read/load data for display.
- **Parameters:** `Dictionary<string, object> data, HttpContext ctx, string key`

#### Line-by-line (this function)

`1258`  ``
`1259`  `    private static int GetInt(Dictionary<string, object> data, HttpContext ctx, string key)`
`1260`  `    {`
`1261`  `        if (data != null && data.ContainsKey(key) && data[key] != null)`
`1262`  `        {`
`1263`  `            int v;`
`1264`  `            if (int.TryParse(Convert.ToString(data[key]), out v)) return v;`
`1265`  `        }`
`1266`  `        int q;`
`1267`  `        if (int.TryParse(ctx.Request[key], out q)) return q;`
`1268`  `        return 0;`
`1269`  `    }`

---

### `GetStr` — lines 1270–1276

```
private static string GetStr(Dictionary<string, object> data, HttpContext ctx, string key)
```

#### Explanation

- **Purpose:** Implements `GetStr`.
- **Pattern:** Read/load data for display.
- **Parameters:** `Dictionary<string, object> data, HttpContext ctx, string key`

#### Line-by-line (this function)

`1270`  ``
`1271`  `    private static string GetStr(Dictionary<string, object> data, HttpContext ctx, string key)`
`1272`  `    {`
`1273`  `        if (data != null && data.ContainsKey(key) && data[key] != null)`
`1274`  `            return Convert.ToString(data[key]);`
`1275`  `        return ctx.Request[key] ?? "";`
`1276`  `    }`

---

### `Write` — lines 1277–1281

```
private static void Write(HttpContext ctx, object obj)
```

#### Explanation

- **Purpose:** Implements `Write`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `HttpContext ctx, object obj`

#### Line-by-line (this function)

`1277`  ``
`1278`  `    private static void Write(HttpContext ctx, object obj)`
`1279`  `    {`
`1280`  `        ctx.Response.Write(Json.Serialize(obj));`
`1281`  `    }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `<%@ WebHandler Language="C#" Class="CurriculumApi" %>`
`   2`  ``
`   3`  `using System;`
  - → Import namespace/types.
`   4`  `using System.Collections.Generic;`
  - → Import namespace/types.
`   5`  `using System.Configuration;`
  - → Import namespace/types.
`   6`  `using System.Data;`
  - → Import namespace/types.
`   7`  `using System.Data.SqlClient;`
  - → Import namespace/types.
`   8`  `using System.IO;`
  - → Import namespace/types.
`   9`  `using System.Web;`
  - → Import namespace/types.
`  10`  `using System.Web.Script.Serialization;`
  - → Import namespace/types.
`  11`  `using System.Web.SessionState;`
  - → Import namespace/types.
`  12`  `using WebAppAssignment.Data;`
  - → Import namespace/types.
`  13`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`  14`  ``
`  15`  `/// <summary>`
`  16`  `/// Pure-SQL curriculum API. Uses SchemaMap to match live EduDB column names.`
`  17`  `/// Lecturer/Admin only.`
`  18`  `/// </summary>`
`  19`  `public class CurriculumApi : IHttpHandler, IRequiresSessionState`
  - → Class declaration for this page/service.
`  20`  `{`
`  21`  `    private static readonly JavaScriptSerializer Json = new JavaScriptSerializer { MaxJsonLength = int.MaxValue };`
`  22`  ``
`  23`  `    public void ProcessRequest(HttpContext context)`
  - → IHttpHandler entry for ashx.
`  24`  `    {`
`  25`  `        context.Response.ContentType = "application/json; charset=utf-8";`
`  26`  `        context.Response.Cache.SetCacheability(HttpCacheability.NoCache);`
`  27`  ``
`  28`  `        try`
  - → Error handling block.
`  29`  `        {`
`  30`  `            int uid = AuthGate.RequireLecturer(context);`
  - → Authorization — block wrong role / anonymous.
`  31`  `            if (uid <= 0)`
`  32`  `            {`
`  33`  `                Write(context, AuthGate.NotAuthenticatedJson("Lecturer sign-in required."));`
  - → Authorization — block wrong role / anonymous.
`  34`  `                return;`
`  35`  `            }`
`  36`  ``
`  37`  `            SchemaMap.Ensure();`
`  38`  ``
`  39`  `            string action = (context.Request["action"] ?? "").Trim().ToLowerInvariant();`
`  40`  `            string body = null;`
`  41`  `            if (context.Request.HttpMethod == "POST" &&`
`  42`  `                (context.Request.ContentType ?? "").IndexOf("json", StringComparison.OrdinalIgnoreCase) >= 0)`
`  43`  `            {`
`  44`  `                using (var reader = new StreamReader(context.Request.InputStream))`
  - → Import namespace/types.
`  45`  `                    body = reader.ReadToEnd();`
`  46`  `            }`
`  47`  ``
`  48`  `            Dictionary<string, object> data = null;`
`  49`  `            if (!string.IsNullOrWhiteSpace(body))`
`  50`  `            {`
`  51`  `                try { data = Json.Deserialize<Dictionary<string, object>>(body); } catch { data = null; }`
  - → Error handling block.
`  52`  `                if (data != null && data.ContainsKey("action") && string.IsNullOrEmpty(action))`
`  53`  `                    action = Convert.ToString(data["action"]).ToLowerInvariant();`
`  54`  `            }`
`  55`  ``
`  56`  `            switch (action)`
`  57`  `            {`
`  58`  `                case "schema":`
`  59`  `                    Write(context, new { success = true, schema = SchemaMap.DebugInfo() });`
`  60`  `                    break;`
`  61`  `                case "get":`
`  62`  `                    Write(context, GetCurriculum(uid, GetInt(data, context, "cid")));`
`  63`  `                    break;`
`  64`  `                case "save_section":`
`  65`  `                    Write(context, SaveSection(uid, GetInt(data, context, "chid"), GetInt(data, context, "cid"), GetStr(data, context, "title")));`
`  66`  `                    break;`
`  67`  `                case "delete_section":`
`  68`  `                    Write(context, DeleteSection(uid, GetInt(data, context, "chid")));`
`  69`  `                    break;`
`  70`  `                case "save_lesson":`
`  71`  `                    Write(context, SaveLesson(uid,`
`  72`  `                        GetInt(data, context, "schid"),`
`  73`  `                        GetInt(data, context, "chid"),`
`  74`  `                        GetStr(data, context, "title"),`
`  75`  `                        GetStr(data, context, "type"),`
`  76`  `                        GetStr(data, context, "content"),`
`  77`  `                        GetStr(data, context, "materialsJson")));`
`  78`  `                    break;`
`  79`  `                case "delete_lesson":`
`  80`  `                    Write(context, DeleteLesson(uid, GetInt(data, context, "schid")));`
`  81`  `                    break;`
`  82`  `                case "get_lesson":`
`  83`  `                    Write(context, GetLesson(uid, GetInt(data, context, "schid")));`
`  84`  `                    break;`
`  85`  `                default:`
`  86`  `                    Write(context, new { success = false, message = "Unknown action: " + action, schema = SchemaMap.DebugInfo() });`
`  87`  `                    break;`
`  88`  `            }`
`  89`  `        }`
`  90`  `        catch (Exception ex)`
  - → Handle/log exception.
`  91`  `        {`
`  92`  `            Write(context, new { success = false, message = ex.Message, detail = ex.ToString(), schema = SchemaMap.DebugInfo() });`
`  93`  `        }`
`  94`  `    }`
`  95`  ``
`  96`  `    // ═══════════════════════════════════════════════════════════════════════`
`  97`  `    // GET curriculum`
`  98`  `    // ═══════════════════════════════════════════════════════════════════════`
`  99`  ``
` 100`  `    private object GetCurriculum(int lecturerUid, int cid)`
` 101`  `    {`
` 102`  `        if (cid <= 0) return new { success = false, message = "Invalid course id." };`
` 103`  ``
` 104`  `        var chapters = new List<object>();`
` 105`  `        using (var conn = Open())`
  - → Import namespace/types.
` 106`  `        {`
` 107`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 108`  ``
` 109`  `            string chSql;`
` 110`  `            if (!string.IsNullOrEmpty(SchemaMap.ChIndex))`
` 111`  `            {`
` 112`  `                chSql = string.Format(`
` 113`  `                    "SELECT {0} AS ChID, {1} AS CID, {2} AS Idx, {3} AS Title FROM {4} WHERE {1}=@CID ORDER BY {2}, {0}",`
` 114`  `                    Q(SchemaMap.ChPk), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChIndex), Q(SchemaMap.ChTitle), Q(SchemaMap.ChTable));`
` 115`  `            }`
` 116`  `            else`
` 117`  `            {`
` 118`  `                chSql = string.Format(`
` 119`  `                    "SELECT {0} AS ChID, {1} AS CID, {2} AS Title FROM {3} WHERE {1}=@CID ORDER BY {0}",`
` 120`  `                    Q(SchemaMap.ChPk), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTitle), Q(SchemaMap.ChTable));`
` 121`  `            }`
` 122`  ``
` 123`  `            DataTable chDt = Query(conn, chSql, P("@CID", cid));`
` 124`  ``
` 125`  `            foreach (DataRow ch in chDt.Rows)`
` 126`  `            {`
` 127`  `                int chid = Convert.ToInt32(ch["ChID"]);`
` 128`  `                var lessons = new List<object>();`
` 129`  ``
` 130`  `                // Preferred: SubChapters/Lessons table holds one row per lesson`
` 131`  `                if (!string.IsNullOrEmpty(SchemaMap.SubTable) && !string.IsNullOrEmpty(SchemaMap.SubPk))`
` 132`  `                {`
` 133`  `                    string scSql;`
` 134`  `                    if (!string.IsNullOrEmpty(SchemaMap.SubIndex))`
` 135`  `                    {`
` 136`  `                        scSql = string.Format(`
` 137`  `                            "SELECT {0} AS SchID, {1} AS ChID, {2} AS Idx, {3} AS Title FROM {4} WHERE {1}=@ChID ORDER BY {2}, {0}",`
` 138`  `                            Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubIndex), Q(SchemaMap.SubTitle), Q(SchemaMap.SubTable));`
` 139`  `                    }`
` 140`  `                    else`
` 141`  `                    {`
` 142`  `                        scSql = string.Format(`
` 143`  `                            "SELECT {0} AS SchID, {1} AS ChID, {2} AS Title FROM {3} WHERE {1}=@ChID ORDER BY {0}",`
` 144`  `                            Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTitle), Q(SchemaMap.SubTable));`
` 145`  `                    }`
` 146`  ``
` 147`  `                    DataTable scDt;`
` 148`  `                    try`
  - → Error handling block.
` 149`  `                    {`
` 150`  `                        scDt = Query(conn, scSql, P("@ChID", chid));`
` 151`  `                    }`
` 152`  `                    catch (Exception ex)`
  - → Handle/log exception.
` 153`  `                    {`
` 154`  `                        return new`
` 155`  `                        {`
` 156`  `                            success = false,`
` 157`  `                            message = "Sub-lessons query failed: " + ex.Message,`
` 158`  `                            schema = SchemaMap.DebugInfo(),`
` 159`  `                            sql = scSql`
` 160`  `                        };`
` 161`  `                    }`
` 162`  ``
` 163`  `                    foreach (DataRow sc in scDt.Rows)`
` 164`  `                    {`
` 165`  `                        int schid = Convert.ToInt32(sc["SchID"]);`
` 166`  `                        string type, content;`
` 167`  `                        // mats may hang on lesson id OR chapter id depending on schema`
` 168`  `                        var materials = SchemaMap.MatLinksToSub`
` 169`  `                            ? LoadMats(conn, schid, out type, out content)`
` 170`  `                            : LoadMats(conn, chid, out type, out content);`
` 171`  ``
` 172`  `                        // If mats hang on chapter, try to pick body for this lesson title`
` 173`  `                        if (!SchemaMap.MatLinksToSub && !string.IsNullOrEmpty(content) && content.Contains("<<<BODY>>>"))`
` 174`  `                        {`
` 175`  `                            // content may be for a different lesson; re-scan mats`
` 176`  `                            try`
  - → Error handling block.
` 177`  `                            {`
` 178`  `                                string matSql = BuildMatSelect() + " WHERE " + Q(SchemaMap.MatSubFk) + "=@Key ORDER BY " + Q(SchemaMap.MatPk);`
` 179`  `                                var mats = Query(conn, matSql, P("@Key", chid));`
` 180`  `                                string lessonTitle = Safe(sc["Title"]);`
` 181`  `                                type = "Text";`
` 182`  `                                content = "";`
` 183`  `                                materials = new List<object>();`
` 184`  `                                foreach (DataRow m in mats.Rows)`
` 185`  `                                {`
` 186`  `                                    var text = Col(m, "TextCol");`
` 187`  `                                    var media = Col(m, "MediaCol");`
` 188`  `                                    var t = Col(m, "TypeCol");`
` 189`  `                                    if (!string.IsNullOrEmpty(text) && text.StartsWith(lessonTitle + "\n<<<BODY>>>", StringComparison.Ordinal))`
` 190`  `                                    {`
` 191`  `                                        type = string.IsNullOrEmpty(t) ? "Text" : t;`
` 192`  `                                        content = text.Substring((lessonTitle + "\n<<<BODY>>>\n").Length);`
` 193`  `                                        if (!string.IsNullOrEmpty(media)) content = media;`
` 194`  `                                    }`
` 195`  `                                    else if (!string.IsNullOrEmpty(text) && text == lessonTitle)`
` 196`  `                                    {`
` 197`  `                                        type = string.IsNullOrEmpty(t) ? "Text" : t;`
` 198`  `                                        content = media ?? "";`
` 199`  `                                    }`
` 200`  `                                    int smid = 0;`
` 201`  `                                    try { smid = Convert.ToInt32(m["SMID"]); } catch { }`
  - → Error handling block.
` 202`  `                                    materials.Add(new { smid = smid, type = t, textContent = text, mediaLink = media, url = media, fileName = text });`
` 203`  `                                }`
` 204`  `                            }`
` 205`  `                            catch { }`
  - → Handle/log exception.
` 206`  `                        }`
` 207`  ``
` 208`  `                        lessons.Add(new`
` 209`  `                        {`
` 210`  `                            schid = schid,`
` 211`  `                            title = Safe(sc["Title"]),`
` 212`  `                            type = type,`
` 213`  `                            content = content,`
` 214`  `                            materials = materials`
` 215`  `                        });`
` 216`  `                    }`
` 217`  `                }`
` 218`  `                else if (!string.IsNullOrEmpty(SchemaMap.MatTable))`
` 219`  `                {`
` 220`  `                    // Fallback: each StudyMat row is a lesson under the chapter`
` 221`  `                    try`
  - → Error handling block.
` 222`  `                    {`
` 223`  `                        string matSql = BuildMatSelect() + " WHERE " + Q(SchemaMap.MatSubFk) + "=@Key ORDER BY " + Q(SchemaMap.MatPk);`
` 224`  `                        var mats = Query(conn, matSql, P("@Key", chid));`
` 225`  `                        int i = 0;`
` 226`  `                        foreach (DataRow m in mats.Rows)`
` 227`  `                        {`
` 228`  `                            i++;`
` 229`  `                            string type = Col(m, "TypeCol");`
` 230`  `                            if (string.IsNullOrEmpty(type)) type = "Text";`
` 231`  `                            var media = Col(m, "MediaCol");`
` 232`  `                            var text = Col(m, "TextCol");`
` 233`  `                            string content = text ?? "";`
` 234`  `                            string lessonTitle = "Lesson " + i;`
` 235`  `                            if (!string.IsNullOrEmpty(text) && text.Contains("<<<BODY>>>"))`
` 236`  `                            {`
` 237`  `                                int p = text.IndexOf("\n<<<BODY>>>\n", StringComparison.Ordinal);`
` 238`  `                                if (p > 0)`
` 239`  `                                {`
` 240`  `                                    lessonTitle = text.Substring(0, p);`
` 241`  `                                    content = text.Substring(p + "\n<<<BODY>>>\n".Length);`
` 242`  `                                }`
` 243`  `                            }`
` 244`  `                            else if (!string.IsNullOrEmpty(text) && text.Length < 80)`
` 245`  `                            {`
` 246`  `                                lessonTitle = text;`
` 247`  `                            }`
` 248`  `                            if (!string.IsNullOrEmpty(media)) content = media;`
` 249`  ``
` 250`  `                            int smid = 0;`
` 251`  `                            try { smid = Convert.ToInt32(m["SMID"]); } catch { smid = i; }`
  - → Error handling block.
` 252`  ``
` 253`  `                            lessons.Add(new`
` 254`  `                            {`
` 255`  `                                schid = smid,`
` 256`  `                                title = lessonTitle,`
` 257`  `                                type = type,`
` 258`  `                                content = content,`
` 259`  `                                materials = new object[0]`
` 260`  `                            });`
` 261`  `                        }`
` 262`  `                    }`
` 263`  `                    catch { /* no mats */ }`
  - → Handle/log exception.
` 264`  `                }`
` 265`  ``
` 266`  `                chapters.Add(new`
` 267`  `                {`
` 268`  `                    chid = chid,`
` 269`  `                    title = Safe(ch["Title"]),`
` 270`  `                    lessons = lessons`
` 271`  `                });`
` 272`  `            }`
` 273`  `        }`
` 274`  ``
` 275`  `        return new { success = true, chapters = chapters, schema = SchemaMap.DebugInfo() };`
` 276`  `    }`
` 277`  ``
` 278`  `    private List<object> LoadMats(SqlConnection conn, int parentId, out string type, out string content)`
  - → Database access (pure SQL).
` 279`  `    {`
` 280`  `        type = "Text";`
` 281`  `        content = "";`
` 282`  `        var materials = new List<object>();`
` 283`  `        try`
  - → Error handling block.
` 284`  `        {`
` 285`  `            DataTable mats = null;`
` 286`  `            // Prefer SchemaMap query; fall back to classic StudyMats`
` 287`  `            try`
  - → Error handling block.
` 288`  `            {`
` 289`  `                if (!string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 290`  `                {`
` 291`  `                    string orderBy = !string.IsNullOrEmpty(SchemaMap.MatIndex)`
` 292`  `                        ? Q(SchemaMap.MatIndex) + ", " + Q(SchemaMap.MatPk)`
` 293`  `                        : Q(SchemaMap.MatPk);`
` 294`  `                    string sql = BuildMatSelect() +`
` 295`  `                                 " WHERE " + Q(SchemaMap.MatSubFk) + "=@Key ORDER BY " + orderBy;`
` 296`  `                    mats = Query(conn, sql, P("@Key", parentId));`
` 297`  `                }`
` 298`  `            }`
` 299`  `            catch { mats = null; }`
  - → Handle/log exception.
` 300`  ``
` 301`  `            if (mats == null || mats.Rows.Count == 0)`
` 302`  `            {`
` 303`  `                try`
  - → Error handling block.
` 304`  `                {`
` 305`  `                    mats = Query(conn, @"`
` 306`  `SELECT SMID, Type AS TypeCol, TextContent AS TextCol, MediaLink AS MediaCol`
` 307`  `FROM StudyMats WHERE SchID=@Key ORDER BY [Index], SMID", P("@Key", parentId));`
` 308`  `                }`
` 309`  `                catch`
  - → Handle/log exception.
` 310`  `                {`
` 311`  `                    try`
  - → Error handling block.
` 312`  `                    {`
` 313`  `                        mats = Query(conn, @"`
` 314`  `SELECT SMID, Type AS TypeCol, TextContent AS TextCol, MediaLink AS MediaCol`
` 315`  `FROM StudyMats WHERE SchID=@Key ORDER BY SMID", P("@Key", parentId));`
` 316`  `                    }`
` 317`  `                    catch { mats = new DataTable(); }`
  - → Handle/log exception.
` 318`  `                }`
` 319`  `            }`
` 320`  ``
` 321`  `            if (mats.Rows.Count > 0)`
` 322`  `            {`
` 323`  `                // Prefer first file row as primary content when present (preview)`
` 324`  `                DataRow bodyRow = mats.Rows[0];`
` 325`  `                DataRow fileRow = null;`
` 326`  `                foreach (DataRow r in mats.Rows)`
` 327`  `                {`
` 328`  `                    var media0 = Col(r, "MediaCol");`
` 329`  `                    var t0 = Col(r, "TypeCol") ?? "";`
` 330`  `                    if (LooksLikeFileUrl(media0) ||`
` 331`  `                        string.Equals(t0, "Video", StringComparison.OrdinalIgnoreCase) ||`
` 332`  `                        string.Equals(t0, "PDF", StringComparison.OrdinalIgnoreCase) ||`
` 333`  `                        string.Equals(t0, "Image", StringComparison.OrdinalIgnoreCase) ||`
` 334`  `                        string.Equals(t0, "File", StringComparison.OrdinalIgnoreCase))`
` 335`  `                    {`
` 336`  `                        if (fileRow == null) fileRow = r;`
` 337`  `                    }`
` 338`  `                }`
` 339`  `                // Body text row if any`
` 340`  `                foreach (DataRow r in mats.Rows)`
` 341`  `                {`
` 342`  `                    var t0 = Col(r, "TypeCol") ?? "";`
` 343`  `                    var media0 = Col(r, "MediaCol");`
` 344`  `                    if (string.Equals(t0, "Text", StringComparison.OrdinalIgnoreCase) ||`
` 345`  `                        string.IsNullOrEmpty(media0) || !LooksLikeFileUrl(media0))`
` 346`  `                    {`
` 347`  `                        bodyRow = r;`
` 348`  `                        break;`
` 349`  `                    }`
` 350`  `                }`
` 351`  ``
` 352`  `                if (fileRow != null)`
` 353`  `                {`
` 354`  `                    type = Col(fileRow, "TypeCol");`
` 355`  `                    if (string.IsNullOrEmpty(type)) type = GuessTypeFromUrl(Col(fileRow, "MediaCol"));`
` 356`  `                    content = Col(fileRow, "MediaCol");`
` 357`  `                    if (string.IsNullOrEmpty(content)) content = Col(fileRow, "TextCol");`
` 358`  `                }`
` 359`  `                else`
` 360`  `                {`
` 361`  `                    type = Col(bodyRow, "TypeCol");`
` 362`  `                    if (string.IsNullOrEmpty(type)) type = "Text";`
` 363`  `                    var mediaB = Col(bodyRow, "MediaCol");`
` 364`  `                    var textB = Col(bodyRow, "TextCol");`
` 365`  `                    content = !string.IsNullOrEmpty(mediaB) && LooksLikeFileUrl(mediaB) ? mediaB : textB;`
` 366`  `                    if (string.IsNullOrEmpty(content)) content = mediaB;`
` 367`  `                }`
` 368`  `            }`
` 369`  ``
` 370`  `            foreach (DataRow m in mats.Rows)`
` 371`  `            {`
` 372`  `                int smid = 0;`
` 373`  `                try { smid = Convert.ToInt32(m["SMID"]); } catch { }`
  - → Error handling block.
` 374`  `                var media = Col(m, "MediaCol");`
` 375`  `                var text = Col(m, "TextCol");`
` 376`  `                var t = Col(m, "TypeCol");`
` 377`  `                // ONLY promote TextContent → media when it is a real store path (GUID / Uploads/...)`
` 378`  `                // Never use original display names like "My Report.pdf" as paths.`
` 379`  `                if (string.IsNullOrEmpty(media) && IsStoredMediaPath(text))`
` 380`  `                    media = text;`
` 381`  `                // If media is a bare original name, keep fileName for Media.ashx .meta lookup`
` 382`  `                string bareName = null;`
` 383`  `                if (!string.IsNullOrEmpty(media) && !IsStoredMediaPath(media))`
` 384`  `                {`
` 385`  `                    bareName = Path.GetFileName(media.Replace('\\', '/'));`
` 386`  `                    media = null;`
` 387`  `                }`
` 388`  ``
` 389`  `                string fn = !string.IsNullOrEmpty(text) ? text : bareName;`
` 390`  `                if (string.IsNullOrEmpty(fn) && IsStoredMediaPath(media))`
` 391`  `                    fn = Path.GetFileName(media.Replace('\\', '/'));`
` 392`  ``
` 393`  `                // When we have GUID path + original name, write .meta so Media.ashx can resolve name→guid`
` 394`  `                if (IsStoredMediaPath(media) && !string.IsNullOrEmpty(fn))`
` 395`  `                {`
` 396`  `                    try`
  - → Error handling block.
` 397`  `                    {`
` 398`  `                        string rel = media.Replace('\\', '/');`
` 399`  `                        if (rel.StartsWith("Uploads/", StringComparison.OrdinalIgnoreCase))`
` 400`  `                            rel = rel.Substring(8);`
` 401`  `                        // HttpContext available via Open() callers — use MapPath from connection's... `
` 402`  `                        // Skip here; UploadMedia writes .meta. Repair via Media.ashx log/meta only.`
` 403`  `                    }`
` 404`  `                    catch { }`
  - → Handle/log exception.
` 405`  `                }`
` 406`  ``
` 407`  `                // For preview: prefer GUID mediaLink; else pass original name for .meta lookup`
` 408`  `                string linkOut = media;`
` 409`  `                if (string.IsNullOrEmpty(linkOut) && !string.IsNullOrEmpty(fn) &&`
` 410`  `                    fn.IndexOf('.') > 0)`
` 411`  `                    linkOut = fn; // Media.ashx FindByOriginalName`
` 412`  ``
` 413`  `                materials.Add(new`
` 414`  `                {`
` 415`  `                    smid = smid,`
` 416`  `                    type = string.IsNullOrEmpty(t) ? GuessTypeFromUrl(media ?? text ?? "") : t,`
` 417`  `                    textContent = text,`
` 418`  `                    mediaLink = linkOut,`
` 419`  `                    url = linkOut,`
` 420`  `                    fileName = fn`
` 421`  `                });`
` 422`  `            }`
` 423`  `        }`
` 424`  `        catch { }`
  - → Handle/log exception.
` 425`  `        return materials;`
` 426`  `    }`
` 427`  ``
` 428`  `    private static string BuildMatSelect()`
` 429`  `    {`
` 430`  `        string typeExpr = string.IsNullOrEmpty(SchemaMap.MatType)`
` 431`  `            ? "CAST(NULL AS nvarchar(100))" : Q(SchemaMap.MatType);`
` 432`  `        string textExpr = string.IsNullOrEmpty(SchemaMap.MatText)`
` 433`  `            ? "CAST(NULL AS nvarchar(max))" : Q(SchemaMap.MatText);`
` 434`  `        string mediaExpr = string.IsNullOrEmpty(SchemaMap.MatMedia)`
` 435`  `            ? "CAST(NULL AS nvarchar(max))" : Q(SchemaMap.MatMedia);`
` 436`  `        return "SELECT " +`
` 437`  `               Q(SchemaMap.MatPk) + " AS SMID, " +`
` 438`  `               typeExpr + " AS TypeCol, " +`
` 439`  `               textExpr + " AS TextCol, " +`
` 440`  `               mediaExpr + " AS MediaCol " +`
` 441`  `               "FROM " + Q(SchemaMap.MatTable);`
` 442`  `    }`
` 443`  ``
` 444`  `    // ═══════════════════════════════════════════════════════════════════════`
` 445`  `    // SECTIONS (Chapters)`
` 446`  `    // ═══════════════════════════════════════════════════════════════════════`
` 447`  ``
` 448`  `    private object SaveSection(int lecturerUid, int chid, int cid, string title)`
` 449`  `    {`
` 450`  `        if (cid <= 0) return new { success = false, message = "Invalid course id." };`
` 451`  `        if (string.IsNullOrWhiteSpace(title)) return new { success = false, message = "Section title required." };`
` 452`  ``
` 453`  `        using (var conn = Open())`
  - → Import namespace/types.
` 454`  `        {`
` 455`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 456`  `            if (chid > 0)`
` 457`  `            {`
` 458`  `                string sql = string.Format("UPDATE {0} SET {1}=@Title WHERE {2}=@ChID AND {3}=@CID",`
` 459`  `                    Q(SchemaMap.ChTable), Q(SchemaMap.ChTitle), Q(SchemaMap.ChPk), Q(SchemaMap.ChCourseFk));`
` 460`  `                Exec(conn, sql, P("@Title", title.Trim()), P("@ChID", chid), P("@CID", cid));`
` 461`  `                return new { success = true, chid = chid };`
` 462`  `            }`
` 463`  ``
` 464`  `            int newId;`
` 465`  `            if (!string.IsNullOrEmpty(SchemaMap.ChIndex))`
` 466`  `            {`
` 467`  `                int next = ScalarInt(conn,`
` 468`  `                    string.Format("SELECT ISNULL(MAX({0}),0)+1 FROM {1} WHERE {2}=@CID",`
` 469`  `                        Q(SchemaMap.ChIndex), Q(SchemaMap.ChTable), Q(SchemaMap.ChCourseFk)),`
` 470`  `                    P("@CID", cid));`
` 471`  `                newId = ScalarInt(conn,`
` 472`  `                    string.Format("INSERT INTO {0} ({1}, {2}, {3}) OUTPUT INSERTED.{4} VALUES (@CID, @Idx, @Title)",`
` 473`  `                        Q(SchemaMap.ChTable), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChIndex), Q(SchemaMap.ChTitle), Q(SchemaMap.ChPk)),`
` 474`  `                    P("@CID", cid), P("@Idx", next), P("@Title", title.Trim()));`
` 475`  `            }`
` 476`  `            else`
` 477`  `            {`
` 478`  `                newId = ScalarInt(conn,`
` 479`  `                    string.Format("INSERT INTO {0} ({1}, {2}) OUTPUT INSERTED.{3} VALUES (@CID, @Title)",`
` 480`  `                        Q(SchemaMap.ChTable), Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTitle), Q(SchemaMap.ChPk)),`
` 481`  `                    P("@CID", cid), P("@Title", title.Trim()));`
` 482`  `            }`
` 483`  `            return new { success = true, chid = newId };`
` 484`  `        }`
` 485`  `    }`
` 486`  ``
` 487`  `    private object DeleteSection(int lecturerUid, int chid)`
` 488`  `    {`
` 489`  `        if (chid <= 0) return new { success = false, message = "Invalid section id." };`
` 490`  `        using (var conn = Open())`
  - → Import namespace/types.
` 491`  `        {`
` 492`  `            int cid = ScalarInt(conn,`
` 493`  `                string.Format("SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 494`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 495`  `                P("@ChID", chid));`
` 496`  `            if (cid <= 0) return new { success = false, message = "Section not found." };`
` 497`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 498`  ``
` 499`  `            // delete children lessons + mats`
` 500`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && SchemaMap.MatLinksToSub)`
` 501`  `            {`
` 502`  `                try`
  - → Error handling block.
` 503`  `                {`
` 504`  `                    Exec(conn, string.Format(`
` 505`  `                        "DELETE m FROM {0} m INNER JOIN {1} s ON s.{2}=m.{3} WHERE s.{4}=@ChID",`
` 506`  `                        Q(SchemaMap.MatTable), Q(SchemaMap.SubTable), Q(SchemaMap.SubPk), Q(SchemaMap.MatSubFk), Q(SchemaMap.SubChapterFk)),`
` 507`  `                        P("@ChID", chid));`
` 508`  `                }`
` 509`  `                catch { }`
  - → Handle/log exception.
` 510`  `                try`
  - → Error handling block.
` 511`  `                {`
` 512`  `                    Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@ChID", Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk)),`
` 513`  `                        P("@ChID", chid));`
` 514`  `                }`
` 515`  `                catch { }`
  - → Handle/log exception.
` 516`  `            }`
` 517`  `            else if (!SchemaMap.MatLinksToSub)`
` 518`  `            {`
` 519`  `                try`
  - → Error handling block.
` 520`  `                {`
` 521`  `                    Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@ChID", Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 522`  `                        P("@ChID", chid));`
` 523`  `                }`
` 524`  `                catch { }`
  - → Handle/log exception.
` 525`  `            }`
` 526`  ``
` 527`  `            Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@ChID", Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 528`  `                P("@ChID", chid));`
` 529`  `        }`
` 530`  `        return new { success = true };`
` 531`  `    }`
` 532`  ``
` 533`  `    // ═══════════════════════════════════════════════════════════════════════`
` 534`  `    // LESSONS`
` 535`  `    // ═══════════════════════════════════════════════════════════════════════`
` 536`  ``
` 537`  `    private object SaveLesson(int lecturerUid, int schid, int chid, string title, string type, string content, string materialsJson)`
` 538`  `    {`
` 539`  `        if (chid <= 0) return new { success = false, message = "Invalid section id (chid)." };`
` 540`  `        if (string.IsNullOrWhiteSpace(title)) return new { success = false, message = "Lesson title is required." };`
` 541`  ``
` 542`  `        using (var conn = Open())`
  - → Import namespace/types.
` 543`  `        {`
` 544`  `            int cid = ScalarInt(conn,`
` 545`  `                string.Format("SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 546`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 547`  `                P("@ChID", chid));`
` 548`  `            if (cid <= 0) return new { success = false, message = "Section not found (ChID=" + chid + ").", schema = SchemaMap.DebugInfo() };`
` 549`  `            AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 550`  ``
` 551`  `            string matType = NormalizeType(type);`
` 552`  `            string textContent, mediaLink;`
` 553`  `            SplitContent(matType, content, title, out textContent, out mediaLink);`
` 554`  `            if (string.IsNullOrEmpty(textContent) && string.IsNullOrEmpty(mediaLink))`
` 555`  `                textContent = title;`
` 556`  ``
` 557`  `            // ── Preferred: SubChapters (or Lessons) row per lesson ─────`
` 558`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && !string.IsNullOrEmpty(SchemaMap.SubPk))`
` 559`  `            {`
` 560`  `                int resolvedId;`
` 561`  `                if (schid > 0)`
` 562`  `                {`
` 563`  `                    int n = Exec(conn, string.Format(`
` 564`  `                        "UPDATE {0} SET {1}=@Title WHERE {2}=@SchID AND {3}=@ChID",`
` 565`  `                        Q(SchemaMap.SubTable), Q(SchemaMap.SubTitle), Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk)),`
` 566`  `                        P("@Title", title.Trim()), P("@SchID", schid), P("@ChID", chid));`
` 567`  `                    if (n <= 0) return new { success = false, message = "Lesson not found for update." };`
` 568`  `                    resolvedId = schid;`
` 569`  `                    // clear prior mats for this lesson (schema map + classic StudyMats)`
` 570`  `                    if (SchemaMap.MatLinksToSub && !string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 571`  `                    {`
` 572`  `                        try`
  - → Error handling block.
` 573`  `                        {`
` 574`  `                            Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@SchID", Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 575`  `                                P("@SchID", resolvedId));`
` 576`  `                        }`
` 577`  `                        catch { }`
  - → Handle/log exception.
` 578`  `                    }`
` 579`  `                    try { Exec(conn, "DELETE FROM StudyMats WHERE SchID=@SchID", P("@SchID", resolvedId)); } catch { }`
  - → Error handling block.
` 580`  `                    try { Exec(conn, "DELETE FROM StudyMat WHERE SchID=@SchID", P("@SchID", resolvedId)); } catch { }`
  - → Error handling block.
` 581`  `                }`
` 582`  `                else`
` 583`  `                {`
` 584`  `                    try`
  - → Error handling block.
` 585`  `                    {`
` 586`  `                        if (!string.IsNullOrEmpty(SchemaMap.SubIndex))`
` 587`  `                        {`
` 588`  `                            int next = ScalarInt(conn, string.Format(`
` 589`  `                                "SELECT ISNULL(MAX({0}),0)+1 FROM {1} WHERE {2}=@ChID",`
` 590`  `                                Q(SchemaMap.SubIndex), Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk)),`
` 591`  `                                P("@ChID", chid));`
` 592`  `                            resolvedId = ScalarInt(conn, string.Format(`
` 593`  `                                "INSERT INTO {0} ({1}, {2}, {3}) OUTPUT INSERTED.{4} VALUES (@ChID, @Idx, @Title)",`
` 594`  `                                Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubIndex), Q(SchemaMap.SubTitle), Q(SchemaMap.SubPk)),`
` 595`  `                                P("@ChID", chid), P("@Idx", next), P("@Title", title.Trim()));`
` 596`  `                        }`
` 597`  `                        else`
` 598`  `                        {`
` 599`  `                            resolvedId = ScalarInt(conn, string.Format(`
` 600`  `                                "INSERT INTO {0} ({1}, {2}) OUTPUT INSERTED.{3} VALUES (@ChID, @Title)",`
` 601`  `                                Q(SchemaMap.SubTable), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTitle), Q(SchemaMap.SubPk)),`
` 602`  `                                P("@ChID", chid), P("@Title", title.Trim()));`
` 603`  `                        }`
` 604`  `                    }`
` 605`  `                    catch (Exception ex)`
  - → Handle/log exception.
` 606`  `                    {`
` 607`  `                        return new`
` 608`  `                        {`
` 609`  `                            success = false,`
` 610`  `                            message = "INSERT into " + SchemaMap.SubTable + " failed: " + ex.Message,`
` 611`  `                            schema = SchemaMap.DebugInfo()`
` 612`  `                        };`
` 613`  `                    }`
` 614`  `                }`
` 615`  ``
` 616`  `                if (resolvedId <= 0)`
` 617`  `                    return new { success = false, message = "Lesson insert returned invalid id.", schema = SchemaMap.DebugInfo() };`
` 618`  ``
` 619`  `                // Attach content: prefer StudyMats keyed by lesson id; else by chapter id`
` 620`  `                int matParent = SchemaMap.MatLinksToSub ? resolvedId : chid;`
` 621`  `                // Encode title into text so content is recoverable when mats hang on chapter`
` 622`  `                string storeText = textContent;`
` 623`  `                if (!SchemaMap.MatLinksToSub)`
` 624`  `                    storeText = title.Trim() + "\n<<<BODY>>>\n" + (textContent ?? "");`
` 625`  ``
` 626`  `                // If lesson is Text but client sent file materials, promote first file`
` 627`  `                // so Course Preview always has a playable/viewable primary media path.`
` 628`  `                PromotePrimaryFromMaterials(ref matType, ref textContent, ref mediaLink, materialsJson);`
` 629`  `                storeText = textContent;`
` 630`  `                if (!SchemaMap.MatLinksToSub)`
` 631`  `                    storeText = title.Trim() + "\n<<<BODY>>>\n" + (textContent ?? "");`
` 632`  ``
` 633`  `                string warn = null;`
` 634`  `                int matsSaved = 0;`
` 635`  `                // Always attempt StudyMats (hardcoded + schema map)`
` 636`  `                warn = InsertMat(conn, matParent, matType, storeText, mediaLink, 1);`
` 637`  `                if (warn == null) matsSaved++;`
` 638`  `                int extra = InsertExtraMaterials(conn, matParent, materialsJson);`
` 639`  `                matsSaved += extra;`
` 640`  `                if (extra == 0 && !string.IsNullOrWhiteSpace(materialsJson) && materialsJson.Trim() != "[]")`
` 641`  `                {`
` 642`  `                    warn = (warn ?? "") + " Materials JSON was provided but 0 file rows were saved. Check StudyMats.MediaLink column.";`
` 643`  `                }`
` 644`  ``
` 645`  `                // Lesson row exists even if StudyMats fails — still success`
` 646`  `                return new`
` 647`  `                {`
` 648`  `                    success = true,`
` 649`  `                    schid = resolvedId,`
` 650`  `                    chid = chid,`
` 651`  `                    warning = warn,`
` 652`  `                    materialsSaved = matsSaved,`
` 653`  `                    type = matType,`
` 654`  `                    schema = SchemaMap.DebugInfo()`
` 655`  `                };`
` 656`  `            }`
` 657`  ``
` 658`  `            // ── Fallback: StudyMats only (no SubChapters table) ────────`
` 659`  `            if (!string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 660`  `            {`
` 661`  `                string storeText = title.Trim() + "\n<<<BODY>>>\n" + (textContent ?? "");`
` 662`  `                int matParent = chid; // mats on chapter`
` 663`  `                int resolvedId;`
` 664`  `                if (schid > 0)`
` 665`  `                {`
` 666`  `                    string updErr = UpdateMat(conn, schid, matType, storeText, mediaLink);`
` 667`  `                    if (updErr != null) return new { success = false, message = updErr, schema = SchemaMap.DebugInfo() };`
` 668`  `                    resolvedId = schid;`
` 669`  `                }`
` 670`  `                else`
` 671`  `                {`
` 672`  `                    string warn = InsertMat(conn, matParent, matType, storeText, mediaLink, 1);`
` 673`  `                    resolvedId = ScalarInt(conn, string.Format(`
` 674`  `                        "SELECT MAX({0}) FROM {1} WHERE {2}=@Parent",`
` 675`  `                        Q(SchemaMap.MatPk), Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 676`  `                        P("@Parent", matParent));`
` 677`  `                    if (resolvedId <= 0)`
` 678`  `                        return new { success = false, message = "StudyMats insert failed. " + warn, schema = SchemaMap.DebugInfo() };`
` 679`  `                }`
` 680`  `                return new { success = true, schid = resolvedId, chid = chid, schema = SchemaMap.DebugInfo() };`
` 681`  `            }`
` 682`  ``
` 683`  `            return new`
` 684`  `            {`
` 685`  `                success = false,`
` 686`  `                message = "Could not determine how lessons are stored. Open CurriculumApi.ashx?action=schema while logged in.",`
` 687`  `                schema = SchemaMap.DebugInfo()`
` 688`  `            };`
` 689`  `        }`
` 690`  `    }`
` 691`  ``
` 692`  `    private object DeleteLesson(int lecturerUid, int schid)`
` 693`  `    {`
` 694`  `        if (schid <= 0) return new { success = false, message = "Invalid lesson id." };`
` 695`  `        using (var conn = Open())`
  - → Import namespace/types.
` 696`  `        {`
` 697`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && SchemaMap.MatLinksToSub)`
` 698`  `            {`
` 699`  `                int chid = ScalarInt(conn, string.Format(`
` 700`  `                    "SELECT {0} FROM {1} WHERE {2}=@Id",`
` 701`  `                    Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTable), Q(SchemaMap.SubPk)),`
` 702`  `                    P("@Id", schid));`
` 703`  `                int cid = ScalarInt(conn, string.Format(`
` 704`  `                    "SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 705`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 706`  `                    P("@ChID", chid));`
` 707`  `                if (cid <= 0) return new { success = false, message = "Lesson not found." };`
` 708`  `                AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 709`  `                try`
  - → Error handling block.
` 710`  `                {`
` 711`  `                    Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@Id", Q(SchemaMap.MatTable), Q(SchemaMap.MatSubFk)),`
` 712`  `                        P("@Id", schid));`
` 713`  `                }`
` 714`  `                catch { }`
  - → Handle/log exception.
` 715`  `                Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@Id", Q(SchemaMap.SubTable), Q(SchemaMap.SubPk)),`
` 716`  `                    P("@Id", schid));`
` 717`  `            }`
` 718`  `            else`
` 719`  `            {`
` 720`  `                // legacy mat id`
` 721`  `                int chid = ScalarInt(conn, string.Format(`
` 722`  `                    "SELECT {0} FROM {1} WHERE {2}=@Id",`
` 723`  `                    Q(SchemaMap.MatSubFk), Q(SchemaMap.MatTable), Q(SchemaMap.MatPk)),`
` 724`  `                    P("@Id", schid));`
` 725`  `                int cid = ScalarInt(conn, string.Format(`
` 726`  `                    "SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 727`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 728`  `                    P("@ChID", chid));`
` 729`  `                if (cid > 0) AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 730`  `                Exec(conn, string.Format("DELETE FROM {0} WHERE {1}=@Id", Q(SchemaMap.MatTable), Q(SchemaMap.MatPk)),`
` 731`  `                    P("@Id", schid));`
` 732`  `            }`
` 733`  `        }`
` 734`  `        return new { success = true };`
` 735`  `    }`
` 736`  ``
` 737`  `    private object GetLesson(int lecturerUid, int schid)`
` 738`  `    {`
` 739`  `        using (var conn = Open())`
  - → Import namespace/types.
` 740`  `        {`
` 741`  `            if (!string.IsNullOrEmpty(SchemaMap.SubTable) && SchemaMap.MatLinksToSub)`
` 742`  `            {`
` 743`  `                var dt = Query(conn, string.Format(`
` 744`  `                    "SELECT {0} AS SchID, {1} AS ChID, {2} AS Title FROM {3} WHERE {0}=@Id",`
` 745`  `                    Q(SchemaMap.SubPk), Q(SchemaMap.SubChapterFk), Q(SchemaMap.SubTitle), Q(SchemaMap.SubTable)),`
` 746`  `                    P("@Id", schid));`
` 747`  `                if (dt.Rows.Count == 0) return new { success = false, message = "Lesson not found." };`
` 748`  `                int chid = Convert.ToInt32(dt.Rows[0]["ChID"]);`
` 749`  `                int cid = ScalarInt(conn, string.Format(`
` 750`  `                    "SELECT {0} FROM {1} WHERE {2}=@ChID",`
` 751`  `                    Q(SchemaMap.ChCourseFk), Q(SchemaMap.ChTable), Q(SchemaMap.ChPk)),`
` 752`  `                    P("@ChID", chid));`
` 753`  `                AssertOwner(conn, lecturerUid, cid);`
  - → Ownership check — prevent IDOR.
` 754`  ``
` 755`  `                string type, content;`
` 756`  `                var materials = LoadMats(conn, schid, out type, out content);`
` 757`  `                return new`
` 758`  `                {`
` 759`  `                    success = true,`
` 760`  `                    schid = schid,`
` 761`  `                    chid = chid,`
` 762`  `                    title = Safe(dt.Rows[0]["Title"]),`
` 763`  `                    type = type,`
` 764`  `                    content = content,`
` 765`  `                    materials = FilterFileMaterials(materials)`
` 766`  `                };`
` 767`  `            }`
` 768`  `            else`
` 769`  `            {`
` 770`  `                string sql = BuildMatSelect() + " WHERE " + Q(SchemaMap.MatPk) + "=@Id";`
` 771`  `                var dt = Query(conn, sql, P("@Id", schid));`
` 772`  `                if (dt.Rows.Count == 0) return new { success = false, message = "Lesson not found." };`
` 773`  `                string type2 = Col(dt.Rows[0], "TypeCol");`
` 774`  `                if (string.IsNullOrEmpty(type2)) type2 = "Text";`
` 775`  `                var media2 = Col(dt.Rows[0], "MediaCol");`
` 776`  `                var text2 = Col(dt.Rows[0], "TextCol");`
` 777`  `                return new`
` 778`  `                {`
` 779`  `                    success = true,`
` 780`  `                    schid = schid,`
` 781`  `                    chid = 0,`
` 782`  `                    title = text2,`
` 783`  `                    type = type2,`
` 784`  `                    content = !string.IsNullOrEmpty(media2) ? media2 : text2,`
` 785`  `                    materials = new object[0]`
` 786`  `                };`
` 787`  `            }`
` 788`  `        }`
` 789`  `    }`
` 790`  ``
` 791`  `    /// <summary>Rows with a file URL suitable for the materials JSON field.</summary>`
` 792`  `    private static List<object> FilterFileMaterials(List<object> materials)`
` 793`  `    {`
` 794`  `        var list = new List<object>();`
` 795`  `        if (materials == null) return list;`
` 796`  `        foreach (var o in materials)`
` 797`  `        {`
` 798`  `            var d = o as Dictionary<string, object>;`
` 799`  `            string media = null, text = null, type = null;`
` 800`  `            int smid = 0;`
` 801`  `            if (d != null)`
` 802`  `            {`
` 803`  `                media = d.ContainsKey("mediaLink") ? Convert.ToString(d["mediaLink"]) : (d.ContainsKey("url") ? Convert.ToString(d["url"]) : null);`
` 804`  `                text = d.ContainsKey("fileName") ? Convert.ToString(d["fileName"]) : (d.ContainsKey("textContent") ? Convert.ToString(d["textContent"]) : null);`
` 805`  `                type = d.ContainsKey("type") ? Convert.ToString(d["type"]) : null;`
` 806`  `                if (d.ContainsKey("smid") && d["smid"] != null) try { smid = Convert.ToInt32(d["smid"]); } catch { }`
` 807`  `            }`
` 808`  `            else`
` 809`  `            {`
` 810`  `                // anonymous type fallback`
` 811`  `                var t = o.GetType();`
` 812`  `                var pMedia = t.GetProperty("mediaLink") ?? t.GetProperty("url");`
` 813`  `                var pText = t.GetProperty("fileName") ?? t.GetProperty("textContent");`
` 814`  `                var pType = t.GetProperty("type");`
` 815`  `                var pId = t.GetProperty("smid");`
` 816`  `                if (pMedia != null) media = pMedia.GetValue(o, null) as string;`
` 817`  `                if (pText != null) text = pText.GetValue(o, null) as string;`
` 818`  `                if (pType != null) type = pType.GetValue(o, null) as string;`
` 819`  `                if (pId != null && pId.GetValue(o, null) != null)`
` 820`  `                    try { smid = Convert.ToInt32(pId.GetValue(o, null)); } catch { }`
  - → Error handling block.
` 821`  `            }`
` 822`  `            if (string.IsNullOrWhiteSpace(media) || !LooksLikeFileUrl(media)) continue;`
` 823`  `            string fn = string.IsNullOrWhiteSpace(text) ? Path.GetFileName(media.Replace('\\', '/')) : text;`
` 824`  `            list.Add(new`
` 825`  `            {`
` 826`  `                smid = smid,`
` 827`  `                url = media,`
` 828`  `                mediaLink = media,`
` 829`  `                fileName = fn,`
` 830`  `                type = string.IsNullOrEmpty(type) ? GuessTypeFromUrl(media) : type`
` 831`  `            });`
` 832`  `        }`
` 833`  `        return list;`
` 834`  `    }`
` 835`  ``
` 836`  `    private static bool LooksLikeFileUrl(string s)`
` 837`  `    {`
` 838`  `        // Only treat as a file URL if it is a real stored path — NOT bare "report.pdf"`
` 839`  `        return IsStoredMediaPath(s);`
` 840`  `    }`
` 841`  ``
` 842`  `    private static string GuessTypeFromUrl(string url)`
` 843`  `    {`
` 844`  `        var low = (url ?? "").ToLowerInvariant();`
` 845`  `        if (low.Contains(".mp4") || low.Contains(".webm") || low.Contains(".mov")) return "Video";`
` 846`  `        if (low.Contains(".png") || low.Contains(".jpg") || low.Contains(".jpeg") || low.Contains(".gif") || low.Contains(".webp")) return "Image";`
` 847`  `        if (low.Contains(".pdf")) return "PDF";`
` 848`  `        return "File";`
` 849`  `    }`
` 850`  ``
` 851`  `    // ═══════════════════════════════════════════════════════════════════════`
` 852`  `    // StudyMats helpers`
` 853`  `    // ═══════════════════════════════════════════════════════════════════════`
` 854`  ``
` 855`  `    private string InsertMat(SqlConnection conn, int parentId, string type, string text, string media, int index)`
  - → Database access (pure SQL).
` 856`  `    {`
` 857`  `        // Normalize media path for storage`
` 858`  `        if (!string.IsNullOrWhiteSpace(media))`
` 859`  `            media = NormalizeStoredMediaPath(media);`
` 860`  ``
` 861`  `        var errors = new List<string>();`
` 862`  ``
` 863`  `        // 1) Standard EduDB StudyMats (preferred — matches ER diagram)`
` 864`  `        string[] attempts = new[]`
` 865`  `        {`
` 866`  `            "INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink, [Index]) VALUES (@Parent, @Type, @Text, @Media, @Idx)",`
` 867`  `            "INSERT INTO StudyMats (SchID, Type, TextContent, MediaLink) VALUES (@Parent, @Type, @Text, @Media)",`
` 868`  `            "INSERT INTO StudyMat (SchID, Type, TextContent, MediaLink, [Index]) VALUES (@Parent, @Type, @Text, @Media, @Idx)",`
` 869`  `            "INSERT INTO StudyMat (SchID, Type, TextContent, MediaLink) VALUES (@Parent, @Type, @Text, @Media)"`
` 870`  `        };`
` 871`  `        foreach (var sql in attempts)`
` 872`  `        {`
` 873`  `            try`
  - → Error handling block.
` 874`  `            {`
` 875`  `                Exec(conn, sql,`
` 876`  `                    P("@Parent", parentId),`
` 877`  `                    P("@Type", type ?? "Text"),`
` 878`  `                    P("@Text", (object)text ?? DBNull.Value),`
` 879`  `                    P("@Media", (object)media ?? DBNull.Value),`
` 880`  `                    P("@Idx", index));`
` 881`  `                return null;`
` 882`  `            }`
` 883`  `            catch (Exception ex) { errors.Add(ex.Message); }`
  - → Handle/log exception.
` 884`  `        }`
` 885`  ``
` 886`  `        // 2) SchemaMap dynamic columns`
` 887`  `        try`
  - → Error handling block.
` 888`  `        {`
` 889`  `            if (!string.IsNullOrEmpty(SchemaMap.MatTable) && !string.IsNullOrEmpty(SchemaMap.MatSubFk))`
` 890`  `            {`
` 891`  `                var cols = new List<string>();`
` 892`  `                var vals = new List<string>();`
` 893`  `                var pars = new List<SqlParameter>();`
` 894`  ``
` 895`  `                cols.Add(Q(SchemaMap.MatSubFk));`
` 896`  `                vals.Add("@Parent");`
` 897`  `                pars.Add(P("@Parent", parentId));`
` 898`  ``
` 899`  `                if (!string.IsNullOrEmpty(SchemaMap.MatType))`
` 900`  `                {`

_… truncated: 384 more lines in source. Open the original file for the rest._

## Source snapshot (raw)

_File has 1284 lines — raw dump omitted here to keep Markdown readable. Open `Pages/Lecturer/CurriculumApi.ashx` in the project._
