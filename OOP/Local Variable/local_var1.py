class Test:
    def m1(self):
        x = 50
        Test.a = 100
        print(Test.a)
        print(x)
    def m2(self):
        b = 200
        print(b)
        print(self.a)
        #print(x)  # impossible to access a bcos it is a local variable
t = Test()
t.m1()
t.m2()
#print(x) impossible to access a bcos it is a local variable