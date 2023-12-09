import random

lstColor = ('red', 'green', 'blue')
colors = [random.choice(lstColor) for i in range(10000)]

for item in colors:                # 遍历列表中的元素并逐个判断
    if item not in lstColor:
        print('error:', item)
        break

if (set(colors)-set(lstColor)):    # 转换为集合之后再比较
                                   # 等价于set(colors)>set(lstColor)
    print('error')
else:
    print('pass')
