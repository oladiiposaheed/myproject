def f3():
    try:
        t = int(input('Enter time is seconds: '))
        g = int(input('Enter acceleration due to gravity: '))
        u = int(input('Enter initial velocity: '))
        if t < 0 and g < 0 and u <= 0:
            print('Please Enter a positive integer for time and acceleration due to gravity!!!')
        else:
            h = u*t + 0.5*g*t**2
        return 'Maximum Height of the object: {}'.format(h)
    except:
        print('Except')
    finally:
        print('Good Attempt')
f3()