from random import randint

def bubbleSort(lst, reverse=False):
    length = len(lst)
    for i in range(0, length):
        flag = False
        for j in range(0, length-i-1):
            # 比较相邻两个元素大小，并根据需要进行交换，默认升序排序
            exp = 'lst[j] > lst[j+1]'
            # 如果reverse=True则降序排序
            if reverse:
                exp = 'lst[j] < lst[j+1]'
            if eval(exp):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # flag=True表示本次扫描发生过元素交换
                flag = True
        # 如果一次扫描结束后，没有发生过元素交换，说明已经按序排列
        if not flag:
            break

data = [3, 5, 7, 2, 9]
print(data)
bubbleSort(data)
print(data)
