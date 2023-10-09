def power(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

t = [x for x in power(10)]
print(t)
