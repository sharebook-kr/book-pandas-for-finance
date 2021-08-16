import pybithumb

df = pybithumb.get_ohlcv("BTC", interval="day")
df["변동성"] = (df['high'] - df['low']) * 0.5
df["목표가"] = df["open"] + df["변동성"].shift(1)
print(df)
