# uploader.js
**Source:** `Pages/Lecturer/Scripts/uploader.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 54
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `fd` | `const/let/var` | Holds “fd” for this scope. |
| `bgInput` | `const/let/var` | Holds “bg Input” for this scope. |
| `preview` | `const/let/var` | Holds “preview” for this scope. |
| `drop` | `const/let/var` | Holds “drop” for this scope. |
| `fileInput` | `const/let/var` | Holds “file Input” for this scope. |
| `f` | `const/let/var` | Holds “f” for this scope. |

## Functions / methods (1 found)

### `uploadThumbnailFile` — lines 2–19

#### Signature

```javascript
function uploadThumbnailFile(file)
```

#### What it is

Browser-side function `uploadThumbnailFile` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `file` | `—` | Uploaded file object or file name. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `fd` | `—` | Holds “fd” for this scope.  Newly constructed object. |
| `bgInput` | `—` | Holds “bg Input” for this scope.  DOM element from the page. |
| `preview` | `—` | Holds “preview” for this scope.  DOM element from the page. |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
