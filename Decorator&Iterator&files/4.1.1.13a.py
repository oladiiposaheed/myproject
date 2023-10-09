def outer(par):
    loc = par

    def inner():
        return loc ** 5
    return inner

var = 3
fun = outer(var)
print(fun())