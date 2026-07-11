# CoursePreview.aspx
**Source:** `Pages/Lecturer/CoursePreview.aspx`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 445
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `<%@ Page Title="Course Preview" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="CoursePreview.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.CoursePreview" %>`
`   2`  ``
`   3`  `<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">`
`   4`  `  <link rel="stylesheet" href="Style/course-preview.css" />`
`   5`  `</asp:Content>`
`   6`  ``
`   7`  `<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">`
`   8`  `  <div class="course-preview-page" id="previewRoot">`
`   9`  `    <div class="text-center py-5 text-muted" id="previewLoading">`
`  10`  `      <i class="fa-solid fa-circle-notch fa-spin me-2"></i> Loading course preview...`
`  11`  `    </div>`
`  12`  `    <div id="previewError" class="alert alert-danger d-none"></div>`
`  13`  ``
`  14`  `    <div id="previewBody" class="d-none">`
`  15`  `      <!-- Top bar -->`
`  16`  `      <div class="preview-topbar">`
`  17`  `        <div class="d-flex align-items-center gap-3 min-w-0">`
`  18`  `          <a href="CourseCreation.aspx" class="preview-back" title="Back to My Courses">`
`  19`  `            <i class="fa-solid fa-chevron-left"></i>`
`  20`  `          </a>`
`  21`  `          <div class="min-w-0">`
`  22`  `            <h1 class="preview-title text-truncate" id="pvTitle">Course</h1>`
`  23`  `            <div class="preview-author text-truncate" id="pvAuthor">Lecturer</div>`
`  24`  `          </div>`
`  25`  `        </div>`
`  26`  `        <div class="preview-progress-wrap d-none d-md-flex">`
`  27`  `          <span class="small text-white-50 me-2">Curriculum</span>`
`  28`  `          <div class="preview-progress-bar">`
`  29`  `            <div class="preview-progress-fill" id="pvProgressFill" style="width:0%"></div>`
`  30`  `          </div>`
`  31`  `          <span class="small text-white ms-2" id="pvProgressLabel">0 sections</span>`
`  32`  `        </div>`
`  33`  `        <div class="d-flex gap-2">`
`  34`  `          <button type="button" class="btn btn-sm btn-light rounded-pill px-3" id="btnEditCourse">`
`  35`  `            <i class="fa-solid fa-pencil me-1"></i> Edit`
`  36`  `          </button>`
`  37`  `        </div>`
`  38`  `      </div>`
`  39`  ``
`  40`  `      <div class="preview-layout">`
`  41`  `        <!-- Main player / content -->`
`  42`  `        <div class="preview-main">`
`  43`  `          <div class="preview-stage" id="pvStage">`
`  44`  `            <img id="pvHero" class="preview-hero" alt="" />`
`  45`  `            <button type="button" class="preview-play" id="pvPlayBtn" title="Play / open content">`
`  46`  `              <i class="fa-solid fa-play"></i>`
`  47`  `            </button>`
`  48`  `          </div>`
`  49`  `          <div class="preview-lesson-panel" id="pvLessonPanel">`
`  50`  `            <div class="d-flex justify-content-between align-items-start gap-2 mb-2">`
`  51`  `              <div>`
`  52`  `                <div class="text-muted small" id="pvLessonMeta">Select a lesson</div>`
`  53`  `                <h4 class="fw-bold mb-0" id="pvLessonTitle"> - </h4>`
`  54`  `              </div>`
`  55`  `              <span class="badge rounded-pill bg-light text-secondary" id="pvLessonType"> - </span>`
`  56`  `            </div>`
`  57`  `            <div class="preview-lesson-body" id="pvLessonBody">`
`  58`  `              <p class="text-muted mb-0">Choose a lesson from the course content panel to preview its materials.</p>`
`  59`  `            </div>`
`  60`  `          </div>`
`  61`  `        </div>`
`  62`  ``
`  63`  `        <!-- Sidebar curriculum -->`
`  64`  `        <aside class="preview-sidebar">`
`  65`  `          <div class="preview-sidebar-head">`
`  66`  `            <h6 class="fw-bold mb-0">Course Content</h6>`
`  67`  `            <span class="text-muted small" id="pvSidebarMeta"></span>`
`  68`  `          </div>`
`  69`  `          <div id="pvCurriculum" class="preview-curriculum"></div>`
`  70`  `        </aside>`
`  71`  `      </div>`
`  72`  `    </div>`
`  73`  `  </div>`
`  74`  ``
`  75`  `  <script>`
`  76`  `    (function () {`
`  77`  `    var cid = parseInt('<%= Request.QueryString["cid"] ?? "0" %>', 10) || 0;`
`  78`  `    var course = null;`
`  79`  `    var chapters = [];`
`  80`  `    var active = { chid: null, schid: null };`
`  81`  ``
`  82`  `    function unwrap(data) {`
`  83`  `    var x = data;`
`  84`  `    if (x && x.d !== undefined) x = x.d;`
`  85`  `    if (x && x.d !== undefined) x = x.d;`
`  86`  `    return x;`
`  87`  `    }`
`  88`  `    function post(method, body) {`
`  89`  `    // curriculum uses ashx; course list still uses page method`
`  90`  `    if (method === 'GetCourseCurriculum') {`
`  91`  `    return fetch('CurriculumApi.ashx', {`
  - → HTTP request to server WebMethod/ashx.
`  92`  `    method: 'POST',`
`  93`  `    headers: { 'Content-Type': 'application/json; charset=utf-8' },`
`  94`  `    body: JSON.stringify(Object.assign({ action: 'get' }, body || {})),`
  - → JS object ↔ JSON text.
`  95`  `    credentials: 'same-origin'`
`  96`  `    }).then(function (r) { return r.json(); });`
`  97`  `    }`
`  98`  `    return fetch('CourseCreation.aspx/' + method, {`
  - → HTTP request to server WebMethod/ashx.
`  99`  `    method: 'POST',`
` 100`  `    headers: { 'Content-Type': 'application/json; charset=utf-8' },`
` 101`  `    body: JSON.stringify(body || {}),`
  - → JS object ↔ JSON text.
` 102`  `    credentials: 'same-origin'`
` 103`  `    }).then(function (r) { return r.json(); }).then(unwrap);`
` 104`  `    }`
` 105`  `    function esc(s) {`
` 106`  `    return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');`
` 107`  `  }`
` 108`  ``
` 109`  `  function showError(msg) {`
` 110`  `  document.getElementById('previewLoading').classList.add('d-none');`
  - → Get HTML element by id.
` 111`  `  var el = document.getElementById('previewError');`
  - → Get HTML element by id.
` 112`  `  el.textContent = msg;`
` 113`  `  el.classList.remove('d-none');`
` 114`  `  }`
` 115`  ``
` 116`  `  function load() {`
` 117`  `  if (!cid) { showError('Missing course id.'); return; }`
` 118`  ``
` 119`  `  // Load course list for header fields + curriculum`
` 120`  `  Promise.all([`
` 121`  `  post('GetCoursesData', {}),`
` 122`  `  post('GetCourseCurriculum', { cid: cid })`
` 123`  `  ]).then(function (results) {`
` 124`  `  var coursesRes = results[0];`
` 125`  `  var currRes = results[1];`
` 126`  ``
` 127`  `  if (!coursesRes || !coursesRes.success) {`
` 128`  `  showError((coursesRes && coursesRes.message) || 'Could not load course.');`
` 129`  `  return;`
` 130`  `  }`
` 131`  `  var list = coursesRes.courses || [];`
` 132`  `  course = null;`
` 133`  `  for (var i = 0; i < list.length; i++) {`
` 134`  `  if (list[i].cid === cid) { course = list[i]; break; }`
` 135`  `  }`
` 136`  `  if (!course) {`
` 137`  `  showError('Course not found or you do not have access.');`
` 138`  `  return;`
` 139`  `  }`
` 140`  `  if (!currRes || !currRes.success) {`
` 141`  `  showError((currRes && currRes.message) || 'Could not load curriculum.');`
` 142`  `  return;`
` 143`  `  }`
` 144`  `  chapters = currRes.chapters || [];`
` 145`  `  render();`
` 146`  `  }).catch(function (err) {`
` 147`  `  console.error(err);`
` 148`  `  showError('Network error loading preview.');`
` 149`  `  });`
` 150`  `  }`
` 151`  ``
` 152`  `  function render() {`
` 153`  `  document.getElementById('previewLoading').classList.add('d-none');`
  - → Get HTML element by id.
` 154`  `  document.getElementById('previewBody').classList.remove('d-none');`
  - → Get HTML element by id.
` 155`  ``
` 156`  `  document.getElementById('pvTitle').textContent = course.name || 'Course';`
  - → Get HTML element by id.
` 157`  `  document.getElementById('pvAuthor').textContent =`
  - → Get HTML element by id.
` 158`  `  (course.category || '') + (course.level ? ' · ' + course.level : '') || 'Your course';`
` 159`  ``
` 160`  `  var hero = document.getElementById('pvHero');`
  - → Get HTML element by id.
` 161`  `  hero.src = course.bgImg || 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200';`
` 162`  `  hero.alt = course.name || '';`
` 163`  ``
` 164`  `  var totalLessons = 0;`
` 165`  `  chapters.forEach(function (ch) { totalLessons += (ch.lessons || []).length; });`
` 166`  `  document.getElementById('pvProgressLabel').textContent =`
  - → Get HTML element by id.
` 167`  `  chapters.length + ' section' + (chapters.length === 1 ? '' : 's') +`
` 168`  `  ' · ' + totalLessons + ' lesson' + (totalLessons === 1 ? '' : 's');`
` 169`  `  var pct = chapters.length ? Math.min(100, Math.round((totalLessons / Math.max(chapters.length * 2, 1)) * 100)) : 0;`
` 170`  `  document.getElementById('pvProgressFill').style.width = Math.max(pct, chapters.length ? 12 : 0) + '%';`
  - → Get HTML element by id.
` 171`  `  document.getElementById('pvSidebarMeta').textContent = totalLessons + ' lessons';`
  - → Get HTML element by id.
` 172`  ``
` 173`  `  document.getElementById('btnEditCourse').onclick = function () {`
  - → Get HTML element by id.
` 174`  `  sessionStorage.setItem('editCourseId', String(cid));`
` 175`  `  window.location.href = 'CourseCreation.aspx?edit=' + encodeURIComponent(cid);`
` 176`  `  };`
` 177`  ``
` 178`  `  renderCurriculum();`
` 179`  ``
` 180`  `  // Auto-select first lesson`
` 181`  `  for (var i = 0; i < chapters.length; i++) {`
` 182`  `  var lessons = chapters[i].lessons || [];`
` 183`  `  if (lessons.length) {`
` 184`  `  selectLesson(chapters[i].chid, lessons[0].schid);`
` 185`  `  break;`
` 186`  `  }`
` 187`  `  }`
` 188`  `  }`
` 189`  ``
` 190`  `  function renderCurriculum() {`
` 191`  `  var box = document.getElementById('pvCurriculum');`
  - → Get HTML element by id.
` 192`  `  if (!chapters.length) {`
` 193`  `  box.innerHTML = '<div class="p-3 text-muted small">No sections yet. Edit the course to add curriculum.</div>';`
  - → Update page HTML.
` 194`  `  return;`
` 195`  `  }`
` 196`  `  var html = '';`
` 197`  `  chapters.forEach(function (ch, ci) {`
` 198`  `  var lessons = ch.lessons || [];`
` 199`  `  var open = true;`
` 200`  `  html += '<div class="pv-section' + (open ? ' open' : '') + '" data-chid="' + ch.chid + '">';`
` 201`  `    html += '<button type="button" class="pv-section-head" data-toggle-section="' + ch.chid + '">';`
` 202`  `      html += '<div><div class="fw-semibold">Section ' + (ci + 1) + ': ' + esc(ch.title) + '</div>';`
` 203`  `        html += '<div class="text-muted" style="font-size:0.75rem;">' + lessons.length + ' lesson' + (lessons.length === 1 ? '' : 's') + '</div></div>';`
` 204`  `      html += '<i class="fa-solid fa-chevron-down pv-chevron"></i></button>';`
` 205`  `    html += '<div class="pv-lessons">';`
` 206`  `      if (!lessons.length) {`
` 207`  `      html += '<div class="pv-lesson text-muted small">No lessons</div>';`
` 208`  `      } else {`
` 209`  `      lessons.forEach(function (les) {`
` 210`  `      var type = (les.type || 'Text').toLowerCase();`
` 211`  `      var icon = type === 'video' ? 'fa-circle-play' : (type === 'quiz' ? 'fa-file-circle-question' : 'fa-file-lines');`
` 212`  `      var activeCls = (active.schid === les.schid) ? ' active' : '';`
` 213`  `      html += '<button type="button" class="pv-lesson' + activeCls + '" data-chid="' + ch.chid + '" data-schid="' + les.schid + '">';`
` 214`  `        html += '<i class="fa-solid ' + icon + '"></i>';`
` 215`  `        html += '<div class="min-w-0"><div class="pv-lesson-title text-truncate">' + esc(les.title) + '</div>';`
` 216`  `          html += '<div class="text-muted" style="font-size:0.72rem;">' + esc(les.type || 'Text') + '</div></div></button>';`
` 217`  `      });`
` 218`  `      }`
` 219`  `      html += '</div></div>';`
` 220`  `  });`
` 221`  `  box.innerHTML = html;`
  - → Update page HTML.
` 222`  ``
` 223`  `  box.querySelectorAll('[data-toggle-section]').forEach(function (btn) {`
` 224`  `  btn.addEventListener('click', function () {`
  - → DOM event handler.
` 225`  `  var sec = btn.closest('.pv-section');`
` 226`  `  if (sec) sec.classList.toggle('open');`
` 227`  `  });`
` 228`  `  });`
` 229`  `  box.querySelectorAll('.pv-lesson[data-schid]').forEach(function (btn) {`
` 230`  `  btn.addEventListener('click', function () {`
  - → DOM event handler.
` 231`  `  selectLesson(parseInt(btn.getAttribute('data-chid'), 10), parseInt(btn.getAttribute('data-schid'), 10));`
` 232`  `  });`
` 233`  `  });`
` 234`  `  }`
` 235`  ``
` 236`  `  function findLesson(chid, schid) {`
` 237`  `  for (var i = 0; i < chapters.length; i++) {`
` 238`  `  if (chapters[i].chid !== chid) continue;`
` 239`  `  var lessons = chapters[i].lessons || [];`
` 240`  `  for (var j = 0; j < lessons.length; j++) {`
` 241`  `  if (lessons[j].schid === schid) return { chapter: chapters[i], lesson: lessons[j] };`
` 242`  `  }`
` 243`  `  }`
` 244`  `  return null;`
` 245`  `  }`
` 246`  ``
` 247`  `  /** App root e.g. "" or "/WebAppAssignment" */`
` 248`  `  function appRoot() {`
` 249`  `  var p = window.location.pathname || '';`
` 250`  `  var i = p.toLowerCase().indexOf('/pages/');`
` 251`  `  if (i > 0) return p.substring(0, i);`
` 252`  `  return '';`
` 253`  `  }`
` 254`  ``
` 255`  `  /**`
` 256`  `  * Always use root Media.ashx so files work under IIS Express.`
` 257`  `  * Example: /Media.ashx?f=CourseMaterials/abc.pdf`
` 258`  `  */`
` 259`  `  function resolveMediaUrl(raw, forDownload) {`
` 260`  `  if (!raw) return '';`
` 261`  `  var u = String(raw).trim();`
` 262`  `  if (/^https?:\/\//i.test(u) &&`
` 263`  `  u.indexOf('/Uploads/') < 0 && u.indexOf('Uploads/') < 0 &&`
` 264`  `  u.indexOf('Media.ashx') < 0 && u.indexOf('ServeUpload') < 0)`
` 265`  `  return u;`
` 266`  ``
` 267`  `  if (u.indexOf('Media.ashx') >= 0 || u.indexOf('ServeUpload') >= 0) {`
` 268`  `  try {`
  - → Error handling block.
` 269`  `  var key = u.indexOf('f=') >= 0 ? 'f=' : (u.indexOf('path=') >= 0 ? 'path=' : null);`
` 270`  `  if (key) {`
` 271`  `  var q = u.split(key)[1];`
` 272`  `  if (q) return resolveMediaUrl(decodeURIComponent(q.split('&')[0]), forDownload);`
` 273`  `  }`
` 274`  `  } catch (e) { }`
` 275`  `  }`
` 276`  `  try {`
  - → Error handling block.
` 277`  `  if (/^https?:\/\//i.test(u)) {`
` 278`  `  var a = document.createElement('a');`
` 279`  `  a.href = u;`
` 280`  `  u = a.pathname || u;`
` 281`  `  }`
` 282`  `  } catch (e) { }`
` 283`  `  var path = u.replace(/\\/g, '/');`
` 284`  `  var idx = path.toLowerCase().indexOf('/uploads/');`
` 285`  `  if (idx >= 0) path = path.substring(idx + 1);`
` 286`  `  if (path.indexOf('~/') === 0) path = path.substring(2);`
` 287`  `  path = path.replace(/^\/+/, '');`
` 288`  `  if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);`
` 289`  `  if (!path) return '';`
` 290`  `  if (path.indexOf('/') < 0) path = 'CourseMaterials/' + path;`
` 291`  `  var url = appRoot() + '/Media.ashx?f=' + encodeURIComponent(path);`
` 292`  `  if (forDownload) url += '&dl=1';`
` 293`  `  return url;`
` 294`  `  }`
` 295`  ``
` 296`  `  function mediaKind(s) {`
` 297`  `  s = (s || '').toLowerCase();`
` 298`  `  if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0 || s.indexOf('video') === 0) return 'video';`
` 299`  `  if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s) || s.indexOf('image') === 0) return 'image';`
` 300`  `  if (/\.pdf(\?|$)/.test(s) || s.indexOf('pdf') === 0) return 'pdf';`
` 301`  `  return 'file';`
` 302`  `  }`
` 303`  ``
` 304`  `  function looksLikeFile(s) {`
` 305`  `  if (!s) return false;`
` 306`  `  s = String(s).trim();`
` 307`  `  // Real stored paths / handlers`
` 308`  `  if (/uploads\//i.test(s) || /Media\.ashx/i.test(s) || /ServeUpload/i.test(s)) return true;`
` 309`  `  if (/coursematerials\/|coursevideos\/|coursethumbnails\//i.test(s)) return true;`
` 310`  `  // GUID filename (32 hex)`
` 311`  `  var base = s.split('/').pop() || s;`
` 312`  `  var noext = base.replace(/\.[^.]+$/, '');`
` 313`  `  if (/^[a-f0-9]{32}$/i.test(noext)) return true;`
` 314`  `  // Bare original names still allowed for Media.ashx .meta lookup`
` 315`  `  return /\.(pdf|mp4|webm|mov|png|jpe?g|gif|webp|docx?|pptx?)(\?|$)/i.test(s);`
` 316`  `  }`
` 317`  ``
` 318`  `  function renderMediaBlock(rawUrl, label) {`
` 319`  `  var view = resolveMediaUrl(rawUrl, false);`
` 320`  `  var dl = resolveMediaUrl(rawUrl, true);`
` 321`  `  var kind = mediaKind(label + ' ' + rawUrl);`
` 322`  `  var h = '';`
` 323`  `  h += '<div class="border rounded p-3 mb-3 bg-white">';`
` 324`  `    h += '<div class="d-flex flex-wrap align-items-center gap-2 mb-2">' +`
` 325`  `      '<span class="small fw-semibold flex-grow-1 text-truncate">' + esc(label || 'File') + '</span>' +`
` 326`  `      '<a class="btn btn-sm btn-outline-secondary py-0" href="' + esc(view) + '" target="_blank" rel="noopener">Open</a>' +`
` 327`  `      '<a class="btn btn-sm btn-outline-primary py-0" href="' + esc(dl) + '">Download</a></div>';`
` 328`  `    if (kind === 'video') {`
` 329`  `    h += '<video controls playsinline preload="metadata" class="w-100 rounded" style="max-height:420px;background:#111;" src="' + esc(view) + '">' +`
` 330`  `      'Your browser cannot play this video. <a href="' + esc(view) + '">Open file</a></video>';`
` 331`  `    } else if (kind === 'image') {`
` 332`  `    h += '<img src="' + esc(view) + '" class="img-fluid rounded" alt="" style="max-height:420px;" />';`
` 333`  `    } else if (kind === 'pdf') {`
` 334`  `    h += '<iframe src="' + esc(view) + '#toolbar=1" class="w-100 rounded border" style="min-height:480px;background:#fff;" title="' + esc(label || 'PDF') + '"></iframe>';`
` 335`  `    } else {`
` 336`  `    h += '<p class="small text-muted mb-0">Preview not available for this file type - use Open or Download.</p>';`
` 337`  `    }`
` 338`  `    h += '</div>';`
` 339`  `  return h;`
` 340`  `  }`
` 341`  ``
` 342`  `  function selectLesson(chid, schid) {`
` 343`  `  active = { chid: chid, schid: schid };`
` 344`  `  renderCurriculum();`
` 345`  `  var found = findLesson(chid, schid);`
` 346`  `  if (!found) return;`
` 347`  `  var les = found.lesson;`
` 348`  `  var ch = found.chapter;`
` 349`  `  document.getElementById('pvLessonMeta').textContent = (ch.title || 'Section') + ' · Lesson';`
  - → Get HTML element by id.
` 350`  `  document.getElementById('pvLessonTitle').textContent = les.title || 'Lesson';`
  - → Get HTML element by id.
` 351`  ``
` 352`  `  var body = document.getElementById('pvLessonBody');`
  - → Get HTML element by id.
` 353`  `  var type = (les.type || 'Text').toLowerCase();`
` 354`  `  var content = les.content || '';`
` 355`  `  var materials = les.materials || [];`
` 356`  `  var html = '';`
` 357`  ``
` 358`  `  // Collect file rows from materials[] and content`
` 359`  `  var files = [];`
` 360`  `  function pushFile(link, label, t) {`
` 361`  `  link = (link || '').trim();`
` 362`  `  if (!link) return;`
` 363`  `  // Prefer path-like values; also accept any .ext string`
` 364`  `  if (!looksLikeFile(link) && !/\.(pdf|mp4|webm|mov|png|jpe?g|gif|webp|docx?|pptx?)(\?|$)/i.test(label || '')) {`
` 365`  `  // still allow if type says media`
` 366`  `  var tl = (t || '').toLowerCase();`
` 367`  `  if (tl !== 'video' && tl !== 'pdf' && tl !== 'image' && tl !== 'file') return;`
` 368`  `  }`
` 369`  `  if (files.some(function (f) { return f.link === link; })) return;`
` 370`  `  files.push({`
` 371`  `  link: link,`
` 372`  `  label: label || link,`
` 373`  `  type: t || mediaKind(label + ' ' + link)`
` 374`  `  });`
` 375`  `  }`
` 376`  ``
` 377`  `  (materials || []).forEach(function (m) {`
` 378`  `  var link = (m.mediaLink || m.url || '').trim();`
` 379`  `  var text = (m.textContent || m.fileName || '').trim();`
` 380`  `  // media empty but text is a real store path (Uploads/ or GUID) - never bare "report.pdf" alone`
` 381`  `  if (!link && looksLikeFile(text)) link = text;`
` 382`  `  // If only original file name is known, still try Media.ashx meta lookup`
` 383`  `  if (!link && text && /\.(pdf|mp4|webm|mov|png|jpe?g|gif|webp|docx?|pptx?)(\?|$)/i.test(text)) {`
` 384`  `  link = text; // Media.ashx resolves via .meta / uploads.log`
` 385`  `  }`
` 386`  `  pushFile(link, m.fileName || m.textContent || link, m.type);`
` 387`  `  });`
` 388`  `  if (looksLikeFile(content)) {`
` 389`  `  pushFile(content, les.title || content, type);`
` 390`  `  }`
` 391`  ``
` 392`  `  // Badge from first file or lesson type`
` 393`  `  var badge = les.type || 'Text';`
` 394`  `  if (files.length) {`
` 395`  `  badge = mediaKind(files[0].label + ' ' + files[0].link);`
` 396`  `  badge = badge.charAt(0).toUpperCase() + badge.slice(1);`
` 397`  `  if (badge === 'File') badge = 'Material';`
` 398`  `  }`
` 399`  `  document.getElementById('pvLessonType').textContent = badge;`
  - → Get HTML element by id.
` 400`  ``
` 401`  `  // Always prefer showing media blocks for files`
` 402`  `  if (files.length) {`
` 403`  `  document.getElementById('pvHero').style.opacity = '0.35';`
  - → Get HTML element by id.
` 404`  `  // Show primary file large, then rest as Materials`
` 405`  `  html += renderMediaBlock(files[0].link, files[0].label || les.title || 'Material');`
` 406`  `  if (files.length > 1) {`
` 407`  `  html += '<div class="mt-3"><div class="fw-semibold mb-2"><i class="fa-solid fa-paperclip me-1"></i>More materials (' + (files.length - 1) + ')</div>';`
` 408`  `    for (var fi = 1; fi < files.length; fi++) {`
` 409`  `    html += renderMediaBlock(files[fi].link, files[fi].label);`
` 410`  `    }`
` 411`  `    html += '</div>';`
` 412`  `  }`
` 413`  `  // Optional short text note under media if content was plain non-file text`
` 414`  `  if (content && !looksLikeFile(content)) {`
` 415`  `  var plainNote = content.replace(/<[^>]+>/g, '').trim();`
` 416`  `  if (plainNote && plainNote.length > 0 && plainNote !== (les.title || '')) {`
` 417`  `  if (content.indexOf('<') === -1)`
` 418`  `  html += '<div class="preview-text-content mt-3 text-muted small">' + esc(content).replace(/\n/g, '<br/>') + '</div>';`
` 419`  `  }`
` 420`  `  }`
` 421`  `  } else if (content && content.replace(/<[^>]+>/g, '').trim()) {`
` 422`  `  if (content.indexOf('<') === -1)`
` 423`  `  html += '<div class="preview-text-content mb-3">' + esc(content).replace(/\n/g, '<br/>') + '</div>';`
` 424`  `  else`
` 425`  `  html += '<div class="preview-text-content mb-3">' + content + '</div>';`
` 426`  `  html += '<div class="alert alert-light border small mt-3 mb-0">' +`
` 427`  `    '<i class="fa-solid fa-circle-info me-1"></i>' +`
` 428`  `    'No file materials on this lesson. Edit the lesson, upload PDF/video under Materials, then Save again.' +`
` 429`  `    '</div>';`
` 430`  `  } else {`
` 431`  `  html += '<p class="text-muted mb-0">No content or materials for this lesson. Edit and upload a file.</p>';`
` 432`  `  }`
` 433`  ``
` 434`  `  body.innerHTML = html;`
  - → Update page HTML.
` 435`  `  }`
` 436`  ``
` 437`  `  document.getElementById('pvPlayBtn').addEventListener('click', function () {`
  - → DOM event handler.
` 438`  `  var panel = document.getElementById('pvLessonPanel');`
  - → Get HTML element by id.
` 439`  `  if (panel) panel.scrollIntoView({ behavior: 'smooth', block: 'start' });`
` 440`  `  });`
` 441`  ``
` 442`  `  load();`
` 443`  `  })();`
` 444`  `</script>`
` 445`  `</asp:Content>`

## Source snapshot (raw)

```html
<%@ Page Title="Course Preview" Language="C#" MasterPageFile="~/Shared/Header&Footer.Master" AutoEventWireup="true" CodeBehind="CoursePreview.aspx.cs" Inherits="WebAppAssignment.Pages.Lecturer.CoursePreview" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
  <link rel="stylesheet" href="Style/course-preview.css" />
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
  <div class="course-preview-page" id="previewRoot">
    <div class="text-center py-5 text-muted" id="previewLoading">
      <i class="fa-solid fa-circle-notch fa-spin me-2"></i> Loading course preview...
    </div>
    <div id="previewError" class="alert alert-danger d-none"></div>

    <div id="previewBody" class="d-none">
      <!-- Top bar -->
      <div class="preview-topbar">
        <div class="d-flex align-items-center gap-3 min-w-0">
          <a href="CourseCreation.aspx" class="preview-back" title="Back to My Courses">
            <i class="fa-solid fa-chevron-left"></i>
          </a>
          <div class="min-w-0">
            <h1 class="preview-title text-truncate" id="pvTitle">Course</h1>
            <div class="preview-author text-truncate" id="pvAuthor">Lecturer</div>
          </div>
        </div>
        <div class="preview-progress-wrap d-none d-md-flex">
          <span class="small text-white-50 me-2">Curriculum</span>
          <div class="preview-progress-bar">
            <div class="preview-progress-fill" id="pvProgressFill" style="width:0%"></div>
          </div>
          <span class="small text-white ms-2" id="pvProgressLabel">0 sections</span>
        </div>
        <div class="d-flex gap-2">
          <button type="button" class="btn btn-sm btn-light rounded-pill px-3" id="btnEditCourse">
            <i class="fa-solid fa-pencil me-1"></i> Edit
          </button>
        </div>
      </div>

      <div class="preview-layout">
        <!-- Main player / content -->
        <div class="preview-main">
          <div class="preview-stage" id="pvStage">
            <img id="pvHero" class="preview-hero" alt="" />
            <button type="button" class="preview-play" id="pvPlayBtn" title="Play / open content">
              <i class="fa-solid fa-play"></i>
            </button>
          </div>
          <div class="preview-lesson-panel" id="pvLessonPanel">
            <div class="d-flex justify-content-between align-items-start gap-2 mb-2">
              <div>
                <div class="text-muted small" id="pvLessonMeta">Select a lesson</div>
                <h4 class="fw-bold mb-0" id="pvLessonTitle"> - </h4>
              </div>
              <span class="badge rounded-pill bg-light text-secondary" id="pvLessonType"> - </span>
            </div>
            <div class="preview-lesson-body" id="pvLessonBody">
              <p class="text-muted mb-0">Choose a lesson from the course content panel to preview its materials.</p>
            </div>
          </div>
        </div>

        <!-- Sidebar curriculum -->
        <aside class="preview-sidebar">
          <div class="preview-sidebar-head">
            <h6 class="fw-bold mb-0">Course Content</h6>
            <span class="text-muted small" id="pvSidebarMeta"></span>
          </div>
          <div id="pvCurriculum" class="preview-curriculum"></div>
        </aside>
      </div>
    </div>
  </div>

  <script>
    (function () {
    var cid = parseInt('<%= Request.QueryString["cid"] ?? "0" %>', 10) || 0;
    var course = null;
    var chapters = [];
    var active = { chid: null, schid: null };

    function unwrap(data) {
    var x = data;
    if (x && x.d !== undefined) x = x.d;
    if (x && x.d !== undefined) x = x.d;
    return x;
    }
    function post(method, body) {
    // curriculum uses ashx; course list still uses page method
    if (method === 'GetCourseCurriculum') {
    return fetch('CurriculumApi.ashx', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
    body: JSON.stringify(Object.assign({ action: 'get' }, body || {})),
    credentials: 'same-origin'
    }).then(function (r) { return r.json(); });
    }
    return fetch('CourseCreation.aspx/' + method, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
    body: JSON.stringify(body || {}),
    credentials: 'same-origin'
    }).then(function (r) { return r.json(); }).then(unwrap);
    }
    function esc(s) {
    return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function showError(msg) {
  document.getElementById('previewLoading').classList.add('d-none');
  var el = document.getElementById('previewError');
  el.textContent = msg;
  el.classList.remove('d-none');
  }

  function load() {
  if (!cid) { showError('Missing course id.'); return; }

  // Load course list for header fields + curriculum
  Promise.all([
  post('GetCoursesData', {}),
  post('GetCourseCurriculum', { cid: cid })
  ]).then(function (results) {
  var coursesRes = results[0];
  var currRes = results[1];

  if (!coursesRes || !coursesRes.success) {
  showError((coursesRes && coursesRes.message) || 'Could not load course.');
  return;
  }
  var list = coursesRes.courses || [];
  course = null;
  for (var i = 0; i < list.length; i++) {
  if (list[i].cid === cid) { course = list[i]; break; }
  }
  if (!course) {
  showError('Course not found or you do not have access.');
  return;
  }
  if (!currRes || !currRes.success) {
  showError((currRes && currRes.message) || 'Could not load curriculum.');
  return;
  }
  chapters = currRes.chapters || [];
  render();
  }).catch(function (err) {
  console.error(err);
  showError('Network error loading preview.');
  });
  }

  function render() {
  document.getElementById('previewLoading').classList.add('d-none');
  document.getElementById('previewBody').classList.remove('d-none');

  document.getElementById('pvTitle').textContent = course.name || 'Course';
  document.getElementById('pvAuthor').textContent =
  (course.category || '') + (course.level ? ' · ' + course.level : '') || 'Your course';

  var hero = document.getElementById('pvHero');
  hero.src = course.bgImg || 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200';
  hero.alt = course.name || '';

  var totalLessons = 0;
  chapters.forEach(function (ch) { totalLessons += (ch.lessons || []).length; });
  document.getElementById('pvProgressLabel').textContent =
  chapters.length + ' section' + (chapters.length === 1 ? '' : 's') +
  ' · ' + totalLessons + ' lesson' + (totalLessons === 1 ? '' : 's');
  var pct = chapters.length ? Math.min(100, Math.round((totalLessons / Math.max(chapters.length * 2, 1)) * 100)) : 0;
  document.getElementById('pvProgressFill').style.width = Math.max(pct, chapters.length ? 12 : 0) + '%';
  document.getElementById('pvSidebarMeta').textContent = totalLessons + ' lessons';

  document.getElementById('btnEditCourse').onclick = function () {
  sessionStorage.setItem('editCourseId', String(cid));
  window.location.href = 'CourseCreation.aspx?edit=' + encodeURIComponent(cid);
  };

  renderCurriculum();

  // Auto-select first lesson
  for (var i = 0; i < chapters.length; i++) {
  var lessons = chapters[i].lessons || [];
  if (lessons.length) {
  selectLesson(chapters[i].chid, lessons[0].schid);
  break;
  }
  }
  }

  function renderCurriculum() {
  var box = document.getElementById('pvCurriculum');
  if (!chapters.length) {
  box.innerHTML = '<div class="p-3 text-muted small">No sections yet. Edit the course to add curriculum.</div>';
  return;
  }
  var html = '';
  chapters.forEach(function (ch, ci) {
  var lessons = ch.lessons || [];
  var open = true;
  html += '<div class="pv-section' + (open ? ' open' : '') + '" data-chid="' + ch.chid + '">';
    html += '<button type="button" class="pv-section-head" data-toggle-section="' + ch.chid + '">';
      html += '<div><div class="fw-semibold">Section ' + (ci + 1) + ': ' + esc(ch.title) + '</div>';
        html += '<div class="text-muted" style="font-size:0.75rem;">' + lessons.length + ' lesson' + (lessons.length === 1 ? '' : 's') + '</div></div>';
      html += '<i class="fa-solid fa-chevron-down pv-chevron"></i></button>';
    html += '<div class="pv-lessons">';
      if (!lessons.length) {
      html += '<div class="pv-lesson text-muted small">No lessons</div>';
      } else {
      lessons.forEach(function (les) {
      var type = (les.type || 'Text').toLowerCase();
      var icon = type === 'video' ? 'fa-circle-play' : (type === 'quiz' ? 'fa-file-circle-question' : 'fa-file-lines');
      var activeCls = (active.schid === les.schid) ? ' active' : '';
      html += '<button type="button" class="pv-lesson' + activeCls + '" data-chid="' + ch.chid + '" data-schid="' + les.schid + '">';
        html += '<i class="fa-solid ' + icon + '"></i>';
        html += '<div class="min-w-0"><div class="pv-lesson-title text-truncate">' + esc(les.title) + '</div>';
          html += '<div class="text-muted" style="font-size:0.72rem;">' + esc(les.type || 'Text') + '</div></div></button>';
      });
      }
      html += '</div></div>';
  });
  box.innerHTML = html;

  box.querySelectorAll('[data-toggle-section]').forEach(function (btn) {
  btn.addEventListener('click', function () {
  var sec = btn.closest('.pv-section');
  if (sec) sec.classList.toggle('open');
  });
  });
  box.querySelectorAll('.pv-lesson[data-schid]').forEach(function (btn) {
  btn.addEventListener('click', function () {
  selectLesson(parseInt(btn.getAttribute('data-chid'), 10), parseInt(btn.getAttribute('data-schid'), 10));
  });
  });
  }

  function findLesson(chid, schid) {
  for (var i = 0; i < chapters.length; i++) {
  if (chapters[i].chid !== chid) continue;
  var lessons = chapters[i].lessons || [];
  for (var j = 0; j < lessons.length; j++) {
  if (lessons[j].schid === schid) return { chapter: chapters[i], lesson: lessons[j] };
  }
  }
  return null;
  }

  /** App root e.g. "" or "/WebAppAssignment" */
  function appRoot() {
  var p = window.location.pathname || '';
  var i = p.toLowerCase().indexOf('/pages/');
  if (i > 0) return p.substring(0, i);
  return '';
  }

  /**
  * Always use root Media.ashx so files work under IIS Express.
  * Example: /Media.ashx?f=CourseMaterials/abc.pdf
  */
  function resolveMediaUrl(raw, forDownload) {
  if (!raw) return '';
  var u = String(raw).trim();
  if (/^https?:\/\//i.test(u) &&
  u.indexOf('/Uploads/') < 0 && u.indexOf('Uploads/') < 0 &&
  u.indexOf('Media.ashx') < 0 && u.indexOf('ServeUpload') < 0)
  return u;

  if (u.indexOf('Media.ashx') >= 0 || u.indexOf('ServeUpload') >= 0) {
  try {
  var key = u.indexOf('f=') >= 0 ? 'f=' : (u.indexOf('path=') >= 0 ? 'path=' : null);
  if (key) {
  var q = u.split(key)[1];
  if (q) return resolveMediaUrl(decodeURIComponent(q.split('&')[0]), forDownload);
  }
  } catch (e) { }
  }
  try {
  if (/^https?:\/\//i.test(u)) {
  var a = document.createElement('a');
  a.href = u;
  u = a.pathname || u;
  }
  } catch (e) { }
  var path = u.replace(/\\/g, '/');
  var idx = path.toLowerCase().indexOf('/uploads/');
  if (idx >= 0) path = path.substring(idx + 1);
  if (path.indexOf('~/') === 0) path = path.substring(2);
  path = path.replace(/^\/+/, '');
  if (path.toLowerCase().indexOf('uploads/') === 0) path = path.substring('uploads/'.length);
  if (!path) return '';
  if (path.indexOf('/') < 0) path = 'CourseMaterials/' + path;
  var url = appRoot() + '/Media.ashx?f=' + encodeURIComponent(path);
  if (forDownload) url += '&dl=1';
  return url;
  }

  function mediaKind(s) {
  s = (s || '').toLowerCase();
  if (/\.(mp4|webm|mov)(\?|$)/.test(s) || s.indexOf('coursevideos') >= 0 || s.indexOf('video') === 0) return 'video';
  if (/\.(png|jpe?g|gif|webp|bmp)(\?|$)/.test(s) || s.indexOf('image') === 0) return 'image';
  if (/\.pdf(\?|$)/.test(s) || s.indexOf('pdf') === 0) return 'pdf';
  return 'file';
  }

  function looksLikeFile(s) {
  if (!s) return false;
  s = String(s).trim();
  // Real stored paths / handlers
  if (/uploads\//i.test(s) || /Media\.ashx/i.test(s) || /ServeUpload/i.test(s)) return true;
  if (/coursematerials\/|coursevideos\/|coursethumbnails\//i.test(s)) return true;
  // GUID filename (32 hex)
  var base = s.split('/').pop() || s;
  var noext = base.replace(/\.[^.]+$/, '');
  if (/^[a-f0-9]{32}$/i.test(noext)) return true;
  // Bare original names still allowed for Media.ashx .meta lookup
  return /\.(pdf|mp4|webm|mov|png|jpe?g|gif|webp|docx?|pptx?)(\?|$)/i.test(s);
  }

  function renderMediaBlock(rawUrl, label) {
  var view = resolveMediaUrl(rawUrl, false);
  var dl = resolveMediaUrl(rawUrl, true);
  var kind = mediaKind(label + ' ' + rawUrl);
  var h = '';
  h += '<div class="border rounded p-3 mb-3 bg-white">';
    h += '<div class="d-flex flex-wrap align-items-center gap-2 mb-2">' +
      '<span class="small fw-semibold flex-grow-1 text-truncate">' + esc(label || 'File') + '</span>' +
      '<a class="btn btn-sm btn-outline-secondary py-0" href="' + esc(view) + '" target="_blank" rel="noopener">Open</a>' +
      '<a class="btn btn-sm btn-outline-primary py-0" href="' + esc(dl) + '">Download</a></div>';
    if (kind === 'video') {
    h += '<video controls playsinline preload="metadata" class="w-100 rounded" style="max-height:420px;background:#111;" src="' + esc(view) + '">' +
      'Your browser cannot play this video. <a href="' + esc(view) + '">Open file</a></video>';
    } else if (kind === 'image') {
    h += '<img src="' + esc(view) + '" class="img-fluid rounded" alt="" style="max-height:420px;" />';
    } else if (kind === 'pdf') {
    h += '<iframe src="' + esc(view) + '#toolbar=1" class="w-100 rounded border" style="min-height:480px;background:#fff;" title="' + esc(label || 'PDF') + '"></iframe>';
    } else {
    h += '<p class="small text-muted mb-0">Preview not available for this file type - use Open or Download.</p>';
    }
    h += '</div>';
  return h;
  }

  function selectLesson(chid, schid) {
  active = { chid: chid, schid: schid };
  renderCurriculum();
  var found = findLesson(chid, schid);
  if (!found) return;
  var les = found.lesson;
  var ch = found.chapter;
  document.getElementById('pvLessonMeta').textContent = (ch.title || 'Section') + ' · Lesson';
  document.getElementById('pvLessonTitle').textContent = les.title || 'Lesson';

  var body = document.getElementById('pvLessonBody');
  var type = (les.type || 'Text').toLowerCase();
  var content = les.content || '';
  var materials = les.materials || [];
  var html = '';

  // Collect file rows from materials[] and content
  var files = [];
  function pushFile(link, label, t) {
  link = (link || '').trim();
  if (!link) return;
  // Prefer path-like values; also accept any .ext string
  if (!looksLikeFile(link) && !/\.(pdf|mp4|webm|mov|png|jpe?g|gif|webp|docx?|pptx?)(\?|$)/i.test(label || '')) {
  // still allow if type says media
  var tl = (t || '').toLowerCase();
  if (tl !== 'video' && tl !== 'pdf' && tl !== 'image' && tl !== 'file') return;
  }
  if (files.some(function (f) { return f.link === link; })) return;
  files.push({
  link: link,
  label: label || link,
  type: t || mediaKind(label + ' ' + link)
  });
  }

  (materials || []).forEach(function (m) {
  var link = (m.mediaLink || m.url || '').trim();
  var text = (m.textContent || m.fileName || '').trim();
  // media empty but text is a real store path (Uploads/ or GUID) - never bare "report.pdf" alone
  if (!link && looksLikeFile(text)) link = text;
  // If only original file name is known, still try Media.ashx meta lookup
  if (!link && text && /\.(pdf|mp4|webm|mov|png|jpe?g|gif|webp|docx?|pptx?)(\?|$)/i.test(text)) {
  link = text; // Media.ashx resolves via .meta / uploads.log
  }
  pushFile(link, m.fileName || m.textContent || link, m.type);
  });
  if (looksLikeFile(content)) {
  pushFile(content, les.title || content, type);
  }

  // Badge from first file or lesson type
  var badge = les.type || 'Text';
  if (files.length) {
  badge = mediaKind(files[0].label + ' ' + files[0].link);
  badge = badge.charAt(0).toUpperCase() + badge.slice(1);
  if (badge === 'File') badge = 'Material';
  }
  document.getElementById('pvLessonType').textContent = badge;

  // Always prefer showing media blocks for files
  if (files.length) {
  document.getElementById('pvHero').style.opacity = '0.35';
  // Show primary file large, then rest as Materials
  html += renderMediaBlock(files[0].link, files[0].label || les.title || 'Material');
  if (files.length > 1) {
  html += '<div class="mt-3"><div class="fw-semibold mb-2"><i class="fa-solid fa-paperclip me-1"></i>More materials (' + (files.length - 1) + ')</div>';
    for (var fi = 1; fi < files.length; fi++) {
    html += renderMediaBlock(files[fi].link, files[fi].label);
    }
    html += '</div>';
  }
  // Optional short text note under media if content was plain non-file text
  if (content && !looksLikeFile(content)) {
  var plainNote = content.replace(/<[^>]+>/g, '').trim();
  if (plainNote && plainNote.length > 0 && plainNote !== (les.title || '')) {
  if (content.indexOf('<') === -1)
  html += '<div class="preview-text-content mt-3 text-muted small">' + esc(content).replace(/\n/g, '<br/>') + '</div>';
  }
  }
  } else if (content && content.replace(/<[^>]+>/g, '').trim()) {
  if (content.indexOf('<') === -1)
  html += '<div class="preview-text-content mb-3">' + esc(content).replace(/\n/g, '<br/>') + '</div>';
  else
  html += '<div class="preview-text-content mb-3">' + content + '</div>';
  html += '<div class="alert alert-light border small mt-3 mb-0">' +
    '<i class="fa-solid fa-circle-info me-1"></i>' +
    'No file materials on this lesson. Edit the lesson, upload PDF/video under Materials, then Save again.' +
    '</div>';
  } else {
  html += '<p class="text-muted mb-0">No content or materials for this lesson. Edit and upload a file.</p>';
  }

  body.innerHTML = html;
  }

  document.getElementById('pvPlayBtn').addEventListener('click', function () {
  var panel = document.getElementById('pvLessonPanel');
  if (panel) panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  load();
  })();
</script>
</asp:Content>

```
