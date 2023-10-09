class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
print(s.push(1))
print(s.push(22))
print(s.push('Three'))
print(s.peek())
print(s.pop())
print(s.pop())
print(s.size())