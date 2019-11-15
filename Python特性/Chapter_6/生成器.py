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
'''

for item in repeat_three_times('Hi arman'):
    print(item)
