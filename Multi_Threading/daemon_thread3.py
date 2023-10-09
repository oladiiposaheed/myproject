import time
from threading import *
def display2():
    print('Display 1 Job')
    time.sleep(100)

def display1():
    print('Display 2 Job')
    t2 = Thread(target=display2)
    #print(t2.isDaemon())
    print('t2 Thread: {}'.format(t2.isDaemon()))
t1 = Thread(target=display1) # Parent of t1 is mainthread which is non-daemon
#t1.setDaemon(True)
t1.start()
print('t1 Thread: {}'.format(t1.isDaemon()))