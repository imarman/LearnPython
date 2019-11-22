xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

result = sorted(xs.items(), reverse=True)
print(result)

# 高级用法
result1 = sorted(xs.items(), key=lambda x: x[1])
print(result1)

# 根据绝对值
result2 = sorted(xs.items(), key=lambda x: abs(x[1]))
