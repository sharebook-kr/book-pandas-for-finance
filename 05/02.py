import pandas as pd

dates = ["2019-06-07", "2019-06-05", "2019-06-04", "2019-06-03", "2019-05-31"]
index = pd.to_datetime(dates)
print(index)
