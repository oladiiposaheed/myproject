class One:
    def do_it(self):
        print('do_it from one')

    def dosomething(self):
        print('Do Something')

    def doanything(self):
        self.do_it()
        self.dosomething()

class Two(One):
    def do_it(self):
        print('do_it from two')

one = One()
two = Two()
one.doanything()
print()
two.doanything()