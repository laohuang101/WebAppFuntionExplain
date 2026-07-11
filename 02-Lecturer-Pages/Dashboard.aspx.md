# Dashboard.aspx
**Source:** `Pages/Lecturer/Dashboard.aspx`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Lecturer home: course stats, recent submissions, charts. Backed by LecturerRepository.

## File overview

- **Total lines:** 166
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `<%@ Page Title="" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="Dashboard.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Dashboard" %>`
`   2`  `<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">`
`   3`  `  <link rel="stylesheet" href="Style/dashboard.css" />`
`   4`  `</asp:Content>`
`   5`  ``
`   6`  `<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">`
`   7`  `  <div class="dashboard-container container-fluid px-0">`
`   8`  `    <div class="d-flex flex-wrap justify-content-end gap-2 mb-3">`
`   9`  `      <a href="<%= ResolveUrl("~/Pages/Lecturer/Grading.aspx?filter=pending") %>" class="btn btn-sm btn-outline-warning rounded-pill px-3">`
`  10`  `        <i class="fa-solid fa-inbox me-1"></i> Grade pending`
`  11`  `      </a>`
`  12`  `      <button type="button" class="btn btn-sm btn-outline-dark rounded-pill px-3" onclick="exportDashGradesCsv()">`
  - → CSV export.
`  13`  `        <i class="fa-solid fa-file-csv me-1"></i> Export grades CSV`
  - → CSV export.
`  14`  `      </button>`
`  15`  `    </div>`
`  16`  `    <!-- Top Metrics Row -->`
`  17`  `    <div class="row g-4 mb-4">`
`  18`  `      <!-- Total Students -->`
`  19`  `      <div class="col-xl-3 col-md-6">`
`  20`  `        <div class="glass-card stat-card-1 p-3 d-flex align-items-center">`
`  21`  `          <div class="stat-icon stat-icon-1 me-3">`
`  22`  `            <i class="fa-solid fa-users"></i>`
`  23`  `          </div>`
`  24`  `          <div>`
`  25`  `            <div class="stat-value" id="lblTotalStudents">0</div>`
`  26`  `            <div class="stat-label">Total Students</div>`
`  27`  `          </div>`
`  28`  `        </div>`
`  29`  `      </div>`
`  30`  ``
`  31`  `      <!-- Active Courses -->`
`  32`  `      <div class="col-xl-3 col-md-6">`
`  33`  `        <div class="glass-card stat-card-2 p-3 d-flex align-items-center">`
`  34`  `          <div class="stat-icon stat-icon-2 me-3">`
`  35`  `            <i class="fa-solid fa-book-open"></i>`
`  36`  `          </div>`
`  37`  `          <div>`
`  38`  `            <div class="stat-value" id="lblActiveCourses">0</div>`
`  39`  `            <div class="stat-label">Active Courses</div>`
`  40`  `          </div>`
`  41`  `        </div>`
`  42`  `      </div>`
`  43`  ``
`  44`  `      <!-- Pending Grading (click → grading queue) -->`
`  45`  `      <div class="col-xl-3 col-md-6">`
`  46`  `        <a href="<%= ResolveUrl("~/Pages/Lecturer/Grading.aspx?filter=pending") %>" class="text-decoration-none">`
`  47`  `        <div class="glass-card stat-card-3 p-3 d-flex align-items-center" style="cursor:pointer;" title="Open pending grading">`
`  48`  `          <div class="stat-icon stat-icon-3 me-3">`
`  49`  `            <i class="fa-solid fa-file-signature"></i>`
`  50`  `          </div>`
`  51`  `          <div>`
`  52`  `            <div class="stat-value" id="lblPendingGrading">0</div>`
`  53`  `            <div class="stat-label">Pending Grading</div>`
`  54`  `          </div>`
`  55`  `        </div>`
`  56`  `        </a>`
`  57`  `      </div>`
`  58`  ``
`  59`  `      <!-- Average Grade -->`
`  60`  `      <div class="col-xl-3 col-md-6">`
`  61`  `        <div class="glass-card stat-card-4 p-3 d-flex align-items-center">`
`  62`  `          <div class="stat-icon stat-icon-4 me-3">`
`  63`  `            <i class="fa-solid fa-chart-line"></i>`
`  64`  `          </div>`
`  65`  `          <div>`
`  66`  `            <div class="stat-value" id="lblAverageGrade">84%</div>`
`  67`  `            <div class="stat-label">Average Grade</div>`
`  68`  `          </div>`
`  69`  `        </div>`
`  70`  `      </div>`
`  71`  `    </div>`
`  72`  ``
`  73`  `    <!-- Charts Row -->`
`  74`  `    <div class="row g-4 mb-4">`
`  75`  `      <!-- Enrollment Trends -->`
`  76`  `      <div class="col-lg-6">`
`  77`  `        <div class="glass-card p-4">`
`  78`  `          <h5 class="fw-bold mb-3 text-dark" style="font-size: 1.05rem;">Enrollment Trends</h5>`
`  79`  `          <div class="chart-container">`
`  80`  `            <!-- Chart.js canvas for Enrollment Trends -->`
`  81`  `            <canvas id="chartEnrollmentTrend" class="w-100 h-100"></canvas>`
`  82`  `          </div>`
`  83`  `        </div>`
`  84`  `      </div>`
`  85`  ``
`  86`  `      <!-- Grade Distribution -->`
`  87`  `      <div class="col-lg-6">`
`  88`  `        <div class="glass-card p-4">`
`  89`  `          <h5 class="fw-bold mb-3 text-dark" style="font-size: 1.05rem;">Grade Distribution</h5>`
`  90`  `          <div class="chart-container">`
`  91`  `            <canvas id="chartGradeDistribution" class="w-100 h-100"></canvas>`
`  92`  `          </div>`
`  93`  `        </div>`
`  94`  `      </div>`
`  95`  `    </div>`
`  96`  ``
`  97`  `    <!-- Recent Submissions Table -->`
`  98`  `    <div class="glass-card mb-4">`
`  99`  `      <div class="p-4 d-flex justify-content-between align-items-center border-bottom border-light">`
` 100`  `        <h5 class="fw-bold mb-0 text-dark" style="font-size: 1.05rem;">Recent Submissions</h5>`
` 101`  `        <a href="<%= ResolveUrl("~/Pages/Lecturer/Grading.aspx") %>" class="text-decoration-none fw-semibold" style="color: var(--primary-accent); font-size: 0.88rem;">View All</a>`
` 102`  `      </div>`
` 103`  ``
` 104`  `      <div class="p-3 pt-0" id="dashSubmissionsWrap">`
` 105`  `        <div class="text-center py-4 text-muted">`
` 106`  `          <i class="fa-solid fa-circle-notch fa-spin me-2"></i>Loading submissions...`
` 107`  `        </div>`
` 108`  `      </div>`
` 109`  `    </div>`
` 110`  `  </div>`
` 111`  ``
` 112`  `  <!-- Grading Modal -->`
` 113`  `  <div class="modal fade" id="gradingModal" tabindex="-1" aria-hidden="true">`
` 114`  `    <div class="modal-dialog modal-dialog-centered">`
` 115`  `      <div class="modal-content modal-glass border-0">`
` 116`  `        <div class="modal-header border-bottom border-light">`
` 117`  `          <h5 class="modal-title fw-bold text-dark" id="modalTitle">Grade Submission</h5>`
` 118`  `          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>`
` 119`  `        </div>`
` 120`  `        <div class="modal-body p-4">`
` 121`  `          <div class="mb-3">`
` 122`  `            <label class="form-label text-muted small fw-bold uppercase">Student</label>`
` 123`  `            <div class="d-flex align-items-center">`
` 124`  `              <div id="modalStudentAvatar" class="student-avatar me-2 bg-secondary"></div>`
` 125`  `              <span id="modalStudentName" class="fw-semibold text-dark"></span>`
` 126`  `            </div>`
` 127`  `          </div>`
` 128`  ``
` 129`  `          <div class="mb-3">`
` 130`  `            <label class="form-label text-muted small fw-bold">Assignment Question</label>`
` 131`  `            <p id="modalAssignment" class="p-3 rounded bg-light text-secondary border border-light small mb-0"></p>`
` 132`  `          </div>`
` 133`  ``
` 134`  `          <div class="mb-3">`
` 135`  `            <label class="form-label text-muted small fw-bold">Student's Answer</label>`
` 136`  `            <div id="modalAnswer" class="p-3 rounded bg-white border border-light text-dark small overflow-auto" style="max-height: 120px; white-space: pre-wrap;"></div>`
` 137`  `          </div>`
` 138`  ``
` 139`  `          <div class="row g-3 mb-3">`
` 140`  `            <div class="col-md-6">`
` 141`  `              <label class="form-label text-muted small fw-bold">Score</label>`
` 142`  `              <div class="input-group">`
` 143`  `                <input type="number" id="txtScore" class="form-control" min="0" value="0" />`
` 144`  `                <span class="input-group-text bg-light text-muted small" id="lblMaxScore">/ 10</span>`
` 145`  `              </div>`
` 146`  `            </div>`
` 147`  `          </div>`
` 148`  ``
` 149`  `          <div class="mb-3">`
` 150`  `            <label class="form-label text-muted small fw-bold">Feedback / Review</label>`
` 151`  `            <textarea id="txtReview" class="form-control" rows="3" placeholder="Provide feedback to the student..."></textarea>`
` 152`  `          </div>`
` 153`  ``
` 154`  `          <div id="modalErrorMessage" class="text-danger small mb-3" style="display:none;"></div>`
` 155`  `        </div>`
` 156`  `        <div class="modal-footer border-top border-light">`
` 157`  `          <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>`
` 158`  `          <button type="button" id="btnSubmitGrade" class="btn text-white rounded-pill px-4" style="background-color: var(--primary-accent);" onclick="submitGrading()">Save Grade</button>`
` 159`  `        </div>`
` 160`  `      </div>`
` 161`  `    </div>`
` 162`  `  </div>`
` 163`  ``
` 164`  `  <!-- Chart.js is lazy-loaded by dashboard.js when charts enter the viewport -->`
` 165`  `  <script src="Scripts/dashboard.js"></script>`
` 166`  `</asp:Content>`

## Source snapshot (raw)

```html
<%@ Page Title="" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="Dashboard.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Dashboard" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
  <link rel="stylesheet" href="Style/dashboard.css" />
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
  <div class="dashboard-container container-fluid px-0">
    <div class="d-flex flex-wrap justify-content-end gap-2 mb-3">
      <a href="<%= ResolveUrl("~/Pages/Lecturer/Grading.aspx?filter=pending") %>" class="btn btn-sm btn-outline-warning rounded-pill px-3">
        <i class="fa-solid fa-inbox me-1"></i> Grade pending
      </a>
      <button type="button" class="btn btn-sm btn-outline-dark rounded-pill px-3" onclick="exportDashGradesCsv()">
        <i class="fa-solid fa-file-csv me-1"></i> Export grades CSV
      </button>
    </div>
    <!-- Top Metrics Row -->
    <div class="row g-4 mb-4">
      <!-- Total Students -->
      <div class="col-xl-3 col-md-6">
        <div class="glass-card stat-card-1 p-3 d-flex align-items-center">
          <div class="stat-icon stat-icon-1 me-3">
            <i class="fa-solid fa-users"></i>
          </div>
          <div>
            <div class="stat-value" id="lblTotalStudents">0</div>
            <div class="stat-label">Total Students</div>
          </div>
        </div>
      </div>

      <!-- Active Courses -->
      <div class="col-xl-3 col-md-6">
        <div class="glass-card stat-card-2 p-3 d-flex align-items-center">
          <div class="stat-icon stat-icon-2 me-3">
            <i class="fa-solid fa-book-open"></i>
          </div>
          <div>
            <div class="stat-value" id="lblActiveCourses">0</div>
            <div class="stat-label">Active Courses</div>
          </div>
        </div>
      </div>

      <!-- Pending Grading (click → grading queue) -->
      <div class="col-xl-3 col-md-6">
        <a href="<%= ResolveUrl("~/Pages/Lecturer/Grading.aspx?filter=pending") %>" class="text-decoration-none">
        <div class="glass-card stat-card-3 p-3 d-flex align-items-center" style="cursor:pointer;" title="Open pending grading">
          <div class="stat-icon stat-icon-3 me-3">
            <i class="fa-solid fa-file-signature"></i>
          </div>
          <div>
            <div class="stat-value" id="lblPendingGrading">0</div>
            <div class="stat-label">Pending Grading</div>
          </div>
        </div>
        </a>
      </div>

      <!-- Average Grade -->
      <div class="col-xl-3 col-md-6">
        <div class="glass-card stat-card-4 p-3 d-flex align-items-center">
          <div class="stat-icon stat-icon-4 me-3">
            <i class="fa-solid fa-chart-line"></i>
          </div>
          <div>
            <div class="stat-value" id="lblAverageGrade">84%</div>
            <div class="stat-label">Average Grade</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Charts Row -->
    <div class="row g-4 mb-4">
      <!-- Enrollment Trends -->
      <div class="col-lg-6">
        <div class="glass-card p-4">
          <h5 class="fw-bold mb-3 text-dark" style="font-size: 1.05rem;">Enrollment Trends</h5>
          <div class="chart-container">
            <!-- Chart.js canvas for Enrollment Trends -->
            <canvas id="chartEnrollmentTrend" class="w-100 h-100"></canvas>
          </div>
        </div>
      </div>

      <!-- Grade Distribution -->
      <div class="col-lg-6">
        <div class="glass-card p-4">
          <h5 class="fw-bold mb-3 text-dark" style="font-size: 1.05rem;">Grade Distribution</h5>
          <div class="chart-container">
            <canvas id="chartGradeDistribution" class="w-100 h-100"></canvas>
          </div>
        </div>
      </div>
    </div>

    <!-- Recent Submissions Table -->
    <div class="glass-card mb-4">
      <div class="p-4 d-flex justify-content-between align-items-center border-bottom border-light">
        <h5 class="fw-bold mb-0 text-dark" style="font-size: 1.05rem;">Recent Submissions</h5>
        <a href="<%= ResolveUrl("~/Pages/Lecturer/Grading.aspx") %>" class="text-decoration-none fw-semibold" style="color: var(--primary-accent); font-size: 0.88rem;">View All</a>
      </div>

      <div class="p-3 pt-0" id="dashSubmissionsWrap">
        <div class="text-center py-4 text-muted">
          <i class="fa-solid fa-circle-notch fa-spin me-2"></i>Loading submissions...
        </div>
      </div>
    </div>
  </div>

  <!-- Grading Modal -->
  <div class="modal fade" id="gradingModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content modal-glass border-0">
        <div class="modal-header border-bottom border-light">
          <h5 class="modal-title fw-bold text-dark" id="modalTitle">Grade Submission</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body p-4">
          <div class="mb-3">
            <label class="form-label text-muted small fw-bold uppercase">Student</label>
            <div class="d-flex align-items-center">
              <div id="modalStudentAvatar" class="student-avatar me-2 bg-secondary"></div>
              <span id="modalStudentName" class="fw-semibold text-dark"></span>
            </div>
          </div>

          <div class="mb-3">
            <label class="form-label text-muted small fw-bold">Assignment Question</label>
            <p id="modalAssignment" class="p-3 rounded bg-light text-secondary border border-light small mb-0"></p>
          </div>

          <div class="mb-3">
            <label class="form-label text-muted small fw-bold">Student's Answer</label>
            <div id="modalAnswer" class="p-3 rounded bg-white border border-light text-dark small overflow-auto" style="max-height: 120px; white-space: pre-wrap;"></div>
          </div>

          <div class="row g-3 mb-3">
            <div class="col-md-6">
              <label class="form-label text-muted small fw-bold">Score</label>
              <div class="input-group">
                <input type="number" id="txtScore" class="form-control" min="0" value="0" />
                <span class="input-group-text bg-light text-muted small" id="lblMaxScore">/ 10</span>
              </div>
            </div>
          </div>

          <div class="mb-3">
            <label class="form-label text-muted small fw-bold">Feedback / Review</label>
            <textarea id="txtReview" class="form-control" rows="3" placeholder="Provide feedback to the student..."></textarea>
          </div>

          <div id="modalErrorMessage" class="text-danger small mb-3" style="display:none;"></div>
        </div>
        <div class="modal-footer border-top border-light">
          <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Cancel</button>
          <button type="button" id="btnSubmitGrade" class="btn text-white rounded-pill px-4" style="background-color: var(--primary-accent);" onclick="submitGrading()">Save Grade</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Chart.js is lazy-loaded by dashboard.js when charts enter the viewport -->
  <script src="Scripts/dashboard.js"></script>
</asp:Content>

```
