import random

def getTwoClosestElements(seq):
    seq = sorted(seq)
    # 直接使用内置函数求解问题
    print(min(zip(seq[:-1], seq[1:]), key=lambda item: abs(item[0]-item[1])))
    dif = float('inf')
    for i, v in enumerate(seq[:-1]):
        d = abs(v-seq[i+1])
        if d < dif:
            first, second, dif = v, seq[i+1], d
    return (first, second)

seq = [random.random() for i in range(20)]
print(seq)
print(sorted(seq))
print(getTwoClosestElements(seq))
