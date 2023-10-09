def fun(n):
    for i in range(n):
        yield 'result', i

for v in fun(5):
    print('Value:',v)