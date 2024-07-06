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

# Adjusted Closeを抽出
price = pd.DataFrame({ticker: data["Adj Close"] for ticker, data in all_data.items()})

# 日ごとのパーセント変化を計算
daily_returns = price.pct_change()

# パーセント変化の最大値とその銘柄を調べる
max_returns = daily_returns.max()
max_tickers = daily_returns.idxmax()

# パーセント変化の最小値とその銘柄を調べる
min_returns = daily_returns.min()
min_tickers = daily_returns.idxmin()

# 銘柄ごとにパーセント変化最大値になった回数を求める
max_count = daily_returns.groupby(max_tickers).size()
max_count = max_count.reindex(tickers, fill_value=0)

# 銘柄ごとにパーセント変化最小値になった回数を求める
min_count = daily_returns.groupby(min_tickers).size()
min_count = min_count.reindex(tickers, fill_value=0)

# テーブルを作成
result_table = pd.DataFrame({
    "最大変化値": max_returns,
    "最大変化値を持った回数": max_count,
    "最小変化値": min_returns,
    "最小変化値を持った回数": min_count
})

# テーブルの整形と表示
result_table_styled = result_table.style.set_table_styles([
    {'selector': 'th', 'props': [('text-align', 'center')]},  # タイトル行のテキストを中央揃えに
    {'selector': 'td', 'props': [('text-align', 'center')]},  # データ行のテキストを中央揃えに
    {'selector': '', 'props': [('border', '1px solid black')]},  # セルの境界線を追加
]).format({
    "最大変化値": "{:.6f}",
    "最小変化値": "{:.6f}",
    "最大変化値を持った回数": "{:.0f}",
    "最小変化値を持った回数": "{:.0f}"
}).to_string()

print(result_table_styled)
