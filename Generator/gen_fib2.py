import time


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
gen = fib()
count = 1
n = int(input('Enter an integer: '))
if n < 0:
    print('Input cannot be negative integer')
    print('Try any positive integer')
elif n == 0:
    print('Zero not allowed')
    print('Try any positive integer greate than zero')
else:
    print('WELCOME TO FIBINOCCI CALCULATOR')
    print('-' * 31)
    print('', end=' | ')
    for i in gen:
        if count > n:
            break
        print(i, end=' | ')
        count += 1
        time.sleep(1)
    print('\nGOOD BYE!')
