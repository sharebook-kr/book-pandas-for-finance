import pandas as pd
from pandas import DataFrame

data = [
    [9450, 9490, 9160, 9220, 145794],
    [9380, 9570, 9330, 9490, 57571],
    [9220, 9400, 9100, 9380, 131427],
    [9200, 9250, 9030, 9230, 66893],
    [9350, 9600, 9070, 9200, 138861]
]

columns = ["시가", "고가", "저가", "종가", "거래량"]
index = ["2019-06-07", "2019-06-05", "2019-06-04", "2019-06-03", "2019-05-31"]
df = DataFrame(data=data, index=pd.to_datetime(index), columns=columns)
print(df)
print(df['2019-06'])