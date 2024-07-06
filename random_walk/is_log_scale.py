import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# データ
execution_counts = [2, 10, 100, 1000, 10000]
means = [31.0, 32.1, 30.7, 30.5, 30.3]  # ダミーデータ
std_devs = [5.1, 4.8, 4.2, 3.9, 3.7]  # ダミーデータ

# 横軸をlogスケールにしたグラフ
plt.figure(figsize=(10, 6))
plt.errorbar(execution_counts, means, yerr=std_devs, fmt='o', capsize=5, label='Mean Time ± Standard Deviation')
plt.xscale('log')
plt.xlabel('Execution Count (log scale)')
plt.ylabel('Time to Reach Distance 30')
plt.title('Random Walk: Time to Reach Distance 30 (Log Scale)')
plt.legend()
plt.grid(True)
plt.show()