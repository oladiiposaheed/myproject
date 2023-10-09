queue = []

def enqueue():
    element = int(input('Enter an element to the queue: '))
    queue.append(element)
    print(element, 'is added to the queue')

def dequeue():
    if not queue:
        print('Queue is empty')
    else:
        remove = queue.pop(0)
        print('Removed Element:', remove)

def display():
    print(queue)

while True:
    print('Select the operation 1. Add 2. Remove 3. Show Result 4. Quit')
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
        print('Enter the correct operation!')
print(queue)
