def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

lst = [13, 4, -6, 3, 10, 34, 9]
#op = filter(even, lst)
op = list(filter(even, lst))
print(type(op))
print(op)