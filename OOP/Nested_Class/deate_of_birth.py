class Person:
    def __init__(self, name, dd, mm, yyyy):
        print('Person Objected Created')
        self.name = name
        self.dob = self.Dob(dd, mm, yyyy)

    def info(self):
        print('Student Name:'.format(self.name))
        self.dob.display()

    class Dob:
        def __init__(self, dd, mm, yyyy):
            print('Date of birth Object Created')
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def display(self):
            print('Date of birth: {}-{}-{}'.format(self.dd, self.mm, self.yyyy))

p = Person('Fatimah', 3, 4, 2010)
p.info()
#p.dob.display()