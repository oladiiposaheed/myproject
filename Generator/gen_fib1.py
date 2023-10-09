import time


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
g = fib()
count = 1
for i in g:
    if count > 5:
        break
    print(i)
    count += 1
    time.sleep(1)