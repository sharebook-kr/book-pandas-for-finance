data = [("000060", 8.25), ("000020", 5.75), ("039490", 1.3)]

def 정렬규칙(x):
    return x[1]

data.sort(key=정렬규칙)
print(data)
