import pandas as pd

dates = ["19/06/07", "19/06/05", "19/06/04", "19/06/03", "19/05/31"]
index = pd.to_datetime(dates, format="%y/%m/%d")
print(index)
