from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185],
]

columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
df = df.set_index('종목코드')

# 현재가를 기준으로 순위
df['순위'] = df['현재가'].rank()
print(df)

