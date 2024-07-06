import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import datetime
import platform
import os

# ターミナルの画面を綺麗にする
def clear_terminal():
    os.system("cls" if platform.system() == "Windows" else "clear")
# end def

# 銘柄ごとの最大/最小変化値を保存
def count_index(daily_returns):
    max_count = daily_returns.dropna().idxmax(axis=1).value_counts()
    min_count = daily_returns.dropna().idxmin(axis=1).value_counts()
    return {"max": max_count, "min": min_count}
# end def

def save_summary_fig(title, idx_counts):
    # データフレームの作成
    max_count = idx_counts["max"]
    min_count = idx_counts["min"]
    summary_df = pd.DataFrame(
        {
            "銘柄": max_count.index,
            "最大": max_count[max_count.index].values,
            "最小": min_count[min_count.index].values,
        }
    )

    # ターミナルに銘柄ごとのデータを表示する
    print(f"\n{title}の変化値：\n\n   銘柄 最大 最小")
    for index, row in summary_df.iterrows():
        print(f"{index + 1:>2} {row['銘柄']:>4} {row['最大']:>4} {row['最小']:>4}")
    
    # 日本語フォントの設定
    plt.rcParams["font.family"] = "MS Gothic"

    # データフレームを画像として表示する
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.axis("off")  # 軸を非表示にする
    ax.set_title(f"銘柄ごとの最大/最小変化値({title})")

    # データフレームをテーブルとして描画する
    idx_table = ax.table(
        cellText=summary_df.values,
        colLabels=summary_df.columns,
        loc="center",
        cellLoc="center",
    )

    # テーブルの書式設定
    idx_table.auto_set_font_size(False)
    idx_table.set_fontsize(12)
    idx_table.scale(1.2, 1.2)

    # 画像を保存する
    plt.tight_layout()
    fig.savefig(f"{title}_table.png", bbox_inches="tight", pad_inches=0.5)
# end def

clear_terminal()

# 銘柄コードの入力
default_tickers = ["AAPL", "IBM", "MSFT", "GOOG"]
print("デフォルト： AAPL, IBM, MSFT, GOOG")
tickers = input("銘柄コードを「,」で区切って入力してください： ")
clear_terminal()
print(f"入力された銘柄コード： {tickers if tickers.strip() != '' else 'AAPL, IBM, MSFT, GOOG'}\n")
tickers = default_tickers if tickers.strip() == "" else [ticker.strip() for ticker in tickers.split(",")]

# データをダウンロード
start = "2015-01-01"
end = datetime.date.today()
all_data = {ticker: yf.download(ticker, start=start, end=end) for ticker in tickers}

# Adj Close と Volume を抽出
prices = pd.DataFrame({ticker: data["Adj Close"] for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data["Volume"] for ticker, data in all_data.items()})

# 日ごとのパーセント変化を計算
prices_daily_returns = prices.pct_change()
volume_daily_returns = volume.pct_change()

# NaN値を含む行を削除してから、銘柄ごとにパーセント変化最大/最小になった日数を求める
prices_count = count_index(prices_daily_returns)
volume_count = count_index(prices_daily_returns)

# 銘柄ごとの最大/最小変化値を画像で保存
save_summary_fig("prices", prices_count)
save_summary_fig("volume", volume_count)
