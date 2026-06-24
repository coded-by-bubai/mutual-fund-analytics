CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_name TEXT NOT NULL,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date DATE PRIMARY KEY,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER NOT NULL,
    date DATE NOT NULL,
    nav REAL NOT NULL CHECK(nav > 0),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date)
        REFERENCES dim_date(date)
);

CREATE TABLE fact_transactions (
    txn_id INTEGER PRIMARY KEY,
    amfi_code INTEGER NOT NULL,
    date DATE NOT NULL,
    investor_id TEXT,
    transaction_type TEXT,
    amount REAL NOT NULL CHECK(amount > 0),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date)
        REFERENCES dim_date(date)
);

CREATE TABLE fact_performance (
    perf_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER NOT NULL,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER NOT NULL,
    date DATE NOT NULL,
    aum REAL NOT NULL CHECK(aum >= 0),

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date)
        REFERENCES dim_date(date)
);