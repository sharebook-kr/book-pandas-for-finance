from pykrx import stock
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.rcParams["font.family"] = "Malgun Gothic"

df = stock.get_market_ohlcv_by_date("20180101", "20190531", "005930")
#df['거래량'].plot.bar()
volume = df['거래량']
plt.bar(volume.index, volume.value)
#plt.yscale('linear')
plt.show()
