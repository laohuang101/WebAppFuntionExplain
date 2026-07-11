# Grading.aspx
**Source:** `Pages/Lecturer/Grading.aspx`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

List submissions for lecturer courses; assign marks and feedback; CSV export.

## File overview

- **Total lines:** 94
- **Kind:** `.aspx`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

```html
   1 | <%@ Page Title="Grading" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="Grading.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Grading" %>
   2 | 
   3 | <asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
   4 |   <link rel="stylesheet" href="Style/lecturer-pages.css" />
   5 | </asp:Content>
   6 | 
   7 | <asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
   8 |   <div class="lecturer-page">
   9 |     <div class="d-flex flex-wrap justify-content-between align-items-start gap-3 mb-3">
  10 |       <div>
  11 |         <h3 class="fw-bold text-dark mb-1" id="lblAssignmentTitle">Grading</h3>
  12 |         <p class="text-muted small mb-0" id="lblAssignmentMeta">Select a submission to grade</p>
  13 |       </div>
  14 |       <div class="d-flex flex-wrap align-items-center gap-3">
  15 |         <div class="btn-group btn-group-sm" role="group" aria-label="Filter">
  16 |           <button type="button" class="btn btn-outline-secondary active" data-filter="all" onclick="setStatusFilter('all', this)">All</button>
  17 |           <button type="button" class="btn btn-outline-secondary" data-filter="pending" onclick="setStatusFilter('pending', this)">
  18 |             Pending <span class="badge bg-warning text-dark ms-1" id="badgePendingCount">0</span>
  19 |           </button>
  20 |           <button type="button" class="btn btn-outline-secondary" data-filter="graded" onclick="setStatusFilter('graded', this)">Graded</button>
  21 |         </div>
  22 |         <button type="button" class="btn btn-sm btn-outline-dark rounded-pill px-3" onclick="exportGradesCsv()">
  23 |           <i class="fa-solid fa-file-csv me-1"></i> Export CSV
  24 |         </button>
  25 |         <div class="text-end">
  26 |           <div class="text-muted small mb-1">Graded: <span id="lblGradedCount">0/0</span></div>
  27 |           <div class="progress" style="width:160px;height:8px;">
  28 |             <div id="gradedBar" class="progress-bar" style="background:var(--primary-accent);width:0%;"></div>
  29 |           </div>
  30 |         </div>
  31 |       </div>
  32 |     </div>
  33 | 
  34 |     <div class="row g-3 grading-layout">
  35 |       <!-- Student list -->
  36 |       <div class="col-lg-3">
  37 |         <div class="glass-card p-3 h-100">
  38 |           <input type="text" id="txtSearchStudents" class="form-control form-control-sm mb-3" placeholder="Search students..." oninput="filterStudents()" />
  39 |           <div id="studentList" class="student-list"></div>
  40 |         </div>
  41 |       </div>
  42 | 
  43 |       <!-- Preview -->
  44 |       <div class="col-lg-5">
  45 |         <div class="glass-card p-3 h-100">
  46 |           <div class="d-flex justify-content-between align-items-center mb-3">
  47 |             <div class="d-flex align-items-center gap-2">
  48 |               <div class="student-avatar" id="previewAvatar"> - </div>
  49 |               <h6 class="fw-bold mb-0" id="previewName">Select a student</h6>
  50 |             </div>
  51 |             <a id="btnDownload" href="#" target="_blank" class="btn btn-sm btn-light border" style="display:none;">
  52 |               <i class="fa-solid fa-download me-1"></i> Open File
  53 |             </a>
  54 |           </div>
  55 |           <div id="answerPreview" class="answer-preview">
  56 |             <div class="text-muted text-center py-5">Document / Answer Preview Area</div>
  57 |           </div>
  58 |         </div>
  59 |       </div>
  60 | 
  61 |       <!-- Rubric / score -->
  62 |       <div class="col-lg-4">
  63 |         <div class="glass-card p-3 h-100 d-flex flex-column">
  64 |           <h6 class="fw-bold mb-3">Grading</h6>
  65 |           <div class="mb-3">
  66 |             <label class="form-label small text-muted fw-bold">Score</label>
  67 |             <div class="input-group">
  68 |               <input type="number" id="txtGradeScore" class="form-control" min="0" value="0" oninput="updateTotalDisplay()" />
  69 |               <span class="input-group-text" id="lblMaxScore">/ 100</span>
  70 |             </div>
  71 |           </div>
  72 |           <div class="mb-3">
  73 |             <div class="d-flex justify-content-between">
  74 |               <span class="fw-bold">Total Score</span>
  75 |               <span class="fw-bold" style="color:var(--primary-accent);" id="lblTotalScore">0/100</span>
  76 |             </div>
  77 |           </div>
  78 |           <div class="mb-3 flex-grow-1">
  79 |             <label class="form-label small text-muted fw-bold">Feedback Comments</label>
  80 |             <textarea id="txtFeedback" class="form-control" rows="6" placeholder="Great job on the layout, but..."></textarea>
  81 |           </div>
  82 |           <div id="gradeError" class="text-danger small mb-2" style="display:none;"></div>
  83 |           <button type="button" class="btn btn-pill-accent w-100 mb-2" onclick="submitGrade()">Submit Grade</button>
  84 |           <div class="d-flex gap-2">
  85 |             <button type="button" class="btn btn-light border flex-fill" onclick="navStudent(-1)"><i class="fa-solid fa-chevron-left"></i></button>
  86 |             <button type="button" class="btn btn-light border flex-fill" onclick="navStudent(1)"><i class="fa-solid fa-chevron-right"></i></button>
  87 |           </div>
  88 |         </div>
  89 |       </div>
  90 |     </div>
  91 |   </div>
  92 | 
  93 |   <script src="Scripts/grading.js"></script>
  94 | </asp:Content>
```

**Line notes**

- **L22:** CSV export.
- **L23:** CSV export.

## Source snapshot (raw)

```html
<%@ Page Title="Grading" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="Grading.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Grading" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
  <link rel="stylesheet" href="Style/lecturer-pages.css" />
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
  <div class="lecturer-page">
    <div class="d-flex flex-wrap justify-content-between align-items-start gap-3 mb-3">
      <div>
        <h3 class="fw-bold text-dark mb-1" id="lblAssignmentTitle">Grading</h3>
        <p class="text-muted small mb-0" id="lblAssignmentMeta">Select a submission to grade</p>
      </div>
      <div class="d-flex flex-wrap align-items-center gap-3">
        <div class="btn-group btn-group-sm" role="group" aria-label="Filter">
          <button type="button" class="btn btn-outline-secondary active" data-filter="all" onclick="setStatusFilter('all', this)">All</button>
          <button type="button" class="btn btn-outline-secondary" data-filter="pending" onclick="setStatusFilter('pending', this)">
            Pending <span class="badge bg-warning text-dark ms-1" id="badgePendingCount">0</span>
          </button>
          <button type="button" class="btn btn-outline-secondary" data-filter="graded" onclick="setStatusFilter('graded', this)">Graded</button>
        </div>
        <button type="button" class="btn btn-sm btn-outline-dark rounded-pill px-3" onclick="exportGradesCsv()">
          <i class="fa-solid fa-file-csv me-1"></i> Export CSV
        </button>
        <div class="text-end">
          <div class="text-muted small mb-1">Graded: <span id="lblGradedCount">0/0</span></div>
          <div class="progress" style="width:160px;height:8px;">
            <div id="gradedBar" class="progress-bar" style="background:var(--primary-accent);width:0%;"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="row g-3 grading-layout">
      <!-- Student list -->
      <div class="col-lg-3">
        <div class="glass-card p-3 h-100">
          <input type="text" id="txtSearchStudents" class="form-control form-control-sm mb-3" placeholder="Search students..." oninput="filterStudents()" />
          <div id="studentList" class="student-list"></div>
        </div>
      </div>

      <!-- Preview -->
      <div class="col-lg-5">
        <div class="glass-card p-3 h-100">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <div class="d-flex align-items-center gap-2">
              <div class="student-avatar" id="previewAvatar"> - </div>
              <h6 class="fw-bold mb-0" id="previewName">Select a student</h6>
            </div>
            <a id="btnDownload" href="#" target="_blank" class="btn btn-sm btn-light border" style="display:none;">
              <i class="fa-solid fa-download me-1"></i> Open File
            </a>
          </div>
          <div id="answerPreview" class="answer-preview">
            <div class="text-muted text-center py-5">Document / Answer Preview Area</div>
          </div>
        </div>
      </div>

      <!-- Rubric / score -->
      <div class="col-lg-4">
        <div class="glass-card p-3 h-100 d-flex flex-column">
          <h6 class="fw-bold mb-3">Grading</h6>
          <div class="mb-3">
            <label class="form-label small text-muted fw-bold">Score</label>
            <div class="input-group">
              <input type="number" id="txtGradeScore" class="form-control" min="0" value="0" oninput="updateTotalDisplay()" />
              <span class="input-group-text" id="lblMaxScore">/ 100</span>
            </div>
          </div>
          <div class="mb-3">
            <div class="d-flex justify-content-between">
              <span class="fw-bold">Total Score</span>
              <span class="fw-bold" style="color:var(--primary-accent);" id="lblTotalScore">0/100</span>
            </div>
          </div>
          <div class="mb-3 flex-grow-1">
            <label class="form-label small text-muted fw-bold">Feedback Comments</label>
            <textarea id="txtFeedback" class="form-control" rows="6" placeholder="Great job on the layout, but..."></textarea>
          </div>
          <div id="gradeError" class="text-danger small mb-2" style="display:none;"></div>
          <button type="button" class="btn btn-pill-accent w-100 mb-2" onclick="submitGrade()">Submit Grade</button>
          <div class="d-flex gap-2">
            <button type="button" class="btn btn-light border flex-fill" onclick="navStudent(-1)"><i class="fa-solid fa-chevron-left"></i></button>
            <button type="button" class="btn btn-light border flex-fill" onclick="navStudent(1)"><i class="fa-solid fa-chevron-right"></i></button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="Scripts/grading.js"></script>
</asp:Content>

```
