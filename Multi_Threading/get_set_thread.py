from threading import *
print(current_thread().getName())
current_thread().setName('Python Thread')
print(current_thread().getName())