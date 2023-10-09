queue = []

def enqueue():
    element = int(input('Enter an element to the queue: '))
    queue.insert(0, element)
    print(element, 'has been added')
    print(queue)

def dequeue():
    if not queue:
        print('Empty Queue')
    else:
        remove = queue.pop()
        print(remove, 'is removed')
        print(queue)

def display():
    print(queue)

while True:
    print('Please Enter Your Choice Operation: 1 to add 2 to remove 3 to display 4 to quit: ')
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print('Incorrect input, enter correct operation')

print(queue)