def factorial(n):
    result = 1
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result
n = int(input('Enter an integer value: '))
result = factorial(n)
print('The Factorial of {} = {}'.format(n, result))