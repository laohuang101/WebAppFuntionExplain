# DatabaseHelper.cs
**Source:** `Data/DatabaseHelper.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Part of EduLMS Landing or Lecturer area. See function sections below.

## File overview

- **Total lines:** 64
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 10:** `ConnString` — type `string`
- **Line 24:** `dt` — type `DataTable`
- **Line 26:** `dt` — type `return`

## Functions / methods (3 found)

### `ExecuteQuery` — lines 11–30

```
public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)
```

#### Explanation

- **Purpose:** Implements `ExecuteQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string query, SqlParameter[] parameters = null`
- **Local variables:** `dt`

#### Line-by-line (this function)

`  11`  ``
`  12`  `        public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)`
  - → Run SQL; return table / rows / scalar.
`  13`  `        {`
`  14`  `            using (SqlConnection conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  15`  `            {`
`  16`  `                using (SqlCommand cmd = new SqlCommand(query, conn))`
  - → Import namespace/types.
`  17`  `                {`
`  18`  `                    if (parameters != null)`
`  19`  `                    {`
`  20`  `                        cmd.Parameters.AddRange(parameters);`
`  21`  `                    }`
`  22`  `                    using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))`
  - → Import namespace/types.
`  23`  `                    {`
`  24`  `                        DataTable dt = new DataTable();`
`  25`  `                        adapter.Fill(dt);`
`  26`  `                        return dt;`
`  27`  `                    }`
`  28`  `                }`
`  29`  `            }`
`  30`  `        }`

---

### `ExecuteNonQuery` — lines 31–46

```
public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)
```

#### Explanation

- **Purpose:** Implements `ExecuteNonQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string query, SqlParameter[] parameters = null`

#### Line-by-line (this function)

`  31`  ``
`  32`  `        public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)`
  - → Run SQL; return table / rows / scalar.
`  33`  `        {`
`  34`  `            using (SqlConnection conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  35`  `            {`
`  36`  `                using (SqlCommand cmd = new SqlCommand(query, conn))`
  - → Import namespace/types.
`  37`  `                {`
`  38`  `                    if (parameters != null)`
`  39`  `                    {`
`  40`  `                        cmd.Parameters.AddRange(parameters);`
`  41`  `                    }`
`  42`  `                    conn.Open();`
`  43`  `                    return cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  44`  `                }`
`  45`  `            }`
`  46`  `        }`

---

### `ExecuteScalar` — lines 47–62

```
public static object ExecuteScalar(string query, SqlParameter[] parameters = null)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalar`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string query, SqlParameter[] parameters = null`

#### Line-by-line (this function)

`  47`  ``
`  48`  `        public static object ExecuteScalar(string query, SqlParameter[] parameters = null)`
  - → Run SQL; return table / rows / scalar.
`  49`  `        {`
`  50`  `            using (SqlConnection conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  51`  `            {`
`  52`  `                using (SqlCommand cmd = new SqlCommand(query, conn))`
  - → Import namespace/types.
`  53`  `                {`
`  54`  `                    if (parameters != null)`
`  55`  `                    {`
`  56`  `                        cmd.Parameters.AddRange(parameters);`
`  57`  `                    }`
`  58`  `                    conn.Open();`
`  59`  `                    return cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`  60`  `                }`
`  61`  `            }`
`  62`  `        }`

---

## Full file listing with line notes

Every line of the source is listed (truncated only if extremely long). Notes appear under lines the analyzer recognizes.

`   1`  `using System;`
  - → Import namespace/types.
`   2`  `using System.Configuration;`
  - → Import namespace/types.
`   3`  `using System.Data;`
  - → Import namespace/types.
`   4`  `using System.Data.SqlClient;`
  - → Import namespace/types.
`   5`  ``
`   6`  `namespace WebAppAssignment.Data`
  - → C# namespace grouping.
`   7`  `{`
`   8`  `    public static class DatabaseHelper`
`   9`  `    {`
`  10`  `        private static readonly string ConnString = ConfigurationManager.ConnectionStrings["MyDbConn"].ConnectionString;`
`  11`  ``
`  12`  `        public static DataTable ExecuteQuery(string query, SqlParameter[] parameters = null)`
  - → Run SQL; return table / rows / scalar.
`  13`  `        {`
`  14`  `            using (SqlConnection conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  15`  `            {`
`  16`  `                using (SqlCommand cmd = new SqlCommand(query, conn))`
  - → Import namespace/types.
`  17`  `                {`
`  18`  `                    if (parameters != null)`
`  19`  `                    {`
`  20`  `                        cmd.Parameters.AddRange(parameters);`
`  21`  `                    }`
`  22`  `                    using (SqlDataAdapter adapter = new SqlDataAdapter(cmd))`
  - → Import namespace/types.
`  23`  `                    {`
`  24`  `                        DataTable dt = new DataTable();`
`  25`  `                        adapter.Fill(dt);`
`  26`  `                        return dt;`
`  27`  `                    }`
`  28`  `                }`
`  29`  `            }`
`  30`  `        }`
`  31`  ``
`  32`  `        public static int ExecuteNonQuery(string query, SqlParameter[] parameters = null)`
  - → Run SQL; return table / rows / scalar.
`  33`  `        {`
`  34`  `            using (SqlConnection conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  35`  `            {`
`  36`  `                using (SqlCommand cmd = new SqlCommand(query, conn))`
  - → Import namespace/types.
`  37`  `                {`
`  38`  `                    if (parameters != null)`
`  39`  `                    {`
`  40`  `                        cmd.Parameters.AddRange(parameters);`
`  41`  `                    }`
`  42`  `                    conn.Open();`
`  43`  `                    return cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  44`  `                }`
`  45`  `            }`
`  46`  `        }`
`  47`  ``
`  48`  `        public static object ExecuteScalar(string query, SqlParameter[] parameters = null)`
  - → Run SQL; return table / rows / scalar.
`  49`  `        {`
`  50`  `            using (SqlConnection conn = new SqlConnection(ConnString))`
  - → Import namespace/types.
`  51`  `            {`
`  52`  `                using (SqlCommand cmd = new SqlCommand(query, conn))`
  - → Import namespace/types.
`  53`  `                {`
`  54`  `                    if (parameters != null)`
`  55`  `                    {`
`  56`  `                        cmd.Parameters.AddRange(parameters);`
`  57`  `                    }`
`  58`  `                    conn.Open();`
`  59`  `                    return cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`  60`  `                }`
`  61`  `            }`
`  62`  `        }`
`  63`  `    }`
`  64`  `}`

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
