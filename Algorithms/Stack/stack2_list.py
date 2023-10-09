stack = []

def push():
    elem = input('Please Enter the element: ')
    stack.append(elem)
    print(stack)


def pop():
    if not stack:
        print('Empty Stack')
    else:
        p = stack.pop()
        print('Removed Element: ', p)
        print(stack)

while True:
    print('Select the operation of your choice 1.push 2.pop 3.quit: ')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('Please Enter Correct Operation!')

print(stack)