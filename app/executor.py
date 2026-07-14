import os
import snowflake.connector
from databricks import sql as databricks_sql
from dotenv import load_dotenv

load_dotenv()


# ─────────────────────────────────────────
# Connections
# ─────────────────────────────────────────

def get_snowflake_connection():
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
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
# Enforce LIMIT 5 on the SQL
# ─────────────────────────────────────────

def enforce_limit(sql, limit=5):
    sql_upper = sql.upper().strip()
    if "LIMIT" in sql_upper:
        return sql
    return f"{sql.strip()}\nLIMIT {limit}"


# ─────────────────────────────────────────
# Execute on Snowflake
# ─────────────────────────────────────────

def execute_snowflake(sql):
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        results = []
        for row in rows:
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[columns[idx]] = (
                    str(value) if value is not None else None
                )
            results.append(row_dict)

        return {
            "success": True,
            "rows": results,
            "row_count": len(results)
        }

    except Exception as e:
        return {
            "success": False,
            "rows": [],
            "row_count": 0,
            "error": str(e)
        }

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────
# Execute on Databricks
# ─────────────────────────────────────────

def execute_databricks(sql):
    conn = get_databricks_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        results = []
        for row in rows:
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[columns[idx]] = (
                    str(value) if value is not None else None
                )
            results.append(row_dict)

        return {
            "success": True,
            "rows": results,
            "row_count": len(results)
        }

    except Exception as e:
        return {
            "success": False,
            "rows": [],
            "row_count": 0,
            "error": str(e)
        }

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────
# Main executor — routes to correct platform
# ─────────────────────────────────────────

def execute_sql(sql, platform):

    if sql == "UNABLE_TO_GENERATE":
        return {
            "success": False,
            "rows": [],
            "row_count": 0,
            "error": "SQL could not be generated for this question"
        }

    # Enforce LIMIT 5 as a safety net
    sql = enforce_limit(sql, limit=5)

    if platform == "SNOWFLAKE":
        return execute_snowflake(sql)
    elif platform == "DATABRICKS":
        return execute_databricks(sql)
    else:
        return {
            "success": False,
            "rows": [],
            "row_count": 0,
            "error": f"Unknown platform: {platform}"
        }