import os
from collections import Counter
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
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

# ─────────────────────────────────────────
# Domain keyword map
# ─────────────────────────────────────────

DOMAIN_KEYWORDS = {
    "source": [
        "source schema", "snowflake", "src_", "ref_",
        "src_customers", "src_orders", "src_trades",
        "src_positions", "src_payments", "src_order_lines",
        "src_products", "src_orders_small", "src_counterparty",
        "ref_currency", "ref_country", "ref_region",
        "ref_instrument", "ref_promotion",
        "currencies", "currency code", "currency name",
        "promo code", "promotion", "discount",
        "counterparty", "trade", "position", "instrument",
        "active customers", "customers", "orders",
        "payment status", "payment", "order value",
        "order lines", "products", "region",
        "active instruments", "risk rating",
        "buy sell", "market value", "pnl",
        "line amount", "quantity"
    ],
    "asset_management": [
        "fund", "aum", "nav", "ocf", "esg", "sfdr",
        "holdings", "flows", "performance", "sharpe",
        "tracking error", "redemption", "article 9",
        "asset class", "benchmark", "volatility",
        "inflows", "outflows", "carbon intensity"
    ],
    "insurance": [
        "policy", "claim", "premium", "renewal", "fraud",
        "underwriting", "churn", "insurer", "lapse",
        "risk band", "settlement", "no claims",
        "missed payment", "delinquency", "broker"
    ],
    "pension": [
        "pension", "member", "contribution", "drawdown",
        "annuity", "retirement", "scheme", "allowance",
        "vulnerability", "consumer duty", "pot size",
        "lapse propensity", "engagement", "tax year",
        "value for money", "auto enrol", "workplace"
    ]
}


# ─────────────────────────────────────────
# Keyword-based domain inference
# ─────────────────────────────────────────

def infer_domain_from_keywords(question):
    question_lower = question.lower()
    scores = {domain: 0 for domain in DOMAIN_KEYWORDS}

    for domain, keywords in DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in question_lower:
                scores[domain] += 1

    best_domain = max(scores, key=scores.get)

    if scores[best_domain] == 0:
        return None

    return best_domain


# ─────────────────────────────────────────
# Embedding generation
# ─────────────────────────────────────────

def generate_embedding(text):
    response = openai_client.embeddings.create(
        input=text,
        model=EMBEDDING_DEPLOYMENT
    )
    return response.data[0].embedding


# ─────────────────────────────────────────
# Search a single index
# ─────────────────────────────────────────

def search_index(index_name, query, top=5):
    client = SearchClient(
        endpoint=SEARCH_ENDPOINT,
        index_name=index_name,
        credential=credential
    )

    vector_query = VectorizedQuery(
        vector=generate_embedding(query),
        k_nearest_neighbors=top,
        fields="content_vector"
    )

    results = client.search(
        search_text=query,
        vector_queries=[vector_query],
        top=top
    )

    return [dict(r) for r in results]


# ─────────────────────────────────────────
# Retrieve full context for SQL generation
# ─────────────────────────────────────────

def retrieve_context(question):

    # Step 1 — keyword domain hint
    keyword_domain = infer_domain_from_keywords(question)

    # Step 2 — search all 5 indexes
    table_results = search_index(
        "table-definitions", question, top=5
    )
    column_results = search_index(
        "column-definitions", question, top=10
    )
    join_results = search_index(
        "join-conditions", question, top=5
    )
    glossary_results = search_index(
        "business-glossary", question, top=3
    )
    sample_results = search_index(
        "sample-queries", question, top=3
    )

    # Step 3 — domain and platform inference
    domain = "unknown"
    platform = "unknown"

    # Hardcoded platform map as fallback
    platform_map_static = {
        "source": "SNOWFLAKE",
        "asset_management": "DATABRICKS",
        "insurance": "DATABRICKS",
        "pension": "DATABRICKS"
    }

    if keyword_domain:
        # Keyword hint takes priority
        domain = keyword_domain

        # Try to get platform from search results
        matching_tables = [
            t for t in table_results
            if t.get("schema_name") == domain
        ]

        if matching_tables:
            platform = matching_tables[0].get(
                "source_platform", "unknown"
            ).upper()
        else:
            # Fall back to static map
            platform = platform_map_static.get(domain, "unknown")

    else:
        # No keyword match — use majority vote from vector search
        if table_results:
            domains = [
                t.get("schema_name", "unknown")
                for t in table_results
            ]
            domain = Counter(domains).most_common(1)[0][0]

            platform_map_dynamic = {
                t.get("schema_name"): t.get(
                    "source_platform", "unknown"
                ).upper()
                for t in table_results
            }
            platform = platform_map_dynamic.get(domain, "unknown")

    return {
        "domain": domain,
        "platform": platform,
        "tables": table_results,
        "columns": column_results,
        "joins": join_results,
        "glossary": glossary_results,
        "sample_queries": sample_results
    }