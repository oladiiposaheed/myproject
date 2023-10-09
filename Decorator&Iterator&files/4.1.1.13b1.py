def outer(par):
    loc = par

    def inner():
        for i in loc:
            if i.isnumeric() in i:
                print('Cube of {} = {}'.format(i, i ** 3))
    return inner

var = [12, 3, -4, 5, 'python', -9, 'django', 3]
fun = outer(var)
fun()