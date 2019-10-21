# namedtuple 是元组的拓展
from collections import namedtuple


# 普通类
class Car_Class:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'Car({self.color, self.mileage})'


# 效果根手动定义的类并提供一个接受 color 和 mileage 值的构造函数相同
Car = namedtuple('Car', ['color', 'mileage', ])

my_car = Car('red', 3812.4)

# namedtuple 是不可变得， 试图覆盖某个字段时会得到一个 AttributeError 异常
my_car.color = 'blue'
# >>> AttributeError: can't set attribute


# 子类化namedtuple
Car = namedtuple('Car', ['color', 'mileage', ])


class MyCarWithMethod(Car):
    def hexocolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethod('red', 1234)
print(c.hexocolor())

# 内置辅助方法 _fields
Car = namedtuple('Car', ['color', 'mileage', ])
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))

print(ElectricCar('red', 1234, 45.0))
# >>> ElectricCar(color='red', mileage=1234, charge=45.0)