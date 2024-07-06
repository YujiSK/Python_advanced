import numpy as np
import matplotlib.pyplot as plt

def random_walk (distance, nwalks):
    
    # 初期化
    nsteps = []

    for i in range(nwalks):
        position = 0
        steps = 0
        
        while abs(position) < distance:
            position += np.random.choice([-1, 1])
            steps += 1
            
        nsteps.append(steps)

    return nsteps
    
# 目標とする距離
distance = 2
nwalks = [2, 10, 100]
means = []
stds = []
   
for nwalk in nwalks:
    nsteps = random_walk (distance, nwalk)
    means.append(np.mean(nsteps))
    stds.append(np.std(nsteps))
    # print(f'Number of Walks: {nwalk}, Mean: {mean}, Standard Deviation: {std}')

plt.figure()
plt.plot(nwalks, means, label='mean')
plt.plot(nwalks, stds, label='std')
# plt.xscale('log')
plt.xlabel('Number of Executions')
plt.ylabel('Time')
plt.legend()
plt.show()