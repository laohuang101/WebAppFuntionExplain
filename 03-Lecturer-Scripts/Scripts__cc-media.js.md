# cc-media.js
**Source:** `Pages/Lecturer/Scripts/cc-media.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Serve files under Uploads with path sandbox + auth policy by folder.

## File overview

- **Total lines:** 411
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 4:** `dz` — script-level `const`/`let`/`var` — **Holds “dz” for this scope.**
- **Line 8:** `fileInput` — script-level `const`/`let`/`var` — **Holds “file Input” for this scope.**
- **Line 13:** `preview` — script-level `const`/`let`/`var` — **Holds “preview” for this scope.**
- **Line 15:** `hiddenField` — script-level `const`/`let`/`var` — **Holds “hidden Field” for this scope.**
- **Line 16:** `dzMsg` — script-level `const`/`let`/`var` — **Holds “dz Msg” for this scope.**
- **Line 24:** `formData` — script-level `const`/`let`/`var` — **Holds “form Data” for this scope.**
- **Line 60:** `file` — script-level `const`/`let`/`var` — **Uploaded file object or file name.**
- **Line 83:** `fd` — script-level `const`/`let`/`var` — **Holds “fd” for this scope.**
- **Line 103:** `p` — script-level `const`/`let`/`var` — **Parameter, path, or password fragment depending on context.**
- **Line 104:** `lower` — script-level `const`/`let`/`var` — **Holds “lower” for this scope.**
- **Line 105:** `i` — script-level `const`/`let`/`var` — **Loop index (0-based counter in for-loops).**
- **Line 117:** `u` — script-level `const`/`let`/`var` — **Holds “u” for this scope.**
- **Line 129:** `key` — script-level `const`/`let`/`var` — **HMAC key bytes or dictionary key.**
- **Line 131:** `q` — script-level `const`/`let`/`var` — **Search query text, or SQL command text.**
- **Line 139:** `a` — script-level `const`/`let`/`var` — **Holds “a” for this scope.**
- **Line 144:** `path` — script-level `const`/`let`/`var` — **File path under Uploads or URL path.**
- **Line 146:** `idx` — script-level `const`/`let`/`var` — **Holds “idx” for this scope.**
- **Line 156:** `root` — script-level `const`/`let`/`var` — **Root directory path (Uploads).**
- **Line 158:** `url` — script-level `const`/`let`/`var` — **HTTP URL to media or page.**
- **Line 164:** `s` — script-level `const`/`let`/`var` — **String value or submission-related object.**
- **Line 173:** `safeView` — script-level `const`/`let`/`var` — **Holds “safe View” for this scope.**
- **Line 174:** `safeName` — script-level `const`/`let`/`var` — **Holds “safe Name” for this scope.**
- **Line 194:** `area` — script-level `const`/`let`/`var` — **Holds “area” for this scope.**
- **Line 196:** `input` — script-level `const`/`let`/`var` — **Holds “input” for this scope.**
- **Line 205:** `msg` — script-level `const`/`let`/`var` — **Human-readable message (error or success).**
- **Line 215:** `ext` — script-level `const`/`let`/`var` — **File extension (.pdf, .mp4, …).**
- **Line 228:** `store` — script-level `const`/`let`/`var` — **Holds “store” for this scope.**
- **Line 229:** `viewUrl` — script-level `const`/`let`/`var` — **URL string.**
- **Line 230:** `dlUrl` — script-level `const`/`let`/`var` — **URL string.**
- **Line 231:** `txt` — script-level `const`/`let`/`var` — **UI control reference (txt).**
- **Line 239:** `prev` — script-level `const`/`let`/`var` — **Holds “prev” for this scope.**
- **Line 299:** `allowed` — script-level `const`/`let`/`var` — **Boolean — path/role is permitted.**
- **Line 305:** `maxMb` — script-level `const`/`let`/`var` — **Holds “max Mb” for this scope.**
- **Line 314:** `materialsField` — script-level `const`/`let`/`var` — **Holds “materials Field” for this scope.**
- **Line 315:** `materials` — script-level `const`/`let`/`var` — **Often a collection related to materials (plural name).**
- **Line 361:** `attachments` — script-level `const`/`let`/`var` — **Often a collection related to attachments (plural name).**
- **Line 368:** `heading` — script-level `const`/`let`/`var` — **Holds “heading” for this scope.**
- **Line 375:** `raw` — script-level `const`/`let`/`var` — **Raw bytes or unprocessed input string.**
- **Line 378:** `name` — script-level `const`/`let`/`var` — **Display name of user/course/criterion.**
- **Line 379:** `kind` — script-level `const`/`let`/`var` — **Upload kind (material/video/thumbnail/submission).**
- **Line 380:** `card` — script-level `const`/`let`/`var` — **Holds “card” for this scope.**

## Functions / methods (13 found)

### `initDropzone` — lines 2–77

```javascript
function initDropzone()
```

#### Explanation

- **Purpose:** Implements `initDropzone`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables (what each means):**
- `dz` — Holds “dz” for this scope.  DOM element from the page.
- `fileInput` — Holds “file Input” for this scope.
- `preview` — Holds “preview” for this scope.  DOM element from the page.
- `hiddenField` — Holds “hidden Field” for this scope.  DOM element from the page.
- `dzMsg` — Holds “dz Msg” for this scope.  DOM element from the page.
- `formData` — Holds “form Data” for this scope.  Newly constructed object.
- `file` — Uploaded file object or file name.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L4:** Get HTML element by id. | `dz` means: Holds “dz” for this scope.  DOM element from the page.
- **L8:** `fileInput` means: Holds “file Input” for this scope.
- **L14:** Get HTML element by id. | `preview` means: Holds “preview” for this scope.  DOM element from the page.
- **L15:** Get HTML element by id. | `hiddenField` means: Holds “hidden Field” for this scope.  DOM element from the page.
- **L16:** Get HTML element by id. | `dzMsg` means: Holds “dz Msg” for this scope.  DOM element from the page.
- **L25:** `formData` means: Holds “form Data” for this scope.  Newly constructed object.
- **L31:** HTTP request to server WebMethod/ashx.
- **L57:** DOM event handler.
- **L59:** DOM event handler.
- **L60:** `file` means: Uploaded file object or file name.
- **L64:** DOM event handler.
- **L68:** DOM event handler.
- **L71:** DOM event handler.
- **L74:** `file` means: Uploaded file object or file name.

---

### `uploadFile` — lines 16–55

```javascript
function uploadFile(file)
```

#### Explanation

- **Purpose:** Implements `uploadFile`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters (what each means):**
- `file` — Uploaded file object or file name.
- **Local variables (what each means):**
- `formData` — Holds “form Data” for this scope.  Newly constructed object.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L25:** `formData` means: Holds “form Data” for this scope.  Newly constructed object.
- **L31:** HTTP request to server WebMethod/ashx.

---

### `uploadLessonFile` — lines 81–99

```javascript
function uploadLessonFile(file)
```

#### Explanation

- **Purpose:** Implements `uploadLessonFile`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters (what each means):**
- `file` — Uploaded file object or file name.
- **Local variables (what each means):**
- `fd` — Holds “fd” for this scope.  Newly constructed object.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L83:** `fd` means: Holds “fd” for this scope.  Newly constructed object.
- **L85:** HTTP request to server WebMethod/ashx.
- **L91:** Error handling block.
- **L92:** JS object ↔ JSON text.

---

### `mediaAppRoot` — lines 101–109

```javascript
function mediaAppRoot()
```

#### Explanation

- **Purpose:** Implements `mediaAppRoot`.
- **Local variables (what each means):**
- `p` — Parameter, path, or password fragment depending on context.
- `lower` — Holds “lower” for this scope.
- `i` — Loop index (0-based counter in for-loops).

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L103:** `p` means: Parameter, path, or password fragment depending on context.
- **L104:** `lower` means: Holds “lower” for this scope.
- **L105:** `i` means: Loop index (0-based counter in for-loops).

---

### `resolveMediaUrl` — lines 114–143

```javascript
function resolveMediaUrl(raw, forDownload)
```

#### Explanation

- **Purpose:** Implements `resolveMediaUrl`.
- **Parameters (what each means):**
- `raw` — Raw bytes or unprocessed input string.
- `forDownload` — Holds “for Download” for this scope.
- **Local variables (what each means):**
- `u` — Holds “u” for this scope.
- `key` — HMAC key bytes or dictionary key.
- `q` — Search query text, or SQL command text.
- `a` — Holds “a” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L117:** `u` means: Holds “u” for this scope.
- **L128:** Error handling block.
- **L129:** `key` means: HMAC key bytes or dictionary key.
- **L131:** `q` means: Search query text, or SQL command text.
- **L137:** Error handling block.
- **L139:** `a` means: Holds “a” for this scope.

---

### `mediaKind` — lines 161–170

```javascript
function mediaKind(urlOrName)
```

#### Explanation

- **Purpose:** Implements `mediaKind`.
- **Parameters (what each means):**
- `urlOrName` — URL string.
- **Local variables (what each means):**
- `s` — String value or submission-related object.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L164:** `s` means: String value or submission-related object.

---

### `buildMaterialPreviewHtml` — lines 170–191

```javascript
function buildMaterialPreviewHtml(viewUrl, kind, fileName)
```

#### Explanation

- **Purpose:** Implements `buildMaterialPreviewHtml`.
- **Parameters (what each means):**
- `viewUrl` — URL string.
- `kind` — Upload kind (material/video/thumbnail/submission).
- `fileName` — Original file name for display/download.
- **Local variables (what each means):**
- `safeView` — Holds “safe View” for this scope.
- `safeName` — Holds “safe Name” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L173:** Encode text to reduce XSS risk. | `safeView` means: Holds “safe View” for this scope.
- **L174:** Encode text to reduce XSS risk. | `safeName` means: Holds “safe Name” for this scope.

---

### `initMediaDropzone` — lines 191–275

```javascript
function initMediaDropzone()
```

#### Explanation

- **Purpose:** Implements `initMediaDropzone`.
- **Local variables (what each means):**
- `area` — Holds “area” for this scope.  DOM element from the page.
- `input` — Holds “input” for this scope.  DOM element from the page.
- `msg` — Human-readable message (error or success).
- `ext` — File extension (.pdf, .mp4, …).
- `store` — Holds “store” for this scope.
- `viewUrl` — URL string.
- `dlUrl` — URL string.
- `txt` — UI control reference (txt).  DOM element from the page.
- `prev` — Holds “prev” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L194:** Get HTML element by id. | `area` means: Holds “area” for this scope.  DOM element from the page.
- **L196:** Get HTML element by id. | `input` means: Holds “input” for this scope.  DOM element from the page.
- **L205:** `msg` means: Human-readable message (error or success).
- **L215:** `ext` means: File extension (.pdf, .mp4, …).
- **L228:** `store` means: Holds “store” for this scope.
- **L229:** `viewUrl` means: URL string.
- **L230:** `dlUrl` means: URL string.
- **L231:** Get HTML element by id. | `txt` means: UI control reference (txt).  DOM element from the page.
- **L237:** Update page HTML.
- **L238:** Encode text to reduce XSS risk.
- **L239:** Get HTML element by id. | `prev` means: Holds “prev” for this scope.  DOM element from the page.
- **L241:** Update page HTML.
- **L242:** Encode text to reduce XSS risk.
- **L243:** Encode text to reduce XSS risk.
- **L244:** Encode text to reduce XSS risk.
- **L259:** DOM event handler.
- **L264:** DOM event handler.
- **L268:** DOM event handler.
- **L269:** DOM event handler.
- **L270:** DOM event handler.

---

### `uploadVideo` — lines 211–257

```javascript
function uploadVideo(file)
```

#### Explanation

- **Purpose:** Implements `uploadVideo`.
- **Parameters (what each means):**
- `file` — Uploaded file object or file name.
- **Local variables (what each means):**
- `ext` — File extension (.pdf, .mp4, …).
- `store` — Holds “store” for this scope.
- `viewUrl` — URL string.
- `dlUrl` — URL string.
- `txt` — UI control reference (txt).  DOM element from the page.
- `prev` — Holds “prev” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L215:** `ext` means: File extension (.pdf, .mp4, …).
- **L228:** `store` means: Holds “store” for this scope.
- **L229:** `viewUrl` means: URL string.
- **L230:** `dlUrl` means: URL string.
- **L231:** Get HTML element by id. | `txt` means: UI control reference (txt).  DOM element from the page.
- **L237:** Update page HTML.
- **L238:** Encode text to reduce XSS risk.
- **L239:** Get HTML element by id. | `prev` means: Holds “prev” for this scope.  DOM element from the page.
- **L241:** Update page HTML.
- **L242:** Encode text to reduce XSS risk.
- **L243:** Encode text to reduce XSS risk.
- **L244:** Encode text to reduce XSS risk.

---

### `initMaterialDropzone` — lines 275–358

```javascript
function initMaterialDropzone()
```

#### Explanation

- **Purpose:** Implements `initMaterialDropzone`.
- **Local variables (what each means):**
- `area` — Holds “area” for this scope.  DOM element from the page.
- `input` — Holds “input” for this scope.  DOM element from the page.
- `msg` — Human-readable message (error or success).
- `allowed` — Boolean — path/role is permitted.
- `ext` — File extension (.pdf, .mp4, …).
- `maxMb` — Holds “max Mb” for this scope.
- `materialsField` — Holds “materials Field” for this scope.  DOM element from the page.
- `materials` — Often a collection related to materials (plural name).
- `store` — Holds “store” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L278:** Get HTML element by id. | `area` means: Holds “area” for this scope.  DOM element from the page.
- **L280:** Get HTML element by id. | `input` means: Holds “input” for this scope.  DOM element from the page.
- **L289:** `msg` means: Human-readable message (error or success).
- **L299:** `allowed` means: Boolean — path/role is permitted.
- **L300:** `ext` means: File extension (.pdf, .mp4, …).
- **L305:** `maxMb` means: Holds “max Mb” for this scope.
- **L314:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L315:** `materials` means: Often a collection related to materials (plural name).
- **L316:** JS object ↔ JSON text.
- **L317:** `store` means: Holds “store” for this scope.
- **L326:** JS object ↔ JSON text.
- **L328:** Update page HTML.
- **L329:** Encode text to reduce XSS risk.
- **L342:** DOM event handler.
- **L347:** DOM event handler.
- **L351:** DOM event handler.
- **L352:** DOM event handler.
- **L353:** DOM event handler.

---

### `uploadMaterial` — lines 295–340

```javascript
function uploadMaterial(file)
```

#### Explanation

- **Purpose:** Implements `uploadMaterial`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `file` — Uploaded file object or file name.
- **Local variables (what each means):**
- `allowed` — Boolean — path/role is permitted.
- `ext` — File extension (.pdf, .mp4, …).
- `maxMb` — Holds “max Mb” for this scope.
- `materialsField` — Holds “materials Field” for this scope.  DOM element from the page.
- `materials` — Often a collection related to materials (plural name).
- `store` — Holds “store” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L299:** `allowed` means: Boolean — path/role is permitted.
- **L300:** `ext` means: File extension (.pdf, .mp4, …).
- **L305:** `maxMb` means: Holds “max Mb” for this scope.
- **L314:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L315:** `materials` means: Often a collection related to materials (plural name).
- **L316:** JS object ↔ JSON text.
- **L317:** `store` means: Holds “store” for this scope.
- **L326:** JS object ↔ JSON text.
- **L328:** Update page HTML.
- **L329:** Encode text to reduce XSS risk.

---

### `renderAttachmentsList` — lines 358–398

```javascript
function renderAttachmentsList()
```

#### Explanation

- **Purpose:** Implements `renderAttachmentsList`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Local variables (what each means):**
- `attachments` — Often a collection related to attachments (plural name).  DOM element from the page.
- `materialsField` — Holds “materials Field” for this scope.  DOM element from the page.
- `materials` — Often a collection related to materials (plural name).
- `heading` — Holds “heading” for this scope.
- `raw` — Raw bytes or unprocessed input string.
- `viewUrl` — URL string.
- `dlUrl` — URL string.
- `name` — Display name of user/course/criterion.
- `kind` — Upload kind (material/video/thumbnail/submission).
- `card` — Holds “card” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L361:** Get HTML element by id. | `attachments` means: Often a collection related to attachments (plural name).  DOM element from the page.
- **L362:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L364:** Update page HTML.
- **L365:** `materials` means: Often a collection related to materials (plural name).
- **L366:** JS object ↔ JSON text.
- **L369:** `heading` means: Holds “heading” for this scope.
- **L375:** `raw` means: Raw bytes or unprocessed input string.
- **L376:** `viewUrl` means: URL string.
- **L377:** `dlUrl` means: URL string.
- **L378:** `name` means: Display name of user/course/criterion.
- **L379:** `kind` means: Upload kind (material/video/thumbnail/submission).
- **L381:** `card` means: Holds “card” for this scope.
- **L383:** Update page HTML.
- **L386:** Encode text to reduce XSS risk.
- **L387:** Encode text to reduce XSS risk.
- **L388:** Encode text to reduce XSS risk.
- **L393:** DOM event handler.

---

### `removeAttachment` — lines 398–410

```javascript
function removeAttachment(url)
```

#### Explanation

- **Purpose:** Implements `removeAttachment`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `url` — HTTP URL to media or page.
- **Local variables (what each means):**
- `materialsField` — Holds “materials Field” for this scope.  DOM element from the page.
- `materials` — Often a collection related to materials (plural name).

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L401:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L403:** `materials` means: Often a collection related to materials (plural name).
- **L404:** JS object ↔ JSON text.
- **L408:** JS object ↔ JSON text.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L4:** Get HTML element by id. | `dz` means: Holds “dz” for this scope.  DOM element from the page.
- **L8:** `fileInput` means: Holds “file Input” for this scope.
- **L14:** Get HTML element by id. | `preview` means: Holds “preview” for this scope.  DOM element from the page.
- **L15:** Get HTML element by id. | `hiddenField` means: Holds “hidden Field” for this scope.  DOM element from the page.
- **L16:** Get HTML element by id. | `dzMsg` means: Holds “dz Msg” for this scope.  DOM element from the page.
- **L25:** `formData` means: Holds “form Data” for this scope.  Newly constructed object.
- **L31:** HTTP request to server WebMethod/ashx.
- **L57:** DOM event handler.
- **L59:** DOM event handler.
- **L60:** `file` means: Uploaded file object or file name.
- **L64:** DOM event handler.
- **L68:** DOM event handler.
- **L71:** DOM event handler.
- **L74:** `file` means: Uploaded file object or file name.
- **L83:** `fd` means: Holds “fd” for this scope.  Newly constructed object.
- **L85:** HTTP request to server WebMethod/ashx.
- **L91:** Error handling block.
- **L92:** JS object ↔ JSON text.
- **L103:** `p` means: Parameter, path, or password fragment depending on context.
- **L104:** `lower` means: Holds “lower” for this scope.
- **L105:** `i` means: Loop index (0-based counter in for-loops).
- **L117:** `u` means: Holds “u” for this scope.
- **L128:** Error handling block.
- **L129:** `key` means: HMAC key bytes or dictionary key.
- **L131:** `q` means: Search query text, or SQL command text.
- **L137:** Error handling block.
- **L139:** `a` means: Holds “a” for this scope.
- **L145:** `path` means: File path under Uploads or URL path.
- **L146:** `idx` means: Holds “idx” for this scope.
- **L157:** `root` means: Root directory path (Uploads).
- **L158:** `url` means: HTTP URL to media or page.
- **L164:** `s` means: String value or submission-related object.
- **L173:** Encode text to reduce XSS risk. | `safeView` means: Holds “safe View” for this scope.
- **L174:** Encode text to reduce XSS risk. | `safeName` means: Holds “safe Name” for this scope.
- **L194:** Get HTML element by id. | `area` means: Holds “area” for this scope.  DOM element from the page.
- **L196:** Get HTML element by id. | `input` means: Holds “input” for this scope.  DOM element from the page.
- **L205:** `msg` means: Human-readable message (error or success).
- **L215:** `ext` means: File extension (.pdf, .mp4, …).
- **L228:** `store` means: Holds “store” for this scope.
- **L229:** `viewUrl` means: URL string.
- **L230:** `dlUrl` means: URL string.
- **L231:** Get HTML element by id. | `txt` means: UI control reference (txt).  DOM element from the page.
- **L237:** Update page HTML.
- **L238:** Encode text to reduce XSS risk.
- **L239:** Get HTML element by id. | `prev` means: Holds “prev” for this scope.  DOM element from the page.
- **L241:** Update page HTML.
- **L242:** Encode text to reduce XSS risk.
- **L243:** Encode text to reduce XSS risk.
- **L244:** Encode text to reduce XSS risk.
- **L259:** DOM event handler.
- **L264:** DOM event handler.
- **L268:** DOM event handler.
- **L269:** DOM event handler.
- **L270:** DOM event handler.
- **L278:** Get HTML element by id. | `area` means: Holds “area” for this scope.  DOM element from the page.
- **L280:** Get HTML element by id. | `input` means: Holds “input” for this scope.  DOM element from the page.
- **L289:** `msg` means: Human-readable message (error or success).
- **L299:** `allowed` means: Boolean — path/role is permitted.
- **L300:** `ext` means: File extension (.pdf, .mp4, …).
- **L305:** `maxMb` means: Holds “max Mb” for this scope.
- **L314:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L315:** `materials` means: Often a collection related to materials (plural name).
- **L316:** JS object ↔ JSON text.
- **L317:** `store` means: Holds “store” for this scope.
- **L326:** JS object ↔ JSON text.
- **L328:** Update page HTML.
- **L329:** Encode text to reduce XSS risk.
- **L342:** DOM event handler.
- **L347:** DOM event handler.
- **L351:** DOM event handler.
- **L352:** DOM event handler.
- **L353:** DOM event handler.
- **L361:** Get HTML element by id. | `attachments` means: Often a collection related to attachments (plural name).  DOM element from the page.
- **L362:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L364:** Update page HTML.
- **L365:** `materials` means: Often a collection related to materials (plural name).
- **L366:** JS object ↔ JSON text.
- **L369:** `heading` means: Holds “heading” for this scope.
- **L375:** `raw` means: Raw bytes or unprocessed input string.
- **L376:** `viewUrl` means: URL string.
- **L377:** `dlUrl` means: URL string.
- **L378:** `name` means: Display name of user/course/criterion.
- **L379:** `kind` means: Upload kind (material/video/thumbnail/submission).
- **L381:** `card` means: Holds “card” for this scope.
- **L383:** Update page HTML.
- **L386:** Encode text to reduce XSS risk.
- **L387:** Encode text to reduce XSS risk.
- **L388:** Encode text to reduce XSS risk.
- **L393:** DOM event handler.
- **L401:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L403:** `materials` means: Often a collection related to materials (plural name).
- **L404:** JS object ↔ JSON text.
- **L408:** JS object ↔ JSON text.

## Source snapshot (raw)

```javascript
// Course Creation — media / materials dropzones
// depends on: cc-core.js
function initDropzone() {
    const dz = document.getElementById('dropzoneArea');
    if (!dz) return;

    // Create hidden file input
    let fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.style.display = 'none';
    dz.appendChild(fileInput);

    const preview = document.getElementById('courseThumbPreview');
    const hiddenField = document.getElementById('txtBgImg');
    const dzMsg = document.getElementById('dzMessage');

    function uploadFile(file) {
        if (!file) return;
        if (file.size > 2 * 1024 * 1024) {
            alert('File too large. Maximum allowed size is 2MB.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file, file.name);

        dz.classList.add('disabled');
        dzMsg.innerText = 'Uploading...';

        fetch('UploadThumbnail.ashx', {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(resp => {
            if (resp.success) {
                hiddenField.value = resp.url;
                if (preview) {
                    preview.src = resp.url;
                    preview.classList.remove('d-none');
                }
                dzMsg.innerText = 'Upload successful';
            } else {
                alert('Upload failed: ' + (resp.message || 'Unknown error'));
                dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
            }
        })
        .catch(err => {
            console.error(err);
            alert('Upload failed.');
            dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';
        })
        .finally(() => dz.classList.remove('disabled'));
    }

    dz.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        uploadFile(file);
    });

    dz.addEventListener('dragover', (e) => {
        e.preventDefault();
        dz.classList.add('border-primary');
    });
    dz.addEventListener('dragleave', (e) => {
        dz.classList.remove('border-primary');
    });
    dz.addEventListener('drop', (e) => {
        e.preventDefault();
        dz.classList.remove('border-primary');
        const file = e.dataTransfer.files[0];
        uploadFile(file);
    });
}



/** Upload a file to UploadMedia.ashx; returns Promise<{success,url,fileName,serveUrl,downloadUrl}> */
function uploadLessonFile(file) {
    var fd = new FormData();
    fd.append('file', file, file.name);
    return fetch('UploadMedia.ashx', {
        method: 'POST',
        body: fd,
        credentials: 'same-origin'
    }).then(function (r) {
        return r.text().then(function (text) {
            try {
                return JSON.parse(text);
            } catch (e) {
                console.error('UploadMedia non-JSON response:', text);
                throw new Error('Upload failed (server returned non-JSON). Check you are logged in and UploadMedia.ashx is reachable.');
            }
        });
    });
}

/** App virtual root: "" or "/MyApp" (never ends with /) */
function mediaAppRoot() {
    var p = window.location.pathname || '';
    var lower = p.toLowerCase();
    var i = lower.indexOf('/pages/');
    if (i > 0) return p.substring(0, i);
    // site at root → ""
    return '';
}

/**
* Resolve stored media to /Media.ashx?f=CourseMaterials/file.ext
* This is the only reliable way under IIS Express (static /Uploads often 404s).
*/
function resolveMediaUrl(raw, forDownload) {
    if (!raw) return '';
    var u = String(raw).trim();

    // External non-upload URLs
    if (/^https?:\/\//i.test(u) &&
    u.indexOf('/Uploads/') < 0 && u.indexOf('Uploads/') < 0 &&
    u.indexOf('Media.ashx') < 0 && u.indexOf('ServeUpload') < 0) {
        return u;
    }

    // Already Media.ashx / ServeUpload - normalize to Media.ashx
    if (u.indexOf('Media.ashx') >= 0 || u.indexOf('ServeUpload') >= 0) {
        try {
            var key = u.indexOf('f=') >= 0 ? 'f=' : (u.indexOf('path=') >= 0 ? 'path=' : null);
            if (key) {
                var q = u.split(key)[1];
                if (q) return resolveMediaUrl(decodeURIComponent(q.split('&')[0]), forDownload);
            }
        } catch (e) { }
    }

    try {
        if (/^https?:\/\//i.test(u)) {
        var a = document.createElement('a');
        a.href = u;
        u = a.pathname || u;
    }
} catch (e) { /* ignore */ }

var path = u.replace(/\\/g, '/');
var idx = path.toLowerCase().indexOf('/uploads/');
if (idx >= 0) path = path.substring(idx + 1); // Uploads/...
if (path.indexOf('~/') === 0) path = path.substring(2);
path = path.replace(/^\/+/, '');
if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);

// path is now CourseMaterials/guid.pdf or CourseVideos/...
if (!path) return '';
// If only a bare filename slipped in, assume CourseMaterials
if (path.indexOf('/') < 0) path = 'CourseMaterials/' + path;

var root = mediaAppRoot();
var url = root + '/Media.ashx?f=' + encodeURIComponent(path);
if (forDownload) url += '&dl=1';
return url;
}

function mediaKind(urlOrName) {
    var s = (urlOrName || '').toLowerCase();
    if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';
    if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';
    if (/\.pdf(\?|$)/.test(s)) return 'pdf';
    if (/\.(pptx?|docx?|pptm)(\?|$)/.test(s)) return 'office';
    return 'file';
}

function buildMaterialPreviewHtml(viewUrl, kind, fileName) {
    var safeView = escapeHtml(viewUrl);
    var safeName = escapeHtml(fileName || 'file');
    if (kind === 'video') {
        return '<video controls preload="metadata" src="' + safeView +
        '" style="max-width:100%;max-height:200px;display:block;border-radius:8px;background:#111;"></video>';
    }
    if (kind === 'image') {
        return '<a href="' + safeView + '" target="_blank" rel="noopener">' +
        '<img src="' + safeView + '" alt="' + safeName +
        '" style="max-width:100%;max-height:180px;border-radius:8px;object-fit:contain;background:#f3f4f6;" /></a>';
    }
    if (kind === 'pdf') {
        return '<iframe src="' + safeView +
        '#toolbar=1" title="' + safeName +
        '" style="width:100%;height:220px;border:1px solid #e5e7eb;border-radius:8px;background:#fff;"></iframe>';
    }
    return '<div class="text-muted small py-2"><i class="fa-solid fa-file me-1"></i>' + safeName +
    ' - use Open / Download</div>';
}

function initMediaDropzone() {
    var area = document.getElementById('mediaDropzone');
    if (!area) return;
    var input = document.getElementById('mediaFileInput');
    if (!input) {
        input = document.createElement('input');
        input.type = 'file';
        input.id = 'mediaFileInput';
        input.accept = 'video/*,.mp4,.webm,.mov';
        input.style.display = 'none';
        area.appendChild(input);
    }
    var msg = area.querySelector('.dz-inner');
    if (!msg) {
        msg = document.createElement('div');
        msg.className = 'dz-inner text-muted small';
        msg.innerText = 'Click to upload video (mp4/webm/mov)';
        area.appendChild(msg);
    }

    function uploadVideo(file) {
        if (!file) return;
        var ext = (file.name.split('.').pop() || '').toLowerCase();
        if (['mp4', 'webm', 'mov'].indexOf(ext) < 0) {
            alert('Unsupported video format. Use mp4, webm, or mov.');
            return;
        }
        if (file.size > 200 * 1024 * 1024) {
            alert('Video too large (max 200MB).');
            return;
        }
        msg.innerText = 'Uploading ' + file.name + '...';
        uploadLessonFile(file)
        .then(function (resp) {
            if (resp && resp.success) {
                var store = resp.storePath || resp.under || resp.url;
                var viewUrl = resp.serveUrl || resolveMediaUrl(store, false);
                var dlUrl = resp.downloadUrl || resolveMediaUrl(store, true);
                var txt = document.getElementById('txtLessonContent');
                if (txt) {
                    // store portable path for DB (Uploads/CourseVideos/...)
                    txt.value = store;
                    txt.classList.remove('d-none');
                }
                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
                escapeHtml(resp.fileName || file.name) + ' (' + (resp.size || file.size) + ' bytes)</span>';
                var prev = document.getElementById('lessonMediaPreview');
                if (prev) {
                    prev.innerHTML = buildMaterialPreviewHtml(viewUrl, 'video', resp.fileName || file.name) +
                    '<div class="mt-1"><a class="small" href="' + escapeHtml(viewUrl) + '" target="_blank">Open</a>' +
                    ' · <a class="small" href="' + escapeHtml(dlUrl) + '">Download</a></div>' +
                    '<div class="hint text-muted" style="font-size:.75rem;word-break:break-all;">' + escapeHtml(viewUrl) + '</div>';
                    prev.classList.remove('d-none');
                }
            } else {
                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
                msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
            }
        })
        .catch(function (err) {
            console.error(err);
            alert(err.message || 'Upload failed');
            msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';
        });
    }

    area.addEventListener('click', function (e) {
        if (e.target === input) return;
        e.preventDefault();
        input.click();
    });
    input.addEventListener('change', function () {
        if (input.files && input.files[0]) uploadVideo(input.files[0]);
        input.value = '';
    });
    area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });
    area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });
    area.addEventListener('drop', function (e) {
        e.preventDefault();
        area.classList.remove('dragover');
        if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadVideo(e.dataTransfer.files[0]);
    });
}

function initMaterialDropzone() {
    var area = document.getElementById('materialDropzone');
    if (!area) return;
    var input = document.getElementById('materialFileInput');
    if (!input) {
        input = document.createElement('input');
        input.type = 'file';
        input.id = 'materialFileInput';
        input.accept = '.pdf,.ppt,.pptx,.docx,image/*,video/*,.mp4,.webm';
        input.style.display = 'none';
        area.appendChild(input);
    }
    var msg = area.querySelector('.dz-inner');
    if (!msg) {
        msg = document.createElement('div');
        msg.className = 'dz-inner text-muted small';
        msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
        area.appendChild(msg);
    }

    function uploadMaterial(file) {
        if (!file) return;
        var allowed = ['pdf', 'ppt', 'pptx', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'mov'];
        var ext = (file.name.split('.').pop() || '').toLowerCase();
        if (allowed.indexOf(ext) < 0) {
            alert('Unsupported file format: .' + ext);
            return;
        }
        var maxMb = (ext === 'mp4' || ext === 'webm' || ext === 'mov') ? 200 : 30;
        if (file.size > maxMb * 1024 * 1024) {
            alert('File too large (max ' + maxMb + 'MB).');
            return;
        }
        msg.innerText = 'Uploading ' + file.name + '...';
        uploadLessonFile(file)
        .then(function (resp) {
            if (resp && resp.success) {
                var materialsField = document.getElementById('lessonMaterials');
                var materials = [];
                try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
                var store = resp.storePath || ('Uploads/' + (resp.under || ''));
                materials.push({
                    storePath: store,
                    url: store,
                    under: resp.under || '',
                    fileName: resp.fileName || file.name,
                    serveUrl: resp.serveUrl || resolveMediaUrl(store, false),
                    downloadUrl: resp.downloadUrl || resolveMediaUrl(store, true)
                });
                materialsField.value = JSON.stringify(materials);
                renderAttachmentsList();
                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +
                escapeHtml(resp.fileName || file.name) + ' - preview below</span>';
            } else {
                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));
                msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
            }
        })
        .catch(function (err) {
            console.error(err);
            alert(err.message || 'Upload failed');
            msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';
        });
    }

    area.addEventListener('click', function (e) {
        if (e.target === input) return;
        e.preventDefault();
        input.click();
    });
    input.addEventListener('change', function () {
        if (input.files && input.files[0]) uploadMaterial(input.files[0]);
        input.value = '';
    });
    area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });
    area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });
    area.addEventListener('drop', function (e) {
        e.preventDefault();
        area.classList.remove('dragover');
        if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadMaterial(e.dataTransfer.files[0]);
    });
}

function renderAttachmentsList() {
    var attachments = document.getElementById('lessonAttachments');
    var materialsField = document.getElementById('lessonMaterials');
    if (!attachments || !materialsField) return;
    attachments.innerHTML = '';
    var materials = [];
    try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
    if (!materials.length) return;

    var heading = document.createElement('div');
    heading.className = 'fw-semibold small text-muted mb-2';
    heading.textContent = 'Materials (' + materials.length + ') - preview & download';
    attachments.appendChild(heading);

    materials.forEach(function (m, idx) {
        var raw = m.url || m.mediaLink || '';
        var viewUrl = m.serveUrl || resolveMediaUrl(raw, false);
        var dlUrl = m.downloadUrl || resolveMediaUrl(raw, true);
        var name = m.fileName || m.textContent || raw || ('File ' + (idx + 1));
        var kind = mediaKind(name + ' ' + raw);

        var card = document.createElement('div');
        card.className = 'mb-2 p-2 rounded border bg-white';
        card.innerHTML =
        '<div class="d-flex align-items-center gap-2 mb-2">' +
        '<i class="fa-solid fa-paperclip text-muted"></i>' +
        '<span class="small flex-grow-1 text-truncate fw-semibold">' + escapeHtml(name) + '</span>' +
        '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeHtml(viewUrl) + '" target="_blank" rel="noopener">Open</a>' +
        '<a class="btn btn-sm btn-outline-primary py-0" href="' + escapeHtml(dlUrl) + '" download>Download</a>' +
        '<button type="button" class="btn btn-sm btn-link text-danger p-0" data-rm="' + idx + '">Remove</button>' +
        '</div>' +
        '<div class="material-preview">' + buildMaterialPreviewHtml(viewUrl, kind, name) + '</div>';

        card.querySelector('[data-rm]').addEventListener('click', function () {
            removeAttachment(raw || m.url);
        });
        attachments.appendChild(card);
    });
}

function removeAttachment(url) {
    var materialsField = document.getElementById('lessonMaterials');
    if (!materialsField) return;
    var materials = [];
    try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }
    materials = materials.filter(function (m) {
        return (m.url !== url) && (m.mediaLink !== url);
    });
    materialsField.value = JSON.stringify(materials);
    renderAttachmentsList();
}


```
