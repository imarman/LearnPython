from collections import deque
from queue import LifoQueue
'''
    deque 类实现了一个双端队列，支持在 O(1) 时间（非均摊）从两端添加和移动元素
    因为双端队列支持从两端支持添加和删除元素，既可以作为队列也可以作为栈
    collections.deque 是实现 栈 的绝佳选择
'''
s = deque()
s.append('eat')
s.append('sleep')
s.append('code')
# print(s)
# >  deque(['eat', 'sleep', 'code'])

'''
    queue.LifoQueue 这个位于 python 标准库的种的栈实现是同步的，提供了锁语义来支持多个并发的生产者和消费者
'''
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')
s.get()  # code
s.get()  # sleep
s.get_nowait()
s.get()  # 空的

# 阻塞，永远停在这里
s.get()

