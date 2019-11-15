'''
    python 中使用了迭代器协议
    只要对象支持 __iter__ 和 __next__ 双下划线方法, 就能使用 for-in循环
'''


# 无限迭代, 实现一个迭代器 无限打印 Hello
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater('Hello')
for item in repeater:
    print(item)

# 这种方式跟上面的一样
repeater = Repeater('Hello')
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)


# 更简单的迭代器,  用一个类会隐藏迭代器协议的基本原理，增加理解难度，不过也可以
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


repeater = Repeater('HELLO')
for item in repeater:
    print(item)
