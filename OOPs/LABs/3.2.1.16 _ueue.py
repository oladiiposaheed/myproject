import time


class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            return QueueError

class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0

que = SuperQueue()
que.put(1)
que.put('goat')
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get(), end='  ')
        time.sleep(3)
    else:
        print('Queue Empty')