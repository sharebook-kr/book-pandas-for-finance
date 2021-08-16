from pykrx import stock
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
df = stock.get_index_kospi_ohlcv_by_date("20190101", "20190531", "코스피")

close = df['종가']
close.plot()
plt.show()
