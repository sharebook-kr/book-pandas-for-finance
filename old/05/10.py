from pykrx import stock

df = stock.get_market_ohlcv_by_date("20190501", "20190531", "005930")
df["전날거래량"] = df["거래량"].shift(1)
cond = df["거래량"] > df["전날거래량"]
df = df[cond]
print(df)

