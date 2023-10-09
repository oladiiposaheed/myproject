class Test:
    def __init__(self, x):
        print('Address of object of self', id(self))
        print('Id object', id(x))

t = Test(x = 10)
print(id(t))