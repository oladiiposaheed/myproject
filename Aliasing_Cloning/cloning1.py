l1 = [10, 20, 30, 40]
l2 = l1.copy()
print(id(l1))
print(id(l2))
if id(l1) == id(l2):
    print(True)
else:
    print(False)