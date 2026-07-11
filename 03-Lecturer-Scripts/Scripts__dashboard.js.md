# dashboard.js
**Source:** `Pages/Lecturer/Scripts/dashboard.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 404
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 3:** `__chartJsLoading` — script-level `const`/`let`/`var` — **Holds “chart Js Loading” for this scope.**
- **Line 4:** `__chartPending` — script-level `const`/`let`/`var` — **Holds “chart Pending” for this scope.**
- **Line 10:** `s` — script-level `const`/`let`/`var` — **String value or submission-related object.**
- **Line 21:** `targets` — script-level `const`/`let`/`var` — **Often a collection related to targets (plural name).**
- **Line 27:** `done` — script-level `const`/`let`/`var` — **Holds “done” for this scope.**
- **Line 28:** `io` — script-level `const`/`let`/`var` — **Holds “io” for this scope.**
- **Line 41:** `enrollmentChart` — script-level `const`/`let`/`var` — **Holds “enrollment Chart” for this scope.**
- **Line 43:** `gradeChart` — script-level `const`/`let`/`var` — **Holds “grade Chart” for this scope.**
- **Line 53:** `ctxEl` — script-level `const`/`let`/`var` — **Holds “ctx El” for this scope.**
- **Line 55:** `ctx` — script-level `const`/`let`/`var` — **Current HTTP request context (Request, Response, Session).**
- **Line 82:** `labels` — script-level `const`/`let`/`var` — **Often a collection related to labels (plural name).**
- **Line 84:** `values` — script-level `const`/`let`/`var` — **Often a collection related to values (plural name).**
- **Line 116:** `defaultLabels` — script-level `const`/`let`/`var` — **Often a collection related to default Labels (plural name).**
- **Line 169:** `currentSubmissionId` — script-level `const`/`let`/`var` — **Holds “current Submission Id” for this scope.**
- **Line 171:** `dashSubmissionsDt` — script-level `const`/`let`/`var` — **Holds “dash Submissions Dt” for this scope.**
- **Line 172:** `dashSubmissionsMap` — script-level `const`/`let`/`var` — **Holds “dash Submissions Map” for this scope.**
- **Line 180:** `wrap` — script-level `const`/`let`/`var` — **Holds “wrap” for this scope.**
- **Line 182:** `colors` — script-level `const`/`let`/`var` — **Often a collection related to colors (plural name).**
- **Line 228:** `rows` — script-level `const`/`let`/`var` — **Collection of rows.**
- **Line 236:** `sub` — script-level `const`/`let`/`var` — **Holds “sub” for this scope.**
- **Line 251:** `res` — script-level `const`/`let`/`var` — **Result object returned from fetch/WebMethod (`data.d` unwrapped).**
- **Line 253:** `blob` — script-level `const`/`let`/`var` — **Holds “blob” for this scope.**
- **Line 254:** `a` — script-level `const`/`let`/`var` — **Holds “a” for this scope.**
- **Line 276:** `resObj` — script-level `const`/`let`/`var` — **Holds “res Obj” for this scope.**
- **Line 304:** `enrollData` — script-level `const`/`let`/`var` — **Holds “enroll Data” for this scope.**
- **Line 306:** `gradeData` — script-level `const`/`let`/`var` — **Holds “grade Data” for this scope.**
- **Line 332:** `avatar` — script-level `const`/`let`/`var` — **Holds “avatar” for this scope.**
- **Line 343:** `txtScore` — script-level `const`/`let`/`var` — **UI control reference (txt Score).**
- **Line 352:** `myModal` — script-level `const`/`let`/`var` — **Holds “my Modal” for this scope.**
- **Line 357:** `score` — script-level `const`/`let`/`var` — **Points earned or max points depending on context.**
- **Line 358:** `review` — script-level `const`/`let`/`var` — **Holds “review” for this scope.**
- **Line 359:** `errDiv` — script-level `const`/`let`/`var` — **Holds “err Div” for this scope.**
- **Line 387:** `modalEl` — script-level `const`/`let`/`var` — **Holds “modal El” for this scope.**
- **Line 388:** `modal` — script-level `const`/`let`/`var` — **Holds “modal” for this scope.**

## Functions / methods (18 found)

### `ensureChartJs` — lines 4–18

```javascript
function ensureChartJs(cb)
```

#### Explanation

- **Purpose:** Implements `ensureChartJs`.
- **Parameters (what each means):**
- `cb` — Holds “cb” for this scope.
- **Local variables (what each means):**
- `s` — String value or submission-related object.

#### Line-by-line (this function)

```javascript
   4 | 
   5 | 
   6 | function ensureChartJs(cb) {
   7 |     if (typeof Chart !== 'undefined') { cb && cb(); return; }
   8 |     if (__chartJsLoading) { __chartJsLoading.then(function () { cb && cb(); }); return; }
   9 |     __chartJsLoading = new Promise(function (resolve, reject) {
  10 |         var s = document.createElement('script');
  11 |         s.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js';
  12 |         s.async = true;
  13 |         s.onload = function () { resolve(); };
  14 |         s.onerror = function () { reject(new Error('Chart.js failed to load')); };
  15 |         document.head.appendChild(s);
  16 |     });
  17 |     __chartJsLoading.then(function () { cb && cb(); }).catch(function (e) { console.error(e); });
  18 | }
```

**Line notes** (what code + variables mean)

- **L6:** Dashboard chart/visualization.
- **L7:** Dashboard chart/visualization.
- **L10:** `s` means: String value or submission-related object.
- **L11:** Dashboard chart/visualization.
- **L14:** Dashboard chart/visualization.

---

### `whenChartsVisible` — lines 18–40

```javascript
function whenChartsVisible(run)
```

#### Explanation

- **Purpose:** Implements `whenChartsVisible`.
- **Parameters (what each means):**
- `run` — Holds “run” for this scope.
- **Local variables (what each means):**
- `targets` — Often a collection related to targets (plural name).
- `done` — Holds “done” for this scope.
- `io` — Holds “io” for this scope.  Newly constructed object.
- `i` — Loop index (0-based counter in for-loops).  Literal number `0`.

#### Line-by-line (this function)

```javascript
  18 | 
  19 | 
  20 | function whenChartsVisible(run) {
  21 |     var targets = [
  22 |         document.getElementById('chartEnrollmentTrend'),
  23 |         document.getElementById('chartGradeDistribution')
  24 |     ].filter(Boolean);
  25 |     if (!targets.length) { run(); return; }
  26 |     if (!('IntersectionObserver' in window)) { run(); return; }
  27 |     var done = false;
  28 |     var io = new IntersectionObserver(function (entries) {
  29 |         if (done) return;
  30 |         for (var i = 0; i < entries.length; i++) {
  31 |             if (entries[i].isIntersecting) {
  32 |                 done = true;
  33 |                 io.disconnect();
  34 |                 run();
  35 |                 break;
  36 |             }
  37 |         }
  38 |     }, { rootMargin: '120px', threshold: 0.05 });
  39 |     targets.forEach(function (el) { io.observe(el); });
  40 | }
```

**Line notes** (what code + variables mean)

- **L20:** Dashboard chart/visualization.
- **L21:** `targets` means: Often a collection related to targets (plural name).
- **L22:** Get HTML element by id.
- **L23:** Get HTML element by id.
- **L27:** `done` means: Holds “done” for this scope.
- **L28:** `io` means: Holds “io” for this scope.  Newly constructed object.

---

### `renderEnrollmentTrendWithChart` — lines 43–112

```javascript
function renderEnrollmentTrendWithChart(data)
```

#### Explanation

- **Purpose:** Implements `renderEnrollmentTrendWithChart`.
- **Parameters (what each means):**
- `data` — Holds “data” for this scope.
- **Local variables (what each means):**
- `ctxEl` — Holds “ctx El” for this scope.  DOM element from the page.
- `ctx` — Current HTTP request context (Request, Response, Session).
- `labels` — Often a collection related to labels (plural name).
- `values` — Often a collection related to values (plural name).

#### Line-by-line (this function)

```javascript
  43 | 
  44 | 
  45 |   function renderEnrollmentTrendWithChart(data) {
  46 |   try {
  47 |   if (!data || !Array.isArray(data) || data.length === 0) {
  48 |   // destroy existing chart and show empty state
  49 |   if (enrollmentChart) {
  50 |   try { enrollmentChart.destroy(); } catch(e){}
  51 |   enrollmentChart = null;
  52 |   }
  53 |   const ctxEl = document.getElementById('chartEnrollmentTrend');
  54 |   if (ctxEl) {
  55 |   const ctx = ctxEl.getContext('2d');
  56 |   ctx.clearRect(0, 0, ctxEl.width, ctxEl.height);
  57 |   // draw "No data" text
  58 |   ctx.font = '16px Arial';
  59 |   ctx.fillStyle = '#9ca3af';
  60 |   ctx.textAlign = 'center';
  61 |   ctx.textBaseline = 'middle';
  62 |   ctx.fillText('No enrollment data', ctxEl.width / 2, ctxEl.height / 2);
  63 |   }
  64 |   return;
  65 |   }
  66 | 
  67 |   if (typeof Chart === 'undefined') {
  68 |   console.warn('Chart.js not available; cannot render enrollment chart.');
  69 |   // draw simple text as fallback
  70 |   const ctxEl = document.getElementById('chartEnrollmentTrend');
  71 |   if (ctxEl) {
  72 |   const ctx = ctxEl.getContext('2d');
  73 |   ctx.clearRect(0, 0, ctxEl.width, ctxEl.height);
  74 |   ctx.font = '16px Arial';
  75 |   ctx.fillStyle = '#9ca3af';
  76 |   ctx.textAlign = 'center';
  77 |   ctx.textBaseline = 'middle';
  78 |   ctx.fillText('Chart library blocked by browser. Enable CDN or use local file.', ctxEl.width / 2, ctxEl.height / 2);
  79 |   }
  80 |   return;
  81 |   }
  82 | 
  83 |   const labels = data.map(d => d.label);
  84 |   const values = data.map(d => d.value);
  85 |   const ctx = document.getElementById('chartEnrollmentTrend').getContext('2d');
  86 |   if (enrollmentChart) enrollmentChart.destroy();
  87 |   enrollmentChart = new Chart(ctx, {
  88 |   type: 'line',
  89 |   data: {
  90 |   labels: labels,
  91 |   datasets: [{
  92 |   label: 'Enrollments',
  93 |   data: values,
  94 |   fill: true,
  95 |   backgroundColor: 'rgba(241,127,84,0.12)',
  96 |   borderColor: '#f17f54',
  97 |   tension: 0.4,
  98 |   pointRadius: 3
  99 |   }]
 100 |   },
 101 |   options: {
 102 |   responsive: true,
 103 |   maintainAspectRatio: false,
 104 |   scales: {
 105 |   y: { beginAtZero: true, ticks: { precision: 0 } }
 106 |   }
 107 |   }
 108 |   });
 109 |   } catch (err) {
 110 |   console.error('Error rendering enrollment chart:', err);
 111 |   }
 112 |   }
```

**Line notes** (what code + variables mean)

- **L45:** Dashboard chart/visualization.
- **L46:** Error handling block.
- **L49:** Dashboard chart/visualization.
- **L50:** Error handling block.
- **L51:** Dashboard chart/visualization.
- **L53:** Get HTML element by id. | `ctxEl` means: Holds “ctx El” for this scope.  DOM element from the page.
- **L55:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L67:** Dashboard chart/visualization.
- **L68:** Dashboard chart/visualization.
- **L70:** Get HTML element by id. | `ctxEl` means: Holds “ctx El” for this scope.  DOM element from the page.
- **L72:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L78:** Dashboard chart/visualization.
- **L83:** `labels` means: Often a collection related to labels (plural name).
- **L84:** `values` means: Often a collection related to values (plural name).
- **L85:** Get HTML element by id. | `ctx` means: Current HTTP request context (Request, Response, Session).  DOM element from the page.
- **L86:** Dashboard chart/visualization.
- **L87:** Dashboard chart/visualization.

---

### `renderGradeDistributionWithChart` — lines 112–163

```javascript
function renderGradeDistributionWithChart(data)
```

#### Explanation

- **Purpose:** Implements `renderGradeDistributionWithChart`.
- **Parameters (what each means):**
- `data` — Holds “data” for this scope.
- **Local variables (what each means):**
- `defaultLabels` — Often a collection related to default Labels (plural name).
- `ctx` — Current HTTP request context (Request, Response, Session).  DOM element from the page.
- `labels` — Often a collection related to labels (plural name).
- `values` — Often a collection related to values (plural name).

#### Line-by-line (this function)

```javascript
 112 | 
 113 | 
 114 |   function renderGradeDistributionWithChart(data) {
 115 |   try {
 116 |   const defaultLabels = ['A', 'B', 'C', 'D', 'F'];
 117 |   if (!data || !Array.isArray(data) || data.length === 0) {
 118 |   // render zeroed chart so layout is consistent
 119 |   if (gradeChart) gradeChart.destroy();
 120 |   const ctx = document.getElementById('chartGradeDistribution').getContext('2d');
 121 |   gradeChart = new Chart(ctx, {
 122 |   type: 'bar',
 123 |   data: {
 124 |   labels: defaultLabels,
 125 |   datasets: [{
 126 |   label: 'Students',
 127 |   data: [0, 0, 0, 0, 0],
 128 |   backgroundColor: ['#f17f54','#3b82f6','#10b981','#f59e0b','#ef4444']
 129 |   }]
 130 |   },
 131 |   options: {
 132 |   responsive: true,
 133 |   maintainAspectRatio: false,
 134 |   scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
 135 |   }
 136 |   });
 137 |   return;
 138 |   }
 139 | 
 140 |   const labels = data.map(d => d.label);
 141 |   const values = data.map(d => d.value);
 142 |   const ctx = document.getElementById('chartGradeDistribution').getContext('2d');
 143 |   if (gradeChart) gradeChart.destroy();
 144 |   gradeChart = new Chart(ctx, {
 145 |   type: 'bar',
 146 |   data: {
 147 |   labels: labels,
 148 |   datasets: [{
 149 |   label: 'Students',
 150 |   data: values,
 151 |   backgroundColor: ['#f17f54','#3b82f6','#10b981','#f59e0b','#ef4444']
 152 |   }]
 153 |   },
 154 |   options: {
 155 |   responsive: true,
 156 |   maintainAspectRatio: false,
 157 |   scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
 158 |   }
 159 |   });
 160 |   } catch (err) {
 161 |   console.error('Error rendering grade distribution chart:', err);
 162 |   }
 163 |   }
```

**Line notes** (what code + variables mean)

- **L114:** Dashboard chart/visualization.
- **L115:** Error handling block.
- **L116:** `defaultLabels` means: Often a collection related to default Labels (plural name).
- **L119:** Dashboard chart/visualization.
- **L120:** Get HTML element by id. | `ctx` means: Current HTTP request context (Request, Response, Session).  DOM element from the page.
- **L121:** Dashboard chart/visualization.
- **L140:** `labels` means: Often a collection related to labels (plural name).
- **L141:** `values` means: Often a collection related to values (plural name).
- **L142:** Get HTML element by id. | `ctx` means: Current HTTP request context (Request, Response, Session).  DOM element from the page.
- **L143:** Dashboard chart/visualization.
- **L144:** Dashboard chart/visualization.

---

### `escapeHtmlDash` — lines 172–404

```javascript
function escapeHtmlDash(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtmlDash`.
- **ASP.NET WebMethod:** Called from browser JS via `Page.aspx/MethodName` POST JSON.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters (what each means):**
- `str` — String value: str.
- **Local variables (what each means):**
- `wrap` — Holds “wrap” for this scope.  DOM element from the page.
- `colors` — Often a collection related to colors (plural name).
- `rows` — Collection of rows.
- `sub` — Holds “sub” for this scope.
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `blob` — Holds “blob” for this scope.  Newly constructed object.
- `a` — Holds “a” for this scope.
- `resObj` — Holds “res Obj” for this scope.
- `enrollData` — Holds “enroll Data” for this scope.
- `gradeData` — Holds “grade Data” for this scope.
- `avatar` — Holds “avatar” for this scope.  DOM element from the page.
- `txtScore` — UI control reference (txt Score).  DOM element from the page.
- `myModal` — Holds “my Modal” for this scope.  DOM element from the page.
- `score` — Points earned or max points depending on context.  DOM element from the page.
- `review` — Holds “review” for this scope.  DOM element from the page.
- `errDiv` — Holds “err Div” for this scope.  DOM element from the page.
- `modalEl` — Holds “modal El” for this scope.  DOM element from the page.
- `modal` — Holds “modal” for this scope.

#### Line-by-line (this function)

```javascript
 172 | 
 173 | 
 174 |     function escapeHtmlDash(str) {
 175 |     if (str == null) return '';
 176 |     return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
 177 |   }
 178 | 
 179 |   function renderDashSubmissions(list) {
 180 |   var wrap = document.getElementById('dashSubmissionsWrap');
 181 |   if (!wrap) return;
 182 |   var colors = ['#f59e0b', '#3b82f6', '#10b981', '#ec4899', '#8b5cf6'];
 183 |   dashSubmissionsMap = {};
 184 |   (list || []).forEach(function (s) { dashSubmissionsMap[s.sid] = s; });
 185 | 
 186 |   if (typeof EduDataTable === 'undefined') {
 187 |   wrap.innerHTML = '<div class="text-muted p-3">No table component.</div>';
 188 |   return;
 189 |   }
 190 |   if (!dashSubmissionsDt) {
 191 |   dashSubmissionsDt = EduDataTable.create({
 192 |   container: wrap,
 193 |   pageSize: 8,
 194 |   pageSizeOptions: [5, 8, 15, 25],
 195 |   searchPlaceholder: 'Search student, assignment, course...',
 196 |   emptyMessage: 'No recent submissions found.',
 197 |   tableClass: 'table table-hover submissions-table mb-0 edt-table',
 198 |   columns: [
 199 |   {
 200 |   key: 'studentName', title: 'Student', sortable: true,
 201 |   render: function (sub, i) {
 202 |   return '<div class="d-flex align-items-center"><div class="student-avatar me-2" style="background-color:' +
 203 |     colors[i % colors.length] + ';">' + escapeHtmlDash(sub.initials || '?') +
 204 |     '</div><span class="fw-semibold text-dark">' + escapeHtmlDash(sub.studentName) + '</span></div>';
 205 | },
 206 | searchValue: function (s) { return (s.studentName || '') + ' ' + (s.studentEmail || ''); }
 207 | },
 208 | { key: 'assignmentTitle', title: 'Assignment', sortable: true, filter: true, filterLabel: 'Assignment' },
 209 | { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },
 210 | { key: 'timeText', title: 'Time', sortable: true, cellClass: 'text-muted small',
 211 | sortValue: function (s) { return s.timestamp || s.timeText || ''; }, type: 'date' },
 212 | {
 213 | key: 'status', title: 'Action', sortable: true, filter: true, filterLabel: 'Status',
 214 | render: function (sub) {
 215 | if (sub.isGraded) {
 216 | return '<span class="badge-graded"><i class="fa-solid fa-circle-check"></i> Graded</span>';
 217 | }
 218 | return '<button type="button" class="btn btn-grade-now" onclick="openGradeModalBySid(' +
 219 | sub.sid + ')">Grade Now</button>';
 220 | },
 221 | sortValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; },
 222 | searchValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
 223 | }
 224 | ]
 225 | });
 226 | }
 227 | // Normalize status field for filter
 228 | var rows = (list || []).map(function (s) {
 229 | s.status = s.isGraded ? 'Graded' : 'Pending';
 230 | return s;
 231 | });
 232 | dashSubmissionsDt.setData(rows);
 233 | }
 234 | 
 235 | function openGradeModalBySid(sid) {
 236 | var sub = dashSubmissionsMap[sid];
 237 | if (sub) openGradeModal(sub);
 238 | }
 239 | 
 240 | // dashboard initialization is deferred until Chart.js and chart helper functions are available (handled at bottom of page)
 241 | 
 242 | function exportDashGradesCsv() {
 243 |   fetch(window.location.pathname + '/ExportGradesCsv', {
 244 |     method: 'POST',
 245 |     headers: { 'Content-Type': 'application/json' },
 246 |     body: JSON.stringify({ cid: 0 }),
 247 |     credentials: 'same-origin'
 248 |   })
 249 |   .then(function (r) { return r.json(); })
 250 |   .then(function (data) {
 251 |     var res = (data && data.d) ? (data.d.d || data.d) : data;
 252 |     if (!res || !res.success) { alert((res && res.message) || 'Export failed'); return; }
 253 |     var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });
 254 |     var a = document.createElement('a');
 255 |     a.href = URL.createObjectURL(blob);
 256 |     a.download = res.fileName || 'grades.csv';
 257 |     document.body.appendChild(a);
 258 |     a.click();
 259 |     setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 400);
 260 |   })
 261 |   .catch(function () { alert('Network error exporting grades.'); });
 262 | }
 263 | 
 264 | function loadDashboardData() {
 265 | // Fetch dashboard statistics and submissions from code-behind
 266 | fetch(window.location.pathname + '/GetDashboardData', {
 267 | method: 'POST',
 268 | headers: {
 269 | 'Content-Type': 'application/json'
 270 | }
 271 | })
 272 | .then(res => res.json())
 273 | .then(data => {
 274 | // Normalize ASP.NET PageMethod response which may be wrapped as { d: {...} }
 275 | // In some environments it can be double-wrapped: { d: { d: {...} } }
 276 | let resObj = null;
 277 | if (data && data.d) {
 278 | resObj = data.d.d ? data.d.d : data.d;
 279 | } else {
 280 | resObj = data;
 281 | }
 282 | if (!resObj || resObj.notAuthenticated) {
 283 | // Redirect to login
 284 | window.location.href = '/Pages/Authentication/Login.aspx';
 285 | return;
 286 | }
 287 | if (!resObj.success) {
 288 | console.error('Failed to load dashboard:', resObj.message || resObj);
 289 | return;
 290 | }
 291 | 
 292 | if (resObj.success) {
 293 | // Update Stats
 294 | document.getElementById('lblTotalStudents').innerText = formatNumber(resObj.totalStudents);
 295 | document.getElementById('lblActiveCourses').innerText = resObj.activeCourses;
 296 | document.getElementById('lblPendingGrading').innerText = resObj.pendingGrading;
 297 | if (!resObj.hasGrades) {
 298 | document.getElementById('lblAverageGrade').innerText = "N/A";
 299 | } else {
 300 | document.getElementById('lblAverageGrade').innerText = resObj.averageGrade + "%";
 301 | }
 302 | 
 303 | // Stats + table first; charts only when visible (lazy Chart.js CDN)
 304 | var enrollData = (resObj.enrollmentTrends && Array.isArray(resObj.enrollmentTrends))
 305 |   ? resObj.enrollmentTrends : [];
 306 | var gradeData = (resObj.gradeDistribution && Array.isArray(resObj.gradeDistribution))
 307 |   ? resObj.gradeDistribution : [];
 308 | whenChartsVisible(function () {
 309 |   ensureChartJs(function () {
 310 |     renderEnrollmentTrendWithChart(enrollData);
 311 |     renderGradeDistributionWithChart(gradeData);
 312 |   });
 313 | });
 314 | 
 315 | // Submissions table with search / sort / filter / pagination
 316 | renderDashSubmissions(resObj.submissions || []);
 317 | }
 318 | })
 319 | .catch(err => {
 320 | console.error("Error loading dashboard data: ", err);
 321 | });
 322 | }
 323 | 
 324 | function formatNumber(num) {
 325 | return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
 326 | }
 327 | 
 328 | function openGradeModal(sub) {
 329 | currentSubmissionId = sub.sid;
 330 | 
 331 | // Set student initials and name
 332 | const avatar = document.getElementById('modalStudentAvatar');
 333 | avatar.innerText = sub.initials;
 334 | avatar.style.backgroundColor = '#f17f54';
 335 | document.getElementById('modalStudentName').innerText = sub.studentName;
 336 | 
 337 | // Set details
 338 | document.getElementById('modalAssignment').innerText = sub.assignmentTitle;
 339 | document.getElementById('modalAnswer').innerText = sub.studentAnswer;
 340 | document.getElementById('lblMaxScore').innerText = "/ " + sub.maxScore;
 341 | 
 342 | // Reset inputs
 343 | const txtScore = document.getElementById('txtScore');
 344 | txtScore.value = 0;
 345 | txtScore.max = sub.maxScore;
 346 | document.getElementById('txtReview').value = '';
 347 | 
 348 | // Hide error
 349 | document.getElementById('modalErrorMessage').style.display = 'none';
 350 | 
 351 | // Show modal
 352 | const myModal = new bootstrap.Modal(document.getElementById('gradingModal'));
 353 | myModal.show();
 354 | }
 355 | 
 356 | function submitGrading() {
 357 | const score = parseInt(document.getElementById('txtScore').value);
 358 | const review = document.getElementById('txtReview').value.trim();
 359 | const errDiv = document.getElementById('modalErrorMessage');
 360 | 
 361 | errDiv.style.display = 'none';
 362 | 
 363 | if (isNaN(score) || score < 0) {
 364 | errDiv.innerText = "Please enter a valid score.";
 365 | errDiv.style.display = 'block';
 366 | return;
 367 | }
 368 | 
 369 | // Call SaveGrade WebMethod
 370 | fetch(window.location.pathname + '/SaveGrade', {
 371 | method: 'POST',
 372 | headers: {
 373 | 'Content-Type': 'application/json'
 374 | },
 375 | body: JSON.stringify({
 376 | sid: currentSubmissionId,
 377 | score: score,
 378 | review: review
 379 | })
 380 | })
 381 | .then(res => res.json())
 382 | .then(data => {
 383 | let resObj = null;
 384 | if (data && data.d) resObj = data.d.d ? data.d.d : data.d; else resObj = data;
 385 | if (resObj && resObj.success) {
 386 | // Close Modal
 387 | const modalEl = document.getElementById('gradingModal');
 388 | const modal = bootstrap.Modal.getInstance(modalEl);
 389 | modal.hide();
 390 | 
 391 | // Refresh dashboard data
 392 | loadDashboardData();
 393 | } else {
 394 | errDiv.innerText = resObj.message || "Failed to save grade.";
 395 | errDiv.style.display = 'block';
 396 | }
 397 | })
 398 | .catch(err => {
 399 | errDiv.innerText = "Network error. Please try again.";
 400 | errDiv.style.display = 'block';
 401 | console.error(err);
 402 | });
 403 | }
 404 | 
```

**Line notes** (what code + variables mean)

- **L174:** Encode text to reduce XSS risk.
- **L180:** Get HTML element by id. | `wrap` means: Holds “wrap” for this scope.  DOM element from the page.
- **L182:** `colors` means: Often a collection related to colors (plural name).
- **L186:** In-memory result set from ADO.NET.
- **L187:** Update page HTML.
- **L191:** In-memory result set from ADO.NET.
- **L203:** Encode text to reduce XSS risk.
- **L204:** Encode text to reduce XSS risk.
- **L228:** `rows` means: Collection of rows.
- **L236:** `sub` means: Holds “sub” for this scope.
- **L242:** CSV export.
- **L243:** HTTP request to server WebMethod/ashx.
- **L246:** JS object ↔ JSON text.
- **L251:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L253:** CSV export. | `blob` means: Holds “blob” for this scope.  Newly constructed object.
- **L254:** `a` means: Holds “a” for this scope.
- **L256:** CSV export.
- **L266:** HTTP request to server WebMethod/ashx.
- **L276:** `resObj` means: Holds “res Obj” for this scope.
- **L294:** Get HTML element by id.
- **L295:** Get HTML element by id.
- **L296:** Get HTML element by id.
- **L298:** Get HTML element by id.
- **L300:** Get HTML element by id.
- **L304:** `enrollData` means: Holds “enroll Data” for this scope.
- **L306:** `gradeData` means: Holds “grade Data” for this scope.
- **L308:** Dashboard chart/visualization.
- **L309:** Dashboard chart/visualization.
- **L310:** Dashboard chart/visualization.
- **L311:** Dashboard chart/visualization.
- **L332:** Get HTML element by id. | `avatar` means: Holds “avatar” for this scope.  DOM element from the page.
- **L335:** Get HTML element by id.
- **L338:** Get HTML element by id.
- **L339:** Get HTML element by id.
- **L340:** Get HTML element by id.
- **L343:** Get HTML element by id. | `txtScore` means: UI control reference (txt Score).  DOM element from the page.
- **L346:** Get HTML element by id.
- **L349:** Get HTML element by id.
- **L352:** Get HTML element by id. | `myModal` means: Holds “my Modal” for this scope.  DOM element from the page.
- **L357:** Get HTML element by id. | `score` means: Points earned or max points depending on context.  DOM element from the page.
- **L358:** Get HTML element by id. | `review` means: Holds “review” for this scope.  DOM element from the page.
- **L359:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L370:** HTTP request to server WebMethod/ashx.
- **L375:** JS object ↔ JSON text.
- **L383:** `resObj` means: Holds “res Obj” for this scope.
- **L387:** Get HTML element by id. | `modalEl` means: Holds “modal El” for this scope.  DOM element from the page.
- **L388:** `modal` means: Holds “modal” for this scope.

---

### `renderDashSubmissions` — lines 177–233

```javascript
function renderDashSubmissions(list)
```

#### Explanation

- **Purpose:** Implements `renderDashSubmissions`.
- **Parameters (what each means):**
- `list` — In-memory collection being built for JSON return.
- **Local variables (what each means):**
- `wrap` — Holds “wrap” for this scope.  DOM element from the page.
- `colors` — Often a collection related to colors (plural name).
- `rows` — Collection of rows.

#### Line-by-line (this function)

```javascript
 177 | 
 178 | 
 179 |   function renderDashSubmissions(list) {
 180 |   var wrap = document.getElementById('dashSubmissionsWrap');
 181 |   if (!wrap) return;
 182 |   var colors = ['#f59e0b', '#3b82f6', '#10b981', '#ec4899', '#8b5cf6'];
 183 |   dashSubmissionsMap = {};
 184 |   (list || []).forEach(function (s) { dashSubmissionsMap[s.sid] = s; });
 185 | 
 186 |   if (typeof EduDataTable === 'undefined') {
 187 |   wrap.innerHTML = '<div class="text-muted p-3">No table component.</div>';
 188 |   return;
 189 |   }
 190 |   if (!dashSubmissionsDt) {
 191 |   dashSubmissionsDt = EduDataTable.create({
 192 |   container: wrap,
 193 |   pageSize: 8,
 194 |   pageSizeOptions: [5, 8, 15, 25],
 195 |   searchPlaceholder: 'Search student, assignment, course...',
 196 |   emptyMessage: 'No recent submissions found.',
 197 |   tableClass: 'table table-hover submissions-table mb-0 edt-table',
 198 |   columns: [
 199 |   {
 200 |   key: 'studentName', title: 'Student', sortable: true,
 201 |   render: function (sub, i) {
 202 |   return '<div class="d-flex align-items-center"><div class="student-avatar me-2" style="background-color:' +
 203 |     colors[i % colors.length] + ';">' + escapeHtmlDash(sub.initials || '?') +
 204 |     '</div><span class="fw-semibold text-dark">' + escapeHtmlDash(sub.studentName) + '</span></div>';
 205 | },
 206 | searchValue: function (s) { return (s.studentName || '') + ' ' + (s.studentEmail || ''); }
 207 | },
 208 | { key: 'assignmentTitle', title: 'Assignment', sortable: true, filter: true, filterLabel: 'Assignment' },
 209 | { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },
 210 | { key: 'timeText', title: 'Time', sortable: true, cellClass: 'text-muted small',
 211 | sortValue: function (s) { return s.timestamp || s.timeText || ''; }, type: 'date' },
 212 | {
 213 | key: 'status', title: 'Action', sortable: true, filter: true, filterLabel: 'Status',
 214 | render: function (sub) {
 215 | if (sub.isGraded) {
 216 | return '<span class="badge-graded"><i class="fa-solid fa-circle-check"></i> Graded</span>';
 217 | }
 218 | return '<button type="button" class="btn btn-grade-now" onclick="openGradeModalBySid(' +
 219 | sub.sid + ')">Grade Now</button>';
 220 | },
 221 | sortValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; },
 222 | searchValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
 223 | }
 224 | ]
 225 | });
 226 | }
 227 | // Normalize status field for filter
 228 | var rows = (list || []).map(function (s) {
 229 | s.status = s.isGraded ? 'Graded' : 'Pending';
 230 | return s;
 231 | });
 232 | dashSubmissionsDt.setData(rows);
 233 | }
```

**Line notes** (what code + variables mean)

- **L180:** Get HTML element by id. | `wrap` means: Holds “wrap” for this scope.  DOM element from the page.
- **L182:** `colors` means: Often a collection related to colors (plural name).
- **L186:** In-memory result set from ADO.NET.
- **L187:** Update page HTML.
- **L191:** In-memory result set from ADO.NET.
- **L203:** Encode text to reduce XSS risk.
- **L204:** Encode text to reduce XSS risk.
- **L228:** `rows` means: Collection of rows.

---

### `render` — lines 201–205

```javascript
function render(sub, i)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters (what each means):**
- `sub` — Holds “sub” for this scope.
- `i` — Loop index (0-based counter in for-loops).

#### Line-by-line (this function)

```javascript
 201 |   render: function (sub, i) {
 202 |   return '<div class="d-flex align-items-center"><div class="student-avatar me-2" style="background-color:' +
 203 |     colors[i % colors.length] + ';">' + escapeHtmlDash(sub.initials || '?') +
 204 |     '</div><span class="fw-semibold text-dark">' + escapeHtmlDash(sub.studentName) + '</span></div>';
 205 | }
```

**Line notes** (what code + variables mean)

- **L203:** Encode text to reduce XSS risk.
- **L204:** Encode text to reduce XSS risk.

---

### `searchValue` — lines 206–206

```javascript
function searchValue(s)
```

#### Explanation

- **Purpose:** Implements `searchValue`.
- **Parameters (what each means):**
- `s` — String value or submission-related object.

#### Line-by-line (this function)

```javascript
 206 | searchValue: function (s) { return (s.studentName || '') + ' ' + (s.studentEmail || ''); }
```

---

### `sortValue` — lines 211–211

```javascript
function sortValue(s)
```

#### Explanation

- **Purpose:** Implements `sortValue`.
- **Parameters (what each means):**
- `s` — String value or submission-related object.

#### Line-by-line (this function)

```javascript
 211 | sortValue: function (s) { return s.timestamp || s.timeText || ''; }
```

---

### `render` — lines 214–220

```javascript
function render(sub)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters (what each means):**
- `sub` — Holds “sub” for this scope.

#### Line-by-line (this function)

```javascript
 214 | render: function (sub) {
 215 | if (sub.isGraded) {
 216 | return '<span class="badge-graded"><i class="fa-solid fa-circle-check"></i> Graded</span>';
 217 | }
 218 | return '<button type="button" class="btn btn-grade-now" onclick="openGradeModalBySid(' +
 219 | sub.sid + ')">Grade Now</button>';
 220 | }
```

---

### `sortValue` — lines 221–221

```javascript
function sortValue(s)
```

#### Explanation

- **Purpose:** Implements `sortValue`.
- **Parameters (what each means):**
- `s` — String value or submission-related object.

#### Line-by-line (this function)

```javascript
 221 | sortValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
```

---

### `searchValue` — lines 222–222

```javascript
function searchValue(s)
```

#### Explanation

- **Purpose:** Implements `searchValue`.
- **Parameters (what each means):**
- `s` — String value or submission-related object.

#### Line-by-line (this function)

```javascript
 222 | searchValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
```

---

### `openGradeModalBySid` — lines 233–238

```javascript
function openGradeModalBySid(sid)
```

#### Explanation

- **Purpose:** Implements `openGradeModalBySid`.
- **Parameters (what each means):**
- `sid` — Submission ID (CWSubmissions.SID).
- **Local variables (what each means):**
- `sub` — Holds “sub” for this scope.

#### Line-by-line (this function)

```javascript
 233 | 
 234 | 
 235 | function openGradeModalBySid(sid) {
 236 | var sub = dashSubmissionsMap[sid];
 237 | if (sub) openGradeModal(sub);
 238 | }
```

**Line notes** (what code + variables mean)

- **L236:** `sub` means: Holds “sub” for this scope.

---

### `exportDashGradesCsv` — lines 240–262

```javascript
function exportDashGradesCsv()
```

#### Explanation

- **Purpose:** Implements `exportDashGradesCsv`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables (what each means):**
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `blob` — Holds “blob” for this scope.  Newly constructed object.
- `a` — Holds “a” for this scope.

#### Line-by-line (this function)

```javascript
 240 | 
 241 | 
 242 | function exportDashGradesCsv() {
 243 |   fetch(window.location.pathname + '/ExportGradesCsv', {
 244 |     method: 'POST',
 245 |     headers: { 'Content-Type': 'application/json' },
 246 |     body: JSON.stringify({ cid: 0 }),
 247 |     credentials: 'same-origin'
 248 |   })
 249 |   .then(function (r) { return r.json(); })
 250 |   .then(function (data) {
 251 |     var res = (data && data.d) ? (data.d.d || data.d) : data;
 252 |     if (!res || !res.success) { alert((res && res.message) || 'Export failed'); return; }
 253 |     var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });
 254 |     var a = document.createElement('a');
 255 |     a.href = URL.createObjectURL(blob);
 256 |     a.download = res.fileName || 'grades.csv';
 257 |     document.body.appendChild(a);
 258 |     a.click();
 259 |     setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 400);
 260 |   })
 261 |   .catch(function () { alert('Network error exporting grades.'); });
 262 | }
```

**Line notes** (what code + variables mean)

- **L242:** CSV export.
- **L243:** HTTP request to server WebMethod/ashx.
- **L246:** JS object ↔ JSON text.
- **L251:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L253:** CSV export. | `blob` means: Holds “blob” for this scope.  Newly constructed object.
- **L254:** `a` means: Holds “a” for this scope.
- **L256:** CSV export.

---

### `loadDashboardData` — lines 262–322

```javascript
function loadDashboardData()
```

#### Explanation

- **Purpose:** Implements `loadDashboardData`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Navigation:** Redirects the browser.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `resObj` — Holds “res Obj” for this scope.
- `enrollData` — Holds “enroll Data” for this scope.
- `gradeData` — Holds “grade Data” for this scope.

#### Line-by-line (this function)

```javascript
 262 | 
 263 | 
 264 | function loadDashboardData() {
 265 | // Fetch dashboard statistics and submissions from code-behind
 266 | fetch(window.location.pathname + '/GetDashboardData', {
 267 | method: 'POST',
 268 | headers: {
 269 | 'Content-Type': 'application/json'
 270 | }
 271 | })
 272 | .then(res => res.json())
 273 | .then(data => {
 274 | // Normalize ASP.NET PageMethod response which may be wrapped as { d: {...} }
 275 | // In some environments it can be double-wrapped: { d: { d: {...} } }
 276 | let resObj = null;
 277 | if (data && data.d) {
 278 | resObj = data.d.d ? data.d.d : data.d;
 279 | } else {
 280 | resObj = data;
 281 | }
 282 | if (!resObj || resObj.notAuthenticated) {
 283 | // Redirect to login
 284 | window.location.href = '/Pages/Authentication/Login.aspx';
 285 | return;
 286 | }
 287 | if (!resObj.success) {
 288 | console.error('Failed to load dashboard:', resObj.message || resObj);
 289 | return;
 290 | }
 291 | 
 292 | if (resObj.success) {
 293 | // Update Stats
 294 | document.getElementById('lblTotalStudents').innerText = formatNumber(resObj.totalStudents);
 295 | document.getElementById('lblActiveCourses').innerText = resObj.activeCourses;
 296 | document.getElementById('lblPendingGrading').innerText = resObj.pendingGrading;
 297 | if (!resObj.hasGrades) {
 298 | document.getElementById('lblAverageGrade').innerText = "N/A";
 299 | } else {
 300 | document.getElementById('lblAverageGrade').innerText = resObj.averageGrade + "%";
 301 | }
 302 | 
 303 | // Stats + table first; charts only when visible (lazy Chart.js CDN)
 304 | var enrollData = (resObj.enrollmentTrends && Array.isArray(resObj.enrollmentTrends))
 305 |   ? resObj.enrollmentTrends : [];
 306 | var gradeData = (resObj.gradeDistribution && Array.isArray(resObj.gradeDistribution))
 307 |   ? resObj.gradeDistribution : [];
 308 | whenChartsVisible(function () {
 309 |   ensureChartJs(function () {
 310 |     renderEnrollmentTrendWithChart(enrollData);
 311 |     renderGradeDistributionWithChart(gradeData);
 312 |   });
 313 | });
 314 | 
 315 | // Submissions table with search / sort / filter / pagination
 316 | renderDashSubmissions(resObj.submissions || []);
 317 | }
 318 | })
 319 | .catch(err => {
 320 | console.error("Error loading dashboard data: ", err);
 321 | });
 322 | }
```

**Line notes** (what code + variables mean)

- **L266:** HTTP request to server WebMethod/ashx.
- **L276:** `resObj` means: Holds “res Obj” for this scope.
- **L294:** Get HTML element by id.
- **L295:** Get HTML element by id.
- **L296:** Get HTML element by id.
- **L298:** Get HTML element by id.
- **L300:** Get HTML element by id.
- **L304:** `enrollData` means: Holds “enroll Data” for this scope.
- **L306:** `gradeData` means: Holds “grade Data” for this scope.
- **L308:** Dashboard chart/visualization.
- **L309:** Dashboard chart/visualization.
- **L310:** Dashboard chart/visualization.
- **L311:** Dashboard chart/visualization.

---

### `formatNumber` — lines 322–326

```javascript
function formatNumber(num)
```

#### Explanation

- **Purpose:** Implements `formatNumber`.
- **Parameters (what each means):**
- `num` — Numeric count of items related to `num`.

#### Line-by-line (this function)

```javascript
 322 | 
 323 | 
 324 | function formatNumber(num) {
 325 | return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
 326 | }
```

---

### `openGradeModal` — lines 326–354

```javascript
function openGradeModal(sub)
```

#### Explanation

- **Purpose:** Implements `openGradeModal`.
- **Parameters (what each means):**
- `sub` — Holds “sub” for this scope.
- **Local variables (what each means):**
- `avatar` — Holds “avatar” for this scope.  DOM element from the page.
- `txtScore` — UI control reference (txt Score).  DOM element from the page.
- `myModal` — Holds “my Modal” for this scope.  DOM element from the page.

#### Line-by-line (this function)

```javascript
 326 | 
 327 | 
 328 | function openGradeModal(sub) {
 329 | currentSubmissionId = sub.sid;
 330 | 
 331 | // Set student initials and name
 332 | const avatar = document.getElementById('modalStudentAvatar');
 333 | avatar.innerText = sub.initials;
 334 | avatar.style.backgroundColor = '#f17f54';
 335 | document.getElementById('modalStudentName').innerText = sub.studentName;
 336 | 
 337 | // Set details
 338 | document.getElementById('modalAssignment').innerText = sub.assignmentTitle;
 339 | document.getElementById('modalAnswer').innerText = sub.studentAnswer;
 340 | document.getElementById('lblMaxScore').innerText = "/ " + sub.maxScore;
 341 | 
 342 | // Reset inputs
 343 | const txtScore = document.getElementById('txtScore');
 344 | txtScore.value = 0;
 345 | txtScore.max = sub.maxScore;
 346 | document.getElementById('txtReview').value = '';
 347 | 
 348 | // Hide error
 349 | document.getElementById('modalErrorMessage').style.display = 'none';
 350 | 
 351 | // Show modal
 352 | const myModal = new bootstrap.Modal(document.getElementById('gradingModal'));
 353 | myModal.show();
 354 | }
```

**Line notes** (what code + variables mean)

- **L332:** Get HTML element by id. | `avatar` means: Holds “avatar” for this scope.  DOM element from the page.
- **L335:** Get HTML element by id.
- **L338:** Get HTML element by id.
- **L339:** Get HTML element by id.
- **L340:** Get HTML element by id.
- **L343:** Get HTML element by id. | `txtScore` means: UI control reference (txt Score).  DOM element from the page.
- **L346:** Get HTML element by id.
- **L349:** Get HTML element by id.
- **L352:** Get HTML element by id. | `myModal` means: Holds “my Modal” for this scope.  DOM element from the page.

---

### `submitGrading` — lines 354–403

```javascript
function submitGrading()
```

#### Explanation

- **Purpose:** Implements `submitGrading`.
- **ASP.NET WebMethod:** Called from browser JS via `Page.aspx/MethodName` POST JSON.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables (what each means):**
- `score` — Points earned or max points depending on context.  DOM element from the page.
- `review` — Holds “review” for this scope.  DOM element from the page.
- `errDiv` — Holds “err Div” for this scope.  DOM element from the page.
- `resObj` — Holds “res Obj” for this scope.
- `modalEl` — Holds “modal El” for this scope.  DOM element from the page.
- `modal` — Holds “modal” for this scope.

#### Line-by-line (this function)

```javascript
 354 | 
 355 | 
 356 | function submitGrading() {
 357 | const score = parseInt(document.getElementById('txtScore').value);
 358 | const review = document.getElementById('txtReview').value.trim();
 359 | const errDiv = document.getElementById('modalErrorMessage');
 360 | 
 361 | errDiv.style.display = 'none';
 362 | 
 363 | if (isNaN(score) || score < 0) {
 364 | errDiv.innerText = "Please enter a valid score.";
 365 | errDiv.style.display = 'block';
 366 | return;
 367 | }
 368 | 
 369 | // Call SaveGrade WebMethod
 370 | fetch(window.location.pathname + '/SaveGrade', {
 371 | method: 'POST',
 372 | headers: {
 373 | 'Content-Type': 'application/json'
 374 | },
 375 | body: JSON.stringify({
 376 | sid: currentSubmissionId,
 377 | score: score,
 378 | review: review
 379 | })
 380 | })
 381 | .then(res => res.json())
 382 | .then(data => {
 383 | let resObj = null;
 384 | if (data && data.d) resObj = data.d.d ? data.d.d : data.d; else resObj = data;
 385 | if (resObj && resObj.success) {
 386 | // Close Modal
 387 | const modalEl = document.getElementById('gradingModal');
 388 | const modal = bootstrap.Modal.getInstance(modalEl);
 389 | modal.hide();
 390 | 
 391 | // Refresh dashboard data
 392 | loadDashboardData();
 393 | } else {
 394 | errDiv.innerText = resObj.message || "Failed to save grade.";
 395 | errDiv.style.display = 'block';
 396 | }
 397 | })
 398 | .catch(err => {
 399 | errDiv.innerText = "Network error. Please try again.";
 400 | errDiv.style.display = 'block';
 401 | console.error(err);
 402 | });
 403 | }
```

**Line notes** (what code + variables mean)

- **L357:** Get HTML element by id. | `score` means: Points earned or max points depending on context.  DOM element from the page.
- **L358:** Get HTML element by id. | `review` means: Holds “review” for this scope.  DOM element from the page.
- **L359:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L370:** HTTP request to server WebMethod/ashx.
- **L375:** JS object ↔ JSON text.
- **L383:** `resObj` means: Holds “res Obj” for this scope.
- **L387:** Get HTML element by id. | `modalEl` means: Holds “modal El” for this scope.  DOM element from the page.
- **L388:** `modal` means: Holds “modal” for this scope.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```javascript
   1 | 
   2 | /* Lazy Chart.js loader — only fetch when chart canvases are near viewport */
   3 | var __chartJsLoading = null;
   4 | var __chartPending = { enrollment: null, grade: null };
   5 | 
   6 | function ensureChartJs(cb) {
   7 |     if (typeof Chart !== 'undefined') { cb && cb(); return; }
   8 |     if (__chartJsLoading) { __chartJsLoading.then(function () { cb && cb(); }); return; }
   9 |     __chartJsLoading = new Promise(function (resolve, reject) {
  10 |         var s = document.createElement('script');
  11 |         s.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js';
  12 |         s.async = true;
  13 |         s.onload = function () { resolve(); };
  14 |         s.onerror = function () { reject(new Error('Chart.js failed to load')); };
  15 |         document.head.appendChild(s);
  16 |     });
  17 |     __chartJsLoading.then(function () { cb && cb(); }).catch(function (e) { console.error(e); });
  18 | }
  19 | 
  20 | function whenChartsVisible(run) {
  21 |     var targets = [
  22 |         document.getElementById('chartEnrollmentTrend'),
  23 |         document.getElementById('chartGradeDistribution')
  24 |     ].filter(Boolean);
  25 |     if (!targets.length) { run(); return; }
  26 |     if (!('IntersectionObserver' in window)) { run(); return; }
  27 |     var done = false;
  28 |     var io = new IntersectionObserver(function (entries) {
  29 |         if (done) return;
  30 |         for (var i = 0; i < entries.length; i++) {
  31 |             if (entries[i].isIntersecting) {
  32 |                 done = true;
  33 |                 io.disconnect();
  34 |                 run();
  35 |                 break;
  36 |             }
  37 |         }
  38 |     }, { rootMargin: '120px', threshold: 0.05 });
  39 |     targets.forEach(function (el) { io.observe(el); });
  40 | }
  41 | 
  42 | let enrollmentChart = null;
  43 |   let gradeChart = null;
  44 | 
  45 |   function renderEnrollmentTrendWithChart(data) {
  46 |   try {
  47 |   if (!data || !Array.isArray(data) || data.length === 0) {
  48 |   // destroy existing chart and show empty state
  49 |   if (enrollmentChart) {
  50 |   try { enrollmentChart.destroy(); } catch(e){}
  51 |   enrollmentChart = null;
  52 |   }
  53 |   const ctxEl = document.getElementById('chartEnrollmentTrend');
  54 |   if (ctxEl) {
  55 |   const ctx = ctxEl.getContext('2d');
  56 |   ctx.clearRect(0, 0, ctxEl.width, ctxEl.height);
  57 |   // draw "No data" text
  58 |   ctx.font = '16px Arial';
  59 |   ctx.fillStyle = '#9ca3af';
  60 |   ctx.textAlign = 'center';
  61 |   ctx.textBaseline = 'middle';
  62 |   ctx.fillText('No enrollment data', ctxEl.width / 2, ctxEl.height / 2);
  63 |   }
  64 |   return;
  65 |   }
  66 | 
  67 |   if (typeof Chart === 'undefined') {
  68 |   console.warn('Chart.js not available; cannot render enrollment chart.');
  69 |   // draw simple text as fallback
  70 |   const ctxEl = document.getElementById('chartEnrollmentTrend');
  71 |   if (ctxEl) {
  72 |   const ctx = ctxEl.getContext('2d');
  73 |   ctx.clearRect(0, 0, ctxEl.width, ctxEl.height);
  74 |   ctx.font = '16px Arial';
  75 |   ctx.fillStyle = '#9ca3af';
  76 |   ctx.textAlign = 'center';
  77 |   ctx.textBaseline = 'middle';
  78 |   ctx.fillText('Chart library blocked by browser. Enable CDN or use local file.', ctxEl.width / 2, ctxEl.height / 2);
  79 |   }
  80 |   return;
  81 |   }
  82 | 
  83 |   const labels = data.map(d => d.label);
  84 |   const values = data.map(d => d.value);
  85 |   const ctx = document.getElementById('chartEnrollmentTrend').getContext('2d');
  86 |   if (enrollmentChart) enrollmentChart.destroy();
  87 |   enrollmentChart = new Chart(ctx, {
  88 |   type: 'line',
  89 |   data: {
  90 |   labels: labels,
  91 |   datasets: [{
  92 |   label: 'Enrollments',
  93 |   data: values,
  94 |   fill: true,
  95 |   backgroundColor: 'rgba(241,127,84,0.12)',
  96 |   borderColor: '#f17f54',
  97 |   tension: 0.4,
  98 |   pointRadius: 3
  99 |   }]
 100 |   },
 101 |   options: {
 102 |   responsive: true,
 103 |   maintainAspectRatio: false,
 104 |   scales: {
 105 |   y: { beginAtZero: true, ticks: { precision: 0 } }
 106 |   }
 107 |   }
 108 |   });
 109 |   } catch (err) {
 110 |   console.error('Error rendering enrollment chart:', err);
 111 |   }
 112 |   }
 113 | 
 114 |   function renderGradeDistributionWithChart(data) {
 115 |   try {
 116 |   const defaultLabels = ['A', 'B', 'C', 'D', 'F'];
 117 |   if (!data || !Array.isArray(data) || data.length === 0) {
 118 |   // render zeroed chart so layout is consistent
 119 |   if (gradeChart) gradeChart.destroy();
 120 |   const ctx = document.getElementById('chartGradeDistribution').getContext('2d');
 121 |   gradeChart = new Chart(ctx, {
 122 |   type: 'bar',
 123 |   data: {
 124 |   labels: defaultLabels,
 125 |   datasets: [{
 126 |   label: 'Students',
 127 |   data: [0, 0, 0, 0, 0],
 128 |   backgroundColor: ['#f17f54','#3b82f6','#10b981','#f59e0b','#ef4444']
 129 |   }]
 130 |   },
 131 |   options: {
 132 |   responsive: true,
 133 |   maintainAspectRatio: false,
 134 |   scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
 135 |   }
 136 |   });
 137 |   return;
 138 |   }
 139 | 
 140 |   const labels = data.map(d => d.label);
 141 |   const values = data.map(d => d.value);
 142 |   const ctx = document.getElementById('chartGradeDistribution').getContext('2d');
 143 |   if (gradeChart) gradeChart.destroy();
 144 |   gradeChart = new Chart(ctx, {
 145 |   type: 'bar',
 146 |   data: {
 147 |   labels: labels,
 148 |   datasets: [{
 149 |   label: 'Students',
 150 |   data: values,
 151 |   backgroundColor: ['#f17f54','#3b82f6','#10b981','#f59e0b','#ef4444']
 152 |   }]
 153 |   },
 154 |   options: {
 155 |   responsive: true,
 156 |   maintainAspectRatio: false,
 157 |   scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
 158 |   }
 159 |   });
 160 |   } catch (err) {
 161 |   console.error('Error rendering grade distribution chart:', err);
 162 |   }
 163 |   }
 164 | 
 165 |   // Initialize dashboard when page loads
 166 |   document.addEventListener('DOMContentLoaded', function () {
 167 |   loadDashboardData();
 168 | });
 169 | 
 170 | let currentSubmissionId = null;
 171 |     let dashSubmissionsDt = null;
 172 |     let dashSubmissionsMap = {};
 173 | 
 174 |     function escapeHtmlDash(str) {
 175 |     if (str == null) return '';
 176 |     return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
 177 |   }
 178 | 
 179 |   function renderDashSubmissions(list) {
 180 |   var wrap = document.getElementById('dashSubmissionsWrap');
 181 |   if (!wrap) return;
 182 |   var colors = ['#f59e0b', '#3b82f6', '#10b981', '#ec4899', '#8b5cf6'];
 183 |   dashSubmissionsMap = {};
 184 |   (list || []).forEach(function (s) { dashSubmissionsMap[s.sid] = s; });
 185 | 
 186 |   if (typeof EduDataTable === 'undefined') {
 187 |   wrap.innerHTML = '<div class="text-muted p-3">No table component.</div>';
 188 |   return;
 189 |   }
 190 |   if (!dashSubmissionsDt) {
 191 |   dashSubmissionsDt = EduDataTable.create({
 192 |   container: wrap,
 193 |   pageSize: 8,
 194 |   pageSizeOptions: [5, 8, 15, 25],
 195 |   searchPlaceholder: 'Search student, assignment, course...',
 196 |   emptyMessage: 'No recent submissions found.',
 197 |   tableClass: 'table table-hover submissions-table mb-0 edt-table',
 198 |   columns: [
 199 |   {
 200 |   key: 'studentName', title: 'Student', sortable: true,
 201 |   render: function (sub, i) {
 202 |   return '<div class="d-flex align-items-center"><div class="student-avatar me-2" style="background-color:' +
 203 |     colors[i % colors.length] + ';">' + escapeHtmlDash(sub.initials || '?') +
 204 |     '</div><span class="fw-semibold text-dark">' + escapeHtmlDash(sub.studentName) + '</span></div>';
 205 | },
 206 | searchValue: function (s) { return (s.studentName || '') + ' ' + (s.studentEmail || ''); }
 207 | },
 208 | { key: 'assignmentTitle', title: 'Assignment', sortable: true, filter: true, filterLabel: 'Assignment' },
 209 | { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },
 210 | { key: 'timeText', title: 'Time', sortable: true, cellClass: 'text-muted small',
 211 | sortValue: function (s) { return s.timestamp || s.timeText || ''; }, type: 'date' },
 212 | {
 213 | key: 'status', title: 'Action', sortable: true, filter: true, filterLabel: 'Status',
 214 | render: function (sub) {
 215 | if (sub.isGraded) {
 216 | return '<span class="badge-graded"><i class="fa-solid fa-circle-check"></i> Graded</span>';
 217 | }
 218 | return '<button type="button" class="btn btn-grade-now" onclick="openGradeModalBySid(' +
 219 | sub.sid + ')">Grade Now</button>';
 220 | },
 221 | sortValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; },
 222 | searchValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
 223 | }
 224 | ]
 225 | });
 226 | }
 227 | // Normalize status field for filter
 228 | var rows = (list || []).map(function (s) {
 229 | s.status = s.isGraded ? 'Graded' : 'Pending';
 230 | return s;
 231 | });
 232 | dashSubmissionsDt.setData(rows);
 233 | }
 234 | 
 235 | function openGradeModalBySid(sid) {
 236 | var sub = dashSubmissionsMap[sid];
 237 | if (sub) openGradeModal(sub);
 238 | }
 239 | 
 240 | // dashboard initialization is deferred until Chart.js and chart helper functions are available (handled at bottom of page)
 241 | 
 242 | function exportDashGradesCsv() {
 243 |   fetch(window.location.pathname + '/ExportGradesCsv', {
 244 |     method: 'POST',
 245 |     headers: { 'Content-Type': 'application/json' },
 246 |     body: JSON.stringify({ cid: 0 }),
 247 |     credentials: 'same-origin'
 248 |   })
 249 |   .then(function (r) { return r.json(); })
 250 |   .then(function (data) {
 251 |     var res = (data && data.d) ? (data.d.d || data.d) : data;
 252 |     if (!res || !res.success) { alert((res && res.message) || 'Export failed'); return; }
 253 |     var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });
 254 |     var a = document.createElement('a');
 255 |     a.href = URL.createObjectURL(blob);
 256 |     a.download = res.fileName || 'grades.csv';
 257 |     document.body.appendChild(a);
 258 |     a.click();
 259 |     setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 400);
 260 |   })
 261 |   .catch(function () { alert('Network error exporting grades.'); });
 262 | }
 263 | 
 264 | function loadDashboardData() {
 265 | // Fetch dashboard statistics and submissions from code-behind
 266 | fetch(window.location.pathname + '/GetDashboardData', {
 267 | method: 'POST',
 268 | headers: {
 269 | 'Content-Type': 'application/json'
 270 | }
 271 | })
 272 | .then(res => res.json())
 273 | .then(data => {
 274 | // Normalize ASP.NET PageMethod response which may be wrapped as { d: {...} }
 275 | // In some environments it can be double-wrapped: { d: { d: {...} } }
 276 | let resObj = null;
 277 | if (data && data.d) {
 278 | resObj = data.d.d ? data.d.d : data.d;
 279 | } else {
 280 | resObj = data;
 281 | }
 282 | if (!resObj || resObj.notAuthenticated) {
 283 | // Redirect to login
 284 | window.location.href = '/Pages/Authentication/Login.aspx';
 285 | return;
 286 | }
 287 | if (!resObj.success) {
 288 | console.error('Failed to load dashboard:', resObj.message || resObj);
 289 | return;
 290 | }
 291 | 
 292 | if (resObj.success) {
 293 | // Update Stats
 294 | document.getElementById('lblTotalStudents').innerText = formatNumber(resObj.totalStudents);
 295 | document.getElementById('lblActiveCourses').innerText = resObj.activeCourses;
 296 | document.getElementById('lblPendingGrading').innerText = resObj.pendingGrading;
 297 | if (!resObj.hasGrades) {
 298 | document.getElementById('lblAverageGrade').innerText = "N/A";
 299 | } else {
 300 | document.getElementById('lblAverageGrade').innerText = resObj.averageGrade + "%";
 301 | }
 302 | 
 303 | // Stats + table first; charts only when visible (lazy Chart.js CDN)
 304 | var enrollData = (resObj.enrollmentTrends && Array.isArray(resObj.enrollmentTrends))
 305 |   ? resObj.enrollmentTrends : [];
 306 | var gradeData = (resObj.gradeDistribution && Array.isArray(resObj.gradeDistribution))
 307 |   ? resObj.gradeDistribution : [];
 308 | whenChartsVisible(function () {
 309 |   ensureChartJs(function () {
 310 |     renderEnrollmentTrendWithChart(enrollData);
 311 |     renderGradeDistributionWithChart(gradeData);
 312 |   });
 313 | });
 314 | 
 315 | // Submissions table with search / sort / filter / pagination
 316 | renderDashSubmissions(resObj.submissions || []);
 317 | }
 318 | })
 319 | .catch(err => {
 320 | console.error("Error loading dashboard data: ", err);
 321 | });
 322 | }
 323 | 
 324 | function formatNumber(num) {
 325 | return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
 326 | }
 327 | 
 328 | function openGradeModal(sub) {
 329 | currentSubmissionId = sub.sid;
 330 | 
 331 | // Set student initials and name
 332 | const avatar = document.getElementById('modalStudentAvatar');
 333 | avatar.innerText = sub.initials;
 334 | avatar.style.backgroundColor = '#f17f54';
 335 | document.getElementById('modalStudentName').innerText = sub.studentName;
 336 | 
 337 | // Set details
 338 | document.getElementById('modalAssignment').innerText = sub.assignmentTitle;
 339 | document.getElementById('modalAnswer').innerText = sub.studentAnswer;
 340 | document.getElementById('lblMaxScore').innerText = "/ " + sub.maxScore;
 341 | 
 342 | // Reset inputs
 343 | const txtScore = document.getElementById('txtScore');
 344 | txtScore.value = 0;
 345 | txtScore.max = sub.maxScore;
 346 | document.getElementById('txtReview').value = '';
 347 | 
 348 | // Hide error
 349 | document.getElementById('modalErrorMessage').style.display = 'none';
 350 | 
 351 | // Show modal
 352 | const myModal = new bootstrap.Modal(document.getElementById('gradingModal'));
 353 | myModal.show();
 354 | }
 355 | 
 356 | function submitGrading() {
 357 | const score = parseInt(document.getElementById('txtScore').value);
 358 | const review = document.getElementById('txtReview').value.trim();
 359 | const errDiv = document.getElementById('modalErrorMessage');
 360 | 
 361 | errDiv.style.display = 'none';
 362 | 
 363 | if (isNaN(score) || score < 0) {
 364 | errDiv.innerText = "Please enter a valid score.";
 365 | errDiv.style.display = 'block';
 366 | return;
 367 | }
 368 | 
 369 | // Call SaveGrade WebMethod
 370 | fetch(window.location.pathname + '/SaveGrade', {
 371 | method: 'POST',
 372 | headers: {
 373 | 'Content-Type': 'application/json'
 374 | },
 375 | body: JSON.stringify({
 376 | sid: currentSubmissionId,
 377 | score: score,
 378 | review: review
 379 | })
 380 | })
 381 | .then(res => res.json())
 382 | .then(data => {
 383 | let resObj = null;
 384 | if (data && data.d) resObj = data.d.d ? data.d.d : data.d; else resObj = data;
 385 | if (resObj && resObj.success) {
 386 | // Close Modal
 387 | const modalEl = document.getElementById('gradingModal');
 388 | const modal = bootstrap.Modal.getInstance(modalEl);
 389 | modal.hide();
 390 | 
 391 | // Refresh dashboard data
 392 | loadDashboardData();
 393 | } else {
 394 | errDiv.innerText = resObj.message || "Failed to save grade.";
 395 | errDiv.style.display = 'block';
 396 | }
 397 | })
 398 | .catch(err => {
 399 | errDiv.innerText = "Network error. Please try again.";
 400 | errDiv.style.display = 'block';
 401 | console.error(err);
 402 | });
 403 | }
 404 | 
```

**Line notes** (what code + variables mean)

- **L3:** `__chartJsLoading` means: Holds “chart Js Loading” for this scope.
- **L4:** `__chartPending` means: Holds “chart Pending” for this scope.
- **L6:** Dashboard chart/visualization.
- **L7:** Dashboard chart/visualization.
- **L10:** `s` means: String value or submission-related object.
- **L11:** Dashboard chart/visualization.
- **L14:** Dashboard chart/visualization.
- **L20:** Dashboard chart/visualization.
- **L21:** `targets` means: Often a collection related to targets (plural name).
- **L22:** Get HTML element by id.
- **L23:** Get HTML element by id.
- **L27:** `done` means: Holds “done” for this scope.
- **L28:** `io` means: Holds “io” for this scope.  Newly constructed object.
- **L42:** Dashboard chart/visualization. | `enrollmentChart` means: Holds “enrollment Chart” for this scope.
- **L43:** Dashboard chart/visualization. | `gradeChart` means: Holds “grade Chart” for this scope.
- **L45:** Dashboard chart/visualization.
- **L46:** Error handling block.
- **L49:** Dashboard chart/visualization.
- **L50:** Error handling block.
- **L51:** Dashboard chart/visualization.
- **L53:** Get HTML element by id. | `ctxEl` means: Holds “ctx El” for this scope.  DOM element from the page.
- **L55:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L67:** Dashboard chart/visualization.
- **L68:** Dashboard chart/visualization.
- **L70:** Get HTML element by id. | `ctxEl` means: Holds “ctx El” for this scope.  DOM element from the page.
- **L72:** `ctx` means: Current HTTP request context (Request, Response, Session).
- **L78:** Dashboard chart/visualization.
- **L83:** `labels` means: Often a collection related to labels (plural name).
- **L84:** `values` means: Often a collection related to values (plural name).
- **L85:** Get HTML element by id. | `ctx` means: Current HTTP request context (Request, Response, Session).  DOM element from the page.
- **L86:** Dashboard chart/visualization.
- **L87:** Dashboard chart/visualization.
- **L114:** Dashboard chart/visualization.
- **L115:** Error handling block.
- **L116:** `defaultLabels` means: Often a collection related to default Labels (plural name).
- **L119:** Dashboard chart/visualization.
- **L120:** Get HTML element by id. | `ctx` means: Current HTTP request context (Request, Response, Session).  DOM element from the page.
- **L121:** Dashboard chart/visualization.
- **L140:** `labels` means: Often a collection related to labels (plural name).
- **L141:** `values` means: Often a collection related to values (plural name).
- **L142:** Get HTML element by id. | `ctx` means: Current HTTP request context (Request, Response, Session).  DOM element from the page.
- **L143:** Dashboard chart/visualization.
- **L144:** Dashboard chart/visualization.
- **L166:** DOM event handler.
- **L170:** `currentSubmissionId` means: Holds “current Submission Id” for this scope.
- **L171:** `dashSubmissionsDt` means: Holds “dash Submissions Dt” for this scope.
- **L172:** `dashSubmissionsMap` means: Holds “dash Submissions Map” for this scope.
- **L174:** Encode text to reduce XSS risk.
- **L180:** Get HTML element by id. | `wrap` means: Holds “wrap” for this scope.  DOM element from the page.
- **L182:** `colors` means: Often a collection related to colors (plural name).
- **L186:** In-memory result set from ADO.NET.
- **L187:** Update page HTML.
- **L191:** In-memory result set from ADO.NET.
- **L203:** Encode text to reduce XSS risk.
- **L204:** Encode text to reduce XSS risk.
- **L228:** `rows` means: Collection of rows.
- **L236:** `sub` means: Holds “sub” for this scope.
- **L242:** CSV export.
- **L243:** HTTP request to server WebMethod/ashx.
- **L246:** JS object ↔ JSON text.
- **L251:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L253:** CSV export. | `blob` means: Holds “blob” for this scope.  Newly constructed object.
- **L254:** `a` means: Holds “a” for this scope.
- **L256:** CSV export.
- **L266:** HTTP request to server WebMethod/ashx.
- **L276:** `resObj` means: Holds “res Obj” for this scope.
- **L294:** Get HTML element by id.
- **L295:** Get HTML element by id.
- **L296:** Get HTML element by id.
- **L298:** Get HTML element by id.
- **L300:** Get HTML element by id.
- **L304:** `enrollData` means: Holds “enroll Data” for this scope.
- **L306:** `gradeData` means: Holds “grade Data” for this scope.
- **L308:** Dashboard chart/visualization.
- **L309:** Dashboard chart/visualization.
- **L310:** Dashboard chart/visualization.
- **L311:** Dashboard chart/visualization.
- **L332:** Get HTML element by id. | `avatar` means: Holds “avatar” for this scope.  DOM element from the page.
- **L335:** Get HTML element by id.
- **L338:** Get HTML element by id.
- **L339:** Get HTML element by id.
- **L340:** Get HTML element by id.
- **L343:** Get HTML element by id. | `txtScore` means: UI control reference (txt Score).  DOM element from the page.
- **L346:** Get HTML element by id.
- **L349:** Get HTML element by id.
- **L352:** Get HTML element by id. | `myModal` means: Holds “my Modal” for this scope.  DOM element from the page.
- **L357:** Get HTML element by id. | `score` means: Points earned or max points depending on context.  DOM element from the page.
- **L358:** Get HTML element by id. | `review` means: Holds “review” for this scope.  DOM element from the page.
- **L359:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L370:** HTTP request to server WebMethod/ashx.
- **L375:** JS object ↔ JSON text.
- **L383:** `resObj` means: Holds “res Obj” for this scope.
- **L387:** Get HTML element by id. | `modalEl` means: Holds “modal El” for this scope.  DOM element from the page.
- **L388:** `modal` means: Holds “modal” for this scope.

## Source snapshot (raw)

```javascript

/* Lazy Chart.js loader — only fetch when chart canvases are near viewport */
var __chartJsLoading = null;
var __chartPending = { enrollment: null, grade: null };

function ensureChartJs(cb) {
    if (typeof Chart !== 'undefined') { cb && cb(); return; }
    if (__chartJsLoading) { __chartJsLoading.then(function () { cb && cb(); }); return; }
    __chartJsLoading = new Promise(function (resolve, reject) {
        var s = document.createElement('script');
        s.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js';
        s.async = true;
        s.onload = function () { resolve(); };
        s.onerror = function () { reject(new Error('Chart.js failed to load')); };
        document.head.appendChild(s);
    });
    __chartJsLoading.then(function () { cb && cb(); }).catch(function (e) { console.error(e); });
}

function whenChartsVisible(run) {
    var targets = [
        document.getElementById('chartEnrollmentTrend'),
        document.getElementById('chartGradeDistribution')
    ].filter(Boolean);
    if (!targets.length) { run(); return; }
    if (!('IntersectionObserver' in window)) { run(); return; }
    var done = false;
    var io = new IntersectionObserver(function (entries) {
        if (done) return;
        for (var i = 0; i < entries.length; i++) {
            if (entries[i].isIntersecting) {
                done = true;
                io.disconnect();
                run();
                break;
            }
        }
    }, { rootMargin: '120px', threshold: 0.05 });
    targets.forEach(function (el) { io.observe(el); });
}

let enrollmentChart = null;
  let gradeChart = null;

  function renderEnrollmentTrendWithChart(data) {
  try {
  if (!data || !Array.isArray(data) || data.length === 0) {
  // destroy existing chart and show empty state
  if (enrollmentChart) {
  try { enrollmentChart.destroy(); } catch(e){}
  enrollmentChart = null;
  }
  const ctxEl = document.getElementById('chartEnrollmentTrend');
  if (ctxEl) {
  const ctx = ctxEl.getContext('2d');
  ctx.clearRect(0, 0, ctxEl.width, ctxEl.height);
  // draw "No data" text
  ctx.font = '16px Arial';
  ctx.fillStyle = '#9ca3af';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText('No enrollment data', ctxEl.width / 2, ctxEl.height / 2);
  }
  return;
  }

  if (typeof Chart === 'undefined') {
  console.warn('Chart.js not available; cannot render enrollment chart.');
  // draw simple text as fallback
  const ctxEl = document.getElementById('chartEnrollmentTrend');
  if (ctxEl) {
  const ctx = ctxEl.getContext('2d');
  ctx.clearRect(0, 0, ctxEl.width, ctxEl.height);
  ctx.font = '16px Arial';
  ctx.fillStyle = '#9ca3af';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText('Chart library blocked by browser. Enable CDN or use local file.', ctxEl.width / 2, ctxEl.height / 2);
  }
  return;
  }

  const labels = data.map(d => d.label);
  const values = data.map(d => d.value);
  const ctx = document.getElementById('chartEnrollmentTrend').getContext('2d');
  if (enrollmentChart) enrollmentChart.destroy();
  enrollmentChart = new Chart(ctx, {
  type: 'line',
  data: {
  labels: labels,
  datasets: [{
  label: 'Enrollments',
  data: values,
  fill: true,
  backgroundColor: 'rgba(241,127,84,0.12)',
  borderColor: '#f17f54',
  tension: 0.4,
  pointRadius: 3
  }]
  },
  options: {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
  y: { beginAtZero: true, ticks: { precision: 0 } }
  }
  }
  });
  } catch (err) {
  console.error('Error rendering enrollment chart:', err);
  }
  }

  function renderGradeDistributionWithChart(data) {
  try {
  const defaultLabels = ['A', 'B', 'C', 'D', 'F'];
  if (!data || !Array.isArray(data) || data.length === 0) {
  // render zeroed chart so layout is consistent
  if (gradeChart) gradeChart.destroy();
  const ctx = document.getElementById('chartGradeDistribution').getContext('2d');
  gradeChart = new Chart(ctx, {
  type: 'bar',
  data: {
  labels: defaultLabels,
  datasets: [{
  label: 'Students',
  data: [0, 0, 0, 0, 0],
  backgroundColor: ['#f17f54','#3b82f6','#10b981','#f59e0b','#ef4444']
  }]
  },
  options: {
  responsive: true,
  maintainAspectRatio: false,
  scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
  }
  });
  return;
  }

  const labels = data.map(d => d.label);
  const values = data.map(d => d.value);
  const ctx = document.getElementById('chartGradeDistribution').getContext('2d');
  if (gradeChart) gradeChart.destroy();
  gradeChart = new Chart(ctx, {
  type: 'bar',
  data: {
  labels: labels,
  datasets: [{
  label: 'Students',
  data: values,
  backgroundColor: ['#f17f54','#3b82f6','#10b981','#f59e0b','#ef4444']
  }]
  },
  options: {
  responsive: true,
  maintainAspectRatio: false,
  scales: { y: { beginAtZero: true, ticks: { precision: 0 } } }
  }
  });
  } catch (err) {
  console.error('Error rendering grade distribution chart:', err);
  }
  }

  // Initialize dashboard when page loads
  document.addEventListener('DOMContentLoaded', function () {
  loadDashboardData();
});

let currentSubmissionId = null;
    let dashSubmissionsDt = null;
    let dashSubmissionsMap = {};

    function escapeHtmlDash(str) {
    if (str == null) return '';
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function renderDashSubmissions(list) {
  var wrap = document.getElementById('dashSubmissionsWrap');
  if (!wrap) return;
  var colors = ['#f59e0b', '#3b82f6', '#10b981', '#ec4899', '#8b5cf6'];
  dashSubmissionsMap = {};
  (list || []).forEach(function (s) { dashSubmissionsMap[s.sid] = s; });

  if (typeof EduDataTable === 'undefined') {
  wrap.innerHTML = '<div class="text-muted p-3">No table component.</div>';
  return;
  }
  if (!dashSubmissionsDt) {
  dashSubmissionsDt = EduDataTable.create({
  container: wrap,
  pageSize: 8,
  pageSizeOptions: [5, 8, 15, 25],
  searchPlaceholder: 'Search student, assignment, course...',
  emptyMessage: 'No recent submissions found.',
  tableClass: 'table table-hover submissions-table mb-0 edt-table',
  columns: [
  {
  key: 'studentName', title: 'Student', sortable: true,
  render: function (sub, i) {
  return '<div class="d-flex align-items-center"><div class="student-avatar me-2" style="background-color:' +
    colors[i % colors.length] + ';">' + escapeHtmlDash(sub.initials || '?') +
    '</div><span class="fw-semibold text-dark">' + escapeHtmlDash(sub.studentName) + '</span></div>';
},
searchValue: function (s) { return (s.studentName || '') + ' ' + (s.studentEmail || ''); }
},
{ key: 'assignmentTitle', title: 'Assignment', sortable: true, filter: true, filterLabel: 'Assignment' },
{ key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },
{ key: 'timeText', title: 'Time', sortable: true, cellClass: 'text-muted small',
sortValue: function (s) { return s.timestamp || s.timeText || ''; }, type: 'date' },
{
key: 'status', title: 'Action', sortable: true, filter: true, filterLabel: 'Status',
render: function (sub) {
if (sub.isGraded) {
return '<span class="badge-graded"><i class="fa-solid fa-circle-check"></i> Graded</span>';
}
return '<button type="button" class="btn btn-grade-now" onclick="openGradeModalBySid(' +
sub.sid + ')">Grade Now</button>';
},
sortValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; },
searchValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
}
]
});
}
// Normalize status field for filter
var rows = (list || []).map(function (s) {
s.status = s.isGraded ? 'Graded' : 'Pending';
return s;
});
dashSubmissionsDt.setData(rows);
}

function openGradeModalBySid(sid) {
var sub = dashSubmissionsMap[sid];
if (sub) openGradeModal(sub);
}

// dashboard initialization is deferred until Chart.js and chart helper functions are available (handled at bottom of page)

function exportDashGradesCsv() {
  fetch(window.location.pathname + '/ExportGradesCsv', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ cid: 0 }),
    credentials: 'same-origin'
  })
  .then(function (r) { return r.json(); })
  .then(function (data) {
    var res = (data && data.d) ? (data.d.d || data.d) : data;
    if (!res || !res.success) { alert((res && res.message) || 'Export failed'); return; }
    var blob = new Blob([res.csv || ''], { type: 'text/csv;charset=utf-8;' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = res.fileName || 'grades.csv';
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 400);
  })
  .catch(function () { alert('Network error exporting grades.'); });
}

function loadDashboardData() {
// Fetch dashboard statistics and submissions from code-behind
fetch(window.location.pathname + '/GetDashboardData', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
}
})
.then(res => res.json())
.then(data => {
// Normalize ASP.NET PageMethod response which may be wrapped as { d: {...} }
// In some environments it can be double-wrapped: { d: { d: {...} } }
let resObj = null;
if (data && data.d) {
resObj = data.d.d ? data.d.d : data.d;
} else {
resObj = data;
}
if (!resObj || resObj.notAuthenticated) {
// Redirect to login
window.location.href = '/Pages/Authentication/Login.aspx';
return;
}
if (!resObj.success) {
console.error('Failed to load dashboard:', resObj.message || resObj);
return;
}

if (resObj.success) {
// Update Stats
document.getElementById('lblTotalStudents').innerText = formatNumber(resObj.totalStudents);
document.getElementById('lblActiveCourses').innerText = resObj.activeCourses;
document.getElementById('lblPendingGrading').innerText = resObj.pendingGrading;
if (!resObj.hasGrades) {
document.getElementById('lblAverageGrade').innerText = "N/A";
} else {
document.getElementById('lblAverageGrade').innerText = resObj.averageGrade + "%";
}

// Stats + table first; charts only when visible (lazy Chart.js CDN)
var enrollData = (resObj.enrollmentTrends && Array.isArray(resObj.enrollmentTrends))
  ? resObj.enrollmentTrends : [];
var gradeData = (resObj.gradeDistribution && Array.isArray(resObj.gradeDistribution))
  ? resObj.gradeDistribution : [];
whenChartsVisible(function () {
  ensureChartJs(function () {
    renderEnrollmentTrendWithChart(enrollData);
    renderGradeDistributionWithChart(gradeData);
  });
});

// Submissions table with search / sort / filter / pagination
renderDashSubmissions(resObj.submissions || []);
}
})
.catch(err => {
console.error("Error loading dashboard data: ", err);
});
}

function formatNumber(num) {
return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function openGradeModal(sub) {
currentSubmissionId = sub.sid;

// Set student initials and name
const avatar = document.getElementById('modalStudentAvatar');
avatar.innerText = sub.initials;
avatar.style.backgroundColor = '#f17f54';
document.getElementById('modalStudentName').innerText = sub.studentName;

// Set details
document.getElementById('modalAssignment').innerText = sub.assignmentTitle;
document.getElementById('modalAnswer').innerText = sub.studentAnswer;
document.getElementById('lblMaxScore').innerText = "/ " + sub.maxScore;

// Reset inputs
const txtScore = document.getElementById('txtScore');
txtScore.value = 0;
txtScore.max = sub.maxScore;
document.getElementById('txtReview').value = '';

// Hide error
document.getElementById('modalErrorMessage').style.display = 'none';

// Show modal
const myModal = new bootstrap.Modal(document.getElementById('gradingModal'));
myModal.show();
}

function submitGrading() {
const score = parseInt(document.getElementById('txtScore').value);
const review = document.getElementById('txtReview').value.trim();
const errDiv = document.getElementById('modalErrorMessage');

errDiv.style.display = 'none';

if (isNaN(score) || score < 0) {
errDiv.innerText = "Please enter a valid score.";
errDiv.style.display = 'block';
return;
}

// Call SaveGrade WebMethod
fetch(window.location.pathname + '/SaveGrade', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify({
sid: currentSubmissionId,
score: score,
review: review
})
})
.then(res => res.json())
.then(data => {
let resObj = null;
if (data && data.d) resObj = data.d.d ? data.d.d : data.d; else resObj = data;
if (resObj && resObj.success) {
// Close Modal
const modalEl = document.getElementById('gradingModal');
const modal = bootstrap.Modal.getInstance(modalEl);
modal.hide();

// Refresh dashboard data
loadDashboardData();
} else {
errDiv.innerText = resObj.message || "Failed to save grade.";
errDiv.style.display = 'block';
}
})
.catch(err => {
errDiv.innerText = "Network error. Please try again.";
errDiv.style.display = 'block';
console.error(err);
});
}


```
