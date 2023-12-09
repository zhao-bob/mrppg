def f():
    a, b = 1, 1  # 序列解包，同时为多个变量赋值
    while True:
        yield a  # 暂停执行，需要时再产生一个新元素
        a, b = b, a + b  # 序列解包，继续生成新元素


print(next(f()))
# for i in f():
#     if i > 100:
#         print(i, end=' ')
#         break

