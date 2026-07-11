# Landing.aspx.cs
**Source:** `Pages/Landing/Landing.aspx.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Public marketing + course catalog. Shows published courses only (`IsPublished`). Guests can browse; Enroll sends unauthenticated users to Login.

## File overview

- **Total lines:** 214
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 18:** `cs` (`var`) — **Connection string text.**
- **Line 40:** `role` (`string`) — **User role code or name (Admin/Student/Lecturer).**
- **Line 42:** `dash` (`string`) — **Holds “dash” for this scope. (text)**
- **Line 108:** `sql` (`string`) — **SQL query text (should use parameters, not raw user input).**
- **Line 113:** `r` (`SqlDataReader`) — **Usually one database row (DataRow) in query loops.**
- **Line 114:** `cmd` (`SqlCommand`) — **SqlCommand — the SQL statement + parameters object.**
- **Line 132:** `grid` (`var`) — **Identifier (`grid`) — database primary/foreign key.**
- **Line 137:** `count` (`int`) — **Number of matching records.**
- **Line 141:** `name` (`string`) — **Display name of user/course/criterion.**
- **Line 142:** `desc` (`string`) — **Description text (may embed <<<META>>> JSON).**
- **Line 143:** `bg` (`string`) — **Holds “bg” for this scope. (text)**
- **Line 144:** `cat` (`string`) — **Date/time value. (text)**
- **Line 145:** `level` (`string`) — **Holds “level” for this scope. (text)**
- **Line 146:** `rating` (`decimal`) — **Holds “rating” for this scope. (number/score)**
- **Line 147:** `img` (`string`) — **Image element or image path.**
- **Line 202:** `o` (`var`) — **Holds “o” for this scope.**

## Functions / methods (6 found)

### `Page_Load` — lines 22–31

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### Explanation

- **Purpose:** Implements `Page_Load`.
- **Page lifecycle:** Runs on every request; `IsPostBack` distinguishes first load vs postback.
- **Parameters (what each means):**
- `sender` (`object`) — Holds “sender” for this scope.
- `e` (`EventArgs`) — Often email string (C#) or DOM event (JS).

#### Line-by-line (this function)

```csharp
  22 | 
  23 |         protected void Page_Load(object sender, EventArgs e)
  24 |         {
  25 |             if (!IsPostBack)
  26 |             {
  27 |                 BindAuthChrome();
  28 |                 LoadStats();
  29 |                 LoadCourses();
  30 |             }
  31 |         }
```

**Line notes** (what code + variables mean)

- **L23:** Page load entry (GET or postback).
- **L25:** False on first open; true after postback.

---

### `BindAuthChrome` — lines 32–55

```csharp
private void BindAuthChrome()
```

#### Explanation

- **Purpose:** Implements `BindAuthChrome`.
- **Session:** Reads/writes ASP.NET Session.
- **Local variables (what each means):**
- `role` (`string`) — User role code or name (Admin/Student/Lecturer).  Read from ASP.NET Session.
- `dash` (`string`) — Holds “dash” for this scope. (text)

#### Line-by-line (this function)

```csharp
  32 | 
  33 |         private void BindAuthChrome()
  34 |         {
  35 |             if (Session["UserID"] != null)
  36 |             {
  37 |                 phGuest.Visible = false;
  38 |                 phUser.Visible = true;
  39 |                 litUserName.Text = HttpUtility.HtmlEncode(Session["UserName"] as string ?? "User");
  40 | 
  41 |                 string role = (Session["UserRole"] as string ?? "").Trim().ToLowerInvariant();
  42 |                 string dash = ResolveUrl("~/Pages/Landing/Landing.aspx");
  43 |                 if (role == "0" || role == "admin")
  44 |                 dash = ResolveUrl("~/Pages/Admin/ADashboard.aspx");
  45 |                 else if (role == "2" || role == "teacher" || role == "lecturer")
  46 |                 dash = ResolveUrl("~/Pages/Lecturer/Dashboard.aspx");
  47 | 
  48 |                 lnkDashboard.HRef = dash;
  49 |             }
  50 |             else
  51 |             {
  52 |                 phGuest.Visible = true;
  53 |                 phUser.Visible = false;
  54 |             }
  55 |         }
```

**Line notes** (what code + variables mean)

- **L35:** Server session for logged-in user.
- **L39:** Server session for logged-in user.
- **L41:** Server session for logged-in user. | `role` means: User role code or name (Admin/Student/Lecturer).  Read from ASP.NET Session.
- **L42:** `dash` means: Holds “dash” for this scope. (text)

---

### `LoadStats` — lines 56–96

```csharp
private void LoadStats()
```

#### Explanation

- **Purpose:** Implements `LoadStats`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Ownership:** Checks course belongs to current lecturer (IDOR protection).
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  56 | 
  57 |         private void LoadStats()
  58 |         {
  59 |             try
  60 |             {
  61 |                 using (var conn = new SqlConnection(ConnString))
  62 |                 {
  63 |                     conn.Open();
  64 | 
  65 |                     litCourseCount.Text = ScalarInt(conn, "SELECT COUNT(*) FROM Courses").ToString("N0");
  66 | 
  67 |                     // Distinct enrolled students
  68 |                     try
  69 |                     {
  70 |                         litStudentCount.Text = ScalarInt(conn,
  71 |                         "SELECT COUNT(DISTINCT StudentUID) FROM Enrollments").ToString("N0");
  72 |                     }
  73 |                     catch
  74 |                     {
  75 |                         litStudentCount.Text = ScalarInt(conn,
  76 |                         "SELECT COUNT(*) FROM Users WHERE Role IN ('1','Student','student')").ToString("N0");
  77 |                     }
  78 | 
  79 |                     try
  80 |                     {
  81 |                         litLecturerCount.Text = ScalarInt(conn,
  82 |                         "SELECT COUNT(DISTINCT LecturerUID) FROM Courses").ToString("N0");
  83 |                     }
  84 |                     catch
  85 |                     {
  86 |                         litLecturerCount.Text = "0";
  87 |                     }
  88 |                 }
  89 |             }
  90 |             catch
  91 |             {
  92 |                 litCourseCount.Text = "0";
  93 |                 litStudentCount.Text = "0";
  94 |                 litLecturerCount.Text = "0";
  95 |             }
  96 |         }
```

**Line notes** (what code + variables mean)

- **L59:** Error handling block.
- **L61:** Import namespace/types.
- **L68:** Error handling block.
- **L73:** Handle/log exception.
- **L79:** Error handling block.
- **L82:** Owner lecturer foreign key.
- **L84:** Handle/log exception.
- **L90:** Handle/log exception.

---

### `LoadCourses` — lines 97–196

```csharp
private void LoadCourses()
```

#### Explanation

- **Purpose:** Implements `LoadCourses`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Publish/draft:** Touches `Courses.IsPublished` / Landing visibility.
- **Pattern:** Read/load data for display.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `cmd` (`SqlCommand`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- `grid` (`var`) — Identifier (`grid`) — database primary/foreign key.  Newly constructed object.
- `count` (`int`) — Number of matching records.  Literal number `0`.
- `name` (`string`) — Display name of user/course/criterion.
- `desc` (`string`) — Description text (may embed <<<META>>> JSON).
- `bg` (`string`) — Holds “bg” for this scope. (text)
- `cat` (`string`) — Date/time value. (text)
- `level` (`string`) — Holds “level” for this scope. (text)
- `rating` (`decimal`) — Holds “rating” for this scope. (number/score)
- `img` (`string`) — Image element or image path.

#### Line-by-line (this function)

```csharp
  97 | 
  98 |         private void LoadCourses()
  99 |         {
 100 |             phCourses.Controls.Clear();
 101 |             try
 102 |             {
 103 |                 try { WebAppAssignment.Data.CourseSchema.Ensure(); } catch { }
 104 | 
 105 |                 using (var conn = new SqlConnection(ConnString))
 106 |                 {
 107 |                     conn.Open();
 108 |                     string sql = @"
 109 | SELECT TOP 12 CID, Name, Description, Rating, BgImg, Categories, Level
 110 | FROM Courses
 111 | WHERE ISNULL(IsPublished, 1) = 1
 112 | ORDER BY CID DESC";
 113 |                     SqlDataReader r = null;
 114 |                     SqlCommand cmd = new SqlCommand(sql, conn);
 115 |                     try
 116 |                     {
 117 |                         r = cmd.ExecuteReader();
 118 |                     }
 119 |                     catch
 120 |                     {
 121 |                         cmd.Dispose();
 122 |                         cmd = new SqlCommand(@"
 123 | SELECT TOP 12 CID, Name, Description, Rating, BgImg, Categories, Level
 124 | FROM Courses
 125 | ORDER BY CID DESC", conn);
 126 |                         r = cmd.ExecuteReader();
 127 |                     }
 128 | 
 129 |                     using (cmd)
 130 |                     using (r)
 131 |                     {
 132 |                         var grid = new StringBuilder();
 133 |                         grid.Append("<div class='course-carousel' id='courseCarousel'>");
 134 |                         grid.Append("<button type='button' class='cc-arrow cc-prev' aria-label='Previous courses'><i class='fa-solid fa-chevron-left'></i></button>");
 135 |                         grid.Append("<div class='cc-viewport'>");
 136 |                         grid.Append("<div class='cc-track' id='courseTrack'>");
 137 |                         int count = 0;
 138 |                         while (r.Read())
 139 |                         {
 140 |                             count++;
 141 |                             string name = Safe(r["Name"]);
 142 |                             string desc = Safe(r["Description"]);
 143 |                             string bg = Safe(r["BgImg"]);
 144 |                             string cat = Safe(r["Categories"]);
 145 |                             string level = Safe(r["Level"]);
 146 |                             decimal rating = r["Rating"] == DBNull.Value ? 0 : Convert.ToDecimal(r["Rating"]);
 147 | 
 148 |                             string img = string.IsNullOrWhiteSpace(bg)
 149 |                                 ? "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600"
 150 |                                 : bg;
 151 | 
 152 |                             grid.Append("<article class='course-card'>");
 153 |                             grid.AppendFormat(
 154 |                                 "<img class='thumb' src='{0}' alt='{1}' onerror=\"this.src='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600'\" />",
 155 |                                 HttpUtility.HtmlAttributeEncode(img), HttpUtility.HtmlAttributeEncode(name));
 156 |                             grid.Append("<div class='body'>");
 157 |                             grid.Append("<div class='meta'>");
 158 |                             if (!string.IsNullOrEmpty(cat))
 159 |                                 grid.AppendFormat("<span class='pill'>{0}</span>", HttpUtility.HtmlEncode(cat));
 160 |                             if (!string.IsNullOrEmpty(level))
 161 |                                 grid.AppendFormat("<span class='pill level'>{0}</span>", HttpUtility.HtmlEncode(level));
 162 |                             grid.Append("</div>");
 163 |                             grid.AppendFormat("<h3>{0}</h3>", HttpUtility.HtmlEncode(name));
 164 |                             grid.AppendFormat("<p class='desc'>{0}</p>", HttpUtility.HtmlEncode(
 165 |                                 string.IsNullOrWhiteSpace(desc) ? "No description provided." : desc));
 166 |                             grid.Append("<div class='card-footer-row'>");
 167 |                             if (rating > 0)
 168 |                                 grid.AppendFormat("<span class='rating'><i class='fa-solid fa-star'></i> {0:0.0}</span>", rating);
 169 |                             else
 170 |                                 grid.Append("<span class='text-muted'>New</span>");
 171 |                             grid.AppendFormat(
 172 |                                 "<a class='btn-accent' style='padding:0.35rem 0.85rem;font-size:0.8rem;' href='{0}'>Enroll</a>",
 173 |                                 ResolveUrl("~/Pages/Authentication/Login.aspx"));
 174 |                             grid.Append("</div></div></article>");
 175 |                         }
 176 |                         grid.Append("</div></div>");
 177 |                         grid.Append("<button type='button' class='cc-arrow cc-next' aria-label='Next courses'><i class='fa-solid fa-chevron-right'></i></button>");
 178 |                         grid.Append("</div>");
 179 | 
 180 |                         if (count == 0)
 181 |                         {
 182 |                             phEmpty.Visible = true;
 183 |                         }
 184 |                         else
 185 |                         {
 186 |                             phEmpty.Visible = false;
 187 |                             phCourses.Controls.Add(new LiteralControl(grid.ToString()));
 188 |                         }
 189 |                     }
 190 |                 }
 191 |             }
 192 |             catch
 193 |             {
 194 |                 phEmpty.Visible = true;
 195 |             }
 196 |         }
```

**Line notes** (what code + variables mean)

- **L101:** Error handling block.
- **L103:** Error handling block.
- **L105:** Import namespace/types.
- **L108:** `sql` means: SQL query text (should use parameters, not raw user input).
- **L111:** Course publish flag for Landing catalog.
- **L114:** Database access (pure SQL). | `cmd` means: SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- **L115:** Error handling block.
- **L119:** Handle/log exception.
- **L122:** Database access (pure SQL).
- **L129:** Import namespace/types.
- **L130:** Import namespace/types.
- **L132:** `grid` means: Identifier (`grid`) — database primary/foreign key.  Newly constructed object.
- **L137:** `count` means: Number of matching records.  Literal number `0`.
- **L141:** `name` means: Display name of user/course/criterion.
- **L142:** `desc` means: Description text (may embed <<<META>>> JSON).
- **L143:** `bg` means: Holds “bg” for this scope. (text)
- **L144:** `cat` means: Date/time value. (text)
- **L145:** `level` means: Holds “level” for this scope. (text)
- **L146:** Null-safe read from database values. | `rating` means: Holds “rating” for this scope. (number/score)
- **L148:** `img` means: Image element or image path.
- **L159:** Encode text to reduce XSS risk.
- **L161:** Encode text to reduce XSS risk.
- **L163:** Encode text to reduce XSS risk.
- **L164:** Encode text to reduce XSS risk.
- **L192:** Handle/log exception.

---

### `ScalarInt` — lines 197–206

```csharp
private static int ScalarInt(SqlConnection conn, string sql)
```

#### Explanation

- **Purpose:** Implements `ScalarInt`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- **Local variables (what each means):**
- `cmd` (`var`) — SqlCommand — the SQL statement + parameters object.  Newly constructed object.

#### Line-by-line (this function)

```csharp
 197 | 
 198 |         private static int ScalarInt(SqlConnection conn, string sql)
 199 |         {
 200 |             using (var cmd = new SqlCommand(sql, conn))
 201 |             {
 202 |                 var o = cmd.ExecuteScalar();
 203 |                 if (o == null || o == DBNull.Value) return 0;
 204 |                 return Convert.ToInt32(o);
 205 |             }
 206 |         }
```

**Line notes** (what code + variables mean)

- **L198:** Database access (pure SQL).
- **L200:** Import namespace/types.
- **L202:** Run SQL; return table / rows / scalar. | `o` means: Holds “o” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY).
- **L203:** Null-safe read from database values.

---

### `Safe` — lines 207–212

```csharp
private static string Safe(object o)
```

#### Explanation

- **Purpose:** Implements `Safe`.
- **Parameters (what each means):**
- `o` (`object`) — Holds “o” for this scope.

#### Line-by-line (this function)

```csharp
 207 | 
 208 |         private static string Safe(object o)
 209 |         {
 210 |             if (o == null || o == DBNull.Value) return "";
 211 |             return o.ToString();
 212 |         }
```

**Line notes** (what code + variables mean)

- **L210:** Null-safe read from database values.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```csharp
   1 | using System;
   2 | using System.Configuration;
   3 | using System.Data;
   4 | using System.Data.SqlClient;
   5 | using System.Text;
   6 | using System.Web;
   7 | using System.Web.UI;
   8 | using System.Web.UI.HtmlControls;
   9 | 
  10 | namespace WebAppAssignment.Pages.Landing
  11 | {
  12 |     public partial class Landing : Page
  13 |     {
  14 |         private string ConnString
  15 |         {
  16 |             get
  17 |             {
  18 |                 var cs = ConfigurationManager.ConnectionStrings["MyDbConn"];
  19 |                 return cs != null ? cs.ConnectionString : string.Empty;
  20 |             }
  21 |         }
  22 | 
  23 |         protected void Page_Load(object sender, EventArgs e)
  24 |         {
  25 |             if (!IsPostBack)
  26 |             {
  27 |                 BindAuthChrome();
  28 |                 LoadStats();
  29 |                 LoadCourses();
  30 |             }
  31 |         }
  32 | 
  33 |         private void BindAuthChrome()
  34 |         {
  35 |             if (Session["UserID"] != null)
  36 |             {
  37 |                 phGuest.Visible = false;
  38 |                 phUser.Visible = true;
  39 |                 litUserName.Text = HttpUtility.HtmlEncode(Session["UserName"] as string ?? "User");
  40 | 
  41 |                 string role = (Session["UserRole"] as string ?? "").Trim().ToLowerInvariant();
  42 |                 string dash = ResolveUrl("~/Pages/Landing/Landing.aspx");
  43 |                 if (role == "0" || role == "admin")
  44 |                 dash = ResolveUrl("~/Pages/Admin/ADashboard.aspx");
  45 |                 else if (role == "2" || role == "teacher" || role == "lecturer")
  46 |                 dash = ResolveUrl("~/Pages/Lecturer/Dashboard.aspx");
  47 | 
  48 |                 lnkDashboard.HRef = dash;
  49 |             }
  50 |             else
  51 |             {
  52 |                 phGuest.Visible = true;
  53 |                 phUser.Visible = false;
  54 |             }
  55 |         }
  56 | 
  57 |         private void LoadStats()
  58 |         {
  59 |             try
  60 |             {
  61 |                 using (var conn = new SqlConnection(ConnString))
  62 |                 {
  63 |                     conn.Open();
  64 | 
  65 |                     litCourseCount.Text = ScalarInt(conn, "SELECT COUNT(*) FROM Courses").ToString("N0");
  66 | 
  67 |                     // Distinct enrolled students
  68 |                     try
  69 |                     {
  70 |                         litStudentCount.Text = ScalarInt(conn,
  71 |                         "SELECT COUNT(DISTINCT StudentUID) FROM Enrollments").ToString("N0");
  72 |                     }
  73 |                     catch
  74 |                     {
  75 |                         litStudentCount.Text = ScalarInt(conn,
  76 |                         "SELECT COUNT(*) FROM Users WHERE Role IN ('1','Student','student')").ToString("N0");
  77 |                     }
  78 | 
  79 |                     try
  80 |                     {
  81 |                         litLecturerCount.Text = ScalarInt(conn,
  82 |                         "SELECT COUNT(DISTINCT LecturerUID) FROM Courses").ToString("N0");
  83 |                     }
  84 |                     catch
  85 |                     {
  86 |                         litLecturerCount.Text = "0";
  87 |                     }
  88 |                 }
  89 |             }
  90 |             catch
  91 |             {
  92 |                 litCourseCount.Text = "0";
  93 |                 litStudentCount.Text = "0";
  94 |                 litLecturerCount.Text = "0";
  95 |             }
  96 |         }
  97 | 
  98 |         private void LoadCourses()
  99 |         {
 100 |             phCourses.Controls.Clear();
 101 |             try
 102 |             {
 103 |                 try { WebAppAssignment.Data.CourseSchema.Ensure(); } catch { }
 104 | 
 105 |                 using (var conn = new SqlConnection(ConnString))
 106 |                 {
 107 |                     conn.Open();
 108 |                     string sql = @"
 109 | SELECT TOP 12 CID, Name, Description, Rating, BgImg, Categories, Level
 110 | FROM Courses
 111 | WHERE ISNULL(IsPublished, 1) = 1
 112 | ORDER BY CID DESC";
 113 |                     SqlDataReader r = null;
 114 |                     SqlCommand cmd = new SqlCommand(sql, conn);
 115 |                     try
 116 |                     {
 117 |                         r = cmd.ExecuteReader();
 118 |                     }
 119 |                     catch
 120 |                     {
 121 |                         cmd.Dispose();
 122 |                         cmd = new SqlCommand(@"
 123 | SELECT TOP 12 CID, Name, Description, Rating, BgImg, Categories, Level
 124 | FROM Courses
 125 | ORDER BY CID DESC", conn);
 126 |                         r = cmd.ExecuteReader();
 127 |                     }
 128 | 
 129 |                     using (cmd)
 130 |                     using (r)
 131 |                     {
 132 |                         var grid = new StringBuilder();
 133 |                         grid.Append("<div class='course-carousel' id='courseCarousel'>");
 134 |                         grid.Append("<button type='button' class='cc-arrow cc-prev' aria-label='Previous courses'><i class='fa-solid fa-chevron-left'></i></button>");
 135 |                         grid.Append("<div class='cc-viewport'>");
 136 |                         grid.Append("<div class='cc-track' id='courseTrack'>");
 137 |                         int count = 0;
 138 |                         while (r.Read())
 139 |                         {
 140 |                             count++;
 141 |                             string name = Safe(r["Name"]);
 142 |                             string desc = Safe(r["Description"]);
 143 |                             string bg = Safe(r["BgImg"]);
 144 |                             string cat = Safe(r["Categories"]);
 145 |                             string level = Safe(r["Level"]);
 146 |                             decimal rating = r["Rating"] == DBNull.Value ? 0 : Convert.ToDecimal(r["Rating"]);
 147 | 
 148 |                             string img = string.IsNullOrWhiteSpace(bg)
 149 |                                 ? "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600"
 150 |                                 : bg;
 151 | 
 152 |                             grid.Append("<article class='course-card'>");
 153 |                             grid.AppendFormat(
 154 |                                 "<img class='thumb' src='{0}' alt='{1}' onerror=\"this.src='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600'\" />",
 155 |                                 HttpUtility.HtmlAttributeEncode(img), HttpUtility.HtmlAttributeEncode(name));
 156 |                             grid.Append("<div class='body'>");
 157 |                             grid.Append("<div class='meta'>");
 158 |                             if (!string.IsNullOrEmpty(cat))
 159 |                                 grid.AppendFormat("<span class='pill'>{0}</span>", HttpUtility.HtmlEncode(cat));
 160 |                             if (!string.IsNullOrEmpty(level))
 161 |                                 grid.AppendFormat("<span class='pill level'>{0}</span>", HttpUtility.HtmlEncode(level));
 162 |                             grid.Append("</div>");
 163 |                             grid.AppendFormat("<h3>{0}</h3>", HttpUtility.HtmlEncode(name));
 164 |                             grid.AppendFormat("<p class='desc'>{0}</p>", HttpUtility.HtmlEncode(
 165 |                                 string.IsNullOrWhiteSpace(desc) ? "No description provided." : desc));
 166 |                             grid.Append("<div class='card-footer-row'>");
 167 |                             if (rating > 0)
 168 |                                 grid.AppendFormat("<span class='rating'><i class='fa-solid fa-star'></i> {0:0.0}</span>", rating);
 169 |                             else
 170 |                                 grid.Append("<span class='text-muted'>New</span>");
 171 |                             grid.AppendFormat(
 172 |                                 "<a class='btn-accent' style='padding:0.35rem 0.85rem;font-size:0.8rem;' href='{0}'>Enroll</a>",
 173 |                                 ResolveUrl("~/Pages/Authentication/Login.aspx"));
 174 |                             grid.Append("</div></div></article>");
 175 |                         }
 176 |                         grid.Append("</div></div>");
 177 |                         grid.Append("<button type='button' class='cc-arrow cc-next' aria-label='Next courses'><i class='fa-solid fa-chevron-right'></i></button>");
 178 |                         grid.Append("</div>");
 179 | 
 180 |                         if (count == 0)
 181 |                         {
 182 |                             phEmpty.Visible = true;
 183 |                         }
 184 |                         else
 185 |                         {
 186 |                             phEmpty.Visible = false;
 187 |                             phCourses.Controls.Add(new LiteralControl(grid.ToString()));
 188 |                         }
 189 |                     }
 190 |                 }
 191 |             }
 192 |             catch
 193 |             {
 194 |                 phEmpty.Visible = true;
 195 |             }
 196 |         }
 197 | 
 198 |         private static int ScalarInt(SqlConnection conn, string sql)
 199 |         {
 200 |             using (var cmd = new SqlCommand(sql, conn))
 201 |             {
 202 |                 var o = cmd.ExecuteScalar();
 203 |                 if (o == null || o == DBNull.Value) return 0;
 204 |                 return Convert.ToInt32(o);
 205 |             }
 206 |         }
 207 | 
 208 |         private static string Safe(object o)
 209 |         {
 210 |             if (o == null || o == DBNull.Value) return "";
 211 |             return o.ToString();
 212 |         }
 213 |     }
 214 | }
```

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L5:** Import namespace/types.
- **L6:** Import namespace/types.
- **L7:** Import namespace/types.
- **L8:** Import namespace/types.
- **L10:** C# namespace grouping.
- **L18:** `cs` means: Connection string text.  Read from Web.config.
- **L23:** Page load entry (GET or postback).
- **L25:** False on first open; true after postback.
- **L35:** Server session for logged-in user.
- **L39:** Server session for logged-in user.
- **L41:** Server session for logged-in user. | `role` means: User role code or name (Admin/Student/Lecturer).  Read from ASP.NET Session.
- **L42:** `dash` means: Holds “dash” for this scope. (text)
- **L59:** Error handling block.
- **L61:** Import namespace/types.
- **L68:** Error handling block.
- **L73:** Handle/log exception.
- **L79:** Error handling block.
- **L82:** Owner lecturer foreign key.
- **L84:** Handle/log exception.
- **L90:** Handle/log exception.
- **L101:** Error handling block.
- **L103:** Error handling block.
- **L105:** Import namespace/types.
- **L108:** `sql` means: SQL query text (should use parameters, not raw user input).
- **L111:** Course publish flag for Landing catalog.
- **L114:** Database access (pure SQL). | `cmd` means: SqlCommand — the SQL statement + parameters object.  Newly constructed object.
- **L115:** Error handling block.
- **L119:** Handle/log exception.
- **L122:** Database access (pure SQL).
- **L129:** Import namespace/types.
- **L130:** Import namespace/types.
- **L132:** `grid` means: Identifier (`grid`) — database primary/foreign key.  Newly constructed object.
- **L137:** `count` means: Number of matching records.  Literal number `0`.
- **L141:** `name` means: Display name of user/course/criterion.
- **L142:** `desc` means: Description text (may embed <<<META>>> JSON).
- **L143:** `bg` means: Holds “bg” for this scope. (text)
- **L144:** `cat` means: Date/time value. (text)
- **L145:** `level` means: Holds “level” for this scope. (text)
- **L146:** Null-safe read from database values. | `rating` means: Holds “rating” for this scope. (number/score)
- **L148:** `img` means: Image element or image path.
- **L159:** Encode text to reduce XSS risk.
- **L161:** Encode text to reduce XSS risk.
- **L163:** Encode text to reduce XSS risk.
- **L164:** Encode text to reduce XSS risk.
- **L192:** Handle/log exception.
- **L198:** Database access (pure SQL).
- **L200:** Import namespace/types.
- **L202:** Run SQL; return table / rows / scalar. | `o` means: Holds “o” for this scope.  Assigned from single SQL scalar (COUNT/IDENTITY).
- **L203:** Null-safe read from database values.
- **L210:** Null-safe read from database values.

## Source snapshot (raw)

```csharp
using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Web.UI.HtmlControls;

namespace WebAppAssignment.Pages.Landing
{
    public partial class Landing : Page
    {
        private string ConnString
        {
            get
            {
                var cs = ConfigurationManager.ConnectionStrings["MyDbConn"];
                return cs != null ? cs.ConnectionString : string.Empty;
            }
        }

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                BindAuthChrome();
                LoadStats();
                LoadCourses();
            }
        }

        private void BindAuthChrome()
        {
            if (Session["UserID"] != null)
            {
                phGuest.Visible = false;
                phUser.Visible = true;
                litUserName.Text = HttpUtility.HtmlEncode(Session["UserName"] as string ?? "User");

                string role = (Session["UserRole"] as string ?? "").Trim().ToLowerInvariant();
                string dash = ResolveUrl("~/Pages/Landing/Landing.aspx");
                if (role == "0" || role == "admin")
                dash = ResolveUrl("~/Pages/Admin/ADashboard.aspx");
                else if (role == "2" || role == "teacher" || role == "lecturer")
                dash = ResolveUrl("~/Pages/Lecturer/Dashboard.aspx");

                lnkDashboard.HRef = dash;
            }
            else
            {
                phGuest.Visible = true;
                phUser.Visible = false;
            }
        }

        private void LoadStats()
        {
            try
            {
                using (var conn = new SqlConnection(ConnString))
                {
                    conn.Open();

                    litCourseCount.Text = ScalarInt(conn, "SELECT COUNT(*) FROM Courses").ToString("N0");

                    // Distinct enrolled students
                    try
                    {
                        litStudentCount.Text = ScalarInt(conn,
                        "SELECT COUNT(DISTINCT StudentUID) FROM Enrollments").ToString("N0");
                    }
                    catch
                    {
                        litStudentCount.Text = ScalarInt(conn,
                        "SELECT COUNT(*) FROM Users WHERE Role IN ('1','Student','student')").ToString("N0");
                    }

                    try
                    {
                        litLecturerCount.Text = ScalarInt(conn,
                        "SELECT COUNT(DISTINCT LecturerUID) FROM Courses").ToString("N0");
                    }
                    catch
                    {
                        litLecturerCount.Text = "0";
                    }
                }
            }
            catch
            {
                litCourseCount.Text = "0";
                litStudentCount.Text = "0";
                litLecturerCount.Text = "0";
            }
        }

        private void LoadCourses()
        {
            phCourses.Controls.Clear();
            try
            {
                try { WebAppAssignment.Data.CourseSchema.Ensure(); } catch { }

                using (var conn = new SqlConnection(ConnString))
                {
                    conn.Open();
                    string sql = @"
SELECT TOP 12 CID, Name, Description, Rating, BgImg, Categories, Level
FROM Courses
WHERE ISNULL(IsPublished, 1) = 1
ORDER BY CID DESC";
                    SqlDataReader r = null;
                    SqlCommand cmd = new SqlCommand(sql, conn);
                    try
                    {
                        r = cmd.ExecuteReader();
                    }
                    catch
                    {
                        cmd.Dispose();
                        cmd = new SqlCommand(@"
SELECT TOP 12 CID, Name, Description, Rating, BgImg, Categories, Level
FROM Courses
ORDER BY CID DESC", conn);
                        r = cmd.ExecuteReader();
                    }

                    using (cmd)
                    using (r)
                    {
                        var grid = new StringBuilder();
                        grid.Append("<div class='course-carousel' id='courseCarousel'>");
                        grid.Append("<button type='button' class='cc-arrow cc-prev' aria-label='Previous courses'><i class='fa-solid fa-chevron-left'></i></button>");
                        grid.Append("<div class='cc-viewport'>");
                        grid.Append("<div class='cc-track' id='courseTrack'>");
                        int count = 0;
                        while (r.Read())
                        {
                            count++;
                            string name = Safe(r["Name"]);
                            string desc = Safe(r["Description"]);
                            string bg = Safe(r["BgImg"]);
                            string cat = Safe(r["Categories"]);
                            string level = Safe(r["Level"]);
                            decimal rating = r["Rating"] == DBNull.Value ? 0 : Convert.ToDecimal(r["Rating"]);

                            string img = string.IsNullOrWhiteSpace(bg)
                                ? "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600"
                                : bg;

                            grid.Append("<article class='course-card'>");
                            grid.AppendFormat(
                                "<img class='thumb' src='{0}' alt='{1}' onerror=\"this.src='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600'\" />",
                                HttpUtility.HtmlAttributeEncode(img), HttpUtility.HtmlAttributeEncode(name));
                            grid.Append("<div class='body'>");
                            grid.Append("<div class='meta'>");
                            if (!string.IsNullOrEmpty(cat))
                                grid.AppendFormat("<span class='pill'>{0}</span>", HttpUtility.HtmlEncode(cat));
                            if (!string.IsNullOrEmpty(level))
                                grid.AppendFormat("<span class='pill level'>{0}</span>", HttpUtility.HtmlEncode(level));
                            grid.Append("</div>");
                            grid.AppendFormat("<h3>{0}</h3>", HttpUtility.HtmlEncode(name));
                            grid.AppendFormat("<p class='desc'>{0}</p>", HttpUtility.HtmlEncode(
                                string.IsNullOrWhiteSpace(desc) ? "No description provided." : desc));
                            grid.Append("<div class='card-footer-row'>");
                            if (rating > 0)
                                grid.AppendFormat("<span class='rating'><i class='fa-solid fa-star'></i> {0:0.0}</span>", rating);
                            else
                                grid.Append("<span class='text-muted'>New</span>");
                            grid.AppendFormat(
                                "<a class='btn-accent' style='padding:0.35rem 0.85rem;font-size:0.8rem;' href='{0}'>Enroll</a>",
                                ResolveUrl("~/Pages/Authentication/Login.aspx"));
                            grid.Append("</div></div></article>");
                        }
                        grid.Append("</div></div>");
                        grid.Append("<button type='button' class='cc-arrow cc-next' aria-label='Next courses'><i class='fa-solid fa-chevron-right'></i></button>");
                        grid.Append("</div>");

                        if (count == 0)
                        {
                            phEmpty.Visible = true;
                        }
                        else
                        {
                            phEmpty.Visible = false;
                            phCourses.Controls.Add(new LiteralControl(grid.ToString()));
                        }
                    }
                }
            }
            catch
            {
                phEmpty.Visible = true;
            }
        }

        private static int ScalarInt(SqlConnection conn, string sql)
        {
            using (var cmd = new SqlCommand(sql, conn))
            {
                var o = cmd.ExecuteScalar();
                if (o == null || o == DBNull.Value) return 0;
                return Convert.ToInt32(o);
            }
        }

        private static string Safe(object o)
        {
            if (o == null || o == DBNull.Value) return "";
            return o.ToString();
        }
    }
}

```
