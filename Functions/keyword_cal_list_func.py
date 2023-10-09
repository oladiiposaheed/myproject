def cal(a, b):
    Sum = a + b
    Diff = a - b
    Mult = a * b
    return [Sum, Diff, Mult]
#result = cal(a = 5, b = 9)
result = cal(b = 9, a = 5)
print(result)
for i in result:
    if i % 2:
        print(i)