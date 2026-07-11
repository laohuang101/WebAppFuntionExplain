# dropdowns.js
**Source:** `Pages/Lecturer/Scripts/dropdowns.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 61
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 4:** `defaultData` — script-level `const`/`let`/`var`
- **Line 33:** `sel` — script-level `const`/`let`/`var`
- **Line 38:** `o` — script-level `const`/`let`/`var`
- **Line 46:** `data` — script-level `const`/`let`/`var`

## Functions / methods (2 found)

### `getData` — lines 26–30

```
function getData()
```

#### Explanation

- **Purpose:** Implements `getData`.
- **Pattern:** Read/load data for display.

#### Line-by-line (this function)

`  26`  ``
`  27`  ``
`  28`  `    function getData(){`
`  29`  `        return window.__dropdownData || defaultData;`
`  30`  `    }`

---

### `populateSelect` — lines 30–43

```
function populateSelect(id, items)
```

#### Explanation

- **Purpose:** Implements `populateSelect`.
- **Parameters:** `id, items`
- **Local variables:** `sel`, `o`

#### Line-by-line (this function)

`  30`  ``
`  31`  ``
`  32`  `    function populateSelect(id, items){`
`  33`  `        const sel = document.getElementById(id);`
  - → Get HTML element by id.
`  34`  `        if(!sel) return;`
`  35`  `        // clear existing`
`  36`  `        sel.innerHTML = '';`
  - → Update page HTML.
`  37`  `        items.forEach(it => {`
`  38`  `            const o = document.createElement('option');`
`  39`  `            o.value = it.value;`
`  40`  `            o.text = it.label;`
`  41`  `            sel.appendChild(o);`
`  42`  `        });`
`  43`  `    }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `// dropdowns.js - provides JSON-driven dropdown population for CourseCreation page`
`   2`  `(function(){`
`   3`  `    // Default dropdown data (can be extended or fetched from server)`
`   4`  `    const defaultData = {`
`   5`  `        categories: [`
`   6`  `        { value: 'UI/UX Design', label: 'UI/UX Design' },`
`   7`  `        { value: 'Product Design', label: 'Product Design' },`
`   8`  `        { value: 'Web Development', label: 'Web Development' },`
`   9`  `        { value: 'Software Engineering', label: 'Software Engineering' }`
`  10`  `        ],`
`  11`  `        levels: [`
`  12`  `        { value: 'Beginner', label: 'Beginner' },`
`  13`  `        { value: 'Intermediate', label: 'Intermediate' },`
`  14`  `        { value: 'Advanced', label: 'Advanced' }`
`  15`  `        ],`
`  16`  `        lessonTypes: [`
`  17`  `        { value: 'Text', label: 'Text Content' },`
`  18`  `        { value: 'Video', label: 'Video Link' },`
`  19`  `        { value: 'Quiz', label: 'Quiz / Assignment Question' }`
`  20`  `        ]`
`  21`  `    };`
`  22`  ``
`  23`  `    // Allows page or tests to override data programmatically`
`  24`  `    window.setDropdownData = function(data){`
`  25`  `        window.__dropdownData = Object.assign({}, window.__dropdownData || defaultData, data);`
`  26`  `    };`
`  27`  ``
`  28`  `    function getData(){`
`  29`  `        return window.__dropdownData || defaultData;`
`  30`  `    }`
`  31`  ``
`  32`  `    function populateSelect(id, items){`
`  33`  `        const sel = document.getElementById(id);`
  - → Get HTML element by id.
`  34`  `        if(!sel) return;`
`  35`  `        // clear existing`
`  36`  `        sel.innerHTML = '';`
  - → Update page HTML.
`  37`  `        items.forEach(it => {`
`  38`  `            const o = document.createElement('option');`
`  39`  `            o.value = it.value;`
`  40`  `            o.text = it.label;`
`  41`  `            sel.appendChild(o);`
`  42`  `        });`
`  43`  `    }`
`  44`  ``
`  45`  `    window.initDropdowns = function(){`
`  46`  `        const data = getData();`
`  47`  `        populateSelect('ddlCategory', data.categories);`
`  48`  `        populateSelect('ddlLevel', data.levels);`
`  49`  `        populateSelect('ddlLessonType', data.lessonTypes);`
`  50`  `    };`
`  51`  ``
`  52`  `    // Optionally attempt to fetch a remote JSON file 'dropdowns.json' in same folder`
`  53`  `    // If present, it will override defaults (non-blocking)`
`  54`  `    fetch('Scripts/dropdowns.json').then(r=>{`
  - → HTTP request to server WebMethod/ashx.
`  55`  `        if(!r.ok) return null; return r.json();`
`  56`  `    }).then(json=>{`
`  57`  `        if(json) {`
`  58`  `            window.setDropdownData(json);`
`  59`  `        }`
`  60`  `    }).catch(()=>{});`
`  61`  `})();`

## Source snapshot (raw)

```javascript
// dropdowns.js - provides JSON-driven dropdown population for CourseCreation page
(function(){
    // Default dropdown data (can be extended or fetched from server)
    const defaultData = {
        categories: [
        { value: 'UI/UX Design', label: 'UI/UX Design' },
        { value: 'Product Design', label: 'Product Design' },
        { value: 'Web Development', label: 'Web Development' },
        { value: 'Software Engineering', label: 'Software Engineering' }
        ],
        levels: [
        { value: 'Beginner', label: 'Beginner' },
        { value: 'Intermediate', label: 'Intermediate' },
        { value: 'Advanced', label: 'Advanced' }
        ],
        lessonTypes: [
        { value: 'Text', label: 'Text Content' },
        { value: 'Video', label: 'Video Link' },
        { value: 'Quiz', label: 'Quiz / Assignment Question' }
        ]
    };

    // Allows page or tests to override data programmatically
    window.setDropdownData = function(data){
        window.__dropdownData = Object.assign({}, window.__dropdownData || defaultData, data);
    };

    function getData(){
        return window.__dropdownData || defaultData;
    }

    function populateSelect(id, items){
        const sel = document.getElementById(id);
        if(!sel) return;
        // clear existing
        sel.innerHTML = '';
        items.forEach(it => {
            const o = document.createElement('option');
            o.value = it.value;
            o.text = it.label;
            sel.appendChild(o);
        });
    }

    window.initDropdowns = function(){
        const data = getData();
        populateSelect('ddlCategory', data.categories);
        populateSelect('ddlLevel', data.levels);
        populateSelect('ddlLessonType', data.lessonTypes);
    };

    // Optionally attempt to fetch a remote JSON file 'dropdowns.json' in same folder
    // If present, it will override defaults (non-blocking)
    fetch('Scripts/dropdowns.json').then(r=>{
        if(!r.ok) return null; return r.json();
    }).then(json=>{
        if(json) {
            window.setDropdownData(json);
        }
    }).catch(()=>{});
})();

```
