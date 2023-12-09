import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
data = np.concatenate((np.random.randint(35, 55, 25),
                         np.random.randint(55, 80, 15)))
# 手动加入异常值
data[25] = 10
data[26] = 99
plt.boxplot(data,
            # 显示均值
            showmeans=True,
            # 设置均值为绿色下三角符号
            meanprops={'marker': 'v', 'color':'green'},
            # 使用2像素宽的红色虚线显示中值
            medianprops={'lw':2, 'ls':'--', 'color':'red'},
            # 使用凹凸的形式显示箱线图
            notch=True,
            # 显示橘红色箱体
            boxprops={'color':'orangered'},
            # 显示异常值
            showfliers=True,
            # 设置异常值的显示形式
            flierprops={'marker':'*', 'markersize':10},
            # 使用蓝色点划线显示箱线图的须
            whiskerprops={'ls':'-.', 'color':'blue'})
# 设置y轴刻度
plt.yticks(range(0, 101, 20))
# 显示绘制结果
plt.show()
