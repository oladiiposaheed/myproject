def cal(a, b):
    Sum = a + b
    Diff = a - b
    Mult = a * b
    return [Sum, Diff, Mult]
#result = cal(a = 5, b = 9)
result = cal(9, b = 5)
print(result)
for i in result:
    if i % 2:
        print(i)

def add(a, b, c, d, e):
    print(a, b, c, d, e)
    print(a, e, c, d, b)
    print(b+a)
    print(a - c)
add(20, 10, d = 2, c = 0, e = 7)

def greet(name, msg):
    print('Hello', name, msg)
greet('Saheed', msg='Good morning')