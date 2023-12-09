def demo(*para):
    avg = sum(para) / len(para)            # 平均值
    g = [i for i in para if i>avg]         # 列表推导式
    return (avg,) + tuple(g)

print(demo(1, 2, 3, 4, 5))                 # 输出：(3.0, 4, 5)
