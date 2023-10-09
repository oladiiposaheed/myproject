class Classy:
    def method(self, par):
        print('Method: {}'.format(par))

obj = Classy()
obj.method([1,3,4])
obj.method(12)
obj.method(-1)
obj.method('Python is fun')
obj.method(44)
obj.method((32, 4, -43))