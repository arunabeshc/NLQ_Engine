import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")

# --------------------------------------------------
# Configure what to delete
# --------------------------------------------------

# Choose which index to clear
INDEX_NAME = "sample-queries"  # Change to any of the 5 indexes:
                                   # table-definitions
                                   # column-definitions
                                   # join-conditions
                                   # business-glossary
                                   # sample-queries

# Leave empty to delete ALL documents in the index
# Or specify specific IDs to delete selectively
IDS_TO_DELETE = [
    # "asset_management.dp_fund_master",
    # "asset_management.dp_fund_flows",
]

# --------------------------------------------------
# Connect
# --------------------------------------------------
client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=AzureKeyCredential(SEARCH_KEY)
)

# --------------------------------------------------
# Fetch documents to delete
# --------------------------------------------------
if IDS_TO_DELETE:
    # Delete specific IDs
    filter_str = " or ".join([f"id eq '{i}'" for i in IDS_TO_DELETE])
    results = client.search(
        search_text="*",
        filter=filter_str,
        select=["id"]
    )
else:
    # Delete ALL documents in the index
    results = client.search(
        search_text="*",
        select=["id"]
    )

docs_to_delete = [{"id": doc["id"]} for doc in results]

# --------------------------------------------------
# Delete
# --------------------------------------------------
if not docs_to_delete:
    print(f"No documents found in {INDEX_NAME}. Nothing deleted.")
else:
    client.delete_documents(documents=docs_to_delete)
    print(f"Deleted {len(docs_to_delete)} documents from: {INDEX_NAME}")