class Claculator:
    def m1(self):
        def calc(a, b):
            print('Scientific Calculator')
            print('-'*22)
            print('{} + {} = {}'.format(a, b, a+b))
            print('{} - {} = {}'.format(a, b, a-b))
            print('{} * {} = {}'.format(a, b, a*b))
            print('{} / {} = {}'.format(a, b, a/b))
            print('{} % {} = {}'.format(a, b, a%b))
            print()
        calc(12, 9)
        calc(34, 78)
        calc(1000, 2000)
c = Claculator()
c.m1()