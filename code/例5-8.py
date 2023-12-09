def demo(x, n):
    t1 = [i for i in x if i<n]
    t2 = [i for i in x if i>n]
    return t1 + [n] + t2

# 输出：4, 5, 2, 8, 9, 13]
print(demo([8, 4, 5, 9, 13, 2], 8))
