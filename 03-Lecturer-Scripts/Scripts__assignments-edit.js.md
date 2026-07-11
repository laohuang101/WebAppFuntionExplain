# assignments-edit.js
**Source:** `Pages/Lecturer/Scripts/assignments-edit.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 31
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `const/let/var` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `opts` | `const/let/var` | Often a collection related to opts (plural name). |

## Functions / methods (1 found)

### `loadAssignmentDetails` — lines 1–31

#### Signature

```javascript
function loadAssignmentDetails(cwid)
```

#### What it is

Reads/loads data related to **Assignment Details** and returns it for display or further use.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. Show a simple popup message to the user.
4. Update a page element (text, HTML, value, or enabled/disabled).
5. Use the assignment due date to decide if submissions are still open.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `—` | CourseWork ID (assignment) (CourseWorks.CWID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `opts` | `—` | Often a collection related to opts (plural name). |

#### Code

```javascript
   1 | 
   2 | function loadAssignmentDetails(cwid) {
   3 |     if (!cwid) return;
   4 |     fetch('Assignments.aspx/GetAssignmentDetails', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })
   5 |     .then(r => r.json()).then(d => {
   6 |         const res = d.d || d;
   7 |         if (!res.success) return alert('Failed to load assignment');
   8 |         // populate fields
   9 |         document.getElementById('txtTitle').value = res.title || '';
  10 |         document.getElementById('txtDescription').value = res.description || '';
  11 |         document.getElementById('txtDueDate').value = res.dueDate || '';
  12 |         document.getElementById('chkRequireUpload').checked = !!res.requireUpload;
  13 |         if (res.type === 'Objective') document.getElementById('typeObjective').checked = true; else document.getElementById('typeSubjective').checked = true;
  14 |         // rubric
  15 |         rubricItems = [];
  16 |         if (res.rubric && Array.isArray(res.rubric)) res.rubric.forEach(r => rubricItems.push({ criterion: r.criterion, points: r.points }));
  17 |         renderRubricList();
  18 |         // questions
  19 |         questions = [];
  20 |         if (res.questions && Array.isArray(res.questions)) {
  21 |             res.questions.forEach(q => {
  22 |                 const opts = (q.options || []).map(o => ({ text: o.text, correct: o.isCorrect }));
  23 |                 questions.push({ prompt: q.prompt, options: opts, type: q.qtype });
  24 |             });
  25 |         }
  26 |         renderQuestions();
  27 |         onTypeChange();
  28 |         // store cwid
  29 |         window.currentEditingCWID = cwid;
  30 |     }).catch(err => console.error(err));
  31 | }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | // Helper to load assignment details into the builder for editing
   2 | function loadAssignmentDetails(cwid) {
   3 |     if (!cwid) return;
   4 |     fetch('Assignments.aspx/GetAssignmentDetails', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ cwid: cwid }) })
   5 |     .then(r => r.json()).then(d => {
   6 |         const res = d.d || d;
   7 |         if (!res.success) return alert('Failed to load assignment');
   8 |         // populate fields
   9 |         document.getElementById('txtTitle').value = res.title || '';
  10 |         document.getElementById('txtDescription').value = res.description || '';
  11 |         document.getElementById('txtDueDate').value = res.dueDate || '';
  12 |         document.getElementById('chkRequireUpload').checked = !!res.requireUpload;
  13 |         if (res.type === 'Objective') document.getElementById('typeObjective').checked = true; else document.getElementById('typeSubjective').checked = true;
  14 |         // rubric
  15 |         rubricItems = [];
  16 |         if (res.rubric && Array.isArray(res.rubric)) res.rubric.forEach(r => rubricItems.push({ criterion: r.criterion, points: r.points }));
  17 |         renderRubricList();
  18 |         // questions
  19 |         questions = [];
  20 |         if (res.questions && Array.isArray(res.questions)) {
  21 |             res.questions.forEach(q => {
  22 |                 const opts = (q.options || []).map(o => ({ text: o.text, correct: o.isCorrect }));
  23 |                 questions.push({ prompt: q.prompt, options: opts, type: q.qtype });
  24 |             });
  25 |         }
  26 |         renderQuestions();
  27 |         onTypeChange();
  28 |         // store cwid
  29 |         window.currentEditingCWID = cwid;
  30 |     }).catch(err => console.error(err));
  31 | }
```
