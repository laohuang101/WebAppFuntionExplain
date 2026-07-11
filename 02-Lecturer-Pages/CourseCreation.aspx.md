# CourseCreation.aspx
**Source:** `Pages/Lecturer/CourseCreation.aspx`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Create/edit courses, curriculum (chapters/lessons), media, publish/draft.

## File overview

- **Total lines:** 258
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `<%@ Page Title="Course Manager" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="CourseCreation.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Course_Creation" %>`
`   2`  ``
`   3`  `<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">`
`   4`  `  <link rel="stylesheet" href="Style/course-creation.css" />`
`   5`  `</asp:Content>`
`   6`  ``
`   7`  `<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">`
`   8`  `  <div class="course-manager-container container-fluid px-0">`
`   9`  `    <!-- Page Header -->`
`  10`  `    <div class="d-flex justify-content-between align-items-center mb-4">`
`  11`  `      <div>`
`  12`  `        <h3 class="fw-bold text-dark mb-1">Course Manager</h3>`
`  13`  `        <p class="text-muted small mb-0">Manage your existing courses or create new ones.</p>`
`  14`  `      </div>`
`  15`  `      <button type="button" class="btn-pill-accent d-flex align-items-center gap-2" onclick="showCreateCourseModal()">`
`  16`  `        <i class="fa-solid fa-plus"></i> Create Course`
`  17`  `      </button>`
`  18`  `    </div>`
`  19`  ``
`  20`  `    <!-- Course Cards Grid -->`
`  21`  `    <div class="row g-4" id="courseGridContainer">`
`  22`  `      <!-- Dynamically populated via JS -->`
`  23`  `      <div class="col-12 text-center py-5">`
`  24`  `        <i class="fa-solid fa-circle-notch fa-spin fa-2x me-2 text-muted"></i>`
`  25`  `        <p class="text-muted mt-2">Loading courses...</p>`
`  26`  `      </div>`
`  27`  `    </div>`
`  28`  `  </div>`
`  29`  ``
`  30`  `  <!-- MAIN COURSE CREATION / EDITING WIZARD MODAL -->`
`  31`  `  <div class="modal fade" id="courseWizardModal" data-bs-backdrop="static" tabindex="-1" aria-hidden="true">`
`  32`  `    <div class="modal-dialog modal-lg modal-dialog-centered">`
`  33`  `      <div class="modal-content modal-glass border-0">`
`  34`  `        <div class="modal-header border-bottom border-light">`
`  35`  `          <h5 class="modal-title fw-bold text-dark" id="wizardModalTitle">Create New Course</h5>`
`  36`  `          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" onclick="confirmCloseWizard(event)"></button>`
`  37`  `        </div>`
`  38`  `        <div class="modal-body p-4">`
`  39`  `          <!-- Progress Steps Header -->`
`  40`  `          <div class="wizard-steps">`
`  41`  `            <div class="wizard-step" id="stepIndicator1" role="button" aria-controls="wizardStep1">`
`  42`  `              <div class="step-circle">1</div>`
`  43`  `              <span class="step-label">Basic Info</span>`
`  44`  `            </div>`
`  45`  ``
`  46`  `            <div class="step-line" id="stepLine1" aria-hidden="true">`
`  47`  `              <div class="step-fill"></div>`
`  48`  `            </div>`
`  49`  ``
`  50`  `            <div class="wizard-step" id="stepIndicator2" role="button" aria-controls="wizardStep2">`
`  51`  `              <div class="step-circle">2</div>`
`  52`  `              <span class="step-label">Curriculum</span>`
`  53`  `            </div>`
`  54`  `          </div>`
`  55`  ``
`  56`  `          <!-- STEP 1: Basic Info Form -->`
`  57`  `          <div id="wizardStep1">`
`  58`  `            <div class="mb-3">`
`  59`  `              <label class="form-label text-muted small fw-bold">Course Title</label>`
`  60`  `              <input type="text" id="txtCourseTitle" class="form-control" placeholder="e.g., Human Computer Interaction" required />`
`  61`  `            </div>`
`  62`  ``
`  63`  `            <div class="mb-3">`
`  64`  `              <label class="form-label text-muted small fw-bold">Description</label>`
`  65`  `              <textarea id="txtCourseDesc" class="form-control" rows="3" placeholder="Describe what students will learn..." required></textarea>`
`  66`  `            </div>`
`  67`  ``
`  68`  `            <div class="row g-3 mb-3">`
`  69`  `              <div class="col-md-6">`
`  70`  `                <label class="form-label text-muted small fw-bold">Category</label>`
`  71`  `                <select id="ddlCategory" class="form-select text-uppercase">`
`  72`  `                  <option value="Development">Development</option>`
`  73`  `                  <option value="Design">Design</option>`
`  74`  `                  <option value="Business">Business</option>`
`  75`  `                  <option value="Others">Others</option>`
`  76`  `                </select>`
`  77`  `              </div>`
`  78`  `              <div class="col-md-6">`
`  79`  `                <label class="form-label text-muted small fw-bold">Level</label>`
`  80`  `                <select id="ddlLevel" class="form-select text-uppercase">`
`  81`  `                  <option value="Beginner">Beginner</option>`
`  82`  `                  <option value="Intermediate">Intermediate</option>`
`  83`  `                  <option value="Advanced">Advanced</option>`
`  84`  `                </select>`
`  85`  `              </div>`
`  86`  `            </div>`
`  87`  ``
`  88`  `            <div class="mb-3">`
`  89`  `              <label class="form-label text-muted small fw-bold">Course Thumbnail</label>`
`  90`  `              <div id="dropzoneArea" class="dropzone-styled text-center py-4" style="cursor:pointer;">`
`  91`  `                <img id="courseThumbPreview" src="" class="course-banner-img mb-2 d-none" style="max-height:120px;width:auto;object-fit:cover;border-radius:8px;margin:0 auto;" />`
`  92`  `                <div id="dzMessage" class="text-muted small">`
`  93`  `                  <i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>`
`  94`  `                  Click to upload image (16:9 ratio)`
`  95`  `                </div>`
`  96`  `              </div>`
`  97`  `              <input type="hidden" id="txtBgImg" />`
`  98`  `            </div>`
`  99`  ``
` 100`  `            <div id="step1Error" class="text-danger small mb-3" style="display:none;"></div>`
` 101`  `          </div>`
` 102`  ``
` 103`  `          <!-- STEP 2: Curriculum Structure -->`
` 104`  `          <div id="wizardStep2" style="display: none;">`
` 105`  `            <h6 class="fw-bold mb-3 text-dark">Course Curriculum Sections</h6>`
` 106`  ``
` 107`  `            <div class="curriculum-container mb-3" id="curriculumView">`
` 108`  `              <!-- Populated dynamically -->`
` 109`  `              <div class="text-center py-4 text-muted">`
` 110`  `                No sections added yet. Click "+ Add New Section" to start building your course.`
` 111`  `              </div>`
` 112`  `            </div>`
` 113`  ``
` 114`  `            <button type="button" class="btn-add-section d-flex align-items-center justify-content-center gap-2 mb-3" onclick="showAddSectionModal()">`
` 115`  `              <i class="fa-solid fa-plus"></i> Add New Section`
` 116`  `            </button>`
` 117`  `          </div>`
` 118`  `        </div>`
` 119`  `        <div class="modal-footer border-top border-light">`
` 120`  `          <!-- Step 1 Footer Buttons -->`
` 121`  `          <div id="wizardFooterStep1" class="d-flex justify-content-end gap-2 w-100">`
` 122`  `            <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>`
` 123`  `            <button type="button" class="btn btn-pill-accent" onclick="nextWizardStep()">Next Step</button>`
` 124`  `          </div>`
` 125`  `          <!-- Step 2 Footer Buttons -->`
` 126`  `          <div id="wizardFooterStep2" class="d-flex justify-content-between w-100" style="display: none !important;">`
` 127`  `            <button type="button" class="btn btn-light rounded-pill px-4" onclick="prevWizardStep()">Back</button>`
` 128`  `            <button type="button" class="btn btn-pill-accent" onclick="completeWizard()">Complete Course</button>`
` 129`  `          </div>`
` 130`  `        </div>`
` 131`  `      </div>`
` 132`  `    </div>`
` 133`  `  </div>`
` 134`  ``
` 135`  `  <!-- SUB-MODAL 1: ADD/EDIT SECTION (CHAPTER) - stacked above wizard -->`
` 136`  `  <div class="modal fade nested-modal" id="sectionModal" tabindex="-1" aria-hidden="true" data-bs-backdrop="static">`
` 137`  `    <div class="modal-dialog modal-dialog-centered">`
` 138`  `      <div class="modal-content modal-glass border-0 shadow-lg">`
` 139`  `        <div class="modal-header border-bottom border-light">`
` 140`  `          <h5 class="modal-title fw-bold text-dark" id="sectionModalTitle">Add New Section</h5>`
` 141`  `          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>`
` 142`  `        </div>`
` 143`  `        <div class="modal-body p-4">`
` 144`  `          <div class="mb-3">`
` 145`  `            <label class="form-label text-muted small fw-bold">Section Title</label>`
` 146`  `            <input type="text" id="txtSectionTitle" class="form-control" placeholder="e.g., Section 1: Introduction" required />`
` 147`  `          </div>`
` 148`  `          <div id="sectionModalError" class="text-danger small" style="display:none;"></div>`
` 149`  `        </div>`
` 150`  `        <div class="modal-footer border-top border-light">`
` 151`  `          <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>`
` 152`  `          <button type="button" class="btn btn-pill-accent" onclick="saveSection()">Save Section</button>`
` 153`  `        </div>`
` 154`  `      </div>`
` 155`  `    </div>`
` 156`  `  </div>`
` 157`  ``
` 158`  `  <!-- SUB-MODAL 2: ADD/EDIT LESSON (SUBCHAPTER) -->`
` 159`  `  <div class="modal fade nested-modal" id="lessonModal" tabindex="-1" aria-hidden="true" data-bs-backdrop="static">`
` 160`  `    <div class="modal-dialog modal-dialog-centered">`
` 161`  `      <div class="modal-content modal-glass border-0 shadow-lg">`
` 162`  `        <div class="modal-header border-bottom border-light">`
` 163`  `          <h5 class="modal-title fw-bold text-dark" id="lessonModalTitle">Add New Lesson</h5>`
` 164`  `          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>`
` 165`  `        </div>`
` 166`  `        <div class="modal-body p-4">`
` 167`  `          <div class="mb-3">`
` 168`  `            <label class="form-label text-muted small fw-bold">Lesson Title</label>`
` 169`  `            <input type="text" id="txtLessonTitle" class="form-control" placeholder="e.g., Figma Basics" required />`
` 170`  `          </div>`
` 171`  ``
` 172`  `          <div class="mb-3">`
` 173`  `            <label class="form-label text-muted small fw-bold">Lesson Type</label>`
` 174`  `            <select id="ddlLessonType" class="form-select" onchange="toggleLessonContentFields()">`
` 175`  `              <option value="Text">Text Content</option>`
` 176`  `              <option value="Video">Video Link</option>`
` 177`  `              <option value="Quiz">Quiz / Assignment Question</option>`
` 178`  `            </select>`
` 179`  `          </div>`
` 180`  ``
` 181`  `          <div class="mb-3" id="lessonContentField">`
` 182`  `            <label class="form-label text-muted small fw-bold" id="lblLessonContent">Content Body</label>`
` 183`  ``
` 184`  `            <!-- Editor toolbar -->`
` 185`  `            <div class="editor-toolbar mb-2" id="editorToolbar" role="toolbar" aria-label="Editor toolbar">`
` 186`  `              <button type="button" class="btn btn-sm btn-light" data-cmd="bold" title="Bold"><i class="fa-solid fa-bold"></i></button>`
` 187`  `              <button type="button" class="btn btn-sm btn-light" data-cmd="italic" title="Italic"><i class="fa-solid fa-italic"></i></button>`
` 188`  `              <button type="button" class="btn btn-sm btn-light" data-cmd="insertUnorderedList" title="Bullet list"><i class="fa-solid fa-list-ul"></i></button>`
` 189`  `              <button type="button" class="btn btn-sm btn-light" data-cmd="insertOrderedList" title="Numbered list"><i class="fa-solid fa-list-ol"></i></button>`
` 190`  `              <button type="button" class="btn btn-sm btn-light" data-cmd="createLink" title="Insert link"><i class="fa-solid fa-link"></i></button>`
` 191`  `              <button type="button" class="btn btn-sm btn-light" data-cmd="unlink" title="Remove link"><i class="fa-solid fa-unlink"></i></button>`
` 192`  `            </div>`
` 193`  ``
` 194`  `            <!-- Rich text editor for text lessons -->`
` 195`  `            <div id="htmlEditor" contenteditable="true" class="form-control editor-content" style="min-height:140px; overflow:auto;"></div>`
` 196`  ``
` 197`  `            <!-- Fallback plain textarea (kept hidden for compatibility) -->`
` 198`  `            <textarea id="txtLessonContent" class="form-control d-none" rows="4" placeholder="Enter lesson text content here..."></textarea>`
` 199`  ``
` 200`  `            <!-- Media dropzone (video) -->`
` 201`  `            <div id="mediaDropzone" class="dropzone-styled mb-2" style="display:none;cursor:pointer;">`
` 202`  `              <div class="dz-inner text-muted small text-center py-3">`
` 203`  `                <i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>`
` 204`  `                Click or drag a video here (mp4 / webm / mov, up to 200MB)`
` 205`  `              </div>`
` 206`  `              <input type="file" id="mediaFileInput" accept="video/*,.mp4,.webm,.mov" style="display:none;" />`
` 207`  `              <div id="lessonMediaPreview" class="d-none mt-2"></div>`
` 208`  `            </div>`
` 209`  ``
` 210`  `            <!-- Materials dropzone (PDF, Office, images, video) -->`
` 211`  `            <div id="materialDropzone" class="dropzone-styled mb-2" style="display:none;cursor:pointer;">`
` 212`  `              <div class="dz-inner text-muted small text-center py-3">`
` 213`  `                <i class="fa-solid fa-file-arrow-up d-block mb-2 fs-4"></i>`
` 214`  `                Click or drag materials (PDF, PPTX, DOCX, images, video - preview and download after upload)`
` 215`  `              </div>`
` 216`  `              <input type="file" id="materialFileInput" accept=".pdf,.ppt,.pptx,.docx,.doc,image/*,video/*,.mp4,.webm,.mov" style="display:none;" />`
` 217`  `            </div>`
` 218`  ``
` 219`  `            <!-- Attachments / materials list with inline preview -->`
` 220`  `            <div id="lessonAttachments" class="mt-2"></div>`
` 221`  ``
` 222`  `            <!-- Hidden field to store materials metadata as JSON -->`
` 223`  `            <input type="hidden" id="lessonMaterials" value="[]" />`
` 224`  `          </div>`
` 225`  ``
` 226`  `          <div id="lessonModalError" class="text-danger small" style="display:none;"></div>`
` 227`  `        </div>`
` 228`  `        <div class="modal-footer border-top border-light">`
` 229`  `          <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>`
` 230`  `          <button type="button" class="btn btn-pill-accent" onclick="saveLesson()">Save Lesson</button>`
` 231`  `        </div>`
` 232`  `      </div>`
` 233`  `    </div>`
` 234`  `  </div>`
` 235`  ``
` 236`  `  <!-- Course manager modules (order matters) -->`
` 237`  `  <script src="Scripts/uploader.js"></script>`
` 238`  `  <script src="Scripts/editor.js"></script>`
` 239`  `  <script src="Scripts/wizard.js"></script>`
` 240`  `  <script src="Scripts/dropdowns.js"></script>`
` 241`  `  <script src="Scripts/cc-core.js"></script>`
` 242`  `  <script src="Scripts/cc-media.js"></script>`
` 243`  `  <script src="Scripts/cc-grid.js"></script>`
` 244`  `  <script src="Scripts/cc-wizard.js"></script>`
` 245`  `  <script src="Scripts/cc-curriculum.js"></script>`
` 246`  `  <script src="course-creation.js"></script>`
` 247`  `  <script>`
` 248`  `    document.addEventListener('DOMContentLoaded', function () {`
  - → DOM event handler.
` 249`  `      if (typeof initDropdowns === 'function') initDropdowns();`
` 250`  `      if (typeof initDropzone === 'function') initDropzone();`
` 251`  `      if (typeof initMediaDropzone === 'function') initMediaDropzone();`
` 252`  `      if (typeof initMaterialDropzone === 'function') initMaterialDropzone();`
` 253`  `      if (typeof initEditor === 'function') initEditor();`
` 254`  `      if (typeof initWizardControls === 'function') initWizardControls();`
` 255`  `      if (typeof loadCourses === 'function') loadCourses();`
` 256`  `    });`
` 257`  `  </script>`
` 258`  `</asp:Content>`

## Source snapshot (raw)

```html
<%@ Page Title="Course Manager" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="CourseCreation.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Course_Creation" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
  <link rel="stylesheet" href="Style/course-creation.css" />
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
  <div class="course-manager-container container-fluid px-0">
    <!-- Page Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h3 class="fw-bold text-dark mb-1">Course Manager</h3>
        <p class="text-muted small mb-0">Manage your existing courses or create new ones.</p>
      </div>
      <button type="button" class="btn-pill-accent d-flex align-items-center gap-2" onclick="showCreateCourseModal()">
        <i class="fa-solid fa-plus"></i> Create Course
      </button>
    </div>

    <!-- Course Cards Grid -->
    <div class="row g-4" id="courseGridContainer">
      <!-- Dynamically populated via JS -->
      <div class="col-12 text-center py-5">
        <i class="fa-solid fa-circle-notch fa-spin fa-2x me-2 text-muted"></i>
        <p class="text-muted mt-2">Loading courses...</p>
      </div>
    </div>
  </div>

  <!-- MAIN COURSE CREATION / EDITING WIZARD MODAL -->
  <div class="modal fade" id="courseWizardModal" data-bs-backdrop="static" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content modal-glass border-0">
        <div class="modal-header border-bottom border-light">
          <h5 class="modal-title fw-bold text-dark" id="wizardModalTitle">Create New Course</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" onclick="confirmCloseWizard(event)"></button>
        </div>
        <div class="modal-body p-4">
          <!-- Progress Steps Header -->
          <div class="wizard-steps">
            <div class="wizard-step" id="stepIndicator1" role="button" aria-controls="wizardStep1">
              <div class="step-circle">1</div>
              <span class="step-label">Basic Info</span>
            </div>

            <div class="step-line" id="stepLine1" aria-hidden="true">
              <div class="step-fill"></div>
            </div>

            <div class="wizard-step" id="stepIndicator2" role="button" aria-controls="wizardStep2">
              <div class="step-circle">2</div>
              <span class="step-label">Curriculum</span>
            </div>
          </div>

          <!-- STEP 1: Basic Info Form -->
          <div id="wizardStep1">
            <div class="mb-3">
              <label class="form-label text-muted small fw-bold">Course Title</label>
              <input type="text" id="txtCourseTitle" class="form-control" placeholder="e.g., Human Computer Interaction" required />
            </div>

            <div class="mb-3">
              <label class="form-label text-muted small fw-bold">Description</label>
              <textarea id="txtCourseDesc" class="form-control" rows="3" placeholder="Describe what students will learn..." required></textarea>
            </div>

            <div class="row g-3 mb-3">
              <div class="col-md-6">
                <label class="form-label text-muted small fw-bold">Category</label>
                <select id="ddlCategory" class="form-select text-uppercase">
                  <option value="Development">Development</option>
                  <option value="Design">Design</option>
                  <option value="Business">Business</option>
                  <option value="Others">Others</option>
                </select>
              </div>
              <div class="col-md-6">
                <label class="form-label text-muted small fw-bold">Level</label>
                <select id="ddlLevel" class="form-select text-uppercase">
                  <option value="Beginner">Beginner</option>
                  <option value="Intermediate">Intermediate</option>
                  <option value="Advanced">Advanced</option>
                </select>
              </div>
            </div>

            <div class="mb-3">
              <label class="form-label text-muted small fw-bold">Course Thumbnail</label>
              <div id="dropzoneArea" class="dropzone-styled text-center py-4" style="cursor:pointer;">
                <img id="courseThumbPreview" src="" class="course-banner-img mb-2 d-none" style="max-height:120px;width:auto;object-fit:cover;border-radius:8px;margin:0 auto;" />
                <div id="dzMessage" class="text-muted small">
                  <i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>
                  Click to upload image (16:9 ratio)
                </div>
              </div>
              <input type="hidden" id="txtBgImg" />
            </div>

            <div id="step1Error" class="text-danger small mb-3" style="display:none;"></div>
          </div>

          <!-- STEP 2: Curriculum Structure -->
          <div id="wizardStep2" style="display: none;">
            <h6 class="fw-bold mb-3 text-dark">Course Curriculum Sections</h6>

            <div class="curriculum-container mb-3" id="curriculumView">
              <!-- Populated dynamically -->
              <div class="text-center py-4 text-muted">
                No sections added yet. Click "+ Add New Section" to start building your course.
              </div>
            </div>

            <button type="button" class="btn-add-section d-flex align-items-center justify-content-center gap-2 mb-3" onclick="showAddSectionModal()">
              <i class="fa-solid fa-plus"></i> Add New Section
            </button>
          </div>
        </div>
        <div class="modal-footer border-top border-light">
          <!-- Step 1 Footer Buttons -->
          <div id="wizardFooterStep1" class="d-flex justify-content-end gap-2 w-100">
            <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-pill-accent" onclick="nextWizardStep()">Next Step</button>
          </div>
          <!-- Step 2 Footer Buttons -->
          <div id="wizardFooterStep2" class="d-flex justify-content-between w-100" style="display: none !important;">
            <button type="button" class="btn btn-light rounded-pill px-4" onclick="prevWizardStep()">Back</button>
            <button type="button" class="btn btn-pill-accent" onclick="completeWizard()">Complete Course</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- SUB-MODAL 1: ADD/EDIT SECTION (CHAPTER) - stacked above wizard -->
  <div class="modal fade nested-modal" id="sectionModal" tabindex="-1" aria-hidden="true" data-bs-backdrop="static">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content modal-glass border-0 shadow-lg">
        <div class="modal-header border-bottom border-light">
          <h5 class="modal-title fw-bold text-dark" id="sectionModalTitle">Add New Section</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body p-4">
          <div class="mb-3">
            <label class="form-label text-muted small fw-bold">Section Title</label>
            <input type="text" id="txtSectionTitle" class="form-control" placeholder="e.g., Section 1: Introduction" required />
          </div>
          <div id="sectionModalError" class="text-danger small" style="display:none;"></div>
        </div>
        <div class="modal-footer border-top border-light">
          <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-pill-accent" onclick="saveSection()">Save Section</button>
        </div>
      </div>
    </div>
  </div>

  <!-- SUB-MODAL 2: ADD/EDIT LESSON (SUBCHAPTER) -->
  <div class="modal fade nested-modal" id="lessonModal" tabindex="-1" aria-hidden="true" data-bs-backdrop="static">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content modal-glass border-0 shadow-lg">
        <div class="modal-header border-bottom border-light">
          <h5 class="modal-title fw-bold text-dark" id="lessonModalTitle">Add New Lesson</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body p-4">
          <div class="mb-3">
            <label class="form-label text-muted small fw-bold">Lesson Title</label>
            <input type="text" id="txtLessonTitle" class="form-control" placeholder="e.g., Figma Basics" required />
          </div>

          <div class="mb-3">
            <label class="form-label text-muted small fw-bold">Lesson Type</label>
            <select id="ddlLessonType" class="form-select" onchange="toggleLessonContentFields()">
              <option value="Text">Text Content</option>
              <option value="Video">Video Link</option>
              <option value="Quiz">Quiz / Assignment Question</option>
            </select>
          </div>

          <div class="mb-3" id="lessonContentField">
            <label class="form-label text-muted small fw-bold" id="lblLessonContent">Content Body</label>

            <!-- Editor toolbar -->
            <div class="editor-toolbar mb-2" id="editorToolbar" role="toolbar" aria-label="Editor toolbar">
              <button type="button" class="btn btn-sm btn-light" data-cmd="bold" title="Bold"><i class="fa-solid fa-bold"></i></button>
              <button type="button" class="btn btn-sm btn-light" data-cmd="italic" title="Italic"><i class="fa-solid fa-italic"></i></button>
              <button type="button" class="btn btn-sm btn-light" data-cmd="insertUnorderedList" title="Bullet list"><i class="fa-solid fa-list-ul"></i></button>
              <button type="button" class="btn btn-sm btn-light" data-cmd="insertOrderedList" title="Numbered list"><i class="fa-solid fa-list-ol"></i></button>
              <button type="button" class="btn btn-sm btn-light" data-cmd="createLink" title="Insert link"><i class="fa-solid fa-link"></i></button>
              <button type="button" class="btn btn-sm btn-light" data-cmd="unlink" title="Remove link"><i class="fa-solid fa-unlink"></i></button>
            </div>

            <!-- Rich text editor for text lessons -->
            <div id="htmlEditor" contenteditable="true" class="form-control editor-content" style="min-height:140px; overflow:auto;"></div>

            <!-- Fallback plain textarea (kept hidden for compatibility) -->
            <textarea id="txtLessonContent" class="form-control d-none" rows="4" placeholder="Enter lesson text content here..."></textarea>

            <!-- Media dropzone (video) -->
            <div id="mediaDropzone" class="dropzone-styled mb-2" style="display:none;cursor:pointer;">
              <div class="dz-inner text-muted small text-center py-3">
                <i class="fa-solid fa-cloud-arrow-up d-block mb-2 fs-4"></i>
                Click or drag a video here (mp4 / webm / mov, up to 200MB)
              </div>
              <input type="file" id="mediaFileInput" accept="video/*,.mp4,.webm,.mov" style="display:none;" />
              <div id="lessonMediaPreview" class="d-none mt-2"></div>
            </div>

            <!-- Materials dropzone (PDF, Office, images, video) -->
            <div id="materialDropzone" class="dropzone-styled mb-2" style="display:none;cursor:pointer;">
              <div class="dz-inner text-muted small text-center py-3">
                <i class="fa-solid fa-file-arrow-up d-block mb-2 fs-4"></i>
                Click or drag materials (PDF, PPTX, DOCX, images, video - preview and download after upload)
              </div>
              <input type="file" id="materialFileInput" accept=".pdf,.ppt,.pptx,.docx,.doc,image/*,video/*,.mp4,.webm,.mov" style="display:none;" />
            </div>

            <!-- Attachments / materials list with inline preview -->
            <div id="lessonAttachments" class="mt-2"></div>

            <!-- Hidden field to store materials metadata as JSON -->
            <input type="hidden" id="lessonMaterials" value="[]" />
          </div>

          <div id="lessonModalError" class="text-danger small" style="display:none;"></div>
        </div>
        <div class="modal-footer border-top border-light">
          <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-pill-accent" onclick="saveLesson()">Save Lesson</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Course manager modules (order matters) -->
  <script src="Scripts/uploader.js"></script>
  <script src="Scripts/editor.js"></script>
  <script src="Scripts/wizard.js"></script>
  <script src="Scripts/dropdowns.js"></script>
  <script src="Scripts/cc-core.js"></script>
  <script src="Scripts/cc-media.js"></script>
  <script src="Scripts/cc-grid.js"></script>
  <script src="Scripts/cc-wizard.js"></script>
  <script src="Scripts/cc-curriculum.js"></script>
  <script src="course-creation.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      if (typeof initDropdowns === 'function') initDropdowns();
      if (typeof initDropzone === 'function') initDropzone();
      if (typeof initMediaDropzone === 'function') initMediaDropzone();
      if (typeof initMaterialDropzone === 'function') initMaterialDropzone();
      if (typeof initEditor === 'function') initEditor();
      if (typeof initWizardControls === 'function') initWizardControls();
      if (typeof loadCourses === 'function') loadCourses();
    });
  </script>
</asp:Content>

```
