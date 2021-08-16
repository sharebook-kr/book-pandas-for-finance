from pandas import Series

mine = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
wife = Series([10, 30, 20], index=['SKT', 'KT', 'NAVER'])
total = mine + wife
print(total)
