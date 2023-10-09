import time
from threading import *

def display(num):
    for i in range(num):
        print('The Child Thread {}: {}'.format(i, current_thread().getName()))
        time.sleep(1)

num = int(input('Enter Positive Integer: '))
name = input('Enter the name of the thread: ')
t = Thread(target=display, args=(num,))
t.setName(name)
t.start()