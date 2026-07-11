# cc-grid.js
**Source:** `Pages/Lecturer/Scripts/cc-grid.js`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 149
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 25:** `container` — script-level `const`/`let`/`var` — **Holds “container” for this scope.**
- **Line 41:** `col` — script-level `const`/`let`/`var` — **Holds “col” for this scope.**
- **Line 43:** `isPublished` — script-level `const`/`let`/`var` — **Course visibility flag for Landing catalog.**
- **Line 45:** `statusBadgeClass` — script-level `const`/`let`/`var` — **Often a collection related to status Badge Class (plural name).**
- **Line 46:** `statusText` — script-level `const`/`let`/`var` — **Holds “status Text” for this scope.**
- **Line 47:** `rating` — script-level `const`/`let`/`var` — **Holds “rating” for this scope.**
- **Line 48:** `ratingHtml` — script-level `const`/`let`/`var` — **Holds “rating Html” for this scope.**
- **Line 51:** `pubBtnLabel` — script-level `const`/`let`/`var` — **Holds “pub Btn Label” for this scope.**
- **Line 52:** `pubBtnIcon` — script-level `const`/`let`/`var` — **Holds “pub Btn Icon” for this scope.**
- **Line 88:** `card` — script-level `const`/`let`/`var` — **Holds “card” for this scope.**
- **Line 90:** `btn` — script-level `const`/`let`/`var` — **Button DOM element.**
- **Line 94:** `action` — script-level `const`/`let`/`var` — **Holds “action” for this scope.**
- **Line 108:** `msg` — script-level `const`/`let`/`var` — **Human-readable message (error or success).**

## Functions / methods (6 found)

### `loadCourses` — lines 3–22

```javascript
function loadCourses()
```

#### Explanation

- **Purpose:** Implements `loadCourses`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Read/load data for display.

#### Line-by-line (this function)

```javascript
   3 | 
   4 | 
   5 | function loadCourses() {
   6 |     postJson('CourseCreation.aspx/GetCoursesData', {})
   7 |     .then(function (resObj) {
   8 |         if (resObj && resObj.success) {
   9 |             courses = resObj.courses || [];
  10 |             renderCourseGrid();
  11 |         } else {
  12 |             document.getElementById('courseGridContainer').innerHTML =
  13 |             '<div class="col-12 text-center text-danger py-4">Failed to load courses: ' +
  14 |             escapeHtml((resObj && resObj.message) || 'Unknown error') + '</div>';
  15 |         }
  16 |     })
  17 |     .catch(function (err) {
  18 |         console.error('Error loading courses: ', err);
  19 |         document.getElementById('courseGridContainer').innerHTML =
  20 |         '<div class="col-12 text-center text-danger py-4">Network error loading courses.</div>';
  21 |     });
  22 | }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L12:** Get HTML element by id.
- **L14:** Encode text to reduce XSS risk.
- **L19:** Get HTML element by id.

---

### `renderCourseGrid` — lines 22–105

```javascript
function renderCourseGrid()
```

#### Explanation

- **Purpose:** Implements `renderCourseGrid`.
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Local variables (what each means):**
- `container` — Holds “container” for this scope.  DOM element from the page.
- `col` — Holds “col” for this scope.
- `isPublished` — Course visibility flag for Landing catalog.
- `statusBadgeClass` — Often a collection related to status Badge Class (plural name).
- `statusText` — Holds “status Text” for this scope.
- `rating` — Holds “rating” for this scope.
- `ratingHtml` — Holds “rating Html” for this scope.
- `pubBtnLabel` — Holds “pub Btn Label” for this scope.
- `pubBtnIcon` — Holds “pub Btn Icon” for this scope.
- `card` — Holds “card” for this scope.
- `btn` — Button DOM element.
- `action` — Holds “action” for this scope.

#### Line-by-line (this function)

```javascript
  22 | 
  23 | 
  24 | function renderCourseGrid() {
  25 |     const container = document.getElementById('courseGridContainer');
  26 |     container.innerHTML = '';
  27 | 
  28 |     if (courses.length === 0) {
  29 |         container.innerHTML = `
  30 |         <div class="col-12 text-center py-5">
  31 |         <div class="glass-card p-5 d-inline-block" style="max-width: 450px;">
  32 |         <i class="fa-solid fa-folder-open fa-3x mb-3 text-muted" style="color: var(--primary-accent) !important; opacity:0.6;"></i>
  33 |         <h5 class="fw-bold">No Courses Created Yet</h5>
  34 |         <p class="text-muted small">Begin by clicking the "Create Course" button at the top right to start your syllabus.</p>
  35 |         </div>
  36 |         </div>`;
  37 |         return;
  38 |     }
  39 | 
  40 |     courses.forEach(c => {
  41 |         const col = document.createElement('div');
  42 |         col.className = 'col-lg-4 col-md-6';
  43 | 
  44 |         const isPublished = !!c.isPublished || (c.status === 'Published');
  45 |         const statusBadgeClass = isPublished ? 'badge-published' : 'badge-draft';
  46 |         const statusText = isPublished ? 'Published' : 'Draft';
  47 |         const rating = (c.rating != null && c.rating > 0) ? Number(c.rating).toFixed(1) : null;
  48 |         const ratingHtml = rating
  49 |         ? `<span class="ms-2"><i class="fa-solid fa-star" style="color:#f59e0b;"></i> ${rating}</span>`
  50 |         : '';
  51 |         const pubBtnLabel = isPublished ? 'Unpublish' : 'Publish';
  52 |         const pubBtnIcon = isPublished ? 'fa-eye-slash' : 'fa-cloud-arrow-up';
  53 | 
  54 |         col.innerHTML = `
  55 |         <div class="course-grid-card h-100 d-flex flex-column course-card-clickable" data-cid="${c.cid}" role="button" title="Open course preview">
  56 |         <div class="position-relative">
  57 |         <img src="${c.bgImg || 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=400'}" class="course-banner-img" alt="${escapeHtml(c.name)}">
  58 |         <div class="position-absolute top-0 end-0 m-3">
  59 |         <span class="badge-status ${statusBadgeClass}">${statusText}</span>
  60 |         </div>
  61 |         </div>
  62 |         <div class="p-4 d-flex flex-column flex-grow-1">
  63 |         <h5 class="course-title">${escapeHtml(c.name)}</h5>
  64 |         <div class="d-flex align-items-center text-muted small fw-semibold mb-3">
  65 |         <i class="fa-solid fa-user-group me-1"></i> ${c.studentsCount || 0}
  66 |         ${ratingHtml}
  67 |         </div>
  68 |         <div class="mt-auto d-flex justify-content-between align-items-center gap-2 pt-2 border-top border-light">
  69 |         <button type="button" class="btn btn-sm rounded-pill px-3 ${isPublished ? 'btn-outline-secondary' : 'btn-pill-accent'}" data-action="publish" title="${pubBtnLabel}">
  70 |         <i class="fa-solid ${pubBtnIcon} me-1"></i>${pubBtnLabel}
  71 |         </button>
  72 |         <div class="d-flex gap-1">
  73 |         <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="preview" title="Preview Course">
  74 |         <i class="fa-regular fa-eye"></i>
  75 |         </button>
  76 |         <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="edit" title="Edit Course">
  77 |         <i class="fa-solid fa-pencil"></i>
  78 |         </button>
  79 |         <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="delete" title="Delete Course">
  80 |         <i class="fa-regular fa-trash-can"></i>
  81 |         </button>
  82 |         </div>
  83 |         </div>
  84 |         </div>
  85 |         </div>`;
  86 | 
  87 |         // Card click → preview; action buttons stop propagation
  88 |         const card = col.querySelector('.course-card-clickable');
  89 |         card.addEventListener('click', function (e) {
  90 |             const btn = e.target.closest('[data-action]');
  91 |             if (btn) {
  92 |                 e.preventDefault();
  93 |                 e.stopPropagation();
  94 |                 const action = btn.getAttribute('data-action');
  95 |                 if (action === 'edit') editCourseBasicInfo(c.cid);
  96 |                 else if (action === 'delete') deleteCourse(c.cid);
  97 |                 else if (action === 'preview') openCoursePreview(c.cid);
  98 |                 else if (action === 'publish') toggleCoursePublished(c.cid, !isPublished);
  99 |                 return;
 100 |             }
 101 |             openCoursePreview(c.cid);
 102 |         });
 103 |         container.appendChild(col);
 104 |     });
 105 | }
```

<<<<<<< HEAD
**Line notes**

- **L25:** Get HTML element by id.
- **L26:** Update page HTML.
- **L29:** Update page HTML.
- **L54:** Update page HTML.
- **L57:** Encode text to reduce XSS risk.
- **L63:** Encode text to reduce XSS risk.
- **L89:** DOM event handler.
=======
**Line notes** (what code + variables mean)

- **L25:** Get HTML element by id. | `container` means: Holds “container” for this scope.  DOM element from the page.
- **L26:** Update page HTML.
- **L29:** Update page HTML.
- **L41:** `col` means: Holds “col” for this scope.
- **L44:** `isPublished` means: Course visibility flag for Landing catalog.
- **L45:** `statusBadgeClass` means: Often a collection related to status Badge Class (plural name).
- **L46:** `statusText` means: Holds “status Text” for this scope.
- **L47:** `rating` means: Holds “rating” for this scope.
- **L48:** `ratingHtml` means: Holds “rating Html” for this scope.
- **L51:** `pubBtnLabel` means: Holds “pub Btn Label” for this scope.
- **L52:** `pubBtnIcon` means: Holds “pub Btn Icon” for this scope.
- **L54:** Update page HTML.
- **L57:** Encode text to reduce XSS risk.
- **L63:** Encode text to reduce XSS risk.
- **L88:** `card` means: Holds “card” for this scope.
- **L89:** DOM event handler.
- **L90:** `btn` means: Button DOM element.
- **L94:** `action` means: Holds “action” for this scope.
>>>>>>> eb8ce01 (update)

---

### `toggleCoursePublished` — lines 105–127

```javascript
function toggleCoursePublished(cid, publish)
```

#### Explanation

- **Purpose:** Implements `toggleCoursePublished`.
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `cid` — Course ID (Courses.CID).
- `publish` — Holds “publish” for this scope.
- **Local variables (what each means):**
- `msg` — Human-readable message (error or success).

#### Line-by-line (this function)

```javascript
 105 | 
 106 | 
 107 | function toggleCoursePublished(cid, publish) {
 108 |     const msg = publish
 109 |         ? 'Publish this course so students can see it on the landing page?'
 110 |         : 'Unpublish this course? It will be hidden from the public catalogue.';
 111 |     if (!window.confirm(msg)) return;
 112 |     postJson('CourseCreation.aspx/SetCoursePublished', { cid: cid, published: !!publish })
 113 |         .then(function (res) {
 114 |             if (res && res.notAuthenticated) {
 115 |                 location.href = '/Pages/Authentication/Login.aspx';
 116 |                 return;
 117 |             }
 118 |             if (!res || !res.success) {
 119 |                 alert((res && res.message) || 'Could not update publish state.');
 120 |                 return;
 121 |             }
 122 |             loadCourses();
 123 |         })
 124 |         .catch(function (err) {
 125 |             alert(err.message || 'Could not update publish state.');
 126 |         });
 127 | }
```
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L108:** `msg` means: Human-readable message (error or success).
>>>>>>> eb8ce01 (update)

---

### `openCoursePreview` — lines 127–131

```javascript
function openCoursePreview(cid)
```

#### Explanation

- **Purpose:** Implements `openCoursePreview`.
- **Parameters (what each means):**
- `cid` — Course ID (Courses.CID).

#### Line-by-line (this function)

```javascript
 127 | 
 128 | 
 129 | function openCoursePreview(cid) {
 130 |     window.location.href = 'CoursePreview.aspx?cid=' + encodeURIComponent(cid);
 131 | }
```

---

### `escapeHtml` — lines 131–149

```javascript
function escapeHtml(str)
```

#### Explanation

- **Purpose:** Implements `escapeHtml`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Parameters (what each means):**
- `str` — String value: str.

#### Line-by-line (this function)

```javascript
 131 | 
 132 | 
 133 | function escapeHtml(str) {
 134 |     if (!str) return '';
 135 |     return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
 136 | }
 137 | 
 138 | 
 139 | function deleteCourse(cid) {
 140 |     if (!confirm('CAUTION: Are you sure you want to delete this course? This will remove all chapters, lessons, materials, and student enrollments! This action is permanent.')) return;
 141 | 
 142 |     postJson('CourseCreation.aspx/DeleteCourse', { cid: cid })
 143 |     .then(function (resObj) {
 144 |         if (resObj && resObj.success) loadCourses();
 145 |         else alert('Delete course failed: ' + ((resObj && resObj.message) || 'Unknown error'));
 146 |     })
 147 |     .catch(function (err) { console.error(err); alert('Network error.'); });
 148 | }
 149 | 
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L133:** Encode text to reduce XSS risk.

---

### `deleteCourse` — lines 136–148

```javascript
function deleteCourse(cid)
```

#### Explanation

- **Purpose:** Implements `deleteCourse`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Pattern:** Delete/clear data.
- **Parameters (what each means):**
- `cid` — Course ID (Courses.CID).

#### Line-by-line (this function)

```javascript
 136 | 
 137 | 
 138 | 
 139 | function deleteCourse(cid) {
 140 |     if (!confirm('CAUTION: Are you sure you want to delete this course? This will remove all chapters, lessons, materials, and student enrollments! This action is permanent.')) return;
 141 | 
 142 |     postJson('CourseCreation.aspx/DeleteCourse', { cid: cid })
 143 |     .then(function (resObj) {
 144 |         if (resObj && resObj.success) loadCourses();
 145 |         else alert('Delete course failed: ' + ((resObj && resObj.message) || 'Unknown error'));
 146 |     })
 147 |     .catch(function (err) { console.error(err); alert('Network error.'); });
 148 | }
```

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

```javascript
   1 | // Course Creation — course grid, publish, delete
   2 | // depends on: cc-core.js
   3 | // ---- Course grid / wizard / curriculum ----
   4 | 
   5 | function loadCourses() {
   6 |     postJson('CourseCreation.aspx/GetCoursesData', {})
   7 |     .then(function (resObj) {
   8 |         if (resObj && resObj.success) {
   9 |             courses = resObj.courses || [];
  10 |             renderCourseGrid();
  11 |         } else {
  12 |             document.getElementById('courseGridContainer').innerHTML =
  13 |             '<div class="col-12 text-center text-danger py-4">Failed to load courses: ' +
  14 |             escapeHtml((resObj && resObj.message) || 'Unknown error') + '</div>';
  15 |         }
  16 |     })
  17 |     .catch(function (err) {
  18 |         console.error('Error loading courses: ', err);
  19 |         document.getElementById('courseGridContainer').innerHTML =
  20 |         '<div class="col-12 text-center text-danger py-4">Network error loading courses.</div>';
  21 |     });
  22 | }
  23 | 
  24 | function renderCourseGrid() {
  25 |     const container = document.getElementById('courseGridContainer');
  26 |     container.innerHTML = '';
  27 | 
  28 |     if (courses.length === 0) {
  29 |         container.innerHTML = `
  30 |         <div class="col-12 text-center py-5">
  31 |         <div class="glass-card p-5 d-inline-block" style="max-width: 450px;">
  32 |         <i class="fa-solid fa-folder-open fa-3x mb-3 text-muted" style="color: var(--primary-accent) !important; opacity:0.6;"></i>
  33 |         <h5 class="fw-bold">No Courses Created Yet</h5>
  34 |         <p class="text-muted small">Begin by clicking the "Create Course" button at the top right to start your syllabus.</p>
  35 |         </div>
  36 |         </div>`;
  37 |         return;
  38 |     }
  39 | 
  40 |     courses.forEach(c => {
  41 |         const col = document.createElement('div');
  42 |         col.className = 'col-lg-4 col-md-6';
  43 | 
  44 |         const isPublished = !!c.isPublished || (c.status === 'Published');
  45 |         const statusBadgeClass = isPublished ? 'badge-published' : 'badge-draft';
  46 |         const statusText = isPublished ? 'Published' : 'Draft';
  47 |         const rating = (c.rating != null && c.rating > 0) ? Number(c.rating).toFixed(1) : null;
  48 |         const ratingHtml = rating
  49 |         ? `<span class="ms-2"><i class="fa-solid fa-star" style="color:#f59e0b;"></i> ${rating}</span>`
  50 |         : '';
  51 |         const pubBtnLabel = isPublished ? 'Unpublish' : 'Publish';
  52 |         const pubBtnIcon = isPublished ? 'fa-eye-slash' : 'fa-cloud-arrow-up';
  53 | 
  54 |         col.innerHTML = `
  55 |         <div class="course-grid-card h-100 d-flex flex-column course-card-clickable" data-cid="${c.cid}" role="button" title="Open course preview">
  56 |         <div class="position-relative">
  57 |         <img src="${c.bgImg || 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=400'}" class="course-banner-img" alt="${escapeHtml(c.name)}">
  58 |         <div class="position-absolute top-0 end-0 m-3">
  59 |         <span class="badge-status ${statusBadgeClass}">${statusText}</span>
  60 |         </div>
  61 |         </div>
  62 |         <div class="p-4 d-flex flex-column flex-grow-1">
  63 |         <h5 class="course-title">${escapeHtml(c.name)}</h5>
  64 |         <div class="d-flex align-items-center text-muted small fw-semibold mb-3">
  65 |         <i class="fa-solid fa-user-group me-1"></i> ${c.studentsCount || 0}
  66 |         ${ratingHtml}
  67 |         </div>
  68 |         <div class="mt-auto d-flex justify-content-between align-items-center gap-2 pt-2 border-top border-light">
  69 |         <button type="button" class="btn btn-sm rounded-pill px-3 ${isPublished ? 'btn-outline-secondary' : 'btn-pill-accent'}" data-action="publish" title="${pubBtnLabel}">
  70 |         <i class="fa-solid ${pubBtnIcon} me-1"></i>${pubBtnLabel}
  71 |         </button>
  72 |         <div class="d-flex gap-1">
  73 |         <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="preview" title="Preview Course">
  74 |         <i class="fa-regular fa-eye"></i>
  75 |         </button>
  76 |         <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="edit" title="Edit Course">
  77 |         <i class="fa-solid fa-pencil"></i>
  78 |         </button>
  79 |         <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="delete" title="Delete Course">
  80 |         <i class="fa-regular fa-trash-can"></i>
  81 |         </button>
  82 |         </div>
  83 |         </div>
  84 |         </div>
  85 |         </div>`;
  86 | 
  87 |         // Card click → preview; action buttons stop propagation
  88 |         const card = col.querySelector('.course-card-clickable');
  89 |         card.addEventListener('click', function (e) {
  90 |             const btn = e.target.closest('[data-action]');
  91 |             if (btn) {
  92 |                 e.preventDefault();
  93 |                 e.stopPropagation();
  94 |                 const action = btn.getAttribute('data-action');
  95 |                 if (action === 'edit') editCourseBasicInfo(c.cid);
  96 |                 else if (action === 'delete') deleteCourse(c.cid);
  97 |                 else if (action === 'preview') openCoursePreview(c.cid);
  98 |                 else if (action === 'publish') toggleCoursePublished(c.cid, !isPublished);
  99 |                 return;
 100 |             }
 101 |             openCoursePreview(c.cid);
 102 |         });
 103 |         container.appendChild(col);
 104 |     });
 105 | }
 106 | 
 107 | function toggleCoursePublished(cid, publish) {
 108 |     const msg = publish
 109 |         ? 'Publish this course so students can see it on the landing page?'
 110 |         : 'Unpublish this course? It will be hidden from the public catalogue.';
 111 |     if (!window.confirm(msg)) return;
 112 |     postJson('CourseCreation.aspx/SetCoursePublished', { cid: cid, published: !!publish })
 113 |         .then(function (res) {
 114 |             if (res && res.notAuthenticated) {
 115 |                 location.href = '/Pages/Authentication/Login.aspx';
 116 |                 return;
 117 |             }
 118 |             if (!res || !res.success) {
 119 |                 alert((res && res.message) || 'Could not update publish state.');
 120 |                 return;
 121 |             }
 122 |             loadCourses();
 123 |         })
 124 |         .catch(function (err) {
 125 |             alert(err.message || 'Could not update publish state.');
 126 |         });
 127 | }
 128 | 
 129 | function openCoursePreview(cid) {
 130 |     window.location.href = 'CoursePreview.aspx?cid=' + encodeURIComponent(cid);
 131 | }
 132 | 
 133 | function escapeHtml(str) {
 134 |     if (!str) return '';
 135 |     return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
 136 | }
 137 | 
 138 | 
 139 | function deleteCourse(cid) {
 140 |     if (!confirm('CAUTION: Are you sure you want to delete this course? This will remove all chapters, lessons, materials, and student enrollments! This action is permanent.')) return;
 141 | 
 142 |     postJson('CourseCreation.aspx/DeleteCourse', { cid: cid })
 143 |     .then(function (resObj) {
 144 |         if (resObj && resObj.success) loadCourses();
 145 |         else alert('Delete course failed: ' + ((resObj && resObj.message) || 'Unknown error'));
 146 |     })
 147 |     .catch(function (err) { console.error(err); alert('Network error.'); });
 148 | }
 149 | 
```

**Line notes**

- **L12:** Get HTML element by id.
- **L14:** Encode text to reduce XSS risk.
- **L19:** Get HTML element by id.
<<<<<<< HEAD
- **L25:** Get HTML element by id.
- **L26:** Update page HTML.
- **L29:** Update page HTML.
- **L54:** Update page HTML.
- **L57:** Encode text to reduce XSS risk.
- **L63:** Encode text to reduce XSS risk.
- **L89:** DOM event handler.
=======
- **L25:** Get HTML element by id. | `container` means: Holds “container” for this scope.  DOM element from the page.
- **L26:** Update page HTML.
- **L29:** Update page HTML.
- **L41:** `col` means: Holds “col” for this scope.
- **L44:** `isPublished` means: Course visibility flag for Landing catalog.
- **L45:** `statusBadgeClass` means: Often a collection related to status Badge Class (plural name).
- **L46:** `statusText` means: Holds “status Text” for this scope.
- **L47:** `rating` means: Holds “rating” for this scope.
- **L48:** `ratingHtml` means: Holds “rating Html” for this scope.
- **L51:** `pubBtnLabel` means: Holds “pub Btn Label” for this scope.
- **L52:** `pubBtnIcon` means: Holds “pub Btn Icon” for this scope.
- **L54:** Update page HTML.
- **L57:** Encode text to reduce XSS risk.
- **L63:** Encode text to reduce XSS risk.
- **L88:** `card` means: Holds “card” for this scope.
- **L89:** DOM event handler.
- **L90:** `btn` means: Button DOM element.
- **L94:** `action` means: Holds “action” for this scope.
- **L108:** `msg` means: Human-readable message (error or success).
>>>>>>> eb8ce01 (update)
- **L133:** Encode text to reduce XSS risk.

## Source snapshot (raw)

```javascript
// Course Creation — course grid, publish, delete
// depends on: cc-core.js
// ---- Course grid / wizard / curriculum ----

function loadCourses() {
    postJson('CourseCreation.aspx/GetCoursesData', {})
    .then(function (resObj) {
        if (resObj && resObj.success) {
            courses = resObj.courses || [];
            renderCourseGrid();
        } else {
            document.getElementById('courseGridContainer').innerHTML =
            '<div class="col-12 text-center text-danger py-4">Failed to load courses: ' +
            escapeHtml((resObj && resObj.message) || 'Unknown error') + '</div>';
        }
    })
    .catch(function (err) {
        console.error('Error loading courses: ', err);
        document.getElementById('courseGridContainer').innerHTML =
        '<div class="col-12 text-center text-danger py-4">Network error loading courses.</div>';
    });
}

function renderCourseGrid() {
    const container = document.getElementById('courseGridContainer');
    container.innerHTML = '';

    if (courses.length === 0) {
        container.innerHTML = `
        <div class="col-12 text-center py-5">
        <div class="glass-card p-5 d-inline-block" style="max-width: 450px;">
        <i class="fa-solid fa-folder-open fa-3x mb-3 text-muted" style="color: var(--primary-accent) !important; opacity:0.6;"></i>
        <h5 class="fw-bold">No Courses Created Yet</h5>
        <p class="text-muted small">Begin by clicking the "Create Course" button at the top right to start your syllabus.</p>
        </div>
        </div>`;
        return;
    }

    courses.forEach(c => {
        const col = document.createElement('div');
        col.className = 'col-lg-4 col-md-6';

        const isPublished = !!c.isPublished || (c.status === 'Published');
        const statusBadgeClass = isPublished ? 'badge-published' : 'badge-draft';
        const statusText = isPublished ? 'Published' : 'Draft';
        const rating = (c.rating != null && c.rating > 0) ? Number(c.rating).toFixed(1) : null;
        const ratingHtml = rating
        ? `<span class="ms-2"><i class="fa-solid fa-star" style="color:#f59e0b;"></i> ${rating}</span>`
        : '';
        const pubBtnLabel = isPublished ? 'Unpublish' : 'Publish';
        const pubBtnIcon = isPublished ? 'fa-eye-slash' : 'fa-cloud-arrow-up';

        col.innerHTML = `
        <div class="course-grid-card h-100 d-flex flex-column course-card-clickable" data-cid="${c.cid}" role="button" title="Open course preview">
        <div class="position-relative">
        <img src="${c.bgImg || 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=400'}" class="course-banner-img" alt="${escapeHtml(c.name)}">
        <div class="position-absolute top-0 end-0 m-3">
        <span class="badge-status ${statusBadgeClass}">${statusText}</span>
        </div>
        </div>
        <div class="p-4 d-flex flex-column flex-grow-1">
        <h5 class="course-title">${escapeHtml(c.name)}</h5>
        <div class="d-flex align-items-center text-muted small fw-semibold mb-3">
        <i class="fa-solid fa-user-group me-1"></i> ${c.studentsCount || 0}
        ${ratingHtml}
        </div>
        <div class="mt-auto d-flex justify-content-between align-items-center gap-2 pt-2 border-top border-light">
        <button type="button" class="btn btn-sm rounded-pill px-3 ${isPublished ? 'btn-outline-secondary' : 'btn-pill-accent'}" data-action="publish" title="${pubBtnLabel}">
        <i class="fa-solid ${pubBtnIcon} me-1"></i>${pubBtnLabel}
        </button>
        <div class="d-flex gap-1">
        <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="preview" title="Preview Course">
        <i class="fa-regular fa-eye"></i>
        </button>
        <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="edit" title="Edit Course">
        <i class="fa-solid fa-pencil"></i>
        </button>
        <button type="button" class="btn btn-sm btn-link text-secondary p-1" data-action="delete" title="Delete Course">
        <i class="fa-regular fa-trash-can"></i>
        </button>
        </div>
        </div>
        </div>
        </div>`;

        // Card click → preview; action buttons stop propagation
        const card = col.querySelector('.course-card-clickable');
        card.addEventListener('click', function (e) {
            const btn = e.target.closest('[data-action]');
            if (btn) {
                e.preventDefault();
                e.stopPropagation();
                const action = btn.getAttribute('data-action');
                if (action === 'edit') editCourseBasicInfo(c.cid);
                else if (action === 'delete') deleteCourse(c.cid);
                else if (action === 'preview') openCoursePreview(c.cid);
                else if (action === 'publish') toggleCoursePublished(c.cid, !isPublished);
                return;
            }
            openCoursePreview(c.cid);
        });
        container.appendChild(col);
    });
}

function toggleCoursePublished(cid, publish) {
    const msg = publish
        ? 'Publish this course so students can see it on the landing page?'
        : 'Unpublish this course? It will be hidden from the public catalogue.';
    if (!window.confirm(msg)) return;
    postJson('CourseCreation.aspx/SetCoursePublished', { cid: cid, published: !!publish })
        .then(function (res) {
            if (res && res.notAuthenticated) {
                location.href = '/Pages/Authentication/Login.aspx';
                return;
            }
            if (!res || !res.success) {
                alert((res && res.message) || 'Could not update publish state.');
                return;
            }
            loadCourses();
        })
        .catch(function (err) {
            alert(err.message || 'Could not update publish state.');
        });
}

function openCoursePreview(cid) {
    window.location.href = 'CoursePreview.aspx?cid=' + encodeURIComponent(cid);
}

function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}


function deleteCourse(cid) {
    if (!confirm('CAUTION: Are you sure you want to delete this course? This will remove all chapters, lessons, materials, and student enrollments! This action is permanent.')) return;

    postJson('CourseCreation.aspx/DeleteCourse', { cid: cid })
    .then(function (resObj) {
        if (resObj && resObj.success) loadCourses();
        else alert('Delete course failed: ' + ((resObj && resObj.message) || 'Unknown error'));
    })
    .catch(function (err) { console.error(err); alert('Network error.'); });
}


```
