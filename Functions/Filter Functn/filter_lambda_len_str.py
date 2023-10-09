t = ('Python', 'Jug', 'Django', 'PHP', 'JavaScript', 'Golang', 'Programming')
op = tuple(filter(lambda n: len(n) > 7, t))
print(op)