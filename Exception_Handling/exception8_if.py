try:
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    c = a/b
    print(c)
except (ZeroDivisionError, ValueError) as e:
    #print('Exception Raised and its Description: ', e)
    if type(e) == ZeroDivisionError:
        print('Please Enter Zero as denominator')
    else:
        print('You have entered string instead of integer')