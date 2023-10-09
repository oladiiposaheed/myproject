try:
    print('Try')
    print(12/0)
except ValueError:
    print('Except')
finally:
    print('Finally')