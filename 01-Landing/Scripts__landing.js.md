# landing.js
**Source:** `Pages/Landing/Scripts/landing.js`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Public marketing + course catalog. Shows published courses only (`IsPublished`). Guests can browse; Enroll sends unauthenticated users to Login.

## File overview

- **Total lines:** 204
- **Kind:** `.js`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 2:** `sections` — script-level `const`/`let`/`var` — **Often a collection related to sections (plural name).**
- **Line 3:** `track` — script-level `const`/`let`/`var` — **Holds “track” for this scope.**
- **Line 4:** `ids` — script-level `const`/`let`/`var` — **Holds “ids” for this scope.**
- **Line 5:** `index` — script-level `const`/`let`/`var` — **Holds “index” for this scope.**
- **Line 6:** `locked` — script-level `const`/`let`/`var` — **Account locked by LoginThrottle.**
- **Line 7:** `touchY` — script-level `const`/`let`/`var` — **Holds “touch Y” for this scope.**
- **Line 8:** `DURATION` — script-level `const`/`let`/`var` — **Holds “DURATION” for this scope.**
- **Line 16:** `prev` — script-level `const`/`let`/`var` — **Holds “prev” for this scope.**
- **Line 44:** `hash` — script-level `const`/`let`/`var` — **Password hash (PBKDF2) stored in DB.**
- **Line 56:** `id` — script-level `const`/`let`/`var` — **Generic primary key / identifier.**
- **Line 58:** `g` — script-level `const`/`let`/`var` — **Holds “g” for this scope.**
- **Line 72:** `root` — script-level `const`/`let`/`var` — **Root directory path (Uploads).**
- **Line 73:** `cTrack` — script-level `const`/`let`/`var` — **Holds “c Track” for this scope.**
- **Line 75:** `prevBtn` — script-level `const`/`let`/`var` — **Holds “prev Btn” for this scope.**
- **Line 77:** `nextBtn` — script-level `const`/`let`/`var` — **Holds “next Btn” for this scope.**
- **Line 80:** `w` — script-level `const`/`let`/`var` — **Holds “w” for this scope.**
- **Line 89:** `n` — script-level `const`/`let`/`var` — **Numeric count or temporary integer.**
- **Line 90:** `show` — script-level `const`/`let`/`var` — **Holds “show” for this scope.**
- **Line 93:** `hideArrows` — script-level `const`/`let`/`var` — **Collection / list related to hide Arrows.**
- **Line 99:** `cards` — script-level `const`/`let`/`var` — **Often a collection related to cards (plural name).**
- **Line 124:** `wheelAcc` — script-level `const`/`let`/`var` — **Holds “wheel Acc” for this scope.**
- **Line 125:** `wheelTimer` — script-level `const`/`let`/`var` — **Date/time value.**
- **Line 128:** `t` — script-level `const`/`let`/`var` — **Temporary string/token/time value.**
- **Line 139:** `dir` — script-level `const`/`let`/`var` — **Filesystem or URL path.**
- **Line 147:** `key` — script-level `const`/`let`/`var` — **HMAC key bytes or dictionary key.**
- **Line 169:** `y` — script-level `const`/`let`/`var` — **Holds “y” for this scope.**
- **Line 170:** `dy` — script-level `const`/`let`/`var` — **Holds “dy” for this scope.**
- **Line 177:** `el` — script-level `const`/`let`/`var` — **Generic DOM element.**
- **Line 180:** `i` — script-level `const`/`let`/`var` — **Loop index (0-based counter in for-loops).**
- **Line 188:** `h` — script-level `const`/`let`/`var` — **Holds “h” for this scope.**

## Functions / methods (8 found)

### `clamp` — lines 8–12

```javascript
function clamp(i)
```

#### Explanation

- **Purpose:** Implements `clamp`.
- **Parameters (what each means):**
- `i` — Loop index (0-based counter in for-loops).

#### Line-by-line (this function)

```javascript
   8 | 
   9 | 
  10 |         function clamp(i) {
  11 |             return Math.max(0, Math.min(ids.length - 1, i));
  12 |         }
```

---

### `goTo` — lines 12–53

```javascript
function goTo(i, pushHash)
```

#### Explanation

- **Purpose:** Implements `goTo`.
- **Parameters (what each means):**
- `i` — Loop index (0-based counter in for-loops).
- `pushHash` — Cryptographic hash string.
- **Local variables (what each means):**
- `prev` — Holds “prev” for this scope.
- `hash` — Password hash (PBKDF2) stored in DB.  Literal text string.

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L16:** `prev` means: Holds “prev” for this scope.
- **L44:** `hash` means: Password hash (PBKDF2) stored in DB.  Literal text string.
>>>>>>> eb8ce01 (update)

---

### `updateChrome` — lines 53–63

```javascript
function updateChrome(i)
```

#### Explanation

- **Purpose:** Implements `updateChrome`.
- **Pattern:** Persist changes.
- **Parameters (what each means):**
- `i` — Loop index (0-based counter in for-loops).
- **Local variables (what each means):**
- `id` — Generic primary key / identifier.
- `g` — Holds “g” for this scope.

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L56:** `id` means: Generic primary key / identifier.
- **L58:** `g` means: Holds “g” for this scope.
>>>>>>> eb8ce01 (update)

---

### `goBy` — lines 63–68

```javascript
function goBy(delta)
```

#### Explanation

- **Purpose:** Implements `goBy`.
- **Parameters (what each means):**
- `delta` — Holds “delta” for this scope.

#### Line-by-line (this function)

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

```javascript
function visibleCap()
```

#### Explanation

- **Purpose:** Implements `visibleCap`.
- **Local variables (what each means):**
- `w` — Holds “w” for this scope.

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L80:** `w` means: Holds “w” for this scope.
>>>>>>> eb8ce01 (update)

---

### `layout` — lines 86–96

```javascript
function layout()
```

#### Explanation

- **Purpose:** Implements `layout`.
- **Local variables (what each means):**
- `n` — Integer count (rows, items, or length).
- `show` — Holds “show” for this scope.
- `hideArrows` — Collection / list related to hide Arrows.

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L89:** `n` means: Integer count (rows, items, or length).
- **L90:** `show` means: Holds “show” for this scope.
- **L93:** `hideArrows` means: Collection / list related to hide Arrows.
>>>>>>> eb8ce01 (update)

---

### `step` — lines 96–106

```javascript
function step(dir)
```

#### Explanation

- **Purpose:** Implements `step`.
- **Parameters (what each means):**
- `dir` — Filesystem or URL path.
- **Local variables (what each means):**
- `cards` — Often a collection related to cards (plural name).

#### Line-by-line (this function)

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
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L99:** `cards` means: Often a collection related to cards (plural name).
>>>>>>> eb8ce01 (update)

---

### `fromHash` — lines 186–192

```javascript
function fromHash()
```

#### Explanation

- **Purpose:** Implements `fromHash`.
- **Local variables (what each means):**
- `h` — Holds “h” for this scope.
- `i` — Loop index (0-based counter in for-loops).

#### Line-by-line (this function)

```javascript
 186 | 
 187 |         function fromHash() {
 188 |             var h = (location.hash || '#home').replace(/^#/, '');
 189 |             var i = ids.indexOf(h);
 190 |             if (i < 0) i = 0;
 191 |             goTo(i, false);
 192 |         }
```
<<<<<<< HEAD
=======

**Line notes** (what code + variables mean)

- **L188:** `h` means: Holds “h” for this scope.
- **L189:** `i` means: Loop index (0-based counter in for-loops).
>>>>>>> eb8ce01 (update)

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

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

**Line notes**

<<<<<<< HEAD
- **L3:** Get HTML element by id.
- **L72:** Get HTML element by id.
- **L73:** Get HTML element by id.
- **L108:** DOM event handler.
- **L113:** DOM event handler.
- **L120:** DOM event handler.
- **L126:** DOM event handler.
- **L145:** DOM event handler.
- **L164:** DOM event handler.
- **L167:** DOM event handler.
- **L176:** DOM event handler.
=======
- **L2:** `sections` means: Often a collection related to sections (plural name).
- **L3:** Get HTML element by id. | `track` means: Holds “track” for this scope.  DOM element from the page.
- **L4:** `ids` means: Holds “ids” for this scope.
- **L5:** `index` means: Holds “index” for this scope.  Literal number `0`.
- **L6:** `locked` means: Account locked by LoginThrottle.
- **L7:** `touchY` means: Holds “touch Y” for this scope.  Literal number `0`.
- **L8:** `DURATION` means: Holds “DURATION” for this scope.  Literal number `1400`.
- **L16:** `prev` means: Holds “prev” for this scope.
- **L44:** `hash` means: Password hash (PBKDF2) stored in DB.  Literal text string.
- **L56:** `id` means: Generic primary key / identifier.
- **L58:** `g` means: Holds “g” for this scope.
- **L72:** Get HTML element by id. | `root` means: Root directory path (Uploads).  DOM element from the page.
- **L73:** Get HTML element by id. | `cTrack` means: Holds “c Track” for this scope.  DOM element from the page.
- **L76:** `prevBtn` means: Holds “prev Btn” for this scope.
- **L77:** `nextBtn` means: Holds “next Btn” for this scope.
- **L80:** `w` means: Holds “w” for this scope.
- **L89:** `n` means: Integer count (rows, items, or length).
- **L90:** `show` means: Holds “show” for this scope.
- **L93:** `hideArrows` means: Collection / list related to hide Arrows.
- **L99:** `cards` means: Often a collection related to cards (plural name).
- **L108:** DOM event handler.
- **L113:** DOM event handler.
- **L120:** DOM event handler.
- **L124:** `wheelAcc` means: Holds “wheel Acc” for this scope.  Literal number `0`.
- **L125:** `wheelTimer` means: Date/time value.
- **L126:** DOM event handler.
- **L128:** `t` means: Temporary string/token/time value.
- **L139:** `dir` means: Filesystem or URL path.
- **L145:** DOM event handler.
- **L147:** `key` means: HMAC key bytes or dictionary key.
- **L164:** DOM event handler.
- **L167:** DOM event handler.
- **L169:** `y` means: Holds “y” for this scope.
- **L170:** `dy` means: Holds “dy” for this scope.
- **L176:** DOM event handler.
- **L177:** `el` means: Generic DOM element.
- **L179:** `id` means: Generic primary key / identifier.
- **L180:** `i` means: Loop index (0-based counter in for-loops).
- **L188:** `h` means: Holds “h” for this scope.
- **L189:** `i` means: Loop index (0-based counter in for-loops).
>>>>>>> eb8ce01 (update)
- **L193:** DOM event handler.
- **L197:** DOM event handler.

## Source snapshot (raw)

```javascript
    (function () {
        var sections = Array.prototype.slice.call(document.querySelectorAll('.fp-section'));
        var track = document.getElementById('fpTrack');
        var ids = sections.map(function (s) { return s.getAttribute('data-section'); });
        var index = 0;
        var locked = false;
        var touchY = 0;
        var DURATION = 1400;

        function clamp(i) {
            return Math.max(0, Math.min(ids.length - 1, i));
        }

        function goTo(i, pushHash) {
            i = clamp(i);
            var prev = index;
            if (i === prev && document.location.hash === '#' + ids[i]) {
                updateChrome(i);
                return;
            }

            locked = true;

            // mark leaving on previous
            sections.forEach(function (s, n) {
                s.classList.remove('is-active', 'is-leaving');
                if (n === prev && n !== i) s.classList.add('is-leaving');
            });

            track.style.transform = 'translate3d(0, -' + (i * 100) + 'vh, 0)';
            index = i;

            // Activate new section so cards fly in as the panel arrives
            window.setTimeout(function () {
                sections.forEach(function (s, n) {
                    s.classList.remove('is-leaving');
                    s.classList.toggle('is-active', n === i);
                });
            }, 280);

            updateChrome(i);

            if (pushHash !== false) {
                var hash = '#' + ids[i];
                if (history.replaceState) {
                    history.replaceState(null, '', hash);
                } else {
                    location.hash = hash;
                }
            }

            window.setTimeout(function () { locked = false; }, DURATION);
        }

        function updateChrome(i) {
            var id = ids[i];
            document.querySelectorAll('[data-goto]').forEach(function (el) {
                var g = el.getAttribute('data-goto');
                if (el.classList.contains('nav-link-soft') || el.closest('#fpNav')) {
                    el.classList.toggle('active', g === id);
                }
            });
        }

        function goBy(delta) {
            if (locked) return;
            goTo(index + delta);
        }

        /* ── Infinite course carousel (instant, no slide transition) ── */
        (function initCourseCarousel() {
            var root = document.getElementById('courseCarousel');
            var cTrack = document.getElementById('courseTrack');
            if (!root || !cTrack) return;

            var prevBtn = root.querySelector('.cc-prev');
            var nextBtn = root.querySelector('.cc-next');

            function visibleCap() {
                var w = window.innerWidth;
                if (w <= 480) return 1;
                if (w <= 700) return 2;
                if (w <= 960) return 3;
                if (w <= 1200) return 4;
                return 5;
            }

            function layout() {
                var n = cTrack.querySelectorAll('.course-card').length;
                var show = Math.max(1, Math.min(n, visibleCap()));
                root.style.setProperty('--cc-visible', String(show));
                // hide arrows when everything fits
                var hideArrows = n <= show;
                if (prevBtn) prevBtn.style.visibility = hideArrows ? 'hidden' : 'visible';
                if (nextBtn) nextBtn.style.visibility = hideArrows ? 'hidden' : 'visible';
            }

            function step(dir) {
                var cards = cTrack.querySelectorAll('.course-card');
                if (cards.length <= 1) return;
                if (dir > 0) {
                    cTrack.appendChild(cTrack.firstElementChild);
                } else {
                    cTrack.insertBefore(cTrack.lastElementChild, cTrack.firstElementChild);
                }
            }

            if (prevBtn) prevBtn.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                step(-1);
            });
            if (nextBtn) nextBtn.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                step(1);
            });

            layout();
            window.addEventListener('resize', layout);
        })();

        // Wheel
        var wheelAcc = 0;
        var wheelTimer = null;
        window.addEventListener('wheel', function (e) {
            // don't hijack if user is interacting with form controls
            var t = e.target;
            if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;

            e.preventDefault();
            if (locked) return;

            wheelAcc += e.deltaY;
            if (wheelTimer) clearTimeout(wheelTimer);
            wheelTimer = setTimeout(function () { wheelAcc = 0; }, 200);

            if (Math.abs(wheelAcc) < 40) return;
            var dir = wheelAcc > 0 ? 1 : -1;
            wheelAcc = 0;
            goBy(dir);
        }, { passive: false });

        // Keyboard
        window.addEventListener('keydown', function (e) {
            if (locked) return;
            var key = e.key;
            if (key === 'ArrowDown' || key === 'PageDown' || key === ' ') {
                e.preventDefault();
                goBy(1);
            } else if (key === 'ArrowUp' || key === 'PageUp') {
                e.preventDefault();
                goBy(-1);
            } else if (key === 'Home') {
                e.preventDefault();
                goTo(0);
            } else if (key === 'End') {
                e.preventDefault();
                goTo(ids.length - 1);
            }
        });

        // Touch
        window.addEventListener('touchstart', function (e) {
            if (e.touches && e.touches.length) touchY = e.touches[0].clientY;
        }, { passive: true });
        window.addEventListener('touchend', function (e) {
            if (locked) return;
            var y = e.changedTouches && e.changedTouches[0] ? e.changedTouches[0].clientY : touchY;
            var dy = touchY - y;
            if (Math.abs(dy) < 50) return;
            goBy(dy > 0 ? 1 : -1);
        }, { passive: true });

        // Clicks / hash links
        document.addEventListener('click', function (e) {
            var el = e.target.closest('[data-goto]');
            if (!el) return;
            var id = el.getAttribute('data-goto');
            var i = ids.indexOf(id);
            if (i < 0) return;
            e.preventDefault();
            goTo(i);
        });

        // Hash on load / back-forward
        function fromHash() {
            var h = (location.hash || '#home').replace(/^#/, '');
            var i = ids.indexOf(h);
            if (i < 0) i = 0;
            goTo(i, false);
        }
        window.addEventListener('hashchange', fromHash);
        fromHash();

        // Resize: keep position
        window.addEventListener('resize', function () {
            track.style.transition = 'none';
            track.style.transform = 'translate3d(0, -' + (index * 100) + 'vh, 0)';
            // force reflow then restore transition
            void track.offsetHeight;
            track.style.transition = '';
        });
    })();

```
