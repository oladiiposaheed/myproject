class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()
print(d.isEmpty())
d.addFront('Fatimah')
#d.addFront(2)
#d.addFront(1)
d.addRear('Saheed')
#d.addRear(10)
#print(d.removeFront())
#print(d.removeRear())
print(d.removeFront() + ' ' + d.removeRear())
print(d.isEmpty())