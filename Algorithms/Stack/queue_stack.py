import queue
stack = queue.LifoQueue()
#stack = queue.LifoQueue(3)
stack.put(20)
stack.put(-32)
stack.put(0)
stack.put('Django')
print(stack)
print(stack.get())
print(stack.get(timeout=1))