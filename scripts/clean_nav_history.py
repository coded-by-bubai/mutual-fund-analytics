"""
Clean nav_history.csv: - Parse dates
to datetime - Sort by amfi_code + date
- Forward-fill missing NAV (holidays) -
Remove duplicates - Validate NAV > 0
"""

import pandas as pd
nav_his = pd.read_csv('data/raw/02_nav_history.csv')
nav_his['date'] = pd.to_datetime(nav_his['date'])

nav_his = nav_his.sort_values(['amfi_code','date'])

nav_his['nav'] = nav_his.groupby('amfi_code')['nav'].ffill()
nav_his = nav_his.drop_duplicates()
nav_his = nav_his[nav_his['nav'] >0]
nav_his.to_csv("data/processed/nav_history.csv", index=False)
assert nav_his['nav'].min() > 0