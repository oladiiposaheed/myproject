def factorial(n):
    print('Finding factorial of',n)
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result
n = int(input('Enter a Positive Integer: '))
if n < 0:
    print('You entered wrong input')
else:
    for i in range(n + 1):
        print('{}! = {}'.format(i, factorial(i)))