from pandas import DataFrame

data = [
    ['037730', '3R', 1510],
    ['036360', '3SOFT', 1790],
    ['005760', 'ACTS', 1185],
]

labels = ['종목코드', '종목명', '현재가']
df = DataFrame(data, columns=labels)
print(df)