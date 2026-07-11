# editor.js
**Source:** `Pages/Lecturer/Scripts/editor.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 41
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `url` | `const/let/var` | HTTP URL to media or page. |
| `htmlEditor` | `const/let/var` | Holds “html Editor” for this scope. |
| `hidden` | `const/let/var` | Holds “hidden” for this scope. |
| `toolbar` | `const/let/var` | Holds “toolbar” for this scope. |
| `btn` | `const/let/var` | Button DOM element. |
| `cmd` | `const/let/var` | SqlCommand — the SQL statement + parameters object. |

## Functions / methods (2 found)

### `execCmd` — lines 2–11

#### Signature

```javascript
function execCmd(cmd, value)
```

#### What it is

Function `execCmd` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `execCmd`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `—` | SqlCommand — the SQL statement + parameters object. |
| `value` | `—` | Holds “value” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `url` | `—` | HTTP URL to media or page. |

#### Code

```javascript
   2 | 
   3 |     function execCmd(cmd, value) {
   4 |         if(cmd === 'createLink'){
   5 |             const url = prompt('Enter URL');
   6 |             if(!url) return;
   7 |             document.execCommand('createLink', false, url);
   8 |             return;
   9 |         }
  10 |         document.execCommand(cmd, false, value || null);
  11 |     }
```

---

### `sync` — lines 17–21

#### Signature

```javascript
function sync()
```

#### What it is

Function `sync` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `sync`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `hidden` | `—` | Holds “hidden” for this scope.  DOM element from the page. |

#### Code

```javascript
  17 | 
  18 |         function sync(){
  19 |             const hidden = document.getElementById('txtLessonContent');
  20 |             if(hidden) hidden.value = htmlEditor.innerHTML;
  21 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | // editor.js: small helpers for lesson editor
   2 | (function(){
   3 |     function execCmd(cmd, value) {
   4 |         if(cmd === 'createLink'){
   5 |             const url = prompt('Enter URL');
   6 |             if(!url) return;
   7 |             document.execCommand('createLink', false, url);
   8 |             return;
   9 |         }
  10 |         document.execCommand(cmd, false, value || null);
  11 |     }
  12 | 
  13 |     window.initEditor = function(){
  14 |         const htmlEditor = document.getElementById('htmlEditor');
  15 |         if(!htmlEditor) return;
  16 | 
  17 |         // sync to hidden textarea
  18 |         function sync(){
  19 |             const hidden = document.getElementById('txtLessonContent');
  20 |             if(hidden) hidden.value = htmlEditor.innerHTML;
  21 |         }
  22 | 
  23 |         htmlEditor.addEventListener('input', sync);
  24 |         htmlEditor.addEventListener('blur', sync);
  25 | 
  26 |         // toolbar bindings
  27 |         const toolbar = document.getElementById('editorToolbar');
  28 |         if(toolbar){
  29 |             toolbar.addEventListener('click', function(e){
  30 |                 const btn = e.target.closest('button[data-cmd]');
  31 |                 if(!btn) return;
  32 |                 const cmd = btn.getAttribute('data-cmd');
  33 |                 execCmd(cmd);
  34 |                 sync();
  35 |             });
  36 |         }
  37 | 
  38 |         // expose quick API
  39 |         window.__editorSync = sync;
  40 |     };
  41 | })();
```
