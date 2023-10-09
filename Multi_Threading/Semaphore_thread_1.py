import time
from threading import *
s = Semaphore()
def wish(name):
    s.acquire()
    for i in range(10):
        print('Good Morning:', end='')
        time.sleep(2)
        print(name)
    s.release()

t1 = Thread(target=wish, args=('Fatimah',))
t2 = Thread(target=wish, args=('Saheed',))
t3 = Thread(target=wish, args=('Jumai',))
t4 = Thread(target=wish, args=('Ahmad',))
t5 = Thread(target=wish, args=('Abdullahi',))
t6 = Thread(target=wish, args=('Uthman',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()