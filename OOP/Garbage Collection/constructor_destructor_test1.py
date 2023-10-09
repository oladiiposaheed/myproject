import time


class Test:
    def __init__(self):
        print('Initialization Activity ...')

    def __del__(self):
        print('Fulfulling Last wish and perform cleanup activities...')

t = Test()
#t = None
#del t
time.sleep(5)
print('End of application')
t1 = Test()
t2 = Test()
time.sleep(10)
print('Complete end of the Application')