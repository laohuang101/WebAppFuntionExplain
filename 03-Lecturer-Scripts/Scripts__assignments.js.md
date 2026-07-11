# assignments.js
**Source:** `Pages/Lecturer/Scripts/assignments.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 387
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 2:** `builderType` — script-level `const`/`let`/`var`
- **Line 4:** `rubricRows` — script-level `const`/`let`/`var`
- **Line 5:** `objectiveQuestions` — script-level `const`/`let`/`var`
- **Line 6:** `ASSIGNMENT_TOTAL_PTS` — script-level `const`/`let`/`var`
- **Line 43:** `res` — script-level `const`/`let`/`var`
- **Line 44:** `ddl` — script-level `const`/`let`/`var`
- **Line 48:** `opt` — script-level `const`/`let`/`var`
- **Line 57:** `existingWorksDt` — script-level `const`/`let`/`var`
- **Line 70:** `box` — script-level `const`/`let`/`var`
- **Line 76:** `items` — script-level `const`/`let`/`var`
- **Line 105:** `closed` — script-level `const`/`let`/`var`
- **Line 106:** `badge` — script-level `const`/`let`/`var`
- **Line 147:** `list` — script-level `const`/`let`/`var`
- **Line 150:** `div` — script-level `const`/`let`/`var`
- **Line 167:** `total` — script-level `const`/`let`/`var`
- **Line 168:** `el` — script-level `const`/`let`/`var`
- **Line 178:** `hint` — script-level `const`/`let`/`var`
- **Line 202:** `opts` — script-level `const`/`let`/`var`
- **Line 203:** `keys` — script-level `const`/`let`/`var`
- **Line 204:** `next` — script-level `const`/`let`/`var`
- **Line 218:** `card` — script-level `const`/`let`/`var`
- **Line 220:** `optionsHtml` — script-level `const`/`let`/`var`
- **Line 263:** `m` — script-level `const`/`let`/`var`
- **Line 265:** `end` — script-level `const`/`let`/`var`
- **Line 270:** `err` — script-level `const`/`let`/`var`
- **Line 271:** `ok` — script-level `const`/`let`/`var`
- **Line 274:** `title` — script-level `const`/`let`/`var`
- **Line 276:** `instructions` — script-level `const`/`let`/`var`
- **Line 277:** `cid` — script-level `const`/`let`/`var`
- **Line 278:** `cwidRaw` — script-level `const`/`let`/`var`
- **Line 279:** `cwid` — script-level `const`/`let`/`var`
- **Line 280:** `dueDate` — script-level `const`/`let`/`var`
- **Line 292:** `score` — script-level `const`/`let`/`var`
- **Line 293:** `rubricJson` — script-level `const`/`let`/`var`
- **Line 294:** `objectiveQuestionsJson` — script-level `const`/`let`/`var`
- **Line 297:** `rubricSum` — script-level `const`/`let`/`var`
- **Line 313:** `perQ` — script-level `const`/`let`/`var`
- **Line 321:** `extra` — script-level `const`/`let`/`var`

## Functions / methods (22 found)

### `setBuilderType` — lines 19–33

```
function setBuilderType(type)
```

#### Explanation

- **Purpose:** Implements `setBuilderType`.
- **Pattern:** Persist changes.
- **Parameters:** `type`

#### Line-by-line (this function)

`  19`  ``
`  20`  ``
`  21`  `function setBuilderType(type) {`
`  22`  `    builderType = type === 'Objective' ? 'Objective' : 'Text';`
`  23`  `    document.getElementById('btnTypeAssignment').classList.toggle('active', builderType === 'Text');`
  - → Get HTML element by id.
`  24`  `    document.getElementById('btnTypeQuiz').classList.toggle('active', builderType === 'Objective');`
  - → Get HTML element by id.
`  25`  `    document.getElementById('panelRubric').style.display = builderType === 'Text' ? 'block' : 'none';`
  - → Get HTML element by id.
`  26`  `    document.getElementById('panelQuestions').style.display = builderType === 'Objective' ? 'block' : 'none';`
  - → Get HTML element by id.
`  27`  `    document.getElementById('timeLimitGroup').style.display = builderType === 'Objective' ? 'block' : 'none';`
  - → Get HTML element by id.
`  28`  `    document.getElementById('requireFileGroup').style.display = builderType === 'Text' ? 'block' : 'none';`
  - → Get HTML element by id.
`  29`  ``
`  30`  `    if (builderType === 'Objective' && objectiveQuestions.length === 0) {`
`  31`  `        addObjectiveQuestion();`
`  32`  `    }`
`  33`  `}`

---

### `loadCourses` — lines 33–56

```
function loadCourses()
```

#### Explanation

- **Purpose:** Implements `loadCourses`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables:** `res`, `ddl`, `opt`

#### Line-by-line (this function)

`  33`  ``
`  34`  ``
`  35`  `function loadCourses() {`
`  36`  `    fetch('Assignments.aspx/GetCourses', {`
  - → HTTP request to server WebMethod/ashx.
`  37`  `        method: 'POST',`
`  38`  `        headers: { 'Content-Type': 'application/json' },`
`  39`  `        body: '{}'`
`  40`  `    })`
`  41`  `    .then(r => r.json())`
`  42`  `    .then(data => {`
`  43`  `        const res = data.d || data;`
`  44`  `        const ddl = document.getElementById('ddlCourse');`
  - → Get HTML element by id.
`  45`  `        ddl.innerHTML = '<option value="">Select course...</option>';`
  - → Update page HTML.
`  46`  `        if (res.success && res.courses) {`
`  47`  `            res.courses.forEach(c => {`
`  48`  `                const opt = document.createElement('option');`
`  49`  `                opt.value = c.cid;`
`  50`  `                opt.textContent = c.name;`
`  51`  `                ddl.appendChild(opt);`
`  52`  `            });`
`  53`  `        }`
`  54`  `    })`
`  55`  `    .catch(console.error);`
`  56`  `}`

---

### `loadExisting` — lines 58–129

```
function loadExisting()
```

#### Explanation

- **Purpose:** Implements `loadExisting`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Read/load data for display.
- **Local variables:** `res`, `box`, `items`, `closed`, `badge`

#### Line-by-line (this function)

`  58`  ``
`  59`  ``
`  60`  `function loadExisting() {`
`  61`  `    fetch('Assignments.aspx/GetCourseWorks', {`
  - → HTTP request to server WebMethod/ashx.
`  62`  `        method: 'POST',`
`  63`  `        headers: { 'Content-Type': 'application/json' },`
`  64`  `        body: '{}',`
`  65`  `        credentials: 'same-origin'`
`  66`  `    })`
`  67`  `    .then(r => r.json())`
`  68`  `    .then(data => {`
`  69`  `        const res = data.d || data;`
`  70`  `        const box = document.getElementById('existingList');`
  - → Get HTML element by id.
`  71`  `        if (!box) return;`
`  72`  `        if (!res.success) {`
`  73`  `            box.innerHTML = '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';`
  - → Update page HTML.
`  74`  `            return;`
`  75`  `        }`
`  76`  `        const items = res.items || [];`
`  77`  `        if (typeof EduDataTable === 'undefined') {`
`  78`  `            box.innerHTML = items.length ? '' : '<div class="text-muted small">No courseworks yet.</div>';`
  - → Update page HTML.
`  79`  `            items.forEach(function (item) {`
`  80`  `                box.innerHTML += '<div class="existing-item">' + escapeHtml(item.title) + '</div>';`
  - → Update page HTML.
`  81`  `            });`
`  82`  `            return;`
`  83`  `        }`
`  84`  `        if (!existingWorksDt) {`
`  85`  `            existingWorksDt = EduDataTable.create({`
`  86`  `                container: box,`
`  87`  `                pageSize: 8,`
`  88`  `                pageSizeOptions: [5, 8, 15, 25],`
`  89`  `                searchPlaceholder: 'Search title or course...',`
`  90`  `                emptyMessage: 'No courseworks yet.',`
`  91`  `                tableClass: 'table table-sm table-hover mb-0 edt-table',`
`  92`  `                columns: [`
`  93`  `                {`
`  94`  `                    key: 'title', title: 'Title', sortable: true,`
`  95`  `                    render: function (item) {`
`  96`  `                        return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';`
  - → Encode text to reduce XSS risk.
`  97`  `                    }`
`  98`  `                },`
`  99`  `                { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },`
` 100`  `                { key: 'type', title: 'Type', sortable: true, filter: true, filterLabel: 'Type' },`
` 101`  `                {`
` 102`  `                    key: 'dueDate', title: 'Due', sortable: true,`
  - → Assignment deadline; submissions close after due day.
` 103`  `                    render: function (item) {`
` 104`  `                        if (!item.dueDate) return '<span class="text-muted small">—</span>';`
  - → Assignment deadline; submissions close after due day.
` 105`  `                        var closed = isDueClosed(item.dueDate);`
  - → Assignment deadline; submissions close after due day.
` 106`  `                        var badge = closed`
` 107`  `                            ? '<span class="badge rounded-pill text-bg-secondary ms-1">Closed</span>'`
` 108`  `                            : '<span class="badge rounded-pill text-bg-success ms-1">Open</span>';`
` 109`  `                        return '<span class="small">' + escapeHtml(item.dueDate) + '</span>' + badge;`
  - → Assignment deadline; submissions close after due day.
` 110`  `                    }`
` 111`  `                },`
` 112`  `                {`
` 113`  `                    key: 'score', title: 'Pts', sortable: true, type: 'number',`
` 114`  `                    render: function () { return '100'; }`
` 115`  `                },`
` 116`  `                {`
` 117`  `                    key: '_actions', title: '', sortable: false, search: false, cellClass: 'text-end',`
` 118`  `                    render: function (item) {`
` 119`  `                        return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +`
` 120`  `                        item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';`
` 121`  `                    }`
` 122`  `                }`
` 123`  `                ]`
` 124`  `            });`
` 125`  `        }`
` 126`  `        existingWorksDt.setData(items);`
` 127`  `    })`
` 128`  `    .catch(console.error);`
` 129`  `}`

---

### `render` — lines 95–97

```
function render(item)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters:** `item`

#### Line-by-line (this function)

`  95`  `                    render: function (item) {`
`  96`  `                        return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';`
  - → Encode text to reduce XSS risk.
`  97`  `                    }`

---

### `render` — lines 103–110

```
function render(item)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Due date:** Related to assignment closing after the due day.
- **Parameters:** `item`
- **Local variables:** `closed`, `badge`

#### Line-by-line (this function)

` 103`  `                    render: function (item) {`
` 104`  `                        if (!item.dueDate) return '<span class="text-muted small">—</span>';`
  - → Assignment deadline; submissions close after due day.
` 105`  `                        var closed = isDueClosed(item.dueDate);`
  - → Assignment deadline; submissions close after due day.
` 106`  `                        var badge = closed`
` 107`  `                            ? '<span class="badge rounded-pill text-bg-secondary ms-1">Closed</span>'`
` 108`  `                            : '<span class="badge rounded-pill text-bg-success ms-1">Open</span>';`
` 109`  `                        return '<span class="small">' + escapeHtml(item.dueDate) + '</span>' + badge;`
  - → Assignment deadline; submissions close after due day.
` 110`  `                    }`

---

### `render` — lines 114–114

```
function render()
```

#### Explanation

- **Purpose:** Implements `render`.

#### Line-by-line (this function)

` 114`  `                    render: function () { return '100'; }`

---

### `render` — lines 118–121

```
function render(item)
```

#### Explanation

- **Purpose:** Implements `render`.
- **Parameters:** `item`

#### Line-by-line (this function)

` 118`  `                    render: function (item) {`
` 119`  `                        return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +`
` 120`  `                        item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';`
` 121`  `                    }`

---

### `addRubricRow` — lines 129–135

```
function addRubricRow(name, pts)
```

#### Explanation

- **Purpose:** Implements `addRubricRow`.
- **Parameters:** `name, pts`

#### Line-by-line (this function)

` 129`  ``
` 130`  ``
` 131`  `function addRubricRow(name, pts) {`
` 132`  `    // New empty rows get 0; user redistributes to keep total 100`
` 133`  `    rubricRows.push({ name: name || '', pts: pts != null ? pts : 0 });`
` 134`  `    renderRubric();`
` 135`  `}`

---

### `getRubricTotal` — lines 135–139

```
function getRubricTotal()
```

#### Explanation

- **Purpose:** Implements `getRubricTotal`.
- **Pattern:** Read/load data for display.

#### Line-by-line (this function)

` 135`  ``
` 136`  ``
` 137`  `function getRubricTotal() {`
` 138`  `    return rubricRows.reduce(function (s, r) { return s + (Number(r.pts) || 0); }, 0);`
` 139`  `}`

---

### `removeRubricRow` — lines 139–144

```
function removeRubricRow(i)
```

#### Explanation

- **Purpose:** Implements `removeRubricRow`.
- **Pattern:** Delete/clear data.
- **Parameters:** `i`

#### Line-by-line (this function)

` 139`  ``
` 140`  ``
` 141`  `function removeRubricRow(i) {`
` 142`  `    rubricRows.splice(i, 1);`
` 143`  `    renderRubric();`
` 144`  `}`

---

### `renderRubric` — lines 144–164

```
function renderRubric()
```

#### Explanation

- **Purpose:** Implements `renderRubric`.
- **Local variables:** `list`, `div`

#### Line-by-line (this function)

` 144`  ``
` 145`  ``
` 146`  `function renderRubric() {`
` 147`  `    const list = document.getElementById('rubricList');`
  - → Get HTML element by id.
` 148`  `    list.innerHTML = '';`
  - → Update page HTML.
` 149`  `    rubricRows.forEach((row, i) => {`
` 150`  `        const div = document.createElement('div');`
` 151`  `        div.className = 'd-flex align-items-center gap-2 mb-2';`
` 152`  `        div.innerHTML = ``
  - → Update page HTML.
` 153`  `        <i class="fa-solid fa-grip-vertical text-muted"></i>`
` 154`  `        <input type="text" class="form-control form-control-sm" placeholder="Criterion" value="${escapeAttr(row.name)}"`
` 155`  `        oninput="rubricRows[${i}].name=this.value" />`
` 156`  `        <input type="number" class="form-control form-control-sm" style="max-width:80px;" min="0" max="100" value="${row.pts}"`
` 157`  `        oninput="rubricRows[${i}].pts=parseFloat(this.value)||0; updateRubricTotal();" />`
` 158`  `        <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeRubricRow(${i})">`
` 159`  `        <i class="fa-regular fa-trash-can"></i>`
` 160`  `        </button>`;`
` 161`  `        list.appendChild(div);`
` 162`  `    });`
` 163`  `    updateRubricTotal();`
` 164`  `}`

---

### `updateRubricTotal` — lines 164–183

```
function updateRubricTotal()
```

#### Explanation

- **Purpose:** Implements `updateRubricTotal`.
- **Pattern:** Persist changes.
- **Local variables:** `total`, `el`, `hint`

#### Line-by-line (this function)

` 164`  ``
` 165`  ``
` 166`  `function updateRubricTotal() {`
` 167`  `    const total = getRubricTotal();`
` 168`  `    const el = document.getElementById('lblRubricTotal');`
  - → Get HTML element by id.
` 169`  `    // Always show "out of 100"`
` 170`  `    el.innerText = total + ' / ' + ASSIGNMENT_TOTAL_PTS;`
` 171`  `    if (total === ASSIGNMENT_TOTAL_PTS) {`
` 172`  `        el.classList.remove('text-danger');`
` 173`  `        el.classList.add('text-success');`
` 174`  `    } else {`
` 175`  `        el.classList.remove('text-success');`
` 176`  `        el.classList.add('text-danger');`
` 177`  `    }`
` 178`  `    const hint = document.getElementById('rubricTotalHint');`
  - → Get HTML element by id.
` 179`  `    if (hint) {`
` 180`  `        hint.style.display = total === ASSIGNMENT_TOTAL_PTS ? 'none' : 'block';`
` 181`  `        hint.textContent = 'Rubric criteria must total exactly ' + ASSIGNMENT_TOTAL_PTS + ' pts (currently ' + total + ').';`
` 182`  `    }`
` 183`  `}`

---

### `addObjectiveQuestion` — lines 183–194

```
function addObjectiveQuestion()
```

#### Explanation

- **Purpose:** Implements `addObjectiveQuestion`.

#### Line-by-line (this function)

` 183`  ``
` 184`  ``
` 185`  `function addObjectiveQuestion() {`
` 186`  `    objectiveQuestions.push({`
` 187`  `        question: '',`
` 188`  `        options: { option1: '', option2: '', option3: '', option4: '' },`
` 189`  `        answer: 'option1',`
` 190`  `        explanation: '',`
` 191`  `        oneOrMultipleAnswer: true`
` 192`  `    });`
` 193`  `    renderQuestions();`
` 194`  `}`

---

### `removeObjectiveQuestion` — lines 194–199

```
function removeObjectiveQuestion(i)
```

#### Explanation

- **Purpose:** Implements `removeObjectiveQuestion`.
- **Pattern:** Delete/clear data.
- **Parameters:** `i`

#### Line-by-line (this function)

` 194`  ``
` 195`  ``
` 196`  `function removeObjectiveQuestion(i) {`
` 197`  `    objectiveQuestions.splice(i, 1);`
` 198`  `    renderQuestions();`
` 199`  `}`

---

### `addOption` — lines 199–207

```
function addOption(qi)
```

#### Explanation

- **Purpose:** Implements `addOption`.
- **Parameters:** `qi`
- **Local variables:** `opts`, `keys`, `next`

#### Line-by-line (this function)

` 199`  ``
` 200`  ``
` 201`  `function addOption(qi) {`
` 202`  `    const opts = objectiveQuestions[qi].options;`
` 203`  `    const keys = Object.keys(opts);`
` 204`  `    const next = 'option' + (keys.length + 1);`
` 205`  `    opts[next] = '';`
` 206`  `    renderQuestions();`
` 207`  `}`

---

### `removeOption` — lines 207–212

```
function removeOption(qi, key)
```

#### Explanation

- **Purpose:** Implements `removeOption`.
- **Pattern:** Delete/clear data.
- **Parameters:** `qi, key`

#### Line-by-line (this function)

` 207`  ``
` 208`  ``
` 209`  `function removeOption(qi, key) {`
` 210`  `    delete objectiveQuestions[qi].options[key];`
` 211`  `    renderQuestions();`
` 212`  `}`

---

### `renderQuestions` — lines 212–258

```
function renderQuestions()
```

#### Explanation

- **Purpose:** Implements `renderQuestions`.
- **Local variables:** `list`, `card`, `optionsHtml`

#### Line-by-line (this function)

` 212`  ``
` 213`  ``
` 214`  `function renderQuestions() {`
` 215`  `    const list = document.getElementById('questionsList');`
  - → Get HTML element by id.
` 216`  `    list.innerHTML = '';`
  - → Update page HTML.
` 217`  `    objectiveQuestions.forEach((q, qi) => {`
` 218`  `        const card = document.createElement('div');`
` 219`  `        card.className = 'glass-card p-4 mb-3';`
` 220`  `        let optionsHtml = '';`
` 221`  `        Object.keys(q.options).forEach(key => {`
` 222`  `            optionsHtml += ``
` 223`  `            <div class="d-flex align-items-center gap-2 mb-2">`
` 224`  `            <input type="radio" name="ans_${qi}" ${q.answer === key ? 'checked' : ''}`
` 225`  `            onchange="objectiveQuestions[${qi}].answer='${key}'" />`
` 226`  `            <input type="text" class="form-control form-control-sm" placeholder="Option"`
` 227`  `            value="${escapeAttr(q.options[key])}"`
` 228`  `            oninput="objectiveQuestions[${qi}].options['${key}']=this.value" />`
` 229`  `            <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeOption(${qi},'${key}')">`
` 230`  `            <i class="fa-regular fa-trash-can"></i>`
` 231`  `            </button>`
` 232`  `            </div>`;`
` 233`  `        });`
` 234`  `        card.innerHTML = ``
  - → Update page HTML.
` 235`  `        <div class="d-flex justify-content-between align-items-center mb-3">`
` 236`  `        <span class="fw-bold"><i class="fa-solid fa-grip-vertical text-muted me-2"></i>Question ${qi + 1}</span>`
` 237`  `        <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeObjectiveQuestion(${qi})">`
` 238`  `        <i class="fa-regular fa-trash-can"></i>`
` 239`  `        </button>`
` 240`  `        </div>`
` 241`  `        <input type="text" class="form-control mb-3" placeholder="Question text"`
` 242`  `        value="${escapeAttr(q.question)}"`
` 243`  `        oninput="objectiveQuestions[${qi}].question=this.value" />`
` 244`  `        ${optionsHtml}`
` 245`  `        <button type="button" class="btn btn-link btn-sm p-0 mb-3" style="color:var(--primary-accent);" onclick="addOption(${qi})">+ Add Option</button>`
` 246`  `        <div class="mb-2">`
` 247`  `        <label class="form-label small text-muted mb-1">Answer key (option id)</label>`
` 248`  `        <input type="text" class="form-control form-control-sm" value="${escapeAttr(q.answer)}"`
` 249`  `        oninput="objectiveQuestions[${qi}].answer=this.value" placeholder="e.g. option1" />`
` 250`  `        </div>`
` 251`  `        <div>`
` 252`  `        <label class="form-label small text-muted mb-1">Explanation</label>`
` 253`  `        <textarea class="form-control form-control-sm" rows="2"`
` 254`  `        oninput="objectiveQuestions[${qi}].explanation=this.value">${escapeHtml(q.explanation || '')}</textarea>`
  - → Encode text to reduce XSS risk.
` 255`  `        </div>`;`
` 256`  `        list.appendChild(card);`
` 257`  `    });`
` 258`  `}`

---

### `isDueClosed` — lines 260–267

```
function isDueClosed(dueDateStr)
```

#### Explanation

- **Purpose:** Implements `isDueClosed`.
- **Due date:** Related to assignment closing after the due day.
- **Parameters:** `dueDateStr`
- **Local variables:** `m`, `end`

#### Line-by-line (this function)

` 260`  ``
` 261`  `function isDueClosed(dueDateStr) {`
  - → Assignment deadline; submissions close after due day.
` 262`  `    if (!dueDateStr) return false;`
  - → Assignment deadline; submissions close after due day.
` 263`  `    var m = String(dueDateStr).match(/^(\d{4})-(\d{2})-(\d{2})/);`
  - → Assignment deadline; submissions close after due day.
` 264`  `    if (!m) return false;`
` 265`  `    var end = new Date(parseInt(m[1], 10), parseInt(m[2], 10) - 1, parseInt(m[3], 10) + 1, 0, 0, 0, 0);`
` 266`  `    return Date.now() >= end.getTime();`
` 267`  `}`

---

### `saveAssignment` — lines 267–363

```
function saveAssignment(publish)
```

#### Explanation

- **Purpose:** Implements `saveAssignment`.
- **Due date:** Related to assignment closing after the due day.
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Persist changes.
- **Parameters:** `publish`
- **Local variables:** `err`, `ok`, `title`, `instructions`, `cid`, `cwidRaw`, `cwid`, `dueDate`, `score`, `rubricJson`, `objectiveQuestionsJson`, `rubricSum`, `perQ`, `extra`, `res`

#### Line-by-line (this function)

` 267`  ``
` 268`  ``
` 269`  `function saveAssignment(publish) {`
` 270`  `    const err = document.getElementById('saveError');`
  - → Get HTML element by id.
` 271`  `    const ok = document.getElementById('saveOk');`
  - → Get HTML element by id.
` 272`  `    err.style.display = 'none';`
` 273`  `    ok.style.display = 'none';`
` 274`  ``
` 275`  `    const title = document.getElementById('txtTitle').value.trim();`
  - → Get HTML element by id.
` 276`  `    const instructions = document.getElementById('txtInstructions').value.trim();`
  - → Get HTML element by id.
` 277`  `    const cid = parseInt(document.getElementById('ddlCourse').value, 10) || 0;`
  - → Get HTML element by id.
` 278`  `    const cwidRaw = document.getElementById('hfCwid').value;`
  - → Get HTML element by id.
` 279`  `    const cwid = cwidRaw ? parseInt(cwidRaw, 10) : null;`
` 280`  `    const dueDate = (document.getElementById('txtDueDate').value || '').trim();`
  - → Assignment deadline; submissions close after due day.
` 281`  ``
` 282`  `    if (!title) { err.innerText = 'Title is required.'; err.style.display = 'block'; return; }`
` 283`  `    if (!cid) { err.innerText = 'Select a target course.'; err.style.display = 'block'; return; }`
` 284`  `    // Due date required when publishing so closing is explicit in demos`
` 285`  `    if (publish && !dueDate) {`
  - → Assignment deadline; submissions close after due day.
` 286`  `        err.innerText = 'Set a due date before publishing (students cannot submit after that day).';`
` 287`  `        err.style.display = 'block';`
` 288`  `        return;`
` 289`  `    }`
` 290`  ``
` 291`  `    // All assignments / quizzes are always out of 100 pts`
` 292`  `    let score = ASSIGNMENT_TOTAL_PTS;`
` 293`  `    let rubricJson = null;`
` 294`  `    let objectiveQuestionsJson = null;`
` 295`  ``
` 296`  `    if (builderType === 'Text') {`
` 297`  `        const rubricSum = getRubricTotal();`
` 298`  `        if (rubricSum !== ASSIGNMENT_TOTAL_PTS) {`
` 299`  `            err.innerText = 'Grading rubric must total exactly ' + ASSIGNMENT_TOTAL_PTS +`
` 300`  `            ' pts (currently ' + rubricSum + '). Adjust the criterion points.';`
` 301`  `            err.style.display = 'block';`
` 302`  `            return;`
` 303`  `        }`
` 304`  `        rubricJson = JSON.stringify(rubricRows);`
  - → JS object ↔ JSON text.
` 305`  `        score = ASSIGNMENT_TOTAL_PTS;`
` 306`  `    } else {`
` 307`  `        if (objectiveQuestions.length === 0) {`
` 308`  `            err.innerText = 'Add at least one quiz question.';`
` 309`  `            err.style.display = 'block';`
` 310`  `            return;`
` 311`  `        }`
` 312`  `        // Evenly distribute 100 pts across questions (for display in meta)`
` 313`  `        const perQ = Math.round((ASSIGNMENT_TOTAL_PTS / objectiveQuestions.length) * 100) / 100;`
` 314`  `        objectiveQuestions = objectiveQuestions.map(function (q) {`
` 315`  `            q.points = perQ;`
` 316`  `            return q;`
` 317`  `        });`
` 318`  `        objectiveQuestionsJson = JSON.stringify(objectiveQuestions);`
  - → JS object ↔ JSON text.
` 319`  `        score = ASSIGNMENT_TOTAL_PTS;`
` 320`  `    }`
` 321`  ``
` 322`  `    const extra = {`
` 323`  `        dueDate: dueDate || null,`
  - → Assignment deadline; submissions close after due day.
` 324`  `        timeLimit: document.getElementById('txtTimeLimit').value || null,`
  - → Get HTML element by id.
` 325`  `        requireFile: document.getElementById('chkRequireFile').checked,`
  - → Get HTML element by id.
` 326`  `        published: !!publish`
` 327`  `    };`
` 328`  ``
` 329`  `    fetch('Assignments.aspx/SaveCourseWork', {`
  - → HTTP request to server WebMethod/ashx.
` 330`  `        method: 'POST',`
` 331`  `        headers: { 'Content-Type': 'application/json' },`
` 332`  `        body: JSON.stringify({`
  - → JS object ↔ JSON text.
` 333`  `            cwid: cwid,`
` 334`  `            cid: cid,`
` 335`  `            title: title,`
` 336`  `            instructions: instructions,`
` 337`  `            type: builderType,`
` 338`  `            score: score,`
` 339`  `            creditGiven: score,`
` 340`  `            rubricJson: rubricJson,`
` 341`  `            extraMetaJson: JSON.stringify(extra),`
  - → JS object ↔ JSON text.
` 342`  `            objectiveQuestionsJson: objectiveQuestionsJson`
` 343`  `        })`
` 344`  `    })`
` 345`  `    .then(r => r.json())`
` 346`  `    .then(data => {`
` 347`  `        const res = data.d || data;`
` 348`  `        if (res.success) {`
` 349`  `            document.getElementById('hfCwid').value = res.cwid;`
  - → Get HTML element by id.
` 350`  `            ok.innerText = publish ? 'Published successfully.' : 'Draft saved.';`
` 351`  `            ok.style.display = 'block';`
` 352`  `            loadExisting();`
` 353`  `        } else {`
` 354`  `            err.innerText = res.message || 'Save failed.';`
` 355`  `            err.style.display = 'block';`
` 356`  `        }`
` 357`  `    })`
` 358`  `    .catch(e => {`
` 359`  `        err.innerText = 'Network error.';`
` 360`  `        err.style.display = 'block';`
` 361`  `        console.error(e);`
` 362`  `    });`
` 363`  `}`

---

### `deleteWork` — lines 363–379

```
function deleteWork(cwid)
```

#### Explanation

- **Purpose:** Implements `deleteWork`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Pattern:** Delete/clear data.
- **Parameters:** `cwid`
- **Local variables:** `res`

#### Line-by-line (this function)

` 363`  ``
` 364`  ``
` 365`  `function deleteWork(cwid) {`
` 366`  `    if (!confirm('Delete this coursework? This cannot be undone.')) return;`
` 367`  `    fetch('Assignments.aspx/DeleteCourseWork', {`
  - → HTTP request to server WebMethod/ashx.
` 368`  `        method: 'POST',`
` 369`  `        headers: { 'Content-Type': 'application/json' },`
` 370`  `        body: JSON.stringify({ cwid: cwid })`
  - → JS object ↔ JSON text.
` 371`  `    })`
` 372`  `    .then(r => r.json())`
` 373`  `    .then(data => {`
` 374`  `        const res = data.d || data;`
` 375`  `        if (res.success) loadExisting();`
` 376`  `        else alert(res.message || 'Delete failed');`
` 377`  `    })`
` 378`  `    .catch(console.error);`
` 379`  `}`

---

### `escapeHtml` — lines 379–387

```
function escapeHtml(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtml`.
- **Parameters:** `str`

#### Line-by-line (this function)

` 379`  ``
` 380`  ``
` 381`  `function escapeHtml(str) {`
  - → Encode text to reduce XSS risk.
` 382`  `    if (!str) return '';`
` 383`  `    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');`
` 384`  `}`
` 385`  `function escapeAttr(str) {`
` 386`  `    return escapeHtml(str).replace(/'/g, '&#39;');`
  - → Encode text to reduce XSS risk.
` 387`  `}`

---

### `escapeAttr` — lines 384–387

```
function escapeAttr(str)
```

#### Explanation

- **Purpose:** Implements `escapeAttr`.
- **Parameters:** `str`

#### Line-by-line (this function)

` 384`  ``
` 385`  `function escapeAttr(str) {`
` 386`  `    return escapeHtml(str).replace(/'/g, '&#39;');`
  - → Encode text to reduce XSS risk.
` 387`  `}`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `/* Assignment Builder - pure-SQL CourseWorks / ObjectiveQuestions UI */`
`   2`  ``
`   3`  `let builderType = 'Text'; // Text | Objective`
`   4`  `let rubricRows = [];`
`   5`  `let objectiveQuestions = [];`
`   6`  ``
`   7`  `const ASSIGNMENT_TOTAL_PTS = 100;`
`   8`  ``
`   9`  `document.addEventListener('DOMContentLoaded', function () {`
  - → DOM event handler.
`  10`  `    loadCourses();`
`  11`  `    loadExisting();`
`  12`  `    setBuilderType('Text');`
`  13`  `    if (rubricRows.length === 0) {`
`  14`  `        // Defaults always sum to 100 pts`
`  15`  `        addRubricRow('Content & understanding', 40);`
`  16`  `        addRubricRow('Structure & clarity', 30);`
`  17`  `        addRubricRow('Presentation / quality', 30);`
`  18`  `    }`
`  19`  `});`
`  20`  ``
`  21`  `function setBuilderType(type) {`
`  22`  `    builderType = type === 'Objective' ? 'Objective' : 'Text';`
`  23`  `    document.getElementById('btnTypeAssignment').classList.toggle('active', builderType === 'Text');`
  - → Get HTML element by id.
`  24`  `    document.getElementById('btnTypeQuiz').classList.toggle('active', builderType === 'Objective');`
  - → Get HTML element by id.
`  25`  `    document.getElementById('panelRubric').style.display = builderType === 'Text' ? 'block' : 'none';`
  - → Get HTML element by id.
`  26`  `    document.getElementById('panelQuestions').style.display = builderType === 'Objective' ? 'block' : 'none';`
  - → Get HTML element by id.
`  27`  `    document.getElementById('timeLimitGroup').style.display = builderType === 'Objective' ? 'block' : 'none';`
  - → Get HTML element by id.
`  28`  `    document.getElementById('requireFileGroup').style.display = builderType === 'Text' ? 'block' : 'none';`
  - → Get HTML element by id.
`  29`  ``
`  30`  `    if (builderType === 'Objective' && objectiveQuestions.length === 0) {`
`  31`  `        addObjectiveQuestion();`
`  32`  `    }`
`  33`  `}`
`  34`  ``
`  35`  `function loadCourses() {`
`  36`  `    fetch('Assignments.aspx/GetCourses', {`
  - → HTTP request to server WebMethod/ashx.
`  37`  `        method: 'POST',`
`  38`  `        headers: { 'Content-Type': 'application/json' },`
`  39`  `        body: '{}'`
`  40`  `    })`
`  41`  `    .then(r => r.json())`
`  42`  `    .then(data => {`
`  43`  `        const res = data.d || data;`
`  44`  `        const ddl = document.getElementById('ddlCourse');`
  - → Get HTML element by id.
`  45`  `        ddl.innerHTML = '<option value="">Select course...</option>';`
  - → Update page HTML.
`  46`  `        if (res.success && res.courses) {`
`  47`  `            res.courses.forEach(c => {`
`  48`  `                const opt = document.createElement('option');`
`  49`  `                opt.value = c.cid;`
`  50`  `                opt.textContent = c.name;`
`  51`  `                ddl.appendChild(opt);`
`  52`  `            });`
`  53`  `        }`
`  54`  `    })`
`  55`  `    .catch(console.error);`
`  56`  `}`
`  57`  ``
`  58`  `let existingWorksDt = null;`
`  59`  ``
`  60`  `function loadExisting() {`
`  61`  `    fetch('Assignments.aspx/GetCourseWorks', {`
  - → HTTP request to server WebMethod/ashx.
`  62`  `        method: 'POST',`
`  63`  `        headers: { 'Content-Type': 'application/json' },`
`  64`  `        body: '{}',`
`  65`  `        credentials: 'same-origin'`
`  66`  `    })`
`  67`  `    .then(r => r.json())`
`  68`  `    .then(data => {`
`  69`  `        const res = data.d || data;`
`  70`  `        const box = document.getElementById('existingList');`
  - → Get HTML element by id.
`  71`  `        if (!box) return;`
`  72`  `        if (!res.success) {`
`  73`  `            box.innerHTML = '<div class="text-danger small">' + escapeHtml(res.message || 'Failed') + '</div>';`
  - → Update page HTML.
`  74`  `            return;`
`  75`  `        }`
`  76`  `        const items = res.items || [];`
`  77`  `        if (typeof EduDataTable === 'undefined') {`
`  78`  `            box.innerHTML = items.length ? '' : '<div class="text-muted small">No courseworks yet.</div>';`
  - → Update page HTML.
`  79`  `            items.forEach(function (item) {`
`  80`  `                box.innerHTML += '<div class="existing-item">' + escapeHtml(item.title) + '</div>';`
  - → Update page HTML.
`  81`  `            });`
`  82`  `            return;`
`  83`  `        }`
`  84`  `        if (!existingWorksDt) {`
`  85`  `            existingWorksDt = EduDataTable.create({`
`  86`  `                container: box,`
`  87`  `                pageSize: 8,`
`  88`  `                pageSizeOptions: [5, 8, 15, 25],`
`  89`  `                searchPlaceholder: 'Search title or course...',`
`  90`  `                emptyMessage: 'No courseworks yet.',`
`  91`  `                tableClass: 'table table-sm table-hover mb-0 edt-table',`
`  92`  `                columns: [`
`  93`  `                {`
`  94`  `                    key: 'title', title: 'Title', sortable: true,`
`  95`  `                    render: function (item) {`
`  96`  `                        return '<div class="fw-semibold small text-dark">' + escapeHtml(item.title || 'Untitled') + '</div>';`
  - → Encode text to reduce XSS risk.
`  97`  `                    }`
`  98`  `                },`
`  99`  `                { key: 'courseName', title: 'Course', sortable: true, filter: true, filterLabel: 'Course' },`
` 100`  `                { key: 'type', title: 'Type', sortable: true, filter: true, filterLabel: 'Type' },`
` 101`  `                {`
` 102`  `                    key: 'dueDate', title: 'Due', sortable: true,`
  - → Assignment deadline; submissions close after due day.
` 103`  `                    render: function (item) {`
` 104`  `                        if (!item.dueDate) return '<span class="text-muted small">—</span>';`
  - → Assignment deadline; submissions close after due day.
` 105`  `                        var closed = isDueClosed(item.dueDate);`
  - → Assignment deadline; submissions close after due day.
` 106`  `                        var badge = closed`
` 107`  `                            ? '<span class="badge rounded-pill text-bg-secondary ms-1">Closed</span>'`
` 108`  `                            : '<span class="badge rounded-pill text-bg-success ms-1">Open</span>';`
` 109`  `                        return '<span class="small">' + escapeHtml(item.dueDate) + '</span>' + badge;`
  - → Assignment deadline; submissions close after due day.
` 110`  `                    }`
` 111`  `                },`
` 112`  `                {`
` 113`  `                    key: 'score', title: 'Pts', sortable: true, type: 'number',`
` 114`  `                    render: function () { return '100'; }`
` 115`  `                },`
` 116`  `                {`
` 117`  `                    key: '_actions', title: '', sortable: false, search: false, cellClass: 'text-end',`
` 118`  `                    render: function (item) {`
` 119`  `                        return '<button type="button" class="btn btn-sm btn-link text-danger p-0" title="Delete" onclick="deleteWork(' +`
` 120`  `                        item.cwid + ')"><i class="fa-regular fa-trash-can"></i></button>';`
` 121`  `                    }`
` 122`  `                }`
` 123`  `                ]`
` 124`  `            });`
` 125`  `        }`
` 126`  `        existingWorksDt.setData(items);`
` 127`  `    })`
` 128`  `    .catch(console.error);`
` 129`  `}`
` 130`  ``
` 131`  `function addRubricRow(name, pts) {`
` 132`  `    // New empty rows get 0; user redistributes to keep total 100`
` 133`  `    rubricRows.push({ name: name || '', pts: pts != null ? pts : 0 });`
` 134`  `    renderRubric();`
` 135`  `}`
` 136`  ``
` 137`  `function getRubricTotal() {`
` 138`  `    return rubricRows.reduce(function (s, r) { return s + (Number(r.pts) || 0); }, 0);`
` 139`  `}`
` 140`  ``
` 141`  `function removeRubricRow(i) {`
` 142`  `    rubricRows.splice(i, 1);`
` 143`  `    renderRubric();`
` 144`  `}`
` 145`  ``
` 146`  `function renderRubric() {`
` 147`  `    const list = document.getElementById('rubricList');`
  - → Get HTML element by id.
` 148`  `    list.innerHTML = '';`
  - → Update page HTML.
` 149`  `    rubricRows.forEach((row, i) => {`
` 150`  `        const div = document.createElement('div');`
` 151`  `        div.className = 'd-flex align-items-center gap-2 mb-2';`
` 152`  `        div.innerHTML = ``
  - → Update page HTML.
` 153`  `        <i class="fa-solid fa-grip-vertical text-muted"></i>`
` 154`  `        <input type="text" class="form-control form-control-sm" placeholder="Criterion" value="${escapeAttr(row.name)}"`
` 155`  `        oninput="rubricRows[${i}].name=this.value" />`
` 156`  `        <input type="number" class="form-control form-control-sm" style="max-width:80px;" min="0" max="100" value="${row.pts}"`
` 157`  `        oninput="rubricRows[${i}].pts=parseFloat(this.value)||0; updateRubricTotal();" />`
` 158`  `        <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeRubricRow(${i})">`
` 159`  `        <i class="fa-regular fa-trash-can"></i>`
` 160`  `        </button>`;`
` 161`  `        list.appendChild(div);`
` 162`  `    });`
` 163`  `    updateRubricTotal();`
` 164`  `}`
` 165`  ``
` 166`  `function updateRubricTotal() {`
` 167`  `    const total = getRubricTotal();`
` 168`  `    const el = document.getElementById('lblRubricTotal');`
  - → Get HTML element by id.
` 169`  `    // Always show "out of 100"`
` 170`  `    el.innerText = total + ' / ' + ASSIGNMENT_TOTAL_PTS;`
` 171`  `    if (total === ASSIGNMENT_TOTAL_PTS) {`
` 172`  `        el.classList.remove('text-danger');`
` 173`  `        el.classList.add('text-success');`
` 174`  `    } else {`
` 175`  `        el.classList.remove('text-success');`
` 176`  `        el.classList.add('text-danger');`
` 177`  `    }`
` 178`  `    const hint = document.getElementById('rubricTotalHint');`
  - → Get HTML element by id.
` 179`  `    if (hint) {`
` 180`  `        hint.style.display = total === ASSIGNMENT_TOTAL_PTS ? 'none' : 'block';`
` 181`  `        hint.textContent = 'Rubric criteria must total exactly ' + ASSIGNMENT_TOTAL_PTS + ' pts (currently ' + total + ').';`
` 182`  `    }`
` 183`  `}`
` 184`  ``
` 185`  `function addObjectiveQuestion() {`
` 186`  `    objectiveQuestions.push({`
` 187`  `        question: '',`
` 188`  `        options: { option1: '', option2: '', option3: '', option4: '' },`
` 189`  `        answer: 'option1',`
` 190`  `        explanation: '',`
` 191`  `        oneOrMultipleAnswer: true`
` 192`  `    });`
` 193`  `    renderQuestions();`
` 194`  `}`
` 195`  ``
` 196`  `function removeObjectiveQuestion(i) {`
` 197`  `    objectiveQuestions.splice(i, 1);`
` 198`  `    renderQuestions();`
` 199`  `}`
` 200`  ``
` 201`  `function addOption(qi) {`
` 202`  `    const opts = objectiveQuestions[qi].options;`
` 203`  `    const keys = Object.keys(opts);`
` 204`  `    const next = 'option' + (keys.length + 1);`
` 205`  `    opts[next] = '';`
` 206`  `    renderQuestions();`
` 207`  `}`
` 208`  ``
` 209`  `function removeOption(qi, key) {`
` 210`  `    delete objectiveQuestions[qi].options[key];`
` 211`  `    renderQuestions();`
` 212`  `}`
` 213`  ``
` 214`  `function renderQuestions() {`
` 215`  `    const list = document.getElementById('questionsList');`
  - → Get HTML element by id.
` 216`  `    list.innerHTML = '';`
  - → Update page HTML.
` 217`  `    objectiveQuestions.forEach((q, qi) => {`
` 218`  `        const card = document.createElement('div');`
` 219`  `        card.className = 'glass-card p-4 mb-3';`
` 220`  `        let optionsHtml = '';`
` 221`  `        Object.keys(q.options).forEach(key => {`
` 222`  `            optionsHtml += ``
` 223`  `            <div class="d-flex align-items-center gap-2 mb-2">`
` 224`  `            <input type="radio" name="ans_${qi}" ${q.answer === key ? 'checked' : ''}`
` 225`  `            onchange="objectiveQuestions[${qi}].answer='${key}'" />`
` 226`  `            <input type="text" class="form-control form-control-sm" placeholder="Option"`
` 227`  `            value="${escapeAttr(q.options[key])}"`
` 228`  `            oninput="objectiveQuestions[${qi}].options['${key}']=this.value" />`
` 229`  `            <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeOption(${qi},'${key}')">`
` 230`  `            <i class="fa-regular fa-trash-can"></i>`
` 231`  `            </button>`
` 232`  `            </div>`;`
` 233`  `        });`
` 234`  `        card.innerHTML = ``
  - → Update page HTML.
` 235`  `        <div class="d-flex justify-content-between align-items-center mb-3">`
` 236`  `        <span class="fw-bold"><i class="fa-solid fa-grip-vertical text-muted me-2"></i>Question ${qi + 1}</span>`
` 237`  `        <button type="button" class="btn btn-sm btn-link text-danger p-0" onclick="removeObjectiveQuestion(${qi})">`
` 238`  `        <i class="fa-regular fa-trash-can"></i>`
` 239`  `        </button>`
` 240`  `        </div>`
` 241`  `        <input type="text" class="form-control mb-3" placeholder="Question text"`
` 242`  `        value="${escapeAttr(q.question)}"`
` 243`  `        oninput="objectiveQuestions[${qi}].question=this.value" />`
` 244`  `        ${optionsHtml}`
` 245`  `        <button type="button" class="btn btn-link btn-sm p-0 mb-3" style="color:var(--primary-accent);" onclick="addOption(${qi})">+ Add Option</button>`
` 246`  `        <div class="mb-2">`
` 247`  `        <label class="form-label small text-muted mb-1">Answer key (option id)</label>`
` 248`  `        <input type="text" class="form-control form-control-sm" value="${escapeAttr(q.answer)}"`
` 249`  `        oninput="objectiveQuestions[${qi}].answer=this.value" placeholder="e.g. option1" />`
` 250`  `        </div>`
` 251`  `        <div>`
` 252`  `        <label class="form-label small text-muted mb-1">Explanation</label>`
` 253`  `        <textarea class="form-control form-control-sm" rows="2"`
` 254`  `        oninput="objectiveQuestions[${qi}].explanation=this.value">${escapeHtml(q.explanation || '')}</textarea>`
  - → Encode text to reduce XSS risk.
` 255`  `        </div>`;`
` 256`  `        list.appendChild(card);`
` 257`  `    });`
` 258`  `}`
` 259`  ``
` 260`  `/** Due date (yyyy-MM-dd) is open all that calendar day; closed from next midnight. */`
` 261`  `function isDueClosed(dueDateStr) {`
  - → Assignment deadline; submissions close after due day.
` 262`  `    if (!dueDateStr) return false;`
  - → Assignment deadline; submissions close after due day.
` 263`  `    var m = String(dueDateStr).match(/^(\d{4})-(\d{2})-(\d{2})/);`
  - → Assignment deadline; submissions close after due day.
` 264`  `    if (!m) return false;`
` 265`  `    var end = new Date(parseInt(m[1], 10), parseInt(m[2], 10) - 1, parseInt(m[3], 10) + 1, 0, 0, 0, 0);`
` 266`  `    return Date.now() >= end.getTime();`
` 267`  `}`
` 268`  ``
` 269`  `function saveAssignment(publish) {`
` 270`  `    const err = document.getElementById('saveError');`
  - → Get HTML element by id.
` 271`  `    const ok = document.getElementById('saveOk');`
  - → Get HTML element by id.
` 272`  `    err.style.display = 'none';`
` 273`  `    ok.style.display = 'none';`
` 274`  ``
` 275`  `    const title = document.getElementById('txtTitle').value.trim();`
  - → Get HTML element by id.
` 276`  `    const instructions = document.getElementById('txtInstructions').value.trim();`
  - → Get HTML element by id.
` 277`  `    const cid = parseInt(document.getElementById('ddlCourse').value, 10) || 0;`
  - → Get HTML element by id.
` 278`  `    const cwidRaw = document.getElementById('hfCwid').value;`
  - → Get HTML element by id.
` 279`  `    const cwid = cwidRaw ? parseInt(cwidRaw, 10) : null;`
` 280`  `    const dueDate = (document.getElementById('txtDueDate').value || '').trim();`
  - → Assignment deadline; submissions close after due day.
` 281`  ``
` 282`  `    if (!title) { err.innerText = 'Title is required.'; err.style.display = 'block'; return; }`
` 283`  `    if (!cid) { err.innerText = 'Select a target course.'; err.style.display = 'block'; return; }`
` 284`  `    // Due date required when publishing so closing is explicit in demos`
` 285`  `    if (publish && !dueDate) {`
  - → Assignment deadline; submissions close after due day.
` 286`  `        err.innerText = 'Set a due date before publishing (students cannot submit after that day).';`
` 287`  `        err.style.display = 'block';`
` 288`  `        return;`
` 289`  `    }`
` 290`  ``
` 291`  `    // All assignments / quizzes are always out of 100 pts`
` 292`  `    let score = ASSIGNMENT_TOTAL_PTS;`
` 293`  `    let rubricJson = null;`
` 294`  `    let objectiveQuestionsJson = null;`
` 295`  ``
` 296`  `    if (builderType === 'Text') {`
` 297`  `        const rubricSum = getRubricTotal();`
` 298`  `        if (rubricSum !== ASSIGNMENT_TOTAL_PTS) {`
` 299`  `            err.innerText = 'Grading rubric must total exactly ' + ASSIGNMENT_TOTAL_PTS +`
` 300`  `            ' pts (currently ' + rubricSum + '). Adjust the criterion points.';`
` 301`  `            err.style.display = 'block';`
` 302`  `            return;`
` 303`  `        }`
` 304`  `        rubricJson = JSON.stringify(rubricRows);`
  - → JS object ↔ JSON text.
` 305`  `        score = ASSIGNMENT_TOTAL_PTS;`
` 306`  `    } else {`
` 307`  `        if (objectiveQuestions.length === 0) {`
` 308`  `            err.innerText = 'Add at least one quiz question.';`
` 309`  `            err.style.display = 'block';`
` 310`  `            return;`
` 311`  `        }`
` 312`  `        // Evenly distribute 100 pts across questions (for display in meta)`
` 313`  `        const perQ = Math.round((ASSIGNMENT_TOTAL_PTS / objectiveQuestions.length) * 100) / 100;`
` 314`  `        objectiveQuestions = objectiveQuestions.map(function (q) {`
` 315`  `            q.points = perQ;`
` 316`  `            return q;`
` 317`  `        });`
` 318`  `        objectiveQuestionsJson = JSON.stringify(objectiveQuestions);`
  - → JS object ↔ JSON text.
` 319`  `        score = ASSIGNMENT_TOTAL_PTS;`
` 320`  `    }`
` 321`  ``
` 322`  `    const extra = {`
` 323`  `        dueDate: dueDate || null,`
  - → Assignment deadline; submissions close after due day.
` 324`  `        timeLimit: document.getElementById('txtTimeLimit').value || null,`
  - → Get HTML element by id.
` 325`  `        requireFile: document.getElementById('chkRequireFile').checked,`
  - → Get HTML element by id.
` 326`  `        published: !!publish`
` 327`  `    };`
` 328`  ``
` 329`  `    fetch('Assignments.aspx/SaveCourseWork', {`
  - → HTTP request to server WebMethod/ashx.
` 330`  `        method: 'POST',`
` 331`  `        headers: { 'Content-Type': 'application/json' },`
` 332`  `        body: JSON.stringify({`
  - → JS object ↔ JSON text.
` 333`  `            cwid: cwid,`
` 334`  `            cid: cid,`
` 335`  `            title: title,`
` 336`  `            instructions: instructions,`
` 337`  `            type: builderType,`
` 338`  `            score: score,`
` 339`  `            creditGiven: score,`
` 340`  `            rubricJson: rubricJson,`
` 341`  `            extraMetaJson: JSON.stringify(extra),`
  - → JS object ↔ JSON text.
` 342`  `            objectiveQuestionsJson: objectiveQuestionsJson`
` 343`  `        })`
` 344`  `    })`
` 345`  `    .then(r => r.json())`
` 346`  `    .then(data => {`
` 347`  `        const res = data.d || data;`
` 348`  `        if (res.success) {`
` 349`  `            document.getElementById('hfCwid').value = res.cwid;`
  - → Get HTML element by id.
` 350`  `            ok.innerText = publish ? 'Published successfully.' : 'Draft saved.';`
` 351`  `            ok.style.display = 'block';`
` 352`  `            loadExisting();`
` 353`  `        } else {`
` 354`  `            err.innerText = res.message || 'Save failed.';`
` 355`  `            err.style.display = 'block';`
` 356`  `        }`
` 357`  `    })`
` 358`  `    .catch(e => {`
` 359`  `        err.innerText = 'Network error.';`
` 360`  `        err.style.display = 'block';`
` 361`  `        console.error(e);`
` 362`  `    });`
` 363`  `}`
` 364`  ``
` 365`  `function deleteWork(cwid) {`
` 366`  `    if (!confirm('Delete this coursework? This cannot be undone.')) return;`
` 367`  `    fetch('Assignments.aspx/DeleteCourseWork', {`
  - → HTTP request to server WebMethod/ashx.
` 368`  `        method: 'POST',`
` 369`  `        headers: { 'Content-Type': 'application/json' },`
` 370`  `        body: JSON.stringify({ cwid: cwid })`
  - → JS object ↔ JSON text.
` 371`  `    })`
` 372`  `    .then(r => r.json())`
` 373`  `    .then(data => {`
` 374`  `        const res = data.d || data;`
` 375`  `        if (res.success) loadExisting();`
` 376`  `        else alert(res.message || 'Delete failed');`
` 377`  `    })`
` 378`  `    .catch(console.error);`
` 379`  `}`
` 380`  ``
` 381`  `function escapeHtml(str) {`
  - → Encode text to reduce XSS risk.
` 382`  `    if (!str) return '';`
` 383`  `    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');`
` 384`  `}`
` 385`  `function escapeAttr(str) {`
` 386`  `    return escapeHtml(str).replace(/'/g, '&#39;');`
  - → Encode text to reduce XSS risk.
` 387`  `}`

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
