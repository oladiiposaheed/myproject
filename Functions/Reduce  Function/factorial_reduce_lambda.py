from functools import *
n = int(input('Enter an integer: '))
op = reduce(lambda x, y: x * y, range(1, n + 1))
print(op)