# Models.cs
**Source:** `Data/Models.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Lightweight POCOs / row shapes (CourseRow, CourseWorkRow, CWSubmissionRow, …) — not Entity Framework entities.

## File overview

- **Total lines:** 92
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See the code listing at the bottom._

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
