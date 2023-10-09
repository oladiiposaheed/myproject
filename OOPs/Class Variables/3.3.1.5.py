class A:
    varia = 1
    def __init__(self, val):
        A.varia = val

print(A.__dict__)
obj = A(2)
print(A.__dict__)
print(obj.__dict__)