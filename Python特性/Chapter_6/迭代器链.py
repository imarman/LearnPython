def integers():
    for i in range(1, 9):
        yield i


def squared(seq):
    for i in seq:
        yield i * i


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
print(list(chain))
'''
    Python 中的迭代器可以链接多个迭代器，从而编写高效的数据处理 管道 
    利用 python 的生成器函数和生成器表达式能够很快的构建简洁而强大的迭代器链
    生成器和生成器表达式时 python 中编写迭代器的语法糖, 与编写基于类的迭代器相比，这种方式能够省去许多样板代码
    
    
    可以从 integers() 生成器种获取的 ”流“， 将其在次送入另一个生成其。
    这就是 ”数据管道“ 或 ”生成器链“ 的功能
    
    在生成器链，每次只处理一个元素。链中的处理步骤之间没有缓冲区
    (1) integers 生成器产生一个值， 比如：3
    (2) 这个值 ”激活“ squared 生成器来处理， 得到 3 * 3 = 9 ，并将其传递到下一阶段
    (3) 由 squared 生成器产生的平方数立即送入 negated 生成器，将其修改为 -9 并在次 yield
    
    还可以继续拓展这个生成器链，添加自己的步骤来构建处理管道。
    生成器链可以很高效执行并很容易修改，因为链中的每一步都是单独的生成器函数
    
    
    
'''

# 改写上述生成器链
'''
    这里将每个步骤替换成一个在前一步基础上处理的生成器表达式，等价于前面的生成器链
    
    使用生成器表达式的唯一缺点就是不能在使用函数参数进行配置，也不能在同一处理管道中多次重复使用相同的生成器表达式
'''

integers = range(1, 9)
squared = (i * i for i in integers)
negated = (-i for i in squared)
print(list(negated))
