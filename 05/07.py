from pykrx import stock

df = stock.get_market_ohlcv_by_date("20190527", "20190531", "006800")
print(df)
print(df.loc["20190531"]["종가"])