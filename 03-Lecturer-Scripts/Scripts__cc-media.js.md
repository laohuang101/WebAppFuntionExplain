# cc-media.js
**Source:** `Pages/Lecturer/Scripts/cc-media.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Serve files under Uploads with path sandbox + auth policy by folder.

## File overview

- **Total lines:** 411
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `dz` | `const/let/var` | Holds “dz” for this scope. |
| `fileInput` | `const/let/var` | Holds “file Input” for this scope. |
| `preview` | `const/let/var` | Holds “preview” for this scope. |
| `hiddenField` | `const/let/var` | Holds “hidden Field” for this scope. |
| `dzMsg` | `const/let/var` | Holds “dz Msg” for this scope. |
| `formData` | `const/let/var` | Holds “form Data” for this scope. |
| `file` | `const/let/var` | Uploaded file object or file name. |
| `fd` | `const/let/var` | Holds “fd” for this scope. |
| `p` | `const/let/var` | Parameter, path, or password fragment depending on context. |
| `lower` | `const/let/var` | Holds “lower” for this scope. |
| `i` | `const/let/var` | Loop index (0-based counter in for-loops). |
| `u` | `const/let/var` | Holds “u” for this scope. |
| `key` | `const/let/var` | HMAC key bytes or dictionary key. |
| `q` | `const/let/var` | Search query text, or SQL command text. |
| `a` | `const/let/var` | Holds “a” for this scope. |
| `path` | `const/let/var` | File path under Uploads or URL path. |
| `idx` | `const/let/var` | Holds “idx” for this scope. |
| `root` | `const/let/var` | Root directory path (Uploads). |
| `url` | `const/let/var` | HTTP URL to media or page. |
| `s` | `const/let/var` | String value or submission-related object. |
| `safeView` | `const/let/var` | Holds “safe View” for this scope. |
| `safeName` | `const/let/var` | Holds “safe Name” for this scope. |
| `area` | `const/let/var` | Holds “area” for this scope. |
| `input` | `const/let/var` | Holds “input” for this scope. |
| `msg` | `const/let/var` | Human-readable message (error or success). |
| `ext` | `const/let/var` | File extension (.pdf, .mp4, …). |
| `store` | `const/let/var` | Holds “store” for this scope. |
| `viewUrl` | `const/let/var` | URL string. |
| `dlUrl` | `const/let/var` | URL string. |
| `txt` | `const/let/var` | UI control reference (txt). |
| `prev` | `const/let/var` | Holds “prev” for this scope. |
| `allowed` | `const/let/var` | Boolean — path/role is permitted. |
| `maxMb` | `const/let/var` | Holds “max Mb” for this scope. |
| `materialsField` | `const/let/var` | Holds “materials Field” for this scope. |
| `materials` | `const/let/var` | Often a collection related to materials (plural name). |
| `attachments` | `const/let/var` | Often a collection related to attachments (plural name). |
| `heading` | `const/let/var` | Holds “heading” for this scope. |
| `raw` | `const/let/var` | Raw bytes or unprocessed input string. |
| `name` | `const/let/var` | Display name of user/course/criterion. |
| `kind` | `const/let/var` | Upload kind (material/video/thumbnail/submission). |
| `card` | `const/let/var` | Holds “card” for this scope. |

## Functions / methods (13 found)

### `initDropzone` — lines 2–77

#### Signature

```javascript
function initDropzone()
```

#### What it is

Browser-side function `initDropzone` — talks to the server and updates the page.

#### How it works

1. Show a simple popup message to the user.
2. Call the server with `fetch` (AJAX) and wait for the JSON result.
3. Parse the server JSON response into a JavaScript object.
4. Show a simple popup message to the user.
5. Attach a browser event handler (click, load, change, …).
6. Stop the browser’s default action (for example form submit).
7. Attach a browser event handler (click, load, change, …).
8. Stop the browser’s default action (for example form submit).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `dz` | `—` | Holds “dz” for this scope.  DOM element from the page. |
| `fileInput` | `—` | Holds “file Input” for this scope. |
| `preview` | `—` | Holds “preview” for this scope.  DOM element from the page. |
| `hiddenField` | `—` | Holds “hidden Field” for this scope.  DOM element from the page. |
| `dzMsg` | `—` | Holds “dz Msg” for this scope.  DOM element from the page. |
| `formData` | `—` | Holds “form Data” for this scope.  Newly constructed object. |
| `file` | `—` | Uploaded file object or file name. |

#### Code

```javascript
   2 | 
   3 | function initDropzone() {
   4 |     const dz = document.getElementById('dropzoneArea');
   5 |     if (!dz) return;
   6 | 
   7 |     // Create hidden file input
   8 |     let fileInput = document.createElement('input');
   9 |     fileInput.type = 'file';
  10 |     fileInput.accept = 'image/*';
  11 |     fileInput.style.display = 'none';
  12 |     dz.appendChild(fileInput);
  13 | 
  14 |     const preview = document.getElementById('courseThumbPreview');
  15 |     const hiddenField = document.getElementById('txtBgImg');
  16 |     const dzMsg = document.getElementById('dzMessage');
  17 | 
  18 |     function uploadFile(file) {
  19 |         if (!file) return;
  20 |         if (file.size > 2 * 1024 * 1024) {
  21 |             alert('File too large. Maximum allowed size is 2MB.');
  22 |             return;
  23 |         }
  24 | 
  25 |         const formData = new FormData();
  26 |         formData.append('file', file, file.name);
  27 | 
  28 |         dz.classList.add('disabled');
  29 |         dzMsg.innerText = 'Uploading...';
  30 | 
  31 |         fetch('UploadThumbnail.ashx', {
  32 |             method: 'POST',
  33 |             body: formData
  34 |         })
  35 |         .then(res => res.json())
  36 |         .then(resp => {
  37 |             if (resp.success) {
  38 |                 hiddenField.value = resp.url;
  39 |                 if (preview) {
  40 |                     preview.src = resp.url;
  41 |                     preview.classList.remove('d-none');
  42 |                 }
  43 |                 dzMsg.innerText = 'Upload successful';
  44 |             } else {
  45 |                 alert('Upload failed: ' + (resp.message || 'Unknown error'));
  46 |                 dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
  47 |             }
  48 |         })
  49 |         .catch(err => {
  50 |             console.error(err);
  51 |             alert('Upload failed.');
  52 |             dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
  53 |         })
  54 |         .finally(() => dz.classList.remove('disabled'));
  55 |     }
  56 | 
  57 |     dz.addEventListener('click', () => fileInput.click());
  58 | 
  59 |     fileInput.addEventListener('change', (e) => {
  60 |         const file = e.target.files[0];
  61 |         uploadFile(file);
  62 |     });
  63 | 
  64 |     dz.addEventListener('dragover', (e) => {
  65 |         e.preventDefault();
  66 |         dz.classList.add('border-primary');
  67 |     });
  68 |     dz.addEventListener('dragleave', (e) => {
  69 |         dz.classList.remove('border-primary');
  70 |     });
  71 |     dz.addEventListener('drop', (e) => {
  72 |         e.preventDefault();
  73 |         dz.classList.remove('border-primary');
  74 |         const file = e.dataTransfer.files[0];
  75 |         uploadFile(file);
  76 |     });
  77 | }
```

---

### `uploadFile` — lines 16–55

#### Signature

```javascript
function uploadFile(file)
```

#### What it is

Browser-side function `uploadFile` — talks to the server and updates the page.

#### How it works

1. Show a simple popup message to the user.
2. Call the server with `fetch` (AJAX) and wait for the JSON result.
3. Parse the server JSON response into a JavaScript object.
4. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `file` | `—` | Uploaded file object or file name. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `formData` | `—` | Holds “form Data” for this scope.  Newly constructed object. |

#### Code

```javascript
  16 | 
  17 | 
  18 |     function uploadFile(file) {
  19 |         if (!file) return;
  20 |         if (file.size > 2 * 1024 * 1024) {
  21 |             alert('File too large. Maximum allowed size is 2MB.');
  22 |             return;
  23 |         }
  24 | 
  25 |         const formData = new FormData();
  26 |         formData.append('file', file, file.name);
  27 | 
  28 |         dz.classList.add('disabled');
  29 |         dzMsg.innerText = 'Uploading...';
  30 | 
  31 |         fetch('UploadThumbnail.ashx', {
  32 |             method: 'POST',
  33 |             body: formData
  34 |         })
  35 |         .then(res => res.json())
  36 |         .then(resp => {
  37 |             if (resp.success) {
  38 |                 hiddenField.value = resp.url;
  39 |                 if (preview) {
  40 |                     preview.src = resp.url;
  41 |                     preview.classList.remove('d-none');
  42 |                 }
  43 |                 dzMsg.innerText = 'Upload successful';
  44 |             } else {
  45 |                 alert('Upload failed: ' + (resp.message || 'Unknown error'));
  46 |                 dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
  47 |             }
  48 |         })
  49 |         .catch(err => {
  50 |             console.error(err);
  51 |             alert('Upload failed.');
  52 |             dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
  53 |         })
  54 |         .finally(() => dz.classList.remove('disabled'));
  55 |     }
```

---

### `uploadLessonFile` — lines 81–99

#### Signature

```javascript
function uploadLessonFile(file)
```

#### What it is

Browser-side function `uploadLessonFile` — talks to the server and updates the page.

#### How it works

1. Call the server with `fetch` (AJAX) and wait for the JSON result.
2. Parse the server JSON response into a JavaScript object.
3. Stop with an error (invalid access or bad input).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `file` | `—` | Uploaded file object or file name. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `fd` | `—` | Holds “fd” for this scope.  Newly constructed object. |

#### Code

```javascript
  81 | 
  82 | function uploadLessonFile(file) {
  83 |     var fd = new FormData();
  84 |     fd.append('file', file, file.name);
  85 |     return fetch('UploadMedia.ashx', {
  86 |         method: 'POST',
  87 |         body: fd,
  88 |         credentials: 'same-origin'
  89 |     }).then(function (r) {
  90 |         return r.text().then(function (text) {
  91 |             try {
  92 |                 return JSON.parse(text);
  93 |             } catch (e) {
  94 |                 console.error('UploadMedia non-JSON response:', text);
  95 |                 throw new Error('Upload failed (server returned non-JSON). Check you are logged in and UploadMedia.ashx is reachable.');
  96 |             }
  97 |         });
  98 |     });
  99 | }
```

---

### `mediaAppRoot` — lines 101–109

#### Signature

```javascript
function mediaAppRoot()
```

#### What it is

Function `mediaAppRoot` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `mediaAppRoot`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `p` | `—` | Parameter, path, or password fragment depending on context. |
| `lower` | `—` | Holds “lower” for this scope. |
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Code

```javascript
 101 | 
 102 | function mediaAppRoot() {
 103 |     var p = window.location.pathname || '';
 104 |     var lower = p.toLowerCase();
 105 |     var i = lower.indexOf('/pages/');
 106 |     if (i > 0) return p.substring(0, i);
 107 |     // site at root → ""
 108 |     return '';
 109 | }
```

---

### `resolveMediaUrl` — lines 114–143

#### Signature

```javascript
function resolveMediaUrl(raw, forDownload)
```

#### What it is

Function `resolveMediaUrl` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `resolveMediaUrl`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `raw` | `—` | Raw bytes or unprocessed input string. |
| `forDownload` | `—` | Holds “for Download” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `u` | `—` | Holds “u” for this scope. |
| `key` | `—` | HMAC key bytes or dictionary key. |
| `q` | `—` | Search query text, or SQL command text. |
| `a` | `—` | Holds “a” for this scope. |

#### Code

```javascript
 114 | 
 115 | function resolveMediaUrl(raw, forDownload) {
 116 |     if (!raw) return '';
 117 |     var u = String(raw).trim();
 118 | 
 119 |     // External non-upload URLs
 120 |     if (/^https?:\/\//i.test(u) &&
 121 |     u.indexOf('/Uploads/') < 0 && u.indexOf('Uploads/') < 0 &&
 122 |     u.indexOf('Media.ashx') < 0 && u.indexOf('ServeUpload') < 0) {
 123 |         return u;
 124 |     }
 125 | 
 126 |     // Already Media.ashx / ServeUpload - normalize to Media.ashx
 127 |     if (u.indexOf('Media.ashx') >= 0 || u.indexOf('ServeUpload') >= 0) {
 128 |         try {
 129 |             var key = u.indexOf('f=') >= 0 ? 'f=' : (u.indexOf('path=') >= 0 ? 'path=' : null);
 130 |             if (key) {
 131 |                 var q = u.split(key)[1];
 132 |                 if (q) return resolveMediaUrl(decodeURIComponent(q.split('&')[0]), forDownload);
 133 |             }
 134 |         } catch (e) { }
 135 |     }
 136 | 
 137 |     try {
 138 |         if (/^https?:\/\//i.test(u)) {
 139 |         var a = document.createElement('a');
 140 |         a.href = u;
 141 |         u = a.pathname || u;
 142 |     }
 143 | }
```

---

### `mediaKind` — lines 161–170

#### Signature

```javascript
function mediaKind(urlOrName)
```

#### What it is

Function `mediaKind` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `mediaKind`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `urlOrName` | `—` | URL string. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `s` | `—` | String value or submission-related object. |

#### Code

```javascript
 161 | 
 162 | 
 163 | function mediaKind(urlOrName) {
 164 |     var s = (urlOrName || '').toLowerCase();
 165 |     if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';
 166 |     if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';
 167 |     if (/\.pdf(\?|$)/.test(s)) return 'pdf';
 168 |     if (/\.(pptx?|docx?|pptm)(\?|$)/.test(s)) return 'office';
 169 |     return 'file';
 170 | }
```

---

### `buildMaterialPreviewHtml` — lines 170–191

#### Signature

```javascript
function buildMaterialPreviewHtml(viewUrl, kind, fileName)
```

#### What it is

Creates/builds **build Material Preview Html** (object, string, secret, or UI content).

#### How it works

1. Starts when something calls `buildMaterialPreviewHtml`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `viewUrl` | `—` | URL string. |
| `kind` | `—` | Upload kind (material/video/thumbnail/submission). |
| `fileName` | `—` | Original file name for display/download. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `safeView` | `—` | Holds “safe View” for this scope. |
| `safeName` | `—` | Holds “safe Name” for this scope. |

#### Code

```javascript
 170 | 
 171 | 
 172 | function buildMaterialPreviewHtml(viewUrl, kind, fileName) {
 173 |     var safeView = escapeHtml(viewUrl);
 174 |     var safeName = escapeHtml(fileName || 'file');
 175 |     if (kind === 'video') {
 176 |         return '<video controls preload="metadata" src="' + safeView +
 177 |         '" style="max-width:100%;max-height:200px;display:block;border-radius:8px;background:#111;"></video>';
 178 |     }
 179 |     if (kind === 'image') {
 180 |         return '<a href="' + safeView + '" target="_blank" rel="noopener">' +
 181 |         '<img src="' + safeView + '" alt="' + safeName +
 182 |         '" style="max-width:100%;max-height:180px;border-radius:8px;object-fit:contain;background:#f3f4f6;" /></a>';
 183 |     }
 184 |     if (kind === 'pdf') {
 185 |         return '<iframe src="' + safeView +
 186 |         '#toolbar=1" title="' + safeName +
 187 |         '" style="width:100%;height:220px;border:1px solid #e5e7eb;border-radius:8px;background:#fff;"></iframe>';
 188 |     }
 189 |     return '<div class="text-muted small py-2"><i class="fa-solid fa-file me-1"></i>' + safeName +
 190 |     ' - use Open / Download</div>';
 191 | }
```

---

### `initMediaDropzone` — lines 191–275

#### Signature

```javascript
function initMediaDropzone()
```

#### What it is

Function `initMediaDropzone` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Show a simple popup message to the user.
2. Attach a browser event handler (click, load, change, …).
3. Stop the browser’s default action (for example form submit).
4. Attach a browser event handler (click, load, change, …).
5. Stop the browser’s default action (for example form submit).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `area` | `—` | Holds “area” for this scope.  DOM element from the page. |
| `input` | `—` | Holds “input” for this scope.  DOM element from the page. |
| `msg` | `—` | Human-readable message (error or success). |
| `ext` | `—` | File extension (.pdf, .mp4, …). |
| `store` | `—` | Holds “store” for this scope. |
| `viewUrl` | `—` | URL string. |
| `dlUrl` | `—` | URL string. |
| `txt` | `—` | UI control reference (txt).  DOM element from the page. |
| `prev` | `—` | Holds “prev” for this scope.  DOM element from the page. |

#### Code

```javascript
 191 | 
 192 | 
 193 | function initMediaDropzone() {
 194 |     var area = document.getElementById('mediaDropzone');
 195 |     if (!area) return;
 196 |     var input = document.getElementById('mediaFileInput');
 197 |     if (!input) {
 198 |         input = document.createElement('input');
 199 |         input.type = 'file';
 200 |         input.id = 'mediaFileInput';
 201 |         input.accept = 'video/*,.mp4,.webm,.mov';
 202 |         input.style.display = 'none';
 203 |         area.appendChild(input);
 204 |     }
 205 |     var msg = area.querySelector('.dz-inner');
 206 |     if (!msg) {
 207 |         msg = document.createElement('div');
 208 |         msg.className = 'dz-inner text-muted small';
 209 |         msg.innerText = 'Click to upload video (mp4/webm/mov)';
 210 |         area.appendChild(msg);
 211 |     }
 212 | 
 213 |     function uploadVideo(file) {
 214 |         if (!file) return;
 215 |         var ext = (file.name.split('.').pop() || '').toLowerCase();
 216 |         if (['mp4', 'webm', 'mov'].indexOf(ext) < 0) {
 217 |             alert('Unsupported video format. Use mp4, webm, or mov.');
 218 |             return;
 219 |         }
 220 |         if (file.size > 200 * 1024 * 1024) {
 221 |             alert('Video too large (max 200MB).');
 222 |             return;
 223 |         }
 224 |         msg.innerText = 'Uploading ' + file.name + '...';
 225 |         uploadLessonFile(file)
 226 |         .then(function (resp) {
 227 |             if (resp && resp.success) {
 228 |                 var store = resp.storePath || resp.under || resp.url;
 229 |                 var viewUrl = resp.serveUrl || resolveMediaUrl(store, false);
 230 |                 var dlUrl = resp.downloadUrl || resolveMediaUrl(store, true);
 231 |                 var txt = document.getElementById('txtLessonContent');
 232 |                 if (txt) {
 233 |                     // store portable path for DB (Uploads/CourseVideos/...)
 234 |                     txt.value = store;
 235 |                     txt.classList.remove('d-none');
 236 |                 }
 237 |                 msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
 238 |                 escapeHtml(resp.fileName || file.name) + ' (' + (resp.size || file.size) + ' bytes)</span>';
 239 |                 var prev = document.getElementById('lessonMediaPreview');
 240 |                 if (prev) {
 241 |                     prev.innerHTML = buildMaterialPreviewHtml(viewUrl, 'video', resp.fileName || file.name) +
 242 |                     '<div class="mt-1"><a class="small" href="' + escapeHtml(viewUrl) + '" target="_blank">Open</a>' +
 243 |                     ' · <a class="small" href="' + escapeHtml(dlUrl) + '">Download</a></div>' +
 244 |                     '<div class="hint text-muted" style="font-size:.75rem;word-break:break-all;">' + escapeHtml(viewUrl) + '</div>';
 245 |                     prev.classList.remove('d-none');
 246 |                 }
 247 |             } else {
 248 |                 alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
 249 |                 msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
 250 |             }
 251 |         })
 252 |         .catch(function (err) {
 253 |             console.error(err);
 254 |             alert(err.message || 'Upload failed');
 255 |             msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
 256 |         });
 257 |     }
 258 | 
 259 |     area.addEventListener('click', function (e) {
 260 |         if (e.target === input) return;
 261 |         e.preventDefault();
 262 |         input.click();
 263 |     });
 264 |     input.addEventListener('change', function () {
 265 |         if (input.files && input.files[0]) uploadVideo(input.files[0]);
 266 |         input.value = '';
 267 |     });
 268 |     area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });
 269 |     area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });
 270 |     area.addEventListener('drop', function (e) {
 271 |         e.preventDefault();
 272 |         area.classList.remove('dragover');
 273 |         if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadVideo(e.dataTransfer.files[0]);
 274 |     });
 275 | }
```

---

### `uploadVideo` — lines 211–257

#### Signature

```javascript
function uploadVideo(file)
```

#### What it is

Function `uploadVideo` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `file` | `—` | Uploaded file object or file name. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `ext` | `—` | File extension (.pdf, .mp4, …). |
| `store` | `—` | Holds “store” for this scope. |
| `viewUrl` | `—` | URL string. |
| `dlUrl` | `—` | URL string. |
| `txt` | `—` | UI control reference (txt).  DOM element from the page. |
| `prev` | `—` | Holds “prev” for this scope.  DOM element from the page. |

#### Code

```javascript
 211 | 
 212 | 
 213 |     function uploadVideo(file) {
 214 |         if (!file) return;
 215 |         var ext = (file.name.split('.').pop() || '').toLowerCase();
 216 |         if (['mp4', 'webm', 'mov'].indexOf(ext) < 0) {
 217 |             alert('Unsupported video format. Use mp4, webm, or mov.');
 218 |             return;
 219 |         }
 220 |         if (file.size > 200 * 1024 * 1024) {
 221 |             alert('Video too large (max 200MB).');
 222 |             return;
 223 |         }
 224 |         msg.innerText = 'Uploading ' + file.name + '...';
 225 |         uploadLessonFile(file)
 226 |         .then(function (resp) {
 227 |             if (resp && resp.success) {
 228 |                 var store = resp.storePath || resp.under || resp.url;
 229 |                 var viewUrl = resp.serveUrl || resolveMediaUrl(store, false);
 230 |                 var dlUrl = resp.downloadUrl || resolveMediaUrl(store, true);
 231 |                 var txt = document.getElementById('txtLessonContent');
 232 |                 if (txt) {
 233 |                     // store portable path for DB (Uploads/CourseVideos/...)
 234 |                     txt.value = store;
 235 |                     txt.classList.remove('d-none');
 236 |                 }
 237 |                 msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
 238 |                 escapeHtml(resp.fileName || file.name) + ' (' + (resp.size || file.size) + ' bytes)</span>';
 239 |                 var prev = document.getElementById('lessonMediaPreview');
 240 |                 if (prev) {
 241 |                     prev.innerHTML = buildMaterialPreviewHtml(viewUrl, 'video', resp.fileName || file.name) +
 242 |                     '<div class="mt-1"><a class="small" href="' + escapeHtml(viewUrl) + '" target="_blank">Open</a>' +
 243 |                     ' · <a class="small" href="' + escapeHtml(dlUrl) + '">Download</a></div>' +
 244 |                     '<div class="hint text-muted" style="font-size:.75rem;word-break:break-all;">' + escapeHtml(viewUrl) + '</div>';
 245 |                     prev.classList.remove('d-none');
 246 |                 }
 247 |             } else {
 248 |                 alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
 249 |                 msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
 250 |             }
 251 |         })
 252 |         .catch(function (err) {
 253 |             console.error(err);
 254 |             alert(err.message || 'Upload failed');
 255 |             msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
 256 |         });
 257 |     }
```

---

### `initMaterialDropzone` — lines 275–358

#### Signature

```javascript
function initMaterialDropzone()
```

#### What it is

Function `initMaterialDropzone` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Show a simple popup message to the user.
2. Parse the server JSON response into a JavaScript object.
3. Convert a JavaScript object into a JSON string for the server.
4. Show a simple popup message to the user.
5. Attach a browser event handler (click, load, change, …).
6. Stop the browser’s default action (for example form submit).
7. Attach a browser event handler (click, load, change, …).
8. Stop the browser’s default action (for example form submit).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `area` | `—` | Holds “area” for this scope.  DOM element from the page. |
| `input` | `—` | Holds “input” for this scope.  DOM element from the page. |
| `msg` | `—` | Human-readable message (error or success). |
| `allowed` | `—` | Boolean — path/role is permitted. |
| `ext` | `—` | File extension (.pdf, .mp4, …). |
| `maxMb` | `—` | Holds “max Mb” for this scope. |
| `materialsField` | `—` | Holds “materials Field” for this scope.  DOM element from the page. |
| `materials` | `—` | Often a collection related to materials (plural name). |
| `store` | `—` | Holds “store” for this scope. |

#### Code

```javascript
 275 | 
 276 | 
 277 | function initMaterialDropzone() {
 278 |     var area = document.getElementById('materialDropzone');
 279 |     if (!area) return;
 280 |     var input = document.getElementById('materialFileInput');
 281 |     if (!input) {
 282 |         input = document.createElement('input');
 283 |         input.type = 'file';
 284 |         input.id = 'materialFileInput';
 285 |         input.accept = '.pdf,.ppt,.pptx,.docx,image/*,video/*,.mp4,.webm';
 286 |         input.style.display = 'none';
 287 |         area.appendChild(input);
 288 |     }
 289 |     var msg = area.querySelector('.dz-inner');
 290 |     if (!msg) {
 291 |         msg = document.createElement('div');
 292 |         msg.className = 'dz-inner text-muted small';
 293 |         msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 294 |         area.appendChild(msg);
 295 |     }
 296 | 
 297 |     function uploadMaterial(file) {
 298 |         if (!file) return;
 299 |         var allowed = ['pdf', 'ppt', 'pptx', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'mov'];
 300 |         var ext = (file.name.split('.').pop() || '').toLowerCase();
 301 |         if (allowed.indexOf(ext) < 0) {
 302 |             alert('Unsupported file format: .' + ext);
 303 |             return;
 304 |         }
 305 |         var maxMb = (ext === 'mp4' || ext === 'webm' || ext === 'mov') ? 200 : 30;
 306 |         if (file.size > maxMb * 1024 * 1024) {
 307 |             alert('File too large (max ' + maxMb + 'MB).');
 308 |             return;
 309 |         }
 310 |         msg.innerText = 'Uploading ' + file.name + '...';
 311 |         uploadLessonFile(file)
 312 |         .then(function (resp) {
 313 |             if (resp && resp.success) {
 314 |                 var materialsField = document.getElementById('lessonMaterials');
 315 |                 var materials = [];
 316 |                 try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
 317 |                 var store = resp.storePath || ('Uploads/' + (resp.under || ''));
 318 |                 materials.push({
 319 |                     storePath: store,
 320 |                     url: store,
 321 |                     under: resp.under || '',
 322 |                     fileName: resp.fileName || file.name,
 323 |                     serveUrl: resp.serveUrl || resolveMediaUrl(store, false),
 324 |                     downloadUrl: resp.downloadUrl || resolveMediaUrl(store, true)
 325 |                 });
 326 |                 materialsField.value = JSON.stringify(materials);
 327 |                 renderAttachmentsList();
 328 |                 msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
 329 |                 escapeHtml(resp.fileName || file.name) + ' - preview below</span>';
 330 |             } else {
 331 |                 alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
 332 |                 msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 333 |             }
 334 |         })
 335 |         .catch(function (err) {
 336 |             console.error(err);
 337 |             alert(err.message || 'Upload failed');
 338 |             msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 339 |         });
 340 |     }
 341 | 
 342 |     area.addEventListener('click', function (e) {
 343 |         if (e.target === input) return;
 344 |         e.preventDefault();
 345 |         input.click();
 346 |     });
 347 |     input.addEventListener('change', function () {
 348 |         if (input.files && input.files[0]) uploadMaterial(input.files[0]);
 349 |         input.value = '';
 350 |     });
 351 |     area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });
 352 |     area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });
 353 |     area.addEventListener('drop', function (e) {
 354 |         e.preventDefault();
 355 |         area.classList.remove('dragover');
 356 |         if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadMaterial(e.dataTransfer.files[0]);
 357 |     });
 358 | }
```

---

### `uploadMaterial` — lines 295–340

#### Signature

```javascript
function uploadMaterial(file)
```

#### What it is

Function `uploadMaterial` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Show a simple popup message to the user.
2. Parse the server JSON response into a JavaScript object.
3. Convert a JavaScript object into a JSON string for the server.
4. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `file` | `—` | Uploaded file object or file name. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `allowed` | `—` | Boolean — path/role is permitted. |
| `ext` | `—` | File extension (.pdf, .mp4, …). |
| `maxMb` | `—` | Holds “max Mb” for this scope. |
| `materialsField` | `—` | Holds “materials Field” for this scope.  DOM element from the page. |
| `materials` | `—` | Often a collection related to materials (plural name). |
| `store` | `—` | Holds “store” for this scope. |

#### Code

```javascript
 295 | 
 296 | 
 297 |     function uploadMaterial(file) {
 298 |         if (!file) return;
 299 |         var allowed = ['pdf', 'ppt', 'pptx', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'mov'];
 300 |         var ext = (file.name.split('.').pop() || '').toLowerCase();
 301 |         if (allowed.indexOf(ext) < 0) {
 302 |             alert('Unsupported file format: .' + ext);
 303 |             return;
 304 |         }
 305 |         var maxMb = (ext === 'mp4' || ext === 'webm' || ext === 'mov') ? 200 : 30;
 306 |         if (file.size > maxMb * 1024 * 1024) {
 307 |             alert('File too large (max ' + maxMb + 'MB).');
 308 |             return;
 309 |         }
 310 |         msg.innerText = 'Uploading ' + file.name + '...';
 311 |         uploadLessonFile(file)
 312 |         .then(function (resp) {
 313 |             if (resp && resp.success) {
 314 |                 var materialsField = document.getElementById('lessonMaterials');
 315 |                 var materials = [];
 316 |                 try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
 317 |                 var store = resp.storePath || ('Uploads/' + (resp.under || ''));
 318 |                 materials.push({
 319 |                     storePath: store,
 320 |                     url: store,
 321 |                     under: resp.under || '',
 322 |                     fileName: resp.fileName || file.name,
 323 |                     serveUrl: resp.serveUrl || resolveMediaUrl(store, false),
 324 |                     downloadUrl: resp.downloadUrl || resolveMediaUrl(store, true)
 325 |                 });
 326 |                 materialsField.value = JSON.stringify(materials);
 327 |                 renderAttachmentsList();
 328 |                 msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
 329 |                 escapeHtml(resp.fileName || file.name) + ' - preview below</span>';
 330 |             } else {
 331 |                 alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
 332 |                 msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 333 |             }
 334 |         })
 335 |         .catch(function (err) {
 336 |             console.error(err);
 337 |             alert(err.message || 'Upload failed');
 338 |             msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 339 |         });
 340 |     }
```

---

### `renderAttachmentsList` — lines 358–398

#### Signature

```javascript
function renderAttachmentsList()
```

#### What it is

Updates the page HTML for **render Attachments List**.

#### How it works

1. Parse the server JSON response into a JavaScript object.
2. Attach a browser event handler (click, load, change, …).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `attachments` | `—` | Often a collection related to attachments (plural name).  DOM element from the page. |
| `materialsField` | `—` | Holds “materials Field” for this scope.  DOM element from the page. |
| `materials` | `—` | Often a collection related to materials (plural name). |
| `heading` | `—` | Holds “heading” for this scope. |
| `raw` | `—` | Raw bytes or unprocessed input string. |
| `viewUrl` | `—` | URL string. |
| `dlUrl` | `—` | URL string. |
| `name` | `—` | Display name of user/course/criterion. |
| `kind` | `—` | Upload kind (material/video/thumbnail/submission). |
| `card` | `—` | Holds “card” for this scope. |

#### Code

```javascript
 358 | 
 359 | 
 360 | function renderAttachmentsList() {
 361 |     var attachments = document.getElementById('lessonAttachments');
 362 |     var materialsField = document.getElementById('lessonMaterials');
 363 |     if (!attachments || !materialsField) return;
 364 |     attachments.innerHTML = '';
 365 |     var materials = [];
 366 |     try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
 367 |     if (!materials.length) return;
 368 | 
 369 |     var heading = document.createElement('div');
 370 |     heading.className = 'fw-semibold small text-muted mb-2';
 371 |     heading.textContent = 'Materials (' + materials.length + ') - preview & download';
 372 |     attachments.appendChild(heading);
 373 | 
 374 |     materials.forEach(function (m, idx) {
 375 |         var raw = m.url || m.mediaLink || '';
 376 |         var viewUrl = m.serveUrl || resolveMediaUrl(raw, false);
 377 |         var dlUrl = m.downloadUrl || resolveMediaUrl(raw, true);
 378 |         var name = m.fileName || m.textContent || raw || ('File ' + (idx + 1));
 379 |         var kind = mediaKind(name + ' ' + raw);
 380 | 
 381 |         var card = document.createElement('div');
 382 |         card.className = 'mb-2 p-2 rounded border bg-white';
 383 |         card.innerHTML =
 384 |         '<div class="d-flex align-items-center gap-2 mb-2">' +
 385 |         '<i class="fa-solid fa-paperclip text-muted"></i>' +
 386 |         '<span class="small flex-grow-1 text-truncate fw-semibold">' + escapeHtml(name) + '</span>' +
 387 |         '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeHtml(viewUrl) + '" target="_blank" rel="noopener">Open</a>' +
 388 |         '<a class="btn btn-sm btn-outline-primary py-0" href="' + escapeHtml(dlUrl) + '" download>Download</a>' +
 389 |         '<button type="button" class="btn btn-sm btn-link text-danger p-0" data-rm="' + idx + '">Remove</button>' +
 390 |         '</div>' +
 391 |         '<div class="material-preview">' + buildMaterialPreviewHtml(viewUrl, kind, name) + '</div>';
 392 | 
 393 |         card.querySelector('[data-rm]').addEventListener('click', function () {
 394 |             removeAttachment(raw || m.url);
 395 |         });
 396 |         attachments.appendChild(card);
 397 |     });
 398 | }
```

---

### `removeAttachment` — lines 398–410

#### Signature

```javascript
function removeAttachment(url)
```

#### What it is

Deletes or clears **remove Attachment** (data or temporary state).

#### How it works

1. Parse the server JSON response into a JavaScript object.
2. Convert a JavaScript object into a JSON string for the server.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `url` | `—` | HTTP URL to media or page. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `materialsField` | `—` | Holds “materials Field” for this scope.  DOM element from the page. |
| `materials` | `—` | Often a collection related to materials (plural name). |

#### Code

```javascript
 398 | 
 399 | 
 400 | function removeAttachment(url) {
 401 |     var materialsField = document.getElementById('lessonMaterials');
 402 |     if (!materialsField) return;
 403 |     var materials = [];
 404 |     try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
 405 |     materials = materials.filter(function (m) {
 406 |         return (m.url !== url) && (m.mediaLink !== url);
 407 |     });
 408 |     materialsField.value = JSON.stringify(materials);
 409 |     renderAttachmentsList();
 410 | }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | // Course Creation — media / materials dropzones
   2 | // depends on: cc-core.js
   3 | function initDropzone() {
   4 |     const dz = document.getElementById('dropzoneArea');
   5 |     if (!dz) return;
   6 | 
   7 |     // Create hidden file input
   8 |     let fileInput = document.createElement('input');
   9 |     fileInput.type = 'file';
  10 |     fileInput.accept = 'image/*';
  11 |     fileInput.style.display = 'none';
  12 |     dz.appendChild(fileInput);
  13 | 
  14 |     const preview = document.getElementById('courseThumbPreview');
  15 |     const hiddenField = document.getElementById('txtBgImg');
  16 |     const dzMsg = document.getElementById('dzMessage');
  17 | 
  18 |     function uploadFile(file) {
  19 |         if (!file) return;
  20 |         if (file.size > 2 * 1024 * 1024) {
  21 |             alert('File too large. Maximum allowed size is 2MB.');
  22 |             return;
  23 |         }
  24 | 
  25 |         const formData = new FormData();
  26 |         formData.append('file', file, file.name);
  27 | 
  28 |         dz.classList.add('disabled');
  29 |         dzMsg.innerText = 'Uploading...';
  30 | 
  31 |         fetch('UploadThumbnail.ashx', {
  32 |             method: 'POST',
  33 |             body: formData
  34 |         })
  35 |         .then(res => res.json())
  36 |         .then(resp => {
  37 |             if (resp.success) {
  38 |                 hiddenField.value = resp.url;
  39 |                 if (preview) {
  40 |                     preview.src = resp.url;
  41 |                     preview.classList.remove('d-none');
  42 |                 }
  43 |                 dzMsg.innerText = 'Upload successful';
  44 |             } else {
  45 |                 alert('Upload failed: ' + (resp.message || 'Unknown error'));
  46 |                 dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
  47 |             }
  48 |         })
  49 |         .catch(err => {
  50 |             console.error(err);
  51 |             alert('Upload failed.');
  52 |             dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
  53 |         })
  54 |         .finally(() => dz.classList.remove('disabled'));
  55 |     }
  56 | 
  57 |     dz.addEventListener('click', () => fileInput.click());
  58 | 
  59 |     fileInput.addEventListener('change', (e) => {
  60 |         const file = e.target.files[0];
  61 |         uploadFile(file);
  62 |     });
  63 | 
  64 |     dz.addEventListener('dragover', (e) => {
  65 |         e.preventDefault();
  66 |         dz.classList.add('border-primary');
  67 |     });
  68 |     dz.addEventListener('dragleave', (e) => {
  69 |         dz.classList.remove('border-primary');
  70 |     });
  71 |     dz.addEventListener('drop', (e) => {
  72 |         e.preventDefault();
  73 |         dz.classList.remove('border-primary');
  74 |         const file = e.dataTransfer.files[0];
  75 |         uploadFile(file);
  76 |     });
  77 | }
  78 | 
  79 | 
  80 | 
  81 | /** Upload a file to UploadMedia.ashx; returns Promise<{success,url,fileName,serveUrl,downloadUrl}> */
  82 | function uploadLessonFile(file) {
  83 |     var fd = new FormData();
  84 |     fd.append('file', file, file.name);
  85 |     return fetch('UploadMedia.ashx', {
  86 |         method: 'POST',
  87 |         body: fd,
  88 |         credentials: 'same-origin'
  89 |     }).then(function (r) {
  90 |         return r.text().then(function (text) {
  91 |             try {
  92 |                 return JSON.parse(text);
  93 |             } catch (e) {
  94 |                 console.error('UploadMedia non-JSON response:', text);
  95 |                 throw new Error('Upload failed (server returned non-JSON). Check you are logged in and UploadMedia.ashx is reachable.');
  96 |             }
  97 |         });
  98 |     });
  99 | }
 100 | 
 101 | /** App virtual root: "" or "/MyApp" (never ends with /) */
 102 | function mediaAppRoot() {
 103 |     var p = window.location.pathname || '';
 104 |     var lower = p.toLowerCase();
 105 |     var i = lower.indexOf('/pages/');
 106 |     if (i > 0) return p.substring(0, i);
 107 |     // site at root → ""
 108 |     return '';
 109 | }
 110 | 
 111 | /**
 112 | * Resolve stored media to /Media.ashx?f=CourseMaterials/file.ext
 113 | * This is the only reliable way under IIS Express (static /Uploads often 404s).
 114 | */
 115 | function resolveMediaUrl(raw, forDownload) {
 116 |     if (!raw) return '';
 117 |     var u = String(raw).trim();
 118 | 
 119 |     // External non-upload URLs
 120 |     if (/^https?:\/\//i.test(u) &&
 121 |     u.indexOf('/Uploads/') < 0 && u.indexOf('Uploads/') < 0 &&
 122 |     u.indexOf('Media.ashx') < 0 && u.indexOf('ServeUpload') < 0) {
 123 |         return u;
 124 |     }
 125 | 
 126 |     // Already Media.ashx / ServeUpload - normalize to Media.ashx
 127 |     if (u.indexOf('Media.ashx') >= 0 || u.indexOf('ServeUpload') >= 0) {
 128 |         try {
 129 |             var key = u.indexOf('f=') >= 0 ? 'f=' : (u.indexOf('path=') >= 0 ? 'path=' : null);
 130 |             if (key) {
 131 |                 var q = u.split(key)[1];
 132 |                 if (q) return resolveMediaUrl(decodeURIComponent(q.split('&')[0]), forDownload);
 133 |             }
 134 |         } catch (e) { }
 135 |     }
 136 | 
 137 |     try {
 138 |         if (/^https?:\/\//i.test(u)) {
 139 |         var a = document.createElement('a');
 140 |         a.href = u;
 141 |         u = a.pathname || u;
 142 |     }
 143 | } catch (e) { /* ignore */ }
 144 | 
 145 | var path = u.replace(/\\/g, '/');
 146 | var idx = path.toLowerCase().indexOf('/uploads/');
 147 | if (idx >= 0) path = path.substring(idx + 1); // Uploads/...
 148 | if (path.indexOf('~/') === 0) path = path.substring(2);
 149 | path = path.replace(/^\/+/, '');
 150 | if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);
 151 | 
 152 | // path is now CourseMaterials/guid.pdf or CourseVideos/...
 153 | if (!path) return '';
 154 | // If only a bare filename slipped in, assume CourseMaterials
 155 | if (path.indexOf('/') < 0) path = 'CourseMaterials/' + path;
 156 | 
 157 | var root = mediaAppRoot();
 158 | var url = root + '/Media.ashx?f=' + encodeURIComponent(path);
 159 | if (forDownload) url += '&dl=1';
 160 | return url;
 161 | }
 162 | 
 163 | function mediaKind(urlOrName) {
 164 |     var s = (urlOrName || '').toLowerCase();
 165 |     if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';
 166 |     if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';
 167 |     if (/\.pdf(\?|$)/.test(s)) return 'pdf';
 168 |     if (/\.(pptx?|docx?|pptm)(\?|$)/.test(s)) return 'office';
 169 |     return 'file';
 170 | }
 171 | 
 172 | function buildMaterialPreviewHtml(viewUrl, kind, fileName) {
 173 |     var safeView = escapeHtml(viewUrl);
 174 |     var safeName = escapeHtml(fileName || 'file');
 175 |     if (kind === 'video') {
 176 |         return '<video controls preload="metadata" src="' + safeView +
 177 |         '" style="max-width:100%;max-height:200px;display:block;border-radius:8px;background:#111;"></video>';
 178 |     }
 179 |     if (kind === 'image') {
 180 |         return '<a href="' + safeView + '" target="_blank" rel="noopener">' +
 181 |         '<img src="' + safeView + '" alt="' + safeName +
 182 |         '" style="max-width:100%;max-height:180px;border-radius:8px;object-fit:contain;background:#f3f4f6;" /></a>';
 183 |     }
 184 |     if (kind === 'pdf') {
 185 |         return '<iframe src="' + safeView +
 186 |         '#toolbar=1" title="' + safeName +
 187 |         '" style="width:100%;height:220px;border:1px solid #e5e7eb;border-radius:8px;background:#fff;"></iframe>';
 188 |     }
 189 |     return '<div class="text-muted small py-2"><i class="fa-solid fa-file me-1"></i>' + safeName +
 190 |     ' - use Open / Download</div>';
 191 | }
 192 | 
 193 | function initMediaDropzone() {
 194 |     var area = document.getElementById('mediaDropzone');
 195 |     if (!area) return;
 196 |     var input = document.getElementById('mediaFileInput');
 197 |     if (!input) {
 198 |         input = document.createElement('input');
 199 |         input.type = 'file';
 200 |         input.id = 'mediaFileInput';
 201 |         input.accept = 'video/*,.mp4,.webm,.mov';
 202 |         input.style.display = 'none';
 203 |         area.appendChild(input);
 204 |     }
 205 |     var msg = area.querySelector('.dz-inner');
 206 |     if (!msg) {
 207 |         msg = document.createElement('div');
 208 |         msg.className = 'dz-inner text-muted small';
 209 |         msg.innerText = 'Click to upload video (mp4/webm/mov)';
 210 |         area.appendChild(msg);
 211 |     }
 212 | 
 213 |     function uploadVideo(file) {
 214 |         if (!file) return;
 215 |         var ext = (file.name.split('.').pop() || '').toLowerCase();
 216 |         if (['mp4', 'webm', 'mov'].indexOf(ext) < 0) {
 217 |             alert('Unsupported video format. Use mp4, webm, or mov.');
 218 |             return;
 219 |         }
 220 |         if (file.size > 200 * 1024 * 1024) {
 221 |             alert('Video too large (max 200MB).');
 222 |             return;
 223 |         }
 224 |         msg.innerText = 'Uploading ' + file.name + '...';
 225 |         uploadLessonFile(file)
 226 |         .then(function (resp) {
 227 |             if (resp && resp.success) {
 228 |                 var store = resp.storePath || resp.under || resp.url;
 229 |                 var viewUrl = resp.serveUrl || resolveMediaUrl(store, false);
 230 |                 var dlUrl = resp.downloadUrl || resolveMediaUrl(store, true);
 231 |                 var txt = document.getElementById('txtLessonContent');
 232 |                 if (txt) {
 233 |                     // store portable path for DB (Uploads/CourseVideos/...)
 234 |                     txt.value = store;
 235 |                     txt.classList.remove('d-none');
 236 |                 }
 237 |                 msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
 238 |                 escapeHtml(resp.fileName || file.name) + ' (' + (resp.size || file.size) + ' bytes)</span>';
 239 |                 var prev = document.getElementById('lessonMediaPreview');
 240 |                 if (prev) {
 241 |                     prev.innerHTML = buildMaterialPreviewHtml(viewUrl, 'video', resp.fileName || file.name) +
 242 |                     '<div class="mt-1"><a class="small" href="' + escapeHtml(viewUrl) + '" target="_blank">Open</a>' +
 243 |                     ' · <a class="small" href="' + escapeHtml(dlUrl) + '">Download</a></div>' +
 244 |                     '<div class="hint text-muted" style="font-size:.75rem;word-break:break-all;">' + escapeHtml(viewUrl) + '</div>';
 245 |                     prev.classList.remove('d-none');
 246 |                 }
 247 |             } else {
 248 |                 alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
 249 |                 msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
 250 |             }
 251 |         })
 252 |         .catch(function (err) {
 253 |             console.error(err);
 254 |             alert(err.message || 'Upload failed');
 255 |             msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
 256 |         });
 257 |     }
 258 | 
 259 |     area.addEventListener('click', function (e) {
 260 |         if (e.target === input) return;
 261 |         e.preventDefault();
 262 |         input.click();
 263 |     });
 264 |     input.addEventListener('change', function () {
 265 |         if (input.files && input.files[0]) uploadVideo(input.files[0]);
 266 |         input.value = '';
 267 |     });
 268 |     area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });
 269 |     area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });
 270 |     area.addEventListener('drop', function (e) {
 271 |         e.preventDefault();
 272 |         area.classList.remove('dragover');
 273 |         if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadVideo(e.dataTransfer.files[0]);
 274 |     });
 275 | }
 276 | 
 277 | function initMaterialDropzone() {
 278 |     var area = document.getElementById('materialDropzone');
 279 |     if (!area) return;
 280 |     var input = document.getElementById('materialFileInput');
 281 |     if (!input) {
 282 |         input = document.createElement('input');
 283 |         input.type = 'file';
 284 |         input.id = 'materialFileInput';
 285 |         input.accept = '.pdf,.ppt,.pptx,.docx,image/*,video/*,.mp4,.webm';
 286 |         input.style.display = 'none';
 287 |         area.appendChild(input);
 288 |     }
 289 |     var msg = area.querySelector('.dz-inner');
 290 |     if (!msg) {
 291 |         msg = document.createElement('div');
 292 |         msg.className = 'dz-inner text-muted small';
 293 |         msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 294 |         area.appendChild(msg);
 295 |     }
 296 | 
 297 |     function uploadMaterial(file) {
 298 |         if (!file) return;
 299 |         var allowed = ['pdf', 'ppt', 'pptx', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'mov'];
 300 |         var ext = (file.name.split('.').pop() || '').toLowerCase();
 301 |         if (allowed.indexOf(ext) < 0) {
 302 |             alert('Unsupported file format: .' + ext);
 303 |             return;
 304 |         }
 305 |         var maxMb = (ext === 'mp4' || ext === 'webm' || ext === 'mov') ? 200 : 30;
 306 |         if (file.size > maxMb * 1024 * 1024) {
 307 |             alert('File too large (max ' + maxMb + 'MB).');
 308 |             return;
 309 |         }
 310 |         msg.innerText = 'Uploading ' + file.name + '...';
 311 |         uploadLessonFile(file)
 312 |         .then(function (resp) {
 313 |             if (resp && resp.success) {
 314 |                 var materialsField = document.getElementById('lessonMaterials');
 315 |                 var materials = [];
 316 |                 try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
 317 |                 var store = resp.storePath || ('Uploads/' + (resp.under || ''));
 318 |                 materials.push({
 319 |                     storePath: store,
 320 |                     url: store,
 321 |                     under: resp.under || '',
 322 |                     fileName: resp.fileName || file.name,
 323 |                     serveUrl: resp.serveUrl || resolveMediaUrl(store, false),
 324 |                     downloadUrl: resp.downloadUrl || resolveMediaUrl(store, true)
 325 |                 });
 326 |                 materialsField.value = JSON.stringify(materials);
 327 |                 renderAttachmentsList();
 328 |                 msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
 329 |                 escapeHtml(resp.fileName || file.name) + ' - preview below</span>';
 330 |             } else {
 331 |                 alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
 332 |                 msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 333 |             }
 334 |         })
 335 |         .catch(function (err) {
 336 |             console.error(err);
 337 |             alert(err.message || 'Upload failed');
 338 |             msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
 339 |         });
 340 |     }
 341 | 
 342 |     area.addEventListener('click', function (e) {
 343 |         if (e.target === input) return;
 344 |         e.preventDefault();
 345 |         input.click();
 346 |     });
 347 |     input.addEventListener('change', function () {
 348 |         if (input.files && input.files[0]) uploadMaterial(input.files[0]);
 349 |         input.value = '';
 350 |     });
 351 |     area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });
 352 |     area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });
 353 |     area.addEventListener('drop', function (e) {
 354 |         e.preventDefault();
 355 |         area.classList.remove('dragover');
 356 |         if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadMaterial(e.dataTransfer.files[0]);
 357 |     });
 358 | }
 359 | 
 360 | function renderAttachmentsList() {
 361 |     var attachments = document.getElementById('lessonAttachments');
 362 |     var materialsField = document.getElementById('lessonMaterials');
 363 |     if (!attachments || !materialsField) return;
 364 |     attachments.innerHTML = '';
 365 |     var materials = [];
 366 |     try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
 367 |     if (!materials.length) return;
 368 | 
 369 |     var heading = document.createElement('div');
 370 |     heading.className = 'fw-semibold small text-muted mb-2';
 371 |     heading.textContent = 'Materials (' + materials.length + ') - preview & download';
 372 |     attachments.appendChild(heading);
 373 | 
 374 |     materials.forEach(function (m, idx) {
 375 |         var raw = m.url || m.mediaLink || '';
 376 |         var viewUrl = m.serveUrl || resolveMediaUrl(raw, false);
 377 |         var dlUrl = m.downloadUrl || resolveMediaUrl(raw, true);
 378 |         var name = m.fileName || m.textContent || raw || ('File ' + (idx + 1));
 379 |         var kind = mediaKind(name + ' ' + raw);
 380 | 
 381 |         var card = document.createElement('div');
 382 |         card.className = 'mb-2 p-2 rounded border bg-white';
 383 |         card.innerHTML =
 384 |         '<div class="d-flex align-items-center gap-2 mb-2">' +
 385 |         '<i class="fa-solid fa-paperclip text-muted"></i>' +
 386 |         '<span class="small flex-grow-1 text-truncate fw-semibold">' + escapeHtml(name) + '</span>' +
 387 |         '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeHtml(viewUrl) + '" target="_blank" rel="noopener">Open</a>' +
 388 |         '<a class="btn btn-sm btn-outline-primary py-0" href="' + escapeHtml(dlUrl) + '" download>Download</a>' +
 389 |         '<button type="button" class="btn btn-sm btn-link text-danger p-0" data-rm="' + idx + '">Remove</button>' +
 390 |         '</div>' +
 391 |         '<div class="material-preview">' + buildMaterialPreviewHtml(viewUrl, kind, name) + '</div>';
 392 | 
 393 |         card.querySelector('[data-rm]').addEventListener('click', function () {
 394 |             removeAttachment(raw || m.url);
 395 |         });
 396 |         attachments.appendChild(card);
 397 |     });
 398 | }
 399 | 
 400 | function removeAttachment(url) {
 401 |     var materialsField = document.getElementById('lessonMaterials');
 402 |     if (!materialsField) return;
 403 |     var materials = [];
 404 |     try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
 405 |     materials = materials.filter(function (m) {
 406 |         return (m.url !== url) && (m.mediaLink !== url);
 407 |     });
 408 |     materialsField.value = JSON.stringify(materials);
 409 |     renderAttachmentsList();
 410 | }
 411 | 
```
