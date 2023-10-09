class ExampleClass:

    counter = 0
    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1

obj = ExampleClass()
obj1 = ExampleClass(2)
obj2 = ExampleClass(4)

print(obj.__dict__, obj.counter)
print(obj1.__dict__, obj1.counter)
print(obj2.__dict__, obj2.counter)