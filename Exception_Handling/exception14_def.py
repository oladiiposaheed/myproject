def f1():
    try:
        print('Hello')
        a = 10/0
        print(a)
        return 10
    except ZeroDivisionError:
        print('Except')
    finally:
        print('Finally')
print(f1())