from pandas import Series

data = [1000, 2000, 3000]
s = Series(data=data)

print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])
