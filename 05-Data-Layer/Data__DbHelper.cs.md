# DbHelper.cs
**Source:** `Data/DbHelper.cs`  
<<<<<<< HEAD
**Generated:** 2026-07-11 21:33  
=======
**Generated:** 2026-07-11 21:40  
>>>>>>> eb8ce01 (update)

---

## Feature / role in EduLMS

Primary SQL helper: open connection from Web.config MyDbConn, ExecuteQuery / NonQuery / Scalar, parameter factory P(), SafeString. All business SQL should go through this (or AuthService helpers).

## File overview

- **Total lines:** 112
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 17:** `cs` (`var`) — **Connection string text.**
- **Line 26:** `conn` (`var`) — **SqlConnection — open link to LocalDB/SQL Server.**
- **Line 28:** `conn` (`return`) — **SqlConnection — open link to LocalDB/SQL Server.**
- **Line 40:** `dt` (`var`) — **DataTable — full result set from SQL (many rows/columns).**
- **Line 42:** `dt` (`return`) — **DataTable — full result set from SQL (many rows/columns).**
- **Line 71:** `result` (`var`) — **AuthResult or API result { success, message, … }.**
- **Line 78:** `result` (`var`) — **AuthResult or API result { success, message, … }.**

## Functions / methods (11 found)

### `OpenConnection` — lines 23–29

```csharp
public static SqlConnection OpenConnection()
```

#### Explanation

- **Purpose:** Implements `OpenConnection`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  23 | 
  24 |         public static SqlConnection OpenConnection()
  25 |         {
  26 |             var conn = new SqlConnection(ConnectionString);
  27 |             conn.Open();
  28 |             return conn;
  29 |         }
```

<<<<<<< HEAD
**Line notes**

- **L24:** Database access (pure SQL).
- **L26:** Database access (pure SQL).
=======
**Line notes** (what code + variables mean)

- **L24:** Database access (pure SQL).
- **L26:** Database access (pure SQL). | `conn` means: SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.
>>>>>>> eb8ce01 (update)

---

### `ExecuteQuery` — lines 30–45

```csharp
public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.
- `adapter` (`var`) — SqlDataAdapter — fills a DataTable from a SqlCommand.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  30 | 
  31 |         public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
  32 |         {
  33 |             using (var conn = OpenConnection())
  34 |             using (var cmd = new SqlCommand(sql, conn))
  35 |             {
  36 |                 if (parameters != null && parameters.Length > 0)
  37 |                 cmd.Parameters.AddRange(parameters);
  38 |                 using (var adapter = new SqlDataAdapter(cmd))
  39 |                 {
  40 |                     var dt = new DataTable();
  41 |                     adapter.Fill(dt);
  42 |                     return dt;
  43 |                 }
  44 |             }
  45 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L31:** Run SQL; return table / rows / scalar.
- **L33:** Import namespace/types.
- **L34:** Import namespace/types.
- **L38:** Import namespace/types.
<<<<<<< HEAD
- **L40:** In-memory result set from ADO.NET.
=======
- **L40:** In-memory result set from ADO.NET. | `dt` means: DataTable — full result set from SQL (many rows/columns).  Newly constructed object.
>>>>>>> eb8ce01 (update)

---

### `ExecuteNonQuery` — lines 46–56

```csharp
public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteNonQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  46 | 
  47 |         public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
  48 |         {
  49 |             using (var conn = OpenConnection())
  50 |             using (var cmd = new SqlCommand(sql, conn))
  51 |             {
  52 |                 if (parameters != null && parameters.Length > 0)
  53 |                 cmd.Parameters.AddRange(parameters);
  54 |                 return cmd.ExecuteNonQuery();
  55 |             }
  56 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L47:** Run SQL; return table / rows / scalar.
- **L49:** Import namespace/types.
- **L50:** Import namespace/types.
- **L54:** Run SQL; return table / rows / scalar.

---

### `ExecuteScalar` — lines 57–67

```csharp
public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalar`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `conn` (`var`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  57 | 
  58 |         public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
  59 |         {
  60 |             using (var conn = OpenConnection())
  61 |             using (var cmd = new SqlCommand(sql, conn))
  62 |             {
  63 |                 if (parameters != null && parameters.Length > 0)
  64 |                 cmd.Parameters.AddRange(parameters);
  65 |                 return cmd.ExecuteScalar();
  66 |             }
  67 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L58:** Run SQL; return table / rows / scalar.
- **L60:** Import namespace/types.
- **L61:** Import namespace/types.
- **L65:** Run SQL; return table / rows / scalar.

---

### `ExecuteScalarInt` — lines 68–74

```csharp
public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalarInt`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `result` (`var`) — AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY).

#### Line-by-line (this function)

```csharp
  68 | 
  69 |         public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
  70 |         {
  71 |             var result = ExecuteScalar(sql, parameters);
  72 |             if (result == null || result == DBNull.Value) return 0;
  73 |             return Convert.ToInt32(result);
  74 |         }
```

<<<<<<< HEAD
**Line notes**

- **L69:** Run SQL; return table / rows / scalar.
- **L71:** Run SQL; return table / rows / scalar.
=======
**Line notes** (what code + variables mean)

- **L69:** Run SQL; return table / rows / scalar.
- **L71:** Run SQL; return table / rows / scalar. | `result` means: AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY).
>>>>>>> eb8ce01 (update)
- **L72:** Null-safe read from database values.

---

### `ExecuteScalarDecimal` — lines 75–81

```csharp
public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalarDecimal`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `sql` (`string`) — SQL query text (should use parameters, not raw user input).
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `result` (`var`) — AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY).

#### Line-by-line (this function)

```csharp
  75 | 
  76 |         public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
  77 |         {
  78 |             var result = ExecuteScalar(sql, parameters);
  79 |             if (result == null || result == DBNull.Value) return 0m;
  80 |             return Convert.ToDecimal(result);
  81 |         }
```

<<<<<<< HEAD
**Line notes**

- **L76:** Run SQL; return table / rows / scalar.
- **L78:** Run SQL; return table / rows / scalar.
=======
**Line notes** (what code + variables mean)

- **L76:** Run SQL; return table / rows / scalar.
- **L78:** Run SQL; return table / rows / scalar. | `result` means: AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY).
>>>>>>> eb8ce01 (update)
- **L79:** Null-safe read from database values.

---

### `P` — lines 82–86

```csharp
public static SqlParameter P(string name, object value)
```

#### Explanation

- **Purpose:** Implements `P`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `name` (`string`) — Display name of user/course/criterion.
- `value` (`object`) — Holds “value” for this scope.

#### Line-by-line (this function)

```csharp
  82 | 
  83 |         public static SqlParameter P(string name, object value)
  84 |         {
  85 |             return new SqlParameter(name, value ?? DBNull.Value);
  86 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L83:** Parameterized SQL — prevents classic SQL injection.
- **L85:** Parameterized SQL — prevents classic SQL injection.

---

### `SafeString` — lines 87–92

```csharp
public static string SafeString(object value)
```

#### Explanation

- **Purpose:** Implements `SafeString`.
- **Parameters (what each means):**
- `value` (`object`) — Holds “value” for this scope.

#### Line-by-line (this function)

```csharp
  87 | 
  88 |         public static string SafeString(object value)
  89 |         {
  90 |             if (value == null || value == DBNull.Value) return string.Empty;
  91 |             return value.ToString();
  92 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L88:** Null-safe read from database values.
- **L90:** Null-safe read from database values.

---

### `SafeInt` — lines 93–98

```csharp
public static int? SafeInt(object value)
```

#### Explanation

- **Purpose:** Implements `SafeInt`.
- **Parameters (what each means):**
- `value` (`object`) — Holds “value” for this scope.

#### Line-by-line (this function)

```csharp
  93 | 
  94 |         public static int? SafeInt(object value)
  95 |         {
  96 |             if (value == null || value == DBNull.Value) return null;
  97 |             return Convert.ToInt32(value);
  98 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L96:** Null-safe read from database values.

---

### `SafeDecimal` — lines 99–104

```csharp
public static decimal? SafeDecimal(object value)
```

#### Explanation

- **Purpose:** Implements `SafeDecimal`.
- **Parameters (what each means):**
- `value` (`object`) — Holds “value” for this scope.

#### Line-by-line (this function)

```csharp
  99 | 
 100 |         public static decimal? SafeDecimal(object value)
 101 |         {
 102 |             if (value == null || value == DBNull.Value) return null;
 103 |             return Convert.ToDecimal(value);
 104 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L102:** Null-safe read from database values.

---

### `SafeDate` — lines 105–110

```csharp
public static DateTime? SafeDate(object value)
```

#### Explanation

- **Purpose:** Implements `SafeDate`.
- **Parameters (what each means):**
- `value` (`object`) — Holds “value” for this scope.

#### Line-by-line (this function)

```csharp
 105 | 
 106 |         public static DateTime? SafeDate(object value)
 107 |         {
 108 |             if (value == null || value == DBNull.Value) return null;
 109 |             return Convert.ToDateTime(value);
 110 |         }
```

<<<<<<< HEAD
**Line notes**
=======
**Line notes** (what code + variables mean)
>>>>>>> eb8ce01 (update)

- **L108:** Null-safe read from database values.

---

## Full file listing with line notes

<<<<<<< HEAD
Source is shown as a single fenced code block with line numbers. Recognized patterns are listed under **Line notes** after the block.
=======
Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.
>>>>>>> eb8ce01 (update)

```csharp
   1 | using System;
   2 | using System.Configuration;
   3 | using System.Data;
   4 | using System.Data.SqlClient;
   5 | 
   6 | namespace WebAppAssignment.Data
   7 | {
   8 |     /// <summary>
   9 |     /// Centralized SQL helper bound to EduDB.mdf via Web.config MyDbConn.
  10 |     /// </summary>
  11 |     public static class DbHelper
  12 |     {
  13 |         public static string ConnectionString
  14 |         {
  15 |             get
  16 |             {
  17 |                 var cs = ConfigurationManager.ConnectionStrings["MyDbConn"];
  18 |                 if (cs == null || string.IsNullOrWhiteSpace(cs.ConnectionString))
  19 |                 throw new InvalidOperationException("Connection string 'MyDbConn' is missing from Web.config.");
  20 |                 return cs.ConnectionString;
  21 |             }
  22 |         }
  23 | 
  24 |         public static SqlConnection OpenConnection()
  25 |         {
  26 |             var conn = new SqlConnection(ConnectionString);
  27 |             conn.Open();
  28 |             return conn;
  29 |         }
  30 | 
  31 |         public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
  32 |         {
  33 |             using (var conn = OpenConnection())
  34 |             using (var cmd = new SqlCommand(sql, conn))
  35 |             {
  36 |                 if (parameters != null && parameters.Length > 0)
  37 |                 cmd.Parameters.AddRange(parameters);
  38 |                 using (var adapter = new SqlDataAdapter(cmd))
  39 |                 {
  40 |                     var dt = new DataTable();
  41 |                     adapter.Fill(dt);
  42 |                     return dt;
  43 |                 }
  44 |             }
  45 |         }
  46 | 
  47 |         public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
  48 |         {
  49 |             using (var conn = OpenConnection())
  50 |             using (var cmd = new SqlCommand(sql, conn))
  51 |             {
  52 |                 if (parameters != null && parameters.Length > 0)
  53 |                 cmd.Parameters.AddRange(parameters);
  54 |                 return cmd.ExecuteNonQuery();
  55 |             }
  56 |         }
  57 | 
  58 |         public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
  59 |         {
  60 |             using (var conn = OpenConnection())
  61 |             using (var cmd = new SqlCommand(sql, conn))
  62 |             {
  63 |                 if (parameters != null && parameters.Length > 0)
  64 |                 cmd.Parameters.AddRange(parameters);
  65 |                 return cmd.ExecuteScalar();
  66 |             }
  67 |         }
  68 | 
  69 |         public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
  70 |         {
  71 |             var result = ExecuteScalar(sql, parameters);
  72 |             if (result == null || result == DBNull.Value) return 0;
  73 |             return Convert.ToInt32(result);
  74 |         }
  75 | 
  76 |         public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
  77 |         {
  78 |             var result = ExecuteScalar(sql, parameters);
  79 |             if (result == null || result == DBNull.Value) return 0m;
  80 |             return Convert.ToDecimal(result);
  81 |         }
  82 | 
  83 |         public static SqlParameter P(string name, object value)
  84 |         {
  85 |             return new SqlParameter(name, value ?? DBNull.Value);
  86 |         }
  87 | 
  88 |         public static string SafeString(object value)
  89 |         {
  90 |             if (value == null || value == DBNull.Value) return string.Empty;
  91 |             return value.ToString();
  92 |         }
  93 | 
  94 |         public static int? SafeInt(object value)
  95 |         {
  96 |             if (value == null || value == DBNull.Value) return null;
  97 |             return Convert.ToInt32(value);
  98 |         }
  99 | 
 100 |         public static decimal? SafeDecimal(object value)
 101 |         {
 102 |             if (value == null || value == DBNull.Value) return null;
 103 |             return Convert.ToDecimal(value);
 104 |         }
 105 | 
 106 |         public static DateTime? SafeDate(object value)
 107 |         {
 108 |             if (value == null || value == DBNull.Value) return null;
 109 |             return Convert.ToDateTime(value);
 110 |         }
 111 |     }
 112 | }
```

**Line notes**

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L6:** C# namespace grouping.
- **L11:** Database access (pure SQL).
<<<<<<< HEAD
- **L24:** Database access (pure SQL).
- **L26:** Database access (pure SQL).
=======
- **L17:** `cs` means: Connection string text.  Read from Web.config.
- **L24:** Database access (pure SQL).
- **L26:** Database access (pure SQL). | `conn` means: SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L31:** Run SQL; return table / rows / scalar.
- **L33:** Import namespace/types.
- **L34:** Import namespace/types.
- **L38:** Import namespace/types.
<<<<<<< HEAD
- **L40:** In-memory result set from ADO.NET.
=======
- **L40:** In-memory result set from ADO.NET. | `dt` means: DataTable — full result set from SQL (many rows/columns).  Newly constructed object.
>>>>>>> eb8ce01 (update)
- **L47:** Run SQL; return table / rows / scalar.
- **L49:** Import namespace/types.
- **L50:** Import namespace/types.
- **L54:** Run SQL; return table / rows / scalar.
- **L58:** Run SQL; return table / rows / scalar.
- **L60:** Import namespace/types.
- **L61:** Import namespace/types.
- **L65:** Run SQL; return table / rows / scalar.
- **L69:** Run SQL; return table / rows / scalar.
<<<<<<< HEAD
- **L71:** Run SQL; return table / rows / scalar.
- **L72:** Null-safe read from database values.
- **L76:** Run SQL; return table / rows / scalar.
- **L78:** Run SQL; return table / rows / scalar.
=======
- **L71:** Run SQL; return table / rows / scalar. | `result` means: AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY).
- **L72:** Null-safe read from database values.
- **L76:** Run SQL; return table / rows / scalar.
- **L78:** Run SQL; return table / rows / scalar. | `result` means: AuthResult or API result { success, message, … }.  Assigned from single SQL scalar (COUNT/IDENTITY).
>>>>>>> eb8ce01 (update)
- **L79:** Null-safe read from database values.
- **L83:** Parameterized SQL — prevents classic SQL injection.
- **L85:** Parameterized SQL — prevents classic SQL injection.
- **L88:** Null-safe read from database values.
- **L90:** Null-safe read from database values.
- **L96:** Null-safe read from database values.
- **L102:** Null-safe read from database values.
- **L108:** Null-safe read from database values.

## Source snapshot (raw)

```csharp
using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;

namespace WebAppAssignment.Data
{
    /// <summary>
    /// Centralized SQL helper bound to EduDB.mdf via Web.config MyDbConn.
    /// </summary>
    public static class DbHelper
    {
        public static string ConnectionString
        {
            get
            {
                var cs = ConfigurationManager.ConnectionStrings["MyDbConn"];
                if (cs == null || string.IsNullOrWhiteSpace(cs.ConnectionString))
                throw new InvalidOperationException("Connection string 'MyDbConn' is missing from Web.config.");
                return cs.ConnectionString;
            }
        }

        public static SqlConnection OpenConnection()
        {
            var conn = new SqlConnection(ConnectionString);
            conn.Open();
            return conn;
        }

        public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
        {
            using (var conn = OpenConnection())
            using (var cmd = new SqlCommand(sql, conn))
            {
                if (parameters != null && parameters.Length > 0)
                cmd.Parameters.AddRange(parameters);
                using (var adapter = new SqlDataAdapter(cmd))
                {
                    var dt = new DataTable();
                    adapter.Fill(dt);
                    return dt;
                }
            }
        }

        public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
        {
            using (var conn = OpenConnection())
            using (var cmd = new SqlCommand(sql, conn))
            {
                if (parameters != null && parameters.Length > 0)
                cmd.Parameters.AddRange(parameters);
                return cmd.ExecuteNonQuery();
            }
        }

        public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
        {
            using (var conn = OpenConnection())
            using (var cmd = new SqlCommand(sql, conn))
            {
                if (parameters != null && parameters.Length > 0)
                cmd.Parameters.AddRange(parameters);
                return cmd.ExecuteScalar();
            }
        }

        public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
        {
            var result = ExecuteScalar(sql, parameters);
            if (result == null || result == DBNull.Value) return 0;
            return Convert.ToInt32(result);
        }

        public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
        {
            var result = ExecuteScalar(sql, parameters);
            if (result == null || result == DBNull.Value) return 0m;
            return Convert.ToDecimal(result);
        }

        public static SqlParameter P(string name, object value)
        {
            return new SqlParameter(name, value ?? DBNull.Value);
        }

        public static string SafeString(object value)
        {
            if (value == null || value == DBNull.Value) return string.Empty;
            return value.ToString();
        }

        public static int? SafeInt(object value)
        {
            if (value == null || value == DBNull.Value) return null;
            return Convert.ToInt32(value);
        }

        public static decimal? SafeDecimal(object value)
        {
            if (value == null || value == DBNull.Value) return null;
            return Convert.ToDecimal(value);
        }

        public static DateTime? SafeDate(object value)
        {
            if (value == null || value == DBNull.Value) return null;
            return Convert.ToDateTime(value);
        }
    }
}

```
