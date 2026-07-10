import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()

DATABRICKS_SCHEMAS = ["asset_management", "insurance", "pension"]

def get_cosmos_container():
    client = CosmosClient(
        url=os.getenv("COSMOS_ENDPOINT"),
        credential=os.getenv("COSMOS_KEY")
    )
    database = client.get_database_client(os.getenv("COSMOS_DATABASE_NAME"))
    container = database.get_container_client(os.getenv("COSMOS_CONTAINER_NAME"))
    print("Cosmos DB connection successful")
    return container


def fetch_databricks_tables(container):
    all_tables = []
    for schema in DATABRICKS_SCHEMAS:
        query = f"""
            SELECT *
            FROM c
            WHERE c.schema = '{schema}'
              AND c.is_latest = true
              AND c.source_platform = 'Databricks'
        """
        items = list(container.query_items(
            query=query,
            enable_cross_partition_query=False,
            partition_key=schema
        ))
        print(f"Fetched {len(items)} tables from schema: {schema}")
        all_tables.extend(items)

    print(f"\nTotal Databricks tables fetched: {len(all_tables)}")
    return all_tables