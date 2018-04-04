# Auther: ZhengZhong,Jiang
# -*- coding:utf-8 -*-

import queue

q = queue.Queue(2)

q.put(11)
q.task_done()
q.put(22)
q.task_done()


print(q.get())

print(q.get())

q.join()


q = queue.LifoQueue()
q.put(11)
q.put(22)
print(q.get())
print(q.get())

q = queue.PriorityQueue()
q.put((1, 11))
q.put((0, 22))
print(q.get())
print(q.get())

q = queue.deque()
q.append(11)
q.append(22)
q.appendleft(33)
print(q.pop())
print(q.popleft())
