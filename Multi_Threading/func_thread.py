from threading import *
import time

def double(nums):
    for num in nums:
        time.sleep(1)
        #print('Double: {}'.format(2*num))
        print('Double:',2*num)

def square(nums):
    for num in nums:
        time.sleep(1)
        print('Square: {}'.format(3*num))
        #print('Square:',num*num)

nums = [1,2,3,4,5,6,7]
begin = time.time()
t1 = Thread(target=double, args=('nums',))
t2 = Thread(target=square, args=('nums',))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('Total Time taken: {}'.format(end - begin))