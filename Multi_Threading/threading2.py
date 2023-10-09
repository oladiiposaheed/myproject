from threading import *
def display():
    for i in range(10):
        print('Python Thread Executed by:', current_thread().getName())

def display1():
    for i in range(10):
        print('PHP Thread Executed by:', current_thread().getName())

def display2():
    for i in range(10):
        print('Java Thread Executed by:', current_thread().getName())

t1 = Thread(target=display)
t2 =Thread(target=display1)
t3 = Thread(target=display2)
t1.start()
t2.start()
t3.start()

for i in range(10):
    print('Threading Executing by:', current_thread().getName())