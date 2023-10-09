class Test:
    def sum(self, *a):
        result = 0
        for i in a:
            result = result + i
        print('Sum: {}'.format(result))

t = Test()
t.sum()
t.sum(12)
t.sum(12, 3)
t.sum(32, 2,4)
t.sum(54, 3, 9, 8, 12)