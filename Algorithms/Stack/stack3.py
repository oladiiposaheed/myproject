stack = []

def push():
    if len(stack) == n:
        print('List is Full')
    else:
        element = input('Enter element into the list: ')
        stack.append(element)
        print(stack)

def pop():
    if not stack:
        print('Empty Stack')
    else:
        e = stack.pop()
        print('Removed element in the stack: ',e)
        print(stack)

n = int(input('Enter the limit of stack: '))
while True:
    print('Enter the Operation 1. Push 2. Pop 3. Quit: ')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('Enter a correct Operation!')

print(stack)