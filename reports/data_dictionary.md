Data Dictionary


**Database:** `bluestock_mf.db`

**Storage Format:** CSV → SQLite

---

# Dataset 1: fund_master.csv

**Description:** Master information for all mutual fund schemes.

| Column             | Data Type | Description                          | 
| ------------------ | --------- | ------------------------------------ | 
| amfi_code          | INTEGER   | Unique AMFI scheme code              |
| fund_house         | TEXT      | Asset Management Company (AMC)       |
| scheme_name        | TEXT      | Name of mutual fund scheme           |
| category           | TEXT      | Main category (Equity, Debt, Hybrid) |
| sub_category       | TEXT      | Scheme classification                |
| plan               | TEXT      | Direct or Regular Plan               |
| launch_date        | DATE      | Scheme launch date                   |
| benchmark          | TEXT      | Benchmark index                      |
| expense_ratio_pct  | REAL      | Annual expense ratio (%)             |
| exit_load_pct      | REAL      | Exit load percentage                 |
| min_sip_amount     | INTEGER   | Minimum SIP investment (₹)           |
| min_lumpsum_amount | INTEGER   | Minimum lump sum investment (₹)      |
| fund_manager       | TEXT      | Fund manager name                    |
| risk_category      | TEXT      | Risk category                        |
| sebi_category_code | TEXT      | SEBI category code                   |

---

# Dataset 2: nav_history.csv

**Description:** Daily Net Asset Value (NAV) history of each scheme.

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- | 
| amfi_code | INTEGER   | Scheme identifier |
| date      | DATE      | NAV date          | 
| nav       | REAL      | Net Asset Value   | 

---

# Dataset 3: investor_transactions.csv

**Description:** Investor transaction records.

| Column             | Data Type | Description                    |
| ------------------ | --------- | ------------------------------ |
| investor_id        | TEXT      | Unique investor ID             |
| transaction_date   | DATE      | Date of transaction            |
| amfi_code          | INTEGER   | Mutual fund scheme code        |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption       |
| amount_inr         | INTEGER   | Transaction amount (₹)         |
| state              | TEXT      | Investor state                 |
| city               | TEXT      | Investor city                  |
| city_tier          | TEXT      | Tier-1, Tier-2, Tier-3         |
| age_group          | TEXT      | Investor age group             |
| gender             | TEXT      | Gender                         |
| annual_income_lakh | REAL      | Annual income (₹ lakh)         |
| payment_mode       | TEXT      | UPI, Net Banking, Cheque, etc. |
| kyc_status         | TEXT      | Verified, Pending, Rejected    |
| kyc_flag           | BOOLEAN   | KYC verification status        |

---

# Dataset 4: scheme_performance.csv

**Description:** Historical performance metrics for mutual fund schemes.

| Column               | Data Type | Description                       |
| -------------------- | --------- | --------------------------------- | 
| amfi_code            | INTEGER   | Scheme code                       |
| scheme_name          | TEXT      | Scheme name                       |
| fund_house           | TEXT      | Asset Management Company          |
| category             | TEXT      | Fund category                     |
| plan                 | TEXT      | Direct/Regular                    |
| return_1yr_pct       | REAL      | One-year return (%)               |
| return_3yr_pct       | REAL      | Three-year CAGR (%)               |
| return_5yr_pct       | REAL      | Five-year CAGR (%)                |
| benchmark_3yr_pct    | REAL      | Benchmark 3-year return (%)       |
| alpha                | REAL      | Alpha value                       |
| beta                 | REAL      | Beta value                        |
| sharpe_ratio         | REAL      | Sharpe Ratio                      |
| sortino_ratio        | REAL      | Sortino Ratio                     |
| std_dev_ann_pct      | REAL      | Annualized standard deviation     |
| max_drawdown_pct     | REAL      | Maximum drawdown (%)              |
| aum_crore            | INTEGER   | Assets Under Management (₹ crore) |
| expense_ratio_pct    | REAL      | Expense ratio (%)                 |
| morningstar_rating   | INTEGER   | Morningstar rating (1–5)          |
| risk_grade           | TEXT      | Risk grade                        |
| negative_sharpe_flag | BOOLEAN   | Indicates negative Sharpe ratio   |
| expence_valid        | BOOLEAN   | Expense ratio validation flag     |

---

# Dataset 5: portfolio_holdings.csv

**Description:** Equity portfolio holdings for each scheme.

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ | 
| amfi_code         | INTEGER   | Scheme code              |
| stock_symbol      | TEXT      | NSE/BSE stock symbol     |
| stock_name        | TEXT      | Company name             |
| sector            | TEXT      | Industry sector          |
| weight_pct        | REAL      | Portfolio allocation (%) |
| market_value_cr   | REAL      | Market value (₹ crore)   |
| current_price_inr | REAL      | Current stock price      |
| portfolio_date    | DATE      | Portfolio reporting date |

---

# Dataset 6: aum_by_fund_house.csv

**Description:** AUM statistics by fund house.

| Column         | Data Type | Description        |
| -------------- | --------- | ------------------ |
| date           | DATE      | Reporting date     |
| fund_house     | TEXT      | AMC name           |
| aum_lakh_crore | REAL      | AUM (₹ lakh crore) |
| aum_crore      | INTEGER   | AUM (₹ crore)      |
| num_schemes    | INTEGER   | Number of schemes  |

---

# Dataset 7: monthly_sip_inflows.csv

**Description:** Monthly SIP industry statistics.

| Column                    | Data Type | Description                  |
| ------------------------- | --------- | ---------------------------- |
| month                     | TEXT      | Reporting month              |
| sip_inflow_crore          | INTEGER   | Monthly SIP inflow (₹ crore) |
| active_sip_accounts_crore | REAL      | Active SIP accounts (crore)  |
| new_sip_accounts_lakh     | REAL      | Newly registered SIPs (lakh) |
| sip_aum_lakh_crore        | REAL      | SIP AUM (₹ lakh crore)       |
| yoy_growth_pct            | REAL      | Year-over-year growth (%)    |

---

# Dataset 8: category_inflows.csv

**Description:** Monthly net inflows by mutual fund category.

| Column           | Data Type | Description          | 
| ---------------- | --------- | -------------------- | 
| month            | TEXT      | Reporting month      |
| category         | TEXT      | Fund category        |
| net_inflow_crore | REAL      | Net inflow (₹ crore) |

---

# Dataset 9: benchmark_indices.csv

**Description:** Benchmark index closing values.

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | DATE      | Trading date         |
| index_name  | TEXT      | Benchmark index name |
| close_value | REAL      | Closing index value  |

---

# Dataset 10: industry_folio_count.csv

**Description:** Industry-wide mutual fund folio statistics.

| Column              | Data Type | Description           |
| ------------------- | --------- | --------------------- |
| month               | TEXT      | Reporting month       |
| total_folios_crore  | REAL      | Total folios (crore)  |
| equity_folios_crore | REAL      | Equity folios         |
| debt_folios_crore   | REAL      | Debt folios           |
| hybrid_folios_crore | REAL      | Hybrid folios         |
| others_folios_crore | REAL      | Other category folios |

---

# Business Definitions

| Term             | Definition                                    |
| ---------------- | --------------------------------------------- |
| NAV              | Net Asset Value per mutual fund unit          |
| AUM              | Assets Under Management                       |
| SIP              | Systematic Investment Plan                    |
| Lumpsum          | One-time investment                           |
| Redemption       | Sale of mutual fund units                     |
| AMFI Code        | Unique identifier for each mutual fund scheme |
| Expense Ratio    | Annual management fee charged by the AMC      |
| Alpha            | Excess return relative to benchmark           |
| Beta             | Volatility compared to benchmark              |
| Sharpe Ratio     | Risk-adjusted return measure                  |
| Sortino Ratio    | Downside risk-adjusted return measure         |
| Maximum Drawdown | Largest peak-to-trough decline                |
| CAGR             | Compound Annual Growth Rate                   |
| Benchmark        | Market index used for comparison              |
| KYC              | Know Your Customer verification               |

---

# Data Quality Rules

| Column            | Validation Rule             |
| ----------------- | --------------------------- |
| amfi_code         | Must exist in fund_master   |
| nav               | Greater than 0              |
| amount_inr        | Greater than 0              |
| expense_ratio_pct | Between 0.1 and 2.5         |
| transaction_type  | SIP, Lumpsum, Redemption    |
| kyc_status        | Verified, Pending, Rejected |
| return values     | Numeric                     |
| date columns      | Valid date format           |
| fund_house        | Cannot be NULL              |
| scheme_name       | Cannot be NULL              |
| benchmark         | Cannot be NULL              |

---

# Primary Keys

| Dataset               | Primary Key                                |
| --------------------- | ------------------------------------------ |
| fund_master           | amfi_code                                  |
| nav_history           | amfi_code + date                           |
| investor_transactions | investor_id + transaction_date + amfi_code |
| scheme_performance    | amfi_code                                  |
| portfolio_holdings    | amfi_code + stock_symbol                   |
| aum_by_fund_house     | fund_house + date                          |
| monthly_sip_inflows   | month                                      |
| category_inflows      | month + category                           |
| benchmark_indices     | date + index_name                          |
| industry_folio_count  | month                                      |

---

# Relationships

* `fund_master.amfi_code` → `nav_history.amfi_code`
* `fund_master.amfi_code` → `investor_transactions.amfi_code`
* `fund_master.amfi_code` → `scheme_performance.amfi_code`
* `fund_master.amfi_code` → `portfolio_holdings.amfi_code`
* `benchmark_indices` is used to compare scheme performance against market indices.
* `category_inflows`, `monthly_sip_inflows`, `industry_folio_count`, and `aum_by_fund_house` provide industry-level analytics and trends.
