import pybithumb

df = pybithumb.get_ohlcv("BTC", interval="day")
df["변동성"] = (df['high'] - df['low']) * 0.5
print(df.head())
