from pykrx import stock

df = stock.get_market_ohlcv_by_date("20190501", "20190531", "005930")
df['5일이동평균'] = df['종가'].rolling(window=5).mean()
print(df)

