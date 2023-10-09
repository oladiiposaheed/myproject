class Goat:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + ' rolled over!')

my_goat = Goat('Willie', 6)
print("My goat's name is " + my_goat.name.title() + ".")
print("My dog is " + str(my_goat.age) + " years old.")
my_goat.sit()       