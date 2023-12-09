def demo(a, n):
    assert type(n)==int and type(a)==int and 0<a<10
    result, t = 0, 0
    for i in range(n):
        t = t*10 + a
        result = result + t
    return result

print(demo(3, 4))
