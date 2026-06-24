"""Clean scheme_performance.csv: 
- Validate return values are numeric 
- Flag negative Sharpe ratios 
- Check expense_ratio range (0.1% – 2.5%)"""

import pandas as pd

schema_perf = pd.read_csv('data/raw/07_scheme_performance.csv')

# print(schema_perf.info())
# print(schema_perf.columns)

return_year = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct']

for year in return_year:
    schema_perf[year] = pd.to_numeric(schema_perf[year])
pd.set_option('display.max_columns', 19)

schema_perf["negative_sharpe_flag"] = schema_perf["sharpe_ratio"] < 0
schema_perf['expence_valid'] = schema_perf['expense_ratio_pct'].between(0.1,2.5)
# print(schema_perf.head(2))

schema_perf.to_csv("data/processed/scheme_performance.csv", index=False)