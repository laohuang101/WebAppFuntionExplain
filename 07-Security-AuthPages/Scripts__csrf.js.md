# csrf.js
**Source:** `Shared/Scripts/csrf.js`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Client helper: attach X-CSRF-Token header to fetch/XHR from meta/cookie.

## File overview

- **Total lines:** 65
- **Kind:** `.js`

## Variables / fields (file level)

- **Line 9:** `m` — script-level `const`/`let`/`var`
- **Line 14:** `meta` — script-level `const`/`let`/`var`
- **Line 26:** `h` — script-level `const`/`let`/`var`
- **Line 33:** `_fetch` — script-level `const`/`let`/`var`
- **Line 36:** `method` — script-level `const`/`let`/`var`
- **Line 47:** `_open` — script-level `const`/`let`/`var`
- **Line 48:** `_send` — script-level `const`/`let`/`var`

## Functions / methods (3 found)

### `readCookie` — lines 6–11

```javascript
function readCookie(name)
```

#### Explanation

- **Purpose:** Implements `readCookie`.
- **Parameters:** `name`
- **Local variables:** `m`

#### Line-by-line (this function)

```javascript
   6 | 
   7 | 
   8 |     function readCookie(name) {
   9 |         var m = document.cookie.match(new RegExp('(?:^|; )' + name.replace(/\./g, '\\.') + '=([^;]*)'));
  10 |         return m ? decodeURIComponent(m[1]) : '';
  11 |     }
```

---

### `getToken` — lines 11–17

```javascript
function getToken()
```

#### Explanation

- **Purpose:** Implements `getToken`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Pattern:** Read/load data for display.
- **Local variables:** `meta`

#### Line-by-line (this function)

```javascript
  11 | 
  12 | 
  13 |     function getToken() {
  14 |         var meta = document.querySelector('meta[name="csrf-token"]');
  15 |         if (meta && meta.content) return meta.content;
  16 |         return readCookie('EduLMS.Csrf') || (global.__CSRF_TOKEN__ || '');
  17 |     }
```

**Line notes**

- **L14:** CSRF anti-forgery protection.
- **L16:** CSRF anti-forgery protection.

---

### `applyHeaders` — lines 17–29

```javascript
function applyHeaders(headers, token)
```

#### Explanation

- **Purpose:** Implements `applyHeaders`.
- **CSRF:** Validates anti-forgery token on mutating request.
- **Parameters:** `headers, token`
- **Local variables:** `h`

#### Line-by-line (this function)

```javascript
  17 | 
  18 | 
  19 |     function applyHeaders(headers, token) {
  20 |         if (!token) return headers;
  21 |         if (!headers) headers = {};
  22 |         if (typeof Headers !== 'undefined' && headers instanceof Headers) {
  23 |             if (!headers.has('X-CSRF-Token')) headers.set('X-CSRF-Token', token);
  24 |             return headers;
  25 |         }
  26 |         var h = headers;
  27 |         if (!h['X-CSRF-Token'] && !h['x-csrf-token']) h['X-CSRF-Token'] = token;
  28 |         return h;
  29 |     }
```

**Line notes**

- **L23:** CSRF token ensure/validate.
- **L27:** CSRF anti-forgery protection.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```javascript
   1 | /**
   2 |  * EduLMS CSRF helper — attaches X-CSRF-Token to mutating fetch/XHR.
   3 |  * Token from <meta name="csrf-token"> or EduLMS.Csrf cookie.
   4 |  */
   5 | (function (global) {
   6 |     'use strict';
   7 | 
   8 |     function readCookie(name) {
   9 |         var m = document.cookie.match(new RegExp('(?:^|; )' + name.replace(/\./g, '\\.') + '=([^;]*)'));
  10 |         return m ? decodeURIComponent(m[1]) : '';
  11 |     }
  12 | 
  13 |     function getToken() {
  14 |         var meta = document.querySelector('meta[name="csrf-token"]');
  15 |         if (meta && meta.content) return meta.content;
  16 |         return readCookie('EduLMS.Csrf') || (global.__CSRF_TOKEN__ || '');
  17 |     }
  18 | 
  19 |     function applyHeaders(headers, token) {
  20 |         if (!token) return headers;
  21 |         if (!headers) headers = {};
  22 |         if (typeof Headers !== 'undefined' && headers instanceof Headers) {
  23 |             if (!headers.has('X-CSRF-Token')) headers.set('X-CSRF-Token', token);
  24 |             return headers;
  25 |         }
  26 |         var h = headers;
  27 |         if (!h['X-CSRF-Token'] && !h['x-csrf-token']) h['X-CSRF-Token'] = token;
  28 |         return h;
  29 |     }
  30 | 
  31 |     // Patch fetch
  32 |     if (typeof global.fetch === 'function') {
  33 |         var _fetch = global.fetch;
  34 |         global.fetch = function (input, init) {
  35 |             init = init || {};
  36 |             var method = (init.method || 'GET').toUpperCase();
  37 |             if (method !== 'GET' && method !== 'HEAD' && method !== 'OPTIONS') {
  38 |                 init.headers = applyHeaders(init.headers || {}, getToken());
  39 |             }
  40 |             if (!init.credentials) init.credentials = 'same-origin';
  41 |             return _fetch.call(this, input, init);
  42 |         };
  43 |     }
  44 | 
  45 |     // Patch XHR open/send
  46 |     if (global.XMLHttpRequest) {
  47 |         var _open = XMLHttpRequest.prototype.open;
  48 |         var _send = XMLHttpRequest.prototype.send;
  49 |         XMLHttpRequest.prototype.open = function (method) {
  50 |             this.__csrfMethod = (method || 'GET').toUpperCase();
  51 |             return _open.apply(this, arguments);
  52 |         };
  53 |         XMLHttpRequest.prototype.send = function () {
  54 |             try {
  55 |                 var m = this.__csrfMethod || 'GET';
  56 |                 if (m !== 'GET' && m !== 'HEAD' && m !== 'OPTIONS') {
  57 |                     this.setRequestHeader('X-CSRF-Token', getToken());
  58 |                 }
  59 |             } catch (e) { /* header may already be set */ }
  60 |             return _send.apply(this, arguments);
  61 |         };
  62 |     }
  63 | 
  64 |     global.EduCsrf = { getToken: getToken };
  65 | })(window);
```

**Line notes**

- **L14:** CSRF anti-forgery protection.
- **L16:** CSRF anti-forgery protection.
- **L23:** CSRF token ensure/validate.
- **L27:** CSRF anti-forgery protection.
- **L50:** CSRF anti-forgery protection.
- **L54:** Error handling block.
- **L55:** CSRF anti-forgery protection.
- **L57:** CSRF token ensure/validate.
- **L64:** CSRF anti-forgery protection.

## Source snapshot (raw)

```javascript
/**
 * EduLMS CSRF helper — attaches X-CSRF-Token to mutating fetch/XHR.
 * Token from <meta name="csrf-token"> or EduLMS.Csrf cookie.
 */
(function (global) {
    'use strict';

    function readCookie(name) {
        var m = document.cookie.match(new RegExp('(?:^|; )' + name.replace(/\./g, '\\.') + '=([^;]*)'));
        return m ? decodeURIComponent(m[1]) : '';
    }

    function getToken() {
        var meta = document.querySelector('meta[name="csrf-token"]');
        if (meta && meta.content) return meta.content;
        return readCookie('EduLMS.Csrf') || (global.__CSRF_TOKEN__ || '');
    }

    function applyHeaders(headers, token) {
        if (!token) return headers;
        if (!headers) headers = {};
        if (typeof Headers !== 'undefined' && headers instanceof Headers) {
            if (!headers.has('X-CSRF-Token')) headers.set('X-CSRF-Token', token);
            return headers;
        }
        var h = headers;
        if (!h['X-CSRF-Token'] && !h['x-csrf-token']) h['X-CSRF-Token'] = token;
        return h;
    }

    // Patch fetch
    if (typeof global.fetch === 'function') {
        var _fetch = global.fetch;
        global.fetch = function (input, init) {
            init = init || {};
            var method = (init.method || 'GET').toUpperCase();
            if (method !== 'GET' && method !== 'HEAD' && method !== 'OPTIONS') {
                init.headers = applyHeaders(init.headers || {}, getToken());
            }
            if (!init.credentials) init.credentials = 'same-origin';
            return _fetch.call(this, input, init);
        };
    }

    // Patch XHR open/send
    if (global.XMLHttpRequest) {
        var _open = XMLHttpRequest.prototype.open;
        var _send = XMLHttpRequest.prototype.send;
        XMLHttpRequest.prototype.open = function (method) {
            this.__csrfMethod = (method || 'GET').toUpperCase();
            return _open.apply(this, arguments);
        };
        XMLHttpRequest.prototype.send = function () {
            try {
                var m = this.__csrfMethod || 'GET';
                if (m !== 'GET' && m !== 'HEAD' && m !== 'OPTIONS') {
                    this.setRequestHeader('X-CSRF-Token', getToken());
                }
            } catch (e) { /* header may already be set */ }
            return _send.apply(this, arguments);
        };
    }

    global.EduCsrf = { getToken: getToken };
})(window);

```
