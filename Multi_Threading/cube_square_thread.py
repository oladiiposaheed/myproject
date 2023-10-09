import time
import threading
from threading import Thread


def square(nums):
    for num in nums:
        print(f'\n{num}^2 = {num * num}')
        time.sleep(0.9)


def cube(nums):
    for num in nums:
        print(f'\n{num}^3 = {num * num * num}')
        time.sleep(0.9)


nums = [2, 3, 5, 8]
start = time.time()
square(nums)
cube(nums)
# end = time.time()
# print('Execution Time: {}'.format(end - start))

t1 = threading.Thread(target=square, args=(nums,))
t2 = threading.Thread(target=cube, args=(nums,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('Execution Time: {}'.format(end - start))
