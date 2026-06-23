import requests
import pandas as pd

schemes = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}
# url = "https://api.mfapi.in/mf/125497"
# response = requests.get(url)

# data = response.json()
# nav_df = pd.DataFrame(data['data'])

# nav_df.to_csv('data/raw/hdfc_top100_nav.csv', index=False)

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    data = requests.get(url).json()
    df = pd.DataFrame(data['data'])
    df.to_csv(f'data/raw/{name}_nav.csv', index=False)
