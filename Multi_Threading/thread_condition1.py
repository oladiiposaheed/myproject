import time
from threading import *
def consumer():
    c.acquire()
    print('Consumer waiting for update')
    c.wait()
    print('Consumer Got Notification From Producer and Consuming item')
    i = 5
    while i:
        print(i, end=' ')
        i -= 1
        time.sleep(2)

def producer():
    c.acquire()
    print('Producer producing items')
    c.notify()
    k = 0
    while True:
        print('Welcome',end=' ')
        time.sleep(3)
        k += 1
        if k == 5:
            break
    print('Producer Giving Notification')
    c.release()

c= Condition()
t1 = Thread(target=consumer)
t2 = Thread(target=producer)

t1.start()
t2.start()