def calc(a, b):
    Sum = a + b
    Subt = a - b
    Mult = a * b
    Div = a / b
    Mod = a % b
    return [Sum, Subt, Mult, Div, Mod]
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
p, q, r, s, t = calc(a, b)
print('Sum: ',p)
print('Difference: ', q)
print('Product:', r)
print('Division:', s)
print('Modulo:', t)
print(type(p))
