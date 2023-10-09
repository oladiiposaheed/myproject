from threading import *

from threading import *
def display():
    for i in range(10):
        print('Good Morning: Parent')

t = Thread(target=display) # Creating thread object for the display
t.start()  #starting of a thread
for i in range(10):
    print('Good Morning: Student')