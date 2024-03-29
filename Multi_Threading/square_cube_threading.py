import threading

def print_cube(num):
    print('Cube of {}: {}'.format(num, num*num*num))

def print_square(num):
    print('Square of {}: {}'.format(num, num*num))

t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()
# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

print('Done')