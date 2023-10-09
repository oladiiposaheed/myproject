class EmptyStackError(Exception):
    pass

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        print(element,'is added to the stack')
        return self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise EmptyStackError('Stack is Empty')
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise EmptyStackError('Stack is Empty')
        return self.items(self.items[-1])

    def size(self):
        return len(self.items)

    def result(self):
        print(self.items)

print('********************************************')

if __name__ == "__main__":
    s = Stack()

while not False:
    print('Select Your Best Operation!')
    print('1: Push 2: Pop 3: Peek 4: Size 5: Result 6: Quit')

    choice = int(input('Please enter your choice: '))
    if choice == 1:
        element = int(input('Please enter the element to the stack: '))
        s.push(element)
    elif choice == 2:
        e = s.pop()
        print(e, 'is removed')
    elif choice == 3:
        print(s.peek(), 'is the top element in the stack')
    elif choice == 4:
        print('The stack length is', s.size())
    elif choice == 5:
        s.result()
    elif choice == 6:
        break
    else:
        print('Wrong Input!!!, Please Enter Operation')

