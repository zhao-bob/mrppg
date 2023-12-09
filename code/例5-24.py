import random

def mergeSort(seq, reverse=False):
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = mergeSort(left)
    if len(right) > 1:
        right = mergeSort(right)
    temp = []
    while left and right:
        if left[-1] >= right[-1]:
            temp.append(left.pop())
        else:
            temp.append(right.pop())
    temp.reverse()
    result = (left or right) + temp
    if reverse:
        result.reverse()
    return result

for i in range(100000):
    reverse = random.choice((True, False))
    x = random.choices(range(1,100), k=20)
    if sorted(x, reverse=reverse) != mergeSort(x, reverse):
        print(x)
else:
    print('通过测试。')
