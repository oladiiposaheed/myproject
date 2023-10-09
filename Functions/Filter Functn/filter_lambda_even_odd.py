lst = [0, 1, 22, 9, 32, 40, 5, 10]
even = list(filter(lambda n: n % 2 == 0, lst))
odd = list(filter(lambda n: n % 2, lst))
print(even)
print(odd)