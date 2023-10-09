def elementwise_greater_than(L, thresh):
    lst = []
    for l in L:
        lst.append(l > thresh)
    return lst
print(elementwise_greater_than([1, 2, 3, 4], 2))


def elementwise_greater_than(L, thresh):
    return [l > thresh for l in L]

print(elementwise_greater_than([12, -2, 5, -10, 3, 4], 2))