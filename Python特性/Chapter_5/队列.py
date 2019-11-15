#  列表 -- 非常慢的队列
#  由于在起始位置插入或删除元素需要将多有的其他元素都移动一个位置，因此需要的时间为O(n)
from collections import deque

q = ['eat', 'sleep', 'code']
#  这种操作很慢！！！
q.pop(0)


'''
    deque 对象一双向链表实现， 这为插入和删除元素提供了出色且一致的性能
    但是，随机访问位于栈中间元素的性能很差， 耗时为 O(n)
'''
q = deque()
q.append('eat')
q.append('sleep')
q.append('code')
print(q)
# >  deque(['eat', 'sleep', 'code'])
q.popleft()
q.popleft()
q.popleft()
q.popleft()  # >> IndexError: pop from an empty deque

# queue.Queue -- 为并行计算提供的锁语义
# 跟栈的 queue.LifoQueue 类似
