def myAll(iterable):
    '''模拟内置函数all()'''
    # 只要有一个元素等价于False，返回False
    for item in iterable:
        if not item:
            return False
    # 如果所有元素都等价于True，返回True
    return True

print(myAll([1, 2, 3, 'Python小屋']))

def myAny(iterable):
    '''模拟内置函数any()'''
    # 只要有一个元素等价于True，返回True
    for item in iterable:
        if item:
            return True
    # 如果所有元素都等价于False，返回False
    return False

print(myAny([1, 2, 3, 'Python小屋']))

def myZip(*iterables):
    '''模拟内置函数zip()'''
    # 获取所有迭代对象的最小长度
    min_length = min(map(len,iterables))
    
    # 依次返回所有迭代对象中对应位置上元素组成的元组
    for i in range(min_length):
        yield tuple((it[i] for it in iterables))

print(list(myZip('Python', 'Julia')))
