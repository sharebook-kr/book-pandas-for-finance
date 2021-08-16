from pykrx import stock
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"

df = stock.get_index_kospi_ohlcv_by_date("20000104", "20181231", "코스피")
df["수익률"] = df["종가"] / df["시가"][0]
df["수익률"].plot()

plt.show()
