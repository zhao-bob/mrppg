import types

class Car:
    price = 100000                               # 定义类属性
    def __init__(self, c):
        self.color = c                           # 定义实例属性

car1 = Car("Red")                                # 实例化对象
car2 = Car("Blue")
print(car1.color, Car.price)                     # 查看实例属性和类属性的值
Car.price = 110000                               # 修改类属性
Car.name = 'QQ'                                  # 动态增加类属性
car1.color = "Yellow"                            # 修改实例属性
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)

def setSpeed(self, s): 
    self.speed = s

car1.setSpeed = types.MethodType(setSpeed, car1) # 动态增加成员方法
car1.setSpeed(50)                                # 调用成员方法
print(car1.speed)
