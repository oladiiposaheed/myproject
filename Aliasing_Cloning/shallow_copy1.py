import copy
l1 = [1, 2, [3,5], 4]
l2 = copy.copy(l1)
print(l2)
print(l1)
print()
print(id(l1), id(l2))