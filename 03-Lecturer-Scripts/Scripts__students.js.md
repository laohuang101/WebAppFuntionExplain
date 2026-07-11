# students.js
**Source:** `Pages/Lecturer/Scripts/students.js`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Enrolled students per course with progress counts.

## File overview

- **Total lines:** 193
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 2:** `trendChart` — script-level `const`/`let`/`var`
- **Line 4:** `studentsDt` — script-level `const`/`let`/`var`
- **Line 5:** `colors` — script-level `const`/`let`/`var`
- **Line 27:** `bg` — script-level `const`/`let`/`var`
- **Line 48:** `pct` — script-level `const`/`let`/`var`
- **Line 62:** `g` — script-level `const`/`let`/`var`
- **Line 99:** `res` — script-level `const`/`let`/`var`
- **Line 126:** `d` — script-level `const`/`let`/`var`
- **Line 133:** `tbody` — script-level `const`/`let`/`var`
- **Line 137:** `tr` — script-level `const`/`let`/`var`
- **Line 155:** `ctx` — script-level `const`/`let`/`var`
- **Line 158:** `labels` — script-level `const`/`let`/`var`
- **Line 159:** `values` — script-level `const`/`let`/`var`

## Functions / methods (10 found)

### `render` — lines 26–32

```javascript
function render(s, i)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters:** `s, i`
- **Local variables:** `bg`

#### Line-by-line (this function)

```javascript
  26 |             render: function (s, i) {
  27 |                 var bg = colors[i % colors.length];
  28 |                 return '<div class="d-flex align-items-center gap-2">' +
  29 |                 '<div class="student-avatar" style="background:' + bg + '">' + escapeHtml(s.initials || '?') + '</div>' +
  30 |                 '<div><div class="fw-semibold">' + escapeHtml(s.studentName) + '</div>' +
  31 |                 '<div class="text-muted small">' + escapeHtml(s.email || '') + '</div></div></div>';
  32 |             }
```

**Line notes**

- **L29:** Encode text to reduce XSS risk.
- **L30:** Encode text to reduce XSS risk.
- **L31:** Encode text to reduce XSS risk.

---

### `searchValue` — lines 33–33

```javascript
function searchValue(s)
```

#### Explanation

- **Purpose:** Implements `searchValue`.
- **Parameters:** `s`

#### Line-by-line (this function)

```javascript
  33 |             searchValue: function (s) { return (s.studentName || '') + ' ' + (s.email || ''); }
```

---

### `render` — lines 47–53

```javascript
function render(s)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters:** `s`
- **Local variables:** `pct`

#### Line-by-line (this function)

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

```javascript
function render(s)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters:** `s`
- **Local variables:** `g`

#### Line-by-line (this function)

```javascript
  61 |             render: function (s) {
  62 |                 var g = s.currentGrade || '-';
  63 |                 return '<span class="grade-badge ' + gradeColor(g) + '">' + escapeHtml(g) + '</span>';
  64 |             }
```

**Line notes**

- **L63:** Encode text to reduce XSS risk.

---

### `render` — lines 78–82

```javascript
function render(s)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters:** `s`

#### Line-by-line (this function)

```javascript
  78 |             render: function (s) {
  79 |                 return '<button type="button" class="btn btn-sm btn-link text-muted" ' +
  80 |                 'onclick="openDetail(' + s.uid + ', ' + s.cid + ')">' +
  81 |                 '<i class="fa-solid fa-chevron-right"></i></button>';
  82 |             }
```

---

### `loadStudents` — lines 88–113

```javascript
function loadStudents()
```

#### Explanation

- **Purpose:** Implements `loadStudents`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables:** `res`

#### Line-by-line (this function)

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

**Line notes**

- **L91:** HTTP request to server WebMethod/ashx.
- **L94:** JS object ↔ JSON text.
- **L102:** Get HTML element by id.
- **L103:** Encode text to reduce XSS risk.
- **L110:** Get HTML element by id.

---

### `openDetail` — lines 113–152

```javascript
function openDetail(uid, cid)
```

#### Explanation

- **Purpose:** Implements `openDetail`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters:** `uid, cid`
- **Local variables:** `res`, `d`, `tbody`, `tr`

#### Line-by-line (this function)

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

**Line notes**

- **L116:** HTTP request to server WebMethod/ashx.
- **L119:** JS object ↔ JSON text.
- **L127:** Get HTML element by id.
- **L128:** Get HTML element by id.
- **L129:** Get HTML element by id.
- **L130:** Get HTML element by id.
- **L131:** Get HTML element by id.
- **L132:** Get HTML element by id.
- **L134:** Get HTML element by id.
- **L135:** Update page HTML.
- **L138:** Update page HTML.
- **L139:** Encode text to reduce XSS risk.
- **L140:** Encode text to reduce XSS risk.
- **L141:** Encode text to reduce XSS risk.
- **L145:** Update page HTML.
- **L149:** Get HTML element by id.

---

### `renderTrend` — lines 152–179

```javascript
function renderTrend(data)
```

#### Explanation

- **Purpose:** Implements `renderTrend`.
- **Parameters:** `data`
- **Local variables:** `ctx`, `labels`, `values`

#### Line-by-line (this function)

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

**Line notes**

- **L155:** Get HTML element by id.
- **L156:** Dashboard chart/visualization.
- **L157:** Dashboard chart/visualization.
- **L160:** Dashboard chart/visualization.

---

### `gradeColor` — lines 179–188

```javascript
function gradeColor(g)
```

#### Explanation

- **Purpose:** Implements `gradeColor`.
- **Parameters:** `g`

#### Line-by-line (this function)

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

```javascript
function escapeHtml(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtml`.
- **Parameters:** `str`

#### Line-by-line (this function)

```javascript
 188 | 
 189 | 
 190 | function escapeHtml(str) {
 191 |     if (str == null) return '';
 192 |     return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
 193 | }
```

**Line notes**

- **L190:** Encode text to reduce XSS risk.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

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

**Line notes**

- **L3:** Dashboard chart/visualization.
- **L7:** DOM event handler.
- **L8:** In-memory result set from ADO.NET.
- **L9:** Get HTML element by id.
- **L10:** In-memory result set from ADO.NET.
- **L14:** In-memory result set from ADO.NET.
- **L29:** Encode text to reduce XSS risk.
- **L30:** Encode text to reduce XSS risk.
- **L31:** Encode text to reduce XSS risk.
- **L63:** Encode text to reduce XSS risk.
- **L91:** HTTP request to server WebMethod/ashx.
- **L94:** JS object ↔ JSON text.
- **L102:** Get HTML element by id.
- **L103:** Encode text to reduce XSS risk.
- **L110:** Get HTML element by id.
- **L116:** HTTP request to server WebMethod/ashx.
- **L119:** JS object ↔ JSON text.
- **L127:** Get HTML element by id.
- **L128:** Get HTML element by id.
- **L129:** Get HTML element by id.
- **L130:** Get HTML element by id.
- **L131:** Get HTML element by id.
- **L132:** Get HTML element by id.
- **L134:** Get HTML element by id.
- **L135:** Update page HTML.
- **L138:** Update page HTML.
- **L139:** Encode text to reduce XSS risk.
- **L140:** Encode text to reduce XSS risk.
- **L141:** Encode text to reduce XSS risk.
- **L145:** Update page HTML.
- **L149:** Get HTML element by id.
- **L155:** Get HTML element by id.
- **L156:** Dashboard chart/visualization.
- **L157:** Dashboard chart/visualization.
- **L160:** Dashboard chart/visualization.
- **L190:** Encode text to reduce XSS risk.

## Source snapshot (raw)

```javascript
/* Student Performance - EduDataTable (search / sort / filter / pagination) */

let trendChart = null;
let studentsDt = null;
const colors = ['#f59e0b', '#3b82f6', '#10b981', '#8b5cf6', '#ec4899'];

document.addEventListener('DOMContentLoaded', function () {
    if (typeof EduDataTable === 'undefined') {
        document.getElementById('studentsTableWrap').innerHTML =
        '<div class="text-danger p-3">DataTable component failed to load.</div>';
        return;
    }

    studentsDt = EduDataTable.create({
        container: '#studentsTableWrap',
        pageSize: 10,
        pageSizeOptions: [5, 10, 25, 50],
        searchPlaceholder: 'Search name, email, course...',
        emptyMessage: 'No enrolled students found.',
        columns: [
        {
            key: 'studentName',
            title: 'Student',
            sortable: true,
            search: true,
            render: function (s, i) {
                var bg = colors[i % colors.length];
                return '<div class="d-flex align-items-center gap-2">' +
                '<div class="student-avatar" style="background:' + bg + '">' + escapeHtml(s.initials || '?') + '</div>' +
                '<div><div class="fw-semibold">' + escapeHtml(s.studentName) + '</div>' +
                '<div class="text-muted small">' + escapeHtml(s.email || '') + '</div></div></div>';
            },
            searchValue: function (s) { return (s.studentName || '') + ' ' + (s.email || ''); }
        },
        {
            key: 'courseName',
            title: 'Course',
            sortable: true,
            filter: true,
            filterLabel: 'Course'
        },
        {
            key: 'progress',
            title: 'Progress',
            sortable: true,
            type: 'number',
            render: function (s) {
                var pct = Math.round(Number(s.progress) || 0);
                return '<div class="d-flex align-items-center gap-2" style="min-width:140px;">' +
                '<div class="progress flex-grow-1" style="height:8px;">' +
                '<div class="progress-bar" style="width:' + pct + '%;background:var(--primary-accent);"></div></div>' +
                '<span class="small text-muted">' + pct + '%</span></div>';
            }
        },
        {
            key: 'currentGrade',
            title: 'Grade',
            sortable: true,
            filter: true,
            filterLabel: 'Grade',
            render: function (s) {
                var g = s.currentGrade || '-';
                return '<span class="grade-badge ' + gradeColor(g) + '">' + escapeHtml(g) + '</span>';
            }
        },
        {
            key: 'lastActive',
            title: 'Last Active',
            sortable: true,
            cellClass: 'text-muted small'
        },
        {
            key: '_actions',
            title: '',
            sortable: false,
            search: false,
            cellClass: 'text-end',
            render: function (s) {
                return '<button type="button" class="btn btn-sm btn-link text-muted" ' +
                'onclick="openDetail(' + s.uid + ', ' + s.cid + ')">' +
                '<i class="fa-solid fa-chevron-right"></i></button>';
            }
        }
        ]
    });

    loadStudents();
});

function loadStudents() {
    fetch('Students.aspx/GetStudents', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ search: null }),
        credentials: 'same-origin'
    })
    .then(function (r) { return r.json(); })
    .then(function (data) {
        var res = data.d || data;
        if (res.notAuthenticated) { location.href = '/Pages/Authentication/Login.aspx'; return; }
        if (!res.success) {
            document.getElementById('studentsTableWrap').innerHTML =
            '<div class="text-danger p-3">' + escapeHtml(res.message || 'Error') + '</div>';
            return;
        }
        studentsDt.setData(res.students || []);
    })
    .catch(function (err) {
        console.error(err);
        document.getElementById('studentsTableWrap').innerHTML =
        '<div class="text-danger p-3">Network error loading students.</div>';
    });
}

function openDetail(uid, cid) {
    fetch('Students.aspx/GetStudentDetail', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ studentUid: uid, cid: cid }),
        credentials: 'same-origin'
    })
    .then(function (r) { return r.json(); })
    .then(function (data) {
        var res = data.d || data;
        if (!res.success) { alert(res.message || 'Failed'); return; }
        var d = res.detail;
        document.getElementById('mAvatar').innerText = d.initials || '?';
        document.getElementById('mName').innerText = d.studentName || '';
        document.getElementById('mMeta').innerText = (d.email || '') + ' · ' + (d.courseName || '');
        document.getElementById('mGrade').innerText = d.currentGrade || '-';
        document.getElementById('mProgress').innerText = Math.round(Number(d.progress) || 0) + '%';
        document.getElementById('mAttendance').innerText = Math.round(Number(d.attendance) || 0) + '%';

        var tbody = document.getElementById('mGradesBody');
        tbody.innerHTML = '';
        (d.recentGrades || []).forEach(function (g) {
            var tr = document.createElement('tr');
            tr.innerHTML =
            '<td>' + escapeHtml(g.assignment) + '</td>' +
            '<td class="text-muted small">' + escapeHtml(g.date) + '</td>' +
            '<td class="text-end text-success fw-semibold">' + escapeHtml(g.score) + '</td>';
            tbody.appendChild(tr);
        });
        if (!d.recentGrades || d.recentGrades.length === 0) {
            tbody.innerHTML = '<tr><td colspan="3" class="text-muted text-center">No graded work yet</td></tr>';
        }

        renderTrend(d.trend || []);
        new bootstrap.Modal(document.getElementById('studentModal')).show();
    })
    .catch(console.error);
}

function renderTrend(data) {
    var ctx = document.getElementById('trendChart');
    if (!ctx || typeof Chart === 'undefined') return;
    if (trendChart) trendChart.destroy();
    var labels = data.map(function (d) { return d.label; });
    var values = data.map(function (d) { return d.value; });
    trendChart = new Chart(ctx.getContext('2d'), {
        type: 'line',
        data: {
            labels: labels.length ? labels : ['-'],
            datasets: [{
                data: values.length ? values : [0],
                borderColor: '#f17f54',
                backgroundColor: 'rgba(241,127,84,0.1)',
                fill: true,
                tension: 0.4,
                pointRadius: 2
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true, max: 100 } }
        }
    });
}

function gradeColor(g) {
    if (!g || g === '-') return '';
    if (g.indexOf('A') === 0) return 'grade-a';
    if (g.indexOf('B') === 0) return 'grade-b';
    if (g.indexOf('C') === 0) return 'grade-c';
    if (g.indexOf('D') === 0 || g.indexOf('F') === 0) return 'grade-f';
    return '';
}

function escapeHtml(str) {
    if (str == null) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

```
