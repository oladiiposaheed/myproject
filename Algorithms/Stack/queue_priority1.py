import queue
q = queue.PriorityQueue()
q.put(10)
q.put(32)
q.put(15)
q.put(90)
q.put(1)
print(q)
print(q.get())
print(q.get())
print(q.get())