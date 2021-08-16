from pandas import DataFrame

data = [
    ["3R", 1510],
    ["3SOFT", 1790],
    ["ACTS", 1185],
]
index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가"]

df = DataFrame(data=data, index=index, columns=columns)
print(df)

