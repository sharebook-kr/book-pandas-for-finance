from pandas import Series

data = [1000, 2000, 3000]
s = Series(data=data)

print(s.loc[0])
print(s.loc[1])
print(s.loc[2])
print(s.loc[-1])
