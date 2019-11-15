# java 或 C 特色的循环
my_items = ['a', 'b', 'c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

# 好一点的方法
for i in range(len(my_items)):
    print(my_items[i])

# Pythonic 方法  range(len(....)) 可以进一步简化
for item in my_items:
    print(item)

# 如果需要用到索引 用 enumerate() 方法
for i, item in enumerate(my_items):
    print(f'{i}:{item}')

emails = {
    'Bob': 'bob@example.com',
    'alice': 'alice@example.com',
}

for name, email in emails.items():
    print(f'{name} -> {email}')
# > Bob -> bob@example.com
# > alice -> alice@example.com

