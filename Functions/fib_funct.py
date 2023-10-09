def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input('Enter a Positive Integer: '))
for i in range(n + 1):
    print('Fibinocci series of {} = {}'.format(i,fib(i)))

a = 0
for i in range(4):
    n = int(input('Enter a Positive Integer: '))
    #a.append(n)
    a += n
print(a)