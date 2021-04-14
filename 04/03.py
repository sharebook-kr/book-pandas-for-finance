from pandas import DataFrame

data = [
    {"종목코드": "037730", "종목명": "3R", "현재가": 1510},
    {"종목코드": "036360", "종목명": "3SOFT", "현재가": 1790},
    {"종목코드": "005760", "종목명": "ACTS", "현재가": 1185},
]

df = DataFrame(data=data)
print(df)