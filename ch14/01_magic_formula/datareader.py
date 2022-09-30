from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
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


def get_closing_accounts_day(code):
    url = f"https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{code}"
    selector = "#compBody > div.section.ul_corpinfo > div.corp_group1 > p > span.stxt.stxt3"
    resp = requests.get(url)
    html = resp.text 

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select(selector)
    return tags[0].text


def get_roic(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode=A{code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=104&stkGb=701"
    try:
        dfs = pd.read_html(url)
        df = dfs[0]
        df.set_index(df.columns[0], inplace=True)
        roic = df.filter(regex="^2020").filter(like='ROIC', axis=0).iloc[0, 0]
        roic = float(roic)
    except:
        roic = np.nan
    return roic 


def get_ev_ebitda(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A{code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701"
    try:
        dfs = pd.read_html(url)
        df = dfs[1]
        df.set_index(df.columns[0], inplace=True)
        ev_ebitda = df.filter(like="EV/EBITDA", axis=0).filter(regex="^2020").iloc[0, 0]
        ev_ebitda = float(ev_ebitda)
    except:
        ev_ebitda = np.nan
    return ev_ebitda


if __name__ == "__main__":
    df = get_corp_code()
    
    columns = ['code', 'name', 'day', 'roic', 'ev/ebitda']
    data = []
    for i in range(len(df)):
        s = df.iloc[i]
        acode = s['cd']
        code = acode[1:]
        name = s['nm']

        day = get_closing_accounts_day(code)
        roic = get_roic(code) 
        ev_ebitda = get_ev_ebitda(code) 
        data.append((code, name, day, roic, ev_ebitda))
        print(i, code, name, day, roic, ev_ebitda)

        if (i+1) % 100 == 0:
            df1 = pd.DataFrame(data=data, columns=columns)
            df1.to_excel(f"./data/data_{i+1}.xlsx")
            data = []

        time.sleep(0.5)

    # last companies            
    df1 = pd.DataFrame(data=data, columns=columns)
    df1.to_excel(f"./data/data_last.xlsx")