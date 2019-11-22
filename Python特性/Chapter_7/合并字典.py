xs = {'a': 1, 'b': 2}
xy = {'b': 3, 'c': 4}

# 最经典的方法 ， 用内置字典的 update() 方法
zs = {}
zs.update(xs)
zs.update(xy)
print(zs)

# 2.结合内置的 dict() 与 ** 操作来“拆包”,此方法知识和两个字典
zs = {**xs, **xy}
print(zs)
