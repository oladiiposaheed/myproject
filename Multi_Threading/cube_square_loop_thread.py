import threading
import time


def square(num):
    print(" Calculate the square of the given number")
    for n in num:
        time.sleep(0.5)
        print('Square: {}'.format(n*n))

def cube(num):
    print(" Calculate the cube of  the given number")
    for n in num:
        time.sleep(0.5)
        print('Cube: {}'.format(n*n*n))

num = [4, 5, 6, 7, 1, 2]
t1 = time.time()
square(num)
cube(num)
t2 = time.time()

print('Total time taken by threads is: ',t2 - t1 )