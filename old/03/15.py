from pandas import Series

data1 = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
data2 = data1 * 10
print(data2)
