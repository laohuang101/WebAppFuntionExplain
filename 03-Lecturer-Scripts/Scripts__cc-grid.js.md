# cc-grid.js
**Source:** `Pages/Lecturer/Scripts/cc-grid.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 149
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `container` | `const/let/var` | Holds “container” for this scope. |
| `col` | `const/let/var` | Holds “col” for this scope. |
| `isPublished` | `const/let/var` | Course visibility flag for Landing catalog. |
| `statusBadgeClass` | `const/let/var` | Often a collection related to status Badge Class (plural name). |
| `statusText` | `const/let/var` | Holds “status Text” for this scope. |
| `rating` | `const/let/var` | Holds “rating” for this scope. |
| `ratingHtml` | `const/let/var` | Holds “rating Html” for this scope. |
| `pubBtnLabel` | `const/let/var` | Holds “pub Btn Label” for this scope. |
| `pubBtnIcon` | `const/let/var` | Holds “pub Btn Icon” for this scope. |
| `card` | `const/let/var` | Holds “card” for this scope. |
| `btn` | `const/let/var` | Button DOM element. |
| `action` | `const/let/var` | Holds “action” for this scope. |
| `msg` | `const/let/var` | Human-readable message (error or success). |

## Functions / methods (6 found)

### `loadCourses` — lines 3–22

#### Signature

```javascript
function loadCourses()
```

#### What it is

Browser JS: load the lecturer’s courses into a dropdown.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `renderCourseGrid` — lines 22–105

#### Signature

```javascript
function renderCourseGrid()
```

#### What it is

Updates the page HTML for **render Course Grid**.

#### How it works

1. Attach a browser event handler (click, load, change, …).
2. Stop the browser’s default action (for example form submit).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `container` | `—` | Holds “container” for this scope.  DOM element from the page. |
| `col` | `—` | Holds “col” for this scope. |
| `isPublished` | `—` | Course visibility flag for Landing catalog. |
| `statusBadgeClass` | `—` | Often a collection related to status Badge Class (plural name). |
| `statusText` | `—` | Holds “status Text” for this scope. |
| `rating` | `—` | Holds “rating” for this scope. |
| `ratingHtml` | `—` | Holds “rating Html” for this scope. |
| `pubBtnLabel` | `—` | Holds “pub Btn Label” for this scope. |
| `pubBtnIcon` | `—` | Holds “pub Btn Icon” for this scope. |
| `card` | `—` | Holds “card” for this scope. |
| `btn` | `—` | Button DOM element. |
| `action` | `—` | Holds “action” for this scope. |

#### Code

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

---

### `toggleCoursePublished` — lines 105–127

#### Signature

```javascript
function toggleCoursePublished(cid, publish)
```

#### What it is

Function `toggleCoursePublished` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. If the previous step failed, show the error and stop.
2. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `—` | Course ID (Courses.CID). |
| `publish` | `—` | Holds “publish” for this scope. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `msg` | `—` | Human-readable message (error or success). |

#### Code

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

---

### `openCoursePreview` — lines 127–131

#### Signature

```javascript
function openCoursePreview(cid)
```

#### What it is

Function `openCoursePreview` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `openCoursePreview`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `—` | Course ID (Courses.CID). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 127 | 
 128 | 
 129 | function openCoursePreview(cid) {
 130 |     window.location.href = 'CoursePreview.aspx?cid=' + encodeURIComponent(cid);
 131 | }
```

---

### `escapeHtml` — lines 131–149

#### Signature

```javascript
function escapeHtml(str)
```

#### What it is

Function `escapeHtml` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `str` | `—` | String value: str. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `deleteCourse` — lines 136–148

#### Signature

```javascript
function deleteCourse(cid)
```

#### What it is

Deletes or clears **delete Course** (data or temporary state).

#### How it works

1. Show a simple popup message to the user.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `—` | Course ID (Courses.CID). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
