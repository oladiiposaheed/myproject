a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the first number: '))
d = int(input('Enter the second number: '))
result = lambda a, b, c, d: a if a > b and a > c and a > d else b if b > c and b > d else c if c > d else d
print('The Maximum Number in {}, {}, {} and {} is {}'.format(a, b,c, d, result(a, b, c, d)))