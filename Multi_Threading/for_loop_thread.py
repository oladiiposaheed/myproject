import time
from threading import *
def display():
    time.sleep(2)
    for i in range(10):
        print('Python Thread Executed by:', current_thread().getName())

t = Thread(target=display)
#t.start()

for i in range(10):
    print(10.0)
    print('Django Thread Executed by:', current_thread().getName())
t.start()