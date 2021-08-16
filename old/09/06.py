from pykrx import stock

# PER 0인 종목 필터링
df = stock.get_market_fundamental_by_ticker(date="20100104", market="KOSPI")
cond = df["PER"] != 0
df = df[cond]

# PER이 낮은 n개 종목 선정
low_per = df["PER"].nsmallest(n=2)

# 등락률
fluctuation = stock.get_market_price_change_by_ticker("20100104", "20100129")
df = fluctuation.loc[low_per.index]

# 수익률
ror = 1 + (df['등락률'].sum() / 2 * 0.01)
print(ror)
