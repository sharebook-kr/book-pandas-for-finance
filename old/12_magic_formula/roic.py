import requests
import re 
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_corp_code():
    url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
    resp = requests.get(url)
    resp.encoding = "utf-8-sig"
    data = resp.json()
    comp = data['Co']
    df = pd.DataFrame(data=comp)
    cond = df['gb'] == '701'
    df2 = df[cond].copy()
    return df2


def get_encparam(code="005930"):
    re_enc = re.compile("encparam: '(.*)'", re.IGNORECASE) 
    re_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)
    url = f"http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd={code}" 
    html = requests.get(url).text 
    encparam = re_enc.search(html).group(1) 
    encid = re_id.search(html).group(1)
    return encparam, encid


def get_data(code, encparam, rpt, item): 
    headers = {
        "Host": "navercomp.wisereport.co.kr",
        "Referer": f"https://navercomp.wisereport.co.kr/v2/company/c1040001.aspx?cmp_cd={code}",
        "User-Agent": "Mozilla/5.0"
    }

    params = {
        "cmp_cd": f"{code}",
        "frq" : "0",
        "rpt": rpt,
        "finGubun": "MAIN",
        "frqTyp": "0",
        "encparam": encparam
    }

    url = "https://navercomp.wisereport.co.kr/v2/company/cF4002.aspx"
    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()

    for x in data['DATA']:
        if x['ACC_NM'] == item:
            result = x['DATA5']
            return result 


if __name__ == "__main__":
    df = get_corp_code()

    data = []
    for i in range(len(df)):
        s = df.iloc[i]
        acode = s['cd']
        code = acode[1:]
        name = s['nm']

        encparam, encid = get_encparam(code)
        roic = get_data(code, encparam, "1", "ROIC")
        ev_ebitda = get_data(code, encparam, "5", "EV/EBITDA")
        data.append((code, name, roic, ev_ebitda))
        print(i, code, name, roic, ev_ebitda)

        if (i+1) % 100 == 0:
            df1 = pd.DataFrame(data=data, columns=['code', 'name', 'roic', 'ev/ebitda'])
            df1.to_excel(f"data_{i+1}.xlsx")
            data = []

        time.sleep(0.5)

    # last companies            
    df1 = pd.DataFrame(data=data, columns=['code', 'name', 'roic', 'ev/ebitda'])
    df1.to_excel(f"data_last.xlsx")
