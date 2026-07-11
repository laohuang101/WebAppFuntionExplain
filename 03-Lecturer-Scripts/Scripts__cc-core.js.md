# cc-core.js
**Source:** `Pages/Lecturer/Scripts/cc-core.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 74
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `courses` | `const/let/var` | Often a collection related to courses (plural name). |
| `currentCourseId` | `const/let/var` | Holds “current Course Id” for this scope. |
| `activeWizardStep` | `const/let/var` | Holds “active Wizard Step” for this scope. |
| `editingSectionId` | `const/let/var` | Holds “editing Section Id” for this scope. |
| `targetChapterId` | `const/let/var` | Holds “target Chapter Id” for this scope. |
| `editingLessonId` | `const/let/var` | Holds “editing Lesson Id” for this scope. |
| `x` | `const/let/var` | Generic temporary / coordinate / exception alias. |
| `parsed` | `const/let/var` | Holds “parsed” for this scope. |
| `msg` | `const/let/var` | Human-readable message (error or success). |
| `body` | `const/let/var` | HTTP request body. |
| `el` | `const/let/var` | Generic DOM element. |
| `inst` | `const/let/var` | Holds “inst” for this scope. |
| `open` | `const/let/var` | Holds “open” for this scope. |

## Functions / methods (5 found)

### `unwrap` — lines 13–21

#### Signature

```javascript
function unwrap(data)
```

#### What it is

Function `unwrap` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `unwrap`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `data` | `—` | Holds “data” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `x` | `—` | Generic temporary / coordinate / exception alias. |

#### Code

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

#### Signature

```javascript
function postJson(url, body)
```

#### What it is

Browser-side function `postJson` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Convert a JavaScript object into a JSON string for the server.
3. Parse the server JSON response into a JavaScript object.
4. Stop with an error (invalid access or bad input).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `url` | `—` | HTTP URL to media or page. |
| `body` | `—` | HTTP request body. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `parsed` | `—` | Holds “parsed” for this scope. |
| `msg` | `—` | Human-readable message (error or success). |

#### Code

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

---

### `curriculumApi` — lines 45–49

#### Signature

```javascript
function curriculumApi(action, payload)
```

#### What it is

Function `curriculumApi` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `curriculumApi`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `action` | `—` | Holds “action” for this scope. |
| `payload` | `—` | Object about to be JSON-serialized or sent over network. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `body` | `—` | HTTP request body. |

#### Code

```javascript
  45 | 
  46 | function curriculumApi(action, payload) {
  47 |     var body = Object.assign({ action: action }, payload || {});
  48 |     return postJson('CurriculumApi.ashx', body);
  49 | }
```

---

### `hideModal` — lines 51–58

#### Signature

```javascript
function hideModal(id)
```

#### What it is

Function `hideModal` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `hideModal`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `id` | `—` | Generic primary key / identifier. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `el` | `—` | Generic DOM element.  DOM element from the page. |
| `inst` | `—` | Holds “inst” for this scope. |

#### Code

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

---

### `showModal` — lines 58–65

#### Signature

```javascript
function showModal(id)
```

#### What it is

Updates the page HTML for **show Modal**.

#### How it works

1. Starts when something calls `showModal`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `id` | `—` | Generic primary key / identifier. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `el` | `—` | Generic DOM element.  DOM element from the page. |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
