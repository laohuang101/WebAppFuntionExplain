# SchemaBootstrap.cs
**Source:** `Data/SchemaBootstrap.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

App-start (or first request) orchestration: run AuthSchema, CourseSchema, DbIndexes, and other Ensure* once.

## File overview

- **Total lines:** 28
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `Gate` | `object` | Holds “Gate” for this scope. |
| `_done` | `bool` | Holds “done” for this scope. (true/false) |

## Functions / methods (1 found)

### `EnsureAll` — lines 14–26

#### Signature

```csharp
public static void EnsureAll()
```

#### What it is

Makes sure **All** exists or is valid before the rest of the code continues.

#### How it works

1. Starts when something calls `EnsureAll`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
  14 | 
  15 |         public static void EnsureAll()
  16 |         {
  17 |             if (_done) return;
  18 |             lock (Gate)
  19 |             {
  20 |                 if (_done) return;
  21 |                 try { AuthSchema.Ensure(); } catch { }
  22 |                 try { CourseSchema.Ensure(); } catch { }
  23 |                 try { DbIndexes.Ensure(); } catch { }
  24 |                 _done = true;
  25 |             }
  26 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```csharp
   1 | using System;
   2 | using WebAppAssignment.Data.Security;
   3 | 
   4 | namespace WebAppAssignment.Data
   5 | {
   6 |     /// <summary>
   7 |     /// One-shot schema warmup so pages don't each pay Ensure() costs repeatedly
   8 |     /// (AuthSchema / CourseSchema already short-circuit after first success).
   9 |     /// </summary>
  10 |     public static class SchemaBootstrap
  11 |     {
  12 |         private static readonly object Gate = new object();
  13 |         private static bool _done;
  14 | 
  15 |         public static void EnsureAll()
  16 |         {
  17 |             if (_done) return;
  18 |             lock (Gate)
  19 |             {
  20 |                 if (_done) return;
  21 |                 try { AuthSchema.Ensure(); } catch { }
  22 |                 try { CourseSchema.Ensure(); } catch { }
  23 |                 try { DbIndexes.Ensure(); } catch { }
  24 |                 _done = true;
  25 |             }
  26 |         }
  27 |     }
  28 | }
```
