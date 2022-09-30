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


def get_gpa(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A{code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701"

    try: 
        dfs = pd.read_html(url)

        # gross profit
        df = dfs[0]
        df2 = df.set_index(df.columns[0])
        gp = df2.filter(regex="^2020").loc["매출총이익"].values[0]
        gp = float(gp) * 100000000

        # asset 
        df3 = dfs[2]
        df4 = df3.set_index(df3.columns[0])
        asset = df4.filter(regex="^2020").loc["자산"].values[0]
        asset = float(asset) * 100000000
        result = gp / asset
    except:
        result = np.nan

    return result


def get_cap(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701"
    try:
        dfs = pd.read_html(url)
        cap = float(dfs[0].iloc[4, 1]) 
        cap = cap * 100000000 
    except:
        cap = np.nan
    return cap

 
def get_pbr(code):
    url = f"https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{code}"
    try:
        dfs = pd.read_html(url)
        df5 = dfs[10]
        df6 = df5.set_index(df5.columns[0])
        pbr = df6["Annual"].filter(regex="^2020").loc["PBR"].values[0]
    except:
        pbr = 0
    return pbr


if __name__ == "__main__":
    df = get_corp_code()
    
    columns = ['code', 'name', 'day', 'gp/a', 'pbr', 'cap']
    data = []
    for i in range(len(df)):
        s = df.iloc[i]
        acode = s['cd']
        code = acode[1:]
        name = s['nm']

        day = get_closing_accounts_day(code)
        gpa = get_gpa(code) 
        pbr = get_pbr(code) 
        cap = get_cap(code)

        data.append((code, name, day, gpa, pbr, cap))
        print(i, code, name, day, gpa, pbr, cap)

        if (i+1) % 100 == 0:
            df1 = pd.DataFrame(data=data, columns=columns)
            df1.to_excel(f"./data/data_{i+1}.xlsx")
            data = []

        time.sleep(0.3)

    # last companies            
    df1 = pd.DataFrame(data=data, columns=columns)
    df1.to_excel(f"./data/data_last.xlsx")