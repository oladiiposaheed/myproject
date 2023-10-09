# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the first number: "))
number5 = int(input("Enter the second number: "))

largest = number1
if number2 > largest:
    largest = number2

if number3 > largest:
    largest = number3

if number4 > largest:
    largest = number4

if number5 > largest:
    largest = number5

print('Largest Number is', largest)


