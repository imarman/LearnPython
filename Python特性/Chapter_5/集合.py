from collections import Counter
'''
collection.Counter 类实现了多重集合，也称 bag 类型；
该类允许在集合里多次出现同一个元素  
'''
inventory = Counter()
loot = {'sword': 1, 'bread': 3}
inventory.update(loot)

more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
# >> Counter({'bread': 3, 'sword': 2, 'apple': 1})

# 唯一元素的个数
len(inventory)
# > 3

# 想获取元素总数需要使用 sum() 函数
sum(inventory.values())
