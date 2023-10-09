from threading import *
print(current_thread().isDaemon())   #False
print(current_thread().daemon)  #False
current_thread().setDaemon(True)
print(current_thread().isDaemon())
