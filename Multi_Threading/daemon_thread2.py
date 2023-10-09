from threading import *
def display():
    print('Hello')

t = Thread(target=display)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())