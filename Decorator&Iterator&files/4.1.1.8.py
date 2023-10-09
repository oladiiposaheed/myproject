the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
#print(the_list)
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
#print(list(the_generator))

for v in the_list:
    print(v, end=' ')
print()

for u in the_generator:
    print(u, end=' ')
print()