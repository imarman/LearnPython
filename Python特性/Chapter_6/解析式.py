# Pythonic 列表推导式
squares = [x * x for x in range(10)]

# 可以添加条件过滤元素
even_squares = [x * x for x in range(10) if x % 2 == 0]

# 集合解析式
result = {x * x for x in range(-9, 10)}

# 字典解析式
result_dict = {x: x * x for x in range(5)}


