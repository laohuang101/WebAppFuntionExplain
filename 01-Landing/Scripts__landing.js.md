# landing.js
**Source:** `Pages/Landing/Scripts/landing.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Public marketing + course catalog. Shows published courses only (`IsPublished`). Guests can browse; Enroll sends unauthenticated users to Login.

## File overview

- **Total lines:** 204
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `sections` | `const/let/var` | Often a collection related to sections (plural name). |
| `track` | `const/let/var` | Holds “track” for this scope. |
| `ids` | `const/let/var` | Holds “ids” for this scope. |
| `index` | `const/let/var` | Holds “index” for this scope. |
| `locked` | `const/let/var` | Account locked by LoginThrottle. |
| `touchY` | `const/let/var` | Holds “touch Y” for this scope. |
| `DURATION` | `const/let/var` | Holds “DURATION” for this scope. |
| `prev` | `const/let/var` | Holds “prev” for this scope. |
| `hash` | `const/let/var` | Password hash (PBKDF2) stored in DB. |
| `id` | `const/let/var` | Generic primary key / identifier. |
| `g` | `const/let/var` | Holds “g” for this scope. |
| `root` | `const/let/var` | Root directory path (Uploads). |
| `cTrack` | `const/let/var` | Holds “c Track” for this scope. |
| `prevBtn` | `const/let/var` | Holds “prev Btn” for this scope. |
| `nextBtn` | `const/let/var` | Holds “next Btn” for this scope. |
| `w` | `const/let/var` | Holds “w” for this scope. |
| `n` | `const/let/var` | Numeric count or temporary integer. |
| `show` | `const/let/var` | Holds “show” for this scope. |
| `hideArrows` | `const/let/var` | Collection / list related to hide Arrows. |
| `cards` | `const/let/var` | Often a collection related to cards (plural name). |
| `wheelAcc` | `const/let/var` | Holds “wheel Acc” for this scope. |
| `wheelTimer` | `const/let/var` | Date/time value. |
| `t` | `const/let/var` | Temporary string/token/time value. |
| `dir` | `const/let/var` | Filesystem or URL path. |
| `key` | `const/let/var` | HMAC key bytes or dictionary key. |
| `y` | `const/let/var` | Holds “y” for this scope. |
| `dy` | `const/let/var` | Holds “dy” for this scope. |
| `el` | `const/let/var` | Generic DOM element. |
| `i` | `const/let/var` | Loop index (0-based counter in for-loops). |
| `h` | `const/let/var` | Holds “h” for this scope. |

## Functions / methods (8 found)

### `clamp` — lines 8–12

#### Signature

```javascript
function clamp(i)
```

#### What it is

Function `clamp` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `clamp`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
   8 | 
   9 | 
  10 |         function clamp(i) {
  11 |             return Math.max(0, Math.min(ids.length - 1, i));
  12 |         }
```

---

### `goTo` — lines 12–53

#### Signature

```javascript
function goTo(i, pushHash)
```

#### What it is

Function `goTo` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `goTo`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `i` | `—` | Loop index (0-based counter in for-loops). |
| `pushHash` | `—` | Cryptographic hash string. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `prev` | `—` | Holds “prev” for this scope. |
| `hash` | `—` | Password hash (PBKDF2) stored in DB.  Literal text string. |

#### Code

```javascript
  12 | 
  13 | 
  14 |         function goTo(i, pushHash) {
  15 |             i = clamp(i);
  16 |             var prev = index;
  17 |             if (i === prev && document.location.hash === '#' + ids[i]) {
  18 |                 updateChrome(i);
  19 |                 return;
  20 |             }
  21 | 
  22 |             locked = true;
  23 | 
  24 |             // mark leaving on previous
  25 |             sections.forEach(function (s, n) {
  26 |                 s.classList.remove('is-active', 'is-leaving');
  27 |                 if (n === prev && n !== i) s.classList.add('is-leaving');
  28 |             });
  29 | 
  30 |             track.style.transform = 'translate3d(0, -' + (i * 100) + 'vh, 0)';
  31 |             index = i;
  32 | 
  33 |             // Activate new section so cards fly in as the panel arrives
  34 |             window.setTimeout(function () {
  35 |                 sections.forEach(function (s, n) {
  36 |                     s.classList.remove('is-leaving');
  37 |                     s.classList.toggle('is-active', n === i);
  38 |                 });
  39 |             }, 280);
  40 | 
  41 |             updateChrome(i);
  42 | 
  43 |             if (pushHash !== false) {
  44 |                 var hash = '#' + ids[i];
  45 |                 if (history.replaceState) {
  46 |                     history.replaceState(null, '', hash);
  47 |                 } else {
  48 |                     location.hash = hash;
  49 |                 }
  50 |             }
  51 | 
  52 |             window.setTimeout(function () { locked = false; }, DURATION);
  53 |         }
```

---

### `updateChrome` — lines 53–63

#### Signature

```javascript
function updateChrome(i)
```

#### What it is

Saves or updates **update Chrome** in the database or UI state.

#### How it works

1. Starts when something calls `updateChrome`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `id` | `—` | Generic primary key / identifier. |
| `g` | `—` | Holds “g” for this scope. |

#### Code

```javascript
  53 | 
  54 | 
  55 |         function updateChrome(i) {
  56 |             var id = ids[i];
  57 |             document.querySelectorAll('[data-goto]').forEach(function (el) {
  58 |                 var g = el.getAttribute('data-goto');
  59 |                 if (el.classList.contains('nav-link-soft') || el.closest('#fpNav')) {
  60 |                     el.classList.toggle('active', g === id);
  61 |                 }
  62 |             });
  63 |         }
```

---

### `goBy` — lines 63–68

#### Signature

```javascript
function goBy(delta)
```

#### What it is

Function `goBy` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `goBy`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `delta` | `—` | Holds “delta” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```javascript
  63 | 
  64 | 
  65 |         function goBy(delta) {
  66 |             if (locked) return;
  67 |             goTo(index + delta);
  68 |         }
```

---

### `visibleCap` — lines 77–86

#### Signature

```javascript
function visibleCap()
```

#### What it is

Function `visibleCap` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `visibleCap`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `w` | `—` | Holds “w” for this scope. |

#### Code

```javascript
  77 | 
  78 | 
  79 |             function visibleCap() {
  80 |                 var w = window.innerWidth;
  81 |                 if (w <= 480) return 1;
  82 |                 if (w <= 700) return 2;
  83 |                 if (w <= 960) return 3;
  84 |                 if (w <= 1200) return 4;
  85 |                 return 5;
  86 |             }
```

---

### `layout` — lines 86–96

#### Signature

```javascript
function layout()
```

#### What it is

Function `layout` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `layout`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `n` | `—` | Integer count (rows, items, or length). |
| `show` | `—` | Holds “show” for this scope. |
| `hideArrows` | `—` | Collection / list related to hide Arrows. |

#### Code

```javascript
  86 | 
  87 | 
  88 |             function layout() {
  89 |                 var n = cTrack.querySelectorAll('.course-card').length;
  90 |                 var show = Math.max(1, Math.min(n, visibleCap()));
  91 |                 root.style.setProperty('--cc-visible', String(show));
  92 |                 // hide arrows when everything fits
  93 |                 var hideArrows = n <= show;
  94 |                 if (prevBtn) prevBtn.style.visibility = hideArrows ? 'hidden' : 'visible';
  95 |                 if (nextBtn) nextBtn.style.visibility = hideArrows ? 'hidden' : 'visible';
  96 |             }
```

---

### `step` — lines 96–106

#### Signature

```javascript
function step(dir)
```

#### What it is

Function `step` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Validate input; if invalid, stop and return an error/message.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `dir` | `—` | Filesystem or URL path. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cards` | `—` | Often a collection related to cards (plural name). |

#### Code

```javascript
  96 | 
  97 | 
  98 |             function step(dir) {
  99 |                 var cards = cTrack.querySelectorAll('.course-card');
 100 |                 if (cards.length <= 1) return;
 101 |                 if (dir > 0) {
 102 |                     cTrack.appendChild(cTrack.firstElementChild);
 103 |                 } else {
 104 |                     cTrack.insertBefore(cTrack.lastElementChild, cTrack.firstElementChild);
 105 |                 }
 106 |             }
```

---

### `fromHash` — lines 186–192

#### Signature

```javascript
function fromHash()
```

#### What it is

Function `fromHash` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `fromHash`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `h` | `—` | Holds “h” for this scope. |
| `i` | `—` | Loop index (0-based counter in for-loops). |

#### Code

```javascript
 186 | 
 187 |         function fromHash() {
 188 |             var h = (location.hash || '#home').replace(/^#/, '');
 189 |             var i = ids.indexOf(h);
 190 |             if (i < 0) i = 0;
 191 |             goTo(i, false);
 192 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

```javascript
   1 |     (function () {
   2 |         var sections = Array.prototype.slice.call(document.querySelectorAll('.fp-section'));
   3 |         var track = document.getElementById('fpTrack');
   4 |         var ids = sections.map(function (s) { return s.getAttribute('data-section'); });
   5 |         var index = 0;
   6 |         var locked = false;
   7 |         var touchY = 0;
   8 |         var DURATION = 1400;
   9 | 
  10 |         function clamp(i) {
  11 |             return Math.max(0, Math.min(ids.length - 1, i));
  12 |         }
  13 | 
  14 |         function goTo(i, pushHash) {
  15 |             i = clamp(i);
  16 |             var prev = index;
  17 |             if (i === prev && document.location.hash === '#' + ids[i]) {
  18 |                 updateChrome(i);
  19 |                 return;
  20 |             }
  21 | 
  22 |             locked = true;
  23 | 
  24 |             // mark leaving on previous
  25 |             sections.forEach(function (s, n) {
  26 |                 s.classList.remove('is-active', 'is-leaving');
  27 |                 if (n === prev && n !== i) s.classList.add('is-leaving');
  28 |             });
  29 | 
  30 |             track.style.transform = 'translate3d(0, -' + (i * 100) + 'vh, 0)';
  31 |             index = i;
  32 | 
  33 |             // Activate new section so cards fly in as the panel arrives
  34 |             window.setTimeout(function () {
  35 |                 sections.forEach(function (s, n) {
  36 |                     s.classList.remove('is-leaving');
  37 |                     s.classList.toggle('is-active', n === i);
  38 |                 });
  39 |             }, 280);
  40 | 
  41 |             updateChrome(i);
  42 | 
  43 |             if (pushHash !== false) {
  44 |                 var hash = '#' + ids[i];
  45 |                 if (history.replaceState) {
  46 |                     history.replaceState(null, '', hash);
  47 |                 } else {
  48 |                     location.hash = hash;
  49 |                 }
  50 |             }
  51 | 
  52 |             window.setTimeout(function () { locked = false; }, DURATION);
  53 |         }
  54 | 
  55 |         function updateChrome(i) {
  56 |             var id = ids[i];
  57 |             document.querySelectorAll('[data-goto]').forEach(function (el) {
  58 |                 var g = el.getAttribute('data-goto');
  59 |                 if (el.classList.contains('nav-link-soft') || el.closest('#fpNav')) {
  60 |                     el.classList.toggle('active', g === id);
  61 |                 }
  62 |             });
  63 |         }
  64 | 
  65 |         function goBy(delta) {
  66 |             if (locked) return;
  67 |             goTo(index + delta);
  68 |         }
  69 | 
  70 |         /* ── Infinite course carousel (instant, no slide transition) ── */
  71 |         (function initCourseCarousel() {
  72 |             var root = document.getElementById('courseCarousel');
  73 |             var cTrack = document.getElementById('courseTrack');
  74 |             if (!root || !cTrack) return;
  75 | 
  76 |             var prevBtn = root.querySelector('.cc-prev');
  77 |             var nextBtn = root.querySelector('.cc-next');
  78 | 
  79 |             function visibleCap() {
  80 |                 var w = window.innerWidth;
  81 |                 if (w <= 480) return 1;
  82 |                 if (w <= 700) return 2;
  83 |                 if (w <= 960) return 3;
  84 |                 if (w <= 1200) return 4;
  85 |                 return 5;
  86 |             }
  87 | 
  88 |             function layout() {
  89 |                 var n = cTrack.querySelectorAll('.course-card').length;
  90 |                 var show = Math.max(1, Math.min(n, visibleCap()));
  91 |                 root.style.setProperty('--cc-visible', String(show));
  92 |                 // hide arrows when everything fits
  93 |                 var hideArrows = n <= show;
  94 |                 if (prevBtn) prevBtn.style.visibility = hideArrows ? 'hidden' : 'visible';
  95 |                 if (nextBtn) nextBtn.style.visibility = hideArrows ? 'hidden' : 'visible';
  96 |             }
  97 | 
  98 |             function step(dir) {
  99 |                 var cards = cTrack.querySelectorAll('.course-card');
 100 |                 if (cards.length <= 1) return;
 101 |                 if (dir > 0) {
 102 |                     cTrack.appendChild(cTrack.firstElementChild);
 103 |                 } else {
 104 |                     cTrack.insertBefore(cTrack.lastElementChild, cTrack.firstElementChild);
 105 |                 }
 106 |             }
 107 | 
 108 |             if (prevBtn) prevBtn.addEventListener('click', function (e) {
 109 |                 e.preventDefault();
 110 |                 e.stopPropagation();
 111 |                 step(-1);
 112 |             });
 113 |             if (nextBtn) nextBtn.addEventListener('click', function (e) {
 114 |                 e.preventDefault();
 115 |                 e.stopPropagation();
 116 |                 step(1);
 117 |             });
 118 | 
 119 |             layout();
 120 |             window.addEventListener('resize', layout);
 121 |         })();
 122 | 
 123 |         // Wheel
 124 |         var wheelAcc = 0;
 125 |         var wheelTimer = null;
 126 |         window.addEventListener('wheel', function (e) {
 127 |             // don't hijack if user is interacting with form controls
 128 |             var t = e.target;
 129 |             if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;
 130 | 
 131 |             e.preventDefault();
 132 |             if (locked) return;
 133 | 
 134 |             wheelAcc += e.deltaY;
 135 |             if (wheelTimer) clearTimeout(wheelTimer);
 136 |             wheelTimer = setTimeout(function () { wheelAcc = 0; }, 200);
 137 | 
 138 |             if (Math.abs(wheelAcc) < 40) return;
 139 |             var dir = wheelAcc > 0 ? 1 : -1;
 140 |             wheelAcc = 0;
 141 |             goBy(dir);
 142 |         }, { passive: false });
 143 | 
 144 |         // Keyboard
 145 |         window.addEventListener('keydown', function (e) {
 146 |             if (locked) return;
 147 |             var key = e.key;
 148 |             if (key === 'ArrowDown' || key === 'PageDown' || key === ' ') {
 149 |                 e.preventDefault();
 150 |                 goBy(1);
 151 |             } else if (key === 'ArrowUp' || key === 'PageUp') {
 152 |                 e.preventDefault();
 153 |                 goBy(-1);
 154 |             } else if (key === 'Home') {
 155 |                 e.preventDefault();
 156 |                 goTo(0);
 157 |             } else if (key === 'End') {
 158 |                 e.preventDefault();
 159 |                 goTo(ids.length - 1);
 160 |             }
 161 |         });
 162 | 
 163 |         // Touch
 164 |         window.addEventListener('touchstart', function (e) {
 165 |             if (e.touches && e.touches.length) touchY = e.touches[0].clientY;
 166 |         }, { passive: true });
 167 |         window.addEventListener('touchend', function (e) {
 168 |             if (locked) return;
 169 |             var y = e.changedTouches && e.changedTouches[0] ? e.changedTouches[0].clientY : touchY;
 170 |             var dy = touchY - y;
 171 |             if (Math.abs(dy) < 50) return;
 172 |             goBy(dy > 0 ? 1 : -1);
 173 |         }, { passive: true });
 174 | 
 175 |         // Clicks / hash links
 176 |         document.addEventListener('click', function (e) {
 177 |             var el = e.target.closest('[data-goto]');
 178 |             if (!el) return;
 179 |             var id = el.getAttribute('data-goto');
 180 |             var i = ids.indexOf(id);
 181 |             if (i < 0) return;
 182 |             e.preventDefault();
 183 |             goTo(i);
 184 |         });
 185 | 
 186 |         // Hash on load / back-forward
 187 |         function fromHash() {
 188 |             var h = (location.hash || '#home').replace(/^#/, '');
 189 |             var i = ids.indexOf(h);
 190 |             if (i < 0) i = 0;
 191 |             goTo(i, false);
 192 |         }
 193 |         window.addEventListener('hashchange', fromHash);
 194 |         fromHash();
 195 | 
 196 |         // Resize: keep position
 197 |         window.addEventListener('resize', function () {
 198 |             track.style.transition = 'none';
 199 |             track.style.transform = 'translate3d(0, -' + (index * 100) + 'vh, 0)';
 200 |             // force reflow then restore transition
 201 |             void track.offsetHeight;
 202 |             track.style.transition = '';
 203 |         });
 204 |     })();
```
