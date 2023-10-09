def f3():
    try:
        num = int(input('Enter an integer: '))
        if num < 0:
            print('Please Enter a positive integer!!!')
        else:
            num1 = num * 2
        return 'Result: {}'.format(num1)
    except:
        print('Except')
    finally:
        print('Good Attempt')
print(f3())