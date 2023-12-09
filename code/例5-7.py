def demo(m, n):
    p = m*n
    while m%n != 0:
        m, n = n, m%n
    return (n, p//n)

print(demo(66, 38))
