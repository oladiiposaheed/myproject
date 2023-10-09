from threading import *

def Sum():
    s = 0
    for i in range(5):
        s += i
        print(s)

t = threading.Thread(target=Sum)
t.start()

for i in range(10):
    print(i)