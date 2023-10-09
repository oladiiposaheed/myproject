import time
from threading import *
def test():
    print('Child Thread')

for i in range(5):
    t = Thread(target=test) # Child Thread reference = t
    t.start()
    time.sleep(1)
    print('Main Thread Identification Number:',(current_thread().ident))
    print('Child Thread Identification Number:',(t.ident))