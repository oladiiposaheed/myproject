def outer(par):
    loc = par

    def inner():
        for i in range(loc + 1):
            print('Cube of {} = {}'.format(i, i ** 3))
    return inner

var = 5
fun = outer(var)
fun()