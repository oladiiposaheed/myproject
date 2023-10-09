a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
result = lambda a, b: a + b
print('{} + {} = {}'.format(a, b, result(a, b)))