import sys
class Customer:
    '''Customer class to describe bank operations'''
    bankname = 'HALAL ISLAMIC BANK'
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Balance After Deposit: #{}'.format(self.balance))

    def withdraw(self, amount):
        if self.balance == 0:
            print('You Balance is #{}'.format(self.balance))
        else:
            if self.balance > 0 or amount > self.balance:
                print('Insufficient Funds, You cannot perform this operation')
                print('Your Balance is #{}'.format(self.balance))
                sys.exit()
            self.balance = self.balance - amount
            print('Balance: #{}'.format(self.balance))

print('Welcome to {}'.format(Customer.bankname))
name = input('Enter Your Name: ')
c = Customer(name)
while True:
    print('d - Deposit\nw - Withdraw\ne - Exit')
    option = input('Choice Your Option: ')
    if option == 'd' or option == 'D':
        amount = float(input('Enter Amount to Deposit: '))
        c.deposit(amount)
    elif option == 'w' or option == 'W':
        amount = float(input('Enter the Amount to Withdraw: '))
        while amount % 500 != 0:
            print('Amount Should be Multiple of 500')
            amount = float(input('Enter Amount to Deposit: '))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks For Banking With Us')
        sys.exit()
    else:
        print('Invalid Option, Please Provide Correct Option')