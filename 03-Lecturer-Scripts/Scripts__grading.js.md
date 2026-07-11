# grading.js
**Source:** `Pages/Lecturer/Scripts/grading.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

List submissions for lecturer courses; assign marks and feedback; CSV export.

## File overview

- **Total lines:** 366
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `submissions` | `const/let/var` | Often a collection related to submissions (plural name). |
| `filtered` | `const/let/var` | Holds “filtered” for this scope. |
| `currentIndex` | `const/let/var` | Holds “current Index” for this scope. |
| `statusFilter` | `const/let/var` | Holds “status Filter” for this scope. |
| `params` | `const/let/var` | Often a collection related to params (plural name). |
| `f` | `const/let/var` | Holds “f” for this scope. |
| `btn` | `const/let/var` | Button DOM element. |
| `p` | `const/let/var` | Parameter, path, or password fragment depending on context. |
| `i` | `const/let/var` | Loop index (0-based counter in for-loops). |
| `u` | `const/let/var` | Holds “u” for this scope. |
| `a` | `const/let/var` | Holds “a” for this scope. |
| `path` | `const/let/var` | File path under Uploads or URL path. |
| `idx` | `const/let/var` | Holds “idx” for this scope. |
| `url` | `const/let/var` | HTTP URL to media or page. |
| `out` | `const/let/var` | Holds “out” for this scope. |
| `s` | `const/let/var` | String value or submission-related object. |
| `o` | `const/let/var` | Holds “o” for this scope. |
| `m` | `const/let/var` | Holds “m” for this scope. |
| `res` | `const/let/var` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `graded` | `const/let/var` | Holds “graded” for this scope. |
| `total` | `const/let/var` | Sum of points or total items. |
| `pending` | `const/let/var` | Holds “pending” for this scope. |
| `bp` | `const/let/var` | Holds “bp” for this scope. |
| `pct` | `const/let/var` | Holds “pct” for this scope. |
| `q` | `const/let/var` | Search query text, or SQL command text. |
| `blob` | `const/let/var` | Holds “blob” for this scope. |
| `box` | `const/let/var` | Container element for lists/tables. |
| `colors` | `const/let/var` | Often a collection related to colors (plural name). |
| `div` | `const/let/var` | Holds “div” for this scope. |
| `parsed` | `const/let/var` | Holds “parsed” for this scope. |
| `fileIcon` | `const/let/var` | Holds “file Icon” for this scope. |
| `scoreHtml` | `const/let/var` | Holds “score Html” for this scope. |
| `raw` | `const/let/var` | Raw bytes or unprocessed input string. |
| `preview` | `const/let/var` | Holds “preview” for this scope. |
| `btnDl` | `const/let/var` | UI control reference (btn Dl). |
| `html` | `const/let/var` | Holds “html” for this scope. |
| `view` | `const/let/var` | Holds “view” for this scope. |
| `dl` | `const/let/var` | Holds “dl” for this scope. |
| `kind` | `const/let/var` | Upload kind (material/video/thumbnail/submission). |
| `label` | `const/let/var` | otpauth account label (issuer:email). |
| `max` | `const/let/var` | Holds “max” for this scope. |
| `score` | `const/let/var` | Points earned or max points depending on context. |
| `next` | `const/let/var` | Holds “next” for this scope. |
| `review` | `const/let/var` | Holds “review” for this scope. |
| `err` | `const/let/var` | Error message string or error element. |

## Functions / methods (16 found)

### `mediaAppRoot` — lines 25–32

#### Signature

```javascript
function mediaAppRoot()
```

#### What it is

Function `mediaAppRoot` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `mediaAppRoot`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `p` | `—` | Parameter, path, or password fragment depending on context. |
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Code

```javascript
  25 | 
  26 | 
  27 | function mediaAppRoot() {
  28 |     var p = window.location.pathname || '';
  29 |     var i = p.toLowerCase().indexOf('/pages/');
  30 |     if (i > 0) return p.substring(0, i);
  31 |     return '';
  32 | }
```

---

### `resolveMediaUrl` — lines 32–49

#### Signature

```javascript
function resolveMediaUrl(raw, forDownload)
```

#### What it is

Function `resolveMediaUrl` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `resolveMediaUrl`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `raw` | `—` | Raw bytes or unprocessed input string. |
| `forDownload` | `—` | Holds “for Download” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `u` | `—` | Holds “u” for this scope. |
| `a` | `—` | Holds “a” for this scope. |

#### Code

```javascript
  32 | 
  33 | 
  34 | function resolveMediaUrl(raw, forDownload) {
  35 |     if (!raw) return '';
  36 |     var u = String(raw).trim();
  37 |     if (/^https?:\/\//i.test(u) && u.indexOf('/Uploads/') < 0 && u.indexOf('Media.ashx') < 0 && u.indexOf('Uploads/') < 0)
  38 |     return u;
  39 |     if (u.indexOf('Media.ashx') >= 0) {
  40 |         if (forDownload && u.indexOf('dl=1') < 0) return u + (u.indexOf('?') >= 0 ? '&' : '?') + 'dl=1';
  41 |         return u;
  42 |     }
  43 |     try {
  44 |         if (/^https?:\/\//i.test(u)) {
  45 |         var a = document.createElement('a');
  46 |         a.href = u;
  47 |         u = a.pathname || u;
  48 |     }
  49 | }
```

---

### `mediaKind` — lines 61–69

#### Signature

```javascript
function mediaKind(s)
```

#### What it is

Function `mediaKind` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `mediaKind`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
  61 | 
  62 | 
  63 | function mediaKind(s) {
  64 |     s = (s || '').toLowerCase();
  65 |     if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';
  66 |     if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';
  67 |     if (/\.pdf(\?|$)/.test(s)) return 'pdf';
  68 |     return 'file';
  69 | }
```

---

### `parseAnswerContent` — lines 71–99

#### Signature

```javascript
function parseAnswerContent(raw)
```

#### What it is

Converts or cleans **parse Answer Content** into a usable form.

#### How it works

1. Parse the server JSON response into a JavaScript object.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `raw` | `—` | Raw bytes or unprocessed input string. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `out` | `—` | Holds “out” for this scope. |
| `s` | `—` | String being cleaned or built. |
| `o` | `—` | Holds “o” for this scope.  JSON serialize/parse result. |
| `m` | `—` | Holds “m” for this scope. |

#### Code

```javascript
  71 | 
  72 | function parseAnswerContent(raw) {
  73 |     var out = { text: '', file: '', fileName: '' };
  74 |     if (raw == null) return out;
  75 |     var s = String(raw).trim();
  76 |     if (!s) return out;
  77 |     if (s.charAt(0) === '{') {
  78 |         try {
  79 |             var o = JSON.parse(s);
  80 |             out.text = o.text || o.Text || '';
  81 |             out.file = o.file || o.fileUrl || o.FileUrl || o.url || '';
  82 |             out.fileName = o.fileName || o.FileName || '';
  83 |             if (!out.fileName && out.file) out.fileName = out.file.split('/').pop();
  84 |             return out;
  85 |         } catch (e) { /* fall through */ }
  86 |     }
  87 |     // marker form
  88 |     var m = s.match(/<<<FILE>>>([\s\S]*?)<<<ENDFILE>>>/i);
  89 |     if (m) {
  90 |         out.file = m[1].trim();
  91 |         out.text = s.replace(m[0], '').trim();
  92 |         out.fileName = out.file.split('/').pop();
  93 |         return out;
  94 |     }
  95 |     if (/uploads\//i.test(s) || /Media\.ashx/i.test(s) || /\.(pdf|docx?|pptx?|png|jpe?g|mp4)(\?|$)/i.test(s)) {
  96 |     out.file = s;
  97 |     out.fileName = s.split('/').pop();
  98 |     return out;
  99 | }
```

---

### `loadSubmissions` — lines 102–140

#### Signature

```javascript
function loadSubmissions()
```

#### What it is

Reads/loads data related to **Submissions** and returns it for display or further use.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. If the previous step failed, show the error and stop.
4. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `graded` | `—` | Holds “graded” for this scope. |
| `total` | `—` | Sum of points or total items. |
| `pending` | `—` | Holds “pending” for this scope.  Literal number `0`. |
| `bp` | `—` | Holds “bp” for this scope.  DOM element from the page. |

#### Code

```javascript
 102 | 
 103 | 
 104 | function loadSubmissions() {
 105 |     fetch('Grading.aspx/GetSubmissions', {
 106 |         method: 'POST',
 107 |         headers: { 'Content-Type': 'application/json' },
 108 |         body: '{}',
 109 |         credentials: 'same-origin'
 110 |     })
 111 |     .then(function (r) { return r.json(); })
 112 |     .then(function (data) {
 113 |         var res = data.d || data;
 114 |         if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }
 115 |         if (!res.success) {
 116 |             document.getElementById('studentList').innerHTML =
 117 |             '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';
 118 |             return;
 119 |         }
 120 |         submissions = res.submissions || [];
 121 |         var graded = res.gradedCount || 0;
 122 |         var total = res.totalCount || submissions.length;
 123 |         var pending = 0;
 124 |         submissions.forEach(function (s) { if (!s.isGraded) pending++; });
 125 |         var bp = document.getElementById('badgePendingCount');
 126 |         if (bp) bp.textContent = String(pending);
 127 |         updateProgress(graded, total);
 128 |         filterStudents();
 129 |         if (filtered.length > 0) selectStudent(0);
 130 |         else {
 131 |             currentIndex = -1;
 132 |             document.getElementById('answerPreview').innerHTML =
 133 |                 '<div class="text-muted text-center py-5">No submissions in this filter</div>';
 134 |         }
 135 |     })
 136 |     .catch(function (err) {
 137 |         console.error(err);
 138 |         document.getElementById('studentList').innerHTML = '<div class="text-danger small">Network error</div>';
 139 |     });
 140 | }
```

---

### `updateProgress` — lines 140–146

#### Signature

```javascript
function updateProgress(graded, total)
```

#### What it is

Saves or updates **update Progress** in the database or UI state.

#### How it works

1. Starts when something calls `updateProgress`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `graded` | `—` | Holds “graded” for this scope. |
| `total` | `—` | Sum of points or total items. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `pct` | `—` | Holds “pct” for this scope. |

#### Code

```javascript
 140 | 
 141 | 
 142 | function updateProgress(graded, total) {
 143 |     document.getElementById('lblGradedCount').innerText = graded + '/' + total;
 144 |     var pct = total > 0 ? (graded / total) * 100 : 0;
 145 |     document.getElementById('gradedBar').style.width = pct + '%';
 146 | }
```

---

### `setStatusFilter` — lines 146–157

#### Signature

```javascript
function setStatusFilter(mode, btn)
```

#### What it is

Saves or updates **set Status Filter** in the database or UI state.

#### How it works

1. Starts when something calls `setStatusFilter`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `mode` | `—` | Holds “mode” for this scope. |
| `btn` | `—` | Button DOM element. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 146 | 
 147 | 
 148 | function setStatusFilter(mode, btn) {
 149 |     statusFilter = mode || 'all';
 150 |     document.querySelectorAll('[data-filter]').forEach(function (b) {
 151 |         b.classList.remove('active');
 152 |     });
 153 |     if (btn) btn.classList.add('active');
 154 |     currentIndex = -1;
 155 |     filterStudents();
 156 |     if (filtered.length > 0) selectStudent(0);
 157 | }
```

---

### `filterStudents` — lines 157–170

#### Signature

```javascript
function filterStudents()
```

#### What it is

Function `filterStudents` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `q` | `—` | Search query text, or SQL command text.  DOM element from the page. |

#### Code

```javascript
 157 | 
 158 | 
 159 | function filterStudents() {
 160 |     var q = (document.getElementById('txtSearchStudents').value || '').toLowerCase();
 161 |     filtered = submissions.filter(function (s) {
 162 |         if (statusFilter === 'pending' && s.isGraded) return false;
 163 |         if (statusFilter === 'graded' && !s.isGraded) return false;
 164 |         return !q ||
 165 |         (s.studentName || '').toLowerCase().indexOf(q) >= 0 ||
 166 |         (s.assignmentTitle || '').toLowerCase().indexOf(q) >= 0 ||
 167 |         (s.courseName || '').toLowerCase().indexOf(q) >= 0;
 168 |     });
 169 |     renderStudentList();
 170 | }
```

---

### `exportGradesCsv` — lines 170–202

#### Signature

```javascript
function exportGradesCsv()
```

#### What it is

Browser-side function `exportGradesCsv` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Convert a JavaScript object into a JSON string for the server.
3. Parse the server JSON response into a JavaScript object.
4. Show a simple popup message to the user.
5. If the previous step failed, show the error and stop.
6. Show a simple popup message to the user.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `blob` | `—` | Holds “blob” for this scope.  Newly constructed object. |
| `a` | `—` | Holds “a” for this scope. |

#### Code

```javascript
 170 | 
 171 | 
 172 | function exportGradesCsv() {
 173 |     fetch('Grading.aspx/ExportGradesCsv', {
 174 |         method: 'POST',
 175 |         headers: { 'Content-Type': 'application/json' },
 176 |         body: JSON.stringify({ cid: 0 }),
 177 |         credentials: 'same-origin'
 178 |     })
 179 |     .then(function (r) { return r.json(); })
 180 |     .then(function (data) {
 181 |         var res = data.d || data;
 182 |         if (res.notAuthenticated || res.csrf) {
 183 |             alert(res.message || 'Please refresh and sign in again.');
 184 |             return;
 185 |         }
 186 |         if (!res.success) {
 187 |             alert(res.message || 'Export failed');
 188 |             return;
 189 |         }
 190 |         var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });
 191 |         var a = document.createElement('a');
 192 |         a.href = URL.createObjectURL(blob);
 193 |         a.download = res.fileName || 'grades.csv';
 194 |         document.body.appendChild(a);
 195 |         a.click();
 196 |         setTimeout(function () {
 197 |             URL.revokeObjectURL(a.href);
 198 |             a.remove();
 199 |         }, 500);
 200 |     })
 201 |     .catch(function () { alert('Network error exporting grades.'); });
 202 | }
```

---

### `renderStudentList` — lines 202–232

#### Signature

```javascript
function renderStudentList()
```

#### What it is

Updates the page HTML for **render Student List**.

#### How it works

1. Starts when something calls `renderStudentList`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `box` | `—` | Container element for lists/tables.  DOM element from the page. |
| `colors` | `—` | Often a collection related to colors (plural name). |
| `div` | `—` | Holds “div” for this scope. |
| `parsed` | `—` | Holds “parsed” for this scope. |
| `fileIcon` | `—` | Holds “file Icon” for this scope. |
| `scoreHtml` | `—` | Holds “score Html” for this scope. |

#### Code

```javascript
 202 | 
 203 | 
 204 | function renderStudentList() {
 205 |     var box = document.getElementById('studentList');
 206 |     box.innerHTML = '';
 207 |     if (filtered.length === 0) {
 208 |         box.innerHTML = '<div class="text-muted small py-3 text-center">No submissions</div>';
 209 |         return;
 210 |     }
 211 |     var colors = ['#f59e0b', '#3b82f6', '#10b981', '#8b5cf6', '#ec4899'];
 212 |     filtered.forEach(function (s, i) {
 213 |         var div = document.createElement('div');
 214 |         div.className = 'student-row' + (i === currentIndex ? ' active' : '');
 215 |         div.onclick = function () { selectStudent(i); };
 216 |         var parsed = parseAnswerContent(s.studentAnswer || s.content || '');
 217 |         var fileIcon = parsed.file
 218 |         ? '<i class="fa-solid fa-paperclip text-muted me-1" style="font-size:.7rem;"></i>'
 219 |         : '';
 220 |         var scoreHtml = s.isGraded
 221 |         ? '<span class="text-success small fw-semibold">' + s.markScore + '/' + s.maxScore + '</span>'
 222 |         : '<span class="pending-dot"></span>';
 223 |         div.innerHTML =
 224 |         '<div class="student-avatar me-2" style="background:' + colors[i % colors.length] + '">' +
 225 |         escapeHtml(s.initials || '?') + '</div>' +
 226 |         '<div class="flex-grow-1 overflow-hidden">' +
 227 |         '<div class="fw-semibold small text-truncate">' + fileIcon + escapeHtml(s.studentName) + '</div>' +
 228 |         '<div class="text-muted" style="font-size:0.7rem;"><i class="fa-regular fa-clock me-1"></i>' +
 229 |         escapeHtml(s.timeText || '') + '</div></div>' + scoreHtml;
 230 |         box.appendChild(div);
 231 |     });
 232 | }
```

---

### `selectStudent` — lines 232–308

#### Signature

```javascript
function selectStudent(index)
```

#### What it is

Function `selectStudent` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `index` | `—` | Holds “index” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |
| `raw` | `—` | Raw bytes or unprocessed input string. |
| `parsed` | `—` | Holds “parsed” for this scope. |
| `preview` | `—` | Holds “preview” for this scope.  DOM element from the page. |
| `btnDl` | `—` | UI control reference (btn Dl).  DOM element from the page. |
| `html` | `—` | Holds “html” for this scope.  Literal text string. |
| `view` | `—` | Holds “view” for this scope. |
| `dl` | `—` | Holds “dl” for this scope. |
| `kind` | `—` | Upload kind (material/video/thumbnail/submission). |
| `label` | `—` | otpauth account label (issuer:email). |
| `max` | `—` | Holds “max” for this scope. |

#### Code

```javascript
 232 | 
 233 | 
 234 | function selectStudent(index) {
 235 |     if (index < 0 || index >= filtered.length) return;
 236 |     currentIndex = index;
 237 |     var s = filtered[index];
 238 |     renderStudentList();
 239 | 
 240 |     document.getElementById('lblAssignmentTitle').innerText = s.assignmentTitle || 'Submission';
 241 |     document.getElementById('lblAssignmentMeta').innerText =
 242 |     (s.courseName || '') + ' · ' + (s.studentName || '') +
 243 |     (s.requireFile ? ' · File required' : '');
 244 | 
 245 |     document.getElementById('previewAvatar').innerText = s.initials || '?';
 246 |     document.getElementById('previewName').innerText = (s.studentName || '') + "'s Submission";
 247 | 
 248 |     var raw = s.studentAnswer || s.content || '';
 249 |     var parsed = parseAnswerContent(raw);
 250 |     // Prefer explicit fields from API if present
 251 |     if (s.fileUrl) parsed.file = s.fileUrl;
 252 |     if (s.fileName) parsed.fileName = s.fileName;
 253 |     if (s.answerText != null && s.answerText !== '') parsed.text = s.answerText;
 254 | 
 255 |     var preview = document.getElementById('answerPreview');
 256 |     var btnDl = document.getElementById('btnDownload');
 257 |     var html = '';
 258 | 
 259 |     if (parsed.file) {
 260 |         var view = resolveMediaUrl(parsed.file, false);
 261 |         var dl = resolveMediaUrl(parsed.file, true);
 262 |         var kind = mediaKind((parsed.fileName || '') + ' ' + parsed.file);
 263 |         var label = parsed.fileName || parsed.file.split('/').pop() || 'file';
 264 | 
 265 |         html += '<div class="file-chip mb-2 d-flex align-items-center gap-2 p-2 border rounded bg-light">' +
 266 |         '<i class="fa-regular fa-file-lines"></i>' +
 267 |         '<span class="small text-truncate flex-grow-1">' + escapeHtml(label) + '</span>' +
 268 |         '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeAttr(view) + '" target="_blank">Open</a>' +
 269 |         '</div>';
 270 | 
 271 |         if (kind === 'pdf') {
 272 |             html += '<iframe src="' + escapeAttr(view) + '#toolbar=1" title="PDF preview" ' +
 273 |             'style="width:100%;height:480px;border:1px solid #e5e7eb;border-radius:10px;background:#fff;"></iframe>';
 274 |         } else if (kind === 'image') {
 275 |             html += '<img src="' + escapeAttr(view) + '" class="img-fluid rounded border" alt="" style="max-height:480px;" />';
 276 |         } else if (kind === 'video') {
 277 |             html += '<video controls playsinline class="w-100 rounded" style="max-height:420px;background:#111;" src="' +
 278 |             escapeAttr(view) + '"></video>';
 279 |         } else {
 280 |             html += '<div class="text-muted small text-center py-4">Preview not available - use Open / Download.</div>';
 281 |         }
 282 | 
 283 |         btnDl.href = dl;
 284 |         btnDl.style.display = 'inline-flex';
 285 |     } else {
 286 |         btnDl.style.display = 'none';
 287 |     }
 288 | 
 289 |     if (parsed.text) {
 290 |         html += '<div class="mt-3"><div class="fw-semibold small text-muted mb-1">Written answer</div>' +
 291 |         '<pre class="small p-3 bg-light rounded" style="white-space:pre-wrap;max-height:240px;overflow:auto;">' +
 292 |         escapeHtml(parsed.text) + '</pre></div>';
 293 |     }
 294 | 
 295 |     if (!parsed.file && !parsed.text) {
 296 |         html = '<div class="text-muted text-center py-5">No answer text or file</div>';
 297 |     }
 298 | 
 299 |     preview.innerHTML = html;
 300 | 
 301 |     var max = s.maxScore || 100;
 302 |     document.getElementById('lblMaxScore').innerText = '/ ' + max;
 303 |     document.getElementById('txtGradeScore').max = max;
 304 |     document.getElementById('txtGradeScore').value = s.isGraded ? s.markScore : 0;
 305 |     document.getElementById('txtFeedback').value = s.review || '';
 306 |     updateTotalDisplay();
 307 |     document.getElementById('gradeError').style.display = 'none';
 308 | }
```

---

### `updateTotalDisplay` — lines 308–314

#### Signature

```javascript
function updateTotalDisplay()
```

#### What it is

Saves or updates **update Total Display** in the database or UI state.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `max` | `—` | Holds “max” for this scope. |
| `score` | `—` | Points earned or max points depending on context.  DOM element from the page. |

#### Code

```javascript
 308 | 
 309 | 
 310 | function updateTotalDisplay() {
 311 |     var max = (filtered[currentIndex] && filtered[currentIndex].maxScore) || 100;
 312 |     var score = parseFloat(document.getElementById('txtGradeScore').value) || 0;
 313 |     document.getElementById('lblTotalScore').innerText = score + '/' + max;
 314 | }
```

---

### `navStudent` — lines 314–322

#### Signature

```javascript
function navStudent(delta)
```

#### What it is

Function `navStudent` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `navStudent`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `delta` | `—` | Holds “delta” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `next` | `—` | Holds “next” for this scope. |

#### Code

```javascript
 314 | 
 315 | 
 316 | function navStudent(delta) {
 317 |     if (filtered.length === 0) return;
 318 |     var next = currentIndex + delta;
 319 |     if (next < 0) next = 0;
 320 |     if (next >= filtered.length) next = filtered.length - 1;
 321 |     selectStudent(next);
 322 | }
```

---

### `submitGrade` — lines 322–358

#### Signature

```javascript
function submitGrade()
```

#### What it is

Browser-side function `submitGrade` — talks to the server and updates the page.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).
2. Call the server with `fetch` (AJAX) and wait for the JSON result.
3. Convert a JavaScript object into a JSON string for the server.
4. Parse the server JSON response into a JavaScript object.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |
| `score` | `—` | Points earned or max points depending on context.  DOM element from the page. |
| `review` | `—` | Holds “review” for this scope.  DOM element from the page. |
| `err` | `—` | Error message string or error element.  DOM element from the page. |
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |

#### Code

```javascript
 322 | 
 323 | 
 324 | function submitGrade() {
 325 |     if (currentIndex < 0 || !filtered[currentIndex]) return;
 326 |     var s = filtered[currentIndex];
 327 |     var score = parseFloat(document.getElementById('txtGradeScore').value);
 328 |     var review = document.getElementById('txtFeedback').value.trim();
 329 |     var err = document.getElementById('gradeError');
 330 |     err.style.display = 'none';
 331 | 
 332 |     if (isNaN(score) || score < 0) {
 333 |         err.innerText = 'Enter a valid score.';
 334 |         err.style.display = 'block';
 335 |         return;
 336 |     }
 337 | 
 338 |     fetch('Grading.aspx/SaveGrade', {
 339 |         method: 'POST',
 340 |         headers: { 'Content-Type': 'application/json' },
 341 |         body: JSON.stringify({ sid: s.sid, score: score, review: review }),
 342 |         credentials: 'same-origin'
 343 |     })
 344 |     .then(function (r) { return r.json(); })
 345 |     .then(function (data) {
 346 |         var res = data.d || data;
 347 |         if (res.success) loadSubmissions();
 348 |         else {
 349 |             err.innerText = res.message || 'Failed to save grade.';
 350 |             err.style.display = 'block';
 351 |         }
 352 |     })
 353 |     .catch(function (e) {
 354 |         err.innerText = 'Network error.';
 355 |         err.style.display = 'block';
 356 |         console.error(e);
 357 |     });
 358 | }
```

---

### `escapeHtml` — lines 358–366

#### Signature

```javascript
function escapeHtml(str)
```

#### What it is

Function `escapeHtml` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `escapeHtml`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `str` | `—` | String value: str. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 358 | 
 359 | 
 360 | function escapeHtml(str) {
 361 |     if (str == null) return '';
 362 |     return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
 363 | }
 364 | function escapeAttr(str) {
 365 |     return escapeHtml(str).replace(/'/g, '&#39;');
 366 | }
```

---

### `escapeAttr` — lines 363–366

#### Signature

```javascript
function escapeAttr(str)
```

#### What it is

Function `escapeAttr` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `escapeAttr`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `str` | `—` | String value: str. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 363 | 
 364 | function escapeAttr(str) {
 365 |     return escapeHtml(str).replace(/'/g, '&#39;');
 366 | }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | /* Grading page - CWSubmissions + CWMarkings; PDF/image/video preview for file answers */
   2 | 
   3 | let submissions = [];
   4 | let filtered = [];
   5 | let currentIndex = -1;
   6 | let statusFilter = 'all'; // all | pending | graded
   7 | 
   8 | document.addEventListener('DOMContentLoaded', function () {
   9 |     // Deep-link: Grading.aspx?filter=pending
  10 |     try {
  11 |         var params = new URLSearchParams(window.location.search || '');
  12 |         var f = (params.get('filter') || '').toLowerCase();
  13 |         if (f === 'pending' || f === 'graded' || f === 'all') {
  14 |             statusFilter = f;
  15 |             var btn = document.querySelector('[data-filter="' + f + '"]');
  16 |             if (btn) {
  17 |                 document.querySelectorAll('[data-filter]').forEach(function (b) {
  18 |                     b.classList.remove('active');
  19 |                 });
  20 |                 btn.classList.add('active');
  21 |             }
  22 |         }
  23 |     } catch (e) { }
  24 |     loadSubmissions();
  25 | });
  26 | 
  27 | function mediaAppRoot() {
  28 |     var p = window.location.pathname || '';
  29 |     var i = p.toLowerCase().indexOf('/pages/');
  30 |     if (i > 0) return p.substring(0, i);
  31 |     return '';
  32 | }
  33 | 
  34 | function resolveMediaUrl(raw, forDownload) {
  35 |     if (!raw) return '';
  36 |     var u = String(raw).trim();
  37 |     if (/^https?:\/\//i.test(u) && u.indexOf('/Uploads/') < 0 && u.indexOf('Media.ashx') < 0 && u.indexOf('Uploads/') < 0)
  38 |     return u;
  39 |     if (u.indexOf('Media.ashx') >= 0) {
  40 |         if (forDownload && u.indexOf('dl=1') < 0) return u + (u.indexOf('?') >= 0 ? '&' : '?') + 'dl=1';
  41 |         return u;
  42 |     }
  43 |     try {
  44 |         if (/^https?:\/\//i.test(u)) {
  45 |         var a = document.createElement('a');
  46 |         a.href = u;
  47 |         u = a.pathname || u;
  48 |     }
  49 | } catch (e) { }
  50 | var path = u.replace(/\\/g, '/');
  51 | var idx = path.toLowerCase().indexOf('/uploads/');
  52 | if (idx >= 0) path = path.substring(idx + 1);
  53 | if (path.indexOf('~/') === 0) path = path.substring(2);
  54 | path = path.replace(/^\/+/, '');
  55 | if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);
  56 | if (!path) return '';
  57 | if (path.indexOf('/') < 0) path = 'CourseSubmissions/' + path;
  58 | var url = mediaAppRoot() + '/Media.ashx?f=' + encodeURIComponent(path);
  59 | if (forDownload) url += '&dl=1';
  60 | return url;
  61 | }
  62 | 
  63 | function mediaKind(s) {
  64 |     s = (s || '').toLowerCase();
  65 |     if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';
  66 |     if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';
  67 |     if (/\.pdf(\?|$)/.test(s)) return 'pdf';
  68 |     return 'file';
  69 | }
  70 | 
  71 | /** Parse CWSubmissions.Content: plain text or JSON {text,file,fileName} */
  72 | function parseAnswerContent(raw) {
  73 |     var out = { text: '', file: '', fileName: '' };
  74 |     if (raw == null) return out;
  75 |     var s = String(raw).trim();
  76 |     if (!s) return out;
  77 |     if (s.charAt(0) === '{') {
  78 |         try {
  79 |             var o = JSON.parse(s);
  80 |             out.text = o.text || o.Text || '';
  81 |             out.file = o.file || o.fileUrl || o.FileUrl || o.url || '';
  82 |             out.fileName = o.fileName || o.FileName || '';
  83 |             if (!out.fileName && out.file) out.fileName = out.file.split('/').pop();
  84 |             return out;
  85 |         } catch (e) { /* fall through */ }
  86 |     }
  87 |     // marker form
  88 |     var m = s.match(/<<<FILE>>>([\s\S]*?)<<<ENDFILE>>>/i);
  89 |     if (m) {
  90 |         out.file = m[1].trim();
  91 |         out.text = s.replace(m[0], '').trim();
  92 |         out.fileName = out.file.split('/').pop();
  93 |         return out;
  94 |     }
  95 |     if (/uploads\//i.test(s) || /Media\.ashx/i.test(s) || /\.(pdf|docx?|pptx?|png|jpe?g|mp4)(\?|$)/i.test(s)) {
  96 |     out.file = s;
  97 |     out.fileName = s.split('/').pop();
  98 |     return out;
  99 | }
 100 | out.text = s;
 101 | return out;
 102 | }
 103 | 
 104 | function loadSubmissions() {
 105 |     fetch('Grading.aspx/GetSubmissions', {
 106 |         method: 'POST',
 107 |         headers: { 'Content-Type': 'application/json' },
 108 |         body: '{}',
 109 |         credentials: 'same-origin'
 110 |     })
 111 |     .then(function (r) { return r.json(); })
 112 |     .then(function (data) {
 113 |         var res = data.d || data;
 114 |         if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }
 115 |         if (!res.success) {
 116 |             document.getElementById('studentList').innerHTML =
 117 |             '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';
 118 |             return;
 119 |         }
 120 |         submissions = res.submissions || [];
 121 |         var graded = res.gradedCount || 0;
 122 |         var total = res.totalCount || submissions.length;
 123 |         var pending = 0;
 124 |         submissions.forEach(function (s) { if (!s.isGraded) pending++; });
 125 |         var bp = document.getElementById('badgePendingCount');
 126 |         if (bp) bp.textContent = String(pending);
 127 |         updateProgress(graded, total);
 128 |         filterStudents();
 129 |         if (filtered.length > 0) selectStudent(0);
 130 |         else {
 131 |             currentIndex = -1;
 132 |             document.getElementById('answerPreview').innerHTML =
 133 |                 '<div class="text-muted text-center py-5">No submissions in this filter</div>';
 134 |         }
 135 |     })
 136 |     .catch(function (err) {
 137 |         console.error(err);
 138 |         document.getElementById('studentList').innerHTML = '<div class="text-danger small">Network error</div>';
 139 |     });
 140 | }
 141 | 
 142 | function updateProgress(graded, total) {
 143 |     document.getElementById('lblGradedCount').innerText = graded + '/' + total;
 144 |     var pct = total > 0 ? (graded / total) * 100 : 0;
 145 |     document.getElementById('gradedBar').style.width = pct + '%';
 146 | }
 147 | 
 148 | function setStatusFilter(mode, btn) {
 149 |     statusFilter = mode || 'all';
 150 |     document.querySelectorAll('[data-filter]').forEach(function (b) {
 151 |         b.classList.remove('active');
 152 |     });
 153 |     if (btn) btn.classList.add('active');
 154 |     currentIndex = -1;
 155 |     filterStudents();
 156 |     if (filtered.length > 0) selectStudent(0);
 157 | }
 158 | 
 159 | function filterStudents() {
 160 |     var q = (document.getElementById('txtSearchStudents').value || '').toLowerCase();
 161 |     filtered = submissions.filter(function (s) {
 162 |         if (statusFilter === 'pending' && s.isGraded) return false;
 163 |         if (statusFilter === 'graded' && !s.isGraded) return false;
 164 |         return !q ||
 165 |         (s.studentName || '').toLowerCase().indexOf(q) >= 0 ||
 166 |         (s.assignmentTitle || '').toLowerCase().indexOf(q) >= 0 ||
 167 |         (s.courseName || '').toLowerCase().indexOf(q) >= 0;
 168 |     });
 169 |     renderStudentList();
 170 | }
 171 | 
 172 | function exportGradesCsv() {
 173 |     fetch('Grading.aspx/ExportGradesCsv', {
 174 |         method: 'POST',
 175 |         headers: { 'Content-Type': 'application/json' },
 176 |         body: JSON.stringify({ cid: 0 }),
 177 |         credentials: 'same-origin'
 178 |     })
 179 |     .then(function (r) { return r.json(); })
 180 |     .then(function (data) {
 181 |         var res = data.d || data;
 182 |         if (res.notAuthenticated || res.csrf) {
 183 |             alert(res.message || 'Please refresh and sign in again.');
 184 |             return;
 185 |         }
 186 |         if (!res.success) {
 187 |             alert(res.message || 'Export failed');
 188 |             return;
 189 |         }
 190 |         var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });
 191 |         var a = document.createElement('a');
 192 |         a.href = URL.createObjectURL(blob);
 193 |         a.download = res.fileName || 'grades.csv';
 194 |         document.body.appendChild(a);
 195 |         a.click();
 196 |         setTimeout(function () {
 197 |             URL.revokeObjectURL(a.href);
 198 |             a.remove();
 199 |         }, 500);
 200 |     })
 201 |     .catch(function () { alert('Network error exporting grades.'); });
 202 | }
 203 | 
 204 | function renderStudentList() {
 205 |     var box = document.getElementById('studentList');
 206 |     box.innerHTML = '';
 207 |     if (filtered.length === 0) {
 208 |         box.innerHTML = '<div class="text-muted small py-3 text-center">No submissions</div>';
 209 |         return;
 210 |     }
 211 |     var colors = ['#f59e0b', '#3b82f6', '#10b981', '#8b5cf6', '#ec4899'];
 212 |     filtered.forEach(function (s, i) {
 213 |         var div = document.createElement('div');
 214 |         div.className = 'student-row' + (i === currentIndex ? ' active' : '');
 215 |         div.onclick = function () { selectStudent(i); };
 216 |         var parsed = parseAnswerContent(s.studentAnswer || s.content || '');
 217 |         var fileIcon = parsed.file
 218 |         ? '<i class="fa-solid fa-paperclip text-muted me-1" style="font-size:.7rem;"></i>'
 219 |         : '';
 220 |         var scoreHtml = s.isGraded
 221 |         ? '<span class="text-success small fw-semibold">' + s.markScore + '/' + s.maxScore + '</span>'
 222 |         : '<span class="pending-dot"></span>';
 223 |         div.innerHTML =
 224 |         '<div class="student-avatar me-2" style="background:' + colors[i % colors.length] + '">' +
 225 |         escapeHtml(s.initials || '?') + '</div>' +
 226 |         '<div class="flex-grow-1 overflow-hidden">' +
 227 |         '<div class="fw-semibold small text-truncate">' + fileIcon + escapeHtml(s.studentName) + '</div>' +
 228 |         '<div class="text-muted" style="font-size:0.7rem;"><i class="fa-regular fa-clock me-1"></i>' +
 229 |         escapeHtml(s.timeText || '') + '</div></div>' + scoreHtml;
 230 |         box.appendChild(div);
 231 |     });
 232 | }
 233 | 
 234 | function selectStudent(index) {
 235 |     if (index < 0 || index >= filtered.length) return;
 236 |     currentIndex = index;
 237 |     var s = filtered[index];
 238 |     renderStudentList();
 239 | 
 240 |     document.getElementById('lblAssignmentTitle').innerText = s.assignmentTitle || 'Submission';
 241 |     document.getElementById('lblAssignmentMeta').innerText =
 242 |     (s.courseName || '') + ' · ' + (s.studentName || '') +
 243 |     (s.requireFile ? ' · File required' : '');
 244 | 
 245 |     document.getElementById('previewAvatar').innerText = s.initials || '?';
 246 |     document.getElementById('previewName').innerText = (s.studentName || '') + "'s Submission";
 247 | 
 248 |     var raw = s.studentAnswer || s.content || '';
 249 |     var parsed = parseAnswerContent(raw);
 250 |     // Prefer explicit fields from API if present
 251 |     if (s.fileUrl) parsed.file = s.fileUrl;
 252 |     if (s.fileName) parsed.fileName = s.fileName;
 253 |     if (s.answerText != null && s.answerText !== '') parsed.text = s.answerText;
 254 | 
 255 |     var preview = document.getElementById('answerPreview');
 256 |     var btnDl = document.getElementById('btnDownload');
 257 |     var html = '';
 258 | 
 259 |     if (parsed.file) {
 260 |         var view = resolveMediaUrl(parsed.file, false);
 261 |         var dl = resolveMediaUrl(parsed.file, true);
 262 |         var kind = mediaKind((parsed.fileName || '') + ' ' + parsed.file);
 263 |         var label = parsed.fileName || parsed.file.split('/').pop() || 'file';
 264 | 
 265 |         html += '<div class="file-chip mb-2 d-flex align-items-center gap-2 p-2 border rounded bg-light">' +
 266 |         '<i class="fa-regular fa-file-lines"></i>' +
 267 |         '<span class="small text-truncate flex-grow-1">' + escapeHtml(label) + '</span>' +
 268 |         '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeAttr(view) + '" target="_blank">Open</a>' +
 269 |         '</div>';
 270 | 
 271 |         if (kind === 'pdf') {
 272 |             html += '<iframe src="' + escapeAttr(view) + '#toolbar=1" title="PDF preview" ' +
 273 |             'style="width:100%;height:480px;border:1px solid #e5e7eb;border-radius:10px;background:#fff;"></iframe>';
 274 |         } else if (kind === 'image') {
 275 |             html += '<img src="' + escapeAttr(view) + '" class="img-fluid rounded border" alt="" style="max-height:480px;" />';
 276 |         } else if (kind === 'video') {
 277 |             html += '<video controls playsinline class="w-100 rounded" style="max-height:420px;background:#111;" src="' +
 278 |             escapeAttr(view) + '"></video>';
 279 |         } else {
 280 |             html += '<div class="text-muted small text-center py-4">Preview not available - use Open / Download.</div>';
 281 |         }
 282 | 
 283 |         btnDl.href = dl;
 284 |         btnDl.style.display = 'inline-flex';
 285 |     } else {
 286 |         btnDl.style.display = 'none';
 287 |     }
 288 | 
 289 |     if (parsed.text) {
 290 |         html += '<div class="mt-3"><div class="fw-semibold small text-muted mb-1">Written answer</div>' +
 291 |         '<pre class="small p-3 bg-light rounded" style="white-space:pre-wrap;max-height:240px;overflow:auto;">' +
 292 |         escapeHtml(parsed.text) + '</pre></div>';
 293 |     }
 294 | 
 295 |     if (!parsed.file && !parsed.text) {
 296 |         html = '<div class="text-muted text-center py-5">No answer text or file</div>';
 297 |     }
 298 | 
 299 |     preview.innerHTML = html;
 300 | 
 301 |     var max = s.maxScore || 100;
 302 |     document.getElementById('lblMaxScore').innerText = '/ ' + max;
 303 |     document.getElementById('txtGradeScore').max = max;
 304 |     document.getElementById('txtGradeScore').value = s.isGraded ? s.markScore : 0;
 305 |     document.getElementById('txtFeedback').value = s.review || '';
 306 |     updateTotalDisplay();
 307 |     document.getElementById('gradeError').style.display = 'none';
 308 | }
 309 | 
 310 | function updateTotalDisplay() {
 311 |     var max = (filtered[currentIndex] && filtered[currentIndex].maxScore) || 100;
 312 |     var score = parseFloat(document.getElementById('txtGradeScore').value) || 0;
 313 |     document.getElementById('lblTotalScore').innerText = score + '/' + max;
 314 | }
 315 | 
 316 | function navStudent(delta) {
 317 |     if (filtered.length === 0) return;
 318 |     var next = currentIndex + delta;
 319 |     if (next < 0) next = 0;
 320 |     if (next >= filtered.length) next = filtered.length - 1;
 321 |     selectStudent(next);
 322 | }
 323 | 
 324 | function submitGrade() {
 325 |     if (currentIndex < 0 || !filtered[currentIndex]) return;
 326 |     var s = filtered[currentIndex];
 327 |     var score = parseFloat(document.getElementById('txtGradeScore').value);
 328 |     var review = document.getElementById('txtFeedback').value.trim();
 329 |     var err = document.getElementById('gradeError');
 330 |     err.style.display = 'none';
 331 | 
 332 |     if (isNaN(score) || score < 0) {
 333 |         err.innerText = 'Enter a valid score.';
 334 |         err.style.display = 'block';
 335 |         return;
 336 |     }
 337 | 
 338 |     fetch('Grading.aspx/SaveGrade', {
 339 |         method: 'POST',
 340 |         headers: { 'Content-Type': 'application/json' },
 341 |         body: JSON.stringify({ sid: s.sid, score: score, review: review }),
 342 |         credentials: 'same-origin'
 343 |     })
 344 |     .then(function (r) { return r.json(); })
 345 |     .then(function (data) {
 346 |         var res = data.d || data;
 347 |         if (res.success) loadSubmissions();
 348 |         else {
 349 |             err.innerText = res.message || 'Failed to save grade.';
 350 |             err.style.display = 'block';
 351 |         }
 352 |     })
 353 |     .catch(function (e) {
 354 |         err.innerText = 'Network error.';
 355 |         err.style.display = 'block';
 356 |         console.error(e);
 357 |     });
 358 | }
 359 | 
 360 | function escapeHtml(str) {
 361 |     if (str == null) return '';
 362 |     return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
 363 | }
 364 | function escapeAttr(str) {
 365 |     return escapeHtml(str).replace(/'/g, '&#39;');
 366 | }
```
