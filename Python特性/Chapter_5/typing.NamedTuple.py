from typing import NamedTuple

'''
改进版namedtuple, 有类型注解 要定义类型， 只是检查类型注解
'''


class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car1 = Car('red', 99.9, True)
print(car1)