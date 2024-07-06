from pandas import Series, DataFrame
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import os

# データをダウンロード
start = "2015-01-01"
end = datetime.date.today()
tickers = ["AAPL", "IBM", "MSFT", "GOOG"]
all_data = {ticker: yf.download(ticker, start=start, end=end) for ticker in tickers}

os.system("cls")

# 関数lessを定義
pd.DataFrame.less = lambda self, n=10: pd.concat([self.head(n // 2), self.tail(n // 2)])

# Adjusted Closeを抽出
price = pd.DataFrame({ticker: data["Adj Close"] for ticker, data in all_data.items()})
# Volumeを抽出
volume = pd.DataFrame({ticker: data["Volume"] for ticker, data in all_data.items()})

# すべての値の最大幅を計算
max_len = max(
    price.apply(
        lambda col: col.map(lambda x: f"{x:.2f}".rstrip("0").rstrip("."))
        .str.len()
        .max()
    ).max(),
    volume.apply(lambda col: col.map(lambda x: f"{x:,}").str.len().max()).max(),
)

# 位置を揃えてフォーマット
price = price.apply(
    lambda col: col.map(lambda x: f"{x:.2f}".rstrip("0").rstrip(".").rjust(max_len))
)
volume = volume.apply(lambda col: col.map(lambda x: f"{x:,}".rjust(max_len)))

# データ名と共に出力
print("Adjusted Close:")
print(price.less(2))
# print(separator)
print("Volume:")
print(volume.less(2))