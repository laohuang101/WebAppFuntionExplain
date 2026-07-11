# manage-submissions.js
**Source:** `Pages/Lecturer/Scripts/manage-submissions.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 97
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 8:** `cwid` — script-level `const`/`let`/`var`
- **Line 21:** `res` — script-level `const`/`let`/`var`
- **Line 22:** `sel` — script-level `const`/`let`/`var`
- **Line 26:** `opt` — script-level `const`/`let`/`var`
- **Line 33:** `container` — script-level `const`/`let`/`var`
- **Line 42:** `div` — script-level `const`/`let`/`var`
- **Line 58:** `s` — script-level `const`/`let`/`var`
- **Line 60:** `body` — script-level `const`/`let`/`var`
- **Line 64:** `modal` — script-level `const`/`let`/`var`
- **Line 77:** `sid` — script-level `const`/`let`/`var`
- **Line 78:** `score` — script-level `const`/`let`/`var`
- **Line 79:** `review` — script-level `const`/`let`/`var`

## Functions / methods (7 found)

### `initManageSubmissions` — lines 3–16

```
function initManageSubmissions()
```

#### Explanation

- **Purpose:** Implements `initManageSubmissions`.
- **Local variables:** `cwid`

#### Line-by-line (this function)

`   3`  ``
`   4`  ``
`   5`  `function initManageSubmissions() {`
`   6`  `    loadAssignments();`
`   7`  `    document.getElementById('btnLoadSubs').addEventListener('click', function () {`
  - → DOM event handler.
`   8`  `        const cwid = parseInt(document.getElementById('ddlAssignments').value);`
  - → Get HTML element by id.
`   9`  `        if (!cwid) return alert('Select an assignment');`
`  10`  `        loadSubmissions(cwid);`
`  11`  `    });`
`  12`  ``
`  13`  `    document.getElementById('btnSubmitGrade').addEventListener('click', function () {`
  - → DOM event handler.
`  14`  `        submitGrade();`
`  15`  `    });`
`  16`  `}`

---

### `loadAssignments` — lines 16–30

```
function loadAssignments()
```

#### Explanation

- **Purpose:** Implements `loadAssignments`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables:** `res`, `sel`, `opt`

#### Line-by-line (this function)

`  16`  ``
`  17`  ``
`  18`  `function loadAssignments() {`
`  19`  `    fetch('ManageSubmissions.aspx/GetAssignments', { method: 'POST', headers: { 'Content-Type': 'application/json' } })`
  - → HTTP request to server WebMethod/ashx.
`  20`  `    .then(r => r.json()).then(d => {`
`  21`  `        const res = d.d || d;`
`  22`  `        const sel = document.getElementById('ddlAssignments');`
  - → Get HTML element by id.
`  23`  `        sel.innerHTML = '';`
  - → Update page HTML.
`  24`  `        if (res && res.success && Array.isArray(res.assignments)) {`
`  25`  `            res.assignments.forEach(a => {`
`  26`  `                const opt = document.createElement('option'); opt.value = a.cwid; opt.textContent = `${a.title} - ${a.course}`; sel.appendChild(opt);`
`  27`  `            });`
`  28`  `        }`
`  29`  `    }).catch(err => console.error(err));`
`  30`  `}`

---

### `loadSubmissions` — lines 30–50

```
function loadSubmissions(cwid)
```

#### Explanation

- **Purpose:** Implements `loadSubmissions`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Parameters:** `cwid`
- **Local variables:** `container`, `res`, `div`, `sid`, `sc`

#### Line-by-line (this function)

`  30`  ``
`  31`  ``
`  32`  `function loadSubmissions(cwid) {`
`  33`  `    const container = document.getElementById('submissionsList');`
  - → Get HTML element by id.
`  34`  `    container.innerHTML = `<div class="text-center py-3 text-muted"><i class="fa-solid fa-circle-notch fa-spin"></i> Loading...</div>`;`
  - → Update page HTML.
`  35`  `    fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })`
  - → HTTP request to server WebMethod/ashx.
`  36`  `    .then(r => r.json()).then(d => {`
`  37`  `        const res = d.d || d;`
`  38`  `        if (!res.success) { container.innerHTML = `<div class="text-danger">${res.message || 'Failed'}</div>`; return; }`
  - → Update page HTML.
`  39`  `        if (!res.submissions || res.submissions.length === 0) { container.innerHTML = `<div class="text-muted">No submissions yet.</div>`; return; }`
  - → Update page HTML.
`  40`  `        container.innerHTML = '';`
  - → Update page HTML.
`  41`  `        res.submissions.forEach(s => {`
`  42`  `            const div = document.createElement('div'); div.className = 'd-flex justify-content-between align-items-center py-2 border-bottom';`
`  43`  `            div.innerHTML = `<div><div class="fw-semibold">${escapeHtml(s.studentName)}</div><div class="small text-muted">${escapeHtml(s.time)}</div></div><div><button class="btn btn-sm btn-light me-2" data-view="${s.sid}">View</button><button class="btn btn-sm btn-pill-accent" data-grade="${s.sid}" data-score="${s.score}">Grade</button></div>`;`
  - → Update page HTML.
`  44`  `            container.appendChild(div);`
`  45`  `        });`
`  46`  ``
`  47`  `        container.querySelectorAll('[data-view]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-view')); viewSubmission(sid); }));`
  - → DOM event handler.
`  48`  `        container.querySelectorAll('[data-grade]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-grade')); const sc = parseInt(this.getAttribute('data-score')); openGradeModal(sid, sc); }));`
  - → DOM event handler.
`  49`  `    }).catch(err => { console.error(err); document.getElementById('submissionsList').innerHTML = `<div class="text-danger">Network error</div>`; });`
  - → Get HTML element by id.
`  50`  `}`

---

### `viewSubmission` — lines 50–69

```
function viewSubmission(sid)
```

#### Explanation

- **Purpose:** Implements `viewSubmission`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters:** `sid`
- **Local variables:** `res`, `s`, `body`, `modal`

#### Line-by-line (this function)

`  50`  ``
`  51`  ``
`  52`  `function viewSubmission(sid) {`
`  53`  `    // reuse GetSubmissions to fetch single submission details`
`  54`  `    fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: parseInt(document.getElementById('ddlAssignments').value) }) })`
  - → HTTP request to server WebMethod/ashx.
`  55`  `    .then(r => r.json()).then(d => {`
`  56`  `        const res = d.d || d;`
`  57`  `        if (!res.success) return alert('Failed to load');`
`  58`  `        const s = res.submissions.find(x => x.sid === sid);`
`  59`  `        if (!s) return alert('Not found');`
`  60`  `        const body = document.getElementById('gradeSubmissionBody');`
  - → Get HTML element by id.
`  61`  `        body.innerHTML = `<div class="mb-2"><strong>${escapeHtml(s.studentName)}</strong> - <span class="small text-muted">${escapeHtml(s.time)}</span></div><div class="border p-3 bg-white" style="min-height:150px">${escapeHtml(s.text)}</div>`;`
  - → Update page HTML.
`  62`  `        document.getElementById('txtGradeScore').value = s.score >= 0 ? s.score : 0;`
  - → Get HTML element by id.
`  63`  `        document.getElementById('txtGradeFeedback').value = s.review || '';`
  - → Get HTML element by id.
`  64`  `        const modal = new bootstrap.Modal(document.getElementById('gradeModal'));`
  - → Get HTML element by id.
`  65`  `        modal.show();`
`  66`  `        // store sid on submit button`
`  67`  `        document.getElementById('btnSubmitGrade').setAttribute('data-sid', sid);`
  - → Get HTML element by id.
`  68`  `    }).catch(err => console.error(err));`
`  69`  `}`

---

### `openGradeModal` — lines 69–74

```
function openGradeModal(sid, score)
```

#### Explanation

- **Purpose:** Implements `openGradeModal`.
- **Parameters:** `sid, score`

#### Line-by-line (this function)

`  69`  ``
`  70`  ``
`  71`  `function openGradeModal(sid, score) {`
`  72`  `    // fetch single submission to show`
`  73`  `    viewSubmission(sid);`
`  74`  `}`

---

### `submitGrade` — lines 74–95

```
function submitGrade()
```

#### Explanation

- **Purpose:** Implements `submitGrade`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables:** `sid`, `score`, `review`, `res`, `modal`, `cwid`

#### Line-by-line (this function)

`  74`  ``
`  75`  ``
`  76`  `function submitGrade() {`
`  77`  `    const sid = parseInt(document.getElementById('btnSubmitGrade').getAttribute('data-sid'));`
  - → Get HTML element by id.
`  78`  `    const score = parseInt(document.getElementById('txtGradeScore').value) || 0;`
  - → Get HTML element by id.
`  79`  `    const review = document.getElementById('txtGradeFeedback').value || '';`
  - → Get HTML element by id.
`  80`  `    document.getElementById('gradeError').style.display = 'none';`
  - → Get HTML element by id.
`  81`  `    fetch('ManageSubmissions.aspx/GradeSubmission', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ sid: sid, score: score, review: review }) })`
  - → HTTP request to server WebMethod/ashx.
`  82`  `    .then(r => r.json()).then(d => {`
`  83`  `        const res = d.d || d;`
`  84`  `        if (res.success) {`
`  85`  `            const modal = bootstrap.Modal.getInstance(document.getElementById('gradeModal'));`
  - → Get HTML element by id.
`  86`  `            if (modal) modal.hide();`
`  87`  `            // reload submissions`
`  88`  `            const cwid = parseInt(document.getElementById('ddlAssignments').value);`
  - → Get HTML element by id.
`  89`  `            if (cwid) loadSubmissions(cwid);`
`  90`  `        } else {`
`  91`  `            document.getElementById('gradeError').innerText = res.message || 'Failed to save grade';`
  - → Get HTML element by id.
`  92`  `            document.getElementById('gradeError').style.display = 'block';`
  - → Get HTML element by id.
`  93`  `        }`
`  94`  `    }).catch(err => { console.error(err); document.getElementById('gradeError').innerText = 'Network error'; document.getElementById('gradeError').style.display = 'block'; });`
  - → Get HTML element by id.
`  95`  `}`

---

### `escapeHtml` — lines 95–97

```
function escapeHtml(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtml`.
- **Parameters:** `str`

#### Line-by-line (this function)

`  95`  ``
`  96`  ``
`  97`  `function escapeHtml(str) { if (!str) return ''; return String(str).replace(/[&<>\"]/g, function (m) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[m]; }); }`
  - → Encode text to reduce XSS risk.

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `document.addEventListener('DOMContentLoaded', function () {`
  - → DOM event handler.
`   2`  `    initManageSubmissions();`
`   3`  `});`
`   4`  ``
`   5`  `function initManageSubmissions() {`
`   6`  `    loadAssignments();`
`   7`  `    document.getElementById('btnLoadSubs').addEventListener('click', function () {`
  - → DOM event handler.
`   8`  `        const cwid = parseInt(document.getElementById('ddlAssignments').value);`
  - → Get HTML element by id.
`   9`  `        if (!cwid) return alert('Select an assignment');`
`  10`  `        loadSubmissions(cwid);`
`  11`  `    });`
`  12`  ``
`  13`  `    document.getElementById('btnSubmitGrade').addEventListener('click', function () {`
  - → DOM event handler.
`  14`  `        submitGrade();`
`  15`  `    });`
`  16`  `}`
`  17`  ``
`  18`  `function loadAssignments() {`
`  19`  `    fetch('ManageSubmissions.aspx/GetAssignments', { method: 'POST', headers: { 'Content-Type': 'application/json' } })`
  - → HTTP request to server WebMethod/ashx.
`  20`  `    .then(r => r.json()).then(d => {`
`  21`  `        const res = d.d || d;`
`  22`  `        const sel = document.getElementById('ddlAssignments');`
  - → Get HTML element by id.
`  23`  `        sel.innerHTML = '';`
  - → Update page HTML.
`  24`  `        if (res && res.success && Array.isArray(res.assignments)) {`
`  25`  `            res.assignments.forEach(a => {`
`  26`  `                const opt = document.createElement('option'); opt.value = a.cwid; opt.textContent = `${a.title} - ${a.course}`; sel.appendChild(opt);`
`  27`  `            });`
`  28`  `        }`
`  29`  `    }).catch(err => console.error(err));`
`  30`  `}`
`  31`  ``
`  32`  `function loadSubmissions(cwid) {`
`  33`  `    const container = document.getElementById('submissionsList');`
  - → Get HTML element by id.
`  34`  `    container.innerHTML = `<div class="text-center py-3 text-muted"><i class="fa-solid fa-circle-notch fa-spin"></i> Loading...</div>`;`
  - → Update page HTML.
`  35`  `    fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })`
  - → HTTP request to server WebMethod/ashx.
`  36`  `    .then(r => r.json()).then(d => {`
`  37`  `        const res = d.d || d;`
`  38`  `        if (!res.success) { container.innerHTML = `<div class="text-danger">${res.message || 'Failed'}</div>`; return; }`
  - → Update page HTML.
`  39`  `        if (!res.submissions || res.submissions.length === 0) { container.innerHTML = `<div class="text-muted">No submissions yet.</div>`; return; }`
  - → Update page HTML.
`  40`  `        container.innerHTML = '';`
  - → Update page HTML.
`  41`  `        res.submissions.forEach(s => {`
`  42`  `            const div = document.createElement('div'); div.className = 'd-flex justify-content-between align-items-center py-2 border-bottom';`
`  43`  `            div.innerHTML = `<div><div class="fw-semibold">${escapeHtml(s.studentName)}</div><div class="small text-muted">${escapeHtml(s.time)}</div></div><div><button class="btn btn-sm btn-light me-2" data-view="${s.sid}">View</button><button class="btn btn-sm btn-pill-accent" data-grade="${s.sid}" data-score="${s.score}">Grade</button></div>`;`
  - → Update page HTML.
`  44`  `            container.appendChild(div);`
`  45`  `        });`
`  46`  ``
`  47`  `        container.querySelectorAll('[data-view]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-view')); viewSubmission(sid); }));`
  - → DOM event handler.
`  48`  `        container.querySelectorAll('[data-grade]').forEach(b => b.addEventListener('click', function () { const sid = parseInt(this.getAttribute('data-grade')); const sc = parseInt(this.getAttribute('data-score')); openGradeModal(sid, sc); }));`
  - → DOM event handler.
`  49`  `    }).catch(err => { console.error(err); document.getElementById('submissionsList').innerHTML = `<div class="text-danger">Network error</div>`; });`
  - → Get HTML element by id.
`  50`  `}`
`  51`  ``
`  52`  `function viewSubmission(sid) {`
`  53`  `    // reuse GetSubmissions to fetch single submission details`
`  54`  `    fetch('ManageSubmissions.aspx/GetSubmissions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: parseInt(document.getElementById('ddlAssignments').value) }) })`
  - → HTTP request to server WebMethod/ashx.
`  55`  `    .then(r => r.json()).then(d => {`
`  56`  `        const res = d.d || d;`
`  57`  `        if (!res.success) return alert('Failed to load');`
`  58`  `        const s = res.submissions.find(x => x.sid === sid);`
`  59`  `        if (!s) return alert('Not found');`
`  60`  `        const body = document.getElementById('gradeSubmissionBody');`
  - → Get HTML element by id.
`  61`  `        body.innerHTML = `<div class="mb-2"><strong>${escapeHtml(s.studentName)}</strong> - <span class="small text-muted">${escapeHtml(s.time)}</span></div><div class="border p-3 bg-white" style="min-height:150px">${escapeHtml(s.text)}</div>`;`
  - → Update page HTML.
`  62`  `        document.getElementById('txtGradeScore').value = s.score >= 0 ? s.score : 0;`
  - → Get HTML element by id.
`  63`  `        document.getElementById('txtGradeFeedback').value = s.review || '';`
  - → Get HTML element by id.
`  64`  `        const modal = new bootstrap.Modal(document.getElementById('gradeModal'));`
  - → Get HTML element by id.
`  65`  `        modal.show();`
`  66`  `        // store sid on submit button`
`  67`  `        document.getElementById('btnSubmitGrade').setAttribute('data-sid', sid);`
  - → Get HTML element by id.
`  68`  `    }).catch(err => console.error(err));`
`  69`  `}`
`  70`  ``
`  71`  `function openGradeModal(sid, score) {`
`  72`  `    // fetch single submission to show`
`  73`  `    viewSubmission(sid);`
`  74`  `}`
`  75`  ``
`  76`  `function submitGrade() {`
`  77`  `    const sid = parseInt(document.getElementById('btnSubmitGrade').getAttribute('data-sid'));`
  - → Get HTML element by id.
`  78`  `    const score = parseInt(document.getElementById('txtGradeScore').value) || 0;`
  - → Get HTML element by id.
`  79`  `    const review = document.getElementById('txtGradeFeedback').value || '';`
  - → Get HTML element by id.
`  80`  `    document.getElementById('gradeError').style.display = 'none';`
  - → Get HTML element by id.
`  81`  `    fetch('ManageSubmissions.aspx/GradeSubmission', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ sid: sid, score: score, review: review }) })`
  - → HTTP request to server WebMethod/ashx.
`  82`  `    .then(r => r.json()).then(d => {`
`  83`  `        const res = d.d || d;`
`  84`  `        if (res.success) {`
`  85`  `            const modal = bootstrap.Modal.getInstance(document.getElementById('gradeModal'));`
  - → Get HTML element by id.
`  86`  `            if (modal) modal.hide();`
`  87`  `            // reload submissions`
`  88`  `            const cwid = parseInt(document.getElementById('ddlAssignments').value);`
  - → Get HTML element by id.
`  89`  `            if (cwid) loadSubmissions(cwid);`
`  90`  `        } else {`
`  91`  `            document.getElementById('gradeError').innerText = res.message || 'Failed to save grade';`
  - → Get HTML element by id.
`  92`  `            document.getElementById('gradeError').style.display = 'block';`
  - → Get HTML element by id.
`  93`  `        }`
`  94`  `    }).catch(err => { console.error(err); document.getElementById('gradeError').innerText = 'Network error'; document.getElementById('gradeError').style.display = 'block'; });`
  - → Get HTML element by id.
`  95`  `}`
`  96`  ``
`  97`  `function escapeHtml(str) { if (!str) return ''; return String(str).replace(/[&<>\"]/g, function (m) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[m]; }); }`
  - → Encode text to reduce XSS risk.

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
