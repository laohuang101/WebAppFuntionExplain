# SchemaBootstrap.cs
**Source:** `Data/SchemaBootstrap.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

App-start (or first request) orchestration: run AuthSchema, CourseSchema, DbIndexes, and other Ensure* once.

## File overview

- **Total lines:** 28
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 12:** `Gate` (`object`) — **Holds “Gate” for this scope.**
- **Line 13:** `_done` (`bool`) — **Holds “done” for this scope. (true/false)**

## Functions / methods (1 found)

### `EnsureAll` — lines 14–26

```csharp
public static void EnsureAll()
```

#### Explanation

- **Purpose:** Implements `EnsureAll`.

#### Line-by-line (this function)

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

**Line notes** (what code + variables mean)

- **L21:** Error handling block.
- **L22:** Error handling block.
- **L23:** Error handling block.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

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

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L4:** C# namespace grouping.
- **L21:** Error handling block.
- **L22:** Error handling block.
- **L23:** Error handling block.

## Source snapshot (raw)

```csharp
using System;
using WebAppAssignment.Data.Security;

namespace WebAppAssignment.Data
{
    /// <summary>
    /// One-shot schema warmup so pages don't each pay Ensure() costs repeatedly
    /// (AuthSchema / CourseSchema already short-circuit after first success).
    /// </summary>
    public static class SchemaBootstrap
    {
        private static readonly object Gate = new object();
        private static bool _done;

        public static void EnsureAll()
        {
            if (_done) return;
            lock (Gate)
            {
                if (_done) return;
                try { AuthSchema.Ensure(); } catch { }
                try { CourseSchema.Ensure(); } catch { }
                try { DbIndexes.Ensure(); } catch { }
                _done = true;
            }
        }
    }
}

```
