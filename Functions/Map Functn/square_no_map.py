def square(n):
    return n * n
lst = [3, 1, 0, 5, -4, 10, 0.45]
op = list(map(square, lst))
print(type(op))
print(op)