def quickSort(lst, reverse=False):
    if len(lst) <= 1:
        return lst
    # 默认使用最后一个元素作为枢点
    pivot = lst.pop()
    first, second = [], []
    # 默认使用升序排序
    exp = 'x<=pivot'
    # reverse=True表示降序排列
    if reverse == True:
        exp = 'x>=pivot'
    for x in lst:
        first.append(x) if eval(exp) else second.append(x)
    # 递归调用
    return quickSort(first, reverse) + [pivot] + quickSort(second, reverse)

data = [3, 5, 7, 2, 9]
print(data)
data = quickSort(data)
print(data)
