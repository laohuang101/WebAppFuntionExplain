# Assignments.aspx
**Source:** `Pages/Lecturer/Assignments.aspx`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Build CourseWorks with due date, rubric or objective quiz. Due date closes student submit.

## File overview

- **Total lines:** 111
- **Kind:** `.aspx`

## Variables / fields (file level)

Simple table of names declared at file/class level.

Markup file — variables live in the matching `.cs` / `.js` companion docs.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See the code listing at the bottom._

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```html
   1 | <%@ Page Title="Assignment Builder" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="Assignments.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Assignments" %>
   2 | 
   3 | <asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
   4 |   <link rel="stylesheet" href="Style/lecturer-pages.css" />
   5 | </asp:Content>
   6 | 
   7 | <asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
   8 |   <div class="lecturer-page">
   9 |     <div class="d-flex flex-wrap justify-content-between align-items-start gap-3 mb-4">
  10 |       <div>
  11 |         <h3 class="fw-bold text-dark mb-1">Assignment Builder</h3>
  12 |         <p class="text-muted small mb-0">Create new assignments or quizzes for your students.</p>
  13 |       </div>
  14 |       <div class="d-flex gap-2">
  15 |         <button type="button" class="btn btn-light border rounded-pill px-4" onclick="saveAssignment(false)">Save Draft</button>
  16 |         <button type="button" class="btn btn-pill-accent d-flex align-items-center gap-2" onclick="saveAssignment(true)">
  17 |           <i class="fa-solid fa-paper-plane"></i> Publish
  18 |         </button>
  19 |       </div>
  20 |     </div>
  21 | 
  22 |     <!-- Type toggle -->
  23 |     <div class="type-toggle mb-4">
  24 |       <button type="button" class="type-btn active" id="btnTypeAssignment" onclick="setBuilderType('Text')">
  25 |         <i class="fa-regular fa-file-lines me-1"></i> Assignment
  26 |       </button>
  27 |       <button type="button" class="type-btn" id="btnTypeQuiz" onclick="setBuilderType('Objective')">
  28 |         <i class="fa-regular fa-circle-question me-1"></i> Quiz
  29 |       </button>
  30 |     </div>
  31 | 
  32 |     <div class="row g-4">
  33 |       <!-- Main column -->
  34 |       <div class="col-lg-8">
  35 |         <div class="glass-card p-4 mb-4">
  36 |           <div class="mb-3">
  37 |             <label class="form-label text-muted small fw-bold">Title</label>
  38 |             <input type="text" id="txtTitle" class="form-control" placeholder="e.g. Final Project Submission" />
  39 |           </div>
  40 |           <div class="mb-0">
  41 |             <label class="form-label text-muted small fw-bold">Description / Instructions</label>
  42 |             <textarea id="txtInstructions" class="form-control" rows="4" placeholder="Provide clear instructions for the students..."></textarea>
  43 |           </div>
  44 |         </div>
  45 | 
  46 |         <!-- Subjective: Grading Rubric -->
  47 |         <div id="panelRubric" class="glass-card p-4 mb-4">
  48 |           <div class="d-flex justify-content-between align-items-center mb-3">
  49 |             <h6 class="fw-bold mb-0">Grading Rubric</h6>
  50 |             <span class="text-muted small">Total: <span id="lblRubricTotal" class="fw-semibold">100 / 100</span> pts</span>
  51 |           </div>
  52 |           <div id="rubricTotalHint" class="text-danger small mb-2" style="display:none;">
  53 |             Rubric criteria must total exactly 100 pts.
  54 |           </div>
  55 |           <div id="rubricList"></div>
  56 |           <button type="button" class="btn btn-link text-decoration-none p-0 mt-2" style="color:var(--primary-accent);" onclick="addRubricRow()">
  57 |             + Add Criterion
  58 |           </button>
  59 |         </div>
  60 | 
  61 |         <!-- Objective: Questions -->
  62 |         <div id="panelQuestions" class="mb-4" style="display:none;">
  63 |           <div id="questionsList"></div>
  64 |           <button type="button" class="btn btn-light border w-100 py-3 text-muted" style="border-style:dashed !important;" onclick="addObjectiveQuestion()">
  65 |             <i class="fa-solid fa-plus me-1"></i> Add Question
  66 |           </button>
  67 |         </div>
  68 |       </div>
  69 | 
  70 |       <!-- Settings sidebar -->
  71 |       <div class="col-lg-4">
  72 |         <div class="glass-card p-4">
  73 |           <h6 class="fw-bold mb-3">Settings</h6>
  74 |           <div class="mb-3">
  75 |             <label class="form-label text-muted small fw-bold">Target Course</label>
  76 |             <select id="ddlCourse" class="form-select"></select>
  77 |           </div>
  78 |           <div class="mb-3">
  79 |             <label class="form-label text-muted small fw-bold">Due Date</label>
  80 |             <input type="date" id="txtDueDate" class="form-control" />
  81 |             <div class="form-text small text-muted">
  82 |               Students can submit through the end of this day. After that the assignment is <strong>closed</strong>.
  83 |               Leave empty for no deadline.
  84 |             </div>
  85 |           </div>
  86 |           <div class="mb-3" id="timeLimitGroup" style="display:none;">
  87 |             <label class="form-label text-muted small fw-bold">Time Limit (minutes)</label>
  88 |             <input type="number" id="txtTimeLimit" class="form-control" min="0" placeholder="Optional" />
  89 |           </div>
  90 |           <div class="form-check" id="requireFileGroup">
  91 |             <input class="form-check-input" type="checkbox" id="chkRequireFile" />
  92 |             <label class="form-check-label small" for="chkRequireFile">Require file upload</label>
  93 |           </div>
  94 |           <input type="hidden" id="hfCwid" value="" />
  95 |           <div id="saveError" class="text-danger small mt-3" style="display:none;"></div>
  96 |           <div id="saveOk" class="text-success small mt-3" style="display:none;"></div>
  97 |         </div>
  98 | 
  99 |         <!-- Existing list -->
 100 |         <div class="glass-card p-4 mt-4">
 101 |           <h6 class="fw-bold mb-3">Your CourseWorks</h6>
 102 |           <div id="existingList" class="existing-list">
 103 |             <div class="text-muted small">Loading...</div>
 104 |           </div>
 105 |         </div>
 106 |       </div>
 107 |     </div>
 108 |   </div>
 109 | 
 110 |   <script src="Scripts/assignments.js"></script>
 111 | </asp:Content>
```
