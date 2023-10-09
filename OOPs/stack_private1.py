class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)
        return self.__stack_list

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

obj = Stack()
print(obj.push([21, 32]))
print(obj.push(20))
print(obj.push(19))
print()
print(obj.pop())
print(obj.pop())
print(obj.pop())
