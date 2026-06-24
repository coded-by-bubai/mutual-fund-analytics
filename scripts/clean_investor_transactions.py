"""Clean investor_transactions.csv: 
- Standardise transaction_type (SIP/Lumpsum/Redemption) 
- Validate amount > 0 
- Check KYC status values 
- Fix date formats"""

import pandas as pd

inv_trans = pd.read_csv("data/raw/08_investor_transactions.csv")

# print(inv_trans.head(2))
# print(inv_trans.columns)
# print(inv_trans['transaction_type'].unique())

inv_trans['transaction_date'] = pd.to_datetime(inv_trans["transaction_date"])
tx_type = {
    "sip":"SIP",
    "lumpsum":"Lumpsum",
    "redemption":"Redemption",
    "redeem":"Redemption"
}

inv_trans['transaction_type'] = inv_trans["transaction_type"].str.lower().replace(tx_type)

inv_trans = inv_trans[inv_trans['amount_inr'] > 0]

# print(inv_trans['kyc_status'].unique())
valid_kyc_status = [
    "Verified",
    "Pending",
    "Rejected",
    "EXPIRED"
]
inv_trans['kyc_flag'] = inv_trans['kyc_status'].isin(valid_kyc_status)
# print(inv_trans.head(2))

inv_trans.to_csv("data/processed/investor_transactions.csv", index=False)