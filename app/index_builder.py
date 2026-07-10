import os
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SearchField as VectorField,
)
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
VECTOR_DIMENSIONS = 3072

openai_client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

credential = AzureKeyCredential(SEARCH_KEY)
index_client = SearchIndexClient(SEARCH_ENDPOINT, credential)


def generate_embedding(text):
    if not text or text.strip() == "":
        return [0.0] * VECTOR_DIMENSIONS
    response = openai_client.embeddings.create(
        input=text,
        model=EMBEDDING_DEPLOYMENT
    )
    return response.data[0].embedding


def get_vector_search_config():
    return VectorSearch(
        algorithms=[
            HnswAlgorithmConfiguration(name="hnsw-config")
        ],
        profiles=[
            VectorSearchProfile(
                name="vector-profile",
                algorithm_configuration_name="hnsw-config"
            )
        ]
    )


def create_index(name, fields):
    vector_search = get_vector_search_config()
    index = SearchIndex(
        name=name,
        fields=fields,
        vector_search=vector_search
    )
    index_client.create_or_update_index(index)
    print(f"Index created/updated: {name}")


def create_all_indexes():

    # Index 1 — table-definitions
    create_index("table-definitions", [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="table_name", type=SearchFieldDataType.String),
        SearchableField(name="schema_name", type=SearchFieldDataType.String),
        SimpleField(name="catalog", type=SearchFieldDataType.String, filterable=True),
        SimpleField(name="source_platform", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="description", type=SearchFieldDataType.String),
        SimpleField(name="refresh_frequency", type=SearchFieldDataType.String),
        SimpleField(name="classification", type=SearchFieldDataType.String, filterable=True),
        SimpleField(name="owner", type=SearchFieldDataType.String),
        SimpleField(name="row_count", type=SearchFieldDataType.String),
        SearchableField(name="content", type=SearchFieldDataType.String),
        VectorField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=VECTOR_DIMENSIONS,
            vector_search_profile_name="vector-profile"
        )
    ])

    # Index 2 — column-definitions
    create_index("column-definitions", [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="table_name", type=SearchFieldDataType.String),
        SearchableField(name="schema_name", type=SearchFieldDataType.String),
        SearchableField(name="column_name", type=SearchFieldDataType.String),
        SimpleField(name="data_type", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="comment", type=SearchFieldDataType.String),
        SimpleField(name="is_foreign_key", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="content", type=SearchFieldDataType.String),
        VectorField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=VECTOR_DIMENSIONS,
            vector_search_profile_name="vector-profile"
        )
    ])

    # Index 3 — join-conditions
    create_index("join-conditions", [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="left_table", type=SearchFieldDataType.String),
        SearchableField(name="right_table", type=SearchFieldDataType.String),
        SimpleField(name="left_key", type=SearchFieldDataType.String),
        SimpleField(name="right_key", type=SearchFieldDataType.String),
        SimpleField(name="join_type", type=SearchFieldDataType.String, filterable=True),
        SimpleField(name="cardinality", type=SearchFieldDataType.String),
        SimpleField(name="schema_left", type=SearchFieldDataType.String, filterable=True),
        SimpleField(name="schema_right", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="content", type=SearchFieldDataType.String),
        VectorField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=VECTOR_DIMENSIONS,
            vector_search_profile_name="vector-profile"
        )
    ])

    # Index 4 — business-glossary
    create_index("business-glossary", [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="term", type=SearchFieldDataType.String),
        SearchableField(name="definition", type=SearchFieldDataType.String),
        SimpleField(name="domain", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="mapped_tables", type=SearchFieldDataType.String),
        SearchableField(name="mapped_columns", type=SearchFieldDataType.String),
        SimpleField(name="regulatory_context", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="content", type=SearchFieldDataType.String),
        VectorField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=VECTOR_DIMENSIONS,
            vector_search_profile_name="vector-profile"
        )
    ])

    # Index 5 — sample-queries
    create_index("sample-queries", [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="natural_language", type=SearchFieldDataType.String),
        SearchableField(name="sql", type=SearchFieldDataType.String),
        SearchableField(name="tables_used", type=SearchFieldDataType.String),
        SimpleField(name="schema_name", type=SearchFieldDataType.String, filterable=True),
        SimpleField(name="domain", type=SearchFieldDataType.String, filterable=True),
        SimpleField(name="complexity", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="content", type=SearchFieldDataType.String),
        VectorField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=VECTOR_DIMENSIONS,
            vector_search_profile_name="vector-profile"
        )
    ])


def get_search_client(index_name):
    return SearchClient(
        endpoint=SEARCH_ENDPOINT,
        index_name=index_name,
        credential=credential
    )

def document_exists(index_name, doc_id):
    client = get_search_client(index_name)
    try:
        client.get_document(key=doc_id)
        return True
    except Exception:
        return False

def upload_documents(index_name, documents):
    client = get_search_client(index_name)
    to_upload = []
    skipped = 0

    for doc in documents:
        if document_exists(index_name, doc["id"]):
            skipped += 1
        else:
            to_upload.append(doc)

    if to_upload:
        batch_size = 100
        for i in range(0, len(to_upload), batch_size):
            batch = to_upload[i:i + batch_size]
            client.upload_documents(documents=batch)
            print(f"Uploaded {len(batch)} documents to {index_name}")

    print(f"Skipped {skipped} existing documents in {index_name}")