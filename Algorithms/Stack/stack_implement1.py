class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        '''Push the element to the last index in the list
        :return: None
        '''
        self.items.append(item)
    def pop(self):
        '''To remove the last item in the list and return None'''
        self.item.pop()

    def peek(self):
        '''Last element'''
        if self.item:
            return self.item[-1]
        else:
            retur n None

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

    def isempty(self):
        '''Check whether the stack is empty or not and return Bool value'''
        if self.item == []:
            return True
        else:
            return  False
if __name__ == "__main__":
    stack = Stack()
    stack.push('1')
    stack.push('2')
    print(stack.size())
    print(stack.peek())