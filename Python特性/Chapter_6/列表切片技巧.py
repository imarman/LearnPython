# 切边操作 [start:stop:step]
lst = [1, 2, 3, 4, 5]
lst[::-1]  # 得到逆序  推荐使用 list.reverse() 和 内置的 reverse() 反转列表

#  ：操作可以清空列表所有的元素, 并且保持对象不变 Py3 种可以使用 list.clear() 完成
del lst[:]

original_list = lst
lst = [7, 8, 9]
# original_list -> [1, 2, 3, 4, 5]

lst[:] = [7, 8, 9]  # 因为是浅复制，只复制元素结构，不复制元素本身；两个列表元素都是相同的实例
# original_list -> [7, 8, 9]
