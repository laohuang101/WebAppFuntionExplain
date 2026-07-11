# DatabaseHelper.cs
**Source:** `Data/DatabaseHelper.cs`  
**Generated:** 2026-07-11 21:47  

---

## Feature / role in EduLMS

Legacy/alternate connection helper (same MyDbConn). Prefer DbHelper for new code; kept for older call sites.

## File overview

- **Total lines:** 64
- **Kind:** `.cs`

## Variables / fields (file level)

Each name is explained in plain English (what it stores / why it exists).

- **Line 10:** `ConnString` (`string`) — **Holds “Conn String” for this scope. (text)**
- **Line 24:** `dt` (`DataTable`) — **DataTable — full result set from SQL (many rows/columns).**
- **Line 26:** `dt` (`return`) — **DataTable — full result set from SQL (many rows/columns).**

## Functions / methods (3 found)

### `ExecuteQuery` — lines 11–30

```csharp
public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
```

#### Explanation

- **Purpose:** Implements `ExecuteQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `query` (`string`) — Holds “query” for this scope. (text)
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.
- `dt` (`DataTable`) — DataTable — full result set from SQL (many rows/columns).  Newly constructed object.

#### Line-by-line (this function)

```csharp
  11 | 
  12 |         public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
  13 |         {
  14 |             using (SqlConnection conn = new SqlConnection(ConnString))
  15 |             {
  16 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  17 |                 {
  18 |                     if (parameters != null)
  19 |                     {
  20 |                         cmd.Parameters.AddRange(parameters);
  21 |                     }
  22 |                     using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
  23 |                     {
  24 |                         DataTable dt = new DataTable();
  25 |                         adapter.Fill(dt);
  26 |                         return dt;
  27 |                     }
  28 |                 }
  29 |             }
  30 |         }
```

**Line notes** (what code + variables mean)

- **L12:** Run SQL; return table / rows / scalar.
- **L14:** Import namespace/types.
- **L16:** Import namespace/types.
- **L22:** Import namespace/types.
- **L24:** In-memory result set from ADO.NET. | `dt` means: DataTable — full result set from SQL (many rows/columns).  Newly constructed object.

---

### `ExecuteNonQuery` — lines 31–46

```csharp
public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
```

#### Explanation

- **Purpose:** Implements `ExecuteNonQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `query` (`string`) — Holds “query” for this scope. (text)
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  31 | 
  32 |         public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
  33 |         {
  34 |             using (SqlConnection conn = new SqlConnection(ConnString))
  35 |             {
  36 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  37 |                 {
  38 |                     if (parameters != null)
  39 |                     {
  40 |                         cmd.Parameters.AddRange(parameters);
  41 |                     }
  42 |                     conn.Open();
  43 |                     return cmd.ExecuteNonQuery();
  44 |                 }
  45 |             }
  46 |         }
```

**Line notes** (what code + variables mean)

- **L32:** Run SQL; return table / rows / scalar.
- **L34:** Import namespace/types.
- **L36:** Import namespace/types.
- **L43:** Run SQL; return table / rows / scalar.

---

### `ExecuteScalar` — lines 47–62

```csharp
public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalar`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters (what each means):**
- `query` (`string`) — Holds “query” for this scope. (text)
- `parameters` (`SqlParameter[]`) — Array of SQL parameters (@Name values) for a query.
- **Local variables (what each means):**
- `conn` (`SqlConnection`) — SqlConnection — open link to LocalDB/SQL Server.  Newly constructed object.

#### Line-by-line (this function)

```csharp
  47 | 
  48 |         public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
  49 |         {
  50 |             using (SqlConnection conn = new SqlConnection(ConnString))
  51 |             {
  52 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  53 |                 {
  54 |                     if (parameters != null)
  55 |                     {
  56 |                         cmd.Parameters.AddRange(parameters);
  57 |                     }
  58 |                     conn.Open();
  59 |                     return cmd.ExecuteScalar();
  60 |                 }
  61 |             }
  62 |         }
```

**Line notes** (what code + variables mean)

- **L48:** Run SQL; return table / rows / scalar.
- **L50:** Import namespace/types.
- **L52:** Import namespace/types.
- **L59:** Run SQL; return table / rows / scalar.

---

## Full file listing with line notes

Source is shown as a single fenced code block with line numbers. Recognized patterns and **variable meanings** are listed under **Line notes**.

```csharp
   1 | using System;
   2 | using System.Configuration;
   3 | using System.Data;
   4 | using System.Data.SqlClient;
   5 | 
   6 | namespace WebAppAssignment.Data
   7 | {
   8 |     public static class DatabaseHelper
   9 |     {
  10 |         private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"].ConnectionString;
  11 | 
  12 |         public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
  13 |         {
  14 |             using (SqlConnection conn = new SqlConnection(ConnString))
  15 |             {
  16 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  17 |                 {
  18 |                     if (parameters != null)
  19 |                     {
  20 |                         cmd.Parameters.AddRange(parameters);
  21 |                     }
  22 |                     using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
  23 |                     {
  24 |                         DataTable dt = new DataTable();
  25 |                         adapter.Fill(dt);
  26 |                         return dt;
  27 |                     }
  28 |                 }
  29 |             }
  30 |         }
  31 | 
  32 |         public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
  33 |         {
  34 |             using (SqlConnection conn = new SqlConnection(ConnString))
  35 |             {
  36 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  37 |                 {
  38 |                     if (parameters != null)
  39 |                     {
  40 |                         cmd.Parameters.AddRange(parameters);
  41 |                     }
  42 |                     conn.Open();
  43 |                     return cmd.ExecuteNonQuery();
  44 |                 }
  45 |             }
  46 |         }
  47 | 
  48 |         public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
  49 |         {
  50 |             using (SqlConnection conn = new SqlConnection(ConnString))
  51 |             {
  52 |                 using (SqlCommand cmd = new SqlCommand(query, conn))
  53 |                 {
  54 |                     if (parameters != null)
  55 |                     {
  56 |                         cmd.Parameters.AddRange(parameters);
  57 |                     }
  58 |                     conn.Open();
  59 |                     return cmd.ExecuteScalar();
  60 |                 }
  61 |             }
  62 |         }
  63 |     }
  64 | }
```

**Line notes** (what code + variables mean)

- **L1:** Import namespace/types.
- **L2:** Import namespace/types.
- **L3:** Import namespace/types.
- **L4:** Import namespace/types.
- **L6:** C# namespace grouping.
- **L12:** Run SQL; return table / rows / scalar.
- **L14:** Import namespace/types.
- **L16:** Import namespace/types.
- **L22:** Import namespace/types.
- **L24:** In-memory result set from ADO.NET. | `dt` means: DataTable — full result set from SQL (many rows/columns).  Newly constructed object.
- **L32:** Run SQL; return table / rows / scalar.
- **L34:** Import namespace/types.
- **L36:** Import namespace/types.
- **L43:** Run SQL; return table / rows / scalar.
- **L48:** Run SQL; return table / rows / scalar.
- **L50:** Import namespace/types.
- **L52:** Import namespace/types.
- **L59:** Run SQL; return table / rows / scalar.

## Source snapshot (raw)

```csharp
using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;

namespace WebAppAssignment.Data
{
    public static class DatabaseHelper
    {
        private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"].ConnectionString;

        public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
        {
            using (SqlConnection conn = new SqlConnection(ConnString))
            {
                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    if (parameters != null)
                    {
                        cmd.Parameters.AddRange(parameters);
                    }
                    using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))
                    {
                        DataTable dt = new DataTable();
                        adapter.Fill(dt);
                        return dt;
                    }
                }
            }
        }

        public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
        {
            using (SqlConnection conn = new SqlConnection(ConnString))
            {
                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    if (parameters != null)
                    {
                        cmd.Parameters.AddRange(parameters);
                    }
                    conn.Open();
                    return cmd.ExecuteNonQuery();
                }
            }
        }

        public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
        {
            using (SqlConnection conn = new SqlConnection(ConnString))
            {
                using (SqlCommand cmd = new SqlCommand(query, conn))
                {
                    if (parameters != null)
                    {
                        cmd.Parameters.AddRange(parameters);
                    }
                    conn.Open();
                    return cmd.ExecuteScalar();
                }
            }
        }
    }
}

```
