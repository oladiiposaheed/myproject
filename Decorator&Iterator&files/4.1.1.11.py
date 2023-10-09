l1 = [x for x in range(5)]
l2 = list(map(lambda x: 2**x, l1))
print(l2)

for x in map(lambda x: x * x, l2):
    print(x, end=' ')
print()