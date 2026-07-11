# Data layer overview — EduLMS (pure SQL)

**No Entity Framework.** Access uses `System.Data.SqlClient` + `DbHelper` against LocalDB `EduDB.mdf` (`MyDbConn`).

**Docs folder:** `05-Data-Layer/`  
**Auth SQL:** also in `06-Security-Core/` (`AuthService`, `AuthSchema`)

---

## Architecture

```
Pages / ashx / WebMethods
        │
        ├─► LecturerRepository  (courses, works, grades, students)
        ├─► AuthService         (users / MFA / JWT)
        │
        └─► DbHelper  →  SqlConnection  →  App_Data/EduDB.mdf
```

Startup:

```
SchemaBootstrap.EnsureAll()
  → AuthSchema / CourseSchema / DbIndexes
```

---

## Files

| Source | Doc |
|--------|-----|
| DbHelper.cs | [Data__DbHelper.cs.md](../05-Data-Layer/Data__DbHelper.cs.md) |
| DatabaseHelper.cs | [Data__DatabaseHelper.cs.md](../05-Data-Layer/Data__DatabaseHelper.cs.md) |
| LecturerRepository.cs | [Data__LecturerRepository.cs.md](../05-Data-Layer/Data__LecturerRepository.cs.md) |
| Models.cs | [Data__Models.cs.md](../05-Data-Layer/Data__Models.cs.md) |
| CourseSchema.cs | [Data__CourseSchema.cs.md](../05-Data-Layer/Data__CourseSchema.cs.md) |
| SchemaMap.cs | [Data__SchemaMap.cs.md](../05-Data-Layer/Data__SchemaMap.cs.md) |
| SchemaBootstrap.cs | [Data__SchemaBootstrap.cs.md](../05-Data-Layer/Data__SchemaBootstrap.cs.md) |
| DbIndexes.cs | [Data__DbIndexes.cs.md](../05-Data-Layer/Data__DbIndexes.cs.md) |

---

## Main tables

| Table | Role |
|-------|------|
| Users | Auth identity, hash, MFA secret |
| Courses | LecturerUID, IsPublished, … |
| Chapters / SubChapters / StudyMats | Curriculum |
| CourseWorks | Assignments + DueDate + Description META |
| CWSubmissions | Student answers |
| CWMarkings | Grades |
| Enrollments | Student ↔ course |

---

## DbHelper pattern

```csharp
var dt = DbHelper.ExecuteQuery(
    "SELECT … FROM Courses WHERE LecturerUID=@L",
    DbHelper.P("@L", lecturerUid));
```

Always use parameters (`DbHelper.P`) — never concatenate user input into SQL.

---

[← Full index](00-INDEX.md) · [Security overview](01-SECURITY-OVERVIEW.md)
