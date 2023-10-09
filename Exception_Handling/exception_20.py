try:
    print('Outer try block')
    try:
        print('Inner try block')
    except ZeroDivisionError:
        print('Inner except block')
    finally:
        print('Outer except block')
except:
    print('Outer except block')
finally:
    print('Outer finally block')