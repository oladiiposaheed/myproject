class Classy:
    varia = 2
    def method(self):
        print('{} {}'.format(self.varia, self.var))
        print('{} {}'.format(Classy.varia, self.var))

obj = Classy()
obj.var = 12
obj.method()