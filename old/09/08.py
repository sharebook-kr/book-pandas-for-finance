from pykrx import stock
import pandas as pd
from pandas import Series


def run_annual_pbr_per_combo(year, month=6, portfolio_num=30):
    # 거래일
    business_day = stock.get_business_days(year, month)
    start = business_day[0]
    business_day = stock.get_business_days(year+1, month-1)
    end = business_day[-1]

    # 2.5 <= PER  <= 10
    df = stock.get_market_fundamental_by_ticker(date=start, market="KOSPI")
    cond = (df["PER"] >= 2.5) & (df["PER"] <= 10)           # 괄호 주의
    df = df[cond]

    # PBR이 낮은 30 종목
    low_per = df["PBR"].nsmallest(n=portfolio_num)

    # 등락률
    fluctuation = stock.get_market_price_change_by_ticker(start, end)
    df = fluctuation.loc[low_per.index]

    # 수익률
    ror = 1 + (df['등락률'].mean() * 0.01)
    return ror


# 기본 설정
month = 6
portfolio_num = 30

index = []
data = []

for year in range(2010, 2019):
    arg = "{}-{:>02}-01".format(year, month)
    date = pd.to_datetime(arg)
    print(date)
    ror = run_annual_pbr_per_combo(year, month, portfolio_num)

    index.append(date)
    data.append(ror)

s = Series(data=data, index=index)
s.to_excel("pbr_per_combo.xlsx")
print(s.cumprod().iloc[-1])

