from pykrx import stock

df = stock.get_market_ohlcv_by_date("20190527", "20190531", "006800")

cond = df["종가"] > df["시가"]
print(df[cond])
