# grading.js
**Source:** `Pages/Lecturer/Scripts/grading.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

List submissions for lecturer courses; assign marks and feedback; CSV export.

## File overview

- **Total lines:** 366
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 2:** `submissions` — script-level `const`/`let`/`var`
- **Line 4:** `filtered` — script-level `const`/`let`/`var`
- **Line 5:** `currentIndex` — script-level `const`/`let`/`var`
- **Line 6:** `statusFilter` — script-level `const`/`let`/`var`
- **Line 11:** `params` — script-level `const`/`let`/`var`
- **Line 12:** `f` — script-level `const`/`let`/`var`
- **Line 15:** `btn` — script-level `const`/`let`/`var`
- **Line 28:** `p` — script-level `const`/`let`/`var`
- **Line 29:** `i` — script-level `const`/`let`/`var`
- **Line 36:** `u` — script-level `const`/`let`/`var`
- **Line 45:** `a` — script-level `const`/`let`/`var`
- **Line 50:** `path` — script-level `const`/`let`/`var`
- **Line 51:** `idx` — script-level `const`/`let`/`var`
- **Line 58:** `url` — script-level `const`/`let`/`var`
- **Line 73:** `out` — script-level `const`/`let`/`var`
- **Line 75:** `s` — script-level `const`/`let`/`var`
- **Line 79:** `o` — script-level `const`/`let`/`var`
- **Line 88:** `m` — script-level `const`/`let`/`var`
- **Line 113:** `res` — script-level `const`/`let`/`var`
- **Line 121:** `graded` — script-level `const`/`let`/`var`
- **Line 122:** `total` — script-level `const`/`let`/`var`
- **Line 123:** `pending` — script-level `const`/`let`/`var`
- **Line 125:** `bp` — script-level `const`/`let`/`var`
- **Line 144:** `pct` — script-level `const`/`let`/`var`
- **Line 160:** `q` — script-level `const`/`let`/`var`
- **Line 190:** `blob` — script-level `const`/`let`/`var`
- **Line 205:** `box` — script-level `const`/`let`/`var`
- **Line 211:** `colors` — script-level `const`/`let`/`var`
- **Line 213:** `div` — script-level `const`/`let`/`var`
- **Line 216:** `parsed` — script-level `const`/`let`/`var`
- **Line 217:** `fileIcon` — script-level `const`/`let`/`var`
- **Line 220:** `scoreHtml` — script-level `const`/`let`/`var`
- **Line 247:** `raw` — script-level `const`/`let`/`var`
- **Line 254:** `preview` — script-level `const`/`let`/`var`
- **Line 256:** `btnDl` — script-level `const`/`let`/`var`
- **Line 257:** `html` — script-level `const`/`let`/`var`
- **Line 260:** `view` — script-level `const`/`let`/`var`
- **Line 261:** `dl` — script-level `const`/`let`/`var`
- **Line 262:** `kind` — script-level `const`/`let`/`var`
- **Line 263:** `label` — script-level `const`/`let`/`var`
- **Line 300:** `max` — script-level `const`/`let`/`var`
- **Line 312:** `score` — script-level `const`/`let`/`var`
- **Line 318:** `next` — script-level `const`/`let`/`var`
- **Line 328:** `review` — script-level `const`/`let`/`var`
- **Line 329:** `err` — script-level `const`/`let`/`var`

## Functions / methods (16 found)

### `mediaAppRoot` — lines 25–32

```
function mediaAppRoot()
```

#### Explanation

- **Purpose:** Implements `mediaAppRoot`.
- **Local variables:** `p`, `i`

#### Line-by-line (this function)

`  25`  ``
`  26`  ``
`  27`  `function mediaAppRoot() {`
`  28`  `    var p = window.location.pathname || '';`
`  29`  `    var i = p.toLowerCase().indexOf('/pages/');`
`  30`  `    if (i > 0) return p.substring(0, i);`
`  31`  `    return '';`
`  32`  `}`

---

### `resolveMediaUrl` — lines 32–49

```
function resolveMediaUrl(raw, forDownload)
```

#### Explanation

- **Purpose:** Implements `resolveMediaUrl`.
- **Parameters:** `raw, forDownload`
- **Local variables:** `u`, `a`

#### Line-by-line (this function)

`  32`  ``
`  33`  ``
`  34`  `function resolveMediaUrl(raw, forDownload) {`
`  35`  `    if (!raw) return '';`
`  36`  `    var u = String(raw).trim();`
`  37`  `    if (/^https?:\/\//i.test(u) && u.indexOf('/Uploads/') < 0 && u.indexOf('Media.ashx') < 0 && u.indexOf('Uploads/') < 0)`
`  38`  `    return u;`
`  39`  `    if (u.indexOf('Media.ashx') >= 0) {`
`  40`  `        if (forDownload && u.indexOf('dl=1') < 0) return u + (u.indexOf('?') >= 0 ? '&' : '?') + 'dl=1';`
`  41`  `        return u;`
`  42`  `    }`
`  43`  `    try {`
  - → Error handling block.
`  44`  `        if (/^https?:\/\//i.test(u)) {`
`  45`  `        var a = document.createElement('a');`
`  46`  `        a.href = u;`
`  47`  `        u = a.pathname || u;`
`  48`  `    }`
`  49`  `}`

---

### `mediaKind` — lines 61–69

```
function mediaKind(s)
```

#### Explanation

- **Purpose:** Implements `mediaKind`.
- **Parameters:** `s`

#### Line-by-line (this function)

`  61`  ``
`  62`  ``
`  63`  `function mediaKind(s) {`
`  64`  `    s = (s || '').toLowerCase();`
`  65`  `    if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';`
`  66`  `    if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';`
`  67`  `    if (/\.pdf(\?|$)/.test(s)) return 'pdf';`
`  68`  `    return 'file';`
`  69`  `}`

---

### `parseAnswerContent` — lines 71–99

```
function parseAnswerContent(raw)
```

#### Explanation

- **Purpose:** Implements `parseAnswerContent`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `raw`
- **Local variables:** `out`, `s`, `o`, `m`

#### Line-by-line (this function)

`  71`  ``
`  72`  `function parseAnswerContent(raw) {`
`  73`  `    var out = { text: '', file: '', fileName: '' };`
`  74`  `    if (raw == null) return out;`
`  75`  `    var s = String(raw).trim();`
`  76`  `    if (!s) return out;`
`  77`  `    if (s.charAt(0) === '{') {`
`  78`  `        try {`
  - → Error handling block.
`  79`  `            var o = JSON.parse(s);`
  - → JS object ↔ JSON text.
`  80`  `            out.text = o.text || o.Text || '';`
`  81`  `            out.file = o.file || o.fileUrl || o.FileUrl || o.url || '';`
`  82`  `            out.fileName = o.fileName || o.FileName || '';`
`  83`  `            if (!out.fileName && out.file) out.fileName = out.file.split('/').pop();`
`  84`  `            return out;`
`  85`  `        } catch (e) { /* fall through */ }`
`  86`  `    }`
`  87`  `    // marker form`
`  88`  `    var m = s.match(/<<<FILE>>>([\s\S]*?)<<<ENDFILE>>>/i);`
`  89`  `    if (m) {`
`  90`  `        out.file = m[1].trim();`
`  91`  `        out.text = s.replace(m[0], '').trim();`
`  92`  `        out.fileName = out.file.split('/').pop();`
`  93`  `        return out;`
`  94`  `    }`
`  95`  `    if (/uploads\//i.test(s) || /Media\.ashx/i.test(s) || /\.(pdf|docx?|pptx?|png|jpe?g|mp4)(\?|$)/i.test(s)) {`
`  96`  `    out.file = s;`
`  97`  `    out.fileName = s.split('/').pop();`
`  98`  `    return out;`
`  99`  `}`

---

### `loadSubmissions` — lines 102–140

```
function loadSubmissions()
```

#### Explanation

- **Purpose:** Implements `loadSubmissions`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables:** `res`, `graded`, `total`, `pending`, `bp`

#### Line-by-line (this function)

` 102`  ``
` 103`  ``
` 104`  `function loadSubmissions() {`
` 105`  `    fetch('Grading.aspx/GetSubmissions', {`
  - → HTTP request to server WebMethod/ashx.
` 106`  `        method: 'POST',`
` 107`  `        headers: { 'Content-Type': 'application/json' },`
` 108`  `        body: '{}',`
` 109`  `        credentials: 'same-origin'`
` 110`  `    })`
` 111`  `    .then(function (r) { return r.json(); })`
` 112`  `    .then(function (data) {`
` 113`  `        var res = data.d || data;`
` 114`  `        if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }`
` 115`  `        if (!res.success) {`
` 116`  `            document.getElementById('studentList').innerHTML =`
  - → Get HTML element by id.
` 117`  `            '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';`
  - → Encode text to reduce XSS risk.
` 118`  `            return;`
` 119`  `        }`
` 120`  `        submissions = res.submissions || [];`
` 121`  `        var graded = res.gradedCount || 0;`
` 122`  `        var total = res.totalCount || submissions.length;`
` 123`  `        var pending = 0;`
` 124`  `        submissions.forEach(function (s) { if (!s.isGraded) pending++; });`
` 125`  `        var bp = document.getElementById('badgePendingCount');`
  - → Get HTML element by id.
` 126`  `        if (bp) bp.textContent = String(pending);`
` 127`  `        updateProgress(graded, total);`
` 128`  `        filterStudents();`
` 129`  `        if (filtered.length > 0) selectStudent(0);`
` 130`  `        else {`
` 131`  `            currentIndex = -1;`
` 132`  `            document.getElementById('answerPreview').innerHTML =`
  - → Get HTML element by id.
` 133`  `                '<div class="text-muted text-center py-5">No submissions in this filter</div>';`
` 134`  `        }`
` 135`  `    })`
` 136`  `    .catch(function (err) {`
` 137`  `        console.error(err);`
` 138`  `        document.getElementById('studentList').innerHTML = '<div class="text-danger small">Network error</div>';`
  - → Get HTML element by id.
` 139`  `    });`
` 140`  `}`

---

### `updateProgress` — lines 140–146

```
function updateProgress(graded, total)
```

#### Explanation

- **Purpose:** Implements `updateProgress`.
- **Pattern:** Persist changes.
- **Parameters:** `graded, total`
- **Local variables:** `pct`

#### Line-by-line (this function)

` 140`  ``
` 141`  ``
` 142`  `function updateProgress(graded, total) {`
` 143`  `    document.getElementById('lblGradedCount').innerText = graded + '/' + total;`
  - → Get HTML element by id.
` 144`  `    var pct = total > 0 ? (graded / total) * 100 : 0;`
` 145`  `    document.getElementById('gradedBar').style.width = pct + '%';`
  - → Get HTML element by id.
` 146`  `}`

---

### `setStatusFilter` — lines 146–157

```
function setStatusFilter(mode, btn)
```

#### Explanation

- **Purpose:** Implements `setStatusFilter`.
- **Pattern:** Persist changes.
- **Parameters:** `mode, btn`

#### Line-by-line (this function)

` 146`  ``
` 147`  ``
` 148`  `function setStatusFilter(mode, btn) {`
` 149`  `    statusFilter = mode || 'all';`
` 150`  `    document.querySelectorAll('[data-filter]').forEach(function (b) {`
` 151`  `        b.classList.remove('active');`
` 152`  `    });`
` 153`  `    if (btn) btn.classList.add('active');`
` 154`  `    currentIndex = -1;`
` 155`  `    filterStudents();`
` 156`  `    if (filtered.length > 0) selectStudent(0);`
` 157`  `}`

---

### `filterStudents` — lines 157–170

```
function filterStudents()
```

#### Explanation

- **Purpose:** Implements `filterStudents`.
- **Local variables:** `q`

#### Line-by-line (this function)

` 157`  ``
` 158`  ``
` 159`  `function filterStudents() {`
` 160`  `    var q = (document.getElementById('txtSearchStudents').value || '').toLowerCase();`
  - → Get HTML element by id.
` 161`  `    filtered = submissions.filter(function (s) {`
` 162`  `        if (statusFilter === 'pending' && s.isGraded) return false;`
` 163`  `        if (statusFilter === 'graded' && !s.isGraded) return false;`
` 164`  `        return !q ||`
` 165`  `        (s.studentName || '').toLowerCase().indexOf(q) >= 0 ||`
` 166`  `        (s.assignmentTitle || '').toLowerCase().indexOf(q) >= 0 ||`
` 167`  `        (s.courseName || '').toLowerCase().indexOf(q) >= 0;`
` 168`  `    });`
` 169`  `    renderStudentList();`
` 170`  `}`

---

### `exportGradesCsv` — lines 170–202

```
function exportGradesCsv()
```

#### Explanation

- **Purpose:** Implements `exportGradesCsv`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables:** `res`, `blob`, `a`

#### Line-by-line (this function)

` 170`  ``
` 171`  ``
` 172`  `function exportGradesCsv() {`
  - → CSV export.
` 173`  `    fetch('Grading.aspx/ExportGradesCsv', {`
  - → HTTP request to server WebMethod/ashx.
` 174`  `        method: 'POST',`
` 175`  `        headers: { 'Content-Type': 'application/json' },`
` 176`  `        body: JSON.stringify({ cid: 0 }),`
  - → JS object ↔ JSON text.
` 177`  `        credentials: 'same-origin'`
` 178`  `    })`
` 179`  `    .then(function (r) { return r.json(); })`
` 180`  `    .then(function (data) {`
` 181`  `        var res = data.d || data;`
` 182`  `        if (res.notAuthenticated || res.csrf) {`
  - → CSRF anti-forgery protection.
` 183`  `            alert(res.message || 'Please refresh and sign in again.');`
` 184`  `            return;`
` 185`  `        }`
` 186`  `        if (!res.success) {`
` 187`  `            alert(res.message || 'Export failed');`
` 188`  `            return;`
` 189`  `        }`
` 190`  `        var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });`
  - → CSV export.
` 191`  `        var a = document.createElement('a');`
` 192`  `        a.href = URL.createObjectURL(blob);`
` 193`  `        a.download = res.fileName || 'grades.csv';`
  - → CSV export.
` 194`  `        document.body.appendChild(a);`
` 195`  `        a.click();`
` 196`  `        setTimeout(function () {`
` 197`  `            URL.revokeObjectURL(a.href);`
` 198`  `            a.remove();`
` 199`  `        }, 500);`
` 200`  `    })`
` 201`  `    .catch(function () { alert('Network error exporting grades.'); });`
` 202`  `}`

---

### `renderStudentList` — lines 202–232

```
function renderStudentList()
```

#### Explanation

- **Purpose:** Implements `renderStudentList`.
- **Local variables:** `box`, `colors`, `div`, `parsed`, `fileIcon`, `scoreHtml`

#### Line-by-line (this function)

` 202`  ``
` 203`  ``
` 204`  `function renderStudentList() {`
` 205`  `    var box = document.getElementById('studentList');`
  - → Get HTML element by id.
` 206`  `    box.innerHTML = '';`
  - → Update page HTML.
` 207`  `    if (filtered.length === 0) {`
` 208`  `        box.innerHTML = '<div class="text-muted small py-3 text-center">No submissions</div>';`
  - → Update page HTML.
` 209`  `        return;`
` 210`  `    }`
` 211`  `    var colors = ['#f59e0b', '#3b82f6', '#10b981', '#8b5cf6', '#ec4899'];`
` 212`  `    filtered.forEach(function (s, i) {`
` 213`  `        var div = document.createElement('div');`
` 214`  `        div.className = 'student-row' + (i === currentIndex ? ' active' : '');`
` 215`  `        div.onclick = function () { selectStudent(i); };`
` 216`  `        var parsed = parseAnswerContent(s.studentAnswer || s.content || '');`
` 217`  `        var fileIcon = parsed.file`
` 218`  `        ? '<i class="fa-solid fa-paperclip text-muted me-1" style="font-size:.7rem;"></i>'`
` 219`  `        : '';`
` 220`  `        var scoreHtml = s.isGraded`
` 221`  `        ? '<span class="text-success small fw-semibold">' + s.markScore + '/' + s.maxScore + '</span>'`
` 222`  `        : '<span class="pending-dot"></span>';`
` 223`  `        div.innerHTML =`
  - → Update page HTML.
` 224`  `        '<div class="student-avatar me-2" style="background:' + colors[i % colors.length] + '">' +`
` 225`  `        escapeHtml(s.initials || '?') + '</div>' +`
  - → Encode text to reduce XSS risk.
` 226`  `        '<div class="flex-grow-1 overflow-hidden">' +`
` 227`  `        '<div class="fw-semibold small text-truncate">' + fileIcon + escapeHtml(s.studentName) + '</div>' +`
  - → Encode text to reduce XSS risk.
` 228`  `        '<div class="text-muted" style="font-size:0.7rem;"><i class="fa-regular fa-clock me-1"></i>' +`
` 229`  `        escapeHtml(s.timeText || '') + '</div></div>' + scoreHtml;`
  - → Encode text to reduce XSS risk.
` 230`  `        box.appendChild(div);`
` 231`  `    });`
` 232`  `}`

---

### `selectStudent` — lines 232–308

```
function selectStudent(index)
```

#### Explanation

- **Purpose:** Implements `selectStudent`.
- **Parameters:** `index`
- **Local variables:** `s`, `raw`, `parsed`, `preview`, `btnDl`, `html`, `view`, `dl`, `kind`, `label`, `max`

#### Line-by-line (this function)

` 232`  ``
` 233`  ``
` 234`  `function selectStudent(index) {`
` 235`  `    if (index < 0 || index >= filtered.length) return;`
` 236`  `    currentIndex = index;`
` 237`  `    var s = filtered[index];`
` 238`  `    renderStudentList();`
` 239`  ``
` 240`  `    document.getElementById('lblAssignmentTitle').innerText = s.assignmentTitle || 'Submission';`
  - → Get HTML element by id.
` 241`  `    document.getElementById('lblAssignmentMeta').innerText =`
  - → Get HTML element by id.
` 242`  `    (s.courseName || '') + ' · ' + (s.studentName || '') +`
` 243`  `    (s.requireFile ? ' · File required' : '');`
` 244`  ``
` 245`  `    document.getElementById('previewAvatar').innerText = s.initials || '?';`
  - → Get HTML element by id.
` 246`  `    document.getElementById('previewName').innerText = (s.studentName || '') + "'s Submission";`
  - → Get HTML element by id.
` 247`  ``
` 248`  `    var raw = s.studentAnswer || s.content || '';`
` 249`  `    var parsed = parseAnswerContent(raw);`
` 250`  `    // Prefer explicit fields from API if present`
` 251`  `    if (s.fileUrl) parsed.file = s.fileUrl;`
` 252`  `    if (s.fileName) parsed.fileName = s.fileName;`
` 253`  `    if (s.answerText != null && s.answerText !== '') parsed.text = s.answerText;`
` 254`  ``
` 255`  `    var preview = document.getElementById('answerPreview');`
  - → Get HTML element by id.
` 256`  `    var btnDl = document.getElementById('btnDownload');`
  - → Get HTML element by id.
` 257`  `    var html = '';`
` 258`  ``
` 259`  `    if (parsed.file) {`
` 260`  `        var view = resolveMediaUrl(parsed.file, false);`
` 261`  `        var dl = resolveMediaUrl(parsed.file, true);`
` 262`  `        var kind = mediaKind((parsed.fileName || '') + ' ' + parsed.file);`
` 263`  `        var label = parsed.fileName || parsed.file.split('/').pop() || 'file';`
` 264`  ``
` 265`  `        html += '<div class="file-chip mb-2 d-flex align-items-center gap-2 p-2 border rounded bg-light">' +`
` 266`  `        '<i class="fa-regular fa-file-lines"></i>' +`
` 267`  `        '<span class="small text-truncate flex-grow-1">' + escapeHtml(label) + '</span>' +`
  - → Encode text to reduce XSS risk.
` 268`  `        '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeAttr(view) + '" target="_blank">Open</a>' +`
` 269`  `        '</div>';`
` 270`  ``
` 271`  `        if (kind === 'pdf') {`
` 272`  `            html += '<iframe src="' + escapeAttr(view) + '#toolbar=1" title="PDF preview" ' +`
` 273`  `            'style="width:100%;height:480px;border:1px solid #e5e7eb;border-radius:10px;background:#fff;"></iframe>';`
` 274`  `        } else if (kind === 'image') {`
` 275`  `            html += '<img src="' + escapeAttr(view) + '" class="img-fluid rounded border" alt="" style="max-height:480px;" />';`
` 276`  `        } else if (kind === 'video') {`
` 277`  `            html += '<video controls playsinline class="w-100 rounded" style="max-height:420px;background:#111;" src="' +`
` 278`  `            escapeAttr(view) + '"></video>';`
` 279`  `        } else {`
` 280`  `            html += '<div class="text-muted small text-center py-4">Preview not available - use Open / Download.</div>';`
` 281`  `        }`
` 282`  ``
` 283`  `        btnDl.href = dl;`
` 284`  `        btnDl.style.display = 'inline-flex';`
` 285`  `    } else {`
` 286`  `        btnDl.style.display = 'none';`
` 287`  `    }`
` 288`  ``
` 289`  `    if (parsed.text) {`
` 290`  `        html += '<div class="mt-3"><div class="fw-semibold small text-muted mb-1">Written answer</div>' +`
` 291`  `        '<pre class="small p-3 bg-light rounded" style="white-space:pre-wrap;max-height:240px;overflow:auto;">' +`
` 292`  `        escapeHtml(parsed.text) + '</pre></div>';`
  - → Encode text to reduce XSS risk.
` 293`  `    }`
` 294`  ``
` 295`  `    if (!parsed.file && !parsed.text) {`
` 296`  `        html = '<div class="text-muted text-center py-5">No answer text or file</div>';`
` 297`  `    }`
` 298`  ``
` 299`  `    preview.innerHTML = html;`
  - → Update page HTML.
` 300`  ``
` 301`  `    var max = s.maxScore || 100;`
` 302`  `    document.getElementById('lblMaxScore').innerText = '/ ' + max;`
  - → Get HTML element by id.
` 303`  `    document.getElementById('txtGradeScore').max = max;`
  - → Get HTML element by id.
` 304`  `    document.getElementById('txtGradeScore').value = s.isGraded ? s.markScore : 0;`
  - → Get HTML element by id.
` 305`  `    document.getElementById('txtFeedback').value = s.review || '';`
  - → Get HTML element by id.
` 306`  `    updateTotalDisplay();`
` 307`  `    document.getElementById('gradeError').style.display = 'none';`
  - → Get HTML element by id.
` 308`  `}`

---

### `updateTotalDisplay` — lines 308–314

```
function updateTotalDisplay()
```

#### Explanation

- **Purpose:** Implements `updateTotalDisplay`.
- **Pattern:** Persist changes.
- **Local variables:** `max`, `score`

#### Line-by-line (this function)

` 308`  ``
` 309`  ``
` 310`  `function updateTotalDisplay() {`
` 311`  `    var max = (filtered[currentIndex] && filtered[currentIndex].maxScore) || 100;`
` 312`  `    var score = parseFloat(document.getElementById('txtGradeScore').value) || 0;`
  - → Get HTML element by id.
` 313`  `    document.getElementById('lblTotalScore').innerText = score + '/' + max;`
  - → Get HTML element by id.
` 314`  `}`

---

### `navStudent` — lines 314–322

```
function navStudent(delta)
```

#### Explanation

- **Purpose:** Implements `navStudent`.
- **Parameters:** `delta`
- **Local variables:** `next`

#### Line-by-line (this function)

` 314`  ``
` 315`  ``
` 316`  `function navStudent(delta) {`
` 317`  `    if (filtered.length === 0) return;`
` 318`  `    var next = currentIndex + delta;`
` 319`  `    if (next < 0) next = 0;`
` 320`  `    if (next >= filtered.length) next = filtered.length - 1;`
` 321`  `    selectStudent(next);`
` 322`  `}`

---

### `submitGrade` — lines 322–358

```
function submitGrade()
```

#### Explanation

- **Purpose:** Implements `submitGrade`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables:** `s`, `score`, `review`, `err`, `res`

#### Line-by-line (this function)

` 322`  ``
` 323`  ``
` 324`  `function submitGrade() {`
` 325`  `    if (currentIndex < 0 || !filtered[currentIndex]) return;`
` 326`  `    var s = filtered[currentIndex];`
` 327`  `    var score = parseFloat(document.getElementById('txtGradeScore').value);`
  - → Get HTML element by id.
` 328`  `    var review = document.getElementById('txtFeedback').value.trim();`
  - → Get HTML element by id.
` 329`  `    var err = document.getElementById('gradeError');`
  - → Get HTML element by id.
` 330`  `    err.style.display = 'none';`
` 331`  ``
` 332`  `    if (isNaN(score) || score < 0) {`
` 333`  `        err.innerText = 'Enter a valid score.';`
` 334`  `        err.style.display = 'block';`
` 335`  `        return;`
` 336`  `    }`
` 337`  ``
` 338`  `    fetch('Grading.aspx/SaveGrade', {`
  - → HTTP request to server WebMethod/ashx.
` 339`  `        method: 'POST',`
` 340`  `        headers: { 'Content-Type': 'application/json' },`
` 341`  `        body: JSON.stringify({ sid: s.sid, score: score, review: review }),`
  - → JS object ↔ JSON text.
` 342`  `        credentials: 'same-origin'`
` 343`  `    })`
` 344`  `    .then(function (r) { return r.json(); })`
` 345`  `    .then(function (data) {`
` 346`  `        var res = data.d || data;`
` 347`  `        if (res.success) loadSubmissions();`
` 348`  `        else {`
` 349`  `            err.innerText = res.message || 'Failed to save grade.';`
` 350`  `            err.style.display = 'block';`
` 351`  `        }`
` 352`  `    })`
` 353`  `    .catch(function (e) {`
` 354`  `        err.innerText = 'Network error.';`
` 355`  `        err.style.display = 'block';`
` 356`  `        console.error(e);`
` 357`  `    });`
` 358`  `}`

---

### `escapeHtml` — lines 358–366

```
function escapeHtml(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtml`.
- **Parameters:** `str`

#### Line-by-line (this function)

` 358`  ``
` 359`  ``
` 360`  `function escapeHtml(str) {`
  - → Encode text to reduce XSS risk.
` 361`  `    if (str == null) return '';`
` 362`  `    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');`
` 363`  `}`
` 364`  `function escapeAttr(str) {`
` 365`  `    return escapeHtml(str).replace(/'/g, '&#39;');`
  - → Encode text to reduce XSS risk.
` 366`  `}`

---

### `escapeAttr` — lines 363–366

```
function escapeAttr(str)
```

#### Explanation

- **Purpose:** Implements `escapeAttr`.
- **Parameters:** `str`

#### Line-by-line (this function)

` 363`  ``
` 364`  `function escapeAttr(str) {`
` 365`  `    return escapeHtml(str).replace(/'/g, '&#39;');`
  - → Encode text to reduce XSS risk.
` 366`  `}`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `/* Grading page - CWSubmissions + CWMarkings; PDF/image/video preview for file answers */`
`   2`  ``
`   3`  `let submissions = [];`
`   4`  `let filtered = [];`
`   5`  `let currentIndex = -1;`
`   6`  `let statusFilter = 'all'; // all | pending | graded`
`   7`  ``
`   8`  `document.addEventListener('DOMContentLoaded', function () {`
  - → DOM event handler.
`   9`  `    // Deep-link: Grading.aspx?filter=pending`
`  10`  `    try {`
  - → Error handling block.
`  11`  `        var params = new URLSearchParams(window.location.search || '');`
`  12`  `        var f = (params.get('filter') || '').toLowerCase();`
`  13`  `        if (f === 'pending' || f === 'graded' || f === 'all') {`
`  14`  `            statusFilter = f;`
`  15`  `            var btn = document.querySelector('[data-filter="' + f + '"]');`
`  16`  `            if (btn) {`
`  17`  `                document.querySelectorAll('[data-filter]').forEach(function (b) {`
`  18`  `                    b.classList.remove('active');`
`  19`  `                });`
`  20`  `                btn.classList.add('active');`
`  21`  `            }`
`  22`  `        }`
`  23`  `    } catch (e) { }`
`  24`  `    loadSubmissions();`
`  25`  `});`
`  26`  ``
`  27`  `function mediaAppRoot() {`
`  28`  `    var p = window.location.pathname || '';`
`  29`  `    var i = p.toLowerCase().indexOf('/pages/');`
`  30`  `    if (i > 0) return p.substring(0, i);`
`  31`  `    return '';`
`  32`  `}`
`  33`  ``
`  34`  `function resolveMediaUrl(raw, forDownload) {`
`  35`  `    if (!raw) return '';`
`  36`  `    var u = String(raw).trim();`
`  37`  `    if (/^https?:\/\//i.test(u) && u.indexOf('/Uploads/') < 0 && u.indexOf('Media.ashx') < 0 && u.indexOf('Uploads/') < 0)`
`  38`  `    return u;`
`  39`  `    if (u.indexOf('Media.ashx') >= 0) {`
`  40`  `        if (forDownload && u.indexOf('dl=1') < 0) return u + (u.indexOf('?') >= 0 ? '&' : '?') + 'dl=1';`
`  41`  `        return u;`
`  42`  `    }`
`  43`  `    try {`
  - → Error handling block.
`  44`  `        if (/^https?:\/\//i.test(u)) {`
`  45`  `        var a = document.createElement('a');`
`  46`  `        a.href = u;`
`  47`  `        u = a.pathname || u;`
`  48`  `    }`
`  49`  `} catch (e) { }`
`  50`  `var path = u.replace(/\\/g, '/');`
`  51`  `var idx = path.toLowerCase().indexOf('/uploads/');`
`  52`  `if (idx >= 0) path = path.substring(idx + 1);`
`  53`  `if (path.indexOf('~/') === 0) path = path.substring(2);`
`  54`  `path = path.replace(/^\/+/, '');`
`  55`  `if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);`
`  56`  `if (!path) return '';`
`  57`  `if (path.indexOf('/') < 0) path = 'CourseSubmissions/' + path;`
`  58`  `var url = mediaAppRoot() + '/Media.ashx?f=' + encodeURIComponent(path);`
`  59`  `if (forDownload) url += '&dl=1';`
`  60`  `return url;`
`  61`  `}`
`  62`  ``
`  63`  `function mediaKind(s) {`
`  64`  `    s = (s || '').toLowerCase();`
`  65`  `    if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';`
`  66`  `    if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';`
`  67`  `    if (/\.pdf(\?|$)/.test(s)) return 'pdf';`
`  68`  `    return 'file';`
`  69`  `}`
`  70`  ``
`  71`  `/** Parse CWSubmissions.Content: plain text or JSON {text,file,fileName} */`
`  72`  `function parseAnswerContent(raw) {`
`  73`  `    var out = { text: '', file: '', fileName: '' };`
`  74`  `    if (raw == null) return out;`
`  75`  `    var s = String(raw).trim();`
`  76`  `    if (!s) return out;`
`  77`  `    if (s.charAt(0) === '{') {`
`  78`  `        try {`
  - → Error handling block.
`  79`  `            var o = JSON.parse(s);`
  - → JS object ↔ JSON text.
`  80`  `            out.text = o.text || o.Text || '';`
`  81`  `            out.file = o.file || o.fileUrl || o.FileUrl || o.url || '';`
`  82`  `            out.fileName = o.fileName || o.FileName || '';`
`  83`  `            if (!out.fileName && out.file) out.fileName = out.file.split('/').pop();`
`  84`  `            return out;`
`  85`  `        } catch (e) { /* fall through */ }`
`  86`  `    }`
`  87`  `    // marker form`
`  88`  `    var m = s.match(/<<<FILE>>>([\s\S]*?)<<<ENDFILE>>>/i);`
`  89`  `    if (m) {`
`  90`  `        out.file = m[1].trim();`
`  91`  `        out.text = s.replace(m[0], '').trim();`
`  92`  `        out.fileName = out.file.split('/').pop();`
`  93`  `        return out;`
`  94`  `    }`
`  95`  `    if (/uploads\//i.test(s) || /Media\.ashx/i.test(s) || /\.(pdf|docx?|pptx?|png|jpe?g|mp4)(\?|$)/i.test(s)) {`
`  96`  `    out.file = s;`
`  97`  `    out.fileName = s.split('/').pop();`
`  98`  `    return out;`
`  99`  `}`
` 100`  `out.text = s;`
` 101`  `return out;`
` 102`  `}`
` 103`  ``
` 104`  `function loadSubmissions() {`
` 105`  `    fetch('Grading.aspx/GetSubmissions', {`
  - → HTTP request to server WebMethod/ashx.
` 106`  `        method: 'POST',`
` 107`  `        headers: { 'Content-Type': 'application/json' },`
` 108`  `        body: '{}',`
` 109`  `        credentials: 'same-origin'`
` 110`  `    })`
` 111`  `    .then(function (r) { return r.json(); })`
` 112`  `    .then(function (data) {`
` 113`  `        var res = data.d || data;`
` 114`  `        if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }`
` 115`  `        if (!res.success) {`
` 116`  `            document.getElementById('studentList').innerHTML =`
  - → Get HTML element by id.
` 117`  `            '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';`
  - → Encode text to reduce XSS risk.
` 118`  `            return;`
` 119`  `        }`
` 120`  `        submissions = res.submissions || [];`
` 121`  `        var graded = res.gradedCount || 0;`
` 122`  `        var total = res.totalCount || submissions.length;`
` 123`  `        var pending = 0;`
` 124`  `        submissions.forEach(function (s) { if (!s.isGraded) pending++; });`
` 125`  `        var bp = document.getElementById('badgePendingCount');`
  - → Get HTML element by id.
` 126`  `        if (bp) bp.textContent = String(pending);`
` 127`  `        updateProgress(graded, total);`
` 128`  `        filterStudents();`
` 129`  `        if (filtered.length > 0) selectStudent(0);`
` 130`  `        else {`
` 131`  `            currentIndex = -1;`
` 132`  `            document.getElementById('answerPreview').innerHTML =`
  - → Get HTML element by id.
` 133`  `                '<div class="text-muted text-center py-5">No submissions in this filter</div>';`
` 134`  `        }`
` 135`  `    })`
` 136`  `    .catch(function (err) {`
` 137`  `        console.error(err);`
` 138`  `        document.getElementById('studentList').innerHTML = '<div class="text-danger small">Network error</div>';`
  - → Get HTML element by id.
` 139`  `    });`
` 140`  `}`
` 141`  ``
` 142`  `function updateProgress(graded, total) {`
` 143`  `    document.getElementById('lblGradedCount').innerText = graded + '/' + total;`
  - → Get HTML element by id.
` 144`  `    var pct = total > 0 ? (graded / total) * 100 : 0;`
` 145`  `    document.getElementById('gradedBar').style.width = pct + '%';`
  - → Get HTML element by id.
` 146`  `}`
` 147`  ``
` 148`  `function setStatusFilter(mode, btn) {`
` 149`  `    statusFilter = mode || 'all';`
` 150`  `    document.querySelectorAll('[data-filter]').forEach(function (b) {`
` 151`  `        b.classList.remove('active');`
` 152`  `    });`
` 153`  `    if (btn) btn.classList.add('active');`
` 154`  `    currentIndex = -1;`
` 155`  `    filterStudents();`
` 156`  `    if (filtered.length > 0) selectStudent(0);`
` 157`  `}`
` 158`  ``
` 159`  `function filterStudents() {`
` 160`  `    var q = (document.getElementById('txtSearchStudents').value || '').toLowerCase();`
  - → Get HTML element by id.
` 161`  `    filtered = submissions.filter(function (s) {`
` 162`  `        if (statusFilter === 'pending' && s.isGraded) return false;`
` 163`  `        if (statusFilter === 'graded' && !s.isGraded) return false;`
` 164`  `        return !q ||`
` 165`  `        (s.studentName || '').toLowerCase().indexOf(q) >= 0 ||`
` 166`  `        (s.assignmentTitle || '').toLowerCase().indexOf(q) >= 0 ||`
` 167`  `        (s.courseName || '').toLowerCase().indexOf(q) >= 0;`
` 168`  `    });`
` 169`  `    renderStudentList();`
` 170`  `}`
` 171`  ``
` 172`  `function exportGradesCsv() {`
  - → CSV export.
` 173`  `    fetch('Grading.aspx/ExportGradesCsv', {`
  - → HTTP request to server WebMethod/ashx.
` 174`  `        method: 'POST',`
` 175`  `        headers: { 'Content-Type': 'application/json' },`
` 176`  `        body: JSON.stringify({ cid: 0 }),`
  - → JS object ↔ JSON text.
` 177`  `        credentials: 'same-origin'`
` 178`  `    })`
` 179`  `    .then(function (r) { return r.json(); })`
` 180`  `    .then(function (data) {`
` 181`  `        var res = data.d || data;`
` 182`  `        if (res.notAuthenticated || res.csrf) {`
  - → CSRF anti-forgery protection.
` 183`  `            alert(res.message || 'Please refresh and sign in again.');`
` 184`  `            return;`
` 185`  `        }`
` 186`  `        if (!res.success) {`
` 187`  `            alert(res.message || 'Export failed');`
` 188`  `            return;`
` 189`  `        }`
` 190`  `        var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });`
  - → CSV export.
` 191`  `        var a = document.createElement('a');`
` 192`  `        a.href = URL.createObjectURL(blob);`
` 193`  `        a.download = res.fileName || 'grades.csv';`
  - → CSV export.
` 194`  `        document.body.appendChild(a);`
` 195`  `        a.click();`
` 196`  `        setTimeout(function () {`
` 197`  `            URL.revokeObjectURL(a.href);`
` 198`  `            a.remove();`
` 199`  `        }, 500);`
` 200`  `    })`
` 201`  `    .catch(function () { alert('Network error exporting grades.'); });`
` 202`  `}`
` 203`  ``
` 204`  `function renderStudentList() {`
` 205`  `    var box = document.getElementById('studentList');`
  - → Get HTML element by id.
` 206`  `    box.innerHTML = '';`
  - → Update page HTML.
` 207`  `    if (filtered.length === 0) {`
` 208`  `        box.innerHTML = '<div class="text-muted small py-3 text-center">No submissions</div>';`
  - → Update page HTML.
` 209`  `        return;`
` 210`  `    }`
` 211`  `    var colors = ['#f59e0b', '#3b82f6', '#10b981', '#8b5cf6', '#ec4899'];`
` 212`  `    filtered.forEach(function (s, i) {`
` 213`  `        var div = document.createElement('div');`
` 214`  `        div.className = 'student-row' + (i === currentIndex ? ' active' : '');`
` 215`  `        div.onclick = function () { selectStudent(i); };`
` 216`  `        var parsed = parseAnswerContent(s.studentAnswer || s.content || '');`
` 217`  `        var fileIcon = parsed.file`
` 218`  `        ? '<i class="fa-solid fa-paperclip text-muted me-1" style="font-size:.7rem;"></i>'`
` 219`  `        : '';`
` 220`  `        var scoreHtml = s.isGraded`
` 221`  `        ? '<span class="text-success small fw-semibold">' + s.markScore + '/' + s.maxScore + '</span>'`
` 222`  `        : '<span class="pending-dot"></span>';`
` 223`  `        div.innerHTML =`
  - → Update page HTML.
` 224`  `        '<div class="student-avatar me-2" style="background:' + colors[i % colors.length] + '">' +`
` 225`  `        escapeHtml(s.initials || '?') + '</div>' +`
  - → Encode text to reduce XSS risk.
` 226`  `        '<div class="flex-grow-1 overflow-hidden">' +`
` 227`  `        '<div class="fw-semibold small text-truncate">' + fileIcon + escapeHtml(s.studentName) + '</div>' +`
  - → Encode text to reduce XSS risk.
` 228`  `        '<div class="text-muted" style="font-size:0.7rem;"><i class="fa-regular fa-clock me-1"></i>' +`
` 229`  `        escapeHtml(s.timeText || '') + '</div></div>' + scoreHtml;`
  - → Encode text to reduce XSS risk.
` 230`  `        box.appendChild(div);`
` 231`  `    });`
` 232`  `}`
` 233`  ``
` 234`  `function selectStudent(index) {`
` 235`  `    if (index < 0 || index >= filtered.length) return;`
` 236`  `    currentIndex = index;`
` 237`  `    var s = filtered[index];`
` 238`  `    renderStudentList();`
` 239`  ``
` 240`  `    document.getElementById('lblAssignmentTitle').innerText = s.assignmentTitle || 'Submission';`
  - → Get HTML element by id.
` 241`  `    document.getElementById('lblAssignmentMeta').innerText =`
  - → Get HTML element by id.
` 242`  `    (s.courseName || '') + ' · ' + (s.studentName || '') +`
` 243`  `    (s.requireFile ? ' · File required' : '');`
` 244`  ``
` 245`  `    document.getElementById('previewAvatar').innerText = s.initials || '?';`
  - → Get HTML element by id.
` 246`  `    document.getElementById('previewName').innerText = (s.studentName || '') + "'s Submission";`
  - → Get HTML element by id.
` 247`  ``
` 248`  `    var raw = s.studentAnswer || s.content || '';`
` 249`  `    var parsed = parseAnswerContent(raw);`
` 250`  `    // Prefer explicit fields from API if present`
` 251`  `    if (s.fileUrl) parsed.file = s.fileUrl;`
` 252`  `    if (s.fileName) parsed.fileName = s.fileName;`
` 253`  `    if (s.answerText != null && s.answerText !== '') parsed.text = s.answerText;`
` 254`  ``
` 255`  `    var preview = document.getElementById('answerPreview');`
  - → Get HTML element by id.
` 256`  `    var btnDl = document.getElementById('btnDownload');`
  - → Get HTML element by id.
` 257`  `    var html = '';`
` 258`  ``
` 259`  `    if (parsed.file) {`
` 260`  `        var view = resolveMediaUrl(parsed.file, false);`
` 261`  `        var dl = resolveMediaUrl(parsed.file, true);`
` 262`  `        var kind = mediaKind((parsed.fileName || '') + ' ' + parsed.file);`
` 263`  `        var label = parsed.fileName || parsed.file.split('/').pop() || 'file';`
` 264`  ``
` 265`  `        html += '<div class="file-chip mb-2 d-flex align-items-center gap-2 p-2 border rounded bg-light">' +`
` 266`  `        '<i class="fa-regular fa-file-lines"></i>' +`
` 267`  `        '<span class="small text-truncate flex-grow-1">' + escapeHtml(label) + '</span>' +`
  - → Encode text to reduce XSS risk.
` 268`  `        '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeAttr(view) + '" target="_blank">Open</a>' +`
` 269`  `        '</div>';`
` 270`  ``
` 271`  `        if (kind === 'pdf') {`
` 272`  `            html += '<iframe src="' + escapeAttr(view) + '#toolbar=1" title="PDF preview" ' +`
` 273`  `            'style="width:100%;height:480px;border:1px solid #e5e7eb;border-radius:10px;background:#fff;"></iframe>';`
` 274`  `        } else if (kind === 'image') {`
` 275`  `            html += '<img src="' + escapeAttr(view) + '" class="img-fluid rounded border" alt="" style="max-height:480px;" />';`
` 276`  `        } else if (kind === 'video') {`
` 277`  `            html += '<video controls playsinline class="w-100 rounded" style="max-height:420px;background:#111;" src="' +`
` 278`  `            escapeAttr(view) + '"></video>';`
` 279`  `        } else {`
` 280`  `            html += '<div class="text-muted small text-center py-4">Preview not available - use Open / Download.</div>';`
` 281`  `        }`
` 282`  ``
` 283`  `        btnDl.href = dl;`
` 284`  `        btnDl.style.display = 'inline-flex';`
` 285`  `    } else {`
` 286`  `        btnDl.style.display = 'none';`
` 287`  `    }`
` 288`  ``
` 289`  `    if (parsed.text) {`
` 290`  `        html += '<div class="mt-3"><div class="fw-semibold small text-muted mb-1">Written answer</div>' +`
` 291`  `        '<pre class="small p-3 bg-light rounded" style="white-space:pre-wrap;max-height:240px;overflow:auto;">' +`
` 292`  `        escapeHtml(parsed.text) + '</pre></div>';`
  - → Encode text to reduce XSS risk.
` 293`  `    }`
` 294`  ``
` 295`  `    if (!parsed.file && !parsed.text) {`
` 296`  `        html = '<div class="text-muted text-center py-5">No answer text or file</div>';`
` 297`  `    }`
` 298`  ``
` 299`  `    preview.innerHTML = html;`
  - → Update page HTML.
` 300`  ``
` 301`  `    var max = s.maxScore || 100;`
` 302`  `    document.getElementById('lblMaxScore').innerText = '/ ' + max;`
  - → Get HTML element by id.
` 303`  `    document.getElementById('txtGradeScore').max = max;`
  - → Get HTML element by id.
` 304`  `    document.getElementById('txtGradeScore').value = s.isGraded ? s.markScore : 0;`
  - → Get HTML element by id.
` 305`  `    document.getElementById('txtFeedback').value = s.review || '';`
  - → Get HTML element by id.
` 306`  `    updateTotalDisplay();`
` 307`  `    document.getElementById('gradeError').style.display = 'none';`
  - → Get HTML element by id.
` 308`  `}`
` 309`  ``
` 310`  `function updateTotalDisplay() {`
` 311`  `    var max = (filtered[currentIndex] && filtered[currentIndex].maxScore) || 100;`
` 312`  `    var score = parseFloat(document.getElementById('txtGradeScore').value) || 0;`
  - → Get HTML element by id.
` 313`  `    document.getElementById('lblTotalScore').innerText = score + '/' + max;`
  - → Get HTML element by id.
` 314`  `}`
` 315`  ``
` 316`  `function navStudent(delta) {`
` 317`  `    if (filtered.length === 0) return;`
` 318`  `    var next = currentIndex + delta;`
` 319`  `    if (next < 0) next = 0;`
` 320`  `    if (next >= filtered.length) next = filtered.length - 1;`
` 321`  `    selectStudent(next);`
` 322`  `}`
` 323`  ``
` 324`  `function submitGrade() {`
` 325`  `    if (currentIndex < 0 || !filtered[currentIndex]) return;`
` 326`  `    var s = filtered[currentIndex];`
` 327`  `    var score = parseFloat(document.getElementById('txtGradeScore').value);`
  - → Get HTML element by id.
` 328`  `    var review = document.getElementById('txtFeedback').value.trim();`
  - → Get HTML element by id.
` 329`  `    var err = document.getElementById('gradeError');`
  - → Get HTML element by id.
` 330`  `    err.style.display = 'none';`
` 331`  ``
` 332`  `    if (isNaN(score) || score < 0) {`
` 333`  `        err.innerText = 'Enter a valid score.';`
` 334`  `        err.style.display = 'block';`
` 335`  `        return;`
` 336`  `    }`
` 337`  ``
` 338`  `    fetch('Grading.aspx/SaveGrade', {`
  - → HTTP request to server WebMethod/ashx.
` 339`  `        method: 'POST',`
` 340`  `        headers: { 'Content-Type': 'application/json' },`
` 341`  `        body: JSON.stringify({ sid: s.sid, score: score, review: review }),`
  - → JS object ↔ JSON text.
` 342`  `        credentials: 'same-origin'`
` 343`  `    })`
` 344`  `    .then(function (r) { return r.json(); })`
` 345`  `    .then(function (data) {`
` 346`  `        var res = data.d || data;`
` 347`  `        if (res.success) loadSubmissions();`
` 348`  `        else {`
` 349`  `            err.innerText = res.message || 'Failed to save grade.';`
` 350`  `            err.style.display = 'block';`
` 351`  `        }`
` 352`  `    })`
` 353`  `    .catch(function (e) {`
` 354`  `        err.innerText = 'Network error.';`
` 355`  `        err.style.display = 'block';`
` 356`  `        console.error(e);`
` 357`  `    });`
` 358`  `}`
` 359`  ``
` 360`  `function escapeHtml(str) {`
  - → Encode text to reduce XSS risk.
` 361`  `    if (str == null) return '';`
` 362`  `    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');`
` 363`  `}`
` 364`  `function escapeAttr(str) {`
` 365`  `    return escapeHtml(str).replace(/'/g, '&#39;');`
  - → Encode text to reduce XSS risk.
` 366`  `}`

## Source snapshot (raw)

```javascript
/* Grading page - CWSubmissions + CWMarkings; PDF/image/video preview for file answers */

let submissions = [];
let filtered = [];
let currentIndex = -1;
let statusFilter = 'all'; // all | pending | graded

document.addEventListener('DOMContentLoaded', function () {
    // Deep-link: Grading.aspx?filter=pending
    try {
        var params = new URLSearchParams(window.location.search || '');
        var f = (params.get('filter') || '').toLowerCase();
        if (f === 'pending' || f === 'graded' || f === 'all') {
            statusFilter = f;
            var btn = document.querySelector('[data-filter="' + f + '"]');
            if (btn) {
                document.querySelectorAll('[data-filter]').forEach(function (b) {
                    b.classList.remove('active');
                });
                btn.classList.add('active');
            }
        }
    } catch (e) { }
    loadSubmissions();
});

function mediaAppRoot() {
    var p = window.location.pathname || '';
    var i = p.toLowerCase().indexOf('/pages/');
    if (i > 0) return p.substring(0, i);
    return '';
}

function resolveMediaUrl(raw, forDownload) {
    if (!raw) return '';
    var u = String(raw).trim();
    if (/^https?:\/\//i.test(u) && u.indexOf('/Uploads/') < 0 && u.indexOf('Media.ashx') < 0 && u.indexOf('Uploads/') < 0)
    return u;
    if (u.indexOf('Media.ashx') >= 0) {
        if (forDownload && u.indexOf('dl=1') < 0) return u + (u.indexOf('?') >= 0 ? '&' : '?') + 'dl=1';
        return u;
    }
    try {
        if (/^https?:\/\//i.test(u)) {
        var a = document.createElement('a');
        a.href = u;
        u = a.pathname || u;
    }
} catch (e) { }
var path = u.replace(/\\/g, '/');
var idx = path.toLowerCase().indexOf('/uploads/');
if (idx >= 0) path = path.substring(idx + 1);
if (path.indexOf('~/') === 0) path = path.substring(2);
path = path.replace(/^\/+/, '');
if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);
if (!path) return '';
if (path.indexOf('/') < 0) path = 'CourseSubmissions/' + path;
var url = mediaAppRoot() + '/Media.ashx?f=' + encodeURIComponent(path);
if (forDownload) url += '&dl=1';
return url;
}

function mediaKind(s) {
    s = (s || '').toLowerCase();
    if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';
    if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';
    if (/\.pdf(\?|$)/.test(s)) return 'pdf';
    return 'file';
}

/** Parse CWSubmissions.Content: plain text or JSON {text,file,fileName} */
function parseAnswerContent(raw) {
    var out = { text: '', file: '', fileName: '' };
    if (raw == null) return out;
    var s = String(raw).trim();
    if (!s) return out;
    if (s.charAt(0) === '{') {
        try {
            var o = JSON.parse(s);
            out.text = o.text || o.Text || '';
            out.file = o.file || o.fileUrl || o.FileUrl || o.url || '';
            out.fileName = o.fileName || o.FileName || '';
            if (!out.fileName && out.file) out.fileName = out.file.split('/').pop();
            return out;
        } catch (e) { /* fall through */ }
    }
    // marker form
    var m = s.match(/<<<FILE>>>([\s\S]*?)<<<ENDFILE>>>/i);
    if (m) {
        out.file = m[1].trim();
        out.text = s.replace(m[0], '').trim();
        out.fileName = out.file.split('/').pop();
        return out;
    }
    if (/uploads\//i.test(s) || /Media\.ashx/i.test(s) || /\.(pdf|docx?|pptx?|png|jpe?g|mp4)(\?|$)/i.test(s)) {
    out.file = s;
    out.fileName = s.split('/').pop();
    return out;
}
out.text = s;
return out;
}

function loadSubmissions() {
    fetch('Grading.aspx/GetSubmissions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: '{}',
        credentials: 'same-origin'
    })
    .then(function (r) { return r.json(); })
    .then(function (data) {
        var res = data.d || data;
        if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }
        if (!res.success) {
            document.getElementById('studentList').innerHTML =
            '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';
            return;
        }
        submissions = res.submissions || [];
        var graded = res.gradedCount || 0;
        var total = res.totalCount || submissions.length;
        var pending = 0;
        submissions.forEach(function (s) { if (!s.isGraded) pending++; });
        var bp = document.getElementById('badgePendingCount');
        if (bp) bp.textContent = String(pending);
        updateProgress(graded, total);
        filterStudents();
        if (filtered.length > 0) selectStudent(0);
        else {
            currentIndex = -1;
            document.getElementById('answerPreview').innerHTML =
                '<div class="text-muted text-center py-5">No submissions in this filter</div>';
        }
    })
    .catch(function (err) {
        console.error(err);
        document.getElementById('studentList').innerHTML = '<div class="text-danger small">Network error</div>';
    });
}

function updateProgress(graded, total) {
    document.getElementById('lblGradedCount').innerText = graded + '/' + total;
    var pct = total > 0 ? (graded / total) * 100 : 0;
    document.getElementById('gradedBar').style.width = pct + '%';
}

function setStatusFilter(mode, btn) {
    statusFilter = mode || 'all';
    document.querySelectorAll('[data-filter]').forEach(function (b) {
        b.classList.remove('active');
    });
    if (btn) btn.classList.add('active');
    currentIndex = -1;
    filterStudents();
    if (filtered.length > 0) selectStudent(0);
}

function filterStudents() {
    var q = (document.getElementById('txtSearchStudents').value || '').toLowerCase();
    filtered = submissions.filter(function (s) {
        if (statusFilter === 'pending' && s.isGraded) return false;
        if (statusFilter === 'graded' && !s.isGraded) return false;
        return !q ||
        (s.studentName || '').toLowerCase().indexOf(q) >= 0 ||
        (s.assignmentTitle || '').toLowerCase().indexOf(q) >= 0 ||
        (s.courseName || '').toLowerCase().indexOf(q) >= 0;
    });
    renderStudentList();
}

function exportGradesCsv() {
    fetch('Grading.aspx/ExportGradesCsv', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cid: 0 }),
        credentials: 'same-origin'
    })
    .then(function (r) { return r.json(); })
    .then(function (data) {
        var res = data.d || data;
        if (res.notAuthenticated || res.csrf) {
            alert(res.message || 'Please refresh and sign in again.');
            return;
        }
        if (!res.success) {
            alert(res.message || 'Export failed');
            return;
        }
        var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });
        var a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = res.fileName || 'grades.csv';
        document.body.appendChild(a);
        a.click();
        setTimeout(function () {
            URL.revokeObjectURL(a.href);
            a.remove();
        }, 500);
    })
    .catch(function () { alert('Network error exporting grades.'); });
}

function renderStudentList() {
    var box = document.getElementById('studentList');
    box.innerHTML = '';
    if (filtered.length === 0) {
        box.innerHTML = '<div class="text-muted small py-3 text-center">No submissions</div>';
        return;
    }
    var colors = ['#f59e0b', '#3b82f6', '#10b981', '#8b5cf6', '#ec4899'];
    filtered.forEach(function (s, i) {
        var div = document.createElement('div');
        div.className = 'student-row' + (i === currentIndex ? ' active' : '');
        div.onclick = function () { selectStudent(i); };
        var parsed = parseAnswerContent(s.studentAnswer || s.content || '');
        var fileIcon = parsed.file
        ? '<i class="fa-solid fa-paperclip text-muted me-1" style="font-size:.7rem;"></i>'
        : '';
        var scoreHtml = s.isGraded
        ? '<span class="text-success small fw-semibold">' + s.markScore + '/' + s.maxScore + '</span>'
        : '<span class="pending-dot"></span>';
        div.innerHTML =
        '<div class="student-avatar me-2" style="background:' + colors[i % colors.length] + '">' +
        escapeHtml(s.initials || '?') + '</div>' +
        '<div class="flex-grow-1 overflow-hidden">' +
        '<div class="fw-semibold small text-truncate">' + fileIcon + escapeHtml(s.studentName) + '</div>' +
        '<div class="text-muted" style="font-size:0.7rem;"><i class="fa-regular fa-clock me-1"></i>' +
        escapeHtml(s.timeText || '') + '</div></div>' + scoreHtml;
        box.appendChild(div);
    });
}

function selectStudent(index) {
    if (index < 0 || index >= filtered.length) return;
    currentIndex = index;
    var s = filtered[index];
    renderStudentList();

    document.getElementById('lblAssignmentTitle').innerText = s.assignmentTitle || 'Submission';
    document.getElementById('lblAssignmentMeta').innerText =
    (s.courseName || '') + ' · ' + (s.studentName || '') +
    (s.requireFile ? ' · File required' : '');

    document.getElementById('previewAvatar').innerText = s.initials || '?';
    document.getElementById('previewName').innerText = (s.studentName || '') + "'s Submission";

    var raw = s.studentAnswer || s.content || '';
    var parsed = parseAnswerContent(raw);
    // Prefer explicit fields from API if present
    if (s.fileUrl) parsed.file = s.fileUrl;
    if (s.fileName) parsed.fileName = s.fileName;
    if (s.answerText != null && s.answerText !== '') parsed.text = s.answerText;

    var preview = document.getElementById('answerPreview');
    var btnDl = document.getElementById('btnDownload');
    var html = '';

    if (parsed.file) {
        var view = resolveMediaUrl(parsed.file, false);
        var dl = resolveMediaUrl(parsed.file, true);
        var kind = mediaKind((parsed.fileName || '') + ' ' + parsed.file);
        var label = parsed.fileName || parsed.file.split('/').pop() || 'file';

        html += '<div class="file-chip mb-2 d-flex align-items-center gap-2 p-2 border rounded bg-light">' +
        '<i class="fa-regular fa-file-lines"></i>' +
        '<span class="small text-truncate flex-grow-1">' + escapeHtml(label) + '</span>' +
        '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeAttr(view) + '" target="_blank">Open</a>' +
        '</div>';

        if (kind === 'pdf') {
            html += '<iframe src="' + escapeAttr(view) + '#toolbar=1" title="PDF preview" ' +
            'style="width:100%;height:480px;border:1px solid #e5e7eb;border-radius:10px;background:#fff;"></iframe>';
        } else if (kind === 'image') {
            html += '<img src="' + escapeAttr(view) + '" class="img-fluid rounded border" alt="" style="max-height:480px;" />';
        } else if (kind === 'video') {
            html += '<video controls playsinline class="w-100 rounded" style="max-height:420px;background:#111;" src="' +
            escapeAttr(view) + '"></video>';
        } else {
            html += '<div class="text-muted small text-center py-4">Preview not available - use Open / Download.</div>';
        }

        btnDl.href = dl;
        btnDl.style.display = 'inline-flex';
    } else {
        btnDl.style.display = 'none';
    }

    if (parsed.text) {
        html += '<div class="mt-3"><div class="fw-semibold small text-muted mb-1">Written answer</div>' +
        '<pre class="small p-3 bg-light rounded" style="white-space:pre-wrap;max-height:240px;overflow:auto;">' +
        escapeHtml(parsed.text) + '</pre></div>';
    }

    if (!parsed.file && !parsed.text) {
        html = '<div class="text-muted text-center py-5">No answer text or file</div>';
    }

    preview.innerHTML = html;

    var max = s.maxScore || 100;
    document.getElementById('lblMaxScore').innerText = '/ ' + max;
    document.getElementById('txtGradeScore').max = max;
    document.getElementById('txtGradeScore').value = s.isGraded ? s.markScore : 0;
    document.getElementById('txtFeedback').value = s.review || '';
    updateTotalDisplay();
    document.getElementById('gradeError').style.display = 'none';
}

function updateTotalDisplay() {
    var max = (filtered[currentIndex] && filtered[currentIndex].maxScore) || 100;
    var score = parseFloat(document.getElementById('txtGradeScore').value) || 0;
    document.getElementById('lblTotalScore').innerText = score + '/' + max;
}

function navStudent(delta) {
    if (filtered.length === 0) return;
    var next = currentIndex + delta;
    if (next < 0) next = 0;
    if (next >= filtered.length) next = filtered.length - 1;
    selectStudent(next);
}

function submitGrade() {
    if (currentIndex < 0 || !filtered[currentIndex]) return;
    var s = filtered[currentIndex];
    var score = parseFloat(document.getElementById('txtGradeScore').value);
    var review = document.getElementById('txtFeedback').value.trim();
    var err = document.getElementById('gradeError');
    err.style.display = 'none';

    if (isNaN(score) || score < 0) {
        err.innerText = 'Enter a valid score.';
        err.style.display = 'block';
        return;
    }

    fetch('Grading.aspx/SaveGrade', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sid: s.sid, score: score, review: review }),
        credentials: 'same-origin'
    })
    .then(function (r) { return r.json(); })
    .then(function (data) {
        var res = data.d || data;
        if (res.success) loadSubmissions();
        else {
            err.innerText = res.message || 'Failed to save grade.';
            err.style.display = 'block';
        }
    })
    .catch(function (e) {
        err.innerText = 'Network error.';
        err.style.display = 'block';
        console.error(e);
    });
}

function escapeHtml(str) {
    if (str == null) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function escapeAttr(str) {
    return escapeHtml(str).replace(/'/g, '&#39;');
}

```
