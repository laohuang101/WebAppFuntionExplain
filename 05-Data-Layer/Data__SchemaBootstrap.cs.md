# SchemaBootstrap.cs
**Source:** `Data/SchemaBootstrap.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 28
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 12:** `Gate` — type `object`
- **Line 13:** `_done` — type `bool`

## Functions / methods (1 found)

### `EnsureAll` — lines 14–26

```
public static void EnsureAll()
```

#### Explanation

- **Purpose:** Implements `EnsureAll`.

#### Line-by-line (this function)

`  14`  ``
`  15`  `        public static void EnsureAll()`
`  16`  `        {`
`  17`  `            if (_done) return;`
`  18`  `            lock (Gate)`
`  19`  `            {`
`  20`  `                if (_done) return;`
`  21`  `                try { AuthSchema.Ensure(); } catch { }`
  - → Error handling block.
`  22`  `                try { CourseSchema.Ensure(); } catch { }`
  - → Error handling block.
`  23`  `                try { DbIndexes.Ensure(); } catch { }`
  - → Error handling block.
`  24`  `                _done = true;`
`  25`  `            }`
`  26`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using WebAppAssignment.Data.Security;`
  - → Import namespace/types.
`   3`  ``
`   4`  `namespace WebAppAssignment.Data`
  - → C# namespace grouping.
`   5`  `{`
`   6`  `    /// <summary>`
`   7`  `    /// One-shot schema warmup so pages don't each pay Ensure() costs repeatedly`
`   8`  `    /// (AuthSchema / CourseSchema already short-circuit after first success).`
`   9`  `    /// </summary>`
`  10`  `    public static class SchemaBootstrap`
`  11`  `    {`
`  12`  `        private static readonly object Gate = new object();`
`  13`  `        private static bool _done;`
`  14`  ``
`  15`  `        public static void EnsureAll()`
`  16`  `        {`
`  17`  `            if (_done) return;`
`  18`  `            lock (Gate)`
`  19`  `            {`
`  20`  `                if (_done) return;`
`  21`  `                try { AuthSchema.Ensure(); } catch { }`
  - → Error handling block.
`  22`  `                try { CourseSchema.Ensure(); } catch { }`
  - → Error handling block.
`  23`  `                try { DbIndexes.Ensure(); } catch { }`
  - → Error handling block.
`  24`  `                _done = true;`
`  25`  `            }`
`  26`  `        }`
`  27`  `    }`
`  28`  `}`

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
