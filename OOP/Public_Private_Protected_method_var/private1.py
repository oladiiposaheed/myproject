class Test:
    def __int__(self):
        self.__x = 14

    def __m1(self):
        print('Private m1 method')

    def m2(self):
        print(self.__x)
        self.m1()
t = Test()
#print(t.__x)
t.m1()
#t.m2()