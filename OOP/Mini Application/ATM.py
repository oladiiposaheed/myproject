from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('Sorry, Insufficient Funds')

    def printStatement(self):
        print('Account Balance: £{}'.format(self.balance))

    @abstractmethod
    def accountInfo(self):
        pass

class SavingsAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, 0) # min_balance = 0

    def __str__(self):
        return "{}'s Saving Account with Balance: £{}".format(self.name, self.balance)

class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, -1000)

    def __str__(self):
        return "{}'s Current Account with Balance: £{}".format(self.name, self.balance)

'''s = SavingsAccount('Saheed', 10000)
print(s)
s.deposit(5000)
s.printStatement()
s.withdraw(4500)
s.printStatement()
s.withdraw(12000)  '''
c = CurrentAccount('Saheed', 10000)
print(c)
c.deposit(5000)
c.printStatement()
c.withdraw(12000)
c.printStatement()
c.withdraw(4000)
c.printStatement()