import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)
z = np.cos(x*x)
plt.figure(figsize=(8,4))
# 标签前后加$将使用内嵌的LaTex引擎将其显示为公式
plt.plot(x, y, label='$sin(x)$', color='red', linewidth=2) # 红色，2个像素宽
plt.plot(x, z, 'b--', label='$cos(x^2)$')                  # 蓝色，虚线
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Sin and Cos figure using pyplot')
plt.ylim(-1.2, 1.2)
plt.legend()                                         # 显示图例
plt.show()                                           # 显示绘图窗口
