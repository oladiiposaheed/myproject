class Account:
    def __init__(self, intial_balance):
        self.__balance = intial_balance

    def getBalance(self):
        #validation authentication
        return self.__balance

    def deposit(self, amount):
        # validation authentication
        self.__balance += amount

    def withdraw(self, amount):
        #validation authentication
        self.__balance -= amount
        