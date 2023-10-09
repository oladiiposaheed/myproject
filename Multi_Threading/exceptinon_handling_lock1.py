import time
from threading import *
l = Lock()
def wish(name):
    l.acquire()
    try:
        print('{} got Lcok'.format(current_thread().getName()))
        time.sleep(5)
        for i in range(7):
            print('Good Morning:', end='')
            time.sleep(2)
            print(name)
        print(100/0)
        print('{} releasing Lock'.format(current_thread().getName()))
        time.sleep(5)
    except:
        print('Exception Raised while Executing this Thread')
    finally:
        l.release()

t1 = Thread(target=wish, args=('Fatimah',), name='{} Thread'.format('Fatimah'))
t2 = Thread(target=wish, args=('Saheed',), name='{} Thread'.format('Saheed'))
t3 = Thread(target=wish, args=('Ahmad',), name='{} Thread'.format('Ahmad'))
t4 = Thread(target=wish, args=('Peace',), name='{} Thread'.format('Peace'))
t1.start()
t2.start()
t3.start()
t4.start()