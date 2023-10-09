class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        #self.odometer_reading = mileage
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = '{} {} {}'.format(self.year, self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        if mileage >= 0:
            print('This car has {} miles on it.'.format(self.odometer_reading))
        else:
            print("The car cannot have NEGATIVE miles")

class ElectricalCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        #self.battery_size = 75
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __int__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print('This car has a {} - kWh battery.'.format(self.battery_size))


mileage = float(input('Enter the mile that the car can take: '))
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_used_car = Car('subaru', 'outbreak', 2015)
print(my_used_car.get_descriptive_name())

my_tesla = ElectricalCar('tesla', 'model s', 2020)

my_used_car.update_odometer(mileage)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#my_new_car.read_odometer()
#my_new_car.odometer_reading = 23
#my_new_car.update_odometer(25)
my_new_car.update_odometer(mileage)
my_new_car.read_odometer()

print('*'*40)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()