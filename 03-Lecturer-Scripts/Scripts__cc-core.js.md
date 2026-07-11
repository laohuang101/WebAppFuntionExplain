# cc-core.js
**Source:** `Pages/Lecturer/Scripts/cc-core.js`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 74
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 4:** `courses` — script-level `const`/`let`/`var`
- **Line 6:** `currentCourseId` — script-level `const`/`let`/`var`
- **Line 7:** `activeWizardStep` — script-level `const`/`let`/`var`
- **Line 8:** `editingSectionId` — script-level `const`/`let`/`var`
- **Line 10:** `targetChapterId` — script-level `const`/`let`/`var`
- **Line 11:** `editingLessonId` — script-level `const`/`let`/`var`
- **Line 17:** `x` — script-level `const`/`let`/`var`
- **Line 32:** `parsed` — script-level `const`/`let`/`var`
- **Line 37:** `msg` — script-level `const`/`let`/`var`
- **Line 47:** `body` — script-level `const`/`let`/`var`
- **Line 53:** `el` — script-level `const`/`let`/`var`
- **Line 55:** `inst` — script-level `const`/`let`/`var`
- **Line 69:** `open` — script-level `const`/`let`/`var`

## Functions / methods (5 found)

### `unwrap` — lines 13–21

```javascript
function unwrap(data)
```

#### Explanation

- **Purpose:** Implements `unwrap`.
- **Parameters:** `data`
- **Local variables:** `x`

#### Line-by-line (this function)

```javascript
  13 | 
  14 | function unwrap(data) {
  15 |     if (window.EduApi && EduApi.unwrap) return EduApi.unwrap(data);
  16 |     if (!data) return data;
  17 |     let x = data;
  18 |     if (x.d !== undefined) x = x.d;
  19 |     if (x && x.d !== undefined) x = x.d;
  20 |     return x;
  21 | }
```

---

### `postJson` — lines 21–43

```javascript
function postJson(url, body)
```

#### Explanation

- **Purpose:** Implements `postJson`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters:** `url, body`
- **Local variables:** `parsed`, `msg`

#### Line-by-line (this function)

```javascript
  21 | 
  22 | 
  23 | function postJson(url, body) {
  24 |     if (window.EduApi && EduApi.postJson) return EduApi.postJson(url, body);
  25 |     return fetch(url, {
  26 |         method: 'POST',
  27 |         headers: { 'Content-Type': 'application/json; charset=utf-8' },
  28 |         body: JSON.stringify(body || {}),
  29 |         credentials: 'same-origin'
  30 |     }).then(function (res) {
  31 |         return res.text().then(function (text) {
  32 |             var parsed = null;
  33 |             try { parsed = text ? JSON.parse(text) : null; } catch (e) {
  34 |                 throw new Error('Server returned non-JSON (HTTP ' + res.status + '): ' + text.slice(0, 200));
  35 |             }
  36 |             if (!res.ok) {
  37 |                 var msg = (parsed && (parsed.message || parsed.Message)) || ('HTTP ' + res.status);
  38 |                 throw new Error(msg);
  39 |             }
  40 |             return unwrap(parsed);
  41 |         });
  42 |     });
  43 | }
```

**Line notes**

- **L25:** HTTP request to server WebMethod/ashx.
- **L28:** JS object ↔ JSON text.
- **L33:** JS object ↔ JSON text.

---

### `curriculumApi` — lines 45–49

```javascript
function curriculumApi(action, payload)
```

#### Explanation

- **Purpose:** Implements `curriculumApi`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `action, payload`
- **Local variables:** `body`

#### Line-by-line (this function)

```javascript
  45 | 
  46 | function curriculumApi(action, payload) {
  47 |     var body = Object.assign({ action: action }, payload || {});
  48 |     return postJson('CurriculumApi.ashx', body);
  49 | }
```

---

### `hideModal` — lines 51–58

```javascript
function hideModal(id)
```

#### Explanation

- **Purpose:** Implements `hideModal`.
- **Parameters:** `id`
- **Local variables:** `el`, `inst`

#### Line-by-line (this function)

```javascript
  51 | 
  52 | function hideModal(id) {
  53 |     var el = document.getElementById(id);
  54 |     if (!el) return;
  55 |     var inst = bootstrap.Modal.getInstance(el);
  56 |     if (!inst) inst = bootstrap.Modal.getOrCreateInstance(el);
  57 |     inst.hide();
  58 | }
```

**Line notes**

- **L53:** Get HTML element by id.

---

### `showModal` — lines 58–65

```javascript
function showModal(id)
```

#### Explanation

- **Purpose:** Implements `showModal`.
- **Parameters:** `id`
- **Local variables:** `el`

#### Line-by-line (this function)

```javascript
  58 | 
  59 | 
  60 | function showModal(id) {
  61 |     var el = document.getElementById(id);
  62 |     if (!el) return;
  63 |     // Nested modals: keep parent wizard open
  64 |     bootstrap.Modal.getOrCreateInstance(el, { backdrop: true, keyboard: true }).show();
  65 | }
```

**Line notes**

- **L61:** Get HTML element by id.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```javascript
   1 | // Course Creation — core helpers (API, modals)
   2 | // Course Creation script (moved from CourseCreation.aspx)
   3 | // Handles course grid, wizard, curriculum, and thumbnail upload via dropzone
   4 | 
   5 | let courses = [];
   6 | let currentCourseId = null;
   7 | let activeWizardStep = 1;
   8 | 
   9 | let editingSectionId = null; // for section add/edit
  10 | let targetChapterId = null; // for lesson adding
  11 | let editingLessonId = null; // for lesson editing
  12 | 
  13 | /** Prefer shared EduApi (csrf + unwrap) from master page when available */
  14 | function unwrap(data) {
  15 |     if (window.EduApi && EduApi.unwrap) return EduApi.unwrap(data);
  16 |     if (!data) return data;
  17 |     let x = data;
  18 |     if (x.d !== undefined) x = x.d;
  19 |     if (x && x.d !== undefined) x = x.d;
  20 |     return x;
  21 | }
  22 | 
  23 | function postJson(url, body) {
  24 |     if (window.EduApi && EduApi.postJson) return EduApi.postJson(url, body);
  25 |     return fetch(url, {
  26 |         method: 'POST',
  27 |         headers: { 'Content-Type': 'application/json; charset=utf-8' },
  28 |         body: JSON.stringify(body || {}),
  29 |         credentials: 'same-origin'
  30 |     }).then(function (res) {
  31 |         return res.text().then(function (text) {
  32 |             var parsed = null;
  33 |             try { parsed = text ? JSON.parse(text) : null; } catch (e) {
  34 |                 throw new Error('Server returned non-JSON (HTTP ' + res.status + '): ' + text.slice(0, 200));
  35 |             }
  36 |             if (!res.ok) {
  37 |                 var msg = (parsed && (parsed.message || parsed.Message)) || ('HTTP ' + res.status);
  38 |                 throw new Error(msg);
  39 |             }
  40 |             return unwrap(parsed);
  41 |         });
  42 |     });
  43 | }
  44 | 
  45 | /** Curriculum API (ashx) - reliable lesson/section CRUD */
  46 | function curriculumApi(action, payload) {
  47 |     var body = Object.assign({ action: action }, payload || {});
  48 |     return postJson('CurriculumApi.ashx', body);
  49 | }
  50 | 
  51 | /** Safely hide a Bootstrap modal (handles missing instance) */
  52 | function hideModal(id) {
  53 |     var el = document.getElementById(id);
  54 |     if (!el) return;
  55 |     var inst = bootstrap.Modal.getInstance(el);
  56 |     if (!inst) inst = bootstrap.Modal.getOrCreateInstance(el);
  57 |     inst.hide();
  58 | }
  59 | 
  60 | function showModal(id) {
  61 |     var el = document.getElementById(id);
  62 |     if (!el) return;
  63 |     // Nested modals: keep parent wizard open
  64 |     bootstrap.Modal.getOrCreateInstance(el, { backdrop: true, keyboard: true }).show();
  65 | }
  66 | 
  67 | /** Keep body scroll + multiple backdrops clean when nested modals close */
  68 | document.addEventListener('hidden.bs.modal', function () {
  69 |     var open = document.querySelectorAll('.modal.show');
  70 |     if (open.length) {
  71 |         document.body.classList.add('modal-open');
  72 |     }
  73 | });
  74 | 
```

**Line notes**

- **L25:** HTTP request to server WebMethod/ashx.
- **L28:** JS object ↔ JSON text.
- **L33:** JS object ↔ JSON text.
- **L53:** Get HTML element by id.
- **L61:** Get HTML element by id.
- **L68:** DOM event handler.

## Source snapshot (raw)

```javascript
// Course Creation — core helpers (API, modals)
// Course Creation script (moved from CourseCreation.aspx)
// Handles course grid, wizard, curriculum, and thumbnail upload via dropzone

let courses = [];
let currentCourseId = null;
let activeWizardStep = 1;

let editingSectionId = null; // for section add/edit
let targetChapterId = null; // for lesson adding
let editingLessonId = null; // for lesson editing

/** Prefer shared EduApi (csrf + unwrap) from master page when available */
function unwrap(data) {
    if (window.EduApi && EduApi.unwrap) return EduApi.unwrap(data);
    if (!data) return data;
    let x = data;
    if (x.d !== undefined) x = x.d;
    if (x && x.d !== undefined) x = x.d;
    return x;
}

function postJson(url, body) {
    if (window.EduApi && EduApi.postJson) return EduApi.postJson(url, body);
    return fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json; charset=utf-8' },
        body: JSON.stringify(body || {}),
        credentials: 'same-origin'
    }).then(function (res) {
        return res.text().then(function (text) {
            var parsed = null;
            try { parsed = text ? JSON.parse(text) : null; } catch (e) {
                throw new Error('Server returned non-JSON (HTTP ' + res.status + '): ' + text.slice(0, 200));
            }
            if (!res.ok) {
                var msg = (parsed && (parsed.message || parsed.Message)) || ('HTTP ' + res.status);
                throw new Error(msg);
            }
            return unwrap(parsed);
        });
    });
}

/** Curriculum API (ashx) - reliable lesson/section CRUD */
function curriculumApi(action, payload) {
    var body = Object.assign({ action: action }, payload || {});
    return postJson('CurriculumApi.ashx', body);
}

/** Safely hide a Bootstrap modal (handles missing instance) */
function hideModal(id) {
    var el = document.getElementById(id);
    if (!el) return;
    var inst = bootstrap.Modal.getInstance(el);
    if (!inst) inst = bootstrap.Modal.getOrCreateInstance(el);
    inst.hide();
}

function showModal(id) {
    var el = document.getElementById(id);
    if (!el) return;
    // Nested modals: keep parent wizard open
    bootstrap.Modal.getOrCreateInstance(el, { backdrop: true, keyboard: true }).show();
}

/** Keep body scroll + multiple backdrops clean when nested modals close */
document.addEventListener('hidden.bs.modal', function () {
    var open = document.querySelectorAll('.modal.show');
    if (open.length) {
        document.body.classList.add('modal-open');
    }
});


```
