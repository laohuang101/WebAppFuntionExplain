# dashboard.js
**Source:** `Pages/Lecturer/Scripts/dashboard.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 404
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `__chartJsLoading` | `const/let/var` | Holds “chart Js Loading” for this scope. |
| `__chartPending` | `const/let/var` | Holds “chart Pending” for this scope. |
| `s` | `const/let/var` | String value or submission-related object. |
| `targets` | `const/let/var` | Often a collection related to targets (plural name). |
| `done` | `const/let/var` | Holds “done” for this scope. |
| `io` | `const/let/var` | Holds “io” for this scope. |
| `enrollmentChart` | `const/let/var` | Holds “enrollment Chart” for this scope. |
| `gradeChart` | `const/let/var` | Holds “grade Chart” for this scope. |
| `ctxEl` | `const/let/var` | Holds “ctx El” for this scope. |
| `ctx` | `const/let/var` | Current HTTP request context (Request, Response, Session). |
| `labels` | `const/let/var` | Often a collection related to labels (plural name). |
| `values` | `const/let/var` | Often a collection related to values (plural name). |
| `defaultLabels` | `const/let/var` | Often a collection related to default Labels (plural name). |
| `currentSubmissionId` | `const/let/var` | Holds “current Submission Id” for this scope. |
| `dashSubmissionsDt` | `const/let/var` | Holds “dash Submissions Dt” for this scope. |
| `dashSubmissionsMap` | `const/let/var` | Holds “dash Submissions Map” for this scope. |
| `wrap` | `const/let/var` | Holds “wrap” for this scope. |
| `colors` | `const/let/var` | Often a collection related to colors (plural name). |
| `rows` | `const/let/var` | Collection of rows. |
| `sub` | `const/let/var` | Holds “sub” for this scope. |
| `res` | `const/let/var` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `blob` | `const/let/var` | Holds “blob” for this scope. |
| `a` | `const/let/var` | Holds “a” for this scope. |
| `resObj` | `const/let/var` | Holds “res Obj” for this scope. |
| `enrollData` | `const/let/var` | Holds “enroll Data” for this scope. |
| `gradeData` | `const/let/var` | Holds “grade Data” for this scope. |
| `avatar` | `const/let/var` | Holds “avatar” for this scope. |
| `txtScore` | `const/let/var` | UI control reference (txt Score). |
| `myModal` | `const/let/var` | Holds “my Modal” for this scope. |
| `score` | `const/let/var` | Points earned or max points depending on context. |
| `review` | `const/let/var` | Holds “review” for this scope. |
| `errDiv` | `const/let/var` | Holds “err Div” for this scope. |
| `modalEl` | `const/let/var` | Holds “modal El” for this scope. |
| `modal` | `const/let/var` | Holds “modal” for this scope. |

## Functions / methods (18 found)

### `ensureChartJs` — lines 4–18

#### Signature

```javascript
function ensureChartJs(cb)
```

#### What it is

Makes sure **Chart Js** exists or is valid before the rest of the code continues.

#### How it works

1. Starts when something calls `ensureChartJs`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cb` | `—` | Holds “cb” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |

#### Code

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

---

### `whenChartsVisible` — lines 18–40

#### Signature

```javascript
function whenChartsVisible(run)
```

#### What it is

Function `whenChartsVisible` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `whenChartsVisible`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `run` | `—` | Holds “run” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `targets` | `—` | Often a collection related to targets (plural name). |
| `done` | `—` | Holds “done” for this scope. |
| `io` | `—` | Holds “io” for this scope.  Newly constructed object. |
| `i` | `—` | Loop index (0-based counter in for-loops).  Literal number `0`. |

#### Code

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

---

### `renderEnrollmentTrendWithChart` — lines 43–112

#### Signature

```javascript
function renderEnrollmentTrendWithChart(data)
```

#### What it is

Updates the page HTML for **render Enrollment Trend With Chart**.

#### How it works

1. Starts when something calls `renderEnrollmentTrendWithChart`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `data` | `—` | Holds “data” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ctxEl` | `—` | Holds “ctx El” for this scope.  DOM element from the page. |
| `ctx` | `—` | Current HTTP request context (Request, Response, Session). |
| `labels` | `—` | Often a collection related to labels (plural name). |
| `values` | `—` | Often a collection related to values (plural name). |

#### Code

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

---

### `renderGradeDistributionWithChart` — lines 112–163

#### Signature

```javascript
function renderGradeDistributionWithChart(data)
```

#### What it is

Updates the page HTML for **render Grade Distribution With Chart**.

#### How it works

1. Starts when something calls `renderGradeDistributionWithChart`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `data` | `—` | Holds “data” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `defaultLabels` | `—` | Often a collection related to default Labels (plural name). |
| `ctx` | `—` | Current HTTP request context (Request, Response, Session).  DOM element from the page. |
| `labels` | `—` | Often a collection related to labels (plural name). |
| `values` | `—` | Often a collection related to values (plural name). |

#### Code

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

---

### `escapeHtmlDash` — lines 172–404

#### Signature

```javascript
function escapeHtmlDash(str)
```

#### What it is

Browser-side function `escapeHtmlDash` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Convert a JavaScript object into a JSON string for the server.
3. Parse the server JSON response into a JavaScript object.
4. Show a simple popup message to the user.
5. Call the server with `fetch` (AJAX) and wait for the JSON result.
6. Parse the server JSON response into a JavaScript object.
7. If the previous step failed, show the error and stop.
8. Update a page element (text, HTML, value, or enabled/disabled).
9. Call the server with `fetch` (AJAX) and wait for the JSON result.
10. Convert a JavaScript object into a JSON string for the server.
11. Parse the server JSON response into a JavaScript object.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `str` | `—` | String value: str. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `wrap` | `—` | Holds “wrap” for this scope.  DOM element from the page. |
| `colors` | `—` | Often a collection related to colors (plural name). |
| `rows` | `—` | Collection of rows. |
| `sub` | `—` | Holds “sub” for this scope. |
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `blob` | `—` | Holds “blob” for this scope.  Newly constructed object. |
| `a` | `—` | Holds “a” for this scope. |
| `resObj` | `—` | Holds “res Obj” for this scope. |
| `enrollData` | `—` | Holds “enroll Data” for this scope. |
| `gradeData` | `—` | Holds “grade Data” for this scope. |
| `avatar` | `—` | Holds “avatar” for this scope.  DOM element from the page. |
| `txtScore` | `—` | UI control reference (txt Score).  DOM element from the page. |
| `myModal` | `—` | Holds “my Modal” for this scope.  DOM element from the page. |
| `score` | `—` | Points earned or max points depending on context.  DOM element from the page. |
| `review` | `—` | Holds “review” for this scope.  DOM element from the page. |
| `errDiv` | `—` | Holds “err Div” for this scope.  DOM element from the page. |
| `modalEl` | `—` | Holds “modal El” for this scope.  DOM element from the page. |
| `modal` | `—` | Holds “modal” for this scope. |

#### Code

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

---

### `renderDashSubmissions` — lines 177–233

#### Signature

```javascript
function renderDashSubmissions(list)
```

#### What it is

Updates the page HTML for **render Dash Submissions**.

#### How it works

1. Starts when something calls `renderDashSubmissions`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `list` | `—` | In-memory collection being built for JSON return. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `wrap` | `—` | Holds “wrap” for this scope.  DOM element from the page. |
| `colors` | `—` | Often a collection related to colors (plural name). |
| `rows` | `—` | Collection of rows. |

#### Code

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

---

### `render` — lines 201–205

#### Signature

```javascript
function render(sub, i)
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
| `sub` | `—` | Holds “sub” for this scope. |
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 201 |   render: function (sub, i) {
 202 |   return '<div class="d-flex align-items-center"><div class="student-avatar me-2" style="background-color:' +
 203 |     colors[i % colors.length] + ';">' + escapeHtmlDash(sub.initials || '?') +
 204 |     '</div><span class="fw-semibold text-dark">' + escapeHtmlDash(sub.studentName) + '</span></div>';
 205 | }
```

---

### `searchValue` — lines 206–206

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
 206 | searchValue: function (s) { return (s.studentName || '') + ' ' + (s.studentEmail || ''); }
```

---

### `sortValue` — lines 211–211

#### Signature

```javascript
function sortValue(s)
```

#### What it is

Function `sortValue` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `sortValue`.
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
 211 | sortValue: function (s) { return s.timestamp || s.timeText || ''; }
```

---

### `render` — lines 214–220

#### Signature

```javascript
function render(sub)
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
| `sub` | `—` | Holds “sub” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

#### Signature

```javascript
function sortValue(s)
```

#### What it is

Function `sortValue` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `sortValue`.
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
 221 | sortValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
```

---

### `searchValue` — lines 222–222

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
 222 | searchValue: function (s) { return s.isGraded ? 'Graded' : 'Pending'; }
```

---

### `openGradeModalBySid` — lines 233–238

#### Signature

```javascript
function openGradeModalBySid(sid)
```

#### What it is

Function `openGradeModalBySid` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `openGradeModalBySid`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sid` | `—` | Submission ID (CWSubmissions.SID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sub` | `—` | Holds “sub” for this scope. |

#### Code

```javascript
 233 | 
 234 | 
 235 | function openGradeModalBySid(sid) {
 236 | var sub = dashSubmissionsMap[sid];
 237 | if (sub) openGradeModal(sub);
 238 | }
```

---

### `exportDashGradesCsv` — lines 240–262

#### Signature

```javascript
function exportDashGradesCsv()
```

#### What it is

Browser-side function `exportDashGradesCsv` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Convert a JavaScript object into a JSON string for the server.
3. Parse the server JSON response into a JavaScript object.
4. Show a simple popup message to the user.

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

---

### `loadDashboardData` — lines 262–322

#### Signature

```javascript
function loadDashboardData()
```

#### What it is

Reads/loads data related to **Dashboard Data** and returns it for display or further use.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. If the previous step failed, show the error and stop.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `resObj` | `—` | Holds “res Obj” for this scope. |
| `enrollData` | `—` | Holds “enroll Data” for this scope. |
| `gradeData` | `—` | Holds “grade Data” for this scope. |

#### Code

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

---

### `formatNumber` — lines 322–326

#### Signature

```javascript
function formatNumber(num)
```

#### What it is

Converts or cleans **format Number** into a usable form.

#### How it works

1. Starts when something calls `formatNumber`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `num` | `—` | Numeric count of items related to `num`. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 322 | 
 323 | 
 324 | function formatNumber(num) {
 325 | return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
 326 | }
```

---

### `openGradeModal` — lines 326–354

#### Signature

```javascript
function openGradeModal(sub)
```

#### What it is

Function `openGradeModal` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sub` | `—` | Holds “sub” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `avatar` | `—` | Holds “avatar” for this scope.  DOM element from the page. |
| `txtScore` | `—` | UI control reference (txt Score).  DOM element from the page. |
| `myModal` | `—` | Holds “my Modal” for this scope.  DOM element from the page. |

#### Code

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

---

### `submitGrading` — lines 354–403

#### Signature

```javascript
function submitGrading()
```

#### What it is

Browser-side function `submitGrading` — talks to the server and updates the page.

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
| `score` | `—` | Points earned or max points depending on context.  DOM element from the page. |
| `review` | `—` | Holds “review” for this scope.  DOM element from the page. |
| `errDiv` | `—` | Holds “err Div” for this scope.  DOM element from the page. |
| `resObj` | `—` | Holds “res Obj” for this scope. |
| `modalEl` | `—` | Holds “modal El” for this scope.  DOM element from the page. |
| `modal` | `—` | Holds “modal” for this scope. |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
