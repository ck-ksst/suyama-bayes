# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib 
from scipy import stats

n = np.arange(1, 501, 1)
# 実験回数
TRIAL_NUMBERS = 6
#　試行回数
N = 5000
# 1（表）の出やすさ
p = 1/3

# x: 試行の列
x = []
# y:　各試行でのその時点での近似エントロピーの値
y = []

# 表裏の列を実験回数個だけ生成
for i in range(TRIAL_NUMBERS):
    x.append(stats.bernoulli.rvs(p=p, size=N))
    y.append([])
n = np.arange(1, N + 1, 1)
c = ['b', 'g', 'r', 'c', 'm', 'y'] # 色
l = [str(j+1)+"回目" for j in range(TRIAL_NUMBERS)] #ラベル：実験回数

for i in range(1, N + 1):
    for j in range(TRIAL_NUMBERS):
        COUNT_ONE = np.count_nonzero(x[j][:i]==1)
        COUNT_ZERO = np.count_nonzero(x[j][:i]==0)
        ap_H = - (COUNT_ONE * np.log(1/3) + COUNT_ZERO * np.log(2/3)) / i
        y[j].append(ap_H)


fig, ax = plt.subplots()
for i in range(TRIAL_NUMBERS):
    ax.plot(n, y[i], color=c[i], label=l[i])
ax.set_xlabel('試行回数')
ax.set_ylabel('近似エントロピー')
ax.set_title('近似エントロピーの実験')
# ax.legend()
plt.legend()
plt.show()