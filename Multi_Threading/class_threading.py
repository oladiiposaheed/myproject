from threading import *
class MyThread(Thread):
    def run(self) -> None:
        for i in range(10):
            print('Good Morning Students')

t = MyThread()   # Main Thread creating child Thread object
t.start() #Main Thread starts child thread

for i in range(10):
    print('Good Evening Parent')
