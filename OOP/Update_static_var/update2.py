class Test:
    a = 10  #static var
    b = 20  #static var
    def m1(self):
        self.b = 888  # instance var
        Test.a = 999 #update static var
t = Test()
t.m1()
print(Test.a) # a = 10
print(t.a) # a = 999
print(Test.b)  ##static var
print(t.b)  #instance var