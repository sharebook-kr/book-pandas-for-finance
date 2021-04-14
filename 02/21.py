class StockItem:
    def __init__(self, code, name, market):
        self.code = code
        self.name = name
        self.market = market

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_market(self):
        return self.market

a = StockItem("000020", "동화약품", "코스피")
b = StockItem("000040", "KR모터스", "코스피")

print(a.get_name())
print(b.get_name())

