from pykrx import stock

# PER 0인 종목 필터링
df = stock.get_market_fundamental_by_ticker(date="20100104", market="KOSPI")
cond = df["PER"] != 0
df = df[cond]

# PER이 낮은 n개 종목 선정
low_per = df["PER"].nsmallest(n=2)
print(low_per)
