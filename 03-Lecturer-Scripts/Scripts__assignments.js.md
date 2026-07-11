# assignments.js
**Source:** `Pages/Lecturer/Scripts/assignments.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 387
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `builderType` | `const/let/var` | Assignment builder mode: Text vs Objective. |
| `rubricRows` | `const/let/var` | UI state: grading rubric criteria rows. |
| `objectiveQuestions` | `const/let/var` | UI state: quiz questions being edited. |
| `ASSIGNMENT_TOTAL_PTS` | `const/let/var` | Often a collection related to ASSIGNMENT TOTAL PTS (plural name). |
| `res` | `const/let/var` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `ddl` | `const/let/var` | Drop-down list (select) element. |
| `opt` | `const/let/var` | Option element or optional label. |
| `existingWorksDt` | `const/let/var` | Holds “existing Works Dt” for this scope. |
| `box` | `const/let/var` | Container element for lists/tables. |
| `items` | `const/let/var` | Array of rows for UI tables. |
| `closed` | `const/let/var` | Holds “closed” for this scope. |
| `badge` | `const/let/var` | Holds “badge” for this scope. |
| `list` | `const/let/var` | In-memory collection being built for JSON return. |
| `div` | `const/let/var` | Holds “div” for this scope. |
| `total` | `const/let/var` | Sum of points or total items. |
| `el` | `const/let/var` | Generic DOM element. |
| `hint` | `const/let/var` | Holds “hint” for this scope. |
| `opts` | `const/let/var` | Often a collection related to opts (plural name). |
| `keys` | `const/let/var` | Often a collection related to keys (plural name). |
| `next` | `const/let/var` | Holds “next” for this scope. |
| `card` | `const/let/var` | Holds “card” for this scope. |
| `optionsHtml` | `const/let/var` | Holds “options Html” for this scope. |
| `m` | `const/let/var` | Holds “m” for this scope. |
| `end` | `const/let/var` | Range end or string end index. |
| `err` | `const/let/var` | Error message string or error element. |
| `ok` | `const/let/var` | Boolean success flag. |
| `title` | `const/let/var` | Title of course work / page heading. |
| `instructions` | `const/let/var` | Student-facing assignment instructions (plain part of Description). |
| `cid` | `const/let/var` | Course ID (Courses.CID). |
| `cwidRaw` | `const/let/var` | Holds “cwid Raw” for this scope. |
| `cwid` | `const/let/var` | CourseWork ID (assignment) (CourseWorks.CWID). |
| `dueDate` | `const/let/var` | Assignment deadline (date); after end of that day submissions close. |
| `score` | `const/let/var` | Points earned or max points depending on context. |
| `rubricJson` | `const/let/var` | Holds “rubric Json” for this scope. |
| `objectiveQuestionsJson` | `const/let/var` | Holds “objective Questions Json” for this scope. |
| `rubricSum` | `const/let/var` | Holds “rubric Sum” for this scope. |
| `perQ` | `const/let/var` | Holds “per Q” for this scope. |
| `extra` | `const/let/var` | Dictionary of optional fields inside META. |

## Functions / methods (22 found)

### `setBuilderType` — lines 19–33

#### Signature

```javascript
function setBuilderType(type)
```

#### What it is

Saves or updates **set Builder Type** in the database or UI state.

#### How it works

1. Starts when something calls `setBuilderType`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `type` | `—` | Holds “type” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
  19 | 
  20 | 
  21 | function setBuilderType(type) {
  22 |     builderType = type === 'Objective' ? 'Objective' : 'Text';
  23 |     document.getElementById('btnTypeAssignment').classList.toggle('active', builderType === 'Text');
  24 |     document.getElementById('btnTypeQuiz').classList.toggle('active', builderType === 'Objective');
  25 |     document.getElementById('panelRubric').style.display = builderType === 'Text' ? 'block' : 'none';
  26 |     document.getElementById('panelQuestions').style.display = builderType === 'Objective' ? 'block' : 'none';
  27 |     document.getElementById('timeLimitGroup').style.display = builderType === 'Objective' ? 'block' : 'none';
  28 |     document.getElementById('requireFileGroup').style.display = builderType === 'Text' ? 'block' : 'none';
  29 | 
  30 |     if (builderType === 'Objective' && objectiveQuestions.length === 0) {
  31 |         addObjectiveQuestion();
  32 |     }
  33 | }
```

---

### `loadCourses` — lines 33–56

#### Signature

```javascript
function loadCourses()
```

#### What it is

Browser JS: load the lecturer’s courses into a dropdown.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `ddl` | `—` | Drop-down list (select) element.  DOM element from the page. |
| `opt` | `—` | Option element or optional label. |

#### Code

```javascript
  33 | 
  34 | 
  35 | function loadCourses() {
  36 |     fetch('Assignments.aspx/GetCourses', {
  37 |         method: 'POST',
  38 |         headers: { 'Content-Type': 'application/json' },
  39 |         body: '{}'
  40 |     })
  41 |     .then(r => r.json())
  42 |     .then(data => {
  43 |         const res = data.d || data;
  44 |         const ddl = document.getElementById('ddlCourse');
  45 |         ddl.innerHTML = '<option value="">Select course...</option>';
  46 |         if (res.success && res.courses) {
  47 |             res.courses.forEach(c => {
  48 |                 const opt = document.createElement('option');
  49 |                 opt.value = c.cid;
  50 |                 opt.textContent = c.name;
  51 |                 ddl.appendChild(opt);
  52 |             });
  53 |         }
  54 |     })
  55 |     .catch(console.error);
  56 | }
```

---

### `loadExisting` — lines 58–129

#### Signature

```javascript
function loadExisting()
```

#### What it is

Browser JS: load and display existing assignments in a table.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. If the previous step failed, show the error and stop.
4. Use the assignment due date to decide if submissions are still open.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |
| `box` | `—` | Container element for lists/tables.  DOM element from the page. |
| `items` | `—` | Array of rows for UI tables. |
| `closed` | `—` | Holds “closed” for this scope. |
| `badge` | `—` | Holds “badge” for this scope. |

#### Code

```javascript
  58 | 
  59 | 
  60 | function loadExisting() {
  61 |     fetch('Assignments.aspx/GetCourseWorks', {
  62 |         method: 'POST',
  63 |         headers: { 'Content-Type': 'application/json' },
  64 |         body: '{}',
  65 |         credentials: 'same-origin'
  66 |     })
  67 |     .then(r => r.json())
  68 |     .then(data => {
  69 |         const res = data.d || data;
  70 |         const box = document.getElementById('existingList');
  71 |         if (!box) return;
  72 |         if (!res.success) {
  73 |             box.innerHTML = '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';
  74 |             return;
  75 |         }
  76 |         const items = res.items || [];
  77 |         if (typeof EduDataTable === 'undefined') {
  78 |             box.innerHTML = items.length ? '' : '<div class="text-muted small">No courseworks yet.</div>';
  79 |             items.forEach(function (item) {
  80 |                 box.innerHTML += '<div class="existing-item">' + escapeHtml(item.title) + '</div>';
  81 |             });
  82 |             return;
  83 |         }
  84 |         if (!existingWorksDt) {
  85 |             existingWorksDt = EduDataTable.create({
  86 |                 container: box,
  87 |                 pageSize: 8,
  88 |                 pageSizeOptions: [5, 8, 15, 25],
  89 |                 searchPlaceholder: 'Search title or course...',
  90 |                 emptyMessage: 'No courseworks yet.',
  91 |                 tableClass: 'table table-sm table-hover mb-0 edt-table',
  92 |                 columns: [
  93 |                 {
  94 |                     key: 'title', title: 'Title', sortable: true,
  95 |                     render: function (item) {
  96 |                         return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';
  97 |                     }
  98 |                 },
  99 |                 { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },
 100 |                 { key: 'type', title: 'Type', sortable: true, filter: true, filterLabel: 'Type' },
 101 |                 {
 102 |                     key: 'dueDate', title: 'Due', sortable: true,
 103 |                     render: function (item) {
 104 |                         if (!item.dueDate) return '<span class="text-muted small">—</span>';
 105 |                         var closed = isDueClosed(item.dueDate);
 106 |                         var badge = closed
 107 |                             ? '<span class="badge rounded-pill text-bg-secondary ms-1">Closed</span>'
 108 |                             : '<span class="badge rounded-pill text-bg-success ms-1">Open</span>';
 109 |                         return '<span class="small">' + escapeHtml(item.dueDate) + '</span>' + badge;
 110 |                     }
 111 |                 },
 112 |                 {
 113 |                     key: 'score', title: 'Pts', sortable: true, type: 'number',
 114 |                     render: function () { return '100'; }
 115 |                 },
 116 |                 {
 117 |                     key: '_actions', title: '', sortable: false, search: false, cellClass: 'text-end',
 118 |                     render: function (item) {
 119 |                         return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +
 120 |                         item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';
 121 |                     }
 122 |                 }
 123 |                 ]
 124 |             });
 125 |         }
 126 |         existingWorksDt.setData(items);
 127 |     })
 128 |     .catch(console.error);
 129 | }
```

---

### `render` — lines 95–97

#### Signature

```javascript
function render(item)
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
| `item` | `—` | Holds “item” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
  95 |                     render: function (item) {
  96 |                         return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';
  97 |                     }
```

---

### `render` — lines 103–110

#### Signature

```javascript
function render(item)
```

#### What it is

Updates the page HTML for **render**.

#### How it works

1. Use the assignment due date to decide if submissions are still open.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `item` | `—` | Holds “item” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `closed` | `—` | Holds “closed” for this scope. |
| `badge` | `—` | Holds “badge” for this scope. |

#### Code

```javascript
 103 |                     render: function (item) {
 104 |                         if (!item.dueDate) return '<span class="text-muted small">—</span>';
 105 |                         var closed = isDueClosed(item.dueDate);
 106 |                         var badge = closed
 107 |                             ? '<span class="badge rounded-pill text-bg-secondary ms-1">Closed</span>'
 108 |                             : '<span class="badge rounded-pill text-bg-success ms-1">Open</span>';
 109 |                         return '<span class="small">' + escapeHtml(item.dueDate) + '</span>' + badge;
 110 |                     }
```

---

### `render` — lines 114–114

#### Signature

```javascript
function render()
```

#### What it is

Updates the page HTML for **render**.

#### How it works

1. Starts when something calls `render`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 114 |                     render: function () { return '100'; }
```

---

### `render` — lines 118–121

#### Signature

```javascript
function render(item)
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
| `item` | `—` | Holds “item” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 118 |                     render: function (item) {
 119 |                         return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +
 120 |                         item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';
 121 |                     }
```

---

### `addRubricRow` — lines 129–135

#### Signature

```javascript
function addRubricRow(name, pts)
```

#### What it is

Saves or updates **add Rubric Row** in the database or UI state.

#### How it works

1. Starts when something calls `addRubricRow`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `name` | `—` | Display name of user/course/criterion. |
| `pts` | `—` | Holds “pts” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 129 | 
 130 | 
 131 | function addRubricRow(name, pts) {
 132 |     // New empty rows get 0; user redistributes to keep total 100
 133 |     rubricRows.push({ name: name || '', pts: pts != null ? pts : 0 });
 134 |     renderRubric();
 135 | }
```

---

### `getRubricTotal` — lines 135–139

#### Signature

```javascript
function getRubricTotal()
```

#### What it is

Reads/loads data related to **Rubric Total** and returns it for display or further use.

#### How it works

1. Starts when something calls `getRubricTotal`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 135 | 
 136 | 
 137 | function getRubricTotal() {
 138 |     return rubricRows.reduce(function (s, r) { return s + (Number(r.pts) || 0); }, 0);
 139 | }
```

---

### `removeRubricRow` — lines 139–144

#### Signature

```javascript
function removeRubricRow(i)
```

#### What it is

Deletes or clears **remove Rubric Row** (data or temporary state).

#### How it works

1. Starts when something calls `removeRubricRow`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 139 | 
 140 | 
 141 | function removeRubricRow(i) {
 142 |     rubricRows.splice(i, 1);
 143 |     renderRubric();
 144 | }
```

---

### `renderRubric` — lines 144–164

#### Signature

```javascript
function renderRubric()
```

#### What it is

Updates the page HTML for **render Rubric**.

#### How it works

1. Starts when something calls `renderRubric`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `list` | `—` | In-memory collection being built for JSON return.  DOM element from the page. |
| `div` | `—` | Holds “div” for this scope. |

#### Code

```javascript
 144 | 
 145 | 
 146 | function renderRubric() {
 147 |     const list = document.getElementById('rubricList');
 148 |     list.innerHTML = '';
 149 |     rubricRows.forEach((row, i) => {
 150 |         const div = document.createElement('div');
 151 |         div.className = 'd-flex align-items-center gap-2 mb-2';
 152 |         div.innerHTML = `
 153 |         <i class="fa-solid fa-grip-vertical text-muted"></i>
 154 |         <input type="text" class="form-control form-control-sm" placeholder="Criterion" value="${escapeAttr(row.name)}"
 155 |         oninput="rubricRows[${i}].name=this.value" />
 156 |         <input type="number" class="form-control form-control-sm" style="max-width:80px;" min="0" max="100" value="${row.pts}"
 157 |         oninput="rubricRows[${i}].pts=parseFloat(this.value)||0; updateRubricTotal();" />
 158 |         <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeRubricRow(${i})">
 159 |         <i class="fa-regular fa-trash-can"></i>
 160 |         </button>`;
 161 |         list.appendChild(div);
 162 |     });
 163 |     updateRubricTotal();
 164 | }
```

---

### `updateRubricTotal` — lines 164–183

#### Signature

```javascript
function updateRubricTotal()
```

#### What it is

Saves or updates **update Rubric Total** in the database or UI state.

#### How it works

1. Starts when something calls `updateRubricTotal`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `total` | `—` | Sum of points or total items. |
| `el` | `—` | Generic DOM element.  DOM element from the page. |
| `hint` | `—` | Holds “hint” for this scope.  DOM element from the page. |

#### Code

```javascript
 164 | 
 165 | 
 166 | function updateRubricTotal() {
 167 |     const total = getRubricTotal();
 168 |     const el = document.getElementById('lblRubricTotal');
 169 |     // Always show "out of 100"
 170 |     el.innerText = total + ' / ' + ASSIGNMENT_TOTAL_PTS;
 171 |     if (total === ASSIGNMENT_TOTAL_PTS) {
 172 |         el.classList.remove('text-danger');
 173 |         el.classList.add('text-success');
 174 |     } else {
 175 |         el.classList.remove('text-success');
 176 |         el.classList.add('text-danger');
 177 |     }
 178 |     const hint = document.getElementById('rubricTotalHint');
 179 |     if (hint) {
 180 |         hint.style.display = total === ASSIGNMENT_TOTAL_PTS ? 'none' : 'block';
 181 |         hint.textContent = 'Rubric criteria must total exactly ' + ASSIGNMENT_TOTAL_PTS + ' pts (currently ' + total + ').';
 182 |     }
 183 | }
```

---

### `addObjectiveQuestion` — lines 183–194

#### Signature

```javascript
function addObjectiveQuestion()
```

#### What it is

Saves or updates **add Objective Question** in the database or UI state.

#### How it works

1. Starts when something calls `addObjectiveQuestion`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 183 | 
 184 | 
 185 | function addObjectiveQuestion() {
 186 |     objectiveQuestions.push({
 187 |         question: '',
 188 |         options: { option1: '', option2: '', option3: '', option4: '' },
 189 |         answer: 'option1',
 190 |         explanation: '',
 191 |         oneOrMultipleAnswer: true
 192 |     });
 193 |     renderQuestions();
 194 | }
```

---

### `removeObjectiveQuestion` — lines 194–199

#### Signature

```javascript
function removeObjectiveQuestion(i)
```

#### What it is

Deletes or clears **remove Objective Question** (data or temporary state).

#### How it works

1. Starts when something calls `removeObjectiveQuestion`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 194 | 
 195 | 
 196 | function removeObjectiveQuestion(i) {
 197 |     objectiveQuestions.splice(i, 1);
 198 |     renderQuestions();
 199 | }
```

---

### `addOption` — lines 199–207

#### Signature

```javascript
function addOption(qi)
```

#### What it is

Saves or updates **add Option** in the database or UI state.

#### How it works

1. Starts when something calls `addOption`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `qi` | `—` | Holds “qi” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `opts` | `—` | Often a collection related to opts (plural name). |
| `keys` | `—` | Often a collection related to keys (plural name). |
| `next` | `—` | Holds “next” for this scope.  Literal text string. |

#### Code

```javascript
 199 | 
 200 | 
 201 | function addOption(qi) {
 202 |     const opts = objectiveQuestions[qi].options;
 203 |     const keys = Object.keys(opts);
 204 |     const next = 'option' + (keys.length + 1);
 205 |     opts[next] = '';
 206 |     renderQuestions();
 207 | }
```

---

### `removeOption` — lines 207–212

#### Signature

```javascript
function removeOption(qi, key)
```

#### What it is

Deletes or clears **remove Option** (data or temporary state).

#### How it works

1. Starts when something calls `removeOption`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `qi` | `—` | Holds “qi” for this scope. |
| `key` | `—` | HMAC key bytes or dictionary key. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 207 | 
 208 | 
 209 | function removeOption(qi, key) {
 210 |     delete objectiveQuestions[qi].options[key];
 211 |     renderQuestions();
 212 | }
```

---

### `renderQuestions` — lines 212–258

#### Signature

```javascript
function renderQuestions()
```

#### What it is

Updates the page HTML for **render Questions**.

#### How it works

1. Starts when something calls `renderQuestions`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `list` | `—` | In-memory collection being built for JSON return.  DOM element from the page. |
| `card` | `—` | Holds “card” for this scope. |
| `optionsHtml` | `—` | Holds “options Html” for this scope.  Literal text string. |

#### Code

```javascript
 212 | 
 213 | 
 214 | function renderQuestions() {
 215 |     const list = document.getElementById('questionsList');
 216 |     list.innerHTML = '';
 217 |     objectiveQuestions.forEach((q, qi) => {
 218 |         const card = document.createElement('div');
 219 |         card.className = 'glass-card p-4 mb-3';
 220 |         let optionsHtml = '';
 221 |         Object.keys(q.options).forEach(key => {
 222 |             optionsHtml += `
 223 |             <div class="d-flex align-items-center gap-2 mb-2">
 224 |             <input type="radio" name="ans_${qi}" ${q.answer === key ? 'checked' : ''}
 225 |             onchange="objectiveQuestions[${qi}].answer='${key}'" />
 226 |             <input type="text" class="form-control form-control-sm" placeholder="Option"
 227 |             value="${escapeAttr(q.options[key])}"
 228 |             oninput="objectiveQuestions[${qi}].options['${key}']=this.value" />
 229 |             <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeOption(${qi},'${key}')">
 230 |             <i class="fa-regular fa-trash-can"></i>
 231 |             </button>
 232 |             </div>`;
 233 |         });
 234 |         card.innerHTML = `
 235 |         <div class="d-flex justify-content-between align-items-center mb-3">
 236 |         <span class="fw-bold"><i class="fa-solid fa-grip-vertical text-muted me-2"></i>Question ${qi + 1}</span>
 237 |         <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeObjectiveQuestion(${qi})">
 238 |         <i class="fa-regular fa-trash-can"></i>
 239 |         </button>
 240 |         </div>
 241 |         <input type="text" class="form-control mb-3" placeholder="Question text"
 242 |         value="${escapeAttr(q.question)}"
 243 |         oninput="objectiveQuestions[${qi}].question=this.value" />
 244 |         ${optionsHtml}
 245 |         <button type="button" class="btn btn-link btn-sm p-0 mb-3" style="color:var(--primary-accent);" onclick="addOption(${qi})">+ Add Option</button>
 246 |         <div class="mb-2">
 247 |         <label class="form-label small text-muted mb-1">Answer key (option id)</label>
 248 |         <input type="text" class="form-control form-control-sm" value="${escapeAttr(q.answer)}"
 249 |         oninput="objectiveQuestions[${qi}].answer=this.value" placeholder="e.g. option1" />
 250 |         </div>
 251 |         <div>
 252 |         <label class="form-label small text-muted mb-1">Explanation</label>
 253 |         <textarea class="form-control form-control-sm" rows="2"
 254 |         oninput="objectiveQuestions[${qi}].explanation=this.value">${escapeHtml(q.explanation || '')}</textarea>
 255 |         </div>`;
 256 |         list.appendChild(card);
 257 |     });
 258 | }
```

---

### `isDueClosed` — lines 260–267

#### Signature

```javascript
function isDueClosed(dueDateStr)
```

#### What it is

Checks a condition related to **is Due Closed** and returns true/false (or tries an action safely).

#### How it works

1. Use the assignment due date to decide if submissions are still open.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `dueDateStr` | `—` | Date/time value. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `m` | `—` | Holds “m” for this scope. |
| `end` | `—` | Range end or string end index.  Newly constructed object. |

#### Code

```javascript
 260 | 
 261 | function isDueClosed(dueDateStr) {
 262 |     if (!dueDateStr) return false;
 263 |     var m = String(dueDateStr).match(/^(\d{4})-(\d{2})-(\d{2})/);
 264 |     if (!m) return false;
 265 |     var end = new Date(parseInt(m[1], 10), parseInt(m[2], 10) - 1, parseInt(m[3], 10) + 1, 0, 0, 0, 0);
 266 |     return Date.now() >= end.getTime();
 267 | }
```

---

### `saveAssignment` — lines 267–363

#### Signature

```javascript
function saveAssignment(publish)
```

#### What it is

Browser JS: collect assignment form fields and POST them to the server WebMethod.

#### How it works

1. Read title, instructions, course, due date, rubric/questions from the form.
2. Require a due date when publishing.
3. POST the data to Assignments.aspx/SaveCourseWork as JSON.
4. Show success or error on the page and refresh the list.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `publish` | `—` | Holds “publish” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `err` | `—` | Error message string or error element.  DOM element from the page. |
| `ok` | `—` | Boolean success flag.  DOM element from the page. |
| `title` | `—` | Title of course work / page heading.  DOM element from the page. |
| `instructions` | `—` | Student-facing assignment instructions (plain part of Description).  DOM element from the page. |
| `cid` | `—` | Course ID (Courses.CID).  DOM element from the page. |
| `cwidRaw` | `—` | Holds “cwid Raw” for this scope.  DOM element from the page. |
| `cwid` | `—` | CourseWork ID (assignment) (CourseWorks.CWID). |
| `dueDate` | `—` | Assignment deadline (date); after end of that day submissions close.  DOM element from the page. |
| `score` | `—` | Points earned or max points depending on context. |
| `rubricJson` | `—` | Holds “rubric Json” for this scope. |
| `objectiveQuestionsJson` | `—` | Holds “objective Questions Json” for this scope. |
| `rubricSum` | `—` | Holds “rubric Sum” for this scope. |
| `perQ` | `—` | Holds “per Q” for this scope. |
| `extra` | `—` | Dictionary of optional fields inside META. |
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |

#### Code

```javascript
 267 | 
 268 | 
 269 | function saveAssignment(publish) {
 270 |     const err = document.getElementById('saveError');
 271 |     const ok = document.getElementById('saveOk');
 272 |     err.style.display = 'none';
 273 |     ok.style.display = 'none';
 274 | 
 275 |     const title = document.getElementById('txtTitle').value.trim();
 276 |     const instructions = document.getElementById('txtInstructions').value.trim();
 277 |     const cid = parseInt(document.getElementById('ddlCourse').value, 10) || 0;
 278 |     const cwidRaw = document.getElementById('hfCwid').value;
 279 |     const cwid = cwidRaw ? parseInt(cwidRaw, 10) : null;
 280 |     const dueDate = (document.getElementById('txtDueDate').value || '').trim();
 281 | 
 282 |     if (!title) { err.innerText = 'Title is required.'; err.style.display = 'block'; return; }
 283 |     if (!cid) { err.innerText = 'Select a target course.'; err.style.display = 'block'; return; }
 284 |     // Due date required when publishing so closing is explicit in demos
 285 |     if (publish && !dueDate) {
 286 |         err.innerText = 'Set a due date before publishing (students cannot submit after that day).';
 287 |         err.style.display = 'block';
 288 |         return;
 289 |     }
 290 | 
 291 |     // All assignments / quizzes are always out of 100 pts
 292 |     let score = ASSIGNMENT_TOTAL_PTS;
 293 |     let rubricJson = null;
 294 |     let objectiveQuestionsJson = null;
 295 | 
 296 |     if (builderType === 'Text') {
 297 |         const rubricSum = getRubricTotal();
 298 |         if (rubricSum !== ASSIGNMENT_TOTAL_PTS) {
 299 |             err.innerText = 'Grading rubric must total exactly ' + ASSIGNMENT_TOTAL_PTS +
 300 |             ' pts (currently ' + rubricSum + '). Adjust the criterion points.';
 301 |             err.style.display = 'block';
 302 |             return;
 303 |         }
 304 |         rubricJson = JSON.stringify(rubricRows);
 305 |         score = ASSIGNMENT_TOTAL_PTS;
 306 |     } else {
 307 |         if (objectiveQuestions.length === 0) {
 308 |             err.innerText = 'Add at least one quiz question.';
 309 |             err.style.display = 'block';
 310 |             return;
 311 |         }
 312 |         // Evenly distribute 100 pts across questions (for display in meta)
 313 |         const perQ = Math.round((ASSIGNMENT_TOTAL_PTS / objectiveQuestions.length) * 100) / 100;
 314 |         objectiveQuestions = objectiveQuestions.map(function (q) {
 315 |             q.points = perQ;
 316 |             return q;
 317 |         });
 318 |         objectiveQuestionsJson = JSON.stringify(objectiveQuestions);
 319 |         score = ASSIGNMENT_TOTAL_PTS;
 320 |     }
 321 | 
 322 |     const extra = {
 323 |         dueDate: dueDate || null,
 324 |         timeLimit: document.getElementById('txtTimeLimit').value || null,
 325 |         requireFile: document.getElementById('chkRequireFile').checked,
 326 |         published: !!publish
 327 |     };
 328 | 
 329 |     fetch('Assignments.aspx/SaveCourseWork', {
 330 |         method: 'POST',
 331 |         headers: { 'Content-Type': 'application/json' },
 332 |         body: JSON.stringify({
 333 |             cwid: cwid,
 334 |             cid: cid,
 335 |             title: title,
 336 |             instructions: instructions,
 337 |             type: builderType,
 338 |             score: score,
 339 |             creditGiven: score,
 340 |             rubricJson: rubricJson,
 341 |             extraMetaJson: JSON.stringify(extra),
 342 |             objectiveQuestionsJson: objectiveQuestionsJson
 343 |         })
 344 |     })
 345 |     .then(r => r.json())
 346 |     .then(data => {
 347 |         const res = data.d || data;
 348 |         if (res.success) {
 349 |             document.getElementById('hfCwid').value = res.cwid;
 350 |             ok.innerText = publish ? 'Published successfully.' : 'Draft saved.';
 351 |             ok.style.display = 'block';
 352 |             loadExisting();
 353 |         } else {
 354 |             err.innerText = res.message || 'Save failed.';
 355 |             err.style.display = 'block';
 356 |         }
 357 |     })
 358 |     .catch(e => {
 359 |         err.innerText = 'Network error.';
 360 |         err.style.display = 'block';
 361 |         console.error(e);
 362 |     });
 363 | }
```

---

### `deleteWork` — lines 363–379

#### Signature

```javascript
function deleteWork(cwid)
```

#### What it is

Deletes or clears **delete Work** (data or temporary state).

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Convert a JavaScript object into a JSON string for the server.
3. Parse the server JSON response into a JavaScript object.
4. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cwid` | `—` | CourseWork ID (assignment) (CourseWorks.CWID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `res` | `—` | Result object returned from fetch/WebMethod (`data.d` unwrapped). |

#### Code

```javascript
 363 | 
 364 | 
 365 | function deleteWork(cwid) {
 366 |     if (!confirm('Delete this coursework? This cannot be undone.')) return;
 367 |     fetch('Assignments.aspx/DeleteCourseWork', {
 368 |         method: 'POST',
 369 |         headers: { 'Content-Type': 'application/json' },
 370 |         body: JSON.stringify({ cwid: cwid })
 371 |     })
 372 |     .then(r => r.json())
 373 |     .then(data => {
 374 |         const res = data.d || data;
 375 |         if (res.success) loadExisting();
 376 |         else alert(res.message || 'Delete failed');
 377 |     })
 378 |     .catch(console.error);
 379 | }
```

---

### `escapeHtml` — lines 379–387

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
 379 | 
 380 | 
 381 | function escapeHtml(str) {
 382 |     if (!str) return '';
 383 |     return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
 384 | }
 385 | function escapeAttr(str) {
 386 |     return escapeHtml(str).replace(/'/g, '&#39;');
 387 | }
```

---

### `escapeAttr` — lines 384–387

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
 384 | 
 385 | function escapeAttr(str) {
 386 |     return escapeHtml(str).replace(/'/g, '&#39;');
 387 | }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | /* Assignment Builder - pure-SQL CourseWorks / ObjectiveQuestions UI */
   2 | 
   3 | let builderType = 'Text'; // Text | Objective
   4 | let rubricRows = [];
   5 | let objectiveQuestions = [];
   6 | 
   7 | const ASSIGNMENT_TOTAL_PTS = 100;
   8 | 
   9 | document.addEventListener('DOMContentLoaded', function () {
  10 |     loadCourses();
  11 |     loadExisting();
  12 |     setBuilderType('Text');
  13 |     if (rubricRows.length === 0) {
  14 |         // Defaults always sum to 100 pts
  15 |         addRubricRow('Content & understanding', 40);
  16 |         addRubricRow('Structure & clarity', 30);
  17 |         addRubricRow('Presentation / quality', 30);
  18 |     }
  19 | });
  20 | 
  21 | function setBuilderType(type) {
  22 |     builderType = type === 'Objective' ? 'Objective' : 'Text';
  23 |     document.getElementById('btnTypeAssignment').classList.toggle('active', builderType === 'Text');
  24 |     document.getElementById('btnTypeQuiz').classList.toggle('active', builderType === 'Objective');
  25 |     document.getElementById('panelRubric').style.display = builderType === 'Text' ? 'block' : 'none';
  26 |     document.getElementById('panelQuestions').style.display = builderType === 'Objective' ? 'block' : 'none';
  27 |     document.getElementById('timeLimitGroup').style.display = builderType === 'Objective' ? 'block' : 'none';
  28 |     document.getElementById('requireFileGroup').style.display = builderType === 'Text' ? 'block' : 'none';
  29 | 
  30 |     if (builderType === 'Objective' && objectiveQuestions.length === 0) {
  31 |         addObjectiveQuestion();
  32 |     }
  33 | }
  34 | 
  35 | function loadCourses() {
  36 |     fetch('Assignments.aspx/GetCourses', {
  37 |         method: 'POST',
  38 |         headers: { 'Content-Type': 'application/json' },
  39 |         body: '{}'
  40 |     })
  41 |     .then(r => r.json())
  42 |     .then(data => {
  43 |         const res = data.d || data;
  44 |         const ddl = document.getElementById('ddlCourse');
  45 |         ddl.innerHTML = '<option value="">Select course...</option>';
  46 |         if (res.success && res.courses) {
  47 |             res.courses.forEach(c => {
  48 |                 const opt = document.createElement('option');
  49 |                 opt.value = c.cid;
  50 |                 opt.textContent = c.name;
  51 |                 ddl.appendChild(opt);
  52 |             });
  53 |         }
  54 |     })
  55 |     .catch(console.error);
  56 | }
  57 | 
  58 | let existingWorksDt = null;
  59 | 
  60 | function loadExisting() {
  61 |     fetch('Assignments.aspx/GetCourseWorks', {
  62 |         method: 'POST',
  63 |         headers: { 'Content-Type': 'application/json' },
  64 |         body: '{}',
  65 |         credentials: 'same-origin'
  66 |     })
  67 |     .then(r => r.json())
  68 |     .then(data => {
  69 |         const res = data.d || data;
  70 |         const box = document.getElementById('existingList');
  71 |         if (!box) return;
  72 |         if (!res.success) {
  73 |             box.innerHTML = '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';
  74 |             return;
  75 |         }
  76 |         const items = res.items || [];
  77 |         if (typeof EduDataTable === 'undefined') {
  78 |             box.innerHTML = items.length ? '' : '<div class="text-muted small">No courseworks yet.</div>';
  79 |             items.forEach(function (item) {
  80 |                 box.innerHTML += '<div class="existing-item">' + escapeHtml(item.title) + '</div>';
  81 |             });
  82 |             return;
  83 |         }
  84 |         if (!existingWorksDt) {
  85 |             existingWorksDt = EduDataTable.create({
  86 |                 container: box,
  87 |                 pageSize: 8,
  88 |                 pageSizeOptions: [5, 8, 15, 25],
  89 |                 searchPlaceholder: 'Search title or course...',
  90 |                 emptyMessage: 'No courseworks yet.',
  91 |                 tableClass: 'table table-sm table-hover mb-0 edt-table',
  92 |                 columns: [
  93 |                 {
  94 |                     key: 'title', title: 'Title', sortable: true,
  95 |                     render: function (item) {
  96 |                         return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';
  97 |                     }
  98 |                 },
  99 |                 { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },
 100 |                 { key: 'type', title: 'Type', sortable: true, filter: true, filterLabel: 'Type' },
 101 |                 {
 102 |                     key: 'dueDate', title: 'Due', sortable: true,
 103 |                     render: function (item) {
 104 |                         if (!item.dueDate) return '<span class="text-muted small">—</span>';
 105 |                         var closed = isDueClosed(item.dueDate);
 106 |                         var badge = closed
 107 |                             ? '<span class="badge rounded-pill text-bg-secondary ms-1">Closed</span>'
 108 |                             : '<span class="badge rounded-pill text-bg-success ms-1">Open</span>';
 109 |                         return '<span class="small">' + escapeHtml(item.dueDate) + '</span>' + badge;
 110 |                     }
 111 |                 },
 112 |                 {
 113 |                     key: 'score', title: 'Pts', sortable: true, type: 'number',
 114 |                     render: function () { return '100'; }
 115 |                 },
 116 |                 {
 117 |                     key: '_actions', title: '', sortable: false, search: false, cellClass: 'text-end',
 118 |                     render: function (item) {
 119 |                         return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +
 120 |                         item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';
 121 |                     }
 122 |                 }
 123 |                 ]
 124 |             });
 125 |         }
 126 |         existingWorksDt.setData(items);
 127 |     })
 128 |     .catch(console.error);
 129 | }
 130 | 
 131 | function addRubricRow(name, pts) {
 132 |     // New empty rows get 0; user redistributes to keep total 100
 133 |     rubricRows.push({ name: name || '', pts: pts != null ? pts : 0 });
 134 |     renderRubric();
 135 | }
 136 | 
 137 | function getRubricTotal() {
 138 |     return rubricRows.reduce(function (s, r) { return s + (Number(r.pts) || 0); }, 0);
 139 | }
 140 | 
 141 | function removeRubricRow(i) {
 142 |     rubricRows.splice(i, 1);
 143 |     renderRubric();
 144 | }
 145 | 
 146 | function renderRubric() {
 147 |     const list = document.getElementById('rubricList');
 148 |     list.innerHTML = '';
 149 |     rubricRows.forEach((row, i) => {
 150 |         const div = document.createElement('div');
 151 |         div.className = 'd-flex align-items-center gap-2 mb-2';
 152 |         div.innerHTML = `
 153 |         <i class="fa-solid fa-grip-vertical text-muted"></i>
 154 |         <input type="text" class="form-control form-control-sm" placeholder="Criterion" value="${escapeAttr(row.name)}"
 155 |         oninput="rubricRows[${i}].name=this.value" />
 156 |         <input type="number" class="form-control form-control-sm" style="max-width:80px;" min="0" max="100" value="${row.pts}"
 157 |         oninput="rubricRows[${i}].pts=parseFloat(this.value)||0; updateRubricTotal();" />
 158 |         <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeRubricRow(${i})">
 159 |         <i class="fa-regular fa-trash-can"></i>
 160 |         </button>`;
 161 |         list.appendChild(div);
 162 |     });
 163 |     updateRubricTotal();
 164 | }
 165 | 
 166 | function updateRubricTotal() {
 167 |     const total = getRubricTotal();
 168 |     const el = document.getElementById('lblRubricTotal');
 169 |     // Always show "out of 100"
 170 |     el.innerText = total + ' / ' + ASSIGNMENT_TOTAL_PTS;
 171 |     if (total === ASSIGNMENT_TOTAL_PTS) {
 172 |         el.classList.remove('text-danger');
 173 |         el.classList.add('text-success');
 174 |     } else {
 175 |         el.classList.remove('text-success');
 176 |         el.classList.add('text-danger');
 177 |     }
 178 |     const hint = document.getElementById('rubricTotalHint');
 179 |     if (hint) {
 180 |         hint.style.display = total === ASSIGNMENT_TOTAL_PTS ? 'none' : 'block';
 181 |         hint.textContent = 'Rubric criteria must total exactly ' + ASSIGNMENT_TOTAL_PTS + ' pts (currently ' + total + ').';
 182 |     }
 183 | }
 184 | 
 185 | function addObjectiveQuestion() {
 186 |     objectiveQuestions.push({
 187 |         question: '',
 188 |         options: { option1: '', option2: '', option3: '', option4: '' },
 189 |         answer: 'option1',
 190 |         explanation: '',
 191 |         oneOrMultipleAnswer: true
 192 |     });
 193 |     renderQuestions();
 194 | }
 195 | 
 196 | function removeObjectiveQuestion(i) {
 197 |     objectiveQuestions.splice(i, 1);
 198 |     renderQuestions();
 199 | }
 200 | 
 201 | function addOption(qi) {
 202 |     const opts = objectiveQuestions[qi].options;
 203 |     const keys = Object.keys(opts);
 204 |     const next = 'option' + (keys.length + 1);
 205 |     opts[next] = '';
 206 |     renderQuestions();
 207 | }
 208 | 
 209 | function removeOption(qi, key) {
 210 |     delete objectiveQuestions[qi].options[key];
 211 |     renderQuestions();
 212 | }
 213 | 
 214 | function renderQuestions() {
 215 |     const list = document.getElementById('questionsList');
 216 |     list.innerHTML = '';
 217 |     objectiveQuestions.forEach((q, qi) => {
 218 |         const card = document.createElement('div');
 219 |         card.className = 'glass-card p-4 mb-3';
 220 |         let optionsHtml = '';
 221 |         Object.keys(q.options).forEach(key => {
 222 |             optionsHtml += `
 223 |             <div class="d-flex align-items-center gap-2 mb-2">
 224 |             <input type="radio" name="ans_${qi}" ${q.answer === key ? 'checked' : ''}
 225 |             onchange="objectiveQuestions[${qi}].answer='${key}'" />
 226 |             <input type="text" class="form-control form-control-sm" placeholder="Option"
 227 |             value="${escapeAttr(q.options[key])}"
 228 |             oninput="objectiveQuestions[${qi}].options['${key}']=this.value" />
 229 |             <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeOption(${qi},'${key}')">
 230 |             <i class="fa-regular fa-trash-can"></i>
 231 |             </button>
 232 |             </div>`;
 233 |         });
 234 |         card.innerHTML = `
 235 |         <div class="d-flex justify-content-between align-items-center mb-3">
 236 |         <span class="fw-bold"><i class="fa-solid fa-grip-vertical text-muted me-2"></i>Question ${qi + 1}</span>
 237 |         <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeObjectiveQuestion(${qi})">
 238 |         <i class="fa-regular fa-trash-can"></i>
 239 |         </button>
 240 |         </div>
 241 |         <input type="text" class="form-control mb-3" placeholder="Question text"
 242 |         value="${escapeAttr(q.question)}"
 243 |         oninput="objectiveQuestions[${qi}].question=this.value" />
 244 |         ${optionsHtml}
 245 |         <button type="button" class="btn btn-link btn-sm p-0 mb-3" style="color:var(--primary-accent);" onclick="addOption(${qi})">+ Add Option</button>
 246 |         <div class="mb-2">
 247 |         <label class="form-label small text-muted mb-1">Answer key (option id)</label>
 248 |         <input type="text" class="form-control form-control-sm" value="${escapeAttr(q.answer)}"
 249 |         oninput="objectiveQuestions[${qi}].answer=this.value" placeholder="e.g. option1" />
 250 |         </div>
 251 |         <div>
 252 |         <label class="form-label small text-muted mb-1">Explanation</label>
 253 |         <textarea class="form-control form-control-sm" rows="2"
 254 |         oninput="objectiveQuestions[${qi}].explanation=this.value">${escapeHtml(q.explanation || '')}</textarea>
 255 |         </div>`;
 256 |         list.appendChild(card);
 257 |     });
 258 | }
 259 | 
 260 | /** Due date (yyyy-MM-dd) is open all that calendar day; closed from next midnight. */
 261 | function isDueClosed(dueDateStr) {
 262 |     if (!dueDateStr) return false;
 263 |     var m = String(dueDateStr).match(/^(\d{4})-(\d{2})-(\d{2})/);
 264 |     if (!m) return false;
 265 |     var end = new Date(parseInt(m[1], 10), parseInt(m[2], 10) - 1, parseInt(m[3], 10) + 1, 0, 0, 0, 0);
 266 |     return Date.now() >= end.getTime();
 267 | }
 268 | 
 269 | function saveAssignment(publish) {
 270 |     const err = document.getElementById('saveError');
 271 |     const ok = document.getElementById('saveOk');
 272 |     err.style.display = 'none';
 273 |     ok.style.display = 'none';
 274 | 
 275 |     const title = document.getElementById('txtTitle').value.trim();
 276 |     const instructions = document.getElementById('txtInstructions').value.trim();
 277 |     const cid = parseInt(document.getElementById('ddlCourse').value, 10) || 0;
 278 |     const cwidRaw = document.getElementById('hfCwid').value;
 279 |     const cwid = cwidRaw ? parseInt(cwidRaw, 10) : null;
 280 |     const dueDate = (document.getElementById('txtDueDate').value || '').trim();
 281 | 
 282 |     if (!title) { err.innerText = 'Title is required.'; err.style.display = 'block'; return; }
 283 |     if (!cid) { err.innerText = 'Select a target course.'; err.style.display = 'block'; return; }
 284 |     // Due date required when publishing so closing is explicit in demos
 285 |     if (publish && !dueDate) {
 286 |         err.innerText = 'Set a due date before publishing (students cannot submit after that day).';
 287 |         err.style.display = 'block';
 288 |         return;
 289 |     }
 290 | 
 291 |     // All assignments / quizzes are always out of 100 pts
 292 |     let score = ASSIGNMENT_TOTAL_PTS;
 293 |     let rubricJson = null;
 294 |     let objectiveQuestionsJson = null;
 295 | 
 296 |     if (builderType === 'Text') {
 297 |         const rubricSum = getRubricTotal();
 298 |         if (rubricSum !== ASSIGNMENT_TOTAL_PTS) {
 299 |             err.innerText = 'Grading rubric must total exactly ' + ASSIGNMENT_TOTAL_PTS +
 300 |             ' pts (currently ' + rubricSum + '). Adjust the criterion points.';
 301 |             err.style.display = 'block';
 302 |             return;
 303 |         }
 304 |         rubricJson = JSON.stringify(rubricRows);
 305 |         score = ASSIGNMENT_TOTAL_PTS;
 306 |     } else {
 307 |         if (objectiveQuestions.length === 0) {
 308 |             err.innerText = 'Add at least one quiz question.';
 309 |             err.style.display = 'block';
 310 |             return;
 311 |         }
 312 |         // Evenly distribute 100 pts across questions (for display in meta)
 313 |         const perQ = Math.round((ASSIGNMENT_TOTAL_PTS / objectiveQuestions.length) * 100) / 100;
 314 |         objectiveQuestions = objectiveQuestions.map(function (q) {
 315 |             q.points = perQ;
 316 |             return q;
 317 |         });
 318 |         objectiveQuestionsJson = JSON.stringify(objectiveQuestions);
 319 |         score = ASSIGNMENT_TOTAL_PTS;
 320 |     }
 321 | 
 322 |     const extra = {
 323 |         dueDate: dueDate || null,
 324 |         timeLimit: document.getElementById('txtTimeLimit').value || null,
 325 |         requireFile: document.getElementById('chkRequireFile').checked,
 326 |         published: !!publish
 327 |     };
 328 | 
 329 |     fetch('Assignments.aspx/SaveCourseWork', {
 330 |         method: 'POST',
 331 |         headers: { 'Content-Type': 'application/json' },
 332 |         body: JSON.stringify({
 333 |             cwid: cwid,
 334 |             cid: cid,
 335 |             title: title,
 336 |             instructions: instructions,
 337 |             type: builderType,
 338 |             score: score,
 339 |             creditGiven: score,
 340 |             rubricJson: rubricJson,
 341 |             extraMetaJson: JSON.stringify(extra),
 342 |             objectiveQuestionsJson: objectiveQuestionsJson
 343 |         })
 344 |     })
 345 |     .then(r => r.json())
 346 |     .then(data => {
 347 |         const res = data.d || data;
 348 |         if (res.success) {
 349 |             document.getElementById('hfCwid').value = res.cwid;
 350 |             ok.innerText = publish ? 'Published successfully.' : 'Draft saved.';
 351 |             ok.style.display = 'block';
 352 |             loadExisting();
 353 |         } else {
 354 |             err.innerText = res.message || 'Save failed.';
 355 |             err.style.display = 'block';
 356 |         }
 357 |     })
 358 |     .catch(e => {
 359 |         err.innerText = 'Network error.';
 360 |         err.style.display = 'block';
 361 |         console.error(e);
 362 |     });
 363 | }
 364 | 
 365 | function deleteWork(cwid) {
 366 |     if (!confirm('Delete this coursework? This cannot be undone.')) return;
 367 |     fetch('Assignments.aspx/DeleteCourseWork', {
 368 |         method: 'POST',
 369 |         headers: { 'Content-Type': 'application/json' },
 370 |         body: JSON.stringify({ cwid: cwid })
 371 |     })
 372 |     .then(r => r.json())
 373 |     .then(data => {
 374 |         const res = data.d || data;
 375 |         if (res.success) loadExisting();
 376 |         else alert(res.message || 'Delete failed');
 377 |     })
 378 |     .catch(console.error);
 379 | }
 380 | 
 381 | function escapeHtml(str) {
 382 |     if (!str) return '';
 383 |     return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
 384 | }
 385 | function escapeAttr(str) {
 386 |     return escapeHtml(str).replace(/'/g, '&#39;');
 387 | }
```
