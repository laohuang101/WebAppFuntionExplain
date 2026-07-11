# cc-media.js
**Source:** `Pages/Lecturer/Scripts/cc-media.js`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Serve files under Uploads with path sandbox + auth policy by folder.

## File overview

- **Total lines:** 411
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 4:** `dz` — script-level `const`/`let`/`var`
- **Line 8:** `fileInput` — script-level `const`/`let`/`var`
- **Line 13:** `preview` — script-level `const`/`let`/`var`
- **Line 15:** `hiddenField` — script-level `const`/`let`/`var`
- **Line 16:** `dzMsg` — script-level `const`/`let`/`var`
- **Line 24:** `formData` — script-level `const`/`let`/`var`
- **Line 60:** `file` — script-level `const`/`let`/`var`
- **Line 83:** `fd` — script-level `const`/`let`/`var`
- **Line 103:** `p` — script-level `const`/`let`/`var`
- **Line 104:** `lower` — script-level `const`/`let`/`var`
- **Line 105:** `i` — script-level `const`/`let`/`var`
- **Line 117:** `u` — script-level `const`/`let`/`var`
- **Line 129:** `key` — script-level `const`/`let`/`var`
- **Line 131:** `q` — script-level `const`/`let`/`var`
- **Line 139:** `a` — script-level `const`/`let`/`var`
- **Line 144:** `path` — script-level `const`/`let`/`var`
- **Line 146:** `idx` — script-level `const`/`let`/`var`
- **Line 156:** `root` — script-level `const`/`let`/`var`
- **Line 158:** `url` — script-level `const`/`let`/`var`
- **Line 164:** `s` — script-level `const`/`let`/`var`
- **Line 173:** `safeView` — script-level `const`/`let`/`var`
- **Line 174:** `safeName` — script-level `const`/`let`/`var`
- **Line 194:** `area` — script-level `const`/`let`/`var`
- **Line 196:** `input` — script-level `const`/`let`/`var`
- **Line 205:** `msg` — script-level `const`/`let`/`var`
- **Line 215:** `ext` — script-level `const`/`let`/`var`
- **Line 228:** `store` — script-level `const`/`let`/`var`
- **Line 229:** `viewUrl` — script-level `const`/`let`/`var`
- **Line 230:** `dlUrl` — script-level `const`/`let`/`var`
- **Line 231:** `txt` — script-level `const`/`let`/`var`
- **Line 239:** `prev` — script-level `const`/`let`/`var`
- **Line 299:** `allowed` — script-level `const`/`let`/`var`
- **Line 305:** `maxMb` — script-level `const`/`let`/`var`
- **Line 314:** `materialsField` — script-level `const`/`let`/`var`
- **Line 315:** `materials` — script-level `const`/`let`/`var`
- **Line 361:** `attachments` — script-level `const`/`let`/`var`
- **Line 368:** `heading` — script-level `const`/`let`/`var`
- **Line 375:** `raw` — script-level `const`/`let`/`var`
- **Line 378:** `name` — script-level `const`/`let`/`var`
- **Line 379:** `kind` — script-level `const`/`let`/`var`
- **Line 380:** `card` — script-level `const`/`let`/`var`

## Functions / methods (13 found)

### `initDropzone` — lines 2–77

```
function initDropzone()
```

#### Explanation

- **Purpose:** Implements `initDropzone`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Local variables:** `dz`, `fileInput`, `preview`, `hiddenField`, `dzMsg`, `formData`, `file`

#### Line-by-line (this function)

`   2`  ``
`   3`  `function initDropzone() {`
`   4`  `    const dz = document.getElementById('dropzoneArea');`
  - → Get HTML element by id.
`   5`  `    if (!dz) return;`
`   6`  ``
`   7`  `    // Create hidden file input`
`   8`  `    let fileInput = document.createElement('input');`
`   9`  `    fileInput.type = 'file';`
`  10`  `    fileInput.accept = 'image/*';`
`  11`  `    fileInput.style.display = 'none';`
`  12`  `    dz.appendChild(fileInput);`
`  13`  ``
`  14`  `    const preview = document.getElementById('courseThumbPreview');`
  - → Get HTML element by id.
`  15`  `    const hiddenField = document.getElementById('txtBgImg');`
  - → Get HTML element by id.
`  16`  `    const dzMsg = document.getElementById('dzMessage');`
  - → Get HTML element by id.
`  17`  ``
`  18`  `    function uploadFile(file) {`
`  19`  `        if (!file) return;`
`  20`  `        if (file.size > 2 * 1024 * 1024) {`
`  21`  `            alert('File too large. Maximum allowed size is 2MB.');`
`  22`  `            return;`
`  23`  `        }`
`  24`  ``
`  25`  `        const formData = new FormData();`
`  26`  `        formData.append('file', file, file.name);`
`  27`  ``
`  28`  `        dz.classList.add('disabled');`
`  29`  `        dzMsg.innerText = 'Uploading...';`
`  30`  ``
`  31`  `        fetch('UploadThumbnail.ashx', {`
  - → HTTP request to server WebMethod/ashx.
`  32`  `            method: 'POST',`
`  33`  `            body: formData`
`  34`  `        })`
`  35`  `        .then(res => res.json())`
`  36`  `        .then(resp => {`
`  37`  `            if (resp.success) {`
`  38`  `                hiddenField.value = resp.url;`
`  39`  `                if (preview) {`
`  40`  `                    preview.src = resp.url;`
`  41`  `                    preview.classList.remove('d-none');`
`  42`  `                }`
`  43`  `                dzMsg.innerText = 'Upload successful';`
`  44`  `            } else {`
`  45`  `                alert('Upload failed: ' + (resp.message || 'Unknown error'));`
`  46`  `                dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';`
`  47`  `            }`
`  48`  `        })`
`  49`  `        .catch(err => {`
`  50`  `            console.error(err);`
`  51`  `            alert('Upload failed.');`
`  52`  `            dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';`
`  53`  `        })`
`  54`  `        .finally(() => dz.classList.remove('disabled'));`
`  55`  `    }`
`  56`  ``
`  57`  `    dz.addEventListener('click', () => fileInput.click());`
  - → DOM event handler.
`  58`  ``
`  59`  `    fileInput.addEventListener('change', (e) => {`
  - → DOM event handler.
`  60`  `        const file = e.target.files[0];`
`  61`  `        uploadFile(file);`
`  62`  `    });`
`  63`  ``
`  64`  `    dz.addEventListener('dragover', (e) => {`
  - → DOM event handler.
`  65`  `        e.preventDefault();`
`  66`  `        dz.classList.add('border-primary');`
`  67`  `    });`
`  68`  `    dz.addEventListener('dragleave', (e) => {`
  - → DOM event handler.
`  69`  `        dz.classList.remove('border-primary');`
`  70`  `    });`
`  71`  `    dz.addEventListener('drop', (e) => {`
  - → DOM event handler.
`  72`  `        e.preventDefault();`
`  73`  `        dz.classList.remove('border-primary');`
`  74`  `        const file = e.dataTransfer.files[0];`
`  75`  `        uploadFile(file);`
`  76`  `    });`
`  77`  `}`

---

### `uploadFile` — lines 16–55

```
function uploadFile(file)
```

#### Explanation

- **Purpose:** Implements `uploadFile`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters:** `file`
- **Local variables:** `formData`

#### Line-by-line (this function)

`  16`  ``
`  17`  ``
`  18`  `    function uploadFile(file) {`
`  19`  `        if (!file) return;`
`  20`  `        if (file.size > 2 * 1024 * 1024) {`
`  21`  `            alert('File too large. Maximum allowed size is 2MB.');`
`  22`  `            return;`
`  23`  `        }`
`  24`  ``
`  25`  `        const formData = new FormData();`
`  26`  `        formData.append('file', file, file.name);`
`  27`  ``
`  28`  `        dz.classList.add('disabled');`
`  29`  `        dzMsg.innerText = 'Uploading...';`
`  30`  ``
`  31`  `        fetch('UploadThumbnail.ashx', {`
  - → HTTP request to server WebMethod/ashx.
`  32`  `            method: 'POST',`
`  33`  `            body: formData`
`  34`  `        })`
`  35`  `        .then(res => res.json())`
`  36`  `        .then(resp => {`
`  37`  `            if (resp.success) {`
`  38`  `                hiddenField.value = resp.url;`
`  39`  `                if (preview) {`
`  40`  `                    preview.src = resp.url;`
`  41`  `                    preview.classList.remove('d-none');`
`  42`  `                }`
`  43`  `                dzMsg.innerText = 'Upload successful';`
`  44`  `            } else {`
`  45`  `                alert('Upload failed: ' + (resp.message || 'Unknown error'));`
`  46`  `                dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';`
`  47`  `            }`
`  48`  `        })`
`  49`  `        .catch(err => {`
`  50`  `            console.error(err);`
`  51`  `            alert('Upload failed.');`
`  52`  `            dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';`
`  53`  `        })`
`  54`  `        .finally(() => dz.classList.remove('disabled'));`
`  55`  `    }`

---

### `uploadLessonFile` — lines 81–99

```
function uploadLessonFile(file)
```

#### Explanation

- **Purpose:** Implements `uploadLessonFile`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **AJAX:** Browser calls server endpoints asynchronously.
- **Parameters:** `file`
- **Local variables:** `fd`

#### Line-by-line (this function)

`  81`  ``
`  82`  `function uploadLessonFile(file) {`
`  83`  `    var fd = new FormData();`
`  84`  `    fd.append('file', file, file.name);`
`  85`  `    return fetch('UploadMedia.ashx', {`
  - → HTTP request to server WebMethod/ashx.
`  86`  `        method: 'POST',`
`  87`  `        body: fd,`
`  88`  `        credentials: 'same-origin'`
`  89`  `    }).then(function (r) {`
`  90`  `        return r.text().then(function (text) {`
`  91`  `            try {`
  - → Error handling block.
`  92`  `                return JSON.parse(text);`
  - → JS object ↔ JSON text.
`  93`  `            } catch (e) {`
`  94`  `                console.error('UploadMedia non-JSON response:', text);`
`  95`  `                throw new Error('Upload failed (server returned non-JSON). Check you are logged in and UploadMedia.ashx is reachable.');`
`  96`  `            }`
`  97`  `        });`
`  98`  `    });`
`  99`  `}`

---

### `mediaAppRoot` — lines 101–109

```
function mediaAppRoot()
```

#### Explanation

- **Purpose:** Implements `mediaAppRoot`.
- **Local variables:** `p`, `lower`, `i`

#### Line-by-line (this function)

` 101`  ``
` 102`  `function mediaAppRoot() {`
` 103`  `    var p = window.location.pathname || '';`
` 104`  `    var lower = p.toLowerCase();`
` 105`  `    var i = lower.indexOf('/pages/');`
` 106`  `    if (i > 0) return p.substring(0, i);`
` 107`  `    // site at root → ""`
` 108`  `    return '';`
` 109`  `}`

---

### `resolveMediaUrl` — lines 114–143

```
function resolveMediaUrl(raw, forDownload)
```

#### Explanation

- **Purpose:** Implements `resolveMediaUrl`.
- **Parameters:** `raw, forDownload`
- **Local variables:** `u`, `key`, `q`, `a`

#### Line-by-line (this function)

` 114`  ``
` 115`  `function resolveMediaUrl(raw, forDownload) {`
` 116`  `    if (!raw) return '';`
` 117`  `    var u = String(raw).trim();`
` 118`  ``
` 119`  `    // External non-upload URLs`
` 120`  `    if (/^https?:\/\//i.test(u) &&`
` 121`  `    u.indexOf('/Uploads/') < 0 && u.indexOf('Uploads/') < 0 &&`
` 122`  `    u.indexOf('Media.ashx') < 0 && u.indexOf('ServeUpload') < 0) {`
` 123`  `        return u;`
` 124`  `    }`
` 125`  ``
` 126`  `    // Already Media.ashx / ServeUpload - normalize to Media.ashx`
` 127`  `    if (u.indexOf('Media.ashx') >= 0 || u.indexOf('ServeUpload') >= 0) {`
` 128`  `        try {`
  - → Error handling block.
` 129`  `            var key = u.indexOf('f=') >= 0 ? 'f=' : (u.indexOf('path=') >= 0 ? 'path=' : null);`
` 130`  `            if (key) {`
` 131`  `                var q = u.split(key)[1];`
` 132`  `                if (q) return resolveMediaUrl(decodeURIComponent(q.split('&')[0]), forDownload);`
` 133`  `            }`
` 134`  `        } catch (e) { }`
` 135`  `    }`
` 136`  ``
` 137`  `    try {`
  - → Error handling block.
` 138`  `        if (/^https?:\/\//i.test(u)) {`
` 139`  `        var a = document.createElement('a');`
` 140`  `        a.href = u;`
` 141`  `        u = a.pathname || u;`
` 142`  `    }`
` 143`  `}`

---

### `mediaKind` — lines 161–170

```
function mediaKind(urlOrName)
```

#### Explanation

- **Purpose:** Implements `mediaKind`.
- **Parameters:** `urlOrName`
- **Local variables:** `s`

#### Line-by-line (this function)

` 161`  ``
` 162`  ``
` 163`  `function mediaKind(urlOrName) {`
` 164`  `    var s = (urlOrName || '').toLowerCase();`
` 165`  `    if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';`
` 166`  `    if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';`
` 167`  `    if (/\.pdf(\?|$)/.test(s)) return 'pdf';`
` 168`  `    if (/\.(pptx?|docx?|pptm)(\?|$)/.test(s)) return 'office';`
` 169`  `    return 'file';`
` 170`  `}`

---

### `buildMaterialPreviewHtml` — lines 170–191

```
function buildMaterialPreviewHtml(viewUrl, kind, fileName)
```

#### Explanation

- **Purpose:** Implements `buildMaterialPreviewHtml`.
- **Parameters:** `viewUrl, kind, fileName`
- **Local variables:** `safeView`, `safeName`

#### Line-by-line (this function)

` 170`  ``
` 171`  ``
` 172`  `function buildMaterialPreviewHtml(viewUrl, kind, fileName) {`
` 173`  `    var safeView = escapeHtml(viewUrl);`
  - → Encode text to reduce XSS risk.
` 174`  `    var safeName = escapeHtml(fileName || 'file');`
  - → Encode text to reduce XSS risk.
` 175`  `    if (kind === 'video') {`
` 176`  `        return '<video controls preload="metadata" src="' + safeView +`
` 177`  `        '" style="max-width:100%;max-height:200px;display:block;border-radius:8px;background:#111;"></video>';`
` 178`  `    }`
` 179`  `    if (kind === 'image') {`
` 180`  `        return '<a href="' + safeView + '" target="_blank" rel="noopener">' +`
` 181`  `        '<img src="' + safeView + '" alt="' + safeName +`
` 182`  `        '" style="max-width:100%;max-height:180px;border-radius:8px;object-fit:contain;background:#f3f4f6;" /></a>';`
` 183`  `    }`
` 184`  `    if (kind === 'pdf') {`
` 185`  `        return '<iframe src="' + safeView +`
` 186`  `        '#toolbar=1" title="' + safeName +`
` 187`  `        '" style="width:100%;height:220px;border:1px solid #e5e7eb;border-radius:8px;background:#fff;"></iframe>';`
` 188`  `    }`
` 189`  `    return '<div class="text-muted small py-2"><i class="fa-solid fa-file me-1"></i>' + safeName +`
` 190`  `    ' - use Open / Download</div>';`
` 191`  `}`

---

### `initMediaDropzone` — lines 191–275

```
function initMediaDropzone()
```

#### Explanation

- **Purpose:** Implements `initMediaDropzone`.
- **Local variables:** `area`, `input`, `msg`, `ext`, `store`, `viewUrl`, `dlUrl`, `txt`, `prev`

#### Line-by-line (this function)

` 191`  ``
` 192`  ``
` 193`  `function initMediaDropzone() {`
` 194`  `    var area = document.getElementById('mediaDropzone');`
  - → Get HTML element by id.
` 195`  `    if (!area) return;`
` 196`  `    var input = document.getElementById('mediaFileInput');`
  - → Get HTML element by id.
` 197`  `    if (!input) {`
` 198`  `        input = document.createElement('input');`
` 199`  `        input.type = 'file';`
` 200`  `        input.id = 'mediaFileInput';`
` 201`  `        input.accept = 'video/*,.mp4,.webm,.mov';`
` 202`  `        input.style.display = 'none';`
` 203`  `        area.appendChild(input);`
` 204`  `    }`
` 205`  `    var msg = area.querySelector('.dz-inner');`
` 206`  `    if (!msg) {`
` 207`  `        msg = document.createElement('div');`
` 208`  `        msg.className = 'dz-inner text-muted small';`
` 209`  `        msg.innerText = 'Click to upload video (mp4/webm/mov)';`
` 210`  `        area.appendChild(msg);`
` 211`  `    }`
` 212`  ``
` 213`  `    function uploadVideo(file) {`
` 214`  `        if (!file) return;`
` 215`  `        var ext = (file.name.split('.').pop() || '').toLowerCase();`
` 216`  `        if (['mp4', 'webm', 'mov'].indexOf(ext) < 0) {`
` 217`  `            alert('Unsupported video format. Use mp4, webm, or mov.');`
` 218`  `            return;`
` 219`  `        }`
` 220`  `        if (file.size > 200 * 1024 * 1024) {`
` 221`  `            alert('Video too large (max 200MB).');`
` 222`  `            return;`
` 223`  `        }`
` 224`  `        msg.innerText = 'Uploading ' + file.name + '...';`
` 225`  `        uploadLessonFile(file)`
` 226`  `        .then(function (resp) {`
` 227`  `            if (resp && resp.success) {`
` 228`  `                var store = resp.storePath || resp.under || resp.url;`
` 229`  `                var viewUrl = resp.serveUrl || resolveMediaUrl(store, false);`
` 230`  `                var dlUrl = resp.downloadUrl || resolveMediaUrl(store, true);`
` 231`  `                var txt = document.getElementById('txtLessonContent');`
  - → Get HTML element by id.
` 232`  `                if (txt) {`
` 233`  `                    // store portable path for DB (Uploads/CourseVideos/...)`
` 234`  `                    txt.value = store;`
` 235`  `                    txt.classList.remove('d-none');`
` 236`  `                }`
` 237`  `                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +`
  - → Update page HTML.
` 238`  `                escapeHtml(resp.fileName || file.name) + ' (' + (resp.size || file.size) + ' bytes)</span>';`
  - → Encode text to reduce XSS risk.
` 239`  `                var prev = document.getElementById('lessonMediaPreview');`
  - → Get HTML element by id.
` 240`  `                if (prev) {`
` 241`  `                    prev.innerHTML = buildMaterialPreviewHtml(viewUrl, 'video', resp.fileName || file.name) +`
  - → Update page HTML.
` 242`  `                    '<div class="mt-1"><a class="small" href="' + escapeHtml(viewUrl) + '" target="_blank">Open</a>' +`
  - → Encode text to reduce XSS risk.
` 243`  `                    ' · <a class="small" href="' + escapeHtml(dlUrl) + '">Download</a></div>' +`
  - → Encode text to reduce XSS risk.
` 244`  `                    '<div class="hint text-muted" style="font-size:.75rem;word-break:break-all;">' + escapeHtml(viewUrl) + '</div>';`
  - → Encode text to reduce XSS risk.
` 245`  `                    prev.classList.remove('d-none');`
` 246`  `                }`
` 247`  `            } else {`
` 248`  `                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));`
` 249`  `                msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';`
` 250`  `            }`
` 251`  `        })`
` 252`  `        .catch(function (err) {`
` 253`  `            console.error(err);`
` 254`  `            alert(err.message || 'Upload failed');`
` 255`  `            msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';`
` 256`  `        });`
` 257`  `    }`
` 258`  ``
` 259`  `    area.addEventListener('click', function (e) {`
  - → DOM event handler.
` 260`  `        if (e.target === input) return;`
` 261`  `        e.preventDefault();`
` 262`  `        input.click();`
` 263`  `    });`
` 264`  `    input.addEventListener('change', function () {`
  - → DOM event handler.
` 265`  `        if (input.files && input.files[0]) uploadVideo(input.files[0]);`
` 266`  `        input.value = '';`
` 267`  `    });`
` 268`  `    area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });`
  - → DOM event handler.
` 269`  `    area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });`
  - → DOM event handler.
` 270`  `    area.addEventListener('drop', function (e) {`
  - → DOM event handler.
` 271`  `        e.preventDefault();`
` 272`  `        area.classList.remove('dragover');`
` 273`  `        if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadVideo(e.dataTransfer.files[0]);`
` 274`  `    });`
` 275`  `}`

---

### `uploadVideo` — lines 211–257

```
function uploadVideo(file)
```

#### Explanation

- **Purpose:** Implements `uploadVideo`.
- **Parameters:** `file`
- **Local variables:** `ext`, `store`, `viewUrl`, `dlUrl`, `txt`, `prev`

#### Line-by-line (this function)

` 211`  ``
` 212`  ``
` 213`  `    function uploadVideo(file) {`
` 214`  `        if (!file) return;`
` 215`  `        var ext = (file.name.split('.').pop() || '').toLowerCase();`
` 216`  `        if (['mp4', 'webm', 'mov'].indexOf(ext) < 0) {`
` 217`  `            alert('Unsupported video format. Use mp4, webm, or mov.');`
` 218`  `            return;`
` 219`  `        }`
` 220`  `        if (file.size > 200 * 1024 * 1024) {`
` 221`  `            alert('Video too large (max 200MB).');`
` 222`  `            return;`
` 223`  `        }`
` 224`  `        msg.innerText = 'Uploading ' + file.name + '...';`
` 225`  `        uploadLessonFile(file)`
` 226`  `        .then(function (resp) {`
` 227`  `            if (resp && resp.success) {`
` 228`  `                var store = resp.storePath || resp.under || resp.url;`
` 229`  `                var viewUrl = resp.serveUrl || resolveMediaUrl(store, false);`
` 230`  `                var dlUrl = resp.downloadUrl || resolveMediaUrl(store, true);`
` 231`  `                var txt = document.getElementById('txtLessonContent');`
  - → Get HTML element by id.
` 232`  `                if (txt) {`
` 233`  `                    // store portable path for DB (Uploads/CourseVideos/...)`
` 234`  `                    txt.value = store;`
` 235`  `                    txt.classList.remove('d-none');`
` 236`  `                }`
` 237`  `                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +`
  - → Update page HTML.
` 238`  `                escapeHtml(resp.fileName || file.name) + ' (' + (resp.size || file.size) + ' bytes)</span>';`
  - → Encode text to reduce XSS risk.
` 239`  `                var prev = document.getElementById('lessonMediaPreview');`
  - → Get HTML element by id.
` 240`  `                if (prev) {`
` 241`  `                    prev.innerHTML = buildMaterialPreviewHtml(viewUrl, 'video', resp.fileName || file.name) +`
  - → Update page HTML.
` 242`  `                    '<div class="mt-1"><a class="small" href="' + escapeHtml(viewUrl) + '" target="_blank">Open</a>' +`
  - → Encode text to reduce XSS risk.
` 243`  `                    ' · <a class="small" href="' + escapeHtml(dlUrl) + '">Download</a></div>' +`
  - → Encode text to reduce XSS risk.
` 244`  `                    '<div class="hint text-muted" style="font-size:.75rem;word-break:break-all;">' + escapeHtml(viewUrl) + '</div>';`
  - → Encode text to reduce XSS risk.
` 245`  `                    prev.classList.remove('d-none');`
` 246`  `                }`
` 247`  `            } else {`
` 248`  `                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));`
` 249`  `                msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';`
` 250`  `            }`
` 251`  `        })`
` 252`  `        .catch(function (err) {`
` 253`  `            console.error(err);`
` 254`  `            alert(err.message || 'Upload failed');`
` 255`  `            msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';`
` 256`  `        });`
` 257`  `    }`

---

### `initMaterialDropzone` — lines 275–358

```
function initMaterialDropzone()
```

#### Explanation

- **Purpose:** Implements `initMaterialDropzone`.
- **Local variables:** `area`, `input`, `msg`, `allowed`, `ext`, `maxMb`, `materialsField`, `materials`, `store`

#### Line-by-line (this function)

` 275`  ``
` 276`  ``
` 277`  `function initMaterialDropzone() {`
` 278`  `    var area = document.getElementById('materialDropzone');`
  - → Get HTML element by id.
` 279`  `    if (!area) return;`
` 280`  `    var input = document.getElementById('materialFileInput');`
  - → Get HTML element by id.
` 281`  `    if (!input) {`
` 282`  `        input = document.createElement('input');`
` 283`  `        input.type = 'file';`
` 284`  `        input.id = 'materialFileInput';`
` 285`  `        input.accept = '.pdf,.ppt,.pptx,.docx,image/*,video/*,.mp4,.webm';`
` 286`  `        input.style.display = 'none';`
` 287`  `        area.appendChild(input);`
` 288`  `    }`
` 289`  `    var msg = area.querySelector('.dz-inner');`
` 290`  `    if (!msg) {`
` 291`  `        msg = document.createElement('div');`
` 292`  `        msg.className = 'dz-inner text-muted small';`
` 293`  `        msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 294`  `        area.appendChild(msg);`
` 295`  `    }`
` 296`  ``
` 297`  `    function uploadMaterial(file) {`
` 298`  `        if (!file) return;`
` 299`  `        var allowed = ['pdf', 'ppt', 'pptx', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'mov'];`
` 300`  `        var ext = (file.name.split('.').pop() || '').toLowerCase();`
` 301`  `        if (allowed.indexOf(ext) < 0) {`
` 302`  `            alert('Unsupported file format: .' + ext);`
` 303`  `            return;`
` 304`  `        }`
` 305`  `        var maxMb = (ext === 'mp4' || ext === 'webm' || ext === 'mov') ? 200 : 30;`
` 306`  `        if (file.size > maxMb * 1024 * 1024) {`
` 307`  `            alert('File too large (max ' + maxMb + 'MB).');`
` 308`  `            return;`
` 309`  `        }`
` 310`  `        msg.innerText = 'Uploading ' + file.name + '...';`
` 311`  `        uploadLessonFile(file)`
` 312`  `        .then(function (resp) {`
` 313`  `            if (resp && resp.success) {`
` 314`  `                var materialsField = document.getElementById('lessonMaterials');`
  - → Get HTML element by id.
` 315`  `                var materials = [];`
` 316`  `                try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }`
  - → JS object ↔ JSON text.
` 317`  `                var store = resp.storePath || ('Uploads/' + (resp.under || ''));`
` 318`  `                materials.push({`
` 319`  `                    storePath: store,`
` 320`  `                    url: store,`
` 321`  `                    under: resp.under || '',`
` 322`  `                    fileName: resp.fileName || file.name,`
` 323`  `                    serveUrl: resp.serveUrl || resolveMediaUrl(store, false),`
` 324`  `                    downloadUrl: resp.downloadUrl || resolveMediaUrl(store, true)`
` 325`  `                });`
` 326`  `                materialsField.value = JSON.stringify(materials);`
  - → JS object ↔ JSON text.
` 327`  `                renderAttachmentsList();`
` 328`  `                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +`
  - → Update page HTML.
` 329`  `                escapeHtml(resp.fileName || file.name) + ' - preview below</span>';`
  - → Encode text to reduce XSS risk.
` 330`  `            } else {`
` 331`  `                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));`
` 332`  `                msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 333`  `            }`
` 334`  `        })`
` 335`  `        .catch(function (err) {`
` 336`  `            console.error(err);`
` 337`  `            alert(err.message || 'Upload failed');`
` 338`  `            msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 339`  `        });`
` 340`  `    }`
` 341`  ``
` 342`  `    area.addEventListener('click', function (e) {`
  - → DOM event handler.
` 343`  `        if (e.target === input) return;`
` 344`  `        e.preventDefault();`
` 345`  `        input.click();`
` 346`  `    });`
` 347`  `    input.addEventListener('change', function () {`
  - → DOM event handler.
` 348`  `        if (input.files && input.files[0]) uploadMaterial(input.files[0]);`
` 349`  `        input.value = '';`
` 350`  `    });`
` 351`  `    area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });`
  - → DOM event handler.
` 352`  `    area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });`
  - → DOM event handler.
` 353`  `    area.addEventListener('drop', function (e) {`
  - → DOM event handler.
` 354`  `        e.preventDefault();`
` 355`  `        area.classList.remove('dragover');`
` 356`  `        if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadMaterial(e.dataTransfer.files[0]);`
` 357`  `    });`
` 358`  `}`

---

### `uploadMaterial` — lines 295–340

```
function uploadMaterial(file)
```

#### Explanation

- **Purpose:** Implements `uploadMaterial`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters:** `file`
- **Local variables:** `allowed`, `ext`, `maxMb`, `materialsField`, `materials`, `store`

#### Line-by-line (this function)

` 295`  ``
` 296`  ``
` 297`  `    function uploadMaterial(file) {`
` 298`  `        if (!file) return;`
` 299`  `        var allowed = ['pdf', 'ppt', 'pptx', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'mov'];`
` 300`  `        var ext = (file.name.split('.').pop() || '').toLowerCase();`
` 301`  `        if (allowed.indexOf(ext) < 0) {`
` 302`  `            alert('Unsupported file format: .' + ext);`
` 303`  `            return;`
` 304`  `        }`
` 305`  `        var maxMb = (ext === 'mp4' || ext === 'webm' || ext === 'mov') ? 200 : 30;`
` 306`  `        if (file.size > maxMb * 1024 * 1024) {`
` 307`  `            alert('File too large (max ' + maxMb + 'MB).');`
` 308`  `            return;`
` 309`  `        }`
` 310`  `        msg.innerText = 'Uploading ' + file.name + '...';`
` 311`  `        uploadLessonFile(file)`
` 312`  `        .then(function (resp) {`
` 313`  `            if (resp && resp.success) {`
` 314`  `                var materialsField = document.getElementById('lessonMaterials');`
  - → Get HTML element by id.
` 315`  `                var materials = [];`
` 316`  `                try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }`
  - → JS object ↔ JSON text.
` 317`  `                var store = resp.storePath || ('Uploads/' + (resp.under || ''));`
` 318`  `                materials.push({`
` 319`  `                    storePath: store,`
` 320`  `                    url: store,`
` 321`  `                    under: resp.under || '',`
` 322`  `                    fileName: resp.fileName || file.name,`
` 323`  `                    serveUrl: resp.serveUrl || resolveMediaUrl(store, false),`
` 324`  `                    downloadUrl: resp.downloadUrl || resolveMediaUrl(store, true)`
` 325`  `                });`
` 326`  `                materialsField.value = JSON.stringify(materials);`
  - → JS object ↔ JSON text.
` 327`  `                renderAttachmentsList();`
` 328`  `                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +`
  - → Update page HTML.
` 329`  `                escapeHtml(resp.fileName || file.name) + ' - preview below</span>';`
  - → Encode text to reduce XSS risk.
` 330`  `            } else {`
` 331`  `                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));`
` 332`  `                msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 333`  `            }`
` 334`  `        })`
` 335`  `        .catch(function (err) {`
` 336`  `            console.error(err);`
` 337`  `            alert(err.message || 'Upload failed');`
` 338`  `            msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 339`  `        });`
` 340`  `    }`

---

### `renderAttachmentsList` — lines 358–398

```
function renderAttachmentsList()
```

#### Explanation

- **Purpose:** Implements `renderAttachmentsList`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Local variables:** `attachments`, `materialsField`, `materials`, `heading`, `raw`, `viewUrl`, `dlUrl`, `name`, `kind`, `card`

#### Line-by-line (this function)

` 358`  ``
` 359`  ``
` 360`  `function renderAttachmentsList() {`
` 361`  `    var attachments = document.getElementById('lessonAttachments');`
  - → Get HTML element by id.
` 362`  `    var materialsField = document.getElementById('lessonMaterials');`
  - → Get HTML element by id.
` 363`  `    if (!attachments || !materialsField) return;`
` 364`  `    attachments.innerHTML = '';`
  - → Update page HTML.
` 365`  `    var materials = [];`
` 366`  `    try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }`
  - → JS object ↔ JSON text.
` 367`  `    if (!materials.length) return;`
` 368`  ``
` 369`  `    var heading = document.createElement('div');`
` 370`  `    heading.className = 'fw-semibold small text-muted mb-2';`
` 371`  `    heading.textContent = 'Materials (' + materials.length + ') - preview & download';`
` 372`  `    attachments.appendChild(heading);`
` 373`  ``
` 374`  `    materials.forEach(function (m, idx) {`
` 375`  `        var raw = m.url || m.mediaLink || '';`
` 376`  `        var viewUrl = m.serveUrl || resolveMediaUrl(raw, false);`
` 377`  `        var dlUrl = m.downloadUrl || resolveMediaUrl(raw, true);`
` 378`  `        var name = m.fileName || m.textContent || raw || ('File ' + (idx + 1));`
` 379`  `        var kind = mediaKind(name + ' ' + raw);`
` 380`  ``
` 381`  `        var card = document.createElement('div');`
` 382`  `        card.className = 'mb-2 p-2 rounded border bg-white';`
` 383`  `        card.innerHTML =`
  - → Update page HTML.
` 384`  `        '<div class="d-flex align-items-center gap-2 mb-2">' +`
` 385`  `        '<i class="fa-solid fa-paperclip text-muted"></i>' +`
` 386`  `        '<span class="small flex-grow-1 text-truncate fw-semibold">' + escapeHtml(name) + '</span>' +`
  - → Encode text to reduce XSS risk.
` 387`  `        '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeHtml(viewUrl) + '" target="_blank" rel="noopener">Open</a>' +`
  - → Encode text to reduce XSS risk.
` 388`  `        '<a class="btn btn-sm btn-outline-primary py-0" href="' + escapeHtml(dlUrl) + '" download>Download</a>' +`
  - → Encode text to reduce XSS risk.
` 389`  `        '<button type="button" class="btn btn-sm btn-link text-danger p-0" data-rm="' + idx + '">Remove</button>' +`
` 390`  `        '</div>' +`
` 391`  `        '<div class="material-preview">' + buildMaterialPreviewHtml(viewUrl, kind, name) + '</div>';`
` 392`  ``
` 393`  `        card.querySelector('[data-rm]').addEventListener('click', function () {`
  - → DOM event handler.
` 394`  `            removeAttachment(raw || m.url);`
` 395`  `        });`
` 396`  `        attachments.appendChild(card);`
` 397`  `    });`
` 398`  `}`

---

### `removeAttachment` — lines 398–410

```
function removeAttachment(url)
```

#### Explanation

- **Purpose:** Implements `removeAttachment`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Delete/clear data.
- **Parameters:** `url`
- **Local variables:** `materialsField`, `materials`

#### Line-by-line (this function)

` 398`  ``
` 399`  ``
` 400`  `function removeAttachment(url) {`
` 401`  `    var materialsField = document.getElementById('lessonMaterials');`
  - → Get HTML element by id.
` 402`  `    if (!materialsField) return;`
` 403`  `    var materials = [];`
` 404`  `    try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }`
  - → JS object ↔ JSON text.
` 405`  `    materials = materials.filter(function (m) {`
` 406`  `        return (m.url !== url) && (m.mediaLink !== url);`
` 407`  `    });`
` 408`  `    materialsField.value = JSON.stringify(materials);`
  - → JS object ↔ JSON text.
` 409`  `    renderAttachmentsList();`
` 410`  `}`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `// Course Creation — media / materials dropzones`
`   2`  `// depends on: cc-core.js`
`   3`  `function initDropzone() {`
`   4`  `    const dz = document.getElementById('dropzoneArea');`
  - → Get HTML element by id.
`   5`  `    if (!dz) return;`
`   6`  ``
`   7`  `    // Create hidden file input`
`   8`  `    let fileInput = document.createElement('input');`
`   9`  `    fileInput.type = 'file';`
`  10`  `    fileInput.accept = 'image/*';`
`  11`  `    fileInput.style.display = 'none';`
`  12`  `    dz.appendChild(fileInput);`
`  13`  ``
`  14`  `    const preview = document.getElementById('courseThumbPreview');`
  - → Get HTML element by id.
`  15`  `    const hiddenField = document.getElementById('txtBgImg');`
  - → Get HTML element by id.
`  16`  `    const dzMsg = document.getElementById('dzMessage');`
  - → Get HTML element by id.
`  17`  ``
`  18`  `    function uploadFile(file) {`
`  19`  `        if (!file) return;`
`  20`  `        if (file.size > 2 * 1024 * 1024) {`
`  21`  `            alert('File too large. Maximum allowed size is 2MB.');`
`  22`  `            return;`
`  23`  `        }`
`  24`  ``
`  25`  `        const formData = new FormData();`
`  26`  `        formData.append('file', file, file.name);`
`  27`  ``
`  28`  `        dz.classList.add('disabled');`
`  29`  `        dzMsg.innerText = 'Uploading...';`
`  30`  ``
`  31`  `        fetch('UploadThumbnail.ashx', {`
  - → HTTP request to server WebMethod/ashx.
`  32`  `            method: 'POST',`
`  33`  `            body: formData`
`  34`  `        })`
`  35`  `        .then(res => res.json())`
`  36`  `        .then(resp => {`
`  37`  `            if (resp.success) {`
`  38`  `                hiddenField.value = resp.url;`
`  39`  `                if (preview) {`
`  40`  `                    preview.src = resp.url;`
`  41`  `                    preview.classList.remove('d-none');`
`  42`  `                }`
`  43`  `                dzMsg.innerText = 'Upload successful';`
`  44`  `            } else {`
`  45`  `                alert('Upload failed: ' + (resp.message || 'Unknown error'));`
`  46`  `                dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';`
`  47`  `            }`
`  48`  `        })`
`  49`  `        .catch(err => {`
`  50`  `            console.error(err);`
`  51`  `            alert('Upload failed.');`
`  52`  `            dzMsg.innerText = 'Drag & drop a thumbnail here or click to browse (Max 2MB)';`
`  53`  `        })`
`  54`  `        .finally(() => dz.classList.remove('disabled'));`
`  55`  `    }`
`  56`  ``
`  57`  `    dz.addEventListener('click', () => fileInput.click());`
  - → DOM event handler.
`  58`  ``
`  59`  `    fileInput.addEventListener('change', (e) => {`
  - → DOM event handler.
`  60`  `        const file = e.target.files[0];`
`  61`  `        uploadFile(file);`
`  62`  `    });`
`  63`  ``
`  64`  `    dz.addEventListener('dragover', (e) => {`
  - → DOM event handler.
`  65`  `        e.preventDefault();`
`  66`  `        dz.classList.add('border-primary');`
`  67`  `    });`
`  68`  `    dz.addEventListener('dragleave', (e) => {`
  - → DOM event handler.
`  69`  `        dz.classList.remove('border-primary');`
`  70`  `    });`
`  71`  `    dz.addEventListener('drop', (e) => {`
  - → DOM event handler.
`  72`  `        e.preventDefault();`
`  73`  `        dz.classList.remove('border-primary');`
`  74`  `        const file = e.dataTransfer.files[0];`
`  75`  `        uploadFile(file);`
`  76`  `    });`
`  77`  `}`
`  78`  ``
`  79`  ``
`  80`  ``
`  81`  `/** Upload a file to UploadMedia.ashx; returns Promise<{success,url,fileName,serveUrl,downloadUrl}> */`
`  82`  `function uploadLessonFile(file) {`
`  83`  `    var fd = new FormData();`
`  84`  `    fd.append('file', file, file.name);`
`  85`  `    return fetch('UploadMedia.ashx', {`
  - → HTTP request to server WebMethod/ashx.
`  86`  `        method: 'POST',`
`  87`  `        body: fd,`
`  88`  `        credentials: 'same-origin'`
`  89`  `    }).then(function (r) {`
`  90`  `        return r.text().then(function (text) {`
`  91`  `            try {`
  - → Error handling block.
`  92`  `                return JSON.parse(text);`
  - → JS object ↔ JSON text.
`  93`  `            } catch (e) {`
`  94`  `                console.error('UploadMedia non-JSON response:', text);`
`  95`  `                throw new Error('Upload failed (server returned non-JSON). Check you are logged in and UploadMedia.ashx is reachable.');`
`  96`  `            }`
`  97`  `        });`
`  98`  `    });`
`  99`  `}`
` 100`  ``
` 101`  `/** App virtual root: "" or "/MyApp" (never ends with /) */`
` 102`  `function mediaAppRoot() {`
` 103`  `    var p = window.location.pathname || '';`
` 104`  `    var lower = p.toLowerCase();`
` 105`  `    var i = lower.indexOf('/pages/');`
` 106`  `    if (i > 0) return p.substring(0, i);`
` 107`  `    // site at root → ""`
` 108`  `    return '';`
` 109`  `}`
` 110`  ``
` 111`  `/**`
` 112`  `* Resolve stored media to /Media.ashx?f=CourseMaterials/file.ext`
` 113`  `* This is the only reliable way under IIS Express (static /Uploads often 404s).`
` 114`  `*/`
` 115`  `function resolveMediaUrl(raw, forDownload) {`
` 116`  `    if (!raw) return '';`
` 117`  `    var u = String(raw).trim();`
` 118`  ``
` 119`  `    // External non-upload URLs`
` 120`  `    if (/^https?:\/\//i.test(u) &&`
` 121`  `    u.indexOf('/Uploads/') < 0 && u.indexOf('Uploads/') < 0 &&`
` 122`  `    u.indexOf('Media.ashx') < 0 && u.indexOf('ServeUpload') < 0) {`
` 123`  `        return u;`
` 124`  `    }`
` 125`  ``
` 126`  `    // Already Media.ashx / ServeUpload - normalize to Media.ashx`
` 127`  `    if (u.indexOf('Media.ashx') >= 0 || u.indexOf('ServeUpload') >= 0) {`
` 128`  `        try {`
  - → Error handling block.
` 129`  `            var key = u.indexOf('f=') >= 0 ? 'f=' : (u.indexOf('path=') >= 0 ? 'path=' : null);`
` 130`  `            if (key) {`
` 131`  `                var q = u.split(key)[1];`
` 132`  `                if (q) return resolveMediaUrl(decodeURIComponent(q.split('&')[0]), forDownload);`
` 133`  `            }`
` 134`  `        } catch (e) { }`
` 135`  `    }`
` 136`  ``
` 137`  `    try {`
  - → Error handling block.
` 138`  `        if (/^https?:\/\//i.test(u)) {`
` 139`  `        var a = document.createElement('a');`
` 140`  `        a.href = u;`
` 141`  `        u = a.pathname || u;`
` 142`  `    }`
` 143`  `} catch (e) { /* ignore */ }`
` 144`  ``
` 145`  `var path = u.replace(/\\/g, '/');`
` 146`  `var idx = path.toLowerCase().indexOf('/uploads/');`
` 147`  `if (idx >= 0) path = path.substring(idx + 1); // Uploads/...`
` 148`  `if (path.indexOf('~/') === 0) path = path.substring(2);`
` 149`  `path = path.replace(/^\/+/, '');`
` 150`  `if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);`
` 151`  ``
` 152`  `// path is now CourseMaterials/guid.pdf or CourseVideos/...`
` 153`  `if (!path) return '';`
` 154`  `// If only a bare filename slipped in, assume CourseMaterials`
` 155`  `if (path.indexOf('/') < 0) path = 'CourseMaterials/' + path;`
` 156`  ``
` 157`  `var root = mediaAppRoot();`
` 158`  `var url = root + '/Media.ashx?f=' + encodeURIComponent(path);`
` 159`  `if (forDownload) url += '&dl=1';`
` 160`  `return url;`
` 161`  `}`
` 162`  ``
` 163`  `function mediaKind(urlOrName) {`
` 164`  `    var s = (urlOrName || '').toLowerCase();`
` 165`  `    if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0) return 'video';`
` 166`  `    if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s)) return 'image';`
` 167`  `    if (/\.pdf(\?|$)/.test(s)) return 'pdf';`
` 168`  `    if (/\.(pptx?|docx?|pptm)(\?|$)/.test(s)) return 'office';`
` 169`  `    return 'file';`
` 170`  `}`
` 171`  ``
` 172`  `function buildMaterialPreviewHtml(viewUrl, kind, fileName) {`
` 173`  `    var safeView = escapeHtml(viewUrl);`
  - → Encode text to reduce XSS risk.
` 174`  `    var safeName = escapeHtml(fileName || 'file');`
  - → Encode text to reduce XSS risk.
` 175`  `    if (kind === 'video') {`
` 176`  `        return '<video controls preload="metadata" src="' + safeView +`
` 177`  `        '" style="max-width:100%;max-height:200px;display:block;border-radius:8px;background:#111;"></video>';`
` 178`  `    }`
` 179`  `    if (kind === 'image') {`
` 180`  `        return '<a href="' + safeView + '" target="_blank" rel="noopener">' +`
` 181`  `        '<img src="' + safeView + '" alt="' + safeName +`
` 182`  `        '" style="max-width:100%;max-height:180px;border-radius:8px;object-fit:contain;background:#f3f4f6;" /></a>';`
` 183`  `    }`
` 184`  `    if (kind === 'pdf') {`
` 185`  `        return '<iframe src="' + safeView +`
` 186`  `        '#toolbar=1" title="' + safeName +`
` 187`  `        '" style="width:100%;height:220px;border:1px solid #e5e7eb;border-radius:8px;background:#fff;"></iframe>';`
` 188`  `    }`
` 189`  `    return '<div class="text-muted small py-2"><i class="fa-solid fa-file me-1"></i>' + safeName +`
` 190`  `    ' - use Open / Download</div>';`
` 191`  `}`
` 192`  ``
` 193`  `function initMediaDropzone() {`
` 194`  `    var area = document.getElementById('mediaDropzone');`
  - → Get HTML element by id.
` 195`  `    if (!area) return;`
` 196`  `    var input = document.getElementById('mediaFileInput');`
  - → Get HTML element by id.
` 197`  `    if (!input) {`
` 198`  `        input = document.createElement('input');`
` 199`  `        input.type = 'file';`
` 200`  `        input.id = 'mediaFileInput';`
` 201`  `        input.accept = 'video/*,.mp4,.webm,.mov';`
` 202`  `        input.style.display = 'none';`
` 203`  `        area.appendChild(input);`
` 204`  `    }`
` 205`  `    var msg = area.querySelector('.dz-inner');`
` 206`  `    if (!msg) {`
` 207`  `        msg = document.createElement('div');`
` 208`  `        msg.className = 'dz-inner text-muted small';`
` 209`  `        msg.innerText = 'Click to upload video (mp4/webm/mov)';`
` 210`  `        area.appendChild(msg);`
` 211`  `    }`
` 212`  ``
` 213`  `    function uploadVideo(file) {`
` 214`  `        if (!file) return;`
` 215`  `        var ext = (file.name.split('.').pop() || '').toLowerCase();`
` 216`  `        if (['mp4', 'webm', 'mov'].indexOf(ext) < 0) {`
` 217`  `            alert('Unsupported video format. Use mp4, webm, or mov.');`
` 218`  `            return;`
` 219`  `        }`
` 220`  `        if (file.size > 200 * 1024 * 1024) {`
` 221`  `            alert('Video too large (max 200MB).');`
` 222`  `            return;`
` 223`  `        }`
` 224`  `        msg.innerText = 'Uploading ' + file.name + '...';`
` 225`  `        uploadLessonFile(file)`
` 226`  `        .then(function (resp) {`
` 227`  `            if (resp && resp.success) {`
` 228`  `                var store = resp.storePath || resp.under || resp.url;`
` 229`  `                var viewUrl = resp.serveUrl || resolveMediaUrl(store, false);`
` 230`  `                var dlUrl = resp.downloadUrl || resolveMediaUrl(store, true);`
` 231`  `                var txt = document.getElementById('txtLessonContent');`
  - → Get HTML element by id.
` 232`  `                if (txt) {`
` 233`  `                    // store portable path for DB (Uploads/CourseVideos/...)`
` 234`  `                    txt.value = store;`
` 235`  `                    txt.classList.remove('d-none');`
` 236`  `                }`
` 237`  `                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +`
  - → Update page HTML.
` 238`  `                escapeHtml(resp.fileName || file.name) + ' (' + (resp.size || file.size) + ' bytes)</span>';`
  - → Encode text to reduce XSS risk.
` 239`  `                var prev = document.getElementById('lessonMediaPreview');`
  - → Get HTML element by id.
` 240`  `                if (prev) {`
` 241`  `                    prev.innerHTML = buildMaterialPreviewHtml(viewUrl, 'video', resp.fileName || file.name) +`
  - → Update page HTML.
` 242`  `                    '<div class="mt-1"><a class="small" href="' + escapeHtml(viewUrl) + '" target="_blank">Open</a>' +`
  - → Encode text to reduce XSS risk.
` 243`  `                    ' · <a class="small" href="' + escapeHtml(dlUrl) + '">Download</a></div>' +`
  - → Encode text to reduce XSS risk.
` 244`  `                    '<div class="hint text-muted" style="font-size:.75rem;word-break:break-all;">' + escapeHtml(viewUrl) + '</div>';`
  - → Encode text to reduce XSS risk.
` 245`  `                    prev.classList.remove('d-none');`
` 246`  `                }`
` 247`  `            } else {`
` 248`  `                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));`
` 249`  `                msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';`
` 250`  `            }`
` 251`  `        })`
` 252`  `        .catch(function (err) {`
` 253`  `            console.error(err);`
` 254`  `            alert(err.message || 'Upload failed');`
` 255`  `            msg.innerText = 'Click to upload video (mp4/webm/mov, up to 200MB)';`
` 256`  `        });`
` 257`  `    }`
` 258`  ``
` 259`  `    area.addEventListener('click', function (e) {`
  - → DOM event handler.
` 260`  `        if (e.target === input) return;`
` 261`  `        e.preventDefault();`
` 262`  `        input.click();`
` 263`  `    });`
` 264`  `    input.addEventListener('change', function () {`
  - → DOM event handler.
` 265`  `        if (input.files && input.files[0]) uploadVideo(input.files[0]);`
` 266`  `        input.value = '';`
` 267`  `    });`
` 268`  `    area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });`
  - → DOM event handler.
` 269`  `    area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });`
  - → DOM event handler.
` 270`  `    area.addEventListener('drop', function (e) {`
  - → DOM event handler.
` 271`  `        e.preventDefault();`
` 272`  `        area.classList.remove('dragover');`
` 273`  `        if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadVideo(e.dataTransfer.files[0]);`
` 274`  `    });`
` 275`  `}`
` 276`  ``
` 277`  `function initMaterialDropzone() {`
` 278`  `    var area = document.getElementById('materialDropzone');`
  - → Get HTML element by id.
` 279`  `    if (!area) return;`
` 280`  `    var input = document.getElementById('materialFileInput');`
  - → Get HTML element by id.
` 281`  `    if (!input) {`
` 282`  `        input = document.createElement('input');`
` 283`  `        input.type = 'file';`
` 284`  `        input.id = 'materialFileInput';`
` 285`  `        input.accept = '.pdf,.ppt,.pptx,.docx,image/*,video/*,.mp4,.webm';`
` 286`  `        input.style.display = 'none';`
` 287`  `        area.appendChild(input);`
` 288`  `    }`
` 289`  `    var msg = area.querySelector('.dz-inner');`
` 290`  `    if (!msg) {`
` 291`  `        msg = document.createElement('div');`
` 292`  `        msg.className = 'dz-inner text-muted small';`
` 293`  `        msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 294`  `        area.appendChild(msg);`
` 295`  `    }`
` 296`  ``
` 297`  `    function uploadMaterial(file) {`
` 298`  `        if (!file) return;`
` 299`  `        var allowed = ['pdf', 'ppt', 'pptx', 'docx', 'doc', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4', 'webm', 'mov'];`
` 300`  `        var ext = (file.name.split('.').pop() || '').toLowerCase();`
` 301`  `        if (allowed.indexOf(ext) < 0) {`
` 302`  `            alert('Unsupported file format: .' + ext);`
` 303`  `            return;`
` 304`  `        }`
` 305`  `        var maxMb = (ext === 'mp4' || ext === 'webm' || ext === 'mov') ? 200 : 30;`
` 306`  `        if (file.size > maxMb * 1024 * 1024) {`
` 307`  `            alert('File too large (max ' + maxMb + 'MB).');`
` 308`  `            return;`
` 309`  `        }`
` 310`  `        msg.innerText = 'Uploading ' + file.name + '...';`
` 311`  `        uploadLessonFile(file)`
` 312`  `        .then(function (resp) {`
` 313`  `            if (resp && resp.success) {`
` 314`  `                var materialsField = document.getElementById('lessonMaterials');`
  - → Get HTML element by id.
` 315`  `                var materials = [];`
` 316`  `                try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }`
  - → JS object ↔ JSON text.
` 317`  `                var store = resp.storePath || ('Uploads/' + (resp.under || ''));`
` 318`  `                materials.push({`
` 319`  `                    storePath: store,`
` 320`  `                    url: store,`
` 321`  `                    under: resp.under || '',`
` 322`  `                    fileName: resp.fileName || file.name,`
` 323`  `                    serveUrl: resp.serveUrl || resolveMediaUrl(store, false),`
` 324`  `                    downloadUrl: resp.downloadUrl || resolveMediaUrl(store, true)`
` 325`  `                });`
` 326`  `                materialsField.value = JSON.stringify(materials);`
  - → JS object ↔ JSON text.
` 327`  `                renderAttachmentsList();`
` 328`  `                msg.innerHTML = '<span class="text-success"><i class="fa-solid fa-circle-check me-1"></i>Uploaded: ' +`
  - → Update page HTML.
` 329`  `                escapeHtml(resp.fileName || file.name) + ' - preview below</span>';`
  - → Encode text to reduce XSS risk.
` 330`  `            } else {`
` 331`  `                alert('Upload failed: ' + ((resp && resp.message) || 'Unknown error'));`
` 332`  `                msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 333`  `            }`
` 334`  `        })`
` 335`  `        .catch(function (err) {`
` 336`  `            console.error(err);`
` 337`  `            alert(err.message || 'Upload failed');`
` 338`  `            msg.innerText = 'Click to upload materials (pdf, pptx, docx, images, video)';`
` 339`  `        });`
` 340`  `    }`
` 341`  ``
` 342`  `    area.addEventListener('click', function (e) {`
  - → DOM event handler.
` 343`  `        if (e.target === input) return;`
` 344`  `        e.preventDefault();`
` 345`  `        input.click();`
` 346`  `    });`
` 347`  `    input.addEventListener('change', function () {`
  - → DOM event handler.
` 348`  `        if (input.files && input.files[0]) uploadMaterial(input.files[0]);`
` 349`  `        input.value = '';`
` 350`  `    });`
` 351`  `    area.addEventListener('dragover', function (e) { e.preventDefault(); area.classList.add('dragover'); });`
  - → DOM event handler.
` 352`  `    area.addEventListener('dragleave', function () { area.classList.remove('dragover'); });`
  - → DOM event handler.
` 353`  `    area.addEventListener('drop', function (e) {`
  - → DOM event handler.
` 354`  `        e.preventDefault();`
` 355`  `        area.classList.remove('dragover');`
` 356`  `        if (e.dataTransfer.files && e.dataTransfer.files[0]) uploadMaterial(e.dataTransfer.files[0]);`
` 357`  `    });`
` 358`  `}`
` 359`  ``
` 360`  `function renderAttachmentsList() {`
` 361`  `    var attachments = document.getElementById('lessonAttachments');`
  - → Get HTML element by id.
` 362`  `    var materialsField = document.getElementById('lessonMaterials');`
  - → Get HTML element by id.
` 363`  `    if (!attachments || !materialsField) return;`
` 364`  `    attachments.innerHTML = '';`
  - → Update page HTML.
` 365`  `    var materials = [];`
` 366`  `    try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }`
  - → JS object ↔ JSON text.
` 367`  `    if (!materials.length) return;`
` 368`  ``
` 369`  `    var heading = document.createElement('div');`
` 370`  `    heading.className = 'fw-semibold small text-muted mb-2';`
` 371`  `    heading.textContent = 'Materials (' + materials.length + ') - preview & download';`
` 372`  `    attachments.appendChild(heading);`
` 373`  ``
` 374`  `    materials.forEach(function (m, idx) {`
` 375`  `        var raw = m.url || m.mediaLink || '';`
` 376`  `        var viewUrl = m.serveUrl || resolveMediaUrl(raw, false);`
` 377`  `        var dlUrl = m.downloadUrl || resolveMediaUrl(raw, true);`
` 378`  `        var name = m.fileName || m.textContent || raw || ('File ' + (idx + 1));`
` 379`  `        var kind = mediaKind(name + ' ' + raw);`
` 380`  ``
` 381`  `        var card = document.createElement('div');`
` 382`  `        card.className = 'mb-2 p-2 rounded border bg-white';`
` 383`  `        card.innerHTML =`
  - → Update page HTML.
` 384`  `        '<div class="d-flex align-items-center gap-2 mb-2">' +`
` 385`  `        '<i class="fa-solid fa-paperclip text-muted"></i>' +`
` 386`  `        '<span class="small flex-grow-1 text-truncate fw-semibold">' + escapeHtml(name) + '</span>' +`
  - → Encode text to reduce XSS risk.
` 387`  `        '<a class="btn btn-sm btn-outline-secondary py-0" href="' + escapeHtml(viewUrl) + '" target="_blank" rel="noopener">Open</a>' +`
  - → Encode text to reduce XSS risk.
` 388`  `        '<a class="btn btn-sm btn-outline-primary py-0" href="' + escapeHtml(dlUrl) + '" download>Download</a>' +`
  - → Encode text to reduce XSS risk.
` 389`  `        '<button type="button" class="btn btn-sm btn-link text-danger p-0" data-rm="' + idx + '">Remove</button>' +`
` 390`  `        '</div>' +`
` 391`  `        '<div class="material-preview">' + buildMaterialPreviewHtml(viewUrl, kind, name) + '</div>';`
` 392`  ``
` 393`  `        card.querySelector('[data-rm]').addEventListener('click', function () {`
  - → DOM event handler.
` 394`  `            removeAttachment(raw || m.url);`
` 395`  `        });`
` 396`  `        attachments.appendChild(card);`
` 397`  `    });`
` 398`  `}`
` 399`  ``
` 400`  `function removeAttachment(url) {`
` 401`  `    var materialsField = document.getElementById('lessonMaterials');`
  - → Get HTML element by id.
` 402`  `    if (!materialsField) return;`
` 403`  `    var materials = [];`
` 404`  `    try { materials = JSON.parse(materialsField.value || '[]'); } catch (e) { materials = []; }`
  - → JS object ↔ JSON text.
` 405`  `    materials = materials.filter(function (m) {`
` 406`  `        return (m.url !== url) && (m.mediaLink !== url);`
` 407`  `    });`
` 408`  `    materialsField.value = JSON.stringify(materials);`
  - → JS object ↔ JSON text.
` 409`  `    renderAttachmentsList();`
` 410`  `}`
` 411`  ``

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
