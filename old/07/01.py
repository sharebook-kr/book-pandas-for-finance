import pybithumb

df = pybithumb.get_ohlcv("BTC", interval="day")
print(df)