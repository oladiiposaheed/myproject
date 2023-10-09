try:
    print(10/0)
except ZeroDivisionError:
    print('Exception handled')

try:
    print('Try')
except:
    print('except')
finally:
    print('Finally')