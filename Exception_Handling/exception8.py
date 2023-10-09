try:
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    c = a/b
    print(c)
except (ZeroDivisionError, ValueError) as e:
    print('Exception Raised and its Description: ', e)