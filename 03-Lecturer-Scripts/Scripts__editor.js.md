# editor.js
**Source:** `Pages/Lecturer/Scripts/editor.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 41
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 5:** `url` — script-level `const`/`let`/`var`
- **Line 14:** `htmlEditor` — script-level `const`/`let`/`var`
- **Line 19:** `hidden` — script-level `const`/`let`/`var`
- **Line 27:** `toolbar` — script-level `const`/`let`/`var`
- **Line 30:** `btn` — script-level `const`/`let`/`var`
- **Line 32:** `cmd` — script-level `const`/`let`/`var`

## Functions / methods (2 found)

### `execCmd` — lines 2–11

```
function execCmd(cmd, value)
```

#### Explanation

- **Purpose:** Implements `execCmd`.
- **Parameters:** `cmd, value`
- **Local variables:** `url`

#### Line-by-line (this function)

`   2`  ``
`   3`  `    function execCmd(cmd, value) {`
`   4`  `        if(cmd === 'createLink'){`
`   5`  `            const url = prompt('Enter URL');`
`   6`  `            if(!url) return;`
`   7`  `            document.execCommand('createLink', false, url);`
`   8`  `            return;`
`   9`  `        }`
`  10`  `        document.execCommand(cmd, false, value || null);`
`  11`  `    }`

---

### `sync` — lines 17–21

```
function sync()
```

#### Explanation

- **Purpose:** Implements `sync`.
- **Local variables:** `hidden`

#### Line-by-line (this function)

`  17`  ``
`  18`  `        function sync(){`
`  19`  `            const hidden = document.getElementById('txtLessonContent');`
  - → Get HTML element by id.
`  20`  `            if(hidden) hidden.value = htmlEditor.innerHTML;`
  - → Update page HTML.
`  21`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `// editor.js: small helpers for lesson editor`
`   2`  `(function(){`
`   3`  `    function execCmd(cmd, value) {`
`   4`  `        if(cmd === 'createLink'){`
`   5`  `            const url = prompt('Enter URL');`
`   6`  `            if(!url) return;`
`   7`  `            document.execCommand('createLink', false, url);`
`   8`  `            return;`
`   9`  `        }`
`  10`  `        document.execCommand(cmd, false, value || null);`
`  11`  `    }`
`  12`  ``
`  13`  `    window.initEditor = function(){`
`  14`  `        const htmlEditor = document.getElementById('htmlEditor');`
  - → Get HTML element by id.
`  15`  `        if(!htmlEditor) return;`
`  16`  ``
`  17`  `        // sync to hidden textarea`
`  18`  `        function sync(){`
`  19`  `            const hidden = document.getElementById('txtLessonContent');`
  - → Get HTML element by id.
`  20`  `            if(hidden) hidden.value = htmlEditor.innerHTML;`
  - → Update page HTML.
`  21`  `        }`
`  22`  ``
`  23`  `        htmlEditor.addEventListener('input', sync);`
  - → DOM event handler.
`  24`  `        htmlEditor.addEventListener('blur', sync);`
  - → DOM event handler.
`  25`  ``
`  26`  `        // toolbar bindings`
`  27`  `        const toolbar = document.getElementById('editorToolbar');`
  - → Get HTML element by id.
`  28`  `        if(toolbar){`
`  29`  `            toolbar.addEventListener('click', function(e){`
  - → DOM event handler.
`  30`  `                const btn = e.target.closest('button[data-cmd]');`
`  31`  `                if(!btn) return;`
`  32`  `                const cmd = btn.getAttribute('data-cmd');`
`  33`  `                execCmd(cmd);`
`  34`  `                sync();`
`  35`  `            });`
`  36`  `        }`
`  37`  ``
`  38`  `        // expose quick API`
`  39`  `        window.__editorSync = sync;`
`  40`  `    };`
`  41`  `})();`

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
