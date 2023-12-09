def before(func):                   # 定义修饰器
    def wrapper(*args, **kwargs):   # 在内层函数中对被修饰的函数进行一定修改
        print('Before function called.')
        return func(*args, **kwargs)
    return wrapper                  # 返回内层函数

def after(func):                    # 定义修饰器
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('After function called.')
        return result
    return wrapper

@before
@after
def test():                         # 同时使用两个修饰器改造函数，距离近的先起作用
    print(3)
# 调用被修饰的函数
test()
