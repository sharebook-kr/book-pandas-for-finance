from pykrx import stock

business_day = stock.get_business_days(2010, 1)
print(business_day[0])
print(business_day[-1])

