# uploader.js
**Source:** `Pages/Lecturer/Scripts/uploader.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 54
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 4:** `fd` — script-level `const`/`let`/`var` — **Holds “fd” for this scope.**
- **Line 10:** `bgInput` — script-level `const`/`let`/`var` — **Holds “bg Input” for this scope.**
- **Line 12:** `preview` — script-level `const`/`let`/`var` — **Holds “preview” for this scope.**
- **Line 22:** `drop` — script-level `const`/`let`/`var` — **Holds “drop” for this scope.**
- **Line 24:** `fileInput` — script-level `const`/`let`/`var` — **Holds “file Input” for this scope.**
- **Line 42:** `f` — script-level `const`/`let`/`var` — **Holds “f” for this scope.**

## Functions / methods (1 found)

### `uploadThumbnailFile` — lines 2–19

```javascript
function uploadThumbnailFile(file)
```

#### Explanation

- **Purpose:** Implements `uploadThumbnailFile`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters (what each means):**
- `file` — Uploaded file object or file name.
- **Local variables (what each means):**
- `fd` — Holds “fd” for this scope.  Newly constructed object.
- `bgInput` — Holds “bg Input” for this scope.  DOM element from the page.
- `preview` — Holds “preview” for this scope.  DOM element from the page.

#### Line-by-line (this function)

```javascript
   2 | 
   3 |     function uploadThumbnailFile(file){
   4 |         const fd = new FormData();
   5 |         fd.append('file', file);
   6 |         fetch('UploadThumbnail.ashx', { method: 'POST', body: fd })
   7 |         .then(r => r.json())
   8 |         .then(resp => {
   9 |             if (resp.success) {
  10 |                 const bgInput = document.getElementById('txtBgImg');
  11 |                 if (bgInput) bgInput.value = resp.url;
  12 |                 const preview = document.getElementById('courseThumbPreview') || document.getElementById('previewImg');
  13 |                 if (preview) preview.src = resp.url;
  14 |             } else {
  15 |                 alert('Upload failed');
  16 |             }
  17 |         })
  18 |         .catch(err => console.error(err));
  19 |     }
```

**Line notes** (what code + variables mean)

- **L4:** `fd` means: Holds “fd” for this scope.  Newly constructed object.
- **L6:** HTTP request to server WebMethod/ashx.
- **L10:** Get HTML element by id. | `bgInput` means: Holds “bg Input” for this scope.  DOM element from the page.
- **L12:** Get HTML element by id. | `preview` means: Holds “preview” for this scope.  DOM element from the page.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```javascript
   1 | // uploader.js: Handles thumbnail and media uploads via existing ASHX endpoints
   2 | (function(){
   3 |     function uploadThumbnailFile(file){
   4 |         const fd = new FormData();
   5 |         fd.append('file', file);
   6 |         fetch('UploadThumbnail.ashx', { method: 'POST', body: fd })
   7 |         .then(r => r.json())
   8 |         .then(resp => {
   9 |             if (resp.success) {
  10 |                 const bgInput = document.getElementById('txtBgImg');
  11 |                 if (bgInput) bgInput.value = resp.url;
  12 |                 const preview = document.getElementById('courseThumbPreview') || document.getElementById('previewImg');
  13 |                 if (preview) preview.src = resp.url;
  14 |             } else {
  15 |                 alert('Upload failed');
  16 |             }
  17 |         })
  18 |         .catch(err => console.error(err));
  19 |     }
  20 | 
  21 |     window.initDropzone = function(){
  22 |         const drop = document.getElementById('dropzoneArea');
  23 |         if (!drop) return;
  24 | 
  25 |         let fileInput = document.getElementById('fileBgImg');
  26 |         if (!fileInput) {
  27 |             fileInput = document.createElement('input');
  28 |             fileInput.type = 'file';
  29 |             fileInput.accept = 'image/*';
  30 |             fileInput.id = 'fileBgImg';
  31 |             fileInput.style.display = 'none';
  32 |             document.body.appendChild(fileInput);
  33 |         }
  34 | 
  35 |         drop.addEventListener('click', () => fileInput.click());
  36 | 
  37 |         drop.addEventListener('dragover', (e) => { e.preventDefault(); drop.classList.add('dragover'); });
  38 |         drop.addEventListener('dragleave', (e) => { drop.classList.remove('dragover'); });
  39 |         drop.addEventListener('drop', (e) => {
  40 |             e.preventDefault();
  41 |             drop.classList.remove('dragover');
  42 |             const f = (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]) || null;
  43 |             if (f) uploadThumbnailFile(f);
  44 |         });
  45 | 
  46 |         fileInput.addEventListener('change', function(){
  47 |             const f = this.files[0];
  48 |             if (f) uploadThumbnailFile(f);
  49 |         });
  50 |     };
  51 | 
  52 |     // backward compatibility
  53 |     window.initUploader = window.initDropzone;
  54 | })();
```

**Line notes** (what code + variables mean)

- **L4:** `fd` means: Holds “fd” for this scope.  Newly constructed object.
- **L6:** HTTP request to server WebMethod/ashx.
- **L10:** Get HTML element by id. | `bgInput` means: Holds “bg Input” for this scope.  DOM element from the page.
- **L12:** Get HTML element by id. | `preview` means: Holds “preview” for this scope.  DOM element from the page.
- **L22:** Get HTML element by id. | `drop` means: Holds “drop” for this scope.  DOM element from the page.
- **L25:** Get HTML element by id. | `fileInput` means: Holds “file Input” for this scope.  DOM element from the page.
- **L35:** DOM event handler.
- **L37:** DOM event handler.
- **L38:** DOM event handler.
- **L39:** DOM event handler.
- **L42:** `f` means: Holds “f” for this scope.
- **L46:** DOM event handler.
- **L47:** `f` means: Holds “f” for this scope.

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
