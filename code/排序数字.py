from random import shuffle      # 从标准库random中导入函数shuffle()

data = list(range(10))          # 创建列表
print(data)                     # 输出列表的值
shuffle(data)                   # 随机打乱列表中元素的顺序
print(data)
data.sort()                     # 把列表中的元素从小到大升序排序
print(data)
