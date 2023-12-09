import abc

class Foo(metaclass=abc.ABCMeta):  # 抽象类
    def f1(self):                  # 普通实例方法
        print(123)

    def f2(self):                  # 普通实例方法
        print(456)

    @abc.abstractmethod            # 抽象方法
    def f3(self):
        raise Exception('You musr reimplement this method.')

class Bar(Foo):
    def f3(self):                  # 必须重新实现基类中的抽象方法
        print(33333)

b = Bar()                          # 创建派生类的实例
b.f3()                             # 调用派生类中实现的基类抽象方法
