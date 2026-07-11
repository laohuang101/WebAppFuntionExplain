# manage-submissions.js
**Source:** `Pages/Lecturer/Scripts/manage-submissions.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 97
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `const/let/var` | CourseWork ID (assignment) (CourseWorks.CWID). |
| `res` | `const/let/var` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `sel` | `const/let/var` | Holds “sel” for this scope. |
| `opt` | `const/let/var` | Option element or optional label. |
| `container` | `const/let/var` | Holds “container” for this scope. |
| `div` | `const/let/var` | Holds “div” for this scope. |
| `s` | `const/let/var` | String value or submission-related object. |
| `body` | `const/let/var` | HTTP request body. |
| `modal` | `const/let/var` | Holds “modal” for this scope. |
| `sid` | `const/let/var` | Submission ID (CWSubmissions.SID). |
| `score` | `const/let/var` | Points earned or max points depending on context. |
| `review` | `const/let/var` | Holds “review” for this scope. |

## Functions / methods (7 found)

### `initManageSubmissions` — lines 3–16

#### Signature

```javascript
function initManageSubmissions()
```

#### What it is

Function `initManageSubmissions` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Attach a browser event handler (click, load, change, …).
2. Update a page element (text, HTML, value, or enabled/disabled).
3. Show a simple popup message to the user.
4. Attach a browser event handler (click, load, change, …).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `—` | CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page. |

#### Code

```javascript
   3 | 
   4 | 
   5 | function initManageSubmissions() {
   6 |     loadAssignments();
   7 |     document.getElementById('btnLoadSubs').addEventListener('click', function () {
   8 |         const cwid = parseInt(document.getElementById('ddlAssignments').value);
   9 |         if (!cwid) return alert('Select an assignment');
  10 |         loadSubmissions(cwid);
  11 |     });
  12 | 
  13 |     document.getElementById('btnSubmitGrade').addEventListener('click', function () {
  14 |         submitGrade();
  15 |     });
  16 | }
```

---

### `loadAssignments` — lines 16–30

#### Signature

```javascript
function loadAssignments()
```

#### What it is

Reads/loads data related to **Assignments** and returns it for display or further use.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `sel` | `—` | Holds “sel” for this scope.  DOM element from the page. |
| `opt` | `—` | Option element or optional label. |

#### Code

```javascript
  16 | 
  17 | 
  18 | function loadAssignments() {
  19 |     fetch('ManageSubmissions.aspx/GetAssignments', { method: 'POST', headers: { 'Content-Type': 'application/json' } })
  20 |     .then(r => r.json()).then(d => {
  21 |         const res = d.d || d;
  22 |         const sel = document.getElementById('ddlAssignments');
  23 |         sel.innerHTML = '';
  24 |         if (res && res.success && Array.isArray(res.assignments)) {
  25 |             res.assignments.forEach(a => {
  26 |                 const opt = document.createElement('option'); opt.value = a.cwid; opt.textContent = `${a.title} - ${a.course}`; sel.appendChild(opt);
  27 |             });
  28 |         }
  29 |     }).catch(err => console.error(err));
  30 | }
```

---

### `loadSubmissions` — lines 30–50

#### Signature

```javascript
function loadSubmissions(cwid)
```

#### What it is

Reads/loads data related to **Submissions** and returns it for display or further use.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. If the previous step failed, show the error and stop.
4. Attach a browser event handler (click, load, change, …).
5. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `—` | CourseWork ID (assignment) (CourseWorks.CWID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `container` | `—` | Holds “container” for this scope.  DOM element from the page. |
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `div` | `—` | Holds “div” for this scope. |
| `sid` | `—` | Submission ID (CWSubmissions.SID). |
| `sc` | `—` | Holds “sc” for this scope. |

#### Code

```javascript
  30 | 
  31 | 
  32 | function loadSubmissions(cwid) {
  33 |     const container = document.getElementById('submissionsList');
  34 |     container.innerHTML = `<div class="text-center py-3 text-muted"><i class="fa-solid fa-circle-notch fa-spin"></i> Loading...</div>`;
  35 |     fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })
  36 |     .then(r => r.json()).then(d => {
  37 |         const res = d.d || d;
  38 |         if (!res.success) { container.innerHTML = `<div class="text-danger">${res.message || 'Failed'}</div>`; return; }
  39 |         if (!res.submissions || res.submissions.length === 0) { container.innerHTML = `<div class="text-muted">No submissions yet.</div>`; return; }
  40 |         container.innerHTML = '';
  41 |         res.submissions.forEach(s => {
  42 |             const div = document.createElement('div'); div.className = 'd-flex justify-content-between align-items-center py-2 border-bottom';
  43 |             div.innerHTML = `<div><div class="fw-semibold">${escapeHtml(s.studentName)}</div><div class="small text-muted">${escapeHtml(s.time)}</div></div><div><button class="btn btn-sm btn-light me-2" data-view="${s.sid}">View</button><button class="btn btn-sm btn-pill-accent" data-grade="${s.sid}" data-score="${s.score}">Grade</button></div>`;
  44 |             container.appendChild(div);
  45 |         });
  46 | 
  47 |         container.querySelectorAll('[data-view]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-view')); viewSubmission(sid); }));
  48 |         container.querySelectorAll('[data-grade]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-grade')); const sc = parseInt(this.getAttribute('data-score')); openGradeModal(sid, sc); }));
  49 |     }).catch(err => { console.error(err); document.getElementById('submissionsList').innerHTML = `<div class="text-danger">Network error</div>`; });
  50 | }
```

---

### `viewSubmission` — lines 50–69

#### Signature

```javascript
function viewSubmission(sid)
```

#### What it is

Browser-side function `viewSubmission` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. Show a simple popup message to the user.
4. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sid` | `—` | Submission ID (CWSubmissions.SID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `s` | `—` | String value or submission-related object. |
| `body` | `—` | HTTP request body.  DOM element from the page. |
| `modal` | `—` | Holds “modal” for this scope.  DOM element from the page. |

#### Code

```javascript
  50 | 
  51 | 
  52 | function viewSubmission(sid) {
  53 |     // reuse GetSubmissions to fetch single submission details
  54 |     fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: parseInt(document.getElementById('ddlAssignments').value) }) })
  55 |     .then(r => r.json()).then(d => {
  56 |         const res = d.d || d;
  57 |         if (!res.success) return alert('Failed to load');
  58 |         const s = res.submissions.find(x => x.sid === sid);
  59 |         if (!s) return alert('Not found');
  60 |         const body = document.getElementById('gradeSubmissionBody');
  61 |         body.innerHTML = `<div class="mb-2"><strong>${escapeHtml(s.studentName)}</strong> - <span class="small text-muted">${escapeHtml(s.time)}</span></div><div class="border p-3 bg-white" style="min-height:150px">${escapeHtml(s.text)}</div>`;
  62 |         document.getElementById('txtGradeScore').value = s.score >= 0 ? s.score : 0;
  63 |         document.getElementById('txtGradeFeedback').value = s.review || '';
  64 |         const modal = new bootstrap.Modal(document.getElementById('gradeModal'));
  65 |         modal.show();
  66 |         // store sid on submit button
  67 |         document.getElementById('btnSubmitGrade').setAttribute('data-sid', sid);
  68 |     }).catch(err => console.error(err));
  69 | }
```

---

### `openGradeModal` — lines 69–74

#### Signature

```javascript
function openGradeModal(sid, score)
```

#### What it is

Function `openGradeModal` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `openGradeModal`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sid` | `—` | Submission ID (CWSubmissions.SID). |
| `score` | `—` | Points earned or max points depending on context. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
  69 | 
  70 | 
  71 | function openGradeModal(sid, score) {
  72 |     // fetch single submission to show
  73 |     viewSubmission(sid);
  74 | }
```

---

### `submitGrade` — lines 74–95

#### Signature

```javascript
function submitGrade()
```

#### What it is

Browser-side function `submitGrade` — talks to the server and updates the page.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).
2. Call the server with `fetch` (AJAX) and wait for the JSON result.
3. Parse the server JSON response into a JavaScript object.
4. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sid` | `—` | Submission ID (CWSubmissions.SID).  DOM element from the page. |
| `score` | `—` | Points earned or max points depending on context.  DOM element from the page. |
| `review` | `—` | Holds “review” for this scope.  DOM element from the page. |
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `modal` | `—` | Holds “modal” for this scope.  DOM element from the page. |
| `cwid` | `—` | CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page. |

#### Code

```javascript
  74 | 
  75 | 
  76 | function submitGrade() {
  77 |     const sid = parseInt(document.getElementById('btnSubmitGrade').getAttribute('data-sid'));
  78 |     const score = parseInt(document.getElementById('txtGradeScore').value) || 0;
  79 |     const review = document.getElementById('txtGradeFeedback').value || '';
  80 |     document.getElementById('gradeError').style.display = 'none';
  81 |     fetch('ManageSubmissions.aspx/GradeSubmission', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ sid: sid, score: score, review: review }) })
  82 |     .then(r => r.json()).then(d => {
  83 |         const res = d.d || d;
  84 |         if (res.success) {
  85 |             const modal = bootstrap.Modal.getInstance(document.getElementById('gradeModal'));
  86 |             if (modal) modal.hide();
  87 |             // reload submissions
  88 |             const cwid = parseInt(document.getElementById('ddlAssignments').value);
  89 |             if (cwid) loadSubmissions(cwid);
  90 |         } else {
  91 |             document.getElementById('gradeError').innerText = res.message || 'Failed to save grade';
  92 |             document.getElementById('gradeError').style.display = 'block';
  93 |         }
  94 |     }).catch(err => { console.error(err); document.getElementById('gradeError').innerText = 'Network error'; document.getElementById('gradeError').style.display = 'block'; });
  95 | }
```

---

### `escapeHtml` — lines 95–97

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
  95 | 
  96 | 
  97 | function escapeHtml(str) { if (!str) return ''; return String(str).replace(/[&<>\"]/g, function (m) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[m]; }); }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | document.addEventListener('DOMContentLoaded', function () {
   2 |     initManageSubmissions();
   3 | });
   4 | 
   5 | function initManageSubmissions() {
   6 |     loadAssignments();
   7 |     document.getElementById('btnLoadSubs').addEventListener('click', function () {
   8 |         const cwid = parseInt(document.getElementById('ddlAssignments').value);
   9 |         if (!cwid) return alert('Select an assignment');
  10 |         loadSubmissions(cwid);
  11 |     });
  12 | 
  13 |     document.getElementById('btnSubmitGrade').addEventListener('click', function () {
  14 |         submitGrade();
  15 |     });
  16 | }
  17 | 
  18 | function loadAssignments() {
  19 |     fetch('ManageSubmissions.aspx/GetAssignments', { method: 'POST', headers: { 'Content-Type': 'application/json' } })
  20 |     .then(r => r.json()).then(d => {
  21 |         const res = d.d || d;
  22 |         const sel = document.getElementById('ddlAssignments');
  23 |         sel.innerHTML = '';
  24 |         if (res && res.success && Array.isArray(res.assignments)) {
  25 |             res.assignments.forEach(a => {
  26 |                 const opt = document.createElement('option'); opt.value = a.cwid; opt.textContent = `${a.title} - ${a.course}`; sel.appendChild(opt);
  27 |             });
  28 |         }
  29 |     }).catch(err => console.error(err));
  30 | }
  31 | 
  32 | function loadSubmissions(cwid) {
  33 |     const container = document.getElementById('submissionsList');
  34 |     container.innerHTML = `<div class="text-center py-3 text-muted"><i class="fa-solid fa-circle-notch fa-spin"></i> Loading...</div>`;
  35 |     fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })
  36 |     .then(r => r.json()).then(d => {
  37 |         const res = d.d || d;
  38 |         if (!res.success) { container.innerHTML = `<div class="text-danger">${res.message || 'Failed'}</div>`; return; }
  39 |         if (!res.submissions || res.submissions.length === 0) { container.innerHTML = `<div class="text-muted">No submissions yet.</div>`; return; }
  40 |         container.innerHTML = '';
  41 |         res.submissions.forEach(s => {
  42 |             const div = document.createElement('div'); div.className = 'd-flex justify-content-between align-items-center py-2 border-bottom';
  43 |             div.innerHTML = `<div><div class="fw-semibold">${escapeHtml(s.studentName)}</div><div class="small text-muted">${escapeHtml(s.time)}</div></div><div><button class="btn btn-sm btn-light me-2" data-view="${s.sid}">View</button><button class="btn btn-sm btn-pill-accent" data-grade="${s.sid}" data-score="${s.score}">Grade</button></div>`;
  44 |             container.appendChild(div);
  45 |         });
  46 | 
  47 |         container.querySelectorAll('[data-view]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-view')); viewSubmission(sid); }));
  48 |         container.querySelectorAll('[data-grade]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-grade')); const sc = parseInt(this.getAttribute('data-score')); openGradeModal(sid, sc); }));
  49 |     }).catch(err => { console.error(err); document.getElementById('submissionsList').innerHTML = `<div class="text-danger">Network error</div>`; });
  50 | }
  51 | 
  52 | function viewSubmission(sid) {
  53 |     // reuse GetSubmissions to fetch single submission details
  54 |     fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: parseInt(document.getElementById('ddlAssignments').value) }) })
  55 |     .then(r => r.json()).then(d => {
  56 |         const res = d.d || d;
  57 |         if (!res.success) return alert('Failed to load');
  58 |         const s = res.submissions.find(x => x.sid === sid);
  59 |         if (!s) return alert('Not found');
  60 |         const body = document.getElementById('gradeSubmissionBody');
  61 |         body.innerHTML = `<div class="mb-2"><strong>${escapeHtml(s.studentName)}</strong> - <span class="small text-muted">${escapeHtml(s.time)}</span></div><div class="border p-3 bg-white" style="min-height:150px">${escapeHtml(s.text)}</div>`;
  62 |         document.getElementById('txtGradeScore').value = s.score >= 0 ? s.score : 0;
  63 |         document.getElementById('txtGradeFeedback').value = s.review || '';
  64 |         const modal = new bootstrap.Modal(document.getElementById('gradeModal'));
  65 |         modal.show();
  66 |         // store sid on submit button
  67 |         document.getElementById('btnSubmitGrade').setAttribute('data-sid', sid);
  68 |     }).catch(err => console.error(err));
  69 | }
  70 | 
  71 | function openGradeModal(sid, score) {
  72 |     // fetch single submission to show
  73 |     viewSubmission(sid);
  74 | }
  75 | 
  76 | function submitGrade() {
  77 |     const sid = parseInt(document.getElementById('btnSubmitGrade').getAttribute('data-sid'));
  78 |     const score = parseInt(document.getElementById('txtGradeScore').value) || 0;
  79 |     const review = document.getElementById('txtGradeFeedback').value || '';
  80 |     document.getElementById('gradeError').style.display = 'none';
  81 |     fetch('ManageSubmissions.aspx/GradeSubmission', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ sid: sid, score: score, review: review }) })
  82 |     .then(r => r.json()).then(d => {
  83 |         const res = d.d || d;
  84 |         if (res.success) {
  85 |             const modal = bootstrap.Modal.getInstance(document.getElementById('gradeModal'));
  86 |             if (modal) modal.hide();
  87 |             // reload submissions
  88 |             const cwid = parseInt(document.getElementById('ddlAssignments').value);
  89 |             if (cwid) loadSubmissions(cwid);
  90 |         } else {
  91 |             document.getElementById('gradeError').innerText = res.message || 'Failed to save grade';
  92 |             document.getElementById('gradeError').style.display = 'block';
  93 |         }
  94 |     }).catch(err => { console.error(err); document.getElementById('gradeError').innerText = 'Network error'; document.getElementById('gradeError').style.display = 'block'; });
  95 | }
  96 | 
  97 | function escapeHtml(str) { if (!str) return ''; return String(str).replace(/[&<>\"]/g, function (m) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[m]; }); }
```
