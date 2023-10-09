class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] # if empty return True

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue(2)
q.enqueue(32)
print(q.dequeue())
q.enqueue('Python')
print('The length of the queue list is',q.size())
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())