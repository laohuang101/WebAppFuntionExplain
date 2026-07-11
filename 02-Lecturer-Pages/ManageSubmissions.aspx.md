# ManageSubmissions.aspx
**Source:** `Pages/Lecturer/ManageSubmissions.aspx`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 65
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```html
   1 | <%@ Page Title="Manage Submissions" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="ManageSubmissions.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.ManageSubmissions" %>
   2 | 
   3 | <asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
   4 |   <link rel="stylesheet" href="Style/course-creation.css" />
   5 | </asp:Content>
   6 | 
   7 | <asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
   8 |   <div class="container-fluid">
   9 |     <div class="d-flex justify-content-between align-items-center mb-4">
  10 |       <div>
  11 |         <h3 class="fw-bold text-dark mb-1">Manage Submissions</h3>
  12 |         <p class="text-muted small mb-0">View and grade student submissions for your assignments.</p>
  13 |       </div>
  14 |     </div>
  15 | 
  16 |     <div class="row g-3">
  17 |       <div class="col-md-4">
  18 |         <div class="glass-card p-3">
  19 |           <label class="form-label small text-muted">Assignment</label>
  20 |           <select id="ddlAssignments" class="form-select mb-2"></select>
  21 |           <button id="btnLoadSubs" class="btn btn-sm btn-pill-accent">Load Submissions</button>
  22 |         </div>
  23 |       </div>
  24 |       <div class="col-md-8">
  25 |         <div class="glass-card p-3">
  26 |           <h6 class="fw-bold">Submissions</h6>
  27 |           <div id="submissionsList" class="mt-2">
  28 |             <div class="text-muted">No assignment selected.</div>
  29 |           </div>
  30 |         </div>
  31 |       </div>
  32 |     </div>
  33 | 
  34 |   </div>
  35 | 
  36 |   <!-- Grading Modal -->
  37 |   <div class="modal fade" id="gradeModal" tabindex="-1" aria-hidden="true">
  38 |     <div class="modal-dialog modal-dialog-centered modal-lg">
  39 |       <div class="modal-content modal-glass border-0">
  40 |         <div class="modal-header border-bottom border-light">
  41 |           <h5 class="modal-title">Grade Submission</h5>
  42 |           <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
  43 |         </div>
  44 |         <div class="modal-body p-4">
  45 |           <div id="gradeSubmissionBody"></div>
  46 |           <div class="mb-3 mt-3">
  47 |             <label class="form-label small text-muted">Score</label>
  48 |             <input type="number" id="txtGradeScore" class="form-control" min="0" />
  49 |           </div>
  50 |           <div class="mb-3">
  51 |             <label class="form-label small text-muted">Feedback</label>
  52 |             <textarea id="txtGradeFeedback" class="form-control" rows="3"></textarea>
  53 |           </div>
  54 |           <div id="gradeError" class="text-danger small" style="display:none"></div>
  55 |         </div>
  56 |         <div class="modal-footer border-top border-light">
  57 |           <button type="button" class="btn btn-light" data-bs-dismiss="modal">Cancel</button>
  58 |           <button type="button" id="btnSubmitGrade" class="btn btn-pill-accent">Save Grade</button>
  59 |         </div>
  60 |       </div>
  61 |     </div>
  62 |   </div>
  63 | 
  64 |   <script src="Scripts/manage-submissions.js"></script>
  65 | </asp:Content>
```

## Source snapshot (raw)

```html
<%@ Page Title="Manage Submissions" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="ManageSubmissions.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.ManageSubmissions" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
  <link rel="stylesheet" href="Style/course-creation.css" />
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
  <div class="container-fluid">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h3 class="fw-bold text-dark mb-1">Manage Submissions</h3>
        <p class="text-muted small mb-0">View and grade student submissions for your assignments.</p>
      </div>
    </div>

    <div class="row g-3">
      <div class="col-md-4">
        <div class="glass-card p-3">
          <label class="form-label small text-muted">Assignment</label>
          <select id="ddlAssignments" class="form-select mb-2"></select>
          <button id="btnLoadSubs" class="btn btn-sm btn-pill-accent">Load Submissions</button>
        </div>
      </div>
      <div class="col-md-8">
        <div class="glass-card p-3">
          <h6 class="fw-bold">Submissions</h6>
          <div id="submissionsList" class="mt-2">
            <div class="text-muted">No assignment selected.</div>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- Grading Modal -->
  <div class="modal fade" id="gradeModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content modal-glass border-0">
        <div class="modal-header border-bottom border-light">
          <h5 class="modal-title">Grade Submission</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body p-4">
          <div id="gradeSubmissionBody"></div>
          <div class="mb-3 mt-3">
            <label class="form-label small text-muted">Score</label>
            <input type="number" id="txtGradeScore" class="form-control" min="0" />
          </div>
          <div class="mb-3">
            <label class="form-label small text-muted">Feedback</label>
            <textarea id="txtGradeFeedback" class="form-control" rows="3"></textarea>
          </div>
          <div id="gradeError" class="text-danger small" style="display:none"></div>
        </div>
        <div class="modal-footer border-top border-light">
          <button type="button" class="btn btn-light" data-bs-dismiss="modal">Cancel</button>
          <button type="button" id="btnSubmitGrade" class="btn btn-pill-accent">Save Grade</button>
        </div>
      </div>
    </div>
  </div>

  <script src="Scripts/manage-submissions.js"></script>
</asp:Content>

```
