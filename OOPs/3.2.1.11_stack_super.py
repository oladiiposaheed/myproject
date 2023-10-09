import time


class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum = self.__sum + val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum = self.__sum - val
        return val

stack_obj = AddingStack()

for i in range(7):
    stack_obj.push(i)
    print(stack_obj.get_sum(), end=' ')
    time.sleep(3)
print('\nSum:',stack_obj.get_sum())

for i in range(5):
    print(stack_obj.pop(), end=' ')
    time.sleep(3)