import pybithumb
import numpy as np
import time


def get_ror(ticker):
    df = pybithumb.get_ohlcv(ticker, interval="day")
    df = df["2019"]

    df["변동성"] = (df['high'] - df['low']) * 0.5
    df["목표가"] = df["open"] + df["변동성"].shift(1)

    df["수익률"] = np.where(df['high'] > df['목표가'],
                            df['목표가'] / df['close'],
                            1)

    df["기간수익률"] = df["수익률"].cumprod()
    return df["기간수익률"].iloc[-1]


tickers = pybithumb.get_tickers()
for ticker in tickers:
    ror = get_ror(ticker)
    print("{} - {}".format(ticker, ror))
    time.sleep(1)
