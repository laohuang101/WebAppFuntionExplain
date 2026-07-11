# DbHelper.cs
**Source:** `Data/DbHelper.cs`  
**Generated:** 2026-07-11 21:21  

---

## Feature / role in EduLMS

Shared SqlConnection helpers — parameterized queries only.

## File overview

- **Total lines:** 112
- **Kind:** `.cs`

## Variables / fields (file level)

- **Line 17:** `cs` — type `var`
- **Line 26:** `conn` — type `var`
- **Line 28:** `conn` — type `return`
- **Line 40:** `dt` — type `var`
- **Line 42:** `dt` — type `return`
- **Line 71:** `result` — type `var`
- **Line 78:** `result` — type `var`

## Functions / methods (11 found)

### `OpenConnection` — lines 23–29

```
public static SqlConnection OpenConnection()
```

#### Explanation

- **Purpose:** Implements `OpenConnection`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Local variables:** `conn`

#### Line-by-line (this function)

`  23`  ``
`  24`  `        public static SqlConnection OpenConnection()`
  - → Database access (pure SQL).
`  25`  `        {`
`  26`  `            var conn = new SqlConnection(ConnectionString);`
  - → Database access (pure SQL).
`  27`  `            conn.Open();`
`  28`  `            return conn;`
`  29`  `        }`

---

### `ExecuteQuery` — lines 30–45

```
public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string sql, params SqlParameter[] parameters`
- **Local variables:** `conn`, `cmd`, `adapter`, `dt`

#### Line-by-line (this function)

`  30`  ``
`  31`  `        public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  32`  `        {`
`  33`  `            using (var conn = OpenConnection())`
  - → Import namespace/types.
`  34`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`  35`  `            {`
`  36`  `                if (parameters != null && parameters.Length > 0)`
`  37`  `                cmd.Parameters.AddRange(parameters);`
`  38`  `                using (var adapter = new SqlDataAdapter(cmd))`
  - → Import namespace/types.
`  39`  `                {`
`  40`  `                    var dt = new DataTable();`
`  41`  `                    adapter.Fill(dt);`
`  42`  `                    return dt;`
`  43`  `                }`
`  44`  `            }`
`  45`  `        }`

---

### `ExecuteNonQuery` — lines 46–56

```
public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteNonQuery`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string sql, params SqlParameter[] parameters`
- **Local variables:** `conn`, `cmd`

#### Line-by-line (this function)

`  46`  ``
`  47`  `        public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  48`  `        {`
`  49`  `            using (var conn = OpenConnection())`
  - → Import namespace/types.
`  50`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`  51`  `            {`
`  52`  `                if (parameters != null && parameters.Length > 0)`
`  53`  `                cmd.Parameters.AddRange(parameters);`
`  54`  `                return cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  55`  `            }`
`  56`  `        }`

---

### `ExecuteScalar` — lines 57–67

```
public static object ExecuteScalar(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalar`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string sql, params SqlParameter[] parameters`
- **Local variables:** `conn`, `cmd`

#### Line-by-line (this function)

`  57`  ``
`  58`  `        public static object ExecuteScalar(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  59`  `        {`
`  60`  `            using (var conn = OpenConnection())`
  - → Import namespace/types.
`  61`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`  62`  `            {`
`  63`  `                if (parameters != null && parameters.Length > 0)`
`  64`  `                cmd.Parameters.AddRange(parameters);`
`  65`  `                return cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`  66`  `            }`
`  67`  `        }`

---

### `ExecuteScalarInt` — lines 68–74

```
public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalarInt`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string sql, params SqlParameter[] parameters`
- **Local variables:** `result`

#### Line-by-line (this function)

`  68`  ``
`  69`  `        public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  70`  `        {`
`  71`  `            var result = ExecuteScalar(sql, parameters);`
  - → Run SQL; return table / rows / scalar.
`  72`  `            if (result == null || result == DBNull.Value) return 0;`
`  73`  `            return Convert.ToInt32(result);`
`  74`  `        }`

---

### `ExecuteScalarDecimal` — lines 75–81

```
public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)
```

#### Explanation

- **Purpose:** Implements `ExecuteScalarDecimal`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string sql, params SqlParameter[] parameters`
- **Local variables:** `result`

#### Line-by-line (this function)

`  75`  ``
`  76`  `        public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  77`  `        {`
`  78`  `            var result = ExecuteScalar(sql, parameters);`
  - → Run SQL; return table / rows / scalar.
`  79`  `            if (result == null || result == DBNull.Value) return 0m;`
`  80`  `            return Convert.ToDecimal(result);`
`  81`  `        }`

---

### `P` — lines 82–86

```
public static SqlParameter P(string name, object value)
```

#### Explanation

- **Purpose:** Implements `P`.
- **Data:** Pure SQL via DbHelper/SqlClient (parameterized).
- **Parameters:** `string name, object value`

#### Line-by-line (this function)

`  82`  ``
`  83`  `        public static SqlParameter P(string name, object value)`
`  84`  `        {`
`  85`  `            return new SqlParameter(name, value ?? DBNull.Value);`
`  86`  `        }`

---

### `SafeString` — lines 87–92

```
public static string SafeString(object value)
```

#### Explanation

- **Purpose:** Implements `SafeString`.
- **Parameters:** `object value`

#### Line-by-line (this function)

`  87`  ``
`  88`  `        public static string SafeString(object value)`
`  89`  `        {`
`  90`  `            if (value == null || value == DBNull.Value) return string.Empty;`
`  91`  `            return value.ToString();`
`  92`  `        }`

---

### `SafeInt` — lines 93–98

```
public static int? SafeInt(object value)
```

#### Explanation

- **Purpose:** Implements `SafeInt`.
- **Parameters:** `object value`

#### Line-by-line (this function)

`  93`  ``
`  94`  `        public static int? SafeInt(object value)`
`  95`  `        {`
`  96`  `            if (value == null || value == DBNull.Value) return null;`
`  97`  `            return Convert.ToInt32(value);`
`  98`  `        }`

---

### `SafeDecimal` — lines 99–104

```
public static decimal? SafeDecimal(object value)
```

#### Explanation

- **Purpose:** Implements `SafeDecimal`.
- **Parameters:** `object value`

#### Line-by-line (this function)

`  99`  ``
` 100`  `        public static decimal? SafeDecimal(object value)`
` 101`  `        {`
` 102`  `            if (value == null || value == DBNull.Value) return null;`
` 103`  `            return Convert.ToDecimal(value);`
` 104`  `        }`

---

### `SafeDate` — lines 105–110

```
public static DateTime? SafeDate(object value)
```

#### Explanation

- **Purpose:** Implements `SafeDate`.
- **Parameters:** `object value`

#### Line-by-line (this function)

` 105`  ``
` 106`  `        public static DateTime? SafeDate(object value)`
` 107`  `        {`
` 108`  `            if (value == null || value == DBNull.Value) return null;`
` 109`  `            return Convert.ToDateTime(value);`
` 110`  `        }`

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
`   8`  `    /// <summary>`
`   9`  `    /// Centralized SQL helper bound to EduDB.mdf via Web.config MyDbConn.`
`  10`  `    /// </summary>`
`  11`  `    public static class DbHelper`
  - → Database access (pure SQL).
`  12`  `    {`
`  13`  `        public static string ConnectionString`
`  14`  `        {`
`  15`  `            get`
`  16`  `            {`
`  17`  `                var cs = ConfigurationManager.ConnectionStrings["MyDbConn"];`
`  18`  `                if (cs == null || string.IsNullOrWhiteSpace(cs.ConnectionString))`
`  19`  `                throw new InvalidOperationException("Connection string 'MyDbConn' is missing from Web.config.");`
`  20`  `                return cs.ConnectionString;`
`  21`  `            }`
`  22`  `        }`
`  23`  ``
`  24`  `        public static SqlConnection OpenConnection()`
  - → Database access (pure SQL).
`  25`  `        {`
`  26`  `            var conn = new SqlConnection(ConnectionString);`
  - → Database access (pure SQL).
`  27`  `            conn.Open();`
`  28`  `            return conn;`
`  29`  `        }`
`  30`  ``
`  31`  `        public static DataTable ExecuteQuery(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  32`  `        {`
`  33`  `            using (var conn = OpenConnection())`
  - → Import namespace/types.
`  34`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`  35`  `            {`
`  36`  `                if (parameters != null && parameters.Length > 0)`
`  37`  `                cmd.Parameters.AddRange(parameters);`
`  38`  `                using (var adapter = new SqlDataAdapter(cmd))`
  - → Import namespace/types.
`  39`  `                {`
`  40`  `                    var dt = new DataTable();`
`  41`  `                    adapter.Fill(dt);`
`  42`  `                    return dt;`
`  43`  `                }`
`  44`  `            }`
`  45`  `        }`
`  46`  ``
`  47`  `        public static int ExecuteNonQuery(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  48`  `        {`
`  49`  `            using (var conn = OpenConnection())`
  - → Import namespace/types.
`  50`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`  51`  `            {`
`  52`  `                if (parameters != null && parameters.Length > 0)`
`  53`  `                cmd.Parameters.AddRange(parameters);`
`  54`  `                return cmd.ExecuteNonQuery();`
  - → Run SQL; return table / rows / scalar.
`  55`  `            }`
`  56`  `        }`
`  57`  ``
`  58`  `        public static object ExecuteScalar(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  59`  `        {`
`  60`  `            using (var conn = OpenConnection())`
  - → Import namespace/types.
`  61`  `            using (var cmd = new SqlCommand(sql, conn))`
  - → Import namespace/types.
`  62`  `            {`
`  63`  `                if (parameters != null && parameters.Length > 0)`
`  64`  `                cmd.Parameters.AddRange(parameters);`
`  65`  `                return cmd.ExecuteScalar();`
  - → Run SQL; return table / rows / scalar.
`  66`  `            }`
`  67`  `        }`
`  68`  ``
`  69`  `        public static int ExecuteScalarInt(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  70`  `        {`
`  71`  `            var result = ExecuteScalar(sql, parameters);`
  - → Run SQL; return table / rows / scalar.
`  72`  `            if (result == null || result == DBNull.Value) return 0;`
`  73`  `            return Convert.ToInt32(result);`
`  74`  `        }`
`  75`  ``
`  76`  `        public static decimal ExecuteScalarDecimal(string sql, params SqlParameter[] parameters)`
  - → Run SQL; return table / rows / scalar.
`  77`  `        {`
`  78`  `            var result = ExecuteScalar(sql, parameters);`
  - → Run SQL; return table / rows / scalar.
`  79`  `            if (result == null || result == DBNull.Value) return 0m;`
`  80`  `            return Convert.ToDecimal(result);`
`  81`  `        }`
`  82`  ``
`  83`  `        public static SqlParameter P(string name, object value)`
`  84`  `        {`
`  85`  `            return new SqlParameter(name, value ?? DBNull.Value);`
`  86`  `        }`
`  87`  ``
`  88`  `        public static string SafeString(object value)`
`  89`  `        {`
`  90`  `            if (value == null || value == DBNull.Value) return string.Empty;`
`  91`  `            return value.ToString();`
`  92`  `        }`
`  93`  ``
`  94`  `        public static int? SafeInt(object value)`
`  95`  `        {`
`  96`  `            if (value == null || value == DBNull.Value) return null;`
`  97`  `            return Convert.ToInt32(value);`
`  98`  `        }`
`  99`  ``
` 100`  `        public static decimal? SafeDecimal(object value)`
` 101`  `        {`
` 102`  `            if (value == null || value == DBNull.Value) return null;`
` 103`  `            return Convert.ToDecimal(value);`
` 104`  `        }`
` 105`  ``
` 106`  `        public static DateTime? SafeDate(object value)`
` 107`  `        {`
` 108`  `            if (value == null || value == DBNull.Value) return null;`
` 109`  `            return Convert.ToDateTime(value);`
` 110`  `        }`
` 111`  `    }`
` 112`  `}`

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
