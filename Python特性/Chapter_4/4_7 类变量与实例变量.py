#  类变量与实例变量的陷进
# class Dog:
#     num_legs = 4  # 类变量
#
#     def __init__(self, name):
#         self.name = name  # 实例变量
#
#     def __repr__(self):
#         return self.name
#
#
# jack = Dog('Jeck')
# print(jack.name)
#
# jill = Dog('jill')
# print(jill.name)
#
# jill.num_legs = 8
#
# print(jack.num_legs)
# print(jill.num_legs)
# print(jill.__class__.num_legs) # 从这里可以发现，并不是 num_legs 变了， 只是 jill.num_legs 创建了同名的“实例变量”
# print(Dog.num_legs)


class CountedObject:
    num_instances = 0

    # 这段代码需要额外的 __class__ 来确保增加的是类上的变量
    def __init__(self):
        self.__class__.num_instances += 1  # __class__ 十分重要


print(CountedObject.num_instances)  # 类变量
print(CountedObject().num_instances)  # 实例变量
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject.num_instances)

# >>> 0
# >>> 1
# >>> 2
# >>> 3
# >>> 3
