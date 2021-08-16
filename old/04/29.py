from pandas import DataFrame
import pandas as pd

# 첫번째 데이터프레임
data = {
    '종가':   [113000, 111500],
    '거래량': [555850, 282163]
}
index = ['2019-06-21', '2019-06-20']
df1 = DataFrame(data=data, index=index)

# 두번째 데이터프레임
data = {
    '종가':   [110000, 109000],
    '거래량': [483689, 791946]
}
index = ['2019-06-19', '2019-06-18']
df2 = DataFrame(data=data, index=index)

df = pd.concat([df1, df2])
print(df)
