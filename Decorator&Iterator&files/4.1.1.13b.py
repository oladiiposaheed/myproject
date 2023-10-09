def outer(par):
    loc = par

    def inner():
        for i in loc:
            print('Cube of {} = {}'.format(i, i ** 3))
    return inner

var = [12, 3, -4, 5, 0, -9, 3]
fun = outer(var)
fun()