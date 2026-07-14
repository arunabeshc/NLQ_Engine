import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

openai_client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")


def build_system_prompt(context):

    tables = context.get("tables", [])
    columns = context.get("columns", [])
    joins = context.get("joins", [])
    glossary = context.get("glossary", [])
    sample_queries = context.get("sample_queries", [])
    platform = context.get("platform", "unknown")
    domain = context.get("domain", "unknown")

    # Build table summary
    table_summary = "\n".join([
        f"- {t.get('table_name')} ({t.get('schema_name')}): {t.get('description', 'No description')}"
        for t in tables
    ])

    # Build column summary
    column_summary = "\n".join([
        f"- {c.get('table_name')}.{c.get('column_name')} [{c.get('data_type')}]: {c.get('comment', 'No description')}"
        for c in columns
    ])

    # Build join summary
    join_summary = "\n".join([
        f"- {j.get('left_table')}.{j.get('left_key')} → {j.get('right_table')}.{j.get('right_key')} ({j.get('join_type')} JOIN, {j.get('cardinality')})"
        for j in joins
    ])

    # Build glossary summary
    glossary_summary = "\n".join([
        f"- {g.get('term')}: {g.get('definition')}"
        for g in glossary
    ])

    # Build sample queries summary
    sample_summary = "\n".join([
        f"- Q: {s.get('natural_language')}\n  SQL: {s.get('sql', '').strip()}"
        for s in sample_queries
    ])

    # Platform-specific SQL dialect instructions
    if platform == "SNOWFLAKE":
        dialect_instructions = """
        - Use Snowflake SQL syntax strictly
        - For date arithmetic use DATEADD(month, -1, CURRENT_DATE())
        - For month formatting use TO_CHAR(DATEADD(month, -1, CURRENT_DATE()), 'YYYY-MM')
        - Fully qualify table names as DATABASE.SCHEMA.TABLE_NAME
        - Use LIMIT for row limiting
        """
    else:
        dialect_instructions = """
        - Use Databricks SQL / Spark SQL syntax strictly
        - For date arithmetic use:
        - Previous month: ADD_MONTHS(CURRENT_DATE(), -1)
        - For month formatting: DATE_FORMAT(ADD_MONTHS(CURRENT_DATE(), -1), 'yyyy-MM')
        - For subtracting days: DATE_SUB(CURRENT_DATE(), 30) — integer only, no INTERVAL
        - For adding days: DATE_ADD(CURRENT_DATE(), 30) — integer only, no INTERVAL
        - For subtracting months: ADD_MONTHS(CURRENT_DATE(), -6)
        - Never use DATEADD() — Snowflake syntax
        - Never use DATE_SUB with INTERVAL — use DATE_SUB(date, integer) instead
        - Never use DATE_ADD with INTERVAL — use DATE_ADD(date, integer) instead
        - Fully qualify table names as keyrus_marketplace.SCHEMA.TABLE_NAME
        - Use LIMIT for row limiting
        - Use backticks for column names with special characters
        """

    return f"""
You are an expert SQL generator for a regulated financial services data platform.

Your job is to generate accurate, executable SQL based on the user's natural language question.
You must only use the tables, columns, and joins provided in the context below.
Never fabricate table names, column names, or join conditions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PLATFORM & DOMAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Platform: {platform}
Domain: {domain}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SQL DIALECT RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{dialect_instructions}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AVAILABLE TABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{table_summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AVAILABLE COLUMNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{column_summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOIN CONDITIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{join_summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BUSINESS GLOSSARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{glossary_summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SIMILAR QUERIES FOR REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{sample_summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT RULES — NON NEGOTIABLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Return ONLY the SQL query — no explanation, no markdown, no backticks
2. Always add LIMIT 5 at the end unless the question explicitly asks for more
3. Never use SELECT * — always name the columns explicitly
4. Never fabricate columns or tables not listed above
5. If the question cannot be answered with the available schema — return exactly: UNABLE_TO_GENERATE
""".strip()


def generate_sql(question, context):

    system_prompt = build_system_prompt(context)

    response = openai_client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0,
        max_tokens=1000
    )

    sql = response.choices[0].message.content.strip()

    return sql