def display(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    print(args)
    for k, v in kwargs.items():
        print('{} = {}'.format(k, v))
display(10, 20, 34, name='Ola', marks=90, roll=12, id = '002')