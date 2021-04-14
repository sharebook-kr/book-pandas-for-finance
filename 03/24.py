from pandas import Series

data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)

print(s.rank())
#print(s.rank(ascending=False))
