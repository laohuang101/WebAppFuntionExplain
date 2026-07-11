# Grading.aspx
**Source:** `Pages/Lecturer/Grading.aspx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

List submissions for lecturer courses; assign marks and feedback; CSV export.

## File overview

- **Total lines:** 94
- **Kind:** `.aspx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See the code listing at the bottom._

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
