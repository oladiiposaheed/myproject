import time
def Cloning(a):
    b = a[:]
    return b

#b = Cloning(a)
a = []
for i in range(5):
    a.append(i)
    b = Cloning(a)
print(a)
print(b)
