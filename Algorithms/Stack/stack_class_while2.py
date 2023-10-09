class EmptyStackError(Exception):
    pass
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            raise EmptyStackError("Empty Stack!")
        return self.items.pop()

    def peek(self):
        if self.items == []:
            raise EmptyStackError("Empty Stack!!")
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def result(self):
        print(self.items)

s = Stack()

print('Select Your Best Operation!')
while not False:
    print('1: Push 2: Pop 3: Peek 4: Size 5: Result 6: Quit')

    choice = int(input('Please enter your choice: '))
    if choice == 1:
        element = int(input('Please enter the element to the stack: '))
        s.push(element)
    elif choice == 2:
        element = s.pop()
        print(element, 'is removed')
    elif choice == 3:
        print(s.peek(), 'is at the top element in the stack')
    elif choice == 4:
        print('The stack length is', s.size())
    elif choice == 5:
        s.result()
    elif choice == 6:
        break
    else:
        print('Wrong Input!!!, Please Enter Operation')
s.result()