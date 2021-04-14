from pandas import Series

close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = Series(data=open, index=index)
close = Series(data=close, index=index)
diff = close - open

cond = close > open
print(diff[cond])
