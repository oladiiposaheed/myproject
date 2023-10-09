def fun(n):
    for i in range(n):
        return i
fun(5)

def fun(n):
    for i in range(n):
        yield i

fun(6)