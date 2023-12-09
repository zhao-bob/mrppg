import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x,y = np.mgrid[-2:2:20j, -2:2:20j]        # 步长使用虚数
                                          # 虚部表示点的个数
                                          # 并且包含end
z = 50 * np.sin(x+y)                      # 测试数据
ax = plt.subplot(111, projection='3d')    # 三维图形
ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.Blues_r)
ax.set_xlabel('X')                        # 设置坐标轴标签
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
