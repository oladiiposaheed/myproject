class Person:
    def __init__(self):
        print('Person Objected Created')
        self.dob = self.Dob()

    class Dob:
        def __init__(self):
            print('Date of birth Object Created')

p = Person()
