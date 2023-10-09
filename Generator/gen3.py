def gen(n):
    i = 1
    while i <= n:
        yield i
        i += 1
v = gen(100000000000)
#print(v)
for i in v:
    print(i)