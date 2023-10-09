class Test:
    count = 0
    def __init__(self):
        Test.count += 1

    @classmethod
    def getNoOfObject(cls):
        #print('The Total Number of Object Created: {}'.format(Test.count))
        print('The Total Number of Object Created: {}'.format(cls.count))

t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
Test.getNoOfObject()