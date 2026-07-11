# editor.js
**Source:** `Pages/Lecturer/Scripts/editor.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 41
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 5:** `url` — script-level `const`/`let`/`var` — **HTTP URL to media or page.**
- **Line 14:** `htmlEditor` — script-level `const`/`let`/`var` — **Holds “html Editor” for this scope.**
- **Line 19:** `hidden` — script-level `const`/`let`/`var` — **Holds “hidden” for this scope.**
- **Line 27:** `toolbar` — script-level `const`/`let`/`var` — **Holds “toolbar” for this scope.**
- **Line 30:** `btn` — script-level `const`/`let`/`var` — **Button DOM element.**
- **Line 32:** `cmd` — script-level `const`/`let`/`var` — **SqlCommand — the SQL statement + parameters object.**

## Functions / methods (2 found)

### `execCmd` — lines 2–11

```javascript
function execCmd(cmd, value)
```

#### Explanation

- **Purpose:** Implements `execCmd`.
- **Parameters (what each means):**
- `cmd` — SqlCommand — the SQL statement + parameters object.
- `value` — Holds “value” for this scope.
- **Local variables (what each means):**
- `url` — HTTP URL to media or page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L5:** `url` means: HTTP URL to media or page.

---

### `sync` — lines 17–21

```javascript
function sync()
```

#### Explanation

- **Purpose:** Implements `sync`.
- **Local variables (what each means):**
- `hidden` — Holds “hidden” for this scope.  DOM element from the page.

#### Line-by-line (this function)

```javascript
  17 | 
  18 |         function sync(){
  19 |             const hidden = document.getElementById('txtLessonContent');
  20 |             if(hidden) hidden.value = htmlEditor.innerHTML;
  21 |         }
```

**Line notes** (what code + variables mean)

- **L19:** Get HTML element by id. | `hidden` means: Holds “hidden” for this scope.  DOM element from the page.
- **L20:** Update page HTML.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L5:** `url` means: HTTP URL to media or page.
- **L14:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L19:** Get HTML element by id. | `hidden` means: Holds “hidden” for this scope.  DOM element from the page.
- **L20:** Update page HTML.
- **L23:** DOM event handler.
- **L24:** DOM event handler.
- **L27:** Get HTML element by id. | `toolbar` means: Holds “toolbar” for this scope.  DOM element from the page.
- **L29:** DOM event handler.
- **L30:** `btn` means: Button DOM element.
- **L32:** `cmd` means: SqlCommand — the SQL statement + parameters object.

## Source snapshot (raw)

```javascript
// editor.js: small helpers for lesson editor
(function(){
    function execCmd(cmd, value) {
        if(cmd === 'createLink'){
            const url = prompt('Enter URL');
            if(!url) return;
            document.execCommand('createLink', false, url);
            return;
        }
        document.execCommand(cmd, false, value || null);
    }

    window.initEditor = function(){
        const htmlEditor = document.getElementById('htmlEditor');
        if(!htmlEditor) return;

        // sync to hidden textarea
        function sync(){
            const hidden = document.getElementById('txtLessonContent');
            if(hidden) hidden.value = htmlEditor.innerHTML;
        }

        htmlEditor.addEventListener('input', sync);
        htmlEditor.addEventListener('blur', sync);

        // toolbar bindings
        const toolbar = document.getElementById('editorToolbar');
        if(toolbar){
            toolbar.addEventListener('click', function(e){
                const btn = e.target.closest('button[data-cmd]');
                if(!btn) return;
                const cmd = btn.getAttribute('data-cmd');
                execCmd(cmd);
                sync();
            });
        }

        // expose quick API
        window.__editorSync = sync;
    };
})();

```
