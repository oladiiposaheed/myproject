class Animal:
    legs = int(input('Enter the leg: '))
    @classmethod
    def walk(cls, name):
        if cls.legs == 4:
            print('{} walks with {} legs'.format(name, cls.legs))
        else:
            print('{} does not walk with 4 legs'.format(name))
name = input('Enter the Name of the Animal: ')
Animal.walk(name.title())