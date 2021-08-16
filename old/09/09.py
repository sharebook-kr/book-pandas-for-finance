from pykrx import stock

df = stock.get_index_kospi_ohlcv_by_date("20100601", "20190531", "코스피")
start = df.iloc[0]
end = df.iloc[-1]
수익률 = end.loc["종가"] / start.loc["시가"]
print(수익률)

CAGR = 수익률 ** (1/9) -1
print("CAGR: ", CAGR * 100)