def demo(lst, k):
    x = lst[k-1::-1]
    y = lst[:k-1:-1]
    return list(reversed(x+y))

print(demo([1, 2, 3, 4, 5, 6, 7], 3))
