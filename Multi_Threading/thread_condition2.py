import time
from threading import *
import random

items = []
def producer():
    while True:
        c.acquire()
        item = random.randint(1, 100)
        print('Producer producing item:',item)
        items.append(item)
        print('Producer Giving Notification to the Consumer')
        time.sleep(3)
        c.notify()
        c.release()
        time.sleep(5)

def consumer():
    while True:
        c.acquire()
        print('Consumer Waiting for Update from Producer')
        #time.sleep(3)
        c.wait()
        while len(items) != 0:
            print('Consumer consumes the item:', items.pop())
        c.release()
        time.sleep(5)

c = Condition()
t1 = Thread(target=consumer)
t2 = Thread(target=producer)

t1.start()
t2.start()