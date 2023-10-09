try:
    print('Try')
    print(10/0)
except ZeroDivisionError:
    print('Cannot be divided by Zero')
finally:
    print('Finally')