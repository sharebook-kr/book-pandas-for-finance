from pykrx import stock

samsung_df = stock.get_market_ohlcv_by_date("20180101", "20190531", "005930")
lge_df = stock.get_market_ohlcv_by_date("20180101", "20190531", "066570")

print(samsung_df.head())
print(lge_df.head())
