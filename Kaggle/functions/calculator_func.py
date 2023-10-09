def least_difference(a, b, c):
    diff1 = a - b
    diff2 = b - c
    diff3 = a - c
    return min(diff1, diff2, diff3)
print(least_difference(1, 10, 100),
      least_difference(1, 10, 10),
      least_difference(5, 6, 29))
