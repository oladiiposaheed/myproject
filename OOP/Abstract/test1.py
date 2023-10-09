from abc import abstractmethod
class Vehicle:
    @abstractmethod
    def getNoOfWheel(self):
        pass

class Bus(Vehicle):
    pass
class Auto(Vehicle):
    pass