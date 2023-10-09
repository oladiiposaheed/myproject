from abc import abstractmethod, ABC
class Vehicle(ABC):
    @abstractmethod
    def getNoOfWheel(self):
        pass

class Bus(Vehicle):

    def getNoOfWheel(self):
        return 6

class Auto(Vehicle):
    def getNoOfWheel(self):
        return 3

b = Bus()
a = Auto()
#print(b.getNoOfWheel())
if not b.getNoOfWheel():
    print('The Vehicle is a Bus')
    print(b.getNoOfWheel())
else:
    print('The vehicle is an auto')
    print(a.getNoOfWheel())