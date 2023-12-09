def selectSort(lst, reverse=False):
    length = len(lst)
    for i in range(0, length):
        # 假设剩余元素中第一个最小或最大
        m = i
        # 扫描剩余元素
        for j in range(i+1, length):
            # 如果有更小或更大的，就记录下它的位置
            exp = 'lst[j] < lst[m]'
            if reverse:
                exp = 'lst[j] > lst[m]'
            if eval(exp):
                m = j
        # 如果发现更小或更大的，就交换值
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]


data = [3, 5, 7, 2, 9]
print(data)
selectSort(data)
print(data)
