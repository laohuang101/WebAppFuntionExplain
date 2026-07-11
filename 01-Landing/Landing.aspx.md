# Landing.aspx
**Source:** `Pages/Landing/Landing.aspx`  
**Generated:** 2026-07-11 21:33  

---

## Feature / role in EduLMS

Public marketing + course catalog. Shows published courses only (`IsPublished`). Guests can browse; Enroll sends unauthenticated users to Login.

## File overview

- **Total lines:** 300
- **Kind:** `.aspx`

## Variables / fields (file level)

Markup/mixed file. Server controls and expressions are explained with code-behind and script companions.

## Functions / methods (0 found)

_No methods matched the scanner (markup-only or unconventional structure). See full file listing below._

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.

```html
   1 | <%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Landing.aspx.cs" Inherits="WebAppAssignment.Pages.Landing.Landing" %>
   2 | 
   3 | <!DOCTYPE html>
   4 | <html lang="en" xmlns="http://www.w3.org/1999/xhtml">
   5 | <head runat="server">
   6 |     <meta charset="utf-8" />
   7 |     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   8 |     <title>EduLMS - Learn without limits</title>
   9 |     <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
  10 |     <meta name="viewport" content="width=device-width, initial-scale=1" />
  11 |     <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin="anonymous" />
  12 |     <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin="anonymous" />
  13 |     <link rel="preconnect" href="https://fonts.googleapis.com" />
  14 |     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  15 |     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
  16 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  17 |     <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  18 |     <link href="Style/landing.css" rel="stylesheet" />
  19 | </head>
  20 | <body>
  21 |     <form id="form1" runat="server">
  22 |         <nav class="topnav" id="topnav">
  23 |             <a class="brand" href="#home" data-goto="home">
  24 |                 <span class="brand-icon"><i class="fa-solid fa-graduation-cap"></i></span>
  25 |                 EduLMS
  26 |             </a>
  27 |             <div class="nav-actions">
  28 |                 <button type="button" class="nav-link-soft d-none d-md-inline active" data-goto="home">Home</button>
  29 |                 <button type="button" class="nav-link-soft d-none d-md-inline" data-goto="about">About</button>
  30 |                 <button type="button" class="nav-link-soft d-none d-md-inline" data-goto="why">Why</button>
  31 |                 <button type="button" class="nav-link-soft d-none d-md-inline" data-goto="courses">Courses</button>
  32 |                 <asp:PlaceHolder ID="phGuest" runat="server">
  33 |                     <a class="btn-ghost" href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Log in</a>
  34 |                     <a class="btn-accent" href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">
  35 |                         Get started <i class="fa-solid fa-arrow-right" style="font-size:0.8rem;"></i>
  36 |                     </a>
  37 |                 </asp:PlaceHolder>
  38 |                 <asp:PlaceHolder ID="phUser" runat="server" Visible="false">
  39 |                     <span class="btn-ghost" style="cursor:default;">
  40 |                         Hi, <asp:Literal ID="litUserName" runat="server" />
  41 |                     </span>
  42 |                     <a class="btn-outline-accent" id="lnkDashboard" runat="server">Dashboard</a>
  43 |                     <a class="btn-accent" href="<%= ResolveUrl("~/Pages/Authentication/Logout.aspx") %>">
  44 |                         <i class="fa-solid fa-right-from-bracket"></i> Logout
  45 |                     </a>
  46 |                 </asp:PlaceHolder>
  47 |             </div>
  48 |         </nav>
  49 | 
  50 |         <nav class="fp-nav" id="fpNav" aria-label="Sections">
  51 |             <button type="button" data-goto="home" data-label="Home" class="active" title="Home"></button>
  52 |             <button type="button" data-goto="about" data-label="About" title="About"></button>
  53 |             <button type="button" data-goto="why" data-label="Why EduLMS" title="Why EduLMS"></button>
  54 |             <button type="button" data-goto="how" data-label="How it works" title="How it works"></button>
  55 |             <button type="button" data-goto="courses" data-label="Courses" title="Courses"></button>
  56 |             <button type="button" data-goto="contact" data-label="Contact" title="Contact"></button>
  57 |         </nav>
  58 | 
  59 |         <div class="fp-viewport" id="fpViewport">
  60 |             <div class="fp-track" id="fpTrack">
  61 | 
  62 |                 <!-- #home -->
  63 |                 <section class="fp-section is-active" id="home" data-section="home">
  64 |                     <div class="sec-body">
  65 |                         <div class="hero">
  66 |                             <div class="hero-badge anim fly-down d1"><i class="fa-solid fa-sparkles me-1"></i> Online learning platform</div>
  67 |                             <h1 class="anim fly-zoom d2">Build skills that matter.<br /><span>Learn without limits.</span></h1>
  68 |                             <p class="anim fly-up d3">
  69 |                                 EduLMS brings students and lecturers together in one secure place -
  70 |                                 browse courses, submit work, track progress, and grade with clarity.
  71 |                             </p>
  72 |                             <div class="hero-cta anim fly-up d4">
  73 |                                 <a class="btn-accent" href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">
  74 |                                     <i class="fa-solid fa-user-plus"></i> Create free account
  75 |                                 </a>
  76 |                                 <button type="button" class="btn-outline-accent" data-goto="courses">Explore courses</button>
  77 |                             </div>
  78 |                             <div class="hero-stats">
  79 |                                 <div class="stat-card anim fly-up d4">
  80 |                                     <div class="num"><asp:Literal ID="litCourseCount" runat="server" Text="0" /></div>
  81 |                                     <div class="lbl">Courses</div>
  82 |                                 </div>
  83 |                                 <div class="stat-card anim fly-up d5">
  84 |                                     <div class="num"><asp:Literal ID="litStudentCount" runat="server" Text="0" /></div>
  85 |                                     <div class="lbl">Students</div>
  86 |                                 </div>
  87 |                                 <div class="stat-card anim fly-up d6">
  88 |                                     <div class="num"><asp:Literal ID="litLecturerCount" runat="server" Text="0" /></div>
  89 |                                     <div class="lbl">Lecturers</div>
  90 |                                 </div>
  91 |                             </div>
  92 |                         </div>
  93 |                     </div>
  94 |                     <div class="scroll-cue"><span>Scroll</span><i class="fa-solid fa-chevron-down"></i></div>
  95 |                 </section>
  96 | 
  97 |                 <!-- #about -->
  98 |                 <section class="fp-section" id="about" data-section="about">
  99 |                     <div class="sec-body">
 100 |                         <div class="about-grid">
 101 |                             <div class="about-card anim fly-up d1">
 102 |                                 <h2>What is EduLMS?</h2>
 103 |                                 <p>
 104 |                                     EduLMS is a lightweight learning management system built for real classrooms and
 105 |                                     self-paced study. Lecturers publish structured courses with lessons, materials, and
 106 |                                     assessments; students enroll, learn, upload submissions, and receive feedback -
 107 |                                     while admins keep the catalogue and community healthy.
 108 |                                 </p>
 109 |                                 <p style="margin-top:0.9rem;">
 110 |                                     Everything is designed to be simple to use, fast to load, and secure by default -
 111 |                                     ideal for campus labs, assignments, and real teaching workloads.
 112 |                                 </p>
 113 |                             </div>
 114 |                             <div class="about-points">
 115 |                                 <div class="point anim fly-up d2">
 116 |                                     <i class="fa-solid fa-chalkboard-user"></i>
 117 |                                     <div>
 118 |                                         <strong>For lecturers</strong>
 119 |                                         <span>Build courses, publish assessments, and grade submissions in one place.</span>
 120 |                                     </div>
 121 |                                 </div>
 122 |                                 <div class="point anim fly-up d3">
 123 |                                     <i class="fa-solid fa-user-graduate"></i>
 124 |                                     <div>
 125 |                                         <strong>For students</strong>
 126 |                                         <span>Enroll, learn from media and materials, submit work, and track progress.</span>
 127 |                                     </div>
 128 |                                 </div>
 129 |                                 <div class="point anim fly-up d4">
 130 |                                     <i class="fa-solid fa-shield-halved"></i>
 131 |                                     <div>
 132 |                                         <strong>Secure by design</strong>
 133 |                                         <span>Hashed passwords, JWT sessions, and optional multi-factor authentication.</span>
 134 |                                     </div>
 135 |                                 </div>
 136 |                             </div>
 137 |                         </div>
 138 |                     </div>
 139 |                 </section>
 140 | 
 141 |                 <!-- #why -->
 142 |                 <section class="fp-section" id="why" data-section="why">
 143 |                     <div class="sec-body">
 144 |                         <div class="sec-head anim fly-down d1">
 145 |                             <h2>Why choose EduLMS?</h2>
 146 |                             <p>Built for focus and clarity - not clutter. Here's what makes the platform a strong choice.</p>
 147 |                         </div>
 148 |                         <div class="why-grid">
 149 |                             <article class="why-card anim fly-up d1">
 150 |                                 <div class="why-icon"><i class="fa-solid fa-layer-group"></i></div>
 151 |                                 <h3>Structured courses</h3>
 152 |                                 <p>Sections and lessons with text, video, PDF, and downloads - learners always know what's next.</p>
 153 |                             </article>
 154 |                             <article class="why-card anim fly-up d2">
 155 |                                 <div class="why-icon"><i class="fa-solid fa-file-circle-check"></i></div>
 156 |                                 <h3>Assessments that fit</h3>
 157 |                                 <p>Written tasks, quizzes, or file uploads. Grade with scores and feedback in one place.</p>
 158 |                             </article>
 159 |                             <article class="why-card anim fly-up d3">
 160 |                                 <div class="why-icon"><i class="fa-solid fa-shield-halved"></i></div>
 161 |                                 <h3>Secure by design</h3>
 162 |                                 <p>PBKDF2 hashing, JWT cookies, and optional MFA help keep accounts safe.</p>
 163 |                             </article>
 164 |                             <article class="why-card anim fly-up d4">
 165 |                                 <div class="why-icon"><i class="fa-solid fa-chart-line"></i></div>
 166 |                                 <h3>Progress you can see</h3>
 167 |                                 <p>Track enrollment, completion, and grades - clear milestones for every role.</p>
 168 |                             </article>
 169 |                             <article class="why-card anim fly-up d5">
 170 |                                 <div class="why-icon"><i class="fa-solid fa-users"></i></div>
 171 |                                 <h3>Roles that make sense</h3>
 172 |                                 <p>Students, lecturers, and admins each get tools that match their job.</p>
 173 |                             </article>
 174 |                             <article class="why-card anim fly-up d6">
 175 |                                 <div class="why-icon"><i class="fa-solid fa-bolt"></i></div>
 176 |                                 <h3>Lightweight and reliable</h3>
 177 |                                 <p>Pure SQL data access keeps the stack transparent and fast.</p>
 178 |                             </article>
 179 |                         </div>
 180 |                     </div>
 181 |                 </section>
 182 | 
 183 |                 <!-- #how -->
 184 |                 <section class="fp-section" id="how" data-section="how">
 185 |                     <div class="sec-body">
 186 |                         <div class="sec-head anim fly-down d1">
 187 |                             <h2>How it works</h2>
 188 |                             <p>Three simple steps from sign-up to success.</p>
 189 |                         </div>
 190 |                         <div class="steps">
 191 |                             <div class="step-card anim fly-up d2">
 192 |                                 <div class="step-num">1</div>
 193 |                                 <h3>Create your account</h3>
 194 |                                 <p>Register as a student or lecturer, then sign in securely - with optional MFA.</p>
 195 |                             </div>
 196 |                             <div class="step-card anim fly-up d3">
 197 |                                 <div class="step-num">2</div>
 198 |                                 <h3>Teach or enroll</h3>
 199 |                                 <p>Lecturers publish courses and assessments. Students browse and join what they need.</p>
 200 |                             </div>
 201 |                             <div class="step-card anim fly-up d4">
 202 |                                 <div class="step-num">3</div>
 203 |                                 <h3>Submit and grow</h3>
 204 |                                 <p>Upload work, get graded, track progress, and build skills with clear feedback.</p>
 205 |                             </div>
 206 |                         </div>
 207 |                     </div>
 208 |                 </section>
 209 | 
 210 |                 <!-- #courses -->
 211 |                 <section class="fp-section" id="courses" data-section="courses">
 212 |                     <div class="sec-body">
 213 |                         <div class="sec-head">
 214 |                             <h2>Featured courses</h2>
 215 |                             <p>Pulled live from EduDB - start learning today.</p>
 216 |                         </div>
 217 |                         <asp:PlaceHolder ID="phCourses" runat="server" />
 218 |                         <asp:PlaceHolder ID="phEmpty" runat="server" Visible="false">
 219 |                             <div class="empty-state">
 220 |                                 <i class="fa-regular fa-folder-open fa-2x mb-3 d-block"></i>
 221 |                                 No courses published yet. Check back soon.
 222 |                             </div>
 223 |                         </asp:PlaceHolder>
 224 |                     </div>
 225 |                 </section>
 226 | 
 227 |                 <!-- #contact (CTA + full-width footer) -->
 228 |                 <section class="fp-section" id="contact" data-section="contact">
 229 |                     <div class="sec-body wide">
 230 |                         <div class="cta-band anim fly-zoom d1">
 231 |                             <div class="cta-inner">
 232 |                                 <h2>Ready to start learning?</h2>
 233 |                                 <p>Join EduLMS free - build courses, enroll students, and grade smarter.</p>
 234 |                                 <a class="btn-light-cta" href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">
 235 |                                     Get started free <i class="fa-solid fa-arrow-right"></i>
 236 |                                 </a>
 237 |                             </div>
 238 |                         </div>
 239 | 
 240 |                         <footer class="site-footer anim fly-up d2">
 241 |                             <div class="footer-inner">
 242 |                                 <div>
 243 |                                     <div class="footer-brand">
 244 |                                         <span class="brand-icon"><i class="fa-solid fa-graduation-cap"></i></span>
 245 |                                         EduLMS
 246 |                                     </div>
 247 |                                     <p class="footer-about">
 248 |                                         A modern learning management system for courses, assessments, and progress -
 249 |                                         built for students, lecturers, and administrators.
 250 |                                     </p>
 251 |                                     <div class="footer-social">
 252 |                                         <a href="#" title="Email" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
 253 |                                         <a href="#" title="GitHub" aria-label="GitHub"><i class="fa-brands fa-github"></i></a>
 254 |                                         <a href="#" title="LinkedIn" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
 255 |                                     </div>
 256 |                                 </div>
 257 |                                 <div class="footer-col">
 258 |                                     <h4>Platform</h4>
 259 |                                     <ul>
 260 |                                         <li><a href="#about" data-goto="about">About EduLMS</a></li>
 261 |                                         <li><a href="#why" data-goto="why">Why choose us</a></li>
 262 |                                         <li><a href="#courses" data-goto="courses">Browse courses</a></li>
 263 |                                         <li><a href="#how" data-goto="how">How it works</a></li>
 264 |                                     </ul>
 265 |                                 </div>
 266 |                                 <div class="footer-col">
 267 |                                     <h4>Account</h4>
 268 |                                     <ul>
 269 |                                         <li><a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Log in</a></li>
 270 |                                         <li><a href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">Register</a></li>
 271 |                                         <li><a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Student access</a></li>
 272 |                                         <li><a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Lecturer access</a></li>
 273 |                                     </ul>
 274 |                                 </div>
 275 |                                 <div class="footer-col">
 276 |                                     <h4>Support</h4>
 277 |                                     <ul>
 278 |                                         <li><a href="mailto:support@edulms.local">support@edulms.local</a></li>
 279 |                                         <li><a href="#">Help centre</a></li>
 280 |                                         <li><a href="#">Privacy</a></li>
 281 |                                         <li><a href="#">Terms of use</a></li>
 282 |                                     </ul>
 283 |                                 </div>
 284 |                             </div>
 285 |                             <div class="footer-bottom">
 286 |                                 <span>&copy; <%= DateTime.Now.Year %> EduLMS. All rights reserved.</span>
 287 |                                 <span>Secure LMS · Hashed passwords · JWT · MFA ready</span>
 288 |                             </div>
 289 |                         </footer>
 290 |                     </div>
 291 |                 </section>
 292 | 
 293 |             </div>
 294 |         </div>
 295 |     </form>
 296 | 
 297 |     <script src="<%= ResolveUrl("~/Shared/Scripts/csrf.js") %>"></script>
 298 |     <script src="Scripts/landing.js" defer></script>
 299 | </body>
 300 | </html>
```

**Line notes**

- **L9:** CSRF anti-forgery protection.
- **L162:** Password hashing (PBKDF2).
- **L297:** CSRF anti-forgery protection.

## Source snapshot (raw)

```html
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Landing.aspx.cs" Inherits="WebAppAssignment.Pages.Landing.Landing" %>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta charset="utf-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>EduLMS - Learn without limits</title>
    <%= WebAppAssignment.Data.Security.CsrfProtection.MetaTag(Context) %>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin="anonymous" />
    <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin="anonymous" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <link href="Style/landing.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">
        <nav class="topnav" id="topnav">
            <a class="brand" href="#home" data-goto="home">
                <span class="brand-icon"><i class="fa-solid fa-graduation-cap"></i></span>
                EduLMS
            </a>
            <div class="nav-actions">
                <button type="button" class="nav-link-soft d-none d-md-inline active" data-goto="home">Home</button>
                <button type="button" class="nav-link-soft d-none d-md-inline" data-goto="about">About</button>
                <button type="button" class="nav-link-soft d-none d-md-inline" data-goto="why">Why</button>
                <button type="button" class="nav-link-soft d-none d-md-inline" data-goto="courses">Courses</button>
                <asp:PlaceHolder ID="phGuest" runat="server">
                    <a class="btn-ghost" href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Log in</a>
                    <a class="btn-accent" href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">
                        Get started <i class="fa-solid fa-arrow-right" style="font-size:0.8rem;"></i>
                    </a>
                </asp:PlaceHolder>
                <asp:PlaceHolder ID="phUser" runat="server" Visible="false">
                    <span class="btn-ghost" style="cursor:default;">
                        Hi, <asp:Literal ID="litUserName" runat="server" />
                    </span>
                    <a class="btn-outline-accent" id="lnkDashboard" runat="server">Dashboard</a>
                    <a class="btn-accent" href="<%= ResolveUrl("~/Pages/Authentication/Logout.aspx") %>">
                        <i class="fa-solid fa-right-from-bracket"></i> Logout
                    </a>
                </asp:PlaceHolder>
            </div>
        </nav>

        <nav class="fp-nav" id="fpNav" aria-label="Sections">
            <button type="button" data-goto="home" data-label="Home" class="active" title="Home"></button>
            <button type="button" data-goto="about" data-label="About" title="About"></button>
            <button type="button" data-goto="why" data-label="Why EduLMS" title="Why EduLMS"></button>
            <button type="button" data-goto="how" data-label="How it works" title="How it works"></button>
            <button type="button" data-goto="courses" data-label="Courses" title="Courses"></button>
            <button type="button" data-goto="contact" data-label="Contact" title="Contact"></button>
        </nav>

        <div class="fp-viewport" id="fpViewport">
            <div class="fp-track" id="fpTrack">

                <!-- #home -->
                <section class="fp-section is-active" id="home" data-section="home">
                    <div class="sec-body">
                        <div class="hero">
                            <div class="hero-badge anim fly-down d1"><i class="fa-solid fa-sparkles me-1"></i> Online learning platform</div>
                            <h1 class="anim fly-zoom d2">Build skills that matter.<br /><span>Learn without limits.</span></h1>
                            <p class="anim fly-up d3">
                                EduLMS brings students and lecturers together in one secure place -
                                browse courses, submit work, track progress, and grade with clarity.
                            </p>
                            <div class="hero-cta anim fly-up d4">
                                <a class="btn-accent" href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">
                                    <i class="fa-solid fa-user-plus"></i> Create free account
                                </a>
                                <button type="button" class="btn-outline-accent" data-goto="courses">Explore courses</button>
                            </div>
                            <div class="hero-stats">
                                <div class="stat-card anim fly-up d4">
                                    <div class="num"><asp:Literal ID="litCourseCount" runat="server" Text="0" /></div>
                                    <div class="lbl">Courses</div>
                                </div>
                                <div class="stat-card anim fly-up d5">
                                    <div class="num"><asp:Literal ID="litStudentCount" runat="server" Text="0" /></div>
                                    <div class="lbl">Students</div>
                                </div>
                                <div class="stat-card anim fly-up d6">
                                    <div class="num"><asp:Literal ID="litLecturerCount" runat="server" Text="0" /></div>
                                    <div class="lbl">Lecturers</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="scroll-cue"><span>Scroll</span><i class="fa-solid fa-chevron-down"></i></div>
                </section>

                <!-- #about -->
                <section class="fp-section" id="about" data-section="about">
                    <div class="sec-body">
                        <div class="about-grid">
                            <div class="about-card anim fly-up d1">
                                <h2>What is EduLMS?</h2>
                                <p>
                                    EduLMS is a lightweight learning management system built for real classrooms and
                                    self-paced study. Lecturers publish structured courses with lessons, materials, and
                                    assessments; students enroll, learn, upload submissions, and receive feedback -
                                    while admins keep the catalogue and community healthy.
                                </p>
                                <p style="margin-top:0.9rem;">
                                    Everything is designed to be simple to use, fast to load, and secure by default -
                                    ideal for campus labs, assignments, and real teaching workloads.
                                </p>
                            </div>
                            <div class="about-points">
                                <div class="point anim fly-up d2">
                                    <i class="fa-solid fa-chalkboard-user"></i>
                                    <div>
                                        <strong>For lecturers</strong>
                                        <span>Build courses, publish assessments, and grade submissions in one place.</span>
                                    </div>
                                </div>
                                <div class="point anim fly-up d3">
                                    <i class="fa-solid fa-user-graduate"></i>
                                    <div>
                                        <strong>For students</strong>
                                        <span>Enroll, learn from media and materials, submit work, and track progress.</span>
                                    </div>
                                </div>
                                <div class="point anim fly-up d4">
                                    <i class="fa-solid fa-shield-halved"></i>
                                    <div>
                                        <strong>Secure by design</strong>
                                        <span>Hashed passwords, JWT sessions, and optional multi-factor authentication.</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- #why -->
                <section class="fp-section" id="why" data-section="why">
                    <div class="sec-body">
                        <div class="sec-head anim fly-down d1">
                            <h2>Why choose EduLMS?</h2>
                            <p>Built for focus and clarity - not clutter. Here's what makes the platform a strong choice.</p>
                        </div>
                        <div class="why-grid">
                            <article class="why-card anim fly-up d1">
                                <div class="why-icon"><i class="fa-solid fa-layer-group"></i></div>
                                <h3>Structured courses</h3>
                                <p>Sections and lessons with text, video, PDF, and downloads - learners always know what's next.</p>
                            </article>
                            <article class="why-card anim fly-up d2">
                                <div class="why-icon"><i class="fa-solid fa-file-circle-check"></i></div>
                                <h3>Assessments that fit</h3>
                                <p>Written tasks, quizzes, or file uploads. Grade with scores and feedback in one place.</p>
                            </article>
                            <article class="why-card anim fly-up d3">
                                <div class="why-icon"><i class="fa-solid fa-shield-halved"></i></div>
                                <h3>Secure by design</h3>
                                <p>PBKDF2 hashing, JWT cookies, and optional MFA help keep accounts safe.</p>
                            </article>
                            <article class="why-card anim fly-up d4">
                                <div class="why-icon"><i class="fa-solid fa-chart-line"></i></div>
                                <h3>Progress you can see</h3>
                                <p>Track enrollment, completion, and grades - clear milestones for every role.</p>
                            </article>
                            <article class="why-card anim fly-up d5">
                                <div class="why-icon"><i class="fa-solid fa-users"></i></div>
                                <h3>Roles that make sense</h3>
                                <p>Students, lecturers, and admins each get tools that match their job.</p>
                            </article>
                            <article class="why-card anim fly-up d6">
                                <div class="why-icon"><i class="fa-solid fa-bolt"></i></div>
                                <h3>Lightweight and reliable</h3>
                                <p>Pure SQL data access keeps the stack transparent and fast.</p>
                            </article>
                        </div>
                    </div>
                </section>

                <!-- #how -->
                <section class="fp-section" id="how" data-section="how">
                    <div class="sec-body">
                        <div class="sec-head anim fly-down d1">
                            <h2>How it works</h2>
                            <p>Three simple steps from sign-up to success.</p>
                        </div>
                        <div class="steps">
                            <div class="step-card anim fly-up d2">
                                <div class="step-num">1</div>
                                <h3>Create your account</h3>
                                <p>Register as a student or lecturer, then sign in securely - with optional MFA.</p>
                            </div>
                            <div class="step-card anim fly-up d3">
                                <div class="step-num">2</div>
                                <h3>Teach or enroll</h3>
                                <p>Lecturers publish courses and assessments. Students browse and join what they need.</p>
                            </div>
                            <div class="step-card anim fly-up d4">
                                <div class="step-num">3</div>
                                <h3>Submit and grow</h3>
                                <p>Upload work, get graded, track progress, and build skills with clear feedback.</p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- #courses -->
                <section class="fp-section" id="courses" data-section="courses">
                    <div class="sec-body">
                        <div class="sec-head">
                            <h2>Featured courses</h2>
                            <p>Pulled live from EduDB - start learning today.</p>
                        </div>
                        <asp:PlaceHolder ID="phCourses" runat="server" />
                        <asp:PlaceHolder ID="phEmpty" runat="server" Visible="false">
                            <div class="empty-state">
                                <i class="fa-regular fa-folder-open fa-2x mb-3 d-block"></i>
                                No courses published yet. Check back soon.
                            </div>
                        </asp:PlaceHolder>
                    </div>
                </section>

                <!-- #contact (CTA + full-width footer) -->
                <section class="fp-section" id="contact" data-section="contact">
                    <div class="sec-body wide">
                        <div class="cta-band anim fly-zoom d1">
                            <div class="cta-inner">
                                <h2>Ready to start learning?</h2>
                                <p>Join EduLMS free - build courses, enroll students, and grade smarter.</p>
                                <a class="btn-light-cta" href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">
                                    Get started free <i class="fa-solid fa-arrow-right"></i>
                                </a>
                            </div>
                        </div>

                        <footer class="site-footer anim fly-up d2">
                            <div class="footer-inner">
                                <div>
                                    <div class="footer-brand">
                                        <span class="brand-icon"><i class="fa-solid fa-graduation-cap"></i></span>
                                        EduLMS
                                    </div>
                                    <p class="footer-about">
                                        A modern learning management system for courses, assessments, and progress -
                                        built for students, lecturers, and administrators.
                                    </p>
                                    <div class="footer-social">
                                        <a href="#" title="Email" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
                                        <a href="#" title="GitHub" aria-label="GitHub"><i class="fa-brands fa-github"></i></a>
                                        <a href="#" title="LinkedIn" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                                    </div>
                                </div>
                                <div class="footer-col">
                                    <h4>Platform</h4>
                                    <ul>
                                        <li><a href="#about" data-goto="about">About EduLMS</a></li>
                                        <li><a href="#why" data-goto="why">Why choose us</a></li>
                                        <li><a href="#courses" data-goto="courses">Browse courses</a></li>
                                        <li><a href="#how" data-goto="how">How it works</a></li>
                                    </ul>
                                </div>
                                <div class="footer-col">
                                    <h4>Account</h4>
                                    <ul>
                                        <li><a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Log in</a></li>
                                        <li><a href="<%= ResolveUrl("~/Pages/Authentication/Register.aspx") %>">Register</a></li>
                                        <li><a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Student access</a></li>
                                        <li><a href="<%= ResolveUrl("~/Pages/Authentication/Login.aspx") %>">Lecturer access</a></li>
                                    </ul>
                                </div>
                                <div class="footer-col">
                                    <h4>Support</h4>
                                    <ul>
                                        <li><a href="mailto:support@edulms.local">support@edulms.local</a></li>
                                        <li><a href="#">Help centre</a></li>
                                        <li><a href="#">Privacy</a></li>
                                        <li><a href="#">Terms of use</a></li>
                                    </ul>
                                </div>
                            </div>
                            <div class="footer-bottom">
                                <span>&copy; <%= DateTime.Now.Year %> EduLMS. All rights reserved.</span>
                                <span>Secure LMS · Hashed passwords · JWT · MFA ready</span>
                            </div>
                        </footer>
                    </div>
                </section>

            </div>
        </div>
    </form>

    <script src="<%= ResolveUrl("~/Shared/Scripts/csrf.js") %>"></script>
    <script src="Scripts/landing.js" defer></script>
</body>
</html>

```
