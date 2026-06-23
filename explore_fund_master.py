import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
# print(fund_master.columns)

print("\n","-"*30,"explore fund master","-"*30)
print("\nUnique fund house")
print(fund_master['fund_house'].unique())
print("\ncategory")
print(fund_master['category'].unique())
print("\nsubcategory")
print(fund_master['sub_category'].unique())
print("\nrisk grade")
print(fund_master['risk_category'].unique())
print("AMFI scheme code")
print(fund_master[['amfi_code','fund_house','scheme_name']])

print("-"*30, "Validate AMFI Codes", "-"*30)
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
# print(nav_history.columns)

master_code = set(fund_master['amfi_code'])
his_code = set(nav_history['amfi_code'])
missing_code = master_code - his_code
matched_code = master_code & his_code

print(f"Total Fund Master Codes: {len(master_code)}")
print(f"Total NAV History Codes: {len(his_code)}")
print(f"Matched Codes: {len(matched_code)}")
print(f"Missing Codes: {len(missing_code)}")
if (len(master_code) == len(master_code)):
    print("\nAll AMFI scheme codes in fund_master exist in nav_history.")