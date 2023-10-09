from threading import *
def display():
    print('The Child Thread Name: {}'.format(current_thread().getName()))

t = Thread(target=display)
t.setName('Fatima Thread')
t.start()

t = Thread(target=display)
t.setName('Halimah Thread')
t.start()