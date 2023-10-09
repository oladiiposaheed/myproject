try:
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    c = a/b
    print(c)
except BaseException as e:
    print('Exception Raised: ',e)