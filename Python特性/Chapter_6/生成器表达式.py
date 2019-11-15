iterator = ('hi' for i in range(3))
'''
    与列表解析式不同，生成器表达式不会构造列表对象
    基于类的迭代器或生成器函数那样“即时”生成值
    与其他生成器表达式一样，需要调用 next() 获取有生成器表达式生成的值
'''
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  # > StopIteration
#
# result = list(iterator)  # 可以对生成器表达式调用 list() 函数来构造一个包含所有生成值的列表对象

# 过滤值, 跟列表解析式一样
even_squares = (x * x for x in range(10) if x % 2 ==0)
for x in even_squares:
    print(x)

# 生成内联生成器表达式
for x in ('Bom dia' for i in range(3)):
    print(x)

# 美化生成器表达式 -->  如果生成器表达式作为函数中的单个参数，可以删除生成器表达式外层括号
sum((x*2 for x in range(10)))
sum(x*2 for x in range(10))


