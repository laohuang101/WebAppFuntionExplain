# cc-wizard.js
**Source:** `Pages/Lecturer/Scripts/cc-wizard.js`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 172
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 14:** `prev` — script-level `const`/`let`/`var` — **Holds “prev” for this scope.**
- **Line 16:** `dzMsg` — script-level `const`/`let`/`var` — **Holds “dz Msg” for this scope.**
- **Line 31:** `params` — script-level `const`/`let`/`var` — **Often a collection related to params (plural name).**
- **Line 32:** `editId` — script-level `const`/`let`/`var` — **Identifier (`editId`) — database primary/foreign key.**
- **Line 36:** `tries` — script-level `const`/`let`/`var` — **Often a collection related to tries (plural name).**
- **Line 37:** `t` — script-level `const`/`let`/`var` — **Temporary string/token/time value.**
- **Line 53:** `c` — script-level `const`/`let`/`var` — **Temporary value (character, course, or counter depending on loop).**
- **Line 62:** `prevEdit` — script-level `const`/`let`/`var` — **Holds “prev Edit” for this scope.**
- **Line 77:** `step1` — script-level `const`/`let`/`var` — **Holds “step1” for this scope.**
- **Line 78:** `step2` — script-level `const`/`let`/`var` — **Holds “step2” for this scope.**
- **Line 79:** `stepLine` — script-level `const`/`let`/`var` — **Holds “step Line” for this scope.**
- **Line 118:** `name` — script-level `const`/`let`/`var` — **Display name of user/course/criterion.**
- **Line 119:** `desc` — script-level `const`/`let`/`var` — **Description text (may embed <<<META>>> JSON).**
- **Line 120:** `category` — script-level `const`/`let`/`var` — **Holds “category” for this scope.**
- **Line 121:** `level` — script-level `const`/`let`/`var` — **Holds “level” for this scope.**
- **Line 122:** `bgImg` — script-level `const`/`let`/`var` — **Holds “bg Img” for this scope.**
- **Line 123:** `errDiv` — script-level `const`/`let`/`var` — **Holds “err Div” for this scope.**
- **Line 162:** `modalEl` — script-level `const`/`let`/`var` — **Holds “modal El” for this scope.**
- **Line 163:** `modal` — script-level `const`/`let`/`var` — **Holds “modal” for this scope.**

## Functions / methods (7 found)

### `showCreateCourseModal` — lines 2–26

```javascript
function showCreateCourseModal()
```

#### Explanation

- **Purpose:** Implements `showCreateCourseModal`.
- **Local variables (what each means):**
- `prev` — Holds “prev” for this scope.  DOM element from the page.
- `dzMsg` — Holds “dz Msg” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L9:** Get HTML element by id.
- **L10:** Get HTML element by id.
- **L11:** Get HTML element by id.
- **L12:** Get HTML element by id.
- **L13:** Get HTML element by id.
- **L14:** Get HTML element by id. | `prev` means: Holds “prev” for this scope.  DOM element from the page.
- **L16:** Get HTML element by id. | `dzMsg` means: Holds “dz Msg” for this scope.  DOM element from the page.
- **L17:** Update page HTML.
- **L19:** Get HTML element by id.
- **L21:** Get HTML element by id.

---

### `editCourseBasicInfo` — lines 50–73

```javascript
function editCourseBasicInfo(cid)
```

#### Explanation

- **Purpose:** Implements `editCourseBasicInfo`.
- **Parameters (what each means):**
- `cid` — Course ID (Courses.CID).
- **Local variables (what each means):**
- `c` — Course object/row.
- `prevEdit` — Holds “prev Edit” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L53:** `c` means: Course object/row.
- **L57:** Get HTML element by id.
- **L58:** Get HTML element by id.
- **L59:** Get HTML element by id.
- **L60:** Get HTML element by id.
- **L61:** Get HTML element by id.
- **L62:** Get HTML element by id. | `prevEdit` means: Holds “prev Edit” for this scope.  DOM element from the page.
- **L68:** Get HTML element by id.
- **L69:** Get HTML element by id.

---

### `setWizardStep` — lines 73–114

```javascript
function setWizardStep(step)
```

#### Explanation

- **Purpose:** Implements `setWizardStep`.
- **Pattern:** Persist changes.
- **Parameters (what each means):**
- `step` — TOTP 30-second time step counter.
- **Local variables (what each means):**
- `step1` — Holds “step1” for this scope.  DOM element from the page.
- `step2` — Holds “step2” for this scope.  DOM element from the page.
- `stepLine` — Holds “step Line” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L77:** Get HTML element by id. | `step1` means: Holds “step1” for this scope.  DOM element from the page.
- **L78:** Get HTML element by id. | `step2` means: Holds “step2” for this scope.  DOM element from the page.
- **L79:** Get HTML element by id. | `stepLine` means: Holds “step Line” for this scope.  DOM element from the page.
- **L90:** Get HTML element by id.
- **L91:** Get HTML element by id.
- **L94:** Get HTML element by id.
- **L95:** Get HTML element by id.
- **L104:** Get HTML element by id.
- **L105:** Get HTML element by id.
- **L108:** Get HTML element by id.
- **L109:** Get HTML element by id.

---

### `nextWizardStep` — lines 114–155

```javascript
function nextWizardStep()
```

#### Explanation

- **Purpose:** Implements `nextWizardStep`.
- **JSON:** Serializes/deserializes UI or META payloads.
- **Local variables (what each means):**
- `name` — Display name of user/course/criterion.  DOM element from the page.
- `desc` — Description text (may embed <<<META>>> JSON).  DOM element from the page.
- `category` — Holds “category” for this scope.  DOM element from the page.
- `level` — Holds “level” for this scope.  DOM element from the page.
- `bgImg` — Holds “bg Img” for this scope.  DOM element from the page.
- `errDiv` — Holds “err Div” for this scope.  DOM element from the page.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L118:** Get HTML element by id. | `name` means: Display name of user/course/criterion.  DOM element from the page.
- **L119:** Get HTML element by id. | `desc` means: Description text (may embed <<<META>>> JSON).  DOM element from the page.
- **L120:** Get HTML element by id. | `category` means: Holds “category” for this scope.  DOM element from the page.
- **L121:** Get HTML element by id. | `level` means: Holds “level” for this scope.  DOM element from the page.
- **L122:** Get HTML element by id. | `bgImg` means: Holds “bg Img” for this scope.  DOM element from the page.
- **L123:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.

---

### `prevWizardStep` — lines 155–159

```javascript
function prevWizardStep()
```

#### Explanation

- **Purpose:** Implements `prevWizardStep`.

#### Line-by-line (this function)

```javascript
 155 | 
 156 | 
 157 | function prevWizardStep() {
 158 |     setWizardStep(1);
 159 | }
```

---

### `completeWizard` — lines 159–166

```javascript
function completeWizard()
```

#### Explanation

- **Purpose:** Implements `completeWizard`.
- **Local variables (what each means):**
- `modalEl` — Holds “modal El” for this scope.  DOM element from the page.
- `modal` — Holds “modal” for this scope.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L162:** Get HTML element by id. | `modalEl` means: Holds “modal El” for this scope.  DOM element from the page.
- **L163:** `modal` means: Holds “modal” for this scope.

---

### `confirmCloseWizard` — lines 166–171

```javascript
function confirmCloseWizard(e)
```

#### Explanation

- **Purpose:** Implements `confirmCloseWizard`.
- **Parameters (what each means):**
- `e` — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

```javascript
 166 | 
 167 | 
 168 | function confirmCloseWizard(e) {
 169 |     // Reload courses in case they cancelled early on step 2 (curriculum changes are saved incrementally)
 170 |     loadCourses();
 171 | }
```

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L9:** Get HTML element by id.
- **L10:** Get HTML element by id.
- **L11:** Get HTML element by id.
- **L12:** Get HTML element by id.
- **L13:** Get HTML element by id.
- **L14:** Get HTML element by id. | `prev` means: Holds “prev” for this scope.  DOM element from the page.
- **L16:** Get HTML element by id. | `dzMsg` means: Holds “dz Msg” for this scope.  DOM element from the page.
- **L17:** Update page HTML.
- **L19:** Get HTML element by id.
- **L21:** Get HTML element by id.
- **L29:** DOM event handler.
- **L30:** Error handling block.
- **L31:** `params` means: Often a collection related to params (plural name).  Newly constructed object.
- **L32:** `editId` means: Identifier (`editId`) — database primary/foreign key.
- **L36:** `tries` means: Often a collection related to tries (plural name).  Literal number `0`.
- **L37:** `t` means: Temporary string/token/time value.
- **L53:** `c` means: Course object/row.
- **L57:** Get HTML element by id.
- **L58:** Get HTML element by id.
- **L59:** Get HTML element by id.
- **L60:** Get HTML element by id.
- **L61:** Get HTML element by id.
- **L62:** Get HTML element by id. | `prevEdit` means: Holds “prev Edit” for this scope.  DOM element from the page.
- **L68:** Get HTML element by id.
- **L69:** Get HTML element by id.
- **L77:** Get HTML element by id. | `step1` means: Holds “step1” for this scope.  DOM element from the page.
- **L78:** Get HTML element by id. | `step2` means: Holds “step2” for this scope.  DOM element from the page.
- **L79:** Get HTML element by id. | `stepLine` means: Holds “step Line” for this scope.  DOM element from the page.
- **L90:** Get HTML element by id.
- **L91:** Get HTML element by id.
- **L94:** Get HTML element by id.
- **L95:** Get HTML element by id.
- **L104:** Get HTML element by id.
- **L105:** Get HTML element by id.
- **L108:** Get HTML element by id.
- **L109:** Get HTML element by id.
- **L118:** Get HTML element by id. | `name` means: Display name of user/course/criterion.  DOM element from the page.
- **L119:** Get HTML element by id. | `desc` means: Description text (may embed <<<META>>> JSON).  DOM element from the page.
- **L120:** Get HTML element by id. | `category` means: Holds “category” for this scope.  DOM element from the page.
- **L121:** Get HTML element by id. | `level` means: Holds “level” for this scope.  DOM element from the page.
- **L122:** Get HTML element by id. | `bgImg` means: Holds “bg Img” for this scope.  DOM element from the page.
- **L123:** Get HTML element by id. | `errDiv` means: Holds “err Div” for this scope.  DOM element from the page.
- **L162:** Get HTML element by id. | `modalEl` means: Holds “modal El” for this scope.  DOM element from the page.
- **L163:** `modal` means: Holds “modal” for this scope.

## Source snapshot (raw)

```javascript
// Course Creation — wizard create/edit course
// depends on: cc-core.js, cc-grid.js
function showCreateCourseModal() {
    currentCourseId = null;
    editingSectionId = null;
    editingLessonId = null;

    // Reset form fields
    document.getElementById('txtCourseTitle').value = '';
    document.getElementById('txtCourseDesc').value = '';
    document.getElementById('ddlCategory').value = 'Development';
    document.getElementById('ddlLevel').value = 'Beginner';
    document.getElementById('txtBgImg').value = '';
    const prev = document.getElementById('courseThumbPreview');
    if (prev) { prev.src = ''; prev.classList.add('d-none'); }
    const dzMsg = document.getElementById('dzMessage');
    if (dzMsg) dzMsg.innerHTML = '<i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>Click to upload image (16:9 ratio)';

    document.getElementById('step1Error').style.display = 'none';

    document.getElementById('wizardModalTitle').innerText = "Create New Course";

    setWizardStep(1);

    showModal('courseWizardModal');
}

// Deep-link: CourseCreation.aspx?edit=123 (from preview Edit button)
document.addEventListener('DOMContentLoaded', function () {
    try {
        var params = new URLSearchParams(window.location.search);
        var editId = parseInt(params.get('edit') || sessionStorage.getItem('editCourseId') || '0', 10);
        if (editId > 0) {
            sessionStorage.removeItem('editCourseId');
            // Wait for courses to load then open editor
            var tries = 0;
            var t = setInterval(function () {
                tries++;
                if (courses && courses.length) {
                    clearInterval(t);
                    editCourseBasicInfo(editId);
                    // jump to curriculum step if already saved
                    if (currentCourseId) setTimeout(function () { setWizardStep(2); }, 200);
                } else if (tries > 40) {
                    clearInterval(t);
                }
            }, 100);
        }
    } catch (e) { /* ignore */ }
});

function editCourseBasicInfo(cid) {
    const c = courses.find(item => item.cid === cid);
    if (!c) return;

    currentCourseId = cid;
    document.getElementById('txtCourseTitle').value = c.name;
    document.getElementById('txtCourseDesc').value = c.description;
    if (c.category) document.getElementById('ddlCategory').value = c.category;
    if (c.level) document.getElementById('ddlLevel').value = c.level;
    document.getElementById('txtBgImg').value = c.bgImg || '';
    const prevEdit = document.getElementById('courseThumbPreview');
    if (prevEdit && c.bgImg) {
        prevEdit.src = c.bgImg;
        prevEdit.classList.remove('d-none');
    }

    document.getElementById('step1Error').style.display = 'none';
    document.getElementById('wizardModalTitle').innerText = 'Edit Course: ' + c.name;

    setWizardStep(1);
    showModal('courseWizardModal');
}

function setWizardStep(step) {
    activeWizardStep = step;
    const step1 = document.getElementById('stepIndicator1');
    const step2 = document.getElementById('stepIndicator2');
    const stepLine = document.getElementById('stepLine1');

    if (step === 1) {
        // Indicators
        step1.classList.remove('completed');
        step1.classList.add('active');
        step2.classList.remove('active');
        step2.classList.remove('completed');
        stepLine.classList.remove('active');

        // Form panels
        document.getElementById('wizardStep1').style.display = 'block';
        document.getElementById('wizardStep2').style.display = 'none';

        // Footers
        document.getElementById('wizardFooterStep1').style.display = 'flex';
        document.getElementById('wizardFooterStep2').style.setProperty('display', 'none', 'important');
    } else {
        // Indicators
        step1.classList.remove('active');
        step1.classList.add('completed');
        step2.classList.add('active');
        stepLine.classList.add('active');

        // Form panels
        document.getElementById('wizardStep1').style.display = 'none';
        document.getElementById('wizardStep2').style.display = 'block';

        // Footers
        document.getElementById('wizardFooterStep1').style.setProperty('display', 'none', 'important');
        document.getElementById('wizardFooterStep2').style.setProperty('display', 'flex', 'important');

        // Load Curriculum
        loadCurriculumView();
    }
}


function nextWizardStep() {
    const name = document.getElementById('txtCourseTitle').value.trim();
    const desc = document.getElementById('txtCourseDesc').value.trim();
    const category = document.getElementById('ddlCategory').value;
    const level = document.getElementById('ddlLevel').value;
    const bgImg = document.getElementById('txtBgImg').value.trim();
    const errDiv = document.getElementById('step1Error');

    errDiv.style.display = 'none';

    if (!name || !desc) {
        errDiv.innerText = "Please fill in all required fields (Title and Description).";
        errDiv.style.display = 'block';
        return;
    }

    postJson('CourseCreation.aspx/SaveCourseInfo', {
        name: name,
        desc: desc,
        category: category,
        level: level,
        bgImg: bgImg,
        cid: currentCourseId || 0
    })
    .then(function (resObj) {
        if (resObj && resObj.success) {
            currentCourseId = resObj.cid;
            setWizardStep(2);
        } else {
            errDiv.innerText = (resObj && resObj.message) || 'Failed to save course details.';
            errDiv.style.display = 'block';
        }
    })
    .catch(function (err) {
        errDiv.innerText = 'Network error saving course.';
        errDiv.style.display = 'block';
        console.error(err);
    });
}

function prevWizardStep() {
    setWizardStep(1);
}

function completeWizard() {
    const modalEl = document.getElementById('courseWizardModal');
    const modal = bootstrap.Modal.getInstance(modalEl);
    modal.hide();
    loadCourses(); // Refresh list
}

function confirmCloseWizard(e) {
    // Reload courses in case they cancelled early on step 2 (curriculum changes are saved incrementally)
    loadCourses();
}


```
