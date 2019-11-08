import array

'''
array.array 的行为和列表类似
区别： 这种数组是单一数据类型的
'''
# arr = array.array('f', (1, 2, 3, 4, 5))
# print(arr[0])

# 字符串是不可变类型
# arr = 'abcd'
# arr[1] = 'f'


# 字符串可以解包到列表中， 从而得到可变版本
# arr = list('abcd')
# arr = ''.join(arr)


# bytes --- 含有但单字节的不可变数组
# arr = bytes((1, 2, 3, 4, 5))
# print(bytes((0, 255))) # 单字节为 0 - 255(含)

# bytearray --- 含有单字节的可变数组 bytes 可以解包到 bytearray  范围和bytes一样
# arr = bytearray((0, 1, 2, 3))

# bytearray 是可变的
# arr[1] = 23

# bytearray 可以增长或缩小
# del arr[1]
# arr.append(42)

# bytearray 可以转回 byte 对象，此过程是复制
# bytes(arr)
