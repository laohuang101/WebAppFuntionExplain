# assignments.js
**Source:** `Pages/Lecturer/Scripts/assignments.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 387
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 2:** `builderType` — script-level `const`/`let`/`var` — **Assignment builder mode: Text vs Objective.**
- **Line 4:** `rubricRows` — script-level `const`/`let`/`var` — **UI state: grading rubric criteria rows.**
- **Line 5:** `objectiveQuestions` — script-level `const`/`let`/`var` — **UI state: quiz questions being edited.**
- **Line 6:** `ASSIGNMENT_TOTAL_PTS` — script-level `const`/`let`/`var` — **Often a collection related to ASSIGNMENT TOTAL PTS (plural name).**
- **Line 43:** `res` — script-level `const`/`let`/`var` — **Result object returned from fetch/WebMethod (`data.d` unwrapped).**
- **Line 44:** `ddl` — script-level `const`/`let`/`var` — **Drop-down list (select) element.**
- **Line 48:** `opt` — script-level `const`/`let`/`var` — **Option element or optional label.**
- **Line 57:** `existingWorksDt` — script-level `const`/`let`/`var` — **Holds “existing Works Dt” for this scope.**
- **Line 70:** `box` — script-level `const`/`let`/`var` — **Container element for lists/tables.**
- **Line 76:** `items` — script-level `const`/`let`/`var` — **Array of rows for UI tables.**
- **Line 105:** `closed` — script-level `const`/`let`/`var` — **Holds “closed” for this scope.**
- **Line 106:** `badge` — script-level `const`/`let`/`var` — **Holds “badge” for this scope.**
- **Line 147:** `list` — script-level `const`/`let`/`var` — **In-memory collection being built for JSON return.**
- **Line 150:** `div` — script-level `const`/`let`/`var` — **Holds “div” for this scope.**
- **Line 167:** `total` — script-level `const`/`let`/`var` — **Sum of points or total items.**
- **Line 168:** `el` — script-level `const`/`let`/`var` — **Generic DOM element.**
- **Line 178:** `hint` — script-level `const`/`let`/`var` — **Holds “hint” for this scope.**
- **Line 202:** `opts` — script-level `const`/`let`/`var` — **Often a collection related to opts (plural name).**
- **Line 203:** `keys` — script-level `const`/`let`/`var` — **Often a collection related to keys (plural name).**
- **Line 204:** `next` — script-level `const`/`let`/`var` — **Holds “next” for this scope.**
- **Line 218:** `card` — script-level `const`/`let`/`var` — **Holds “card” for this scope.**
- **Line 220:** `optionsHtml` — script-level `const`/`let`/`var` — **Holds “options Html” for this scope.**
- **Line 263:** `m` — script-level `const`/`let`/`var` — **Holds “m” for this scope.**
- **Line 265:** `end` — script-level `const`/`let`/`var` — **Range end or string end index.**
- **Line 270:** `err` — script-level `const`/`let`/`var` — **Error message string or error element.**
- **Line 271:** `ok` — script-level `const`/`let`/`var` — **Boolean success flag.**
- **Line 274:** `title` — script-level `const`/`let`/`var` — **Title of course work / page heading.**
- **Line 276:** `instructions` — script-level `const`/`let`/`var` — **Student-facing assignment instructions (plain part of Description).**
- **Line 277:** `cid` — script-level `const`/`let`/`var` — **Course ID (Courses.CID).**
- **Line 278:** `cwidRaw` — script-level `const`/`let`/`var` — **Holds “cwid Raw” for this scope.**
- **Line 279:** `cwid` — script-level `const`/`let`/`var` — **CourseWork ID (assignment) (CourseWorks.CWID).**
- **Line 280:** `dueDate` — script-level `const`/`let`/`var` — **Assignment deadline (date); after end of that day submissions close.**
- **Line 292:** `score` — script-level `const`/`let`/`var` — **Points earned or max points depending on context.**
- **Line 293:** `rubricJson` — script-level `const`/`let`/`var` — **Holds “rubric Json” for this scope.**
- **Line 294:** `objectiveQuestionsJson` — script-level `const`/`let`/`var` — **Holds “objective Questions Json” for this scope.**
- **Line 297:** `rubricSum` — script-level `const`/`let`/`var` — **Holds “rubric Sum” for this scope.**
- **Line 313:** `perQ` — script-level `const`/`let`/`var` — **Holds “per Q” for this scope.**
- **Line 321:** `extra` — script-level `const`/`let`/`var` — **Dictionary of optional fields inside META.**

## Functions / methods (22 found)

### `setBuilderType` — lines 19–33

```javascript
function setBuilderType(type)
```

#### Explanation

- **Purpose:** Implements `setBuilderType`.
- **Pattern:** Persist changes.
- **Parameters (what each means):**
- `type` — Holds “type” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L23:** Get HTML element by id.
- **L24:** Get HTML element by id.
- **L25:** Get HTML element by id.
- **L26:** Get HTML element by id.
- **L27:** Get HTML element by id.
- **L28:** Get HTML element by id.

---

### `loadCourses` — lines 33–56

```javascript
function loadCourses()
```

#### Explanation

- **Purpose:** Implements `loadCourses`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `ddl` — Drop-down list (select) element.  DOM element from the page.
- `opt` — Option element or optional label.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L36:** HTTP request to server WebMethod/ashx.
- **L43:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L44:** Get HTML element by id. | `ddl` means: Drop-down list (select) element.  DOM element from the page.
- **L45:** Update page HTML.
- **L48:** `opt` means: Option element or optional label.

---

### `loadExisting` — lines 58–129

```javascript
function loadExisting()
```

#### Explanation

- **Purpose:** Implements `loadExisting`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).
- `box` — Container element for lists/tables.  DOM element from the page.
- `items` — Array of rows for UI tables.
- `closed` — Holds “closed” for this scope.
- `badge` — Holds “badge” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L61:** HTTP request to server WebMethod/ashx.
- **L69:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L70:** Get HTML element by id. | `box` means: Container element for lists/tables.  DOM element from the page.
- **L73:** Update page HTML.
- **L76:** `items` means: Array of rows for UI tables.
- **L77:** In-memory result set from ADO.NET.
- **L78:** Update page HTML.
- **L80:** Update page HTML.
- **L85:** In-memory result set from ADO.NET.
- **L96:** Encode text to reduce XSS risk.
- **L102:** Assignment deadline; submissions close after due day.
- **L104:** Assignment deadline; submissions close after due day.
- **L105:** Assignment deadline; submissions close after due day. | `closed` means: Holds “closed” for this scope.
- **L106:** `badge` means: Holds “badge” for this scope.
- **L109:** Assignment deadline; submissions close after due day.

---

### `render` — lines 95–97

```javascript
function render(item)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters (what each means):**
- `item` — Holds “item” for this scope.

#### Line-by-line (this function)

```javascript
  95 |                     render: function (item) {
  96 |                         return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';
  97 |                     }
```

**Line notes** (what code + variables mean)

- **L96:** Encode text to reduce XSS risk.

---

### `render` — lines 103–110

```javascript
function render(item)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Due date:** Related to assignment closing after the due day.
- **Parameters (what each means):**
- `item` — Holds “item” for this scope.
- **Local variables (what each means):**
- `closed` — Holds “closed” for this scope.
- `badge` — Holds “badge” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L104:** Assignment deadline; submissions close after due day.
- **L105:** Assignment deadline; submissions close after due day. | `closed` means: Holds “closed” for this scope.
- **L106:** `badge` means: Holds “badge” for this scope.
- **L109:** Assignment deadline; submissions close after due day.

---

### `render` — lines 114–114

```javascript
function render()
```

#### Explanation

- **Purpose:** Implements `render`.

#### Line-by-line (this function)

```javascript
 114 |                     render: function () { return '100'; }
```

---

### `render` — lines 118–121

```javascript
function render(item)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters (what each means):**
- `item` — Holds “item” for this scope.

#### Line-by-line (this function)

```javascript
 118 |                     render: function (item) {
 119 |                         return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +
 120 |                         item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';
 121 |                     }
```

---

### `addRubricRow` — lines 129–135

```javascript
function addRubricRow(name, pts)
```

#### Explanation

- **Purpose:** Implements `addRubricRow`.
- **Parameters (what each means):**
- `name` — Display name of user/course/criterion.
- `pts` — Holds “pts” for this scope.

#### Line-by-line (this function)

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

```javascript
function getRubricTotal()
```

#### Explanation

- **Purpose:** Implements `getRubricTotal`.
- **Pattern:** Read/load data for display.

#### Line-by-line (this function)

```javascript
 135 | 
 136 | 
 137 | function getRubricTotal() {
 138 |     return rubricRows.reduce(function (s, r) { return s + (Number(r.pts) || 0); }, 0);
 139 | }
```

---

### `removeRubricRow` — lines 139–144

```javascript
function removeRubricRow(i)
```

#### Explanation

- **Purpose:** Implements `removeRubricRow`.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `i` — Loop index (0-based counter in for-loops).

#### Line-by-line (this function)

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

```javascript
function renderRubric()
```

#### Explanation

- **Purpose:** Implements `renderRubric`.
- **Local variables (what each means):**
- `list` — In-memory collection being built for JSON return.  DOM element from the page.
- `div` — Holds “div” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L147:** Get HTML element by id. | `list` means: In-memory collection being built for JSON return.  DOM element from the page.
- **L148:** Update page HTML.
- **L150:** `div` means: Holds “div” for this scope.
- **L152:** Update page HTML.

---

### `updateRubricTotal` — lines 164–183

```javascript
function updateRubricTotal()
```

#### Explanation

- **Purpose:** Implements `updateRubricTotal`.
- **Pattern:** Persist changes.
- **Local variables (what each means):**
- `total` — Sum of points or total items.
- `el` — Generic DOM element.  DOM element from the page.
- `hint` — Holds “hint” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L167:** `total` means: Sum of points or total items.
- **L168:** Get HTML element by id. | `el` means: Generic DOM element.  DOM element from the page.
- **L178:** Get HTML element by id. | `hint` means: Holds “hint” for this scope.  DOM element from the page.

---

### `addObjectiveQuestion` — lines 183–194

```javascript
function addObjectiveQuestion()
```

#### Explanation

- **Purpose:** Implements `addObjectiveQuestion`.

#### Line-by-line (this function)

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

```javascript
function removeObjectiveQuestion(i)
```

#### Explanation

- **Purpose:** Implements `removeObjectiveQuestion`.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `i` — Loop index (0-based counter in for-loops).

#### Line-by-line (this function)

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

```javascript
function addOption(qi)
```

#### Explanation

- **Purpose:** Implements `addOption`.
- **Parameters (what each means):**
- `qi` — Holds “qi” for this scope.
- **Local variables (what each means):**
- `opts` — Often a collection related to opts (plural name).
- `keys` — Often a collection related to keys (plural name).
- `next` — Holds “next” for this scope.  Literal text string.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L202:** `opts` means: Often a collection related to opts (plural name).
- **L203:** `keys` means: Often a collection related to keys (plural name).
- **L204:** `next` means: Holds “next” for this scope.  Literal text string.

---

### `removeOption` — lines 207–212

```javascript
function removeOption(qi, key)
```

#### Explanation

- **Purpose:** Implements `removeOption`.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `qi` — Holds “qi” for this scope.
- `key` — HMAC key bytes or dictionary key.

#### Line-by-line (this function)

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

```javascript
function renderQuestions()
```

#### Explanation

- **Purpose:** Implements `renderQuestions`.
- **Local variables (what each means):**
- `list` — In-memory collection being built for JSON return.  DOM element from the page.
- `card` — Holds “card” for this scope.
- `optionsHtml` — Holds “options Html” for this scope.  Literal text string.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L215:** Get HTML element by id. | `list` means: In-memory collection being built for JSON return.  DOM element from the page.
- **L216:** Update page HTML.
- **L218:** `card` means: Holds “card” for this scope.
- **L220:** `optionsHtml` means: Holds “options Html” for this scope.  Literal text string.
- **L234:** Update page HTML.
- **L254:** Encode text to reduce XSS risk.

---

### `isDueClosed` — lines 260–267

```javascript
function isDueClosed(dueDateStr)
```

#### Explanation

- **Purpose:** Implements `isDueClosed`.
- **Due date:** Related to assignment closing after the due day.
- **Parameters (what each means):**
- `dueDateStr` — Date/time value.
- **Local variables (what each means):**
- `m` — Holds “m” for this scope.
- `end` — Range end or string end index.  Newly constructed object.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L261:** Assignment deadline; submissions close after due day.
- **L262:** Assignment deadline; submissions close after due day.
- **L263:** Assignment deadline; submissions close after due day. | `m` means: Holds “m” for this scope.
- **L265:** `end` means: Range end or string end index.  Newly constructed object.

---

### `saveAssignment` — lines 267–363

```javascript
function saveAssignment(publish)
```

#### Explanation

- **Purpose:** Implements `saveAssignment`.
- **Due date:** Related to assignment closing after the due day.
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Persist changes.
- **Parameters (what each means):**
- `publish` — Holds “publish” for this scope.
- **Local variables (what each means):**
- `err` — Error message string or error element.  DOM element from the page.
- `ok` — Boolean success flag.  DOM element from the page.
- `title` — Title of course work / page heading.  DOM element from the page.
- `instructions` — Student-facing assignment instructions (plain part of Description).  DOM element from the page.
- `cid` — Course ID (Courses.CID).  DOM element from the page.
- `cwidRaw` — Holds “cwid Raw” for this scope.  DOM element from the page.
- `cwid` — CourseWork ID (assignment) (CourseWorks.CWID).
- `dueDate` — Assignment deadline (date); after end of that day submissions close.  DOM element from the page.
- `score` — Points earned or max points depending on context.
- `rubricJson` — Holds “rubric Json” for this scope.
- `objectiveQuestionsJson` — Holds “objective Questions Json” for this scope.
- `rubricSum` — Holds “rubric Sum” for this scope.
- `perQ` — Holds “per Q” for this scope.
- `extra` — Dictionary of optional fields inside META.
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L270:** Get HTML element by id. | `err` means: Error message string or error element.  DOM element from the page.
- **L271:** Get HTML element by id. | `ok` means: Boolean success flag.  DOM element from the page.
- **L275:** Get HTML element by id. | `title` means: Title of course work / page heading.  DOM element from the page.
- **L276:** Get HTML element by id. | `instructions` means: Student-facing assignment instructions (plain part of Description).  DOM element from the page.
- **L277:** Get HTML element by id. | `cid` means: Course ID (Courses.CID).  DOM element from the page.
- **L278:** Get HTML element by id. | `cwidRaw` means: Holds “cwid Raw” for this scope.  DOM element from the page.
- **L279:** `cwid` means: CourseWork ID (assignment) (CourseWorks.CWID).
- **L280:** Assignment deadline; submissions close after due day. | `dueDate` means: Assignment deadline (date); after end of that day submissions close.  DOM element from the page.
- **L285:** Assignment deadline; submissions close after due day.
- **L292:** `score` means: Points earned or max points depending on context.
- **L293:** `rubricJson` means: Holds “rubric Json” for this scope.
- **L294:** `objectiveQuestionsJson` means: Holds “objective Questions Json” for this scope.
- **L297:** `rubricSum` means: Holds “rubric Sum” for this scope.
- **L304:** JS object ↔ JSON text.
- **L313:** `perQ` means: Holds “per Q” for this scope.
- **L318:** JS object ↔ JSON text.
- **L322:** `extra` means: Dictionary of optional fields inside META.
- **L323:** Assignment deadline; submissions close after due day.
- **L324:** Get HTML element by id.
- **L325:** Get HTML element by id.
- **L329:** HTTP request to server WebMethod/ashx.
- **L332:** JS object ↔ JSON text.
- **L341:** JS object ↔ JSON text.
- **L347:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L349:** Get HTML element by id.

---

### `deleteWork` — lines 363–379

```javascript
function deleteWork(cwid)
```

#### Explanation

- **Purpose:** Implements `deleteWork`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `cwid` — CourseWork ID (assignment) (CourseWorks.CWID).
- **Local variables (what each means):**
- `res` — Result object returned from fetch/WebMethod (`data.d` unwrapped).

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L367:** HTTP request to server WebMethod/ashx.
- **L370:** JS object ↔ JSON text.
- **L374:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).

---

### `escapeHtml` — lines 379–387

```javascript
function escapeHtml(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtml`.
- **Parameters (what each means):**
- `str` — String value: str.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L381:** Encode text to reduce XSS risk.
- **L386:** Encode text to reduce XSS risk.

---

### `escapeAttr` — lines 384–387

```javascript
function escapeAttr(str)
```

#### Explanation

- **Purpose:** Implements `escapeAttr`.
- **Parameters (what each means):**
- `str` — String value: str.

#### Line-by-line (this function)

```javascript
 384 | 
 385 | function escapeAttr(str) {
 386 |     return escapeHtml(str).replace(/'/g, '&#39;');
 387 | }
```

**Line notes** (what code + variables mean)

- **L386:** Encode text to reduce XSS risk.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L3:** `builderType` means: Assignment builder mode: Text vs Objective.  Literal text string.
- **L4:** `rubricRows` means: UI state: grading rubric criteria rows.
- **L5:** `objectiveQuestions` means: UI state: quiz questions being edited.
- **L7:** `ASSIGNMENT_TOTAL_PTS` means: Often a collection related to ASSIGNMENT TOTAL PTS (plural name).  Literal number `100`.
- **L9:** DOM event handler.
- **L23:** Get HTML element by id.
- **L24:** Get HTML element by id.
- **L25:** Get HTML element by id.
- **L26:** Get HTML element by id.
- **L27:** Get HTML element by id.
- **L28:** Get HTML element by id.
- **L36:** HTTP request to server WebMethod/ashx.
- **L43:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L44:** Get HTML element by id. | `ddl` means: Drop-down list (select) element.  DOM element from the page.
- **L45:** Update page HTML.
- **L48:** `opt` means: Option element or optional label.
- **L58:** `existingWorksDt` means: Holds “existing Works Dt” for this scope.
- **L61:** HTTP request to server WebMethod/ashx.
- **L69:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L70:** Get HTML element by id. | `box` means: Container element for lists/tables.  DOM element from the page.
- **L73:** Update page HTML.
- **L76:** `items` means: Array of rows for UI tables.
- **L77:** In-memory result set from ADO.NET.
- **L78:** Update page HTML.
- **L80:** Update page HTML.
- **L85:** In-memory result set from ADO.NET.
- **L96:** Encode text to reduce XSS risk.
- **L102:** Assignment deadline; submissions close after due day.
- **L104:** Assignment deadline; submissions close after due day.
- **L105:** Assignment deadline; submissions close after due day. | `closed` means: Holds “closed” for this scope.
- **L106:** `badge` means: Holds “badge” for this scope.
- **L109:** Assignment deadline; submissions close after due day.
- **L147:** Get HTML element by id. | `list` means: In-memory collection being built for JSON return.  DOM element from the page.
- **L148:** Update page HTML.
- **L150:** `div` means: Holds “div” for this scope.
- **L152:** Update page HTML.
- **L167:** `total` means: Sum of points or total items.
- **L168:** Get HTML element by id. | `el` means: Generic DOM element.  DOM element from the page.
- **L178:** Get HTML element by id. | `hint` means: Holds “hint” for this scope.  DOM element from the page.
- **L202:** `opts` means: Often a collection related to opts (plural name).
- **L203:** `keys` means: Often a collection related to keys (plural name).
- **L204:** `next` means: Holds “next” for this scope.  Literal text string.
- **L215:** Get HTML element by id. | `list` means: In-memory collection being built for JSON return.  DOM element from the page.
- **L216:** Update page HTML.
- **L218:** `card` means: Holds “card” for this scope.
- **L220:** `optionsHtml` means: Holds “options Html” for this scope.  Literal text string.
- **L234:** Update page HTML.
- **L254:** Encode text to reduce XSS risk.
- **L261:** Assignment deadline; submissions close after due day.
- **L262:** Assignment deadline; submissions close after due day.
- **L263:** Assignment deadline; submissions close after due day. | `m` means: Holds “m” for this scope.
- **L265:** `end` means: Range end or string end index.  Newly constructed object.
- **L270:** Get HTML element by id. | `err` means: Error message string or error element.  DOM element from the page.
- **L271:** Get HTML element by id. | `ok` means: Boolean success flag.  DOM element from the page.
- **L275:** Get HTML element by id. | `title` means: Title of course work / page heading.  DOM element from the page.
- **L276:** Get HTML element by id. | `instructions` means: Student-facing assignment instructions (plain part of Description).  DOM element from the page.
- **L277:** Get HTML element by id. | `cid` means: Course ID (Courses.CID).  DOM element from the page.
- **L278:** Get HTML element by id. | `cwidRaw` means: Holds “cwid Raw” for this scope.  DOM element from the page.
- **L279:** `cwid` means: CourseWork ID (assignment) (CourseWorks.CWID).
- **L280:** Assignment deadline; submissions close after due day. | `dueDate` means: Assignment deadline (date); after end of that day submissions close.  DOM element from the page.
- **L285:** Assignment deadline; submissions close after due day.
- **L292:** `score` means: Points earned or max points depending on context.
- **L293:** `rubricJson` means: Holds “rubric Json” for this scope.
- **L294:** `objectiveQuestionsJson` means: Holds “objective Questions Json” for this scope.
- **L297:** `rubricSum` means: Holds “rubric Sum” for this scope.
- **L304:** JS object ↔ JSON text.
- **L313:** `perQ` means: Holds “per Q” for this scope.
- **L318:** JS object ↔ JSON text.
- **L322:** `extra` means: Dictionary of optional fields inside META.
- **L323:** Assignment deadline; submissions close after due day.
- **L324:** Get HTML element by id.
- **L325:** Get HTML element by id.
- **L329:** HTTP request to server WebMethod/ashx.
- **L332:** JS object ↔ JSON text.
- **L341:** JS object ↔ JSON text.
- **L347:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L349:** Get HTML element by id.
- **L367:** HTTP request to server WebMethod/ashx.
- **L370:** JS object ↔ JSON text.
- **L374:** `res` means: Result object returned from fetch/WebMethod (`data.d` unwrapped).
- **L381:** Encode text to reduce XSS risk.
- **L386:** Encode text to reduce XSS risk.

## Source snapshot (raw)

```javascript
/* Assignment Builder - pure-SQL CourseWorks / ObjectiveQuestions UI */

let builderType = 'Text'; // Text | Objective
let rubricRows = [];
let objectiveQuestions = [];

const ASSIGNMENT_TOTAL_PTS = 100;

document.addEventListener('DOMContentLoaded', function () {
    loadCourses();
    loadExisting();
    setBuilderType('Text');
    if (rubricRows.length === 0) {
        // Defaults always sum to 100 pts
        addRubricRow('Content & understanding', 40);
        addRubricRow('Structure & clarity', 30);
        addRubricRow('Presentation / quality', 30);
    }
});

function setBuilderType(type) {
    builderType = type === 'Objective' ? 'Objective' : 'Text';
    document.getElementById('btnTypeAssignment').classList.toggle('active', builderType === 'Text');
    document.getElementById('btnTypeQuiz').classList.toggle('active', builderType === 'Objective');
    document.getElementById('panelRubric').style.display = builderType === 'Text' ? 'block' : 'none';
    document.getElementById('panelQuestions').style.display = builderType === 'Objective' ? 'block' : 'none';
    document.getElementById('timeLimitGroup').style.display = builderType === 'Objective' ? 'block' : 'none';
    document.getElementById('requireFileGroup').style.display = builderType === 'Text' ? 'block' : 'none';

    if (builderType === 'Objective' && objectiveQuestions.length === 0) {
        addObjectiveQuestion();
    }
}

function loadCourses() {
    fetch('Assignments.aspx/GetCourses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: '{}'
    })
    .then(r => r.json())
    .then(data => {
        const res = data.d || data;
        const ddl = document.getElementById('ddlCourse');
        ddl.innerHTML = '<option value="">Select course...</option>';
        if (res.success && res.courses) {
            res.courses.forEach(c => {
                const opt = document.createElement('option');
                opt.value = c.cid;
                opt.textContent = c.name;
                ddl.appendChild(opt);
            });
        }
    })
    .catch(console.error);
}

let existingWorksDt = null;

function loadExisting() {
    fetch('Assignments.aspx/GetCourseWorks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: '{}',
        credentials: 'same-origin'
    })
    .then(r => r.json())
    .then(data => {
        const res = data.d || data;
        const box = document.getElementById('existingList');
        if (!box) return;
        if (!res.success) {
            box.innerHTML = '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';
            return;
        }
        const items = res.items || [];
        if (typeof EduDataTable === 'undefined') {
            box.innerHTML = items.length ? '' : '<div class="text-muted small">No courseworks yet.</div>';
            items.forEach(function (item) {
                box.innerHTML += '<div class="existing-item">' + escapeHtml(item.title) + '</div>';
            });
            return;
        }
        if (!existingWorksDt) {
            existingWorksDt = EduDataTable.create({
                container: box,
                pageSize: 8,
                pageSizeOptions: [5, 8, 15, 25],
                searchPlaceholder: 'Search title or course...',
                emptyMessage: 'No courseworks yet.',
                tableClass: 'table table-sm table-hover mb-0 edt-table',
                columns: [
                {
                    key: 'title', title: 'Title', sortable: true,
                    render: function (item) {
                        return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';
                    }
                },
                { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },
                { key: 'type', title: 'Type', sortable: true, filter: true, filterLabel: 'Type' },
                {
                    key: 'dueDate', title: 'Due', sortable: true,
                    render: function (item) {
                        if (!item.dueDate) return '<span class="text-muted small">—</span>';
                        var closed = isDueClosed(item.dueDate);
                        var badge = closed
                            ? '<span class="badge rounded-pill text-bg-secondary ms-1">Closed</span>'
                            : '<span class="badge rounded-pill text-bg-success ms-1">Open</span>';
                        return '<span class="small">' + escapeHtml(item.dueDate) + '</span>' + badge;
                    }
                },
                {
                    key: 'score', title: 'Pts', sortable: true, type: 'number',
                    render: function () { return '100'; }
                },
                {
                    key: '_actions', title: '', sortable: false, search: false, cellClass: 'text-end',
                    render: function (item) {
                        return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +
                        item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';
                    }
                }
                ]
            });
        }
        existingWorksDt.setData(items);
    })
    .catch(console.error);
}

function addRubricRow(name, pts) {
    // New empty rows get 0; user redistributes to keep total 100
    rubricRows.push({ name: name || '', pts: pts != null ? pts : 0 });
    renderRubric();
}

function getRubricTotal() {
    return rubricRows.reduce(function (s, r) { return s + (Number(r.pts) || 0); }, 0);
}

function removeRubricRow(i) {
    rubricRows.splice(i, 1);
    renderRubric();
}

function renderRubric() {
    const list = document.getElementById('rubricList');
    list.innerHTML = '';
    rubricRows.forEach((row, i) => {
        const div = document.createElement('div');
        div.className = 'd-flex align-items-center gap-2 mb-2';
        div.innerHTML = `
        <i class="fa-solid fa-grip-vertical text-muted"></i>
        <input type="text" class="form-control form-control-sm" placeholder="Criterion" value="${escapeAttr(row.name)}"
        oninput="rubricRows[${i}].name=this.value" />
        <input type="number" class="form-control form-control-sm" style="max-width:80px;" min="0" max="100" value="${row.pts}"
        oninput="rubricRows[${i}].pts=parseFloat(this.value)||0; updateRubricTotal();" />
        <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeRubricRow(${i})">
        <i class="fa-regular fa-trash-can"></i>
        </button>`;
        list.appendChild(div);
    });
    updateRubricTotal();
}

function updateRubricTotal() {
    const total = getRubricTotal();
    const el = document.getElementById('lblRubricTotal');
    // Always show "out of 100"
    el.innerText = total + ' / ' + ASSIGNMENT_TOTAL_PTS;
    if (total === ASSIGNMENT_TOTAL_PTS) {
        el.classList.remove('text-danger');
        el.classList.add('text-success');
    } else {
        el.classList.remove('text-success');
        el.classList.add('text-danger');
    }
    const hint = document.getElementById('rubricTotalHint');
    if (hint) {
        hint.style.display = total === ASSIGNMENT_TOTAL_PTS ? 'none' : 'block';
        hint.textContent = 'Rubric criteria must total exactly ' + ASSIGNMENT_TOTAL_PTS + ' pts (currently ' + total + ').';
    }
}

function addObjectiveQuestion() {
    objectiveQuestions.push({
        question: '',
        options: { option1: '', option2: '', option3: '', option4: '' },
        answer: 'option1',
        explanation: '',
        oneOrMultipleAnswer: true
    });
    renderQuestions();
}

function removeObjectiveQuestion(i) {
    objectiveQuestions.splice(i, 1);
    renderQuestions();
}

function addOption(qi) {
    const opts = objectiveQuestions[qi].options;
    const keys = Object.keys(opts);
    const next = 'option' + (keys.length + 1);
    opts[next] = '';
    renderQuestions();
}

function removeOption(qi, key) {
    delete objectiveQuestions[qi].options[key];
    renderQuestions();
}

function renderQuestions() {
    const list = document.getElementById('questionsList');
    list.innerHTML = '';
    objectiveQuestions.forEach((q, qi) => {
        const card = document.createElement('div');
        card.className = 'glass-card p-4 mb-3';
        let optionsHtml = '';
        Object.keys(q.options).forEach(key => {
            optionsHtml += `
            <div class="d-flex align-items-center gap-2 mb-2">
            <input type="radio" name="ans_${qi}" ${q.answer === key ? 'checked' : ''}
            onchange="objectiveQuestions[${qi}].answer='${key}'" />
            <input type="text" class="form-control form-control-sm" placeholder="Option"
            value="${escapeAttr(q.options[key])}"
            oninput="objectiveQuestions[${qi}].options['${key}']=this.value" />
            <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeOption(${qi},'${key}')">
            <i class="fa-regular fa-trash-can"></i>
            </button>
            </div>`;
        });
        card.innerHTML = `
        <div class="d-flex justify-content-between align-items-center mb-3">
        <span class="fw-bold"><i class="fa-solid fa-grip-vertical text-muted me-2"></i>Question ${qi + 1}</span>
        <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeObjectiveQuestion(${qi})">
        <i class="fa-regular fa-trash-can"></i>
        </button>
        </div>
        <input type="text" class="form-control mb-3" placeholder="Question text"
        value="${escapeAttr(q.question)}"
        oninput="objectiveQuestions[${qi}].question=this.value" />
        ${optionsHtml}
        <button type="button" class="btn btn-link btn-sm p-0 mb-3" style="color:var(--primary-accent);" onclick="addOption(${qi})">+ Add Option</button>
        <div class="mb-2">
        <label class="form-label small text-muted mb-1">Answer key (option id)</label>
        <input type="text" class="form-control form-control-sm" value="${escapeAttr(q.answer)}"
        oninput="objectiveQuestions[${qi}].answer=this.value" placeholder="e.g. option1" />
        </div>
        <div>
        <label class="form-label small text-muted mb-1">Explanation</label>
        <textarea class="form-control form-control-sm" rows="2"
        oninput="objectiveQuestions[${qi}].explanation=this.value">${escapeHtml(q.explanation || '')}</textarea>
        </div>`;
        list.appendChild(card);
    });
}

/** Due date (yyyy-MM-dd) is open all that calendar day; closed from next midnight. */
function isDueClosed(dueDateStr) {
    if (!dueDateStr) return false;
    var m = String(dueDateStr).match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (!m) return false;
    var end = new Date(parseInt(m[1], 10), parseInt(m[2], 10) - 1, parseInt(m[3], 10) + 1, 0, 0, 0, 0);
    return Date.now() >= end.getTime();
}

function saveAssignment(publish) {
    const err = document.getElementById('saveError');
    const ok = document.getElementById('saveOk');
    err.style.display = 'none';
    ok.style.display = 'none';

    const title = document.getElementById('txtTitle').value.trim();
    const instructions = document.getElementById('txtInstructions').value.trim();
    const cid = parseInt(document.getElementById('ddlCourse').value, 10) || 0;
    const cwidRaw = document.getElementById('hfCwid').value;
    const cwid = cwidRaw ? parseInt(cwidRaw, 10) : null;
    const dueDate = (document.getElementById('txtDueDate').value || '').trim();

    if (!title) { err.innerText = 'Title is required.'; err.style.display = 'block'; return; }
    if (!cid) { err.innerText = 'Select a target course.'; err.style.display = 'block'; return; }
    // Due date required when publishing so closing is explicit in demos
    if (publish && !dueDate) {
        err.innerText = 'Set a due date before publishing (students cannot submit after that day).';
        err.style.display = 'block';
        return;
    }

    // All assignments / quizzes are always out of 100 pts
    let score = ASSIGNMENT_TOTAL_PTS;
    let rubricJson = null;
    let objectiveQuestionsJson = null;

    if (builderType === 'Text') {
        const rubricSum = getRubricTotal();
        if (rubricSum !== ASSIGNMENT_TOTAL_PTS) {
            err.innerText = 'Grading rubric must total exactly ' + ASSIGNMENT_TOTAL_PTS +
            ' pts (currently ' + rubricSum + '). Adjust the criterion points.';
            err.style.display = 'block';
            return;
        }
        rubricJson = JSON.stringify(rubricRows);
        score = ASSIGNMENT_TOTAL_PTS;
    } else {
        if (objectiveQuestions.length === 0) {
            err.innerText = 'Add at least one quiz question.';
            err.style.display = 'block';
            return;
        }
        // Evenly distribute 100 pts across questions (for display in meta)
        const perQ = Math.round((ASSIGNMENT_TOTAL_PTS / objectiveQuestions.length) * 100) / 100;
        objectiveQuestions = objectiveQuestions.map(function (q) {
            q.points = perQ;
            return q;
        });
        objectiveQuestionsJson = JSON.stringify(objectiveQuestions);
        score = ASSIGNMENT_TOTAL_PTS;
    }

    const extra = {
        dueDate: dueDate || null,
        timeLimit: document.getElementById('txtTimeLimit').value || null,
        requireFile: document.getElementById('chkRequireFile').checked,
        published: !!publish
    };

    fetch('Assignments.aspx/SaveCourseWork', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            cwid: cwid,
            cid: cid,
            title: title,
            instructions: instructions,
            type: builderType,
            score: score,
            creditGiven: score,
            rubricJson: rubricJson,
            extraMetaJson: JSON.stringify(extra),
            objectiveQuestionsJson: objectiveQuestionsJson
        })
    })
    .then(r => r.json())
    .then(data => {
        const res = data.d || data;
        if (res.success) {
            document.getElementById('hfCwid').value = res.cwid;
            ok.innerText = publish ? 'Published successfully.' : 'Draft saved.';
            ok.style.display = 'block';
            loadExisting();
        } else {
            err.innerText = res.message || 'Save failed.';
            err.style.display = 'block';
        }
    })
    .catch(e => {
        err.innerText = 'Network error.';
        err.style.display = 'block';
        console.error(e);
    });
}

function deleteWork(cwid) {
    if (!confirm('Delete this coursework? This cannot be undone.')) return;
    fetch('Assignments.aspx/DeleteCourseWork', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cwid: cwid })
    })
    .then(r => r.json())
    .then(data => {
        const res = data.d || data;
        if (res.success) loadExisting();
        else alert(res.message || 'Delete failed');
    })
    .catch(console.error);
}

function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function escapeAttr(str) {
    return escapeHtml(str).replace(/'/g, '&#39;');
}

```
