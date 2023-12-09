def hannuo(num, src, dst, temp=None):
    # 声明用来记录移动次数的变量为全局变量
    global times
    # 确认参数类型和范围
    assert type(num) == int, 'num must be integer'
    assert num > 0, 'num must > 0'
    # 只剩最后或只有一个盘子需要移动，这也是函数递归调用的结束条件
    if num == 1:
        print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
        times += 1
    else:
        # 递归调用函数自身，
        # 先把除最后一个盘子之外的所有盘子移动到临时底座上
        hannuo(num-1, src, temp, dst)
        # 把最后一个盘子直接移动到目标底座上
        hannuo(1, src, dst)
        # 把除最后一个盘子之外的其他盘子从临时底座上移动到目标底座上
        hannuo(num-1, temp, dst, src)

# 用来记录移动次数的变量
times = 1
# A表示最初放置盘子的底座，C是目标底座，B是临时底座
hannuo(3, 'A', 'C', 'B')
