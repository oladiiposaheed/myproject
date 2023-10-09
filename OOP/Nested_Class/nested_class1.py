class Outer:
    def __init__(self):
        print('Outer Class Object Creation')
    class Inner:
        def __init__(self):
            print('Inner Class Object Creation')

        def m1(self):
            print('Inner Class Method')
#o = Outer()
#i = o.Inner()
#i.m1()
Outer().Inner().m1()