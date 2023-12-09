def myMaxMin(iterable):
    '''返回序列的最大值和最小值'''
    tMax = tMin = iterable[0]
    for item in iterable[1:]:
        if item > tMax:
            tMax = item
        elif item < tMin:
            tMin = item
            
    return (tMax, tMin)

print(myMaxMin([8, 1, 9, 0, 6, 3]))
