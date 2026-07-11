# manage-submissions.js
**Source:** `Pages/Lecturer/Scripts/manage-submissions.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 97
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 8:** `cwid` — script-level `const`/`let`/`var` — **CourseWork ID (assignment) (CourseWorks.CWID).**
- **Line 21:** `res` — script-level `const`/`let`/`var` — **Result object returned from fetch/WebMethod (`data.d` unwrapped).**
- **Line 22:** `sel` — script-level `const`/`let`/`var` — **Holds “sel” for this scope.**
- **Line 26:** `opt` — script-level `const`/`let`/`var` — **Option element or optional label.**
- **Line 33:** `container` — script-level `const`/`let`/`var` — **Holds “container” for this scope.**
- **Line 42:** `div` — script-level `const`/`let`/`var` — **Holds “div” for this scope.**
- **Line 58:** `s` — script-level `const`/`let`/`var` — **String value or submission-related object.**
- **Line 60:** `body` — script-level `const`/`let`/`var` — **HTTP request body.**
- **Line 64:** `modal` — script-level `const`/`let`/`var` — **Holds “modal” for this scope.**
- **Line 77:** `sid` — script-level `const`/`let`/`var` — **Submission ID (CWSubmissions.SID).**
- **Line 78:** `score` — script-level `const`/`let`/`var` — **Points earned or max points depending on context.**
- **Line 79:** `review` — script-level `const`/`let`/`var` — **Holds “review” for this scope.**

## Functions / methods (7 found)

### `initManageSubmissions` — lines 3–16

```javascript
function initManageSubmissions()
```

#### Explanation

- **Purpose:** Implements `initManageSubmissions`.
- **Local variables (what each means):**
- `cwid` — CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L7:** DOM event handler.
- **L8:** Get HTML element by id. | `cwid` means: CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page.
- **L13:** DOM event handler.

---

### `loadAssignments` — lines 16–30

```javascript
function loadAssignments()
```

#### Explanation

- **Purpose:** Implements `loadAssignments`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `sel` — Holds “sel” for this scope.  DOM element from the page.
- `opt` — Option element or optional label.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L19:** HTTP request to server WebMethod/ashx.
- **L21:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L22:** Get HTML element by id. | `sel` means: Holds “sel” for this scope.  DOM element from the page.
- **L23:** Update page HTML.
- **L26:** `opt` means: Option element or optional label.

---

### `loadSubmissions` — lines 30–50

```javascript
function loadSubmissions(cwid)
```

#### Explanation

- **Purpose:** Implements `loadSubmissions`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Parameters (what each means):**
- `cwid` — CourseWork ID (assignment) (CourseWorks.CWID).
- **Local variables (what each means):**
- `container` — Holds “container” for this scope.  DOM element from the page.
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `div` — Holds “div” for this scope.
- `sid` — Submission ID (CWSubmissions.SID).
- `sc` — Holds “sc” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L33:** Get HTML element by id. | `container` means: Holds “container” for this scope.  DOM element from the page.
- **L34:** Update page HTML.
- **L35:** HTTP request to server WebMethod/ashx.
- **L37:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L38:** Update page HTML.
- **L39:** Update page HTML.
- **L40:** Update page HTML.
- **L42:** `div` means: Holds “div” for this scope.
- **L43:** Update page HTML.
- **L47:** DOM event handler.
- **L48:** DOM event handler.
- **L49:** Get HTML element by id.

---

### `viewSubmission` — lines 50–69

```javascript
function viewSubmission(sid)
```

#### Explanation

- **Purpose:** Implements `viewSubmission`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters (what each means):**
- `sid` — Submission ID (CWSubmissions.SID).
- **Local variables (what each means):**
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `s` — String value or submission-related object.
- `body` — HTTP request body.  DOM element from the page.
- `modal` — Holds “modal” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L54:** HTTP request to server WebMethod/ashx.
- **L56:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L58:** `s` means: String value or submission-related object.
- **L60:** Get HTML element by id. | `body` means: HTTP request body.  DOM element from the page.
- **L61:** Update page HTML.
- **L62:** Get HTML element by id.
- **L63:** Get HTML element by id.
- **L64:** Get HTML element by id. | `modal` means: Holds “modal” for this scope.  DOM element from the page.
- **L67:** Get HTML element by id.

---

### `openGradeModal` — lines 69–74

```javascript
function openGradeModal(sid, score)
```

#### Explanation

- **Purpose:** Implements `openGradeModal`.
- **Parameters (what each means):**
- `sid` — Submission ID (CWSubmissions.SID).
- `score` — Points earned or max points depending on context.

#### Line-by-line (this function)

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

```javascript
function submitGrade()
```

#### Explanation

- **Purpose:** Implements `submitGrade`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables (what each means):**
- `sid` — Submission ID (CWSubmissions.SID).  DOM element from the page.
- `score` — Points earned or max points depending on context.  DOM element from the page.
- `review` — Holds “review” for this scope.  DOM element from the page.
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `modal` — Holds “modal” for this scope.  DOM element from the page.
- `cwid` — CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L77:** Get HTML element by id. | `sid` means: Submission ID (CWSubmissions.SID).  DOM element from the page.
- **L78:** Get HTML element by id. | `score` means: Points earned or max points depending on context.  DOM element from the page.
- **L79:** Get HTML element by id. | `review` means: Holds “review” for this scope.  DOM element from the page.
- **L80:** Get HTML element by id.
- **L81:** HTTP request to server WebMethod/ashx.
- **L83:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L85:** Get HTML element by id. | `modal` means: Holds “modal” for this scope.  DOM element from the page.
- **L88:** Get HTML element by id. | `cwid` means: CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page.
- **L91:** Get HTML element by id.
- **L92:** Get HTML element by id.
- **L94:** Get HTML element by id.

---

### `escapeHtml` — lines 95–97

```javascript
function escapeHtml(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtml`.
- **Parameters (what each means):**
- `str` — String value: str.

#### Line-by-line (this function)

```javascript
  95 | 
  96 | 
  97 | function escapeHtml(str) { if (!str) return ''; return String(str).replace(/[&<>\"]/g, function (m) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[m]; }); }
```

**Line notes** (what code + variables mean)

- **L97:** Encode text to reduce XSS risk.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L1:** DOM event handler.
- **L7:** DOM event handler.
- **L8:** Get HTML element by id. | `cwid` means: CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page.
- **L13:** DOM event handler.
- **L19:** HTTP request to server WebMethod/ashx.
- **L21:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L22:** Get HTML element by id. | `sel` means: Holds “sel” for this scope.  DOM element from the page.
- **L23:** Update page HTML.
- **L26:** `opt` means: Option element or optional label.
- **L33:** Get HTML element by id. | `container` means: Holds “container” for this scope.  DOM element from the page.
- **L34:** Update page HTML.
- **L35:** HTTP request to server WebMethod/ashx.
- **L37:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L38:** Update page HTML.
- **L39:** Update page HTML.
- **L40:** Update page HTML.
- **L42:** `div` means: Holds “div” for this scope.
- **L43:** Update page HTML.
- **L47:** DOM event handler.
- **L48:** DOM event handler.
- **L49:** Get HTML element by id.
- **L54:** HTTP request to server WebMethod/ashx.
- **L56:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L58:** `s` means: String value or submission-related object.
- **L60:** Get HTML element by id. | `body` means: HTTP request body.  DOM element from the page.
- **L61:** Update page HTML.
- **L62:** Get HTML element by id.
- **L63:** Get HTML element by id.
- **L64:** Get HTML element by id. | `modal` means: Holds “modal” for this scope.  DOM element from the page.
- **L67:** Get HTML element by id.
- **L77:** Get HTML element by id. | `sid` means: Submission ID (CWSubmissions.SID).  DOM element from the page.
- **L78:** Get HTML element by id. | `score` means: Points earned or max points depending on context.  DOM element from the page.
- **L79:** Get HTML element by id. | `review` means: Holds “review” for this scope.  DOM element from the page.
- **L80:** Get HTML element by id.
- **L81:** HTTP request to server WebMethod/ashx.
- **L83:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L85:** Get HTML element by id. | `modal` means: Holds “modal” for this scope.  DOM element from the page.
- **L88:** Get HTML element by id. | `cwid` means: CourseWork ID (assignment) (CourseWorks.CWID).  DOM element from the page.
- **L91:** Get HTML element by id.
- **L92:** Get HTML element by id.
- **L94:** Get HTML element by id.
- **L97:** Encode text to reduce XSS risk.

## Source snapshot (raw)

```javascript
document.addEventListener('DOMContentLoaded', function () {
    initManageSubmissions();
});

function initManageSubmissions() {
    loadAssignments();
    document.getElementById('btnLoadSubs').addEventListener('click', function () {
        const cwid = parseInt(document.getElementById('ddlAssignments').value);
        if (!cwid) return alert('Select an assignment');
        loadSubmissions(cwid);
    });

    document.getElementById('btnSubmitGrade').addEventListener('click', function () {
        submitGrade();
    });
}

function loadAssignments() {
    fetch('ManageSubmissions.aspx/GetAssignments', { method: 'POST', headers: { 'Content-Type': 'application/json' } })
    .then(r => r.json()).then(d => {
        const res = d.d || d;
        const sel = document.getElementById('ddlAssignments');
        sel.innerHTML = '';
        if (res && res.success && Array.isArray(res.assignments)) {
            res.assignments.forEach(a => {
                const opt = document.createElement('option'); opt.value = a.cwid; opt.textContent = `${a.title} - ${a.course}`; sel.appendChild(opt);
            });
        }
    }).catch(err => console.error(err));
}

function loadSubmissions(cwid) {
    const container = document.getElementById('submissionsList');
    container.innerHTML = `<div class="text-center py-3 text-muted"><i class="fa-solid fa-circle-notch fa-spin"></i> Loading...</div>`;
    fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })
    .then(r => r.json()).then(d => {
        const res = d.d || d;
        if (!res.success) { container.innerHTML = `<div class="text-danger">${res.message || 'Failed'}</div>`; return; }
        if (!res.submissions || res.submissions.length === 0) { container.innerHTML = `<div class="text-muted">No submissions yet.</div>`; return; }
        container.innerHTML = '';
        res.submissions.forEach(s => {
            const div = document.createElement('div'); div.className = 'd-flex justify-content-between align-items-center py-2 border-bottom';
            div.innerHTML = `<div><div class="fw-semibold">${escapeHtml(s.studentName)}</div><div class="small text-muted">${escapeHtml(s.time)}</div></div><div><button class="btn btn-sm btn-light me-2" data-view="${s.sid}">View</button><button class="btn btn-sm btn-pill-accent" data-grade="${s.sid}" data-score="${s.score}">Grade</button></div>`;
            container.appendChild(div);
        });

        container.querySelectorAll('[data-view]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-view')); viewSubmission(sid); }));
        container.querySelectorAll('[data-grade]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-grade')); const sc = parseInt(this.getAttribute('data-score')); openGradeModal(sid, sc); }));
    }).catch(err => { console.error(err); document.getElementById('submissionsList').innerHTML = `<div class="text-danger">Network error</div>`; });
}

function viewSubmission(sid) {
    // reuse GetSubmissions to fetch single submission details
    fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: parseInt(document.getElementById('ddlAssignments').value) }) })
    .then(r => r.json()).then(d => {
        const res = d.d || d;
        if (!res.success) return alert('Failed to load');
        const s = res.submissions.find(x => x.sid === sid);
        if (!s) return alert('Not found');
        const body = document.getElementById('gradeSubmissionBody');
        body.innerHTML = `<div class="mb-2"><strong>${escapeHtml(s.studentName)}</strong> - <span class="small text-muted">${escapeHtml(s.time)}</span></div><div class="border p-3 bg-white" style="min-height:150px">${escapeHtml(s.text)}</div>`;
        document.getElementById('txtGradeScore').value = s.score >= 0 ? s.score : 0;
        document.getElementById('txtGradeFeedback').value = s.review || '';
        const modal = new bootstrap.Modal(document.getElementById('gradeModal'));
        modal.show();
        // store sid on submit button
        document.getElementById('btnSubmitGrade').setAttribute('data-sid', sid);
    }).catch(err => console.error(err));
}

function openGradeModal(sid, score) {
    // fetch single submission to show
    viewSubmission(sid);
}

function submitGrade() {
    const sid = parseInt(document.getElementById('btnSubmitGrade').getAttribute('data-sid'));
    const score = parseInt(document.getElementById('txtGradeScore').value) || 0;
    const review = document.getElementById('txtGradeFeedback').value || '';
    document.getElementById('gradeError').style.display = 'none';
    fetch('ManageSubmissions.aspx/GradeSubmission', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ sid: sid, score: score, review: review }) })
    .then(r => r.json()).then(d => {
        const res = d.d || d;
        if (res.success) {
            const modal = bootstrap.Modal.getInstance(document.getElementById('gradeModal'));
            if (modal) modal.hide();
            // reload submissions
            const cwid = parseInt(document.getElementById('ddlAssignments').value);
            if (cwid) loadSubmissions(cwid);
        } else {
            document.getElementById('gradeError').innerText = res.message || 'Failed to save grade';
            document.getElementById('gradeError').style.display = 'block';
        }
    }).catch(err => { console.error(err); document.getElementById('gradeError').innerText = 'Network error'; document.getElementById('gradeError').style.display = 'block'; });
}

function escapeHtml(str) { if (!str) return ''; return String(str).replace(/[&<>\"]/g, function (m) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[m]; }); }

```
