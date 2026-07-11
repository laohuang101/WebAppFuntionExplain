# Landing.aspx.cs
**Source:** `Pages/Landing/Landing.aspx.cs`  
**Generated:** 2026-07-11 21:56  

---

## Feature / role in EduLMS

Public marketing + course catalog. Shows published courses only (`IsPublished`). Guests can browse; Enroll sends unauthenticated users to Login.

## File overview

- **Total lines:** 214
- **Kind:** `.cs`

## Variables / fields (file level)

Simple table of names declared at file/class level.

_No file-level fields found. See each function’s **Variables** table for locals._

## Functions / methods (6 found)

### `Page_Load` — lines 22–31

#### Signature

```csharp
protected void Page_Load(object sender, EventArgs e)
```

#### What it is

Runs automatically when the ASP.NET page opens or posts back; sets up the page and security checks.

#### How it works

1. ASP.NET calls this automatically on every request.
2. On first load (`!IsPostBack`), initialize UI or redirect if already logged in.
3. On postback, button handlers run separately after this method.

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `sender` | `object` | The control that raised the event (the button that was clicked). |
| `e` | `EventArgs` | Event data from the button/control click (ASP.NET EventArgs). |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

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

---

### `BindAuthChrome` — lines 32–55

#### Signature

```csharp
private void BindAuthChrome()
```

#### What it is

Function `BindAuthChrome` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Save temporary state in Session (`Session["UserID"] !`).
2. Save temporary state in Session (`Session["UserName"] as string ?? "User");`).
3. Save temporary state in Session (`Session["UserRole"] as string ?? "").Trim().ToLowerInvariant();`).
4. If the user is Admin, complete login without MFA; otherwise require MFA.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `role` | `string` | User role code or name (Admin/Student/Lecturer).  Read from ASP.NET Session. |
| `dash` | `string` | Holds “dash” for this scope. (text) |

#### Code

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

---

### `LoadStats` — lines 56–96

#### Signature

```csharp
private void LoadStats()
```

#### What it is

Reads/loads data related to **Stats** and returns it for display or further use.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |

#### Code

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

---

### `LoadCourses` — lines 97–196

#### Signature

```csharp
private void LoadCourses()
```

#### What it is

Browser JS: load the lecturer’s courses into a dropdown.

#### How it works

1. Open a connection to the LocalDB / SQL Server database.

#### Parameters

_No parameters._

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `var` | SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object. |
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |
| `cmd` | `SqlCommand` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |
| `grid` | `var` | Identifier (`grid`) — database primary/foreign key.  Newly constructed object. |
| `count` | `int` | Number of matching records.  Literal number `0`. |
| `name` | `string` | Display name of user/course/criterion. |
| `desc` | `string` | Description text (may embed <<<META>>> JSON). |
| `bg` | `string` | Holds “bg” for this scope. (text) |
| `cat` | `string` | Date/time value. (text) |
| `level` | `string` | Holds “level” for this scope. (text) |
| `rating` | `decimal` | Holds “rating” for this scope. (number/score) |
| `img` | `string` | Image element or image path. |

#### Code

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

---

### `ScalarInt` — lines 197–206

#### Signature

```csharp
private static int ScalarInt(SqlConnection conn, string sql)
```

#### What it is

Function `ScalarInt` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Run SQL that returns one value (count, id, flag).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `conn` | `SqlConnection` | SqlConnection — open link to LocalDB/SQL Server. |
| `sql` | `string` | SQL query text (should use parameters, not raw user input). |

#### Variables (inside this function)

| Variable | Type | What it is |
|----------|------|------------|
| `cmd` | `var` | SqlCommand — the SQL statement + parameters object.  Newly constructed object. |

#### Code

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

---

### `Safe` — lines 207–212

#### Signature

```csharp
private static string Safe(object o)
```

#### What it is

Function `Safe` — supports this feature by running the logic in its body (see **How it works**).

#### How it works

1. Starts when something calls `Safe`.
2. Uses the parameters and local variables listed below.
3. Runs the statements in the code block (checks, database/UI work, then return).

#### Parameters

| Variable | Type | What it is |
|----------|------|------------|
| `o` | `object` | Holds “o” for this scope. |

#### Variables (inside this function)

_No local variables detected (or only uses parameters)._

#### Code

```csharp
 207 | 
 208 |         private static string Safe(object o)
 209 |         {
 210 |             if (o == null || o == DBNull.Value) return "";
 211 |             return o.ToString();
 212 |         }
```

---

## Full file code

Complete source with line numbers (for reading along with the function sections above).

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
