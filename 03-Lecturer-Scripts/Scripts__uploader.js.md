# uploader.js
**Source:** `Pages/Lecturer/Scripts/uploader.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 54
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 4:** `fd` — script-level `const`/`let`/`var`
- **Line 10:** `bgInput` — script-level `const`/`let`/`var`
- **Line 12:** `preview` — script-level `const`/`let`/`var`
- **Line 22:** `drop` — script-level `const`/`let`/`var`
- **Line 24:** `fileInput` — script-level `const`/`let`/`var`
- **Line 42:** `f` — script-level `const`/`let`/`var`

## Functions / methods (1 found)

### `uploadThumbnailFile` — lines 2–19

```
function uploadThumbnailFile(file)
```

#### Explanation

- **Purpose:** Implements `uploadThumbnailFile`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters:** `file`
- **Local variables:** `fd`, `bgInput`, `preview`

#### Line-by-line (this function)

`   2`  ``
`   3`  `    function uploadThumbnailFile(file){`
`   4`  `        const fd = new FormData();`
`   5`  `        fd.append('file', file);`
`   6`  `        fetch('UploadThumbnail.ashx', { method: 'POST', body: fd })`
  - → HTTP request to server WebMethod/ashx.
`   7`  `        .then(r => r.json())`
`   8`  `        .then(resp => {`
`   9`  `            if (resp.success) {`
`  10`  `                const bgInput = document.getElementById('txtBgImg');`
  - → Get HTML element by id.
`  11`  `                if (bgInput) bgInput.value = resp.url;`
`  12`  `                const preview = document.getElementById('courseThumbPreview') || document.getElementById('previewImg');`
  - → Get HTML element by id.
`  13`  `                if (preview) preview.src = resp.url;`
`  14`  `            } else {`
`  15`  `                alert('Upload failed');`
`  16`  `            }`
`  17`  `        })`
`  18`  `        .catch(err => console.error(err));`
`  19`  `    }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `// uploader.js: Handles thumbnail and media uploads via existing ASHX endpoints`
`   2`  `(function(){`
`   3`  `    function uploadThumbnailFile(file){`
`   4`  `        const fd = new FormData();`
`   5`  `        fd.append('file', file);`
`   6`  `        fetch('UploadThumbnail.ashx', { method: 'POST', body: fd })`
  - → HTTP request to server WebMethod/ashx.
`   7`  `        .then(r => r.json())`
`   8`  `        .then(resp => {`
`   9`  `            if (resp.success) {`
`  10`  `                const bgInput = document.getElementById('txtBgImg');`
  - → Get HTML element by id.
`  11`  `                if (bgInput) bgInput.value = resp.url;`
`  12`  `                const preview = document.getElementById('courseThumbPreview') || document.getElementById('previewImg');`
  - → Get HTML element by id.
`  13`  `                if (preview) preview.src = resp.url;`
`  14`  `            } else {`
`  15`  `                alert('Upload failed');`
`  16`  `            }`
`  17`  `        })`
`  18`  `        .catch(err => console.error(err));`
`  19`  `    }`
`  20`  ``
`  21`  `    window.initDropzone = function(){`
`  22`  `        const drop = document.getElementById('dropzoneArea');`
  - → Get HTML element by id.
`  23`  `        if (!drop) return;`
`  24`  ``
`  25`  `        let fileInput = document.getElementById('fileBgImg');`
  - → Get HTML element by id.
`  26`  `        if (!fileInput) {`
`  27`  `            fileInput = document.createElement('input');`
`  28`  `            fileInput.type = 'file';`
`  29`  `            fileInput.accept = 'image/*';`
`  30`  `            fileInput.id = 'fileBgImg';`
`  31`  `            fileInput.style.display = 'none';`
`  32`  `            document.body.appendChild(fileInput);`
`  33`  `        }`
`  34`  ``
`  35`  `        drop.addEventListener('click', () => fileInput.click());`
  - → DOM event handler.
`  36`  ``
`  37`  `        drop.addEventListener('dragover', (e) => { e.preventDefault(); drop.classList.add('dragover'); });`
  - → DOM event handler.
`  38`  `        drop.addEventListener('dragleave', (e) => { drop.classList.remove('dragover'); });`
  - → DOM event handler.
`  39`  `        drop.addEventListener('drop', (e) => {`
  - → DOM event handler.
`  40`  `            e.preventDefault();`
`  41`  `            drop.classList.remove('dragover');`
`  42`  `            const f = (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]) || null;`
`  43`  `            if (f) uploadThumbnailFile(f);`
`  44`  `        });`
`  45`  ``
`  46`  `        fileInput.addEventListener('change', function(){`
  - → DOM event handler.
`  47`  `            const f = this.files[0];`
`  48`  `            if (f) uploadThumbnailFile(f);`
`  49`  `        });`
`  50`  `    };`
`  51`  ``
`  52`  `    // backward compatibility`
`  53`  `    window.initUploader = window.initDropzone;`
`  54`  `})();`

## Source snapshot (raw)

```javascript
// uploader.js: Handles thumbnail and media uploads via existing ASHX endpoints
(function(){
    function uploadThumbnailFile(file){
        const fd = new FormData();
        fd.append('file', file);
        fetch('UploadThumbnail.ashx', { method: 'POST', body: fd })
        .then(r => r.json())
        .then(resp => {
            if (resp.success) {
                const bgInput = document.getElementById('txtBgImg');
                if (bgInput) bgInput.value = resp.url;
                const preview = document.getElementById('courseThumbPreview') || document.getElementById('previewImg');
                if (preview) preview.src = resp.url;
            } else {
                alert('Upload failed');
            }
        })
        .catch(err => console.error(err));
    }

    window.initDropzone = function(){
        const drop = document.getElementById('dropzoneArea');
        if (!drop) return;

        let fileInput = document.getElementById('fileBgImg');
        if (!fileInput) {
            fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.accept = 'image/*';
            fileInput.id = 'fileBgImg';
            fileInput.style.display = 'none';
            document.body.appendChild(fileInput);
        }

        drop.addEventListener('click', () => fileInput.click());

        drop.addEventListener('dragover', (e) => { e.preventDefault(); drop.classList.add('dragover'); });
        drop.addEventListener('dragleave', (e) => { drop.classList.remove('dragover'); });
        drop.addEventListener('drop', (e) => {
            e.preventDefault();
            drop.classList.remove('dragover');
            const f = (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]) || null;
            if (f) uploadThumbnailFile(f);
        });

        fileInput.addEventListener('change', function(){
            const f = this.files[0];
            if (f) uploadThumbnailFile(f);
        });
    };

    // backward compatibility
    window.initUploader = window.initDropzone;
})();

```
