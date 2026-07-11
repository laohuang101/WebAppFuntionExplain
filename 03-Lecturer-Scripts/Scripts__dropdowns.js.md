# dropdowns.js
**Source:** `Pages/Lecturer/Scripts/dropdowns.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 61
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `defaultData` | `const/let/var` | Holds “default Data” for this scope. |
| `sel` | `const/let/var` | Holds “sel” for this scope. |
| `o` | `const/let/var` | Holds “o” for this scope. |
| `data` | `const/let/var` | Holds “data” for this scope. |

## Functions / methods (2 found)

### `getData` — lines 26–30

#### Signature

```javascript
function getData()
```

#### What it is

Reads/loads data related to **Data** and returns it for display or further use.

#### How it works

1. Starts when something calls `getData`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
  26 | 
  27 | 
  28 |     function getData(){
  29 |         return window.__dropdownData || defaultData;
  30 |     }
```

---

### `populateSelect` — lines 30–43

#### Signature

```javascript
function populateSelect(id, items)
```

#### What it is

Function `populateSelect` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `populateSelect`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `id` | `—` | Generic primary key / identifier. |
| `items` | `—` | Array of rows for UI tables. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `sel` | `—` | Holds “sel” for this scope.  DOM element from the page. |
| `o` | `—` | Holds “o” for this scope. |

#### Code

```javascript
  30 | 
  31 | 
  32 |     function populateSelect(id, items){
  33 |         const sel = document.getElementById(id);
  34 |         if(!sel) return;
  35 |         // clear existing
  36 |         sel.innerHTML = '';
  37 |         items.forEach(it => {
  38 |             const o = document.createElement('option');
  39 |             o.value = it.value;
  40 |             o.text = it.label;
  41 |             sel.appendChild(o);
  42 |         });
  43 |     }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | // dropdowns.js - provides JSON-driven dropdown population for CourseCreation page
   2 | (function(){
   3 |     // Default dropdown data (can be extended or fetched from server)
   4 |     const defaultData = {
   5 |         categories: [
   6 |         { value: 'UI/UX Design', label: 'UI/UX Design' },
   7 |         { value: 'Product Design', label: 'Product Design' },
   8 |         { value: 'Web Development', label: 'Web Development' },
   9 |         { value: 'Software Engineering', label: 'Software Engineering' }
  10 |         ],
  11 |         levels: [
  12 |         { value: 'Beginner', label: 'Beginner' },
  13 |         { value: 'Intermediate', label: 'Intermediate' },
  14 |         { value: 'Advanced', label: 'Advanced' }
  15 |         ],
  16 |         lessonTypes: [
  17 |         { value: 'Text', label: 'Text Content' },
  18 |         { value: 'Video', label: 'Video Link' },
  19 |         { value: 'Quiz', label: 'Quiz / Assignment Question' }
  20 |         ]
  21 |     };
  22 | 
  23 |     // Allows page or tests to override data programmatically
  24 |     window.setDropdownData = function(data){
  25 |         window.__dropdownData = Object.assign({}, window.__dropdownData || defaultData, data);
  26 |     };
  27 | 
  28 |     function getData(){
  29 |         return window.__dropdownData || defaultData;
  30 |     }
  31 | 
  32 |     function populateSelect(id, items){
  33 |         const sel = document.getElementById(id);
  34 |         if(!sel) return;
  35 |         // clear existing
  36 |         sel.innerHTML = '';
  37 |         items.forEach(it => {
  38 |             const o = document.createElement('option');
  39 |             o.value = it.value;
  40 |             o.text = it.label;
  41 |             sel.appendChild(o);
  42 |         });
  43 |     }
  44 | 
  45 |     window.initDropdowns = function(){
  46 |         const data = getData();
  47 |         populateSelect('ddlCategory', data.categories);
  48 |         populateSelect('ddlLevel', data.levels);
  49 |         populateSelect('ddlLessonType', data.lessonTypes);
  50 |     };
  51 | 
  52 |     // Optionally attempt to fetch a remote JSON file 'dropdowns.json' in same folder
  53 |     // If present, it will override defaults (non-blocking)
  54 |     fetch('Scripts/dropdowns.json').then(r=>{
  55 |         if(!r.ok) return null; return r.json();
  56 |     }).then(json=>{
  57 |         if(json) {
  58 |             window.setDropdownData(json);
  59 |         }
  60 |     }).catch(()=>{});
  61 | })();
```
