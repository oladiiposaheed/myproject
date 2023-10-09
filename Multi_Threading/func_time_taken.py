import time


def double(nums):
    for num in nums:
        time.sleep(1)
        print('Double: {}'.format(2*num))

def square(nums):
    for num in nums:
        time.sleep(1)
        print('Square: {}'.format(num*num))

nums = [1,2,3,4,5,6,7]
begin = time.time()
double(nums)
end = time.time()
square(nums)
print('Total Time taken: {}'.format(end - begin))