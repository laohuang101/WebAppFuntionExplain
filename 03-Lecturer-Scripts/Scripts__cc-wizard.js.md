# cc-wizard.js
**Source:** `Pages/Lecturer/Scripts/cc-wizard.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 172
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `prev` | `const/let/var` | Holds “prev” for this scope. |
| `dzMsg` | `const/let/var` | Holds “dz Msg” for this scope. |
| `params` | `const/let/var` | Often a collection related to params (plural name). |
| `editId` | `const/let/var` | Identifier (`editId`) — database primary/foreign key. |
| `tries` | `const/let/var` | Often a collection related to tries (plural name). |
| `t` | `const/let/var` | Temporary string/token/time value. |
| `c` | `const/let/var` | Temporary value (character, course, or counter depending on loop). |
| `prevEdit` | `const/let/var` | Holds “prev Edit” for this scope. |
| `step1` | `const/let/var` | Holds “step1” for this scope. |
| `step2` | `const/let/var` | Holds “step2” for this scope. |
| `stepLine` | `const/let/var` | Holds “step Line” for this scope. |
| `name` | `const/let/var` | Display name of user/course/criterion. |
| `desc` | `const/let/var` | Description text (may embed <<<META>>> JSON). |
| `category` | `const/let/var` | Holds “category” for this scope. |
| `level` | `const/let/var` | Holds “level” for this scope. |
| `bgImg` | `const/let/var` | Holds “bg Img” for this scope. |
| `errDiv` | `const/let/var` | Holds “err Div” for this scope. |
| `modalEl` | `const/let/var` | Holds “modal El” for this scope. |
| `modal` | `const/let/var` | Holds “modal” for this scope. |

## Functions / methods (7 found)

### `showCreateCourseModal` — lines 2–26

#### Signature

```javascript
function showCreateCourseModal()
```

#### What it is

Updates the page HTML for **show Create Course Modal**.

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `prev` | `—` | Holds “prev” for this scope.  DOM element from the page. |
| `dzMsg` | `—` | Holds “dz Msg” for this scope.  DOM element from the page. |

#### Code

```javascript
   2 | 
   3 | function showCreateCourseModal() {
   4 |     currentCourseId = null;
   5 |     editingSectionId = null;
   6 |     editingLessonId = null;
   7 | 
   8 |     // Reset form fields
   9 |     document.getElementById('txtCourseTitle').value = '';
  10 |     document.getElementById('txtCourseDesc').value = '';
  11 |     document.getElementById('ddlCategory').value = 'Development';
  12 |     document.getElementById('ddlLevel').value = 'Beginner';
  13 |     document.getElementById('txtBgImg').value = '';
  14 |     const prev = document.getElementById('courseThumbPreview');
  15 |     if (prev) { prev.src = ''; prev.classList.add('d-none'); }
  16 |     const dzMsg = document.getElementById('dzMessage');
  17 |     if (dzMsg) dzMsg.innerHTML = '<i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>Click to upload image (16:9 ratio)';
  18 | 
  19 |     document.getElementById('step1Error').style.display = 'none';
  20 | 
  21 |     document.getElementById('wizardModalTitle').innerText = "Create New Course";
  22 | 
  23 |     setWizardStep(1);
  24 | 
  25 |     showModal('courseWizardModal');
  26 | }
```

---

### `editCourseBasicInfo` — lines 50–73

#### Signature

```javascript
function editCourseBasicInfo(cid)
```

#### What it is

Function `editCourseBasicInfo` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `cid` | `—` | Course ID (Courses.CID). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `c` | `—` | Course object/row. |
| `prevEdit` | `—` | Holds “prev Edit” for this scope.  DOM element from the page. |

#### Code

```javascript
  50 | 
  51 | 
  52 | function editCourseBasicInfo(cid) {
  53 |     const c = courses.find(item => item.cid === cid);
  54 |     if (!c) return;
  55 | 
  56 |     currentCourseId = cid;
  57 |     document.getElementById('txtCourseTitle').value = c.name;
  58 |     document.getElementById('txtCourseDesc').value = c.description;
  59 |     if (c.category) document.getElementById('ddlCategory').value = c.category;
  60 |     if (c.level) document.getElementById('ddlLevel').value = c.level;
  61 |     document.getElementById('txtBgImg').value = c.bgImg || '';
  62 |     const prevEdit = document.getElementById('courseThumbPreview');
  63 |     if (prevEdit && c.bgImg) {
  64 |         prevEdit.src = c.bgImg;
  65 |         prevEdit.classList.remove('d-none');
  66 |     }
  67 | 
  68 |     document.getElementById('step1Error').style.display = 'none';
  69 |     document.getElementById('wizardModalTitle').innerText = 'Edit Course: ' + c.name;
  70 | 
  71 |     setWizardStep(1);
  72 |     showModal('courseWizardModal');
  73 | }
```

---

### `setWizardStep` — lines 73–114

#### Signature

```javascript
function setWizardStep(step)
```

#### What it is

Saves or updates **set Wizard Step** in the database or UI state.

#### How it works

1. Starts when something calls `setWizardStep`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `step` | `—` | TOTP 30-second time step counter. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `step1` | `—` | Holds “step1” for this scope.  DOM element from the page. |
| `step2` | `—` | Holds “step2” for this scope.  DOM element from the page. |
| `stepLine` | `—` | Holds “step Line” for this scope.  DOM element from the page. |

#### Code

```javascript
  73 | 
  74 | 
  75 | function setWizardStep(step) {
  76 |     activeWizardStep = step;
  77 |     const step1 = document.getElementById('stepIndicator1');
  78 |     const step2 = document.getElementById('stepIndicator2');
  79 |     const stepLine = document.getElementById('stepLine1');
  80 | 
  81 |     if (step === 1) {
  82 |         // Indicators
  83 |         step1.classList.remove('completed');
  84 |         step1.classList.add('active');
  85 |         step2.classList.remove('active');
  86 |         step2.classList.remove('completed');
  87 |         stepLine.classList.remove('active');
  88 | 
  89 |         // Form panels
  90 |         document.getElementById('wizardStep1').style.display = 'block';
  91 |         document.getElementById('wizardStep2').style.display = 'none';
  92 | 
  93 |         // Footers
  94 |         document.getElementById('wizardFooterStep1').style.display = 'flex';
  95 |         document.getElementById('wizardFooterStep2').style.setProperty('display', 'none', 'important');
  96 |     } else {
  97 |         // Indicators
  98 |         step1.classList.remove('active');
  99 |         step1.classList.add('completed');
 100 |         step2.classList.add('active');
 101 |         stepLine.classList.add('active');
 102 | 
 103 |         // Form panels
 104 |         document.getElementById('wizardStep1').style.display = 'none';
 105 |         document.getElementById('wizardStep2').style.display = 'block';
 106 | 
 107 |         // Footers
 108 |         document.getElementById('wizardFooterStep1').style.setProperty('display', 'none', 'important');
 109 |         document.getElementById('wizardFooterStep2').style.setProperty('display', 'flex', 'important');
 110 | 
 111 |         // Load Curriculum
 112 |         loadCurriculumView();
 113 |     }
 114 | }
```

---

### `nextWizardStep` — lines 114–155

#### Signature

```javascript
function nextWizardStep()
```

#### What it is

Function `nextWizardStep` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Update a page element (text, HTML, value, or enabled/disabled).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `name` | `—` | Display name of user/course/criterion.  DOM element from the page. |
| `desc` | `—` | Description text (may embed <<<META>>> JSON).  DOM element from the page. |
| `category` | `—` | Holds “category” for this scope.  DOM element from the page. |
| `level` | `—` | Holds “level” for this scope.  DOM element from the page. |
| `bgImg` | `—` | Holds “bg Img” for this scope.  DOM element from the page. |
| `errDiv` | `—` | Holds “err Div” for this scope.  DOM element from the page. |

#### Code

```javascript
 114 | 
 115 | 
 116 | 
 117 | function nextWizardStep() {
 118 |     const name = document.getElementById('txtCourseTitle').value.trim();
 119 |     const desc = document.getElementById('txtCourseDesc').value.trim();
 120 |     const category = document.getElementById('ddlCategory').value;
 121 |     const level = document.getElementById('ddlLevel').value;
 122 |     const bgImg = document.getElementById('txtBgImg').value.trim();
 123 |     const errDiv = document.getElementById('step1Error');
 124 | 
 125 |     errDiv.style.display = 'none';
 126 | 
 127 |     if (!name || !desc) {
 128 |         errDiv.innerText = "Please fill in all required fields (Title and Description).";
 129 |         errDiv.style.display = 'block';
 130 |         return;
 131 |     }
 132 | 
 133 |     postJson('CourseCreation.aspx/SaveCourseInfo', {
 134 |         name: name,
 135 |         desc: desc,
 136 |         category: category,
 137 |         level: level,
 138 |         bgImg: bgImg,
 139 |         cid: currentCourseId || 0
 140 |     })
 141 |     .then(function (resObj) {
 142 |         if (resObj && resObj.success) {
 143 |             currentCourseId = resObj.cid;
 144 |             setWizardStep(2);
 145 |         } else {
 146 |             errDiv.innerText = (resObj && resObj.message) || 'Failed to save course details.';
 147 |             errDiv.style.display = 'block';
 148 |         }
 149 |     })
 150 |     .catch(function (err) {
 151 |         errDiv.innerText = 'Network error saving course.';
 152 |         errDiv.style.display = 'block';
 153 |         console.error(err);
 154 |     });
 155 | }
```

---

### `prevWizardStep` — lines 155–159

#### Signature

```javascript
function prevWizardStep()
```

#### What it is

Function `prevWizardStep` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `prevWizardStep`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 155 | 
 156 | 
 157 | function prevWizardStep() {
 158 |     setWizardStep(1);
 159 | }
```

---

### `completeWizard` — lines 159–166

#### Signature

```javascript
function completeWizard()
```

#### What it is

Function `completeWizard` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `completeWizard`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `modalEl` | `—` | Holds “modal El” for this scope.  DOM element from the page. |
| `modal` | `—` | Holds “modal” for this scope. |

#### Code

```javascript
 159 | 
 160 | 
 161 | function completeWizard() {
 162 |     const modalEl = document.getElementById('courseWizardModal');
 163 |     const modal = bootstrap.Modal.getInstance(modalEl);
 164 |     modal.hide();
 165 |     loadCourses(); // Refresh list
 166 | }
```

---

### `confirmCloseWizard` — lines 166–171

#### Signature

```javascript
function confirmCloseWizard(e)
```

#### What it is

Function `confirmCloseWizard` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `confirmCloseWizard`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `e` | `—` | Often email string (C#) or DOM event (JS). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
 166 | 
 167 | 
 168 | function confirmCloseWizard(e) {
 169 |     // Reload courses in case they cancelled early on step 2 (curriculum changes are saved incrementally)
 170 |     loadCourses();
 171 | }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 | // Course Creation — wizard create/edit course
   2 | // depends on: cc-core.js, cc-grid.js
   3 | function showCreateCourseModal() {
   4 |     currentCourseId = null;
   5 |     editingSectionId = null;
   6 |     editingLessonId = null;
   7 | 
   8 |     // Reset form fields
   9 |     document.getElementById('txtCourseTitle').value = '';
  10 |     document.getElementById('txtCourseDesc').value = '';
  11 |     document.getElementById('ddlCategory').value = 'Development';
  12 |     document.getElementById('ddlLevel').value = 'Beginner';
  13 |     document.getElementById('txtBgImg').value = '';
  14 |     const prev = document.getElementById('courseThumbPreview');
  15 |     if (prev) { prev.src = ''; prev.classList.add('d-none'); }
  16 |     const dzMsg = document.getElementById('dzMessage');
  17 |     if (dzMsg) dzMsg.innerHTML = '<i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>Click to upload image (16:9 ratio)';
  18 | 
  19 |     document.getElementById('step1Error').style.display = 'none';
  20 | 
  21 |     document.getElementById('wizardModalTitle').innerText = "Create New Course";
  22 | 
  23 |     setWizardStep(1);
  24 | 
  25 |     showModal('courseWizardModal');
  26 | }
  27 | 
  28 | // Deep-link: CourseCreation.aspx?edit=123 (from preview Edit button)
  29 | document.addEventListener('DOMContentLoaded', function () {
  30 |     try {
  31 |         var params = new URLSearchParams(window.location.search);
  32 |         var editId = parseInt(params.get('edit') || sessionStorage.getItem('editCourseId') || '0', 10);
  33 |         if (editId > 0) {
  34 |             sessionStorage.removeItem('editCourseId');
  35 |             // Wait for courses to load then open editor
  36 |             var tries = 0;
  37 |             var t = setInterval(function () {
  38 |                 tries++;
  39 |                 if (courses && courses.length) {
  40 |                     clearInterval(t);
  41 |                     editCourseBasicInfo(editId);
  42 |                     // jump to curriculum step if already saved
  43 |                     if (currentCourseId) setTimeout(function () { setWizardStep(2); }, 200);
  44 |                 } else if (tries > 40) {
  45 |                     clearInterval(t);
  46 |                 }
  47 |             }, 100);
  48 |         }
  49 |     } catch (e) { /* ignore */ }
  50 | });
  51 | 
  52 | function editCourseBasicInfo(cid) {
  53 |     const c = courses.find(item => item.cid === cid);
  54 |     if (!c) return;
  55 | 
  56 |     currentCourseId = cid;
  57 |     document.getElementById('txtCourseTitle').value = c.name;
  58 |     document.getElementById('txtCourseDesc').value = c.description;
  59 |     if (c.category) document.getElementById('ddlCategory').value = c.category;
  60 |     if (c.level) document.getElementById('ddlLevel').value = c.level;
  61 |     document.getElementById('txtBgImg').value = c.bgImg || '';
  62 |     const prevEdit = document.getElementById('courseThumbPreview');
  63 |     if (prevEdit && c.bgImg) {
  64 |         prevEdit.src = c.bgImg;
  65 |         prevEdit.classList.remove('d-none');
  66 |     }
  67 | 
  68 |     document.getElementById('step1Error').style.display = 'none';
  69 |     document.getElementById('wizardModalTitle').innerText = 'Edit Course: ' + c.name;
  70 | 
  71 |     setWizardStep(1);
  72 |     showModal('courseWizardModal');
  73 | }
  74 | 
  75 | function setWizardStep(step) {
  76 |     activeWizardStep = step;
  77 |     const step1 = document.getElementById('stepIndicator1');
  78 |     const step2 = document.getElementById('stepIndicator2');
  79 |     const stepLine = document.getElementById('stepLine1');
  80 | 
  81 |     if (step === 1) {
  82 |         // Indicators
  83 |         step1.classList.remove('completed');
  84 |         step1.classList.add('active');
  85 |         step2.classList.remove('active');
  86 |         step2.classList.remove('completed');
  87 |         stepLine.classList.remove('active');
  88 | 
  89 |         // Form panels
  90 |         document.getElementById('wizardStep1').style.display = 'block';
  91 |         document.getElementById('wizardStep2').style.display = 'none';
  92 | 
  93 |         // Footers
  94 |         document.getElementById('wizardFooterStep1').style.display = 'flex';
  95 |         document.getElementById('wizardFooterStep2').style.setProperty('display', 'none', 'important');
  96 |     } else {
  97 |         // Indicators
  98 |         step1.classList.remove('active');
  99 |         step1.classList.add('completed');
 100 |         step2.classList.add('active');
 101 |         stepLine.classList.add('active');
 102 | 
 103 |         // Form panels
 104 |         document.getElementById('wizardStep1').style.display = 'none';
 105 |         document.getElementById('wizardStep2').style.display = 'block';
 106 | 
 107 |         // Footers
 108 |         document.getElementById('wizardFooterStep1').style.setProperty('display', 'none', 'important');
 109 |         document.getElementById('wizardFooterStep2').style.setProperty('display', 'flex', 'important');
 110 | 
 111 |         // Load Curriculum
 112 |         loadCurriculumView();
 113 |     }
 114 | }
 115 | 
 116 | 
 117 | function nextWizardStep() {
 118 |     const name = document.getElementById('txtCourseTitle').value.trim();
 119 |     const desc = document.getElementById('txtCourseDesc').value.trim();
 120 |     const category = document.getElementById('ddlCategory').value;
 121 |     const level = document.getElementById('ddlLevel').value;
 122 |     const bgImg = document.getElementById('txtBgImg').value.trim();
 123 |     const errDiv = document.getElementById('step1Error');
 124 | 
 125 |     errDiv.style.display = 'none';
 126 | 
 127 |     if (!name || !desc) {
 128 |         errDiv.innerText = "Please fill in all required fields (Title and Description).";
 129 |         errDiv.style.display = 'block';
 130 |         return;
 131 |     }
 132 | 
 133 |     postJson('CourseCreation.aspx/SaveCourseInfo', {
 134 |         name: name,
 135 |         desc: desc,
 136 |         category: category,
 137 |         level: level,
 138 |         bgImg: bgImg,
 139 |         cid: currentCourseId || 0
 140 |     })
 141 |     .then(function (resObj) {
 142 |         if (resObj && resObj.success) {
 143 |             currentCourseId = resObj.cid;
 144 |             setWizardStep(2);
 145 |         } else {
 146 |             errDiv.innerText = (resObj && resObj.message) || 'Failed to save course details.';
 147 |             errDiv.style.display = 'block';
 148 |         }
 149 |     })
 150 |     .catch(function (err) {
 151 |         errDiv.innerText = 'Network error saving course.';
 152 |         errDiv.style.display = 'block';
 153 |         console.error(err);
 154 |     });
 155 | }
 156 | 
 157 | function prevWizardStep() {
 158 |     setWizardStep(1);
 159 | }
 160 | 
 161 | function completeWizard() {
 162 |     const modalEl = document.getElementById('courseWizardModal');
 163 |     const modal = bootstrap.Modal.getInstance(modalEl);
 164 |     modal.hide();
 165 |     loadCourses(); // Refresh list
 166 | }
 167 | 
 168 | function confirmCloseWizard(e) {
 169 |     // Reload courses in case they cancelled early on step 2 (curriculum changes are saved incrementally)
 170 |     loadCourses();
 171 | }
 172 | 
```
