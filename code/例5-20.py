from random import randint

def bubbleSort(lst, end=None, reverse=False):
    if end == None:
        length = len(lst)
    else:
        length = end
    if length <= 1:
        return
    flag = False                          # flag用来标记本次扫描过程中是否发生了元素的交换
    for j in range(length-1):
        exp = 'lst[j] > lst[j+1]'         # 比较相邻两个元素大小，并根据需要进行交换，默认升序排序
        if reverse:                       # 如果reverse=True则降序排序
            exp = 'lst[j] < lst[j+1]'
        if eval(exp):
            lst[j], lst[j+1] = lst[j+1], lst[j]
            flag = True
    if flag == False:                     # 如果没有发生元素交换，则表示已按序排列
        return
    else:
        bubbleSort(lst, length-1, reverse)# 对剩余的元素进行排序

data = [3, 5, 7, 2, 9]
print(data)
bubbleSort(data)
print(data)
