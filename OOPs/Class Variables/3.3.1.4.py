class ExampleClass:

    __counter = 0
    def __init__(self, val=1):
        self.__first = val
        ExampleClass.__counter += 1

obj = ExampleClass()
obj1 = ExampleClass(2)
obj2 = ExampleClass(4)

print(obj.__dict__, obj._ExampleClass__counter)
print(obj1.__dict__, obj1._ExampleClass__counter)
print(obj2.__dict__, obj2._ExampleClass__counter)