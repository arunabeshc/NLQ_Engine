# Index 3 — Join Conditions

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
    },
    # Source — Snowflake
    {
        "id": "join-src-orders-src-customers",
        "left_table": "src_orders",
        "right_table": "src_customers",
        "left_key": "CUSTOMER_ID",
        "right_key": "CUSTOMER_ID",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_orders to src_customers on CUSTOMER_ID to get customer name, region and status for each order."
    },
    {
        "id": "join-src-orders-src-order-lines",
        "left_table": "src_orders",
        "right_table": "src_order_lines",
        "left_key": "ORDER_ID",
        "right_key": "ORDER_ID",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_orders to src_order_lines on ORDER_ID to get line item details for each order including product, quantity and line amount."
    },
    {
        "id": "join-src-orders-src-payments",
        "left_table": "src_orders",
        "right_table": "src_payments",
        "left_key": "ORDER_ID",
        "right_key": "ORDER_ID",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_MANY",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_orders to src_payments on ORDER_ID to get payment amount and status for each order."
    },
    {
        "id": "join-src-order-lines-src-products",
        "left_table": "src_order_lines",
        "right_table": "src_products",
        "left_key": "PRODUCT_ID",
        "right_key": "PRODUCT_ID",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_order_lines to src_products on PRODUCT_ID to get product name, category and price for each order line."
    },
    {
        "id": "join-src-orders-small-src-customers",
        "left_table": "src_orders_small",
        "right_table": "src_customers",
        "left_key": "CUSTOMER_ID",
        "right_key": "CUSTOMER_ID",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_orders_small to src_customers on CUSTOMER_ID to get customer name and region for each small order."
    },
    {
        "id": "join-src-orders-small-ref-promotion",
        "left_table": "src_orders_small",
        "right_table": "ref_promotion",
        "left_key": "PROMO_CODE",
        "right_key": "PROMO_CODE",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_orders_small to ref_promotion on PROMO_CODE to get discount percentage applied to each order."
    },
    {
        "id": "join-src-customers-ref-region",
        "left_table": "src_customers",
        "right_table": "ref_region",
        "left_key": "REGION_CODE",
        "right_key": "REGION_CODE",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_customers to ref_region on REGION_CODE to get region name for each customer."
    },
    {
        "id": "join-src-counterparty-ref-country",
        "left_table": "src_counterparty",
        "right_table": "ref_country",
        "left_key": "COUNTRY_CD",
        "right_key": "COUNTRY_CD",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_counterparty to ref_country on COUNTRY_CD to get country name and region for each counterparty."
    },
    {
        "id": "join-src-trades-src-counterparty",
        "left_table": "src_trades",
        "right_table": "src_counterparty",
        "left_key": "COUNTERPARTYID",
        "right_key": "COUNTERPARTYID",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_trades to src_counterparty on COUNTERPARTYID to get counterparty type, risk rating and country for each trade."
    },
    {
        "id": "join-src-trades-ref-instrument",
        "left_table": "src_trades",
        "right_table": "ref_instrument",
        "left_key": "INSTRUMENTID",
        "right_key": "INSTRUMENT_CD",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_trades to ref_instrument on INSTRUMENTID to INSTRUMENT_CD to get instrument description and type for each trade."
    },
    {
        "id": "join-src-trades-ref-currency",
        "left_table": "src_trades",
        "right_table": "ref_currency",
        "left_key": "CURRENCYCODE",
        "right_key": "CURRENCY_CODE",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_trades to ref_currency on CURRENCYCODE to CURRENCY_CODE to get currency name for each trade."
    },
    {
        "id": "join-src-positions-src-trades",
        "left_table": "src_positions",
        "right_table": "src_trades",
        "left_key": "TRADEID",
        "right_key": "TRADEID",
        "join_type": "LEFT",
        "cardinality": "ONE_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_positions to src_trades on TRADEID to get trade details for each position including instrument, quantity, price and counterparty."
    },
    {
        "id": "join-src-orders-ref-currency",
        "left_table": "src_orders",
        "right_table": "ref_currency",
        "left_key": "CURRENCY_CODE",
        "right_key": "CURRENCY_CODE",
        "join_type": "LEFT",
        "cardinality": "MANY_TO_ONE",
        "schema_left": "source",
        "schema_right": "source",
        "content": "Join src_orders to ref_currency on CURRENCY_CODE to get currency name for each order."
    },
]


# Index 4 — Business Glossary

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
        "definition": "Sustainable Finance Disclosure Regulation. EU regulation requiring fund managers to classify funds as Article 6, Article 8 or Article 9.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_master, dp_fund_esg_metrics",
        "mapped_columns": "article_classification, sfdr_classification",
        "regulatory_context": "SFDR, EU Taxonomy",
        "content": "SFDR Sustainable Finance Disclosure Regulation Article 6 8 9 ESG sustainable investment fund classification dp_fund_master dp_fund_esg_metrics"
    },
    {
        "id": "term-tracking-error",
        "term": "Tracking Error",
        "definition": "The standard deviation of the difference between a fund's returns and its benchmark returns. Low for index funds, higher for active funds.",
        "domain": "asset_management",
        "mapped_tables": "dp_fund_performance",
        "mapped_columns": "tracking_error_1y",
        "regulatory_context": "MiFID II, PRIIPs",
        "content": "Tracking error benchmark deviation active passive index fund performance dp_fund_performance tracking_error_1y"
    },
    {
        "id": "term-redemption-pressure",
        "term": "Redemption Pressure",
        "definition": "The level of investor redemption activity relative to fund liquidity. Flagged as NONE, ELEVATED, HIGH or EXTREME.",
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
        "definition": "No Claims Discount. A discount applied to insurance premiums for policyholders who have not made any claims.",
        "domain": "insurance",
        "mapped_tables": "dp_policy_360",
        "mapped_columns": "no_claims_discount_pct",
        "regulatory_context": "FCA pricing practices",
        "content": "NCD No Claims Discount premium reduction policyholder claims-free retention dp_policy_360 no_claims_discount_pct"
    },
    {
        "id": "term-churn-risk",
        "term": "Churn Risk",
        "definition": "The predicted probability that a policyholder will not renew their policy at the next renewal date.",
        "domain": "insurance",
        "mapped_tables": "dp_policy_360, dp_policy_renewals",
        "mapped_columns": "lapse_risk_pct, churn_risk_pct",
        "regulatory_context": "FCA Consumer Duty",
        "content": "Churn risk lapse renewal probability ML prediction retention policyholder dp_policy_360 dp_policy_renewals lapse_risk_pct churn_risk_pct"
    },
    {
        "id": "term-fraud-flag",
        "term": "Fraud Flag",
        "definition": "A boolean indicator set by the fraud detection model when a claim exhibits characteristics associated with fraudulent behaviour.",
        "domain": "insurance",
        "mapped_tables": "dp_claims, dp_underwriting_risk",
        "mapped_columns": "fraud_flag, fraud_risk_flag",
        "regulatory_context": "FCA, Insurance Fraud Bureau",
        "content": "Fraud flag suspicious claim detection model SIU investigation insurance dp_claims dp_underwriting_risk fraud_flag fraud_risk_flag"
    },
    {
        "id": "term-srri",
        "term": "SRRI",
        "definition": "Synthetic Risk and Reward Indicator. A 1-7 scale measuring the risk and potential return of a fund.",
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
        "definition": "The maximum amount that can be contributed to a pension in a tax year while still receiving tax relief. Currently £60,000 for most individuals.",
        "domain": "pension",
        "mapped_tables": "dp_pension_contributions",
        "mapped_columns": "annual_allowance_used, carry_forward_used",
        "regulatory_context": "HMRC, Finance Act",
        "content": "Annual allowance pension contribution limit £60000 tax relief HMRC carry forward dp_pension_contributions annual_allowance_used carry_forward_used"
    },
    {
        "id": "term-drawdown",
        "term": "Drawdown",
        "definition": "A flexible retirement income option where the pension pot remains invested and the member withdraws income directly from the fund.",
        "domain": "pension",
        "mapped_tables": "dp_retirement_outcomes",
        "mapped_columns": "drawdown_initial_invest, annual_drawdown_amount, drawdown_strategy",
        "regulatory_context": "FCA Retirement Outcomes Review, Pension Freedoms",
        "content": "Drawdown flexible retirement income pension pot invested withdrawal strategy FCA Pension Freedoms dp_retirement_outcomes drawdown_initial_invest annual_drawdown_amount"
    },
    {
        "id": "term-consumer-duty",
        "term": "Consumer Duty",
        "definition": "FCA regulation requiring firms to deliver good outcomes for retail customers across four outcome areas.",
        "domain": "pension",
        "mapped_tables": "dp_pension_engagement, dp_workplace_scheme_performance",
        "mapped_columns": "consumer_duty_outcome_rating, consumer_duty_status",
        "regulatory_context": "FCA Consumer Duty PS22/9",
        "content": "Consumer Duty FCA good outcomes retail customers products services price value understanding support dp_pension_engagement dp_workplace_scheme_performance"
    },
    {
        "id": "term-vfm",
        "term": "Value for Money",
        "definition": "An assessment framework requiring workplace pension schemes to demonstrate they deliver good value relative to costs. Schemes rated RED must take remedial action.",
        "domain": "pension",
        "mapped_tables": "dp_workplace_scheme_performance",
        "mapped_columns": "value_for_money_rating",
        "regulatory_context": "FCA, TPR, DWP Value for Money framework",
        "content": "Value for Money VfM workplace pension scheme assessment GREEN AMBER RED remedial FCA TPR DWP dp_workplace_scheme_performance value_for_money_rating"
    },
    {
        "id": "term-vulnerability",
        "term": "Vulnerable Customer",
        "definition": "A customer who due to their personal circumstances is especially susceptible to harm. FCA guidance identifies four drivers: health, life events, resilience and capability.",
        "domain": "pension",
        "mapped_tables": "dp_pension_engagement",
        "mapped_columns": "vulnerability_flag, vulnerability_drivers",
        "regulatory_context": "FCA FG21/1 Guidance on Vulnerable Customers",
        "content": "Vulnerable customer FCA health life events resilience capability flag fair treatment dp_pension_engagement vulnerability_flag vulnerability_drivers"
    },
    {
        "id": "term-pcls",
        "term": "PCLS",
        "definition": "Pension Commencement Lump Sum. The tax-free cash entitlement available when a member first takes benefits from their pension. Typically 25% of the pension pot.",
        "domain": "pension",
        "mapped_tables": "dp_retirement_outcomes",
        "mapped_columns": "tax_free_cash_taken",
        "regulatory_context": "HMRC, Finance Act 2004",
        "content": "PCLS Pension Commencement Lump Sum tax free cash 25% retirement benefits dp_retirement_outcomes tax_free_cash_taken"
    },
    # Source — Snowflake terms
    {
        "id": "term-customer",
        "term": "Customer",
        "definition": "A customer is an individual or organisation that places orders. Customer data is stored in src_customers in the source schema on Snowflake. Contains customer ID, name, region and status.",
        "domain": "source",
        "mapped_tables": "src_customers",
        "mapped_columns": "CUSTOMER_ID, CUSTOMER_NAME, REGION_CODE, STATUS",
        "regulatory_context": "",
        "content": "customer order buyer src_customers source snowflake CUSTOMER_ID CUSTOMER_NAME region status"
    },
    {
        "id": "term-order",
        "term": "Order",
        "definition": "An order represents a purchase transaction placed by a customer. Order data is stored in src_orders and src_order_lines in the source schema on Snowflake.",
        "domain": "source",
        "mapped_tables": "src_orders, src_order_lines",
        "mapped_columns": "ORDER_ID, CUSTOMER_ID, ORDER_DATE, STATUS, CURRENCY_CODE",
        "regulatory_context": "",
        "content": "order purchase transaction customer src_orders src_order_lines source snowflake ORDER_ID CUSTOMER_ID ORDER_DATE"
    },
    {
        "id": "term-order-value",
        "term": "Order Value",
        "definition": "The total monetary value of an order calculated from line items. Derived from LINE_AMOUNT in src_order_lines joined to src_orders on ORDER_ID.",
        "domain": "source",
        "mapped_tables": "src_orders, src_order_lines",
        "mapped_columns": "LINE_AMOUNT, ORDER_ID",
        "regulatory_context": "",
        "content": "order value total amount line items src_order_lines src_orders source snowflake LINE_AMOUNT ORDER_ID"
    },
    {
        "id": "term-trade",
        "term": "Trade",
        "definition": "A trade represents a buy or sell transaction of a financial instrument. Trade data is stored in src_trades in the source schema on Snowflake. Contains trade ID, instrument, quantity, price, currency and counterparty.",
        "domain": "source",
        "mapped_tables": "src_trades",
        "mapped_columns": "TRADEID, INSTRUMENTID, BUYSELL, QUANTITY, PRICE, CURRENCYCODE, COUNTERPARTYID",
        "regulatory_context": "",
        "content": "trade buy sell instrument quantity price currency counterparty src_trades source snowflake TRADEID INSTRUMENTID BUYSELL"
    },
    {
        "id": "term-position",
        "term": "Position",
        "definition": "A position represents the current holding of a financial instrument derived from a trade. Position data is stored in src_positions in the source schema on Snowflake. Contains market value, PnL and quantity.",
        "domain": "source",
        "mapped_tables": "src_positions",
        "mapped_columns": "POSITIONID, TRADEID, QUANTITY, MARKETVALUE, PNL, PRICE",
        "regulatory_context": "",
        "content": "position holding instrument market value PnL quantity trade src_positions source snowflake POSITIONID TRADEID MARKETVALUE PNL"
    },
    {
        "id": "term-counterparty",
        "term": "Counterparty",
        "definition": "A counterparty is the other party in a financial trade transaction. Counterparty data is stored in src_counterparty in the source schema on Snowflake. Contains counterparty type, risk rating and country.",
        "domain": "source",
        "mapped_tables": "src_counterparty",
        "mapped_columns": "COUNTERPARTYID, COUNTERPARTYTYPE, COUNTRY_CD, RISKRATING, STATUS",
        "regulatory_context": "",
        "content": "counterparty trade transaction risk rating country type src_counterparty source snowflake COUNTERPARTYID RISKRATING"
    },
    {
        "id": "term-payment",
        "term": "Payment",
        "definition": "A payment represents a financial settlement against an order. Payment data is stored in src_payments in the source schema on Snowflake. Contains payment ID, order ID, amount and payment status.",
        "domain": "source",
        "mapped_tables": "src_payments",
        "mapped_columns": "PAYMENT_ID, ORDER_ID, AMOUNT, PAYMENT_STATUS",
        "regulatory_context": "",
        "content": "payment settlement order amount status src_payments source snowflake PAYMENT_ID ORDER_ID AMOUNT PAYMENT_STATUS"
    },
    {
        "id": "term-product",
        "term": "Product",
        "definition": "A product is an item available for purchase. Product data is stored in src_products in the source schema on Snowflake. Contains product ID, name, category and price.",
        "domain": "source",
        "mapped_tables": "src_products",
        "mapped_columns": "PRODUCT_ID, PRODUCT_NAME, CATEGORY, PRICE",
        "regulatory_context": "",
        "content": "product item purchase category price src_products source snowflake PRODUCT_ID PRODUCT_NAME CATEGORY PRICE"
    },
    {
        "id": "term-instrument",
        "term": "Instrument",
        "definition": "A financial instrument is a tradeable asset. Instrument reference data is stored in ref_instrument in the source schema on Snowflake. Contains instrument code, description and type.",
        "domain": "source",
        "mapped_tables": "ref_instrument",
        "mapped_columns": "INSTRUMENT_CD, INSTRUMENT_DESC, INSTRUMENT_TYPE, IS_ACTIVE",
        "regulatory_context": "",
        "content": "instrument financial asset tradeable ref_instrument source snowflake INSTRUMENT_CD INSTRUMENT_DESC INSTRUMENT_TYPE"
    },
    {
        "id": "term-promotion",
        "term": "Promotion",
        "definition": "A promotion is a discount applied to an order. Promotion data is stored in ref_promotion in the source schema on Snowflake. Contains promo code and discount percentage.",
        "domain": "source",
        "mapped_tables": "ref_promotion",
        "mapped_columns": "PROMO_CODE, DISCOUNT_PCT",
        "regulatory_context": "",
        "content": "promotion discount promo code order ref_promotion source snowflake PROMO_CODE DISCOUNT_PCT"
    },
]


# Index 5 — Sample Queries

SAMPLE_QUERIES = [
    # Asset Management
    {
        "id": "query-001",
        "natural_language": "Show me all funds with a 1-year return above 10% and an OCF below 0.5%",
        "sql": """
            SELECT m.fund_name, m.fund_code, m.asset_class, p.return_1y_pct, m.ocf_pct
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
            SELECT m.fund_name, f.fund_code, f.flow_month, SUM(f.net_flows_gbp) AS total_net_flows_gbp
            FROM dp_fund_flows f
            INNER JOIN dp_fund_master m ON f.fund_code = m.fund_code
            WHERE f.flow_month = DATE_FORMAT(ADD_MONTHS(CURRENT_DATE(), -1), 'yyyy-MM')
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
            SELECT m.fund_name, m.fund_code, m.article_classification, e.portfolio_carbon_intensity, e.snapshot_date
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
            SELECT h.instrument_name, h.isin, h.sector, SUM(h.market_value_gbp) AS total_market_value_gbp, AVG(h.weight_pct) AS avg_weight_pct
            FROM dp_fund_holdings h
            INNER JOIN dp_fund_master m ON h.fund_code = m.fund_code
            WHERE m.asset_class = 'EQUITY'
              AND h.holding_date = (SELECT MAX(holding_date) FROM dp_fund_holdings)
            GROUP BY h.instrument_name, h.isin, h.sector
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
            SELECT m.fund_name, f.fund_code, f.flow_date, f.redemption_pressure_flag, f.net_flows_gbp
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
            SELECT p.policy_id, p.customer_id, p.product_type, p.risk_band, c.claim_id, c.claim_date, c.fraud_flag
            FROM dp_policy_360 p
            INNER JOIN dp_claims c ON p.policy_id = c.policy_id
            WHERE p.risk_band = 'HIGH'
              AND c.fraud_flag = TRUE
              AND c.claim_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
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
        "natural_language": "What is the average settlement time for accident claims?",
        "sql": """
            SELECT c.claim_type, AVG(c.settlement_time_days) AS avg_settlement_days, COUNT(*) AS total_claims
            FROM dp_claims c
            WHERE c.claim_type = 'ACCIDENT' AND c.claim_status = 'SETTLED'
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
            SELECT r.policy_id, r.renewal_due_date, r.churn_risk_pct, r.renewal_offer_premium_gbp, p.product_type
            FROM dp_policy_renewals r
            INNER JOIN dp_policy_360 p ON r.policy_id = p.policy_id
            WHERE r.renewal_due_date BETWEEN CURRENT_DATE() AND DATE_ADD(CURRENT_DATE(), INTERVAL 30 DAY)
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
            SELECT pp.policy_id, pp.customer_id, COUNT(*) AS missed_payment_count, p.product_type
            FROM dp_policy_premiums pp
            INNER JOIN dp_policy_360 p ON pp.policy_id = p.policy_id
            WHERE pp.payment_status = 'MISSED'
              AND pp.is_repeated_miss = TRUE
              AND pp.due_date >= ADD_MONTHS(CURRENT_DATE(), -6)
            GROUP BY pp.policy_id, pp.customer_id, p.product_type
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
            SELECT m.member_id, m.member_first_name, m.member_last_name, m.fund_value_gbp,
                   e.vulnerability_flag, e.engagement_score, e.next_best_action
            FROM dp_pension_member_360 m
            INNER JOIN dp_pension_engagement e ON m.member_id = e.member_id
            WHERE e.vulnerability_flag = TRUE AND m.digital_engaged = FALSE
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
            SELECT c.member_id, m.member_first_name, m.member_last_name,
                   SUM(c.annual_allowance_used) AS total_allowance_used, c.tax_year
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
            SELECT scheme_id, scheme_name, employer_name, total_active_members,
                   total_aua_gbp, value_for_money_rating, consumer_duty_status
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
            SELECT retirement_option, COUNT(*) AS member_count,
                   ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct_of_total,
                   AVG(pot_size_at_decision) AS avg_pot_size_gbp
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
            SELECT m.member_id, m.member_first_name, m.fund_value_gbp,
                   e.likely_to_lapse_pct, e.engagement_band, e.next_best_action
            FROM dp_pension_member_360 m
            INNER JOIN dp_pension_engagement e ON m.member_id = e.member_id
            WHERE e.likely_to_lapse_pct > 0.6 AND m.fund_value_gbp > 100000
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
            SELECT c.scheme_id, s.scheme_name, s.employer_name, c.tax_year,
                   SUM(CASE WHEN c.contribution_type = 'EMPLOYEE' THEN c.gross_amount_gbp ELSE 0 END) AS total_employee_gbp,
                   SUM(CASE WHEN c.contribution_type = 'EMPLOYER' THEN c.gross_amount_gbp ELSE 0 END) AS total_employer_gbp
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
    },
    # Source — Snowflake
    {
        "id": "query-016",
        "natural_language": "Show me the top 5 customers by total order value",
        "sql": """
            SELECT c.CUSTOMER_ID, c.CUSTOMER_NAME, c.REGION_CODE,
                   SUM(ol.LINE_AMOUNT) AS total_order_value
            FROM AI_TOOL_DB.source.src_customers c
            INNER JOIN AI_TOOL_DB.source.src_orders o ON c.CUSTOMER_ID = o.CUSTOMER_ID
            INNER JOIN AI_TOOL_DB.source.src_order_lines ol ON o.ORDER_ID = ol.ORDER_ID
            GROUP BY c.CUSTOMER_ID, c.CUSTOMER_NAME, c.REGION_CODE
            ORDER BY total_order_value DESC
            LIMIT 5
        """,
        "tables_used": "src_customers, src_orders, src_order_lines",
        "schema_name": "source",
        "domain": "source",
        "complexity": "MEDIUM",
        "content": "top customers total order value purchase amount src_customers src_orders src_order_lines snowflake"
    },
    {
        "id": "query-017",
        "natural_language": "Show me all active customers in the UK region",
        "sql": """
            SELECT c.CUSTOMER_ID, c.CUSTOMER_NAME, c.REGION_CODE, c.STATUS
            FROM AI_TOOL_DB.source.src_customers c
            INNER JOIN AI_TOOL_DB.source.ref_region r ON c.REGION_CODE = r.REGION_CODE
            WHERE c.STATUS = 'ACTIVE' AND r.REGION_NAME = 'United Kingdom'
            LIMIT 5
        """,
        "tables_used": "src_customers, ref_region",
        "schema_name": "source",
        "domain": "source",
        "complexity": "SIMPLE",
        "content": "active customers UK region status src_customers ref_region snowflake"
    },
    {
        "id": "query-018",
        "natural_language": "Show me all trades for high risk counterparties",
        "sql": """
            SELECT t.TRADEID, t.TRADEDATE, t.INSTRUMENTID, t.BUYSELL,
                   t.QUANTITY, t.PRICE, t.CURRENCYCODE, cp.COUNTERPARTYTYPE, cp.RISKRATING
            FROM AI_TOOL_DB.source.src_trades t
            INNER JOIN AI_TOOL_DB.source.src_counterparty cp ON t.COUNTERPARTYID = cp.COUNTERPARTYID
            WHERE cp.RISKRATING = 'HIGH'
            ORDER BY t.TRADEDATE DESC
            LIMIT 5
        """,
        "tables_used": "src_trades, src_counterparty",
        "schema_name": "source",
        "domain": "source",
        "complexity": "MEDIUM",
        "content": "trades high risk counterparties rating instrument buy sell src_trades src_counterparty snowflake"
    },
    {
        "id": "query-019",
        "natural_language": "Show me all orders with their payment status",
        "sql": """
            SELECT o.ORDER_ID, o.CUSTOMER_ID, o.ORDER_DATE, o.STATUS,
                   p.AMOUNT, p.PAYMENT_STATUS
            FROM AI_TOOL_DB.source.src_orders o
            LEFT JOIN AI_TOOL_DB.source.src_payments p ON o.ORDER_ID = p.ORDER_ID
            ORDER BY o.ORDER_DATE DESC
            LIMIT 5
        """,
        "tables_used": "src_orders, src_payments",
        "schema_name": "source",
        "domain": "source",
        "complexity": "SIMPLE",
        "content": "orders payment status amount src_orders src_payments snowflake"
    },
    {
        "id": "query-020",
        "natural_language": "Show me positions with their trade details and market value",
        "sql": """
            SELECT pos.POSITIONID, pos.ASOFDATE, pos.QUANTITY, pos.MARKETVALUE,
                   pos.PNL, t.INSTRUMENTID, t.BUYSELL, t.PRICE
            FROM AI_TOOL_DB.source.src_positions pos
            LEFT JOIN AI_TOOL_DB.source.src_trades t ON pos.TRADEID = t.TRADEID
            ORDER BY pos.MARKETVALUE DESC
            LIMIT 5
        """,
        "tables_used": "src_positions, src_trades",
        "schema_name": "source",
        "domain": "source",
        "complexity": "MEDIUM",
        "content": "positions market value PnL trade instrument src_positions src_trades snowflake"
    },
    {
        "id": "query-021",
        "natural_language": "Show me order lines with product details and discount applied",
        "sql": """
            SELECT ol.LINE_ID, ol.ORDER_ID, p.PRODUCT_NAME, p.CATEGORY,
                   ol.QTY, ol.LINE_AMOUNT, pr.DISCOUNT_PCT
            FROM AI_TOOL_DB.source.src_order_lines ol
            INNER JOIN AI_TOOL_DB.source.src_products p ON ol.PRODUCT_ID = p.PRODUCT_ID
            LEFT JOIN AI_TOOL_DB.source.src_orders_small os ON ol.ORDER_ID = os.ORDER_ID
            LEFT JOIN AI_TOOL_DB.source.ref_promotion pr ON os.PROMO_CODE = pr.PROMO_CODE
            ORDER BY ol.LINE_AMOUNT DESC
            LIMIT 5
        """,
        "tables_used": "src_order_lines, src_products, src_orders_small, ref_promotion",
        "schema_name": "source",
        "domain": "source",
        "complexity": "COMPLEX",
        "content": "order lines product details discount promotion quantity amount src_order_lines src_products ref_promotion snowflake"
    },
]