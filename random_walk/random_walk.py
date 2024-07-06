import numpy as np
import matplotlib.pyplot as plt


def random_walk(distance, nwalk):
    nsteps = []

    for i in range(nwalk):
        position = 0
        steps = 0

        while abs(position) < distance:
            position += np.random.choice([-1, 1])
            steps += 1
        nsteps.append(steps)
    mean = np.mean(nsteps)
    std = np.std(nsteps)
    print(f"実行回数: {nwalk:>5}, 平均歩数: {mean:>7.2f}, 標準偏差: {std:>7.2f}")
    return mean, std
# end random_walk

# 実行回数と目標距離
nwalks = [2, 10, 100, 1000, 10000]
distance = 30

# 各実行回数での平均歩数と標準偏差を計算
results = [random_walk(distance, nwalk) for nwalk in nwalks]
means, stds = zip(*results)

# 日本語フォントの設定
plt.rcParams["font.family"] = "MS Gothic"

# 平均/標準偏差プロットの作成
fig, ax = plt.subplots()
ax.plot(nwalks, means, "o-", label="平均歩数")
ax.errorbar(nwalks, means, yerr=stds, fmt="o", label="標準偏差")

# ログスケール/軸ラベル/タイトルの設定
ax.set_xscale("log")
ax.set_xlabel("ランダムウォークを行った回数 (Log スケール)")
ax.set_ylabel(f"目標距離 {distance} までに掛かった歩数")
ax.set_title("ランダムウォーク：平均歩数と標準偏差")

# 凡例/グリッド/プロットの表示
ax.legend()
ax.grid(axis="y", which="both")
fig.savefig("random_walk.png")
plt.show()
