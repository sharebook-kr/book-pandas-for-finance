import requests
import pandas as pd

url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
resp = requests.get(url)
resp.encoding = "utf-8-sig"

data = resp.json()
comp = data['Co']

df = pd.DataFrame(data=comp)
cond = df['gb'] == '701'
df2 = df[cond].copy()
df2.to_excel("comp_code.xlsx")