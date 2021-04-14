import pybithumb

df = pybithumb.get_ohlcv("XRP", interval="day")
print(df)