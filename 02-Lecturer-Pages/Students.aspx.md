# Students.aspx
**Source:** `Pages/Lecturer/Students.aspx`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Enrolled students per course with progress counts.

## File overview

- **Total lines:** 85
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```html
   1 | <%@ Page Title="Student Performance" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="Students.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Students" %>
   2 | 
   3 | <asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
   4 |   <link rel="stylesheet" href="Style/lecturer-pages.css" />
   5 | </asp:Content>
   6 | 
   7 | <asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
   8 |   <div class="lecturer-page">
   9 |     <div class="mb-4">
  10 |       <h3 class="fw-bold text-dark mb-1">Student Performance</h3>
  11 |       <p class="text-muted small mb-0">Monitor progress and identify students who need help. Search, sort, filter, and paginate below.</p>
  12 |     </div>
  13 | 
  14 |     <div class="glass-card p-3">
  15 |       <div id="studentsTableWrap">
  16 |         <div class="text-center text-muted py-4">
  17 |           <i class="fa-solid fa-circle-notch fa-spin me-2"></i>Loading students...
  18 |         </div>
  19 |       </div>
  20 |     </div>
  21 |   </div>
  22 | 
  23 |   <!-- Student detail modal -->
  24 |   <div class="modal fade" id="studentModal" tabindex="-1" aria-hidden="true">
  25 |     <div class="modal-dialog modal-lg modal-dialog-centered">
  26 |       <div class="modal-content border-0" style="border-radius:18px;">
  27 |         <div class="modal-header border-0 pb-0">
  28 |           <div class="d-flex align-items-center gap-3">
  29 |             <div class="student-avatar lg" id="mAvatar"> - </div>
  30 |             <div>
  31 |               <h5 class="fw-bold mb-0" id="mName">Student</h5>
  32 |               <div class="text-muted small" id="mMeta"></div>
  33 |             </div>
  34 |           </div>
  35 |           <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
  36 |         </div>
  37 |         <div class="modal-body">
  38 |           <div class="row g-3 mb-4">
  39 |             <div class="col-md-4">
  40 |               <div class="stat-mini text-center p-3">
  41 |                 <div class="text-muted small">Current Grade</div>
  42 |                 <div class="fw-bold fs-3" id="mGrade" style="color:#10b981;"> - </div>
  43 |               </div>
  44 |             </div>
  45 |             <div class="col-md-4">
  46 |               <div class="stat-mini text-center p-3">
  47 |                 <div class="text-muted small">Course Progress</div>
  48 |                 <div class="fw-bold fs-3" id="mProgress">0%</div>
  49 |               </div>
  50 |             </div>
  51 |             <div class="col-md-4">
  52 |               <div class="stat-mini text-center p-3">
  53 |                 <div class="text-muted small">Attendance*</div>
  54 |                 <div class="fw-bold fs-3" id="mAttendance"> - </div>
  55 |               </div>
  56 |             </div>
  57 |           </div>
  58 |           <p class="text-muted small mb-3">* Attendance uses Enrollments/CourseProgresses Progress (no separate attendance table in EduDB).</p>
  59 | 
  60 |           <h6 class="fw-bold mb-2">Performance Trend</h6>
  61 |           <div class="chart-box mb-4">
  62 |             <canvas id="trendChart" height="100"></canvas>
  63 |           </div>
  64 | 
  65 |           <h6 class="fw-bold mb-2">Recent Grades</h6>
  66 |           <div class="table-responsive">
  67 |             <table class="table table-sm mb-0">
  68 |               <thead>
  69 |                 <tr>
  70 |                   <th>Assignment</th>
  71 |                   <th>Date</th>
  72 |                   <th class="text-end">Score</th>
  73 |                 </tr>
  74 |               </thead>
  75 |               <tbody id="mGradesBody"></tbody>
  76 |             </table>
  77 |           </div>
  78 |         </div>
  79 |       </div>
  80 |     </div>
  81 |   </div>
  82 | 
  83 |   <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  84 |   <script src="Scripts/students.js"></script>
  85 | </asp:Content>
```

**Line notes**

- **L62:** Dashboard chart/visualization.
- **L83:** Dashboard chart/visualization.

## Source snapshot (raw)

```html
<%@ Page Title="Student Performance" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="Students.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.Students" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
  <link rel="stylesheet" href="Style/lecturer-pages.css" />
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
  <div class="lecturer-page">
    <div class="mb-4">
      <h3 class="fw-bold text-dark mb-1">Student Performance</h3>
      <p class="text-muted small mb-0">Monitor progress and identify students who need help. Search, sort, filter, and paginate below.</p>
    </div>

    <div class="glass-card p-3">
      <div id="studentsTableWrap">
        <div class="text-center text-muted py-4">
          <i class="fa-solid fa-circle-notch fa-spin me-2"></i>Loading students...
        </div>
      </div>
    </div>
  </div>

  <!-- Student detail modal -->
  <div class="modal fade" id="studentModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content border-0" style="border-radius:18px;">
        <div class="modal-header border-0 pb-0">
          <div class="d-flex align-items-center gap-3">
            <div class="student-avatar lg" id="mAvatar"> - </div>
            <div>
              <h5 class="fw-bold mb-0" id="mName">Student</h5>
              <div class="text-muted small" id="mMeta"></div>
            </div>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <div class="row g-3 mb-4">
            <div class="col-md-4">
              <div class="stat-mini text-center p-3">
                <div class="text-muted small">Current Grade</div>
                <div class="fw-bold fs-3" id="mGrade" style="color:#10b981;"> - </div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="stat-mini text-center p-3">
                <div class="text-muted small">Course Progress</div>
                <div class="fw-bold fs-3" id="mProgress">0%</div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="stat-mini text-center p-3">
                <div class="text-muted small">Attendance*</div>
                <div class="fw-bold fs-3" id="mAttendance"> - </div>
              </div>
            </div>
          </div>
          <p class="text-muted small mb-3">* Attendance uses Enrollments/CourseProgresses Progress (no separate attendance table in EduDB).</p>

          <h6 class="fw-bold mb-2">Performance Trend</h6>
          <div class="chart-box mb-4">
            <canvas id="trendChart" height="100"></canvas>
          </div>

          <h6 class="fw-bold mb-2">Recent Grades</h6>
          <div class="table-responsive">
            <table class="table table-sm mb-0">
              <thead>
                <tr>
                  <th>Assignment</th>
                  <th>Date</th>
                  <th class="text-end">Score</th>
                </tr>
              </thead>
              <tbody id="mGradesBody"></tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="Scripts/students.js"></script>
</asp:Content>

```
