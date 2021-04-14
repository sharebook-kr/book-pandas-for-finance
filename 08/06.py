from pykrx import stock

df = stock.get_index_kospi_ohlcv_by_date("20000104", "20181231", "코스피")
start = df.iloc[0]
end = df.iloc[-1]
수익률 = end.loc["종가"] / start.loc["시가"]
print(수익률)

