import pandas as pd
import yfinance as yf
import datetime

# データをダウンロード
start = "2015-01-01"
end = datetime.date.today()
tickers = ["AAPL", "IBM", "MSFT", "GOOG"]
all_data = {ticker: yf.download(ticker, start=start, end=end) for ticker in tickers}

# Adjusted Closeを抽出
price = pd.DataFrame({ticker: data["Adj Close"] for ticker, data in all_data.items()})

# 日ごとのパーセント変化を計算
daily_returns = price.pct_change()

# パーセント変化の最大/最小値とその回数を計算
max_returns = daily_returns.max()
min_returns = daily_returns.min()
max_count = daily_returns.idxmax(axis=1).value_counts()
min_count = daily_returns.idxmin(axis=1).value_counts()

# データフレームの作成
summary_df = pd.DataFrame({
    '銘柄': max_returns.index,
    'パーセント変化最大値': max_returns.values,
    '最大値をとった回数': max_count[max_returns.index].values,
    'パーセント変化最小値': min_returns.values,
    '最小値をとった回数': min_count[min_returns.index].values
})

# データフレームの表示（横幅を揃えて左寄せ）
print(summary_df.to_string(index=False, justify='left'))
