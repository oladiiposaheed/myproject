from random import seed, randint

seed()
data = [randint(-10, 10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)

a = [randint(2, 9) for i in range(10)]
print(a)