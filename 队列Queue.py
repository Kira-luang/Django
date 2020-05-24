# 1.队列的特点以及应用场景
'''
自带锁机制,会阻塞,获得和归还时候具有原子性
应用场景:当限定有限个资源时,并且需要循环利用这些有限资源的时候(线程安全性)
'''

# 2.队列的使用
'''
from queue import Queue
queue = Queue(1)
queue.put('data')
queue.get()
'''

# 3.计算队列大小
'''
queue.qsize()
'''
print('test1')
