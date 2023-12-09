def binarySearch(lst, value):
    start = 0
    end = len(lst) - 1
    while start <= end:
        # 计算中间位置
        middle = (start + end) // 2
        # 查找成功，返回元素对应的位置
        if value == lst[middle]:
            return middle
        # 在后面一半元素中继续查找
        elif value > lst[middle]:
            start = middle + 1
        # 在前面一半元素中继续查找
        elif value < lst[middle]:
            end = middle - 1
    # 查找不成功，返回False
    return False

data = list(range(20))
print(binarySearch(data, 15))
