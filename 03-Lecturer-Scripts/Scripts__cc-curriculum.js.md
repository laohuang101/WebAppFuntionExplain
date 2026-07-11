# cc-curriculum.js
**Source:** `Pages/Lecturer/Scripts/cc-curriculum.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 420
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `view` | `const/let/var` | Holds “view” for this scope. |
| `chapters` | `const/let/var` | Often a collection related to chapters (plural name). |
| `secDiv` | `const/let/var` | Holds “sec Div” for this scope. |
| `lessonsHtml` | `const/let/var` | Holds “lessons Html” for this scope. |
| `lessons` | `const/let/var` | Often a collection related to lessons (plural name). |
| `type` | `const/let/var` | Holds “type” for this scope. |
| `typeClass` | `const/let/var` | Often a collection related to type Class (plural name). |
| `title` | `const/let/var` | Title of course work / page heading. |
| `errDiv` | `const/let/var` | Holds “err Div” for this scope. |
| `chid` | `const/let/var` | Chapter ID (Chapters.ChID). |
| `saveBtn` | `const/let/var` | Holds “save Btn” for this scope. |
| `htmlEditor` | `const/let/var` | Holds “html Editor” for this scope. |
| `mediaPrev` | `const/let/var` | Holds “media Prev” for this scope. |
| `mediaMsg` | `const/let/var` | Holds “media Msg” for this scope. |
| `matMsg` | `const/let/var` | Holds “mat Msg” for this scope. |
| `lessonType` | `const/let/var` | Holds “lesson Type” for this scope. |
| `mats` | `const/let/var` | Often a collection related to mats (plural name). |
| `cleaned` | `const/let/var` | Holds “cleaned” for this scope. |
| `vUrl` | `const/let/var` | URL string. |
| `lbl` | `const/let/var` | UI control reference (lbl). |
| `textarea` | `const/let/var` | Holds “textarea” for this scope. |
| `editorToolbar` | `const/let/var` | Holds “editor Toolbar” for this scope. |
| `mediaDZ` | `const/let/var` | Holds “media DZ” for this scope. |
| `materialDZ` | `const/let/var` | Holds “material DZ” for this scope. |
| `attachments` | `const/let/var` | Often a collection related to attachments (plural name). |
| `content` | `const/let/var` | Submission body text or JSON payload in CWSubmissions. |
| `materialsField` | `const/let/var` | Holds “materials Field” for this scope. |
| `materialsRaw` | `const/let/var` | Holds “materials Raw” for this scope. |
| `materialsArr` | `const/let/var` | Holds “materials Arr” for this scope. |
| `url` | `const/let/var` | HTTP URL to media or page. |
| `firstUrl` | `const/let/var` | URL string. |
| `firstName` | `const/let/var` | Holds “first Name” for this scope. |
| `kind` | `const/let/var` | Upload kind (material/video/thumbnail/submission). |
| `plain` | `const/let/var` | Text without META trailer (student-visible instructions). |
| `schid` | `const/let/var` | SubChapter / lesson ID. |
| `matsJson` | `const/let/var` | Holds “mats Json” for this scope. |

## Functions / methods (10 found)

### `loadCurriculumView` — lines 2–101

#### Signature

```javascript
function loadCurriculumView()
```

#### What it is

Reads/loads data related to **Curriculum View** and returns it for display or further use.

#### How it works

1. If the previous step failed, show the error and stop.
2. Attach a browser event handler (click, load, change, …).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `view` | `—` | Holds “view” for this scope.  DOM element from the page. |
| `chapters` | `—` | Often a collection related to chapters (plural name). |
| `secDiv` | `—` | Holds “sec Div” for this scope. |
| `lessonsHtml` | `—` | Holds “lessons Html” for this scope.  Literal text string. |
| `lessons` | `—` | Often a collection related to lessons (plural name). |
| `type` | `—` | Holds “type” for this scope. |
| `typeClass` | `—` | Often a collection related to type Class (plural name).  Literal text string. |

#### Code

```javascript
   2 | 
   3 | function loadCurriculumView() {
   4 |     const view = document.getElementById('curriculumView');
   5 |     if (!view) return;
   6 | 
   7 |     if (!currentCourseId) {
   8 |         view.innerHTML = '<div class="text-center py-4 text-muted">Save basic info first (step 1) before adding sections.</div>';
   9 |         return;
  10 |     }
  11 | 
  12 |     view.innerHTML = '<div class="text-center py-4"><i class="fa-solid fa-circle-notch fa-spin me-2 text-muted"></i>Loading curriculum...</div>';
  13 | 
  14 |     curriculumApi('get', { cid: currentCourseId })
  15 |     .then(function (resObj) {
  16 |         if (!resObj || !resObj.success) {
  17 |             view.innerHTML = '<div class="text-danger py-4 text-center">Failed to load curriculum: ' +
  18 |             escapeHtml((resObj && resObj.message) || 'Unknown error') + '</div>';
  19 |             return;
  20 |         }
  21 | 
  22 |         const chapters = resObj.chapters || [];
  23 |         if (chapters.length === 0) {
  24 |             view.innerHTML = '<div class="text-center py-4 text-muted">No sections added yet. Click "+ Add New Section" to start building your course.</div>';
  25 |             return;
  26 |         }
  27 | 
  28 |         view.innerHTML = '';
  29 |         chapters.forEach(function (ch) {
  30 |             const secDiv = document.createElement('div');
  31 |             secDiv.className = 'section-item';
  32 |             secDiv.setAttribute('data-chid', ch.chid);
  33 | 
  34 |             let lessonsHtml = '';
  35 |             const lessons = ch.lessons || [];
  36 |             if (lessons.length > 0) {
  37 |                 lessons.forEach(function (les, idx) {
  38 |                     const type = (les.type || 'Text');
  39 |                     const typeClass = 'lesson-type-' + String(type).toLowerCase();
  40 |                     lessonsHtml +=
  41 |                     '<div class="lesson-item">' +
  42 |                     '<div class="lesson-meta d-flex align-items-center gap-2">' +
  43 |                     '<span class="text-muted small">' + (idx + 1) + '.</span>' +
  44 |                     '<span class="lesson-type-badge ' + typeClass + '">' + escapeHtml(type) + '</span>' +
  45 |                     '<span class="fw-semibold">' + escapeHtml(les.title || '') + '</span>' +
  46 |                     '</div>' +
  47 |                     '<div class="d-flex gap-2">' +
  48 |                     '<button type="button" class="btn btn-sm btn-link p-0 text-secondary" data-edit-lesson="' + les.schid + '" data-chid="' + ch.chid + '" title="Edit Lesson"><i class="fa-solid fa-pencil"></i></button>' +
  49 |                     '<button type="button" class="btn btn-sm btn-link p-0 text-danger" data-del-lesson="' + les.schid + '" title="Delete Lesson"><i class="fa-solid fa-trash"></i></button>' +
  50 |                     '</div></div>';
  51 |                 });
  52 |             } else {
  53 |                 lessonsHtml = '<div class="text-muted small py-2 px-1">No lessons added to this section.</div>';
  54 |             }
  55 | 
  56 |             secDiv.innerHTML =
  57 |             '<div class="section-header">' +
  58 |             '<span class="fw-bold">' + escapeHtml(ch.title || '') + '</span>' +
  59 |             '<div class="d-flex gap-2">' +
  60 |             '<button type="button" class="btn btn-sm btn-link p-0 text-secondary" data-edit-section="' + ch.chid + '" data-title="' + escapeHtml(ch.title || '') + '" title="Edit Section Title"><i class="fa-solid fa-pencil"></i></button>' +
  61 |             '<button type="button" class="btn btn-sm btn-link p-0 text-danger" data-del-section="' + ch.chid + '" title="Delete Section"><i class="fa-solid fa-trash"></i></button>' +
  62 |             '</div></div>' +
  63 |             '<div class="lesson-list">' + lessonsHtml +
  64 |             '<button type="button" class="btn btn-sm btn-light border w-100 text-muted py-2 mt-2" data-add-lesson="' + ch.chid + '" style="border-style: dashed !important;">' +
  65 |             '<i class="fa-solid fa-plus me-1"></i> Add New Lesson</button></div>';
  66 | 
  67 |             view.appendChild(secDiv);
  68 |         });
  69 | 
  70 |         // Bind section/lesson actions without inline onclick (avoids quote bugs)
  71 |         view.querySelectorAll('[data-edit-section]').forEach(function (btn) {
  72 |             btn.addEventListener('click', function () {
  73 |                 editSection(parseInt(btn.getAttribute('data-edit-section'), 10), btn.getAttribute('data-title') || '');
  74 |             });
  75 |         });
  76 |         view.querySelectorAll('[data-del-section]').forEach(function (btn) {
  77 |             btn.addEventListener('click', function () {
  78 |                 deleteSection(parseInt(btn.getAttribute('data-del-section'), 10));
  79 |             });
  80 |         });
  81 |         view.querySelectorAll('[data-add-lesson]').forEach(function (btn) {
  82 |             btn.addEventListener('click', function () {
  83 |                 showAddLessonModal(parseInt(btn.getAttribute('data-add-lesson'), 10));
  84 |             });
  85 |         });
  86 |         view.querySelectorAll('[data-edit-lesson]').forEach(function (btn) {
  87 |             btn.addEventListener('click', function () {
  88 |                 editLesson(parseInt(btn.getAttribute('data-edit-lesson'), 10), parseInt(btn.getAttribute('data-chid'), 10));
  89 |             });
  90 |         });
  91 |         view.querySelectorAll('[data-del-lesson]').forEach(function (btn) {
  92 |             btn.addEventListener('click', function () {
  93 |                 deleteLesson(parseInt(btn.getAttribute('data-del-lesson'), 10));
  94 |             });
  95 |         });
  96 |     })
  97 |     .catch(function (err) {
  98 |         console.error('Error loading curriculum: ', err);
  99 |         view.innerHTML = '<div class="text-danger py-4 text-center">Failed to load curriculum.</div>';
 100 |     });
 101 | }
```

---

### `showAddSectionModal` — lines 101–109

#### Signature

```javascript
function showAddSectionModal()
```

#### What it is

Updates the page HTML for **show Add Section Modal**.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 101 | 
 102 | 
 103 | function showAddSectionModal() {
 104 |     editingSectionId = null;
 105 |     document.getElementById('txtSectionTitle').value = '';
 106 |     document.getElementById('sectionModalTitle').innerText = 'Add New Section';
 107 |     document.getElementById('sectionModalError').style.display = 'none';
 108 |     showModal('sectionModal');
 109 | }
```

---

### `editSection` — lines 109–117

#### Signature

```javascript
function editSection(chid, title)
```

#### What it is

Function `editSection` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `chid` | `—` | Chapter ID (Chapters.ChID). |
| `title` | `—` | Title of course work / page heading. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 109 | 
 110 | 
 111 | function editSection(chid, title) {
 112 |     editingSectionId = chid;
 113 |     document.getElementById('txtSectionTitle').value = title || '';
 114 |     document.getElementById('sectionModalTitle').innerText = 'Edit Section';
 115 |     document.getElementById('sectionModalError').style.display = 'none';
 116 |     showModal('sectionModal');
 117 | }
```

---

### `saveSection` — lines 117–163

#### Signature

```javascript
function saveSection()
```

#### What it is

Saves or updates **save Section** in the database or UI state.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `title` | `—` | Title of course work / page heading.  DOM element from the page. |
| `errDiv` | `—` | Holds “err Div” for this scope.  DOM element from the page. |
| `chid` | `—` | Chapter ID (Chapters.ChID). |
| `saveBtn` | `—` | Holds “save Btn” for this scope. |

#### Code

```javascript
 117 | 
 118 | 
 119 | function saveSection() {
 120 |     const title = document.getElementById('txtSectionTitle').value.trim();
 121 |     const errDiv = document.getElementById('sectionModalError');
 122 |     errDiv.style.display = 'none';
 123 | 
 124 |     if (!title) {
 125 |         errDiv.innerText = 'Please enter a section title.';
 126 |         errDiv.style.display = 'block';
 127 |         return;
 128 |     }
 129 |     if (!currentCourseId) {
 130 |         errDiv.innerText = 'Course is not saved yet. Go back to step 1.';
 131 |         errDiv.style.display = 'block';
 132 |         return;
 133 |     }
 134 | 
 135 |     // Send 0 instead of null - ASP.NET WebMethods often reject null int?
 136 |     const chid = editingSectionId ? parseInt(editingSectionId, 10) : 0;
 137 | 
 138 |     const saveBtn = document.querySelector('#sectionModal .btn-pill-accent');
 139 |     if (saveBtn) { saveBtn.disabled = true; saveBtn.innerText = 'Saving...'; }
 140 | 
 141 |     curriculumApi('save_section', {
 142 |         chid: chid,
 143 |         cid: currentCourseId,
 144 |         title: title
 145 |     })
 146 |     .then(function (resObj) {
 147 |         if (resObj && resObj.success) {
 148 |             hideModal('sectionModal');
 149 |             setTimeout(function () { loadCurriculumView(); }, 150);
 150 |         } else {
 151 |             errDiv.innerText = (resObj && resObj.message) || 'Failed to save section.';
 152 |             errDiv.style.display = 'block';
 153 |         }
 154 |     })
 155 |     .catch(function (err) {
 156 |         errDiv.innerText = (err && err.message) || 'Network error saving section.';
 157 |         errDiv.style.display = 'block';
 158 |         console.error(err);
 159 |     })
 160 |     .finally(function () {
 161 |         if (saveBtn) { saveBtn.disabled = false; saveBtn.innerText = 'Save Section'; }
 162 |     });
 163 | }
```

---

### `deleteSection` — lines 163–174

#### Signature

```javascript
function deleteSection(chid)
```

#### What it is

Deletes or clears **delete Section** (data or temporary state).

#### How it works

1. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `chid` | `—` | Chapter ID (Chapters.ChID). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 163 | 
 164 | 
 165 | function deleteSection(chid) {
 166 |     if (!confirm('Are you sure you want to delete this section? All lessons inside will be deleted too!')) return;
 167 | 
 168 |     curriculumApi('delete_section', { chid: chid })
 169 |     .then(function (resObj) {
 170 |         if (resObj && resObj.success) loadCurriculumView();
 171 |         else alert('Delete failed: ' + ((resObj && resObj.message) || 'Unknown error'));
 172 |     })
 173 |     .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
 174 | }
```

---

### `showAddLessonModal` — lines 174–199

#### Signature

```javascript
function showAddLessonModal(chid)
```

#### What it is

Updates the page HTML for **show Add Lesson Modal**.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `chid` | `—` | Chapter ID (Chapters.ChID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `htmlEditor` | `—` | Holds “html Editor” for this scope.  DOM element from the page. |
| `mediaPrev` | `—` | Holds “media Prev” for this scope.  DOM element from the page. |
| `mediaMsg` | `—` | Holds “media Msg” for this scope. |
| `matMsg` | `—` | Holds “mat Msg” for this scope. |

#### Code

```javascript
 174 | 
 175 | 
 176 | function showAddLessonModal(chid) {
 177 |     targetChapterId = chid;
 178 |     editingLessonId = null;
 179 |     document.getElementById('txtLessonTitle').value = '';
 180 |     document.getElementById('ddlLessonType').value = 'Text';
 181 |     document.getElementById('txtLessonContent').value = '';
 182 |     document.getElementById('lessonModalTitle').innerText = 'Add New Lesson';
 183 |     document.getElementById('lessonModalError').style.display = 'none';
 184 |     document.getElementById('lessonModalError').innerText = '';
 185 | 
 186 |     var htmlEditor = document.getElementById('htmlEditor');
 187 |     if (htmlEditor) htmlEditor.innerHTML = '';
 188 |     document.getElementById('lessonMaterials').value = '[]';
 189 |     var mediaPrev = document.getElementById('lessonMediaPreview');
 190 |     if (mediaPrev) { mediaPrev.innerHTML = ''; mediaPrev.classList.add('d-none'); }
 191 |     var mediaMsg = document.querySelector('#mediaDropzone .dz-inner');
 192 |     if (mediaMsg) mediaMsg.innerHTML = '<i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>Click or drag a video here (mp4 / webm / mov, up to 200MB)';
 193 |     var matMsg = document.querySelector('#materialDropzone .dz-inner');
 194 |     if (matMsg) matMsg.innerHTML = '<i class="fa-solid fa-file-arrow-up d-block mb-2 fs-4"></i>Click or drag materials (pdf, pptx, docx, images, up to 30MB)';
 195 |     if (typeof renderAttachmentsList === 'function') renderAttachmentsList();
 196 | 
 197 |     toggleLessonContentFields();
 198 |     showModal('lessonModal');
 199 | }
```

---

### `editLesson` — lines 199–248

#### Signature

```javascript
function editLesson(schid, chid)
```

#### What it is

Function `editLesson` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).
2. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `schid` | `—` | SubChapter / lesson ID. |
| `chid` | `—` | Chapter ID (Chapters.ChID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `lessonType` | `—` | Holds “lesson Type” for this scope. |
| `htmlEditor` | `—` | Holds “html Editor” for this scope.  DOM element from the page. |
| `mats` | `—` | Often a collection related to mats (plural name). |
| `cleaned` | `—` | Holds “cleaned” for this scope. |
| `mediaPrev` | `—` | Holds “media Prev” for this scope.  DOM element from the page. |
| `vUrl` | `—` | URL string. |

#### Code

```javascript
 199 | 
 200 | 
 201 | function editLesson(schid, chid) {
 202 |     targetChapterId = chid;
 203 |     editingLessonId = schid;
 204 |     document.getElementById('lessonModalTitle').innerText = 'Edit Lesson';
 205 |     document.getElementById('lessonModalError').style.display = 'none';
 206 | 
 207 |     curriculumApi('get_lesson', { schid: schid })
 208 |     .then(function (resObj) {
 209 |         if (resObj && resObj.success) {
 210 |             document.getElementById('txtLessonTitle').value = resObj.title || '';
 211 |             var lessonType = resObj.type || 'Text';
 212 |             // Map DB types that are not in the dropdown
 213 |             if (['PDF', 'Image', 'File'].indexOf(lessonType) >= 0) lessonType = 'Text';
 214 |             document.getElementById('ddlLessonType').value = lessonType;
 215 |             document.getElementById('txtLessonContent').value = resObj.content || '';
 216 |             var htmlEditor = document.getElementById('htmlEditor');
 217 |             if (htmlEditor && lessonType === 'Text') {
 218 |                 htmlEditor.innerHTML = resObj.content || '';
 219 |             }
 220 |             // Restore file materials so re-save does not wipe them
 221 |             var mats = resObj.materials || [];
 222 |             var cleaned = (mats || []).filter(function (m) {
 223 |                 return m && (m.url || m.mediaLink);
 224 |             }).map(function (m) {
 225 |                 return {
 226 |                     url: m.url || m.mediaLink,
 227 |                     fileName: m.fileName || m.textContent || 'file',
 228 |                     type: m.type || ''
 229 |                 };
 230 |             });
 231 |             document.getElementById('lessonMaterials').value = JSON.stringify(cleaned);
 232 |             var mediaPrev = document.getElementById('lessonMediaPreview');
 233 |             if (mediaPrev && lessonType === 'Video' && resObj.content) {
 234 |                 var vUrl = resolveMediaUrl(resObj.content, false);
 235 |                 mediaPrev.innerHTML = buildMaterialPreviewHtml(vUrl, 'video', 'Lesson video') +
 236 |                 '<div class="mt-1"><a class="small" href="' + escapeHtml(vUrl) + '" target="_blank">Open</a> · ' +
 237 |                 '<a class="small" href="' + escapeHtml(resolveMediaUrl(resObj.content, true)) + '">Download</a></div>';
 238 |                 mediaPrev.classList.remove('d-none');
 239 |             }
 240 |             toggleLessonContentFields();
 241 |             renderAttachmentsList();
 242 |             showModal('lessonModal');
 243 |         } else {
 244 |             alert('Failed to load lesson details: ' + ((resObj && resObj.message) || ''));
 245 |         }
 246 |     })
 247 |     .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
 248 | }
```

---

### `toggleLessonContentFields` — lines 248–290

#### Signature

```javascript
function toggleLessonContentFields()
```

#### What it is

Function `toggleLessonContentFields` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `type` | `—` | Holds “type” for this scope.  DOM element from the page. |
| `lbl` | `—` | UI control reference (lbl).  DOM element from the page. |
| `textarea` | `—` | Holds “textarea” for this scope.  DOM element from the page. |
| `htmlEditor` | `—` | Holds “html Editor” for this scope.  DOM element from the page. |
| `editorToolbar` | `—` | Holds “editor Toolbar” for this scope.  DOM element from the page. |
| `mediaDZ` | `—` | Holds “media DZ” for this scope.  DOM element from the page. |
| `materialDZ` | `—` | Holds “material DZ” for this scope.  DOM element from the page. |
| `attachments` | `—` | Often a collection related to attachments (plural name).  DOM element from the page. |

#### Code

```javascript
 248 | 
 249 | 
 250 | function toggleLessonContentFields() {
 251 |     const type = document.getElementById('ddlLessonType').value;
 252 |     const lbl = document.getElementById('lblLessonContent');
 253 |     const textarea = document.getElementById('txtLessonContent');
 254 | 
 255 |     const htmlEditor = document.getElementById('htmlEditor');
 256 |     const editorToolbar = document.getElementById('editorToolbar');
 257 |     const mediaDZ = document.getElementById('mediaDropzone');
 258 |     const materialDZ = document.getElementById('materialDropzone');
 259 |     const attachments = document.getElementById('lessonAttachments');
 260 | 
 261 |     // Hide all optional areas first
 262 |     if(htmlEditor) htmlEditor.style.display = 'none';
 263 |     if(editorToolbar) editorToolbar.style.display = 'none';
 264 |     if(textarea) textarea.classList.add('d-none');
 265 |     if(mediaDZ) mediaDZ.style.display = 'none';
 266 |     if(materialDZ) materialDZ.style.display = 'none';
 267 |     if(attachments) attachments.style.display = 'none';
 268 | 
 269 |     if (type === 'Video') {
 270 |         lbl.innerText = 'Video URL / Upload';
 271 |         if(mediaDZ) mediaDZ.style.display = 'block';
 272 |         if(textarea) textarea.classList.remove('d-none');
 273 |         textarea.placeholder = 'e.g., https://example.com/video.mp4 or upload below';
 274 |         // Extra file materials still allowed for Video lessons
 275 |         if(materialDZ) materialDZ.style.display = 'block';
 276 |         if(attachments) attachments.style.display = 'block';
 277 |     } else if (type === 'Quiz') {
 278 |         lbl.innerText = 'Quiz Question Description';
 279 |         if(textarea) textarea.classList.remove('d-none');
 280 |         textarea.placeholder = 'Provide the quiz questions or description for the student...';
 281 |         if(materialDZ) materialDZ.style.display = 'block';
 282 |         if(attachments) attachments.style.display = 'block';
 283 |     } else {
 284 |         lbl.innerText = 'Content Body';
 285 |         if(editorToolbar) editorToolbar.style.display = 'flex';
 286 |         if(htmlEditor) htmlEditor.style.display = 'block';
 287 |         if(materialDZ) materialDZ.style.display = 'block';
 288 |         if(attachments) attachments.style.display = 'block';
 289 |     }
 290 | }
```

---

### `saveLesson` — lines 290–408

#### Signature

```javascript
function saveLesson()
```

#### What it is

Saves or updates **save Lesson** in the database or UI state.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).
2. Parse the server JSON response into a JavaScript object.
3. Validate input; if invalid, stop and return an error/message.
4. Convert a JavaScript object into a JSON string for the server.
5. Show a simple popup message to the user.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `title` | `—` | Title of course work / page heading.  DOM element from the page. |
| `type` | `—` | Holds “type” for this scope.  DOM element from the page. |
| `errDiv` | `—` | Holds “err Div” for this scope.  DOM element from the page. |
| `content` | `—` | Submission body text or JSON payload in CWSubmissions.  Literal text string. |
| `htmlEditor` | `—` | Holds “html Editor” for this scope.  DOM element from the page. |
| `materialsField` | `—` | Holds “materials Field” for this scope.  DOM element from the page. |
| `materialsRaw` | `—` | Holds “materials Raw” for this scope. |
| `materialsArr` | `—` | Holds “materials Arr” for this scope. |
| `url` | `—` | HTTP URL to media or page. |
| `firstUrl` | `—` | URL string. |
| `firstName` | `—` | Holds “first Name” for this scope. |
| `kind` | `—` | Upload kind (material/video/thumbnail/submission). |
| `plain` | `—` | Text without META trailer (student-visible instructions). |
| `schid` | `—` | SubChapter / lesson ID. |
| `saveBtn` | `—` | Holds “save Btn” for this scope. |
| `matsJson` | `—` | Holds “mats Json” for this scope.  JSON serialize/parse result. |

#### Code

```javascript
 290 | 
 291 | 
 292 | function saveLesson() {
 293 |     var title = document.getElementById('txtLessonTitle').value.trim();
 294 |     var type = document.getElementById('ddlLessonType').value;
 295 |     var errDiv = document.getElementById('lessonModalError');
 296 |     errDiv.style.display = 'none';
 297 |     errDiv.innerText = '';
 298 | 
 299 |     if (!title) {
 300 |         errDiv.innerText = 'Please enter a lesson title.';
 301 |         errDiv.style.display = 'block';
 302 |         return;
 303 |     }
 304 |     if (!targetChapterId) {
 305 |         errDiv.innerText = 'No section selected. Close and open Add Lesson from a section.';
 306 |         errDiv.style.display = 'block';
 307 |         return;
 308 |     }
 309 | 
 310 |     var content = '';
 311 |     if (type === 'Video') {
 312 |         content = document.getElementById('txtLessonContent').value.trim();
 313 |     } else if (type === 'Quiz') {
 314 |         content = document.getElementById('txtLessonContent').value.trim();
 315 |     } else {
 316 |         var htmlEditor = document.getElementById('htmlEditor');
 317 |         content = htmlEditor ? htmlEditor.innerHTML.trim() : document.getElementById('txtLessonContent').value.trim();
 318 |         // treat empty editor shells as empty
 319 |         if (content === '<br>' || content === '<div><br></div>' || content === '<p><br></p>') content = '';
 320 |     }
 321 | 
 322 |     var materialsField = document.getElementById('lessonMaterials');
 323 |     var materialsRaw = materialsField ? (materialsField.value || '').trim() : '';
 324 |     var materialsArr = [];
 325 |     try { materialsArr = materialsRaw ? JSON.parse(materialsRaw) : []; } catch (e) { materialsArr = []; }
 326 |     if (!Array.isArray(materialsArr)) materialsArr = [];
 327 | 
 328 |     // Normalize each material to storePath + url for the server
 329 |     materialsArr = materialsArr.map(function (m) {
 330 |         var url = (m && (m.storePath || m.url || m.mediaLink)) || '';
 331 |         return {
 332 |             storePath: m.storePath || url,
 333 |             url: url,
 334 |             fileName: (m && m.fileName) || 'file',
 335 |             serveUrl: (m && m.serveUrl) || '',
 336 |             downloadUrl: (m && m.downloadUrl) || ''
 337 |         };
 338 |     }).filter(function (m) { return !!m.url; });
 339 | 
 340 |     // Allow save if we have content OR at least one uploaded material
 341 |     if (!content && materialsArr.length === 0 && type !== 'Quiz') {
 342 |         errDiv.innerText = type === 'Video'
 343 |         ? 'Upload a video or paste a video URL.'
 344 |         : 'Enter lesson content or upload at least one material file.';
 345 |         errDiv.style.display = 'block';
 346 |         return;
 347 |     }
 348 |     if (type === 'Quiz' && !content) {
 349 |         content = 'Quiz / assignment';
 350 |     }
 351 | 
 352 |     // Promote first uploaded file so preview always gets a real media path
 353 |     if (materialsArr.length > 0) {
 354 |         var firstUrl = materialsArr[0].storePath || materialsArr[0].url || '';
 355 |         var firstName = materialsArr[0].fileName || firstUrl;
 356 |         var kind = mediaKind(firstName + ' ' + firstUrl);
 357 |         if (type === 'Text' || type === 'Video') {
 358 |             // Video lesson: ensure content is the video path
 359 |             if (type === 'Video' && firstUrl && !content) content = firstUrl;
 360 |             // Text lesson with only a short placeholder body → use file as primary media
 361 |             var plain = (content || '').replace(/<[^>]+>/g, '').trim();
 362 |             if (type === 'Text' && firstUrl && (plain.length < 40 || plain === title)) {
 363 |                 if (kind === 'video') type = 'Video';
 364 |                 else if (kind === 'pdf') type = 'PDF';
 365 |                 else if (kind === 'image') type = 'Image';
 366 |                 else type = 'PDF';
 367 |                 content = firstUrl;
 368 |             }
 369 |         }
 370 |     }
 371 | 
 372 |     var schid = editingLessonId ? parseInt(editingLessonId, 10) : 0;
 373 |     var saveBtn = document.querySelector('#lessonModal .btn-pill-accent');
 374 |     if (saveBtn) { saveBtn.disabled = true; saveBtn.textContent = 'Saving...'; }
 375 | 
 376 |     var matsJson = materialsArr.length ? JSON.stringify(materialsArr) : '[]';
 377 | 
 378 |     curriculumApi('save_lesson', {
 379 |         schid: schid,
 380 |         chid: parseInt(targetChapterId, 10),
 381 |         title: title,
 382 |         type: type,
 383 |         content: content,
 384 |         materialsJson: matsJson
 385 |     })
 386 |     .then(function (resObj) {
 387 |         if (resObj && resObj.success) {
 388 |             if (resObj.warning) console.warn('Lesson warning:', resObj.warning);
 389 |             if (materialsArr.length && resObj.materialsSaved === 0) {
 390 |                 alert('Lesson saved, but materials may not have been stored (materialsSaved=0). Check StudyMats.MediaLink. Warning: ' +
 391 |                 (resObj.warning || 'none'));
 392 |             }
 393 |             hideModal('lessonModal');
 394 |             setTimeout(function () { loadCurriculumView(); }, 200);
 395 |         } else {
 396 |             errDiv.innerText = (resObj && resObj.message) || 'Failed to save lesson.';
 397 |             errDiv.style.display = 'block';
 398 |         }
 399 |     })
 400 |     .catch(function (err) {
 401 |         errDiv.innerText = (err && err.message) ? err.message : 'Network error saving lesson.';
 402 |         errDiv.style.display = 'block';
 403 |         console.error(err);
 404 |     })
 405 |     .finally(function () {
 406 |         if (saveBtn) { saveBtn.disabled = false; saveBtn.textContent = 'Save Lesson'; }
 407 |     });
 408 | }
```

---

### `deleteLesson` — lines 408–419

#### Signature

```javascript
function deleteLesson(schid)
```

#### What it is

Deletes or clears **delete Lesson** (data or temporary state).

#### How it works

1. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `schid` | `—` | SubChapter / lesson ID. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 408 | 
 409 | 
 410 | function deleteLesson(schid) {
 411 |     if (!confirm('Are you sure you want to delete this lesson?')) return;
 412 | 
 413 |     curriculumApi('delete_lesson', { schid: schid })
 414 |     .then(function (resObj) {
 415 |         if (resObj && resObj.success) loadCurriculumView();
 416 |         else alert('Delete failed: ' + ((resObj && resObj.message) || 'Unknown error'));
 417 |     })
 418 |     .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
 419 | }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | // Course Creation — sections & lessons
   2 | // depends on: cc-core.js, cc-media.js
   3 | function loadCurriculumView() {
   4 |     const view = document.getElementById('curriculumView');
   5 |     if (!view) return;
   6 | 
   7 |     if (!currentCourseId) {
   8 |         view.innerHTML = '<div class="text-center py-4 text-muted">Save basic info first (step 1) before adding sections.</div>';
   9 |         return;
  10 |     }
  11 | 
  12 |     view.innerHTML = '<div class="text-center py-4"><i class="fa-solid fa-circle-notch fa-spin me-2 text-muted"></i>Loading curriculum...</div>';
  13 | 
  14 |     curriculumApi('get', { cid: currentCourseId })
  15 |     .then(function (resObj) {
  16 |         if (!resObj || !resObj.success) {
  17 |             view.innerHTML = '<div class="text-danger py-4 text-center">Failed to load curriculum: ' +
  18 |             escapeHtml((resObj && resObj.message) || 'Unknown error') + '</div>';
  19 |             return;
  20 |         }
  21 | 
  22 |         const chapters = resObj.chapters || [];
  23 |         if (chapters.length === 0) {
  24 |             view.innerHTML = '<div class="text-center py-4 text-muted">No sections added yet. Click "+ Add New Section" to start building your course.</div>';
  25 |             return;
  26 |         }
  27 | 
  28 |         view.innerHTML = '';
  29 |         chapters.forEach(function (ch) {
  30 |             const secDiv = document.createElement('div');
  31 |             secDiv.className = 'section-item';
  32 |             secDiv.setAttribute('data-chid', ch.chid);
  33 | 
  34 |             let lessonsHtml = '';
  35 |             const lessons = ch.lessons || [];
  36 |             if (lessons.length > 0) {
  37 |                 lessons.forEach(function (les, idx) {
  38 |                     const type = (les.type || 'Text');
  39 |                     const typeClass = 'lesson-type-' + String(type).toLowerCase();
  40 |                     lessonsHtml +=
  41 |                     '<div class="lesson-item">' +
  42 |                     '<div class="lesson-meta d-flex align-items-center gap-2">' +
  43 |                     '<span class="text-muted small">' + (idx + 1) + '.</span>' +
  44 |                     '<span class="lesson-type-badge ' + typeClass + '">' + escapeHtml(type) + '</span>' +
  45 |                     '<span class="fw-semibold">' + escapeHtml(les.title || '') + '</span>' +
  46 |                     '</div>' +
  47 |                     '<div class="d-flex gap-2">' +
  48 |                     '<button type="button" class="btn btn-sm btn-link p-0 text-secondary" data-edit-lesson="' + les.schid + '" data-chid="' + ch.chid + '" title="Edit Lesson"><i class="fa-solid fa-pencil"></i></button>' +
  49 |                     '<button type="button" class="btn btn-sm btn-link p-0 text-danger" data-del-lesson="' + les.schid + '" title="Delete Lesson"><i class="fa-solid fa-trash"></i></button>' +
  50 |                     '</div></div>';
  51 |                 });
  52 |             } else {
  53 |                 lessonsHtml = '<div class="text-muted small py-2 px-1">No lessons added to this section.</div>';
  54 |             }
  55 | 
  56 |             secDiv.innerHTML =
  57 |             '<div class="section-header">' +
  58 |             '<span class="fw-bold">' + escapeHtml(ch.title || '') + '</span>' +
  59 |             '<div class="d-flex gap-2">' +
  60 |             '<button type="button" class="btn btn-sm btn-link p-0 text-secondary" data-edit-section="' + ch.chid + '" data-title="' + escapeHtml(ch.title || '') + '" title="Edit Section Title"><i class="fa-solid fa-pencil"></i></button>' +
  61 |             '<button type="button" class="btn btn-sm btn-link p-0 text-danger" data-del-section="' + ch.chid + '" title="Delete Section"><i class="fa-solid fa-trash"></i></button>' +
  62 |             '</div></div>' +
  63 |             '<div class="lesson-list">' + lessonsHtml +
  64 |             '<button type="button" class="btn btn-sm btn-light border w-100 text-muted py-2 mt-2" data-add-lesson="' + ch.chid + '" style="border-style: dashed !important;">' +
  65 |             '<i class="fa-solid fa-plus me-1"></i> Add New Lesson</button></div>';
  66 | 
  67 |             view.appendChild(secDiv);
  68 |         });
  69 | 
  70 |         // Bind section/lesson actions without inline onclick (avoids quote bugs)
  71 |         view.querySelectorAll('[data-edit-section]').forEach(function (btn) {
  72 |             btn.addEventListener('click', function () {
  73 |                 editSection(parseInt(btn.getAttribute('data-edit-section'), 10), btn.getAttribute('data-title') || '');
  74 |             });
  75 |         });
  76 |         view.querySelectorAll('[data-del-section]').forEach(function (btn) {
  77 |             btn.addEventListener('click', function () {
  78 |                 deleteSection(parseInt(btn.getAttribute('data-del-section'), 10));
  79 |             });
  80 |         });
  81 |         view.querySelectorAll('[data-add-lesson]').forEach(function (btn) {
  82 |             btn.addEventListener('click', function () {
  83 |                 showAddLessonModal(parseInt(btn.getAttribute('data-add-lesson'), 10));
  84 |             });
  85 |         });
  86 |         view.querySelectorAll('[data-edit-lesson]').forEach(function (btn) {
  87 |             btn.addEventListener('click', function () {
  88 |                 editLesson(parseInt(btn.getAttribute('data-edit-lesson'), 10), parseInt(btn.getAttribute('data-chid'), 10));
  89 |             });
  90 |         });
  91 |         view.querySelectorAll('[data-del-lesson]').forEach(function (btn) {
  92 |             btn.addEventListener('click', function () {
  93 |                 deleteLesson(parseInt(btn.getAttribute('data-del-lesson'), 10));
  94 |             });
  95 |         });
  96 |     })
  97 |     .catch(function (err) {
  98 |         console.error('Error loading curriculum: ', err);
  99 |         view.innerHTML = '<div class="text-danger py-4 text-center">Failed to load curriculum.</div>';
 100 |     });
 101 | }
 102 | 
 103 | function showAddSectionModal() {
 104 |     editingSectionId = null;
 105 |     document.getElementById('txtSectionTitle').value = '';
 106 |     document.getElementById('sectionModalTitle').innerText = 'Add New Section';
 107 |     document.getElementById('sectionModalError').style.display = 'none';
 108 |     showModal('sectionModal');
 109 | }
 110 | 
 111 | function editSection(chid, title) {
 112 |     editingSectionId = chid;
 113 |     document.getElementById('txtSectionTitle').value = title || '';
 114 |     document.getElementById('sectionModalTitle').innerText = 'Edit Section';
 115 |     document.getElementById('sectionModalError').style.display = 'none';
 116 |     showModal('sectionModal');
 117 | }
 118 | 
 119 | function saveSection() {
 120 |     const title = document.getElementById('txtSectionTitle').value.trim();
 121 |     const errDiv = document.getElementById('sectionModalError');
 122 |     errDiv.style.display = 'none';
 123 | 
 124 |     if (!title) {
 125 |         errDiv.innerText = 'Please enter a section title.';
 126 |         errDiv.style.display = 'block';
 127 |         return;
 128 |     }
 129 |     if (!currentCourseId) {
 130 |         errDiv.innerText = 'Course is not saved yet. Go back to step 1.';
 131 |         errDiv.style.display = 'block';
 132 |         return;
 133 |     }
 134 | 
 135 |     // Send 0 instead of null - ASP.NET WebMethods often reject null int?
 136 |     const chid = editingSectionId ? parseInt(editingSectionId, 10) : 0;
 137 | 
 138 |     const saveBtn = document.querySelector('#sectionModal .btn-pill-accent');
 139 |     if (saveBtn) { saveBtn.disabled = true; saveBtn.innerText = 'Saving...'; }
 140 | 
 141 |     curriculumApi('save_section', {
 142 |         chid: chid,
 143 |         cid: currentCourseId,
 144 |         title: title
 145 |     })
 146 |     .then(function (resObj) {
 147 |         if (resObj && resObj.success) {
 148 |             hideModal('sectionModal');
 149 |             setTimeout(function () { loadCurriculumView(); }, 150);
 150 |         } else {
 151 |             errDiv.innerText = (resObj && resObj.message) || 'Failed to save section.';
 152 |             errDiv.style.display = 'block';
 153 |         }
 154 |     })
 155 |     .catch(function (err) {
 156 |         errDiv.innerText = (err && err.message) || 'Network error saving section.';
 157 |         errDiv.style.display = 'block';
 158 |         console.error(err);
 159 |     })
 160 |     .finally(function () {
 161 |         if (saveBtn) { saveBtn.disabled = false; saveBtn.innerText = 'Save Section'; }
 162 |     });
 163 | }
 164 | 
 165 | function deleteSection(chid) {
 166 |     if (!confirm('Are you sure you want to delete this section? All lessons inside will be deleted too!')) return;
 167 | 
 168 |     curriculumApi('delete_section', { chid: chid })
 169 |     .then(function (resObj) {
 170 |         if (resObj && resObj.success) loadCurriculumView();
 171 |         else alert('Delete failed: ' + ((resObj && resObj.message) || 'Unknown error'));
 172 |     })
 173 |     .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
 174 | }
 175 | 
 176 | function showAddLessonModal(chid) {
 177 |     targetChapterId = chid;
 178 |     editingLessonId = null;
 179 |     document.getElementById('txtLessonTitle').value = '';
 180 |     document.getElementById('ddlLessonType').value = 'Text';
 181 |     document.getElementById('txtLessonContent').value = '';
 182 |     document.getElementById('lessonModalTitle').innerText = 'Add New Lesson';
 183 |     document.getElementById('lessonModalError').style.display = 'none';
 184 |     document.getElementById('lessonModalError').innerText = '';
 185 | 
 186 |     var htmlEditor = document.getElementById('htmlEditor');
 187 |     if (htmlEditor) htmlEditor.innerHTML = '';
 188 |     document.getElementById('lessonMaterials').value = '[]';
 189 |     var mediaPrev = document.getElementById('lessonMediaPreview');
 190 |     if (mediaPrev) { mediaPrev.innerHTML = ''; mediaPrev.classList.add('d-none'); }
 191 |     var mediaMsg = document.querySelector('#mediaDropzone .dz-inner');
 192 |     if (mediaMsg) mediaMsg.innerHTML = '<i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>Click or drag a video here (mp4 / webm / mov, up to 200MB)';
 193 |     var matMsg = document.querySelector('#materialDropzone .dz-inner');
 194 |     if (matMsg) matMsg.innerHTML = '<i class="fa-solid fa-file-arrow-up d-block mb-2 fs-4"></i>Click or drag materials (pdf, pptx, docx, images, up to 30MB)';
 195 |     if (typeof renderAttachmentsList === 'function') renderAttachmentsList();
 196 | 
 197 |     toggleLessonContentFields();
 198 |     showModal('lessonModal');
 199 | }
 200 | 
 201 | function editLesson(schid, chid) {
 202 |     targetChapterId = chid;
 203 |     editingLessonId = schid;
 204 |     document.getElementById('lessonModalTitle').innerText = 'Edit Lesson';
 205 |     document.getElementById('lessonModalError').style.display = 'none';
 206 | 
 207 |     curriculumApi('get_lesson', { schid: schid })
 208 |     .then(function (resObj) {
 209 |         if (resObj && resObj.success) {
 210 |             document.getElementById('txtLessonTitle').value = resObj.title || '';
 211 |             var lessonType = resObj.type || 'Text';
 212 |             // Map DB types that are not in the dropdown
 213 |             if (['PDF', 'Image', 'File'].indexOf(lessonType) >= 0) lessonType = 'Text';
 214 |             document.getElementById('ddlLessonType').value = lessonType;
 215 |             document.getElementById('txtLessonContent').value = resObj.content || '';
 216 |             var htmlEditor = document.getElementById('htmlEditor');
 217 |             if (htmlEditor && lessonType === 'Text') {
 218 |                 htmlEditor.innerHTML = resObj.content || '';
 219 |             }
 220 |             // Restore file materials so re-save does not wipe them
 221 |             var mats = resObj.materials || [];
 222 |             var cleaned = (mats || []).filter(function (m) {
 223 |                 return m && (m.url || m.mediaLink);
 224 |             }).map(function (m) {
 225 |                 return {
 226 |                     url: m.url || m.mediaLink,
 227 |                     fileName: m.fileName || m.textContent || 'file',
 228 |                     type: m.type || ''
 229 |                 };
 230 |             });
 231 |             document.getElementById('lessonMaterials').value = JSON.stringify(cleaned);
 232 |             var mediaPrev = document.getElementById('lessonMediaPreview');
 233 |             if (mediaPrev && lessonType === 'Video' && resObj.content) {
 234 |                 var vUrl = resolveMediaUrl(resObj.content, false);
 235 |                 mediaPrev.innerHTML = buildMaterialPreviewHtml(vUrl, 'video', 'Lesson video') +
 236 |                 '<div class="mt-1"><a class="small" href="' + escapeHtml(vUrl) + '" target="_blank">Open</a> · ' +
 237 |                 '<a class="small" href="' + escapeHtml(resolveMediaUrl(resObj.content, true)) + '">Download</a></div>';
 238 |                 mediaPrev.classList.remove('d-none');
 239 |             }
 240 |             toggleLessonContentFields();
 241 |             renderAttachmentsList();
 242 |             showModal('lessonModal');
 243 |         } else {
 244 |             alert('Failed to load lesson details: ' + ((resObj && resObj.message) || ''));
 245 |         }
 246 |     })
 247 |     .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
 248 | }
 249 | 
 250 | function toggleLessonContentFields() {
 251 |     const type = document.getElementById('ddlLessonType').value;
 252 |     const lbl = document.getElementById('lblLessonContent');
 253 |     const textarea = document.getElementById('txtLessonContent');
 254 | 
 255 |     const htmlEditor = document.getElementById('htmlEditor');
 256 |     const editorToolbar = document.getElementById('editorToolbar');
 257 |     const mediaDZ = document.getElementById('mediaDropzone');
 258 |     const materialDZ = document.getElementById('materialDropzone');
 259 |     const attachments = document.getElementById('lessonAttachments');
 260 | 
 261 |     // Hide all optional areas first
 262 |     if(htmlEditor) htmlEditor.style.display = 'none';
 263 |     if(editorToolbar) editorToolbar.style.display = 'none';
 264 |     if(textarea) textarea.classList.add('d-none');
 265 |     if(mediaDZ) mediaDZ.style.display = 'none';
 266 |     if(materialDZ) materialDZ.style.display = 'none';
 267 |     if(attachments) attachments.style.display = 'none';
 268 | 
 269 |     if (type === 'Video') {
 270 |         lbl.innerText = 'Video URL / Upload';
 271 |         if(mediaDZ) mediaDZ.style.display = 'block';
 272 |         if(textarea) textarea.classList.remove('d-none');
 273 |         textarea.placeholder = 'e.g., https://example.com/video.mp4 or upload below';
 274 |         // Extra file materials still allowed for Video lessons
 275 |         if(materialDZ) materialDZ.style.display = 'block';
 276 |         if(attachments) attachments.style.display = 'block';
 277 |     } else if (type === 'Quiz') {
 278 |         lbl.innerText = 'Quiz Question Description';
 279 |         if(textarea) textarea.classList.remove('d-none');
 280 |         textarea.placeholder = 'Provide the quiz questions or description for the student...';
 281 |         if(materialDZ) materialDZ.style.display = 'block';
 282 |         if(attachments) attachments.style.display = 'block';
 283 |     } else {
 284 |         lbl.innerText = 'Content Body';
 285 |         if(editorToolbar) editorToolbar.style.display = 'flex';
 286 |         if(htmlEditor) htmlEditor.style.display = 'block';
 287 |         if(materialDZ) materialDZ.style.display = 'block';
 288 |         if(attachments) attachments.style.display = 'block';
 289 |     }
 290 | }
 291 | 
 292 | function saveLesson() {
 293 |     var title = document.getElementById('txtLessonTitle').value.trim();
 294 |     var type = document.getElementById('ddlLessonType').value;
 295 |     var errDiv = document.getElementById('lessonModalError');
 296 |     errDiv.style.display = 'none';
 297 |     errDiv.innerText = '';
 298 | 
 299 |     if (!title) {
 300 |         errDiv.innerText = 'Please enter a lesson title.';
 301 |         errDiv.style.display = 'block';
 302 |         return;
 303 |     }
 304 |     if (!targetChapterId) {
 305 |         errDiv.innerText = 'No section selected. Close and open Add Lesson from a section.';
 306 |         errDiv.style.display = 'block';
 307 |         return;
 308 |     }
 309 | 
 310 |     var content = '';
 311 |     if (type === 'Video') {
 312 |         content = document.getElementById('txtLessonContent').value.trim();
 313 |     } else if (type === 'Quiz') {
 314 |         content = document.getElementById('txtLessonContent').value.trim();
 315 |     } else {
 316 |         var htmlEditor = document.getElementById('htmlEditor');
 317 |         content = htmlEditor ? htmlEditor.innerHTML.trim() : document.getElementById('txtLessonContent').value.trim();
 318 |         // treat empty editor shells as empty
 319 |         if (content === '<br>' || content === '<div><br></div>' || content === '<p><br></p>') content = '';
 320 |     }
 321 | 
 322 |     var materialsField = document.getElementById('lessonMaterials');
 323 |     var materialsRaw = materialsField ? (materialsField.value || '').trim() : '';
 324 |     var materialsArr = [];
 325 |     try { materialsArr = materialsRaw ? JSON.parse(materialsRaw) : []; } catch (e) { materialsArr = []; }
 326 |     if (!Array.isArray(materialsArr)) materialsArr = [];
 327 | 
 328 |     // Normalize each material to storePath + url for the server
 329 |     materialsArr = materialsArr.map(function (m) {
 330 |         var url = (m && (m.storePath || m.url || m.mediaLink)) || '';
 331 |         return {
 332 |             storePath: m.storePath || url,
 333 |             url: url,
 334 |             fileName: (m && m.fileName) || 'file',
 335 |             serveUrl: (m && m.serveUrl) || '',
 336 |             downloadUrl: (m && m.downloadUrl) || ''
 337 |         };
 338 |     }).filter(function (m) { return !!m.url; });
 339 | 
 340 |     // Allow save if we have content OR at least one uploaded material
 341 |     if (!content && materialsArr.length === 0 && type !== 'Quiz') {
 342 |         errDiv.innerText = type === 'Video'
 343 |         ? 'Upload a video or paste a video URL.'
 344 |         : 'Enter lesson content or upload at least one material file.';
 345 |         errDiv.style.display = 'block';
 346 |         return;
 347 |     }
 348 |     if (type === 'Quiz' && !content) {
 349 |         content = 'Quiz / assignment';
 350 |     }
 351 | 
 352 |     // Promote first uploaded file so preview always gets a real media path
 353 |     if (materialsArr.length > 0) {
 354 |         var firstUrl = materialsArr[0].storePath || materialsArr[0].url || '';
 355 |         var firstName = materialsArr[0].fileName || firstUrl;
 356 |         var kind = mediaKind(firstName + ' ' + firstUrl);
 357 |         if (type === 'Text' || type === 'Video') {
 358 |             // Video lesson: ensure content is the video path
 359 |             if (type === 'Video' && firstUrl && !content) content = firstUrl;
 360 |             // Text lesson with only a short placeholder body → use file as primary media
 361 |             var plain = (content || '').replace(/<[^>]+>/g, '').trim();
 362 |             if (type === 'Text' && firstUrl && (plain.length < 40 || plain === title)) {
 363 |                 if (kind === 'video') type = 'Video';
 364 |                 else if (kind === 'pdf') type = 'PDF';
 365 |                 else if (kind === 'image') type = 'Image';
 366 |                 else type = 'PDF';
 367 |                 content = firstUrl;
 368 |             }
 369 |         }
 370 |     }
 371 | 
 372 |     var schid = editingLessonId ? parseInt(editingLessonId, 10) : 0;
 373 |     var saveBtn = document.querySelector('#lessonModal .btn-pill-accent');
 374 |     if (saveBtn) { saveBtn.disabled = true; saveBtn.textContent = 'Saving...'; }
 375 | 
 376 |     var matsJson = materialsArr.length ? JSON.stringify(materialsArr) : '[]';
 377 | 
 378 |     curriculumApi('save_lesson', {
 379 |         schid: schid,
 380 |         chid: parseInt(targetChapterId, 10),
 381 |         title: title,
 382 |         type: type,
 383 |         content: content,
 384 |         materialsJson: matsJson
 385 |     })
 386 |     .then(function (resObj) {
 387 |         if (resObj && resObj.success) {
 388 |             if (resObj.warning) console.warn('Lesson warning:', resObj.warning);
 389 |             if (materialsArr.length && resObj.materialsSaved === 0) {
 390 |                 alert('Lesson saved, but materials may not have been stored (materialsSaved=0). Check StudyMats.MediaLink. Warning: ' +
 391 |                 (resObj.warning || 'none'));
 392 |             }
 393 |             hideModal('lessonModal');
 394 |             setTimeout(function () { loadCurriculumView(); }, 200);
 395 |         } else {
 396 |             errDiv.innerText = (resObj && resObj.message) || 'Failed to save lesson.';
 397 |             errDiv.style.display = 'block';
 398 |         }
 399 |     })
 400 |     .catch(function (err) {
 401 |         errDiv.innerText = (err && err.message) ? err.message : 'Network error saving lesson.';
 402 |         errDiv.style.display = 'block';
 403 |         console.error(err);
 404 |     })
 405 |     .finally(function () {
 406 |         if (saveBtn) { saveBtn.disabled = false; saveBtn.textContent = 'Save Lesson'; }
 407 |     });
 408 | }
 409 | 
 410 | function deleteLesson(schid) {
 411 |     if (!confirm('Are you sure you want to delete this lesson?')) return;
 412 | 
 413 |     curriculumApi('delete_lesson', { schid: schid })
 414 |     .then(function (resObj) {
 415 |         if (resObj && resObj.success) loadCurriculumView();
 416 |         else alert('Delete failed: ' + ((resObj && resObj.message) || 'Unknown error'));
 417 |     })
 418 |     .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
 419 | }
 420 | 
```
