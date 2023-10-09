def gen():
    yield 'A'
    yield 'B'
    yield 'Python'
g = gen()
for i in g:
    print(i)