def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
        print('Completion of finding factorial of', n)
    return result
n = int(input('Enter a positive integer: '))
print('{}! = {}'.format(n, factorial(n)))
#print('Factorial of 5 is', factorial(5))
#print('5! =',factorial(5))