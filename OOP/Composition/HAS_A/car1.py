class Engine:

    def __init__(self):
        self.power = '125kw'
    def useEngine(self):
        print('Engine Specific Functionality')

class Car:
    def __init__(self):
        self.engine = Engine()

    def useCar(self):
        print('Car Required Engine Functionlity')
        self.engine.useEngine()
        print(self.engine.power)

c = Car()
c.useCar()