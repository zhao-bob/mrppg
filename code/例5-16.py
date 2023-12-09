from random import randint
from itertools import permutations

# 4个数字和2个运算符可能组成的表达式形式
exps = ('((%s %s %s) %s %s) %s %s',
        '(%s %s %s) %s (%s %s %s)', 
        '(%s %s (%s %s %s)) %s %s',
        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))')
ops = r'+-*/'

def test24(v):
    result = []
    # Python允许函数的嵌套定义
    # 这个函数对字符串表达式求值并验证是否等于24
    def check(exp):
        try:
            # 有可能会出现除0异常，所以放到异常处理结构中
            return eval(exp) == 24
        except:
            return False
    # 全排列，枚举4个数的所有可能顺序
    for a in permutations(v):
        # 查找4个数的当前排列能实现24的表达式
        t = [exp % (a[0], op1, a[1], op2, a[2], op3, a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps if check(exp %(a[0], op1, a[1], op2, a[2], op3, a[3]))]
        if t:
            result.append(t)
    return result

for i in range(20):
    print('='*20)
    # 生成随机数字进行测试
    lst = [randint(1, 13) for j in range(4)]
    r = test24(lst)
    if r:
        print(r)
    else:
        print('No answer for ', lst)
