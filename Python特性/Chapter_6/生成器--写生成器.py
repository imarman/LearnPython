'''
    生成器是简化版迭代器
'''


# 无限生成器
def repeater(value):
    while True:
        yield value


# for item in repeater('Hi'):
#     print(item)


# 停的下来的生成器
def repeat_three_times(value):
    yield value
    yield value
    yield value


'''
    该生成器在迭代三次后停止生产新值，
    原因是执行到后面引发 StopIteration 异常引起的
    当函数内部调用 return 语句时：控制权会永久性的还给函数的调用者
    调用 yield 语句时：虽然控制权也交给函数的调用者了，但是只是暂时的
'''

for item in repeat_three_times('Hi arman'):
    print(item)

# > Hi arman
# > Hi arman
# > Hi arman


def bound_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return None
        count += 1
        yield value


for item in bound_repeater('Hi', 3):
    print(item)


# 上述生成器的更优化版本, 用 range() 方法 替换 while 语句
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value


for item in bounded_repeater('Hi', 3):
    print(item)