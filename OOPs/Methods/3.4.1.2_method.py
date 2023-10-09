class Classy:
    def other(self):
        print('Other')

    def method(self):
        print('Method')
        self.other()

obj = Classy()
obj.other()
print('*********')
obj.method()