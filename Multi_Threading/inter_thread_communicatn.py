import time
from threading import *

def producer():
    time.sleep(10)
    print('Producer thread producing items')
    print('Producer thread giving notification')
    e.set()

def consumer():
    print('Consumer thread consuming items')
    e.wait()
    print('Consumer thread got notification and consuming items')

t1 = Thread(target=producer)
t2 = Thread(target=consumer)

e = Event()
t1.start()
t2.start()
