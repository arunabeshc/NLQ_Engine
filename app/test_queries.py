import requests

NLQ_URL = "https://nlq-service.icyflower-540bf6d4.uksouth.azurecontainerapps.io/nlq"

TEST_CASES = [
    # ─────────────────────────────────────────
    # Snowflake — Source
    # ─────────────────────────────────────────
    {
        "question": "Show me all active customers in the UK region",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me all orders with their payment status",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me the top 5 customers by total order value",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me all trades for high risk counterparties",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me positions with their trade details and market value",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me order lines with product details and discount applied",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "List all available currencies",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me all active instruments and their types",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "What promotions are currently available and what discounts do they offer?",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me all counterparties with a high risk rating and their country",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    {
        "question": "Show me the top 5 products by total revenue across all orders",
        "expected_domain": "source",
        "expected_platform": "SNOWFLAKE"
    },
    # ─────────────────────────────────────────
    # Databricks — Asset Management
    # ─────────────────────────────────────────
    {
        "question": "Show me the top 5 funds by assets under management",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which funds had net outflows last month?",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which funds had net outflows last year?",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which funds have underperformed their benchmark by more than 2% over the past year?",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me funds with an EXTREME redemption pressure flag and their current AUM",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which Article 9 funds have the highest carbon intensity relative to their peer group?",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me the top 5 funds by net inflows from institutional investors last month",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which funds have a Sharpe ratio below 0.5 and AUM above 500 million?",
        "expected_domain": "asset_management",
        "expected_platform": "DATABRICKS"
    },
    # ─────────────────────────────────────────
    # Databricks — Insurance
    # ─────────────────────────────────────────
    {
        "question": "Show me all high risk insurance policies with fraud flags in the last 30 days",
        "expected_domain": "insurance",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me details of the users who have filed claims in the past year",
        "expected_domain": "insurance",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me all policies due for renewal in the next 30 days where the premium has increased by more than 20%",
        "expected_domain": "insurance",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which customers have both a high risk score and a fraud flagged claim in the last 6 months?",
        "expected_domain": "insurance",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me policies with repeated missed payments where the churn risk is above 70%",
        "expected_domain": "insurance",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "What is the average settlement time for claims by claim type?",
        "expected_domain": "insurance",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me all HIGH risk underwriting policies with approved claims above 10000",
        "expected_domain": "insurance",
        "expected_platform": "DATABRICKS"
    },
    # ─────────────────────────────────────────
    # Databricks — Pension
    # ─────────────────────────────────────────
    {
        "question": "Which pension members have exceeded their annual allowance this tax year?",
        "expected_domain": "pension",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me workplace pension schemes with a RED value for money rating",
        "expected_domain": "pension",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which pension members are within 2 years of their selected retirement date but have a fund value below 50000?",
        "expected_domain": "pension",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me disengaged members with a lapse propensity above 80% and a pot size above 100000",
        "expected_domain": "pension",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Which workplace schemes have a RED value for money rating and more than 1000 active members?",
        "expected_domain": "pension",
        "expected_platform": "DATABRICKS"
    },
    {
        "question": "Show me members who chose drawdown at retirement but have a sustainability score below 40",
        "expected_domain": "pension",
        "expected_platform": "DATABRICKS"
    },
]


def check_pass_fail(test_case, response):
    failures = []

    # Check 1 — domain
    if response.get("inferred_domain") != test_case["expected_domain"]:
        failures.append(
            f"Domain mismatch — expected '{test_case['expected_domain']}' "
            f"got '{response.get('inferred_domain')}'"
        )

    # Check 2 — platform
    if response.get("platform") != test_case["expected_platform"]:
        failures.append(
            f"Platform mismatch — expected '{test_case['expected_platform']}' "
            f"got '{response.get('platform')}'"
        )

    # Check 3 — SQL generated
    if response.get("sql") == "UNABLE_TO_GENERATE":
        failures.append("SQL generation failed — UNABLE_TO_GENERATE")

    # Check 4 — syntax valid
    if not response.get("validation", {}).get("syntax_valid"):
        failures.append(
            f"Syntax invalid — {response.get('validation', {}).get('issues', [])}"
        )

    # Check 5 — schema valid
    if not response.get("validation", {}).get("schema_valid"):
        failures.append(
            f"Schema invalid — {response.get('validation', {}).get('issues', [])}"
        )

    # Check 6 — execution succeeded
    if not response.get("execution", {}).get("success"):
        failures.append(
            f"Execution failed — {response.get('execution', {}).get('error', 'unknown error')}"
        )

    return failures


def run_tests():
    print("=" * 60)
    print("NLQ SERVICE — TEST SUITE")
    print("=" * 60)

    passed = 0
    failed = 0
    total = len(TEST_CASES)

    for i, test_case in enumerate(TEST_CASES, 1):
        question = test_case["question"]

        try:
            response = requests.post(
                NLQ_URL,
                json={"question": question},
                timeout=60
            )
            data = response.json()

        except Exception as e:
            print(f"\n[{i}/{total}] FAIL — {question}")
            print(f"  ERROR: Request failed — {str(e)}")
            failed += 1
            continue

        failures = check_pass_fail(test_case, data)

        if not failures:
            print(f"\n[{i}/{total}] PASS — {question}")
            print(f"  Domain   : {data.get('inferred_domain')}")
            print(f"  Platform : {data.get('platform')}")
            print(f"  Rows     : {data.get('execution', {}).get('row_count', 0)}")
            passed += 1
        else:
            print(f"\n[{i}/{total}] FAIL — {question}")
            for failure in failures:
                print(f"  ✗ {failure}")
            failed += 1

    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed / {failed} failed / {total} total")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()