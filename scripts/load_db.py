import pandas as pd
from sqlalchemy import create_engine, text
import sqlite3

engine = create_engine("sqlite:///bluestock_mf.db") 

df_inv_trans = pd.read_csv('data/processed/investor_transactions.csv')
df_inv_trans.to_sql("fact_transactions", engine, if_exists="replace", index=False)

df_nav_his = pd.read_csv("data/processed/nav_history.csv")
df_nav_his.to_sql("fact_nav", engine, if_exists="replace", index=False)

fact_performance = pd.read_csv("data/processed/scheme_performance.csv")
fact_performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

aum_by_fund_house = pd.read_csv("data/processed/aum_by_fund_house.csv")
aum_by_fund_house.to_sql("aum_by_fund_house", engine, if_exists="replace", index=False)

benchmark_indices = pd.read_csv("data/processed/benchmark_indices.csv")
benchmark_indices.to_sql("benchmark_indices", engine, if_exists="replace", index=False)

category_inflows = pd.read_csv("data/processed/category_inflows.csv")
category_inflows.to_sql("category_inflows", engine, if_exists="replace", index=False)

fund_master = pd.read_csv("data/processed/fund_master.csv")
fund_master.to_sql("fund_master", engine, if_exists="replace", index=False)

industry_folio_count = pd.read_csv("data/processed/industry_folio_count.csv")
industry_folio_count.to_sql("industry_folio_count", engine, if_exists="replace", index=False)

monthly_sip_inflows = pd.read_csv("data/processed/monthly_sip_inflows.csv")
monthly_sip_inflows.to_sql("monthly_sip_inflows", engine, if_exists="replace", index=False)

portfolio_holdings = pd.read_csv("data/processed/portfolio_holdings.csv")
portfolio_holdings.to_sql("portfolio_holdings", engine, if_exists="replace", index=False)


with engine.connect() as conn :
    result = conn.execute(text("SELECT COUNT(*) FROM fact_nav"))
    print(result.scalar(), df_nav_his.shape)

    result = conn.execute(text("SELECT COUNT(*) FROM fact_transactions"))
    print(result.scalar(), df_inv_trans.shape)

    result = conn.execute(text("SELECT COUNT(*) FROM fact_performance"))
    print(result.scalar(), fact_performance.shape)


# Convert to datetime
df_nav_his["date"] = pd.to_datetime(df_nav_his["date"])
df_inv_trans["transaction_date"] = pd.to_datetime(df_inv_trans["transaction_date"])

# Collect unique dates
dates = pd.concat([df_nav_his["date"], df_inv_trans["transaction_date"]]).drop_duplicates().sort_values()

# Create date dimension
dim_date = pd.DataFrame({
    "date": dates
})
dim_date["day"] = dim_date["date"].dt.day
dim_date["month"] = dim_date["date"].dt.month
dim_date["month_name"] = dim_date["date"].dt.month_name()
dim_date["quarter"] = dim_date["date"].dt.quarter
dim_date["year"] = dim_date["date"].dt.year
dim_date["weekday"] = dim_date["date"].dt.day_name()
dim_date["is_weekend"] = dim_date["date"].dt.weekday >= 5
dim_date['date'] = dim_date['date'].dt.strftime('%Y-%m-%d')

print(dim_date.head())
dim_date.to_sql('dim_date', engine, if_exists="replace", index=False)

with open("sql/queries.sql", "r") as f:
    sql_queries = f.read()

queries = [q.strip() for q in sql_queries.split(';') if q.strip()]
conn = sqlite3.connect("bluestock_mf.db")
for query in queries:
    print(query)
    df = pd.read_sql_query(query, conn)
    print(df)