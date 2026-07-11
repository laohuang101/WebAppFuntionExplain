# Data layer overview — EduLMS (pure SQL)

**No Entity Framework.** All access uses `System.Data.SqlClient` against LocalDB (`EduDB.mdf`) via connection string `MyDbConn` in `Web.config`.

**Docs folder:** `05-Data-Layer/`  
**Security SQL helpers:** `06-Security-Core/` (`AuthService`, `AuthSchema`, …)

---

## Architecture

```
Pages / ashx / WebMethods
        │
        ▼
┌───────────────────┐     ┌────────────────────┐
│ LecturerRepository│     │ AuthService        │
│ (lecturer domain) │     │ (users / MFA / JWT)│
└─────────┬─────────┘     └──────────┬─────────┘
          │                          │
          └────────────┬─────────────┘
                       ▼
                 ┌──────────┐
                 │ DbHelper │  ← OpenConnection, ExecuteQuery/NonQuery/Scalar, P()
                 └────┬─────┘
                      ▼
              SQL Server LocalDB
              App_Data/EduDB.mdf
```

Optional startup path:

```
Global.asax / Master Page_Load
  → SchemaBootstrap.EnsureAll()
       → AuthSchema.Ensure()      (MfaSecret, PasswordHash, …)
       → CourseSchema.Ensure()    (IsPublished, …)
       → DbIndexes.Ensure()       (indexes if missing)
```

---

## Files in `Data/`

| Source | Doc | Role |
|--------|-----|------|
| `DbHelper.cs` | [Data__DbHelper.cs.md](../05-Data-Layer/Data__DbHelper.cs.md) | **Primary** ADO.NET helper |
| `DatabaseHelper.cs` | [Data__DatabaseHelper.cs.md](../05-Data-Layer/Data__DatabaseHelper.cs.md) | Legacy connection helper |
| `LecturerRepository.cs` | [Data__LecturerRepository.cs.md](../05-Data-Layer/Data__LecturerRepository.cs.md) | Courses, works, grades, students |
| `Models.cs` | [Data__Models.cs.md](../05-Data-Layer/Data__Models.cs.md) | Simple POCOs (not EF) |
| `CourseSchema.cs` | [Data__CourseSchema.cs.md](../05-Data-Layer/Data__CourseSchema.cs.md) | Ensure `IsPublished` etc. |
| `SchemaMap.cs` | [Data__SchemaMap.cs.md](../05-Data-Layer/Data__SchemaMap.cs.md) | Discover real table/column names |
| `SchemaBootstrap.cs` | [Data__SchemaBootstrap.cs.md](../05-Data-Layer/Data__SchemaBootstrap.cs.md) | Run all Ensure* once |
| `DbIndexes.cs` | [Data__DbIndexes.cs.md](../05-Data-Layer/Data__DbIndexes.cs.md) | Create indexes if missing |
| `Data/Security/*` | [06-Security-Core](../06-Security-Core/) | Auth + audit + upload guards |

---

## Connection string

From `Web.config`:

```xml
<connectionStrings>
  <add name="MyDbConn"
       connectionString="Data Source=(LocalDB)\MSSQLLocalDB;
         AttachDbFilename=|DataDirectory|\EduDB.mdf;
         Initial Catalog=EduDB; Integrated Security=True; ..." />
</connectionStrings>
```

`|DataDirectory|` → `App_Data/`.

---

## Domain tables (assignment MDF)

| Table | Key columns | Used by |
|-------|-------------|---------|
| **Users** | UID, Name, Email, Password/PasswordHash, Role, MfaSecret, MfaEnabled | AuthService |
| **Courses** | CID, LecturerUID, Name, Description, IsPublished, BgImg, … | LecturerRepository, Landing |
| **Chapters** | ChID, CID, … | CourseWorks parent, curriculum |
| **SubChapters** | SchID, ChID, Title, Content, … | CurriculumApi (name may vary — SchemaMap) |
| **StudyMats** | media links for lessons | CurriculumApi / uploads |
| **CourseWorks** | CWID, ChID, Title, Description (+ META JSON), **DueDate** | Assignments |
| **CWSubmissions** | SID, CWID, StudentUID, Content, SubmissionDate | Submit, Grading |
| **CWMarkings** | marks/feedback on SID | Grading |
| **Enrollments** | StudentUID, CID | Students page, stats |
| **SecurityAudit** (or similar) | Action, UserId, Email, IP, time | SecurityAudit + Admin AuditLog |

Exact names can differ slightly per MDF dump; `SchemaMap` / try-catch fallbacks handle that.

---

## LecturerRepository — responsibility map

| Area | Typical methods (see full doc) |
|------|--------------------------------|
| Dashboard | `GetDashboardData`, counts, recent submissions |
| Courses | `GetCoursesForLecturer`, `SaveCourse`, `DeleteCourse`, `SetCoursePublished` |
| Ownership | `AssertCourseOwner` — **always** before mutate |
| Curriculum support | chapter ensure helpers used by CourseWorks |
| Assignments | `GetCourseWorksForLecturer`, `SaveCourseWork`, `DeleteCourseWork`, META pack/parse |
| Grading | list submissions, `SaveGrade`, export helpers |
| Students | enrollments + progress counts |

**Rule:** almost every mutating query includes  
`WHERE … LecturerUID = @LecturerUID` (or join through course).

---

## DbHelper usage pattern

```csharp
using (var conn = DbHelper.OpenConnection()) { ... }  // or helpers that open internally

var dt = DbHelper.ExecuteQuery(
    "SELECT … FROM Courses WHERE LecturerUID=@L",
    DbHelper.P("@L", lecturerUid));

int n = DbHelper.ExecuteNonQuery(
    "UPDATE Courses SET IsPublished=@P WHERE CID=@C AND LecturerUID=@L",
    DbHelper.P("@P", 1), DbHelper.P("@C", cid), DbHelper.P("@L", uid));

int id = DbHelper.ExecuteScalarInt(
    "INSERT …; SELECT CAST(SCOPE_IDENTITY() AS INT);",
    DbHelper.P("@Name", name));
```

- **Always** use `DbHelper.P` / parameters — never string-concat user input into SQL.  
- `SafeString(row["Col"])` for null-safe string reads.

---

## Schema bootstrap vs migrations

This project does **not** use EF migrations. Instead:

1. Ship `App_Data/EduDB.mdf` with base tables.  
2. On run, `Ensure*` methods add missing columns/indexes if the MDF is older.  
3. Failures are often caught so the app still runs on partial schemas (with degraded features).

---

## Seed data

| Source | Notes |
|--------|--------|
| `Pages/Lecturer/SeedMockData.ashx` | Runtime seed (requires `AllowSeedMockData=true` + lecturer/admin) |
| `App_Data/SeedMockData.sql` | Optional SQL script for SSMS |

Seeded users may lack MFA secrets — prefer **Register + MFA** for real login demos.

---

## Pure SQL claim (markers)

- `packages.config` — no Entity Framework package for domain data.  
- Source uses `SqlConnection` / `SqlCommand` / `DbHelper`.  
- `Models.cs` classes are plain C# objects, **not** mapped EF entities.  
- Security folder is still pure SQL for Users/audit (documented under Security).

---

## How to study the Data docs

1. Read this file.  
2. [Data__DbHelper.cs.md](../05-Data-Layer/Data__DbHelper.cs.md) — connection + query API.  
3. [Data__LecturerRepository.cs.md](../05-Data-Layer/Data__LecturerRepository.cs.md) — largest domain SQL surface.  
4. [Data__Models.cs.md](../05-Data-Layer/Data__Models.cs.md) — shapes.  
5. Schema trio: CourseSchema → SchemaMap → SchemaBootstrap → DbIndexes.  
6. Cross-link to [01-SECURITY-OVERVIEW.md](01-SECURITY-OVERVIEW.md) for Users table auth SQL.

---

[← Full index](00-INDEX.md)
