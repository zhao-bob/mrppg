import pylab as pl
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf') # 设置字体
t = pl.arange(0.0, 2.0*pl.pi, 0.01)         # 自变量取值范围
s = pl.sin(t)                               # 计算正弦函数值
z = pl.cos(t)                               # 计算余弦函数值
pl.plot(t, s, label='正弦')
pl.plot(t, z, label='余弦')
pl.xlabel('x-变量', fontproperties='STKAITI', fontsize=18)        # 设置x标签
pl.ylabel('y-正弦余弦函数值', fontproperties='simhei', fontsize=18)
pl.title('sin-cos函数图像', fontproperties='STLITI', fontsize=24)
pl.legend(prop=myfont)                      # 设置图例
pl.show()
