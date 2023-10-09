import time
from threading import *
def display():
    for i in range(10):
        print('Supporting Thread/Daemon Thread')
        time.sleep(1)
t = Thread(target=display)
t.setDaemon(True)
t.start()
print('End of Main')