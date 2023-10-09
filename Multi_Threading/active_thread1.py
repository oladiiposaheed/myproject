import time
from threading import *
def display():
    print('{} Started'.format(current_thread().getName())) # get and start the current thread name
    time.sleep(3)
    print('{} Ended'.format(current_thread().getName()))  # end the current thread name
print('The Number of active threads: {}'.format(active_count()))
t1 = Thread(target=display, name='ChildThread-1')
t2 = Thread(target=display, name='ChildThread-2')
t3 = Thread(target=display, name='ChildThread-3')
t1.start()
t2.start()
t3.start()
print('The Number of active threads: {}'.format(active_count()))
time.sleep(5) # main thread sleep for 5secs
print('The Number of active threads: {}'.format(active_count()))