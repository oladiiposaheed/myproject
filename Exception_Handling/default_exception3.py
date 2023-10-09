try:
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print('Exception Raised and its Description: ', e)
except:
    print('Default Except Block:')