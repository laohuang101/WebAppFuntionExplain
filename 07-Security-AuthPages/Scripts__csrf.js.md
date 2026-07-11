# csrf.js
**Source:** `Shared/Scripts/csrf.js`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Client helper: attach X-CSRF-Token header to fetch/XHR from meta/cookie.

## File overview

- **Total lines:** 65
- **Kind:** `.js`

## Variables / fields (file level)

Simple table of names declared at file/class level.

| Variable | Type | What it is |
|----------|------|------------|
| `m` | `const/let/var` | Holds “m” for this scope. |
| `meta` | `const/let/var` | Extra settings packed as JSON (dueDate, requireFile, …). |
| `h` | `const/let/var` | Holds “h” for this scope. |
| `_fetch` | `const/let/var` | Holds “fetch” for this scope. |
| `method` | `const/let/var` | HTTP method (GET/POST) or MFA method (totp/email). |
| `_open` | `const/let/var` | Holds “open” for this scope. |
| `_send` | `const/let/var` | Holds “send” for this scope. |

## Functions / methods (3 found)

### `readCookie` — lines 6–11

#### Signature

```javascript
function readCookie(name)
```

#### What it is

Reads/loads data related to **read Cookie** and returns it for display or further use.

#### How it works

1. Starts when something calls `readCookie`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `name` | `—` | Display name of user/course/criterion. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `m` | `—` | Holds “m” for this scope.  Newly constructed object. |

#### Code

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

#### Signature

```javascript
function getToken()
```

#### What it is

Reads/loads data related to **Token** and returns it for display or further use.

#### How it works

1. Starts when something calls `getToken`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `meta` | `—` | Extra settings packed as JSON (dueDate, requireFile, …). |

#### Code

```javascript
  11 | 
  12 | 
  13 |     function getToken() {
  14 |         var meta = document.querySelector('meta[name="csrf-token"]');
  15 |         if (meta && meta.content) return meta.content;
  16 |         return readCookie('EduLMS.Csrf') || (global.__CSRF_TOKEN__ || '');
  17 |     }
```

---

### `applyHeaders` — lines 17–29

#### Signature

```javascript
function applyHeaders(headers, token)
```

#### What it is

Function `applyHeaders` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `applyHeaders`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `headers` | `—` | HTTP headers object for fetch. |
| `token` | `—` | JWT or CSRF token string. |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `h` | `—` | Holds “h” for this scope. |

#### Code

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

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
