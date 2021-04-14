from pykrx import stock

df = stock.get_market_fundamental_by_ticker(date="20100104", market="KOSPI")
print(df)