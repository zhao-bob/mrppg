import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fig = plt.figure(facecolor='#eeeeee')
ax = plt.axes(facecolor='#ffaaee')
# 创建DataFrame对象，见13.3节
df = pd.DataFrame({'男性': (450,800,200), '女性': (150,100,300)})
# 绘制柱状图
df.plot(kind='bar', ax=ax, color=['red','blue'])

font = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf', size=12)
# 设置x轴刻度和文本
plt.xticks([0,1,2], ['从不闯红灯', '跟从别人闯红灯', '带头闯红灯'],
            color='black',              # 刻度文本的颜色
            fontproperties=font,        # 中文字体
            rotation=20)                # 对刻度文本进行旋转

# 设置y轴只在有数据的位置显示刻度
plt.yticks(list(df['男性'].values) + list(df['女性'].values))
plt.ylabel('人数', fontproperties='stkaiti', fontsize=14)
plt.title('过马路方式', fontproperties='stkaiti', fontsize=20)

# 创建和设置图例字体
plt.legend(prop=font)

plt.show()
