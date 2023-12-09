import numpy as np
import matplotlib.pyplot as plt

labels = np.array(list('abcdefghij'))  # 设置标签
data = np.array([11,4]*5)              # 创建模拟数据
dataLength = len(labels)               # 数据长度

# angles数组把圆周等分为dataLength份
angles = np.linspace(0,                # 数组第一个数据
                     2*np.pi,          # 数组最后一个数据
                     dataLength,       # 数组中数据数量
                     endpoint=False)   # 不包含终点
data = np.append(data, data[0])
angles = np.append(angles, angles[0])  # 首尾相接，使得曲线闭合
# 绘制雷达图
plt.polar(angles,                      # 设置角度
          data,                        # 设置各角度上的数据
          'rv--',                      # 设置颜色、线型和端点符号
          linewidth=2)                 # 设置线宽

# 设置角度网格标签
plt.thetagrids(angles[:10]*180/np.pi,  # 角度
               labels)                 # 标签

# 设置填充色
plt.fill(angles,                       # 设置角度
         data,                         # 设置各角度上的数据
         facecolor='r',                # 设置填充色
         alpha=0.6)                    # 设置透明度
plt.ylim(0, 12)                        # 设置坐标跨度

plt.show()
