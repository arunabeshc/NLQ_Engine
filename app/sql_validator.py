import os
import sqlglot
import snowflake.connector
from databricks import sql as databricks_sql
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization
from pathlib import Path

load_dotenv()

SKIP_KEYWORDS = {
    "count", "sum", "avg", "max", "min", "null",
    "true", "false", "current_date", "current_timestamp"
}


# ─────────────────────────────────────────
# Database connections
# ─────────────────────────────────────────

def get_snowflake_connection():

    private_key_path = os.getenv(
        "SNOWFLAKE_PRIVATE_KEY_PATH",
        str(Path(__file__).resolve().parent.parent / "secrets" / "snowflake_private_key.pem")
    )

    private_key_password = os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSWORD")

    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=(
                private_key_password.encode()
                if private_key_password
                else None
            )
        )

    private_key_der = private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        private_key=private_key_der,
        role=os.getenv("SNOWFLAKE_ROLE"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE")
    )


def get_databricks_connection():
    return databricks_sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN")
    )


# ─────────────────────────────────────────
# Step 1 — Syntax Validation via sqlglot
# ─────────────────────────────────────────

def validate_syntax(sql, platform):

    if sql == "UNABLE_TO_GENERATE":
        return {
            "valid": False,
            "issues": ["SQL could not be generated for this question"]
        }

    dialect = "snowflake" if platform == "SNOWFLAKE" else "databricks"

    try:
        sqlglot.parse_one(sql, dialect=dialect)
        return {"valid": True, "issues": []}

    except sqlglot.errors.ParseError as e:
        return {"valid": False, "issues": [str(e)]}


# ─────────────────────────────────────────
# Step 2 — Extract columns mapped to tables
# ─────────────────────────────────────────

def extract_columns_by_table(sql, platform):

    dialect = "snowflake" if platform == "SNOWFLAKE" else "databricks"

    try:
        parsed = sqlglot.parse_one(sql, dialect=dialect)
    except Exception:
        return {}

    # Build alias map
    alias_map = {}
    for table in parsed.find_all(sqlglot.exp.Table):
        table_name = table.name.lower()
        alias = table.alias.lower() if table.alias else None
        if alias:
            alias_map[alias] = table_name
        alias_map[table_name] = table_name

    # Map columns to their tables
    columns_by_table = {}
    for col in parsed.find_all(sqlglot.exp.Column):
        col_name = col.name.lower()
        table_ref = col.table.lower() if col.table else None

        if not col_name or col_name in SKIP_KEYWORDS:
            continue

        resolved_table = alias_map.get(table_ref) if table_ref else None

        if resolved_table not in columns_by_table:
            columns_by_table[resolved_table] = []

        if col_name not in columns_by_table[resolved_table]:
            columns_by_table[resolved_table].append(col_name)

    return columns_by_table


# ─────────────────────────────────────────
# Step 3 — Validate tables and columns
# directly against INFORMATION_SCHEMA
# ─────────────────────────────────────────

def validate_against_db(columns_by_table, platform, domain):

    issues = []

    if not columns_by_table:
        return {"valid": True, "issues": []}

    try:
        if platform == "SNOWFLAKE":
            conn = get_snowflake_connection()
            cursor = conn.cursor()

            for table_name, columns in columns_by_table.items():

                if not table_name:
                    continue

                # Validate table exists
                cursor.execute(f"""
                    SELECT COUNT(*)
                    FROM {os.getenv("SNOWFLAKE_DATABASE")}.INFORMATION_SCHEMA.TABLES
                    WHERE LOWER(TABLE_NAME) = '{table_name}'
                    AND LOWER(TABLE_SCHEMA) = '{domain}'
                """)
                table_count = cursor.fetchone()[0]

                if table_count == 0:
                    issues.append(
                        f"Table '{table_name}' does not exist in schema '{domain}'"
                    )
                    continue

                # Validate each column exists in that table
                for column in columns:
                    cursor.execute(f"""
                        SELECT COUNT(*)
                        FROM {os.getenv("SNOWFLAKE_DATABASE")}.INFORMATION_SCHEMA.COLUMNS
                        WHERE LOWER(TABLE_NAME) = '{table_name}'
                        AND LOWER(COLUMN_NAME) = '{column}'
                        AND LOWER(TABLE_SCHEMA) = '{domain}'
                    """)
                    col_count = cursor.fetchone()[0]

                    if col_count == 0:
                        issues.append(
                            f"Column '{column}' does not exist in table '{table_name}'"
                        )

            cursor.close()
            conn.close()

        else:
            # Databricks
            conn = get_databricks_connection()
            cursor = conn.cursor()

            for table_name, columns in columns_by_table.items():

                if not table_name:
                    continue

                # Validate table exists
                cursor.execute(f"""
                    SELECT COUNT(*)
                    FROM keyrus_marketplace.information_schema.tables
                    WHERE LOWER(table_name) = '{table_name}'
                    AND LOWER(table_schema) = '{domain}'
                """)
                table_count = cursor.fetchone()[0]

                if table_count == 0:
                    issues.append(
                        f"Table '{table_name}' does not exist in schema '{domain}'"
                    )
                    continue

                # Validate each column exists in that table
                for column in columns:
                    cursor.execute(f"""
                        SELECT COUNT(*)
                        FROM keyrus_marketplace.information_schema.columns
                        WHERE LOWER(table_name) = '{table_name}'
                        AND LOWER(column_name) = '{column}'
                        AND LOWER(table_schema) = '{domain}'
                    """)
                    col_count = cursor.fetchone()[0]

                    if col_count == 0:
                        issues.append(
                            f"Column '{column}' does not exist in table '{table_name}'"
                        )

            cursor.close()
            conn.close()

    except Exception as e:
        issues.append(f"Validation error: {str(e)}")

    return {
        "valid": len(issues) == 0,
        "issues": issues
    }


# ─────────────────────────────────────────
# Step 4 — EXPLAIN query
# dry run to catch logical errors
# ─────────────────────────────────────────

def explain_query(sql, platform):

    try:
        if platform == "SNOWFLAKE":
            conn = get_snowflake_connection()
            cursor = conn.cursor()
            cursor.execute(f"EXPLAIN {sql}")
            cursor.close()
            conn.close()

        else:
            conn = get_databricks_connection()
            cursor = conn.cursor()
            cursor.execute(f"EXPLAIN {sql}")
            cursor.close()
            conn.close()

        return {"valid": True, "issues": []}

    except Exception as e:
        return {
            "valid": False,
            "issues": [f"Query explanation failed: {str(e)}"]
        }


# ─────────────────────────────────────────
# Main validator — runs all checks
# ─────────────────────────────────────────

def validate_sql(sql, platform, domain):

    all_issues = []

    # Step 1 — Syntax check
    syntax_result = validate_syntax(sql, platform)
    if not syntax_result["valid"]:
        return {
            "syntax_valid": False,
            "schema_valid": False,
            "explain_valid": False,
            "issues": syntax_result["issues"]
        }

    # Step 2 — Extract columns mapped to tables
    columns_by_table = extract_columns_by_table(sql, platform)

    # Step 3 — Validate tables and columns against DB
    db_result = validate_against_db(
        columns_by_table, platform, domain
    )
    all_issues.extend(db_result["issues"])

    # Step 4 — EXPLAIN query
    explain_result = explain_query(sql, platform)
    all_issues.extend(explain_result["issues"])

    return {
        "syntax_valid": True,
        "schema_valid": db_result["valid"],
        "explain_valid": explain_result["valid"],
        "columns_by_table": columns_by_table,
        "issues": all_issues
    }