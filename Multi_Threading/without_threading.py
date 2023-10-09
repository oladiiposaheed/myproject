import time


def double(nums):
    for n in nums:
        time.sleep(1)
        print(f'The Double of {n} = {2*n}')

def square(nums):
    for n in nums:
        time.sleep(1)
        print(f'The Square of {n} = {n*n}')

nums = [1, 2, 3, 4, 5, 6, 7]
begin = time.time()
double(nums)
square(nums)
end = time.time()
print('Total Time taken:', end - begin)