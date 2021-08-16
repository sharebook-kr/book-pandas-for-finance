from pykrx import stock
import pandas as pd
from pandas import Series


def run_monthly_low_per(year, month, portfolio_num=5):
    # 거래일
    business_day = stock.get_business_days(year, month)
    start = business_day[0]
    end = business_day[-1]

    # PER 0인 종목 필터링
    df = stock.get_market_fundamental_by_ticker(date=start, market="KOSPI")
    cond = df["PER"] != 0
    df = df[cond]

    # PER이 낮은 n개 종목 선정
    low_per = df["PER"].nsmallest(n=portfolio_num)

    # 등락률
    fluctuation = stock.get_market_price_change_by_ticker(start, end)
    df = fluctuation.loc[low_per.index]

    # 수익률
    ror = 1 + (df['등락률'].mean() * 0.01)
    return ror


index = []
data = []

for year in range(2010, 2019):
    for month in range(1, 13):
        arg = "{}-{:>02}-01".format(year, month)
        date = pd.to_datetime(arg)
        print(date)
        ror = run_monthly_low_per(year, month, portfolio_num=5)

        index.append(date)
        data.append(ror)

s = Series(data=data, index=index)
s.to_excel("ror.xlsx")
print(s.cumprod().iloc[-1])

