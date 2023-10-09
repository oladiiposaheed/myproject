try:
    print(10/0)
except ZeroDivisionError:
    print('Exception handled')
finally:
    print('Finally')