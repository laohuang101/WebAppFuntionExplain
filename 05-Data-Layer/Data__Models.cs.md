# Models.cs
**Source:** `Data/Models.cs`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Lightweight POCOs / row shapes (CourseRow, CourseWorkRow, CWSubmissionRow, …) — not Entity Framework entities.

## File overview

- **Total lines:** 92
- **Kind:** `.cs`

## Variables / fields (file level)

_No classic field declarations detected (or mostly locals inside methods)._

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```csharp
   1 | using System;
   2 | 
   3 | namespace WebAppAssignment.Data
   4 | {
   5 |     // Actual EduDB.mdf schema (from VS Server Explorer)
   6 | 
   7 |     // Users: UID, Name, Email, Password, Role, ...
   8 |     public class UserRow
   9 |     {
  10 |         public int UID { get; set; }
  11 |         public string Name { get; set; }
  12 |         public string Email { get; set; }
  13 |         public string Password { get; set; }
  14 |         public string Role { get; set; }
  15 |         public string Avatar { get; set; }
  16 |         public string Description { get; set; }
  17 |         public string ContactInfo { get; set; }
  18 |     }
  19 | 
  20 |     // Courses: CID, LecturerUID, Name, Description, Rating, BgImg, Categories, Level
  21 |     public class CourseRow
  22 |     {
  23 |         public int CID { get; set; }
  24 |         public int LecturerUID { get; set; }
  25 |         public string Name { get; set; }
  26 |         public string Description { get; set; }
  27 |         public decimal? Rating { get; set; }
  28 |         public string BgImg { get; set; }
  29 |         public string Categories { get; set; }
  30 |         public string Level { get; set; }
  31 |     }
  32 | 
  33 |     // Enrollments: CID, StudentUID, Progress
  34 |     public class EnrollmentRow
  35 |     {
  36 |         public int CID { get; set; }
  37 |         public int StudentUID { get; set; }
  38 |         public decimal Progress { get; set; }
  39 |     }
  40 | 
  41 |     // CourseWorks: CWID, ChID, Title, Description, DueDate
  42 |     public class CourseWorkRow
  43 |     {
  44 |         public int CWID { get; set; }
  45 |         public int ChID { get; set; }
  46 |         public string Title { get; set; }
  47 |         public string Description { get; set; }
  48 |         public DateTime? DueDate { get; set; }
  49 |     }
  50 | 
  51 |     // CWSubmissions: SID, CWID, StudentUID, SubmissionDate, Content
  52 |     public class CWSubmissionRow
  53 |     {
  54 |         public int SID { get; set; }
  55 |         public int CWID { get; set; }
  56 |         public int StudentUID { get; set; }
  57 |         public DateTime SubmissionDate { get; set; }
  58 |         public string Content { get; set; }
  59 |     }
  60 | 
  61 |     // ObjectiveQuestions: QID, QuestionText, OptionA, OptionB, OptionC, OptionD, CorrectAnswer
  62 |     public class ObjectiveQuestionRow
  63 |     {
  64 |         public int QID { get; set; }
  65 |         public string QuestionText { get; set; }
  66 |         public string OptionA { get; set; }
  67 |         public string OptionB { get; set; }
  68 |         public string OptionC { get; set; }
  69 |         public string OptionD { get; set; }
  70 |         public string CorrectAnswer { get; set; }
  71 |     }
  72 | 
  73 |     // ObjectiveAnswers: AnswerID, QID, StudentUID, SelectedAnswer, IsCorrect
  74 |     public class ObjectiveAnswerRow
  75 |     {
  76 |         public int AnswerID { get; set; }
  77 |         public int QID { get; set; }
  78 |         public int StudentUID { get; set; }
  79 |         public string SelectedAnswer { get; set; }
  80 |         public bool IsCorrect { get; set; }
  81 |     }
  82 | 
  83 |     // Live: GradeScales (GID, GradeLetter, MinMarks, MaxMarks)
  84 |     public class GradeScaleRow
  85 |     {
  86 |         public int GSID { get; set; }
  87 |         public string ScoreRange { get; set; }
  88 |         public string Grade { get; set; }
  89 |         public decimal MinMarks { get; set; }
  90 |         public decimal MaxMarks { get; set; }
  91 |     }
  92 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L3:** C# namespace grouping.
- **L8:** Class declaration for this page/service.
- **L21:** Class declaration for this page/service.
- **L24:** Owner lecturer foreign key.
- **L34:** Class declaration for this page/service.
- **L42:** Class declaration for this page/service.
- **L48:** Assignment deadline; submissions close after due day.
- **L52:** Class declaration for this page/service.
- **L62:** Class declaration for this page/service.
- **L74:** Class declaration for this page/service.
- **L84:** Class declaration for this page/service.

## Source snapshot (raw)

```csharp
using System;

namespace WebAppAssignment.Data
{
    // Actual EduDB.mdf schema (from VS Server Explorer)

    // Users: UID, Name, Email, Password, Role, ...
    public class UserRow
    {
        public int UID { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public string Role { get; set; }
        public string Avatar { get; set; }
        public string Description { get; set; }
        public string ContactInfo { get; set; }
    }

    // Courses: CID, LecturerUID, Name, Description, Rating, BgImg, Categories, Level
    public class CourseRow
    {
        public int CID { get; set; }
        public int LecturerUID { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public decimal? Rating { get; set; }
        public string BgImg { get; set; }
        public string Categories { get; set; }
        public string Level { get; set; }
    }

    // Enrollments: CID, StudentUID, Progress
    public class EnrollmentRow
    {
        public int CID { get; set; }
        public int StudentUID { get; set; }
        public decimal Progress { get; set; }
    }

    // CourseWorks: CWID, ChID, Title, Description, DueDate
    public class CourseWorkRow
    {
        public int CWID { get; set; }
        public int ChID { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public DateTime? DueDate { get; set; }
    }

    // CWSubmissions: SID, CWID, StudentUID, SubmissionDate, Content
    public class CWSubmissionRow
    {
        public int SID { get; set; }
        public int CWID { get; set; }
        public int StudentUID { get; set; }
        public DateTime SubmissionDate { get; set; }
        public string Content { get; set; }
    }

    // ObjectiveQuestions: QID, QuestionText, OptionA, OptionB, OptionC, OptionD, CorrectAnswer
    public class ObjectiveQuestionRow
    {
        public int QID { get; set; }
        public string QuestionText { get; set; }
        public string OptionA { get; set; }
        public string OptionB { get; set; }
        public string OptionC { get; set; }
        public string OptionD { get; set; }
        public string CorrectAnswer { get; set; }
    }

    // ObjectiveAnswers: AnswerID, QID, StudentUID, SelectedAnswer, IsCorrect
    public class ObjectiveAnswerRow
    {
        public int AnswerID { get; set; }
        public int QID { get; set; }
        public int StudentUID { get; set; }
        public string SelectedAnswer { get; set; }
        public bool IsCorrect { get; set; }
    }

    // Live: GradeScales (GID, GradeLetter, MinMarks, MaxMarks)
    public class GradeScaleRow
    {
        public int GSID { get; set; }
        public string ScoreRange { get; set; }
        public string Grade { get; set; }
        public decimal MinMarks { get; set; }
        public decimal MaxMarks { get; set; }
    }
}

```
