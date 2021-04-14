from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185],
]
columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)

print(df.loc[[0, 1], ["종목코드", "종목명"]])
print(df.iloc[[0, 1], [0, 1]])