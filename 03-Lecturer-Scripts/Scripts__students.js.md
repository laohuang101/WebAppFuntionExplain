# students.js
**Source:** `Pages/Lecturer/Scripts/students.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Enrolled students per course with progress counts.

## File overview

- **Total lines:** 193
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `trendChart` | `const/let/var` | Holds “trend Chart” for this scope. |
| `studentsDt` | `const/let/var` | Holds “students Dt” for this scope. |
| `colors` | `const/let/var` | Often a collection related to colors (plural name). |
| `bg` | `const/let/var` | Holds “bg” for this scope. |
| `pct` | `const/let/var` | Holds “pct” for this scope. |
| `g` | `const/let/var` | Holds “g” for this scope. |
| `res` | `const/let/var` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `d` | `const/let/var` | Often a dictionary payload or date value. |
| `tbody` | `const/let/var` | Holds “tbody” for this scope. |
| `tr` | `const/let/var` | Holds “tr” for this scope. |
| `ctx` | `const/let/var` | Current HTTP request context (Request, Response, Session). |
| `labels` | `const/let/var` | Often a collection related to labels (plural name). |
| `values` | `const/let/var` | Often a collection related to values (plural name). |

## Functions / methods (10 found)

### `render` — lines 26–32

#### Signature

```javascript
function render(s, i)
```

#### What it is

Updates the page HTML for **render**.

#### How it works

1. Starts when something calls `render`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `bg` | `—` | Holds “bg” for this scope. |

#### Code

```javascript
  26 |             render: function (s, i) {
  27 |                 var bg = colors[i % colors.length];
  28 |                 return '<div class="d-flex align-items-center gap-2">' +
  29 |                 '<div class="student-avatar" style="background:' + bg + '">' + escapeHtml(s.initials || '?') + '</div>' +
  30 |                 '<div><div class="fw-semibold">' + escapeHtml(s.studentName) + '</div>' +
  31 |                 '<div class="text-muted small">' + escapeHtml(s.email || '') + '</div></div></div>';
  32 |             }
```

---

### `searchValue` — lines 33–33

#### Signature

```javascript
function searchValue(s)
```

#### What it is

Function `searchValue` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `searchValue`.
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
  33 |             searchValue: function (s) { return (s.studentName || '') + ' ' + (s.email || ''); }
```

---

### `render` — lines 47–53

#### Signature

```javascript
function render(s)
```

#### What it is

Updates the page HTML for **render**.

#### How it works

1. Starts when something calls `render`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `pct` | `—` | Holds “pct” for this scope. |

#### Code

```javascript
  47 |             render: function (s) {
  48 |                 var pct = Math.round(Number(s.progress) || 0);
  49 |                 return '<div class="d-flex align-items-center gap-2" style="min-width:140px;">' +
  50 |                 '<div class="progress flex-grow-1" style="height:8px;">' +
  51 |                 '<div class="progress-bar" style="width:' + pct + '%;background:var(--primary-accent);"></div></div>' +
  52 |                 '<span class="small text-muted">' + pct + '%</span></div>';
  53 |             }
```

---

### `render` — lines 61–64

#### Signature

```javascript
function render(s)
```

#### What it is

Updates the page HTML for **render**.

#### How it works

1. Starts when something calls `render`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `g` | `—` | Holds “g” for this scope. |

#### Code

```javascript
  61 |             render: function (s) {
  62 |                 var g = s.currentGrade || '-';
  63 |                 return '<span class="grade-badge ' + gradeColor(g) + '">' + escapeHtml(g) + '</span>';
  64 |             }
```

---

### `render` — lines 78–82

#### Signature

```javascript
function render(s)
```

#### What it is

Updates the page HTML for **render**.

#### How it works

1. Starts when something calls `render`.
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
  78 |             render: function (s) {
  79 |                 return '<button type="button" class="btn btn-sm btn-link text-muted" ' +
  80 |                 'onclick="openDetail(' + s.uid + ', ' + s.cid + ')">' +
  81 |                 '<i class="fa-solid fa-chevron-right"></i></button>';
  82 |             }
```

---

### `loadStudents` — lines 88–113

#### Signature

```javascript
function loadStudents()
```

#### What it is

Reads/loads data related to **Students** and returns it for display or further use.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Convert a JavaScript object into a JSON string for the server.
3. Parse the server JSON response into a JavaScript object.
4. If the previous step failed, show the error and stop.
5. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |

#### Code

```javascript
  88 | 
  89 | 
  90 | function loadStudents() {
  91 |     fetch('Students.aspx/GetStudents', {
  92 |         method: 'POST',
  93 |         headers: { 'Content-Type': 'application/json' },
  94 |         body: JSON.stringify({ search: null }),
  95 |         credentials: 'same-origin'
  96 |     })
  97 |     .then(function (r) { return r.json(); })
  98 |     .then(function (data) {
  99 |         var res = data.d || data;
 100 |         if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }
 101 |         if (!res.success) {
 102 |             document.getElementById('studentsTableWrap').innerHTML =
 103 |             '<div class="text-danger p-3">' + escapeHtml(res.message || 'Error') + '</div>';
 104 |             return;
 105 |         }
 106 |         studentsDt.setData(res.students || []);
 107 |     })
 108 |     .catch(function (err) {
 109 |         console.error(err);
 110 |         document.getElementById('studentsTableWrap').innerHTML =
 111 |         '<div class="text-danger p-3">Network error loading students.</div>';
 112 |     });
 113 | }
```

---

### `openDetail` — lines 113–152

#### Signature

```javascript
function openDetail(uid, cid)
```

#### What it is

Browser-side function `openDetail` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Convert a JavaScript object into a JSON string for the server.
3. Parse the server JSON response into a JavaScript object.
4. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `uid` | `—` | User ID (Users.UID) of the logged-in or target user. |
| `cid` | `—` | Course ID (Courses.CID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `d` | `—` | Often a dictionary payload or date value. |
| `tbody` | `—` | Holds “tbody” for this scope.  DOM element from the page. |
| `tr` | `—` | Holds “tr” for this scope. |

#### Code

```javascript
 113 | 
 114 | 
 115 | function openDetail(uid, cid) {
 116 |     fetch('Students.aspx/GetStudentDetail', {
 117 |         method: 'POST',
 118 |         headers: { 'Content-Type': 'application/json' },
 119 |         body: JSON.stringify({ studentUid: uid, cid: cid }),
 120 |         credentials: 'same-origin'
 121 |     })
 122 |     .then(function (r) { return r.json(); })
 123 |     .then(function (data) {
 124 |         var res = data.d || data;
 125 |         if (!res.success) { alert(res.message || 'Failed'); return; }
 126 |         var d = res.detail;
 127 |         document.getElementById('mAvatar').innerText = d.initials || '?';
 128 |         document.getElementById('mName').innerText = d.studentName || '';
 129 |         document.getElementById('mMeta').innerText = (d.email || '') + ' · ' + (d.courseName || '');
 130 |         document.getElementById('mGrade').innerText = d.currentGrade || '-';
 131 |         document.getElementById('mProgress').innerText = Math.round(Number(d.progress) || 0) + '%';
 132 |         document.getElementById('mAttendance').innerText = Math.round(Number(d.attendance) || 0) + '%';
 133 | 
 134 |         var tbody = document.getElementById('mGradesBody');
 135 |         tbody.innerHTML = '';
 136 |         (d.recentGrades || []).forEach(function (g) {
 137 |             var tr = document.createElement('tr');
 138 |             tr.innerHTML =
 139 |             '<td>' + escapeHtml(g.assignment) + '</td>' +
 140 |             '<td class="text-muted small">' + escapeHtml(g.date) + '</td>' +
 141 |             '<td class="text-end text-success fw-semibold">' + escapeHtml(g.score) + '</td>';
 142 |             tbody.appendChild(tr);
 143 |         });
 144 |         if (!d.recentGrades || d.recentGrades.length === 0) {
 145 |             tbody.innerHTML = '<tr><td colspan="3" class="text-muted text-center">No graded work yet</td></tr>';
 146 |         }
 147 | 
 148 |         renderTrend(d.trend || []);
 149 |         new bootstrap.Modal(document.getElementById('studentModal')).show();
 150 |     })
 151 |     .catch(console.error);
 152 | }
```

---

### `renderTrend` — lines 152–179

#### Signature

```javascript
function renderTrend(data)
```

#### What it is

Updates the page HTML for **render Trend**.

#### How it works

1. Starts when something calls `renderTrend`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `data` | `—` | Holds “data” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctx` | `—` | Current HTTP request context (Request, Response, Session).  DOM element from the page. |
| `labels` | `—` | Often a collection related to labels (plural name). |
| `values` | `—` | Often a collection related to values (plural name). |

#### Code

```javascript
 152 | 
 153 | 
 154 | function renderTrend(data) {
 155 |     var ctx = document.getElementById('trendChart');
 156 |     if (!ctx || typeof Chart === 'undefined') return;
 157 |     if (trendChart) trendChart.destroy();
 158 |     var labels = data.map(function (d) { return d.label; });
 159 |     var values = data.map(function (d) { return d.value; });
 160 |     trendChart = new Chart(ctx.getContext('2d'), {
 161 |         type: 'line',
 162 |         data: {
 163 |             labels: labels.length ? labels : ['-'],
 164 |             datasets: [{
 165 |                 data: values.length ? values : [0],
 166 |                 borderColor: '#f17f54',
 167 |                 backgroundColor: 'rgba(241,127,84,0.1)',
 168 |                 fill: true,
 169 |                 tension: 0.4,
 170 |                 pointRadius: 2
 171 |             }]
 172 |         },
 173 |         options: {
 174 |             responsive: true,
 175 |             plugins: { legend: { display: false } },
 176 |             scales: { y: { beginAtZero: true, max: 100 } }
 177 |         }
 178 |     });
 179 | }
```

---

### `gradeColor` — lines 179–188

#### Signature

```javascript
function gradeColor(g)
```

#### What it is

Function `gradeColor` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `gradeColor`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `g` | `—` | Holds “g” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 179 | 
 180 | 
 181 | function gradeColor(g) {
 182 |     if (!g || g === '-') return '';
 183 |     if (g.indexOf('A') === 0) return 'grade-a';
 184 |     if (g.indexOf('B') === 0) return 'grade-b';
 185 |     if (g.indexOf('C') === 0) return 'grade-c';
 186 |     if (g.indexOf('D') === 0 || g.indexOf('F') === 0) return 'grade-f';
 187 |     return '';
 188 | }
```

---

### `escapeHtml` — lines 188–193

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
 188 | 
 189 | 
 190 | function escapeHtml(str) {
 191 |     if (str == null) return '';
 192 |     return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
 193 | }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | /* Student Performance - EduDataTable (search / sort / filter / pagination) */
   2 | 
   3 | let trendChart = null;
   4 | let studentsDt = null;
   5 | const colors = ['#f59e0b', '#3b82f6', '#10b981', '#8b5cf6', '#ec4899'];
   6 | 
   7 | document.addEventListener('DOMContentLoaded', function () {
   8 |     if (typeof EduDataTable === 'undefined') {
   9 |         document.getElementById('studentsTableWrap').innerHTML =
  10 |         '<div class="text-danger p-3">DataTable component failed to load.</div>';
  11 |         return;
  12 |     }
  13 | 
  14 |     studentsDt = EduDataTable.create({
  15 |         container: '#studentsTableWrap',
  16 |         pageSize: 10,
  17 |         pageSizeOptions: [5, 10, 25, 50],
  18 |         searchPlaceholder: 'Search name, email, course...',
  19 |         emptyMessage: 'No enrolled students found.',
  20 |         columns: [
  21 |         {
  22 |             key: 'studentName',
  23 |             title: 'Student',
  24 |             sortable: true,
  25 |             search: true,
  26 |             render: function (s, i) {
  27 |                 var bg = colors[i % colors.length];
  28 |                 return '<div class="d-flex align-items-center gap-2">' +
  29 |                 '<div class="student-avatar" style="background:' + bg + '">' + escapeHtml(s.initials || '?') + '</div>' +
  30 |                 '<div><div class="fw-semibold">' + escapeHtml(s.studentName) + '</div>' +
  31 |                 '<div class="text-muted small">' + escapeHtml(s.email || '') + '</div></div></div>';
  32 |             },
  33 |             searchValue: function (s) { return (s.studentName || '') + ' ' + (s.email || ''); }
  34 |         },
  35 |         {
  36 |             key: 'courseName',
  37 |             title: 'Course',
  38 |             sortable: true,
  39 |             filter: true,
  40 |             filterLabel: 'Course'
  41 |         },
  42 |         {
  43 |             key: 'progress',
  44 |             title: 'Progress',
  45 |             sortable: true,
  46 |             type: 'number',
  47 |             render: function (s) {
  48 |                 var pct = Math.round(Number(s.progress) || 0);
  49 |                 return '<div class="d-flex align-items-center gap-2" style="min-width:140px;">' +
  50 |                 '<div class="progress flex-grow-1" style="height:8px;">' +
  51 |                 '<div class="progress-bar" style="width:' + pct + '%;background:var(--primary-accent);"></div></div>' +
  52 |                 '<span class="small text-muted">' + pct + '%</span></div>';
  53 |             }
  54 |         },
  55 |         {
  56 |             key: 'currentGrade',
  57 |             title: 'Grade',
  58 |             sortable: true,
  59 |             filter: true,
  60 |             filterLabel: 'Grade',
  61 |             render: function (s) {
  62 |                 var g = s.currentGrade || '-';
  63 |                 return '<span class="grade-badge ' + gradeColor(g) + '">' + escapeHtml(g) + '</span>';
  64 |             }
  65 |         },
  66 |         {
  67 |             key: 'lastActive',
  68 |             title: 'Last Active',
  69 |             sortable: true,
  70 |             cellClass: 'text-muted small'
  71 |         },
  72 |         {
  73 |             key: '_actions',
  74 |             title: '',
  75 |             sortable: false,
  76 |             search: false,
  77 |             cellClass: 'text-end',
  78 |             render: function (s) {
  79 |                 return '<button type="button" class="btn btn-sm btn-link text-muted" ' +
  80 |                 'onclick="openDetail(' + s.uid + ', ' + s.cid + ')">' +
  81 |                 '<i class="fa-solid fa-chevron-right"></i></button>';
  82 |             }
  83 |         }
  84 |         ]
  85 |     });
  86 | 
  87 |     loadStudents();
  88 | });
  89 | 
  90 | function loadStudents() {
  91 |     fetch('Students.aspx/GetStudents', {
  92 |         method: 'POST',
  93 |         headers: { 'Content-Type': 'application/json' },
  94 |         body: JSON.stringify({ search: null }),
  95 |         credentials: 'same-origin'
  96 |     })
  97 |     .then(function (r) { return r.json(); })
  98 |     .then(function (data) {
  99 |         var res = data.d || data;
 100 |         if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }
 101 |         if (!res.success) {
 102 |             document.getElementById('studentsTableWrap').innerHTML =
 103 |             '<div class="text-danger p-3">' + escapeHtml(res.message || 'Error') + '</div>';
 104 |             return;
 105 |         }
 106 |         studentsDt.setData(res.students || []);
 107 |     })
 108 |     .catch(function (err) {
 109 |         console.error(err);
 110 |         document.getElementById('studentsTableWrap').innerHTML =
 111 |         '<div class="text-danger p-3">Network error loading students.</div>';
 112 |     });
 113 | }
 114 | 
 115 | function openDetail(uid, cid) {
 116 |     fetch('Students.aspx/GetStudentDetail', {
 117 |         method: 'POST',
 118 |         headers: { 'Content-Type': 'application/json' },
 119 |         body: JSON.stringify({ studentUid: uid, cid: cid }),
 120 |         credentials: 'same-origin'
 121 |     })
 122 |     .then(function (r) { return r.json(); })
 123 |     .then(function (data) {
 124 |         var res = data.d || data;
 125 |         if (!res.success) { alert(res.message || 'Failed'); return; }
 126 |         var d = res.detail;
 127 |         document.getElementById('mAvatar').innerText = d.initials || '?';
 128 |         document.getElementById('mName').innerText = d.studentName || '';
 129 |         document.getElementById('mMeta').innerText = (d.email || '') + ' · ' + (d.courseName || '');
 130 |         document.getElementById('mGrade').innerText = d.currentGrade || '-';
 131 |         document.getElementById('mProgress').innerText = Math.round(Number(d.progress) || 0) + '%';
 132 |         document.getElementById('mAttendance').innerText = Math.round(Number(d.attendance) || 0) + '%';
 133 | 
 134 |         var tbody = document.getElementById('mGradesBody');
 135 |         tbody.innerHTML = '';
 136 |         (d.recentGrades || []).forEach(function (g) {
 137 |             var tr = document.createElement('tr');
 138 |             tr.innerHTML =
 139 |             '<td>' + escapeHtml(g.assignment) + '</td>' +
 140 |             '<td class="text-muted small">' + escapeHtml(g.date) + '</td>' +
 141 |             '<td class="text-end text-success fw-semibold">' + escapeHtml(g.score) + '</td>';
 142 |             tbody.appendChild(tr);
 143 |         });
 144 |         if (!d.recentGrades || d.recentGrades.length === 0) {
 145 |             tbody.innerHTML = '<tr><td colspan="3" class="text-muted text-center">No graded work yet</td></tr>';
 146 |         }
 147 | 
 148 |         renderTrend(d.trend || []);
 149 |         new bootstrap.Modal(document.getElementById('studentModal')).show();
 150 |     })
 151 |     .catch(console.error);
 152 | }
 153 | 
 154 | function renderTrend(data) {
 155 |     var ctx = document.getElementById('trendChart');
 156 |     if (!ctx || typeof Chart === 'undefined') return;
 157 |     if (trendChart) trendChart.destroy();
 158 |     var labels = data.map(function (d) { return d.label; });
 159 |     var values = data.map(function (d) { return d.value; });
 160 |     trendChart = new Chart(ctx.getContext('2d'), {
 161 |         type: 'line',
 162 |         data: {
 163 |             labels: labels.length ? labels : ['-'],
 164 |             datasets: [{
 165 |                 data: values.length ? values : [0],
 166 |                 borderColor: '#f17f54',
 167 |                 backgroundColor: 'rgba(241,127,84,0.1)',
 168 |                 fill: true,
 169 |                 tension: 0.4,
 170 |                 pointRadius: 2
 171 |             }]
 172 |         },
 173 |         options: {
 174 |             responsive: true,
 175 |             plugins: { legend: { display: false } },
 176 |             scales: { y: { beginAtZero: true, max: 100 } }
 177 |         }
 178 |     });
 179 | }
 180 | 
 181 | function gradeColor(g) {
 182 |     if (!g || g === '-') return '';
 183 |     if (g.indexOf('A') === 0) return 'grade-a';
 184 |     if (g.indexOf('B') === 0) return 'grade-b';
 185 |     if (g.indexOf('C') === 0) return 'grade-c';
 186 |     if (g.indexOf('D') === 0 || g.indexOf('F') === 0) return 'grade-f';
 187 |     return '';
 188 | }
 189 | 
 190 | function escapeHtml(str) {
 191 |     if (str == null) return '';
 192 |     return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
 193 | }
```
