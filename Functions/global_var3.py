def f1():
    global a
    a = 999
    print(a)


def f2():
    global a
    a = 120
    print(a)


f1()
f2()
print(a)