# Index 3 — Join Conditions
# Derived from FK relationships visible in column comments across 16 Databricks tables

JOIN_CONDITIONS = [
    # Asset Management
    {
        "id": "join-fund-master-fund-performance",
        "left_table": "dp_fund_master",
        "right_table": "dp_fund_performance",
        "left_key": "fund_code",
        "right_key": "fund_code",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "asset_management",
        "schema_right": "asset_management",
        "content": "Join dp_fund_master to dp_fund_performance on fund_code to get fund details with daily performance metrics including NAV, returns, volatility and Sharpe ratio."
    },
    {
        "id": "join-fund-master-fund-flows",
        "left_table": "dp_fund_master",
        "right_table": "dp_fund_flows",
        "left_key": "fund_code",
        "right_key": "fund_code",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "asset_management",
        "schema_right": "asset_management",
        "content": "Join dp_fund_master to dp_fund_flows on fund_code to analyse fund inflows, outflows and net flows by investor type, channel and geography."
    },
    {
        "id": "join-fund-master-fund-holdings",
        "left_table": "dp_fund_master",
        "right_table": "dp_fund_holdings",
        "left_key": "fund_code",
        "right_key": "fund_code",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "asset_management",
        "schema_right": "asset_management",
        "content": "Join dp_fund_master to dp_fund_holdings on fund_code to get position-level holdings for each fund including instrument, weight, market value and ESG score."
    },
    {
        "id": "join-fund-master-fund-esg",
        "left_table": "dp_fund_master",
        "right_table": "dp_fund_esg_metrics",
        "left_key": "fund_code",
        "right_key": "fund_code",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "asset_management",
        "schema_right": "asset_management",
        "content": "Join dp_fund_master to dp_fund_esg_metrics on fund_code to get ESG scores, carbon intensity, SFDR classification and stewardship metrics per fund."
    },
    # Insurance
    {
        "id": "join-policy-360-claims",
        "left_table": "dp_policy_360",
        "right_table": "dp_claims",
        "left_key": "policy_id",
        "right_key": "policy_id",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "insurance",
        "schema_right": "insurance",
        "content": "Join dp_policy_360 to dp_claims on policy_id to get all claims associated with a policy including claim type, status, amount and fraud flag."
    },
    {
        "id": "join-policy-360-renewals",
        "left_table": "dp_policy_360",
        "right_table": "dp_policy_renewals",
        "left_key": "policy_id",
        "right_key": "policy_id",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_ONE",
        "schema_left": "insurance",
        "schema_right": "insurance",
        "content": "Join dp_policy_360 to dp_policy_renewals on policy_id to get renewal status, offer premium, churn risk and intervention flags for each policy."
    },
    {
        "id": "join-policy-360-premiums",
        "left_table": "dp_policy_360",
        "right_table": "dp_policy_premiums",
        "left_key": "policy_id",
        "right_key": "policy_id",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "insurance",
        "schema_right": "insurance",
        "content": "Join dp_policy_360 to dp_policy_premiums on policy_id to get premium billing history, payment status and delinquency flags."
    },
    {
        "id": "join-policy-360-underwriting",
        "left_table": "dp_policy_360",
        "right_table": "dp_underwriting_risk",
        "left_key": "policy_id",
        "right_key": "policy_id",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_ONE",
        "schema_left": "insurance",
        "schema_right": "insurance",
        "content": "Join dp_policy_360 to dp_underwriting_risk on policy_id to get risk scores, fraud signals and pricing adjustments for each policy."
    },
    {
        "id": "join-policy-master-policy-360",
        "left_table": "dp_insurance_policy_master",
        "right_table": "dp_policy_360",
        "left_key": "policy_id",
        "right_key": "policy_id",
        "join_type": "INNER",
        "cardinality": "ONE_TO_ONE",
        "schema_left": "insurance",
        "schema_right": "insurance",
        "content": "Join dp_insurance_policy_master to dp_policy_360 on policy_id to reconcile master policy data with the enriched 360 view including risk scores and ML predictions."
    },
    # Pension
    {
        "id": "join-member-360-contributions",
        "left_table": "dp_pension_member_360",
        "right_table": "dp_pension_contributions",
        "left_key": "member_id",
        "right_key": "member_id",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "pension",
        "schema_right": "pension",
        "content": "Join dp_pension_member_360 to dp_pension_contributions on member_id to get full contribution history including employee, employer, AVC and transfer-in payments."
    },
    {
        "id": "join-member-360-engagement",
        "left_table": "dp_pension_member_360",
        "right_table": "dp_pension_engagement",
        "left_key": "member_id",
        "right_key": "member_id",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "pension",
        "schema_right": "pension",
        "content": "Join dp_pension_member_360 to dp_pension_engagement on member_id to get engagement scores, lapse propensity, vulnerability flags and next best action recommendations."
    },
    {
        "id": "join-member-360-retirement-outcomes",
        "left_table": "dp_pension_member_360",
        "right_table": "dp_retirement_outcomes",
        "left_key": "member_id",
        "right_key": "member_id",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_ONE",
        "schema_left": "pension",
        "schema_right": "pension",
        "content": "Join dp_pension_member_360 to dp_retirement_outcomes on member_id to get retirement decisions including annuity, drawdown strategy and sustainability score."
    },
    {
        "id": "join-member-360-scheme-performance",
        "left_table": "dp_pension_member_360",
        "right_table": "dp_workplace_scheme_performance",
        "left_key": "scheme_id",
        "right_key": "scheme_id",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "pension",
        "schema_right": "pension",
        "content": "Join dp_pension_member_360 to dp_workplace_scheme_performance on scheme_id to get scheme-level governance scores, VfM ratings and Consumer Duty status for each member's scheme."
    }
]


# Index 4 — Business Glossary
# Grounded in regulated financial services context of the 16 Databricks tables

BUSINESS_GLOSSARY = [
    # Asset Management terms
    {
        "id": "term-aum",
        "term": "AUM",
        "definition": "Assets Under Management. The total market value of investments managed by a fund on behalf of its investors. A key measure of fund size and commercial scale.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_master, dp_fund_performance",
        "mapped_columns": "aum_gbp, fund_aum_gbp",
        "regulatory_context": "PRIIPs, MiFID II",
        "content": "AUM Assets Under Management total market value investments fund investors size scale dp_fund_master dp_fund_performance aum_gbp"
    },
    {
        "id": "term-nav",
        "term": "NAV",
        "definition": "Net Asset Value. The per-unit value of a fund calculated as total assets minus liabilities divided by units outstanding. Calculated daily for UCITS funds.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_master, dp_fund_performance",
        "mapped_columns": "nav_per_unit_gbp",
        "regulatory_context": "UCITS, PRIIPs KID",
        "content": "NAV Net Asset Value per unit fund daily valuation UCITS PRIIPs dp_fund_master dp_fund_performance nav_per_unit_gbp"
    },
    {
        "id": "term-ocf",
        "term": "OCF",
        "definition": "Ongoing Charges Figure. The annual cost of owning a fund expressed as a percentage of AUM. Includes management fee and operating expenses. Required disclosure under PRIIPs.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_master",
        "mapped_columns": "ocf_pct",
        "regulatory_context": "PRIIPs KID, MiFID II costs and charges",
        "content": "OCF Ongoing Charges Figure annual cost fund percentage AUM management fee PRIIPs MiFID II dp_fund_master ocf_pct"
    },
    {
        "id": "term-net-flows",
        "term": "Net Flows",
        "definition": "The difference between gross subscriptions (inflows) and gross redemptions (outflows) for a fund over a period. Positive net flows indicate more money entering than leaving.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_flows",
        "mapped_columns": "net_flows_gbp, gross_subscriptions_gbp, gross_redemptions_gbp",
        "regulatory_context": "Liquidity stress testing, FCA",
        "content": "Net flows subscriptions redemptions inflows outflows fund liquidity dp_fund_flows net_flows_gbp gross_subscriptions_gbp gross_redemptions_gbp"
    },
    {
        "id": "term-sharpe-ratio",
        "term": "Sharpe Ratio",
        "definition": "A measure of risk-adjusted return. Calculated as excess return over the risk-free rate divided by the standard deviation of returns. Higher is better.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_performance",
        "mapped_columns": "sharpe_ratio_1y",
        "regulatory_context": "MiFID II, Consumer Duty value assessment",
        "content": "Sharpe ratio risk adjusted return excess return standard deviation volatility performance dp_fund_performance sharpe_ratio_1y"
    },
    {
        "id": "term-sfdr",
        "term": "SFDR",
        "definition": "Sustainable Finance Disclosure Regulation. EU regulation requiring fund managers to classify funds as Article 6 (no sustainability focus), Article 8 (ESG promoted) or Article 9 (sustainable investment objective).",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_master, dp_fund_esg_metrics",
        "mapped_columns": "article_classification, sfdr_classification",
        "regulatory_context": "SFDR, EU Taxonomy",
        "content": "SFDR Sustainable Finance Disclosure Regulation Article 6 8 9 ESG sustainable investment fund classification dp_fund_master dp_fund_esg_metrics"
    },
    {
        "id": "term-tracking-error",
        "term": "Tracking Error",
        "definition": "The standard deviation of the difference between a fund's returns and its benchmark returns. Measures how closely a fund follows its benchmark. Low for index funds, higher for active funds.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_performance",
        "mapped_columns": "tracking_error_1y",
        "regulatory_context": "MiFID II, PRIIPs",
        "content": "Tracking error benchmark deviation active passive index fund performance dp_fund_performance tracking_error_1y"
    },
    {
        "id": "term-redemption-pressure",
        "term": "Redemption Pressure",
        "definition": "The level of investor redemption activity relative to fund liquidity. Flagged as NONE, ELEVATED, HIGH or EXTREME. HIGH or EXTREME may trigger liquidity management tools.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_flows",
        "mapped_columns": "redemption_pressure_flag",
        "regulatory_context": "FCA liquidity stress testing, AIFMD",
        "content": "Redemption pressure liquidity stress investor outflows flag ELEVATED HIGH EXTREME fund management dp_fund_flows redemption_pressure_flag"
    },
    # Insurance terms
    {
        "id": "term-loss-ratio",
        "term": "Loss Ratio",
        "definition": "Claims paid divided by premiums earned expressed as a percentage. A loss ratio above 100% means the insurer pays out more in claims than it collects in premiums.",
        "domain": "insurance",
        "mapped_tables": "dp_claims, dp_policy_premiums",
        "mapped_columns": "claim_amount_gbp, approved_amount_gbp, premium_amount_gbp",
        "regulatory_context": "Solvency II, PRA",
        "content": "Loss ratio claims paid premiums earned percentage profitability underwriting insurance dp_claims dp_policy_premiums claim_amount_gbp premium_amount_gbp"
    },
    {
        "id": "term-ncd",
        "term": "NCD",
        "definition": "No Claims Discount. A discount applied to insurance premiums for policyholders who have not made any claims. Rewards low-risk behaviour and incentivises retention.",
        "domain": "insurance",
        "mapped_tables": "dp_policy_360",
        "mapped_columns": "no_claims_discount_pct",
        "regulatory_context": "FCA pricing practices",
        "content": "NCD No Claims Discount premium reduction policyholder claims-free retention dp_policy_360 no_claims_discount_pct"
    },
    {
        "id": "term-churn-risk",
        "term": "Churn Risk",
        "definition": "The predicted probability that a policyholder will not renew their policy at the next renewal date. Derived from ML model using payment history, premium changes and engagement signals.",
        "domain": "insurance",
        "mapped_tables": "dp_policy_360, dp_policy_renewals",
        "mapped_columns": "lapse_risk_pct, churn_risk_pct",
        "regulatory_context": "FCA Consumer Duty",
        "content": "Churn risk lapse renewal probability ML prediction retention policyholder dp_policy_360 dp_policy_renewals lapse_risk_pct churn_risk_pct"
    },
    {
        "id": "term-fraud-flag",
        "term": "Fraud Flag",
        "definition": "A boolean indicator set by the fraud detection model when a claim exhibits characteristics associated with fraudulent behaviour. Flagged claims are routed to the Special Investigations Unit.",
        "domain": "insurance",
        "mapped_tables": "dp_claims, dp_underwriting_risk",
        "mapped_columns": "fraud_flag, fraud_risk_flag",
        "regulatory_context": "FCA, Insurance Fraud Bureau",
        "content": "Fraud flag suspicious claim detection model SIU investigation insurance dp_claims dp_underwriting_risk fraud_flag fraud_risk_flag"
    },
    {
        "id": "term-srri",
        "term": "SRRI",
        "definition": "Synthetic Risk and Reward Indicator. A 1-7 scale measuring the risk and potential return of a fund. Required disclosure on UCITS Key Investor Information Documents.",
        "domain": "insurance",
        "mapped_tables": "dp_fund_master",
        "mapped_columns": "risk_rating",
        "regulatory_context": "UCITS KIID, PRIIPs",
        "content": "SRRI Synthetic Risk Reward Indicator 1-7 scale fund risk UCITS KIID PRIIPs dp_fund_master risk_rating"
    },
    # Pension terms
    {
        "id": "term-annual-allowance",
        "term": "Annual Allowance",
        "definition": "The maximum amount that can be contributed to a pension in a tax year while still receiving tax relief. Currently £60,000 for most individuals. Excess contributions are subject to a tax charge.",
        "domain": "pension",
        "mapped_tables": "dp_pension_contributions",
        "mapped_columns": "annual_allowance_used, carry_forward_used",
        "regulatory_context": "HMRC, Finance Act",
        "content": "Annual allowance pension contribution limit £60000 tax relief HMRC carry forward dp_pension_contributions annual_allowance_used carry_forward_used"
    },
    {
        "id": "term-drawdown",
        "term": "Drawdown",
        "definition": "A flexible retirement income option where the pension pot remains invested and the member withdraws income directly from the fund. The pot can rise or fall depending on investment performance.",
        "domain": "pension",
        "mapped_tables": "dp_retirement_outcomes",
        "mapped_columns": "drawdown_initial_invest, annual_drawdown_amount, drawdown_strategy",
        "regulatory_context": "FCA Retirement Outcomes Review, Pension Freedoms",
        "content": "Drawdown flexible retirement income pension pot invested withdrawal strategy FCA Pension Freedoms dp_retirement_outcomes drawdown_initial_invest annual_drawdown_amount"
    },
    {
        "id": "term-consumer-duty",
        "term": "Consumer Duty",
        "definition": "FCA regulation requiring firms to deliver good outcomes for retail customers across four outcome areas: products and services, price and value, consumer understanding, and consumer support.",
        "domain": "pension",
        "mapped_tables": "dp_pension_engagement, dp_workplace_scheme_performance",
        "mapped_columns": "consumer_duty_outcome_rating, consumer_duty_status",
        "regulatory_context": "FCA Consumer Duty PS22/9",
        "content": "Consumer Duty FCA good outcomes retail customers products services price value understanding support dp_pension_engagement dp_workplace_scheme_performance"
    },
    {
        "id": "term-vfm",
        "term": "Value for Money",
        "definition": "An assessment framework requiring workplace pension schemes to demonstrate they deliver good value relative to costs. Schemes rated RED must take remedial action. Part of FCA and TPR joint supervisory agenda.",
        "domain": "pension",
        "mapped_tables": "dp_workplace_scheme_performance",
        "mapped_columns": "value_for_money_rating",
        "regulatory_context": "FCA, TPR, DWP Value for Money framework",
        "content": "Value for Money VfM workplace pension scheme assessment GREEN AMBER RED remedial FCA TPR DWP dp_workplace_scheme_performance value_for_money_rating"
    },
    {
        "id": "term-vulnerability",
        "term": "Vulnerable Customer",
        "definition": "A customer who due to their personal circumstances is especially susceptible to harm. FCA guidance identifies four drivers: health, life events, resilience and capability. Firms must treat vulnerable customers fairly.",
        "domain": "pension",
        "mapped_tables": "dp_pension_engagement",
        "mapped_columns": "vulnerability_flag, vulnerability_drivers",
        "regulatory_context": "FCA FG21/1 Guidance on Vulnerable Customers",
        "content": "Vulnerable customer FCA health life events resilience capability flag fair treatment dp_pension_engagement vulnerability_flag vulnerability_drivers"
    },
    {
        "id": "term-pcls",
        "term": "PCLS",
        "definition": "Pension Commencement Lump Sum. The tax-free cash entitlement available when a member first takes benefits from their pension. Typically 25% of the pension pot up to the Lump Sum Allowance.",
        "domain": "pension",
        "mapped_tables": "dp_retirement_outcomes",
        "mapped_columns": "tax_free_cash_taken",
        "regulatory_context": "HMRC, Finance Act 2004",
        "content": "PCLS Pension Commencement Lump Sum tax free cash 25% retirement benefits dp_retirement_outcomes tax_free_cash_taken"
    },
]


# Index 5 — Sample Queries
# Representative NL questions and SQL grounded in the 16 Databricks tables

SAMPLE_QUERIES = [
    # Asset Management
    {
        "id": "query-001",
        "natural_language": "Show me all funds with a 1-year return above 10% and an OCF below 0.5%",
        "sql": """
            SELECT
                m.fund_name,
                m.fund_code,
                m.asset_class,
                p.return_1y_pct,
                m.ocf_pct
            FROM dp_fund_performance p
            INNER JOIN dp_fund_master m ON p.fund_code = m.fund_code
            WHERE p.return_1y_pct > 10
              AND m.ocf_pct < 0.005
              AND p.valuation_date = (SELECT MAX(valuation_date) FROM dp_fund_performance)
            ORDER BY p.return_1y_pct DESC
        """,
        "tables_used": "dp_fund_performance, dp_fund_master",
        "schema_name": "asset_management",
        "domain": "asset_management",
        "complexity": "MEDIUM",
        "content": "funds 1 year return above 10% OCF below 0.5% performance charges filter sort"
    },
    {
        "id": "query-002",
        "natural_language": "Which funds had net outflows last month?",
        "sql": """
            SELECT
                m.fund_name,
                f.fund_code,
                f.flow_month,
                SUM(f.net_flows_gbp) AS total_net_flows_gbp
            FROM dp_fund_flows f
            INNER JOIN dp_fund_master m ON f.fund_code = m.fund_code
            WHERE f.flow_month = TO_CHAR(DATEADD(month, -1, CURRENT_DATE()), 'YYYY-MM')
            GROUP BY m.fund_name, f.fund_code, f.flow_month
            HAVING SUM(f.net_flows_gbp) < 0
            ORDER BY total_net_flows_gbp ASC
        """,
        "tables_used": "dp_fund_flows, dp_fund_master",
        "schema_name": "asset_management",
        "domain": "asset_management",
        "complexity": "MEDIUM",
        "content": "funds net outflows last month redemptions subscriptions negative flows"
    },
    {
        "id": "query-003",
        "natural_language": "Show me the carbon intensity of all Article 9 funds",
        "sql": """
            SELECT
                m.fund_name,
                m.fund_code,
                m.article_classification,
                e.portfolio_carbon_intensity,
                e.carbon_footprint_tco2e,
                e.snapshot_date
            FROM dp_fund_esg_metrics e
            INNER JOIN dp_fund_master m ON e.fund_code = m.fund_code
            WHERE m.article_classification = 'Article 9'
              AND e.snapshot_date = (SELECT MAX(snapshot_date) FROM dp_fund_esg_metrics)
            ORDER BY e.portfolio_carbon_intensity ASC
        """,
        "tables_used": "dp_fund_esg_metrics, dp_fund_master",
        "schema_name": "asset_management",
        "domain": "asset_management",
        "complexity": "MEDIUM",
        "content": "carbon intensity Article 9 SFDR sustainable funds ESG emissions tCO2e"
    },
    {
        "id": "query-004",
        "natural_language": "What are the top 10 holdings by weight across all equity funds?",
        "sql": """
            SELECT
                h.instrument_name,
                h.isin,
                h.sector,
                h.country_of_risk,
                SUM(h.market_value_gbp) AS total_market_value_gbp,
                AVG(h.weight_pct) AS avg_weight_pct
            FROM dp_fund_holdings h
            INNER JOIN dp_fund_master m ON h.fund_code = m.fund_code
            WHERE m.asset_class = 'EQUITY'
              AND h.holding_date = (SELECT MAX(holding_date) FROM dp_fund_holdings)
            GROUP BY h.instrument_name, h.isin, h.sector, h.country_of_risk
            ORDER BY total_market_value_gbp DESC
            LIMIT 10
        """,
        "tables_used": "dp_fund_holdings, dp_fund_master",
        "schema_name": "asset_management",
        "domain": "asset_management",
        "complexity": "MEDIUM",
        "content": "top holdings weight equity funds instruments positions market value sector country"
    },
    {
        "id": "query-005",
        "natural_language": "Which funds have elevated or high redemption pressure today?",
        "sql": """
            SELECT
                m.fund_name,
                f.fund_code,
                f.flow_date,
                f.redemption_pressure_flag,
                f.net_flows_gbp,
                f.flow_vs_aum_pct
            FROM dp_fund_flows f
            INNER JOIN dp_fund_master m ON f.fund_code = m.fund_code
            WHERE f.flow_date = CURRENT_DATE()
              AND f.redemption_pressure_flag IN ('ELEVATED', 'HIGH', 'EXTREME')
            ORDER BY f.flow_date DESC
        """,
        "tables_used": "dp_fund_flows, dp_fund_master",
        "schema_name": "asset_management",
        "domain": "asset_management",
        "complexity": "SIMPLE",
        "content": "redemption pressure elevated high extreme liquidity risk fund flows today"
    },
    # Insurance
    {
        "id": "query-006",
        "natural_language": "Show me all high risk policies with fraud flags in the last 30 days",
        "sql": """
            SELECT
                p.policy_id,
                p.customer_id,
                p.product_type,
                p.risk_band,
                c.claim_id,
                c.claim_date,
                c.claim_amount_gbp,
                c.fraud_flag
            FROM dp_policy_360 p
            INNER JOIN dp_claims c ON p.policy_id = c.policy_id
            WHERE p.risk_band = 'HIGH'
              AND c.fraud_flag = TRUE
              AND c.claim_date >= DATEADD(day, -30, CURRENT_DATE())
            ORDER BY c.claim_date DESC
        """,
        "tables_used": "dp_policy_360, dp_claims",
        "schema_name": "insurance",
        "domain": "insurance",
        "complexity": "MEDIUM",
        "content": "high risk policies fraud flags claims last 30 days suspicious investigation"
    },
    {
        "id": "query-007",
        "natural_language": "What is the average settlement time for motor claims?",
        "sql": """
            SELECT
                c.claim_type,
                AVG(c.settlement_time_days) AS avg_settlement_days,
                MIN(c.settlement_time_days) AS min_days,
                MAX(c.settlement_time_days) AS max_days,
                COUNT(*) AS total_claims
            FROM dp_claims c
            WHERE c.claim_type = 'ACCIDENT'
              AND c.claim_status = 'SETTLED'
            GROUP BY c.claim_type
        """,
        "tables_used": "dp_claims",
        "schema_name": "insurance",
        "domain": "insurance",
        "complexity": "SIMPLE",
        "content": "average settlement time motor claims days resolved accident"
    },
    {
        "id": "query-008",
        "natural_language": "Which policies are due for renewal in the next 30 days with high churn risk?",
        "sql": """
            SELECT
                r.policy_id,
                r.customer_id,
                r.renewal_due_date,
                r.churn_risk_pct,
                r.renewal_offer_premium_gbp,
                r.last_year_premium_gbp,
                r.premium_change_pct,
                p.product_type,
                p.risk_band
            FROM dp_policy_renewals r
            INNER JOIN dp_policy_360 p ON r.policy_id = p.policy_id
            WHERE r.renewal_due_date BETWEEN CURRENT_DATE() AND DATEADD(day, 30, CURRENT_DATE())
              AND r.churn_risk_pct > 0.7
              AND r.renewal_status = 'PENDING'
            ORDER BY r.churn_risk_pct DESC
        """,
        "tables_used": "dp_policy_renewals, dp_policy_360",
        "schema_name": "insurance",
        "domain": "insurance",
        "complexity": "MEDIUM",
        "content": "renewal due next 30 days high churn risk lapse pending retention intervention"
    },
    {
        "id": "query-009",
        "natural_language": "Show me policies with repeated missed payments in the last 6 months",
        "sql": """
            SELECT
                pp.policy_id,
                pp.customer_id,
                COUNT(*) AS missed_payment_count,
                SUM(pp.premium_amount_gbp) AS total_missed_gbp,
                p.product_type,
                p.policy_status
            FROM dp_policy_premiums pp
            INNER JOIN dp_policy_360 p ON pp.policy_id = p.policy_id
            WHERE pp.payment_status = 'MISSED'
              AND pp.is_repeated_miss = TRUE
              AND pp.due_date >= DATEADD(month, -6, CURRENT_DATE())
            GROUP BY pp.policy_id, pp.customer_id, p.product_type, p.policy_status
            ORDER BY missed_payment_count DESC
        """,
        "tables_used": "dp_policy_premiums, dp_policy_360",
        "schema_name": "insurance",
        "domain": "insurance",
        "complexity": "MEDIUM",
        "content": "repeated missed payments last 6 months delinquency premium billing policy"
    },
    # Pension
    {
        "id": "query-010",
        "natural_language": "Show me members with vulnerability flags who have not logged in for 90 days",
        "sql": """
            SELECT
                m.member_id,
                m.member_first_name,
                m.member_last_name,
                m.age,
                m.fund_value_gbp,
                e.vulnerability_flag,
                e.vulnerability_drivers,
                e.engagement_score,
                e.next_best_action
            FROM dp_pension_member_360 m
            INNER JOIN dp_pension_engagement e ON m.member_id = e.member_id
            WHERE e.vulnerability_flag = TRUE
              AND m.digital_engaged = FALSE
            ORDER BY m.fund_value_gbp DESC
        """,
        "tables_used": "dp_pension_member_360, dp_pension_engagement",
        "schema_name": "pension",
        "domain": "pension",
        "complexity": "MEDIUM",
        "content": "vulnerable members not logged in 90 days disengaged FCA flag next best action"
    },
    {
        "id": "query-011",
        "natural_language": "Which members have exceeded their annual allowance this tax year?",
        "sql": """
            SELECT
                c.member_id,
                m.member_first_name,
                m.member_last_name,
                SUM(c.annual_allowance_used) AS total_allowance_used,
                SUM(c.carry_forward_used) AS carry_forward_used,
                c.tax_year
            FROM dp_pension_contributions c
            INNER JOIN dp_pension_member_360 m ON c.member_id = m.member_id
            WHERE c.tax_year = '2024-25'
            GROUP BY c.member_id, m.member_first_name, m.member_last_name, c.tax_year
            HAVING SUM(c.annual_allowance_used) > 60000
            ORDER BY total_allowance_used DESC
        """,
        "tables_used": "dp_pension_contributions, dp_pension_member_360",
        "schema_name": "pension",
        "domain": "pension",
        "complexity": "MEDIUM",
        "content": "annual allowance exceeded £60000 tax year contributions HMRC pension member"
    },
    {
        "id": "query-012",
        "natural_language": "Show me workplace schemes with a RED value for money rating",
        "sql": """
            SELECT
                scheme_id,
                scheme_name,
                employer_name,
                total_active_members,
                total_aua_gbp,
                value_for_money_rating,
                consumer_duty_status,
                governance_score,
                review_due_date
            FROM dp_workplace_scheme_performance
            WHERE value_for_money_rating = 'RED'
            ORDER BY total_aua_gbp DESC
        """,
        "tables_used": "dp_workplace_scheme_performance",
        "schema_name": "pension",
        "domain": "pension",
        "complexity": "SIMPLE",
        "content": "RED value for money rating workplace scheme remediation governance Consumer Duty"
    },
    {
        "id": "query-013",
        "natural_language": "What percentage of members chose drawdown over annuity at retirement?",
        "sql": """
            SELECT
                retirement_option,
                COUNT(*) AS member_count,
                ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct_of_total,
                AVG(pot_size_at_decision) AS avg_pot_size_gbp,
                AVG(age_at_decision) AS avg_age
            FROM dp_retirement_outcomes
            GROUP BY retirement_option
            ORDER BY member_count DESC
        """,
        "tables_used": "dp_retirement_outcomes",
        "schema_name": "pension",
        "domain": "pension",
        "complexity": "MEDIUM",
        "content": "drawdown annuity retirement option percentage members pot size age decision"
    },
    {
        "id": "query-014",
        "natural_language": "Show me members with high lapse propensity and large pot sizes",
        "sql": """
            SELECT
                m.member_id,
                m.member_first_name,
                m.member_last_name,
                m.fund_value_gbp,
                m.age,
                m.selected_retirement_dt,
                e.likely_to_lapse_pct,
                e.engagement_band,
                e.next_best_action
            FROM dp_pension_member_360 m
            INNER JOIN dp_pension_engagement e ON m.member_id = e.member_id
            WHERE e.likely_to_lapse_pct > 0.6
              AND m.fund_value_gbp > 100000
            ORDER BY m.fund_value_gbp DESC
        """,
        "tables_used": "dp_pension_member_360, dp_pension_engagement",
        "schema_name": "pension",
        "domain": "pension",
        "complexity": "MEDIUM",
        "content": "high lapse propensity large pot size retention at risk members engagement"
    },
    {
        "id": "query-015",
        "natural_language": "Show total employer and employee contributions by scheme this tax year",
        "sql": """
            SELECT
                c.scheme_id,
                s.scheme_name,
                s.employer_name,
                c.tax_year,
                SUM(CASE WHEN c.contribution_type = 'EMPLOYEE' THEN c.gross_amount_gbp ELSE 0 END) AS total_employee_gbp,
                SUM(CASE WHEN c.contribution_type = 'EMPLOYER' THEN c.gross_amount_gbp ELSE 0 END) AS total_employer_gbp,
                COUNT(DISTINCT c.member_id) AS contributing_members
            FROM dp_pension_contributions c
            INNER JOIN dp_workplace_scheme_performance s ON c.scheme_id = s.scheme_id
            WHERE c.tax_year = '2024-25'
            GROUP BY c.scheme_id, s.scheme_name, s.employer_name, c.tax_year
            ORDER BY total_employer_gbp DESC
        """,
        "tables_used": "dp_pension_contributions, dp_workplace_scheme_performance",
        "schema_name": "pension",
        "domain": "pension",
        "complexity": "COMPLEX",
        "content": "employer employee contributions scheme tax year total breakdown HMRC payroll"
    }
]