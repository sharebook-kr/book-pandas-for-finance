from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185],
]
columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)

print(df.loc[0])
print(df.loc[1])
print(df.loc[2])

print(df.iloc[0])
print(df.iloc[-1])
