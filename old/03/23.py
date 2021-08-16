from pandas import Series

data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
print(s)

# 정렬 (오름차순)
s1 = s.sort_values()
print(s1)

# 정렬 (내림차순)
s2 = s.sort_values(ascending=False)
print(s2)