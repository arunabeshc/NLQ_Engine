import os
import re
from dotenv import load_dotenv
from cosmos_reader import get_cosmos_container, fetch_databricks_tables
from index_builder import (
    create_all_indexes,
    generate_embedding,
    upload_documents
)
from mock_data import JOIN_CONDITIONS, BUSINESS_GLOSSARY, SAMPLE_QUERIES

load_dotenv()


# ─────────────────────────────────────────
# Document builders — one per index
# ─────────────────────────────────────────

def build_table_definition_docs(tables):
    docs = []
    for t in tables:
        props = t.get("table_properties", {})

        # Generate description if null
        description = t.get("description")
        if not description:
            table_name = t["table_name"]
            readable_name = (
                table_name
                .replace("src_", "")
                .replace("ref_", "")
                .replace("_", " ")
            )
            description = f"Source table containing {readable_name} data"

        content = (
            f"Table {t['table_name']} in {t['schema']} schema "
            f"on {t.get('source_platform', 'unknown')}. "
            f"{description}. "
            f"Columns: {', '.join([c['name'] for c in t.get('columns', [])])}."
        )

        doc = {
            "id": f"{t['schema']}_{t['table_name']}",
            "table_name": t["table_name"],
            "schema_name": t["schema"],
            "catalog": t.get("catalog", ""),
            "source_platform": t.get("source_platform", ""),
            "description": description,
            "refresh_frequency": props.get("data_product.refresh_frequency", ""),
            "classification": props.get("data_product.classification", ""),
            "owner": props.get("data_product.owner", ""),
            "row_count": props.get("snowflake.row_count", ""),
            "content": content,
            "content_vector": generate_embedding(content)
        }
        docs.append(doc)
        print(f"Built table definition: {doc['id']}")
    return docs


def build_column_definition_docs(tables):
    docs = []
    for t in tables:
        for col in t.get("columns", []):
            fk_indicators = ["_id", "_code", "_key", "_ref"]
            is_fk = any(col["name"].lower().endswith(ind) for ind in fk_indicators)

            content = f"""
                Column {col['name']} in table {t['table_name']} 
                schema {t['schema']}.
                Data type: {col['type']}.
                Description: {col.get('comment', 'No description')}.
                {'This column is a likely foreign key.' if is_fk else ''}
            """.strip()

            col_id = f"{t['schema']}.{t['table_name']}.{col['name']}"
            col_id = re.sub(r'[^a-zA-Z0-9_\-]', '_', col_id)

            doc = {
                "id": col_id,
                "table_name": t["table_name"],
                "schema_name": t["schema"],
                "column_name": col["name"],
                "data_type": col["type"],
                "comment": col.get("comment", ""),
                "is_foreign_key": "YES" if is_fk else "NO",
                "content": content,
                "content_vector": generate_embedding(content)
            }
            docs.append(doc)
    print(f"Built {len(docs)} column definition documents")
    return docs


def build_join_condition_docs(join_conditions):
    docs = []
    for j in join_conditions:
        doc = {
            **j,
            "content_vector": generate_embedding(j["content"])
        }
        docs.append(doc)
    print(f"Built {len(docs)} join condition documents")
    return docs


def build_glossary_docs(glossary):
    docs = []
    for g in glossary:
        doc = {
            **g,
            "content_vector": generate_embedding(g["content"])
        }
        docs.append(doc)
    print(f"Built {len(docs)} business glossary documents")
    return docs


def build_sample_query_docs(queries):
    docs = []
    for q in queries:
        doc = {
            **q,
            "content_vector": generate_embedding(q["content"])
        }
        docs.append(doc)
    print(f"Built {len(docs)} sample query documents")
    return docs


# ─────────────────────────────────────────
# Main orchestrator
# ─────────────────────────────────────────

def run():
    print("=== Search Indexer — Starting ===\n")

    # Step 1 — Create all 5 indexes
    print("--- Creating indexes ---")
    create_all_indexes()

    # Step 2 — Fetch Databricks tables from Cosmos DB
    print("\n--- Fetching Databricks tables from Cosmos DB ---")
    container = get_cosmos_container()
    tables = fetch_databricks_tables(container)

    # Step 3 — Build and upload table definitions
    print("\n--- Index 1: Table Definitions ---")
    table_docs = build_table_definition_docs(tables)
    upload_documents("table-definitions", table_docs)

    # Step 4 — Build and upload column definitions
    print("\n--- Index 2: Column Definitions ---")
    column_docs = build_column_definition_docs(tables)
    upload_documents("column-definitions", column_docs)

    # Step 5 — Build and upload join conditions
    print("\n--- Index 3: Join Conditions ---")
    join_docs = build_join_condition_docs(JOIN_CONDITIONS)
    upload_documents("join-conditions", join_docs)

    # Step 6 — Build and upload business glossary
    print("\n--- Index 4: Business Glossary ---")
    glossary_docs = build_glossary_docs(BUSINESS_GLOSSARY)
    upload_documents("business-glossary", glossary_docs)

    # Step 7 — Build and upload sample queries
    print("\n--- Index 5: Sample Queries ---")
    query_docs = build_sample_query_docs(SAMPLE_QUERIES)
    upload_documents("sample-queries", query_docs)

    print("\n=== Search Indexer — Complete ===")
    print(f"Table definitions : {len(table_docs)}")
    print(f"Column definitions: {len(column_docs)}")
    print(f"Join conditions   : {len(join_docs)}")
    print(f"Glossary terms    : {len(glossary_docs)}")
    print(f"Sample queries    : {len(query_docs)}")


if __name__ == "__main__":
    run()