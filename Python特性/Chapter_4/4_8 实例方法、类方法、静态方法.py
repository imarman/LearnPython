# class MyClass:
#     def method(self):
#         return 'instance method called', self
#
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#
#     @staticmethod
#     def staticmethod():
#         return 'static method called'
#
#
# obj = MyClass()
# # 实例方法
# print(obj.method())
# # print(MyClass.method(obj))  # 两种方法一样
#
# # 类方法
# print(obj.classmethod())
#
# # 静态方法
# print(obj.staticmethod())
#
# print(MyClass.classmethod())
# print(MyClass.staticmethod())
# print(MyClass.method()) # 会报错 没有实例化 会抛出 TypeError
#
#
#
# # 使用 @classmethod 的工厂类
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return f'Pizza({self.ingredients})'
#
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])
#
#     @classmethod
#     def prosciutto(cls):
#         return cls(['mozzarella', 'tomatoes', 'ham'])
#
#
# # print(Pizza(['cheese', 'tomatoes']))
# # print(Pizza(['cheese', 'tomatoes', 'ham', 'mushrooms']))
# # print(Pizza(['ham'] * 4))
# print(Pizza.margherita())
# print(Pizza.prosciutto())


# 使用 静态方法
import math


class Pizza:

    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.radius}, {self.ingredients})'

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(4, ['ham', 'tomatoes'])
print(p.area())
