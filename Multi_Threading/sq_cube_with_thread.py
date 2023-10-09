#import threading
import time
from threading import *

def double(nums):
    for n in nums:
        time.sleep(1)
        print(f'Double of {n}: {2*n}')

def square(nums):
    for n in nums:
        time.sleep(1)
        print(f'Square of {n}: {n**2}')

def cube(nums):
    for n in nums:
        time.sleep(1)
        print(f'Cube of {n}: {n**3}')

nums = [1, 2, 3, 4, 5, 6, 7]
begin = time.time()
t1 = Thread(target=double, args=(nums,))
t2 = Thread(target=square, args=(nums,))
t3 = Thread(target=cube, args=(nums,))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
end = time.time()
print('The Total Time Taken:', end - begin)