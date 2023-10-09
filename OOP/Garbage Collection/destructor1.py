import time


class Test:
    def __init__(self):
        print('Initialization Activity ...')

    def __del__(self):
        print('Fulfulling Last wish and perform cleanup activities...')

t1 = Test()
t2 = t1
t3 = t2
del t1
time.sleep(5)
print('Object not yet destroyed after deleting t1')
del t2
time.sleep(10)
print('Object not yet destroyed after deleting t2')
del t3
time.sleep(10)
print('The last reference also removed now object eligible for gc')
