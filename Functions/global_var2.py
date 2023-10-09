a = 12
def f1():
    global a
    a = 999   # a = 12 is replaced with 999
    print(a)

def f2():
    print(a)

f1()
f2()
print(a)