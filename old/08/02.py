from pykrx import stock

df = stock.get_index_kospi_ohlcv_by_date("20000104", "20190609", "코스피")
print(df['종가'].max())
