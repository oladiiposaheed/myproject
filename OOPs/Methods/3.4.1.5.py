class Classy:
    varia = 1
    def __init__(self):
        self.var = 4

    def method(self):
        pass

    def __hidden(self):
        print('Love Python')

obj = Classy()
print(obj.__dict__)
print(obj.var)
print(obj.varia)
print(Classy.varia)
print(Classy.__dict__)
obj._Classy__hidden()

try:
    Classy.var
except:
    print('Error')