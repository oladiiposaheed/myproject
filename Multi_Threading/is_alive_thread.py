import time
from threading import *

def display():
    print(f'{current_thread().getName()} Started')
    time.sleep(3)
    print(f'{current_thread().getName()} Ended')

t1 = Thread(target=display, name='ChildThread-1')
t2 = Thread(target=display, name='ChildThread-2')
t1.start()
t2.start()
print('{} is Alive: {}'.format(t1.getName(), t1.is_alive()))
print('{} is Alive: {}'.format(t2.getName(), t2.is_alive()))