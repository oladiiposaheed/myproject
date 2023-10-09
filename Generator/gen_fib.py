import time


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
g = fib()
for i in g:
    if i > 100:
        break
    print(i)
    time.sleep(1)