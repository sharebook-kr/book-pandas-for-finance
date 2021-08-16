from pykrx import stock

df = stock.get_index_kospi_ohlcv_by_date("20000104", "20190609", "코스피")
df["변동폭"] = df["종가"] - df["종가"].shift(1)
print(df["변동폭"].nsmallest(n=5))
