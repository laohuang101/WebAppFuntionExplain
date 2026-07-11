# assignments-edit.js
**Source:** `Pages/Lecturer/Scripts/assignments-edit.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 31
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 6:** `res` — script-level `const`/`let`/`var`
- **Line 22:** `opts` — script-level `const`/`let`/`var`

## Functions / methods (1 found)

### `loadAssignmentDetails` — lines 1–31

```
function loadAssignmentDetails(cwid)
```

#### Explanation

- **Purpose:** Implements `loadAssignmentDetails`.
- **Due date:** Related to assignment closing after the due day.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Parameters:** `cwid`
- **Local variables:** `res`, `opts`

#### Line-by-line (this function)

`   1`  ``
`   2`  `function loadAssignmentDetails(cwid) {`
`   3`  `    if (!cwid) return;`
`   4`  `    fetch('Assignments.aspx/GetAssignmentDetails', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })`
  - → HTTP request to server WebMethod/ashx.
`   5`  `    .then(r => r.json()).then(d => {`
`   6`  `        const res = d.d || d;`
`   7`  `        if (!res.success) return alert('Failed to load assignment');`
`   8`  `        // populate fields`
`   9`  `        document.getElementById('txtTitle').value = res.title || '';`
  - → Get HTML element by id.
`  10`  `        document.getElementById('txtDescription').value = res.description || '';`
  - → Get HTML element by id.
`  11`  `        document.getElementById('txtDueDate').value = res.dueDate || '';`
  - → Assignment deadline; submissions close after due day.
`  12`  `        document.getElementById('chkRequireUpload').checked = !!res.requireUpload;`
  - → Get HTML element by id.
`  13`  `        if (res.type === 'Objective') document.getElementById('typeObjective').checked = true; else document.getElementById('typeSubjective').checked = true;`
  - → Get HTML element by id.
`  14`  `        // rubric`
`  15`  `        rubricItems = [];`
`  16`  `        if (res.rubric && Array.isArray(res.rubric)) res.rubric.forEach(r => rubricItems.push({ criterion: r.criterion, points: r.points }));`
`  17`  `        renderRubricList();`
`  18`  `        // questions`
`  19`  `        questions = [];`
`  20`  `        if (res.questions && Array.isArray(res.questions)) {`
`  21`  `            res.questions.forEach(q => {`
`  22`  `                const opts = (q.options || []).map(o => ({ text: o.text, correct: o.isCorrect }));`
`  23`  `                questions.push({ prompt: q.prompt, options: opts, type: q.qtype });`
`  24`  `            });`
`  25`  `        }`
`  26`  `        renderQuestions();`
`  27`  `        onTypeChange();`
`  28`  `        // store cwid`
`  29`  `        window.currentEditingCWID = cwid;`
`  30`  `    }).catch(err => console.error(err));`
`  31`  `}`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `// Helper to load assignment details into the builder for editing`
`   2`  `function loadAssignmentDetails(cwid) {`
`   3`  `    if (!cwid) return;`
`   4`  `    fetch('Assignments.aspx/GetAssignmentDetails', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })`
  - → HTTP request to server WebMethod/ashx.
`   5`  `    .then(r => r.json()).then(d => {`
`   6`  `        const res = d.d || d;`
`   7`  `        if (!res.success) return alert('Failed to load assignment');`
`   8`  `        // populate fields`
`   9`  `        document.getElementById('txtTitle').value = res.title || '';`
  - → Get HTML element by id.
`  10`  `        document.getElementById('txtDescription').value = res.description || '';`
  - → Get HTML element by id.
`  11`  `        document.getElementById('txtDueDate').value = res.dueDate || '';`
  - → Assignment deadline; submissions close after due day.
`  12`  `        document.getElementById('chkRequireUpload').checked = !!res.requireUpload;`
  - → Get HTML element by id.
`  13`  `        if (res.type === 'Objective') document.getElementById('typeObjective').checked = true; else document.getElementById('typeSubjective').checked = true;`
  - → Get HTML element by id.
`  14`  `        // rubric`
`  15`  `        rubricItems = [];`
`  16`  `        if (res.rubric && Array.isArray(res.rubric)) res.rubric.forEach(r => rubricItems.push({ criterion: r.criterion, points: r.points }));`
`  17`  `        renderRubricList();`
`  18`  `        // questions`
`  19`  `        questions = [];`
`  20`  `        if (res.questions && Array.isArray(res.questions)) {`
`  21`  `            res.questions.forEach(q => {`
`  22`  `                const opts = (q.options || []).map(o => ({ text: o.text, correct: o.isCorrect }));`
`  23`  `                questions.push({ prompt: q.prompt, options: opts, type: q.qtype });`
`  24`  `            });`
`  25`  `        }`
`  26`  `        renderQuestions();`
`  27`  `        onTypeChange();`
`  28`  `        // store cwid`
`  29`  `        window.currentEditingCWID = cwid;`
`  30`  `    }).catch(err => console.error(err));`
`  31`  `}`

## Source snapshot (raw)

```javascript
// Helper to load assignment details into the builder for editing
function loadAssignmentDetails(cwid) {
    if (!cwid) return;
    fetch('Assignments.aspx/GetAssignmentDetails', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })
    .then(r => r.json()).then(d => {
        const res = d.d || d;
        if (!res.success) return alert('Failed to load assignment');
        // populate fields
        document.getElementById('txtTitle').value = res.title || '';
        document.getElementById('txtDescription').value = res.description || '';
        document.getElementById('txtDueDate').value = res.dueDate || '';
        document.getElementById('chkRequireUpload').checked = !!res.requireUpload;
        if (res.type === 'Objective') document.getElementById('typeObjective').checked = true; else document.getElementById('typeSubjective').checked = true;
        // rubric
        rubricItems = [];
        if (res.rubric && Array.isArray(res.rubric)) res.rubric.forEach(r => rubricItems.push({ criterion: r.criterion, points: r.points }));
        renderRubricList();
        // questions
        questions = [];
        if (res.questions && Array.isArray(res.questions)) {
            res.questions.forEach(q => {
                const opts = (q.options || []).map(o => ({ text: o.text, correct: o.isCorrect }));
                questions.push({ prompt: q.prompt, options: opts, type: q.qtype });
            });
        }
        renderQuestions();
        onTypeChange();
        // store cwid
        window.currentEditingCWID = cwid;
    }).catch(err => console.error(err));
}

```
