import numpy as np
import matplotlib.pyplot as plt

x, y = 0, 0
distance = 5
steps = 0

# ランダムウォークの移動を記録するリスト
walk_x = [x]
walk_y = [y]

while np.sqrt(x**2 + y**2) < distance:
    direction = np.random.choice(["x", "y"])
    step = np.random.choice([-1, 1])
    x += step if direction == "x" else 0
    y += step if direction == "y" else 0
    steps += 1
    walk_x.append(x)
    walk_y.append(y)

mean = np.mean(steps)
std = np.std(steps)
print(f"歩数: {steps} 最終位置: ({x}, {y})")

# 日本語フォントの設定
plt.rcParams["font.family"] = "MS Gothic"

# グラフで移動経路を表示
plt.figure(figsize=(8, 6))
plt.plot(walk_x, walk_y, marker='o', linestyle='-', color='b')
plt.scatter(0, 0, color='g', label='始点 (0, 0)', zorder=2)
plt.scatter(x, y, color='r', label=f'終点 ({x}, {y})', zorder=2)
plt.plot([0, x], [0, y], linestyle='--', color='k', label='始点から終点への線')
plt.title('二次元ランダムウォークの移動経路')
plt.xlabel('X 軸')
plt.ylabel('Y 軸')
plt.legend()
plt.grid(True)
# plt.savefig("random_walk_2d_1.png")
plt.show()