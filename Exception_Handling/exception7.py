try:
    a = int(input('Enter First Number: '))
    b = int(input('Enter Second Number: '))
    c = a/b
    print(c)
except BaseException as e:
    print('BaseException raised:', e.__class__.__name__)
except ZeroDivisionError:
    print('ZeroDivisionError raised')
except ValueError:
    print('ValueError raised')