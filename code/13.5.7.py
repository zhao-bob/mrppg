import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['legend.fontsize'] = 10        # 图例字号
ax = plt.subplot(projection='3d')           # 三维图形
theta = np.linspace(-4*np.pi, 4*np.pi, 100)
z = np.linspace(-4, 4, 100)*0.3             # 测试数据
r = z**3 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()
