# cc-curriculum.js
**Source:** `Pages/Lecturer/Scripts/cc-curriculum.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 420
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 4:** `view` — script-level `const`/`let`/`var` — **Holds “view” for this scope.**
- **Line 21:** `chapters` — script-level `const`/`let`/`var` — **Often a collection related to chapters (plural name).**
- **Line 30:** `secDiv` — script-level `const`/`let`/`var` — **Holds “sec Div” for this scope.**
- **Line 33:** `lessonsHtml` — script-level `const`/`let`/`var` — **Holds “lessons Html” for this scope.**
- **Line 35:** `lessons` — script-level `const`/`let`/`var` — **Often a collection related to lessons (plural name).**
- **Line 38:** `type` — script-level `const`/`let`/`var` — **Holds “type” for this scope.**
- **Line 39:** `typeClass` — script-level `const`/`let`/`var` — **Often a collection related to type Class (plural name).**
- **Line 120:** `title` — script-level `const`/`let`/`var` — **Title of course work / page heading.**
- **Line 121:** `errDiv` — script-level `const`/`let`/`var` — **Holds “err Div” for this scope.**
- **Line 136:** `chid` — script-level `const`/`let`/`var` — **Chapter ID (Chapters.ChID).**
- **Line 137:** `saveBtn` — script-level `const`/`let`/`var` — **Holds “save Btn” for this scope.**
- **Line 185:** `htmlEditor` — script-level `const`/`let`/`var` — **Holds “html Editor” for this scope.**
- **Line 189:** `mediaPrev` — script-level `const`/`let`/`var` — **Holds “media Prev” for this scope.**
- **Line 191:** `mediaMsg` — script-level `const`/`let`/`var` — **Holds “media Msg” for this scope.**
- **Line 193:** `matMsg` — script-level `const`/`let`/`var` — **Holds “mat Msg” for this scope.**
- **Line 211:** `lessonType` — script-level `const`/`let`/`var` — **Holds “lesson Type” for this scope.**
- **Line 221:** `mats` — script-level `const`/`let`/`var` — **Often a collection related to mats (plural name).**
- **Line 222:** `cleaned` — script-level `const`/`let`/`var` — **Holds “cleaned” for this scope.**
- **Line 234:** `vUrl` — script-level `const`/`let`/`var` — **URL string.**
- **Line 252:** `lbl` — script-level `const`/`let`/`var` — **UI control reference (lbl).**
- **Line 253:** `textarea` — script-level `const`/`let`/`var` — **Holds “textarea” for this scope.**
- **Line 256:** `editorToolbar` — script-level `const`/`let`/`var` — **Holds “editor Toolbar” for this scope.**
- **Line 257:** `mediaDZ` — script-level `const`/`let`/`var` — **Holds “media DZ” for this scope.**
- **Line 258:** `materialDZ` — script-level `const`/`let`/`var` — **Holds “material DZ” for this scope.**
- **Line 259:** `attachments` — script-level `const`/`let`/`var` — **Often a collection related to attachments (plural name).**
- **Line 309:** `content` — script-level `const`/`let`/`var` — **Submission body text or JSON payload in CWSubmissions.**
- **Line 321:** `materialsField` — script-level `const`/`let`/`var` — **Holds “materials Field” for this scope.**
- **Line 323:** `materialsRaw` — script-level `const`/`let`/`var` — **Holds “materials Raw” for this scope.**
- **Line 324:** `materialsArr` — script-level `const`/`let`/`var` — **Holds “materials Arr” for this scope.**
- **Line 330:** `url` — script-level `const`/`let`/`var` — **HTTP URL to media or page.**
- **Line 354:** `firstUrl` — script-level `const`/`let`/`var` — **URL string.**
- **Line 355:** `firstName` — script-level `const`/`let`/`var` — **Holds “first Name” for this scope.**
- **Line 356:** `kind` — script-level `const`/`let`/`var` — **Upload kind (material/video/thumbnail/submission).**
- **Line 361:** `plain` — script-level `const`/`let`/`var` — **Text without META trailer (student-visible instructions).**
- **Line 371:** `schid` — script-level `const`/`let`/`var` — **SubChapter / lesson ID.**
- **Line 375:** `matsJson` — script-level `const`/`let`/`var` — **Holds “mats Json” for this scope.**

## Functions / methods (10 found)

### `loadCurriculumView` — lines 2–101

```javascript
function loadCurriculumView()
```

#### Explanation

- **Purpose:** Implements `loadCurriculumView`.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `view` — Holds “view” for this scope.  DOM element from the page.
- `chapters` — Often a collection related to chapters (plural name).
- `secDiv` — Holds “sec Div” for this scope.
- `lessonsHtml` — Holds “lessons Html” for this scope.  Literal text string.
- `lessons` — Often a collection related to lessons (plural name).
- `type` — Holds “type” for this scope.
- `typeClass` — Often a collection related to type Class (plural name).  Literal text string.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L4:** Get HTML element by id. | `view` means: Holds “view” for this scope.  DOM element from the page.
- **L8:** Update page HTML.
- **L12:** Update page HTML.
- **L17:** Update page HTML.
- **L18:** Encode text to reduce XSS risk.
- **L22:** `chapters` means: Often a collection related to chapters (plural name).
- **L24:** Update page HTML.
- **L28:** Update page HTML.
- **L30:** `secDiv` means: Holds “sec Div” for this scope.
- **L34:** `lessonsHtml` means: Holds “lessons Html” for this scope.  Literal text string.
- **L35:** `lessons` means: Often a collection related to lessons (plural name).
- **L38:** `type` means: Holds “type” for this scope.
- **L39:** `typeClass` means: Often a collection related to type Class (plural name).  Literal text string.
- **L44:** Encode text to reduce XSS risk.
- **L45:** Encode text to reduce XSS risk.
- **L56:** Update page HTML.
- **L58:** Encode text to reduce XSS risk.
- **L60:** Encode text to reduce XSS risk.
- **L72:** DOM event handler.
- **L77:** DOM event handler.
- **L82:** DOM event handler.
- **L87:** DOM event handler.
- **L92:** DOM event handler.
- **L99:** Update page HTML.

---

### `showAddSectionModal` — lines 101–109

```javascript
function showAddSectionModal()
```

#### Explanation

- **Purpose:** Implements `showAddSectionModal`.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L105:** Get HTML element by id.
- **L106:** Get HTML element by id.
- **L107:** Get HTML element by id.

---

### `editSection` — lines 109–117

```javascript
function editSection(chid, title)
```

#### Explanation

- **Purpose:** Implements `editSection`.
- **Parameters (what each means):**
- `chid` — Chapter ID (Chapters.ChID).
- `title` — Title of course work / page heading.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L113:** Get HTML element by id.
- **L114:** Get HTML element by id.
- **L115:** Get HTML element by id.

---

### `saveSection` — lines 117–163

```javascript
function saveSection()
```

#### Explanation

- **Purpose:** Implements `saveSection`.
- **ASP.NET WebMethod:** Called from browser JS via `Page.aspx/MethodName` POST JSON.
- **Pattern:** Persist changes.
- **Local variables (what each means):**
- `title` — Title of course work / page heading.  DOM element from the page.
- `errDiv` — Holds “err Div” for this scope.  DOM element from the page.
- `chid` — Chapter ID (Chapters.ChID).
- `saveBtn` — Holds “save Btn” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L120:** Get HTML element by id. | `title` means: Title of course work / page heading.  DOM element from the page.
- **L121:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L136:** `chid` means: Chapter ID (Chapters.ChID).
- **L138:** `saveBtn` means: Holds “save Btn” for this scope.

---

### `deleteSection` — lines 163–174

```javascript
function deleteSection(chid)
```

#### Explanation

- **Purpose:** Implements `deleteSection`.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `chid` — Chapter ID (Chapters.ChID).

#### Line-by-line (this function)

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

```javascript
function showAddLessonModal(chid)
```

#### Explanation

- **Purpose:** Implements `showAddLessonModal`.
- **Parameters (what each means):**
- `chid` — Chapter ID (Chapters.ChID).
- **Local variables (what each means):**
- `htmlEditor` — Holds “html Editor” for this scope.  DOM element from the page.
- `mediaPrev` — Holds “media Prev” for this scope.  DOM element from the page.
- `mediaMsg` — Holds “media Msg” for this scope.
- `matMsg` — Holds “mat Msg” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L179:** Get HTML element by id.
- **L180:** Get HTML element by id.
- **L181:** Get HTML element by id.
- **L182:** Get HTML element by id.
- **L183:** Get HTML element by id.
- **L184:** Get HTML element by id.
- **L186:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L187:** Update page HTML.
- **L188:** Get HTML element by id.
- **L189:** Get HTML element by id. | `mediaPrev` means: Holds “media Prev” for this scope.  DOM element from the page.
- **L190:** Update page HTML.
- **L191:** `mediaMsg` means: Holds “media Msg” for this scope.
- **L192:** Update page HTML.
- **L193:** `matMsg` means: Holds “mat Msg” for this scope.
- **L194:** Update page HTML.

---

### `editLesson` — lines 199–248

```javascript
function editLesson(schid, chid)
```

#### Explanation

- **Purpose:** Implements `editLesson`.
- **Parameters (what each means):**
- `schid` — SubChapter / lesson ID.
- `chid` — Chapter ID (Chapters.ChID).
- **Local variables (what each means):**
- `lessonType` — Holds “lesson Type” for this scope.
- `htmlEditor` — Holds “html Editor” for this scope.  DOM element from the page.
- `mats` — Often a collection related to mats (plural name).
- `cleaned` — Holds “cleaned” for this scope.
- `mediaPrev` — Holds “media Prev” for this scope.  DOM element from the page.
- `vUrl` — URL string.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L204:** Get HTML element by id.
- **L205:** Get HTML element by id.
- **L210:** Get HTML element by id.
- **L211:** `lessonType` means: Holds “lesson Type” for this scope.
- **L214:** Get HTML element by id.
- **L215:** Get HTML element by id.
- **L216:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L218:** Update page HTML.
- **L221:** `mats` means: Often a collection related to mats (plural name).
- **L222:** `cleaned` means: Holds “cleaned” for this scope.
- **L231:** Get HTML element by id.
- **L232:** Get HTML element by id. | `mediaPrev` means: Holds “media Prev” for this scope.  DOM element from the page.
- **L234:** `vUrl` means: URL string.
- **L235:** Update page HTML.
- **L236:** Encode text to reduce XSS risk.
- **L237:** Encode text to reduce XSS risk.

---

### `toggleLessonContentFields` — lines 248–290

```javascript
function toggleLessonContentFields()
```

#### Explanation

- **Purpose:** Implements `toggleLessonContentFields`.
- **Local variables (what each means):**
- `type` — Holds “type” for this scope.  DOM element from the page.
- `lbl` — UI control reference (lbl).  DOM element from the page.
- `textarea` — Holds “textarea” for this scope.  DOM element from the page.
- `htmlEditor` — Holds “html Editor” for this scope.  DOM element from the page.
- `editorToolbar` — Holds “editor Toolbar” for this scope.  DOM element from the page.
- `mediaDZ` — Holds “media DZ” for this scope.  DOM element from the page.
- `materialDZ` — Holds “material DZ” for this scope.  DOM element from the page.
- `attachments` — Often a collection related to attachments (plural name).  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L251:** Get HTML element by id. | `type` means: Holds “type” for this scope.  DOM element from the page.
- **L252:** Get HTML element by id. | `lbl` means: UI control reference (lbl).  DOM element from the page.
- **L253:** Get HTML element by id. | `textarea` means: Holds “textarea” for this scope.  DOM element from the page.
- **L255:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L256:** Get HTML element by id. | `editorToolbar` means: Holds “editor Toolbar” for this scope.  DOM element from the page.
- **L257:** Get HTML element by id. | `mediaDZ` means: Holds “media DZ” for this scope.  DOM element from the page.
- **L258:** Get HTML element by id. | `materialDZ` means: Holds “material DZ” for this scope.  DOM element from the page.
- **L259:** Get HTML element by id. | `attachments` means: Often a collection related to attachments (plural name).  DOM element from the page.

---

### `saveLesson` — lines 290–408

```javascript
function saveLesson()
```

#### Explanation

- **Purpose:** Implements `saveLesson`.
- **Pattern:** Persist changes.
- **Local variables (what each means):**
- `title` — Title of course work / page heading.  DOM element from the page.
- `type` — Holds “type” for this scope.  DOM element from the page.
- `errDiv` — Holds “err Div” for this scope.  DOM element from the page.
- `content` — Submission body text or JSON payload in CWSubmissions.  Literal text string.
- `htmlEditor` — Holds “html Editor” for this scope.  DOM element from the page.
- `materialsField` — Holds “materials Field” for this scope.  DOM element from the page.
- `materialsRaw` — Holds “materials Raw” for this scope.
- `materialsArr` — Holds “materials Arr” for this scope.
- `url` — HTTP URL to media or page.
- `firstUrl` — URL string.
- `firstName` — Holds “first Name” for this scope.
- `kind` — Upload kind (material/video/thumbnail/submission).
- `plain` — Text without META trailer (student-visible instructions).
- `schid` — SubChapter / lesson ID.
- `saveBtn` — Holds “save Btn” for this scope.
- `matsJson` — Holds “mats Json” for this scope.  JSON serialize/parse result.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L293:** Get HTML element by id. | `title` means: Title of course work / page heading.  DOM element from the page.
- **L294:** Get HTML element by id. | `type` means: Holds “type” for this scope.  DOM element from the page.
- **L295:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L310:** `content` means: Submission body text or JSON payload in CWSubmissions.  Literal text string.
- **L312:** Get HTML element by id.
- **L314:** Get HTML element by id.
- **L316:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L317:** Get HTML element by id.
- **L322:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L323:** `materialsRaw` means: Holds “materials Raw” for this scope.
- **L324:** `materialsArr` means: Holds “materials Arr” for this scope.
- **L325:** JS object ↔ JSON text.
- **L330:** `url` means: HTTP URL to media or page.
- **L354:** `firstUrl` means: URL string.
- **L355:** `firstName` means: Holds “first Name” for this scope.
- **L356:** `kind` means: Upload kind (material/video/thumbnail/submission).
- **L361:** `plain` means: Text without META trailer (student-visible instructions).
- **L372:** `schid` means: SubChapter / lesson ID.
- **L373:** `saveBtn` means: Holds “save Btn” for this scope.
- **L376:** JS object ↔ JSON text. | `matsJson` means: Holds “mats Json” for this scope.  JSON serialize/parse result.

---

### `deleteLesson` — lines 408–419

```javascript
function deleteLesson(schid)
```

#### Explanation

- **Purpose:** Implements `deleteLesson`.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `schid` — SubChapter / lesson ID.

#### Line-by-line (this function)

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

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L4:** Get HTML element by id. | `view` means: Holds “view” for this scope.  DOM element from the page.
- **L8:** Update page HTML.
- **L12:** Update page HTML.
- **L17:** Update page HTML.
- **L18:** Encode text to reduce XSS risk.
- **L22:** `chapters` means: Often a collection related to chapters (plural name).
- **L24:** Update page HTML.
- **L28:** Update page HTML.
- **L30:** `secDiv` means: Holds “sec Div” for this scope.
- **L34:** `lessonsHtml` means: Holds “lessons Html” for this scope.  Literal text string.
- **L35:** `lessons` means: Often a collection related to lessons (plural name).
- **L38:** `type` means: Holds “type” for this scope.
- **L39:** `typeClass` means: Often a collection related to type Class (plural name).  Literal text string.
- **L44:** Encode text to reduce XSS risk.
- **L45:** Encode text to reduce XSS risk.
- **L56:** Update page HTML.
- **L58:** Encode text to reduce XSS risk.
- **L60:** Encode text to reduce XSS risk.
- **L72:** DOM event handler.
- **L77:** DOM event handler.
- **L82:** DOM event handler.
- **L87:** DOM event handler.
- **L92:** DOM event handler.
- **L99:** Update page HTML.
- **L105:** Get HTML element by id.
- **L106:** Get HTML element by id.
- **L107:** Get HTML element by id.
- **L113:** Get HTML element by id.
- **L114:** Get HTML element by id.
- **L115:** Get HTML element by id.
- **L120:** Get HTML element by id. | `title` means: Title of course work / page heading.  DOM element from the page.
- **L121:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L136:** `chid` means: Chapter ID (Chapters.ChID).
- **L138:** `saveBtn` means: Holds “save Btn” for this scope.
- **L179:** Get HTML element by id.
- **L180:** Get HTML element by id.
- **L181:** Get HTML element by id.
- **L182:** Get HTML element by id.
- **L183:** Get HTML element by id.
- **L184:** Get HTML element by id.
- **L186:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L187:** Update page HTML.
- **L188:** Get HTML element by id.
- **L189:** Get HTML element by id. | `mediaPrev` means: Holds “media Prev” for this scope.  DOM element from the page.
- **L190:** Update page HTML.
- **L191:** `mediaMsg` means: Holds “media Msg” for this scope.
- **L192:** Update page HTML.
- **L193:** `matMsg` means: Holds “mat Msg” for this scope.
- **L194:** Update page HTML.
- **L204:** Get HTML element by id.
- **L205:** Get HTML element by id.
- **L210:** Get HTML element by id.
- **L211:** `lessonType` means: Holds “lesson Type” for this scope.
- **L214:** Get HTML element by id.
- **L215:** Get HTML element by id.
- **L216:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L218:** Update page HTML.
- **L221:** `mats` means: Often a collection related to mats (plural name).
- **L222:** `cleaned` means: Holds “cleaned” for this scope.
- **L231:** Get HTML element by id.
- **L232:** Get HTML element by id. | `mediaPrev` means: Holds “media Prev” for this scope.  DOM element from the page.
- **L234:** `vUrl` means: URL string.
- **L235:** Update page HTML.
- **L236:** Encode text to reduce XSS risk.
- **L237:** Encode text to reduce XSS risk.
- **L251:** Get HTML element by id. | `type` means: Holds “type” for this scope.  DOM element from the page.
- **L252:** Get HTML element by id. | `lbl` means: UI control reference (lbl).  DOM element from the page.
- **L253:** Get HTML element by id. | `textarea` means: Holds “textarea” for this scope.  DOM element from the page.
- **L255:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L256:** Get HTML element by id. | `editorToolbar` means: Holds “editor Toolbar” for this scope.  DOM element from the page.
- **L257:** Get HTML element by id. | `mediaDZ` means: Holds “media DZ” for this scope.  DOM element from the page.
- **L258:** Get HTML element by id. | `materialDZ` means: Holds “material DZ” for this scope.  DOM element from the page.
- **L259:** Get HTML element by id. | `attachments` means: Often a collection related to attachments (plural name).  DOM element from the page.
- **L293:** Get HTML element by id. | `title` means: Title of course work / page heading.  DOM element from the page.
- **L294:** Get HTML element by id. | `type` means: Holds “type” for this scope.  DOM element from the page.
- **L295:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L310:** `content` means: Submission body text or JSON payload in CWSubmissions.  Literal text string.
- **L312:** Get HTML element by id.
- **L314:** Get HTML element by id.
- **L316:** Get HTML element by id. | `htmlEditor` means: Holds “html Editor” for this scope.  DOM element from the page.
- **L317:** Get HTML element by id.
- **L322:** Get HTML element by id. | `materialsField` means: Holds “materials Field” for this scope.  DOM element from the page.
- **L323:** `materialsRaw` means: Holds “materials Raw” for this scope.
- **L324:** `materialsArr` means: Holds “materials Arr” for this scope.
- **L325:** JS object ↔ JSON text.
- **L330:** `url` means: HTTP URL to media or page.
- **L354:** `firstUrl` means: URL string.
- **L355:** `firstName` means: Holds “first Name” for this scope.
- **L356:** `kind` means: Upload kind (material/video/thumbnail/submission).
- **L361:** `plain` means: Text without META trailer (student-visible instructions).
- **L372:** `schid` means: SubChapter / lesson ID.
- **L373:** `saveBtn` means: Holds “save Btn” for this scope.
- **L376:** JS object ↔ JSON text. | `matsJson` means: Holds “mats Json” for this scope.  JSON serialize/parse result.

## Source snapshot (raw)

```javascript
// Course Creation — sections & lessons
// depends on: cc-core.js, cc-media.js
function loadCurriculumView() {
    const view = document.getElementById('curriculumView');
    if (!view) return;

    if (!currentCourseId) {
        view.innerHTML = '<div class="text-center py-4 text-muted">Save basic info first (step 1) before adding sections.</div>';
        return;
    }

    view.innerHTML = '<div class="text-center py-4"><i class="fa-solid fa-circle-notch fa-spin me-2 text-muted"></i>Loading curriculum...</div>';

    curriculumApi('get', { cid: currentCourseId })
    .then(function (resObj) {
        if (!resObj || !resObj.success) {
            view.innerHTML = '<div class="text-danger py-4 text-center">Failed to load curriculum: ' +
            escapeHtml((resObj && resObj.message) || 'Unknown error') + '</div>';
            return;
        }

        const chapters = resObj.chapters || [];
        if (chapters.length === 0) {
            view.innerHTML = '<div class="text-center py-4 text-muted">No sections added yet. Click "+ Add New Section" to start building your course.</div>';
            return;
        }

        view.innerHTML = '';
        chapters.forEach(function (ch) {
            const secDiv = document.createElement('div');
            secDiv.className = 'section-item';
            secDiv.setAttribute('data-chid', ch.chid);

            let lessonsHtml = '';
            const lessons = ch.lessons || [];
            if (lessons.length > 0) {
                lessons.forEach(function (les, idx) {
                    const type = (les.type || 'Text');
                    const typeClass = 'lesson-type-' + String(type).toLowerCase();
                    lessonsHtml +=
                    '<div class="lesson-item">' +
                    '<div class="lesson-meta d-flex align-items-center gap-2">' +
                    '<span class="text-muted small">' + (idx + 1) + '.</span>' +
                    '<span class="lesson-type-badge ' + typeClass + '">' + escapeHtml(type) + '</span>' +
                    '<span class="fw-semibold">' + escapeHtml(les.title || '') + '</span>' +
                    '</div>' +
                    '<div class="d-flex gap-2">' +
                    '<button type="button" class="btn btn-sm btn-link p-0 text-secondary" data-edit-lesson="' + les.schid + '" data-chid="' + ch.chid + '" title="Edit Lesson"><i class="fa-solid fa-pencil"></i></button>' +
                    '<button type="button" class="btn btn-sm btn-link p-0 text-danger" data-del-lesson="' + les.schid + '" title="Delete Lesson"><i class="fa-solid fa-trash"></i></button>' +
                    '</div></div>';
                });
            } else {
                lessonsHtml = '<div class="text-muted small py-2 px-1">No lessons added to this section.</div>';
            }

            secDiv.innerHTML =
            '<div class="section-header">' +
            '<span class="fw-bold">' + escapeHtml(ch.title || '') + '</span>' +
            '<div class="d-flex gap-2">' +
            '<button type="button" class="btn btn-sm btn-link p-0 text-secondary" data-edit-section="' + ch.chid + '" data-title="' + escapeHtml(ch.title || '') + '" title="Edit Section Title"><i class="fa-solid fa-pencil"></i></button>' +
            '<button type="button" class="btn btn-sm btn-link p-0 text-danger" data-del-section="' + ch.chid + '" title="Delete Section"><i class="fa-solid fa-trash"></i></button>' +
            '</div></div>' +
            '<div class="lesson-list">' + lessonsHtml +
            '<button type="button" class="btn btn-sm btn-light border w-100 text-muted py-2 mt-2" data-add-lesson="' + ch.chid + '" style="border-style: dashed !important;">' +
            '<i class="fa-solid fa-plus me-1"></i> Add New Lesson</button></div>';

            view.appendChild(secDiv);
        });

        // Bind section/lesson actions without inline onclick (avoids quote bugs)
        view.querySelectorAll('[data-edit-section]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                editSection(parseInt(btn.getAttribute('data-edit-section'), 10), btn.getAttribute('data-title') || '');
            });
        });
        view.querySelectorAll('[data-del-section]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                deleteSection(parseInt(btn.getAttribute('data-del-section'), 10));
            });
        });
        view.querySelectorAll('[data-add-lesson]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                showAddLessonModal(parseInt(btn.getAttribute('data-add-lesson'), 10));
            });
        });
        view.querySelectorAll('[data-edit-lesson]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                editLesson(parseInt(btn.getAttribute('data-edit-lesson'), 10), parseInt(btn.getAttribute('data-chid'), 10));
            });
        });
        view.querySelectorAll('[data-del-lesson]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                deleteLesson(parseInt(btn.getAttribute('data-del-lesson'), 10));
            });
        });
    })
    .catch(function (err) {
        console.error('Error loading curriculum: ', err);
        view.innerHTML = '<div class="text-danger py-4 text-center">Failed to load curriculum.</div>';
    });
}

function showAddSectionModal() {
    editingSectionId = null;
    document.getElementById('txtSectionTitle').value = '';
    document.getElementById('sectionModalTitle').innerText = 'Add New Section';
    document.getElementById('sectionModalError').style.display = 'none';
    showModal('sectionModal');
}

function editSection(chid, title) {
    editingSectionId = chid;
    document.getElementById('txtSectionTitle').value = title || '';
    document.getElementById('sectionModalTitle').innerText = 'Edit Section';
    document.getElementById('sectionModalError').style.display = 'none';
    showModal('sectionModal');
}

function saveSection() {
    const title = document.getElementById('txtSectionTitle').value.trim();
    const errDiv = document.getElementById('sectionModalError');
    errDiv.style.display = 'none';

    if (!title) {
        errDiv.innerText = 'Please enter a section title.';
        errDiv.style.display = 'block';
        return;
    }
    if (!currentCourseId) {
        errDiv.innerText = 'Course is not saved yet. Go back to step 1.';
        errDiv.style.display = 'block';
        return;
    }

    // Send 0 instead of null - ASP.NET WebMethods often reject null int?
    const chid = editingSectionId ? parseInt(editingSectionId, 10) : 0;

    const saveBtn = document.querySelector('#sectionModal .btn-pill-accent');
    if (saveBtn) { saveBtn.disabled = true; saveBtn.innerText = 'Saving...'; }

    curriculumApi('save_section', {
        chid: chid,
        cid: currentCourseId,
        title: title
    })
    .then(function (resObj) {
        if (resObj && resObj.success) {
            hideModal('sectionModal');
            setTimeout(function () { loadCurriculumView(); }, 150);
        } else {
            errDiv.innerText = (resObj && resObj.message) || 'Failed to save section.';
            errDiv.style.display = 'block';
        }
    })
    .catch(function (err) {
        errDiv.innerText = (err && err.message) || 'Network error saving section.';
        errDiv.style.display = 'block';
        console.error(err);
    })
    .finally(function () {
        if (saveBtn) { saveBtn.disabled = false; saveBtn.innerText = 'Save Section'; }
    });
}

function deleteSection(chid) {
    if (!confirm('Are you sure you want to delete this section? All lessons inside will be deleted too!')) return;

    curriculumApi('delete_section', { chid: chid })
    .then(function (resObj) {
        if (resObj && resObj.success) loadCurriculumView();
        else alert('Delete failed: ' + ((resObj && resObj.message) || 'Unknown error'));
    })
    .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
}

function showAddLessonModal(chid) {
    targetChapterId = chid;
    editingLessonId = null;
    document.getElementById('txtLessonTitle').value = '';
    document.getElementById('ddlLessonType').value = 'Text';
    document.getElementById('txtLessonContent').value = '';
    document.getElementById('lessonModalTitle').innerText = 'Add New Lesson';
    document.getElementById('lessonModalError').style.display = 'none';
    document.getElementById('lessonModalError').innerText = '';

    var htmlEditor = document.getElementById('htmlEditor');
    if (htmlEditor) htmlEditor.innerHTML = '';
    document.getElementById('lessonMaterials').value = '[]';
    var mediaPrev = document.getElementById('lessonMediaPreview');
    if (mediaPrev) { mediaPrev.innerHTML = ''; mediaPrev.classList.add('d-none'); }
    var mediaMsg = document.querySelector('#mediaDropzone .dz-inner');
    if (mediaMsg) mediaMsg.innerHTML = '<i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>Click or drag a video here (mp4 / webm / mov, up to 200MB)';
    var matMsg = document.querySelector('#materialDropzone .dz-inner');
    if (matMsg) matMsg.innerHTML = '<i class="fa-solid fa-file-arrow-up d-block mb-2 fs-4"></i>Click or drag materials (pdf, pptx, docx, images, up to 30MB)';
    if (typeof renderAttachmentsList === 'function') renderAttachmentsList();

    toggleLessonContentFields();
    showModal('lessonModal');
}

function editLesson(schid, chid) {
    targetChapterId = chid;
    editingLessonId = schid;
    document.getElementById('lessonModalTitle').innerText = 'Edit Lesson';
    document.getElementById('lessonModalError').style.display = 'none';

    curriculumApi('get_lesson', { schid: schid })
    .then(function (resObj) {
        if (resObj && resObj.success) {
            document.getElementById('txtLessonTitle').value = resObj.title || '';
            var lessonType = resObj.type || 'Text';
            // Map DB types that are not in the dropdown
            if (['PDF', 'Image', 'File'].indexOf(lessonType) >= 0) lessonType = 'Text';
            document.getElementById('ddlLessonType').value = lessonType;
            document.getElementById('txtLessonContent').value = resObj.content || '';
            var htmlEditor = document.getElementById('htmlEditor');
            if (htmlEditor && lessonType === 'Text') {
                htmlEditor.innerHTML = resObj.content || '';
            }
            // Restore file materials so re-save does not wipe them
            var mats = resObj.materials || [];
            var cleaned = (mats || []).filter(function (m) {
                return m && (m.url || m.mediaLink);
            }).map(function (m) {
                return {
                    url: m.url || m.mediaLink,
                    fileName: m.fileName || m.textContent || 'file',
                    type: m.type || ''
                };
            });
            document.getElementById('lessonMaterials').value = JSON.stringify(cleaned);
            var mediaPrev = document.getElementById('lessonMediaPreview');
            if (mediaPrev && lessonType === 'Video' && resObj.content) {
                var vUrl = resolveMediaUrl(resObj.content, false);
                mediaPrev.innerHTML = buildMaterialPreviewHtml(vUrl, 'video', 'Lesson video') +
                '<div class="mt-1"><a class="small" href="' + escapeHtml(vUrl) + '" target="_blank">Open</a> · ' +
                '<a class="small" href="' + escapeHtml(resolveMediaUrl(resObj.content, true)) + '">Download</a></div>';
                mediaPrev.classList.remove('d-none');
            }
            toggleLessonContentFields();
            renderAttachmentsList();
            showModal('lessonModal');
        } else {
            alert('Failed to load lesson details: ' + ((resObj && resObj.message) || ''));
        }
    })
    .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
}

function toggleLessonContentFields() {
    const type = document.getElementById('ddlLessonType').value;
    const lbl = document.getElementById('lblLessonContent');
    const textarea = document.getElementById('txtLessonContent');

    const htmlEditor = document.getElementById('htmlEditor');
    const editorToolbar = document.getElementById('editorToolbar');
    const mediaDZ = document.getElementById('mediaDropzone');
    const materialDZ = document.getElementById('materialDropzone');
    const attachments = document.getElementById('lessonAttachments');

    // Hide all optional areas first
    if(htmlEditor) htmlEditor.style.display = 'none';
    if(editorToolbar) editorToolbar.style.display = 'none';
    if(textarea) textarea.classList.add('d-none');
    if(mediaDZ) mediaDZ.style.display = 'none';
    if(materialDZ) materialDZ.style.display = 'none';
    if(attachments) attachments.style.display = 'none';

    if (type === 'Video') {
        lbl.innerText = 'Video URL / Upload';
        if(mediaDZ) mediaDZ.style.display = 'block';
        if(textarea) textarea.classList.remove('d-none');
        textarea.placeholder = 'e.g., https://example.com/video.mp4 or upload below';
        // Extra file materials still allowed for Video lessons
        if(materialDZ) materialDZ.style.display = 'block';
        if(attachments) attachments.style.display = 'block';
    } else if (type === 'Quiz') {
        lbl.innerText = 'Quiz Question Description';
        if(textarea) textarea.classList.remove('d-none');
        textarea.placeholder = 'Provide the quiz questions or description for the student...';
        if(materialDZ) materialDZ.style.display = 'block';
        if(attachments) attachments.style.display = 'block';
    } else {
        lbl.innerText = 'Content Body';
        if(editorToolbar) editorToolbar.style.display = 'flex';
        if(htmlEditor) htmlEditor.style.display = 'block';
        if(materialDZ) materialDZ.style.display = 'block';
        if(attachments) attachments.style.display = 'block';
    }
}

function saveLesson() {
    var title = document.getElementById('txtLessonTitle').value.trim();
    var type = document.getElementById('ddlLessonType').value;
    var errDiv = document.getElementById('lessonModalError');
    errDiv.style.display = 'none';
    errDiv.innerText = '';

    if (!title) {
        errDiv.innerText = 'Please enter a lesson title.';
        errDiv.style.display = 'block';
        return;
    }
    if (!targetChapterId) {
        errDiv.innerText = 'No section selected. Close and open Add Lesson from a section.';
        errDiv.style.display = 'block';
        return;
    }

    var content = '';
    if (type === 'Video') {
        content = document.getElementById('txtLessonContent').value.trim();
    } else if (type === 'Quiz') {
        content = document.getElementById('txtLessonContent').value.trim();
    } else {
        var htmlEditor = document.getElementById('htmlEditor');
        content = htmlEditor ? htmlEditor.innerHTML.trim() : document.getElementById('txtLessonContent').value.trim();
        // treat empty editor shells as empty
        if (content === '<br>' || content === '<div><br></div>' || content === '<p><br></p>') content = '';
    }

    var materialsField = document.getElementById('lessonMaterials');
    var materialsRaw = materialsField ? (materialsField.value || '').trim() : '';
    var materialsArr = [];
    try { materialsArr = materialsRaw ? JSON.parse(materialsRaw) : []; } catch (e) { materialsArr = []; }
    if (!Array.isArray(materialsArr)) materialsArr = [];

    // Normalize each material to storePath + url for the server
    materialsArr = materialsArr.map(function (m) {
        var url = (m && (m.storePath || m.url || m.mediaLink)) || '';
        return {
            storePath: m.storePath || url,
            url: url,
            fileName: (m && m.fileName) || 'file',
            serveUrl: (m && m.serveUrl) || '',
            downloadUrl: (m && m.downloadUrl) || ''
        };
    }).filter(function (m) { return !!m.url; });

    // Allow save if we have content OR at least one uploaded material
    if (!content && materialsArr.length === 0 && type !== 'Quiz') {
        errDiv.innerText = type === 'Video'
        ? 'Upload a video or paste a video URL.'
        : 'Enter lesson content or upload at least one material file.';
        errDiv.style.display = 'block';
        return;
    }
    if (type === 'Quiz' && !content) {
        content = 'Quiz / assignment';
    }

    // Promote first uploaded file so preview always gets a real media path
    if (materialsArr.length > 0) {
        var firstUrl = materialsArr[0].storePath || materialsArr[0].url || '';
        var firstName = materialsArr[0].fileName || firstUrl;
        var kind = mediaKind(firstName + ' ' + firstUrl);
        if (type === 'Text' || type === 'Video') {
            // Video lesson: ensure content is the video path
            if (type === 'Video' && firstUrl && !content) content = firstUrl;
            // Text lesson with only a short placeholder body → use file as primary media
            var plain = (content || '').replace(/<[^>]+>/g, '').trim();
            if (type === 'Text' && firstUrl && (plain.length < 40 || plain === title)) {
                if (kind === 'video') type = 'Video';
                else if (kind === 'pdf') type = 'PDF';
                else if (kind === 'image') type = 'Image';
                else type = 'PDF';
                content = firstUrl;
            }
        }
    }

    var schid = editingLessonId ? parseInt(editingLessonId, 10) : 0;
    var saveBtn = document.querySelector('#lessonModal .btn-pill-accent');
    if (saveBtn) { saveBtn.disabled = true; saveBtn.textContent = 'Saving...'; }

    var matsJson = materialsArr.length ? JSON.stringify(materialsArr) : '[]';

    curriculumApi('save_lesson', {
        schid: schid,
        chid: parseInt(targetChapterId, 10),
        title: title,
        type: type,
        content: content,
        materialsJson: matsJson
    })
    .then(function (resObj) {
        if (resObj && resObj.success) {
            if (resObj.warning) console.warn('Lesson warning:', resObj.warning);
            if (materialsArr.length && resObj.materialsSaved === 0) {
                alert('Lesson saved, but materials may not have been stored (materialsSaved=0). Check StudyMats.MediaLink. Warning: ' +
                (resObj.warning || 'none'));
            }
            hideModal('lessonModal');
            setTimeout(function () { loadCurriculumView(); }, 200);
        } else {
            errDiv.innerText = (resObj && resObj.message) || 'Failed to save lesson.';
            errDiv.style.display = 'block';
        }
    })
    .catch(function (err) {
        errDiv.innerText = (err && err.message) ? err.message : 'Network error saving lesson.';
        errDiv.style.display = 'block';
        console.error(err);
    })
    .finally(function () {
        if (saveBtn) { saveBtn.disabled = false; saveBtn.textContent = 'Save Lesson'; }
    });
}

function deleteLesson(schid) {
    if (!confirm('Are you sure you want to delete this lesson?')) return;

    curriculumApi('delete_lesson', { schid: schid })
    .then(function (resObj) {
        if (resObj && resObj.success) loadCurriculumView();
        else alert('Delete failed: ' + ((resObj && resObj.message) || 'Unknown error'));
    })
    .catch(function (err) { console.error(err); alert((err && err.message) || 'Network error.'); });
}


```
