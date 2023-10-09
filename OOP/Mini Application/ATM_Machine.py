import datetime
import sys
from random import randint
from abc import ABC, abstractmethod
class Util:
    history = []
    @staticmethod
    def generateAccountNumber():
        acc_number = ''
        for i in range(12):
            acc_number = acc_number + str(randint(0, 9))
        return acc_number

    @classmethod
    def addEntry(cls, msg):
        Util.history.append(msg)

class Account(ABC):
    BANKNAME = 'OSBank'
    def __init__(self, name, balance, min_balance):
        self.account_number = Util.generateAccountNumber()
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

class SavingsAccount(Account):
    def __init__(self, name, balance):
        super(SavingsAccount, self).__init__(name, balance, 0)

class CurrentAcount(Account):
    pass

print('Welcome to {}'.format(Account.BANKNAME))
print('Do You want to Open Savings or Current Account: ')
print('s - Savings Acoount\nc - Current Account')
option = input('Choose Your Option: ').lower()
no_attempt = 0
while option not in ['s', 'S', 'c', 'C']:
    if no_attempt >= 3:
        print('Sorry Maximum Number Attempts Reached, Try later')
        sys.exit()
    option = input('Please Select Valid Option[s | c]: ').lower()
    no_attempt += 1

if option == 's':
    name = input('Enter Customer Name: ')
    balance = float(input('Enter Initial Balance: '))
    while balance < 0:
        balance = eval(input('Your Initial Balance Should NOT be NEGATIVE, Please Enter Valid Value:  '))
    account = SavingsAccount(name, balance)
    Util.addEntry('{} - Savings Account Created with A/C No: {}'.format(datetime.datetime.now(), account.account_number))
    print('Congratulations! {}, You have Successfully Created Your Savings Account with A/C Number: {}'.format(account.name, account.account_number))

else:
    name = input('Enter Company Name: ')
    balance = float(input('Enter Initial Balance: '))
    while balance < 0:
        balance = eval(input('Your Initial Balance Should NOT be NEGATIVE, Please Enter Valid Value:  '))
    account = SavingsAccount(name, balance)
    print('Congratulations! {}, You have Successfully Created Your Current Account with A/C Number: {}'.format(
        account.name, account.account_number))