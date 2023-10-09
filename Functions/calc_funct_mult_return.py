def calc(a, b):
    Sum = a + b
    Subt = a - b
    Mult = a * b
    Div = a / b
    Mod = a % b
    return Sum, Subt, Mult, Div, Mod
    #return [Sum, Subt, Mult, Div, Mod]
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
result = calc(a, b)
print(result)
for i in result:
    print(i)