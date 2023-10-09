import time
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
num = int(input('Enter Positive Integer: '))
for j in range(3):
    fibs = list(fibonacci(num))
    print(fibs)
    time.sleep(2)