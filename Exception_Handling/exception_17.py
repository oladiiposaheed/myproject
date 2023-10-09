def f2():
    try:
        print('Hello World')
        return 200
    except:
        print('Except')
    finally:
        print('Finally')
f2()