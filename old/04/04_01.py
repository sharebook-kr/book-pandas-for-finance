# 딕셔너리 객체로부터 DataFrame 객체 생성
from pandas import DataFrame

data = {
    '종목코드': ['037730', '036360', '005760'],
    '종목명': ['3R', '3SOFT', 'ACTS'],
    '현재가': [1510, 1790, 1185]
}

df = DataFrame(data)
print(df)