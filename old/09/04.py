from pykrx import stock

df = stock.get_market_price_change_by_ticker("20100104", "20100129")
print(df)
#print(df.loc["005880"]["등락률"])
#print(df.loc["009280"]["등락률"])
