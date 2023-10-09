from threading import *
class Test:
    def disp(self):
        for i in range(10):
            print('Good Morning')
obj = Test()
t = Thread(target=obj.disp)
t.start()
for i in range(10):
    print('Good Evening')