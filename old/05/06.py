from pykrx import stock

df = stock.get_market_ohlcv_by_date("20190501", "20190531", "005930")
print(df)