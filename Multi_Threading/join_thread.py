import time
from threading import *
def display():
    for i in range(10):
        print('Python Thread')
        time.sleep(2)

t = Thread(target=display)
t.start()
#t.join() # Main thread will wait until completing child thread
t.join(5)

for i in range(10):
    print('Django Thread')