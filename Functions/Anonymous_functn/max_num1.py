a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
result = lambda a, b: a if a > b else b
print('The bigger number is', result(a, b))
