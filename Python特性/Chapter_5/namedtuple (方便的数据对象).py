
'''
collections.namedtuple -- 方便的数据对象
可以当作类使用
'''
from collections import namedtuple

Animal = namedtuple('Car', 'name age cry')
cat = Animal('小猫', 2, 'miao')
# 有不错的 __repr__ 方法
print(cat)
# >>> Car(name='小猫', age=2, cry='miao')

# 访问字段
cat.cry

# 字段是不可变的
cat.age = 4
# >>> AttributeError: can't set attribute
