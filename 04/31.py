from pandas import DataFrame
import numpy as np

data = [
    ["037730", "3R", '1,510'],
    ["036360", "3SOFT", '1,790'],
    ["005760", "ACTS", '1,185'],
]

columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
print(df)

# 컴마 제거
def remove_comma(x):
    return x.replace(',', '')

df['현재가'] = df['현재가'].apply(remove_comma)
print(df)
print(df.dtypes)

df = df.astype({'현재가': np.int64})
print(df)
print(df.dtypes)
